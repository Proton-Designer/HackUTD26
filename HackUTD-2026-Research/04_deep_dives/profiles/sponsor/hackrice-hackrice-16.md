# HackRice — HackRice 16 (1 projects)

### Larp City
*HackRice HackRice 16 · dataset: sponsor · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** Winner [CHALLENGE] - Capital One Best Financial Hack

**What it is:** A browser financial-life simulator in a pixel city where the player lives from age 22 to retirement, making decisions on insurance, cards, investing, debt and events, then gets a score and AI coach review.
**Problem / user:** Learners who find financial literacy content abstract; the game lets them see consequences of money choices, with a vision for bank and school use.

**Features**
- Sammy owl onboarding — Narrator walks through health insurance, a beginner card, emergency fund, Roth IRA and 401(k), expenses and car loan. *[shown_working]*
- Day-by-day seeded simulation — Deterministic engine with modules for paychecks, bills, credit, loans, debt, taxes, investing; skip to next event. *[shown_working]*
- Market and life events — Crashes, booms, recessions, car breakdowns, injuries, marriage; time pauses at major moments for a decision. *[shown_working]*
- In-game phone — Apps for banking, stocks, news, bills, taxes, calendar, goals and map. *[shown_working]*
- Review and replay — Revisit a past decision on identical seeded market and luck and compare outcomes. *[shown_working]*
- Real credit-card data — Beginner cards drawn from CFPB survey and real terms; stored in Tiger Data Postgres. *[claimed]*
- Retirement score and AI financial coach — Score blends readiness and wellbeing; AI explains choices from run history; ElevenLabs voice dependency present. *[claimed]*

**Flow:** Start at 22 with randomized salary, debt and credit score → Sammy guides initial financial setup → Time advances day by day with pauses on events → Check phone apps and make decisions → Retire when ready → Review decisions and replay earlier choices

**Prompt:** Capital One Best Financial Hack at HackRice 16: use creativity and technical skill to build tools for any finance-related need; no API named.
**Fit (implied):** Teaches personal-finance decision making through a life simulation, aimed at financial literacy and eventual bank use.  *(targeted: Capital One Best Financial Hack)*
**AI:** AI financial coach produces personalized explanations from the player's run history; Gemini listed; ElevenLabs client and backboard SDK in server deps.
**Architecture:** PixiJS/TypeScript browser game with a separate deterministic simulation engine, Express server (ElevenLabs, backboard SDK, Postgres), Tiger Data database, Python data scripts.
**Novelty:** Full life-to-retirement simulation with deterministic replay, research data pipelines and real card terms; unusually large for a hackathon.
**Scope:** large · working: Live site larpcity.club noted in README; 1,291 files, 68k LOC, tests present. · polish: Extensive docs, design vision notes, art assets and pixel city; three Devpost screenshots.
**Claims:** Complete simulated financial life from age 22 to retirement | Seeded deterministic replay under identical market conditions
**Gaps:** README read to 3000 chars only; live site not tested
Sources: https://devpost.com/software/temp-6yaocn, https://github.com/cayden-h/LarpCity

---

