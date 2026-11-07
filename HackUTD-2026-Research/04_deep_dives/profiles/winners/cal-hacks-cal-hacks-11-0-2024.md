# Cal Hacks — Cal Hacks 11.0 (2024) (9 projects)

### Blockify
*Cal Hacks Cal Hacks 11.0 (2024) · dataset: winners · tier: sponsor_winner · evidence A · confidence medium*
**Prizes:** Winner Cal Hacks / Berkeley RDI: Berkeley RDI Web3 Prize; Winner Sui: Reimagine the internet with Sui

**What it is:** A music royalty platform on the Sui blockchain: an artist attaches a Move smart contract to an uploaded track, and the system watches Spotify stream counts and pays royalties to the artist's Sui wallet.
**Problem / user:** Independent artists, producers and DJs who lose control and most streaming revenue to labels and distributors, and wait on slow royalty payouts.

**Features**
- Smart contract attached at upload — Artist attaches a Move contract to a track when uploading, encoding royalty terms. *[claimed]*
- Stream-count tracking — A Node/Express service polls the Spotify API for streams and triggers payment logic. *[claimed]*
- Automatic wallet payouts — Royalties are sent to the artist's Sui wallet as streams accumulate, per the writeup. *[claimed]*
- Wallet-connected React dashboard — Artists connect a Sui wallet via dapp-kit and view earnings through the Sui SDK. *[claimed]*
- NFTs for exclusive content — Fan-engagement NFTs are listed as a future addition. *[planned]*

**Flow:** Artist connects a Sui wallet in the web app → Uploads a track with an attached royalty smart contract → Backend reads Spotify stream data → Contract logic triggers a payment to the wallet → Artist sees updated earnings in the interface

**Prompt:** Sui challenge: best projects integrating the Sui blockchain win cash prizes. Berkeley RDI Web3 Prize: no description published on the prize list.
**Fit (explicit):** Writes royalty contracts in Move on Sui and uses Sui wallets and the Sui SDK in the frontend and a royalty service, which is the integration the Sui prize asks for.  *(targeted: Sui: Reimagine the internet with Sui, Berkeley RDI Web3 Prize)*
**Sponsor tools:** Sui (Move, Sui SDK, dapp-kit wallets) (Royalty smart contracts, wallet connection and payouts, core); Spotify API (Source of stream counts that trigger payouts, supporting)
**AI:** none
**Architecture:** React app (Sui dapp-kit) for wallet and earnings; a royalty_manager Node/Express service calls the Spotify API and the Sui SDK; Move contracts hold the payout logic on Sui.
**Novelty:** Ties off-chain Spotify stream counts to on-chain royalty contracts; the page does not explain how stream data is verified or how payouts are funded.
**Scope:** small · working: Devpost video embedded and repo has contract, backend and frontend code; no written walkthrough or metrics. · polish: Frontend README is unmodified Create React App boilerplate; no live demo.
**Claims:** Reduces disputes over missed or delayed royalty payments | Immutable auditable record of streams and payments | Royalty updates in real time as songs stream
**Gaps:** README is CRA boilerplate so no repo-side feature list; No demo walkthrough text; end-to-end payout flow not confirmed; Berkeley RDI Web3 prize has no description
Sources: https://devpost.com/software/blockify-x2owt7, evidence/cal-hacks-cal-hacks-11-0-2024-blockify.json (repo README boilerplate, manifests), https://cal-hacks-11-0.devpost.com/

---

### Duet: Brainwaves -> Live Music
*Cal Hacks Cal Hacks 11.0 (2024) · dataset: winners · tier: overall_top3 · evidence A · confidence medium*
**Prizes:** Winner Cal Hacks: 1st Overall [1st]

**What it is:** An Emotiv EEG headset streams focus and relaxation levels to a backend, and Gemini acts as a live composer choosing instruments and writing the next seconds of Sonic Pi music. A Next.js page shows a 3D brain and audio visualizer.
**Problem / user:** Children with developmental disabilities, including non-verbal students, and teachers seeking expression.

