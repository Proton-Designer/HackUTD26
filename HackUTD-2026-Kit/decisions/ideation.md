---
name: ideation
description: Load at hour 0:30-2:00 when the team generates candidate solutions after sponsor kickoff, when every candidate looks like the obvious sponsor-prompt app, when the team has circled the same 2-3 ideas for 20+ minutes, or mid-build when a surprise or 3 AM idea tempts a change of course.
---
# Decision guide: ideation

## Open this when
- **Hour 0:30-1:00.** Sponsor tracks and APIs are announced, a rough problem frame exists, and the team is about to start throwing out ideas. Shortlist due by hour 2:00, lock by 3:00, hard stop at 4:00.
- **Hour 1:00-2:00.** The board has ideas, but they read as "X but smarter with AI," or they match what the sponsor prompt suggests on first read (what ~200 other teams will also build).
- **Any time in hours 0-3.** The same 2-3 ideas keep coming back for 20+ minutes, or two teammates have argued about direction for more than 5 minutes.
- **Hours 8-16.** An odd model output, a surprising bug, or an overnight idea makes someone want to change course.

## Steps
Total budget is about 90 minutes of generation and filtering. Put a visible timer on every step. The output is 3-5 shortlisted concepts handed to idea selection, not a final pick.

1. **Test the frame first (10 min).** Write 3 how-might-we (HMW) questions with any solution form removed (no "dashboard," "chatbot," "app"). For each, list 5 different solutions in 3 minutes. If you cannot reach 5, the frame is too narrow or too vague, so rewrite it. On a sponsor track, keep the sponsor's stated requirement as the core and reframe only around it. Add two lines: "Not in scope:" and "Constraints that are really assumptions:".
2. **Build the parts table (15 min).** List every sponsor API or dataset, each model API, any hardware, each member's strongest skill, and 3-5 real annoyances per member (things that actually happened to them, not hypotheticals). For each sponsor API, write the intended use plus 3 unintended uses, with at least one aimed at a different audience. Each idea should combine 2-3 parts from this table.
3. **Lightning demos (about 20 min).** Each person shows 1-2 products from *other fields* that solved the same underlying structure (matching, triage, trust, handoff, filtering), at 2 minutes each. Write down the mechanism (the "big idea"), not the product name. Do not demo competitors.
4. **Generate alone, then share, then alone again (25-35 min).** Do 10 minutes of silent solo writing, then read ideas aloud with no critique, then do another solo round to build on what was heard. Optional: 4-3-5 brainwriting (3 ideas per sheet, pass it on, build on the previous sheet, 15 min). **Number every idea in the order it was written.**
5. **Run one prompt round (10-20 min). Pick one technique:**
   - Assumption reversal: each person lists 5 assumptions about the user, workflow, or product format, flips each one, and asks "how could the opposite work?"
   - Idea Box: 4 parameters (for example user, input, output, channel) with 5 variations each. Keep a parameter only if the challenge would disappear without it. Each person draws 5 random combinations.
   - TRIZ contradiction: "If we improve X, Y gets worse." Then picture the ideal final result: the job gets done without this step existing.
   - Three levers: change the reality, the perception, or the desire. A perception fix is often the only thing you can build in 24h.
   - **Go/no-go gate:** move to step 6 only when the board has **20+ ideas and at least 3 came from a prompt technique or a cross-field analogy**. Otherwise run another round.
   - **Stuck rule:** if the team has circled the same 2-3 ideas for 20 minutes, do not think harder. Add parts: an outsider's view, an obscure API, or a non-tech workflow.
6. **Strike ideas #1-#8 (2 min) (counterintuitive).** Cross out the first 6-8 numbered ideas and any idea that is the first thing the sponsor prompt suggests. If a struck idea still pulls at the team, keep only its 3rd or 4th variant.
7. **Rewrite test (5 min).** Rewrite each surviving one-liner without "better," "faster," "smarter," or "AI-powered," and name the job the user can now do that was impossible before. If nothing distinctive remains, or no new job exists, drop the idea. Also ask whether ChatGPT could do this in one prompt. If yes, name what survives a model upgrade (workflow, data, integration), or drop it.
8. **Dot only demoable cores (5 min).** Everyone dots silently, but only on ideas whose core loop could be demoed in about 4 hours. Keep 3-5 that **differ in kind**: three variants of one interface count as one option.
9. **Check dependencies and prior art (5 min per idea).** List 3-5 load-bearing dependencies and mark each "exists and we have access" or "must build." **More than one must-build outside the core novelty means reshape or drop.** Search Devpost (the idea plus the sponsor challenge) and past HackUTD galleries. If a polished product already solves the same problem for the same audience, change the audience or the angle, not the features. If the sponsor already sells it, extend it instead.
10. **Make each finalist concrete and anonymous (15 min).** Draw a 3-panel storyboard for each finalist: pain moment, key interaction, result, with real on-screen text. Judge with silent dots while the author stays quiet. Then one assigned dissenter spends 5 minutes arguing against the favorite and for a very different alternative.
11. **Walk, then hand off (15-20 min).** Take a short walk away from the board before the selection vote. Then pass the shortlist to the idea-selection guide (equal-weight 1-5 scorecard, where any score of 1 eliminates an idea, and the named Decider breaks ties).
12. **State the decision.** Write the decision line in the template naming the principle and citation behind it. Photograph the board and save the parking lot.

