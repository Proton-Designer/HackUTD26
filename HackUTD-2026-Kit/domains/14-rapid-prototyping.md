---
name: 14-rapid-prototyping
description: Open when turning a locked idea into a build in hours 0-3 (demo path, API contract, walking skeleton, first deploy), deciding whether a demo step is built real, faked, or cut, sizing or sequencing a slice, running a spike, coordinating parallel work with git and AI agents, hitting the midpoint or freeze checkpoint, or hardening the demo after freeze.
---
# Rapid prototyping and implementation

## Use this when
- Hour 0-1:30: the idea is locked and the team must turn it into a demo path, an API contract, and four parallel streams before anyone writes feature code.
- Hour 1:30-3:30: building the walking skeleton, or it will not deploy and someone says "we'll fix deploy later".
- A demo step depends on something slow, flaky, gated, or unbuilt (LLM, sponsor API, dataset, hardware) and you must choose build real, fake, or cut.
- A task estimate exceeds 2 hours, someone has been stuck 30 minutes, or an AI agent has looped on the same bug twice.
- The midpoint (~+12h) or feature freeze (~+18h) arrives and the full demo does not run end to end.
- Post-freeze: hardening, fallbacks, tagging the demo build, and deciding which bugs to touch.

## Core principles
1. **Get a walking skeleton onto a public URL in the first 2-3 hours, touching every external dependency.** (counterintuitive) It delivers no user value, but one click traveling UI -> API -> DB/LLM -> UI flushes out env-var, CORS, key, and deploy failures while they cost minutes instead of the last 3 hours. [Seed: E. Walking Skeleton, §E] [Seed: A. Hackathon Kit, §A4] [User Story Mapping, p.103-104]
2. **Push the novel, risky slice uphill next, and call it solved only when a real call returns real data inside your app.** (counterintuitive) Login, nav, and the shell feel productive but teach nothing; reading the docs is "thought about it", not "validated". [Shape Up, p.111-112, p.139-141] [Lean Startup, p.100-101]
3. **Keep tracer code; throw away spikes.** The demo path is thin but real (structure, error handling, real environment) and grows into the final system; a spike answers one written question in 30-60 minutes and is then deleted, because a prototype that quietly becomes the product is a movie-set facade with nothing behind it. [Seed: D. Tracer Bullets vs Prototypes, §D] [Seed: 0. Synthesis / Playbook, §3]
4. **Mock the plumbing, never the magic.** Seeded data, recorded API responses, cached LLM outputs, hardcoded auth, and a human behind the curtain are legitimate for non-core steps (Aardvark ran human-powered backends for months; Food on the Table served its first customer with no software), but the differentiator must run live on a judge's fresh input. [Seed: A. Hackathon Kit, §A7] [Lean Startup, p.85-91] [Sprint, p.138-140]
5. **Agree the API contract as JSON examples in hour 1, then parallelize against mocks.** (counterintuitive) Spending hour 1 not coding is what lets frontend build against a local mock of the exact JSON while backend and AI build the real thing, with nobody waiting; changing the contract means telling the other side out loud. [Seed: A. Hackathon Kit, §A5] [Shape Up, p.107-111]
6. **Build half a product, not a half-assed one: one golden path, each screen with regular, blank, and error states.** Two features that work flawlessly beat six that half-work, and a judge lands on the empty or failing screen more often than your seeded happy path suggests. [Seed: 0. Synthesis / Playbook, §6] [Getting Real, p.81-84] [Lean UX, p.120-121]
7. **Every estimate over 2 hours triggers "what is the 1-hour version?"** Restate the hard problem as an easier one with the same user outcome (IMVU replaced avatar walking with teleportation and users ranked it a top-3 feature). Price a feature as UI + backend + error state + demo data + pitch line; needing more than three of those means it is not cheap. [Lean Startup, p.92-93] [Getting Real, p.46, p.88-89, p.91]
8. **Wire affordances before pixels; polish only the demo path, only in the last 4-5 hours.** Plain buttons, inputs, and places where data appears answer "does it work and make sense"; early spacing and color work is fake progress because you cannot yet tell which details matter. [Shape Up, p.107-111] [Getting Real, p.37]
9. **Keep `main` always deployed and demoable.** Small commits, `git pull --rebase` before every push, branches that live hours, one owner per file where possible, unfinished work behind a `DEMO_MODE`/`SHOW_X` env flag, and a `demo-v1` tag you can redeploy from in one step. [Seed: J. Version Control for Speed, §J] [Seed: A. Hackathon Kit, §A9]
10. **Drive AI agents with small, bounded tasks and a context file.** Stack, folder layout, conventions, and do-not-touch files go in CLAUDE.md/AGENTS.md; one specific task per prompt, with the curl or test input requested alongside; commit before every large AI edit; never two agents on the same files. Mega-prompts ("add billing") plant timebombs and agents overshoot scope. [Seed: A. Hackathon Kit, §A8] [Seed: I. AI-Assisted Building (2026), §I]
11. **Wrap every external API in one module with a recorded-response fallback.** Providers rename fields and rate-limit without warning; validate the response shape, save a sample, and flip to it if the live call fails during judging. Start canned end to end, then go live only on the step judges will probe. [Make, p.121] [Lean UX, p.120]
12. **Fix the clock with hard checkpoints; the deadline is the circuit breaker.** Skeleton by ~+3:30, full demo path by ~+12h, freeze at ~+18h. Knapp found 10-day to 6-week sprints achieved little more than 5 days and bred attachment, so nothing still uphill at freeze gets more time. [Seed: A. Hackathon Kit, §A2] [Sprint, p.35-36] [Shape Up, p.79-81, p.148-149]

