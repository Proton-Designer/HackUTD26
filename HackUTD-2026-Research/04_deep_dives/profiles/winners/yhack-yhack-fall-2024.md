# YHack — YHack Fall 2024 (3 projects)

### bellcrve
*YHack YHack Fall 2024 · dataset: winners · tier: overall_top3 · evidence B · confidence medium*
**Prizes:** 2nd Place [2nd]

**What it is:** Distributed Monte Carlo option-pricing platform on 10 DigitalOcean VMs (8 workers, master, scheduler) managed with Dask. Simulations use geometric Brownian motion and Black-Scholes, written with Wolfram/Python, with a Next.js/D3 app showing convergence in real time.
**Problem / user:** People pricing options who want faster Monte Carlo simulation; no user stated beyond finance and engineering interest.

**Features**
- Distributed simulation cluster — Scheduler hands simulations to workers as they free up; up to 10,000 simulations on 10 machines *[claimed]*
- GBM price paths and Black-Scholes pricing — Wolfram and Python compute paths and theoretical value *[claimed]*
- Convergence view — Compares GBM and Black-Scholes as steps and iterations increase *[shown_working]*
- Web app for choosing stocks and pricing options in real time — Next.js client with websocket backend and D3 charts *[claimed]*
- PyPI package of the math — Published for reuse *[claimed]*

**Flow:** Open the web app → Pick a stock and simulation count → Cluster runs simulations → Watch charts converge toward Black-Scholes

**Prompt:** not public / not found
**Fit (none):** Page lists no track; project was entered under Lambda Labs-named Devpost slug but no prompt text is stated.  *(targeted: 2nd Place (overall))*
**Sponsor tools:** Wolfram (Monte Carlo math and fast convergence, supporting)
**AI:** none
**Architecture:** Flask/Python websocket API and Dask scheduler over DigitalOcean VMs run Wolfram-backed simulations; Next.js/React/D3 frontend deployed on Vercel.
**Novelty:** Builds a real multi-VM compute cluster for a 24-hour hack rather than a single-server simulation.
**Scope:** medium · working: Deployed site bellcrve.com and embedded video per page; no benchmarks. · polish: Challenges (WSS, CORS) documented; no repo read; no metrics.
**Claims:** Up to 10,000 simulations on 10 machines | Low error through GBM and Black-Scholes convergence
**Gaps:** No repo in record; org page not read; No benchmark numbers
Sources: https://devpost.com/software/lambda-labs, https://yhack.devpost.com/

---

### Percival
*YHack YHack Fall 2024 · dataset: winners · tier: overall_top3 · evidence A · confidence medium*
**Prizes:** 1st Place [1st]; Best AI Project with Databricks Open Source

**What it is:** Clinical data-entry assistant for doctors: enter patient information by text, speech (Whisper) or PDF, auto-anonymize, fill medical forms with OpenAI, and cluster the case against anonymized similar patients to suggest diagnoses and treatments. Focus is on AIDS cases.
**Problem / user:** Doctors burdened by data entry and diagnosis support, with a need to protect patient privacy.

**Features**
- Multimodal intake by text, audio or PDF — Whisper transcribes speech; OpenAI structures content into medical forms *[claimed]*
- Automatic anonymization — Patient identifiers removed before storage in the shared case store *[claimed]*
- Similar-case matching — K-means on Databricks open source over a vector database groups symptoms and history *[claimed]*
- Diagnosis and treatment recommendations — Drawn from similar patient clusters *[claimed]*
- Doctor login, dashboard and patient pages — Next.js UI with PDF viewer and add-patient page; Cloudflare D1 for data *[claimed]*

**Flow:** Doctor logs in → Adds patient via text, audio or PDF → Data transcribed, structured and anonymized → Reviews dashboard and patient forms → Sees treatment suggestions from similar cases

**Prompt:** Databricks Best AI Project with Open Source: build an AI project using Databricks open-source projects. YHack Fall 2024 (Yale's 11th): 1st-3rd overall listed without prize description; tracks incl. Health; Databricks prize asks for an AI project using Databricks open-source tools; ActualFood award for sustainability challenges. Judging: originality 25%, impact 25%, complexity 20%, UX 20%, pitch 10%.
**Fit (explicit):** Uses K-means clustering on Databricks open source inside a vector database for case matching; Devpost lists the Databricks award as won.  *(targeted: 1st Place, Best AI Project with Databricks Open Source)*
**Sponsor tools:** Databricks Open Source (K-means clustering of patient cases, supporting)
**AI:** Whisper speech-to-text and OpenAI API for form population; embeddings in a vector database with K-means clustering for case similarity.
**Architecture:** Next.js frontend and Flask API; Cloudflare D1 for auth and data; vector database holds anonymized cases clustered for recommendations.
**Novelty:** Combines anonymization, form filling and cohort retrieval in one clinician workflow rather than a chatbot.
**Scope:** medium · working: Screenshots only on Devpost; repo ~4k lines with tests, but README is create-next-app boilerplate. · polish: Several UI pages; no demo video; no evaluation metrics.
**Claims:** Improved diagnostic accuracy and efficiency (no data)
**Gaps:** README uninformative; Case database source unknown
Sources: https://devpost.com/software/percival-nr46ol, https://github.com/roshanbellary/Percival (evidence file; README is boilerplate), https://yhack.devpost.com/

---

### The Tales of Detective Toasty
*YHack YHack Fall 2024 · dataset: winners · tier: overall_top3 · evidence B · confidence medium*
**Prizes:** 3rd Place [3rd]

**What it is:** Ren'Py visual-novel murder mystery set on a trapped boat. Player is Detective Toasty investigating four suspects, with a GPT-powered assistant answering questions, DALL-E art refined by hand, and point-and-click room exploration.
**Problem / user:** Players of narrative and mystery games; no problem statement given.

**Features**
- Playable mystery with four suspects — Talk to characters, switch rooms, find the body, progress through CG scenes *[shown_working]*
- AI assistant answering player questions — ChatGPT API prompted with the game world; replies vary by playthrough *[claimed]*
- Home screen and save/load — Ren'Py menus *[shown_working]*
- Generated art and sprites — DALL-E images edited in Procreate; transparent backgrounds *[shown_working]*
- Inventory with AI-generated evidence, more chapters — Stated future work *[planned]*

**Flow:** Start or load a game → Watch the intro CG → Talk to suspects and explore rooms → Ask the AI assistant questions → Discover the body and keep investigating

**Prompt:** not public / not found
**Fit (none):** No stated prize target; page describes homage to Persona and Ghost Trick.  *(targeted: 3rd Place (overall))*
**AI:** OpenAI GPT API prompt-tuned as an in-game assistant for dialogue consistency and plot advancement; DALL-E for art.
**Architecture:** Ren'Py/Python game scripts call the OpenAI API; art assets generated and edited offline; distributed through itch.io.
**Novelty:** First-hackathon team shipped a complete narrative game with generated art and an LLM question-answering layer.
**Scope:** small · working: Playable itch.io build and screenshots per page; no repo. · polish: Custom art and UI via Canva; no video; no source link.
**Claims:** First hackathon for the team
**Gaps:** No repository; Whether GPT is live in the shipped build is unclear since GPT dialogue is also listed as planned
Sources: https://devpost.com/software/placeholder-5hgbfe, https://yhack.devpost.com/

---

