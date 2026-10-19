#!/usr/bin/env python3
"""Erzeugt die SVG-Grafiken in static/img/ aus data/*.yaml bzw. aus Werten,
die wörtlich in den Artikeln stehen. Aufruf: python3 tools/grafiken.py
Benötigt PyYAML. Keine Fremdbilder, keine Logos."""
import os, html, yaml
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "static", "img")
os.makedirs(OUT, exist_ok=True)
ps = yaml.safe_load(open(os.path.join(ROOT, "data", "powerstations.yaml"), encoding="utf-8"))
bkw = yaml.safe_load(open(os.path.join(ROOT, "data", "balkonkraftwerke.yaml"), encoding="utf-8"))

STYLE = """<style>
.bg{fill:#ffffff}.t{fill:#111111}.m{fill:#55595e}.g{stroke:#e2e2df}.ax{stroke:#111111}
.a{fill:#0a6b3d}.as{stroke:#0a6b3d}.b{fill:#9a4a00}.bs{stroke:#9a4a00}.c{fill:#1f4f8f}.cs{stroke:#1f4f8f}
.box{fill:#f1eee6;stroke:#111111}.boxa{fill:#ffffff;stroke:#0a6b3d}.boxb{fill:#ffffff;stroke:#9a4a00}
.ar{fill:#111111}.ars{stroke:#111111}.al{fill:#0a6b3d;fill-opacity:.14}.bl{fill:#9a4a00;fill-opacity:.14}
text{font-family:system-ui,-apple-system,"Segoe UI",Roboto,Arial,sans-serif}
@media (prefers-color-scheme:dark){
.bg{fill:#0f1f1a}.t{fill:#eef2ee}.m{fill:#b5c2bb}.g{stroke:#2a4a40}.ax{stroke:#eef2ee}
.a{fill:#5fd69a}.as{stroke:#5fd69a}.b{fill:#f0b45a}.bs{stroke:#f0b45a}.c{fill:#8db8f0}.cs{stroke:#8db8f0}
.box{fill:#16302a;stroke:#eef2ee}.boxa{fill:#0f1f1a;stroke:#5fd69a}.boxb{fill:#0f1f1a;stroke:#f0b45a}
.ar{fill:#eef2ee}.ars{stroke:#eef2ee}.al{fill:#5fd69a;fill-opacity:.18}.bl{fill:#f0b45a;fill-opacity:.18}}
</style>"""

def esc(s): return html.escape(str(s), quote=True)
def de(n, d=0):
    s = f"{n:,.{d}f}"
    return s.replace(",", "X").replace(".", ",").replace("X", ".")

def deg(n, maxd=3):
    s = f"{n:.{maxd}f}".rstrip("0").rstrip(".")
    return de(float(s), len(s.split(".")[1]) if "." in s else 0)

def svg(name, w, h, title, desc, body):
    out = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" '
           f'role="img" aria-labelledby="t d" lang="de">\n<title id="t">{esc(title)}</title>\n'
           f'<desc id="d">{esc(desc)}</desc>\n{STYLE}\n<rect class="bg" width="{w}" height="{h}" rx="8"/>\n'
           + "\n".join(body) + "\n</svg>\n")
    with open(os.path.join(OUT, name), "w", encoding="utf-8") as f: f.write(out)
    print("geschrieben", name, len(out), "Bytes")

def T(x, y, s, cls="t", size=13, anchor="start", weight="normal", extra=""):
    return (f'<text x="{x}" y="{y}" class="{cls}" font-size="{size}" text-anchor="{anchor}" '
            f'font-weight="{weight}" {extra}>{esc(s)}</text>')
def R(x, y, w, h, cls, rx=0, extra=""): return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" class="{cls}" rx="{rx}" {extra}/>'
def L(x1, y1, x2, y2, cls="g", sw=1, extra=""): return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" class="{cls}" stroke-width="{sw}" {extra}/>'

def short(m): return m.replace("Anker SOLIX ", "Anker ").replace("Jackery Explorer ", "Jackery ")

# ---------- 1) Powerstations: Kapazität und Gewicht (Butterfly) ----------
def ps_kapazitaet_gewicht(name="ps-kapazitaet-gewicht.svg"):
    rows = sorted(ps, key=lambda p: (p["kapazitaet_wh"], p["gewicht_kg"]))
    W, top, rh = 760, 78, 30
    H = top + rh * len(rows) + 58
    lab_w, cx = 190, 470          # Label-Spalte, Mittelachse
    left_w, right_w = cx - lab_w - 10 - 6, W - cx - 6 - 70
    maxwh = 2200; maxkg = 20
    b = [T(20, 30, "Kapazität und Gewicht laut Hersteller", size=18, weight="bold"),
         T(20, 52, "Links: Kapazität in Wh · rechts: Gewicht in kg · Zahl rechts: Wh pro kg (berechnet)", "m", 12.5),
         T(cx - 6, top - 8, "Kapazität (Wh)", "a", 12, "end", "bold"),
         T(cx + 6, top - 8, "Gewicht (kg)", "b", 12, "start", "bold"),
         T(W - 20, top - 8, "Wh/kg", "m", 12, "end", "bold")]
    for i, p in enumerate(rows):
        y = top + i * rh
        wh, kg = p["kapazitaet_wh"], p["gewicht_kg"]
        lw = left_w * wh / maxwh; rw = right_w * kg / maxkg
        b.append(T(20, y + 19, short(p["modell"]), size=13))
        b.append(R(cx - 6 - lw, y + 6, lw, rh - 12, "a", 2))
        b.append(T(cx - 10 - lw, y + 19.5, de(wh), "t", 12, "end"))
        b.append(R(cx + 6, y + 6, rw, rh - 12, "b", 2))
        b.append(T(cx + 10 + rw, y + 19.5, deg(kg, 2), "t", 12))
        b.append(T(W - 20, y + 19.5, de(wh / kg, 0), "m", 12, "end"))
    yb = top + rh * len(rows)
    b.append(L(cx, top - 2, cx, yb + 2, "ax"))
    b.append(T(20, yb + 26, "Quelle: Herstellerangaben, Stand 19.10.2026 (Links im Vergleich). Wh/kg = Kapazität ÷ Gewicht, gerundet.", "m", 11.5))
    b.append(T(20, yb + 44, "Balkenlängen: Kapazität bis 2.200 Wh, Gewicht bis 20 kg.", "m", 11.5))
    svg(name, W, H, "Kapazität und Gewicht der Powerstations im Vergleich",
        "Balkendiagramm mit " + str(len(rows)) + " Powerstations. " +
        "; ".join(f'{p["modell"]}: {de(p["kapazitaet_wh"])} Wh, {de(p["gewicht_kg"],2)} kg' for p in rows) + ".", b)

