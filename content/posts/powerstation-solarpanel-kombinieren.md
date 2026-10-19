+++
title = 'Powerstation mit Solarpanel kombinieren: Spannung, Stecker, Leistung'
date = '2026-10-19'
description = 'Welches Solarpanel passt an welche Powerstation? Spannungsbereich, Strom, maximale Leistung, Stecker (XT60, DC8020, SDC, USB-C), Reihen- oder Parallelschaltung und warum die Leerlaufspannung im Winter steigt.'
draft = true
kategorie = 'powerstations'
keywords = ['solar', 'solarpanel', 'mppt', 'xt60']
kurz = [
  'Drei Werte müssen passen: **Spannungsbereich (V)**, **maximaler Strom (A)** und **maximale Solarleistung (W)** des Eingangs.',
  'Die **Leerlaufspannung** eines Panels ist bei Kälte am höchsten (SMA). Sie muss auch im Winter unter der Höchstspannung des Eingangs bleiben.',
  'Stecker unterscheiden sich: XT60, DC8020, DJI-SDC, USB-C. Oft brauchst du ein Adapterkabel vom Hersteller.',
  'Geräte mit nicht entkoppelten DC-Eingängen nicht gleichzeitig über Solar und Auto laden (ADAC).',
]
[[faq]]
  f = 'Welches Solarpanel passt zu meiner Powerstation?'
  a = 'Eines, dessen Spannung im Eingangsbereich der Powerstation liegt, dessen Strom den Grenzwert nicht überschreitet und dessen Stecker passt. Die maximale Solarleistung bestimmt, wie viel die Station höchstens aufnimmt. Die Werte für die zehn Modelle aus unserem Vergleich stehen in der Tabelle im Artikel.'
[[faq]]
  f = 'Reihe oder parallel – wie schließe ich zwei Panels an?'
  a = 'In Reihe addieren sich die Spannungen, parallel die Ströme. Bei Reihenschaltung muss die summierte Leerlaufspannung auch bei Kälte unter der Höchstspannung des Eingangs bleiben. Manche Geräte schreiben eine Schaltung vor: Bei der Jackery Explorer 1000 v2 sind die beiden Eingänge parallel geschaltet, und Jackery verlangt gleiche Panels.'
[[faq]]
  f = 'Warum ist die Leerlaufspannung im Winter wichtig?'
  a = 'Laut SMA-Planungsleitfaden ist die Leerlaufspannung bei niedrigen Temperaturen am höchsten. Wer nahe an der Höchstspannung des Eingangs plant, kann sie an einem kalten, sonnigen Tag überschreiten.'
+++

Ein Solarpanel macht eine Powerstation unabhängig von der Steckdose. Damit das funktioniert, muss das Panel elektrisch und mechanisch zum Solareingang passen. Hier sind die drei wichtigsten Werte, die Steckerfrage und die Daten der zehn Modelle aus unserem Vergleich.

