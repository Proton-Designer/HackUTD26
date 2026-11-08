# Failure drills (TASK-055), private stack
Hub :8190 + P2 :8102, own processes, SYNTHETIC irs.wav (Magpie voice, 2 caller lines, ask line "pay today with gift cards") streamed as Telnyx frames by `scripts/drills.py`. Gap = `alert.fired` time minus the end of the ask line (negative = alert came before the line ended). Single run each, 2026-11-08 ~04:50 CT. Real 429s were not produced: refused connections stand in for them.

| # | Drill | Result | healthz shows | Operator action |
|---|---|---|---|---|
| 1a | llama down (LOCAL_LLM_URL dead), cloud ok | 1 alert, gap -1.72 s, engine `cloud`, max s 0.97 | `local_reachable` false, `failovers.local_to_cloud` rising | none; watchdog restarts llama in ~2 min |
| 1b | llama AND cloud dead | 1 alert, gap -0.65 s from the rules floor (risk.update engine still labelled `local`), max s 0.95 | `local_reachable` false, `last_error` empty | none for the alert; restore llama/network for nuance |
| 2 | Riva and cloud LLM refuse (429 stand-in), llama up | 1 alert, gap -0.05 s (whisper finals are slower), 2 finals, engine `local`, max s 0.95 | `stt.primary_failures` 2, `primary_bypassed` true (bypass 30 s, then re-probes) | none |
| 3a | hub killed 1 s into the call, back 5 s later (before the ask) | 1 alert, gap -1.75 s, no duplicate; one early final lost while the hub was down | `hub_subscriber_connected` false then true within ~20 s; `last_error` hub.emit ConnectError | none; P2 reconnects by itself |
| 3b | hub down across the alert moment (8.5 s) | BEFORE fix: alert lost, 0 alerts (bug). AFTER fix (alert.py `_emit_alert`, retry up to 20 s): 1 alert delivered 6.9 s after the ask line, when the hub came back, no duplicate | same as 3a | none; if the hub stays down > 20 s the alert is dropped, restart the hub and press Continue/replay |
| 4 | P2 process killed mid-call (before the ask) | hub stays healthy (200); that call gets no alert (no detector); restarted P2 healthy in 0.8 s; the next call alerts normally (gap -1.03 s) | after restart: `local_reachable` true, hub sub true, counters reset | watchdog restarts p2svc on refusal; the call in progress is not recoverable from P2: P1's relay must reopen `/stt/<id>` |
| 5 | Tunnel URL changes | Not run live. Path by code + `tests/test_watchdog.py` (fake cloudflared): watchdog probes `<tunnel>/healthz` every 60 s, 3 fails in a row (~3 min) restarts p2tunnel, parses the new URL into `logs/p2_tunnel_url.txt` and logs `!!!! TUNNEL URL CHANGED !!!!`; never restarts while `active_stt_sockets`>0 | n/a (URL differs from before) | lead tells P1 `P2_STT_URL=wss://<host>`, P1 restarts the relay between calls. Faster: `WD_TUN_EVERY=1` makes detection ~1.5 min |
| 6 | Handoff tap (F6, TASK-066), method: real `voip/router.py` restore code, `vr.handoff()` called in-process on the first alert.fired (POST /events rejects the reserved handoff.started), RESTORE_LOW_S=10, private hub :8194 + P2 :8104, local engine, HEAD 1c52469 | HARD (real dump 499a20d2): after the tap scores stay 0.95, benign closing line = 0.60 (sticky floor), no restore. SOFT (synthetic, 1 IRS opener, no hard ask, then benign lines): scores 0.05, handoff.restored 16.5 s after the tap. Scam lines continuing past the 30 s restore window: no restore | `handoff` state in hub events; risk.update s | none |

