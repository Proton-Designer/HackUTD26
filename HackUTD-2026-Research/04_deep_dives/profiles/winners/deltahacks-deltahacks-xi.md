# DeltaHacks — DeltaHacks XI (3 projects)

### GitAgent
*DeltaHacks DeltaHacks XI · dataset: winners · tier: overall_top3 · evidence A · confidence high*
**Prizes:** Third Place: Digital Camera [3rd]; [MLH] Best Use of GenAI; Build an AI agent with Cohere

**What it is:** Streamlit app where a developer connects a GitHub repository and an agent built on Cohere Command R+ does semantic code search, refactoring, commenting, README and Dockerfile generation, committing changes to a separate branch.
**Problem / user:** Developers and teams burdened by repetitive repository maintenance work.

**Features**
- Semantic search — Finds code responsible for a queried feature using repo contents as RAG documents. *[claimed]*
- Instructed refactor — Rewrites code per instructions for readability or optimization. *[claimed]*
- Auto commenter — Adds comments to code. *[claimed]*
- README generator — Produces an onboarding README adapted to project structure. *[claimed]*
- Dockerfile generator — Creates a Dockerfile for the repo. *[claimed]*
- Branch commits — Writes results to a separate branch via GitHub API for PR review. *[claimed]*
- Merge assistant, CI/CD, GitLab, offline mode — Future work listed. *[planned]*

**Flow:** Open the Streamlit app → Enter GitHub token and repo → Choose a task → Agent reads repo and runs it → Review changes on new branch

**Prompt:** DeltaHacks XI Cohere challenge: build an AI agent that helps people become power users of their tools, judged on creative impactful AI use; MLH Best Use of GenAI asks for generative AI APIs delivering user value.
**Fit (explicit):** Devpost names the Cohere agent prize and a repo-maintenance agent on Command R+ with document RAG.  *(targeted: Build an AI agent with Cohere, [MLH] Best Use of GenAI, Third Place: Digital Camera [3rd])*
**Sponsor tools:** Cohere (Command R+ with RAG documents and Prompt Tuner, core)
**AI:** Cohere Command R+ with RAG over repo tree contents, per-use-case prompts developed with Cohere Prompt Tuner.
**Architecture:** Streamlit UI and FastAPI backend traverse repo via GitHub REST API into RAG documents, call Cohere and commit to a branch.
**Novelty:** Agent writes results to a reviewable branch rather than only chat output.
**Scope:** small · working: Hosted Streamlit demo listed; repo about 670 lines. · polish: Short README; demo video and screenshots on Devpost.
**Claims:** Automates key developer tasks (no figures)
**Gaps:** README does not mention FastAPI backend; Demo site not opened; Screenshot count approximated
Sources: https://devpost.com/software/gitagent, https://github.com/SuperMK15/GitAgent, evidence/deltahacks-deltahacks-xi-gitagent.json, https://deltahacks-xi.devpost.com/

---

### Layoff Evaders
*DeltaHacks DeltaHacks XI · dataset: winners · tier: overall_top3 · evidence A · confidence medium*
**Prizes:** Second Place: YUNZII AL66 Wireless Mechanical Keyboard [2nd]

**What it is:** VR fitness game in Unity where the player is a software engineer fleeing an evil boss and must squat, lunge and jump in real life to dodge office-themed obstacles, with a web dashboard of calories and activity.
**Problem / user:** Software engineers whose sedentary work carries long-sitting health risks.

**Features**
- Exercise-driven movement — VR controller motion tracking detects squats, lunges and jumps that move the character. *[claimed]*
- Office obstacle course — Standup meetings, budget cuts and performance reviews serve as hazards to dodge. *[claimed]*
- Stats dashboard — Streamlit dashboard shows calories burned, jumps completed and active time. *[shown_working]*
- Firebase storage — Realtime Database holds user session data. *[claimed]*
- Personalized chat and settings screens — Appear in screenshot captions without description. *[unclear]*
- Leetcode quick-time events and wearables — Future ideas. *[planned]*

