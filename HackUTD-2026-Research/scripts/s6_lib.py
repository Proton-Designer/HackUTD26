"""Shared helpers for S6 compute scripts. Every table carries n and N; cells with N < 5 are flagged low_n."""
import csv, json, pathlib, collections
ROOT = pathlib.Path(__file__).resolve().parents[1]
P, T = ROOT / 'data/processed', ROOT / 'data/tables'
T.mkdir(parents=True, exist_ok=True)
INDEX = []  # (table, question, script, description)

def B(x):
    """CSV booleans -> True/False/None."""
    if x in (True, 'True', 'true', '1', 1): return True
    if x in (False, 'False', 'false', '0', 0): return False
    return None

def load_projects(include_dups=False):
    rows = list(csv.DictReader(open(P / 'projects.csv')))
    return [r for r in rows if include_dups or not r['duplicate_of']]

def load_awards():
    return list(csv.DictReader(open(P / 'awards.csv')))

def load_tags():
    """Joined tag+rating rows keyed by project_id (empty dict if S3 not run yet)."""
    f = ROOT / 'data/tagged/content_all.jsonl'
    if not f.exists(): return {}
    key = {r['blind_id']: r['project_id'] for r in csv.DictReader(open(ROOT / 'data/tagged/blind_key_map.csv'))}
    out = {}
    for l in open(f):
        r = json.loads(l); out[key[r['blind_id']]] = r
    return out

def pct(n, N): return '' if not N else round(100 * n / N)
def cell(n, N): return f'{n} of {N} ({pct(n, N)}%)' + (' low n' if N < 5 else '')

def write(name, rows, question, script, desc):
    if not rows: rows = [{'note': 'no rows'}]
    fields = []
    for r in rows:
        for k in r:
            if k not in fields: fields.append(k)
    with open(T / name, 'w', newline='') as fo:
        w = csv.DictWriter(fo, fieldnames=fields); w.writeheader(); w.writerows(rows)
    INDEX.append((name, question, script, desc))

def prevalence_table(groups, features):
    """groups: {label: [rows]}, features: {name: fn(row)->value or None(unknown)}.
    One row per (feature, value); per group: n, N_known, pct, N_total, unknown."""
    out = []
    for fname, fn in features.items():
        vals = collections.OrderedDict()
        for g, rs in groups.items():
            for r in rs:
                v = fn(r)
                if v is not None: vals.setdefault(str(v), None)
        for v in vals:
            row = {'feature': fname, 'value': v}
            for g, rs in groups.items():
                known = [fn(r) for r in rs if fn(r) is not None]
                n = sum(1 for x in known if str(x) == v)
                row[f'{g}_n'] = n; row[f'{g}_N'] = len(known); row[f'{g}_pct'] = pct(n, len(known))
                row[f'{g}_unknown'] = len(rs) - len(known); row[f'{g}_low_n'] = len(known) < 5
            out.append(row)
    return out

def flush_index():
    f = T / 'INDEX.md'
    old = {}
    if f.exists():
        for line in f.read_text().splitlines():
            if line.startswith('| `'):
                parts = [p.strip() for p in line.strip('|').split('|')]
                old[parts[0].strip('`')] = parts
    for name, q, s, d in INDEX: old[name] = [name, q, f'`{s}`', d]
    L = ['# data/tables index', '', 'Every number in outputs/ must trace to one of these tables.', '',
         '| table | question | script | contents |', '|---|---|---|---|']
    for name in sorted(old):
        p = old[name]; L.append(f'| `{p[0].strip("`")}` | {p[1]} | {p[2]} | {p[3]} |')
    f.write_text('\n'.join(L) + '\n')
