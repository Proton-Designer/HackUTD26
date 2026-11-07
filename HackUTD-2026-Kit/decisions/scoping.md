---
name: scoping
description: Load at H1:30-H3 when turning the locked idea into capacity math, a demo path, and one cut line; whenever someone proposes "one more feature" after H6; and at the H3/H6/H8/H12/H14/H18/H20 checkpoints when the build is behind and something must be cut.
---
# Decision guide: scoping

## Open this when
- **H1:30-H3:00:** the idea is locked. Produce the capacity math, the demo path with Real/Fake/Cut labels, a single cut line, and the not-doing list before anyone writes feature code.
- **Any time after H6:** a teammate, mentor, or sponsor rep says "we should also...". After H6 the default answer is no unless the admission check passes.
- **H3, H6, H8, H12, H14:** a checkpoint arrives and a spike failed, the skeleton is not live, or half the time is gone with a third of the work done.
- **H18-H20:** something is unfinished at freeze and someone asks for "one more hour".

## Steps
1. **Capacity (5 min).** Build hours = hours left after idea lock minus ~3h for demo prep (target 15-18h). Multiply by 4 people, then subtract 30% for work you only discover by building. Musts may use at most 60% of what remains. Example: 16h x 4 = 64, minus 30% = 45, so Musts are 27 person-hours or less. Multiply any estimate by 1.5-2x for a new API or deploy path and 2-3x when a standalone script must plug into the shared app. This is tighter than a 50/30/20 split, on purpose.
2. **Demo path (20 min).** 3-5 steps, 60-90 seconds, completable by a judge in under 2 minutes. Mark the one differentiator step. Nothing off the path goes above the line.
3. **Label every step Real, Fake, or Cut.**
   - Differentiator: Real, always. If it cannot be real by H12, change the differentiator; do not fake it.
   - Depends on something gated, paid, slow, or flaky: Fake it (recorded response, cached output, seed data) and write its one-line honest framing now.
   - Table stakes (auth, settings, admin, payments, sharing): hardcode or cut. Seeded demo account, zero settings pages.
   - Over 2h and not the differentiator: find the 1-hour version or cut.
4. **Admit features one at a time.** A feature goes above the line only if all four hold: it is on the demo path; you can finish "a judge will ___ differently because of this"; it makes another feature better; it costs 2h or less (only the differentiator may exceed that). Price it as UI + backend + error state + demo data + pitch line. If it needs more than 3 of those five, it is not cheap.
5. **Draw one line, not three tiers.** Use MoSCoW once to sort the brainstorm, then collapse to a single in/out line. Items below the line get a "~" prefix and are reviewed only if the demo path is green at H20.
6. **Not-doing list (10 min).** At least 5 named exclusions (users, platforms, flows). Ask each teammate which pet feature they gave up. If nobody gave one up, scope is not cut enough; cut again.
7. **Reliability math.** Multiply per-step success on the demo path (10 steps at 95% each is about 60%). If the end-to-end estimate is under ~90%, cut a step, cache a result, or replace an agent loop with a fixed chain of 1-2 model calls. Keep at most 2 external integrations required on the path; put the rest behind a DEMO_MODE flag.
8. **Spike and skeleton.** Every external integration returns one real response from a minimal script by H2, or it is dropped unless it is core or sponsor-required. The riskiest technical unknown gets an owner, a written question, and an H3 deadline. A walking skeleton (UI -> API -> DB/LLM -> UI) is live on a public URL by H3:30. Stop rule: not live by H3:30 means all four stop feature work and fix deploy.
9. **Run checkpoints with triggers written now** (Template). Act on the trigger, not the mood. At each check-in, each person reports each slice as uphill (unknowns remain) or downhill (just executing), never as percent done, and names the blocker for anything uphill.
10. **State every call out loud.** The scope owner decides. Announce each cut or admit as: "We [cut/keep] X because [principle] [citation]; the cost is Y; the fallback is Z." Log it. A settled cut reopens only when a trigger fires, not because someone is tired or bored.

