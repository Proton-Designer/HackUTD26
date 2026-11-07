---
name: 07-ideation
description: Open when the team is about to generate or pick the project idea (hour 0-4), when every candidate looks like the obvious sponsor-prompt chatbot, when the team has circled the same 2-3 ideas for 20+ minutes, when two teammates deadlock on direction, or when someone proposes a new idea after scope lock.
---
# Creative problem solving, ideation, and solution generation

## Use this when
- Hour 0-1: sponsor tracks and APIs are announced and the team needs a pool of candidate ideas fast.
- Hour 1-3: cutting 20+ raw ideas to one concept with explicit kill conditions.
- Any time the shortlist reads as "X but smarter with AI" or matches what ~200 other projects will build from the same prompt.
- The team is stuck: same ideas recycled, frustration rising, or a sponsor challenge feels too narrow to be original.
- Two teammates argue for different directions and debate is past 5 minutes.
- Mid-build (hour 8-16): a surprising bug, odd model output, or 3 AM idea appears and someone wants to change course.

## Core principles
1. **Every load-bearing dependency must exist today; invent exactly one layer.** For each candidate, list 3-5 load-bearing dependencies and mark each "exists and we have access" or "must build." More than one must-build that is not the core novelty means drop or reshape. Ideas needing a missing part fail in the short term no matter how good. [Where Good Ideas Come From, p.35-38; p.141, 143, 156]
2. **Strike the first 6-8 ideas before choosing (counterintuitive).** About 80 percent of free associations are the predictable ones, and simultaneous independent invention is the norm, so other teams are converging on your first idea from the same APIs. In a competition you want variance from other entrants, not a better copy of the crowd's idea. [Where Good Ideas Come From, p.34-35, p.106-107; Noise, p.30]
3. **Generate alone and silently, then combine together (counterintuitive).** A 1958 Yale study found individuals beat brainstorming groups on number, quality and originality. Run write-alone, share, write-again rounds until the board holds 15-20+ ideas; the most original ones tend to come late. [Sprint, p.88; Continuous Discovery Habits, p.111-116]
4. **Reframe before ideating, and test the frame with the five-solutions test.** Write the obvious how-might-we plus at least two reframes; if the team cannot produce about five different solutions to a frame in a few minutes, it is too narrow or too vague. Strip any named solution form ("a dashboard," "a chatbot") from the prompt first. [Creative Confidence, p.105-107; IDEO Field Guide, p.24; Thinkertoys, p.67]
5. **Steal mechanisms from other fields, not features from competitors.** A hospital copied an F1 pit crew's handoff checklists and cut technical errors 42 percent; copying competitor best practices only moves one number a little. Ask "where is this structure already solved in logistics, games, medicine, finance?" and transplant the mechanism. [Creative Confidence, p.90-91, p.94-96; Where Good Ideas Come From, p.115-120]
6. **Repurpose the sponsor's API for an unintended job.** Everyone builds the intended use. For each sponsor API or dataset, write the intended use, then 3 unintended uses, and look for one serving a different audience (hyperlinks became PageRank quality votes). [Where Good Ideas Come From, p.118-119, 123-125]
7. **Change in kind, not in degree.** Score ambition by how many previously impossible jobs the user can now do, not by engineering difficulty. Rewrite the one-liner without "better," "faster," "smarter," or "AI-powered"; if nothing distinctive remains, keep looking. [Where Good Ideas Come From, p.21-22]
8. **Choose with an equal-weight scorecard plus a showstopper rule, not debate (counterintuitive).** Score each shortlisted idea 1-5 on fixed criteria and sum with equal weights; the simple sum beats holistic expert judgment. Any single very low score eliminates an idea even if its total is high. [Noise, p.112-114; Thinking, Fast and Slow, p.216-220; Crossing the Chasm, p.83-85]
9. **Seed one dissenter before lock.** Assigned dissent, even when wrong, measurably pushes groups toward more original associations (Nemeth). Give one person 5 minutes to argue against the favorite and for a very different alternative; rotate the role. [Where Good Ideas Come From, p.106-108, 112]
10. **Make ideas concrete and anonymous before judging; the author stays silent.** Vague ideas get underrated or overrated by status and charisma. A 3-panel storyboard (pain moment, key interaction, result) with real copy, judged by silent dots, removes the pitch effect. [Sprint, p.87-88, 93-94, 107-110]
11. **Load the problem, then step away briefly before the final vote.** Sleeping on a hidden-pattern task more than doubled solvers; incubation only works after immersion. At a hackathon this is a 15-20 minute walk, not a night. [Where Good Ideas Come From, p.79-80; A Technique for Producing Ideas, p.21-23; Creative Confidence, p.91-93]

