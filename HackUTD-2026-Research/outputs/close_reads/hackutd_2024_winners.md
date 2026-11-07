# Q19 close read: HackUTD 2024 ("Ripple Effect") winners

Sources read: `04_deep_dives/profiles/winners/hackutd-hackutd-2024.md` (all 35 rows), the 35 `"edition": "HackUTD 2024"` rows in `04_deep_dives/data/deepdive_all.jsonl` and `01_winners/data/project_records.jsonl`, `05_master_winner_lists/HackUTD_winners_master_v2.md`, `04_deep_dives/prompts_cache/hackutd-2024*.md`, `06_hackutd_2026_sponsors/*.md`. Devpost pages could not be re-checked: hackutd-ripple.devpost.com and devpost.com/software/* both returned HTTP 403 on 2026-11-06.

Counts: `scripts/s5_q19_hackutd2024_counts.py` → `data/tables/Q19_hackutd2024_close_read_tags.csv` (one row per project, my hand tags) and `data/tables/Q19_hackutd2024_counts.txt` (every count below with its names).

Scope rules applied:
- **N = 33 included winners.** I excluded 2 of the 35 rows: **Roomie** (evidence C, no Devpost page, year not confirmed) and **The Virtual Fitness Assistant** (its Next Step and Interview Cake badges show under Student Hacks, not HackUTD 2024). No row has `duplicate_of` set.
- **InvestIQ's "First Place" badge is not a HackUTD prize.** `project_records` says the badge sits under the separate "Lightning Fast AI Hackathon" on Devpost. Only Infosys counts as its HackUTD 2024 win. So the 2024 placements we actually know are: Toyota 1st FUELICIENT; Pinata 1st Monch, 2nd Capsule, 3rd Cheddarboxd. The Cheddarboxd 3rd comes from the master list, which cites the Pinata blog; `project_records` marks it "not verified on Devpost".
- **There is no 2024 non-winner baseline.** Every statement below is about prevalence among winners only.
- The 2024 Devpost listed **no public sponsor challenge text**; the challenges were in the kickoff hackerpack. MLH prize text is public. The General track allowed max 2 sponsor challenges per team and a 2-minute demo video.
- Tags used: "core" = the sponsor's product or data is the main thing the project runs on; "problem-only" = the project addresses the sponsor's industry problem without using any sponsor tool or data; "video" = a YouTube URL in project_records or has_video in deepdive (the two files disagree a lot; see Open questions).

---

## 1. Per-project close reads (grouped by track won)

### General track (3 verified; placements not published)

**TalkTuahBank** — https://devpost.com/software/talktuahbank
- Won: General + Goldman Sachs. The README calls it "Overall 1st place". That is self-reported; Devpost does not confirm it.
- What: banking by ordinary phone call (balance, transfer, bill pay) for unbanked adults who have no smartphone or internet.
- Centerpiece: a Retell AI voice agent connected to OpenAI Swarm multi-agent routing that runs backend banking actions, plus a Next.js admin dashboard. It was very visible: the phone call is the demo.
- Worked vs claimed: phone banking, the Swarm actions and the admin dashboard are [shown_working]. Multilingual support and Pinata storage are claimed. Fraud ML and education are planned.
- Goldman integration: problem-only (no Goldman tool exists to use). Pinata is supporting.
- Assets: live site, 2-min video, polished README, architecture screenshot (the only architecture diagram among the 33). Evidence A.

**Lumo** — https://devpost.com/software/pay-your-daddy
- Won: General + Goldman Sachs.
- What: group-expense app that charges each member's own card their share at the moment of purchase, for unbanked and underbanked households pooling rent and groceries.
- Centerpiece: multi-card Stripe charging through an Express/Mongo backend. Visibility is unclear: no live demo; a video URL is in project_records, but deepdive says no video.
- Worked vs claimed: everything is [claimed], including a "fully functional MVP with real transactions". Apple Pay was not achieved. Square itemized splitting is planned.
- Goldman integration: problem-only.
- Assets: 6 screenshots, empty README, 4 commits. Evidence A, but the build itself is thinly documented.
- Inference: the reframing (no one fronts cash) probably carried more weight than technical depth.

**Ripple Banking** — https://devpost.com/software/tbd-z4uir2
- Won: General only.
- What: pop-up micro-banking. Small business owners borrow from big banks and act as local lenders; underbanked consumers find them on a map and apply for loans.
- Centerpiece: a two-sided platform (customer and merchant dashboards, Google Maps). The "ML background check" is claimed with no details. Fairly visible through screenshots and a GIF.
- Worked vs claimed: the map and both dashboards are [shown_working]. The ML check and heat map are claimed.
- Integration: n/a (General only). Its name matches the event theme "Ripple Effect" (inference: deliberate).
- Assets: screenshots, GIF, video URL, ~6k LOC, README stub, no live demo. Evidence A.

*(Excluded: Roomie. The ACM UTD site lists it as "Winner General and Hardware Track", year unconfirmed, evidence C, no Devpost page, no description.)*

### Goldman Sachs (also see Lumo and TalkTuahBank above)

**AllBank** — https://devpost.com/software/allbank
- Won: Goldman Sachs.
- What: React Native banking app for the unbanked and small businesses: QR pay, goal savings, loan planner, doorstep-banking booking, Gemini assistant.
- Centerpiece: breadth across about 8 features on Firebase; no single hard part. The Gemini chat is an add-on.
- Worked vs claimed: all 8 features are [claimed]. There is no demo and no video.
- Goldman integration: problem-only.
- Assets: 11 screenshots, structured README, 45 commits. Evidence A.

### PNC Bank (title sponsor)

**Data Pattern Observatory** — https://devpost.com/software/data-pattern-observatory
- Won: PNC.
- What: data observability system that tracks how organizational data is created, moved and used, with anomaly detection and forecasts in a Streamlit dashboard.
- Centerpiece: a multi-database pipeline (MongoDB, Elasticsearch, TimescaleDB, Redis, Docker) plus statistical models. Low visibility: the video embed points to an unrelated link.
- Worked vs claimed: all [claimed]. A CrewAI agent and a Random Forest were separate experiments that were never integrated.
- PNC integration: problem-only, but the page explicitly says the problem statement came from the PNC challenge.
- Assets: detailed README with setup steps; only 5 commits, all on the final day. Evidence A.

**FinnAI** — https://devpost.com/software/finnai
- Won: PNC.
- What: Streamlit personal-finance app with an AI budgeting chatbot, auto-categorized expenses and savings goals.
- Centerpiece: the chatbot (model not named). Its visibility can't be judged because the video was not viewable.
- Worked vs claimed: all [claimed]. Bank linking and a mobile version are planned.
- PNC integration: problem-only.
- Assets: an embedded video (per deepdive); no repo. Evidence B. The record is thin; Devpost re-check blocked (403).

**Hermes** — https://devpost.com/software/hermes-c2onvq
- Won: PNC.
- What: crypto wallet and investing app for people outside traditional banking (Hispanic community framing), with live prices, news, predictions and risk.
- Centerpiece: a PyTorch LSTM price model, but the record says it is unclear whether the LSTM drives the predictions shown. Live CoinGecko prices are the visible part.
- Worked vs claimed: all [claimed]. Pension-style payouts are planned.
- PNC integration: problem-only.
- Assets: video, one screenshot, default CRA README. Evidence A.

### Toyota (Financial Services)

**FUELICIENT** — https://devpost.com/software/fuelicient
- Won: **Toyota 1st** (confirmed placement).
- What: Streamlit explorer for the Toyota-supplied fuel-efficiency dataset, with accounts, editable saved datasets and CSV export.
- Centerpiece: persistent per-user dataset copies (Firebase auth plus Pinata/IPFS storage). No AI and no modeling. Visible through 3 live links and a video.
- Worked vs claimed: all [claimed], but there are three live deploys.
- Toyota integration: core data (it is built on the challenge dataset).
- Assets: live demos, video, custom domain; no repo. Evidence B. Devpost re-check blocked.

**KaizenDrive** — https://devpost.com/software/project-ip7kgx0314sh
- Won: Toyota.
- What: Streamlit dashboard over four years of Toyota car data, with competitor comparison and a build-your-own dashboard, aimed at engineers.
- Centerpiece: an in-house RAG chatbot (sentence-transformers plus OpenAI) over tabular data; the chatbot is an add-on.
- Worked vs claimed: all [claimed]. Missing values degrade the graphs.
- Toyota integration: core data (inference: "Toyota car data" is likely the challenge dataset).
- Assets: video and Drive demo, minimal README, 57 commits. Evidence A.

**ToyoTrends** — https://devpost.com/software/toyota-car-analytics-app
- Won: Toyota.
- What: React analytics site for Toyota engineers comparing fuel efficiency and emissions across cars, manufacturers and years.
- Centerpiece: deterministic charting (Chart.js over local JSON). The SambaNova chatbot is an add-on.
- Worked vs claimed: lookup and both comparisons are [shown_working]. The chatbot and images are claimed. Predictive emissions is planned.
- Toyota integration: core data (inference; data source unnamed).
- Assets: 5 screenshots, video, intro animation; no repo. Evidence B.

### EOG Resources

**PipeBrAIns** — https://devpost.com/software/pipebrains
- Won: EOG.
- What: dashboard that predicts hydrate blockages in gas pipelines, for pipeline owners.
- Centerpiece: a scikit-learn random forest trained on the EOG challenge data with a hydrate label the team added themselves. Claimed R² ≈ 0.94. Alerts every second, SendGrid email.
- Worked vs claimed: all [claimed]; the video was not viewable.
- EOG integration: core data (explicitly says it used the EOG datasets).
- Assets: video, multi-page dashboard, empty README. Evidence A.

**DHy-n0** — https://devpost.com/software/dhy-n0
- Won: EOG + [MLH] Best .Tech Domain.
- What: hydrate-anomaly monitoring web app for lease operators, with strong branding (mascot, promo video, dhy-n0.tech).
- Centerpiece: Pandas anomaly analysis behind Flask/React/Recharts. The algorithm is unspecified and the code is about 800 LOC. Branding is the most visible part.
- Worked vs claimed: analysis features are [claimed]; only the branding and promo are [shown_working].
- EOG integration: core data (inference: the README says it was built for the EOG hydrate-from-data challenge). The .Tech prize is core by construction.
- Assets: live site, video. Evidence A.

### CBRE / Veolia (property sustainability)

**Eco Fast Track** — https://devpost.com/software/apartment-monitoring
- Won: CBRE + Veolia.
- What: DIY smart water gauge (Arduino, Grove sensors, LCD, 3D-printed case) feeding a Next.js app with usage graphs, Gemini saving tips and over-average email alerts, for property managers and tenants.
- Centerpiece: the hardware-to-web data path. WiFi failed, so it runs over serial. Visible through hardware photos.
- Worked vs claimed: the gauge, graphs and email are [shown_working] as proof of concept. Gemini tips and the Wrapped-style view are claimed. Leak detection is planned.
- Integration: problem-only for both CBRE and Veolia. Pinata is listed with an unclear role.
- Assets: hardware photos, Figma, video URL. Evidence A.

**EcoVerse** — https://devpost.com/software/ecoverse-5dczmp
- Won: CBRE.
- What: Unity VR replica of an office where property managers see energy and water data, talk to a Llama avatar (SambaNova), feel spikes through bHaptics gloves, and invite technicians over Photon.
- Centerpiece: the VR, haptics and multiplayer stack. The data is synthetic (Faker).
- Worked vs claimed: all [claimed]. The page is inconsistent on whether remote joining works.
- CBRE integration: problem-only.
- Assets: large repo, Canva design, an unlabelled Drive file. Evidence A.

**Greenify** — https://devpost.com/software/greenwise-y6o4bu
- Won: CBRE.
- What: emissions calculator and score for office managers, a GPT-4 advice chatbot, and a map of CBRE locations scored by LLaMA 3 over CBRE reports stored in Pinecone.
- Centerpiece: RAG over the sponsor's own reports and location data.
- Worked vs claimed: all [claimed]. The main repo is about 350 LOC with code in other repos; the page is inconsistent on Leaflet vs Google Maps.
- CBRE integration: core data.
- Assets: video and 6 screenshots, high UI polish. Evidence A.

**EcoLens (Sustainable Building Manager)** — https://devpost.com/software/ecolens-pqk62d
- Won: Veolia.
- What: building sustainability dashboard with energy, water and carbon trends plus what-if simulation sliders and a score map.
- Centerpiece: the simulation sliders. No AI.
- Worked vs claimed: all [claimed], from the README only; the Devpost narrative is blank.
- Veolia integration: problem-only.
- Assets: README screenshots; no video or demo. Evidence A on paper but substantively thin.

### Frontier

**FrontierMap** — https://devpost.com/software/frontierbeyond
- Won: Frontier.
- What: an iOS RoomPlan LiDAR scan of a home becomes a 2D floor plan on the web; the user marks the router and the app shows a Wi-Fi coverage heatmap with suggested extender spots, for Frontier internet customers.
- Centerpiece: a geometry pipeline (USDZ → OBJ → 2D plan → placement algorithm). No ML. Highly visible, with a sample file provided for judges.
- Worked vs claimed: plan conversion, placement, heatmap and the live site are [shown_working]. The AR scan is claimed. Multi-story support is planned.
- Frontier integration: problem-only.
- Assets: live demo plus a backup deploy, video, screenshots, Docker. Evidence A with no gaps (the most complete record of the 33).

**Homelander** — https://devpost.com/software/homelander
- Won: Frontier.
- What: two-sided app with plan and add-on recommendations for customers and per-city outage predictions and stats for the company.
- Centerpiece: rule thresholds plus unnamed ML over the provided datasets.
- Worked vs claimed: all [claimed].
- Frontier integration: core data ("provided datasets").
- Assets: live link; no repo, video or screenshots. Evidence B.

**Promising Products** — https://devpost.com/software/promising-products
- Won: Frontier.
- What: product recommender (internet, tech, smart home) for Frontier customers.
- Centerpiece: a hybrid memory- and model-based collaborative-filtering model. The dataset is unnamed.
- Worked vs claimed: all [claimed]. Social sharing is planned.
- Frontier integration: problem-only (the dataset source is unknown).
- Assets: video URL, 3 brainstorm screenshots, about 700 LOC. Evidence A.

### Infosys

**InvestIQ** — https://devpost.com/software/investiq-1b0cio
- Won: Infosys (its "First Place" badge belongs to another hackathon, see Scope rules).
- What: chat-based investing tool where beginners describe a strategy in plain English, AutoGen agents code it, it is backtested on simulated data, and a vision model reviews the charts.
- Centerpiece: the agent → strategy code → backtest loop (Llama 3.1 8B and 90B Vision on SambaNova).
- Worked vs claimed: all [claimed]. Live trading is planned.
- Infosys integration: unknown (the fit is not described).
- Assets: 4 screenshots, detailed README, video URL. Evidence A.

### Pinata (placements known)

**Monch** — https://devpost.com/software/monch-e5k0hv
- Won: **Pinata 1st**.
- What: estimates macros from a meal photo and tracks them against the user's goals.
- Centerpiece: a self-trained image classifier ("built without ChatGPT-style API calls") plus a nutrition lookup. Visible because classification is [shown_working] (the hotdog example).
- Worked vs claimed: classification is shown working; macros, graphs and Clerk auth are claimed.
- Pinata integration: core (images and data).
- Assets: monch.tech live, video. Evidence A.

**Capsule** — https://devpost.com/software/capsule-lp540f
- Won: **Pinata 2nd**.
- What: upload emergency documents (medical, pet) into a "capsule" and share it by URL, QR code or NFC card.
- Centerpiece: Pinata as the entire storage and metadata layer with signed URLs and no other database, plus the physical NFC/QR sharing.
- Worked vs claimed: capsules, sharing and editor pages are [shown_working]. Passwords and emergency alerts are planned.
- Pinata integration: core.
- Assets: live Vercel app, 5 screenshots; no repo or video. Evidence B.

**Cheddarboxd** — https://devpost.com/software/cheddarboxd
- Won: Pinata (3rd per master list) + Best Solo Hack.
- What: a joke "Letterboxd for cheese" social PWA, built solo.
- Centerpiece: none beyond a working SvelteKit PWA with Pinata storage (about 1.2k LOC).
- Worked vs claimed: all [claimed].
- Pinata integration: core (what exactly it stores is not stated).
- Assets: video; template README. Evidence A.

### SambaNova

**Backtracc** — https://devpost.com/software/project-cd41lvjbiorw
- Won: SambaNova + Hardware + [MLH] Cloudflare (3 prizes, the most of any 2024 project).
- What: an in-car rig for rideshare. Back-seat ultrasonic sensors detect riders leaving, a webcam photographs the cabin, a SambaNova vision LLM lists forgotten items, and the rider gets a push notification.
- Centerpiece: a three-codebase embedded → hub → server chain (Pico W C++, Pi 4 Python, Express), a 3D-printed enclosure, Terraform and CI. Very visible because the physical rig sits on the table.
- Worked vs claimed: every core feature is [shown_working].
- Integration: SambaNova core; Hardware core. **Cloudflare was DNS only (token)**, even though the MLH prompt asks for Workers AI and similar services.
- Assets: backtracc.tech live, video URL in project_records, tests, Docker; README is an unfilled template. Evidence A.

**Notable** — https://devpost.com/software/pipeview
- Won: SambaNova.
- What: AI lecture notes: live transcription, natural-language editing, Mermaid diagram generation, voice assistant, crewAI web context, share and PDF export.
- Centerpiece: low-latency SambaNova inference across many AI features, with a Terraform-managed AWS deploy.
- Worked vs claimed: all [claimed].
- SambaNova integration: core.
- Assets: Vercel demo and live API docs; README stub; no video. Evidence A.

**Vestique** — https://devpost.com/software/vestique
- Won: SambaNova + [MLH] Best Use of Streamlit.
- What: wardrobe assistant. A vision LLM classifies clothing photos, the app logs wear, emails about unworn items, and suggests resale.
- Centerpiece: a Llama 3.2 11B Vision → wear-log → Brevo email loop. Streamlit is the whole UI.
- Worked vs claimed: all [claimed].
- Integration: SambaNova core, Streamlit core.
- Assets: 9 screenshots, good README, 100 commits (running to 11-27, after the event). Evidence A.

### Side tracks

**Echo** (Best Design) — https://devpost.com/software/hackutd-project-kbhins
- What: gamified emotion-mimicry trainer for neurodivergent children, with webcam expression matching, a quiz, and Blender/Three.js 3D mascots.
- Centerpiece: webcam facial-landmark and emotion detection plus rigged 3D mascots. Design is the visible part.
- Worked vs claimed: all [claimed]. The team says the webcam and quiz pages were completed and admits recognition is slow with multiple faces.
- Assets: no video or demo; template README. Evidence A.

**EcoLens (property evaluator)** (Best Beginner) — https://devpost.com/software/property-evaluator
- What: Swift app. Upload a room video, frames are extracted, Google Vision labels the furniture, and Llama assesses damage and suggests sustainable repairs.
- Centerpiece: a multi-stage vision → LLM pipeline.
- Worked vs claimed: all [claimed]. IoT is planned.
- Assets: video URL in project_records; no repo or demo. Evidence B.

**poyo.ed** (Poyo's Prize) — https://devpost.com/software/poyovision
- What: lecture companion built around a HackUTD-mascot Poyo plush with a hidden camera that captures slides while speech is transcribed and summarized.
- Centerpiece: the camera-in-plush hardware.
- Worked vs claimed: slide capture is [shown_working]; transcription and summaries are claimed.
- Sponsor tools: SambaNova and Pinata supporting.
- Assets: screenshots, detailed README; no video or live demo. Evidence A.
- Claim: "rated above 279 teams and 1,100 participants" (self-reported).

**Planet Score** (Best Devpost) — https://devpost.com/software/planet-score
- What: Chrome extension estimating a product's carbon footprint from keyword-inferred materials × OpenLCA/Exiobase spend factors.
- Centerpiece: none beyond the spend-based lookup (about 390 LOC). Solo build.
- Worked vs claimed: all [claimed].
- Assets: 6 screenshots, template README. Evidence A. The prize was for the writeup itself.

**DuckTalk** (Guided Track) — https://devpost.com/software/ducktalk
- What: solo beginner companion app (to-do list, map, weather, Firebase login) built from the hackathon's Hacker Project Guide.
- Centerpiece: none.
- Worked vs claimed: claimed. The GPT chat is planned.
- Assets: its project_records video URL is identical to Backtracc's (data error). Evidence B.

**What's The Move?** (Most Relatable) — https://devpost.com/software/what-s-the-move-4z5sih
- What: finds a fair meetup spot for a friend group using an inverse-weighted midpoint plus Google Places.
- Centerpiece: a custom Midpoint API.
- Worked vs claimed: the midpoint and nearby search are [shown_working].
- Sponsor tools: Pinata token.
- Assets: live Firebase demo, tests and CI, Figma; no video. Evidence A.

**Cheddarboxd** also won Best Solo Hack (see Pinata). **Backtracc** also won Hardware (see SambaNova).

### MLH only

**GitFile** ([MLH] Best Use of Terraform) — https://devpost.com/software/gitfile
- What: a C wrapper around Git that stores only the diffs of flat business files (PDF, DOCX), with a dashboard, PDF.js editing and an embedded SSH terminal.
- Centerpiece: the C git wrapper (systems work) on a Terraform-provisioned Azure VM.
- Worked vs claimed: all [claimed]. "500x storage cost reduction" has no stated method.
- Terraform integration: core. Pinata is core for history storage, but it did not win Pinata.
- Assets: gitfile.tech live, video URL in project_records. Evidence A.

*(Excluded: The Virtual Fitness Assistant. Its prizes appear to be from Student Hacks.)*

---

## 2. Patterns across HackUTD 2024 winners

N = 33 included winners. The 2024 data has no non-winner baseline, so every count is prevalence among winners, never a win rate. Names behind each count are in `data/tables/Q19_hackutd2024_counts.txt`.

**F1. Domain-sponsor winners almost all solved the sponsor's own business problem, usually without any sponsor technology.**
- FINDING: Of the projects that won a company-challenge track, nearly all addressed that sponsor's own industry problem. Most used no sponsor tool at all (problem-only); the rest built on a sponsor-supplied dataset.
- SUPPORT, domain match: 18 of 19 (95%) are in the sponsor's own business problem.
  - Goldman: AllBank, Lumo, TalkTuahBank
  - PNC: Data Pattern Observatory, FinnAI, Hermes
  - Toyota: FUELICIENT, KaizenDrive, ToyoTrends
  - EOG: PipeBrAIns, DHy-n0
  - CBRE/Veolia: Eco Fast Track, EcoVerse, Greenify, EcoLens SBM
  - Frontier: FrontierMap, Homelander, Promising Products
- SUPPORT, integration depth (unweighted, of 19):
  - problem-only: 11 of 19 (58%)
  - sponsor dataset at the core: 7 of 19 (37%). Explicit on the record: FUELICIENT, PipeBrAIns, Greenify, Homelander. By inference: KaizenDrive, ToyoTrends, DHy-n0.
  - unknown: 1 (InvestIQ)
- COUNTEREXAMPLES: InvestIQ (Infosys; fit not described).
- CONFIDENCE: medium. The counts are clear, but challenge text is not public, so "matches the prompt" cannot be verified.
- TYPE: fact (prevalence); "dataset-driven challenges" is inference.
- IMPLICATION FOR US: For a company-challenge track, pitch the sponsor's own operational problem in its own vocabulary. If they hand out a dataset, make it the core input. Do not count on bolting on a sponsor API.

**F2. Tool-sponsor prizes went only to projects where the tool was the backbone; side usage was common but did not win that prize.**
- FINDING: Pinata and SambaNova prizes went only to projects where the sponsor tool was the backbone, while many other winners used those tools in a minor way.
- SUPPORT:
  - 6 of 6 (100%) tool-sponsor winners have core integration: Monch, Capsule, Cheddarboxd (Pinata); Notable, Vestique, Backtracc (SambaNova).
  - Pinata appears in 15 of 33 (45%) winners. 3 of those 15 won Pinata, all of them with Pinata as the whole storage layer. In the other 12 Pinata was supporting, unclear or token, except FUELICIENT and GitFile, where it was core but they won other tracks.
  - SambaNova appears in 8 of 33 (24%); 3 won the SambaNova prize.
- COUNTEREXAMPLES: none found among the 6 tool-sponsor winners.
- CONFIDENCE: medium. The n is small and we cannot see who submitted to which track.
- TYPE: association (within winners).
- IMPLICATION FOR US: Only target an API or tool prize if that tool carries a core path in the demo. A sprinkled-in integration was common among 2024 winners and is not what the tool prizes rewarded.

**F3. An LLM was not needed to win. Every 2024 project with a known placement had no LLM, and most data-challenge winners used classical ML or none.**
- FINDING: An LLM was not required to win at HackUTD 2024; classical ML or no AI was common, especially on data-challenge tracks.
- SUPPORT, AI role across all 33:
  - core LLM or agent: 9 (27%)
  - LLM chatbot as an add-on: 5 (15%)
  - own or classical ML / stats / CV: 9 (27%)
  - none: 10 (30%)
- SUPPORT, subgroups:
  - Known-placement projects with no LLM: 4 of 4 (low n): FUELICIENT (Toyota 1st, no AI), Monch (Pinata 1st, self-trained classifier), Capsule (Pinata 2nd, no AI), Cheddarboxd (Pinata 3rd, no AI).
  - Toyota, EOG and Frontier winners with no LLM: 6 of 8 (75%): FUELICIENT, PipeBrAIns, DHy-n0, FrontierMap, Homelander, Promising Products.
- COUNTEREXAMPLES: TalkTuahBank (General plus Goldman) has a core LLM agent. All 3 SambaNova winners are LLM-core, by construction.
- CONFIDENCE: medium for prevalence, low for the placement subset (n = 4, and Pinata is a storage sponsor).
- TYPE: fact (prevalence); no causal claim.
- IMPLICATION FOR US: Do not treat "add an LLM" as the differentiator. On a dataset challenge, a trained model or domain algorithm on the sponsor's data is a proven winning shape. If an LLM is used, it should do the core job, not be a chat sidebar (5 winners had a sidebar, but it was never their centerpiece).

**F4. All three verified General winners were financial-inclusion fintech that reframed how banking reaches people, two stacked with Goldman, and none was a dashboard or hardware.**
- FINDING: The verified General winners share one theme (banking access for the unbanked through a non-obvious channel), and two of the three also won Goldman.
- SUPPORT:
  - 3 of 3 (low n) target the unbanked or underbanked: TalkTuahBank (bank by phone call), Lumo (charge everyone's card at purchase), Ripple Banking (merchants as micro-banks).
  - 2 of 3 also won Goldman Sachs: Lumo, TalkTuahBank.
  - 0 of 3 are data/analytics dashboards, versus 9 of 17 (53%) domain-sponsor-primary winners.
  - 0 of 3 have hardware.
  - Event-wide, 5 of 33 (15%) winners target the unbanked (adds AllBank and Hermes), and 3 of 3 Goldman winners do.
- COUNTEREXAMPLES: Roomie (unverified campus study-space finder, said to be General plus Hardware) would break the pattern if confirmed.
- CONFIDENCE: low-medium. n = 3; the PNC title sponsorship and the theme may explain the clustering (inference).
- TYPE: fact (counts); "reframing is what judges rewarded" is inference.
- IMPLICATION FOR US: A General-winning frame in 2024 was a clear human problem with a new delivery mechanism, not a better dashboard. Pairing it with the closest-domain sponsor track (Goldman, which took 2 of 3 General winners) stacked cleanly. Check whether 2026 has a theme or title-sponsor problem space that General judges may lean toward.

**F5. Prize stacking: 7 of 33 won 2+ prizes, mostly by pairing one sponsor track with General, MLH or a side prize.**
- FINDING: About a fifth of winners stacked prizes, almost always one sponsor track plus a General, MLH, Hardware or side prize.
- SUPPORT: 7 of 33 (21%) are multi-prize:
  - General + Goldman: Lumo, TalkTuahBank
  - sponsor + MLH: DHy-n0 (EOG + .Tech), Vestique (SambaNova + Streamlit)
  - sponsor + Hardware + MLH: Backtracc
  - sponsor + side: Cheddarboxd (Pinata + Solo)
  - two same-theme sponsors: Eco Fast Track (CBRE + Veolia)
- SUPPORT: no project won two unrelated sponsor tracks. MLH prizes did not count toward the 2-sponsor cap.
- COUNTEREXAMPLES: InvestIQ looks multi-prize, but its second badge is from another event.
- CONFIDENCE: medium.
- TYPE: fact.
- IMPLICATION FOR US: Use both sponsor slots on tracks that share one problem framing (as CBRE and Veolia did). Add MLH prizes only where the build already uses the tool (.Tech domain, Streamlit UI) because they are nearly free. Note that Backtracc's Cloudflare win was DNS only, so MLH bars were low in 2024 (one case).

**F6. Hardware was rare among 2024 winners, but the hardware projects collected more prizes.**
- FINDING: Only 4 winners had hardware, and they averaged more prizes than the other winners.
- SUPPORT:
  - hardware: 4 of 33 (12%) (low n): Backtracc (3 prizes), Eco Fast Track (2), EcoVerse (1, VR plus haptic gloves), poyo.ed (1, camera plush).
  - mean prizes: 1.75 for hardware vs 1.17 for the others.
  - Backtracc is the only project with every core feature [shown_working].
- COUNTEREXAMPLES: EcoVerse and poyo.ed won only one prize each.
- CONFIDENCE: low (n = 4).
- TYPE: association.
- IMPLICATION FOR US: A small, physically demonstrable piece (sensor or camera) is a stacking lever at HackUTD (Hardware prize plus a sponsor track) and is very visible at expo judging. Only do it if it works reliably; Eco Fast Track fell back to serial when WiFi failed.

**F7. Completeness bar: most 2024 winners showed little proof that their core feature worked; a video or live link was the norm, not working-proof.**
- FINDING: Most 2024 winners' pages only claimed their features worked, and a video or live link was the main presentation asset.
- SUPPORT:
  - core feature marked [shown_working]: 10 of 33 (30%): TalkTuahBank, Ripple Banking, ToyoTrends, Eco Fast Track, FrontierMap, Monch, Capsule, Backtracc, poyo.ed, What's The Move?
  - video or live demo: 25 of 33 (76%)
  - neither: 8 of 33 (24%): AllBank, Data Pattern Observatory, EcoVerse, EcoLens SBM, Echo, poyo.ed, Planet Score, DuckTalk
  - architecture diagram: 1 of 33 (TalkTuahBank)
  - README empty, template or boilerplate: 11 of 33, plus 4 "minimal" (deepdive readme_quality). This includes General winners Lumo and Ripple Banking.
- COUNTEREXAMPLES: n/a.
- CONFIDENCE: medium. Devpost text under-documents what was actually shown live at expo judging (spec rule 6: judging was in person).
- TYPE: fact (page evidence); "judges did not require proof" is inference.
- IMPLICATION FOR US: The Devpost page was not the deciding factor for most 2024 winners. Spend the effort on a live, repeatable expo demo. A short video plus a live link plus one architecture diagram would already put our page in the top tier of 2024 pages (only 1 of 33 had a diagram).

**F8. Data source: live feeds were a minority among winners; static sponsor datasets and user input were each as common.**
- FINDING: Live data was not required to win in 2024; static sponsor datasets and user-entered data were about as common.
- SUPPORT:
  - live API, sensor or stream: 11 of 33 (33%)
  - user input only: 10 of 33 (30%)
  - static (sponsor) dataset: 8 of 33 (24%): FUELICIENT, KaizenDrive, ToyoTrends, PipeBrAIns, DHy-n0, Greenify, Homelander, Promising Products
  - synthetic: 2 (EcoVerse, InvestIQ)
  - unclear: 2
- SUPPORT: General winners: 2 of 3 live (TalkTuahBank phone call, Lumo Stripe charges) and 1 user input (Ripple Banking).
- COUNTEREXAMPLES: n/a.
- CONFIDENCE: medium. The "live" boundary is my tag (see the script docstring).
- TYPE: fact (tag counts).
- IMPLICATION FOR US: Live data is not required. On a dataset challenge, use their data deeply. For a General pitch, a real interaction in the demo (a real call, a real charge) is what 2 of 3 General winners had.

**F9. Sponsor-track winners are dominated by dashboards and analytics tools; idea novelty mattered more on the General side.**
- FINDING: More than half of domain-sponsor-primary winners were data or analytics tools, which is the opposite of the General winners.
- SUPPORT: data_or_analytics in 9 of 17 (53%) domain-sponsor-primary winners: Data Pattern Observatory, FUELICIENT, KaizenDrive, ToyoTrends, PipeBrAIns, DHy-n0, Greenify, EcoLens SBM, Homelander. General winners: 0 of 3.
- SUPPORT: within Toyota (3 of 3) and EOG (2 of 2), every winner is a dashboard or predictor over the challenge data.
- COUNTEREXAMPLES: FrontierMap (AR plus geometry) and EcoVerse (VR) won domain tracks with non-dashboard ideas.
- CONFIDENCE: medium.
- TYPE: association (within winners); the novelty interpretation is inference.
- IMPLICATION FOR US: For a data-handout sponsor track, a well-executed analytics tool on their data is a proven winning shape (Toyota 1st was exactly that). For General 1st, it is not, so pick a build whose sponsor-track version is the analytics core and whose General pitch is the human problem.

---

## 3. Open questions / data issues

1. **InvestIQ "First Place [1st]"** in `deepdive_all.jsonl` and the profile is mis-attributed. `project_records` says the badge is from the "Lightning Fast AI Hackathon". Fix the deepdive prize label so that later stages (Q1/Q4) do not count it as a HackUTD 1st.
2. **The Virtual Fitness Assistant** is likely not a HackUTD 2024 winner: its badges are under Student Hacks, and similar prize names appear at HackTX 2024. It should be dropped from HackUTD 2024 winner counts or reassigned.
3. **Roomie**: evidence C, year unconfirmed, no Devpost page. Ask the team or organizers. If it is a real 2024 General plus Hardware winner, it breaks F4.
4. **The General track has only 3 verified winners**, with no 1st/2nd/3rd order. TalkTuahBank's "Overall 1st" is from its own README. Ask the team or check HackUTD social posts.
5. **Cheddarboxd Pinata placement** conflicts: the master list says 3rd per the Pinata blog; `project_records` says "not verified on Devpost". The blog URL is in the master list; re-check it.
6. **Video field conflict** between the two files: `project_records.has_demo_video` and `deepdive.presentation_assets.has_video` disagree (one true, the other false or null) for 14 of 35 rows: Backtracc, DuckTalk, Eco Fast Track, EcoLens PE, FinnAI, FUELICIENT, GitFile, InvestIQ, Lumo, Promising Products, Ripple Banking, TalkTuahBank, ToyoTrends, Vestique. Live-demo flags agree on all 35. For example, Backtracc, Lumo, Ripple Banking and Vestique have YouTube URLs but deepdive says no video. I counted video = URL present OR deepdive true.
7. **DuckTalk's `demo_video_url` is identical to Backtracc's** (youtube ffVqJkIsxhU), almost certainly a copy error. I counted DuckTalk as no video.
8. **Sponsor briefs vs dataset gaps:**
   - `pnc.md` and `toyota_financial_services.md` say "HackUTD 2024: unknown", but this dataset has 3 PNC and 3 Toyota winners (including Toyota 1st FUELICIENT). The briefs should be updated.
   - `cbre.md` names "EcoManage" (Dyne Labs) as a 2024 CBRE winner, but it is not in the master list or the dataset. The 2024 CBRE winner list may be incomplete.
9. **No 2024 sponsor challenge text is public** (it was in the kickoff hackerpack). All "fit" and "matches prompt" judgments for 2024 are inference.
10. **Repos changed after judging**: commits continue past 2024-11-17 for Backtracc, Vestique, EcoLens SBM, Echo, Promising Products, TalkTuahBank and InvestIQ (into 2025–2026). `commits_in_event_window` is mostly null. Repo state is not the judged state.
11. **Notable**'s repo is named "HackUTD25" and its demo is "hack-utd-25.vercel.app", but it won a 2024 sponsor prize (SambaNova was a 2024 sponsor). Most likely a naming quirk; low priority to verify.
12. **Evidence-B records** (Capsule, DuckTalk, EcoLens property evaluator, FinnAI, FUELICIENT, Homelander, ToyoTrends) could not be enriched because Devpost returned 403. FUELICIENT matters most: it is the only confirmed sponsor 1st in a company-challenge track, and it has no repo and no visible build detail.
13. Several tags are mine: "core_data*" (sponsor-dataset use by inference), ai_role buckets, and the "live" data boundary. They are hand tags and should be checked by the S3 tagger or the red team.
