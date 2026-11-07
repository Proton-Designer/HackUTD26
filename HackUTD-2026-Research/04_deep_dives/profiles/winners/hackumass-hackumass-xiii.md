# HackUMass — HackUMass XIII (27 projects)

### $HackProof
*HackUMass HackUMass XIII · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** [MLH] Best Use of Solana

**What it is:** Solana-based hackathon voting prototype: participants register with a wallet, mint an identity NFT, submit projects and spend tokens to vote, with a live leaderboard.
**Problem / user:** Hackathon participants and organizers wanting transparent community judging rather than a few judges.

**Features**
- Soulbound participant NFT — Minted at registration as identity *[claimed]*
- Project submission with IPFS metadata — Project NFTs tied to participant *[claimed]*
- Token voting — 100 $HACK tokens each, with anti-self-vote checks, counted on-chain *[claimed]*
- Leaderboard — Ranking from on-chain votes *[claimed]*
- QR code voting — Mobile voting at live demos *[claimed]*
- Judge weights and cross-event reputation — Future *[planned]*

**Flow:** Connect Phantom wallet → Register and get NFT → Receive tokens → Submit project → Vote → View leaderboard

**Prompt:** MLH Best Use of Solana: build fast, efficient, scalable apps avoiding high fees and slow confirmations.
**Fit (explicit):** Anchor program on Devnet handles registration, tokens, NFTs and vote counting.  *(targeted: [MLH] Best Use of Solana)*
**Sponsor tools:** Solana (Anchor, SPL, devnet) (Identity NFTs, voting tokens, on-chain votes, core)
**AI:** none
**Architecture:** Next.js frontend with wallet adapter; Rust Anchor program on Devnet; shared TypeScript IPFS/metadata library.
**Novelty:** Treats judging as on-chain tokenized peer voting with identity credentials.
**Scope:** medium · working: ~5.4k LOC with tests, live demo sites listed, README flow. · polish: Mermaid diagram in README; live deployments.
**Claims:** End-to-end flow works on Devnet
**Gaps:** README says this is an older prototype
Sources: https://devpost.com/software/hackproof-r9v24j, https://github.com/namerror/HackProof-prototype, https://hackumass-xiii.devpost.com/

---

### 3D Printing Kiosk
*HackUMass HackUMass XIII · dataset: winners · tier: overall_top3 · evidence A · confidence high*
**Prizes:** Winner Second Prize [2nd]

**What it is:** Kiosk app and RFID reader for a university makerspace that checks a student ID before starting a 3D print and logs the job. Integrates with OrcaSlicer and sends prints to the printer over LAN.
**Problem / user:** Makerspace staff and patrons; prints had no owner, length or training checks.

**Features**
- Slicer integration — Mimics OctoPrint API so OrcaSlicer uploads sliced files *[claimed]*
- GCode parser — Reads duration, weight, printer and filament without loading whole file *[claimed]*
- ID scan authorization — ESP32 with PN5180 reads card, derives ID, database checks eligibility *[claimed]*
- Remote print start — REST call to printer over LAN *[claimed]*
- Usage stats and print records — Per-user totals and traceable failed prints *[claimed]*
- Queue and web upload — Future *[planned]*

**Flow:** Upload or slice a model → Kiosk shows print info → Scan ID → System checks authorization → Print starts → Stats recorded

**Prompt:** HackUMass XIII Second Prize: general prize, items only.
**Fit (none):** General prize; real-world makerspace tool.  *(targeted: Second Prize)*
**AI:** none
**Architecture:** Qt Quick/QML C++ kiosk with state machine; ESP32 firmware reads RFID over serial; database and printer REST.
**Novelty:** Solo hardware plus software system built for a real deployment site, with reverse-engineered slicer calls.
**Scope:** medium · working: ~6.2k LOC across two repos, Docker, demo video, intended for production use. · polish: Custom 3D-printed case, LED and buzzer feedback.
**Claims:** Built for long-term makerspace use
**Gaps:** Firmware repo not read
Sources: https://devpost.com/software/pcm-3d-printing-kiosk, https://github.com/Atyrnal/PCMakerspace3DPKiosk

---

### Amby
*HackUMass HackUMass XIII · dataset: winners · tier: track_winner · evidence B · confidence medium*
**Prizes:** [HACKUMASS] [Hardware] Best Circuit Hack

**What it is:** ESP32 noise monitor with a microphone and colour LEDs showing blue, blinking green or blinking red against a user-set loudness threshold, plus a FastAPI website with noise graphs.
**Problem / user:** People seeking quiet study spots or avoiding neighbor noise complaints.

**Features**
- LED loudness indicator — Colour state from mic level versus threshold *[claimed]*
- Adjustable threshold — User-set *[claimed]*
- Noise smoothing — Filtering of mic disturbances *[claimed]*
- Web dashboard — FastAPI with Pandas and Plotly graphs of noise over time *[claimed]*
- WiFi multi-device data — Future *[planned]*

**Flow:** Place device → Set threshold → Watch LED → View graphs on site

**Prompt:** HackUMass XIII Best Circuit Hack: no description; prize PINECIL soldering iron.
**Fit (implied):** Built around a custom ESP32 circuit.  *(targeted: Best Circuit Hack)*
**AI:** none
**Architecture:** ESP32 firmware (Arduino) reads mic and drives LEDs; FastAPI site renders charts from recorded data.
**Novelty:** Hardware visualization of noise paired with area analytics.
**Scope:** small · working: Demo video on Vimeo; repo not cloneable here. · polish: Unclear.
**Gaps:** Repo clone failed; Web data source unclear
Sources: https://devpost.com/software/amby, https://hackumass-xiii.devpost.com/

---

### AR Cube Cannon
*HackUMass HackUMass XIII · dataset: winners · tier: track_winner · evidence A · confidence medium*
**Prizes:** [HACKUMASS] [Hardware] Best Hardware Hack

**What it is:** Handheld device with a transparent OLED showing a virtual grid of cubes you place and remove, using an IMU for orientation and buttons for movement. Custom 3D engine, scrap-part body.
**Problem / user:** No stated problem; playful mix of Garry's Mod tool gun and Minecraft building.

**Features**
- Cube placement and removal — Grid-based cubes in virtual space *[claimed]*
- Transparent OLED display — Shows rendered cubes in view *[claimed]*
- IMU aiming — Orientation drives view; drift forced buttons for position *[claimed]*
- Custom graphics engine — 3D rendering on Arduino/C++ *[claimed]*

**Flow:** Hold device → Aim with orientation → Press buttons to move → Place or break cubes

**Prompt:** HackUMass XIII Best Hardware Hack: no description; prize Creality Ender 3.
**Fit (implied):** Physical AR device built from scrap parts.  *(targeted: Best Hardware Hack)*
**AI:** none
**Architecture:** Microcontroller C++ renders cubes to OLED, reads IMU and buttons.
**Novelty:** Custom rendering engine on constrained hardware.
**Scope:** small · working: ~1.9k LOC; six screenshots; no video. · polish: Custom body; empty README.
**Gaps:** README empty
Sources: https://devpost.com/software/ar-cube-cannon, https://github.com/Magirush/AR-Cube-Cannon

