+++
title = 'Kann eine Powerstation einen Heizlüfter betreiben?'
foto = 'stromausfall'
seotitle = 'Heizlüfter an der Powerstation: Wie lange reicht der Akku?'
date = '2026-10-28'
description = "Heizlüfter oder Heizdecke an der Powerstation: welche Dauerleistung nötig ist, wie lange 1, 2 oder 3 kWh reichen und was X-Boost und Power Lifting bringen."
draft = false
kategorie = 'powerstations'
kurzgesagt = 'Ja, aber nur kurz. Ein Heizlüfter mit 2.000 W braucht eine Station mit mindestens 2.000 W Dauerleistung. Eine Powerstation mit rund 1 kWh ist damit rechnerisch nach etwa 25 Minuten leer, eine mit 2 kWh nach knapp einer Stunde. Eine Heizdecke mit 60 bis 150 W hält an derselben 1-kWh-Station dagegen rund 5 bis 12 Stunden durch.'
fuer_dich = ['du bei einem Stromausfall im Winter ein paar Stunden überbrücken willst.', 'du beim Camping oder im Gartenhaus kurz heizen möchtest.', 'du wissen willst, ob deine Station genug Watt für einen Heizlüfter hat.']
eher_nicht = ['du einen Raum über Stunden mit Strom heizen willst – dafür reicht kein Akku in dieser Größe.', 'du eine Heizung ersetzen willst – die Verbraucherzentrale nennt Heizlüfter nur eine teure Notlösung.', 'deine Station weniger als 2.000 W Dauerleistung hat und du den Heizlüfter mit voller Leistung brauchst.']
weiter = { tool = 'laufzeitrechner', url = '/laufzeitrechner/?m=anker-solix-c2000-gen-2&g=Heizl%C3%BCfter~2000~0.5,Heizdecke~100~4', text = 'Heizlüfter und Heizdecke an der Anker C2000 Gen 2 durchrechnen', artikel = '/posts/powerstation-notstrom-blackout/' }
keywords = ['heizlüfter', 'heizdecke', 'heizen', 'stromausfall', 'winter', 'x-boost', 'power lifting', 'laufzeit']
kurz = [
  '**Leistung:** Geräte, die Wärme erzeugen, brauchen laut BBK schnell 1.500 bis 2.000 W. Die Dauerleistung der Station muss darüber liegen.',
  '**Laufzeit bei 2.000 W:** rund 26 Minuten an 1 kWh, 52 Minuten an 2 kWh, 1 Stunde 16 Minuten an 3 kWh (eigene Rechnung, 85 % nutzbar).',
  '**Heizdecke statt Heizlüfter:** 60 bis 150 W laut TÜV-Verband. Das ist rund ein Zwanzigstel eines Heizlüfters.',
  '**Boost-Modi** wie X-Boost (EcoFlow) oder Power Lifting (BLUETTI) betreiben Heizgeräte über der Nennleistung, aber mit abgesenkter Spannung und damit weniger Heizleistung.',
]
[[faq]]
  f = 'Wie lange läuft ein Heizlüfter an einer Powerstation?'
  gruppe = 'Laufzeit'
  a = 'Bei 2.000 W rechnerisch rund 26 Minuten an einer Station mit 1.024 Wh, rund 52 Minuten an 2.048 Wh und rund 1 Stunde 16 Minuten an 3.014 Wh. Angenommen sind 85 % nutzbare Kapazität und 15 W Eigenverbrauch. Schaltet das Thermostat den Heizlüfter zwischendurch ab, hält der Akku entsprechend länger.'
[[faq]]
  f = 'Welche Powerstation schafft einen 2.000-W-Heizlüfter?'
  gruppe = 'Technik'
  a = 'Eine mit mindestens 2.000 W Dauerleistung. In meinem Vergleich sind das unter anderem Anker SOLIX C1000 Gen 2 (2.000 W), Anker SOLIX C2000 Gen 2 und BLUETTI Elite 300 (je 2.400 W) sowie EcoFlow DELTA 3 Max Plus und DJI Power 2000 (je 3.000 W), alles Herstellerangaben.'
[[faq]]
  f = 'Funktioniert ein Heizlüfter mit X-Boost oder Power Lifting?'
  gruppe = 'Technik'
  a = 'Ja, aber mit weniger Leistung. EcoFlow nennt für die DELTA 3 Plus mit X-Boost bis 2.400 W bei 230 V, die Nennleistung bleibt 1.800 W. BLUETTI schreibt für die Elite 100 V2, dass Power Lifting reine Widerstandslasten bis 2.700 W versorgt, die tatsächliche Ausgangsleistung aber 1.800 W bleibt. Der Heizlüfter heizt dann schwächer.'
[[faq]]
  f = 'Ist eine Heizdecke an der Powerstation sinnvoller?'
  gruppe = 'Laufzeit'
  a = 'Für eine Person meist ja. Eine Heizdecke hat laut TÜV-Verband 60 bis 150 W. Mit 100 W hält eine 1-kWh-Station rechnerisch rund 7,5 Stunden, eine 2-kWh-Station rund 15 Stunden. Sie wärmt aber nur dich, nicht den Raum.'