**Mid-build (hours 8-16):** If a model or API does something unexpected, spend up to 10 minutes asking "is this the interesting part?" before you suppress it. A new idea after lock goes to the parking lot unless it cuts scope or de-risks the riskiest assumption.

## Template
```
IDEATION BOARD          start __:__   shortlist due __:__ (by hour 2)   lock __:__ (by hour 3)

FRAME
HMW (no solution form): ______________________________________
Five-solutions test: 1.____ 2.____ 3.____ 4.____ 5.____   pass? Y/N
Reframe A: ____________________   Reframe B: ____________________
Sponsor requirement kept as core: ______________________________
Not in scope: ________   Constraint that is really an assumption: ________

PARTS TABLE
| Part (API / dataset / model / hardware) | Intended use | Unintended 1 | Unintended 2 | Unintended 3 (other audience) |
|-----------------------------------------|--------------|--------------|--------------|-------------------------------|
| Member | Strongest skill | Real annoyances (last time it happened) |
|--------|-----------------|-----------------------------------------|

IDEA LOG (number in order written)
| # | One line (no better/faster/smarter/AI-powered) | Source: solo / brainwrite / lightning demo / reversal / Idea Box / TRIZ / lever / unintended use | Parts combined | Struck? (#1-8, prompt echo, no new job, one-prompt ChatGPT) |
Gate: total ideas __ (>=20)   from technique or analogy __ (>=3)

SHORTLIST CARD (3-5 cards, must differ in kind)
Name:
[Product] helps [persona] [do job] by [mechanism], so they [outcome].
New job enabled (impossible before):
Mechanism borrowed from (field / product):
Workaround it replaces:
Load-bearing deps: 1.____ E/M  2.____ E/M  3.____ E/M  4.____ E/M  (E = exists + access, M = must build)
Must-builds outside the novelty: __  (more than 1 = reshape or drop)
Survives "ChatGPT in one prompt" because:
Closest Devpost / past HackUTD project: ________  what it missed: ________
Storyboard: [pain moment] -> [key interaction] -> [result]
Core loop demoable in ~4h? Y/N        Riskiest assumption + test by hour __:
Tracks: general / sponsor ____ / MLH ____

DECISION LINE
"Shortlist: __, __, __. Struck: #1-#__ and __ (prompt echo). Advanced __ over __ because
<principle> [citation]. Runner-up: __. Parking lot photographed: Y/N"
```

