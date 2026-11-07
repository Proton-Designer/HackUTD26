---
name: 15-ai-app-design-eval
description: Open when deciding whether and how a HackUTD project should use an LLM or ML model (hour 0-2 idea check, picking chain vs router vs agent, RAG or not), when building the Saturday eval set and judge, when hardening the demo path against wrong, slow, or injected outputs, or when preparing the "wrapper / how do you know it works / what if it's wrong" answers.
---
# AI application design and evaluation

## Use this when
- Hour 0-2: an idea "uses AI" and you must prove the AI does a job rules or plain UI cannot, and name what the team owns beyond the model call.
- Hour 2-6: choosing the architecture (single call, chain, router, agent, RAG, text-to-SQL) and the model.
- Saturday morning to midday: writing the 20-50 case eval set, picking checkers, and running error analysis.
- Hours 14-22: someone wants to tweak the prompt, swap the model, or add an agent step, and you need a go/no-go rule.
- Final rehearsal: judges will type off-script inputs; you need out-of-scope handling, guardrails, and a pitch number you can defend.

## Core principles
1. **Own something the model does not: data, workflow, interface, or eval results.** Everyone calls the same models, so the prompt is not a moat (assume it leaks) and a chat box is a wrapper; value moves to the complements around cheap prediction. [Seed: 0. Synthesis / Playbook, §0.2]; [Huyen, AI Engineering, p.465-467]; [Agrawal, Prediction Machines, p.22]
2. **Use the simplest pattern that works; agents lose demos (counterintuitive).** At 95% per-step accuracy, 10 steps succeed end to end about 60% of the time; one 2025 analysis found 40-80% of multi-agent tasks failing on coordination or verification. [Huyen, AI Engineering, p.539]; [Lakshmanan, Generative AI Design Patterns, p.517-520]
3. **Write the pass criteria before the feature, and prefer tasks with checkable answers.** If you cannot say how a good output differs from a bad one, the feature is not scoped; classification, schema extraction, and runnable SQL let you show a number. Add a close-ended spine to open-ended ideas. [Huyen, AI Engineering, p.316-319, p.63, p.318]
4. **Read your outputs before you pick metrics (counterintuitive).** Generic scores (ROUGE, BLEU, "hallucination score") rarely track your real failures; open-code each failing trace in one line, group and count the notes, fix the top 1-3. Many fixes are trivial, like injecting today's date. [Seed: C. Evals and Error Analysis, §C]; [Huyen, AI Engineering, p.259-264]
5. **Code assertions first, a binary LLM judge only for fuzzy criteria, validated against your own labels.** Binary pass/fail is the biggest single judge improvement; judges are lenient (scores cluster near 0.9), favor their own family by up to +25%, favor the first option and longer answers. Use a different model family, temperature 0, frozen prompt, and check against 20+ hand labels. [Seed: D. LLM-as-a-Judge, §D]; [Huyen, AI Engineering, p.281, p.289-290]; [Lakshmanan, Generative AI Design Patterns, p.424-426]
6. **Small evals only detect big differences.** For 95% confidence, a 30-point gap needs about 10 cases, a 10-point gap about 100, a 3-point gap about 1,000. With 30-50 cases, trust only 10+ point jumps and call results preliminary. [Huyen, AI Engineering, p.405-407]
7. **A number means nothing without a trivial baseline.** Report next to zero-rule (majority class), a simple heuristic, and the existing manual workflow; on imbalanced tasks show a confusion matrix, because 94.5% accuracy coexisted with 42% precision and 30% recall in a fraud example. [Huyen, Designing ML Systems, p.201-205]; [Lakshmanan, ML Design Patterns, p.157-159, p.401-406]
8. **Never ship free-form text into code.** Few-shot makes the format likely, not guaranteed; use schema or JSON mode, validate, and retry up to 2 times with the parser error appended. Two retries on a >90% call push failure below 1%. [Alammar, Hands-On LLMs, p.257, p.270-273]; [Lakshmanan, Generative AI Design Patterns, p.438, p.519]
9. **Give the system a way out, then flag its guesses.** Nearest-neighbor search always returns something, and field extraction from documents is only about 90-97% accurate, so 3-10% of numbers can be invented. Allow "unknown" in the schema (float | "Unknown"), add a similarity cutoff and an out-of-scope class, and verify with a checksum (line items sum to the total) or logprobs on the key tokens: in one receipt demo correct rows scored above 0.9, rows with an imputed value 0.55 or lower. [Lakshmanan, Generative AI Design Patterns, p.599-609]; [Alammar, Hands-On LLMs, p.328-329]
10. **Design for being wrong: suggest, show why, route uncertainty to a human.** Complementary, user-requested AI tolerates errors; critical or proactive AI needs a much higher bar. Confirm in proportion to uncertainty times impact; referring the 20% least-certain cases let one medical model beat its referral standard. [Huyen, AI Engineering, p.80-82]; [Christian, The Alignment Problem, p.285-286]; [Seed: F. Guidelines for Human-AI Interaction, §F]
11. **Treat every retrieved or tool-returned string as an attacker.** Indirect injection through docs, emails, and usernames is the real threat, and permissive agent defaults saw 100% injection success in one study. Limit impact by architecture: read-only tools, human approval for writes, sandboxed code. [Huyen, AI Engineering, p.473-477, p.484-489]; [Seed: I. OWASP Top 10 for LLM Applications 2025, §LLM01, §LLM06]
12. **Let code own the facts; the LLM only words them (counterintuitive).** Pull exact fields (price, dosage, dates, totals) from a database or typed object, have the model rephrase, then assert the fields survived. Rewording adds far fewer errors than writing from scratch, and models invent citations and URLs that look right. Where combinations are enumerable, pregenerate and hand-review templates and fill placeholders at runtime: a demo path that cannot hallucinate. [Lakshmanan, Generative AI Design Patterns, p.584-596]; [Brousseau & Sharp, LLMs in Production, p.106-107]

