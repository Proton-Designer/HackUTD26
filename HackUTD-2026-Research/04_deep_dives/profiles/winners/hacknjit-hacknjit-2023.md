# HackNJIT — HackNJIT - 2023 (4 projects)

### Coralations
*HackNJIT HackNJIT - 2023 · dataset: winners · tier: track_winner · evidence A · confidence high*
**Prizes:** Best First-Year Hack [1st]

**What it is:** Educational GoDaddy-hosted website about Caribbean coral bleaching with two interactive Folium maps (bleaching severity by reef, and CO2 emissions of nearby countries by year) and an embedded Kommunicate chatbot answering general questions.
**Problem / user:** Coral bleaching in the Caribbean may correlate with CO2-driven warming; the site serves interested members of the public.

**Features**
- Bleaching severity map — Folium HTML map of Caribbean reef bleaching built from a Zenodo reef dataset. *[shown_working]*
- CO2 emissions map — Map of emissions for countries nearest each reef by year, from Zenodo/Kaggle records merged with Pandas on country and year. *[shown_working]*
- Info chatbot — Kommunicate.io bot trained on Caribbean and bleaching facts, embedded as HTML. *[shown_working]*
- Hosted site — Built with GoDaddy website builder on a GoDaddy domain. *[shown_working]*

**Flow:** Open the site → Explore bleaching map → Explore CO2 map by year → Ask the chatbot questions

**Prompt:** HackNJIT 2023 Best First-Year Hack: a team of 50% or more freshmen; theme of the event was Nautical. GoDaddy Registry domain prize also existed.
**Fit (implied):** Marine-science topic fits the nautical theme; README says the team were students from a marine-science high school. First-year status is not stated on the page.  *(targeted: Best First-Year Hack, GoDaddy Best Domain Name (tagged))*
**Sponsor tools:** GoDaddy (domain and website builder hosting the project, core); Kommunicate.io (chatbot builder, supporting)
**AI:** No custom model; a no-code chatbot builder trained on provided facts.
**Architecture:** Pandas merges Zenodo and Kaggle datasets, Folium exports HTML maps, embedded into a GoDaddy site with a Kommunicate chat widget.
**Novelty:** Mostly no-code assembly, notable for pairing two public datasets to visualise a possible CO2 and bleaching link.
**Scope:** tiny · working: Live GoDaddy site link on Devpost; README and page agree on features. · polish: Simple site with two maps; no video, no metrics or analysis of the correlation.
**Gaps:** no correlation results reported
Sources: https://devpost.com/software/name-po5230, https://raw.githubusercontent.com/dudghks/HackNJIT-2023/main/README.md, https://hacknjit-2023.devpost.com/

---

### SeaSOS
*HackNJIT HackNJIT - 2023 · dataset: winners · tier: overall_top3 · evidence A · confidence medium*
**Prizes:** 3rd Place [3rd]

**What it is:** Cruise-ship operations and emergency app: a FastAPI/Redis backend handles onboarding, staff management and emergency protocols, and an iOS app with Unity and ARKit guides passengers along routes to the nearest exits.
**Problem / user:** Ship operators and staff need organized emergency response and passenger guidance; built for the nautical and patient-safety challenge themes.

**Features**
- AR evacuation guidance — iOS app with Unity/ARKit shows passengers the way to the nearest exit. *[claimed]*
- Route calculation — Algorithms compute evacuation routes under time pressure. *[claimed]*
- Onboarding and staff management — Backend features for passengers and staff. *[claimed]*
- Emergency protocol automation — Backend triggers organized emergency response. *[claimed]*
- Redis as primary store — Redis and Redis Stack used for data, not only caching. *[claimed]*
- AWS infrastructure — Cognito, API Gateway and EC2 behind the API. *[claimed]*

**Flow:** Passenger onboarded → Emergency declared → Staff protocols fire → Passenger opens AR view → App guides to nearest exit

**Prompt:** HackNJIT 2023 third place overall ($500 split); event theme Nautical, with sponsor prizes for Redis Cloud and AWS and a Patient Safety Technology Challenge.
**Fit (implied):** Nautical setting plus safety focus; Devpost says the idea came from a nautical hackathon with patient safety on the high seas and credits Redis and AWS.  *(targeted: 3rd Place, Redis Cloud (implied), AWS (implied))*
**Sponsor tools:** Redis / Redis Stack (primary data store, core); AWS (Cognito, API Gateway, EC2) (auth, API and hosting, supporting)
**AI:** none
**Architecture:** Swift iOS app with Unity/ARKit module calling a FastAPI backend on AWS (API Gateway, EC2, Cognito) that stores data in Redis.
**Novelty:** AR exit navigation on a ship with Redis as the main database in a 25-hour build.
**Scope:** small · working: README links a YouTube demo (not watched); Devpost lists no video and no metrics; backend lives on a separate branch. · polish: Main branch has only two files and says instructions are coming; little visible code.
**Claims:** Built in a 25-hour coding marathon
**Gaps:** code not on main branch; video content unknown
Sources: https://devpost.com/software/seasos, evidence/hacknjit-hacknjit-2023-seasos.json (README), https://hacknjit-2023.devpost.com/

