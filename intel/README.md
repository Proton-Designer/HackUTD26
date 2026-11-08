# intel/ (P4a: real lookups, intel agent, policy gate)

Setup (repo root, venv active): `pip install httpx fastapi pytest`

Real lookups (needs internet):
    python -m intel.lookups domain example.com
    python -m intel.lookups wallet <btc-or-eth-address>
    python -m intel.lookups allow 1-800-935-9935

Offline tests (no internet): `python -m pytest -q intel/`

End-to-end demo:
    python -m intel.demo_run           # offline: fixture lookups + mock Nemotron
    python -m intel.demo_run --live    # real lookups + real Nemotron 3 Super (needs NVIDIA_API_KEY)

Mount in P1's FastAPI app:
    from intel import api as intel_api
    app.include_router(intel_api.router)
    intel_api.configure(emit=publish)   # publish(type, call_id, data) -> event bus

Endpoints: POST /intel/ingest · POST /intel/actions/{id}/approve · POST /intel/blocklist/{undo_token}/undo · GET /intel/blocked?number= · GET /intel/state
