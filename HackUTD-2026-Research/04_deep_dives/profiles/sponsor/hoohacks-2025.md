# HooHacks — 2025 (1 projects)

### Morpheus
*HooHacks 2025 · dataset: sponsor · tier: sponsor_winner · evidence A · confidence medium*
**Prizes:** Best Artificial Intelligence (OpenAI credits + 1yr NordVPN/NordPass/Incogni + 1GB Saily)

**What it is:** A personal second-brain note app that is meant to give AI agents persistent context about the user. It has a rich note editor, AI tags and summaries, a knowledge graph, semantic search, a Chrome clipper, and a custom MCP server so Claude can query the notes.
**Problem / user:** Makers, researchers and deep thinkers who must re-explain themselves to every new AI tool because there is no persistent context layer.

**Features**
- WYSIWYG note-taking and collection — Tiptap-based rich editor with a notes collection view. *[claimed]*
- AI auto-tagging and summaries — OpenAI GPT-3.5 tags and summarizes each note. *[claimed]*
- Knowledge graph — Vis.js graph visualizes how notes and ideas connect over time. *[claimed]*
- RAG semantic search — Notes embedded in a vector store and retrieved by similarity. *[claimed]*
- Daily prompts — Prompts shown on the home page to encourage reflection. *[claimed]*
- Chrome extension — Saves and clips links and content into the notes. *[claimed]*
- MCP server for agents — Exposes the user's context as an API so Claude can query the second brain. *[claimed]*

**Flow:** Write or clip notes → Notes are auto-tagged and summarized → Explore them in the knowledge graph → Search semantically → Connect Claude through the MCP server to query the notes

**Prompt:** not public / not found
**Fit (implied):** General AI track with no specific brief; project is an LLM and embedding-based knowledge tool with an MCP interface for agents.  *(targeted: Best Artificial Intelligence)*
**Sponsor tools:** OpenAI API (Summaries, tagging and embeddings (prize included OpenAI credits), core)
**AI:** OpenAI GPT-3.5 summarizes and tags notes; embeddings in a vector store power RAG search; an MCP server lets external agents like Claude read the context.
**Architecture:** React/TypeScript client with Tailwind and Tiptap, Node/Express server on Neon Postgres, OpenAI calls, Vis.js graph, a Chrome extension and an MCP server over the note store.
**Novelty:** Frames notes as a portable context layer for agents via MCP rather than only a human notes app.
**Scope:** large · working: About 16k LOC across client and server; team says it was built in about 16 hours; no demo or video. · polish: Six screenshots; repo has no README; extension and MCP server claimed working.
**Claims:** Built in about 16 hours by two developers plus AI helpers
**Gaps:** Repo has no README; MCP server and extension not located in file tree; No prize brief beyond general AI
Sources: https://devpost.com/software/morpheus-nu26ai, https://github.com/dayumsam/morpheus

---

