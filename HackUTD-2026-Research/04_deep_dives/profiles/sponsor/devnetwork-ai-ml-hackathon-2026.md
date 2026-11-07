# DevNetwork [AI + ML] Hackathon — 2026 (2 projects)

### Argus
*DevNetwork [AI + ML] Hackathon 2026 · dataset: sponsor · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** Crusoe: Build a Hermes / NemoClaw agent running Nvidia Nemotron on Crusoe Cloud Managed Inference

**What it is:** An on-call SRE agent that runs each incident investigation with two LLMs in lockstep (Claude primary, Nemotron on Crusoe as shadow), fails over mid-flight, and stores resolved incidents in a Neo4j/Graphiti knowledge graph. Includes a fictional product, Ridgeline, that triggers it.
**Problem / user:** On-call operators and teams running production agents, which fail when an LLM provider degrades and lose incident knowledge in chat logs.

**Features**
- Dual-cognition investigation — Two models run in lockstep through TrueFoundry gateway; disagreement is a hallucination signal and shadow takes over without losing context. *[shown_working]*
- Chaos failover — Kill-provider action aborts in-flight calls; gateway severance falls back to direct mode. *[shown_working]*
- Brownout detection — Token-set similarity flags slow-but-failing providers without embeddings. *[claimed]*
- Incident knowledge graph — Resolved cases ingested into Neo4j and Graphiti and retrieved, then verified against live signals. *[shown_working]*
- MCP tool servers — Logs, metrics, traces, runbooks and KB wrapped with retries and circuit breakers over a mock cluster. *[shown_working]*
- Ridgeline product simulation — Four surfaces, six faults; embedded launcher streams a Haiku triage then deep-links to Argus. *[shown_working]*
- Approval-gated remediation, real observability — Future work. *[planned]*

**Flow:** Trigger fault in Ridgeline → Launcher streams first-pass triage → Deep-link to full investigation → Argus retrieves similar past incidents → Kill Claude or gateway to watch failover → Resolved case ingested into graph

**Prompt:** Build a Hermes or NemoClaw-style agent harness running NVIDIA Nemotron 3 Nano 30B through Crusoe Cloud managed inference, an OpenAI-compatible endpoint; prizes DGX Spark and Mac mini.
**Fit (explicit):** Uses Nemotron on Crusoe as shadow cognition and for Graphiti extraction and reranking, after other providers rate-limited; Claude is the primary model.  *(targeted: Crusoe: Nemotron agent on Crusoe Managed Inference)*
**Sponsor tools:** Nemotron on Crusoe Managed Inference (shadow investigation model and KB entity extraction/reranking, core)
**AI:** Claude and Nemotron run the same investigation in parallel via TrueFoundry; divergence and brownout heuristics trigger failover; Graphiti uses Nemotron for entity extraction; Claude Haiku for first-pass triage.
**Architecture:** Next.js apps (Argus, Ridgeline) on Vercel; Hono orchestrator conductor, FastAPI KB and mock cluster, Neo4j and Caddy in docker-compose on a DigitalOcean droplet; MCP servers between agent and tools.
**Novelty:** Applies high-availability thinking to the LLM itself, with live failover demos and a product-embedded trigger instead of a standalone chat.
**Scope:** large · working: Three live URLs (two Vercel apps and backend), docker-compose deploy, tests, about 11.6k lines, YouTube video. · polish: Two branded UIs, documented architecture table, deployment write-up.
**Claims:** Zero context loss on failover | Live ingest completes in seconds on Crusoe Nemotron
**Gaps:** video not watchable; data are mocks, no real observability
Sources: https://devpost.com/software/argus-475hkv, https://github.com/aditya1rawat/devnetwork-aiml-hackathon-2026 (evidence README), sponsor_prompts_NVIDIA.jsonl (DevNetwork 2026)

---

### Leavitt: On-call AI agent turns alerts into answers
*DevNetwork [AI + ML] Hackathon 2026 · dataset: sponsor · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** Crusoe: Build a Hermes / NemoClaw agent running Nvidia Nemotron on Crusoe Cloud Managed Inference

**What it is:** A read-only incident-triage agent built as a state machine exposed over MCP: it reads metrics, logs, client load and feature-flag state, correlates them and files a report whose status (resolved, degraded, inconclusive) is limited by the evidence. Runs as a Hermes agent on Nemotron via Crusoe.
**Problem / user:** On-call engineers piecing together dashboards under pressure, where an LLM may give a confident but wrong root cause.

**Features**
- Enforced triage workflow — Burr state machine mounted by Theodosia validates each step: enumerate sources, read, correlate, distill, hypothesize, report. *[shown_working]*
- Four-source evidence reading — Prometheus, Loki, k6 client load and flagd flag state via MCP servers. *[shown_working]*
- Graded conclusions — Reports resolved, degraded or inconclusive; declines on garbage or lost data. *[shown_working]*
- Read-only by design — Graph has no write transitions, so agent cannot change systems. *[claimed]*
- Unattended scheduling and Discord delivery — Hermes cron or webhook triggers runs; report posted to channel. *[claimed]*
- Audit trail and live console — Every read logged and rendered live in a terminal view. *[shown_working]*
- Benchmark against bare agent — Compared with and without the state-machine layer across flagd failure scenarios. *[claimed]*

**Flow:** Submit an incident question or scheduled trigger → Agent enumerates and reads four sources step by step → Evidence correlated and distilled → Hypothesis formed → Report filed with confidence and read trail

**Prompt:** Build a Hermes or NemoClaw-style agent harness running NVIDIA Nemotron 3 Nano 30B through Crusoe Cloud managed inference, an OpenAI-compatible endpoint; prizes DGX Spark and Mac mini.
**Fit (explicit):** Ships as a Hermes agent profile with Nemotron on Crusoe driving the Leavitt MCP, a headless run plus cron deployment; README shows a challenge-winner banner.  *(targeted: Crusoe: Nemotron agent on Crusoe Managed Inference)*
**Sponsor tools:** Nemotron on Crusoe Managed Inference (drives the triage workflow through Hermes, core)
**AI:** Hermes headless agent with Nemotron calls one validated step tool; deterministic distill_evidence step shrinks telemetry before reasoning; TrueFoundry gateway for failover.
**Architecture:** OpenTelemetry Demo with flagd chaos, Prometheus, Loki and k6; fastmcp servers; Burr state machine via Theodosia as MCP; Hermes outer agent; audit trail feeding terminal view.
**Novelty:** Constrains the agent with an enforced state graph instead of trusting the model, and benchmarks that against a bare agent on real fault injection.
**Scope:** medium · working: Demo script brings up real microservice substrate; tests, Docker, bench folder, YouTube video; 4.5k lines. · polish: Branded README with GIF, deploy docs, results table in repo.
**Claims:** No metrics were mocked | Bare agent drifts to confident wrong answers under failure while Leavitt degrades or declines
**Gaps:** video not watchable; benchmark numbers not on page
Sources: https://devpost.com/software/leavitt, https://github.com/msradam/leavitt (evidence README), sponsor_prompts_NVIDIA.jsonl (DevNetwork 2026)

---

