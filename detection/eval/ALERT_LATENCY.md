# Alert latency breakdown (TASK-075, 2026-11-08 ~06:00 CT)
Replay of the real PSTN dumps adad65a0 and 499a20d2 through a private P2 (HEAD ce5d515, engine local, no hub). Times are audio seconds (replay is real-time). Word times from faster-whisper base.en on the dump (±0.2 s). n=2 calls.

| stage | adad65a0 | 499a20d2 |
|---|---|---|
| trigger words spoken | "give me your social security" 10.1-11.3 | "...haven't paid. I am the IRS" 4.8-10.8 |
| speech end -> utterance final (450 ms VAD endpoint + ~0.25 s Riva) | not needed: alert fired mid-utterance | 10.8 -> 12.2 (~1.4 s) |
| queue wait | 0 | 0 (one detect in flight, coalesced) |
| LLM (local Nemotron 4B), per call | not on the alert path | 1.7 s on that final (2.4 and 3.0 s on the two before) |
| alert-machine hold (window/consecutive rules) | 0 (first alert needs s>=0.80, no extra lines) | 0 |
| hub emit | ~0 ms | ~5 ms |
| alert.fired | +11.6 s, src=fast-partial (rules on an interim transcript, 0.3 s after "security" ends) | +13.9 s, src=llm (live: +14.9) |

Reading: adad65a0 is already at the floor (rules on partials, alert ~0.3-0.9 s after the words). 499a20d2 waits for utterance end (1.4 s) plus the LLM (1.7 s) because no rule fires on "I am the IRS ... haven't paid".

## Knobs (nothing shipped, defaults unchanged)
1. Authority-impersonation + money-owed rule floor 0.80 (regex: "I am/this is ... IRS/SSA/federal/marshal/court ..." and owed/unpaid/warrant/arrest/penalty in the same window, not negated), applied to partials and finals. Expected gain on 499a20d2: 1.7 s (at the final) to ~2.4 s (on a partial). Measured offline over 155 rows (heldout_v2, extra_rows, hardneg_v3): no new false alarm on 87 benign rows (the one hit was "nothing owed today", fixed by a negation check); fires earlier on 3 of 68 scam rows; 1 of 17 real-call finals (the scam one). Risk: low-medium; small sample, and a legitimate caller saying "I'm with the IRS ... you owe" would alert (arguably correct). Lives in detect.py (eng1's); needs the full eval + hardneg before shipping.
2. P2_ENDPOINT_MS 450 -> 300: gain ~0.15 s only; more split utterances. Not worth it.
Everything else (LLM-on-partials, smaller windows) is either risky for false alarms or saves <1 s.
