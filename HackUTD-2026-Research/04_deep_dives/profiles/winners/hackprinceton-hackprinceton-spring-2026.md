# HackPrinceton — HackPrinceton Spring 2026 (6 projects)

### Asclepius
*HackPrinceton HackPrinceton Spring 2026 · dataset: winners · tier: overall_top3 · evidence A · confidence high*
**Prizes:** Best Overall Hack; AI Research and Alignment Environments by d_model [$500 for 1st, $250 for 2nd, $125 for 3rd (Amazon gift cards)]; AI & Tech for Clinical Trials by Regeneron [Cash Prizes]

**What it is:** A local privacy layer between clinical-trial staff and cloud LLMs. It strips HIPAA identifiers and sensitive trial details on-device, routes each request to an abstract rewrite, a differentially-private proxy, or local-only answering, then re-applies the original entities to the cloud reply. A five-attack evaluation harness measures how much it actually leaks.
**Problem / user:** Medical writers, pharmacovigilance and regulatory staff at pharma/CROs who paste confidential documents into cloud LLMs; includes non-PHI leakage such as compound codenames and interim efficacy results.

**Features**
- Safe Harbor stripper — Regex plus local NER replace all 18 HIPAA identifiers and clinical quasi-identifiers (site, compound code, dose, AE grade) with tagged placeholders; mapping stays local. *[shown_working]*
- Neural router — Local LLM classifies each request as abstract-extractable, DP-tolerant or local-only (targets about 70/20/10 percent); deterministic override for high-sensitivity spans. *[shown_working]*
- Differential privacy path — Hidden-state embeddings clipped and Gaussian-noised with Renyi accounting, per-session budget and hard refusal when exhausted. *[shown_working]*
- Answer applier — Cloud response is returned locally and placeholders restored longest-key-first. *[shown_working]*
- Adversarial evaluation harness — Five attacks (span inversion, similarity, membership inference, etc.) measure text-surface leakage per route over a 1,200-document synthetic corpus. *[shown_working]*
- Forensic workspace UI — VS Code-style panes, Analyst and Reviewer personas, live epsilon dock and three-lane view of proxy, cloud reply, rehydrated answer. *[shown_working]*
- Audit logging — Model-call wrappers, canary-token leak detection and SHA-256-only logs. *[claimed]*

**Flow:** Load a clinical document in the workspace → Stripper replaces identifiers → Router picks a privacy path → Proxy sent to cloud (or answered locally) → Answer rehydrated locally → Forensic dock shows epsilon spent and proxy

**Prompt:** d_model: AI research lab focused on RLVR, interpretability and agents hosting an alignment and mechanistic interpretability track. Regeneron: best solutions for clinical trials in biotech. Best Overall: best project via initial and final judging.
**Fit (explicit):** Privacy tool for clinical-trial documents (Regeneron) plus adversarial measurement of its own failures reported as a research result (d_model); README lists all three wins.  *(targeted: Best Overall Hack, AI Research and Alignment Environments by d_model, AI & Tech for Clinical Trials by Regeneron)*
**AI:** Local LM for routing, query synthesis and paraphrase decoding; Claude via Anthropic SDK as the remote model; MiniLM similarity, DistilBERT span inversion, logistic-regression membership inference and LLM-as-judge for evaluation.
**Architecture:** Modular Python pipeline (stripper, router, synthesizer, DP mechanism, proxy decoder, remote client, answer applier) behind FastAPI with React/TypeScript frontend and audit wrappers.
**Novelty:** Ships both a privacy tool and a harness that reports its failures: v1 leaked 76.5 percent of spans verbatim; fixes cut that to 7.2 percent but utility fell sharply; DP epsilon sweep showed no effect.
**Scope:** large · working: 205 files, about 18.7k LOC, tests (74 per Devpost), CI, live demo site, video, paper folder. · polish: Architecture diagram, env example, docs, Overleaf writeup, detailed UI.
**Claims:** v1 verbatim leak 76.5 percent, v2 7.2 percent, utility 1.000 to 0.266 | DP epsilon sweep left outputs identical | 74 passing tests | 35 percent of protocol docs hit router parse errors
**Gaps:** video and live site not viewed; README read only through first ~7000 chars
Sources: https://devpost.com/software/asclepius-4rthsu, https://github.com/Shiv-aurora/hackprincetonS26, https://hackprinceton-spring-26.devpost.com/

