# Real PSTN calls through the live pipeline (TASK-045)

Aggregate numbers only. Audio dumps (`logs/audio/`) and transcripts stay local and are gitignored. Source: `logs/p2.log`, summarized with `detection/scripts/call_report.py`. Times are in seconds from the first audio frame. Updated 03:40 CT, 2026-11-08.

| call | time | length | utterances / finals logged | STT after endpoint p50 / max | engine per window | failovers / rules fallbacks | first risk >= thr | alert | final band | truth |
|---|---|---|---|---|---|---|---|---|---|---|
| 7420a294 | 02:15 | 22 s | 0 / 0 | n/a | none (no speech reached STT) | 0 / 0 | n/a | no | n/a | benign test |
| a99a2060 | 02:30 | 15 s | 2 / 2 | 0.48 s / 0.71 s | 1 cloud, 1 local | 1 (cloud 429 -> local) / 0 | none | no | low (0.00) | benign test |
| 4d8dd2f8 | 03:04 | 72 s | 11 / 7 | 0.53 s / 2.07 s | 4 local, 3 cloud-after-fallback (9 risk updates) | 0 / 3 (local TimeoutError) | none | no | low (0.00) | benign test |
| 922262b2 | 03:06 | 24 s | 6 / 6 | 2.25 s / 6.51 s | 4 local | 0 / 1 (local TimeoutError) | none | no | low (0.00) | benign test |
| 37cbc8e2 | 03:17 | 14 s | 2 / 2 | 0.34 s / 0.37 s | 2 local | 0 / 0 | none | no | low (0.00) | benign test |
| 8894eb46 | 03:20 | 33 s | 2 / 1 | n/a | no windows scored | 0 / 0 | n/a | no | n/a | benign test |
| 6352e850 | 03:26 | 146 s | 23 / 14 | 0.24 s p50 / 0.84 s max | 14 local | 0 / 0 | none | no | low (0.05) | scam-card role-play: the card was read but the detector heard nothing |

**6352e850 (P1 scam-card call) is a miss caused upstream, not by the detector.** The inbound track carried 28 s of digital zero while the card was read, which is a P1-side mute (the detector only heard greetings and "can you hear me" chatter). The risk stayed at 0.00-0.05 for 14 windows, which is correct for what it heard. Lead's positive control: the same card text sent to live `/detect` (local engine) scores s 1.00 critical in about 1 s. So detector recall on the card text is fine, and the failure is the audio path. A later call (497ef1d4, 03:3x) was still in progress when this was written and is not in the table.

## Takeaway
1. The pipeline ran on real PSTN audio end to end (Telnyx mu-law 8 kHz -> Riva STT -> local llama): 6 calls, 0 crashes, calls always connected, 0 false alerts.
2. Six of the seven calls are benign tests (mostly "Hello"); the scam-card call lost its audio upstream. No real call has put a scam ask in front of the detector, so real-call recall is unmeasured. Only about false alarms (0 alerts in about 30 windows), and the caveat is that the windows are tiny.
3. The real failure was latency under contention: llama TimeoutErrors (4 windows, 03:04-03:06) happened while eval runs shared the single-slot GPU. The runner now pauses while `active_stt_sockets>0`. STT finals arriving 5.7-6.5 s after endpoint in 922262b2 came after the audio had ended and were dropped as late.

