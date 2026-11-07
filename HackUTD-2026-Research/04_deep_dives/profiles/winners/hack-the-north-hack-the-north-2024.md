# Hack the North — Hack the North 2024 (6 projects)

### ChatGPMe
*Hack the North Hack the North 2024 · dataset: winners · tier: honorable_or_finalist · evidence A · confidence medium*
**Prizes:** Winner Hack the North 2024 Finalists

**What it is:** A Unity game inspired by Overcooked in which the player plays an AI assistant: timed requests from human users arrive and the player types answers before each timer runs out, then a Cohere-based scorer rates how close the answer is to a real AI response.
**Problem / user:** Players interested in AI and fast time-management games; the premise is to experience handling many LLM requests at once.

**Features**
- Timed order stream — Mock requests of varying difficulty arrive, from facts and maths to creative writing and emotional advice, each with a countdown. *[claimed]*
- Typing response mechanic — Player scans an order and types an answer in Unity before the timer expires. *[claimed]*
- AI similarity scoring — Backend API marks the response; Cohere compares it with what a real AI would say. *[claimed]*
- Orders with a Twist — As the AI becomes aware, orders include existential musings or the AI asking the player questions. *[claimed]*
- 2.5D world — Character movement, interaction, walk animation and start menu in Unity. *[claimed]*
- Input sanitization — Defang used for template generation and sanitizing user inputs. *[claimed]*

**Flow:** Start the game → Receive an order → Scan the request and type a reply → Timer expires or reply is submitted → Cohere-based scorer rates similarity to an AI answer

**Prompt:** Finalists: no criteria given beyond a top-12 selection with eligibility to apply to AWS Magnet. Cohere prize (not clearly entered): best use of Cohere with credit and cash awards.
**Fit (none):** Finalist selection has no stated criteria; page lists Cohere and Defang use but does not name a prize target.  *(targeted: Hack the North 2024 Finalists)*
**Sponsor tools:** Cohere API (Scoring player answers against typical AI replies, core); Defang (Template generation and input sanitizing, supporting)
**AI:** Cohere API evaluates how similar the player's typed answer is to an AI-style reply; the game itself is hand-built Unity logic with mock requests.
**Architecture:** Unity C# client sending player answers to a small backend API that calls Cohere for scoring; JavaScript and Google Cloud listed without detail.
**Novelty:** Inverts the usual chatbot relationship by making the human the AI under time pressure; scored by an actual model.
**Scope:** small · working: Unity project of 176 files but only about 435 lines of scripts and no README; no demo or video. · polish: Hand-drawn Procreate art, 2.5D map and animation per credits; screenshots only.
**Claims:** Multiple playtests refined speed and unpredictability
**Gaps:** Repo has no README so evidence is file tree only; Backend not visible in evidence; Devpost shows both Winner and Finalists labels, wording ambiguous
Sources: https://devpost.com/software/chatgpme, https://github.com/r-chong/HTN-2024 (evidence: no README, Unity project tree), https://hackthenorth2024.devpost.com/

---

### ConArt AI
*Hack the North Hack the North 2024 · dataset: winners · tier: honorable_or_finalist · evidence A · confidence high*
**Prizes:** Winner Hack the North 2024 Finalists

**What it is:** A multiplayer web game for team brainstorming: each player makes a timed quick sketch and writes a prompt, AI turns them into concept images, and the team votes 1 to 5 to fill a leaderboard.
**Problem / user:** Artists and design teams who stall at the start of a project and need a fast way to turn ideas into concrete concept art.

**Features**
- Shared team space — Players join a room and move through real-time sketching, voting and scoring phases via Convex. *[shown_working]*
- Timed sketch plus prompt — Each participant draws a quick doodle and writes a prompt before the countdown ends. *[shown_working]*
- AI concept image generation — Replicate runs ControlNet with Stable Diffusion on the sketch and prompt, called from Convex actions. *[shown_working]*
- Voting and leaderboard — Team scores each design 1 to 5; points feed a leaderboard. *[shown_working]*
- Responsive layout — Interface adapts to different devices and screen sizes. *[claimed]*
- Profiles and saved art — Planned user profiles and saving concept art for iteration. *[planned]*

**Flow:** Join a shared team space → Sketch and write a prompt before the timer → Sketches are converted to concept images → Everyone votes 1 to 5 → Leaderboard and generated art are displayed

