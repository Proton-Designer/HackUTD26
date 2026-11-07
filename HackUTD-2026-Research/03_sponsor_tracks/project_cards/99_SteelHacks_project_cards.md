# SteelHacks: project cards (3 projects)

Facts and short paraphrases only; no cross-project analysis. Full records are in the workbook and JSONL.

## SteelHacks XIII (2026)

### Heard!  (SteelHacks XIII (2026))

- **Prizes:** [NVIDIA] Beyond the Chatbot [unknown]  (tier: sponsor_winner)
- **Pitch:** Ambient voice agent that joins working meetings, sorts ideas into a live board, researches open questions and speaks up when it has something to add.
- **Problem / user:** Meeting AI tools only transcribe and summarize; teams want a participant that researches and thinks along in real time. / project teams in working meetings
- **Domain / idea type:** productivity_workplace + ai_agents_infra / automation_or_agent
- **Platforms / hardware / AI:** web / False / llm_chat; agent_or_tool_use; speech_or_voice
- **Stack:** langs Python; TypeScript; frontend React; Vite; backend FastAPI; db ; hosting 
- **Tech/APIs:** NVIDIA Nemotron Super 120B on NVIDIA NIM (ai_model, core, sponsor); Claude Agent SDK (framework, core); ElevenLabs Scribe v2 + TTS (ai_model, core); FastAPI (framework, supporting)
- **Sponsor APIs:** NVIDIA Nemotron; NVIDIA NIM | fit: Targeted NVIDIA Beyond the Chatbot by using Nemotron on NIM as the fast always-on classifier and background note-taking agent in an ambient meeting teammate, chosen after benchmarking latency with reasoning on and off.
- **Repo:** public, commits 66 (before/in/after event: 0/66/0), README detailed
- **Demo/writeup:** video True, live none, screenshots 10, writeup medium, impact claims False
- **Notes:** Nemotron Super 120B (reasoning off) classifies speech every few seconds, a second Nemotron agent rewrites notes every 20s, and a Claude Agent SDK session decides answer/research/silence; speed was benchmarked on NVIDIA NIM first.
- **Team size:** 3 | **Confidence:** high | unverified: ui_polish
- **Links:** [Devpost](https://devpost.com/software/heard-puhs0f) | [GitHub](https://github.com/jiazhenz026/heard-meeting)

### SurrealEstate  (SteelHacks XIII (2026))

- **Prizes:** [NVIDIA] Beyond the Chatbot [unknown]  (tier: sponsor_winner)
- **Pitch:** Paste a Zillow link and an evidence-grounded virtual agent gives an interactive room-by-room tour plus sourced neighborhood research, with a one-page review sheet.
- **Problem / user:** Remote or out-of-town home buyers must research neighborhoods, schools, safety and the property across many tabs or travel to see it. / remote and relocating home buyers
- **Domain / idea type:** housing_real_estate + ai_agents_infra / twist_on_known_app
- **Platforms / hardware / AI:** web / False / agent_or_tool_use; vision; rag_or_search; speech_or_voice; llm_chat
- **Stack:** langs ; frontend ; backend ; db ; hosting 
- **Tech/APIs:** NVIDIA Nemotron (orchestration, vision, verification) (ai_model, core, sponsor); Google Gemini (ai_model, supporting); ElevenLabs (ai_model, supporting); Census / OpenStreetMap / FEMA / NCES / Yelp data (data_source, core)
- **Sponsor APIs:** NVIDIA Nemotron | fit: Targeted NVIDIA Beyond the Chatbot with Nemotron as the orchestrator that labels floor-plan rooms with vision, selects facts, runs follow-up research and verifies answers against source evidence.
- **Repo:** private_or_missing, commits None (before/in/after event: None/None/None), README None
- **Demo/writeup:** video True, live none, screenshots 13, writeup long, impact claims False
- **Notes:** Converts a 3D home tour into a HouseGraph with Nemotron vision labeling rooms; Nemotron selects and verifies facts while Gemini writes the text and ElevenLabs speaks; draws on Census, OSM, FEMA, NCES, Yelp and Reddit data.
- **Team size:** 3 | **Confidence:** high | unverified: ui_polish; stack_*; repo_clone_failed
- **Links:** [Devpost](https://devpost.com/software/surrealestate) | [GitHub](https://github.com/Lucas-Granucci/SurrealEstate)

### Weave  (SteelHacks XIII (2026))

- **Prizes:** [NVIDIA] Beyond the Chatbot [unknown]; [MLH] Best Use of Gemini API [unknown]  (tier: sponsor_winner)
- **Pitch:** Electron co-browsing app where a helper and a family member share one webpage, each with a personalized accessible view and an in-page spider assistant that explains where to click.
- **Problem / user:** Helping relatives with banking or medical sites over screen share is hard, and most pages are not built for accessibility. / older adults and the relatives who help them online
- **Domain / idea type:** accessibility + social_community / new_category
- **Platforms / hardware / AI:** desktop / False / llm_chat; agent_or_tool_use; speech_or_voice
- **Stack:** langs TypeScript; frontend Electron; backend Fastify; zod; pnpm monorepo; db Snowflake; hosting 
- **Tech/APIs:** NVIDIA Nemotron 3.5 Lightning via NIM (ai_model, core, sponsor); Google Gemini API (ai_model, core, sponsor); ElevenLabs (ai_model, supporting); Snowflake (database, unclear); Electron (framework, core)
- **Sponsor APIs:** NVIDIA Nemotron; NVIDIA NIM; Gemini API | fit: Targeted NVIDIA Beyond the Chatbot with Nemotron via NIM powering the assistant's answers, element targeting and per-person layout proposals, while Gemini handled translation and simpler wording (also winning the MLH Gemini prize).
- **Repo:** private_or_missing, commits None (before/in/after event: None/None/None), README None
- **Demo/writeup:** video True, live none, screenshots 10, writeup medium, impact claims False
- **Notes:** Per-person page rebuilds from a sanitized DOM model with every outbound model payload audited; Nemotron via NIM handles answers and element targeting, hedged requests and provider fallback cut latency to about a second; won an MLH Gemini prize too.
- **Team size:** 2 | **Confidence:** high | unverified: ui_polish; repo_clone_failed
- **Links:** [Devpost](https://devpost.com/software/weave-z8t1i0) | [GitHub](https://github.com/Emmit3/Weave)
