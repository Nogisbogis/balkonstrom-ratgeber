+++
title = 'Wie lange hält eine Powerstation einen Kühlschrank?'
foto = 'stromausfall'
seotitle = 'Powerstation & Kühlschrank: So lange reicht der Akku'
date = '2026-10-22'
description = "Wie lange läuft ein Kühlschrank an einer Powerstation mit 1 oder 2 kWh? Rechnung mit EU-Label, Eigenverbrauch des Wechselrichters und Anlaufleistung."
draft = true
kategorie = 'powerstations'
kurzgesagt = 'Ein sparsamer Kühlschrank mit 100 bis 200 kWh im Jahr läuft an einer Powerstation mit rund 1 kWh rechnerisch etwa einen Tag (23 bis 33 Stunden), an einer mit rund 2 kWh etwa zwei Tage. Den Ausschlag geben der Jahresverbrauch auf dem EU-Label und der Eigenverbrauch der Station. Außerdem muss die Spitzenleistung den Anlauf des Kompressors schaffen.'
fuer_dich = ['du deinen Kühlschrank bei einem Stromausfall weiterlaufen lassen willst.', 'du wissen willst, ob 1 oder 2 kWh für einen oder zwei Tage reichen.', 'du den Jahresverbrauch deines Kühlschranks vom EU-Label kennst oder ablesen kannst.']
eher_nicht = ['der Stromausfall nur kurz ist – geschlossen hält ein Kühlschrank laut Verbraucherzentrale vier bis sechs Stunden die Kälte.', 'du mehrere Großgeräte über Tage versorgen willst – dafür reicht eine Powerstation nicht.', 'du beim Camping eine 12-V-Kühlbox nutzt – die läuft ohne Wechselrichter an der Kfz-Buchse.']
weiter = { tool = 'laufzeitrechner', url = '/laufzeitrechner/?m=anker-solix-c1000-gen-2&g=K%C3%BChlschrank~23~24', text = 'Kühlschrank mit 200 kWh im Jahr an der Anker C1000 Gen 2 durchrechnen', artikel = '/posts/powerstation-notstrom-blackout/' }
keywords = ['kühlschrank', 'laufzeit', 'stromausfall', 'anlaufstrom', 'eigenverbrauch']
kurz = [
  '**Mittlere Leistung:** Jahresverbrauch laut EU-Label geteilt durch 8.760 Stunden. 200 kWh im Jahr sind im Mittel rund 23 W oder 548 Wh am Tag.',
  '**Neue Kühlschränke** sollten laut Verbraucherzentrale unter 100 kWh im Jahr liegen, ältere nicht selten mehr als 300 kWh.',
  '**Eigenverbrauch:** Ein eingeschalteter Wechselrichter kostet laut ADAC teils 30 W. Anker nennt für die C2000 Gen 2 9 W, Jackery für die Explorer 1000 v2 18 W. Bei einem Kühlschrank mit 10 bis 30 W im Mittel ist das ähnlich viel wie das Gerät selbst.',
  '**Anlauf:** Der Kompressor braucht beim Start laut Jackery typischerweise das 3- bis 7-Fache seiner Nennleistung. Die Spitzenleistung der Station muss darüber liegen.',
  '**Ohne Strom** hält ein geschlossener Kühlschrank laut Verbraucherzentrale vier bis sechs Stunden die Kälte, ein voller Gefrierschrank oft bis zu 48 Stunden.',
]
[[faq]]
  f = 'Wie lange läuft ein Kühlschrank an einer 1000-Wh-Powerstation?'
  gruppe = 'Laufzeit'
  a = 'Rechnerisch rund 18 bis 33 Stunden, wenn der Kühlschrank laut EU-Label 100 bis 300 kWh im Jahr braucht. Angenommen sind 85 % nutzbare Kapazität und 15 W Eigenverbrauch der Station. Ohne Eigenverbrauch wären es 25 bis 76 Stunden, darum lohnt ein Blick auf diesen Wert.'
[[faq]]
  f = 'Wie viel Watt braucht ein Kühlschrank?'
  gruppe = 'Technik'
  a = 'Im Mittel wenig: Jahresverbrauch geteilt durch 8.760 Stunden, bei 200 kWh also rund 23 W. Während der Kompressor läuft, ist es mehr; den Wert nennt das Typenschild. Beim Anlaufen braucht er laut Jackery typischerweise das 3- bis 7-Fache der Nennleistung.'
