#!/usr/bin/env bash
# Run the P2 service on :8100 (loads .env without printing it). Logs to logs/p2.log
cd "$(git rev-parse --show-toplevel)" || exit 1
mkdir -p logs; set -a; [ -f .env ] && . ./.env; set +a
. scripts/pipeline_token   # derive the shared PIPELINE_TOKEN from NVIDIA_API_KEY if unset (P1 #30)
exec .venv/bin/uvicorn detection.app:app --host 0.0.0.0 --port "${P2_PORT:-8100}" 2>&1 | tee -a logs/p2.log