---

### Atlas
*HackUMass HackUMass XIII · dataset: winners · tier: track_winner · evidence A · confidence high*
**Prizes:** [HACKUMASS] [Software] Best Web Hack

**What it is:** Web app where uploaded images are embedded with CLIP, projected to 3D with PCA, clustered and shown as an explorable 3D graph. Users sign in and browse clusters and neighbors.
**Problem / user:** Anyone wanting to explore visual relationships in an image collection.

**Features**
- Batch image upload with CLIP — 512-D embeddings per image *[claimed]*
- PCA 3D projection — Replaced slow UMAP *[claimed]*
- K-means clustering — k chosen by silhouette score *[claimed]*
- kNN plus MST graph — Ensures global connectivity *[claimed]*
- 3D scene — React Three Fiber orbit, zoom, select *[claimed]*
- Search and auth — Supabase JWT, multi-user, Gemini descriptions *[claimed]*

**Flow:** Sign in → Upload images → Pipeline builds map → Orbit and select nodes → Browse clusters

**Prompt:** HackUMass XIII Best Web Hack: no description; prize Fire TV Stick.
**Fit (implied):** Full-stack web app.  *(targeted: Best Web Hack)*
**AI:** CLIP ViT-B/32 embeddings; Gemini image descriptions.
**Architecture:** React/Vite with Three.js; FastAPI computes embeddings, PCA, clustering; Supabase stores data.
**Novelty:** Spatial 3D map of image similarity.
**Scope:** medium · working: End-to-end pipeline with YouTube video; repo with detailed README. · polish: Interactive 3D visualization.
**Gaps:** Evidence README not fully re-read
Sources: https://devpost.com/software/atlas-5pzm69, https://github.com/c-aly/Atlas

---

### Birders' Cuckoo Clock
*HackUMass HackUMass XIII · dataset: winners · tier: track_winner · evidence A · confidence high*
**Prizes:** [HACKUMASS] [Hardware] Best Beginner Hardware

**What it is:** Raspberry Pi Pico digital cuckoo clock that plays a random bird call each hour and shows its name on a 16x2 LCD; only a goose is loaded so far.
**Problem / user:** Aspiring birders learning to recognize bird calls.

**Features**
- Hourly chime with bird call — Plays random call through LM386 speaker *[claimed]*
- Name display — LCD shows bird *[claimed]*
- Time setting — Two buttons at startup *[claimed]*

**Flow:** Set time with buttons → Clock runs → Hourly call plays and name shows

**Prompt:** HackUMass XIII Best Beginner Hardware: no description; prize Raspberry Pi 5.
**Fit (implied):** First hackathon hardware build.  *(targeted: Best Beginner Hardware)*
**AI:** none
**Architecture:** MicroPython on Pico drives LCD and audio amp.
**Novelty:** Passive learning device.
**Scope:** tiny · working: ~165 LOC; one photo. · polish: Sound quality poor.
**Gaps:** Only one bird
Sources: https://devpost.com/software/birders-cuckoo-clock, https://github.com/sharayujosh/hackathon25

---

### Clause
*HackUMass HackUMass XIII · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** [MLH] Best Use of AI powered by Reach Capital

**What it is:** Legal-rights assistant for Massachusetts: upload a lease, medical bill or contract, get violations flagged, damages computed, and demand letters generated with statute citations. Chrome extension scans Airbnb listings.
**Problem / user:** Renters, patients and consumers who do not know their rights.

**Features**
- Document analysis — Gemini with retrieved statutes flags violations and damages *[claimed]*
- Demand letters — Generated with citations *[claimed]*
- PII redaction — spaCy NER plus regex before analysis *[claimed]*
- Snowflake RAG — Cortex embeddings over Massachusetts law *[claimed]*
- Chrome extension — Flags clauses on Airbnb *[claimed]*
- Multilingual voice chat — ElevenLabs *[claimed]*
- Solana timestamping — Hashes documents *[claimed]*

**Flow:** Upload document → PII stripped → Review highlights → Get demand letter → Ask follow-ups

**Prompt:** MLH Best Use of AI powered by Reach Capital: broad AI prompt about what technology can now accomplish.
**Fit (implied):** RAG-grounded legal assistant.  *(targeted: [MLH] Best Use of AI powered by Reach Capital)*
**Sponsor tools:** Snowflake Cortex (Embeddings, core); Solana (Timestamping, supporting); ElevenLabs (Voice, supporting); Vultr (Hosting, supporting)
**AI:** Gemini 2.0 Flash Thinking with strict retrieval grounding.
**Architecture:** Next.js frontend, FastAPI backend, Snowflake, R2, Solana, extension.
**Novelty:** Spans three repos plus extension.
**Scope:** large · working: ~6k LOC backend, video; zero hallucination claimed. · polish: Three repos.
**Claims:** Zero hallucinations in legal analysis | ~80% of U.S. medical bills contain errors
**Gaps:** Frontend and extension repos not read
Sources: https://devpost.com/software/clause-bu9l74, https://github.com/sh1v-ansh/clause-backend, https://hackumass-xiii.devpost.com/

---

### Data Security Hub
*HackUMass HackUMass XIII · dataset: winners · tier: track_winner · evidence A · confidence medium*
**Prizes:** [HACKUMASS] [Cybersecurity] Best Beginner Cybersecurity Hack

**What it is:** Single-page HTML tool that encrypts and decrypts text and uses Gemini to generate memorable passwords from a theme the user types.
**Problem / user:** Individuals wanting to protect data and create strong passwords.

**Features**
- Encrypt and decrypt — In-browser *[claimed]*
- Themed password generation — Gemini API *[claimed]*

**Flow:** Open HTML → Enter data or theme → Get output

**Prompt:** HackUMass XIII Best Beginner Cybersecurity Hack: no description; prize power bank.
**Fit (implied):** Beginner security tool.  *(targeted: Best Beginner Cybersecurity Hack)*
**AI:** Gemini API generates passwords from themes.
**Architecture:** One HTML file calling Gemini.
**Novelty:** Beginner scope.
**Scope:** tiny · working: ~555 LOC in a single file. · polish: Minimal.
**Gaps:** Encryption method unspecified
Sources: https://devpost.com/software/data-security-hub, https://github.com/LordBraveNick/DataSecHub

---

### DataVault
*HackUMass HackUMass XIII · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** [MLH] Best Use of Vultr

**What it is:** Privacy pipeline for sensitive records: data is anonymized, AES-256 encrypted into PostgreSQL, decrypted in memory to build embeddings in ChromaDB, then queried in natural language with Gemini on anonymized context.
**Problem / user:** Organizations like hospitals and banks wanting AI on sensitive data without exposure.