# ---------- 2) Powerstations: Dauerleistung ----------
def ps_dauerleistung(name="ps-dauerleistung.svg"):
    rows = sorted(ps, key=lambda p: (p["dauerleistung_w"], p["kapazitaet_wh"]))
    W, top, rh = 760, 78, 30
    H = top + rh * len(rows) + 62
    x0, x1, maxw = 200, 690, 2500
    sx = lambda v: x0 + (x1 - x0) * v / maxw
    b = [T(20, 30, "Dauerleistung am 230-V-Ausgang laut Hersteller", size=18, weight="bold"),
         T(20, 52, "Nennleistung ohne Boost- oder Spitzenleistung, in Watt", "m", 12.5)]
    for v in range(0, maxw + 1, 500):
        b.append(L(sx(v), top - 4, sx(v), top + rh * len(rows), "g"))
        b.append(T(sx(v), top + rh * len(rows) + 16, de(v), "m", 11, "middle"))
    xr = sx(1000)
    b.append(L(xr, top - 14, xr, top + rh * len(rows), "bs", 2, 'stroke-dasharray="5 4"'))
    b.append(T(xr + 6, top - 4, "1.000 W: Geräte mit Heizelement liegen oft darüber", "b", 11.5))
    for i, p in enumerate(rows):
        y = top + i * rh
        v = p["dauerleistung_w"]
        b.append(T(20, y + 19, short(p["modell"]), size=13))
        b.append(R(x0, y + 6, sx(v) - x0, rh - 12, "a", 2))
        b.append(T(sx(v) + 6, y + 19.5, de(v) + " W", "t", 12))
    yb = top + rh * len(rows)
    b.append(T(20, yb + 38, "Quelle: Herstellerangaben, Stand 19.10.2026. Wasserkocher, Föhn, Kaffeemaschine: oft über 1.000 W (siehe Text).", "m", 11.5))
    b.append(T(20, yb + 54, "Die Leistung aller gleichzeitig laufenden Geräte muss unter der Dauerleistung liegen.", "m", 11.5))
    svg(name, W, H, "Dauerleistung der Powerstations im Vergleich",
        "Balkendiagramm der Dauerleistung: " + "; ".join(f'{p["modell"]} {de(p["dauerleistung_w"])} W' for p in rows) +
        ". Eine gestrichelte Linie markiert 1.000 Watt.", b)

# ---------- 3) Powerstations: Was läuft wie lange? ----------
def ps_laufzeit(name="ps-laufzeit.svg"):
    caps = [(min(p["kapazitaet_wh"] for p in ps), None), (1024, None), (max(p["kapazitaet_wh"] for p in ps), None)]
    # Dauerleistung der jeweiligen Klasse (kleinste Dauerleistung der Geräte mit genau dieser Kapazität)
    def dl(wh): return min(p["dauerleistung_w"] for p in ps if p["kapazitaet_wh"] == wh)
    caps = [(wh, dl(wh)) for wh, _ in caps]
    devices = [("LED-Lampe", 10), ("Kompressor-Kühlbox (Mittelwert)", 40), ("Laptop", 60), ("Kaffeemaschine", 1000)]
    W, top = 760, 92
    groupH = 3 * 24 + 26
    H = top + groupH * len(devices) + 66
    x0, x1 = 300, 590
    colors = ["a", "c", "b"]
    b = [T(20, 30, "Was läuft wie lange? Rechnerische Laufzeit", size=18, weight="bold"),
         T(20, 52, "Kapazität laut Hersteller ÷ Geräteleistung. Geräteleistungen sind Beispielwerte, keine Messwerte.", "m", 12.5),
         T(20, 70, "Umwandlungsverluste sind nicht abgezogen – die reale Laufzeit ist kürzer.", "b", 12.5, weight="bold")]
    lx = 400
    for k, (wh, d) in enumerate(caps):
        b.append(R(lx + k * 120, top - 18, 12, 12, colors[k], 2))
        b.append(T(lx + k * 120 + 17, top - 8, f"{de(wh)} Wh", "t", 12))
    for j, (dev, w) in enumerate(devices):
        gy = top + j * groupH
        b.append(T(20, gy + 26, dev, size=13.5, weight="bold"))
        b.append(T(20, gy + 44, f"Beispielwert: {de(w)} W", "m", 12))
        hours = [wh / w for wh, _ in caps]
        mx = max(hours)
        for k, (wh, d) in enumerate(caps):
            y = gy + 8 + k * 24
            if w > d:
                b.append(T(x0, y + 15, f"läuft nicht – Dauerleistung nur {de(d)} W", "m", 12, extra='font-style="italic"'))
                continue
            h = wh / w
            bw = (x1 - x0) * h / mx
            b.append(R(x0, y + 3, max(bw, 2), 16, colors[k], 2))
            lab = f"≈ {de(h, 1 if h < 10 else 0)} h"
            if h >= 48: lab += f" (≈ {de(h/24, 1)} Tage)"
            b.append(T(x0 + max(bw, 2) + 6, y + 16, lab, "t", 12))
        b.append(L(20, gy + groupH - 4, W - 20, gy + groupH - 4, "g"))
    yb = top + groupH * len(devices)
    b.append(T(20, yb + 20, f"Kapazitäten: kleinstes Gerät ({de(caps[0][0])} Wh), 1-kWh-Klasse ({de(caps[1][0])} Wh), größtes Gerät ({de(caps[2][0])} Wh) im Vergleich.", "m", 11.5))
    b.append(T(20, yb + 37, "„Läuft nicht“: Die Geräteleistung liegt über der Dauerleistung der kleinsten Powerstation dieser Kapazität.", "m", 11.5))
    b.append(T(20, yb + 54, "Kühlboxen: Verbrauch pro 24 h aus dem Datenblatt ist genauer als ein Mittelwert.", "m", 11.5))
    desc = []
    for dev, w in devices:
        parts = []
        for wh, d in caps:
            parts.append(f"{de(wh)} Wh: " + ("läuft nicht" if w > d else f"etwa {de(wh/w,1)} Stunden"))
        desc.append(f"{dev} mit Beispielwert {w} W – " + ", ".join(parts))
    svg(name, W, H, "Was läuft wie lange? Rechnerische Laufzeiten ohne Umwandlungsverluste", "; ".join(desc) + ".", b)

