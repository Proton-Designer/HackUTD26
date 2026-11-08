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

## TASK-054: peer-to-peer echo leak (measured 04:45, aggregates only)
- Data available: `logs/p2.log` holds 11 call ids; the newest real call is 497ef1d4 (03:32, 14 finals, 61 s, 0 alerts, risk 0.00 throughout, a two-way "can you hear me" chat). No real call has been logged since 03:33, so **no call yet exists in the #75 mode (customer in app, decoy as customer)**.
- Decoy / customer text is not in p2.log (P2 never logs it) and the hub `/events` history was not reachable from this worktree (nothing listening on the local hub ports), so the fuzzy-match count against decoy.turn(speaker=decoy) could not be run: **0 of 0 measurable calls**.
- Only known leak: 922262b2 (03:28, "Maria" as caller speech, 1 final). It did not move risk: every risk.update for that call is s=0.00 band=low and no alert fired.
- Verdict: no evidence a guard is needed; the leak is real on PSTN but harmless so far, because a leaked decoy line is not scam content. Re-measure on the first #75-mode call (needs decoy.turn events from the hub). The proposed guard (drop caller finals fuzzy-matching decoy text from the last ~6 s) is NOT built.

## adad65a0: first real PSTN scam alert (04:46:41-04:47:26, Telnyx PCMU 8 kHz, live f65e0d9, local engine)
Team actor reading a known script, n=1. Quoted lines are team-actor speech.
| t into call | event | result |
|---|---|---|
| +7.3 s / +11.2 s | benign openers ("What's up?", "Do you want to check the screen?") | s=0.05 low |
| **+12.3 s** | fast-path partial, mid-sentence, before the final | **alert, s=0.82 high, asks=ssn** |
| +17.5 s | final "give me your social security card and don't tell anybody" | s=0.95 critical, asks=secrecy,ssn |
| +25 to +33 s | later benign-sounding lines, scores held | s=0.95 critical |
| +45.4 s | u7 "give me your money" | dropped, arrived after the call ended (expected) |
Finals arrived 0.23-0.35 s after endpoint; 1 alert, 0 failovers, 0 429s, 7 utterances (4 finals scored). Caveat: n=1, a team actor, a script the team knows; this shows the path works on a real phone line, not a detection rate.
