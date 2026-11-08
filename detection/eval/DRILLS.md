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