**Features**
- PII anonymization — Synthetic replacements before storage *[claimed]*
- AES-256 encrypted storage — Blobs in Postgres *[claimed]*
- Just-in-time decryption — For RAG only *[claimed]*
- Vector search with ChromaDB — Embeddings *[claimed]*
- Natural-language querying — Gemini answers *[claimed]*
- gRPC ingestion — Producers send data *[claimed]*
- Web UI — Pipeline view and queries *[claimed]*

**Flow:** Send data via gRPC → Anonymize and encrypt → Build vectors → Ask question → Get answer

**Prompt:** MLH Best Use of Vultr: bring high-performance projects to life on Vultr cloud.
**Fit (implied):** Hosted on Vultr in a secured environment.  *(targeted: [MLH] Best Use of Vultr)*
**Sponsor tools:** Vultr (Hosting, supporting)
**AI:** Gemini RAG over ChromaDB.
**Architecture:** Docker Compose: backend, Postgres, Redis, ChromaDB.
**Novelty:** Security-first RAG.
**Scope:** medium · working: ~ Docker setup, simulations and e2e test; video. · polish: Detailed README.
**Gaps:** Challenges not on page
Sources: https://devpost.com/software/datavault-cqajxi, https://github.com/P-Bhanu-Sohan/DataVault

---

### HALO
*HackUMass HackUMass XIII · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** [HACKUMASS] [PIT] Best Accessibility Hack

**What it is:** A Manifest V3 Chrome extension with two modes: it watches videos on major social platforms and pauses them when dangerous flashing is detected, and it summarizes web articles with Gemini and reads them aloud via ElevenLabs.
**Problem / user:** People with photosensitive epilepsy lacking real-time protection from flashing video, plus people with ADHD or dyslexia who struggle with dense online text.

**Features**
- Flash detection and auto-pause on YouTube, TikTok, X, Instagram, Twitch — Samples video frames, computes WCAG 2.1 luminance changes, pauses at 3+ flashes per second and shows a warning overlay with stats *[shown_working]*
- Performance and false-positive tuning — Every third frame, pixel sampling, capped resolution, warmup frames, dark-frame skipping, red-flash detection *[claimed]*
- Article summarizer — Extracts main text with four fallback strategies, sends to Gemini for brief, moderate or bullet summaries *[shown_working]*
- Text-to-speech narration — ElevenLabs multilingual model with 10 selectable voices reads summaries *[shown_working]*
- White noise player — Plays background sounds for concentration, persistent audio under Manifest V3 *[shown_working]*
- Popup, stats and export — Mode toggle, counters for videos monitored and warnings, copy or download summary as txt *[shown_working]*

**Flow:** Install extension and enter Gemini/ElevenLabs keys in config window → Browse; on supported video sites flashes trigger pause plus warning overlay → Open popup on an article to choose summary length → Read the summary or play it with a chosen voice and optional white noise → Copy or download the summary

**Prompt:** PIT category prize for the Best Accessibility Hack; the hackathon page gives only the name, no extra description.
**Fit (implied):** Two accessibility tools in one extension: seizure protection for photosensitive viewers and summarization with audio narration for ADHD or dyslexic readers.  *(targeted: [HACKUMASS] [PIT] Best Accessibility Hack, MLH Best Use of Gemini API, MLH Best Use of ElevenLabs)*
**Sponsor tools:** Google Gemini API (article summarization (gemini-2.0-flash), core); ElevenLabs (multilingual text-to-speech narration of summaries, core)
**AI:** Gemini 2.0 Flash summarizes extracted article text in selectable lengths; ElevenLabs multilingual v2 produces narration. Flash detection is rule-based luminance math, not ML.
**Architecture:** Content scripts: detector.js (video frame analysis) and summarizer.js (page text extraction); background service worker; popup plus full-page web app; Gemini and ElevenLabs called from the extension; settings in Chrome sync.
**Novelty:** Bundles two unrelated accessibility needs in one extension; flash detection implemented locally in-browser per WCAG thresholds with platform-specific handling such as YouTube Shorts.
**Scope:** small · working: Detailed README of implemented files and settings; demo video on Devpost; no live link. · polish: Popup UI, stats, warning overlay, 10 voices, multiple summary modes, error-recovery handling.
**Claims:** Claims 12-48x speedup in flash detection from optimizations | Claims zero false positives after extensive testing | Flags 3+ flashes per second per WCAG 2.1
**Gaps:** video not watched; screenshots not counted
Sources: https://devpost.com/software/halo-u73r9j, https://github.com/athulya-anil/Halo (evidence file), https://hackumass-xiii.devpost.com/

---

### healthNET
*HackUMass HackUMass XIII · dataset: winners · tier: track_winner · evidence A · confidence high*
**Prizes:** [HACKUMASS] [Ethical AI] Most Impactful AI Hack

**What it is:** A federated-learning platform where hospitals run node servers that train a shared neural network locally and send only weight updates to a central aggregator, which averages them with FedAvg. A React dashboard shows training and inference.
**Problem / user:** Hospitals and research institutions that cannot pool patient data under privacy law, so single-site models are less accurate and more biased.

**Features**
- Federated training across nodes — Nodes train on local data; aggregator distributes global model and averages returned weights with FedAvg over multiple rounds using Flower *[shown_working]*
- Aggregator server and dashboard — FastAPI backend coordinates rounds; dashboard shows training progress *[shown_working]*
- Client training and inference dashboards — React views for a node to train locally and run inference on the model *[shown_working]*
- Cloud-hosted aggregator — Aggregator and training hosted on Vultr; live dashboard at a project domain *[shown_working]*
- Auth, more models, custom datasets, desktop client — Listed as next steps *[planned]*

**Flow:** Start the FastAPI aggregator and the React dashboard → Nodes connect with their private datasets → Run a federated round: model sent out, local training, updates returned → Aggregator averages updates into the global model → View results in training and inference dashboards

**Prompt:** Most Impactful AI Hack (Ethical AI track): create a customized agent that benefits the campus community, with bonus for usability feedback and improvements.
**Fit (implied):** Frames impact as privacy-preserving collaboration among healthcare institutions rather than a campus agent; no stated campus or agent angle.  *(targeted: [HACKUMASS] [Ethical AI] Most Impactful AI Hack, Best Use of Vultr)*
**Sponsor tools:** Vultr (cloud credits hosting the aggregator server and training, supporting)
**AI:** Neural networks trained with federated learning using the Flower framework and FedAvg aggregation; no specific model architecture or dataset is named.
**Architecture:** Python FastAPI + Flower aggregator on Vultr; node servers per institution holding local data; React/Vite client dashboards; managed with uv.
**Novelty:** Applies an established technique (federated learning) as a hosted multi-hospital product with dashboards; the team presents it as new learning for them.
**Scope:** small · working: Live dashboard URL, README with run steps for aggregator and clients, demo video. · polish: Separate client and aggregator dashboards; no tests; no quantitative results reported.
**Claims:** Says the system is simple to use and scales easily | Cites healthcare as roughly 30% of world data volume
**Gaps:** no accuracy numbers; dashboards seen only via captions
Sources: https://devpost.com/software/healthnet-h5o0dx, https://github.com/HenryLiu714/healthnet (evidence file), https://hackumass-xiii.devpost.com/

