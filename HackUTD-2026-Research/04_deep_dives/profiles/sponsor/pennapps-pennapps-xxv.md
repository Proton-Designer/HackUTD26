# PennApps — PennApps XXV (1 projects)

### Plate-O
*PennApps PennApps XXV · dataset: sponsor · tier: sponsor_winner · evidence A · confidence medium*
**Prizes:** Winner Track: Best Financial Hack (Sponsored by Capital One)

**What it is:** A takeout budgeting app that calculates an affordable food-delivery budget from income, expenses and savings, then recommends restaurants within it, including a surprise-meal pick that orders within the limit and learns from feedback.
**Problem / user:** People who order takeout often and want to stay within budget without losing variety.

**Features**
- Takeout budget calculation — Uses Capital One API data on income, expenses and savings to derive an ideal takeout budget. *[claimed]*
- Taste- and budget-aware restaurant recommendations — Yelp and Uber Eats data merged with Word2Vec, scored on cost, speed, novelty and sustainability. *[claimed]*
- Surprise meal — User enters a budget and the app picks and orders a meal inside financial limits. *[claimed]*
- Preference learning — Stores past orders, ratings, dietary restrictions and feedback in MongoDB to refine suggestions. *[claimed]*
- Natural-language preferences — Tune LLM API processes free-text input and predicts preferences. *[claimed]*

**Flow:** Sign in → Enter a takeout budget → Receive a surprise restaurant pick → Order the meal → Feedback improves later picks

**Prompt:** Best Financial Hack sponsored by Capital One: reimagine banking and how financial services could be redesigned.
**Fit (implied):** Ties personal finance data from the Capital One API to a daily spending category, takeout, to set limits and guide choices.  *(targeted: Track: Best Financial Hack (Sponsored by Capital One))*
**Sponsor tools:** Capital One API (Income, expense and savings data for budget calculation, core)
**AI:** Tune-hosted LLM and Llama 3.1 405B for language input and preference prediction; Word2Vec and fuzzy matching to merge restaurant datasets; scikit-learn style ranking.
**Architecture:** Next.js frontend, FastAPI backend, MongoDB Atlas, Docker/Defang deploy; datasets from Yelp and Uber Eats CSV combined by embeddings.
**Novelty:** Surprise-meal ordering constrained by a bank-derived budget, plus sustainability scoring of restaurants.
**Scope:** small · working: About 3k LOC repo with Docker; demo video on Devpost; README only lists libraries. · polish: Next.js UI with sign-in screen; no tests; thin documentation.
**Claims:** Model combines personal finance data with restaurant preferences for tailored recommendations
**Gaps:** README is a library list; Video not viewed; Real ordering integration unclear
Sources: https://devpost.com/software/plate-o, https://github.com/pennapps-w/plate-o

---

