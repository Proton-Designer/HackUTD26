# server/ (hub)
Run: `python3 -m venv .venv-hub && .venv-hub/bin/pip install -r server/requirements.txt && .venv-hub/bin/uvicorn server.main:app --port 8000`
Test: `.venv-hub/bin/python -m pytest server -q`
- `from server.bus import publish` then `publish("call.routed", call_id, {...})` (never raises).
- `from server.main import mount_router` to mount a FastAPI router (voip/, others).
- Routing: `server/routing.py` (fail-open), store `server/db.py` (env `HUB_DB` for path).
- Endpoints: see contracts/interfaces.md. Stubs: /intel/ingest logs only.

## Run + ops (TASK-010)
- `scripts/run_hub` starts the hub and a cloudflared quick tunnel (ephemeral URL; `NO_TUNNEL=1` to skip) and prints the Telnyx webhook command for the lead.
- `GET /demo/status` (JSON, or HTML with `?format=html`): routers mounted (voip `/telnyx*`, P2 `/detect`, P3 `/decoy`, P4 `/intel/actions`), probes of `VOIP_BASE`/`P2_BASE`/`P3_BASE`/`P4_BASE` (1 s), env flags (set/unset only), DB counts.
- `GET /demo/latency`: route_ms (incoming→routed), alert_ms (incoming→alert.fired), handoff_ms (user.action→handoff.started); also appended to `logs/latency.jsonl` (gitignored).