**Flow:** Put on VR headset → Run through office levels → Squat, lunge or jump to dodge obstacles → Stats are written to Firebase → View progress on dashboard

**Prompt:** DeltaHacks XI second place (YUNZII AL66 keyboard); judged on impact, technical strength, originality, presentation.
**Fit (none):** No stated prize targeting; health-themed VR game entered for overall places.  *(targeted: Second Place: YUNZII AL66 Wireless Mechanical Keyboard [2nd])*
**AI:** none
**Architecture:** Unity C# game on Meta VR tracks controller motion, writes stats to Firebase Realtime Database; Streamlit dashboard reads them; separate web folder.
**Novelty:** Pairs humor aimed at tech-worker culture with physical exercise detection in VR.
**Scope:** medium · working: Repo of about 8.7k lines with large Unity game folder; live site layoffs.work and demo video. · polish: Logo, live site, Devpost-style README.
**Claims:** Polished VR experience with accurate motion detection (qualitative)
**Gaps:** README repeats Devpost; mentions React dashboard while Devpost says Streamlit; Individual contributions blank; Live site not opened; Unity project dominates repo file count
Sources: https://devpost.com/software/layoff-evaders, https://github.com/martin226/layoffevaders, evidence/deltahacks-deltahacks-xi-layoff-evaders.json, https://deltahacks-xi.devpost.com/

---

### WhaleBeing
*DeltaHacks DeltaHacks XI · dataset: winners · tier: overall_top3 · evidence A · confidence high*
**Prizes:** First Place: Nintendo Switch + Nord Securities Bundle [1st]; Dyson Innovation Challenge

**What it is:** Web app that shows daily predicted blue whale habitat suitability off California as an animated heatmap, lets users search a ship route and scores that route's chance of crossing high-whale-activity areas.
**Problem / user:** Ship strikes kill up to 20,000 whales per year; operators, conservation groups and policymakers need risk visibility.

**Features**
- Habitat prediction model — Boosted regression tree and GAMM approach from a 2019 paper, translated from R to Python, predicts daily suitability. *[claimed]*
- Animated heatmap — Mapbox map displays the predictions. *[shown_working]*
- Ship route search — SeaRoutes API returns routes drawn over the heatmap. *[shown_working]*
- Route risk score — Sums distribution weights along route nodes to estimate intersection likelihood. *[claimed]*
- Custom routes and other regions — Future expansion starting with Sri Lanka. *[planned]*

**Flow:** Open the site → Search for a ship route → See route over whale-habitat heatmap → Read the risk likelihood

**Prompt:** DeltaHacks XI first place (Nintendo Switch plus Nord bundle); Dyson Innovation Challenge: identify a pressing environmental, societal, technological or personal issue and build a prototype.
**Fit (implied):** Addresses an environmental issue (whale ship strikes) with a prototype risk tool, matching the Dyson issue-and-solution brief; stated as prize on page.  *(targeted: First Place: Nintendo Switch + Nord Securities Bundle [1st], Dyson Innovation Challenge)*
**Sponsor tools:** SeaRoutes API (ship route generation, core); Microsoft Azure (model hosting, supporting); Mapbox (map display, core)
**AI:** Statistical ML (boosted regression tree plus GAMM candidates) trained on satellite blue whale tracking data; no LLM.
**Architecture:** Flask Python model backend and Next.js/React frontend with Mapbox; SeaRoutes provides routes; risk computed over route nodes.
**Novelty:** Applies a published ecological model to a live routing-risk visualization.
**Scope:** small · working: Live site whalebeing.co, demo video; repo about 1.5k lines plus large public data. · polish: Deployed site and CI; README short.
**Claims:** Up to 20,000 whales killed per year by ships (cited) | Could potentially save thousands of whales
**Gaps:** Model accuracy not reported; README lists prerequisites only; Live site not opened
Sources: https://devpost.com/software/whalebeing-27sj0w, https://github.com/lucasliao0403/WhaleBeing, evidence/deltahacks-deltahacks-xi-whalebeing.json, https://deltahacks-xi.devpost.com/

---