## Card 2 judge variants (TASK-091)
Demo card = `data/script-cards.md` Card 2 "Bank Fraud Department" (7 spoken lines: 5 numbered + payment + Zelle) and the trimmed 3-line version in `pitch/script.md`. SYNTHETIC phone-quality audio (Magpie TTS, 300-3400 Hz band-pass, noise, mu-law, `detection/scripts/pstn_cards.build`), replayed through `replay_call` into a scratch P2 (:8104, local engine nemotron-nano-4b, rules + LLM, HEAD 4f094a3, private, hub dead). "Alert at" = seconds after the judge's first word. One run per variant.

| Variant | Alert at | Line that triggers it | Verdict |
|---|---|---|---|
| A verbatim, 7 lines | 19.7 s | line 3 "text with a six-digit code. Read it to me" (a hard ask, fired on the partial, before the line ended) | ok, borderline vs 20 s |
| B pitch-trimmed (3 lines, as scripted for the demo) | 7.5 s | line 1 ("move them to a safe account ... don't tell anyone at the branch") | ok |
| C fast (1.25x) | 16.3 s | line 3 code ask | ok |
| D first 2 lines then stop | NO ALERT (max s 0.15) | none | RISK, see below |
| E loose paraphrase | 17.9 s | line 4 ("put your savings into a safe account") | ok |
| F skips "don't tell branch staff" | 19.7 s | line 3 code ask (that line comes after it) | ok |
| G small talk first (3 chatty lines) | 19.8 s after the card's first word | line 3 of the card | ok; 32.5 s after the call started |
| H flat, slow, quiet (-34 dBFS, 0.9x) | 21.7 s | end of line 3 | RISK: >20 s, the code ask just takes longer to say |
| I trimmed + fast + quiet | 6.5 s | line 1 | ok |

Reading: every variant that reaches the code ask or the "move savings" line alerts; 5 s to 20 s after the first word for the full card, 6-8 s for the trimmed demo script. Judges who read the full card get the alert at the code ask (line 3), not at line 1 or 2.
Risk D: lines 1-2 ("we noticed suspicious charges ... was that you?") are word-for-word what a legitimate bank fraud call says (benign card b1 scores low). Nothing safe can alert there. If a judge stops after line 2, no alert is correct behaviour for this detector. Tell judges to read at least through line 3.
Risk H: only slow speech pushes it past 20 s; the alert point is the code ask, not detector latency (end-to-risk 2.1-2.7 s per utterance).
Prototype fix (NOT pushed): rule floor 0.60 (the "watch" band, not an alert) on "your bank / fraud team" + "suspicious/unauthorized charge". Offline text check over 160 rows (data/eval/scripts + extra_rows + heldout_v2): 0 of 74 benign rows match, 1 of 86 scam rows match, so it buys nothing on the sets and could not be scored properly (no held-out bank-notice rows). It would turn a legitimate "suspicious charge" call into a yellow band. Not recommended; full run_eval/hardneg was not run for it.
Not done: one run each, TTS voice is one voice (Mia), no real judge voices or accents, no Riva-vs-whisper split, LLM not re-run for the fix.

### TASK-095 repeat: demo card x 3 runs x 2 voices, and the final v3 bank cards
Alert = seconds after the judge's first word; HEAD b2eb56f, same method (scratch P2 :8104, local engine, hub dead). Runs differ in noise seed only (TTS audio is cached, so the range is small).

| Card | Voice | Runs (s) | Median | Fires on |
|---|---|---|---|---|
| Trimmed demo card (pitch/script.md, 3 lines) | Mia | 7.4 / 7.4 / 7.3 | 7.4 | line 1 |
| Trimmed demo card | Jason | 9.4 / 9.5 / 9.4 | 9.4 | line 1 |
| Full Card 2 verbatim (7 lines) | Mia | 19.8 / 19.7 / 19.7 | 19.7 | line 3 (code ask) |
| Full Card 2 verbatim | Jason | 21.8 / 21.7 / 21.7 | 21.7 | line 3 |
| Card 2 with the code ask moved to line 2 | Mia | 12.7 / 12.7 / 12.7 | 12.7 | line 2 (7 s earlier than the original order) |