# ---------- 4) Speicher: Schema ----------
def arrow(x1, y1, x2, y2, cls="ars", sw=2.5, dash=None):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" class="{cls}" stroke-width="{sw}" marker-end="url(#pf)"{d}/>'
DEFS = '<defs><marker id="pf" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" class="ar"/></marker></defs>'

def box(x, y, w, h, cls, lines, size=13.5):
    o = [R(x, y, w, h, cls, 8, 'stroke-width="1.5"')]
    n = len(lines); cy = y + h / 2 - (n - 1) * 9
    for i, (s, c, wt) in enumerate(lines):
        o.append(T(x + w / 2, cy + i * 18 + 5, s, c, size if wt == "bold" else 12, "middle", wt))
    return o

def speicher_schema(name="speicher-schema.svg"):
    W, H = 760, 400
    b = [DEFS, T(20, 30, "So arbeitet ein Balkonkraftwerk mit Speicher", size=18, weight="bold"),
         T(20, 52, "Schematische Darstellung eines All-in-one-Systems (Speicher mit integriertem Wechselrichter)", "m", 12.5)]
    b += box(20, 90, 150, 76, "box", [("Solarmodule", "t", "bold"), ("Gleichstrom", "m", "normal"), ("max. 2.000 Wp*", "m", "normal")])
    b += box(240, 74, 200, 108, "boxa", [("Speicher mit", "t", "bold"), ("Wechselrichter", "t", "bold"), ("lädt mit Überschuss", "m", "normal"), ("gibt max. 800 W ab", "m", "normal")])
    b += box(520, 90, 220, 76, "box", [("Hausnetz", "t", "bold"), ("Kühlschrank, Router,", "m", "normal"), ("Waschmaschine …", "m", "normal")])
    b += box(520, 250, 220, 76, "boxb", [("Öffentliches Netz", "t", "bold"), ("Überschuss: keine", "m", "normal"), ("Vergütung**", "m", "normal")])
    b += box(240, 250, 200, 76, "box", [("Off-Grid-Steckdose", "t", "bold"), ("nur direkt angeschlossene", "m", "normal"), ("Geräte bei Stromausfall", "m", "normal")])
    b.append(arrow(172, 128, 236, 128))
    b.append(arrow(442, 128, 516, 128))
    b.append(T(479, 118, "≤ 800 W", "m", 11.5, "middle"))
    b.append(arrow(630, 168, 630, 246))
    b.append(T(622, 204, "nicht verbrauchter", "m", 11.5, "end")); b.append(T(622, 220, "Strom", "m", 11.5, "end"))
    b.append(arrow(340, 184, 340, 246, dash="5 4"))
    b.append(T(348, 220, "optional", "m", 11.5))
    b.append(box(20, 250, 150, 76, "box", [("Smart Meter / Lesekopf", "t", "bold"), ("optional: regelt nach", "m", "normal"), ("aktuellem Verbrauch", "m", "normal")], 12.5)[0])
    b += box(20, 250, 150, 76, "box", [("Smart Meter", "t", "bold"), ("optional: regelt", "m", "normal"), ("nach Verbrauch", "m", "normal")])[1:]
    b.append(f'<path d="M172 288 C 205 288 205 182 250 182" fill="none" class="ars" stroke-width="2" stroke-dasharray="5 4" marker-end="url(#pf)"/>')
    b.append(T(20, 360, "* Grenze für den vereinfachten Betrieb als Steckersolargerät; Wechselrichter höchstens 800 VA laut Typenschild.", "m", 11.5))
    b.append(T(20, 378, "** Bei der Sonderregelung für Steckersolargeräte „unentgeltliche Abnahme“ (Bundeswirtschaftsministerium).", "m", 11.5))
    svg(name, W, H, "Schema: Solarmodule, Speicher mit Wechselrichter, Hausnetz und öffentliches Netz",
        "Schematische Darstellung: Solarmodule liefern Gleichstrom an einen Speicher mit integriertem Wechselrichter. "
        "Dieser gibt höchstens 800 Watt ins Hausnetz ab. Nicht verbrauchter Strom fließt ohne Vergütung ins öffentliche Netz. "
        "Optional versorgt eine Off-Grid-Steckdose direkt angeschlossene Geräte, und ein Smart Meter regelt die Abgabe nach dem Verbrauch.", b)

# ---------- 5) Speicher: Tagesprofil (schematisch) ----------
def speicher_tagesprofil(name="speicher-tagesprofil.svg"):
    import math
    W, H = 760, 380
    x0, x1, y0, y1 = 70, 730, 300, 90     # Achsen: Stunden 0..24
    sx = lambda h: x0 + (x1 - x0) * h / 24
    def prod(h):  # Glockenkurve 6–20 Uhr, rein schematisch
        return max(0.0, math.sin(math.pi * (h - 6) / 14)) ** 1.6 if 6 <= h <= 20 else 0.0
    def cons(h):  # Grundlast + Morgen- und Abendspitze, schematisch
        return 0.16 + 0.32 * math.exp(-((h - 7.2) / 1.1) ** 2) + 0.45 * math.exp(-((h - 19.5) / 1.8) ** 2) + 0.10 * math.exp(-((h - 12.5) / 1.0) ** 2)
    sy = lambda v: y0 - (y0 - y1) * v
    hs = [i / 10 for i in range(0, 241)]
    pp = " ".join(f"{sx(h):.1f},{sy(prod(h)):.1f}" for h in hs)
    cp = " ".join(f"{sx(h):.1f},{sy(cons(h)):.1f}" for h in hs)
    # Flächen: Überschuss (prod>cons) und Defizit am Abend (cons>prod, h>=14)
    def area(f, g, cond):
        segs, cur = [], []
        for h in hs:
            if cond(h) and f(h) > g(h): cur.append(h)
            elif cur: segs.append(cur); cur = []
        if cur: segs.append(cur)
        out = []
        for s in segs:
            up = " ".join(f"{sx(h):.1f},{sy(f(h)):.1f}" for h in s)
            dn = " ".join(f"{sx(h):.1f},{sy(g(h)):.1f}" for h in reversed(s))
            out.append(f'<polygon points="{up} {dn}" class="{{c}}"/>')
        return out
    b = [T(20, 30, "Tagesverlauf: Erzeugung und Verbrauch", size=18, weight="bold"),
         T(20, 52, "Schematische Darstellung – keine Messwerte, ohne Zahlenskala. Der Verlauf ändert sich mit Wetter, Jahreszeit und Haushalt.", "m", 12.5)]
    b += [a.replace("{c}", "al") for a in area(prod, cons, lambda h: True)]
    b += [a.replace("{c}", "bl") for a in area(cons, prod, lambda h: 14 <= h <= 24)]
    for h in range(0, 25, 3):
        b.append(L(sx(h), y1 - 6, sx(h), y0, "g"))
        b.append(T(sx(h), y0 + 18, f"{h} Uhr", "m", 11.5, "middle"))
    b.append(L(x0, y0, x1, y0, "ax")); b.append(L(x0, y1 - 10, x0, y0, "ax"))
    b.append(T(x0 - 8, y1 + 4, "Leistung", "m", 11.5, "end"))
    b.append(f'<polyline points="{pp}" fill="none" class="as" stroke-width="3"/>')
    b.append(f'<polyline points="{cp}" fill="none" class="bs" stroke-width="3" stroke-dasharray="7 4"/>')
    b.append(T(sx(12.6), sy(prod(12.6)) - 10, "Erzeugung der Module", "a", 12.5, "middle", "bold"))
    b.append(T(sx(12.9), sy(0.42), "Überschuss → lädt den Speicher", "t", 12, "middle"))
    b.append(T(sx(20.3), sy(cons(19.6)) - 12, "Verbrauch im Haushalt", "b", 12.5, "middle", "bold"))
    b.append(T(sx(20.1), sy(0.1), "Speicher gibt ab", "t", 12, "middle"))
    b.append(R(20, 334, 14, 12, "al", 2)); b.append(T(40, 345, "Überschuss: ohne Speicher ginge er unvergütet ins Netz", "m", 12))
    b.append(R(400, 334, 14, 12, "bl", 2)); b.append(T(420, 345, "Bedarf am Abend: kann aus dem Speicher kommen", "m", 12))
    b.append(T(20, 368, "Ein Teil der Energie geht beim Laden und Entladen verloren; der Speicher erzeugt keinen zusätzlichen Strom.", "m", 11.5))
    svg(name, W, H, "Schematischer Tagesverlauf von Solarerzeugung und Haushaltsverbrauch",
        "Schematische Darstellung ohne Messwerte: Die Erzeugung der Module steigt am Morgen, erreicht mittags ihr Maximum und fällt bis zum Abend. "
        "Der Verbrauch hat eine Spitze am Morgen und eine größere am Abend. Mittags ist die Erzeugung höher als der Verbrauch – dieser Überschuss lädt den Speicher. "
        "Am Abend ist der Verbrauch höher als die Erzeugung – dann gibt der Speicher Energie ab.", b)

# ---------- 6) Speicher: Beispielrechnung ----------
def speicher_rechnung(name="speicher-beispielrechnung.svg"):
    kwh, tage, eta, preis = 1.92, 200, 0.9, 0.35          # Annahmen aus dem Artikel
    jahr_kwh = kwh * tage * eta; jahr_eur = jahr_kwh * preis
    lo, hi = 700, 1000                                   # Preisspanne Stiftung Warentest
    W, H = 760, 440
    b = [T(20, 30, "Beispielrechnung: Wann ist der Speicher abbezahlt?", size=18, weight="bold"),
         T(20, 52, "Alle Werte sind Annahmen aus dem Text – keine Messwerte, keine Prognose.", "b", 12.5, weight="bold")]
    # Rechenweg
    steps = [(f"{de(kwh,2)} kWh", "Kapazität"), (f"× {tage} Tage", "volle Zyklen/Jahr"), (f"× {de(eta*100)} %", "nach Verlusten"),
             (f"≈ {de(jahr_kwh)} kWh", "pro Jahr"), (f"× {de(preis*100)} ct", "pro kWh"), (f"≈ {de(jahr_eur)} €", "Ersparnis/Jahr")]
    bx = 20; bw = 113; gap = 6
    for i, (v, l) in enumerate(steps):
        cls = "boxa" if i in (3, 5) else "box"
        b.append(R(bx + i * (bw + gap), 70, bw, 54, cls, 6, 'stroke-width="1.2"'))
        b.append(T(bx + i * (bw + gap) + bw / 2, 93, v, "t", 14, "middle", "bold"))
        b.append(T(bx + i * (bw + gap) + bw / 2, 112, l, "m", 11.5, "middle"))
    # Chart kumulierte Ersparnis 0..10 Jahre
    x0, x1, y0, y1 = 80, 720, 370, 160
    ymax = 1300
    sx = lambda j: x0 + (x1 - x0) * j / 10
    sy = lambda v: y0 - (y0 - y1) * v / ymax
    for v in range(0, ymax + 1, 250):
        b.append(L(x0, sy(v), x1, sy(v), "g")); b.append(T(x0 - 6, sy(v) + 4, de(v) + " €", "m", 11, "end"))
    for j in range(0, 11):
        b.append(T(sx(j), y0 + 17, str(j), "m", 11, "middle"))
    b.append(T((x0 + x1) / 2, y0 + 34, "Jahre", "m", 11.5, "middle"))
    b.append(R(x0, sy(hi), x1 - x0, sy(lo) - sy(hi), "bl"))
    b.append(L(x0, sy(lo), x1, sy(lo), "bs", 1.5, 'stroke-dasharray="5 4"'))
    b.append(L(x0, sy(hi), x1, sy(hi), "bs", 1.5, 'stroke-dasharray="5 4"'))
    b.append(T(x0 + 8, sy(hi) - 6, "Kaufpreis-Spanne laut Stiftung Warentest: ca. 700–1.000 € (Stand Feb. 2026)", "b", 12, weight="bold"))
    b.append(f'<line x1="{sx(0)}" y1="{sy(0)}" x2="{sx(10)}" y2="{sy(jahr_eur*10)}" class="as" stroke-width="3"/>')
    b.append(T(sx(6.2), sy(400), f"kumulierte Ersparnis (≈ {de(jahr_eur)} € pro Jahr)", "a", 12, "start", "bold"))
    for p in (lo, hi):
        j = p / jahr_eur
        b.append(f'<circle cx="{sx(j):.1f}" cy="{sy(p):.1f}" r="5" class="a"/>')
        b.append(T(sx(j) + 8, sy(p) + 16, f"≈ {de(j,1)} Jahre", "t", 12))
    b.append(L(x0, y0, x1, y0, "ax"))
    b.append(T(20, 428, "Ergibt etwa 6 bis 8 Jahre nur für den Speicher. Weniger volle Zyklen (z. B. im Winter) verlängern die Zeit deutlich.", "m", 11.5))
    svg(name, W, H, "Beispielrechnung zur Amortisation eines Balkonkraftwerk-Speichers",
        f"Rechenweg mit Annahmen aus dem Text: {de(kwh,2)} kWh mal {tage} Tage mal 90 Prozent ergibt etwa {de(jahr_kwh)} kWh pro Jahr, "
        f"bei 35 Cent pro kWh etwa {de(jahr_eur)} Euro Ersparnis pro Jahr. Ein Liniendiagramm zeigt die kumulierte Ersparnis über zehn Jahre; "
        f"sie erreicht 700 Euro nach etwa {de(lo/jahr_eur,1)} und 1.000 Euro nach etwa {de(hi/jahr_eur,1)} Jahren.", b)

# ---------- 7) Anmelden: Ablauf ----------
def anmelden_ablauf(name="anmelden-ablauf.svg"):
    W = 760
    steps = [
        ("1", "Gerät prüfen", ["Wechselrichter ≤ 800 VA laut Typenschild", "Module ≤ 2.000 W (Schuko: ≤ 960 W, DIN VDE V 0126-95)"]),
        ("2", "Zustimmung einholen", ["Mieter: Vermieter fragen (§ 554 BGB)", "Eigentümer: Gemeinschaft fragen (§ 20 Abs. 2 Nr. 5 WEG)"]),
        ("3", "Montieren und anschließen", ["Sicher montieren (Wind, Schnee), passende Steckdose,", "keine Mehrfachsteckdose; Stromkreis ggf. prüfen lassen"]),
        ("4", "Im Marktstammdatenregister registrieren", ["innerhalb eines Monats nach Inbetriebnahme", "Netzbetreiber-Meldung fürs Balkonkraftwerk entfällt"]),
        ("5", "Zählertausch abwarten", ["Messstellenbetreiber prüft und tauscht bei Bedarf –", "im Regelfall kostenlos für dich"]),
    ]
    top, bh, gap = 70, 74, 26
    H = top + len(steps) * (bh + gap) + 30
    bx, bw = 20, 440
    b = [DEFS, T(20, 30, "Balkonkraftwerk in Betrieb nehmen: Schritt für Schritt", size=18, weight="bold"),
         T(20, 52, "Ablauf laut Bundeswirtschaftsministerium, Bundesnetzagentur, Umweltbundesamt und VDE (Stand Okt. 2026)", "m", 12.5)]
    for i, (n, head, lines) in enumerate(steps):
        y = top + i * (bh + gap)
        b.append(R(bx, y, bw, bh, "boxa" if i == 3 else "box", 8, 'stroke-width="1.5"'))
        b.append(f'<circle cx="{bx+28}" cy="{y+bh/2}" r="15" class="a"/>')
        b.append(T(bx + 28, y + bh / 2 + 5, n, "bg", 15, "middle", "bold"))
        b.append(T(bx + 54, y + 24, head, "t", 14.5, weight="bold"))
        for k, l in enumerate(lines):
            b.append(T(bx + 54, y + 44 + k * 17, l, "m", 12))
        if i < len(steps) - 1:
            b.append(arrow(bx + bw / 2, y + bh + 2, bx + bw / 2, y + bh + gap - 3, sw=2))
    # Speicher-Abzweig an Schritt 4
    y4 = top + 3 * (bh + gap)
    b.append(arrow(bx + bw + 2, y4 + bh / 2, 556, y4 + bh / 2, sw=2))
    b.append(T((bx + bw + 556) / 2, y4 + bh / 2 - 8, "mit Speicher?", "m", 11.5, "middle"))
    b += box(560, y4 - 8, 180, bh + 16, "boxb", [("Speicher", "t", "bold"), ("im Register mit angeben", "m", "normal"), ("und beim Netzbetreiber", "m", "normal"), ("anmelden (BMWE)", "m", "normal")])
    b.append(T(20, H - 12, "Keine Rechtsberatung. Details und Quellen im Artikel.", "m", 11.5))
    svg(name, W, H, "Ablaufdiagramm: Balkonkraftwerk anmelden und in Betrieb nehmen",
        "Fünf Schritte: 1. Gerät prüfen – Wechselrichter höchstens 800 VA laut Typenschild, Module höchstens 2.000 Watt, für Schuko höchstens 960 Watt und DIN VDE V 0126-95. "
        "2. Zustimmung von Vermieter oder Eigentümergemeinschaft einholen. 3. Sicher montieren und passend anschließen. "
        "4. Innerhalb eines Monats im Marktstammdatenregister registrieren; mit Speicher diesen angeben und zusätzlich beim Netzbetreiber anmelden. "
        "5. Zählertausch durch den Messstellenbetreiber abwarten, im Regelfall kostenlos.", b)

# ---------- 8) Anmelden: Modulleistung und Anschluss ----------
def anmelden_stecker(name="anmelden-modulleistung-anschluss.svg"):
    W, H = 760, 270
    x0, x1 = 30, 730; mx = 2400
    sx = lambda v: x0 + (x1 - x0) * v / mx
    y, h = 110, 46
    b = [T(20, 30, "Modulleistung und Anschluss: was gilt?", size=18, weight="bold"),
         T(20, 52, "Summe der Modulleistung (Wp), Wechselrichter jeweils höchstens 800 VA laut Typenschild", "m", 12.5)]
    b.append(R(sx(0), y, sx(960) - sx(0), h, "boxa", 0, 'stroke-width="1.5"'))
    b.append(R(sx(960), y, sx(2000) - sx(960), h, "boxb", 0, 'stroke-width="1.5"'))
    b.append(R(sx(2000), y, sx(mx) - sx(2000), h, "box", 0, 'stroke-width="1.5"'))
    b.append(T((sx(0) + sx(960)) / 2, y + 20, "Schuko-Steckdose möglich", "t", 13, "middle", "bold"))
    b.append(T((sx(0) + sx(960)) / 2, y + 37, "mit Gerät nach DIN VDE V 0126-95", "m", 11.5, "middle"))
    b.append(T((sx(960) + sx(2000)) / 2, y + 20, "Energiesteckvorrichtung (z. B. Wieland)", "t", 13, "middle", "bold"))
    b.append(T((sx(960) + sx(2000)) / 2, y + 37, "oder Festanschluss durch Elektrofachkraft", "m", 11.5, "middle"))
    b.append(T((sx(2000) + sx(mx)) / 2, y + 20, "reguläre", "t", 13, "middle", "bold"))
    b.append(T((sx(2000) + sx(mx)) / 2, y + 37, "PV-Anlage", "t", 13, "middle", "bold"))
    for v in (0, 960, 2000):
        b.append(L(sx(v), y - 10, sx(v), y + h + 10, "ax", 1.5))
        b.append(T(sx(v), y + h + 28, de(v) + " Wp", "t", 12.5, "middle" if v else "start", "bold"))
    b.append(T(sx(480), y - 16, "bis 960 Wp = 800 W + 20 %, etwa zwei Standardmodule", "m", 11.5, "middle"))
    b.append(T(sx(1480), y - 16, "Steckersolargerät, vereinfachte Regeln", "m", 11.5, "middle"))
    b.append(T(20, 226, "Quelle: DIN VDE V 0126-95:2025-12 (VDE), EEG nach Solarpaket I. Schuko zusätzlich nur mit sichergestelltem Basisschutz.", "m", 11.5))
    b.append(T(20, 244, "Skala bis 2.400 Wp nur zur Darstellung. Keine Rechtsberatung.", "m", 11.5))
    svg(name, W, H, "Welche Steckverbindung bei welcher Modulleistung",
        "Skala der Modulleistung: Bis 960 Wp ist der Anschluss an eine Schuko-Steckdose normgerecht, wenn das Gerät DIN VDE V 0126-95 erfüllt. "
        "Über 960 bis 2.000 Wp braucht es eine Energiesteckvorrichtung wie den Wieland-Stecker oder einen Festanschluss. "
        "Über 2.000 Wp gilt die Anlage als reguläre PV-Anlage. Der Wechselrichter darf jeweils höchstens 800 VA haben.", b)

# ---------- 9) Anmelden: Angaben im MaStR ----------
def anmelden_mastr(name="anmelden-mastr-angaben.svg"):
    W, H = 760, 250
    items = [("Standort", "der Anlage"), ("Datum", "der Inbetriebnahme"), ("Modulleistung", "gesamt in Watt"),
             ("Wechselrichter", "Leistung"), ("Zählernummer", "deines Stromzählers")]
    b = [T(20, 30, "Diese 5 Angaben fragt das Marktstammdatenregister ab", size=18, weight="bold"),
         T(20, 52, "Registrierung innerhalb eines Monats nach Inbetriebnahme, mit Benutzerkonto im Register", "m", 12.5)]
    cw, gap = 136, 10
    for i, (h1, h2) in enumerate(items):
        x = 20 + i * (cw + gap)
        b.append(R(x, 76, cw, 100, "box", 8, 'stroke-width="1.5"'))
        b.append(f'<circle cx="{x+cw/2}" cy="104" r="15" class="a"/>')
        b.append(T(x + cw / 2, 109, str(i + 1), "bg", 15, "middle", "bold"))
        b.append(T(x + cw / 2, 142, h1, "t", 13.5, "middle", "bold"))
        b.append(T(x + cw / 2, 161, h2, "m", 11.5, "middle"))
    b.append(R(20, 190, 720, 34, "boxb", 6, 'stroke-width="1.2"'))
    b.append(T(32, 212, "Mit Speicher: Frage nach dem Stromspeicher mit „Ja“ beantworten und dessen Daten angeben.", "t", 12.5))
    b.append(T(20, 243, "Quelle: Bundesnetzagentur, Registrierungshilfe für Balkonkraftwerke; Bundeswirtschaftsministerium.", "m", 11.5))
    svg(name, W, 250 + 4, "Die fünf Angaben bei der Registrierung im Marktstammdatenregister",
        "Fünf Karten: 1. Standort der Anlage, 2. Datum der Inbetriebnahme, 3. Gesamtleistung der Module in Watt, "
        "4. Leistung des Wechselrichters, 5. Nummer des Stromzählers. Hinweis: Mit Speicher die Frage nach dem Stromspeicher mit Ja beantworten und dessen Daten angeben.", b)

# ---------- 10) Vergleich: Balkonkraftwerk-Speicher ----------
def bkw_speicher(name="vergleich-bkw-speicher.svg"):
    rows = [p for p in bkw if p["speicher_kwh"]]
    rows.sort(key=lambda p: (p["speicher_kwh"], p["pv_max_w"]))
    W, top, rh = 760, 84, 34
    H = top + rh * len(rows) + 64
    lab = 230; cx = 470
    lw = cx - lab - 70; rw = W - cx - 90
    mk, mp = 3.0, 4000
    b = [T(20, 30, "Speicher fürs Balkonkraftwerk: Kapazität und PV-Eingang", size=18, weight="bold"),
         T(20, 52, "Herstellerangaben · Ausgang ins Hausnetz bei allen: 800 W", "m", 12.5),
         T(cx - 8, top - 8, "Speicher (kWh)", "a", 12, "end", "bold"), T(cx + 8, top - 8, "max. PV-Eingang (W)", "c", 12, "start", "bold")]
    x2000 = cx + 8 + rw * 2000 / mp
    for i, p in enumerate(rows):
        y = top + i * rh
        k, pv = p["speicher_kwh"], p["pv_max_w"]
        b.append(T(20, y + 21, short(p["modell"]).replace("Anker Solarbank", "Anker Solarbank"), size=13))
        a = lw * k / mk
        b.append(R(cx - 8 - a, y + 8, a, rh - 16, "a", 2))
        b.append(T(cx - 12 - a, y + 21.5, deg(k, 3), "t", 12, "end"))
        c = rw * pv / mp
        b.append(R(cx + 8, y + 8, c, rh - 16, "c", 2))
        b.append(T(cx + 12 + c, y + 21.5, de(pv), "t", 12))
    yb = top + rh * len(rows)
    b.append(L(cx, top - 2, cx, yb + 2, "ax"))
    b.append(L(x2000, top - 2, x2000, yb + 4, "bs", 2, 'stroke-dasharray="5 4"'))
    b.append(T(x2000, yb + 18, "2.000 Wp: Grenze für Steckersolargeräte", "b", 11.5, "middle", "bold"))
    b.append(T(20, yb + 40, "Ein höherer PV-Eingang ist technisch möglich, für den vereinfachten Betrieb zählen aber höchstens 2.000 Wp Module.", "m", 11.5))
    b.append(T(20, yb + 56, "Quelle: Herstellerangaben, Stand 19.10.2026, Links in der Tabelle.", "m", 11.5))
    svg(name, W, H, "Kapazität und maximaler PV-Eingang der Balkonkraftwerk-Speicher",
        "Balkendiagramm: " + "; ".join(f'{p["modell"]}: {de(p["speicher_kwh"],3)} kWh, PV-Eingang {de(p["pv_max_w"])} W' for p in rows) +
        ". Eine gestrichelte Linie markiert die 2.000-Wp-Grenze für Steckersolargeräte.", b)

# ---------- Favicon ----------
def favicon():
    s = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="8" fill="#111111"/>'
         '<rect x="8" y="46" width="48" height="6" fill="#4cd38a"/>'
         '<path d="M12 40 L20 14 H52 L44 40 Z" fill="#ffffff"/>'
         '<path d="M30 14 L26 40 M41 14 L35 40 M16 27 H48" stroke="#111111" stroke-width="2.6" fill="none"/></svg>\n')
    open(os.path.join(ROOT, "static", "favicon.svg"), "w").write(s)

