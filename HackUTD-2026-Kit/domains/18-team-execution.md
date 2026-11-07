---
name: 18-team-execution
description: Open at the hour-0 kickoff (roles, Decider, timeline), when sizing scope against real capacity, at each checkpoint (H6, H12, H18, H22) to decide continue/cut/mock/pivot, when a teammate is stuck or two teammates deadlock, when someone offers to "just jump in" late, at the overnight low, and when setting feature freeze, demo freeze, test slots, and rehearsal time.
---
# Team execution and time management under pressure
> Built from cross-domain links; thinner sourcing than other domains.

## Use this when
- Hour 0-1: writing the team agreement (owners, Decider, tie-break rule, stuck rule, sleep plan) and the hour-by-hour plan before anyone codes.
- Turning the feature list into a cut line: deciding how much fits in the real build hours of four tired people.
- A scheduled checkpoint (H6, H12, H18, H22) where the team must decide continue, cut, mock, or pivot from evidence rather than mood.
- Someone has been stuck on a bug for 30+ minutes, or two teammates are arguing about scope or architecture.
- Hour 14-20: the core path is shaky, the deadline is fixed, and someone proposes a heroic rescue or a new feature.
- Setting freeze times, test slots, rehearsal blocks, and booth roles for science-fair judging.

## Core principles
1. **Plan on about 10-12 real build hours per person, then commit to roughly half the features you think fit (counterintuitive).** Only about half of clock time is build-and-debug, and plans are near best case, so a "24h x 4 people" plan overruns by default. [Brooks, Mythical Man-Month, p.109]; [Kahneman, Thinking Fast and Slow, p.242-243]; pad anything touching a new API, model, or deploy path by 1.5-2x [Brooks, Mythical Man-Month, p.33-34]
2. **Shape the 24 hours around integration and testing, not coding.** Brooks's split is 1/3 plan, 1/6 code, 1/2 test; compressed, that is about 3-4h plan/spec, 5-6h happy path, 8-10h integration, fixing, and rehearsal. Do not plan 20 hours of feature coding. [Brooks, Mythical Man-Month, p.37]; the 60-to-100 last mile is the brutal part for AI demos [Huyen, AI Engineering, p.86-87]
3. **Integrate a thin end-to-end slice by H6-8, then merge at least hourly.** Integration cost grows with time apart and always overflows when left to the end; unit tests passing proves nothing about the seams. [Martin, Clean Architecture, p.129-130]; [Khorikov, Unit Testing, p.185, 190]
4. **Cut formally at fixed checkpoints; never let scope get trimmed silently.** With a fixed deadline, slippage otherwise turns into untracked shortcuts and skipped testing. Write the cut, agree it, re-plan the demo path. Signal to watch: half the time spent but a third done. [Brooks, Mythical Man-Month, p.40-41]; [Patton, User Story Mapping, p.105-106]; [Crispin and Gregory, Agile Testing, p.380-382]
5. **Protect one coherent demo flow and cut everything around it, but never amputate the flow itself.** If a piece can be cut without harm it was not part of the minimal product; the MVP is the one flow a judge completes end to end in under 2 minutes. [Cagan, Inspired, p.137-139]; [Ries, Lean Startup, p.81-83]; use the core claim as a 10-second veto question on every new feature [Heath, Made to Stick, p.33-34]
6. **When losing late, take the sure small loss (mock or record the broken part), not the long-shot rescue (counterintuitive).** Facing sure losses, people turn risk-seeking and convert manageable failures into disasters. [Kahneman, Thinking Fast and Slow, p.310]; judge stuck work only on future cost: "if we had not spent the last N hours, would we start this now?" [Kahneman, Thinking Fast and Slow, p.335, 337]
7. **Lock irreversible decisions (scope, architecture, story) before about H10 while rested; after H16 follow the written plan.** Fatigue pushes toward quick fixes and makes people accept false claims, and the decider cannot feel it happening. [Kahneman et al., Noise, p.82]; [Kahneman, Thinking Fast and Slow, p.80-81, p.43-45]
8. **Name one Decider and collect votes privately before anyone speaks.** Consensus voting yields compromise and absent deciders relitigate later; once the first voice is heard, independent judgment collapses into a cascade. [Knapp, Sprint, p.28-29, p.111-114]; [Kahneman et al., Noise, p.91-93]
9. **Run a 5-minute noise audit before writing code (counterintuitive).** Each person privately writes the one-line pitch, the target user, and a 0-100 score; teams that feel aligned typically are not. A spread over about 25 points or different users means stop and resolve. [Kahneman et al., Noise, p.28-29, 32-33]
10. **Hand each person a whole slice plus 2-3 written contracts and mocks, not layers or a relay.** Layer splits need heavy communication per feature, handoff chains water the idea down, and mocked step interfaces let people build in parallel and double as demo fallbacks. [Singer, Shape Up, p.96-97]; [Richards and Ford, Fundamentals of Software Architecture 2e, p.321]; [Lakshmanan et al., Generative AI Design Patterns, p.445-448]; [Johnson, Where Good Ideas Come From, p.128-129]
11. **Coordinate rarely and on purpose: long heads-down blocks, short future-focused syncs.** Interruptions reset focus, over-coordination freezes specialists, and "what I did" stand-ups crowd out problem solving; but the sync itself is where most breakthroughs come from, so make it about surprises and blockers. [Fried et al., Getting Real, p.66-67]; [Rumelt, Good Strategy Bad Strategy, p.104-105]; [Stickdorn et al., This Is Service Design Methods, p.598-600]; [Johnson, Where Good Ideas Come From, p.52-54]
12. **Put test slots and rehearsal on the timeline now as immovable events; cut polish before cutting them.** If someone must decide when to test, it does not happen; people forgive ugly sooner than unusable; and polished delivery is planned practice. [Krug, Rocket Surgery Made Easy, p.36-37]; [Klein, UX for Lean Startups, p.83-84]; [Gallo, Presentation Secrets of Steve Jobs, p.307-312]

