"""S6: computations that need S3/S4 tags (Q0-Q8, Q10-Q18, Q20, Q23).
In:  data/processed/*.csv, data/tagged/content_all.jsonl, data/tagged/cover_test.jsonl (optional), data/pages/page_facts.jsonl
Out: data/tables/Qxx_*.csv (+ INDEX.md)

Conventions
- Unit = project, except paired comparisons, which use award rows in paired tracks (a project 1st in one track and
  2nd in another appears once on each side).
- 'excl_weak' views drop evidence depth C and low-confidence records.
- Paired sign tests: per track with a published 1st and 2nd/3rd, compare the 1st's value with the mean of the
  lower placers; count tracks where 1st is higher / equal / lower.
- Ratings are analyst judgments (spec rule 5): only used for within-track comparisons and floor/spread analysis.
"""
import sys, pathlib, json, csv, collections, statistics, re
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from s6_lib import *
S = 'scripts/s6_tagged.py'
PROJ = {r['project_id']: r for r in load_projects()}
AW = [a for a in load_awards() if a['project_id'] in PROJ]
TAG = load_tags()
if not TAG: sys.exit('no tags yet (data/tagged/content_all.jsonl)')
BID = {r['blind_id']: pid for pid, r in PROJ.items()}
COVER = {}
cf = ROOT / 'data/tagged/cover_test.jsonl'
if cf.exists():
    for l in open(cf):
        r = json.loads(l)
        if r['blind_id'] in BID: COVER[BID[r['blind_id']]] = r
PAGE = {}
for l in open(ROOT / 'data/pages/page_facts.jsonl'):
    r = json.loads(l)
    if r.get('status') == 'ok': PAGE[r['project_id']] = r
DIMS = ['innovation', 'technical_complexity', 'completeness', 'design', 'impact', 'presentation']

def v(x): return x.get('v') if isinstance(x, dict) else x
def T(pid, f): return v(TAG[pid].get(f)) if pid in TAG else None
def rating(pid, d):
    x = v((TAG.get(pid, {}).get('ratings') or {}).get(d))
    return x if isinstance(x, int) else None
def ratings(pid): return [rating(pid, d) for d in DIMS if rating(pid, d) is not None]
def weak(pid): return PROJ[pid]['evidence_depth'] == 'C' or PROJ[pid]['confidence'] == 'low'
def unk(x): return None if x in (None, 'unknown', 'na', '') else x
def bucket(n, cuts):
    if n is None: return None
    lo = 0
    for c in cuts:
        if n <= c: return str(c) if lo == c else f'{lo}-{c}'
        lo = c + 1
    return f'>{cuts[-1]}'
def int_or_none(x):
    try: return int(float(x))
    except Exception: return None
def page_has(pid, pat):
    p = PAGE.get(pid)
    if not p: return None
    return any(re.search(pat, s.get('heading') or '', re.I) for s in p.get('sections') or [])

