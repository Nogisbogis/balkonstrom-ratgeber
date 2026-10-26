#!/usr/bin/env python3
"""Strompreis-Feed: Day-Ahead-Börsenpreis DE-LU von energy-charts (Fraunhofer ISE) holen
und als kompaktes JSON nach static/api/strompreis.json schreiben (Hugo kopiert es nach /api/strompreis.json).

Läuft im Pages-Workflow vor dem Hugo-Build (Cron alle 30 min + bei jedem Push). Der Browser ruft nur
die eigene Domain ab, nie energy-charts direkt.

Zeitfenster: heute 00:00 bis morgen 23:45 Europe/Berlin (lokale Kalendertage, inkl. Zeitumstellung).
Die Werte für morgen veröffentlicht die Börse gegen 13 Uhr; vorher enthält der Feed nur heute.

Fällt die API aus, wird der zuletzt veröffentlichte Feed der Live-Seite übernommen (Werte unverändert,
as_of_unix bleibt alt). Gibt es auch den nicht, wird {"available": false} geschrieben. Der Build bricht nie ab.
Nur Standardbibliothek.
"""
import json, os, sys, time, urllib.request, urllib.parse
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

BERLIN = ZoneInfo("Europe/Berlin")
UPSTREAM = "https://api.energy-charts.info/price"
LIVE_FEED = os.environ.get("STROMPREIS_LIVE_FEED", "https://balkonstrom-ratgeber.de/api/strompreis.json")
OUT = os.environ.get("STROMPREIS_OUT", os.path.join(os.path.dirname(__file__), "..", "static", "api", "strompreis.json"))
UA = "balkonstrom-ratgeber.de strompreis-feed (+https://balkonstrom-ratgeber.de/)"


def get_json(url, timeout=30):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.load(r)


def fetch_upstream(now):
    day0 = now.astimezone(BERLIN).replace(hour=0, minute=0, second=0, microsecond=0)
    end = (day0 + timedelta(days=2)).replace(hour=0) - timedelta(minutes=15)  # morgen 23:45 lokal
    q = urllib.parse.urlencode({"bzn": "DE-LU", "start": day0.isoformat(timespec="minutes"), "end": end.isoformat(timespec="minutes")})
    last = None
    for attempt in range(3):
        try:
            d = get_json(f"{UPSTREAM}?{q}")
            ts, pr = d.get("unix_seconds"), d.get("price")
            if not isinstance(ts, list) or not isinstance(pr, list) or len(ts) != len(pr) or not ts:
                raise ValueError("unerwartete Antwort")
            if d.get("unit") != "EUR / MWh":
                raise ValueError(f"unerwartete Einheit {d.get('unit')!r}")
            return d
        except Exception as e:  # noqa: BLE001
            last = e
            time.sleep(5 * (attempt + 1))
    raise RuntimeError(f"energy-charts nicht erreichbar: {last}")


def hour_mean(slots, start):
    vals = [p for t, p in slots if start <= t < start + 3600 and p is not None]
    return sum(vals) / len(vals) if vals else None


def build(d, now):
    slots = [(int(t), (None if p is None else float(p))) for t, p in zip(d["unix_seconds"], d["price"])]
    slots.sort()
    now_s = int(now.timestamp())
    hour = now_s - now_s % 3600  # volle Stunde (Berlin ist ganzstündig zu UTC versetzt)
    cur, nxt = hour_mean(slots, hour), hour_mean(slots, hour + 3600)
    loc0 = now.astimezone(BERLIN).replace(hour=0, minute=0, second=0, microsecond=0)
    t0, t1 = int(loc0.timestamp()), int((loc0 + timedelta(days=1, hours=2)).replace(hour=0).timestamp())
    today = [p for t, p in slots if t0 <= t < t1 and p is not None]
    r = lambda x, n=2: None if x is None else round(x, n)
    return {
        "available": True,
        "bzn": "DE-LU",
        "unit": d["unit"],
        "license_info": d.get("license_info"),
        "deprecated": bool(d.get("deprecated", False)),
        "source": "energy-charts.info (Fraunhofer ISE), Daten Bundesnetzagentur | SMARD.de",
        "window": "heute 00:00 bis morgen 23:45 Europe/Berlin",
        "updated_at": now.astimezone(BERLIN).isoformat(timespec="seconds"),
        "as_of_unix": now_s,
        "current_hour_start_unix": hour,
        "current_hour_eur_per_kwh": r(None if cur is None else cur / 1000, 5),
        "current_hour_ct_per_kwh": r(None if cur is None else cur / 10),
        "next_hour_ct_per_kwh": r(None if nxt is None else nxt / 10),
        "day_min_ct": r(min(today) / 10) if today else None,
        "day_max_ct": r(max(today) / 10) if today else None,
        "unix_seconds": [t for t, _ in slots],
        "price": [p for _, p in slots],
    }


def main():
    now = datetime.now(tz=BERLIN)
    try:
        out = build(fetch_upstream(now), now)
        msg = f"ok: {len(out['price'])} Werte, aktuelle Stunde {out['current_hour_ct_per_kwh']} ct/kWh"
    except Exception as e:  # noqa: BLE001
        print(f"warn: {e}", file=sys.stderr)
        try:
            out = get_json(LIVE_FEED)
            if not out.get("available"):
                raise ValueError("Live-Feed leer")
            out["stale"] = True
            msg = "fallback: letzter Live-Feed übernommen"
        except Exception as e2:  # noqa: BLE001
            print(f"warn: kein Fallback ({e2})", file=sys.stderr)
            out = {"available": False, "updated_at": now.isoformat(timespec="seconds"), "as_of_unix": int(now.timestamp())}
            msg = "nicht verfügbar"
    os.makedirs(os.path.dirname(os.path.abspath(OUT)), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, separators=(",", ":"))
    print(msg)


if __name__ == "__main__":
    main()