## Decision procedure
Main decision: for each step of the demo path, build real, fake, or cut, and in what order.

1. **Write the demo path (hour 0-1, 20 min).** 3-5 steps, 60-90 seconds, completable by a judge in under 2 minutes [Lean Startup, p.81-83]. Mark the one differentiator step. Everything off the path waits. [Seed: 0. Synthesis / Playbook, §1]
2. **Label each step Real, Fake, or Cut (10 min).**
   - Differentiator: Real, always. If it cannot be real by +12h, change the differentiator; do not fake it.
   - Depends on something gated, paid, slow, or flaky: Fake with the matching technique (recorded response, cached output, seeded data) and write its honest framing line now [Seed: A. Hackathon Kit, §A7].
   - Table stakes (auth, settings, admin, payments, sharing): hardcode or cut; seeded demo account; zero settings pages [Getting Real, p.57, p.87].
   - Over 2h and not the differentiator: find the 1-hour version or cut.
3. **Rabbit-hole pass (20 min).** Walk the path in slow motion: technical work we have never done? parts we assume fit together? a design answer we assume exists? [Shape Up, p.48-52]. Each unknown gets a spike (written question, pass criterion, 60-minute cap, owner) or a stub. Confirm keys, credits, and rate limits now [Make, p.116-120].
4. **Contract and owners (by +1:30).** One request/response/error JSON per route, the data model, and streams: P1 frontend, P2 backend/data, P3 AI/core, P4 integrator/pitch [Seed: A. Hackathon Kit, §A5-A6].
5. **Walking skeleton (+1:30 to +3:30).** Gate: the skeleton checklist below. **Stop rule:** not live on the public URL by +3:30 means all four stop feature work and fix deploy, falling back to the simplest host plus SQLite or JSON files [Seed: H. Hackathon-Specific Execution Advice, §H] [Make, p.90].
6. **Riskiest slice (+3:30 to +6).** Gate at +6h: the differentiator returns real output on real input inside the deployed app. If not, allow one alternative approach capped at 60 minutes; if that fails, zoom in on whatever part works and re-plan the demo around it.
7. **Demo-path slices (+6 to +12), one at a time.** Feature 2 starts only when feature 1 is demoable end to end [Seed: H. Hackathon-Specific Execution Advice, §H]. Tasks are 1-2 hours; anything not done in 2 hours is split or simplified [Getting Real, p.63]. P4 runs the full path on the deployed URL every 2 hours [Seed: A. Hackathon Kit, §A6]; owners report each slice as uphill or downhill and name the blocker for uphill [Shape Up, p.127-137]. Stuck 30 minutes: say it aloud, then swap approach, swap person, or mock it [Seed: 0. Synthesis / Playbook, §11].
8. **Midpoint (~+12h).** Does the full demo run start to finish on the deployed URL? Yes: start Should items and states. No: cut to the steps that run and fake or drop the rest now. Half the time gone with a third done means cut now, not at hour 22 [User Story Mapping, p.105-106].
9. **Freeze (~+18h).** No new features. Fix only P0 (crashes or blocks the demo path, loses data) and P1 (visible during the demo); ignore P2 [Getting Real, p.129]. Anything still uphill is cut and replaced by its fallback (cached data, recorded clip) [Shape Up, p.148-149].
10. **Harden and rehearse (+18 to +23).** Run the hardening checklist, tag `demo-v1`, record the backup video, do 5+ timed runs, submit with buffer [Seed: A. Hackathon Kit, §A2, §A11].

## Checklists
**Walking skeleton gate (before any feature work)** [Seed: A. Hackathon Kit, §A4]
- [ ] Page renders on the public URL, not localhost.
- [ ] One button calls one route that reads/writes one DB row or makes one LLM call with a fixed prompt, and the result shows on screen.
- [ ] Every external service the demo needs has received at least one real request [Seed: E. Walking Skeleton, §E].
- [ ] Env vars set in hosting; keys server-side only, never pasted into prompts.
- [ ] Every teammate can pull, run, and deploy; logs are visible somewhere you can check during judging.

