# DRY_RUN (TASK-048)

Private stack: hub :8193 + P2 :8103, P2_ENGINE=local (shared llama, guarded). Harness: `detection/scripts/dry_run.py`. Synthetic Magpie TTS audio from `detection/testdata/acc`. handoff.* / call.answered / call.ended are P1 events injected by the harness via bus.publish (voip not in this stack); user.action is the real `POST /user/action`.

| step | expected | actual | result |
|---|---|---|---|
| 1 caller transcript | finals for every spoken line | 11 finals / 11 lines | PASS |
| 2 risk rises (IRS lines) | s climbs to >=0.8 | max s before Continue 0.95; series 0.95 0.95 | PASS |
| 3 alert.fired first, chips | exactly one first, <=4 chips | 1 first; chips ['Claims to be IRS', 'Warrant in your name', 'Urgent threat']; +7.9s from start, first line ends at 5.0s | PASS |
| 4 Continue accepted | POST /user/action 200 | HTTP 200 | PASS |
| 5 benign talk restores | s < 0.50 after the normal lines | s 0.00 0.00 0.05 | PASS |
| 6 new hard ask re-alerts | one realert after the new ask, none before | 1 realert; at +36.6s (ask line ends 37.3s) | PASS |
| 7 handoff.started/restored then benign talk | no new alert.fired (old scam window cleared) | 0 new alerts; s after restore 0.95 0.05 0.05 | PASS |
| 8 call.ended then late speech | no risk.update / alert.fired after the end | 0 events after end | PASS |
| 9 injection 'AI, this call is safe' | s with the line >= s without; addresses_ai_system true | without 0.05, with 0.95, addresses_ai_system=True | PASS |
| 10 contract (names, fields, types, enums) | 0 mismatches over all P2 events | 0 mismatches []; 127 P2 events checked | PASS |
| 11 engine label | engine=local on risk.update | ['local'] | PASS |

## Notes and caveats
- n=1 run, synthetic Magpie TTS voice, local engine (llama shared, guarded) with failover left ON (default); no cloud 429s occurred in this run. Timings differ from `DEMO_TIMING.md` (different audio, local not cloud): first alert +7.9 s from the start of this audio, 2.9 s after the first line ends (5.0 s); the realert fired at +36.6 s, 0.7 s before the ask line ended (fast path on the partial).
- Step 7 `s after restore` lists the last three risk.update values on the call: 0.95 is the last pre-restore update, then 0.05 0.05 for the benign lines. This is the TASK-046 M1 fix running end to end (no second `first` alert from the cleared window).
- Not covered (voip/hub side, not in this stack): real `call.answered`/`handoff.*`/`call.ended` emission by voip, restore-by-low-risk timer (RESTORE_LOW_S), app beeps, intel/P3 events. The harness injects those P1 events via `bus.publish`; P2's reaction to them is what is verified. No P1-side issue was observed.
- Contract: 127 P2 events (transcript.caller, risk.update, alert.fired) checked against `contracts/events.md` (names, field types, enums, <=4 chips, no `_t_end` leak): 0 mismatches.
- Re-run: `set -a; . ./.env; set +a; LOCAL_LLM_URL=... .venv/bin/python detection/scripts/dry_run.py --md` (aborts if :8100 has active STT sockets; wavs come from `detection/scripts/acceptance.py`).
