# P1 release notes: frozen build (network hub + scam line + customer app)

Tag with `scripts/freeze_tag` (dry run by default, `--yes` to push). Rollback: `git checkout p1-known-good-<HHMM>`, then `scripts/restart_hub_safe`, `scripts/ready_check`. Operator steps: `docs/DEMO_DAY_RUNBOOK.md`; env/endpoints: `docs/P1_RUNBOOK.md`; second client: `docs/CLIENT_API.md`; events: `contracts/events.md`.

## What is in the build
- **One hub process** (`server/`): routing (emergency, confirmed, campaign, intel block, trusted+A, LIVE_GUARD; fails open), event bus + `WS /events`, voip (Telnyx scam line), intel (P4a), android_voip bridge (optional, fail open), static `/app` (customer PWA) and `/command-center`.
- **Live call path**: Telnyx webhook -> media WS -> relay -> P2 (detection) with reconnect (2 s x3, then 10 s), alert (duplicate alerts dropped), customer taps -> decoy (P3, falls back to the built-in stand-in if P3 is down) -> hang-up -> intel block. `handoff.failed` if no decoy can start.
- **Customer modes** (`MARIA_LEG`): `sip` (WebRTC leg), `listen` (hear the caller and decoy over `WS /listen`), `talk` (customer speaks over `WS /talk`, muted while the decoy has the call). `SIM_MODE` phone-free demo (`scripts/demo_call`).
- **Customer actions**: `POST /user/action` continue / scammer_get_scammed / hang_up / answer / decline (answer/decline only while ringing).
- **Pairing and auth**: PIN -> device token; loopback requires same-origin; `/talk`, `/listen`, device events use the `["bf-device", token]` subprotocol; reconnects from the same device replace the old socket; a restart or `/demo/reset` never un-pairs a phone.
- **Do Not Screen list** (`/trusted`), **voice enrollment** (`/voice/enroll`, webm/ogg/wav/mp4; falls back to a synthetic voice, audio never stored without P3), protection log + undo.
- **Device-side detection**: a paired device attached to a live call may post `risk.update` / `transcript.caller` with `engine:"device"` (validated, rate-limited, nothing else).
- **Fallback detector** (`FALLBACK_DETECT=1`): regex + Nemotron, gov-agency + arrest floor 0.82, one retry on 429.
- **Ops**: `/demo/status` flags (incl. `active_calls`, `active_calls_detail` for paired/loopback only), `/demo/reset` (refused while a call is live; `?force=1`), `scripts/restart_hub_safe` (refuses during a call, reuses the tunnel), `scripts/preflight`, `scripts/ready_check`, `logs/p2_tunnel_url.txt` (P2 URL re-read per connect, no restart), PWA headers (no-cache html/js/css, manifest type).
- **Config**: `CUSTOMER_NAME` (default "Maria"; empty = no name) shown in the app title, judge card and greeting. Judge cards in `data/script-cards.md` (first card = "Judge card (use this one)").

## Env expected on the live hub
| var | live value |
|---|---|
| `SIM_MODE`, `VOIP_OPEN_TOKEN`, `DEMO_MODE`, `HUB_TOKEN` | unset |
| `MARIA_LEG` | `talk` (or `listen` / `sip`) |
| `DEVICE_PIN`, `TELNYX_*` (API key, public key, app/connection/SIP/credential ids), `NVIDIA_API_KEY`, `NESSIE_API_KEY` | set in `.env` (never printed) |
| `P2_STT_URL` (or `P2_BASE`), `P3_DECOY_URL` + `P3_VOICE_URL` (decoy on `127.0.0.1:8300`) | set |
| `PIPELINE_TOKEN` | same value as on P2/P3 |
| `PUBLIC_WS` | set by `run_hub`/`restart_hub_safe` from the running tunnel |
| `CUSTOMER_NAME` | optional |
| `FALLBACK_DETECT` | `1` if P2 is flaky (needs restart) |
| `EVENTS_REDACT` | unset (see limits) |

## Known limits
- **Unverified live**: real Telnyx behaviour of `talk`/`listen` end to end on a phone, answer/decline wiring in voip (needs `call.answered` on success), a real browser on `/listen`, the preflight tunnel-403 PASS path.
- **Single customer**: every paired device is one customer's phone; no per-customer binding. Any paired device can call `/demo/reset` and `/trusted`.
- **`EVENTS_REDACT` is off**: `WS /events` over the tunnel shows transcripts and numbers to anyone with the URL until the customer app sends the subprotocol and the command center is viewed locally.
- **No Telnyx cleanup on restart (F21)**: a hub restart mid-call drops the call; use `restart_hub_safe`.
- **NVIDIA quota is shared**: P2/P3/intel/fallback all draw on it; 429s degrade to rules / canned lines. One rehearsal at a time.
- **iOS**: the page must stay open with the screen on; mic needs earphones (echo).
- **Hub is one process**: a crash drops live calls; P2 or P3 outages fail open (calls connect, alerts/decoy lost).
- `PIPELINE_TOKEN` unset would leave `POST /events` open (repo is public): keep it set.
