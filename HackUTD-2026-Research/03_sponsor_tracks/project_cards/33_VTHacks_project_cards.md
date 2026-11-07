# VTHacks: project cards (2 projects)

Facts and short paraphrases only; no cross-project analysis. Full records are in the workbook and JSONL.

## VTHacks 13

### CrediWise - Use the right card, every time.  (VTHacks 13)

- **Prizes:** Winner [Capital One] $250 Amazon Gift Card [unknown]  (tier: sponsor_winner)
- **Pitch:** Chrome extension that detects checkout pages and recommends the credit card with the best rewards, plus a savings dashboard with AI insights from scraped public card offers.
- **Problem / user:** Shoppers rarely know which of their cards earns the best rewards at a given checkout and miss out on cashback. / credit-card-holding online shoppers
- **Domain / idea type:** fintech_finance + retail_consumer / twist_on_known_app
- **Platforms / hardware / AI:** browser_extension; web / False / llm_chat; recommendation
- **Stack:** langs Python; JavaScript; frontend React; Tailwind CSS; Vite; backend Flask; db Supabase (Postgres); Upstash Redis; hosting Vercel; GitHub Actions
- **Tech/APIs:** Bright Data MCP (data_source, core); Llama / Gemini LLM (ai_model, supporting); Supabase (database, supporting); Chrome extension (MV3) (framework, core); Flask (framework, supporting)
- **Sponsor APIs:**  | fit: Targeted the Capital One challenge with a card-rewards optimizer built on scraped public offers; the page names no Capital One API or dataset.
- **Repo:** public, commits 17 (before/in/after event: 0/16/1), README solid
- **Demo/writeup:** video True, live not_checked, screenshots 6, writeup medium, impact claims False
- **Notes:** Bright Data MCP scrapers refreshed by GitHub Actions normalize public card offers; an LLM parses offer terms into rules; stores issuer/rewards profiles, not card data. Prize is a Capital One gift card.
- **Team size:** 3 | **Confidence:** high | unverified: ui_polish; n_screenshots
- **Links:** [Devpost](https://devpost.com/software/crediwise-use-the-right-card-every-time) | [GitHub](https://github.com/adithyaharish/crediwise-vthacks)


## VTHacks 14

### LoadCheck  (VTHacks 14)

- **Prizes:** Winner [Capital One] Best Use of Nessie [unknown]  (tier: sponsor_winner)
- **Pitch:** Decision tool for owner-operator truck drivers that reads load offers, computes true net profit, searches multi-load routes and predicts cash shortages using Nessie sandbox bills.
- **Problem / user:** Advertised per-mile rates hide deadhead miles, fuel, fixed costs and upcoming bills, so drivers can accept loads that cause low profit or cash shortages. / independent owner-operator truck drivers
- **Domain / idea type:** fintech_finance + mobility_transport / automation_or_agent
- **Platforms / hardware / AI:** web / False / llm_chat; vision
- **Stack:** langs Python; TypeScript; frontend React; TypeScript; backend FastAPI; db ; hosting 
- **Tech/APIs:** Capital One Nessie API (payments, supporting, sponsor); Google Gemini (ai_model, core); FastAPI (framework, supporting); React (framework, supporting); Claude / Codex / OpenAI (dev tools) (ai_model, token)
- **Sponsor APIs:** Capital One Nessie API | fit: Used Nessie for sandbox banking activity, upcoming bills and advance information feeding a cash-flow timeline that predicts shortages, targeting Best Use of Nessie; recorded fallbacks keep the demo working offline.
- **Repo:** public, commits 87 (before/in/after event: 0/87/0), README detailed
- **Demo/writeup:** video False, live none, screenshots 5, writeup long, impact claims False
- **Notes:** Gemini only extracts offers (with user confirmation) and explains results; all numbers come from deterministic Python modules; labels sandbox data clearly; reports 100 backend tests and 15/15 demo checks.
- **Team size:** 2 | **Confidence:** high | unverified: ui_polish; n_screenshots
- **Links:** [Devpost](https://devpost.com/software/loadcheck) | [GitHub](https://github.com/VTHACKATHON/VTHACKS)
