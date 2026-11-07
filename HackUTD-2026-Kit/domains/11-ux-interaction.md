---
name: 11-ux-interaction
description: Open when laying out the judge-facing demo flow (hours 1-6), wiring loading/error/empty states around slow AI or API calls, deciding on onboarding, forms, confirmations or undo, running a hallway test or heuristic pass (hours ~10-12 and ~18-20), or doing the final polish and accessibility sweep before judging.
---
# User experience and interactive design

## Use this when
- Hour 1-6: turning the chosen idea into screens, and deciding what sits on the one screen a judge will touch.
- Wiring any LLM call, upload or fetch that takes more than a second into the demo path.
- Deciding between a wizard, a form, sample data or a template gallery for first run.
- A teammate wants a confirm dialog, a settings page, a custom gesture or "one more widget" on the main screen.
- Running a hallway test or heuristic review and deciding which findings to fix before the next round.
- The last 2-4 hours: polish, delete pass, accessibility pass, robustness checks before judges arrive.

## Core principles
1. **Design for a transient first-time user who decides in seconds.** At HackUTD each judge gives a project about 4 minutes on a science-fair floor; first impressions form in about 50 ms and rarely change, so the first screen must say what this is, what you can do, and where to start without narration. [Don't Make Me Think, p.114-129]; [Laws of UX, p.111-116]; [About Face, p.243-245]
2. **Deliver value before asking for anything (counterintuitive: no tour, no sign-up).** Open on a prefilled draft, seeded realistic data or 3 clickable example scenarios; most people fix a near-right result faster than they can describe what they want. Ask for any investment (save, follow, connect) only right after the first result, as one tap: people did about twice the work for a computer that had just helped them. [About Face, p.291-292, p.418-421]; [Hooked, p.92-98]; [Seed: Synthesis, §0.4]
3. **One primary action per screen, and separate "do it" from "configure it".** Decision time grows with options (24 jams drew attention but shoppers were one-tenth as likely to buy as with 6), and users run a function about 10 times for each time they configure it, so the big button runs the default and options hide behind a small link. [Laws of UX, p.64-66]; [About Face, p.292-294]; [Refactoring UI, p.46-49]
4. **Acknowledge every action within 0.1 s, show live progress past 1 s, and never let a live step exceed about 10 s.** Without feedback people double-submit or give up; staged status text and visible steps cut abandonment (Uber used this to reduce cancellations); when you estimate time, quote the long end so you beat it. [Design of Everyday Things, p.77]; [About Face, p.295-296]; [Laws of UX, p.98, p.156-161]
5. **Spend the novelty budget on exactly one interaction; use stock conventions for everything else.** Users carry expectations from other products, and a change that is only slightly better loses to the familiar; one Signature Moment is memorable, novelty everywhere is a learning tax. [Laws of UX, p.31]; [Design of Everyday Things, p.159-164]; [Microinteractions, p.47-48, p.222]
6. **Design all five states of every demo-path screen: blank, loading, partial, error, ideal.** Missing states make an app feel broken and are where demos fall apart; judges at the table often try a fresh account, so the empty state is their first impression. [Seed: Hackathon UX kit, §A2]; [Refactoring UI, p.189-192]
7. **Prevent, then repair, then message; prefer Undo to "Are you sure?" (counterintuitive).** Bounded controls and disabled-until-valid buttons stop most errors; if your guess is right about 80% of the time, act and offer Undo, because routine confirmations get dismissed by reflex and fail exactly when needed. [Microinteractions, p.139-141]; [About Face, p.228, p.681-683]
8. **Let the AI absorb messy input, but make its output checkable.** Parse free-text dates, units and formats and echo "we read this as X"; below a confidence threshold, ask for more input instead of showing a guess; when a judge cannot verify one answer, show 2-3 candidates as visual previews; word "we are having trouble" differently from "check your input". [Laws of UX, p.83, p.142-147]; [Designing Machine Learning Systems, p.206-207, p.381-382]; [Release It!, p.132]
9. **Visible signifiers beat hidden capability.** If a control needs a sign saying "tap here", fix the cue; text labels beat icon-only buttons (heart and star mean different things across products), and judges will never discover a swipe. [Design of Everyday Things, p.29-38]; [Laws of UX, p.75-77]; [Microinteractions, p.70-75, p.243]
10. **Polish the first screen, the peak and the end; hunt single flaws on the demo path.** People judge by the most intense and the final moment, not the average, and one glitch or confusing label spreads to the whole product (horns effect), so the last UI hour goes to the result screen, the closing frame and rough edges, not settings. [Laws of UX, p.94-95]; [Psychology of UX Design, p.169-177, p.294, p.299-300]
11. **Watch behavior, never trust praise (counterintuitive: a pretty build hides its problems).** Testers rate attractive designs as more usable even when they are not, and 5-person tests cannot detect small differences, so count hesitations and completions, and report "4 of 5", never percentages or "significant". [Laws of UX, p.123-124]; [Microinteractions, p.241]; [Don't Make Me Think, p.142-143]
12. **Hit the cheap accessibility floor, and treat it as a judging talking point.** 4.5:1 text contrast (3:1 for 18px+ or bold 14pt+), real labels, keyboard access, 44x44 px minimum tap targets and a non-color cue on every state take about 20-30 minutes; low contrast alone fails about 83% of top homepages. [Refactoring UI, p.131-135]; [Psychology of UX Design, p.30]; [Laws of UX, p.136-137]; [Seed: Accessibility baseline, §D]

## Decision procedure
Main decision: what goes on the judge-facing flow, how it behaves, and when it is good enough to stop changing.

1. **Write the core flow spec (hour 1-3, 15 min).** One primary user, the "aha" result screen, steps from landing to aha, pre-seeded data, what is mocked, and a verb-plus-object label for each screen's primary button ("Generate schedule"). [Seed: Hackathon UX kit, §A1]
   - Go: landing to aha is 3-4 steps or fewer. List every step from need to payoff on paper and keep deleting; compare the count with today's workaround. [Hooked, p.48-50]
   - Stop: if you cannot name one primary user whose needs cover the others, the scope is too broad; shrink it before building. [About Face, p.118-119]
2. **Set the screen budget.** Cap the app at 3 screens. Sort every feature into three buckets: used in the demo, occasional, rare. Only bucket 1 gets screen space; the rest go behind an "Advanced" toggle or onto the cut list. Delete any visible control that is "if time" so the demo never shows a dead button. [About Face, p.269-273, p.303-304]; [Refactoring UI, p.13-14]
3. **Name screens and controls in the user's words.** Write the user's nouns and verbs first; no screen named after an endpoint or table, no one-button-per-API layout. [About Face, p.47-49, p.300-301]
4. **Pick the one signature interaction.** Everything else comes from the component library unmodified (restyle color only). Give the signature interaction a 5-minute test with a non-teammate.
   - Go: a stranger performs it within about 10 seconds without explanation. [Design of Everyday Things, p.20]
   - Otherwise: add a visible conventional button beside it, or drop it.
5. **Set a latency budget per demo step.** Press state within 0.1 s; staged text or streamed tokens past 1 s ("Reading syllabus... Building schedule..."); anything that can exceed about 10 s live gets precomputed or cached, with a sample-data fallback if the API fails. [About Face, p.295-296]; [Seed: Interaction patterns, §C4]
6. **Build the five states for each demo-path screen** and write the three most likely failure messages (bad input, empty result, API failure), each with a one-click fix such as Retry or Use sample data. [About Face, p.677-678]; [Design of Everyday Things, p.82-84]
7. **Hallway test, round 1 at hour ~10-12, round 2 at hour ~18-20.** 3 people per round who are not on the team, one silent facilitator, a goal rather than instructions. Thresholds:
   - 5-second test: shown the first screen, the tester can say what it is and what they would click. [Don't Make Me Think, p.114-129]
   - Core task completed unaided in under 1 minute. [Don't Make Me Think, p.191-198]
   - Fix anything rated severity 3-4 (major or blocking), or hit by 2 of 3 (3 of 5) testers. Fix a 1-tester issue only if it takes minutes. Skip "kayak" problems where the tester recovered alone on the second guess. [Seed: Hackathon UX kit, §A3-A4]; [Don't Make Me Think, p.170]
   - For each stall, ask which is missing: motivation, ability or a trigger (a visible prompt). Fix ability first, by removing fields, clicks or choices, then renaming; help text comes last. [Hooked, p.44-45, p.56-57]; [Don't Make Me Think, p.168-170]
   - Take the top 3 problems, assign an owner to each, and ship the fixes before the next round.
   - Stop rule: if at hour 12 a stranger cannot finish the core path, freeze new features until they can.
8. **Feature freeze at hour ~18-20.** The remaining hours go to the peak and end screens, a 15-minute delete pass, the checklists below, and a recorded happy-path video as fallback. [Design of Everyday Things, p.242, p.248-250]; [Microinteractions, p.231-234]

## Checklists
**A. Per demo-path screen (run on your own output)**
- [ ] Exactly one filled primary button; secondary actions outlined or ghost; destructive actions kept apart and quieter, at least 8px from neighbors. [Refactoring UI, p.46-49]; [Laws of UX, p.38, p.41]
- [ ] The follow-up control (confirm, next, undo) sits beside the control just used; trace the cursor path for long jumps. [Psychology of UX Design, p.34-38]
- [ ] Every permission or ask has a visible "Not now"; nothing social or visible to others is on by default. [Hooked, p.34, p.82-83]
- [ ] A stranger can answer: what can I do now, how, what happened, did it work? (Norman's seven stages, condensed.) [Design of Everyday Things, p.87-89]
- [ ] Every async button disables and shows state on click; slow work shows staged progress, not a bare spinner.
- [ ] Zero modals on the happy path; success shown inline; errors persist until fixed, never in an auto-dismissing toast. [About Face, p.655-656, p.665-666]
- [ ] Errors keep all valid input and sit next to the field with a fix. [About Face, p.217-218]; [Seed: Interaction patterns, §C3]
- [ ] Primary actions and nav carry text labels; nothing important lives only behind a gesture or hover.
- [ ] Realistic seeded data, no "lorem ipsum" or "test123"; empty state has a headline, one line and one action.
- [ ] Highlighted elements per screen: 1-2. [Laws of UX, p.129-130, p.137]

**B. Pre-judging robustness and accessibility (about 30 min, one person)**
- [ ] Contrast checker on the 3-4 main color pairs; check on the projector and on a phone in bright light.
- [ ] Every input has a visible label tied by for/id; placeholder is an example only. [Inclusive Design Patterns, p.267-271]
- [ ] Tab through the whole flow: visible focus, logical order, Enter submits, Esc closes and returns focus. [Inclusive Design Patterns, p.123]
- [ ] Selected, error and status states have an icon or text besides color; check a grayscale screenshot.
- [ ] Native button/a elements, `<html lang>`, one h1, alt text; run WAVE once. [Seed: Hackathon UX kit, §A6]
- [ ] Paste a very long name and paragraph, zoom to 150%, open at phone width. [Laws of UX, p.90-91]
- [ ] Type three messy inputs into each field a judge might use. [Microinteractions, p.137-139]
- [ ] Network off or API failing: the screen degrades to cached or sample data, not a blank page.
- [ ] "Reset demo data" sits out of reach of everyday controls; a visible "Start over" exists for walk-up judges. [About Face, p.260-261, p.294-295]

**C. Reading a test session (keep on a card)**
- "Why am I doing this?": bad label or missing copy. "Did anything happen?": feedback too subtle. "I didn't see that button": hierarchy. "I didn't know I could do that": hidden action. "What do I do now?": no clear next step. [Microinteractions, p.242-243]
- Prompt neutrally ("What would you do to proceed?", never "Is this button helpful?"), keep a flat face, and recruit hackers nearest the persona, not teammates. [Psychology of UX Design, p.286, p.289-290, p.304-307]

## Anti-patterns
1. **Login wall before value.** Tell: the first screen is a sign-in form. Fix: a pre-seeded demo account or no auth on the demo path; the root URL works without login. [Don't Make Me Think, p.121-122, p.204-206]
2. **Silent or bare-spinner AI call.** Tell: judges stare at a static spinner for 5+ seconds. Fix: stream output or show named stages, offer Cancel, and cache one demo result. [Laws of UX, p.98]
3. **Implementation-model UI.** Tell: one button per endpoint, screens named after modules, labels like "Ascending" or database field names. Fix: rename everything in the user's words and name screens after goals ("Plan my week"). [About Face, p.300-301, p.320-323]
4. **Confirmation and alert() everywhere.** Tell: "Are you sure?" on reversible actions, "Saved!" in a modal. Fix: soft-delete with a 5-10 s Undo toast and a quiet inline status. [About Face, p.286, p.681-683]
5. **Tragedy of the commons on the main screen.** Tell: each teammate's feature is promoted on the hero screen in the last 6 hours. Fix: one owner of the main screen with veto power; the demo tells one story. [Don't Make Me Think, p.129-130]
6. **Bolted-on gamification.** Tell: points, badges or a streak added late with no named feeling they relieve. Fix: cut it; a 3-minute demo cannot show multi-day reinforcement, and Mahalo's cash rewards failed where Quora's free peer upvotes worked. [Hooked, p.80-82]; [Psychology of UX Design, p.264, p.269-271]
7. **Testing with teammates or trusting "looks great".** Tell: the feedback is about colors, or the tester already knows the flow. Fix: strangers, a task goal, silence, and counting hesitations; ignore color comments unless about 3 of 4 testers react strongly. [Don't Make Me Think, p.170]; [Laws of UX, p.123-124]
8. **Dark-pattern urgency and surprise opt-ins.** Tell: a fake "only 3 left" counter, a countdown, or sharing switched on by default. Fix: delete it; judges read it as manipulation, and Quora reversed an auto-enrolled visibility feature within weeks after a user revolt. [Hooked, p.34, p.82]; [Psychology of UX Design, p.225, p.231]
9. **Shouting.** Tell: several colored badges, banners and bold elements compete. Fix: de-emphasize the competitors rather than turning up the main one; pass the squint test from across the room. [About Face, p.443-444]; [Refactoring UI, p.34-35]
10. **Error copy that blames or dumps a stack trace.** Tell: "Error 500", "Invalid input". Fix: what happened plus a fix button, with no "error" or "warning" words and no implied user fault. [Microinteractions, p.181-183]

## Hackathon calibration
- **A booth is a kiosk.** Judges stand, get interrupted and come cold: huge targets, a single path, minimal typing, and a "Start over" button. [About Face, p.585-594]
- **Bias toward the beginner.** About Face's advice to optimize for "perpetual intermediates" assumes users who live in the app; judges use it once, so a skippable first-run hint is fine, but still no permanent tutorial. [About Face, p.267-269, p.274]
- **Scale research down hard.** Use one provisional persona with its assumptions listed, and confirm or refute one assumption in a real conversation before hour 8; skip the 8-12 interviews and full journey maps (15 minutes on a whiteboard at most). [About Face, p.75, p.97]; [Laws of UX, p.102-104]
- **Skip settings pages, setup wizards, signature sounds and haptics.** Hard-code the good default and mention the setting as a next step; the hall is loud and judges may be mid-conversation. [Microinteractions, p.131-136, p.183-185]
- **Skip retention mechanics unless retention is the product.** Habit needs high frequency or very high utility; for an occasional-use tool, drop streaks and notifications and spend the hour on the one-shot experience. If you show a trigger, mock one notification tied to the user's last action and name the moment it targets. [Hooked, p.17, p.23-25, p.103-109]
- **If onboarding is in the demo, start its progress bar partly filled.** A punch card with 2 free stamps (same purchases needed) had 82% higher completion. [Hooked, p.62-63]
- **Undo and history: one level only.** Implement one-level Undo on the main destructive action and keep the last few AI outputs in a history strip for flipping between variants, not a global versioning system. [About Face, p.364-367, p.403-406]
- **Projector and venue conditions.** Subtle contrast washes out, so make active and selected states twice as strong as feels comfortable; venue Wi-Fi is often poor, so cache the demo path. [Don't Make Me Think, p.107-109, p.189-190]
- **Claim usability, not demand.** A hallway test shows people can use it, not that they want it; quote it as "we tested with 5 students; 4 of 5 finished in under a minute after we moved X". [Don't Make Me Think, p.230-237]; [Seed: Testing with users, §E]
- **Accessibility is cheap scoring.** About 20-30 minutes, then one sentence in the pitch about it as a design decision. [Don't Make Me Think, p.218-222]

## Where experts disagree
- **Wizard or one screen?** Krug prefers a 4-step wizard with one obvious question per step over a dense form [Don't Make Me Think, p.70]; About Face calls wizards an interrogation, prefers templates, and finds perceived speed tracks goal completion more than page count [About Face, p.252, p.418-421]. Follow About Face here: one screen with example scenarios and the result appearing in place. Use steps only when inputs are truly sequential and each step is a mindless click.
- **Fewest steps or the familiar sequence?** Hooked says adoption rises each time a step is removed [Hooked, p.48-50, p.64-65]; Kumar warns that a non-standard shortcut that makes users stop and think feels worse than one extra expected step [Psychology of UX Design, p.296-297]. Delete steps that are pure overhead (sign-up, typing what can be prefilled), but keep the order users expect (pick, review, confirm) and optimize inside each step.
- **Confirm or undo?** Norman and Yablonski keep deliberate friction and forcing functions for risky actions [Design of Everyday Things, p.156-159]; [Laws of UX, p.191]; About Face says replace confirmations with Undo [About Face, p.681-683]. Follow both by scope: Undo for anything reversible, and one light confirm on the single truly irreversible action.
- **Fast or deliberately slow?** The Doherty threshold says respond under 400 ms [Laws of UX, p.156]; the same book says a short artificial delay raises trust in "analysis" results [Laws of UX, p.164]. Always acknowledge instantly. Add a 1-2 s staged "analyzing" step only where an instant result would look trivial or untrustworthy, and never let it stack on top of a slow real call.
- **When to validate.** The NN/g guidance in the seeds says validate when the user leaves a field [Seed: Interaction patterns, §C3]; About Face says validate live after a 0.5 s pause [About Face, p.646-648]; Pickering says nothing before the first submit, then a 150 ms debounced re-check [Inclusive Design Patterns, p.285-287]. Follow Pickering: it is cheapest to build and kindest to screen readers.
- **Rough or polished prototypes for feedback?** Pickering says polish draws polite comments [Inclusive Design Patterns, p.182]; Saffer says test interactions at high fidelity because timing and feedback only show there [Microinteractions, p.240]. Use sketches for idea feedback in hours 2-6, and the real build for flow tests from hour 10, always measuring behavior over opinion.
- **Cap menus at 7?** The seeds suggest 5-7 nav items [Seed: Core principles, §B4]; Yablonski says visible menus are not a memory task and the cap is a myth [Laws of UX, p.59-60]. Decide by category clarity; a 3-screen hackathon app ends up at 3-5 items anyway because of scope, not memory.
- **How many testers, and when?** Krug says 3 per round, as early as possible [Don't Make Me Think, p.144-151]; Norman says 5 per round [Design of Everyday Things, p.240-241]; About Face says test late, because testing evaluates rather than creates [About Face, p.169-171]. Run two rounds of 3 (hours ~10-12 and ~18-20): early enough to fix, late enough to have a real flow.

## Go deeper
- search_experts("first screen what is this what can I do here", domain="11-ux-interaction")
- search_experts("response time thresholds progress indicator long wait", domain="11-ux-interaction")
- search_experts("replace confirmation dialog with undo", domain="11-ux-interaction")
- search_experts("eliminate error messages bounded controls forgiving input", domain="11-ux-interaction")
- search_experts("signifiers discoverability hidden gestures", domain="11-ux-interaction")
- search_experts("defaults instead of questions prefill templates", domain="11-ux-interaction")
- search_experts("hallway usability test script think aloud debrief", domain="11-ux-interaction")
- search_experts("kiosk first-time user booth design", domain="11-ux-interaction")
- search_experts("investment after reward foot in the door onboarding", domain="11-ux-interaction")
- search_experts("form labels placeholder validation accessibility", domain="11-ux-interaction")