## Decision procedure
Main decision: which concept to build. Target lock by hour 3, hard stop hour 4-5 [A Technique for Producing Ideas, p.17, 24 adaptation]. The team plan already lists comparison criteria; this procedure adds order, thresholds and stop rules.

1. **Parts table (15 min).** Whiteboard every sponsor API, dataset, model API, hardware item, and each member's strongest skill. Add each member's 3-5 pre-collected real annoyances. Ideas must come from pairs or triples of parts. [Where Good Ideas Come From, p.39-40, p.151-153; Creative Confidence, p.123-124]
2. **Frame (10 min).** Write 3 HMWs; run the five-solutions test on each; keep the one that opens the most solutions. Add two lines: "Not in scope:" and "Constraints that are really assumptions:". [IDEO Field Guide, p.24; Thinkertoys, p.172, 176]
   - Sponsor track: keep the sponsor's stated requirement as the core feature; reframe only around it. [Six Thinking Hats, p.106-107]
3. **Diverge alone (25-35 min).** Lightning demos at 2-3 min each with the "big idea" captured, then silent write-share-write rounds, then one prompt round (pick one: assumption reversal, attribute split, SCAMPER on one workflow step, Idea Box 4 parameters x 5 variations, TRIZ contradiction). [Sprint, p.80-82; Thinkertoys, p.68, 77-81, 101-102, 149-155; Seed: B. Generating ideas, §B6]
   - Go to step 4 only when the board has 20+ ideas and at least 3 came from a prompt technique or cross-field analogy.
   - If the team circles the same 2-3 ideas for 20+ minutes, do not think harder: add parts (an outsider, an obscure API, a non-tech workflow). [Where Good Ideas Come From, p.40]
4. **Strike and filter (10 min).** Strike the first 6-8 ideas and any idea that is the first thing the sponsor prompt suggests. Then each person dots only ideas whose core loop could be demoed in about 4 hours. Keep 3-5. [Where Good Ideas Come From, p.106-107; Creative Confidence, p.131-132]
5. **Dependency check (5 min per idea).** Drop or reshape any idea with more than one must-build dependency outside its core novelty. [Where Good Ideas Come From, p.35-38]
6. **Score (10 min).** Each person scores silently, 1-5, on the seed's seven criteria: problem fit, wow, buildability (~18 build hours), sponsor fit, differentiation, explainability, demo risk. Sum with equal weights. A 1 on any criterion, or a 2 on buildability or problem fit, eliminates. [Seed: A. Hackathon ideation session, §Hackathon scoring for the shortlist; Noise, p.112-114; Crossing the Chasm, p.83-85]
7. **Stress the top 2 (15 min).** For each: 3 min benefits only, then 3 min risks only, everyone in the same mode. Then 5 min of assigned dissent. If you cannot find real benefits, stop there. [Six Thinking Hats, p.21, 23; Where Good Ideas Come From, p.106-108]
8. **Pass the gates.** The winner must: fit "[Product] helps [persona] [do job] by [key mechanism], so they [outcome]" in one sentence; name exactly one attribute no competitor claims; enable at least one new job; survive the no-"better/faster" rewrite. Fail any gate: return to the runner-up or do one 15-minute variant round. [Seed: C. Converging and choosing, §One-sentence test; Thinkertoys, p.82; Where Good Ideas Come From, p.21-22]
9. **Walk (15-20 min), then decide.** Straw poll is advisory; the pre-named Decider makes the call. If the top two are within 2 points, pick the one a stranger can try soonest, or the one cheaper to reverse. Build both ("battle") only if two people can each ship a thin version inside the timebox. [Sprint, p.111-114, 116-117; Creative Confidence, p.117; Six Thinking Hats, p.131-132]
10. **Lock with kill conditions.** Write the riskiest assumption and test it in the first 2-3 build hours with a hard-coded screen or a single API call. Write the switch rule, for example: "if the core API call does not return usable output by hour 6, switch to the runner-up." Open a parking lot; after lock only cuts and bug fixes are allowed. [IDEO Field Guide, p.111; Sprint, p.125-126]

## Checklists

**Idea-lock check (run on the chosen concept)**
- [ ] One-sentence pitch written and understood by an outsider on first read.
- [ ] Every load-bearing dependency verified, with at most one must-build (the novelty).
- [ ] One unique attribute named; it is also the demo's wow moment.
- [ ] Core loop fits ~18 build hours; demo works without fragile wifi or slow APIs, or has a fallback.
- [ ] Sponsor tech is load-bearing, not a decorative call.
- [ ] Riskiest assumption, its test, and a switch rule with an hour stamp are written down.
- [ ] Runner-up idea and the parking lot are photographed and saved.

