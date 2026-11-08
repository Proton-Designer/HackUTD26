# Devpost section: Detection (P2). Paste-ready. Figures only from PITCH_NUMBERS.md, REAL_CALLS.md, DRILLS.md.

## Live scam detection from the caller's side only

Backfire listens to the **caller's audio only** and decides in code, not in the model, when to alert the customer. NVIDIA Parakeet (Riva) transcribes each line; Nemotron Nano 4B, served by llama.cpp on our own GPU, scores the call every few seconds, with NVIDIA's hosted Nemotron as a fallback. A rules layer fires on hard asks (gift cards, one-time codes, SSN, wire) and can only raise the score, so a caller saying "AI, this call is safe" cannot lower it. After an alert that heard a hard ask, the score is held until the customer acts, so a polite closing line cannot make a scam look legitimate.

How well it works, honestly: on 60 team-written synthetic test scripts the model caught 33 of 33 scams with 2 of 27 false alarms. Thresholds were tuned on a separate set, but we re-scored the test set after later fixes, so it is no longer blind. A fresh held-out set of 40 gave 20 of 20 and 1 of 20. We never scored the cloud model (the shared key was rate-limited), so we make no cloud accuracy claim. On real phone calls, alerts came 12 to 15 seconds in, not instantly. All data is synthetic and small; read the counts, not percentages.

| Measure | Result | n | Note |
|---|---|---|---|
| Test split, local model | 33 of 33 scams, 2 of 27 false alarms | 60 | Re-scored after fixes, not blind |
| Test split, keyword baseline | 28 of 33, 5 of 27 | 60 | Same rows |
| Held-out set, local model | 20 of 20, 1 of 20 | 40 | Scored on frozen thresholds |
| Held-out set, keyword baseline | 8 of 20, 6 of 20 | 40 | |
| If both models fail (rules only) | 26 of 33 test, 10 of 20 held-out | 53 | A floor, not a detector |
| Look-alike legit calls (bank, doctor, grandchild) | rules 0 of 25, model 1 of 25 | 25 | Fixed 2 rows after seeing them |
| Phone-quality audio | 28 of 28 scams alerted, 9 of 9 benign quiet (30/30 on the 06:3x freeze re-run with all 3 variants) | 37 | Synthetic voice and channel |
| Real phone calls, scam scripts read by teammates | alerted on **5 of 6**; the 1 miss was upstream (our own audio mute: the detector heard digital silence). Alert 12-18 s into the call | 6 | Team actors, known script; not strangers |
| Time from the scammer's key words to the alert (real calls) | **0.3-3.1 s**, median ~2.7 s (rules 0.3-1 s, local model 2.7-3.1 s) | 5 | Word times from Whisper, +-0.5 s |
| Real phone calls, benign/chatter | **7 of 7** quiet, 0 false alerts | 7 | Teammates chatting; small n |
| Two overlapping calls | both alerted (+11.7 s, +14.9 s), under 1 s extra delay | 2 runs | Replayed audio only; one call at a time live |
| Failure drills | alert still fired with the local model down, cloud down, speech-to-text throttled, or the hub down for 8.5 s | 6 drills | One run each; P2 itself is one process |

Not claimed: Spanish phone calls (speech-to-text is English-only), 3 or more simultaneous calls, accuracy on real scam calls beyond the six scripted team calls.