FEAT = collections.OrderedDict([
    ('pattern', lambda p: T(p, 'pattern')),
    ('ai_role', lambda p: T(p, 'ai_role')),
    ('single_call_wrapper_or_none', lambda p: None if T(p, 'ai_role') is None else T(p, 'ai_role') in ('single_call_wrapper', 'none')),
    ('named_user', lambda p: T(p, 'named_user')),
    ('cost_of_problem_stated', lambda p: T(p, 'cost_of_problem_stated')),
    ('cost_evidence_beyond_assertion', lambda p: None if T(p, 'cost_of_problem_stated') is None else T(p, 'cost_of_problem_stated') in ('cited_stat', 'user_quote_or_interview', 'measured_by_team')),
    ('live_data', lambda p: unk(T(p, 'live_data'))),
    ('mocked_parts_disclosed', lambda p: unk(T(p, 'mocked_parts_disclosed'))),
    ('novelty_source', lambda p: T(p, 'novelty_source')),
    ('centerpiece_visible', lambda p: T(p, 'centerpiece_visible')),
    ('centerpiece_in_demo_output', lambda p: None if T(p, 'centerpiece_visible') is None else T(p, 'centerpiece_visible') == 'in_demo_output'),
    ('n_user_flows', lambda p: bucket(unk(T(p, 'n_user_flows')), [0, 1, 2])),
    ('has_hardware', lambda p: B(PROJ[p]['has_hardware'])),
    ('has_video_embed', lambda p: PAGE[p].get('has_video_embed') if p in PAGE else None),
    ('has_arch_diagram', lambda p: B(PROJ[p]['has_arch_diagram'])),
    ('n_images', lambda p: bucket(int_or_none(PROJ[p]['n_images']), [0, 3, 6])),
    ('n_external_deps', lambda p: bucket(int_or_none(PROJ[p]['n_external_deps']), [2, 4, 7])),
    ('page_has_challenges_section', lambda p: page_has(p, r'challenge')),
    ('page_has_whats_next_section', lambda p: page_has(p, r"what'?s next|next steps|future")),
    ('page_has_accomplishments_section', lambda p: page_has(p, r'accomplish|proud')),
    ('cover_test_score', lambda p: COVER[p]['cover_test_score'] if p in COVER else None),
    ('cover_test_3of3', lambda p: COVER[p]['cover_test_score'] == 3 if p in COVER else None),
    *[(f'rating_{d}', (lambda d: lambda p: rating(p, d))(d)) for d in DIMS],
    *[(f'rating_{d}_ge4', (lambda d: lambda p: None if rating(p, d) is None else rating(p, d) >= 4)(d)) for d in DIMS],
    ('rating_min', lambda p: min(ratings(p)) if ratings(p) else None),
    ('rating_spread', lambda p: max(ratings(p)) - min(ratings(p)) if ratings(p) else None),
])
ORDINAL = ['cover_test_score', *[f'rating_{d}' for d in DIMS], 'rating_min', 'rating_spread']

def tagged(ps): return [p for p in ps if p in TAG]
def views(ps): return {'all': tagged(ps), 'excl_weak': [p for p in tagged(ps) if not weak(p)]}

# ---------------- Q0: HackUTD 2025 winners vs demo_ready vs random ----------------
w25 = [p for p, r in PROJ.items() if r['s_hackutd'] == 'True' and r['edition_key'] == 'HackUTD 2025']
dr = [p for p, r in PROJ.items() if r['sample_group'] == 'demo_ready']
rnd = [p for p, r in PROJ.items() if r['sample_group'] == 'random']
for vn in ('all', 'excl_weak'):
    G = {'winners': views(w25)[vn], 'demo_ready': views(dr)[vn], 'random': views(rnd)[vn]}
    rows = prevalence_table(G, {k: f for k, f in FEAT.items() if k not in ORDINAL})
    for r in rows: r['gap_winners_minus_demo_ready_pts'] = (r['winners_pct'] or 0) - (r['demo_ready_pct'] or 0) if r['winners_N'] and r['demo_ready_N'] else ''
    write(f'Q00_hackutd2025_vs_baseline_{vn}.csv', rows, 'Q0', S, f'HackUTD 2025 winners vs demo_ready vs random non-winners, every tagged field ({vn}).')
    rows = []
    for f in ORDINAL:
        row = {'feature': f}
        for g, ps in G.items():
            xs = [FEAT[f](p) for p in ps if FEAT[f](p) is not None]
            row[f'{g}_N'] = len(xs); row[f'{g}_median'] = statistics.median(xs) if xs else ''; row[f'{g}_mean'] = round(statistics.mean(xs), 2) if xs else ''
        rows.append(row)
    write(f'Q00_hackutd2025_ordinal_{vn}.csv', rows, 'Q0', S, f'HackUTD 2025 winners vs baseline groups: medians/means of ratings and cover score ({vn}).')

