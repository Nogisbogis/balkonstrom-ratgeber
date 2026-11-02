+++
title = 'Gasheizung bei Stromausfall: Hilft eine Powerstation?'
foto = 'stromausfall'
seotitle = 'Gastherme an der Powerstation: Strombedarf, Laufzeit, Erdung'
date = '2026-11-02'
description = "Läuft die Gasheizung bei Stromausfall an einer Powerstation? Wie viel Watt eine Therme braucht, wie lange 1 bis 3 kWh reichen und warum die Erdung entscheidet."
draft = false
kategorie = 'powerstations'
kurzgesagt = 'Vom Strombedarf her ja: Eine moderne Gastherme braucht laut Vaillant höchstens 55 bis 91 W. Eine Powerstation mit rund 1 kWh reicht damit rechnerisch etwa 8 bis 11 Stunden, eine mit 2 kWh rund 16 bis 21 Stunden. Das Problem ist der Anschluss: Heizungen brauchen ein geerdetes Netz, viele Powerstations liefern aber erdfreien Strom. Das muss eine Elektrofachkraft lösen, bevor der Ernstfall kommt.'
fuer_dich = ['du eine Gas- oder Ölheizung hast und für einen längeren Stromausfall im Winter vorsorgen willst.', 'du wissen willst, ob deine Powerstation genug Kapazität für die Therme hat.', 'du vor dem Gespräch mit deinem Heizungs- oder Elektrobetrieb die Grundlagen kennen willst.']
eher_nicht = ['du eine Wärmepumpe hast – für sie gilt die Rechnung hier nicht.', 'du die Therme selbst umklemmen oder per Kabel in eine Steckdose einspeisen willst – das gehört in die Hand einer Elektrofachkraft.', 'du nur ein paar Stunden überbrücken musst – dann halten Haus und Decken meist die Wärme.']
weiter = { tool = 'laufzeitrechner', url = '/laufzeitrechner/?m=anker-solix-c2000-gen-2&g=Gastherme~66~24', text = 'Gastherme an der Anker C2000 Gen 2 durchrechnen', artikel = '/posts/powerstation-notstrom-blackout/' }
keywords = ['gasheizung', 'gastherme', 'heizung', 'stromausfall', 'notstrom', 'erdung', 'ionisation', 'flammenüberwachung', 'umwälzpumpe']
kurz = [
  '**Ohne Strom keine Wärme:** Regelung, Pumpen und Brenner brauchen Strom. Fällt er aus, bleibt laut Viessmann auch eine intakte Heizung kalt.',
  '**Strombedarf:** 55 bis 91 W maximal inklusive Pumpe bei Vaillants ecoTEC plus, im Standby unter 2 W. Alte ungeregelte Pumpen brauchen laut Verbraucherzentrale allein 80 bis 100 W.',
  '**Laufzeit bei 66 W Dauerlast:** rund 10,7 Stunden an 1 kWh, 21,5 Stunden an 2 kWh, 31,6 Stunden an 3 kWh (eigene Rechnung, 85 % nutzbar, 15 W Eigenverbrauch).',
  '**Knackpunkt Erdung:** Viessmann verlangt ein geerdetes Netz, unter anderem für die Flammenüberwachung. Anker beschreibt den Ausgang der C2000 Gen 2 als erdfrei (Floating Ground). Die Lösung gehört in die Hand einer Elektrofachkraft.',
]
[[faq]]
  f = 'Wie viel Strom braucht eine Gastherme?'
  gruppe = 'Technik'
  a = 'Weniger als viele denken. Vaillant gibt für die Gas-Brennwerttherme ecoTEC plus je nach Modell maximal 55 bis 91 W inklusive Pumpe an, bei 30 % Teillast 41 bis 59 W und im Standby unter 2 W. Hängen zusätzliche Pumpen oder Stellmotoren dran, kommt deren Leistung dazu. Den Wert deiner Therme findest du im Datenblatt oder auf dem Typenschild.'
[[faq]]
  f = 'Wie lange läuft eine Gastherme an einer Powerstation?'
  gruppe = 'Laufzeit'
  a = 'Bei 66 W Dauerlast rechnerisch rund 10,7 Stunden an einer Station mit 1.024 Wh, rund 21,5 Stunden an 2.048 Wh und rund 31,6 Stunden an 3.014 Wh. Angenommen sind 85 % nutzbare Kapazität und 15 W Eigenverbrauch der Station. Da die Therme nicht ständig mit Maximalleistung läuft, ist das eher die vorsichtige Rechnung.'