## Template
```
SCOPE SHEET  (fill H1:30-H3; re-read at every checkpoint)
Capacity: __h left - 3h prep = __h x 4 = __ ph, -30% = __ ph   Musts cap (60%) = __ ph
Differentiator (runs live on a judge's fresh input): ______________________

DEMO PATH (60-90 s)        R/F/C  Owner  Est h  x mult  Real call by  Honest line if Fake
1. ________________         _      __     __     __      H__           ________________
2. ________ [DIFFERENTIATOR] R     __     __     __      H__           n/a
3. ________________         _      __     __     __      H__           ________________
4. ________________         _      __     __     __      H__           ________________
Musts total: __ ph   <= cap?  Y / N  (N -> cut before assigning work)
Reliability: __ x __ x __ x __ = __   (< 0.90 -> cut or cache a step)
Required external integrations on path (max 2): ________ ________

=================== CUT LINE ===================
~ ________________  (review only if path is green at H20)
~ ________________
NOT DOING (>= 5): ______ | ______ | ______ | ______ | ______
Pet feature given up:  P1 ______  P2 ______  P3 ______  P4 ______

ADMISSION CHECK (any late add)
Feature | on path? | judge does ___ differently | improves which feature | <=2h? | deepens or broadens? | what equal item comes off
______  |   Y/N    | ________                   | ________              |  Y/N  |  D / B               | ________

CHECKPOINT TRIGGERS (agreed now, read aloud on the hour)
H2     every integration returned 1 real response   else drop it (unless core/sponsor)
H3     spike returned real data inside the app       else swap approach or fake it now
H3:30  skeleton live on public URL                   else all 4 stop and fix deploy
H6     differentiator: real output on real input     else one 60-min alternative, then zoom in
H8     skeleton runs end to end                       else cut to the single surviving path
H12    full path runs on the deployed URL             else cut to steps that run; fake or drop the rest
any    >= half the time gone, <= 1/3 done             cut now
H14    new-feature freeze                             new ideas -> roadmap list only
H18    code freeze                                    fix only P0 (crash, data loss) and P1 (visible in demo)
H20    anything still uphill                          cut it; use its fallback (cache, recorded clip)

DECISION LOG
H__ | cut/keep ______ | because ______ [citation] | cost ______ | fallback ______
```

## Principles
1. **Fix the time, flex the scope, and keep Musts at 60% of capacity or less.** An appetite starts from a number and ends in a design, so the deadline never moves and the feature list does. [Shape Up, p.29-30] [Seed: D. Prioritization frameworks, §D2]
2. **Cut early as one coherent whole, never by whatever runs late.** (counterintuitive) Cutting by lateness ships an incoherent product; if a feature can be cut without harm it was never part of the minimum. Make cuts by ~H6, then protect the core by stealing from polish. [Inspired, p.137-139]
3. **Push the scariest unknown uphill first and count it solved only when real data returns inside your app.** (counterintuitive) Login and the UI shell feel productive and teach nothing; reading the docs is "thought about it", not "validated". [Shape Up, p.111-112, p.139] [Lean Startup, p.100-101]
4. **Mock the plumbing, never the magic.** Seed data, recorded responses, and hardcoded auth are fine off the core; the differentiator must run live because judges probe it and technicality is scored. [Seed: A. Hackathon Kit, §A7] [Lean Startup, p.85-91]
5. **Every estimate over 2 hours triggers "what is the 1-hour version?"** Restate the problem with the same user outcome: IMVU replaced avatar walking with teleporting and users ranked it a top-3 feature. [Lean Startup, p.92-93] [Getting Real, p.46]
6. **Multiply step reliabilities before you trust the demo path.** 95% per step over 10 steps is about 60% end to end, and five serial dependencies at 99.9% cap you near 99.5%, so required integrations stay at 1-2. [AI Engineering, p.539] [Nygard, Release It!, p.102-105]
7. **The guiding policy must tell a teammate what NOT to build.** If nobody can name a proposed feature the policy rules out, it is a vision, not a scope. [Good Strategy Bad Strategy, p.89-91, p.76-77]
8. **Build half a product, not a half-assed one.** Two features that work flawlessly beat six that half-work, and each path screen needs regular, blank, and error states because judges land on the empty screen. [Getting Real, p.81-84] [Seed: 0. Synthesis / Playbook, §6]
9. **Deepen for your one user; decline anything that broadens to another.** Every late admit names an equal-size item that comes off the line. [Playing to Win, p.104-105] [Good Strategy Bad Strategy, p.34-35]
10. **At the deadline, only all-downhill work gets more time.** (counterintuitive) Uphill work at freeze means the concept had a hole; cut it and use the fallback rather than eating rehearsal time. [Shape Up, p.148-149]
11. **"Good enough" means clearly beats today's workaround, not the ideal.** Once the demo beats the manual or competitor baseline, stop polishing and rehearse. [Shape Up, p.143-144]

