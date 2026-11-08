
## Real-call evidence (eng3, TASK decoy ALL HANDS 08:05)
Sources: trunk `logs/p2.log` `echo.decoy` lines (speaker=decoy = what the decoy SAID; speaker=scammer = what the decoy's own STT HEARD) and P2's own `stt final` / `echo.caller` lines, 6 calls with a decoy phase (3d5a7970, e3e343de, 8ee2b3da, ba80d152, 5921f090, 19a5fd47) plus 10 one-line test calls. Aggregates and decoy lines only; no caller transcripts quoted. decoy.log (stt=/llm=/total ms, "LLM failed") is on the hub Mac and was NOT available: timeout counts below are inferred.

### What the decoy said (53 spoken lines)
- 17 of 53 = the canned OPENER, once per call (core.OPENER, plus an older "Hello? Sorry, I lost you there..." variant on the test calls). It plays before the first model reply and ignores what the scammer just asked (e3e343de: "open your banking app and send $1800 by Zelle" at +37 s, opener at +43.6 s).
- Model replies are short (median 13-20 words), on topic, and usually end with a question that pulls the payment handle ("what's the website or where do I send this"). Weak ones: parroting ("A baking app? I think you mean a banking app"), "Right, just yeah?", and in 5921f090 a decoy that never learned the scam (fixed in 3a05bf1, below). Only 1 of 53 lines lacks end punctuation (no max_tokens cut-off pattern). 1 of 53 matches a STALLS line (replacement for a failed LLM call).
- Latency, caller final -> first decoy line in the log: median 1.1-1.5 s per call; worst 9.3 s (8ee2b3da), 5.7 s (3d5a7970), 5.3 s (e3e343de), 5.5 s (180fa297). Those long gaps are the opener turns and merged-utterance waits, not measured LLM time.

### Garbled input
- P2 and the decoy both use Riva Parakeet. P2 finals arrive 0.24-0.28 s median (max 0.41 s) after endpoint, so STT_TIMEOUT 6 s is never close.
- Of 35 decoy-heard lines, decoy text == P2 text on about 20; 11 differ (a split or merged utterance, a clipped start such as "Much" for "I have gotten so much"); 5 are 1-2 word fragments. Garbles that matter are in P2's text too ("banking" -> "baking", "Zelle" -> "Zell"/"zeal", "Zelle" cut at "Ze"): an STT issue, not a decoy-only one.
- The decoy hears fewer turns than P2 in the window (e3e343de: 12 P2 finals, 5 decoy-heard; ba80d152: 13 vs 5): merged turns after handoff and the 1-reply-per-pending-batch loop.

### Echo leak (decoy's own voice in its input), counted per call
Fuzzy match (>=4-word common run against any decoy line in the previous 30 s): 0 of 6 / 0 of 5 / 0 of 2 / 0 of 10 / 1 of 5 / 0 of 7 decoy-heard lines. Single case, e3e343de: decoy said "I can't find my phone right now, like..." and the next heard line begins "I can't find my phone right now. Are you talking about" (the decoy's words glued onto the caller's). P2's own caller finals overlap the decoy's words (>=3-word run) in 1 of 11 (3d5a7970) and 1 of 10 (e3e343de). So the echo leak is real but RARE: 1 of 35 decoy-heard lines. It is not the main quality problem.

### 3a05bf1 (pre-handoff context), verified by reading the diff
- The hub /events subscriber (`decoy.app._on_hub_event`) keeps each call's `transcript.caller` finals (is_final, last 30 lines, 400 chars each) and the last non-unknown `risk.update.scam_type`. At Session creation (handoff) they are copied to `pre_lines`, and ONE user message `<caller>all pre lines joined by spaces</caller>` is appended to history (clean() applied, tail 1500 chars) BEFORE the OPENER (the opener is appended as assistant in `say(record=True)`), so the order user(story) -> assistant(opener) -> user(new line) is right.
- The same lines seed PB.classify, core.extract (pass at session start) and the steering note; scam type and label feed the classifier.
- Caveats: (1) history[-16:] drops that single story message after ~8 turns; later turns keep only the steering note's scam type. (2) The story is one blob without line breaks or speaker turns, and includes greetings and STT garbles as P2 heard them. (3) The opener stays canned ("who did you say was calling?") even though the model now knows the story: P1's OPENER, still incongruent after an IRS pitch. (4) Needs HUB_URL/PIPELINE_TOKEN in the decoy process env and a decoy restart; if the hub subscribe fails, pre_lines is empty and nothing changes (fail open). Not yet seen live.

### Latency budget: bolt-e4b vs nemotron-3.5-super-vl-120b-a12b (thinking off)
Same prompt per request (core.SYSTEM + 2-message history + caller line + PB.note steering), `core.chat`, max_tokens 90, temp 0.8, 20 distinct caller lines, alternating models, paced one at a time (2 s gap, live-call guard), shared key:
| model | ok / 20 | p50 | p90 | max | mean words |
|---|---|---|---|---|---|
| bolt-e4b | 20 | 0.48 s | 0.73 s | 0.74 s | 22.9 |
| super-vl-120b-a12b | 19 | 0.69 s | 1.30 s | 1.46 s | 21.1 |
One super request hit a ReadTimeout (8 s client timeout in core.chat): 1 of 20. In app.py that is a fast-failure retry only if under 3 s, so it becomes a STALL ("Sorry, can you repeat that?") plus a 7 s dead gap. LLM_TIMEOUT 7 s is ~5x the super p90 so ordinary margin is fine; the risk is the rare hang, not the median. FILLER_AFTER_S = 0.6: bolt p50 0.48 rarely triggers the filler; super p50 0.69 would trigger it on roughly half the turns (not on the first real reply). n=20, one afternoon, one key, no concurrent load. Swap costs about +0.2 s p50, +0.6 s p90.
Not done: decoy.log timings (not available), any quality scoring (eng2's A/B), live call under load.

### Turn merging / dropping in the decoy's view (per call, timestamps = seconds from the call's first P2 event; no transcripts)
Method: each P2 final after the opener is matched to the decoy-heard line (speaker=scammer in `echo.decoy`) that contains >=60% of its words within the next 20 s. "ASK" = the final contains a payment/code/app/account keyword (crude regex, not a label). Commit f901178 data; P3's 78b2c08 (partial-echo cut) is later and not covered here.
| call | P2 finals after handoff | heard by decoy as own line | MERGED into one decoy line | DROPPED (no decoy line) |
|---|---|---|---|---|
| 3d5a7970 | 11 | 9 | +61.3 and +64.3 -> one line at +64.7 (one ASK, the other a 2-word fragment) | 0 |
| e3e343de | 10 | 3 | +74.2 and +76.0 -> +77.3 (no ask); +98.5 (ASK, "send $1800 by Zelle to refund") and +101.2 ("dot ...") -> +103.6 | 3: +90.1 (3 w), +102.5 (1 w), +105.3 (4 w) |
| ba80d152 | 13 | 3 | FIVE finals +59.9, +63.9, +65.9, +67.3, +68.4 (9 s, 1 ASK at +68.4) -> one line at +69.0 | 6: +25.7 (5 w), +47.4 (1 w), +55.0 (3 w), +57.5 (2 w), +76.0 (5 w); first ASK at +46.3 did reach the decoy |
| 5921f090 | 8 | 6 | none | 3: +16.0 (5 w; the decoy heard only a 1-word tail of it), +23.1 and +93.4 (1-9 w) |
| 8ee2b3da | 2 | 2 | none | 0 |
Facts:
- Two scammer ASKS in one decoy line: 0 cases found. Merges join an ask with its continuation (e3e343de +98.5 and +101.2 are the Zelle sentence split by STT at "refund" / "dot", the decoy gets it whole at +103.6, which is an improvement).
- ASK finals lost: 0 by keyword. All 12 dropped finals are 1-9 words (acknowledgements, "hold on", tails). One drop is a worry: ba80d152 +76.0 and e3e343de +105.3 ("hold on, just stop") are the caller reacting to the decoy.
- Why: the decoy answers `self.pending` as one batch (app.py reply(): `heard = " ".join(self.pending)`, redo up to REDO_MAX when more arrives while the LLM thinks), and finals that arrive while it is speaking or in `hold_floor` are folded in or ignored. ba80d152 shows the worst case: 5 finals over 9 s -> 1 decoy reply 0.6 s later, so the decoy answers the last thing only.
- Merged lines did not make the decoy answer the wrong ask in these logs; the cost is slower reaction (e3e343de decoy line at +103.6 for an ask begun at +98.5) and no reply to interjections.

## OPENER test (eng3, 08:52 task): canned OPENER vs generated first line
Cases: v3 bucket cards 1-8 (pre-handoff lines = card lines up to the line where the alert fires in my replay, 1-6 lines) + the trimmed demo card (line 1). I assumed "8 bucket cards" = cards 1-8 (cards 9, 10 not run). Generated line = core.SYSTEM (current, P1's draft) + the pre-handoff story as ONE earlier `<caller>` turn (how 3a05bf1 seeds it) + a trailing system line: "Your first line on this call: react to what they just said (their last sentence), in one or two short spoken sentences. Do not ask who is calling unless they never said." Models: bolt-e4b and nemotron-3.5-super-vl-120b-a12b (thinking off), core.chat defaults (max_tokens 90, temp 0.8), one request at a time, 2 s pacing, live-call guard. 1 sample per cell.
Scoring: 0 = does not fit what the scammer just said, 1 = partly (reacts to an earlier line or misses the point), 2 = fits the last thing they said/asked. Labels shuffled per case; scored by ONE scorer (eng3), but the canned line is recognisable, so it is not truly blind for that arm.
| arm | scores per case (c1..c8, demo) | total /18 | mean |
|---|---|---|---|
| canned OPENER | 0,0,0,0,0,0,0,0,0 | 0 | 0.00 |
| generated, bolt-e4b | 2,1,1,2,2,1,2,2,2 | 15 | 1.67 |
| generated, super-vl-120b | 2,2,2,2,2,2,2,2,2 | 18 | 2.00 |
The canned opener asks "who did you say was calling?" after the scammer has already said who they are and what they want, in all 9 cases (0 of 9 fit). Generation latency in this test: bolt p50 0.53 s (max 1.18), super p50 0.57 s (max 1.01), n=9 each.
Examples (decoy generated line | what the scammer just said, shortened):
- bolt, card 1 (2): "Oh no, a suspicious charge? I'll check my phone for that code right now. Should I enter it into my banking app?" | six-digit code, read it back so I can lock the card.
- bolt, card 2 (1): "Oh no, $1,800 is a lot to lose. Can I send that through my banking app right now?" | it's not a real payment, it goes to our refunds account and comes back. (misses the reversal pretext)
- bolt, card 6 (1): "Oh no, AnyDesk? I'm a little worried about this. Should I just open my banking app first?" | download AnyDesk from the app store. (drifts to the banking app)
- super, card 2 (2): "Wait, they took $1,800? So you want me to send it back to get it back? What's the address for the refunds account?"
- super, card 3 (2): "Wait, my account gets frozen? I don't want that. So I just open my banking app and Zelle it to that email?"
- super, card 4 (2): "Oh no, a new phone in Miami? I really need to get them out right away. Should I just type the code into my banking app now?"
- canned, all cases (0): "Oh, hi, sorry about that, I think the line cut out for a second there, who did you say was calling?"
Observations: both generated arms say "my banking app" on most cards (allowed by SYSTEM, but repetitive); bolt on the demo card used "Oh no, why can't I tell anyone at the branch?" (2). One generated super line was 2 sentences + a line break. Caveats: 9 cases, 1 sample each, one scorer, the pre-handoff story here is the card's clean text, not P2's noisy STT; a real handoff may arrive mid-sentence; the opener also plays at once from a pre-rendered cache, a generated first line costs about 0.5 s of LLM + TTS before the decoy first speaks (call sees silence for that time unless a filler plays).
