"""S6 Q9: how multi-award projects stack prizes. Uses S0 outputs only.
Tables: Q09_n_awards_dist.csv, Q09_kind_pairs.csv, Q09_general_1st_also_sponsor.csv, Q09_award_concentration.csv
"""
import collections, itertools, statistics
import sys, pathlib; sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from s6_lib import *
S = 'scripts/s6_q09_stacking.py'
proj = {r['project_id']: r for r in load_projects() if r['dataset'] != 'baseline'}
aw = collections.defaultdict(list)
for a in load_awards():
    if a['project_id'] in proj: aw[a['project_id']].append(a)
SPONSOR = {'sponsor_domain', 'sponsor_api_depth', 'sponsor_open'}

def scope(name, pred):
    return name, [p for p in proj.values() if pred(p)]
SCOPES = [scope('all_winners', lambda p: True), scope('hackutd', lambda p: p['event_type'] == 'hackutd'),
          scope('student_24h_inperson', lambda p: p['event_type'] == 'student_24h_inperson'),
          scope('student_36_48h', lambda p: p['event_type'] == 'student_36_48h')]

rows = []
for name, ps in SCOPES:
    c = collections.Counter(min(len(aw[p['project_id']]), 4) for p in ps)
    for k in sorted(c):
        rows.append(dict(scope=name, n_awards='4+' if k == 4 else k, n=c[k], N=len(ps), pct=pct(c[k], len(ps))))
write('Q09_n_awards_dist.csv', rows, 'Q9', S, 'Distribution of awards per winning project, by event type (projects, not awards).')

rows = []
for name, ps in SCOPES:
    multi = [p for p in ps if len(aw[p['project_id']]) >= 2]
    pc = collections.Counter()
    for p in multi:
        kinds = sorted(a['prize_kind'] for a in aw[p['project_id']])
        for x, y in set(itertools.combinations(kinds, 2)): pc[(x, y)] += 1
    for (x, y), n in pc.most_common():
        ex = [p['project_name'] for p in multi if (x, y) in set(itertools.combinations(sorted(a['prize_kind'] for a in aw[p['project_id']]), 2))][:4]
        rows.append(dict(scope=name, kind_a=x, kind_b=y, n_projects=n, N_multi_award=len(multi), pct_of_multi=pct(n, len(multi)),
                         low_n=len(multi) < 5, examples='; '.join(ex)))
write('Q09_kind_pairs.csv', rows, 'Q9', S, 'Prize-kind pairs held by the same project (multi-award projects only).')

rows = []
for name, ps in SCOPES:
    for place in ('1', 'any'):
        g = [p for p in ps if any(a['prize_kind'] == 'general' and (place == 'any' or a['placement'] == place) for a in aw[p['project_id']])]
        alsos = [p for p in g if any(a['prize_kind'] in SPONSOR for a in aw[p['project_id']])]
        alsom = [p for p in g if any(a['prize_kind'] == 'mlh' for a in aw[p['project_id']])]
        alsoside = [p for p in g if any(a['prize_kind'].startswith('side_') for a in aw[p['project_id']])]
        rows.append(dict(scope=name, general_placement=place, N_general=len(g),
                         also_sponsor_n=len(alsos), also_sponsor=cell(len(alsos), len(g)),
                         also_mlh=cell(len(alsom), len(g)), also_side=cell(len(alsoside), len(g)),
                         examples_also_sponsor='; '.join(p['project_name'] for p in alsos[:6])))
write('Q09_general_1st_also_sponsor.csv', rows, 'Q9', S, 'Share of general-track winners (1st / any place) that also won a sponsor, MLH or side prize.')

rows = []
for name, ps in SCOPES:
    counts = sorted((len(aw[p['project_id']]) for p in ps), reverse=True)
    tot = sum(counts); k = max(1, round(len(counts) * 0.10))
    rows.append(dict(scope=name, projects=len(counts), awards=tot, top10pct_projects=k, top10pct_awards=sum(counts[:k]),
                     top10pct_share=pct(sum(counts[:k]), tot), mean_awards=round(tot / len(counts), 2) if counts else '',
                     note='dataset sampled winners per track, so concentration is a lower bound of the real one'))
write('Q09_award_concentration.csv', rows, 'Q9', S, 'Share of all awards held by the top 10% of projects.')

# sponsor-track pairing among projects holding 2+ sponsor prizes (track-slot usage)
rows = []
for name, ps in SCOPES:
    two = [p for p in ps if sum(a['prize_kind'] in SPONSOR for a in aw[p['project_id']]) >= 2]
    pc = collections.Counter()
    for p in two:
        ks = sorted({a['prize_kind'] for a in aw[p['project_id']] if a['prize_kind'] in SPONSOR})
        pc['+'.join(ks) if len(ks) > 1 else ks[0] + ' x2'] += 1
    for k, n in pc.most_common():
        rows.append(dict(scope=name, sponsor_kind_combo=k, n=n, N_two_sponsor=len(two), pct=pct(n, len(two)), low_n=len(two) < 5))
write('Q09_two_sponsor_combos.csv', rows, 'Q9', S, 'Among projects with 2+ sponsor prizes: which sponsor prize kinds they combined.')
flush_index(); print('Q9 tables written')
