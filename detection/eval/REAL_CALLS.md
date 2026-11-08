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

**adad65a0 full chain (numbers from P1's hub journal, not measured by P2):** alert +12.5 s, takeover ("Scammer Get Scammed") +18.2 s, decoy 4 turns (median 1.09 s, max 1.45 s), caller hung up +46 s, intel block +75 s. This is the first full real-PSTN chain (detect, takeover, decoy, hang-up, block). P2's own log timing above (alert +12.3 s) agrees within 0.2 s. Same caveat: n=1, team actor, known script.

## b58cec24: SIMULATED call into the live service (benign), NOT a real phone call
P1's phone-free simulated call (a script streamed in Telnyx stream format, 04:54:48-04:55:24, media format `audio/x-mulaw`, start keys include `tracks`). A dentist-office reminder: 4 utterances, finals 0.27-0.33 s after endpoint, every risk update s=0.05 low, 0 alerts, 0 failovers. It confirms the live service accepts that start-message variant and stays quiet on benign talk; it is not a real-PSTN true negative and is not counted in the real-call numbers.

## 499a20d2: second real PSTN scam call (IRS + OTP/SSN), live local engine
Team actor, scripted, n=1. Live first alert +14.9 s (P1's number), IRS impersonation + one-time-code / SSN asks, max s 0.95, 0 false alarms. Replayed through the private stack (HEAD eff9462, local engine): first alert +14.2 s, same chips, max 0.95, 10 finals scored.

## TASK-063 replay table (real PSTN dumps through private hub :8190 + P2 :8102 on eff9462, local engine; aggregates only)
| call | length | finals scored | first alert | max s | false alarms | note |
|---|---|---|---|---|---|---|
| adad65a0 | 43 s | 7 | +11.8 s (SSN ask) | 0.95 | 0 | scam script |
| 0afc3446 | 99 s | 13 | none | 0.05 | 0 | team chatter, no scam content; `user.action hang_up` posted at +6.6 s (as the live Decline tap): all finals still scored (live run before the TASK-061 fix scored 0 of 14) |
| 499a20d2 | 59 s | 10 | +14.2 s (IRS, OTP/SSN) | 0.95 | 0 | scam script; s falls to 0.05 on the last benign closing line after the alert |
Caveat: n=3, team actors, scripts the team knows; shows the path works on real phone lines, not a detection rate.

## Regression @ 1fbf6de (TASK-071, every saved real-audio dump replayed through the current trunk build; aggregates only)
Private P2 :8104, local engine (nemotron-nano-4b), real time, HUB_URL dead, one run at a time with the live-socket guard (`--wait`). Expected = earlier replay/live result in this file. 11111111-* (synthetic) and b58cec24 (simulated) excluded.
| call | length | expected | alert time / quiet | s and band at end | finals lag max | pass |
|---|---|---|---|---|---|---|
| adad65a0 | 44 s | alert +11.8 s (SSN) | first +11.63 s | 0.95 critical | 0.40 s | PASS (-0.2 s) |
| 499a20d2 | 59 s | alert +14.2 s | first +14.17 s | 0.60 (F6 sticky floor, was 0.05 before F6) | 0.31 s | PASS (0.0 s) |
| 0afc3446 | 99 s | quiet | quiet, 0 alerts | 0.05 low | 0.34 s | PASS |
| 922262b2 | 24 s | quiet | quiet | 0.05 low | 0.57 s (was 0.31 s after TASK-047) | PASS, finals still far from the 6.5 s live lag |
| a99a2060 | 15 s | quiet | quiet | 0.00 low | 0.50 s | PASS |
| 37cbc8e2 | 14 s | quiet (no earlier row) | quiet | 0.00 low | 0.28 s | PASS (first replay) |
| 8894eb46 | 33 s | quiet (no earlier row) | quiet | 0.00 low | 0.20 s | PASS (first replay) |
| 4d8dd2f8 | 72 s | quiet | quiet | 0.05 low | 0.31 s | PASS |
| 497ef1d4 | 62 s | quiet | quiet | 0.00 low | 0.36 s | PASS |
| 6352e850 | 146 s | quiet in the live run (upstream digital-zero mute, not a detector miss) | quiet | 0.05 low | 0.32 s | SAME as before (known upstream miss) |
| 93c95fd6 | 94 s | alert +18.3 s live (earlier row in STT_FALLBACK.md) | first +18.04 s | 0.60 critical-labelled in P2 log | 0.36 s | PASS (-0.3 s vs live), 1 alert, no repeat |
| a9142648 | 40 s | no earlier row | first +13.13 s | 0.95 critical | 0.39 s | first replay: alerts |
| ba80d152 | 78 s | no earlier row | first +13.49 s | 0.95 critical | 0.34 s | first replay: alerts |
Result: no alert moved by more than 0.2 s versus the earlier numbers, 0 new false alarms (every benign dump stayed quiet), 1 alert per alerting call. The three calls added here (93c95fd6, a9142648, ba80d152) are labelled SCAM below (lead, from the p2.log finals); 93c95fd6 also has the live +18.3 s row in STT_FALLBACK.md. The 0.60 end-state in the P2 log carries the band label of the raw score; the hub-side band for 0.60 is "watch" (seen in TASK-066).

## Labels for the three calls added in TASK-071 (lead's reading of logs/p2.log finals, 06:01)
| call | start (CT) | label | replay alert | result |
|---|---|---|---|---|
| 93c95fd6 | 03:34 | SCAM (IRS "Officer Daniel Brooks", warrant, settle $4,800 now) | +18.04 s | true positive |
| a9142648 | 05:08 | SCAM (IRS unpaid taxes + SSN ask) | +13.13 s | true positive |
| ba80d152 | 05:37 | SCAM (IRS + gift cards + tell nobody) | +13.49 s | true positive |
PSTN vs simulated for these three: not stated in any file I have (not guessed; asked the lead).

## Caller-track mute (TASK-083, read only, 06:05; per-second RMS of the caller track in logs/audio, aggregates only)
Zero = per-second RMS < 2 (digital zero, not line noise) after speech started. Stretch = start second + length in s, only runs > 1 s. P1's `689c3f6` (03:33) added per-second inbound RMS logging and 20 ms paced Maria injection; no commit claims a mute fix.
| call | time | zero stretches > 1 s | vs 689c3f6 |
|---|---|---|---|
| 4d8dd2f8 | 03:04 | 5 (2-6 s each) | before |
| 922262b2 | 03:06 | 1 (11 s, from 4 s) | before |
| 37cbc8e2 | 03:17 | 2 (3 s, 2 s) | before |
| 8894eb46 | 03:20 | 2 (5 s, 7 s) | before |
| 6352e850 | 03:26 | 6+ (longest 15 s at 54-69 s) | before (the scam-card miss) |
| 497ef1d4 | 03:32 | 3 (2-3 s) | before |
| 93c95fd6 | 03:34 | 3 (2-3 s) | before |
| adad65a0 | 04:46 | 0 | after |
| 0afc3446 | 05:03 | 0 | after |
| 499a20d2 | 05:05 | 0 | after |
| a9142648 | 05:08 | 0 | after |
| ba80d152 | 05:37 | 0 | after |
Verdict: **not seen since 689c3f6 (0 of 5 dumps), unproven for Maria talk-over.** The 5 later calls are continuously spoken scam scripts and none had Maria talking over the caller; no hub inrms log is kept, so the cause of the old gaps is not shown. Proof needs one talk-mode call with Maria speaking over a silent caller and the hub log kept (P1 rehearsal 09:00). The simulated b58cec24 (one 2 s gap) is not counted.
