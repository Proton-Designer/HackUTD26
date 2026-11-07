---
name: value-prop
description: Load at hour 1-2 when choosing which differentiator to stake an idea on and writing the one-liner, at hour 12 when locking the message against what was actually built, and at hour 18-22 when the tagline, Devpost fields, and "isn't this just ChatGPT?" answer must be final.
---
# Decision guide: value-prop

## Open this when
- **Hour 1-2:** 2-4 candidate ideas are on the table and the team must pick the one that is different in kind, not slightly better, then write its one-liner.
- **Hour 6-12:** the persona is still a hypothesis; someone wants to add "AI-powered", a second user type, or one more feature "to stand out".
- **Hour 12:** midpoint lock. Check that the claim still matches the build, then freeze the master sheet every artifact copies from.
- **Hour 18-22:** writing the Devpost tagline, poster headline, first 15 seconds of the pitch, and the 15-second answers to "how is this different from X?" and "couldn't OpenAI just build this?"

## Steps
State each choice you make as "We chose X because [principle] [citation]" in the master sheet.

1. **Ask before you search (10 min).** Ask 2-3 people who fit the user: "What do you do today when X happens?" and "What would you use if this did not exist?" Log literal answers, rank by frequency. GO: at least one answer is a workaround (spreadsheet, group chat, manual steps, nothing). STOP: nobody has a workaround or cares; question the need.
2. **Prior-art sweep (20 min, hard stop).** Devpost search for the idea plus the sponsor challenge, plus past HackUTD galleries. If a polished product already serves this exact user: change the user or angle, not features. If the sponsor already sells it: complement it. If one ChatGPT prompt does it: the differentiator must be data, workflow, integration, or action, and you must say what survives a model upgrade.
3. **Rank the pains, attack 1-2.** Score the user's pains 1-5 from their view, keep the top 3, and drop any that is not felt right now (a judge cannot feel it in the demo).
4. **Unique attributes filter.** List what your idea has that the logged alternatives lack. Strike anything 2+ alternatives already have. GO: 2-4 survivors. Zero survivors: rework or drop.
5. **Pick one dimension and size the gap** against the top alternative from step 1 (minutes, steps, errors). Target about 10x. Under about 2x: pick another dimension or narrow the user until a gap is large. Prefer time and effort over "bigger outcome" claims.
6. **Onliness test.** Write "the ONLY [category] that [differentiator] for [whom]". List every plausible claimant, including other HackUTD teams on the same sponsor track. GO: no other claimant. Otherwise narrow and retry; after 2 failed rounds, move to the next idea.
7. **Choose the frame.** Write 2-3 category frames; pick the familiar one that makes your standout feature look natural. List features that frame implies; for each you lack, switch frame or add one line: "deliberately does not do Y".
8. **Write ERRC cuts.** At least one Eliminate and one Reduce next to every Raise and Create. Cuts become the explicit not-building list.
9. **Write all forms from one source** (see Template): tagline of 6-8 words, one-liner of 12 words or fewer, "from ___ to ___ in ___", headline of 140 characters or fewer.
10. **Comprehension test (10 min).** Say the one-liner once to 3 people outside the team. Ask: what is it, for whom, why does it help? GO: 2 of 3 get all three unprompted. "I don't get it" means fix the words; "not useful" means fix the idea. Discount "it's weird" from testers who understood it.
11. **Hour 12 lock.** A teammate who did not build the core describes the product in one sentence. If it differs from the plan, pitch what exists. Freeze the master sheet. Reopen only if a step-2 stop rule newly fires.
12. **Hour 20 proof and consistency.** Each claim has one measured number with its baseline and sample size, visible on screen within 5 seconds. All 4 teammates say the one-liner word for word.

## Template
Copy into the team doc at hour 1; fill top to bottom; freeze at hour 12.

