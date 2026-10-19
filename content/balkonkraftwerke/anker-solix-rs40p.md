---
title: Anker SOLIX RS40P (2 × 445 W, MI80)
modell: Anker SOLIX RS40P Balkonkraftwerk (2 × 445 W, MI80)
layout: bkw-produkt
date: '2026-10-19'
lastmod: '2026-10-19'
description: 'Anker SOLIX RS40P Balkonkraftwerk mit 2 × 445 W und MI80-Wechselrichter: Daten mit Quellen, Widersprüche zwischen Anker-Seiten, Tests von COMPUTER BILD und heise.'
kurzzeile: 'Set ohne Speicher: 890 Wp, 800-W-Wechselrichter MI80'
kurzfazit: 'Das RS40P ist ein klassisches Balkonkraftwerk ohne Speicher: zwei 445-W-Module und der Mikrowechselrichter MI80, der laut Datenblatt 800 W einspeisen kann. Mit 890 Wp bleibt es deutlich unter der 2.000-Wp-Grenze für Steckersolargeräte. Die langen Garantien (15 Jahre Module, 10 Jahre Wechselrichter) sind ein Plus. Die Tests von COMPUTER BILD (1,8 „gut“) und heise stammen aus 2023/2024 und betreffen die ältere Ausführung mit dem MI60. Außerdem widersprechen sich Ankers eigene Seiten bei Modultechnik, Maßen und Leistungsgarantie. Prüfe also vor dem Kauf, welche Modulversion geliefert wird.'
fuer:
- Mieter und Eigentümer, die tagsüber Grundlast decken wollen (Kühlschrank, Router, Homeoffice) und keinen Speicher brauchen
- Wer ein Komplettset mit passender Balkonhalterung möchte statt einzeln gekaufter Teile
- 'Wer auf lange Garantie Wert legt: 15 Jahre auf die Module'
nicht_fuer:
- 'Wer abends und nachts Solarstrom nutzen will: kein Speicher'
- 'Notstrom bei Stromausfall: Der Wechselrichter schaltet bei Netzausfall ab, eine Inselsteckdose gibt es nicht'
- 'Wer mehr als zwei Module anschließen will: Der MI80 hat zwei Eingänge'
quellen:
- id: db
  titel: 'Anker: Datenblatt SOLIX RS40P DIY Balkonkraftwerk (Modul A5507, MI80 A5143), bei OBI hinterlegt'
  url: https://bilder.obi.at/8f11a88f-d87c-4cdc-969c-6c325e889963/serve.php
  art: Hersteller-Datenblatt
- id: mod
  titel: 'Anker SOLIX DE: RS40P Solarpanel (445 W) – Produktseite'
  url: https://www.ankersolix.com/de/products/b5555416?variant=58249281044829
  art: Hersteller
- id: gar
  titel: 'Anker SOLIX DE: Herstellergarantie Balkonkraftwerk'
  url: https://www.ankersolix.com/de/balkonkraftwerk_herstellergarantie
  art: Hersteller
- id: sup
  titel: 'Anker SOLIX Support: RS40P Solar Panel (445W) – Spezifikation'
  url: https://support.ankersolix.com/s/product/a08J1000000Y2vaIAC/anker-solix-rs40p-solar-panel-445w
  art: Hersteller
- id: eu
  titel: 'Anker SOLIX EU: Produktseite b5143 (zeigt inzwischen ein 820-W-Set)'
  url: https://www.ankersolix.com/eu/products/b5143
  art: Hersteller
- id: cb
  titel: 'COMPUTER BILD: Anker Solix RS40P – Balkonkraftwerk im Test (13.08.2023)'
  url: https://www.computerbild.de/artikel/cb-Tests-Energie-Anker-Solix-Balkonkraftwerk-Test-36270327.html
  art: Test
- id: heise
  titel: 'heise bestenlisten: Balkonkraftwerk Anker Solix im Test (14.02.2024)'
  url: https://www.heise.de/bestenlisten/testbericht/balkonkraftwerk-anker-solix-im-test/feet97v
  art: Test
