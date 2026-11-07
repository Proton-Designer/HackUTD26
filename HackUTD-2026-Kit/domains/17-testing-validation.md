---
name: 17-testing-validation
description: Open when deciding what to test and when across the 24h build (hour-0 deploy setup, the hour-6 thin slice, each merge, feature freeze, the pre-judging hardening block), when planning a hallway usability round or before/after timing test, or before putting any number, percentage, or "we validated" claim on a slide or in a judge answer.
---
# Testing and experimental validation

## Use this when
- Hour 0-2: setting up the repo and deciding which checks to automate (auto-deploy, smoke test, one test runner) and writing Test Cards for the riskiest assumptions.
- Hour 8-10 and 18-20: running a 3-person hallway usability round on whatever exists, and turning findings into a top-3 fix list.
- Hour 14-22: choosing where scarce testing minutes go (risk list, exploratory charters, failure drills) and triaging bugs after feature freeze.
- Any time the team wants to claim impact: "saves X minutes", "N of M users succeeded", "more accurate than ChatGPT". Check the design supports the claim.
- When a judge asks "how do you know it works?", "did you test this?", or "how would you validate this at scale?"

## Core principles
1. **Test what the judges will see, and gate every deploy on it.** One scripted smoke test of the 3-5 step demo path, run before and after every deploy, beats a large unit suite on code no one sees; a smoke failure means stop and fix, not test deeper. [Seed: Synthesis / Playbook, §0]; [Winters et al., Software Engineering at Google, p.366]; [Kaner, Bach & Pettichord, Lessons Learned in Software Testing, p.347, 351]
2. **Fix the pass/fail number before you run any test.** Write hypothesis, test, metric, and a numeric criterion ("at least 5 of 6 finish in under 30s") first, so weak results cannot be rationalized afterward. [Bland, Testing Business Ideas, p.61-62]; [Kohavi, Trustworthy Online Controlled Experiments, p.70, 78-79]
3. **Watch behavior; ignore opinions and ratings.** (counterintuitive) Hand over the laptop and a task instead of asking "do you like it?"; people who nearly gave up still rate it high, and "I would use it" is weak evidence next to a completed task or a signup with a real email. [Krug, Rocket Surgery Made Easy, p.24, 95-96]; [Bland, Testing Business Ideas, p.68]
4. **Small samples find problems; they do not prove effects.** (counterintuitive) Three people per round, then fix, then three more, beats one big round; report counts ("4 of 5") and call no-difference results "inconclusive", never "80% of users". [Krug, Rocket Surgery Made Easy, p.25, 35-36]; [Kohavi, Trustworthy Online Controlled Experiments, p.85]; [Seed: How Many Users, §G]
5. **A result that looks amazing is probably a bug (Twyman's law).** Before quoting an impressive number, replay one raw session or log line; a 28% click jump once turned out to be confused users clicking repeatedly. [Kohavi, Trustworthy Online Controlled Experiments, p.82-83, 103]
6. **Tests are a liability; admit only high-value ones.** (counterintuitive) Pull the one piece of real logic (scoring, parsing, matching) into a pure function, test it with output assertions, skip trivial and glue code; a few robust tests beat many brittle ones that break on every refactor. [Khorikov, Unit Testing Principles, p.102, 153-154]; [Winters et al., Software Engineering at Google, p.370-371]
7. **Hard-code expected values computed outside the code.** A test that re-derives the answer with the production formula can never fail; AI-written tests often do exactly this, so replace computed expectations with literals from a hand calculation or spreadsheet. [Khorikov, Unit Testing Principles, p.264-266]; [Winters et al., Software Engineering at Google, p.403-405]
8. **Inject the failure of every external dependency before the venue does it for you.** For each API, model, DB, and auth: timeout, rate limit, 500, empty or malformed response; confirm the UI degrades to a message or cached fallback. [Winters et al., Software Engineering at Google, p.367]; [Kaner, Bach & Pettichord, Lessons Learned in Software Testing, p.348]
9. **Diverse half-measures beat one exhaustive technique.** Run each kind of testing until its find rate drops, then switch (demo walkthrough, bad-input pass, fresh-user pass, other device, AI spot check); big escapes come from a whole category never tried. [Kaner, Bach & Pettichord, Lessons Learned in Software Testing, p.342-343]
10. **The builder is the worst tester of their own feature.** Builders test the visible path with inputs they expect; have someone else (ideally an outsider) try to break it, and let the least-attached teammate facilitate user sessions. [Kaner, Bach & Pettichord, Lessons Learned in Software Testing, p.74-75]; [Krug, Rocket Surgery Made Easy, p.89-90]
11. **A flaky test is worse than no test.** Around 1% flakiness erodes trust; once "just rerun it" starts, red stops meaning anything. Quarantine any test that fails once without a code change. [Winters et al., Software Engineering at Google, p.360]
12. **Never say "verified"; say what you tried and what you did not.** Testing can show failure but not prove correctness; a scoped answer ("demo path, 12 bad inputs, 30 real samples; not tested at load") reads as maturity. [Kaner, Bach & Pettichord, Lessons Learned in Software Testing, p.50, 71]

## Decision procedure
Main decision: what to test or validate now, and when to stop.

1. **Hour 0-2, plumbing first.** Wire auto-deploy from main and one smoke command before any feature test; it has the best return of any automation. [Crispin & Gregory, Agile Testing, p.321] Pick one test runner per language and put the command in the README. [Winters et al., Software Engineering at Google, p.416]
2. **Hour 0-2, pick what to validate.** Write 8-10 assumptions, plot importance vs evidence, keep the top 1-2 that are critical and evidence-free. [Bland, Testing Business Ideas, p.52-55] Order: desirability, then feasibility, then viability (viability gets one line). [Bland, Testing Business Ideas, p.48-51] Write a Test Card for each with a numeric criterion.
3. **Feasibility spike: 30-90 minutes, hard stop by hour 3-4.** Write acceptance criteria first. Fails criteria: swap the component or fake it (Wizard of Oz) and plan to disclose that in Q&A. [Bland, Testing Business Ideas, p.285-286, 306-308] Make one real call to each sponsor API in the first 2-3 hours and save the response as a fixture and demo fallback. [Crispin & Gregory, Agile Testing, p.382-384]
4. **By hour 6, one thin slice through every layer**, even with hard-coded data. Hours 0-10 run only smoke and "does each function work once" checks; do not throw harsh tests at an immature build. [Crispin & Gregory, Agile Testing, p.378-379]; [Kaner, Bach & Pettichord, Lessons Learned in Software Testing, p.345-348]
5. **Hour 8-10, usability round 1 (3 people, 10-15 min each).** Debrief within an hour with observers only; each names their top 3; fix the top 3 with the smallest change that stops the observed problem. [Krug, Rocket Surgery Made Easy, p.111-114, 118-121]
6. **Hour 8 checkpoint: persevere, pivot, or kill.** No positive signal on the core hypothesis after several quick tests: pivot now. A pivot at hour 8 is feasible; after hour 14 it usually is not. [Bland, Testing Business Ideas, p.61-63]; [Kohavi, Trustworthy Online Controlled Experiments, p.58-59]
7. **Every merge: 2-5 minutes** running the demo path plus the changed feature, its neighbors, and its data. Do not batch merges. [Kaner, Bach & Pettichord, Lessons Learned in Software Testing, p.351]; [Kaner & Johnson, LAWST Styles of Exploration, p.10]
8. **Hour 14-16, risk list in 10 minutes.** Score each failure mode impact 1-5 times likelihood 1-5; anything that can crash or show a wrong number on stage is impact 5; test from the top down. [Crispin & Gregory, Agile Testing, p.407-409] Flag new-to-team tech, last-minute changes, and third-party parts first. [Kaner, Bach & Pettichord, Lessons Learned in Software Testing, p.117-119]
9. **Hour 14-20, chartered exploratory sessions**, 20-30 min, one per person, "Explore <area> with <inputs> to discover <problem>", different person than the builder. 15-minute pass on a shaky component forces keep, fix, or cut; cut anything seriously broken that is off the demo path. [Kaner & Johnson, LAWST Styles of Exploration, p.3]; [Seed: Hackathon Kit, §A3]
10. **Hour 18-19, feature freeze.** After it, triage: demo-blocker = fix now, all hands; visible = fix if under 20 min, else route the demo around it; minor = known-issues list. [Seed: Hackathon Kit, §A5]; [Crispin & Gregory, Agile Testing, p.455-456] Cap debugging at 30 minutes per bug, then cut or work around. [Kaner & Johnson, LAWST Styles of Exploration, p.42]
11. **Hour 18-20, usability round 2** on the near-final build; also the timed before/after test if you will claim time savings (step 13).
12. **Last 2 hours: meticulous only.** No new features; verify the deployed version equals the tested commit; pair run-through on the exact demo machine, browser, and network; run every failure drill. [Kaner, Bach & Pettichord, Lessons Learned in Software Testing, p.346]
13. **Choosing a validation design for a claim:**
    - "Easier to use": 3-5 person usability rounds, report completions and what you changed.
    - "Faster than today": within-subjects timing, 5-8 screened users, half do old way first; report each person's two times, median difference, and range. [Seed: Hackathon Kit, §A7-A8]
    - "Better output": side-by-side with hidden labels and randomized order, or the same 20-50 inputs through your system and the obvious baseline with the same checker. [Seed: Hackathon Kit, §A7]
    - "People want it": fake-door or signup at the event, reported as "N of M visitors", never "demand validated".
    - Real A/B test: no. A 10% to 12% conversion lift needs about 3,800 users per arm. [Seed: Hackathon Kit, §A9]

**Stop rules:** stop a usability round when you have more problems than you can fix in the next 1-2 hours. [Krug, Rocket Surgery Made Easy, p.35-36] Stop an exploratory technique when it stops finding bugs. Stop writing automated tests at about 10-15% of team time. [Crispin & Gregory, Agile Testing, p.329-330]

## Checklists
**A. Demo-readiness (run twice before judging)**
- [ ] Smoke test passes against the deployed URL in under 2-3 minutes; fast local suite under about 30s. [Winters et al., Software Engineering at Google, p.371-372]
- [ ] Startup check fails loudly if env vars or API keys are missing. [Khorikov, Unit Testing Principles, p.210-212]
- [ ] Wi-Fi off, API key revoked or 500, Slow 3G, fresh incognito, phone, 1920x1080 projector, offline backup video all checked. [Seed: Hackathon Kit, §A4]
- [ ] Main input survives empty, 10,000 chars, emoji, quotes, non-English, pasted multiline, double-submit. [Kaner & Johnson, LAWST Styles of Exploration, p.15]
- [ ] Key async flow survives navigate-away, refresh, cancel, second request mid-flight, and waiting past the timeout. [Kaner & Johnson, LAWST Styles of Exploration, p.32-38]
- [ ] Console, network tab, and server logs clean during a full run, even if the UI looks fine. [Kaner & Johnson, LAWST Styles of Exploration, p.3]
- [ ] Seed/reset script returns the DB to the demo state; rerun before each judge. [Krug, Rocket Surgery Made Easy, p.79-80]
- [ ] Two different people ran the full demo path independently. [Kaner, Bach & Pettichord, Lessons Learned in Software Testing, p.349]

**B. Evidence claims (every number on a slide or in Q&A)**
- [ ] Criterion was written before the test (Test Card exists).
- [ ] n, exact task, and who participants were are stated; counts, not percentages, under about 20 people. [Seed: Hackathon Kit, §A10]
- [ ] Denominator is people who reached the step, including those who quit. [Kohavi, Trustworthy Online Controlled Experiments, p.67, 93]
- [ ] Surprising result double-checked against raw data.
- [ ] Claim matches design: usability is not demand, preference is not accuracy, signups are not revenue, correlation is not cause. [Kohavi, Trustworthy Online Controlled Experiments, p.33]
- [ ] Simulated or Wizard-of-Oz parts are disclosed; one-sentence limitation ready.

**C. User session (10-15 min)**
- [ ] Screened with one qualifying question if the claim is about target users. [Bland, Testing Business Ideas, p.111]
- [ ] Same 30-second intro: testing the app not you, think aloud, I can't help while you try. [Krug, Rocket Surgery Made Easy, p.80-81]
- [ ] First-screen check: can they say what it is and who it is for? [Krug, Rocket Surgery Made Easy, p.126-129]
- [ ] Tasks written in goal language with no button labels; about 3 minutes cap each. [Krug, Rocket Surgery Made Easy, p.65, 84-85]
- [ ] Facilitator answers questions with "What do you think?"; builder observes silently.
- [ ] Close with "What did you expect when you clicked X?" and "What was most confusing?"

## Anti-patterns
- **Ice cream cone suite.** Tell: "just a Playwright script for everything". Fix: exactly one E2E smoke on the demo path; the rest in pure-logic and seam tests. [Winters et al., Software Engineering at Google, p.364]
- **Coverage target.** Tell: someone wants 80% or a badge. Fix: no target; use coverage once to find unexercised branches in core logic; break the code (flip an operator) to confirm a test goes red. [Kaner, Bach & Pettichord, Lessons Learned in Software Testing, p.91]; [Crispin & Gregory, Agile Testing, p.361-364]
- **Test counts as quality.** Tell: "47 tests, 90% passing" in the README or pitch. Fix: "38 of 40 sample inputs correct" or "tests across the 3 failure modes we feared most". [Kaner, Bach & Pettichord, Lessons Learned in Software Testing, p.340-341]
- **Mocking your own internals or DB.** Tell: `verify()` on a stub, partial mocks, SQLite in tests when prod is Postgres. Fix: mock only the boundary others observe (LLM, payment, email); assert outputs; test on the same DB engine or skip integration tests. [Khorikov, Unit Testing Principles, p.96-97, 110-111, 246]
- **Satisfaction quotes as evidence.** Tell: "testers rated it 9/10" on a slide. Fix: cite what they accomplished and what you changed. [Krug, Rocket Surgery Made Easy, p.95-96]
- **Peeking and stopping early.** Tell: testing until the numbers look good, or slicing results until something wins. Fix: fix the participant count and one primary metric in advance; label other slices exploratory. [Kohavi, Trustworthy Online Controlled Experiments, p.88-89]
- **Hand-picked comparison groups.** Tell: friends try the new version, strangers the old. Fix: alternate by arrival order or coin flip and counterbalance order. [Kohavi, Trustworthy Online Controlled Experiments, p.31-32]
- **"It works" from the author.** Tell: a teammate's click-through on their own laptop. Fix: done means it ran on the demo laptop, demo data, clean start, by someone else. [Kaner, Bach & Pettichord, Lessons Learned in Software Testing, p.70-71]
- **Fake door on the demo path or collecting real payment.** Tell: a 404 button judges might click, or a real card form. Fix: fake doors on side pages only, honest "not ready yet" message, no payment data. [Bland, Testing Business Ideas, p.86-87, 160-161]

## Hackathon calibration
- **Compress session lengths, keep the structure.** SBTM sessions of 60-90 minutes become 20-30 [Seed: Exploratory Testing, §D]; Krug's 50-minute session becomes 10-15 with the same order (intro, first screen, tasks, probe) [Krug, Rocket Surgery Made Easy, p.80-88]; Bland's 15-20 interviews become 5-8 [Bland, Testing Business Ideas, p.111-113]; a 10-minute push-triggered suite becomes 2-3 minutes [Crispin & Gregory, Agile Testing, p.321].
- **Ignore the statistics machinery of A/B testing, keep its habits.** SRM checks, power analysis, novelty-effect windows, and one-week minimums cannot apply to 5-20 people in one day. Keep pre-stated criteria, guardrails, Twyman's law, and correct denominators. Use OEC, guardrail, MDE, and SRM as vocabulary only when a judge asks how you would validate at scale. [Seed: Trustworthy Online Controlled Experiments, §E]
- **Ignore long-horizon evidence channels.** Paid ads (1-3 day approval), funnel analytics (weeks of traffic), and fake doors run for days need traffic you will not have; substitute posting the link in 3-5 targeted campus channels and counting. [Bland, Testing Business Ideas, p.130-132, 146-150]
- **Judges give about 4 minutes and probe numbers.** One defensible number with n stated beats three impressive ones. HackUTD criteria name usefulness and impact; a "What we tested this weekend" Learning Card slide is how validation earns credit there. Whether judges weight validation explicitly is unconfirmed. [Seed: Gaps and Books, §H]; [Seed: Testing Business Ideas, §F]
- **The venue is a free recruiting pool.** Other hackers, volunteers, and sponsor reps work for general usability; for value claims, add at least one person from the real target group or a sponsor rep who knows the domain. [Krug, Rocket Surgery Made Easy, p.53-58]
- **Two fixed test slots on the timeline.** Put them on the schedule now (for example hour 9 and hour 19) and test whatever exists then; deciding "when" is how testing gets skipped. [Krug, Rocket Surgery Made Easy, p.36-39]
- **Drop production-scale process:** migration history, parallel test infra, coverage dashboards, bug trackers. A shared "steps / expected / actual / blocker?" channel replaces the tracker. [Kaner, Bach & Pettichord, Lessons Learned in Software Testing, p.228-230]

## Where experts disagree
- **Test shape: pyramid vs trophy.** Google suggests about 80/15/5 unit/integration/E2E and Crispin says test at the lowest layer that catches the bug [Winters et al., Software Engineering at Google, p.363-365]; [Crispin & Gregory, Agile Testing, p.316-318]. The Dodds trophy says mostly integration, because tests that resemble real use give more confidence per test [Seed: Testing Trophy, §B]. Khorikov splits it: unit tests for edge cases, one integration test for the longest happy path [Khorikov, Unit Testing Principles, p.187, 210]. **Follow Khorikov here:** static checks everywhere, a handful of output tests on the one or two logic functions, one test per seam between teammates' code, one E2E smoke. Hackathon code churns too fast for broad unit suites, and the judged artifact is the integrated demo.
- **How many users.** Nielsen: 5 find about 85% of problems [Seed: How Many Users, §G]; Faulkner and Atlassian: 5 can miss a lot, and the 85% figure holds only when each user finds about 31% of problems. Krug: 3 per round, more rounds [Krug, Rocket Surgery Made Easy, p.35-36]. **Follow Krug:** 3 per round, two rounds, because the limit is fix capacity, not discovery, and no sample this size supports a percentage.
- **Who to recruit.** Krug: almost anyone reveals the common problems [Krug, Rocket Surgery Made Easy, p.53-55]. Bland: pick a narrow segment and screen [Bland, Testing Business Ideas, p.108, 111]. **Follow both, by claim type:** anyone for usability; screened target users for any desirability, time-saving, or value claim.
- **Script flexibility.** Krug lets you change tasks between participants because you are not proving anything [Krug, Rocket Surgery Made Easy, p.25]; Bland requires identical subject, context, and script for comparable results [Bland, Testing Business Ideas, p.61]. **Follow Krug for find-and-fix rounds, Bland for any timed or before/after test you will quote.**
- **Before/after comparisons.** Kohavi warns before/after is confounded by time and wants variants run concurrently [Kohavi, Trustworthy Online Controlled Experiments, p.73]; the seed recommends within-subjects before/after [Seed: Hackathon Kit, §A8]. **Follow the seed with counterbalancing:** each person does both conditions in the same sitting, half in each order, which removes the time confound Kohavi worries about.
- **Test databases.** Crispin: logic tests in memory with fakes [Crispin & Gregory, Agile Testing, p.306]; Google: an in-memory or temp DB beats mocking the ORM [Winters et al., Software Engineering at Google, p.392-394]; Khorikov: never substitute a different engine [Khorikov, Unit Testing Principles, p.246]. **Follow Khorikov for integration tests** (same engine as deploy), and keep logic pure so it needs no DB.
- **Flags in production code.** Crispin endorses feature switches to keep unfinished work off the stable path [Crispin & Gregory, Agile Testing, p.384, 501]; Khorikov forbids `isTest` branches [Khorikov, Unit Testing Principles, p.266-268]. **Both hold:** a query-string or env flag for experimental demo features is fine; for tests, swap behavior through one injection seam, not scattered test checks.
- **Scripted vs exploratory.** Kaner prefers exploration over scripts [Kaner, Bach & Pettichord, Lessons Learned in Software Testing, p.64-65]; Google automates well-understood behavior and pins exploratory finds as regression tests [Winters et al., Software Engineering at Google, p.378-379]. **Do both:** automate only the demo-path smoke; explore everything else; add a test only for a demo-relevant bug you can reproduce in under a minute.

## Go deeper
- search_experts("demo path smoke test run after every deploy", domain="17-testing-validation")
- search_experts("test card success criterion set before testing", domain="17-testing-validation")
- search_experts("assumptions mapping importance versus evidence riskiest assumption", domain="17-testing-validation")
- search_experts("three users per round debrief fix top problems", domain="17-testing-validation")
- search_experts("Twyman's law sanity checks surprising result", domain="17-testing-validation")
- search_experts("hard-coded expected values tautology tests mocks", domain="17-testing-validation")
- search_experts("interference testing interrupt cancel timeout async", domain="17-testing-validation")
- search_experts("evidence strength say versus do commitment", domain="17-testing-validation")
- search_experts("how do you know it works report what was not tested", domain="17-testing-validation")
