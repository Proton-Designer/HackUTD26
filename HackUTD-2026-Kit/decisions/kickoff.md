---
name: kickoff
description: Load at H0:00-H1:00 of HackUTD (opening ceremony through sponsor challenge reveal) to set roles, the Decider, the team agreement, the hour plan and the track shortlist, and again at H1:30 when the idea is locked and the track choice must pass the sponsor delete test.
---
# Decision guide: kickoff

## Open this when
- **H0:00-H0:20:** hacking has started and nobody has written down who decides, how ties break, or when anything is due.
- **H0:15-H1:00:** sponsor challenges are announced and the team must shortlist the general track plus at most two sponsor tracks and any MLH prizes.
- **H1:30 (idea lock):** re-run the track gates against the chosen idea; drop any track whose tech is bolted on. Hand idea choice itself to the idea-selection guide.
- **Any hour before Saturday 11:00 PM:** nobody has created the Devpost project and invited all four teammates yet (confirm the 2026 time).

## Steps
1. **Facts card (H0:00-0:10).** Ask an organizer five questions and write the answers on the wall: minutes per judge visit (plan for 4: 2 demo, 1 Q&A, 1 travel), judging window length, whether finalists present again (about 7 minutes if so), which judges cover which tracks, and the 2026 Devpost registration and final-submit times. [Seed: A. HackUTD-specific, §A1] [Seed: B. Standard rubrics and how judging is run, §B2]
2. **Register now, not later (H0:10).** Create a blank Devpost project, invite every teammate by their Devpost email, create the public repo. Placeholder links are allowed until Sunday; missing the Saturday registration step or a teammate is not. [Seed: A, §A2]
3. **Team agreement, one page (H0:10-0:25).** Decider named aloud. Tie-break rule: area owner decides; if it is a cross-area call, a 30-minute test; if reversible, coin flip. Debate cap 5 minutes. Stuck rule: 30 minutes blocked means say it aloud; at 45-60 minutes ask "if we had not spent this time, would we start this now?" and switch or mock if no. Nobody merges on red. [Stickdorn et al., This Is Service Design Methods, p.571-572] [Bland and Osterwalder, Testing Business Ideas, p.161] [Kahneman, Thinking Fast and Slow, p.335]
4. **Roles by slice, not by layer.** Map the team plan's four ownership areas to: two slice owners (each owns one part of the demo flow from UI to data), one integrator (deploy, one-script redeploy, merges, seams), one evidence and pitch owner who also codes. Everyone must be able to run and redeploy the app. [Singer, Shape Up, p.96-97] [Fried et al., Getting Real, p.29-30]
5. **Track survey (H0:15-0:50).** For every track, write one line: "This track wants X; we deliver X by Y." Ask each sponsor rep two things: "Which of your products would you want to see carrying the core of a project?" and "What result would you be proud to announce as your winner?" The second is the real test, because sponsor judges ask "if I reward this, will my company look good?" [Hackathon Planning Kit, p.5-6, p.8] [Seed: C. Writeups from judges and repeat winners, §C3]
6. **Score tracks with the Template grid.** Gates, any fail drops the track: (a) delete test, the demo changes if the sponsor tech is removed; (b) the topic is one the sponsor cares about, not one we like; (c) at most two sponsor tracks. Prefer spec-based bounties over open "best overall" prompts, since they draw fewer entries. Add an MLH prize only if its tech is already in the stack; MLH judges score technology, design, completion and learning, not pitch or originality. [Hackathon Planning Kit, p.8] [Seed: C, §C3] [Seed: A, §A3] [Seed: B, §B1]
7. **Shortlist is provisional until H1:30.** After idea lock, re-run gate (a) on the real idea. If a track fails, drop it the same minute; do not bolt on.
8. **Noise audit (right after idea lock, 5 minutes).** Each person privately writes the one-line pitch, the target user, and a 0-100 score for the idea. Reveal together. Spread over 25 points, or two different users named: stop and resolve before code. [Kahneman et al., Noise, p.28-29, 32-33]
9. **Size the build (H1:30-2:00).** Real capacity is about 40-48 person-hours, not 96. Estimate each feature, multiply anything touching a new API, model or deploy path by 1.5-2x, rank, and draw the cut line so must-ship uses at most half of capacity. Below the line goes on a visible "NOT doing" list. [Brooks, Mythical Man-Month, p.109, p.33-34] [Kahneman, Thinking Fast and Slow, p.242-243]
10. **Contracts, setup, spike (H2:00-4:00).** Write 2-3 interface contracts (API shape, record format) and commit mock versions so slices build in parallel. One lockfile, one setup script; every teammate runs the app locally before splitting. Spike the riskiest dependency with written acceptance criteria and a hard stop by H3; if it fails, swap or fake it. [Martin, Clean Architecture, p.155] [Lakshmanan et al., Generative AI Design Patterns, p.445-448] [Bland and Osterwalder, Testing Business Ideas, p.306-308]
11. **Write the clock on the whiteboard** (Template, part C). Times are commitments, not hopes.
12. **State the decision.** The Decider says aloud the tracks chosen, the roles, and the principle behind each choice with its citation, and pastes it into one pinned decision doc. Chat carries only the link. [Richards and Ford, Fundamentals of Software Architecture 2e, p.697-698]

