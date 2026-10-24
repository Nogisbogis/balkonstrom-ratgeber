#!/usr/bin/env python3
"""Verfügbarkeits-Check für alle Amazon-ASINs der Website.

Sammelt jede ASIN (data/*.yaml, Shortcodes und amazon.de-URLs in content/ und layouts/), ruft
ausschließlich die UNGETAGGTE Produktseite https://www.amazon.de/dp/<ASIN> auf und ordnet zu:

  verfuegbar        Kaufbox („In den Einkaufswagen“/„Jetzt kaufen“) vorhanden, ODER keine Kaufbox,
                    aber „Alle Angebote“ (wird aufgeklappt) enthält mindestens ein NEU-Angebot.
  nicht_verfuegbar  „Derzeit nicht verfügbar“ bzw. keine Kaufbox und kein Neu-Angebot
                    (nur Gebraucht/B-Ware zählt als nicht verfügbar).
  ungueltig         HTTP 404/„Seite nicht gefunden“ (Hundeseite), Weiterleitung auf eine andere
                    Produktseite, deren Titel nicht zu unserem Modell passt, oder Titel passt nicht.
  unklar            Captcha, Sperre, Netzwerk-/Browserfehler, Seite ohne erkennbares Produkt.
                    „unklar“ ändert NIE den gespeicherten Status (letzter bekannter Stand bleibt).

Höflich: ein Abruf nach dem anderen, 6–11 s Pause, bis zu 3 Versuche mit wachsender Pause.
Abruf per Headless-Chrome (eigenes Profil mit Lieferort Berlin), realistische Header.

data/verfuegbarkeit.yaml wird nur geschrieben, wenn sich ein Status ändert (oder ASINs hinzukommen/
wegfallen). Ein Protokoll jedes Laufs landet außerhalb des Repos (~/.local/state/balkonstrom/).
Der Partner-Tag wird weder verwendet noch ausgegeben.

Aufruf:  python tools/verfuegbarkeit.py [--nur ASIN ...] [--trocken]
Exit-Code: 0 = ok (Datei ggf. geändert), 3 = zu viele „unklar“ (nichts geändert),
           8 = Abbruch „amazon blockt“ (die ersten ASINs alle unklar bzw. wiederholt Sperr-/Rumpfseiten;
               nichts geändert).

Robustheit: jede ASIN hat ein hartes Zeitbudget (ASIN_TIMEOUT, Standard 90 s, alle Versuche inkl.
Websocket-Wartezeiten zusammen, abgesichert per SIGALRM); bei Überschreitung -> unklar („timeout“).
Chrome läuft in einer eigenen Prozessgruppe und wird beim Beenden (auch bei SIGTERM) samt Kindprozessen beendet.
"""
import argparse, atexit, datetime as dt, glob, json, os, random, re, shutil, signal, socket, subprocess, sys, time, urllib.request
sys.dont_write_bytecode = True
import yaml, websocket

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATEI = os.path.join(ROOT, 'data', 'verfuegbarkeit.yaml')
STATE = os.path.expanduser('~/.local/state/balkonstrom')
PROFIL = os.environ.get('AMZ_PROFIL', os.path.expanduser('~/.local/share/balkonstrom/amz-profil'))
PROFIL_VORLAGE = '/workspace/amzcheck/chromeprof'   # Profil mit Lieferort 10115 Berlin
UA = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36'
UNKLAR_GRENZE = 0.30
ASIN_TIMEOUT = float(os.environ.get('VK_ASIN_TIMEOUT', 90))   # Sekunden je ASIN, alle Versuche zusammen
BLOCK_ANFANG = int(os.environ.get('VK_BLOCK_ANFANG', 5))       # so viele unklar direkt am Anfang -> Abbruch
BLOCK_SPERRSEITEN = int(os.environ.get('VK_BLOCK_SPERR', 3))   # so viele ASINs in Folge mit Sperr-/Rumpfseite -> Abbruch
EXIT_BLOCKT = 8


