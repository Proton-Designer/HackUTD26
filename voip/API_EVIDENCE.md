# Telnyx API evidence (spec: github.com/team-telnyx/openapi spec3.json; docs: https://developers.telnyx.com/api-reference/call-commands/streaming-start)
| Endpoint | Keys we send | Notes |
|---|---|---|
| `POST /v2/calls/{ccid}/actions/answer` | stream_url, stream_track=inbound_track, stream_codec=PCMU, stream_bidirectional_mode=rtp, stream_bidirectional_codec=PCMU, stream_bidirectional_target_legs | answer accepts the stream params, so one call starts the ONE stream |
| `POST /v2/calls/{ccid}/actions/streaming_start` | same + stream_bidirectional_sampling_rate (8000..48000), stream_auth_token, client_state, command_id | alternative to answer-with-stream |
- `stream_bidirectional_target_legs` enum: `both | self | opposite` (default `opposite`). Hypothesis: on the caller leg, `self` = caller hears injected audio. **UNVERIFIED until a real call.**
- SHAKEN/STIR: spec has `shaken_stir_attestation` / `shaken_stir_validated` names (exact webhook location **UNVERIFIED**; capture from first real `call.initiated` in logs/eng2-webhooks.jsonl).
- Account numbers: see voip/ACCOUNT.md.

## LIVE EVIDENCE 2026-11-08 (backup account, calls #1-#5; ids truncated, no secrets)
- Webhook signature: Telnyx webhooks verify (Ed25519, TELNYX_PUBLIC_KEY); unsigned POST -> 403. `call.initiated` payload keys (names only): call_control_id, call_leg_id, call_session_id, caller_id_name, calling_party_type, client_state, connection_codecs, connection_id, direction, flow_destination, from, from_sip_uri, offered_codecs, start_time, state, to, to_sip_uri. **No shaken/stir/attestation key** -> attestation is NOT available from the webhook. CDR (`GET /v2/detail_records?filter[record_type]=sip-trunking`) has `shaken_stir: "A"` on the inbound leg.
- `POST /v2/calls` (dial): `connection_id` MUST be the Call Control App id (cred-connection id -> 422 10015). Accepts `audio_url`, `time_limit_secs`, `from`, `to` (E.164 or `sip:user@sip.telnyx.com`). Dialing a SIP user requires that credential connection's `sip_uri_calling_preference = internal` (unset -> CDR `hangup_details: recv_refuse` within 1 s).
- Our dialed Maria leg is delivered back to the SAME webhook as `call.initiated` with `direction: incoming`, its own `call_session_id`, `client_state` echoed (role=maria), `to` = her SIP user. Answering it -> 422 90102 "Can not issue an answer command on an outbound call". Ignore it.
- `answer` with stream_* (inbound_track, PCMU, bidirectional rtp, target_legs=self): media WS start frame = {media_format: {channels:1, encoding:PCMU, sample_rate:8000}}, `tracks` null. Frames arrive as `media` with `track: inbound` only (3.6k per 73 s); frames we write back to the same WS (decoy/echo) are heard by the caller (counted by hub: frames_to_caller).
- Conference: stream survives Maria joining/leaving; leave on an ended leg -> 422 90018 "Call has already ended" (harmless). Hangup on ended call same code.
- Trial account: termination blocked (D17) -> can't test; backup (verified) account works. Cost per 73 s test call about $0.0164 (inbound 0.0064 + outbound 0.01); SIP leg to browser $0.
- Restore: re-joining after handoff worked within the 30 s window (caller + Maria both rejoined the conference).
