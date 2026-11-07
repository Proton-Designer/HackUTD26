---
name: pitch-demo
description: Load at hour 1-2 to write the demo script before code, at hour 12-16 to cut the demo to one path, in the final hours to freeze, rehearse, and submit to Devpost, and during judging when a judge walks up or the live demo or hardware breaks.
---
# Decision guide: pitch-demo

## Open this when
- **Hour 1-2:** the idea is locked; the team needs the script and the single payoff screen the build must reach.
- **Hour 12-16:** deciding which features appear in the demo, which get one sentence, and which run live, cached, or from video. The path must run live by hour 12; unfinished work is cut at hour 16.
- **Last hours:** demo freeze, backup video, rehearsal, table setup, and the Devpost submission (see Submission).
- **Judging window:** a judge arrives, asks something off-path, or a live step or device fails.

If the team is already past an hour below, do what the current hour needs; do not list what they missed.

## What to hand the team
Give finished output with their names and facts filled in: the timed script with a speaker per line, the Q&A owner list, the cut list, the submission checklist with owners. Placeholders (____) only where a fact is unknown; never invent numbers, quotes, or features. Cite a principle only when it changes the team's mind.

## Steps
1. **Confirm the format.** Ask an organizer: minutes per visit, judging window, whether finalists present again (about 7 minutes). Until confirmed, plan 4 minutes: 2:00 spoken, at least 90 s of questions, the rest travel. [Seed: B. Standard rubrics and how judging is run, §B2]
2. **Inventory what is built before writing a word.** List each feature as LIVE (runs now on the demo machine), CACHED (real output, replayed), MOCKED (fake), or NOT BUILT. The script may only claim LIVE and CACHED work; MOCKED is labeled out loud; NOT BUILT appears only as "next, we'd add ____." Re-run this inventory at hour 12 and hour 18, because the plan and the build drift apart. [Obviously Awesome, p.26-27]
3. **Write the script (Template A).** Three voices, each segment mapped to the judging criterion it earns. STOP if you cannot name the persona, the before-state cost in human units, and why now: that is missing discovery, not missing code.
4. **Pick the payoff screen.** Test: a teammate who did not build it gets the value in 10 seconds with the sound off. Fail: redesign the screen, not the narration.
5. **Cut the flow.** One sentence per demo step stating what the judge should conclude; delete steps without one. Cap 3 steps, one feature each. Anything over 15 s is precomputed or seeded to a finished state.
6. **Risk-rate each step.** Not recoverable within 10 s: it runs cached or from video. Put venue Wi-Fi, third-party APIs, live LLM calls, and hardware behind one demo-mode switch that replays captured real output. Keep a reset script.
7. **Hardware or flaky integration: diagnose the failing layer before judging, not at the table.** Reproduce the failure, then change one thing at a time in this order: power (laptop USB port vs powered hub or wall supply; does it fail when a motor, LED strip, or radio turns on?), physical connection (reseat, swap the cable, tape or hot-glue it), port and driver (does the device enumerate; did the serial port name change after a replug?), firmware (read the serial log at the failure moment), then network (venue Wi-Fi, IP change, sleep). Write the cause in one line, fix it if the fix is small, and record 3-5 real sensor readings or responses so the app can replay them through the same interface when the device drops. [Clean Architecture, p.267-271] [Agile Testing, p.253-254]
8. **Hour 12 go/no-go.** The single path runs live end to end, or new work stops until it does. Hour 16: unfinished is cut, not demoed.
9. **Claims audit (hour 18).** One teammate tags every number on screen, script, and Devpost as measured, cited, or estimated; untraceable numbers are deleted. Stop if nothing real is left for a technical judge to poke. [Thinking, Fast and Slow, p.45-47]
10. **Q&A owner list (Template A, bottom).** One owner per question bucket, one 15-second answer each, answer first. Write the 3 harshest questions a judge could ask and script calm answers. [Never Split the Difference, p.55-59]
11. **Screen pass (hour 18-20).** Template C, demo path and first screen only, then stop.
12. **Rehearse (hours 20-23).** At least 5 timed, standing, out-loud runs with all three speakers, each fixing one thing a listener named. Cut about a third on the first run and move it into Q&A answers. Over time: cut a segment, never speak faster. Go when 3 runs in a row finish under 90% of the slot and the flow runs 3 times from reset. [Presentation Secrets of Steve Jobs, p.311-312]
13. **Record the backup video:** 2 minutes or less, hook in 15-20 s, proof by 60-90 s, saved locally and as a public link for Devpost. Only show what is LIVE or CACHED.
14. **During judging,** pick the variant (Template B) from one opening question. After each visit, ask "What did you expect us to answer that we didn't?" and fix the next pitch.

