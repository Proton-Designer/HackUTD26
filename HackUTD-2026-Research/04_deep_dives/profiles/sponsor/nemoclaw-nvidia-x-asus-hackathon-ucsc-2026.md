# NemoClaw NVIDIA x ASUS Hackathon @ UCSC — 2026 (3 projects)

### ClawForge
*NemoClaw NVIDIA x ASUS Hackathon @ UCSC 2026 · dataset: sponsor · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** Best Use of Brev

**What it is:** A prompt-first builder where a small-business owner describes an agent in plain English and gets a structured blueprint (workflow, tools, memory, policies, approval gates) on a visual canvas, then runs it in a NemoClaw sandbox on Brev with a live audit dashboard and final report.
**Problem / user:** Small business owners (pizza shop example) who need automation but cannot wire tools, prompts, memory and safety policies themselves.

**Features**
- Prompt-to-blueprint builder — Nemotron generates structured agent plans; chat on left, workflow canvas on right. *[shown_working]*
- Safety layer — NemoClaw policies, approval gates, audit stream and memory rules. *[claimed]*
- Runtime dashboard and incident report — Pages for live runtime, audit, approvals, memory and a final report from predeploy test runs. *[claimed]*
- Brev-hosted runtime — API can create or reuse a Brev GPU VM for generated NemoClaw instances. *[claimed]*
- Provider fallback and mock mode — MiniMax fallback and mock API for demos. *[shown_working]*
- Accounts and integrations — Supabase accounts; Composio, AgentMail and Vapi hooks. *[claimed]*
- Chat as true agent editor — Commands like add Slack update canvas. *[planned]*

**Flow:** Describe the agent in plain English → Review generated blueprint → Run predeploy test in sandbox → Watch audit stream and approve gated actions → Read final incident report

**Prompt:** 24-hour build of a deployed autonomous OpenClaw agent powered by Nemotron with persistent memory, multi-step reasoning and live tool use. Cloud track runs on Brev; Edge track on ASUS Ascent GX10 (DGX Spark); bonus track for deploying via the NemoClaw security sandbox.
**Fit (explicit):** README names a Brev GPU VM as canonical runtime, with Brev CLI calls, setup script and Launchable checklist, hosting NemoClaw sandbox plus Nemotron reasoning.  *(targeted: Best Use of Brev)*
**Sponsor tools:** NVIDIA Brev (canonical GPU VM runtime and brev create for generated instances, core); NemoClaw (policies, approvals, audit logs, memory rules, core); Nemotron / NIM (blueprint reasoning, core)
**AI:** Nemotron (target nemotron-3-nano-30b) produces blueprint JSON; MiniMax as fallback; agents run under NemoClaw with memory via mem0/Supabase.
**Architecture:** TanStack/React app plus Node API on Railway and Cloudflare Worker mirror; Brev VM runs NemoClaw sandbox; Supabase for accounts; contracts shared across pages.
**Novelty:** Treats safety (approval gates, audit, pre-deploy test report) as a first-class output of agent creation, with a real local business as design input.
**Scope:** large · working: Live Cloudflare app and health endpoint, 28k lines, tests and Docker, YouTube demo; README calls API mock-functional. · polish: Multi-page UI, deploy docs for Railway and Brev, Supabase migrations.
**Claims:** Every small business can build an AI workforce from a prompt
**Gaps:** video not watchable; README says API is mock-functional
Sources: https://devpost.com/software/clawforge, https://github.com/animvsh/clawforge (evidence README), https://nemoclaw.devpost.com/ (via sponsor_prompts_NVIDIA.jsonl)

---

### FactoryMind
*NemoClaw NVIDIA x ASUS Hackathon @ UCSC 2026 · dataset: sponsor · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** Best Use of DGX Spark

**What it is:** A browser 3D warehouse digital twin where colored packages spawn, a Nemotron leader assigns idle worker robots to pick-up pads and matching drop boxes, and workers path-find under a NemoClaw-style allow/deny policy file that logs decisions.
**Problem / user:** Operations teams coordinating many mobile robots who need a single inspectable, policy-bound controller with fallbacks; used as a demo for autonomy that acts under constraints.

**Features**
- Leader-worker dispatch — Leader proposes JSON assignments (Nemotron Super 49B via NIM), validated; deterministic nearest-worker planner runs when model is unreachable. *[shown_working]*
- Pathfinding workers — A* movement; pick up only at pads, drop only at matching colors. *[shown_working]*
- Policy governance — scripts/nemoclaw_policy.yaml allow/deny rules for leader and workers, decisions logged. *[shown_working]*
- Live controls — Start/stop, speed, order spikes and worker failure with rerouting. *[claimed]*
- Layout builder and PNG import — Build walls, factories, boxes in browser; upload floorplan PNG to convert. *[claimed]*
- Worker Nano rationales, memory — Planned. *[planned]*

**Flow:** Press START in web UI → Factories spawn packages → Leader assigns workers → Workers deliver while policy logs fill → Inject failures or spikes → Edit layout and compare

