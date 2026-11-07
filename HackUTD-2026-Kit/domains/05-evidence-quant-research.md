---
name: 05-evidence-quant-research
description: Open when a number, stat, survey result, user-test result, market size, accuracy figure or chart is about to enter the pitch, Devpost, README or a judge answer; when deciding how many people to interview or test; or when a teammate says "users want this" or "we validated it".
---
# Evidence quality and quantitative research

## Use this when
- Hours 1-3: picking a problem from a headline stat, sizing the market, or deciding how many hallway interviews are enough before locking the idea.
- Hours 8-20: running hallway usability rounds and turning "4 of 5 finished" or task timings into something you can say out loud.
- Any time a dataset shows a striking pattern or the model scores suspiciously high, before it becomes a pitch claim.
- Hours 18-22: building the problem, impact and "before vs after" slides and charts, and filling in Devpost claims.
- Q&A prep: a judge will ask "how do you know?", "n?", "mean or median?", "is that causal?".

## Core principles
1. **Count what people did and what they gave up, never what they say they would do (counterintuitive).** "I would definitely use it" is the most dangerous data there is; only past behavior and commitments of time, reputation or money count. [Mom Test, p.29-30, p.67-69] [How to Lie with Statistics, p.101-104]
2. **Every headline number ships with a baseline measured the same way.** A number nobody can compare gets ignored or doubted; write it as "40 s vs 4 m 10 s in their current tool (n=6)". [Calling Bullshit, p.93-94] [Thinking, Fast and Slow, p.351]
3. **Small samples are usable if you report counts and lead with the lower bound (counterintuitive).** The "need n=30" rule is a myth; 6 of 8 has a 95% adjusted-Wald range of 40-94%, so "at least ~40% of users" survives any challenge. 5 of 5 is "all 5 testers", never "100%". Weight by n, not by headline rate: 12 of 20 is stronger evidence than 4 of 5. [Quantifying the User Experience, p.26, p.37-42] [Thinking, Fast and Slow, p.413-414] [Seed: A. Hackathon evidence kit, §A3]
4. **Who you asked matters more than how many (counterintuitive).** Size shrinks random error, not bias: Literary Digest's 2.4 million responses lost to Gallup's ~3,000. Ten varied real target users beat 200 hackers near your table. [How to Make the World Add Up, p.136-137] [Quantifying the User Experience, p.26-28]
5. **No causal verb without a comparison.** Association fits forward cause, reverse cause, a third factor or chance; in one sample only 15 of 50 shared health studies supported causation. Say "in our test, users did X faster", or flip a coin to assign who gets the feature. [Calling Bullshit, p.64-65, p.83-85]
6. **Trace every outside stat to the original and write its definition in one line.** Zombie stats lose their caveats as they spread, and most number disputes are really definition disputes; if you cannot find the source or state the definition, drop the number. [Calling Bullshit, p.110-112] [How to Make the World Add Up, p.65-68, p.72-74]
7. **Size markets bottom-up and Fermi-check them.** Reachable customers × annual price from 3-4 sourced numbers beats "1% of a $10B market"; cross-check top-down, and if the two differ by 10x, fix or drop. SOM over 10% of TAM gets skepticism. [How to Measure Anything, p.43] [Calling Bullshit, p.273-278] [Seed: C. Gathering quantitative evidence ourselves, §C4]
8. **Gather evidence only for a decision you can name, and only on the 1-4 riskiest assumptions.** Most variables have near-zero information value; spend hours where uncertainty and the cost of being wrong are both high. [How to Measure Anything, p.28-31, p.77-78]
9. **Fix the test, the sample size and the pass bar before you look.** Re-running until it works, or showing the best of 20 runs, measures selection, not skill. Write "must beat baseline on 7 of 10" on a sticky note first, and say "best of N" if that is what it is. [How to Measure Anything, p.46] [How to Make the World Add Up, p.109-111]
10. **A result that looks too good is a bug until proven otherwise.** Extreme numbers are usually transcription, definition or leakage errors; 99% validation accuracy is the first place to hunt for a leak. [Calling Bullshit, p.271-273] [How to Make the World Add Up, p.106]
11. **For anything that detects or flags, report precision against the base rate, not accuracy (counterintuitive).** With a 1-in-100,000 base rate and a 1-in-10,000 false-positive rate, a "99.99% accurate" detector is right on only about 9% of its flags. Show a confusion table with counts. [Naked Statistics, p.113-114] [Thinking, Fast and Slow, p.151-152]
12. **Five testers only find the common problems.** The chance of seeing a problem in n sessions is 1-(1-p)^n: with 5 users you catch 97% of problems hitting half of users but only 41% of 10%-problems. "5 users find 85%" holds only when p is about 0.31. [Quantifying the User Experience, p.159-166]