## Decision procedure
Main decision: what the AI does and the smallest architecture that delivers it reliably on stage.

1. **AI justification (hour 0-1).** Write "Given X, predict Y, judged by Z" [Huyen, Designing ML Systems, p.62] and the before/after ("2 hours by hand, 10 seconds with it") [Seed: 0. Synthesis / Playbook, §0.1]. Stop if a lookup table or fixed rule solves it; instead carve out the one sub-step only a model can do [Huyen, Designing ML Systems, p.20-27]. An LLM fits language jobs (generation, Q&A, talk-to-your-data); for forecasting, outlier detection, math, or sub-second features use classic code or a small classifier and let the LLM only explain the computed result [Brousseau & Sharp, LLMs in Production, p.8-9, p.28]; [Raschka, Build an LLM from Scratch, p.23]. Stop if a wrong answer is costly, unreviewed, and the user cannot verify it [Seed: A. Hackathon Kit, §A1].
2. **Set the human role.** Label each step auto, suggest, or human [Agrawal, Prediction Machines, p.107-112]. Default to suggest-with-override. Put a cost on a false alarm and on a miss; pick the threshold from that ratio, not accuracy [Agrawal, Prediction Machines, p.81-83].
3. **Pick the pattern.** Steps known in advance: chain of 2-4 calls with code checks between. A few known input types: temperature-0 router with an enum output. Subtasks unknowable until runtime: orchestrator-workers. Full agent only if failures are cheap, with 3-5 tools, a 5-8 step cap, and a spend cap [Seed: A. Hackathon Kit, §A2]; [Huyen, AI Engineering, p.548-551, p.559]. Multiply per-step success; if the demo path estimate is under 90%, cut steps or precompute.
4. **Pick the knowledge path.** Corpus under about 200K tokens: put it in the prompt with caching, no retriever [Huyen, AI Engineering, p.497-498]. Larger: keyword/BM25 first, add embeddings via reciprocal rank fusion if test queries miss, add a reranker if the right chunk is retrieved but not on top (one benchmark: 36.5 to 62.8 nDCG@10) [Huyen, AI Engineering, p.505-506]; [Alammar, Hands-On LLMs, p.336-341]. Tables: text-to-SQL on a read-only user [Huyen, AI Engineering, p.532-534]. Plain NumPy until millions of vectors [Alammar, Hands-On LLMs, p.333-334]. Gate: write 10-15 queries with the expected passage; wherever it misses the top 3, fix retrieval before touching the answer prompt, since a good generator cannot recover from bad context [Alammar, Hands-On LLMs, p.341-348]; [Huyen, AI Engineering, p.513-518].
5. **Pick the model.** Prove feasibility on the strongest model, then try cheaper ones and keep the cheapest that clears your threshold; 15 of your own inputs per candidate beats leaderboard reading [Huyen, AI Engineering, p.355-357, p.384-392]. Before switching models, decompose the task (one case went from about 20% to 70%). Default to a hosted API; self-hosting needs about 2 GB per billion parameters at half precision (7B is about 14 GB) plus download and load time, so do it only if privacy or offline use is the pitch and it truly runs locally in the demo [Brousseau & Sharp, LLMs in Production, p.13-14, p.99-100]. Decide by hour 6.
6. **Build the eval set (Saturday morning).** 20-50 cases tagged by slice: typical, messy/typo, 5+ off-topic or hostile, 5 false-premise, 5 obscure-entity, and "answer not available" [Huyen, AI Engineering, p.328, p.396-397, p.403-405]. Write the pass threshold down before the first run. One command writes a CSV of input, output, pass/fail, note [Seed: A. Hackathon Kit, §A5].
7. **Iterate with gates.** Keep a prompt change only if it gains 10+ points on the fixed set, or wins pairwise against the old output in both orders [Lakshmanan, Generative AI Design Patterns, p.424-425]. Timebox tuning to about 45 minutes per feature [Alammar, Hands-On LLMs, p.244].
8. **Freeze and rehearse.** Feature freeze by about hour 14 [Huyen, AI Engineering, p.86-87]. Run the demo path 10 times; more than 1 failure means remove a step or cache that result [Lakshmanan, Generative AI Design Patterns, p.519]. No model or prompt changes in the last 6 hours. Final eval run on the demo build gives the pitch number.

