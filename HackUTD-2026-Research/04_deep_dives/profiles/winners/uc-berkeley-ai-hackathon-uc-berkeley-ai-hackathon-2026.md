# UC Berkeley AI Hackathon — UC Berkeley AI Hackathon 2026 (21 projects)

### AeroFreight AI
*UC Berkeley AI Hackathon UC Berkeley AI Hackathon 2026 · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** Best Use of The Agentverse by Fetch AI

**What it is:** A multi-agent freight orchestration system on Fetch.ai uAgents: a user describes an international import shipment in ASI:One chat, and specialist agents assess tariffs, pick air or sea routes, compute landed cost, then take Stripe payment and produce a PDF invoice after approval.
**Problem / user:** Businesses importing goods into the U.S. face freight planning split across routing, cost estimation and payment.

**Features**
- Natural-language shipment intake — Orchestrator converts chat (via ASI:One and a Claude extractor) into structured shipment data and asks follow-ups for missing fields. *[shown_working]*
- Economist agent — Flags high-value cargo, estimates U.S. tariffs and entry taxes, and sets mode to AIR, SHIP or EITHER. *[claimed]*
- Routing agent with air and sea sub-agents — Builds airport or seaport routes with trucking, fees, transit time, picks by speed or cost, using Haversine distance. *[claimed]*
- Landed cost summary — Treasury agent reports mode, route nodes, itemized costs and total landed cost. *[claimed]*
- Stripe checkout and PDF invoice — Embedded Stripe (test) payment then reportlab invoice, optional Drive upload. *[shown_working]*
- Human approval gate — User must confirm before settlement and can reject. *[claimed]*
- Typed agent contracts — Pydantic schemas fix messages between agents, with timeouts and failure handling. *[shown_working]*
- Local mock or remote agents — Teammate agents can run in-process or as remote uAgents on Agentverse. *[shown_working]*

**Flow:** Describe a shipment in ASI:One chat → Answer follow-up questions if details missing → Economist assesses tariffs and mode → Routing agents compute route and cost → Treasury shows landed-cost quote → User confirms and pays via Stripe → Invoice PDF generated

**Prompt:** Fetch AI: build an agent discoverable through ASI:One that takes real action on a real-world problem, beyond a chat interface or light API wrapper; $3,000 across 10 winners.
**Fit (explicit):** Six agents are registered on Agentverse and reachable via ASI:One; the chat triggers a real action chain ending in a payment flow and invoice rather than a bare conversation.  *(targeted: Best Use of The Agentverse by Fetch AI)*
**Sponsor tools:** Fetch.ai uAgents / Agentverse (orchestrator and specialist agents, registered profiles, core); ASI:One (user-facing chat interface, core); Stripe (simulated settlement checkout, supporting)
**AI:** Claude extracts structured shipment fields from natural language; ASI:One is the chat front end; routing, pricing and validation are deterministic Python behind Pydantic contracts.
**Architecture:** Hub-and-spoke: orchestrator coordinates economist, routing (air/ship) and treasury agents over uAgents messaging; FastAPI serves a browser demo; Stripe and reportlab handle payment and invoice.
**Novelty:** Splits logistics into specialist agents with strict typed contracts and a human approval gate before payment, with tests using mocked LLM and Stripe clients.
**Scope:** medium · working: Shared ASI:One chat, two videos and six Agentverse profiles linked; README gives CLI and browser demo steps; pytest suite present. · polish: Architecture write-up, env template, fetchai-asi branch note, slides; about 15k LOC.
**Claims:** Produces a validated route, landed-cost estimate and user-approved settlement | No quantitative metrics reported
**Gaps:** Videos not watched; Freight and tariff data are static datasets; live pricing listed as future work; Claude role only in README
Sources: https://devpost.com/software/aerofreight-ai, evidence/aerofreight-ai (README), https://ai-hackathon-2026.devpost.com/

---

### AgriBroker
*UC Berkeley AI Hackathon UC Berkeley AI Hackathon 2026 · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** Best Use of The Agentverse by Fetch AI

**What it is:** An agent-based produce procurement marketplace: a buyer types a request like 500 tomatoes under $250, and agents discover farms, collect quotes, compute the cheapest split, take payment and return one itemized receipt.
**Problem / user:** Restaurants, co-ops and bulk buyers manually compare suppliers, split orders and pay separately; small farmers have surplus to move.

**Features**
- Natural-language buy request — ASI:One intent parser with local fallback extracts item, quantity and budget. *[shown_working]*
- Seller discovery — Registry agent tracks which farm agents sell which catalog items. *[shown_working]*
- Live quotes from farmer agents — Farmer uAgents hold inventory and prices and answer quote requests. *[shown_working]*
- Cheapest-split optimizer — Deterministic greedy optimizer splits an order across farms under budget. *[shown_working]*
- Payment and payouts — Buyer funds orchestrator via Stripe Checkout; payouts to farms are simulated, with optional testnet FET. *[claimed]*
- Single itemized receipt and agent trace — Returns one combined receipt with a step-by-step trace. *[shown_working]*
- Farmer self-onboarding — New farms join without changing the orchestrator. *[claimed]*

**Flow:** Buyer states intent in chat → Orchestrator asks Registry for sellers → Farmers return quotes → Optimizer picks cheapest split → Buyer funds order → Farms are paid → Receipt returned with trace

**Prompt:** Fetch AI: build an agent discoverable through ASI:One that takes real action on a real-world problem, beyond a chat interface or light API wrapper; $3,000 across 10 winners.
**Fit (explicit):** Agents on Agentverse reachable via ASI:One turn a buying intent into discovery, quoting, payment and receipt, with a verified-brand Flockx seller stretch.  *(targeted: Best Use of The Agentverse by Fetch AI)*
**Sponsor tools:** Fetch.ai uAgents / Agentverse (orchestrator, registry and farmer agents, core); ASI:One (intent parsing and chat entry, core); Flockx Business Agent (verified seller demo with code fallback, supporting)
**AI:** ASI:One parses buyer intent into structured order data; pricing choice is a deterministic optimizer, not an LLM.
**Architecture:** Orchestrator uAgent queries a Registry agent, then farmer agents; optimizer picks the split; payments module simulates Stripe or testnet FET; local deterministic workflow runs without credentials.
**Novelty:** Local deterministic core with live integrations layered on top for demo reliability, and visible agent traces for judges.
**Scope:** small · working: README gives a runnable local demo with expected result ($206 for 500 tomatoes) and readiness-check scripts; demo video and ASI1 chat linked; tests included. · polish: Docs, config of demo farms, Agentverse profile printer; only tomatoes in catalog.
**Claims:** Demo: 500 tomatoes split across two farms for $206 under a $250 budget | Cites USDA ERS estimate that about 30% of U.S. food goes uneaten
**Gaps:** Payouts simulated; hosted deployment not done; Video not watched
Sources: https://devpost.com/software/agribroker, evidence/agribroker (README), https://ai-hackathon-2026.devpost.com/

---

### baymax
*UC Berkeley AI Hackathon UC Berkeley AI Hackathon 2026 · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** Best Use of The Agentverse by Fetch AI

**What it is:** A network of hospital supply agents that predict shortages from weather, illness and camera-counted stock, then negotiate multi-hospital transfers via Fetch.ai agents and settle them as an on-chain testnet payment, driven by a plain-English request in ASI:One.
**Problem / user:** Hospital supply managers: one facility runs short while a nearby one has surplus, and phone coordination is too slow.

**Features**
- Shortage prediction — Fuses Open-Meteo weather, disease.sh illness data and live inventory into forecasts. *[claimed]*
- Edge-vision inventory counts — Claude Vision and OpenCV count stock from camera input. *[claimed]*
- Request broadcast and constrained offers — Front agent broadcasts need; surplus hospitals reply with quantity, ETA, expiry and urgency. *[shown_working]*
- Claude offer ranking and split transfers — Claude ranks offers and composes split plans, re-planning on partial rejection. *[shown_working]*
- On-chain settlement — Fetch Payment Protocol on Dorado testnet; payment card appears in ASI:One chat to sign. *[shown_working]*
- Live dashboard — Redis-backed Flask dashboard shows inventory, alert and negotiation in real time. *[shown_working]*
- Decision tracing — Arize Phoenix logs predictions, rankings and outcomes. *[claimed]*

**Flow:** Manager states shortage in ASI:One → Shortfall detected and request broadcast → Hospitals answer with offers → Claude ranks and splits transfer → User signs testnet payment → Transfer confirmed; dashboard and traces update

