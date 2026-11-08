#!/usr/bin/env bash
# P2 acceptance suite (hub :8190 / P2 :8191, real NVIDIA STT+LLM, synthetic TTS calls). ~2-3 min. Exit 0 = no FAIL.
cd "$(git rev-parse --show-toplevel)" || exit 1
[ -z "${LOCAL_LLM_URL:-}" ] && export LOCAL_LLM_URL="http://$(ip route | awk '/default/{print $3}'):8101"  # WSL gateway: llama-server (engines/run_local_llm.sh) does not listen on 127.0.0.1
set -a; [ -f .env ] && . ./.env; set +a
exec .venv/bin/python detection/scripts/acceptance.py