- id: cbase
  titel: 'ComputerBase: Anker Solix RS40P im Test (2023)'
  url: https://www.computerbase.de/artikel/smart-home/balkonkraftwerk-anker-solix-rs40p-test.83750/
  art: Test
- id: swt25
  titel: 'Stiftung Warentest: Balkonkraftwerk-Test (22.05.2025)'
  url: https://www.test.de/balkonkraftwerk-test-5501703-0/
  art: Test, Einzelnoten kostenpflichtig
daten:
- gruppe: Module
- k: Module im Set
  v: 2 × 445 W = 890 Wp
  q: db
- k: Modultechnik / Wirkungsgrad
  v: monokristallin, 25 % (Datenblatt)
  q:
  - db
  - mod
  hinweis: Die Anker-Shopseite nennt TOPCon mit 22,27 % – siehe Widersprüche.
- k: Leerlaufspannung Voc
  v: 40 V
  q:
  - db
  - sup
  hinweis: 'Support-Seite: 40,09 V.'
- k: Kurzschlussstrom Isc
  v: 13,8 A
  q:
  - db
  - sup
  hinweis: 'Support-Seite: 13,69 A.'
- k: Maße / Gewicht je Modul
  v: 1706 × 1134 × 35 mm, 22 kg
  q:
  - db
  - mod
  hinweis: 'Shopseite: 1762 × 1134 × 30 mm, 21,5 kg.'
- k: Stecker
  v: MC4-kompatibel
  q: db
- k: Belastbarkeit
  v: vorn 5400 Pa, hinten 2400 Pa
  q: db
- gruppe: Wechselrichter MI80
- k: AC-Ausgang
  v: max. 800 W
  q: db
  hinweis: 'Datenblatt: „800W-Mikro-Wechselrichter, begrenzt auf 600W“ – Freischaltung auf 800 W per Update.'
- k: Eingänge / MPPT
  v: 2 Eingänge, je max. 20 A; MPPT-Bereich 28–45 V
  q: db
- k: Max. empfohlene PV-Leistung
  v: 2 × 700 Wp
  q: db
- k: Max. DC-Leerlaufspannung
  v: 60 V
  q: db
- k: CEC-Wirkungsgrad
  v: 97,3 %
  q: db
- k: Verbrauch nachts
  v: 0,02 W
  q: db
- k: Zertifizierung
  v: VDE-AR-N 4105:2018, DIN VDE V 0124-100:2020
  q: db
- gruppe: Speicher und Notstrom
- k: Speicher
  v: keiner
  q: db
- k: Notstrom-/Inselsteckdose
  v: keine
  q: db
- gruppe: Garantie
- k: Produktgarantie
  v: Module 180 Monate (15 Jahre), MI80 120 Monate (10 Jahre)
  q: gar
  hinweis: Laut Anker nur bei Kauf im offiziellen Shop; sonst über den Händler klären.
- k: Leistungsgarantie Module
  v: 15 Jahre ≥ 93,4 %, 30 Jahre ≥ 88,8 %
  q:
  - gar
  - mod
  hinweis: 'Shopseite: „30 Jahre bei mindestens 87,4 %“.'
widersprueche:
- t: '**Modultechnik und Maße:** Das Datenblatt nennt 25 % Wirkungsgrad, 1706 × 1134 × 35 mm und 22 kg, die aktuelle Shopseite TOPCon mit 22,27 %, 1762 × 1134 × 30 mm und 21,5 kg. Vermutlich gibt es zwei Modulversionen unter demselben Namen. Für die Montage zählt das Maß des gelieferten Moduls.'
  q:
  - db
  - mod
- t: '**Leistungsgarantie:** Garantieseite 88,8 % nach 30 Jahren, Shopseite 87,4 %.'
  q:
  - gar
  - mod
- t: '**Elektrische Werte:** Vmp 34,56 V im Datenblatt, 33,91 V auf der Support-Seite.'
  q:
  - db
  - sup
