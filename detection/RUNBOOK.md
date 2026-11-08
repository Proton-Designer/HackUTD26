# P2 runbook (live)
**Start / restart the service** (supervised: restarts uvicorn 2 s after any exit and logs `uvicorn exited rc=N` with a timestamp to `logs/p2.log`):
`bash detection/scripts/run.sh` in a tmux window (e.g. `tmux new-window -n p2svc 'bash detection/scripts/run.sh'`). Ctrl-C twice stops it; `kill <pid>` (SIGTERM) stops it. Port `P2_PORT` (default 8100). Loads `.env` without printing it.
**Tunnel:** `bash detection/scripts/tunnel.sh` (own window `p2tun`). Quick-tunnel URL lands in `logs/p2-tunnel.log` and changes on every restart; P1's relay needs `P2_STT_URL=wss://<host>` updated when it does.
**Is it healthy?** `curl -s localhost:8100/healthz`: `stt.backend` riva|whisper, `engines.cloud_key_present` / `local_reachable`, `hub_subscriber_connected` (false = P2 can't hear `user.action`/hub events; check HUB_URL), `active_stt_sockets`, `last_error` (source + exception class + time, never a secret).
**Reading the frame counts:** each call logs `stt ws <call> first frame: event=<x>` and at close `stt ws <call> closed: frames={...} utterances=N`.
- no log line at all: the relay never connected (tunnel URL stale, or 1008 reject = PIPELINE_TOKEN mismatch; look for a 403/1008 on the relay side).
- `frames={'connected':1,'start':1}` with no `media`: relay connected but forwarded no audio (Telnyx stream not started or wrong track).
- `media` > 0 but `utterances=0`: audio arrived but VAD heard no speech (silence, wrong track = the customer side, or very low level).
- `utterances>0` but no transcripts on the hub: look for `stt failed` (NVIDIA key/rate limit) and `/healthz` `last_error`; whisper fallback kicks in automatically.
**PIPELINE_TOKEN flip:** set the same `PIPELINE_TOKEN=<secret>` in the hub env (P1) and in P2's env/.env, restart both (P2 via run.sh restart: Ctrl-C twice, rerun). The relay sends it as header `x-pipeline-token` on `/stt`; P2 sends it on `POST /events`. Unset on P2 = `/stt` and `/detect` are open (a warning is logged at boot). Wrong value: WS closes 1008, `/detect` 401. To turn auth off in an emergency, unset it on both sides and restart. Never paste the value into chat or commits.
**DEMO_MODE fallback** (P2 down or flaky): on the hub run with `DEMO_MODE=1` (loops `mock/events.json`) or `POST /demo/replay`; the web UI then runs off scripted events with no P2. `FALLBACK_DETECT=1` on the hub arms P1's own backup detector. P2 itself never raises into the call path: if it dies, calls still connect and just lose alerts.
**Acceptance / checks:** `bash detection/scripts/acceptance.sh` (~1 min, hub :8190 + P2 :8191, real NVIDIA calls, prints PASS/FAIL table). Two-call load check: `set -a; . ./.env; set +a; .venv/bin/python detection/scripts/concurrency.py`. Unit tests: `.venv/bin/python -m pytest -q detection`.
**Env knobs:** `P2_ENGINE` cloud|local, `P2_STT=whisper` force fallback STT, `P2_ENDPOINT_MS`, `P2_PARTIALS=0`, `ALERT_S`, `HARD_ASK_S`, `LOCAL_LLM_URL`.

## engine=local (Nemotron 3 Nano 4B on the GPU, TASK-013)
- Why it was unreachable: `LOCAL_LLM_URL` was unset (default 127.0.0.1:11434 = Ollama), but on WSL2 the model runs as a Windows llama.cpp `llama-server.exe` listening on the WSL gateway IP :8101 (127.0.0.1 does not reach it). The probe used Ollama's `/api/tags`; it now uses `/v1/models`.
- Start the model: `bash detection/engines/run_local_llm.sh` (eng3's script; keep it running in its own tmux window). Check: `curl -s http://$(ip route | awk '/default/{print $3}'):8101/health` -> `{"status":"ok"}`.
- `run.sh` and `acceptance.sh` now default `LOCAL_LLM_URL` to `http://<WSL gateway>:8101` when unset (override in `.env` if the model lives elsewhere). `/healthz` -> `engines.local_reachable` should be true.
- Switch the live engine: restart P2 with `P2_ENGINE=local scripts/run.sh` (global), or per request `POST /detect {"engine":"local"}`. Back to cloud: unset `P2_ENGINE`.
- (Resolved in 20ca58a: `detection/engines/local.py` speaks OpenAI /v1/chat/completions, so llama-server works.)
- Measured (my box): detect() with engine=local ~1.6-1.7 s per scam window; acceptance case 6 PASS (irs alert s=0.95, bank no alert s=0.40).

## Cloud -> local failover (TASK-018)
- `detect(engine=cloud)`: on cloud exception/timeout/429/exhausted P2_CLOUD_RPM budget, if the local server answered a cached (10 s) `GET $LOCAL_LLM_URL/v1/models` probe, it retries ONCE on local inside the 4 s overall budget (cloud attempt is capped at 2.5 s when local is reachable). Output `engine="local"`, WARNING log `detect <id> failover: cloud <Err> -> local`, counter `detect.FAILOVERS`. Then the rule floor as always. `P2_FAILOVER=0` disables it. The cloud rate bucket never gates local.
- Real check: `ACC_BREAK_CLOUD=1 ACC_P2_PORT=8102 bash detection/scripts/acceptance.sh` (cloud LLM base URL pointed at a dead port for that P2 only; STT unaffected).
- Limit: llama-server runs `-np 1`, so many parallel calls queue; a local call that misses the remaining budget falls to rules-only for that window (score dips to the rule floor, then can re-arm the alert state: acceptance 4a flaked in that mode). One or two calls is fine (~1.7 s each).

## Hold last score on an engine-failed window (TASK-019)
- `detect()` sets `detect.ENGINE_FAILED[call_id]` (no schema/contract change) when a window had no LLM result (rules-only because every engine failed). `alert.py _hold`: for such a window it keeps max(last anchor s, rules s) for 10 s / 3 windows (anchor = last LLM-backed result or rule fast-path score >= 0.5), then decays. A real low LLM score passes through unchanged (restore still works). Log: `hold last score` (INFO).
- Trade-off: while engines are failing, restore after normal talk can lag up to ~10 s.
- Real check: `ACC_BREAK_CLOUD=1 ACC_P2_PORT=8102 bash detection/scripts/acceptance.sh` with 5 parallel calls on the single-slot llama: 4a PASS (was FAIL); case 5 restore passed in 2 of 3 runs (one run held 0.95 at the last normal line).

## Restore after Continue (TASK-021)
- Root cause of acceptance case 5 (s stayed 0.95 after normal talk): the scoring window is the last 6 finals, so scam lines kept s high until ~6 benign lines had passed. Fix: user.action=continue clears the window (and drops any in-flight result scored on the old window via an epoch); a new hard ask still fires on its own.
- Rules-clean failed windows (both engines failing, rules s<0.2, no asks) are held only once (TASK-019 hold otherwise unchanged).
- Failover budget: cloud+probe capped at 2.0 s, local gets >= 2.0 s inside OVERALL_TIMEOUT_S=4.0; probe is lock-guarded, 0.5 s cap, shared with /healthz. `ACC_BREAK_CLOUD=blackhole` tests the timeout path.

## Per-call report (TASK-025)
`.venv/bin/python detection/scripts/call_report.py [logs/p2.log] [--call ID-prefix] [--last N]` prints a timeline per call (ws open/close frames, each final with its latency after endpoint and the first 60 chars, each risk.update with s/band/engine/src/asks, alerts marked fast-path vs LLM, Continue/restore, dropped late finals, failovers, 429s, demo-cache hits) and a SUMMARY line (first alert, final s, alerts, failovers, 429s). Read-only. Needs the timestamped log format (restart P2 after TASK-025; older untimestamped lines still parse but show `--` times and cannot tell a 429 from another HTTP error). Demo-cache lines carry no call id, so they are attributed to the most recent call.

## Watchdog (TASK-030, zero tokens)
`bash detection/scripts/watchdog.sh` (run it in its own tmux window, e.g. `backfire-p2:watchdog`). Log: `logs/watchdog.log`.
- Every 20 s GET :8100/healthz. Refused 3x in a row AND window `p2svc` missing or a bare shell -> recreates it / types `LOCAL_MODEL=nemotron-nano-4b [HUB_URL=...] bash detection/scripts/run.sh` (run.sh sources .env itself; nothing secret is printed). If the window runs a process (the supervisor) it is left alone.
- Every 60 s GET `<tunnel>/healthz` (URL from `logs/p2_tunnel_url.txt`, else the current one hard-coded). 3 fails while local is OK -> restarts `p2tunnel` (tunnel.sh), parses the new trycloudflare URL into `logs/p2_tunnel_url.txt` and logs `!!!! TUNNEL URL CHANGED ... !!!!`. **The lead must then tell P1** (`P2_STT_URL=wss://<new host>`); the script never posts anywhere.
- Never restarts the tunnel while `active_stt_sockets>0`. The service is only restarted when refused (nothing to lose).
- Env overrides: WD_SESSION WD_SVC_WIN WD_TUN_WIN WD_PORT WD_TUNNEL_URL WD_TICK_S WD_TUN_EVERY WD_FAILS WD_MAX_TICKS WD_SVC_CMD WD_TUN_CMD. Test: `pytest detection/tests/test_watchdog.py` (throwaway tmux session, fake service+tunnel).

## STT fallback (TASK-031): Riva down -> local Whisper
- Whisper = faster-whisper `base.en`, **CPU int8** (no GPU, so no OOM risk for llama-server). Override model with `P2_WHISPER_MODEL=tiny.en` (faster, less accurate). Measured: ~0.65 s per call on 16 cores, throughput-bound (2 concurrent calls ~1.3 s each, 4 ~2.6 s).
- Triggers: Riva init fails, or a Riva call errors/times out (`P2_STT_TIMEOUT`, 6 s). Whisper preloads in a background thread at startup (`whisper_fallback_loaded` in /healthz). After 2 consecutive Riva failures Riva is bypassed for 30 s (no 6 s wait per utterance), then re-probed. `/healthz` stt: `primary_failures`, `primary_bypassed`, `whisper_model`.
- Demo override: `P2_STT=whisper` (Riva never used). While on whisper, partials slow to every 1.5 s (`P2_SLOW_PARTIAL_EVERY_S`) and pause while a final is waiting, so finals are not starved.
- Test it: `ACC_BREAK_STT=1 ACC_P2_PORT=8102 bash detection/scripts/acceptance.sh` (dead Riva URI via `RIVA_URI` for that P2 only; `blackhole` = hanging connect). Result 9/9 with Riva down.
- Whisper mishears sometimes (e.g. "6th digit"); rules still match the ask words, accuracy is the cost, availability is the gain.

## VAD on quiet / odd real calls (TASK-032)
- At every socket close p2.log has `rms(per 20ms frame): {frames,p50,p90,max,voiced,noise,thr}` and at start `media_format=...`. Zero utterances + `max` < `thr` = line too quiet. `P2_DUMP_AUDIO=1` writes logs/audio/<call>.wav (local only, off by default; listen to it).
- VAD: speech = frame RMS > max(P2_VAD_FLOOR=60, noise*P2_VAD_REL=2.5); noise floor starts at 30, falls fast / rises slowly, capped at P2_NOISE_CAP=300 (thr <= 750). Was floor 300 and noise*3.5.
- Decoding follows start.media_format.encoding: PCMU (default), PCMA, L16 (big-endian); 16 kHz is averaged to 8 kHz.

## Offline demo / demo in a box (TASK-035)
`bash detection/scripts/demo_local.sh` boots, all on this machine with temp DBs and no tunnel/Telnyx: hub (`server.main`, SIM_MODE=1, :8200), P2 (:8102, pointed at the hub), P3 decoy (:8310), an auto-tap helper (`demo_tap.py`: presses "Scammer Get Scammed" 2 s after alert.fired, like Maria's button), then P1's `scripts/demo_call --reset` with `detection/testdata/scam_call_synth.wav` (SIMULATED caller, synthetic voice). It prints Maria's page `http://127.0.0.1:8200/app/` (PIN 1234) and the command center `.../command-center/`, the hub TIMELINE and the P2 call_report, then shuts everything down (process groups; logs kept in the printed temp dir).
- `KEEP_UP=1` leaves it running to show the pages; `AUTO_TAP=0` = you press the button; `DEMO_WAV=<8 kHz mono wav>`; `DEMO_NO_DECOY=1` = hub echo stand-in instead of P3.
- `OFFLINE=1` = P2_STT=whisper + P2_ENGINE=local (needs llama-server on :8101). P2 then needs no internet; P3 decoy and P4 intel still call NVIDIA.
- Measured (cloud, 2026-11-08 02:3x): incoming 0.0 s -> answered 1.5 -> first alert 6.2-7.8 -> handoff.started ~9.8 -> blocklist.updated ~41 s; P2 finals 0.2-0.4 s after endpoint, all 4 events present. OFFLINE (whisper+local, no decoy): first alert +9.0-10.6 s, finals 1-4.7 s after endpoint (whisper CPU and llama share the box), 2 engine timeouts fell back to rules.
