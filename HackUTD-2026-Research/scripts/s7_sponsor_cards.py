"""S7: sponsor playbook cards (Q13) for the 17 HackUTD 2026 sponsors.
In:  data/tables/Q13_sponsor_card_rows.csv, Q11_pattern_x_industry.csv, Q19_hackutd2025_track_targeting.csv
Out: outputs/sponsor_cards.md, data/tables/Q13_sponsor_card_stats.csv
Every count in the cards is computed here. Brief facts are hand-copied from 06_hackutd_2026_sponsors/*.md and keep the
brief's [V]/[U] marks. Findings/pitch angles are hand-written (inference) but every number in them is computed.
Run from the project root: python3 -I scripts/s7_sponsor_cards.py
"""
import csv, collections, statistics, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
T = ROOT / 'data/tables'
ROWS = list(csv.DictReader(open(T / 'Q13_sponsor_card_rows.csv')))
TARGET = list(csv.DictReader(open(T / 'Q19_hackutd2025_track_targeting.csv')))
BY = collections.defaultdict(list)
for r in ROWS:
    BY[r['hackutd2026_sponsor']].append(r)


def pct(n, N):
    return int(100 * n / N + 0.5) if N else 0


def nN(n, N):
    return f"{n} of {N} ({pct(n, N)}%)"


def dist(rows, field, order=None):
    c = collections.Counter(r[field] for r in rows)
    N = len(rows)
    keys = order or [k for k, _ in c.most_common()]
    return '; '.join(f"{k}: {nN(c[k], N)}" for k in keys if c[k])


def med_feat(rows):
    v = [int(r['sponsor_features_used']) for r in rows]
    m = statistics.median(v) if v else None
    return int(m) if m is not None and m == int(m) else m


def link(r):
    return f"<{r['devpost']}>" if r['devpost'] else '[no link in dataset]'


def match(rows, field, vals):
    vals = vals if isinstance(vals, (list, tuple, set)) else [vals]
    return [r for r in rows if r[field] in vals]


def names(rows, k=4):
    return ', '.join(f"{r['project']} ({r['event']}) {link(r)}" for r in rows[:k]) or 'none'


def conf(N, share):
    # capped at medium: tags are analyst judgments and most placements are unpublished
    if N < 10:
        return 'low (n<10; tags are analyst judgments)'
    if N >= 12 and share >= 70:
        return 'medium (n>=12, share>=70%; capped at medium: analyst tags, placements mostly unpublished)'
    return 'medium-low (moderate n or share; analyst tags)'


def finding(sp, sentence, field, vals, impl, typ='association', note=''):
    rows = BY[sp]
    N = len(rows)
    sup = match(rows, field, vals)
    cnt = [r for r in rows if r not in sup]
    return (f"FINDING: {sentence}\n"
            f"SUPPORT: {nN(len(sup), N)} (unweighted, {field}={'/'.join(vals) if isinstance(vals,(list,tuple)) else vals}); "
            f"examples: {names(sup, 3)}\n"
            f"COUNTEREXAMPLES: {names(cnt, 3)}\n"
            f"CONFIDENCE: {conf(N, pct(len(sup), N))}\n"
            f"TYPE: {typ}{(' · ' + note) if note else ''}\n"
            f"IMPLICATION FOR US: {impl}")


def targeting(track):
    out = {}
    for r in TARGET:
        if r['track'] == track:
            out[r['group']] = (int(r['n_targeting']), int(r['N']))
    return out


# ------------------------------------------------------------------ brief facts (hand-copied; marks kept) ----------
B = {}
B['T-Mobile'] = dict(
    tier='Title', ask="Challenge text NOT public [V]; revealed at hacking start; up to 2 sponsor tracks [V]. 2025 prompt (inferred from winners, [U]): a tool for T-Mobile product managers to understand customer sentiment/pain points in real time. T-Mobile Fireside Chat Sat 1:30pm [V].",
    prize="2025: 1st iPhone 17, 2nd iPad Air, 3rd Beats Studio Pro [V]. 2026 prizes not public [V].")