## Template

**A. Script (2:00 target, 300-380 words, hard stop 2:30; 3 speakers, 2 scripted handoffs)**
```
Headline (<=140 chars, names the product): ______  (same words on sign, Devpost title, repo)
Persona (also in seed data): ______   Before-state cost in human units: ______
Tracks entered: 1 ______ (stronger, lead with it)  2 ______
Speakers: S1 storyteller ____  S2 demo driver + narrator ____  S3 tech lead ____
          S4 timer, reset, backup tab, Q&A owner ____

Time       Who  Says / does                                          Criterion earned   Status
0:00-0:10  S1   Headline. No team intro, no stack names.            Usefulness
0:10-0:30  S1   [Persona] at [moment], [what goes wrong]. One       Impact
                number: her cost. Gap question: "How long do you
                think this takes by hand?"
                Handoff: "[S2], show them what [persona] gets."
0:30-0:40  S2   Payoff screen first.                                 UI/UX              LIVE/CACHED
0:40-1:25  S2   Shortest path on the hardest real input. Pause      Uniqueness,        LIVE/CACHED
                2 s on the key moment. Narrate the hidden work,      Technicality
                not the clicks.
                Handoff: "[S3] built the part that makes this work."
1:25-1:45  S3   "The hard part was ____; we solved it with ____     Complexity,
                [sponsor tech]. We checked its output by ____."      Technicality
1:45-1:55  S3   Real vs mocked, what breaks first, next step:       Viability
                "Next we'd add ____" (NOT BUILT items go only here).
1:55-2:05  S1   Close: "[Persona] goes from [before] to [after]."    Impact
                Headline. Stop. "What would you like to go deeper on?"

Numbers (max 3, each measured + baseline): 1 ____ vs ____  2 ____ vs ____
Failure line per risky step: "The [device/network] dropped; here is the recorded run." -> tab ____

Q&A owners (answer in 15 s, answer first; owner speaks, others stay quiet)
  Why not [existing tool / ChatGPT]?            ____
  How accurate is it / how did you test it?     ____
  What did you build this weekend vs reuse?     ____
  Why does [sponsor tech] matter here?          ____
  Privacy / data source / bias?                 ____
  What breaks first / how does it scale?        ____
  Business case / who pays? (one sentence)      ____
  What's next?                                  ____
```
Criteria above are the general track [Seed: A. HackUTD-specific, §A3]. For an MLH prize, relabel to technology, design, completion, learning [Seed: B, §B1]; for a sponsor track, to "does this make [sponsor] look good" [Seed: C, §C3]. A segment that earns no criterion for this judge gets cut.

**B. Variants (same spine; every teammate can give the 30 s one)**
```
30 s (hurried):  what it does / what problem / how it differs / why we care.
60 s (late or tired judge): headline -> payoff screen -> pause moment -> close.
Sponsor judge: open with what [sponsor tech] made possible; use their product names.
MLH judge:     technology, completion, what we learned; skip viability.
Technical judge: S3 leads after the payoff; answer first, then 2-3 supports.
Opening question: "What's your background?" or "Judging a specific track?"
```

