# HackUTD 2026 — Track-Day Kit

Use this the moment tracks are announced. It turns the research into decisions. Evidence lives in `outputs/findings.md` (finding numbers in brackets, e.g. [F0.1]); every number traces to `data/tables/` via `data/tables/INDEX.md`. Ratings are analyst judgments, not judge scores. "Association" means a difference between groups, not proof of cause.

Goal: 1st in General + 1st in one sponsor track, plus any side/MLH prize the same build earns.
Prior-work rule: do not pre-write submission code. Safe prep = reading docs, creating accounts and API keys, throwaway practice code that is not submitted.

---

## 0. Before tracks are announced (checklist)

- [ ] Accounts + API keys ready for likely tools (NVIDIA, Auth0-type MLH prizes, cloud/hosting). Keys never committed to the repo.
- [ ] Read `outputs/sponsor_cards.md` once, end to end.
- [ ] Read the 3–5 archetype cards in `outputs/archetypes.md`.
- [ ] At opening, confirm the open questions in §8 below.

---

## 1. The ten rules (from the evidence)

Each rule names its evidence type. "Association" = a difference between groups, not proof of cause; HackUTD 2025 is the only event with a non-winner comparison.

1. **Get one flow fully working; never present an unbuilt feature.** HackUTD 2025 (association): winners more often showed two working flows (8 of 35, 23% vs 0 of 47 strong non-winners); 25 of 35 winners (71%) showed exactly one; zero working flows 1 of 35 (3%) winners vs 9 of 47 (19%) strong non-winners. [F0.1, F3.1]
2. **Nothing visible on Devpost separates 1st from 2nd/3rd.** Fact over 127 track pairs; *why* is not explained by available evidence. Inference: the live demo and judge Q&A may decide it, so rehearse both as seriously as the build. [F2.1]
3. **Treat every rubric dimension as a gate (judgment).** No dimension is a floor among winners; 1sts are rated higher than their track peers slightly more often on technical complexity (54 higher / 37 equal / 36 lower tracks) and presentation (52 / 37 / 38); minimum rating 47 / 46 / 34 (low–medium confidence). [F2.2, F2.3]
4. **Make the hard part visible.** HackUTD 2025 (association): winners showed the centerpiece via diagram/logs 19% vs 6% and in demo output 31% vs 22% of strong non-winners. Across other events, 1sts show it no more often than 2nd/3rd (49% vs 57%). [F0.5, F3.2]
5. **If AI is used, make it multi-step.** HackUTD 2025: agentic 47% of winners vs 28% strong non-winners (association). Single-call wrappers are 9% of general 1sts and slightly more common in 2nd/3rd (14% vs 8%). Agentic (26%) and live data (65%) are common among recent winners — not required (15 of 65 general 1sts use no AI). [F0.2, F3.2, F7.2]
6. **For General, avoid a plain dashboard core.** Data-in/dashboard-out is 4 of 65 general 1sts (6%) and the most common shape among HackUTD 2025 strong non-winners (24 of 50, 48%). [F0.3, F1.1]
7. **Problem-style sponsor tracks: solve the stated problem, literally, for the stated user; sponsor tech is optional.** 22 of 24 HackUTD 2025 company-problem awards used no sponsor product (fact). Sponsor-domain 1sts built exactly what was asked in 15 of 17 (88%) vs 18 of 27 (67%) 2nd/3rd — association; literalness unknown for about half (17 of 34 1sts, 29 of 56 lower). Evidence covers banks, insurance, real estate, energy, telecom, NMC2; health/legal sponsors have no dataset winners. [F4.2, F6.1]
8. **Tool/API prizes: make the sponsor tool non-removable and show it working.** Any-place fact: 117 of 138 API-depth winners (85%) made the tool non-removable; 55% used one feature, 45% two or more. No evidence on which depth places higher. [F4.3]
9. **Cover, images, video and full Devpost sections are typical among winners, not universal.** General 1sts: video 84%, what's-next section 80%, accomplishments 73%, zero images 9%. A clear cover did not separate HackUTD 2025 winners from strong non-winners (83% vs 88% at 3/3). Do them well, then move on. [F0.6, F5.1, F5.2]
10. **Put one cited number about the problem in the pitch.** Cited statistics: 18 of 61 (30%) general 1sts vs 16 of 117 (14%) 2nd/3rd (association, below the 20-point bar); measured evidence is rare everywhere. [F5.4]

---

## 2. Track-announcement procedure (spec §5)

