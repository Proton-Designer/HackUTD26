---
name: 04-workflow-friction
description: Open when mapping how the target user does the task today (hours 1-3), choosing which single workflow step to build around, turning a friction log or interviews into a before/after number for the pitch, or walking through our own demo flow to find where judges and testers stall.
---
# Workflow and friction analysis

## Use this when
- Hour 1-3: a problem area is picked and the team needs a current-state map of the user's task plus one "hot spot" step to build for.
- Two or three candidate pain points are on the board and the team must pick one with evidence, not opinion.
- Interview notes, a friction log, or stopwatch timings need converting into an outcome statement and a before/after metric for the pitch and the team plan's foundation statement.
- A mentor, sponsor, or teammate pushes a feature mid-build and you need to check whether it touches the hot-spot step at all.
- Hours 8-20: walking through our own demo path (cognitive walkthrough, hallway tests) to remove the places a first-time judge would hesitate.
- Writing the before/after slide or answering "how do you know this is a real problem?" in Q&A.

## Core principles
1. **Stopwatch the current workflow before building; the time delta is the headline.** Measured before/after times are the strongest friction evidence in the books (210 min across two providers cut to 65; registration cut from 50 to 10 min), and judges remember a number. [Mapping Experiences, p.283-285] [This Is Service Design Doing, p.751, p.792] [Seed: 0. Synthesis, §8]
2. **Watch people do the task; do not trust what they say hurts.** People rarely notice or report their own difficulties and blame themselves for interface failures, so absence of complaints proves nothing; count observed mistakes, retries, and workarounds instead. [The Design of Everyday Things, p.29, p.85-86] [Mapping Experiences, p.132-133]
3. **Treat the team's guess about the pain point as a hypothesis and label every map ASSUMPTION or RESEARCH (n=).** In Kalbach's clinic case staff blamed scheduling, but patients liked scheduling and were anxious about not knowing what came next; fixing the wrong step can lower satisfaction. (counterintuitive) [Mapping Experiences, p.311-314] [This Is Service Design Doing, p.86]
4. **Map the job, not the tool: verb + object steps that hold regardless of method.** A job map across Define, Locate, Prepare, Confirm, Execute, Monitor, Modify, Conclude finds opportunities in the unglamorous stages (Locate, Monitor, Modify) that a feature-centered view misses. [Seed: B. Mapping the job and the journey, §B1] [Mapping Experiences, p.323-325] [What Customers Want, pp.62-65]
5. **Build for one hot spot, not an even spread of improvements.** Perception is the sum of a few charged moments; score each step -2 to +2, tally pain per step, and aim at the deepest dip. [Mapping Experiences, p.55-57] [This Is Service Design Doing, p.104, p.613-615] [Seed: A. Hackathon quick-run protocol, §Step 4]
6. **Diagnose the scarcest ability factor; click count is rarely the blocker.** Check time, money, physical effort, brain cycles, routine fit (plus social deviance in the seed's extended model) and fix the weakest link; about three mindless clicks cost the same as one click that needs thought. (counterintuitive) [Tiny Habits, p.103-104] [Seed: C. Finding and diagnosing friction, §C2] [Don't Make Me Think, p.59]
7. **When users skip a step, check prompt first, then ability, then motivation.** Persuasion and nagging are the usual first instinct and usually wrong; a missing cue or one hard sub-step is cheaper to fix and easier to demo. (counterintuitive) [Tiny Habits, p.43-45, p.37]
8. **Friction clusters at handoffs, and the boundary tells you the fix type.** Line of interaction failure (can't find it) needs a screen fix; line of visibility failure (waiting with no update) needs status and visible evidence; internal line failure (work dropped between systems) needs integration or automation. [Seed: B. Mapping the job and the journey, §B4] [Mapping Experiences, p.42-43, p.54] [This Is Service Design Doing, p.119-122]
9. **Delete a step before you automate it.** For each row ask "does the user care about this step?"; technology fixes applied to no-value steps miss the real problem. (counterintuitive for AI projects) [Mapping Experiences, p.280-283] [Seed: B. Mapping the job and the journey, §B1]
10. **Write outcomes as "minimize/increase + unit + object" and rank by importance + max(importance - satisfaction, 0).** Above 15 is extreme, 12-15 low-hanging fruit, 10-12 worth considering, below 10 drop; feature requests and adjectives ("faster", "easier") are not requirements. [What Customers Want, pp.62-64, pp.77-79, pp.81-82, pp.17-18]
11. **Test our own flow with 3 users per round and treat any error seen twice as a defect.** The first three users surface most major problems; more small rounds beat one big round. [Don't Make Me Think, p.173-174] [The Design of Everyday Things, p.85-86]
12. **Time-box mapping to the questions it must answer.** Write the 2-3 questions first and stop when they are answered; detailed maps cause "mapping overload". [Mapping Experiences, p.51-52, p.329-330]

## Decision procedure
Main decision: which workflow step do we build around, and is the evidence strong enough to commit 20 hours to it?

1. **Scope (5 min).** Write one line: "[specific person] doing [specific task], from trigger to done." One point of view only. Add a job statement: "When [situation], I want to [motivation], so I can [outcome]." [Mapping Experiences, p.45-46] [This Is Service Design Doing, p.109]
2. **Draft the assumption map (20-30 min, whole team).** 8-15 verb + object steps under the 8 job stages, no tool names. Include what the user does right before and after the task, not only where software is touched. Tag it ASSUMPTION. [Seed: A. Hackathon quick-run protocol, §Step 1] [This Is Service Design Doing, p.115-116, p.249]
3. **Collect evidence in one 60-90 min loop, split across people.**
   - One teammate runs a friction log of the current way, end to end, screen recorded, stopwatch on, every search/click/error/reaction logged and coded Green/Yellow/Red. [Seed: C. Finding and diagnosing friction, §C1]
   - Two pairs run 3-5 interviews of 15-20 min: open with "tell me about the last time this went wrong", then "show me how you did it". One lead, one silent notetaker. [Mapping Experiences, p.153, p.152] [This Is Service Design Doing, p.229]
   - Optional 30 min: reviews, Reddit, forums for existing friction evidence. [Mapping Experiences, p.133-135]
   - Stop when the last two sessions repeat the same top 2 pains. [This Is Service Design Doing, p.201-202]
4. **Fill the workflow table.** Columns from the seed: step, how done today, time, handoff?, pain quote (coded like i3.12), Fogg factor, waste type, G/Y/R. Add one column: gulf (execute = "how do I do it", evaluate = "did it work"). [Seed: A. Hackathon quick-run protocol, §Step 2] [The Design of Everyday Things, p.59-61]
5. **Rank candidate steps.** Hot spot score = most Red + most time + most handoffs/tool switches. Circle every point where the user switches tool, copies data by hand, or waits on someone. If 10+ target users are reachable, add importance/satisfaction ratings and compute the opportunity score as a tie-breaker. [Seed: A. Hackathon quick-run protocol, §Step 4] [Mapping Experiences, p.54] [What Customers Want, pp.77-79]
6. **Choose the fix type for the top step.** In order of preference: unnecessary (delete it), automatic, faster, easier. Label the mechanism as skill, tool, or tiny; prefer tool or tiny. Match the fix to the boundary where the failure sits (principle 8). [Seed: A. Hackathon quick-run protocol, §Step 4] [Tiny Habits, p.105-107]
7. **Go/no-go gate (target: by hour 3).**
   - GO if all are true: the step's pain was observed (not only reported) in at least 2 sessions or the friction log; it has a stopwatch time or countable steps/tools; the fixed flow can be shown end to end in about one minute; opportunity score is 10+ if you scored it.
   - NO-GO if any is true: the only evidence is the team's belief; users said they like that step; the only gap is motivation (they can do it and choose not to); opportunity score under 10.
   - On NO-GO, take the next-ranked step and repeat steps 5-7 once. If that also fails, take the strongest remaining step, write its weakness down as a known risk, and commit; do not run a third research loop. [Tiny Habits, p.117] [What Customers Want, pp.81-82] [This Is Service Design Doing, part 3, p.574-578]
8. **Lock the metric.** Write the outcome statement ("minimize the time to X: N min across K tools today") and record the sample size. This fills the "[root cause]" and "[friction]" slots of the team plan's foundation statement. Re-open the hot spot only once, at the first prototype test (around hour 8-10). [What Customers Want, pp.62-64] [The Design of Everyday Things, p.29]

## Checklists
**A. Current-state map, before handing it to builders**
- [ ] One person type, one task, trigger to done.
- [ ] Every step is verb + object with no product names.
- [ ] Every step has a time; waiting time is separated from active time.
- [ ] Handoffs, tool switches, and manual copy points are circled.
- [ ] Tagged ASSUMPTION or RESEARCH (n=interviews, n=friction logs).
- [ ] At least 3 raw quotes coded to their source; interpretations kept in a separate column.
- [ ] One hot spot chosen, with the fix type and the boundary it sits on.
- [ ] Outcome statement written as minimize/increase + unit + object.

**B. Our own demo flow (run at each block-end and before freeze)**
- [ ] Each teammate answers the 4 walkthrough questions alone for every step, then compare; fix any step where answers disagree. [Seed: D. Checking our own flow, §D1]
- [ ] Every step has a visible prompt (button, label, or event) that triggers it. [Tiny Habits, p.37]
- [ ] Every action is acknowledged within 0.1 s; anything slower shows progress and disables the button. [The Design of Everyday Things, p.80]
- [ ] No dead-end errors: input is preserved and the fix is on the error message. [The Design of Everyday Things, p.85]
- [ ] The first action succeeds with pre-filled sample data. [The Design of Everyday Things, p.83-84]
- [ ] Each click is a mindless, unambiguous choice. [Don't Make Me Think, p.59]

**C. Before/after slide**
- [ ] Same format for both sides: steps, minutes, tools, handoffs, error points. [This Is Service Design Doing, p.113-114]
- [ ] "Before" numbers come from a stopwatch, not an estimate; projected savings labeled as projected.
- [ ] Sample size stated plainly ("we watched 6 people"). [Don't Make Me Think, p.171]
- [ ] One verbatim user quote, ideally a self-blame line ("I'm just bad at this"). [The Design of Everyday Things, p.60, p.83-84]

## Anti-patterns
1. **Mapping the tool, not the job.** Tell: steps read "open Excel", "email Bob". Fix: rewrite as verb + object that would hold if the tool changed ("confirm the latest usage numbers"). [Seed: B. Mapping the job and the journey, §B1]
2. **Optimizing click count.** Tell: the success metric is "fewer clicks" and nobody can name the Fogg factor. Fix: name the scarcest factor per red step; usually brain cycles (decisions) or routine fit. [Seed: C. Finding and diagnosing friction, §C2]
3. **Building on the team's guess.** Tell: the problem statement has no observed session behind it and the map is not tagged. Fix: one friction log plus two "show me" sessions before committing. [Mapping Experiences, p.311-314]
4. **Automating a step that should not exist.** Tell: the AI feature generates an artifact no one in the interviews mentioned using. Fix: ask "does the user care about this step?" and delete before automating. [Mapping Experiences, p.280-283]
5. **Fixing a handoff failure with a prettier screen.** Tell: the complaint is "I never know if it went through" and the fix is a redesign. Fix: add state and visible evidence ("Submitted, approver notified, usually 2 h"). [Seed: B. Mapping the job and the journey, §B4] [The Design of Everyday Things, p.88-89]
6. **Touchpoint-only map.** Tell: the map starts when the user opens an app. Fix: ask "what were you doing right before and right after?" and add those steps. [This Is Service Design Doing, p.115-116]
7. **Logging requests as requirements.** Tell: backlog items say "faster search", "smarter X". Fix: convert each to an outcome statement and ask "what would you give up for that?" [What Customers Want, pp.17-18, p.76]
8. **Opinion polling instead of observation.** Tell: five attendees asked "would you use this?". Fix: one person at a time doing a real task. [Don't Make Me Think, p.168-169] [This Is Service Design Doing, p.232]
9. **Mapping overload.** Tell: more than 90 minutes on the diagram, or someone opens a design tool to make it pretty. Fix: the whiteboard photo is the deliverable. [Mapping Experiences, p.329-330]

## Hackathon calibration
- **Interview volume.** The books assume 4-6 interviews per segment at 1-2 hours each, or 180-600 survey respondents for outcome scoring. Shrink to 3-5 conversations of 15-20 min plus one friction log; treat any opportunity score from 10-20 raters as directional and show the raw ratings. [Mapping Experiences, p.151] [What Customers Want, pp.79-80]
- **Remote is the default.** Over a weekend, a screen-share of the user doing the real task beats a phone discussion. [Mapping Experiences, p.150]
- **Service blueprints only for multi-actor problems.** If the task crosses people or departments, a 3-lane sketch (user, visible system, hidden system or person) in 15 min is enough; skip it for single-user tools. [This Is Service Design Doing, p.119-122]
- **Ignore the org-scale material.** Stakeholder alignment workshops, engagement-vs-satisfaction curves, 12-stage journey checklists, and multi-week in-store prototyping do not fit. The Olympics listen-learn-act loop collapses to one loop in the last 4 hours: watch one user, fix the top pain in 30 min, retest. [This Is Service Design Doing, p.613-617]
- **Judges are first-time users with about 4 minutes.** Design the demo from the novice's first-run view, since newcomers magnify small frictions. The before/after must read on one slide in seconds; a judge trying the broken workflow is too slow, so use a 10-15 s clip or a single before number instead of the books' 30-60 s footage. [Mapping Experiences, p.312-313] [This Is Service Design Doing, p.696-699, p.750]
- **Where this hits the criteria.** The before/after metric serves usefulness and impact; the walkthrough checklist serves UI/UX and completion (MLH); the evidence chain from quote to feature answers viability questions. [This Is Service Design Doing, part 3, p.589-591]
- **Schedule.** Mapping and gate by hour 3; hallway rounds of 3 at roughly hour 10 and hour 18 with a 10-minute fix triage capped at 3 items; full click-through at every block end. [Don't Make Me Think, p.173-174, p.192-193]

## Where experts disagree
- **Count steps or not?** The seed's pitch formula leads with step counts ("11 steps across 4 apps"), while Fogg says physical effort is easy to measure and rarely the blocker and Krug says click difficulty matters more than count. Follow both, for different jobs: report steps, minutes, and tools on the slide because judges remember them, but choose the fix by scarcest ability factor. [Seed: 0. Synthesis, §4, §8] [Don't Make Me Think, p.59]
- **Five or six ability factors.** Tiny Habits lists five links (time, money, physical, mental, routine); the seed's extended model adds social deviance. Use six; social deviance matters for anything users do in front of peers or bosses. [Tiny Habits, p.103-104] [Seed: C. Finding and diagnosing friction, §C2]
- **Job map or journey map first.** Ulwick-style job maps find what nobody has built; current-state journey maps find where people suffer today; Kalbach says pick the map by the question. Follow the seed protocol: 20-min coarse job map to pick the stage, then a detailed current-state table only for that stage. [Seed: B. Mapping the job and the journey, §B2] [Mapping Experiences, p.47, p.303]
- **Study competitors or not.** Krug and Kalbach say time an incumbent's key task early as free friction evidence; Stickdorn's Sun Life case says benchmarking yields average designs (opinion strength). Follow: a 20-min incumbent friction log counts as current-state evidence, but no feature enters the backlog unless it traces to observed user pain. [Don't Make Me Think, p.179-180] [Mapping Experiences, p.146-147] [This Is Service Design Doing, p.693]
- **How many test users.** Krug says 3 per round; Stickdorn cites 5 users finding about 85% of problems. Follow Krug: two rounds of 3 give a fix cycle between them, which one round of 5 does not. [Don't Make Me Think, p.173-174] [This Is Service Design Doing, p.201-202]
- **When to lock the problem.** Norman says delay specifying the problem and iterate; the team plan says reassess at checkpoints, not continuously. Follow the team plan: lock the hot spot by hour 3 as a hypothesis and reopen it exactly once at the first prototype test. [The Design of Everyday Things, p.29]

## Go deeper
- search_experts("friction log green yellow red would have given up", domain="04-workflow-friction")
- search_experts("job map define locate prepare confirm execute monitor modify conclude", domain="04-workflow-friction")
- search_experts("opportunity score importance satisfaction thresholds underserved", domain="04-workflow-friction")
- search_experts("ability factors weakest link brain cycles non-routine", domain="04-workflow-friction")
- search_experts("prompt ability motivation troubleshooting order", domain="04-workflow-friction")
- search_experts("service blueprint line of visibility failure points backstage", domain="04-workflow-friction")
- search_experts("time each step before after minutes vehicle inspection registration", domain="04-workflow-friction")
- search_experts("self-blame workarounds users do not report errors", domain="04-workflow-friction")
- search_experts("cognitive walkthrough four questions disagreement", domain="04-workflow-friction")
