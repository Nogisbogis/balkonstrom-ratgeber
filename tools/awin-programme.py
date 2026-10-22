#!/usr/bin/env python3
"""AWIN-Programmstatus prüfen und data/awin.yaml schreiben.

- Token kommt NUR aus der Umgebungsvariable AWIN_API_TOKEN (Bearer). Er wird nie ausgegeben,
  geloggt oder in Dateien geschrieben.
- Fragt die Programmlisten je Beziehung ab (joined, pending, suspended, rejected, notjoined) und
  ermittelt den Status der Ziel-Advertiser sowie aller in data/powerstations.yaml und
  data/balkonkraftwerke.yaml per awin_advertiser referenzierten Advertiser.
- Nur für Advertiser mit Status joined: Provisionsgruppen (API-Werte, unverändert) und Prüfung der
  Hersteller-Produktseiten (shop_url) – erreichbar und Domain im validDomains-Bereich des Programms.
- Bewerbungen/Beitritte macht das Skript NIE (nur GET; einziges POST wäre der Link Builder – nicht genutzt).

Ausgabe: Zeilen „ÄNDERUNG …“ für inhaltliche Änderungen (Status, Shop-Erreichbarkeit).
Exit 0 = ok (Datei ggf. geschrieben), 2 = Token fehlt, 3 = API-Fehler (Datei unverändert).
Aufruf: python3 tools/awin-programme.py
"""
import datetime, json, os, re, subprocess, sys, urllib.error, urllib.parse, urllib.request
from pathlib import Path

import yaml

PUBLISHER = 3131632
API = f"https://api.awin.com/publishers/{PUBLISHER}"
ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "data" / "awin.yaml"
# Ziel-Advertiser: Schlüssel -> (bekannte ID oder None, Namensmuster)
ZIELE = {
    "anker-solix-de": (32623, r"^anker solix de$"),
    "solakon-de": (None, r"solakon"),
    "zendure-eu": (68786, r"^zendure eu"),
    "jackery-de": (30415, r"^jackery de$"),
    "alldrei-de": (28945, r"^alldrei de$"),
    "ecoflow-de": (51793, r"^ecoflow de$"),
}
NAMEN = {"solakon-de": "Solakon DE"}
BEZIEHUNGEN = ["joined", "pending", "suspended", "rejected", "notjoined"]
UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36"
HEUTE = datetime.date.today().isoformat()


class ApiFehler(Exception):
    pass


