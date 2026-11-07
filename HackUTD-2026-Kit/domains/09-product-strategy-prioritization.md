---
name: 09-product-strategy-prioritization
description: Open when choosing between candidate ideas at hour 0-2, writing the strategy kernel and not-doing list, deciding what to build vs fake vs cut, sequencing the first build hours by risk, running the +3h/+6h/+8h/midpoint/+14h checkpoints, or deciding whether a late feature or mentor suggestion gets in.
---
# Product strategy and feature prioritization

## Use this when
- Hour 0-2: the team has 2-4 candidate ideas and must commit to one with a stated reason and explicit pivot conditions.
- Hour 1-3: turning the chosen idea into a scoped build (cut line, demo path, fake list, first spike).
- A teammate, mentor, or sponsor rep proposes "one more feature" after scope is set.
- A checkpoint arrives and the build is behind, a spike failed, or testers shrugged.
- Two teammates are deadlocked on scope or direction and the clock is running.
- Preparing answers to "why this?", "why not also X?", and "what's missing?" for judges.

## Core principles
1. **Fix the appetite first, then shape the solution to fit it.** An estimate starts from a design and ends in a number; an appetite starts from a number and ends in a design, so scope flexes and the deadline never does. Keep Musts at or under ~60% of build capacity. [Shape Up, p.29-30] [Seed: D. Prioritization frameworks, §D2]
2. **The guiding policy must tell a teammate what NOT to build.** Write diagnosis, guiding policy, and 3-6 coherent actions; if a teammate cannot list features that violate the policy, it is a vision, not a policy. Strategy is mostly the list of whole classes of work you refuse. [Good Strategy Bad Strategy, p.89-91, 95-97, 34-35] [Playing to Win, p.64]
3. **Build the scariest unknown first, and count it solved only when real data returns inside your app.** (counterintuitive) Teams start with login, nav, and the UI shell because they are familiar; that teaches nothing. The first slice must be core, small, and novel. Reading the docs is "thought about it", not "validated". [Lean Startup, p.100-101] [Shape Up, p.111-112, 139]
4. **Solve the whole core task crudely before any part of it nicely.** A skateboard is usable; a wheel is not. The walking skeleton (top card of every story-map column, end to end through every layer) must run by +8h, ugly is fine. [User Story Mapping, p.93-95, 103-104] [Seed: A. Hackathon product plan, §7]
5. **Make the cuts early, then treat the minimal product as one coherent whole.** (counterintuitive) Cutting whatever runs late produces an incoherent product; if a feature can be cut without harm it was never part of the minimum. With a fixed deadline, cut before validation (by ~+6h) and protect the validated core afterward by stealing from polish and extras. [Inspired, p.137-139]
6. **No feature without a behavior hypothesis and a link to another feature.** Ask "what will a user or judge do differently because of this?" and "which other feature does this make better?". Features that are orphans or that conflict with the core promise get cut. [Lean Startup, p.117] [Good Strategy Bad Strategy, p.40, 102-103]
7. **Choose one user in one moment; "everyone" means you have not chosen.** (counterintuitive) A narrow, focused build looks too small to the team but stands out among ~200 sprawling projects, because most teams spread effort. [Playing to Win, p.67] [Good Strategy Bad Strategy, p.26, 97-99] [User Story Mapping, p.77-78]
8. **Write real code only where the novelty lives; fake or borrow the rest.** Concierge, Wizard of Oz, hardcoded seeds, and off-the-shelf auth are legitimate for everything that is not the core experience or the core technical risk. Disclose what is simulated if asked. [Inspired, p.96] [Lean Startup, p.85-91] [Escaping the Build Trap, p.117]
9. **Win on one dimension users can see, not on "better tech".** Pick the single axis (speed, accuracy, simplicity, accessibility) and put polish there; a superior model alone does not answer "what stops a big company copying this?". Each claimed advantage needs visible proof in the demo. [Playing to Win, p.100-105, 96-97]
10. **Count progress in user behavior, reported in people.** "7 of 10 testers finished unaided" beats "we built 12 features" or page views. Predict the number before testing so you cannot rationalize the result. [Lean Startup, p.83, 101, 104-105] [Escaping the Build Trap, p.123]
11. **Decide "good enough" against today's workaround, not the ideal.** If the demo clearly beats the manual or competitor baseline, stop polishing and rehearse. [Shape Up, p.143-144]
12. **Name one decider; do not vote among 3+ options.** Pairwise votes among four people with different rankings can cycle with no stable winner, and "do all of them" is the usual mushy escape. [Good Strategy Bad Strategy, p.72-74]

