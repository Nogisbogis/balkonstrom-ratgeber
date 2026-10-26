#!/usr/bin/env python3
"""Schematische Produkt-Illustrationen (selbst gezeichnet) nach Herstellerangaben.
Maße (mm) stammen von den Produktseiten (content/*/<slug>.md, Zeile „Maße“), Anschlusszahlen
aus den Datenblättern. Keine Logos, keine Nachzeichnung von Fotos.
Aufruf: python3 tools/illus.py  → static/img/illu/<slug>.svg + groesse-*.svg"""
import os, html
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "static", "img", "illu")
os.makedirs(OUT, exist_ok=True)

STYLE = """<style>
.f{fill:#e3e0d8}.t{fill:#f1eee6}.s{fill:#c9c5bb}.l{stroke:#111;stroke-width:1.6;stroke-linejoin:round;stroke-linecap:round}
.p{fill:#262b2e}.a{fill:#0a6b3d}.as{stroke:#0a6b3d}.k{fill:#f7f5f0}.h{fill:#262b2e}.m{fill:#55595e}.ml{stroke:#55595e}
.c{fill:#2f4f6f}.cl{stroke:#9db7d1}
text{font-family:system-ui,-apple-system,"Segoe UI",Roboto,Arial,sans-serif}
@media (max-width:220px){.dim{display:none}}
@media (prefers-color-scheme:dark){.f{fill:#3b4d46}.t{fill:#4b5f57}.s{fill:#2c3b36}.l{stroke:#eef2ee}
.p{fill:#0b1512}.a{fill:#5fd69a}.as{stroke:#5fd69a}.k{fill:#26372f}.h{fill:#0b1512}.m{fill:#b5c2bb}.ml{stroke:#b5c2bb}
.c{fill:#24476b}.cl{stroke:#7fa2c8}}
</style>"""