**Prompt:** Fetch AI: build an agent discoverable through ASI:One that takes real action on a real-world problem, beyond a chat interface or light API wrapper; $3,000 across 10 winners. README also names the challenge From Intent to Action.
**Fit (explicit):** README states it was built for the Fetch.ai From Intent to Action challenge: one chat intent leads to multi-agent negotiation and a real testnet settlement.  *(targeted: Best Use of The Agentverse by Fetch AI)*
**Sponsor tools:** Fetch.ai uAgents / Agentverse / chat and payment protocols (per-hospital agents, messaging, on-chain payment, core); ASI:One (natural-language entry and payment card UI, core); Arize Phoenix (decision tracing, supporting)
**AI:** Claude Haiku and Sonnet rank offers and plan splits; Claude Vision reads inventory; weather and illness signals feed forecasts; deterministic fallbacks for failures.
**Architecture:** One uAgent per hospital (front, B, C) over Fetch messaging; Redis shared state syncs ASI:One and a Flask dashboard; payments via Fetch Payment Protocol; Phoenix tracing.
**Novelty:** Settles an actual testnet payment after multi-party negotiation and states a scope limit to logistics, never clinical guidance; five sub-teams built against a shared Redis schema.
**Scope:** large · working: Demo video and README describe live end-to-end settlement; about 13k LOC, 175 files, Docker; no tests. · polish: Detailed README, dashboard, tracing, documented bug fixes such as echo filtering.
**Claims:** Live end-to-end settlement demonstrated | No quantitative metrics
**Gaps:** README read only to ~3.5k chars; Video not watched; Hospital data and vision inputs likely simulated; not confirmed
Sources: https://devpost.com/software/baymax-1wumi3, evidence/baymax (README, partial), https://ai-hackathon-2026.devpost.com/

---

### CareLoop
*UC Berkeley AI Hackathon UC Berkeley AI Hackathon 2026 · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** Best Use of The Agentverse by Fetch AI

**What it is:** A voice-first healthcare navigation concierge: a user speaks a health problem, and a set of Fetch.ai agents triage urgency, find real in-network providers, estimate out-of-pocket cost, take a test-mode deposit and book, then read the confirmation back by voice.
**Problem / user:** Patients, elderly people, caregivers and non-native speakers who struggle to work out whom to see, cost, and booking.

**Features**
- Voice or text intake — Browser voice app using Deepgram speech-to-text and text-to-speech, or chat directly in ASI:One. *[claimed]*
- Urgency triage with 911 routing — Claude-based triage with rules sends red-flag symptoms straight to 911, never to booking. *[claimed]*
- Real provider search — Provider agent queries the CMS NPPES registry for nearby providers. *[claimed]*
- Out-of-pocket cost estimate — Cost agent estimates what the patient would pay. *[claimed]*
- Scheduling and payment — Scheduler makes an .ics confirmation; Payment agent takes a Stripe test-mode deposit before booking. *[claimed]*
- Evidence agent — For serious or chronic conditions surfaces ClinicalTrials.gov trials and openFDA drug-safety notes. *[claimed]*
- Seven registered agents with fallbacks — Orchestrator plus six specialists on Agentverse; calls fall back to in-process logic. *[claimed]*

**Flow:** Speak or type a health concern → Triage checks urgency; emergencies go to 911 → Providers found nearby → Cost estimated → Deposit paid and appointment booked → Confirmation read back by voice

**Prompt:** Fetch AI: build an agent discoverable through ASI:One that takes real action on a real-world problem, beyond a chat interface or light API wrapper; $3,000 across 10 winners.
**Fit (explicit):** Orchestrator uses the Agent Chat Protocol so the whole workflow runs from ASI:One, with specialist agents on Agentverse completing booking and payment as real actions.  *(targeted: Best Use of The Agentverse by Fetch AI)*
**Sponsor tools:** Fetch.ai uAgents / Agentverse / ASI:One (seven-agent orchestration and chat entry, core); Deepgram (voice input and output, supporting); Redis (caching and state, supporting); Stripe (test-mode deposit, supporting)
**AI:** ASI:One LLM parses intent and composes replies; Claude does clinical triage under rule-based red-flag guardrails; no diagnosis is attempted.
**Architecture:** Orchestrator agent receives ASI:One chat or REST /voice calls and messages triage, provider, cost, scheduler, payment and evidence agents via Agentverse, with in-process fallbacks.
**Novelty:** Safety-first design: explicit non-diagnosis disclaimer, hard 911 routing, and real public data sources (NPPES, ClinicalTrials.gov, openFDA).
**Scope:** medium · working: README describes a working flow with real APIs; no demo video or live link; no tests. · polish: Detailed architecture diagram and safety notes; about 5k LOC.
**Claims:** Feels like a real access workflow rather than a chatbot | No quantitative metrics
**Gaps:** Devpost names an OpenAI-compatible client while README names Claude and ASI:One; Cost estimation method unknown; No video
Sources: https://devpost.com/software/careloop-gsiy8w, evidence/careloop (README), https://ai-hackathon-2026.devpost.com/

---

### Constructa
*UC Berkeley AI Hackathon UC Berkeley AI Hackathon 2026 · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** Best Use of The Agentverse by Fetch AI

**What it is:** A construction planning platform with two surfaces: a nationwide land-intelligence map that scores sites, and a project workspace where a described build becomes a 3D model, a six-stage timeline with per-stage agents, and auto-filled permit forms.
**Problem / user:** Developers and contracting teams whose projects run late and over budget partly because zoning, permit and compliance rules are hard to navigate.

**Features**
- Land discovery map — Choropleth maps by state and district with feasibility scores built from zoning, hazards, infrastructure and market factors. *[claimed]*
- Live web research — Browserbase browsers scrape listings, permit and zoning signals, with Redis caching. *[claimed]*
- Buy/hold/avoid recommendation — ASI:One orchestrates six custom Agentverse agents to synthesize a site verdict. *[claimed]*
- Natural-language 3D model — ASI:One emits Three.js instructions placing parameterized components (roads, pools, structures) at the site. *[claimed]*
- Six-stage project timeline — Clicking stages from compliance to closeout focuses the 3D camera and shows cost, schedule, regulations and checklist. *[claimed]*
- Per-stage assistant agents — Agents handle daily logs, RFIs, compliance, permit research, hazards and model edits. *[claimed]*
- Permit forms auto-fill — Fills Cal/OSHA DOSH 41-1 and RFI PDFs from project context. *[claimed]*
- Tiered fallbacks and tracing — Consensus, then single agent, then seeded data; Arize records agent spans. *[claimed]*

**Flow:** Explore the national land map and drill into districts → Review site scores and sources → Pick a site and describe the build → View the generated 3D model → Step through timeline stages → Ask stage assistants questions → Click Permit Forms to fill paperwork

**Prompt:** Fetch AI: build an agent discoverable through ASI:One that takes real action on a real-world problem, beyond a chat interface or light API wrapper; $3,000 across 10 winners.
**Fit (explicit):** ASI:One is lead orchestrator over six uploaded Agentverse agents that research, recommend and generate artifacts; Browserbase powers the live web agent scraping.  *(targeted: Best Use of The Agentverse by Fetch AI, Best Use of Browserbase)*
**Sponsor tools:** Fetch.ai ASI:One / Agentverse (lead orchestrator over six agents and 3D component generation, core); Browserbase (live scraping of listings and zoning data, core); Redis (caching map scores, research, models, supporting); Arize (agent call observability, supporting)
**AI:** ASI:One orchestrates multiple agents for site synthesis and constrained 3D component placement; Claude SDK is tagged; low-confidence agents are re-queried once.
**Architecture:** TanStack Start React app with Hono API; Redis cache; optional Python FastAPI agent service; Browserbase scrapers; Three.js and MapLibre front ends; pdf-lib forms.
**Novelty:** Spans site selection through permits in one product, with constrained component dictionary for 3D and real regulatory form filling.
**Scope:** large · working: Deployment disabled for API keys; Devpost has screenshots; large TypeScript codebase with Docker (about 19k LOC). · polish: Landing page with 3D hero, maps, workspace; offline pre-scraped data; no tests.
**Claims:** Cites McKinsey: projects average a year late and 30% over budget | Cites LA study: 25% faster approvals would raise housing production 12.7%
**Gaps:** Devpost fetch says no video, README says demo video on Devpost; Second prize Best Use of Browserbase also shown on page; Unclear which features run on seeded data
Sources: https://devpost.com/software/constructa, evidence/constructa (README), https://ai-hackathon-2026.devpost.com/

---

### Fetch Health
*UC Berkeley AI Hackathon UC Berkeley AI Hackathon 2026 · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** Best Use of The Agentverse by Fetch AI

**What it is:** An educational organ donor-recipient matching simulator: staff upload a patient or donor case, a swarm of public Fetch.ai router agents hands work to a private FastAPI gateway and local agents, and the app returns top three candidates with scores, risks and a voice debrief.
**Problem / user:** Hospital staff, educators and students who need to understand and explain a hard, document-heavy matching workflow; explicitly not for clinical use.