[[faq]]
  f = 'Reicht eine kleine Powerstation mit 300 Wh für den Kühlschrank?'
  gruppe = 'Laufzeit'
  a = 'Nur für wenige Stunden. Mit 288 Wh, 85 % nutzbar und 15 W Eigenverbrauch kommen rechnerisch 5 bis 9 Stunden heraus. Dazu kommt der Anlauf: Die kleinen Modelle in meinem Vergleich nennen 600 bis 1.500 W Spitzenleistung, die höheren Werte zusammen mit Boost-Modi. Ob dein Kühlschrank anläuft, zeigt nur ein Test.'
[[faq]]
  f = 'Wie lange bleibt ein Kühlschrank ohne Strom kalt?'
  gruppe = 'Laufzeit'
  a = 'Laut Verbraucherzentrale Niedersachsen je nach Füllstand und Isolierung etwa vier bis sechs Stunden, wenn du ihn selten öffnest. Gefrierschränke halten die Temperatur bei geschlossener Tür oft bis zu 48 Stunden, besonders wenn sie gut gefüllt sind.'
+++

Ob eine Powerstation den Kühlschrank durch einen Stromausfall bringt, lässt sich mit zwei Zahlen abschätzen: dem Jahresverbrauch vom EU-Label und der nutzbaren Kapazität der Station. Dazu kommen zwei Haken, die in vielen Rechnungen fehlen: der Eigenverbrauch des Wechselrichters und der Anlauf des Kompressors.

*Ich habe keine eigenen Messungen gemacht. Die Rechnung nutzt die Annahmen meines Laufzeitrechners und die verlinkten Quellen.*

## Die Rechnung in drei Schritten

1. **Verbrauch ablesen:** Auf dem EU-Energielabel steht der Stromverbrauch pro Jahr in kWh. Denselben Wert findest du in der EU-Datenbank EPREL; dorthin führt laut Verbraucherzentrale der QR-Code auf dem Label.
2. **In Watt umrechnen:** kWh pro Jahr × 1.000 ÷ 8.760 Stunden. 200 kWh im Jahr ergeben im Mittel rund 23 W, also 548 Wh am Tag. Der Kompressor läuft nicht ständig, sondern taktet. Der Mittelwert reicht für die Laufzeit.
3. **Teilen:** nutzbare Wattstunden ÷ (Kühlschrank + Eigenverbrauch der Station) = Stunden.

Wie viel ein Kühlschrank braucht, unterscheidet sich stark. Laut Verbraucherzentrale Baden-Württemberg sollte ein neuer Kühlschrank unter 100 kWh im Jahr liegen. Ältere Geräte brauchen nicht selten mehr als 300 kWh, große doppeltürige bis zu 500 kWh. Der Verbrauch hängt laut Verbraucherzentrale außerdem von der eingestellten Temperatur ab. Den echten Wert deines Geräts misst du mit einem Strommessgerät, das du bei den Beratungsstellen der Verbraucherzentralen ausleihen kannst, am besten sieben Tage lang.

## Das Ergebnis: rund ein Tag pro Kilowattstunde

{{< grafik src="img/kuehlschrank-laufzeit.svg" alt="Säulendiagramm, eigene Rechnung mit 85 Prozent nutzbarer Kapazität und 15 Watt Eigenverbrauch. Kühlschrank mit 100 kWh im Jahr: 1-kWh-Klasse rund 33 Stunden, 2-kWh-Klasse rund 66 Stunden. 200 kWh: rund 23 und 46 Stunden. 300 kWh: rund 18 und 35 Stunden." caption="Eigene Rechnung, keine Messung: 85 % der Nennkapazität nutzbar, 15 W Eigenverbrauch der Station, Verbrauch laut EU-Label." >}}

| Kühlschrank laut Label | im Mittel | ~1 kWh (870 Wh nutzbar) | ~2 kWh (1.741 Wh nutzbar) |
|---|---:|---:|---:|
| 100 kWh/Jahr | 11 W | rund 33 h | rund 66 h |
| 200 kWh/Jahr | 23 W | rund 23 h | rund 46 h |
| 300 kWh/Jahr | 34 W | rund 18 h | rund 35 h |

