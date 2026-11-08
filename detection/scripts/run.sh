#!/usr/bin/env bash
# Run the P2 service on :8100 (loads .env without printing it) under a supervisor: if uvicorn exits for any reason,
# log the exit code + time to logs/p2.log and restart after 2 s. Ctrl-C twice (within the restart window) stops it; SIGTERM stops it.
cd "$(git rev-parse --show-toplevel)" || exit 1
mkdir -p logs; set -a; [ -f .env ] && . ./.env; set +a
LOG=logs/p2.log; INTS=0; CHILD=""
trap 'INTS=$((INTS+1)); echo "$(date +%T) got INT #$INTS" >> "$LOG"' INT
trap '[ -n "$CHILD" ] && kill "$CHILD" 2>/dev/null; echo "$(date "+%F %T") supervisor: SIGTERM, stopping" | tee -a "$LOG"; exit 0' TERM
while :; do
  echo "$(date "+%F %T") supervisor: starting uvicorn on :${P2_PORT:-8100}" | tee -a "$LOG"
  ${P2_CMD:-.venv/bin/uvicorn detection.app:app --host 0.0.0.0 --port "${P2_PORT:-8100}"} 2>&1 | tee -a "$LOG"
  RC=${PIPESTATUS[0]}
  echo "$(date "+%F %T") supervisor: uvicorn exited rc=$RC" | tee -a "$LOG"
  [ "$INTS" -ge 2 ] && { echo "$(date "+%F %T") supervisor: stopped by Ctrl-C x2" | tee -a "$LOG"; exit 0; }
  echo "$(date "+%F %T") supervisor: restarting in 2 s (Ctrl-C again to stop)" | tee -a "$LOG"
  sleep 2 & wait $!; WRC=$?
  [ "$INTS" -ge 2 ] && { echo "$(date "+%F %T") supervisor: stopped by Ctrl-C x2" | tee -a "$LOG"; exit 0; }
  [ "$WRC" -eq 0 ] && INTS=0      # an interrupted wait keeps the count so the next Ctrl-C stops
done
