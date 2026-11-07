---
name: 01-judging
description: Open when picking tracks at hour 0-1, writing the one-line identity, deciding what goes in the 2-minute table demo, auditing claims and mocks before judging, prepping Q&A, or adjusting the pitch for a sponsor, MLH, or late-slot judge.
---
# Hackathon judging and evaluation

## Use this when
- Hour 0-1: choosing the general track plus at most two sponsor tracks and writing what each track's judges will reward.
- Before the first feature is coded: locking the one-sentence identity and the single demo flow.
- Hour 12 checkpoint: deciding whether the end-to-end path is live or scope must be cut.
- Hours 18-22: building the 4-minute table visit, the claims and mocks audit, and the Q&A answer buckets.
- During the 3-hour science-fair window: switching pitch variants for a sponsor judge, an MLH judge, a technical judge, or a tired late judge.
- Writing the Devpost description and demo video so the deliberation material matches what judges saw at the table.

## Core principles
1. **Play to make each judge's top 3 in their batch, not to earn a decent average (counterintuitive).** MLH's recommended method has each judge name a top 3 from the projects they saw (3/2/1 points), summed across judges; a solid-but-forgettable project scores zero from that judge. [Seed: B. Standard rubrics and how judging is run, §B2] Rubric scores compress to mid-range anyway, so the gap comes from a live demo, a clear first sentence, and right-sized scope. [Seed: C. Writeups from judges and repeat winners, §C7]
2. **One end-to-end path that runs live beats a broader project shown partly on slides.** Five half-built features lose to one that works; deliver 100% of a narrow promise rather than 80-90% of a broad one, because claimed completeness gets checked. [Seed: 0. Synthesis, §6] [Crossing the Chasm, p.95-96]
3. **The first sentence says what it is and who it is for; the whole message lands in 30 seconds.** Judges' fast first impression usually becomes their verdict and slower thinking mostly rubber-stamps it; opening with market size or a long backstory burned about a third of a slot. [Thinking, Fast and Slow, p.26, p.46-47] [Seed: C, §C7] [Minto Pyramid Principle, p.49, p.59]
4. **Give the judge one line they can repeat to other judges in deliberation.** Memorability decides who survives the debrief; a short, rhythmic phrase repeated at open, demo moment, and close feels more insightful and more true, and an easy-to-say name is rated more favorably. [Seed: C, §C7] [Thinking, Fast and Slow, p.64-65, p.67] Cap it at 140 characters and make it name the product. [Talk Like TED, p.105-107]
5. **Know which rubric the judge in front of you holds.** General track: uniqueness, technicality, viability, UI/UX, complexity, usefulness, impact. MLH: technology, design, completion, learning, equal weight, and explicitly not pitch quality, originality, or real-world problem fit. Sponsor: "If I reward this, will my company look good?" [Seed: A. HackUTD-specific, §A3] [Seed: B, §B1] [Seed: C, §C3] Phrase each answer in terms of what that judge is measured on. [The Challenger Sale, p.152-159]
6. **Name your biggest weakness before the judge does (counterintuitive).** Naming a real "what breaks first" raised scores, while claiming nothing could break cost credibility. [Seed: C, §C7] Say the top harsh objection ("it's an API wrapper", "the data is mocked") calmly and first. [Never Split the Difference, p.55-59] When asked about a gap, say what you did, what you did not, and how it would work. [Crucial Conversations, p.153-154]
7. **Late judges score harsher; make late visits shorter and easier to say yes to.** In the parole study, approvals fell from about 65% after a food break to near zero before the next; depleted evaluators fall back on "no." [Thinking, Fast and Slow, p.45] Cut to the 60-second live moment when a judge looks spent.
8. **Polish the first screen and the demo path only.** Attractive UIs are read as easier to use and get forgiven for small flaws, with opinions forming in about 50 ms; large, high-contrast text raises belief. [Laws of UX, p.111-116] [Thinking, Fast and Slow, p.64-65] Polish past readability did not move scores and can hint at a neglected backend. [Seed: C, §C7]
9. **Tag every number as measured, cited, or estimated, and recompute it before it goes on the poster.** One soft claim spotted by a judge downgrades the rest; plausible-sounding numbers are accepted without checking unless someone is assigned to check. [Thinking, Fast and Slow, p.46-47] Treat a surprisingly good result as a likely bug until verified. [Trustworthy Online Controlled Experiments, p.82-83]
10. **Mock the periphery, label it, and keep one real core the judge can poke.** Faking hard parts is normal at hackathons, but nice design cannot rescue an obviously fake demo, and judges ask "what did you build this weekend?" [Hackathon Planning Kit, p.14] [Thinking, Fast and Slow, p.65-66] [Seed: C, §C7]
11. **Let the judge verify one claim with their own hands, built around one surprise.** A claim the judge tests (predict, then see the result) beats one they are told; a single expectation-violating moment early triggers focused attention. [Made to Stick, p.143-145] [Thinking, Fast and Slow, p.72] Build up to it and repeat the headline after. [Presentation Secrets of Steve Jobs, p.262-268]
12. **For sponsor tracks, pick the topic the sponsor cares about, not the one you like.** Sponsors judge like customers; an entry tied to the sponsor's trend beat a technically comparable one tied to the team's interest. [Seed: C, §C3] Past HackUTD winners stacked several sponsor prizes by making the sponsor tech core and naming a concrete recipient (TxDOT, State Farm customers). [Seed: A, §A3]