Final judge cards `data/script-cards-v3-bank.md` (e95611f, 10 cards, 5 lines + payment step each), voice Mia, 1 run each:

| Card | Alert | Line fired | Note |
|---|---|---|---|
| 1 Safe account | 15.1 | 3 (code ask) | |
| 2 Zelle reversal | 14.5 | 3 | |
| 3 Deposit sent by mistake | **42.3** | 6 = payment step | RISK: no code/secrecy ask before payment |
| 4 New device login | 14.1 | 3 | |
| 5 Inside job | 21.5 | 5 ("move $1,800") | slightly over 20 s |
| 6 Screen share | 10.6 | 2 | |
| 7 Bounced check | 21.9 | 5 ("Pay it now") | slightly over 20 s |
| 8 Bank plus police | 17.9 | 4 | |
| 9 Pre-approved loan | **28.7** | 6 = payment step | RISK: line 5 "don't mention at the branch" did not fire |
| 10 Account verification | 16.8 | 4 | |

Range 10.6-42.3 s, median 17.4 s; every card alerts (no silent card); 3 and 9 alert only at the payment step. Suggested one-line edits (UNTESTED, card owner decides; prefer the lines that fire on other cards): card 3 line 3 -> "I'm texting you a six-digit code to freeze it, read it to me."; card 9 line 3 -> "...fee of $1,800, sent by Zelle before we release the funds, and don't tell the branch."; cards 5 and 7: add "read me the six-digit code" to line 3. Not done: 2nd voice for v3 cards (shared NVIDIA key saturated, lead said one voice), edited cards not re-run, 1 run per card.

## Not covered
- Hub fallback detector (server/fallback_detect.py) takes caller transcripts from voip/Telnyx transcription, which this private stack does not have, so drill 4 does not show it covering a dead P2 (covered by server/tests/test_fallback.py only).
- Real 429 responses from NVIDIA, real Cloudflare tunnel churn, a hub restart under a real PSTN call, a P1 relay that reconnects after P2 dies.
- Each drill ran once. The risk.update during hub downtime is dropped (only alert.fired is retried).
Reproduce: `ACC_P2_PORT=8102 .venv/bin/python detection/scripts/drills.py 1a 1b 2 3a 3b 4` (source .env, LOCAL_LLM_URL set; drill 2 waits for `:8100` active_stt_sockets==0).

## Judge bucket verification (#147), eng1: cards 6, 7, 8, 10
Frozen detector (detection/ runtime unchanged since p2-known-good-0750), local engine (llama via WSL gateway :8101, rules + LLM), scratch hub :8193 + P2 :8103 (live hub never touched). SYNTHETIC phone-quality TTS (Magpie Mia + Jason, -28 dBFS, 300-3400 Hz, mu-law), data/script-cards-v3-bank.md verbatim (6 lines each, last = payment step), 1 run per card+voice, socket guard on. "s" = seconds from the judge's first word (stream t minus the 1.0 s lead silence). Card 8 line 3 is read with its "(as the detective)" stage direction (cached TTS). A first pass without LOCAL_LLM_URL fell back to rules (card 7 did not alert) and was discarded.

| card | voice | alert | fires on (line) | s | before payment | margin s | cue / risk |
|---|---|---|---|---|---|---|---|
| 6 Screen share | Mia | yes | L2 "Download AnyDesk from the app store" | 11.5 | yes | 15.1 | remote-access ask (chip "Asks for remote access"); STT must hear "AnyDesk" |
| 6 Screen share | Jason | yes | L3 "read me the nine-digit code AnyDesk shows you" | 14.2 | yes | 14.3 | same chip, one line later (L2 not enough for Jason) |
| 7 Bounced check | Mia | yes | L5 "Pay it now and we'll keep this off your record" | 23.1 | yes | **0.6** | collections claim + counterfeit check + overdrawn; only crosses on the pay-now line |
| 7 Bounced check | Jason | yes | L5 same | 25.0 | yes | **0.8** | same |
| 8 Bank plus police | Mia | yes | L4 "move your money to a verified account today" | 19.5 | yes | 8.2 | detective impersonation + "Unverified threat"; transfer ask on L4 |
| 8 Bank plus police | Jason | yes | L4 same | 22.8 | yes | 8.1 | chip "Asks for a wire transfer" |
| 10 Account verification | Mia | yes | L4 "$1,800 verification deposit" | 18.4 | yes | 10.2 | compliance claim + one-time code + card details (L3) + deposit |
| 10 Account verification | Jason | yes | L4 same | 19.3 | yes | 11.1 | same |

