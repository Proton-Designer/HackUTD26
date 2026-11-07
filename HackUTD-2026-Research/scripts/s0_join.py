"""S0: join + derive.

In:  04_deep_dives/data/deepdive_all.jsonl, 01_/02_/03_ project_records.jsonl, ALL_PROJECTS_INDEX.csv,
     data/processed/prize_labels_input.jsonl + prize_labels_classified_part*.jsonl (S0a/S0b),
     data/processed/edition_facts_research.json (optional; web-verified event dates/durations),
     data/tagged/blind_key_map.csv (blind ids)
Out: data/processed/projects.csv, awards.csv, editions.csv, unmapped_labels.csv, join_report.md

Derivation rules (spec 2.0.1):
- has_hardware: first-pass has_hardware.
- has_video: deep-dive presentation_assets.has_video, falling back to first-pass has_demo_video when null.
  (Sources disagree: first-pass says video on more projects; both kept as has_video_fp / has_video_dd.)
- n_images: deep-dive screenshot_count, else first-pass n_screenshots.
- has_arch_diagram: deep-dive presentation_assets.has_architecture_diagram.
- n_external_deps: count of first-pass tech_items whose kind is a named external API/service/device
  (ai_model, cloud, data_source, maps_geo, auth, telecom, payments, hardware_part, database);
  frameworks and 'other' excluded.
- event_type/weight/recent: from editions table (see edition_facts()).
- awards: from first-pass prizes[] (structured placement), classified by S0b label lookup.
"""
import json, csv, re, collections, pathlib, datetime
ROOT = pathlib.Path(__file__).resolve().parents[1]
P = ROOT / 'data/processed'

def jl(p): return [json.loads(l) for l in open(p)]
dd = {r['project_id']: r for r in jl(ROOT / '04_deep_dives/data/deepdive_all.jsonl')}
fp, ds_of = {}, {}
for p, ds in [('01_winners', 'winners'), ('02_baseline_non_winners', 'baseline'), ('03_sponsor_tracks', 'sponsor')]:
    for r in jl(ROOT / p / 'data/project_records.jsonl'): fp[r['project_id']] = r; ds_of[r['project_id']] = ds
idx = {r['project_id']: r for r in csv.DictReader(open(ROOT / 'ALL_PROJECTS_INDEX.csv'))}
blind = {r['project_id']: r['blind_id'] for r in csv.DictReader(open(ROOT / 'data/tagged/blind_key_map.csv'))}

# ---------------- editions ----------------
ALIAS = {  # (hackathon, edition) -> canonical edition key
    ('Cal Hacks', 'Cal Hacks 13.0'): 'Cal Hacks 13.0 (2026)',
    ('DubHacks', "DubHacks '26"): 'DubHacks 2026',
    ('HackTX', '2026'): 'HackTX 2026',
    ('HooHacks', '2025'): 'HooHacks 2025',
    ('PennApps', 'PennApps XXV'): 'PennApps XXV (Fall 2024)',
    ('PennApps', 'PennApps XXVI'): 'PennApps XXVI (Fall 2025)',
    ('HackPrinceton', 'Spring 2025'): 'HackPrinceton Spring 2025',
    ('VTHacks', 'VTHacks 13'): 'VTHacks - 13', ('VTHacks', 'VTHacks 14'): 'VTHacks - 14',
    ('SwampHacks', 'SwampHacks XI'): 'SwampHacks - XI', ('SwampHacks', 'SwampHacks XII'): 'SwampHacks - XII',
    ('HackRPI', '2025'): 'HackRPI - 2025',
    ('HackNYU', '2025'): 'HackNYU - 2025',
    ('UC Berkeley AI Hackathon', '2025'): 'UC Berkeley AI Hackathon 2025',
    ('WEHack 2026', 'WEHack 2026'): 'WEHack 2026',
    ('UofTHacks', 'UofTHacks - 13'): 'UofTHacks 13',
}
HACK_ALIAS = {'WEHack 2026': 'WEHack', 'UXperience 2025': 'UXperience'}
CORPORATE = {'HP & NVIDIA Developer Challenge', 'Agentic AI Unleashed: AWS & NVIDIA Hackathon',
             'Building the Next-Gen Agentic App with GraphRAG & NVIDIA cuGraph (ArangoDB)',
             'DevNetwork [AI + ML] Hackathon'}