**Real-vs-fake ledger (in the README; check before each test round and before judging)**
- [ ] Every faked step is listed with its technique and one-line honest framing [Seed: A. Hackathon Kit, §A7].
- [ ] The differentiator runs live on an input the team has never tried.
- [ ] Seed data is realistic, consistent across screens (same names, dates, numbers), free of real personal data, and matches the pitch story [Sprint, p.140, p.146-147] [Getting Real, p.100].
- [ ] Nothing in the pitch or Devpost text claims more than the live demo shows [Lean Startup, p.94-95].

**Hardening pass (post-freeze)** [Seed: A. Hackathon Kit, §A11]
- [ ] Demo path run 5+ times in a row on the deployed URL from the judging device and network.
- [ ] Demo mode works with the network off or the LLM key revoked; each API has a recorded response.
- [ ] Blank, loading, and error states on every demo screen, checked once as a brand-new user with an empty database [Getting Real, p.81-84].
- [ ] Console spam, debug buttons, lorem ipsum, and dead links removed.
- [ ] Known-good build tagged; backup recording saved locally and uploaded.

## Anti-patterns
- **Layer-cake build, big-bang integration.** Tell: at +6h frontend and backend each "work" but have never been joined. Fix: integrate a thin slice now; P4 runs the path every 2 hours. [Shape Up, p.103-104] [Seed: E. Walking Skeleton, §E]
- **Spike promoted to product.** Tell: a 30-minute experiment with hardcoded keys and no error handling now sits on the demo path. Fix: rewrite it as tracer code before building on it, or log it as a deliberate fake. [Seed: D. Tracer Bullets vs Prototypes, §D]
- **Faking the magic.** Tell: the core result is hardcoded and the team cannot run a judge's fresh input. Fix: make the differentiator real and fake its surroundings; if it cannot be real, change the claim. [Seed: A. Hackathon Kit, §A7]
- **Stack debate.** Tell: more than 10 minutes on framework choice, or someone learning a new framework for the core (a nearby team lost four hours of a 36-hour event to React vs Vue). Fix: the stack most of the team ships in; whoever writes most of the code decides; new tools only off the critical path or for a required sponsor SDK. [Seed: H. Hackathon-Specific Execution Advice, §H] [Make, p.88-94]
- **Mega-prompt agent edits.** Tell: one AI diff touches 15 files, or an agent loops on the same bug a second time. Fix: revert to the last commit, re-prompt one route or component at a time; after two loops read the error yourself, switch model, or simplify. [Seed: A. Hackathon Kit, §A8] [Seed: I. AI-Assisted Building (2026), §I]
- **Early pixel-pushing.** Tell: tuning spacing and colors at hour 6 while a demo step still has a gap. Fix: component-library defaults until freeze, then one polish block. [Getting Real, p.37] [Shape Up, p.107-111]
- **Infrastructure for problems you do not have.** Tell: queues, microservices, Kubernetes, a settings page, or an admin panel appear on the board. Fix: one deploy target, one DB, hardcoded defaults, seed scripts, and a one-line "what we'd change at 10x" answer. [Getting Real, p.39, p.41, p.57, p.87]
- **Localhost-only demo.** Tell: the path has only ever run on a dev laptop. Fix: run it on the deployed URL from the judging device with logs open. [Seed: A. Hackathon Kit, §A11] [Make, p.130]
- **"There's still time" feature.** Tell: new feature work starts after freeze. Fix: refuse; spend the hours on rehearsal, fallbacks, and the presenter's sleep. [Seed: H. Hackathon-Specific Execution Advice, §H] [Seed: A. Hackathon Kit, §A12]
- **Silent stuck.** Tell: a slice has been "almost done" or uphill across two check-ins. Fix: apply the 30-minute rule, name the unknown aloud, swap person or mock it. [Shape Up, p.127-137] [Seed: 0. Synthesis / Playbook, §11]