# ---------------- paired sets (Q1, Q2, Q3, Q5, Q6, Q8, Q10, Q14, Q15, Q17, Q23) ----------------
paired = [a for a in AW if a['in_paired_set'] == 'True']
tracks = collections.defaultdict(lambda: {'1': [], 'lower': []})
for a in paired:
    tracks[a['track_key']]['1' if a['placement'] == '1' else 'lower'].append(a['project_id'])
def track_kind(t): return 'general' if t.endswith('|general') else ('sponsor' if '|sponsor:' in t else 'other_track')

def paired_rows(feats, kind_filter=None, drop_weak=False, label=''):
    rows = []
    for f, fn in feats.items():
        firsts, lowers = [], []
        hi = eq = lo = 0
        for t, g in tracks.items():
            if kind_filter and track_kind(t) not in kind_filter: continue
            a = [p for p in g['1'] if p in TAG and not (drop_weak and weak(p))]
            b = [p for p in g['lower'] if p in TAG and not (drop_weak and weak(p))]
            av = [fn(p) for p in a if fn(p) is not None]; bv = [fn(p) for p in b if fn(p) is not None]
            firsts += av; lowers += bv
            if av and bv and f in ORDINAL:
                d = statistics.mean(av) - statistics.mean(bv)
                hi += d > 0; eq += d == 0; lo += d < 0
            elif av and bv and f not in ORDINAL:
                pass
        if f in ORDINAL:
            rows.append(dict(view=label, feature=f, value='(ordinal)', first_N=len(firsts), lower_N=len(lowers),
                             first_median=statistics.median(firsts) if firsts else '', lower_median=statistics.median(lowers) if lowers else '',
                             first_mean=round(statistics.mean(firsts), 2) if firsts else '', lower_mean=round(statistics.mean(lowers), 2) if lowers else '',
                             tracks_first_higher=hi, tracks_equal=eq, tracks_first_lower=lo, n_track_pairs=hi + eq + lo,
                             low_n=(hi + eq + lo) < 5))
        else:
            vals = sorted({str(x) for x in firsts + lowers})
            for val in vals:
                n1 = sum(str(x) == val for x in firsts); n2 = sum(str(x) == val for x in lowers)
                # track-level pairs where both sides known
                tp = 0
                for t, g in tracks.items():
                    if kind_filter and track_kind(t) not in kind_filter: continue
                    if any(fn(p) is not None for p in g['1'] if p in TAG) and any(fn(p) is not None for p in g['lower'] if p in TAG): tp += 1
                gap = pct(n1, len(firsts)) - pct(n2, len(lowers)) if firsts and lowers else ''
                rows.append(dict(view=label, feature=f, value=val, first_n=n1, first_N=len(firsts), first_pct=pct(n1, len(firsts)),
                                 lower_n=n2, lower_N=len(lowers), lower_pct=pct(n2, len(lowers)), gap_pts=gap, n_track_pairs=tp,
                                 flag_gap20_pairs5=(gap != '' and abs(gap) >= 20 and tp >= 5), low_n=min(len(firsts), len(lowers)) < 5))
    return rows

for kinds, name in ((None, 'all_tracks'), ({'general'}, 'general'), ({'sponsor'}, 'sponsor'), ({'other_track'}, 'theme_other')):
    rows = paired_rows(FEAT, kinds, False, 'all') + paired_rows(FEAT, kinds, True, 'excl_weak')
    write(f'Q01_paired_{name}.csv', rows, 'Q1/Q2/Q3/Q5/Q6/Q8/Q14/Q15/Q17', S,
          f'1st vs 2nd/3rd in the same event+track ({name}); categorical shares with gap + track-pair count; ordinal medians + per-track sign counts.')
write('Q01_paired_tracks.csv', [dict(track_key=t, kind=track_kind(t), firsts='; '.join(PROJ[p]['project_name'] for p in g['1']),
                                     lowers='; '.join(PROJ[p]['project_name'] for p in g['lower']),
                                     tagged_first=sum(p in TAG for p in g['1']), tagged_lower=sum(p in TAG for p in g['lower']))
                                for t, g in sorted(tracks.items())], 'Q1', S, 'Every paired track (published 1st + 2nd/3rd) and its projects.')

