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
