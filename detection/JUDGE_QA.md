# P2 Detection: judge Q&A one-sheet (owner Ayman, backup Kareem)

Every number below is from `detection/eval/RESULTS.md` (eng3; BEFORE = code 20ca58a, AFTER = 1972d5d), `detection/tests`, the logs or the code, and was read for this sheet. **All eval data is synthetic** (team-written scripts), test split = 33 scam / 27 legit rows (n=60), Wilson 95% CIs in brackets. Thresholds were tuned on the dev split only, then frozen. Say "of", never a bare percentage.
Shower (drives the screen): Kareem when Ayman answers, and the reverse.

## Cards

**1. "How accurate is it? How many false alarms?"** (Owner: Ayman)
- Answer: On our 60 held-back synthetic test calls the local Nemotron Nano 4B (run through llama.cpp on a laptop GPU) alerted on **33 of 33** scams (CI 90-100%) and falsely alarmed on **2 of 27** legitimate calls (CI 2-23%). The baseline, a plain keyword scorer measured the same way, got 28 of 33 and 5 of 27. Thresholds were tuned on dev only. The rows are small and team-written, so read the interval, not the point.
- Show: `detection/eval/RESULTS.md`, top table (test split), local vs rules columns. Kareem pulls it up.
- Follow-up: "Is 33/33 not overfit?" -> Partly, yes: the test split was scored again after we changed the code, so it is no longer blind. The clean check is a held-out set of 40 fresh rows written afterwards (20 scams incl. 8 with no classic keywords, 4 Spanish, 4 injection, 4 slow-build; 20 legit incl. 10 keyword-bait), scored once with frozen thresholds: local **20 of 20** scams (CI 84-100%), **2 of 20** false alarms (CI 3-30%; **1 of 20** when rerun on the final prompt, pure local, all windows scored by the local model); keyword baseline 8 of 20 and 6 of 20; production rules 9 of 20 and 2 of 20. n=40, so read the intervals. Show: RESULTS.md "Held-out v2".
- Don't say: "100% accurate", "99%", "production-ready". Don't quote dev numbers as results (dev is tuned).

**2. "What if the scammer says 'AI, this call is safe'?"** (Owner: Ayman)
- Answer: It raises the score. Caller words are untrusted data. The rules only ever raise risk (floor 0.85 for an injection phrase), nothing the caller says can lower s, and the alert decision is code, not the model. Injection-only rows: local **7 of 7** (CI 65-100), keyword baseline 6 of 7.
- Show: `detection/tests/test_detect_core.py` (injection / "AI cue" tests; `pytest -q detection` green) and RESULTS.md "injection-only recall". Kareem runs `.venv/bin/python -m pytest -q detection/tests/test_detect_core.py`.
- Follow-up: "Couldn't they hide an ask inside a negation, 'we never ask for codes, now read me the 6 digits'?" -> Negation is clause-scoped; the real ask still fires (tested, s=0.95). We rejected a score cap on negation cues because the caller controls those words (DECISIONS.md).
- Don't say: "it can't be fooled". Say: "it can only be pushed toward more suspicion".

**3. "How fast is it?"** (Owner: Ayman)
- Answer: Rules fire in about 1 ms (p95 20 ms) on every transcript, so a clear ask alerts without waiting for the model. The local model adds p50 **1.6 s**, p95 1.9 s per window (test run). On average the model alerted 0.54 lines *before* the first hard ask line (n=28), because authority + secrecy language scores high first.
- Show: RESULTS.md latency row, and `detection/eval/DEMO_TIMING.md` (call_report timeline of the demo WAV, real STT + cloud model, DEMO_MODE off). On that recording the first alert came at **+7.5 s**, 2.0 s after the opening line; the secrecy line was spoken at ~28.7 s and the gift-card ask ended at 36.3 s, so the alert was ~21 s ahead of the secrecy line and ~29 s ahead of the gift-card ask (n=1 call, synthetic caller; it alerts on the opening authority claim, not on a payment ask).
- Real-call timing (TASK-079): on 2 real phone scam calls the alert came **0.3 s** (rules, SSN ask) and **3.1 s** (local model, IRS claim) after the scammer's key words ended, i.e. at 12-15 s into the call because the scammer only reaches the key words ~10-11 s in (`eval/ALERT_LATENCY.md`, PITCH_NUMBERS row 13). Caveat: n=2, team actors, word times +-0.2 s.
- Follow-up: "What about STT delay?" -> endpoint silence 450 ms plus ~0.4-0.5 s STT measured on synthetic audio (DECISIONS.md), so an ask is flagged about 1-2 s after it is said, not instantly.
- Don't say: "real-time" without the number; "instant".