```
VALUE-PROP MASTER SHEET  (frozen at hour __ by __)

1. ALTERNATIVES (literal user answers, ranked by frequency)
   #1 ______________ (n=__ of __ asked)   #2 ______________   #3 ______________
   Market alternative (habit/budget displaced): ______________
   Product alternative (other newcomer on same tech, e.g. ChatGPT): ______________

2. TOP PAIN (felt now, scored 1-5): ______________ score __

3. UNIQUE ATTRIBUTES (struck if 2+ alternatives have it)
   | Attribute | Benefit | Value (user goal + number) | Proof shown in demo |
   |-----------|---------|----------------------------|---------------------|
   |           |         |                            |                     |

4. GAP: dimension ______  today ______  ours ______  ratio __x  (GO if about 10x; redo if under 2x)

5. ONLINESS: The ONLY ______ that ______ for ______.
   Other possible claimants: ______  -> clean? Y/N

6. FRAME: "______ for ______"   Implied features we lack: ______
   "We deliberately do not ______."

7. ERRC   Eliminate: ____  Reduce: ____  Raise: ____  Create: ____

8. FORMS (all derived from rows 3-6)
   Tagline (6-8 words, no one else could use it): ______________
   One-liner (12 words max, names user + outcome): ______________
   From/To: Users go from ______ to ______ in ______.
   Headline (140 chars max, subject-verb-object): ______________
   Emotional line (identity or internal pain): ______________
   Sponsor line: For [sponsor], this makes [their product name] do ______ it could not before.

9. COMPREHENSION TEST   Tester 1 __/3   Tester 2 __/3   Tester 3 __/3   (GO at 2 of 3)

10. PROOF (one per claim)
   Claim ______  number ______  vs baseline ______  sample "__ of __ cases"  on screen at __s

11. 15-SECOND ANSWERS
   "How is this different from [#1 alternative]?"
     [X] works well for A, but cannot do B because C. We do B, shown by D.
   "Isn't this just ChatGPT?"
     [What it lacks: data / action / workflow]. If the model improves, we keep ______.
   "What stops Google/OpenAI/[sponsor] copying it?"
     [Incentive conflict / data access / niche too small for them]. Today our lead is ______.

12. DECISION LOG
   We chose ______ because ______ [citation].
```

## Principles
1. **The competitor is what the user does today, not a rival startup or "legacy systems". (counterintuitive)** Users judge "better" against their own habit and have never heard of the startups you found; beating an unused rival convinces no one. [Obviously Awesome, p.39, p.63-65]
2. **Win by about 10x on one dimension, with the yardstick in the same sentence.** A 20% gain is invisible and slightly-better-everywhere does not read as different; "5 minutes versus an hour of copy-paste" does. [Zero to One, p.38-39]; [Value Proposition Design, pp.160-161]; [Obviously Awesome, p.39]
3. **Pass the onliness test against the room, not just the market.** If another team at the venue could say your sentence, it is not a USP; the wider the competition, the narrower the focus. [Zag, p.52, p.56]
4. **Derive the positioning statement last; never use it as the method. (counterintuitive)** The For/Who/Unlike template records untested assumptions; fill it only after the alternatives-to-value analysis, as a check. [Obviously Awesome, p.35-38]
5. **Borrow a known category with a twist; do not coin one. (counterintuitive)** A new category needs teaching time a 4-minute visit does not have, and the label you pick brings assumed competitors and features. [Obviously Awesome, p.25-33, p.92-96]
6. **"X for Y" only works if Y would use it differently.** Ask two members of Y what they would do differently; no concrete answer means a cosmetic niche. [Obviously Awesome, p.88]
7. **Differentiate on time and effort pushed toward zero, and make it visible. (counterintuitive)** Bigger-outcome claims are easiest to copy; speed and ease are harder, but invisible backend gains count for nothing without a counter or before/after on screen. [$100M Offers, p.62-63, p.68-69]
8. **A trend word goes after the category and must change the result.** "AI-powered" is not a category; if the AI does not visibly change what the user gets, move it to the stack slide. [Obviously Awesome, p.43-45, p.98-101]
9. **Subtract to differentiate.** Raise-and-Create only produces a costlier me-too; eliminations pay for the build time and sharpen the claim. [Blue Ocean Strategy, p.40-43, p.65-66]; [Zag, p.16-17, p.57]
10. **Person first, number second. (counterintuitive)** Adding statistics to a single story cut giving from $2.38 to $1.43; put the user's moment first and the measured number in the next beat, in human units. [Made to Stick, p.151-153, p.131-134]
11. **Answer the copy question with a Benefit and a Barrier, never "we execute better".** Name incentives, data access, or niche size; for AI projects, state what is retained when the model improves. [7 Powers, p.30-31, p.80]
12. **Claim only the fit you reached, in counts.** 24 hours buys problem-solution fit at most; a signup or follow-up beats "I'd use this", and small samples are stated as "4 of 5 testers", not 80%. [Value Proposition Design, pp.123-126, pp.525-528]; [Houston, We Have a Narrative, pp.14-16]

