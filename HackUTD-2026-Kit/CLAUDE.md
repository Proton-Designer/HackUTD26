# HackUTD 2026 team core (always loaded)

HackUTD 2026, UT Dallas, Nov 7-8: 24 hours, 4 people, about 200 projects. Paths are relative to the kit root. "Seed" = corpus/01-judging/01-hackathon-judging-and-evaluation.

## 1. How judging works here
- **Format:** in-person science fair at our numbered table; judges visit over about 3 hours and we must stay [Seed: A. HackUTD-specific, §A1]. Plan 4 min per judge: 2 demo, 1 Q&A and scoring, 1 travel. 3+ judges per project; finalists, if any, get about 7 min; the video is only a deliberation reference [Seed: B. Standard rubrics and how judging is run, §B2].
- **General track:** uniqueness, technicality, viability, UI & UX design, complexity, usefulness, impact factor [Seed: A, §A3].
- **MLH prizes:** technology, design, completion, learning, equal weight; pitch and originality not scored [Seed: B, §B1].
- **Sponsor tracks:** judged by the sponsor: "if I reward this, will my company look good?" Their tech must carry the core loop; max two tracks [Seed: C. Writeups from judges and repeat winners, §C3] [Seed: A, §A2].
- **Scoring:** likely stack ranking: each judge names a top 3 (3/2/1 points). Forgettable scores zero, so aim for every judge's top 3 [Seed: B, §B2].

## 2. Hour checkpoints (H0 = hacking starts; act on the trigger, not the mood)
- **H0:10** Devpost project created, all 4 invited, public repo (kickoff).
- **H1:30** Idea locked by the Decider, noise audit passed. Hard stop H3 (kickoff).
- **H2** Each integration returned 1 real response, else drop it unless core or sponsor-required (scoping).
- **H3** Riskiest spike got real data inside the app, stack and schema locked; else swap or fake it (architecture).
- **H3:30** Walking skeleton live on a public URL; else all 4 stop features and fix deploy [Seed: E. Walking Skeleton, §E].
- **H6** Differentiator gives real output on real input, deployed; else one 60-min alternative, then re-plan (build-test).
- **H8** Thin slice runs end to end; else cut to the surviving path. Last hour for a full pivot (scoping).
- **H9-10, H18-19** Stranger tests, 3 people; fix what 2 of 3 hit (build-test).
- **H12** Full path live on the deployed URL; else stop new work and cut to what runs. After H12, zoom-in pivots only (pitch-demo).
- **H14** Feature freeze; new ideas go to the roadmap list (scoping). **H16** unfinished stretch work is cut, not demoed (pitch-demo).
- **H18** Code, prompt, model frozen; fix only demo-visible bugs. Core not live by H19: mock or record it (kickoff).
- **H20** Demo deployment frozen; anything still uphill is cut to its fallback (scoping).
- **H20-23** 5+ timed rehearsals; demo path 10 runs from reset (pitch-demo, build-test).
- **Any hour** Half the time gone, a third done: cut now (scoping).

