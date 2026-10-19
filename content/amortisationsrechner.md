+++
title = "Lohnt sich mein Balkonkraftwerk? Amortisationsrechner"
linktitle = "Amortisationsrechner"
description = "Amortisationsrechner fürs Balkonkraftwerk: Modulleistung, Ertrag, Eigenverbrauch, Strompreis und Kosten eingeben. Alle Annahmen offen und mit Quelle."
layout = "amortisation"
date = 2026-10-19
intro = "Trag deine Anlage und deinen Strompreis ein. Der Rechner zeigt, wann sich das Balkonkraftwerk bezahlt macht – und wie stark das von den Annahmen abhängt. Er rechnet nur im Browser, nichts wird gespeichert."
[[presets]]
name = "Süd, senkrecht am Balkon – 665 kWh/kWp (Umweltbundesamt)"
wert = 665
standard = true
[[presets]]
name = "Süd, senkrecht am Balkon – 700 kWh/kWp (Verbraucherzentrale)"
wert = 700
[[presets]]
name = "Süd, optimal geneigt (30–40°) – 950 kWh/kWp (Umweltbundesamt)"
wert = 950
+++

## So rechnet der Rechner

- **Jahresertrag** = Modulleistung in kWp × spezifischer Ertrag (kWh pro kWp und Jahr).
- **Selbst genutzt** = Jahresertrag × Eigenverbrauchsanteil. Nur dieser Strom spart Geld. Was ins Netz fließt, wird bei Steckersolargeräten in der Regel nicht vergütet.
- **Ersparnis pro Jahr** = selbst genutzte kWh × Arbeitspreis.
- **Amortisation** = Anschaffungskosten ÷ Ersparnis pro Jahr. Mit Strompreisänderung zählt der Rechner Jahr für Jahr zusammen.

## Woher die Standardwerte kommen

Alle vorgegebenen Werte sind **Annahmen** aus öffentlichen Quellen. Du kannst jeden davon ändern.

- **Ertrag 950 bzw. 665 kWh/kWp:** Das Umweltbundesamt rechnet für optimal geneigte Südmodule mit 950 Volllaststunden pro Jahr. Senkrecht am Balkon sinke der Ertrag um rund 30 % auf 665 Stunden.
- **Ertrag 700 kWh/kWp:** Die Verbraucherzentrale nennt für ein unverschattetes 400-W-Modul senkrecht am Südbalkon etwa 280 kWh im Jahr.
- **Eigenverbrauch 45 %:** Laut Umweltbundesamt werden ohne Speicher im Durchschnitt 45 % zeitgleich im Haushalt verbraucht. Im Beispiel der Verbraucherzentrale mit nur einem Modul sind es rund 70 % (200 von 280 kWh). Je kleiner die Anlage im Verhältnis zur Grundlast, desto höher der Anteil.
- **Strompreis 37 ct/kWh:** Diesen Arbeitspreis setzt das Umweltbundesamt in seinem Rechenbeispiel an. Trag am besten den Preis von deiner Rechnung ein.
- **20 Jahre:** Ein vorsichtiger Wert. Die Verbraucherzentrale schreibt, ein Modul könne über 25 Jahre eingesetzt werden. Für die Solarbank nennt Anker eine Lebensdauer von 15 Jahren.

Zum Vergleich: Das Umweltbundesamt kommt für 800 W senkrecht, 45 % Eigenverbrauch, 37 ct und 400 € Kosten auf knapp fünf Jahre. Die Verbraucherzentrale nennt für Geräte ohne Speicher meist drei bis fünf Jahre.

## Und mit Speicher?

Ein Speicher erhöht den Eigenverbrauchsanteil, kostet aber deutlich mehr. Beim Ein- und Ausspeichern geht zudem Energie verloren. Das Umweltbundesamt hält Speicher bei durchschnittlichem Verbrauch „eher nicht“ für lohnend. Pauschal belastbare Werte für den Eigenverbrauch mit Speicher habe ich nicht gefunden. Rechne deinen Fall mit dem [Stecker-Solar-Simulator der HTW Berlin](https://solar.htw-berlin.de/rechner/stecker-solar-simulator/) und trag den Anteil hier ein. Mehr dazu im Artikel [Balkonkraftwerk mit Speicher: Lohnt sich das?](/posts/balkonkraftwerk-mit-speicher-lohnt-sich/).

## Grenzen

- Verschattung, Ost-/Westlage und Modulneigung verändern den Ertrag stark. Den Wert für deinen Standort liefern PVGIS oder der HTW-Simulator.
- Der Rechner berücksichtigt weder Alterung der Module noch Wechselrichterverluste über die Annahme hinaus noch Grundgebühren.
- Über 960 Wp ist laut Umweltbundesamt der normale Schukostecker nicht mehr normgerecht. Über 2.000 Wp gelten die vereinfachten Regeln für Steckersolargeräte nicht mehr.

Geräte im Detail: [Balkonkraftwerke und Speicher](/balkonkraftwerke/#modelle).

{{< quellen >}}
- Umweltbundesamt: [Steckersolargeräte reduzieren eigene Stromkosten](https://www.umweltbundesamt.de/umwelttipps-fuer-den-alltag/steckersolargeraete-reduzieren-eigene-stromkosten)
- Verbraucherzentrale: [Steckersolar: Solarstrom vom Balkon direkt in die Steckdose](https://www.verbraucherzentrale.de/wissen/energie/erneuerbare-energien/steckersolar-solarstrom-vom-balkon-direkt-in-die-steckdose-44715), Stand 24.07.2026
- Energieberatung der Verbraucherzentrale: [Balkonkraftwerk](https://verbraucherzentrale-energieberatung.de/erneuerbare-energien/photovoltaik/balkonkraftwerk/)
- HTW Berlin: [Stecker-Solar-Simulator](https://solar.htw-berlin.de/rechner/stecker-solar-simulator/); EU-Kommission JRC: [PVGIS](https://re.jrc.ec.europa.eu/pvg_tools/de/)
- Anker SOLIX: [Solarbank 3 E2700 Pro, technische Details](https://www.ankersolix.com/it/products/a17c53z1)
{{< /quellen >}}