# front = sichtbare Breite, tief, hoch (mm). Bei DJI ist die Frontseite die kurze Seite (Foto DJI).
PS = [
 dict(slug="ecoflow-river-3", name="EcoFlow RIVER 3", dims=(255,212,113), ac=1, usbc=1, usba=2, disp="left", griff="mulde"),
 dict(slug="ecoflow-river-3-plus", name="EcoFlow RIVER 3 Plus", dims=(234,232,146), ac=3, usbc=1, usba=2, disp="left", griff="buegel"),
 dict(slug="jackery-explorer-300-plus", name="Jackery Explorer 300 Plus", dims=(230,155,167), ac=1, usbc=1, usba=1, disp="left", griff="klapp"),
 dict(slug="anker-solix-c300x", name="Anker SOLIX C300X", dims=(164,161,240), ac=2, usbc=3, usba=1, disp="top", griff="schlaufe"),
 dict(slug="dji-power-1000-mini", name="DJI Power 1000 Mini", dims=(212,314,216), ac=2, usbc=2, usba=2, disp="left", griff="mulde", licht=True, masse_txt=(314,212,216)),
 dict(slug="anker-solix-c1000-gen-2", name="Anker SOLIX C1000 Gen 2", dims=(384,208,244), ac=4, usbc=3, usba=1, disp="top", griff="schulter"),
 dict(slug="ecoflow-delta-3-plus", name="EcoFlow DELTA 3 Plus", dims=(398,200,284), ac=4, usbc=2, usba=2, disp="top", griff="zwei"),
 dict(slug="bluetti-elite-100-v2", name="BLUETTI Elite 100 V2", dims=(320,215,250), ac=2, usbc=2, usba=2, disp="top", griff="mulde"),
 dict(slug="jackery-explorer-1000-v2", name="Jackery Explorer 1000 v2", dims=(327,224,247), ac=3, usbc=2, usba=1, disp="left", griff="klapp"),
 dict(slug="anker-solix-c2000-gen-2", name="Anker SOLIX C2000 Gen 2", dims=(459,250,257), ac=4, usbc=3, usba=1, disp="top", griff="schulter"),
 # ergänzt 20.10.2026 (Maße und Anschlusszahlen laut Hersteller bzw. Handbuch; Elite 30 V2: 1 AC laut Test, EU-Version)
 dict(slug="ecoflow-delta-3-max-plus", name="EcoFlow DELTA 3 Max Plus", dims=(494,242,305), ac=4, usbc=3, usba=1, disp="top", griff="zwei"),
 dict(slug="dji-power-2000", name="DJI Power 2000", dims=(448,225,324), ac=4, usbc=4, usba=4, disp="top", griff="zwei"),
 dict(slug="bluetti-elite-300", name="BLUETTI Elite 300", dims=(366,305,297.5), ac=2, usbc=2, usba=2, disp="top", griff="zwei"),
 dict(slug="ecoflow-delta-pro-3", name="EcoFlow DELTA Pro 3", dims=(693,341,410), ac=5, usbc=2, usba=2, disp="top", griff="zwei", rollen=True),
 dict(slug="ecoflow-trail-300-dc", name="EcoFlow TRAIL 300 DC", dims=(166,115,167), ac=0, usbc=2, usba=2, disp="left", griff="schlaufe", kfz=True, masse_txt=(115,166,167)),
 dict(slug="bluetti-elite-30-v2", name="BLUETTI Elite 30 V2", dims=(250,178,167.5), ac=1, usbc=2, usba=2, disp="left", griff="mulde"),
# Ergänzt 22.10.2026 (Herstellerseiten-Entwurf); Anschlusszahl nur schematisch, Maße laut Herstellerseite
 dict(slug="anker-solix-s2000", name="Anker SOLIX S2000", dims=(208,282,323.3), ac=1, usbc=2, usba=1, disp="top", griff="zwei"),
 dict(slug="ecoflow-delta-3-classic", name="EcoFlow DELTA 3 Classic", dims=(398,200,283), ac=2, usbc=2, usba=1, disp="top", griff="zwei"),
 dict(slug="ecoflow-trail-200-dc", name="EcoFlow TRAIL 200 DC", dims=(115,126,167), ac=0, usbc=2, usba=2, disp="left", griff="schlaufe"),
 dict(slug="jackery-explorer-3600-plus", name="Jackery Explorer 3600 Plus", dims=(385,309,491), ac=3, usbc=2, usba=2, disp="top", griff="zwei", rollen=True),
 dict(slug="jackery-explorer-2000-v2", name="Jackery Explorer 2000 v2", dims=(335,264,292), ac=2, usbc=2, usba=1, disp="left", griff="klapp"),
 # Zendure 26.10.2026. Ace: L × B × H laut FAQ; kein integrierter Akku.
 dict(slug="zendure-ace-1500", name="Zendure Ace 1500", dims=(326,200,108), masse_label="L × B × H", ac=1, usbc=1, usba=1, disp="left", griff="keine"),
]
BKW = [
 dict(slug="anker-solix-solarbank-2-e1600-pro", name="Anker SOLIX Solarbank 2 E1600 Pro", dims=(460,249,254), ac=1, mppt=4, griff="keine", led=True),
 dict(slug="anker-solix-solarbank-3-e2700-pro", name="Anker SOLIX Solarbank 3 E2700 Pro", dims=(460,254,279), ac=1, mppt=4, griff="keine", led=True),
 dict(slug="zendure-solarflow-800-pro", name="Zendure SolarFlow 800 Pro", dims=(338.6,226,358), ac=1, mppt=4, griff="zwei", led=False),
 dict(slug="ecoflow-stream-ultra", name="EcoFlow STREAM Ultra", dims=(255,284,458), ac=2, mppt=4, griff="mulde", led=True),
 dict(slug="ecoflow-stream-pro", name="EcoFlow STREAM Pro", dims=(255,284,458), ac=2, mppt=3, griff="mulde", led=True),
 dict(slug="growatt-nexa-2000", name="Growatt NEXA 2000", dims=(406,255,290), ac=1, mppt=4, griff="keine", led=False),
# Ergänzt 22.10.2026; mppt = Zahl der PV-Eingänge (Zendure: Eingänge laut Shop, MPPT-Zahl keine Angabe)
 dict(slug="anker-solix-solarbank-4-e5000-pro", name="Anker SOLIX Solarbank 4 E5000 Pro", dims=(460,305,355), ac=1, mppt=4, griff="keine", led=True),
 dict(slug="anker-solix-solarbank-max", name="Anker SOLIX Solarbank Max", dims=(670,356,350), ac=1, mppt=3, griff="keine", led=True),
 dict(slug="ecoflow-stream-ultra-x", name="EcoFlow STREAM Ultra X", dims=(420,294,460), ac=1, mppt=4, griff="mulde", led=True),
 dict(slug="jackery-solarvault-3-pro-max", name="Jackery SolarVault 3 Pro Max", dims=(485,248,282), ac=1, mppt=4, griff="zwei", led=True),
 dict(slug="zendure-solarflow-800-pro-2", name="Zendure SolarFlow 800 Pro 2", dims=(392.7,236.3,276), ac=1, mppt=4, griff="zwei", led=False),
 dict(slug="zendure-solarflow-2400-ac-plus", name="Zendure SolarFlow 2400 AC+", dims=(326,294,251), ac=1, mppt=0, griff="zwei", led=False),
 dict(slug="zendure-solarflow-800-plus", name="Zendure SolarFlow 800 Plus", dims=(393,236,242), ac=0, mppt=2, griff="zwei", led=False),
 # Zendure 26.10.2026. 2400 Pro: B × H × T 326 × 294 × 251 → dims B, T, H.
 # Hub 2000: B × T × H laut FAQ. ohne_mass: Produktseite ohne (eindeutige) Maße.
 dict(slug="zendure-solarflow-2400-pro", name="Zendure SolarFlow 2400 Pro", dims=(326,251,294), ac=1, mppt=4, griff="keine", led=False),
 dict(slug="zendure-hub-2000", name="Zendure Hub 2000", dims=(363,64,246), ac=0, mppt=2, griff="keine", led=False),
 dict(slug="zendure-solarflow-1600-ac", name="Zendure SolarFlow 1600 AC+", ohne_mass=True, ac=1, mppt=0),
 dict(slug="zendure-solarflow-2400-ac", name="Zendure SolarFlow 2400 AC", ohne_mass=True, mass_hinweis="Maße widersprüchlich, nicht maßstäblich", ac=1, mppt=0),
 dict(slug="zendure-solarflow-3000-mix-ac", name="Zendure SolarFlow 3000 Mix AC+", ohne_mass=True, ac=1, mppt=0, rollen=True),
 dict(slug="zendure-solarflow-4000-mix-ac", name="Zendure SolarFlow 4000 Mix AC+", ohne_mass=True, ac=1, mppt=0, rollen=True),
 dict(slug="zendure-solarflow-4000-mix-pro", name="Zendure SolarFlow 4000 Mix Pro", ohne_mass=True, ac=1, mppt=2, rollen=True),
 dict(slug="zendure-powerhub", name="Zendure PowerHub", ohne_mass=True, ac=0, mppt=0),
]
KX, KY = 0.45, 0.30   # Schrägprojektion: Tiefe nach rechts oben