## Decision procedure
Main decision: **can this claim go in front of judges, and in what exact words?** Run it per number.

1. **Name the job.** Which decision or pitch beat does this number support? If removing it changes nothing a judge scores, cut it. [How to Measure Anything, p.28-31]
2. **Fill the claim card**: exact words, number and unit, source plus year or "our data", method and n, what it does NOT show, ladder rung, a one-line answer to a challenge. [Seed: A. Hackathon evidence kit, §A2]
3. **Place it on the ladder** (opinion, anecdote, unverified stat, credible secondary source, own interviews on past behavior, own observed measurement, commitment). Rungs 1-3 never appear as evidence: an anecdote may open the story but is labeled as a story. Aim to have at least one rung 6 or 7 item by judging. [Seed: A. Hackathon evidence kit, §A1]
4. **Outside stat gate.** Pass only if all hold: traced to the original (SIFT "Trace", about 2 minutes), definition written in one line, publisher's incentive noted ("who says so, how do they know, what are they selling"), current enough for the topic. Research findings need 2 independent sources; a single surprising viral finding gets one search for "replication" or "meta-analysis", else it is stated as a hypothesis. [How to Lie with Statistics, p.97-99] [How to Make the World Add Up, p.100-102, p.123] [Seed: B. Evaluating sources, §B2]
5. **Own-data gate.**
   - n under 10: counts only ("6 of 8"), no percentages. [Seed: A. Hackathon evidence kit, §A7]
   - Any proportion: compute adjusted-Wald (add 2 successes and 2 failures; p ± 1.96·sqrt(p(1-p)/(n+4))) and quote the lower bound in Q&A. If 95% is too wide to say anything, use 90% (z=1.64). [Quantifying the User Experience, p.37-41]
   - Task times under 25 users: geometric mean (=EXP(AVERAGE(LN(range)))) plus the individual values. [Quantifying the User Experience, p.45-49]
   - State recruitment in one line: "8 HackUTD attendees near our table, convenience sample". [Calling Bullshit, p.115-122]
6. **Comparison gate.** A "better/faster" claim needs the same task, same metric, same inputs on both sides, ideally the same person with and without the tool. Claim a difference only if it is large and obvious (minutes, not seconds; a 4x speedup, not 12%). Within a couple of points of baseline on a small test set means "no difference". [How to Lie with Statistics, p.47-51, p.70-72] [Seed: A. Hackathon evidence kit, §A3]
7. **Causal wording gate.** Scan for "reduces", "improves", "causes", "because of", and subjunctive "if X were higher". Without a randomized or controlled comparison, rewrite as an observation and name one confounder ready for Q&A. [Calling Bullshit, p.74] [How to Lie with Statistics, p.73-80]
8. **Magnitude gate.** Fermi-check: 2-4 factors to the nearest power of ten, under 5 minutes. Within about 10x: keep. Off by 100x: fix or drop. Each teammate writes their own estimate before anyone opens an analyst figure or competitor's TAM, because any number seen first anchors everyone's estimate. [Thinking, Fast and Slow, p.118-126] For your own Fermi estimates, two different factor chains should agree within 2-3x. [Calling Bullshit, p.273-278] [How to Make the World Add Up, p.75-76] [Seed: C. Gathering quantitative evidence ourselves, §C5]
9. **Framing gate.** Show absolute and relative together ("from 12 min to 4, a 67% reduction"), say "percentage points" for differences between rates, give the count and the rate ("2 failures in 150 runs"), and round to the precision your method supports. [Calling Bullshit, p.94-100] [How to Lie with Statistics, p.85-90]
10. **Stop/go.** GO if it passed every gate and one teammate can defend it in under 30 seconds. DOWNGRADE (move to Devpost or a backup slide, softened wording) if it passes but is weaker than rung 4. CUT if any gate fails and cannot be fixed in 10 minutes. [Seed: A. Hackathon evidence kit, §A7]