---

### Interdict.
*HackUMass HackUMass XIII · dataset: winners · tier: track_winner · evidence A · confidence high*
**Prizes:** [HACKUMASS] [Software] Best Software Hack

**What it is:** A Python SOCKS5 proxy that quietly slows connections to user-listed addictive sites and apps, with delay growing the longer they are used. The aim is to make doomscrolling frustrating enough that users cut back without a visible block.
**Problem / user:** People trying to reduce doomscrolling who defeat visible time-locks by dismissing them; wants limits the user is not explicitly told about.

**Features**
- Transparent SOCKS5 proxy — Routes traffic directly unless destination is on blocklist; inspects only destinations, not content, preserving TLS *[shown_working]*
- Usage-based gradual throttling — Tracks time spent per service over a window and adds random packet delay along a sigmoid curve *[shown_working]*
- Configurable parameters — Grace period, aggressiveness, max delay and tracking window set by user *[shown_working]*
- Web UI configurator — Flask/Tailwind page to edit settings and start the proxy; logs show throttling *[shown_working]*
- External hosting for iOS — Run proxy on a remote server so sandboxed phones connect via a proxy client *[shown_working]*
- ML-driven tuning, auth, router deployment — Listed as next steps *[planned]*

**Flow:** Install with pip flask and run ui.py to configure → Add sites to the blocklist and set throttle parameters → Point device or app proxy settings at Interdict → Use blocked services normally; lag increases with use → Run proxy.py headless after configuring

**Prompt:** Best Software Hack in the Software category; hackathon page gives no descriptive text beyond the name.
**Fit (none):** General software entry: a working network tool with config UI that tackles screen-time addiction through adversive conditioning.  *(targeted: [HACKUMASS] [Software] Best Software Hack)*
**AI:** none
**Architecture:** Python SOCKS5 server using sockets and threads intercepts TCP streams; per-domain usage tracker feeds a delay function; Flask UI configures it; can be hosted remotely.
**Novelty:** Takes a covert behavioral-conditioning approach instead of blocking, implemented as a network-layer proxy that works on any device with proxy settings.
**Scope:** small · working: Reported working on an iPhone via externally hosted proxy; demo video; README with install and run commands. · polish: Screenshots of UI and logs; small codebase (about 570 LOC est.); no tests.
**Claims:** Reported working on an iPhone | Says no traffic content is logged, only destinations
**Gaps:** video not watched
Sources: https://devpost.com/software/interdict, https://github.com/theokrueger/interdict (evidence file), https://hackumass-xiii.devpost.com/

---

### minutemesh
*HackUMass HackUMass XIII · dataset: winners · tier: sponsor_winner · evidence C · confidence low*
**Prizes:** [HACKUMASS] [Cybersecurity] Most Impactful Cybersecurity Hack

**What it is:** A security-testing tool for Meshtastic-style mesh radio networks that demonstrates a sender-impersonation weakness. Entered in HackUMass XIII's cybersecurity prize. Detailed attack mechanics deliberately not recorded.
**Problem / user:** Security-minded users of mesh radio networks; shows that channel trust can be abused when a key is known.

**Features**
- Impersonation demo against a mesh radio protocol — High-level only: pentest tool built on MeshTNC firmware (from existing brief); details not recorded. *[claimed]*
- Pentest-style tooling for mesh channels — Not recorded in detail. *[unclear]*

**Prompt:** HackUMass XIII cybersecurity prize (Most Impactful Cybersecurity Hack); only the prize name is public.
**Fit (implied):** Demonstrates a security weakness in a mesh radio protocol, matching the cybersecurity track.  *(targeted: [HACKUMASS] [Cybersecurity] Most Impactful Cybersecurity Hack)*
**AI:** none
**Architecture:** Built on MeshTNC firmware per existing brief; not analyzed further.
**Novelty:** Targets an uncommon hardware/radio protocol surface for a hackathon security project.
**Scope:** small · working: Prize-winning entry per existing brief; not independently reviewed here. · polish: Not assessed.
**Gaps:** Deep read intentionally kept high-level; attack details not recorded
Sources: dd_master existing brief

---

### Obscurafy
*HackUMass HackUMass XIII · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** [HACKUMASS] [Cybersecurity] Best Data Protection

**What it is:** An iOS app that scans the photo library with an on-device object-detection model for IDs, passports and credit cards, then lets the user swipe each flagged photo to keep, redact (blur) or delete it. Gemini explains why an image was flagged.
**Problem / user:** iPhone users who accumulate screenshots and photos containing personal documents and may share or leave them exposed unknowingly.

**Features**
- Sensitive-photo scanning — YOLOv11 model fine-tuned on eight open datasets, converted to Core ML, runs on-device over the Photos library *[shown_working]*
- Swipe triage — Tinder-style cards: left keeps, up redacts by blurring, right deletes *[shown_working]*
- Explainer — Shows ML rating plus a Gemini-written assessment of why the image was flagged, after PII is redacted before the API call *[shown_working]*
- Background scan with notification — Scan continues in background and notifies on completion *[claimed]*
- Aggregate statistics — Summary screen of scan results *[shown_working]*
- Android port, vault mode, enterprise dashboard — Listed as future work *[planned]*

**Flow:** Grant photo read/write permission → Scanner runs in background over library → Flagged images appear one at a time → Open ML rating and Gemini explanation → Swipe to keep, blur or delete → View aggregated stats

**Prompt:** Best Data Protection in the Cybersecurity track; the hackathon page gives only the name.
**Fit (implied):** Protects personal data by finding exposed IDs in photos locally, keeping processing on-device and redacting before any cloud call.  *(targeted: [HACKUMASS] [Cybersecurity] Best Data Protection, MLH Best Use of Gemini API)*
**Sponsor tools:** Google Gemini API (natural-language explanation of why a photo was flagged, supporting)
**AI:** Custom YOLOv11 detector trained in PyTorch on merged ID/passport/card datasets and run via Core ML; Gemini generates explanations from redacted content.
**Architecture:** SwiftUI app using Photos API and Core ML for detection; Swift server layer proxies Gemini calls; Python used offline for dataset cleaning and training.
**Novelty:** Trained its own detector from several mismatched datasets and pairs on-device detection with a swipe-review interface for privacy cleanup.
**Scope:** medium · working: Screenshots of scan, flagged list, explainer; project website listed; no video. · polish: Native iOS UI with swipe cards and stats; around 7k LOC across 82 files; no tests.
**Claims:** Says sensitive data is never sent through API calls | Says model was trained from scratch on eight datasets in hackathon time
**Gaps:** no accuracy metrics; website content not read
Sources: https://devpost.com/software/vaulteye, https://github.com/AlexanderMcGreevy/Obscurafy (evidence file), https://hackumass-xiii.devpost.com/

---

### OceanEye
*HackUMass HackUMass XIII · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** [HACKUMASS] [PIT] Best Sustainability Hack

