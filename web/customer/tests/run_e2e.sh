#!/usr/bin/env bash
# One command: no-phone rehearsal of the P1 demo path. Makes a throwaway venv (playwright + websockets) in /tmp on first use.
set -eu
cd "$(dirname "$0")/../../.."
V=${E2E_VENV:-/tmp/backfire-e2e-venv}
[ -x "$V/bin/python" ] || { python3 -m venv "$V" && "$V/bin/python" -m pip install -q playwright websockets; }
exec "$V/bin/python" web/customer/tests/e2e_demo.py "$@"