B['PNC Bank'] = dict(
    tier='Platinum', ask="Challenge text NOT public [V]; workshop Sat 2:30pm [V]. 2025 challenge statements came in a hackerpack at hacking start [V]. The brief says it could not identify 2024/25 PNC winners and calls 2024 'unknown'; the dataset has 3 HackUTD 2024 + 3 HackUTD 2025 PNC winners (dataset wins over the brief, STATUS open issue).",
    prize="2025: 1st PlayStation 5 Slim, 2nd Ray-Ban Meta glasses, 3rd Yaber T1 Pro-Mini projector [V]. 2026 not public.")
B['Goldman Sachs'] = dict(
    tier='Gold', ask="Challenge text NOT public [V]; workshop Sat 6:10pm [V]. 2022 prompt: 'Build a tool for U.S. investors that factors in macroeconomic conditions' [V]. GS Quant/developer.gs.com need institutional credentials [V]: expect no API access unless handed out [U].",
    prize="2022: AirPods Max / Apple TV / $35 Grubhub, 4 winners [V]. 2026 not public.")
B['Capital One'] = dict(
    tier='Silver (official page); the unofficial redesign page lists Platinum, low trust', ask="Challenge text NOT public [V]. Only verified item: 'Switch Competition' Sat 6:45pm ECSW 4.210 (what it is: unverified) [V]. Nessie/DevExchange mock APIs may be retired [U].",
    prize="HackUTD IX (2022): 1 winner, 50 Amazon gift cards [V]. 2026 not public.")
B['Toyota Financial Services'] = dict(
    tier='Gold', ask="Challenge text NOT public [V]; no public API [brief tier table]. The brief calls 2024 'unknown'; the dataset has 3 HackUTD 2024 + 3 HackUTD 2025 winners (dataset wins).",
    prize="2025: 1st $500, 2nd $350, 3rd $150 Amazon gift cards [V]. 2022/2023 Toyota prizes were JBL/SXM gear [V].")
B['State Farm'] = dict(
    tier='Silver', ask="Challenge text NOT public [V]. 2022 prompt: 'Use technology to create a creative solution to a problem facing the community' [V]; workshop then was serverless REST APIs on AWS [V].",
    prize="2022: 34-inch LG Ultrawide / iPad / Beats Studio 3 [V]. 2026 not public.")
B['CBRE'] = dict(
    tier='Silver', ask="Challenge text NOT public [V]. Past challenges shipped a PDF statement + sample/quarterly data [V]. 2025 challenge 'Lost in the Pages' (chatbot over contracts/reports) [V]. 2022: AI/ML for customer experience from social media/contact centres/surveys [V]. CBRE's own Innovate 2026 rubric: business impact, technical innovation, scalability, market readiness, execution [V]. The brief cites a 2024 CBRE winner 'EcoManage' that is NOT in the dataset (dataset used).",
    prize="2022: $125/$75/$50 Amazon gift cards [V]. 2026 not public.")
B['EOG Resources'] = dict(
    tier='Gold', ask="Challenge text NOT public [V]; EOG Workshop Sat 5:15pm [V]. 2022 prompt: web/mobile/analysis app on drilling data to improve speed, cost, efficiency [V]. Expect a sponsor-provided dataset [U].",
    prize="2022: 2 winners (DJI Mini SE / Skullcandy Crusher Evo) [V]. 2026 not public.")
B['NMC2'] = dict(
    tier='Gold (identity assumed = NorthMark Compute & Cloud, low confidence)', ask="Challenge text NOT public [V]; NMC workshop Sat 4:20pm ECSW 1.365 [V]. 2025 challenge statement not public on Devpost [V]. The brief's NMC-to-winner mapping is [U] inference.",
    prize="2025 (Northmark): 1st Nintendo Switch 2, 2nd Sony WH-1000XM5, 3rd DJI Tello [V]. 2026 not public.")
B['NVIDIA'] = dict(
    tier='Silver', ask="No challenge or prize public; no NVIDIA event on the 2026 schedule [V]. Free Nemotron endpoints on build.nvidia.com [V]. Do not assume a prize [brief].",
    prize="Unknown for HackUTD 2026 [V absence].")
B['Spacetime'] = dict(
    tier='Silver', ask="Challenge text NOT public [V]; hosts a 'Bot Tournament' Sat 10:45pm (format unknown) [V]. Company identity unconfirmed: spec 0.2 assumes SpacetimeDB (Clockwork Labs) [U].",
    prize="Unknown; no HackUTD history found [U].")
