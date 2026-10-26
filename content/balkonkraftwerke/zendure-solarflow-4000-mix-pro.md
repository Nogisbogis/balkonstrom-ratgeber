---
title: Zendure SolarFlow 4000 Mix Pro
modell: Zendure SolarFlow 4000 Mix Pro
layout: bkw-produkt
date: '2026-10-26'
lastmod: '2026-10-26'
description: 'Zendure SolarFlow 4000 Mix Pro (8 kWh, 2 MPPT bis 8.000 W DC, dazu AC-PV, 3 kW Plug-and-Play, 80 kg): Daten von zendure.de, Stand 26.10.2026.'
kurzzeile: 8 kWh, zwei MPPT bis 8.000 W DC, 3 kW an der Steckdose
kurzfazit: 'Der SolarFlow 4000 Mix Pro hat laut FAQ zwei unabhängige MPPT und bis zu 8.000 W DC-PV (4.000 W × 2), Spannung 30–400 V, Start 30 V, Kurzschlussstrom 18 A je MPPT, nur Reihenschaltung. Zusammen mit bis zu 5 kW AC-gekoppelter PV nennt der Produkttext 13 kW PV-Gesamteingang. Plug-and-Play geht bis 3 kW, der Wechselrichter ist für 4 kW ausgelegt, 5 kW nur mit Festverdrahtung und externer AC-PV. Off-Grid: 3.680 W dauerhaft, 7.200 W für 200 ms. Gewicht 80 kg, IP65, 10 Jahre Garantie. Die FAQ zur Zyklenfrage nennt keine Testbedingung, sondern Ladeleistungen.'
fuer:
- Neuinstallation oder größere Strings mit Hochvolt-MPPT plus Speicher
- Wer DC- und AC-gekoppelte PV an einem 8-kWh-Gerät bündeln will
nicht_fuer:
- Parallelschaltung von Modulsträngen am selben MPPT
- Eine einzelne Einheit als Notstrom für das ganze Haus
quellen:
- id: hst
  titel: 'Zendure DE: SolarFlow 4000 Mix Pro – Produktseite und FAQ'
  url: https://www.zendure.de/products/solarflow-4000-mix-pro
  art: Hersteller
daten:
- gruppe: Akku
- k: Kapazität
  v: 8 kWh
  q: hst
- k: Zellchemie
  v: keine Angabe
  q: hst
- k: Zyklen
  v: Produkttext „10.000 Zyklen bei 70 % EOL SOH“, 15 Jahre, 10 Jahre Garantie
  q: hst
  hinweis: Unter der FAQ-Frage nach Zyklen und Testbedingungen steht stattdessen die Ladeleistung 4.000 W bzw. 10.000 W mit Zusatzbatterien.
- k: Laden, Einzelgerät
  v: nur PV, nur AC oder kombiniert jeweils bis 4 kW
  q: hst
- k: Laden mit Zusatzpacks
  v: PV bis 8 kW, AC bis 4 kW, kombiniert bis 10 kW
  q: hst
- k: Batterietemperatur
  v: Laden 0 °C bis 55 °C, Entladen −20 °C bis 55 °C
  q: hst
- gruppe: Solar (DC)
- k: MPPT
  v: 2 unabhängige, nur Reihe, nicht parallel
  q: hst
- k: PV-Eingang DC
  v: bis 8.000 W (4.000 W × 2), 30–400 V, Start 30 V, Isc 18 A je MPPT, Voc des Strings höchstens 400 V
  q: hst
- k: PV gesamt
  v: bis 13 kW (8 kW MPPT plus 5 kW AC-gekoppelte PV)
  q: hst
- gruppe: Netz und Notstrom (AC)
- k: Netz-Ausgang
  v: Plug-and-Play max. 3 kW; Wechselrichter für 4 kW ausgelegt
  q: hst
- k: Festverdrahtung
  v: bis 5 kW, nur zusammen mit externem AC-gekoppeltem PV-Eingang
  q: hst
- k: Inselbetrieb
  v: dauerhaft bis 3.680 W, Spitze 7.200 W für 200 ms; Produkttext nennt 10 ms USV
  q: hst
- gruppe: Allgemein
- k: Schutzart
  v: IP65
  q: hst
- k: Betriebstemperatur
  v: −20 °C bis 55 °C
  q: hst
- k: Gewicht
  v: 80 kg, Rollen und Stützfüße
  q: hst
- k: Maße
  v: keine Angabe
  q: hst
- k: Geräusch
  v: etwa 25 dB bei 2.000 W, 1 m, 25 °C; Volllast im Produkttext etwa 40 dB, in der FAQ etwa 43 dB
  q: hst
- k: Ganzes Haus
  v: eine Einheit allein versorgt laut FAQ nicht das ganze Haus im Off-Grid-Betrieb
  q: hst
- k: Garantie
  v: 10 Jahre
  q: hst
staerken:
- t: Zwei Hochvolt-MPPT bis 8.000 W DC und zusätzlich AC-PV
  q: hst
- t: 8 kWh, 3.680 W Off-Grid-Dauerleistung, IP65, 80 kg genannt
  q: hst
schwaechen:
- t: 5 kW Netzausgang nur unter den engen FAQ-Bedingungen
  q: hst
- t: Die Zyklen-FAQ beantwortet die Frage nach den Testbedingungen nicht
  q: hst
widersprueche:
- t: '**Zyklen:** Der Produkttext nennt 10.000 Zyklen bei 70 % EOL SOH. Die FAQ-Antwort auf die Frage nach Zyklen und Testbedingungen beschreibt die Ladeleistung (4.000 W bzw. 10.000 W) und keine Prüfbedingung wie 0,5C.'
  q: hst
- t: '**Lautstärke:** Volllast etwa 40 dB im Produkttext und etwa 43 dB in der FAQ.'
  q: hst
tests_hinweis: Unabhängige Tests (z. B. Stiftung Warentest, COMPUTER BILD, CHIP, heise) habe ich für dieses Modell bis zum 26.10.2026 nicht ausgewertet; hier stehen deshalb nur Herstellerangaben.
alternativen:
- slug: zendure-solarflow-4000-mix-ac
  warum: Gleiche Kapazität ohne DC-MPPT, wenn die Anlage schon einen Dach-Wechselrichter hat.
- slug: anker-solix-solarbank-max
  warum: Ebenfalls großer Speicher mit hohem PV-Eingang, anderer Hersteller.
---
