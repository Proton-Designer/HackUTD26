# DataHacks — DataHacks 2026 (1 projects)

### TIDAL WAVE
*DataHacks DataHacks 2026 · dataset: sponsor · tier: sponsor_winner · evidence A · confidence medium*
**Prizes:** Challenge: Best Use of Nvidia Brev

**What it is:** A web simulator where a user types an environmental policy idea, Groq turns it into six global ecosystem parameters grounded in CalCOFI ocean data, and seven species agents plus population equations play out a Southern California coastal ecosystem year by year.
**Problem / user:** Non-expert users and would-be policymakers who only get retrospective ecological data and cannot test future policy outcomes.

**Features**
- Policy-to-parameter translation — Natural-language policy converted by LLM into six global simulation levers. *[claimed]*
- CalCOFI grounding and backtest — Parameter medians and distributions from CalCOFI data used to check outputs. *[claimed]*
- Species agents — Seven AI agents (e.g. anchovy, sardine, kelp, urchin, sea lion) decide each simulated year. *[claimed]*
- Ecological dynamics — Lotka-Volterra and trophic coupling equations drive populations, limiting hallucination. *[claimed]*
- Web UI with yearly navigation — React/Vite interface to enter policy and step through years of results. *[claimed]*
- Parallel runs on AWS — Compare policies via EC2/ECS; early stage. *[planned]*

**Flow:** Enter a policy idea → Groq maps it to six parameters → Simulation runs year by year → Step through yearly parameters, environment and populations

**Prompt:** Sponsor challenge for projects using NVIDIA Brev GPU cloud; the hackathon overview publishes only the prize ($500, one winner), no detailed brief.
**Fit (implied):** Page lists NVIDIA Brev under built-with and says the team won the Brev challenge; README mentions Ollama locally and Groq, so how Brev is used is not described.  *(targeted: Best Use of Nvidia Brev)*
**Sponsor tools:** NVIDIA Brev (listed as part of the stack; role not described, unclear)
**AI:** Groq-hosted LLM (and local Ollama in README) parses policies; LLM agents per species choose actions; rule-based engine with Lotka-Volterra dynamics.
**Architecture:** React/Vite front end over a Python simulation (policy parser, rule engine, species agents, visualization); AWS Docker deployment partly built.
**Novelty:** Forward-looking policy sandbox mixing LLM agents with grounded ecological equations rather than retrospective dashboards.
**Scope:** medium · working: About 18k lines, Docker, run.py driver and layered simulators; no live link or video. · polish: README explains components; AWS side admitted early stage; repo holds duplicate folders.
**Claims:** Won Data Analytics track and Best Use of Nvidia Brev | Outputs backtested against CalCOFI distributions
**Gaps:** no Brev usage detail; no video
Sources: https://devpost.com/software/tidal-wave-ump7f9, https://github.com/davdwan21/TIDAL-WAVE (evidence README), sponsor_prompts_NVIDIA.jsonl (DataHacks 2026)

---