**Prompt:** Finalists: no criteria given beyond a top-12 selection with eligibility to apply to AWS Magnet.
**Fit (none):** Finalist track states no requirements, so no stated fit; page mentions only the Winner/Finalist label.  *(targeted: Hack the North 2024 Finalists)*
**Sponsor tools:** Convex (Game state, real-time sync and calling the image API, core); Replicate (ControlNet/Stable Diffusion) (Sketch-to-image generation, core)
**AI:** Replicate-hosted ControlNet guided Stable Diffusion converts each player's sketch plus text prompt into a finished concept image via Convex server actions.
**Architecture:** React/Vite/Tailwind frontend on Vercel; Convex backend for game logic, state and actions; Replicate API for image generation.
**Novelty:** Wraps sketch-to-image generation in a party-game loop (timed sketch, vote, leaderboard) aimed at team ideation.
**Scope:** small · working: Deployed at its own domain per Devpost; screenshots of doodle, leaderboard and generated art; no video. · polish: Responsive UI, full deployment by end of hackathon; small 2k-line repo with a stub README.
**Claims:** Fully deployed by end of the hackathon | UI/UX completed in under 36 hours
**Gaps:** README is a stub; Devpost lists Winner and Finalists labels
Sources: https://devpost.com/software/conart-ai, https://github.com/benjamindrussell/conartAI (evidence README stub), https://hackthenorth2024.devpost.com/

---

### Flashback
*Hack the North Hack the North 2024 · dataset: winners · tier: honorable_or_finalist · evidence B · confidence medium*
**Prizes:** Winner Hack the North 2024 Finalists; Winner Intuit: Win a VR Headset!

**What it is:** A memory museum: users upload photos, video, audio and music in a web app, then walk through a 3D VR gallery (built in Unity, tested on Meta Quest) where approaching an exhibit plays its music, audio clip and captions.
**Problem / user:** People who want a private, reflective way to revisit memories and achievements rather than sharing on social media.

**Features**
- Web app for memories — React/Express app with Convex lets the user upload, update and group memories into collections; Spotify API supplies music. *[claimed]*
- 3D VR museum — Unity scene turns each memory into an exhibit in a gallery, tested on a Meta Quest headset. *[claimed]*
- Proximity-triggered playback — Walking up to an exhibit plays its music, audio clip and captions. *[claimed]*
- Hi-fi design mockups — Figma mockups of web app and VR flows, with mascot Framey. *[shown_working]*
- Accounts and visiting museums — Authentication, visiting other users' museums and VR asset customization listed as future. *[planned]*

**Flow:** Upload and organize memories in the web app → Enter the VR museum → Approach an exhibit → Music, audio and captions play → Revisit the museum over time

**Prompt:** Intuit: hackers must incorporate the QuickBooks API and say how in their submission; judged on entrepreneurial spirit, originality and UX. Finalists: no criteria beyond top-12 selection.
**Fit (none):** The project is itself a VR experience, but Devpost text does not mention QuickBooks or any Intuit API, so how it met the Intuit requirement is not stated.  *(targeted: Hack the North 2024 Finalists, Intuit: Win a VR Headset!)*
**Sponsor tools:** Convex (Database and backend, supporting); Spotify API (Music for exhibits, supporting)
**AI:** none
**Architecture:** React/Express web client and Convex backend for uploads; Unity C# VR client reads the same data to build exhibits; Spotify API for music.
**Novelty:** Reframes a personal photo archive as a walkable VR museum with audio triggers, built by a team new to VR.
**Scope:** small · working: Page claims integrated client, server and VR tested on Quest; no video, demo or code review available. · polish: Hi-fi Figma mockups and mascot art; repo link is only the event organization page.
**Claims:** Tested on a Meta Quest headset | Integrated client, server and VR components
**Gaps:** Repo link is an org listing, not a project repo; No QuickBooks mention to confirm Intuit fit; No video
Sources: https://devpost.com/software/flashback-q3kzg9, https://hackthenorth2024.devpost.com/

---

### LureLore
*Hack the North Hack the North 2024 · dataset: winners · tier: honorable_or_finalist · evidence A · confidence high*
**Prizes:** Winner Hack the North 2024 Finalists

