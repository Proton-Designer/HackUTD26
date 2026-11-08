# Backfire hub: client API (a second client acting as the customer)

For Evan's native Android app (or any client) acting as the protected customer on a live Telnyx call. Everything here is served by the one hub process (`<HUB>` = `https://<tunnel>` or `http://127.0.0.1:8000`; use `wss://` / `ws://` for sockets). Event shapes: `contracts/events.md`. The customer's display name (default "Maria") is hub flag `CUSTOMER_NAME`; enum values such as `by:"maria"` never change.
The hub is single-customer: every paired device is one of that customer's phones, and there is no per-customer binding (out of scope for the demo). Never log tokens, PINs or audio. All demo data is synthetic. Everything the hub does for a call fails open: if your client is gone the call still connects.

## 1. Pair (once per device)
`POST /pair` `{"pin":"<DEVICE_PIN shown by the operator>"}` -> `200 {"device_token":"<opaque>"}`. Store it securely; it survives hub restarts and demo resets.
Errors: `401` wrong PIN, `429` too many wrong tries (5 per minute per IP, 30 global; wait a minute).
Send the token as header `x-device-token: <token>` on every HTTP call below. For WebSockets from a browser-like stack that cannot set headers use the subprotocol form (section 4); a native client may also use the header.

## 2. Read hub state
- `GET /demo/status?format=json` (no auth): `flags` incl. `SIM_MODE`, `MARIA_LEG` (`sip` | `listen` | `talk`), `CUSTOMER_NAME`, `FALLBACK_DETECT`, `telnyx_ok`, `active_calls` (count). Use `MARIA_LEG` to know whether your client must dial/answer a SIP leg (`sip`) or only listens/talks over the hub sockets (`listen`/`talk`).
- `GET /healthz` -> `{"ok":true}`.
- `GET /voip/webrtc-token` (device token): `{"token":"<jwt>"}` for the Telnyx WebRTC login in `sip` mode (or `{"login","password"}` on trial accounts); `502` if unavailable.

## 3. Events: `WS /events`
`GET /events?call_id=<id>` upgrades to a WebSocket (omit `call_id` for all calls). No auth unless the operator set `HUB_TOKEN` (then `?token=<HUB_TOKEN>`). The hub sends only JSON envelopes `{"type","call_id","ts","data"}`; history is not replayed (connect before the call, or at `call.incoming`).
Types a customer client needs:
| type | data (key fields) | client action |
|---|---|---|
| `call.incoming` | `from`, `to`, `attestation`, `scam_id_score` | hold; do not ring yet (a blocked call is never delivered) |
| `call.routed` | `decision` (`NORMAL` / `LIVE_GUARD` / `BLOCKED_BACKFIRE`), `reason` | `LIVE_GUARD` or `NORMAL`: ring now; `BLOCKED_BACKFIRE`: never ring |
| `call.answered` | `by:"maria"`, optional `via` | the customer picked up |
| `transcript.caller` | `utterance_id`, `text`, `is_final` | optional live captions (caller side only) |
| `risk.update` | `s` 0-1, `band` low/watch/high/critical, `asks[]`, `scam_type`, `stage`, `impersonates`, `why_chips[]`, `engine` | drive the risk badge; label `engine:"fallback"` / `"device"` as such |
| `alert.fired` | `level` `first`/`realert`, `why_chips[]` | two beeps + red alert; show the three buttons |
| `handoff.started` / `handoff.restored` | - | decoy has the caller / customer has the line again |
| `call.ended` | `ended_by`, `duration_s`, optional `legit` | tear down |
| `blocklist.updated`, `intel.*` | - | optional protection-log refresh |
Ignore unknown types and fields.

## 4. Audio sockets
Both share auth: header `x-device-token`, **or** WebSocket subprotocol list `["bf-device","<token>"]` (the hub accepts with `bf-device` only; the token is never echoed and must not go in the URL). A bad/absent token, an unknown `call_id`, or (`/talk`) a call not in talk mode closes with `1008` before accept. The call must be known to the hub: attach as soon as `call.incoming` is on `WS /events` (before media exists).
**Reconnects:** a new connection from the same paired device REPLACES that device's old socket for the call (old gets close `1000`). A different device is refused (`1013`).

### `WS /listen/{call_id}` (hear the call)
Server -> client text frames: `{"track":"caller"|"decoy","payload":"<base64 PCMU 8 kHz mono, 160 bytes = 20 ms>"}`. `caller` = the scammer's inbound audio; `decoy` = what the decoy says to the scammer after handoff. The customer's own voice is never in this stream. Client sends nothing (any text is ignored). Max 3 listeners across the hub (the 4th gets `1013`). A listener that cannot take a frame within 1 s is dropped; closed after 5 min with no frames and when the call ends.

