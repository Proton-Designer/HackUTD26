# McHacks: project cards (6 projects)

Facts and short paraphrases only; no cross-project analysis. Full records are in the workbook and JSONL.

## McHacks 12

### Debug Debacle  (McHacks 12)

- **Prizes:** 3rd Place [3rd]; Gumloop - Best AI project that uses the Gumloop API [unknown]  (tier: overall_top3)
- **Pitch:** A competitive web game where users race in real time to find a bug in code within five minutes, without seeing test cases.
- **Problem / user:** Hunting a stubborn bug is frustrating; the team turned it into a timed multiplayer contest to practise debugging. / programmers and students
- **Domain / idea type:** entertainment_games + dev_tools / entertainment_or_game
- **Platforms / hardware / AI:** web / False / llm_chat
- **Stack:** langs Python; TypeScript; frontend React; Tailwind; backend Flask; Socket.IO; db Supabase; hosting 
- **Tech/APIs:** Gumloop (other, unclear, sponsor); Auth0 (auth, supporting, sponsor); Supabase (database, supporting); Socket.IO (framework, core); Flask (framework, core); React (framework, core)
- **Sponsor APIs:** Gumloop; Auth0 | fit: Entered for the Gumloop AI prize and lists Gumloop in its stack; the specific use was not confirmed from the page text read.
- **Repo:** public, commits 133 (before/in/after event: None/None/None), README solid
- **Demo/writeup:** video True, live none, screenshots 13, writeup medium, impact claims False
- **Notes:** Browser IDE with live competition via Socket.IO; Gumloop is used for the AI part, exact role not verified.
- **Team size:** 4 | **Confidence:** medium | unverified: event_start; event_end; ai_types; sponsor_fit_note; tech_items.Auth0.is_sponsor
- **Links:** [Devpost](https://devpost.com/software/debug-debacle) | [GitHub](https://github.com/honzikschenk/web-app-ide)

### Planorama  (McHacks 12)

- **Prizes:** 2nd Place [2nd]  (tier: overall_top3)
- **Pitch:** A visual node-based project planning tool, started for developers and generalized for any team or non-technical user.
- **Problem / user:** Existing project planning tools felt too complicated or not tailored to developers who want to map projects visually. / developers and project teams
- **Domain / idea type:** productivity_workplace + dev_tools / twist_on_known_app
- **Platforms / hardware / AI:** web; bot_or_chat / False / None
- **Stack:** langs TypeScript; frontend Next.js; React Flow; backend Prisma; discord.js; db MongoDB; Firebase; hosting 
- **Tech/APIs:** React Flow (framework, core); Next.js (framework, core); Prisma (framework, supporting); MongoDB (database, supporting); Firebase (database, supporting); discord.js (framework, supporting)
- **Sponsor APIs:** 
- **Repo:** none_listed, commits None (before/in/after event: None/None/None), README None
- **Demo/writeup:** video True, live none, screenshots 9, writeup long, impact claims None
- **Notes:** Solo build using a React Flow canvas with a Discord bot integration; heading structure of writeup not standard, only inspiration section confirmed.
- **Team size:** 1 | **Confidence:** medium | unverified: event_start; event_end; ai_used; writeup_sections; has_impact_claims
- **Links:** [Devpost](https://devpost.com/software/planorama-ft9hj4)

### SeeForMe  (McHacks 12)

- **Prizes:** 1st Place [1st]  (tier: overall_top3)
- **Pitch:** Real-time object detection with spoken feedback and map-based directions to help visually or mobility impaired people get around.
- **Problem / user:** People with visual or mobility impairments need help identifying nearby objects and navigating daily routes. / visually or mobility impaired people
- **Domain / idea type:** accessibility + mobility_transport / social_good
- **Platforms / hardware / AI:** desktop / False / vision; speech_or_voice
- **Stack:** langs Python; frontend ; backend ; db ; hosting 
- **Tech/APIs:** YOLO (ai_model, core); Google Directions API (maps_geo, supporting); Google Geocoding API (maps_geo, supporting)
- **Sponsor APIs:** 
- **Repo:** public, commits None (before/in/after event: None/None/None), README None
- **Demo/writeup:** video True, live none, screenshots 3, writeup medium, impact claims False
- **Notes:** YOLO object detection paired with voice output and Google directions; writeup is brief and omits how-built and challenges sections.
- **Team size:** 4 | **Confidence:** medium | unverified: event_start; event_end; platforms; repo_clone_failed
- **Links:** [Devpost](https://devpost.com/software/seeforme) | [GitHub](https://github.com/garancedvn/SFM)


## McHacks 13

### Bloomscroll  (McHacks 13)

- **Prizes:** Third Place [3rd]; Best AI project that uses the Gumloop API [unknown]  (tier: overall_top3)
- **Pitch:** A study tool that turns the doomscroll gesture into a structured learning flow, with each scroll advancing the student through material.
- **Problem / user:** Students prefer effortless scrolling over rigid studying, so the app channels that habit into learning. / students
- **Domain / idea type:** education + mental_health / twist_on_known_app
- **Platforms / hardware / AI:** web / False / llm_chat
- **Stack:** langs JavaScript; frontend Svelte; Tailwind; backend ; db MongoDB; hosting 
- **Tech/APIs:** Gumloop (other, unclear, sponsor); Svelte (framework, core); MongoDB (database, supporting); Tailwind CSS (framework, supporting)
- **Sponsor APIs:** Gumloop | fit: Entered for the Gumloop AI prize and lists Gumloop in its stack; the specific workflow was not confirmed from the page text read.
- **Repo:** public, commits None (before/in/after event: None/None/None), README None
- **Demo/writeup:** video True, live none, screenshots 17, writeup long, impact claims False
- **Notes:** Short-video-style vertical feed used as study interface; Gumloop is listed in the stack and the team also won the Gumloop AI prize; writeup uses reflection section instead of next steps.
- **Team size:** 4 | **Confidence:** medium | unverified: event_start; event_end; ai_types; sponsor_fit_note; repo_clone_failed
- **Links:** [Devpost](https://devpost.com/software/brain-rejuvenate) | [GitHub](https://github.com/jackolsen0171/mchacks_13)

### McGill Go  (McHacks 13)

- **Prizes:** First Place [1st]  (tier: overall_top3)
- **Pitch:** Web app helping students plan exchange semesters by finding which partner-university courses count toward their home degree.
- **Problem / user:** Course-equivalency information for exchange is fragmented across systems, making degree planning slow and confusing. / university students planning exchange
- **Domain / idea type:** education / twist_on_known_app
- **Platforms / hardware / AI:** web / False / llm_chat; rag_or_search
- **Stack:** langs Python; TypeScript; frontend Next.js; React; backend FastAPI; Selenium; db MongoDB; hosting 
- **Tech/APIs:** Gemini (ai_model, core); Claude (ai_model, supporting); Selenium (framework, supporting); MongoDB (database, supporting); FastAPI (framework, core); Next.js (framework, core)
- **Sponsor APIs:** 
- **Repo:** public, commits None (before/in/after event: None/None/None), README None
- **Demo/writeup:** video True, live none, screenshots 11, writeup medium, impact claims False
- **Notes:** Uses Selenium scraping alongside LLMs; page lists Claude and Cursor among tools; Devpost project is titled Exchange in the URL and McGill Go on the page.
- **Team size:** 4 | **Confidence:** medium | unverified: event_start; event_end; ai_types; tech_items.Gemini.depth; repo_clone_failed
- **Links:** [Devpost](https://devpost.com/software/exchange-v1hmq8) | [GitHub](https://github.com/yufei002/McHacks-13)

### WaterYouDoin  (McHacks 13)

- **Prizes:** Second Place [2nd]  (tier: overall_top3)
- **Pitch:** Browser extension that analyzes prompts locally before they reach an AI assistant, redirecting simple factual lookups to a non-AI search engine.
- **Problem / user:** Developers use AI for trivial queries that do not need it, wasting resources; the tool nudges more intentional AI use. / developers using AI assistants
- **Domain / idea type:** sustainability_climate + dev_tools / dev_tool
- **Platforms / hardware / AI:** browser_extension / False / False
- **Stack:** langs TypeScript; JavaScript; frontend Vite; backend Node.js; db ; hosting 
- **Tech/APIs:** Vite (framework, supporting); Vitest (framework, supporting); Node.js (framework, supporting)
- **Sponsor APIs:** 
- **Repo:** public, commits 67 (before/in/after event: None/None/None), README solid
- **Demo/writeup:** video True, live none, screenshots 11, writeup medium, impact claims False
- **Notes:** Prompt classification happens locally in the extension rather than via a remote model; framed around AI resource awareness.
- **Team size:** 4 | **Confidence:** medium | unverified: event_start; event_end; ai_used
- **Links:** [Devpost](https://devpost.com/software/wateryourdoin) | [GitHub](https://github.com/memoud0/WaterYouDoin)