**What it is:** A fishing journal app: photograph a catch and Gemini identifies the species, rates rarity and writes a short 'fish tale'; each fish is added to a 3D Three.js aquarium and a shared world map of catches, with achievements.
**Problem / user:** Anglers who only keep plain photos of catches and want a richer, revisitable record of them.

**Features**
- Photo-based species identification — Catch photo sent to Google Gemini, which returns species and rarity data stored with time and location. *[shown_working]*
- AI fish tale and joke — Gemini writes a short story or joke per catch shown in the fish detail view. *[shown_working]*
- 3D virtual aquarium — Three.js scene displays all past catches; clicking a fish shows stats, date and place. *[shown_working]*
- Achievements — Milestones such as first fish, first tropical fish or first 20-pound fish unlock from catch data. *[shown_working]*
- World catch map — Leaflet map plots where users caught fish worldwide to find spots. *[shown_working]*
- Dashboard and accounts — Interactive dashboard to view and manage catches; login and sign-up per Devpost. *[claimed]*

**Flow:** Snap a photo of a catch → AI identifies species and records stats → Fish appears in the 3D aquarium → Click a fish for rarity, location and its tale → Unlock achievements and browse the world map

**Prompt:** Finalists: no criteria beyond top-12 selection with eligibility to apply to AWS Magnet.
**Fit (none):** Finalist selection has no stated requirements; README labels it a finalist and presented it.  *(targeted: Hack the North 2024 Finalists)*
**Sponsor tools:** MongoDB Atlas (Catch storage, supporting); Google Gemini API (Fish ID from photos and story text, core)
**AI:** Gemini multimodal call identifies the fish from a photo and a separate text prompt generates the tale and rarity; no training or retrieval.
**Architecture:** React frontend with Three.js aquarium and Leaflet map; Node/Express backend calling Gemini; MongoDB Atlas storing catches.
**Novelty:** Turns a mundane logging task into a game-like 3D aquarium plus shared catch map; entire stack is a conventional web app around one multimodal call.
**Scope:** small · working: Demo video and screenshots of aquarium, map and achievements; repo of about 5k LOC with tests flag. · polish: 3D aquarium and map views, README with install steps; no live link.
**Claims:** README title mentions a 5000+ dollar prize total
**Gaps:** Video and finalist presentation not watched; Devpost shows Winner and Finalists labels
Sources: https://devpost.com/software/lurelore, https://github.com/danielh-hong/hackthenorth2024 (evidence README), https://hackthenorth2024.devpost.com/

---

### PathSense
*Hack the North Hack the North 2024 · dataset: winners · tier: honorable_or_finalist · evidence A · confidence high*
**Prizes:** Winner Hack the North 2024 Finalists; Winner Cohere: Best Use of Cohere

**What it is:** A voice-first indoor navigation system for visually impaired people: fixed cameras feed a vision pipeline that describes the scene, MappedIn supplies floor-plan routes, Cohere reranking finds relevant context, and Voiceflow speaks guidance through Unreal Engine text-to-speech.
**Problem / user:** Visually impaired people navigating complex indoor spaces, motivated by family members.

**Features**
- Voice-controlled interaction — Groq Whisper transcribes speech; a Voiceflow decision tree identifies whether the user wants a space or object and the destination. *[claimed]*
- Real-time scene understanding — Tapo 1080p camera streams go through Detectron detection, DPT depth, sub-box splitting and parallel gpt-4o-mini narrations merged into a description. *[claimed]*
- Indoor routing — MappedIn SDK floor plans produce a route from current location to destination or object. *[claimed]*
- Cohere reranking — Rerank picks the most relevant CV tags and map data for the query before Voiceflow forms its answer. *[claimed]*
- Spoken, continuously updated guidance — Instructions converted to speech with Unreal Engine TTS and updated as user and surroundings change. *[claimed]*
- Planned extensions — More venues, personal profiles, wearables, crowd updates, AR for companions, smart building integration. *[planned]*

**Flow:** User speaks a request → Voiceflow identifies target and destination → Cameras and CV pipeline describe the scene → Cohere ranks relevant CV and map data → MappedIn builds a route → Spoken instructions update as the user moves

