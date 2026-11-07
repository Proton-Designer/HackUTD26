"""S2: stratified 30-project pilot sample (seeded). Out: data/tagged/pilot/pilot_input.jsonl, pilot_ids.csv"""
import json, csv, random, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[1]
dd = {json.loads(l)['project_id']: json.loads(l) for l in open(ROOT / '04_deep_dives/data/deepdive_all.jsonl')}
bl = {json.loads(l)['project_id']: json.loads(l) for l in open(ROOT / '02_baseline_non_winners/data/project_records.jsonl')}
key = {r['project_id']: r['blind_id'] for r in csv.DictReader(open(ROOT / 'data/tagged/blind_key_map.csv'))}
blind = {json.loads(l)['blind_id']: json.loads(l) for l in open(ROOT / 'data/tagged/blind_inputs.jsonl')}
rng = random.Random(20261106)
def pick(pred, n):
    pool = sorted(p for p, d in dd.items() if pred(p, d) and not d.get('duplicate_of'))
    return rng.sample(pool, n)
hu = lambda d: d['hackathon'] == 'HackUTD'
strata = {
  'hackutd_winner': pick(lambda p, d: hu(d) and d['dataset'] != 'baseline', 6),
  'baseline_demo_ready': pick(lambda p, d: d['dataset'] == 'baseline' and bl[p]['sample_group'] == 'demo_ready', 3),
  'baseline_random': pick(lambda p, d: d['dataset'] == 'baseline' and bl[p]['sample_group'] == 'random', 3),
  'other_overall_top3': pick(lambda p, d: not hu(d) and d['placement_tier'] == 'overall_top3', 6),
  'other_sponsor_winner': pick(lambda p, d: not hu(d) and d['placement_tier'] == 'sponsor_winner', 6),
  'other_track_or_hm': pick(lambda p, d: not hu(d) and d['placement_tier'] in ('track_winner', 'honorable_or_finalist'), 6),
}
ids = [(s, p) for s, ps in strata.items() for p in ps]
rng.shuffle(ids)
out = ROOT / 'data/tagged/pilot'; out.mkdir(parents=True, exist_ok=True)
with open(out / 'pilot_input.jsonl', 'w') as f:
    for s, p in ids: f.write(json.dumps(blind[key[p]], ensure_ascii=False) + '\n')
with open(out / 'pilot_ids.csv', 'w', newline='') as f:
    w = csv.writer(f); w.writerow(['blind_id', 'project_id', 'stratum'])
    for s, p in ids: w.writerow([key[p], p, s])
print(len(ids), 'pilot projects')