def esc(s): return html.escape(str(s), quote=True)
def cm(mm):
    v = round(mm / 10, 1)
    return (f"{v:.1f}".rstrip("0").rstrip(".")).replace(".", ",")
def r(v): return f"{v:.1f}".rstrip("0").rstrip(".")

def schuko(cx, cy, rr):
    return (f'<circle cx="{r(cx)}" cy="{r(cy)}" r="{r(rr)}" class="k l"/>'
            f'<circle cx="{r(cx-rr*.38)}" cy="{r(cy)}" r="{r(rr*.13)}" class="h"/><circle cx="{r(cx+rr*.38)}" cy="{r(cy)}" r="{r(rr*.13)}" class="h"/>')

def usbc(x, y, w):
    return f'<rect x="{r(x)}" y="{r(y)}" width="{r(w)}" height="{r(w*.38)}" rx="{r(w*.19)}" class="h"/>'
def usba(x, y, w):
    return f'<rect x="{r(x)}" y="{r(y)}" width="{r(w)}" height="{r(w*.42)}" rx="1" class="h"/>'

def display(x, y, w, h):
    return (f'<rect x="{r(x)}" y="{r(y)}" width="{r(w)}" height="{r(h)}" rx="{r(min(w,h)*.12)}" class="p"/>'
            f'<rect x="{r(x+w*.1)}" y="{r(y+h*.68)}" width="{r(w*.55)}" height="{r(max(1.5,h*.09))}" rx="1" class="a"/>'
            f'<rect x="{r(x+w*.1)}" y="{r(y+h*.25)}" width="{r(w*.3)}" height="{r(h*.28)}" rx="1" class="a" opacity=".55"/>')

