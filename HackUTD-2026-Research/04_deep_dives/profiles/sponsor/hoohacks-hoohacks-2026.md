# HooHacks — HooHacks 2026 (1 projects)

### foreGASt
*HooHacks HooHacks 2026 · dataset: sponsor · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** Winner Best Financial Hack - Sponsored by Capital One

**What it is:** A fertilizer price forecasting tool for farmers that uses natural gas market data. XGBoost models predict urea price and direction 30, 60 and 90 days out, a Monte Carlo engine adds risk ranges, and the app turns this into a buy-now-or-wait recommendation based on the farmer's crops and acreage.
**Problem / user:** Farmers who face volatile fertilizer prices with little protection and fixed planting windows; page also pitches it to banks offering it to farm customers.

**Features**
- Price forecasts at 30/60/90 days — Six XGBoost models: regressors for price and classifiers for up/down direction, trained on 1997-2024 EIA and World Bank data. *[shown_working]*
- Monte Carlo risk engine — 10,000 simulated paths using walk-forward error distribution give P10/P90 ranges. *[claimed]*
- Nitrogen exposure calculation — Computed from the crops and acreage a user enters. *[claimed]*
- Buy-now vs wait recommendation — Compares risk across horizons to give personalized advice. *[claimed]*
- Accounts and crop dashboard — Login with encrypted data in SQLite, crop overview, current costs and a data tab, in Streamlit. *[shown_working]*

**Flow:** Sign up or log in → Add crops and acreage → App computes nitrogen exposure and shows current fertilizer costs → Review 30/60/90-day forecasts and confidence intervals → Read the recommendation and open the data tab

**Prompt:** Finance-track prize sponsored by Capital One with no brief beyond the track name.
**Fit (implied):** Farm-finance risk tool that could be offered by banks; uses no Capital One API. Page says it won the Capital One financial prize.  *(targeted: Best Financial Hack - Capital One)*
**AI:** XGBoost regressors and classifiers with recency weighting and a logistic objective; Monte Carlo simulation over historical error; Claude and Claude Code used to write much of the code.
**Architecture:** Python pipeline ingests EIA data, trains models, writes forecasts to a cache; FastAPI backend and Streamlit frontend with SQLite accounts; Docker on Railway.
**Novelty:** Links natural gas prices to fertilizer decisions at the individual farm level using only free public data.
**Scope:** medium · working: Live Railway demo link and Docker setup; about 3.9k LOC; no tests. · polish: Streamlit dashboard with login; no video; README is run notes.
**Claims:** About 75% accuracy on 90-day price direction averaged over 50 training runs | 10,000 Monte Carlo price paths
**Gaps:** No video; Accuracy figure described two ways
Sources: https://devpost.com/software/hoohacks-submission, https://github.com/bob3457/HooHacks26

---