**What it is:** A dashboard that detects and segments floating trash in ocean drone and satellite footage with a YOLOv8 model, uses Gemini with retrieval for cleanup insights, and plans clustered, boat-friendly cleanup routes.
**Problem / user:** Ocean cleanup crews and researchers who currently locate and collect marine debris manually and inefficiently.

**Features**
- Debris detection and segmentation — YOLOv8 fine-tuned on drone/satellite imagery with augmentation for glare, waves and turbidity *[shown_working]*
- Satellite accumulation zones — Sentinel-2 data via Google Earth Engine flags likely pollution areas and trends *[shown_working]*
- Gemini RAG insights — Gemini with a vector store of history, tide and wind context writes trend and risk reports *[shown_working]*
- Cleanup route optimizer — Clusters sites, orders stops with nearest neighbor plus 2-opt, smooths path with Catmull-Rom splines *[shown_working]*
- Interactive maps and charts — Next.js dashboard with maps, charts and 3D views of debris and routes *[shown_working]*
- Drift prediction, live feeds, drone fleets — Listed as next steps *[planned]*

**Flow:** Upload or load ocean footage → View detected and classified debris → Read Gemini insights for the area → Inspect clustered sites and optimized route → Explore satellite maps and trends

**Prompt:** Best Sustainability Hack in the PIT category; hackathon page gives only the name.
**Fit (implied):** Targets ocean plastic pollution by detecting debris, tracking accumulation from satellites and planning efficient cleanup routes.  *(targeted: [HACKUMASS] [PIT] Best Sustainability Hack, MLH Best Use of Gemini API, Best Use of Vultr)*
**Sponsor tools:** Google Gemini API (RAG-based cleanup insights and risk reports, core); Vultr (hosting the Flask backend, supporting)
**AI:** YOLOv8 instance segmentation in PyTorch for debris; Gemini RAG over a vector store of pollution, tide and wind context; classical route heuristics.
**Architecture:** Next.js/React/TypeScript frontend on Netlify; Flask backend on Vultr with OpenCV, YOLOv8 inference, route solver and Gemini RAG; Earth Engine satellite data.
**Novelty:** Combines vision detection, satellite monitoring, LLM analysis and route planning in one dashboard, with a route cost balancing fuel and ecological disruption.
**Scope:** medium · working: Demo video and screenshots of detection, routes and maps; no live link; about 13.6k LOC est. · polish: Modern UI stack with 3D and charts; no tests or metrics.
**Claims:** Claims strong real-world segmentation performance without metrics | Claims biologically safer navigation paths
**Gaps:** no model metrics
Sources: https://devpost.com/software/oceanhub, https://github.com/Tirth2116/OceanEye (evidence file), https://hackumass-xiii.devpost.com/

---

### OnePen
*HackUMass HackUMass XIII · dataset: winners · tier: track_winner · evidence B · confidence medium*
**Prizes:** [HACKUMASS] [Ethical AI] Most Novel Use of AI

**What it is:** A browser handwriting-notes canvas that interprets pen gestures (underline, box, bracket, strike-through, circle) as formatting commands so the writer never reaches for a toolbar. It also recognizes handwritten math, builds a table of contents and syncs to Google Drive.
**Problem / user:** Heavy handwritten note-takers, such as students, whose flow breaks when they switch to toolbars to format.

**Features**
- Gesture modifiers — TensorFlow.js hybrid model reads strokes: underline or box highlights, strike-through deletes, brackets group *[shown_working]*
- Pen style switching and quick popup — 20+ pen styles and tool/color changes via circle, hold or gesture *[shown_working]*
- Math recognition — Flask backend with Pix2Text parses handwritten formulas *[claimed]*
- Handwritten table of contents — Detects titles and subtitles and builds a clickable index *[claimed]*
- Smart Summarize — Collects titles, boxed items and formulas from several notes into one Total Note *[claimed]*
- Sticky notes and stroke links — Hidden notes behind text; strokes become links to files or sites *[claimed]*
- Autosave and Drive sync — IndexedDB locally, JSON synced to Google Drive *[claimed]*

**Flow:** Open the web canvas and write with a stylus → Draw a modifier gesture to format or group content → Circle or hold for the quick tool popup → Generate a table of contents or Total Note → Notes autosave and sync to Drive

**Prompt:** Most Novel Use of AI in the Ethical AI track; hackathon page gives only the name.
**Fit (implied):** Uses a custom-trained stroke-gesture model so handwriting itself becomes the interface for formatting and structuring notes.  *(targeted: [HACKUMASS] [Ethical AI] Most Novel Use of AI)*
**AI:** Custom TensorFlow.js hybrid model on image plus geometric stroke features, trained in Keras on 4,000+ hand-written samples augmented to 36,000+; Pix2Text for math OCR.
**Architecture:** Vanilla JS canvas front end with IndexedDB; TF.js in-browser gesture inference; Flask server for Pix2Text and Google Drive API sync.
**Novelty:** Trained its own gesture-recognition model on self-collected handwriting data and treats pen gestures as a command language, rather than calling a hosted LLM.
**Scope:** medium · working: Live GitHub Pages demo linked; broad feature list; no repo link or video on the page. · polish: Many features beyond core; authors note known bugs and weaker math solver.
**Claims:** Expanded 4,000+ samples to 36,000+ for training | Says interaction is smooth and real-time, no metrics
**Gaps:** no repo in dataset; page did not link repo; live demo not opened
Sources: https://devpost.com/software/onepen, https://hackumass-xiii.devpost.com/

---

### Pacific
*HackUMass HackUMass XIII · dataset: winners · tier: track_winner · evidence A · confidence medium*
**Prizes:** [HACKUMASS] [Ethical AI] Best Theory and Plan

**What it is:** A Rust and wgpu implementation of radiance cascades, a real-time global-illumination technique, with cascades generated in a compute shader and shown through a fragment shader. The working version is 2D.
**Problem / user:** Graphics developers wanting sharp real-time global illumination without heavy ray counts and denoising.

**Features**
- Radiance cascade lighting in 2D — Light probes sample dense short rays near and sparser long rays farther away *[shown_working]*
- GPU pipeline — Compute shader builds cascades; fragment shader composites result *[claimed]*
- Light-source ray intersection — Handled like standard ray tracing *[claimed]*
- 3D extension — Next step *[planned]*

**Flow:** Install Rust → Clone repo and run cargo run --release → View the lit 2D scene

**Prompt:** Best Theory and Plan in the Ethical AI track; hackathon page gives only the name.
**Fit (none):** Page explains the rendering-equation background and why cascades beat denoised ray tracing; no AI content.  *(targeted: [HACKUMASS] [Ethical AI] Best Theory and Plan)*
**AI:** none
**Architecture:** Rust program on wgpu with WGSL shaders and a teammate-built V4 game engine for shader plumbing; compute pass to fragment pass.
**Novelty:** Reimplements a recent graphics technique from sparse papers; no AI or app layer, unusual among entries.
**Scope:** tiny · working: README gives run command; no video or screenshots mentioned; about 300 LOC est. · polish: Minimal README; no demo assets.
**Claims:** Says it implemented a novel technique in a short time
**Gaps:** no visuals seen
Sources: https://devpost.com/software/pacific, https://github.com/gabefork/pacific (evidence file), https://hackumass-xiii.devpost.com/

