# HackRice — HackRice 15 (2 projects)

### OwlNudge
*HackRice HackRice 15 · dataset: sponsor · tier: sponsor_winner · evidence A · confidence medium*
**Prizes:** Winner Capital One Best Financial Hack

**What it is:** A web financial-planning app with three Gemini-driven advisor personas, an onboarding quiz, a personalized dashboard, push notifications and learning modules, designed to work without any bank account connection.
**Problem / user:** Unbanked and underbanked people, students, gig workers and recent immigrants who need accessible financial guidance without linking a bank; cites 63 million unbanked Americans.

**Features**
- Three AI advisors: Sofia (literacy), Marcus (investing education), Luna (behavioral coaching) — Chat interface backed by Google Gemini calls from a FastAPI backend. *[claimed]*
- Onboarding quiz — Collects financial situation, goals and background to build a user profile. *[claimed]*
- Personalized dashboard — Metrics and insights adapt to profile and goals; built-in user personas for diverse situations. *[claimed]*
- Real-time proactive notifications — WebSocket channel from backend pushes financial insights; APScheduler is in requirements. *[claimed]*
- Gamified learning modules — Interactive financial education content in the React frontend. *[claimed]*
- No-bank-account design — Advice built from quiz and self-entered data rather than bank linkage. *[claimed]*

**Flow:** Complete onboarding quiz → Explore personalized dashboard → Chat with one of three AI advisors → Receive proactive notifications → Work through learning modules

**Prompt:** Capital One Best Financial Hack at HackRice 15: build tools addressing finance-related problems using creativity and technical skill; no API named.
**Fit (implied):** Offers financial guidance and education aimed at unbanked users, an inclusion angle on the open finance prompt.  *(targeted: Capital One Best Financial Hack)*
**AI:** Google Gemini powers three persona advisors giving tailored financial advice and nudges; prompts are tied to user profile data.
**Architecture:** React/Vite/Tailwind/shadcn frontend talks to a FastAPI backend with SQLite persistence, WebSocket notifications and Gemini API calls.
**Novelty:** Persona-split advisors and explicit unbanked-first framing; otherwise a standard chat plus dashboard stack. Devpost built-with lists Flutter, inconsistent with the repo.
**Scope:** medium · working: About 11.5k LOC across frontend and backend with setup steps; no demo, video or tests. · polish: Readable README with quick start; extensive shadcn component set; no screenshots listed.
**Claims:** Dedicated to the 63 million unbanked Americans | Smart planning with no bank account required
**Gaps:** no demo or video; feature status unverified
Sources: https://devpost.com/software/owlnudge, https://github.com/reyanp/OwlNudge

---

### Swipe Coach
*HackRice HackRice 15 · dataset: sponsor · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** Winner Capital One Best Financial Hack

**What it is:** A web app that tells a multi-card holder which credit card to swipe for each purchase to earn the most rewards, with spending dashboards, recurring-charge detection, card recommendations and a Gemini chatbot called Flow Coach.
**Problem / user:** People holding several credit cards who cannot tell which gives the best cashback per purchase and want to see where their money goes.

**Features**
- Smart Swipe best-card recommendation — Scores each card per merchant, category and amount using parameterized reward rules, bonuses and monthly caps, with an explainable breakdown. *[shown_working]*
- Monte Carlo scenario ranking — Simulates spending scenarios to rank cards, described as sample average approximation. *[claimed]*
- Card management and applications — Add, edit and remove linked cards through a secure add-card flow. *[shown_working]*
- Transaction tracking and spending overview — Transactions with summaries and monthly insights stored in MongoDB. *[shown_working]*
- Recurring-charge detection and forecast — Separates one-off from recurring charges, surfaces subscriptions and predicts next expected charges. *[claimed]*
- Card recommendations with comparison — Suggests new cards and compares them against current ones. *[shown_working]*
- Flow Coach chatbot — Gemini-based chat and narratives layered on the finance computations. *[shown_working]*
- Monthly budget preferences — Saved budget shown on Home and in Category Momentum. *[claimed]*

**Flow:** Sign in with Auth0 → Add a credit card → View dashboard and spending overview → Use Smart Swipe for a purchase → Review card recommendations → Ask Flow Coach questions

**Prompt:** Capital One Best Financial Hack at HackRice 15: build tools addressing finance-related problems using creativity and technical skill; no API named.
**Fit (implied):** Credit card rewards optimization and spending insight for consumers, squarely a consumer-finance tool.  *(targeted: Capital One Best Financial Hack)*
**AI:** Gemini drives the Flow Coach chatbot and narrative explanations; the recommendation engine itself uses rule-based reward modeling with Monte Carlo simulation, not an LLM.
**Architecture:** React/TypeScript/Vite client with Auth0 login, Flask API on MongoDB (users, accounts, transactions, cards), reward engine module, Gemini calls; hosted on Firebase.
**Novelty:** Reward optimizer models caps, rotating categories and effective versus marginal rates with simulation, deeper than a typical card-picker; Plaid code was removed.
**Scope:** medium · working: Live Firebase demo link and demo video; about 13.6k LOC split client and server. · polish: Multiple pages, Auth0 protected routes, screenshots and indexes tuned; no tests.
**Claims:** Cap-saturation stress tests and regression coverage for recommendations | Reduced slow Mongo queries via composite indexes
**Gaps:** README text empty in evidence; video not viewed
Sources: https://devpost.com/software/swipe-coach, https://github.com/leo2971998/HackRice25

---