## Decision procedure
Main decision: what we show judges, and when to cut.

1. **Hour 0-1, get the facts.** Ask an organizer: minutes per visit (plan for 4: 2 demo, 1 Q&A, 1 travel), judging window (about 3 hours, team must stay), whether finalists present (finalist slot is about 7 minutes: 3-5 presenting), which judges cover which tracks. [Seed: A, §A1] [Seed: B, §B2] Pick at most two sponsor tracks. For each track write: "This track wants X; we deliver X by Y." If Y needs the sponsor tech bolted on rather than central, drop that track. [Hackathon Planning Kit, p.5-6, p.8]
2. **Before coding, lock the identity sentence.** Format: "[Name] lets [specific user] [do task] so [result]." Gate: run the email or stranger test (send two sentences; ask them to explain it back). Any clarifying question means rewrite. No feature work until it passes. [Seed: What is Y Combinator?, §Improving Your Answers] [Thinking, Fast and Slow, p.79-80]
3. **Pick the core loop.** One user action, one result that makes the judge care, understandable in about 60 seconds. [Seed: C, §C5] Gate: if the judge must hold more than 3 ideas to get it, cut. [Thinking, Fast and Slow, p.37-39]
4. **Hour 12 go/no-go.** The single end-to-end path must run live by the halfway mark. [Seed: C, §C7] If not: stop all new work, cut until it runs, describe the rest in one sentence. Freeze the stretch list at hour 16; anything unfinished is cut, not demoed. [Hackathon Planning Kit, p.6]
5. **Feature-in-demo filter.** Show a feature only if it appears in the 2-minute flow and supports a named criterion for this judge's track. Otherwise it gets one spoken sentence or nothing. Never tour features. [Seed: C, §C1]
6. **Mocks audit (hour 18).** List every mocked or canned component. Each gets a spoken label. Stop if nothing real is left for a technical judge to poke; move effort to making one core path genuine. [Hackathon Planning Kit, p.14]
7. **Claims audit.** One teammate recomputes every number on poster, slide, and Devpost in 2 minutes and tags it measured/cited/estimated. Any number that cannot be traced is removed. [Thinking, Fast and Slow, p.45-47]
8. **Q&A prep.** Run the accusation audit (write every harsh thing a judge could say; script calm answers to the top 3). Then write one answer per bucket: competition ("why not X?"), accuracy, privacy/data, scalability ("what breaks first"), what you built this weekend vs existing parts, why the sponsor tech matters, what next. [Never Split the Difference, p.55-59] [Presentation Secrets of Steve Jobs, p.326-330] [Seed: C, §C7]
9. **Script the 4-minute visit.**
   - 0:00-0:10 identity sentence.
   - 0:10-0:30 one concrete moment of the felt problem (a person, a task, what goes wrong).
   - 0:30-1:30 live flow from pre-loaded state, ending on the one surprise; silence while the key result loads, then narrate. [Thinking, Fast and Slow, p.25, p.35-36]
   - 1:30-2:00 what is real, what is mocked, what breaks first, next step.
   - 2:00-3:00 their questions; fill the time if they have none, since later teams get less Q&A. [Seed: C, §C2]
   - Variants: 30-second version (official HackUTD tip), 60-second late-judge version, sponsor version that opens with the sponsor tech's effect. [Seed: A, §A1]