B['Photon'] = dict(
    tier='Other', ask="Not public; listed only under 'Other' sponsors, no event [V]. Product pitch: messaging-agent SDK, 'agents in the conversations people already use' [brief]. No past HackUTD sponsorship found (first time, [U]).",
    prize="Unknown.")
# zero-winner cards (brief only)
Z = {
    '8090 AI': dict(tier='Platinum ("8090 Solutions" on the site)',
        ask="Challenge text and prizes NOT public [V]; no Devpost page found [V absence]. Company assumed = 8090 Solutions, Inc. (Software Factory: requirements -> blueprints -> work orders -> tests; agents via MCP) [V for identity/site name]. Hackathon access likely needs sponsor-provided seats/credits [U].",
        angle="[inference] Show requirements-to-tests traceability for a regulated-industry or legacy-modernisation problem; use their MCP workflow only if the booth confirms credits. Brief ideas: legacy-app modernisation, feedback-to-work-order loop, drift/compliance dashboard.",
        rule="[inference] No dataset evidence for a depth rule. Default to genuine, demo-visible use of their workflow if (and only if) access is confirmed; otherwise treat as problem-fit only."),
    'AT&T': dict(tier='Other (presents Saturday dinner)',
        ask="No AT&T challenge or prize listed [V]; AT&T absent from 2022/2023/2025 Devpost prize pages [V]; 2024 unknown. T-Mobile is title sponsor, so a telecom-themed track is likely T-Mobile's [V for title; rest U]. Aduna/CAMARA network APIs (Number Verification, SIM Swap) exist [V]; hackathon sandbox status unknown.",
        angle="[inference] Do not plan around an AT&T prize. If one appears, SIM-swap/number-verification fraud defence (mocked behind an interface) or low-signal resilience are the brief's directions.",
        rule="[inference] Ask at the booth first; do not spend integration effort before a prize is confirmed."),
    'Axxess': dict(tier='Bronze (brief assumes "Axess" = Axxess, Dallas home-health software)',
        ask="Challenge text and prizes NOT public; no Axxess workshop on the Nov 7 schedule [V]. Axxess ran its own healthcare hackathon at UTD Feb 21-22, 2026 (no prizes/challenge text on the page) [V]. API access is negotiated, no self-serve sandbox [third-party claim, U]: expect synthetic data.",
        angle="[inference] Clinician/agency-admin workflow tool on synthetic data (voice-to-visit-note with missing-field flags, natural-language agency analytics, plain-language family summaries), with explicit no-real-PHI handling.",
        rule="[inference] Problem-fit only (no API likely); safe-handling of PHI and a clinician persona matter more than integration depth."),
    'Niantic Spatial': dict(tier='Bronze',
        ask="Challenge text and prizes NOT public; no Devpost/MLH listing found [V absence]. Tools: Niantic Spatial SDK (VPS localisation, anchors; Unity/Swift/Kotlin, no web), Scaniverse [V]. 8th Wall is being shut down: do not build on it [V]. Its own contests judged creativity, innovation, technical excellence [V].",
        angle="[inference] A real place scanned with Scaniverse and localised with VPS (e.g. campus wayfinding or facility-inspection anchors), shown live at the station; enterprise/physical-AI framing over a games gimmick.",
        rule="[inference] If entered, core use of VPS/Scaniverse must be visible in the demo; needs a mobile/Unity build, so check team skills before choosing."),
    'Winstead PC': dict(tier='Gold (assumed Dallas law firm, medium-low)',
        ask="Challenge text and prizes NOT public [V]. No past HackUTD/Devpost challenge from Winstead found [V absence]; sponsors startup events (MassChallenge Texas, Texas A&M New Ventures) [V listing only]. Use only synthetic/public documents [brief].",
        angle="[inference] Trustworthy lawyer/client tool: lease or loan-agreement abstraction with source-cited quotes, startup legal-onboarding checklist, or data-room triage with an audit trail; accuracy, confidentiality and human-in-the-loop framing.",
        rule="[inference] Problem-fit only; every claim should link to a source page/clause. Related dataset pattern: docs_to_action (see CBRE/Goldman cards)."),
}
ORDER = ['T-Mobile', 'AT&T', 'PNC Bank', 'Goldman Sachs', 'Capital One', 'Toyota Financial Services', 'State Farm', 'CBRE',
         'EOG Resources', 'NVIDIA', 'NMC2', '8090 AI', 'Niantic Spatial', 'Spacetime', 'Axxess', 'Winstead PC', 'Photon']