def koerper(x, y, fw, fh, dx, dy, rad):
    """Quader in Schrägansicht: Oberseite, rechte Seite, Front."""
    top = f'<path d="M{r(x)} {r(y)}L{r(x+dx)} {r(y-dy)}H{r(x+fw+dx)}L{r(x+fw)} {r(y)}Z" class="t l"/>'
    side = f'<path d="M{r(x+fw)} {r(y)}L{r(x+fw+dx)} {r(y-dy)}V{r(y+fh-dy)}L{r(x+fw)} {r(y+fh)}Z" class="s l"/>'
    front = f'<rect x="{r(x)}" y="{r(y)}" width="{r(fw)}" height="{r(fh)}" rx="{r(rad)}" class="f l"/>'
    return top + side + front

def griff(kind, x, y, fw, fh, dx, dy):
    o = []
    if kind == "mulde":   # eingelassener Griff in der Oberseite
        o.append(f'<path d="M{r(x+fw*.32+dx*.5)} {r(y-dy*.5)}H{r(x+fw*.68+dx*.5)}" class="l" stroke-width="6" stroke-linecap="round" fill="none" opacity=".7"/>')
    elif kind in ("buegel", "klapp"):   # Bügel über der Oberseite
        hgt = max(10, fh * (.22 if kind == "buegel" else .16))
        x1, x2 = x + fw*.18 + dx*.5, x + fw*.82 + dx*.5; yb = y - dy*.5
        o.append(f'<path d="M{r(x1)} {r(yb)}V{r(yb-hgt*.6)}Q{r(x1)} {r(yb-hgt)} {r(x1+hgt*.4)} {r(yb-hgt)}H{r(x2-hgt*.4)}Q{r(x2)} {r(yb-hgt)} {r(x2)} {r(yb-hgt*.6)}V{r(yb)}" class="l" fill="none" stroke-width="{4 if kind=="klapp" else 6}"/>')
    elif kind == "schlaufe":
        x1, x2 = x + fw*.3 + dx*.5, x + fw*.7 + dx*.5; yb = y - dy*.5
        o.append(f'<path d="M{r(x1)} {r(yb)}C{r(x1)} {r(yb-fh*.3)} {r(x2)} {r(yb-fh*.3)} {r(x2)} {r(yb)}" class="l" fill="none" stroke-width="4"/>')
    elif kind in ("schulter", "zwei"):   # zwei Griffe an den Enden
        w = fw * (.2 if kind == "schulter" else .15); hgt = max(9, fh*.11)
        for gx in (x + fw*.05, x + fw*.95 - w):
            bx, by = gx + dx*.5, y - dy*.5
            o.append(f'<path d="M{r(bx)} {r(by)}l{r(hgt*.45)} {r(-hgt)}h{r(w-hgt*.9)}l{r(hgt*.45)} {r(hgt)}Z" class="f l"/>'
                     f'<path d="M{r(bx+hgt*.75)} {r(by-hgt*.45)}h{r(w-hgt*1.5)}" class="l" stroke-width="3" fill="none" opacity=".5"/>')
    return "".join(o)

