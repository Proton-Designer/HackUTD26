# Bitcamp: project cards (2 projects)

Facts and short paraphrases only; no cross-project analysis. Full records are in the workbook and JSONL.

## Bitcamp 2025

### BudgetBuddy  (Bitcamp 2025)

- **Prizes:** Winner Best Financial Hack - Capital One [unknown]  (tier: sponsor_winner)
- **Pitch:** Gamified finance app that pulls Nessie transaction history, flags unusual spending with an anomaly model and gives emotional Gemini-written nudges.
- **Problem / user:** People find budgeting dull and miss spending trends and big purchases until it is too late. / young adults managing personal spending
- **Domain / idea type:** fintech_finance + mental_health / twist_on_known_app
- **Platforms / hardware / AI:** web / False / llm_chat; predictive_ml
- **Stack:** langs Python; TypeScript; JavaScript; frontend React; Vite; Zustand; TanStack Router; styled-components; backend Flask; db MongoDB Atlas; hosting Netlify
- **Tech/APIs:** Capital One Nessie API (data_source, core, sponsor); Google Gemini (ai_model, core); scikit-learn Isolation Forest (ai_model, core); MongoDB Atlas (database, supporting); Flask (framework, core); React (framework, core)
- **Sponsor APIs:** Capital One Nessie API | fit: Targeted Capital One's Best Financial Hack by pulling a user's transaction history through the Nessie API and running trend and anomaly analysis on it, then presenting results through a gamified assistant.
- **Repo:** public, commits 49 (before/in/after event: 0/49/0), README solid
- **Demo/writeup:** video True, live not_checked, screenshots 25, writeup medium, impact claims False
- **Notes:** Separate frontend, backend and notifications-API repos; Isolation Forest anomaly detection on Nessie transactions plus an emotional-companion style; deployed on Netlify.
- **Team size:** 4 | **Confidence:** high | unverified: event_end; ui_polish
- **Links:** [Devpost](https://devpost.com/software/budgetbuddy-3qvr78) | [GitHub](https://github.com/team-moondust/BudgetBuddy-frontend)

### FinGuard  (Bitcamp 2025)

- **Prizes:** Winner Best Financial Hack - Capital One [unknown]  (tier: sponsor_winner)
- **Pitch:** Browser extension and web dashboard that recommends the best credit card per purchase, warns about risky spending and builds financial habits.
- **Problem / user:** Shoppers use the wrong card or overspend and lack in-the-moment financial guidance. / credit-card-holding consumers
- **Domain / idea type:** fintech_finance + safety_security / twist_on_known_app
- **Platforms / hardware / AI:** browser_extension; web / False / llm_chat; recommendation
- **Stack:** langs Python; JavaScript; frontend React; Tailwind CSS; backend Python; db MongoDB; hosting 
- **Tech/APIs:** Google Gemini (ai_model, core); Selenium and BeautifulSoup scraping (data_source, supporting); MongoDB (database, supporting); React (framework, core)
- **Sponsor APIs:**  | fit: Entered for Capital One's Best Financial Hack with a card-recommendation and spending-safety extension; the page does not mention Capital One or Nessie APIs.
- **Repo:** none_listed, commits None (before/in/after event: None/None/None), README None
- **Demo/writeup:** video False, live none, screenshots 22, writeup long, impact claims False
- **Notes:** Selenium and BeautifulSoup scrape card reward rules; React extension plus dashboard; very long writeup (about 1000 words).
- **Team size:** 4 | **Confidence:** high | unverified: event_end; sponsor_fit_note; ui_polish
- **Links:** [Devpost](https://devpost.com/software/finguard-x1akuc)
