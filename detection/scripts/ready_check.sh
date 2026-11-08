#!/usr/bin/env bash
# One-command readiness check (TASK-050). Read-only. Usage: bash detection/scripts/ready_check.sh [--live URL] [--tunnel URL] [--tests] [--no-detect]
cd "$(git rev-parse --show-toplevel)" || exit 1
exec "$([ -x .venv/bin/python ] && echo .venv/bin/python || echo python3)" detection/scripts/ready_check.py "$@"