OTHER = {'NemoClaw NVIDIA x ASUS Hackathon @ UCSC', 'UXperience 2025'}  # 1-day / design-only formats
WEIGHT = {'hackutd': 3, 'student_24h_inperson': 2, 'student_36_48h': 1}

def ekey(h, e): return ALIAS.get((h, e), e)

research = {}
rp = P / 'edition_facts_research.json'
if rp.exists():
    for r in json.load(open(rp)): research[(r['hackathon'], r['edition'])] = r

def d(s):
    try: return datetime.date.fromisoformat(s) if s else None
    except Exception: return None

editions = collections.OrderedDict()
for pid, r in dd.items():
    f = fp[pid]; h, e = r['hackathon'], r['edition']; k = (HACK_ALIAS.get(h, h), ekey(h, e))
    E = editions.setdefault(k, dict(hackathon=k[0], edition_key=k[1], aliases=set(), fp_start=set(), fp_end=set(), n=0))
    E['aliases'].add(e); E['n'] += 1
    if f.get('event_start'): E['fp_start'].add(f['event_start'])
    if f.get('event_end'): E['fp_end'].add(f['event_end'])

def edition_facts(E):
    """Resolve start/end/hours/format/event_type with a recorded basis."""
    res = [research[(h, a)] for a in E['aliases'] for h in (E['hackathon'], *[x for x, y in HACK_ALIAS.items() if y == E['hackathon']])
           if (h, a) in research]
    res = sorted(res, key=lambda r: {'this_edition': 0, 'adjacent_edition': 1}.get(r.get('basis'), 2))
    start = end = hours = None; fmt = 'unknown'; basis = []
    if res and (res[0].get('start') or res[0].get('hours')):
        R = res[0]; start, end, hours, fmt = d(R.get('start')), d(R.get('end')), R.get('hours'), R.get('format') or 'unknown'
        basis.append('web:' + (R.get('basis') or '?'))
    if not start and E['fp_start']:
        start = d(sorted(E['fp_start'])[0]); end = end or d(sorted(E['fp_end'])[-1]) if E['fp_end'] else end
        basis.append('first_pass_dates')
    span = (end - start).days if start and end else None
    if hours is None and span is not None:
        hours_basis = {0: 24, 1: 24}.get(span, 36 if span == 2 else None)
        if hours_basis: hours = hours_basis; basis.append(f'hours_from_date_span({span}d)')
    h = E['hackathon']
    if h == 'HackUTD': et = 'hackutd'
    elif h in CORPORATE: et = 'corporate_or_mlh_online'
    elif h in OTHER or h + ' 2025' in OTHER: et = 'other'
    elif fmt == 'virtual': et = 'virtual'
    elif hours is None: et = 'unknown_duration'
    elif hours <= 26: et = 'student_24h_inperson'
    elif hours <= 50: et = 'student_36_48h'
    else: et = 'other'
    return dict(start=start.isoformat() if start else '', end=end.isoformat() if end else '', hours=hours or '',
                format=fmt, event_type=et, weight=WEIGHT.get(et, 0.5 if et != 'unknown_duration' else 1),
                recent=(start >= datetime.date(2025, 6, 1)) if start else '', basis='; '.join(basis) or 'none')

for E in editions.values(): E.update(edition_facts(E))

# ---------------- awards ----------------
lab_in = {r['label_id']: r for r in jl(P / 'prize_labels_input.jsonl')}
lab_out = {}
for p in sorted(P.glob('prize_labels_classified_part*.jsonl')):
    for r in jl(p): lab_out[r['label_id']] = r
import hashlib
def label_id(h, p):
    parts = (h, p.get('prize') or '', p.get('category_as_awarded') or '', str(p.get('placement')))
    return hashlib.sha1('||'.join(parts).encode()).hexdigest()[:12]

KINDS = {'general', 'theme_track', 'sponsor_domain', 'sponsor_api_depth', 'sponsor_open', 'side_design', 'side_hardware',
         'side_social_impact', 'side_beginner', 'mlh', 'peoples_choice', 'other'}
