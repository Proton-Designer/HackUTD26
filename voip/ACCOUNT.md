# Telnyx account (read-only findings, 2026-11-07 ~23:40 CT; no secrets)
- Phone numbers: **0** (nothing to call yet).
- Call Control apps: 1 — "Softdial" (id 2893461320823211836), inactive, webhook points at an unrelated Supabase function. Do NOT reuse; create a Backfire app.
- Credential connections: 3 — "Default Credential Connection" (inactive), "softdial2" (inactive, Supabase webhook), "Forward Only" (active, no webhook). None set up for Backfire/WebRTC.
- Outbound voice profiles: 1 — "Default" (enabled).
## Needed (billable/config -> lead)
1. Buy a US voice number: `POST /v2/number_orders {"phone_numbers":[{"phone_number":"+1..."}]}` (search first: `GET /v2/available_phone_numbers?filter[country_code]=US&filter[features][]=voice`).
2. Create Call Control app: `POST /v2/call_control_applications {"application_name":"backfire","webhook_event_url":"<tunnel>/telnyx/webhook","webhook_api_version":"2","active":true,"outbound":{"outbound_voice_profile_id":"2878166320602416944"}}`.
3. Assign number: `PATCH /v2/phone_numbers/{id} {"connection_id":"<app id>"}`.
4. For Maria's WebRTC (TASK-005): credential connection + `POST /v2/telephony_credentials`.
