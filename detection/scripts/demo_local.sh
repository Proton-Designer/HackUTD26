#!/usr/bin/env bash
# "Demo in a box": the whole phone-free demo on this machine, no tunnel, no Telnyx. SIMULATED caller (synthetic WAV), SIMULATED Maria tap.
#   bash detection/scripts/demo_local.sh                 # NVIDIA STT+LLM
#   OFFLINE=1 bash detection/scripts/demo_local.sh       # P2_STT=whisper + P2_ENGINE=local (needs llama-server on :8101; intel/decoy may still want NVIDIA)
# Env: HUB_PORT=8200 P2_PORT=8102 DEMO_P3_PORT=8310 DEMO_NO_DECOY=1 DEMO_WAV=<8k mono wav> AUTO_TAP=1 (0 = you press the button at <hub>/app/) KEEP_UP=1 (leave it running, Ctrl-C stops)
# Isolated: temp DBs/logs, its own ports, no HUB_TOKEN/PIPELINE_TOKEN. Never touches :8100 or the live hub. Clean shutdown via process groups.
cd "$(git rev-parse --show-toplevel)" || exit 1
set -a; [ -f .env ] && . ./.env; set +a
unset HUB_TOKEN PIPELINE_TOKEN PUBLIC_WS
HP=${HUB_PORT:-8200}; PP=${P2_PORT:-8102}; DP=${DEMO_P3_PORT:-8310}; HUB="http://127.0.0.1:$HP"
for p in $HP $PP $DP; do lsof -nP -iTCP:$p -sTCP:LISTEN >/dev/null 2>&1 && { echo "port $p busy; set HUB_PORT / P2_PORT"; exit 1; }; done
[ -z "${LOCAL_LLM_URL:-}" ] && export LOCAL_LLM_URL="http://$(ip route | awk '/default/{print $3}'):8101"
T=$(mktemp -d); PIDS=()
if [ "${OFFLINE:-}" = "1" ]; then export P2_STT=whisper P2_ENGINE=local; echo "OFFLINE mode: whisper STT + local LLM ($LOCAL_LLM_URL)"; fi
cleanup() { trap - EXIT INT TERM; for p in "${PIDS[@]:-}"; do [ -n "$p" ] && kill -TERM -- "-$p" 2>/dev/null; done; sleep 1
            for p in "${PIDS[@]:-}"; do [ -n "$p" ] && kill -KILL -- "-$p" 2>/dev/null; done; echo "stopped (logs kept in $T)"; }
trap cleanup EXIT INT TERM
launch() { local log=$1; shift; setsid "$@" >"$log" 2>&1 & PIDS+=($!); }
export SIM_MODE=1 NO_TUNNEL=1 HUB_DB=$T/hub.db INTEL_DB=$T/intel.db LOGDIR=$T HUB_NO_PIN_FILE=1 DEVICE_PIN=${DEVICE_PIN:-1234}
export DEMO_CALLER_WAV=${DEMO_WAV:-$PWD/detection/testdata/scam_call_synth.wav} P2_BASE="http://127.0.0.1:$PP" HUB_URL="$HUB" P2_PORT=$PP
unset P2_STT_URL
[ "${DEMO_NO_DECOY:-}" != "1" ] && export P3_DECOY_URL="ws://127.0.0.1:$DP" P3_VOICE_URL="http://127.0.0.1:$DP" P3_BASE="http://127.0.0.1:$DP"   # P3 decoy (NVIDIA LLM+TTS, needs ffmpeg); DEMO_NO_DECOY=1 = hub echo stand-in
launch $T/hub.log .venv/bin/python -m uvicorn server.main:app --host 127.0.0.1 --port "$HP"
[ "${DEMO_NO_DECOY:-}" != "1" ] && HUB_URL="$HUB" launch $T/p3.log .venv/bin/python -m uvicorn decoy.app:app --host 127.0.0.1 --port "$DP"
HUB_URL="$HUB" launch $T/p2.log .venv/bin/python -m uvicorn detection.app:app --host 127.0.0.1 --port "$PP"
for _ in $(seq 1 60); do curl -fsS -m1 "$HUB/healthz" >/dev/null 2>&1 && curl -fsS -m1 "http://127.0.0.1:$PP/healthz" >/dev/null 2>&1 && break; sleep 0.5; done
curl -fsS -m2 "$HUB/healthz" >/dev/null && curl -fsS -m2 "http://127.0.0.1:$PP/healthz" >/dev/null || { echo "hub or P2 failed to start; tails:"; tail -5 $T/hub.log $T/p2.log; exit 1; }
echo "hub  $HUB   P2 http://127.0.0.1:$PP   logs $T"
echo "Maria's page:   $HUB/app/        (device PIN $DEVICE_PIN)"
echo "Command center: $HUB/command-center/"
[ "${AUTO_TAP:-1}" = "1" ] && launch $T/tap.log .venv/bin/python detection/scripts/demo_tap.py "$HUB" 2
.venv/bin/python scripts/demo_call --reset --hub "$HUB" --wav "$DEMO_CALLER_WAV" ${DEMO_ARGS:-}
RC=$?
echo; echo "== P2 per-call report"; .venv/bin/python detection/scripts/call_report.py $T/p2.log --last 1 2>&1 | tail -25
[ -f $T/tap.log ] && echo "== tap: $(tail -1 $T/tap.log)"
[ "${KEEP_UP:-}" = "1" ] && { echo "left running; Ctrl-C to stop"; wait; }
exit $RC
