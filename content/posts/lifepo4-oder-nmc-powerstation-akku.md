+++
title = 'LiFePO4 oder NMC: Welcher Akku gehört in die Powerstation?'
foto = 'unterwegs'
lastmod = '2026-10-20T13:30:00+02:00'
date = '2026-10-19'
description = "LiFePO4 oder NMC? Was eine KIT-Studie zur Sicherheit zeigt, warum LFP-Powerstations schwerer sind, was Zyklen bedeuten, wie Anker die Garantie staffelt."
draft = false
kategorie = 'powerstations'
kurzgesagt = 'LiFePO4-Zellen (LFP) reagierten in einer KIT-Laborstudie später und schwächer auf Überhitzung und gingen beim Nageltest nie in den thermischen Durchgang – NMC- und NCA-Zellen schon. Dafür speichert eine LFP-Zelle weniger Energie, LFP-Geräte sind größer und schwerer. Bei Powerstations ist LFP heute Standard; die Zellchemie ersetzt aber keinen Gerätetest.'
fuer_dich = ['dir Sicherheit wichtiger ist als das letzte Kilo – dann passt LiFePO4.', 'du auf lange Garantie achtest: Anker gibt in der EU 5 Jahre auf Powerstations mit LiFePO4-Akku.', 'du Zyklenangaben vergleichst und dabei auf die gleiche Restkapazität achtest.']
eher_nicht = ['Gewicht für dich alles ist – dann kann NMC Vorteile haben; prüfe dann Garantie und Sicherheitstests besonders.', 'du im Winter unter 0 °C laden musst – die meisten Geräte erlauben das laut Datenblatt nicht.', 'du die Zellchemie als Ersatz für einen Gerätetest siehst – auch ein Gerät mit LFP-Akku kann durchfallen (ADAC 2025).']
weiter = { tool = 'finder', url = '/powerstation-finder/?einsatz=camping&kg=5', text = 'Leichte Powerstation unter 5 kg finden', artikel = '/posts/powerstation-camping-kaufberatung/' }
keywords = ['akku', 'lifepo4', 'nmc', 'sicherheit']
kurz = [
  '**Sicherheit:** In einer KIT-Studie gingen LFP-Zellen beim Nageltest nie in den thermischen Durchgang, NMC- und NCA-Zellen ab 30 % Ladung schon.',
  '**Energiedichte:** Die LFP-Zelle im selben 21700-Format speicherte dort 9,9 Wh, NMC und NCA 18 Wh. LFP-Geräte sind daher größer und schwerer.',
  '**Garantie:** Anker gibt in der EU 5 Jahre auf Powerstations mit LiFePO4-Akku, 1,5 Jahre auf ältere Modelle mit NMC-Akku.',
  'Alle Powerstations in meinem Vergleich nutzen LiFePO4.',
]
[[faq]]
  f = 'Ist LiFePO4 sicherer als NMC?'
  gruppe = 'Technik'
  a = 'In der KIT-Studie von 2023 an 21700-Zellen ja: LFP reagierte erst bei deutlich höheren Temperaturen und ging beim Nageltest bei keinem Ladezustand in den thermischen Durchgang. NMC- und NCA-Zellen taten das ab 30 % Ladung. Die Forscher nennen LFP „inhärent sicherer“.'
[[faq]]
  f = 'Warum sind LiFePO4-Powerstations schwerer?'
  gruppe = 'Technik'
  a = 'LFP speichert pro Zelle weniger Energie. Im KIT-Vergleich hatte die LFP-Zelle 9,9 Wh, die NMC- und NCA-Zellen im selben Format 18 Wh. Für dieselbe Kapazität braucht man also mehr Zellen.'
[[faq]]
  f = 'Was bedeuten 4.000 Zyklen bis 80 %?'
  gruppe = 'Kauf'
  a = 'Nach 4.000 vollen Lade- und Entladezyklen soll laut Hersteller noch 80 % der ursprünglichen Kapazität vorhanden sein. Jackery gibt für die Explorer 1000 v2 dagegen 4.000 Zyklen bis 70 % an. Die Werte sind nur vergleichbar, wenn die Restkapazität gleich ist.'
+++

