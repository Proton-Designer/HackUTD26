# HackNC: project cards (2 projects)

Facts and short paraphrases only; no cross-project analysis. Full records are in the workbook and JSONL.

## HackNC 2024

### AI-powered Investment Portfolio Creator  (HackNC 2024)

- **Prizes:** Winner Capital One - Best Financial Hack [unknown]  (tier: sponsor_winner)
- **Pitch:** Web app that builds a tailored stock portfolio from a user's answers to prompts, using Gemini and Yahoo Finance market data.
- **Problem / user:** Newcomers do not know how to turn their goals and risk tolerance into a portfolio. / beginner investors
- **Domain / idea type:** fintech_finance / twist_on_known_app
- **Platforms / hardware / AI:** web / False / llm_chat; recommendation
- **Stack:** langs Python; TypeScript; frontend React; Tailwind CSS; backend Flask; db ; hosting 
- **Tech/APIs:** Google Gemini (ai_model, core); Yahoo Finance data (data_source, core); API Ninjas (data_source, supporting); pandas and NumPy (framework, supporting)
- **Sponsor APIs:**  | fit: Won Capital One's Best Financial Hack with an investment-portfolio generator; the page cites Yahoo Finance and Gemini, not Capital One APIs.
- **Repo:** public, commits 26 (before/in/after event: 0/26/0), README solid
- **Demo/writeup:** video True, live none, screenshots 7, writeup short, impact claims False
- **Notes:** Very short writeup; Flask back end with React front end, Gemini for generation and Yahoo Finance for real-time and historical prices.
- **Team size:** 4 | **Confidence:** high | unverified: event_end; writeup_sections; ui_polish
- **Links:** [Devpost](https://devpost.com/software/ai-powered-investment-portfolio-creator) | [GitHub](https://github.com/ColeWhaley1/hackNC24)


## HackNC 2026

### RxSolve  (HackNC 2026)

- **Prizes:** Winner [Capital One] The Best Use of Nessie [unknown]  (tier: sponsor_winner)
- **Pitch:** Agent layer between pharmacies and pharmacy benefit managers that audits paid claims for underpayment, gathers evidence and files appeals, tested against a PBM simulator with Nessie ledger transfers.
- **Problem / user:** PBMs underpay pharmacy claims and appeals are slow and manual. / independent pharmacies
- **Domain / idea type:** health_wellness + fintech_finance / automation_or_agent
- **Platforms / hardware / AI:** web / False / agent_or_tool_use; llm_chat; speech_or_voice
- **Stack:** langs TypeScript; Python; frontend React; backend Bun; db TigerData; hosting 
- **Tech/APIs:** Capital One Nessie sandbox (payments, core, sponsor); Photon (telecom, supporting, sponsor); Google Gemini (ai_model, core); ElevenLabs (ai_model, supporting); TigerData (database, core)
- **Sponsor APIs:** Capital One Nessie API; Photon | fit: Won Best Use of Nessie by using the Nessie sandbox as the money ledger for recovered claim underpayments, adapting logical transfers to Nessie's actual transaction behavior.
- **Repo:** public, commits 104 (before/in/after event: 0/104/0), README detailed
- **Demo/writeup:** video True, live none, screenshots 46, writeup long, impact claims False
- **Notes:** TypeScript/Bun monorepo with an API orchestrator, a standalone PBM simulator and a dashboard; ElevenLabs voice, Photon messaging and TigerData storage; 46 screenshots.
- **Team size:** 4 | **Confidence:** high | unverified: event_end; Photon use depth; ui_polish
- **Links:** [Devpost](https://devpost.com/software/rxsolve) | [GitHub](https://github.com/manyuagashe/rxsolve)