**C. Screen and table check (hour 18-20, again before judging)** [Knaflic, Storytelling with Data, p.141-147] [Refactoring UI, p.34-35, 46-49] [Few, Information Dashboard Design, p.56-57]
```
[ ] Squint test: eye stops 3-5 times max; the largest element is the payoff.
[ ] Everything grey, one accent on the result (about 10% of the screen), one filled button.
[ ] Headline metric as a big number with its baseline on the same card ("3 min vs 20 min").
[ ] Charts: bars from 0, sorted, labeled directly, title states the takeaway; no pie, gauge, 3D.
[ ] Dark text on light; browser zoom 125-150%; read standing 2-3 m away on the real screen.
[ ] Empty and loading states styled; every click responds under ~400 ms.
[ ] Seed data: 5-10 coherent records, persona's name, a local touch.
[ ] Sign: product name, headline, screenshot, QR to Devpost and video.
[ ] Laptop angled so the judge stands beside the speaker; S4 holds a visible timer.
```

## Submission (last 60 minutes)
Assign one owner; a second teammate verifies. Confirm the deadline time with an organizer; registration and final submit are separate deadlines [Seed: A, §A2].
```
T-60 to T-55  [ ] Tick every track and prize box you qualify for, max two sponsor tracks. Do it first;
                  it is the easiest thing to forget. If one track is weak (its tech is not in the
                  core loop), say so to the team: keep the box only if it honestly qualifies, and
                  lead the pitch and Devpost with the stronger track. [Seed: A, §A2] [Seed: C, §C3]
              [ ] All 4 teammates appear on the project (invites accepted, not just sent).
T-55 to T-35  [ ] Fields: title = headline; tagline; What it does (first line = logline); How we
                  built it (sponsor tech named, mocked parts labeled); Challenges; What we learned;
                  Built with; try-it link; repo link; video link; 2-3 screenshots.
                  Every claim matches the script; NOT BUILT items appear only under "What's next."
              [ ] Repo public. Before flipping it: search the code and git history for keys
                  (grep for "sk-", "key", "secret", "token"); move them to .env; add .env to
                  .gitignore; commit a .env.example with blank values. Any key ever committed is
                  rotated, because deleting the file leaves it in history. [Software Architecture: The Hard Parts, p.31]
              [ ] README: one-line headline, how to run, screenshot.
              [ ] Video public or unlisted, under the length limit, plays logged out.
T-35          [ ] Save and submit the draft now, with every required field filled.
T-30 to T-15  [ ] Open an incognito window: the Devpost page, repo, video, and live URL each load
                  without your login. Click every link. Check the tracks show on the project page.
T-15          [ ] Final edits done and saved. Screenshot the submitted page. No edits after T-5.
```

## Principles
1. **Play for each judge's top 3 with one moment they can repeat.** Judges name a top 3 from their batch, so a forgettable project scores zero from that judge. [Seed: B, §B2] [Seed: Hackathon-specific sources, §B3]
2. **Claim only what runs (contradicts the hype instinct).** Judges poke at what they are told; a claim that fails under their hands costs trust in everything else, while unbuilt work said as "next we'd add" still shows viability. [Obviously Awesome, p.26-27]
3. **Three voices, scripted handoffs.** Varying speakers resets attention, and the person who built a part answers its questions best; each handoff sentence sets up the next payoff, so script it word for word. Keep it to 2 handoffs in a 2-minute slot. [Resonate, p.138-139] [Confessions of a Public Speaker, p.98]
4. **Payoff screen before 0:40 (counterintuitive).** Building up to the result spends the attention peak on setup. [Seed: Great Demo: method in one page, §0]
5. **Demo the hardest real input; let the judge verify one claim by hand (counterintuitive).** One demanding case proves more than a success rate. [Made to Stick, p.138-145] Hand over control only after the core flow, on one pre-tested task. [Berkun, p.145-149]
6. **Name your biggest weakness before the judge does (counterintuitive).** A real "what breaks first" raised scores; claiming nothing breaks cost credibility. [Seed: C. Writeups from judges and repeat winners, §C7] [Never Split the Difference, p.55-59]
7. **Person first, then at most 3 numbers in human units.** Adding statistics to a story cut giving from $2.38 to $1.43. [Made to Stick, p.151-153, p.131-134]
8. **Narrate the hidden engineering, never the clicks.** "We used an LLM" scores nothing; the pipeline, model choice, and how you checked output are the technicality score. [Seed: Hackathon-specific sources, §B2]
9. **Never retry a failed step; one line, switch within 10-15 seconds.** Judges score the recovery, not the failure. [Seed: Presentation delivery sources, §C3] [Gallo, Steve Jobs, p.353-358]
10. **Tech after the demo, as the answer to "how?"** An architecture slide first answers a question nobody asked yet. [Minto, p.34-36]
11. **Close on the persona's after-state, then one headline, repeated word for word by everyone.** "Thank you, questions?" reads as needy; a short repeated line is what survives deliberation. [Resonate, p.66-68] [Presentation Secrets of Steve Jobs, p.84-90]
12. **Shorten for late, tired judges.** Depleted evaluators default to "no," so switch to the 60-second version. [Thinking, Fast and Slow, p.45]

