# VTHacks — VTHacks 14 (1 projects)

### LoadCheck
*VTHacks VTHacks 14 · dataset: sponsor · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** Winner [Capital One] Best Use of Nessie

**What it is:** Decision tool for owner-operator truck drivers. It reads a pasted or screenshot load offer with Gemini, has the driver confirm the fields, then deterministic code computes true net profit, finds better multi-load runs, and checks cash flow against Nessie sandbox bank data.
**Problem / user:** Independent truckers whose headline per-mile rate hides deadhead, fuel, truck payment, dispatcher fees and upcoming bills.

**Features**
- Offer extraction — Gemini pulls pickup, destination, rate, miles and times from pasted text or a screenshot; driver edits and approves on a confirm screen. *[claimed]*
- True-profit calculator — Python profit module includes empty miles, fuel, maintenance, fixed costs and dispatcher cut; compares advertised vs net rate. *[shown_working]*
- Counteroffer suggestion — Computes a rate that hits the driver's target profit. *[claimed]*
- Multi-load route search — Searches combinations of up to three loads over 60 simulated loads with windows and simplified hours-of-service, preferring home-to-home runs. *[shown_working]*
- Cash-flow timeline — Combines Nessie balances, bills and expenses to predict shortages and test a delivery advance. *[shown_working]*
- Plain-language explanation — Gemini explains results; its numbers are checked against the code's math. *[claimed]*

**Flow:** Paste offer or upload screenshot → Review and approve extracted fields → See true profit and counteroffer → Compare better routes → View cash-flow timeline and advance check → Read AI explanation

**Prompt:** Capital One prize for best use of its Nessie banking API at VTHacks 14; no further brief on the listing.
**Fit (explicit):** Uses seeded Nessie sandbox accounts and bills to judge whether a driver can afford a trip before payment arrives; README labels Nessie data as sandbox.  *(targeted: [Capital One] Best Use of Nessie)*
**Sponsor tools:** Capital One Nessie API (Sandbox balances, upcoming bills and advance info feeding the cash-flow simulation, core)
**AI:** Gemini only reads unstructured offers and explains finished results; all profit, route and cash numbers come from Python, and AI-stated numbers are validated against it.
**Architecture:** React/TypeScript frontend over FastAPI backend with modules profit, optimizer, cashflow, geo plus gemini and nessie adapters; seeded load board and cached city data with recorded-data fallbacks.
**Novelty:** Strict AI/math separation with a human confirm step and a niche trucking domain; repo built with parallel team-owned modules and agent prompts.
**Scope:** medium · working: ~7.8k LOC, CI, tests (page reports 100 backend tests and 15/15 demo checks), health endpoint; no live link or video. · polish: SPEC contract, labeled simulated data, truck settings screens, five screenshots.
**Claims:** 100 passing backend tests | 15 of 15 end-to-end demo checks pass | Tested on 60 simulated loads
**Gaps:** No video or live demo to confirm
Sources: https://devpost.com/software/loadcheck, evidence/sponsor-vthacks-vthacks-14-loadcheck.json, sponsor_prompts_CapitalOne_StateFarm_CBRE.jsonl

---

