# SwampHacks — SwampHacks XI (1 projects)

### Pay Pals
*SwampHacks SwampHacks XI · dataset: sponsor · tier: sponsor_winner · evidence A · confidence medium*
**Prizes:** Winner Best Finance Hack Sponsored By Capital One

**What it is:** Gamified savings-accountability app styled like a prediction market: friends join a lobby, Gemini proposes shared financial goals from their spending profiles, and members wager favors and Solana tokens on who will hit them.
**Problem / user:** College students and young adults who find financial tools unengaging; uses social stakes instead of real money.

**Features**
- Onboarding with Nessie data and wallet — Pulls Capital One Nessie transaction data and generates a Solana wallet. *[claimed]*
- AI user titles — Gemini turns spending patterns into a playful title such as a coffee-lover label. *[claimed]*
- Lobbies and invites — Users create private lobbies and send invite links (Blinks) to friends. *[shown_working]*
- Generated shared goals — Gemini reads the lobby's profiles to propose financial goals. *[claimed]*
- Friend wagers — Participants bet favors/SOL tokens on peers' success; losers settle with real-world favors. *[claimed]*
- 3D visuals — Three.js elements used in the UI. *[shown_working]*

**Flow:** Land and onboard (link Nessie data, wallet) → Add friends → Create or join a lobby → Gemini generates goals → Place wagers on friends

**Prompt:** Capital One Best Finance Hack at SwampHacks XI: open-ended fintech build (payments, smarter shopping, accessible financing, literacy); Nessie mock banking API available; Capital One staff judge.
**Fit (implied):** Uses Nessie transaction data to profile users and a financial-habit game to encourage saving; the writeup lists Capital One data and Solana for validation.  *(targeted: Best Finance Hack Sponsored By Capital One)*
**Sponsor tools:** Nessie API (Transaction history for onboarding and profiling users, supporting)
**AI:** Gemini generates user title labels from Nessie transactions and creates shared goals from lobby profiles; no other models described.
**Architecture:** React/TypeScript/Tailwind/Three.js frontend with FastAPI backend, MongoDB Atlas, Nessie, Gemini and Solana APIs, hosted on Railway.
**Novelty:** Kalshi-style betting reframed as favors and tokens for saving habits; mixes Solana tokens with Nessie data.
**Scope:** small · working: Live Railway link and YouTube video; repo is only ~200 LOC across 16 files. · polish: README with architecture and roadmap, ten screenshots, a 3D GIF.
**Claims:** Users can feel incentivized to save without money
**Gaps:** Token wager mechanics unspecified; Repo seems small relative to claims
Sources: https://devpost.com/software/project-c1nomzfei7a0, evidence/sponsor-swamphacks-swamphacks-xi-pay-pals.json, sponsor_prompts_CapitalOne_StateFarm_CBRE.jsonl

---

