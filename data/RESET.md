# Rehearsal reset (between judges)

Run on the **hub machine**, from the repo root, venv active. `seed_demo` writes the hub's intel DB
(`INTEL_DB`, default `intel/intel.db`), so it must run on the same machine as the hub.
Order matters: the hub reset also wipes the intel tables, so seed **after** it.

```bash
export HUB=http://127.0.0.1:8000          # the hub's local URL (not the tunnel)

# 1. Hub reset: calls, bus, routing lists, intel tables
curl -s -X POST -H "x-hub-token: $HUB_TOKEN" $HUB/demo/reset; echo

# 2. Seed yesterday's sighting (same wallet + callback as the script cards)
python -m intel.seed_demo

# 3. Check
python -m intel.seed_demo --check
curl -s "$HUB/routing/lookup?from=%2B12145550199"; echo
```

## Expected output

```
{"ok":true,"seconds":0.003}
intel DB reset + seeded in 2 ms -> .../intel/intel.db
  campaign camp-xxxxxx: observed, 1 sighting (caller +1 469 555 0100, seed-carrier, <yesterday>)
  shared indicators: wallet:1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa, callback_phone:8885550123
  next: the judge's call with this wallet or callback = sighting #2 -> campaign confirms live
  Nessie: pending $1,800 'Zelle to refunds.dept@backfire-demo.example' from Maria (scripted, mock bank)
{'campaigns': 1, 'queue': 0, 'actions': 0, 'denied': 0, 'blocklist': 0, 'callback_warnings': 0, 'holds': 0, 'immunity': 0}
{"decision":"LIVE_GUARD","reason":"Caller ID not verified","attestation":"none"}
```

Good state: exactly **1 campaign**, everything else **0**, and the judge number (`+1 214 555 0199`, synthetic) routes
`LIVE_GUARD`, not `BLOCKED_BACKFIRE`. If it says `BLOCKED_BACKFIRE`, step 1 didn't run (wrong `$HUB` or token).
While the demo values are still placeholders, `seed_demo` adds `(PLACEHOLDER values: ...)` to its first line.
That's expected until the real domain and wallet are set (env `BACKFIRE_DEMO_DOMAIN` / `BACKFIRE_DEMO_WALLET`, or
`intel/demo_config.json`; then refill `data/script-cards.md` with the same values).

Note: `POST /demo/reset` now seeds intel itself (P1, 79cd0f2) and starts Maria's pending Nessie transfer, so step 2 is
redundant on the hub (harmless to run). Nessie needs a one-time `python -m intel.seed_nessie` and NESSIE_API_KEY in .env;
without them the Nessie line says "skipped" and everything else is unchanged. With Nessie the reset takes 0.18-0.31 s (3 s worst
case if Nessie is unreachable).

## Timing (must be under 60 s)

Measured 2026-11-08 on Kareem's MacBook Air against a local hub (`NO_TUNNEL=1 HUB_PORT=8767 scripts/run_hub`), full
sequence 1-3 wall-clock:

| Run | Total |
|---|---|
| 1 | 0.15 s |
| 2 | 0.12 s |

## Optional full check (about 6 s, uses live Nemotron + real lookups; adds test rows, so reset again after)

```bash
python -m intel.acceptance --hub $HUB --token "$HUB_TOKEN" --require-nemotron   # expect 7/7; 2a must say engine=nemotron
```