---

### Atlas
*HackPrinceton HackPrinceton Spring 2026 · dataset: winners · tier: sponsor_winner · evidence A · confidence medium*
**Prizes:** Best AI-Powered App by Orchids (1st place: $300 cash, 2nd place: $200 cash); AI & Tech for Clinical Trials by Regeneron [Cash Prizes]

**What it is:** A web app where a user types a historical event or science concept, a 3D Gaussian-splat world is generated, and a voiced AI guide answers questions about what is in the scene. A STEM mode adds guided experiments.
**Problem / user:** Learners (history and science) for whom textbooks are passive; wants to show rather than tell.

**Features**
- Prompt-to-3D world — World Labs Marble API creates Gaussian splat scenes from text or user images, streamed as .spz in Spark/Three.js; generation takes minutes. *[shown_working]*
- Scene-grounded AI guide — Gemini answers questions using a scene graph of labeled objects to avoid hallucinated items. *[shown_working]*
- Voice replies — ElevenLabs speech synthesized in a separate audio pipeline so chat is not blocked. *[shown_working]*
- Click-to-focus objects — Clicking an object focuses it for follow-up questions and points-of-interest context. *[claimed]*
- STEM experiment mode — Guided experiments such as a photosynthesis cycle responding to user actions. *[claimed]*
- World library and info pages — Browse previously generated worlds; home, how it works and about pages. *[claimed]*
- VR and body motion — Planned interaction by body movement. *[planned]*

**Flow:** Type an event or concept → Wait for world generation → Step into the scene and navigate → Click objects, ask by text or voice → Try STEM experiments or browse library

**Prompt:** Orchids: best AI-powered app, judged on how effectively the project leverages Orchids app building. Regeneron: best solutions for clinical trials in biotech.
**Fit (none):** README frames an education product; no mention of Orchids usage or clinical trials found in the page or README.  *(targeted: Best AI-Powered App by Orchids, AI & Tech for Clinical Trials by Regeneron)*
**Sponsor tools:** World Labs Marble API (3D world generation from prompts, core); Orchids (not described in sources read, unclear)
**AI:** Marble generates splat worlds; Gemini interprets scenes and powers a guide constrained by a custom scene graph; ElevenLabs gives voice.
**Architecture:** Next.js/React frontend with Spark/Three.js splat viewer, Node/Express backend calling Marble, Gemini and ElevenLabs, scene graph data per world.
**Novelty:** Turns generated Gaussian-splat worlds into a queryable scene graph so a conversational guide stays grounded; world quality is acknowledged blurry.
**Scope:** medium · working: Repo about 833 files (mostly backend data) and 13.7k LOC with tests; demo video; README says demo scope is one polished prompt. · polish: Multiple pages, voice, library; no live demo link.
**Claims:** End-to-end prompt to world to voiced guide works | Guide gives historically accurate detail
**Gaps:** video not viewed; Orchids and Regeneron connections not found; README describes aspirational flow
Sources: https://devpost.com/software/atlas-kb2cnu, https://github.com/ch4nbin/atlas, https://hackprinceton-spring-26.devpost.com/

---

### Citadail
*HackPrinceton HackPrinceton Spring 2026 · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** Best AI-Powered App by Orchids (1st place: $300 cash, 2nd place: $200 cash)

**What it is:** Citadail is an AI equity-research and paper-trading workflow: pick a ticker and thesis, get a memo (.docx), model (.xlsx) and pitch deck (.pptx), then PM review, risk gate and paper positions; a Full Auto mode replays history without lookahead. Paper-only.
**Problem / user:** Investment analysts and PMs wanting a process-driven research-to-monitoring workflow, not a chatbot.