**Features**
- EEG reading — Cortex library streams headset data to Python. *[claimed]*
- Live AI composer — Gemini composes upcoming seconds from recent emotional data and prior music. *[claimed]*
- Sonic Pi playback — Generated scores play live. *[claimed]*
- Emotion to music mapping — Focus/relaxation steer tempo and intensity. *[claimed]*
- Visualization — 3D brain, brainwave and audio visualizer in three.js. *[claimed]*
- Low-latency store — SingleStore holds live data. *[claimed]*

**Flow:** Wear headset → Brainwaves stream to backend → Gemini composes next segment → Sonic Pi plays → Frontend displays waves and sound

**Prompt:** Cal Hacks 11.0 overall prizes: 1st Overall (Framework laptops), judged on application, functionality, creativity and technical complexity.
**Fit (implied):** General judging; page stresses a novel live AI-composition approach and a social-good use for children.  *(targeted: Cal Hacks: 1st Overall)*
**Sponsor tools:** SingleStore (Real-time storage of EEG data, supporting); Google Gemini (Live music composition, core)
**AI:** Gemini prompted as a live composer given recent emotion data and past output, choosing instruments and emitting Sonic Pi code.
**Architecture:** Emotiv headset to Python Cortex backend, SingleStore, Gemini, Sonic Pi; Next.js frontend with three.js.
**Novelty:** Closed loop from brain signals to LLM-written live music; team says no known equivalent.
**Scope:** medium · working: Two repos, four screenshots; no video listed; no user study. · polish: Visualizer UI; Devpost has 33 likes.
**Claims:** Believes it is the first live AI music generation from brainwaves | Music therapy sector growth 15.59% (unsourced)
**Gaps:** Repos not browsed beyond evidence file; No video
Sources: https://devpost.com/software/duet-0tbkxe, https://cal-hacks-11-0.devpost.com/

---

### GhostWriter
*Cal Hacks Cal Hacks 11.0 (2024) · dataset: winners · tier: overall_top3 · evidence A · confidence medium*
**Prizes:** Winner Cal Hacks: 2nd Overall [2nd]

**What it is:** A note app that listens to a live office-hour conversation via Deepgram, decides whether each chunk is worth keeping using embeddings against stored notes, and inserts new content at the right line in markdown notes using an LLM. Changes render live.
**Problem / user:** Teaching assistants whose office-hour insights go unrecorded and need tedious post-session revision.

**Features**
- Live transcription — Record button starts a session with Deepgram streaming. *[shown_working]*
- Relevance decision — Chunks queried in ChromaDB; distance thresholds pick no note, add, or new note. *[claimed]*
- Line-level insertion — LLM generates markdown and target position using unique markers. *[claimed]*
- Resource search — Metadata and semantic search over class notes. *[claimed]*
- Notes editor — Add, delete, select, render markdown notes. *[claimed]*

**Flow:** Open class notes → Press record → Speech transcribed → Chunks matched to notes → Edits appear live

**Prompt:** Cal Hacks 11.0 overall prizes: 2nd Overall (Bambu Labs 3D printer), judged on application, functionality, creativity and technical complexity.
**Fit (implied):** General judging; addresses a real TA workflow with live retrieval-augmented generation pipeline.  *(targeted: Cal Hacks: 2nd Overall)*
**Sponsor tools:** Groq (Llama3-70b generation, core); Deepgram (Live transcription, core)
**AI:** Gemini embeddings plus ChromaDB for retrieval; llama3-70b on Groq generates markdown insertions with RAG and prompt engineering.
**Architecture:** Reflex Python full-stack app; Deepgram threaded audio; Gemini embeddings into ChromaDB; Groq generation back into notes.
**Novelty:** Passive line-level note editing from speech, no post-session cleanup.
**Scope:** medium · working: Repo; claims complete pipeline; no video. · polish: System design screenshots; 14 likes.
**Claims:** Complete live note-generation pipeline from audio to insertion
**Gaps:** No video
Sources: https://devpost.com/software/ghostwriter-491kuy, https://cal-hacks-11-0.devpost.com/