if __name__ == "__main__":
    ps_kapazitaet_gewicht(); ps_dauerleistung(); ps_laufzeit()
    speicher_schema(); speicher_tagesprofil(); speicher_rechnung()
    anmelden_ablauf(); anmelden_stecker(); anmelden_mastr()
    bkw_speicher(); favicon()

# ---------- Titelillustrationen (selbst gezeichnet, generisch, keine Produkte) ----------
ILLU_STYLE = """<style>
.sky{fill:#e6f1ea}.sun{fill:#f2b84b}.wall{fill:#d9cdb8}.rail{fill:#7d8a83}.pan{fill:#24456b}.cell{stroke:#7fa2c8}
.grass{fill:#9cc49a}.tent{fill:#0b7a4b}.tent2{fill:#08603b}.bat{fill:#5b6b75}.batl{fill:#4fd197}.doc{fill:#ffffff;stroke:#5b6b75}
.ln{stroke:#5b6b75}.chk{stroke:#0b7a4b}.hill{fill:#b9d6bd}.plant{fill:#3f8a5a}.pot{fill:#b5653a}
@media (prefers-color-scheme:dark){.sky{fill:#16302a}.sun{fill:#e8b04f}.wall{fill:#3a362e}.rail{fill:#9fb0a8}.pan{fill:#2c5a8c}
.cell{stroke:#9cc0e6}.grass{fill:#2c4a33}.hill{fill:#22382a}.doc{fill:#1b3a32;stroke:#9fb0a8}.ln{stroke:#9fb0a8}.chk{stroke:#4fd197}
.tent{fill:#2f9e6a}.tent2{fill:#1f7a50}.bat{fill:#7d8a83}}
</style>"""