class ZeitLimit(Exception):
    """Zeitbudget einer ASIN aufgebraucht."""


def _alarm(signum, frame):
    raise ZeitLimit('timeout')
ASIN_RE = r'[A-Z0-9]{10}'


# ---------------------------------------------------------------- ASINs sammeln
def sammle():
    """-> {asin: {'name': Modellname oder '', 'fundorte': [...]}}"""
    res = {}
    def add(a, name, ort):
        e = res.setdefault(a, {'name': '', 'fundorte': []})
        if name and not e['name']:
            e['name'] = name
        if ort not in e['fundorte']:
            e['fundorte'].append(ort)
    for f in sorted(glob.glob(os.path.join(ROOT, 'data', '*.yaml'))):
        if f == DATEI:
            continue
        d = yaml.safe_load(open(f, encoding='utf-8'))
        if isinstance(d, list):
            for x in d:
                if isinstance(x, dict) and re.fullmatch(ASIN_RE, str(x.get('asin') or '')):
                    add(x['asin'], x.get('modell', ''), os.path.relpath(f, ROOT))
    pats = [r'asin\s*=\s*"(' + ASIN_RE + ')"', r'amazon\.de/(?:[^/\s"\')]+/)?(?:dp|gp/product)/(' + ASIN_RE + ')']
    for f in sorted(glob.glob(os.path.join(ROOT, 'content', '**', '*.md'), recursive=True) +
                    glob.glob(os.path.join(ROOT, 'layouts', '**', '*.html'), recursive=True)):
        t = open(f, encoding='utf-8').read()
        for p in pats:
            for m in re.finditer(p, t):
                if m.group(1) == 'B0XXXXXXXX':
                    continue
                add(m.group(1), '', os.path.relpath(f, ROOT))
    return res


# ---------------------------------------------------------------- Titelabgleich
UNTERSCHEIDER = {'max', 'pro', 'mini', 'plus', 'ultra', 'gen', 'dc', 'v2', 'v3', 'elite', 'air', 'lite', 'se'}
def woerter(s):
    s = s.lower().replace('×', ' ')
    s = re.sub(r'[^a-z0-9äöüß]+', ' ', s)
    return s.split()

def titel_passt(name, titel):
    """Alle markanten Wörter des Modellnamens müssen im Amazon-Titel stehen; außerdem darf der
    Titelanfang (bis zum ersten Komma) kein Unterscheidungswort (Max, Pro, Mini …) enthalten,
    das unser Modellname nicht hat. Klammerzusätze im Modellnamen werden ignoriert."""
    if not name or not titel:
        return True, ''
    kern = re.sub(r'\(.*?\)', ' ', name)
    nw = [w for w in woerter(kern) if w not in {'balkonkraftwerk'}]
    tw = set(woerter(titel))
    fehlt = [w for w in nw if w not in tw]
    if fehlt:
        return False, 'fehlt im Titel: ' + ' '.join(fehlt)
    kopf = set(woerter(titel.split(',')[0]))
    extra = sorted((kopf & UNTERSCHEIDER) - set(nw))
    if extra:
        return False, 'anderes Modell? Titel enthält: ' + ' '.join(extra)
    return True, ''