## Why finals lagged in 922262b2 (5.7-6.5 s) but not elsewhere (log + code read, no replay yet)
Most likely cause: head-of-line blocking in the per-call STT worker. `stream.py` runs one worker per call that does `handle_utterance` = transcribe, emit, then `await on_final(...)`. `alert.py:on_final` awaits `detect()` (LLM call) inside that same worker, so the next utterance is not even transcribed until the previous window's detect returns. Evidence in the log: lag grew 0.21 -> 0.32 -> 1.53 -> 2.98 s as local detect calls took ~2-3 s each (u2, u3, u4). The u4 detect then hit a local TimeoutError (about 5 s, then a cloud failover). u5 and u6 were transcribed only after it returned, so their finals logged 6.5 s and 5.7 s after endpoint. The audio had already ended by then (ws closed at +24 s), so both were dropped as "call already ended".
Checked the executor-starvation hint (stt.py:72 `wait_for(to_thread)` leaving Riva threads running): no evidence of it in this call. The log has 0 "primary STT failed" / Riva timeout lines for the whole session, `primary_failures=0`, and the only whisper activity was the background preload at 03:04:03 (two minutes earlier, already finished). The u5 final landed 0.26 s after u4's detect returned (03:06:10.77 -> 11.03), so the STT call itself was fast and the delay was the wait in the worker. The risk is real in principle (cancelled Riva threads keep holding default-executor slots, and Whisper uses the same pool), but it did not occur here.
Second hypothesis (not excluded): llama was busy with a competing local run (eval/bench) at 03:04-03:06, which made the local detect slow and then time out. That is what lengthens the block, so it is the trigger and the worker chain is the amplifier. Riva stall, Whisper fallback and VAD are unlikely: `primary_failures=0`, no "primary STT failed" line, and the STT call itself is quick in the other calls.
Consequence for the demo: with a slow local detect, a later scam ask is transcribed late, and the rules fast path (which runs at the start of `on_final`) is also delayed by it. Suggested fix, not in my lane: run `on_final` as a background task (or keep the STT worker separate from detect), keeping per-call order only for the window append.

## Replay harness (TASK-047 acceptance number)
`python -m detection.eval.replay_call WAV --url ws://127.0.0.1:8104 --log <target service log> --label before|after --json out.json` streams a call WAV (8 kHz mono: a `logs/audio` dump or a script-card wav) as Telnyx mu-law frames in real time to `/stt/<fresh id>`, then reads the target's log and prints per utterance: endpoint -> final and endpoint -> first `risk.update` (a risk shared by two finals means the window was coalesced), plus alerts and first-alert time. No transcript text is printed or saved. Guards: refuses while live :8100 has `active_stt_sockets>0` (`--wait` pauses instead), and needs the target `/healthz`. Parsing and summary are unit-tested (`tests/test_eval_replay.py`). BEFORE (current trunk) vs AFTER (eng2's SHA) results go in the table below after CLEAR.

| run | audio | finals p50 / max | endpoint->risk p50 / max | alerts | first alert |
|---|---|---|---|---|---|
| before (trunk ea2ddb9) 922262b2 | 24 s | 0.77 / 4.69 s | 3.39 / 7.32 s | 0 | none |
| after (1a7ea68) 922262b2 | 24 s | 0.28 / 0.31 s | 2.10 / 3.23 s | 0 | none |
| before (trunk ea2ddb9) 4d8dd2f8 | 72 s | 0.26 / 0.31 s | 2.84 / 3.33 s | 0 | none |
| after (1a7ea68) 4d8dd2f8 | 72 s | 0.27 / 0.31 s | 3.28 / 5.08 s | 0 | none |

Replayed in real time on :8104 with P2_ENGINE=local, idle live service, one llama request at a time (guard on). The before replay of 922262b2 reproduces the live lag (final lag 0.28 -> 4.69 s, growing); after the TASK-047 fix it stays at ~0.3 s. 4d8dd2f8 never had the lag, so finals are unchanged. Its after risk times are higher with one cloud failover at u4 (5.08 s); other eval runs were probably using llama then (single slot), so this is noise, not a regression. n=2 replays, no repeats.

## Caveats
- n is tiny: 7 calls, about 50 speech windows, one speaker (a teammate).
- Role-play only. No real victim, no real scammer. The scam-card call is scripted by a teammate.
- "Truth" labels were assigned by hand from the call purpose, not from a transcript audit.
- Not a held-out estimate of recall. Use RESULTS.md (synthetic) for that.
