---
name: 20-demo-delivery
description: Open when writing the demo script (hour 0-2), choosing what the demo shows and what gets mocked or recorded, setting feature freeze and rehearsal time, preparing the expo table, planning what to say when the live demo breaks, or coaching the speaker in the final 3 hours before judging.
---
# Demo design and presentation delivery

## Use this when
- Hour 0-2: writing the one-page demo script before real code, and picking the single payoff screen the build must reach.
- Deciding whether a feature appears in the demo, gets one sentence, or is cut.
- Deciding which demo segments run live, which use cached or mocked responses, and which run as recorded video.
- The final 4 hours: feature freeze, backup video, rehearsal schedule, table setup.
- During judging: a judge walks up, a judge asks something off-path, or the live demo fails.
- After a bad judge visit: diagnosing what to change before the next one.

## Core principles
1. **Do the Last Thing First: show the finished result within the first 40 seconds, then the shortest path to it.** (counterintuitive) Judges decide whether they want the dish from the photo; building up to the payoff wastes the attention peak. [Seed: Great Demo: method in one page, §0]; open with the most dramatic highlight and be into point one inside 60 seconds [Berkun, p.91-92].
2. **Demo one golden path with 2-3 features at most; nothing on screen takes over 15 seconds.** Jobs showed 10 of 300 features, and every extra feature dilutes the message and adds a failure point. [Gallo, Steve Jobs, p.252-254]; Kawasaki's five S's [Gallo, Steve Jobs, p.243-246]; go deep or wide, not both [Reynolds, Naked Presenter, p.49].
3. **Optimize for the room, not for infrastructure: hardcode the path, mock externals, cache LLM output, seed realistic data.** (counterintuitive) Teams lose points for never reaching the payoff, not for imperfect plumbing. [Seed: Hackathon-specific sources, §B1]. Use real-feeling people and data, never "Test User 1" [Reynolds, Naked Presenter, p.56].
4. **Engineer one "pause button" moment and change the app until it exists.** The single emotionally charged moment is what judges recall and repeat to each other after 200 projects. [Seed: Hackathon-specific sources, §B3]; [Gallo, Talk Like TED, p.110-115].
5. **Show before and after on the same task, side by side, with a number in human units, then go silent.** People notice differences; a bare "92% accuracy" invites "is that good?" while "20 minutes saved per shift" lands. [Gallo, Steve Jobs, p.244-246, 252-253]; [Reynolds, Naked Presenter, p.115-116]; [Gallo, Steve Jobs, p.191-195].
6. **Never retry a failed step. Say one line, switch to the next segment or backup video within 10-15 seconds, narrate live over it.** (counterintuitive) Retrying usually fails twice (the Cybertruck window), and audiences judge recovery, not perfection. [Seed: Presentation delivery sources, §C3]; [Gallo, Steve Jobs, p.353-358].
7. **Narrate what is not on screen: the pipeline, the model you chose and why, how you checked its output.** Judges can see the clicks; in 2026 "we used an LLM" scores nothing, so the hidden engineering is the technicality score. [Seed: Hackathon-specific sources, §B2].
8. **One voice, one driver.** The speaker keeps eye contact while a teammate clicks in sync; mic handoffs burn seconds and break flow. [Seed: Hackathon demo kit, §A6]; [Seed: Presentation delivery sources, §C1].
9. **Rehearse the talk, not the slides: 4-5 timed, standing, out-loud runs, each targeting one named fix.** (counterintuitive) Nervous teams polish visuals instead, and plain repetition improves less than goal-plus-feedback runs. [Berkun, p.22]; [Reynolds, Naked Presenter, p.54-55]; [Gallo, Steve Jobs, p.311-312].
10. **Script to 80-90% of the slot and reserve 20-30% for questions.** Overrunning is the common failure, and judge questions are where judges engage most. [Reynolds, Presentation Zen, p.258-259]; [Berkun, p.200].
11. **Go deeper only where the judge pulls: Peel Back the Layers, park tangents, offer a menu to an unknown judge.** A CTO judge wants model and architecture, a business judge wants who pays and the Delta; one fixed tour fits neither. [Seed: Great Demo: Do It / Peel Back the Layers, §B4]; [Seed: Great Demo: Menu Approach, §B8].
12. **Energy and enthusiasm multiply, but substance still gets probed.** In the Dr. Fox study a content-free speaker was rated highly, so delivery buys credit; keep every claim checkable on the spot. [Berkun, p.127-130]; most presenters sit at 3-6 of 10 on energy and should overshoot [Gallo, Steve Jobs, p.321-323].