def api_get(pfad):
    token = os.environ.get("AWIN_API_TOKEN", "")
    req = urllib.request.Request(API + pfad, headers={"Authorization": "Bearer " + token, "Accept": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            return json.load(r)
    except urllib.error.HTTPError as e:
        raise ApiFehler(f"HTTP {e.code} bei {pfad.split('?')[0]}") from None
    except Exception as e:  # Netz/JSON – Meldung ohne Header
        raise ApiFehler(f"{type(e).__name__} bei {pfad.split('?')[0]}") from None


def produkte():
    out = []
    for f in ("powerstations.yaml", "balkonkraftwerke.yaml", "powerbanks.yaml"):
        for p in yaml.safe_load((ROOT / "data" / f).read_text(encoding="utf-8")) or []:
            if p.get("awin_advertiser"):
                out.append(p)
    return out


def domain_ok(url, domains):
    host = (urllib.parse.urlsplit(url).hostname or "").lower()
    for d in domains or []:
        d = (d.get("domain") if isinstance(d, dict) else d or "").lower()
        if d.startswith("*."):
            if host.endswith(d[1:]):
                return True
        elif host == d or host == "www." + d:
            return True
    return False


def shop_status(url):
    """erreichbar | nicht_erreichbar | unklar. Erst einfacher GET, bei Bot-Sperre (403/429 …)
    Fallback über echten Browser (tools/awin-shopcheck.cjs), sonst unklar."""
    try:
        req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Language": "de-DE,de;q=0.9"})
        with urllib.request.urlopen(req, timeout=30) as r:
            if r.status == 200:
                return "erreichbar"
    except urllib.error.HTTPError as e:
        if e.code in (404, 410):
            return "nicht_erreichbar"
    except Exception:
        pass
    try:
        r = subprocess.run(["node", str(ROOT / "tools" / "awin-shopcheck.cjs"), url],
                           capture_output=True, text=True, timeout=120)
        code = (r.stdout.strip().split() or ["0"])[0]
        if code == "200":
            return "erreichbar"
        if code in ("404", "410"):
            return "nicht_erreichbar"
    except Exception:
        pass
    return "unklar"


def main():
    if not os.environ.get("AWIN_API_TOKEN"):
        print("PROBLEM: AWIN_API_TOKEN ist nicht gesetzt.", file=sys.stderr)
        return 2
    alt = {}
    if OUT.exists():
        alt = yaml.safe_load(OUT.read_text(encoding="utf-8")) or {}
    alt_adv = alt.get("advertisers") or {}
    alt_shops = alt.get("shops") or {}
    prods = produkte()

    try:
        listen = {b: api_get(f"/programmes?relationship={b}") for b in BEZIEHUNGEN}
        for b, l in listen.items():
            if not isinstance(l, list):
                raise ApiFehler(f"unerwartete Antwort für relationship={b}")
        # Status je Advertiser-ID
        status, info = {}, {}
        for b in BEZIEHUNGEN:
            for p in listen[b]:
                status.setdefault(p["id"], b)
                info.setdefault(p["id"], p)
        ids = {}
        for key, (aid, muster) in ZIELE.items():
            if aid is None:
                treffer = [p for b in BEZIEHUNGEN for p in listen[b] if re.search(muster, (p.get("name") or ""), re.I)]
                aid = treffer[0]["id"] if treffer else None
            ids[key] = aid
        for p in prods:
            if int(p["awin_advertiser"]) not in ids.values():
                ids[f"id-{p['awin_advertiser']}"] = int(p["awin_advertiser"])

        adv = {}
        for key, aid in ids.items():
            if aid is None or aid not in status:
                adv[key] = {"id": aid, "name": NAMEN.get(key, key), "status": "nicht_gefunden", "domain": "", "geprueft": HEUTE}
                continue
            i = info[aid]
            dom = urllib.parse.urlsplit(i.get("displayUrl") or "").hostname or ""
            e = {"id": aid, "name": i.get("name"), "status": status[aid], "domain": dom, "geprueft": HEUTE}
            if status[aid] == "joined":
                cg = api_get(f"/commissiongroups?advertiserId={aid}")
                e["provision"] = cg.get("commissionGroups") or []  # API-Werte unverändert
            adv[key] = e
    except ApiFehler as e:
        print(f"PROBLEM: AWIN-API: {e} – data/awin.yaml bleibt unverändert.", file=sys.stderr)
        return 3

    aenderungen = []
    for key, e in adv.items():
        vorher = (alt_adv.get(key) or {}).get("status")
        if vorher != e["status"]:
            aenderungen.append(f"{e['name']} ({e['id']}): {vorher or 'neu'} → {e['status']}")

    # Shop-Seiten: nur für beigetretene Advertiser prüfen, sonst bisherigen Stand behalten
    joined = {e["id"] for e in adv.values() if e["status"] == "joined"}
    shops = {}
    for p in prods:
        slug, url, aid = p["slug"], p.get("shop_url"), int(p["awin_advertiser"])
        if not url:
            continue
        a = alt_shops.get(slug) or {}
        s = {"url": url, "advertiser": aid, "status": a.get("status", "ungeprueft") if a.get("url") == url else "ungeprueft",
             "geprueft": a.get("geprueft", "") if a.get("url") == url else ""}
        if aid in joined:
            if not domain_ok(url, info.get(aid, {}).get("validDomains")):
                neu = "domain_ungueltig"
            else:
                neu = shop_status(url)
                if neu == "unklar" and s["status"] in ("erreichbar", "nicht_erreichbar"):
                    neu = s["status"]  # bei unklarer Prüfung letzten sicheren Stand behalten
            s["geprueft"] = HEUTE
            if neu != s["status"]:
                aenderungen.append(f"Shop {p['modell']}: {s['status']} → {neu}")
            s["status"] = neu
        shops[slug] = s
    for slug in alt_shops:
        if slug not in shops:
            aenderungen.append(f"Shop {slug}: entfernt")

    daten = {"publisher": PUBLISHER, "stand": HEUTE, "advertisers": adv, "shops": shops}
    kopf = ("# Automatisch erzeugt von tools/awin-programme.py – nicht von Hand ändern (kein Token hier!).\n"
            "# advertisers.status: joined | pending | suspended | rejected | notjoined | nicht_gefunden\n"
            "# shops.status: erreichbar | nicht_erreichbar | unklar | domain_ungueltig | ungeprueft\n"
            "# AWIN-Links erscheinen nur bei advertiser joined UND shop erreichbar (layouts/_partials/awin-url.html).\n")
    OUT.write_text(kopf + yaml.safe_dump(daten, allow_unicode=True, sort_keys=False), encoding="utf-8")
    for key, e in adv.items():
        print(f"{e['name']} ({e['id']}): {e['status']}")
    for a in aenderungen:
        print("ÄNDERUNG " + a)
    return 0


if __name__ == "__main__":
    sys.exit(main())
