---
title: Zendure SolarFlow 800 Pro
modell: Zendure SolarFlow 800 Pro
layout: bkw-produkt
date: '2026-10-19'
lastmod: '2026-10-19'
description: 'Zendure SolarFlow 800 Pro (1,92 kWh, 48 V, 4 MPPT bis 2.640 W, 1.000-W-Notstrom): Daten mit Quellen, VDE-Zertifikat, Tests von COMPUTER BILD, heise und Stiftung Warentest.'
kurzzeile: 1,92 kWh (48 V), 4 MPPT bis 2.640 W, 1.000 W Notstrom
kurzfazit: Der SolarFlow 800 Pro speichert 1,92 kWh in einem 48-V-Akku, hat vier MPPT mit zusammen 2.640 W und eine Notstromsteckdose mit 1.000 W. Laut Zendure schaltet sie bei Stromausfall in 15 ms um, wenn die Funktion in der App aktiv ist. COMPUTER BILD und heise loben Effizienz, Notstrom und Smart-Meter-Regelung; Kritik gibt es an Kalibrierungs-Entladungen und der Cloud-Abhängigkeit. Stiftung Warentest führt das Gerät als „nicht mehr im Handel“, Zendure verkauft es im eigenen Shop weiter. Einen passenden Amazon-Link habe ich nicht.
fuer:
- Wer viel Modulleistung über vier Eingänge verteilen will (je 660 W)
- 'Smart-Home-Nutzer: lokale API und Home Assistant laut heise'
- Wer Notstrom mit automatischer Umschaltung möchte (1.000 W, kurz 1.200 W)
nicht_fuer:
- 'Wer ohne Cloud-Konto arbeiten will: laut heise standardmäßig cloudabhängig'
- Wer 2.000-W-Geräte über die Notstromsteckdose betreiben will
quellen:
- id: shop
  titel: 'Zendure DE: SolarFlow 800 Pro – Produktseite, Spezifikation und FAQ'
  url: https://www.zendure.de/products/solarflow-800-pro
  art: Hersteller
- id: hb
  titel: 'Zendure: SolarFlow 800 Pro Benutzerhandbuch (EN, bei selfio hinterlegt)'
  url: https://media.selfio.de/downloads/pdf/SolarFlow-800-Pro-User-Manual-EN-compressed.pdf
  art: Hersteller-Handbuch
- id: gar
  titel: 'Zendure DE: Garantiebestimmungen'
  url: https://www.zendure.de/pages/garantiebestimmungen
  art: Hersteller
- id: vde
  titel: 'Intertek: Einheitenzertifikat CN-PVES-250221 (ZDSF800P) nach VDE-AR-N 4105'
  url: https://www.oekostromhelden.de/wp-content/themes/oekostromhelden/datasheets/CN-PVES-250221_Security.pdf
  art: Zertifikat
- id: swd
  titel: 'Stiftung Warentest: Zendure SolarFlow 800 Pro – Produktmerkmale'
  url: https://www.test.de/speicher-fuer-balkonkraftwerke-test-6278221-detail/320000039340!6/
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
  titel: 'COMPUTER BILD: Zendure Solarflow 800 Pro im Praxis-Test (20.01.2026)'
  url: https://www.computerbild.de/artikel/Tests-Energie-Zendure-Solarflow-800-Pro-Test-00877-40675967.html
  art: Test
- id: heise
  titel: 'heise bestenlisten: Zendure Solarflow 800 Pro im Test (21.07.2026)'
  url: https://www.heise.de/bestenlisten/testbericht/zendure-solarflow-800-pro-im-test-inzwischen-sehr-guenstig/29cqkhv
  art: Test
daten:
- gruppe: Akku
- k: Kapazität
  v: 1.920 Wh, 48 V
  q:
  - shop
  - hb
- k: Zellchemie
  v: LiFePO4 (LFP)
  q: shop
- k: Lade-/Entladeleistung
  v: 1.440 W ohne, 2.000 W mit Zusatzakku
  q:
  - shop
  - hb
- k: Erweiterung
  v: bis 5 Zusatzakkus (AB1000/AB2000-Serie), max. 11.520 Wh
  q: shop
- k: Temperatur
  v: Laden 0–55 °C, Entladen −20–55 °C
  q:
  - shop
  - hb
- gruppe: Solar (DC)
- k: MPPT
  v: 4, je max. 660 W
  q: shop
- k: PV-Eingang max.
  v: 2.640 W
  q:
  - shop
  - hb
- k: Spannungsbereich
  v: 14–55 V, je Eingang 18 A (Isc 22,5 A)
  q: shop
  hinweis: 'Zendure warnt: mehr als 55 V Leerlaufspannung kann das Gerät dauerhaft beschädigen.'
- gruppe: Netz und Notstrom (AC)
- k: Netz-Ausgang
  v: 800 W (3,5 A)
  q:
  - shop
  - vde
- k: Notstrom-Steckdose
  v: 1.000 W, 10 s bis 1.200 W
  q: shop
  hinweis: Off-Grid-Funktion muss in der App aktiviert sein; Umschaltung laut Zendure in 15 ms. Netz und Off-Grid zusammen max. 1.000 W.
