# TAMUhack: project cards (2 projects)

Facts and short paraphrases only; no cross-project analysis. Full records are in the workbook and JSONL.

## TAMUhack 2025

### PAWS - Personal Assets and Wise Saving  (TAMUhack 2025)

- **Prizes:** Winner Capital One Challenge [unknown]  (tier: sponsor_winner)
- **Pitch:** Gamified budgeting app that builds a budget and savings plan from transactions and rewards completed goals with points for a cat-collecting gacha.
- **Problem / user:** Young people find managing money overwhelming; the app makes good budgeting habits rewarding through game mechanics. / young people learning to budget
- **Domain / idea type:** fintech_finance + entertainment_games / twist_on_known_app
- **Platforms / hardware / AI:** web / False / predictive_ml; llm_chat
- **Stack:** langs Python; JavaScript; frontend React; backend Flask; db MongoDB; SQL; hosting AWS
- **Tech/APIs:** Capital One API (Nessie) (payments, supporting, sponsor); Amazon Bedrock Mistral (ai_model, core); AWS (cloud, supporting); Flask (framework, supporting); React (framework, supporting); MongoDB (database, supporting)
- **Sponsor APIs:** Capital One API | fit: Used the Capital One API to host users' savings and transaction data that feeds the budget and savings-goal logic, targeting the Capital One Challenge.
- **Repo:** public, commits 80 (before/in/after event: 0/80/0), README thin
- **Demo/writeup:** video True, live none, screenshots 12, writeup short, impact claims False
- **Notes:** Cat-collecting gacha mechanic as budgeting incentive; page also shows a USAA Challenge win not listed in the queue; AI via Amazon Bedrock Mistral.
- **Team size:** 4 | **Confidence:** high | unverified: ui_polish; n_screenshots; sponsor_apis_used depth
- **Links:** [Devpost](https://devpost.com/software/cat-finances) | [GitHub](https://github.com/Redninjale/budget-app)


## TAMUhack 2026

### Drift  (TAMUhack 2026)

- **Prizes:** Winner Capital One Challenge [unknown]  (tier: sponsor_winner)
- **Pitch:** Personal-finance planner that pulls Capital One Nessie profiles, parses goals with AI and runs Monte Carlo simulations to show goal probabilities and what-if sensitivity.
- **Problem / user:** Graduates heading into full-time work want realistic forecasts of reaching financial goals instead of plugging static values into calculators. / young professionals planning finances
- **Domain / idea type:** fintech_finance + accessibility / data_or_analytics
- **Platforms / hardware / AI:** web / False / llm_chat; speech_or_voice; predictive_ml
- **Stack:** langs TypeScript; Python; frontend Next.js; Tailwind CSS; Three.js; backend Node.js; Express; Python (NumPy, pandas); db ; hosting 
- **Tech/APIs:** Capital One Nessie API (payments, core, sponsor); Google Gemini (ai_model, supporting); ElevenLabs (ai_model, supporting); NumPy/pandas Monte Carlo engine (framework, core); Next.js (framework, supporting); Three.js (framework, token)
- **Sponsor APIs:** Capital One Nessie API | fit: Generated customer profiles and account/transaction data through the Nessie API as the input to a Monte Carlo goal-forecasting model, targeting the Capital One Challenge.
- **Repo:** public, commits 77 (before/in/after event: 0/69/8), README solid
- **Demo/writeup:** video True, live none, screenshots 5, writeup medium, impact claims False
- **Notes:** Monte Carlo engine scaled with high-performance computing; natural-language goal input and ElevenLabs text-to-speech added as accessibility features; authors say the model lacks real financial expertise.
- **Team size:** 3 | **Confidence:** high | unverified: ui_polish; n_screenshots
- **Links:** [Devpost](https://devpost.com/software/pff) | [GitHub](https://github.com/aadit2805/drift)