---

### PixelParty
*HackUMass HackUMass XIII · dataset: winners · tier: overall_top3 · evidence A · confidence high*
**Prizes:** Winner Third Prize [3rd]

**What it is:** A 64x64 LED matrix driven by a Raspberry Pi that mirrors a shared web drawing canvas in real time, so friends anywhere can paint on the physical panel together.
**Problem / user:** Friends wanting a physical, shared creative display that makes remote interaction feel present.

**Features**
- Shared web canvas — Pixel grid plus RGB color picker served by Flask *[shown_working]*
- Real-time sync to LED panel — Separate panel process fed over a pipe updates the hardware as strokes arrive *[shown_working]*
- Multi-user drawing — Concurrent edits kept consistent between web canvases and the panel *[shown_working]*
- Public deployment — Reachable on a custom domain *[shown_working]*
- Saving, per-device canvases, games — Listed next steps *[planned]*

**Flow:** Open the PixelParty site → Pick a color → Draw on the pixel grid → See strokes on every browser and the physical panel instantly

**Prompt:** Overall Third Prize at HackUMass XIII; chosen from all projects, no track text.
**Fit (none):** No stated prize target; automatically considered for overall prizes.  *(targeted: Third Prize)*
**AI:** none
**Architecture:** Flask server (Python) with JS canvas; launches a multi-threaded panel process linked by a pipe; rpi-led-matrix drives a 64x64 Adafruit panel from a Raspberry Pi 3 B+ without the IO hat.
**Novelty:** Physical hardware shared canvas wired without the standard IO hat; first hackathon for the team per the page.
**Scope:** small · working: Live domain, demo video and photo of panel beside website. · polish: Small codebase (about 380 LOC); README sets out run command and inspiration.
**Claims:** Says panel and web canvas stay in sync in real time for all users
**Gaps:** video not watched
Sources: https://devpost.com/software/pixelparty, https://github.com/AshwinSarma21/PixelParty (evidence file), https://hackumass-xiii.devpost.com/

---

### Plotholes
*HackUMass HackUMass XIII · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** [MLH] Best Use of Snowflake API

**What it is:** A geospatial web platform that maps NYC road-damage reports, scores severity by neighborhood, routes drivers around damaged streets and lets users upload photos that a pothole-segmentation model rates. Natural-language questions convert to SQL through Snowflake Cortex.
**Problem / user:** Drivers wanting smoother routes and city planners needing to prioritize road repairs.

**Features**
- Interactive damage map — Leaflet map of NYC 311 reports, heatmaps and neighborhood risk choropleths with layer toggles *[shown_working]*
- Damage-avoiding route planning — OpenStreetMap routes between two points avoiding recorded damage *[claimed]*
- Photo reporting with severity — YOLOv8 pothole segmentation model assigns severity to an uploaded image and location *[claimed]*
- Severity scoring and aggregation — Shapely point-in-polygon rolls issues into neighborhoods, GeoJSON out *[claimed]*
- Natural-language querying — Snowflake Cortex turns questions into SQL *[claimed]*
- Dataset upload — Uploads update the map live *[claimed]*

**Flow:** Open map and toggle raw, heat or risk layers → Enter start and end for a safer route → Upload a photo and place a pin to report damage → Ask questions in plain language → Use neighborhood summaries to plan repairs

**Prompt:** MLH Best Use of Snowflake API: build apps using Snowflake REST API and LLMs.
**Fit (explicit):** Uses Snowflake storage and Cortex to translate natural-language questions about road conditions into SQL; README states it won this award.  *(targeted: MLH Best Use of Snowflake API)*
**Sponsor tools:** Snowflake / Cortex (data store and natural-language-to-SQL querying, supporting)
**AI:** YOLOv8n pothole segmentation model from Hugging Face on user photos; Snowflake Cortex LLM for text-to-SQL.
**Architecture:** Next.js/Leaflet front end; Flask API with Shapely and OSM routing; Supabase and Snowflake stores; NYC 311 and crowd reports as data.
**Novelty:** Pairs public 311 data, user photo reports, routing and an LLM query layer in one civic tool; pivoted from Amherst/Boston to NYC for data volume.
**Scope:** medium · working: Live site at project domain; sizeable frontend and backend directories; no video. · polish: Multiple map layers, report drawer, upload box; around 3.8k LOC; no tests.
**Claims:** Claims scalable full-stack geospatial platform; no metrics
**Gaps:** live site not opened
Sources: https://devpost.com/software/plothole, https://github.com/GraceW03/Plotholes (evidence file), https://hackumass-xiii.devpost.com/

---

### Racing Sim Pedal Set
*HackUMass HackUMass XIII · dataset: winners · tier: track_winner · evidence A · confidence medium*
**Prizes:** [HACKUMASS] [Hardware] Best Mechanical Hack

**What it is:** A custom-machined three-pedal set (clutch, brake, accelerator) for racing simulators, built from aluminum blocks with bearings, Hall-effect sensors and brake load cells, read by a Raspberry Pi Pico that presents as a USB game controller.
**Problem / user:** Sim-racing hobbyists, here the builders themselves, wanting rig-mountable pedals recognized as an HID gamepad.

**Features**
- Machined pedal assembly — Aluminum blocks with bearings on a clamped stationary rod, mountable to a rig *[shown_working]*
- Hall-effect clutch and throttle — Sensors read pedal travel *[claimed]*
- Load-cell brake — Load cells measure brake pressure *[claimed]*
- HID game controller output — Pico firmware in C reports axes to the game *[shown_working]*

**Flow:** Mount pedals to a rig → Plug in over USB → Press pedals in a racing game

**Prompt:** Best Mechanical Hack in the Hardware category; hackathon page gives only the name.
**Fit (implied):** Most effort went into machining the mechanical pedal parts in the makerspace machine shop.  *(targeted: [HACKUMASS] [Hardware] Best Mechanical Hack)*
**AI:** none
**Architecture:** Mechanical pedal frame with three sensors feeding a Raspberry Pi Pico running C that exposes an HID gamepad.
**Novelty:** Fully custom-machined hardware project with little software, unlike most entries.
**Scope:** small · working: Page says it works in racing games; one photo; tiny repo (about 100 LOC est.). · polish: Minimal documentation; sensitivity tuning listed as future work.
**Claims:** Says it works in racing games
**Gaps:** no demo video
Sources: https://devpost.com/software/racing-sim-pedal-set, https://github.com/audtheshaud/racing-sim-pedals (evidence file), https://hackumass-xiii.devpost.com/

---

### Reddit's Mood
*HackUMass HackUMass XIII · dataset: winners · tier: sponsor_winner · evidence A · confidence medium*
**Prizes:** [MLH] Best .Tech Domain Name