## Checklists

**Eval and claims (run before any number goes on a slide)**
- [ ] Stated as "X of Y passed", with the range (34/40 is about 70-93%), the test setup, and "preliminary" if n < 100. [Seed: 0. Synthesis / Playbook, §0.8]
- [ ] Shown beside a zero-rule or heuristic baseline and the manual workflow.
- [ ] Per-slice pass rates; worst slice and top failure type named with its mitigation. Thresholds written down first, and a teammate who did not write the prompt runs and labels it. [Huyen, Designing ML Systems, p.324, p.394]
- [ ] Multi-step pipeline scored per step (retrieve, extract, answer) as well as end to end, so each failure is pinned to a step. [Huyen, AI Engineering, p.393-394]
- [ ] RAG: top-3 hit rate on labeled queries, plus faithfulness (claims supported by context) and citation precision hand-graded yes/no on 10 answers; source index checked for stale or wrong docs, which no metric catches. [Alammar, Hands-On LLMs, p.357-358]; [Seed: H. RAG Evaluation, §H]
- [ ] For guardrails: attack success rate and false refusal rate on 10 + 10 prompts. [Huyen, AI Engineering, p.484, p.486]
- [ ] LLM judge agreement with hand labels reported; judge prompt, model, and test-set version committed. [Christian, The Alignment Problem, p.262-263]
- [ ] Labels described as what they measure ("accurate against our two-person consensus"). [Christian, The Alignment Problem, p.313]
- [ ] Result too good? Check leakage: correlated rows split by user/date, test set never used for tuning. [Lakshmanan, ML Design Patterns, p.329-331]

**Demo path reliability and safety**
- [ ] Every model output validated against a schema; retry with error, then a fallback.
- [ ] Temperature 0 and pinned model version on the demo path (providers change models behind one name; one GPT-3.5 update dropped 10%); exact demo inputs pre-cached. [Alammar, Hands-On LLMs, p.240-243]; [Huyen, AI Engineering, p.871-874, p.889-890]
- [ ] Timeout on every model call that falls back to a heuristic or cached answer instead of a spinner. [Huyen, Designing ML Systems, p.382-383]
- [ ] LLM classifiers answer with single, distinct-first-token labels (A/B/C, Yes/No); options sharing a first token pool probability and flip the pick. [Ziegler, Prompt Engineering for LLMs, p.155-156]
- [ ] Each LLM step is an injectable function with a mock, reused as the offline fallback. [Lakshmanan, Generative AI Design Patterns, p.445-448]
- [ ] Untrusted text wrapped and labeled as data; model output escaped before HTML, SQL, or shell.
- [ ] Write actions need a confirm click; agent has a visible stop, step cap, and spend cap. [Christian, The Alignment Problem, p.293-294]
- [ ] Keys server-side, per-user rate limit and max tokens, no secrets in the system prompt. [Seed: A. Hackathon Kit, §A10]
- [ ] 10 irrelevant inputs tried live; each declines gracefully.
- [ ] One JSONL line per call: prompt version, input, output, latency, tokens, cost, request ID. [Huyen, AI Engineering, p.881-887]

