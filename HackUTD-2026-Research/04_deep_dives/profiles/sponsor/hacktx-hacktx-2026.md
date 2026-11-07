# HackTX — HackTX 2026 (1 projects)

### BreakingPoint
*HackTX HackTX 2026 · dataset: sponsor · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** Winner [Capital One] The Best Use of Nessie

**What it is:** A financial-recovery planner for a surprise expense. Using a seeded Nessie customer, it simulates 30 days of cash flow after a car breakdown, draws a causal graph of consequences, researches local options, and ranks combined recovery plans.
**Problem / user:** People whose one unexpected cost, such as a car repair, cascades into missed shifts, lost pay and unpaid rent.

**Features**
- Nessie-seeded customer snapshot — Seeder creates a fictional customer with 90 days of transactions, payroll and bills; falls back to a labeled fixture. *[shown_working]*
- Deterministic 30-day simulator — Models shifts, paychecks, bills and repair with a ledger so later income cannot hide an earlier missed bill. *[shown_working]*
- Animated consequence graph — React Flow graph traces repair cost to lost income and bills at risk in causal order. *[shown_working]*
- Bounded research — Gemini proposes hypotheses; SerpApi fetches web, maps and transit evidence with call limits and kept source links. *[shown_working]*
- Clarifying questions — Asks high-impact yes/no/not-sure questions one at a time about remote work or rent extension. *[shown_working]*
- Ranked recovery plans — Evaluates combinations of up to three of eight actions (92 combos), each re-simulated; includes bus Route 5 fares and copyable outreach drafts. *[shown_working]*

**Flow:** Review fictional customer's finances and edit wage, quote and breakdown date → See projected cash impact and animated ripple graph → Confirm commute details and run research → Answer prioritized questions → Compare ranked plans with costs and next actions → Copy outreach drafts

**Prompt:** Build an app that uses Nessie API endpoints creatively to address a finance problem and improve users' financial lives.
**Fit (implied):** Seeds a Nessie sandbox customer with accounts, transactions, deposits and bills as the baseline for forecasting a financial shock and recovery options.  *(targeted: [Capital One] The Best Use of Nessie)*
**Sponsor tools:** Capital One Nessie API (Seeded customer, accounts, transactions, payroll and bills feeding the simulator, core)
**AI:** Gemini only extracts hypotheses and candidates from search evidence within backend validation and call limits; financial math and plan ranking are deterministic code.
**Architecture:** Next.js frontend proxies to a FastAPI backend that holds Nessie, Gemini and SerpApi keys; simulation, research and optimizer modules produce plans shown with React Flow.
**Novelty:** Deliberate separation of deterministic finance logic from LLM research, with conditional outcomes for unconfirmed approvals and no automatic actions.
**Scope:** large · working: About 12k LOC with tests, seed scripts, docs and detailed demo flow; no live demo link. · polish: Four-stage UI with accessibility notes, fixtures fallback, thorough README; no video.
**Claims:** Up to 92 action combinations evaluated and re-simulated
**Gaps:** No video or demo; No user testing
Sources: https://devpost.com/software/breakingpoint, https://github.com/MMehta45/hacktx26

---