Gerechnet ist mit Stationen mit 1.024 und 2.048 Wh, davon 85 % nutzbar, und 15 W Eigenverbrauch. Eine kleine Station mit 288 Wh kommt mit denselben Annahmen nur auf 5 bis 9 Stunden. Im [Laufzeitrechner](/laufzeitrechner/?m=anker-solix-c1000-gen-2&g=K%C3%BChlschrank~23~24) ist der Kühlschrank mit 200 kWh im Jahr schon eingetragen. Den Eigenverbrauch stellst du dort unter „Annahmen“ ein, voreingestellt sind 0 W.

{{% mehr "So habe ich gerechnet und warum 15 W Eigenverbrauch" %}}

- **85 % nutzbar:** Das ist die Standardannahme im [Laufzeitrechner](/laufzeitrechner/). Bei kleinen Lasten liegt sie eher zu hoch: IMTEST maß an der DJI Power 1000 Mini bei rund 80 W 757 von 1.008 Wh (75 %), Notebookcheck an der Anker SOLIX C2000 Gen 2 bei rund 200 W knapp 79 %.
- **15 W Eigenverbrauch:** Laut ADAC gehen bei eingeschaltetem Wechselrichter „teils schon 30 Watt“ verloren. Anker nennt für die C2000 Gen 2 9 W im Leerlauf (interne Tests), Jackery für die Explorer 1000 v2 18 W Standby. 15 W liegt dazwischen. Für dein Modell setzt du im Rechner den Wert aus Datenblatt oder Test ein.
- **Ohne Eigenverbrauch** wären es an der 1-kWh-Station 76, 38 und 25 Stunden. Beim sparsamen Kühlschrank mit 100 kWh kostet der Eigenverbrauch also mehr als die Hälfte der Laufzeit.
- **Plausibilität:** Anker gibt für die C2000 Gen 2 selbst 30 bis 64 Stunden „maximale Laufzeit für Kühlschrank“ an. Meine Rechnung landet für die 2-kWh-Klasse bei 35 bis 66 Stunden.
- **Nicht berechnet:** häufiges Öffnen, warme Räume, frisch eingeräumte Lebensmittel. All das lässt den Kompressor länger laufen.

{{% /mehr %}}

## Der Anlauf: Spitzenleistung zählt

Ein Kompressor braucht beim Einschalten kurz deutlich mehr Leistung als im Betrieb. Jackery nennt typischerweise das 3- bis 7-Fache der Nennleistung: Ein Kühlschrank mit 200 W Nennleistung brauche beim Start möglicherweise 600 bis 1.400 W. Die Powerstation braucht deshalb zwei Reserven:

- **Dauerleistung** über der Nennleistung des Kühlschranks (Typenschild).
- **Spitzenleistung** über der Anlaufleistung. Die Stationen der 1-kWh-Klasse in meinem Vergleich nennen 1.000 bis 3.600 W, die kleinen mit rund 300 Wh 600 bis 1.500 W. Die Werte über 600 W stehen bei den kleinen aber zusammen mit Boost-Modi im Datenblatt (EcoFlow X-Boost, BLUETTI Power Lifting).

Vorsicht bei Boost-Modi: BLUETTI schreibt im Handbuch der Elite 100 V2, dass „Power Lifting“ nur für ohmsche Lasten wie Heizgeräte gilt. Für einen Kompressor zählt die normale Spitzenleistung. Jackery rät, im Zweifel beim Hersteller des Kühlschranks nachzufragen, ob das Gerät an einer Powerstation laufen darf. Teste es am besten, bevor du es im Notfall brauchst.

{{< produkte art="ps" modelle="Anker SOLIX C1000 Gen 2|EcoFlow DELTA 3 Plus|Anker SOLIX C2000 Gen 2" >}}

## So hält der Akku länger

- **Tür zu:** Geschlossen hält ein Kühlschrank laut Verbraucherzentrale Niedersachsen vier bis sechs Stunden die Kälte, ein voller Gefrierschrank oft bis zu 48 Stunden. Jedes Öffnen kostet Laufzeit.
- **Nur den Kühlschrank anschließen:** Router, Licht und Handy brauchen zusätzlich Energie. Handys lädst du über die USB-Ausgänge, dafür muss der Wechselrichter nicht laufen.
- **Abschaltautomatik prüfen:** Viele Stationen schalten die Steckdosen im Leerlauf ab, um Energie zu sparen. Bei der Anker C1000 Gen 2 passiert das laut Handbuch nur, wenn 15 Minuten lang kein Stecker erkannt wird. Bei anderen Modellen steht die Einstellung im Handbuch oder in der App. Sie darf den Kühlschrank nicht in einer Kompressorpause abschalten.
- **Nachladen:** Mit einem Solarpanel verlängerst du die Laufzeit, wenn die Sonne scheint. Was dabei passen muss, steht in [Powerstation mit Solarpanel kombinieren](/posts/powerstation-solarpanel-kombinieren/).

