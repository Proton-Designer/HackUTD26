---
name: 13-architecture-tradeoffs
description: Open when picking the stack and system shape at hour 0-3, wiring the first LLM/sponsor/third-party API, deciding sync vs async or cache vs live, when someone proposes services/Kafka/a second database, at the hour 10-12 "should we restructure?" moment, during hour 18-22 demo hardening, and when preparing answers to "why this stack / how does it scale / what if the API dies".
---
# Software architecture and engineering tradeoffs

## Use this when
- Hour 0-3: turning the chosen idea into a stack, a data model, and a box diagram, and a teammate wants to debate frameworks or add "real production" components.
- Wiring any external dependency (LLM, sponsor SDK, scraper, maps, payments) onto the demo path.
- A call takes over ~2 seconds and the UI freezes, or two judges clicking at once could double-book or miscount.
- Hour 10-16: merge collisions, cross-breakage, or the urge to rewrite.
- Hour 18-22: freezing and hardening the demo deployment before science-fair judging.
- Writing the architecture slide, README diagram, and Q&A answers on scale, cost, failure, and security.

## Core principles
1. **One repo, one deployable, one database; never more services than people (counterintuitive).** Each split adds a hop (ten chained 100 ms calls cost a full second, and the p95-p99 tail is worse) and turns one ACID transaction into two-phase commit or sagas; Brooks saw productivity fall from about 10,000 to 1,500 instructions per person-year as component interactions grew. [Brooks, Mythical Man-Month, p.110]; [Fundamentals of Software Architecture 1e, p.176-177]; [Newman, Building Microservices 2e, p.275-281]; [Fundamentals of Software Architecture, p.603-605]
2. **Integration points are the top cause of failure, so put an explicit connect and read timeout on every outbound call, in one shared wrapper.** Most client libraries wait forever by default, and once every request slot hangs the app is down while the process looks "up". [Nygard, Release It!, p.111-114, p.46-47]
3. **A slow response is worse than an error (counterintuitive).** Cap waits at about 8-10s, then serve a cached or canned result; slowness cascades upward and users reload, adding load. [Nygard, Release It!, p.100-101]
4. **Hide each messy dependency behind one deep function that owns retries, timeout, and fallback, and keep a fake implementation beside the real one.** One fix then covers every caller, and the fake doubles as demo insurance and test double; wire the real/fake choice in one config file with a DEMO_MODE switch. [Ousterhout, Philosophy of Software Design, p.98-99, p.44-45]; [Martin, Clean Architecture, p.235, p.241-242]
5. **Make your reliability promise match your weakest required dependency.** Five serial dependencies at 99.9% cap you near 99.5%, so keep only 1-2 integrations required on the demo path and put the rest behind flags. [Nygard, Release It!, p.102-105]
6. **Use the one tool that already does everything; do not distribute what fits on one machine.** Hackathon data fits in RAM, where a single process likely beats a cluster; each added store (Redis, Elasticsearch, Kafka, a vector DB) brings config, quirks, and sync problems. [Kleppmann, DDIA, p.562, p.645, p.662-663]
7. **Write to exactly one source of truth and derive every other copy from it.** Writing the same change to the database and to a cache or vector index from app code leaves them permanently inconsistent with no error. [Kleppmann, DDIA, p.596-598]
8. **Model entities and the 3-5 demo queries first, then freeze the schema by hour 3-4.** The schema is the concrete, heavily depended-on, volatile module that is hardest to change, and data outlives code. [Seed: Synthesis Playbook, §0]; [Martin, Clean Architecture, p.147-149]; [Ford et al., Software Architecture: The Hard Parts, p.22]
9. **Precompute what is slow, common, and knowable in advance; compute live only for open-ended input.** A 100 ms delay cost Akamai 7% conversion and one LLM call outweighs thousands of DB queries, so cache anything that costs money or more than a few seconds and never recompute it during the demo. [Huyen, Designing ML Systems, p.37-40, p.224-233]; [Kleppmann, DDIA, p.558, p.671-672]
10. **Give every live-clicked write a client-generated operation id with a UNIQUE constraint (counterintuitive).** A timed-out request may still have run, and double-clicks and resubmits pass straight through TCP and transactions; only an end-to-end id stops a $11 transfer becoming $22. [Kleppmann, DDIA, p.680-683, p.629-630, p.368-371]
11. **Let the database enforce every "only one" and counter rule (counterintuitive).** SELECT-then-INSERT and read-modify-write both race when two judges click at once (both see the slot free; 42 becomes 43, not 44), and snapshot isolation does not catch it. A UNIQUE index or `SET n = n + 1` is one line. [Kleppmann, DDIA, p.321-323, p.328-330]
12. **Define errors out of existence: make delete, get-or-create, and empty results normal cases instead of exceptions.** Error handling is rarely tested, and a cited study traced over 90% of catastrophic failures in distributed data systems to it. [Ousterhout, Philosophy of Software Design, p.91-98]

