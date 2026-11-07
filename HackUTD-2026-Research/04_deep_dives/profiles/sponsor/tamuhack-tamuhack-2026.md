# TAMUhack — TAMUhack 2026 (1 projects)

### Drift
*TAMUhack TAMUhack 2026 · dataset: sponsor · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** Winner Capital One Challenge

**What it is:** A financial planning tool that runs 100,000 Monte Carlo simulations to give the probability of reaching a goal. Users connect a Nessie bank account, type a goal in plain English, and get success odds, percentiles, what-if scenarios and optional voice narration.
**Problem / user:** Young adults nearing full-time work who want a real forecast instead of plugging fixed numbers into a calculator.

**Features**
- Nessie account ingestion — Pulls customer profile, accounts and transactions from Capital One Nessie. *[claimed]*
- Natural-language goal parsing — Gemini converts a sentence like saving a sum for a house in three years into model parameters. *[claimed]*
- Monte Carlo engine — Python NumPy vectorized simulation across CPU cores models income variance, spending volatility, returns, emergencies, inflation. *[shown_working]*
- Probability and percentile results — Dashboard with Recharts shows success probability and outcome percentiles. *[claimed]*
- Sensitivity and what-if scenarios — Re-runs simulation with changed inputs to suggest levers. *[claimed]*
- Voice narration — ElevenLabs reads results aloud for accessibility. *[claimed]*

**Flow:** Land on the landing page → Connect or enter bank data via Nessie → Type a goal in plain English → Gemini parses it and the simulation runs → View probabilities, percentiles and what-ifs on the dashboard → Listen to narrated results

**Prompt:** Open-ended fintech track: payments, smarter shopping or easier consumer financial tools; intentionally vague.
**Fit (implied):** Consumer planning tool built on Nessie banking data that converts goals into probability forecasts; the page does not name the prize it targeted.  *(targeted: Capital One Challenge)*
**Sponsor tools:** Capital One Nessie API (Customer profile and transaction data feeding simulations, core)
**AI:** Gemini parses natural-language goals; ElevenLabs speaks results; the core forecast is a numeric Monte Carlo simulation, not an ML model.
**Architecture:** Turborepo monorepo: Next.js frontend with Three.js, Express API calling Nessie and Gemini, and a Python simulation service using NumPy multiprocessing.
**Novelty:** Probabilistic distributions instead of point estimates, with a claimed 100k runs in about half a second.
**Scope:** large · working: About 17k LOC, tests, seeding scripts and docs; no live demo or video. · polish: Clear README, architecture diagram on Devpost, DeepWiki docs site.
**Claims:** 100,000 simulations in about 500 ms
**Gaps:** No video or demo; Model accuracy not validated by team
Sources: https://devpost.com/software/pff, https://github.com/aadit2805/drift

---