**Prompt:** Cohere: Best Use of Cohere awards cash and Cohere credits to the best use of Cohere; Finalists has no criteria beyond top-12 selection. Also related sponsor prizes (MappedIn, Voiceflow).
**Fit (explicit):** README states 1st place Cohere use: reranking over CV tags and map data to select context for navigation answers; also builds on MappedIn, Voiceflow, Convex.  *(targeted: Hack the North 2024 Finalists, Cohere: Best Use of Cohere)*
**Sponsor tools:** Cohere Rerank (Choosing relevant CV and mapping data per query, core); Voiceflow (Conversation flow and responses, core); MappedIn SDK (Floor plans and routes, core); Convex (Storing CV and map JSON, supporting); Groq (Whisper speech-to-text, supporting)
**AI:** Detectron object detection, DPT depth, gpt-4o-mini narration of sub-boxes, Cohere rerank for retrieval, Voiceflow agent for dialogue, Whisper STT and Unreal TTS.
**Architecture:** Tapo cameras stream to a CV pipeline writing JSON to Convex alongside MappedIn data; Cohere rerank and route feed Voiceflow, whose text goes to Unreal TTS for the user.
**Novelty:** Combines fixed-camera scene understanding, indoor map routing and reranking-based retrieval into one spoken navigation loop; multi-vendor integration.
**Scope:** medium · working: Ngrok demo link and routed screenshot; no tests or video; 70 files and about 3.5k LOC. · polish: Detailed README workflow; prototype with physical camera setup; no measured accuracy.
**Claims:** README: grand winner and 1st place Best Use of Cohere
**Gaps:** No video; Demo is a temporary tunnel link; Cohere prize text lacks detailed criteria
Sources: https://devpost.com/software/pathsense-athy2r, https://github.com/akjadhav/hackthenorth-2024 (evidence README), https://hackthenorth2024.devpost.com/

---

### TinkerFlow
*Hack the North Hack the North 2024 · dataset: winners · tier: honorable_or_finalist · evidence A · confidence medium*
**Prizes:** Winner Hack the North 2024 Finalists

**What it is:** A web assistant that identifies electronic components from a photo or typed list, suggests projects buildable with them, and generates wiring plans, step-by-step instructions with a playful voice, and a custom-drawn electrical schematic.
**Problem / user:** Beginners to experienced hobbyists who have parts but do not know how to wire them or what to build.

**Features**
- Component identification — Photo goes to a Flask backend where Google Vision AI classifies it; alternatively user types components; about 80% accuracy claimed. *[claimed]*
- Project suggestions — LLM proposes projects (e.g. weather station, motor speed controller) from available parts. *[shown_working]*
- Wiring scheme and instructions — Large structured prompts with examples make the LLM output wire lists and playful build steps. *[shown_working]*
- Custom schematic drawer — Hand-built JavaScript drawer renders schematics because existing React Flow-based libraries were deprecated. *[shown_working]*
- Selectable LLM backend — Cohere (default, RAG and preamble) or Groq (faster, lower quality). *[claimed]*
- Code export — Exporting generated code files. *[planned]*

**Flow:** Upload a component photo or type parts → Backend identifies components → Choose Cohere or Groq → LLM returns project ideas, wiring and schematic data → View schematic and instructions in browser

**Prompt:** Finalists: no criteria beyond top-12 selection. Cohere prize rewards best use of Cohere with credits and cash.
**Fit (none):** Finalist track has no stated criteria; README only labels it a winner.  *(targeted: Hack the North 2024 Finalists)*
**Sponsor tools:** Cohere (Default LLM with RAG and custom preamble, core); Groq (Faster alternate LLM, supporting)
**AI:** Google Vision AI image classification feeds Cohere or Groq LLMs through heavily structured prompts and LangChain; Cohere RAG and preamble for consistent output.
**Architecture:** React frontend and custom schematic renderer; Flask backend calling Google Vision AI, then Cohere or Groq; results returned as text and schematic data.
**Novelty:** Combines vision-based part recognition with LLM wiring generation and a self-built schematic renderer for makers.
**Scope:** small · working: Screenshots of generated projects; repo has tests flag but README is a stub; no demo or video. · polish: Custom schematic drawing; UI and speed listed as next steps.
**Claims:** Component identification about 80% accurate
**Gaps:** README nearly empty so repo adds no feature detail; Devpost page: Finalists only; README claims Winner
Sources: https://devpost.com/software/tinkerflow, https://github.com/wilsonchenghy/TinkerFlow (evidence README stub), https://hackthenorth2024.devpost.com/

---

