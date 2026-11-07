# DeltaHacks: project cards (6 projects)

Facts and short paraphrases only; no cross-project analysis. Full records are in the workbook and JSONL.

## DeltaHacks 12

### deltawash  (DeltaHacks 12)

- **Prizes:** Second Place: Garmin Smartwatch [2nd]  (tier: overall_top3)
- **Pitch:** Camera-based handwashing monitor that checks WHO protocol steps and shows progress with LEDs.
- **Problem / user:** Many people, including healthcare workers, skip proper handwashing steps, risking infection. / healthcare workers and clinics
- **Domain / idea type:** health_wellness + safety_security / hardware_gadget
- **Platforms / hardware / AI:** hardware; web / True / vision; predictive_ml
- **Stack:** langs Python; C++; frontend React; Tailwind; CSS; backend ; db ; hosting 
- **Tech/APIs:** Raspberry Pi (hardware_part, core); Pi Camera (hardware_part, core); ESP8266 (hardware_part, core); TensorFlow (framework, core); PyTorch (framework, supporting)
- **Sponsor APIs:** 
- **Repo:** public, commits 9 (before/in/after event: None/None/None), README none
- **Demo/writeup:** video True, live not_checked, screenshots 9, writeup medium, impact claims False
- **Notes:** Pi camera plus on-device vision model classifies handwash step; Pi signals an ESP8266 over WiFi that lights LEDs per step; React site alongside.
- **Team size:** 4 | **Confidence:** medium | unverified: event_start; event_end; n_screenshots; writeup_length
- **Links:** [Devpost](https://devpost.com/software/deltawash) | [GitHub](https://github.com/Goldenstar2660/DeltaWash)

### Quota  (DeltaHacks 12)

- **Prizes:** First Place: Bose Headphones [1st]  (tier: overall_top3)
- **Pitch:** VS Code extension and web dashboard that flag costly AI API calls in code, suggest cheaper models and forecast spend.
- **Problem / user:** AI API costs are invisible to developers until the invoice arrives, causing surprise bills. / developers and engineering teams using AI APIs
- **Domain / idea type:** dev_tools + fintech_finance / dev_tool
- **Platforms / hardware / AI:** desktop; web / False / llm_chat; other
- **Stack:** langs TypeScript; Python; JavaScript; frontend Next.js; React; React Flow; Tailwind; backend FastAPI; LangChain; db MongoDB; hosting Vercel
- **Tech/APIs:** VS Code API (framework, core); tree-sitter (framework, core); Gemini (ai_model, supporting); LangChain (framework, supporting); MongoDB (database, supporting); React Flow (framework, supporting)
- **Sponsor APIs:** 
- **Repo:** public, commits 119 (before/in/after event: None/None/None), README solid
- **Demo/writeup:** video None, live not_checked, screenshots 6, writeup long, impact claims False
- **Notes:** Custom AST parser and token-estimate heuristic drive inline cost heatmap and one-click refactors; companion Next.js/React Flow dashboard with sandbox and exports.
- **Team size:** 4 | **Confidence:** medium | unverified: event_start; event_end; has_demo_video; ai_types; n_screenshots
- **Links:** [Devpost](https://devpost.com/software/quota-fg4pzi) | [GitHub](https://github.com/dwseoh/Quota)

### ReelJobs  (DeltaHacks 12)

- **Prizes:** Third Place: Corsair Keyboard [3rd]  (tier: overall_top3)
- **Pitch:** Mobile app that turns job listings into short vertical videos you swipe through, with semantic matching to your profile.
- **Problem / user:** Job hunting means reading walls of text and repetitive applications, unlike effortless short-form video browsing. / job seekers
- **Domain / idea type:** productivity_workplace + creative_media / twist_on_known_app
- **Platforms / hardware / AI:** mobile_cross / False / llm_chat; recommendation; speech_or_voice; generative_media; rag_or_search
- **Stack:** langs Python; TypeScript; frontend React Native; Expo; backend FastAPI; Docker; Playwright; db MongoDB Atlas; hosting Vultr; DigitalOcean Spaces
- **Tech/APIs:** Google Gemini (ai_model, core); MongoDB Atlas (database, core); Fish Audio (ai_model, supporting); Whisper (ai_model, supporting); ffmpeg (other, core); Vultr (cloud, supporting); Expo (framework, core)
- **Sponsor APIs:** 
- **Repo:** public, commits 154 (before/in/after event: None/None/None), README detailed
- **Demo/writeup:** video True, live none, screenshots 5, writeup medium, impact claims False
- **Notes:** Pipeline scrapes jobs, generates 15-30s videos with TTS and ffmpeg, streams via HLS; three FastAPI microservices, vector search for matching.
- **Team size:** 4 | **Confidence:** medium | unverified: event_start; event_end; ai_types; tech_items.depth
- **Links:** [Devpost](https://devpost.com/software/reeljobs) | [GitHub](https://github.com/Scr4tch587/DeltaHacks12)


## DeltaHacks XI

### GitAgent  (DeltaHacks XI)

- **Prizes:** Third Place: Digital Camera [3rd]; [MLH] Best Use of GenAI [unknown]; Build an AI agent with Cohere [unknown]  (tier: overall_top3)
- **Pitch:** AI agent for GitHub repos that searches code semantically, refactors, comments and writes READMEs using an LLM.
- **Problem / user:** Maintaining and improving repositories involves tedious repetitive tasks like refactoring and documentation. / developers and software teams
- **Domain / idea type:** dev_tools + ai_agents_infra / automation_or_agent
- **Platforms / hardware / AI:** web / False / llm_chat; rag_or_search; agent_or_tool_use
- **Stack:** langs Python; frontend Streamlit; backend FastAPI; db ; hosting Streamlit Cloud
- **Tech/APIs:** Cohere Command R+ (ai_model, core, sponsor); GitHub API (other, core); FastAPI (framework, supporting); Streamlit (framework, supporting)
- **Sponsor APIs:** Cohere | fit: Built the agent on Cohere's Command R+ model with document-based RAG for code analysis and generation.
- **Repo:** public, commits 15 (before/in/after event: None/None/None), README solid
- **Demo/writeup:** video True, live not_checked, screenshots 9, writeup medium, impact claims False
- **Notes:** Solo build using Cohere Command R+ with document RAG over repo contents and GitHub API integration; Streamlit front end.
- **Team size:** 1 | **Confidence:** medium | unverified: event_start; event_end; n_screenshots; writeup_length
- **Links:** [Devpost](https://devpost.com/software/gitagent) | [GitHub](https://github.com/SuperMK15/GitAgent)

### Layoff Evaders  (DeltaHacks XI)

- **Prizes:** Second Place: YUNZII AL66 Wireless Mechanical Keyboard [2nd]  (tier: overall_top3)
- **Pitch:** VR fitness game where you play a software engineer dodging office hazards and an evil boss by doing real exercises.
- **Problem / user:** Tech workers sit too long and exercise is dull; gamified workouts with workplace humor can make fitness fun. / tech workers and VR fitness players
- **Domain / idea type:** entertainment_games + health_wellness / entertainment_or_game
- **Platforms / hardware / AI:** other; web / True / False
- **Stack:** langs C#; Python; frontend Unity; Streamlit; backend ; db Firebase Realtime Database; hosting 
- **Tech/APIs:** Unity (framework, core); Meta VR headset (hardware_part, core); Firebase (database, supporting); Streamlit (framework, supporting)
- **Sponsor APIs:** 
- **Repo:** public, commits 59 (before/in/after event: None/None/None), README solid
- **Demo/writeup:** video True, live not_checked, screenshots 9, writeup medium, impact claims False
- **Notes:** Unity VR game detecting exercises via controller motion tracking, with Firebase stat storage and a Streamlit dashboard; satirical layoff-themed obstacles.
- **Team size:** 4 | **Confidence:** medium | unverified: event_start; event_end; ai_used; platforms; n_screenshots
- **Links:** [Devpost](https://devpost.com/software/layoff-evaders) | [GitHub](https://github.com/martin226/layoffevaders)

### WhaleBeing  (DeltaHacks XI)

- **Prizes:** First Place: Nintendo Switch + Nord Securities Bundle [1st]; Dyson Innovation Challenge [unknown]  (tier: overall_top3)
- **Pitch:** Web app that predicts blue whale habitat and shows how ship routes overlap with it so vessels can slow or reroute.
- **Problem / user:** Ship strikes kill many whales yearly, though slowing or rerouting ships could avoid most of them. / shipping operators and marine conservationists
- **Domain / idea type:** sustainability_climate / data_or_analytics
- **Platforms / hardware / AI:** web / False / predictive_ml
- **Stack:** langs Python; JavaScript; frontend React; Tailwind; backend Flask; Node.js; db ; hosting Azure
- **Tech/APIs:** Searoutes API (data_source, core); Azure (cloud, supporting); Flask (framework, supporting); Habitat ML model (other, core)
- **Sponsor APIs:**  | fit: Also won the Dyson Innovation Challenge; page does not state how it matched that track.
- **Repo:** public, commits 70 (before/in/after event: None/None/None), README solid
- **Demo/writeup:** video True, live not_checked, screenshots 7, writeup medium, impact claims True (Cites up to 20,000 whales killed per year by ships globally.)
- **Notes:** Habitat prediction model adapted from a 2019 research paper, translated from R to Python; combined with Searoutes API route data on a web map.
- **Team size:** 4 | **Confidence:** medium | unverified: event_start; event_end; sponsor_apis_used; n_screenshots; writeup_length
- **Links:** [Devpost](https://devpost.com/software/whalebeing-27sj0w) | [GitHub](https://github.com/lucasliao0403/WhaleBeing)