**Trust UX**
- [ ] First screen says what it does and how reliable it is; no overpromising. [Seed: F. Guidelines for Human-AI Interaction, §F]
- [ ] Citations or highlighted evidence the user can click through.
- [ ] One click to accept, edit, regenerate, or dismiss; edits logged as (ai_output, user_final). [Lakshmanan, Generative AI Design Patterns, p.629-632]
- [ ] Low-confidence fields flagged individually ("needs review", or "likely/possible" categories rather than raw percentages), not a blanket disclaimer. [Lakshmanan, Generative AI Design Patterns, p.643]; [Seed: G. People + AI Guidebook, §G]
- [ ] If users cannot check the output themselves (code for non-programmers), render 2-3 candidates as previews they can judge; if they can edit fast, one draft is fine. [Huyen, Designing ML Systems, p.381-382]
- [ ] Streaming or staged progress for anything over about 1 second.

## Anti-patterns
1. **The wrapper.** Tell: the deliverable is a chat window; the pitch says "ChatGPT for X". Fix: embed the AI in the task screen, close the loop with an action, and name the data or workflow you own.
2. **A team of agents.** Tell: the diagram has four named agents or a multi-agent framework appears mid-build. Fix: plain code with awaits, one router, `asyncio.gather` for independent calls; parallelism is the only multi-agent use that reliably pays. [Lakshmanan, Generative AI Design Patterns, p.505-506]
3. **Ranking versions by absolute judge score.** Tell: "v2 scored 0.90, v1 scored 0.89." Fix: pairwise against the baseline in both orders; one example gave 0.89 vs 0.90 alone but a clear 0.63 gain relative to the original. [Lakshmanan, Generative AI Design Patterns, p.424-425]
4. **Vibe-check iteration.** Tell: "I tweaked the prompt, it seems better." Fix: prompts in versioned files, a fixed set rerun by script after every change. [Huyen, AI Engineering, p.453, p.458-461]
5. **Retrieval that never says no.** Tell: off-topic judge questions get confident answers built from loosely related chunks. Fix: distance cutoff calibrated on 5 in-scope and 5 out-of-scope queries; top-k of 2-3, since models treat every supplied snippet as relevant. [Alammar, Hands-On LLMs, p.328-329]; [Ziegler, Prompt Engineering for LLMs, p.123-124]
6. **Raw confidence as probability.** Tell: a "97% confident" badge with no calibration. Fix: show categories or a review flag; softmax confidence is unreliable on novel inputs. [Christian, The Alignment Problem, p.275-277]
7. **Unfair comparisons.** Tell: model A with a tuned prompt vs model B with a default one. Fix: identical template and examples; prompting alone moved one MMLU score from 83.7% to 90.04%. [Huyen, AI Engineering, p.108-109]
8. **Late model swap.** Tell: a sponsor model or "the new version" goes in at hour 20. Fix: rerun the fixed set on both; swap only if it wins; keep the known-good tagged and deployable. [Lakshmanan, ML Design Patterns, p.290-292, p.388-397]
9. **Live multi-call loops on stage.** Tell: judges wait through reflection, self-consistency, or an inline judge. Fix: reflect once at most on chat paths, precompute the showcase flow; note that output guardrails conflict with streaming. [Lakshmanan, Generative AI Design Patterns, p.437-438]; [Huyen, AI Engineering, p.857-861]
10. **Blaming the model before reading the prompt.** Tell: output is mysteriously bad after wiring a library or template, and someone proposes a bigger model. Fix: log the exact final prompt after templating and compare it with the model's chat template; one author lost a day to a stale template, and framework default prompts have shipped with typos. [Huyen, AI Engineering, p.427, p.457]

