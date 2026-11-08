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

## Not covered
- Hub fallback detector (server/fallback_detect.py) takes caller transcripts from voip/Telnyx transcription, which this private stack does not have, so drill 4 does not show it covering a dead P2 (covered by server/tests/test_fallback.py only).
- Real 429 responses from NVIDIA, real Cloudflare tunnel churn, a hub restart under a real PSTN call, a P1 relay that reconnects after P2 dies.
- Each drill ran once. The risk.update during hub downtime is dropped (only alert.fired is retried).
Reproduce: `ACC_P2_PORT=8102 .venv/bin/python detection/scripts/drills.py 1a 1b 2 3a 3b 4` (source .env, LOCAL_LLM_URL set; drill 2 waits for `:8100` active_stt_sockets==0).
