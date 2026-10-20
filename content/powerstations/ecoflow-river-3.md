---
title: "EcoFlow RIVER 3"
modell: "EcoFlow RIVER 3"
layout: produkt
date: 2026-10-19
lastmod: 2026-10-20
description: "EcoFlow RIVER 3 (245 Wh, 300 W, 3,55 kg): technische Daten mit Quellen, Testergebnisse von CHIP und IMTEST, Stärken, Schwächen und Alternativen."
kurzzeile: "245 Wh, 300 W, 3,55 kg – kleinste Kapazität im Vergleich"
kurzfazit: |
  Die RIVER 3 ist die leichteste Powerstation mit 230-V-Steckdose und die mit der kleinsten Kapazität in meinem Vergleich (nur die TRAIL 300 DC ohne Steckdose ist leichter): 245 Wh und 300 W Dauerleistung bei 3,55 kg laut EcoFlow. Sie reicht für Handy, Laptop, Licht und Router, aber nicht für Geräte mit Heizelement. IMTEST hat 224 Wh nutzbare Energie und rund eine Stunde Ladezeit gemessen; CHIP bemängelt die wenigen Anschlüsse und kommt nur auf „befriedigend“. Mit 24 Monaten ist die Garantie bei Kauf im EcoFlow-Shop kürzer als bei der RIVER 3 Plus.
fuer:
  - "Wochenend-Camping, Festival, Balkon: Handy, Laptop, Kamera-Akkus, LED-Licht"
  - "Router oder kleiner Rechner als Überbrückung bei kurzen Stromausfällen (USV-Umschaltung < 20 ms laut EcoFlow)"
  - "Wer das Gerät oft tragen will: 3,55 kg"
nicht_fuer:
  - "Wasserkocher, Föhn, Heizlüfter – die Dauerleistung liegt bei 300 W"
  - "Mehrere 230-V-Geräte gleichzeitig: nur eine Steckdose"
  - "Kompressor-Kühlbox über mehrere Tage ohne Nachladen"
quellen:
  - {id: h, titel: "EcoFlow: RIVER 3 – Produktseite und technische Daten", url: "https://de.ecoflow.com/products/river-3-portable-power-station", art: "Hersteller"}
  - {id: g, titel: "EcoFlow: Garantiebestimmungen (Käufe auf de.ecoflow.com)", url: "https://de.ecoflow.com/pages/warranty-policy", art: "Hersteller"}
  - {id: cb, titel: "COMPUTER BILD: EcoFlow stellt neue Powerstations vor (Datentabelle RIVER-3-Serie)", url: "https://www.computerbild.de/artikel/cb-Haus-Garten-Energie-EcoFlow-stellt-neue-Powerstations-vor-38895875.html", art: "Fachpresse, keine Testnote"}
  - {id: chip, titel: "CHIP: EcoFlow River 3 im Test (23.12.2024)", url: "https://www.chip.de/test/ecoflow-river-3-im-test_332943", art: "Test"}
  - {id: im, titel: "IMTEST: Mini-Powerstations im Test", url: "https://www.imtest.de/energie/mini-powerstation-testsieger-2026-hohe-leistung-klein/522617/", art: "Test"}
