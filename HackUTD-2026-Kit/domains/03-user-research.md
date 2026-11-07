---
name: 03-user-research
description: Open when choosing the target user for a sponsor challenge (hour 0-2), writing or running the hallway interview script (hour 1-3), deciding go / narrow / pivot from interview notes (hour 3-4), building the persona and job story, testing the prototype with real users (hour ~12 and ~20), or deciding what user evidence to claim to judges.
---
# User research, audience selection, and customer understanding

## Use this when
- Hour 0-2: the team has a sponsor challenge or idea and must name ONE primary user before building.
- Hour 1-3: you are about to walk up to sponsor engineers, mentors, or other hackers and need questions that do not produce polite lies.
- Hour 3-4: notes are in and the team must decide go, narrow the segment, or switch to the fallback.
- A mentor, judge, or teammate suggests a feature or a broader audience mid-build.
- Hour 12-20: testing the prototype with 3-5 people and triaging what they hit.
- Writing the problem slide, persona, "who are your competitors" answer, or any "N users said" claim.

## Core principles
1. **Narrow to a who-where pair until you can walk to them today: "[who] at [where] who currently [workaround]."** (counterintuitive) Vague segments give mixed, uninterpretable signals, and Aulet reports never seeing a team focus too much. [Mom Test, p.97-101; Disciplined Entrepreneurship, p.143-147]
2. **Ask only about the last specific time, never "would you" or "what do you want."** People cannot predict their own behavior and answer as who they want to be; specific past events are rarely invented. [Just Enough Research, p.107-108; Mom Test, p.10-11; Interviewing Users, p.193-194]
3. **A pain is real only if they already spend time, money, or a workaround on it.** Someone with an "awful" problem who never Googled a fix is a complainer, not a customer; many observed frictions are tolerated "good enough" (satisficing). [Mom Test, p.19-20; Interviewing Users, p.26-29; Competing Against Luck, p.89-90]
4. **Define the target as a job in a circumstance, not a demographic, and never average two jobs into one product.** Milkshake commuters and parents shared a product but not a job; the "average pilot" cockpit fit zero pilots. [Competing Against Luck, p.22-23, p.40-41]
5. **Your real competitor is whatever gets hired today, including spreadsheets, group chats, and doing nothing; name what must get fired.** QuickBooks competed with a shoebox; you must beat the habit plus the switching cost, so be dramatically better. [Competing Against Luck, p.24-26, p.103-104; Seed: B. Talking to users, §B2]
6. **Adoption needs push + pull > habit + anxiety; spend at least one feature on the biggest anxiety.** (counterintuitive) Teams over-invest in pull (features) while loss aversion is roughly twice the lure of gain; anxiety reducers like sample data, undo, or a preview cut a home builder's cancellations from 5-6 a month to 1. [Competing Against Luck, p.104-105, p.108]
7. **Compliments, fluff, and feature ideas are not evidence; only facts and commitments count, weighted by what the person gave up (time, reputation, money).** "I would definitely buy that" cost the author about $10M. [Mom Test, p.24-25, p.29-30, p.67-69]
8. **Watch the job happen, then ask about what you saw.** Intermountain built software from clinician descriptions and clinicians did not use it; the milkshake team observed for 18 hours before asking "why." [Competing Against Luck, p.20, p.95-96; Talking to Humans, p.28-29]
9. **Scattered answers mean the segment is too broad: narrow it, do not add interviews.** (counterintuitive) Twenty different must-haves from twenty chats is one conversation each with twenty customer types. [Mom Test, p.92-97]
10. **Write pass/fail targets and the scary question before the first chat.** Pre-set criteria block confirmation bias; a question only counts as important if a bad answer would change your plan. [Disciplined Entrepreneurship, p.126; Talking to Humans, p.49-50; Mom Test, p.42-43]
11. **The persona is one real, re-contactable person outside the team, with ranked priorities; lead the pitch with their top priority even if it is unglamorous.** A water-filtration team assumed "green" was the edge; facilities managers ranked reliability, growth, cost, then green a distant fourth. [Disciplined Entrepreneurship, p.154, p.177-184, p.189-195]
12. **The people who build must hear users first-hand, in pairs (one asks, one writes verbatim).** Second-hand "the customer said" becomes a trump card and loses detail; a third interviewer makes people less open. [Mom Test, p.103-108; Interviewing Users, p.116]

## Decision procedure
Main decision: which single user to build for, and whether the pain is strong enough to commit by hour 4.

