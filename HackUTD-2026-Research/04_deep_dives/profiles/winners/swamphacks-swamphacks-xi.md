# SwampHacks — SwampHacks - XI (3 projects)

### OffTrails
*SwampHacks SwampHacks - XI · dataset: winners · tier: overall_top3 · evidence A · confidence high*
**Prizes:** Best Overall Sponsored By Vobile (1st, 2nd, & 3rd Place)

**What it is:** Route planner for off-trail wilderness travel: the user picks start and end points on a Leaflet map and a modified A* search over USGS elevation and Sentinel-2 water and vegetation data finds a low-effort path, shown on the map and downloadable as GPX.
**Problem / user:** Hikers going cross-country must plan carefully because one misjudged route can be dangerous; they need safer, faster routes where no trail exists.

**Features**
- Terrain data ingestion — Pulls USGS topographic data and ESA Sentinel-2 L2A water and vegetation layers, read with rasterio from a released data pack. *[shown_working]*
- Start/end route selection — User sets endpoints in a Leaflet web UI. *[shown_working]*
- Modified A* pathfinding — Cost function from the Minetti 2002 walking energy model (replacing Tobler) plus water and vegetation penalties; AI-optimized for speed. *[shown_working]*
- Route display — Computed route drawn on the map in the web interface. *[shown_working]*
- GPX export — Route downloadable as GPX for use in other map apps via gpxpy. *[shown_working]*
- Hierarchical pathfinding — Multi-pass search at rising resolution to widen radius. *[planned]*

**Flow:** Open web UI → Choose start and end points → Backend runs A* over terrain cost grid → Route appears on map → Download GPX to a map app

**Prompt:** SwampHacks XI Best Overall (sponsored by co-host Vobile): $1,250/$750/$500 for the top three plus MLH pins; the prize page gives no theme beyond the sponsor name.
**Fit (none):** No stated targeting; submitted for the general overall prize. It is a complete safety-oriented routing tool using real geospatial data.  *(targeted: Best Overall Sponsored By Vobile)*
**AI:** AI assistance used to optimize the energy-cost formula so pathfinding runs within interactive limits; no model in the product itself.
**Architecture:** Leaflet front end; Python backend with numpy, rasterio, matplotlib, gpxpy; raster elevation and satellite layers feed a cost grid searched by A*; GPX output.
**Novelty:** Uses a published biomechanical energy-cost model and satellite water/vegetation layers rather than a generic shortest-path over a trail graph.
**Scope:** small · working: Devpost shows a demo video and four screenshots; README points to a data release; no live site. · polish: About 1.9k LOC in 19 files, no tests; README is the Devpost text.
**Gaps:** no benchmarks or example route lengths reported
Sources: https://devpost.com/software/offtrails, evidence/swamphacks-swamphacks-xi-offtrails.json (README), https://swamphacks-xi.devpost.com/

---

### ReStory
*SwampHacks SwampHacks - XI · dataset: winners · tier: overall_top3 · evidence A · confidence medium*
**Prizes:** Best Overall Sponsored By Vobile (1st, 2nd, & 3rd Place)

**What it is:** Wearable memory aid for people with Alzheimer's: a Raspberry Pi 5 streams video and audio to a GPU server that identifies faces and voices, separates speakers, turns conversations into structured notes about each person, and shows a live contact feed on a mobile dashboard.
**Problem / user:** People with Alzheimer's lose context for who they are talking to, causing social anxiety; the tool aims to restore confidence in conversations.

**Features**
- Face plus voice identity fusion — 512-d ArcFace face embeddings and 192-d ECAPA-TDNN voice embeddings stored per contact in ChromaDB. *[claimed]*
- Wearer anchor and diarization — Isolates the wearer voice and separates other speakers in real time. *[claimed]*
- Spatial zone locking — OpenCV tracking keeps identity when faces turn or move. *[claimed]*
- Centroid evolution and silence protection — Keeps voice candidates tied to a face despite acoustic drift instead of creating duplicate contacts. *[claimed]*
- Gemini lore synthesis — Gemini 3 Flash converts diarized WhisperX transcripts into JSON facts merged with prior knowledge. *[claimed]*
- Real-time memory dashboard — React mobile view sorts people by frequency and recency and highlights the current speaker with face. *[claimed]*
- Pi video streaming — Pi camera frames sent as JPEG over WebSocket to a FastAPI server that rebroadcasts to a browser viewer. *[shown_working]*

**Flow:** Wearer starts Pi stream → Server detects faces and voices → Active speaker highlighted on dashboard → Transcripts processed into lore → Person record updates over repeated meetings

