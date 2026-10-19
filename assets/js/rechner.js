// Laufzeitrechner: rechnet nur im Browser, speichert nichts, kein Tracking.
(function () {
  var form = document.getElementById('rechner');
  var el = document.getElementById('ps-daten');
  if (!form || !el) return;
  var daten = JSON.parse(el.textContent);
  var tbody = document.getElementById('zeilen');
  var sel = document.getElementById('modell');
  var eigen = document.getElementById('eigen');
  var out = document.getElementById('r-ergebnis');
  var nf = new Intl.NumberFormat('de-DE', { maximumFractionDigits: 1 });
  function f(n) { return nf.format(n); }
  function num(x) { var v = parseFloat(String(x).replace(',', '.')); return isFinite(v) && v >= 0 ? v : 0; }
  function esc(s) { return String(s).replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); }
  function dauer(h) {
    if (!isFinite(h)) return '–';
    if (h >= 48) return f(Math.round(h / 24 * 10) / 10) + ' Tage';
    var std = Math.floor(h), min = Math.round((h - std) * 60);
    if (min === 60) { std++; min = 0; }
    return std + ' h ' + (min < 10 ? '0' : '') + min + ' min';
  }
  daten.forEach(function (p) {
    var o = document.createElement('option');
    o.value = p.s; o.textContent = p.m + ' (' + f(p.wh) + ' Wh, ' + f(p.w) + ' W)';
    sel.appendChild(o);
  });
  var n = 0;
  function zeile(name, w, h, anz) {
    n++;
    var tr = document.createElement('tr');
    tr.innerHTML = '<td><input type="text" aria-label="Gerät ' + n + '" placeholder="z. B. Kühlbox" value="' + esc(name || '') + '"></td>' +
      '<td><input type="number" min="0" max="5000" step="1" inputmode="numeric" aria-label="Watt Gerät ' + n + '" value="' + (w || '') + '"></td>' +
      '<td><input type="number" min="0" max="240" step="0.5" inputmode="decimal" aria-label="Stunden Gerät ' + n + '" value="' + (h || '') + '"></td>' +
      '<td><input type="number" min="1" max="20" step="1" inputmode="numeric" aria-label="Anzahl Gerät ' + n + '" value="' + (anz || 1) + '"></td>' +
      '<td><button type="button" class="btn-sec" aria-label="Zeile entfernen">✕</button></td>';
    tr.querySelector('button').addEventListener('click', function () { tr.remove(); rechne(); });
    tbody.appendChild(tr);
  }
  document.getElementById('plus').addEventListener('click', function () { zeile(); rechne(); tbody.lastChild.querySelector('input').focus(); });
  function station() {
    var p = daten.filter(function (x) { return x.s === sel.value; })[0];
    if (p) return { name: p.m, wh: p.wh, w: p.w, url: p.url, warn: p.warn };
    return { name: 'eigene Angabe', wh: num(document.getElementById('kap').value), w: num(document.getElementById('dauer').value) };
  }
  function rechne() {
    eigen.hidden = !!sel.value;
    var eta = Math.min(100, Math.max(40, num(document.getElementById('eta').value) || 85)) / 100;
    var ev = num(document.getElementById('eigenv').value);
    var E = 0, P = 0, rows = 0;
    Array.prototype.forEach.call(tbody.rows, function (tr) {
      var i = tr.querySelectorAll('input');
      var w = num(i[1].value), h = num(i[2].value), a = Math.max(1, Math.round(num(i[3].value)) || 1);
      if (w > 0) { rows++; P += w * a; E += w * h * a; }
    });
    var s = station();
    var nutz = s.wh * eta;
    var h = '<h2>Ergebnis</h2>';
    if (!rows) { out.innerHTML = h + '<p>Trag mindestens ein Gerät mit Wattzahl ein.</p>'; return; }
    h += '<p>Nutzbare Energie (Annahme): ' + f(s.wh) + ' Wh × ' + f(Math.round(eta * 100)) + ' % = <strong>' + f(Math.round(nutz)) + ' Wh</strong>' + (s.url ? ' – <a href="' + esc(s.url) + '">' + esc(s.name) + '</a>' : '') + '</p>';
    h += '<p>Dein Bedarf: <strong>' + f(Math.round(E)) + ' Wh</strong> pro Ladung · gleichzeitige Leistung, wenn alles zugleich läuft: <strong>' + f(P) + ' W</strong></p>';
    if (P > s.w) h += '<p class="warnbox">Achtung: ' + f(P) + ' W übersteigt die Dauerleistung von ' + f(s.w) + ' W. Laufen alle Geräte gleichzeitig, schaltet die Station voraussichtlich ab. Geräte nacheinander betreiben oder ein stärkeres Modell wählen.</p>';
    if (E > 0) {
      var anteil = nutz / E;
      h += '<p class="big">' + (anteil >= 1 ? 'Reicht: ' + f(Math.floor(anteil * 10) / 10) + '× deinen Bedarf' : 'Reicht nicht: nur ' + f(Math.round(anteil * 100)) + ' % deines Bedarfs') + '</p>';
    }
    var dauerAll = nutz / (P + ev);
    h += '<p>Laufen alle Geräte ununterbrochen gleichzeitig' + (ev ? ' (plus ' + f(ev) + ' W Eigenverbrauch)' : '') + ', hält der Akku etwa <strong>' + dauer(dauerAll) + '</strong>.</p>';
    if (ev && E > 0) h += '<p class="note">Der Eigenverbrauch fällt an, solange die Station eingeschaltet ist. Die Bedarfsrechnung oben enthält ihn nicht, weil die Einschaltzeit unbekannt ist.</p>';
    if (s.warn) h += '<p class="warnbox">' + esc(s.warn) + '</p>';
    // Alle Modelle im Überblick
    h += '<h3>So lange reichen die Modelle aus meinem Vergleich</h3><p class="note">Gleiche Geräte, gleiche Annahmen. ✗ = Dauerleistung zu klein für alle Geräte gleichzeitig.</p><div class="tablewrap"><table class="cmp"><thead><tr><th>Modell</th><th class="r">nutzbar (Annahme)</th><th class="r">Anteil deines Bedarfs</th><th class="r">Dauerbetrieb</th></tr></thead><tbody>';
    daten.forEach(function (p) {
      var nz = p.wh * eta;
      h += '<tr><td><a href="' + esc(p.url) + '">' + esc(p.m) + '</a></td><td class="r">' + f(Math.round(nz)) + ' Wh</td><td class="r">' + (E > 0 ? f(Math.round(nz / E * 100)) + ' %' : '–') + '</td><td class="r">' + (P > p.w ? '✗ ' : '') + dauer(nz / (P + ev)) + '</td></tr>';
    });
    h += '</tbody></table></div>';
    out.innerHTML = h;
  }
  form.addEventListener('input', rechne);
  form.addEventListener('change', rechne);
  form.addEventListener('submit', function (e) { e.preventDefault(); });
  var m = new URLSearchParams(location.search).get('m');
  if (m && daten.some(function (p) { return p.s === m; })) sel.value = m;
  zeile('', '', '', 1); zeile('', '', '', 1);
  rechne();
})();
