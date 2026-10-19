// Auswahl per Link: /vergleich/?m=slug1,slug2 – nur in der URL, keine Cookies, kein localStorage
var AUSWAHL = (function () {
  var m = new URLSearchParams(location.search).get('m');
  if (!m) return [];
  var alle = Array.prototype.map.call(document.querySelectorAll('table.cmp tbody tr[data-slug]'), function (tr) { return tr.dataset.slug; });
  return m.split(',').map(function (x) { return x.trim(); }).filter(function (x, i, a) { return x && alle.indexOf(x) >= 0 && a.indexOf(x) === i; });
})();
(function () {
  var box = document.getElementById('auswahl-hinweis');
  if (!box || !AUSWAHL.length) return;
  var namen = AUSWAHL.map(function (s) { var tr = document.querySelector('tr[data-slug="' + s + '"] .mname'); return tr ? tr.textContent.trim() : s; });
  box.innerHTML = '<p><strong>Deine Auswahl: ' + AUSWAHL.length + (AUSWAHL.length === 1 ? ' Modell' : ' Modelle') + '</strong> – ' + namen.map(function (n) { return n.replace(/[&<>"]/g, ''); }).join(', ') + '</p><p><a class="textlink" href="' + location.pathname + '">Alle Modelle anzeigen</a></p><p class="note">Die Auswahl steht nur in der Adresse dieser Seite – du kannst sie teilen. Nichts wird gespeichert.</p>';
  box.hidden = false;
})();
(function () {
  'use strict';
  function num(v) { var n = parseFloat(String(v).replace(',', '.')); return isNaN(n) ? null : n; }

  // Filter
  document.querySelectorAll('form.filters').forEach(function (form) {
    var table = document.getElementById(form.dataset.table);
    if (!table) return;
    form.hidden = false;
    var rows = Array.prototype.slice.call(table.tBodies[0].rows);
    var count = form.querySelector('.count'); // im HTML vorhanden (kein Layoutsprung beim Laden)
    if (!count) { count = document.createElement('p'); count.className = 'count'; count.setAttribute('aria-live', 'polite'); (form.querySelector('fieldset') || form).appendChild(count); }
    function apply() {
      var shown = 0;
      rows.forEach(function (tr) {
        var ok = !AUSWAHL.length || AUSWAHL.indexOf(tr.dataset.slug) >= 0;
        form.querySelectorAll('[data-filter]').forEach(function (el) {
          var val = el.value.trim();
          if (!val) return;
          var cell = tr.dataset[el.dataset.filter];
          if (el.dataset.op === 'eq') { if (cell !== val) ok = false; return; }
          var a = num(cell), b = num(val);
          if (b === null) return;
          if (el.dataset.op === 'min' && !(a !== null && a >= b)) ok = false;
          if (el.dataset.op === 'max' && !(a !== null && a <= b)) ok = false;
        });
        tr.hidden = !ok;
        if (ok) shown++;
      });
      count.textContent = shown + ' von ' + rows.length + ' Modellen angezeigt' + (AUSWAHL.length ? ' (deine Auswahl)' : '');
    }
    form.addEventListener('input', apply);
    form.addEventListener('change', apply);
    form.addEventListener('reset', function () { setTimeout(apply, 0); });
    form.addEventListener('submit', function (e) { e.preventDefault(); });
    apply();
  });

  // Sortierung
  document.querySelectorAll('table.cmp').forEach(function (table) {
    var ths = table.tHead.rows[0].cells;
    Array.prototype.forEach.call(ths, function (th, idx) {
      var type = th.dataset.sort;
      if (!type) return;
      var btn = document.createElement('button');
      btn.type = 'button';
      btn.className = 'sort';
      btn.innerHTML = th.innerHTML;
      th.innerHTML = '';
      th.appendChild(btn);
      th.setAttribute('aria-sort', 'none');
      btn.addEventListener('click', function () {
        var dir = th.getAttribute('aria-sort') === 'ascending' ? -1 : 1;
        Array.prototype.forEach.call(ths, function (o) { if (o.dataset.sort) o.setAttribute('aria-sort', 'none'); });
        th.setAttribute('aria-sort', dir === 1 ? 'ascending' : 'descending');
        var body = table.tBodies[0];
        var rows = Array.prototype.slice.call(body.rows);
        rows.sort(function (a, b) {
          var ca = a.cells[idx], cb = b.cells[idx];
          if (type === 'num') {
            return dir * ((num(ca.dataset.v) || 0) - (num(cb.dataset.v) || 0));
          }
          return dir * ca.textContent.trim().localeCompare(cb.textContent.trim(), 'de');
        });
        rows.forEach(function (r) { body.appendChild(r); });
      });
    });
  });
})();

// Tabs Powerstations / Balkonkraftwerke (ohne JS: Sprunglinks, beide Tabellen sichtbar)
(function () {
  'use strict';
  var nav = document.querySelector('nav.tabs');
  if (!nav) return;
  var links = Array.prototype.slice.call(nav.querySelectorAll('a[data-tab]'));
  var panels = links.map(function (a) { return document.getElementById(a.dataset.tab); });
  var mitAuswahl = panels.filter(function (p) { return AUSWAHL.some(function (s) { return p.querySelector('tr[data-slug="' + s + '"]'); }); });
  if (mitAuswahl.length > 1) { document.documentElement.classList.add('js-tabs-aus'); return; } // Auswahl aus beiden Kategorien: beide Tabellen untereinander zeigen
  nav.setAttribute('role', 'tablist');
  links.forEach(function (a, i) {
    a.setAttribute('role', 'tab');
    a.setAttribute('aria-controls', a.dataset.tab);
    panels[i].setAttribute('role', 'tabpanel');
  });
  function show(id, focus) {
    var found = links.some(function (a) { return a.dataset.tab === id; });
    if (!found) id = links[0].dataset.tab;
    links.forEach(function (a, i) {
      var on = a.dataset.tab === id;
      a.setAttribute('aria-selected', on ? 'true' : 'false');
      a.tabIndex = on ? 0 : -1;
      panels[i].hidden = !on;
      if (on && focus) a.focus();
    });
  }
  links.forEach(function (a, i) {
    a.addEventListener('click', function (e) {
      e.preventDefault();
      history.replaceState(null, '', '#' + a.dataset.tab);
      show(a.dataset.tab);
    });
    a.addEventListener('keydown', function (e) {
      var d = e.key === 'ArrowRight' ? 1 : e.key === 'ArrowLeft' ? -1 : 0;
      if (!d) return;
      e.preventDefault();
      var n = links[(i + d + links.length) % links.length];
      history.replaceState(null, '', '#' + n.dataset.tab);
      show(n.dataset.tab, true);
    });
  });
  window.addEventListener('hashchange', function () { show(location.hash.slice(1)); });
  document.documentElement.classList.add('js-tabs');
  show(location.hash.slice(1) || (mitAuswahl[0] && mitAuswahl[0].id) || '');
})();
