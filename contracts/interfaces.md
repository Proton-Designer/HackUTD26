# Backfire interfaces (v1, owned by P1)

All HTTP/WS paths hang off the P1 hub base URL (public tunnel in demo). Audio everywhere = Telnyx media-streaming format: **PCMU (mu-law) 8 kHz mono, base64 payload**, 20 ms frames (160 bytes).

## Hub (P1)
- `WS /events`: broadcasts every event envelope (see events.md). Optional `?call_id=` filter. No auth in demo.
- `POST /events`: `{type, call_id, ts?, data}` publishes an event from another pipeline (P2/P3/P4). Response `{"ok":true}`. (ts defaults to now.)
- `GET /routing/lookup?from=+1555...` -> `{"decision":"NORMAL|BLOCKED_BACKFIRE|LIVE_GUARD","reason":"...","attestation":"A|B|C|none"}` in under 50 ms. Optional `&attestation=A`.
- `POST /user/action` `{call_id, action}` -> publishes `user.action`. `{"ok":true}`
- `POST /intel/ingest` (P1 stub, logs only; P4 later) `{call_id, scammer_transcript, artifacts[]}` -> `{"ok":true,"stub":true}`
- `GET /protection-log` -> `{"blocked":[{number,reason,ts,undo_token}],"calls":[{call_id,from_number,decision,reason,ts}]}` (`decision` = NORMAL|BLOCKED_BACKFIRE|LIVE_GUARD, `ts` unix seconds, newest first, max 50); `POST /protection-log/undo {undo_token}` -> `{"ok":true}`
- `GET /app/` serves `web/customer/` static (same origin as the hub, for the phone via tunnel).
- `GET /healthz` -> `{"ok":true}`

## P2 detection
- `POST /detect` `{call_id, window_text, metadata, engine:"cloud|local"}` -> typed risk JSON = the `risk.update` data fields (s, band, asks, scam_type, stage, impersonates, addresses_ai_system, why_chips, engine).
- **Caller audio seam (PROPOSED, P2 confirm):** P1 connects as a WS client to `WS /stt/{call_id}` on P2 and forwards the Telnyx frames verbatim (`connected`/`start`/`media`/`stop` JSON, payload PCMU 8 kHz base64, caller track only). P2 emits `transcript.caller`, `risk.update`, `alert.fired` via `POST /events` (or in-process publish if mounted on the hub). Alternative if P2 prefers: in-process `feed_audio(call_id, pcmu_bytes)` when mounted in the hub app.

## P3 decoy
- `WSS /decoy/{call_id}`: Telnyx media-streaming protocol, bidirectional. **P1 is the client**: after handoff it sends `connected`, `start` (with `streamSid`/`stream_id`, `call_id` as custom parameter and in the path), then `media` frames caller->decoy; P3 returns `media` (PCMU 8 kHz base64), `mark`, `clear`. P1 relays them to the caller's leg.
- `POST /voice/enroll` JSON body `{"recording": "<base64 of the audio bytes, no data: prefix>", "mime": "audio/webm" | "audio/ogg" (as recorded by MediaRecorder), "consent_version": "v1"}` -> `{"voice_id":"..."}`; emits `voice.enrolled`.
- `DELETE /voice/{voice_id}` -> `{"ok":true}`; emits `voice.deleted`.

## P4
- `POST /intel/ingest` (P4 replaces the stub), `POST /intel/actions/{id}/approve` -> `{"ok":true,"status":"approved"}`.

## Media relay seam (Option A, INSTRUCTIONS section 2)
```
caller leg --(one Telnyx bidirectional stream, inbound_track, PCMU 8k)--> P1 WS /media/{call_id}
P1 --> P2 /stt/{call_id}   (always, caller frames)
after handoff: P1 --> P3 WSS /decoy/{call_id} (caller frames), P3 media/clear --> P1 --> Telnyx stream --> caller hears decoy
```
Never use forking. Maria's audio is never streamed. Fail open: if the relay breaks the call stays connected.

### Media relay seam (TASK-013, `server/relay.py`; voip/ calls it in-process)
All async, none raises, none blocks on P2/P3 (bounded queues, drop on full).
- `await relay.open(call_id, send_to_caller, on_decoy_lost=None)`; `send_to_caller(frame: dict)` writes a Telnyx `media`/`clear`/`mark` frame to the Telnyx WS.
- `await relay.caller_frame(call_id, frame)` for EVERY Telnyx frame (`connected`/`start`/`media`/`stop`; dict or JSON str). Always forwarded verbatim to P2 (`P2_STT_URL` -> `WS /stt/{call_id}`; or in-process `relay.feed_audio_hook(call_id, frame)`). After `start_decoy`, `media`/`stop` also go to P3. Media whose `track` is not `inbound` is dropped (Maria's audio never enters).
- `await relay.start_decoy(call_id) -> bool`: connects to `P3_DECOY_URL` -> `WSS /decoy/{call_id}` (unset: built-in echo decoy `/decoy-echo/{call_id}` on the hub), sends `connected` + `start` (stream_id = Telnyx stream id, `custom_parameters.call_id`). P3 `media`/`clear`/`mark` -> `send_to_caller`. False = P3 unreachable (decoy not started; call unaffected).
- `await relay.stop_decoy(call_id)`, `await relay.close(call_id)`. `on_decoy_lost(call_id)` fires if P3 drops mid-call (voip may restore Maria).
- Latency: `relay_decoy_rtt_ms` (caller frame -> decoy reply) and `relay_p2_send_ms`, sampled, in `logs/latency.jsonl` / `GET /demo/latency`.

### Device pairing (TASK-014)
- `POST /pair {"pin":"123456"}` -> `{"device_token":"..."}` (401 wrong pin; 429 after 5 failures/min per IP or 30 total). PIN = env `DEVICE_PIN` or random 6 digits at hub start, printed by `scripts/run_hub` and in `logs/device_pin.txt`.
- Header `x-device-token: <token>` is required on `GET /protection-log`, `POST /protection-log/undo`, `POST /user/action` and `GET /voip/webrtc-token` (via `Depends(server.device.require_device)`). Direct loopback requests (no proxy headers) and `x-hub-token == HUB_TOKEN` also pass. Requests arriving through the tunnel are always remote. `WS /events`, `/app`, `/command-center` stay open (read-only).
