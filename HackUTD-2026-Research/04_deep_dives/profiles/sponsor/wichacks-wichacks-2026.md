# WiCHacks — WiCHacks 2026 (1 projects)

### Income Firewall
*WiCHacks WiCHacks 2026 · dataset: sponsor · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** Winner Capital One: Best Financial Hack

**What it is:** A Next.js risk engine for variable-income earners that runs seasonal bootstrap Monte Carlo simulations on monthly income to estimate the chance of hitting zero, recommends what share of surplus to set aside, and backtests that policy against history.
**Problem / user:** Freelancers, creators and gig workers whose income swings widely and who need a probability-based saving rule rather than a budget tracker.

**Features**
- Bootstrap Monte Carlo — Resamples historical months, seasonally bucketed, to estimate shortfall probability over a forward horizon *[shown_working]*
- Smoothing policy recommendation — Computes target buffer, gap and percent of surplus to route into savings with a plain-English rule *[shown_working]*
- Common Random Numbers — Reuses seeds so smoothing on/off comparisons are stable *[shown_working]*
- Backtest and allocation replay — Replays history through the policy, tracking deposits, releases and buffer *[shown_working]*
- Dashboard — KPI cards and Recharts trajectory chart in dark theme *[shown_working]*
- Data inputs — CSV upload, three 60-month synthetic profiles, and Nessie sandbox deposits with cache and fallback *[shown_working]*

**Flow:** Pick Creator, Gig or Freelancer sample, CSV or Nessie → Run analysis → View volatility score and zero-balance probability → Toggle smoothing to see risk drop → Review allocation replay and backtest

**Prompt:** not public / not found
**Fit (implied):** A personal-finance risk tool for irregular income that adds a Nessie adapter as one bank-style data source.  *(targeted: Capital One Best Financial Hack)*
**Sponsor tools:** Capital One Nessie API (Optional server-side fetch of account deposits aggregated monthly, with 10-minute cache and graceful fallback, supporting)
**AI:** none
**Architecture:** Next.js front end calls /api/analyze, which normalizes income, computes features, generates a policy, simulates and backtests; adapters supply CSV, synthetic or Nessie data; deployed on Vercel.
**Novelty:** Uses statistical simulation with variance-reduction (CRN) instead of an LLM; frames income volatility as a probability problem.
**Scope:** small · working: Live Vercel demo, about 1.9k LOC, demo scenarios in README; no tests or video. · polish: Detailed README with methodology, dashboard charts; Devpost has blank sections.
**Gaps:** no WiCHacks Capital One prize text; Devpost accomplishments/next steps blank
Sources: https://devpost.com/software/income-firewall, evidence/sponsor-wichacks-wichacks-2026-income-firewall.json

---

