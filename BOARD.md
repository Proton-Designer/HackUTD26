# Team Board
> Maintained by hackutd-delegator. H0 = Sat Nov 7, 13:00 CT (Rayan confirmed at 00:12. Entries before 00:12 used H0 = 12:00, so their H-hours are 1 h too high). Decider: Ayman.
> Product: **Backfire**. Source of truth: `Finalized-Idea/BACKFIRE_MASTER_CONTEXT.md` (Part 1), then `01_ARCHITECTURE.md` §15 for demo stand-ins.
> Key times (Kareem, from zeroday.hackutd.co, 00:16): final submission Sun 12:00 · judging Sun 13:00-16:00 in ECSW/ECSS · closing 17:00 in ATEC. Info desk (Kareem, 00:24): ~4 min per judge visit, one round, no finalist round, judged in a big lecture hall (no table number yet).

## Now
| Person | Task | Done when | Started | Est. | Status |
|---|---|---|---|---|---|
| Evan | **P3 Decoy & voice** (`decoy/`): echo bot over Twilio `<Connect><Stream>` first, then persona card | `WSS /decoy/{call_id}` echoes audio on a test call (Twilio Media Streams protocol: connected/start/media/mark/stop, μ-law 8 kHz); persona card generator outputs fake values only | 22:55 (H10:55) | 90 min | In progress |
| Ayman | **Machine A: P1 Network & call control** + contract; **Machine B: P2 Detection** | A: `contracts/events.md` + `mock/events.json` by 23:15, then server + tunnel + scam line with pre-ring `<Reject>` and caller-only `inbound_track` stream. B: model IDs pinned, `POST /detect` returns typed JSON on 3 scripts | 22:55 (H10:55) | 30 + 90 min | In progress |
| Rayan | **P4b: T-Mobile command center** (`web/command-center/`) on `mock/events.json` (finish the Devpost initial submission first if it isn't in) | Command center plays the whole of `mock/events.json` as a timeline: caller transcript, risk + why chips, decoy turns, artifacts, lookups, agent trace, auto actions, Approve queue, campaign + immunity counter, denied log, Simulated / attested labels, cloud/local badge. A stranger gets it in 5 seconds | 23:05 (H11:05) | 150 min | In progress |
| Kareem | **Venue check in ECSW/ECSS + log info-desk answers in §6** | §6 has the 5 info-desk answers (committed). In the ECSW/ECSS lecture-hall area: signal bars (2 carriers if possible), a normal phone call to a teammate stays up for 2 min without dropping, venue Wi-Fi speed-test number. Posted in #15 | 00:24 (H11:24) | 30 min | In progress |

## Up next
- Ayman A (P1): Maria's call screen (`web/customer/`, Voice JS SDK, two local beeps, Continue / Scammer Get Scammed / Hang up) → handoff swap to `/decoy` → stub: decoy-ended caller → `confirmed_scammers` (callback rejected before ring).
- Ayman B (P2): fusion + state machine (architecture §6) emitting `risk.update` / `alert.fired` → streaming speech-to-text → local Nemotron 3 Nano 4B behind `/detect engine=local` → eval table.
- Evan (P3): realtime decoy loop (speech-to-text → Nemotron Lightning persona → TTS), playbook to payment details, guardrails, voice clone (03:00 decision), extractor.
- **P4 is split (23:05):** P4a Intel = Kareem (`intel/`), P4b Command center + story = Rayan (`web/command-center/`, pitch, Devpost).
- Rayan (P4b): switch the command center from mock to live `WS /events` when Ayman's server is up → pitch v1 opening on the moment (P4 guide outcome 6) + T-Mobile booth questions (architecture §17) → claims audit → backup video at 09:00 → final Devpost 11:30.
- Ayman A (P1), 10 min, **by 01:00** (moved up 00:08, unblocks Kareem): pull `finalized-idea-backfire` through 867ff7c, add `NVIDIA_API_KEY` to the hub's `.env` (Kareem DMs his tested key), restart the hub, ping Kareem "hub restarted" in thread #15. Kareem runs the acceptance, not Ayman.
- Kareem (after venue check, ~00:55): when Ayman pings "hub restarted" (by 01:00): `python -m intel.acceptance` against the shared hub, post pass count in #15 → be the 02:00 thin-slice test caller reading a card. Stuck: Ayman, then Evan.

## Owned files and folders
(Updated 22:55 per Ayman. One owner per folder. Plan: `Finalized-Idea/07_EXECUTION_PLAN.md`.)
- Ayman, machine A (P1): `contracts/`, `mock/`, `server/`, `voip/`, `web/customer/`, merges
- Ayman, machine B (P2): `detection/`, `contracts/models.md`
- Evan (P3): `decoy/`
- Kareem (P4a Intel): `intel/`, `data/` (script cards, eval set), `HackUTD-2026-Kit/CLAUDE.md` §6
- Rayan (P4b Command center + story): `web/command-center/`, Devpost text, pitch, backup video

## Blocked
| What | Who is stuck | Waiting on | Since |
|---|---|---|---|
| **Telnyx outbound/termination disabled** on the trial account (balance -0.03; `voip/LIVE_TEST_PLAN.md` §4, checks 6-12 open). Blocks Maria dial, handoff, callback rejection, the 02:00 thin slice and the judge-calls-the-line demo | Ayman (P1), whole demo path | **Ayman decides who pays by 00:40**; account owner tops up + upgrades off trial by 01:00 | 00:15 (H11:15) |
| ~~Command center build~~ CLEARED 00:12 (H11:12): `contracts/events.md` + `mock/events.json` are in git (1572539), and command center commit d248634 is in too | Rayan | (none) | 22:45 |
| P4a acceptance on the shared hub (not his current task) | Kareem | Ayman: pull 867ff7c + `NVIDIA_API_KEY` in hub `.env` + restart, by 01:00. Table question answered: `/routing/lookup` reads hub SQLite `confirmed_scammers` → `campaign_numbers` → `intel.store.is_blocked()` (trusted overrides intel only) → `trusted` (`server/routing.py`). Evan #16 / Rayan #17 are demo moments, not blockers for the acceptance run | 00:07 |
| Eval row format must match detector output | Kareem | Uses the enums in master context §5 (`asks[]`: otp, card, ssn, gift_card, crypto, wire, p2p, remote_app, secrecy); Evan confirms at next check-in | 22:45 |

## Done
| Time | Person | Task | Verified (merged / on deployed URL) |
|---|---|---|---|
| 22:31 (H10:31) | Ayman | Backfire idea finalized, architecture v2, research | Pushed to `finalized-idea-backfire` (commit 7e4eea1) |
| 00:07 (H12:07) | Kareem | Script cards (10) + eval set (`data/`) | Files in repo; not separately checked |
| 00:07 (H12:07) | Kareem | P4a Tasks 1-3: real lookups (RDAP, BTC/ETH explorers, allowlist), Nemotron intel agent (fixed chain, live), policy gate (auto / Approve / denied; allowlist = poisoning), `intel.seed_demo` reset | Pushed through 867ff7c (git verified). Hub code imports intel (e641ec0, `server/routing.py`), but the **running** hub hasn't pulled it yet. P4 acceptance 7/7 locally, fail-open drill passed (reported) |
| 00:15 (H11:15) | Kareem | Script-card payment blanks filled from `intel/demo_config.json` | Git verified (8514536); no `____` left on any card. The card → `intel.acceptance` check is still open and runs once the hub is restarted |
| 00:24 (H11:24) | Kareem | Info desk answers: ~4 min per judge visit; one round, no finalists; big lecture hall, no table number yet; live calls "should work" in ECSW/ECSS (untested by us); no sponsor/MLH phone credits, so we pay for Telnyx | Reported in chat (not a code task) |
| 00:18 (H11:18) | Kareem | `HackUTD-2026-Kit/CLAUDE.md` §6 filled (deadlines, judging window, tracks) | Git verified (15555c9) |
| 00:15 (H11:15) | Kareem | `data/RESET.md` reset sequence, timed twice (0.15 s / 0.12 s) | Git verified (38e6312). Times are local; re-time against the shared hub at the 02:00 slice |

## Checkpoints (compressed: idea locked at H10:30)
- **23:00** Devpost initial submission in (Rayan).
- **23:15** Contract + mock events committed (Ayman).
- **00:30 (H12:30)** Each integration returned one real response: Twilio caller stream, Nemotron typed JSON, one RDAP lookup. Anything that hasn't gets dropped or mocked unless it is core.
- **02:00 (H14)** Thin slice end to end: call the scam line → caller transcript → detector → two beeps + buttons → event shows on the command center. Else cut to the path that runs.
- **03:00 (H15)** Voice-clone call: if the clone isn't working, the decoy uses a synthetic voice (allowed by our locked decisions; label it).
- **05:00 (H17)** Full demo path: handoff → decoy → artifacts → real lookups → auto block → judge calls back and is rejected before it rings. Feature freeze.
- **08:00 (H20)** Code, prompts and models frozen; demo-visible bugs only.
- **09:00 (H21)** Demo setup frozen; 5+ timed rehearsals from reset.
- **11:30 (H23:30)** Final Devpost submitted (hard deadline 12:00).

## Decisions log
- 00:24 (H11:24) | **Info-desk facts change two things.** (1) ~4 min per judge, one round, no finalists, so every visit counts as the final. Pitch + demo must fit in ~3:00 with ~1 min left for questions, and the scripted path has to work on the first try from reset. Rayan writes pitch v1 to 3:00. (2) No free credits, so the 00:18 "fund Telnyx" recommendation stands. Ayman's 00:40 call is now just "pay" or "go phone-free". Nobody has tested live calls in the lecture hall yet, so Kareem checks signal and Wi-Fi there now. The 01:30 fallback (hub replays a recording as the caller) stays as the backup.
- 00:18 (H11:18) | **Fund Telnyx now (delegator recommendation; Ayman decides by 00:40).** Top up the existing Telnyx account and upgrade it off trial (smallest amount the portal allows: $____), cost split 4 ways. Not a fresh backup account: the app/connection IDs and the Maria-dial fix are already verified there, and a new account means redoing that setup. Why: "judge calls the scam line" and "callback rejected before ring" are on the never-cut list, and both need a working call path. Cost: a few dollars + ~20 min of Ayman's time. Fallback if calls aren't working by 01:30: the 02:00 slice runs with the hub replaying a script-card recording as the caller (no phone), and the live-call demo is re-decided at 03:00. Still unknown: whether inbound calls work right now; Ayman checks with one call.
- 00:18 (H11:18) | Notes: board text calling P3 "Twilio" is stale. The provider has been Telnyx since 22:59 (`01_ARCHITECTURE.md` mapping table). §6 now says H0 = 12:00 (Kareem, from the site) and the board says 13:00 (Rayan). Rayan still decides; no checkpoint moves.
- 00:16 (H11:16) | **H0 conflict reopened, with a source:** Kareem reads zeroday.hackutd.co as "Hacking Starts 12:00pm", but Rayan confirmed 13:00 at 00:12. Board labels stay at 13:00 until Rayan checks the site and settles it. Nothing moves either way because every checkpoint is a clock time. Also open: the 23:00 initial Devpost checkpoint isn't marked done. Rayan confirms it's in with all 4 teammates.
- 00:12 (H11:12) | **H0 = 13:00 (Rayan confirmed).** This settles the 00:07 mismatch. No checkpoint moves because they are all clock times. Old entries keep their labels so history isn't rewritten. New entries use H0 = 13:00.
- 00:08 (H12:08) | **Kareem keeps building while the shared-hub acceptance waits.** It needs only Ayman's 10-min pull + key + restart (moved up to 01:00), not Evan's `instruction_to_ai` (#16) or Rayan's agent-trace panel (#17); those two land with their own lanes and get checked in the 02:00 thin slice. Evan stays on the P3 echo bot, Rayan on the command center. Cost: shared-hub acceptance slips to ~01:00. Fallback: if the hub isn't restarted by 01:15, Kareem's local 7/7 counts for now and Ayman restarts it as step 1 of the 02:00 slice.
- 00:07 (H12:07) | **Intel model = `nemotron-3.5-super-vl-120b-a12b`**: `3-super-120b` returns 404 on our keys (Kareem, tested live). Ayman-B records it in `contracts/models.md`. Fallback: fail-open stays in, so lookups and blocks still show if the model call fails.
- 00:07 (H12:07) | **H0 mismatch:** board says 12:00, bot header says 13:00. Board stays at 12:00 (every timestamp uses it) until Rayan confirms; checkpoints use clock times, so they don't move.
- 23:21 (H11:21) | **Evan has repo access** (`evan-olson31` is a collaborator on Proton-Designer/HackUTD26, verified via GitHub). Blocker cleared.
- 23:15 (H11:15) | **No sleep shifts.** The whole team works through the night (Rayan). Sleep schedule removed from the board and from the delegator's rules.
- 23:05 (H11:05) | **P4 split in two, one owner each:** Kareem = P4a Intel (`intel/`: real lookups, fixed-chain Nemotron agent, policy gate); Rayan = P4b command center + story. Not both on all of P4 (shared files, merge fights) and not one person alone (13 items incl. the pitch). Command center starts now on mock events instead of 02:00, because it's the screen judges watch. Intel agent uses a fixed chain, not free tool-calling, because it's more reliable in a live demo. Cost: Kareem's eval set stops at 30 rows (Ayman-B grows it with Claude if needed); Kareem is on backend logic, so he escalates fast (Evan for Nemotron, Ayman for the server). Fallback: if lookups aren't on screen by 03:00, Rayan pairs on them and the agent becomes proposals from a template. Ayman (Decider) can override.
- 23:00 (H11:00) | Team talks to the delegator through the Discord bot (`@Delegation_Bot done/blocked/next/...`). Only the bot edits BOARD.md, to avoid merge conflicts. Bot runs on Rayan's laptop.
- 22:55 (H10:55) | **Lanes reassigned by Ayman (Decider):** Ayman runs P1 Network & call control (machine A) and P2 Detection (machine B) in two Claude sessions; Evan runs P3 Decoy & voice; P4 Intel + command center + story starts later (by 02:00, owner TBD). Overrides the 22:45 lane split. Cost: Ayman carries Decider + integrator + two lanes; P4 starts late. Fallback: P1 ships a stub that adds decoy-ended callers to `confirmed_scammers`, so "callback rejected before ring" works without P4; real lookups are P4's first task at 02:00.
- 22:45 (H10:45) | Lanes set by the team: Evan owns everything Nemotron + the VoIP app; Ayman owns the product workflow starting from the local server. This overrides the delegator default (Evan as integrator): **Ayman owns the shared event contract and merges**, because his server is the hub every screen reads from. Cost: Ayman carries both Decider and integrator load. Fallback: Evan takes merges if Ayman is stuck past 30 min.
- 22:45 (H10:45) | Schedule compressed because the idea was locked at H10:30: feature freeze 05:00, code freeze 08:00, rehearsals from 09:00. Cost: about 6 hours of build time for the full path. Fallback: cut order below.
- 22:45 (H10:45) | Cut order if behind (first to go first): (1) voice clone → synthetic voice; (2) live local-4B toggle → offline cloud-vs-local accuracy table on the eval set; (3) Twilio coaching beeps → app plays beeps locally; (4) analyst network-wide actions → show proposed + one approve click on mock data. Never cut: judge calls the scam line, alert + Scammer Get Scammed, real lookups, callback rejected before ring.
