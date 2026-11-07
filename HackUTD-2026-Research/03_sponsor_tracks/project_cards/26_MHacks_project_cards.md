# MHacks: project cards (5 projects)

Facts and short paraphrases only; no cross-project analysis. Full records are in the workbook and JSONL.

## MHacks 2026

### CoClip  (MHacks 2026)

- **Prizes:** Best Use of Spacetime [unknown]  (tier: sponsor_winner)
- **Pitch:** Google-Docs-style collaborative video editor, forked from OpenCut, where several editors and a Gemini assistant work on the same timeline in real time via SpacetimeDB.
- **Problem / user:** Collaborative video tools exist, but few let humans and AI edit the same project live. / video editors and creative teams
- **Domain / idea type:** creative_media + productivity_workplace / creative_tool
- **Platforms / hardware / AI:** web / False / agent_or_tool_use; llm_chat
- **Stack:** langs TypeScript; frontend OpenCut fork (React); backend SpacetimeDB; db SpacetimeDB; hosting Vercel; SpacetimeDB Maincloud
- **Tech/APIs:** SpacetimeDB (shared timeline/media state, presence) (database, core, sponsor); Google Gemini (tool-calling assistant) (ai_model, core); OpenCut (open-source editor) (framework, core); Vercel (cloud, supporting)
- **Sponsor APIs:** SpacetimeDB | fit: Synchronized the video timeline, media and project state through a SpacetimeDB module hosted on its cloud so edits propagate live, including cursors, permissions and shared state, targeting Best Use of Spacetime.
- **Repo:** public, commits 39 (before/in/after event: 0/39/0), README detailed
- **Demo/writeup:** video True, live not_checked, screenshots 3, writeup long, impact claims False
- **Notes:** Forks the open-source OpenCut editor and syncs timeline, media and app state through SpacetimeDB Maincloud; adds live cursors, read/write permissions and exposes editor tools to Gemini; idea pivoted from collaborative prompting.
- **Team size:** 4 | **Confidence:** high | unverified: ui_polish; n_screenshots
- **Links:** [Devpost](https://devpost.com/software/coclip) | [GitHub](https://github.com/anuragsk05/CoClip)

### Concierge  (MHacks 2026)

- **Prizes:** Photon iMessage Agents Track Winner [unknown]  (tier: sponsor_winner)
- **Pitch:** AI operations assistant for solo small-business owners: the owner texts over iMessage while a voice agent phones vendors such as repair shops on their behalf.
- **Problem / user:** Solo business owners lose mornings calling vendors one by one when something breaks, with no staff to delegate to. / solo small-business owners
- **Domain / idea type:** productivity_workplace + ai_agents_infra / automation_or_agent
- **Platforms / hardware / AI:** bot_or_chat / False / agent_or_tool_use; speech_or_voice; llm_chat
- **Stack:** langs TypeScript; SQL; frontend ; backend ; db ; hosting 
- **Tech/APIs:** Photon (iMessage) (telecom, core, sponsor); ElevenLabs (ai_model, core); OpenAI (ai_model, core); Cursor (other, supporting)
- **Sponsor APIs:** Photon | fit: Won Photon's iMessage Agents track: Photon carries the owner's side of the product entirely in iMessage while ElevenLabs voice calls reach vendors.
- **Repo:** public, commits 48 (before/in/after event: 0/48/0), README detailed
- **Demo/writeup:** video True, live none, screenshots 16, writeup long, impact claims True (Cites SBA figures: 36.2 million US small businesses, over 80% with no employees.)
- **Notes:** Frames product as two parallel conversations: owner side over iMessage (Photon) and vendor side by phone (ElevenLabs); opens with SBA small-business statistics; built with Cursor.
- **Team size:** 3 | **Confidence:** high | unverified: writeup_sections
- **Links:** [Devpost](https://devpost.com/software/concierge-o38bu5) | [GitHub](https://github.com/sszz01/zero-knowledge-team)

### scalpal.  (MHacks 2026)

- **Prizes:** Best Use of Spacetime [unknown]  (tier: sponsor_winner)
- **Pitch:** Meta Quest 3S surgical-training simulator that runs a full case from voice-based patient history to an open appendectomy with an AI coach, and turns learner motion into robot-training demonstrations.
- **Problem / user:** Surgical practice needs expensive simulators and repetition; robot training lacks cheap demonstration data that learners could generate. / surgical trainees and robotics researchers
- **Domain / idea type:** education + health_wellness / new_category
- **Platforms / hardware / AI:** hardware; web / True / agent_or_tool_use; speech_or_voice; llm_chat; vision; predictive_ml
- **Stack:** langs C#; TypeScript; Python; JavaScript; frontend Unity 6 (Meta XR / OpenXR); Next.js; backend Hono; SpacetimeDB; MuJoCo worker; db SpacetimeDB; hosting Vercel; Cloudflare
- **Tech/APIs:** SpacetimeDB (shared session state, scheduled physiology reducer, WebRTC signaling) (database, core, sponsor); ElevenLabs Agents / Scribe / Flash (ai_model, core, sponsor); Anthropic Claude Sonnet and Haiku (ai_model, core); FinchNode synthetic health records (data_source, core, sponsor); Presage SmartSpectra vitals (other, supporting, sponsor); Meta Quest 3S (hardware_part, core); MuJoCo behavior cloning (framework, supporting); .Tech domain (other, token, sponsor)
- **Sponsor APIs:** SpacetimeDB; ElevenLabs; FinchNode; Presage | fit: Used a SpacetimeDB module with 25 tables and 52 reducers for sessions, attempts, coach transcript, headset commands and WebRTC signaling, plus a scheduled reducer ticking patient physiology so every client sees the same patient state.
- **Repo:** public, commits 632 (before/in/after event: 0/632/0), README detailed
- **Demo/writeup:** video True, live not_checked, screenshots 15, writeup long, impact claims False
- **Notes:** Unity VR app with ElevenLabs voice agents (Claude Sonnet), FinchNode synthetic charts, Presage phone-camera vitals, MuJoCo behavior-cloning robot, and a SpacetimeDB module (25 tables, 52 reducers) with a scheduled physiology tick; TypeScript and C# engines kept in parity by a 41-action golden log.
- **Team size:** 4 | **Confidence:** high | unverified: ui_polish; n_screenshots
- **Links:** [Devpost](https://devpost.com/software/scalpal) | [GitHub](https://github.com/stephenhungg/scalpal)

### Tab: Groupchat Accountant  (MHacks 2026)

- **Prizes:** Photon iMessage Agents Track Winner [unknown]  (tier: sponsor_winner)
- **Pitch:** Expense-splitting bot that joins an iMessage group chat, parses messages like 'groceries $63', computes splits, handles settle-up disputes and shows a live web ledger.
- **Problem / user:** Groups sharing trip and house costs track who owes what in spreadsheets and forget over time; splitting apps live outside the chat. / friend groups, roommates and travel groups
- **Domain / idea type:** fintech_finance + social_community / automation_or_agent
- **Platforms / hardware / AI:** bot_or_chat; web / False / llm_chat; vision; agent_or_tool_use
- **Stack:** langs TypeScript; frontend React; Vite; React Flow; backend Node.js; Zod; db SpacetimeDB; hosting Vercel; SpacetimeDB Maincloud
- **Tech/APIs:** iMessage via Mac bridge (telecom, core); SpacetimeDB (Maincloud) (database, core, sponsor); Capital One Nessie API (payments, supporting, sponsor); Grok (xAI API) and Grok Vision (ai_model, core, sponsor); React Flow (framework, supporting); Vitest (framework, supporting)
- **Sponsor APIs:** SpacetimeDB; Capital One Nessie API; xAI Grok | fit: Won Photon iMessage Agents track, but the page text shows a custom Mac iMessage bridge and no Photon use; it relies on SpacetimeDB as the backend and also lists Nessie and Grok.
- **Repo:** private_or_missing, commits None (before/in/after event: None/None/None), README None
- **Demo/writeup:** video True, live none, screenshots 1, writeup medium, impact claims False
- **Notes:** Writeup describes a Mac bridge that reads enabled group chats and sends replies and tapbacks; SpacetimeDB Maincloud is the source of truth via typed reducers; tests run a simulated group chat against an in-memory DB module.
- **Team size:** 3 | **Confidence:** high | unverified: sponsor_apis_used depth; writeup_sections; repo_clone_failed
- **Links:** [Devpost](https://devpost.com/software/tab-groupchat-finances) | [GitHub](https://github.com/kien-le-trung/Tab_MHacks26)

### Traycer: Food-waste Intelligence  (MHacks 2026)

- **Prizes:** Best Use of Spacetime [unknown]  (tier: sponsor_winner)
- **Pitch:** Phone-camera computer vision reads returned cafeteria trays into per-food waste, carbon, water and cost, then tests menu changes in a 3D simulation of AI diners and offers chef and consultant agents to call.
- **Problem / user:** Dining halls cannot see what food is thrown away or why, so they cannot cut waste or its climate cost. / cafeteria and kitchen operators
- **Domain / idea type:** sustainability_climate + food_nutrition / data_or_analytics
- **Platforms / hardware / AI:** web; mobile_cross / False / vision; agent_or_tool_use; llm_chat; speech_or_voice
- **Stack:** langs Python; TypeScript; JavaScript; frontend React; Three.js; React Three Fiber; Vite; backend FastAPI; Node.js; SpacetimeDB; Pipecat; db SpacetimeDB; SQLite; hosting Vercel; SpacetimeDB Maincloud
- **Tech/APIs:** SpacetimeDB (2 modules, scheduled 200 ms tick, subscriptions) (database, core, sponsor); YOLO-World + OpenCV + ByteTrack (ai_model, core); OpenAI vision / agent diners (ai_model, core); Google Gemini (insight summaries) (ai_model, supporting, sponsor); Relay agents (voice/video) (ai_model, supporting, sponsor); ElevenLabs voices + Scribe (ai_model, supporting, sponsor); Pipecat (framework, supporting); Notability (other, token, sponsor)
- **Sponsor APIs:** SpacetimeDB; Relay; ElevenLabs; Google Gemini API; Notability; Figma | fit: Used SpacetimeDB as the single backend: a reducer rewrites each tray's food rows and recomputes gram, carbon, water and cost totals in one transaction, while a scheduled reducer runs the cafeteria simulation and Relay agents query the same tables.
- **Repo:** public, commits 90 (before/in/after event: 0/90/0), README detailed
- **Demo/writeup:** video True, live not_checked, screenshots 9, writeup long, impact claims True (Cites UNEP/FAO global food waste, emissions and hunger statistics as motivation; reports 14 of 17 vision-model tests passing.)
- **Notes:** Two SpacetimeDB modules (25 tables): camera module stores tray rows and JPEG bytes with transactional totals, and a world module ticks a cafeteria simulation every 200 ms with scheduled reducers; entry also targeted Notability, ElevenLabs, Gemini, Figma and .Tech prizes.
- **Team size:** 3 | **Confidence:** high | unverified: ui_polish; n_screenshots
- **Links:** [Devpost](https://devpost.com/software/traycer-ai-food-waste-intelligence) | [GitHub](https://github.com/anton-3/traycer)
