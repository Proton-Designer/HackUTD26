# Finalized Idea: Backfire (T-Mobile Safe Signal + NVIDIA Nemotron)

Home for everything about the idea the team is building. Last updated Nov 7, 2026, 10:30pm CT.

## In three lines
- When a scam call gets through, you hear **two beeps** and tap **Scammer Get Scammed**. T-Mobile's network silently swaps you out for an NVIDIA Nemotron decoy **speaking in your own (consented) voice**.
- The decoy keeps the scammer talking until they reveal how they get paid. Backfire then blocks them for you automatically, links them to their scam campaign, and (with one analyst click) shuts their infrastructure down for every customer.
- **Your voice is never analyzed.** Only the caller's side is, only if you opt in, inside an attested NVIDIA confidential-computing container or with a local Nemotron 4B model.

## Start here
**`BACKFIRE_MASTER_CONTEXT.md`**: one large doc with everything (a 10-minute briefing + the full text of every doc below). Give this to any teammate or AI agent first.

## Files
| File | What it is |
|---|---|
| `BACKFIRE_MASTER_CONTEXT.md` | **Everything in one file** |
| `01_ARCHITECTURE.md` | **Architecture v2 (decisions locked):** routing, components, agents and trust boundaries, state machine, call flows, sequence diagram, UX, intel model, privacy, latency, the two implementations, evaluation, demo build |
| `06_OPEN_QUESTIONS_FOR_TEAM.md` | **Decision log** (rounds 1–4) + what's still open |
| `07_EXECUTION_PLAN.md` | **Execution plan:** 4 parallel pipelines aligned to `BOARD.md` (Evan: call + AI engine · Ayman: server + intel · Rayan: command center + story · Kareem: data + eval), checkpoints to the 11:30 submission, contracts, demo path, scope sheet, architecture → step traceability |
| `02_PROBLEM_AND_POSITIONING.md` | Prompt, insight, why it's T-Mobile's problem, key numbers, persona, pitch lines |
| `03_TMOBILE_EXISTING_PROTECTIONS.md` | Everything T-Mobile already offers, what it doesn't, competitors |
| `04_PRIVACY_LEGAL_TRUST.md` | Consent, voice-clone safeguards, the decoy's legal line, trust stats |
| `05_COST_MODEL.md` | Rough cost per screened minute and at scale |
| `AGENT_CONTEXT.md` | Rules and context for AI coding agents working on this project |
| `reviews/` | Two independent Opus architecture reviews, the brief they were given, and the v1 synthesis |
| `source/` | Whiteboard v1 photo + transcription, original Backfire concept note |

## Status
- ✅ Problem, audience (older woman) and positioning locked
- ✅ Architecture v2 locked: Live Guard, auto-blocking of confirmed and campaign-linked numbers, customer-triggered decoy in a cloned voice, split enforcement, two implementations (cloud confidential computing + local 4B)
- ⏳ Open: N12 (weekly summary); verifications and booth questions (architecture §17–18)
- ✅ Execution plan: `07_EXECUTION_PLAN.md`
- ⏳ Next: Phase 0 contracts (all 4), then the 4 pipelines in parallel

## Related research
- `../Research/05_Target_Analysis/`: goal decision, top-4 audiences
- `../Research/03_Safe_Signal_Deep_Research/`: NVIDIA stack, tool APIs, detection confidence, agent security, privacy, pitch ammo
- `../Research/02_TMobile_Threats_and_Issues/`: threat map, incident and cost history, existing protections
- `../HackUTD-2026-Kit/`: judging, architecture, demo and pitch guides
- `../HackUTD-2026-Research/`: past-winner analysis
