# Hack Western — Hack Western 11 (1 projects)

### BravoDispatch
*Hack Western Hack Western 11 · dataset: winners · tier: overall_top3 · evidence B · confidence medium*
**Prizes:** First place (overall winner) [1st]

**What it is:** A computer-aided dispatch application for emergency call operators. An AI assistant reads the live caller transcript, pulls out key details and keeps a list of active cases so the operator types less.
**Problem / user:** Emergency dispatch operators who must enter details by hand under stress; inspired by a 2018 Cincinnati case where a failed dispatch involving human and computer errors led to a teen's death.

**Features**
- Live transcript analysis — Caller transcript goes to a Cloudflare Worker running Llama 3 that extracts critical call details automatically. *[claimed]*
- Active case management — Operators see and manage a set of currently open emergency cases, stored in Supabase. *[claimed]*
- Live transcription module — Converts the call audio to text feeding the extraction step; more languages and robustness listed as future work. *[claimed]*
- Address verification and recommended actions — Listed as future outlook: verify addresses and suggest actions per call category. *[planned]*
- DeX integration — Named in future outlook without explanation. *[planned]*

**Flow:** Operator opens the home page of the dispatch app → A call comes in and is transcribed live → Bravo AI extracts key details from the transcript → Case appears among active cases for the operator to manage

**Prompt:** Hack Western 12 lists a Cloudflare MLH prize for AI applications built with Cloudflare services such as Workers AI; Hack Western 11 wording not fetched. Overall first place has no theme text.
**Fit (implied):** Uses a Cloudflare Worker with Llama 3 for transcript extraction, matching the Cloudflare AI prize wording seen for the next edition.  *(targeted: First place (overall winner), Best AI Application Built with Cloudflare)*
**Sponsor tools:** Cloudflare Workers (Llama 3) (Extracting key call information from transcripts, core)
**AI:** Llama 3 on a Cloudflare Worker extracts structured details from caller transcripts, plus a live transcription step.
**Architecture:** Next.js/React app with Supabase data store; transcript text sent to a Cloudflare Worker that calls Llama 3; an architecture diagram exists on the project page.
**Novelty:** Targets a safety-critical public-service workflow with a real-world motivating incident; dispatcher-facing AI assistant rather than a caller-facing bot.
**Scope:** small · working: Reported demo video and screenshot; built in 36 hours per project text; no repo content inspected. · polish: Home page screenshot and architecture diagram only.
**Claims:** Reduces manual data entry for dispatchers | Built in 36 hours
**Gaps:** No Devpost link in queue; devpost.com/software/bravodispatch fetch failed; Repo found by search; matched by name and Hack Western 11 mention only; no evidence file; Hack Western 11 prize text not fetched; Best AI Application Built with Cloudflare mentioned as a second prize in mirrored text
Sources: https://www.ivey.uwo.ca/scotiabank-digital-banking-lab/news/2024/11/hack-western-11-where-ideas-took-flight/, https://raw.githubusercontent.com/marmanios/bravo-dispatch/HEAD/README.md (also a text mirror of the project page), https://hack-western-12.devpost.com/ (next edition prizes only)

---

