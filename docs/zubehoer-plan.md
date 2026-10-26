# Zubehör-Track: Strukturplan und interne Verlinkung (Entwurf)

Stand: 26.10.2026. /zubehoer/ und der Messsteckdosen-Ratgeber sind seit 26.10.2026 live; die internen Links aus Winter-, Ausrichtungs- und Speicher-Artikel sind eingebaut.

## URL-Baum

```
/zubehoer/                                   Übersicht (Layout zubehoer-liste), 5 Rubriken
  Messsteckdosen und Smart Plugs  -> /posts/balkonkraftwerk-ertrag-messen-steckdose/  (Entwurf fertig)
  Lesekopf für den Stromzähler    -> Ratgeber folgt
  Kabel und Verlängerung          -> Ratgeber folgt
  Stecker und Einspeisesteckdose  -> Ratgeber folgt (Schuko/Wieland, verweist auf /posts/balkonkraftwerk-anmelden-2026/)
  Halterungen und Wandmontage     -> Ratgeber folgt
```

Ratgeber liegen wie bisher unter `/posts/` und haben `kategorie = 'zubehoer'`.
Dadurch erscheinen sie auch auf /ratgeber/ in einer eigenen Rubrik „Zubehör“, und ihr Breadcrumb ist „Startseite › Zubehör“.

## Daten und Templates

| Datei | Zweck |
|---|---|
| `data/zubehoer.yaml` | Produktdaten für Zubehör (eigene Datei; Finder, Suche und Vergleich lesen sie nicht) |
| `layouts/_shortcodes/zubehoer.html` | `{{< zubehoer modelle="A\|B" hinweis="A=Text" >}}`, Karten aus zubehoer.yaml |
| `layouts/_partials/zubehoerkarte.html` | Karte ohne Bild, Amazon-Button mit „Anzeige“, „(Affiliate-Link)“, rel="sponsored nofollow noopener" |
| `layouts/zubehoer-liste.html` | Übersichtsseite /zubehoer/ |
| `layouts/kategorie.html`, `_partials/schema.html` | Rubrik „zubehoer“ in /ratgeber/ und ItemList ergänzt |
| `layouts/baseof.html` | Nav-Link „Zubehör“, erscheint nur, wenn /zubehoer/ veröffentlicht ist |

`tools/verfuegbarkeit.py` liest zubehoer.yaml automatisch mit, weil es alle Listen in data/*.yaml prüft.

## Interne Links (erst nach Freigabe einbauen, weil das Ziel noch Entwurf ist)

| Quelle | Stelle | Vorgeschlagener Satz |
|---|---|---|
| posts/balkonkraftwerk-winter-ertrag.md | nach Zeile 41 (PVGIS-Hinweis) | „Wie viel deine eigene Anlage liefert, zeigt eine Messsteckdose: [Balkonkraftwerk-Ertrag messen]({{< relref "balkonkraftwerk-ertrag-messen-steckdose" >}}).“ |
| posts/balkonkraftwerk-ausrichtung-neigung.md | nach Zeile 45 (PVGIS-Hinweis) | gleicher Satz, Anker „Ertrag selbst messen“ |
| posts/balkonkraftwerk-mit-speicher-lohnt-sich.md | Abschnitt „Worauf du beim Kauf achten solltest“ (Z. 117) | „Bevor du einen Speicher kaufst, miss ein paar Wochen lang, wie viel Strom dein Balkonkraftwerk liefert: [Ertrag messen]({{< relref "balkonkraftwerk-ertrag-messen-steckdose" >}}).“ |
| posts/balkonkraftwerk-anmelden-2026.md | Abschnitt „Die Steckdose: Schuko oder Energiesteckvorrichtung?“ (Z. 111) | später auf den Stecker-Ratgeber verlinken, sobald es ihn gibt |
| balkonkraftwerke/* (Produktseiten) | Block „Weiter“ | optional: Link auf /zubehoer/ |

Vom neuen Artikel gehen schon Links auf winter-ertrag, ausrichtung-neigung und den Amortisationsrechner.

## Nächste Themen (Vorschlag)

1. Lesekopf für den Stromzähler (Tibber Pulse, Shelly 3EM als Alternative, Hichi/Tasmota): Hersteller-Daten nötig.
2. Wieland-Stecker oder Schuko: baut auf dem Anmelde-Artikel auf.
3. Verlängerungskabel und Querschnitt für Balkonkraftwerke.
4. Halterungen für Geländer, Wand und Boden: Windlast und Material.

## Vor dem Veröffentlichen

- `draft = true` in `content/zubehoer/_index.md` und im Artikel entfernen. Datum auf den Veröffentlichungstag setzen.
- `python3 tools/verfuegbarkeit.py` laufen lassen (curl zeigte bei beiden Shelly-Steckdosen und der FRITZ!-Steckdose nur „Alle Angebote“).
- Geklärt: B0DJFCQRWL hat die Modellnummer 3800235261842 = EAN der Plug S MTR Gen3 (weiß) laut Shelly-Konformitätserklärung Nr. 180. Shelly führt sie als eingestellt, empfohlener Nachfolger Plug M Gen3 (Rückleistungsmessung dort unbelegt, deshalb nicht aufgenommen).
- Verfügbarkeit: am 26.10.2026 blockte Amazon den Check; die 4 ASINs sind noch ohne Eintrag (= gelten als verfügbar) und laufen ab dem nächsten Tageslauf mit.
- Die übliche Prüfung: hugo --minify, lychee, JSON-LD, Lighthouse, Screenshots bei 1440/768/390.
