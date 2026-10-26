# Redesign v4 „Sonnenstand“ (Entwurf, nicht live)

Status: **Entwurf auf Branch `redesign-v4`**. Nichts ist gepusht, gemergt oder deployt. Live geht es erst nach einem ausdrücklichen Ja des Betreibers.

## Idee in einem Satz

Der Tag eines Balkonmoduls als Farbkapitel: Im Hero steht „Strom“ im Himmel über der Brüstung und „auf Vorrat“ im Modulblau, die Kante (Wasserlinie) liegt zwischen den Zeilen. Danach folgen Mittagssonne (Einsatz), Papier (Empfehlungen), Grün (Selbst rechnen), Papier (Artikel) und Nachtblau (So arbeite ich, Fuß mit der Kontaktadresse als Überschrift).

## Ziele

- Ein komplett neuer Look mit starkem Kontrast. Er soll modern und minimal wirken, nicht nach Vorlage oder KI aussehen.
- Kein schlichtes Schwarz: Dunkelmodus und Fuß sind in Nachtblau gesetzt, die Flächen in Himmel, Modulblau, Sonne und Grün.
- Wenig sichtbarer Text: Details stecken hinter Pfeil-Aufklappern, rechtliche Hinweise bleiben dezent, aber immer sichtbar (nie eingeklappt).
- Alle Funktionen bleiben unverändert: Finder, Pagefind (/suche/), Rechner, Hersteller, Powerbanks, Zubehör, AWIN- und Amazon-Links samt Kennzeichnung, Verfügbarkeitssystem.

## Nicht-Ziele

- Keine neuen Inhalte, Preise, Bewertungen oder Testergebnisse.
- Keine Änderungen an Daten, Shortcodes, Affiliate-Logik oder JS-Funktionen.
- Kein Deployment und keine Cloudflare-Änderung.

## Tokens

Schriften (selbst gehostet, OFL, Latin-Subset, siehe `static/fonts/`):

- Display: League Spartan 700 (`--display`, auch `--serif`)
- Text: Figtree 400/600 (`--sans`)

Größen:

- `--fs-s` 1rem
- `--fs-b` clamp(1.0625rem … 1.1875rem)
- `--fs-l` clamp(1.25rem … 1.625rem)
- `--fs-h` clamp(2rem … 4rem)
- Hero clamp(3.5rem … 10.5rem)

Formen:

- Pillen-Buttons
- Flächenradius `--r-flaeche` 16px
- Flächen statt Linien: Karten, Kurzantwort, Aufklapper und Herstellerblöcke

Farbfelder (`--<feld>`, `--<feld>-ink`, `--<feld>-muted`):

| Feld | Hell | Dunkel | Einsatz |
|---|---|---|---|
| himmel | #cfe6f3 | #24476f | Hero Zeile 1, Seitenköpfe (`.kopf-feld`, `.post-kopf`) |
| zelle | #142c52 | #0a1830 | Hero unten, Kopfzeile, „So arbeite ich“ |
| sonne | #ffcf33 | #f2c230 | „Wofür brauchst du Strom?“, Hauptbutton, Akzente |
| blatt | #0a6b3d | #0d5c37 | „Selbst rechnen“ |
| nacht | #0b1a2b | #081426 | Fuß |
| Papier (bg) | #f4f6f1 | #10213a | Grundfläche |

### Kontraste (WCAG, berechnet)

**hell**

| Paar | Text | Fläche | Kontrast |
|---|---|---|---|
| ink/bg | `#0b1a2b` | `#f4f6f1` | 16.1:1 |
| muted/bg | `#4a5568` | `#f4f6f1` | 6.9:1 |
| accent/bg | `#0a6b3d` | `#f4f6f1` | 6.1:1 |
| muted/surface | `#4a5568` | `#e7ece4` | 6.3:1 |
| himmel ink | `#0b1a2b` | `#cfe6f3` | 13.6:1 |
| himmel muted | `#33465c` | `#cfe6f3` | 7.5:1 |
| zelle ink | `#f4f6f1` | `#142c52` | 12.8:1 |
| zelle muted | `#c3d0e4` | `#142c52` | 8.9:1 |
| sonne auf zelle (Hero-Zeile 2) | `#ffcf33` | `#142c52` | 9.4:1 |
| sonne ink | `#0b1a2b` | `#ffcf33` | 11.9:1 |
| sonne muted | `#3b3413` | `#ffcf33` | 8.4:1 |
| blatt ink | `#ffffff` | `#0a6b3d` | 6.6:1 |
| blatt muted | `#d3ecdc` | `#0a6b3d` | 5.3:1 |
| nacht ink | `#eef3f8` | `#0b1a2b` | 15.7:1 |
| nacht muted | `#b3c0d3` | `#0b1a2b` | 9.5:1 |
| sonne auf nacht | `#ffcf33` | `#0b1a2b` | 11.9:1 |
| btn-sun Text | `#0b1a2b` | `#ffcf33` | 11.9:1 |

**dunkel**

