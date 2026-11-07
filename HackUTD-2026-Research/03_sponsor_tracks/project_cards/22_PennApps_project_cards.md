# PennApps: project cards (3 projects)

Facts and short paraphrases only; no cross-project analysis. Full records are in the workbook and JSONL.

## PennApps XXV

### Plate-O  (PennApps XXV)

- **Prizes:** Winner Track: Best Financial Hack (Sponsored by Capital One) [unknown]  (tier: sponsor_winner)
- **Pitch:** Food delivery recommender that uses a user's income, expenses and savings to suggest meals that fit their budget and tastes.
- **Problem / user:** Takeout is convenient but hurts budgets; people lack guidance that balances finances with food discovery. / budget-conscious takeout customers
- **Domain / idea type:** food_nutrition + fintech_finance / twist_on_known_app
- **Platforms / hardware / AI:** web / False / llm_chat; recommendation
- **Stack:** langs Python; frontend ; backend FastAPI; db MongoDB Atlas; hosting Docker; Defang
- **Tech/APIs:** Capital One API (data_source, core, sponsor); Llama (ai_model, core); MongoDB Atlas (database, supporting); Defang (cloud, supporting); FastAPI (framework, core)
- **Sponsor APIs:** Capital One API | fit: Won the Capital One Best Financial Hack track by analyzing a user's income, expenses and savings through the Capital One API to set a meal-ordering budget feeding the recommender.
- **Repo:** public, commits 80 (before/in/after event: 0/80/0), README thin
- **Demo/writeup:** video True, live none, screenshots 13, writeup long, impact claims False
- **Notes:** Combines a Llama-based recommendation engine with Capital One account analysis to compute an affordable ordering budget; FastAPI, MongoDB Atlas and Docker, with Defang deployment.
- **Team size:** 4 | **Confidence:** high | unverified: event_end; writeup_sections; Capital One API product name; ui_polish
- **Links:** [Devpost](https://devpost.com/software/plate-o) | [GitHub](https://github.com/pennapps-w/plate-o)


## PennApps XXVI

### SproutAI  (PennApps XXVI)

- **Prizes:** Winner CATEGORY - Finance (Capital One) [unknown]  (tier: sponsor_winner)
- **Pitch:** Grocery inventory optimizer that forecasts demand with ML and sustainability metrics to cut food waste and keep shelves stocked.
- **Problem / user:** Retailers overstock or run out, wasting food and money. / grocery retailers
- **Domain / idea type:** retail_consumer + sustainability_climate / data_or_analytics
- **Platforms / hardware / AI:** web / False / predictive_ml; llm_chat; rag_or_search
- **Stack:** langs Python; JavaScript; Java; frontend React; backend ; db ; hosting 
- **Tech/APIs:** Cerebras (ai_model, core); Exa (data_source, supporting); Google Gemini (ai_model, supporting); React (framework, supporting)
- **Sponsor APIs:**  | fit: Won the Capital One finance category with a retail inventory-forecasting platform; the page shows no Capital One API or banking feature.
- **Repo:** none_listed, commits None (before/in/after event: None/None/None), README None
- **Demo/writeup:** video True, live none, screenshots 16, writeup medium, impact claims False
- **Notes:** Uses Cerebras for fast training/inference alongside Exa and Gemini; short writeup with no repo link on the page.
- **Team size:** 2 | **Confidence:** high | unverified: event_end; sponsor_fit_note; writeup_sections; ui_polish
- **Links:** [Devpost](https://devpost.com/software/sproutai-9vil8w)

### Subsave  (PennApps XXVI)

- **Prizes:** Winner CATEGORY - Finance (Capital One) [unknown]  (tier: sponsor_winner)
- **Pitch:** Mobile app where users prepay a year of subscriptions into a DeFi yield vault so yield offsets costs while keeping monthly cancellation.
- **Problem / user:** Subscriptions drain money with no yield; users want cheaper recurring payments without long commitments. / subscription-paying consumers
- **Domain / idea type:** fintech_finance / new_category
- **Platforms / hardware / AI:** mobile_cross / False / llm_chat
- **Stack:** langs TypeScript; frontend React Native; Expo; backend ; db MongoDB Atlas; hosting 
- **Tech/APIs:** Lulo (payments, core); Squads Grid (payments, core); Auth0 (auth, supporting); Google Gemini (ai_model, supporting); MongoDB Atlas (database, supporting)
- **Sponsor APIs:**  | fit: Won the Capital One finance category with a DeFi-backed subscription-prepay app; no Capital One API is listed on the page.
- **Repo:** public, commits 3 (before/in/after event: 1/2/0), README detailed
- **Demo/writeup:** video True, live none, screenshots 1, writeup medium, impact claims False
- **Notes:** DeFi yield vault via Lulo and Squads Grid on Solana-style rails, with Auth0 login and a mobile-first Expo dashboard.
- **Team size:** 3 | **Confidence:** high | unverified: event_end; sponsor_fit_note; writeup_sections; ui_polish
- **Links:** [Devpost](https://devpost.com/software/subsave) | [GitHub](https://github.com/adlonymous/subsave)
