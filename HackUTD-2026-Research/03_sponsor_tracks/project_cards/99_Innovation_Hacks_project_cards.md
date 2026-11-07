# Innovation Hacks: project cards (2 projects)

Facts and short paraphrases only; no cross-project analysis. Full records are in the workbook and JSONL.

## Innovation Hacks 2.0

### Dollar Dash  (Innovation Hacks 2.0)

- **Prizes:** Winner State Farm: Financial Wellness Track [unknown]  (tier: sponsor_winner)
- **Pitch:** Real-time multiplayer classroom stock-market game where students trade through news events and watch portfolios and a leaderboard move.
- **Problem / user:** Students rarely get hands-on exposure to how money works; financial literacy is taught abstractly through lectures. / students and teachers in classrooms
- **Domain / idea type:** education + fintech_finance / entertainment_or_game
- **Platforms / hardware / AI:** web / False / None
- **Stack:** langs JavaScript; frontend React; Tailwind; backend Node.js; Socket.IO; WebSockets; db ; hosting Render
- **Tech/APIs:** Socket.IO / WebSockets (framework, core); ElevenLabs (ai_model, unclear); React (framework, supporting); Render (cloud, supporting)
- **Sponsor APIs:**  | fit: Won State Farm's Financial Wellness track with a stock-trading classroom game teaching diversification and compound growth; no State Farm API or dataset is mentioned.
- **Repo:** public, commits 102 (before/in/after event: 0/102/0), README detailed
- **Demo/writeup:** video True, live not_checked, screenshots 19, writeup short, impact claims False
- **Notes:** Page is a short impact summary rather than a build writeup; uses Socket.IO/WebSockets for live play; ElevenLabs appears in the stack tags with no described use.
- **Team size:** 3 | **Confidence:** high | unverified: ai_used; writeup_sections
- **Links:** [Devpost](https://devpost.com/software/dollar-dash) | [GitHub](https://github.com/WillBlair/dollardash)

### Redreemer  (Innovation Hacks 2.0)

- **Prizes:** Winner State Farm: Financial Wellness Track [unknown]  (tier: sponsor_winner)
- **Pitch:** SMS service usable from any phone, even a flip phone, that guides homeless and formerly incarcerated people up an 8-step ladder to financial independence and blocks predatory lenders.
- **Problem / user:** Financial apps assume a smartphone, email and bank account, excluding people who are homeless or recently released from prison. / homeless and reentry populations, plus caseworkers
- **Domain / idea type:** fintech_finance + social_community / social_good
- **Platforms / hardware / AI:** bot_or_chat; web / False / llm_chat; predictive_ml; rag_or_search
- **Stack:** langs TypeScript; frontend React; Tailwind CSS; backend Node.js; db PostgreSQL; Supabase; hosting Vercel
- **Tech/APIs:** Twilio SMS (telecom, core); Gemini 2.5 Flash (ai_model, core); ElevenLabs (ai_model, supporting); Auth0 (auth, supporting); Supabase (database, supporting); PostgreSQL (database, supporting); Vercel (cloud, supporting)
- **Sponsor APIs:**  | fit: Won State Farm's Financial Wellness track with an SMS-based financial-inclusion ladder (benefits eligibility, scam interception, fair-chance jobs); no State Farm API or dataset is mentioned.
- **Repo:** public, commits 14 (before/in/after event: 0/14/0), README detailed
- **Demo/writeup:** video True, live not_checked, screenshots 19, writeup medium, impact claims True (Cites 582,000 homeless Americans and 600,000 yearly prison releases; claims 23 scam attempts blocked so far.)
- **Notes:** Messages pass a 20-layer detection pipeline (crisis, scam, employer layers) before Gemini replies; includes a caseworker dashboard with risk scoring; claims 23 scam attempts blocked.
- **Team size:** 2 | **Confidence:** high | unverified: writeup_sections
- **Links:** [Devpost](https://devpost.com/software/redreemer) | [GitHub](https://github.com/sumedha092/redreemer)
