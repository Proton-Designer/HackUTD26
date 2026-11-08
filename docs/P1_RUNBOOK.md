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
`scripts/reset_demo` (local) or `scripts/reset_demo <public URL>` (needs `x-hub-token` only if `HUB_TOKEN` is set). It clears hub calls/blocklist and the intel store and re-seeds the trusted bank number. It does NOT touch Telnyx or Maria's pairing. As of TASK-021 the same reset also runs `intel.seed_demo` in-process (hub's own intel DB) and prints the `--check` summary (expect 1 campaign, all else 0) plus the routing check for the judge number (must be `LIVE_GUARD`); `POST /demo/reset?seed=0` skips seeding. Details: `data/RESET.md` (P4a's doc).

## Phone-free demo (no Telnyx; SIM_MODE)
Use when Telnyx is down/blocked. Same real path as a live call (hub routing -> P2 relay, transcripts, alert -> Maria's page -> tap -> handoff to the decoy -> call.ended -> Nemotron intel block); only the caller is a local fake and voip sends no Telnyx request (it logs `sim: would <cmd>`).
1. Hub with `SIM_MODE=1` (same tunnel is fine): `set -a; . ./.env; set +a; SIM_MODE=1 PUBLIC_WS=wss://<tunnel host> .venv-hub/bin/python -m uvicorn server.main:app --host 127.0.0.1 --port 8000`. Unsigned sim webhooks and sim `/media` are accepted ONLY from a direct loopback client (no cf-/x-forwarded headers); anything via the tunnel still needs a valid Telnyx signature. Do not set `HUB_TOKEN` (it would also gate P2's `/events` posts and browsers).
2. Demo audio (~58 s, synthetic IRS card, the file BOTH the page `GET /demo/caller.wav` and the fake caller use): `voip/.venv/bin/python voip/test_call.py --script irs --wav-out logs/sim_scam.wav` (needs macOS `say` + ffmpeg; env `DEMO_CALLER_WAV` overrides the path).
3. Open Maria's page on the hub (`/app/?sim=1` or it auto-detects SIM_MODE), paired as usual.
4. One command from the hub machine: `scripts/demo_call --reset` (resets blocklist/events first; `--hub URL`, `--from +1555...`, `--wav f`, `--script irs|bank|crypto|benign`, `--wait-intel N`). Tap the on-screen button after the alert. It prints a timeline (seconds from call start): incoming, answered, alert, tap, handoff, ended, intel, blocklist. Expect: alert ~10 s, handoff right after the tap, decoy echo frames back, `call.ended` ~58 s, `blocklist.updated` ~20 s later.
5. Between runs: `scripts/demo_call --reset` again (or `scripts/reset_demo`). Say on stage that the caller is simulated.
Restore variant: `--script benign` + tap, then hold low risk 10 s (`RESTORE_LOW_S=10`): `handoff.restored`, no block.

## When X fails
| failure | do |
|---|---|
| Tunnel dies / URL changes | stop `run_hub`, start it again, then `scripts/point_telnyx --apply`, re-open `/app/` with the new URL on the phone (pairing survives) |
| Telnyx down / no number / no credit | `scripts/run_hub --fallback`: looped replay of the IRS/bank/benign stories on `/app/` and `/command-center/`, no telephony. Say it is a replay. |
| voip failed to import | hub still starts (see `logs/hub.log`); `/demo/status` shows voip `not mounted`; use fallback |
| P2/P3 unreachable | `/demo/status` shows `unreachable`; calls still connect (fail open); decoy start returns false and Maria keeps the call |
| Intel failed to import | hub falls back to the P1 decoy-ended blocklist stub; `/demo/status` shows P4 `not mounted` |
| Phone cannot pair (locked out) | wait a minute, or pair from the hub machine on localhost |
| Need a no-phone rehearsal | `SIM_MODE=1 NO_TUNNEL=1 scripts/run_hub` then `.venv-hub/bin/python scripts/sim_call.py --from +15555550123 --wav logs/sim_scam.wav` (make the WAV with `scripts/make_scam_wav.sh`). With a public tunnel too: sim is loopback-only (see Phone-free demo). |

## Where things are
`logs/hub.log`, `logs/tunnel.log`, `logs/latency.jsonl`, `logs/tunnel_url.txt`, `logs/device_pin.txt` (all gitignored). Latency summary: `/demo/latency`.

`scripts/run_hub` env precedence: repo `.env` overrides stale inherited vars (old TELNYX_* in tmux shells) EXCEPT run-control vars you set explicitly in the shell (HUB_PORT HUB_BIND HUB_DB INTEL_DB LOGDIR HUB_NO_PIN_FILE DEVICE_PIN HUB_TOKEN NO_TUNNEL SIM_MODE DEMO_MODE FALLBACK FALLBACK_DETECT, plus anything in `RUN_HUB_KEEP=VAR1,VAR2`), so isolated test copies keep their own values. `POST /demo/reset` and `/demo/replay` need direct localhost, a paired device, or `x-hub-token` (remote without one = 401).

`GET /demo/caller.wav` (no auth, audio only) serves the synthetic scammer WAV for the phone-free demo: env `DEMO_CALLER_WAV`, else `$LOGDIR/sim_scam.wav` (made by `scripts/make_scam_wav.sh`, the same file `sim_call.py --wav` streams); 404 until it exists; Range supported.

`scripts/preflight [--live] [--tunnel URL] [--no-tunnel]` (read-only, stdlib, no Telnyx calls) prints PASS/FAIL and exits 1 on any FAIL: hub /healthz local + tunnel; /demo/status (SIM_MODE on for phone-free, off with --live; intel_engine nemotron; NVIDIA_API_KEY_set; P2 reachable via P2_STT_URL/P2_BASE; telnyx_ok not false); /demo/caller.wav 200 + duration; /app/ and /app/judge.html via the tunnel; WS /events handshake; demo fresh (judge number LIVE_GUARD, protection log empty). Tunnel URL from --tunnel, $PUBLIC_URL, or logs/tunnel_url.txt. Run it right after scripts/reset_demo.

`WS /listen/{call_id}` (phone-free demo audio for judges): text frames `{"track":"caller"|"decoy","payload":<base64 PCMU 8k, 20 ms>}` fanned out from the relay (caller inbound + decoy->caller only; Maria never). Auth before accept: direct loopback, or a paired device token sent as WebSocket subprotocols `["bf-device", <token>]` (never in the URL; hub accepts with `bf-device`), or `x-hub-token`; else close 1008. Max 3 listeners (4th gets close 1013); a slow listener drops frames, or is closed if its socket stalls 1 s. Default decoy for the built-in relay is the voip stand-in persona (`/decoy-standin`); `DECOY_STANDIN=echo` restores the echo.

- Do Not Screen list: `GET/POST /trusted`, `DELETE /trusted/<number>` (device-authed; E.164 validated; same table routing uses for trusted+A NORMAL). Fallback detector: gov agency + arrest/warrant floors the regex score at 0.82; one retry on NVIDIA 429.

- WS /talk/{call_id} (MARIA_LEG=talk, role-play demos): same auth as /listen (subprotocols ["bf-device", token] or loopback same-origin), call known on the bus and voip.talk_enabled(call_id); one talker per call; JSON {payload: b64 PCMU 8k, 160 B = 20 ms, up to 960 B} or binary 160 B multiples; <=60 frames/s; dropped while the decoy has the call. Maria's audio goes only to voip.inject_maria (caller leg), never to P2/P3, never stored or logged.

- Restart guard: `scripts/restart_hub_safe [--check] [--force]` refuses (exit 2, prints call-id prefixes) while /demo/status flags.active_calls>0 (calls with an open media session; last_call_activity_ts shows recency), then stops the listener and execs run_hub. Use it instead of killing/restarting the hub by hand.

- Customer display name: env `CUSTOMER_NAME` (default `Maria`, empty = no name) -> `/demo/status` flags.CUSTOMER_NAME, page title + judge card text, and the listen/talk greeting ("Hello? ... Yes, this is <name>." / "Hello?"). Event enums (`by:"maria"`) are unchanged. Restart the hub after changing it; the greeting audio re-synthesizes on the first call.

- `POST /demo/reset` (and `scripts/reset_demo`, `demo_call --reset`) is refused with 409 while a call is live (`active_calls>0`); `?force=1` / `scripts/reset_demo <hub> --force` overrides.

- `EVENTS_REDACT=1`: WS /events gives remote viewers that are neither loopback nor paired (subprotocol ["bf-device", token], x-device-token, x-hub-token) a redacted stream: no transcript text, no extracted artifacts, phone numbers masked. Default OFF: customer app and command center connect unauthenticated today, so enable it only after the customer app sends the subprotocol (and the command-center is viewed on the hub machine).

- `VOICE_LOCK=1` (in .env): paired devices get 409 "voice is locked for the demo" on `DELETE /voice/*` and `POST /voice/enroll`; the operator on the hub machine (direct loopback, same-origin) can still manage voices. `scripts/ready_check` FAILs if the decoy reports `cloned_voice:false`. Takes effect on hub restart; to re-enroll the demo voice, do it from this Mac or unset it.