## Hackathon calibration
- **Judging is about 4 minutes, science-fair style.** The eval gets one sentence plus one backup slide: n, pass rate, baseline, top failure and fix. Judges assume you use AI coding tools and probe whether you understand your own system. [Seed: J. How AI Projects Stand Out to Hackathon Judges, §J]
- **Judges type their own inputs.** Out-of-scope, false-premise, and injection handling matter more here than in production, where users self-select. Rehearse one live off-topic input so the refusal becomes a feature moment.
- **Shrink the eval, not the honesty.** The books' "about 300 examples for a trustworthy absolute score" and 1,000+ for small deltas do not fit; 20-50 cases with an honest range and slice table is the target. [Huyen, AI Engineering, p.405-407]
- **Precompute instead of serving.** Batch-score the demo dataset beforehand and serve from a lookup; keep one or two live showpiece inputs. [Lakshmanan, ML Design Patterns, p.271-277]
- **Ignore for 24h:** pretraining or self-hosting large models [Raschka, Build an LLM from Scratch, p.33, p.37]; fine-tuning (prompting plus retrieval first; LoRA needs hundreds to thousands of examples and teaches format, not facts) [Ziegler, Prompt Engineering for LLMs, p.162-165]; drift monitoring and retraining (state the one-sentence trigger instead) [Lakshmanan, ML Design Patterns, p.289-290]; semantic caching; SAFE-style claim verification unless factuality is the pitch; full safety stacks (one input guard, one output check) [Lakshmanan, Generative AI Design Patterns, p.609-618]; feature stores and pipelines.
- **Pitch the ladder, demo the bottom rung.** Demo the human-approves "Crawl" step and present full automation as roadmap with an acceptance-rate metric. [Huyen, AI Engineering, p.82-83]
- **User feedback under 30 testers is anecdote.** Count rephrases and early stops while watching people; do not claim statistics. Show the logging schema as the data-flywheel proof. [Huyen, AI Engineering, p.898-906, p.919-925]
- **Wizard-of-Oz is fine only if disclosed** when a judge asks. [Huyen, Designing ML Systems, p.23-24]

## Where experts disagree
- **Strongest model first vs small model first.** Alammar prototypes small and scales up [Hands-On LLMs, p.237]; Huyen and Ziegler start with the best model to establish feasibility [AI Engineering, p.355-357]; [Prompt Engineering for LLMs, p.159-162]. Follow Huyen here: cost is negligible at demo volume and a feasibility answer in hour 2 matters most. Move routers and guardrails to small models after the path works.
- **Keyword vs embeddings as the default retriever.** Huyen and Ziegler say BM25 first [AI Engineering, p.505-506]; [Prompt Engineering for LLMs, p.124-127]; Alammar defaults to embeddings for paraphrased queries [Hands-On LLMs, p.325-328]. Decide by corpus: names, IDs, codes favor keyword; conversational paraphrase favors embeddings; hybrid via rank fusion is a few lines. First check whether you need retrieval at all.
- **Prompt optimizers.** Lakshmanan favors DSPy-style search once you have examples and a metric [Generative AI Design Patterns, p.449-462]; Huyen warns of hidden calls (10 variants x 30 examples = 300) and wrong templates [AI Engineering, p.456-458]. Hand-iterate unless a teammate already knows DSPy.
- **Frameworks.** Lakshmanan wants an LLM-agnostic client layer from the first commit [Generative AI Design Patterns, p.475-476]; Anthropic and Huyen warn frameworks hide prompts and calls [Seed: B. Building Effective Agents, §B]; [AI Engineering, p.456-458]. Both hold: use a thin provider wrapper (one function with a model parameter, or LiteLLM) and write orchestration in plain code.
- **Judge scale and written reasons.** Huyen accepts anchored 1-5 scales [AI Engineering, p.398-399]; the seeds and Lakshmanan push binary for anything that drives a decision [Seed: D. LLM-as-a-Judge, §D]; [Generative AI Design Patterns, p.424]. Go binary. Lakshmanan notes written justifications may slightly hurt judge accuracy [p.425-426], but keep them: you need the reasons for error analysis. On pairwise: Lakshmanan and the Eugene Yan seed find head-to-head more reliable than absolute scores [Generative AI Design Patterns, p.424-425]; [Seed: E. Patterns for LLM Systems and Products, §E], while Huyen limits it to taste [AI Engineering, p.296-298]. Use pairwise for tone and helpfulness; check facts with code or against the source context [AI Engineering, p.326-333].

## Go deeper
- search_experts("compound error agent step count reliability", domain="15-ai-app-design-eval")
- search_experts("eval set size difference to detect bootstrap", domain="15-ai-app-design-eval")
- search_experts("LLM judge bias position verbosity self-preference", domain="15-ai-app-design-eval")
- search_experts("open coding axial coding error analysis traces", domain="15-ai-app-design-eval")
- search_experts("similarity threshold out-of-corpus refusal", domain="15-ai-app-design-eval")
- search_experts("prompt injection containment plan-then-execute action-selector", domain="15-ai-app-design-eval")
- search_experts("decision threshold cost of false positive false negative", domain="15-ai-app-design-eval")
- search_experts("retrieval test suite top-3 faithfulness citation precision", domain="15-ai-app-design-eval")
- search_experts("assemble facts deterministically LLM only rewords template", domain="15-ai-app-design-eval")
- search_experts("skip RAG context stuffing BM25 reranker", domain="15-ai-app-design-eval")