def panel(x, y, w, h, skew=14):
    cells = []
    for i in range(1, 4):
        cells.append(f'<line x1="{x+w*i/4+skew*(1-0)/2:.1f}" y1="{y}" x2="{x+w*i/4-skew/2:.1f}" y2="{y+h}" class="cell" stroke-width="1.5"/>')
    for j in range(1, 3):
        yy = y + h * j / 3; off = skew * (1 - j / 3)
        cells.append(f'<line x1="{x+off-skew/2+skew/2:.1f}" y1="{yy:.1f}" x2="{x+w+off-skew/2:.1f}" y2="{yy:.1f}" class="cell" stroke-width="1.5"/>')
    return (f'<path d="M{x+skew} {y} H{x+w+skew/2} L{x+w-skew/2} {y+h} H{x} Z" class="pan"/>' + "".join(cells))

def illu(name, title, desc, parts):
    s = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 480 270" width="480" height="270" role="img" aria-labelledby="t d" lang="de">'
         f'<title id="t">{esc(title)}</title><desc id="d">{esc(desc)}</desc>{ILLU_STYLE}'
         '<rect class="sky" width="480" height="270"/><circle class="sun" cx="400" cy="62" r="30"/>' + "".join(parts) + "</svg>\n")
    open(os.path.join(OUT, name), "w", encoding="utf-8").write(s); print("geschrieben", name)

