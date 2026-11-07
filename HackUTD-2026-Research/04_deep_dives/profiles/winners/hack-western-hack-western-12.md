# Hack Western — Hack Western 12 (3 projects)

### FlowBoard
*Hack Western Hack Western 12 · dataset: winners · tier: overall_top3 · evidence A · confidence high*
**Prizes:** Second Place Overall [2nd]

**What it is:** A web storyboard canvas built on tldraw where users sketch on 16:9 frames, add text prompts, and generate video clips with Veo 3.1. Frames linked by arrows form sequences that can keep extending, and clips merge into one video.
**Problem / user:** Creators and storyboarders for whom traditional animation, redrawing and refining every frame, is slow; the page names no specific user.

**Features**
- Sketch-on-frame canvas — Custom 16:9 frame shapes on tldraw let users draw motion instructions directly onto each frame. *[shown_working]*
- Prompt-driven clip generation — Frame sketch plus text prompt sent to Veo 3.1 on Vertex AI to produce the next clip. *[shown_working]*
- Arrow-linked sequences — Arrows connect frames into a story, with video thumbnails shown on the arrows; clips build on prior context. *[shown_working]*
- AI frame enhancement — A Gemini image model refines rough drawings on demand before video generation. *[shown_working]*
- Video merging and playback — Generated clips combine into one final video viewable in a built-in player. *[shown_working]*
- Job queue and storage — Redis queue with polling handles long AI jobs; outputs go to Google Cloud Storage; Supabase auth and credits. *[shown_working]*
- Local persistence — Board data kept in browser IndexedDB. *[claimed]*

**Flow:** Create a 16:9 frame → Sketch a motion idea on it → Optionally enhance the drawing with AI → Add a text prompt and press generate → Link frames with arrows to chain scenes → Merge clips and play the final video

**Prompt:** Hack Western 12 overall prize tiers (first, second, third) are general with no theme text; second place goes to the project judged strong overall.
**Fit (none):** General overall prize; nothing in the page or README ties it to a specific track.  *(targeted: Second Place Overall)*
**Sponsor tools:** Google Vertex AI (Veo 3.1, Gemini 2.5) (Video generation and frame enhancement, core)
**AI:** Veo 3.1 generates clips from sketch frames plus prompts; Gemini-family image model enhances frames; context carried across connected frames. A credits table gates usage.
**Architecture:** React/Vite/tldraw frontend with IndexedDB; BlackSheep Python backend queues jobs in Redis, calls Vertex AI, stores media in GCS; Supabase handles auth and credits.
**Novelty:** Treats video generation as a graph of sketched frames on an infinite canvas, with thumbnails on connecting arrows, rather than a single prompt box.
**Scope:** medium · working: README has demo video and full setup; backend plus frontend about 9.6k LOC. · polish: Auth, credits (autumn-js), job queue and Dockerfile present; no tests or CI.
**Claims:** Videos of any length via continuous extension | Context-aware connected clips | Seamless end-to-end generation
**Gaps:** Devpost names image model as Nano Banana Pro Flash while README says Gemini 2.5; both recorded; No performance metrics
Sources: https://devpost.com/software/flowboard-bdpqzg, https://hack-western-12.devpost.com/, evidence/hack-western-hack-western-12-flowboard.json

---

### komo
*Hack Western Hack Western 12 · dataset: winners · tier: overall_top3 · evidence A · confidence high*
**Prizes:** Third Place Overall [3rd]

**What it is:** A unified workspace search tool that queries Slack and Notion at once, groups matches by topic, and shows Gemini-written short summaries with links back to the sources, plus thread and page previews.
**Problem / user:** Busy startup professionals who lose time searching Slack threads, Notion pages and attachments separately for one piece of information.

**Features**
- Cross-platform search — One query hits Slack Search and Notion Search APIs; users toggle which apps are included; results update as typed with debounce. *[shown_working]*
- AI topic summaries — Gemini groups results by topic and writes 10-20 word summaries with reference links across active apps. *[shown_working]*
- Rich previews — Full Slack threads with replies and complete Notion page content with keyword highlighting and metadata. *[shown_working]*
- File retrieval with OCR — PPTX, PDF and image files are downloaded, OCRed and summarized with nearby messages for context. *[claimed]*
- Notion caching — Pages cached in local SQLite plus in-memory search cache to avoid rate limits; team claims 96% faster search. *[claimed]*
- Landing page and integration picker — Screens for choosing which services to connect; tokens are hardcoded for the hackathon. *[shown_working]*
- More integrations and global hotkey — Drive, Gmail, Discord, GitHub, iMessage, workspaces and a spotlight popup listed as future. *[planned]*

