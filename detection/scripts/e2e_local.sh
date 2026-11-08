#!/usr/bin/env bash
# Full local loop test on ports 8190 (hub) / 8191 (P2). Needs NVIDIA_API_KEY in .env (real STT + cloud engine). Exit 0 = pass.
cd "$(git rev-parse --show-toplevel)" || exit 1
set -a; [ -f .env ] && . ./.env; set +a
exec .venv/bin/python detection/scripts/e2e_local.py