# ---------------------------------------------------------------- Browser
JS = r"""(()=>{const q=s=>{const e=document.querySelector(s);return e?e.innerText.replace(/\s+/g,' ').trim():''};
const vis=s=>{const e=document.querySelector(s);return !!(e&&e.offsetParent!==null)};
const body=(document.body?document.body.innerText:'').replace(/\s+/g,' ');
const asinIn=(document.querySelector('input#ASIN,input[name="ASIN"]')||{}).value||'';
const canon=(document.querySelector('link[rel=canonical]')||{}).href||'';
return {url:location.href,doctitle:document.title,title:q('#productTitle'),avail:q('#availability').slice(0,160),
 oos:!!document.querySelector('#outOfStock'),cart:vis('#add-to-cart-button'),buynow:vis('#buy-now-button'),
 choices:q('#buybox-see-all-buying-choices').slice(0,160),aod:q('#aod-ingress-link, #olp_feature_div, #olpLinkWidget_feature_div').slice(0,200),
 used:q('#usedBuySection, #usedAccordionRow, #buyBoxAccordion').slice(0,200),
 captcha:!!document.querySelector('form[action*="validateCaptcha"]')||/Geben Sie die Zeichen|Zeichen unten ein|Klicke auf die Schaltfläche unten, um mit dem Einkauf fortzufahren|Click the button below to continue shopping/i.test(body.slice(0,4000)),
 dog:/Seite nicht gefunden|Page Not Found|konnten wir die gesuchte Seite nicht finden|Suchen Sie bestimmte Informationen/i.test(document.title+' '+body.slice(0,3000)),
 asin:asinIn,canon:canon,ort:q('#glow-ingress-line2'),rs:document.readyState,ppd:!!document.querySelector('#ppd'),
 laenge:document.documentElement.outerHTML.length}})()"""

# fertig = Dokument vollständig geladen, oder Produktspalte samt Kaufbox-/Verfügbarkeitsteil da,
# oder eine Sonderseite (Captcha/404), die ohnehin keine Produktspalte hat.
BEREIT_JS = r"""(()=>{const d=document,has=s=>!!d.querySelector(s);
const prod=has('#productTitle')&&(has('#availability')||has('#add-to-cart-button')||has('#buy-now-button')||has('#outOfStock')||has('#buybox-see-all-buying-choices'));
return {fertig:!window.__vkAlt&&(d.readyState==='complete'||prod||has('form[action*="validateCaptcha"]')),rs:d.readyState}})()"""