## Decision procedure
Main decision: what goes above the cut line, in what order, and when to change course.

1. **Compute capacity (5 min).** Build hours = time after idea lock minus ~3h demo prep and buffer (target ~15-18h). Multiply by 4 people. Subtract 25-30% for work you will only discover by building [Shape Up, p.101-102]. Musts may consume at most 60% of what remains. Example: 16h x 4 = 64 person-hours, minus 30% = ~45, so Musts ≤ ~27 person-hours.
2. **Gate each candidate idea (10 min per idea, 90 min hard cap total).** Pass all or drop it:
   - Diagnosis completes "Existing tools fail because ___" with a mechanism, not an outcome ("people waste time" fails). [Good Strategy Bad Strategy, p.68-70]
   - One sentence "For [user], we win because [one distinctive thing]" where the second half follows from the first. [Playing to Win, p.109]
   - Five betting questions: problem matters, appetite fits (would a smaller version fit?), solution attractive, right time, right people (someone has built something similar). [Shape Up, p.90-93]
   - The essential benefit is demonstrable live in about 2 minutes. If two ideas pass, the decider picks; do not average them.
3. **Write the kernel and not-doing list (15 min).** Diagnosis, guiding policy, 3-5 coherent actions; at least 5 named exclusions (segments, platforms, flows such as accounts, settings, multi-user). Ask each member which pet feature they gave up; if nobody gave one up, scope is not cut enough. [Good Strategy Bad Strategy, p.76-77]
4. **Rank leap-of-faith assumptions (10 min).** Write 2-4 in blunt present tense, no analogies [Lean Startup, p.71-73]. Rank by "if false, does the idea die?" times "how little do we know?". Label each Premise, Operations, or Launch and test Premise first; Launch risk barely exists for a weekend demo [The Right It, p.29-30]. The top technical one gets a spike that must finish by **+3h**; the top value one gets 3-5 five-minute "last time you did X" conversations running in parallel.
5. **Map and slice (30 min).** Backbone of 4-7 verb-led user activities; tasks beneath, essential on top. Draw the walking-skeleton line. Then ask "what must a judge see and do in ~2 minutes?" and drop everything not required for that event [User Story Mapping, p.74-76]. That path is the demo script.
6. **Admit features individually.** Above the line only if all hold: on the demo path, has a behavior hypothesis, links to another feature, sub-appetite ≤2h (only the technical centerpiece may exceed it). Tag each card differentiator or table stakes; invest in the 1-2 differentiators, fake or minimize table stakes [User Story Mapping, p.79-80]. Anything off the demo path taking >2h is cut [Escaping the Build Trap, p.155-156].
7. **Run checkpoints with pre-agreed triggers.**
   - **+3h:** spike returned real data in-app, or swap the approach or fake it now.
   - **+6h:** if 3 of 4 testers do not want it, change the framing or the problem; if the "why we win" sentence no longer holds, change user or angle [Inspired, p.153] [Playing to Win, p.112].
   - **+8h:** skeleton runs end to end. If not, cut to the single surviving path and redesign around it.
   - **Midpoint (~+11-12h), 20 min:** pivot-or-persevere with tester numbers on the table and a non-builder or mentor as outside voice. Default pivot is zoom-in: the one part testers liked becomes the whole demo [Lean Startup, p.128-129, 135-136, 142-145].
   - **Any checkpoint:** half the time gone with a third done means cut now, not at hour 22 [User Story Mapping, p.105-106].
   - **+14h:** feature freeze. New ideas go to a "post-demo / roadmap" list only.
   - **+18h:** only demo-path bugs (crash, data loss, broken step) get fixed; record the backup video.
8. **After freeze, extend nothing that is still uphill.** If an unfinished item still has unknowns at +20h, cut it and use the fallback (cached data, recorded clip) rather than eating rehearsal time [Shape Up, p.148-149].

