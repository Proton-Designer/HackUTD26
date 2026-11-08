#!/usr/bin/env bash
# Quick cloudflared tunnel to the P2 service; URL goes to logs/p2-tunnel.log and prints here. WS /stt works over wss://<host>/stt/{call_id}
cd "$(git rev-parse --show-toplevel)" || exit 1
mkdir -p logs
exec cloudflared tunnel --url "http://localhost:${P2_PORT:-8100}" 2>&1 | tee logs/p2-tunnel.log