+++

Fällt im Winter der Strom aus, fällt meist auch die Heizung aus. Die naheliegende Idee: den Heizlüfter an die Powerstation hängen. Das geht, wenn die Station genug Leistung hat. Die Frage ist nur, wie lange. Hier steht die Rechnung mit Herstellerdaten, dazu die Alternative, die deutlich länger durchhält.

*Ich habe keine eigenen Messungen gemacht. Die Rechnung nutzt die Annahmen meines Laufzeitrechners, die Leistungsdaten stammen von den Herstellern. Stand: 28.10.2026.*

## Erste Hürde: die Dauerleistung

Ein Heizlüfter wandelt Strom direkt in Wärme um. Laut Verbraucherzentrale braucht jede elektrische Direktheizung für eine Kilowattstunde Wärme eine Kilowattstunde Strom. Das BBK schreibt, dass Geräte, die Wärme erzeugen, „schnell 1500 Watt bis 2000 Watt“ brauchen. Welche Leistung dein Gerät hat, steht auf dem Typenschild.

Die Powerstation muss diese Leistung dauerhaft liefern, nicht nur als Spitze. Für einen Heizlüfter mit 2.000 W kommen in meinem Vergleich nur diese Modelle infrage (Dauerleistung laut Hersteller):

| Modell | Kapazität | Dauerleistung |
|---|---:|---:|
| [Anker SOLIX C1000 Gen 2](/powerstations/anker-solix-c1000-gen-2/) | 1.024 Wh | 2.000 W |
| [Anker SOLIX C2000 Gen 2](/powerstations/anker-solix-c2000-gen-2/) | 2.048 Wh | 2.400 W |
| [EcoFlow DELTA 3 Max Plus](/powerstations/ecoflow-delta-3-max-plus/) | 2.048 Wh | 3.000 W |
| [DJI Power 2000](/powerstations/dji-power-2000/) | 2.048 Wh | 3.000 W |
| [BLUETTI Elite 300](/powerstations/bluetti-elite-300/) | 3.014 Wh | 2.400 W |
| [EcoFlow DELTA Pro 3](/powerstations/ecoflow-delta-pro-3/) | 4.096 Wh | 4.000 W |

Bei der Anker C1000 Gen 2 liegt ein 2.000-W-Heizlüfter genau an der Grenze. Kleinere Stationen wie die DJI Power 1000 Mini mit 800 W schaffen ihn gar nicht. Alle Modelle mit Filter nach Leistung findest du in der [Powerstation-Suche](/powerstation-suche/).

{{% mehr "Was bringen X-Boost und Power Lifting?" %}}

Einige Hersteller bieten Modi für Heizgeräte über der Nennleistung an. Sie senken dafür die Ausgangsspannung. Das Gerät läuft, nimmt aber weniger Leistung auf und heizt entsprechend schwächer.

- **EcoFlow X-Boost (DELTA 3 Plus):** laut Handbuch bis 2.400 W bei 230 V, Nennleistung 1.800 W. EcoFlow nennt als geeignete Geräte zum Beispiel Heizdecken. Nicht verfügbar, solange die Station am Netz lädt oder im Bypass-Modus ist. Für Geräte mit Spannungsschutz ist X-Boost laut EcoFlow nicht geeignet.
- **BLUETTI Power Lifting (Elite 100 V2):** laut Handbuch für reine Widerstandslasten von 1.800 bis 2.700 W, etwa Wasserkocher, Heizdecken und Haartrockner. Die tatsächliche Ausgangsleistung bleibt 1.800 W.

Für einen Heizlüfter heißt das: Er läuft an einer 1.800-W-Station, liefert aber nicht seine volle Wärme. Prüfe vorher, ob dein Gerät das mitmacht.

{{% /mehr %}}

## Zweite Hürde: die Laufzeit

Die Rechnung ist dieselbe wie im [Laufzeitrechner](/laufzeitrechner/): nutzbare Wattstunden geteilt durch die Leistung. Ich nehme wie dort 85 % der Nennkapazität als nutzbar an und rechne 15 W Eigenverbrauch der Station dazu.

| Gerät | ~1 kWh (870 Wh nutzbar) | ~2 kWh (1.741 Wh nutzbar) | ~3 kWh (2.562 Wh nutzbar) |
|---|---:|---:|---:|
| Heizlüfter 2.000 W | rund 26 min | rund 52 min | rund 1 h 16 min |
| Heizlüfter auf 1.000 W | rund 51 min | rund 1 h 43 min | rund 2 h 31 min |
| Heizdecke 150 W | rund 5,3 h | rund 10,6 h | rund 15,5 h |
| Heizdecke 100 W | rund 7,6 h | rund 15,1 h | rund 22,3 h |
| Heizdecke 60 W | rund 11,6 h | rund 23,2 h | rund 34,2 h |

*Eigene Rechnung, keine Messung. Kapazitäten: 1.024 Wh, 2.048 Wh und 3.014 Wh laut Hersteller.*

Die 1.000-W-Zeile gilt nur, wenn dein Heizlüfter eine solche Stufe hat. Hat er ein Thermostat, das zwischendurch abschaltet, läuft er insgesamt länger. Die Dauerleistung muss trotzdem für die volle Stufe reichen.

