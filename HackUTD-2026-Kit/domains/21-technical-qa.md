---
name: 21-technical-qa
description: Open when preparing or running judge Q&A, such as writing the Saturday-night question bank and accusation audit, running a mock Q&A, answering a skeptical, vague, hostile, or "is this real?" question at the table, handling "I don't know" or a missing feature, or deciding after a judge visit whether to change the pitch or the answer.
---
# Technical Q&A and objection handling

## Use this when
- Saturday night: drafting the question bank, the real/mocked/hardcoded list, and the accusation audit before Sunday judging.
- Sunday-morning mock Q&A: a teammate or mentor plays the hard technical judge, the business judge, and the skeptic, and you need to decide what to fix.
- At the table, a judge asks something vague ("does it scale?"), loaded ("isn't this just a ChatGPT wrapper?"), or based on a wrong premise.
- A judge asks for a number you never measured, a feature you did not build, or "what's real versus mocked?"
- A sponsor-track judge asks why their tech is central rather than bolted on.
- After 2 or more judge visits, the same objection keeps coming back.

## Core principles
1. **A repeated objection means the pitch is broken. Fix the pitch, not the rebuttal (counterintuitive).** Objections mostly come from the presenter, not the listener. Teaching high-objection sellers to build the need first, without ever mentioning objections, cut objections per hour by 55%. Across 694 calls, more objections meant lower success, not more interest. [SPIN Selling, p.147-148, p.163-167]
2. **Diagnose before you answer. A judge's literal words are a position, and the concern behind them is what you have to answer (counterintuitive).** The usual failure is a fast, polished answer to the wrong problem. Use LAER's Explore step ("cost, latency, or getting users?") or a mirror of the last 1-3 words, then wait 4 seconds. [Seed: Q&A technique sources, §C4; Never Split the Difference, p.34, p.41; Getting to Yes, p.59]
3. **Answer, then evidence, then so-what, then stop.** Use 2-3 sentences and never go past 60-90 seconds. If the judge wants more, they will ask, and a short answer leaves time for another question. [Seed: Synthesis, §3; Seed: Hackathon Q&A kit, §A1]
4. **Put the number before the interpretation, and make it person-sized.** "In our test of 50 inputs, 41 succeeded" persuades because the judge can follow your path from evidence to conclusion. "It caught 9 of the 10 cases we tested" lands better than "F1 0.87." [Crucial Conversations, p.147-150; Pitch Anything, p.101-102]
5. **Never bluff. Say what you tested, what you did not, and how you would find out.** Calibrated claims carry more weight than absolute ones. Use the pattern "we tested A and B; I'd expect C to behave like B because..., but we haven't verified it." Concede to good reasons, never to pressure: "we did not build that" beats a bluff. [Crucial Conversations, p.153-155; Getting to Yes, p.99-100; Seed: Q&A technique sources, §C3]
6. **Every design choice gets "because" plus a tradeoff.** Attaching any reason took compliance in Langer's study from 60% to over 90%. The format: "We chose X over Y because [requirement]. It costs us [sacrifice]. If [condition], we'd use Y." It takes 15-20 seconds, and naming the cost is what signals seniority. [Never Split the Difference, p.189; Seed: Hackathon and judge sources, §B8]
7. **Run an accusation audit and say the top criticisms first, calmly.** If you say "you're probably thinking we just glued two APIs together" before the judge does, the sting is gone and you control the framing. Denying a criticism after it is raised makes it more believable. [Never Split the Difference, p.55-59; Seed: Hackathon Q&A kit, §A5]
8. **Concede a real gap in one sentence, give one next step, and never probe a need you cannot meet (counterintuitive).** Acknowledging the gap costs nothing. Asking "why do you need that?" about a missing feature makes the judge spell out its value and raises its weight. [Getting to Yes, p.51-52; SPIN Selling, p.122-123; Never Split the Difference, p.50-51]
9. **A nod or "you're right" is not a win. "That's right" is.** People say "you're right" to end the exchange. A judge who elaborates or asks a follow-up has taken in your point. [Never Split the Difference, p.82, p.86-89]
10. **Answer the judge's real criterion, not the generic one.** A sponsor engineer wants to know if their tech is used well, a business judge if it is viable, a professor if it is technically sound. Map each question to viability, technicality, impact, or uniqueness. [Seed: Doing Discovery translation to HackUTD, §A3; Getting to Yes, p.59]
11. **Anything in the repo, a teammate can explain.** Teams lose when an AI wrote the feature that sets them apart and nobody can explain it under questioning. [Seed: Hackathon and judge sources, §B2]
12. **Slow down, pause before every answer, and never counterattack.** Rushing makes the judge feel unheard. A visible pause reads as confidence, and fight-or-flight wrecks reasoning at hour 20 and later. [Never Split the Difference, p.29, p.43, p.129-132; Getting to Yes, p.48-49]