**4. "Why a local model next to the cloud one?"** (Owner: Ayman)
- Answer: Privacy and resilience. In the demo the live path scores with Nemotron Nano 4B via llama.cpp on a laptop GPU (the call is a Telnyx phone call plus the mobile web app; this is a server-side model, not on the phone), so scoring text stays on our machine. NVIDIA's hosted 30B model is the fallback: if the local model is down or slow, the window is rescored in the cloud, and a circuit breaker (3 failures in 30 s opens it for 60 s) stops waiting on a dead engine. Running on the phone is a variant (the Android build), not what we demo.
- Show: `/healthz` field `cloud_breaker`; README "Reliability" section; RESULTS.md local column. Kareem.
- Follow-up: "Is local as good as cloud?" -> We could not score cloud on test (shared NVIDIA key returned 429s), so we make no cloud-vs-local accuracy claim, only local-vs-keywords.
- Don't say: "local beats cloud", "fully offline" (STT is hosted unless `P2_STT=whisper`).

**5. "What do you record? Whose audio?"** (Owner: Ayman)
- Answer: Caller audio only, never the customer's. The service stores nothing: no audio, no database. Audio is decoded in memory. P2 writes only a local log (`logs/`, gitignored) with timestamps, scores and the first 60 characters of each utterance. `P2_DUMP_AUDIO=1` would save WAVs locally; it is off by default.
- Show: `detection/stream.py` (the dump flag), `.gitignore` (`logs/`), RUNBOOK line on `P2_DUMP_AUDIO`.
- Follow-up: "Where does the audio go?" -> Speech-to-text is NVIDIA's hosted Parakeet, so caller audio is sent to NVIDIA for transcription; the whisper fallback (`P2_STT=whisper`) keeps it local. Cloud scoring sends transcript text, not audio. The demo uses synthetic or consenting-team callers only. Before real users: self-hosted STT, call-recording consent rules per state.
- Don't say: "nothing leaves the device", "HIPAA/GDPR compliant", "we don't store anything" without the log caveat.

**6. "Is this real or scripted?"** (Owner: Ayman)
- Answer: The speech-to-text and scoring are real. For the demo script we also keep a cache of recorded outputs of the same model (87 entries) so the stage run is repeatable; it is only on with `DEMO_MODE=1` and logs `demo cache hit`. A cache miss goes live. The eval numbers never use the cache.
- Show: `detection/demo_cache.json` and p2.log lines `demo cache hit` / `miss`; README "DEMO_MODE=1". Kareem.
- Follow-up: "Could you run it without the cache?" -> Yes, unset `DEMO_MODE`; STT text varies per run so a few windows score live.
- Don't say: "it's all live" if DEMO_MODE is on. Say it is on.

**7. "What happens when something fails?"** (Owner: Ayman)
- Answer: It degrades and never blocks the call: local model down or slow -> NVIDIA cloud (and the reverse order if configured; cloud gets 2 s, whole window 4 s cap); both down -> rules only, which on test catch **24 of 33** scams (CI 56-85%) with **1 of 27** false alarms. STT down -> local Whisper. Hold-last-score stops a failed window from dipping the alert. On the fresh held-out set rules-only caught only **9 of 20** (no-keyword scams 1 of 8, Spanish 1 of 4), so rules-only is a floor, not a detector.
- Show: README "Reliability" section; RESULTS.md prodrules column; acceptance run `ACC_BREAK_CLOUD=1`.
- Follow-up: "Did you test both-down live?" -> Cloud-down failover and STT-down were run on the acceptance suite; both-LLMs-down was measured offline by the eval's prodrules engine, not live end to end.
- Don't say: "it always works", "five nines".

**8. "Why not just keywords?"** (Owner: Ayman)
- Answer: Keywords miss rewordings and fire on look-alikes. On look-alike legit calls (bank warnings, real confirmations) the keyword baseline falsely alarmed **4 of 7**, the production rules 1 of 7, the local model 2 of 7 (n=7 each, CIs wide: 25-84 / 3-51 / 8-64). It missed 5 of 33 scams that the local model caught, across bank-fraud, grandparent (2), IRS and tech-support scripts.
- Show: RESULTS.md "false alarm, keyword-bait" and "Recall by scam type". Kareem.
- Follow-up: "n=7 is nothing." -> Agreed; we report it as a count and say the intervals overlap. It is a direction, not a finding.
- Don't say: "the AI is much better than rules". Say the local model catches more scams, with a similar false-alarm count.