def front_ps(m, x, y, fw, fh):
    o = []; pad = fw*.07; ix, iy, iw, ih = x+pad, y+fh*.1, fw-2*pad, fh*.8
    ac, nc, na = m["ac"], m["usbc"], m["usba"]
    if m["disp"] == "top":
        dw, dh = iw*.46, ih*.26
        o.append(display(ix+(iw-dw)/2, iy, dw, dh))
        uw = min(iw*.07, dh*.55); ux = ix + (iw-dw)/2 - (nc+na)*uw*1.5 - uw*.3
        ux = max(ix, ux); uy = iy + dh*.4
        for i in range(nc): o.append(usbc(ux + i*uw*1.4, uy, uw))
        ux2 = ix + (iw+dw)/2 + uw*.5
        for i in range(na): o.append(usba(ux2 + i*uw*1.4, uy, uw))
        zone_y, zone_h, zone_x, zone_w = iy+dh+ih*.08, ih-dh-ih*.08, ix, iw
    else:
        dw, dh = iw*.34, ih*.42
        o.append(display(ix, iy, dw, dh))
        uw = min(dw/(max(nc+na,1)*1.45), ih*.12)
        for i in range(nc): o.append(usbc(ix + i*uw*1.45, iy+dh+ih*.12, uw))
        for i in range(na): o.append(usba(ix + (nc+i)*uw*1.45, iy+dh+ih*.12, uw))
        zone_x, zone_w, zone_y, zone_h = ix+dw+iw*.06, iw-dw-iw*.06, iy, ih*.7
    if ac:
        rr = min(zone_h*.36, zone_w/(ac*2.5))
        gap = (zone_w - ac*2*rr)/(ac+1)
        for i in range(ac):
            o.append(schuko(zone_x + gap*(i+1) + rr*(2*i+1), zone_y + zone_h*.45, rr))
    if m.get("kfz"):   # runde 12-V-Kfz-Buchse statt Steckdose (reine DC-Station)
        rk = min(zone_h*.24, zone_w*.2); cx, cy = zone_x + zone_w*.5, zone_y + zone_h*.45
        o.append(f'<circle cx="{r(cx)}" cy="{r(cy)}" r="{r(rk)}" class="k l"/><circle cx="{r(cx)}" cy="{r(cy)}" r="{r(rk*.55)}" class="h"/><circle cx="{r(cx)}" cy="{r(cy)}" r="{r(rk*.16)}" class="k"/>')
    if m.get("licht"):
        o.append(f'<rect x="{r(x+fw*.15)}" y="{r(y+fh*.86)}" width="{r(fw*.7)}" height="{r(fh*.05)}" rx="2" class="k l" stroke-width="1"/>')
    return "".join(o)

def front_bkw(m, x, y, fw, fh, dx, dy):
    o = []
    if m.get("led"):
        o.append(f'<rect x="{r(x+fw*.25)}" y="{r(y+fh*.14)}" width="{r(fw*.5)}" height="{r(max(2.5,fh*.025))}" rx="2" class="a"/>')
    rr = min(fw, fh)*.07
    for i in range(m["ac"]):   # Notstrom-Steckdose(n) mit Klappe
        cx = x + fw*(.5 if m["ac"] == 1 else (.36 + .28*i)); cy = y + fh*.62
        o.append(f'<rect x="{r(cx-rr*1.45)}" y="{r(cy-rr*1.45)}" width="{r(rr*2.9)}" height="{r(rr*2.9)}" rx="{r(rr*.5)}" class="t l"/>' + schuko(cx, cy, rr))
    # MPPT-Eingänge als Steckerpaare an der rechten Seite
    n = m["mppt"]
    for i in range(n):
        t = (i + 1) / (n + 1); px = x + fw + dx*.5; py = y + fh*(.3 + .55*t) - dy*.5
        for k, off in enumerate((-3.2, 3.2)):
            o.append(f'<circle cx="{r(px+off)}" cy="{r(py)}" r="2.4" class="{"h" if k else "a"}"/>')
    o.append(f'<rect x="{r(x+fw*.08)}" y="{r(y+fh*.93)}" width="{r(fw*.84)}" height="{r(fh*.03)}" class="s"/>')
    return "".join(o)