**Features**
- Assist Mode workbench — Analyst picks ticker and direction; system builds ThesisRecord and artifacts. *[claimed]*
- Office deliverables — docx, exceljs, pptxgenjs generate real files. *[claimed]*
- PM review and risk gate — Staged approval before paper trade desk and live book. *[claimed]*
- Full Auto replay — Walk-forward simulation filtering data by simulationTime. *[claimed]*
- iMessage PM updates — Photon Spectrum sends summaries to a group chat. *[claimed]*
- Dedalus/OpenClaw runtime — Bounded replay steps run remotely with execution proof, local fallback. *[claimed]*
- Audit journal — Logs decisions, equity curve, scorecard. *[claimed]*

**Flow:** Choose ticker or start date → Generate thesis and artifacts → PM and risk review → Open paper position → Monitor and journal

**Prompt:** Best AI-Powered App by Orchids: judged on how effectively the project uses Orchids app building ($300 1st, $200 2nd).
**Fit (implied):** README badge says Orchids winner; page does not explain Orchids use; also uses Dedalus and Photon.  *(targeted: Best AI-Powered App by Orchids)*
**Sponsor tools:** Dedalus (OpenClaw-compatible runtime for replay, supporting); Photon Spectrum (iMessage layer, supporting); Orchids (not described on page, unclear)
**AI:** Multi-agent LLM workflow (Gemini, Perplexity tags) around a shared ThesisRecord.
**Architecture:** Next.js/TypeScript app with agent modules, document generators, replay engine, Spectrum and Dedalus layers.
**Novelty:** End-to-end lifecycle with no-lookahead replay and real Office outputs.
**Scope:** large · working: ~32k LOC, Vitest tests, YouTube demo; no returns claimed. · polish: README with diagrams and safety section.
**Claims:** No predictive power claimed | Paper-only
**Gaps:** Tier (1st/2nd) unknown; Orchids use not described
Sources: https://devpost.com/software/citadail, evidence/hackprinceton-hackprinceton-spring-2026-citadail.json, prompts_cache/hackprinceton-spring-2026.md

---

### Confab
*HackPrinceton HackPrinceton Spring 2026 · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** AI Research and Alignment Environments by d_model [$500 for 1st, $250 for 2nd, $125 for 3rd (Amazon gift cards)]

**What it is:** An interpretability study and Streamlit demo of a hallucination signal called Update Direction Coherence, the average cosine similarity between consecutive layer-to-layer hidden-state updates per answer token, tested on Gemma with a length-controlled benchmark the team built.
**Problem / user:** Students and educational AI tools that need to flag confabulated LLM answers; also researchers questioning hallucination benchmarks.

**Features**
- UDC metric engine — Hooks a HuggingFace forward pass, computes layer update vectors and cosine similarity, takes the median over answer tokens. *[shown_working]*
- BENCH-2 benchmark — Length-controlled HaluEval QA subset where factual and hallucinated answers differ by at most 2 tokens. *[shown_working]*
- Benchmark audit — Shows raw HaluEval length alone reaches about 0.97 AUC, UDC AUC 0.743 on BENCH-2, 0.501 on TruthfulQA. *[shown_working]*
- Streamlit demo — Curated examples with token-level UDC heatmaps and hidden-state geometry views using precomputed Gemma artifacts. *[shown_working]*
- Gemini explanations — Optional natural-language explanation of UDC scores. *[claimed]*

**Flow:** Open demo tab with factual vs confabulated examples → Inspect token heatmaps and geometry → Read optional Gemini explanation → Switch to audit tab for benchmark results

