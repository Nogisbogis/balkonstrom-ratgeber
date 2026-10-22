#!/bin/bash
# Täglicher AWIN-Lauf: prüft Programmstatus (tools/awin-programme.py → data/awin.yaml) und – nur bei
# inhaltlicher Änderung (Status eines Advertisers oder Erreichbarkeit einer Shopseite) – Hugo-Testbuild,
# Commit „AWIN: …“, Push (= Deploy via Actions). Reine Datums-Aktualisierung = „keine änderung“.
# Ist danach ≥1 Programm joined, laufen vor dem Push zusätzlich: lychee offline und die Prüfung, dass jede Seite
# mit awin1-Link den AWIN-Werbehinweis trägt (plus AWIN-Abschnitt in Datenschutz/Impressum); sonst PROBLEM, kein Push.
# API-Fehler: PROBLEM melden, nichts ändern. Token nur aus Umgebung AWIN_API_TOKEN (wird nie ausgegeben).
# Aufruf: bash tools/awin-lauf.sh
set -uo pipefail
cd "$(dirname "$0")/.."
PY=${PY:-python3}
HUGO=${HUGO:-$HOME/.local/bin/hugo}
LYCHEE=${LYCHEE:-$HOME/.local/bin/lychee}
F=data/awin.yaml
LOG=$(mktemp)
trap 'rm -f "$LOG"' EXIT

zurueck() { if git ls-files --error-unmatch "$F" >/dev/null 2>&1; then git checkout -q -- "$F"; elif [ -f "$LOG.bak" ]; then cp "$LOG.bak" "$F"; fi; }

if [ -n "$(git status --porcelain -- "$F")" ]; then
  echo "PROBLEM: $F hat bereits uncommittete Änderungen – Lauf abgebrochen."; exit 2
fi
git pull -q --rebase --autostash origin main || { echo "PROBLEM: git pull fehlgeschlagen – Lauf abgebrochen."; exit 2; }
[ -f "$F" ] && cp "$F" "$LOG.bak"
trap 'rm -f "$LOG" "$LOG.bak"' EXIT

"$PY" tools/awin-programme.py 2>&1 | tee "$LOG"
rc=${PIPESTATUS[0]}
if [ "$rc" != 0 ]; then
  zurueck
  echo; echo "PROBLEM: AWIN-Prüfung mit Fehler $rc beendet (API/Token?) – nichts geändert."; exit "$rc"
fi

AEND=$(grep '^ÄNDERUNG ' "$LOG" | sed 's/^ÄNDERUNG //')
if [ -z "$AEND" ]; then
  zurueck
  echo; echo "keine änderung"; exit 0
fi

OUT=$(mktemp -d)
if ! "$HUGO" --quiet --minify -d "$OUT" >/dev/null 2>"$OUT.err"; then
  echo; echo "PROBLEM: Hugo-Build schlägt fehl – Änderung NICHT committet:"; cat "$OUT.err"
  zurueck; rm -rf "$OUT" "$OUT.err"; exit 4
fi
# Sicherheitsnetz: AWIN-Links im Build nur für Advertiser mit Status joined
PRUEF=$("$PY" - "$OUT" <<'PYEOF'
import sys, yaml, glob, re, collections
d = yaml.safe_load(open('data/awin.yaml')) or {}
ok = {str(a.get('id')) for a in (d.get('advertisers') or {}).values() if a.get('status') == 'joined'}
n, bad = collections.Counter(), []
for f in glob.glob(sys.argv[1] + '/**/*.html', recursive=True):
    for mid in re.findall(r'awin1\.com/cread\.php\?awinmid=(\d+)', open(f, encoding='utf-8').read()):
        n[mid] += 1
        if mid not in ok:
            bad.append(f'{mid} in {f}')
# Rechtstexte-Gate (nur wenn ≥1 Programm joined): jede Seite mit awin1-Link braucht den AWIN-Zusatz der
# Werbekennzeichnung, Datenschutz braucht Abschnitt #awin, Impressum den AWIN-Hinweis.
fehlt = []
if ok:
    for f in glob.glob(sys.argv[1] + '/**/*.html', recursive=True):
        t = open(f, encoding='utf-8').read()
        if 'awin1.com' in t and 'Partnernetzwerk AWIN' not in t:
            fehlt.append(f'Werbehinweis fehlt: {f}')
    for p, s in (('datenschutz', 'id=awin'), ('impressum', 'über das Partnernetzwerk AWIN')):
        try:
            if s not in open(f'{sys.argv[1]}/{p}/index.html', encoding='utf-8').read():
                fehlt.append(f'AWIN-Text fehlt: /{p}/')
        except OSError:
            fehlt.append(f'Seite fehlt: /{p}/')
if bad:
    print('BAD ' + '; '.join(sorted(set(bad))))
elif fehlt:
    print('RECHT ' + '; '.join(fehlt))
else:
    print(('AKTIV ' if ok else 'LINKS ') + (', '.join(f'{k}: {v}' for k, v in sorted(n.items())) or 'keine'))
PYEOF
)
case "$PRUEF" in
  BAD*) echo; echo "PROBLEM: Build enthält AWIN-Links für nicht beigetretene Programme – NICHT committet:"; echo "${PRUEF#BAD }"; rm -rf "$OUT" "$OUT.err"; zurueck; exit 5;;
  RECHT*) echo; echo "PROBLEM: AWIN aktiv, aber Rechtstexte unvollständig – NICHT committet:"; echo "${PRUEF#RECHT }"; rm -rf "$OUT" "$OUT.err"; zurueck; exit 8;;
  AKTIV*)
    # Aktivierung: zusätzlich Linkprüfung (offline, interne Links/Anker) vor dem Push
    if ! (cd "$OUT" && "$LYCHEE" --offline --index-files index.html --root-dir "$OUT" --exclude 'amazon\.' --exclude 'awin1' --no-progress '**/*.html' >"$OUT.err" 2>&1); then
      echo; echo "PROBLEM: lychee meldet kaputte Links – NICHT committet:"; grep -E '\[(ERROR|[0-9]{3})\]|Errors' "$OUT.err" | head -20
      rm -rf "$OUT" "$OUT.err"; zurueck; exit 9
    fi
    PRUEF="LINKS ${PRUEF#AKTIV }";;
esac
rm -rf "$OUT" "$OUT.err"

KURZ=$(echo "$AEND" | paste -sd ';' | sed 's/;/; /g')
git add "$F"
git commit -q -m "AWIN: ${KURZ:0:200}" -m "$AEND" -m "AWIN-Links im Build: ${PRUEF#LINKS }" || { echo "PROBLEM: Commit fehlgeschlagen"; exit 6; }
if ! git push -q origin HEAD:main; then
  echo "PROBLEM: Push fehlgeschlagen – Commit liegt lokal ($(git log --oneline -1))."; exit 7
fi
echo
echo "AWIN geändert und veröffentlicht ($(git log --oneline -1 | cut -c1-7)):"
echo "$AEND" | sed 's/^/  - /'
echo "  AWIN-Links im Build: ${PRUEF#LINKS }"
