# SunHacks — SunHacks 2025 (1 projects)

### Crises.ai
*SunHacks SunHacks 2025 · dataset: sponsor · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** Winner State Farm - Best Hack for Safety

**What it is:** A disaster-intelligence dashboard for insurers that merges earthquake, wildfire, FEMA, 911 and social-media feeds into one live map with Gemini claim forecasts, customer-density overlays and adjuster need estimates.
**Problem / user:** Insurance carrier claims, underwriting and field teams who cannot combine disaster data fast enough.

**Features**
- Unified live risk map — Layers for USGS quakes, NASA FIRMS fires, FEMA declarations, 911 clusters and social hotspots *[claimed]*
- Claim forecasts — Gemini predicts claims with a heuristic fallback *[claimed]*
- Customer exposure overlays — Density polygons across 18+ metros showing policies at stake (seeded mock data) *[claimed]*
- Adjuster need estimates — Estimates field staffing needs from events *[claimed]*
- Real-time updates — Pollers normalize feeds into Postgres and push through Socket.IO *[claimed]*

**Flow:** Open dashboard map → Toggle event, call, social and polygon layers → Read activity feed → View Gemini predicted claims

**Prompt:** State Farm SunHacks 2025 Best Hack for Safety: build a project that improves safety; no further detail.
**Fit (explicit):** Gives insurers faster disaster awareness; README says it provides situational awareness for State Farm.  *(targeted: State Farm - Best Hack for Safety)*
**AI:** Gemini forecasts claims; AI scoring of social posts; heuristic fallback when AI fails.
**Architecture:** Node/TypeScript pollers write to Postgres via Drizzle; Next.js dashboard with React-Leaflet and Zustand; Socket.IO pushes updates; FastAPI AI service.
**Novelty:** Broad multi-source ingestion with deterministic seeded demo data.
**Scope:** medium · working: Repo with backend, frontend, tests and three screenshots; no video or live link. · polish: Env example, docs and normalized risk math.
**Claims:** 18+ metros of customer polygons
**Gaps:** no video; customer data seeded not real
Sources: https://devpost.com/software/crises-ai, https://github.com/SankrityaT/Crises.ai (evidence README), sponsor_prompts_*.jsonl (SunHacks 2025)

---

