---
name: problem-discovery
description: Load at hour 0 when sponsor challenges drop and the team must pick a problem, at hour 1-3 when deciding whether early chats and online evidence prove a real pain, and at the hour 6 and 12 check-ins when feedback suggests the problem is wrong.
---
# Decision guide: problem-discovery

## Open this when
- **Hour 0-0:45.** Sponsor challenges are out and someone says "let's build X with [sponsor API / LLM]," or the team is about to vote on a single idea.
- **Hour 0:45-3.** Chats with sponsor engineers, mentors, or attendees are coming back and the team must decide GO, NARROW, or SWITCH, and lock the problem by hour 3.
- **Hour 1-3, in parallel.** You need to know whether the data the problem depends on exists, is legal to use, and actually shows the signal before you commit the architecture.
- **Hours 6 and 12.** A 15-minute check-in: a sponsor rep said "that's not really a problem for us," testers shrug, or scope has drifted from the original user.

## Steps
State every choice you make out loud in the form "We chose X because [principle] [citation]." Write it on the lock card.

1. **Rewrite each target sponsor prompt (hour 0, 15 min).** Classify it as pain, goal, or solution. Most sponsor briefs are goals or disguised solutions, so restate the goal one level up ("what is that for?") [What's Your Problem?, p.85-91] [What's Your Problem?, p.136-140]. Ask the sponsor rep one question: "What would make this a win for you?" [What's Your Problem?, p.223-229].
2. **Put 3 candidates on the board that differ in kind, never 1 (hour 0:15-0:45).** Different users or different pains, not three UIs for one idea. For each, write "[who] at [where] who currently [workaround]" [The Mom Test, p.97-101]. If nobody can name a real person who has it, drop it.
3. **Run four 5-minute filters on each.** (a) Tarpit: search Devpost and GitHub for past attempts and name why they did not stick [Seed: D. Choosing the right problem (startup lens), §D2]. (b) Hammer: are we shaping this to fit a tool we like? [What's Your Problem?, p.116-120]. (c) Data: can you open the needed data in the next 30 minutes? Records requests take weeks, so they never count [Seed: 0. Synthesis / Playbook, §2] [Data Journalism Handbook, p.43]. (d) Demo: can the "after" be shown live in about one minute?
4. **One reframe loop on the top 2 (10-15 min, timer on).** Ask what is missing from the statement (other users, earlier steps, incentives). List the three levers: change reality, change perception, change the desire [Are Your Lights On?, p.29-31]. Keep the framing that is cheapest to demo and most visible to a judge.
5. **Write pass criteria on the whiteboard BEFORE the first chat.** "At least 3 of 5 real target users describe a specific recent instance AND an existing workaround, tool, or spend" [Continuous Discovery Habits, p.141-142]. Write the kill rule too: "If 3 of the first 5 show no workaround or urgency, we switch by hour 3" [The Mom Test, p.43-45].
6. **Split the team for the evidence loop (hour 0:45-2:30).**
   - Pair A: 5-8 casual chats, 5 minutes each, using "tell me about the last time..." plus one question that could kill the idea. Sponsor engineers first; they are both users and judges [Seed: E. Finding problem evidence fast (for the event), §E3].
   - Pair B, person 1: stopwatch the current workflow end to end (friction log), circling tool switches, hand-copied data, and waiting. This produces your "before" number [Mapping Experiences, p.283-285].
   - Pair B, person 2: data check. Follow the acquisition order (sponsor data, official API, open portal, curated repo with provenance, polite scrape, own collection, labeled synthetic) [Seed: 0. Synthesis / Playbook, §2]. Ask the sponsor table first. If 15 minutes of searching finds nothing, plan to hand-build the data or use a proxy and write what the proxy misses [Seed: A. Hackathon Kit, §A2]. Load it and plot the key variable within 20-30 minutes; if the signal the idea needs is not visible, switch data or idea before hour 6 [Elements of Data Analytic Style, p.8-12, p.92].
   - Tag every note F (fact), C (compliment), H (hypothetical), I (idea). Only F lines count [The Mom Test, p.24-25].
7. **Debrief every 2-3 chats (5 min).** Tally against the pass criteria. Each person names one surprise. An empty surprise list means nobody was listening.
8. **Decide at hour 2:30-3.**
   - **GO:** pass criteria met, the pain heard from 2+ independent people, a "before" number from the stopwatch, data in hand, named sponsor fit.
   - **NARROW:** answers are scattered across user types. Keep the subgroup with the strongest emotion and workaround. Do not add interviews [The Mom Test, p.93-97].
   - **SWITCH:** kill rule triggered. Move to the runner-up; do not go hunting for one supporter.
   - **DIG FIRST:** a flat "no" can hide one buildable wedge. Ask which single part they would still hand off [Continuous Discovery Habits, p.167-168].
   - Any stalled argument: 5 minutes, then the named decision owner rules [Sprint, p.73-74].
9. **Lock (hour 3).** Fill the lock card below. Run a 5-minute pre-mortem: "It is judging and we flopped. Why?" Put 15-minute problem check-ins at hours 6 and 12 with a named owner [What's Your Problem?, p.250-254]. After about hour 16, do not reopen the problem; only reword it [Are Your Lights On?, p.54-58].

## Template
Copy into the team doc. Fill one column per candidate, then the lock card for the winner.

```
CANDIDATE BOARD (hour 0:45)                     | Cand A      | Cand B      | Cand C
Kind of difference (user / pain / moment)       |             |             |
"[who] at [where] who currently [workaround]"   |             |             |
Prompt type (pain / goal / solution)            |             |             |
Tarpit: prior Devpost/GitHub attempts + why died|             |             |
Hammer check: framed to fit a tool? (Y/N)       |             |             |
Data: best source + license + in hand by hour?  |             |             |
Live "after" demoable in ~60 s? (Y/N)           |             |             |
Sponsor fit + rep's "win" answer                |             |             |
Biggest risk: market (do they care) / product   |             |             |

PASS CRITERIA (write before chat #1)
GO if >= 3 of 5 real target users: recent specific instance + workaround/spend
SWITCH if 3 of first 5: no workaround, no urgency   -> switch by hour 3
Kill question we will ask: ______________________

EVIDENCE TALLY            | Who (role, not a friend?) | Last-time story? | Workaround? | Quote (verbatim)
1                         |                           |                  |             |
2 ...                     |                           |                  |             |
Online signal: threads __, upvotes __, comments __, subreddits __, within 90 days? __

LOCK CARD (hour 3)
Problem: "The problem is that [person] in [situation] ___________"   (no tech, no feature)
POV: [user] needs to [verb] because [surprising insight]
Why it persists (root cause chain, each why with evidence):
  why 1 ____ (source)  why 2 ____ (source)  why 3 ____ (actionable, not "human error")
Lever we pull: reality / perception / desire
Replaces: ________ (incl. spreadsheet, group chat, doing nothing)
Before number (stopwatch, n=__): ____ min, ____ steps, ____ tools, ____ handoffs
After metric we will show live: ____
Data card: source, license, date pulled, rows, known gaps, synthetic parts labeled
Best outside stat: traced to original? Y/N   definition in one line: ____
Three ways we could be wrong: 1.__ 2.__ 3.__
Decision: "We chose __ because __ [citation]."
Check-ins: hour 6 owner __, hour 12 owner __. Frozen after hour 16.
```

## Principles
1. **Hold three candidates that differ in kind; never vote yes/no on one idea.** Nutt's research found single-option decisions wrong more than half the time versus about a third with multiple options. (counterintuitive) [What's Your Problem?, p.52-53]
2. **No existing workaround means a complainer, not a customer.** If someone with an "awful" problem never Googled, hacked a spreadsheet, or paid, the pain is cheap talk; the workaround is your real competitor. [The Mom Test, p.19-20] [Competing Against Luck, p.24-26, p.103-104]
3. **Only past behavior is evidence: ask about the last time, never "would you."** Direct questions get coherent invented reasons, and "I would definitely buy that" cost Fitzpatrick about $10M. Baseline questions like "what's the most tedious part of your week?" invite this. (counterintuitive) [The Mom Test, p.29-30] [Continuous Discovery Habits, p.64-69]
4. **Set numeric pass and kill criteria before the first conversation.** Pre-set counts block the team from reading every chat as a yes. [Continuous Discovery Habits, p.141-142] [The Mom Test, p.43-45]
5. **Scattered answers mean narrow the segment, not more interviews.** Twenty must-haves from twenty chats is one chat each with twenty user types. (counterintuitive) [The Mom Test, p.93-97]
6. **Measure the "before" yourself; a searched stat is the weakest evidence.** Own observed measurement sits near the top of the evidence ladder and an unverified stat near the bottom; a stopwatched current workflow gives the judge-memorable delta. This corrects the baseline's "one quick stat is enough." (counterintuitive) [Seed: A. Hackathon evidence kit, §A1] [Mapping Experiences, p.283-285]
7. **Trace any outside stat to its original and write its definition, or drop it.** Zombie stats lose their caveats as they spread, and most number disputes are definition disputes. [Calling Bullshit, p.110-112]
8. **Prove the data shows the signal before committing.** Wanting an answer does not make the dataset contain one; a 20-30 minute load-and-plot test decides it. [Elements of Data Analytic Style, p.8-12, p.92]
9. **A missing dataset or a two-source join can be the unique angle.** Hand-built data (under about 200 rows, split among teammates) is something competitors cannot copy, and overlaying two sources on one key found 7,000 illegally planted hectares; frame the problem around that overlap number. (counterintuitive) [Data Journalism Handbook, p.45-49, p.47-48] [Data Journalism Handbook, p.26-27]
10. **Change perception, not only reality.** A problem is the gap between desired and perceived; the slow elevator was fixed with mirrors, and a perception fix is often the only thing buildable in 24 hours. [Are Your Lights On?, p.29-31]
11. **Delete a step before you automate it.** Technology applied to a step the user does not care about misses the problem; ask that of every AI feature. (counterintuitive for AI projects) [Mapping Experiences, p.280-283]
12. **Who you asked beats how many.** Size shrinks random error, not bias; fellow hackers skew young and technical and are not your users unless they are the segment. [How to Make the World Add Up, p.136-137] [Quantifying the User Experience, p.26-28]

## Mistakes
- **Tech-first idea.** Sign: the first sentence names AI, AR, or the sponsor API. Fix: write "who has this problem and what do they do today?"; if no name, drop or reframe.
- **Single-option vote.** Sign: "should we do X?" Fix: three candidates of different kinds on the board before anyone votes; the loudest advocate argues for the second-best option for 5 minutes [Continuous Discovery Habits, p.108].
- **Scoring grid as the decider.** Sign: the baseline's 1-5 checklist sums settle the choice. Fix: use scores only as a gate on evidence strength; choose by debating how many and how often, team skill plus sponsor fit, and importance versus dissatisfaction with current options [Continuous Discovery Habits, p.103-106].
- **Loud mistaken for large.** Sign: one viral thread or a "DISASTER" quote drives the pick. Fix: require 4-5 signals (100+ upvotes, 50+ comments, multiple threads, more than one subreddit, within 90 days); 1-2 is weak [Seed: E. Finding problem evidence fast (for the event), §E2].
- **Silence read as no problem.** Sign: "nobody complains about it." Fix: ask "what do you do to work around X?" and "what do you avoid because of it?"; users blame themselves and adapt [Are Your Lights On?, p.70-73].
- **Root cause stops at a person.** Sign: chain ends in "users are lazy" or "human error." Fix: ask what incentive or setup produces that behavior, with evidence at each why [Seed: C. Root cause analysis, §C1].
- **Data assumed, not checked.** Sign: architecture drawn around a dataset nobody has opened. Fix: the step 6 data check, and cache the first pull to disk so the demo never depends on a live third-party API [Seed: 0. Synthesis / Playbook, §3].
- **Ignoring the sponsor's "not a problem for us."** Sign: the team keeps going after a sponsor engineer shrugs. Fix: re-check the choice before hour 3 [Sprint, p.30].

## Hackathon calibration
- **Compress cadence, keep the method.** Weekly interviews and "a week or two of conversations" become 2-3 hours of 5-minute chats, done by hour 3 [The Mom Test, p.115]. The baseline's 60-90 minute cap is right for the first framing, not for the evidence loop; start the feasibility spike in parallel so building is not blocked.
- **Commitments without cash.** Deposits and LOIs do not fit 24 hours. Ask for time and reputation: a named quote, an intro to a colleague, an email for tonight's link, a real task done with the prototype before judging [The Mom Test, p.67-69, p.72].
- **Skip the slow tools.** Fault trees take half a day or more; skip them. A fishbone becomes a 15-minute whiteboard pass, logic trees max 3 levels [Seed: C. Root cause analysis, §C3]. Market sizing gets one honest bottom-up line, not a TAM slide.
- **Lock dates, not depth.** Reframe in 5-15 minute loops tied to real contact rather than long analysis [What's Your Problem?, p.63-71]. Reopen the problem at hours 6 and 12 only; after hour 16 you may reword it for the pitch but not change it.
- **Ask a judge-ready "why hasn't anyone solved this?"** The root cause chain is that answer and feeds viability and impact. Simple answers get disbelieved, so pair a simple fix with one technically deep element and say what you ruled out [Are Your Lights On?, p.48].
- **Prefer local, reachable data and users.** Dallas OpenData and the Texas Open Data Portal have per-dataset Socrata APIs; a segment at UT Dallas or the venue lets you test in person [Seed: A. Hackathon Kit, §A2].
- **Ethics check on data.** Ask "would we be comfortable telling judges and the people in it where this data came from?" [Are Your Lights On?, p.47-50].

## Go deeper
- [../domains/02-problem-discovery.md](../domains/02-problem-discovery.md)
- [../domains/03-user-research.md](../domains/03-user-research.md)
- [../domains/04-workflow-friction.md](../domains/04-workflow-friction.md)
- [../domains/05-evidence-quant-research.md](../domains/05-evidence-quant-research.md)
- [../domains/16-data-acquisition.md](../domains/16-data-acquisition.md)
- search_experts("three options that differ in kind single option decision error", domain="02-problem-discovery")
- search_experts("complainer versus customer existing workaround", domain="02-problem-discovery")
- search_experts("pass criteria counts not percentages assumption test", domain="02-problem-discovery")
- search_experts("time each step before after minutes vehicle inspection registration", domain="04-workflow-friction")
- search_experts("build your own dataset when none exists verify second source", domain="16-data-acquisition")
- search_experts("trace statistic to original source definition", domain="05-evidence-quant-research")