## Decision procedure
How to handle one judge question at the table. Assume about 4 minutes per judge, which leaves room for 2-4 questions.

1. **Let them finish.** Pause one beat (1-2 seconds) before speaking, even if you know the answer.
2. **Classify the question in your head:** clear factual / vague or loaded / wrong premise / don't know / missing feature / real weakness / hostile.
3. **If you can think of two plausible meanings, explore before answering.** Ask "are you asking about X or Y?" or mirror the key words and stay silent for 4 seconds. Explore at most twice. If it is still unclear, paraphrase it once ("so you're asking whether this survives past a demo?") and answer that. For a simple factual question, skip this step.
4. **Only the owner answers** (owners are set in advance by question type, see Checklist A). A teammate adds at most one sentence ("To add to that..."). Nobody contradicts a teammate in front of the judge.
5. **Answer with the formula:** one conclusion sentence, one piece of evidence with a number from your own tests or interviews, one so-what tied to the user or the judge's criterion. Target about 30 seconds and stop at 90. For "why X?", use the tradeoff line from principle 6.
6. **Branch by type:**
   - *Don't know:* repeat the keyword, give the reason you lack it, say what you do know, then "we'd find out by [method]." If you are saying "I don't know" to a core question about your own product, mark it as a prep failure for the debrief.
   - *Missing feature:* "Not built in 24 hours. Here's how we'd add it: [one line]." Do not ask why they want it.
   - *Wrong premise:* correct it with facts and soft wording ("I may have explained that badly; it runs locally, so no data leaves the device"). Never nod along to a wrong premise.
   - *Real weakness:* "You're right, [gap]. We'd fix it first at [step]." That is two sentences, with no defending the past.
   - *Hostile:* label it ("It sounds like you're worried this is just another wrapper"), answer the substance, and ignore the tone.
7. **Check that it landed.** Ask "Does that answer it?" or "What would make this stronger for you?" If you get a flat "yeah" and the judge moves on, that is fine. If the judge comes back to the same objection, name the shared goal ("you want something that could ship; here's the path") and answer once more. If it comes up a third time, offer the repo or README and move on.
8. **Close** with one sentence restating the main point, then thank them. Do not let the visit trail off on the last question.
9. **Debrief within 2 minutes of the visit.** The assigned listener logs each question word for word, plus any parting comment. Stop/go rule: if 2 judges, or 2 rehearsal listeners, raise the same objection, edit the pitch to address it before the next visit instead of polishing the answer. Tag each objection "early" (the solution came before the problem was established) or "value" ("why switch?", "who'd pay?"). Either tag means the problem section of the pitch needs strengthening.

