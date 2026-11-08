# Team Board
> Maintained by hackutd-delegator. H0 = Sat Nov 7, 12:00 CT. Decider: Ayman.
> Product: **Backfire**. Source of truth: `Finalized-Idea/BACKFIRE_MASTER_CONTEXT.md` (Part 1), then `01_ARCHITECTURE.md` §15 for demo stand-ins.
> Key times (from zeroday.hackutd.co, per our research; Kareem confirms): initial Devpost submission Sat ~23:00 · final submission Sun 12:00 · judging Sun 13:00-16:00.

## Now
| Person | Task | Done when | Started | Est. | Status |
|---|---|---|---|---|---|
| Evan | **P3 Decoy & voice** (`decoy/`): echo bot over Twilio `<Connect><Stream>` first, then persona card | `WSS /decoy/{call_id}` echoes audio on a test call (Twilio Media Streams protocol: connected/start/media/mark/stop, μ-law 8 kHz); persona card generator outputs fake values only | 22:55 (H10:55) | 90 min | In progress |
| Ayman | **Machine A: P1 Network & call control** + contract; **Machine B: P2 Detection** | A: `contracts/events.md` + `mock/events.json` by 23:15, then server + tunnel + scam line with pre-ring `<Reject>` and caller-only `inbound_track` stream. B: model IDs pinned, `POST /detect` returns typed JSON on 3 scripts | 22:55 (H10:55) | 30 + 90 min | In progress |
| Rayan | **P4b: T-Mobile command center** (`web/command-center/`) on `mock/events.json` (finish the Devpost initial submission first if it isn't in) | Command center plays the whole of `mock/events.json` as a timeline: caller transcript, risk + why chips, decoy turns, artifacts, lookups, agent trace, auto actions, Approve queue, campaign + immunity counter, denied log, Simulated / attested labels, cloud/local badge. A stranger gets it in 5 seconds | 23:05 (H11:05) | 150 min | In progress |
| Kareem | Confirm event facts, then **10 judge script cards + 30 eval rows** (`data/`) | §6 filled; `data/script-cards.md` (10 cards, each with callback number, website, wallet as ____) + `data/eval/scripts.jsonl` (10 scam, 10 look-alike, 10 adversarial) in P2's enums | 22:45 (H10:45) | 15 + 75 min | In progress |

## Up next
- Ayman A (P1): Maria's call screen (`web/customer/`, Voice JS SDK, two local beeps, Continue / Scammer Get Scammed / Hang up) → handoff swap to `/decoy` → stub: decoy-ended caller → `confirmed_scammers` (callback rejected before ring).
- Ayman B (P2): fusion + state machine (architecture §6) emitting `risk.update` / `alert.fired` → streaming speech-to-text → local Nemotron 3 Nano 4B behind `/detect engine=local` → eval table.
- Evan (P3): realtime decoy loop (speech-to-text → Nemotron Lightning persona → TTS), playbook to payment details, guardrails, voice clone (03:00 decision), extractor.
- **P4 is split (23:05):** P4a Intel = Kareem (`intel/`), P4b Command center + story = Rayan (`web/command-center/`, pitch, Devpost).
- Rayan (P4b): switch the command center from mock to live `WS /events` when Ayman's server is up → pitch v1 opening on the moment (P4 guide outcome 6) + T-Mobile booth questions (architecture §17) → claims audit → backup video at 09:00 → final Devpost 11:30.
- Kareem (P4a, from ~00:30): (1) **real lookups, never cut**: RDAP domain age/registrar, public-blockchain inflows, verified-business allowlist seed → emit `intel.lookup`; (2) from 02:00 the intel agent as a **fixed chain** (lookups → Nemotron 3 Super summarizes + proposes actions; the guide's fixed-template option), not free tool-calling; (3) policy gate in plain code: auto / Approve queue / `injection.denied`, replacing P1's blocklist stub. Nemotron questions → Evan; server/contract questions → Ayman.

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
| Command center build | Rayan | Ayman's `mock/events.json` + `contracts/events.md` (due 23:15; Rayan sketches the layout until then) | 22:45 |
| Eval row format must match detector output | Kareem | Uses the enums in master context §5 (`asks[]`: otp, card, ssn, gift_card, crypto, wire, p2p, remote_app, secrecy); Evan confirms at next check-in | 22:45 |

## Done
| Time | Person | Task | Verified (merged / on deployed URL) |
|---|---|---|---|
| 22:31 (H10:31) | Ayman | Backfire idea finalized, architecture v2, research | Pushed to `finalized-idea-backfire` (commit 7e4eea1) |

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
- 23:21 (H11:21) | **Evan has repo access** (`evan-olson31` is a collaborator on Proton-Designer/HackUTD26, verified via GitHub). Blocker cleared.
- 23:15 (H11:15) | **No sleep shifts.** The whole team works through the night (Rayan). Sleep schedule removed from the board and from the delegator's rules.
- 23:05 (H11:05) | **P4 split in two, one owner each:** Kareem = P4a Intel (`intel/`: real lookups, fixed-chain Nemotron agent, policy gate); Rayan = P4b command center + story. Not both on all of P4 (shared files, merge fights) and not one person alone (13 items incl. the pitch). Command center starts now on mock events instead of 02:00, because it's the screen judges watch. Intel agent uses a fixed chain, not free tool-calling, because it's more reliable in a live demo. Cost: Kareem's eval set stops at 30 rows (Ayman-B grows it with Claude if needed); Kareem is on backend logic, so he escalates fast (Evan for Nemotron, Ayman for the server). Fallback: if lookups aren't on screen by 03:00, Rayan pairs on them and the agent becomes proposals from a template. Ayman (Decider) can override.
- 23:00 (H11:00) | Team talks to the delegator through the Discord bot (`@Delegation_Bot done/blocked/next/...`). Only the bot edits BOARD.md, to avoid merge conflicts. Bot runs on Rayan's laptop.
- 22:55 (H10:55) | **Lanes reassigned by Ayman (Decider):** Ayman runs P1 Network & call control (machine A) and P2 Detection (machine B) in two Claude sessions; Evan runs P3 Decoy & voice; P4 Intel + command center + story starts later (by 02:00, owner TBD). Overrides the 22:45 lane split. Cost: Ayman carries Decider + integrator + two lanes; P4 starts late. Fallback: P1 ships a stub that adds decoy-ended callers to `confirmed_scammers`, so "callback rejected before ring" works without P4; real lookups are P4's first task at 02:00.
- 22:45 (H10:45) | Lanes set by the team: Evan owns everything Nemotron + the VoIP app; Ayman owns the product workflow starting from the local server. This overrides the delegator default (Evan as integrator): **Ayman owns the shared event contract and merges**, because his server is the hub every screen reads from. Cost: Ayman carries both Decider and integrator load. Fallback: Evan takes merges if Ayman is stuck past 30 min.
- 22:45 (H10:45) | Schedule compressed because the idea was locked at H10:30: feature freeze 05:00, code freeze 08:00, rehearsals from 09:00. Cost: about 6 hours of build time for the full path. Fallback: cut order below.
- 22:45 (H10:45) | Cut order if behind (first to go first): (1) voice clone → synthetic voice; (2) live local-4B toggle → offline cloud-vs-local accuracy table on the eval set; (3) Twilio coaching beeps → app plays beeps locally; (4) analyst network-wide actions → show proposed + one approve click on mock data. Never cut: judge calls the scam line, alert + Scammer Get Scammed, real lookups, callback rejected before ring.