## Principles
1. **Strike the first 6-8 ideas before choosing (counterintuitive).** About 80 percent of free associations are predictable, and teams working from the same APIs converge on the same first idea. In a competition you want to differ from other entrants, not build a better copy of the crowd's idea. [Where Good Ideas Come From, p.34-35, p.106-107; Noise, p.30]
2. **Invent exactly one layer; every other load-bearing dependency must exist today.** An idea that needs a missing part fails in the short term no matter how good it is, so a "we'll figure it out later" dependency kills it at the shortlist, not at hour 14. [Where Good Ideas Come From, p.35-38]
3. **Repurpose the sponsor's API for an unintended job (counterintuitive).** The "most impressive thing with the sponsor API" is the intended use, and everyone builds that. A load-bearing unintended use stands out to the sponsor judges who know their own product (hyperlinks became PageRank quality votes). [Where Good Ideas Come From, p.118-119, 123-125]
4. **Steal mechanisms from other fields, not features from competitors.** A hospital copied an F1 pit crew's handoff checklists and cut technical errors 42 percent, while copying peers' best practices moves the result only a little. [Creative Confidence, p.90-91; Sprint, p.78-80]
5. **Change in kind, not in degree.** Measure ambition by the new jobs the user can now do. If the one-liner falls apart without "smarter" or "AI-powered," it is a me-too. [Where Good Ideas Come From, p.21-22]
6. **Generate alone, then combine (counterintuitive).** Individuals beat brainstorming groups on number, quality, and originality, and the most original ideas tend to come in later write-share-write rounds. [Sprint, p.88; Continuous Discovery Habits, p.111-116]
7. **Test the frame before ideating on it.** If a frame does not produce about five different solutions in a few minutes, it is too narrow or too vague, and every idea built on it inherits that flaw. [Creative Confidence, p.105-107; IDEO Field Guide, p.24; Thinkertoys, p.67]
8. **When stuck, add parts instead of effort.** Good ideas come from recombining available parts, so a stalled board needs new inputs (an outsider, an obscure API, a non-tech workflow), not more staring. [Where Good Ideas Come From, p.39-40]
9. **Judge concrete, anonymous storyboards while the author stays silent.** Vague ideas get overrated or underrated by the status and charisma of whoever pitches them, and a 3-panel sketch removes that pitch effect. [Sprint, p.87-88, 93-94, 107-110]
10. **Keep 3 candidates that differ in kind.** Decisions made with a single option are wrong more than half the time, versus about a third with multiple options. Fifteen variants of one interface still count as one option. [What's Your Problem?, p.52-53]
11. **Seed one dissenter before lock.** Assigned dissent pushes groups toward more original associations even when the dissenter is wrong. Rotate the role so it never sticks to one person. [Where Good Ideas Come From, p.106-108, 112]
12. **Differentiate by subtracting, not only adding.** Ideas that only raise and create things become costlier me-toos. Asking what to eliminate or reduce opens new shapes and frees build hours. [Blue Ocean Strategy, p.40-43, p.58-60]

## Mistakes
- **Dot-voting the open board.** Tell: dots land on the first ideas spoken and the loudest author's ideas. Fix: strike #1-8 first, dot only cores demoable in ~4h, judge anonymous storyboards.
- **Sponsor-tech-first generation.** Tell: the first sentence names the API or "AI." Fix: write intended use plus 3 unintended uses, and say who has the problem and what they do today.
- **Feasibility noted, not enforced.** Tell: the card lists "need data we don't have" as a risk and the idea still advances. Fix: more than one must-build outside the novelty means reshape or drop now.
- **Cosmetic analogy or niche.** Tell: "Duolingo for X" or "for nurses" with no change in flow, data, or vocabulary. Fix: name the mechanism being transplanted and what that user would do differently. [Obviously Awesome, p.88]
- **Shortlist of one shape.** Tell: all 3-5 finalists are a web app with a chat panel. Fix: require differences in kind (interface, user, mechanism); otherwise run an Idea Box round.
- **Waiting for the eureka.** Tell: hour 2, nothing "feels brilliant," the search continues. Fix: hold the 90-minute timebox, pool half-formed hunches, choose by combination and feasibility. [Where Good Ideas Come From, p.63-65, 72]
- **Suppressing the surprise.** Tell: an odd model output gets "fixed" within 2 minutes. Fix: give it 10 minutes and show it to a teammate working on another component. [Where Good Ideas Come From, p.105-106]
- **Post-lock idea creep.** Tell: a 3 AM idea becomes a feature at hour 14. Fix: parking lot, unless it cuts scope or de-risks the riskiest assumption. [Sprint, p.125-126]

## Hackathon calibration
- **Compress, do not skip.** Sprint's four-step sketch becomes 5 + 5 + 8 + 15 minutes. Young's incubation becomes a 15-20 minute walk, not a night. Save real sleep for mid-build stalls at hours 10-16. [Sprint, p.89-93; A Technique for Producing Ideas, p.17, 21-24; Where Good Ideas Come From, p.79-80]
- **Quantity and depth both fit.** IDEO's target of up to 100 ideas an hour and Sprint's one detailed sketch per person do not conflict: generate many raw ideas, then make one detailed storyboard per finalist. [IDEO Field Guide, p.95; Sprint, p.96]
- **Shrink the long-horizon tools.** Broad-reading habits and reading weeks are preparation only. Field research shrinks to 3-5 conversations at the venue. Lotus Blossom goes one level deep. Mind maps are never shelved for days. [Creative Confidence, p.79-80; Thinkertoys, p.94-98, 164-168]
- **Science fair, about 4 minutes per judge.** An idea that needs 90 seconds of setup loses. Panel 1 of the storyboard (the pain moment) should be the demo's opening, one step before the product appears. [Sprint, p.93-94, 123-125]
- **About 200 projects.** Uniqueness is judged against the room, so the Devpost and past-HackUTD sweep matters more than market research. Put the one risky element in the core and keep everything else boring, so you satisfy both uniqueness and MLH completion. [Sprint, p.126; Where Good Ideas Come From, p.35-38]
- **Outsiders for ideas, experts for feasibility.** Use mentors and sponsor engineers to check feasibility. Trust an expert's "possible," and test an expert's "impossible" before believing it. [Thinkertoys, p.230-234; Creative Confidence, p.98, 104-105]
- **Keep ideation alive during the build.** At each 3-4 hour sync, give each person 2 minutes on "what surprised me, what is stuck." Lab breakthroughs mostly came from these meetings. Keep a shared hunch log open overnight. [Where Good Ideas Come From, p.52-54, 67, 70]

## Go deeper
- [07 Ideation reference](../domains/07-ideation.md)
- [02 Problem discovery reference](../domains/02-problem-discovery.md)
- [06 Competitor differentiation reference](../domains/06-competitor-differentiation.md)
- search_experts("strike obvious first ideas free association", domain="07-ideation")
- search_experts("exaptation repurpose feature unintended use", domain="07-ideation")
- search_experts("adjacent possible dependencies exist today", domain="07-ideation")
- search_experts("idea box parameters variations assumption reversal TRIZ contradiction", domain="07-ideation")
- search_experts("lightning demos big idea other industries", domain="07-ideation")
- search_experts("what stops a model update killing an AI wrapper moat data workflow", domain="06-competitor-differentiation")