class Browser:
    def __init__(self):
        if not os.path.isdir(PROFIL):
            os.makedirs(os.path.dirname(PROFIL), exist_ok=True)
            if os.path.isdir(PROFIL_VORLAGE):
                shutil.copytree(PROFIL_VORLAGE, PROFIL, ignore=shutil.ignore_patterns('Singleton*', '*.lock'))
            else:
                os.makedirs(PROFIL)
        for f in glob.glob(os.path.join(PROFIL, 'Singleton*')):
            try: os.remove(f)
            except OSError: pass
        s = socket.socket(); s.bind(('127.0.0.1', 0)); self.port = s.getsockname()[1]; s.close()
        self.frist = None   # Zeitpunkt (time.time()), bis zu dem die aktuelle ASIN fertig sein muss
        self.p = subprocess.Popen(['google-chrome', '--headless=new', '--no-sandbox', '--disable-gpu',
                                   f'--remote-debugging-port={self.port}', '--user-data-dir=' + PROFIL,
                                   '--lang=de-DE', '--window-size=1366,900', 'about:blank'],
                                  stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
                                  start_new_session=True)   # eigene Prozessgruppe -> samt Renderern beendbar
        atexit.register(self.zu)
        for _ in range(40):
            try:
                tabs = json.load(urllib.request.urlopen(f'http://127.0.0.1:{self.port}/json', timeout=2)); break
            except Exception:
                time.sleep(0.5)
        else:
            raise RuntimeError('Chrome startet nicht')
        tab = [t for t in tabs if t['type'] == 'page'][0]
        self.ws = websocket.create_connection(tab['webSocketDebuggerUrl'], suppress_origin=True, timeout=60)
        self.i = 0; self.status = {}
        self.cmd('Network.enable'); self.cmd('Page.enable')
        self.cmd('Network.setUserAgentOverride', userAgent=UA, acceptLanguage='de-DE,de;q=0.9')
        # nur der HTTP-Status des Hauptdokuments zählt (nicht der von Werbe-/Hilfs-iframes)
        self.hauptframe = self.cmd('Page.getFrameTree')['result']['frameTree']['frame']['id']

    def _merke(self, r):
        p = r.get('params') or {}
        if (r.get('method') == 'Network.responseReceived' and p.get('type') == 'Document'
                and p.get('frameId') in (None, getattr(self, 'hauptframe', None))):
            self.status[p['response']['url']] = p['response']['status']

    def _recv_timeout(self, wunsch=60):
        """Websocket-Wartezeit, nie über das Zeitbudget der aktuellen ASIN hinaus."""
        if self.frist is None:
            return wunsch
        rest = self.frist - time.time()
        if rest <= 0:
            raise ZeitLimit('timeout')
        return max(0.05, min(wunsch, rest))

    def cmd(self, m, **pa):
        self.i += 1; self.ws.send(json.dumps({'id': self.i, 'method': m, 'params': pa}))
        while True:
            # ohne Frist-Prüfung hier konnte ein Strom anderer Ereignisse die Schleife endlos am Leben halten
            self.ws.settimeout(self._recv_timeout())
            try:
                r = json.loads(self.ws.recv())
            except websocket.WebSocketTimeoutException:
                if self.frist is not None and time.time() >= self.frist:
                    raise ZeitLimit('timeout')
                raise
            self._merke(r)
            if r.get('id') == self.i:
                return r

    def lade(self, url, warte=7, max_warte=60):
        """Navigiert und wartet, bis das Dokument wirklich fertig ist (readyState 'complete' bzw.
        Produktspalte samt Kaufbox-Elementen da), mindestens `warte` s, höchstens `max_warte` s.
        Früher wurde fest nach 7 s ausgewertet: Amazon streamt die Produktseite in Teilen; kommt der
        Rest langsamer (Netz/Server), stand dann nur der Kopf (<title>) im DOM, #productTitle fehlte
        noch und jede ASIN wurde fälschlich „unklar“."""
        self.status = {}
        # alte Seite markieren, damit die Bereitschaftsprüfung nicht versehentlich sie auswertet
        self.cmd('Runtime.evaluate', expression='window.__vkAlt=1')
        self.cmd('Page.navigate', url=url)
        start = time.time()
        bereit_seit = None
        naechste = start + 1
        if self.frist is not None:              # nie länger warten als das ASIN-Budget erlaubt
            max_warte = min(max_warte, max(0, self.frist - start - 5))
        while time.time() - start < max_warte:
            rest = naechste - time.time()
            if rest > 0:                        # bis zur nächsten Prüfung Ereignisse abholen
                self.ws.settimeout(self._recv_timeout(rest))
                try:
                    r = json.loads(self.ws.recv())
                    self._merke(r)
                except websocket.WebSocketTimeoutException:
                    pass
                continue
            naechste = time.time() + 1
            z = self.cmd('Runtime.evaluate', expression=BEREIT_JS, returnByValue=True)['result']['result'].get('value') or {}
            if z.get('fertig'):
                bereit_seit = bereit_seit or time.time()
                # kurz nachlaufen lassen, damit per JS nachgeladene Kaufbox-Teile stehen
                if time.time() - start >= warte and time.time() - bereit_seit >= 2:
                    break
            else:
                bereit_seit = None
        v = self.cmd('Runtime.evaluate', expression=JS, returnByValue=True)['result']['result'].get('value') or {}
        v['http'] = list(self.status.values())
        v['wartezeit'] = round(time.time() - start, 1)
        return v

    def angebote(self):
        """Klickt „Alle Angebote/Kaufoptionen“ (normale Seitenbedienung) und liest die Zustände der Angebote."""
        js = r"""(async()=>{const c=document.querySelector('#buybox-see-all-buying-choices');const a=c&&(c.querySelector('a,input,button')||c);
if(!a)return [];a.click();await new Promise(r=>setTimeout(r,5000));
return [...document.querySelectorAll('#aod-pinned-offer, #aod-offer')].map(x=>((x.querySelector('#aod-offer-heading')||{}).innerText||'').replace(/\s+/g,' ').trim()).filter(Boolean)})()"""
        return self.cmd('Runtime.evaluate', expression=js, returnByValue=True, awaitPromise=True)['result']['result'].get('value') or []

    def zu(self):
        """Beendet Chrome samt aller Kindprozesse (eigene Prozessgruppe). Mehrfach aufrufbar."""
        try: self.ws.close()
        except Exception: pass
        try: pgid = os.getpgid(self.p.pid)
        except Exception: pgid = None
        if self.p.poll() is None:
            self.p.terminate()
            try: self.p.wait(10)
            except Exception: self.p.kill()
        if pgid:
            try: os.killpg(pgid, signal.SIGKILL)   # verbliebene Renderer/Helfer
            except Exception: pass
        try: self.p.wait(5)
        except Exception: pass


