# DEV analysis (dev worktree `HackUTD26-dev`, branch `finalized-idea-backfire`)

Written by the dev (Fable) session for the P1 lead. Live demo folder was only READ (`logs/`). Nothing here is on `demo-stable` until the lead promotes it.

## Status
| time | task | commits | tests |
|---|---|---|---|
| 10:22 | baseline of the dev worktree | — | server 116 pass, decoy 32 pass, intel 44 pass, e2e 49 pass |
| 10:48 | **Task 2 done: `/listen` 403 reconnect loop** (root cause below, risk 5) | `f827838` pushed to `finalized-idea-backfire` | server **117** pass (new test), decoy 32, intel 44, e2e **50** pass (new check) |
| 10:50 | **Task 1 done: this report** | — | — |
| | Task 3 (UI round-3 safe items): in progress | | |

## Top 10 remaining risks for the judged demo (ranked)

### 1. Silent customer: the caller hears nothing from the customer before Fire Back (2 of the last 6 live calls)
**Evidence** (`logs/hub.log`): `talk eb66fef0 closed: msgs_sent=0`, `talk aecc22f2 closed: msgs_sent=0`; every `inrms` line of both calls shows `maria_out=0`. In the same calls the page's own `talk <id> diag` reports `mic: on, state: open, gate: open, rms 0.08-0.31 (floor 0.006), ctx: running, track live/false/true`, but the `frames` counter never moves (`5087` and `1408` for the whole call) and `rms` repeats the same value: `onaudioprocess` stopped firing (frozen ScriptProcessorNode) while every state flag looked healthy. In both broken calls `frames` started non-zero, i.e. the page had done an earlier call without a reload; in the three good calls it started at 0 or kept rising (`83ea9b14` 0 -> 583 = msgs_sent 583). The watchdog commit `cda6bab` (09:47) targets exactly this, but the 09:54 call still ran the old JS (its diag has no `audioAge`/`wd` fields), so **the watchdog is unproven on a phone**.
**Fix:** (a) demo-day rule: reload the customer page (or kill and reopen the PWA) before each judged call so the watchdog JS is loaded and the audio graph is fresh. (b) Code (dev, customer app only, needs one on-phone check): one shared `AudioContext` for beeps, decoy playback and the mic (today app.js, sim.js, talk.js and ui.js each create their own; iOS Safari caps concurrent contexts and a ScriptProcessor on one context is known to stall when another is created or interrupted), and an `AudioWorklet` capture node instead of the deprecated `ScriptProcessorNode`. (c) Hub-side backstop (call flow, needs lead OK): when `/talk` is accepted but no frames arrive for 3 s while the diag says the gate is open, publish a `talk.stalled` event so the page shows "Tap the mic button" at once.

### 2. iOS audio interruption mid-call
**Evidence:** `talk aecc22f2 diag ... "ctx": "interrupted", "track": "live/true/true"` at 09:54:58 (track muted = true). Two `interrupted` samples in the log. An interrupted context silences beeps, decoy listen-in and the mic until a gesture.
**Fix:** on `visibilitychange`/`focus` and in the watchdog, `resume()` every context (today only `st.ctx` in app.js is resumed on visibility) and show the "Tap to turn on call sounds" banner when a context stays non-running. Part of the shared-context work in risk 1b.

### 3. Decoy STT has no working fallback on the live machine
**Evidence** (`logs/decoy.log`): 17x `Exception in thread Thread-1 (_load_fb) ... ModuleNotFoundError: No module named 'faster_whisper'` (one per call). Riva works with 3 NVIDIA keys, but if the shared quota 429s, the decoy hears nothing. `faster-whisper` is in `detection/requirements.txt`, not in `decoy/requirements.txt`; the dev `decoy/.venv` lacks it too.
**Fix:** `decoy/.venv/bin/pip install faster-whisper` on the live machine between calls (no restart needed: the thread retries each call) and add it to `decoy/requirements.txt`. Lead decision: install is a live-machine action.

