---
title: Growatt NEXA 2000
modell: Growatt NEXA 2000
layout: bkw-produkt
date: '2026-10-19'
lastmod: '2026-10-19'
description: 'Growatt NEXA 2000 (2,048 kWh, 4 MPPT bis 2.600 W, IP66, 800-W-Notstrom): Datenblatt mit Quellen, Tests von COMPUTER BILD und Stiftung Warentest.'
kurzzeile: 2,048 kWh, 4 MPPT bis 2.600 W, IP66, Notstrom 800 W
kurzfazit: Der NEXA 2000 speichert 2,048 kWh, hat vier MPPT mit zusammen 2.600 W und als einziges Gerät im Vergleich Schutzart IP66. Erweiterbar ist er auf 8,2 kWh. Die Notstromsteckdose liefert 800 W, weniger als bei Anker, EcoFlow oder Zendure. COMPUTER BILD bewertet ihn mit 4,3 von 5 und kritisiert die umständliche App-Einrichtung. Stiftung Warentest hat ihn im März 2026 geprüft; die Note ist kostenpflichtig. Zertifikate nennt Growatt im Datenblatt (VDE-AR-N 4105).
fuer:
- Aufstellung im Freien bei Wind und Wetter (IP66 laut Datenblatt)
- Wer 2 kWh Speicher und vier Modul-Eingänge sucht
- Wer später auf bis zu 8 kWh erweitern will
nicht_fuer:
- Notstrom für Geräte über 800 W
- Wer eine einfache App-Einrichtung erwartet (Kritik von COMPUTER BILD)
quellen:
- id: db
  titel: 'Growatt: NEXA 2000 Datenblatt DE (04/2025)'
  url: https://de.growatt.com/upload/file/Nexa2000_Datenblatt_202504_DE.pdf
  art: Hersteller-Datenblatt
- id: swd
  titel: 'Stiftung Warentest: Growatt Nexa 2000 – Produktmerkmale'
  url: https://www.test.de/speicher-fuer-balkonkraftwerke-test-6278221-detail/320000039340!4/
  art: Test, Messwerte teils frei
- id: swt
  titel: 'Stiftung Warentest: Speicher für Balkonkraftwerke im Test (19.03.2026, test 4/2026)'
  url: https://www.test.de/speicher-fuer-balkonkraftwerke-test-6278221-0/
  art: Test, Einzelnoten kostenpflichtig
- id: bvss
  titel: 'Bundesverband Steckersolar e.V.: Pressemitteilung zum Warentest-Speichertest (19.03.2026)'
  url: https://sh1.sendinblue.com/3g884dus6f9pfe.html?t=1773947374900
  art: Verband, Stellungnahme
- id: cb
  titel: 'COMPUTER BILD: Growatt Nexa 2000 getestet (04.12.2025)'
  url: https://www.computerbild.de/artikel/Tests-Energie-Balkonkraftwerk-Growatt-Nexa-2000-Test-40564259.html
  art: Test
daten:
- gruppe: Akku
- k: Kapazität
  v: 2.048 Wh (51,2 V)
  q: db
  hinweis: 'Stiftung Warentest: 2,05 kWh laut Anbieter.'
- k: Zellchemie
  v: LiFePO4
  q: db
- k: Erweiterung
  v: Zusatzbatterien à 2.048 Wh, max. 8.192 Wh
  q: db
- k: Ladeleistung
  v: max. 2.000 W
  q: db
- k: Temperatur
  v: Laden 0–55 °C, Entladen −20–55 °C; Start ab −20 °C mit Selbstheizung
  q: db
- gruppe: Solar (DC)
- k: MPPT
  v: 4, je 1 String
  q: db
- k: PV-Eingang max.
  v: 2.600 W
  q: db
- k: Spannungsbereich
  v: 16–60 V, max. 20 A je Eingang
  q: db
- gruppe: Netz und Notstrom (AC)
- k: Netz-Ausgang
  v: 800 W (3,5 A)
  q:
  - db
  - swd