[[faq]]
  f = 'Warum geht die Gastherme an der Powerstation auf Störung?'
  gruppe = 'Technik'
  a = 'Häufig wegen der fehlenden Erdung. Laut Viessmann-Kundenservice braucht die Heizung ein geerdetes Netz, unter anderem für die Überwachung der Gasflamme. Viele Notstromquellen arbeiten mit Schutztrennung ohne Erdverbindung. Anker beschreibt den AC-Ausgang der C2000 Gen 2 als isoliertes Erdungssystem (Floating Ground). Wie das sicher gelöst wird, klärt eine Elektrofachkraft.'
[[faq]]
  f = 'Darf ich die Heizung selbst an die Powerstation anschließen?'
  gruppe = 'Sicherheit'
  a = 'Nur wenn die Therme ohnehin mit Stecker an einer Steckdose hängt und der Hersteller den Betrieb an einer Notstromquelle zulässt. Fest angeschlossene Thermen umklemmen oder Strom ins Hausnetz einspeisen dürfen nach § 13 NAV nur eingetragene Installationsbetriebe. Viessmann warnt, dass eine fehlerhafte Schaltung lebensgefährlich sein kann.'
[[faq]]
  f = 'Reicht eine Powerstation auch für eine Wärmepumpe?'
  gruppe = 'Technik'
  a = 'Das behandelt dieser Artikel nicht. Die Werte hier gelten für Gasthermen, für eine Wärmepumpe lässt sich die Rechnung nicht übertragen. Frag dafür deinen Heizungsbetrieb.'
+++

Fällt im Winter der Strom aus, wird es auch mit Gasanschluss kalt. Die Gastherme braucht Strom für Regelung, Zündung und Pumpe. Weil sie dafür nur wenig Leistung braucht, liegt die Idee nahe: einfach an die Powerstation hängen. Rein rechnerisch klappt das gut. In der Praxis scheitert es oft an einem Detail, das man vorher klären muss.

*Ich habe keine eigenen Messungen gemacht und keine Therme an einer Powerstation betrieben. Die Leistungsdaten stammen von den Herstellern, die Laufzeiten sind eigene Rechnung. Stand: 02.11.2026.*

## Warum die Heizung ohne Strom ausgeht

Viessmann schreibt es deutlich: Fallen Regelung, Motorventile oder Pumpen aus, liefert die Heizung „auch ohne Defekt keine Wärme mehr“. Das gilt für Gas- und Ölheizungen gleichermaßen. Das BBK zählt die Heizung ebenfalls zu den Dingen, die bei einem Stromausfall nicht mehr funktionieren.

Meist dauert ein Ausfall nur ein paar Stunden. Laut BBK kann es bei großflächigen Schäden aber auch Tage dauern. Erst dann wird es in einem gut gedämmten Haus richtig kalt, und erst dann lohnt sich die Notversorgung der Heizung.

## Wie viel Strom braucht eine Gastherme?

Erstaunlich wenig. Als Beispiel die Herstellerangaben zur Vaillant ecoTEC plus, einer verbreiteten Gas-Brennwerttherme:

| Modell | max. inkl. Pumpe | bei 30 % Teillast | Standby |
|---|---:|---:|---:|
| VC 10CS/1-5 | 66 W | 52 W | < 2 W |
| VC 15CS/1-5 | 56 W | 45 W | < 2 W |
| VC 20CS/1-5 | 55 W | 41 W | 2 W |
| VC 25CS/1-5 | 91 W | 57 W | < 2 W |
| VC 30CS/1-5 | 80 W | 59 W | 2 W |

*Herstellerangaben laut Vaillant, Stand 02.11.2026.*

Das ist nur die Therme selbst. Hat deine Anlage weitere Heizkreispumpen, Mischer oder eine externe Regelung, kommt deren Bedarf dazu. Eine alte, ungeregelte Umwälzpumpe braucht laut Verbraucherzentrale allein 80 bis 100 W, eine moderne Hocheffizienzpumpe 15 W oder weniger. Den Wert deiner Geräte findest du auf dem Typenschild oder im Datenblatt.

{{% mehr "Anlaufströme und Reserve" %}}

