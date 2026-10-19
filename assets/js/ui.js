// Balkonstrom-Ratgeber – kleine Bedienschicht (eigenes Skript, keine externen Quellen, kein Tracking).
// Laufzeit-Beleg auf der Startseite: Gerät wählen → gleiche Formel wie der Laufzeitrechner (Wh × 85 % / W).
// Keine Einblende-Animationen und kein Farbwechsel der Kopfleiste mehr (Okt. 2026: Seite soll beim Laden ruhig stehen).
(function () {
  var d = document;
  d.addEventListener('DOMContentLoaded', function () {
    // 3) Laufzeit-Beleg
    var wahl = d.querySelector('.slip-wahl'), slip = d.querySelector('.slip');
    if (wahl && slip) {
      var wh = parseFloat(slip.getAttribute('data-wh')), eta = parseFloat(slip.getAttribute('data-eta'));
      var link = d.querySelector('[data-slip-link]');
      wahl.addEventListener('click', function (ev) {
        var b = ev.target.closest('button[data-k]'); if (!b) return;
        var w = parseFloat(b.getAttribute('data-w')), h = wh * eta / w;
        var hh = Math.floor(h), mm = Math.round((h - hh) * 60); if (mm === 60) { hh += 1; mm = 0; }
        Array.prototype.forEach.call(wahl.querySelectorAll('button'), function (x) { x.setAttribute('aria-pressed', x === b ? 'true' : 'false'); });
        slip.querySelector('[data-slip-name]').textContent = b.getAttribute('data-n') + ' (typischer Wert, ' + b.getAttribute('data-q') + ')';
        slip.querySelector('[data-slip-w]').textContent = new Intl.NumberFormat('de-DE').format(w) + ' W';
        slip.querySelector('[data-slip-erg]').textContent = '≈ ' + hh + ' h ' + mm + ' min';
        if (link) link.setAttribute('href', link.getAttribute('href').replace(/g=[^&]*/, 'g=' + encodeURIComponent(b.getAttribute('data-k'))));
        slip.classList.remove('neu'); void slip.offsetWidth; slip.classList.add('neu');
      });
    }
  });
})();
// Sprungziele in zugeklappten Abschnitten (z. B. Quellenverweis #q-…): umgebende <details> öffnen.
// Ohne JS bleibt alles zugänglich, nur eben zugeklappt.
(function () {
  function auf() {
    var id = decodeURIComponent(location.hash.slice(1)), el = id && document.getElementById(id);
    for (var p = el; p; p = p.parentElement) if (p.tagName === 'DETAILS') p.open = true;
    if (el && el.closest('details')) el.scrollIntoView();
  }
  window.addEventListener('hashchange', auf);
  document.addEventListener('DOMContentLoaded', function () { if (location.hash) auf(); });
})();
