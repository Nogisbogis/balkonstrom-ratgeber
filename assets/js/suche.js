// Powerstation-Suche: filtert die serverseitig gerenderte Liste, Zustand in der URL (teilbar). Kein Tracking.
(function () {
  var form = document.getElementById('suche'), liste = document.getElementById('s-liste');
  if (!form || !liste) return;
  var items = Array.prototype.slice.call(liste.children);
  var count = document.getElementById('s-count'), leer = document.getElementById('s-leer');
  var gesamt = items.length;
  var ZAHL = ['whmin', 'whmax', 'w', 'kg', 'pv'], WAHL = ['q', 'marke', 'akku', 'zyk', 'sort'], HAKEN = ['ac', 'usv', 'usv10', 'erw'];
  function num(el, k) { var v = el.getAttribute('data-' + k); return v === '' || v === null ? null : parseFloat(v); }
  function wert(n) { var e = form.elements[n]; if (!e) return ''; return e.type === 'checkbox' ? (e.checked ? '1' : '') : String(e.value).trim(); }
  // URL -> Formular (nur bekannte Felder, Zahlen geprüft)
  var qs = new URLSearchParams(location.search);
  ZAHL.forEach(function (n) { var x = parseFloat((qs.get(n) || '').replace(',', '.')); if (isFinite(x) && x >= 0 && x < 100000) form.elements[n].value = x; });
  WAHL.forEach(function (n) {
    var v = qs.get(n); if (v === null) return; var e = form.elements[n];
    if (e.tagName === 'SELECT') { if (Array.prototype.some.call(e.options, function (o) { return o.value === v; })) e.value = v; }
    else e.value = v.slice(0, 60);
  });
  HAKEN.forEach(function (n) { if (qs.get(n) === '1') form.elements[n].checked = true; });
  form.hidden = false;

  function passt(el) {
    var q = wert('q').toLowerCase(), f;
    if (q && el.getAttribute('data-name').indexOf(q) < 0) return false;
    if (wert('marke') && el.getAttribute('data-marke') !== wert('marke')) return false;
    if (wert('akku') && el.getAttribute('data-akku') !== wert('akku')) return false;
    // Zahl-Filter: fehlender Wert (keine Angabe) fällt nur heraus, wenn der Filter aktiv ist
    var regeln = [['whmin', 'wh', 1], ['whmax', 'wh', -1], ['w', 'w', 1], ['kg', 'kg', -1], ['pv', 'pv', 1], ['zyk', 'zyk', 1]];
    for (var i = 0; i < regeln.length; i++) {
      f = parseFloat(wert(regeln[i][0])); if (!isFinite(f)) continue;
      var v = num(el, regeln[i][1]); if (v === null) return false;
      if (regeln[i][2] > 0 ? v < f : v > f) return false;
    }
    if (wert('ac') && el.getAttribute('data-ac') !== '1') return false;
    var usv = num(el, 'usv');
    if (wert('usv') && !(usv > 0)) return false;
    if (wert('usv10') && !(usv > 0 && usv <= 10)) return false;
    if (wert('erw') && el.getAttribute('data-erw') !== '1') return false;
    return true;
  }
  function sortiere() {
    var s = wert('sort') || 'wh', ab = s.charAt(0) === '-', k = ab ? s.slice(1) : s;
    items.sort(function (a, b) {
      if (k === 'name') return a.getAttribute('data-name').localeCompare(b.getAttribute('data-name'), 'de');
      var x = num(a, k), y = num(b, k);
      if (x === null && y === null) return 0; if (x === null) return 1; if (y === null) return -1;
      return ab ? y - x : x - y;
    });
    items.forEach(function (el) { liste.appendChild(el); });
  }
  function url() {
    var p = new URLSearchParams();
    ZAHL.concat(WAHL, HAKEN).forEach(function (n) { var v = wert(n); if (v && !(n === 'sort' && v === 'wh')) p.set(n, v); });
    var s = p.toString();
    history.replaceState(null, '', location.pathname + (s ? '?' + s : '') + location.hash);
  }
  function lauf() {
    sortiere();
    var n = 0;
    items.forEach(function (el) { var ok = passt(el); el.hidden = !ok; if (ok) n++; });
    count.textContent = n + ' von ' + gesamt + ' Modellen';
    leer.hidden = n > 0;
    url();
  }
  var t;
  form.addEventListener('input', function () { clearTimeout(t); t = setTimeout(lauf, 120); });
  form.addEventListener('change', lauf);
  form.addEventListener('submit', function (e) { e.preventDefault(); lauf(); });
  form.addEventListener('reset', function () { setTimeout(lauf, 0); });
  leer.querySelector('button').addEventListener('click', function () { form.reset(); form.elements.q.focus(); });
  lauf();
})();