**What it is:** A website with a 3D globe that shows the emotional tone of Reddit posts from countries around the world, with Gemini scoring each post. Built with Django, Spline/three.js visuals and hosted on Vultr.
**Problem / user:** Curious viewers who want an at-a-glance view of global mood from social media.

**Features**
- 3D mood globe — Spline/three.js planet displays posts and their emotions by country *[shown_working]*
- Reddit scraping — Pulls posts via Reddit API *[claimed]*
- Gemini emotion analysis — Gemini rates intensity and type of emotion per post *[claimed]*
- Live site — Deployed at project .tech domain *[shown_working]*

**Flow:** Visit the site → Explore the globe → See emotions of posts per country

**Prompt:** MLH .Tech Domain Name: win a .tech domain to showcase and expand a project.
**Fit (implied):** Project is hosted on its own .tech domain; the prize is about a domain, so fit is the registered site.  *(targeted: MLH Best .Tech Domain Name, MLH Best Use of Gemini API, Best Use of Vultr)*
**Sponsor tools:** .Tech domain (project site address, token); Google Gemini API (emotion analysis of posts, core); Vultr (hosting backend, supporting)
**AI:** Gemini classifies emotion and intensity of scraped Reddit posts; no custom model.
**Architecture:** Django backend on Vultr scrapes Reddit, calls Gemini, serves data to a Framer/Spline/three.js front end.
**Novelty:** Visualizes sentiment on a 3D globe rather than a chart; small data pipeline behind a design-led front end.
**Scope:** small · working: Live site linked; Django app (about 2.3k LOC est.). · polish: Preview image in README; Spline planet; team says accuracy still to improve.
**Gaps:** live site not opened
Sources: https://devpost.com/software/reddit-s-mood, https://github.com/aamir-azeez/redditsmood (evidence file), https://hackumass-xiii.devpost.com/

---

### Resi
*HackUMass HackUMass XIII · dataset: winners · tier: track_winner · evidence A · confidence high*
**Prizes:** [HACKUMASS] [Ethical AI] Best Beginner AI Hack

**What it is:** A voice-first Expo/React Native app for campus housing where residents describe a maintenance or resident-life problem in a spoken conversation; AI turns it into a classified ticket that appears in live queues for Maintenance and RA staff.
**Problem / user:** UMass residents who rely on forms, calls or emails for dorm issues, and the maintenance and resident-assistant staff who triage them.

**Features**
- Voice reporting conversation — Resident speaks; Whisper/Vapi transcribes, AI asks clarifying questions and replies by voice *[shown_working]*
- Ticket classification — OpenAI classifies into Maintenance or Resident Life and extracts urgency, location, issue type and summary *[shown_working]*
- Role-based dashboards — Maintenance and RA views with urgency filters, live queue ordering, status updates and weekly closed tickets *[shown_working]*
- Resident queue view — Residents see open queue position and closed history *[shown_working]*
- Auth and persistence — Firebase email/password auth, restricted to campus accounts; tickets in Realtime Database *[shown_working]*
- Push notifications, image upload, FMX integration, analytics — Listed as next steps *[planned]*

**Flow:** Pick a role and sign in → Resident records the issue by voice → AI asks follow-up questions → Ticket created and routed with queue position → Staff watch the live dashboard and update status

**Prompt:** Best Beginner AI Hack in the Ethical AI track; hackathon page gives only the name (track text asks for agents benefiting the campus community).
**Fit (implied):** A voice agent serving campus housing residents and staff, aligned with the track's campus-community framing.  *(targeted: [HACKUMASS] [Ethical AI] Best Beginner AI Hack)*
**Sponsor tools:** Vapi (real-time voice calls and webhook ticket creation, supporting); ElevenLabs (voice preview endpoint, token)
**AI:** OpenAI Whisper transcription, GPT-4-class model for conversation and classification, text-to-speech replies; Vapi handles live voice calls.
**Architecture:** Expo app (web/iOS/Android) to Node/Express server on Render handling audio, OpenAI and Vapi webhooks; Firebase Auth and Realtime Database store tickets.
**Novelty:** Applies a conversational voice agent to campus housing triage with role-specific live queues across web and mobile.
**Scope:** medium · working: Live Render demo, demo video, detailed README; about 7.8k LOC est. · polish: Three role flows, Docker and CI files present; no tests.
**Claims:** Voice request submission in under a minute | Queue positions sync every 5 seconds
**Gaps:** repo is named MoveMate but README describes Resi
Sources: https://devpost.com/software/resi, https://github.com/RavjeetChahal/MoveMate/ (evidence file), https://hackumass-xiii.devpost.com/

---

### SlideScribe
*HackUMass HackUMass XIII · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** [MLH] Best Use of ElevenLabs

**What it is:** A Flutter phone app that watches a classroom screen with the camera, detects slide changes, interprets slide content with OCR and Gemini, and answers spoken questions through ElevenLabs speech so blind students can follow presentations.
**Problem / user:** Blind and visually impaired students who cannot see slide images, charts and text in lectures.

**Features**
- Slide change detection — Camera frames compared via CLIP embeddings and OCR text matching on a FastAPI backend *[claimed]*
- Slide interpretation — EasyOCR plus Gemini summarize text, lists and images *[claimed]*
- Spoken Q&A — ElevenLabs speech-to-text captures questions, a lightweight LLM via OpenRouter answers, ElevenLabs TTS replies *[claimed]*
- Revisit earlier slides — Users ask about earlier slides they could not see *[claimed]*
- Remote camera sharing — Optional Node signaling server for sharing camera *[claimed]*

**Flow:** Point phone at the presentation → App detects each new slide → Ask a question aloud → Hear a spoken answer in earbuds without disturbing the presenter

**Prompt:** MLH Best Use of ElevenLabs: create realistic, dynamic, emotionally expressive voices.
**Fit (explicit):** ElevenLabs provides both speech-to-text for questions and text-to-speech for spoken answers, the core interface for blind users.  *(targeted: MLH Best Use of ElevenLabs, [HACKUMASS] [PIT] Best Accessibility Hack (considered))*
**Sponsor tools:** ElevenLabs (speech-to-text for questions and text-to-speech answers, core); Google Gemini API (slide summarization, supporting)
**AI:** CLIP embeddings and OCR detect slide changes; Gemini summarizes slides; OpenRouter LLM answers questions; ElevenLabs STT and TTS form the voice loop.
**Architecture:** Flutter mobile client; FastAPI Python backend for capture and slide analysis; optional Node signaling server; external Gemini, OpenRouter and ElevenLabs APIs.
**Novelty:** Accessibility voice assistant that tracks slides from a live camera and supports questions about past slides.
**Scope:** medium · working: Demo video and a multi-platform Flutter project with backend; about 9.8k LOC est. · polish: Detailed README and setup steps; has tests flag in repo.
**Claims:** Says no special hardware or setup needed
**Gaps:** no accuracy data; README calls the app SightScribe too
Sources: https://devpost.com/software/and_then_there_was_light, https://github.com/SuyashManiyar/HackUMass_codebase (evidence file), https://hackumass-xiii.devpost.com/

