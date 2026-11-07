---
name: build-test
description: Load at hour 0-1 to label each demo step real, fake, or cut; at hour 1:30-6 for the walking skeleton and riskiest-slice gates; at hour 8-12 to build the AI eval set and run the first stranger test; whenever a step (hardware bridge, LLM parse, deploy) works only some of the time; and at freeze (hour ~18) to harden, drill failures, and pick the one number for the pitch.
---
# Decision guide: build-test

## Open this when
- **Hour 0-1:30:** the idea is locked and the team must turn it into a 3-5 step demo path, a JSON contract, and four parallel streams before feature code.
- **Hour 1:30-6:** the skeleton is not on a public URL yet, or the differentiator has not returned real output inside the deployed app.
- **Hour 8-14:** someone is tweaking a prompt, swapping a model, adding an agent step, or wants to put an accuracy number on a slide.
- **Any hour:** something works some of the time and someone wants to add a retry or record a video instead.
- **Hour 18-23:** freeze, bug triage, failure drills, and the final run that produces the pitch number.

## Steps
Hand the team the concrete result for their stack and hour (the fix, the test list, the exact fallback), not these steps. One citation per major call, only when it changes their mind.

1. **Hour 0-1: write the demo path and label it.** 3-5 steps, 60-90 s. Differentiator = Real, always. Gated, paid, slow, or flaky dependency = Fake (recorded response, cached output, seeded data) with an honest framing line. Auth, settings, admin = hardcode or cut. Any other step over 2h: find the 1-hour version or cut.
2. **Hour 1-1:30: contract and agent context.** One request/response/error JSON example per route; frontend builds against a local mock of it. Put stack, folder layout, conventions, and do-not-touch files in CLAUDE.md/AGENTS.md before anyone prompts an AI agent.
3. **Hour 1:30-3:30: walking skeleton.** Gate: one button on the public URL calls one route that makes one real call to every external service the demo needs (LLM, sponsor API, DB) and shows the result. Save each first real response as a fixture. **Stop rule:** not live by +3:30 means all four stop feature work and fix deploy, falling back to the simplest host plus SQLite or JSON files.
4. **Hour 3:30-6: riskiest slice.** Errors compound per AI step (10 steps at 95% is about 60%), so turn any agent into a fixed 2-4 call chain with code checks between calls, or precompute. Gate at +6h: real output on real input in the deployed app; if not, one alternative capped at 60 min, then re-plan around what works.
5. **Hour 6-12: one slice at a time.** Feature 2 starts only when feature 1 runs end to end. Every merge: 2-5 min running the demo path plus the changed feature, its neighbors, and its data. Stuck 30 min, or an AI agent loops on the same bug twice: revert to last commit, run the root-cause list below, then swap approach, person, or mock it.
6. **Hour 8-10: build the eval set before tuning.** 20-50 cases tagged by slice (Template B). Write the pass threshold before the first run. One command writes a CSV of input, output, pass/fail, note. Read every failing output and note its cause in one line before choosing any metric.
7. **Prompt and model gate.** Keep a change only if it gains 10+ points on the fixed set, or wins pairwise against the old output in both orders. Timebox tuning to about 45 min per feature. Use code assertions first; an LLM judge only for fuzzy criteria, binary, a different model family from the generator, checked against 20+ hand labels.
8. **Hour 9-10 and 18-19: stranger rounds.** 3 people not on the team, one silent facilitator, a goal not instructions. Go: a 5-second look at the first screen lets them say what it is and what to click; core task done unaided in under 1 min. Fix issues hit by 2 of 3 testers or rated blocking; ship the top 3 fixes before the next round. **Stop rule:** at hour 12 a stranger cannot finish the core path, so freeze new features until they can.
9. **Hour 12 midpoint.** Full path runs on the deployed URL: start states and polish items. No: cut to the steps that run, fake or drop the rest now.
10. **Hour 14-16: risk list in 10 min.** List what can crash, hang, or show a wrong number on stage, worst first. Run the failure drills in Template C in that order, each by someone other than the builder.
11. **Hour 18: freeze features, prompt, and model version.** Triage: demo blocker = all hands now; visible = fix only if under 20 min, else route the demo around it; minor = known-issues list. Cap debugging at 30 min per bug.
12. **Hour 18-22: harden.** Run the demo path 10 times from reset on the deployed URL from the judging laptop and network; more than 1 failure means run the root-cause list first, then remove that step or cache its result. Two different people run it independently. Final eval run on the tagged `demo-v1` build produces the only number allowed in the pitch.

## Debug the real failure first
Use when a step works some of the time (a hardware bridge at ~60%, an LLM parse that breaks 1 in 5, a route fine locally but not deployed). A fallback hides a bug you may fix in 20 minutes, and auto-retry only postpones the root cause [Winters et al., Software Engineering at Google, p.360].
1. **Measure it.** Run it 10-20 times, count failures, write the exact symptom and when it occurs (first call only, after replug, after idle). [Kaner, Bach & Pettichord, Lessons Learned in Software Testing, p.228-230]
2. **List the 3-5 most likely concrete causes for this stack,** most likely first, each with a 5-15 minute test that confirms or kills it. Change one thing at a time on the smallest setup that shows the bug. [Huyen, Designing ML Systems, p.193-194]
3. **Time box the whole hunt (60-90 min; 30 after freeze).** Fixed or not, then build the fallback, now as insurance rather than cover.

