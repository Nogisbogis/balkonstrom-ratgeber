---
title: Zendure SolarFlow 2400 AC
modell: Zendure SolarFlow 2400 AC
layout: bkw-produkt
date: '2026-10-26'
lastmod: '2026-10-26'
description: 'Zendure SolarFlow 2400 AC (AC-Koppler, nur mit AB3000X, ab 2,88 kWh, Ausgang standard 200 W): Daten von zendure.de, Stand 26.10.2026.'
kurzzeile: AC-Koppler, kleinste Shop-Variante 2,88 kWh, Standardausgang 200 W
kurzfazit: 'Der SolarFlow 2400 AC (ZDSF2400AC) ist ein AC-gekoppelter Speicher ohne eigenen PV-Eingang. Der Shop verkauft ihn nur zusammen mit mindestens einem Akku AB3000X. Die kleinste Variante ist mit 2,88 kWh beschriftet; die Spezifikation des AB3000X nennt 2.880 Wh. Bis zu sechs AB3000X ergeben laut FAQ und Spezifikation 17,28 kWh. Der Netzausgang steht laut FAQ standardmäßig auf 200 W und lässt sich nach Elektrofachbetrieb und App-Freigabe auf 2.400 W stellen. Eine Garantiedauer in Jahren nennt die Seite nicht.'
warnung: Die 2,88 kWh in der Übersicht sind die kleinste Shop-Variante (ein AB3000X), nicht eine in der Spezifikation genannte Kapazität des Koppler-Gehäuses. Die Wh-Angabe steht auf dem Reiter der Batterie AB3000X.
fuer:
- Nachrüstung eines vorhandenen PV-Systems, das schon einen Wechselrichter hat
- Wer die Kapazität in 2,88-kWh-Schritten mit AB3000X aufbauen will
nicht_fuer:
- Wer Module direkt anschließen will
- Wer AB1000- oder AB2000-Akkus aus einem älteren SolarFlow weiterverwenden will
quellen:
- id: hst
  titel: 'Zendure DE: SolarFlow 2400 AC – Produktseite, FAQ und Spezifikation'
  url: https://www.zendure.de/products/zendure-solarflow-2400-ac
  art: Hersteller
daten:
- gruppe: Akku
- k: Kleinste Shop-Variante
  v: 1× AB3000X, auf der Seite mit 2,88 kWh beschriftet
  q: hst
- k: Zellchemie des AB3000X
  v: LiFePO₄, 2.880 Wh, 60 Ah, 48 V
  q: hst
- k: Zyklen des AB3000X
  v: 6.000
  q: hst
  hinweis: Die Spezifikation nennt keine Testbedingungen zu diesen 6.000 Zyklen.
- k: Erweiterung
  v: nur AB3000X, bis zu 6 Stück, 17,28 kWh laut FAQ; Spezifikation rechnet 2.880 Wh × 6 = 17.280 Wh
  q: hst
- k: Nicht kompatibel
  v: AB1000, AB1000S, AB1000X, AB2000, AB2000S, AB2000X
  q: hst
- gruppe: Solar (DC)
- k: PV-Eingang
  v: keiner; Module lassen sich laut FAQ nicht anschließen
  q: hst
- gruppe: Netz und Notstrom (AC)
- k: Netz-Ausgang
  v: standardmäßig 200 W, maximal 2.400 W
  q: hst
  hinweis: 2.400 W nur nach Anschluss durch einen Elektrofachbetrieb an einen eigenen Stromkreis oder über einen eigenen Leitungsschutzschalter und nach Freigabe in der App.
- k: On-grid max.
  v: 2.400 W Ein- und Ausgang, 230 V, 50 Hz
  q: hst
- k: Inselbetrieb
  v: Off-Grid-Steckdose, Dauer 2.400 W, Spitze 3.600 W für 10 s laut FAQ
  q: hst
- k: Umschaltung
  v: 15 ms laut FAQ, nachdem die Off-Grid-Funktion in der App aktiv ist
  q: hst
- gruppe: Allgemein
- k: Schutzart
  v: IP65, Schutzklasse I
  q: hst
  hinweis: IP65 entfällt, wenn die wasserdichte Abdeckung offen ist oder ein Stecker in der Off-Grid-Dose steckt.
- k: Betriebstemperatur
  v: −20 °C bis +60 °C
  q: hst
- k: Maße
  v: siehe Widerspruch; Nettogewicht 10,12 kg
  q: hst
- k: Gewicht AB3000X
  v: 26,1 kg, 477,5 × 320 × 194 mm
  q: hst
- k: Wirkungsgrad
  v: bis 93 % Round-Trip laut FAQ, interne Labortests
  q: hst
- k: Garantie
  v: keine Angabe in Jahren
  q: hst
staerken:
- t: AC-Nachrüstung ohne neuen Modulanschluss
  q: hst
- t: Off-Grid-Dose mit 2.400 W Dauer laut FAQ
  q: hst
- t: Koppler selbst 10,12 kg
  q: hst
schwaechen:
- t: Standardausgang nur 200 W
  q: hst
- t: Nur AB3000X, und der Shop bietet keine Variante ohne Akku
  q: hst
- t: Smart Meter nötig für die automatische Leistungsanpassung
  q: hst
widersprueche:
- t: '**Maße:** Die FAQ nennt 448 × 303,6 × 88 mm (L × B × H). Die Spezifikation nennt die Produktgröße 410 × 302 × 75 mm. Beide nennen 10,12 kg netto. Deshalb gibt es keine maßstäbliche Zeichnung.'
  q: hst
- t: '**Kapazität der Dreier-Variante:** Die Shop-Auswahl beschriftet 3× AB3000X mit 8,84 kWh. Dreimal 2,88 kWh sind 8,64 kWh. Die Spezifikation rechnet 2.880 Wh × 6 = 17.280 Wh.'
  q: hst
tests_hinweis: Unabhängige Tests (z. B. Stiftung Warentest, COMPUTER BILD, CHIP, heise) habe ich für dieses Modell bis zum 26.10.2026 nicht ausgewertet; hier stehen deshalb nur Herstellerangaben.
alternativen:
- slug: zendure-solarflow-2400-ac-plus
  warum: Ebenfalls AC-gekoppelt, mit 2,4 kWh im Gerät und 800 W Standardausgang.
- slug: zendure-solarflow-2400-pro
  warum: Gleiche Namensfamilie, aber mit eigenem PV-Eingang und eingebautem Akku.
---
