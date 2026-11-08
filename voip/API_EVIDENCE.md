# Telnyx API evidence (spec: github.com/team-telnyx/openapi spec3.json; docs: https://developers.telnyx.com/api-reference/call-commands/streaming-start)
| Endpoint | Keys we send | Notes |
|---|---|---|
| `POST /v2/calls/{ccid}/actions/answer` | stream_url, stream_track=inbound_track, stream_codec=PCMU, stream_bidirectional_mode=rtp, stream_bidirectional_codec=PCMU, stream_bidirectional_target_legs | answer accepts the stream params, so one call starts the ONE stream |
| `POST /v2/calls/{ccid}/actions/streaming_start` | same + stream_bidirectional_sampling_rate (8000..48000), stream_auth_token, client_state, command_id | alternative to answer-with-stream |
- `stream_bidirectional_target_legs` enum: `both | self | opposite` (default `opposite`). Hypothesis: on the caller leg, `self` = caller hears injected audio. **UNVERIFIED until a real call.**
- SHAKEN/STIR: spec has `shaken_stir_attestation` / `shaken_stir_validated` names (exact webhook location **UNVERIFIED**; capture from first real `call.initiated` in logs/eng2-webhooks.jsonl).
- Account numbers: see voip/ACCOUNT.md.
