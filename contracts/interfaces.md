# Backfire interfaces (v1, owned by P1)

All HTTP/WS paths hang off the P1 hub base URL (public tunnel in demo). Audio everywhere = Telnyx media-streaming format: **PCMU (mu-law) 8 kHz mono, base64 payload**, 20 ms frames (160 bytes).

## Hub (P1)
- `WS /events`: broadcasts every event envelope (see events.md). Optional `?call_id=` filter. No auth in demo.
- `POST /events`: `{type, call_id, ts?, data}` publishes an event from another pipeline (P2/P3/P4). Response `{"ok":true}`. (ts defaults to now.)
- `GET /routing/lookup?from=+1555...` -> `{"decision":"NORMAL|BLOCKED_BACKFIRE|LIVE_GUARD","reason":"...","attestation":"A|B|C|none"}` in under 50 ms. Optional `&attestation=A`.
- `POST /user/action` `{call_id, action}` -> publishes `user.action`. `{"ok":true}`
- `POST /intel/ingest` (P1 stub, logs only; P4 later) `{call_id, scammer_transcript, artifacts[]}` -> `{"ok":true,"stub":true}`
- `GET /protection-log` -> `{"blocked":[{number,reason,ts,undo_token}],"calls":[...]}`; `POST /protection-log/undo {undo_token}` -> `{"ok":true}`
- `GET /healthz` -> `{"ok":true}`

## P2 detection
- `POST /detect` `{call_id, window_text, metadata, engine:"cloud|local"}` -> typed risk JSON = the `risk.update` data fields (s, band, asks, scam_type, stage, impersonates, addresses_ai_system, why_chips, engine).
- **Caller audio seam (PROPOSED, P2 confirm):** P1 connects as a WS client to `WS /stt/{call_id}` on P2 and forwards the Telnyx frames verbatim (`connected`/`start`/`media`/`stop` JSON, payload PCMU 8 kHz base64, caller track only). P2 emits `transcript.caller`, `risk.update`, `alert.fired` via `POST /events` (or in-process publish if mounted on the hub). Alternative if P2 prefers: in-process `feed_audio(call_id, pcmu_bytes)` when mounted in the hub app.

## P3 decoy
- `WSS /decoy/{call_id}`: Telnyx media-streaming protocol, bidirectional. **P1 is the client**: after handoff it sends `connected`, `start` (with `streamSid`/`stream_id`, `call_id` as custom parameter and in the path), then `media` frames caller->decoy; P3 returns `media` (PCMU 8 kHz base64), `mark`, `clear`. P1 relays them to the caller's leg.
- `POST /voice/enroll` `{recording (base64 or multipart), consent_version}` -> `{"voice_id":"..."}`; emits `voice.enrolled`.
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
