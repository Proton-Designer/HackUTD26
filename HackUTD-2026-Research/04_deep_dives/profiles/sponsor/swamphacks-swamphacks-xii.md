# SwampHacks — SwampHacks XII (1 projects)

### Runway
*SwampHacks SwampHacks XII · dataset: sponsor · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** Winner Capital One - The Best Use of Nessie!

**What it is:** Mobile/web app that forecasts a user's checking balance 30 days out from Capital One Nessie data and, when a shortfall looms, quietly moves money from pre-consented family or friends via real sandbox transfers, repaid automatically after a verified paycheck.
**Problem / user:** People living paycheck to paycheck who face short gaps before payday and are embarrassed to ask for help.

**Features**
- 30-day balance forecast — Deterministic engine with recurring-payment detection and a calibrated cautious range; warns when balance dips. *[shown_working]*
- Quiet Support Agreements — Supporter sets a limit, recipient opts in; both must consent before support is active. *[shown_working]*
- Network Guardian — On a predicted dip, checks each supporter's own forecast, computes a safe amount and splits cover across supporters via Nessie transfers. *[shown_working]*
- Automatic repayment — Returns money after a verified paycheck without causing a new dip; early repayment allowed. *[shown_working]*
- Ask Runway — Gemini assistant with tool calling answers affordability questions; guard drops figures not traced to the engine. *[shown_working]*
- Circles — Named groups with invite links to send or request money with tags. *[claimed]*
- Privacy by design — Supporters never see balances, spending or reasons. *[claimed]*
- What-if scenarios — Tap an amount to update the forecast instantly. *[claimed]*

**Flow:** Open site and pick a demo customer → See forecast and shortfall warning → Ask a question in Ask Runway → Network Guardian covers the gap from supporters → Auto-repay after verified payday

**Prompt:** Capital One challenge: build an app that reimagines the banking experience, creatively using Nessie endpoints (accounts, merchants, bills, P2P transfers) to improve users' financial lives.
**Fit (explicit):** README states it was built for this challenge; uses 8 Nessie endpoints and every cover, repayment and send is a real sandbox transfer plus deposit.  *(targeted: Capital One - The Best Use of Nessie!)*
**Sponsor tools:** Capital One Nessie API (Source of accounts, bills, purchases, deposits and all money movement (8 endpoints), core); Auth0 (Sign-in and approvals, supporting)
**AI:** Gemini with tool calling powers Ask Runway, with a grounding guard; forecast uses conformal calibration and a formality model matches reply tone; math is deterministic, not LLM.
**Architecture:** Expo React Native client; FastAPI backend with Pydantic; TigerData/Postgres hypertables for transactions and a transfer journal; Nessie sandbox; Gemini; Auth0; Docker on Vultr with Caddy and CI deploys.
**Novelty:** Multi-party consented lending with each helper's own forecast checked; unusually rigorous evals, journaled transfers and security reviews for a hackathon.
**Scope:** large · working: Live site with demo customers, ~32k LOC, Docker, CI, tests (page cites 570+), YouTube video. · polish: Film page, evals, production deploy, read-only visitor mode, privacy and security reviews.
**Claims:** Forecast error 66% lower than bills alone ($138 vs $408) | 0 unsafe transfers across 2,000 simulated networks | 15/15 privacy attacks held | 570+ tests run on every push
**Gaps:** Screenshot count not captured; Page included an embedded edit suggestion aimed at the author, ignored
Sources: https://devpost.com/software/runway-57dpic, evidence/sponsor-swamphacks-swamphacks-xii-runway.json, sponsor_prompts_CapitalOne_StateFarm_CBRE.jsonl

---