**Features**
- Recipient and donor intake — Staff choose patient or donor and upload documents, images, video and records. *[claimed]*
- Top-three candidate ranking — Shows compatibility percent, organ type, transport time, risks, missing-data warnings and reasoning. *[claimed]*
- Donor eligibility check — Explains ineligibility or adds accepted donors to a database. *[claimed]*
- 80 public Fetch.ai agents plus harness — Thin routers with a master orchestrator that activates only needed agents, discoverable on ASI:One. *[shown_working]*
- Context capsules — Agents pass compact facts, risks and missing fields; exact IDs and scores preserved; prompts compressed by The Token Company. *[claimed]*
- Redis vector retrieval — RediSearch KNN candidate retrieval and semantic cache. *[claimed]*
- Voice debrief and diagrams — Deepgram voice reports; Midjourney education diagrams pre-generated. *[claimed]*
- Truthful degradation — Missing keys or workers return not-configured signals rather than fabricated output; Sentry monitoring. *[shown_working]*

**Flow:** Choose recipient or donor on intake screen → Upload medical files → Loading screen while orchestrator runs agents → Recipient: view top-three candidates and reports → Donor: see added confirmation or ineligibility reasons

**Prompt:** Fetch AI: build an agent discoverable through ASI:One that takes real action on a real-world problem, beyond a chat interface or light API wrapper; $3,000 across 10 winners.
**Fit (implied):** Agents are published as public Fetch.ai uAgents discoverable through ASI:One, fronting a private gateway that does the real analysis; README maps six sponsor integrations.  *(targeted: Best Use of The Agentverse by Fetch AI)*
**Sponsor tools:** Fetch.ai uAgents / ASI:One (80 public router agents and orchestrator harness, core); Redis (vector search, run state, semantic cache, core); The Token Company (prompt compression before Claude, supporting); Deepgram (transcription and voice debrief, supporting); Sentry (monitoring, supporting); Midjourney (education diagrams via proxy, token)
**AI:** Claude extracts fields, explains and narrates reports; matching is transparent rule-based scoring; vector retrieval for candidates; prompt compression reduces tokens.
**Architecture:** Five layers: public Fetch agents, harness, FastAPI HPC gateway, local bureau of worker agents (document parser real, others stubs), and shared integrations; Redis stores state.
**Novelty:** Large generated agent swarm with selective activation and a stated no-faked-output policy; many sponsor tools integrated.
**Scope:** large · working: README has smoke-test script and honest status where workers are stubs; only document parser real; no demo link. · polish: Tests, Docker, sponsor map; repo file count inflated by generated agents (8,972 files, about 18k LOC).
**Claims:** Six sponsor technologies integrated honestly | No quantitative metrics
**Gaps:** Most local workers are stubs per README; No video or live demo; Devpost lists no Redis role beyond storage
Sources: https://devpost.com/software/fetch-health, evidence/fetch-health (README), https://ai-hackathon-2026.devpost.com/

---

### Fireflai
*UC Berkeley AI Hackathon UC Berkeley AI Hackathon 2026 · dataset: winners · tier: sponsor_winner · evidence B · confidence medium*
**Prizes:** Best Use of The Agentverse by Fetch AI

**What it is:** A dispatch-console pipeline that turns a property listing link plus 911 call text into a hazard-annotated, walkable 3D model of the home, a safest-route plan to a trapped occupant, and a multi-agent go/no-go briefing for firefighters before arrival.
**Problem / user:** Firefighters enter burning homes without floor plans or knowledge of where fire and victims are; the 911 call details are lost. Users are crews and the dispatch operator.

**Features**
- Listing photo acquisition — Browserbase stealth browser pulls public real-estate photos; a canned fallback exists if scraping is blocked. *[claimed]*
- 3D and panorama reconstruction — World Labs Marble turns a hero photo into a 3D world, 360 panorama and Gaussian splats. *[claimed]*
- Room graph mapping — Groq Llama 4 Scout vision builds a room-by-room graph with doors, windows and entries. *[claimed]*
- Hazard pinning from 911 text — Fire, smoke, gas and trapped occupants are placed on the panorama at yaw/pitch angles. *[claimed]*
- Safest route planning — NetworkX Dijkstra over rooms weighted by fire and smoke from outside to the victim. *[claimed]*
- Four-agent consensus briefing — Fire, structural, evacuation and personnel agents reach go/no-go, defaulting to undetermined when unsupported. *[claimed]*
- Live dashboard — React/three.js console streams stage progress, with Mapbox incident map and walkable 3D world. *[claimed]*
- LLM-as-judge evals — Arize AX scores each briefing on grounding, actionability, safety and clarity. *[claimed]*

**Flow:** Operator pastes listing link and 911 call text → Pipeline runs acquire, curate, map, reconstruct, hazard, plan, tactical, briefing → Dashboard updates live per stage → Crew sees hazard-annotated 3D model, route and briefing

**Prompt:** Fetch AI: build an agent discoverable through ASI:One that takes real action on a real-world problem, beyond a chat interface or light API wrapper; $3,000 across 10 winners.
**Fit (implied):** Six stage agents plus a coordinator run as Fetch.ai uAgents on Agentverse and can be mentioned from ASI:One, which also parses the call and writes the briefing.  *(targeted: Best Use of The Agentverse by Fetch AI)*
**Sponsor tools:** Fetch.ai uAgents / Agentverse / ASI:One (stage agents, coordinator and briefing writer, core); Browserbase (scraping listing photos past bot protection, core); Arize AX (traces and LLM-judge scores, supporting); Deepgram (tag only; role unexplained, unclear)
**AI:** Groq-hosted Llama 4 Scout vision for curate/map/hazard/tactical; World Labs Marble for 3D; ASI:One parses call and writes briefing; LLM judge scores output; geometry limited to photos to curb hallucination.
**Architecture:** FastAPI streams stage events by WebSocket to a React/three.js dashboard; Browserbase fetch, Groq vision, Marble reconstruction, NetworkX routing, uAgents coordinator, Arize tracing.
**Novelty:** Combines public listing photos with 911 text to produce pre-arrival 3D situational awareness, with explicit anti-hallucination rules and an automated judge.
**Scope:** large · working: Devpost claims an end-to-end pipeline; no demo link, video or readable repo; no metrics. · polish: Detailed pipeline, fallbacks and robustness notes; 58 likes.
**Claims:** End-to-end from link and call to 3D hazard model and go/no-go briefing | Judge catches invented exits | No quantitative metrics
**Gaps:** Repo clone failed; raw README 404 on final-code branch; Aura and Deepgram tags unexplained; Scrapes a real-estate site, scraping terms not discussed
Sources: https://devpost.com/software/fireflai, https://ai-hackathon-2026.devpost.com/

---

### FirstResponder-Relay
*UC Berkeley AI Hackathon UC Berkeley AI Hackathon 2026 · dataset: winners · tier: honorable_or_finalist · evidence B · confidence medium*
**Prizes:** Finalist

**What it is:** A wildfire-emergency overflow system: non-English callers scan a QR code and speak, Claude triages and checks their location against fire perimeters, and human dispatchers see a ranked map and reply in English that is translated and spoken back.
**Problem / user:** 911 lines saturate in disasters, and callers who speak other languages lose time; users are those callers and human dispatchers.

**Features**
- QR phone access — Callers join from any phone by scanning a QR code. *[claimed]*
- Multilingual live transcription — Deepgram nova-3 streaming; 13 languages tested. *[claimed]*
- Claude triage — Sonnet 4.6 labels URGENT, GUIDANCE or INFO, extracts address and detects language. *[shown_working]*
- Fire perimeter check — Mapbox geocoding then Shapely point-in-polygon against three active fire perimeters. *[claimed]*
- Calming spoken reply — System speaks reassurance in the caller's language in about 2 seconds. *[claimed]*
- Dispatcher dashboard — Calls ranked by urgency on a live Mapbox map with transcript and English summary. *[claimed]*
- Two-way translation bridge — Dispatcher types or speaks English; reply is translated and voiced on the caller's phone. *[claimed]*
- Arize tracing — All Claude reasoning traces stream to Arize AX. *[claimed]*

**Flow:** Caller scans QR and speaks → Speech transcribed live → Claude classifies urgency, address and language → Address geocoded and checked against fire polygons → Calming response spoken → Dispatcher sees ranked call on map → Dispatcher replies and translated voice plays back

