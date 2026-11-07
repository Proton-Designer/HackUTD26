# Bitcamp — Bitcamp 2025 (2 projects)

### BudgetBuddy
*Bitcamp Bitcamp 2025 · dataset: sponsor · tier: sponsor_winner · evidence A · confidence medium*
**Prizes:** Winner Best Financial Hack - Capital One

**What it is:** A progressive web app where a virtual pet reacts to your spending. It pulls simulated bank transactions from Nessie, flags odd purchases with an anomaly model, and lets you chat with the pet, whose Gemini-written feedback is sarcastic, supportive or soft.
**Problem / user:** College-age users who find finance apps cold and overwhelming; goal is budgeting that feels more emotional and less boring.

**Features**
- Nessie transaction sync — Backend pulls account transaction history from Capital One's Nessie API for display and analysis. *[claimed]*
- Mood-reactive buddy pet — Pet's mood shifts happier or sadder with spending behavior and big purchases. *[claimed]*
- Chat with chosen tone — Gemini generates feedback in sarcastic, supportive or soft tone per user preference. *[claimed]*
- Anomaly detection — scikit-learn IsolationForest flags unusual purchases as possible fraud. *[claimed]*
- Synthetic transaction generator — Python tool builds spend data from merchant categories and emotional context. *[claimed]*
- Monthly budget insights and scoring — LLM and ML outputs combined into a score with trend analysis. *[claimed]*
- Game-like onboarding, transactions and settings pages — React PWA with login, onboarding, transaction list and preferences. *[shown_working]*

**Flow:** Open home screen with the buddy → Sign up or log in via game-like onboarding → Sync transactions from Nessie → See buddy react to spending → Chat with buddy in chosen tone → Adjust settings

**Prompt:** Open-ended Best Financial Hack: payments, smarter shopping, accessible financing or financial literacy.
**Fit (implied):** Uses the Nessie API for transaction history and applies trend and anomaly analysis plus an emotional gamified assistant, framed as making budgeting approachable.  *(targeted: Best Financial Hack - Capital One)*
**Sponsor tools:** Capital One Nessie API (Source of transaction history, core)
**AI:** Gemini API writes tone-controlled feedback and chat; IsolationForest detects anomalous transactions; LLM and ML outputs feed a combined behavior score.
**Architecture:** React/TypeScript PWA (Zustand, TanStack Router) on Netlify calling a Flask backend with MongoDB Atlas; Nessie plus a custom generator feed transactions to the ML and Gemini steps; separate notifications repo exists.
**Novelty:** Emotional virtual-pet framing for budgeting with user-selectable sarcasm level; pairs classic anomaly model with LLM tone.
**Scope:** medium · working: Live Netlify demo link and about 1.7k LOC frontend repo; backend in separate repos not inspected. · polish: Styled PWA with multiple pages; README is the unmodified Vite template; no video.
**Claims:** Working fraud detection model built in limited time
**Gaps:** README is template; Backend repo not read; No video; Notifications API purpose unstated
Sources: https://devpost.com/software/budgetbuddy-3qvr78, https://github.com/team-moondust/BudgetBuddy-frontend

---

### FinGuard
*Bitcamp Bitcamp 2025 · dataset: sponsor · tier: sponsor_winner · evidence B · confidence medium*
**Prizes:** Winner Best Financial Hack - Capital One

**What it is:** A browser extension plus web dashboard that recommends the best linked credit card for each online purchase, warns about scam sites, and offers a Gemini retrieval-based assistant over the user's transactions.
**Problem / user:** Online shoppers who miss card rewards, hit scam sites or overspend and lack clear monthly spending visibility.

**Features**
- Best-card recommendation — Extension picks among linked cards using rewards, points and discounts stored in MongoDB. *[claimed]*
- Nudge scam-site warning — Site reputation checked through IPQS and a warning shown if flagged. *[claimed]*
- Spending tracking by category — Transactions are categorized and stored for analysis. *[claimed]*
- Financial dashboard — React/Tailwind page shows income, expenses, savings and cashback. *[claimed]*
- Gemini RAG insights — Gemini answers spending questions grounded in the user's transaction data. *[claimed]*
- Spending limits and auth — Node backend handles login and limits. *[claimed]*

**Flow:** Link credit cards → Shop online with the extension active → Extension recommends a card and checks site reputation → Transactions get tracked and categorized → Review dashboard → Ask the assistant about spending

**Prompt:** Open-ended Best Financial Hack: payments, smarter shopping, accessible financing or financial literacy.
**Fit (implied):** Page states it won the Capital One financial prize; fits the smarter-shopping and financial-literacy angles through card optimization, scam warnings and spending insights. No Capital One API is mentioned.  *(targeted: Best Financial Hack - Capital One)*
**AI:** Gemini used as a RAG model over user transaction data for insights and Q&A; extension card logic is lookup-based.
**Architecture:** React browser extension and React/Tailwind dashboard, Node.js backend, MongoDB for users, transactions and card rewards data, IPQS and Gemini external APIs.
**Novelty:** Combines point-of-purchase card optimization and scam-site nudges with a spending dashboard.
**Scope:** medium · working: Page claims integrated extension, dashboard and recommendation engine; no repo, demo or video links. · polish: Seven uncaptioned screenshots; otherwise unverified.
**Claims:** Users reportedly improved spending habits and savings, no numbers given
**Gaps:** No repo; No demo or video; Insights Recharge unexplained; Python/Selenium role unknown
Sources: https://devpost.com/software/finguard-x1akuc

---

