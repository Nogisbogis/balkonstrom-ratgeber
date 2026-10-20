// Powerstation-Finder: transparente Regeln, keine Speicherung, kein Tracking.
(function () {
  var form = document.getElementById('finder');
  var out = document.getElementById('finder-ergebnis');
  var el = document.getElementById('ps-daten');
  if (!form || !out || !el) return;
  var daten = JSON.parse(el.textContent);
  var ETA = 0.85; // Annahme: nutzbarer Anteil der Nennkapazität
  var nf = new Intl.NumberFormat('de-DE', { maximumFractionDigits: 2 });
  function f(n) { return nf.format(n); }
  function wert(name) {
    var r = form.querySelector('input[name="' + name + '"]:checked');
    if (!r) return NaN;
    if (r.value === 'custom') return parseFloat(form.elements[name + '_custom'].value);
    return parseFloat(r.value);
  }
  function esc(s) { return String(s).replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); }
  // Eingabe in ein Zahlenfeld wählt automatisch die Option "genau"
  ['watt', 'wh'].forEach(function (n) {
    form.elements[n + '_custom'].addEventListener('input', function () {
      form.querySelector('input[name="' + n + '"][value="custom"]').checked = true;
    });
  });
  // Vorbelegung per Link, z. B. ?einsatz=van&kg=5 – nur bekannte Optionen oder Zahlen
  var qs = new URLSearchParams(location.search), vorbelegt = false;
  ['einsatz', 'watt', 'wh', 'kg'].forEach(function (n) {
    var v = qs.get(n); if (v === null) return;
    var r = form.querySelector('input[name="' + n + '"][value="' + (/^[a-z0-9]+$/.test(v) ? v : '') + '"]');
    if (r && v !== 'custom') { r.checked = true; vorbelegt = true; return; }
    var c = form.elements[n + '_custom'], x = parseFloat(v);
    if (c && isFinite(x) && x > 0 && x <= parseFloat(c.max)) { c.value = x; form.querySelector('input[name="' + n + '"][value="custom"]').checked = true; vorbelegt = true; }
  });
  if (vorbelegt) {
    var hint = document.createElement('p');
    hint.className = 'notice'; hint.id = 'vorbelegt';
    hint.textContent = 'Einige Antworten sind über den Link vorausgewählt. Prüf sie kurz – du kannst alles ändern.';
    form.insertBefore(hint, form.firstChild);
  }
  var sortText = {
    camping: 'leichteste zuerst',
    van: 'größter Solareingang zuerst',
    notstrom: 'kürzeste USV-Umschaltzeit zuerst, dann größte Kapazität',
    werkzeug: 'höchste Dauerleistung zuerst'
  };
  function sortiere(liste, einsatz) {
    return liste.sort(function (a, b) {
      // Derzeit bei Amazon nicht verfügbare Modelle stehen hinter den verfügbaren (sonst gleiche Regeln)
      if (!!a.na !== !!b.na) return a.na ? 1 : -1;
      if (einsatz === 'van') return b.pv - a.pv || a.kg - b.kg;
      if (einsatz === 'notstrom') return (a.usv || 999) - (b.usv || 999) || b.wh - a.wh;
      if (einsatz === 'werkzeug') return b.w - a.w || a.kg - b.kg;
      return a.kg - b.kg || b.wh - a.wh;
    });
  }
  function pruefe(p, w, wh, kg, einsatz) {
    var nutz = p.wh * ETA;
    var c = [
      { ok: p.w >= w, t: 'Dauerleistung ' + f(p.w) + ' W ' + (p.w >= w ? '≥' : '<') + ' ' + f(w) + ' W' },
      { ok: nutz >= wh, t: f(p.wh) + ' Wh × 85 % = ' + f(Math.round(nutz)) + ' Wh ' + (nutz >= wh ? '≥' : '<') + ' ' + f(wh) + ' Wh' },
      { ok: p.kg <= kg, t: f(p.kg) + ' kg ' + (p.kg <= kg ? '≤' : '>') + ' ' + (kg >= 99 ? 'keine Grenze' : f(kg) + ' kg') }
    ];
    // Reine DC-Stationen (ohne 230-V-Steckdose) taugen nicht für Notstrom oder Werkzeug
    if (p.dc && (einsatz === 'notstrom' || einsatz === 'werkzeug')) c.push({ ok: false, t: 'keine 230-V-Steckdose (nur USB und 12 V)' });
    return c;
  }
  var sortGrund = {
    camping: function (p) { return 'für unterwegs zählt das Gewicht: ' + f(p.kg) + ' kg'; },
    van: function (p) { return 'für mehrere Tage mit Solar zählt der Solareingang: ' + f(p.pv) + ' W'; },
    notstrom: function (p) { return p.usv ? 'für den Stromausfall zählt die Umschaltzeit: USV ≤ ' + p.usv + ' ms laut Hersteller' : 'für den Stromausfall zählt die Umschaltzeit: dieses Modell hat keine USV'; },
    werkzeug: function (p) { return 'für Werkzeug zählt die Dauerleistung: ' + f(p.w) + ' W'; }
  };
  var EINSATZ = 'camping';
  function karte(p, checks, knapp) {
    var h = '<div class="treffer' + (knapp ? ' knapp' : '') + '"><h3><a href="' + esc(p.url) + '">' + esc(p.m) + '</a></h3>';
    h += '<p class="note">' + f(p.wh) + ' Wh · ' + f(p.w) + ' W' + (p.dc ? ' (nur DC)' : '') + ' · ' + f(p.kg) + ' kg · Solar ' + f(p.pv) + ' W · ' + (p.usv ? 'USV ≤ ' + p.usv + ' ms' : 'keine USV') + ' · ' + esc(p.akku) + '</p><p class="regeln-titel"><strong>' + (knapp ? 'Knapp daneben, weil eine Regel nicht erfüllt ist:' : 'Passt, weil:') + '</strong></p><ul class="regeln">';
    checks.forEach(function (c) { h += '<li>' + (c.ok ? '<span class="mk mk-ja" aria-hidden="true">+</span> ' : '<span class="mk mk-nein" aria-hidden="true">–</span> <span class="sr">nicht erfüllt: </span>') + esc(c.t) + '</li>'; });
    h += '<li>' + (knapp ? '' : '<span class="mk mk-ja" aria-hidden="true">+</span> ') + esc(sortGrund[EINSATZ](p)) + '</li></ul>';
    if (p.warn) h += '<p class="warnbox">' + esc(p.warn) + '</p>';
    if (p.na) h += '<p class="amz-na-zeile"><span class="amz-na">Derzeit bei Amazon nicht verfügbar</span></p>';
    h += '<p><a href="' + esc(p.url) + '">Datenblatt, Tests &amp; Quellen</a> · <a href="../laufzeitrechner/?m=' + encodeURIComponent(p.s) + '">Laufzeit jetzt ausrechnen</a></p></div>';
    return h;
  }
  // Schritt für Schritt: eine Frage pro Ansicht (ohne JS stehen alle Fragen untereinander)
  var sets = Array.prototype.slice.call(form.querySelectorAll('fieldset'));
  var submitP = form.querySelector('button[type=submit]').parentNode;
  var nav = document.createElement('div');
  nav.className = 'wiz-nav';
  nav.innerHTML = '<p class="wiz-stand" aria-live="polite"></p><p class="wiz-btns"><button type="button" class="btn-sec wiz-zurueck">Zurück</button> <button type="button" class="btn wiz-weiter">Weiter</button></p>';
  form.insertBefore(nav, submitP);
  form.insertBefore(nav.querySelector('.wiz-stand'), sets[0]);
  var stand = form.querySelector('.wiz-stand'), zur = nav.querySelector('.wiz-zurueck'), wei = nav.querySelector('.wiz-weiter');
  var schritt = 0;
  function zeige(i, fokus) {
    schritt = Math.max(0, Math.min(sets.length - 1, i));
    sets.forEach(function (fs, k) { fs.hidden = k !== schritt; });
    stand.innerHTML = '<span class="wiz-text">Frage ' + (schritt + 1) + ' von ' + sets.length + '</span><span class="bar" aria-hidden="true"><i style="width:' + ((schritt + 1) / sets.length * 100) + '%"></i></span>';
    zur.hidden = schritt === 0;
    wei.hidden = schritt === sets.length - 1;
    submitP.hidden = schritt !== sets.length - 1;
    if (fokus) { var lg = sets[schritt].querySelector('legend'); lg.setAttribute('tabindex', '-1'); lg.focus(); }
  }
  form.classList.add('wiz');
  wei.addEventListener('click', function () { zeige(schritt + 1, true); });
  zur.addEventListener('click', function () { out.innerHTML = ''; zeige(schritt - 1, true); });
  zeige(0, false);
  form.addEventListener('submit', function (e) {
    e.preventDefault();
    var einsatz = (form.querySelector('input[name="einsatz"]:checked') || {}).value || 'camping';
    EINSATZ = sortText[einsatz] ? einsatz : 'camping';
    var w = wert('watt'), wh = wert('wh'), kg = wert('kg');
    if (!(w > 0) || !(wh > 0)) { out.innerHTML = '<p class="warnbox">Bitte bei „genau“ eine Zahl größer als 0 eintragen.</p>'; return; }
    var passt = [], knapp = [];
    daten.forEach(function (p) {
      var c = pruefe(p, w, wh, kg, einsatz);
      var fehl = c.filter(function (x) { return !x.ok; }).length;
      if (fehl === 0) passt.push({ p: p, c: c }); else if (fehl === 1) knapp.push({ p: p, c: c });
    });
    var key = function (x) { return x.p; };
    var ps = sortiere(passt.map(key), einsatz);
    var ks = sortiere(knapp.map(key), einsatz);
    var find = function (arr, p) { return arr.filter(function (x) { return x.p === p; })[0].c; };
    var h = '<h2>Ergebnis</h2>';
    h += '<p>Deine Angaben: bis ' + f(w) + ' W gleichzeitig, ' + f(wh) + ' Wh pro Ladung, Gewicht ' + (kg >= 99 ? 'egal' : 'bis ' + f(kg) + ' kg') + '. Sortierung: ' + sortText[einsatz] + '.</p>';
    if (ps.length) {
      h += '<p><strong>' + ps.length + ' von ' + daten.length + ' Modellen erfüllen alle drei Regeln.</strong></p>';
      ps.forEach(function (p) { h += karte(p, find(passt, p), false); });
    } else {
      h += '<p class="warnbox">Kein Modell in meinem Vergleich erfüllt alle drei Regeln. Unten stehen die Modelle, die nur an einer Regel scheitern.</p>';
    }
    if (ks.length) {
      h += '<h3>Knapp daneben (eine Regel nicht erfüllt)</h3>';
      ks.forEach(function (p) { h += karte(p, find(knapp, p), true); });
    }
    if (einsatz === 'notstrom') h += '<p class="note">Notstrom: Die USV-Funktion der Powerstations ist laut Herstellern keine unterbrechungsfreie 0-ms-USV. Einspeisen ins Hausnetz nur durch einen Elektrofachbetrieb (BBK).</p>';
    out.innerHTML = h;
    out.querySelector('h2').setAttribute('tabindex', '-1');
    out.querySelector('h2').focus();
  });
})();