**Prompt:** Finalist: ten winners, limited-edition tumblers; no description published.
**Fit (none):** No track text applies to a Finalist listing; project is positioned as decision support for dispatchers.  *(targeted: Finalist)*
**Sponsor tools:** Deepgram (multilingual STT and English TTS, core); Arize AX (observability, supporting); Redis Cloud (shared state, supporting); Mapbox (geocoding and map, supporting)
**AI:** Claude Sonnet 4.6 classifies urgency, extracts addresses, detects language and translates; Deepgram nova-3 transcribes; triage is a recommendation for a human.
**Architecture:** Next.js caller and dispatcher views over WebSockets to a FastAPI backend with Redis; Deepgram STT/TTS, Claude, Mapbox and Shapely; deployed on Vercel with ngrok.
**Novelty:** Closes the loop with a two-way translated voice bridge for dispatchers and reports a small eval suite.
**Scope:** medium · working: Live Vercel caller and dashboard links, 30-case eval reported; no repo or video. · polish: Two polished views, map, urgency ranking; fire perimeters are three demo areas.
**Claims:** 90% urgency accuracy, 100% language and address accuracy on 30 cases | Under three seconds end-to-end translation latency | About 2 seconds to calming response | 13 languages tested
**Gaps:** No repo; Live demo not visited; Fire perimeter source undescribed; Eval covers four languages only
Sources: https://devpost.com/software/firstresponder-relay, https://ai-hackathon-2026.devpost.com/

---

### Inspector
*UC Berkeley AI Hackathon UC Berkeley AI Hackathon 2026 · dataset: winners · tier: honorable_or_finalist · evidence A · confidence high*
**Prizes:** Finalist; Hacker's Choice Award

**What it is:** An MCP server that gives a coding agent eyes and hands: it launches the app under test in a sandbox, tests regions of the UI in parallel with computer-use agents, verifies findings by replay, and returns a reproducible fix list tied to source locations.
**Problem / user:** Developers using Claude Code, Cursor or other MCP agents who still have to run, click through and describe bugs in AI-written apps.

**Features**
- MCP tools observe, act, verify — FastMCP server with launch_app and 13+ tools; each action returns a post-action screenshot and changed flag. *[shown_working]*
- Set-of-Mark clicking — OmniParser numbers interactive elements so the agent clicks by id. *[shown_working]*
- Region-parallel testing — A Mapper splits UI into regions and one agent per region tests in isolated sandboxes. *[claimed]*
- Verified findings — Independent replay must agree twice; Merger dedups into a fix list pointing to file and line. *[claimed]*
- Accessibility audit — audit_dom runs axe-core on the live DOM. *[shown_working]*
- Four surfaces — One SurfaceAdapter for web, Electron, Android, iOS; README says web is live, others in progress. *[claimed]*
- Dashboard and bug ledger — Next.js dashboard with runs, replay traces and statuses open/verified/fixing/dismissed. *[claimed]*
- Devin PR integration — Hands findings to Devin to open a pull request. *[claimed]*

**Flow:** Coding agent calls Inspector via MCP → App launches in E2B sandbox → Mapper clusters UI into regions → Region agents test in parallel → Verifier replays and Merger dedups → Findings go to terminal, dashboard or Devin → Agent patches code and Inspector re-verifies

