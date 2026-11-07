# DubHacks: project cards (2 projects)

Facts and short paraphrases only; no cross-project analysis. Full records are in the workbook and JSONL.

## DubHacks 2026

### Fluffy  (DubHacks 2026)

- **Prizes:** Photon: Best Voice Agent [unknown]  (tier: sponsor_winner)
- **Pitch:** Camera-driven home assistant for elderly care that labels the scene with a vision model, infers needs and triggers tool calls like dimming lights or texting a caretaker.
- **Problem / user:** Elderly people living at home need proactive help for instinctive needs without issuing explicit commands. / elderly people and their caretakers
- **Domain / idea type:** health_wellness + accessibility / automation_or_agent
- **Platforms / hardware / AI:** web / False / vision; agent_or_tool_use; speech_or_voice
- **Stack:** langs Python; JavaScript; frontend React; backend ; db ; hosting 
- **Tech/APIs:** Photon API (telecom, supporting, sponsor); Perceptron Mk 1.5 VLM (ai_model, core, sponsor); Spotify API (other, supporting); ElevenLabs (ai_model, supporting); Grok (ai_model, token, sponsor); Cursor (other, supporting); React (framework, supporting)
- **Sponsor APIs:** Photon API; Perceptron Mk 1.5; Grok; ElevenLabs | fit: Targeted Photon's Best Voice Agent challenge; used the Photon API to send emergency texts to caretakers as one of several tool calls, alongside Perceptron vision inference.
- **Repo:** public, commits 41 (before/in/after event: 0/41/0), README detailed
- **Demo/writeup:** video True, live none, screenshots 13, writeup long, impact claims False
- **Notes:** Pivoted from a planned robotic-arm project after not getting the hardware; built entirely in Cursor; Grok voice plan dropped when credits were unavailable.
- **Team size:** 2 | **Confidence:** high | unverified: sponsor_apis_used depth
- **Links:** [Devpost](https://devpost.com/software/fluffy-xq8lgp) | [GitHub](https://github.com/edwinthemathman/dubhacks26-Fluffy/branches)

### restock  (DubHacks 2026)

- **Prizes:** Photon: Runner Up [unknown]  (tier: sponsor_winner)
- **Pitch:** iMessage assistant for shared households: text what you ran out of, get ranked live-price options, and checkout splits the bill among roommates.
- **Problem / user:** Roommates coordinate restocking across group chat, store apps and payment apps, and someone ends up fronting money. / roommates in shared households
- **Domain / idea type:** retail_consumer + fintech_finance / automation_or_agent
- **Platforms / hardware / AI:** bot_or_chat / False / llm_chat; agent_or_tool_use
- **Stack:** langs TypeScript; JavaScript; frontend ; backend Node.js; Express.js; db SQLite; hosting Railway
- **Tech/APIs:** Photon (telecom, core, sponsor); Stripe (payments, core); SerpApi (data_source, core); Veyzl (other, unclear); SQLite (database, supporting); Railway (cloud, supporting); Express.js (framework, supporting)
- **Sponsor APIs:** Photon | fit: Photon runner-up: used Photon to run the whole product as an iMessage agent that parses roommate texts, returns shopping options and sends private payment texts.
- **Repo:** public, commits 316 (before/in/after event: 0/314/2), README detailed
- **Demo/writeup:** video True, live not_checked, screenshots 1, writeup long, impact claims False
- **Notes:** Entire flow lives in an iMessage thread; shows its shared-vs-personal decisions in each reply; splits bills via per-member cards or owner-covered IOU texts.
- **Team size:** 4 | **Confidence:** high | unverified: writeup_sections
- **Links:** [Devpost](https://devpost.com/software/restock-n5hxgo) | [GitHub](https://github.com/aknotwell/restock)
