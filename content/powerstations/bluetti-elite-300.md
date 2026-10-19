---
title: "BLUETTI Elite 300"
modell: "BLUETTI Elite 300"
layout: produkt
date: 2026-10-20T01:00:00+02:00
lastmod: 2026-10-20T01:00:00+02:00
description: "BLUETTI Elite 300 (3.014 Wh, 2.400 W, 26,3 kg): technische Daten aus dem Handbuch mit Quellen, heise-Messwerte (~95,5 % AC-Effizienz), nur zwei Steckdosen, PV bis 60 V, Stärken, Schwächen, Alternativen."
kurzzeile: "3.014 Wh in 26,3 kg, 2.400 W – heise maß ~95,5 % nutzbar"
kurzfazit: |
  Die Elite 300 packt 3.014 Wh in 26,3 kg – für 3 kWh sehr leicht und kompakt. heise konnte bei 500 und 1.000 W rund 2,85 bis 2,89 kWh entnehmen (etwa 95,5 % der Nennkapazität), die USV hielt ein Home-Office-Setup ohne Abbruch. Die Kompromisse: nur zwei Schuko-Steckdosen, 2.400 W Dauerleistung (Power Lifting bis 4.800 W nur für ohmsche Geräte wie Wasserkocher), keine Erweiterung, deutlich hörbare Lüfter und ein Solareingang, dessen Leerlaufspannung 60 V nie überschreiten darf.
fuer:
  - "Notstrom mit viel Kapazität pro Kilogramm"
  - "Wohnmobil: 12-V-Ausgang mit 30 A (XT60) für Kühlschrank und Heizung"
  - "Home-Office-USV (heise: Umschaltung ohne Abbruch)"
nicht_fuer:
  - "Mehr als zwei 230-V-Geräte ohne Mehrfachsteckdose"
  - "Dachmodule in Reihe: PV-Leerlaufspannung max. 60 V"
  - "Ruhige Schlafräume bei AC-Last (hörbare Lüfter)"
quellen:
  - {id: hb, titel: "BLUETTI: Elite 300 – Benutzerhandbuch EU (PDF, EN/DE)", url: "https://s4.bluettipower.com/bluetti/purchasePageBiz/2026/06/Elite_300_User_Manual_EU_EN-DE-1780541601377-0f1e.pdf", art: "Hersteller"}
  - {id: h, titel: "BLUETTI: Elite 300 – Produktseite (DE)", url: "https://de.bluettipower.eu/products/elite-300-tragbare-powerstation", art: "Hersteller"}
  - {id: heise, titel: "heise bestenlisten: Bluetti Elite 300 im Test (9.3.2026)", url: "https://www.heise.de/bestenlisten/testbericht/bluetti-elite-300-weltweit-kleinste-powerstation-mit-3-kwh-im-test/8gembzk", art: "Test"}
  - {id: nbc, titel: "Notebookcheck: Powerstation Bluetti Elite 300 im Praxis-Test", url: "https://www.notebookcheck.com/3-kWh-kompakt-verpackt-Powerstation-Bluetti-Elite-300-im-Praxis-Test.1243566.0.html", art: "Test"}