- k: Notstrom-Steckdose
  v: 800 W
  q:
  - db
  - swd
- k: „Power+“
  v: 'Ausgangsleistung manuell einstellbar (Grafik: 800 W / 1.000 W)'
  q: db
  hinweis: Für ein Steckersolargerät gelten höchstens 800 VA Wechselrichterleistung.
- k: Zertifizierung
  v: VDE-AR-N 4105:2018, EN 50549, IEC 62109, IEC 62619 u. a. (laut Datenblatt)
  q: db
  hinweis: Ein Einheitenzertifikat selbst habe ich nicht eingesehen.
- gruppe: Allgemein
- k: Schutzart
  v: IP66
  q:
  - db
  - swd
- k: Maße / Gewicht
  v: 406 × 255 × 290 mm, ca. 24 kg
  q:
  - db
  - swd
  hinweis: Stiftung Warentest wog 23,7 kg.
- k: Smart Meter
  v: Shelly Pro 3EM, Shelly 3EM, GroPlug
  q: db
- k: App
  v: ja, WLAN und Bluetooth, LED-Anzeige
  q: db
- k: Garantie
  v: 10 Jahre
  q: db
widersprueche:
- t: '**Datenblatt-Tippfehler:** Bei der Erweiterungsbatterie steht „Batteriekapazität 2000W“, gemeint ist offenbar die Leistung; die Nennkapazität ist mit 2.048 Wh angegeben.'
  q: db
staerken:
- t: IP66 und Start bei −20 °C mit Selbstheizung
  q: db
- t: Vier MPPT bis 2.600 W, je Eingang bis 20 A (laut Growatt für Module bis 650 W)
  q: db
- t: 'COMPUTER BILD: erweiterbar, Leistung smart steuerbar, notstromfähig'
  q: cb
schwaechen:
- t: Notstrom nur 800 W
  q:
  - db
  - swd
- t: 'COMPUTER BILD: Einrichtung in der App umständlich'
  q: cb
- t: 'Stiftung Warentest: Wasser drang bei vier von fünf Geräten in die Steckdose; welche, steht im kostenpflichtigen Teil'
  q: swt
tests:
- name: Stiftung Warentest
  datum: 19.03.2026
  url: https://www.test.de/speicher-fuer-balkonkraftwerke-test-6278221-detail/320000039340!4/
  urteil: Note nur im kostenpflichtigen Teil
  text: 'Im Test mit vier weiteren Speichern (Funktion 60 %, Handhabung 25 %, EMV, Sicherheit und Datenschutz je 5 %). Frei zugänglich: Drei der fünf Geräte erhielten „mangelhaft“, weil sie zu viele elektromagnetische Störsignale aussenden; beim Starkregentest drang bei vier Geräten Wasser in die integrierten Steckdosen. Welche Geräte betroffen sind, steht im kostenpflichtigen Teil; ich habe ihn nicht eingesehen. Frei sichtbar: gemessen 23,7 kg, Off-Grid-Leistung 800 W. Der Bundesverband Steckersolar kritisiert die Abwertungsregel, nach der ein einzelnes schwaches Prüfkriterium das Gesamturteil auf „mangelhaft“ ziehen kann.'
- name: COMPUTER BILD
  datum: 04.12.2025
  url: https://www.computerbild.de/artikel/Tests-Energie-Balkonkraftwerk-Growatt-Nexa-2000-Test-40564259.html
  urteil: Bewertung 4,3 von 5 (laut Seitendaten)
  text: 'Plus: erweiterbare Speicherkapazität, Leistung smart steuerbar, notstromfähig. Minus: Einrichtung in der App etwas umständlich. Fazit: „ein solider, erweiterbarer Energiespeicher“.'
alternativen:
- slug: zendure-solarflow-800-pro
  warum: 1,92 kWh, Notstrom 1.000 W mit automatischer Umschaltung.
- slug: anker-solix-solarbank-3-e2700-pro
  warum: Mehr Akku (2,7 kWh) und 1.200-W-Steckdose, aber 5 kg schwerer.
---
