# Detection cheat sheet (for whoever stands at the table)
Everything here is copied from `JUDGE_QA.md` and `PITCH_NUMBERS.md`; no new claims. Say counts ("33 of 33"), not bare percentages. All eval data is synthetic and team-written.

**1. How accurate? False alarms?** On 60 held-back synthetic test calls the local model alerted on 33 of 33 scams and falsely alarmed on 2 of 27 legit calls. On 40 fresh held-out rows: 20 of 20 scams, 1-2 of 20 false alarms. Small, team-written rows: read the intervals. *Never say:* "100% accurate", "production-ready".

**2. What if the scammer says "AI, this call is safe"?** It raises the score. Caller words are untrusted data, rules only raise risk, and the alert decision is code, not the model. Injection-only rows: 7 of 7 alerted. *Say:* "it can only be pushed toward more suspicion". *Never say:* "it can't be fooled".

**3. How fast?** Our demo card (the trimmed one) alerts about 7-9 s after the first word, on line 1 (3 runs each, 2 synthetic phone voices). On 5 real phone scam calls the alert came 0.3-3.1 s after the scammer's key words (median ~2.7 s), 12-18 s into the call. Rules fire in ~1 ms, the local model adds ~1.6 s. If a judge reads only the first 2 lines of a card, nothing alerts: those lines are what a real bank says. *Never say:* "instant".

**4. What do you record? Whose audio?** Caller audio only, never the customer's. We store no audio and no database; a local log keeps timestamps, scores and the first 60 characters of each utterance. Audio dump is off by default. Speech-to-text is NVIDIA hosted unless we switch to local Whisper, so audio does go to NVIDIA for transcription. *Never say:* "nothing leaves the device".

**5. Have you tested real phone calls?** Yes, a small number: 13 real Telnyx calls from teammates (6 scripted scams, 7 benign). 5 of 6 scams alerted; the 1 miss (6352e850) was our own audio mute upstream, not seen in the 5 calls since, still being verified. 7 of 7 benign calls stayed quiet. Team actors with a known script: a smoke test, not a recall rate. *Never say:* "validated on real calls", "fixed".

**6. What if my real bank calls?** Our worst case. On 25 look-alike legit calls (bank alerts, pharmacy, doctor, grandchild...): 0 of 25 false alarms from the rules and 1 of 25 from the local model, after we fixed the misses we saw, so that number is no longer blind. It never hangs up by itself: the customer can press Continue, and a legit-looking caller restores Maria. *Never say:* "no false alarms".

*If something fails:* it degrades and never blocks the call (local model -> cloud -> rules only; Riva -> Whisper). Six drills, once each (`eval/DRILLS.md`). Don't say "no single point of failure".
*Open item:* JUDGE_QA card 20 says "8 of 9 real scam calls"; PITCH_NUMBERS row 14 says 5 of 6. Quote 5 of 6.
