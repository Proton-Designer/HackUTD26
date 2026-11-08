# Team Board
> Maintained by hackutd-delegator. H0 = Sat Nov 7, 12:00 CT. Decider: Ayman.
> Product: **Backfire**. Source of truth: `Finalized-Idea/BACKFIRE_MASTER_CONTEXT.md` (Part 1), then `01_ARCHITECTURE.md` §15 for demo stand-ins.
> Key times (from zeroday.hackutd.co, per our research; Kareem confirms): initial Devpost submission Sat ~23:00 · final submission Sun 12:00 · judging Sun 13:00-16:00.

## Now
| Person | Task | Done when | Started | Est. | Status |
|---|---|---|---|---|---|
| Evan | Twilio scam line + Nemotron detector: first real response from each | Calling the scam line streams caller-only audio (`inbound_track`) to the backend websocket, AND one script through Nemotron returns the typed detector JSON (`scam_type`, `stage`, `asks[]`, `impersonates`, `addresses_ai_system`); model IDs confirmed with `GET /v1/models` | 22:45 (H10:45) | 90 min | In progress |
| Ayman | Event contract + mock events, then local server skeleton | `contracts/events.md` + `mock/events.json` committed by 23:15 so Rayan and Kareem can build; then server runs locally behind a public tunnel that Twilio can reach, SQLite lists in place, pre-ring `<Reject>` works for one listed number | 22:45 (H10:45) | 30 + 90 min | In progress |
| Rayan | Devpost project + initial submission (urgent, ~23:00 cutoff) | Devpost project exists, all 4 invited and accepted, initial submission in | 22:45 (H10:45) | 10 min | In progress |
| Kareem | Confirm event facts | `HackUTD-2026-Kit/CLAUDE.md` §6 filled: exact Devpost cutoffs, judging window and room, minutes per judge visit, finalist round Y/N | 22:45 (H10:45) | 15 min | In progress |

## Up next
- Evan: decoy agent over Twilio `<Connect><Stream>` with a synthetic voice first (voice clone only after the synthetic voice works end to end); then the extractor → typed artifacts.
- Ayman: call state machine + policy gate as plain code, emitting the events in `contracts/events.md`; then the intel-agent tool calls (real RDAP + public-blockchain lookup) wired to `propose_action()`.
- Rayan: T-Mobile command center screen against `mock/events.json` (live caller transcript, score + why chips, campaign forming, artifacts, auto actions, analyst Approve button, immunity counter, injection `denied` log, "Simulated" labels). Then pitch script v1 + T-Mobile booth questions.
- Kareem: synthetic scripts: 10 judge script cards + first 30 eval rows; then grow the eval set toward ~150.

## Owned files and folders
(Proposed at 22:45; Ayman can rename folders when he creates the server, but keep one owner per folder.)
- Evan: `voip/` (Twilio scam line, conference, media streams, Maria's call app), `nemotron/` (detector, decoy, extractor, local 4B model)
- Ayman: `contracts/`, `mock/`, `server/` (router, state machine, policy gate, intel agent, SQLite), merges
- Rayan: `web/command-center/`, Devpost text, pitch, `HackUTD-2026-Kit/` pitch files
- Kareem: `data/` (script cards, eval set), `HackUTD-2026-Kit/CLAUDE.md` §6

## Blocked
| What | Who is stuck | Waiting on | Since |
|---|---|---|---|
| Command center build | Rayan | Ayman's `mock/events.json` (Rayan does Devpost first, so no idle time) | 22:45 |
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
- 22:45 (H10:45) | Lanes set by the team: Evan owns everything Nemotron + the VoIP app; Ayman owns the product workflow starting from the local server. This overrides the delegator default (Evan as integrator): **Ayman owns the shared event contract and merges**, because his server is the hub every screen reads from. Cost: Ayman carries both Decider and integrator load. Fallback: Evan takes merges if Ayman is stuck past 30 min.
- 22:45 (H10:45) | Schedule compressed because the idea was locked at H10:30: feature freeze 05:00, code freeze 08:00, rehearsals from 09:00. Cost: about 6 hours of build time for the full path. Fallback: cut order below.
- 22:45 (H10:45) | Cut order if behind (first to go first): (1) voice clone → synthetic voice; (2) live local-4B toggle → offline cloud-vs-local accuracy table on the eval set; (3) Twilio coaching beeps → app plays beeps locally; (4) analyst network-wide actions → show proposed + one approve click on mock data. Never cut: judge calls the scam line, alert + Scammer Get Scammed, real lookups, callback rejected before ring.

## Sleep shifts
- Kareem 01:30-03:00
- Evan 03:00-04:30
- Ayman 04:30-06:00
- Rayan 06:00-07:30
(Never both coders down at once. Nobody sleeps through a checkpoint they own.)
