# UofTHacks — UofTHacks - 13 (1 projects)

### Identity Matrix
*UofTHacks UofTHacks - 13 · dataset: winners · tier: overall_top3 · evidence A · confidence high*
**Prizes:** Overall 1st place; Best "UofT" Hack [1st]

**What it is:** A shared 2D multiplayer world where each user uploads an identity (interview plus photos), gets a pixel-art avatar, and has a persistent AI agent that keeps living, talking and forming relationships in the world after they log off.
**Problem / user:** Explores what happens to a person's online presence when they log off; no explicit user named, aimed at players curious about persistent AI stand-ins and social simulation.

**Features**
- Real-time multiplayer world — React and Phaser client with a Node WebSocket server on a 10Hz tick, server-authoritative movement and collision *[shown_working]*
- AI takeover on disconnect — Disconnected avatars continue as AI-controlled agents; positions persist in Supabase *[shown_working]*
- Onboarding interview personality seed — LLM interview (Grok 4 via OpenRouter per Devpost) builds the agent's personality and style *[claimed]*
- Photo to pixel-art sprites — Gemini image model generates sprites and animations, with pixel-level direction detection *[claimed]*
- Utility-based decision engine — Python scores wander, approach, talk, avoid and idle then selects by softmax; LLM writes dialogue only *[claimed]*
- Social memory and needs — Hunger and social needs, memory bank and sentiment signals make agents seek or avoid people *[claimed]*
- Proximity conversations — Players and robots request, accept and hold real-time conversations *[shown_working]*
- Spectator mode — Watch-only /watch view of the world without login *[shown_working]*

**Flow:** Sign up and complete onboarding interview and photo upload → Enter the world and move with WASD → Talk to other players and agents → Log off while the agent continues → Spectators watch relationships develop

**Prompt:** UofTHacks 13 overall 1st prize and Best UofT Hack; judging asks projects to relate to an unnamed event theme; the UofT prize is a bookstore swag bag and ONRamp memberships.
**Fit (none):** Page does not state a theme link; it frames the project as parallel-universe identities persisting online. No explicit UofT tie is stated on the page.  *(targeted: Overall 1st, Best UofT Hack)*
**AI:** LLM (Grok 4 via OpenRouter) for interview, dialogue and sentiment signals; Gemini 3 Pro Image for sprites; non-LLM utility engine chooses actions; LLM never controls movement.
**Architecture:** React/Phaser client; Node WebSocket server (play 3001, watch 3002) with shared pure-TypeScript world engine; FastAPI agent service; Supabase auth, positions, memories and sprite storage.
**Novelty:** Persistent AI doppelganger agents in a server-authoritative game world with a deterministic engine, utility decision-making and social memory, going beyond a chat bot.
**Scope:** large · working: 218-file repo, about 25.8k LOC with tests across five components; team says it actually works; no live link. · polish: Detailed README with architecture and setup; separate better video; README describes simpler robots than Devpost.
**Claims:** Team states real-time multiplayer, persistent agents and conversation all work together | 10Hz server tick | Personality consistency about 80% prompt engineering and memory hygiene
**Gaps:** README describes basic AI robots and pathfinding while Devpost describes LLM personality agents and sprite generation; video not watched
Sources: https://devpost.com/software/temp-sqyptg, evidence/uofthacks-uofthacks-13-identity-matrix.json, https://uofthacks-13.devpost.com/

---