## Mistakes
- **One person talks for 2 minutes.** Tell: the script has one name. -> S1 story, S2 demo, S3 how and weakness; S4 runs the clock and owns Q&A buckets.
- **Pitching the plan, not the build.** Tell: a script line describes a feature nobody has run today. -> Check it against the step-2 inventory; demote to "next we'd add."
- **Unowned questions.** Tell: two teammates answer at once, or everyone looks at the speaker. -> Q&A owner list; the owner answers, others stay quiet.
- **Debugging hardware at the table.** Tell: unplugging and replugging while the judge waits. -> Failure line, replay tab, keep narrating; diagnose between visits.
- **Clean toy input with "Test User 1."** -> Seed realistic records and run your ugliest real case. [Reynolds, Naked Presenter, p.56]
- **Ending on "so, any questions?"** -> Scripted close, headline, silence, then "what would you like to go deeper on?"
- **Submitting in the last 5 minutes.** Tell: the draft does not exist at T-30. -> Draft submitted at T-35, verified in incognito, final at T-15.
- **Keys in a public repo.** Tell: `.env` or a hardcoded key in git history. -> Rotate the key, then fix .gitignore.
- **Polishing past readability.** Tell: hour 21 on animations, rehearsal count 1. -> Demo path first; polish beyond readability did not move scores. [Lidwell, p.30] [Seed: C, §C7]
- **Apologizing for the 24 hours.** Tell: "sorry, it's rough." -> "Next step is X"; judges know the time limit.

## Hackathon calibration
- **Clock.** Pitch books plan 18-20 minute talks [Pitch Anything, p.89-90]; here the spoken pitch is 2:00 with one before/after swing, the demo as the "could be." [Resonate, p.58-63]
- **Speakers.** Gallo caps a short slot at 2 speakers [Presentation Secrets of Steve Jobs, p.228-231]; we use 3 because each owns a criterion and the questions on it, with only 2 handoffs. If a teammate freezes on stage, give them Q&A buckets instead.
- **Failure cutoff.** Berkun's 10-minute troubleshooting window is for conference talks; at a table the judge leaves, so the cutoff is 10-15 seconds. [Berkun, p.196, 201]
- **Slides mostly disappear.** For 1-3 standing judges, lead with the live product; keep 1-4 slides only for a finalist stage, plus one backup slide with raw numbers and method. [Reynolds, Presentation Zen, p.19, 277-278]
- **Repetition is the hidden load.** Expect 15-30 pitches in 2-3 hours: rotate S1, reset after each visit, drink water. [Gallo, Steve Jobs, p.321-323]
- **Business case is one sentence.** Viability is a HackUTD criterion; lead with it only for sponsor or business judges, drop it for MLH.

## Go deeper
- [../domains/19-storytelling.md](../domains/19-storytelling.md): headline tests, number rules, Devpost write-up checklist.
- [../domains/20-demo-delivery.md](../domains/20-demo-delivery.md): live vs cached vs recorded, failure readiness, table setup.
- [../domains/01-judging.md](../domains/01-judging.md): rubrics per judge type, claims audit, Q&A buckets.
- [../domains/12-visual-design.md](../domains/12-visual-design.md): chart integrity, screen polish pass, Devpost thumbnail.
- [judge-qa.md](judge-qa.md): full answers to judge questions.
- search_experts("demo failure never retry backup video recovery line", domain="20-demo-delivery")
- search_experts("stub flaky dependencies hardware canned responses")