INDS = {'telecom', 'finance_banking', 'insurance', 'real_estate', 'energy', 'auto_mobility', 'geospatial_ar', 'ai_compute',
        'security_privacy', 'identity_auth', 'cloud_devtools', 'retail', 'health', 'legal', 'other', 'none'}
PLACES = {'1', '2', '3', 'HM', 'unranked'}
OVERRIDE_2026 = {  # manual resolutions, logged in join_report
    ('HackUTD', 'Toyota'): 'Toyota Financial Services',   # HackUTD "Toyota" track; TFS is the 2025/2026 Toyota sponsor (assumed)
}
awards, unmapped, problems = [], [], []
for pid, f in fp.items():
    if ds_of[pid] == 'baseline': continue
    for i, p in enumerate(f['prizes']):
        lid = label_id(f['hackathon'], p); o = lab_out.get(lid)
        if not o: problems.append(f'no label classification for {pid} #{i}'); continue
        if o.get('confidence') == 'low' or o.get('note'):
            unmapped.append(dict(label_id=lid, hackathon=f['hackathon'], prize=p.get('prize'), confidence=o.get('confidence'),
                                 note=o.get('note'), example_project=pid))
        for j, a in enumerate(o['awards']):
            s26 = (a.get('hackutd2026_sponsor') if str(a.get('hackutd2026_sponsor')).lower() not in ('none', 'null', '') else None) or OVERRIDE_2026.get((f['hackathon'], a.get('sponsor')))
            bad = [k for k, ok in [('placement', a['placement'] in PLACES), ('prize_kind', a['prize_kind'] in KINDS),
                                   ('sponsor_industry', a['sponsor_industry'] in INDS)] if not ok]
            if bad: problems.append(f'{pid}: invalid {bad} in label {lid}')
            awards.append(dict(project_id=pid, award_idx=f'{i}.{j}', prize_label=p.get('prize'), prize_name=a['prize_name'],
                               placement=a['placement'], prize_kind=a['prize_kind'], sponsor=a.get('sponsor') or '',
                               sponsor_industry=a['sponsor_industry'], hackutd2026_sponsor=s26 or '',
                               label_confidence=o.get('confidence'), label_id=lid))

# ---------------- corrections (data/processed/corrections.csv; inputs stay read-only) ----------------
CORR = list(csv.DictReader(open(P / 'corrections.csv'))) if (P / 'corrections.csv').exists() else []
drop_aw = {(c['project_id'], c['award_idx']) for c in CORR if c['action'] == 'drop_award'}
excluded = {c['project_id']: c['reason'] for c in CORR if c['action'] == 'exclude_project'}
awards = [a for a in awards if (a['project_id'], a['award_idx']) not in drop_aw and a['project_id'] not in excluded]

# ---------------- track keys + paired sets ----------------
PLACE_WORDS = re.compile(r'\b(1st|2nd|3rd|4th|first|second|third|place|prize|winner|overall|runner[- ]?up|grand)\b|[\[\]\(\)\-–—:|,]', re.I)
def track_key(a, edition_key):
    if a['prize_kind'] == 'general': return f'{edition_key}|general'
    if a['sponsor']: return f"{edition_key}|sponsor:{a['sponsor'].lower()}|{a['prize_kind']}"
    return f"{edition_key}|{a['prize_kind']}:{re.sub(r'\s+', ' ', PLACE_WORDS.sub(' ', a['prize_name'].lower())).strip()}"
proj_edition = {pid: (HACK_ALIAS.get(dd[pid]['hackathon'], dd[pid]['hackathon']), ekey(dd[pid]['hackathon'], dd[pid]['edition'])) for pid in dd}
for a in awards: a['track_key'] = track_key(a, ' / '.join(proj_edition[a['project_id']]))
dup = {pid for pid, r in dd.items() if r.get('duplicate_of')} | set(excluded)
by_track = collections.defaultdict(set)
for a in awards:
    if a['project_id'] not in dup and a['placement'] in ('1', '2', '3'): by_track[a['track_key']].add(a['placement'])