1. **Verify** (§8 below). Paste the official rubric, track list and limits into the team doc.
2. **For each track**, map to sponsor_industry and prize kind:
   - *problem-style* (bank, insurer, real estate, energy, health, law firm, telecom business problem) → use rule 7.
   - *tool/API-depth* (NVIDIA, Spacetime, cloud/AI platforms, MLH tool prizes) → use rule 8.
   - *open/theme* → General logic.
   Read its card in `outputs/sponsor_cards.md` and its row in the matrix (§3).
3. **Generate 3–5 candidates** as (problem, primary sponsor track, secondary track or side/MLH prize), seeded from the archetypes (`outputs/archetypes.md`) and the matrix cells. The general-1st archetypes (n of 65 general 1sts, `Q04_archetype_counts.csv`): A Hardware sense-and-act loop 22 (34%) · B Multimodal human-need pipeline 16 (25%) · C Agent/dev-tool automation 11 (17%) · D Playful new interaction 9 (14%) · E Data-to-decision utility 4 (6%, low n) · unassigned 3 (5%). Seed from B and C first (archetypes.md rates their HackUTD fit medium-to-strong and strong). Use A only if the team already has a working hardware loop: 0 of 6 HackUTD general winners were hardware, and 15 of 22 A examples come from 36–48h events (HackUTD is 24h).
4. **Gates** — fail any = fix or drop:
   - Eligible under the rules (track limits, prior-work rule).
   - The demo action and the visible result can be said in one sentence ("Judge pastes their own document → the agent files the three actions and shows the trace"; or "Judge says X into the mic → the device does Y").
   - The team can name a credible path to a working core flow within the event.
5. **Score survivors** with the sheet in §4. Never let a high total hide a 1 or 2 in any row.
6. **Commit to one.** Then: initial Devpost entry by its deadline → build core flow 1 → freeze features once flow 1 is demo-stable → (optional) flow 2 → test → record the ≤2-min demo-only video → finish Devpost → rehearse the station pitch and the likely questions (§6) → submit.
7. **Station prep:** a cover screen that passes the cover test (§5), seeded demo data, a one-click reset, the backup video loaded locally.

---

## 3. Pattern × sponsor-industry lookup (Q11)

What past sponsor-prize winners in each 2026 industry built (all events; counts are projects; source `data/tables/Q11_pattern_x_industry.csv`, full examples there). Sponsor tracks frequently reward data-to-decision; General does not (rule 6) — so for a General + sponsor double, add an action/interaction on top of the insight.

| industry (2026 sponsors) | top winning patterns (n projects) | examples |
|---|---|---|
| finance_banking (Capital One, PNC, Goldman Sachs, Toyota FS) N=85 | data_to_decision 36 · workflow_automation_agent 10 · docs_to_action 7 · education_feedback 6 | AutoPM, CFO-Sabbatical, AutoBoard, Lapse |
| insurance (State Farm) N=14 | education_feedback 5 · devtool 3 · game_or_social 2 · sensor_to_alert 2 | MirrorAPI, UpGuardian, Halo |
| telecom (T-Mobile, AT&T) N=12 | data_to_decision 6 · risk_detect_and_respond 2 | Beacon, HarmoniQ, CareLens |
| real_estate (CBRE) N=17 | data_to_decision 7 · docs_to_action 5 · sensor_to_alert 2 | Aero, Meet+, Eco Fast Track |
| energy (EOG) N=9 | data_to_decision 4 · risk_detect_and_respond 3 | DHy-n0, PipeBrAIns |
| ai_compute (NVIDIA, NMC2, 8090 AI) N=123 | workflow_automation_agent 31 · risk_detect_and_respond 14 · vision_to_assist 12 · data_to_decision 10 | ANNEAL, Argus, Embers |
| health (Axxess) N=17 | docs_to_action 5 · voice_to_action 3 · risk_detect_and_respond 2 | ClearPath, CuraVox, Asclepius |
| cloud_devtools (Spacetime, NMC2) N=102 | workflow_automation_agent 18 · data_to_decision 17 · devtool 12 | Aether, Cinder Control, Atlas |
| auto_mobility (Toyota FS) N=21 | data_to_decision 8 · education_feedback 3 · voice_to_action 3 | DreamDrive, Aria kiosk |
| other (incl. Photon) N=106 | data_to_decision 19 · game_or_social 13 · sensor_to_alert 12 · workflow_automation_agent 9 | Photon card: 17 winners, messaging layer core in 13 of 17 (76%) |
| geospatial_ar (Niantic Spatial), legal (Winstead PC), health (Axxess), 8090 AI, AT&T | no dataset winners for these sponsors — brief-only cards | — |

Capital One is mostly problem-style, but 9 of its 42 dataset awards are API-depth prizes (see its card).

