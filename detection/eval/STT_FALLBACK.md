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
Per-card alert time vs the end of the ask line: 6 of 10 fired before the ask line ended (earlier lines already carried the signal), the other four at +1.4, +1.4, +1.7 and +3.5 s (s2). Per-card rows are in the JSON the tool writes (`--json`), not committed.

## Caveats
- Whisper heard clean Magpie TTS with synthetic band-pass/noise. Real human voices on a real phone line are harder, and Whisper base.en is generally less robust than Riva on accents and noise. I did not measure that: the only real-voice calls (benign "hello" tests) have no reference text.
- Whisper runs on this laptop's CPU; the judging machine may be slower. Riva latency here includes the shared key's rate-limit waits.
- eng2's Riva numbers are quoted from the lead's brief, not re-run by me. One run per card, n=13.

## Recommendation (3 lines)
1. The fallback path works: no lost utterances, bypass after 2 fails, 1-1.2 s per final once bypassed; keep it, and do not rely on Riva alone.
2. Because the key is shared and already 429ing, set `P2_STT=whisper` as the PRIMARY for judging (equal or better words matched and about half the final latency on the cards, no dependency on the shared key), keeping Riva only if a quick on-site real-voice test shows Whisper clearly worse.
3. If Riva stays primary, lower `P2_STT_TIMEOUT` to about 3 s and expect ~7 s finals on the first two utterances of a Riva outage.

## 3. Real human voices: Whisper replay vs live Riva on the 8 real PSTN dumps (TASK-053; aggregates only, no text)
Whisper base.en (`P2_STT=whisper`, local llama) replayed in real time on :8104 from the same dumps; Riva = the live finals logged for the same call. Riva is a proxy, not ground truth (there is no reference text). Agreement = share of Riva's words also in Whisper's finals (multiset). Both sides are cut at 80 chars per final in the logs.

| call | Riva finals / Whisper finals | agreement (Riva words found in Whisper / reverse) | Whisper endpoint->final p50 / max | Riva live p50 |
|---|---|---|---|---|
| 37cbc8e2, 8894eb46, a99a2060 (1-2 word "hello" calls) | 2/2, 1/1, 2/2 | 100% | 0.6-1.0 s | ~0.3 s |
| 922262b2 | 6 / 6 | 88% / 100% | 0.67 / 0.99 s | ~0.3 s (lagged by blocking, now fixed) |
| 4d8dd2f8 | 7 / 6 | 69% / 45% | 1.13 / 1.5 s | ~0.3-2 s |
| 497ef1d4 | 10 / 8 | 48% / 71% | 0.94 / 5.39 s | ~0.25 s |
| 6352e850 (146 s, 28 s of digital zero) | 14 / 12 | 60% / 74% | 1.04 / 8.25 s | 0.24 s |
| 93c95fd6 (93 s, the call with real scam content) | 13 / 16 | 90% / 69% | 1.11 / 3.3 s | ~0.25 s |
- On the one call with a real scam ask (93c95fd6) both engines raised an alert: live Riva +18.3 s from call start, Whisper replay +21.9 s (about 3.6 s later, from slower finals and the extra window).
- Dropped / hallucinated: no Whisper final inside the 28 s digital-zero stretch of 6352e850 (finals at 45.7 s and 82.5 s only), and no "Thank you."-style hallucination. Whisper had 2 finals with no Riva counterpart in 8 calls and missed 4 Riva finals (short words); Riva also produced a few odd short finals.
- Lower agreement on the three conversational calls means the two engines disagree on short or noisy phrases. I cannot say which is right without reference text.
- **Latency is the real difference on real voices:** live Riva answered in ~0.25 s after endpoint (when the key was healthy); Whisper p50 is ~1.0-1.2 s with spikes of 4-8 s in 3 of 8 replays (497ef1d4, 6352e850, 93c95fd6) while other eval jobs shared the CPU (load average 3-5). The 6 s Riva finals seen earlier were the blocking bug, not Riva.
- `P2_STT=whisper` never constructs Riva and does not import `riva`: checked with `NVIDIA_API_KEY` unset (`WhisperSTT`, no riva modules loaded). It does fetch the model from huggingface.co on first use, it is not preloaded at startup (the first utterance pays the load: 1.4 s final in my warm-up), and the first transcribe in a fresh process is cold.

**Verdict: do NOT switch the default.** The synthetic cards favored Whisper, the real voices do not: Riva is about 4x faster when its key answers. Keep Riva primary with the tested Whisper fallback (no lost utterances, bypass after 2 fails), and switch to `P2_STT=whisper` only if Riva probes 429/hang at judging time (flip, restart, `P2_STT_TIMEOUT` ~3 s if Riva stays primary). Whisper still catches the scam call, about 3.6 s later.
Caveats: n=8 calls, one or two speakers, role-play, no reference transcript, CPU shared with teammates' jobs during the replays.