**Prompt:** 24-hour build of a deployed autonomous OpenClaw agent powered by Nemotron with persistent memory, multi-step reasoning and live tool use. Cloud track runs on Brev; Edge track on ASUS Ascent GX10 (DGX Spark); bonus track for deploying via the NemoClaw security sandbox.
**Fit (explicit):** Runs Nemotron through local NIM endpoints on an ASUS GX10 (DGX Spark) as edge leader, with NemoClaw-style policies; also supports NVIDIA cloud endpoints.  *(targeted: Best Use of DGX Spark)*
**Sponsor tools:** DGX Spark / ASUS GX10 (hosting local NIM endpoints, core); Nemotron (Super 49B, Nano 9B) (leader assignments; worker model configured, core); NemoClaw-style policy (allow/deny rules and logs, supporting)
**AI:** Nemotron leader outputs JSON task assignments over an OpenAI-compatible client; output validated and discarded if illegal; deterministic planner fallback; movement kept in code.
**Architecture:** Python simulation core with A*, leader/worker agents, policy loader and a stdlib HTTP bridge feeding a Three.js browser UI.
**Novelty:** LLM is deliberately an optional layer over deterministic safe planning; policy file gates what agents may do.
**Scope:** small · working: About 6.7k lines with tests and scripts; runnable web demo; no video or live link. · polish: Thorough README; 3D UI; no CI or Docker.
**Claims:** Dispatch continues when the model endpoint is down
**Gaps:** no video; no metrics
Sources: https://devpost.com/software/factorymind, https://github.com/rohanlab104/R2D2 (evidence README), https://nemoclaw.devpost.com/ (via sponsor_prompts_NVIDIA.jsonl)

---

### MonkeyClaw
*NemoClaw NVIDIA x ASUS Hackathon @ UCSC 2026 · dataset: sponsor · tier: sponsor_winner · evidence A · confidence high*
**Prizes:** Best Use of NemoClaw

**What it is:** An autonomous red/purple/blue security agent that attacks NemoClaw sandboxes with Nemotron-generated ideas, judges and reproduces findings, drafts patches through an 8-gate verifier, and checks the defense emitted telemetry.
**Problem / user:** Teams running coding agents with broad privileges, where one-off audits go stale and silently blocked attacks can regress unnoticed.

**Features**
- Five-stage loop — Red, judge, repro, blue, purple run end to end across 18 attack-surface zones with MITRE ATLAS and OWASP-LLM seeding. *[shown_working]*
- Tiered judging — Programmatic checks then a five-role Nemotron ensemble with Elo weighting and frontier appeal. *[claimed]*
- Reproduction and root cause — Replays on fresh victims, delta-minimizes, BFS over SQLite code graph, cold verify. *[claimed]*
- Patch verifier — Eight gates including mutation robustness and telemetry still firing. *[claimed]*
- Detection-as-pass scoring — Control passes only if blocked and observed in NemoClaw telemetry. *[claimed]*
- Custom red-team model — Nemotron-3-Nano-4B LoRA-tuned on 1,032 examples on Brev A100. *[claimed]*
- Zero-credential demo with dashboard — One command runs a real cycle on planted vulnerabilities, shown in eleven panels. *[shown_working]*

**Flow:** Run one-command demo → Red generates and executes attacks → Judge and repro confirm findings → Blue patches through verifier gates → Purple scores detection and loops back → Watch eleven-panel dashboard

**Prompt:** 24-hour build of a deployed autonomous OpenClaw agent powered by Nemotron with persistent memory, multi-step reasoning and live tool use. Cloud track runs on Brev; Edge track on ASUS Ascent GX10 (DGX Spark); bonus track for deploying via the NemoClaw security sandbox.
**Fit (explicit):** Treats NemoClaw itself as the target and runtime: attacks its sandboxes, privacy routing and permissions, and measures its telemetry; Nemotron drives all roles.  *(targeted: Best Use of NemoClaw)*
**Sponsor tools:** NemoClaw (runtime sandboxes and the probed security controls, core); Nemotron models (ideation, judging, content-safety role, custom fine-tuned red model, core); NVIDIA Brev (A100 for LoRA fine-tuning, supporting)
**AI:** Per-role Nemotron routing, ensemble judge with Elo, LoRA-tuned Nemotron-3-Nano-4B for attack ideation, frontier-model appeal for split votes.
**Architecture:** Python/FastAPI orchestrator with strict interface contracts between red, blue and purple teams, SQLite code graph and migrations, MCP control plane, OpenAI-compatible inference endpoints.
**Novelty:** Detection-as-pass scoring and the purple layer; custom fine-tuned attack model; very large codebase with 1000+ tests for a 24-hour event.
**Scope:** large · working: Over 450 files, about 57k lines, 154 test files, Docker, one-command demo with planted-vulnerability victim. · polish: Extensive docs folder, dark/light branded assets, status section, quick start.
**Claims:** 1000+ tests | 18 attack zones | Red model 0% refusal on held-out eval | Eight verifier gates
**Gaps:** no video
Sources: https://devpost.com/software/monkeyclaw, https://github.com/justin06lee/monkeyclaw (evidence README), https://nemoclaw.devpost.com/ (via sponsor_prompts_NVIDIA.jsonl)

---

