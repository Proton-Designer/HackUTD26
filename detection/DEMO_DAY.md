# P2 demo-day card (rehearsal 09:00, judging 13:00)
Repo root = ~/HackUTD26 (live service runs from the trunk checkout). Live P2 = :8100. Nothing here needs an LLM or a secret on screen.

## 1. Start order (one tmux window each; tmux session `backfire-p2`, llama in `backfire-p2-eng:llama`)
1. **llama-server** (GPU, local detector): `bash detection/engines/run_local_llm.sh`  (wait ~30 s for the model; `curl -s $LOCAL_LLM_URL/health` -> 200)
2. **p2svc**: `P2_ENGINE=local HUB_URL=<hub url> bash detection/scripts/run.sh`  (supervised, restarts itself; logs/p2.log; ready in ~6 s). `<hub url>` = the hub P1/lead runs (e.g. `http://localhost:8000`). No hub yet (rehearsal): `HUB_DB=/tmp/hub.db .venv/bin/uvicorn server.main:app --port 8190` in its own window, then `HUB_URL=http://localhost:8190`.
3. **tunnel**: `bash detection/scripts/tunnel.sh`  (prints a *.trycloudflare.com URL in ~5 s). **Then save it for the watchdog** (otherwise the watchdog probes a stale built-in URL, sees it fail and restarts the tunnel by itself, changing the URL): `grep -o 'https://[a-z0-9-]*\.trycloudflare\.com' logs/p2-tunnel.log | tail -1 > logs/p2_tunnel_url.txt`
4. **watchdog**: `bash detection/scripts/watchdog.sh`  (restarts p2svc / tunnel / llama on repeated failure; logs/watchdog.log). Rehearsing next to the live stack: use `WD_SESSION=<your tmux session> WD_PORT=<your P2 port> WD_LLAMA=0 bash detection/scripts/watchdog.sh` or it manages the live `backfire-p2` windows and llama.
LOCAL_LLM_URL defaults to the WSL gateway `:8101`. `.env` is sourced by run.sh; never cat it.

## 2. 30-second health check
`curl -s localhost:8100/healthz | python3 -m json.tool` and read:
- `engine` / `engines.primary` = `local`; `engines.local_reachable` = true; `engines.local_probe_ms` small (<200).
- `cloud_breaker.state` = `closed` (open = NVIDIA trouble; local still works).
- `hub_subscriber_connected` = true.
- `stt.backend` riva and `stt.primary_bypassed` = false (true = Riva down, whisper CPU fallback in use, slower finals).
- `active_stt_sockets` 0 before a call, 1 during. `last_error` empty or old.
Then: `curl -s <tunnel url>/healthz` -> 200. Then one test call: `(set -a; . ./.env; set +a; .venv/bin/python detection/scripts/stream_wav.py detection/testdata/acc/irs.wav --url ws://localhost:8100 --call "demo_test?token=$PIPELINE_TOKEN")` (the token rides on the call id because P2 rejects a missing PIPELINE_TOKEN with 403; synthetic IRS caller, ~10 s, alert at about +8 s), wait 4 s, then `.venv/bin/python detection/scripts/call_report.py --last 1` -> expect `ALERT first`, `alerts 1`, `failovers 0`.

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
### If X breaks during judging (drilled, see eval/DRILLS.md)
- **llama down:** alert still fires (cloud, or rules floor if cloud is down too), 0.7-1.7 s early. Do nothing; watchdog restarts llama in ~2 min.
- **NVIDIA key rate-limited (Riva + cloud):** whisper STT + local llama keep the alert (about 1 s later). Do nothing.
- **Hub restarts mid-call:** P2 reconnects within ~15 s; alert.fired is retried for 20 s so it is not lost. Do nothing; do not restart P2.
- **P2 dies mid-call:** that call is not detected; watchdog brings P2 back in <1 min (restart itself is <1 s). Tell P1 to reopen the relay; next call is fine.
- **Tunnel dies:** ~3 min to notice; read `logs/p2_tunnel_url.txt`, lead tells P1 `P2_STT_URL=wss://<host>`, repoint between calls.

Offline insurance: `OFFLINE=1 bash detection/scripts/demo_local.sh` (hub+P2+decoy+simulated caller, no internet).

## 4. Freeze rules
- Known-good tag = the newest `git tag -l 'p2-known-good-*' | tail -1` (at 05:40: **p2-known-good-0535**). Do not deploy during a judge visit; do not deploy after code freeze (08:00) except a rollback.
- Roll back: `git checkout <newest p2-known-good tag>` in the live checkout, then restart p2svc (Ctrl-C twice in its window, rerun step 2). Return later with `git checkout <branch>`.
- Never `pkill`/`tmux kill-*` in the live session; interrupt (Ctrl-C) the one window you mean.

