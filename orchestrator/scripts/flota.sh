#!/bin/bash
# Leagă fiecare rol al flotei de sesiunea Claude pornită în folderul lui din rădăcina flotei.
# Motiv: numele din ListAgents au sufix volatil și, dacă pe aceeași mașină rulează o a doua
# flotă cu aceleași prefixe de rol, un mesaj trimis pe nume poate ajunge la agentul greșit.
# Ieșire: rol, adresa pentru SendMessage (uds:...), sau LIPSEȘTE / DUBLAT.
#
# Rolurile se citesc din orchestrator/roluri.txt, câte unul pe linie. Nu edita scriptul.

# Scriptul foloseste tablouri bash. Rulat din zsh, ele se comportă altfel și rezultatul
# iese gol fără nicio eroare, adică arată ca o ieșire bună. Verificat pe 7 octombrie 2026.
if [ -z "$BASH_VERSION" ]; then
  echo "flota.sh: rulează-l cu /bin/bash, nu prin alt shell." >&2
  echo "           corect:  /bin/bash scripts/flota.sh" >&2
  exit 2
fi

AICI="$(cd "$(dirname "$0")" && pwd)"
ORCHESTRATOR="$(cd "$AICI/.." && pwd)"
RADACINA="$(cd "$ORCHESTRATOR/.." && pwd)"
ROLURI="$ORCHESTRATOR/roluri.txt"

if [ ! -f "$ROLURI" ]; then
  echo "flota.sh: lipsește $ROLURI. Scrie în el prefixele rolurilor, câte unul pe linie." >&2
  exit 2
fi

while IFS= read -r rol || [ -n "$rol" ]; do
  rol="${rol%%#*}"                      # comentariile de la capăt de linie
  rol="$(echo "$rol" | tr -d '[:space:]')"
  [ -n "$rol" ] || continue

  if [ ! -d "$RADACINA/$rol" ]           # un rol fără folder e o greșeală de scris
  then
    echo "$rol  FĂRĂ FOLDER în $RADACINA"
    continue
  fi

  gasite=()
  for s in /tmp/cc-socks/*.sock; do
    [ -e "$s" ] || continue
    pid=$(basename "$s" .sock)
    cwd=$(lsof -a -p "$pid" -d cwd -Fn 2>/dev/null | sed -n 's/^n//p')
    [ "$cwd" = "$RADACINA/$rol" ] && gasite+=("uds:$s")
  done

  case ${#gasite[@]} in
    0) echo "$rol  LIPSEȘTE" ;;
    1) echo "$rol  ${gasite[0]}" ;;
    *) echo "$rol  DUBLAT: ${gasite[*]}" ;;
  esac
done < "$ROLURI"
