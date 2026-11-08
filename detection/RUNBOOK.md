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
- NEEDS eng3's OpenAI-style `detection/engines/local.py` (uses /v1/chat/completions) to be pushed; the trunk copy speaks Ollama `/api/chat` and llama-server will 404.
- Measured (my box): detect() with engine=local ~1.6-1.7 s per scam window; acceptance case 6 PASS (irs alert s=0.95, bank no alert s=0.40).

## Cloud -> local failover (TASK-018)
- `detect(engine=cloud)`: on cloud exception/timeout/429/exhausted P2_CLOUD_RPM budget, if the local server answered a cached (10 s) `GET $LOCAL_LLM_URL/v1/models` probe, it retries ONCE on local inside the 4 s overall budget (cloud attempt is capped at 2.5 s when local is reachable). Output `engine="local"`, WARNING log `detect <id> failover: cloud <Err> -> local`, counter `detect.FAILOVERS`. Then the rule floor as always. `P2_FAILOVER=0` disables it. The cloud rate bucket never gates local.
- Real check: `ACC_BREAK_CLOUD=1 ACC_P2_PORT=8102 bash detection/scripts/acceptance.sh` (cloud LLM base URL pointed at a dead port for that P2 only; STT unaffected).
- Limit: llama-server runs `-np 1`, so many parallel calls queue; a local call that misses the remaining budget falls to rules-only for that window (score dips to the rule floor, then can re-arm the alert state: acceptance 4a flaked in that mode). One or two calls is fine (~1.7 s each).
