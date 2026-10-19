(function () {
  'use strict';
  function num(v) { var n = parseFloat(String(v).replace(',', '.')); return isNaN(n) ? null : n; }

  // Filter
  document.querySelectorAll('form.filters').forEach(function (form) {
    var table = document.getElementById(form.dataset.table);
    if (!table) return;
    form.hidden = false;
    var rows = Array.prototype.slice.call(table.tBodies[0].rows);
    var count = document.createElement('p');
    count.className = 'count';
    count.setAttribute('aria-live', 'polite');
    table.parentNode.after(count);
    function apply() {
      var shown = 0;
      rows.forEach(function (tr) {
        var ok = true;
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
      count.textContent = shown + ' von ' + rows.length + ' Modellen angezeigt';
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