## Decision procedure
Main decision: the system shape and stack, settled by hour 3.

1. **Constraints (10 min).** Write the 3-step demo path. Each teammate votes for 3 characteristics from a list of about 7; keep the top 3 (usually speed of delivery, demo reliability, plus one product-specific such as latency or accuracy). Ask "which one would we drop?" and drop it. [Fundamentals of Software Architecture, p.153-158]
2. **Data (15 min).** List entities and the 3-5 queries the demo runs. Default to Postgres (hosted) or SQLite with a JSON column. Choose NoSQL only if you can name one of: blob-only JSON, non-relational data, very low latency, massive volume. [Xu, System Design Interview, p.8]
3. **Shape.** Default: single deployable plus one managed DB. Add a second process only if a component needs a different runtime or operational profile (Python ML worker, LLM streams longer than the serverless timeout). Hard cap: UI + API + one worker, sharing one DB. [Fundamentals of Software Architecture, p.384-385, p.655-656]
4. **Innovation tokens.** Any tool fewer than two teammates have used costs a token; cap at three, and at least one must go to the differentiator. Each token gets a 30-minute smoke test before it enters the plan. [Seed: Hackathon Kit, §A1]; [Brooks, Mythical Man-Month, p.197, p.205]
5. **Integrations.** List every external call. By hour 2, each must return one real response from a minimal script. If it does not, drop it unless it is the core or a sponsor requirement. [Brooks, Mythical Man-Month, p.200]
6. **Sync vs async, by measured latency.** Under ~2s: plain synchronous call. 2-10s: stream (SSE) with a visible loading state; if the user only needs an acknowledgement, return it at once and finish in the background (a 3,100 ms synchronous post became 25 ms perceived) with a status field for failures. Over 10s or batch: insert a row into a jobs table, return immediately, poll or stream status. No message broker. [Seed: Hackathon Kit, §A5]; [Fundamentals of Software Architecture 1e, p.259-261]; [Fundamentals of Software Architecture, p.656-657]
7. **Precompute check.** If the demo inputs are knowable, precompute and store their outputs; keep the live path for "try your own" with the stored answers as fallback. Be ready to say which path is live. [Huyen, Designing ML Systems, p.224-233]
8. **Deadlock rule.** If a choice is still open after 20 minutes, run a 30-minute spike per option or take the option the strongest person already knows. [Fundamentals of Software Architecture, p.71, p.693-694]
9. **Lock and record.** Lock stack, data model, and sync/async by hour 2-3; leave timeouts, caching, and breakers for a later hardening block. Write 4-6 mini-ADRs in DECISIONS.md, each naming its cost. Spend 10-15 minutes writing request/response shapes as one shared types file so front and back build against mocks; after the first integration, changes are additive only. [Nygard, Release It!, p.142-143]; [Newman, Building Microservices 2e, p.236-244]
10. **Go/stop gate at hour 3:** a walking skeleton (UI -> API -> stubbed model/data -> response) is deployed through the real pipeline. If not, cut an integration or a token, not the deploy. [Brooks, Mythical Man-Month, p.216-217]; [Martin, Clean Architecture, p.156]
11. **Hour 10-12 gate:** if two of the monolith warning signs appear (changes slow, one area breaks another, teammates collide in files, slow startup), split ownership by module folder and agree on one interface. Do not re-architect. [Fundamentals of Software Architecture, p.315]

## Checklists