paired_tracks = {t for t, s in by_track.items() if '1' in s and ({'2', '3'} & s)}
for a in awards: a['in_paired_set'] = a['track_key'] in paired_tracks and a['placement'] in ('1', '2', '3')

# ---------------- projects ----------------
DEP_KINDS = {'ai_model', 'cloud', 'data_source', 'maps_geo', 'auth', 'telecom', 'payments', 'hardware_part', 'database'}
aw_by = collections.defaultdict(list)
for a in awards: aw_by[a['project_id']].append(a)
def rank(p): return {'1': 1, '2': 2, '3': 3, 'HM': 4, 'unranked': 5}.get(p, 6)
rows = []
for pid, r in dd.items():
    f = fp[pid]; pa = r.get('presentation_assets') or {}; E = editions[proj_edition[pid]]
    aws = aw_by.get(pid, [])
    hv_dd, hv_fp = pa.get('has_video'), f.get('has_demo_video')
    gen = [a for a in aws if a['prize_kind'] == 'general']
    rows.append(dict(
        project_id=pid, blind_id=blind[pid], dataset=ds_of[pid], sample_group=f.get('sample_group', ''),
        project_name=r['project_name'], hackathon=E['hackathon'], edition_key=E['edition_key'], edition_raw=r['edition'],
        event_date=E['start'], event_type=E['event_type'], weight=E['weight'], recent=E['recent'],
        placement_tier=r.get('placement_tier'), n_awards=len(aws),
        best_placement=min([a['placement'] for a in aws], key=rank) if aws else '',
        general_placement=min([a['placement'] for a in gen], key=rank) if gen else '',
        prize_kinds=json.dumps(sorted({a['prize_kind'] for a in aws})),
        sponsors=json.dumps(sorted({a['sponsor'] for a in aws if a['sponsor']})),
        sponsor_industries=json.dumps(sorted({a['sponsor_industry'] for a in aws if a['sponsor_industry'] != 'none'})),
        hackutd2026_sponsors=json.dumps(sorted({a['hackutd2026_sponsor'] for a in aws if a['hackutd2026_sponsor']})),
        has_hardware=f.get('has_hardware'), has_video=hv_dd if hv_dd is not None else hv_fp, has_video_dd=hv_dd, has_video_fp=hv_fp,
        has_live_demo=pa.get('has_live_demo') if pa.get('has_live_demo') is not None else f.get('has_live_demo'),
        n_images=pa.get('screenshot_count') if pa.get('screenshot_count') is not None else f.get('n_screenshots'),
        has_arch_diagram=pa.get('has_architecture_diagram'),
        n_external_deps=sum(1 for t in f.get('tech_items') or [] if t.get('kind') in DEP_KINDS),
        n_tech_items=len(f.get('tech_items') or []),
        ai_used=f.get('ai_used'), ai_types=json.dumps(f.get('ai_types') or []),
        n_sponsor_tools_core=sum(1 for s in r.get('sponsor_tool_use') or [] if s.get('depth') == 'core'),
        n_features=len(r.get('core_features') or []),
        n_features_shown_working=sum(1 for c in r.get('core_features') or [] if c.get('working_status') == 'shown_working'),
        n_features_planned=sum(1 for c in r.get('core_features') or [] if c.get('working_status') == 'planned'),
        n_user_flow_steps=len(r.get('user_flow') or []),
        readme_quality=f.get('readme_quality'), writeup_length=f.get('writeup_length'),
        writeup_sections=json.dumps(f.get('writeup_sections') or []), has_impact_claims=f.get('has_impact_claims'),
        team_size=f.get('team_size'), commits_in_window_share=f.get('share_commits_in_window', ''),
        evidence_depth=(r.get('evidence') or {}).get('depth'), confidence=r.get('confidence'),
        duplicate_of=r.get('duplicate_of') or ('EXCLUDED: ' + excluded[pid] if pid in excluded else ''), second_pass_flag=r.get('second_pass_flag'),
        prompt_text_found=r.get('prompt_text_found'),
        s_hackutd=E['event_type'] == 'hackutd' and ds_of[pid] != 'baseline',
        s_baseline=ds_of[pid] == 'baseline',
        s_paired=any(a['in_paired_set'] for a in aws),
        s_multi_award=len(aws) >= 2,
        s_24h_general_1st=E['event_type'] == 'student_24h_inperson' and any(a['prize_kind'] == 'general' and a['placement'] == '1' for a in aws),
    ))