# ---------------- Q2: floor vs differentiator ----------------
winners = [p for p, r in PROJ.items() if r['dataset'] != 'baseline' and p in TAG]
rows = []
for d in DIMS:
    xs = [rating(p, d) for p in winners if rating(p, d) is not None]
    g4 = sum(x >= 4 for x in xs)
    pr = [r for r in paired_rows({f'rating_{d}': FEAT[f'rating_{d}']}, None, False, 'all')][0]
    w25x = [rating(p, d) for p in w25 if p in TAG and rating(p, d) is not None]
    drx = [rating(p, d) for p in dr if p in TAG and rating(p, d) is not None]
    rows.append(dict(dimension=d, winners_N=len(xs), winners_ge4=cell(g4, len(xs)), winners_ge4_pct=pct(g4, len(xs)),
                     floor_if_ge80=pct(g4, len(xs)) >= 80 if xs else '',
                     paired_first_median=pr['first_median'], paired_lower_median=pr['lower_median'],
                     paired_median_gap=(pr['first_median'] - pr['lower_median']) if pr['first_median'] != '' and pr['lower_median'] != '' else '',
                     paired_tracks_first_higher=pr['tracks_first_higher'], paired_tracks_equal=pr['tracks_equal'], paired_tracks_first_lower=pr['tracks_first_lower'],
                     hackutd25_winners_median=statistics.median(w25x) if w25x else '', demo_ready_median=statistics.median(drx) if drx else ''))
write('Q02_floor_vs_differentiator.csv', rows, 'Q2', S, 'Per rubric dimension: share of winners rated >=4 (floor if >=80%), paired 1st-minus-lower medians and per-track signs, HackUTD 2025 winners vs demo_ready medians.')

# ---------------- Q4: general 1sts (archetype inputs) ----------------
g1 = sorted({a['project_id'] for a in AW if a['prize_kind'] == 'general' and a['placement'] == '1'})
rows = []
for p in g1:
    if p not in TAG: continue
    r = PROJ[p]
    rows.append(dict(project=r['project_name'], event=r['edition_key'], event_type=r['event_type'], weight=r['weight'],
                     pattern=T(p, 'pattern'), ai_role=T(p, 'ai_role'), has_hardware=r['has_hardware'], live_data=T(p, 'live_data'),
                     novelty_source=T(p, 'novelty_source'), centerpiece=T(p, 'technical_centerpiece'), wow=T(p, 'wow_moment'),
                     one_sentence=TAG[p].get('one_sentence'), n_awards=r['n_awards'], also=r['prize_kinds'],
                     devpost=next((x['url'] for x in [PAGE.get(p, {})] if x), '')))
write('Q04_general_1sts.csv', rows, 'Q4', S, 'Every general/overall 1st with clustering fields (pattern, ai_role, hardware, live data, novelty), centerpiece and wow moment.')
cross = collections.Counter((x['pattern'], x['ai_role']) for x in rows)
wcross = collections.Counter()
for x in rows: wcross[(x['pattern'], x['ai_role'])] += float(x['weight'])
write('Q04_general_1sts_pattern_x_ai.csv', [dict(pattern=k[0], ai_role=k[1], n=n, N=len(rows), weighted=round(wcross[k], 1)) for k, n in cross.most_common()],
      'Q4', S, 'General 1sts: pattern x ai_role counts (unweighted and event-type weighted).')
for f in ('pattern', 'ai_role', 'novelty_source', 'live_data', 'has_hardware'):
    c = collections.Counter(x[f] for x in rows); wc = collections.Counter()
    for x in rows: wc[x[f]] += float(x['weight'])
    tw = sum(wc.values())
    write(f'Q04_general_1sts_{f}.csv', [dict(value=k, n=n, N=len(rows), pct=pct(n, len(rows)), weighted_pct=round(100 * wc[k] / tw) if tw else '') for k, n in c.most_common()],
          'Q4', S, f'General 1sts: distribution of {f} (unweighted + weighted).')

