// Amortisationsrechner: rechnet nur im Browser, speichert nichts, kein Tracking.
(function () {
  var form = document.getElementById('amort');
  if (!form) return;
  var out = document.getElementById('a-ergebnis');
  var preset = document.getElementById('preset');
  var spezEl = document.getElementById('spez');
  var nf0 = new Intl.NumberFormat('de-DE', { maximumFractionDigits: 0 });
  var nf1 = new Intl.NumberFormat('de-DE', { maximumFractionDigits: 1, minimumFractionDigits: 1 });
  var eur = new Intl.NumberFormat('de-DE', { style: 'currency', currency: 'EUR', maximumFractionDigits: 0 });
  function v(id) { var x = parseFloat(String(document.getElementById(id).value).replace(',', '.')); return isFinite(x) ? x : NaN; }
  function clamp(x, a, b) { return Math.min(b, Math.max(a, x)); }
  // Jahre bis zur Amortisation; Strompreis ändert sich jährlich um g (z. B. 0,02)
  function amort(kosten, s1, g, max) {
    if (s1 <= 0) return Infinity;
    if (!g) return kosten / s1;
    var sum = 0;
    for (var j = 0; j < max; j++) {
      var s = s1 * Math.pow(1 + g, j);
      if (sum + s >= kosten) return j + (kosten - sum) / s;
      sum += s;
    }
    return Infinity;
  }
  function summe(s1, g, n) { var t = 0; for (var j = 0; j < n; j++) t += s1 * Math.pow(1 + g, j); return t; }
  function jahre(x) { return isFinite(x) ? nf1.format(Math.round(x * 10) / 10) + ' Jahre' : 'nicht innerhalb von 50 Jahren'; }
  preset.addEventListener('change', function () { if (preset.value) spezEl.value = preset.value; rechne(); });
  spezEl.addEventListener('input', function () { if (preset.value && preset.value !== spezEl.value) preset.value = ''; });
  function rechne() {
    var wp = v('wp'), kosten = v('kosten'), spez = v('spez'), ev = v('ev'), preis = v('preis'), g = v('steig'), n = v('jahre');
    var h = '<h2>Ergebnis</h2>';
    if (!(wp > 0) || !(spez > 0) || !(ev > 0) || !(preis > 0)) { out.innerHTML = h + '<p>Bitte Modulleistung, Ertrag, Eigenverbrauch und Strompreis mit Werten über 0 ausfüllen.</p>'; return; }
    ev = clamp(ev, 1, 100) / 100; g = isFinite(g) ? clamp(g, -10, 15) / 100 : 0; n = isFinite(n) ? clamp(Math.round(n), 1, 30) : 20;
    var ertrag = wp / 1000 * spez;
    var eigen = ertrag * ev;
    var s1 = eigen * preis / 100;
    h += '<p>Jahresertrag: ' + nf0.format(wp) + ' Wp × ' + nf0.format(spez) + ' kWh/kWp = <strong>' + nf0.format(ertrag) + ' kWh</strong></p>';
    h += '<p>Davon selbst genutzt (' + nf0.format(ev * 100) + ' %): <strong>' + nf0.format(eigen) + ' kWh</strong> · Rest fließt ohne Vergütung ins Netz</p>';
    h += '<p>Ersparnis im ersten Jahr: ' + nf0.format(eigen) + ' kWh × ' + nf1.format(preis) + ' ct = <strong>' + eur.format(s1) + '</strong></p>';
    if (!(kosten > 0)) {
      h += '<p class="warnbox">Trag deine Anschaffungskosten ein, dann siehst du, nach wie vielen Jahren sich die Anlage bezahlt gemacht hat.</p>';
    } else {
      var a = amort(kosten, s1, g, 50);
      var tot = summe(s1, g, n);
      h += '<p class="big">Amortisiert nach etwa ' + jahre(a) + '</p>';
      h += '<p>Über ' + n + ' Jahre gespart: ' + eur.format(tot) + ' − ' + eur.format(kosten) + ' Kosten = <strong>' + eur.format(tot - kosten) + '</strong>' + (g ? ' (mit ' + nf1.format(g * 100) + ' % Preisänderung pro Jahr)' : '') + '</p>';
      if (isFinite(a) && a > n) h += '<p class="warnbox">Die Amortisation liegt hinter deinem Betrachtungszeitraum. Bei Speichern lohnt sich ein Blick auf die Lebensdauer: Anker nennt für die Solarbank 15 Jahre.</p>';
      // Spannbreite
      h += '<h3>Wie empfindlich ist das Ergebnis?</h3><p class="note">Gleiche Kosten und gleicher Strompreis, nur Ertrag und Eigenverbrauch verändert.</p>';
      h += '<div class="tablewrap"><table class="cmp"><thead><tr><th>Eigenverbrauch</th><th class="r">Ertrag −15 %</th><th class="r">Ertrag wie eingegeben</th><th class="r">Ertrag +15 %</th></tr></thead><tbody>';
      [ev - 0.15, ev, ev + 0.15].forEach(function (e) {
        if (e <= 0 || e > 1) return;
        h += '<tr><th scope="row">' + nf0.format(e * 100) + ' %' + (e === ev ? ' (deine Angabe)' : '') + '</th>';
        [0.85, 1, 1.15].forEach(function (k) { h += '<td class="r">' + jahre(amort(kosten, ertrag * k * e * preis / 100, g, 50)) + '</td>'; });
        h += '</tr>';
      });
      h += '</tbody></table></div>';
    }
    if (wp > 2000) h += '<p class="warnbox">Mehr als 2.000 Wp: Dann gelten die vereinfachten Regeln für Steckersolargeräte nicht mehr. Kläre die Anmeldung mit deinem Netzbetreiber.</p>';
    else if (wp > 960) h += '<p class="warnbox">Mehr als 960 Wp: Laut Umweltbundesamt ist der normale Schukostecker dann nicht mehr normgerecht; nötig ist eine spezielle Energiesteckvorrichtung, die eine Elektrofachkraft installiert.</p>';
    out.innerHTML = h;
  }
  form.addEventListener('input', rechne);
  form.addEventListener('change', rechne);
  form.addEventListener('submit', function (e) { e.preventDefault(); });
  if (preset.value) spezEl.value = preset.value;
  // Vorbelegung per Link, z. B. ?wp=800&ev=45 – nur Zahlen im erlaubten Bereich
  var qs = new URLSearchParams(location.search);
  ['wp', 'kosten', 'spez', 'ev', 'preis', 'steig', 'jahre'].forEach(function (id) {
    var raw = qs.get(id); if (raw === null) return;
    var x = parseFloat(raw.replace(',', '.')), el = document.getElementById(id);
    if (!isFinite(x) || x < parseFloat(el.min) || x > parseFloat(el.max)) return;
    el.value = x;
    if (id === 'spez') preset.value = '';
  });
  if (qs.get('spez') && preset.querySelector('option[value="' + spezEl.value + '"]')) preset.value = spezEl.value;
  rechne();
})();