daten:
  - gruppe: Akku und Leistung
  - {k: Kapazität, v: "245 Wh", q: h}
  - {k: Akkutyp, v: "LiFePO4 (LFP)", q: h}
  - {k: Zyklen, v: "3.000 bis 80 % Restkapazität", q: h}
  - {k: Dauerleistung AC, v: "300 W", q: h}
  - {k: Spitze / X-Boost, v: "600 W", q: h, hinweis: "X-Boost ist für Geräte mit Heizelement gedacht, die mit reduzierter Leistung laufen dürfen."}
  - gruppe: Anschlüsse
  - {k: 230-V-Steckdosen, v: "1", q: h}
  - {k: USB-C, v: "1 × bis 100 W", q: [h, chip], hinweis: "CHIP schreibt dagegen, der USB-C-Port liefere nur 20 W (Quick Charge 2.0) – siehe Widersprüche."}
  - {k: USB-A, v: "2 × 12 W", q: h}
  - {k: Kfz-Ausgang, v: "12,6 V / 10 A, 126 W", q: h}
  - gruppe: Laden
  - {k: AC-Laden, v: "305 W, 0–100 % in 60 min", q: [h, im], hinweis: "IMTEST maß 61 Minuten."}
  - {k: Solareingang, v: "11–30 V, 8 A, max. 110 W; 0–100 % in 2,6 h", q: h}
  - {k: Laden im Auto, v: "100 W, 0–100 % in 2,8 h", q: h}
  - gruppe: Alltag
  - {k: USV-Umschaltung, v: "< 20 ms", q: h, hinweis: "Die Variante „RIVER 3 USV“ gibt EcoFlow mit < 10 ms an."}
  - {k: Gewicht, v: "3,55 kg", q: h}
  - {k: Maße, v: "255 × 212 × 113 mm", q: h}
  - {k: Lautstärke, v: "< 30 dB (Herstellerangabe)", q: h, hinweis: "IMTEST maß unter 36 dB."}
  - {k: Schutzart, v: "IP54 – nur der Akkupack, nicht das ganze Gerät", q: h}
  - {k: Temperatur, v: "Laden 0–45 °C, Entladen −10–45 °C", q: h}
  - {k: Erweiterbar, v: "nein", q: cb}
  - {k: App, v: "ja", q: chip}
  - {k: Garantie, v: "24 Monate (Kauf auf de.ecoflow.com)", q: [g, cb]}
widersprueche:
  - {t: "**USB-C-Leistung:** EcoFlow nennt bis zu 100 W, CHIP schreibt von 20 W nach Quick Charge 2.0. Wer ein Notebook über USB-C laden will, sollte das vor dem Kauf beim Händler oder Hersteller klären.", q: [h, chip]}
  - {t: "**Lautstärke:** EcoFlow gibt unter 30 dB an, IMTEST hat unter 36 dB gemessen. Messabstand und Last unterscheiden sich vermutlich.", q: [h, im]}
staerken:
  - {t: "Leicht und kompakt: 3,55 kg, 255 × 212 × 113 mm", q: h}
  - {t: "Schnell geladen: laut EcoFlow 60 Minuten an der Steckdose, IMTEST maß 61 Minuten", q: [h, im]}
  - {t: "Im IMTEST-Test 224 Wh nutzbar, also gut 91 % der Nennkapazität", q: im}
  - {t: "Leise; CHIP lobt außerdem die App", q: [chip, im]}
schwaechen:
  - {t: "Nur 300 W Dauerleistung und eine Steckdose; CHIP kritisiert die wenigen Schnittstellen", q: [h, chip]}
  - {t: "CHIP misst einen Gesamtwirkungsgrad von 79 %", q: chip}
  - {t: "Solareingang nur bis 110 W", q: h}
  - {t: "Garantie 24 Monate, bei der RIVER 3 Plus 5 Jahre", q: g}
  - {t: "Keine Taschenlampe, kein kabelloses Laden (IMTEST)", q: im}
tests:
  - name: CHIP
    datum: "23.12.2024"
    url: "https://www.chip.de/test/ecoflow-river-3-im-test_332943"
    urteil: "Testurteil 3,3 – befriedigend"
    text: "Gesamtwirkungsgrad 79 %. Positiv: kurze Ladezeit, leiser Betrieb, relativ geringes Gewicht, App. Negativ: wenige Schnittstellen, maximal 300 W."
  - name: IMTEST
    datum: "2026"
    url: "https://www.imtest.de/energie/mini-powerstation-testsieger-2026-hohe-leistung-klein/522617/"
    urteil: "gut (1,95)"
    text: "224 Wh nutzbare Energie, Ladezeit 61 Minuten, unter 36 dB. Kritik: kein kabelloses Laden, keine Taschenlampe."
alternativen:
  - {slug: ecoflow-river-3-plus, warum: "Doppelte Dauerleistung (600 W), drei Steckdosen, erweiterbar und 5 Jahre Garantie, wiegt aber 1,15 kg mehr. Laut EcoFlow seit 30.01.2026 in Deutschland ausgelaufen."}
  - {slug: anker-solix-c300x, warum: "Ähnliche Klasse mit 2 × 140 W USB-C und 5 Jahren Garantie, Solar aber ebenfalls nur 100 W."}
  - {slug: jackery-explorer-300-plus, warum: "Gleiche Klasse; CHIP nennt sie „Mobile Empfehlung“, misst aber nur 63 % Wirkungsgrad."}
---
