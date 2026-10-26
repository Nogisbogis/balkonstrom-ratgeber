#!/usr/bin/env python3
"""Fixtures für die Amazon-Einstufung: normale Produktseite, Rumpfseite, Captcha.

Die Fixtures sind kurze HTML-Schnipsel (keine Seitendumps). signale_aus_html liest dieselben
Anker, die das Browser-JS abfragt, und gibt das Dict, das einstufen erwartet.
"""
import inspect, os, re, unittest

import verfuegbarkeit as vk

FIX = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'fixtures', 'verfuegbarkeit')


def signale_aus_html(html):
    """Grobe Entsprechung des Browser-JS für die Fixture-Schnipsel."""
    def has(id_):
        return f'id="{id_}"' in html

    def text(id_):
        m = re.search(r'id="' + re.escape(id_) + r'"[^>]*>(.*?)</', html, re.S)
        if not m:
            return ''
        raw = re.sub(r'<[^>]+>', ' ', m.group(1))
        return re.sub(r'\s+', ' ', raw).strip()

    titel = text('productTitle') or text('title')
    if not titel and 'product-title-word-break' in html:
        m = re.search(r'class="[^"]*product-title-word-break[^"]*"[^>]*>(.*?)</', html, re.S)
        if m:
            titel = re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', m.group(1))).strip()
    avail = (text('availability') or text('outOfStock'))[:160]
    body = re.sub(r'<[^>]+>', ' ', html)
    body = re.sub(r'\s+', ' ', body)
    captcha = ('validateCaptcha' in html) or bool(re.search(
        r'Geben Sie die Zeichen|Zeichen unten ein|Klicke auf die Schaltfläche unten, um mit dem Einkauf fortzufahren',
        body))
    dog = bool(re.search(r'Seite nicht gefunden|Page Not Found|konnten wir die gesuchte Seite nicht finden', html))
    produkt = has('ppd') or has('centerCol') or has('desktop_buybox') or has('outOfStock') or has('productTitle')
    cart = has('add-to-cart-button') or 'name="submit.add-to-cart"' in html
    return {
        'doctitle': (re.search(r'<title>(.*?)</title>', html, re.S).group(1) if '<title>' in html else ''),
        'title': titel,
        'avail': avail,
        'oos': has('outOfStock'),
        'cart': cart,
        'buynow': has('buy-now-button'),
        'choices': text('buybox-see-all-buying-choices')[:160],
        'aod': '',
        'used': '',
        'captcha': captcha,
        'dog': dog,
        'asin': 'B0EXAMPLE1' if has('ASIN') else '',
        'canon': '',
        'url': 'https://www.amazon.de/dp/B0EXAMPLE1',
        'rs': 'complete',
        'ppd': produkt,
        'http': [200],
        'laenge': len(html),
    }


class TestFixtures(unittest.TestCase):
    def _html(self, name):
        with open(os.path.join(FIX, name), encoding='utf-8') as f:
            return f.read()

    def test_normale_seite_verfuegbar(self):
        st, warum = vk.einstufen('B0EXAMPLE1', '', signale_aus_html(self._html('produkt-verfuegbar.html')))
        self.assertEqual(st, 'verfuegbar', warum)

    def test_normale_seite_nicht_verfuegbar(self):
        st, warum = vk.einstufen('B0EXAMPLE1', '', signale_aus_html(self._html('produkt-nicht-verfuegbar.html')))
        self.assertEqual(st, 'nicht_verfuegbar', warum)
        self.assertFalse(vk.sperrseite(st, warum))

    def test_rumpfseite_bleibt_unklar(self):
        html = self._html('rumpfseite.html')
        self.assertNotIn('id="productTitle"', html)
        self.assertNotIn('id="ppd"', html)
        v = signale_aus_html(html)
        self.assertFalse(v['ppd'])
        self.assertFalse(v['title'])
        self.assertIn('Anker SOLIX', v['doctitle'])
        st, warum = vk.einstufen('B0EXAMPLE1', '', v)
        self.assertEqual(st, 'unklar', warum)
        self.assertTrue(warum.startswith('Amazon lieferte die Seite ohne Produktbereich'), warum)
        self.assertTrue(vk.sperrseite(st, warum))

    def test_captcha_bleibt_unklar(self):
        st, warum = vk.einstufen('B0EXAMPLE1', '', signale_aus_html(self._html('captcha.html')))
        self.assertEqual(st, 'unklar', warum)
        self.assertTrue(vk.sperrseite(st, warum))


