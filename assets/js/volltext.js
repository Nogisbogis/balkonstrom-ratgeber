// Volltextsuche (Pagefind, lokal im Browser, kein Tracking). ?q= füllt das Suchfeld vor.
(function () {
  function start() {
    var el = document.getElementById('volltext');
    if (!el || typeof PagefindUI === 'undefined') return;
    var ui = new PagefindUI({ element: '#volltext', bundlePath: el.getAttribute('data-bundle'), showImages: false, showSubResults: true, resetStyles: false, autofocus: true });
    var q = new URLSearchParams(location.search).get('q');
    if (q) ui.triggerSearch(q);
    // Pagefind setzt nur title am Suchfeld – echtes Label für Screenreader ergänzen.
    var n = 0, t = setInterval(function () {
      var i = el.querySelector('input');
      if (i) { i.setAttribute('aria-label', 'Website durchsuchen'); clearInterval(t); }
      else if (++n > 50) clearInterval(t);
    }, 100);
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', start); else start();
})();