## Checklists
**A. Q&A one-sheet (finish by Saturday night, one page, carried to the table)**
- [ ] A 1-2 sentence answer for each question bank category: problem and user, differentiation, architecture, why AI, real vs mocked, scale and cost, failure handling, business, what's next, what we learned.
- [ ] Accusation audit: 5-8 criticisms listed, top 3-5 kept, each turned into a label line plus an honest answer, each marked "say in pitch" or "hold for Q&A."
- [ ] Real/mocked/hardcoded list with one honest line each, covering what is seeded, why, and what real integration would take.
- [ ] Tradeoff lines for the 3-5 biggest technical choices.
- [ ] AI evaluation line: "We tested on N hand-labeled examples and got X right. The main failure mode is Y, handled by Z."
- [ ] Roadmap lines for the 3 features judges are most likely to ask about that we did not build.
- [ ] Owner and backup for each question type. Every teammate can explain the architecture in 60 seconds.
- [ ] Sponsor track: 3 phrases from the challenge text to reuse naturally, plus the line "why [sponsor tech] is central."
- [ ] 3 calibrated "what/how" questions per teammate, such as "What part of this matters most for your team?"

**B. Self-check on every drafted answer**
- [ ] The first sentence is the conclusion.
- [ ] It contains at least one number we measured or heard firsthand, with the sample size.
- [ ] Every design decision has a "because" in the same sentence.
- [ ] 3 sentences or fewer, about 30 seconds read aloud.
- [ ] No "100%", "no competitors", "we didn't have time", "it was working earlier", or "I think" when we know the answer.
- [ ] It ends tied to the user or the judge's criterion.

**C. Post-visit debrief**
- [ ] Questions logged word for word, describing behavior only ("asked 3 pricing questions"). Words like "hated it" or "didn't get it" are banned.
- [ ] One thing that surprised us.
- [ ] Pattern check run (procedure step 9).

## Anti-patterns
- **Polishing a rebuttal for a recurring objection.** Tell: the third judge raises the "wrapper" concern. Fix: add one line to the pitch that addresses it. [SPIN Selling, p.154-155; Crucial Conversations, p.208-209]
- **Answering fast and solving the wrong problem.** Tell: the judge rephrases the same question. Fix: explore first (procedure step 3). [Seed: Q&A technique sources, §C4]
- **Inventing a number.** Tell: "I think it's around..." for something you never measured. Fix: the don't-know pivot plus how you would measure it.
- **"We have no competitors."** Tell: the judge's eyebrows go up. Fix: name the status quo (spreadsheets, doing it by hand, doing nothing) and one real tool, with one line on why a user would switch. [Seed: Synthesis, §8; Pitch Anything, p.114]
- **Feature tour as an answer.** Tell: the answer lists 4 or more features. That invites "how is this viable?" because long feature lists raise cost and price concerns. Fix: give 2-3 benefits tied to a need the judge stated. [SPIN Selling, p.150-154, p.170]
- **Defending the past.** Tell: "we didn't have time" or a long explanation of a shortcut. Fix: "we prioritized X over Y because...", then the next step. [Getting to Yes, p.66-67]
- **Two answerers.** Tell: teammates talk over or correct each other. Fix: the owner table and the one-sentence add-on rule. [Seed: Hackathon Q&A kit, §A4]
- **Asking a judge "why?" or "what do you mean?"** Tell: the judge gets defensive or curt. Fix: mirror their words, or ask "What about this doesn't work for you?" [Never Split the Difference, p.127-128]
- **Late-night snapping.** Tell: sarcasm, going quiet, over-explaining. Fix: an agreed tag-out hand signal, and the silent question "why would a reasonable person ask this?" [Never Split the Difference, p.129-132; Crucial Conversations, p.133-135]

