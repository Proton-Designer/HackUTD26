# QHacks: project cards (6 projects)

Facts and short paraphrases only; no cross-project analysis. Full records are in the workbook and JSONL.

## QHacks 2025

### LUNA  (QHacks 2025)

- **Prizes:** First Place: PS5 Slim Digital [1st]; Nord Security Bundle [unknown]  (tier: overall_top3)
- **Pitch:** Wearable ESP32-based device aimed at assisting blind and low-vision users, with a Node.js backend and machine-learning component.
- **Problem / user:** Over a billion people live with vision loss, and the team wanted an assistive wearable for daily navigation. / blind and low-vision people
- **Domain / idea type:** accessibility + health_wellness / hardware_gadget
- **Platforms / hardware / AI:** hardware; web / True / predictive_ml
- **Stack:** langs C++; JavaScript; frontend ; backend Node.js; Express.js; db ; hosting 
- **Tech/APIs:** ESP32 (hardware_part, core); Arduino (hardware_part, core); Express.js (framework, supporting); machine learning (ai_model, unclear)
- **Sponsor APIs:** 
- **Repo:** public, commits 16 (before/in/after event: None/None/None), README solid
- **Demo/writeup:** video True, live none, screenshots 9, writeup long, impact claims True (Cites global vision-loss figures (over a billion affected) and fear-of-blindness research as motivation.)
- **Notes:** Inspiration cites global vision-loss statistics and a research study; hardware built on ESP32/Arduino; exact sensing method not confirmed from the text read.
- **Team size:** 4 | **Confidence:** medium | unverified: event_start; event_end; ai_types; platforms
- **Links:** [Devpost](https://devpost.com/software/luna-nblywg) | [GitHub](https://github.com/Valagit12/Qhacks2025)

### NextBid  (QHacks 2025)

- **Prizes:** Third Place: Keychron V1 Keyboard [3rd]; Nord Security Bundle [unknown]  (tier: overall_top3)
- **Pitch:** Tinder-style auction marketplace where buyers swipe right to bid and an AI algorithm recommends items; sellers list goods.
- **Problem / user:** Traditional auctions feel outdated, so the team wanted a faster, more engaging buyer-seller experience. / online buyers and sellers
- **Domain / idea type:** retail_consumer + entertainment_games / twist_on_known_app
- **Platforms / hardware / AI:** web / False / recommendation; llm_chat
- **Stack:** langs JavaScript; HTML; CSS; frontend Next.js; React; Tailwind; backend Node.js; db SQLite; hosting AWS
- **Tech/APIs:** OpenAI (ai_model, supporting); Clerk (auth, supporting); AWS (cloud, supporting); SQLite (database, supporting); Next.js (framework, core)
- **Sponsor APIs:** 
- **Repo:** public, commits 5 (before/in/after event: None/None/None), README detailed
- **Demo/writeup:** video False, live none, screenshots 9, writeup long, impact claims False
- **Notes:** Swipe interface applied to bidding with AI-curated item feed; no demo video listed on the page.
- **Team size:** 4 | **Confidence:** medium | unverified: event_start; event_end; ai_types
- **Links:** [Devpost](https://devpost.com/software/next-bid) | [GitHub](https://github.com/ela202/QHacksAuction)

### TLDR.AI  (QHacks 2025)

- **Prizes:** Second Place: Meta Quest 3S [2nd]; Nord Security Bundle [unknown]  (tier: overall_top3)
- **Pitch:** Chrome extension that reads the terms and conditions on a signup page and summarizes the risky or unfair clauses for the user.
- **Problem / user:** Nobody reads lengthy legal terms, so users unknowingly accept unfair clauses and data-privacy risks. / everyday web users
- **Domain / idea type:** civic_legal + safety_security / twist_on_known_app
- **Platforms / hardware / AI:** browser_extension / False / llm_chat
- **Stack:** langs Python; HTML; CSS; frontend HTML5; CSS; backend FastAPI; db ; hosting 
- **Tech/APIs:** OpenAI (ai_model, core); Cohere (ai_model, core); FastAPI (framework, core); Figma (other, supporting)
- **Sponsor APIs:** 
- **Repo:** public, commits 54 (before/in/after event: None/None/None), README solid
- **Demo/writeup:** video True, live none, screenshots 11, writeup long, impact claims False
- **Notes:** Uses two LLM providers (OpenAI and Cohere) behind a FastAPI service; Figma used for design.
- **Team size:** 4 | **Confidence:** medium | unverified: event_start; event_end; tech_items.Cohere.is_sponsor
- **Links:** [Devpost](https://devpost.com/software/tldr-ai-amuh73) | [GitHub](https://github.com/pooriaahmadi/qhacks2025)


## QHacks 2026

### Atlas  (QHacks 2026)

- **Prizes:** Second Place [2nd]  (tier: overall_top3)
- **Pitch:** Pick a place on a 3D globe and talk by voice to an AI guide that takes you into an immersive scene of that location in history.
- **Problem / user:** People can read about history but rarely feel what a place and time were like. / learners and history enthusiasts
- **Domain / idea type:** education + entertainment_games / creative_tool
- **Platforms / hardware / AI:** web / False / llm_chat; speech_or_voice; generative_media
- **Stack:** langs Python; TypeScript; frontend React; Vite; Three.js; Globe.gl; Spark.js; backend FastAPI; WebSockets; db ; hosting 
- **Tech/APIs:** Gemini (ai_model, core); World Labs (ai_model, core); Gradium (ai_model, supporting); Three.js (framework, core); Globe.gl (framework, core); CARTO (maps_geo, supporting); FastAPI (framework, supporting)
- **Sponsor APIs:** 
- **Repo:** public, commits 36 (before/in/after event: None/None/None), README thin
- **Demo/writeup:** video True, live none, screenshots 0, writeup medium, impact claims False
- **Notes:** Combines a Globe.gl globe, World Labs generated 3D scenes rendered with Spark.js/Three.js, and a voice guide over websockets; page shows no screenshots.
- **Team size:** 2 | **Confidence:** medium | unverified: event_start; event_end; ai_types; tech_items.depth
- **Links:** [Devpost](https://devpost.com/software/atlas-m8yot1) | [GitHub](https://github.com/MatthewLones/QHacks-2026)

### Orca  (QHacks 2026)

- **Prizes:** First Place [1st]  (tier: overall_top3)
- **Pitch:** Agentic AI music tool that turns hummed or tapped musical ideas into produced tracks while keeping the artist in control.
- **Problem / user:** Enthusiast musicians have melodies in their heads but lack a way to turn them into real music. / hobbyist musicians and producers
- **Domain / idea type:** creative_media + ai_agents_infra / creative_tool
- **Platforms / hardware / AI:** web / False / agent_or_tool_use; generative_media; speech_or_voice; llm_chat
- **Stack:** langs Python; TypeScript; frontend Next.js; backend FastAPI; MCP; db ; hosting 
- **Tech/APIs:** Gemini (ai_model, core); ElevenLabs (ai_model, supporting); Hugging Face (ai_model, supporting); MCP (framework, core); FastAPI (framework, core); Next.js (framework, core)
- **Sponsor APIs:** 
- **Repo:** public, commits 40 (before/in/after event: None/None/None), README detailed
- **Demo/writeup:** video True, live none, screenshots 7, writeup long, impact claims False
- **Notes:** Uses MCP-based agent tooling plus ElevenLabs and Hugging Face models; longest writeups in this batch (about 1000 words).
- **Team size:** 3 | **Confidence:** medium | unverified: event_start; event_end; ai_types; tech_items.depth
- **Links:** [Devpost](https://devpost.com/software/orca-4po0nm) | [GitHub](https://github.com/Beebdoles/qhacks-2026)

### Willow  (QHacks 2026)

- **Prizes:** Third Place [3rd]  (tier: overall_top3)
- **Pitch:** Voice-driven computer assistant that helps elderly users operate technology by speaking instead of using keyboard and mouse.
- **Problem / user:** Seniors struggle with modern interfaces they did not grow up with, limiting their access to technology. / elderly computer users
- **Domain / idea type:** accessibility + social_community / social_good
- **Platforms / hardware / AI:** desktop / False / speech_or_voice; agent_or_tool_use
- **Stack:** langs Python; C++; JavaScript; PowerShell; Shell; frontend CSS; backend ; db ; hosting 
- **Tech/APIs:** ElevenLabs (ai_model, core); PyInstaller (other, supporting)
- **Sponsor APIs:** 
- **Repo:** public, commits 39 (before/in/after event: None/None/None), README solid
- **Demo/writeup:** video True, live none, screenshots 5, writeup long, impact claims False
- **Notes:** Packaged as an installable desktop tool via PyInstaller with PowerShell/shell scripts; ElevenLabs used for voice; page text does not confirm the exact LLM used.
- **Team size:** 4 | **Confidence:** medium | unverified: event_start; event_end; ai_types; platforms
- **Links:** [Devpost](https://devpost.com/software/willow-8f5wqn) | [GitHub](https://github.com/regularpooria/willow_qhacks2026)
