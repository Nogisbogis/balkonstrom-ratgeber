---
title: EcoFlow STREAM Pro
modell: EcoFlow STREAM Pro
layout: bkw-produkt
date: '2026-10-19'
lastmod: '2026-10-19'
description: 'EcoFlow STREAM Pro (1,92 kWh, 3 MPPT bis 1.500 W, 1.200-W-Steckdosen): technische Daten mit Quellen aus dem Handbuch, Unterschiede zum STREAM Ultra, Testlage.'
kurzzeile: 1,92 kWh, 3 MPPT bis 1.500 W, Steckdosen 1.200 W
kurzfazit: 'Der STREAM Pro ist laut EcoFlow-Handbuch technisch der STREAM Ultra mit einem Modul-Eingang weniger: 3 MPPT, zusammen 1.500 W PV, 22,8 kg. Akku (1,92 kWh LFP), Steckdosen (1.200 W) und Netzbetrieb (bis 2.300 W für angeschlossene Geräte) sind gleich. Eigene unabhängige Tests zum Pro habe ich nicht gefunden. Die Tests zum Ultra lassen sich nur eingeschränkt übertragen, auch die EMV-Kritik der Stiftung Warentest nicht. Eine Garantieangabe für den Pro fehlt auf der deutschen EcoFlow-Seite.'
fuer:
- Wer höchstens drei Module anschließt und die Funktionen des Ultra will
- Verteilte Speicher im Haus (Verbund bis 6 STREAM-Geräte)
- Geräte direkt am Speicher betreiben (bis 1.200 W ohne, 2.300 W mit Netz)
nicht_fuer:
- Wer vier Module oder mehr als 1.500 W PV anschließen will
- Wer sich auf unabhängige Tests genau dieses Modells stützen möchte
quellen:
- id: hb
  titel: 'EcoFlow: STREAM Ultra & Pro User Manual (EN)'
  url: https://ecoflow-service-us-prod.oss-us-west-1.aliyuncs.com/cms/manual/1750903136593/EcoFlow%20STREAM%20Ultra%20%26%20Pro_User%20Manual.pdf
  art: Hersteller-Handbuch
- id: shop
  titel: 'EcoFlow DE: STREAM Series – Spezifikation und FAQ'
  url: https://de.ecoflow.com/pages/stream-series-plug-in-battery
  art: Hersteller
- id: vde
  titel: 'SGS: Einheitenzertifikat 250082RECO05-A-CER (STREAM Ultra/Pro/AC Pro) nach VDE-AR-N 4105 (bei Powerness hinterlegt)'
  url: https://www.powerness.de/cdn/shop/files/EcoFlow_STREAM_Ultra_Grid_Certificate-DE.pdf?v=4436621794854187166
  art: Zertifikat
- id: amz
  titel: 'Amazon.de: Angebotstitel zu ASIN B0F5B7WDQ4'
  url: https://www.amazon.de/dp/B0F5B7WDQ4
  art: Händlerangabe
- id: cb
  titel: 'COMPUTER BILD: EcoFlow Stream Ultra im Test (nennt Preise der Serie)'
  url: https://www.computerbild.de/artikel/Tests-Energie-EcoFlow-Stream-Balkonkraftwerk-Speicher-Ikea-Kauf-39780725.html
  art: Test (Ultra)
daten:
- gruppe: Akku
- k: Kapazität
  v: 1,92 kWh (19,2 V)
  q: hb
- k: Zellchemie
  v: LiFePO4 (LFP)
  q: hb
- k: Zyklen
  v: 6.000 (0,5C, 25 °C)
  q: hb
- k: Erweiterung
  v: Verbund bis 6 STREAM-Geräte
  q: hb
- gruppe: Solar (DC)
- k: MPPT
  v: 3, je max. 500 W
  q: hb
- k: PV-Eingang max.
  v: 1.500 W
  q: hb
  hinweis: Der Amazon-Angebotstitel nennt 2.300 W – siehe Widersprüche.
- k: Spannungsbereich
  v: 15–60 V, max. 14 A (Isc 20 A)
  q: hb
- gruppe: Netz und Steckdosen (AC)
- k: Netz-Ausgang
  v: 800 W (Variante mit 600 W existiert)
  q:
  - hb
  - vde
- k: Steckdosen am Gerät
  v: 1.200 W / 1.200 VA
  q: hb
- k: Max. Geräteleistung am Netz
  v: 2.300 W über den Parallel-Anschluss bzw. Bypass
  q: hb
- k: Zertifizierung
  v: VDE-AR-N 4105:2018-11 (Modell EF-EA-HD-P2K-800 im SGS-Zertifikat)
  q: vde
- gruppe: Allgemein
- k: Schutzart
  v: IP65, lüfterlos
  q: hb
- k: Temperatur
  v: −20 bis 55 °C
  q: hb
- k: Maße / Gewicht
  v: 255 × 284 × 458 mm, 22,8 kg
  q: hb
- k: App
  v: ja, WLAN und Bluetooth
  q: hb
- k: Garantie
  v: keine Angabe für den Pro gefunden
  q: shop
  hinweis: Für STREAM Ultra und AC Pro nennt EcoFlow 10 Jahre.
widersprueche:
- t: '**PV-Eingang:** Handbuch 1.500 W (3 × 500 W), Amazon-Angebotstitel „2300W Solareingang“. Die 2.300 W entsprechen der maximalen Geräteleistung am Netz, nicht dem PV-Eingang laut Handbuch.'
  q:
  - hb
  - amz
- t: '**Maximale Kapazität:** Amazon-Titel und EcoFlow-Seite 11,52 kWh, Fußnote der EcoFlow-Seite 11,92 kWh.'
  q:
  - amz
  - shop
staerken:
- t: Gleiche Steckdosen- und Netzfunktionen wie der Ultra
  q: hb
- t: Lüfterlos, IP65, Betrieb −20 bis 55 °C
  q: hb
- t: VDE-AR-N-4105-Einheitenzertifikat
  q: vde
schwaechen:
- t: Nur 3 MPPT, 1.500 W PV
  q: hb
- t: Keine eigenständigen unabhängigen Tests gefunden
  q: cb
- t: Garantie auf der deutschen EcoFlow-Seite nicht angegeben
  q: shop
tests:
- name: Keine eigenständigen Tests gefunden
  url: https://www.computerbild.de/artikel/Tests-Energie-EcoFlow-Stream-Balkonkraftwerk-Speicher-Ikea-Kauf-39780725.html
  text: COMPUTER BILD nennt den Pro im Test des Ultra nur mit Preis (999 Euro UVP zum Testzeitpunkt). Stiftung Warentest, CHIP und c't haben den Ultra geprüft. Deren Ergebnisse auf der [Seite zum STREAM Ultra](/balkonkraftwerke/ecoflow-stream-ultra/) gelten nur, soweit die Geräte baugleich sind; das hat kein Tester bestätigt.
alternativen:
- slug: ecoflow-stream-ultra
  warum: Vierter MPPT (2.000 W PV), 10 Jahre Garantie laut EcoFlow, mehrere Tests.
- slug: anker-solix-solarbank-2-e1600-pro
  warum: 4 MPPT, 1,6 kWh, Notstrom 1.000 W.
---
