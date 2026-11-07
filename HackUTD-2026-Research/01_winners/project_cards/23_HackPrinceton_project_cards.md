# HackPrinceton: project cards (6 projects)

Facts and short paraphrases only; no cross-project analysis. Full records are in the workbook and JSONL.

## HackPrinceton Spring 2026

### Asclepius  (HackPrinceton Spring 2026)

- **Prizes:** Best Overall Hack [unknown]; AI Research and Alignment Environments by d_model [$500 for 1st, $250 for 2nd, $125 for 3rd (Amazon gift cards)] [unknown]; AI & Tech for Clinical Trials by Regeneron [Cash Prizes] [unknown]  (tier: overall_top3)
- **Pitch:** Local privacy layer for clinical-trial staff using cloud LLMs: strips HIPAA identifiers, routes requests to abstract rewrite, DP-noised or local-only paths, plus an adversarial test harness.
- **Problem / user:** Staff paste confidential trial documents into cloud LLMs, leaking patient data and material non-public information that regex tools miss. / clinical trial staff and pharma compliance teams
- **Domain / idea type:** health_wellness + safety_security / dev_tool
- **Platforms / hardware / AI:** web / False / llm_chat; agent_or_tool_use; predictive_ml
- **Stack:** langs Python; TypeScript; frontend React; Vite; D3.js; backend FastAPI; Pydantic; db Supabase; PostgreSQL; hosting 
- **Tech/APIs:** Gemma (local model) (ai_model, core); Anthropic Claude (cloud LLM) (ai_model, core); PyTorch / Hugging Face Transformers (framework, core); sentence-transformers (ai_model, supporting); DistilBERT (ai_model, supporting); Differential privacy (Renyi accounting) (other, core)
- **Sponsor APIs:**  | fit: Targets the Regeneron clinical-trials prompt and the d_model AI research prompt with a privacy proxy and an adversarial evaluation of its failures.
- **Repo:** public, commits 45 (before/in/after event: None/None/None), README detailed
- **Demo/writeup:** video True, live not_checked, screenshots 8, writeup long, impact claims True (Cites survey figures (58% of staff use unapproved AI) and reports measured leak-rate and utility numbers.)
- **Notes:** Reports a negative research result: differential-privacy noise on hidden states did not change decoded text across a 10x epsilon range; five-attack harness, 1,200 synthetic documents, 74 tests; links an Overleaf paper.
- **Team size:** 4 | **Confidence:** high | unverified: event_start; event_end; ui_polish; placement
- **Links:** [Devpost](https://devpost.com/software/asclepius-4rthsu) | [GitHub](https://github.com/Shiv-aurora/hackprincetonS26)

### Atlas  (HackPrinceton Spring 2026)

- **Prizes:** Best AI-Powered App by Orchids (1st place: $300 cash, 2nd place: $200 cash) [unknown]; AI & Tech for Clinical Trials by Regeneron [Cash Prizes] [unknown]  (tier: sponsor_winner)
- **Pitch:** Type a historical event or science concept and explore a generated 3D world with a voiced AI guide that answers questions about the scene.
- **Problem / user:** Textbook learning of history and science is passive; students are told rather than shown. / students and learners of history and STEM
- **Domain / idea type:** education + creative_media / new_category
- **Platforms / hardware / AI:** web / False / llm_chat; speech_or_voice; generative_media
- **Stack:** langs TypeScript; frontend Next.js; React; Three.js; Spark.js; Tailwind CSS; Framer; backend Node.js; Express.js; db ; hosting 
- **Tech/APIs:** World Labs Marble API (ai_model, core, sponsor); Google Gemini API (ai_model, core); ElevenLabs (ai_model, supporting); Three.js / Spark.js (framework, core); Next.js (framework, supporting)
- **Sponsor APIs:** World Labs Marble API | fit: Awards are sponsor tracks (Orchids AI app, Regeneron clinical-trials tech); writeup reads as an education product and the clinical-trials connection was not visible in what was read.
- **Repo:** public, commits 45 (before/in/after event: None/None/None), README detailed
- **Demo/writeup:** video None, live none, screenshots 6, writeup long, impact claims False
- **Notes:** Generates Gaussian-splat 3D worlds from text via World Labs Marble; a scene graph of labeled objects grounds the Gemini guide; includes interactive STEM experiments such as photosynthesis.
- **Team size:** 4 | **Confidence:** medium | unverified: event_start; event_end; has_demo_video; is_sponsor flags; writeup_sections beyond challenges; placement; ui_polish
- **Links:** [Devpost](https://devpost.com/software/atlas-kb2cnu) | [GitHub](https://github.com/ch4nbin/atlas)

### Citadail  (HackPrinceton Spring 2026)

- **Prizes:** Best AI-Powered App by Orchids (1st place: $300 cash, 2nd place: $200 cash) [unknown]  (tier: sponsor_winner)
- **Pitch:** AI-native investment desk of cooperating agents that builds research packages (memo, model, deck), reviews risk, runs a walk-forward paper-trading replay and sends iMessage updates.
- **Problem / user:** Investment teams need a system that forms, challenges and monitors theses, not another chatbot. / investment analysts and portfolio managers
- **Domain / idea type:** fintech_finance + ai_agents_infra / automation_or_agent
- **Platforms / hardware / AI:** web; bot_or_chat / False / agent_or_tool_use; llm_chat
- **Stack:** langs TypeScript; frontend Next.js; React; Framer Motion; backend ; db ; hosting Dedalus Machines
- **Tech/APIs:** Gemini (ai_model, core); Perplexity (data_source, supporting); Dedalus Machines (cloud, supporting, sponsor); Photon Spectrum (iMessage) (other, supporting, sponsor); docx / exceljs / pptxgenjs (framework, core); OpenClaw-compatible runtime (framework, supporting)
- **Sponsor APIs:** Dedalus; Photon Spectrum | fit: Orchids AI-powered app prize; page also uses Dedalus runtime and Photon Spectrum but ties no sponsor feature to Orchids.
- **Repo:** public, commits 19 (before/in/after event: None/None/None), README detailed
- **Demo/writeup:** video True, live not_checked, screenshots 4, writeup long, impact claims False
- **Notes:** Solo; shared ThesisRecord object across agents; generates real DOCX, XLSX and PPTX files; replay filters sources by simulated time; paper-only; iMessage via Photon Spectrum; Dedalus-hosted OpenClaw-compatible runtime with local fallback.
- **Team size:** 1 | **Confidence:** high | unverified: event_start; event_end; ui_polish
- **Links:** [Devpost](https://devpost.com/software/citadail) | [GitHub](https://github.com/Taz33m/citadail)

### Confab  (HackPrinceton Spring 2026)

- **Prizes:** AI Research and Alignment Environments by d_model [$500 for 1st, $250 for 2nd, $125 for 3rd (Amazon gift cards)] [unknown]  (tier: sponsor_winner)
- **Pitch:** Hallucination detector measuring how consistently an LLM's layer-to-layer hidden-state updates point in the same direction, evaluated on a length-controlled benchmark, with a Streamlit demo.
- **Problem / user:** Students cannot tell when LLMs confabulate, and common hallucination benchmarks can be gamed by answer length. / students and AI researchers
- **Domain / idea type:** ai_agents_infra + education / dev_tool
- **Platforms / hardware / AI:** web / False / llm_chat; predictive_ml
- **Stack:** langs Python; frontend Streamlit; Plotly; backend ; db ; hosting Google Colab
- **Tech/APIs:** Gemma 4 E2B (ai_model, core); Hugging Face Transformers (framework, core); Gemini API (ai_model, supporting); Streamlit (framework, core); PyTorch (framework, core)
- **Sponsor APIs:**  | fit: Hidden-state interpretability method for detecting model confabulation, matching the d_model research track theme.
- **Repo:** public, commits 6 (before/in/after event: None/None/None), README detailed
- **Demo/writeup:** video True, live not_checked, screenshots 0, writeup long, impact claims True (Reports AUC figures such as 0.7429 on BENCH-2 and 0.5008 on TruthfulQA.)
- **Notes:** Research-style project: Update Direction Coherence metric on Gemma 4 E2B, BENCH-2 length-controlled HaluEval subset, reports AUC 0.74 and near-chance 0.50 on TruthfulQA; Gemma artifacts precomputed on Colab; optional Gemini explanations.
- **Team size:** 2 | **Confidence:** high | unverified: event_start; event_end; ui_polish
- **Links:** [Devpost](https://devpost.com/software/confab) | [GitHub](https://github.com/Aditya-Agarwal2006/hackprinceton)

### GreenChain  (HackPrinceton Spring 2026)

- **Prizes:** Best Use of K2 Think V2 by Institute of Foundation Models at MBZUAI [reMarkable tablet for every member of the winning team] [unknown]; Best use of Dedalus Containers by Dedalus [$250 for the top 4] [unknown]; Best agent swarm hosted on Dedalus Containers by Dedalus [$500 for 1st place] [unknown]  (tier: sponsor_winner)
- **Pitch:** Supply-chain emissions comparator: an agent swarm finds real manufacturers, ML and datasets score five environmental factors, shown on a graph and 3D globe with plain-English scenario edits.
- **Problem / user:** Procurement managers lack fast, affordable tools to compare supplier and transport emissions despite Scope 3 reporting rules. / procurement managers
- **Domain / idea type:** sustainability_climate + ai_agents_infra / automation_or_agent
- **Platforms / hardware / AI:** web / False / agent_or_tool_use; llm_chat; predictive_ml; rag_or_search
- **Stack:** langs Python; TypeScript; frontend Next.js; React; Tailwind CSS; Three.js; D3.js; shadcn/ui; backend FastAPI; Pydantic; Uvicorn; db SQLite; hosting Dedalus Machines
- **Tech/APIs:** Dedalus Labs SDK / Machines (cloud, core, sponsor); Claude Sonnet 4.6 (ai_model, core); K2 Think V2 (ai_model, core, sponsor); Gemma 4 via Gemini API (ai_model, supporting, sponsor); Brave Search API (data_source, core); XGBoost (ai_model, core); EPA USEEIO / Ember / ND-GAIN data (data_source, core); GoDaddy domain (other, token, sponsor)
- **Sponsor APIs:** Dedalus Containers; K2 Think V2; Gemini API; GoDaddy | fit: Routes all untrusted page fetches through a Dedalus Machine, runs the research swarm on Dedalus, and uses K2 Think V2 for structured scenario edits.
- **Repo:** public, commits 96 (before/in/after event: None/None/None), README detailed
- **Demo/writeup:** video True, live not_checked, screenshots 4, writeup long, impact claims True (Cites supply chains causing over 60% of corporate emissions, ESG software over $50,000 a year, and a $20T manufacturing market.)
- **Notes:** Dedalus Machine isolates all web page fetches via the container API; Claude Sonnet 4.6 swarm with up to 14 steps; XGBoost quantile emissions model; K2 Think V2 two-pass scenario editor; sponsor-by-sponsor notes on the page.
- **Team size:** 3 | **Confidence:** high | unverified: event_start; event_end; ui_polish
- **Links:** [Devpost](https://devpost.com/software/greenchain-1xglhu) | [GitHub](https://github.com/thejustjim/hackprinceton2026)

### Object State Tracking in Language Models  (HackPrinceton Spring 2026)

- **Prizes:** AI Research and Alignment Environments by d_model [$500 for 1st, $250 for 2nd, $125 for 3rd (Amazon gift cards)] [unknown]  (tier: sponsor_winner)
- **Pitch:** Interpretability study testing whether Gemma 2B and 7B track object locations across story events, using linear probes to compare internal encoding with output accuracy.
- **Problem / user:** Unclear whether LLM failures in tracking entity state are storage failures or readout failures. / AI researchers
- **Domain / idea type:** ai_agents_infra + education / other
- **Platforms / hardware / AI:** other / False / llm_chat
- **Stack:** langs Python; frontend ; backend ; db ; hosting 
- **Tech/APIs:** Gemma 2B-IT / 7B-IT (ai_model, core); PyTorch (framework, core); Hugging Face (framework, core); scikit-learn linear probes (framework, core)
- **Sponsor APIs:**  | fit: Interpretability experiment on open models, aligned with the d_model AI research and alignment prompt.
- **Repo:** public, commits 19 (before/in/after event: None/None/None), README detailed
- **Demo/writeup:** video False, live not_checked, screenshots 3, writeup medium, impact claims False
- **Notes:** Research writeup rather than an app: 63 templated stories, accuracy collapse at 3+ transfers, probes beat output accuracy on Gemma 2B (55.4% vs 41.3% stated); no demo video.
- **Team size:** 1 | **Confidence:** high | unverified: event_start; event_end; ui_polish
- **Links:** [Devpost](https://devpost.com/software/object-state-tracking-in-language-models) | [GitHub](https://github.com/ddiyas/Object-State-Tracking-in-Language-Models)
