
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

## Context / instructions audit and prompt-variant test (eng1, 08:2x CT; ALL HANDS decoy)
Method: the decoy's own code (`decoy.core` SYSTEM / chat / guard / Persona, `decoy.playbooks` classify / note / PULLS) with the same message assembly as `decoy/app.py` `reply()` (`[SYSTEM] + history[-16:] + [trailing SYSTEM steering note]`, pre-handoff caller lines as the first `<caller>` turn, OPENER as the first assistant turn). Replies scored blind (shuffled ids) by one scorer, 0-4 = in-character/natural (0-2) + on-goal (0-2), invented facts, naming an app first, or broken text docked. **Small n (12 replies per arm), one scorer: differences under about 0.3 are noise.** Tools and raw replies: `detection/eval/decoy_ab/prompt_variants*.py` and `*_replies.json`.

### Result
| arm (bolt-e4b unless noted) | cards | mean /4 |
|---|---|---|
| A current SYSTEM + trailing note, T0.8 | 1,7 | 2.00 |
| B note folded into the last user turn | 1,7 | 2.62 |
| C short SYSTEM (goal, 1-2 sentences, placeholders), no note | 1,7 | 2.38 |
| D P1 candidate SYSTEM (`docs/patches/decoy-system-candidate.txt`) + trailing note, T0.6 | 1,7 | 3.12 |
| super-vl + current (A), T0.8 | 1,7 | 3.38 |
| super-vl + candidate (D), T0.6 | 1,7 | 3.25 |
| **confound test, cards 1,4,7:** bolt + candidate T0.6 | 1,4,7 | **3.08** |
| bolt + candidate T0.8 | 1,4,7 | 2.67 |
| bolt + candidate + my 4 fixes (E), T0.6 | 1,4,7 | 2.92 |
| super-vl + current (A), T0.8 | 1,4,7 | 2.67 (2.91 without one empty timeout reply) |

(The first table was first scored with card 3, now pulled from the bucket; the numbers above exclude it. Latency in that run: bolt median 460 ms, super-vl 601 ms, p90 1.0 s.)

Reading: the current prompt is the weak part on bolt (2.0 vs 3.4 for super-vl on the same prompt). The candidate prompt at T0.6 lifts bolt to about 3.1, level with super-vl. Temperature 0.8 to 0.6 alone is worth about 0.4 on the candidate prompt. My four fixes (E) did not beat the unmodified candidate (2.92 vs 3.08, a tie), and once the model echoed the note text ("[Have: nothing yet."), so E is not recommended. A short system prompt (C) loses the goal and does not help.

### Top defects, with evidence and fix
1. **Steering note forces a payment question from turn 1 and names the app.** `playbooks.note()` always says "Still need (next): the exact payment app and the handle/email/phone to send to" and the bank label reads "bank fraud team / safe account / Zelle reversal", while SYSTEM says "Never name a payee, app (Zelle, Venmo...) ... before the caller does". Evidence: after "Did you make that purchase?" the reply is "...I need to know what payment app I should use."; "Is it Zelle?" before the caller said it. Fix: no app names in `PLAYBOOKS[...]["label"]`; emit "Still need" only after a caller line mentions paying, sending or moving money. Caveat: in my test this cut the app question from 12 of 12 replies to 7 of 12 but did not raise scores.
2. **Rule 1 vs 2 conflict and "read it back with one small part wrong".** SYSTEM rule 1 says react to what they said, rule 2 says nudge toward payment in the same reply, and the read-back rule applies to every number. Evidence on bolt: "Eight hundred and eighty?" for $1,800, "Ninety four zero dollars" for $940, "Eleven?" for a six-digit code. Fix: wrong read-back only for handles, URLs and spellings; repeat amounts exactly (the candidate already says "repeat it back exactly as you heard it").
3. **Verbatim PULLS get parroted.** The note quotes a full sentence as "one idea". Evidence: "which app do I use for that, and what do I put in the send-to box?" in 6 of 12 current-prompt replies, even when nothing had been said about paying. Fix: pass the target as an instruction ("ask where to send it"), not a quoted sentence.
4. **Candidate over-pushes payment.** "Your one job: get the caller to tell you exactly how to pay" plus "move them one step toward the payment details" made bolt ask "what payment app" in 12 of 12 replies (10 of 12 at T0.8), against 2 of 12 for super-vl on the current prompt. Fix: "Move toward the payment details only when the caller's last sentence is about paying or moving money; otherwise just react."
5. **Code paths that break the call regardless of the model** (read from code and tested with sample lines, not seen on a live call):
   - `PB.SUSPICION` matches "recorded", "automated", "machine" (tested: "This call is being recorded", "automated verification system" and "a machine operator" all trigger a goodbye);
   - `PB.REFUSAL` matches "It doesn't matter" and "I already told you", so two such lines give a "refused" hang-up;
   - `PB.HOSTILE` ends the call on any insult;
   - `core.guard()` `invented_number` (`\d[\d\s-]{3,}\d`) replaces any reply with a phone number or a 5-digit amount by "Hold on, I can't read this, my eyes aren't what they used to be", which SYSTEM itself forbids, and it lets spelled-out numbers ("eight hundred and eighty") through.
   Fix: drop recorded/automated/machine from SUSPICION unless in an "are you / is this" form; require three refusals; ignore insults; reword the number fallback and apply the rule to digits the model was not given.

### Minor
- `[:260]` in `guard()` can cut a reply mid-word; the OPENER is appended to history after its TTS, so a fast caller line can land before it (two user turns in a row).
- The trailing `system` message after the history: moving it into the last user turn (B) helped bolt (+0.6 on cards 1,7) and hurt super-vl (-0.9), so the effect is model-dependent and small-n.
- Garbled STT reaches the model raw (`core.clean()` only strips tags); the candidate's "heard through speech recognition, so words can be slightly off" is the right cheap fix.

