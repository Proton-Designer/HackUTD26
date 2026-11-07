# hackCBS — hackCBS 8.0 (1 projects)

### WealthPulse
*hackCBS hackCBS 8.0 · dataset: winners · tier: overall_top3 · evidence A · confidence high*
**Prizes:** 1st Runner Up [2nd]

**What it is:** A fintech web app that tracks stocks, mutual funds and crypto in one dashboard, gives Gemini-generated risk-aware insights, a chatbot and automated portfolio reports, and includes a financial education hub with Auth0 sign-in.
**Problem / user:** Investing needs costly advisors or expertise and means juggling platforms; aimed at beginner and self-directed investors.

**Features**
- Unified multi-asset dashboard — Separate stock, crypto and mutual-fund dashboards plus a portfolio page with live price feeds from backend modules. *[shown_working]*
- AI investment insights — Gemini 2.0 Flash via OpenRouter gives personalized recommendations by risk profile. *[claimed]*
- Portfolio analysis and reports — AI endpoint generates reports with risk categorization, volatility and Sharpe ratio metrics. *[claimed]*
- Smart chatbot — Chat endpoint answers financial questions with the LLM. *[claimed]*
- Portfolio CRUD — Add and update holdings per user stored in MongoDB. *[claimed]*
- Education hub — Courses, videos and blogs from beginner to advanced. *[shown_working]*
- Auth0 login — Auth0 SDK with Next.js middleware secures user portfolios. *[claimed]*
- Alerts — Market-movement alerts mentioned on Devpost; not seen in README. *[unclear]*

**Flow:** Sign in with Auth0 → Set risk profile and add holdings → View stock, MF and crypto dashboards → Request AI insights or report → Chat with assistant or study in education hub

**Prompt:** not public / not found
**Fit (explicit):** Devpost lists the three MLH tracks: Gemini for insights, MongoDB for portfolios, Auth0 for login.  *(targeted: Best Use of Gemini API, Best Use of MongoDB Atlas, Best Use of Auth0, 1st Runner Up)*
**Sponsor tools:** Gemini API (via OpenRouter) (Insights, reports and chatbot, core); MongoDB Atlas (Portfolio storage, supporting); Auth0 (Authentication, supporting)
**AI:** Gemini 2.0 Flash accessed via OpenRouter with preprocessed inputs and managed token use to produce recommendations, reports and chat replies.
**Architecture:** Next.js 15 frontend with Auth0 and Recharts on Vercel; FastAPI backend with stock, crypto and mutual fund API modules and MongoDB portfolios; Next API routes call the LLM.
**Novelty:** Combines three asset classes, AI advice and learning content in one app; common fintech hackathon pattern.
**Scope:** medium · working: Live Vercel demo, YouTube video and repo about 8,000 lines with README screenshots section. · polish: Detailed README, Canva deck, animated UI; no tests; README license says private.
**Claims:** Real-time insights and alerts | Encrypted storage of financial data
**Gaps:** Which data APIs supply live prices not named; No accuracy or user metrics; Video not watched; Track prompts not published
Sources: https://devfolio.co/projects/wealthpulse-fa3f, evidence/hackcbs-hackcbs-8-0-wealthpulse.json

---