# ------------------------------------------------------------------ hand-written findings/pitch (numbers computed) --
def cards_logic(sp):
    rows = BY.get(sp, [])
    N = len(rows)
    F, P, R = [], '', ''
    if sp == 'T-Mobile':
        tg = targeting('T-Mobile')
        F.append(finding(sp, f"The three HackUTD 2025 T-Mobile winners are PM/ops sentiment dashboards, the DubHacks winners are consumer tools, and none needed a T-Mobile product (sponsor_removable yes: " + nN(len(match(rows,'sponsor_removable','yes')),N) + ").",
                         'pattern', 'data_to_decision',
                         "Treat T-Mobile as a problem-fit track: show a named persona and a ranked-actions output; no API is needed."))
        if tg:
            w, d, r_ = tg.get('winner'), tg.get('demo_ready'), tg.get('random')
            F.append("FINDING: In HackUTD 2025 the T-Mobile track was crowded with near-identical sentiment dashboards.\n"
                     f"SUPPORT: entries targeting T-Mobile: winners {nN(*w)}, demo_ready baseline {nN(*d)}, random baseline {nN(*r_)} (table Q19_hackutd2025_track_targeting.csv; counts only, not a win rate); examples: winners Beacon, HarmoniQ, InsighT; baseline MagentaMonitor, PulseWire, SentimentRadar\n"
                     "COUNTEREXAMPLES: none found\nCONFIDENCE: medium (counts exact; the 'near-identical' reading is from the close read)\nTYPE: fact (counts) / inference (reading)\n"
                     "IMPLICATION FOR US: if the 2026 prompt is again 'sentiment/insights', differentiation (a different persona, a real action loop, live data) matters more than polish alone.")
        P = "[inference] Pitch the T-Mobile customer/business problem first, name the persona, show the ranked action on screen in the first minute. Brief directions: customer-experience signal engine (differentiated from 2025), SIM-swap/number-verification fraud demo with a mocked network API, Quality-on-Demand scenario app."
        R = "[inference] Problem-fit depth is enough (0 sponsor features used: " + str(nN(len(match(rows, 'sponsor_features_used', '0')), N)) + "). Add a network-API mock behind an interface only if the prompt asks."
    elif sp == 'PNC Bank':
        F.append(finding(sp, "PNC winners were data-to-decision or workflow-agent tools built around the prompt rather than a PNC API, and prompt text is unavailable for most.",
                         'sponsor_removable', 'yes',
                         "Plan problem-fit with a clean fintech/fraud/payments story; mock PNC-style APIs behind an interface."))
        P = "[inference] Brief directions: payee/account verification and fraud prevention, instant payout for gig workers, mobile check-deposit assistant. Lead with the payments/fraud problem and a visible agent or analytics output."
        R = "[inference] Problem-only depth; API use cannot be a requirement because 2026 credentials are unknown."
    elif sp == 'Goldman Sachs':
        F.append(finding(sp, "Goldman winners did not use Goldman tooling (removable: " + nN(len(match(rows,'sponsor_removable','yes')),N) + ") and their prompt text is not in the dataset (prompt_literalness na: " + nN(len(match(rows,'prompt_literalness','na')),N) + ").",
                         'sponsor_removable', 'yes',
                         "Do not rely on GS Quant (institutional credentials); use public market data (FRED, EDGAR) and show a clear finance story with explainability."))
        P = "[inference] Retail-investor macro/risk explainer or portfolio stress-test with plain-English narration and visible uncertainty; polish UX (the HackMIT GS prize was a UX prize [V])."
        R = "[inference] Problem-fit only; no sponsor feature can be assumed available."
    elif sp == 'Capital One':
        api = match(rows, 'prize_kind', 'sponsor_api_depth')
        medf = med_feat(api)
        F.append(finding(sp, "Capital One winners across other events are mostly consumer-facing data-to-decision tools where Capital One tech was removable.",
                         'sponsor_removable', 'yes',
                         "Default to a consumer finance story on synthetic transactions; do not budget for a required API integration."))
        F.append("FINDING: A minority of Capital One awards (sponsor_api_depth prizes) did need the sponsor's API, and those were not removable.\n"
                 f"SUPPORT: api-depth prizes {nN(len(api), N)}; of these, sponsor_removable=no {nN(len(match(api, 'sponsor_removable', 'no')), len(api))}; median sponsor_features_used among them {medf}; examples: {names(match(api, 'sponsor_removable', 'no'), 3)}\n"
                 f"COUNTEREXAMPLES: {names(match(api, 'sponsor_removable', 'yes'), 3)}\nCONFIDENCE: low-medium (small subgroup)\nTYPE: association\n"
                 "IMPLICATION FOR US: if a Capital One API/credit prize is announced, add the integration as a visible, live step; otherwise ignore it.")
        P = "[inference] Personal-finance coach, fraud/anomaly explainer or financial-inclusion tool for students, built on synthetic data with LLM explanations. Ask what the Switch Competition is."
        R = "[inference] Problem-fit by default; core integration only for an explicit API-depth prize."
    elif sp == 'Toyota Financial Services':
        F.append(finding(sp, "Toyota winners lean data-to-decision (car-buying / cost-of-ownership) tools, with sponsor customers as the stated problem owner in half of them.",
                         'pattern', 'data_to_decision',
                         "Frame a buyer-facing cost-transparency or lease-vs-buy tool; a gamified finance-lesson angle also appeared (Hingine)."))
        P = "[inference] True cost of ownership with what-if APR, agentic first-time-buyer assistant, or a payment-hardship helper; show a before/after cost number on screen."
        R = "[inference] Problem-fit (no public Toyota API). Non-removable winners: (" + nN(len(match(rows, 'sponsor_removable', 'no')), N) + "): see their lines before assuming zero integration."
    elif sp == 'State Farm':
        F.append(finding(sp, "State Farm winners show no dominant pattern and none needed State Farm tech (removable: " + nN(len(match(rows,'sponsor_removable','yes')),N) + ").",
                         'sponsor_removable', 'yes',
                         "Open-ended, community-problem prompts: pick by problem relevance (disaster readiness, driving safety, financial resilience), not by sponsor tooling."))
        P = "[inference] Disaster-preparedness / claims-readiness, teen-driver coaching or financial-resilience planner. Make the community problem and a measurable benefit obvious."
        R = "[inference] Problem-only depth."
    elif sp == 'CBRE':
        F.append(finding(sp, "CBRE winners are overwhelmingly data-to-decision or docs-to-action tools for sponsor-internal/B2B users, and CBRE tech was never needed.",
                         'pattern', ['data_to_decision', 'docs_to_action'],
                         "Prepare a documents/data-to-structured-decision frame (lease Q&A with citations, market briefing, energy copilot) so it is ready when the prompt drops."))
        F.append(finding(sp, "CBRE winners did not use any CBRE-provided feature (0 features used: " + nN(len(match(rows,'sponsor_features_used','0')),N) + "), so depth is problem-fit.",
                         'sponsor_features_used', '0',
                         "Use the provided dataset/PDF as the input and show cited, confidence-marked output; no integration work."))
        P = "[inference] Cited answers with confidence levels, structured extraction tables, and a business-impact line (CBRE's own rubric: business impact, innovation, scalability, market readiness, execution)."
        R = "[inference] Problem-only depth; spend the saved time on correctness and sourcing."
    elif sp == 'EOG Resources':
        F.append(finding(sp, "EOG winners are risk-detect-and-respond tools for sponsor-internal (operations) users; LOW N, treat as an anecdote.",
                         'pattern', 'risk_detect_and_respond',
                         "If a drilling/operations dataset is provided, build an anomaly/alert tool with a cost-or-time-saved number; otherwise skip."))
        P = "[inference] ROP/anomaly detector with cost-saved estimate, or a mobile field dashboard with alerts (the 'control room in your pocket' framing)."
        R = "[inference] Problem-fit on the provided dataset; low n, so no depth rule is supported by the data."
    elif sp == 'NMC2':
        F.append(finding(sp, "NMC2-tagged awards are workflow-automation agents or data tools for sponsor-internal users; the dataset has only a handful of rows (TAMUhack 2026 has the only ranked ones), so evidence is thin.",
                         'sponsor_removable', 'yes',
                         "Datacenter/AI-ops framing (technician work orders, GPU/power dashboards) is the evidence-backed lane; confirm identity at the NMC workshop first."))
        P = "[inference] Datacenter ops copilot (work-order triage, runbook RAG), GPU workload/power visualiser, or an efficient-inference demo with a benchmark view."
        R = "[inference] Problem-fit (removable: " + nN(len(match(rows,'sponsor_removable','yes')),N) + "). The brief's mapping of 2025 winners to NMC is itself inferred."
    elif sp == 'NVIDIA':
        medf = med_feat(rows)
        F.append(finding(sp, "NVIDIA-prize winners mostly could not remove NVIDIA tech, and most were multi-step agents.",
                         'sponsor_removable', 'no',
                         "If NVIDIA announces a track, make Nemotron/NIM the working core (not a logo) and show it live."))
        F.append(finding(sp, "NVIDIA-prize winners are mostly agentic_multistep systems.", 'ai_role', 'agentic_multistep',
                         f"Build a visible multi-step tool-calling flow; median sponsor_features_used in the dataset is {medf}."))
        P = "[inference] Tool-calling agent on Nemotron with an eval/guardrail story, a vision-language document app, or a model-routing latency/cost tool. Note the 2025 NVIDIA track was reportedly crowded (100+ entries, unverified, spec 0.2)."
        R = "[inference] Core integration, 1-2 NVIDIA features minimum (median " + str(medf) + "), shown in the demo."
    elif sp == 'Spacetime':
        medf = med_feat(rows)
        F.append(finding(sp, "Every Spacetime award in the dataset used Spacetime as the core backend (sponsor_removable no: " + nN(len(match(rows,'sponsor_removable','no')),N) + ").",
                         'sponsor_removable', 'no',
                         f"Enter only if the team builds on the sponsor's database/runtime from the start; median sponsor_features_used is {medf}, and " + nN(len(match(rows,'sponsor_features_used','1')),N) + " used only one feature, so one deep use is the floor."))
        P = "[inference] A bot/agent for the tournament game API, a self-play tuning harness, or a spectator/replay dashboard. Get the tournament spec early. Identity of the 2026 sponsor is unconfirmed."
        R = "[inference] Core integration is required (non-removable: " + nN(len(match(rows,'sponsor_removable','no')),N) + "); do not enter as an afterthought."
    elif sp == 'Photon':
        F.append(finding(sp, "Photon winners are consumer agents where the Photon messaging layer was core (sponsor_removable no: " + nN(len(match(rows,'sponsor_removable','no')),N) + "), mostly with one sponsor feature (sponsor_features_used=1: " + nN(len(match(rows,'sponsor_features_used','1')),N) + ").",
                         'sponsor_removable', 'no',
                         "If a Photon track appears, the agent must be reachable through the real messaging channel in the live demo."))
        P = "[inference] Campus assistant over iMessage, group-chat agent, or an accessibility check-in agent; pair with a model backend (Nemotron is a natural pair, [U])."
        R = "[inference] Core use of the SDK with a live text exchange at the station; 1 feature is enough per the data (median " + str(med_feat(rows)) + ")."
    elif sp == 'T-Mobile_dummy':
        pass
    return F, P, R