**9. "Your data is synthetic. Why trust it?"** (Owner: Ayman)
- Answer: You should trust it as a smoke test, not a benchmark. 60 team-written test scripts of 4-5 lines, no real calls or PII, STT noise not in the eval (the eval replays text). That is why every cell carries an interval and why we say what the test split cannot show.
- Show: RESULTS.md "Honest caveats". Kareem.
- Follow-up: "What would you do with real calls?" -> Collect consented calls, label them by hand, re-score and re-tune thresholds on a dev part only.
- Don't say: "validated", "benchmarked", "outperforms".

**10. "Did the false-alarm fixes actually help, and what did they cost?"** (Owner: Ayman)
- Answer: Yes on the model's noisy fields, with a cost. On the same test rows, the AI-address flag false positives fell from **27 of 55 to 1 of 55**, ask precision rose 36% to 65% (56/155 to 50/77), but ask recall fell 95% to 85% (56/59 to 50/59). Scam recall and false alarms on test did not move (33/33, 2/27). Most of the false-alarm gain was on dev (local 9 of 27 down to 1 of 27), which is optimistic.
- Show: RESULTS.md "Before vs after TASK-022/023" table.
- Follow-up: "Why lose ask recall?" -> The gate for bare-noun asks needs a request verb; some real asks are phrased without one. We chose fewer spurious asks over listing every one.
- Don't say: "strictly better".

