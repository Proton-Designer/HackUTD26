---
name: 02-problem-discovery
description: Open when choosing or locking the problem in hours 0-3, rewriting a sponsor prompt as a user problem, judging whether interview or Reddit evidence is real, explaining why the problem persists (root cause), or running the hour 6/12/18 "is this still the right problem?" check-ins.
---
# Problem discovery, framing, and identifying root causes

## Use this when
- Hour 0-1: sponsor challenges are out and the team is about to pick an idea, or someone says "let's build an app that uses X."
- Hour 1-3: deciding whether early conversations, reviews, or Reddit threads prove a real, painful problem, or only compliments.
- A sponsor prompt or mentor suggestion arrives phrased as a method or a feature ("use our API to...", "make X faster").
- Writing the problem sentence, POV, or the pitch's "why this problem / why existing tools fail" answer.
- Mid-build (hours 6, 12, 18): feedback is mixed, a test flopped, or scope has drifted from the original user.

## Core principles
1. **Test the problem before the solution, and try to prove the framing wrong.** Solution testing builds momentum that has nothing to do with whether the problem is real; a pain heard in every interview can still be one users reject help for (Simply Business: late payments everywhere, but owners refused third-party collection). [What's Your Problem?, p.234-237] [Continuous Discovery Habits, p.163-165]
2. **Never decide "this idea or not"; hold three candidates that differ in kind.** Nutt's research: single-option decisions are wrong more than half the time versus about a third with multiple options; fifteen elevator vendors is still one option. [What's Your Problem?, p.52-53] [Continuous Discovery Habits, p.31-32]
3. **Only past behavior counts as evidence; ask "tell me about the last time..." (counterintuitive).** Direct questions get coherent invented reasons (the jeans buyer said fit; her real purchase was brand plus a sale), and "I would definitely buy that" cost Fitzpatrick roughly $10M. [Continuous Discovery Habits, p.64-69] [The Mom Test, p.29-30]
4. **No existing workaround means a complainer, not a customer.** If someone with an "awful" problem has not Googled, hacked a spreadsheet, or spent money, the pain is cheap talk; the real competitor is that workaround or doing nothing. [The Mom Test, p.19-20] [Seed: B. Framing and reframing, §B3]
5. **Reframe in short 5-15 minute loops, not long analysis (counterintuitive).** "Spend 55 of 60 minutes defining the problem" is misattributed and produces paralysis; Frame, Reframe, Move Forward, then repeat after real-world contact. [What's Your Problem?, p.63-71] [Are Your Lights On?, p.21]
6. **Look outside the frame before digging inside it.** The mind frames one slice automatically (13 ships, not 7, because ships already at sea were left out); ask what is missing: other users, earlier events, existing tools, incentives. [What's Your Problem?, p.111-115]
7. **A problem is the gap between desired and perceived, so list all three levers.** You can change reality, change perception, or change the desire; the elevator was fixed with mirrors, and a perception fix is often the only thing buildable in 24h. [Are Your Lights On?, p.29-31] [Seed: B. Framing and reframing, §B1]
8. **Pick one user and one moment, then solve a leaf completely.** Teams that circled one actor and one moment on the map (Savioke: hotel guest at delivery) got clean tests; broad parents stay intractable, so pitch the big problem and demo one leaf. [Sprint, p.68-71] [Continuous Discovery Habits, p.88-90]
9. **Frame the goal as a countable change in user behavior, not an output.** "More course reviews" failed because reviews piled up on unviewed courses; the metric you claim must be observable live in the demo (time saved, steps removed, accuracy on a test set). [Continuous Discovery Habits, p.42-43, p.50]
10. **A tech, feature, or sponsor-API starting point is a solution hiding a problem.** Classify the start as pain point, unreachable goal, or beloved solution; the third is hardest to diagnose, and a sponsor brief is usually type 2 or 3. [What's Your Problem?, p.85-91] [Seed: D. Choosing the right problem (startup lens), §D1]
11. **Root causes need evidence at every "why" and must stop at something you can act on.** Untrained teams guess each why; never stop at "human error," and switch to a fishbone when causes do not form one chain. [Seed: C. Root cause analysis, §C1] [Seed: C. Root cause analysis, §C3]
12. **Weigh demand by what people give up, not what they say.** Compliments cost nothing; time, reputation, or cash commitments filter real interest (Managed by Q: 1 of 20 boards signed versus 18 of 25 office managers, so they switched segment). [What's Your Problem?, p.244-248] [The Mom Test, p.67-69]

## Decision procedure
Main decision: which problem to commit to, locked by hour 3, with scheduled re-checks.

1. **Read and rewrite the prompts (hour 0, 15 min).** Copy each target sponsor's rules verbatim as boundaries, plus "must work live in the demo" [Bulletproof Problem Solving, p.70-72]. Classify each prompt (pain / goal / solution) and restate its goal one level up ("what is that for?") [What's Your Problem?, p.136-140]. Circle tricky words ("all," "or," "may," "too") and ask the sponsor engineer one clarifying question per ambiguous sentence [Are Your Lights On?, p.87-88]. Ask the rep "what would make this a win for you?" [What's Your Problem?, p.223-229].
2. **Generate at least 3 candidates that differ in kind (hour 0:15-0:45).** Sources in priority order: team expertise and problems members personally hit (list every job and internship) [Seed: D. Choosing the right problem (startup lens), §D1]; sponsor booth conversations [Seed: E. Finding problem evidence fast (for the event), §E3]; review and Reddit mining [Seed: E. Finding problem evidence fast (for the event), §E1-E2]. For each, write "The problem is that..." as a full sentence plus who is involved [What's Your Problem?, p.82-84], and the who-where-workaround line: "[who] at [where] who currently [workaround]" [The Mom Test, p.97-101]. If no one can name a real person with the problem, drop it.
3. **Quick filters per candidate (5 min each).** Tarpit: search Devpost, GitHub, app stores for prior attempts and name why they failed [Seed: D. Choosing the right problem (startup lens), §D2] [Sprint, p.58-59]. Hammer: are we framing this to fit our favorite tool? [What's Your Problem?, p.116-120]. Whose problem: user, buyer/sponsor, operator rows; if they conflict, pick one and say so [Are Your Lights On?, p.22-28].
4. **One reframe loop (10-15 min, timer).** For the top 2 candidates run: what is missing from this statement; try another category (usability vs incentive vs emotion: Nickelodeon got 10x sign-ups by treating a password step as an emotional problem); bright spots (when is the problem absent?); the three levers. Keep 2 framings each and choose the one cheapest to demo and most visible to judges [Seed: B. Framing and reframing, §B1] [What's Your Problem?, p.51-52].
5. **Pre-register pass criteria, then gather evidence (hour 0:45-2:30).** Before the first conversation, write on the board as counts: "At least 3 of 5 real target users describe a specific recent instance AND an existing workaround, tool, or spend" [Continuous Discovery Habits, p.141-142]. Run 5-8 casual 5-minute chats using "last time" prompts and one scary question that could kill the idea [The Mom Test, p.42-43, p.58-63]. In parallel, one teammate mines 20-30 one-to-three-star reviews of 3-5 existing tools and runs pain-phrase searches ("I wish there was a tool that...") [Seed: E. Finding problem evidence fast (for the event), §E1-E2]. Tag every note F (fact), C (compliment), H (hypothetical), I (idea); only F lines enter the decision [The Mom Test, p.24-25].
6. **Score the online signal.** Reddit intensity: 100+ upvotes, 50+ comments, multiple threads, more than one subreddit, posted within 90 days; 4-5 signals is validated, 1-2 weak. Rubric of 5 factors at 1-10 each: 35+ build, 20-35 track, under 20 drop [Seed: E. Finding problem evidence fast (for the event), §E2].
7. **Compare candidates, do not stack-rank.** Debate the survivors on four lenses: how many and how often, table stakes vs differentiator, team skill plus sponsor fit, and importance versus dissatisfaction with current options [Continuous Discovery Habits, p.103-106]. The loudest advocate argues for the second-best option for 5 minutes [Continuous Discovery Habits, p.108].
8. **Stop/go rules.**
   - GO: pass criteria met, need heard from 2+ independent people [Continuous Discovery Habits, p.92], a root-cause chain with evidence at each step, a live-demoable metric, and a named sponsor fit.
   - NARROW: answers are scattered across people; narrow the segment instead of adding interviews [The Mom Test, p.93-97].
   - SWITCH: 3 of the first 5 real users show no workaround or urgency; switch by hour 3, do not hunt for a supporter [The Mom Test, p.43-45].
   - DIG FIRST: a shallow "no" may hide a buildable wedge (FCSAmerica: customers wanted their loan officer, except for "what can I afford?") [Continuous Discovery Habits, p.167-168].
   - Any stalled argument gets 5 minutes, then the named Decider rules [Sprint, p.73-74].
9. **Lock and schedule (hour 2:30-3).** Write the POV ("[user] needs to [verb] because [surprising insight]") and 3-5 HMW questions [Seed: B. Framing and reframing, §B2]. Run a 5-minute pre-mortem phrased as certain failure ("it is demo day and we flopped; why?") [Continuous Discovery Habits, p.130]. Classify the top risk: market risk gets more conversations, product risk gets a feasibility spike first [The Mom Test, p.52-56]. Put 15-minute problem check-ins on the clock at hours 6, 12, 18 with a named owner [What's Your Problem?, p.250-254]; stop reopening the definition after about hour 16 [Are Your Lights On?, p.54-58].

## Checklists

**Problem statement check (run on your own sentence)**
- [ ] Names a person, a situation, and a pain; not a goal like "more revenue" or a catch-all like "culture" [What's Your Problem?, p.86-87].
- [ ] Contains no feature, technology, or implied fix ("lack of a tool for...") [What's Your Problem?, p.94-96].
- [ ] Admits more than one solution; if it implies exactly one build, rewrite it [Continuous Discovery Habits, p.98-99].
- [ ] Phrased so a real user could say it out loud [Continuous Discovery Habits, p.96-98].
- [ ] Outcome-focused, specific, time-bound, aligned with judges plus sponsor criteria, open to creative solutions, at the highest level you can act on [Bulletproof Problem Solving, p.67-68].
- [ ] You can name three ways your understanding could be wrong [Are Your Lights On?, p.68].
- [ ] Every statistic on it has a known source ("how do we know this is true? compared to what?") [What's Your Problem?, p.92-93].

**Evidence audit (before saying "we validated it")**
- [ ] They talked more than you (target about 80%) [The Mom Test, p.39-41].
- [ ] You asked at least one question you were scared of [The Mom Test, p.113].
- [ ] Evidence is past actions and commitments, not "X of 10 said they'd use it" [The Mom Test, p.29-30].
- [ ] At least 3 verbatim quotes recorded with names for the pitch [The Mom Test, p.109-112].
- [ ] Interviewees matched the persona; other hackers count only if they are the user [Sprint, p.153-154].
- [ ] An unexpected answer actually changed something in the plan [The Mom Test, p.113].

**Root cause check**
- [ ] Problem stated as what, where, when, how you know [Seed: C. Root cause analysis, §C1].
- [ ] Each "why" backed by a log, quote, review, or observation; none stop at a person [Seed: C. Root cause analysis, §C1].
- [ ] Multiple causes? Fishbone with People / Process / Tools / Data / Environment / Measurement, each cause marked verified, suspected, or ruled out [Seed: C. Root cause analysis, §C3].
- [ ] One possible confounder named and how you checked it [What's Your Problem?, p.120-125].
- [ ] The cause explains why existing alternatives still fail, and your fix acts on it within 24h.

## Anti-patterns
1. **Tech-first idea.** Tell: the first sentence names AI, AR, or the sponsor API. Fix: write "who has this problem and what do they do today?" in one sentence; no name, drop or reframe [What's Your Problem?, p.89-91] [Seed: 0. Synthesis: the playbook, §2].
2. **Counting opinions as demand.** Tell: notes say "loved it" or "would definitely use." Fix: reply "how do you handle this today?" and report current behavior, spend, and commitments [The Mom Test, p.25-29].
3. **Framing paralysis.** Tell: problem talk passes an hour with no decision. Fix: write the current best definition at the timebox and revisit at the next check-in [Are Your Lights On?, p.21].
4. **Single-option vote.** Tell: "should we do X?" Fix: put three candidates of different kinds on the board before any vote [What's Your Problem?, p.52-53].
5. **Disguised solution as problem.** Tell: the "need" can only be met one way ("let me fast-forward ads"). Fix: restate as the need ("I do not like commercials") [Continuous Discovery Habits, p.98-99].
6. **Fuzzy segment.** Tell: every chat produced a different must-have feature. Fix: keep the user type with the strongest emotion and workaround and cut features only others asked for [The Mom Test, p.93-97].
7. **Stopping at a symptom or a person.** Tell: chain ends in "users are lazy" or "human error." Fix: ask what incentive or setup produces that behavior; the knowledge platform failed on job-protection incentives, not usability [What's Your Problem?, p.201-203] [Seed: C. Root cause analysis, §C1].
8. **Loud mistaken for large.** Tell: one dramatic thread or a "DISASTER" quote drives the choice. Fix: ask "what does it cost you, what happens if you do nothing?"; the yeller just threw interns at it [The Mom Test, p.17-18] [Seed: E. Finding problem evidence fast (for the event), §E2].
9. **Silence read as no problem.** Tell: "thousands use it and nobody complains." Fix: ask "what do you do to work around X?" and "what do you avoid because of it?"; users blame themselves and adapt [Are Your Lights On?, p.70-73].

## Hackathon calibration
- **Compress cadences, keep the method.** Torres's weekly interviews and Fitzpatrick's "a week or two of conversations" become 2-3 hours of 5-minute chats; done by hour 3 [The Mom Test, p.115] [Continuous Discovery Habits, p.77-79]. Sponsor engineers are both users and judges, so they are your fastest research [Seed: E. Finding problem evidence fast (for the event), §E3].
- **Commitments without cash.** Aim for time and reputation: a named testimonial, an intro to a colleague, a real task done with the prototype before judging [The Mom Test, p.67-69, p.72].
- **Ignore long-horizon tests.** YC's "work on it for years" and market-size questions barely matter for a 24h build; replace with "why can our team build this convincingly in 24h?" [Seed: A. One-page problem framing worksheet, §Why now / why us]. Skip fault trees (half a day or more) entirely; fishbone becomes a 15-minute whiteboard pass; logic trees max 3 levels in 30 minutes [Seed: C. Root cause analysis, §C3] [Bulletproof Problem Solving, p.85-91].
- **Judges spend about 4 minutes.** The problem must land as one sentence plus one user quote, opened with the user's felt pain, not your features [What's Your Problem?, p.213-222]. The root cause is your answer to "why hasn't anyone solved this?", which feeds viability and impact.
- **Simple answers get disbelieved.** A five-minute solution needed 20 more minutes of explanation to be accepted; show what you ruled out and pair a simple perception fix with one technically deep element for the complexity criterion [Are Your Lights On?, p.48].
- **Ethics check on data.** Absorbing technical problems make teams skip it; ask "would we be comfortable telling judges and the people in it where this data came from?" [Are Your Lights On?, p.47-50].
- **Problem over sponsor stretch.** Fit the sponsor challenge to a real problem; if a sponsor mentor says "that's not really a problem for us," re-check the choice before hour 3 [Sprint, p.30] [Seed: A. One-page problem framing worksheet, §Sponsor fit].

## Where experts disagree
- **Find the root cause vs find a better problem.** Seeds and the team plan say identify root causes with verified 5 Whys [Seed: C. Root cause analysis, §C1]; Wedell-Wedellsborg says stop hunting one root cause because most problems have several causes and framings [What's Your Problem?, p.51-52]. Follow: choose the framing by tractability and demoability, then use a verified why-chain to explain why the problem persists. Judges reward the explanation; they do not require the one true cause.
- **How long to spend defining.** Gause and Conn want deliberate definition before data or code [Are Your Lights On?, p.21] [Bulletproof Problem Solving, p.66]; Wedell-Wedellsborg rejects "55 of 60 minutes" [What's Your Problem?, p.63-64]. Follow: a 30-45 minute first definition, then repeated 15-minute loops tied to real contact. Under a 24h clock, iteration beats upfront depth.
- **Specific and measurable now, or later.** Conn wants a specific, measurable statement at hour 1 [Bulletproof Problem Solving, p.67-68]; Wedell-Wedellsborg says add metrics only once confident it is the right problem [What's Your Problem?, p.105-106], and Torres starts with a learning goal (strong evidence) [Continuous Discovery Habits, p.46-47]. Follow: hour 1 names person, situation, pain with no KPI; add the demoable metric after the first user contact.
- **Numeric scorecard vs judgment lenses.** The seed rubric scores evidence out of 50 with 35+ to build [Seed: E. Finding problem evidence fast (for the event), §E2]; Torres warns scoring creates false precision [Continuous Discovery Habits, p.103-106]. Follow: use the rubric only as a gate on online evidence strength, and use the lenses plus debate to choose between candidates.
- **Open broad vs go narrow.** Fitzpatrick says open interviews broad so your topic appears unprompted [The Mom Test, p.45-52]; Sprint and the seeds say pick one narrow user and moment [Sprint, p.68-71]. Not a real conflict: open each conversation broad, keep the target narrow.
- **Hardest user vs most eager user.** Sprint targets the toughest audience who has never heard of you (opinion) [Sprint, p.69]; Fitzpatrick and Maurya target emotional early adopters who already hack a workaround [The Mom Test, p.75-76] [Seed: B. Framing and reframing, §B3]. Follow: build for the early adopter, since evidence is stronger there; make the demo readable by a cold judge.
- **Describe the problem back vs never mention your idea.** Wedell-Wedellsborg tells stakeholders their problem to test resonance [What's Your Problem?, p.237-241]; Fitzpatrick says mention the idea as late as possible [The Mom Test, p.13-14]. Follow: after the unprompted opening, you may describe the problem; never the product until you ask for a commitment.

## Go deeper
- search_experts("ask about the last time it happened, not hypotheticals", domain="02-problem-discovery")
- search_experts("three options that differ in kind single option decision error", domain="02-problem-discovery")
- search_experts("look outside the frame what is missing reframing", domain="02-problem-discovery")
- search_experts("complainer versus customer existing workaround", domain="02-problem-discovery")
- search_experts("pass criteria counts not percentages assumption test", domain="02-problem-discovery")
- search_experts("choose one target user and one moment on the map", domain="02-problem-discovery")
- search_experts("commitment and advancement time reputation money", domain="02-problem-discovery")
- search_experts("bright spots positive outliers when is the problem absent", domain="02-problem-discovery")
- search_experts("5 whys verify each answer fishbone versus fault tree", domain="02-problem-discovery")
- search_experts("question the goal goal map sponsor challenge", domain="02-problem-discovery")