---

### Treasure Snap!
*HackNJIT HackNJIT - 2023 · dataset: winners · tier: overall_top3 · evidence A · confidence high*
**Prizes:** 2nd Place [2nd]

**What it is:** Pirate-themed photo scavenger game in Streamlit: players pick an image another user uploaded and try to find where it was taken, then upload their own photo from the spot; GPS from EXIF and CNN image similarity decide whether they found the treasure.
**Problem / user:** Geocaching and GeoGuessr style fun for players who like location puzzles and uploading challenges.

**Features**
- Challenge browsing — Players choose from user-uploaded location images. *[shown_working]*
- Dual verification — Attempt photo must match by EXIF GPS proximity and CNN cosine similarity (VGG16 per creator bio). *[shown_working]*
- Treasure profile — Wins stored on user profile; goal is collecting seven treasures. *[shown_working]*
- User uploads with riddles — Players add their own challenge with a treasure and riddle. *[shown_working]*
- Accounts and storage — Streamlit multipage app with MongoDB Atlas on AWS holding users, images and metadata. *[shown_working]*

**Flow:** Sign up or log in → Choose a challenge image → Travel to the place and take a photo → Upload attempt → See wrong-location message or treasure award → View treasures on profile

**Prompt:** HackNJIT 2023 second place overall ($1,000 split); theme Nautical; sponsor prize for Best Use of Streamlit existed.
**Fit (implied):** Pirate treasure hunt satisfies the nautical theme; Streamlit is the core framework, though no sponsor prize is claimed.  *(targeted: 2nd Place, Best Use of Streamlit (implied))*
**Sponsor tools:** Streamlit (whole app UI and pages, core); MongoDB Atlas on AWS (users, images and treasures, core)
**AI:** CNN embeddings of attempt and target images compared by cosine similarity, combined with EXIF GPS distance as an anti-cheat check.
**Architecture:** Streamlit pages, MongoDB Atlas (free M0 on AWS) storing users and image blobs with metadata, CNN similarity module.
**Novelty:** Combines EXIF GPS and learned image similarity for a location-verified treasure hunt.
**Scope:** small · working: Features described in detail with screenshot captions; not deployed publicly; no video. · polish: About 230 LOC of repo code, no tests; free MongoDB tier slowed image fetch, stalling the key feature.
**Gaps:** no demo or video
Sources: https://devpost.com/software/treasure-snap, evidence/hacknjit-hacknjit-2023-treasure-snap.json (README), https://hacknjit-2023.devpost.com/

---

### Wager Whales
*HackNJIT HackNJIT - 2023 · dataset: winners · tier: overall_top3 · evidence A · confidence medium*
**Prizes:** 1st Place [1st]

**What it is:** Play-money betting site on aquarium live streams: users draw a target area on a stream and bet coins that a fish will swim into it within a set time; YOLOv8 detects fish and the balance updates with the result.
**Problem / user:** Entertainment project for visitors who like betting on fish movement; states no real currency was used.

**Features**
- Login and starting balance — Registration, login and a generated starting coin balance. *[claimed]*
- Live aquarium streams — Restreams public aquarium feeds with OpenCV; two streams at submission. *[shown_working]*
- Draw-an-area bets — User selects a region on the video and wagers coins a fish will enter it within a time limit. *[shown_working]*
- YOLOv8 fish detection — Detector runs on the selected frame region to settle each bet. *[shown_working]*
- Docker and generated SDK — Containerized backend; SDK generated from FastAPI OpenAPI spec. *[claimed]*

**Flow:** Register or log in → Pick a stream → Draw target area → Place coin bet and timer → Result updates balance

**Prompt:** HackNJIT 2023 first place "Best in Show" ($1,500 split); event theme was Nautical.
**Fit (implied):** Aquatic (oceanic) betting fits the nautical theme; Devpost says the idea began from oceanic trackers.  *(targeted: 1st Place (Best in Show))*
**AI:** YOLOv8-style fish detector (README mentions darknet-format weights in a yolofish folder) applied to user-selected stream regions.
**Architecture:** Vue 3 + Naive UI front end, FastAPI backend, OpenCV restream and detection, Docker, live site wagerwhales.club.
**Novelty:** Turns existing public aquarium streams into a real-time vision-settled betting game; team built a restream layer to avoid lag.
**Scope:** small · working: Live domain listed and README gives run script; no video; no accuracy data. · polish: Front-end UI was the highlighted polish; model weights are external and fish detection was hard to integrate.
**Gaps:** repo not read beyond README; detector accuracy unknown
Sources: https://devpost.com/software/wager-whales, https://raw.githubusercontent.com/chilaxan/Wager-Whale/main/README.md, https://hacknjit-2023.devpost.com/

---