{{% mehr "Camping: Kühlbox statt Kühlschrank" %}}

Unterwegs ist eine 12-V-Kompressorkühlbox an der Kfz-Buchse der Station oft die bessere Wahl, weil dann kein Wechselrichter mitläuft. Der ADAC rät, den Wechselrichter auszuschalten, wenn die 230-V-Steckdosen nicht gebraucht werden. Für eine Kühlbox mit 50 W rechnet der ADAC an einer 1.000-Wh-Station mit rund 20 Stunden. Mehr dazu im Artikel [Beste Powerstation fürs Camping](/posts/powerstation-camping-kaufberatung/).

{{% /mehr %}}

Was eine Powerstation sonst im Stromausfall kann und was nicht, steht im Artikel [Powerstation als Notstrom](/posts/powerstation-notstrom-blackout/). Der [Powerstation-Finder](/powerstation-finder/) hat dafür eine eigene Einstellung.

## Quellen

{{< quellen >}}
- Verbraucherzentrale Baden-Württemberg: [Energiesparmythen: Wir klären auf!](https://www.verbraucherzentrale-bawue.de/pressemitteilungen/energiesparmythen-wir-klaeren-auf-82399), Pressemitteilung vom 16.03.2023
- Verbraucherzentrale: [So finden Sie den passenden Kühlschrank](https://www.verbraucherzentrale.de/wissen/energie/strom-sparen/so-finden-sie-den-passenden-kuehlschrank-10573), Stand 21.09.2026
- Verbraucherzentrale Niedersachsen: [Verpflegung bei Stromausfall](https://www.verbraucherzentrale-niedersachsen.de/wissen/lebensmittel/auswaehlen-zubereiten-aufbewahren/verpflegung-bei-stromausfall-vorraete-sichern-tiefkuehlkost-retten-und-ohne-strom-kochen-124714), Stand 04.08.2026
- Jackery Helpcenter: [Kann eine tragbare Stromversorgung eine Klimaanlage oder einen Kühlschrank versorgen?](https://helpcenter.eu.jackery.com/hc/de/articles/52465576818843-Kann-eine-tragbare-Stromversorgung-eine-Klimaanlage-oder-einen-K%C3%BChlschrank-versorgen), aktualisiert am 14.07.2026
- Jackery Helpcenter: [Explorer 1000 V2 – Grundlegende Informationen](https://helpcenter.eu.jackery.com/hc/de/articles/52683026571291-Explorer-1000-V2-Grundlegende-Informationen) (Standby 18 W)
- ADAC: [Mobile Powerstations im Test 2025](https://www.adac.de/rund-ums-haus/energie/versorgung/mobile-powerstations-test/), 11.06.2025
- Anker: [SOLIX C2000 Gen 2](https://www.ankersolix.com/de/c2000-gen2), Produktseite (Leerlaufverbrauch 9 W und Kühlschrank-Laufzeit laut internen Tests), abgerufen am 22.10.2026
- Anker: [SOLIX C1000 Gen 2 Benutzerhandbuch (A1763)](https://support.ankersolix.com/s/article/Anker-SOLIX-C1000-Gen-2-Portable-Power-Station-Benutzerhandbuch-A1763) (Abschaltung der AC-Ausgänge)
- BLUETTI: [Elite 100 V2 Benutzerhandbuch](https://s4.bluettipower.com/bluetti/purchasePageBiz/2026/06/Elite_100_V2_User_Manual_EU_EN-DE-1780889806412-6beb.pdf) (Power Lifting nur für ohmsche Lasten)
- IMTEST: [DJI Power 1000 Mini im Test](https://www.imtest.de/energie/dji-power-1000-mini-im-test-kleine-powerstation-2026/619685/), 11.10.2026
- Notebookcheck: [Anker Solix C2000 Gen 2 im Praxis-Test](https://www.notebookcheck.com/11-6-kg-leichter-als-der-Vorgaenger-Powerstation-Anker-Solix-C2000-Gen-2-im-Praxis-Test.1230097.0.html), 24.02.2026
- Spitzenleistungen der Modelle: Herstellerangaben, verlinkt auf den [Produktseiten](/powerstations/#modelle)
{{< /quellen >}}
