# Balkonstrom-Ratgeber

Hugo-Quellcode für https://balkonstrom-ratgeber.de/ – Ratgeber zu Balkonkraftwerken & Powerstations.
Deploy automatisch per GitHub Actions bei jedem Push auf `main`. Details: siehe Betriebsanleitung im Blogbot-Arbeitsverzeichnis.

## Produktabbildungen

Feld `abbildung` je Modell in `data/*.yaml` (derzeit `img/illu/<slug>.svg`, erzeugt mit `tools/illus.py`;
später eine PA-API-Bild-URL). Rendering: `layouts/_partials/abbildung.html`. Amazon-Bilder nie herunterladen
oder selbst hosten. Details: README im Projektordner.