**Prompt:** Finalist: ten winners, limited-edition tumblers. Hacker's Choice Award: one winner, GMMK keyboards. Neither has a published description.
**Fit (none):** No track text published; the project is a developer tool, closest to a tooling track but no stated target.  *(targeted: Finalist, Hacker's Choice Award)*
**Sponsor tools:** Devin (auto-open PRs from findings, supporting); E2B desktop sandboxes (isolated VMs for web and Electron runs, core); Replicate (hosting perception models (role not described), unclear)
**AI:** Claude reasons over screenshots as the computer-use brain; OmniParser (YOLOv8 + Florence-2) detects elements; adversarial test planning and replay verification.
**Architecture:** Host coding agent calls an Inspector control plane (Mapper, Coordinator, Region-Agents, Verifier, Merger) that drives sandboxed adapters; Next.js dashboard reads run traces.
**Novelty:** Parallel region-scoped agents with 2-of-2 replay verification and a unified adapter across web and mobile surfaces.
**Scope:** large · working: README states web proven end to end with 100+ tests; Electron and mobile adapters in progress. · polish: Design docs 01-13, sample buggy apps per surface, doctor command, CI-style Docker; about 21k LOC.
**Claims:** Four platforms with zero platform branching in core | Bug rates up 41% (external stat) | Computer-use replay verification 2-of-2
**Gaps:** Repo named LoopBack; Project name Inspector vs repo name; No video
Sources: https://devpost.com/software/inspector-23ser6, evidence/inspector (README), https://ai-hackathon-2026.devpost.com/

---

### IronBook
*UC Berkeley AI Hackathon UC Berkeley AI Hackathon 2026 · dataset: winners · tier: track_winner · evidence B · confidence medium*
**Prizes:** GRAND PRIZE - Ddoski's Toolbox Track; Finalist

**What it is:** A tool that preserves shop-floor expertise: workers photograph a machine from many angles, the app reconstructs a 3D Gaussian splat, and a Claude agent answers typed or spoken questions by flying the camera to and highlighting parts.
**Problem / user:** New manufacturing technicians who lose out as experienced machinists retire with tacit knowledge.

**Features**
- Guided photo capture — 20+ overlapping photos with a coverage score and gap warnings. *[claimed]*
- 3D Gaussian splat reconstruction — COLMAP with msplat on Apple Metal; fallbacks to MLX CPU and depth-anything 2.5D. *[claimed]*
- Custom WebGL2 viewer — Orbit, walk and fly modes with WASD and mouse. *[claimed]*
- Agent camera control — Claude with vision returns text plus actions like fly_to, look_at, highlight, zoom. *[claimed]*
- Voice questions — Deepgram input for hands-free use. *[claimed]*
- Asset library — Searchable library of scanned assets. *[claimed]*
- Observability — Sentry and Langfuse for errors and LLM traces; health endpoint reports backend. *[claimed]*

**Flow:** Photograph the machine from many angles → Upload; app scores coverage → Pipeline reconstructs the 3D scene → Ask a question by text or voice → Camera flies to and highlights the answer → Scan saved to library

**Prompt:** Ddoski's Toolbox Track: grand prize, $5,000 cash for one winner; no description published. Finalist: limited-edition tumblers.
**Fit (none):** No track text published; a worker-facing tool for capturing and querying equipment knowledge.  *(targeted: GRAND PRIZE - Ddoski's Toolbox Track, Finalist)*
**Sponsor tools:** Deepgram (voice input, supporting); Sentry (error and transaction monitoring, supporting); Langfuse (LLM tracing, supporting)
**AI:** Claude with vision gets a screenshot, camera state and history and returns structured JSON actions; 3D Gaussian splatting from photos; prompt engineering grounds left/right and occlusion.
**Architecture:** React/Vite/TypeScript viewer with custom WebGL2 splat renderer; FastAPI backend runs COLMAP and splat training with three fallbacks; Claude agent bridges to the viewer via an action protocol.
**Novelty:** Builds its own splat renderer and agent-to-camera action protocol; three-tier reconstruction fallback for any machine.
**Scope:** medium · working: Devpost claims working reconstruction (about 24 dB PSNR) and 77 tests; no demo, video or repo. · polish: Detailed technical write-up; conflicting tag lists (Next.js, PyTorch) noted.
**Claims:** About 24 dB PSNR on M-series chips | 77 tests (27 backend, 50 frontend) | Cites 57% of retiring boomers shared less than half their knowledge | Won Ddoski's Toolbox grand prize
**Gaps:** No repo link; Claude version stated as claude-3-5-sonnet; Second built-with list conflicts with first
Sources: https://devpost.com/software/ironbook, https://ai-hackathon-2026.devpost.com/

---

### LifeLink
*UC Berkeley AI Hackathon UC Berkeley AI Hackathon 2026 · dataset: winners · tier: sponsor_winner · evidence B · confidence medium*
**Prizes:** Best Use of The Agentverse by Fetch AI

**What it is:** A multi-agent blood-supply network driven from ASI:One chat: a hospital agent checks stock, discovery and center agents find and quote blood, donor agents handle fresh donations, funds are held in Stripe test escrow, and a custody agent logs a hash-chained trail until verified delivery.
**Problem / user:** Hospital clinicians who need blood fast; the page frames the problem as delivering right units on time amid testing windows, eligibility and cold-chain rules.

**Features**
- Chat requests via ASI:One — A nurse asks in plain language, such as 5 units B+ within 72 hours. *[shown_working]*
- Hospital and discovery agents — Check own inventory then find blood centers for the remainder. *[claimed]*
- Center quotes — Three demo centers return real persisted inventory and pricing tiers. *[claimed]*
- Normal and emergency paths — Normal SLA may use fresh donations; emergency QSLA uses pre-tested stock only. *[claimed]*
- Donor eligibility — Donor agents join when fresh donation is needed. *[claimed]*
- Escrowed payment — Stripe test PaymentIntent held at commitment and captured only on verified delivery. *[claimed]*
- Hash-chained custody trail — Custody agent records dispatch-to-receipt events. *[claimed]*
- Orchestrator and shared state — Authoritative order state avoids double-allocation; MongoDB Atlas event log with JSON fallback. *[claimed]*

**Flow:** Nurse types request in ASI:One → Hospital checks local stock → Discovery finds centers and quotes → Allocation and donor check → Stripe holds funds → Custody agent logs delivery → Payment captured on verified arrival

**Prompt:** Fetch AI: build an agent discoverable through ASI:One that takes real action on a real-world problem, beyond a chat interface or light API wrapper; $3,000 across 10 winners.
**Fit (explicit):** Eleven agents registered on Agentverse with mailbox and Almanac, reachable through ASI:One chat, execute an end-to-end order with payment and custody rather than answering questions.  *(targeted: Best Use of The Agentverse by Fetch AI)*
**Sponsor tools:** Fetch.ai uAgents / Agentverse / ASI:One (11-agent network and chat interface, core); MongoDB Atlas (shared state and event log, supporting); Stripe (test-mode escrow, supporting)
**AI:** ASI:One chat protocol routes requests; Pydantic AI listed but models unspecified; allocation and custody are agent logic rather than a described model.
**Architecture:** Hospital, Discovery, Courier, Center, Donor, Payment and Orchestrator uAgents on Agentverse; MongoDB Atlas state with JSON fallback; Stripe PaymentIntents; React/Vite UI.
**Novelty:** Models the whole blood chain including escrow-until-delivery and tamper-evident custody log, with emergency versus normal SLA paths.
**Scope:** medium · working: Shared ASI:One demo session and 11 agent profiles linked; no repo or video; no metrics. · polish: Rich writeup but challenge section lists headings only.
**Claims:** Full chain runs end to end with no invented orders or inventory | Built in one weekend | Blood supply down 35% in a month (external)
**Gaps:** No repo; AEVs undefined; Demo chat not opened
Sources: https://devpost.com/software/lifelink-soibwr, https://ai-hackathon-2026.devpost.com/

---

### Lucid Voice
*UC Berkeley AI Hackathon UC Berkeley AI Hackathon 2026 · dataset: winners · tier: track_winner · evidence A · confidence high*
**Prizes:** GRAND PRIZE - Ddoski's World Track; Finalist

**What it is:** A local-first assistive communication (AAC) app where a person taps two or three words and receives several full candidate sentences grounded in a personal knowledge graph, then hears the chosen one in a clone of their own voice.
**Problem / user:** People who cannot speak fluently (ALS, aphasia after stroke, autism, cerebral palsy) who communicate at about 8 words/minute on tap-boards and want private, personal, natural speech.

**Features**
- Tap-to-sentence reconstruction — Tapped fragments are anchored to graph nodes; LLM writes three candidate sentences at different lengths and registers; user picks one *[shown_working]*
- Listener-aware register — Detects who is being spoken to and swaps terms of address and tone (daughter vs 4-year-old grandson) for identical input *[shown_working]*
- Personal knowledge graph — Embedded Kuzu graph of people, places, routines, preferences and phrases feeds hybrid GraphRAG retrieval with abstain-if-unsure *[shown_working]*
- Own-voice cloning — Coqui XTTS-v2 zero-shot clone, cache-first playback with system-voice fallback *[claimed]*
- Online learning loop — Confirmed choices reinforce graph edges; consolidation promotes patterns; decay fades unused memories; style model re-ranks candidates *[claimed]*
- 3D hologram brain view — Shows retrieved memories firing along the path that grounded each reply *[shown_working]*
- Build-your-brain interview — AI interviews the user and each answer adds a memory node live, solving cold start *[claimed]*
- Offline/on-device operation — Local Gemma/LM Studio LLM, faster-whisper STT, local embeddings; cloud providers opt-in only *[claimed]*

**Flow:** Tap two or three vocabulary tiles, or capture the partner's speech via mic → System picks the listener and retrieves related memories from the graph → Three candidate sentences appear; tone dial can nudge register → User selects one → Sentence plays in the cloned voice → Choice reinforces the graph and style model → Optionally open /graph to watch memories fire

**Prompt:** Ddoski's World is one of four $5,000 grand-prize tracks; the public page gives no description for it. Finalist also awarded.
**Fit (implied):** No stated link to the track text; project addresses a human-world accessibility problem (speech impairment) with on-device personalization. Also lists Deepgram, Sentry, Arize, Redis tools.  *(targeted: GRAND PRIZE - Ddoski's World Track, Finalist)*
**Sponsor tools:** Redis/RediSearch (local vector search listed in stack, unclear); Deepgram (optional cloud speech-to-text provider, supporting); Sentry (observability, unclear); Arize Phoenix (evaluation, unclear); Anthropic Claude (opt-in cloud LLM provider and dev tool, supporting)
**AI:** Frozen local Gemma (MLX/LM Studio) generates strict-JSON candidates from GraphRAG facts; BGE embeddings; XTTS voice clone; Whisper STT; a preference-trained style model re-ranks choices.
**Architecture:** React/Vite/three.js frontend calls FastAPI backend: retrieval.py (graph+vector GraphRAG), generation.py, style.py, Kuzu graph, learning.py, cache-first /speak, pluggable local/cloud providers.
**Novelty:** Combines a personal memory graph, listener-conditioned phrasing, own-voice cloning and fully offline operation for AAC, with a visible brain visualization of retrieval.
**Scope:** medium · working: 11k LOC repo with run.sh quickstart, documented API endpoints; page reports a working laptop demo offline. · polish: Branded README with logo, 3D visualization, tone dial; no tests.
**Claims:** Closes gap between ~8 wpm tap-boards and ~150 wpm speech | Runs fully offline in airplane mode | Cut response time from ~60s to near-instant by disabling hidden reasoning tokens
**Gaps:** No demo video listed; Track description not public; No user testing reported
Sources: https://devpost.com/software/lucid-voice, evidence/lucid-voice.json (README), https://ai-hackathon-2026.devpost.com/

---

### Paper Cuts
*UC Berkeley AI Hackathon UC Berkeley AI Hackathon 2026 · dataset: winners · tier: track_winner · evidence A · confidence high*
**Prizes:** GRAND PRIZE - Ddoski's Playground Track; Finalist; Best UI/UX

**What it is:** A live creation game: players draw on an iPad or browser, an AI pipeline recognizes the doodle, restyles it into a clean sprite, assigns gameplay mechanics, and drops it into a running phone-controlled platform fighter (Doodle Smash).
**Problem / user:** Young builders and kids who consume games but find engines too hard; wants drawing to become playable creation without code.

**Features**
- Draw surface — tldraw canvas on iPad/browser plus phone-as-pen into shared projected scene *[shown_working]*
- Three-tier doodle recognition — Custom CNN, open-vocabulary VLM, and Redis HNSW vector memory retrieval fused behind a confidence gate *[claimed]*
- Sprite enhancement (Caecae) — Image-to-image model (SD/SDXL, InstructPix2Pix fine-tune trained on Trainium) re-renders doodle as flat bold sprite, then background removal *[claimed]*
- Mechanic composer (Moose) — LoRA-tuned intent model plus safe operation graph maps drawings to mechanics (sword swings, fire projectile, fruit heals, spring launches) *[claimed]*
- Clarification loop — System proposes candidate labels/mechanics and player confirms or corrects *[claimed]*
- Phone gamepads — QR join lobbies, up to 6 phones as controllers via WebSocket relay *[shown_working]*
- Generative KO finishers — Pika video clips via fal.ai triggered on first item grab, pre-baked and cached *[claimed]*
- Game and editor — Smash, King of the Hill, Gem Grab, K.O. Rush on five maps; character drawing rig and stage editor *[shown_working]*

**Flow:** Draw a shape on the iPad canvas or with a phone pen → Recognition names it → Enhanced sprite appears with background removed → Composer proposes a mechanic; player confirms or corrects → Drag object onto live mini-map into the match → Others join via QR on phones and fight → First item grab triggers a generated KO finisher

**Prompt:** Ddoski's Playground is one of four $5,000 grand-prize tracks; no public description. Best UI/UX has no criteria beyond general judging; Redis track rewards use beyond caching.
**Fit (implied):** Playful creation tool turning drawings into game content; page frames Redis vector index as recognition memory not a cache, and a hand-drawn marker aesthetic.  *(targeted: GRAND PRIZE - Ddoski's Playground Track, Finalist, Best UI/UX, Redis (labelled sponsor track on page))*
**Sponsor tools:** Redis Stack (RediSearch HNSW) (Paper Trail doodle memory for retrieval-augmented recognition, core); fal.ai / Pika (generative KO finisher videos, supporting); AWS Trainium (training the image enhancement model, supporting)
**AI:** CNN + VLM + vector kNN recognition; fine-tuned image-to-image sprite model; LoRA intent model feeding rule-based safe mechanic graph; rembg/BiRefNet matting; video generation for finishers.
**Architecture:** Vanilla JS canvas game, React/tldraw draw client, FastAPI backend (rooms, recognition, finishers, Paper Trail), Node WebSocket relay for phones and QR, Redis vector index.
**Novelty:** Full draw-to-playable-mechanic loop with multi-device realtime play, custom Trainium-trained sprite model and safe-by-construction mechanic composition.
**Scope:** large · working: 28k LOC, tests, Docker, docs folder; playable game runs by opening index.html; live demo used hosted inference after losing Trainium access. · polish: Hand-drawn art style, modes/maps, editor; Best UI/UX award.
**Claims:** Sub-500ms enhancement chased as a goal, not reported achieved | Thirteen Devpost likes | Phone controllers up to 6 per lobby
**Gaps:** README title is Doodle Smash and describes the base game; AI pieces from Devpost; No video listed
Sources: https://devpost.com/software/paper-cuts, evidence/paper-cuts.json (README), https://ai-hackathon-2026.devpost.com/

---

### Percept
*UC Berkeley AI Hackathon UC Berkeley AI Hackathon 2026 · dataset: winners · tier: honorable_or_finalist · evidence A · confidence high*
**Prizes:** Finalist

**What it is:** A closed-loop video-ad engine plus a viewer for Meta TRIBE v2 cortical-response predictions: it researches, generates short ads with Pika, predicts attention over time, scores them, and rewrites one creative lever per round, using Redis as memory.
**Problem / user:** Small businesses running short-form video ads who can't afford trial and error and don't learn why an ad failed.

**Features**
- Research and creative plan — Researches product, audience and ad patterns, stores in Redis, then builds a plan (hook, beats, product timing, pacing, CTA) *[claimed]*
- Pika video generation — Custom Pika MCP skills generate the short ad *[claimed]*
- Attention prediction — Meta TRIBE v2 predicts cortical response curve per video *[shown_working]*
- Attention score — Custom layer combines response strength, peak and temporal drop-off *[claimed]*
- One-lever rewrite loop — Agent changes one lever (hook, timing, pacing, motion, CTA), regenerates and rescores *[claimed]*
- Redis context engine — Vector indexes, reward-weighted graph, semantic LLM cache, session memory, video blobs *[shown_working]*
- Cortex explorer UI — WebGL cortex with time-scrubbable response charts and timeline *[shown_working]*
- Ranked versions — Returns versions with scores and explanation of changes *[claimed]*

**Flow:** Describe the ad (product, audience, platform, length) → Research stored to Redis → Plan and first video generated → TRIBE v2 scores response → Agent edits one lever and regenerates → Ranked versions with reasons returned

**Prompt:** Redis track: use Redis for more than caching (agent memory, vector search, retrieval) with originality and solid engineering. Pika: creativity, effective Pika MCP use, output quality. Finalist is an honor.
**Fit (explicit):** README states it is a Best Use of Redis submission and details four vector indexes, graph, semantic cache and video blobs; Pika MCP generates the ads.  *(targeted: Finalist, Best Use of Redis (README submission), Most Creative Use of Pika)*
**Sponsor tools:** Redis / RedisVL (vector RAG, graph, semantic cache, memory, video store, core); Pika MCP (video generation, core); Meta TRIBE v2 (attention prediction, core)
**AI:** Claude agent rewrites plans; Pika generates video; TRIBE v2 predicts neural response; MiniLM embeddings for RAG over ~59 ad-science vectors; YOLO/CLIP for frame search.
**Architecture:** Next.js/three.js front end, Python pipeline and worker services, percept-context and percept-vision MCP plugins backed by Redis, Supabase storage, prediction cache.
**Novelty:** Uses a neuroscience brain-response model as the reward signal for iterative ad generation, with Redis serving as full memory substrate.
**Scope:** large · working: Live demo link on Devpost, 10.7k LOC across several services, tests and Docker. · polish: Detailed README, YouTube video, hosted demo; no CI.
**Claims:** Semantic cache cuts ~40-77s to ~1s on similar brief | Four Redis vector indexes | No benchmarks vs real campaign results
**Gaps:** Page only says Winner Finalist; Redis/Pika prize outcome not shown; Terac folder purpose not read
Sources: https://devpost.com/software/cerebra-diqop9, evidence/percept.json (README), https://ai-hackathon-2026.devpost.com/

---

### Quorum : drop-in validation layer for multi-agent AI Systems
*UC Berkeley AI Hackathon UC Berkeley AI Hackathon 2026 · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** Best Use of The Agentverse by Fetch AI

**What it is:** A validation and consensus layer for Fetch.ai multi-agent workflows: each agent claim passes three validators (source, consistency, reasoning), a weighted consensus accepts, rejects or quarantines it, and a dashboard shows provenance and trust.
**Problem / user:** Developers of multi-agent pipelines where one hallucinating agent corrupts downstream agents; also non-developers via ASI:One chat.

**Features**
- Source validator — Checks claims against web via Browserbase, DuckDuckGo, Wikipedia and APIs like PubMed/EDGAR/OpenWeather *[claimed]*
- Consistency validator — Compares claim to prior accepted claims in Redis per workflow session using Claude *[claimed]*
- Reasoning validator — Claude judges logical soundness, with optional debate round *[claimed]*
- Consensus engine — Weights verdicts by reliability times confidence times evidence quality into accept, needs-review or reject *[claimed]*
- Quarantine and provenance — Holds uncertain claims for human review; immutable audit trail of who said and validated *[claimed]*
- Trust manager — Per-agent and per-validator trust scores updated after each consensus *[claimed]*
- Agentverse deployment — uAgents mailbox agent reachable via ASI:One chat protocol *[shown_working]*
- Live dashboard — Next.js pages for consensus, provenance, trust, quarantine over WebSocket *[claimed]*

**Flow:** Add Quorum agent address to a workflow or chat with it on ASI:One → Submit a claim → Three validators assess it → Consensus verdict returned with breakdown → Quarantined claims reviewed on dashboard

**Prompt:** Fetch AI Agentverse prize: build an agent discoverable through ASI:One that understands intent and takes real action, not a chatbot or thin wrapper.
**Fit (explicit):** Deploys a live Agentverse agent with mailbox and Chat Protocol, discoverable via ASI:One, that validates other agents' claims; README sponsor table maps Fetch, Redis, Anthropic, Browserbase.  *(targeted: Best Use of The Agentverse by Fetch AI)*
**Sponsor tools:** Fetch.ai uAgents/Agentverse/ASI:One (deployment, Bureau demo, chat protocol, core); Redis (workflow state, claim memory, trust, quarantine, core); Anthropic Claude (consistency and reasoning validators, core); Browserbase (web verification, supporting)
**AI:** Claude prompts for contradiction and logic checks; web retrieval for source scoring; no model training.
**Architecture:** Claim enters pipeline of three validators, consensus engine, then state store, quarantine, provenance; FastAPI REST/WebSocket feeds Next.js dashboard; uAgents gatekeeper on Agentverse; Redis with FakeStore fallback.
**Novelty:** Targets trust between agents rather than adding agents, with a drop-in gatekeeper and provenance graph.
**Scope:** medium · working: Live Agentverse agent and ASI:One chat links; 10k LOC with 52 test files. · polish: Four-page dashboard, README diagram, Docker; no benchmarks.
**Claims:** Sub-millisecond Redis cross-claim lookups (unquantified) | Robust under adversarial claims and concurrency
**Gaps:** No accuracy measurements
Sources: https://devpost.com/software/quoram, evidence/quorum.json (README), https://ai-hackathon-2026.devpost.com/

---

### SafeStreets
*UC Berkeley AI Hackathon UC Berkeley AI Hackathon 2026 · dataset: winners · tier: sponsor_winner · evidence B · confidence medium*
**Prizes:** Best Use of Claude

**What it is:** A pin-drop tool that gathers crash records, 311 complaints, news and Street View for a dangerous intersection, uses Claude to find hazards from imagery, and outputs fixes, funding grants, an official to contact, a council letter, a tweet and before/after renders.
**Problem / user:** Residents and advocates who want a city to fix a dangerous intersection but face scattered data and must write letters and find funding.

**Features**
- Pin-drop data gathering — Collects crash data, 311, news and Street View in parallel for the chosen intersection *[claimed]*
- Blind vision analysis — Claude Haiku reviews satellite and Street View images without community data *[claimed]*
- Corroboration pass — Cross-checks findings against crash and 311 data, keeping signals independent *[claimed]*
- Zone-based hazards — Places hazards by named zones such as NW corner instead of pixels *[claimed]*
- Fix and grant matching — Maps each hazard to a remedy and funding program, and identifies who to contact *[claimed]*
- Outputs — Council letter, tweet and before/after renders *[claimed]*
- Live agent feed — Shows what each agent is doing during analysis *[claimed]*
- Two-layer Redis cache — Caches raw scrapes and full analyses only when real data returned *[claimed]*

**Flow:** Drop a pin on the map → Data collected → Blind image analysis → Cross-check with community data → Fixes and grants matched → Receive letter, tweet and renders

**Prompt:** Best Use of Claude: $5,000 credits; projects built with Claude Code tackling big problems in health, education, economic opportunity or similar; ambition and effort over outcome.
**Fit (implied):** Claude Haiku powers two-stage vision analysis and Claude Code built much of it; addresses civic road safety. Page does not explicitly cite the prize text.  *(targeted: Best Use of Claude)*
**Sponsor tools:** Anthropic Claude (two-stage vision analysis and development, core); Browserbase (scraping news and council PDFs, supporting); Redis (two-layer cache, supporting); Fetch.ai uAgents (listed, role undescribed, unclear)
**AI:** Claude Haiku analyzes satellite and Street View images blind, then a second pass reconciles with crash/311 data; image generation (Imagen 4 listed) for renders.
**Architecture:** React/Mapbox front end, FastAPI backend with agents scraping open-data APIs and Browserbase, Redis cache layers, Claude analysis and generation outputs.
**Novelty:** Separates blind visual evidence from resident-reported data to corroborate rather than bias, and ends with a ready-to-send advocacy package.
**Scope:** small · working: No repo or demo linked; page describes pipeline and bugs fixed. · polish: Retro pixel aesthetic described; no screenshots read.
**Claims:** Won Best Use of Claude
**Gaps:** No repo link; No video or demo; Role of Fetch.ai and Imagen unexplained
Sources: https://devpost.com/software/safestreets-h6yprx, https://ai-hackathon-2026.devpost.com/

---

### Sentinel
*UC Berkeley AI Hackathon UC Berkeley AI Hackathon 2026 · dataset: winners · tier: honorable_or_finalist · evidence A · confidence medium*
**Prizes:** Finalist

**What it is:** A security platform aimed at apps built with AI coding tools: connect a repo or URL, agents look for common weaknesses, reproduce them in isolated sandboxes, explain them in plain English, and propose patches (including a GitHub pull request) with an ongoing trust score.
**Problem / user:** Founders, indie hackers and student builders who ship AI-generated apps without security expertise and get noisy, jargon-heavy reports from traditional scanners.

**Features**
- Multi-agent scanning — Coordinator plus specialist agents (secrets, auth, injection, rate limiting, supply chain) run in parallel and a validator dedups *[claimed]*
- Sandbox reproduction — Findings are escalated only when reproduced in an isolated per-scan environment using Browserbase *[claimed]*
- Plain-English explanation — Risk text with visual evidence and a cinematic replay concept *[claimed]*
- Patch generation — LLMs generate fixes and can open a GitHub PR with the patch *[claimed]*
- Trust Score monitoring — Tracks an app's security over time *[claimed]*
- Web dashboard — Next.js app with scan results; Vercel demo link *[shown_working]*
- Edge orchestration — Cloudflare Workers and Durable Objects with Upstash Redis queues and Postgres/Prisma *[claimed]*
- Roadmap items — VS Code extension, SSRF/CSRF/IDOR, org dashboards, Trust Passports *[planned]*

**Flow:** Connect a repo or paste a URL → Agents investigate in parallel → Sandbox confirms which issues are reproducible → Findings explained in plain language → Patch or PR generated → Trust Score tracked over time

**Prompt:** Only Finalist is listed (tumblers). Page lists Browserbase, Fetch.ai, Redis, Sentry tags; Browserbase track asks for web-using agents on its platform.
**Fit (none):** No stated prize target beyond Finalist; uses Browserbase for sandboxed browsing and lists Sentry and Arize observability.  *(targeted: Finalist)*
**Sponsor tools:** Browserbase (live browser-based sandbox simulation, core); Upstash Redis (queues and rate limiting, supporting); Sentry / Arize (observability, supporting); Fetch.ai (tag only, role unexplained, unclear)
**AI:** Claude and OpenAI models drive code-reasoning agents and patch generation; a validator agent requires sandbox proof; README merges three earlier prototypes (VibeAudit, Codebreaker, Synapse).
**Architecture:** Next.js UI, Cloudflare Workers/Durable Objects orchestrate scan agents and sandbox containers, Postgres via Prisma, Upstash queues, GitHub PR integration.
**Novelty:** Pairs vulnerability detection with sandbox reproduction and auto-PR remediation aimed at non-experts; README says it merges three prior projects into one.
**Scope:** large · working: 25k LOC, tests, CI, Vercel demo link; no video; accuracy not reported. · polish: Long README and dashboard; roadmap items such as VS Code extension unbuilt.
**Claims:** Reports only exploits reproduced in sandbox | Generates production-ready patches | No detection accuracy figures
**Gaps:** README says product merges three earlier repos; extent of work done at the event unclear; Security-themed: described at high level, no operational steps recorded
Sources: https://devpost.com/software/sentinel-poyh3v, evidence/sentinel.json (README), https://ai-hackathon-2026.devpost.com/

---

### SnapCycle
*UC Berkeley AI Hackathon UC Berkeley AI Hackathon 2026 · dataset: winners · tier: honorable_or_finalist · evidence A · confidence high*
**Prizes:** Finalist

**What it is:** A mobile app where you photograph a bulky or awkward item, AI identifies it, and the app finds local disposal routes, then acts: fills a hauler's booking form, shows call numbers, or texts several haulers and streams back quotes.
**Problem / user:** College students at move-out and households disposing of mattresses, furniture, electronics or paint who find options scattered across city sites.

**Features**
- Photo identification — Gemini 2.5 Flash identifies item and asks a clarifying question when confidence is low *[claimed]*
- Local guide building — Browserbase crawls local ordinances, programs and haulers into a location RAG in Redis *[claimed]*
- Ranked disposal cards — Donation, city bulky pickup, collectives, HHW/e-waste, paid haulers with cost, eco and distance; priority filter re-sorts *[shown_working]*
- Home-bin triage — Tells user to use trash or recycling when item needs no special pathway *[claimed]*
- Action agent — Simular auto-fills web forms; tap-to-call for city or collective scheduling *[claimed]*
- Hauler bidding — Twilio messages the three closest top-rated haulers with the photo and streams quotes sorted low to high *[claimed]*
- Profile and saved items — Tracks items donated, sold or kept from landfill *[claimed]*
- Observability — Arize Phoenix tracing and Sentry error capture *[claimed]*

**Flow:** Onboard with address and zip → Snap item photo → Confirm or answer clarification → See ranked disposal cards → Tap a card for details and action → Form filled, number shown, or haulers texted → Quotes arrive and item saved

**Prompt:** Only Finalist (tumblers) listed; page names sponsor APIs (Browserbase, Redis, Simular, Arize, Sentry, Twilio) without stating a prize target.
**Fit (implied):** Page says five sponsor APIs integrated; Simular track asks meaningful use of Simular products; no explicit prize claim.  *(targeted: Finalist)*
**Sponsor tools:** Browserbase (crawling local disposal programs, core); Redis (cache, location RAG vectors, agent state, core); Simular (executing form-filling actions, supporting); Arize Phoenix (tracing and prompt tuning, supporting); Sentry (error capture, supporting); Twilio (hauler SMS bids, supporting)
**AI:** Gemini vision identifies items; RAG over crawled local data; two cooperating agents research card details and decide action mode; Claude Code used for planning.
**Architecture:** Expo/React Native app with Supabase; FastAPI backend endpoints (research, identify, triage, disposal-options, card-detail) orchestrating Gemini, Browserbase, Redis RAG, Twilio.
**Novelty:** Goes from finding disposal info to executing it (form fill, multi-hauler SMS bidding) and builds a per-ZIP local knowledge base.
**Scope:** medium · working: 13k LOC mobile app plus backend with Docker; demo video on Devpost; no tests. · polish: Mobile-first UI, live-updating quotes, README flow diagram.
**Claims:** Survey of 87: 89% unaware of disposal services, 58% would use one | Claims first to help complete disposal, not only find info
**Gaps:** Page says Winner Finalist without a specific prize
Sources: https://devpost.com/software/rrr-s98zwc, evidence/snapcycle.json (README), https://ai-hackathon-2026.devpost.com/

---

### StudForge
*UC Berkeley AI Hackathon UC Berkeley AI Hackathon 2026 · dataset: winners · tier: honorable_or_finalist · evidence A · confidence high*
**Prizes:** Finalist

**What it is:** A compiler-style pipeline that turns a plain-English or voice prompt for a multi-robot course into a typed scene, converts it to stud-based brick geometry, validates and repairs it, exports USD-style formats, and runs a light swarm simulation with a lineage report.
**Problem / user:** Robotics and simulation developers who need validated, collision-free, connected multi-robot training environments rather than hand-placed geometry or unreliable generated scenes.

**Features**
- Prompt to SceneSpec — Claude with schema-constrained generation compiles text or voice into typed contracts *[shown_working]*
- Voice input — Deepgram nova-3 live transcription with typed fallback; frontend exists, backend routes unfinished per README *[planned]*
- Advisory visual prior — Midjourney MCP preview may nudge walls but cannot bypass validation *[claimed]*
- Brick compression planners — Deterministic strategies plus learned Qwen2.5-1.5B LoRA path *[claimed]*
- Validator suite with repair — Checks connectivity, collision and coverage with bounded repair loops *[shown_working]*
- Exports — USD canonical scene, SDF/URDF/MJCF stand-ins as JSON *[claimed]*
- Swarm sim and observers — Scripted multi-robot run; coverage, coordination, collision observers write to Redis memory *[shown_working]*
- Lineage report — JSON and HTML report of compiler, compression, validation and swarm metrics *[shown_working]*

**Flow:** Enter prompt such as a 4-robot search-and-rescue maze → Compiled to SceneSpec → Optional visual preview → Brick geometry compressed and validated → Exports generated → Swarm simulation runs → Open lineage report

**Prompt:** Finalist only listed. Page shows Claude, Deepgram, Midjourney MCP, Redis, Trainium integrations; Best Physical AI (UFB) track covers code closing loop with simulated robots or generating training worlds.
**Fit (none):** Generates simulated multi-robot training scenes; page does not name a prize target.  *(targeted: Finalist)*
**Sponsor tools:** Anthropic Claude (scene compilation and robot policy generation, core); Deepgram nova-3 (voice prompt transcription, supporting); Midjourney MCP (advisory visual priors, supporting); Redis Cloud (observer agent memory, supporting); AWS Trainium (initial Qwen fine-tune, lost mid-event, supporting)
**AI:** Claude compiles prompts and policies; Qwen2.5-1.5B LoRA learns compression; observer agents write findings to Redis memory with validator-gated recall.
**Architecture:** Typed Pydantic contracts through compiler, visual prior, assembly, compression, USD scene, validators, exports, sim, report; FastAPI/Typer backend, React/Three.js frontend.
**Novelty:** Treats generative output as advisory, passing everything through deterministic validators and typed contracts; bricks as simulation geometry.
**Scope:** large · working: 20k LOC, pytest suite, offline smoke pipeline; no live demo or video; playback and voice backend unfinished. · polish: PRD, CLI, fixture-mode 3D frontend; USD still JSON stand-ins.
**Claims:** Zero coverage error and single connected component in sample run | Health reporting across nine integrations
**Gaps:** Winner Finalist label without specific prize
Sources: https://devpost.com/software/studforge, evidence/studforge.json (README), https://ai-hackathon-2026.devpost.com/

---

### Theracat
*UC Berkeley AI Hackathon UC Berkeley AI Hackathon 2026 · dataset: winners · tier: track_winner · evidence A · confidence high*
**Prizes:** GRAND PRIZE - Ddoski's Lab Track; Finalist; SkyDeck Grand Prize Winner

**What it is:** A hardware prototype for anxiety and panic support: a wrist band with an accelerometer streams motion, a Random Forest flags agitation, and the system responds with paced haptic breathing and a plush cat whose ears move and that speaks calming prompts.
**Problem / user:** People having anxiety or panic attacks who cannot operate a phone app in the moment; later direction for children and families.

**Features**
- Wrist motion sensing — ESP32 with MPU6050 streams accelerometer over BLE *[shown_working]*
- Agitation classifier — Moving-average filter, sliding windows, time/frequency features, Random Forest trained on simulated calm vs agitated data *[shown_working]*
- Haptic paced breathing — Wrist motor drives slow contract-release rhythm when elevated patterns persist *[claimed]*
- Plush cat ears — Two ESP32-controlled motors move ears on stress detection *[claimed]*
- Voice companion — ElevenLabs voice with Claude conversation, check-ins and grounding skills like physiological sigh *[claimed]*
- Safety screening — Risk-language detection routes to 988 crisis support *[claimed]*
- Adaptive breathing coach — Exhale length lengthens as detected stress rises (README) *[claimed]*
- Personalization — Adapts to user's motion pattern *[planned]*

**Flow:** Wear the band, no action needed → Motion streams to host → Model sees rising arousal → Wrist haptic breathing starts → Cat ears move and cat speaks or guides grounding → Risk language triggers 988 referral

**Prompt:** Ddoski's Lab is one of four $5,000 grand-prize tracks, no public description. SkyDeck Grand Prize gives guaranteed admission to the Pad-13 incubator.
**Fit (implied):** Hardware-plus-AI mental health prototype; next steps reference a Berkeley SkyDeck phase validating feasibility and market fit. Page does not quote track text.  *(targeted: GRAND PRIZE - Ddoski's Lab Track, Finalist, SkyDeck Grand Prize Winner)*
**Sponsor tools:** Anthropic Claude (conversation logic and debugging help, supporting); ElevenLabs (voice in and out, supporting)
**AI:** Random Forest on simulated accelerometer features for calm/agitated; Claude for dialogue and safety check-ins; ElevenLabs speech.
**Architecture:** ESP32 wristband streams BLE/WebSocket to a Python laptop host and orchestrator that scores stress and drives plush motors, haptics and voice.
**Novelty:** Embodied, no-screen intervention combining haptic breathing and a plush companion rather than another phone app.
**Scope:** small · working: 1.3k LOC, firmware and orchestrator; Vimeo demo in README; trained on synthetic data, no user testing. · polish: Physical plush prototype, logo and feature plot screenshots; no tests.
**Claims:** Literature accuracy cited ~91.3% and 78%+, not own results | Prototype does not diagnose anxiety or detect rumination
**Gaps:** Devpost lists no video but README links Vimeo; Model trained on synthetic data
Sources: https://devpost.com/software/theracat, evidence/theracat.json (README), https://ai-hackathon-2026.devpost.com/

---

### Vanguard Telematics
*UC Berkeley AI Hackathon UC Berkeley AI Hackathon 2026 · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** Best Use of The Agentverse by Fetch AI

**What it is:** An edge-sensing system for first-responder vehicles: an STM32 sensor rig and Raspberry Pi 5 on QNX stream accelerometer, vibration, temperature, pressure, proximity and camera data to Redis, a live 3D dashboard, and Fetch.ai agents that detect events and write open-ended incident descriptions.
**Problem / user:** Volunteer fire departments and ambulance crews in low-coverage areas whose vehicle may be in an incident with no operator to radio for help.

**Features**
- Live telemetry dashboard — React/Three.js dashboard with a 3D vehicle model reacting to Redis-stored sensor streams *[shown_working]*
- Per-vehicle baseline anomaly detection — Rolling mean/std and z-scores per sensor *[claimed]*
- Multi-sensor trigger — Flags an event only when several sensors cross thresholds for consecutive samples *[claimed]*
- Pre/post event buffering — Windows passed to downstream agents *[claimed]*
- Agent pipeline on Agentverse — uAgents extract physics features, add vehicle context, LLM writes free-text incident description *[shown_working]*
- Proximity camera — Camera feed activates when object too close *[claimed]*
- Embedded hardware stack — STM32 Nucleo with IKS5A1 sensors feeding Pi 5 running QNX *[shown_working]*
- Off-grid relay — Radio relay attempted, dropped for licensing and interference *[planned]*

**Flow:** Sensors stream to Pi 5 on QNX into Redis → Dashboard shows live data and 3D model → Trigger agent checks baselines → Downstream agents describe the incident → Judges explore via Agentverse agents and ASI:One shared chats

**Prompt:** Fetch AI Agentverse: build an agent discoverable via ASI:One that understands intent and takes real action. QNX: product must run QNX on embedded hardware, cannot-fail real-time reliability, creative AI use.
**Fit (explicit):** Three Agentverse agents with shared ASI:One chats; sensors run on QNX embedded hardware.  *(targeted: Best Use of The Agentverse by Fetch AI, Best Use of QNX (Devpost shows Winner; README says 1st place))*
**Sponsor tools:** Fetch.ai Agentverse/ASI:One (multi-agent incident pipeline, core); QNX on Raspberry Pi 5 (real-time sensor host, core); Redis (live telemetry store, core); Deepgram (listed in tags, role undescribed, unclear)
**AI:** Deterministic z-score signal processing in the edge layer; OpenAI LLM for open-ended incident synthesis in agents.
**Architecture:** STM32 sensors to Pi 5 (QNX) to Redis stream; FastAPI backend and React dashboard; Fetch.ai agents on Agentverse read Redis, extract features, synthesize descriptions.
**Novelty:** Real embedded sensor hardware with real-time OS and agents, separating deterministic detection from LLM description.
**Scope:** large · working: 34k LOC including STM32 firmware and samples, backend, frontend; live agents; no video, no tests. · polish: 3D dashboard and pitch deck link; accuracy not measured.
**Claims:** 82% of US fire departments are mostly volunteer (background) | Brought up real sensors on real-time OS within a weekend | No accuracy or latency figures
**Gaps:** Queue lists only Agentverse prize; Devpost also shows QNX winner; README claims 1st place QNX plus Fetch honorable mentions, Devpost says winner for both
Sources: https://devpost.com/software/vanguard-telematics, evidence/vanguard-telematics.json (README), https://ai-hackathon-2026.devpost.com/

---

