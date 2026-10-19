// Balkonstrom-Ratgeber – kleine Bedienschicht (eigenes Skript, keine externen Quellen, kein Tracking).
// 1) Kopfleiste nimmt die Farbe des Abschnitts darunter an (data-field: paper | field | surface).
// 2) Abschnitte erscheinen gestaffelt (nur ohne „Bewegung reduzieren“; ohne JS ist alles sofort sichtbar).
// 3) Laufzeit-Beleg auf der Startseite: Gerät wählen → gleiche Formel wie der Laufzeitrechner (Wh × 85 % / W).
(function () {
  var d = document, root = d.documentElement;
  root.classList.add('ui'); // „mo“ setzt schon das Inline-Skript im <head> (vor dem ersten Bild, kein Flackern)

  d.addEventListener('DOMContentLoaded', function () {
    // 1) Kopf-Farbe nach Abschnitt
    var head = d.querySelector('.site-header');
    var fields = d.querySelectorAll('[data-field]');
    if (head && fields.length && 'IntersectionObserver' in window) {
      var setField = function () {
        var y = head.getBoundingClientRect().bottom - 1, cur = 'paper';
        for (var i = 0; i < fields.length; i++) {
          var r = fields[i].getBoundingClientRect();
          if (r.top <= y && r.bottom > y) cur = fields[i].getAttribute('data-field');
        }
        if (head.getAttribute('data-unter') !== cur) head.setAttribute('data-unter', cur);
      };
      var tick = false;
      window.addEventListener('scroll', function () { if (!tick) { tick = true; requestAnimationFrame(function () { tick = false; setField(); }); } }, { passive: true });
      window.addEventListener('resize', setField);
      setField();
    }

    // 2) Gestaffelte Einblendung – Startseite markiert selbst, sonst die üblichen Bausteine
    if (root.classList.contains('mo')) {
      var auto = '.post-body > h2, .post-body > figure, .post-body > .pcards > li, .post-foto, .kurzantwort, .empfbox .empf, .weiter-grid > a, .weiterlesen .card, .cards > li, .plist > li, .tool-tiles > li, .schritte li, .einsatz-sec, .einsatz-foto, .p-top > *, .p-fazit, .p-fuer > *, .p-sw > *, .faq-gruppe, .footer-grid > *, .vergleich .tabpanel > *, .p-test, .p-quellen, .p-wider, .p-alt li';
      Array.prototype.forEach.call(d.querySelectorAll(auto), function (el) { if (!el.closest('[data-r]') && !el.querySelector('[data-r]') && el.getBoundingClientRect().top > window.innerHeight) el.setAttribute('data-r', ''); });
      var els = d.querySelectorAll('[data-r]');
      var io = new IntersectionObserver(function (es) {
        es.forEach(function (e) {
          if (!e.isIntersecting) return;
          var el = e.target, sib = el.parentNode ? el.parentNode.querySelectorAll(':scope > [data-r]') : [];
          var idx = Array.prototype.indexOf.call(sib, el);
          el.style.setProperty('--d', Math.max(0, idx) * 80 + 'ms');
          el.classList.add('is-in');
          io.unobserve(el);
        });
      }, { rootMargin: '0px 0px -8% 0px', threshold: 0.08 });
      Array.prototype.forEach.call(els, function (el) { io.observe(el); });
    }

    // 3) Laufzeit-Beleg
    var wahl = d.querySelector('.slip-wahl'), slip = d.querySelector('.slip');
    if (wahl && slip) {
      wahl.hidden = false;
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
