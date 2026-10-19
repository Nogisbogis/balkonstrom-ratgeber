---
title: "Jackery Explorer 1000 v2"
modell: "Jackery Explorer 1000 v2"
layout: produkt
date: 2026-10-19
lastmod: 2026-10-19
description: "Jackery Explorer 1000 v2 (1.070 Wh, 1.500 W, 10,8 kg): technische Daten mit Quellen, ADAC-Ergebnis „mangelhaft“ wegen nicht entkoppelter DC-Eingänge, IMTEST, Stärken, Schwächen."
kurzzeile: "1.070 Wh, 1.500 W, 10,8 kg – ADAC „mangelhaft“ (DC-Eingänge)"
warnung: "**ADAC (06/2025): „mangelhaft“ (5,0)** wegen nicht entkoppelter DC-Eingänge. Wer gleichzeitig über Solar und Auto lädt, riskiert laut ADAC Schäden am 12-V-Bordnetz. Nicht gleichzeitig über Auto und Solar laden. Wir verlinken dieses Modell deshalb nicht zum Kauf."
kurzfazit: |
  Die Explorer 1000 v2 ist mit 10,8 kg die leichteste Station der 1-kWh-Klasse in unserem Vergleich und laut IMTEST leise (38 dB). Der ADAC hat sie 2025 aber mit „mangelhaft“ (5,0) bewertet, weil die DC-Eingänge nicht voneinander entkoppelt sind. Im Jackery-Helpcenter steht inzwischen, dass gleichzeitiges Laden über Solar und Auto nicht zulässig ist. IMTEST vergab nach altem Verfahren „gut (2,13)“. Wir führen die Station zur Vollständigkeit, aber ohne Kauflink.
fuer:
  - "Wer sie ausschließlich an Steckdose oder Solar lädt und nie zugleich über Auto und Solar"
  - "Leise Nutzung im Zelt oder Wohnmobil (IMTEST: 38 dB)"
nicht_fuer:
  - "Laden im Fahrzeug, wenn gleichzeitig Solar angeschlossen sein könnte (ADAC-Sicherheitsmangel)"
  - "Solar über 400 W"
  - "Geräte über 1.500 W Dauerlast"
quellen:
  - {id: h, titel: "Jackery Helpcenter: Explorer 1000 V2 – Grundlegende Informationen (JE-1000D)", url: "https://helpcenter.eu.jackery.com/hc/de/articles/52683026571291-Explorer-1000-V2-Grundlegende-Informationen", art: "Hersteller"}
  - {id: adac, titel: "ADAC: Mobile Powerstations im Test 2025 (11.06.2025)", url: "https://www.adac.de/rund-ums-haus/energie/versorgung/mobile-powerstations-test/", art: "Test"}
  - {id: adac1, titel: "ADAC: Einzelergebnis Jackery Explorer 1000 v2", url: "https://www.adac.de/rund-ums-haus/energie/versorgung/mobile-powerstations-test/jackery-explorer-1000-v2-id-5032/", art: "Test"}
  - {id: im, titel: "IMTEST: Jackery Explorer 1000 v2 im Test", url: "https://www.imtest.de/energie/jackery-explorer-1000-v2-tragbare-portable-powerstation-test-review/527517/", art: "Test"}
daten:
  - gruppe: Akku und Leistung
  - {k: Kapazität, v: "1.070 Wh", q: h}
  - {k: Akkutyp, v: "LiFePO4 (LFP)", q: h}
  - {k: Zyklen, v: "4.000 bis 70 %", q: h, hinweis: "Andere Hersteller geben meist Zyklen bis 80 % an – die Werte sind nicht direkt vergleichbar."}
  - {k: Dauerleistung AC, v: "1.500 W", q: h}
  - {k: Spitze, v: "3.000 W", q: h}
  - gruppe: Anschlüsse
  - {k: 230-V-Steckdosen, v: "3 (Jackery) / 2 (IMTEST)", q: [h, im], hinweis: "Siehe Widersprüche."}
  - {k: USB gesamt, v: "4 Anschlüsse (Jackery) / 3 (IMTEST)", q: [h, im]}
  - {k: USB-C, v: "1 × 100 W + 1 × 30 W (kein USB-C-Eingang)", q: h}
  - {k: USB-A, v: "max. 18 W", q: h}
  - {k: Kfz-Ausgang, v: "12 V / 10 A", q: h}
  - gruppe: Laden
  - {k: AC-Laden, v: "ca. 1,7 h; schneller per App-Notladung", q: h, hinweis: "IMTEST maß 1 h 37 min regulär, knapp 1 h per Notfall-Ladung."}
  - {k: Solareingang, v: "2 × DC8020, 16–60 V; 1 Port 200 W, 2 Ports parallel 400 W", q: h}
  - {k: Ladezeit Solar, v: "SolarSaga 200: 1 Modul ca. 7,5 h, 2 Module ca. 3,8 h", q: h}
  - {k: Auto, v: "12–16 V, 8 A, ca. 12 h; Auto-Schnellladung ca. 3 h", q: h}
  - {k: Solar + Auto gleichzeitig, v: "laut Jackery nicht zulässig", q: [h, adac]}
  - gruppe: Alltag
  - {k: USV-Umschaltung, v: "20 ms", q: h, hinweis: "Dieselbe Jackery-Tabelle nennt „EPS-Funktion: keine“ – siehe Widersprüche."}
  - {k: Gewicht, v: "ca. 10,8 kg", q: h}
  - {k: Maße, v: "32,7 × 22,4 × 24,7 cm", q: h}
  - {k: Lüfter, v: "≤ 22 dB (Herstellerangabe)", q: h, hinweis: "IMTEST maß 38 dB."}
  - {k: Standby-Verbrauch, v: "18 W", q: h}
  - {k: Licht, v: "LED-Beleuchtung", q: h}
  - {k: Erweiterbar, v: "nein", q: h}
  - {k: App, v: "ja", q: h}
  - {k: Garantie, v: "3 Jahre + 2 Jahre nach Registrierung", q: h, hinweis: "IMTEST nennt 3 Jahre."}