def zeichne(m, x, y, s, art):
    L, D, H = m["dims"]
    fw, fh, dx, dy = L*s, H*s, D*s*KX, D*s*KY
    rad = min(fw, fh)*.06
    body = koerper(x, y, fw, fh, dx, dy, rad)
    g = griff(m["griff"], x, y, fw, fh, dx, dy)
    det = front_ps(m, x, y, fw, fh) if art == "ps" else front_bkw(m, x, y, fw, fh, dx, dy)
    if m.get("rollen"):   # Rollen an der Unterseite (Trolley)
        rw = max(3, fh*.05)
        for wx in (x + fw*.1, x + fw*.9):
            det += f'<circle cx="{r(wx)}" cy="{r(y+fh)}" r="{r(rw)}" class="h l" stroke-width="1.2"/>'
    return body + g + det

def masse(m):
    L, D, H = m.get("masse_txt", m["dims"])
    return f"{cm(L)} × {cm(D)} × {cm(H)} cm"

def svg(name, w, h, title, body):
    out = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img" aria-label="{esc(title)}" lang="de">'
           f'{STYLE}{body}</svg>\n')
    open(os.path.join(OUT, name), "w", encoding="utf-8").write(out)
    return len(out)

def ohne_mass(m, art):
    """Kiste ohne Maßstab, wenn die Produktseite keine (eindeutigen) Maße nennt."""
    W, H = 400, 300
    fw, fh, dx, dy = (170, 120, 40, 26) if art == "ps" else (140, 160, 42, 28)
    x, y = (W - fw - dx) / 2, 78
    b = koerper(x, y, fw, fh, dx, dy, min(fw, fh) * .06)
    if art == "ps":
        b += front_ps(m, x, y, fw, fh)
    else:
        b += front_bkw(m, x, y, fw, fh, dx, dy)
    if m.get("rollen"):
        rw = 7
        for wx in (x + fw * .18, x + fw * .82):
            b += f'<circle cx="{r(wx)}" cy="{r(y+fh)}" r="{r(rw)}" class="h l" stroke-width="1.2"/>'
    b += (f'<text x="{W/2}" y="{H-28}" class="m" font-size="13" text-anchor="middle">{esc(m.get("mass_hinweis", "Maße: keine Angabe auf der Produktseite"))}</text>'
          f'<text x="{W/2}" y="{H-10}" class="m" font-size="12" text-anchor="middle">schematisch, nicht maßstäblich</text>')
    return svg(m["slug"] + ".svg", W, H, f'{m["name"]}, schematische Darstellung ohne Maßangabe', b)

def einzeln(m, art):
    if m.get("ohne_mass"):
        return ohne_mass(m, art)
    W, H, mx, top, unten = 400, 300, 34, 24, 50
    L, D, Hh = m["dims"]
    hext = .26 if m["griff"] in ("buegel", "schlaufe") else .12
    s = min((W - 2*mx) / (L + D*KX), (H - top - unten) / (Hh*(1+hext) + D*KY))
    tw, th = (L + D*KX)*s, (Hh + D*KY)*s
    x = (W - tw)/2; y = top + Hh*hext*s + D*KY*s + (H - top - unten - th - Hh*hext*s)/2
    b = zeichne(m, x, y, s, art)
    fw = L*s; yb = y + Hh*s + 12
    b += (f'<g class="dim"><path d="M{r(x)} {r(yb-4)}v8M{r(x)} {r(yb)}H{r(x+fw)}M{r(x+fw)} {r(yb-4)}v8" class="ml" stroke-width="1.2" fill="none"/>'
          f'<text x="{r(x+fw/2)}" y="{r(yb+16)}" class="m" font-size="13" text-anchor="middle">{cm(L)} cm</text>'
          f'<text x="{W/2}" y="{H-8}" class="m" font-size="12" text-anchor="middle">{masse(m)} ({esc(m.get("masse_label", "B × T × H"))}) laut Hersteller</text></g>')
    return svg(m["slug"] + ".svg", W, H, f'{m["name"]}, schematische Darstellung', b)

