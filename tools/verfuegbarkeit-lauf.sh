#!/bin/bash
# Täglicher Verfügbarkeits-Lauf: prüft alle Amazon-ASINs (tools/verfuegbarkeit.py), und nur wenn sich
# data/verfuegbarkeit.yaml ändert: Hugo-Testbuild, Commit „Verfügbarkeit: …“, Push (= Deploy via Actions).
# Zu viele „unklar“ (Captcha/Sperre): Problem melden, nichts ändern.
# Amazon blockt (Prüfskript Exit 8) oder Gesamtzeit > VK_GESAMT (Standard 20 min): Problem melden, nichts ändern.
# Aufruf: bash tools/verfuegbarkeit-lauf.sh
set -uo pipefail
cd "$(dirname "$0")/.."
# Python: $PY, sonst venv (falls vorhanden), sonst python3. Fehlende Module werden per pip --user nachinstalliert.
if [ -z "${PY:-}" ]; then
  if [ -x /workspace/blogbot/venv/bin/python ]; then PY=/workspace/blogbot/venv/bin/python; else PY=$(command -v python3); fi
fi
FEHLT=""
for m in yaml:pyyaml websocket:websocket-client; do
  "$PY" -c "import ${m%%:*}" 2>/dev/null || FEHLT="$FEHLT ${m#*:}"
done
if [ -n "$FEHLT" ]; then
  echo "Installiere fehlende Python-Module:$FEHLT"
  "$PY" -m pip install --user --quiet $FEHLT 2>/dev/null || "$PY" -m pip install --user --quiet --break-system-packages $FEHLT \
    || { echo "PROBLEM: Python-Module$FEHLT nicht installierbar – Lauf abgebrochen."; exit 2; }
  for m in yaml websocket; do "$PY" -c "import $m" 2>/dev/null || { echo "PROBLEM: Modul $m mit $PY nicht importierbar – Lauf abgebrochen."; exit 2; }; done
fi
HUGO=${HUGO:-$HOME/.local/bin/hugo}
LOG=$(mktemp)
PROFIL=${AMZ_PROFIL:-$HOME/.local/share/balkonstrom/amz-profil}
# Beim Beenden (auch Abbruch/Timeout) keine Chrome-Reste mit dem Prüfprofil zurücklassen
aufraeumen() { rm -f "$LOG"; pkill -KILL -f -- "--user-data-dir=$PROFIL" 2>/dev/null || true; }
trap aufraeumen EXIT
trap 'exit 130' INT TERM HUP

if [ -n "$(git status --porcelain -- data/verfuegbarkeit.yaml)" ]; then
  echo "PROBLEM: data/verfuegbarkeit.yaml hat bereits uncommittete Änderungen – Lauf abgebrochen."; exit 2
fi
git pull -q --rebase --autostash origin main || { echo "PROBLEM: git pull fehlgeschlagen – Lauf abgebrochen."; exit 2; }

timeout --kill-after=30 "${VK_GESAMT:-20m}" "$PY" tools/verfuegbarkeit.py "$@" 2>&1 | tee "$LOG"
rc=${PIPESTATUS[0]}
if [ "$rc" = 124 ] || [ "$rc" = 137 ]; then
  git checkout -q -- data/verfuegbarkeit.yaml 2>/dev/null
  echo; echo "PROBLEM: Gesamtzeit von ${VK_GESAMT:-20m} überschritten – Lauf abgebrochen, es wurde nichts geändert."; exit 124
elif [ "$rc" = 8 ]; then
  git checkout -q -- data/verfuegbarkeit.yaml 2>/dev/null
  echo; echo "PROBLEM: amazon blockt (die ersten Prüfungen alle „unklar“/Sperrseiten) – Lauf abgebrochen, es wurde nichts geändert."; exit 8
elif [ "$rc" = 3 ]; then
  echo; echo "PROBLEM: zu viele Prüfungen „unklar“ (Captcha/Sperre?) – es wurde nichts geändert."; exit 3
elif [ "$rc" != 0 ]; then
  git checkout -q -- data/verfuegbarkeit.yaml 2>/dev/null
  echo; echo "PROBLEM: Prüfskript mit Fehler $rc beendet – nichts geändert."; exit "$rc"
fi

if git diff --quiet -- data/verfuegbarkeit.yaml && [ -z "$(git ls-files --others --exclude-standard data/verfuegbarkeit.yaml)" ]; then
  echo; echo "keine änderung"; exit 0
fi

OUT=$(mktemp -d)
if ! "$HUGO" --quiet -d "$OUT" >/dev/null 2>"$OUT.err"; then
  echo; echo "PROBLEM: Hugo-Build schlägt fehl – Änderung NICHT committet:"; cat "$OUT.err"
  git checkout -q -- data/verfuegbarkeit.yaml 2>/dev/null; rm -rf "$OUT" "$OUT.err"; exit 4
fi
# Kein Link auf eine als nicht verfügbar/ungültig markierte ASIN im Build
BAD=$("$PY" - "$OUT" <<'PYEOF'
import sys, yaml, glob, re
d = (yaml.safe_load(open('data/verfuegbarkeit.yaml')) or {}).get('asins', {}) or {}
weg = [a for a, v in d.items() if v.get('status') in ('nicht_verfuegbar', 'ungueltig')]
hits = []
for f in glob.glob(sys.argv[1] + '/**/*.html', recursive=True):
    t = open(f, encoding='utf-8').read()
    for a in weg:
        if re.search(r'href="?https://www\.amazon\.de/[^"> ]*' + a, t):
            hits.append(f'{a} in {f}')
print('\n'.join(hits))
PYEOF
)
rm -rf "$OUT" "$OUT.err"
if [ -n "$BAD" ]; then
  echo; echo "PROBLEM: Build enthält noch Links auf nicht verfügbare ASINs – NICHT committet:"; echo "$BAD"
  git checkout -q -- data/verfuegbarkeit.yaml; exit 5
fi

AEND=$(grep '^ÄNDERUNG ' "$LOG" | sed 's/^ÄNDERUNG //')
KURZ=$(echo "$AEND" | sed -E 's/^[A-Z0-9]{10} //; s/ \(.*$//' | paste -sd ';' | sed 's/;/; /g')
git add data/verfuegbarkeit.yaml
git commit -q -m "Verfügbarkeit: ${KURZ:0:200}" -m "$AEND" || { echo "PROBLEM: Commit fehlgeschlagen"; exit 6; }
if ! git push -q origin HEAD:main; then
  echo "PROBLEM: Push fehlgeschlagen – Commit liegt lokal ($(git log --oneline -1))."; exit 7
fi
echo
echo "Verfügbarkeit geändert und veröffentlicht ($(git log --oneline -1 | cut -c1-7)):"
echo "$AEND" | sed 's/^/  - /'
