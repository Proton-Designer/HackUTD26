# P2 demo-day card (rehearsal 09:00, judging 13:00)
Repo root = ~/HackUTD26 (live service runs from the trunk checkout). Live P2 = :8100. Nothing here needs an LLM or a secret on screen.

## 1. Start order (one tmux window each; tmux session `backfire-p2`, llama in `backfire-p2-eng:llama`)
1. **llama-server** (GPU, local detector): `bash detection/engines/run_local_llm.sh`  (wait ~30 s for the model; `curl -s $LOCAL_LLM_URL/health` -> 200)
2. **p2svc**: `P2_ENGINE=local HUB_URL=<hub url> bash detection/scripts/run.sh`  (supervised, restarts itself; logs/p2.log)
3. **tunnel**: `bash detection/scripts/tunnel.sh`  (prints a *.trycloudflare.com URL; the watchdog writes logs/p2_tunnel_url.txt)
4. **watchdog**: `bash detection/scripts/watchdog.sh`  (restarts p2svc / tunnel / llama on repeated failure; logs/watchdog.log)
LOCAL_LLM_URL defaults to the WSL gateway `:8101`. `.env` is sourced by run.sh; never cat it.

## 2. 30-second health check
`curl -s localhost:8100/healthz | python3 -m json.tool` and read:
- `engine` / `engines.primary` = `local`; `engines.local_reachable` = true; `engines.local_probe_ms` small (<200).
- `cloud_breaker.state` = `closed` (open = NVIDIA trouble; local still works).
- `hub_subscriber_connected` = true.
- `stt.backend` riva and `stt.primary_bypassed` = false (true = Riva down, whisper CPU fallback in use, slower finals).
- `active_stt_sockets` 0 before a call, 1 during. `last_error` empty or old.
Then: `curl -s <tunnel url>/healthz` -> 200. Then one test call; `python3 detection/scripts/call_report.py --last 1` (needs `.venv/bin/python`).

## 3. If X then Y
| X | Fix (1 line) | Tell |
|---|---|---|
| Tunnel URL changed (watchdog log "TUNNEL URL CHANGED") | read the new URL from logs/p2_tunnel_url.txt | lead -> P1: set `P2_STT_URL=wss://<host>` and restart their relay (not during a call) |
| llama down (`local_reachable` false) | watchdog restarts it in ~2 min; manual: rerun step 1. Meanwhile P2 falls back to cloud automatically | nobody unless it stays down |
| NVIDIA 429 / cloud breaker open | nothing: local primary is unaffected; breaker re-probes itself | nobody |
| Riva down (`primary_bypassed` true) | nothing: whisper fallback takes over; alert still fires from the rules fast path, finals are 1-4 s slower | nobody |
| Hub disconnected (`hub_subscriber_connected` false) | check hub is up; P2 reconnects itself; else restart p2svc (step 2) | lead / P1 if the hub is down |
| No transcripts on a real call | `grep 'rms(per 20ms' logs/p2.log \| tail -1`: p90 < ~40 and thr 60 means very quiet line, set `P2_VAD_FLOOR=40` and restart; no `/stt` line at all means the relay never connected (tunnel URL / P1 side) | P1 (relay / URL) |
| False alarm on stage (legit call alerts) | press **Continue** in the UI (restores calm, window is cleared); do not restart anything | lead after the demo, with call id |
| Alert did not fire on a scam | hard asks (gift card / OTP / wire) fire in <1 s from partials; check `risk.update` s in logs, then engine failover lines | lead |
Offline insurance: `OFFLINE=1 bash detection/scripts/demo_local.sh` (hub+P2+decoy+simulated caller, no internet).

## 4. Freeze rules
- Known-good tag: **p2-known-good-0250** (older: 0241, 0240, 0221). Do not deploy during a judge visit; do not deploy after code freeze (08:00) except a rollback.
- Roll back: `git checkout p2-known-good-0250` in the live checkout, then restart p2svc (Ctrl-C twice in its window, rerun step 2). Return later with `git checkout <branch>`.
- Never `pkill`/`tmux kill-*` in the live session; interrupt (Ctrl-C) the one window you mean.

## 5. Before judging
- Stop evals/benchmarks (shared GPU + NVIDIA key): no `eval/` runs, no acceptance runs, no llama tuning.
- `rm -f logs/audio/*.wav`; make sure `P2_DUMP_AUDIO` is unset/0 (caller audio is not kept on stage).
- `engines.primary` = local, cloud breaker closed, one rehearsal call done, then leave services alone.
- **Run `bash detection/scripts/ready_check.sh --tunnel <p2 tunnel URL>`** (add `--tests` before the freeze). Read-only: healthz fields, tunnel matches live, `P2_DUMP_AUDIO` off in the live process (key only, never values), `logs/audio` empty, llama answers, watchdog alive, live HEAD is a `p2-known-good` tag and the process is newer than the last `detection/*.py` commit, plus one positive (gift card + secrecy -> critical) and one negative (benign -> low) control through `/detect` (skipped while a call is active). Every FAIL prints a one-line fix. Do not start judging on `NOT READY`; WARN is acceptable if you know why (e.g. cloud breaker open while local is primary).