# ---------------------------------------------------------------- Einstufung
def einstufen(asin, name, v):
    """-> (status, begruendung)"""
    if not v:
        return 'unklar', 'keine Antwort'
    if v.get('captcha'):
        return 'unklar', 'Captcha/Robot-Check'
    http = v.get('http') or []
    if 404 in http or v.get('dog'):
        return 'ungueltig', 'Seite nicht gefunden (404/Hundeseite)'
    if any(c in (403, 429, 503) for c in http) and not v.get('title'):
        return 'unklar', f'HTTP {http}'
    titel = v.get('title', '')
    if not titel and v.get('rs') == 'complete' and not v.get('ppd'):
        # Seite fertig geladen, aber Amazon hat den Produktbereich (#ppd) gar nicht ausgeliefert –
        # nur Kopf/Navigation und „Weitermachen, wo du aufgehört hast“. Kein Captcha, aber auch keine
        # Aussage über die Verfügbarkeit möglich -> unklar (später erneut versuchen, nichts umgehen).
        return 'unklar', (f'Amazon lieferte die Seite ohne Produktbereich (Seitentitel: {v.get("doctitle", "")[:60]!r}, '
                          f'HTTP {http}, {v.get("laenge", 0) // 1024} KB)')
    if not titel:
        return 'unklar', (f'kein Produkttitel erkannt (Seitentitel: {v.get("doctitle", "")[:60]!r}, HTTP {http}, '
                          f'readyState {v.get("rs", "?")}, {v.get("laenge", 0) // 1024} KB nach {v.get("wartezeit", "?")} s)')
    ok, warum = titel_passt(name, titel)
    seite = v.get('asin') or (re.search(r'/dp/(' + ASIN_RE + ')', v.get('canon', '') + ' ' + v.get('url', '')) or [None, ''])[1]
    if not ok:
        return 'ungueltig', f'Titel passt nicht ({warum}); Seite zeigt ASIN {seite or "?"}'
    if v.get('cart') or v.get('buynow'):
        return 'verfuegbar', 'Kaufbox vorhanden' + (f' (Seite zeigt Variante {seite})' if seite and seite != asin else '')
    angebote = ' '.join([v.get('choices', ''), v.get('aod', ''), ' '.join(v.get('angebote') or [])])
    if re.search(r'\bNeu\b', angebote):
        return 'verfuegbar', 'keine Kaufbox, aber Neu-Angebot anderer Verkäufer: ' + angebote[:80]
    if v.get('oos') or re.search(r'nicht verfügbar', v.get('avail', ''), re.I):
        return 'nicht_verfuegbar', v.get('avail', '')[:80] or 'outOfStock'
    if re.search(r'Gebraucht', angebote + ' ' + v.get('used', '')):
        return 'nicht_verfuegbar', 'nur Gebraucht-Angebote'
    if v.get('choices'):
        return 'unklar', 'nur „Alle Kaufoptionen“ ohne erkennbares Neu-Angebot'
    return 'nicht_verfuegbar', 'keine Kaufbox, kein Angebot (' + (v.get('avail', '') or '-')[:60] + ')'


