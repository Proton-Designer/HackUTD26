---
name: judge-qa
description: Load when writing the Saturday-night judge Q&A one-sheet, running the Sunday-morning mock Q&A, fixing a wrong or weak claim before judging, answering a live judge question, deciding whether to patch a gap a judge found, or deciding between visits whether a repeated objection means changing the pitch.
---
# Decision guide: judge-qa

## Open this when
- **Saturday night (hour 16-20):** writing the question cards for this project.
- **Sunday-morning mock (hour 21-23):** a teammate plays a hostile technical judge, a business judge and a skeptic.
- **Any time a claim looks wrong** (a metric, a "real-time", a "secure", a user count), before a judge finds it.
- **During judging:** a judge asks something hard, or exposes a gap you might patch.
- **Between visits:** 2 or more judges raised the same objection.

## What the team should get
Not a method. A one-page sheet of question cards for *their* project, built from their real stack, data, numbers and names. Each card has five parts:
1. **Answer** (45 seconds max, conclusion first, one measured number with n).
2. **Show:** the exact screen, chart, log or code file that proves it, and which teammate pulls it up. An answer with nothing on screen is a claim; with the screen, it is evidence.
3. **Follow-up:** the sharper question a skeptic asks next, and its answer.
4. **Don't say:** the specific phrases that would hurt on this question (a wrong number, "100%", "fully secure", "it was working earlier").
5. **Owner** and backup.

## Steps
1. **Start from the facts.** List what is live, what is seeded or hardcoded, every number anyone says, what data the app touches and where it is stored. Write 8-12 questions a judge would ask about *this* build, weighted to its weak spots: technical depth, AI/eval, data and privacy, viability, sponsor tech, "is this real?". Skip generic questions the pitch already answers.
2. **Check every number before writing its card.** The metric must fit the model type (see "Metric matches the model"). Under n=10, use counts ("6 of 8"), never percentages. Put the baseline next to it, measured the same way. A number that fails and cannot be fixed in 10 minutes is cut, then contained (step 3).
3. **Contain a bad claim everywhere at once.** When a claim is wrong, fixing the sentence in the pitch is not enough; judges read the Devpost and README before or after the visit, and a teammate under pressure repeats the old line. Find and fix every copy:
   - pitch script and demo narration; slides and chart titles; Devpost (tagline, description, image captions, "what we learned"); README; demo video; UI text and dashboard labels; and each teammate's memorized lines.
   - Then write the replacement sentence, plus the honest answer if a judge saw the old number: "We first reported accuracy, which is the wrong measure for a forecast. The right one is mean error: __ [units] vs __ for the last-value baseline." All 4 say it aloud once. If an edit is locked after the submission deadline, fix the README and say the correction at the table.
4. **Privacy and security cards name the frame that fits the data,** then answer concretely: what is collected, where it lives, who can read it, what the demo uses (synthetic or public data), and the one step before real users. Frames to recognize: student grades, schedules or IDs are education records under FERPA; health data under HIPAA when handled for a provider or insurer; payment cards under PCI DSS; users under 13 under COPPA. Name the frame in one clause; do not claim compliance you have not checked. Show the data model, the auth check in code, or the seeded-data flag on screen.
5. **Decide each known gap now: fix it or disclose it** (rule below). Write the disclose line on the card either way.
6. **Mock Q&A, 10 minutes per persona.** The hostile persona asks the follow-up on every card and interrupts at 45 seconds. The listener writes questions word for word. Rewrite any card where the answer ran long, had nothing on screen, or used a don't-say phrase.
7. **At the table:** let the judge finish, pause a beat. If the question could mean two things, ask once ("cost, or getting users?"). Owner answers from the card while the shower pulls up the screen; teammates add one sentence at most and never contradict each other. Wrong premise: correct it softly. Real weakness: "You're right, [gap]; we'd fix it first by [step]." Missing feature: "Not built in 24 hours; we'd add it by [one line]." Hostile: answer the substance, ignore the tone. End on one line the judge can repeat to co-judges.
8. **Between visits:** if 2 judges raise the same objection, change the pitch before the next visit instead of sharpening the rebuttal.

