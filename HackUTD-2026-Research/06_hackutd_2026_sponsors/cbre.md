# CBRE - HackUTD 2026 brief
(V = verified from a fetched page; U = unverified/inferred)

## 1. Who they are
Largest commercial real estate services and investment firm [U: general knowledge]. Currently AI-heavy: CBRE ran "Innovate 2026", a 48-hour global AI hackathon, 1,400+ employees, 300+ teams, 20+ countries; projects: extract insights from complex datasets, digital assistants to cut manual work, connected client experiences. [V, cbre.com/blogs/thrive-inside-innovate-2026]. Data Intelligence team tracks quarterly market movements [V].

## 2. HackUTD 2026 challenge/prize
- Silver sponsor [V, zeroday.hackutd.co]. No CBRE workshop listed in the Day-1 schedule I saw [V partial].
- Challenge text: **not public** (announced at start of hacking) [V]. Prizes: not public.

## 3. Products/APIs
No public CBRE API/SDK/credits found [U absence]. Past challenges shipped a PDF challenge statement and sample/quarterly data; one 2025 team generated synthetic data from CBRE quarterly data and PDF reports [V, devpost IKARIS summary]. Common stacks teams used: FastAPI/Flask, CrewAI/LangChain/Chroma, MongoDB Atlas, Next.js/React, Nemotron or Llama via Ollama [V from project pages]. NVIDIA is a 2026 Silver sponsor [V], so Nemotron/NIM tooling may be offered [U].

## 4. Prior hackathons (brief; team has own data)
- HackUTD IX 2022: prototype AI/ML to improve customer experience from social media, contact centers, surveys. Prizes $125/$75/$50 Amazon gift cards. Winners: CustomAssure, Scrutiny. [V]
- HackUTD 2024: CBRE Challenge; EcoManage (building energy dashboard, 7-day linear-regression forecast, EcoScore, recommendations) by Dyne Labs [V, dyne-ecomanage.netlify.app].
- HackUTD 2025: challenge "Lost in the Pages" (chatbot over contracts/reports) [V via IKARIS devpost]. Overall winner Cura: CRE intelligence platform, CrewAI agents, Llama 3.1 local, MongoDB Atlas, Next.js; README says built for the CBRE Challenge [V, github.com/armaanamatya/HackUTD2025]. IKARIS: RAG chatbot with confidence level and inline sources, Nemotron [V]. Inconsistency: Cura "won HackUTD 2025" per its README (self-reported) [unverified].
- New for 2026: CBRE's own judging rubric at Innovate 2026 (business impact, technical innovation, scalability, market readiness, execution) [V].

## 5. Likely values + ideas (INFERENCE)
Evidence: Innovate 2026 rubric; 2025 winners combined agentic AI + CRE data + clear sourcing.
Ideas:
1. Lease/contract Q&A agent with citations, confidence and extraction to structured tables.
2. Building energy/ESG copilot (EcoManage-style) with forecast plus action recommendations for data centers/office portfolios.
3. Market-movement briefing agent turning quarterly CRE data into a client-ready narrative with charts.

## 6. Questions for the booth
- Challenge statement and datasets: real, redacted or synthetic? Allowed to publish?
- Do they want agents/RAG specifically, or any approach? Is business-impact framing scored?
- Any model/API credits (NVIDIA, cloud) provided? Judges' backgrounds?

## Sources
- https://zeroday.hackutd.co [V]
- https://www.cbre.com/blogs/thrive-inside-innovate-2026 [V]
- https://cs.utdallas.edu/?p=26350 ; https://hackutd-ix.devpost.com/ [V]
- https://devpost.com/software/ikaris [V]
- https://github.com/armaanamatya/HackUTD2025 [V; README text only]
- https://dyne-ecomanage.netlify.app/ [V; self-promotional claims unverified]