Starting lists (verify on the actual stack):
- **USB serial bridge (Arduino, ESP32):** opening the port toggles DTR and resets the board, so early bytes or the handshake are lost (wait for a "ready" line after open, or disable DTR before opening); port name changes after replug (`ttyUSB0` to `ttyUSB1`, COM3 to COM5: find it by VID/PID or serial number, reconnect in a loop); the port opened per request or by two processes (open once in one bridge process, broadcast over WebSocket or SSE); USB selective suspend or laptop sleep drops the device (disable it, stay on AC power, powered hub); baud mismatch or partial lines (newline-framed messages, readline with timeout, drop malformed lines).
- **LLM structured output:** preamble or code fences around JSON, truncation at max tokens, a field the schema allows but the code does not, 429 rate limit, timeout with no cap.
- **Works locally, not deployed:** env var missing at build vs runtime, CORS origin, HTTPS page calling HTTP or `ws://`, cold start past the client timeout, dev DB URL in prod.
- **Venue Wi-Fi:** captive portal, blocked WebSocket or non-443 ports, DNS; test on a phone hotspot to split network from code.

## Template
Copy into the README or team channel at hour 0 and keep it current.

```
A. DEMO PATH LEDGER (check before each test round and before judging)
Step | What judge sees            | Real/Fake/Cut | Fake technique  | Honest framing line        | Owner | Live latency
1    | ______                     | ____          | ______          | ______                     | __    | __ s
2*   | ______ (* = differentiator)| REAL          | n/a             | n/a                        | __    | __ s
3    | ______                     | ____          | ______          | ______                     | __    | __ s
Rule: any live step that can exceed ~10 s is precomputed or cached. Press state <0.1 s, staged text >1 s.

B. EVAL SET (eval.csv: id, slice, input, expected/criterion, output, pass, note)
Slice              | Count | Pass  | Top failure cause       | Fix / mitigation
typical            | 10-20 | __/__ | ______                  | ______
messy / typo       | 5     | __/__ | ______                  | ______
off-topic/hostile  | 5+    | __/__ | (must decline cleanly)  | ______
false premise      | 5     | __/__ | ______                  | ______
answer not present | 3-5   | __/__ | (must say "unknown")    | ______
Threshold (set before run 1): ____   Baseline (zero-rule / heuristic / manual): ____
Pitch line: "__ of __ passed (about __-__%), vs __ for [baseline], preliminary; worst slice: __, mitigated by __."

C. FAILURE DRILLS (pass = UI shows a message or cached fallback, never blank or a stack trace)
[ ] LLM/API: timeout, 429, 500, empty body, malformed JSON
[ ] Key revoked or Wi-Fi physically off (night before) -> DEMO_MODE serves recorded responses and local data
[ ] Hardware: unplug and replug, restart the bridge, laptop sleep -> reconnects without a page reload; simulator switch works
[ ] Input: empty, 10,000 chars, emoji, quotes, non-English, pasted multiline, double-submit
[ ] Async: refresh mid-call, navigate away, second request in flight, wait past timeout
[ ] "Ignore previous instructions" pasted into the main input and into any retrieved doc
[ ] Fresh incognito + empty DB: blank state has headline, one line, one action
[ ] Console, network tab, server logs clean during a full run
[ ] Reset script returns demo state; rerun before each judge
```

