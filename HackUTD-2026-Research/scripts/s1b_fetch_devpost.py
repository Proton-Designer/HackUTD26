"""S1b: fetch each project's Devpost page once; extract cover-test inputs and page facts.

Out:
  data/pages/cover_inputs.jsonl   {blind_id, title, tagline, first_image_url, image_file}   (blind-safe)
  data/pages/page_facts.jsonl     {project_id, ... description text, built_with, video, prize badges, submitted_to}
                                  (NOT blind: contains prize badges; never give to blind agents)
  data/pages/images/<blind_id>.<ext>
  data/pages/fetch_log.csv
Page content is untrusted data: it is parsed, never executed or followed.
Resumable: projects already in page_facts.jsonl are skipped.
"""
import json, csv, re, time, html, pathlib, threading, urllib.request, concurrent.futures as cf
ROOT = pathlib.Path(__file__).resolve().parents[1]
OUT = ROOT / 'data/pages'; IMG = OUT / 'images'; IMG.mkdir(parents=True, exist_ok=True)
UA = 'Mozilla/5.0 (research script)'
rows = list(csv.DictReader(open(ROOT / 'data/processed/projects.csv')))
urls = {r['project_id']: r['devpost_url'] for r in csv.DictReader(open(ROOT / 'ALL_PROJECTS_INDEX.csv'))}
done = set()
if (OUT / 'page_facts.jsonl').exists():
    done = {json.loads(l)['project_id'] for l in open(OUT / 'page_facts.jsonl')}
lock = threading.Lock()

import subprocess
def get(url, binary=False):
    # curl, not urllib: Devpost returns 403 to Python's default HTTP client.
    r = subprocess.run(['curl', '-sL', '--max-time', '30', '-A', UA, '-w', '\n%{http_code}|%{content_type}', url],
                       capture_output=True, check=True)
    body, _, meta = r.stdout.rpartition(b'\n')
    code, _, ct = meta.decode().partition('|')
    if code != '200': raise RuntimeError(f'HTTP {code}')
    return (body, ct) if binary else body.decode('utf-8', 'ignore')

def text(s): return re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', ' ', s or ''))).strip()
def m1(p, h, flags=re.S):
    m = re.search(p, h, flags); return m.group(1) if m else None

def parse(h):
    title = text(m1(r'<h1[^>]*id="app-title"[^>]*>(.*?)</h1>', h)) or html.unescape(m1(r'<meta property="og:title" content="([^"]*)"', h) or '')
    tagline = text(m1(r'<p class="large"[^>]*>(.*?)</p>', h)) or html.unescape(m1(r'<meta property="og:description" content="([^"]*)"', h) or '')
    gallery = m1(r'id="gallery".*?<img[^>]+src="([^"]+)"', h)
    og = m1(r'<meta property="og:image" content="([^"]*)"', h)
    img = gallery or og
    if img and img.startswith('//'): img = 'https:' + img
    details = m1(r'id="app-details-left"[^>]*>(.*?)<div id="built-with"', h) or ''
    gal = m1(r'<div id="gallery">(.*?)</ul>', h) or ''
    details = details.replace(gal, '')
    sections, cur = [], None
    for part in re.split(r'(<h2[^>]*>.*?</h2>)', details, flags=re.S):
        if part.startswith('<h2'): cur = text(part); continue
        t = text(part)
        if t: sections.append({'heading': cur, 'text': t[:4000]})
    built = [text(x) for x in re.findall(r'<span class="cp-tag[^"]*"[^>]*>(.*?)</span>', m1(r'id="built-with"(.*?)</ul>', h) or '', re.S)]
    badges = [text(x) for x in re.findall(r'<span class="winner[^"]*"[^>]*>.*?</span>\s*(.*?)</li>', h, re.S)]
    submitted = [text(x) for x in re.findall(r'<div class="software-list-content">\s*<p>\s*<a[^>]*>(.*?)</a>', h, re.S)]
    video = bool(re.search(r'(youtube\.com/embed|player\.vimeo|youtu\.be|video-embed)', h))
    return dict(title=title, tagline=tagline, first_image_url=img, sections=sections, built_with=built,
                prize_badges=badges, submitted_to=submitted, has_video_embed=video,
                n_gallery_items=len(re.findall(r'<li[\s>]', gal)),
                first_gallery_item_is_video=bool(re.match(r'\s*<li>\s*<div class="flex-video', gal)))

def work(r):
    pid, bid = r['project_id'], r['blind_id']; url = urls.get(pid) or ''
    if pid in done: return None
    rec = dict(project_id=pid, blind_id=bid, url=url, status='', image_file='')
    if not url.startswith('https://devpost.com/software/'):
        rec['status'] = 'no_devpost_url'; return rec
    try:
        h = get(url); rec.update(parse(h)); rec['status'] = 'ok'
        if rec.get('first_image_url'):
            try:
                b, ct = get(rec['first_image_url'], binary=True)
                ext = {'image/png': 'png', 'image/gif': 'gif', 'image/webp': 'webp'}.get(ct.split(';')[0], 'jpg')
                (IMG / f'{bid}.{ext}').write_bytes(b); rec['image_file'] = f'data/pages/images/{bid}.{ext}'
            except Exception as e: rec['image_error'] = str(e)[:120]
    except Exception as e:
        rec['status'] = 'error: ' + str(e)[:150]
    time.sleep(0.6)
    return rec

with cf.ThreadPoolExecutor(4) as ex, open(OUT / 'page_facts.jsonl', 'a') as pf:
    for i, rec in enumerate(ex.map(work, rows)):
        if rec is None: continue
        with lock: pf.write(json.dumps(rec, ensure_ascii=False) + '\n'); pf.flush()
        if i % 100 == 0: print(i, rec['status'], flush=True)

facts = [json.loads(l) for l in open(OUT / 'page_facts.jsonl')]
with open(OUT / 'cover_inputs.jsonl', 'w') as fo:
    for f in facts:
        if f['status'] == 'ok':
            fo.write(json.dumps({k: f.get(k) for k in ('blind_id', 'title', 'tagline', 'first_image_url', 'image_file')}, ensure_ascii=False) + '\n')
with open(OUT / 'fetch_log.csv', 'w', newline='') as fo:
    w = csv.writer(fo); w.writerow(['project_id', 'status', 'has_image', 'n_sections'])
    for f in facts: w.writerow([f['project_id'], f['status'], bool(f.get('image_file')), len(f.get('sections') or [])])
from collections import Counter
print(Counter(f['status'][:20] for f in facts), 'images:', sum(bool(f.get('image_file')) for f in facts))
