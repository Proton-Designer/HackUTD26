# server/ (hub)
Run: `python3 -m venv .venv-hub && .venv-hub/bin/pip install -r server/requirements.txt && .venv-hub/bin/uvicorn server.main:app --port 8000`
Test: `.venv-hub/bin/python -m pytest server -q`
- `from server.bus import publish` then `publish("call.routed", call_id, {...})` (never raises).
- `from server.main import mount_router` to mount a FastAPI router (voip/, others).
- Routing: `server/routing.py` (fail-open), store `server/db.py` (env `HUB_DB` for path).
- Endpoints: see contracts/interfaces.md. Stubs: /intel/ingest logs only.
