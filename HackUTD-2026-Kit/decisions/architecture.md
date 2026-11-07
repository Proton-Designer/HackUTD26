---
name: architecture
description: Load at H0:00-H3:00 when turning the locked idea into components, owners, data path, AI design, and an offline mode; again when a dependency (API, Wi-Fi, hardware) is slow or flaky, when someone proposes a new service, agent, or vector DB, at the H10-12 "should we restructure?" moment, and at H18-22 demo hardening.
---
# Decision guide: architecture

## Open this when
- **H0-H3:** the idea is locked; pick components, owners, stack, data, AI pattern, and the offline path, then ship a walking skeleton.
- **H2-H8:** an integration returns nothing useful, a call takes over 2s, a device drops out, a source caps you, or someone wants Redis, a vector DB, a second service, or "a few agents."
- **H10-H12:** merge collisions tempt a rewrite. **H18-H22:** freezing the demo and preparing "what if the Wi-Fi dies / is this real data / how does it work?"

## What to hand the team
The answer is the filled sheet below, built from the team's real names, skills, hour, and stack. Not the steps, not voting tables or probability math (CLAUDE.md §5). It must contain:
1. **Component diagram, 5-7 boxes, one named owner each; every teammate owns at least one box** and the boxes they own form a slice they can demo alone against a mocked contract. Typical split: UI + demo flow / API + data / AI or model core / hardware or integration + offline mode. [Singer, Shape Up, p.96-97]
2. **Data path, every source labeled REAL or SYNTHETIC** on the diagram and in the UI, plus one path that takes real data live (CSV upload, or one real public dataset) so "is this real?" gets a demo, not a promise.
3. **Offline mode:** what runs with no network (local SQLite or CSV snapshot, recorded LLM responses, hardware simulator), the single switch that turns it on, the visible badge that says so, and the test: full demo path the night before with Wi-Fi physically off. [Xu, System Design Interview, p.16]; [Lakshmanan, ML Design Patterns, p.306-308]
4. **1-2 depth features judges can probe** (pick ones that expose the differentiator's internals, see step 8).
5. **One tradeoff line per major choice:** "We chose X over Y because Z; cost W; fallback V."

## Steps
1. **Demo path (H0).** 3-5 steps a judge sees in under 2 minutes; mark the differentiator. Label each step Real / Fake / Cut. Differentiator is Real, always; if it cannot be real by H12, change the differentiator. Gated, paid, slow, or flaky steps: Fake (recorded response, cached output, seeded data) with an honest framing line. Auth, settings, admin: hardcode or cut. [Seed: A. Hackathon Kit, §A7]
2. **AI job and pattern.** Write "Given X, predict Y, judged by Z" and what the team owns beyond the model call. If a rule solves it, carve out the one sub-step only a model can do. Steps known in advance: a chain of 2-4 calls with code checks between. Few input types: temperature-0 router with enum output. Agent only if failures are cheap (3-5 tools, 5-8 step cap, spend cap). Let code own the facts (prices, counts, dates) and the model only word them. [Huyen, Designing ML Systems, p.62]; [Huyen, AI Engineering, p.548-551]; [Lakshmanan, Generative AI Design Patterns, p.584-596]
3. **Data model and source.** List entities and the 3-5 queries the demo runs; default to hosted Postgres or SQLite with a JSON column; freeze schema by H3-4. Source ladder: sponsor data, official API, open portal (Dallas OpenData, Texas Open Data, Census, FRED, NOAA), curated repo, polite scrape, hand collection, labeled synthetic. Check the browser Network tab for a hidden JSON endpoint before scraping. Synthetic data: generate it from a schema that matches a real source's columns, so the same loader ingests real CSVs unchanged. [Xu, System Design Interview, p.8]; [Seed: A. Hackathon Kit, §A3]; [Web Scraping with Python, p.315-318]
4. **Shape.** One deployable plus one DB. A second process only for a different runtime (Python ML worker, long LLM stream, a hardware bridge that must own a serial port). Hard cap: UI + API + one worker. Any tool fewer than two teammates have used gets a 30-minute smoke test; cap 3 such tools. [Fundamentals of Software Architecture, p.384-385]; [Seed: Hackathon Kit, §A1]
5. **Knowledge and latency.** Corpus under about 200K tokens: in the prompt with caching, no retriever; larger: BM25 first. Under ~2s: plain call; 2-10s: stream with named stages; over 10s: jobs-table row and poll. No broker. Precompute outputs for known demo inputs; keep live for "try your own." [Huyen, AI Engineering, p.497-498, p.505-506]; [Huyen, Designing ML Systems, p.224-233]
6. **Owners and contracts.** Assign boxes by actual skill, not preference. Write one shared types file (request/response/error per route) in the first 15 minutes so everyone builds against mocks; changes after the first integration are additive only. [Newman, Building Microservices 2e, p.236-244]
7. **Offline and fallback design.** Every external dependency (LLM, sponsor API, Wi-Fi, hardware) sits behind one wrapper with a timeout, one retry, a fake twin, and a visible fallback flag; one DEMO_MODE / OFFLINE switch in config picks real or fake. Offline set: committed SQLite or CSV snapshot, recorded responses for the demo inputs (saved from the first real calls), and for hardware a simulator replaying recorded readings. Core logic must run from a script with no server or network. [Ousterhout, Philosophy of Software Design, p.98-99]; [Martin, Clean Architecture, p.212, p.267-271]
8. **Depth features (choose 1-2).** Options: an **explain endpoint** returning why this output (the computed inputs, rules, retrieved sources, or top feature attributions that drove it), shown as a "why?" panel; **bring-your-own-data** (CSV upload or a judge's own text) that runs the real pipeline live; a **verifier** that checks model output against computed facts (totals sum, fields exist in source) and flags mismatches; a live **eval or accuracy readout** ("34 of 40 on our test set"). Each must hit the real core, not a canned path. [Lakshmanan, ML Design Patterns, p.169]; [Lakshmanan, Generative AI Design Patterns, p.599-609]; [Heath, Made to Stick, p.143-145]
9. **Checkpoints.** H2: each integration returns one real response from a minimal script, else drop it unless core or sponsor-required. H3:30: skeleton live on the public URL touching every dependency; if not, all four fix deploy. H6: differentiator gives real output on real input, deployed; else one 60-minute alternative. H10-12: if teammates collide or one area breaks another, split by module folder, do not re-architect. If the team is past a checkpoint, say what to do now. [Brooks, Mythical Man-Month, p.200]; [Seed: E. Walking Skeleton, §E]; [Fundamentals of Software Architecture, p.315]
10. **Hardening (H18-22).** Night before: Wi-Fi off, run the full path in offline mode. Point each integration at a fake server (/hang, /500, /garbage, /empty) and confirm the fallback shows. Run the heaviest flow 10 times, then in two tabs. Freeze a demo deployment with its own keys and DB; warm-up request before each judge. [Nygard, Release It!, p.136-140, p.119-123, p.50-56]

## Template
```
ARCHITECTURE SHEET (fill by H3, pin in the team doc)
COMPONENTS (5-7 boxes)            OWNER     REAL/FAKE  FALLBACK (offline)
 UI + demo flow                   ____      ____       static build, local API
 API + DB (____)                  ____      ____       SQLite/CSV snapshot in repo
 AI core: given __ predict __     ____      REAL       recorded responses, badge
 Integration/hardware: ____       ____      ____       simulator / replay file
 Depth feature: ____              ____      REAL       ____
Arrows: UI -> API -> AI core -> DB; device -> bridge (sole port owner) -> API
DATA PATH
 Source ____  REAL / SYNTHETIC (label shown in UI: ____)
 Real-data path for judges: CSV upload [ ] / live public source ____ [ ]
 Synthetic generated from columns of: ____ (same loader as real)
OFFLINE MODE  switch: ____   badge: "offline mode"   tested Wi-Fi off: date/time ____
 Works offline: ____   Needs network: ____ (what judges see instead: ____)
DEPTH FEATURES  1. ____ (probe: "click why?")  2. ____
AI: pattern ____  model ____ (pinned, temp 0)  way out: "unknown" / out-of-scope
TRADEOFFS  We chose __ over __ because __; cost __; fallback __
CHECKPOINTS  H2 real calls [ ]  H3:30 skeleton [ ]  H6 real core [ ]  Wi-Fi-off run [ ]
```

## Principles
1. **Every outbound call goes through one wrapper with a timeout, at most one retry, a fake twin, and a visible fallback flag.** Integration points are the top cause of failure and most clients wait forever by default; the fake doubles as offline mode. [Nygard, Release It!, p.111-114]; [Ousterhout, Philosophy of Software Design, p.98-99]
2. **The fastest, most reliable network request is no network request.** Venue Wi-Fi and third-party APIs are the demo's single points of failure; a local snapshot and recorded responses remove them. [Kleppmann, DDIA, p.669-670]; [Xu, System Design Interview, p.16]
3. **A slow response is worse than an error (counterintuitive).** Cap waits at 8-10s, then serve cached; slowness cascades and users reload. [Nygard, Release It!, p.100-101]
4. **Multiply reliabilities before adding a dependency or AI step.** Five serial 99.9% dependencies cap you near 99.5%; 10 agent steps at 95% succeed about 60%. Keep 1-2 required integrations on the demo path. [Nygard, Release It!, p.102-105]; [Huyen, AI Engineering, p.539]
5. **Never more services than people; one repo, one deployable, one DB (counterintuitive).** [Brooks, Mythical Man-Month, p.110]; [Fundamentals of Software Architecture, p.603-605]
6. **Wrap hardware in an app-level interface with a simulator from hour one.** Only one device exists and it may fail; a simulator lets every teammate build and is the demo fallback. [Martin, Clean Architecture, p.267-271]
7. **Mock the plumbing, never the magic.** Judges probe the differentiator with fresh input and score technicality on it. [Seed: A. Hackathon Kit, §A7]
8. **Make the depth inspectable.** Judges see architecture in about 4 minutes; an explanation panel or a run on their own data shows the mechanism, where a diagram only claims it. [Seed: Hackathon Kit, §A3]; [Lakshmanan, ML Design Patterns, p.169]
9. **Give the AI a way out: "unknown", "not in sources", out-of-scope.** Retrieval always returns something and judges type off-script. [Alammar, Hands-On LLMs, p.328-329]
10. **Write to one source of truth; rebuild every index or cache from it.** Dual writes drift with no error. [Kleppmann, DDIA, p.596-598]
11. **Every choice names its cost in one line.** No cost named means no trade-off found. [Fundamentals of Software Architecture, p.26-27]

## Mistakes
- **Unowned boxes.** Tell: the diagram has components nobody's name is on, or one person owns the whole backend. Fix: one owner per box, every teammate on the diagram.
- **Offline mode that was never run.** Tell: "we have a fallback" but nobody turned the Wi-Fi off. Fix: the night-before Wi-Fi-off run, logged on the sheet.
- **Synthetic data passed off as real.** Tell: no label, and the team hesitates at "where is this from?" Fix: label it, and show the CSV-upload path on real data.
- **Silent fallback.** Tell: canned data appears and nobody can tell. Fix: visible badge plus log line. [Ousterhout, Philosophy of Software Design, p.106]
- **Vendor SDK on the demo path.** Tell: no timeout parameter, hangs on venue Wi-Fi. Fix: raw REST inside your wrapper. [Nygard, Release It!, p.57-58]
- **Several processes opening the device.** Tell: each request opens the serial port. Fix: one bridge process owns it and broadcasts readings (WebSocket or SSE).
- **Team of agents.** Tell: four named agents in the diagram. Fix: plain code with awaits, one router. [Lakshmanan, Generative AI Design Patterns, p.505-506]
- **Double-click doubles a write.** Fix: client operation id with a UNIQUE constraint. [Kleppmann, DDIA, p.680-683]
- **Open paid endpoint behind a table QR code.** Fix: per-IP rate limit, spend cap, LIMIT 20-50 on queries. [Nygard, Release It!, p.106-109]
- **Mid-build rewrite at H12-16.** Fix: refactor one module, 30-60 minutes, only after two failed patches. [Martin, Clean Architecture, p.39]

## Hackathon calibration
- **Say it, do not build it:** load balancers, sharding, Kubernetes, brokers, multi-region. Name the first real bottleneck (usually the LLM API) and the next rungs: cache, replicas, queue. [Xu, System Design Interview, p.30, p.32]
- **Budget 10-12 real build hours per person;** multiply estimates 1.5-2x for any new API, deploy path, or hardware link. [Brooks, Mythical Man-Month, p.107, p.109]
- **Three folders** (core, adapters, UI); core imports neither, which is what lets offline mode and the simulator swap in. [Martin, Clean Architecture, p.215-219]
- **Every box ties to a demo-visible feature or a likely judge question;** otherwise delete it. [Xu, System Design Interview, p.42]

## Go deeper
- [../domains/13-architecture-tradeoffs.md](../domains/13-architecture-tradeoffs.md): timeouts, breakers, hardening, Q&A math
- [../domains/15-ai-app-design-eval.md](../domains/15-ai-app-design-eval.md): AI pattern, RAG, verification, trust UX
- [../domains/16-data-acquisition.md](../domains/16-data-acquisition.md): source ladder, scraping, data card
- search_experts("offline fallback demo connectivity local copy", domain="15-ai-app-design-eval")
- search_experts("remove single points of failure demo path", domain="13-architecture-tradeoffs")
- search_experts("explain individual predictions feature attributions", domain="15-ai-app-design-eval")
- search_experts("hardware abstraction simulator test off-target", domain="13-architecture-tradeoffs")
