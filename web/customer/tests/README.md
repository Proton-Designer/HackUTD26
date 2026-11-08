# P1 demo rehearsal, no phone (TASK-015)

    web/customer/tests/run_e2e.sh        # first run makes /tmp/backfire-e2e-venv (pip: playwright, websockets)

Starts the real hub via `scripts/run_hub` (NO_TUNNEL=1 SIM_MODE=1 VOIP_OPEN_TOKEN=1, port 8011, throwaway DB), opens Maria's app at 390x844
in headless Chromium, and plays the demo: unlisted number rings -> Answer -> fake P2 `risk.update`+`alert.fired` (beeps counted via an
AudioContext hook, chips, 3 buttons) -> Fire Back -> `user.action`, `handoff.started`, echo decoy -> hang up -> `blocklist.updated`
-> same number again is `BLOCKED_BACKFIRE` and the app never rings. Screenshots go to a temp dir (or $E2E_SHOTS); the hub gets its own LOGDIR and HUB_NO_PIN_FILE=1 so it never touches a live hub's logs or PIN. Exit 0 only if all pass.
Each step prints PASS / FAIL / GAP (GAP = a known missing piece in another lane, with the owner named).

Everything is SIMULATED: simulated caller (reuses `scripts/sim_call.py` webhook builders; the call is held open by the test), no Telnyx, no real audio.
Not covered: real WebRTC ring/answer (app runs with `?novoip`), real microphone/voice enrolment, iOS Safari, real P2/P3 services (the test plays P2; P3 is the hub's echo decoy).
Env: `E2E_PORT`, `DEVICE_PIN`, `E2E_VENV`. Dummy `TELNYX_CRED_CONNECTION_ID`/`TELNYX_SIP_USER` are set because voip reads them unguarded in SIM_MODE.
