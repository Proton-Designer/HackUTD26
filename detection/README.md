
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
**Honest limits.** (1) Live STT text can differ from the script, so DEMO_MODE hits depend on the fuzzy match; in the real-STT acceptance run, lines outside the recorded set missed (they went live). (2) Rate budget is shared by the team key; when exhausted a window gets rules only. (3) No Super verifier (not servable). (4) `engine=local` is untested end to end here. (5) Campaign matching is only as broad as the script cards plus the dev-split eval rows. (6) Synthetic data only; thresholds were tuned on small sets.
<!-- EVAL TABLE (eng3) -->
## Local engine + eval (eng3)
Local engine (`engine=local`): Nemotron 3 Nano 4B `Q4_K_M` (nvidia/NVIDIA-Nemotron-3-Nano-4B-GGUF) served by llama.cpp `llama-server` on the laptop GPU (RTX 3050 Ti 4 GB).
This WSL2 box has NVIDIA driver 546, which Ollama (needs 550+) and the Linux CUDA-12.8 llama.cpp builds reject, so the working path is the **Windows llama.cpp CUDA-12.4 build run through WSL interop**.
One-time setup: download `llama-b12199-bin-win-cuda-12.4-x64.zip` and `cudart-llama-bin-win-cuda-12.4-x64.zip` from github.com/ggml-org/llama.cpp releases, extract both into `/mnt/c/backfire-llama/`, and copy the GGUF there.
Run: `bash detection/engines/run_local_llm.sh` (binds the WSL gateway IP, port 8101). Then `export LOCAL_LLM_URL=http://$(ip route | awk '/default/{print $3}'):8101 LOCAL_MODEL=nemotron-nano-4b` (127.0.0.1 does not reach a Windows process).
Smoke: `curl $LOCAL_LLM_URL/health`; `POST /detect` with `"engine":"local"`. If the server is down, detect() fails open to rules.

Eval: `.venv/bin/python -m detection.eval.run_eval --engine {rules,cloud,local} --split dev`, then `--freeze` (tunes thresholds on dev only, writes FROZEN.json), then `--engine all --split test`, then `--report` (writes RESULTS.md). Rows: `data/eval/scripts.jsonl` + `detection/eval/extra_rows.jsonl` (regenerate with `python -m detection.eval.gen_extra_rows`). Scores are cached in `detection/eval/.cache` (gitignored); cloud is throttled to 20 rpm.
Tests: `.venv/bin/python -m pytest -q detection/tests/test_local.py detection/tests/test_eval.py` (HTTP mocked).