## Hackathon calibration
- **Time compresses every technique.** With about 4 minutes per judge, the full LAER loop shrinks to at most one Explore question. Voss's "that's right" loop becomes one summary attempt. Crucial Conversations' mirror, paraphrase, prime sequence becomes one mirror plus one question at most.
- **Judges deliberate without you.** With about 200 projects in the room, end each exchange with one line the judge can repeat to co-judges, ideally built on something they said. [SPIN Selling, p.109-112; Getting to Yes, p.89-90]
- **Match the track.** General judges score uniqueness, technicality, viability, UI/UX, complexity, usefulness, and impact. Sponsor judges score their own tech and use case. MLH judges score technology, design, completion, and learning, so prepare a real "what did you learn" answer for them.
- **Ignore the long-horizon sales advice.** Skip Cohan's 25-minute discovery and second-call ask, buying-committee mapping, and revenue forecasts. For viability, give cost per query or per user plus one assumption you tested, not a TAM or a hockey-stick curve. [Pitch Anything, p.113-114]
- **Ignore the dominance tactics.** Skip Klaff's push/pull walk-outs, "qualify yourself to me," and refusing small talk. Use only the calm, unfazed part: "fair challenge, here's what we tested." [Pitch Anything, p.9-10]
- **Use risky moves sparingly.** "How would you suggest we approach that in 24 hours?" works only in a warm tone, and it is anecdote-grade advice. [Never Split the Difference, p.125-127] Feel-Felt-Found works only with real interview evidence. Without it, answer directly. [Seed: Q&A technique sources, §C5]
- **Fatigue is the main risk at hour 20 and later.** Decide your tone in advance, rehearse the 3 hardest answers in a slow, low voice, and rotate who delivers the 3 core sentences each hour. [Never Split the Difference, p.43, p.48]

## Where experts disagree
- **Asking "why."** Voss says "why" sounds like an accusation [Never Split the Difference, p.127-128]. Cohan and Rackham use soft "why is that important?" questions to surface value [Seed: Doing Discovery, §B6; SPIN Selling, p.103-106]. Follow this: never ask a judge "why"; use "What about that matters most to you?" A soft "why is that important?" is fine in user interviews, where you have time to build rapport.
- **Restate first or answer first.** Getting to Yes and Crucial Conversations say to restate the concern before answering [Getting to Yes, p.51-52; Crucial Conversations, p.174-175]. The seed formula puts the conclusion first. Getting to Yes p.66 even says to give the constraint before the conclusion. Follow this: paraphrase only loaded or multi-part questions (5 seconds), and answer factual ones immediately. For design questions, fold the constraint into one clause: "Given 24 hours and no labeled data, we chose X because..."
- **Raise weaknesses first or hold them back.** Voss says to say your accusations aloud first [p.55-59]. Getting to Yes says not to pour out every limitation unasked [p.53]. Follow this: pre-empt only the 1-2 criticisms nearly every judge will raise (wrapper, fake data) in one line each, hold the rest for Q&A, and never deny a gap when asked.
- **How deep to go.** Klaff says to give a high-level number and redirect, because detail cools the room [Pitch Anything, p.50-51; opinion]. System-design rubrics reward going deep and justifying tradeoffs with evidence [Seed: Hackathon and judge sources, §B8]. Follow this: give the short answer first, and if a technical or sponsor judge digs, go as deep as they want. Technicality is a scored criterion, and Klaff's argument is opinion-grade.
- **Small talk.** Klaff says skip it [p.85-86]. Voss says to show real similarity early [p.187-188]. Follow this: one true line of common ground taken from the judge's badge or bio, then start.

## Go deeper
- search_experts("prevent objections build need before solution", domain="21-technical-qa")
- search_experts("accusation audit label skepticism before answering", domain="21-technical-qa")
- search_experts("mirror calibrated what how questions silence", domain="21-technical-qa")
- search_experts("that's right versus you're right agreement", domain="21-technical-qa")
- search_experts("STATE my path talk tentatively calibrated claims", domain="21-technical-qa")
- search_experts("interests behind positions objective criteria standard", domain="21-technical-qa")
- search_experts("implication need-payoff questions benefits", domain="21-technical-qa")
- search_experts("critical business issue delta quantify current desired state", domain="21-technical-qa")
- search_experts("explain why not that decision record tradeoff", domain="13-architecture-tradeoffs")
- search_experts("hallucination failure modes evaluation honest limits", domain="15-ai-app-design-eval")