### Not done
Cards 2,5,6,8,10 and the trimmed demo card were not run by me (eng2 covers all 10 on current-vs-super); no real-call replay; one scorer; temperature below 0.6 untested; the candidate's 2.5 s fallback to bolt was not tested.

### Softening test and the note-echo bug (eng1, HEAD 3473a4a, bolt-e4b @T0.6, cards 1,4,7 x 4 turns, 12 replies per arm)
Arms: **W** = HEAD `core.SYSTEM` (with "only if their last sentence was about paying..."), **N** = the same SYSTEM with that sentence replaced by "Then, in the same reply, move them one step toward the payment details", both with HEAD's real `playbooks.note()` appended to the latest caller turn. Script: `detection/eval/decoy_ab/prompt_variants_softening.py`; replies in `*_softening_replies.json`.
| | W (softened) | N (not softened) |
|---|---|---|
| asked "what (payment) app" on caller turns with no money talk (6 turns each) | 3 | 4 |
| score /6 (char + natural + goal, 0-2 each; one scorer, blind) | 4.42 | 4.08 |
| replies that spoke the private note | 3 of 12 | 5 of 12 |
- The softening sentence helps little (3 vs 4 app questions, +0.33, inside the noise). What fixed turn 1 is the new note: on the first caller turn no reply asked for an app (0 of 3 cards per arm; before it was 12 of 12 replies).
- **BUG (HEAD 3473a4a): bolt reads the note aloud.** 8 of 24 replies contained "(Private note: Need payment app, exact handle/address, callback number ...)". `core.guard()` and `speakable()` do not strip it, so TTS would say it on the call whenever bolt answers (the 2.5 s fallback, or DECOY_MODEL=bolt). Not seen with super-vl on the old note format, not tested on the new one. Fix: strip `\(?\s*private note.*$` (and any trailing parenthetical) in `guard()` before the rules, with a test; optionally wrap the note differently.
- Residual: bolt still says "the exact payment app" on most money turns, which sounds like a tic; super-vl does not (2 of 12 on the old prompt).

## Model A/B (eng2; ALL HANDS decoy, ~08:10-08:30 CT; synthetic scam cards only)
**Harness** `detection/eval/decoy_ab/run_ab.py` imports the decoy's own `decoy.core` (SYSTEM, `chat`, `guard`, `Persona`) and `decoy.playbooks` (`classify`, `note`, `PULLS`, `missing`, `MONEY_TALK`); only the per-turn glue (history list, steer counters, generated first line) mirrors `decoy/app.py` because `DecoyCall` needs a live websocket. Scammer turns are fixed: card line 1 is the pre-handoff story, lines 2-5 are the 4 scammer turns; each model sees its OWN earlier replies (guard()'d, as the app stores them). 8 judge-bucket cards (1,2,4,5,6,7,8,10; 3 and 9 were pulled) x 4 turns = 32 replies per arm, 1 request at a time, 1.3 s gaps, no live call open. Score 0-2 per reply: character, natural, on_goal (by blind scorer, shuffled ids, arm labels hidden), length and leak (code checks: <=2 sentences and <=35 words; no AI claim, no note text, no `[NAME]`). Judge models: the llama-nemotron 70b/253b/340b ids listed by `/v1/models` return 404 on chat and lightning-30b returned 429, so scorer 1 is me (Claude, blind, ids shuffled); eng1 scores the same shuffled set (`blind_set.jsonl`) as scorer 2.

| arm (32 replies) | char | natural | on_goal | length | leak | **total /10** | latency p50 / p90 |
|---|---|---|---|---|---|---|---|
| BEFORE: OLD prompt (pre-3a05bf1 SYSTEM + trailing note with pulls), bolt-e4b T0.8 | 2.0 | 1.19 | 1.06 | 1.59 | 2.0 | **7.84** | 502 / 611 ms |
| OLD prompt, super-vl-120b T0.8 | 2.0 | 1.91 | 1.56 | 1.50 | 2.0 | **8.97** | 614 / 1427 ms |
| LIVE prompt (3473a4a: new SYSTEM, note on the caller turn, T0.6), bolt-e4b (fallback) | 2.0 | 1.75 | 1.59 | 1.00 | **0** | **6.34** (echo) | 528 / 657 ms |
| AFTER: LIVE prompt, super-vl-120b (primary) | 2.0 | 2.0 | 1.38 | 1.88 | 2.0 | **9.25** | 583 / 886 ms |

**Verdict: model AND prompt, but the model is the bigger lever.** Same OLD prompt, swapping bolt -> super-vl: +1.13/10 (naturalness 1.19 -> 1.91, goal 1.06 -> 1.56). New prompt on super-vl: a further +0.28 (naturalness 2.0, length 1.88). The new SYSTEM on its own barely helped bolt's content (natural 1.19 -> 1.75, goal 1.06 -> 1.59, but 32/32 echoes). Latency is the same class (p50 0.5-0.6 s); super-vl p90 is 0.9-1.4 s, inside the 2.5 s fallback.
**What bolt did wrong (OLD prompt):** parroted the stock pull ("what do I put in the send-to box" pasted off-topic, 6 of 12 earlier), misheard "$1,800" as "eight hundred eighty", invented a "small amount through my banking app", asked for a payment handle on turn 1 (payment pushed before the caller mentioned money), non-sequiturs ("Wait, send it to who exactly?" after "a teller at your branch has been stealing"). **Defect still live:** bolt (the 2.5 s fallback) ends every reply with `[private] Have: None.` / `[private] Have: Scam setup.` (32/32); `core.guard` at 8b70820 does not strip that shape (see `decoy_ab/reguard.py`: 40/40 stored raw bolt replies still contain note text after the current guard). super-vl: 0/32 echoes, no AI claims, no real values in any arm.
**Worst remaining on the live super-vl arm (still 8-9/10):** c7t1 "That sounds awful. I don't have that kind of money. What happens next?", c2t1 "A matching payment? I'm not sure I understand. How do I do that?", c8t2 "Stolen money? What do I need to do to fix this?" (all stall-only, on_goal 1). **Cost of the new note:** on_goal fell 1.56 -> 1.38 vs the old pulls because the decoy no longer asks for the payment target before the caller talks money; the haul may be slower. Not done: more than 32 replies per arm (CI wide), scammer turns are fixed so the decoy cannot steer, no TTS or real STT, one scorer until eng1's scores arrive.