def rs40p():
    W, H = 400, 300
    pw, ph = 1134, 1706; gap = 60; s = min(300/(2*pw+gap), 220/ph)
    x0 = (W - (2*pw+gap)*s)/2 - 42; y0 = 18
    b = ""
    for k in range(2):
        x = x0 + k*(pw+gap)*s; w, h = pw*s, ph*s
        b += f'<rect x="{r(x)}" y="{r(y0)}" width="{r(w)}" height="{r(h)}" rx="2" class="c l"/>'
        for i in range(1, 6): b += f'<path d="M{r(x+w*i/6)} {r(y0+2)}V{r(y0+h-2)}" class="cl" stroke-width=".8"/>'
        for j in range(1, 10): b += f'<path d="M{r(x+2)} {r(y0+h*j/10)}H{r(x+w-2)}" class="cl" stroke-width=".8"/>'
    ix = x0 + (2*pw+gap)*s + 16; iy = y0 + ph*s*.55
    b += koerper(ix, iy, 26, 34, 8, 5, 3) + f'<rect x="{r(ix+6)}" y="{r(iy+8)}" width="14" height="3" class="a"/>'
    b += f'<path d="M{r(ix+13)} {r(iy+34)}v14" class="l" fill="none"/>'
    b += f'<g class="dim"><text x="{W-6}" y="{r(iy+66)}" class="m" font-size="11" text-anchor="end">Wechsel-</text><text x="{W-6}" y="{r(iy+80)}" class="m" font-size="11" text-anchor="end">richter</text></g>'
    yb = y0 + ph*s + 12
    b += (f'<g class="dim"><path d="M{r(x0)} {r(yb-4)}v8M{r(x0)} {r(yb)}H{r(x0+pw*s)}M{r(x0+pw*s)} {r(yb-4)}v8" class="ml" stroke-width="1.2" fill="none"/>'
          f'<text x="{r(x0+pw*s/2)}" y="{r(yb+16)}" class="m" font-size="13" text-anchor="middle">{cm(pw)} cm</text>'
          f'<text x="{W/2}" y="{H-8}" class="m" font-size="12" text-anchor="middle">2 Module, je 170,6 × 113,4 × 3,5 cm laut Datenblatt</text></g>')
    return svg("anker-solix-rs40p.svg", W, H, "Anker SOLIX RS40P Balkonkraftwerk, schematische Darstellung", b)

def vergleich(liste, art, name, title, s, pro_reihe):
    """Alle Geräte im selben Maßstab nebeneinander (Frontansicht), mit 10-cm-Maßstab."""
    gapx, mx = 26, 20
    reihen = [liste[i:i+pro_reihe] for i in range(0, len(liste), pro_reihe)]
    rh = [max((m["dims"][2]*1.12 + m["dims"][1]*KY)*s for m in rr) + 40 for rr in reihen]
    W = int(max(sum((m["dims"][0] + m["dims"][1]*KX)*s for m in rr) + gapx*(len(rr)-1) for rr in reihen) + 2*mx)
    H = int(sum(rh) + 46)
    b = ""; y = 10
    for rr, hh in zip(reihen, rh):
        x = mx; base = y + hh - 34
        for m in rr:
            L, D, Hh = m["dims"]
            b += zeichne(m, x, base - Hh*s, s, art)
            nm = m["name"].replace("Anker SOLIX ", "Anker ").replace("Jackery Explorer ", "Jackery ")
            tx = max(x + L*s/2, 4 + len(nm)*2.9)   # Beschriftung nicht links abschneiden (schmale Geräte)
            b += f'<text x="{r(tx)}" y="{r(base+16)}" class="m" font-size="11.5" text-anchor="middle">{esc(nm)}</text>'
            x += (L + D*KX)*s + gapx
        y += hh
    b += (f'<path d="M{mx} {H-22}v-6M{mx} {H-25}h{r(100*s)}M{r(mx+100*s)} {H-22}v-6" class="ml" stroke-width="1.4" fill="none"/>'
          f'<text x="{r(mx+100*s+8)}" y="{H-21}" class="m" font-size="12">10 cm · alle im selben Maßstab, Maße laut Hersteller</text>')
    return svg(name, W, H, title, b)

