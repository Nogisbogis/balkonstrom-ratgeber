+++
title = "Laufzeitrechner: Wie lange hält meine Powerstation?"
description = "Laufzeitrechner für Powerstations: Geräte mit Watt und Stunden eintragen, Modell oder Kapazität wählen, Laufzeit sehen. Wirkungsgrad als einstellbare Annahme (Standard 85 %)."
layout = "rechner"
date = 2026-10-19
intro = "Trag deine Geräte ein und wähle ein Modell. Der Rechner zeigt, ob der Akku reicht – für alle zehn Powerstations aus meinem Vergleich auf einen Blick. Er rechnet nur im Browser, nichts wird gespeichert."
+++

## So rechnet der Rechner

- **Bedarf pro Ladung** = Summe aus Watt × Stunden × Anzahl.
- **Nutzbare Energie** = Nennkapazität × Wirkungsgrad. Der Wirkungsgrad ist eine **Annahme**. Standard sind 85 %, du kannst ihn ändern.
- **Dauerbetrieb** = nutzbare Energie ÷ (Leistung aller Geräte + Eigenverbrauch).
- **Warnung**, wenn alle Geräte zusammen mehr Watt brauchen, als die Station dauerhaft liefert. Maßgeblich ist die Dauerleistung laut Hersteller, nicht die Spitze.

## Warum 85 % – und warum du das ändern solltest

Powerstations geben nie die volle Nennkapazität ab. Bei der Umwandlung auf 230 V geht Energie verloren, und bei kleiner Last arbeiten viele Wechselrichter weniger effizient.

- **ADAC (2025):** Die nutzbare Kapazität lag im Schnitt 10 bis 15 % unter der Angabe. Manche Wechselrichter brauchten selbst schon rund 30 W.
- **IMTEST:** Bei der EcoFlow RIVER 3 waren 224 von 245 Wh nutzbar (gut 91 %), bei der DJI Power 1000 Mini 757 von 1.008 Wh (rund 75 %), jeweils bei rund 80 W Last.
- **Notebookcheck:** Bei der Anker SOLIX C2000 Gen 2 waren es knapp 79 % bei 200 W und gut 90 % bei 1.800 W.
- **CHIP** misst einen Gesamtwirkungsgrad, also Laden und Entladen zusammen, und kommt je nach Modell auf 63 bis 79 %. Das ist eine andere Größe als der nutzbare Anteil hier.

Für kleine Lasten über die Steckdose rechne lieber mit 75–80 %. Für USB- und 12-V-Geräte ohne Wechselrichter darf der Wert höher liegen. Der Eigenverbrauch ist ebenfalls eine Annahme: Jackery nennt als Standby-Leistung 12 W (Explorer 300 Plus) bzw. 18 W (Explorer 1000 v2), Anker für die C2000 Gen 2 unter 10 W im Leerlauf.

## Grenzen

- Geräte mit Motor oder Kompressor, etwa Kühlschrank oder Werkzeug, brauchen beim Anlaufen kurz deutlich mehr Leistung. Diese Spitzen rechnet das Tool nicht ein.
- Kühlgeräte laufen nicht ständig. Für die Stunden zählt nur die Zeit, in der der Kompressor arbeitet; Angaben dazu stehen oft im Datenblatt.
- Kälte verringert die nutzbare Kapazität. Beachte die Temperaturangaben auf den Produktseiten.

Passt die Station nicht? Der [Powerstation-Finder](/powerstation-finder/) schlägt Modelle anhand deiner Angaben vor.

{{< quellen >}}
- ADAC: [Mobile Powerstations im Test 2025](https://www.adac.de/rund-ums-haus/energie/versorgung/mobile-powerstations-test/), 11.06.2025
- IMTEST: [Mini-Powerstations im Test](https://www.imtest.de/energie/mini-powerstation-testsieger-2026-hohe-leistung-klein/522617/) und [DJI Power 1000 Mini im Test](https://www.imtest.de/energie/dji-power-1000-mini-im-test-kleine-powerstation-2026/619685/)
- Notebookcheck: [Anker Solix C2000 Gen 2 im Praxis-Test](https://www.notebookcheck.com/11-6-kg-leichter-als-der-Vorgaenger-Powerstation-Anker-Solix-C2000-Gen-2-im-Praxis-Test.1230097.0.html), 24.02.2026
- CHIP: [Powerstation-Bestenliste](https://www.chip.de/artikel/Powerstation-Test-Die-beste-Powerstation-mit-Solarpanel-Kompatibilitaet_184362262.html); [EcoFlow River 3 im Test](https://www.chip.de/test/ecoflow-river-3-im-test_332943)
- Jackery Helpcenter: [Explorer 300 Plus](https://helpcenter.eu.jackery.com/hc/en-gb/articles/52682971950363-Explorer-300-Plus-Basic-Information), [Explorer 1000 V2](https://helpcenter.eu.jackery.com/hc/de/articles/52683026571291-Explorer-1000-V2-Grundlegende-Informationen); Anker: [SOLIX C2000 Gen 2](https://www.ankersolix.com/de/c2000-gen2)
{{< /quellen >}}
