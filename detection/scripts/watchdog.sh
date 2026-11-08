#!/usr/bin/env bash
# Zero-token watchdog for the live P2 service + quick tunnel (demo insurance). No LLM, never prints .env.
#  1. every WD_TICK_S (20): GET /healthz; refused >=WD_FAILS (3) in a row AND the svc tmux window is missing or a bare shell -> (re)start run.sh there.
#  2. every WD_TUN_EVERY (3) ticks (=60 s): GET <tunnel>/healthz; fails WD_FAILS in a row while local is OK -> restart cloudflared, parse the NEW
#     trycloudflare URL, write logs/p2_tunnel_url.txt, log "TUNNEL URL CHANGED" (the lead tells P1; this script never posts anywhere).
#  3. never restarts while healthz active_stt_sockets>0 (unless local is refused). Log: logs/watchdog.log.
# Launch: bash detection/scripts/watchdog.sh   (e.g. in its own tmux window). Env overrides (tests use them): WD_SESSION WD_SVC_WIN WD_TUN_WIN
# WD_PORT WD_TUNNEL_URL WD_TICK_S WD_TUN_EVERY WD_FAILS WD_MAX_TICKS WD_SVC_CMD WD_TUN_CMD WD_TUN_LOG WD_URL_FILE WD_LOG
cd "$(git rev-parse --show-toplevel)" || exit 1
ROOT=$PWD; mkdir -p logs
SESS=${WD_SESSION:-backfire-p2}; SVCW=${WD_SVC_WIN:-p2svc}; TUNW=${WD_TUN_WIN:-p2tunnel}
PORT=${WD_PORT:-8100}; TICK=${WD_TICK_S:-20}; TUN_EVERY=${WD_TUN_EVERY:-3}; FAILS=${WD_FAILS:-3}; MAXT=${WD_MAX_TICKS:-0}
URLF=${WD_URL_FILE:-logs/p2_tunnel_url.txt}; TLOG=${WD_TUN_LOG:-logs/p2-tunnel.log}; LOG=${WD_LOG:-logs/watchdog.log}
SVC_CMD=${WD_SVC_CMD:-"LOCAL_MODEL=${LOCAL_MODEL:-nemotron-nano-4b} ${HUB_URL:+HUB_URL=$HUB_URL }P2_PORT=$PORT bash detection/scripts/run.sh"}
TUN_CMD=${WD_TUN_CMD:-"P2_PORT=$PORT bash detection/scripts/tunnel.sh"}
TUNNEL=${WD_TUNNEL_URL:-}; [ -z "$TUNNEL" ] && [ -s "$URLF" ] && TUNNEL=$(head -1 "$URLF")
[ -z "$TUNNEL" ] && TUNNEL="https://holding-whether-directories-voting.trycloudflare.com"
say() { echo "$(date '+%F %T') $*" | tee -a "$LOG"; }
health() { curl -s -m 5 -o "$1" -w '%{http_code}' "$2/healthz" 2>/dev/null; }     # prints http code (000 = refused/timeout)
active() { grep -o '"active_stt_sockets": *[0-9]*' "$1" 2>/dev/null | grep -o '[0-9]*$' | head -1; }
bare() { case "$(tmux display -p -t "$SESS:$SVCW" '#{pane_current_command}' 2>/dev/null)" in bash|zsh|sh|fish|dash|"") return 0;; *) return 1;; esac; }
win_exists() { tmux list-windows -t "$SESS" -F '#{window_name}' 2>/dev/null | grep -qx "$1"; }
start_in() {   # $1 window  $2 command: recreate window if missing, else type into the bare shell
  if win_exists "$1"; then tmux send-keys -t "$SESS:$1" "cd $ROOT && $2" Enter
  else tmux has-session -t "$SESS" 2>/dev/null && tmux new-window -d -t "$SESS" -n "$1" -c "$ROOT" "$2" \
       || tmux new-session -d -s "$SESS" -n "$1" -c "$ROOT" "$2"; fi
}
restart_svc() {
  if win_exists "$SVCW" && ! bare; then say "svc: refused x$LFAIL but window $SVCW runs a process: leaving it to the supervisor"; return; fi
  say "SVC RESTART: $SVCW missing or bare shell, refused x$LFAIL -> run.sh"; start_in "$SVCW" "$SVC_CMD"; LFAIL=0
}
restart_tunnel() {
  say "TUNNEL RESTART: $TUNNEL failed x$TFAIL while local OK"
  tmux kill-window -t "$SESS:$TUNW" 2>/dev/null; : > "$TLOG"; start_in "$TUNW" "$TUN_CMD"
  local u="" i; for i in $(seq 1 30); do u=$(grep -o 'https://[a-z0-9-]*\.trycloudflare\.com' "$TLOG" 2>/dev/null | head -1); [ -n "$u" ] && break; sleep 1; done
  if [ -z "$u" ]; then say "TUNNEL: no URL after 30 s, will retry at the next failure"; return; fi
  echo "$u" > "$URLF"; TFAIL=0
  if [ "$u" != "$TUNNEL" ]; then say "!!!! TUNNEL URL CHANGED: $TUNNEL -> $u  (tell P1: P2_STT_URL=wss://${u#https://}) !!!!"; TUNNEL=$u; else say "TUNNEL restarted, same URL $u"; fi
}
say "watchdog start: :$PORT svc=$SESS:$SVCW tunnel=$TUNNEL tick=${TICK}s"
LFAIL=0; TFAIL=0; N=0; TMP=$(mktemp); trap 'rm -f "$TMP"' EXIT
while :; do
  N=$((N+1)); code=$(health "$TMP" "http://localhost:$PORT"); ACT=0
  if [ "$code" = 200 ]; then LFAIL=0; ACT=$(active "$TMP"); ACT=${ACT:-0}; else LFAIL=$((LFAIL+1)); say "local healthz code=$code (x$LFAIL)"; fi
  [ "$LFAIL" -ge "$FAILS" ] && restart_svc
  if [ "$code" = 200 ] && [ $((N % TUN_EVERY)) -eq 0 ]; then
    tcode=$(health /dev/null "$TUNNEL")
    if [ "$tcode" = 200 ]; then TFAIL=0; else TFAIL=$((TFAIL+1)); say "tunnel healthz code=$tcode (x$TFAIL)"; fi
    if [ "$TFAIL" -ge "$FAILS" ]; then
      if [ "$ACT" -gt 0 ]; then say "tunnel down but $ACT active stt sockets: not restarting"; else restart_tunnel; fi
    fi
  fi
  [ "$MAXT" -gt 0 ] && [ "$N" -ge "$MAXT" ] && { say "watchdog stop (WD_MAX_TICKS)"; exit 0; }
  sleep "$TICK"
done
