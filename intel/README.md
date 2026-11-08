# intel/ (P4a: real lookups, intel agent, policy gate)

Run from the repo root with the venv active (`pip install httpx pytest`).

Real lookups (needs internet):
    python -m intel.lookups domain example.com
    python -m intel.lookups wallet <btc-or-eth-address>
    python -m intel.lookups allow 1-800-935-9935

Offline tests (no internet):
    python -m pytest -q intel/test_lookups.py
