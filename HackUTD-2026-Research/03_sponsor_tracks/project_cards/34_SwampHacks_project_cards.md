# SwampHacks: project cards (2 projects)

Facts and short paraphrases only; no cross-project analysis. Full records are in the workbook and JSONL.

## SwampHacks XI

### Pay Pals  (SwampHacks XI)

- **Prizes:** Winner Best Finance Hack Sponsored By Capital One [unknown]  (tier: sponsor_winner)
- **Pitch:** Gamified accountability app where friends wager favors and tokens on each other's financial goals, with Nessie data and Solana tokens to validate users.
- **Problem / user:** Young adults struggle to follow through on financial goals; social betting between friends is meant to add accountability without real money. / college students and young adults
- **Domain / idea type:** fintech_finance + social_community / new_category
- **Platforms / hardware / AI:** web / False / llm_chat
- **Stack:** langs Python; JavaScript; frontend React; Tailwind CSS; Three.js; backend FastAPI; db MongoDB Atlas; hosting Railway
- **Tech/APIs:** Capital One Nessie API (payments, core, sponsor); Solana API (other, core); Gemini API (ai_model, supporting); MongoDB Atlas (database, supporting); FastAPI (framework, supporting); React (framework, supporting); Railway (cloud, supporting)
- **Sponsor APIs:** Capital One Nessie API | fit: Used the Nessie API as the financial-tool layer to validate users' financial goals within a friend-betting app, targeting the Capital One Best Finance Hack prize.
- **Repo:** public, commits 2 (before/in/after event: 0/2/0), README detailed
- **Demo/writeup:** video True, live not_checked, screenshots 11, writeup medium, impact claims False
- **Notes:** Kalshi-style prediction-market concept using favors instead of cash, with a Three.js 3D frontend element and lobby-based friend betting; hosted on Railway with a live URL.
- **Team size:** 4 | **Confidence:** high | unverified: ui_polish; n_screenshots
- **Links:** [Devpost](https://devpost.com/software/project-c1nomzfei7a0) | [GitHub](https://github.com/GridGxly/PayPals)


## SwampHacks XII

### Runway  (SwampHacks XII)

- **Prizes:** Winner Capital One - The Best Use of Nessie! [unknown]  (tier: sponsor_winner)
- **Pitch:** Forecasts a user's checking balance 30 days out from Capital One data and arranges consented, private cover from friends via real Nessie sandbox transfers when a shortfall looms.
- **Problem / user:** People living paycheck to paycheck hit overdrafts before payday and find asking for help embarrassing; banks warn only after balances are low. / paycheck-to-paycheck bank customers and their family/friends
- **Domain / idea type:** fintech_finance + social_community / new_category
- **Platforms / hardware / AI:** web; mobile_cross / False / llm_chat; agent_or_tool_use; predictive_ml
- **Stack:** langs Python; TypeScript; frontend Expo; React Native; backend FastAPI; db TimescaleDB (Tiger Data); PostgreSQL; hosting Vultr; Caddy; Docker
- **Tech/APIs:** Capital One Nessie API (payments, core, sponsor); Google Gemini (ai_model, core); Tiger Data / TimescaleDB (database, core); Auth0 (auth, supporting); FastAPI (framework, supporting); Expo / React Native (framework, supporting); Vultr (cloud, supporting); Claude Code (other, supporting)
- **Sponsor APIs:** Capital One Nessie API | fit: Used 8 Nessie endpoints (customers, accounts, bills, merchants, purchases, deposits, transfers) for the forecast data and moved real sandbox money as transfer plus deposit pairs, targeting the Best Use of Nessie prize.
- **Repo:** public, commits 172 (before/in/after event: 0/170/2), README detailed
- **Demo/writeup:** video True, live not_checked, screenshots 2, writeup long, impact claims True (Reports own eval numbers: 66% lower forecast error, 15/15 privacy attacks held, 0 unsafe transfers in 2,000 simulated networks.)
- **Notes:** Deterministic forecast engine does the maths while Gemini only picks tools; journaled idempotent transfers; reports eval suites (privacy attacks, 2,000 simulated networks, 570+ tests); built with Claude Code and Auth0 sign-in.
- **Team size:** 3 | **Confidence:** high | unverified: ui_polish; n_screenshots
- **Links:** [Devpost](https://devpost.com/software/runway-57dpic) | [GitHub](https://github.com/rshah2001/runway)
