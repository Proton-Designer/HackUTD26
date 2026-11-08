# STT independence from the shared NVIDIA key (TASK-049)
Question: if Riva 429s or hangs during judging, does the Whisper fallback hold up? Tools: `detection/eval/stt_fallback.py` (`failure` and `cards`). Synthetic voices only; no transcripts saved.

## 1. Riva failure -> Whisper (in process; real `RivaSTT.transcribe`, `FallbackSTT` and `WhisperSTT`, only Riva's network call is faked)
Six utterances cut from a PSTN-degraded script card, sent one after another. "Warm" = Whisper already preloaded (the normal case, it preloads at startup); "cold" = the first failure pays the model load.

| failure | whisper | per-utterance seconds (u1..uN) | text returned | fails after | bypass engaged after u2 |
|---|---|---|---|---|---|
| resource_exhausted | warm | 1.17 / 1.32 / 1.91 / 1.77 / 1.92 / 5.52 | 6/6 | 2 | True |
| resource_exhausted | cold | 3.61 / 2.05 / 2.05 / 2.16 / 2.1 / 6.31 | 6/6 | 2 | True |
| unavailable | warm | 1.7 / 2.02 / 2.06 / 2.1 / 2.2 / 4.61 | 6/6 | 2 | True |
| unavailable | cold | 2.73 / 1.51 / 1.48 / 1.4 / 1.48 / 4.95 | 6/6 | 2 | True |
| hang | warm | 8.11 / 8.1 / 2.18 / 2.2 / 1.83 / 6.1 | 6/6 | 2 | True |
| hang | cold | 9.17 / 7.84 / 1.76 / 1.95 / 1.81 / 4.63 | 6/6 | 2 | True |

Whisper base.en alone on this CPU: p50 1.60 s, max 2.88 s per utterance (6 utterances, first warm call 1.21 s).

- No utterance lost in any case: every utterance came back with text (6/6).
- The bypass engages after the 2nd consecutive failure, as designed (`BYPASS_AFTER=2`): utterances 3+ skip Riva and cost about 1 s each. The bypass lasts 30 s, then Riva is probed again.
- Fast failures (429 RESOURCE_EXHAUSTED, UNAVAILABLE): the first Whisper final comes in 1.0-1.2 s (warm), 2-3.4 s (cold load). A hang costs `P2_STT_TIMEOUT=6 s` for each of the first two utterances (about 7 s final), and again for one utterance every 30 s when the bypass expires and Riva is re-probed while still hung.

## 2. Whisper-only (base.en, int8, CPU) on the PSTN script cards (variant p28, local llama engine, private ports 8290/8294, llama guard on)
| | Whisper base.en (this run) | Riva (eng2, as reported) |
|---|---|---|
| words matched, 13 cards | mean 96.9%, min 92% (range 92-100%) | 93-96% |
| endpoint -> final | p50 1.59 s, max 3.62 s | about 3.5 s |
| scam cards alerting (10) | 10 of 10 | see eng2 |
| benign cards alerting (3) | 0 of 3 (b1 reached s 0.45) | see eng2 |
Per-card alert time vs the end of the ask line: 7 of 10 fired before the ask line ended (the fast path acts on earlier lines), the other three at +1.4, +1.4, +1.7 s and one at +3.5 s (s2). Per-card rows are in the JSON the tool writes (`--json`), not committed.

## Caveats
- Whisper heard clean Magpie TTS with synthetic band-pass/noise. Real human voices on a real phone line are harder, and Whisper base.en is generally less robust than Riva on accents and noise. I did not measure that: the only real-voice calls (benign "hello" tests) have no reference text.
- Whisper runs on this laptop's CPU; the judging machine may be slower. Riva latency here includes the shared key's rate-limit waits.
- eng2's Riva numbers are quoted from the lead's brief, not re-run by me. One run per card, n=13.

## Recommendation (3 lines)
1. The fallback path works: no lost utterances, bypass after 2 fails, 1-1.2 s per final once bypassed; keep it, and do not rely on Riva alone.
2. Because the key is shared and already 429ing, set `P2_STT=whisper` as the PRIMARY for judging (equal or better words matched and about half the final latency on the cards, no dependency on the shared key), keeping Riva only if a quick on-site real-voice test shows Whisper clearly worse.
3. If Riva stays primary, lower `P2_STT_TIMEOUT` to about 3 s and expect ~7 s finals on the first two utterances of a Riva outage.
