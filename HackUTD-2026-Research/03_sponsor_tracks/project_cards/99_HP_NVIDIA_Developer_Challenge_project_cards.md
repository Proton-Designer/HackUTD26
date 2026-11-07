# HP & NVIDIA Developer Challenge: project cards (10 projects)

Facts and short paraphrases only; no cross-project analysis. Full records are in the workbook and JSONL.

## 2025

### AffectLink  (2025)

- **Prizes:** Winner First Place [1st]  (tier: overall_top3)
- **Pitch:** Local-first tele-health dashboard that fuses facial, vocal-tone and spoken-text emotion into an Emotional Consistency Index to flag when words and cues disagree.
- **Problem / user:** Clinicians lose non-verbal emotional cues in tele-health sessions, and sending patient audio/video to the cloud raises privacy concerns. / mental health clinicians doing tele-health
- **Domain / idea type:** mental_health + health_wellness / new_category
- **Platforms / hardware / AI:** web; desktop / False / vision; speech_or_voice; llm_chat; predictive_ml
- **Stack:** langs Python; frontend Streamlit; backend Python; db ; hosting local HP workstation
- **Tech/APIs:** HP AI Studio (other, core, sponsor); MLflow (other, supporting); Whisper (ai_model, core); DeepFace (ai_model, core); PyTorch (framework, supporting); Streamlit (framework, core)
- **Sponsor APIs:** HP AI Studio | fit: Placed first in the HP & NVIDIA challenge by deploying the Whisper, speech-emotion and text-emotion models locally through HP AI Studio's Swagger API with MLflow tracking; no NVIDIA-specific tool is named in the writeup.
- **Repo:** public, commits 178 (before/in/after event: 0/170/8), README detailed
- **Demo/writeup:** video True, live none, screenshots 16, writeup long, impact claims False
- **Notes:** Solo entry; Whisper, speech-emotion and text-emotion models deployed through HP AI Studio's local Swagger API, while DeepFace ran as a direct library call because AI Studio integration failed in time.
- **Team size:** 1 | **Confidence:** high | unverified: ui_polish
- **Links:** [Devpost](https://devpost.com/software/affectlink) | [GitHub](https://github.com/kingkw1/AffectLink)

### Codence  (2025)

- **Prizes:** Bonus Best in Enterprise Data Analysis [unknown]  (tier: sponsor_winner)
- **Pitch:** AI that extracts decisions from meeting notes, syncs Jira tickets after human approval, and checks GitLab pull requests against those decisions.
- **Problem / user:** Specs and meeting decisions drift from implementation; PMs manually reconcile Jira and developers unknowingly violate specs. / product managers and engineering teams
- **Domain / idea type:** productivity_workplace + dev_tools / automation_or_agent
- **Platforms / hardware / AI:** web / False / llm_chat; agent_or_tool_use
- **Stack:** langs Python; frontend ; backend FastAPI; Flask; db ; hosting Docker
- **Tech/APIs:** OpenAI GPT (ai_model, core); HP AI Studio (other, token, sponsor); GitLab webhooks (other, core); Jira REST API (other, core); FastAPI (framework, supporting); Docker (other, supporting)
- **Sponsor APIs:** HP AI Studio | fit: Won the bonus Enterprise Data Analysis prize as a meeting-note and Jira/GitLab alignment tool; HP AI Studio is tagged but the writeup describes GPT-based extraction rather than any HP or NVIDIA component.
- **Repo:** public, commits 32 (before/in/after event: 0/32/0), README detailed
- **Demo/writeup:** video True, live none, screenshots 16, writeup medium, impact claims False
- **Notes:** Combines GitLab webhooks, Jira REST sync and GPT-based rule extraction with a human approval step; HP AI Studio appears only as a Built With tag.
- **Team size:** 1 | **Confidence:** high | unverified: ui_polish; team_size; sponsor_fit_note depth
- **Links:** [Devpost](https://devpost.com/software/codence) | [GitHub](https://github.com/ChaoKuan-Lin/HP-hackathon)

### Document Analysis Toolset  (2025)

- **Prizes:** Winner Second Place [2nd]  (tier: overall_top3)
- **Pitch:** Streamlit document-forensics toolkit that detects signatures in PDFs with YOLO, classifies forgeries with a ViT, and flags edits through Error Level Analysis.
- **Problem / user:** Manual verification of document signatures and tampering is slow, subjective and misses subtle digital alterations. / legal, financial and forensic document reviewers
- **Domain / idea type:** safety_security + civic_legal / data_or_analytics
- **Platforms / hardware / AI:** web / False / vision; predictive_ml
- **Stack:** langs Python; frontend Streamlit; backend PyTorch; ONNX; db ; hosting Streamlit Community Cloud; Hugging Face
- **Tech/APIs:** HP AI Studio (other, core, sponsor); NVIDIA RTX GPU (training) (hardware_part, supporting, sponsor); MLflow (other, supporting); YOLO (ONNX) (ai_model, core); Vision Transformer (ai_model, core); Streamlit (framework, core)
- **Sponsor APIs:** HP AI Studio | fit: Placed second in the HP & NVIDIA challenge by training models in HP AI Studio on an NVIDIA GPU with MLflow tracking, then offering the YOLO and ViT models for inference through AI Studio as well as a hosted web app.
- **Repo:** public, commits 31 (before/in/after event: 0/31/0), README detailed
- **Demo/writeup:** video True, live not_checked, screenshots 13, writeup long, impact claims True (Claims over 95% signature-detection precision and over 90% forgery-classification accuracy; also says fraud costs organizations billions.)
- **Notes:** Solo entry; custom YOLO exported to ONNX, ViT forgery classifier hosted on Hugging Face for the web version, models trained on an RTX 4070 Ti Super via HP AI Studio.
- **Team size:** 1 | **Confidence:** high | unverified: ui_polish
- **Links:** [Devpost](https://devpost.com/software/document-analysis-toolset) | [GitHub](https://github.com/msamylea/hprepo)

### Medical Report Analyzer / Healthy Habits Recommender  (2025)

- **Prizes:** Bonus Honorable Mention: Healthcare [unknown]  (tier: sponsor_winner)
- **Pitch:** App that OCRs uploaded medical reports, summarizes them with an LLM and suggests personalized health habits and food changes based on a user's whole history.
- **Problem / user:** People forget which checkup values need improvement and lack ongoing, personalized follow-up advice from their reports. / patients tracking annual checkup results
- **Domain / idea type:** health_wellness + food_nutrition / twist_on_known_app
- **Platforms / hardware / AI:** web / False / llm_chat; vision; recommendation
- **Stack:** langs Python; HTML; frontend HTML; backend Python; db ; hosting HP AI Studio
- **Tech/APIs:** HP AI Studio (other, supporting, sponsor); MLflow (other, supporting); Tesseract OCR (ai_model, core); OpenAI GPT (ai_model, core); Llama 2 (local) (ai_model, supporting)
- **Sponsor APIs:** HP AI Studio | fit: Won a bonus Healthcare honorable mention; the project says it was deployed and tested on HP AI Studio with MLflow model packaging, with no NVIDIA-specific tool described.
- **Repo:** public, commits 8 (before/in/after event: 0/8/0), README detailed
- **Demo/writeup:** video True, live none, screenshots 10, writeup medium, impact claims False
- **Notes:** Detects duplicate uploads to avoid reprocessing; mixes OpenAI GPT with a local Llama2 option; model packaged via MLflow and tested on HP AI Studio.
- **Team size:** 2 | **Confidence:** high | unverified: ui_polish
- **Links:** [Devpost](https://devpost.com/software/medical-report-analyzer-healthy-habits-recommender) | [GitHub](https://github.com/nobelchowdary/hp-ai-hackathon-health-habit-recommender-app)

### Mira3D  (2025)

- **Prizes:** Winner Third Place [3rd]  (tier: overall_top3)
- **Pitch:** Local pipeline that turns short 2D videos into interactive 3D Gaussian-splat models, with background removal, COLMAP reconstruction and an in-browser editor.
- **Problem / user:** Most digital media is flat, and making 3D content normally needs cloud services or expensive tools. / creators and shoppers wanting 3D models from video
- **Domain / idea type:** creative_media / creative_tool
- **Platforms / hardware / AI:** web / False / vision; generative_media
- **Stack:** langs Python; frontend React; Three Fiber; backend Python; Swagger; db ; hosting HP AI Studio containers
- **Tech/APIs:** HP AI Studio (other, core, sponsor); NVIDIA CUDA (COLMAP) (framework, core, sponsor); MLflow (other, supporting); BiRefNet (ONNX) (ai_model, core); Brush Gaussian splatting (framework, core); React Three Fiber (framework, supporting)
- **Sponsor APIs:** HP AI Studio; NVIDIA CUDA | fit: Placed third in the HP & NVIDIA challenge by running the whole 3D reconstruction pipeline locally in HP AI Studio containers, using CUDA-accelerated COLMAP and MLflow/Swagger deployment.
- **Repo:** public, commits 6 (before/in/after event: 0/5/1), README detailed
- **Demo/writeup:** video True, live none, screenshots 13, writeup medium, impact claims False
- **Notes:** Solo entry running COLMAP with CUDA and a Vulkan-based Brush splatting engine inside HP AI Studio containers; author hit gsplat compatibility problems on Blackwell GPUs.
- **Team size:** 1 | **Confidence:** high | unverified: ui_polish
- **Links:** [Devpost](https://devpost.com/software/mirai-5d98z3) | [GitHub](https://github.com/ankithreddypati/mira3d)

### OpenMed  (2025)

- **Prizes:** Bonus Best in Enterprise Computer Vision [unknown]  (tier: sponsor_winner)
- **Pitch:** Medical imaging platform that classifies pneumonia, TB and brain tumors with ResNet50 models, shows Grad-CAM heatmaps, and answers questions through an OpenAI-powered chat interface.
- **Problem / user:** Clinicians distrust black-box diagnostic AI and many regions lack radiologists, so explainable image analysis is needed. / clinicians, rural hospitals and medical students
- **Domain / idea type:** health_wellness + ai_agents_infra / new_category
- **Platforms / hardware / AI:** web / False / vision; llm_chat; agent_or_tool_use
- **Stack:** langs Python; frontend OpenWebUI; backend FastAPI; PyTorch; db SQLite; PostgreSQL; hosting Docker; HP AI Studio
- **Tech/APIs:** HP AI Studio (other, core, sponsor); MLflow (other, supporting); PyTorch ResNet50 (ai_model, core); Grad-CAM (framework, core); OpenAI API (ai_model, supporting); OpenWebUI (framework, supporting); Kaggle medical imaging datasets (data_source, core)
- **Sponsor APIs:** HP AI Studio | fit: Won the bonus Enterprise Computer Vision prize by training its ResNet50 imaging models on HP AI Studio GPUs with MLflow tracking and deploying the front, middle and back-end services from AI Studio terminals.
- **Repo:** public, commits 24 (before/in/after event: 0/22/2), README detailed
- **Demo/writeup:** video True, live none, screenshots 22, writeup long, impact claims True (States test accuracies of 96.49%, 98.65% and 97.21%, under-3-second processing, and clinical acceptance and compliance claims.)
- **Notes:** Three separate ResNet50 models trained on Kaggle datasets, published on Hugging Face, fronted by OpenWebUI with a FastAPI OpenAI-compatible backend; reports 96-99% test accuracy and extensive clinical-readiness claims.
- **Team size:** 2 | **Confidence:** high | unverified: ui_polish
- **Links:** [Devpost](https://devpost.com/software/openmed-gtp792) | [GitHub](https://github.com/sriharshapy/openMed)

### Orpheus Engine  (2025)

- **Prizes:** Bonus Honorable Mention: Technology [unknown]  (tier: sponsor_winner)
- **Pitch:** Browser and Electron digital audio workstation with an AI agent that analyzes, transcribes and slices recordings, with plans for exporting audio to Web3.
- **Problem / user:** Audio professionals need restoration and analysis tools with AI research help across devices and inputs such as Bluetooth and MADI. / audio engineers and producers
- **Domain / idea type:** creative_media + ai_agents_infra / creative_tool
- **Platforms / hardware / AI:** web; desktop / False / speech_or_voice; rag_or_search; agent_or_tool_use
- **Stack:** langs TypeScript; Python; frontend TypeScript; Electron; backend GraphQL; Python; db ; hosting 
- **Tech/APIs:** HP AI Studio (other, supporting, sponsor); MLflow (other, supporting); Hugging Face model (ai_model, supporting); GraphQL (framework, supporting); Electron (framework, supporting)
- **Sponsor APIs:** HP AI Studio | fit: Won a bonus Technology honorable mention; the writeup says the Hugging Face model was later run in HP AI Studio and MLflow/Jupyter demos guided development, with several features only mocked up.
- **Repo:** public, commits 289 (before/in/after event: 0/285/4), README detailed
- **Demo/writeup:** video True, live none, screenshots 7, writeup medium, impact claims False
- **Notes:** Solo entry; author admits many features (plugin management, nRF device support) are mockups; much code was AI-assisted and had to be refactored from Electron-only to run in a browser.
- **Team size:** 1 | **Confidence:** high | unverified: ui_polish; prize name truncated in queue; page shows Bonus Honorable Mention: Technology
- **Links:** [Devpost](https://devpost.com/software/orpheus-engine) | [GitHub](https://github.com/jhead12/orpheus-engine)

### QuantumFinance AI  (2025)

- **Prizes:** Bonus Honorable Mention: Finance [unknown]  (tier: sponsor_winner)
- **Pitch:** LLM-powered stock research platform with market dashboard, sentiment, risk analysis, trading-strategy ideas and a finance Q&A assistant built on Perplexity models.
- **Problem / user:** Financial data tools are too complex or costly for ordinary investors who want clear, actionable market insight. / retail investors
- **Domain / idea type:** fintech_finance / data_or_analytics
- **Platforms / hardware / AI:** web / False / llm_chat; rag_or_search; predictive_ml
- **Stack:** langs Python; frontend ; backend FastAPI; db ; hosting Vercel; HP AI Studio
- **Tech/APIs:** HP AI Studio (other, core, sponsor); MLflow (other, supporting); Perplexity API (ai_model, core); Alpha Vantage API (data_source, supporting); FastAPI (framework, supporting); NVIDIA GPU libraries (via HP AI Studio) (hardware_part, token, sponsor)
- **Sponsor APIs:** HP AI Studio | fit: Won the bonus Finance honorable mention; it ran the FastAPI backend in HP AI Studio containers and used its MLflow to log prompt versions, citing NVIDIA GPU libraries only generally.
- **Repo:** public, commits 5 (before/in/after event: 0/5/0), README detailed
- **Demo/writeup:** video True, live not_checked, screenshots 10, writeup long, impact claims False
- **Notes:** Solo entry; all AI features call Perplexity APIs (including Deep Research) with Alpha Vantage history, while HP AI Studio hosted the FastAPI backend and MLflow prompt-version logging.
- **Team size:** 1 | **Confidence:** high | unverified: ui_polish
- **Links:** [Devpost](https://devpost.com/software/quantumfinance-ai) | [GitHub](https://github.com/Husky-AI9/QuantumFinanceAI)

### Sophia  (2025)

- **Prizes:** Bonus Best in Gen AI [unknown]  (tier: sponsor_winner)
- **Pitch:** Crypto intelligence platform with a LoRA-fine-tuned Phi-3-Mini chat model, news RAG, sentiment across 100+ coins, paper trading and auto-generated daily podcasts.
- **Problem / user:** Retail crypto investors cannot keep up with fast-moving news, sentiment and market data. / retail crypto traders
- **Domain / idea type:** fintech_finance + ai_agents_infra / data_or_analytics
- **Platforms / hardware / AI:** web / False / llm_chat; rag_or_search; agent_or_tool_use; speech_or_voice; predictive_ml
- **Stack:** langs Python; TypeScript; frontend React; Tailwind CSS; backend Node.js; Express; Flask; db SQLite; Milvus; hosting Docker; HP AI Studio
- **Tech/APIs:** HP AI Studio (other, core, sponsor); MLflow model serving (other, core); Phi-3-Mini (LoRA fine-tune) (ai_model, core); Milvus (database, core); CoinGecko API (data_source, supporting); LangChain agents (framework, supporting)
- **Sponsor APIs:** HP AI Studio | fit: Won the bonus Best in Gen AI prize by fine-tuning Phi-3-Mini with LoRA in HP AI Studio and serving it via AI Studio's MLflow model serving, wrapped for the web app.
- **Repo:** private_or_missing, commits None (before/in/after event: None/None/None), README None
- **Demo/writeup:** video True, live not_checked, screenshots 22, writeup long, impact claims False
- **Notes:** Fine-tuned Phi-3-Mini-128k with LoRA and 8-bit quantization inside HP AI Studio, served through a custom Flask OpenAI-compatible wrapper; Milvus RAG over 11,000+ scraped articles.
- **Team size:** 2 | **Confidence:** high | unverified: ui_polish; repo_clone_failed
- **Links:** [Devpost](https://devpost.com/software/sophia-76ueiq) | [GitHub](https://github.com/prasaddpathak/hp-hackathon)

### TRYON  (2025)

- **Prizes:** Bonus Honorable Mention: Retail [unknown]  (tier: sponsor_winner)
- **Pitch:** Offline virtual try-on app that segments the user's body and uses an inpainting diffusion model to overlay clothing without uploading photos.
- **Problem / user:** Online shoppers cannot see how clothes look on them and do not want to upload personal photos to the cloud. / online clothing shoppers
- **Domain / idea type:** retail_consumer / twist_on_known_app
- **Platforms / hardware / AI:** web; desktop / False / vision; generative_media
- **Stack:** langs Python; frontend ; backend Transformers; db ; hosting local
- **Tech/APIs:** HP AI Studio (other, supporting, sponsor); Body segmentation model (ai_model, core); Inpainting diffusion model (ai_model, core); Hugging Face Transformers (framework, supporting)
- **Sponsor APIs:** HP AI Studio | fit: Won the bonus Retail honorable mention by registering its local virtual try-on pipeline model in HP AI Studio for versioning and deployment; no NVIDIA-specific tool is named.
- **Repo:** public, commits 5 (before/in/after event: 0/4/1), README solid
- **Demo/writeup:** video True, live none, screenshots 7, writeup short, impact claims False
- **Notes:** Solo entry; all inference runs locally, with the pipeline model registered in HP AI Studio; author notes running every endpoint concurrently strained GPU memory.
- **Team size:** 1 | **Confidence:** high | unverified: ui_polish
- **Links:** [Devpost](https://devpost.com/software/tryon-woi0bh) | [GitHub](https://github.com/krishnaadithya/tryon)