---

### MafiAI
*Cal Hacks Cal Hacks 11.0 (2024) · dataset: winners · tier: track_winner · evidence A · confidence low*
**Prizes:** Winner Cal Hacks: Hack on AI

**What it is:** A web version of the party game Mafia in which the other players are LLM-driven characters. The human tries to work out who the mafia are while the AI players talk and vote.
**Problem / user:** No problem statement given; aimed at players of social-deduction games who want AI opponents.

**Features**
- LLM-driven Mafia players — AI characters take part in the discussion and voting rounds of a Mafia game. *[claimed]*
- Real-time game UI — React/TypeScript frontend with rpgui styling talks to a Python backend over WebSockets (socket.io client). *[unclear]*
- Voice and fast inference services — Page lists Cartesia, Groq and Gemini but does not say what each does; Cartesia is likely speech. *[unclear]*

**Flow:** Join a Mafia game in the browser → AI characters and the player discuss → Everyone votes to eliminate a suspect → Player tries to identify the mafia

**Prompt:** not public / not found
**Fit (implied):** Makes LLMs the game participants; the track page gives only a prize, no description.  *(targeted: Cal Hacks: Hack on AI)*
**Sponsor tools:** Cartesia (Listed on Devpost; role not stated, unclear); Groq (Listed on Devpost; role not stated, unclear); Gemini (Listed on Devpost; role not stated, unclear)
**AI:** LLM agents play distinct Mafia roles and converse and vote; which model does what is not documented.
**Architecture:** Python backend (5 files) and React/TypeScript frontend (36 files) connected by WebSockets; LLM and voice APIs called from the backend.
**Novelty:** LLMs act as full social-deduction players rather than a chatbot; very sparse documentation.
**Scope:** small · working: Repo has a frontend and backend (~1k LOC), but no demo or video is linked. · polish: Pixel-RPG UI library in dependencies; README is a one-line title.
**Gaps:** Devpost text is one line; README empty; Roles of Cartesia, Groq, Gemini unstated; No demo, so game flow is inferred
Sources: https://devpost.com/software/mafiai, evidence/cal-hacks-cal-hacks-11-0-2024-mafiai.json, https://cal-hacks-11-0.devpost.com/

---

### Resililink
*Cal Hacks Cal Hacks 11.0 (2024) · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** Winner Cal Hacks: Hack for Impact; Winner Skylo: Seamlessly Switch from Cellular to Satellite

**What it is:** A disaster-time messaging network: cheap LoRa and ESP32 nodes form a mesh, and a satellite-equipped super node uses Skylo to relay messages to a cloud server, which texts the recipient through Twilio and sends an acknowledgment back.
**Problem / user:** People in hurricane or disaster zones with no cell or internet service who need to reach family or responders.

**Features**
- LoRa mesh of low-cost nodes — Each normal node is one LoRa radio plus an ESP32; messages hop long distances at low power. *[shown_working]*
- Satellite super node — A super node with a Skylo-enabled board sends mesh traffic over satellite via MQTT. *[shown_working]*
- Relay server to SMS — Azure-hosted server receives MQTT, decrypts messages and sends SMS via Twilio. *[shown_working]*
- Delivery acknowledgment — Server returns an ack to the originating node once the message goes out. *[claimed]*
- Custom protobuf protocol — Compact Protocol Buffers format fitting the 256-byte packet limit, with encrypted payloads. *[claimed]*
- Dual connectivity — Nodes can use internet when available or peer-to-peer long-range radio. *[claimed]*

**Flow:** User sends a message from a LoRa node → Mesh forwards it to the super node → Super node relays over Skylo satellite via MQTT → Server decrypts and calls Twilio to SMS the recipient → Acknowledgment returns to the sending node

