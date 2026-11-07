# TAMUhack — TAMUhack 2025 (1 projects)

### PAWS - Personal Assets and Wise Saving
*TAMUhack TAMUhack 2025 · dataset: sponsor · tier: sponsor_winner · evidence A · confidence medium*
**Prizes:** Winner Capital One Challenge

**What it is:** A gamified budgeting app with a cat theme. It analyzes transactions to build a budget and savings plan, then awards points for meeting goals that can be spent on a gacha for collectible cats and a shop for cat accessories.
**Problem / user:** Young people who find money management overwhelming; app tries to build habits through game rewards.

**Features**
- Budget generation and goals — Analyzes expenses and transactions to produce a budget with per-goal detail pages. *[claimed]*
- Savings goals — Dedicated savings goal screens tied to a savings plan. *[claimed]*
- Points for completed goals — Completing goals earns points used in the game layer. *[claimed]*
- Cat gacha — Randomized draw lets users win cats using points. *[claimed]*
- Shop for cats and accessories — Points are spent on cats and accessories. *[claimed]*
- Monthly recap — Recap view with a budget tab summarizing the month. *[claimed]*
- Capital One API data — Capital One API hosts users' savings and transactions. *[claimed]*

**Flow:** Home page → Budget page with goals → Savings goals → Earn points on completion → Gacha draw to win a cat → Shop for cats and accessories → Monthly recap

**Prompt:** Open-ended Best Financial Hack: build a tool that helps with anything finance-related.
**Fit (implied):** Finance habit-building app using Capital One API data for transactions and savings; page lists the Capital One prize as won without explaining targeting.  *(targeted: Capital One Challenge)*
**Sponsor tools:** Capital One API (Hosting users' savings and transactions, supporting)
**AI:** Amazon Bedrock with Mistral on AWS is listed, likely for analysis and plan generation; specifics not described.
**Architecture:** React/Vite frontend with Tailwind and framer-motion calling a Flask backend using SQLAlchemy/Postgres driver, boto3 for AWS, and the Capital One API.
**Novelty:** Collectible-cat gacha and shop mechanics layered on budgeting.
**Scope:** small · working: Repo about 2k LOC with frontend and Flask backend; only screenshots, no demo or video. · polish: Themed UI screenshots; README is a Vite template; no tests.
**Gaps:** No demo or video; How Bedrock is used unstated; MongoDB/SQL roles unclear
Sources: https://devpost.com/software/cat-finances, https://github.com/Redninjale/budget-app

---

