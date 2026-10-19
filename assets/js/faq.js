// FAQ-Filter: blendet Fragen aus, die den Suchtext nicht enthalten. Nichts wird gespeichert.
(function () {
  var box = document.querySelector('.faq-filter');
  var input = document.getElementById('faq-suche');
  if (!box || !input) return;
  box.hidden = false;
  var items = Array.prototype.slice.call(document.querySelectorAll('.faq-gruppe details'));
  var gruppen = Array.prototype.slice.call(document.querySelectorAll('.faq-gruppe'));
  var zahl = document.getElementById('faq-zahl'), leer = document.getElementById('faq-leer');
  function norm(s) { return s.toLowerCase().normalize('NFD').replace(/[\u0300-\u036f]/g, ''); }
  var texte = items.map(function (d) { return norm(d.textContent); });
  function filter() {
    var w = norm(input.value.trim()).split(/\s+/).filter(Boolean), n = 0;
    items.forEach(function (d, i) {
      var ok = w.every(function (x) { return texte[i].indexOf(x) >= 0; });
      d.hidden = !ok; if (ok) n++;
      if (w.length && ok && w.join('').length > 2) d.open = true;
      if (!w.length) d.open = false;
    });
    gruppen.forEach(function (g) { g.hidden = !g.querySelector('details:not([hidden])'); });
    zahl.textContent = w.length ? n + (n === 1 ? ' Frage passt' : ' Fragen passen') : items.length + ' Fragen';
    leer.hidden = n > 0;
  }
  input.addEventListener('input', filter);
  filter();
})();
