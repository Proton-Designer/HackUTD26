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

Mount in P1's hub (server/main.py), 3 lines:
    from intel import api as intel_api
    app.include_router(intel_api.router)                       # replaces the /intel/ingest stub
    intel_api.configure(emit=bus.publish); bus.add_observer(intel_api.observe)

`observe` runs the chain on `artifacts.extracted` in a background thread (calling number + attestation come from
`call.incoming`). If a decoy call ends and no artifacts arrive within INTEL_EXTRACT_GRACE (20 s), it still blocks the
caller for her. Routing: `intel.store.is_blocked(number) -> (bool, reason)`. Protection log:
`intel_api.protection_entries()` / `intel_api.undo_block(token)`. Key: NVIDIA_API_KEY from env or repo-root .env.
Model: INTEL_MODEL (default nvidia/nemotron-3.5-super-vl-120b-a12b).

Rehearsal reset (idempotent, ~5 ms, no network): `python -m intel.seed_demo` clears the intel DB and seeds one
synthetic sighting from "yesterday" sharing the demo wallet + callback, so the judge's call confirms the campaign live.
`--check` prints counts only.

Demo values (domain, wallet, callback, numbers) live in intel/demo_config.json; swap with
BACKFIRE_DEMO_DOMAIN=... BACKFIRE_DEMO_WALLET=... (env) or edit the JSON. Placeholders until the team picks real ones.

Acceptance checklist against a running hub (exit 0 = all pass):
    python -m intel.acceptance --hub http://127.0.0.1:8000 [--token $HUB_TOKEN] [--domain <demo domain>] [--wallet <demo BTC>]

Fail-open drill: start the hub with INTEL_RDAP_BASE=http://10.255.255.1 INTEL_BTC_BASE=http://10.255.255.1, then
    python -m intel.acceptance --hub <url> --drill   (lookups show 'unavailable'; gate checks must still pass)

Endpoints: POST /intel/ingest · POST /intel/actions/{id}/approve · POST /intel/blocklist/{undo_token}/undo · GET /intel/blocked?number= · GET /intel/state

Events: superset of contracts/events.md (required fields present; extras such as gate_status, n_baseline_added are
ignorable). intel.action.status is applied|queued|approved, plus denied|held (proposed to P1). Extra P4 trace events:
intel.plan, intel.agent, intel.proposals.
