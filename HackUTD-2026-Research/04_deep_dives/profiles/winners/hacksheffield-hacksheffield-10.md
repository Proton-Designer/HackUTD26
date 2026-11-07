# HackSheffield — HackSheffield 10 (3 projects)

### 2025: A Beer Odyssey
*HackSheffield HackSheffield 10 · dataset: winners · tier: overall_top3 · evidence A · confidence medium*
**Prizes:** HackSheffield10 1st Place [1st]

**What it is:** A group pub-crawl app themed on the Odyssey: a leader sets a start, end and number of pubs, the app generates a random route through real pubs, members can veto stops, and each member's selfie at a pub gets a drunkenness rating and an insult from an LLM.
**Problem / user:** Groups of friends, especially students, wanting a structured and playful pub crawl; the page states no formal problem.

**Features**
- Group creation and route generation — Leader sets start, end and number of pubs; the app builds a random path toward the end with that many stops. *[claimed]*
- Pub-only venue filtering — Google place results were narrowed to pubs after restaurants and leisure venues serving alcohol appeared. *[claimed]*
- Veto of pubs — Members see example pubs and can veto options. *[claimed]*
- Photo challenge — Each member uploads a selfie at the end of every pub and photos are shared with the group. *[claimed]*
- AI drunk rating and insult — A fine-tuned GPT-4o-mini scores each selfie on a drunkenness scale and adds a roast. *[claimed]*
- Distance calculation — Haversine formula computes distances between pub coordinates. *[claimed]*

**Flow:** Leader creates a group and picks start, end and pub count → App shows the generated map path → Members review pubs and veto → At each pub members take a selfie → Group sees shared photos with rating and insult

**Prompt:** HackSheffield 10 had overall placings; no theme or prize wording was fetchable (event page returned an error). The page says the aim was a journey like the Odyssey.
**Fit (implied):** Page frames the app as an Odyssey-style journey and picks a student pub crawl as its realisation; no explicit link to a stated prompt.  *(targeted: HackSheffield10 1st Place)*
**AI:** GPT-4o-mini, fine-tuned by the team, rates selfies on a drunkenness scale and writes an insult; Google venue data and Haversine distance for routing.
**Architecture:** React/JavaScript frontend with Google Maps polyline handling and a Flask backend calling Google place data and the LLM; photos shared per group.
**Novelty:** Playful combination of a generated pub route, group veto and an LLM that judges selfies.
**Scope:** small · working: Repo with separate frontend (41 files) and backend (23 files); screenshots of map path, veto and selfie screens; no live demo. · polish: Standalone UI screens with radix components; repo README is only a placeholder; author notes Devpost story was accidentally deleted.
**Claims:** Tests with sober and drunk selfies tuned the rating until it was mostly accurate
**Gaps:** Devpost story partly deleted by author; Repo README empty so flow comes from Devpost; Event prize wording not fetchable (edition page errored); Repo under a winners organisation; may be a copy
Sources: https://devpost.com/software/2025-a-beer-odyssey, https://github.com/hacksheffield-10-winners/hs10 (evidence; README is a placeholder)

---

### SupplyTrace
*HackSheffield HackSheffield 10 · dataset: winners · tier: overall_top3 · evidence B · confidence medium*
**Prizes:** HackSheffield10 3rd Place [3rd]

**What it is:** A web visualiser where the user enters a product and GPT output is broken into raw materials, refinement steps and components, each placed at a likely industrial hub on an interactive globe-style map with an alternative flow-diagram view.
**Problem / user:** People curious how everyday products are made, since the route from raw materials to finished goods is hard to see.

**Features**
- Product breakdown by GPT — Prompts make OpenAI models list raw materials, refinement processes and components for a product. *[claimed]*
- Geographic linking — Each item is assigned to its most likely industrial location. *[claimed]*
- Interactive map — HTML Canvas draws resources, factories and consumers with curved lines accounting for Earth's curvature and hover detection. *[claimed]*
- Flow diagram view — Alternative diagram of the same supply chain. *[claimed]*
- Analytics dashboard — Total travel distance, carbon footprint and time are listed as future work. *[planned]*

**Flow:** Enter a product name → GPT generates the supply-chain data → Explore it on the interactive map → Switch to the flow diagram

**Prompt:** No prize wording or theme was available for HackSheffield 10; the page names no track.
**Fit (none):** No stated link to a prompt; the project is an open-ended visualisation entry placed third overall.  *(targeted: HackSheffield10 3rd Place)*
**AI:** OpenAI GPT models with engineered prompts return structured lists of materials, components and locations; output is parsed into a linked graph.
**Architecture:** Static HTML/CSS/JavaScript front end calling OpenAI, with custom Canvas plotting for the map and flow views.
**Novelty:** Uses an LLM as the only data source to build a geographic supply chain graph with custom canvas projection code.
**Scope:** tiny · working: Devpost has a demo video and four screenshots; repo not inspectable (clone failed). · polish: Custom curved-line canvas rendering and hover handling; no metrics; accuracy of GPT data unverified.
**Claims:** Turns linear AI output into a linked interactive graph
**Gaps:** Repo clone failed and README fetch failed on raw and github pages; Video not watched; Prize wording not found
Sources: https://devpost.com/software/supply-trace

---

### TripSync
*HackSheffield HackSheffield 10 · dataset: winners · tier: overall_top3 · evidence A · confidence low*
**Prizes:** HackSheffield10 2nd Place [2nd]; [Reply] Multi-Agent AI Challenge

**What it is:** A multi-agent group chat for friends planning a trip, where several AI agents help the group converge on a holiday plan; built with a Python backend, React front end and Supabase on Vercel.
**Problem / user:** Groups of friends for whom getting everyone on board is the hardest part of trip planning.

**Features**
- Group chat with multiple AI agents — Friends chat together while several agents take part in planning the trip. *[claimed]*
- Agent architecture and logs — Screenshots show an agent architecture diagram and run logs but the page does not describe agent roles. *[unclear]*
- Shared state via Supabase — Frontend depends on the Supabase client for chat or group data. *[unclear]*

**Flow:** Friends join a shared chat → Agents contribute suggestions while the group talks → Group refines a trip plan

**Prompt:** Reply Multi-Agent AI Challenge: the page implies a challenge on multi-agent AI; official wording was not found.
**Fit (explicit):** Described as a multi-agent group chat using multiple AI agents and won the Reply Multi-Agent AI Challenge; agent roles are not detailed.  *(targeted: HackSheffield10 2nd Place, Reply Multi-Agent AI Challenge)*
**Sponsor tools:** Reply Multi-Agent AI Challenge (sponsor track) (Multiple cooperating AI agents in a trip-planning chat, unclear)
**AI:** Several AI agents collaborate in a chat; models, frameworks and roles are not named on the page or README.
**Architecture:** React frontend with Supabase client; Python backend (one file in repo); deployed on Vercel.
**Novelty:** Puts agents inside a human group chat rather than a single assistant, but details are thin.
**Scope:** tiny · working: Screenshots of a trial and logs; repo has tiny source (about 760 LOC excluding modules); no demo link. · polish: Very sparse page, empty README; no stated results.
**Gaps:** Page and README give no feature list or flow; Agent roles and models unknown; Reply challenge text not found; Source code not read
Sources: https://devpost.com/software/mu-u86lhg, https://github.com/MuratGuneyKemal/hacksheffield (evidence; README is a title only)

---