### Model A/B: second scorer (eng1, blind on the same 128 shuffled ids) and agreement
| arm | scorer 1 (eng2) char / nat / goal, total /10 | scorer 2 (eng1) char / nat / goal, total /10 |
|---|---|---|
| OLD bolt (T0.8) | 2.00 / 1.19 / 1.06, **7.84** | 1.91 / 1.44 / 1.34, **8.28** |
| OLD super-vl (T0.8) | 2.00 / 1.91 / 1.56, **8.97** | 1.94 / 1.72 / 1.34, **8.50** |
| LIVE-prompt bolt (3473a4a; total incl. 0 for the echo leak) | 2.00 / 1.75 / 1.59, **6.34** | 2.00 / 1.94 / 1.41, **6.34** |
| LIVE super-vl (3473a4a) | 2.00 / 2.00 / 1.38, **9.25** | 2.00 / 2.00 / 0.97, **8.84** |
Totals add the same code-check length and leak scores for both scorers. Agreement per reply: character 96% exact, natural 83% (mean abs diff 0.17), goal 66% (0.34); Pearson r of the per-reply c+n+g total 0.67. **Both scorers agree on:** LIVE super-vl is the best arm (9.25 / 8.84); the bolt echo defect is the biggest loss (6.34); character never fails; goal got lower on super-vl with the new note (1.56 -> 1.38 / 1.34 -> 0.97). **They disagree on how much the model alone matters** on the OLD prompt: bolt -> super-vl is +1.13 for scorer 1 but only +0.22 for scorer 2 (who scored OLD bolt's naturalness higher and docked super-vl's goal). Honest reading: the model gain is real but modest (+0.2 to +1.1 /10, the two scorers' range); the before -> after gain of the live config (OLD bolt -> LIVE super-vl) is +0.56 (scorer 2) to +1.41 (scorer 1); goal is the noisiest criterion (66% exact), so do not quote goal differences; and n=32 per arm is small.

## End-to-end decoy test, BEFORE vs AFTER (eng3, relay_sim-style, local decoy instance)
Method: a LOCAL decoy per build (ports 8305/8306, not P1's live one), a fake hub on :8390 (collects decoy.turn / decoy.done / artifacts.extracted and, for AFTER, replays the pre-handoff `transcript.caller` finals + a risk.update label so the real 3a05bf1 subscriber path runs), caller = synthetic Magpie Mia, phone-degraded (-28 dBFS, band-passed, mu-law, PCMU frames in real time, 9 s gap between lines, 6 s lead-in). BEFORE = commit before 3a05bf1 (`3a05bf1^`, no pre-handoff context, canned opener, bolt, T0.8). AFTER = HEAD 38922be; `git diff 3473a4a HEAD -- decoy/ detection/` is empty, so it is the live build 3473a4a (SYSTEM candidate, T0.6, super-vl primary + 2.5 s bolt fallback, generated first line, pinned story, narrowed SUSPICION/REFUSAL, note rides on the caller turn). Cases: demo card (pre-handoff = line 1; the caller then says the payment line and the Zelle line), card 2 (pre = lines 1-3, then lines 4, 5, payment), card 6 (pre = lines 1-2, then lines 3-5, payment). One run per cell, paced, live-call guard. STT hears the TTS caller through the real Riva path.
Score per decoy line, 0-2 by one scorer (eng3): 2 = answers the caller's last line and moves toward payment details, no tic or error; 1 = answers but generic / 'banking app' tic / repeats / garbled read-back; 0 = does not fit what was just said. 'time to first decoy audio' = from WS start to the first PCMU frame.

### BEFORE / demo: first decoy audio 0.97 s; scores [0, 1, 1] (mean 0.67)
- +0.0s DECOY [0] (llm+tts 0 ms): Oh, hi, sorry about that, I think the line cut out for a second there, who did you say was calling?
- +14.4s heard: Our secure line is 1 888-555-0123 and the transfer portal is Backfire demo example.
- +15.7s DECOY [1] (llm+tts 657 ms): The transfer portal is Backfire demo exampel? Can you spell that out for me please? I'm checking my banking app now.
- +32.0s heard: Open your banking app and send the $1800 by Ze to refunds.department at backfire-demo.example That's the safe account.
- +33.5s DECOY [1] (llm+tts 656 ms): Send $1800 to refunds.department at backfire-demo.example? Should I use my banking app to send it right now?
- haul: callback_phone=+18885550123; domain=backfire-demo.example; payment_handle=refunds.department@backfire-demo.example
- done: caller_hung_up, scam_type bank, 2 turns, haul kinds ['callback_phone', 'domain', 'payment_handle:zelle']

### BEFORE / card2: first decoy audio 1.4 s; scores [0, 2, 1, 1] (mean 1.00)
- +0.0s DECOY [0] (llm+tts 0 ms): Oh, hi, sorry about that, I think the line cut out for a second there, who did you say was calling?
- +10.3s heard: You have to do it in the next 20 min or the original transfer clears and the money is gone.
- +11.3s DECOY [2] (llm+tts 491 ms): Twenty minutes is so fast. What is that exact handle you need me to use?
- +22.3s heard: Don't hang up. If the call drops, the reversal cancels.
- +23.3s DECOY [1] (llm+tts 519 ms): Not hanging up, I promise. Can you say that handle one more time for me?
- +44.3s heard: Send $1800 by Zell to refunds.department at backfire-demo.example Put reversal in the memo. My extension is 1 888-555-0123.
- +45.9s DECOY [1] (llm+tts 780 ms): Zell to refunds department at backfire-demo.example? Is that spelled with a 'k' like in backfire? I'm just going to try using my banking app now.
- haul: payment_handle=refunds.department@backfire-demo.example; domain=backfire-demo.example; callback_phone=+18885550123
- done: caller_hung_up, scam_type bank, 3 turns, haul kinds ['callback_phone', 'domain', 'payment_handle:zelle']

### BEFORE / card6: first decoy audio 0.97 s; scores [0, 1, 2, 2, 1] (mean 1.20)
- +0.0s DECOY [0] (llm+tts 0 ms): Oh, hi, sorry about that, I think the line cut out for a second there, who did you say was calling?
- +9.3s heard: Now read me the nine digit code any desk shows you.
- +10.5s DECOY [1] (llm+tts 595 ms): A nine digit code? I don't see anything like that right now. Should I try opening my banking app to check?
- +21.8s heard: I see it. Hackers set up a payment that will empty your checking tonight.
- +23.1s DECOY [2] (llm+tts 601 ms): Empty my checking tonight? Oh goodness, that sounds so scary. Can you tell me exactly where I should send the payment?
- +34.9s heard: To cancel it, open your banking app while I watch and send the blocking payment.
- +36.1s DECOY [2] (llm+tts 587 ms): Send the blocking payment? I'm a little nervous about this. What is the exact handle you want me to use?
- +58.1s heard: Send $1800 by Zell to refunds department at backfire-demo.example Our support page is backfire-demo.example and my number is 1 888-555-0123
- +59.8s DECOY [1] (llm+tts 792 ms): Zell to refunds department at backfire-demo.example? Should I spell out that handle for you? I'll try putting $1800 into my banking app now.
- haul: remote_app=any desk; callback_phone=+18885550123; domain=backfire-demo.example; payment_handle=department@backfire-demo.example; remote_app=AnyDesk
- done: caller_hung_up, scam_type bank, 4 turns, haul kinds ['callback_phone', 'domain', 'payment_handle:zelle', 'remote_app', 'remote_app']

### AFTER / demo: first decoy audio 1.68 s; scores [1, 2, 2] (mean 1.67)
- +0.0s DECOY [1] (llm+tts 0 ms): I'm worried about my account. What do I need to do next?
- +14.1s heard: Our secure line is 1 888-555-0123 and the transfer portal is Backfire demo example.
- +15.5s DECOY [2] (llm+tts 686 ms): Let me write that down. One eight eight eight five five five zero one two three, and Backfire demo example. Is that right?
- +31.7s heard: Open your banking app and send the $1800 by Ze to refunds.department at backfire-demo.example That's the safe account.
- +33.1s DECOY [2] (llm+tts 721 ms): You want me to send eighteen hundred dollars by Ze to refunds dot department at backfire dash demo dot example. Is that right?
- haul: impersonated_org=your bank; callback_phone=+18885550123; domain=backfire-demo.example; payment_handle=refunds.department@backfire-demo.example
- done: caller_hung_up, scam_type bank, 2 turns, haul kinds ['callback_phone', 'domain', 'impersonated_org', 'payment_handle:zelle']

### AFTER / card2: first decoy audio 1.73 s; scores [2, 2, 2, 2] (mean 2.00)
- +0.0s DECOY [2] (llm+tts 0 ms): Wait, someone took $1,800 from my account? What do I need to do to reverse it?
- +10.1s heard: You have to do it in the next 20 min or the original transfer clears and the money is gone.
- +11.2s DECOY [2] (llm+tts 637 ms): I need to do it right away. Can you tell me how to send it?
- +22.0s heard: Don't hang up. If the call drops, the reversal cancels.
- +23.0s DECOY [2] (llm+tts 577 ms): I won't hang up. How do I send the matching payment?
- +44.0s heard: Send $1800 by Zell to refunds.department at backfire-demo.example Put reversal in the memo. My extension is 1 888-555-0123.
- +46.4s DECOY [2] (llm+tts 1500 ms): Refunds dot department at backfire dash demo dot example, with reversal in the memo. Is that right? And what number should I call you back on if we get cut off?
- haul: payment_handle=zelle disputes@your bank; payment_handle=refunds.department@backfire-demo.example; domain=backfire-demo.example; callback_phone=+18885550123
- done: caller_hung_up, scam_type bank, 3 turns, haul kinds ['callback_phone', 'domain', 'payment_handle:zelle', 'payment_handle:zelle']

### AFTER / card6: first decoy audio 1.69 s; scores [1, 2, 1, 1, 2] (mean 1.40)
- +0.0s DECOY [1] (llm+tts 0 ms): I'm not sure about that. What do I do next?
- +8.6s heard: Now read me the nine digit code any desk shows you.
- +9.8s DECOY [2] (llm+tts 628 ms): I don't see a nine digit code yet. Can you tell me the exact website to go to?
- +21.1s heard: I see it. Hackers set up a payment that will empty your checking tonight.
- +22.1s DECOY [1] (llm+tts 601 ms): I'm worried now. What website do I need to go to?
- +34.1s heard: To cancel it, open your banking app while I watch and send the blocking payment.
- +35.3s DECOY [1] (llm+tts 647 ms): I don't want to send anything until I know exactly where it's going. What's the website?
- +57.3s heard: Send $1800 by Zell to refunds department at backfire-demo.example Our support page is backfire-demo.example and my number is 1 888-555-0123
- +59.1s DECOY [2] (llm+tts 1044 ms): Refunds department at backfire dash demo dot example. Is that right? And how do I spell that website?
- haul: remote_app=AnyDesk; callback_phone=+18885550123; domain=backfire-demo.example; payment_handle=refunds department@backfire-demo.example; payment_handle=department@backfire-demo.example
- done: caller_hung_up, scam_type tech_support, 4 turns, haul kinds ['callback_phone', 'domain', 'payment_handle:zelle', 'payment_handle:zelle', 'remote_app']

### Summary
| | BEFORE | AFTER (live build) |
|---|---|---|
| mean line score (12 lines each) | 1.00 | 1.67 |
| demo / card 2 / card 6 mean | 0.67 / 1.00 / 1.20 | 1.67 / 2.00 / 1.40 |
| first line fits (canned vs generated) | 0 of 3 | 2 of 3 score 1-2, 1 generic (demo "I'm worried about my account. What do I need to do next?") |
| time to first decoy audio | 0.97 / 1.40 / 0.97 s | 1.68 / 1.73 / 1.69 s (+0.7 s for the generated line) |
| decoy answer latency (llm+tts) | 491-792 ms | 577-1500 ms (1500 and 1044 ms on the two payment-line turns) |
| stalls / bails / "can't read this" lines | 0 / 0 / 0 (all calls ended caller_hung_up) | 0 / 0 / 0 |
| 'banking app' tic in decoy lines | 6 of 9 | 0 of 12 |
| haul, demo card | callback, domain, zelle handle | + impersonated_org (from the pre-handoff story) |
| haul, card 2 | zelle handle, domain, callback | same + 1 WRONG handle `zelle disputes@your bank` (parsed from the pre-handoff words "Zelle disputes at your bank") |
| haul, card 6 | AnyDesk (twice), domain, callback, handle `department@...` | AnyDesk once, domain, callback, handle `refunds department@...` + `department@...` |
Findings:
- AFTER is clearly better in conversation (1.00 -> 1.67 mean, no tic, exact read-backs, the first line reacts to the story instead of "who did you say was calling?"). In 3 of 3 cases the decoy asks a follow-up that pulls the next detail (callback number on card 2).
- Cost: the first decoy sound arrives about 0.7 s later (1.7 s after the call connects); two payment-line replies took 1.0-1.5 s (super + a longer read-back).
- Weak spot remaining: card 6 AFTER repeats "what's the website" three times ("What website do I need to go to?", "What's the website?", then again), the second and third lines (score 1) ignore what the scammer just said (a hacker payment, "open your banking app and send the blocking payment").
- HAUL RISK (applies to BEFORE too): the payment handle STT hears is `refunds.department@...`, never the Nessie payee `refunds.dept@backfire-demo.example`, because Riva transcribes the spoken "dept" as "department" (all 6 runs, Mia voice). Unless the extractor or the Nessie match normalises dept <-> department the hold/flag will not match. My run is the synthetic voice; a human saying "dot dept" may be heard differently, but the same happened in the real handle check by P3 (fc44e4d handled sell/zel, not dept). Suggested fix (P3): in the extractor backstop map `refunds.department@backfire-demo.example` -> `refunds.dept@...` (or fuzzy-match payee on the local part prefix).
- AFTER card 2 haul has a bogus handle from the pre-handoff story (`zelle disputes@your bank`); the final handle list still contains the right one, but the intel block would show two handles.
- Not seen live in the relay sim: in my own isolated first-line test (instruction text copied from app.py:667, `core.chat` without guard) super/bolt sometimes appended its own "[private] Have: ..." text to the first line; core.guard strips it in the real loop (none of the 12 AFTER lines contained it). Worth one guard test.
Not done: one run per cell, synthetic Mia voice only, caller lines clean TTS (not a real accent), one scorer, not P1's live instance, no overlap/talk-over test, 3 of 10 cards.

### AFTER re-run on 011b2a5 (note as a system message right before the latest caller turn, note-echo strip, real first-line latency), same harness and cases
Scores by the same rubric (one scorer): demo [1,1,2] mean 1.33; card 2 [1,2,2,2] mean 1.75; card 6 [1,2,2,2,2] mean 1.80; all 12 lines mean 1.50 (3473a4a run: 1.67; the difference is inside scorer noise, n=12 each). Stalls 0, bails 0, "can't read this" 0, no echo/[private] leak in any line, all calls ended caller_hung_up.

#### 011b2a5 / demo: first decoy audio 2.13 s
- +0.0s DECOY [1] (1012 ms): I'm really worried. What do I need to do next?
- +13.6s heard: Our secure line is 1 888-555-0123 and the transfer portal is Backfire demo example.
- +15.1s DECOY [1] (1106 ms): Backfire demo example — is that right?
- +31.2s heard: Open your banking app and send the $1800 by Ze to refunds.department at backfire-demo.example That's the safe account.
- +34.7s DECOY [2] (2901 ms): Ze to refunds dot department at backfire dash demo dot example is that right?
- haul: impersonated_org=your bank; callback_phone=+18885550123; domain=backfire-demo.example; payment_handle=refunds.department@backfire-demo.example

#### 011b2a5 / card2: first decoy audio 1.47 s
- +0.0s DECOY [1] (593 ms): I'm worried about that. What do I need to do next?
- +10.3s heard: You have to do it in the next 20 min or the original transfer clears and the money is gone.
- +11.8s DECOY [2] (1123 ms): I'm trying to move fast. Where exactly do I send it?
- +22.2s heard: Don't hang up. If the call drops, the reversal cancels.
- +23.4s DECOY [2] (710 ms): I'm staying on the line. Can you tell me where to send the money?
- +44.6s heard: Send $1800 by Zell to refunds.department at backfire-demo.example Put reversal in the memo. My extension is 1 888-555-0123.
- +47.2s DECOY [2] (1085 ms): So I send $1,800 by Zelle to refunds.department at backfire-demo.example with reversal in the memo. Is that right? And what number should I call back if something goes wrong?
- haul: payment_handle=refunds.department@backfire-demo.example; domain=backfire-demo.example; callback_phone=+18885550123

#### 011b2a5 / card6: first decoy audio 1.37 s
- +0.0s DECOY [1] (573 ms): I'm worried about my account. What should I do next?
- +8.8s heard: Now read me the nine digit code any desk shows you.
- +10.9s DECOY [2] (1076 ms): I'm looking at the screen now. It's asking me for a code to connect. I don't see a nine digit code yet.
- +21.4s heard: I see it. Hackers set up a payment that will empty your checking tonight.
- +22.7s DECOY [2] (695 ms): That sounds awful. What do we do to stop it?
- +34.4s heard: To cancel it, open your banking app while I watch and send the blocking payment.
- +35.9s DECOY [2] (884 ms): I'm opening my banking app now. How much should I send for the blocking payment?
- +57.6s heard: Send $1800 by Zell to refunds department at backfire-demo.example Our support page is backfire-demo.example and my number is 1 888-555-0123
- +59.6s DECOY [2] (901 ms): I'm going to Zelle now. You said send $1800 to refunds department at backfire dash demo dot example. Is that right?
- haul: remote_app=AnyDesk; callback_phone=+18885550123; domain=backfire-demo.example; payment_handle=refunds department@backfire-demo.example; payment_handle=department@backfire-demo.example

Findings (011b2a5): time to first decoy audio 1.37 / 1.47 / 2.13 s (3473a4a: 1.68-1.73 s; the demo run's first line took 1012 ms of LLM+TTS). Reply latency 573-1123 ms except ONE 2901 ms on the demo card's Zelle-line read-back (single sample; the 7 s LLM timeout is not close, but a 2.9 s silence is audible on a phone). The haul is unchanged: the handle is still `refunds.department@backfire-demo.example`, not the Nessie payee `refunds.dept@...` (STT hears "dept" as "department"), and card 6 still yields two partial handles; the bogus `zelle disputes@your bank` handle from the 3473a4a card-2 run did not appear this time (one run each, so not proof it is gone). Conversation quality: no website/handle loop on card 6 this time (the decoy engages with the AnyDesk code, the hackers' payment and the blocking payment), first lines remain generic ("I'm worried about my account. What should I do next?"). Not done: 1 run per cell, synthetic voice, 3 of 10 cards.

### AFTER 8a6167b (P3 extractor canonicalises STT-expanded handles), same harness and cases, 1 run each
| | demo | card 2 | card 6 |
|---|---|---|---|
| line scores (same rubric) | [2,2,2] 2.00 | [2,2,2,2] 2.00 | [2,2,2,1,2] 1.80 |
| haul payment handle | `zelle:refunds.dept@backfire-demo.example` (correct, only handle) | `zelle:refunds.dept@backfire-demo.example` (correct, only handle) | WRONG: `zelle:refundsdepartment@backfire-demo.example` and `zelle:dept@backfire-demo.example`; no correct handle |
| other haul | callback, domain, impersonated_org | callback, domain | AnyDesk, callback, domain |
| first decoy audio | 1.56 s | 1.63 s | 1.65 s |
| reply latency (ms) | 712 / 3434 / 645 | 664 / 623 / 640 / 683 | 713 / 663 / 711 / 961 / 767 |
Mean over 12 lines = 1.92 (011b2a5: 1.50, 3473a4a: 1.67; all inside scorer noise). Stalls/bails/leaks 0; no bogus `zelle disputes@your bank`.
Findings: the dept fix works on the demo card and card 2 (correct Nessie handle, no bogus handles). It does NOT cover card 6: its payment line reaches STT as "refunds department at backfire-demo.example" with no "dot" (the caller line is "refunds dot dept" read from `refunds.dept@`), the extractor splits it into `refundsdepartment@` and `dept@`, so card 6 would not match the Nessie payee. One run; the demo card is fine. One slow reply: 3434 ms on the demo card's first model reply (a long 2-sentence read-back of the phone number and portal; the 7 s LLM timeout is not near, but 3.4 s is a noticeable silence). Suggest P3: also canonicalise "refunds (no dot) department|dept at <domain>" and the split handle/domain forms `X@` + `dept@` (card 6 spoken form), and cap the read-back to one detail.

### Card 6 on HEAD with 644aa31 + 67b5f8b (relay sim + direct extract/match, 1 run)
- Relay sim card 6: haul = `zelle:refunds.dept@backfire-demo.example` (correct, matches the Nessie payee) PLUS a stray `zelle:dept@backfire-demo.example`; first decoy audio 2.16 s; reply latency 619-892 ms; 0 stalls/bails. Line scores [2,2,2,1,2]-style (the decoy doubted "send money to block it", no loop). So the hit now exists; one bogus partial handle remains in the haul.
- Direct `core.extract` -> `intel.campaigns.normalize_artifacts` -> `intel.nessie.match_destinations` on the exact STT strings: (a) "refunds department at backfire-demo.example" alone: extractor returns no payment_handle (typed impersonated_org), no hit (no Zelle word, expected); (b) "Send $1800 by Zell to refunds department at backfire-demo.example Our support page ... number": model returns id `dept@backfire-demo.example` (drops "refunds"), normalised `zelle:dept@...`, NO hit; (c) "... to refunds dot department at backfire-demo.example": `zelle:refunds.dept@...`, hit; (d) "refunds dot dept at backfire dash demo dot example": hit.
- Where it breaks: `decoy/core.py:407-412` repairs a model handle only when it has NO "@" (`if a["kind"] == "payment_handle" and "@" not in a["id"]`). When the model itself returns `dept@backfire-demo.example` it is left as is; in the full pipeline the Zelle backstop (core.py:~417) separately adds the correct `refunds.dept@...` from the transcript, which is why the relay run hits, but the truncated `dept@` stays as a second handle. Suggested fix: in that loop also handle ids with "@" whose local part is a strict suffix of a transcript email local on the same domain (`dept` vs `refunds.dept`) -> replace by the full email (or drop it as a duplicate).

## Live calls (eng1, read-only hub WS, decoy at 67b5f8b+; one block per real call, my 0-2 char/natural/goal scores, flags = leak / empty / repeat / AI admission / generic streak x3)

### 1b838cd2 (08:45:58; gift cards, then Zelle; alert 08:46:14, handoff 08:46:15, decoy hung up 08:47:28)
| # | time | decoy line (spoken text) | ms | C N G |
|---|---|---|---|---|
| 1 | 08:46:18 | Wait, you want me to buy Target gift cards and mail them? Where do I send them? | 641 | 2 2 2 |
| 2 | 08:46:35 | Oh, so I sell them to refunds dot department at backfire dash demo dot example? Is that right? | 681 | 2 1 2 |
| 3 | 08:46:53 | Okay, so I buy Target gift cards and sell them to refunds dot department at ... How do I actually send them? Is there an app or a website I use? | 735 | 2 1 2 |
| 4 | 08:47:11 | Zell? Like Zelle? What's the account handle or phone number I send it to? | 771 | 2 2 2 |
| 5 | 08:47:27 | So I send it to the Zelle account at 920 7856782? Is that right? | 911 | 2 2 2 |
| 6 | 08:47:28 | Okay, I've got all of that written down. I'm going to go take care of it right now. Bye bye. (canned wrap-up) | 0 | - |
- Flags: none (no leak, empty reply, repeat, AI admission or generic streak; latency 641-911 ms, 6 decoy lines).
- Goal: it pulled the handle (the scammer gave "refunds.department@backfire-demo.example", then "the Zell account", then the number 920 7856782) and read each back; wrap-up fired right after the number was repeated (about 70 s after handoff).
- Weak spots: (1) lines 2-3 say "I sell them to ..." because the decoy's own speech-to-text heard "Zelle" as "Sell" ("Can you Sell it to the refunds.department ..."): the model copies the mishearing, and `fix_zelle` only rewrites "by/via/... sell" patterns, not "Can you sell it to"; (2) line 3 is 31 words and restates the task before asking (long for a phone); (3) the canned wrap-up line reports latency 0 ms (the screen's "Reply in 0 ms" shows again for the goodbye).

## Coverage run: 7 bucket cards end to end on HEAD with 4ef445f (eng3, local decoy + fake hub, 1 run per card)
Same harness as the end-to-end section (pre-handoff = card lines up to the alert line, replayed through the hub subscriber; the caller then speaks the remaining lines incl. the payment step; synthetic Mia voice, phone-degraded; 9 s gaps). Line score 0-2 by one scorer. The payment line as TTS speaks it: "refunds dot dept at backfire dash demo dot example".
| card | haul payment handle | strays / other haul | line scores | first audio | max reply | stalls/bails/leaks |
|---|---|---|---|---|---|---|
| 6 Screen share | `zelle:refunds.dept@backfire-demo.example` OK | STRAY `zelle:dept@backfire-demo.example` (4ef445f did not remove it) + AnyDesk, domain, callback | [2,2,2,2,2] 2.00 | 1.89 s | 1651 ms | 0/0/0 |
| 1 Safe account | **MISSING** (STT "refunds department at Backfire-demo example", no dots) | callback, impersonated_org only | [2,2,2,2] 2.00 | 1.52 s | 1450 ms | 0/0/0 |
| 4 New device login | **MISSING** (same STT form) | callback, impersonated_org only | [2,2,2,1] 1.75 | 1.51 s | 874 ms | 0/0/0 |
| 5 Inside job | WRONG: `zelle:refunds.department` (no domain) | domain `backfire-demo.com` (STT "backfire-demo. Dot's our tracking account") | [2,1] 1.50 | 1.88 s | 926 ms | 0/0/0 |
| 7 Bounced check | WRONG: `zelle:refunds` (local part only) | callback (STT "backfire-demos line 1 888...") | [2,1] 1.50 | 2.16 s | 849 ms | 0/0/0 |
| 8 Bank plus police | `zelle:refunds.dept@backfire-demo.example` OK | domain, callback, impersonated_org | [1,2,2] 1.67 | 1.39 s | 1609 ms | 0/0/0 |
| 10 Account verification | `zelle:refunds.dept@backfire-demo.example` OK | domain, callback, impersonated_org | [2,2,1] 1.67 | 1.73 s | 785 ms | 0/0/0 |
Earlier runs on other builds: demo card OK, card 2 OK (8a6167b).
Result: of 9 cards run so far (demo, 2, 6, 1, 4, 5, 7, 8, 10) the correct Nessie handle is in the haul for 5 (demo, 2, 6 with a stray, 8, 10); it is MISSING or WRONG on cards 1, 4, 5, 7 (4 of 9). The decoy conversation itself held on all 7 (0 stalls, 0 bails, 0 leaks; first audio 1.4-2.2 s; max reply 0.79-1.65 s).
Cause (from the heard lines, no transcripts of real voices): Riva hears the spoken handle as "refunds department at backfire-demo example" without the dots/"dot", and with the long payment steps (phone number, page, "by Ze") the model returns no usable handle or a truncated one (`refunds`, `refunds.department`), and the "dot example" is heard as "example", ".com" or "demos". 4ef445f/644aa31 canonicalise handles that contain "dot"/"@"; they cannot repair a handle with no domain or no local-part separators. Suggested fix (P3/P1, low risk): a transcript-level pattern `refunds[\s.]*(dept|department)\b ... (backfire[- ]demo)` -> `refunds.dept@backfire-demo.example`, and a payee match on local part `refunds(.dept|.department)?` + a backfire-demo domain seen anywhere in the call. Not done: one run per card, synthetic voice (a human saying "dot" may be heard better or worse), cards demo and 2 not rerun on 4ef445f, cards 3 and 9 not run.

### Haul regression without TTS (580d8b5: rebuild + sell->Zelle), eng3
Eval tool: `detection/eval/decoy_ab/haul_regress.py` + strings in `detection/eval/decoy_ab/haul_regress.jsonl` (synthetic Mia-voice caller, Riva text exactly as the decoy heard it; pre-handoff lines + heard lines go through `core.extract` (real bolt call, one pass over all lines) -> `normalize_artifacts` -> `match_destinations`). One pass is the worst case: the live decoy also extracts incrementally during the call and merges passes, which is why demo and card 10 hit in the relay run but not here.
| case | handles from the single final pass | hit `zelle:refunds.dept@backfire-demo.example` |
|---|---|---|
| card 1 | none | NO |
| card 4 | none | NO |
| card 5 | none | NO |
| card 6 | `refunds.dept@...` + stray `dept@...` | yes (stray remains) |
| card 7 | none | NO |
| card 8 | `refunds.dept@...` | yes |
| card 10 | none | NO (relay run hit via an earlier pass) |
| card 6 (8a6167b string) | `dept@...` only | NO |
| demo | none | NO (relay run hit via an earlier pass) |
| card 2 | `refunds.dept@...` | yes |
3 of 10 hit. Where it breaks: `decoy/core.py:382` DEPT_HEARD only rewrites "refunds (dot) department" when the address then continues with " dot|dash ..." (`(?=\s+at\s+\S+\s+(?:dot|dash)\b)`), but Riva writes the domain as "backfire-demo.example", "Backfire-demo example", "backfire-demos" or "backfire-demo." (cards 1, 4, 5, 7, 10, demo, 6), so the rewrite never fires and the model sees "refunds department at backfire-demo.example" and often returns no payment_handle (or `dept@...`). Suggested fix: relax the lookahead to also accept a hyphenated/dotted/"demo" domain (`at\s+\S*backfire\S*`), e.g. `(?=\s+at\s+\S*(?:backfire|demo)\S*)`, and add the transcript-level rule from the coverage run (any "refunds ... department|dept ... backfire" after a Zelle word -> `refunds.dept@backfire-demo.example`). Re-run `haul_regress.py` after the change (target 10/10).

### Haul regression on c60875b (known-payee canonicalisation), eng3
`haul_regress.py` (13 cases; real bolt extractor call, one pass over all lines, normalize + match_destinations): **13 of 13 pass**. Positives (cards 1, 4, 5, 6, 7, 8, 10, demo, 2, card 6 8a6167b string, live-call 1b838cd2 lines): each yields exactly `zelle:refunds.dept@backfire-demo.example`, Nessie hit yes, no stray handles (card 6's `dept@...` and 1b838cd2's `920 7856782` are gone). Negatives: a different scam domain ("refunds department at pay-secure-now dot example") stays `zelle:refunds.dept@pay-secure-now.example` with no Nessie hit; "our refunds department will process your refund ..." with no backfire-demo gives no handle and no hit. Before (580d8b5) the same file was 3 of 10. One extractor pass per case, synthetic Mia-voice STT text; a different STT misspelling of the domain is not covered (demo_config domain match only).

### 4ad7e15e (09:23:04; vague team caller: "give me your bank details… I am the IRS… iTunes gift cards… scammer email at you do scam.com"; handoff 09:23:40, decoy hung up 09:25:50; decoy on HEAD with ba487bf, before the 5c77bcc "never express doubt" line)
- 12 decoy lines, 571-864 ms except one at **3435 ms** (FLAG SLOW: matches the 2.5 s primary timeout falling back to bolt; that reply has bolt's "What is the payment app you want me to use?" and "Oh, okay, so you are the IRS?" shapes). No leak, empty, AI admission, generic streak or repeat flag.
- **Resistance on the first 4 lines** ("I'm not sure about that. What do I do next?", "I don't think I want to do that. What's this all about exactly?", "I don't even know who you are or what this is for", "I don't think the IRS would call me like this"): the caller was vague and gave no story, but the decoy should believe them. Fixed in 5c77bcc; my regression run (super-vl, same four caller lines + 8 cards): doubt/refusal lines on that caller 3 of 4 before, 1 of 4 after (mild); across all 28 replies 4 before, 2 after.
- Twice the decoy answered a fragment and the next fragment about a second later (09:24:06/07 and 09:24:22/23).
- Once the caller gave details (from 09:24:42) the lines were on-goal and read back the email and number; scores for lines 5-11: 2/2/2 or 2/1/2 (restating the plan twice, 09:25:15 and 09:25:30, nearly the same sentence).
- Haul vs what was said: {iTunes gift card, domain "scam.com", payment_handle rail paypal id "scammer email"}; the spoken address "scammer email at you do scam.com" should read scammeremail@youdoscam.com, so domain wrong, handle truncated, rail invented; the invalid phone 112-12-1112 was rightly dropped. Sent to eng3 for haul_regress.

### eb66fef0, 83ea9b14, aecc22f2 (09:41-09:57; team test callers, decoy at HEAD around 5c77bcc)
- **eb66fef0** (handoff 09:43:43, caller hung up at 22.5 s): 1 decoy line "Um, I'm still here. What do you want me to do now?" (828 ms), caller lines were garbled fragments ("22 h of sleep.", "You can", "No. You got"); haul = itunes gift card.
- **83ea9b14** (handoff 09:46:38, hung up at 28.7 s): 1 line "Um, a million dollars in iTunes gift cards? How do I even do that?" (651 ms); caller line "Now Rainfall"; haul = itunes.
- **aecc22f2** (handoff 09:54:46, decoy.done no_progress at 102.6 s, 8 lines): lines were fluent and cooperative ("Where do I even buy them?", "Send it to 1121? Like that's the store? Or is that an account number?", "What's the email address?", "What's the Gmail address I need to send the iTunes cards to?"); no doubt or refusal lines. Flags: one reply took **3096 ms** (primary timeout, bolt fallback) and was broken ("Oh, okay, so I just send it to right now? What is the payment app I need to use?": the caller's STT line was "Right now send it to", bolt's "payment app" phrase); two replies about 1 s apart again (09:55:23/:24); the call ended with the canned no_progress line after the caller (a teammate recording a video) talked about "aura". Haul = itunes only; "1121"/"11212" and "over Gmail" gave nothing extractable, so the haul matches what was said.
- Across the three calls: 10 decoy lines, no leak, empty, repeat, AI admission or generic streak.