## Mistakes
- **Tagline sized like a sentence.** Sign: 15-20 words on the title card. Fix: 6-8 word tagline beside the name that no one else could use, plus a 12-word one-liner. [Don't Make Me Think, p.125-128]
- **Imaginary or rigged competitor set.** Sign: "unlike other apps" or the comparison table omits ChatGPT and the manual way. Fix: lead with the logged workaround, include what a skeptical judge names first. [Zero to One, p.23-25]
- **Sponsor marketing vocabulary.** Sign: the pitch echoes the sponsor's slogans. Fix: use their product names and say what their tech made possible; frame impact in their mission. [Presentation Secrets of Steve Jobs, p.212-213]
- **Fighting the leader head-on.** Sign: "a better ChatGPT/Notion for everyone". Fix: name the niche need the leader ignores and show it live. [Obviously Awesome, p.81-85]
- **Hour-16 feature to stand out.** Sign: "one more feature" proposed to differentiate. Fix: strike anything that does not serve the onliness line. [Zag, p.57]
- **Claim drift.** Sign: Devpost says what the plan said, demo shows something else. Fix: hour-12 non-builder description; pitch what exists. [Obviously Awesome, p.26-27]
- **Tagline polish over a broken core.** Sign: hour 20 on wording while the demo path fails. Fix: make the one path reliable first. [$100M Offers, p.123]

## Hackathon calibration
- **Clutter is the competition.** ~200 projects and ~4 minutes: what, who, and why must land in 5 seconds and survive deliberation. Open the demo on the finished result, not a login or empty state. [Zag, p.16-17]; [$100M Offers, p.65-66]
- **Compressed narrowing.** Books split on narrow-early versus broad-early; here, test broadly until hour 6-8, lock one persona by hour 12. [Obviously Awesome, p.49-51]
- **Criteria map.** Onliness serves uniqueness; the measured gap serves usefulness and impact; honest fit staging plus one segment-size number serves viability. Spend about 80% of talk on today's problem and demo, 20% on scale. [Obviously Awesome, p.52, p.75]
- **Sponsor track has a second buyer.** Write a separate pain/gain line for the sponsor and make their tech deliver the differentiating dimension, not a side feature. [Value Proposition Design, pp.127-131]
- **MLH tracks** score technology, design, completion, learning; a light differentiation story is enough there.
- **Ignore:** moats beyond an honest early lead, brand, pricing tiers, switching costs, category creation, statistical significance, scarcity tactics. Give one pricing line anchored to the manual alternative's cost if asked. [7 Powers, p.35, p.88]; [Value Proposition Design, pp.564-568]
- **Wizard of Oz is fine for the long tail** if the core path is real and you disclose it when asked. [Value Proposition Design, pp.546-553]

## Go deeper
- [../domains/10-usp-value-prop.md](../domains/10-usp-value-prop.md)
- [../domains/06-competitor-differentiation.md](../domains/06-competitor-differentiation.md)
- [../domains/19-storytelling.md](../domains/19-storytelling.md)
- search_experts("onliness statement only category differentiator", domain="10-usp-value-prop")
- search_experts("competitive alternatives what would you use if we did not exist", domain="06-competitor-differentiation")
- search_experts("market category frame of reference subsegment X for Y", domain="10-usp-value-prop")
- search_experts("benefit and barrier counter-positioning incumbent will not copy", domain="06-competitor-differentiation")
- search_experts("what stops a model update killing an AI wrapper moat data workflow", domain="06-competitor-differentiation")
- search_experts("Twitter-length headline repeated across materials", domain="19-storytelling")