def sperrseite(st, warum):
    """True, wenn ein unklar-Ergebnis nach Sperre aussieht (Captcha, Rumpfseite ohne #ppd, 403/429/503)."""
    return st == 'unklar' and bool(re.match(r'Captcha|Amazon lieferte die Seite ohne Produktbereich|HTTP \[', warum))


# ---------------------------------------------------------------- Hauptprogramm
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--nur', nargs='*', help='nur diese ASINs prüfen (Rest behält Stand)')
    ap.add_argument('--trocken', action='store_true', help='nichts schreiben')
    a = ap.parse_args()
    heute = dt.date.today().isoformat()
    asins = sammle()
    alt = {}
    if os.path.exists(DATEI):
        alt = (yaml.safe_load(open(DATEI, encoding='utf-8')) or {}).get('asins', {}) or {}
    pruef = [x for x in asins if not a.nur or x in a.nur]
    print(f'{len(asins)} ASINs auf der Website, prüfe {len(pruef)} (je amazon.de/dp/<ASIN>, ohne Tag)', flush=True)
    ergebnis = {}
    blockt = ''
    # SIGTERM (z. B. von `timeout` im Wrapper) -> normales Beenden, damit finally/atexit Chrome schließen
    signal.signal(signal.SIGTERM, lambda s, f: sys.exit(143))
    signal.signal(signal.SIGALRM, _alarm)
    b = None
    try:
        b = Browser()
        sperr_folge = 0
        for n, asin in enumerate(pruef):
            name = asins[asin]['name']
            st, warum, v = 'unklar', '', {}
            frist = time.time() + ASIN_TIMEOUT
            b.frist = frist
            # harte Obergrenze auch für blockierende Aufrufe außerhalb des Websockets (+10 s Puffer)
            signal.setitimer(signal.ITIMER_REAL, ASIN_TIMEOUT + 10)
            try:
                for versuch in range(3):
                    try:
                        v = b.lade(f'https://www.amazon.de/dp/{asin}')
                        if v.get('title') and not (v.get('cart') or v.get('buynow')) and v.get('choices'):
                            v['angebote'] = b.angebote()      # Zustände der Angebote (Neu/Gebraucht)
                        st, warum = einstufen(asin, name, v)
                    except ZeitLimit:
                        raise
                    except Exception as e:
                        st, warum = 'unklar', f'Fehler: {type(e).__name__}: {e}'[:120]
                        b.zu(); b = Browser(); b.frist = frist
                    if st != 'unklar':
                        break
                    pause = 20 * (versuch + 1) + random.uniform(0, 10)
                    if versuch == 2 or frist - time.time() < pause + 15:
                        break                                 # Budget reicht für keinen sinnvollen Versuch mehr
                    time.sleep(pause)
            except ZeitLimit:
                st, warum = 'unklar', f'timeout (> {ASIN_TIMEOUT:.0f} s)'
                signal.setitimer(signal.ITIMER_REAL, 0)
                b.frist = None
                b.zu(); b = Browser()                         # Seite/Browser hängt evtl. -> frisch starten
            finally:
                signal.setitimer(signal.ITIMER_REAL, 0)
                if b is not None:
                    b.frist = None
            ergebnis[asin] = {'status': st, 'grund': warum, 'titel': (v.get('title') or '')[:120],
                              'ort': v.get('ort', ''), 'name': name}
            print(f'[{n + 1}/{len(pruef)}] {asin} {st:16} {name or "-"} | {warum}', flush=True)
            # Früher Abbruch: Amazon blockt -> keine halbe Stunde weiterprobieren
            sperr_folge = sperr_folge + 1 if sperrseite(st, warum) else 0
            if (n + 1 == BLOCK_ANFANG and len(pruef) > BLOCK_ANFANG
                    and all(e['status'] == 'unklar' for e in ergebnis.values())):
                blockt = f'die ersten {BLOCK_ANFANG} ASINs alle „unklar“'
            elif sperr_folge >= BLOCK_SPERRSEITEN and len(pruef) > BLOCK_SPERRSEITEN:
                blockt = f'{sperr_folge} ASINs in Folge mit Captcha/Sperr-/Rumpfseite'
            if blockt:
                break
            if n + 1 < len(pruef):
                time.sleep(random.uniform(6, 11))
    finally:
        signal.setitimer(signal.ITIMER_REAL, 0)
        if b is not None:
            b.zu()

    os.makedirs(STATE, exist_ok=True)   # Protokoll liegt außerhalb des Repos
    json.dump({'zeit': dt.datetime.now().isoformat(timespec='seconds'), 'ergebnis': ergebnis,
               'abbruch': blockt or None},
              open(os.path.join(STATE, f'verfuegbarkeit-{heute}.json'), 'w'), ensure_ascii=False, indent=1)

    if blockt:
        print(f'PROBLEM: amazon blockt ({blockt}) – Lauf abgebrochen, es wird NICHTS geändert.', flush=True)
        return EXIT_BLOCKT

    unklar = [x for x in ergebnis if ergebnis[x]['status'] == 'unklar']
    if pruef and len(unklar) / len(pruef) > UNKLAR_GRENZE:
        print(f'PROBLEM: {len(unklar)} von {len(pruef)} ASINs „unklar“ (> {int(UNKLAR_GRENZE * 100)} %) – '
              'vermutlich Captcha/Sperre. Es wird NICHTS geändert.', flush=True)
        return 3

    neu, aenderungen = {}, []
    for asin in sorted(asins, key=lambda x: (asins[x]['name'] or 'zzz', x)):
        vorher = alt.get(asin)
        e = ergebnis.get(asin)
        if e is None or e['status'] == 'unklar':
            if vorher:
                neu[asin] = vorher                     # letzter bekannter Stand bleibt
            continue                                   # unbekannt und unklar -> kein Eintrag (= Link bleibt)
        if vorher and vorher.get('status') == e['status']:
            neu[asin] = dict(vorher, geprueft=heute)
        else:
            neu[asin] = {'modell': asins[asin]['name'] or None, 'status': e['status'], 'geprueft': heute, 'seit': heute}
            aenderungen.append((asin, asins[asin]['name'], (vorher or {}).get('status', 'neu'), e['status'], e['grund']))
    for asin in alt:
        if asin not in asins:
            aenderungen.append((asin, alt[asin].get('modell') or '', alt[asin].get('status'), 'entfernt', 'nicht mehr auf der Website'))

    if not aenderungen:
        print('keine änderung', flush=True)
        return 0
    for asin, name, v, n_, g in aenderungen:
        print(f'ÄNDERUNG {asin} {name or "-"}: {v} -> {n_} ({g})', flush=True)
    if a.trocken:
        print('(--trocken: Datei nicht geschrieben)')
        return 0
    kopf = ('# Amazon-Verfügbarkeit je ASIN – automatisch erzeugt von tools/verfuegbarkeit.py, nicht von Hand pflegen.\n'
            '# status: verfuegbar | nicht_verfuegbar | ungueltig. Bei nicht_verfuegbar/ungueltig zeigt die Website\n'
            '# keinen Amazon-Link, sondern „Derzeit bei Amazon nicht verfügbar“; Empfehlungen weichen auf ersatz aus.\n'
            '# geprueft: Datum der letzten Prüfung mit Ergebnis (wird nur bei einer Statusänderung mitgeschrieben),\n'
            '# seit: seit wann der Status gilt. ASINs ohne Eintrag gelten als verfügbar.\n')
    with open(DATEI, 'w', encoding='utf-8') as f:
        f.write(kopf)
        yaml.safe_dump({'asins': neu}, f, allow_unicode=True, sort_keys=False, default_flow_style=False)
    return 0


if __name__ == '__main__':
    sys.exit(main())