Of the 100 sampled HackUTD 2025 non-winners, none targeted State Farm or Goldman Sachs, yet each awarded 3 prizes [F6.2]. This is a sample, not all entries: ask organizers or watch the room for which tracks look crowded. When two tracks fit equally, prefer the business-problem track fewer teams seem to pick.

---

## 4. Candidate scoring sheet (spec §5)

Score each surviving candidate 1–5 per row. Total = Σ(score × weight) / 5 (max 100). Discussion tool, not an oracle. Any 1 or 2 = fix or drop, whatever the total.

| criterion | weight | 5 looks like | 1 looks like | cand A | cand B | cand C |
|---|---|---|---|---|---|---|
| General-track strength (archetype fit, not a plain dashboard/chat) | 25 | matches an archetype; visible non-trivial centerpiece | dashboard over public data / single prompt wrapper | | | |
| Demo memorability (one wow moment, shown live) | 20 | judge sees the system act on the real world or their own input | slides + a chart | | | |
| Sponsor fit (literal to prompt; tool non-removable for API tracks) | 15 | builds exactly what the challenge asked, for its named user | loose theme match | | | |
| Feasibility for 4 people (one flow fully working) | 15 | core flow path is clear and uses known tools | depends on an unknown API or hardware we lack | | | |
| Problem/user value (named user + one cited number) | 10 | specific user role + cited statistic | "everyone" + asserted impact | | | |
| Distinctiveness vs look-alikes | 10 | combination or new interaction | the common AI idea of the year | | | |
| Extra prize fit (MLH/side prize already used by the build) | 5 | the build already needs the tool | tool added only for the prize | | | |
| **Total** | 100 | | | | | |

---

## 5. Minimum winning build, avoid list, templates

### 5a. Minimum winning build [F0.1, F3.1, F3.2]
- One end-to-end user flow working on real (or clearly seeded) data. Optional second connected flow only after the first is demo-stable.
- External services: the typical general 1st uses 0–4 (50 of 61, 82%); more is fine if each one works at the table (HackUTD 2025 winners used 5–7 more often than strong non-winners).
- One non-trivial technical centerpiece (multi-input/multi-step pipeline, agent with tool calls, custom model, or hardware) that the demo visibly exercises.
- Say plainly what is simulated or mocked.
- No endpoint the demo touches may be missing or static (judgment; in the single calibration case — `outputs/close_reads/calibration_tmobile_2025.md`, analyst ratings, n = 3 — static JSON and a missing endpoint were the largest gaps).

### 5b. Avoid list — low-confidence signal (gaps 3–6 points overall) [F7.1, F0.3]
Reject quickly for General unless the track asks for it or the sponsor has rewarded it (State Farm: education_feedback is its most common past-winner pattern).
- Study/quiz feedback app (education_feedback: 3% of general 1sts vs 14% of general 2nd/3rd).
- One-prompt GPT wrapper (single_call_wrapper).
- Dashboard over a public dataset as the whole product (data_to_decision) for General.
- "New dataset" as the only novelty.
- Any feature in the pitch that is not working.

### 5c. Common now vs still distinctive [F7.2, F1.2]
- Common among recent winners (not required): live data (65%), agentic AI (26%), a video, images, full Devpost sections.
- Still distinctive: physical/hardware interaction, a visible centerpiece, a second working flow, a cited number.

### 5d. Cover test (station screen + Devpost title/tagline) [F5.1]
- Title + tagline must answer *who it is for* and *what it does* in one line: "**<Name>** — <what it does> for <specific user>".
- Good (real 1st-place covers scoring 3/3): "FaceTimeOS: AI Mac Agent — FaceTime to talk, see, and control your Macbook with AI Agents" · "PrezPal — A voice controlled custom slides editor, powered by generative AI" (`Q15_cover_examples_1sts.csv`).
- Bad (real 1st-place covers that scored low): "Redefining mobile computing." · "Connect color to a sound" · "."
- Test it on a stranger (another team): can they say what it does after reading only the cover? If not, rewrite.
- First gallery image = the product working (screenshot or photo), not a logo.

### 5e. Station pitch skeleton (expo format: a short demo/pitch then questions, repeated for each judge group; confirm the per-visit format at opening) [structure = inference; live pitches are not in the data]
1. One line: user + problem + one cited number.
2. Show the working result early (the wow moment) — before architecture or slides. [inference; video openings were not measured]
3. Walk the core flow end to end on seeded data; narrate what the system is doing.
4. Show the centerpiece: open the logs/agent trace/architecture view next to the result.
5. Say what is real vs simulated, and what is next.
6. Sponsor sentence: "For <sponsor>, this solves <their stated problem> for <their named user>."
7. Invite questions. Keep the one-click reset ready for the next group.