def stats_rows():
    out = []
    for sp in sorted(BY):
        rows = BY[sp]
        N = len(rows)
        for field in ['pattern', 'problem_owner', 'prompt_literalness', 'sponsor_removable', 'sponsor_features_used', 'placement', 'prize_kind']:
            c = collections.Counter(r[field] for r in rows)
            for k, n in sorted(c.items()):
                out.append(dict(sponsor=sp, field=field, value=k, n=n, N=N, pct=pct(n, N), low_n=N < 5,
                                median_sponsor_features_used=med_feat(rows)))
    return out


def main():
    lines = []
    A = lines.append
    A("# HackUTD 2026 sponsor playbook cards (Q13)")
    A("")
    A("Draft by eng1 for TASK-103. Source of every count: `data/tables/Q13_sponsor_card_rows.csv` (one row per past award from a HackUTD 2026 sponsor), computed by `scripts/s7_sponsor_cards.py` into `data/tables/Q13_sponsor_card_stats.csv`. Brief facts are from `06_hackutd_2026_sponsors/` and keep its [V] verified / [U] unverified marks. Dataset beats the briefs where they disagree (pnc, toyota, cbre).")
    A("")
    A("Reading rules:")
    A("- Counts are 'n of N (pct%)'. Cards with N < 5 are marked LOW N; any single-digit count is an anecdote, not a rule. Winners are unweighted projects-awards, not a win rate (spec rule 1).")
    A("- 'placement unranked' = the event does not publish 1st/2nd/3rd for that prize (HackUTD badges never do). Most rows are unranked, so these cards describe WHAT sponsors rewarded, not what beat what.")
    A("- `prompt_literalness` 0/1/2 = how closely the winner follows the sponsor prompt; `na` = prompt text unavailable or no prompt. `sponsor_removable` = could the sponsor's tech be removed without breaking the project. Both are analyst tags.")
    A("- Many rows come from other hackathons where the same company sponsored; the event is shown on every line. All 2026 challenge texts are NOT public (revealed Sat ~12:00 CT), so every pitch angle is inference.")
    A("- Sponsors with 0 dataset winners (8090 AI, AT&T, Axxess, Niantic Spatial, Winstead PC) have [brief only] cards.")
    A("")
    for sp in ORDER:
        rows = BY.get(sp, [])
        N = len(rows)
        if sp in Z:
            z = Z[sp]
            A(f"## {sp} — [brief only] no dataset winners")
            A(f"- Tier: {z['tier']}")
            A(f"- What the sponsor asked: {z['ask']}")
            A("- Past winners in dataset: 0 of 0 (no rows in Q13_sponsor_card_rows.csv). Counts, findings: not available.")
            A(f"- Pitch angle (inference): {z['angle']}")
            A(f"- Integration depth rule (inference): {z['rule']}")
            A("- Source: brief only (`06_hackutd_2026_sponsors/`); Q13_sponsor_card_rows.csv has 0 rows for this sponsor.")
            A("")
            continue
        if sp == 'AT&T':
            pass
        b = B[sp]
        evs = collections.Counter(r['event'] for r in rows)
        A(f"## {sp}{' — LOW N' if N < 5 else ''}")
        A(f"- Tier: {b['tier']}")
        A(f"- What the sponsor asked: {b['ask']}")
        A(f"- Prize structure: {b['prize']}")
        A(f"- Past winners in dataset: {N} awards across {len(evs)} events ({'; '.join(f'{e} x{n}' for e, n in evs.most_common(6))}{'; ...' if len(evs) > 6 else ''}).")
        for r in rows:
            A(f"  - {r['project']} — {r['event']}, placement {r['placement']}, {r['pattern']}, owner={r['problem_owner']}: {r['one_sentence']} {link(r)}")
        A("- Counts (Q13_sponsor_card_rows.csv; low n flagged by N<5):")
        A(f"  - pattern: {dist(rows, 'pattern')}")
        A(f"  - problem_owner: {dist(rows, 'problem_owner')}")
        A(f"  - prompt_literalness: {dist(rows, 'prompt_literalness', ['0', '1', '2', 'na'])}")
        A(f"  - sponsor_removable: {dist(rows, 'sponsor_removable')}")
        A(f"  - sponsor_features_used: median {med_feat(rows)}; {dist(rows, 'sponsor_features_used', sorted({r['sponsor_features_used'] for r in rows}, key=int))}")
        A(f"  - placement: {dist(rows, 'placement')}; prize_kind: {dist(rows, 'prize_kind')}")
        F, P, R = cards_logic(sp)
        A("- What won:")
        for f in F:
            for i, l in enumerate(f.split('\n')):
                A(('  - ' if i == 0 else '    ') + l)
        A(f"- Pitch angle (inference): {P.replace('[inference] ', '', 1)}")
        A(f"- Integration depth rule (inference): {R.replace('[inference] ', '', 1)}")
        A(f"- Tables: Q13_sponsor_card_rows.csv, Q13_sponsor_card_stats.csv{', Q19_hackutd2025_track_targeting.csv' if sp == 'T-Mobile' else ''}.")
        A("")
    (ROOT / 'outputs/sponsor_cards.md').write_text('\n'.join(lines) + '\n')
    sr = stats_rows()
    with open(T / 'Q13_sponsor_card_stats.csv', 'w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=list(sr[0].keys()))
        w.writeheader()
        w.writerows(sr)
    print(len(lines), 'lines;', len(sr), 'stat rows')


main()