**Architecture review (run at hour 3 and hour 12)**
- [ ] Every box in the diagram ties to a demo-visible feature or a likely judge question; otherwise delete it. [Xu, System Design Interview, p.42]
- [ ] Exactly one write target; secondary stores rebuild from it by script.
- [ ] Every outbound call goes through the wrapper: timeout, at most one retry (idempotent calls only), fallback, and a visible "fallback mode" flag. [Nygard, Release It!, p.113-114]; [Ousterhout, Philosophy of Software Design, p.106]
- [ ] Circuit breaker on each flaky integration: open after 3 consecutive failures, probe after 30s. [Nygard, Release It!, p.115-118]
- [ ] LIMIT on every query and list (20-50 rows) and a cap on what goes into any LLM prompt. [Nygard, Release It!, p.106-109]
- [ ] Keys server-side only (check NEXT_PUBLIC_/VITE_ prefixes), server checks resource ownership, parameterized queries, spend cap on any paid-API endpoint. [Seed: Hackathon Kit, §A7]; [Seed: OWASP Top 10:2025, §I]
- [ ] Per-IP token-bucket rate limit (framework built-in; fixed windows let 2x the quota through at a boundary); typeahead inputs debounced 200-300 ms, since each search otherwise fires about 20 requests. [Xu, System Design Interview 1e, p.72-82, p.255, p.269]
- [ ] Parallel vendor calls capped by a semaphore of 3-5. [Nygard, Release It!, p.96-99]
- [ ] Core logic callable from a script with no server, DB, or UI. [Martin, Clean Architecture, p.212]

**Demo hardening (hour 18-22)**
- [ ] Nasty fake server with routes /hang, /garbage, /slow, /500, /empty; each one shows a fallback in the UI, not a blank screen. [Nygard, Release It!, p.136-140]
- [ ] Heaviest flow run 10 times back to back, then in two tabs at once; record p50 and p95 from the client over 20+ runs (with several backend calls, the slowest sets the wait). [Nygard, Release It!, p.71-72]; [Kleppmann, DDIA, p.32-36]
- [ ] Every booking, claim, vote, or points flow hit by two simultaneous scripted requests; exactly one wins or the count is exact. Manual clicking never finds these. [Kleppmann, DDIA, p.326-331]
- [ ] Frozen demo deployment with its own keys and DB, separate from dev; tag the known-good commit. Any post-freeze fix goes to a preview URL, gets tested, then is promoted, with the old deploy kept for rollback. Config and env mistakes cause more outages than hardware (10-25%). [Nygard, Release It!, p.119-123]; [Newman, Building Microservices 2e, p.370, p.436-437]; [Kleppmann, DDIA, p.26-27]
- [ ] DB snapshot plus one-command reset; full demo run from a clean checkout. [Kleppmann, DDIA, p.679, p.697-700]
- [ ] Warm-up request before each judge visit (idle connections get silently dropped). [Nygard, Release It!, p.50-56]
- [ ] Scripted 5-10 step demo check re-run after every fix, since each fix has a 20-50% chance of a new defect. [Brooks, Mythical Man-Month, p.141]

**Judge Q&A readiness**
- [ ] Tradeoff sentence per major choice: "We chose X over Y because [time / skill / demo reliability / cost]; the cost is W; next step is Z." [Seed: Synthesis Playbook, §0]
- [ ] Scaling answer naming the first real bottleneck (usually the LLM API) and the next 2-3 rungs: cache, read replicas, queue. [Seed: Hackathon Kit, §A9]
- [ ] Capacity and cost math: users x actions / 86,400 = average rps, peak about 2x; tokens x requests x price. [Xu, System Design Interview, p.39]
- [ ] One measured number per top decision, with conditions ("under 2s at 5 concurrent users on free tier"). [Fundamentals of Software Architecture, p.149, p.708-709]
- [ ] Uptime question: an honest target in time (99.9% is about 8h46m a year, 86 s a day) plus what you built (health check, fallback, cached demo), never "five nines". [Fundamentals of Software Architecture 1e, p.455-457]