Greeting-only (d) is eng2's. Findings: 8/8 alert, all before the payment line, but **card 7 is the tight one: 0.6 / 0.8 s margin, so a slower read or a missed line 5 means the alert lands with or after the Zelle line.** Latest alerts on my cards: card 7 (both voices), then card 8 Jason (22.8 s) and card 8 Mia (19.5 s).
Smallest tip for a loose read: card 7, say lines 3 and 5 exactly ("If it's not paid today, we close the account and report you for check fraud", "Pay it now") and do not skip line 4; card 6, say "AnyDesk" clearly and keep line 3 (the code ask); card 8, keep line 4 ("move your money to a verified account"); card 10, keep line 3 (account number + texted code) and line 4 (the $1,800 deposit). Paraphrase tests are eng2's pass, not mine: the cue column comes from the alert chips, not from dropping lines.
Not done: n=1 per card+voice (±1-2 s run to run, LLM latency varies), no real PSTN, no greeting-only, no dropped-cue run, no 2nd run for card 7 to measure the margin spread.

### Judge bucket verification (#147), eng2 part: demo card, greeting-only for all 9, paraphrase pass
Method: frozen detector (code = tag p2-known-good-0750, detection/ unchanged), scratch hub + P2 on my ports (8190/8102, temp hub DB, P2_ENGINE=local with llama via the WSL gateway, never the live hub), phone-quality synthetic TTS (`pstn_cards.build`: -28 dBFS, 300-3400 Hz band-pass, noise 25 dB SNR; Magpie voices Mia and Jason), one call at a time, socket guard on :8100 (the driver paused while real calls were open), driver `detection/eval/judge_verify.py`. Alert time and scores are read from the scratch P2's own log (exact), seconds are from the stream start unless "from first word" (first word = 1.0 s after stream start). n=1 run per cell, synthetic voices only.

**Demo / Judge card (trimmed 3 lines: pitch, secure line + portal, Zelle line), full call:**
| card | voice | alert | fires on | s from first word | before the Zelle (payment) line | margin | before line 2 (secure line) | max s |
|---|---|---|---|---|---|---|---|---|
| demo | Mia | yes, 8.6 s | line 1 (the pitch itself, mid-line: line 1 ends 10.2 s) | 7.6 s | yes | +12.2 s (Zelle line starts 20.8 s) | yes, +2.8 s | 1.00 |
| demo | Jason | yes, 10.6 s | line 1 (mid-line: line 1 ends 12.1 s) | 9.6 s | yes | +14.8 s (Zelle line starts 25.5 s) | yes, +2.7 s | 1.00 |

