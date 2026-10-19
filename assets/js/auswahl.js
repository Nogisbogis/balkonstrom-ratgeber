// Empfehlungen vergleichen: Häkchen setzen, ab 2 Modellen erscheint ein Link zur Vergleichstabelle.
// Die Auswahl steht nur im Link (?m=…) – keine Cookies, kein localStorage.
(function () {
  var boxes = document.querySelectorAll('.cmp-check input[type=checkbox]');
  if (!boxes.length) return;
  var bar = document.getElementById('cmp-bar');
  var link = bar.querySelector('a');
  var seen = [];
  Array.prototype.forEach.call(boxes, function (b) { b.parentNode.hidden = false; });
  function update() {
    var sel = [];
    Array.prototype.forEach.call(boxes, function (b) { if (b.checked && sel.indexOf(b.value) < 0) sel.push(b.value); });
    bar.hidden = sel.length < 2;
    link.href = link.dataset.base + '?m=' + sel.map(encodeURIComponent).join(',');
    link.textContent = sel.length + ' Modelle nebeneinander ansehen';
    document.body.classList.toggle('mit-cmp-bar', sel.length >= 2);
  }
  Array.prototype.forEach.call(boxes, function (b) {
    b.addEventListener('change', function () {
      Array.prototype.forEach.call(boxes, function (o) { if (o.value === b.value) o.checked = b.checked; });
      update();
    });
  });
  update();
})();
