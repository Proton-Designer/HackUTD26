# Telnyx safe use (read before touching the Telnyx account)

Context: on 2026-11-08 ~01:00 the backup Telnyx account started returning `401 / 10009 "This user has been marked as blocked"` right after six automated test calls (`voip/test_call.py --live`). It was restored afterwards and is Ayman's long-term account. Everything below exists so that never happens again.

## What most likely tripped the block (our inference; Telnyx never said)
1. **Self-dials via the API**: `POST /v2/calls` with `from` = `to` = our own number, repeatedly. Call pumping / traffic-pumping and "spoofed caller ID" shape (from == to is the classic spoof).
2. **New number + burst**: a freshly bought number and ~6 calls within ~25 minutes (new account, $1 number, then volume).
3. **Prerecorded, fixed-length robocall shape**: `audio_url` played to a callee, always 73 s (`time_limit_secs`), same file, same cadence.
4. **Scam-script audio**: IRS / gift-card / crypto content ("warrant for your arrest", "buy Target gift cards", wallet addresses) over PSTN. Likely flagged by content/abuse review or by a carrier complaint pipeline.
Contributing: unverified SHAKEN/STIR on our own outbound leg, and the account also hosting another product's numbers.
We cannot tell which of the four mattered; treat all as unsafe.

## Rules from now on
- **No PSTN outbound. Ever.** Not for tests, not for "just one". voip enforces it: `telnyx.dial()` raises unless `to` is exactly `sip:<TELNYX_SIP_USER>@sip.telnyx.com` (Maria's browser), or the human override `BACKFIRE_ALLOW_PSTN_OUTBOUND=1` is set. `voip/test_call.py --live` refuses without that same variable. Do not set it without the lead's explicit OK and Ayman's.
- **Tests are inbound only, from a real phone** (a person dials the scam line), **at least 3 minutes apart**, **benign words** (e.g. "this is the dental office confirming Thursday"). Never read scam scripts into a real phone call. The scripted scam content stays inside SIM_MODE (`scripts/demo_call`), which sends zero Telnyx requests.
- **One Telnyx-touching person at a time** (today: the lead). Engineers do not call the Telnyx API, not even `GET`s, not for "just checking balance"; ask the lead. `voip/` only reads Telnyx via webhooks.
- **No new numbers, no config changes, no webhook PATCHes** except by the lead (`scripts/point_telnyx` is dry-run by default; `--apply` is lead-only).
- **No bursts**: never more than a handful of calls per hour on the whole account, including the other product's.
- Prefer the **phone-free demo** (`docs/P1_RUNBOOK.md` -> "Phone-free demo", `scripts/demo_call`) for rehearsals, screenshots and CI. Telnyx is only for the single judged live path, once.
- If a call returns `10009 marked as blocked` or `D17 account disabled`: stop all API use immediately, tell the lead, do not retry (retries look like abuse). The hub keeps working in SIM_MODE.

## SIM -> LIVE switch checklist (do in order; lead performs the Telnyx-touching steps)
0. Confirm the lead has approved going live and nobody else is calling the API. Check the portal/email for any compliance notice first.
1. **Dry run only**: `scripts/point_telnyx` (no `--apply`). Confirm it prints the current tunnel URL + `/telnyx/webhook` for both the Call Control app and the credential connection.
2. **Env flips** (in `.env`, then restart the hub, same tunnel if possible):
   - remove / unset `SIM_MODE` (must NOT be `1` on the live hub);
   - `VOIP_ALLOW_UNSIGNED` unset; `TELNYX_PUBLIC_KEY` set (webhooks verify Ed25519; unsigned -> 403);
   - `PUBLIC_WS=wss://<tunnel host>` set (media stream URL given to Telnyx);
   - `TELNYX_API_KEY`, `TELNYX_CALL_CONTROL_APP_ID`, `TELNYX_SIP_USER` (+ `TELNYX_SIP_PASSWORD`), `TELNYX_SCAM_LINE`, `TELNYX_CRED_CONNECTION_ID` present for the CURRENT account;
   - `PIPELINE_TOKEN` and `DEVICE_PIN` set; `RESTORE_LOW_S=10`; `P2_STT_URL`, `NVIDIA_API_KEY` set; `BACKFIRE_ALLOW_PSTN_OUTBOUND` NOT set.
3. After restart: `curl localhost:8000/healthz`, `GET /demo/status` (`SIM_MODE:false`, `NVIDIA_API_KEY_set:true`, intel nemotron), `POST <tunnel>/telnyx/webhook` unsigned -> 403 "bad signature", `POST <tunnel>/demo/reset` -> 401, local `/demo/reset` ok.
4. Lead runs `scripts/point_telnyx --apply` once (only if the tunnel URL changed). Check the two PATCHes return 200.
5. Maria's credential connection must have `sip_uri_calling_preference = internal` (else CDR `recv_refuse` and Maria never rings). Lead checks once in the portal/API.
6. **eng3's page in live mode**: open `/app/` WITHOUT `?sim=1` on the phone through the tunnel, pair with `DEVICE_PIN`, wait until the Telnyx WebRTC client shows registered (SIP login served by `/voip/webrtc-token` to the paired device).
7. **One benign inbound test**: a real phone dials `TELNYX_SCAM_LINE`, says benign words for ~30 s, then hangs up. Expected in the hub log: signed webhook 200, `call.incoming/routed`, media `frames_in` only `media:inbound`, Maria's leg rings (CDR not needed), `call.answered{maria}`. Do NOT tap handoff with scam content; if the handoff path must be shown, tap it on the benign call and then let risk stay low (restore) -- no scam audio.
8. Wait >= 3 minutes before any second call; stop after the judged path works. Record the result in `voip/LIVE_TEST_PLAN.md`.
9. To go back to SIM: set `SIM_MODE=1`, restart the hub; the phone-free path needs no Telnyx.

## Quick reference
- Block symptom: `401 10009 ... marked as blocked` (any endpoint) or `D17 ... termination call is blocked`.
- Safe read of what happened: the hub log (`logs/hub-eng2-live.log` style) and webhook events; do not poll Telnyx REST.
- Guards in code: `voip/telnyx.py::dial_allowed`, `voip/test_call.py` (`BACKFIRE_ALLOW_PSTN_OUTBOUND`), SIM webhooks loopback-only (`voip/router.py::direct_local`).