Viessmann rät bei Notstromaggregaten, alle gleichzeitig laufenden Verbraucher zu addieren (Brenner, Umwälzpumpen, Stellmotoren). Wegen der Anlaufströme sollte die Auslegung das Zwei- bis Dreifache abdecken. Der Kundenservice nennt für Ein- und Zweifamilienhäuser je nach Ausstattung rund 600 bis 1.000 VA. Der Stromerzeuger-Hersteller Güde empfiehlt, seine Geräte höchstens zu zwei Dritteln auszulasten.

Für Powerstations mit 1.000 bis 2.400 W Dauerleistung ist das in der Regel kein Engpass. Die Grenze setzt eher der Akku, also die Laufzeit.

{{% /mehr %}}

## Wie lange reicht die Powerstation?

Ich rechne wie im [Laufzeitrechner](/laufzeitrechner/): 85 % der Nennkapazität nutzbar, dazu 15 W Eigenverbrauch der Station. Die Zeilen gehen davon aus, dass die Leistung durchgehend anliegt. Taktet die Therme oder steht sie zwischendurch im Standby, hält der Akku länger.

| Dauerlast | ~1 kWh (870 Wh nutzbar) | ~2 kWh (1.741 Wh nutzbar) | ~3 kWh (2.562 Wh nutzbar) |
|---|---:|---:|---:|
| 45 W (Teillast) | 14,5 h | 29 h | 42,7 h |
| 66 W | 10,7 h | 21,5 h | 31,6 h |
| 91 W | 8,2 h | 16,4 h | 24,2 h |
| 150 W (Therme plus alte Pumpe) | 5,3 h | 10,6 h | 15,5 h |

*Eigene Rechnung, keine Messung, Werte gerundet. Kapazitäten: 1.024 Wh, 2.048 Wh und 3.014 Wh laut Hersteller. Die 150-W-Zeile ist eine Beispielannahme.*

**Die Folgerung:** Eine 2-kWh-Station kann eine moderne Therme rechnerisch etwa einen Tag lang versorgen. Laut ADAC gehen bei eingeschaltetem Wechselrichter „teils schon 30 Watt verloren“. Dann wird die Laufzeit bei so kleinen Lasten spürbar kürzer. Wie du die Station sonst im Stromausfall einsetzt, steht im Artikel [Powerstation als Notstrom](/posts/powerstation-notstrom-blackout/).

## Der Knackpunkt: Erdung und Flammenüberwachung

Hier scheitern viele Versuche. Laut Viessmann-Kundenservice sind die Geräte der Heizung für ein geerdetes Netz mit sinusförmiger Spannung von 200 bis 250 V und 49 bis 51 Hz ausgelegt. Die Erdung braucht die Heizung aus drei Gründen: für die elektrische Sicherheit von Pumpen und Geräten, damit der Temperaturbegrenzer sicher abschaltet, und für die Überwachung der Gasflamme.

Viele Notstromquellen arbeiten aber mit **Schutztrennung**, also ohne Erdverbindung. Viessmann schreibt dazu: Ohne Erdverbindung ist das System nicht sicher und darf so nicht betrieben werden. Auch Powerstations sind oft so gebaut. Anker beschreibt den AC-Ausgang der SOLIX C2000 Gen 2 als „isoliertes (Floating Ground)-Erdungssystem“. Für Geräte, die eine Verbindung von Neutralleiter und Erde brauchen, nennt Anker einen Erdungs-Neutralstecker.

Ob so ein Stecker für deine Heizung genügt und sicher ist, kann ich nicht beurteilen. Güde schreibt für seine Stromerzeuger, dass die Umstellung von Schutztrennung auf ein TN-Netz nur eine Elektrofachkraft vornehmen darf. Sie muss auch prüfen, ob die Schutzmaßnahmen danach noch wirken, etwa ein Fehlerstromschutzschalter.

{{% mehr "Steckdose oder fest angeschlossen?" %}}

- **Therme mit Stecker:** Hängt deine Therme an einer Schutzkontaktsteckdose, lässt sich die Station im Ernstfall einstecken. Die Erdungsfrage bleibt trotzdem und sollte vorher geklärt sein.
- **Fest angeschlossen:** Dann musst du in die Hausinstallation eingreifen. Arbeiten hinter der Hausanschlusssicherung dürfen laut § 13 NAV nur der Netzbetreiber oder ein eingetragenes Installationsunternehmen ausführen.
- **Keine Einspeisung über die Steckdose:** Strom per Kabel über eine Steckdose ins Hausnetz zu schicken, ist kein Weg. Viessmann warnt, dass eine fehlerhafte Schaltung lebensgefährlich sein kann.
- **Hersteller fragen:** Güde rät, vorher die Anforderungen beim Heizungshersteller zu erfragen. Viessmann empfiehlt den Kontakt zum Fachpartner.

