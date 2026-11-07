# DivHacks — DivHacks 2026 (2 projects)

### RentEscrow
*DivHacks DivHacks 2026 · dataset: sponsor · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** Winner Sponsor Challenge: Capital One [The Best Use of Nessie]

**What it is:** A web app where tenants and landlords share one case per repair issue, with photo evidence, AI evidence summaries, iMessage updates, NYC housing records and a simulated rent escrow that settles on XRPL Testnet.
**Problem / user:** Tenants and landlords in NYC whose repair disputes drag on with scattered photos and unanswered messages and no clear record; housing advocates named as test users.

**Features**
- Tenant and landlord dashboards with shared repair cases — Each repair issue becomes a case both sides follow through progress states. *[shown_working]*
- Evidence upload with timestamps — Photos and documents stored in MongoDB GridFS attached to the case. *[shown_working]*
- Gemini evidence analysis — Gemini interprets uploaded evidence and writes observations to support review; not the payment decider. *[claimed]*
- iMessage coordination — A separate messaging worker on Photon Spectrum relays repair updates between tenant and landlord phones. *[claimed]*
- NYC HPD complaint and violation lookup — Pulls public NYC Open Data housing records into the case context. *[claimed]*
- Simulated rent escrow with Nessie sandbox — Nessie sandbox supplies account verification, balances and rent history; in-app USD escrow balances are simulated. *[claimed]*
- Conditional settlement on XRPL Testnet — Signed agreements and application rule checks gate payments; guards against unauthorized or duplicate payouts. *[claimed]*

**Flow:** Report a repair issue as a tenant → Upload photos and documents as evidence → AI summarizes observations for review → Landlord and tenant exchange updates in app or iMessage → Tenant confirms the repair is done → Settlement released under signed-agreement rules on testnet

**Prompt:** Capital One sponsor challenge, Best Use of Nessie: a broad finance prompt (payments, smarter shopping, accessible financing, financial literacy) with the Nessie sandbox API as an optional tool.
**Fit (explicit):** README states Nessie sandbox data is used for account verification, balances and rent history behind the rent escrow flow.  *(targeted: Capital One Best Use of Nessie, Ripple agentic finance on XRPL, Photon Agents in iMessage, MLH Gemini, MLH MongoDB Atlas, Hack The City)*
**Sponsor tools:** Capital One Nessie API (account verification, balances and rent history for simulated escrow, supporting); Photon Spectrum (iMessage tenant-landlord messaging worker, supporting)
**AI:** Gemini analyzes uploaded repair evidence and produces observations; settlement itself follows deterministic application rules and signed-agreement permissions.
**Architecture:** Next.js web app with server routes on Railway; separate messaging worker for Photon Spectrum; MongoDB plus GridFS; calls to Gemini, NYC HPD open data, Nessie sandbox and XRPL Testnet via settlement rule checks.
**Novelty:** Combines five sponsor integrations (Nessie, Photon, Gemini, MongoDB, XRPL) around a niche tenant-repair dispute workflow with guarded settlement.
**Scope:** large · working: Live Railway deployment, demo video, tests directory and docs; README states escrow is simulated. · polish: Logo, mermaid architecture diagram, .env example, tailored README and separate worker deployment.
**Claims:** Working prototype linking repair report, evidence review, tenant confirmation and guarded settlement | Cites a Brooklyn dispute with about $24,000 returned by court order as motivation
**Gaps:** video content not viewed; screenshot count unknown
Sources: https://devpost.com/software/rentescrow-nthfwb, https://github.com/mujtaba-atif/divhacks1

---

### unsaid
*DivHacks DivHacks 2026 · dataset: sponsor · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** Winner Sponsor Challenge: Capital One [The Best Use of Nessie]

**What it is:** An iMessage agent that plans a group dinner by chatting privately with each person, proposing budgets from their Nessie spending history, negotiating a venue that fits everyone, and sending an iMessage poll and final map-linked plan.
**Problem / user:** Friends in New York planning outings, especially those on tight budgets who hesitate to state budget or diet limits in a group chat.

**Features**
- Private 1:1 intake with join codes — Host texts a plan, others send JOIN plus a four-character code and answer location, time, travel, diet, budget in their own DM. *[shown_working]*
- Budget suggestion from Nessie spending — Dinner-like purchases from the Nessie sandbox yield a proposed budget the user can accept or override; seeded ledgers if no key. *[shown_working]*
- Grok reply parsing — Grok via the OpenAI SDK extracts typed fields from messy replies; deterministic resolvers handle times, money, diet and run alone if Grok is down. *[shown_working]*
- Constraint negotiation engine — Per-person agents score venues and concede in rounds; picks the option maximizing worst-case score across the group. *[shown_working]*
- Native iMessage poll and voting — Top three venues go out as a poll; votes by tap, tapback, number or name; ties return to the group. *[shown_working]*
- Final plan fan-out with maps — Winner sent to each DM with a Google Maps pin and transit from that person's home. *[shown_working]*
- Persistent profile and offline venue catalogue — Home, diet and blackouts persist across plans; 1,089 NYC venues from Google Places precomputed into JSON. *[shown_working]*

**Flow:** Host texts the bot a plan → Bot asks constraints and proposes a Nessie-based budget → Host gets a join code and shares it → Friends text JOIN code and answer in their own DMs → Host texts go to start negotiation → Group receives a poll of three venues and votes → Everyone gets the final plan with a map link

**Prompt:** Capital One DivHacks 2026 sponsor challenge, Best Use of Nessie: broad finance prompt (payments, smarter shopping, accessible financing, financial literacy) with Nessie as an optional API.
**Fit (implied):** Uses Nessie purchase history to propose each person's budget instead of asking them to name a number, so spending limits are set privately.  *(targeted: Capital One Best Use of Nessie)*
**Sponsor tools:** Capital One Nessie API (suggest per-person dinner budget from past spending, supporting); Photon Spectrum (iMessage transport, polls, tapbacks, core)
**AI:** Grok (xAI via OpenAI SDK) turns free-text replies into structured fields and scores venues; deterministic resolvers and ranking provide a fallback and the final negotiation logic.
**Architecture:** Spectrum iMessage router with per-person agents and shared types; MongoDB Atlas stores plans, profiles and transcripts; offline Google Places venue JSON; a projector 'backroom' UI reads Mongo.
**Novelty:** Never joins the group thread; agents negotiate privately and pool only lowest budget, combined diet needs and time overlap. Deterministic negotiation with LLM only for extraction.
**Scope:** medium · working: Harness script for end-to-end checks, four screenshots; no video or live demo link. · polish: Detailed README setup table, backroom projector UI, handling of ambiguous replies and tapbacks.
**Claims:** Venue catalogue of 1,089 NYC restaurants and cafes with real opening hours | Negotiation loop converges to a single option, ties go back to group
**Gaps:** no demo video
Sources: https://devpost.com/software/unsaid-zm8w5v, https://github.com/argsdio/unsaid

---

