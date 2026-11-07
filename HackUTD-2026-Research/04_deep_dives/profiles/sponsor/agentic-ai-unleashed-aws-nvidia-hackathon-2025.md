# Agentic AI Unleashed: AWS & NVIDIA Hackathon — 2025 (3 projects)

### Agent Builder
*Agentic AI Unleashed: AWS & NVIDIA Hackathon 2025 · dataset: sponsor · tier: overall_top3 · evidence B · confidence medium*
**Prizes:** Third Place [3rd]

**What it is:** A web tool where the user describes a workflow in chat and an LLM assembles agents and tools from a catalog into a visual ReactFlow graph, which can be edited, tested with live input and deployed to AWS ECS or Lambda.
**Problem / user:** Data scientists and developers (and nominally non-coders) who find wiring agents, tools and integrations too boilerplate-heavy.

**Features**
- Chat-to-workflow generation — Nemotron produces schema-constrained JSON of nodes and edges from a plain-language request, then post-validation repairs errors. *[shown_working]*
- Semantic catalog search — Embeddings (nv-embedqa-e5-v5) retrieve relevant agents and tools; only top items go into the prompt. *[claimed]*
- Visual drag-and-drop canvas — ReactFlow editor for refining AI output, with tool-attachment handles. *[shown_working]*
- Live test run — Enter input and watch step-by-step execution. *[claimed]*
- One-click deploy — Containerized microservices pushed to ECS or Lambda with WebSocket progress. *[claimed]*
- Demo and backend modes — Dummy mode for demos, backend mode for production; regex fallbacks if LLM unavailable. *[claimed]*
- Multi-turn refinement, marketplace, templates — Future work. *[planned]*

**Flow:** Describe the desired workflow in chat → AI generates agents/tools graph (example: sentiment, data analysis, summarizer with database and PDF tools) → Edit nodes on canvas → Test with live input → Deploy to AWS

**Prompt:** Build an agentic application powered by the llama-3.1-nemotron-nano-8B reasoning model as an NVIDIA NIM plus at least one retrieval-embedding NIM, hosted on Amazon EKS or SageMaker endpoints; a full-stack real-world app.
**Fit (implied):** Uses the exact Nemotron-nano-8B and nv-embedqa NIM pair for reasoning and retrieval in an agent-authoring app, with AWS deployment services; writeup does not state where the NIMs were hosted.  *(targeted: Third Place)*
**Sponsor tools:** llama-3.1-nemotron-nano-8B NIM (reasoning and JSON workflow generation, core); nv-embedqa-e5-v5 embedding NIM (catalog retrieval, core)
**AI:** Nemotron generates constrained JSON workflows via LangChain with retrieved catalog items and sliding-window history; embeddings retrieve agents; output is validated and repaired.
**Architecture:** React/ReactFlow/Zustand front end; Node/Express orchestration with Postgres and Redis; Python FastAPI LLM service with a vector DB; deployment service using Docker and AWS SDK to ECS/Lambda.
**Novelty:** Meta-tool that builds agents rather than being one agent; handles tool-vs-flow edges and validation of hallucinated node ids.
**Scope:** medium · working: Vimeo demo video and four screenshots; no repo or live link on page. · polish: Detailed architecture and challenge writeup; performance claims unverified.
**Claims:** Natural language to deployment in under 30 seconds | Sub-millisecond catalog retrieval | Streaming feels 3x faster
**Gaps:** no repo; video not watchable
Sources: https://devpost.com/software/agent-builder, https://nvidia-aws.devpost.com/ (via sponsor_prompts_NVIDIA.jsonl)

---

### Nomi
*Agentic AI Unleashed: AWS & NVIDIA Hackathon 2025 · dataset: sponsor · tier: overall_top3 · evidence B · confidence medium*
**Prizes:** Grand Prize [1st]

**What it is:** An eldercare monitoring system: ESP32 sensors (pulse, pressure films, temperature-humidity) and an on-device camera posture check feed AWS, and a Nemotron NIM summarizes patterns into plain-language insights on a React dashboard with caregiver email alerts.
**Problem / user:** Seniors aging in place and their caregivers who lack continuous visibility into missed medication, meals, falls and vitals.

**Features**
- Medication and meal detection — Pressure film under pillbox or tray infers taken or skipped events tracked in DynamoDB. *[claimed]*
- Fall and posture detection — OpenCV and MediaPipe run locally and email caregivers on fallen or inactive posture; first alert email reportedly arrived. *[claimed]*
- Vitals and room sensing — Pulse sensor plus temperature-humidity readings sent via ESP32 to API Gateway and Lambda. *[claimed]*
- AI health insights — NVIDIA NIM Nemotron summarizes data, flags risks, recommends actions. *[claimed]*
- Caregiver alerts — SNS or Gmail SMTP messages with time, vitals and advice. *[claimed]*
- Dashboard with sample-data mode — React/Recharts cards; public demo runs on sample data. *[shown_working]*
- MQTT streaming, IoT Core, SpO2 modules — Next steps. *[planned]*