## Code freeze 07:45 (lead, in `~/HackUTD26`, live checkout; ~3 min; do it between calls)
Run from the repo root. `$P2W` = the tmux window running p2svc (`tmux list-windows -t backfire-p2`). Nothing here kills by port or name. Dry-run (TASK-072, 8 steps verified on a spare instance): `env -u P2_DUMP_AUDIO P2_PORT=8199 P2_ENGINE=local HUB_URL=http://127.0.0.1:9 bash detection/scripts/run.sh` in your own tmux session, then use `--live http://localhost:8199` and `ws://localhost:8199`; without a hub `hub_subscriber_connected` is false and the clean-tree check fails only on your own edits.
1. **No call, no jobs.** `curl -s localhost:8100/healthz | python3 -c 'import sys,json;print(json.load(sys.stdin)["active_stt_sockets"])'` -> `0` (if not 0, wait; never restart mid-call). Stop evals/acceptance runs in the eng windows.
2. **Code is final.** `git status --short detection contracts/models.md` -> empty; `git log -1 --format=%h` and note it. `git fetch -q && git diff --stat HEAD origin/finalized-idea-backfire -- detection` -> empty (pull first if not; no pushes after 08:00 except a rollback).
3. **Dumps off.** `rm -f logs/audio/*.wav; ls logs/audio | wc -l` -> `0`.
4. **Restart p2svc without dumps**: `tmux send-keys -t backfire-p2:$P2W C-c; sleep 1; tmux send-keys -t backfire-p2:$P2W C-c` (two Ctrl-C within the window stops the supervisor), then `tmux send-keys -t backfire-p2:$P2W 'env -u P2_DUMP_AUDIO P2_ENGINE=local HUB_URL=<hub url> bash detection/scripts/run.sh' Enter`. Wait ~6 s: `curl -s localhost:8100/healthz` -> `"ok":true`, `"engine":"local"`, `"primary":"local"`, `"local_reachable":true`, `"stt":{"backend":"riva",...}`, `"hub_subscriber_connected":true`.
5. **Tag it.** `git tag p2-known-good-$(date +%H%M)` (only if step 6 passes; if it fails, delete the tag with `git tag -d` and fix first).
6. **Readiness.** `bash detection/scripts/ready_check.sh --live http://localhost:8100 --tunnel <p2 tunnel URL> --tests` -> ends `READY` with 0 FAIL. Expected: `P2_DUMP_AUDIO off in live process` PASS (`=unset`), `logs/audio empty` PASS, `live HEAD is a p2-known-good tag` PASS (an exact tag, or "same runtime .py as" the newest tag when only non-P2 commits followed), positive control `critical`, negative control `low`. `--tests` strips `PIPELINE_TOKEN` itself, so it passes whether or not `.env` is sourced. A WARN is OK if you can say why. NOT READY -> do not tag; fix the FAIL line.
7. **One rehearsal call** (after the rest of the line is quiet): `set -a; . ./.env; set +a; .venv/bin/python detection/scripts/stream_wav.py --url ws://localhost:8100 --call "rehearsal?token=$PIPELINE_TOKEN" detection/testdata/scam_call_synth.wav` (17 s; prints nothing secret), then `.venv/bin/python detection/scripts/call_report.py --last 1` -> `SUMMARY rehearsal: first alert +~10 s · final s 0.95 · alerts 1 · failovers 0 · 429s 0 · finals 4`, engine=local. (Streams into the live hub as a real test call: tell P1 first, or skip it.) Then `ls logs/audio | wc -l` -> `0` again (dumps stayed off).
8. **Leave it alone.** Watchdog alive (`pgrep -fc watchdog.sh` is read-only; expect 1), no more evals, no llama tuning. Rollback only via section 4.

## 5. Before judging
- Stop evals/benchmarks (shared GPU + NVIDIA key): no `eval/` runs, no acceptance runs, no llama tuning.
- `rm -f logs/audio/*.wav`; make sure `P2_DUMP_AUDIO` is unset/0 (caller audio is not kept on stage).
- `engines.primary` = local, cloud breaker closed, one rehearsal call done, then leave services alone.
- **Run `bash detection/scripts/ready_check.sh --tunnel <p2 tunnel URL>`** (checks `:8100`; for another port add `--live http://localhost:<port>`; the two checks tag/clean-tree only pass in the live checkout) (add `--tests` before the freeze). Read-only: healthz fields, tunnel matches live, `P2_DUMP_AUDIO` off in the live process (key only, never values), `logs/audio` empty, llama answers, watchdog alive, live HEAD is a `p2-known-good` tag and the process is newer than the last `detection/*.py` commit, plus one positive (gift card + secrecy -> critical) and one negative (benign -> low) control through `/detect` (skipped while a call is active). Every FAIL prints a one-line fix. Do not start judging on `NOT READY`; WARN is acceptable if you know why (e.g. cloud breaker open while local is primary).