PB = [   # Powerbanks: dims = Länge × Tiefe × Höhe (liegend), Maße laut Herstellerseite
 dict(slug="ecoflow-rapid-pro-20k", name="EcoFlow RAPID Pro 20K", dims=(145,56,55), usbc=3, usba=0, kabel=True),
 dict(slug="ecoflow-rapid-pro-27k", name="EcoFlow RAPID Pro 27K", dims=(166,58,55), usbc=3, usba=0, kabel=True),
 dict(slug="ecoflow-rapid-25k", name="EcoFlow RAPID 25K", dims=(157,48.8,53.8), usbc=2, usba=1, kabel=False),
]

def powerbank(m):
    """Powerbank liegend in Schrägansicht: Display vorn, Anschlüsse an der Stirnseite links, ggf. integriertes Kabel."""
    W, H, mx, top, unten = 400, 300, 40, 30, 50
    L, D, Hh = m["dims"]
    s = min((W - 2*mx - 30) / (L + D*KX), (H - top - unten - 40) / (Hh + D*KY))
    fw, fh, dx, dy = L*s, Hh*s, D*s*KX, D*s*KY
    x = (W - fw - dx)/2 + 12; y = top + 30 + dy + (H - top - unten - 30 - fh - dy)/2
    b = koerper(x, y, fw, fh, dx, dy, fh*.22)
    b += display(x + fw*.42, y + fh*.22, fw*.36, fh*.5)
    n = m["usbc"] + m["usba"]; uw = min(fh*.16, 22)
    for i in range(m["usbc"]): b += usbc(x + fw*.06, y + fh*(.2 + .2*i), uw*1.3)
    for i in range(m["usba"]): b += usba(x + fw*.06, y + fh*(.2 + .2*(m["usbc"]+i)), uw*1.3)
    if m.get("kabel"):
        cx = x - 6
        b += (f'<path d="M{r(x+2)} {r(y+fh*.8)}C{r(cx-34)} {r(y+fh*.8)} {r(cx-34)} {r(y-dy-20)} {r(x+fw*.2)} {r(y-dy*.6)}" class="l" fill="none" stroke-width="5" stroke-linecap="round"/>'
              f'<rect x="{r(x+fw*.2-4)}" y="{r(y-dy*.6-5)}" width="16" height="8" rx="3" class="k l" stroke-width="1"/>')
    b += f'<rect x="{r(x+fw*.86)}" y="{r(y+fh*.42)}" width="{r(fw*.06)}" height="{r(fh*.12)}" rx="2" class="a"/>'
    yb = y + fh + 14
    b += (f'<g class="dim"><path d="M{r(x)} {r(yb-4)}v8M{r(x)} {r(yb)}H{r(x+fw)}M{r(x+fw)} {r(yb-4)}v8" class="ml" stroke-width="1.2" fill="none"/>'
          f'<text x="{r(x+fw/2)}" y="{r(yb+16)}" class="m" font-size="13" text-anchor="middle">{cm(L)} cm</text>'
          f'<text x="{W/2}" y="{H-8}" class="m" font-size="12" text-anchor="middle">{cm(L)} × {cm(D)} × {cm(Hh)} cm laut Hersteller</text></g>')
    return svg(m["slug"] + ".svg", W, H, f'{m["name"]}, schematische Darstellung', b)

if __name__ == "__main__":
    for m in PS: print(m["slug"], einzeln(m, "ps"), "Bytes")
    for m in BKW: print(m["slug"], einzeln(m, "bkw"), "Bytes")
    for m in PB: print(m["slug"], powerbank(m), "Bytes")
    print("anker-solix-rs40p", rs40p(), "Bytes")
    ps_sorted = sorted([m for m in PS if not m.get("ohne_mass")], key=lambda m: m["dims"][0]*m["dims"][1]*m["dims"][2])
    print("groesse-powerstations", vergleich(ps_sorted, "ps", "groesse-powerstations.svg", "Größenvergleich der Powerstations im selben Maßstab, schematische Darstellung", .42, 5), "Bytes")
    b_sorted = sorted([m for m in BKW if not m.get("ohne_mass")], key=lambda m: m["dims"][0]*m["dims"][1]*m["dims"][2])
    print("groesse-balkonspeicher", vergleich(b_sorted, "bkw", "groesse-balkonspeicher.svg", "Größenvergleich der Balkonspeicher im selben Maßstab, schematische Darstellung", .36, 6), "Bytes")