def balkon():
    return ['<rect class="wall" x="0" y="0" width="70" height="270"/>',
            '<rect class="wall" x="0" y="200" width="480" height="70"/>',
            '<rect class="rail" x="60" y="140" width="420" height="6"/>',
            *[f'<rect class="rail" x="{60+i*42}" y="146" width="4" height="54"/>' for i in range(11)],
            panel(110, 108, 110, 66), panel(236, 108, 110, 66)]

def illus():
    illu("titel-anmelden.svg", "Illustration: Balkon mit Solarmodulen und Checkliste",
         "Gezeichnete, generische Illustration: zwei Solarmodule am Balkongeländer, daneben ein Formular mit Häkchen.",
         balkon() + ['<rect class="doc" x="370" y="96" width="78" height="100" rx="6" stroke-width="2"/>',
                     *[f'<path d="M382 {120+i*24} l6 6 l11 -12" fill="none" class="chk" stroke-width="3"/><line x1="406" y1="{122+i*24}" x2="438" y2="{122+i*24}" class="ln" stroke-width="2"/>' for i in range(3)]])
    illu("titel-speicher.svg", "Illustration: Balkon mit Solarmodulen und Speicher",
         "Gezeichnete, generische Illustration: zwei Solarmodule am Balkongeländer und ein schlichter Akkublock mit Ladeanzeige.",
         balkon() + ['<rect class="bat" x="372" y="150" width="76" height="56" rx="6"/>',
                     '<rect class="batl" x="384" y="164" width="12" height="28" rx="2"/><rect class="batl" x="400" y="164" width="12" height="28" rx="2"/><rect class="batl" x="416" y="164" width="12" height="28" rx="2" opacity=".35"/>',
                     '<path d="M300 186 C 330 210 350 190 372 180" fill="none" class="ln" stroke-width="3" stroke-dasharray="6 5"/>'])
    illu("titel-powerstation.svg", "Illustration: Zelt mit mobilem Solarpanel und Akku",
         "Gezeichnete, generische Illustration: ein Zelt auf einer Wiese, davor ein aufgestelltes Solarpanel und ein schlichter Akkublock.",
         ['<path class="hill" d="M0 170 Q120 110 240 160 T480 150 V270 H0Z"/>', '<rect class="grass" x="0" y="196" width="480" height="74"/>',
          '<path class="tent" d="M40 210 L130 96 L220 210 Z"/><path class="tent2" d="M130 96 L150 210 H110 Z"/>',
          panel(250, 150, 96, 56), '<line x1="300" y1="206" x2="314" y2="222" class="ln" stroke-width="3"/>',
          '<rect class="bat" x="370" y="168" width="70" height="52" rx="6"/>',
          '<rect class="batl" x="382" y="180" width="11" height="26" rx="2"/><rect class="batl" x="397" y="180" width="11" height="26" rx="2"/><rect class="batl" x="412" y="180" width="11" height="26" rx="2"/>'])

illus()