{{% /mehr %}}

**Mein Rat:** Kläre das mit deinem Heizungs- oder Elektrobetrieb, solange der Strom noch da ist. Am besten testet ihr den Betrieb an der Station gemeinsam. Im Ernstfall ist dafür keine Zeit.

## Powerstations mit genug Kapazität

Diese drei Modelle haben laut Hersteller 1 bis 3 kWh Kapazität und 2.000 bis 2.400 W Dauerleistung. Die Leistung reicht für jede Therme in der Tabelle oben mit viel Reserve. Den Unterschied macht die Kapazität. Die Erdungsfrage stellt sich bei allen und muss vorher geklärt werden.

{{< produkte art="ps" modelle="Anker SOLIX C1000 Gen 2|Anker SOLIX C2000 Gen 2|BLUETTI Elite 300" >}}

Weitere Modelle mit Filter nach Kapazität findest du in der [Powerstation-Suche](/powerstation-suche/), eine Empfehlung nach deinem Bedarf im [Powerstation-Finder](/powerstation-finder/).

## Wenn es ohne Heizung gehen muss

Das BBK rät bei ausgefallener Heizung zu warmer Kleidung und Decken. Halte dich möglichst in einem Raum auf und lass die Türen geschlossen. Gelüftet werden muss trotzdem regelmäßig. Ersatzheizungen nur nach Beratung durch Fachleute einbauen. Gasbetriebene Heizgeräte brauchen laut BBK eine Sauerstoffmangel- und Zündsicherung, ein Kohlenmonoxid-Warnmelder erhöht die Sicherheit. Wer nur sich selbst warm halten will, kommt mit einer [Heizdecke an der Powerstation](/posts/powerstation-heizluefter-heizdecke/) lange aus.

## Quellen

{{< quellen >}}
- Viessmann: [Heizung defekt? Ursachen und Lösungen](https://www.viessmann.ch/de/wissen/wartung-und-reparatur/heizung-defekt.html), Abschnitt Notstromaggregat, abgerufen am 02.11.2026
- Viessmann-Kundenservice: [Antwort zu Betrieb an einem Notstromaggregat](https://community.viessmann.de/t5/Gas/Vitoladens-300-C-Betrieb-an-einem-Notstromaggregat-230V-1500-W/td-p/277618) in der Viessmann-Community, 23.11.2022
- Vaillant: [ecoTEC plus, technische Daten](https://www.vaillant.de/produkte/ecotec-plus/), abgerufen am 02.11.2026
- Verbraucherzentrale: [Heizung optimieren und Heizkosten sparen](https://www.verbraucherzentrale.de/wissen/energie/heizen-und-warmwasser/heizung-optimieren-und-heizkosten-sparen-30096), abgerufen am 02.11.2026
- Anker: [Bedienungsanleitung SOLIX C2000 Gen 2](https://cdn-reichelt.de/documents/datenblatt/D400/ANKER_S_C2000_2_ANL-DE.pdf) (PDF), FAQ Nr. 8 und technische Daten, abgerufen am 02.11.2026
- Güde: [Hinweis zum Betrieb von Stromerzeugern an Heizungsanlagen](https://www.guede.com/sys/dl/40657_40717_40719_40720_40721_40724_zi.pdf) (PDF), abgerufen am 02.11.2026
- BBK: [Vorsorge und Handeln bei Stromausfall](https://www.bbk.bund.de/DE/Warnung-Vorsorge/Vorsorge/Stromausfall/stromausfall_node.html), abgerufen am 02.11.2026
- Bundesministerium der Justiz: [§ 13 NAV – Elektrische Anlage](https://www.gesetze-im-internet.de/nav/__13.html), abgerufen am 02.11.2026
- ADAC: [Mobile Powerstations im Test 2025](https://www.adac.de/rund-ums-haus/energie/versorgung/mobile-powerstations-test/), 11.06.2025
- Kapazität und Dauerleistung der Modelle: Herstellerangaben, verlinkt auf den [Produktseiten](/powerstations/#modelle)
{{< /quellen >}}