## Fix now or disclose (gaps found during judging)
- **Real exposure comes first:** a leaked API key, a public database or bucket with real personal data, or credentials in the repo or client code. Rotate the key or take the data offline now, even if a feature breaks, and switch to seeded data. Then disclose.
- **Otherwise fix now only if all are true:** the fix fits a 20-minute time-box; one person does it on a branch, away from the table, while the others keep judging; it does not touch the demo path; and it passes a full demo run from reset before it is deployed, between visits.
- **Never deploy over the demo build during a visit.** Keep a known-good tag and revert the moment anything regresses. A broken demo costs more than any disclosed gap.
- **If any condition fails, disclose:** "Good catch. Right now [gap]; the demo uses [seeded data / a single user]. Before real users we'd [specific step]." Add the gap to the README's known-limits list so the Devpost and the table say the same thing.

## Metric matches the model
- **Classification** (category, alert, yes/no): accuracy only when classes are balanced; otherwise precision and recall, against the majority-class baseline.
- **Regression or forecast** (a number): mean absolute error or RMSE in real units, against a naive baseline (last value, average). "Accuracy" on a forecast is a red flag to any technical judge.
- **LLM output:** "__ of __ hand-labeled examples correct", main failure mode, how it is handled.
- **Ranking or search:** "right result in top 3 for __ of __ queries".

## Template
```
Q&A ONE-SHEET  (one page, carried to the table)

OWNERS  Technical ___ (backup ___)  AI/eval ___  Data/privacy ___
        Business ___  Sponsor ___   Shower (drives the screen) ___

QUESTION CARDS (8-12, weighted to this build's weak spots)
Q: "___"                                              Owner: ___
  Answer (<=45 s): ___ [conclusion] ___ [number, n, baseline] ___ [so-what]
  Show: ___ [screen / chart / file:line]  pulled up by ___
  Follow-up: "___"  ->  ___
  Don't say: ___

REAL / SEEDED / HARDCODED (visible fallback flag in UI: Y/N)
- ___ is live via ___ | ___ is seeded because ___; real needs ___

NUMBER CARDS
- Claim words: "___"  __ of __ (n=__, who: ___)  Metric fits model type? Y/N
  Baseline, same metric: ___   Does NOT show: ___   Best of N? ___

BAD-CLAIM SWEEP (claim: "___" -> replacement: "___")
[ ] pitch/narration [ ] slides/chart titles [ ] Devpost (tagline, text, captions)
[ ] README [ ] video [ ] UI labels [ ] all 4 teammates said the new line aloud
If a judge saw the old claim: "___"

KNOWN GAPS                      Fix now (20 min, branch, demo run) / Disclose line
- ___                           ___

TRADEOFF LINES (3-5): "Given 24 hours and ___, we chose ___ over ___ because
  ___. It costs us ___. If ___, we'd switch to ___."

COMPETITORS (each under 15 s): vs manual/do-nothing, vs ChatGPT/incumbent:
  "___ works for ___, but cannot ___ because ___; we do ___, shown by ___."
  "Why won't Google/OpenAI build this?" Barrier: ___ (none: "early lead from ___")

SCALE/COST: first bottleneck ___ | next step ___ | $__ per user per month
SPONSOR: "[tech] is central because without it ___."  MLH learned: ___
CLOSING LINE (repeatable to co-judges): "___"
```