## Decision procedure
Main decision: what the demo shows, in what order, and what runs live vs cached vs recorded.

1. **Confirm format** at opening ceremony or Discord: expo table, stage, or both; minutes per judge. Default until confirmed: expo, 3-5 min including questions, 2-3 hour window, every judge a fresh first impression. [Seed: Hackathon-specific sources, §B7]
2. **Write the one-page script by hour 2** with these fields: persona and problem, before state and its cost, trigger, pause-button moment, result with before/after number, close, failure lines. [Seed: Hackathon demo kit, §A1]. STOP if you cannot name the persona, the cost (Delta), and why now: that is missing discovery, not missing code. [Seed: Great Demo: Situation Slide, §B1]
3. **Pick the Illustration** (the one payoff screen). Go test: a teammate who did not build it understands the value in 10 seconds with the sound off. Fail: redesign the screen or the feature, not the narration.
4. **Cut features.** For each demo step write one sentence on what the judge should conclude; delete steps without one [Berkun, p.93-95]. Cap: 3 messages, one feature each [Gallo, Steve Jobs, p.100-102]. Everything else goes to Q&A or the README.
5. **Time each step.** Anything over 15 seconds gets precomputed or time-warped (seed a finished state, start the job, jump to the result). [Seed: Great Demo: Do It / Peel Back the Layers, §B4]
6. **Risk-rate each segment:** picture the failure, its impact, how fast you recover. If catastrophic and not recoverable in 10 seconds, that segment runs from video or a cached response. Any dependency on venue Wi-Fi, a third-party API, or a live LLM runs behind a single demo-mode switch with cached output. [Seed: Presentation delivery sources, §C3]
7. **Milestones:** visible click-through flow (placeholders fine) by about hour 6; working demo by the halfway point; feature freeze 4 hours before submission. [Seed: Hackathon demo kit, §A3]
8. **Rehearse.** Go when 3 consecutive runs finish under 90% of the slot and an outsider can repeat what it does in one sentence. If over time, cut a segment; never speed up. [Gallo, Talk Like TED, p.150-151]
9. **Record the backup video twice the night before**, 2 minutes or less, saved locally and as a public YouTube link for Devpost. [Seed: Hackathon demo kit, §A3]; [Seed: Hackathon-specific sources, §B8]
10. **Count safe runs.** Know how many runs the demo survives before API quotas or dirty data degrade it, and keep a reset script. [Seed: Presentation delivery sources, §C3]

Default 3-minute shape [Seed: Great Demo: translation to HackUTD, §A]:
| Time | Beat |
|---|---|
| 0:00-0:20 | Situation: one person, their problem, the cost, why now |
| 0:20-0:40 | Illustration: "here is what she gets" |
| 0:40-1:30 | Do It: fewest clicks from start to that result |
| 1:30-2:20 | One layer down: the hard tech and why it matters |
| 2:20-2:45 | Summary: before, after, Delta, next step. Then stop. |
Expo opener: problem, solution, impact in under 30 seconds, then hand the judge the product. [Seed: Hackathon demo kit, §A2]

## Checklists
**Script audit (run on the draft)**
- [ ] First sentence contains a person, a pain, and a payoff; no team name or stack names. [Gallo, Steve Jobs, p.49-51]
- [ ] Payoff screen appears before 0:40.
- [ ] No "if", "or", "also" in the core flow. [Seed: Great Demo: Do It / Peel Back the Layers, §B4]
- [ ] Every number has a baseline or a human-unit translation; 2-3 numbers total. [Gallo, Steve Jobs, p.202]
- [ ] Model named, reason it beat the obvious alternative, how output was checked.
- [ ] Hard problem framed as "the hard part was X, we solved it with Y".
- [ ] Mocked parts are known to the speaker and disclosed if asked.
- [ ] Close is one line: "[persona] goes from [before] to [after], built on [hard tech]", then team and product name, then silence. [Seed: Great Demo: translation to HackUTD, §A]; [Seed: Hackathon demo kit, §A2]
- [ ] 30-second, 2-minute, and full versions exist; every teammate can give the 30-second one. [Reynolds, Presentation Zen, p.66]

