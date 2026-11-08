# P4a handoff (read first if you are the P4a Claude Code session)

Owner: Kareem. Pipeline id: P4a. Folder: `intel/` only. Branch: `finalized-idea-backfire`.

## Read, in order
1. `Finalized-Idea/pipelines/00_SHARED_RULES.md` (non-negotiables, contract, checkpoints)
2. `Finalized-Idea/pipelines/P4_INTEL_STORY.md` (outcomes 1-4 are ours; acceptance checklist at bottom)
3. `Finalized-Idea/01_ARCHITECTURE.md` §5 (agents + trust boundaries), §10 (intel data model, enforcement table, anti-poisoning), §15 (demo build)
4. `Finalized-Idea/BACKFIRE_MASTER_CONTEXT.md` Part 1 (10-min briefing; §7 is the 90-second demo)
5. `AGENT_COMMS_SETUP.md` (how to message other pipelines)
6. `intel/README.md`, `intel/DECISIONS.md`
7. Deep research notes (outside the repo, read as needed): `~/Desktop/HackUTD/research-notes/` — `00-MASTER_SYNTHESIS.md` first; `10-fraud-analytics-prevention.md` (signal fusion, graph/campaign linking, cost-asymmetric thresholds), `12-adversarial-ai-attacks.md` + `17-research-05-08.md` (prompt injection, lethal trifecta, OWASP Agentic Top 10), `11-ai-engineering-huyen.md` + `14-llms-prompt-engineering.md` (agent design, strict JSON, fallbacks), `21`/`22`/`23` (what wins HackUTD: shown-working beats claimed, visible trace, name your weak point).

## Done (pushed)
- Task 1: `data/script-cards.md` (10 judge cards, ____ blanks for callback/site/wallet) + `data/eval/scripts.jsonl` (30 rows, validated by `data/eval/validate.py`).
- Task 2 (never cut): `intel/lookups.py` real RDAP, BTC (blockstream) + ETH (blockscout) explorers, seeded allowlist (`intel/allowlist.json`); verified live on Kareem's Mac.
- Task 3 (built early, offline-tested, 17/17 tests): `store.py` (SQLite + `is_blocked`), `campaigns.py` (strong-indicator linking; calling number alone never merges), `agent.py` (fixed chain: lookups -> one Nemotron 3 Super call on typed artifacts only -> proposals; deterministic fallback), `gate.py` (auto / queued-for-Approve simulated / denied + allowlist poisoning), `api.py` (FastAPI router), `demo_run.py`, `test_agent_gate.py`.

## Next
1. `python -m intel.demo_run --live` — first real Nemotron call. If engine shows fallback, fix model ID from `contracts/models.md` (env `INTEL_MODEL`).
2. Commit Task 3; `bash scripts/comms/status 3 "..."`.
3. Integrate with P1 (Ayman): he mounts `intel.api.router`, calls `intel.api.configure(emit=<bus publish>)`, sends `calling_number` in `/intel/ingest`, routing calls `intel.store.is_blocked()` / `GET /intel/blocked`. Retires P1's 1.7 stub.
4. Seam with P3 (Evan): extractor emits `{type:"instruction_to_ai", text, target}` for AI-directed instructions -> gate -> `injection.denied`.
5. Seam with P4b (Rayan): command center renders intel.plan / intel.lookup / intel.agent / intel.proposals / intel.action / injection.denied / campaign.updated / blocklist.updated; Approve -> `POST /intel/actions/{id}/approve`.
6. Pick demo domain + wallet (team-controlled; fresh domain so RDAP shows "registered today"). Fill script-card blanks with Ayman.
7. Run the P4 acceptance checklist live on the shared server; report results.

## Rules that bite
- Agent never reads raw transcripts. Untrusted extracted values = lookup args only, never action targets without corroboration + analyst approval.
- Only public lookups; never contact scammer infrastructure. Label simulated actions. Fail open.
- Only edit `intel/`. Only P1 edits `contracts/`. Only the Discord bot edits `BOARD.md`. Never commit `.env`.
- Stuck 30 min: Nemotron -> Evan (P3), server/contract -> Ayman (P1).
