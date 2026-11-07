"""S4b QA: flag glance shards whose answers ignore the tagline (image-only answers). Run before scoring.
A shard with > 5 such answers is re-run with the text-first rule."""
import json, glob, re, pathlib
D = pathlib.Path(__file__).resolve().parents[1] / 'data/tagged/cover'
for gf in sorted(D.glob('shard_*_glance.jsonl')):
    sid = gf.name.split('_glance')[0]
    ins = {json.loads(l)['blind_id']: json.loads(l) for l in open(D / f'{sid}_in.jsonl')}
    G = [json.loads(l) for l in open(gf)]
    bad = sum(1 for g in G if re.search(r'unclear|cover is|logo|icon|not shown|not stated|no product|nothing project|abstract', g['what'], re.I) and len(ins[g['blind_id']].get('tagline') or '') > 25)
    print(sid, len(G), 'of', len(ins), 'image-only answers despite tagline:', bad, 'RERUN' if bad > 5 else 'ok')