**Prompt:** SwampHacks XI Best Overall (sponsored by co-host Vobile): $1,250/$750/$500 for the top three plus MLH pins; the prize page gives no theme beyond the sponsor name. Best Integration of Hardware (Raspberry Pi 5) was also on offer.
**Fit (none):** No stated targeting. A hardware-plus-multimodal-AI accessibility build with a role-play demo of memory updating.  *(targeted: Best Overall Sponsored By Vobile)*
**Sponsor tools:** Gemini API (turning transcripts into JSON lore, supporting)
**AI:** InsightFace ArcFace, SpeechBrain ECAPA-TDNN, WhisperX with diarization and Gemini 3 Flash; linker ties voice to face by co-occurrence; vectors in ChromaDB on an RTX 5090.
**Architecture:** Raspberry Pi 5 streams 30 FPS video and PCM audio over binary WebSocket to a FastAPI GPU backend (PyTorch), ChromaDB store, and React mobile dashboard.
**Novelty:** Combines face and voice embeddings with a wearer-voice anchor on custom edge hardware to build per-person memory notes, going well beyond a face-recognition demo.
**Scope:** medium · working: Devpost reports role-play demo and screenshots of wearable and dashboard; repo README only documents the Pi video streaming piece. · polish: About 2.8k LOC in 63 files with tests; README is narrow vs Devpost claims.
**Claims:** Full pipeline worked end to end across role-play scenarios
**Gaps:** identity pipeline not described in README; no accuracy figures
Sources: https://devpost.com/software/restory, evidence/swamphacks-swamphacks-xi-restory.json (README), https://swamphacks-xi.devpost.com/

---

### SignHero
*SwampHacks SwampHacks - XI · dataset: winners · tier: overall_top3 · evidence A · confidence high*
**Prizes:** Best Overall Sponsored By Vobile (1st, 2nd, & 3rd Place); Best Game Design Project

**What it is:** Rhythm game that teaches ASL fingerspelling: a webcam reads hand landmarks with MediaPipe, a MobileNetV2 model classifies the letter A to Z, and the player must sign letters as notes hit a Guitar Hero style highway, with training, testing and arcade modes.
**Problem / user:** Few hearing people can sign ASL; the project targets hearing learners who want a fun way to practise fingerspelling.

**Features**
- Song Game — Rhythm mode with scrolling note highway, hit windows, combos and streak effects synced to beatmaps. *[shown_working]*
- Real-time sign recognition — MediaPipe landmarks drawn as a mask feed a MobileNetV2 classifier for 26 letters at roughly 30 to 50 ms. *[shown_working]*
- Training Mode — Step-by-step practice with hand pose hints. *[shown_working]*
- Testing Mode — Timed challenges with accuracy tracking and a report. *[shown_working]*
- Whack-A-Sign — Arcade reflex game for quick recognition. *[shown_working]*
- Latency engineering — Landmarks sent as small JSON over a persistent WebSocket to a micro-batching FastAPI server on a GPU. *[shown_working]*
- Mirror-pose accuracy trick — Original and mirrored hands both scored; max confidence wins plus thresholds. *[shown_working]*
- Words and phrases — Dataset generated, training started. *[planned]*

**Flow:** Enter player name → Pick a mode → Grant webcam access → Sign letters as notes arrive → See score, combos, report

**Prompt:** SwampHacks XI Best Overall (sponsored by co-host Vobile): $1,250/$750/$500 for the top three plus MLH pins; the prize page gives no theme beyond the sponsor name. Best Game Design Project: LEGO prize, no description given.
**Fit (implied):** Not stated; it is a game with synthwave visuals and four modes, which maps to the game design category.  *(targeted: Best Overall Sponsored By Vobile, Best Game Design Project)*
**AI:** Trained PyTorch MobileNetV2 CNN on ASL alphabet data plus augmentation; MediaPipe Hands for landmarks; server batches up to 32 frames per 10 ms sweep.
**Architecture:** Next.js 15 game with MediaPipe in browser, tRPC and Prisma/MongoDB for players, WebSocket to FastAPI PyTorch server that returns letter and confidence.
**Novelty:** Turns sign-language recognition into a rhythm game and engineers for under 100 ms play latency with landmark masks and GPU micro-batching.
**Scope:** large · working: README documents four game modes and latency; Devpost update claims dual stream at 60fps under 100 ms; no video link. · polish: About 22k LOC, 1,000+ files, tests, Docker and CI, architecture doc.
**Claims:** About 30 to 50 ms inference latency on localhost | Dual streaming at 60fps with sub-100 ms inference (post-event update) | 48 million Americans deaf or hard of hearing (cited)
**Gaps:** no video link
Sources: https://devpost.com/software/signhero, evidence/swamphacks-swamphacks-xi-signhero.json (README), https://swamphacks-xi.devpost.com/

---

