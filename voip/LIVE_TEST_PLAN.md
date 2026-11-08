# Live-call test plan (run the minute the Telnyx number is assigned to app `backfire`)
Owner: eng2. Evidence goes to `voip/API_EVIDENCE.md`; raw logs to `.claude/overnight/run-20261107-2330/logs/` (never commit audio).

## 0. Setup (5 min)
1. Hub up with voip mounted: `PUBLIC_WS=wss://<tunnel-host> TARGET_LEGS=self RESTORE_LOW_S=10 uvicorn server.main:app --port 8000` (env from `.env`; SIM_MODE **off**). PUBLIC_WS is required for real calls (the tunnel terminates TLS, so the hub can't infer `wss`).
2. Tunnel: `cloudflared tunnel --url http://localhost:8000`. If the URL changed, PATCH app `backfire` (3088437325215040882) `webhook_event_url=<tunnel>/telnyx/webhook` and the credential connection 3088441327981954669 → **NEEDS LEAD** (config change).
3. `TELNYX_PUBLIC_KEY` set (portal → Keys & Credentials → public key). If missing: real webhooks 403. Fallback for the first call only: `VOIP_ALLOW_UNSIGNED=1`, then remove.
4. Maria's app open, paired (PIN in `logs/device_pin.txt`), WebRTC client registered. Tail `logs/` hub output + `tail -f` the webhook log.
5. Caller = a second phone (judge simulation). Calls the Telnyx number.

## 1. Ordered checks (stop at the first failure; use the fallback, then continue)
| # | Assumption | How to observe | Pass looks like | Fallback if it fails |
|---|---|---|---|---|
| 1 | Webhook reaches us and signature verifies | Call the number; hub log `POST /telnyx/webhook 200`; no 403 | `call.incoming` + `call.routed LIVE_GUARD` on `WS /events` | 403: check `TELNYX_PUBLIC_KEY` (base64 raw 32-byte key), clock skew < 300 s; temporary `VOIP_ALLOW_UNSIGNED=1` |
| 2 | Attestation fields in `call.initiated` | Inspect first webhook payload (hub log at DEBUG / `logs/eng2-webhooks.jsonl` if spike) for `shaken_stir_*` | `attestation` in `call.incoming` is A/B/C (not `none`) for a normal cell caller | Fields absent → record real shape in API_EVIDENCE.md, fix `attestation_of()`; demo toggle: eng1 `/routing/lookup?attestation=` override |
| 3 | `answer` with stream params starts ONE stream | Frames at `/media/{call_id}`: `connected`, `start`, `media` (hub relay stats) | `transcript.caller` appears (P2) while caller speaks | Answer without stream, then `streaming_start` on the caller leg (same params); else TASK-008 fallback B (restart stream at handoff) |
| 4 | Stream is caller-only | Speak on Maria's side only; no `media` energy / no transcript from Maria's words. `track` in frames = `inbound` | Only the caller's voice in decoded μ-law | If both voices appear: stop streaming from conference leg; stream the pre-conference caller leg only; **block the demo until fixed** (rule: never process Maria's audio) |
| 5 | Maria's WebRTC rings + answers | `dial` to `sip:<TELNYX_SIP_USER>@sip.telnyx.com`; her app rings; tap Answer | `call.answered by=maria`, two-way audio caller↔Maria | `from` rejected → set `TELNYX_FROM_NUMBER` to the bought number; SIP creds wrong → re-check connection 3088441327981954669; last resort: dial her real phone number (NEEDS LEAD) |
| 6 | Conference keeps the caller stream alive after Maria joins | After join, keep talking as caller; frames keep arriving | `transcript.caller` continues | Replace conference with Call Control `bridge` (`POST /calls` with `link_to` + `bridge_on_answer`); or restart stream after join |
| 7 | Alert → beeps → Scammer Get Scammed | Trigger `alert.fired` (script card) and tap the button | `user.action`, `handoff.started`; `relay.start_decoy` logs "ok" | If decoy unreachable the handoff aborts and Maria stays (by design); check `P3_DECOY_URL` / echo decoy |
| 8 | **Caller hears the decoy**: `stream_bidirectional_target_legs` | Echo decoy first (built-in): caller hears own voice back ~RTT later after handoff | Caller hears echo; Maria hears nothing | Try `self` (default we send) → `opposite` → `both`; set via `TARGET_LEGS` env and re-call (record winner in API_EVIDENCE.md) |
| 9 | Maria leave/join audio | After handoff, Maria's phone is silent to the caller; caller hears only decoy. Then (restore test) low-risk `risk.update`s for `RESTORE_LOW_S` | `handoff.restored`, Maria talks to the caller again, decoy silent | If `leave` leaves residual audio: also `mute`/`hold` her leg; if rejoin fails the code re-dials her SIP automatically |
| 10 | No audible gap at handoff | Record caller phone side; listen for gap/hold music | gap < ~0.5 s, no music | `beep_enabled` is already `never`; start decoy earlier (we start it before Maria leaves); consider `comfort_noise` |
| 11 | Decoy end → callback rejected pre-ring | Let decoy finish (P3 closes) or hang up as caller; call back from the same number | `call.ended ended_by=decoy` (or caller), `blocklist.updated`, second call gets `reject`, Maria never rings | `curl /routing/lookup?from=<number>` should say BLOCKED_BACKFIRE; check E.164 normalisation (`+1...`) |
| 12 | Limits | 5 quick calls from one number | 5th rejected "Too many calls"; a 5-min call is cut | tune `VOIP_PER_CALLER`, `VOIP_CALL_CAP_S` |

