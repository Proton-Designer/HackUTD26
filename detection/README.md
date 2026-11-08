
## Streaming (eng2)
Run: bash detection/scripts/run.sh (:8100); tunnel: bash detection/scripts/tunnel.sh. Test client: .venv/bin/python detection/scripts/stream_wav.py --url ws://localhost:8100. Synthetic WAV regenerated with detection/scripts/make_testwav.py (Magpie TTS). Env: HUB_URL PIPELINE_TOKEN P2_ENGINE P2_STT P2_ENDPOINT_MS.

## detect API (eng1)
- `await detection.detect.detect(call_id, window_text, metadata, engine)` -> risk.update data dict (LLM + rule backstop, never raises).
- `detection.detect.quick(window_text, engine="cloud")` -> same shape, **rules only, sync, no I/O (<5 ms)**. Call it on every partial/final to alert on a rule floor >= 0.80 before the LLM returns; merge by taking the max of s with the later `detect()` result.
- Acceptance: `bash detection/scripts/acceptance.sh` (~1-3 min, hub :8190 + P2 :8191, real NVIDIA STT/LLM, synthetic TTS WAVs cached in detection/testdata/acc/) prints a PASS/FAIL/SKIP table; engine=local case runs only if LOCAL_LLM_URL answers.

## P2 overview (eng1)
**What it does.** Caller-only audio (from P1's relay) -> STT (`/stt/{call_id}`, `detection/stream.py`) -> per-call alert machine (`alert.py`, code not an LLM) -> `detect()` -> `risk.update` / `alert.fired` posted to the hub (`hub.py`). The detector has no tools and returns typed output; caller words are untrusted data.
**Models.** Pinned in `contracts/models.md`: cloud primary `nvidia/nemotron-3.5-lightning-30b-a3b` (thinking off, `json_object`, 2.5 s timeout). The three 404 ids there are unusable. `P2_ENGINE=cloud` (default) or `local` (eng3's `engines/local.py`, an Ollama-style server at `LOCAL_LLM_URL`; skipped when unreachable). Both engines share `prompt.py` so the comparison is fair.
**Scoring.** On every final utterance the alert machine runs `quick()` (rules only, sync, no I/O) over the last 6 utterances and can alert before the LLM returns, then `detect()` (LLM + rules) and takes `max(quick, llm)` for that window. Rules only raise s: hard ask floor 0.82, gift card/OTP 0.9, two hard asks or ask+secrecy 0.95, injection 0.85, with a negation guard. Chips come from `schema.build_chips` (max 4); a campaign-similarity match (`campaign.py`) adds "Known scam campaign" and +0.1 and needs two sentences matching the same script.
**Bands.** low < 0.40, watch 0.40-0.79, high 0.80-0.94, critical >= 0.95. First alert at s >= 0.80, or a hard ask with s >= 0.60.
**Budget and fail-open.** Cache of 512 windows, token bucket `P2_CLOUD_RPM` (35/min, waits at most 0.5 s), 4 s overall timeout. Any failure returns the rules-only result; `detect()` never raises into P1.
**DEMO_MODE=1.** Serves `detection/demo_cache.json` (63 recorded LLM answers for the script-card and mock-call windows). Exact key = engine|model|normalized text; on a miss, the nearest recorded window by char n-gram cosine >= 0.92 is served only if the live rule asks are a subset of the cached asks; the rule floor still applies. Off outside DEMO_MODE. Re-record with `DEMO_RECORD=1 PYTHONPATH=. .venv/bin/python detection/record_demo.py` (resumable, <= 18 rpm). Log lines: `demo cache hit` / `fuzzy hit` / `miss`.
**Run / check.** See `detection/RUNBOOK.md`. Tests: `.venv/bin/python -m pytest -q detection`.
**Checked in a DEMO_MODE run (second port :8101, 2026-11-08):** 63 card+mock windows through `POST /detect`: 63 exact hits, 0 fuzzy, 0 misses, max 0.07 s per call. `replay_mock --real` alerted on the IRS call and not on the bank call.
**Honest limits.** (1) Live STT text can differ from the script, so DEMO_MODE hits depend on the fuzzy match; in the real-STT acceptance run, lines outside the recorded set missed (they went live). (2) Rate budget is shared by the team key; when exhausted a window gets rules only. (3) No Super verifier (not servable). (4) `engine=local` is a 4B model on a laptop GPU: slower (p50 2.7 s) and over-flags the AI-address field; the cloud engine is the default. (5) Campaign matching is only as broad as the script cards plus the dev-split eval rows. (6) Synthetic data only; thresholds were tuned on small sets.
## Reliability, safety rules, and what changed (eng1)
- **Cloud -> local failover** (`detect.py`, 463280f/34b788e): if the cloud engine fails or is slow, the same window is scored by the local engine when `LOCAL_LLM_URL` answers a cached probe (10 s, 0.5 s timeout). Cloud gets 2 s when local is reachable; the overall cap is 4 s. If both are down the window gets rules only. `P2_FAILOVER=0` turns it off.
- **Circuit breaker** (75ece5f): 3 cloud failures (429/5xx/timeout/transport) in 30 s open it for 60 s, so calls go straight to local instead of waiting out the timeout. Then one half-open probe; backoff 60/120/240 s, capped at 300. Cached answers are still served while open. `/healthz` shows `cloud_breaker`. `P2_BREAKER=0` disables it. State is per process.
- **Hold last score** (bfa0bac, `alert.py`): a window scored by rules only because the engine failed keeps the last LLM-backed s for up to 10 s / 3 windows, then decays. A real low LLM score always passes through. No dip, no spurious re-alert.
- **Continue** (34b788e, 476aca8): after the user taps Continue, the utterance window is cleared and results scored before it are dropped, as are late finals whose audio ended before Continue. Benign talk then restores s quickly; a NEW hard ask still re-alerts.
- **Fewer false alarms** (7859d33): negation is clause-scoped ("we never ask for codes" does not fire; "never ask for codes, but read me the 6 digits" does), a weak bare-noun ask (gift card, crypto, SSN, card, wire transfer) needs a request verb and must not be the user's own past action, and the shared prompt has WARNING != REQUEST, CONFIRMATION != REQUEST, GIVEN != ASKED examples. Rules only ever raise s; nothing the caller says lowers it.
- **AI-address gating** (8874f7f): the LLM's `addresses_ai_system` flag counts only if the text has an AI cue or the injection rule fired; it never lowers s.
- **Chips** (1715892): negative chips ("No pin ask") are dropped; chips describe risk signals only.
- **Auth and logs**: `PIPELINE_TOKEN` (if set) is required on WS `/stt` and `POST /detect`; unset = open and logged. `detection/scripts/call_report.py` prints a per-call timeline from `p2.log` (8e18ef4).

## Evaluation (synthetic, n=60 test rows: 33 scam / 27 legit)
Numbers are from `detection/eval/RESULTS.md` (eng3, 1242399), the BEFORE table scored on code `20ca58a`, before the false-alarm fixes above. Thresholds were tuned on the dev split only, frozen in `FROZEN.json`, then the test split was scored once. All cells carry Wilson 95% CIs in RESULTS.md; n is small.

| test split | rules baseline (thr 0.85) | local Nemotron Nano 4B (thr 0.95) |
|---|---|---|
| scam recall | 85% (28/33) | 100% (33/33) |
| adversarial / injection recall | 69% (9/13) / 86% (6/7) | 100% (13/13) / 100% (7/7) |
| false alarm, all legit | 19% (5/27) | 7% (2/27) |
| false alarm, keyword-bait legit | 57% (4/7) | 29% (2/7) |
| latency p50 | 0 ms | 2.7 s |

Honesty notes: the cloud engine was **not scored on test** (the shared NVIDIA key returned 429s), so there is no cloud test number; cloud dev numbers exist but are optimistic (tuned on dev). The "rules" column is eng3's plain keyword baseline, not the production `rule_scan`. Local over-flags the AI-address field (27/55 false positives before the fix). The AFTER table (current code) goes in the slot below when TASK-028 lands.
<!-- EVAL TABLE (eng3) -->
## Local engine + eval (eng3)
Local engine (`engine=local`): Nemotron 3 Nano 4B `Q4_K_M` (nvidia/NVIDIA-Nemotron-3-Nano-4B-GGUF) served by llama.cpp `llama-server` on the laptop GPU (RTX 3050 Ti 4 GB).
This WSL2 box has NVIDIA driver 546, which Ollama (needs 550+) and the Linux CUDA-12.8 llama.cpp builds reject, so the working path is the **Windows llama.cpp CUDA-12.4 build run through WSL interop**.
One-time setup: download `llama-b12199-bin-win-cuda-12.4-x64.zip` and `cudart-llama-bin-win-cuda-12.4-x64.zip` from github.com/ggml-org/llama.cpp releases, extract both into `/mnt/c/backfire-llama/`, and copy the GGUF there.
Run: `bash detection/engines/run_local_llm.sh` (binds the WSL gateway IP, port 8101). Then `export LOCAL_LLM_URL=http://$(ip route | awk '/default/{print $3}'):8101 LOCAL_MODEL=nemotron-nano-4b` (127.0.0.1 does not reach a Windows process).
Smoke: `curl $LOCAL_LLM_URL/health`; `POST /detect` with `"engine":"local"`. If the server is down, detect() fails open to rules.

Eval: `.venv/bin/python -m detection.eval.run_eval --engine {rules,cloud,local} --split dev`, then `--freeze` (tunes thresholds on dev only, writes FROZEN.json), then `--engine all --split test`, then `--report` (writes RESULTS.md). Rows: `data/eval/scripts.jsonl` + `detection/eval/extra_rows.jsonl` (regenerate with `python -m detection.eval.gen_extra_rows`). Scores are cached in `detection/eval/.cache` (gitignored); cloud is throttled to 20 rpm.
Tests: `.venv/bin/python -m pytest -q detection/tests/test_local.py detection/tests/test_eval.py` (HTTP mocked).