**Session hygiene check (run on the ideation process)**
- [ ] Generation and judgment never happened in the same phase. [Seed: 0. Synthesis, §1]
- [ ] Every person wrote alone before anyone spoke.
- [ ] 20+ ideas before any vote; first 6-8 struck.
- [ ] At least one cross-field analogy and one reversal or attribute-split idea on the board.
- [ ] Sketches judged anonymously, creator silent until the end. [Sprint, p.109-110]
- [ ] Every debate had a visible timer; none ran past 5 minutes. [Sprint, p.103-104]

## Anti-patterns
- **The prompt-echo idea.** Tell: the concept surfaced in the first 10 minutes and is the obvious reading of the sponsor challenge (an assistant, a chatbot, a dashboard). Fix: strike it; push to the 3rd or 4th variant, add an unusual part or a niche user. [Where Good Ideas Come From, p.34-35]
- **Degree, not kind.** Tell: the one-liner depends on "smarter," "faster," "AI-powered." Fix: list new jobs enabled; if zero, add a participation or new-capability element or move on. [Where Good Ideas Come From, p.21-22]
- **The visionary leap.** Tell: "we will figure out X later" about a load-bearing piece. Fix: dependency check; reshape so that piece is either off-the-shelf or is the single novelty. [Where Good Ideas Come From, p.35-38]
- **Loud-room brainstorm.** Tell: one person talks most, ideas are critiqued as they are spoken. Fix: 2 minutes silent writing before any round; say "risks-only for 3 minutes" instead of "stop being negative." [Sprint, p.88; Six Thinking Hats, p.20-21, 24-25]
- **Permanent critic.** Tell: the same teammate always kills ideas and the same one always pitches wild ones. Fix: everyone wears the same mode at the same time; rotate the dissenter. [Six Thinking Hats, p.12-13]
- **Grab-bag concept.** Tell: the pitch is a feature list with no single unique attribute. Fix: bundle only the parts that live in one user flow; cut the rest to the parking lot. [IDEO Field Guide, p.97-98; Thinkertoys, p.82]
- **Consensus compromise.** Tell: the vote produced a blend nobody is excited about, or the debate keeps reopening. Fix: Decider supervote, plus a 1-minute gut check after the analysis; an idea nobody likes rarely gets finished. [Sprint, p.111-114; Six Thinking Hats, p.111-112, 122-123]
- **Waiting for the eureka.** Tell: hour 2, nothing "feels brilliant," the team keeps searching. Fix: timebox to ~90 minutes, pool half-formed hunches in one doc, choose by combination and feasibility. [Where Good Ideas Come From, p.63-65, 72]
- **Post-lock idea creep.** Tell: a 3 AM idea becomes a new feature at hour 14. Fix: it goes to the parking lot unless it is a cut or it de-risks the riskiest assumption. [Sprint, p.125-126]
- **Bug fixed before it was understood.** Tell: an odd model output or API result gets suppressed in 2 minutes. Fix: spend up to 10 minutes asking "is this the interesting part?" and show it to a teammate on another component. [Where Good Ideas Come From, p.105-106; Thinkertoys, p.126-127, 136]

## Hackathon calibration
- **Compress, do not skip.** Young's five stages become research 45 min, digest 30 min, a short walk, then capture; Sprint's four-step sketch becomes 5 + 5 + 8 + 15 minutes; a full Six Hats decision fits in 15-25 minutes at about one minute per person per phase. [A Technique for Producing Ideas, p.17, 24; Sprint, p.89-93; Six Thinking Hats, p.22]
- **Science-fair judging, ~4 minutes per judge.** An idea that needs 90 seconds of setup loses. The 3-panel solution sketch should already be the demo script: pain moment, key interaction, result. Open at the user's pain, one step before the product appears. [Sprint, p.93-94, 123-125]
- **~200 projects.** Differentiation is a selection criterion, not polish. Uniqueness and impact reward a change in kind; MLH completion rewards the adjacent possible. Satisfy both by putting the one risky element in the core and keeping everything else boring. [Sprint, p.126; Where Good Ideas Come From, p.35-38]
- **Sponsor tracks.** Sponsors judge their own tracks, so a sponsor API used for an unintended but load-bearing job beats a token call. Do not reinterpret the sponsor's stated requirement away. [Where Good Ideas Come From, p.118-125; Six Thinking Hats, p.106-107]
- **Ignore or shrink.** Young's broad-reading habit and Johnson's reading weeks are preparation only. IDEO's field research shrinks to 3-5 conversations at the venue. Google's 20 percent time shrinks to one person for 1-2 hours in the early-middle build, with a 2-minute demo at the next sync and a kill. Mind maps are not shelved for days. Lotus Blossom goes one level deep only. Platform-first architecture only if the API is free to expose. [Creative Confidence, p.79-80; Where Good Ideas Come From, p.75-76, p.144-145; Thinkertoys, p.94-98, 164-168]
- **Overnight.** Keep a shared hunch log open; anyone waking with an idea posts it. Review at the next checkpoint, under the post-lock rule. [A Technique for Producing Ideas, p.22-23; Where Good Ideas Come From, p.67, 70]
- **Keep ideation alive in the build.** At each 3-4 hour sync, 2 minutes per person on "what surprised me, what is stuck"; most lab breakthroughs came from these meetings, not from solo work. [Where Good Ideas Come From, p.52-54]