## Template
```
KICKOFF ONE-PAGER                       (pin it; Decider signs at H1:30)

A. FACTS CARD
Visit length: __ min   Judging window: __ h   Finalist round: Y/N, __ min
Judges per track: General ____  Sponsor ____  MLH ____
Devpost registration: Sat __:__   Final submit: Sun __:__
[ ] Blank Devpost project created   [ ] All 4 invited   [ ] Repo public

B. TRACK GRID   (gates are pass/fail; one fail drops the track)
Track | Wants X | We deliver X by Y | Delete test | Sponsor's topic? | Spec bounty? | P(top 3 of that judge's batch) 0-100 | Keep?
______|_________|___________________|_____________|__________________|______________|______________________________________|______
______|_________|___________________|_____________|__________________|______________|______________________________________|______
Rep answers: "carries the core" = ____  "proud to announce" = ____
Chosen: General + Sponsor 1 ____ + Sponsor 2 ____ (optional) + MLH ____
Principle + citation: ________________________________________________

C. CLOCK
H1:30 idea lock (hard stop H3)        H3    spike verdict
H6    checkpoint 1                    H8    thin end-to-end slice runs
H9-10 user test slot 1                H8    last full pivot (only one)
H12   checkpoint 2, full path live, 10-min retro (1 stop, 1 start)
H14   feature freeze                   H16   stretch cut, H18 code freeze
H18-19 user test slot 2               H19   core not live -> mock or record it
H20   demo deployment frozen          H20-23 rehearsal, at least 5 timed runs
H22   checkpoint 4                    Sleep shifts: __ / __ / __ / __
Checkpoint = 10 min max: expected, happened, continue?, cut? (% time vs % done)

D. TEAM AGREEMENT
Decider: ____   Tie-break: owner / 30-min test / coin if reversible
Slice owner 1: ____ (flow part ____)   Slice owner 2: ____ (flow part ____)
Integrator: ____   Evidence + pitch: ____
Stuck: 30 min say it; 45-60 min sunk-cost question aloud
Merge: hourly, never on red   Debate cap: 5 min
Noise audit spread: __ points  Same user named? Y/N

E. SCOPE
Capacity ____ person-hours x 0.5 = must-ship budget ____
Must-ship (est x risk factor): ____ / ____ / ____
NOT doing: ____ / ____ / ____
Demo acceptance: "Input ____ produces ____ in under __ s on stage."
Contracts committed with mocks: [ ] ____ [ ] ____ [ ] ____
```

## Principles
1. **Pick tracks to land in a judge's top 3, not to collect prize entries (counterintuitive).** Judges likely name a top 3 (3/2/1 points), so a forgettable entry scores zero from that judge, and with about 200 projects the general prize alone has a low base rate. [Seed: B. Standard rubrics and how judging is run, §B2] [Kahneman et al., Noise, p.145-146]
2. **A sponsor track is worth entering only if its tech carries the core loop and the topic is the sponsor's.** Sponsors judge like customers; an entry on the sponsor's trend beat a comparable one on the team's interest, and past HackUTD winners stacked prizes by making sponsor tech central and naming a concrete recipient (TxDOT, State Farm customers). [Seed: C. Writeups from judges and repeat winners, §C3] [Seed: A. HackUTD-specific, §A3] [Hackathon Planning Kit, p.8]
3. **Plan on 40-48 real person-hours and commit to half of what seems to fit (counterintuitive).** Only about half of clock time becomes build-and-debug, and plans are near best case, so a "24h x 4" plan overruns by default. [Brooks, Mythical Man-Month, p.109] [Kahneman, Thinking Fast and Slow, p.242-243]
4. **Give each person a vertical slice plus written contracts, not a frontend/backend/AI layer (counterintuitive).** Layer splits need heavy coordination per feature and integration overflows when left late; mocked contracts let slices run in parallel and double as demo fallbacks. [Singer, Shape Up, p.96-97] [Lakshmanan et al., Generative AI Design Patterns, p.445-448]
5. **Collect votes privately before anyone speaks, then the Decider calls it.** Once the first voice is heard, judgment cascades; consensus voting yields compromise and an absent decider means relitigating later. [Knapp, Sprint, p.28-29, p.111-114] [Kahneman et al., Noise, p.91-93]
6. **Run a noise audit before code (counterintuitive).** Teams that feel aligned usually are not; a 25+ point spread or two different users exposes it in 5 minutes. [Kahneman et al., Noise, p.28-29, 32-33]
7. **Build the clock around integration and testing, not coding.** Brooks's split is 1/3 plan, 1/6 code, 1/2 test, so the walking skeleton must be public by H3:30, the thin slice must run by H8 and the live path by H12, not H14. [Brooks, Mythical Man-Month, p.37] [Martin, Clean Architecture, p.129-130] [Seed: C, §C7]
8. **Lock irreversible choices (tracks, architecture, story) before about H10 while rested.** Fatigue pushes toward quick fixes and acceptance of false claims, and the tired decider cannot feel it. [Kahneman et al., Noise, p.82] [Kahneman, Thinking Fast and Slow, p.80-81]
9. **Spike the riskiest dependency with acceptance criteria and a hard stop at H3.** Late dead ends are the costly ones; new tech earns a place only where it carries the core loop and survived the spike. [Cagan, Inspired, p.141] [Bland and Osterwalder, Testing Business Ideas, p.306-308] [Seed: C, §C4-C6]
10. **Make syncs about what is next and stuck, and merge hourly without meeting.** "What I did" stand-ups crowd out problem solving and interruptions reset focus, yet the sync is where breakthroughs come from. [Stickdorn et al., This Is Service Design Methods, p.598-600] [Fried et al., Getting Real, p.66-67] [Martin, Clean Architecture, p.129-130]
11. **Put test slots and rehearsal on the clock now as fixed events.** If someone must decide when to test, it does not happen; cut polish before cutting these. [Krug, Rocket Surgery Made Easy, p.36-37] [Gallo, Presentation Secrets of Steve Jobs, p.307-312]