widersprueche:
  - {t: "**Steckdosen:** Das Jackery-Helpcenter nennt drei AC-Ausgänge, IMTEST beschreibt zwei Steckdosen. Möglicherweise gibt es Regionalvarianten – vor dem Kauf prüfen.", q: [h, im]}
  - {t: "**USB-Anschlüsse:** Jackery nennt vier USB-Anschlüsse, IMTEST zählt einen USB-A- und zwei USB-C-Ports.", q: [h, im]}
  - {t: "**USV/EPS:** Die Jackery-Tabelle nennt „EPS-Funktion: keine“, aber eine „UPS-Funktion“ mit 20 ms. Jackery selbst schreibt, die Funktion sei keine 0-ms-USV und nicht für Server oder Workstations gedacht. Wir rechnen mit 20 ms.", q: h}
  - {t: "**Gleichzeitiges Laden:** Zum ADAC-Testzeitpunkt fehlte laut ADAC ein Warnhinweis an Gerät und Anleitung. Das Jackery-Helpcenter bezeichnet gleichzeitiges Laden über Solar und Auto inzwischen als nicht zulässig.", q: [adac, h]}
staerken:
  - {t: "Leicht für 1 kWh: ca. 10,8 kg", q: h}
  - {t: "Leise: IMTEST maß 38 dB", q: im}
  - {t: "IMTEST: 10 h 9 min Laufzeit bei rund 80 W", q: im}
  - {t: "Bis zu 5 Jahre Garantie nach Registrierung", q: h}
schwaechen:
  - {t: "ADAC-Sicherheitsurteil 5,0: DC-Eingänge nicht entkoppelt", q: [adac, adac1]}
  - {t: "Lange reguläre Ladezeit (IMTEST)", q: im}
  - {t: "Solar max. 400 W, 18 W Standby", q: h}
  - {t: "Zyklenangabe nur bis 70 % Restkapazität", q: h}
tests:
  - name: ADAC
    datum: "11.06.2025"
    url: "https://www.adac.de/rund-ums-haus/energie/versorgung/mobile-powerstations-test/jackery-explorer-1000-v2-id-5032/"
    urteil: "5,0 – mangelhaft"
    text: "Teilnoten: Handhabung 1,8, Funktion 2,9, Ausstattung 2,1, Sicherheit 5,0. Grund für die Abwertung: nicht entkoppelte DC-Eingänge; bei gleichzeitigem Laden über Solar und Auto drohen laut ADAC Schäden am 12-V-Bordnetz."
  - name: IMTEST
    datum: "26.06.2025, aktualisiert 18.02.2026"
    url: "https://www.imtest.de/energie/jackery-explorer-1000-v2-tragbare-portable-powerstation-test-review/527517/"
    urteil: "gut (2,13) – nach dem Bewertungsverfahren vor 2025"
    text: "10 h 9 min bei rund 80 W, 38 dB, AC-Laden 1 h 37 min (Notfall-Ladung knapp 1 h), Solar mit 400 W ca. 2¾ h. Kontra: lange reguläre Ladezeit, kein kabelloses Laden."
alternativen:
  - {slug: ecoflow-delta-3-plus, warum: "ADAC-Note 2,1 (Sicherheit 1,0), erweiterbar; 1,7 kg schwerer."}
  - {slug: dji-power-1000-mini, warum: "Kompakter, USV 10 ms, 5 Jahre Garantie; 800 W."}
  - {slug: anker-solix-c1000-gen-2, warum: "2.000 W, CHIP „gut (2,2)“; 11,3 kg."}
---
