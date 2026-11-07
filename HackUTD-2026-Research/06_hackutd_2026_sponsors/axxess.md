# Axxess (spelled "Axxess" on HackUTD site; user wrote "Axess")

Assumption: "Axess" = Axxess, Dallas healthcare-at-home software company. Only sponsor with that name on the HackUTD site. [verified]

## 1. Who they are
Dallas-based "technology innovator for healthcare at home"; software for home health, home care, hospice and palliative providers, said to serve 9,000+ organizations. [verified: axxess.com/hackathon]
Sells: care delivery (Home Health, Home Care, Hospice, Palliative), revenue cycle/billing, Business Intelligence, patient engagement (CAHPS, Connect, Family Portal), connectivity (Axxess Exchange, Physician Portal), workforce (Training, Axxess Care). AI: "Axxess Intelligence" natural-language search over patient data (e.g. high fall-risk patients, patients on anticoagulants) and "Ask Axxess" for billing. [verified: axxess.com]

## 2. HackUTD 2026 prize/challenge
- Listed as **Bronze** sponsor on zeroday.hackutd.co. [verified]
- Challenge text and prizes: **not public**; tracks announced when hacking starts. No Axxess workshop appears in the Nov 7 schedule. [verified]
- Axxess also runs/hosted its own hackathon Feb 21-22, 2026 at UTD ECSW (healthcare innovation, teams up to 4; no hardware provided, "select challenge"). No prizes or challenge text on page. [verified: axxess.com/hackathon]

## 3. Products/APIs for 36 hours
- Developer Platform https://www.axxess.com/developer-platform/ ; Axxess API https://www.axxess.com/axxess-api/ ; usage policy https://www.axxess.com/axxess-api-usage-policy/ [links verified present on homepage; contents NOT read]
- Third-party report (Supergood.ai, a competitor-ish vendor): no self-serve signup, sandbox or keys; only a CEHRT patient-access endpoint is public; broader access via negotiated agreements; ~15-18 interoperability partners. [verified that the page says this; claim itself unverified/third-party]
- Practical: expect to use synthetic data. Useful public resources (general knowledge, unverified here): HL7 FHIR sandboxes (e.g. HAPI FHIR test server), Synthea synthetic patients, CMS OASIS public item sets. Ask Axxess for sample data.

## 4. Prior hackathon sponsorships
- HackUTD past sponsor (Axxess on "Past Sponsors" and 2026 Silver in the redesign page) [verified]; Axxess not in HackUTD 2025 prize list I could see [verified], so their prior prompt: not found.
- Axxess Feb 2026 hackathon winners/prompts: not found in search. [unverified]

## 5. Likely judging (inference)
Evidence is thin: domain is home health/hospice with heavy admin burden, compliance, scheduling, billing, clinical documentation. Expect values: real workflow relevance for clinicians/agency admins, safe/responsible handling of PHI, practicality, AI that saves time. All inference.
Directions (inference):
1. Voice-to-visit-note: caregiver records a visit, LLM drafts structured note with flags for missing OASIS-style fields (synthetic data only).
2. Natural-language agency analytics: "Ask your agency" over synthetic schedule/claims data showing denials or missed-visit risk, with explanations.
3. Caregiver scheduling/route optimizer or family-portal summary generator that turns clinical notes into plain-language updates.

## 6. Questions for the booth
- Challenge statement and rubric? Any sample/synthetic datasets or API sandbox?
- Axxess Intelligence or Exchange access for the weekend?
- Which compliance constraints (HIPAA, no real PHI) should demos respect?
- Who judges (clinical vs engineering)? What did winners of your Feb 2026 hackathon build?

## Sources
- https://zeroday.hackutd.co ; https://hackutd.co [verified]
- https://axxess.com/hackathon ; https://www.axxess.com [verified]
- https://supergood.ai/docs/axxess-api (third-party; page itself says some endpoints are hypothetical) [partially reliable]