**Die Folgerung:** Selbst eine 2-kWh-Station versorgt einen Heizlüfter keine Stunde lang. Für den Router, das Licht und den Kühlschrank bleibt dann nichts mehr übrig. Was eine Station sonst im Stromausfall leistet, steht im Artikel [Powerstation als Notstrom](/posts/powerstation-notstrom-blackout/).

## Die bessere Wahl: Heizdecke

Eine Heizdecke oder ein Wärmeunterbett hat laut TÜV-Verband im Durchschnitt 60 bis 150 W. Das ist ein Bruchteil eines Heizlüfters. Mit 100 W hält eine 1-kWh-Station rechnerisch einen ganzen Abend und die Nacht. Sie wärmt allerdings nur die Person darunter, nicht den Raum.

Das passt zu dem, was BBK und Verbraucherzentrale raten. Das BBK empfiehlt bei ausgefallener Heizung warme Kleidung und Decken, einen einzigen Aufenthaltsraum mit geschlossenen Türen und trotzdem regelmäßiges Lüften. Die Verbraucherzentrale rät, elektrische Direktheizungen nur punktuell einzusetzen und gezielt auf die Personen im Raum zu richten.

{{% mehr "Sicherheit und Praxis bei Heizdecken" %}}

- **Nicht unbeaufsichtigt:** Der TÜV-Verband rät, Heizdecken nie unbeaufsichtigt zu betreiben. Wärmeunterbetten sollen das Bett vorwärmen und laut TÜV-Verband nicht während des Schlafens laufen.
- **Abschaltautomatik:** Kaufe nur Modelle mit Überhitzungsschutz und Abschaltautomatik. Alte Decken ohne diese Funktionen nicht mehr verwenden (TÜV-Verband).
- **Eco-Modus der Station:** Manche Stationen schalten den AC-Ausgang bei geringer Last ab. BLUETTI rät für die Elite 100 V2, den ECO-Modus bei Geräten unter 60 W auszuschalten. Prüfe die Einstellung, damit die Decke nachts nicht unbemerkt ausgeht.
- **USB oder Akku:** Laut TÜV-Verband gibt es auch Heizdecken mit Akku oder USB-Anschluss. Die laufen ohne den 230-V-Wechselrichter der Station.

{{% /mehr %}}

## Powerstations mit genug Leistung für einen Heizlüfter

Diese vier Modelle haben laut Hersteller 2.400 bis 3.000 W Dauerleistung und 2 bis 3 kWh Kapazität. Sie schaffen einen 2.000-W-Heizlüfter mit voller Leistung, aber ebenfalls nur für etwa eine Stunde. Für eine Heizdecke reichen sie mehrere Nächte.

{{< produkte art="ps" modelle="Anker SOLIX C2000 Gen 2|EcoFlow DELTA 3 Max Plus|DJI Power 2000|BLUETTI Elite 300" >}}

Welche Größe zu deinem Bedarf passt, zeigt der [Powerstation-Finder](/powerstation-finder/).

## Quellen

{{< quellen >}}
- BBK: [Vorsorge und Handeln bei Stromausfall](https://www.bbk.bund.de/DE/Warnung-Vorsorge/Vorsorge/Stromausfall/stromausfall_node.html), abgerufen am 28.10.2026
- BBK: [Stromausfall – Vorsorge und Selbsthilfe](https://www.bbk.bund.de/SharedDocs/Downloads/DE/Mediathek/Publikationen/Buergerinformationen/stromausfall-vorsorge-selbsthilfe.pdf?__blob=publicationFile) (PDF), Kapitel Stromerzeugung (Leistungsbedarf von Geräten mit Heizelement)
- Verbraucherzentrale: [Elektrische Direktheizung](https://verbraucherzentrale-energieberatung.de/heizen/neue-heiztechnik/elektrische-direktheizung/), abgerufen am 28.10.2026
- TÜV-Verband: [Wärme ohne Risiko: Tipps für den sicheren Gebrauch von Heizdecken](https://www.tuev-verband.de/pressemitteilungen/waerme-ohne-risiko-tipps-und-fuer-den-sicheren-gebrauch-von-heizdecken), 30.01.2024
- EcoFlow: [Benutzerhandbuch DELTA 3 Plus](https://ecoflow-service-us-prod.oss-us-west-1.aliyuncs.com/cms/manual/1777530776809/EcoFlow%20DELTA%203%20Plus_User%20Manual.pdf) (PDF), Abschnitt X-Boost, abgerufen am 28.10.2026
- BLUETTI: [Bedienungsanleitung Elite 100 V2](https://s4.bluettipower.com/bluetti/purchasePageBiz/2026/06/Elite_100_V2_User_Manual_EU_EN-DE-1780889806412-6beb.pdf) (PDF), Abschnitte Power Lifting und ECO-Modus, abgerufen am 28.10.2026
- Dauerleistung und Kapazität der Modelle: Herstellerangaben, verlinkt auf den [Produktseiten](/powerstations/#modelle)
{{< /quellen >}}
