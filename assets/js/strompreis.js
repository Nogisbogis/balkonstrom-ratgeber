// Börsenstrompreis DE-LU (Day-Ahead): lädt nur /api/strompreis.json von dieser Domain.
// Kein Aufruf fremder Server, kein Tracking. Werte kommen ausschließlich aus dem Feed (energy-charts / SMARD).
(function () {
  var boxes = document.querySelectorAll('[data-strompreis]');
  if (!boxes.length) return;
  var src = boxes[0].getAttribute('data-strompreis');
  var ct = new Intl.NumberFormat('de-DE', { minimumFractionDigits: 1, maximumFractionDigits: 1 });
  var hm = new Intl.DateTimeFormat('de-DE', { hour: '2-digit', minute: '2-digit', timeZone: 'Europe/Berlin' });
  var dayKey = new Intl.DateTimeFormat('en-CA', { year: 'numeric', month: '2-digit', day: '2-digit', timeZone: 'Europe/Berlin' });
  function mean(d, start) {
    var s = 0, n = 0;
    for (var i = 0; i < d.unix_seconds.length; i++) {
      var t = d.unix_seconds[i], p = d.price[i];
      if (t >= start && t < start + 3600 && typeof p === 'number' && isFinite(p)) { s += p; n++; }
    }
    return n ? s / n : null;
  }
  function fmt(eurMwh) { return ct.format(eurMwh / 10).replace('-0,0', '0,0'); }
  function auswerten(d) {
    if (!d || !d.available || d.unit !== 'EUR / MWh' || !d.unix_seconds || !d.price) return null;
    var now = Math.floor(Date.now() / 1000), h = now - now % 3600;
    var cur = mean(d, h);
    if (cur === null) return null; // Feed veraltet oder Stunde fehlt: nichts anzeigen statt raten
    var heute = dayKey.format(new Date()), min = null, max = null;
    for (var i = 0; i < d.unix_seconds.length; i++) {
      var p = d.price[i];
      if (typeof p !== 'number' || dayKey.format(new Date(d.unix_seconds[i] * 1000)) !== heute) continue;
      if (min === null || p < min.p) min = { p: p, t: d.unix_seconds[i] };
      if (max === null || p > max.p) max = { p: p, t: d.unix_seconds[i] };
    }
    return { h: h, cur: cur, next: mean(d, h + 3600), min: min, max: max, asOf: d.as_of_unix };
  }
  function zeigen(r) {
    boxes.forEach(function (box) {
      var v = box.querySelector('.sp-wert'), m = box.querySelector('.sp-meta');
      box.classList.remove('sp-laedt');
      if (!r) {
        box.classList.add('sp-leer');
        v.textContent = 'gerade nicht verfügbar';
        m.textContent = 'Der Börsenpreis lässt sich im Moment nicht laden.';
        return;
      }
      box.classList.remove('sp-leer');
      v.innerHTML = '<b>' + fmt(r.cur) + '</b> ct/kWh <span class="sp-zeit">' + hm.format(new Date(r.h * 1000)) + '–' + hm.format(new Date((r.h + 3600) * 1000)) + ' Uhr, Stundenmittel</span>';
      var t = [];
      if (r.next !== null) t.push('nächste Stunde ' + fmt(r.next) + ' ct');
      if (r.min && r.max) t.push('heute ' + fmt(r.min.p) + ' ct (' + hm.format(new Date(r.min.t * 1000)) + ') bis ' + fmt(r.max.p) + ' ct (' + hm.format(new Date(r.max.t * 1000)) + ')');
      if (r.asOf) t.push('abgerufen ' + hm.format(new Date(r.asOf * 1000)) + ' Uhr');
      m.textContent = t.join(' · ');
    });
    document.dispatchEvent(new CustomEvent('strompreis', { detail: r }));
  }
  function laden() {
    fetch(src, { cache: 'no-cache', credentials: 'omit' })
      .then(function (res) { if (!res.ok) throw new Error(res.status); return res.json(); })
      .then(function (d) { zeigen(auswerten(d)); })
      .catch(function () { zeigen(null); });
  }
  laden();
  setInterval(laden, 15 * 60 * 1000);
})();