## Principles
1. **Deploy a walking skeleton touching every external dependency early (counterintuitive).** One real round trip flushes env-var, CORS, key, and deploy failures while they cost minutes. [Seed: E. Walking Skeleton, §E]
2. **Mock the plumbing, never the magic.** Judges probe the differentiator with fresh input and score technicality on it. [Seed: A. Hackathon Kit, §A7]
3. **Use the simplest AI pattern that works; agents lose demos (counterintuitive).** Errors multiply per step. [Huyen, AI Engineering, p.539]
4. **Give the system a way out: "unknown", "not in sources", out-of-scope.** Judges type off-script, retrieval always returns something, and classifiers label junk confidently; an explicit null and a similarity cutoff turn a judge's trick input into a feature moment. [Alammar, Hands-On LLMs, p.328-329] [Christian, The Alignment Problem, p.277-281]
5. **Small evals only detect big differences, so gate changes at 10+ points.** A 30-point gap needs about 10 cases and a 10-point gap about 100; with 30-50 cases, "it seems better" after a prompt tweak is noise. [Huyen, AI Engineering, p.405-407] [Lakshmanan, Generative AI Design Patterns, p.424-425]
6. **Read failing outputs before choosing metrics.** Generic scores rarely track your real failures; one-line notes on each failing trace, grouped and counted, show the top 1-3 fixes, often trivial ones like injecting today's date. [Seed: C. Evals and Error Analysis, §C] [Huyen, AI Engineering, p.259-264]
7. **Report "X of Y" with a range and a trivial baseline, never a bare percentage.** 34/40 is really about 70-93%, and 94.5% accuracy once coexisted with 30% recall; a number without a zero-rule or manual comparison invites the first hard question. [Seed: 0. Synthesis / Playbook, §0.8] [Huyen, Designing ML Systems, p.201-205] [Lakshmanan, ML Design Patterns, p.157-159, p.401-406]
8. **The builder is the worst tester of their own feature.** Builders try the inputs they expect; "done" means it ran on the demo laptop, with demo data, from a clean start, driven by someone else. [Kaner, Bach & Pettichord, Lessons Learned in Software Testing, p.70-71, 74-75]
9. **Inject the failure of every external dependency before the venue does.** Timeout, rate limit, 500, and malformed responses are the common judging-time breaks; confirm each degrades to a message or cached fallback. [Winters et al., Software Engineering at Google, p.367] [Make, p.121]
10. **Staged progress, not a spinner: 0.1 s acknowledge, 1 s live status, 10 s live maximum.** Without feedback people double-submit; named stages make AI work visible. [About Face, p.295-296]
11. **Drive AI coding agents with one bounded task per prompt and a commit before each large edit.** Mega-prompts overshoot scope and plant timebombs; after two loops on one bug, read the error yourself, switch model, or simplify. [Seed: A. Hackathon Kit, §A8] [Seed: I. AI-Assisted Building (2026), §I]
12. **Hard-code test expectations computed outside the code.** AI-written tests often re-derive the answer with the production formula, so they can never fail; use literals from a hand calculation. [Khorikov, Unit Testing Principles, p.264-266]

## Mistakes
- **Layer-cake build.** Tell: at +6h frontend and backend each "work" but have never been joined. -> Integrate a thin slice now; the integrator runs the full path on the deployed URL every 2 hours.
- **Vibe-check prompt iteration.** Tell: "I tweaked the prompt, it seems better." -> Prompts in versioned files; rerun the fixed eval set by script; keep only 10+ point gains.
- **Ranking versions by absolute LLM-judge score.** Tell: "v2 scored 0.90, v1 0.89," judged by the same model family. -> Binary pass/fail, pairwise in both orders, different family; judges favor their own family by up to +25%, the first option, and longer answers. [Seed: D. LLM-as-a-Judge, §D]
- **A result that looks amazing.** Tell: 100% on the eval or a huge speedup on the first try. -> Twyman's law: replay one raw log line and check the test set was never used for tuning. [Kohavi, Trustworthy Online Controlled Experiments, p.82-83]
- **Fallback over an undiagnosed bug.** Tell: "it works 60% of the time, add a retry and record a video." -> Run the root-cause list above first; the fallback ships either way.
- **Free-form model text parsed by code.** Tell: the demo breaks when the model adds a preamble. -> Schema or JSON mode, validate, retry up to 2 times with the parser error appended; that pushes a >90% call below 1% failure. [Alammar, Hands-On LLMs, p.270-273]
- **Late model swap.** Tell: "the new version" or a sponsor model goes in at hour 20. -> Rerun the fixed set on both; swap only if it wins; keep `demo-v1` deployable. [Lakshmanan, ML Design Patterns, p.290-292]

## Hackathon calibration
- **No test suite, one smoke run.** Judges do not read coverage or commit history. One scripted demo-path smoke, a few output tests on the one real logic function, and one test per seam between teammates' code; stop automated tests at about 10-15% of team time. [Crispin & Gregory, Agile Testing, p.329-330]
- **Eval size shrinks, honesty does not.** The books' ~300 examples for a trustworthy absolute score become 20-50 with a stated range and a slice table. [Huyen, AI Engineering, p.405-407]
- **Usability: 3 per round, two rounds,** not 5 or more, because fix capacity is the limit; report counts, never percentages. [Krug, Rocket Surgery Made Easy, p.35-36]
- **Skip:** A/B tests, fine-tuning, drift monitoring, coverage targets, bug trackers. A shared "steps / expected / actual / blocker?" channel replaces the tracker. [Seed: Hackathon Kit, §A9]

## Go deeper
- [../domains/14-rapid-prototyping.md](../domains/14-rapid-prototyping.md): real/fake/cut, skeleton gate, contract-first parallel work, AI agent discipline.
- [../domains/17-testing-validation.md](../domains/17-testing-validation.md): smoke tests, risk list, exploratory charters, evidence-claim checklist.
- [../domains/15-ai-app-design-eval.md](../domains/15-ai-app-design-eval.md): pattern choice, eval set design, LLM judges, guardrails, trust UX.
- search_experts("walking skeleton deploy day one touch every dependency", domain="14-rapid-prototyping")
- search_experts("compound error agent step count reliability", domain="15-ai-app-design-eval")
- search_experts("eval set size difference to detect bootstrap", domain="15-ai-app-design-eval")
- search_experts("interference testing interrupt cancel timeout async", domain="17-testing-validation")
- search_experts("third-party API fallback recorded response", domain="14-rapid-prototyping")
- search_experts("stub or emulate flaky dependencies simulator", domain="17-testing-validation")
