"""S2/S3/S4a input builder: blind, scrubbed per-project inputs for taggers/raters.

Blindness rules (spec 2.4, pipeline principle 6):
- No placement, prizes, dataset, sample_group, project_id prefixes, URLs, evidence source paths.
- Same whitelisted fields for every dataset (so field presence can't reveal the group).
- Free text: sentences mentioning winning/prizes/placement are dropped (LEAK regex).
- 'Sponsor tracks considered' comes from prompt_fit.targeted_prizes for EVERY project
  (winners and non-winners alike), reduced to sponsor/track names.

Out: data/tagged/blind_inputs.jsonl  (key = opaque blind_id)
     data/tagged/blind_key_map.csv   (blind_id -> project_id; NOT given to taggers)
"""
import json, re, hashlib, csv, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[1]
def load(p): return {json.loads(l)['project_id']: json.loads(l) for l in open(ROOT / p)}
dd = load('04_deep_dives/data/deepdive_all.jsonl')
fp = {}
for p in ['01_winners/data/project_records.jsonl', '02_baseline_non_winners/data/project_records.jsonl',
          '03_sponsor_tracks/data/project_records.jsonl']:
    fp.update(load(p))

LEAK = re.compile(r"\b(won|wins?|winner|winners|winning|placed|placing|placement|prizes?|awards?|awarded|finalists?|"
                  r"honou?rable|1st|2nd|3rd|4th|first[- ]place|second[- ]place|third[- ]place|runner[- ]?up|"
                  r"grand prize|judges? (chose|picked|selected)|non[- ]?winner|baseline|demo_ready|sample)\b", re.I)
SENT = re.compile(r'(?<=[.!?;])\s+')

def scrub_text(s):
    if not isinstance(s, str): return s
    kept = [x for x in SENT.split(s) if not LEAK.search(x)]
    return ' '.join(kept) if kept else '[redacted]'

def scrub(o):
    if isinstance(o, str): return scrub_text(o)
    if isinstance(o, list):
        out = [scrub(x) for x in o]
        return [x for x in out if x != '[redacted]']
    if isinstance(o, dict): return {k: scrub(v) for k, v in o.items()}
    return o

TRACK_TOKEN = re.compile(r"\b(winners?|won|wins?|prizes?|awards?|\[?\d(st|nd|rd|th)\]?|first|second|third|place|"
                         r"runner[- ]?up|finalists?|honou?rable mention)\b|\[|\]|\(\s*\)", re.I)
def tracks_considered(d):
    tp = ((d.get('prompt_fit') or {}).get('targeted_prizes')) or []
    out = []
    for t in tp:
        for part in re.split(r';', str(t)):
            x = re.sub(r'\s+', ' ', TRACK_TOKEN.sub(' ', part)).strip(' -:,.')
            if x and x.lower() not in {'general', 'general track'}: out.append(x)
    return sorted(set(out))

DD_FIELDS = ['project_name', 'hackathon', 'edition', 'what_it_is', 'problem_and_user', 'core_features', 'user_flow',
             'prompt_text_found', 'prompt_summary', 'sponsor_tool_use', 'ai_approach', 'architecture', 'novelty_notes',
             'scope_and_completeness', 'claims', 'presentation_assets', 'repo_signals']
FP_FIELDS = ['one_line_pitch', 'problem_statement', 'target_user', 'domain_primary', 'domain_secondary', 'idea_type',
             'distinctive_notes', 'platforms', 'has_hardware', 'ai_used', 'ai_types', 'tech_items', 'sponsor_apis_used',
             'sponsor_fit_note', 'has_demo_video', 'has_live_demo', 'n_screenshots', 'ui_polish', 'readme_quality',
             'writeup_sections', 'writeup_length', 'has_impact_claims', 'impact_claims_note', 'team_size']

# Devpost page text (S1b), if fetched: title, tagline, description sections, built-with. Badges/submitted_to excluded.
pages = {}
pf = ROOT / 'data/pages/page_facts.jsonl'
if pf.exists():
    for l in open(pf):
        x = json.loads(l)
        if x.get('status') == 'ok': pages[x['project_id']] = x
def devpost_text(pid):
    x = pages.get(pid)
    if not x: return None
    secs, budget = [], 6000
    for sct in x.get('sections') or []:
        if LEAK.search(sct.get('heading') or '') or re.search(r'prize|award|track|recogni', sct.get('heading') or '', re.I): continue
        t = scrub_text(sct.get('text') or '')[:1500]
        if re.search(r'grand ?prize', t, re.I): continue
        if budget <= 0: break
        secs.append({'heading': sct.get('heading'), 'text': t[:budget]}); budget -= len(t)
    return {'title': x.get('title'), 'tagline': scrub_text(x.get('tagline')), 'sections': secs,
            'built_with': x.get('built_with'), 'has_video_embed': x.get('has_video_embed'),
            'n_gallery_items': x.get('n_gallery_items')}

rows, keymap = [], []
for pid, d in dd.items():
    f = fp.get(pid, {})
    bid = 'P' + hashlib.sha1(('blind-salt-2026|' + pid).encode()).hexdigest()[:10]
    rec = {'blind_id': bid}
    for k in DD_FIELDS: rec[k] = scrub(d.get(k))
    pf = d.get('prompt_fit') or {}
    rec['prompt_fit'] = {'how_it_answers_prompt': scrub(pf.get('how_it_answers_prompt')), 'evidence': pf.get('evidence')}
    rec['sponsor_tracks_considered'] = tracks_considered(d)
    ev = d.get('evidence') or {}
    rec['evidence_depth'] = ev.get('depth'); rec['evidence_gaps'] = scrub(ev.get('gaps'))
    rec['record_confidence'] = d.get('confidence')
    for k in FP_FIELDS: rec[k] = scrub(f.get(k))
    rec['devpost_page'] = devpost_text(pid)
    rows.append(rec); keymap.append((bid, pid))

out = ROOT / 'data/tagged'; out.mkdir(parents=True, exist_ok=True)
with open(out / 'blind_inputs.jsonl', 'w') as fo:
    for r in rows: fo.write(json.dumps(r, ensure_ascii=False) + '\n')
with open(out / 'blind_key_map.csv', 'w', newline='') as fo:
    w = csv.writer(fo); w.writerow(['blind_id', 'project_id']); w.writerows(keymap)
# leak audit
leaks = sum(1 for r in rows if LEAK.search(json.dumps({k: v for k, v in r.items() if k not in ('project_name',)})))
print(len(rows), 'blind inputs; with devpost page:', sum(1 for r in rows if r['devpost_page']), '; rows with residual leak words:', leaks, '; distinct ids:', len({r['blind_id'] for r in rows}))