## Checklists
**Scope review (run on your own plan before assigning work)**
- [ ] Policy rules out at least 3 features someone proposed.
- [ ] One named user, one named moment; deferred users listed as roadmap.
- [ ] Riskiest assumption has a spike with a +3h deadline and an owner.
- [ ] Every Must traces to the demo script; Musts ≤60% of capacity after buffer.
- [ ] Each feature has "users will ___ differently" written next to it.
- [ ] Fake/borrow list exists (auth, payments, admin, scale) and is disclosed in Q&A notes.
- [ ] Sponsor tech sits inside the core loop, not bolted on beside it.

**Feature admission (30 seconds, after +6h default answer is no)**
- [ ] Is it on the demo path? What happens if we skip it? Can we fake it? [Shape Up, p.144-146]
- [ ] Does it deepen the experience for our chosen user, or broaden to another user? (broaden = decline) [Playing to Win, p.104-105]
- [ ] What equal-size item comes off the line to make room? [Good Strategy Bad Strategy, p.34-35]

**Pre-freeze honesty check**
- [ ] Every number in the pitch states its sample size and comes from observed behavior.
- [ ] Every claimed advantage is visible in the demo.
- [ ] Omissions are framed as deliberate choices from the not-doing list.

## Anti-patterns
- **Feature pile (build trap).** Tell: status updates list features built; nobody can say what a user does differently. Fix: re-anchor on the one-sentence outcome and delete orphans. [Escaping the Build Trap, p.25-27]
- **"Do all of the above."** Tell: the team resolves a split by keeping two ideas or chasing three sponsor tracks with separate features. Fix: one decider, 3 minutes per advocate, then one choice; enter extra tracks only if the same build already qualifies. [Good Strategy Bad Strategy, p.72-74] [Escaping the Build Trap, p.100-101]
- **Layer-by-layer build.** Tell: at +8h frontend and backend each "work" but have never been joined. Fix: integrate a thin slice immediately; assign people whole slices, not layers. [Shape Up, p.96-97, 103-104]
- **Spiking the familiar.** Tell: the first hours go to auth, routing, or a landing page. Fix: stub them; the model, data source, or sponsor API goes first. [Shape Up, p.139-141]
- **Gutted big idea.** Tell: the demo shows 30% of a grand vision with dead buttons. Fix: define the smallest complete experience for one user and build all of it; pitch the vision verbally. [Playing to Win, p.110-111] [Shape Up, p.83]
- **Polishing a flat result.** Tell: two rounds of UI tweaks and testers are still unmoved. Fix: change the idea or audience, not the styling. [Lean Startup, p.103-106]
- **Order-taking.** Tell: every mentor suggestion becomes a ticket. Fix: log it as "interesting, maybe some day"; implement only what serves the stated outcome. [Escaping the Build Trap, p.46-47] [Shape Up, p.31]
- **Category label as strategy.** Tell: the pitch says "an AI-powered platform for X". Fix: replace with a verb phrase: "we detect X from Y so that Z can ___". [Good Strategy Bad Strategy, p.50-54] [Shape Up, p.33-34]
- **Claiming white space.** Tell: "nobody does this" without a search. Fix: 15 minutes on Devpost, app stores, GitHub; rewrite as "unlike X, we do Y for Z". [Playing to Win, p.76]
- **Willpower plan.** Tell: "we'll push through overnight" replaces a cut. Fix: at the overnight low, re-plan scope and sleep in shifts. [Good Strategy Bad Strategy, p.61-63]