Research sizing sub-rules (when gathering, not reporting):
- **Interviews:** stop at 3-5 if answers converge; if 10 or more are still scattered, narrow the segment instead of adding interviews. To hear a pain held by 25% of users with 90% odds, plan about 9. [Mom Test, p.92, p.96-97] [Quantifying the User Experience, p.159]
- **Pivot trigger:** set it before you start, e.g. if 3 of the first 5 real target users show no existing workaround or urgency, switch ideas by hour 3. [Mom Test, p.43-45]
- **Usability rounds:** 2-3 people around hour 8-10, fix, then 3-4 around hour 18-20 with different tasks or user types. Stopping rule: 4 of 5 complete the core task unaided, or the clock. [Quantifying the User Experience, p.162, p.175-179]
- **Quick range with no data:** time 5 random cases; there is a 93.75% chance the median lies between the smallest and largest (call it ~90%). [How to Measure Anything, p.69-72]

## Checklists

**Number audit (run on the deck and Devpost before submission)**
- [ ] Every number has a claim card, a source with year or "our data, n=", and a one-line definition.
- [ ] No "would use / would pay" counts presented as demand; demand evidence is behavior or commitment.
- [ ] No percentage from under 10 people; no "100%" or "0%" from a small sample.
- [ ] Each headline number has a baseline beside it, measured the same way.
- [ ] No causal verb without a controlled comparison.
- [ ] Market size is bottom-up, Fermi-checked within 10x, SOM at or below about 5% of TAM.
- [ ] Model or eval numbers state the test set size, "best of N" if applicable, and the baseline's score with the absolute difference. The set includes 5-10 edge or adversarial inputs, and failures are sorted by category (if 2 input types cause most errors, fix those first). [Naked Statistics, p.38-39, p.128-130]
- [ ] Any composite score defines each input's unit and range and was tested on all-zeros and one-input-extreme. [Calling Bullshit, p.105-110]
- [ ] Flattery check: if all our rounding choices and framings lean our way, fix the one-directional "mistakes". [How to Lie with Statistics, p.81-82]

**Survey and interview instrument (before asking anyone)**
- [ ] Every question asks about a specific past event ("last time", "in the last week, how many times").
- [ ] No "would you", "do you like", leading or double-barreled wording; forced choice instead of agree/disagree.
- [ ] At least one question could kill the idea. [Mom Test, p.42-43]
- [ ] When someone says the problem matters a lot, follow with "when did you last think about it on a normal day?"; importance is inflated while they are focused on it. Ask the general question before any specific or emotional one. [Thinking, Fast and Slow, p.101-102, p.393-395]
- [ ] Sample size and stopping rule written down in advance. [How to Make the World Add Up, p.110-111]
- [ ] Piloted on 2 people; notes tagged F (fact), C (compliment), H (hypothetical), I (idea); only F lines feed decisions. [Mom Test, p.24-25] [Seed: A. Hackathon evidence kit, §A6]

**Chart check (every exported chart; a truncated bar once drew a 1.08x change with 2.7x the ink)** [Calling Bullshit, p.170-178, p.190-191] [How to Lie with Statistics, p.52-56]
- [ ] Bar y-axis min explicitly set to 0 (chart libraries auto-scale).
- [ ] No dual axes (use two stacked panels sharing an x-axis), no 3D, no scaled icons.
- [ ] Rates with the denominator in the axis label when groups differ in exposure.
- [ ] Time window justified; n and source in the caption; title states the takeaway.