## Mistakes
- **Layer split.** Tell: roles read "frontend, backend, AI, pitch" and nothing runs end to end at H10. -> Two slice owners, one integrator, one evidence and pitch owner; thin slice by H8. [Singer, Shape Up, p.96-97]
- **Assumed alignment.** Tell: "we all get it," but nobody wrote the pitch down privately. -> Noise audit; resolve any 25+ point spread before code. [Kahneman et al., Noise, p.28-29]
- **Track chosen by prize size or team taste.** Tell: the sponsor API could be deleted and the demo would look the same. -> Delete test; enter at most two tracks where the sponsor's topic is the project's topic. [Hackathon Planning Kit, p.8] [Seed: C, §C3]
- **Copying a past winner's story.** Tell: "last year a hardware project won, so we need hardware." -> Tag 10-20 past projects by features and keep only features that recur across winners and not losers. [Kahneman et al., Noise, p.136-139]
- **Twenty hours of features on the plan.** Tell: the must-ship list fills the whole capacity. -> Cut to half; everything else goes on the NOT-doing list. [Brooks, Mythical Man-Month, p.109]
- **Loudest-voice kickoff.** Tell: the first person to speak sets the track and the idea. -> Silent writing, private straw poll, Decider calls it. [Knapp, Sprint, p.88, p.111-114]
- **All-nighter as the plan.** Tell: "we'll push through tonight," no sleep times on the board. -> Staggered 90-minute shifts at the overnight low, open problem written on a card before sleeping. [Rumelt, Good Strategy Bad Strategy, p.61-63] [Johnson, Where Good Ideas Come From, p.79-80]
- **Devpost left for Sunday.** Tell: at H6 nobody has created the project. -> Blank project and all invites in the first 10 minutes. [Seed: A, §A2]

## Hackathon calibration
- **Ceremonies compress, the shape stays.** Daily standups and weekly planning become a 10-minute checkpoint every 3-6 hours, and one 5-10 minute retro at H12 that yields one stop and one start, checked at H18. [Bland and Osterwalder, Testing Business Ideas, p.67-76] [Crispin and Gregory, Agile Testing, p.485-487]
- **Design time shrinks to about 2-4 hours total.** Cap architecture design at about 45 minutes at kickoff; interfaces first, no refactors after H18. [Ousterhout, Philosophy of Software Design, p.28-31] [Richards and Ford, Fundamentals of Software Architecture, p.32, p.103]
- **The team plan's competition brief becomes the facts card.** Full problem evidence, user research and sponsor-fit statements belong to later guides; kickoff only needs facts, tracks, roles, clock and scope.
- **Base rates are directional.** Kahneman and Noise findings come from lab and field studies, not hackathons; use them to set thresholds, not as precise odds.
- **Ignore** long-horizon advice on hiring, team-of-teams structure, monthly decision cadence and moats. Nothing there changes a 24-hour plan.

## Go deeper
- [../domains/18-team-execution.md](../domains/18-team-execution.md) for checkpoint rules, freeze go/no-go, booth roles.
- [../domains/01-judging.md](../domains/01-judging.md) for rubrics per judge type, HackUTD rules and past winners.
- search_experts("Decider straw poll independent votes cascade", domain="18-team-execution")
- search_experts("noise audit illusion of agreement team", domain="18-team-execution")
- search_experts("productive hours half the clock estimate overrun", domain="18-team-execution")
- search_experts("sponsor judge will my company look good topic fit", domain="01-judging")
- search_experts("HackUTD VI winners sponsor prizes TxDOT State Farm", domain="01-judging")