## Hackathon calibration
- **Judging format drives scope.** About 4 minutes per judge, science-fair style, means the demo path must run in roughly 2 minutes with room for questions, and must run identically many times in a row. Reliability of one path outranks breadth. MLH criteria reward completion, which a thin complete flow satisfies and a broad half-flow does not.
- **Judges ask strategy questions in disguise.** "Why this?" wants the diagnosis; "why not also X?" wants the guiding policy and not-doing list. [Seed: B. Strategy, §B1]
- **Ignore RICE.** It needs real reach data and is unreliable below ~1,000 users. [Seed: D. Prioritization frameworks, §D1-D2]
- **Ignore A/B tests, cohorts, and staged rollouts** as practices; you will never reach significance. Use them only as "what we'd measure next" talking points. [Escaping the Build Trap, p.142]
- **Shrink tester targets.** Cagan's "six clean users in a row" becomes 3-6 testers total with at least one fix cycle between them; report how many you reached. [Inspired, p.153]
- **Shrink orientation time.** Shape Up tolerates days of quiet exploration; here allow 1-2 hours, then require something clickable by +4-6h. [Shape Up, p.100-101]
- **Invert Cagan's slip rule.** He extends the schedule to protect a validated core; you cannot, so you cut earlier instead. [Inspired, p.138]
- **Pivot windows close fast.** A full problem pivot is survivable at +6-8h; after the midpoint, only zoom-in pivots that reuse the working pipeline are realistic. [Lean Startup, p.138-139, 145]
- **Viability is four back-of-envelope numbers** (who pays, price, cost to serve, how they find you), labeled as assumptions, plus one concrete first-100-users path instead of a TAM slide. [Inspired, p.89] [Good Strategy Bad Strategy, p.54-56]
- **Sponsor tracks:** meet the sponsor's stated requirement with the smallest compliant slice inside the core loop; do not let it fork the product. [Escaping the Build Trap, p.27, 33-34]

## Where experts disagree
- **Three tiers vs one line.** The seed uses MoSCoW; Patton prefers a single in/out line [User Story Mapping, p.66]; Cagan says drop P1/P2/P3 labels once the minimum is defined [Inspired, p.137-139]. Follow here: use MoSCoW once at hour 1-2 to sort the brainstorm, then work from a single cut line, with "~" on nice-to-haves [Shape Up, p.126]. Musts inflate under pressure, and a binary line resists that.
- **Scoring vs judgment.** The seed offers an ICE scale; Hubbard warns that multiplying ordinal ratings is not measurement [How to Measure Anything, p.58-59]; Torres says compare without a scorecard [Continuous Discovery Habits, p.103-106]. Follow here: use ICE only to expose where teammates disagree, then let the decider settle the top two using plain units (hours, rough probability of finishing by +14h).
- **Value risk first vs feasibility first.** Cagan's camp says the deadliest risk is usually value [Seed: B. Strategy, §B2]; Shape Up and Ries push the scariest technical unknown uphill first. Follow here: run both in the first 3 hours in parallel (one engineer spikes, one person holds problem conversations). In 24h a failed core integration kills the demo outright, while a weak value story can still be reframed.
- **How much discovery up front.** Cagan front-loads about a third of the time on prototypes [Inspired, p.176-177]; Ries warns against analysis paralysis and says timebox planning [Lean Startup, p.78-79]. Follow Ries here: 90 minutes to lock the idea, then learn by building, with tester checks at +6h and the midpoint.
- **Bold bet vs simplify.** Sprint says put the risky, high-payoff idea in the prototype [Sprint, p.126]; Ries says when in doubt, leave it out [Lean Startup, p.82-83]. Follow both by splitting: be bold on the single differentiator, cut everything else to the bone.
- **Decider vs buy-in.** Rumelt wants a named decider [Good Strategy Bad Strategy, p.73-74]; Cagan wants everyone on board [Inspired, p.100-102]. Follow here: open debate with visible ranked goals, then the decider calls it and everyone commits. Under time pressure, waiting for consensus costs more than resentment does.

## Go deeper
- search_experts("riskiest assumption test leap of faith", domain="09-product-strategy-prioritization")
- search_experts("appetite fixed time variable scope", domain="09-product-strategy-prioritization")
- search_experts("guiding policy diagnosis coherent action kernel", domain="09-product-strategy-prioritization")
- search_experts("scope hammering decide when to stop", domain="09-product-strategy-prioritization")
- search_experts("walking skeleton release slice story map", domain="09-product-strategy-prioritization")
- search_experts("minimal product stop cutting validated core", domain="09-product-strategy-prioritization")
- search_experts("pivot or persevere zoom-in pivot", domain="09-product-strategy-prioritization")
- search_experts("where to play how to win differentiation", domain="09-product-strategy-prioritization")
- search_experts("concierge Wizard of Oz fake the back end", domain="09-product-strategy-prioritization")
- search_experts("cost of delay urgency value cut scope", domain="09-product-strategy-prioritization")
