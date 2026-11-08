#!/usr/bin/env bash
# P2 acceptance suite (hub :8190 / P2 :8191, real NVIDIA STT+LLM, synthetic TTS calls). ~2-3 min. Exit 0 = no FAIL.
cd "$(git rev-parse --show-toplevel)" || exit 1
set -a; [ -f .env ] && . ./.env; set +a
exec .venv/bin/python detection/scripts/acceptance.py