# ---------------- Q5/Q6 general 1st vs lower specifics ----------------
cp = []
for p in g1:
    if p in TAG: cp.append(dict(project=PROJ[p]['project_name'], event_type=PROJ[p]['event_type'], ai_role=T(p, 'ai_role'),
                                centerpiece=T(p, 'technical_centerpiece'), visible=T(p, 'centerpiece_visible')))
write('Q06_general_1st_centerpieces.csv', cp, 'Q6', S, 'Technical centerpiece text and visibility for every general 1st.')

# ---------------- Q7 novelty: general 1sts vs sponsor 1sts ----------------
s1 = sorted({a['project_id'] for a in AW if a['prize_kind'].startswith('sponsor_') and a['placement'] == '1'})
write('Q07_novelty_general1_vs_sponsor1.csv', prevalence_table({'general_1st': tagged(g1), 'sponsor_1st': tagged(s1)},
      {'novelty_source': FEAT['novelty_source'], 'pattern': FEAT['pattern'], 'ai_role': FEAT['ai_role']}),
      'Q7', S, 'Novelty source (and pattern, ai_role) among general 1sts vs sponsor 1sts.')

# ---------------- Q10 / Q12 / Q13 / Q14: sponsor fit for the AWARDING sponsor ----------------
def norm(s): return re.sub(r'[^a-z0-9]', '', (s or '').lower())
def sponsor_fit_for(pid, sponsor, prize_name):
    keys = [k for k in (norm(sponsor), norm(prize_name)) if len(k) >= 3]
    for t in TAG.get(pid, {}).get('sponsor_fit') or []:
        tn = norm(t.get('track'))
        if any(k[:6] in tn or tn[:6] in k for k in keys): return t
    return None
SFF = ['sponsor_removable', 'sponsor_features_used', 'prompt_literalness', 'prompt_words_in_title', 'problem_owner']
def sf_val(a, f):
    t = sponsor_fit_for(a['project_id'], a['sponsor'], a['prize_name'])
    if not t: return None
    x = v(t.get(f))
    return None if x in ('unknown', 'na', None) else x
spaw = [a for a in AW if a['prize_kind'].startswith('sponsor_') and a['project_id'] in TAG]
match = sum(1 for a in spaw if sponsor_fit_for(a['project_id'], a['sponsor'], a['prize_name']))
rows = []
for kind in ('sponsor_domain', 'sponsor_api_depth', 'sponsor_open', 'all_sponsor'):
    A_ = [a for a in spaw if kind == 'all_sponsor' or a['prize_kind'] == kind]
    for side, pred in (('1st', lambda a: a['placement'] == '1'), ('2nd_3rd', lambda a: a['placement'] in ('2', '3')),
                       ('paired_1st', lambda a: a['in_paired_set'] == 'True' and a['placement'] == '1'),
                       ('paired_2nd_3rd', lambda a: a['in_paired_set'] == 'True' and a['placement'] in ('2', '3')),
                       ('any_placement', lambda a: True)):
        G = [a for a in A_ if pred(a)]
        for f in SFF + ['completeness']:
            vals = [sf_val(a, f) if f != 'completeness' else rating(a['project_id'], 'completeness') for a in G]
            known = [x for x in vals if x is not None]
            for val in sorted({str(x) for x in known}):
                n = sum(str(x) == val for x in known)
                rows.append(dict(prize_kind=kind, group=side, field=f, value=val, n=n, N_known=len(known), pct=pct(n, len(known)),
                                 N_awards=len(G), unknown_or_unmatched=len(G) - len(known), low_n=len(known) < 5))
write('Q10_sponsor_fit_by_placement.csv', rows, 'Q10/Q12/Q14', S,
      f'Awarding-sponsor fit (removable, features used, prompt literalness, prompt words in title, problem owner, completeness) by sponsor prize kind and placement. Sponsor_fit matched to award for {match} of {len(spaw)} sponsor awards.')