**Final hour and table setup**
- [ ] App already open on the first screen, logged in, data loaded, URL bookmarked; no live typing of URLs or logins. [Reynolds, Naked Presenter, p.72, 78]
- [ ] Notifications off, other tabs closed, charger in, sleep disabled, adapter tested on the real display.
- [ ] Browser zoom 125-150%; text readable from 2 meters. [Duarte, slide:ology, p.143, 152]
- [ ] Backup video and screenshots open in a separate tab; backup operator named.
- [ ] Laptop angled so judges stand beside the speaker, not across a barrier. [Reynolds, Naked Presenter, p.123-126]
- [ ] Sign with team name, product name, headline, QR to Devpost and video. [Seed: Hackathon demo kit, §A5]
- [ ] Visible timer; one teammate signals one minute left. [Berkun, p.91-92]
- [ ] Speaker says "I'm excited" aloud, 5 slow breaths, water. [Seed: Presentation delivery sources, §C6]; [Reynolds, Naked Presenter, p.98-99]

**Failure readiness**
- [ ] Written failure line per risky step ("The network is slow, here is the recorded run").
- [ ] Every screen has a route home; segments run independently.
- [ ] Team has rehearsed one run with the laptop closed (outline only). [Gallo, Steve Jobs, p.317-318]; [Berkun, p.71-74]
- [ ] Nobody opens a terminal or editor in front of judges. [Seed: Hackathon demo kit, §A7]

## Anti-patterns
1. **Harbor Tour.** Sign: "and here's another screen..." with no target. Fix: open on the matching persona story, show the Illustration, then ask what they want to see. [Seed: Great Demo: demo diseases, §B9]
2. **Architecturitis / team-intro opener.** Sign: first slide is the stack or "We are team X and we built...". Fix: lead with the problem moment; architecture is one layer down or in Q&A. [Seed: Great Demo: demo diseases, §B9]; [Gallo, Steve Jobs, p.58-62]
3. **Retrying the broken step or debugging live.** Sign: clicking the same button a third time, terminal on screen. Fix: one line, switch to backup, restate the value. [Seed: Hackathon demo kit, §A7]
4. **Apologizing.** Sign: "sorry, it's rough, we only had 24 hours", "it normally works". Fix: frame gaps as "next step is X"; judges already know it is a 24-hour build. [Reynolds, Naked Presenter, p.83]
5. **Making judges watch setup.** Sign: logins, file hunting, a dead spinner. Fix: pre-stage state; if setup is unavoidable, ask the judge a question while it loads. [Reynolds, Naked Presenter, p.72, 78]
6. **Narrating the clicks.** Sign: "now I click Submit." Fix: use those seconds for the hidden work and the "why". [Seed: Hackathon-specific sources, §B2]
7. **Feature creep in the script.** Sign: "you could also...", showing a 6-hour backend piece because it was hard. Fix: 10 seconds or Q&A backup. [Reynolds, Presentation Zen, p.65-66]
8. **Reading slides or text-heavy screens.** Sign: over 7 words on a slide, speaker facing the screen. Fix: one image or number per slide; people cannot read and listen at once. [Reynolds, Presentation Zen, p.20-21]; [Gallo, Steve Jobs, p.156-165]
9. **Trailing off.** Sign: "so yeah, that's it, any questions?" Fix: scripted close, then "is there anything you'd like me to go deeper on?" [Reynolds, Naked Presenter, p.176-182]; [Berkun, p.101-102]
10. **Trusting polite praise.** Sign: "great job!" and no change between visits. Fix: ask each judge or visitor "what did you expect us to answer that we didn't?" and adjust the next pitch. [Berkun, p.123-133]