## Hackathon calibration
- **Judging shape sets the build.** About 4 minutes per judge, science-fair style, means one ~2-minute path that runs identically many times from a clean, resettable state, with a seeded account and no signup [Getting Real, p.102-103]. Reliability of one path beats breadth; MLH "completion" rewards a thin complete flow.
- **Technicality and complexity are scored.** Sprint's slide-deck facade [Sprint, p.144-145] and Levels' 30-minute no-code concierge [Make, p.103-115] suit pre-build user tests and roadmap screens only; the technical centerpiece must be real code. Match fidelity to audience: sketch for teammates, clickable mock for early outsiders, coded flow for judges [Lean UX, p.116-117].
- **Shrink every book's time unit.** Cockburn's skeleton (20 minutes to 2 weeks) becomes 1-2 hours [Seed: E. Walking Skeleton, §E]; Getting Real's 6-10 hour chunks become 1-2 hour tasks [Getting Real, p.63]; Shape Up's days of quiet orientation become 1-2 hours, then something clickable by +4-6h [Shape Up, p.100-101]; weekly test cadences become ~3 testers per round near +6h, +12h, +18h [Lean UX, p.128-132].
- **Ignore scale and production ceremony.** SQLite, in-memory structures, or JSON files are fine for 24 hours [Seed: H. Hackathon-Specific Execution Advice, §H] [User Story Mapping, p.96-97]; pre-rendering for traffic spikes is irrelevant at ~200 projects [Make, p.147-148]. Judges do not read commit history, test coverage, or docs, so one smoke run of the demo path replaces a test suite [Seed: H. Hackathon-Specific Execution Advice, §H]; the README still needs "what is real vs mocked" for Q&A.
- **Pretotyping runs beside the build, not before it.** Savoia would spend the first 1-3 hours on a demand test before real code [The Right It, p.29-31]. The skeleton is mostly idea-independent, so build it while P4 runs any demand test; a sign-up or fake-door count is viability evidence for the pitch, not a gate.
- **Energy is part of the build.** Sleep in shifts after the midpoint so someone always holds context, and protect the presenter's rest; bugs written at hour 20 get debugged at hour 23 [Seed: 0. Synthesis / Playbook, §12] [Seed: A. Hackathon Kit, §A12].

## Where experts disagree
- **Disposable vs kept.** Sprint says never build a prototype you cannot throw away [Sprint, p.134-135]; Hunt and Thomas and Cockburn treat early end-to-end code as production code that grows into the system [Seed: D. Tracer Bullets vs Prototypes, §D] [Seed: E. Walking Skeleton, §E]. Follow here: the demo path is kept tracer code; only spikes and pre-build test mocks are disposable. There is no second window to rewrite in.
- **Interface first vs risk first.** Getting Real designs screens before the backend [Getting Real, p.78-79] and Sprint solves the surface first [Sprint, p.26-27]; Shape Up and Ries push the scariest technical unknown first [Shape Up, p.139-141] [Lean Startup, p.100-101]. Follow here: both at once through the contract. P1 builds the epicenter result screen against the mock while P3 spikes the core, and the contract joins them.
- **Fake the hard tech vs build the novel core first.** Ries says refuse to solve the hard technical problem early and Wizard-of-Oz it [Lean Startup, p.88-91]; Singer says the first slice must be the novel part [Shape Up, p.111-112]. Follow Singer for the differentiator, because judges probe it and score technicality; follow Ries for every other hard step and for user tests that run before the real core lands.
- **How low quality may go.** Ries accepts a low-quality MVP when you do not yet know the customer [Lean Startup, p.91-93]; Levels insists "minimum" still means "minimum good" [Make, p.73-75] and Patton rejects "the crappiest thing you could ship" [User Story Mapping, p.81-82]. Follow Levels and Patton: judges score UI/UX, so the demo path and first screen look finished while off-path screens stay rough or hidden. Ries's allowance never covers defects that can crash the path [Lean Startup, p.93].
- **Slices vs streams.** Shape Up gives each person a whole slice (UI plus logic) and warns against layer roles [Shape Up, p.96-97]; the seed assigns frontend, backend, AI, and integrator streams [Seed: A. Hackathon Kit, §A6]. Follow the seed for four people, since few can own the full stack in 24 hours, but blunt Singer's risk with the hour-1 contract, a board organized by named slices rather than layers, and P4's end-to-end run every 2 hours.
- **Slides vs code for click-throughs.** Sprint defaults to Keynote and says it sufficed in nearly all of 100+ sprints [Sprint, p.144-145]; Klein warns slide prototypes become a maintenance sink [UX for Lean Startups, p.62]. Follow Klein: if a click-through is needed before building, make it in Figma or as plain HTML in the real repo so it can become tracer code.

## Go deeper
- search_experts("walking skeleton deploy day one touch every dependency", domain="14-rapid-prototyping")
- search_experts("tracer bullets versus throwaway prototype", domain="14-rapid-prototyping")
- search_experts("wizard of oz concierge fake the back end", domain="14-rapid-prototyping")
- search_experts("get one piece done core small novel first slice", domain="14-rapid-prototyping")
- search_experts("rabbit holes walk the use case in slow motion", domain="14-rapid-prototyping")
- search_experts("hard-coded versus live data prototype fidelity", domain="14-rapid-prototyping")
- search_experts("three state solution blank slate error state", domain="14-rapid-prototyping")
- search_experts("less software restate the problem cheaper version", domain="14-rapid-prototyping")
- search_experts("substitute cheap hack teleport instead of walking", domain="14-rapid-prototyping")
- search_experts("third-party API fallback recorded response", domain="14-rapid-prototyping")