**Prompt:** Skylo: build a connected experience that uses cellular and satellite links to collect data from and act on devices worldwide, using Monogoto APIs and hardware. Hack for Impact: no description on the prize list.
**Fit (explicit):** Super node bridges a local mesh to the internet over Skylo satellite when cellular is gone, and the README says it took first place in the Skylo challenge.  *(targeted: Skylo: Seamlessly Switch from Cellular to Satellite, Cal Hacks: Hack for Impact)*
**Sponsor tools:** Skylo satellite connectivity (Mutura evaluation board) (Backhaul from the super node to the server over MQTT, core); Twilio (SMS delivery to recipients, supporting)
**AI:** none
**Architecture:** ESP32+LoRa normal nodes form a mesh to a Raspberry Pi/ESP32 super node with a Skylo board; MQTT to an Azure Python relay server that decrypts and calls Twilio; React/Vite front end.
**Novelty:** Combines home-built LoRa mesh hardware with a satellite uplink and SMS gateway; had to fit a 256-byte packet limit and poorly documented AT commands.
**Scope:** medium · working: README and Devpost claim a working demonstration; repo has separate normal_node, super_node and relay_server code (~7.9k LOC). · polish: Detailed README, hardware assets and screenshots; no measured range or latency.
**Claims:** Fully functional network with working demonstration | Long-distance, low-power message delivery
**Gaps:** No quantitative range or latency; No demo video link on page
Sources: https://devpost.com/software/resilink, evidence/cal-hacks-cal-hacks-11-0-2024-resililink.json, https://cal-hacks-11-0.devpost.com/

---

### SnackSnap - recycle to feed your pet
*Cal Hacks Cal Hacks 11.0 (2024) · dataset: winners · tier: overall_top3 · evidence B · confidence medium*
**Prizes:** Winner Cal Hacks: 3rd Overall [3rd]

**What it is:** An iOS app where users photograph themselves recycling, Gemini checks the photo, and valid recycling earns snacks to feed a growing digital pet, plus XP for rewards.
**Problem / user:** Everyday people who skip recycling when bins are less convenient.

**Features**
- Photo verification — Gemini 1.5 Pro judges whether the photo shows recycling. *[claimed]*
- Pet feeding — Snacks feed Baby Chester, who grows. *[shown_working]*
- XP rewards — XP redeemable for rewards such as early product access. *[claimed]*

**Flow:** Recycle an item → Take a photo → Gemini validates → Feed pet → Redeem XP

**Prompt:** Cal Hacks 11.0 overall prizes: 3rd Overall (iPads), judged on application, functionality, creativity and technical complexity.
**Fit (implied):** General judging; a gamified sustainability app with a polished pet concept.  *(targeted: Cal Hacks: 3rd Overall)*
**Sponsor tools:** Google Gemini (Image verification, core)
**AI:** Gemini 1.5 Pro image recognition validates recycling photos.
**Architecture:** Swift/SwiftUI iOS app with Firebase and Firebase Storage; Gemini via Google SDK.
**Novelty:** Gamifies recycling with photo proof, but verification is easily gamed.
**Scope:** small · working: Demo video and four screenshots; no repo. · polish: Custom pet art and sketched flow.
**Claims:** Pet growth reduces carbon waste (unquantified)
**Gaps:** No repo; Reward details vague
Sources: https://devpost.com/software/snacksnap-lw4b9q, https://cal-hacks-11-0.devpost.com/

---

### Talk Tuah
*Cal Hacks Cal Hacks 11.0 (2024) · dataset: winners · tier: track_winner · evidence A · confidence medium*
**Prizes:** Winner Cal Hacks: Best Beginner Hack; Winner Deepgram: Deepgram Voice Agent Quest

**What it is:** DIY AR glasses that listen to and look at whoever you are talking to, estimate their mood, and display a suggested positive reply on a small OLED so the wearer can say it. A React Native app handles setup and transcripts.
**Problem / user:** Introverted or socially awkward people who freeze on what to say next in conversation.