**Prompt:** d_model: AI research lab focused on RLVR, interpretability and agents hosting an alignment and mechanistic interpretability track.
**Fit (explicit):** Hidden-state interpretability method for detecting confabulation with a benchmark audit; README and Devpost say it won this track.  *(targeted: AI Research and Alignment Environments by d_model)*
**AI:** Open Gemma 4 E2B on Colab L4 GPUs; hidden-state update-vector coherence as a training-free detector, calibrated thresholds; Gemini optional for explanations.
**Architecture:** Python engine extracts per-layer states, experiment scripts and tests produce results, and a Streamlit app with Plotly reads precomputed artifacts.
**Novelty:** Treats the benchmark itself as a finding by exposing a length shortcut, reports a negative TruthfulQA result and narrows the claim.
**Scope:** medium · working: 84 files, about 9.9k LOC, tests, results folder and Streamlit demo; no hosted demo. · polish: Detailed README with metrics and honest limits; demo uses precomputed artifacts.
**Claims:** UDC AUC 0.7429 on BENCH-2 vs length baseline 0.5632 | Raw HaluEval length alone about 0.97 AUC | TruthfulQA AUC 0.5008
**Gaps:** video not viewed; single model tested
Sources: https://devpost.com/software/confab, https://github.com/Aditya-Agarwal2006/hackprinceton, https://hackprinceton-spring-26.devpost.com/

---

### GreenChain
*HackPrinceton HackPrinceton Spring 2026 · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** Best Use of K2 Think V2 by Institute of Foundation Models at MBZUAI [reMarkable tablet for every member of the winning team]; Best use of Dedalus Containers by Dedalus [$250 for the top 4]; Best agent swarm hosted on Dedalus Containers by Dedalus [$500 for 1st place]

**What it is:** A sourcing comparison tool: a user enters a product, countries and transport mode; a Dedalus-hosted agent swarm finds real manufacturers, an ML model and datasets score five environmental dimensions, and results show on a graph, 3D globe and ranked list with plain-English scenario edits and a memo export.
**Problem / user:** Procurement managers at mid-market firms with no emissions visibility; ESG software is costly and compliance-oriented.

**Features**
- Agent swarm manufacturer discovery — Dedalus runner orchestrates Claude with Brave search and fetch tools per country; fetches run on a Dedalus Machine; retries broaden geography. *[shown_working]*
- Five-factor eco-score — Manufacturing emissions, transport carbon, grid intensity, certifications and climate risk combine into a 0-100 score with adjustable weights. *[shown_working]*
- XGBoost emissions estimates — Quantile regression (q10/q50/q90) trained on NAICS industries by country gives uncertainty bands. *[claimed]*
- Instant transport rescoring — Toggling sea, air, rail or road recomputes GLEC-style transport emissions in the browser. *[shown_working]*
- Graph and 3D globe views — Force-directed supply graph and Three.js globe with animated mode-styled routes and layout slider. *[shown_working]*
- Plain-English scenario edits — K2 Think V2 classifies intent and keeps or removes suppliers, with SQLite revision history. *[shown_working]*
- Memo export — Gemma via Gemini API writes a five-section cited sustainability memo. *[claimed]*

**Flow:** Land and import scenario CSV or open demo → Loading while swarm and scoring run → Dashboard with graph, globe, ranking → Adjust weights or transport mode → Edit scenario in plain English → Export memo

