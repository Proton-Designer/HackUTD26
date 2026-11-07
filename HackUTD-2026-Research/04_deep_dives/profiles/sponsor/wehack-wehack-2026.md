# WEHack — WEHack 2026 (2 projects)

### Miro
*WEHack WEHack 2026 · dataset: sponsor · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** Winner CBRE Challenge

**What it is:** A memory layer for commercial property managers that ingests Gmail threads, Google Sheets, voice notes, documents and maintenance photos, extracts tenant and property intelligence with Gemini, and presents a daily ranked briefing, risk heatmap and natural-language Q&A.
**Problem / user:** Property managers whose tenant history is scattered across emails, spreadsheets and memory, so a new manager restarts from zero after a handoff.

**Features**
- Gmail and Sheets ingestion — Google OAuth read-only access; full email threads and spreadsheet data are pulled in *[claimed]*
- Structured memory extraction — Gemini converts unstructured data into tenant risk, maintenance, payment and escalation signals stored for RAG *[claimed]*
- Daily ranked briefing — First screen lists urgent issues, high-risk tenants, recurring problems and follow-ups with context *[claimed]*
- Portfolio heatmap and ranked tenant table — Visual risk and activity map plus sortable urgency table *[shown_working]*
- Natural-language querying — Agent answers questions over history, such as churn-risk tenants or prior agreements *[claimed]*
- Maintenance image analysis — Gemini Vision analyzes uploaded photos and links them to property context *[claimed]*
- Tenant profile view — Per-tenant analysis page *[shown_working]*

**Flow:** Connect Google Workspace → Miro ingests and extracts memory → Open the daily briefing → Check heatmap and ranked tenants → Open a tenant profile → Ask questions or upload a maintenance image

**Prompt:** Build a prototype AI agent or multi-agent system with a deliberate memory design showing how information is created, stored, retrieved, updated and applied so the agent behaves context-aware over time.
**Fit (implied):** Builds institutional memory for property managers: records are ingested, structured, embedded for retrieval and applied in briefings and answers; the writeup cites CBRE portfolio scale as motivation.  *(targeted: CBRE Challenge)*
**AI:** Gemini extracts structured memory from emails, sheets and notes; Gemini Vision reads maintenance photos; pgvector/Chroma-based RAG retrieval feeds an agent for queries and ranking.
**Architecture:** React/shadcn dashboard over FastAPI; Google OAuth ingestion of Gmail and Sheets; Gemini extraction pipeline; vector store for retrieval (README says Supabase pgvector, tags list ChromaDB/SQLite); Railway hosting.
**Novelty:** Frames institutional-memory handoff as the product and includes multimodal maintenance photos and ElevenLabs voice tooling.
**Scope:** medium · working: Repo of about 4.4k LOC with frontend and backend, YouTube demo video, four screenshots; no tests or live link. · polish: Dashboard UI, Figma prototype and README with problem/solution framing.
**Claims:** One property manager may oversee 20-60 properties and 200-500+ tenants (cited as CBRE)
**Gaps:** video not watched; README and tags disagree on vector store
Sources: https://devpost.com/software/miro-rzbevu, evidence/sponsor-wehack-2026-wehack-2026-miro.json

---

### Temp
*WEHack WEHack 2026 · dataset: sponsor · tier: sponsor_winner · evidence A · confidence medium*
**Prizes:** Winner CBRE Challenge

**What it is:** A local LLM agent memory system that stores property-management records as hyperlinked Obsidian markdown files, gives each record a salience score that decays and gets pruned, and combines graph traversal with ChromaDB similarity search to answer questions.
**Problem / user:** AI agents that need persistent, precise memory; demonstrated with a property manager juggling many tenants.

**Features**
- Operational weights — High-stakes legal and financial records are weighted above routine maintenance logs *[claimed]*
- Salience score with decay — Score from importance, relevance and status updates with new info and decays at a rate set by importance *[claimed]*
- Pruning — Low-salience records are dropped so the agent focuses on recent important data *[claimed]*
- Graph of linked records — Obsidian wiki links let the agent follow relationships to answer record-specific queries *[claimed]*
- Hybrid retrieval — ChromaDB vector similarity alongside the markdown vault, with justification records for changes *[claimed]*
- Local agent with demo UI — Gemma 3 via Ollama with a React and FastAPI demo front end *[claimed]*

**Flow:** Property records live in the markdown vault → Ask the agent a question in the demo UI → Agent searches links and vectors, weighted by salience → Answer is returned from retained records

**Prompt:** Build a prototype AI agent or multi-agent system with a deliberate memory design showing how information is created, stored, retrieved, updated and applied so the agent behaves context-aware over time.
**Fit (explicit):** Explicitly built around memory design: creation, scoring, decay, pruning, linked retrieval and update, with a property-manager example; README says it accepted the CBRE challenge.  *(targeted: CBRE Challenge)*
**AI:** Gemma 3 run locally through Ollama as the agent; ChromaDB embeddings plus link traversal for retrieval; salience and decay logic governs which records stay.
**Architecture:** Obsidian-style markdown vault of property records plus ChromaDB; FastAPI backend with local Gemma 3 agent; small React UI.
**Novelty:** Treats memory as scored, decaying, prunable records with human-readable markdown audit trail and fully local inference.
**Scope:** small · working: About 780 LOC plus 58 sample property data files; no demo, video or evaluation; team notes slow local runs. · polish: Minimal demo UI; README is a prose writeup.
**Gaps:** no demo or video; no evaluation of memory behavior
Sources: https://devpost.com/software/temp-5aht81, evidence/sponsor-wehack-2026-wehack-2026-temp.json

---

