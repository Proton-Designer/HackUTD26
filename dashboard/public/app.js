(() => {
'use strict';

/* ============ helpers ============ */
const $ = (s) => document.querySelector(s);
const el = (tag, cls, text) => {
  const n = document.createElement(tag);
  if (cls) n.className = cls;
  if (text != null) n.textContent = String(text);
  return n;
};
const clamp = (v, a, b) => Math.max(a, Math.min(b, v));
const ease = (t) => (t < .5 ? 4 * t * t * t : 1 - Math.pow(-2 * t + 2, 3) / 2);
const rootPx = () => parseFloat(getComputedStyle(document.documentElement).fontSize) || 16;
const hexA = (hex, a) => {
  const h = String(hex || '#9db4d8').replace('#', '');
  const n = parseInt(h.length === 3 ? h.split('').map((c) => c + c).join('') : h.padEnd(6, '0').slice(0, 6), 16);
  return `rgba(${(n >> 16) & 255},${(n >> 8) & 255},${n & 255},${a})`;
};
const safeColor = (c) => (/^#[0-9a-f]{3,8}$/i.test(c || '') ? c : '#9db4d8');
const trunc = (s, n) => { s = String(s == null ? '' : s); return s.length > n ? s.slice(0, n - 1) + '…' : s; };
const firstLine = (s) => {
  const l = String(s || '').split('\n').map((x) => x.trim()).filter(Boolean);
  return l[0] || '';
};
const fmtAge = (s) => {
  s = Math.max(0, Math.round(s));
  if (s < 60) return s + 's ago';
  if (s < 3600) return Math.floor(s / 60) + 'm ago';
  return Math.floor(s / 3600) + 'h ' + String(Math.floor((s % 3600) / 60)).padStart(2, '0') + 'm ago';
};
const pad2 = (n) => String(n).padStart(2, '0');

/* ============ state ============ */
const FALLBACK_COLORS = { P1: '#00e5ff', P2: '#b388ff', P3: '#ff4081', P4a: '#69f0ae', P4b: '#ffd740' };
const S = { pipelines: [], pmap: {}, machines: [], stats: {}, health: {}, mode: 'demo', recvAt: Date.now(), messages: [] };
const seen = new Set();
let firstState = true;
const edgeCounts = {};
const edgeGlow = {};
const nodePulse = {};
const ekey = (a, b) => (a < b ? a + '|' + b : b + '|' + a);

function colorOf(id) { const p = S.pmap[id]; return safeColor(p ? p.color : FALLBACK_COLORS[id]); }

/* ============ stars background ============ */
const starCv = $('#stars');
function drawStars() {
  const dpr = Math.min(window.devicePixelRatio || 1, 2);
  const w = innerWidth, h = innerHeight;
  starCv.width = w * dpr; starCv.height = h * dpr;
  const c = starCv.getContext('2d'); c.scale(dpr, dpr);
  let seed = 1337; const rnd = () => ((seed = (seed * 16807) % 2147483647) / 2147483647);
  for (let i = 0; i < 260; i++) {
    const x = rnd() * w, y = rnd() * h, r = rnd() * 1.3 + .2, a = rnd() * .6 + .1;
    c.fillStyle = `rgba(${150 + rnd() * 100 | 0},${190 + rnd() * 60 | 0},255,${a})`;
    c.beginPath(); c.arc(x, y, r, 0, 6.283); c.fill();
  }
}

/* ============ header: clock / countdown ============ */
const DEADLINE = Date.parse('2026-11-08T15:00:00Z'); // 2026-11-08 09:00 America/Chicago (CST, UTC-6)
const fmtTime = new Intl.DateTimeFormat('en-GB', { timeZone: 'America/Chicago', hour12: false, hour: '2-digit', minute: '2-digit', second: '2-digit' });
const fmtDate = new Intl.DateTimeFormat('en-US', { timeZone: 'America/Chicago', weekday: 'short', month: 'short', day: 'numeric', timeZoneName: 'short' });
function tickClock() {
  const now = new Date();
  $('#clock').textContent = fmtTime.format(now).replace(/^24/, '00');
  $('#clockSub').textContent = fmtDate.format(now).toUpperCase().replace(',', ' ·');
  let d = DEADLINE - now.getTime();
  const neg = d < 0; d = Math.abs(d);
  const s = Math.floor(d / 1000), hh = Math.floor(s / 3600);
  $('#countdown').textContent = (neg ? '+' : '') + pad2(hh) + ':' + pad2(Math.floor((s % 3600) / 60)) + ':' + pad2(s % 60);
  $('#cdSub').textContent = neg ? 'SINCE SUBMISSION DEADLINE' : 'UNTIL SUBMISSION · SUN 9:00 AM';
  const blk = $('#cdBlock');
  blk.classList.toggle('warn', !neg && hh < 6);
  blk.classList.toggle('crit', neg || hh < 1);
}

/* ============ lanes ============ */
const laneEls = {};
const OS_SVG = {
  mac: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="4" y="5" width="16" height="11" rx="1.5"/><path d="M2 19h20"/></svg>',
  win: '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M3 5.5l8-1.1v7H3zM12 4.3l9-1.3v8.4h-9zM3 12.6h8v7l-8-1.1zM12 12.6h9V21l-9-1.3z"/></svg>',
  linux: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="4" width="18" height="16" rx="2"/><path d="M7 9l3 3-3 3M13 15h4"/></svg>',
  other: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"><rect x="3" y="4" width="18" height="12" rx="2"/><path d="M8 20h8M12 16v4"/></svg>'
};
function osIcon(os) {
  const o = String(os || '').toLowerCase();
  const k = /mac|darwin|os x/.test(o) ? 'mac' : /win/.test(o) ? 'win' : /lin|ubuntu|debian|arch/.test(o) ? 'linux' : 'other';
  const d = el('span', 'os'); d.title = os || '';
  d.innerHTML = OS_SVG[k]; // static trusted markup only
  return d;
}

function buildLanes() {
  const host = $('#lanes');
  host.textContent = '';
  for (const k of Object.keys(laneEls)) delete laneEls[k];
  for (const p of S.pipelines) {
    const lane = el('div', 'lane');
    lane.style.setProperty('--c', safeColor(p.color));
    const top = el('div', 'lane-top');
    const id = el('span', 'lane-id', p.id);
    const name = el('span', 'lane-name', p.name);
    const owner = el('span', 'lane-owner', p.owner || '');
    const sp = el('span', 'sp');
    const pill = el('span', 'pill');
    const ag = el('span', 'lane-agents');
    top.append(id, name, owner, sp, pill, ag);
    const label = el('div', 'step-label');
    const track = el('div', 'track');
    const text = el('div', 'step-text');
    const machines = el('div', 'machines');
    lane.append(top, label, track, text, machines);
    host.append(lane);
    laneEls[p.id] = { lane, pill, ag, label, track, text, machines, sig: '', segs: [], lastStep: null };
  }
}

function machineStatus(m) {
  const age = machineAge(m);
  if (age > 600) return 'offline';
  if (age > 180) return 'stale';
  return m.status || 'idle';
}
function machineAge(m) {
  if (typeof m.age_s === 'number') return m.age_s + (Date.now() - S.recvAt) / 1000;
  const t = Date.parse(m.updated || '');
  return isNaN(t) ? 99999 : (Date.now() - t) / 1000;
}
function pipelineStatus(p) {
  const ms = S.machines.filter((m) => m.pipeline === p.id);
  if (!ms.length && !p.status) return 'offline';
  let st = p.status || 'offline';
  if (ms.length && ms.every((m) => machineAge(m) > 600)) st = 'offline';
  return ['working', 'idle', 'blocked', 'offline'].includes(st) ? st : 'idle';
}
S.pStatus = {};

function renderLanes() {
  const maxM = document.body.classList.contains('details') ? 4 : 3;
  for (const p of S.pipelines) {
    const L = laneEls[p.id]; if (!L) continue;
    const st = pipelineStatus(p);
    S.pStatus[p.id] = st;
    L.lane.classList.remove('working', 'idle', 'blocked', 'offline');
    L.lane.classList.add(st);
    L.pill.className = 'pill ' + st;
    L.pill.textContent = st.toUpperCase();
    const agents = S.machines.filter((m) => m.pipeline === p.id && machineAge(m) <= 600).reduce((a, m) => a + (+m.agents || 0), 0);
    const agTotal = st === 'offline' ? 0 : (agents || +p.agents || 0);
    L.ag.textContent = '';
    L.ag.append(document.createTextNode(String(agTotal) + ' '), el('small', null, agTotal === 1 ? 'AGENT' : 'AGENTS'));

    const steps = p.steps || [];
    const n = p.step_n == null ? null : +p.step_n;
    const sig = steps.length + ':' + n;
    if (L.segs.length !== steps.length) {
      L.track.textContent = ''; L.segs = steps.map((t, i) => { const s = el('i', 'seg'); s.title = (i + 1) + '. ' + t; L.track.append(s); return s; });
    }
    L.segs.forEach((s, i) => {
      s.className = 'seg' + (n != null && i + 1 < n ? ' done' : n != null && i + 1 === n ? ' cur' : '');
    });
    L.label.textContent = '';
    if (n != null && steps[n - 1]) {
      L.label.append(el('b', null, 'STEP ' + n + '/' + steps.length), document.createTextNode(' · ' + steps[n - 1]));
    } else L.label.append(el('b', null, 'STEP – /' + steps.length), document.createTextNode(' · not reported'));
    if (L.lastStep !== sig) { if (L.lastStep != null) { L.lane.classList.remove('flash'); void L.lane.offsetWidth; L.lane.classList.add('flash'); } L.lastStep = sig; }
    L.text.textContent = p.step_text || (st === 'offline' ? 'No agent online' : 'Waiting for status…');
    L.text.className = 'step-text' + (p.step_text ? '' : ' none');

    // machines
    const ms = S.machines.filter((m) => m.pipeline === p.id).sort((a, b) => machineAge(a) - machineAge(b));
    L.machines.textContent = '';
    if (!ms.length) L.machines.append(el('div', 'no-mach', 'no machines reporting'));
    const detailed = document.body.classList.contains('details');
    ms.slice(0, maxM).forEach((m, idx) => {
      const ms_ = machineStatus(m);
      const compact = detailed || idx > 0;
      const row = el('div', 'mach ' + ms_ + (compact ? ' compact' : ''));
      const l1 = el('div', 'm-l1');
      l1.append(el('span', 'm-host', m.host || m.key), el('span', 'm-person', m.person || ''));
      if (compact && m.last_tool) l1.append(el('span', 'm-tool-inline', m.last_tool + (m.last_file ? ' ' + m.last_file : '')));
      const r1 = el('div', 'm-r1');
      r1.append(document.createTextNode((m.agents || 0) + 'a · ' + (m.sessions || 0) + 's'));
      const age = el('span', 'm-age m-age-inline'); age.dataset.upd = String(Date.now() - machineAge(m) * 1000); age.textContent = fmtAge(machineAge(m));
      if (compact) r1.append(age);
      row.append(osIcon(m.os), l1, r1);
      if (!compact) {
        const l2 = el('div', 'm-l2');
        if (m.last_tool) l2.append(el('span', 'm-tool', m.last_tool), document.createTextNode(m.last_file ? '  ' + m.last_file : ''));
        else l2.textContent = '—';
        const r2 = el('div', 'm-r2 m-age'); r2.dataset.upd = String(Date.now() - machineAge(m) * 1000);
        r2.textContent = fmtAge(machineAge(m));
        row.append(l2, r2);
      }
      L.machines.append(row);
    });
    if (ms.length > maxM) L.machines.append(el('div', 'm-more', '+' + (ms.length - maxM) + ' more'));
  }
}
function tickAges() {
  document.querySelectorAll('.m-age[data-upd]').forEach((n) => {
    n.textContent = fmtAge((Date.now() - (+n.dataset.upd)) / 1000);
  });
}

/* ============ header stats ============ */
const lastStat = {};
function setStat(id, v) {
  const n = $(id); const t = String(v == null ? 0 : v);
  if (n.textContent !== t) {
    n.textContent = t;
    if (lastStat[id] != null) { n.classList.remove('bump'); void n.offsetWidth; n.classList.add('bump'); }
  }
  lastStat[id] = t;
}
function renderHeader() {
  const st = S.stats || {};
  const online = S.machines.filter((m) => machineAge(m) <= 600);
  setStat('#stAgents', st.agents_total != null ? st.agents_total : online.reduce((a, m) => a + (+m.agents || 0), 0));
  setStat('#stMachines', st.machines_online != null ? st.machines_online : online.length);
  setStat('#stRate', st.messages_last_hour != null ? st.messages_last_hour : 0);
  setStat('#stThreads', st.open_threads != null ? st.open_threads : 0);
  $('#project').textContent = S.project || 'Backfire · HackUTD 2026';
  const live = S.mode === 'live';
  const b = $('#modeBadge'); b.textContent = live ? 'LIVE' : 'DEMO'; b.className = 'badge ' + (live ? 'live' : 'demo');
  const h = S.health || {};
  const ok = h.github === 'ok';
  const dot = $('#healthDot');
  dot.className = 'dot ' + (live ? (ok ? 'ok' : 'err') : (h.github && h.github !== 'ok' && !/demo/i.test(h.github) ? 'err' : 'demo'));
  $('#healthText').textContent = live ? 'GITHUB' : 'SIMULATED';
  $('#healthSub').textContent = ok || !live ? (h.rate_remaining != null ? h.rate_remaining + ' req left' : (live ? 'ok' : 'demo data')) : trunc(h.github || 'unknown', 24);
  $('#health').title = JSON.stringify(h);
  $('#graphSub').textContent = (S.stats && S.stats.messages_total != null ? S.stats.messages_total : S.messages.length) + ' messages';
  $('#lanesSub').textContent = '';
}

/* ============ feed ============ */
const feedEl = $('#feed');
function chip(id) {
  const c = el('span', 'chip', id);
  c.style.setProperty('--cc', colorOf(id));
  return c;
}
function addFeed(m, animate) {
  const item = el('div', 'item' + (animate ? ' new' : ''));
  item.style.setProperty('--c', colorOf(m.from));
  const i1 = el('div', 'i1');
  const d = new Date(m.created_at);
  const tm = isNaN(d) ? '--:--' : new Intl.DateTimeFormat('en-GB', { timeZone: 'America/Chicago', hour12: false, hour: '2-digit', minute: '2-digit', second: '2-digit' }).format(d).replace(/^24/, '00');
  i1.append(el('span', 'i-time', tm), chip(m.from), el('span', 'arrow', '→'));
  const to = Array.isArray(m.to) ? m.to : [];
  to.slice(0, 3).forEach((t) => i1.append(chip(t)));
  if (to.length > 3) i1.append(el('span', 'chip more', '+' + (to.length - 3)));
  const kind = String(m.kind || 'reply');
  i1.append(el('span', 'kind ' + kind.replace(/[^a-z]/g, ''), kind));
  const subj = el('div', 'subj', m.title || '(no subject)');
  const body = el('div', 'body', document.body.classList.contains('details') ? String(m.body || '').replace(/\s+/g, ' ').trim() : firstLine(m.body));
  body.dataset.full = String(m.body || '').replace(/\s+/g, ' ').trim();
  body.dataset.first = firstLine(m.body);
  item.append(i1, subj, body);
  feedEl.prepend(item);
  while (feedEl.children.length > 40) feedEl.lastChild.remove();
  $('#feedEmpty').classList.add('hide');
}
function refreshFeedBodies() {
  feedEl.querySelectorAll('.body').forEach((b) => { b.textContent = document.body.classList.contains('details') ? b.dataset.full : b.dataset.first; });
}

/* ============ graph canvas ============ */
const cv = $('#graph'), ctx = cv.getContext('2d');
let W = 0, H = 0, DPR = 1, nodes = [], SC = 1;
const packets = [], labels = [], queue = [];
let nextSlot = 0;

function layoutGraph() {
  const r = cv.getBoundingClientRect();
  DPR = Math.min(window.devicePixelRatio || 1, 2);
  W = Math.max(50, r.width); H = Math.max(50, r.height);
  cv.width = W * DPR; cv.height = H * DPR;
  SC = rootPx() / 16;
  const n = S.pipelines.length || 5;
  const rx = Math.min(W * .34, H * .36 * (W / H > .8 ? 1.2 : 1)), ry = H * .325;
  const cx = W / 2, cy = H * .5;
  nodes = S.pipelines.map((p, i) => {
    const a = -Math.PI / 2 + (i / n) * Math.PI * 2;
    return { id: p.id, x: cx + Math.cos(a) * rx, y: cy + Math.sin(a) * ry, a, r: Math.min(W, H) * .092 };
  });
  nodes.cx = cx; nodes.cy = cy;
}
const nodeById = (id) => nodes.find((n) => n.id === id);
function ctrl(a, b) { // bezier control, pulled toward centre
  const mx = (a.x + b.x) / 2, my = (a.y + b.y) / 2;
  return { x: mx + (nodes.cx - mx) * .38, y: my + (nodes.cy - my) * .38 };
}
function bez(a, c, b, t) {
  const u = 1 - t;
  return { x: u * u * a.x + 2 * u * t * c.x + t * t * b.x, y: u * u * a.y + 2 * u * t * c.y + t * t * b.y };
}

function recomputeEdges() {
  for (const k in edgeCounts) delete edgeCounts[k];
  for (const m of S.messages) for (const t of (m.to || [])) if (t !== m.from) { const k = ekey(m.from, t); edgeCounts[k] = (edgeCounts[k] || 0) + 1; }
}

function launch(m, fast) {
  const from = nodeById(m.from);
  if (!from) return;
  const now = performance.now();
  const gap = fast ? 260 : 520;
  let at = Math.max(now, nextSlot);
  nextSlot = at + gap;
  const rec = (m.to || []).filter((t) => t !== m.from && nodeById(t));
  rec.forEach((t, i) => {
    queue.push({ at: at + i * (fast ? 70 : 140), from: m.from, to: t, dur: fast ? 1000 : 1900, color: colorOf(m.from), title: m.title || '', labelIt: i === 0, kind: m.kind });
  });
}

function pumpQueue(now) {
  for (let i = queue.length - 1; i >= 0; i--) {
    const q = queue[i];
    if (q.at <= now) {
      queue.splice(i, 1);
      if (packets.length > 60) continue;
      packets.push({ ...q, t0: now });
      edgeGlow[ekey(q.from, q.to)] = 1;
      if (q.labelIt) labels.push({ from: q.from, to: q.to, text: q.title, color: q.color, t0: now, dur: q.dur + 900 });
    }
  }
}

function drawGraph(now) {
  ctx.setTransform(DPR, 0, 0, DPR, 0, 0);
  ctx.clearRect(0, 0, W, H);
  if (!nodes.length) return;
  const s = SC;
  const cx = nodes.cx, cy = nodes.cy;
  const T = now;

  // centre radar
  ctx.save();
  ctx.translate(cx, cy);
  const base = Math.min(W, H) * .17;
  for (let i = 1; i <= 3; i++) {
    ctx.beginPath(); ctx.ellipse(0, 0, base * i * .62, base * i * .62 * (H / W > 1 ? 1.05 : .85), 0, 0, 6.283);
    ctx.strokeStyle = `rgba(90,150,255,${.13 - i * .025})`; ctx.lineWidth = 1; ctx.setLineDash(i === 2 ? [4, 8] : []); ctx.stroke();
  }
  ctx.setLineDash([]);
  if (ctx.createConicGradient) {
    const g = ctx.createConicGradient((T / 3500) % 6.283, 0, 0);
    g.addColorStop(0, 'rgba(0,229,255,0)'); g.addColorStop(.86, 'rgba(0,229,255,0)'); g.addColorStop(1, 'rgba(0,229,255,.16)');
    ctx.fillStyle = g; ctx.beginPath(); ctx.arc(0, 0, base * 1.2, 0, 6.283); ctx.fill();
  }
  ctx.textAlign = 'center'; ctx.textBaseline = 'middle';
  ctx.font = `800 ${22 * s}px ${getComputedStyle(document.body).getPropertyValue('--mono')}`;
  ctx.fillStyle = 'rgba(200,225,255,.85)'; ctx.shadowColor = '#00e5ff'; ctx.shadowBlur = 14;
  ctx.fillText('BACKFIRE', 0, -8 * s);
  ctx.shadowBlur = 0;
  ctx.font = `600 ${12 * s}px ${getComputedStyle(document.body).getPropertyValue('--mono')}`;
  ctx.fillStyle = 'rgba(140,170,220,.8)';
  ctx.fillText('AGENT MESH', 0, 14 * s);
  ctx.restore();

  // edges
  const ids = nodes.map((n) => n.id);
  for (let i = 0; i < ids.length; i++) for (let j = i + 1; j < ids.length; j++) {
    const A = nodes[i], B = nodes[j];
    const k = ekey(ids[i], ids[j]);
    const cnt = edgeCounts[k] || 0;
    const glow = edgeGlow[k] || 0;
    if (glow > 0) edgeGlow[k] = Math.max(0, glow - .006);
    const c = ctrl(A, B);
    ctx.beginPath(); ctx.moveTo(A.x, A.y); ctx.quadraticCurveTo(c.x, c.y, B.x, B.y);
    if (!cnt) { ctx.strokeStyle = 'rgba(110,150,230,.07)'; ctx.lineWidth = 1; ctx.setLineDash([3, 7]); ctx.stroke(); ctx.setLineDash([]); continue; }
    const g = ctx.createLinearGradient(A.x, A.y, B.x, B.y);
    const ca = colorOf(A.id), cb = colorOf(B.id);
    const al = .28 + glow * .5;
    g.addColorStop(0, hexA(ca, al)); g.addColorStop(1, hexA(cb, al));
    ctx.strokeStyle = g;
    ctx.lineWidth = (1.2 + Math.min(cnt, 14) * .55) * s;
    ctx.shadowColor = glow > .05 ? '#fff' : 'transparent'; ctx.shadowBlur = glow * 14;
    ctx.stroke(); ctx.shadowBlur = 0;
    // count label at curve middle
    const mid = bez(A, c, B, .5);
    ctx.font = `700 ${12 * s}px ${getComputedStyle(document.body).getPropertyValue('--mono')}`;
    ctx.textAlign = 'center'; ctx.textBaseline = 'middle';
    const cw = ctx.measureText(String(cnt)).width + 10 * s;
    ctx.fillStyle = 'rgba(5,10,22,.85)'; ctx.fillRect(mid.x - cw / 2, mid.y - 9 * s, cw, 18 * s);
    ctx.fillStyle = 'rgba(200,220,255,.9)';
    ctx.fillText(String(cnt), mid.x, mid.y + .5);
  }

  // packets
  for (let i = packets.length - 1; i >= 0; i--) {
    const p = packets[i];
    const A = nodeById(p.from), B = nodeById(p.to);
    const t = (now - p.t0) / p.dur;
    if (t >= 1 || !A || !B) {
      packets.splice(i, 1);
      if (B) nodePulse[p.to] = { t0: now, color: p.color };
      continue;
    }
    const c = ctrl(A, B);
    const e = ease(t);
    // trail
    for (let k = 14; k >= 0; k--) {
      const tt = clamp(e - k * .012, 0, 1);
      const q = bez(A, c, B, tt);
      ctx.beginPath(); ctx.arc(q.x, q.y, (6 - k * .33) * s, 0, 6.283);
      ctx.fillStyle = hexA(p.color, (1 - k / 15) * .5);
      ctx.fill();
    }
    const h = bez(A, c, B, e);
    ctx.save();
    ctx.shadowColor = p.color; ctx.shadowBlur = 26 * s;
    ctx.beginPath(); ctx.arc(h.x, h.y, 8 * s, 0, 6.283); ctx.fillStyle = p.color; ctx.fill();
    ctx.shadowBlur = 0;
    ctx.beginPath(); ctx.arc(h.x, h.y, 3.5 * s, 0, 6.283); ctx.fillStyle = '#fff'; ctx.fill();
    ctx.restore();
  }

  // nodes
  for (const nd of nodes) drawNode(nd, T, s);

  // labels
  for (let i = labels.length - 1; i >= 0; i--) {
    const L = labels[i];
    const t = (now - L.t0) / L.dur;
    if (t >= 1) { labels.splice(i, 1); continue; }
    const A = nodeById(L.from), B = nodeById(L.to); if (!A || !B) { labels.splice(i, 1); continue; }
    const c = ctrl(A, B); const mid = bez(A, c, B, .5);
    let dx = mid.x - cx, dy = mid.y - cy; const dl = Math.hypot(dx, dy) || 1;
    const alpha = t < .12 ? t / .12 : t > .75 ? (1 - t) / .25 : 1;
    const rise = (1 - ease(Math.min(1, t * 3))) * 8 * s;
    ctx.font = `700 ${15 * s}px ${getComputedStyle(document.body).getPropertyValue('--sans')}`;
    const txt = trunc(L.text, 44);
    const tw = ctx.measureText(txt).width + 22 * s, th = 26 * s;
    let x = mid.x + dx / dl * 26 * s, y = mid.y + dy / dl * 22 * s + rise;
    x = clamp(x, tw / 2 + 6, W - tw / 2 - 6); y = clamp(y, th, H - th);
    ctx.save(); ctx.globalAlpha = alpha;
    ctx.fillStyle = 'rgba(4,8,18,.92)'; ctx.strokeStyle = L.color; ctx.lineWidth = 1.5 * s;
    ctx.shadowColor = L.color; ctx.shadowBlur = 14;
    ctx.beginPath(); (ctx.roundRect ? ctx.roundRect(x - tw / 2, y - th / 2, tw, th, 7 * s) : ctx.rect(x - tw / 2, y - th / 2, tw, th)); ctx.fill(); ctx.stroke();
    ctx.shadowBlur = 0; ctx.fillStyle = '#fff'; ctx.textAlign = 'center'; ctx.textBaseline = 'middle';
    ctx.fillText(txt, x, y + .5);
    ctx.restore();
  }
}

function drawNode(nd, T, s) {
  const p = S.pmap[nd.id] || {};
  const col = colorOf(nd.id);
  const st = S.pStatus[nd.id] || 'offline';
  const r = nd.r;
  const mono = getComputedStyle(document.body).getPropertyValue('--mono');
  const sans = getComputedStyle(document.body).getPropertyValue('--sans');
  const ringCol = st === 'blocked' ? '#ff3b55' : col;
  ctx.save();
  ctx.translate(nd.x, nd.y);
  const dim = st === 'offline' ? .5 : st === 'idle' ? .8 : 1;

  // arrival pulse
  const np = nodePulse[nd.id];
  if (np) {
    const t = (T - np.t0) / 900;
    if (t >= 1) delete nodePulse[nd.id];
    else { ctx.beginPath(); ctx.arc(0, 0, r * (1 + t * .9), 0, 6.283); ctx.strokeStyle = hexA(np.color, (1 - t) * .9); ctx.lineWidth = 4 * s * (1 - t) + 1; ctx.stroke(); }
  }
  // ripples
  if (st === 'working' || st === 'blocked') {
    const per = st === 'blocked' ? 1100 : 2000;
    for (let k = 0; k < 3; k++) {
      const ph = ((T / per) + k / 3) % 1;
      ctx.beginPath(); ctx.arc(0, 0, r * (1.05 + ph * .75), 0, 6.283);
      ctx.strokeStyle = hexA(ringCol, (1 - ph) * .45); ctx.lineWidth = 2 * s; ctx.stroke();
    }
  }
  // body
  const g = ctx.createRadialGradient(0, -r * .3, r * .1, 0, 0, r);
  g.addColorStop(0, hexA(col, .28 * dim)); g.addColorStop(1, 'rgba(5,10,22,.96)');
  ctx.beginPath(); ctx.arc(0, 0, r, 0, 6.283); ctx.fillStyle = g; ctx.fill();
  // status ring
  ctx.lineWidth = (st === 'working' ? 4.5 : 3.5) * s;
  if (st === 'offline') { ctx.setLineDash([7 * s, 8 * s]); ctx.strokeStyle = 'rgba(120,135,165,.8)'; ctx.lineDashOffset = 0; }
  else if (st === 'idle') { ctx.strokeStyle = hexA(col, .38 + .08 * Math.sin(T / 900)); }
  else if (st === 'blocked') { ctx.strokeStyle = hexA('#ff3b55', .6 + .4 * Math.sin(T / 140)); ctx.shadowColor = '#ff3b55'; ctx.shadowBlur = 24; }
  else { ctx.strokeStyle = col; ctx.shadowColor = col; ctx.shadowBlur = 22 + 8 * Math.sin(T / 400); }
  ctx.beginPath(); ctx.arc(0, 0, r, 0, 6.283); ctx.stroke();
  ctx.setLineDash([]); ctx.shadowBlur = 0;
  if (st === 'working') { // rotating arc
    const a0 = (T / 900) % 6.283;
    ctx.beginPath(); ctx.arc(0, 0, r + 8 * s, a0, a0 + 1.1);
    ctx.strokeStyle = '#fff'; ctx.lineWidth = 3 * s; ctx.lineCap = 'round'; ctx.shadowColor = col; ctx.shadowBlur = 14; ctx.stroke();
    ctx.lineCap = 'butt'; ctx.shadowBlur = 0;
  }
  // id
  ctx.textAlign = 'center'; ctx.textBaseline = 'middle';
  ctx.font = `800 ${r * .62}px ${mono}`;
  ctx.fillStyle = st === 'offline' ? '#7f8ca8' : '#fff'; ctx.shadowColor = col; ctx.shadowBlur = st === 'offline' ? 0 : 12;
  ctx.fillText(nd.id, 0, 2 * s);
  ctx.shadowBlur = 0;

  // agent badge
  const L = laneEls[nd.id];
  const agNum = L ? parseInt(L.ag.textContent, 10) || 0 : 0;
  const bx = r * .74, by = -r * .74, br = Math.max(13 * s, r * .27);
  ctx.beginPath(); ctx.arc(bx, by, br, 0, 6.283);
  ctx.fillStyle = st === 'offline' ? '#2a3348' : col; ctx.fill();
  ctx.strokeStyle = '#050a16'; ctx.lineWidth = 3 * s; ctx.stroke();
  ctx.font = `800 ${br * 1.15}px ${mono}`; ctx.fillStyle = st === 'offline' ? '#8a97b3' : '#04070e'; ctx.fillText(String(agNum), bx, by + 1 * s);

  // labels (outward: top node above, others below)
  const above = nd.a < -Math.PI / 2 + .01 && nd.y < nodes.cy - 5;
  const lh = 17 * s;
  const y0 = above ? -r - 12 * s - lh * 2.15 : r + 14 * s;
  const line = (txt, y, font, color) => {
    ctx.font = font; const w = ctx.measureText(txt).width;
    ctx.fillStyle = 'rgba(3,6,13,.82)'; ctx.fillRect(-w / 2 - 6 * s, y - lh * .62, w + 12 * s, lh * 1.15);
    ctx.fillStyle = color; ctx.fillText(txt, 0, y);
  };
  ctx.globalAlpha = dim;
  line(trunc(p.name || nd.id, 26), y0 + lh * .5, `700 ${16 * s}px ${sans}`, '#eaf2ff');
  line((p.owner || '') + '  ·  ' + st.toUpperCase(), y0 + lh * 1.65, `700 ${12.5 * s}px ${mono}`, st === 'blocked' ? '#ff6b80' : st === 'working' ? col : '#8da3c7');
  ctx.restore();
}

let lastFrame = 0;
function frame(now) {
  pumpQueue(now);
  drawGraph(now);
  requestAnimationFrame(frame);
}

/* ============ data ingest ============ */
function applyState(s, fromEvent) {
  if (!s || typeof s !== 'object') return;
  S.recvAt = Date.now();
  S.mode = s.mode || S.mode;
  S.project = s.project || S.project;
  S.health = s.health || S.health;
  S.stats = s.stats || S.stats;
  S.machines = Array.isArray(s.machines) ? s.machines : S.machines;
  const pl = Array.isArray(s.pipelines) ? s.pipelines : S.pipelines;
  const structural = pl.length !== S.pipelines.length || pl.some((p, i) => !S.pipelines[i] || S.pipelines[i].id !== p.id || (S.pipelines[i].steps || []).length !== (p.steps || []).length);
  S.pipelines = pl;
  S.pmap = {}; pl.forEach((p) => { S.pmap[p.id] = p; });
  if (structural) { buildLanes(); layoutGraph(); }

  const incoming = Array.isArray(s.messages) ? s.messages : [];
  const fresh = incoming.filter((m) => m && m.id != null && !seen.has(m.id));
  if (firstState) {
    firstState = false;
    incoming.forEach((m) => seen.add(m.id));
    S.messages = incoming.slice();
    recomputeEdges();
    incoming.slice(-40).forEach((m) => addFeed(m, false));
    $('#feedEmpty').classList.toggle('hide', incoming.length > 0);
    replay();
  } else if (fresh.length) {
    fresh.forEach((m) => ingestMessage(m));
  }
  renderLanes();
  renderHeader();
}
function ingestMessage(m) {
  if (!m || m.id == null || seen.has(m.id)) return;
  seen.add(m.id);
  S.messages.push(m); if (S.messages.length > 400) S.messages.shift();
  recomputeEdges();
  addFeed(m, true);
  launch(m, false);
  renderHeader();
}
function replay() {
  const last = S.messages.slice(-10);
  nextSlot = performance.now() + 400;
  last.forEach((m) => launch(m, true));
}

/* ============ transport ============ */
let es = null, pollTimer = null;
function setConn(t) { $('#connLbl').textContent = t; }
async function poll() {
  try {
    const r = await fetch('/api/state', { cache: 'no-store' });
    if (!r.ok) throw new Error(r.status);
    applyState(await r.json());
    if (es && es.readyState === 1) stopPoll(); else setConn('POLL 3s');
  } catch (e) { setConn('OFFLINE'); }
}
function startPoll() { if (pollTimer) return; poll(); pollTimer = setInterval(poll, 3000); }
function stopPoll() { if (pollTimer) { clearInterval(pollTimer); pollTimer = null; } }
function connect() {
  if (typeof EventSource === 'undefined') { startPoll(); return; }
  try { es = new EventSource('/api/events'); } catch (e) { startPoll(); return; }
  es.onopen = () => { stopPoll(); setConn('● SSE'); };
  es.addEventListener('state', (ev) => { try { applyState(JSON.parse(ev.data)); setConn('● SSE'); } catch (e) { console.warn('bad state', e); } });
  es.addEventListener('message', (ev) => { try { if (!firstState) ingestMessage(JSON.parse(ev.data)); } catch (e) { console.warn('bad message', e); } });
  es.onerror = () => { setConn('RECONNECTING'); startPoll(); };
}

/* ============ keyboard ============ */
addEventListener('keydown', (e) => {
  if (e.ctrlKey || e.metaKey || e.altKey) return;
  const k = e.key.toLowerCase();
  if (k === 'f') { if (document.fullscreenElement) document.exitFullscreen(); else document.documentElement.requestFullscreen && document.documentElement.requestFullscreen().catch(() => {}); }
  else if (k === 'r') replay();
  else if (k === 'd') { document.body.classList.toggle('details'); refreshFeedBodies(); renderLanes(); }
});

/* ============ boot ============ */
function onResize() { drawStars(); layoutGraph(); }
addEventListener('resize', onResize);
new ResizeObserver(() => layoutGraph()).observe($('#graphWrap'));
drawStars();
tickClock(); setInterval(tickClock, 250);
setInterval(tickAges, 1000);
setInterval(() => { if (S.pipelines.length) { renderLanes(); renderHeader(); } }, 5000);
layoutGraph();
requestAnimationFrame(frame);
connect();
// initial fetch in case SSE is slow
setTimeout(() => { if (firstState) startPoll(); }, 2500);
})();
