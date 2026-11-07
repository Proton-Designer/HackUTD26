# Hacklanta: project cards (2 projects)

Facts and short paraphrases only; no cross-project analysis. Full records are in the workbook and JSONL.

## Hacklanta 2026

### Ingineer  (Hacklanta 2026)

- **Prizes:** [Photon] Agents in iMessage - Winner [unknown]  (tier: sponsor_winner)
- **Pitch:** iMessage agent named Ing that turns a group idea into a scheduled plan, coordinating times and options and using a cloud browser to act.
- **Problem / user:** Making plans with friends stalls in endless group-chat back-and-forth before anything gets booked. / friend groups making social plans
- **Domain / idea type:** social_community + productivity_workplace / automation_or_agent
- **Platforms / hardware / AI:** bot_or_chat; web / False / agent_or_tool_use; llm_chat
- **Stack:** langs TypeScript; JavaScript; SQL; frontend Next.js; HTML; CSS; backend Node.js; WebSockets; db PostgreSQL (Neon); hosting Vercel
- **Tech/APIs:** Photon (telecom, core, sponsor); ClawMessenger (other, unclear); E2B (cloud, supporting); Neon PostgreSQL (database, supporting); Next.js (framework, supporting); Vercel (cloud, supporting)
- **Sponsor APIs:** Photon | fit: Won Photon's Agents in iMessage track by building a coordinator agent on Photon that users text directly for group planning, with screenshots and results returned in the thread.
- **Repo:** private_or_missing, commits None (before/in/after event: None/None/None), README None
- **Demo/writeup:** video True, live not_checked, screenshots 1, writeup long, impact claims False
- **Notes:** Main coordinator agent receives texts via Photon; browsing work runs in a sandboxed cloud browser (E2B) and returns screenshots and results through iMessage.
- **Team size:** 4 | **Confidence:** high | unverified: writeup_sections; repo_clone_failed
- **Links:** [Devpost](https://devpost.com/software/ingineer) | [GitHub](https://github.com/workoholyguy/Ingenium)

### Safeword  (Hacklanta 2026)

- **Prizes:** [Photon] Agents in iMessage - Runner Up [unknown]  (tier: sponsor_winner)
- **Pitch:** Personal-safety companion you text over iMessage when walking alone; a single agent keeps you talking, loops in contacts and gives a dispatcher facts by voice, without placing 911 calls itself.
- **Problem / user:** Panic buttons need a free hand and are conspicuous; many people fear walking alone at night and want discreet, low-friction help. / people walking alone, esp. students and women
- **Domain / idea type:** safety_security + social_community / social_good
- **Platforms / hardware / AI:** bot_or_chat / False / agent_or_tool_use; speech_or_voice; llm_chat
- **Stack:** langs JavaScript; frontend ; backend Node.js; db ; hosting 
- **Tech/APIs:** Photon Spectrum (iMessage) (telecom, core, sponsor); ElevenLabs (ai_model, core); Twilio (telecom, supporting); Claude (ai_model, core); Node.js (framework, supporting)
- **Sponsor APIs:** Photon Spectrum | fit: Runner-up in Photon's Agents in iMessage track: Photon Spectrum puts one agent behind the iMessage thread as the product's only user entry point, with voice via ElevenLabs/Twilio.
- **Repo:** none_listed, commits None (before/in/after event: None/None/None), README None
- **Demo/writeup:** video True, live none, screenshots 16, writeup long, impact claims True (Cites Gallup and AAU survey statistics on fear of walking alone and campus sexual contact.)
- **Notes:** Writeup argues the product has no front door without Photon and no voice without ElevenLabs; uses Twilio for calling; states software never contacts 911 itself.
- **Team size:** 4 | **Confidence:** high | unverified: writeup_sections
- **Links:** [Devpost](https://devpost.com/software/safeword-3ef01z)
