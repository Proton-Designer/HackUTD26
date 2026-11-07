# WEHack 2026: project cards (2 projects)

Facts and short paraphrases only; no cross-project analysis. Full records are in the workbook and JSONL.

## WEHack 2026

### Miro  (WEHack 2026)

- **Prizes:** Winner CBRE Challenge [unknown]  (tier: sponsor_winner)
- **Pitch:** RAG memory layer for property managers that ingests Gmail, Sheets, voice notes and documents into a searchable intelligence dashboard with tenant heatmaps.
- **Problem / user:** Property managers oversee many assets and lose operational knowledge scattered across inboxes, sheets and notes. / commercial property managers
- **Domain / idea type:** housing_real_estate + ai_agents_infra / automation_or_agent
- **Platforms / hardware / AI:** web / False / rag_or_search; llm_chat; speech_or_voice
- **Stack:** langs Python; JavaScript; frontend React; shadcn/ui; backend FastAPI; SQLAlchemy; db ChromaDB; SQLite; hosting Railway
- **Tech/APIs:** Google Gemini API (ai_model, core); ChromaDB (database, core); ElevenLabs (ai_model, supporting); Google OAuth Gmail and Sheets (auth, core); Google Maps (maps_geo, supporting); FastAPI (framework, core)
- **Sponsor APIs:**  | fit: Built for the CBRE challenge around property-manager workload; the writeup cites CBRE-scale portfolios as motivation and builds a memory system for that persona, without a CBRE API.
- **Repo:** public, commits 40 (before/in/after event: 0/40/0), README detailed
- **Demo/writeup:** video True, live none, screenshots 16, writeup long, impact claims True (Cites estimated portfolio sizes a property manager at large firms oversees as motivation.)
- **Notes:** Multi-layer RAG over Google OAuth read-only Gmail and Sheets data, ElevenLabs voice notes and a Figma-prototyped dashboard; deployed on Railway.
- **Team size:** 4 | **Confidence:** high | unverified: event_end; impact claim detail; ui_polish
- **Links:** [Devpost](https://devpost.com/software/miro-rzbevu) | [GitHub](https://github.com/enayas/wehack26)

### Temp  (WEHack 2026)

- **Prizes:** Winner CBRE Challenge [unknown]  (tier: sponsor_winner)
- **Pitch:** Local LLM agent that reads an Obsidian markdown wiki of property records, weighting legal and financial data above routine maintenance for a property manager.
- **Problem / user:** Property managers juggle many tenants and need an agent that prioritizes high-stakes records over noise. / property managers
- **Domain / idea type:** housing_real_estate + ai_agents_infra / automation_or_agent
- **Platforms / hardware / AI:** web / False / llm_chat; rag_or_search; agent_or_tool_use
- **Stack:** langs Python; JavaScript; frontend React; backend FastAPI; db ; hosting 
- **Tech/APIs:** Gemma 3 via Ollama (ai_model, core); Obsidian markdown wiki (other, core); FastAPI (framework, supporting); React (framework, supporting)
- **Sponsor APIs:**  | fit: Chose the CBRE challenge and modelled a property manager handling many tenants, building an LLM agent with weighted operational priorities over tenant records; no CBRE data used.
- **Repo:** public, commits 20 (before/in/after event: 0/20/0), README solid
- **Demo/writeup:** video True, live none, screenshots 7, writeup medium, impact claims False
- **Notes:** Runs Gemma 3 locally through Ollama over an Obsidian-style hyperlinked markdown wiki, with weighted operational priorities per record type.
- **Team size:** 2 | **Confidence:** high | unverified: event_end; ui_polish
- **Links:** [Devpost](https://devpost.com/software/temp-5aht81) | [GitHub](https://github.com/sachi-jh/we-hack)
