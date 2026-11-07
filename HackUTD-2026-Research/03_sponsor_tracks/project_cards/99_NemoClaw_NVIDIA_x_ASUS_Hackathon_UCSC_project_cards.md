# NemoClaw NVIDIA x ASUS Hackathon @ UCSC: project cards (3 projects)

Facts and short paraphrases only; no cross-project analysis. Full records are in the workbook and JSONL.

## 2026

### ClawForge  (2026)

- **Prizes:** Best Use of Brev [unknown]  (tier: sponsor_winner)
- **Pitch:** No-code agent builder where small-business owners describe an agent in plain English and get a visual blueprint with tools, memory, policies and approval gates, using Nemotron and NemoClaw safety.
- **Problem / user:** Small businesses want automation but lack the time or skills to wire up tools, prompts, memory, deployment and safety policies. / small business owners
- **Domain / idea type:** ai_agents_infra + productivity_workplace / automation_or_agent
- **Platforms / hardware / AI:** web / False / llm_chat; agent_or_tool_use
- **Stack:** langs TypeScript; frontend React; Vite; TanStack Router; Tailwind CSS; backend Node.js; Cloudflare Workers; Railway; db Supabase; mem0; hosting Railway; Cloudflare Workers; Brev
- **Tech/APIs:** NVIDIA Nemotron (ai_model, core, sponsor); NemoClaw (framework, core, sponsor); NVIDIA Brev (cloud, supporting, sponsor); NVIDIA NIMs (ai_model, unclear, sponsor); MiniMax (ai_model, supporting); Supabase (database, supporting); mem0 (database, supporting); Railway (cloud, supporting); Cloudflare Workers (cloud, supporting)
- **Sponsor APIs:** NVIDIA Nemotron; NemoClaw; NVIDIA Brev; NVIDIA NIMs | fit: Entered Best Use of Brev; the writeup lists Brev among deployment and runtime paths alongside Railway and Cloudflare, while Nemotron generates the agent blueprints and NemoClaw supplies the safety-policy layer.
- **Repo:** public, commits 109 (before/in/after event: 70/39/0), README detailed
- **Demo/writeup:** video True, live none, screenshots 13, writeup long, impact claims False
- **Notes:** Agent that builds agents; generates workflow-canvas blueprints; shaped by a talk with a local pizzeria owner; has mock-mode fallback when provider keys are missing; Nemotron-nano reliability still listed as future work.
- **Team size:** 4 | **Confidence:** high | unverified: ui_polish; team_size; sponsor_fit_note depth
- **Links:** [Devpost](https://devpost.com/software/clawforge) | [GitHub](https://github.com/animvsh/clawforge)

### FactoryMind  (2026)

- **Prizes:** Best Use of DGX Spark [unknown]  (tier: sponsor_winner)
- **Pitch:** Autonomous factory digital twin where a Nemotron leader agent assigns worker robots to package tasks under policy checks, shown in a 3D Three.js view with live disruption controls.
- **Problem / user:** Autonomous agents should observe a live system, act within bounds and adapt, which warehouse routing makes easy to demonstrate. / warehouse and factory operations planners
- **Domain / idea type:** ai_agents_infra + productivity_workplace / automation_or_agent
- **Platforms / hardware / AI:** web / False / llm_chat; agent_or_tool_use
- **Stack:** langs Python; JavaScript; frontend Three.js; backend Python; Pygame; db ; hosting ASUS GX10 / DGX Spark
- **Tech/APIs:** NVIDIA DGX Spark / ASUS GX10 (hardware_part, core, sponsor); NVIDIA Nemotron Super 49B / Nano 9B (ai_model, core, sponsor); NVIDIA NIM (ai_model, core, sponsor); NemoClaw policy YAML (framework, supporting, sponsor); TensorRT-LLM (framework, supporting, sponsor); Three.js (framework, supporting)
- **Sponsor APIs:** NVIDIA DGX Spark; NVIDIA Nemotron; NVIDIA NIM; NemoClaw; TensorRT-LLM | fit: Targeted Best Use of DGX Spark by serving Nemotron Super 49B and Nano 9B through local NIM endpoints on an ASUS GX10 (DGX Spark-class) box, falling back to NVIDIA cloud endpoints, to drive the agent fleet.
- **Repo:** public, commits 51 (before/in/after event: 0/51/0), README detailed
- **Demo/writeup:** video True, live none, screenshots 1, writeup medium, impact claims False
- **Notes:** Leader on Nemotron Super 49B and workers on Nemotron Nano 9B via OpenAI-compatible NIM endpoints (local GX10/DGX Spark or NVIDIA cloud); pathfinding and policy checks stay deterministic; PNG floorplan upload builds the sim.
- **Team size:** 4 | **Confidence:** high | unverified: ui_polish
- **Links:** [Devpost](https://devpost.com/software/factorymind) | [GitHub](https://github.com/rohanlab104/R2D2)

### MonkeyClaw  (2026)

- **Prizes:** Best Use of NemoClaw [unknown]  (tier: sponsor_winner)
- **Pitch:** Autonomous red/blue/purple-team agent loop that continuously attacks NemoClaw's security controls, patches findings through verifier gates and checks the defenses emit telemetry.
- **Problem / user:** Coding agents are highly privileged and constantly changing, so one-time audits go stale and a blocked attack without telemetry hides regressions. / agent platform and security teams
- **Domain / idea type:** safety_security + ai_agents_infra / dev_tool
- **Platforms / hardware / AI:** web; cli / False / llm_chat; agent_or_tool_use
- **Stack:** langs Python; frontend ; backend FastAPI; MCP; tree-sitter; db SQLite; hosting NemoClaw sandboxes; NVIDIA Brev
- **Tech/APIs:** NemoClaw (framework, core, sponsor); NVIDIA Nemotron (Nano/Super, content-safety reasoning) (ai_model, core, sponsor); NVIDIA Brev (A100 finetune) (cloud, core, sponsor); OpenClaw (framework, core, sponsor); MCP control plane (framework, supporting); MITRE ATLAS / OWASP-LLM catalogs (data_source, supporting)
- **Sponsor APIs:** NemoClaw; OpenClaw; NVIDIA Nemotron; NVIDIA Brev | fit: Targeted Best Use of NemoClaw by making NemoClaw both the runtime and the attack target, running the red-blue-purple loop against live NemoClaw sandboxes with Nemotron models and a Brev-finetuned red-team model.
- **Repo:** public, commits 415 (before/in/after event: 81/334/0), README detailed
- **Demo/writeup:** video True, live none, screenshots 10, writeup long, impact claims True (Claims 0% refusal on held-out eval, 1,032 training examples, 1000+ tests, 18 attack zones and 8 verifier gates.)
- **Notes:** Includes a Nemotron-3-Nano-4B LoRA-finetuned on Brev (A100) using 1,032 self-generated examples as the red-team model; five-role Nemotron judge ensemble; 1000+ tests; detection-as-pass scoring.
- **Team size:** 3 | **Confidence:** high | unverified: ui_polish
- **Links:** [Devpost](https://devpost.com/software/monkeyclaw) | [GitHub](https://github.com/justin06lee/monkeyclaw)