*Alle Gerätewerte sind Herstellerangaben, verlinkt auf den [Produktseiten](/powerstations/#modelle). Wir haben keine eigenen Ladetests gemacht.*

## Die drei Werte, die passen müssen

1. **Spannungsbereich (V):** Der Eingang arbeitet nur in einem bestimmten Spannungsfenster, zum Beispiel 11–60 V. Liegt das Panel darunter, lädt nichts. Liegt es darüber, kann der Eingang Schaden nehmen.
2. **Maximaler Strom (A):** Mehr Strom nimmt der Eingang nicht auf. Er begrenzt die Leistung, vor allem bei Panels mit niedriger Spannung.
3. **Maximale Solarleistung (W):** Mehr Leistung verarbeitet die Station nicht, auch wenn das Panel mehr liefern könnte.

Auf dem Typenschild eines Panels stehen meist die **Leerlaufspannung (Voc)** und die **Spannung im Leistungsmaximum (Vmp)**. Für die Obergrenze des Eingangs zählt die Leerlaufspannung. Das ist die Spannung ohne Last, und sie ist höher als die Arbeitsspannung.

## Achtung Kälte: Die Spannung steigt

Der Wechselrichterhersteller SMA schreibt in seinem Planungsleitfaden: „Die Leerlaufspannung ist bei niedrigen Temperaturen am höchsten.“ Wie stark sie steigt, ergibt sich aus dem Temperaturkoeffizienten im Datenblatt des Panels und der niedrigsten zu erwartenden Temperatur am Aufstellort. Für Powerstations heißt das: Plane die Leerlaufspannung nicht knapp unter der Höchstspannung des Eingangs, besonders wenn du zwei Panels in Reihe schaltest.

## Reihe oder parallel?

- **Reihenschaltung:** Die Spannungen addieren sich, der Strom bleibt gleich. Das ist sinnvoll bei Eingängen mit hoher Höchstspannung, zum Beispiel 60 V. Die Leerlaufspannung muss dabei auch bei Kälte im erlaubten Bereich bleiben.
- **Parallelschaltung:** Die Ströme addieren sich, die Spannung bleibt gleich. Das ist sinnvoll bei Eingängen mit niedriger Höchstspannung. Hier begrenzt der maximale Eingangsstrom.

Manche Hersteller schreiben Regeln vor. Bei der **Jackery Explorer 1000 v2** sind die beiden Solareingänge laut Jackery parallel geschaltet. Unterschiedlich starke Panels dürfen nicht gleichzeitig angeschlossen werden, also nicht 100 W an einem und 200 W am anderen Eingang. Bei Mischbetrieb müssen Nennleistung, Leerlauf- und Betriebsspannung identisch sein. Die **Jackery Explorer 300 Plus** erlaubt laut Jackery nur ein einziges Panel.

## Die Solareingänge der zehn Modelle

| Modell | Spannung | Strom | Solar max. | Anschluss |
|---|---|---|---|---|
| [EcoFlow RIVER 3](/powerstations/ecoflow-river-3/) | 11–30 V | 8 A | 110 W | – |
| [EcoFlow RIVER 3 Plus](/powerstations/ecoflow-river-3-plus/) | 11–55 V | 13 A | 220 W | – |
| [Jackery Explorer 300 Plus](/powerstations/jackery-explorer-300-plus/) | 12–27 V | 5 A | 100 W | USB-C, Adapter 8020 → USB-C nötig |
| [Anker SOLIX C300X](/powerstations/anker-solix-c300x/) | 11–28 V | 8,2 A | 100 W | XT-60 |
| [DJI Power 1000 Mini](/powerstations/dji-power-1000-mini/) | 9–28 V | – | 400 W | SDC, DJI-MC4-Kabel |
| [Anker SOLIX C1000 Gen 2](/powerstations/anker-solix-c1000-gen-2/) | bis 60 V | – | 600 W | XT-60 |
| [EcoFlow DELTA 3 Plus](/powerstations/ecoflow-delta-3-plus/) | 11–60 V | – | 2 × 500 W | 2 Eingänge |
| [BLUETTI Elite 100 V2](/powerstations/bluetti-elite-100-v2/) | 12–60 V | 20 A | 1.000 W | XT60, MC4-Kabel |
| [Jackery Explorer 1000 v2](/powerstations/jackery-explorer-1000-v2/) | 16–60 V | 10,5 A je Port / 21 A gesamt | 200 W je Port / 400 W gesamt | 2 × DC8020, parallel |
| [Anker SOLIX C2000 Gen 2](/powerstations/anker-solix-c2000-gen-2/) | 11–28 V / 28–60 V | 8,2 A / 17 A | 800 W | XT-60i |

„–“ heißt: Den Wert haben wir in den Herstellerquellen nicht gefunden. Ein Beispiel für die Stromgrenze: Bei der Anker C2000 Gen 2 sind laut Anleitung unter 28 V höchstens 8,2 A erlaubt, das sind bei 28 V rund 230 W. Die vollen 800 W gibt es also nur im oberen Spannungsbereich.

## Stecker und Adapter

- **XT60 / XT-60i:** Anker C300X, C1000 Gen 2, C2000 Gen 2. Bei der BLUETTI Elite 100 V2 führt ein MC4-auf-XT60-Kabel vom Panel zur Station.
- **DC8020:** Jackery. Die Explorer 300 Plus lädt Solar aber nur über USB-C und braucht dafür einen Adapter.
- **SDC:** DJI-eigener Anschluss. Für Solar gibt es laut DJI ein MC4-Kabel.
- **MC4:** der übliche Stecker an größeren Solarmodulen. Fast immer brauchst du ein Adapterkabel auf den Eingang der Powerstation.

Ob ein Solarkabel im Karton liegt, ist unterschiedlich. Beim ADAC-Test fehlte der EcoFlow DELTA 3 Plus das PV-Ladekabel, bei der Anker C300X sind Solar- und Kfz-Kabel laut Anker separat erhältlich. Bei der BLUETTI Elite 100 V2 widersprechen sich Herstellerseite und ein Praxistest. Einzelheiten stehen auf den Produktseiten.

{{< produkte art="ps" modelle="BLUETTI Elite 100 V2|EcoFlow DELTA 3 Plus|Anker SOLIX C2000 Gen 2" >}}

## Sicherheit: nicht gleichzeitig über Solar und Auto laden

Der ADAC hat 2025 die Jackery Explorer 1000 v2 und die Ective BlackBox 10 mit „mangelhaft“ bewertet. Bei beiden sind die DC-Eingänge nicht voneinander entkoppelt. Wer gleichzeitig über Solarmodul und Auto lädt, riskiert laut ADAC Schäden am 12-V-Bordnetz. Jackery bezeichnet gleichzeitiges Laden über Solar und Auto im Helpcenter inzwischen als „nicht zulässig“. Das gilt auch für gleichzeitiges Laden über zwei Autokabel.

## Wie schnell lädt Solar wirklich?

Die Ladezeiten der Hersteller gelten für ideale Bedingungen. COMPUTER BILD maß an der EcoFlow DELTA 3 Plus bei Solarladung bis zu 983 W und 92 Minuten bis voll; EcoFlow nennt rund 70 Minuten. Wetter, Panelwinkel und Temperatur senken die Leistung, und wie viel im Alltag ankommt, hängt stark vom Standort ab.

Wie viel Energie du am Tag nachladen musst, zeigt der [Laufzeitrechner](/laufzeitrechner/). Der [Powerstation-Finder](/powerstation-finder/) sortiert beim Einsatz „Van“ nach der größten Solarleistung.

## Checkliste

1. Leerlaufspannung des Panels oder der Reihe liegt auch bei Kälte unter der Höchstspannung des Eingangs.
2. Die Arbeitsspannung liegt über der Mindestspannung des Eingangs.
3. Der Strom übersteigt nicht die Grenze des Eingangs. Bei Parallelschaltung addieren sich die Ströme.
4. Ein passender Stecker oder ein Adapterkabel vom Hersteller ist vorhanden.
5. Die Regeln des Herstellers zu mehreren Panels sind beachtet, etwa gleiche Panels bei Jackery.
6. Nicht gleichzeitig über Solar und Auto laden, wenn der Hersteller das ausschließt.

## Quellen

{{< quellen >}}
- SMA: [Planungsleitfaden – Dimensionierung von PV-Anlagen](https://files.sma.de/downloads/DC-PL-de-11.pdf), Kap. 3.2.1.1 (Leerlaufspannung bei niedrigen Temperaturen)
- ADAC: [Mobile Powerstations im Test 2025](https://www.adac.de/rund-ums-haus/energie/versorgung/mobile-powerstations-test/), 11.06.2025
- Jackery Helpcenter: [Explorer 1000 V2](https://helpcenter.eu.jackery.com/hc/de/articles/52683026571291-Explorer-1000-V2-Grundlegende-Informationen), [Explorer 300 Plus](https://helpcenter.eu.jackery.com/hc/en-gb/articles/52682971950363-Explorer-300-Plus-Basic-Information)
- Anker: [SOLIX C2000 Gen 2 – Bedienungsanleitung](https://cdn-reichelt.de/documents/datenblatt/D400/ANKER_S_C2000_2_ANL-DE.pdf), [C300X-Datenblatt](https://www.e-tec.at/xstorage/1/Produktdatenbl%C3%A4tter/A1723-datasheet_EU.pdf), [C300X-Produktseite](https://www.ankersolix.com/de/products/anker-solix-c300x)
- DJI: [Power 1000 Mini – FAQ](https://www.dji.com/de/power-1000-mini/faq); BLUETTI: [Elite 100 V2 – Handbuch](https://s4.bluettipower.com/bluetti/purchasePageBiz/2026/06/Elite_100_V2_User_Manual_EU_EN-DE-1780889806412-6beb.pdf)
- COMPUTER BILD: [EcoFlow Delta 3 Plus im Test](https://www.computerbild.de/artikel/cb-Tests-Energie-EcoFlow-Delta-3-Plus-Test-powerstation-39441187.html), 15.02.2025
- Übrige Eingangsdaten: Herstellerangaben auf den [Produktseiten](/powerstations/#modelle)
{{< /quellen >}}