### 4. Decoy latency spikes: one ~3-4 s turn per call
**Evidence:** `chat: primary model slow (> 2.5 s), using fallback` + `llm=3435ms total=4490ms` (4ad7e15e 09:24) and `llm=3096ms total=4052ms` (aecc22f2 09:55); all other turns 1.3-2.0 s. The hedge (`476d4a0`, super-vl kept until 3.5 s, bolt started at 1.8 s) went live at 10:00, after both calls: **unproven live**. A 4 s gap after "send it to..." is where a judge decides the decoy is a bot.
**Fix:** keep the hedge; add a filler ("Hold on, let me write that down") spoken at 1.8 s when the primary has not answered, so the line is never silent > 2 s (decoy logic: needs lead OK, Evan's domain).

### 5. (fixed in `f827838`) `/listen` 403 loop
**Root cause:** not a reconnect of the paired phone. Any extra `/app/` page (unpaired spectator: 21 loads of `/app/` from the campus IP) receives every event over the public `/events`, rings on `call.incoming`, never answers, and at `handoff.started` sim.js calls `decoyStart` with no device token -> hub closes before accept (uvicorn prints `403 Forbidden`) -> browser sees close 1006 -> sim.js retried with 0.5/1/2/4/4/4 s backoff: exactly the 7 lines per handoff seen for 83ea9b14 and aecc22f2. The phone's own socket stayed open the whole call. Harmless to audio, but it hid real problems in the log.
**Fix shipped:** remote page without a token never opens `/listen`; a refused handshake gets one retry, not six; hub logs the refusal reason. Tests added (server + e2e).

### 6. Bank hold not yet seen on a real call: Zelle line must be captured exactly
**Evidence:** the hold fires only when a `payment_handle` artifact canonicalizes to `zelle:refunds.dept@backfire-demo.example` (`intel/nessie.py match_destinations`). Live hauls so far: `domain, gift_card_brand, payment_handle:paypal` (4ad7e15e), `gift_card_brand` (aecc22f2): no Zelle handle. `canon_handle` handles "dot/at/dash/department", but STT variants I tested fail: "refunds department at backfire demo dot example" -> `backfiredemo.example` (dash dropped), "refund stepped at..." (STT) -> no match.
**Fix:** scammer reads the card slowly, says "dash" and "dot" explicitly, repeats once. Code (intel, needs lead OK): compare the domain with dashes/dots removed and accept a local part within 2 edits of the payee's (`refunds.dept`), so "backfiredemo" and "refund stepped" still hold the $1,800.

### 7. Telnyx webhooks rejected: `POST /telnyx/webhook 403 Forbidden` from the campus IP
**Evidence:** 6 lines, each right after `GET /healthz` + `GET /demo/status` from the same IP (`129.110.242.17`): a periodic probe (ready_check/preflight?) posting to the webhook without a valid signature, not Telnyx (Telnyx webhooks come from `192.76.120.130` and return 200). Harmless now, but noise next to real failures, and if that probe is P2's monitor it will also fail the day the signature check matters.
**Fix:** find the prober (`grep -rn "telnyx/webhook" scripts detection`) and make it use `/healthz` only.

### 8. Pre-alert window: detection fires at 9-19 s, the judge may already be past line 1
**Evidence** (`logs/calls/*.jsonl`): alert at +9.1 s (83ea9b14, aecc22f2), +13.6 s (4ad7e15e), +19.1 s (eb66fef0, first transcript only at +16.9 s: the caller started late). If the judge reads all three lines quickly, the Zelle line (which drives the hold) may be spoken before Fire Back, and the decoy never hears it.
**Fix:** judge card already says "say the Zelle line last"; the customer should tap Fire Back on the first alert. Hub option (needs lead OK): feed the pre-handoff transcript's Zelle handle to the extractor (decoy already gets pre-handoff context lines; make the extractor run on them too).

### 9. Customer page state carried across calls (no reload)
**Evidence:** `frames` counters starting at 408/1068/5087/715/1408 show the page lived through several calls. Besides risk 1, stale state showed up before (07:45 handoff-screen bug, fixed) and the `/listen` spectator loop.
**Fix:** reload before each judged call (runbook line), and in code reset `BF.talkStats.frames` and sim stats on `call.incoming` so the diag is per call.

### 10. UI tells (round-3 skipped items) that a judge sees in the first 10 s
**Evidence:** `FEEDBACK.md` round 3: five competing hues (pink Fire Back, green, red, amber, white), Live Guard as a button instead of a switch, landscape alert buttons below the fold, root font-size pinned at 16 px, Inter from Google Fonts (third-party request from a privacy app, flash of fallback font on venue Wi-Fi).
**Fix:** task 3 (safe subset: one primary color, Live Guard switch, landscape alert fit); self-hosted Inter and root font-size 100 % as follow-ups; no transitions/fades (risk of iOS repaint bugs on demo day).

## Task 4 candidates (low risk, high value; waiting for the lead's OK)
1. **Risk 1b**: shared AudioContext + AudioWorklet mic in the customer app (customer app only, but touches the live audio path: needs one on-phone test before promotion).
2. **Risk 6**: tolerant Zelle handle match in `intel/nessie.py` (dash/dot-insensitive domain, 2-edit local part) with tests on the STT variants above.
3. **Risk 3**: add `faster-whisper` to `decoy/requirements.txt` (install on the live machine is the lead's call).
4. **Risk 7**: find and fix the webhook prober.
5. **Risk 9**: per-call reset of diag counters (talk.js/sim.js).
