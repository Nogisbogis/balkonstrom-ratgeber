#!/bin/bash
# Täglicher AWIN-Lauf: prüft Programmstatus (tools/awin-programme.py → data/awin.yaml) und – nur bei
# inhaltlicher Änderung (Status eines Advertisers oder Erreichbarkeit einer Shopseite) – Hugo-Testbuild,
# Commit „AWIN: …“, Push (= Deploy via Actions). Reine Datums-Aktualisierung = „keine änderung“.
# API-Fehler: PROBLEM melden, nichts ändern. Token nur aus Umgebung AWIN_API_TOKEN (wird nie ausgegeben).
# Aufruf: bash tools/awin-lauf.sh
set -uo pipefail
cd "$(dirname "$0")/.."
PY=${PY:-python3}
HUGO=${HUGO:-$HOME/.local/bin/hugo}
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
print('BAD ' + '; '.join(sorted(set(bad))) if bad else 'LINKS ' + (', '.join(f'{k}: {v}' for k, v in sorted(n.items())) or 'keine'))
PYEOF
)
rm -rf "$OUT" "$OUT.err"
case "$PRUEF" in
  BAD*) echo; echo "PROBLEM: Build enthält AWIN-Links für nicht beigetretene Programme – NICHT committet:"; echo "${PRUEF#BAD }"; zurueck; exit 5;;
esac

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
