# P3 decoy (server side) + voice enrollment

The real decoy for the hub/Telnyx path: drop-in for P1's stand-in via `P3_DECOY_URL`, and the clone voice via `P3_VOICE_URL`.
Same brain as the on-phone decoy in `android_voip/backfire` (tested live on a Galaxy S22).

```
caller audio (PCMU 8k, from P1's relay) -> P2's Segmenter + speech-to-text (detection/, Parakeet on NVIDIA Riva)
  -> Nemotron (NVIDIA cloud, DECOY_MODEL, default nvidia/nemotron-3.5-bolt-e4b) as "Margaret", placeholders only
  -> code guardrails + per-call fake values (decoy.fake_value, guardrail.tripped)
  -> voice: Magpie TTS Zero-shot with Maria's enrolled voice (else Magpie Multilingual EN-US.Aria.Calm, labeled synthetic)
  -> PCMU 20 ms media frames back, paced in real time; `clear` when the caller talks over it (barge-in)
call ends -> extractor (model proposes, code validates) -> artifacts.extracted
```

## Run (on the hub machine, so everything stays on localhost)

```bash
pip install -r decoy/requirements.txt        # + ffmpeg
NVIDIA_API_KEY=nvapi-... HUB_URL=http://127.0.0.1:8000 PIPELINE_TOKEN=... \
  python -m uvicorn decoy.app:app --host 127.0.0.1 --port 8300
# hub: P3_DECOY_URL=ws://127.0.0.1:8300  P3_VOICE_URL=http://127.0.0.1:8300
```

Access: direct loopback, or `x-pipeline-token: $PIPELINE_TOKEN`. Anything else is refused (fail closed).

| Endpoint | |
|---|---|
| `WS /decoy/{call_id}` | Telnyx frames both ways (seam #2). In: connected/start/media (inbound)/stop. Out: media, clear |
| `POST /voice/enroll` | `{recording: base64, mime, consent_version}` -> `{voice_id}`. Accepts webm/opus, ogg, mp4/AAC (iOS), wav. Keeps only the loudest 8 s of speech as the voice prompt, in `decoy/voices/` (git-ignored). Emits `voice.enrolled` |
| `DELETE /voice/{voice_id}` | Deletes the prompt; emits `voice.deleted` |
| `GET /healthz` | `{ok, cloned_voice, model}` |

The decoy speaks with the most recently enrolled voice (single-customer demo). No watermark is applied (don't claim one).

## Measured (laptop, NVIDIA hosted APIs)
- Reply decision 500-750 ms (bolt-e4b; lightning was 429 rate-limited on the shared key).
- Magpie: synthetic ~0.5 s per sentence; clone 1.0-1.8 s per sentence (faster than real time). Fillers cover the gap.

## Test
```bash
python -m pytest -q decoy/tests/test_core.py                       # offline rules: fake values, guardrails, validators, framing
python decoy/tests/relay_sim.py ws://127.0.0.1:8300 /tmp seg0.wav seg1.wav   # acts like P1's relay with caller WAVs
```
