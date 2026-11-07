"""S0a: extract distinct prize labels (with hackathon context) for classification.
Out: data/processed/prize_labels_input.jsonl  (one row per distinct label key)
"""
import json, hashlib, collections, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[1]
def load(p): return [json.loads(l) for l in open(ROOT / p)]
recs = load('01_winners/data/project_records.jsonl') + load('03_sponsor_tracks/data/project_records.jsonl')
rows = collections.OrderedDict()
for r in recs:
    for p in r['prizes']:
        key_parts = (r['hackathon'], p.get('prize') or '', p.get('category_as_awarded') or '', str(p.get('placement')))
        k = hashlib.sha1('||'.join(key_parts).encode()).hexdigest()[:12]
        if k not in rows:
            rows[k] = dict(label_id=k, hackathon=r['hackathon'], prize=key_parts[1],
                           category_as_awarded=key_parts[2], placement_field=key_parts[3],
                           record_sponsors=r.get('sponsors'), n_projects=0, example_project=r['project_name'])
        rows[k]['n_projects'] += 1
out = ROOT / 'data/processed/prize_labels_input.jsonl'
with open(out, 'w') as f:
    for v in rows.values(): f.write(json.dumps(v) + '\n')
print(len(rows), 'distinct label keys ->', out)