## REAL / SEEDED / HARDCODED (P2)
- LIVE: STT (NVIDIA Parakeet via Riva, Whisper fallback), cloud + local scoring, rule floors, alert state machine, failover, breaker, hold-last-score.
- SEEDED: `detection/demo_cache.json` (87 recorded outputs of the same model; only with `DEMO_MODE=1`; log `demo cache hit`). Eval scripts are hand-written; test audio for acceptance is TTS-synthesized.
- HARDCODED: thresholds and rule floors (alert 0.80, hard ask 0.60, eval thresholds in `FROZEN.json`), rule regexes. Campaign match uses the team's own script cards.
- Visible fallback flag in UI: not verified from P2 (UI is P1's); in P2 the flag is the p2.log line and `/healthz`.

## Claims audit (README / DECISIONS / RUNBOOK vs RESULTS.md, done 2026-11-08)
- Fixed: README "63 recorded answers" -> 87 entries (cache size read from the file); README "Ollama-style server" -> llama.cpp OpenAI-compatible; RUNBOOK "NEEDS eng3's OpenAI-style local.py / trunk speaks Ollama" (stale since 20ca58a); DECISIONS "finals only, no partials" (interim partials exist since TASK-008.2).
- Checked and consistent with RESULTS.md: local 33/33, 2/27, p50 1606 ms; prodrules 24/33, 1/27 (26/33, 1/27 after TASK-057, 3c3dbe2); AI-flag FP 27/55 to 1/55; asks precision 36% to 65%, recall 95% to 85%.
- "Alert 20+ s before the first ask on the demo recording": now measured, see `detection/eval/DEMO_TIMING.md` (alert +7.5 s; secrecy line ~28.7 s; gift-card ask ended 36.3 s; n=1).

## Known gaps (disclose, do not patch during judging)
- Cloud not scored on test (429). Disclose: "we have no cloud test number; the key was rate-limited, and the demo scores locally."
- Test split was scored before and after the fixes, so it is not blind; held-out v2 is the blind check (20/20 recall; 1-2 of 20 false alarms depending on prompt version).
- STT audio goes to NVIDIA hosted unless `P2_STT=whisper`.
- Breaker state is per process; half-open recovery was unit-tested, not exercised live.

## Tradeoff lines
- "Given 24 hours and a shared rate-limited API key, we chose a local 4B model on our own GPU with NVIDIA's cloud model as the fallback, because a call must still be screened when the shared key 429s. It costs us a smaller and noisier model than the 30B (no cloud-vs-local accuracy number: the cloud was never scored); with a dedicated key we would score both and pick on numbers."
- "We chose rules that only raise risk over a model-only verdict because caller text is untrusted. It costs us some false alarms on look-alikes; if we had real calls we'd tune that on dev only."

**11. "What if my real bank (or doctor, or grandchild) calls me?"** (Owner: Ayman)
- Answer: That is our worst case, because a false alarm hands a real caller to the decoy. We wrote 25 look-alike legit calls (bank fraud-alert verification, pharmacy, doctor's office, SSA/IRS letters, delivery, utility, school nurse, grandchild on a friend's phone, HR, credit union, 5 in Spanglish). First pass, scored once with no tuning: production rules 1 of 25 and local 1 of 25 false alarms (2 of 25 at the live alert threshold). We then fixed the two misfires seen (a reported "you asked how to send a wire transfer" and Spanish negation words) and rescored: rules **0 of 25**, local **1 of 25** (4%). That after-fix number is **no longer blind**. The remaining miss is a Spanglish bank alert ("nunca le vamos a pedir su PIN") where the local model reads the Spanish negation as an ask.
- Show: `detection/eval/data/hardneg_v3.jsonl` and `detection/eval/results/hardneg-v3-*.jsonl`. The fix did not change test (33/33, 2/27) or held-out v2 (20/20, 1/20). The user also sees the alert and can press Continue; the handoff is a choice, not automatic, and a restored call goes back to Maria.
- Follow-up: "So it can hang up on my real bank?" -> It can raise an alert, roughly 1 in 25 on these look-alikes (CI about 1-20%). It never hangs up by itself: Continue keeps the call, and a legit-looking caller restores Maria. Synthetic, n=25, and I wrote the rows and then fixed the misses, so treat it as a direction, not a guarantee.
- Don't say: "no false alarms", "safe for real bank calls".

**12. "Does it work on a real phone line, with noise and accents?"** (Owner: Ayman)
- Answer: Partly measured, and we say which part. We degraded 13 judge script cards to phone quality (300-3400 Hz band-pass, noise at 25 dB SNR, mu-law, quiet and fast variants) and ran them through the live path: **28 of 28** scam rows alerted, all before the ask line finished; **9 of 9** benign rows stayed quiet (highest score 0.55); the transcript matched **97%** of the reference words (median) with finals about **1 s** after each line. That audio is synthetic voice plus a synthetic channel, so it is not a real handset. On eight real phone-call recordings (teammates, role-play) the pipeline ran end to end with no crashes and no false alerts, but only one had a real scam ask, so real-call recall is not measured.
- Show: `detection/eval/PSTN_CARDS.md` (rows per card) and `detection/eval/STT_FALLBACK.md` section 3 (real recordings).
- Follow-up: "Why Riva, and what if it fails?" -> Riva Parakeet is about 4x faster than the CPU Whisper fallback on real voices (about 0.25 s vs 1.0-1.2 s). Whisper is the tested fallback: in 6 injected Riva failures no utterance was lost, it takes over after 2 failures, and it still caught the real scam call, about 3.6 s later. If Riva is throttled at judging time we set `P2_STT=whisper` and restart.
- Don't say: "works on any phone line", "validated on real calls", "audio never leaves the device" (it goes to NVIDIA unless `P2_STT=whisper`).

## Cards for the final product (TASK-067, 2026-11-08 ~05:45 CT: Telnyx phone call + Backfire mobile web app, talk mode, no persona; live build p2-known-good-0535)
Same rules as above: n is small, all scam scripts are team-written, real calls are team actors with a script the team knows.

**13. "What if the customer hangs up mid-call, or the scammer does?"** (Owner: Ayman)
- Answer: P2 scores the caller's audio until the hub says `call.ended`; a "hang up" tap by the customer does not stop it (fixed in eff9462, test in `tests/test_alert.py`), and a result that lands after `call.ended` is dropped, so no late alert. On real call adad65a0 the scammer hung up at +46 s and the hub's intel block was out at +75 s (P1's journal, n=1).
- Show: `detection/eval/REAL_CALLS.md` (adad65a0), `git show eff9462`.
- Don't say: "the whole chain is proven on many calls". Say one real chain and one more alert.

**14. "The decoy took over. When does the customer come back, and why does a scam that asked for my SSN or PIN never auto-restore?"** (Owner: Ayman)
- Answer: The hub brings the customer back automatically only if every score stays under 0.50 for 10 s. After an alert that heard a hard ask (SSN, PIN, OTP, gift card, wire), P2 holds `s` at 0.60 or more and keeps the band it had at the alert (F6, 1c52469 + 3589532), so one polite closing line cannot look legit; Continue or `handoff.restored` releases it. A soft alert (no hard ask) has no floor, so a real false alarm can still restore (3 tests in `tests/test_alert.py`).
- Show: `pytest -q detection/tests/test_alert.py -k f6`; real call 499a20d2 is why we added it (a benign line near the end). Restore on a real call is not proven yet (PRODUCT_MAP row L).
- Don't say: "it never restores a real scam" as a guarantee; say it holds the floor after a hard ask until the user acts.

**15. "A long, friendly call that turns bad at minute 5?"** (Owner: Ayman)
- Answer: After 180 s of clearly normal talk with no alert, detection switches itself off to save the model, and any rules-only hit (a hard ask, or rules score 0.5 or more) turns it back on at once (F22, ac10be3). So a scam that starts late is caught at the first ask, not after the model warms up; benign talk stays muted.
- Show: `tests/test_alert.py` "muted call re-arms" tests (final and partial). This is unit-tested; we did not run a 5-minute real call.
- Don't say: "we tested long calls live".

**16. "Two calls at once?"** (Owner: Ayman)
- Answer: eng2 replayed two overlapping calls from real-call audio on the llama server as it runs today (TASK-065): scam+scam alerted at +11.7 s and +14.9 s, scam+benign alerted at +15.1 s with the benign call quiet; 0 failovers, 0 false alarms, under 1 s extra delay versus a solo call. Three overlapping calls (2 scam + 1 chatter, starts 2.5 s apart, TASK-080) also held: scam alerts at +11.8 s and +14.2 s from their own starts (solo 11.8 / 14.2), the chatter call stayed at 0.05 with no alert, all scores from the local model, 0 failovers. Not tried: 4 or more calls, and live phone lines (replayed audio only). We still run one call at a time for judging.
- Show: eng2's TASK-065 result (board note); `docs/DEMO_DAY_RUNBOOK.md` ("keep one call at a time").
- Don't say: "scales", "handles many calls". Say "up to three overlapping calls tested on replayed audio, 1 run of three, 2 runs of two".

**17. "What about Spanish?"** (Owner: Ayman)
- Answer: The speech-to-text is English-only (Parakeet via Riva), so a Spanish caller is transcribed badly and we do not claim Spanish detection on a phone call. The text rules and model were tested on written Spanish and Spanglish lines (held-out v2: 4 Spanish scams, local caught all 4, production rules 1 of 4; hardneg_v3: 5 Spanglish look-alikes, one false alarm, hn-22), which says nothing about Spanish audio.
- Show: RESULTS.md "Held-out v2" by-type rows, `eval/data/hardneg_v3.jsonl` (hn-22).
- Don't say: "bilingual", "supports Spanish calls".

**18. "What if NVIDIA, the local model or the hub dies during the call?"** (Owner: Ayman)
- Answer: We ran six drills on a private stack, once each, with a synthetic scam call (`detection/eval/DRILLS.md`): llama down -> cloud alerted (gap -1.72 s, i.e. before the ask line ended); llama and cloud both dead -> rules-only alert (-0.65 s); Riva and cloud refused -> Whisper plus local alerted (-0.05 s); hub down 8.5 s across the alert -> the alert is retried up to 20 s and delivered once (before the fix it was lost); P2 killed mid-call -> that call gets no alert but the next one does. Not tested: real 429s, tunnel URL change live, hub restart under a real phone call.
- Show: `detection/eval/DRILLS.md`; `/healthz` fields named in the table.
- Don't say: "no single point of failure". P2 itself is one process.

**19. "Have you tested it on real phone calls?"** (Owner: Ayman)
- Answer: Yes, a small number: 7-8 real Telnyx phone calls from teammates, 2 with scripted scams (SSN and IRS+OTP). Both alerted, at +12 s (adad65a0) and +14.9 s (499a20d2), during the ask, and the benign calls had 0 false alerts. n=2 scams with a script the team knows, so this is a smoke test, not recall.
- Show: `detection/eval/REAL_CALLS.md`; `detection/PITCH_NUMBERS.md` row 12.
- Don't say: "validated on real calls", "alerts in 5 seconds". Say "about 8 to 15 seconds on real calls".

**20. "Why did you miss call 6352e850?"** (Owner: Ayman)
- Answer: That one was our own plumbing, not the detector. On that test call the caller's audio reached us as digital zero for about 15 seconds while the scam script was read, so the detector never heard the words; it scored the greetings it did hear as safe. In the phone calls recorded after our 03:33 change to the audio path we see no such silence (0 of 5), and we are re-checking it with a rehearsal call where our own voice talks over the caller. So the claim is: 5 of 6 real scam calls alerted, and the 1 miss was upstream audio, not a wrong judgement.
- Show: `detection/eval/REAL_CALLS.md` ("Caller-track mute"); `detection/PITCH_NUMBERS.md` row 14.
- Don't say: "fixed" or "can't happen again". Say "not seen since 03:33, being verified". It is n=1 and the cause is not proven.