## Anti-patterns
- **"8 of 10 people said they'd use it."** Tell: future tense on a slide. Fix: report what they do now, spend now, and committed to (email for tonight's test link, a named intro). [Mom Test, p.29-30, p.70-72]
- **"75% success rate" from 6 testers or "100% of users succeeded".** Tell: a percent sign next to a single-digit n. Fix: "all 5 testers"; in Q&A, "plausible range 51-100%". [Quantifying the User Experience, p.40-41]
- **Headlining a pattern you found while mining the dataset.** Tell: the insight arrived at hour 6 from scanning many columns. Fix: split the data 50/50 at the start; mine one half, require the pattern to hold in the other. [How to Make the World Add Up, p.110-113] [Calling Bullshit, p.77-81]
- **"Users who tried feature X got 3x more done."** Tell: comparing opt-in users with non-users. Fix: randomly assign who is prompted, or call it association. [Calling Bullshit, p.141-144]
- **"Improves accuracy by 40%."** Tell: relative change with no starting value. Fix: baseline score, our score, absolute difference, same test set and preprocessing. [Calling Bullshit, p.97-100] [How to Make the World Add Up, p.65-67]
- **"The prompt tweak fixed it."** Tell: a bad eval run, a change, then a better run, credited to the change. Fix: extremes drift back toward average on their own; re-run both versions on the same fresh inputs and compare average to average. [Naked Statistics, p.137-139] [Thinking, Fast and Slow, p.416-418]
- **Eval score rose after the test set shrank.** Tell: failing cases quietly removed as "broken". Fix: keep the same inputs across rounds and report n each time, like a fixed cohort. [Naked Statistics, p.158-160]
- **An invented "Impact Score" or "Trust Index" formula on screen.** Tell: terms with different units added together. Fix: define units and ranges, or show a table of up/down relations instead. [Calling Bullshit, p.105-110]
- **Desk-research facts gathered by interview.** Tell: asking users how big the market is. Fix: secondary sources for facts and figures, interviews for past behavior and pain. [Mom Test, p.104-106]
- **A headline metric you could hit without helping the user.** Tell: sign-ups, clicks, messages sent. Fix: pair the primary metric with a guardrail (tasks completed plus error rate) and say so to judges. [Calling Bullshit, p.102-105] [How to Measure Anything, p.79]

## Hackathon calibration
- **Formative, not summative.** Every 24h test is for finding and fixing problems. Statistics exist here to set floors ("at least ~40%") and to stop overclaiming, not to prove significance. Never present a 5-person test as a benchmark. [Quantifying the User Experience, p.26]
- **Judges give ~4 minutes each.** One headline number with its baseline goes in the spoken pitch; the rest go to Devpost and a backup slide. Every number needs an owner who can defend it in 30 seconds. [Seed: A. Hackathon evidence kit, §A7]
- **Commitment currency shifts.** Cash is unrealistic in a weekend; aim for time and reputation: a tester using it for a real task before judging, a named testimonial, an intro, an email given for a link tonight. Record any unprompted "can I use this?" with the person's name. [Mom Test, p.67-69, p.72-73]
- **Hackers are not your users.** Fellow attendees skew young and technical. Frame the product for whom you tested, or reach one real target user (walk the venue, DM a community) and weight that session more. [Quantifying the User Experience, p.26-28] [Calling Bullshit, p.119-120]
- **Research must be done by hour 2-3.** If a call, a DM or a walk to a table answers a question, do that instead of designing a study. [Mom Test, p.115]
- **Ignore long-horizon rigor:** formal value-of-information math (use "how uncertain × how costly if wrong"), power analysis, Cochrane-level reviews (2-minute search only, unless on a health track), growth projections (show only what is measured; any projection gets a conservative bound and a stated assumption). [How to Measure Anything, p.31] [How to Lie with Statistics, p.106-107]
- **Check eval numbers on a schedule.** Run the full test set every 2-3 hours, not after each prompt tweak; frequent small readings cause churn. [Thinking, Fast and Slow, p.331]
- **Tired teams believe bad numbers.** Depletion makes people accept claims they would reject rested; after about hour 18, any new "it works" verdict or metric claim gets a second reader before it reaches a slide. [Thinking, Fast and Slow, p.80-81]
- **Pair the headline stat with one named case.** Judges change their minds from a specific person or input, not from aggregates; show one real tester's before-and-after task next to "6 of 8 testers". [Thinking, Fast and Slow, p.167-171]
- **One honest limitation wins trust.** State one limit and one next experiment in the pitch; it reads as rigor, and judges probe overclaims. [Thinking, Fast and Slow, p.254-255] [Calling Bullshit, p.64-65]

## Where experts disagree
- **Comparing two versions with few people.** The seed suggests t-tests and N-1 two-proportion tests; Bergstrom says a coin-flip assignment with 10-20 testers is a defensible comparison; Sauro says conversion-style A/B tests need on the order of 1,000 users per version. Follow: never A/B a landing page at the event; do compare the same task with and without the tool on the same people, with a coin deciding which goes first, and claim only large, obvious gaps. [Seed: A. Hackathon evidence kit, §A3] [Calling Bullshit, p.83-85] [Quantifying the User Experience, p.31] [How to Lie with Statistics, p.70-72]
- **When a margin of error is legitimate.** Wheelan's rule (mean ± 2 standard errors, SE = SD/sqrt(n)) is stated for samples of 30 or more; Sauro calls "need n=30" a myth and uses adjusted-Wald and t-based intervals at any n. Follow Sauro for user tests under 30; Wheelan's 2-SE check is fine for eval sets of 30+ items or runs. [Naked Statistics, p.173-177] [Quantifying the User Experience, p.26, p.37-42]
- **Which average for times.** Bergstrom, Huff and Wheelan say median for skewed data (one value 5x the rest: report the median and name the outlier); Sauro shows the geometric mean is more accurate under 25 users. Follow Sauro for task times, and also show the raw values; use median and p95 for system latency. [Calling Bullshit, p.89-90] [How to Lie with Statistics, p.26-31] [Naked Statistics, p.36-37] [Quantifying the User Experience, p.45-49]
- **Scoring ideas.** Kahneman: score 4-6 criteria separately, sum, let gut vote once at equal weight. Hubbard: weighted matrices of 1-5 ratings have no evidence of improving decisions; use real units and probabilities. Follow Kahneman to rank and surface disagreement at hour 1, then put explicit probabilities (finish, judges care) on the top two. [Thinking, Fast and Slow, p.224-226] [How to Measure Anything, p.58-63]
- **Rating scales.** Fitzpatrick says drop 1-5 scales because they make chats formal; Sauro recommends a standardized post-task ease question. Follow both by context: no scales in discovery conversations; one 1-7 ease question after each usability task, reported as counts or a distribution with n, the mean only as a rough signal. [Mom Test, p.60-61] [Quantifying the User Experience, p.30, p.42-45]
- **Percentages from small n.** The seed bans percentages under 10 people; Sauro says percentages are fine with an interval. Follow the seed on slides (counts) and Sauro in Q&A (range and lower bound). [Seed: A. Hackathon evidence kit, §A7] [Quantifying the User Experience, p.35-36]
- **Count vs percent framing.** Kahneman notes "1 in 1,000" feels bigger than "0.1%" and suggests counts for vivid problem size; Bergstrom says give both so you cannot be accused of spin. Follow Bergstrom: "X of Y (Z%)" in one line. [Thinking, Fast and Slow, p.320-322] [Calling Bullshit, p.94-96]
- **Landing-page sign-ups as demand.** Fitzpatrick distrusts conversion rates without context. Follow him: quote a sign-up count only alongside 1-2 verbatim replies from real people. [Mom Test, p.80]

## Go deeper
- search_experts("adjusted Wald confidence interval small sample completion rate", domain="05-evidence-quant-research")
- search_experts("commitment and advancement time reputation money", domain="05-evidence-quant-research")
- search_experts("problem discovery 1-(1-p)^n how many testers", domain="05-evidence-quant-research")
- search_experts("bottom-up market sizing Fermi check anchoring", domain="05-evidence-quant-research")
- search_experts("false positives base rate precision rare event detector", domain="05-evidence-quant-research")
- search_experts("selection bias who is missing from the sample", domain="05-evidence-quant-research")
- search_experts("correlation causation confounder randomized comparison", domain="05-evidence-quant-research")
- search_experts("trace statistic to original source definition", domain="05-evidence-quant-research")
- search_experts("best of N runs hold-out regression to the mean", domain="05-evidence-quant-research")
- search_experts("truncated axis dual axis misleading chart", domain="05-evidence-quant-research")