## Principles
1. **A repeated objection means the pitch is broken, so fix the pitch and not the rebuttal (counterintuitive).** Objections mostly come from how the presenter frames things; building the need first cut objections per hour by 55%. [SPIN Selling, p.147-148, p.163-167]
2. **The metric must match the model, or the number cannot even be compared.** RMSE and accuracy measure different things; the use case decides which applies. A forecast reported as "92% accuracy" tells a technical judge you did not evaluate it. [Lakshmanan, Machine Learning Design Patterns, p.123-126]
3. **Every number needs a naive baseline beside it.** Performance only means something relative to a trivial predictor, and the baseline pre-empts "how good is it really?" [O'Neil, Weapons of Math Destruction, p.83]
4. **A number that looks too good is a bug until proven otherwise.** Judges hunt for leaks behind 99% accuracy. Disclose best-of-N and the baseline's score. [Calling Bullshit, p.271-273; How to Measure Anything, p.46]
5. **Small-n numbers are fine as counts (counterintuitive).** The "need n=30" rule is a myth; 6 of 8 still has a 95% range of about 40-94%, so "at least ~40%" survives a challenge and "75%" does not. [Quantifying the User Experience, p.26, p.37-42]
6. **Diagnose before answering.** The usual failure is a polished answer to the wrong question; one clarifying question fixes it. [Seed: Q&A technique sources, §C4; Never Split the Difference, p.34, p.41]
7. **Say the top 1-2 criticisms yourself and hold the rest.** A criticism you name first loses its sting, and denying one after a judge raises it makes it more believable. Pouring out every limitation unasked hurts. [Never Split the Difference, p.55-59; Getting to Yes, p.53]
8. **Never swap a live build in place.** Change a copy, test it against the same checks as the current version, and promote only if it wins; keep a known-good tag to revert to. [Huyen, Designing Machine Learning Systems, p.291-292, p.313]
9. **Privacy answers name where data goes.** Data sent to an API provider can be used or leaked, and the risk is the app builder's; use synthetic or public data in the demo and state a one-line privacy stance. [Huyen, AI Engineering, p.360-366]
10. **Every design choice gets "because" plus its cost.** Giving a reason raised compliance from 60% to over 90%; naming the cost signals seniority. [Never Split the Difference, p.189; Seed: Hackathon and judge sources, §B8]
11. **No causal verb without a comparison.** "Reduces errors" invites "compared to what?"; say "40 s vs 4 m 10 s in their current tool (n=6)". [Calling Bullshit, p.64-65, p.83-85]
12. **Never ask a judge why they want a missing feature.** It makes them spell out its value and raises its weight. [SPIN Selling, p.122-123; Never Split the Difference, p.127-128]
13. **Competitor answers name the alternative, its limit, and your proof; a moat needs a real barrier.** "No competitors" reads as "did not look", and "we execute better" is not a barrier. [Crossing the Chasm, p.133; 7 Powers, p.30-31, p.116-122]

## Mistakes
- **Pitch fixed, Devpost still says the old number** -> run the full bad-claim sweep; a judge who reads "92% accuracy" after the visit scores the old claim.
- **Defending the wrong metric's value instead of the metric choice** -> say why it was the wrong measure, give the right one with its baseline, move on.
- **Privacy answered in the abstract** ("we take security seriously") -> name the data, where it lives, who can read it, the frame (e.g. FERPA), and show it on screen.
- **Patching a judge-found gap on main during judging** -> branch, 20-minute box, full demo run, deploy between visits only, or disclose.
- **Third judge raises "wrapper" and you have a better rebuttal** -> add one label line to the pitch instead. [SPIN Selling, p.154-155]
- **"I think it's around..." for something unmeasured** -> say what you do know, then "we'd find out by [method]".
- **"We didn't have time"** -> "We prioritized X over Y because [reason]; next we'd [step]." [Getting to Yes, p.66-67]
- **Canned data appears and the presenter does not know it** -> visible fallback flag in the UI; know which path is live. [Huyen, Designing ML Systems, p.224-233]
- **"Let me try it" and the app hangs** -> warm-up request before each visit; rate-limit paid endpoints. [Nygard, Release It!, p.50-56, p.88-90]

## Hackathon calibration
- **About 1 minute of Q&A per visit** means 2-3 questions. Short answer first; if a technical or sponsor judge digs, go as deep as they want, because technicality is scored.
- **Skip long-horizon sales and strategy moves:** discovery calls, revenue forecasts, dominance tactics, brand or switching-cost moats. Use trust devices instead: visible sources, an accuracy count, a real tester quote. [Pitch Anything, p.9-10; 7 Powers, p.35, p.88]
- **Hackers are not your users.** If testers were attendees, say so in one line. [Quantifying the User Experience, p.26-28]
- **Match the track:** sponsor judges want their tech central, in their challenge's words; MLH judges want a real "what did you learn".
- **After hour 20, fatigue is the risk.** Rehearse the 3 hardest cards slowly and agree a tag-out signal. [Never Split the Difference, p.43, p.48, p.129-132]

## Go deeper
- [../domains/21-technical-qa.md](../domains/21-technical-qa.md): question handling, accusation audit
- [../domains/05-evidence-quant-research.md](../domains/05-evidence-quant-research.md): claim cards, small-n wording, causal gates
- [../domains/15-ai-app-design-eval.md](../domains/15-ai-app-design-eval.md): eval metrics, failure modes, privacy
- [../domains/13-architecture-tradeoffs.md](../domains/13-architecture-tradeoffs.md): tradeoff lines, scale math, demo hardening
- search_experts("choose regression versus classification metric", domain="15-ai-app-design-eval")
- search_experts("privacy licensing data sent to API", domain="15-ai-app-design-eval")
- search_experts("champion challenger known-good version late change", domain="13-architecture-tradeoffs")
