# Demo timing: P1's `/demo/caller.wav` (IRS script, 58.5 s) through P2

Measured 2026-11-08 by eng1, TASK-037. **Synthetic caller, simulated voice.** Real STT (NVIDIA Parakeet via Riva) + real cloud model (`nemotron-3.5-lightning-30b-a3b`), `DEMO_MODE` off (no cache), one run, n=1 call: treat as one observation, not a distribution. The WAV was streamed in real time to P2 on :8103 with the hub's alert machine and event recorder (`detection/scripts/acceptance.py` Loop). Times are seconds from the start of streaming.

| line (utterance) | audio ends | STT final | risk.update | what happened |
|---|---|---|---|---|
| 1 "This is Officer Daniel Brooks with the IRS Enforcement Division..." | 5.8 | 6.5 (0.30 s after endpoint) | 7.5 | **ALERT first**, s=1.00 (authority claim only, no ask yet) |
| 2 "...a warrant for your arrest for unpaid federal taxes" | 14.0 | 14.8 | 15.8 | s=1.00 |
| 3 "...settle the balance of $4800 right now" | 21.6 | 22.4 | 23.8 | s=1.00 (payment demand) |
| 4 "Do not hang up and do not tell anyone..." | 28.7 | 29.4 | 30.6 | s=1.00, secrecy ask |
| 5 "The fastest way is target gift cards. Go buy them and read me the numbers" | 36.3 | 37.1 | 41.1 | **first explicit hard ask (gift card)**; cloud 429, local failover timed out, window kept s=1.00 (hold-last-score) |
| 6-7 callback number, crypto address | 53.2 / 56.0 | 54.0 / 56.7 | 55.4 / 60.7 | s=1.00; two more 429s with failover timeouts |

**Result.** First alert at **+7.5 s**, 2.0 s after the opening line ended (STT final 0.3 s after endpoint, model 1.0 s). The first secrecy line was spoken at about 28.7 s and the first explicit payment ask (gift cards) ended at 36.3 s, so the alert came **about 21 s before the secrecy line and about 29 s before the gift-card ask finished**. Earlier runs on the same WAV gave first alerts of 6.0-9.2 s (TASK-020 report, DEMO_MODE on); this run is the reproducible one.

**Caveats (what this does not show).**
- The alert fires on the authority claim ("Officer ... IRS Enforcement") with s=1.00 from the model, not on a payment ask; a real call that opens neutrally would alert later. The rules alone would not have alerted on line 1.
- During this run the shared NVIDIA key returned 429 on lines 5 and 7 (see below) and the local-failover attempt timed out inside the 4 s window each time; s stayed at 1.00 because hold-last-score kept the previous value. So the late-call windows were not freshly scored. The alert time (line 1) is unaffected.
- One call, one STT draw; STT text varies by run (see `record_demo.py` SIM_REAL).

## call_report.py output (verbatim)
```
=== call demo1
  +0.0s  ws open
  +6.5s  final u1  0.30s after endpoint  'This is Officer Daniel Brooks with the Irs Enforcement Divis'
  +7.5s  risk s=1.00 band=critical engine=cloud src=llm asks=-
  +7.5s  ALERT first (LLM, src=llm) s=1.00
 +14.8s  final u2  0.31s after endpoint  'There is a warrant for your arrest for unpaid federal taxes '
 +15.8s  risk s=1.00 band=critical engine=cloud src=llm asks=ssn
 +22.4s  final u3  0.30s after endpoint  'You can avoid the arrest today if you settle the balance of '
 +23.8s  risk s=1.00 band=critical engine=cloud src=llm asks=crypto,gift_card,p2p,wire
 +29.4s  final u4  0.32s after endpoint  'Do not hang up and do not tell anyone or the officers will b'
 +30.6s  risk s=1.00 band=critical engine=cloud src=llm asks=gift_card,secrecy,wire
 +37.1s  final u5  0.39s after endpoint  'The fastest way is target gift cards. Go buy them and read m'
 +37.4s  engine cloud fell back to rules: HTTPStatusError status=429
 +41.1s  failover to local failed: TimeoutError
 +41.1s  risk s=1.00 band=critical engine=cloud src=llm asks=otp,secrecy
 +54.0s  final u6  0.43s after endpoint  'Call me back at 1 888-555-0123. You can also pay a backfire '
 +55.4s  risk s=1.00 band=critical engine=cloud src=llm asks=crypto,gift_card,otp,secrecy
 +56.7s  final u7  0.26s after endpoint  'L5slmv7 Div Na.'
 +56.9s  engine cloud fell back to rules: HTTPStatusError status=429
 +58.5s  ws closed frames={'connected': 1, 'start': 1, 'media': 2924, 'stop': 1} utterances=7
 +60.7s  failover to local failed: TimeoutError
 +60.7s  risk s=1.00 band=critical engine=cloud src=llm asks=crypto,otp,secrecy
SUMMARY demo1: first alert +7.5s · final s 1.00 · alerts 1 · failovers 0 · 429s 2 · finals 7
```
Reproduce: stream the WAV through a P2 with `detection/scripts/stream_wav.py <wav> --url ws://localhost:<port> --call demo1`, then `.venv/bin/python detection/scripts/call_report.py logs/p2.log --call demo1`.