## 2. Latency numbers to record (hub `/demo/latency` + stopwatch)
- ring: caller dials → `call.incoming` event; → Maria's app rings
- first caller word → `transcript.caller` (P2 STT)
- `alert.fired` → beeps on Maria's phone
- tap Scammer Get Scammed → `handoff.started` → first decoy audio heard by the caller (target < 2 s)
- `relay_decoy_rtt_ms`, `relay_p2_send_ms` (sampled)
- restore: low-risk threshold reached → Maria audible (target < 3 s)

## 3. After the first call
Update API_EVIDENCE.md (payload shapes, winning `target_legs`, attestation location), LANE-eng2.md, and tell the lead which fallbacks were used. Remove `VOIP_ALLOW_UNSIGNED`.

## 4. Live results, 2026-11-08 00:11-00:15 (trial account, automated test calls from the scam line to itself)
Evidence for call 1: hub `/events` log (`logs/eng2_events_live.log`). Calls 2-3: reported by lead/eng3, NOT in my logs (I restarted the hub; media frame logging only exists from commit 7376280).
| Check | Status | Evidence |
|---|---|---|
| 1 webhook reaches hub (unsigned mode, VOIP_ALLOW_UNSIGNED=1) | VERIFIED | `call.initiated/answered` POSTs 200 through the tunnel; `call.incoming` + `call.routed LIVE_GUARD` emitted |
| 1b Ed25519 signature | OPEN | no TELNYX_PUBLIC_KEY (portal-only); compensating control added: `GET /calls/{ccid}` must succeed for call.initiated (fail closed) - untested live |
| 2 attestation | OPEN | `attestation: "none"` for this self-call; payload field location still unverified (needs a real PSTN call from another carrier) |
| 3 answer with stream params starts ONE stream | VERIFIED (lead) | media WS `/media/<sid>` connected with token. Frame counts / `connected`+`start` shape NOT captured |
| 4 caller-only audio | OPEN | no frame/track evidence |
| 5 Maria: dial + WebRTC ring + answer | VERIFIED (eng3, via lead) | needed `connection_id = TELNYX_CALL_CONTROL_APP_ID` (cred-connection id -> 422 10015). eng3's page ring + answer seen |
| 5b WS after Maria joined | FAILED (call 2) | media WS 502 during my uvicorn restart; cause = restart, not a code bug (unconfirmed) |
| 6-12 conference keeps stream, handoff, target_legs, leave/join audio, gap, callback rejection, limits | OPEN | blocked: Telnyx disabled outbound/termination on the trial account (D17, balance -0.03), so no further calls |
Findings to carry: (a) POST /calls needs the Call Control App id; (b) trial credit can't be used for termination; (c) trial allows one Call Control app, so our own dialed legs come back through the same webhook - handled (`call.initiated` acted on only for direction=incoming); (d) webrtc-token on trial returns SIP login (device-gated).
Next: on the backup account, re-run from check 3 with `TARGET_LEGS=self`, record media frame counts/track, then 6-12.
