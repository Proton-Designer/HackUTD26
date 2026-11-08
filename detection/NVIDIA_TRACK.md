# NVIDIA pieces in P2 (detection) and where they are used
P2 listens to the **caller's audio only**, transcribes it, scores scam risk with a small model, and raises an alert. Numbers are from `detection/PITCH_NUMBERS.md` (row #), which names each source file and caveat.

## What we use
| NVIDIA piece | Role in P2 | Where |
|---|---|---|
| **Nemotron 3 Nano 4B** (Q4_K_M GGUF, llama.cpp, laptop GPU) | **Live primary detector.** Every real call since 02:42 CT 2026-11-08 ran `engine=local`. | `detection/engines/local.py`, `engines/run_local_llm.sh`, `contracts/models.md` |
| **Nemotron 3.5 Lightning 30B-A3B** via build.nvidia.com | **Failover** when the local model is slow or down (4 s local, 6 s total), then rules. | `detection/engines/cloud.py`, `detect.py` |
| **Riva Parakeet** hosted ASR (NVCF gRPC) | **Primary speech-to-text** for the phone stream. | `detection/stt.py` |
| Whisper base.en (not NVIDIA) | Tested CPU fallback if Riva fails (bypassed 30 s after 2 failures). | `detection/stt.py` |
| Magpie TTS (hosted) | Only to make synthetic test calls (script cards, acceptance). Not in the live path. | `detection/scripts/pstn_cards.py` |

## Why
- **Privacy:** scoring text stays on the laptop on the normal path; the cloud model only sees caller text on failover. Audio goes to hosted Riva unless `P2_STT=whisper` (so we do **not** claim "nothing leaves the device").
- **Latency:** local model p50 **1.7 s** alone, 3.2 s with 2 concurrent calls, 4.0 s with 4 (#5, RTX 3050 Ti 4 GB, one GPU slot). A rules fast path alerts on partial speech before any model returns. Riva finals arrive ~0.25-1 s after the endpoint, Whisper ~1.0-1.2 s (#11, `eval/STT_FALLBACK.md`).
- **Cost/limits:** no per-call API cost on the primary path, and the shared hosted key is rate limited (~40 rpm), so it is only the failover.

## Measured (synthetic unless stated)
- Local model: **33/33** test scams alerted, **2/27** false alarms; fresh held-out **20/20** and **1/20** (#1, #2). Keyword baseline 28/33 and 8/20.
- If both models fail, rules alone catch 26/33 and 10/20 (#3).
- Phone-quality script cards: **28/28** scam rows alerted before the first ask line ended, **9/9** benign quiet (#10, `eval/PSTN_CARDS.md`).
- Real phone calls (team actors, scripted): alert 12-15 s into the call on the scam calls (#12, `eval/REAL_CALLS.md`); zero false alarms on the real calls replayed.
- Failure drills: llama down, cloud down, Riva refused, hub restart, P2 restart all still produced the alert or recovered (`eval/DRILLS.md`).

## Honest caveats
- Eval sets are synthetic, written by the team; thresholds were tuned on dev splits. Not a detection-rate estimate for real scammers.
- Real calls: **n=2** scripted scam calls by team actors (plus one chatter call that stayed quiet), not strangers; English-only speech-to-text.
- The laptop GPU stands in for a phone; Nano 4B on 4 GB serves one call at a time well, 4 concurrent calls queue (4.0 s p50).
- The cloud model has no clean test number (rate limited during scoring, #8).