**Flow:** ESP32 posts sensor readings → Lambda normalizes into DynamoDB → FastAPI fetches and asks NIM for summary → Dashboard shows vitals and insights → Alert emailed on fall or abnormal vitals

**Prompt:** Build an agentic application powered by the llama-3.1-nemotron-nano-8B reasoning model as an NVIDIA NIM plus at least one retrieval-embedding NIM, hosted on Amazon EKS or SageMaker endpoints; a full-stack real-world app.
**Fit (implied):** Uses a Nemotron-Nano-8B NIM for health reasoning in a full-stack IoT app on AWS; SageMaker hosting was blocked by IAM so a local NIM proxy stood in for the demo.  *(targeted: Grand Prize)*
**Sponsor tools:** NVIDIA NIM (Llama-3.1 Nemotron Nano 8B) (summarizing sensor data into insights, core); AWS SageMaker (intended NIM hosting; replaced by local proxy, unclear)
**AI:** Nemotron NIM summarizes DynamoDB records into risk flags and recommendations; MediaPipe/OpenCV does posture classification on device.
**Architecture:** ESP32 sensors to API Gateway, Lambda and DynamoDB; FastAPI backend with Pydantic calls NIM; React/Tailwind dashboard; SNS/SMTP alerts; camera processed locally.
**Novelty:** Physical hardware build (sensors, 3D-printed camera stand) with privacy-preserving local video, unusual among AI-agent entries.
**Scope:** medium · working: GitHub Pages demo on sample data, YouTube video and repo; hardware photos described; no detection metrics. · polish: Detailed Devpost writeup with statistics and challenges; 20 likes.
**Claims:** First fall-alert email delivered successfully | Only anonymized event labels leave the device
**Gaps:** repo clone failed so README unread; video not watchable
Sources: https://devpost.com/software/nomi-aoim58, https://nvidia-aws.devpost.com/ (via sponsor_prompts_NVIDIA.jsonl)

---

### Skyrchitect
*Agentic AI Unleashed: AWS & NVIDIA Hackathon 2025 · dataset: sponsor · tier: overall_top3 · evidence B · confidence medium*
**Prizes:** Second Place [2nd]

**What it is:** An agent that turns natural-language requirements (or an uploaded diagram) into an AWS architecture: retrieves patterns from a curated knowledge base, calls tools for service info and cost, validates, and renders an interactive diagram plus Terraform/CloudFormation.
**Problem / user:** Developers, startups and enterprises who struggle to pick cloud services, estimate cost, secure and codify infrastructure.

**Features**
- Architecture generation from requirements — Nemotron-Nano-8B on SageMaker plans nodes and connections as structured JSON. *[claimed]*
- RAG over architecture patterns — Embedding NIM retrieves top 3 patterns (HA, serverless, microservices, cost) to enrich the prompt. *[claimed]*
- Five agent tools — Service info, cost calculation, optimization, alternatives and validation. *[claimed]*
- Interactive React Flow diagram — Rendered from model JSON with themed provider cards. *[shown_working]*
- IaC generation — Terraform and CloudFormation viewer with syntax highlighting. *[claimed]*
- Diagram upload analysis — Listed as feature but also future work. *[unclear]*
- Dual backend — MODEL_TYPE switch between NIMs on SageMaker and Claude on Bedrock. *[claimed]*

**Flow:** Describe requirements or upload diagram → Embedding NIM retrieves patterns → Agent calls tools for cost and validation → View interactive diagram → Inspect generated IaC

**Prompt:** Build an agentic application powered by the llama-3.1-nemotron-nano-8B reasoning model as an NVIDIA NIM plus at least one retrieval-embedding NIM, hosted on Amazon EKS or SageMaker endpoints; a full-stack real-world app.
**Fit (explicit):** Deploys both required NIMs on SageMaker ml.g5.xlarge endpoints via boto3, uses Strands agent adapter and RAG; matches prompt closely.  *(targeted: Second Place)*
**Sponsor tools:** Llama 3.1 Nemotron Nano 8B NIM (reasoning, architecture and code generation, core); NVIDIA Retrieval Embedding NIM (RAG pattern retrieval, core)
**AI:** Strands agent with custom SageMakerNIMModel adapter calling Nemotron with tool use; RAG via embedding NIM and cosine similarity; hash-embedding fallback for dev.
**Architecture:** React/TypeScript/React Flow front end; FastAPI backend with agent files per model backend; SageMaker endpoints for LLM and embeddings; S3 backup; deploy script.
**Novelty:** Adapted the Strands agents framework to SageMaker-hosted NIMs and kept one codebase for two hackathons with a model switch.
**Scope:** medium · working: Vimeo demo video, deploy and integration test scripts named; no live demo. · polish: Detailed writeup; some inconsistencies (vision both current and future).
**Claims:** Semantic similarity 0.900, also reached by fallback embeddings | Two endpoints about $2.82 per hour | First Strands agent on SageMaker NIMs
**Gaps:** repo clone failed so README unread; video not watchable
Sources: https://devpost.com/software/skyrchitect-6d37yf, https://nvidia-aws.devpost.com/ (via sponsor_prompts_NVIDIA.jsonl)

---

