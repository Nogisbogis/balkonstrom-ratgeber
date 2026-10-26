# Balkonstrom-Ratgeber

Hugo-Quellcode für https://balkonstrom-ratgeber.de/ – Ratgeber zu Balkonkraftwerken & Powerstations.
Deploy automatisch per GitHub Actions bei jedem Push auf `main`. Details: siehe Betriebsanleitung im Blogbot-Arbeitsverzeichnis.

## Produktabbildungen

Feld `abbildung` je Modell in `data/*.yaml` (derzeit `img/illu/<slug>.svg`, erzeugt mit `tools/illus.py`;
später eine PA-API-Bild-URL). Rendering: `layouts/_partials/abbildung.html`. Amazon-Bilder nie herunterladen
oder selbst hosten. Details: README im Projektordner.

## Design v3 (Okt. 2026)

- Designsprache: `DESIGN.md` (WIRED aus VoltAgent/awesome-design-md, MIT) mit Abschnitt „Anpassung Balkonstrom-Ratgeber“: Serif (Systemschriften) für Überschriften und Erzähltext, Sans für Navigation, Buttons, Tabellen, Formulare; abgerundete Buttons (Pille, seit v3.1), keine Schatten außer Menü/fixierten Leisten, kräftige Linien statt Haarlinien.
- Fotos: nur frei lizenzierte Bilder von Wikimedia Commons in `assets/img/welt/`, Metadaten (Alt-Text, Urheber, Lizenz, Quelle) in `data/fotos.yaml`. Einbinden mit `{{ partial "foto.html" (dict "key" "camping" "sizes" "…" "lazy" true "cls" "…" "ratio" "4/3" "cap" "…") }}`; die Credits stehen automatisch im Fuß. Artikel bekommen ein Titelbild über `foto = '<key>'` im Front Matter (als „Symbolbild“ beschriftet). Keine Amazon-Bilder herunterladen oder hosten.
- `assets/js/ui.js`: nur noch der Laufzeit-Beleg auf der Startseite. Keine Lade-Animationen, kein Farbwechsel der Kopfleiste (v3.1). Inline im `<head>` setzt ein Einzeiler die Klasse `js`, damit JS-abhängige Bedienelemente ohne Layoutsprung erscheinen.
- Prüfskripte (lokal auf der Arbeitsmaschine unter `blogbot/gen/`, nicht im Repo): `sitecheck.py BASE` (alle Sitemap-URLs: 200, kein Überlauf bei 1440/768/390, Hinweis, rel=sponsored, JSON-LD), `pwshots.sh BASE PREFIX` (Screenshots).

## Börsenstrompreis-Widget (Okt. 2026)

- Feed: `tools/strompreis_feed.py` holt im Pages-Workflow („Deploy Hugo site to Pages“, Schritt „Strompreis-Feed“) den Day-Ahead-Preis DE-LU von `api.energy-charts.info/price` und schreibt `static/api/strompreis.json` → live unter `/api/strompreis.json`. Zeitfenster heute 00:00 bis morgen 23:45 Europe/Berlin (morgen erst ab ca. 13 Uhr verfügbar).
- Aktualisierung: Cron `7,37 * * * *` (alle 30 min, GitHub verzögert Cron oft um einige Minuten) plus jeder Push und `workflow_dispatch`. Die Datei wird nicht committet (`.gitignore`).
- Ausfall der API: Feed der Live-Seite wird übernommen (`"stale": true`), sonst `"available": false`. Das Widget zeigt nur Werte, deren Stunde im Feed vorkommt, sonst „gerade nicht verfügbar“.
- Anzeige: `layouts/_partials/strompreis.html` + `assets/js/strompreis.js` auf `/werkzeuge/` und `/amortisationsrechner/` (dort nur zum Vergleich, nicht als Vorgabe, weil der Börsenpreis keine Netzentgelte/Steuern enthält). Der Browser ruft nur die eigene Domain ab, keine Drittanbieter-Anfrage, daher keine Änderung an der Datenschutzerklärung nötig.
- Umrechnung: ct/kWh = EUR/MWh ÷ 10. Quelle im UI: CC BY 4.0 Bundesnetzagentur | SMARD.de via energy-charts (Fraunhofer ISE).