## Anti-patterns
- **Service-per-feature diagram.** Tell: more boxes than teammates, or services that must call each other to do one job. Fix: merge into the monolith; name the one module you would extract first and why. [Fundamentals of Software Architecture, p.603-605, p.412-413]
- **Dual-write to DB and vector store/cache.** Tell: app code calls `db.insert` then `index.upsert`. Fix: write once, rebuild the index from the DB on startup or a timer. [Kleppmann, DDIA, p.596-598, p.542-543]
- **Trusting the vendor SDK on the demo path.** Tell: no timeout parameter exposed, hangs on bad network. Fix: call the raw REST endpoint inside your own wrapper. [Nygard, Release It!, p.57-58]
- **Retry loops inside a request handler.** Tell: `while (!ok)` around an LLM call. Fix: one short-delay retry max, then fallback; queue work that matters. [Nygard, Release It!, p.67, p.113-114]
- **Silent fallback.** Tell: canned data appears and nobody on the team can tell. Fix: a visible fallback flag and log line; say "mocked" precisely when asked. [Ousterhout, Philosophy of Software Design, p.106]; [Brooks, Mythical Man-Month, p.137]
- **Classitis from AI code generation.** Tell: many thin service/helper classes whose signatures are as long as their bodies. Fix: collapse into fewer, deeper functions; ask the assistant for that explicitly. [Ousterhout, Philosophy of Software Design, p.40-42]
- **Long-lived branches.** Tell: a branch older than a few hours, 3+ active branches, merge hell at hour 20. Fix: merge to main about hourly, hide half-done work behind a config flag, and a red main blocks all other merges until fixed (DORA data ties sub-day branches to higher delivery performance). [Newman, Building Microservices 2e, p.309-313, p.438-439]
- **Upload-then-notify race.** Tell: code stores a file or row, then fires a webhook or queue message to a worker that reads it back. The message can beat the data, leaving results stale for good. Fix: put the payload in the job row in the same DB, or have the worker retry briefly when the object is missing. [Kleppmann, DDIA, p.437-439]
- **Mid-build rewrite.** Tell: "let's restart cleanly" at hour 12-16. Fix: local refactor of one module, capped at 30-60 minutes, only after two failed patches; never restart the app. [Martin, Clean Architecture, p.39]; [Brooks, Mythical Man-Month, p.142]
- **Chaining models or ensembles for accuracy.** Tell: 3+ sequential LLM calls on the hot path. Fix: one model/prompt; add a step only for a measured weakness if latency still fits (20 of 22 Kaggle winners used ensembles, yet they are rarely deployed). [Huyen, Designing ML Systems, p.36-37]

## Hackathon calibration
- The demo is your production launch: highest stakes, least traffic. Spend hardening on integration points (timeouts, fallbacks, demo mode), not scale. [Seed: Release It! Stability Patterns, §F]
- **Say it, do not build it:** load balancers, replicas, sharding, Kubernetes, brokers, CQRS/event-sourcing frameworks, feature stores, continual learning, multi-region, alerting stacks. Prepare the 20-second verbal answer with costs (hot keys, lost cross-shard joins). Host on a PaaS or serverless platform you already know; Kubernetes is "huge overkill" for a handful of developers even when managed. [Xu, System Design Interview, p.30, p.32]; [Newman, Building Microservices 2e, p.413-414, p.434-435]
- **Compress long-horizon design advice.** Ousterhout's 10-20% design investment becomes 2-4 hours: interfaces up front, one mid-build cleanup, one pre-freeze pass on the demo path, no refactors after hour 18. Clean Architecture's four rings become three folders (core, adapters, UI); core imports nothing from the other two. [Ousterhout, Philosophy of Software Design, p.28-31]; [Martin, Clean Architecture, p.182-189, p.215-219]
- **Budget honestly.** Expect 10-12 real build hours per person, not 24. Multiply estimates 1.5-2x for any new API or deploy path, and 2-3x when a standalone script must plug into the shared app. Budget novel systems work (custom protocol, scheduler) at 3x and allow at most one such piece. [Brooks, Mythical Man-Month, p.107, p.109, p.113]
- **Judges skim fast (~4 minutes, science fair).** Architecture shows through a 5-7 box diagram marking real vs mocked, folder names that say what the product does, and one deep component they can probe for technicality. Polish that component and stub the rest. [Seed: Hackathon Kit, §A3]; [Martin, Clean Architecture, p.209-212]; [Xu, System Design Interview, p.46]
- **Burst, not average, load.** Several judges may open the app at once, and a QR code on the table invites a flash mob. Test a few concurrent users on the heaviest endpoint, serve the landing page statically, and rate-limit paid endpoints. Serverless scales out but your DB and LLM quota do not, so set a function concurrency cap. [Fundamentals of Software Architecture, p.138-139]; [Nygard, Release It!, p.88-90]; [Newman, Building Microservices 2e, p.401-403]
- **Default to one responsive web app;** go native only if a sensor or OS feature is the core. In-browser inference (WASM about 45-55% slower than native) only as a deliberate privacy or offline angle. [Fundamentals of Software Architecture, p.147]; [Huyen, Designing ML Systems, p.256-257]
- **Sponsor tech** goes in through an adapter so it is demoable without rewiring the core, and it must materially contribute. [Martin, Clean Architecture, p.285-287]