## Where experts disagree
- **Solo vs group generation.** Sprint says skip group brainstorming (Yale study); IDEO's seven rules run a group brainstorm; Johnson finds breakthroughs in group lab meetings (Dunbar). Follow: generate alone, then use the group to combine and to reframe stuck problems. The studies measure different things: Yale measured raw idea output, Dunbar measured reinterpreting an existing problem. [Sprint, p.88; IDEO Field Guide, p.94-95; Where Good Ideas Come From, p.52-54]
- **Pick one vs bundle.** Sprint has the Decider pick one concept; IDEO says bundle clusters into a system. Follow: bundle only what fits a single user flow the demo can show in under a minute; otherwise pick one and park the rest. [Sprint, p.111-114; IDEO Field Guide, p.97-98]
- **Bold bet vs shippable.** Sprint and Creative Confidence favor the risky, harder, more human idea; Johnson and IDEO's Ways to Grow favor what can ship, noting incremental ideas can have the biggest impact. Follow: exactly one risky element, and it must be the core novelty; every other dependency must already exist. [Sprint, p.111, 126; Creative Confidence, p.80; Where Good Ideas Come From, p.35-38; IDEO Field Guide, p.141-143]
- **Outsiders vs experts.** Thinkertoys says ask outsiders because experts call good ideas impossible; Creative Confidence says seek unexpected experts and extreme users. Follow: use outsiders for ideas and experts for feasibility; trust an expert's "possible," and test an expert's "impossible" before believing it. [Thinkertoys, p.230-234; Creative Confidence, p.98, 104-105]
- **Reframe vs stay in frame.** Creative Confidence and Thinkertoys push reframing the question; de Bono warns against always solving a different problem. Follow: reframe freely on the general track; on a sponsor track, keep the stated requirement as the core. [Creative Confidence, p.105-107; Thinkertoys, p.67; Six Thinking Hats, p.106-107]
- **How long to incubate.** Young says incubation cannot be skipped; Johnson's evidence is sleep after immersion. Follow: a 15-20 minute walk before the final vote; save real sleep for mid-build stalls at hours 10-16. [A Technique for Producing Ideas, p.21-23; Where Good Ideas Come From, p.79-80]
- **When to expose the idea.** Young says show the new idea to critics right away; Sprint keeps authors silent and sketches anonymous. Follow: anonymous judging before lock, then within 30 minutes of lock pitch it to 2-3 mentors and write down what they add. [A Technique for Producing Ideas, p.24; Sprint, p.107-110]
- **Quantity vs fewer sketches.** IDEO targets up to 100 ideas an hour; Sprint limits detailed solution sketches to one per person. Not a real conflict: many raw ideas, one detailed sketch each. [IDEO Field Guide, p.95; Sprint, p.96]

## Go deeper
- search_experts("adjacent possible dependencies exist today", domain="07-ideation")
- search_experts("individuals outperform brainstorming groups sketch alone", domain="07-ideation")
- search_experts("strike obvious first ideas free association", domain="07-ideation")
- search_experts("exaptation repurpose feature unintended use", domain="07-ideation")
- search_experts("reframe challenge how might we question zero", domain="07-ideation")
- search_experts("heat map speed critique straw poll decider supervote", domain="07-ideation")
- search_experts("assumption reversal attribute listing idea box", domain="07-ideation")
- search_experts("dissent increases original ideas Nemeth", domain="07-ideation")
- search_experts("equal weight scoring formula beats judgment", domain="08-decisions-uncertainty")
- search_experts("incubation sleep walk insight after immersion", domain="07-ideation")
