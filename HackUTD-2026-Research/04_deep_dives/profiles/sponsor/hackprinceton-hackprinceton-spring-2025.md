# HackPrinceton — HackPrinceton Spring 2025 (1 projects)

### Roots
*HackPrinceton HackPrinceton Spring 2025 · dataset: sponsor · tier: sponsor_winner · evidence A · confidence medium*
**Prizes:** Winner Best Financial Hack [Sponsored by Capital One]

**What it is:** Roots is a one-stop personal finance web app: budgeting with AI-optimized sliders, Gemini-built investment portfolios, credit card recommendations from transaction history, and generated lessons. Nessie supplies simulated accounts and spending.
**Problem / user:** New investors needing literacy and experienced investors juggling many assets, overwhelmed by many separate fintech apps.

**Features**
- Budgeting dashboard — Finds discretionary spending, offers manual or AI-optimized sliders and computes savings since account start. *[claimed]*
- AI portfolio recommendation — Questionnaire and uploaded trades go to Gemini, which proposes a portfolio from budget savings with hypothetical returns. *[claimed]*
- Optimized vs current portfolio comparison — For existing investors, shows holdings next to the optimized version. *[claimed]*
- Credit card recommendations — Matches hand-collected card cashback data to spending categories; supports apply and side-by-side comparison. *[claimed]*
- Personalized lessons — Gemini drafts budgeting and investing modules from the user's transactions, human-reviewed. *[claimed]*

**Flow:** Log in via Auth0 → Nessie creates accounts and seeds transactions → Adjust budget sliders or let AI optimize → Fill investment questionnaire and view portfolio → Review recommended cards and lessons

**Prompt:** Capital One's HackPrinceton Spring 2025 prize for any finance-related tool; Capital One staff also judged. No further brief published.
**Fit (implied):** Broad finance app covering budgeting, investing and cards, built on Capital One's Nessie sandbox for accounts and transactions.  *(targeted: Best Financial Hack [Sponsored by Capital One])*
**Sponsor tools:** Capital One Nessie (Simulated accounts and transaction history, core)
**AI:** Gemini generates investment portfolios from questionnaire and savings data and writes lesson content; credit card matching is rule/data based.
**Architecture:** Next.js/React/Tailwind frontend with Auth0 and Plaid/Knot keys; Flask backend on PostgreSQL; Nessie and Gemini called from backend.
**Novelty:** Bundles budgeting, investing, card optimization and education in one app, tying investment sizing to counterfactual budget savings.
**Scope:** medium · working: Devpost describes full flow; parent repo only holds submodules so code not seen. · polish: Demo video on Devpost; README minimal.
**Claims:** Fully functional investment portfolio | Dozens of credit cards hand-collected
**Gaps:** Submodule code not inspected; Video not watchable
Sources: https://devpost.com/software/roots-xk19te, https://github.com/Roots-Finance/parent-repo

---

