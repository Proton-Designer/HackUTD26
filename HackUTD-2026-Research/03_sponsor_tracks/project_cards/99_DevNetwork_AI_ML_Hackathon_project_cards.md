# DevNetwork [AI + ML] Hackathon: project cards (2 projects)

Facts and short paraphrases only; no cross-project analysis. Full records are in the workbook and JSONL.

## DevNetwork [AI + ML] Hackathon 2026

### Argus  (DevNetwork [AI + ML] Hackathon 2026)

- **Prizes:** Crusoe: Build a Hermes / NemoClaw agent running Nvidia Nemotron on Crusoe Cloud Managed Inference [unknown]  (tier: sponsor_winner)
- **Pitch:** Autonomous on-call SRE agent that runs two LLMs in lockstep (Claude primary, Nemotron shadow) so investigations survive provider outages, with a learning incident knowledge graph.
- **Problem / user:** Production agents die when their LLM provider degrades and incident knowledge is lost after each outage. / on-call SRE and platform teams running agents
- **Domain / idea type:** dev_tools + ai_agents_infra / automation_or_agent
- **Platforms / hardware / AI:** web / False / llm_chat; agent_or_tool_use; rag_or_search
- **Stack:** langs TypeScript; Python; frontend Next.js 16; React 19; Tailwind CSS; backend Hono; FastAPI; Node.js; db Neo4j; Graphiti; hosting Vercel; DigitalOcean; Docker; Caddy
- **Tech/APIs:** NVIDIA Nemotron on Crusoe Cloud Managed Inference (ai_model, core, sponsor); NVIDIA NIM (ai_model, supporting, sponsor); Claude (ai_model, core); TrueFoundry AI Gateway (other, core); Neo4j + Graphiti (database, core); MCP (framework, core)
- **Sponsor APIs:** Crusoe Cloud Managed Inference; NVIDIA Nemotron; NVIDIA NIM | fit: Targeted the Crusoe/Nemotron challenge: Nemotron hosted on Crusoe Managed Inference serves as the shadow model that takes over when Claude fails, and also does Graphiti entity extraction and reranking.
- **Repo:** public, commits 105 (before/in/after event: 0/105/0), README detailed
- **Demo/writeup:** video True, live not_checked, screenshots 28, writeup long, impact claims False
- **Notes:** Dual-cognition design treats disagreement between models as a hallucination signal; includes a fictional product (Ridgeline) with six fault scenarios and live chaos failover demo.
- **Team size:** 1 | **Confidence:** high | unverified: ui_polish
- **Links:** [Devpost](https://devpost.com/software/argus-475hkv) | [GitHub](https://github.com/aditya1rawat/devnetwork-aiml-hackathon-2026)

### Leavitt: On-Call AI Agent, Turns Alerts Into Answers  (DevNetwork [AI + ML] Hackathon 2026)

- **Prizes:** Crusoe: Build a Hermes / NemoClaw agent running Nvidia Nemotron on Crusoe Cloud Managed Inference [unknown]  (tier: sponsor_winner)
- **Pitch:** Read-only on-call agent that diagnoses incidents from Prometheus, Loki, k6 and feature-flag data via MCP, constrained by a state machine so it reports confidence honestly.
- **Problem / user:** LLM triage agents invent confident wrong root causes, and agents that can act may worsen outages. / on-call engineers and SRE teams
- **Domain / idea type:** dev_tools + ai_agents_infra / automation_or_agent
- **Platforms / hardware / AI:** cli; bot_or_chat / False / agent_or_tool_use; llm_chat
- **Stack:** langs Python; frontend ; backend Burr; FastMCP; Theodosia; db ; hosting 
- **Tech/APIs:** NVIDIA Nemotron via Crusoe Cloud managed inference (ai_model, core, sponsor); Hermes agent (NousResearch) (framework, core); TrueFoundry AI Gateway (other, supporting); Burr (framework, core); Grafana/Prometheus/Loki/k6 (data_source, core); MCP (framework, core)
- **Sponsor APIs:** Crusoe Cloud managed inference; NVIDIA Nemotron | fit: Targeted the Crusoe challenge by running the agent as a Hermes agent whose driving model is Nemotron on Crusoe managed inference, which walked the Leavitt MCP workflow to a correct diagnosis.
- **Repo:** public, commits 84 (before/in/after event: 0/68/16), README detailed
- **Demo/writeup:** video True, live none, screenshots 19, writeup long, impact claims False
- **Notes:** Burr state machine mounted as an MCP server (Theodosia) forces validated steps; benchmarked against a bare agent under chaos using the OpenTelemetry Demo and flagd; runs unattended via Hermes cron.
- **Team size:** 1 | **Confidence:** high | unverified: ui_polish; team_size
- **Links:** [Devpost](https://devpost.com/software/leavitt) | [GitHub](https://github.com/msradam/leavitt)