10. **Rehearsal gates (hours 20-22).** Timed out loud at least once; one cold run with a stranger, 5 minutes, no coaching, note where they stumble; record a 60-second screen-capture backup and the ~2-minute Devpost video. Go to judging only when the stranger can repeat the identity sentence and the live flow runs 3 times in a row from reset. [Seed: C, §C1, §C7] [Thinking, Fast and Slow, p.26, p.62-63]

## Checklists
**Table readiness (run before the window opens)**
- [ ] Demo pre-loaded at the start state; one-click reset tested; realistic seed data (5-10 coherent records, no "test test"). [Thinking, Fast and Slow, p.72-75]
- [ ] First screen readable from 6 feet; no error, spinner, or login on first view. [Thinking, Fast and Slow, p.64-65]
- [ ] Table sign or one-pager shows name, identity sentence, and one screenshot of the running product. [Seed: C, §C7]
- [ ] Recorded backup plays offline; nothing depends on venue wifi.
- [ ] Roles set: one talks, one drives, one handles questions and arriving judges. [Hackathon Planning Kit, p.7]
- [ ] Team has eaten and rested before the last rehearsal. [Thinking, Fast and Slow, p.43-45]

**Pitch and claims self-check**
- [ ] First sentence names product and user; no market size, backstory, or stack talk before it.
- [ ] Tagline appears at open, demo moment, close, and on the poster, word for word.
- [ ] Every number tagged and recomputed; no "would use it" survey results presented as demand. [The Mom Test, p.29-30]
- [ ] Every mock is labeled out loud; we never say "we have no competitors." [Zero to One, p.23-24]
- [ ] "What breaks first" answer is honest and specific.
- [ ] No "we didn't have enough time." [Seed: C, §C2]

**Submission (HackUTD rules)**
- [ ] Repo public and staying public; commit history shows work inside the window; AI tools and libraries disclosed. [Seed: B, §B1]
- [ ] All four teammates on the one Devpost project; registered by Saturday 11:00 PM, final by Sunday 12:00 PM (confirm 2026 times); at most two sponsor tracks. [Seed: A, §A2]
- [ ] Video about 2 minutes on a public host; screenshots or GIFs show only what actually works. [Seed: A, §A2]
- [ ] Devpost, video, poster, and table pitch make identical claims.

## Anti-patterns
- **Context before product.** Tell: the first 20 seconds contain a statistic or "imagine if" and no product name. Fix: identity sentence first, problem second. [Seed: C, §C7]
- **Feature tour.** Tell: the driver says "and we also..." more than twice. Fix: one flow, one "this is now possible" moment, contrasted with the old pain. [Seed: C, §C1]
- **Platform instead of tool.** Tell: the description uses "platform" or serves three user types. Fix: name one user and one moment. [Seed: What is Y Combinator?, §Improving Your Answers] [Hackathon Planning Kit, p.7]
- **Talking over the demo.** Tell: explaining architecture while the result animates. Fix: one channel at a time; pause on the payoff. [Thinking, Fast and Slow, p.25, p.35-36]
- **Blurring what was built this weekend.** Tell: you cannot answer "which parts existed before?" in one sentence. Fix: prepare the split and disclose it. [Seed: C, §C7]
- **Hiding limitations.** Tell: "nothing really breaks." Fix: the accusation audit answer, stated first. [Never Split the Difference, p.55-59]
- **Backend-heavy, front-end-empty.** Tell: at hour 14 the UI is a form with JSON output. Fix: shift a teammate to the visible path; judges only see the UX. [Seed: C, §C2]
- **Opening with an apology or glitch.** Tell: "sorry, it's a bit rough." Fix: open warm and energetic; one early oddity frames everything after, so switch to the backup within 10 seconds of a failure. [Thinking, Fast and Slow, p.55-56, p.72-74]
- **Trusting the team's own read.** Tell: nobody outside the team has seen the demo by hour 20. Fix: the stranger test. [Thinking, Fast and Slow, p.26, p.62-63]
- **Bolted-on sponsor tech.** Tell: the sponsor API could be deleted without changing the demo. Fix: make it carry the core loop or drop the track. [Hackathon Planning Kit, p.8]

