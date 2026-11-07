"""S3: shard blind inputs for tag+rate agents.
Priority strata (HackUTD winners, HackUTD 2025 baseline, paired sets, multi-award, 24h general 1sts) -> Opus shards;
everything else -> Sonnet shards. Duplicates/excluded projects are skipped.
Out: data/tagged/content/shard_<model>_<NN>_in.jsonl + data/tagged/content/shards.csv
"""
import json, csv, pathlib, sys
ROOT = pathlib.Path(__file__).resolve().parents[1]
SIZE = int(sys.argv[1]) if len(sys.argv) > 1 else 30
proj = {r['blind_id']: r for r in csv.DictReader(open(ROOT / 'data/processed/projects.csv'))}
rows = [json.loads(l) for l in open(ROOT / 'data/tagged/blind_inputs.jsonl')]
rows = [r for r in rows if not proj[r['blind_id']]['duplicate_of']]
pri = [r for r in rows if proj[r['blind_id']]['s_priority'] == 'True']
rest = [r for r in rows if proj[r['blind_id']]['s_priority'] != 'True']
out = ROOT / 'data/tagged/content'; out.mkdir(parents=True, exist_ok=True)
man = []
# Overnight run decision: every shard is tagged by Sonnet (pilot round 2 showed Opus~Sonnet agreement; single
# model removes the model-by-stratum confound). Priority shards are numbered first so they finish first.
groups = (('pri', sorted(pri, key=lambda r: r['blind_id'])), ('rest', sorted(rest, key=lambda r: r['blind_id'])))
for model, rs in groups:
    for i in range(0, len(rs), SIZE):
        name = f'shard_{model}_{i // SIZE:02d}'
        with open(out / f'{name}_in.jsonl', 'w') as f:
            for r in rs[i:i + SIZE]: f.write(json.dumps(r, ensure_ascii=False) + '\n')
        man.append(dict(shard=name, model=model, n=len(rs[i:i + SIZE])))
with open(out / 'shards.csv', 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=['shard', 'model', 'n']); w.writeheader(); w.writerows(man)
print(len(pri), 'priority ->', sum(m['model'] == 'pri' for m in man), 'shards;', len(rest), 'rest ->',
      sum(m['model'] == 'rest' for m in man), 'shards')