## Hackathon calibration
- **Discovery collapses to one question.** Cohan's Situation Slide assumes calls before the demo. At a table, ask "what's your background?" or "what are you looking for in a project?" and pick the technical or the benefit cut. [Reynolds, Naked Presenter, p.47-48]; [Seed: Great Demo: starting when you don't know the audience, §B7]
- **Cohan's timings shrink 10x.** His Do It Again (5-10 min) and Q&A (5-10 min) become one peeled layer and judge questions. The 10-minute attention rule (strong evidence [Berkun, p.87-89]) becomes a mode change every 60-90 seconds and the strongest moment in the first minute.
- **Rehearsal is hours, not weeks.** Jobs rehearsed for days; protect a 2-3 hour block at the end and do 5 runs. Feature freeze is what makes that block real. [Gallo, Steve Jobs, p.307-312]
- **Tech-failure cutoff drops from 10 minutes to about 10-15 seconds.** Berkun's 10-minute troubleshoot window is for conference talks; at a table the judge leaves. [Berkun, p.196, 201]; [Gallo, Steve Jobs, p.353-358]
- **Slides mostly disappear at the table.** For 1-3 judges lead with the live product and one visual; keep 1-4 slides for stage and a backup set for Q&A. [Reynolds, Presentation Zen, p.19, 277-278]; [Seed: Presentation delivery sources, §C5]
- **Repetition is the hidden load.** 15-30 pitches in a 2-3 hour window: rotate presenters, water, reset after each visit, treat every judge as the first. [Seed: Hackathon demo kit, §A5]; [Reynolds, Naked Presenter, p.85-88]
- **Sleep loss flattens delivery.** Do a 5-minute loud warm-up before judging and overshoot energy. [Gallo, Steve Jobs, p.321-323]
- **Let the judge drive, but only after your core flow,** on one pre-tested task under 30 seconds. [Berkun, p.145-149]; Cohan warns to let the audience drive only after practicing it [Seed: Great Demo: Do It / Peel Back the Layers, §B4]
- **The video is a second judge.** Judges may not watch past 2 minutes: hook in 15-20 seconds, proof by 60-90. Polish does not score; clarity does. [Seed: Hackathon-specific sources, §B9]
- **Ignore:** company-overview openers, multi-role "rank order" chunking beyond one panel, Kawasaki's full 10-slide deck, financial projections unless a track asks.

## Where experts disagree
- **How long on the problem.** Gallo and HackerEarth put about a third of the pitch on the problem [Gallo, Steve Jobs, p.120-138]; [Seed: Hackathon-specific sources, §B1]. YC says keep it short and do not bury the lead [Seed: Presentation delivery sources, §C1], and Cohan says show the payoff first. Follow: 15-25 seconds of one person's problem, then the Illustration. The pain returns as the "before" half of the contrast, so it gets more screen time without delaying the payoff.
- **Admit what was hard?** Reynolds says put the struggle in the foreground [Reynolds, Presentation Zen, p.85] and AngelHack says name the hardest engineering decision; Salesforce says never volunteer problems [Seed: Hackathon-specific sources, §B3]. Follow: name the hard problem as an accomplishment ("we assumed X, data said Y, we built Z"); never list bugs or missing features.
- **Open with a story or a stat.** Gallo says delay the first statistic [Gallo, Talk Like TED, p.40-41]; Reskilll opens with one sentence plus one statistic [Seed: Hackathon-specific sources, §B4]. Follow: open on the named person, and make the one number that person's cost.
- **Handoffs.** Gallo says hand each part to the teammate who knows it best [Gallo, Steve Jobs, p.228-231]; YC says one presenter, no handoffs [Seed: Presentation delivery sources, §C1]. Follow YC for the pitch (2 people at most: speaker plus driver), Gallo for Q&A, where pre-assigned owners answer their bucket.
- **How to close.** Cohan summarizes at every chunk end [Seed: Great Demo: summarize and chunking, §B6]; Gallo says end on a showstopper, not a summary [Gallo, Talk Like TED, p.125-127]; Reynolds says end on a story, not an argument [Reynolds, Naked Presenter, p.175-177]. Follow: one sentence that returns to the opening person's before and after (story plus summary in one line), then the name, then stop.
- **Humor.** Gallo's Jobs book suggests one planned joke [Gallo, Steve Jobs, p.358-360]; Talk Like TED and Naked Presenter say no jokes [Gallo, Talk Like TED, p.130, 133-134]; [Reynolds, Naked Presenter, p.76-77]. Follow: no jokes; get the smile from playful demo data (a judge's school, a local landmark) [Gallo, Steve Jobs, p.248-251].

## Go deeper
- search_experts("do the last thing first illustration payoff screen", domain="20-demo-delivery")
- search_experts("demo one feature five S's short simple swift", domain="20-demo-delivery")
- search_experts("demo failure never retry backup video recovery line", domain="20-demo-delivery")
- search_experts("side-by-side comparison silent beat before after", domain="20-demo-delivery")
- search_experts("jaw-dropping wow moment build up", domain="20-demo-delivery")
- search_experts("peel back the layers parking lot menu approach", domain="20-demo-delivery")
- search_experts("rehearse deliberately record yourself filler words", domain="20-demo-delivery")
- search_experts("never make the audience watch you boot up opening PUNCH", domain="20-demo-delivery")
- search_experts("dress up numbers human units comparison", domain="20-demo-delivery")
- search_experts("expo table setup judge walks up 30-second opener", domain="20-demo-delivery")