class TestEinstufen(unittest.TestCase):
    def test_kaufbox(self):
        st, _ = vk.einstufen('B0TEST12345', '', {'title': 'X', 'ppd': True, 'cart': True, 'http': [200], 'rs': 'complete'})
        self.assertEqual(st, 'verfuegbar')

    def test_neu_angebot_ohne_kaufbox(self):
        st, _ = vk.einstufen('B0TEST12345', '', {
            'title': 'X', 'ppd': True, 'choices': 'Alle Angebote', 'angebote': ['Neu'], 'http': [200], 'rs': 'complete'})
        self.assertEqual(st, 'verfuegbar')

    def test_nur_gebraucht(self):
        st, _ = vk.einstufen('B0TEST12345', '', {'title': 'X', 'ppd': True, 'used': 'Gebraucht – wie neu', 'http': [200]})
        self.assertEqual(st, 'nicht_verfuegbar')

    def test_kaufoptionen_ohne_neu_bleibt_unklar(self):
        st, warum = vk.einstufen('B0TEST12345', '', {
            'title': 'X', 'ppd': True, 'choices': 'Alle Kaufoptionen anzeigen', 'http': [200], 'rs': 'complete'})
        self.assertEqual(st, 'unklar', warum)
        self.assertFalse(vk.sperrseite(st, warum))

    def test_hundeseite(self):
        st, _ = vk.einstufen('B0TEST12345', '', {'dog': True, 'title': '', 'http': [404]})
        self.assertEqual(st, 'ungueltig')

    def test_titel_passt_nicht(self):
        st, warum = vk.einstufen('B0TEST12345', 'Anker SOLIX RS40P', {
            'title': 'Ganz andere Marke ohne die Wörter', 'ppd': True, 'cart': True, 'http': [200],
            'canon': 'https://www.amazon.de/dp/B0OTHER123', 'url': ''})
        self.assertEqual(st, 'ungueltig', warum)

    def test_fallback_titel_mit_kaufbox_nicht_rumpf(self):
        """Produktseite ohne das alte #ppd-Flag, aber mit Titel und Kaufbox, ist verfügbar."""
        st, warum = vk.einstufen('B0TEST12345', '', {
            'title': 'Anker SOLIX Beispiel', 'ppd': True, 'cart': True, 'http': [200], 'rs': 'complete',
            'doctitle': 'Anker SOLIX Beispiel : Amazon.de', 'laenge': 900000})
        self.assertEqual(st, 'verfuegbar', warum)
        self.assertFalse(vk.sperrseite(st, warum))


class TestSitzung(unittest.TestCase):
    def test_lade_verwirft_sitzungscookies(self):
        """Ohne diesen Schritt liefert die zweite ASIN nur die Rumpfseite."""
        self.assertIn('sitzung_leeren', inspect.getsource(vk.Browser.lade))
        self.assertIn('clearBrowserCookies', inspect.getsource(vk.Browser.sitzung_leeren))

    def test_js_fallbacks(self):
        """Mehrere Anker, nicht nur #productTitle/#ppd. Die Rumpfseite hat #dp, aber keine davon."""
        for nadel in ('#productTitle', 'product-title-word-break', 'h1#title', '#centerCol',
                      '#desktop_buybox', 'submit.add-to-cart', '#outOfStock'):
            self.assertIn(nadel, vk.JS, nadel)
        self.assertIn('#centerCol', vk.BEREIT_JS)


if __name__ == '__main__':
    unittest.main()