# Q11 matrix + Q13 cards
IND26 = {'telecom', 'finance_banking', 'insurance', 'real_estate', 'energy', 'auto_mobility', 'geospatial_ar', 'ai_compute', 'cloud_devtools', 'health', 'legal', 'other'}
cellp = collections.defaultdict(set)
for a in spaw: cellp[(T(a['project_id'], 'pattern'), a['sponsor_industry'])].add(a['project_id'])
gen_won = {a['project_id'] for a in AW if a['prize_kind'] == 'general'}
rows = []
for (pat, ind), ps in sorted(cellp.items(), key=lambda x: (-len(x[1]), x[0])):
    rows.append(dict(pattern=pat, sponsor_industry=ind, in_2026_industries=ind in IND26, n_projects=len(ps),
                     n_also_general=len(ps & gen_won), examples='; '.join(sorted(PROJ[p]['project_name'] for p in ps)[:3]),
                     examples_also_general='; '.join(sorted(PROJ[p]['project_name'] for p in ps & gen_won)[:3])))
write('Q11_pattern_x_industry.csv', rows, 'Q11', S, 'Pattern x sponsor_industry for all sponsor-prize winners (projects), with examples and how many also won general.')
rows = []
for a in spaw:
    if a['hackutd2026_sponsor']:
        p = a['project_id']; t = sponsor_fit_for(p, a['sponsor'], a['prize_name']) or {}
        rows.append(dict(hackutd2026_sponsor=a['hackutd2026_sponsor'], project=PROJ[p]['project_name'], event=PROJ[p]['edition_key'],
                         placement=a['placement'], prize_kind=a['prize_kind'], pattern=T(p, 'pattern'), ai_role=T(p, 'ai_role'),
                         problem_owner=v(t.get('problem_owner')), prompt_literalness=v(t.get('prompt_literalness')),
                         sponsor_removable=v(t.get('sponsor_removable')), sponsor_features_used=v(t.get('sponsor_features_used')),
                         completeness=rating(p, 'completeness'), one_sentence=TAG[p].get('one_sentence'),
                         also_won=PROJ[p]['prize_kinds'], devpost=PAGE.get(p, {}).get('url', '')))
write('Q13_sponsor_card_rows.csv', sorted(rows, key=lambda r: (r['hackutd2026_sponsor'], r['placement'])), 'Q13', S,
      'One row per past award from a HackUTD 2026 sponsor: project, placement, pattern, problem owner, literalness, centrality, completeness.')
# ---------------- Q15 cover test ----------------
if COVER:
    for name, G in (('hackutd2025', {'winners': tagged(w25), 'demo_ready': tagged(dr), 'random': tagged(rnd)}),):
        rows = prevalence_table({g: [p for p in ps if p in COVER] for g, ps in G.items()},
                                {'cover_test_score': FEAT['cover_test_score'], 'cover_test_3of3': FEAT['cover_test_3of3']})
        write(f'Q15_cover_{name}.csv', rows, 'Q15', S, 'Cover-test score distribution: HackUTD 2025 winners vs baseline groups.')
    allc = collections.Counter(int(COVER[p]['cover_test_score']) for p in TAG if p in COVER)
    tot = sum(allc.values())
    write('Q15_cover_distribution_all.csv', [dict(score=k, n=allc[k], N=tot, pct=pct(allc[k], tot)) for k in sorted(allc, reverse=True)], 'Q15', S,
          'Cover-test score distribution over every tagged project with a valid cover score (ceiling check).')
    ex = []
    for p in tagged(g1) + tagged(s1):
        if p in COVER and p in PAGE:
            ex.append(dict(project=PROJ[p]['project_name'], group='general_1st' if p in g1 else 'sponsor_1st', score=COVER[p]['cover_test_score'],
                           title=PAGE[p].get('title'), tagline=PAGE[p].get('tagline')))
    write('Q15_cover_examples_1sts.csv', sorted(ex, key=lambda r: -int(r['score'])), 'Q15', S, 'Cover-test score with exact title + tagline for every tagged 1st (best/worst tagline examples).')