---

### Soundbrush
*HackUMass HackUMass XIII · dataset: winners · tier: overall_top3 · evidence A · confidence medium*
**Prizes:** Winner Grand Prize [1st]

**What it is:** A web drawing app where each of eight hues is tied to a synth note, so a user hears the color they are painting. It has a color wheel, lightness and saturation sliders, a color-name readout, undo/redo and save/load.
**Problem / user:** Visually impaired artists who need a non-visual way to identify the color being drawn.

**Features**
- Color-to-sound mapping — Eight Tone.js synth notes each linked to a hue, played while drawing *[shown_working]*
- Color controls — Color wheel for hue, sliders for lightness and saturation, name of color displayed *[shown_working]*
- Freehand canvas — p5.js canvas in a Next.js app *[shown_working]*
- Undo and redo — Step through strokes *[claimed]*
- Save and load sketches — Saved sketches reopen from a dropdown *[claimed]*

**Flow:** Pick a hue and adjust sliders → Draw while hearing the note and seeing the color name → Undo or redo → Save or load a sketch

**Prompt:** Grand Prize (first place overall) at HackUMass XIII; all projects automatically considered.
**Fit (none):** No stated prize target; it addresses an accessibility use case without claiming that track.  *(targeted: Grand Prize)*
**AI:** none
**Architecture:** Next.js/React front end with p5.js canvas and Tone.js synths; sketch state saved client-side.
**Novelty:** Sonifies color for drawing, evolved from an earlier p5.js keyboard-note-to-color sketch; no AI or backend.
**Scope:** small · working: Page calls it functional and stable; no demo link or video; about 1.1k LOC est. · polish: Figma design mostly implemented; README is the default Next.js template.
**Claims:** Says drawing is fluid, functional and stable
**Gaps:** no demo or video; README is boilerplate
Sources: https://devpost.com/software/sound-art-app, https://github.com/maxdopp/SoundBrush (evidence file), https://hackumass-xiii.devpost.com/

---

### TabSense
*HackUMass HackUMass XIII · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** [MLH] Best Use of Gemini API

**What it is:** A Chrome extension that uses Gemini to sort open tabs into categories like Work, Social or Entertainment, creates color-coded tab groups and tracks time spent in each category, with a popup for search and tab control.
**Problem / user:** Chrome users with many open tabs who find manual tab grouping tedious.

**Features**
- AI tab categorization — Heuristics by domain first, then page content sent to Gemini for a semantic category *[shown_working]*
- Automatic color-coded groups — Tabs grouped by category in the browser *[shown_working]*
- Time tracking per category — tabs.onActivated events accumulate time in extension storage *[shown_working]*
- Popup management — Search, activate or close tabs from the popup *[shown_working]*
- Chatbot, themes, analytics charts — Listed as future *[planned]*

**Flow:** Install unpacked extension → Extension classifies open tabs → Tabs are grouped and colored → Open popup to view groups and minutes per category

**Prompt:** MLH Best Use of Gemini API: build AI-powered apps with the Gemini API.
**Fit (explicit):** Gemini does the content-based classification that drives grouping.  *(targeted: MLH Best Use of Gemini API)*
**Sponsor tools:** Google Gemini API (classifying tab content into categories, core)
**AI:** Hybrid classifier: domain heuristics plus Gemini analysis of extracted tab content, results cached in extension storage.
**Architecture:** Chrome extension background script and popup; a Render-hosted server relays Gemini calls; storage in chrome.storage.local.
**Novelty:** A small, common extension idea; combines AI grouping with usage timing.
**Scope:** small · working: README with install steps and mechanics, screenshots; no video or live demo; about 840 LOC est. · polish: Popup UI screenshots; team notes slow rendering waiting on backend.
**Gaps:** no demo video
Sources: https://devpost.com/software/tabsense-7dh05r, https://github.com/anshuanjna/TabSense (evidence file), https://hackumass-xiii.devpost.com/

---

### Tandem
*HackUMass HackUMass XIII · dataset: winners · tier: track_winner · evidence A · confidence medium*
**Prizes:** [HACKUMASS] [Software] Best Beginner Software

**What it is:** A web app where UMass students register, post a planned or in-progress study session for a class with time and location, and others in that class browse and join it.
**Problem / user:** Students who want a study partner right now in a specific class; the campus Study Buddies tool only lists contacts.

**Features**
- Registration and login — Account creation and authentication *[shown_working]*
- Post a study session — Pick a class, time and location, now or planned *[shown_working]*
- Browse sessions by class — See sessions others posted for the same course *[shown_working]*
- Join a session — Opt in to another student's appointment *[shown_working]*
- Chat, notifications, profiles — Listed as next steps *[planned]*

**Flow:** Register → Post a session for a class → Classmates view the listing → A student joins

**Prompt:** Best Beginner Software in the Software category; hackathon page gives only the name.
**Fit (implied):** A first-hackathon full-stack web app solving a campus study-matching need; hosted on a .tech domain.  *(targeted: [HACKUMASS] [Software] Best Beginner Software, MLH .Tech Domain Name)*
**Sponsor tools:** .Tech domain (custom domain for the deployed app, token)
**AI:** none
**Architecture:** FastAPI backend with SQLAlchemy models for classes, students and appointments; HTML/JS front end; hosted on Render with custom domain.
**Novelty:** Real-time, ad hoc study matching tied to course data from the campus directory; no AI.
**Scope:** small · working: Live Render URL and custom domain; about 4k LOC across 49 files. · polish: Multi-page front end with images and CSS; README only links the site.
**Gaps:** README minimal
Sources: https://devpost.com/software/tandem-t0zvo4, https://github.com/paperfour/tandem (evidence file), https://hackumass-xiii.devpost.com/

---

### Vault
*HackUMass HackUMass XIII · dataset: winners · tier: track_winner · evidence B · confidence low*
**Prizes:** [HACKUMASS] [Software] Best Mobile Hack

**What it is:** A Swift iOS app that blocks chosen apps when the phone is at selected geofenced places such as the gym or dining hall, aimed at cutting public phone distraction.
**Problem / user:** People who want to stop being glued to their phones in public settings like gyms and dining halls.

**Features**
- Location-based app blocking — Selected apps are blocked inside geofenced locations *[claimed]*
- Local storage — SQLite stores settings *[claimed]*

**Prompt:** Best Mobile Hack in the Software category; hackathon page gives only the name.
**Fit (implied):** Native iOS app using location services.  *(targeted: [HACKUMASS] [Software] Best Mobile Hack)*
**AI:** none
**Architecture:** Swift iOS app using MapKit location features and SQLite storage (inferred from tags).
**Novelty:** Blocks apps by place instead of by time; page is a very short summary.
**Scope:** small · working: Demo video and screenshots on Devpost; repo not readable. · polish: Unknown; page has little detail.
**Gaps:** repo clone failed; user flow, challenges and next steps absent from page
Sources: https://devpost.com/software/vault-mk1l65, https://hackumass-xiii.devpost.com/

---

