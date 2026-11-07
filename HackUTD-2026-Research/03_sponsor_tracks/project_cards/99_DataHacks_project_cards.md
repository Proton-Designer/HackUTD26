# DataHacks: project cards (1 projects)

Facts and short paraphrases only; no cross-project analysis. Full records are in the workbook and JSONL.

## DataHacks 2026

### TIDAL WAVE  (DataHacks 2026)

- **Prizes:** Challenge: Best Use of Nvidia Brev [unknown]  (tier: sponsor_winner)
- **Pitch:** Policy-simulation tool: type an environmental policy in plain language, an LLM turns it into parameters, and species agents simulate a coastal ecosystem over years.
- **Problem / user:** Ecological analytics look backward and exclude non-experts; users cannot test how policy ideas would change an ecosystem. / non-expert policymakers and ecological analysts
- **Domain / idea type:** sustainability_climate + ai_agents_infra / data_or_analytics
- **Platforms / hardware / AI:** web / False / llm_chat; agent_or_tool_use; predictive_ml
- **Stack:** langs Python; frontend React; Vite; Tailwind CSS; backend Python; db ; hosting AWS EC2; ECS; ECR; S3; Docker
- **Tech/APIs:** NVIDIA Brev (cloud, unclear, sponsor); Groq API (ai_model, core); AWS (EC2/ECR/ECS/S3) (cloud, supporting); CalCOFI ocean data (data_source, core); React (framework, supporting)
- **Sponsor APIs:** NVIDIA Brev | fit: Entered the Best Use of NVIDIA Brev challenge and lists Brev in Built With, but the writeup text never describes what Brev was used for (the described LLM was Groq and compute was AWS).
- **Repo:** public, commits 24 (before/in/after event: 0/22/2), README detailed
- **Demo/writeup:** video True, live none, screenshots 7, writeup medium, impact claims False
- **Notes:** Seven species each run as an AI agent atop Lotka-Volterra dynamics; Groq parameters were backtested against CalCOFI ocean data distributions; AWS EC2/ECS deployment only partly done.
- **Team size:** 3 | **Confidence:** high | unverified: ui_polish; sponsor_fit_note depth
- **Links:** [Devpost](https://devpost.com/software/tidal-wave-ump7f9) | [GitHub](https://github.com/davdwan21/TIDAL-WAVE)