# ---------------- Q16 wow moments (text, not video) ----------------
rows = [dict(project=PROJ[p]['project_name'], group='general_1st' if p in g1 else 'sponsor_1st', pattern=T(p, 'pattern'), wow_moment=T(p, 'wow_moment'),
             has_video_embed=PAGE.get(p, {}).get('has_video_embed')) for p in tagged(g1) + tagged(s1) if T(p, 'wow_moment') != 'none_visible']
write('Q16_wow_moments_1sts.csv', rows, 'Q16', S, 'Wow moment (from page text, not video) for every 1st; videos were not watched.')

# ---------------- Q18 Devpost page contents ----------------
P18 = {k: FEAT[k] for k in ('has_video_embed', 'has_arch_diagram', 'n_images', 'page_has_challenges_section', 'page_has_whats_next_section', 'page_has_accomplishments_section')}
write('Q18_page_contents.csv', prevalence_table({'general_1st': tagged(g1), 'sponsor_1st': tagged(s1), 'hackutd2025_winners': tagged(w25),
                                                 'demo_ready': tagged(dr), 'random': tagged(rnd)}, P18), 'Q18', S,
      'Devpost page checklist prevalence: general 1sts, sponsor 1sts, HackUTD 2025 winners vs baseline.')

# ---------------- Q20 recent vs older ----------------
rec = [p for p in winners if PROJ[p]['recent'] == 'True']; old = [p for p in winners if PROJ[p]['recent'] == 'False']
F20 = {k: FEAT[k] for k in ('ai_role', 'has_hardware', 'live_data', 'pattern', 'single_call_wrapper_or_none', 'centerpiece_in_demo_output')}
rows = prevalence_table({'recent': rec, 'older': old}, F20)
for r in rows:
    for g, ps in (('recent', rec), ('older', old)):
        fn = F20[r['feature']]; known = [p for p in ps if fn(p) is not None]
        tw = sum(float(PROJ[p]['weight']) for p in known); hw = sum(float(PROJ[p]['weight']) for p in known if str(fn(p)) == r['value'])
        r[f'{g}_weighted_pct'] = round(100 * hw / tw) if tw else ''
write('Q20_recent_vs_older.csv', rows, 'Q20', S, 'Winners since 2025-06 vs older: ai_role, hardware, live data, pattern (unweighted + event-type weighted).')

# ---------------- Q23 place-but-rarely-1st ----------------
hm_tracks = collections.defaultdict(list)
for a in AW:
    if a['placement'] in ('2', '3', 'HM') and a['track_key'] in tracks: hm_tracks[a['track_key']].append(a['project_id'])
firsts = [p for g in tracks.values() for p in g['1'] if p in TAG]
lowers = [p for ps in hm_tracks.values() for p in ps if p in TAG]
rows = prevalence_table({'first': firsts, 'second_third_HM': lowers}, {k: FEAT[k] for k in ('pattern', 'ai_role', 'novelty_source')})
for r in rows: r['gap_lower_minus_first_pts'] = (r['second_third_HM_pct'] or 0) - (r['first_pct'] or 0)
write('Q23_place_not_first.csv', sorted(rows, key=lambda r: -r['gap_lower_minus_first_pts']), 'Q23', S,
      'In tracks with a published 1st: patterns/ai_roles over-represented among 2nd/3rd/HM vs 1st (association).')

# ---------------- data quality ----------------
rows = []
for f, fn in FEAT.items():
    allp = [p for p in PROJ if p in TAG]
    rows.append(dict(feature=f, N_tagged=len(allp), unknown=sum(fn(p) is None for p in allp), unknown_pct=pct(sum(fn(p) is None for p in allp), len(allp))))
write('Q99_unknown_rates.csv', rows, 'data quality', S, 'Unknown/na rate per field across all tagged projects.')
flush_index(); print('tagged tables written;', len(TAG), 'tagged projects')