1. **List segments (0:00-0:20).** Each teammate silently writes end user + use case pairs for the sponsor challenge; merge to 6-12, including fringe ones. [Seed: C. Audience selection, §C1; Disciplined Entrepreneurship, p.92-93]
2. **Score (0:20-0:50, hard stop at 45 min of debate).** Each person scores every segment 1-3 independently on: compelling pain, reachable at the venue today, whole core flow demo-able in 24h, has budget/sponsor/obvious value, entrenched competition (count "doing nothing"), sponsor-track fit, "will we care at hour 20." Break ties with the YC triple: cost of the problem, frequency, buyer authority (McDonald's beats The French Laundry). Pick the top score; write the runner-up as the only fallback. [Disciplined Entrepreneurship, p.96-98, p.141-142; Seed: B. Talking to users, §B1]
3. **Write the research kit (10-15 min).** (a) who-where sentence; (b) one-line screener: "Have you done [task] in the last month?"; (c) research question with an outcome verb ("We will identify the two most frequent obstacles..."), not "understand"; (d) the 3 riskiest assumptions plus one question that could kill the idea (5-minute pre-mortem); (e) pass target on the whiteboard: **at least 4 of 6 screened users describe the pain before you mention it AND have used a workaround in the last month.** [Just Enough Research, p.57-59; Mom Test, p.57, p.105-106; Disciplined Entrepreneurship, p.126]
4. **Classify the risk.** If the idea's main risk is product (can the model/data/hardware work at all), conversations cannot resolve it: send one person to prototype that piece now and keep interviews short. If it is market risk (do they care), interviews are the priority. [Mom Test, p.52-56]
5. **Run 5-8 conversations (hour 1-3).** Two parallel pairs, rotating lead. 5 minutes to screen and confirm the problem exists; 10-15 for good fits. Script in the Seed (§A1): role, hardest part, last time, why hard, frequency, cost, what tried and what you dislike about it, who pays, show me, what should I have asked. End every chat with "who else deals with this even more than you?" [Seed: A. Hackathon quick-run protocol, §A1; Mom Test, p.58-63; Talking to Humans, p.54]
6. **Debrief after every 2-3 chats (5 min).** Tally against the pass target; each person names one surprise and one thing that contradicted the plan (empty list = not listening). Rewrite the guide. [Disciplined Entrepreneurship, p.133; Talking to Humans, p.63]
7. **Decide at hour 3-4.**
   - **GO** if the pass target is met and the last 2-3 people repeated themes you already had (saturation). Lock persona and job story.
   - **NARROW** if answers split across user types: keep the subgroup with the strongest signals (emotion, existing workaround, money/time spent), drop features only others asked for, run 2-3 more chats with that subgroup only.
   - **PIVOT** to the runner-up if 3 of the first 5 screened users show no workaround and no urgency. Do it by hour 3; hour 6 is far cheaper than hour 16.
   - Change direction only when 3+ independent sources agree; one passionate interviewee is a hypothesis. [Mom Test, p.43-45, p.93-97; Disciplined Entrepreneurship, p.134, p.242-245; Talking to Humans, p.90]
8. **Synthesize (30-45 min, never under 30).** One verbatim quote per sticky, silent clustering, name 3-5 themes, tag quotes push/pull/anxiety/habit, write 1-3 job stories ("When [situation], I want to [motivation], so I can [outcome]", no product names, one job each), then 2-3 "How might we" questions to brainstorm against. [Seed: D. Understanding why customers switch, §D2; Interviewing Users, p.270, p.283-284]
9. **Re-test at hour ~12 and ~20** with 3-5 people from the same segment (ideally the same ones). Give a goal, not instructions; the builder of the feature does not facilitate. Any issue hit by 2+ testers on the demo path is Tier 1: fix it, then retest with one fresh person. End each test with a concrete ask (email for tonight's link, a named intro, a quote with name and role). [Just Enough Research, p.137-144; Mom Test, p.65-67]

## Checklists
**Interview guide (run before anyone walks out)**
- [ ] Screener is the first sentence of every chat; screener failures are excluded from counts.
- [ ] No question starts with would / do you / is / are; no "A or B?" options inside a question.
- [ ] Opens broad ("what do you spend most of your time on?") before zooming in, so the topic can appear unprompted.
- [ ] Contains the scary question and at least one cost probe (time per week, money, tools tried).
- [ ] 5-8 prompts on one card, not a script; idea and pitch banned until the last 2 minutes, if at all.
- [ ] Verbal consent includes "may we quote you anonymously on our slides?"; nobody under 18.

**Evidence claim (run before any slide or judge answer says "users")**
- [ ] Every note line tagged F (fact), C (compliment), H (hypothetical), I (idea); only F lines and commitments are counted.
- [ ] Counts said as "5 of 7 people we talked to," never as a percentage or "statistically."
- [ ] A source column shows who was a friend or friend-of-friend; those are flagged, not counted as validation.
- [ ] Each counted interview contains at least one concrete last-time story.
- [ ] Evidence rung named: conversation, mockup reaction, Wizard-of-Oz trial, or working prototype.
- [ ] One-line limits statement ready: who we talked to, who we missed.

**Persona and job output**
- [ ] Persona is a real person you can message again this weekend, not a teammate, matching a pattern seen in 3+ people; each field marked evidence or guess.
- [ ] Job story plus functional, social, and emotional lines; at least one UI decision serves the emotional line.
- [ ] Top 3 ranked priorities (100-point split if you got it); headline benefit equals priority #1.
- [ ] "Replaces: X" (including a non-software alternative) and "Built for X, not for Y."
- [ ] Biggest anxiety named and one reducer shown in the demo (under an hour to build).
- [ ] 2-3 verbatim quotes and one photo or screenshot of the real workaround.

## Anti-patterns
- **Reporting stated intent.** Tell: "8 of 10 said they would use it" on a slide. Fix: report what they do now, what it costs them, and what they committed to. [Mom Test, p.29-30; Interviewing Users, p.38-39]
- **Interviewing your circle.** Tell: the interviewee list is teammates' friends, or a teammate says "I would use this." Fix: recruit one degree removed (other teams in the segment, mentors, people in registration and lunch lines); use teammates only as a reality check. [Talking to Humans, p.53; Disciplined Entrepreneurship, p.127, p.155]
- **Google Form instead of conversations.** Tell: someone proposes a poll to settle an argument, or quotes a percentage from n under 30. Fix: five person-to-person chats; use a form only to screen or recruit. [Just Enough Research, p.119-120, p.173-180]
- **The blended persona.** Tell: the problem statement could describe five unrelated apps, or features come from different user types. Fix: add who/when/where until it describes one job; move the others to a "not now" list. [Competing Against Luck, p.43-44; Disciplined Entrepreneurship, p.88]
- **Pitching or validating mid-interview.** Tell: you talk more than 20% of the time, say "cool" or "me too," or summarize "so basically...?" and get a polite "right." Fix: minimal "mm" acknowledgments, wait a second beat of silence, save summaries for the debrief. [Mom Test, p.39-41; Interviewing Users, p.158-160, p.181-182, p.202-203]
- **Obeying feature requests.** Tell: a mentor suggests a feature and it lands in the backlog. Fix: ask "why do you want that, what would it let you do, how do you cope without it?" and check if it can be faked or handled manually. [Mom Test, p.34-38]
- **Banking compliments.** Tell: "that meeting went really well" with no fact or next step. Fix: reply to praise with "how do you handle this today?" and end with a time or reputation ask. [Mom Test, p.25-29, p.65-67]
- **Builder runs the test and rescues the user.** Tell: hints, explanations, tech support during the session. Fix: swap roles; at each stall ask "what did you expect to happen?" and note it silently. [Just Enough Research, p.139-140; Interviewing Users, p.202-204]
- **Top-down market math.** Tell: "0.1% of X billion people." Fix: "We talked to N people in segment Y; Z described this pain and use workaround W." [Disciplined Entrepreneurship, p.89-90]

## Hackathon calibration
- **Sample size.** Books cite 50-100 conversations for consumer products and saturation around 6-12 interviews [Talking to Humans, p.72-73; Seed: C. Audience selection, §C2]. Here: 5-8 in hours 1-3, 8-15 across the event, every teammate doing at least 2 by hour 6, always stating n. Act on a theme only when 3+ independent people raised it unprompted. [Talking to Humans, p.70-71, p.91]
- **Time.** Cap discovery at 3-4 hours. Analysis normally takes 2-3x interview time [Interviewing Users, p.270]; compress to about 1 hour of synthesis per hour of interviews, minimum 30 minutes. Keep three touchpoints (hour 1-4 discovery, ~12 prototype, ~20 final flow) rather than one block. [Talking to Humans, p.92]
- **Commitments.** LOIs, deposits, and pre-orders rarely fit 24h. Aim for time and reputation: a tester using it on a real task before judging, an email for tonight's link, a named intro, a quote with name and role. Record any unsolicited "can I use/buy this?" with the person's name for the pitch. [Mom Test, p.67-73]
- **Who is reachable.** Sponsor engineers and recruiters at booths, mentors, other hackers who fit the segment, idle lines, campus Discords for recruiting only [Seed: A. Hackathon quick-run protocol, §A]. Prefer a segment at the venue or UT Dallas so you can test in person [Disciplined Entrepreneurship, p.142-143]. If a sponsor engineer starts pitching their product, ask what they expect from the chat, then steer with "yes, and today I'm curious about your day-to-day." [Interviewing Users, p.131]
- **Switch interviews.** The Moesta method wants people who switched within 30 days (ideally 14) [Seed: D. Understanding why customers switch, §D3]. At the event, use the four forces as tags on ordinary last-time interviews, and grab any recent tool-switcher you meet.
- **PMF survey.** The Superhuman 40% "very disappointed" benchmark needs users who used the product twice in two weeks and about 40 responses [Seed: E. Measuring whether users truly want it, §E1]. With 10 or so testers, the question is directional only: say "6 of 10 testers," never "PMF."
- **Ignore for 24h:** TAM sizing beyond one honest line, full life-cycle use case maps, sales-cycle analysis, fundraising risks [Talking to Humans, p.24-25].
- **What judges see in ~4 minutes:** one named persona in a specific moment, the photographed workaround as the "before," one verbatim quote, one "N of M" count, "replaces X," and "built for X, not Y." Judges asking "who needs this and how do you know?" are probing principle 3. [Interviewing Users, p.26-29; Competing Against Luck, p.98]
- **No users reachable for the segment?** Act as the AI yourself (Wizard of Oz) for a couple of testers in the first half, and say which evidence rung you reached. [Talking to Humans, p.50-51, p.71-72]

## Where experts disagree
- **Asking about future use or price.** Fitzpatrick and Hall: never. Portigal: ask anyway and read the reasoning as a mental model, not a prediction. Constable: make pricing feel real with a fake "join at $X" button. Follow here: no hypotheticals in the first 80% of a chat; one "what would make this worth paying for?" at the end is fine for language, never cited as demand; use a click-counting button if you need a price signal. [Mom Test, p.29-30; Just Enough Research, p.107-108; Interviewing Users, p.119-120; Talking to Humans, p.48]
- **Length and formality.** Fitzpatrick: casual, 5 minutes is enough to learn if a problem exists, never call it an interview. Portigal: rapport can take minutes to an hour, budget 20. Follow: 5-minute screens for everyone, 15-20 minutes only with the 2-3 strongest-fit people (persona candidates). [Mom Test, p.58-63; Interviewing Users, p.132-134]
- **How many is enough.** Fitzpatrick: 3-5 if answers converge. Constable: 50-100 for consumer. Aulet: 10 similar excited prospects. Christensen: a few deep stories beat many shallow ones. Follow the saturation rule with the 3+ independent-sources threshold; Aulet's own hackathon scaling says 3-5 matching users responding to the same story is a pass. [Mom Test, p.92; Talking to Humans, p.72-73; Disciplined Entrepreneurship, p.240-243; Competing Against Luck, p.124-125]
- **Hypotheses versus beginner's mind.** Christensen and Portigal: go in without feature hypotheses; dump assumptions so you can hear surprises. Constable, Aulet, and Fitzpatrick: write risky assumptions and numeric pass/fail targets first. Reconcile: write hypotheses and targets about the user and problem, never about features, and keep all of them out of the conversation itself. [Competing Against Luck, p.111; Interviewing Users, p.143-144; Talking to Humans, p.45-50]
- **Real person or archetype.** Aulet: one actual person. Hall: archetypes from observed patterns. Seed allows a blend of two. Follow: a real person you can re-contact, accepted only if their pattern appeared in 3+ interviews, because a single persona can be an outlier. [Disciplined Entrepreneurship, p.177-182, p.240-243; Just Enough Research, p.111]
- **Surveys.** Hall: the most dangerous tool, never a fallback. Portigal: pair interviews with a 3-question form for rough counts. Follow: only after interviews, only to check a theme already found, reported as raw counts with n and who responded. [Just Enough Research, p.173-175; Interviewing Users, p.37-38]
- **Remote contact.** Fitzpatrick and Constable: in person first, phone last, no chat for research. The Seed lists phone calls and Discord. Follow: walk up to people at the venue; video if remote; Discord and DMs only to recruit. [Mom Test, p.89; Talking to Humans, p.61; Seed: A. Hackathon quick-run protocol, §A]

## Go deeper
- search_experts("last time it happened interview questions", domain="03-user-research")
- search_experts("compliments fluff hypotheticals bad data commitment", domain="03-user-research")
- search_experts("beachhead segment selection criteria narrow", domain="03-user-research")
- search_experts("push pull anxiety habit switching forces", domain="03-user-research")
- search_experts("workaround nonconsumption competing with nothing", domain="03-user-research")
- search_experts("persona real person ranked priorities 100 points", domain="03-user-research")
- search_experts("pass fail criteria confirmation bias interview targets", domain="03-user-research")
- search_experts("usability test severity frequency tiers facilitator", domain="03-user-research")
- search_experts("silence follow-up questions mirror participant words", domain="03-user-research")
- search_experts("affinity synthesis job story how might we", domain="03-user-research")
