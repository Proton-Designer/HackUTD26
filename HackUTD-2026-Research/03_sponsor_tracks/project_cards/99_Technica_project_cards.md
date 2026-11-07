# Technica: project cards (5 projects)

Facts and short paraphrases only; no cross-project analysis. Full records are in the workbook and JSONL.

## Technica 2024

### Pennywise  (Technica 2024)

- **Prizes:** Winner Capital One: Best Financial Hack [unknown]  (tier: sponsor_winner)
- **Pitch:** Event-budgeting web app with a form for event type, date and expected costs, an AI financial-advice chatbot and spending analytics.
- **Problem / user:** People planning events struggle to stay within budget; the team paired budgeting with a friendly AI chatbot. / people planning events on a budget
- **Domain / idea type:** fintech_finance + accessibility / twist_on_known_app
- **Platforms / hardware / AI:** web / False / llm_chat
- **Stack:** langs JavaScript; Python; frontend React; Ant Design; backend Flask; db ; hosting Vercel
- **Tech/APIs:** Gemini (ai_model, core); React (framework, supporting); Ant Design (framework, supporting); Flask (framework, supporting)
- **Sponsor APIs:**  | fit: Targeted Capital One's Best Financial Hack with an event-budget planner and AI advisor; the page lists no Capital One API or dataset use.
- **Repo:** public, commits 35 (before/in/after event: 0/35/0), README none
- **Demo/writeup:** video True, live not_checked, screenshots 4, writeup medium, impact claims False
- **Notes:** Beginner team (most new to React and backend); includes accommodation and pronoun settings; page names no Capital One API and no sponsor tool beyond the prize.
- **Team size:** 4 | **Confidence:** high | unverified: ui_polish; n_screenshots
- **Links:** [Devpost](https://devpost.com/software/pennywise-84p1il) | [GitHub](https://github.com/Yashaswe/pennywise)


## Technica 2025

### Personal Cart Roaster  (Technica 2025)

- **Prizes:** Winner [Capital One] Best Financial Hack [unknown]  (tier: sponsor_winner)
- **Pitch:** Chrome extension that sends a shopper's cart info to Gemini for a roast and reads it aloud with ElevenLabs to discourage impulse buying.
- **Problem / user:** The author impulse buys often and wanted a humorous financial deterrent at checkout. / impulse online shoppers
- **Domain / idea type:** fintech_finance + entertainment_games / creative_tool
- **Platforms / hardware / AI:** browser_extension / False / llm_chat; speech_or_voice
- **Stack:** langs TypeScript; HTML/CSS; frontend React; Vite; backend Node.js; db ; hosting 
- **Tech/APIs:** Gemini API (ai_model, core); ElevenLabs API (ai_model, core); Chrome extension (MV3) (framework, core); React/Vite (framework, supporting)
- **Sponsor APIs:**  | fit: Targeted Capital One's Best Financial Hack as a spending deterrent; the page lists no Capital One API or dataset use, only Gemini and ElevenLabs.
- **Repo:** none_listed, commits None (before/in/after event: None/None/None), README None
- **Demo/writeup:** video False, live none, screenshots 2, writeup short, impact claims False
- **Notes:** Solo build of a Manifest V3 Chrome extension; autoplay audio was blocked so a manual audio player was used; initially aimed at Amazon only.
- **Team size:** 1 | **Confidence:** high | unverified: ui_polish; n_screenshots
- **Links:** [Devpost](https://devpost.com/software/personal-cart-roaster)

### Resale Radar  (Technica 2025)

- **Prizes:** Winner [Capital One] Best Financial Hack [unknown]  (tier: sponsor_winner)
- **Pitch:** Java desktop tool that scrapes Poshmark sold listings, removes outliers and recommends effective listing prices for resellers, with graphs of the data.
- **Problem / user:** Resale sites suggest prices based on sold prices while items often sell below list price, so sellers misprice listings. / online resale sellers (Poshmark)
- **Domain / idea type:** fintech_finance + retail_consumer / data_or_analytics
- **Platforms / hardware / AI:** desktop / False / False
- **Stack:** langs Java; frontend JavaFX; FXML; SceneBuilder; backend Playwright; db ; hosting 
- **Tech/APIs:** Playwright (framework, core); JavaFX/FXML (framework, core); Poshmark sold-listing data (scraped) (data_source, core)
- **Sponsor APIs:**  | fit: Targeted Capital One's Best Financial Hack with a pricing tool to help sellers maximize sale revenue; the page lists no Capital One API or dataset use.
- **Repo:** none_listed, commits None (before/in/after event: None/None/None), README None
- **Demo/writeup:** video False, live none, screenshots 0, writeup short, impact claims False
- **Notes:** Non-AI statistical tool built in Java with JavaFX/FXML GUI and Playwright scraping; no GitHub or screenshots listed on the page.
- **Team size:** 2 | **Confidence:** high | unverified: ui_polish
- **Links:** [Devpost](https://devpost.com/software/resale-radar)


## Technica 2026

### Atlantis - The Long Night  (Technica 2026)

- **Prizes:** Winner [Capital One] The Best Use of Nessie [unknown]  (tier: sponsor_winner)
- **Pitch:** 2D pixel-art finance-education game in a sinking city where every in-game coin movement is a real Nessie banking record and a mirror button reveals the real-world concept.
- **Problem / user:** Finance education feels dull; existing games do not teach by consequence or reflect real barriers like missing credit history or family wealth. / young adults and students learning personal finance
- **Domain / idea type:** education + fintech_finance / entertainment_or_game
- **Platforms / hardware / AI:** web / False / llm_chat
- **Stack:** langs Python; TypeScript; frontend React; Phaser 3; Vite; backend FastAPI; Pydantic; db SQLite; hosting Vercel; Render
- **Tech/APIs:** Capital One Nessie API (payments, core, sponsor); Gemini API (ai_model, supporting); Phaser 3 (framework, core); FastAPI (framework, supporting); SQLite (database, supporting); Vercel (cloud, supporting); Render (cloud, supporting)
- **Sponsor APIs:** Capital One Nessie API | fit: Made Nessie the game's money layer: each class is a Nessie customer with checking, savings and credit accounts, wages are deposits, spending is purchases, loans are loan records, all synced with confirm-by-GET, targeting Best Use of Nessie.
- **Repo:** public, commits 64 (before/in/after event: 0/64/0), README thin
- **Demo/writeup:** video True, live not_checked, screenshots 15, writeup long, impact claims False
- **Notes:** Four starting classes based on real financial barriers; deterministic seeded engine with bot balance simulator; Nessie writes queued, POSTed then confirmed by GET with local cache; Gemini only writes feedback bullets, numbers checked against the engine.
- **Team size:** 4 | **Confidence:** high | unverified: ui_polish; n_screenshots
- **Links:** [Devpost](https://devpost.com/software/atlantis-the-long-night) | [GitHub](https://github.com/Mitanshcodes/Atlantis)

### Treasure Dive  (Technica 2026)

- **Prizes:** Winner [Capital One] The Best Use of Nessie [unknown]  (tier: sponsor_winner)
- **Pitch:** Mobile/web app that reads a user's Nessie purchase history, matches stores against open class-action settlements found by a Gemini scout agent, and shows possible claims in a pixel-art treasure UI.
- **Problem / user:** People miss money they may be owed from settlements because finding and matching claims against their own purchases is tedious. / consumers who may qualify for settlements
- **Domain / idea type:** fintech_finance + civic_legal / automation_or_agent
- **Platforms / hardware / AI:** mobile_ios; web / False / llm_chat; agent_or_tool_use; vision; rag_or_search
- **Stack:** langs TypeScript; frontend Expo; React Native; React Native Paper; Reanimated; backend Node.js; Express; node-cron; zod; db SQLite; hosting 
- **Tech/APIs:** Capital One Nessie API (payments, core, sponsor); Google Gemini (search grounding, URL context, vision) (ai_model, core); Expo / React Native (framework, supporting); SQLite (better-sqlite3) (database, supporting); react-native-maps (maps_geo, supporting)
- **Sponsor APIs:** Capital One Nessie API | fit: Pulled real sandbox customer, accounts, merchants and purchases from Nessie to match against settlements and recorded a Nessie deposit when a claim is marked paid, targeting Best Use of Nessie.
- **Repo:** private_or_missing, commits None (before/in/after event: None/None/None), README None
- **Demo/writeup:** video True, live none, screenshots 1, writeup long, impact claims False
- **Notes:** Gemini scout agent uses Google Search grounding and URL context, with code verifying claim sites before showing a badge; 'may qualify' wording enforced in code; English/Spanish; 145 tests and a mock mode.
- **Team size:** 1 | **Confidence:** high | unverified: ui_polish; n_screenshots; repo_clone_failed
- **Links:** [Devpost](https://devpost.com/software/treasure-dive) | [GitHub](https://github.com/prajithravisankar/technica_2026)