## Where experts disagree
- **Clean as you go vs ship tactically.** Martin says rushing in a mess is slower even within a day, and Ousterhout says do not postpone cleanup. Brooks and the 24h horizon argue the payoff never arrives. Follow the middle: wrappers and the three-folder split from hour 0 (cheap), then fix structure only when it has slowed a change in the last few hours; Martin's evidence is one developer on a trivial task. [Martin, Clean Architecture, p.37-38]; [Ousterhout, Philosophy of Software Design, p.32-33]
- **Defer the database vs model data first.** Clean Architecture wants in-memory stubs and a late DB choice. The seeds, Hard Parts, and Release It! say data and other irreversible choices come early. Resolution: model entities and queries in the first hour and pick the store the team knows, so nothing is left to defer. Kleppmann's "dump raw data first" applies to acquisition only: save raw API/scrape blobs verbatim, but freeze the app schema by hour 3-4. [Martin, Clean Architecture, p.180-182]; [Kleppmann, DDIA, p.547-548]; [Nygard, Release It!, p.142-143]
- **Sync by default vs async for anything slow.** Fundamentals defaults to sync because async adds races and debugging pain. Release It! warns that sync request/reply turns shocks into cascades. Use the latency thresholds in step 6. [Fundamentals of Software Architecture, p.656-657]; [Nygard, Release It!, p.141-143]
- **Plan to throw one away vs never rewrite.** Brooks says the first version of a novel concept will be wrong. Martin says the same team will rebuild the same mess. Both hold if the throwaway is planned: a 1-2 hour spike on the riskiest piece in a scratch branch, never a whole-app restart. [Brooks, Mythical Man-Month, p.137]; [Martin, Clean Architecture, p.39]
- **Innovation tokens vs "Against Innovation Tokens".** The counterpoint says tokens breed stagnation. For 24 hours follow McKinley, but wrap any risky new tool behind an interface so it can be swapped. [Seed: Choose Boring Technology, §B]
- **Shared types across components.** Newman warns shared domain libraries force lock-step redeploys. That holds only for separately deployed services; in one repo and one deploy, a shared types file is the cheapest contract. [Newman, Building Microservices 2e, p.259-261]
- **Monolith vs services when boundaries are clear.** Fowler admits some argue for services from the start. Fundamentals allows a coarse service-based split when parts need different operational profiles. The only hackathon case is a separate ML or scraping worker sharing the one DB. [Seed: Monolith First, §C]; [Fundamentals of Software Architecture, p.384-385]

## Go deeper
- search_experts("timeouts circuit breaker integration points fallback", domain="13-architecture-tradeoffs")
- search_experts("modular monolith versus microservices when to split", domain="13-architecture-tradeoffs")
- search_experts("dual write source of truth derived data", domain="13-architecture-tradeoffs")
- search_experts("idempotency operation id duplicate requests", domain="13-architecture-tradeoffs")
- search_experts("batch versus online prediction precompute latency", domain="13-architecture-tradeoffs")
- search_experts("deep modules information hiding define errors out of existence", domain="13-architecture-tradeoffs")
- search_experts("architecture decision record trade-off justification", domain="13-architecture-tradeoffs")
- search_experts("back of envelope estimation QPS scaling checklist", domain="13-architecture-tradeoffs")
- search_experts("productivity interactions estimate optimistic schedule testing", domain="13-architecture-tradeoffs")
- search_experts("lost update write skew unique constraint check then insert", domain="13-architecture-tradeoffs")