daten:
  - gruppe: Akku und Leistung
  - {k: Kapazität, v: "3.014,4 Wh", q: hb, hinweis: "heise entnahm 2,85–2,89 kWh bei 500 W und 1.000 W."}
  - {k: Erweiterung, v: "nein", q: nbc}
  - {k: Akkutyp, v: "LiFePO4", q: hb}
  - {k: Zyklen, v: "6.000 bis 80 %", q: heise, hinweis: "Im Handbuch nicht gefunden; Wert laut heise-Test."}
  - {k: Dauerleistung AC, v: "2.400 W (Bypass 2.300 W)", q: hb}
  - {k: Power Lifting, v: "bis 4.800 W, nur ohmsche Geräte (z. B. Wasserkocher, Heizlüfter) – mit abgesenkter Spannung", q: [hb, heise]}
  - gruppe: Anschlüsse
  - {k: 230-V-Steckdosen, v: "2 (Schuko)", q: [nbc, heise], hinweis: "Die Anzahl steht nicht in der Datentabelle des Handbuchs; laut Tests zwei."}
  - {k: USB-C, v: "1 × 100 W, 1 × 140 W", q: hb}
  - {k: USB-A, v: "2 (zusammen 15 W)", q: hb, hinweis: "Notebookcheck nennt je 15 W."}
  - {k: 12 V, v: "Kfz-Buchse 12 V / 10 A und XT60-Ausgang 12 V / 30 A – parallel, zusammen max. 30 A", q: [hb, heise]}
  - gruppe: Laden
  - {k: AC-Laden, v: "bis 2.300 W", q: hb, hinweis: "heise: Turbo 0–100 % in ca. 1 h 52 min."}
  - {k: Solar-/DC-Eingang, v: "XT60, 12–60 V, max. 22 A, bis 1.200 W", q: hb}
  - {k: AC + DC, v: "bis 2.400 W", q: hb}
  - {k: PV-Grenze, v: "Leerlaufspannung (Voc) darf 60 V nie überschreiten", q: [hb, heise]}
  - gruppe: Alltag
  - {k: USV-Umschaltung, v: "≤ 10 ms", q: hb, hinweis: "heise: Home-Office-Setup mit NAS lief ohne Abbruch weiter."}
  - {k: Gewicht, v: "ca. 26,3 kg", q: [hb, nbc]}
  - {k: Maße, v: "366 × 305 × 297,5 mm", q: hb}
  - {k: Lautstärke, v: "heise maß ca. 53 dB in 1 m beim Turbo-Laden bzw. hoher AC-Last", q: heise}
  - {k: Schutzart, v: "IP20", q: [hb, heise]}
  - {k: Garantie, v: "5 Jahre", q: heise, hinweis: "Wert laut heise; die Produktseite war beim Abruf nicht erreichbar."}
widersprueche:
  - {t: "**Steckdosen:** Das Handbuch nennt in der Datentabelle keine Anzahl; Notebookcheck und heise beschreiben zwei Schuko-Steckdosen.", q: [hb, nbc]}
staerken:
  - {t: "Sehr hohe gemessene AC-Effizienz: ~95,5 % der Nennkapazität nutzbar", q: heise}
  - {t: "3 kWh in 26,3 kg und 366 × 305 × 297,5 mm", q: hb}
  - {t: "12-V-Ausgang mit 30 A für Camper", q: [hb, heise]}
  - {t: "6.000 Zyklen und 5 Jahre Garantie (heise)", q: heise}
schwaechen:
  - {t: "Nur zwei Steckdosen, nicht erweiterbar, keine Leuchte (Notebookcheck)", q: nbc}
  - {t: "Deutlich hörbare Lüfter bei AC-Last, IP20", q: heise}
  - {t: "Solar max. 60 V / 22 A: zwei Dachmodule in Reihe meist zu viel Spannung", q: heise}
  - {t: "Round-Trip AC→AC laut heise nur rund 77 %", q: heise}
tests:
  - name: heise bestenlisten
    datum: "9.3.2026"
    url: "https://www.heise.de/bestenlisten/testbericht/bluetti-elite-300-weltweit-kleinste-powerstation-mit-3-kwh-im-test/8gembzk"
    urteil: ""
    text: "2,85–2,89 kWh entnommen bei 500 W und 1.000 W (~95,5 %). Turbo-Laden 0–100 % in ca. 1 h 52 min, 3,70–3,74 kWh aus dem Netz, Round-Trip rund 77 %. USV im Bereich der Herstellerangabe (< 10 ms). Bis ca. 53 dB in 1 m. Minus: hörbare Lüfter, PV-Eingang strikt 60 V / 22 A, IP20."
  - name: Notebookcheck
    datum: ""
    url: "https://www.notebookcheck.com/3-kWh-kompakt-verpackt-Powerstation-Bluetti-Elite-300-im-Praxis-Test.1243566.0.html"
    urteil: ""
    text: "Lob für das geringe Gewicht. Kritik: nur zwei Steckdosen, keine Erweiterung, keine LED-Leuchte; 2.400 W können für mehrere Geräte gleichzeitig zu wenig sein."
alternativen:
  - {slug: ecoflow-delta-pro-3, warum: "4 kWh, 4.000 W, erweiterbar – aber 51,5 kg."}
  - {slug: ecoflow-delta-3-max-plus, warum: "2 kWh, 3.000 W, vier Steckdosen, erweiterbar; 22,1 kg."}
  - {slug: anker-solix-c2000-gen-2, warum: "2 kWh in 18,9 kg, vier Steckdosen."}
---