## Decision procedure
Main decision: at each checkpoint, continue, cut, mock, or pivot. Steps 1-3 run once at kickoff.

1. **Kickoff agreement (H0, 15 min, one page).** Owner per area (build on the team plan's four ownership areas, but give each a vertical slice where possible), the Decider, the tie-break rule, the stuck rule (blocked 30 minutes means say it aloud), merge rule (nobody merges on red), and a staggered sleep plan. [Stickdorn et al., This Is Service Design Methods, p.571-572]; [Grenny et al., Crucial Conversations, p.201-202]; [Winters et al., Software Engineering at Google, p.351-352]
2. **Size scope (H0-2).** Capacity is about 40-48 person-hours of real building. Estimate each feature, multiply risky ones by 1.5-2x, rank them, and draw the cut line so the must-ship set uses at most about half of capacity. Everything below the line is stretch, written on the wall, and the stretch list freezes at about H16. [Brooks, Mythical Man-Month, p.109, p.33-34]; [Kahneman, Thinking Fast and Slow, p.242-243]; [Hackathon Planning Kit, Goal, p.6]
3. **Fix the clock.** Write these on the whiteboard before coding: problem converge by H3, solution converge by H6 [Norman, Design of Everyday Things, p.231-233]; cleaned data table by H6 [McKinney, Python for Data Analysis, p.308]; thin E2E slice by H6-8; demo-able end to end by H12 [Kelley and Kelley, Creative Confidence, p.130-131]; user test slots near H9-10 and H18-19 [Krug, Rocket Surgery Made Easy, p.36-37]; [Klein, UX for Lean Startups, p.83-84]; feature freeze H16-18; frozen demo deployment by H20; last 2-3 hours for rehearsal.
4. **At each checkpoint (H6, H12, H18, H22; 10 minutes max).** Ask four questions: what did we expect, what happened, are we continuing, what do we cut? Compare percent of time used with percent done for each owner. [Ries, Lean Startup, p.135-136]; [Patton, User Story Mapping, p.105-106]
   - Done roughly matches time: continue; move nothing across the line.
   - Done is under about two-thirds of time used (for example 50% time, 33% done): cut the lowest cost-of-delay item below the line or replace it with a smaller version that delivers the same value. [Perri, Escaping the Build Trap, p.155-157]; [Crispin and Gregory, Agile Testing, p.380-382]
   - Thin slice not integrated at H8: stop new work, everyone integrates against mocks until one request travels end to end.
5. **Pivot window (H10-12 only).** Pivot only if the core hypothesis has shown no positive signal after several quick tests, or 3 of 5 testers were confused by the core flow. Before committing, a devil's advocate argues the strongest case against for 5 minutes. After H12, no pivots: cut instead. [Kohavi et al., Trustworthy Online Controlled Experiments, p.58-59]; [Knapp, Sprint, p.171-173]; [Kahneman et al., Noise, p.94-97, p.82]
6. **Stuck-work rule (any time).** At 30 minutes blocked, say it aloud. At 45-60 minutes, ask the sunk-cost question out loud; if the answer is no, switch approach or mock it. [Kahneman, Thinking Fast and Slow, p.335]; [Grenny et al., Crucial Conversations, p.208-209]
7. **H18 hard rule.** If the core path does not work by a time written down in advance (for example H19), switch that part to a mocked or prerecorded version and spend the remaining time on polish and rehearsal. No late architecture changes, no refactors after H18. [Kahneman, Thinking Fast and Slow, p.310]; [Ousterhout, Philosophy of Software Design, p.28-31]
8. **H20 demo freeze.** The demo runs from its own deployment with its own keys and database; nothing is pushed to it after freeze. Go/no-go is a written checklist decided jointly, not by one gatekeeper. [Nygard, Release It!, p.119-123]; [Kaner et al., Lessons Learned in Software Testing, p.52]
9. **Final hours.** At least five timed run-throughs with the live demo on the real clock, one in front of an outsider who is asked only "what was it about, and what was confusing?" [Gallo, Presentation Secrets of Steve Jobs, p.307-312]; [Olson, Houston We Have a Narrative, p.189]

## Checklists
**Kickoff (H0-1), all must be yes before coding**
- [ ] Decider named aloud; tie-break rule written (owner decides, or a 30-minute test, or coin flip if reversible). [Knapp, Sprint, p.28-29]; [Bland and Osterwalder, Testing Business Ideas, p.161]
- [ ] Noise audit done; score spread under about 25 points and everyone names the same user. [Kahneman et al., Noise, p.28-29]
- [ ] 2-3 interface contracts (API shape, record format) written, with mock versions committed. [Martin, Clean Architecture, p.155]; [Kleppmann, Designing Data-Intensive Applications, p.521-523]
- [ ] One lockfile and one setup script; every teammate has run the app locally. [Huyen, Designing ML Systems, p.341, p.345-347]
- [ ] Cut line, "NOT doing" list, minimum demo goal and stretch goal visible on the wall. [Lafley and Martin, Playing to Win, p.64, p.75]; [Hackathon Planning Kit, Goal, p.6]
- [ ] Demo acceptance sentence written: "Input X produces Y in under Z seconds on stage." [Heath, Made to Stick, p.108]
- [ ] Clock times for checkpoints, test slots, freezes, meals, and sleep shifts written down.

**Each checkpoint**
- [ ] Percent time vs percent done per owner compared; any cut written on the wall, not done silently.
- [ ] Work in progress at most about 2 features for 4 people; demo-critical feature finished before nice-to-haves. [Crispin and Gregory, Agile Testing, p.411-412]
- [ ] Each person said what they do next and where they need help (not what they did). [Stickdorn et al., This Is Service Design Methods, p.598-600]
- [ ] Decisions recorded in one pinned doc; chat carries only a link. [Richards and Ford, Fundamentals of Software Architecture 2e, p.697-698]
- [ ] Next checkpoint time and owner restated. [Wedell-Wedellsborg, What's Your Problem, p.250-254]

**Freeze go/no-go (H18-20)**
- [ ] Cross-test done: each owner tested someone else's part and the seams between them. [Kaner et al., Lessons Learned in Software Testing, p.350]; [Kaner and Johnson, LAWST 7 Styles of Exploration, p.45]
- [ ] A teammate cloned the repo to a clean machine and ran it end to end. [Leek, Elements of Data Analytic Style, p.96]
- [ ] Known-good version tagged and runnable; fallback mock or recording ready. [Lakshmanan et al., Machine Learning Design Patterns, p.388-397]
- [ ] The most rested person checked every number and claim on slides and in the submission. [Kahneman, Thinking Fast and Slow, p.80-81]
- [ ] Meal and a 15-minute rest scheduled before the last rehearsal. [Kahneman, Thinking Fast and Slow, p.43-45]

## Anti-patterns
- **Big-bang merge.** Tell: four branches, nothing runs end to end at H10. Fix: thin slice by H6-8, hourly merges, a 15-minute joint session tracing one request across owners. [Martin, Clean Architecture, p.129-130]; [Kaner and Johnson, LAWST 7 Styles of Exploration, p.45]
- **Silent trim.** Tell: features quietly half-done, testing skipped, nobody can say what is left. Fix: formal cut at the next checkpoint, re-plan the demo path. [Brooks, Mythical Man-Month, p.40-41]
- **Heroic all-nighter as the plan.** Tell: "we'll just push through tonight." Fix: at the overnight low, re-plan scope and sleep in staggered 90-minute shifts, with the open problem written on a card before sleeping. [Rumelt, Good Strategy Bad Strategy, p.61-63]; [Johnson, Where Good Ideas Come From, p.79-80]
- **Late helper on the critical path.** Tell: a mentor or spare person is onboarded to the main module at H15. Fix: give them isolated work only (seed data, README, slides, demo script). [Brooks, Mythical Man-Month, p.40-42]
- **Loudest-voice brainstorm.** Tell: ideas judged live, first speaker sets the direction. Fix: 30-40 minutes silent solo sketching, private straw poll, Decider calls it. [Knapp, Sprint, p.88, p.111-114]
- **Relitigating settled decisions at 3 a.m.** Tell: a pivot or stack change proposed after H12. Fix: point to the written decision and the "if X then Y" list; tired-hour proposals go to the parking lot. [Kahneman et al., Noise, p.82]; [Michalko, Thinkertoys, p.98]
- **Endless debate.** Tell: the same argument for 10+ minutes. Fix: 3-5 minute cap, each person states the goal behind their position, ask "what data would settle this?", run a 30-minute test or let the area owner decide. [Grenny et al., Crucial Conversations, p.103-107]; [de Bono, Six Thinking Hats, p.118-119]
- **Polish before the flow works.** Tell: hours on visuals while no stranger has completed the flow. Fix: run the scheduled test even if ugly; polish only after a stranger succeeds. [Gothelf, Lean UX, p.119-120]
- **Blame spiral after a bad judge visit.** Tell: "the judges are clueless" or "it's too late anyway." Fix: each person names one thing they could do differently before anyone blames; a mutual 10-minute time-out with a stated return time, never "calm down." [Grenny et al., Crucial Conversations, p.128-130, p.210]

## Hackathon calibration
- **Compress ceremonies, keep the shape.** Weekly planning, retros, and daily standups become a 5-10 minute sync at each 3-4 hour block boundary. [Bland and Osterwalder, Testing Business Ideas, p.67-76]
- **Design investment shrinks.** Ousterhout's 10-20% of time on design becomes about 2-4 hours total: interfaces up front, one mid-build cleanup, one pre-freeze pass, and no refactoring after H18. Cap architecture design at about 45 minutes. [Ousterhout, Philosophy of Software Design, p.28-31]; [Richards and Ford, Fundamentals of Software Architecture, p.32, p.103]
- **Skip infrastructure judges will not see.** No ML pipelines, feature stores, or registries; one train script, one serve script, pinned dependencies, roadmap on one slide. [Lakshmanan et al., Machine Learning Design Patterns, p.358, p.365]
- **Learning loops shrink to 2-3 hours.** Plan two or three build-test-fix loops instead of one long build; "runway" is how many of those loops remain. [Ries, Lean Startup, p.131-133]
- **Judging changes the end of the timeline.** With about 200 projects and roughly 4 minutes per judge, most teams show a working demo, so the conversation separates you; budget the last 3-4 hours for rehearsal and Q&A. Treat Dixon's 53% figure as directional (B2B sales data). [Dixon and Adamson, Challenger Sale, p.78-82]; [Knaflic, Storytelling with Data, p.299-301]
- **Booth roles.** Two presenters maximum for a short slot (story plus demo driver), others take technical Q&A in their area; rotate a listener who notes 2-3 judge phrases after each visit; agree a hand signal to tag out a heated teammate, which matters most at H20+. [Gallo, Presentation Secrets of Steve Jobs, p.228-231]; [Voss, Never Split the Difference, p.27, p.129-132]
- **Energy before judging.** Five slow breaths or a 60-second walk between judge visits; practice the hardest sentence aloud three times. [Reynolds, The Naked Presenter, p.98-99]; [Gallo, Talk Like TED, p.86-88]
- **Ignore** long-horizon advice on hiring, team-of-teams structure, monthly decision cadence, and payback-over-months design arguments; none applies inside 24 hours.

## Where experts disagree
- **When to freeze features.** Huyen says about H14 for AI demos; Agile Testing says H18-19; the Planning Kit freezes the stretch list at H16; Gallo says H20 to protect rehearsal. Follow: freeze stretch work at H16, freeze all features by H18, freeze the demo deployment at H20. AI-heavy projects should lean toward H14-16 because reliability is the slow part. [Huyen, AI Engineering, p.86-87]; [Crispin and Gregory, Agile Testing, p.416]; [Hackathon Planning Kit, Goal, p.6]; [Gallo, Presentation Secrets of Steve Jobs, p.307-312]
- **Cut hard vs stop cutting.** Kahneman and Agile Testing say plan half and keep cutting at every checkpoint; Cagan says the minimal product is coherent and cutting further breaks it. Both hold: cut aggressively around the one demo flow and below the line, never inside the flow. [Kahneman, Thinking Fast and Slow, p.242-243]; [Cagan, Inspired, p.137-139]
- **Vertical slices vs role split.** Shape Up and Fundamentals want end-to-end slice owners; Getting Real and Huyen want a floater or single deploy owner. Follow: two slice owners, one integrator who owns deploy and the one-script redeploy, one evidence and pitch owner (matching the team plan), with everyone able to run and redeploy. [Singer, Shape Up, p.96-97]; [Fried et al., Getting Real, p.29-30]; [Huyen, Designing ML Systems, p.385-388]
- **One Decider vs shared release call.** Knapp and Perri want one person who breaks ties; Kaner warns that a single release gatekeeper gets blamed and lets others relax. Follow: the Decider owns scope and priority; go/no-go at freeze is a written checklist the team runs together. [Knapp, Sprint, p.111-114]; [Perri, Escaping the Build Trap, p.44-46]; [Kaner et al., Lessons Learned in Software Testing, p.52]
- **Retro or no retro.** Bland says skip retros at this pace; Agile Testing and Stickdorn want a short one. Follow: one 5-10 minute retro at the midpoint (H12), producing one stop and one start, checked at H18. [Bland and Osterwalder, Testing Business Ideas, p.67-76]; [Crispin and Gregory, Agile Testing, p.485-487]; [Stickdorn et al., This Is Service Design Methods, p.607-608]
- **How often to talk.** Getting Real wants 3-hour silent blocks; Martin wants hourly merges; Johnson says breakthroughs come from the group table. Follow: merge code hourly without meeting, talk every 3 hours with 2 minutes each on "what surprised me, what is stuck." [Fried et al., Getting Real, p.66-67]; [Martin, Clean Architecture, p.129-130]; [Johnson, Where Good Ideas Come From, p.52-54]

## Go deeper
- search_experts("productive hours half the clock estimate overrun", domain="18-team-execution")
- search_experts("planning fallacy best case scope cut list", domain="18-team-execution")
- search_experts("sunk cost risk seeking when losing mock fallback", domain="18-team-execution")
- search_experts("integrate in small steps weekly build interface contracts", domain="18-team-execution")
- search_experts("Decider straw poll independent votes cascade", domain="18-team-execution")
- search_experts("noise audit illusion of agreement team", domain="18-team-execution")
- search_experts("fatigue decision quality irreversible decisions early", domain="18-team-execution")
- search_experts("feature freeze testing crunch rehearsal time", domain="18-team-execution")
- search_experts("stuck blocked say it early crucial conversation team", domain="18-team-execution")
- search_experts("staggered sleep incubation break creativity", domain="18-team-execution")
