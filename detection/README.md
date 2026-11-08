
## Streaming (eng2)
Run: bash detection/scripts/run.sh (:8100); tunnel: bash detection/scripts/tunnel.sh. Test client: .venv/bin/python detection/scripts/stream_wav.py --url ws://localhost:8100. Synthetic WAV regenerated with detection/scripts/make_testwav.py (Magpie TTS). Env: HUB_URL PIPELINE_TOKEN P2_ENGINE P2_STT P2_ENDPOINT_MS.

## detect API (eng1)
- `await detection.detect.detect(call_id, window_text, metadata, engine)` -> risk.update data dict (LLM + rule backstop, never raises).
- `detection.detect.quick(window_text, engine="cloud")` -> same shape, **rules only, sync, no I/O (<5 ms)**. Call it on every partial/final to alert on a rule floor >= 0.80 before the LLM returns; merge by taking the max of s with the later `detect()` result.
- Acceptance: `bash detection/scripts/acceptance.sh` (~1-3 min, hub :8190 + P2 :8191, real NVIDIA STT/LLM, synthetic TTS WAVs cached in detection/testdata/acc/) prints a PASS/FAIL/SKIP table; engine=local case runs only if LOCAL_LLM_URL answers.
