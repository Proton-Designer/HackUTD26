# P1 runbook: network hub, scam line, Maria's app (simulated carrier network)

All commands run from the repo root. `run_hub` and `point_telnyx` load the repo `.env` first and it OVERRIDES stale shell values. The hub is ONE process: hub + voip (Telnyx scam line) + relay + intel + static `/app` and `/command-center`.

## Env: set / must NOT be set
| var | real demo | note |
|---|---|---|
| `TELNYX_API_KEY` | set (env, never printed/committed) | needed by voip and `point_telnyx --apply` |
| `TELNYX_PUBLIC_KEY` | set | webhook Ed25519 verify; without it webhooks are rejected |
| `TELNYX_CRED_CONNECTION_ID`, `TELNYX_SIP_USER`, `TELNYX_TELEPHONY_CREDENTIAL_ID`, `TELNYX_FROM_NUMBER` | set | Maria's WebRTC leg; voip logs loudly at startup if missing |
| `DEVICE_PIN` | optional | else random 6 digits, printed by `run_hub` and in `logs/device_pin.txt` |
| `P2_BASE`, `P3_BASE`, `P4_BASE` | set to the live pipelines (http://host:port) | status page probes them; relay uses P2_BASE and P3_BASE |
| `NVIDIA_API_KEY` | set (or repo-root `.env`) | intel agent (Nemotron); falls back to baseline rules |
| `PIPELINE_TOKEN` | set (shared with P2/P3/P4, header `x-pipeline-token`) | gates `POST /events` so spoofed risk.update can't trigger restore/legit |
| `HUB_TOKEN` | leave UNSET | browser apps need `WS /events`; device pairing protects the sensitive routes |
| **`SIM_MODE`** | **MUST NOT be set** | with a public tunnel anyone could post `x-sim-call` webhooks that skip signature verification |
| **`VOIP_OPEN_TOKEN`** | **MUST NOT be set** | would mint WebRTC tokens without pairing |
| `DEMO_MODE` / `--fallback` | not set (fallback only) | loops the mock replay |

## Startup order
1. `scripts/run_hub` (starts cloudflared quick tunnel first, exports `PUBLIC_WS`, then the hub). Note the printed **public URL** and **DEVICE PIN**.
2. LEAD: `scripts/point_telnyx` (dry run, check the URL), then `scripts/point_telnyx --apply`; it PATCHes the Call Control app and the credential connection and prints the stored URLs (all must say OK).
3. Open `<public URL>/demo/status`: hub up, voip mounted, P2/P3/P4 `up` or mounted, `SIM_MODE` false, `HUB_TOKEN_set` false.
4. Open Maria's app on her phone at `<public URL>/app/`.

## Pairing Maria's phone (once per device)
First run shows "Enter the code shown on the demo screen": type the DEVICE PIN printed by `run_hub`. The app stores a device token; it sends `x-device-token` on the protection log, buttons and WebRTC token. 5 wrong tries per minute locks that source out; the operator on the hub machine can still pair directly on localhost. A new PIN is generated each hub restart, but already-paired phones stay paired.

## Pre-demo checklist
- [ ] `/demo/status` all green (above), `logs/latency.jsonl` writable.
- [ ] `scripts/point_telnyx --apply` printed `OK` for both URLs after the LAST tunnel restart.
- [ ] Maria's phone paired, Live Guard on, voice enrolled (or skipped).
- [ ] Test call from a teammate's phone to the Backfire number: call.incoming/routed on `/command-center`, Maria's phone rings, alert fires.
- [ ] `scripts/reset_demo <public URL>` (< 30 s) so the blocklist and intel store are clean.
- [ ] Keep `scripts/run_hub --fallback` ready in a second terminal (use a different `HUB_PORT`).

## Reset between judges
`scripts/reset_demo` (local) or `scripts/reset_demo <public URL>` (needs `x-hub-token` only if `HUB_TOKEN` is set). It clears hub calls/blocklist and the intel store and re-seeds the trusted bank number. It does NOT touch Telnyx or Maria's pairing.

## When X fails
| failure | do |
|---|---|
| Tunnel dies / URL changes | stop `run_hub`, start it again, then `scripts/point_telnyx --apply`, re-open `/app/` with the new URL on the phone (pairing survives) |
| Telnyx down / no number / no credit | `scripts/run_hub --fallback`: looped replay of the IRS/bank/benign stories on `/app/` and `/command-center/`, no telephony. Say it is a replay. |
| voip failed to import | hub still starts (see `logs/hub.log`); `/demo/status` shows voip `not mounted`; use fallback |
| P2/P3 unreachable | `/demo/status` shows `unreachable`; calls still connect (fail open); decoy start returns false and Maria keeps the call |
| Intel failed to import | hub falls back to the P1 decoy-ended blocklist stub; `/demo/status` shows P4 `not mounted` |
| Phone cannot pair (locked out) | wait a minute, or pair from the hub machine on localhost |
| Need a no-phone rehearsal | `SIM_MODE=1 NO_TUNNEL=1 scripts/run_hub` then `.venv-hub/bin/python scripts/sim_call.py --from +15555550123 --wav logs/sim_scam.wav` (make the WAV with `scripts/make_scam_wav.sh`). Never with a public tunnel. |

## Where things are
`logs/hub.log`, `logs/tunnel.log`, `logs/latency.jsonl`, `logs/tunnel_url.txt`, `logs/device_pin.txt` (all gitignored). Latency summary: `/demo/latency`.