## Hackathon calibration
- **Seibel's seven questions shrink to three.** Keep "what do you do" (with the user-path walkthrough), "progress" (what you built in 24 hours is the progress ratio judges feel), and "unique insight." Market size, team, and the ask are mostly noise at a table; keep one viability sentence in reserve. [Seed: What is Y Combinator?, §2-7]
- **The team plan's 9-part pitch does not fit a 2-minute slot.** Compress to identity, felt moment, live demo with technical centerpiece visible through its effect, honest limits. Hold differentiation and before/after evidence for Q&A or the finalist version.
- **Chan's 8-part startup demo (problem, solution, market, validation, demo, model, rollout, team)** is built for stage judging with investor panels; use it only if HackUTD runs a finalist round. [Seed: C, §C2]
- **Validation is cheap but must be honest.** One or two real conversations with target users (recorded, with photos) can win a business judge; report past actions, not "I would use it." [Seed: C, §C2] [The Mom Test, p.29-30]
- **Kahneman's findings are lab and field studies, not hackathon trials.** Use them as tie-breakers on delivery, never as a reason to cut working functionality for polish.
- **Ignore long-horizon advice** on defensibility moats, pricing tiers, and go-to-market plans except as a one-line Q&A answer. MLH briefs judges to weigh learning and creativity over commercial potential. [Seed: B, §B2, §B3]
- **At 4 minutes a visit, a judge can see at most about 45 tables in a 3-hour window (our arithmetic from the MLH timing).** Expect blurred memories by the end of a batch; the repeatable line and the one surprise are what survive. [Seed: B, §B2]

## Where experts disagree
- **Product first or problem first?** Seibel and Kurbaitaev say open with what it does; Minto says the whole message in 30 seconds. Bacon (JetBrains) and the planning kit say make the problem felt first or judges won't care. Follow: identity sentence in 10 seconds, then one concrete felt moment in under 20. Both camps are satisfied and the slot is not burned. [Seed: C, §C1, §C7] [Hackathon Planning Kit, p.7]
- **How much polish?** Yablonski and Kahneman show polish raises perceived usability and belief; Kurbaitaev saw polish past readability do nothing. Follow: polish the first screen and the demo path; stop there. [Laws of UX, p.111-116] [Seed: C, §C7]
- **Does the business case matter?** Chan and Clark lost to investable ideas with investor and BD judges; MLH tells judges to ignore the business side. Follow: HackUTD's general criteria include viability and impact, so keep one sentence ready, lead with it only for sponsor or business judges, and drop it for MLH tracks. [Seed: C, §C2, §C6] [Seed: B, §B1, §B3]
- **Does the pitch decide it?** Wong says judges only judge what happens in front of them; MLH does not score pitch quality. Follow: delivery matters for general and sponsor tracks; for MLH tracks spend the time showing technology and what you learned. [Seed: C, §C4] [Seed: B, §B1]
- **Is the video paramount?** The Substack winner says judges mostly watch the video; MLH's organizer guide says it is only a reference in deliberation at science-fair events. Follow: HackUTD is in-person science fair, so the table wins first, but deliberation uses the video, so it must show the same flow and claims. [Seed: C, §C3] [Seed: B, §B2]
- **Fake or real?** The planning kit endorses faking hard parts for ad hoc teams; CTO-type judges and Kurbaitaev probe what was really built. Follow: mock the periphery, keep one genuine core, label everything. [Hackathon Planning Kit, p.6, p.14] [Seed: C, §C2, §C7]
- **Newest tech or safe stack?** Clark lost to a team on a just-launched API and Wong favors trendy ideas; Molina warns against fragile stacks chosen to impress. Follow: new tech only where it carries the core loop and was proven in a feasibility spike by hour 4. [Seed: C, §C4, §C5, §C6]

## Go deeper
- search_experts("stack ranking top 3 judges batch scoring", domain="01-judging")
- search_experts("first impression System 1 opening minute demo", domain="01-judging")
- search_experts("judge fatigue parole decisions late slot", domain="01-judging")
- search_experts("what breaks first honest weakness judges questions", domain="01-judging")
- search_experts("sponsor judge will my company look good topic fit", domain="01-judging")
- search_experts("four judge types API CTO investor business development", domain="01-judging")
- search_experts("faking hard parts mock data prototype accepted", domain="01-judging")
- search_experts("cognitive ease legibility rhyme repetition belief", domain="01-judging")
- search_experts("accusation audit pre-empt objections", domain="01-judging")
- search_experts("what do you do email test two sentence pitch", domain="01-judging")