for x in rows: x['s_priority'] = any(x[k] for k in ('s_hackutd', 's_baseline', 's_paired', 's_multi_award', 's_24h_general_1st'))

def wcsv(name, recs, fields=None):
    fields = fields or list(recs[0].keys())
    with open(P / name, 'w', newline='') as fo:
        w = csv.DictWriter(fo, fieldnames=fields); w.writeheader(); w.writerows(recs)
wcsv('projects.csv', rows); wcsv('awards.csv', awards)
wcsv('editions.csv', [dict(hackathon=E['hackathon'], edition_key=E['edition_key'], aliases=json.dumps(sorted(E['aliases'])),
                           n_projects=E['n'], start=E['start'], end=E['end'], hours=E['hours'], format=E['format'],
                           event_type=E['event_type'], weight=E['weight'], recent=E['recent'], basis=E['basis'])
                      for E in editions.values()])
wcsv('unmapped_labels.csv', unmapped or [dict(label_id='', hackathon='', prize='', confidence='', note='', example_project='')])

# ---------------- report ----------------
C = collections.Counter
nd = [x for x in rows if not x['duplicate_of']]
L = ['# S0 join report', '', f'Generated by `scripts/s0_join.py` on {datetime.date.today()}.', '',
     '## Counts', f'- projects: {len(rows)} ({dict(C(x["dataset"] for x in rows))}); duplicates collapsed (duplicate_of set): {len(dup)} -> {len(nd)} counted',
     f'- awards: {len(awards)} from {len({a["project_id"] for a in awards})} winner projects; first-pass prize entries without a label classification: {sum("no label" in p for p in problems)}',
     f'- schema problems: {len([p for p in problems if "invalid" in p])}', '',
     '## Award placement coverage', *[f'- {k}: {v}' for k, v in sorted(C(a["placement"] for a in awards).items())], '',
     '## prize_kind', *[f'- {k}: {v}' for k, v in C(a["prize_kind"] for a in awards).most_common()], '',
     '## HackUTD 2026 sponsors among past awards', *[f'- {k}: {v}' for k, v in C(a["hackutd2026_sponsor"] for a in awards if a["hackutd2026_sponsor"]).most_common()], '',
     '## Event types (projects, duplicates excluded)', *[f'- {k}: {v}' for k, v in C(x["event_type"] for x in nd).most_common()], '',
     '## Edition date/duration basis', *[f'- {k}: {v}' for k, v in C(E["basis"].split(";")[0] for E in editions.values()).most_common()], '',
     '## Strata (duplicates excluded)',
     *[f'- {k}: {sum(1 for x in nd if x[k])}' for k in ('s_hackutd', 's_baseline', 's_paired', 's_multi_award', 's_24h_general_1st', 's_priority')],
     f'- paired tracks (published 1st + 2nd/3rd in same event+track): {len(paired_tracks)}', '',
     f'## Corrections applied: {len(CORR)} (data/processed/corrections.csv)', *[f"- {c['project_id']}: {c['action']} {c['award_idx']} — {c['reason']}" for c in CORR], '',
     '## Manual resolutions', '- HackUTD "Toyota" track -> hackutd2026_sponsor = Toyota Financial Services (assumed: TFS is the Toyota entity sponsoring HackUTD 2025/2026).',
     '- prize_kind `theme_track` added to the spec enum: organizer-run themed categories (Healthcare Track etc.) that are neither general nor sponsor prizes.',
     '- event_type `unknown_duration` used where no source gives the edition length (weight 1, excluded from 24h-only views).', '',
     f'## Labels needing review: {len(unmapped)} (see unmapped_labels.csv)', '',
     '## Problems', *([f'- {p}' for p in problems[:50]] or ['- none'])]
(P / 'join_report.md').write_text('\n'.join(L) + '\n')
print('\n'.join(L[:40]))
