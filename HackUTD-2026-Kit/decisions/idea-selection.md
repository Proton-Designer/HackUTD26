---
name: idea-selection
description: Load when the team is choosing among 2-5 candidate ideas (H0 to H1:30 after sponsor challenges are revealed), when a spike or a similar project threatens the chosen idea (H3-H8), or when someone proposes switching ideas.
---
# Decision guide: idea-selection

## Open this when
- **H0:00-H1:30:** sponsor challenges are out and the team has 2-5 candidate ideas. The decision locks at H1:30 at the latest.
- **H0:30-H1:00:** a Devpost, app-store or venue check turns up a near-identical project, or the sponsor already sells the idea.
- **H3:** the spike on the riskiest dependency failed, or returned no real data inside the app.
- **H6-H8:** testers shrug or a teammate argues for a "better" idea. After the midpoint (about H12) only a zoom-in pivot that reuses the working pipeline is allowed.

## Steps
1. **Before H0: name the Decider** (the scope owner). Set a visible timer on every debate. Past 5 minutes, the Decider calls it. Hard cap of 90 minutes from shortlist to lock. [Sprint, p.103-104] [Good Strategy Bad Strategy, p.72-74] Write the target question at the top of the shared note: "Which idea gets a top-3 spot from the judges who see it?", not "Which do we like?" [Thinking, Fast and Slow, p.97-99]
2. **Put at least 3 ideas that differ in kind on the board.** If you have only 2, or 3 versions of one, silent-write for 3 minutes to add one. Single-option decisions go wrong more than half the time, versus about a third with multiple options. [What's Your Problem?, p.52-53] [Continuous Discovery Habits, p.31-32]
3. **One card per idea (2 min each),** using the Template. If a card has no "today's workaround", no "riskiest assumption" and no dependency list, it is not ready to be judged.
4. **Kill gates, about 10 min per idea. Pass/fail, and one fail kills.** A high total score cannot rescue a failed gate. You get one rework round per idea (narrow the user or change the angle), then drop it.
   - G1 Diagnosis: "Existing tools fail because ___" names a mechanism. "People waste time" is an outcome, so it fails.
   - G2 Prior art (20 min total, shared across ideas): search Devpost, past HackUTD galleries, the sponsor's own products, and "does ChatGPT/Claude do this in one prompt?" STOP if a polished product already serves this exact user. If the sponsor sells it, extend it. If one prompt does it, the edge must come from workflow, data or integration that survives a model upgrade.
   - G3 Unique attributes: list what the alternatives lack and strike anything 2+ alternatives have. You need 2-4 left. Zero means NO-GO.
   - G4 Gap: one dimension (minutes, steps, errors) at least 2x better than today's workaround, aiming for 10x. Under 2x will not read as different at a table.
   - G5 Onliness: "the only [category] that [differentiator] for [whom]." If 3 HackUTD teams could plausibly say it, it fails.
   - G6 Demo: the core benefit shows live in about 2 minutes, and the judge holds no more than 3 ideas to get it.
   - G7 Sponsor delete test: if the sponsor API could be removed without changing the demo, drop that track. Max 2 sponsor tracks.
   - G8 Capacity: (build hours x 4) minus 30% for surprises. Musts fit in 60% of that. Example: 16h x 4 = 64, minus 30% = 45, so Musts are 27 person-hours or less.
   - G9 Dependencies and people: list 3-5 load-bearing dependencies, each marked "exists and we have access" or "must build". More than one "must build" that is not the idea's core novelty fails. Spend 2 minutes per dependency proving it exists (open the file, call the API once). Someone has built something similar, or the hardest part can be spiked by H3. [Where Good Ideas Come From, p.35-38] [Agile Testing, p.373-376] [Playing to Win, p.31-32, p.74]
5. **Outside check, run in parallel (H0:30-H1:00).** Ask 2-3 target users "What do you do today when X?" and write down their literal answers. Say the one-liner to 2-3 non-teammates and ask them to repeat what it is, who it is for, and why it helps. Go only if 2 of 3 get all three. "I don't get it" means fix the words. "Not useful" means fix the idea. Never ask "is this a good idea?"
6. **Count survivors.** If 0 survive at H1:15, take the idea with the highest chance of finishing and zoom in on its strongest moment. If 1 survives, take it and skip to step 8. If 2 or more survive, continue.
7. **Compare the top 2 in plain units, not ordinal sums.** First say the base rate out loud: with about 200 projects, the prior for any one prize is low, and 70-90% of new ideas fail. Then each teammate writes privately, with no number spoken until all four are down:
   (a) P(core path runs live by H12). Multiply step reliabilities: 10 steps at 95% each run end to end about 60% of the time. (b) P(a judge who sees it ranks it top 3 of their batch).
   Expected value = a x b (take the median across people), plus a note on how many tracks it is central to (2 or fewer). Forecast first, then decide how much risk you want, as a separate step.
   If one idea clearly leads, it is the default. If the two are within about 10%, use tie-breakers in order: hours until a stranger can try it, cheaper to reverse, fewer "must build" dependencies. [Creative Confidence, p.117] [Six Thinking Hats, p.131-132]
   If estimates for one idea differ by 30+ points, that is the unknown to resolve. Spike it for 20 minutes only if the answer could flip the choice.
8. **Premortem plus dissent before committing (10 min).** 5 minutes silent writing: "It is Sunday noon and we placed nowhere. Write the story." Drop an idea whose top cause has no mitigation. Otherwise carry the top 3 causes into the plan, each with a fallback. Then one assigned dissenter gets 5 minutes to argue for a very different option, and the Decider asks, "What is the strongest reason this is a bad idea?" [Where Good Ideas Come From, p.106-108] [Crucial Conversations, p.202-203]
9. **Straw poll, then the Decider decides.** Everyone silently picks one, then explains in 1 minute. The poll is advisory, but the Decider sees the private estimates before calling it. The Decider states the choice and the principle behind it, with its citation, out loud and in the 3-line record (context and alternatives, decision and why, what you gave up). An override of the estimates carries a written reason. Losing ideas go to "maybe later." Never vote among 3+ options and never "do both." [Software Architecture (Ford et al.), p.23]
10. **Write tripwires now, before any result exists.** +3h: the spike returns real data inside the app, or swap the approach or fake it. +6h: if 3 of 4 testers do not want it, pivot one of user, problem or solution and keep the other two. +8h: the skeleton runs end to end. Midpoint: zoom-in pivot only. The choice reopens only when a tripwire fires, never because someone is tired or has a new idea. [Testing Business Ideas, p.61-63, p.96]

## Template
```
IDEA CARD  (one per idea)
Name / one-liner (12 words max): ____
For [user, by findable trait: "people who ___ N times/week"]: ____
Today's workaround (their words): ____
Diagnosis: existing tools fail because ____ (mechanism)
Gap dimension: today ___ vs ours ___  (= __x)
Onliness: "the only ___ that ___ for ___"   Others who could say it: ____
Unique attributes surviving (2-4): ____
Demo moment (the one surprise, <60s): ____
Sponsor track(s), max 2, + delete test result: ____
Dependencies (3-5): ____ exists/must-build, checked Y/N
Riskiest assumption -> test by H3: ____
Closest prior art (Devpost / sponsor / one-prompt LLM): ____

GATES   G1 G2 G3 G4 G5 G6 G7 G8 G9   any FAIL -> drop / one rework
Idea A  _  _  _  _  _  _  _  _  _
Idea B  _  _  _  _  _  _  _  _  _
Idea C  _  _  _  _  _  _  _  _  _

TOP-2 ESTIMATES (private, then reveal)   Base rate said aloud: Y/N
            P(live by H12)   P(top-3 of a judge's batch)   EV=a*b (median)   spread
Idea A      __ __ __ __      __ __ __ __                   ___               ___
Idea B      __ __ __ __      __ __ __ __                   ___               ___

PREMORTEM top causes (per idea): 1.___ 2.___ 3.___   mitigable? Y/N   fallback: ____
Dissenter: ____   strongest case against: ____

DECISION RECORD
Chosen: ____   Decided by: ____   Time: H__:__
Context + alternatives: ____
Principle + citation: ____
What we gave up / why not #2: ____
Override of estimates? reason: ____
Forecast: __% core path returns real data by +3h
Outsider test: _/3 repeated what/who/why
Tracks: General + ____ + ____ (+ MLH ____)
Tripwires: +3h ____  +6h ____  +8h ____  midpoint: zoom-in only
Maybe-later list: ____
```

## Principles
1. **Pick for a top-3 spot in each judge's batch, not a decent average (counterintuitive).** Under MLH's recommended 3/2/1 stack ranking, an idea that is solid on every criterion but memorable on none scores zero from that judge. [Seed: B. Standard rubrics and how judging is run, §B2] [Seed: C. Writeups from judges and repeat winners, §C7]
2. **Gates are non-compensatory: any very low score eliminates the idea whatever its total.** A strong total hides a fatal hole (no user, no complete flow in 24h, an owned market). [Crossing the Chasm, p.83-85]
3. **Do not hand-weight 1-5 scores to choose (counterintuitive).** Ordinal ratings are not quantities, and the evidence that they improve decisions is absent or negative. Tuned weights add nothing: simple equal-weight sums matched fitted models (r about .60 vs .57). Use scores only to surface disagreement, then compare probabilities. [How to Measure Anything, p.58-59] [Continuous Discovery Habits, p.103-106] [Noise, p.112-114]
4. **Never decide on a single option.** Nutt found single-option decisions fail more than half the time versus about a third with multiple options, and many versions of the same solution still count as one option. [What's Your Problem?, p.52-53] [Continuous Discovery Habits, p.31-32]
5. **Start every forecast from the base rate, then adjust (counterintuitive).** About 70-90% of new ideas fail, and with about 200 projects the prior for one prize is low however good the story feels. Write forecasts as percents, and set risk appetite as a separate step so hope does not leak into the estimate. [The Right It, p.24] [Noise, p.145-146] [Noise, p.62-63] [How to Measure Anything, p.60-62]
6. **Write estimates privately before anyone speaks.** Anchoring effects run about 40-55% and hit experts nearly as hard as novices, and open discussion lines everyone's errors up behind the first confident speaker. [Thinking, Fast and Slow, p.84, p.118-126]
7. **Uniqueness is scored against the room, so run the onliness test against likely HackUTD teams.** About 200 projects get 4 minutes each, so a judge may have seen your idea last year or an hour ago. [Zag, p.52] [Seed: 0. Synthesis, §3]
8. **Require one dimension at least 2x better than today's real workaround, and aim for 10x.** A 20% gain is invisible, and the real competitor is the spreadsheet, the group chat, or doing nothing. [Zero to One, p.38-39] [Value Proposition Design, pp.160-161] [Obviously Awesome, p.39, p.63-64]
9. **The diagnosis must name why current tools fail.** It is the answer to the judge's disguised "why this?" question, and an outcome-only diagnosis leaves the guiding policy empty. [Good Strategy Bad Strategy, p.68-70]
10. **Choose the sponsor topic the sponsor cares about, with their tech in the core loop.** Sponsors judge as "will my company look good?", and past HackUTD multi-prize winners made the sponsor tech central. [Seed: C, §C3] [Seed: A. HackUTD-specific, §A3] [Hackathon Planning Kit, p.8]
11. **One Decider; the straw poll is advisory (counterintuitive).** Consensus voting yields compromise, and pairwise votes among four people can cycle with no stable winner. The Decider still sees the private estimates first and records any override, which keeps the speed and the noise reduction. [Sprint, p.111-114] [Good Strategy Bad Strategy, p.72-74] [Thinking, Fast and Slow, p.84]
12. **Run the premortem before the commit, not after.** Once a choice looks made, doubts get suppressed as disloyalty. The premortem breaks that groupthink. [Thinking, Fast and Slow, p.256-257]
13. **Test comprehension with outsiders, and act only on patterns.** Small teams hype each other, and distinctive ideas test poorly on preference, so act on "can they repeat it?" and not on "do they like it?" One passionate voice is not a mandate; a pattern across at least 3 people is a signal. [Make: Bootstrappers Handbook, p.62-63] [Zag, p.30-32] [Talking to Humans, p.90]
14. **Gather only evidence that could flip the choice, and set the kill criterion before you see it.** Spend validation on the 1-4 assumptions that are both most uncertain and most damaging, and drop any check where both outcomes lead to the same pick. After the fact people rewrite what they believed, so a pre-written trigger turns a checkpoint into a decision. [How to Measure Anything, p.28-31, p.77-78] [Thinking, Fast and Slow, p.197-198] [Testing Business Ideas, p.61-63]

## Mistakes
- **"Safe 4s everywhere" wins the spreadsheet.** Tell: the top scorer is the idea nobody can retell in one line. Fix: ask "which one would a judge repeat in deliberation?" and apply principle 1.
- **"X but with AI" or one-prompt wrapper.** Tell: ChatGPT does the core in one prompt, and the value curve runs parallel to the incumbent's. Fix: change one factor entirely (workflow, data, an action completed end to end) or drop it. [Blue Ocean Strategy, p.81] [7 Powers, p.80]
- **Cosmetic niche.** Tell: "for students" or "for nurses" with no change in flow, data, or vocabulary. Fix: ask two members of that group what they would do differently with it. No concrete answer means change the group or the idea. [Obviously Awesome, p.88]
- **Keeping two ideas alive or chasing three tracks.** Tell: "let's build the core of both" or separate features per sponsor. Fix: the Decider picks one, and a track counts only if the same build already qualifies. [Escaping the Build Trap, p.100-101]
- **Feasibility "validated" by reading docs.** Tell: G9 passed because the API "should" support it. Fix: it counts only when real data returns inside your app by H3. [Shape Up, p.111-112]
- **Re-pitching the sponsor's own product.** Tell: the sponsor rep says "we have that." Fix: extend or complement it instead. [Seed: A. Hackathon quick-run protocol, §2]
- **Answering the easier question.** Tell: the case for an idea is all "it would look cool on stage" or "I'd use it." Fix: re-read the target question from step 1 and ask which question the discussion just answered. [Thinking, Fast and Slow, p.97-99]
- **Group hype or one voice as evidence.** Tell: no outsider has heard it, or one mentor's or sponsor rep's reaction picks the idea. Fix: run step 5 before step 9, and treat a single reaction as a hypothesis until 2 more people repeat it. [Talking to Humans, p.90]
- **Relitigating.** Tell: the H1 debate returns at H6 with no new evidence. Fix: point to the decision record; reopen only if a tripwire fired. [Software Architecture (Ford et al.), p.23]

## Hackathon calibration
- **MLH tracks do not score originality or real-world problem fit.** If an MLH prize is the realistic target, weight G6, G8 and G9 over G4 and G5. [Seed: B, §B1]
- **Shrink discovery.** Cagan's third-of-the-time discovery becomes a 90-minute lock, and Cagan's six clean users become 3-5 five-minute conversations. Hubbard's value-of-information math becomes a gut check: rank assumptions by uncertainty times cost of being wrong, test the top 1-2, each in under an hour, in parallel with the build and never as a gate past H3. [Inspired, p.153, p.176-177] [Lean Startup, p.78-79] [How to Measure Anything, p.31, p.77-78] [Testing Business Ideas, p.52-55]
- **Commit to one idea by H2; allow two throwaway approach prototypes within it during H3-H8, converging at a fixed hour.** Hold the persona loosely until H6-H8 and lock it by H12. Moore's commitment governs the idea and build scope; Stickdorn's parallel concepts and Dunford's stay-broad advice apply only inside it. [Crossing the Chasm, p.76-77] [This Is Service Design Methods, p.560-561] [Obviously Awesome, p.51]
- **Ignore RICE, TAM slides, moats, and pricing tiers when choosing.** Viability is one back-of-envelope sentence held in reserve, not a selection criterion. [Seed: D. Prioritization frameworks, §D1-D2] [Seed: B, §B2-B3]
- **"Decisions are reversible" (Torres) only holds until about H6-H8 here.** A full pivot is survivable up to about H8; after H14 it usually is not. [Continuous Discovery Habits, p.32-33] [Lean Startup, p.138-139]
- **Kahneman's findings and the 70-90% failure rate come from lab, field and product studies, not hackathons.** Use them to justify private estimates and the premortem, not as precise numbers.

## Go deeper
- ../domains/08-decisions-uncertainty.md
- ../domains/01-judging.md
- ../domains/06-competitor-differentiation.md
- ../domains/09-product-strategy-prioritization.md
- ../domains/10-usp-value-prop.md
- search_experts("Decider straw poll super-vote", domain="08-decisions-uncertainty")
- search_experts("base rate outside view prediction", domain="08-decisions-uncertainty")
- search_experts("assumptions mapping importance evidence quadrant", domain="08-decisions-uncertainty")
- search_experts("weighted score ordinal ratings probability estimates", domain="05-evidence-quant-research")
- search_experts("onliness statement only category differentiator", domain="10-usp-value-prop")
- search_experts("market alternative product alternative creating the competition", domain="06-competitor-differentiation")
- search_experts("five betting questions appetite right people", domain="09-product-strategy-prioritization")
