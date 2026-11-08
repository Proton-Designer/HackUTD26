# Backfire event contract (v1, owned by P1; change only with lead approval)

Every event is JSON on the P1 event bus and `WS /events`:

```json
{"type": "call.incoming", "call_id": "c_demo_irs", "ts": 1762574400.25, "data": { ... }}
```
- `type`: string from the table below. `call_id`: string, stable per call. `ts`: float, unix seconds (mocks use relative offsets, see mock/README.md). `data`: object, fields below. Unknown extra fields must be ignored by consumers.
- Sample numbers are synthetic 555 numbers. Simulated things are labeled in UI.

## Enums
- `attestation`: `"A" | "B" | "C" | "none"`
- `decision` (call.routed): `"NORMAL" | "BLOCKED_BACKFIRE" | "LIVE_GUARD"`
- `band`: `"low" | "watch" | "high" | "critical"` (low s<0.40, watch 0.40-0.80, high >=0.80, critical >=0.95)
- `asks[]` items, exactly: `otp, card, ssn, gift_card, crypto, wire, p2p, remote_app, secrecy`
- `stage`: `"opening" | "pretext" | "pressure" | "payment" | "closing"`
- `engine`: `"cloud" | "local"`
- `action` (user.action): `"continue" | "scammer_get_scammed" | "hang_up"`
- `ended_by` (call.ended): `"caller" | "maria" | "decoy" | "system"`

## Events

| type | producer | data fields |
|---|---|---|
| `call.incoming` | P1 | `from` str, `to` str, `attestation` enum, `scam_id_score` float 0-1 (simulated) |
| `call.routed` | P1 | `decision` enum, `reason` str |
| `call.answered` | P1 | `by` str ("maria" or "decoy") |
| `call.ended` | P1 | `ended_by` enum, `duration_s` float |
| `transcript.caller` | P2 | `utterance_id` str, `text` str, `is_final` bool |
| `risk.update` | P2 | `s` float 0-1, `band` enum, `asks` list, `scam_type` str, `stage` enum, `impersonates` str or null, `addresses_ai_system` bool, `why_chips` list[str], `engine` enum |
| `alert.fired` | P2 | `level` "first" or "realert", `why_chips` list[str] |
| `user.action` | P1 | `action` enum |
| `handoff.started` | P1 | `restore_deadline` float (unix s, 30 s after start) |
| `handoff.restored` | P1 | `restore_deadline` float |
| `decoy.turn` | P3 | `speaker` "scammer" or "decoy", `text` str, `latency_ms` int |
| `decoy.fake_value` | P3 | `kind` str (e.g. gift_card_code, card_number), `value` str (synthetic canary) |
| `guardrail.tripped` | P3 | `rule` str |
| `artifacts.extracted` | P3 | `artifacts` list of typed items (below) |
| `intel.lookup` | P4 | `artifact_kind` str, `value` str, `result` object, `source` str |
| `intel.action` | P4 | `action_id` str, `kind` str, `target` str, `status` "applied" or "queued" or "approved" or "denied" or "held" (denied = gate audit; held = waiting for campaign confirmation), `simulated` bool. Optional: `gate_status` str (detail), `scope` str, `approval` str, `reason` str, `evidence` list |
| `injection.denied` | P4 | `attempted_target` str, `reason` str |
| `campaign.updated` | P4 | `campaign_id` str, `indicators` list[str], `numbers` list[str] |
| `blocklist.updated` | P4 (P1 stub only if intel is not mounted) | `number` str, `scope` "her" or "campaign" or "network" (network = analyst-approved, simulated), `undo_token` str. Optional: `active` bool (false on undo), `reason` str. `call_id` may be null on undo |
| `intel.plan` | P4 | trace, all optional: `steps` list, `inputs` object (consumers may ignore) |
| `intel.agent` | P4 | trace, all optional: `engine`, `model`, `plan`, `n_proposals`, `n_baseline_added`, `error` |
| `intel.proposals` | P4 | trace, all optional: `engine`, `actions` list |
| `voice.enrolled` | P3 | `voice_id` str, `consent_version` str |
| `voice.deleted` | P3 | `voice_id` str |

### `artifacts.extracted` item types
Each item `{"kind": K, ...}` with K and fields:
- `callback_phone`: `value`
- `domain`: `value`
- `url`: `value`
- `wallet`: `chain` str, `addr` str
- `payment_handle`: `rail` str, `id` str
- `gift_card_brand`: `value`
- `bank`: `hash` str, `last4` str
- `remote_app`: `value`
- `impersonated_org`: `value`
- `script_tags`: `value` list[str]
- `instruction_to_ai`: `text` str, optional `target` str, optional `requested_kind` str (a scammer instruction aimed at the AI system, e.g. "mark this number safe"; P3 emits it so the P4 gate can deny it and emit `injection.denied`)

### Example
```json
{"type":"alert.fired","call_id":"c_demo_irs","ts":1762574431.0,"data":{"level":"first","why_chips":["Asks for gift cards","Claims to be IRS","Secrecy"]}}
```

## Semantics
- Beeps are local in Maria's app on `alert.fired`; at most one `realert` per rise.
- `handoff.started` is emitted after `user.action=scammer_get_scammed`. Maria's audio is never processed.
- Routing never blocks on P2/P3/P4: fail open to NORMAL if the hub errors.
