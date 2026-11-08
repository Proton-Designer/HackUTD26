# 05 — Detection quality, honest confidence and usable warnings
**Research date: 2026-11-07 | High-stakes classification: a generated number is not a calibrated probability.**

## TL;DR — use first
1. Do **not** display Nemotron's free-form “97% confidence” as if statistically calibrated; require measured reliability.
2. Build a holdout with **scams + benign look-alikes + prompt-injection**; report false-positive rate and per-scam-type recall.
3. Display a risk category, concrete evidence, source freshness and safe next step; abstain when sources are absent.
4. Make the user approve all consequential actions and offer a safe way to correct a mistaken warning.
5. A brief, well-timed “pause and verify” intervention has better research support than repeating generic red warnings.

## A. How to get a confidence number responsibly

| Source / URL | Finding | Build/pitch use |
|---|---|---|
| **The Score Granularity Gap in Black-Box LLM Classification** (2026) — [paper](https://arxiv.org/html/2606.22179) | Verbalized confidence measures confidence in the *predicted class*; it is **not automatically P(scam)**. A 95%-confident “benign” predicts scam probability ~5%, assuming the quoted confidence is meaningful. Coarse verbalized probabilities can be hard to calibrate. | Store label and raw score separately, convert to a positive-class score only if justified, then test reliability on holdout. |
| **Evaluation Pitfalls and Sparsity Limitations in LLM-Based Confidence Estimates for Classification** (2026) — [paper](https://arxiv.org/html/2608.04899) | Token-logprob confidence and stated confidence depend on class label tokenization and API support; evaluation can be misleading when score resolution is sparse. | Avoid treating first-token logprobs as a universal clean posterior; compare methods if time permits. |
| **Rethinking Verbalized Confidence for LLM-as-a-Judge** (2026) — [paper](https://arxiv.org/html/2609.10996v1) | On some newer proprietary models, structured verbalized confidence can work better than logprob alternatives **for judging tasks**; this does not show consumer-scam classification is calibrated. | Resist universal “logprobs always win” claims; measure your own domain. |
| **ConfidenceBench** (2026) — [paper](https://arxiv.org/abs/2607.20526) | Calibration quality varies among models even when predictions sound certain. | Pitch visible calibration diagnostics; distinguish model output from validated reliability. |
| **scikit-learn calibration curves** — [official docs](https://scikit-learn.org/stable/modules/calibration.html) | Reliability diagrams compare predicted probability buckets with observed frequencies; Brier score is a proper probability-scoring rule. | Produce a 10-bin reliability plot and Brier score for held-out **synthetic** test cases. |

**Recommended demo behavior** (inference/design recommendation grounded in above): use `high concern`, `needs verification`, `no strong scam signals detected`, and `insufficient evidence` rather than false-exact percentages. If probability display is required, label **“calibrated on our synthetic test set only”**, give sample size and cutoff, and show reliability diagram. If only 40 holdout samples, 10 bins are sparse; use 4 bins or show counts, do **not** imply strong calibration.

### Example backend record and evidence-bound interface

```json
{
  "predicted_class": "likely_scam",
  "risk_display": "High concern — not a confirmed scam",
  "evidence": [
    {"signal":"Requests urgent transfer to a new account", "source":"message_text"},
    {"signal":"Domain similar to bank name", "source":"local_dnstwist"},
    {"signal":"Reputation service did not return a match", "source":"web_risk", "status":"not_listed"}
  ],
  "model_confidence": null,
  "probability_calibrated": false,
  "recommended_action": "Do not transfer yet. Call the bank using the number on your card.",
  "user_approval_required": true
}
```

**UI rule:** show independent signals and their caveats, not only “Nemotron thinks scam.” A “no result” from a threat feed is not evidence that a URL is safe. [Google Safe Browsing](https://developers.google.com/safe-browsing/reference), [Web Risk](https://cloud.google.com/web-risk/docs/lookup-api).

## B. Synthetic benchmark and metrics

| Test cohort | Proposed count | Intended challenge | Score to report |
|---|---:|---|---|
| 12 scam families x 5 variants | 60 | Basic detection + varied wording | **Per-type recall** and overall recall |
| Benign look-alikes from same 12 domains of life | 60 | Mistakenly blocking real deliveries, real bank texts, friendly messages | **False-positive rate**, specificity, precision |
| Adversarial variants within the above (or separate) | >=12 | Spelling, shortened URL, URL in QR, harmless-appearing long message, multilingual and prompt injection | **Attack-specific recall** + unauthorized-tool-call rate |
| Unavailable evidence fixture | >=6 | Threat feed returns error/timeout or model refuses | Rate of **safe abstention** and honest UI |

**Formulae:** `recall = TP / (TP + FN)`; `false_positive_rate = FP / (FP + TN)`; `precision = TP / (TP + FP)`; `Brier = mean((p_scam - y)^2)`. Report denominators; *accuracy alone masks failures*. For confidence calibration use reliability data by bin (`mean predicted p` vs `empirical scam share`) and optionally expected calibration error (ECE); see [scikit-learn](https://scikit-learn.org/stable/modules/calibration.html). Don't use the same test examples to tune and claim final results. Final demo figures must come from actual tests—**none are measured in this research deliverable**.

### Minimal deterministic evaluation skeleton

```python
from collections import defaultdict

def summarize(rows):
    # rows = [{"truth":0/1, "pred":0/1, "type":"package"}, ...]
    tp = sum(r["truth"] == 1 and r["pred"] == 1 for r in rows)
    fn = sum(r["truth"] == 1 and r["pred"] == 0 for r in rows)
    fp = sum(r["truth"] == 0 and r["pred"] == 1 for r in rows)
    tn = sum(r["truth"] == 0 and r["pred"] == 0 for r in rows)
    per_type = {}
    for family in {r["type"] for r in rows if r["truth"] == 1}:
        subset = [r for r in rows if r["truth"] == 1 and r["type"] == family]
        per_type[family] = sum(r["pred"] == 1 for r in subset) / len(subset)
    return {"TP":tp,"FN":fn,"FP":fp,"TN":tn,
            "recall":tp/(tp+fn) if tp+fn else None,
            "benign_FPR":fp/(fp+tn) if fp+tn else None,
            "per_type_recall":per_type}
```

## C. How to design actionable warnings

| Research / guidelines | What it supports | Specific UI decision |
|---|---|---|
| **Google PAIR People + AI Guidebook — Explainability & Trust** — [chapter](https://pair.withgoogle.com/guidebook-v2/chapters/explainability-trust) | Give explanations appropriate to trust level and to potential harm; consider both false positives and false negatives. | Add a 2-signal evidence list and a “Why am I seeing this?” expander. |
| **Google PAIR — Errors & Graceful Failure** — [chapter](https://pair.withgoogle.com/guidebook-v2/chapters/errors-failing) | Define failure modes and give users a way forward even when AI is wrong or uncertain. | Add “This seems legitimate,” “Check another way,” and official provider verification. |
| **Microsoft 18 Guidelines / HAX** — [HAX Toolkit](https://www.microsoft.com/en-us/research/project/hax-toolkit), [guidelines](https://www.microsoft.com/en-us/haxtoolkit/ai-guidelines/) | Guidelines include **G2 Make clear how well system can do what it can do**, **G3 Time services based on context**, **G7 Support efficient invocation**, **G8 Support efficient dismissal**, **G9 Support efficient correction**, **G10 Scope services when in doubt**, **G11 Make clear why system did what it did**, **G16 Convey consequences of user actions**. | Alert *at moment of risky transfer*, explain evidence and effect; user can dismiss or correct; show reversible action when possible. Exact wording of guideline titles can vary by edition; refer to linked HAX list. |
| **Alice in Warningland** — [USENIX Security 2013](https://www.usenix.org/conference/usenixsecurity13/technical-sessions/presentation/akhawe) | A field study with **25,405,944** warning impressions found large differences in click-through by browser/warning design; warning presentation matters. | Show one clear interruption at the irreversible step; avoid noisy repeated warnings. |
| **Warning habituation studies** — [Brigham Young University research index](https://scholarsarchive.byu.edu/facpub/6495/) | Repeated, unvaried warning exposure can drive habituation; exact experimental effect in this cited record **not revalidated here**. | Suppress duplicate alerts for same incident and provide escalating, meaningful new evidence. |
| **Multidimensional Warning Messages on Payment Security Behavior** (2026) — [open-access study](https://pmc.ncbi.nlm.nih.gov/articles/PMC13024239/) | Two sequential lab experiments examine warnings in mobile-payment contexts, including intervention wording, visual treatment and attention. Experimental scenario limits generalization. | User-facing “Pause. Verify recipient through a trusted channel.” beside transfer approval. |
| **Reducing Consumer Fraud and Scam Victimization Through Incubation** (2026) — [journal article](https://link.springer.com/article/10.1007/s10603-026-09619-3) | Behavioral studies suggest a short intervening reflection task can improve recognition of a complex suspicious offer; external validity to real bank transactions not proven. | Add a deliberate pause with a simple “How did this person first contact you?” check, not manipulative dark patterns. |

## D. What to do when our own classifier is wrong

- **False positive (legit bank fraud alert):** Do not automatically delete or block. Say “could not independently authenticate this sender; verify in your bank's official app,” give one-tap override and optional allowlist. [Google PAIR](https://pair.withgoogle.com/guidebook-v2/chapters/errors-failing).
- **False negative (novel scam, no malicious URL matches):** Avoid “safe.” Say “No known threat-list match; scammers can use new domains.” Maintain a simple contextual warning around money/OTP/remote-access requests. [Google Safe Browsing overview](https://developers.google.com/safe-browsing/reference).
- **Uncertain / service outage:** Show `evidence unavailable`, user-safe verification steps, no numerical fake precision. [HAX](https://www.microsoft.com/en-us/haxtoolkit/ai-guidelines/).
- **Consequential action:** A threat label alone never initiates a payment freeze, report, block or outbound message. A separate policy engine + **explicit informed user confirmation** must authorize the mocked action. [Securing LLM agent design patterns](https://arxiv.org/html/2506.08837).

## E. Demo-ready evaluation slide template (fill only with real measured values)

> **Synthetic evaluation (N = ___, collected Nov 2026)**: Scam recall ___/___ = ___%; legitimate-message false-positive rate ___/___ = ___%; worst-performing scam type ___; unapproved tool actions ___/___ (target 0); known limits: synthetic, text-centric, no network deployment, no external validation.

Avoid benchmarks on real victims' data: sponsor prompt prohibits real customer data.

**Verification caveat:** Any provider feature, quota, fee, metric or endpoint not explicitly validated from a current primary source is **UNVERIFIED**; no production-connected result is claimed.