**Features**
- Glasses capture and reply display — Camera and mic hardware (Raspberry Pi/Arduino) capture the partner; suggested reply appears on an OLED. *[claimed]*
- Mood detection — Hume AI reads facial expressions and Deepgram handles real-time speech-to-text and voice cues. *[claimed]*
- Mood-aware chatbot replies — GPT-4 prompted on social etiquette picks a positive response based on detected mood and a sensibility score. *[claimed]*
- User profile and contact context — Server stores name, hobbies, likes and dislikes plus contact info to make replies relevant. *[claimed]*
- Speaker voice recognition — SpeechBrain/PyTorch identifies the user's voice from sample audio. *[claimed]*
- Mobile companion app — React Native app for setup, custom prompts, voice recording and transcript review. *[shown_working]*

**Flow:** Enter personal details and record voice in the app → Config is sent to the Flask backend → Wear the glasses; they capture partner speech and face → Mood and transcript feed the chatbot → Suggested reply shows on the OLED → Review transcripts in the app afterward

**Prompt:** Deepgram Voice Agent Quest: tiers of cash and credits with no challenge text on the prize page. Best Beginner Hack: prize only, no description.
**Fit (implied):** Uses Deepgram for live speech-to-text in a voice-driven conversational assistant; the page does not explicitly say it targets the prize.  *(targeted: Deepgram: Voice Agent Quest, Cal Hacks: Best Beginner Hack)*
**Sponsor tools:** Deepgram (Real-time speech-to-text and voice analysis, core); Hume AI (Emotion from facial expressions, supporting)
**AI:** GPT-4 chatbot conditioned on mood and user profile; Deepgram transcription, Hume facial emotion, SpeechBrain speaker recognition.
**Architecture:** Wearable (Pi/Arduino, C firmware) streams audio/video to a Flask server that calls Deepgram, Hume and OpenAI and returns text to the OLED; React Native app configures it via ngrok.
**Novelty:** Full hardware-plus-app wearable built by self-described beginners, with custom firmware and a multi-model perception pipeline.
**Scope:** medium · working: Repo has mobile, chatbot, firmware, speech-to-text and facial-recognition folders (~2.4k LOC); no demo video; latency target unmeasured. · polish: Figma mockups and a mobile app; README is a single line.
**Claims:** Near-zero latency from speech to on-glasses display (stated goal)
**Gaps:** No demo video or live demo; Which features worked end to end is not shown
Sources: https://devpost.com/software/talk-tuah, evidence/cal-hacks-cal-hacks-11-0-2024-talk-tuah.json, https://cal-hacks-11-0.devpost.com/

---

### TeachXR
*Cal Hacks Cal Hacks 11.0 (2024) · dataset: winners · tier: track_winner · evidence A · confidence high*
**Prizes:** Winner Cal Hacks: Hackers' Choice; Winner Vapi: Show us your Voice AI

**What it is:** An XR study assistant for Meta Quest 3: a learner circles a textbook paragraph with a finger, makes an OK gesture to crop it, then asks questions out loud and gets spoken explanations, examples and visualizations.
**Problem / user:** Students short of teacher attention, including those anxious about asking for help; the page cites high student-teacher ratios.

**Features**
- Gesture-based paragraph selection — MediaPipe on the Quest detects pointing and circling; OK gesture crops the region. *[shown_working]*
- OCR of the crop — Google OCR extracts words from the cropped paragraph and neighboring pages for context. *[claimed]*
- Voice Q&A — Vapi orchestrates Deepgram transcription, Gemini 1.5 Flash answers and Cartesia speech, with interruption support. *[shown_working]*
- Summaries, examples and visuals — Assistant gives context-aware summaries, related examples and concept visuals. *[claimed]*
- Real-time data pipeline — SingleStore moves image and OCR text to the voice assistant. *[claimed]*

**Flow:** Open the app in a Quest 3 with a textbook in view → Circle the confusing paragraph → OK gesture crops and submits it → OCR text goes to the voice assistant → Hear the answer and interrupt with follow-ups