### `WS /talk/{call_id}` (speak; only when `MARIA_LEG=talk`)
Client -> server frames, either JSON text `{"payload":"<base64 PCMU 8 kHz mono>"}` or a binary message; each message must be a whole number of 20 ms frames (160 bytes, up to 960 bytes = 6 frames). Server sends nothing back. Rules: **one talker per call**; rate limit **60 frames/s** (excess is dropped silently, not queued); frames are **dropped while the decoy has the call** (after `handoff.started` until `handoff.restored`) and while the stream is not up; invalid frames are dropped, the socket stays open. Mic audio goes only to the caller leg: never to detection or storage. The socket closes after 5 min of silence or when the call ends. Encode G.711 mu-law, 8000 Hz, mono, 20 ms per frame.

## 5. Acting on a call
- `POST /user/action` `{"call_id","action"}` with `action` in `continue` | `scammer_get_scammed` | `hang_up` -> `{"ok":true}`; `404` unknown call, `401` unpaired. `scammer_get_scammed` triggers the decoy handoff (`handoff.started` appears on `WS /events`).
- `GET /protection-log` -> `{"blocked":[{"number","reason","ts","undo_token"}],"calls":[...]}`; `POST /protection-log/undo` `{"undo_token"}` -> `{"ok":true|false}`.
- Do Not Screen list: `GET /trusted` -> `{"trusted":[{"number","label"}]}`; `POST /trusted` `{"number":"+15555550123","label":"Dr. Lee"}` (E.164 required, else `422`; label <= 60 chars); `DELETE /trusted/{number}` (URL-encode the `+`; always `{"ok":true,"removed":bool}`).
- Voice: `POST /voice/enroll` `{"recording":"<base64>","mime":"audio/mp4","consent_version":"v1"}` -> `{"voice_id":"..."}`, or `{"voice_id":null,"fallback":"synthetic","reason":...}` when no voice service is connected (the audio is then discarded; show "your voice wasn't saved, a synthetic voice is used"). Accepted: webm, ogg, wav, mp4/m4a/aac (mime params like `;codecs=opus` are fine); 5 MB decoded max; mime and file header must agree; `415` wrong/mismatched format, `400` bad JSON/base64, `413` too large. `DELETE /voice/{voice_id}` -> `{"ok":true}` (idempotent). Only ask for the recording after an explicit consent screen.

## 6. Device-side detection: `POST /events`
A paired device may publish its own detector's output so the UI and hub see it. Header `x-device-token`; body `{"type","call_id","data"}`. **Only** these two, **only** with `data.engine == "device"`, **only** for a call the hub has seen that is still active (not ended), **and only from a device that currently holds that call's `/listen` or `/talk` socket** (open one first):
- `transcript.caller`: `{"text":str (<=500),"is_final":bool,"utterance_id":str?,"engine":"device"}`
- `risk.update`: `{"s":0-1,"band":low|watch|high|critical,"stage":opening|pretext|pressure|payment|closing,"asks":[otp|card|ssn|gift_card|crypto|wire|p2p|remote_app|secrecy],"why_chips":[<=4 strings],"scam_type":str,"impersonates":str|null,"addresses_ai_system":bool,"engine":"device"}`
The hub rebuilds the event from the validated fields (extras are dropped). Errors: `403` any other type or engine (including `alert.fired`, `call.*`, `handoff.*`, `user.action`), `404` unknown call, `409` call already ended, `403` also when this device holds no `/listen`/`/talk` socket for the call, `422` invalid field, `429` over 40 events per 10 s per device, `401` no/invalid token. Notes: a `risk.update` with `engine:"device"` is treated like a real detector score by the hub (it silences the hub fallback detector briefly and can count toward restore decisions), so post honest scores at a modest rate (about 1 per utterance); the hub does not turn it into `alert.fired` for you (P2 / the fallback detector do that).

## 7. Typical live-call flow
1. Pair once; open `WS /events`; read `/demo/status` flags.
2. `call.incoming` -> `call.routed LIVE_GUARD` -> ring (and, in `sip` mode, accept the Telnyx WebRTC leg) -> `call.answered`.
3. Optional: `WS /listen/{id}` for audio; in `talk` mode open `WS /talk/{id}` and stream mic frames.
4. `alert.fired` -> alert UI -> `POST /user/action scammer_get_scammed` -> `handoff.started` (mic muted by the hub) -> `call.ended` -> `blocklist.updated`.