**Greeting line ALONE (first line of each card, then silence): no alert on 16 of 16 bucket greetings.**
| card | Mia max s | Jason max s |
|---|---|---|
| 1 Safe account | 0.05 | 0.05 |
| 2 Zelle reversal | 0.05 | **0.40** (watch band, below 0.80) |
| 4 New device login | 0.05 | 0.05 |
| 5 Inside job | 0.05 | 0.05 |
| 6 Screen share | 0.05 | 0.05 |
| 7 Bounced check | 0.05 | 0.05 |
| 8 Bank plus police | 0.05 | 0.05 |
| 10 Account verification | 0.05 | 0.05 |
| demo (line 1) | 0.95, ALERT 8.6 s | 0.95, ALERT 10.5 s |
The demo card is the exception by design: its "first line" is already the whole pitch (draining your account, safe account, don't tell the branch), not a greeting. Card 2 with Jason touched 0.40 on "This is Marcus with Zelle disputes... someone just sent $1,800 out" (a transfer notice reads as watch, never an alert).

**Paraphrase pass (the key cue line dropped, the rest read; Mia; the 3 latest-alerting cards from eng1's rows so far: 7 at 23.1 s, 8 at 19.5 s, 10 at 18.4 s; eng3's cards 1/2/4/5 were not available to me when I chose):**
| card | dropped line (cue) | alert | fires on | s from first word | before payment line | margin | max s | risk / smallest tip |
|---|---|---|---|---|---|---|---|---|
| 7 Bounced check | L5 "Pay it now and we'll keep this off your record." | 36.5 s | the payment step itself (line 5; the alert lands 3.3 s AFTER the Zelle line ends at 33.2 s, on the model path) | 35.5 s | **no** | -14.9 s (payment line starts 21.6 s) | 0.95 | full card had only +0.6 s margin; without "pay it now / off your record" nothing fires before the Zelle line. Tip: say "pay it now, we'll keep this off your record" (urgency + secrecy), or read the payment line without trailing off |
| 8 Bank plus police | L4 "To prove you're not involved, you need to move your money to a verified account today." | 20.3 s | line 4, the sealed-investigation line ("if you tell your bank or your family, you'll be charged too") | 19.3 s | yes | +3.1 s | 0.95 | the secrecy-under-threat line carries it; margin shrinks from +8.2 s (full) to +3.1 s. Tip: always read the "sealed investigation, don't tell your bank or family" line |
| 10 Account verification | L4 "We also need a $1,800 verification deposit. It's refunded within 24 hours." | 18.5 s | line 4, the deadline/closure line ("if we don't finish today the account is closed and your balance is mailed as a paper check") | 17.5 s | yes | +4.2 s | 0.95 | margin shrinks from +10.2 s (full) to +4.2 s. Tip: keep either the $1,800 deposit line or the "closed today" threat line |
Caveats: one run per cell, one voice for the paraphrase pass, synthetic TTS (no accents or handset noise), alert times are from the stream start (a real call adds about 0.5 s for the relay). First attempts of this driver returned empty events (hub websocket path, then a call-id regex) and were discarded; the numbers above are from the corrected run.

**#147 eng2 addendum (12:08): card 5 paraphrase.** With eng3's rows (cards 1, 2, 4, 5) the three latest-alerting cards overall are 7 (25.0 s Jason), 5 (23.2 s Jason, 21.5 s Mia) and 8 (22.8 s Jason); card 10 (19.3 s) is not in the top 3, so card 5 replaces it as the third pass (card 10's row above is kept as extra data).
| card | dropped line (cue) | alert | fires on | s from first word | before payment line | margin | max s | risk / smallest tip |
|---|---|---|---|---|---|---|---|---|
| 5 Inside job | L5 "We need you to move $1,800 so we can trace where the teller sends it." | 21.9 s | the payment step itself (line 5, 0.7 s after it starts) | 20.9 s | **no** (just after it starts) | -0.7 s (full card +4.4 s) | 0.95 | the "move $1,800 so we can trace it" line is the cue; without it the alert comes on the Zelle ask. Tip: always read the "move $1,800" line, it names the money before the payment step |

### Card 7 (Bounced check) repeat runs, eng1 (#147 follow-up)
Same setup as above (frozen detector, local engine via WSL gateway, scratch hub/P2, SYNTHETIC Magpie phone-quality audio), 3 more runs per voice at normal speed + 1 run per voice at 1.15x (speed-up of the whole line audio, so the payment line starts earlier too). "s" = seconds from first word; margin = payment-line start minus alert time. All 10 runs (incl. the first, earlier row) alert on **line 5 ("Pay it now and we'll keep this off your record")**, and none after the payment line started.

| voice | run | s | margin s |
|---|---|---|---|
| Mia | first (table above) | 23.1 | 0.63 |
| Mia | r1 | 22.9 | 0.84 |
| Mia | r2 | 23.1 | 0.57 |
| Mia | r3 | 23.3 | 0.35 |
| Mia | 1.15x | 20.3 | 1.12 |
| Jason | first | 25.0 | 0.84 |
| Jason | r1 | 24.6 | 1.27 |
| Jason | r2 | 24.3 | 1.50 |
| Jason | r3 | 24.4 | 1.45 |
| Jason | 1.15x | 22.4 | 0.87 |

Spread at normal speed: Mia margin 0.35-0.84 s (4 runs, mean 0.60), Jason 0.84-1.50 s (4 runs, mean 1.27); alert time spread 22.9-23.3 s (Mia), 24.3-25.0 s (Jason), so the alert time is stable (±0.4 s) and the margin only varies with how long the voice's line 5 + gap runs. **Smallest margin 0.35 s: it is always before the payment line but never by more than 1.5 s; one slower STT final on line 5 (finals land 0.7-2.2 s after endpoint) would push it past.** In every run the risk is 0.85 high after line 4 and crosses to the alert on line 5. Mia r2 was run before I added a paused flag to the driver (no live call was open then; its numbers match its neighbours). Not done: not a different TTS voice beyond Mia/Jason, no slower read (0.85x), no real phone line, n=4 per voice.

## Judge bucket verification (#147), cards 1, 2, 4, 5 (eng3)
Frozen detector (detection/ runtime identical to tag p2-known-good-0750; verified by diff), scratch P2 on :8104 with `P2_ENGINE=local`, `HUB_URL=http://127.0.0.1:1`, phone-quality TTS (`pstn_cards.py`, -28 dBFS, 1.0x), Mia + Jason, 1 run per card and voice. Alert time is seconds from the first word (file time minus the 1 s lead-in). Mia rows are the earlier v3 run on the same runtime code. The greeting-only check (d) is eng2's.

| Card | Voice | Alert | Alert s | Fires in | Before payment line | Margin to payment start (s) |
|---|---|---|---|---|---|---|
| 1 Safe account | Mia | yes | 15.1 | line 3, "I'm sending a six-digit code ... Read it back" | yes | 14.3 |
| 1 | Jason | yes | 17.4 | line 3 | yes | 15.6 |
| 2 Zelle reversal | Mia | yes | 14.5 | line 3, "It's not a real payment. It goes to our refunds account ..." | yes | 14.3 |
| 2 | Jason | yes | 16.1 | line 3 (engine failed over to cloud on u3, score 0.85) | yes | 16.2 |
| 4 New device login | Mia | yes | 14.1 | line 3, "I'm sending you a verification code. Read it to me" | yes | 12.1 |
| 4 | Jason | yes | 14.3 | line 3 | yes | 12.9 |
| 5 Inside job | Mia | yes | 21.5 | line 5, "We need you to move $1,800 ..." | yes | 4.4 |
| 5 | Jason | yes | 23.2 | line 5 | yes | 4.3 |

Risk / tip (e): cards 1 and 4 depend on the code ask ("six-digit code / verification code, read it back"); card 2 on "not a real payment, goes to our refunds account"; all three fire at the end of line 3, 12-16 s before the payment step. Card 5 is the thin one: line 4 ("Don't talk to anyone at the branch") scores 0.05 to 0.85 and the alert needs line 5 (the $1,800 move), 4 s before the payment step; a loose read that drops "move $1,800" would alert only at the payment step. Tip: have the reader say the code ask ("read me the six-digit code") in line 3 of card 5 (untested suggestion from the earlier v3 run). 1 run per cell, so a few seconds of spread between runs is normal (card 2 Jason: one local-to-cloud failover on u3).