## Mistakes
- **Layer-cake build.** Tell: at H6 frontend and backend each "work" but have never been joined. Fix: integrate a thin slice now; the integrator runs the full path on the deployed URL every 2h. [Shape Up, p.103-104]
- **Gutted big idea.** Tell: the demo shows 30% of a grand vision with dead buttons. Fix: the smallest complete experience for one user, built all the way; pitch the vision verbally. [Playing to Win, p.110-111]
- **Silent stuck.** Tell: a slice is "almost done" across two check-ins. Fix: after 30 minutes stuck (counterintuitive: not the usual 60-90), say it aloud, then swap approach, swap person, or mock it. [Shape Up, p.127-137] [Seed: 0. Synthesis / Playbook, §11]
- **Spike promoted to product.** Tell: a 30-minute experiment with hardcoded keys and no error handling sits on the demo path. Fix: rewrite it as tracer code or log it as a deliberate fake. [Seed: D. Tracer Bullets vs Prototypes, §D]
- **Mid-build restart.** Tell: "let's restart cleanly" at H12-16. Fix: refactor one module for 30-60 minutes, only after two failed patches; never restart the app. [Martin, Clean Architecture, p.39]
- **Order-taking.** Tell: every mentor or sponsor suggestion becomes a ticket. Fix: log it as "maybe some day"; one voice is a hypothesis until 2 more people repeat it. [Escaping the Build Trap, p.46-47] [Talking to Humans, p.90]
- **Sponsor fork.** Tell: a separate feature per sponsor track. Fix: the smallest compliant slice inside the core loop; if the sponsor API could be deleted without changing the demo, drop that track. [Escaping the Build Trap, p.27, 33-34]
- **Willpower plan.** Tell: "we'll push through overnight" replaces a cut. Fix: re-plan scope at the overnight low; between midnight and 6am put a 5-minute timer on every scope debate and let the scope owner decide. [Good Strategy Bad Strategy, p.61-63] [Thinking, Fast and Slow, p.42-43]

## Hackathon calibration
- **Shrink every time unit.** Shape Up's days of orientation become 1-2 hours with something clickable by H4-6; Getting Real's 6-10 hour chunks become 1-2 hour tasks. [Shape Up, p.100-101] [Getting Real, p.63]
- **Invert Cagan's slip rule.** He extends the schedule to protect a validated core. You cannot, so you cut earlier. [Inspired, p.138]
- **Skip scoring frameworks as deciders.** RICE needs real reach data and is unreliable below ~1,000 users; use ICE only to expose where teammates disagree, then decide in plain units (hours, chance of finishing by H14). [Seed: D. Prioritization frameworks, §D1-D2] [How to Measure Anything, p.58-59]
- **Count in people, not significance.** "Six clean users in a row" becomes 3-6 testers total, about 3 per round near H6, H12, H18; kill triggers read "3 of 4 testers". A/B tests are only "what we'd measure next". [Inspired, p.153] [Escaping the Build Trap, p.142]
- **Budget 10-12 real build hours per person,** not 24, before any multiplier. [Brooks, Mythical Man-Month, p.107, p.109, p.113]
- **Pivot windows close fast.** A full problem pivot survives until about H8; after the midpoint only a zoom-in pivot (the part testers liked becomes the whole demo) that reuses the working pipeline is realistic. [Lean Startup, p.138-139, 145]
- **Ries's low-quality MVP does not apply to the path.** UI/UX is scored, so the demo path and first screen look finished while off-path screens stay hidden. [Make, p.73-75] [User Story Mapping, p.81-82]
- **Say scale, do not build it.** Queues, replicas, Kubernetes, and admin panels get a 20-second verbal answer; SQLite or JSON files are fine. [Xu, System Design Interview, p.30, p.32]

## Go deeper
- [../domains/09-product-strategy-prioritization.md](../domains/09-product-strategy-prioritization.md): cut line, admission checks, checkpoint triggers
- [../domains/14-rapid-prototyping.md](../domains/14-rapid-prototyping.md): Real/Fake/Cut, skeleton gate, real-vs-fake ledger
- [../domains/13-architecture-tradeoffs.md](../domains/13-architecture-tradeoffs.md): integration count, innovation tokens, precompute
- [../domains/08-decisions-uncertainty.md](../domains/08-decisions-uncertainty.md): reliability math, decision record, kill criteria
- search_experts("scope hammering decide when to stop", domain="09-product-strategy-prioritization")
- search_experts("less software restate the problem cheaper version", domain="14-rapid-prototyping")
- search_experts("minimal product stop cutting validated core", domain="09-product-strategy-prioritization")
- search_experts("uphill downhill hill chart unknowns")
- search_experts("compounding error multi-step agent reliability", domain="08-decisions-uncertainty")
- search_experts("third-party API fallback recorded response", domain="14-rapid-prototyping")
