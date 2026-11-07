"""S4b: shard cover inputs for blind glance agents; priority strata first. Out: data/tagged/cover/shard_XX_in.jsonl"""
import json, csv, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[1]
pri = {r['blind_id']: r['s_priority'] == 'True' for r in csv.DictReader(open(ROOT / 'data/processed/projects.csv'))}
rows = [json.loads(l) for l in open(ROOT / 'data/pages/cover_inputs.jsonl')]
rows.sort(key=lambda r: (not pri.get(r['blind_id'], False), r['blind_id']))
out = ROOT / 'data/tagged/cover'; out.mkdir(parents=True, exist_ok=True)
SIZE = 85
for i in range(0, len(rows), SIZE):
    with open(out / f'shard_{i // SIZE:02d}_in.jsonl', 'w') as f:
        for r in rows[i:i + SIZE]: f.write(json.dumps({k: r[k] for k in ('blind_id', 'title', 'tagline', 'image_file')}, ensure_ascii=False) + '\n')
print(len(rows), 'rows ->', (len(rows) + SIZE - 1) // SIZE, 'shards')