### 5f. Demo video (≤ 2 min, demo-only) [F5.2, F5.3]
- Open on the working result, not a title card or problem slide. [inference; Q16 openings not measured]
- Show the core flow live; one wow moment; centerpiece visible on screen.
- Record from the frozen build; keep a local copy at the station as backup.

### 5g. Devpost page template [F5.2]
- Title + tagline (cover test).
- Video embedded.
- Several images (judgment: ≥ 4; 38 of 58 general 1sts, 66%, had 4+): product working first; one architecture/flow diagram; one with the hardware or real-world setup if any.
- Sections: Inspiration (one cited number) · What it does (named user, the flow) · How we built it (the centerpiece) · Challenges · Accomplishments · What we learned · What's next.
- Built-with tags list every sponsor/MLH tool actually used (and only those).
- Name the sponsor challenge answered in plain words.

---

## 6. Predicted judge questions and answer angles (inference; live Q&A is not observed)

From the technical-centerpiece catalog (`Q06_general_1st_centerpieces.csv`), the single calibration case (close read) and HackUTD close reads. Prepare a short, honest answer for each; demonstrate when possible.

| question | why they ask | answer angle |
|---|---|---|
| "What part did you build vs call an API for?" | separates wrappers from engineering | Point at the centerpiece on screen; name the steps you wrote. |
| "Is this live or hardcoded?" | in the one calibration case, static data was the largest gap (n = 3) | Show the data source/endpoint live; say exactly what is seeded or simulated. |
| "What happens if the model is wrong / the sensor fails?" | robustness, completeness | Show the fallback or validation step; if none, say what you would add. |
| "Who is the user and how do you know it is a problem?" | impact | Named user role + the cited number; any test or quote gathered during the event. |
| "How does this use <sponsor>'s product / answer <sponsor>'s challenge?" | sponsor judges | Problem-style: restate their challenge and show the matching output. Tool-style: show the one feature that is core and what breaks without it. |
| "How is this different from <well-known product>?" | innovation | The combination or new interaction in one sentence. |
| "What would you do next?" | completeness, vision | Next concrete feature + what you would measure. |
| "How did you split the work?" | team, credibility | One sentence per person, tied to a visible part. |

---

## 7. Sponsor quick reference

One card per 2026 sponsor in `outputs/sponsor_cards.md` (past winners, patterns, literalness, integration depth, pitch angle). Rules of thumb:
- **Banks / insurance / real estate / energy / telecom / NMC2 (problem-style):** literal solution to the stated problem for the stated user; sponsor tech optional [F4.2, F6.1]. NMC2 dataset winners used no NMC tech (6 of 6 removable) — treat as a datacenter/AI-ops problem track; confirm at the workshop. Capital One also has API-depth prizes.
- **Health (Axxess) / legal (Winstead PC):** no dataset winners — brief-only; read the challenge literally.
- **NVIDIA / Spacetime / Photon and MLH tool prizes (tool-style):** sponsor tool non-removable and shown working [F4.3]. Spacetime past winners all used SpacetimeDB as the core backend (spec §0.2); Photon's messaging layer was core in 13 of 17 winners.
- **8090 AI, AT&T:** no dataset evidence; ask at the booth what the challenge rewards.
- **T-Mobile:** 2025 winners were sentiment dashboards. Calibration (n = 3, analyst ratings, placement team-reported): the largest gaps for the 3rd-place project were technical complexity (−2) and completeness (−1.5); innovation −0.5 (close read; anecdote, not a finding).
- **Stacking:** General + sponsor happens in a minority (10 of 65 general 1sts, 15%); pick the sponsor whose problem fits the General idea, then add one MLH/side prize the build already uses [F4.1].

---

## 8. Confirm at opening (spec §6)

- Can one project win General and sponsor prizes together?
- Are MLH/side prizes again outside the 2-sponsor-track limit?
- What do NMC2, 8090 AI, Spacetime and Photon challenges actually ask?
- Prior-work and boilerplate rules; must the repo be public?
- Number of judge groups per station; how finalists/winners are chosen (second round?).
- Exact per-visit timing in each room.
- Rubric unchanged from 2024/2025 (Innovation & Creativity, Technical Complexity, Completeness, Design, Impact, Presentation)?

Event facts (spec §0.1): 24-hour in-person event; every project is in General; up to 2 sponsor tracks plus unlimited side tracks; expo judging at the team's station; demo-only video ≤ 2 min; initial Devpost submission and final submission deadlines per the official schedule.
