# Agentic AI Unleashed: AWS & NVIDIA Hackathon: project cards (3 projects)

Facts and short paraphrases only; no cross-project analysis. Full records are in the workbook and JSONL.

## 2025 (NVIDIA-run Devpost event)

### Agent Builder  (2025 (NVIDIA-run Devpost event))

- **Prizes:** Third Place [3rd]  (tier: overall_top3)
- **Pitch:** Chat-driven platform that turns plain-English requests into agent workflows on a visual canvas using NVIDIA NIM reasoning and embedding models, deployable as containers to AWS.
- **Problem / user:** Building agent workflows requires boilerplate and manual wiring of agents, tools and integrations. / developers and data scientists building agent workflows
- **Domain / idea type:** ai_agents_infra + dev_tools / dev_tool
- **Platforms / hardware / AI:** web / False / llm_chat; agent_or_tool_use; rag_or_search
- **Stack:** langs TypeScript; Python; JavaScript; frontend React; Vite; ReactFlow; Zustand; backend Node.js; Express; FastAPI; LangChain; db PostgreSQL; Redis; Pinecone/Weaviate; hosting AWS ECS; AWS Lambda; S3; Docker
- **Tech/APIs:** NVIDIA NIM llama-3.1-nemotron-nano-8B-v1 (ai_model, core, sponsor); NVIDIA nv-embedqa-e5-v5 embeddings (ai_model, core, sponsor); AWS ECS/Lambda/S3 (cloud, supporting, sponsor); LangChain (framework, supporting); ReactFlow (framework, supporting); Vector DB (Pinecone/Weaviate) (database, supporting)
- **Sponsor APIs:** NVIDIA NIM llama-3.1-nemotron-nano-8B-v1; NVIDIA nv-embedqa-e5-v5; AWS | fit: Used the Nemotron Nano NIM for schema-constrained workflow JSON generation and the nv-embedqa-e5-v5 embedding NIM for retrieval over the agent/tool catalog, targeting the NVIDIA and AWS agentic AI hackathon.
- **Repo:** none_listed, commits None (before/in/after event: None/None/None), README None
- **Demo/writeup:** video True, live none, screenshots 4, writeup long, impact claims True (Claims a workflow can be generated and deployed in under 30 seconds and 3x faster perceived speed from streaming; not substantiated.)
- **Notes:** Schema-constrained JSON generation from llama-3.1-nemotron-nano-8B with retrieval via nv-embedqa-e5-v5 over an agent/tool catalog; dummy mode for demos; no GitHub or live link listed; description appears partly aspirational about deployment.
- **Team size:** 1 | **Confidence:** high | unverified: ui_polish; n_screenshots; placement_tier
- **Links:** [Devpost](https://devpost.com/software/agent-builder)

### Nomi  (2025 (NVIDIA-run Devpost event))

- **Prizes:** Grand Prize [1st]  (tier: overall_top3)
- **Pitch:** ESP32 sensor network (pulse, pressure, temperature) plus local pose detection feeding DynamoDB and an NVIDIA NIM Nemotron model that summarizes elderly residents' health and emails caregiver alerts.
- **Problem / user:** Seniors living alone risk unnoticed falls, missed medication and meals, and silent health decline while caregivers cannot monitor 24/7. / elderly people living alone and their caregivers
- **Domain / idea type:** health_wellness + safety_security / hardware_gadget
- **Platforms / hardware / AI:** web; hardware / True / llm_chat; vision; agent_or_tool_use
- **Stack:** langs Python; JavaScript; C++ (Arduino); frontend React; Tailwind CSS; Recharts; backend FastAPI; AWS Lambda; API Gateway; Pydantic; db DynamoDB; hosting AWS; GitHub Pages
- **Tech/APIs:** NVIDIA NIM Llama-3.1-Nemotron-Nano-8B (ai_model, core, sponsor); AWS SageMaker (planned NIM endpoint) (cloud, supporting, sponsor); AWS Lambda / API Gateway / DynamoDB / SNS (cloud, core, sponsor); ESP32 + pulse, pressure film, temp-humidity sensors (hardware_part, core); OpenCV + MediaPipe (ai_model, core); FastAPI (framework, supporting)
- **Sponsor APIs:** NVIDIA NIM Llama-3.1-Nemotron-Nano-8B; AWS SageMaker; AWS Lambda; AWS DynamoDB; AWS SNS | fit: Used the Llama-3.1-Nemotron-Nano-8B NIM to turn DynamoDB sensor records into plain-language health insights and risk summaries; SageMaker deployment was initialized but the submission fell back to a local NIM API proxy.
- **Repo:** public, commits 31 (before/in/after event: 0/31/0), README detailed
- **Demo/writeup:** video True, live not_checked, screenshots 3, writeup long, impact claims True (Cites UN, WHO and CDC statistics on aging population, caregiver shortage and fall costs.)
- **Notes:** Intended SageMaker NIM deployment was replaced by a local API proxy after IAM permission changes; front-end uses sample data because live collection needed 24 hours; fall detection runs locally with OpenCV and MediaPipe; 3D-printed camera stand.
- **Team size:** 2 | **Confidence:** high | unverified: ui_polish; n_screenshots; placement_tier
- **Links:** [Devpost](https://devpost.com/software/nomi-aoim58) | [GitHub](https://github.com/Crustaly/nomi)

### Skyrchitect  (2025 (NVIDIA-run Devpost event))

- **Prizes:** Second Place [2nd]  (tier: overall_top3)
- **Pitch:** Cloud-architecture agent that designs AWS diagrams from plain-English requirements using Nemotron Nano and the NVIDIA retrieval embedding NIM on SageMaker, with cost estimates and Terraform/CloudFormation output.
- **Problem / user:** Developers struggle to turn app ideas into production cloud infrastructure given service choice, cost and security complexity. / developers and startups designing cloud infrastructure
- **Domain / idea type:** dev_tools + ai_agents_infra / dev_tool
- **Platforms / hardware / AI:** web / False / llm_chat; agent_or_tool_use; rag_or_search; vision
- **Stack:** langs Python; TypeScript; frontend React; React Flow; backend FastAPI; Strands Agents; boto3; db ; hosting AWS SageMaker (ml.g5.xlarge); S3
- **Tech/APIs:** NVIDIA Llama-3.1-Nemotron-Nano-8B NIM on SageMaker (ai_model, core, sponsor); NVIDIA Retrieval Embedding NIM on SageMaker (ai_model, core, sponsor); Amazon SageMaker (cloud, core, sponsor); Strands Agents framework (framework, core); AWS Bedrock Claude (alternate backend) (ai_model, supporting, sponsor); React Flow (framework, supporting)
- **Sponsor APIs:** NVIDIA Llama-3.1-Nemotron-Nano-8B NIM; NVIDIA Retrieval Embedding NIM; Amazon SageMaker | fit: Deployed both required NIMs (Nemotron Nano LLM and retrieval embedding) on SageMaker GPU endpoints and used them for RAG over cloud-architecture patterns plus autonomous tool-calling design, mapping the writeup point by point to the hackathon criteria.
- **Repo:** private_or_missing, commits None (before/in/after event: None/None/None), README None
- **Demo/writeup:** video True, live none, screenshots 0, writeup long, impact claims True (Reports 0.900 retrieval similarity scores and a $2.82/hour endpoint cost; the 0.900 score is said to come from fallback embeddings.)
- **Notes:** Adapter makes the Strands Agents framework work with SageMaker NIM endpoints; the same codebase can switch to Bedrock Claude via an environment variable; hash-based fallback embeddings used when endpoints are down; five custom tools; GitHub link only, no screenshots.
- **Team size:** 1 | **Confidence:** high | unverified: ui_polish; placement_tier; team_size (one private profile); repo_clone_failed
- **Links:** [Devpost](https://devpost.com/software/skyrchitect-6d37yf) | [GitHub](https://github.com/EimisPacheco/nvidia-aws-skychitect)