**Prompt:** Vapi: three $1,500 prizes for best uses of Voice AI. Hackers' Choice: prize only, no description.
**Fit (explicit):** The tutor is a Vapi voice agent that listens, answers and can be interrupted, with Vapi named as the voice orchestrator.  *(targeted: Vapi: Show us your Voice AI, Cal Hacks: Hackers' Choice)*
**Sponsor tools:** Vapi (Voice conversation orchestration, core); Deepgram (Transcription in the voice stack, supporting); Cartesia (Voice synthesis, supporting); SingleStore (Streaming image/text data between services, supporting)
**AI:** Gemini 1.5 Flash answers questions over OCR text via a Vapi voice pipeline; MediaPipe gesture recognition runs on the headset.
**Architecture:** Quest 3 frontend (React/XR) runs gesture detection and streams crops to cloud services; Google OCR and SingleStore feed a Vapi voice assistant; separate dataflow and gesture backend repos.
**Novelty:** Pairs hand-gesture textbook selection with a voice tutor in XR; the project later moved to a consolidated repo rebuilt on Gemini Live and a browser version.
**Scope:** medium · working: Devpost calls it a functional MVP, with a demo video and live site; frontend repo ~0.8k LOC plus two backend repos. · polish: Live site, demo video, sample use-case images; repo now archived and moved.
**Claims:** Cropping and understanding happens in under 1 second | Millisecond voice response times | Billed as the first AI study assistant in XR
**Gaps:** Backend repos not read; Latency claims unverified; Archived README describes a later Gemini Live version; feature list follows the Devpost page
Sources: https://devpost.com/software/teachxr, evidence/cal-hacks-cal-hacks-11-0-2024-teachxr.json, https://cal-hacks-11-0.devpost.com/

---

### Unreal EngJam
*Cal Hacks Cal Hacks 11.0 (2024) · dataset: winners · tier: track_winner · evidence A · confidence high*
**Prizes:** Winner Cal Hacks: Most Entertaining Hack; Winner Warp: Best Developer Tool by Warp

**What it is:** A from-scratch programming language and game engine that is programmed by drawing boxes and arrows on a Figma FigJam board. It can run Pong and render 3D models in a game window inside Figma, with a Clippy helper.
**Problem / user:** A joke-leaning developer-tool pitch for designers who want to code visually, framed as 'engineer designers'.

**Features**
- Visual dataflow language — A box defines a variable; arrows into it store values and arrows out read them, so no names are needed. *[shown_working]*
- Interpreter in a Figma plugin — Plugin traverses the FigJam document, builds an AST and interprets it in TypeScript with no dependencies. *[shown_working]*
- In-Figma game window — Programs draw to a game window inside Figma; Pong and 3D model rendering are demoed. *[shown_working]*
- Graphical comments, color-coded code — Comments and colors are first-class and move with refactoring by drag and drop. *[claimed]*
- Clippy assistant — Hovers above the offending code to point out mistakes. *[shown_working]*
- Argument inference — Function and operator arguments are matched by applied name, then by type. *[claimed]*

**Flow:** Draw boxes and arrows on a FigJam board → Run the plugin → It parses the board into an AST and executes it → Game window shows Pong or a 3D model → Clippy flags mistakes

**Prompt:** Warp Best Developer Tool: a hack focused on improving the developer experience in a meaningful way; Warp use optional. Most Entertaining Hack: prize only.
**Fit (implied):** Presents itself as a developer tool (a programming environment inside Figma); humor-driven framing fits the entertainment prize. No explicit prize statement.  *(targeted: Warp: Best Developer Tool by Warp, Cal Hacks: Most Entertaining Hack)*
**AI:** none
**Architecture:** TypeScript Figma plugin: traverses FigJam nodes, generates an AST, interprets it with a custom runtime, and renders into an in-document game window.
**Novelty:** Entire language and runtime written without dependencies, with 3D rendering inside Figma; tongue-in-cheek presentation.
**Scope:** small · working: README and Devpost show Pong and a 3D model screenshots; ~1.9k LOC TypeScript. · polish: Humorous README with screenshots; the Devpost shows a broken 3D render.
**Gaps:** No video or setup instructions; Warp tool use not stated
Sources: https://devpost.com/software/unreal-engjam, evidence/cal-hacks-cal-hacks-11-0-2024-unreal-engjam.json, https://cal-hacks-11-0.devpost.com/

---