## 3. Rules that beat instinct
1. Strike your first 6-8 ideas; other teams have them too [Where Good Ideas Come From, p.34-35, p.106-107; Noise, p.30].
2. Use the sponsor API for a job it was not built for [Where Good Ideas Come From, p.118-119, 123-125].
3. Never vote yes/no on one idea; hold 3 that differ in kind [What's Your Problem?, p.52-53].
4. Only past behavior is evidence; ask "last time", never "would you" [The Mom Test, p.29-30].
5. The competitor is today's workaround, not a startup [Obviously Awesome, p.39, p.63-65].
6. Private noise audit before code; a 25-point spread means stop [Kahneman et al., Noise, p.28-29, 32-33].
7. Budget 40-48 real person-hours; Musts get half [Brooks, Mythical Man-Month, p.109].
8. Split by vertical slice plus mocked contracts, not by layer [Singer, Shape Up, p.96-97].
9. Scariest unknown first; solved means real data in our app [Shape Up, p.111-112, p.139].
10. Never more services than people [Brooks, Mythical Man-Month, p.110].
11. Agents lose demos; use a fixed 2-4 call chain [Huyen, AI Engineering, p.539].
12. Small samples as counts ("6 of 8"), never percentages [Quantifying the User Experience, p.26, p.37-42].
13. Payoff screen up before 0:40 [Seed: Great Demo: method in one page, §0].
14. Demo the hardest real input; let the judge verify one claim [Made to Stick, p.138-145].
15. Name your biggest weakness before the judge does [Never Split the Difference, p.55-59].
16. Same objection from 2 judges: fix the pitch, not the rebuttal [SPIN Selling, p.147-148, p.163-167].

## 4. Router
- Roles, Decider, tracks, clock -> decisions/kickoff.md
- Problem, users, data check -> decisions/problem-discovery.md
- Generating ideas -> decisions/ideation.md
- Choosing or pivoting -> decisions/idea-selection.md
- One-liner, USP, "how is this different" -> decisions/value-prop.md
- Sizing, cutting, admitting a feature, checkpoints -> decisions/scoping.md
- Stack, data, AI pattern, deploy -> decisions/architecture.md
- Building, evals, freeze, hardening -> decisions/build-test.md
- Demo script, rehearsal, table -> decisions/pitch-demo.md
- Judge questions -> decisions/judge-qa.md
- Stuck, deadlock, sleep, booth roles -> domains/18-team-execution.md
- Rubric detail, past winners -> domains/01-judging.md
- Review an idea, scope, script or Devpost text -> agents/judge-critic.md
- Need evidence -> search_experts tool

## 5. Decision rule
For idea choice, scope cuts, architecture and pitch structure, say "We choose X because <reason in plain words>; cost Y; fallback Z" and log it in the pinned decision doc [Richards and Ford, Fundamentals of Software Architecture 2e, p.697-698]. A settled call reopens only when a written trigger fires. Small steps need no ceremony.

**Use the kit to inform the answer, not to perform it.**
- Start from the team's actual situation: their names, skills, current hour, what is broken. Every recommendation must fit those facts; tailoring beats any rule.
- Give the team the output (the decision, the plan, the script, the exact words), not the method. Do not hand them rituals, gate codes, scoring schemes or probability math unless they asked for a process or it clearly pays off in the time they have.
- Plain language. No internal labels (G2, H3:30, "noise audit") the team has not seen. At most one short citation per major decision, only when it changes their mind.
- Checkpoints are relative: if the team is already past one, say what to do now, not what they missed.
- Feasibility first: never rank an idea above the team's real skills or the clock.
- Never invent facts, user stories, quotes or numbers. Use placeholders the team must fill.

## 6. Event specifics (TEAM FILLS from separate research; max ~300 tokens; blank = unknown)
- H0 clock time: Sat Nov 7, 12:00 PM CT  Hacking ends: Sun 12:00 PM (assumed = final submit; not published)  Judging window: Sun 1:00-4:00 PM, ECSW + ECSS (site); info desk says a big lecture hall, room/table TBD
- Devpost registration: Sat 11:00 PM (initial)  Final submit: Sun 12:00 PM (we submit 11:30) [zeroday.hackutd.co]
- Minutes per visit: about 4 (confirmed by info desk; split 2 demo / 1 Q&A / 1 travel)  Finalists: none, one judging round (info desk, 00:20)  Theme: Zero Day
- Closing: Sun 5:00-6:00 PM, ATEC Auditorium
- Sponsor tracks (name | wants | judge | prize): T-Mobile Safe Signal | protect customers before/during/after, beyond classification, honest confidence, privacy by design, synthetic data only | creativity, impact, usability, security+privacy, detection quality | prize TBD (ask booth) ;; NVIDIA | Nemotron beyond a chatbot: multi-step agents, tool integration, real-world use | 1st: 2x RTX 5080 + $200 Brev; 2nd: 1x RTX 5080 + $200 Brev + swag
- MLH prizes in play: ____ (check Devpost prize list)