**Prompt:** K2 Think V2: use it as a core part of the product, not a side API call. Dedalus prizes: best use of Dedalus Containers and best agent swarm hosted on Dedalus Containers (no further text).
**Fit (explicit):** Routes untrusted fetches through a Dedalus Machine, runs a research swarm via Dedalus runner, and uses K2 for scenario intent and supplier keep/remove decisions; README and Devpost name these.  *(targeted: Best Use of K2 Think V2, Best use of Dedalus Containers, Best agent swarm hosted on Dedalus Containers)*
**Sponsor tools:** Dedalus Containers / DedalusRunner (agent swarm orchestration and isolated web fetching, core); K2 Think V2 (scenario intent classification and supplier keep/remove decisions, core); Gemini API (Gemma 4) (report synthesis, supporting); GoDaddy (project domain, token)
**AI:** Claude Sonnet via Dedalus for search agents, K2 Think V2 for two-pass intent and parallel keep/remove checks, Gemma for memo, XGBoost quantile regression for emissions.
**Architecture:** Next.js/Three.js/d3 frontend to FastAPI backend with SQLite cache; Dedalus Machine for fetches; datasets USEEIO, Ember, ND-GAIN, GLEC feed ScoreAssembler.
**Novelty:** Combines agent web research, ML uncertainty bands and client-side counterfactual rescoring, and isolates untrusted retrieval in a container.
**Scope:** large · working: 372 files, about 28k LOC, tests, docs, screenshots of landing, import, loading and dashboard, demo video. · polish: Detailed README with API reference and roadmap; custom domain; no CI.
**Claims:** Ranked comparison in under 60 seconds (README) | Trained on 1,016 industries by 179 countries | Supply chains cause over 60 percent of corporate emissions
**Gaps:** video not viewed; no model accuracy reported; hosted demo not listed
Sources: https://devpost.com/software/greenchain-1xglhu, https://github.com/thejustjim/hackprinceton2026, https://hackprinceton-spring-26.devpost.com/

---

### Object State Tracking in Language Models
*HackPrinceton HackPrinceton Spring 2026 · dataset: winners · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** AI Research and Alignment Environments by d_model [$500 for 1st, $250 for 2nd, $125 for 3rd (Amazon gift cards)]

**What it is:** A mechanistic-interpretability experiment asking whether instruction-tuned LLMs track an object's location as it moves through templated stories, and whether failures come from never encoding the answer or from failing to read it out. Linear probes on residual-stream activations are compared with model outputs.
**Problem / user:** ML researchers and builders of narrative-understanding systems who need to know whether state-tracking failures are storage or readout problems.

**Features**
- Controlled synthetic story dataset — Templated stories with 0-4 object transfers and distractor or red-herring conditions; truth is the last actual location. Devpost says 63 stories; repo later says 1,020. *[shown_working]*
- Behavioral accuracy evaluation — Measures output accuracy by transfer count; Gemma accuracy falls from about 81 percent at zero transfers to under 20 percent at 3-4. *[shown_working]*
- Linear probes on residual stream — Per-layer probes test whether the correct location is encoded; Gemma 2B probes reach 55.4 percent vs 41.3 percent output. *[shown_working]*
- Layer-wise and scale comparison — Compares 2B and 7B: 2B signal rises from layer 7, 7B jumps after layer 17; repo extends to nine models. *[shown_working]*

**Flow:** Generate templated stories → Run models and score outputs → Extract activations and train probes → Compare probe and output accuracy by layer, model and failure cases

**Prompt:** d_model: AI research lab focused on RLVR, interpretability and agents hosting an alignment and mechanistic interpretability track.
**Fit (implied):** Interpretability study of open models; Devpost states it won this track.  *(targeted: AI Research and Alignment Environments by d_model)*
**AI:** Gemma 2B-IT and 7B-IT (later nine models, 2B-14B) with linear probes on residual activations in PyTorch/Hugging Face, scikit-learn; Pythia dropped for prompt sensitivity.
**Architecture:** Python scripts generate stories, run model inference via SLURM jobs, save activations, train per-layer probes and plot results; no application layer.
**Novelty:** Pure research output: distinguishes storage from readout failure; repo abstract claims probes beat outputs on failures across all nine models (p<0.0001).
**Scope:** small · working: 71 files, about 1.2k LOC, results, probe summaries, plots and SLURM scripts; abstract in README. · polish: Paper-style README; no tests, demo or video.
**Claims:** Accuracy drops from about 81% to under 20% at 3-4 transfers | Probes 55.4% vs output 41.3% on Gemma 2B | Probes beat outputs on failures in all nine models (repo abstract)
**Gaps:** Devpost and repo differ in dataset size and model count (likely extended after submission); no demo
Sources: https://devpost.com/software/object-state-tracking-in-language-models, https://github.com/ddiyas/Object-State-Tracking-in-Language-Models, https://hackprinceton-spring-26.devpost.com/

---