Fast jede neue Powerstation wirbt mit „LiFePO4“. Ältere Geräte und viele Powerbanks nutzen dagegen NMC-Zellen. Was steckt hinter den Kürzeln, und spielt es für dich eine Rolle? Hier fasse ich zusammen, was eine Laborstudie des Karlsruher Instituts für Technologie (KIT) und die Herstellerangaben dazu sagen.

*Ich habe keine eigenen Messungen gemacht. Die Zahlen stammen aus den verlinkten Quellen.*

## Was die Kürzel bedeuten

Lithium-Ionen-Akkus unterscheiden sich vor allem im Material der Kathode:

- **LFP oder LiFePO4:** Lithium-Eisenphosphat
- **NMC:** Lithium-Nickel-Mangan-Kobalt-Oxid
- **NCA:** Lithium-Nickel-Kobalt-Aluminium-Oxid

{{% mehr "Zur Studie des KIT" %}}

Die KIT-Forscher haben 2023 handelsübliche Zellen im Format 21700 mit allen drei Kathoden verglichen. Das ist ein verbreitetes Rundzellen-Format, 21 mm dick und 70 mm lang. Die Zellen wurden gezielt überhitzt und mit einem Nagel durchstochen.

{{% /mehr %}}

## Sicherheit: LFP reagiert später und schwächer

Die Ergebnisse der Studie in Kürze:

- **Überhitzung:** NMC-Zellen reagierten zuerst, NCA-Zellen gingen etwas früher in den thermischen Durchgang („Thermal Runaway“). LFP-Zellen reagierten „langsamer und bei deutlich höheren Temperaturen“. Der Durchgang setzte bei vollgeladenen LFP-Zellen im Mittel bei rund 256 °C ein, bei NMC bei rund 198 °C.
- **Nageltest:** LFP-Zellen gingen bei keinem Ladezustand in den thermischen Durchgang und erreichten höchstens rund 130 °C. NMC- und NCA-Zellen taten das bei 30, 50 und 100 % Ladung.
- **Ladezustand:** Bei 0 % Ladung trat bei keiner Chemie ein thermischer Durchgang auf.

{{% mehr "Fazit der Autoren und Einordnung der Studie" %}}

Das Fazit der Autoren: LFP-Zellen sind „inhärent sicherer“ als NCA- und NMC-Zellen. Sie weisen aber auch darauf hin, dass das langsamere Reagieren das Erkennen eines Fehlers erschweren kann. Batteriemanagementsysteme müssten darauf ausgelegt sein.

Wichtig für die Einordnung: Die Studie untersuchte einzelne Zellen, keine fertigen Powerstations. Wie sicher ein Gerät ist, hängt auch von Gehäuse, Elektronik und Batteriemanagement ab. Dass ein Gerät mit LFP-Akku trotzdem durchfallen kann, zeigt der ADAC-Test 2025. Dort bekam die Jackery Explorer 1000 v2 wegen nicht entkoppelter DC-Eingänge die Note „mangelhaft“, mit Zellchemie hatte das nichts zu tun.

{{% /mehr %}}

## Der Preis: weniger Energie pro Zelle

Die Sicherheit hat laut KIT einen Preis. Im 21700-Format war die LFP-Zelle nur mit 3 Ah erhältlich, NMC und NCA mit 5 Ah. Weil LFP zudem eine niedrigere Nennspannung hat (3,3 V statt 3,6 V), ergibt das:

| Zelle (21700) | Kapazität | Nennspannung | Energie |
|---|---|---|---|
| NMC / NCA | 5 Ah | 3,6 V | 18 Wh |
| LFP | 3 Ah | 3,3 V | 9,9 Wh |

Für dieselbe Kapazität braucht ein LFP-Gerät also mehr Zellen und wird größer und schwerer. Bei den Powerstations in meinem Vergleich liegt die Energiedichte des ganzen Geräts, also Kapazität geteilt durch Gewicht laut Hersteller, zwischen rund 61 Wh/kg (EcoFlow RIVER 3 Plus) und rund 115 Wh/kg (BLUETTI Elite 300). Darin stecken neben den Zellen auch Gehäuse, Wechselrichter und Lüfter. Große Geräte schneiden deshalb meist besser ab.