| Paar | Text | Fläche | Kontrast |
|---|---|---|---|
| ink/bg | `#eef3f8` | `#10213a` | 14.5:1 |
| muted/bg | `#b3c0d3` | `#10213a` | 8.8:1 |
| accent/bg | `#7ee0a8` | `#10213a` | 10.1:1 |
| muted/surface | `#b3c0d3` | `#172b48` | 7.7:1 |
| himmel ink | `#f4f6f1` | `#24476f` | 8.7:1 |
| himmel muted | `#c9d6e6` | `#24476f` | 6.5:1 |
| zelle ink | `#eef3f8` | `#0a1830` | 15.9:1 |
| zelle muted | `#b3c0d3` | `#0a1830` | 9.6:1 |
| sonne auf zelle | `#ffcf33` | `#0a1830` | 12.0:1 |
| sonne ink | `#0b1a2b` | `#f2c230` | 10.5:1 |
| sonne muted | `#3b3413` | `#f2c230` | 7.4:1 |
| blatt ink | `#ffffff` | `#0d5c37` | 8.1:1 |
| blatt muted | `#cfe8d8` | `#0d5c37` | 6.2:1 |
| nacht ink | `#eef3f8` | `#081426` | 16.5:1 |
| nacht muted | `#b3c0d3` | `#081426` | 10.0:1 |

Alle Text-Paare erreichen mindestens AA (4,5:1), die meisten AAA.

## Komponenten

- **`.wl` Wasserlinien-Hero:** H1 in zwei Blockzeilen (`.wl-z1` Himmel/Tinte, `.wl-z2` Modulblau/Sonne). Darunter `.wl-unten` mit Satz, Sonnen-Button, Textlink und einem echten Foto (Wikimedia, Credits im Fuß).
- **`.poster`:** Einsatzliste als große Zeilen auf Sonnengelb mit Pfeilspalte.
- **`.empf-home`:** 4/8-Raster, Überschrift links, Empfehlungen rechts. Die Kennzeichnung steht direkt unter der Überschrift.
- **`.slip-sec`:** grünes Feld mit dem Laufzeit-Beleg (Chips, Ergebniszeile in Sonne).
- **`.artikel-sec`:** fixierte Überschrift links, Artikelzeilen mit Pfeil rechts.
- **`.about-panel`:** eingerücktes Modulblau-Panel, Aufklapper im Panelstil.
- **Fuß:** Kontakt-Mail als Display-Überschrift, darunter Linkspalten, Kennzeichnung und Foto-Credits.
- **`.kopf-feld` / `.post-kopf`:** Himmel-Fläche über die volle Breite für Breadcrumb, H1, Lead und Kennzeichnung auf allen Listen-, Werkzeug-, Produkt- und Rechtsseiten.

## Bewegung

Es gibt nur Interaktionsbewegung:

- Unterstrich in der Navigation
- Poster- und Zeilenpfeile
- drehende Aufklapp-Pfeile
- Button-Druck
- Karten-Hover
- Ergebnis im Beleg

Beim Laden bewegt sich nichts, und die Kopfzeile wechselt ihre Farbe nicht. Beides ist ein ausdrücklicher Wunsch des Betreibers (Okt. 2026, Commit d081203). `prefers-reduced-motion` schaltet alles ab.

## Bewusste Abweichungen

1. **taste-skill `still-page` (FAIL bleibt stehen):** Das Skill verlangt Lade- und Scroll-Animationen, der Betreiber will einen ruhigen Seitenaufbau. Der Betreiberwunsch gewinnt.
2. **Schriften:** DESIGN.md sah Systemschriften vor. v4 nutzt zwei selbst gehostete OFL-Schriften (zusammen ca. 36 KB woff2, Preload für die zwei wichtigsten Schnitte). Es gibt keinen Google-Fonts-Abruf, also keinen Drittanbieter-Request (DSGVO).
3. **Palette:** Die vom Skill gezogene Palette (Ultramarin/Pink) wurde durch Themenfarben ersetzt (Himmel, Modul, Sonne, Grün, Nacht).
4. **Hero-Technik:** Die gezogene Richtung sah zwei überlagerte, beschnittene Überschriften-Kopien vor. Der Inspektor wertet das als verdeckten Text, eine Variante mit `background-clip:text` als Verlaufstext. v4 setzt die Kante deshalb zwischen die Zeilen: echte Flächen, Volltonfarben, keine Duplikate für Screenreader.
5. **Kein Video (WARN):** Es gibt kein ehrliches, frei lizenziertes Clip-Material zum Thema. Fotos bleiben Wikimedia, Geräte bleiben eigene Illustrationen.
6. **Schriftgrößen (WARN, 11 Stufen):** Tabellen, Anzeige-Labels und Kennzeichnung brauchen eigene kleine Stufen.

## Prüfung

- Build: `hugo --minify` plus Pagefind 1.5.2, beide ohne Fehler.
- taste-skill lint: Die eigenen Dateien sind sauber. Alle Treffer liegen im generierten Pagefind-CSS (Fremdcode).
- taste-skill inspect auf der Startseite: vorher 3 FAIL / 5 WARN, jetzt 1 FAIL (`still-page`, bewusst) / 2 WARN.
- Screenshots: `/workspace/blogbot/screens-redesign-v4/`. Abgedeckt sind home, post, zubehoer, hersteller und suche, jeweils hell und dunkel bei 1440, 768 und 390 px.

## Risiken vor dem Livegang

- Fast alle Templates bekommen einen `<header class="kopf-feld">`. Die Vollbreite hängt an `calc(50% - 50vw)` und funktioniert nur in zentrierten Containern. Ungeprüfte Seiten (Einsatzseiten, 404, einzelne Powerbank-Seiten) sollten vor dem Livegang einmal angesehen werden.
- Ältere v3-Regeln liegen weiter in `style.css` (z. B. `.h2f-*`). Sie sind ungenutzt, aber harmlos und können beim Aufräumen raus.
- Der Branch ist auf `main` 6b8d969 (inkl. Strompreis-Widget) rebased. Bewegt sich `main` (z. B. durch `wt-zubehoer`), muss vor dem Merge rebased werden.