- t: '**Produktseite:** Die bisher verlinkte Anker-EU-Seite zum RS40P zeigt inzwischen ein 820-W-Set mit 410-W-Modulen und eine veraltete FAQ zur 600-W-Grenze. heise schrieb im August 2025, Anker biete im eigenen Shop keine Sets ohne Speicher mehr an.'
  q:
  - eu
  - heise
staerken:
- t: 'Lange Garantie: 15 Jahre auf die Module, 10 Jahre auf den Wechselrichter'
  q: gar
- t: Komplettset mit passender Halterung, laut heise auch für Laien montierbar
  q: heise
- t: MI80 mit 800 W, zwei Eingängen bis 700 Wp und VDE-AR-N-4105-Nachweis
  q: db
- t: COMPUTER BILD maß 2023 bis zu 435 W je Modul (damalige 440-W-Version), bei diffuser Verschattung noch 205 W
  q: cb
schwaechen:
- t: Kein Speicher und keine Notstromsteckdose
  q: db
- t: 'heise: verhältnismäßig teuer, kein Werkzeug zum Lösen der MC4-Stecker beigelegt'
  q: heise
- t: Widersprüchliche Herstellerangaben zu Modultechnik, Maßen und Leistungsgarantie
  q:
  - db
  - mod
  - gar
- t: Die vorhandenen Tests betreffen die ältere MI60-Ausführung
  q:
  - cb
  - heise
  - cbase
tests:
- name: COMPUTER BILD
  datum: 13.08.2023
  url: https://www.computerbild.de/artikel/cb-Tests-Energie-Anker-Solix-Balkonkraftwerk-Test-36270327.html
  urteil: Testnote 1,8 – gut (Ausführung 2023)
  text: Getestet wurde die frühere Version mit 440-W-Modulen und MI60. Das Modul war das leistungsstärkste im Test (bis 435 W); Abzug gab es für den MI60, der nicht über 595 W Einspeisung kam. Im Fazit schreibt COMPUTER BILD, dass Anker das Set inzwischen mit 445-W-Modulen und MI80 verkauft.
- name: heise bestenlisten
  datum: 14.02.2024
  url: https://www.heise.de/bestenlisten/testbericht/balkonkraftwerk-anker-solix-im-test/feet97v
  urteil: Bewertung 4,5 von 5 (laut Seitendaten)
  text: 'Plus: Komplettset mit Halterung und Wechselrichter, lange Garantie, hohe Leistung, einfache Installation. Minus: verhältnismäßig teuer, kein Werkzeug für die MC4-Stecker. Getestet mit dem MI60.'
- name: ComputerBase
  datum: '2023'
  url: https://www.computerbase.de/artikel/smart-home/balkonkraftwerk-anker-solix-rs40p-test.83750/
  text: 'Vergleich mit einem selbst zusammengestellten Set. Fazit: teurer, aber ohne Vorwissen nutzbar; Smart-Home-Anbindung fehlte. Laut Update vom 19.07.2023 tauschte Anker den MI60 bei allen Kunden aus, weil ein Bauteil nicht den deutschen Sicherheitsvorgaben entsprach.'
- name: Stiftung Warentest
  datum: 22.05.2025
  url: https://www.test.de/balkonkraftwerk-test-5501703-0/
  urteil: anderes Set getestet
  text: Im Balkonkraftwerk-Test war ein Anker-Set mit 870-Wp-Bifazialmodul und demselben MI80. Die Module unterscheiden sich vom RS40P; die Note (kostenpflichtig) lässt sich nicht übertragen.
tests_hinweis: Einen Test genau dieser Kombination aus 445-W-Modulen und MI80 habe ich nicht gefunden.
alternativen:
- slug: anker-solix-solarbank-2-e1600-pro
  warum: 'Wer Solarstrom auch abends nutzen will: Speicher mit Wechselrichter und Notstromsteckdose, Module separat.'
- slug: growatt-nexa-2000
  warum: Speicher mit eingebautem 800-W-Wechselrichter und 4 MPPT, ebenfalls ohne Module im Lieferumfang.
---
