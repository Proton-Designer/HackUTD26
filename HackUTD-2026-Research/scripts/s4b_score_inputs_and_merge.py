"""S4b: (mode 'build') pair glance answers with trimmed blind records into scorer shards;
(mode 'merge') validate + merge scorer outputs into data/tagged/cover_test.jsonl.
Usage: python3 scripts/s4b_score_inputs_and_merge.py build|merge
"""
import json, sys, pathlib, glob
ROOT = pathlib.Path(__file__).resolve().parents[1]; D = ROOT / 'data/tagged/cover'
mode = sys.argv[1]
blind = {json.loads(l)['blind_id']: json.loads(l) for l in open(ROOT / 'data/tagged/blind_inputs.jsonl')}
KEEP = ['what_it_is', 'problem_and_user', 'one_line_pitch', 'target_user', 'problem_statement']
def trim(r):
    out = {k: r.get(k) for k in KEEP}
    dp = r.get('devpost_page') or {}
    out['devpost_tagline'] = dp.get('tagline')
    out['devpost_first_sections'] = [s['text'][:700] for s in (dp.get('sections') or [])[:2]]
    return out
if mode == 'build':
    n = 0
    for gf in sorted(D.glob('shard_*_glance.jsonl')):
        sid = gf.name.split('_glance')[0]
        if (D / f'{sid}_score_in.jsonl').exists() and '--force' not in sys.argv: continue
        ins = [json.loads(l)['blind_id'] for l in open(D / f'{sid}_in.jsonl')]
        g = {json.loads(l)['blind_id']: json.loads(l) for l in open(gf)}
        missing = [b for b in ins if b not in g]
        if missing: print(sid, 'incomplete, skipped'); continue
        with open(D / f'{sid}_score_in.jsonl', 'w') as f:
            for b in ins:
                if b in g: f.write(json.dumps({'blind_id': b, 'glance': {k: g[b].get(k) for k in ('what', 'for_whom', 'why', 'image_helped')}, 'record': trim(blind[b])}, ensure_ascii=False) + '\n'); n += 1
        print(sid, 'glance rows', len(g), 'missing', len(missing))
    print('score inputs:', n)
else:
    out, bad = [], []
    for sf in sorted(D.glob('shard_*_score_out.jsonl')):
        for l in open(sf):
            r = json.loads(l)
            pts = [r.get(k) for k in ('what_pt', 'whom_pt', 'why_pt')]
            if all(p in (0, 1) for p in pts) and r.get('cover_test_score') == sum(pts): out.append(r)
            else: bad.append(r.get('blind_id'))
    gl = {}
    for gf in D.glob('shard_*_glance.jsonl'):
        for l in open(gf): x = json.loads(l); gl[x['blind_id']] = x
    # QA exclusion: glance answers that ignored a substantive tagline (image-only answers) are dropped,
    # not scored (see s4b_check_glance.py; shard 05 kept 13 such rows after its rerun).
    import re
    tag = {json.loads(l)['blind_id']: json.loads(l).get('tagline') or '' for l in open(ROOT / 'data/pages/cover_inputs.jsonl')}
    bad_glance = {b for b, g in gl.items() if re.search(r'unclear|cover is|logo|icon|not shown|not stated|no product|nothing project|abstract', g.get('what') or '', re.I) and len(tag.get(b, '')) > 25}
    n0 = len(out); out = [r for r in out if r['blind_id'] not in bad_glance]
    print('excluded image-only glance rows:', n0 - len(out))
    with open(ROOT / 'data/tagged/cover_test.jsonl', 'w') as f:
        for r in out: r['image_helped'] = gl.get(r['blind_id'], {}).get('image_helped'); f.write(json.dumps(r) + '\n')
    from collections import Counter
    print('merged', len(out), 'invalid', len(bad), Counter(r['cover_test_score'] for r in out))