- k: Laden aus dem Netz
  v: max. 1.000 W
  q: shop
- k: Zertifizierung
  v: VDE-AR-N 4105:2018-11 (Einheitenzertifikat CN-PVES-250221)
  q: vde
- gruppe: Allgemein
- k: Schutzart
  v: IP65 – nicht bei offener Off-Grid-Abdeckung
  q: shop
- k: Maße
  v: 338,6 × 226 × 358 mm (Handbuch)
  q:
  - hb
  - shop
  hinweis: 'FAQ der Produktseite: 349,7 × 201,7 × 340 mm.'
- k: Gewicht
  v: 25,9 kg
  q:
  - shop
  - swd
  hinweis: Stiftung Warentest wog 26,0 kg.
- k: App
  v: ja, WLAN 2,4 GHz und Bluetooth
  q: shop
- k: Garantie
  v: 10 Jahre
  q: gar
widersprueche:
- t: '**Maße:** Handbuch 338,6 × 226 × 358 mm, Produktseiten-FAQ 349,7 × 201,7 × 340 mm.'
  q:
  - hb
  - shop
- t: '**Verfügbarkeit:** Stiftung Warentest führt das Gerät als „nicht mehr im Handel“ (Stand 27.09.2026), Zendure verkauft es im eigenen Shop.'
  q:
  - swd
  - shop
staerken:
- t: Vier MPPT mit je 660 W, Start laut Zendure schon ab 14 V
  q: shop
- t: Notstrom mit automatischer Umschaltung (15 ms laut Zendure)
  q: shop
- t: 'COMPUTER BILD: Akkuheizung sprang im Winter zuverlässig an; Laden aus dem Netz verhindert Tiefentladung'
  q: cb
- t: 'heise: arbeitet mit Shelly Pro 3EM zuverlässig und effizient; lokale API und Home Assistant'
  q: heise
schwaechen:
- t: 'COMPUTER BILD: teils unangekündigte Kalibrierungs-Entladungen; App etwas verschachtelt'
  q: cb
- t: 'heise: standardmäßig von der Cloud abhängig'
  q: heise
- t: 'Stiftung Warentest: Ob der SolarFlow zu den drei Geräten mit „mangelhaft“ gehört, steht im kostenpflichtigen Teil'
  q: swt
tests:
- name: Stiftung Warentest
  datum: 19.03.2026
  url: https://www.test.de/speicher-fuer-balkonkraftwerke-test-6278221-detail/320000039340!6/
  urteil: Note nur im kostenpflichtigen Teil
  text: 'Im Test mit vier weiteren Speichern (Funktion 60 %, Handhabung 25 %, EMV, Sicherheit und Datenschutz je 5 %). Frei zugänglich: Drei der fünf Geräte erhielten „mangelhaft“, weil sie zu viele elektromagnetische Störsignale aussenden; beim Starkregentest drang bei vier Geräten Wasser in die integrierten Steckdosen. Welche Geräte betroffen sind, steht im kostenpflichtigen Teil; ich habe ihn nicht eingesehen. Frei sichtbar: gemessen 26,0 kg, Off-Grid-Leistung 1.000 W. Der Bundesverband Steckersolar kritisiert die Abwertungsregel, nach der ein einzelnes schwaches Prüfkriterium das Gesamturteil auf „mangelhaft“ ziehen kann.'
- name: COMPUTER BILD
  datum: 20.01.2026
  url: https://www.computerbild.de/artikel/Tests-Energie-Zendure-Solarflow-800-Pro-Test-00877-40675967.html
  urteil: Bewertung 4,7 von 5 (laut Seitendaten)
  text: 'Plus: notstromfähig, erweiterbar, per Netzstrom aufladbar. Minus: Akku entlädt zur Kalibrierung, App etwas verschachtelt. Fazit: „ein sehr attraktiver Einstieg in die Solarstrom-Speicherung“ (zum damaligen Preis).'
- name: heise bestenlisten
  datum: 21.07.2026
  url: https://www.heise.de/bestenlisten/testbericht/zendure-solarflow-800-pro-im-test-inzwischen-sehr-guenstig/29cqkhv
  urteil: Bewertung 4,5 von 5 (laut Seitendaten)
  text: 'Plus: effizienter Wechselrichter mit vier MPPT, Nulleinspeisung per Shelly Pro 3EM, bidirektionales Laden, lokale API. Minus: standardmäßig cloudabhängig, App teilweise unübersichtlich. Laut heise lohnt sich Netzladen bei dynamischen Tarifen erst, wenn der Preisunterschied deutlich über 20 % liegt.'
alternativen:
- slug: anker-solix-solarbank-2-e1600-pro
  warum: Ähnliche Klasse mit 1,6 kWh, Notstrom 1.000 W, gültiges VDE-Zertifikat, Amazon-Link vorhanden.
- slug: growatt-nexa-2000
  warum: 2,048 kWh, IP66, Notstrom 800 W.
---