{{< produkte art="ps" modelle="EcoFlow RIVER 3|Jackery Explorer 300 Plus|Anker SOLIX C2000 Gen 2" >}}

## Lebensdauer: Zyklenangaben richtig lesen

Die Hersteller der LFP-Powerstations in meinem Vergleich geben meist 3.000 bis 4.000 Ladezyklen an, für die BLUETTI Elite 300 nennt heise 6.000. Achte darauf, worauf sich die Zahl bezieht:

- EcoFlow RIVER 3: 3.000 Zyklen bis 80 % Restkapazität
- Anker SOLIX C1000 Gen 2: 4.000 Zyklen bis mindestens 80 %
- DJI Power 1000 Mini: 4.000 Zyklen, danach über 80 %, gemessen bei 25 °C und 400 W Entladung
- Jackery Explorer 1000 v2: 4.000 Zyklen bis **70 %**

{{% mehr "Restkapazität richtig vergleichen und Garantie als Indiz" %}}

Eine Angabe „bis 70 %“ ist nicht mit „bis 80 %“ vergleichbar. Unabhängige Langzeittests der Zyklenfestigkeit habe ich für keines der Geräte gefunden. Die Zahlen sind Herstellerangaben.

Ein indirektes Indiz liefert die Garantie. Anker staffelt sie in der EU ausdrücklich nach Zellchemie: **5 Jahre für Modelle mit LiFePO4, 1,5 Jahre für Modelle mit NMC-Akku.** Die NMC-Modelle in Ankers Liste sind ältere PowerHouse-Geräte.

{{% /mehr %}}

## Temperatur: Laden ab 0 °C

Die meisten Geräte in meinem Vergleich dürfen laut Datenblatt erst ab 0 °C geladen werden. Beispiele sind die EcoFlow RIVER 3, die Jackery-Modelle sowie die Anker C300X, C1000 Gen 2 und C2000 Gen 2. DJI gibt für die Power 1000 Mini −10 bis 45 °C für Betrieb und Laden an. Wer im Winter campt, sollte das Gerät vor dem Laden aufwärmen lassen.

## Was heißt das für den Kauf?

- **Für Powerstations ist LFP heute Standard.** Alle Modelle in meinem [Vergleich](/vergleich/#powerstations) nutzen LiFePO4. NMC begegnet dir vor allem bei älteren oder sehr leichten Geräten und Powerbanks.
- **Wenn Gewicht alles ist**, kann NMC Vorteile haben. Prüfe dann besonders die Garantie und unabhängige Sicherheitstests.
- **Zyklenangaben** nur bei gleicher Restkapazität vergleichen.
- **Die Zellchemie ersetzt keinen Gerätetest.** Auf den [Produktseiten](/powerstations/#modelle) stehen die Testergebnisse je Modell.

## Quellen

{{< quellen >}}
- Ohneseit, S. et al. (KIT): [Thermal and Mechanical Safety Assessment of Type 21700 Lithium-Ion Batteries with NMC, NCA and LFP Cathodes](https://www.mdpi.com/2313-0105/9/5/237), Batteries 2023, 9(5), 237, doi:10.3390/batteries9050237
- Anker SOLIX: [Portable Power Station Warranty Policy (EU)](https://www.ankersolix.com/eu/anker-portable-power-station-warranty-policy)
- ADAC: [Mobile Powerstations im Test 2025](https://www.adac.de/rund-ums-haus/energie/versorgung/mobile-powerstations-test/), 11.06.2025
- Herstellerangaben zu Zyklen, Temperaturen und Gewicht: [EcoFlow RIVER 3](https://de.ecoflow.com/products/river-3-portable-power-station), [Anker SOLIX C1000 Gen 2](https://www.ankersolix.com/de/products/c1000-gen2), [DJI Power 1000 Mini](https://www.dji.com/de/power-1000-mini/specs), [Jackery Explorer 1000 V2](https://helpcenter.eu.jackery.com/hc/de/articles/52683026571291-Explorer-1000-V2-Grundlegende-Informationen) sowie die übrigen auf den [Produktseiten](/powerstations/#modelle)
{{< /quellen >}}
