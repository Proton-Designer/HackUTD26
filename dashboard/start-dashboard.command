#!/bin/bash
# macOS: double-click in Finder (or run ./start-dashboard.command). Starts the dashboard and opens it in Microsoft Edge.
cd "$(dirname "$0")" || exit 1
export PATH="/opt/homebrew/bin:/usr/local/bin:$PATH"
PORT="${PORT:-7777}"
lsof -ti "tcp:$PORT" 2>/dev/null | xargs kill 2>/dev/null   # stop an older copy
( sleep 2; open -a "Microsoft Edge" "http://localhost:$PORT" 2>/dev/null || open "http://localhost:$PORT" ) &
echo "Backfire Agent Ops dashboard → http://localhost:$PORT   (Ctrl+C to stop)"
exec python3 server.py --port "$PORT" "$@"