**Flow:** Open the landing page and pick integrations → Type a query such as onboarding slides → Backend queries Slack and Notion and caches Notion pages → Files are downloaded and OCRed with surrounding messages → Results list shows previews on one side and the AI summary on the other → Cmd-click to open the original source

**Prompt:** Hack Western 12 overall prizes are general with no theme text; third place overall.
**Fit (none):** General overall prize; no track targeted.  *(targeted: Third Place Overall)*
**AI:** Gemini summarizes and categorizes search results into topics; OCR extracts file text before summarization. No retrieval index beyond API search and cache.
**Architecture:** Next.js 16 frontend, Express/TypeScript backend with Slack and Notion service wrappers, SQLite cache, Gemini for summaries; deployed at a custom domain.
**Novelty:** Combines federated search of two work tools with file OCR and topic grouping; UI reportedly designed by a non-designer teammate.
**Scope:** medium · working: Live site linked, README with setup and deployment docs, about 14.6k LOC in repo. · polish: Landing page, split-view UI and deploy guides; no tests or CI, auth tokens hardcoded.
**Claims:** Search time reduced by 96% with caching | Integrated Slack and Notion despite thin docs
**Gaps:** Devpost lists searchkomo-style demo domain differently from README live domain (komosearch.tech vs searchkomo.tech); Search-time benchmark method not given
Sources: https://devpost.com/software/komo-4lrjdg, https://hack-western-12.devpost.com/, evidence/hack-western-hack-western-12-komo.json

---

### Vril
*Hack Western Hack Western 12 · dataset: winners · tier: overall_top3 · evidence A · confidence high*
**Prizes:** First Place Overall [1st]; [MLH] Best Use of Gemini API

**What it is:** An AI product design studio: describe or upload a reference to get an editable 3D product model, refine it through a Cursor-style chat, then generate packaging with dielines, textures and artwork and export the files.
**Problem / user:** Non-designers such as event organizers, small businesses and artists who have physical product ideas but no 3D modeling skills, time or budget for a designer.

**Features**
- Text or image to 3D product — Plain-English description or reference image produces an editable 3D model rendered in the browser with Three.js. *[shown_working]*
- Chat-based model editing — Cursor-style panel lets users change shape, form and material by prompt, with a material-control viewer. *[shown_working]*
- AI packaging generation — Generates SVG dielines and parallel Gemini textures for each panel, with structured prompt templates and guardrails. *[shown_working]*
- Panel-level packaging edits — Users target a specific panel or surface for localized edits in a 3D view and a 2D dieline editor. *[shown_working]*
- Export — Product and packaging files exported in standard formats (README lists GLB tooling such as trimesh/pygltflib). *[claimed]*
- Physics, multi-part, manufacturing links — Physics-aware dimensions, multi-material products and ordering prototypes listed as next steps. *[planned]*

**Flow:** Describe a product or upload a reference image → Get an editable 3D model → Refine shape and material through the chat panel → Open packaging view and generate dieline plus artwork → Edit individual panels in 3D or 2D → Export the product and packaging

**Prompt:** MLH Best Use of Gemini API: build AI-powered apps with Google's Gemini API, such as chatbots, research summarizers or content generators. Overall prizes are general.
**Fit (implied):** Gemini generates packaging panel textures and drives design iteration, matching the Gemini prize; the page ties the stack tag to that award.  *(targeted: First Place Overall, MLH Best Use of Gemini API)*
**Sponsor tools:** Gemini API (Image generation for packaging textures and design iteration, core)
**AI:** Gemini generates panel textures and interprets edit prompts with structured templates; a text/image-to-3D generator (TRELLIS listed, fal-client in deps) creates meshes. Parallelized panel generation.
**Architecture:** Next.js/React Three Fiber frontend with 3D viewer, dieline editor and chat; FastAPI backend with product, packaging, panel and dieline services, Redis and Docker.
**Novelty:** Extends text-to-3D to packaging with dielines and per-panel texture editing, framed as Lovable for physical products.
**Scope:** medium · working: README with demo video and architecture; backend has pytest tests; about 13.5k LOC. · polish: Detailed README, Docker, typed stack, shadcn UI.
**Claims:** Real product design in minutes instead of days | Panel-level packaging editing solved | End-to-end prompt to export workflow
**Gaps:** Devpost video id differs from README video id; TRELLIS role not stated on page; inferred from deps (fal-client); README setup section not fully read (truncated at 7000 chars)
Sources: https://devpost.com/software/vril, https://hack-western-12.devpost.com/, evidence/hack-western-hack-western-12-vril.json

---

