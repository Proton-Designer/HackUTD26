/*
 * Backfire command center.
 * Live: subscribes to WS /events on the P1 server. Fallback: replays mock/events.json, else the local fixture.
 * No build step, no dependencies. Every value from an event is escaped before it reaches the DOM
 * (transcripts and artifacts are scammer-controlled text).
 */
(() => {
  'use strict';

  // ---------- config: URL params only, no settings UI ----------
  const qs = new URLSearchParams(location.search);
  const CFG = {
    src: (qs.get('src') || 'auto').toLowerCase(),        // auto | live | mock | fixture
    server: (qs.get('server') || '').replace(/\/+$/, ''), // P1 base URL, e.g. http://192.168.1.20:8000
    speed: Math.max(0.1, parseFloat(qs.get('speed')) || 1),
    maxGap: Math.max(0.3, parseFloat(qs.get('gap')) || 6), // replay: long silences are squeezed to this many seconds
    mockUrl: qs.get('mock') || '../../mock/events.json',
    voice: (qs.get('voice') || '').toLowerCase(),         // clone | synthetic: override when voice.enrolled was missed
  };

  // ---------- labels ----------
  const ASK = { otp: 'One-time code', card: 'Card number', ssn: 'SSN', gift_card: 'Gift cards', crypto: 'Crypto', wire: 'Wire transfer', p2p: 'P2P payment', remote_app: 'Remote-access app', secrecy: 'Secrecy' };
  const ART = { callback_phone: 'Callback number', domain: 'Website', url: 'Link', wallet: 'Crypto wallet', payment_handle: 'Payment handle', gift_card_brand: 'Gift card brand', bank: 'Bank account', remote_app: 'Remote-access app', impersonated_org: 'Impersonating', script_tags: 'Script' };
  const SUBJECT = { callback_phone: 'Callback number', domain: 'Website', url: 'Link', wallet: 'Wallet', payment_handle: 'Payment handle', bank: 'Bank account' };
  const LOOKUPABLE = new Set(['callback_phone', 'domain', 'wallet', 'payment_handle']);
  const TOOL = { bank: 'Bank (simulated)', rdap: 'RDAP', whois: 'RDAP', blockchain: 'Chain', chain: 'Chain', btc: 'BTC', eth: 'ETH', mempool: 'Chain', etherscan: 'Chain', allowlist: 'Allowlist', safe_browsing: 'Safe Browsing', popularity: 'Site rank' };
  // P4a's kind names (intel/gate.py), plus P1's mock name and older aliases
  const KIND = {
    block_caller_for_customer: 'Block caller for Maria', link_campaign: 'Link to campaign, block its numbers before ring',
    callback_protection_warning: 'Add callback number to Scam Callback Protection', network_number_block: 'Block calling number network-wide',
    number_block_network: 'Block calling number network-wide', dns_block_registrar_report: 'DNS block + registrar abuse report',
    exchange_freeze_request: 'Exchange freeze request for the wallet', ftc_ic3_packet: 'FTC + IC3 report packet',
    hold_transfer: 'Held the transfer to the scammer', flag_payee_bankwide: 'Flag this payee bank-wide',
    mark_number_safe: 'Mark number safe', add_trusted_contact: 'Add trusted contact', unblock_number: 'Unblock number', allowlist_add: 'Add to allowlist',
    block_for_customer: 'Block caller for Maria', campaign_link: 'Link to campaign', callback_protection: 'Add to Callback Protection',
    network_block: 'Block number network-wide', dns_block: 'DNS block + registrar report', freeze_request: 'Freeze request',
    report_packet: 'FTC + IC3 report packet', ftc_ic3: 'FTC + IC3 report packet',
  };
  // Trust changes only Maria can make in her app; when they come from untrusted input they're injection attempts
  const TRUST_ASK = { mark_number_safe: t => `Mark ${t} as safe`, add_trusted_contact: t => `Add ${t} as a trusted contact`, unblock_number: t => `Unblock ${t}`, allowlist_add: t => `Allowlist ${t}` };
  const ENDED_BY = { maria: 'Maria', caller: 'the caller', decoy: 'the decoy', system: 'the system', scammer: 'the scammer', network_reject: 'the network' };
  const ROUTE = { NORMAL: 'rang normally', LIVE_GUARD: 'Live Guard on', BLOCKED_BACKFIRE: 'blocked before ring' };
  // Five steps (the kit caps a demo path at five), grouped in the brief's own words: during, after, before the next ring.
  // 'extract' is tracked separately but shown inside Verify.
  const STAGES = [['detect', 'Detect'], ['handoff', 'Hand off'], ['verify', 'Verify'], ['burn', 'Block'], ['immune', 'Immune']];
  const PHASES = [['During the call', 1, 3], ['After the call', 3, 5], ['Before the next ring', 5, 6]];
  // Contract bands as words, never a bare percentage ("honest confidence")
  const BAND = { low: 'Low risk', watch: 'Watch', high: 'Likely scam', critical: 'Scam' };
  const ASK_PHRASE = { otp: 'her one-time code', card: 'her card number', ssn: 'her Social Security number', gift_card: 'gift cards', crypto: 'crypto', wire: 'a wire transfer', p2p: 'a P2P payment', remote_app: 'remote access to her phone', secrecy: 'secrecy' };
  const bandWord = r => BAND[String(r.band || '').toLowerCase()] || (r.s >= 0.95 ? 'Scam' : r.s >= 0.8 ? 'Likely scam' : r.s >= 0.4 ? 'Watch' : 'Low risk');
  // STIR/SHAKEN level in T-Mobile's words
  const ATTEST = { A: 'Caller Verified', B: 'caller ID partly verified', C: 'caller ID not verified', NONE: 'no caller ID check' };
  const attestWords = a => ATTEST[String(a || 'none').toUpperCase()] || `attestation ${a}`;
  const TAGLINE = 'T-Mobile customers hand a live scam call to an AI decoy that <em>exposes and blocks the scammer.</em>';
  const CALL_EVENTS = new Set(['call.incoming', 'call.routed', 'call.answered', 'call.ended', 'transcript.caller', 'risk.update', 'alert.fired', 'user.action', 'handoff.started', 'handoff.restored', 'decoy.turn', 'decoy.fake_value', 'guardrail.tripped']);

  // ---------- helpers ----------
  const $ = id => document.getElementById(id);
  const bodyOf = panel => document.querySelector(`#p-${panel} .body`);
  const esc = v => String(v ?? '').replace(/[&<>"']/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
  const arr = v => (Array.isArray(v) ? v : v == null || v === '' ? [] : [v]);
  const num = v => (v == null || v === '' ? NaN : Number(v));
  const digits = v => String(v ?? '').replace(/\D/g, '');
  const last10 = v => digits(v).slice(-10);
  const isPhoneLike = v => typeof v === 'string' && /^[+\d\s().-]{10,}$/.test(v.trim()) && digits(v).length >= 10 && digits(v).length <= 15;
  const humanize = v => String(v ?? '').replace(/[_.]+/g, ' ').trim();
  const cap = s => (s ? s[0].toUpperCase() + s.slice(1) : s);
  const lcFirst = s => (s && !/^[A-Z]{2}/.test(s) ? s[0].toLowerCase() + s.slice(1) : s);
  const pct = s => Math.round(Math.max(0, Math.min(1, s || 0)) * 100);
  const pushUniq = (list, v) => { if (v != null && v !== '' && !list.includes(v)) list.push(v); };
  const empty = t => `<div class="empty">${esc(t)}</div>`;

  function fmtPhone(v) {
    const d = digits(v);
    if (d.length === 11 && d[0] === '1') return `+1 ${d.slice(1, 4)}-${d.slice(4, 7)}-${d.slice(7)}`;
    if (d.length === 10) return `+1 ${d.slice(0, 3)}-${d.slice(3, 6)}-${d.slice(6)}`;
    return String(v ?? '');
  }
  const fmtVal = v => (isPhoneLike(String(v ?? '')) ? fmtPhone(v) : String(v ?? ''));
  function shortVal(v) {
    const s = fmtVal(v);
    return s.length > 28 ? `${s.slice(0, 13)}…${s.slice(-6)}` : s;
  }
  function normVal(v) {
    if (v == null) return '';
    if (typeof v === 'object') v = v.addr ?? v.value ?? v.id ?? JSON.stringify(v);
    const s = String(v).trim();
    if (isPhoneLike(s)) return last10(s);
    return s.toLowerCase().replace(/^https?:\/\//, '').replace(/^www\./, '').replace(/\/+$/, '');
  }
  function tsMs(ts) {
    if (ts == null || ts === '') return NaN;
    const n = typeof ts === 'number' ? ts : Number(ts);
    if (!Number.isNaN(n)) return n < 1e12 ? n * 1000 : n;
    return Date.parse(ts);
  }
  const fmtTime = ms => (Number.isFinite(ms) ? new Date(ms).toLocaleTimeString([], { hour: '2-digit', minute: '2-digit', second: '2-digit' }) : '');
  const fmtInt = n => Math.round(n).toLocaleString('en-US');
  function fmtCompact(n) {
    if (n >= 1e6) return `${(n / 1e6).toFixed(n >= 1e7 ? 0 : 2).replace(/\.?0+$/, '')}M`;
    if (n >= 1e3) return `${(n / 1e3).toFixed(n >= 1e4 ? 0 : 1).replace(/\.0$/, '')}K`;
    return String(Math.round(n));
  }
  function scopeKey(s) {
    s = String(s || '').toLowerCase();
    if (/^(her|customer|self|user|maria)/.test(s)) return 'her';
    if (/backfire|campaign/.test(s)) return 'backfire';
    if (/extern/.test(s)) return 'external';
    if (/all|network|global/.test(s)) return 'all';
    return 'her';
  }
  const scopeLabel = s => ({ her: 'Maria only', backfire: 'Backfire users', all: 'All customers', external: 'External' }[scopeKey(s)]);

  // ---------- state ----------
  const MODE = { kind: 'connecting', base: '', url: '', label: '' };
  let S = freshState();
  let painted = {};
  let lastFlash = 0, flashTimer = 0;

  function freshState() {
    return {
      seq: 0, count: 0,
      calls: new Map(), focus: null,
      engine: null, model: '', voice: null,
      arts: new Map(), artOrder: [], orgs: [], tags: [], loose: [], instructions: [], standIn: false,
      trace: [], traceCall: null, proposed: new Set(), inputLogged: new Set(), agent: null, agentN: 0,
      pipeSeq: {}, lastMs: 0,
      actions: new Map(), actOrder: [],
      blocks: [], rejects: [],
      campaigns: new Map(), campaignId: null, immunityShown: 0, immunityBase: null,
      denied: [],
      stage: {},
      // Idle is never blank: the tagline, word for word as on the slides and Devpost
      head: { text: TAGLINE, sub: 'Live Guard is on and waiting for a call to the scam line. It only ever hears the caller.', tone: '' },
      flashSeq: 0,
    };
  }
  function getCall(id) {
    const key = id || '_';
    let c = S.calls.get(key);
    if (!c) {
      c = { id: key, from: '', to: '', attestation: '', scamId: NaN, decision: '', reason: '', answered: false, ended: '', risk: null, alert: null, feed: [], utt: new Map(), handoff: false, restored: false };
      S.calls.set(key, c);
    }
    return c;
  }
  const focusCall = () => (S.focus ? S.calls.get(S.focus) : null);
  function focusOn(c) { if (S.focus !== c.id) { S.focus = c.id; dirty('risk', 'feed'); } }
  function head(text, sub, tone) { S.head = { text, sub: sub || '', tone: tone || '' }; dirty('hero'); }
  function stage(key, sub) {
    const st = S.stage[key];
    S.stage[key] = { seq: st ? st.seq : S.seq, sub: sub ?? (st ? st.sub : '') };
    dirty('hero');
  }
  function trace(cls, k, html) { S.trace.push({ cls, k, html, seq: S.seq }); dirty('trace'); }
  const isLive = () => MODE.kind === 'live' || MODE.kind === 'reconnecting';
  function voiceState() {
    if (CFG.voice === 'clone' || CFG.voice === 'synthetic') return CFG.voice;
    if (!S.voice) return 'unknown';
    return S.voice.deleted ? 'synthetic' : 'clone';
  }
  const voiceName = () => ({ clone: "Maria's consented voice", synthetic: 'a synthetic voice', unknown: 'the decoy voice' }[voiceState()]);
  const voiceShort = () => ({ clone: "Maria's voice", synthetic: 'synthetic voice', unknown: 'decoy voice' }[voiceState()]);

  // ---------- event normalizing ----------
  function envelope(raw) {
    if (!raw || typeof raw !== 'object') return null;
    const type = raw.type || raw.event;
    if (!type) return null;
    let data = raw.data ?? raw.payload ?? {};
    if (typeof data !== 'object' || data === null) data = { value: data };
    return { type: String(type), call_id: raw.call_id ?? data.call_id ?? null, ts: raw.ts, ms: tsMs(raw.ts), data };
  }

  function normArtifacts(d) {
    let list = Array.isArray(d) ? d : (d.artifacts || d.items || null);
    if (!Array.isArray(list)) {
      list = [];
      for (const [k, v] of Object.entries(d || {})) {
        if (!(k in ART)) continue;
        const many = Array.isArray(v) && k !== 'script_tags' ? v : [v];
        for (const x of many) list.push(x && typeof x === 'object' && !Array.isArray(x) ? { type: k, ...x } : { type: k, value: x });
      }
    }
    return list.filter(Boolean).map(a => {
      if (typeof a !== 'object') return { type: 'unknown', value: a, meta: {} };
      const type = String(a.type || a.kind || 'unknown').toLowerCase();
      let value;
      if (type === 'wallet') value = a.addr ?? a.address ?? a.value;
      else if (type === 'payment_handle') value = a.id ?? a.handle ?? a.value;
      else if (type === 'bank') value = a.last4 ? `account ending ${a.last4}` : (a.value ?? a.hash);
      else if (type === 'script_tags') value = a.value ?? a.tags ?? a.script_tags ?? [];
      else value = a.value ?? a.number ?? a.domain ?? a.url ?? a.brand ?? a.name ?? a.app ?? a.org;
      return { type, value, meta: a };
    });
  }
  const artKey = (type, value) => `${type}|${normVal(value)}`;
  function findArt(l) {
    const exact = S.arts.get(artKey(l.type, l.value));
    if (exact) return exact;
    const v = normVal(l.value);
    for (const k of S.artOrder) { const a = S.arts.get(k); if (normVal(a.value) === v) return a; }
    return null;
  }

  function guessType(value, tool) {
    const v = String(value ?? '');
    if (isPhoneLike(v)) return 'callback_phone';
    if (IS_CHAIN.test(tool)) return 'wallet';
    if (/rdap|whois|safe_browsing|popularity/.test(tool) || /\.[a-z]{2,}$/i.test(v)) return 'domain';
    return 'unknown';
  }
  // P4a (intel/lookups.py) sends flat data: {kind: domain|wallet|allowlist, value, status: ok|not_found|unavailable|invalid, ...fields}.
  // A nested {tool, artifact:{type,value}, result:{...}} shape is also accepted.
  function lookupTool(d) {
    const t = String(d.tool || d.source_type || '').toLowerCase();
    if (t) return t;
    const k = String(d.kind || d.artifact_kind || '').toLowerCase();
    return { domain: 'rdap', wallet: 'chain', allowlist: 'allowlist', phone: 'allowlist', callback_phone: 'allowlist', bank_transfer: 'bank' }[k] || k || 'lookup';
  }
  const ARTIFACT_KIND = { phone: 'callback_phone', callback_phone: 'callback_phone', domain: 'domain', url: 'url', wallet: 'wallet', payment_handle: 'payment_handle' };
  const IS_CHAIN = /chain|btc|eth|mempool|etherscan|blockstream|blockscout/;
  function normLookup(d) {
    const art = d.artifact && typeof d.artifact === 'object' ? d.artifact : (d.indicator || {});
    const r = d.result && typeof d.result === 'object' ? { ...d, ...d.result } : d;
    const value = art.value ?? art.addr ?? d.value ?? d.target ?? d.domain ?? d.addr ?? d.address ?? d.number;
    const tool = lookupTool(d);
    let type = art.type || d.artifact_type || ARTIFACT_KIND[String(d.artifact_kind || '').toLowerCase()];
    if (!type && /allow/.test(tool) && d.value_type) type = d.value_type === 'domain' ? 'domain' : 'callback_phone';
    if (!type) type = guessType(value, tool);
    const status = String(d.status || 'ok').toLowerCase();
    const ok = !(d.ok === false || d.error || /unavailable|error|invalid|fail|timeout/.test(status));
    const l = {
      id: d.lookup_id || null, tool, type: String(type).toLowerCase(), value, ok, status,
      error: d.error || d.reason || status, real: d.real !== false && d.simulated !== true,
      result: r, latency: d.latency_ms, source: d.source || '',
    };
    if (tool === 'bank') {
      // P4a's simulated bank lookup: value arrives as "zelle:<payee id>"; match the card on the id
      const v = String(value ?? '');
      if (/^[a-z0-9_-]+:/i.test(v)) { l.rail = v.split(':')[0]; l.value = v.slice(l.rail.length + 1); }
      if (!d.artifact_kind || !ARTIFACT_KIND[String(d.artifact_kind).toLowerCase()]) l.type = 'payment_handle';
    }
    l.summary = d.summary || autoSummary(l);
    l.detail = d.detail || autoDetail(l);
    l.verdict = verdictWord(d.verdict) || autoVerdict(l);
    return l;
  }
  const fmtAmt = x => Number(x).toLocaleString('en-US', { maximumFractionDigits: 4 });
  const fmtMoney = x => `$${Number(x).toLocaleString('en-US', { maximumFractionDigits: 0 })}`;
  // Money a bank hold kept from leaving (simulated bank); undone holds don't count
  function heldTotal() {
    let t = 0;
    for (const id of S.actOrder) {
      const a = S.actions.get(id);
      if (/hold_transfer/.test(a.kind) && a.status === 'auto' && !a.undone && Number.isFinite(a.amount)) t += a.amount;
    }
    return t;
  }
  function ago(days) {
    if (days <= 0) return 'today';
    if (days === 1) return '1 day ago';
    if (days < 60) return `${days} days ago`;
    if (days < 730) return `${Math.round(days / 30.4)} months ago`;
    return `${Math.floor(days / 365.25)} years ago`;
  }
  const shortSource = s => String(s || '').replace(/\s*\(.*\)\s*$/, '');
  function autoSummary(l) {
    const r = l.result;
    if (/rdap|whois/.test(l.tool)) {
      if (l.status === 'not_found') return 'No registration record';
      const age = r.age_days ?? r.registered_days_ago ?? (r.registered ? Math.floor((Date.now() - Date.parse(r.registered)) / 864e5) : null);
      if (age == null || Number.isNaN(Number(age))) return 'Registration found';
      return `Registered ${ago(Number(age))}`;
    }
    if (IS_CHAIN.test(l.tool)) {
      const unit = r.unit || r.chain || '';
      const recv = r.total_received ?? r.received_btc ?? r.received_eth ?? r.received;
      const inflows = r.tx_in ?? r.inflows;
      const n = inflows ?? r.tx_count;
      const parts = [];
      if (recv != null && recv !== '') parts.push(`${fmtAmt(recv)} ${unit} received`.replace(/\s+/g, ' '));
      else if (r.balance != null) parts.push(`Balance ${fmtAmt(r.balance)} ${unit}`.trim());
      if (n != null) parts.push(`${n} ${inflows != null ? 'inflows' : 'transactions'}`);
      return parts.join(', ') || 'On-chain activity found';
    }
    if (/allow/.test(l.tool)) {
      if (r.match) return `Matches ${r.matched_org || r.org || 'a verified business'}`;
      return r.value_type === 'domain' || l.type === 'domain' ? 'Not a verified business domain' : 'Not a verified business number';
    }
    return r.summary || 'Lookup done';
  }
  function autoDetail(l) {
    const r = l.result;
    const src = shortSource(l.source);
    if (l.tool === 'bank') return r.source_label || 'Simulated bank (Capital One Nessie sandbox, mock data)';
    if (!l.ok) return src;
    if (/rdap|whois/.test(l.tool)) return [r.registrar ? `Registrar: ${r.registrar}` : '', src].filter(Boolean).join(' · ');
    if (IS_CHAIN.test(l.tool)) return [r.first_seen ? `First seen ${r.first_seen}` : '', src].filter(Boolean).join(' · ');
    if (/allow/.test(l.tool) && r.match) return 'Never actioned: flagged as poisoning';
    return src;
  }
  function verdictWord(v) {
    v = String(v || '').toLowerCase();
    if (!v) return '';
    if (/conflict|poison|allowlist|match/.test(v)) return 'conflict';
    if (/bad|malicious|suspicious|scam|high|risky/.test(v)) return 'bad';
    if (/ok|clean|safe|benign|low/.test(v)) return 'ok';
    return 'unknown';
  }
  function autoVerdict(l) {
    const r = l.result;
    if (!l.ok) return 'unknown';
    if (/allow/.test(l.tool)) return r.match ? 'conflict' : 'unknown';
    if (l.tool === 'bank') return num(r.pending_count) > 0 || num(r.activity_count) > 0 ? 'bad' : 'unknown';
    if (/rdap|whois/.test(l.tool)) {
      if (r.newly_registered === true) return 'bad';
      const age = num(r.age_days ?? r.registered_days_ago);
      return Number.isFinite(age) ? (age < 30 ? 'bad' : 'ok') : 'unknown';
    }
    if (IS_CHAIN.test(l.tool)) return num(r.tx_in ?? r.inflows ?? r.tx_count) > 0 || num(r.total_received) > 0 ? 'bad' : 'unknown';
    return 'unknown';
  }

  function normStatus(s, approval) {
    s = String(s || '').toLowerCase();
    approval = String(approval || '').toLowerCase();
    if (/den|reject|refus|not_actioned/.test(s)) return 'denied';
    if (/skip/.test(s)) return 'skipped';
    if (/^held/.test(s)) return 'held';
    if (/queue|pending|await/.test(s)) return 'queued';
    if (/approved/.test(s)) return 'applied';
    if (/applied|done|executed/.test(s)) return approval === 'analyst' && !/auto/.test(s) ? 'applied' : 'auto';
    if (/auto/.test(s)) return 'auto';
    if (approval === 'auto') return 'auto';
    if (approval === 'analyst') return 'queued';
    return 'proposed';
  }
  // When an action arrives without a scope (P1's mock), infer it from the kind instead of defaulting to "Maria only"
  function inferScope(kind) {
    const k = String(kind || '').toLowerCase();
    if (/network|dns|freeze|ftc|ic3|report|registrar/.test(k)) return 'network';
    if (/campaign/.test(k)) return 'campaign';
    if (/callback_protection/.test(k)) return 'all_customers';
    return 'her';
  }
  function normAction(d, callId) {
    const status = normStatus(d.status, d.approval);
    const kind = String(d.kind || d.type || 'action');
    return {
      id: String(d.action_id || d.id || `act-${S.seq}`), call: callId,
      kind, label: d.label || d.title || KIND[kind] || cap(humanize(kind)),
      target: d.target ?? d.value ?? '', scope: d.scope || inferScope(kind), approval: d.approval || '',
      status, gate: d.gate_status || '', simulated: d.simulated !== false, evidence: arr(d.evidence),
      expiry: d.expiry || d.expires_in || (d.payload && d.payload.body && d.payload.body.expiresInDays ? `${d.payload.body.expiresInDays} days` : ''),
      undo: d.undo_token || '', reason: d.reason || d.rule || '',
      amount: num(d.amount), source: d.source || '', undone: d.active === false,
    };
  }

  // ---------- handlers (one per contract event) ----------
  const H = {
    'call.incoming'(e, d, c) {
      c.from = d.from ?? c.from; c.to = d.to ?? c.to;
      c.attestation = d.attestation ?? c.attestation; c.scamId = num(d.scam_id_score ?? c.scamId);
      if (!S.focus) focusOn(c);
      const sid = Number.isFinite(c.scamId) ? ` · Scam ID ${c.scamId.toFixed(2)} (simulated)` : '';
      head(`Incoming call from <em>${esc(fmtPhone(c.from))}</em>`, `${cap(attestWords(c.attestation))}${sid}`, '');
      dirty('feed');
    },
    'call.routed'(e, d, c) {
      c.decision = String(d.decision || '').toUpperCase();
      c.reason = d.reason || '';
      if (c.decision.startsWith('BLOCKED')) {
        S.rejects.push({ seq: S.seq, ms: S.lastMs, number: c.from, reason: c.reason });
        stage('immune', 'callback rejected');
        head(`<em>${esc(fmtPhone(c.from))}</em> called back. Rejected before it rang.`, c.reason || 'Confirmed scammer', 'win');
        S.flashSeq = S.seq;
        dirty('auto');
      } else if (c.decision === 'LIVE_GUARD') {
        head('Ringing Maria with <em>Live Guard on</em>', `${fmtPhone(c.from)} · ${c.reason}`, '');
      }
      dirty('feed');
    },
    'call.answered'(e, d, c) {
      c.answered = true; focusOn(c);
      if (String(d.by || 'maria').toLowerCase() === 'decoy') return; // the handoff events tell this part
      // A new call Maria answers starts the story over (the rail and the Story view follow the latest call)
      if (S.storyCall && S.storyCall !== c.id) { S.stage = {}; VIEW.pinned = null; }
      S.storyCall = c.id;
      const listen = String(d.via || '').toLowerCase() === 'listen';
      head('Maria answered. Live Guard hears <em>the caller only</em>.', listen ? 'She answered in the Backfire app (listen mode) · her voice is never processed' : 'Her voice is never processed', '');
      dirty('feed');
    },
    'call.ended'(e, d, c) {
      c.ended = d.ended_by || 'unknown';
      const dur = Number.isFinite(num(d.duration_s)) ? ` after ${Math.round(num(d.duration_s))} s` : '';
      if (!c.decision.startsWith('BLOCKED')) c.feed.push({ kind: 'sys', text: `Call ended by ${ENDED_BY[c.ended] || humanize(c.ended)}${dur}`, seq: S.seq });
      dirty('feed');
    },
    'transcript.caller'(e, d, c) {
      if (c.decision.startsWith('BLOCKED')) return;
      if (c.handoff && !c.restored) return; // during the handoff, decoy.turn carries both sides
      focusOn(c);
      const id = d.utterance_id ?? `u${S.seq}`;
      let line = c.utt.get(id);
      if (!line) { line = { kind: 'caller', seq: S.seq }; c.utt.set(id, line); c.feed.push(line); }
      line.text = d.text ?? '';
      line.final = d.is_final !== false;
      dirty('feed');
    },
    'risk.update'(e, d, c) {
      focusOn(c);
      const prev = c.risk;
      c.risk = { s: num(d.s) || 0, band: d.band || '', asks: arr(d.asks), type: d.scam_type || '', stage: d.stage || '', imp: d.impersonates || '', ai: !!d.addresses_ai_system, why: arr(d.why_chips), prevPct: prev ? pct(prev.s) : 0 };
      if (d.engine) S.engine = String(d.engine).toLowerCase();
      if (d.model) S.model = String(d.model);
      const p = pct(c.risk.s);
      const word = bandWord(c.risk);
      if (c.risk.s >= 0.5) stage('detect', word.toLowerCase());
      if (!c.handoff && !S.stage.extract) {
        if (c.risk.s >= 0.8) {
          // Lead with what he asked for, in plain words; the score stays small in the Risk panel
          const ask = c.risk.asks.find(a => a !== 'secrecy') || c.risk.asks[0];
          const what = ask ? `he's asking for ${ASK_PHRASE[ask] || humanize(ask)}` : c.risk.why[0] ? lcFirst(c.risk.why[0]) : 'scam pattern';
          head(`${esc(word)}: <em>${esc(what)}</em>`, c.risk.why.join(' · '), 'alert');
        } else {
          head(`Live Guard is listening · <em>${esc(word.toLowerCase())}</em>`, c.risk.why.join(' · ') || 'Caller side only', '');
        }
      }
      dirty('risk', 'header', 'attest');
    },
    'alert.fired'(e, d, c) {
      c.alert = { level: d.level || 'first', why: arr(d.why_chips) };
      c.feed.push({ kind: 'sys', tone: 'hot', seq: S.seq, text: d.level === 'realert' ? 'Risk rose: two more beeps to Maria' : 'Two beeps to Maria: Continue · Scammer Get Scammed · Hang up' });
      stage('detect');
      dirty('risk', 'feed');
    },
    'user.action'(e, d, c) {
      const a = String(d.action || '');
      const text = { scammer_get_scammed: 'Maria tapped Scammer Get Scammed', hang_up: 'Maria hung up', continue: 'Maria tapped Continue' }[a] || `Maria: ${humanize(a)}`;
      c.feed.push({ kind: 'sys', tone: a === 'scammer_get_scammed' ? 'hot' : '', text, seq: S.seq });
      if (a === 'scammer_get_scammed') {
        stage('handoff', 'Maria tapped it');
        head('Maria tapped <em>Scammer Get Scammed</em>', 'The network swaps her out. The decoy keeps the scammer talking.', 'alert');
      }
      dirty('feed');
    },
    'handoff.started'(e, d, c) {
      c.handoff = true; c.restored = false; focusOn(c);
      const dlMs = tsMs(d.restore_deadline); // mocks use relative seconds; only show a real clock time
      const dl = Number.isFinite(dlMs) && dlMs > 1e12 ? ` · she can step back in until ${fmtTime(dlMs)}` : '';
      c.feed.push({ kind: 'sys', tone: 'hot', text: `Decoy took over in ${voiceName()}${dl}`, seq: S.seq });
      stage('handoff', voiceShort());
      head(`The decoy took over in <em>${esc(voiceName())}</em>`, 'The scammer is now talking to Nemotron. Maria is off the call.', 'alert');
      dirty('feed');
    },
    'handoff.restored'(e, d, c) {
      c.restored = true;
      c.feed.push({ kind: 'sys', text: 'Maria is back on the call (decoy stepped out)', seq: S.seq });
      dirty('feed');
    },
    'decoy.turn'(e, d, c) {
      focusOn(c);
      const spk = String(d.speaker || '').toLowerCase() === 'decoy' ? 'decoy' : 'scammer';
      c.feed.push({ kind: spk, text: d.text ?? '', latency: num(d.latency_ms), fakes: [], seq: S.seq });
      if (spk === 'decoy' && !S.stage.extract) {
        const lat = Number.isFinite(num(d.latency_ms)) ? `Reply in ${Math.round(num(d.latency_ms))} ms · ` : '';
        head(`The scammer is talking to the decoy in <em>${esc(voiceShort())}</em>`, `${lat}fake values come from code, never from the model`, 'alert');
      }
      dirty('feed');
    },
    'decoy.fake_value'(e, d, c) {
      const label = `fake ${humanize(d.kind || 'value')} given, made by code`;
      const last = [...c.feed].reverse().find(l => l.kind === 'decoy');
      if (last) last.fakes.push(label); else c.feed.push({ kind: 'sys', tone: 'guard', text: label, seq: S.seq });
      dirty('feed');
    },
    'guardrail.tripped'(e, d, c) {
      const rule = humanize(d.rule || d.kind || 'guardrail');
      c.feed.push({ kind: 'sys', tone: 'guard', text: `Guardrail: ${rule}`, seq: S.seq });
      S.denied.push({ kind: 'guardrail', what: d.detail || cap(rule), why: `Decoy guardrail · ${rule}`, seq: S.seq });
      dirty('feed', 'denied');
    },
    'artifacts.extracted'(e, d) {
      const list = normArtifacts(d);
      // P1's phone-free SIM_MODE injects the script-card values with source 'demo_stand_in' until P3's extractor
      // is wired (#35). Non-negotiable 7: say so everywhere these values show.
      const standIn = /stand.?in|simulat/i.test(String(d.source || ''));
      if (standIn) S.standIn = true;
      for (const a of list) {
        if (a.type === 'impersonated_org') { pushUniq(S.orgs, a.value); continue; }
        if (a.type === 'script_tags') { arr(a.value).forEach(t => pushUniq(S.tags, t)); continue; }
        if (a.type === 'instruction_to_ai') { pushUniq(S.instructions, a.meta.text || a.value); continue; } // the gate denies these
        const art = addArt(a.type, a.value, a.meta);
        if (art && standIn) art.standIn = true;
      }
      const kinds = [...new Set(list.filter(a => !['script_tags', 'instruction_to_ai'].includes(a.type)).map(a => (ART[a.type] || humanize(a.type)).toLowerCase()))];
      const n = S.artOrder.length;
      traceCall(e.call_id);
      S.inputLogged.add(e.call_id || '_');
      if (standIn) {
        trace('input', 'INPUT', `${list.length} typed artifacts, SIMULATED stand-in <span class="res">· extractor not wired yet · raw transcript never read</span>`);
        stage('extract', `${n} artifacts (simulated)`);
        head(`<em>${n} artifacts</em> loaded · simulated stand-in`, 'The extractor is simulated with the script-card values; the lookups that follow are real', 'alert');
      } else {
        trace('input', 'INPUT', `${list.length} typed artifacts from the extractor <span class="res">· raw transcript never read</span>`);
        stage('extract', `${n} artifacts`);
        head(`The decoy extracted <em>${n} artifacts</em>`, kinds.join(' · '), 'alert');
      }
      dirty('artifacts');
    },
    // ----- P4a agent trace: plan → lookups → Nemotron → proposals → gate -----
    'intel.plan'(e, d) {
      traceCall(e.call_id);
      const steps = arr(d.steps).filter(s => s && typeof s === 'object');
      for (const s of steps) {
        const tool = String(s.tool || '').toLowerCase();
        const type = /rdap|whois/.test(tool) ? 'domain' : IS_CHAIN.test(tool) || /explorer/.test(tool) ? 'wallet' : isPhoneLike(String(s.arg || '')) ? 'callback_phone' : 'domain';
        if (s.arg) addArt(type, s.arg, {}); // cards appear now as "awaiting lookup", then fill in
      }
      const inputs = typeof d.inputs === 'string' ? d.inputs : d.inputs ? JSON.stringify(d.inputs) : 'typed artifacts only';
      if (!S.inputLogged.has(e.call_id || '_')) { S.inputLogged.add(e.call_id || '_'); trace('input', 'INPUT', `${esc(inputs)}`); }
      if (steps.length) trace('plan', 'PLAN', steps.map(s => `${esc(s.tool)}(${esc(shortVal(s.arg))})`).join(' <span class="res">→</span> '));
      dirty('artifacts');
    },
    'intel.agent'(e, d) {
      traceCall(e.call_id);
      const engine = String(d.engine || 'nemotron');
      S.agent = { engine, model: d.model || '', error: d.error || '' };
      if (num(d.n_proposals) > 0) S.agentN = num(d.n_proposals);
      const fallback = /fallback/i.test(engine), mock = /mock/i.test(engine);
      const k = fallback ? 'FALLBACK' : mock ? 'MOCK LLM' : 'NEMOTRON';
      const counts = [d.n_proposals != null ? `${d.n_proposals} proposals` : '', num(d.n_baseline_added) > 0 ? `+${d.n_baseline_added} from baseline rule` : ''].filter(Boolean).join(' ');
      const err = d.error ? ` <span class="res">· error: ${esc(d.error)}</span>` : '';
      trace(fallback ? 'agent fallback' : 'agent', k, `${d.plan ? `“${esc(d.plan)}”` : 'planned'}${counts ? ` <span class="res">· ${esc(counts)}</span>` : ''}${err}`);
      dirty('header');
    },
    'intel.proposals'(e, d) {
      traceCall(e.call_id);
      const acts = arr(d.actions).filter(a => a && typeof a === 'object');
      S.proposed.add(e.call_id || '_');
      S.agentN = acts.length || S.agentN;
      const untrusted = acts.filter(a => /instruction_to_ai/.test(a.target_source || '')).length;
      const kinds = acts.map(a => esc(a.kind)).join(', ');
      trace('propose', 'PROPOSED', `${acts.length} action${acts.length === 1 ? '' : 's'} <span class="res">· ${kinds}${untrusted ? ` · ${untrusted} from an instruction to the AI` : ''}</span>`);
    },
    'intel.lookup'(e, d) {
      traceCall(e.call_id);
      const l = normLookup(d);
      l.seq = S.seq;
      const a = findArt(l) || addArt(l.type, l.value, {}); // P1/P4a may look up values we never saw extracted
      const bucket = a ? a.lookups : S.loose;
      // P4a sends no lookup id, so a repeat of the same tool on the same value replaces the old result.
      const i = bucket.findIndex(x => (l.id ? x.id === l.id : x.tool === l.tool && normVal(x.value) === normVal(l.value)));
      if (i >= 0) bucket[i] = l; else bucket.push(l);
      const res = l.ok ? l.summary : `error: ${l.error || 'failed'}`;
      trace('tool', 'TOOL', `${esc(toolFn(l))}(${esc(shortVal(l.value))}) <span class="res">→ ${esc(res)}${l.real ? '' : ' (simulated)'}</span>`);
      const n = countLookups();
      stage('verify', `${n} lookup${n === 1 ? '' : 's'}`);
      const best = lookupHeadlines();
      if (best.length && !S.stage.burn) head(`${isLive() ? 'Real lookup' : 'Lookup'} · <em>${esc(best[0])}</em>`, best.slice(1, 3).join(' · '), 'alert');
      dirty('artifacts');
    },
    'intel.action'(e, d) {
      traceCall(e.call_id);
      const n = normAction(d, e.call_id);
      const prev = S.actions.get(n.id);
      if (!prev) {
        n.seq = S.seq; n.ms = S.lastMs;
        S.actions.set(n.id, n); S.actOrder.push(n.id);
        // After an intel.proposals summary, each action gets one GATE line; otherwise PROPOSE + GATE
        if (!S.proposed.has(e.call_id || '_')) trace('propose', 'PROPOSE', `${esc(n.kind)}(${esc(shortVal(n.target))}) <span class="res">· ${esc(scopeLabel(n.scope))}</span>`);
        gateTrace(n, S.proposed.has(e.call_id || '_'));
      } else {
        // Merge only the fields this update carries, so a bare status update keeps the label and target.
        const before = prev.status;
        if (d.approval) prev.approval = d.approval;
        if (d.status) {
          let st = normStatus(d.status, prev.approval);
          if ((before === 'queued' || before === 'applied') && st === 'auto') st = 'applied'; // approved elsewhere
          if (before === 'applied' && st === 'queued') st = 'applied'; // never un-approve on a stale event
          prev.status = st;
        }
        if (d.label || d.title) prev.label = d.label || d.title;
        if (d.target != null) prev.target = d.target;
        if (d.scope) prev.scope = d.scope;
        if (d.evidence) prev.evidence = arr(d.evidence);
        if (d.expiry) prev.expiry = d.expiry;
        if (d.undo_token) prev.undo = d.undo_token;
        if (d.reason || d.rule) prev.reason = d.reason || d.rule;
        if (Number.isFinite(num(d.amount))) prev.amount = num(d.amount);
        if (d.active === false && !prev.undone) {
          // e.g. Maria released a bank hold from her app
          prev.undone = true; prev.seq = S.seq;
          trace('gate queued', 'CUSTOMER', `undid ${esc(prev.kind)}(${esc(shortVal(prev.target))}) <span class="res">· ${esc(d.gate_status || 'undone by customer')}</span>`);
        }
        if (d.gate_status) prev.gate = d.gate_status;
        if (before !== prev.status) {
          prev.seq = S.seq; prev.ui = '';
          if (prev.status === 'applied') prev.appliedMs = S.lastMs;
          gateTrace(prev, true);
        }
      }
      afterActions();
    },
    'blocklist.updated'(e, d) {
      // Matched to actions at render time, so it works whichever of block / action arrives first.
      const s = String(d.scope || 'her').toLowerCase();
      const scope = /campaign/.test(s) ? 'campaign' : /network|all/.test(s) ? 'network' : 'her';
      const prev = d.undo_token ? S.blocks.find(b => b.undo === d.undo_token) : null;
      if (prev) { prev.active = d.active !== false; prev.seq = S.seq; }
      else S.blocks.push({ seq: S.seq, ms: S.lastMs, call: e.call_id, number: d.number, scope, undo: d.undo_token || '', reason: d.reason || '', active: d.active !== false });
      stage('burn', burnSub());
      dirty('auto');
    },
    'injection.denied'(e, d) {
      traceCall(e.call_id);
      const target = d.target ?? d.attempted_target ?? '';
      const akind = String(d.kind || d.requested_action || '');
      const src = String(d.source || '');
      const kind = d.attempted_poisoning === true ? 'poisoning'
        : d.attempted_poisoning === false ? (TRUST_ASK[akind] || /instruction_to_ai/.test(src) ? 'injection' : 'uncorroborated')
          : /poison|allowlist/i.test(`${akind} ${d.rule || ''} ${d.reason || ''}`) ? 'poisoning' : 'injection';
      const t = fmtVal(target);
      const what = d.attempt || d.text
        || (TRUST_ASK[akind] ? TRUST_ASK[akind](t)
          : kind === 'poisoning' ? `${t} is a verified business, given as a scam contact`
            : `${KIND[akind] || cap(humanize(akind)) || 'Action'}: ${shortVal(target)}`);
      // P4a also sends a denied intel.action for the same thing; keep one row
      const dup = S.denied.findIndex(x => x.fromAction && x.akind === akind && normVal(x.target) === normVal(target));
      const row = { kind, akind, what, target, why: d.reason || d.rule || 'Untrusted value used as an action target', source: src, seq: S.seq };
      if (dup >= 0) S.denied[dup] = row; else S.denied.push(row);
      const res = kind === 'poisoning' ? 'allowlist match, flagged as poisoning' : kind === 'uncorroborated' ? 'no corroboration yet' : 'untrusted input cannot change trust';
      trace('gate denied', 'GATE', `denied ${esc(akind || kind)}(${esc(shortVal(target))}) <span class="res">· ${res}</span>`);
      dirty('denied');
    },
    'campaign.updated'(e, d) {
      traceCall(e.call_id);
      const id = String(d.campaign_id || d.id || 'campaign');
      const prev = S.campaigns.get(id) || {};
      const imm = d.immunity && typeof d.immunity === 'object' ? d.immunity : { count: d.immunity ?? d.immunity_count };
      const count = num(imm.count);
      const nums = Array.isArray(d.numbers) ? d.numbers : null;
      const cmp = {
        id, name: d.name ?? prev.name ?? '', type: d.scam_type ?? prev.type ?? '', status: String(d.status ?? prev.status ?? 'observed'),
        linkedVia: d.linked_via ?? prev.linkedVia ?? '',
        sightings: d.sightings ?? prev.sightings, independent: d.independent_sightings ?? prev.independent,
        numbers: num(d.calling_numbers) >= 0 ? num(d.calling_numbers) : nums ? nums.length : prev.numbers,
        indicators: arr(d.strong_indicators ?? prev.indicators).map(x => humanize(x)),
        poisoning: d.poisoning_attempt_seen ?? prev.poisoning ?? false,
        immunity: Number.isFinite(count) ? count : (prev.immunity || 0),
        immLabel: imm.label ?? prev.immLabel ?? '', immSim: imm.simulated ?? prev.immSim ?? true, seq: S.seq,
      };
      S.campaigns.set(id, cmp); S.campaignId = id;
      if (prev.status !== cmp.status || !prev.id) {
        const via = cmp.linkedVia ? ` · linked via ${esc(cmp.linkedVia)}` : '';
        const seen = cmp.sightings != null ? ` · ${esc(cmp.sightings)} sightings` : '';
        trace('plan', 'CAMPAIGN', `${esc(id)} <span class="res">· ${esc(cmp.status)}${seen}${via}</span>`);
      }
      if (cmp.immunity > 0) stage('immune', `${fmtCompact(cmp.immunity)} blocked for all`);
      dirty('campaign');
    },
    'voice.enrolled'(e, d) { S.voice = { id: d.voice_id, consent: d.consent_version, deleted: false }; dirty('attest'); },
    'voice.deleted'(e, d) { S.voice = { id: d.voice_id, deleted: true }; dirty('attest'); },
  };

  function toolFn(l) {
    const t = l.tool;
    if (/rdap|whois/.test(t)) return 'rdap.domain';
    if (/allow/.test(t)) return 'allowlist.check';
    if (IS_CHAIN.test(t)) return `chain.${String(l.result.chain || 'btc').toLowerCase()}`;
    return t;
  }
  function countLookups() { let n = S.loose.length; for (const k of S.artOrder) n += S.arts.get(k).lookups.length; return n; }
  function lookupHeadlines() {
    const out = [];
    const order = ['domain', 'wallet', 'payment_handle', 'callback_phone', 'url', 'bank'];
    const arts = S.artOrder.map(k => S.arts.get(k)).sort((a, b) => order.indexOf(a.type) - order.indexOf(b.type));
    for (const a of arts) {
      for (const l of a.lookups) {
        if (!l.ok || l.verdict !== 'bad') continue;
        const subject = SUBJECT[a.type] || cap(humanize(a.type));
        out.push(a.type === 'domain' ? `${subject} ${lcFirst(l.summary)}` : `${subject}: ${lcFirst(l.summary)}`);
      }
    }
    return out;
  }
  function gateTrace(a, compact) {
    // P4a sends injection.denied first, then a denied intel.action for the same thing: one row, one trace line
    const seen = a.status === 'denied' && S.denied.some(x => !x.fromAction && x.akind === a.kind && normVal(x.target) === normVal(a.target));
    if (seen) return;
    const tgt = compact ? `${esc(a.kind)}(${esc(shortVal(a.target))}) → ` : '';
    const why = a.reason ? `· ${esc(a.reason)}` : '';
    const t = {
      auto: ['gate auto', 'GATE', `${tgt}auto-applied ✓ <span class="res">· affects only Maria or only adds a warning</span>`],
      queued: ['gate queued', 'GATE', `${tgt}queued for one analyst click <span class="res">· network-wide or external</span>`],
      held: ['gate queued', 'GATE', `${tgt}held <span class="res">${why || '· waiting for campaign confirmation'}</span>`],
      // skipped (e.g. the simulated bank is down): nothing changed, so it is never shown as applied
      skipped: ['gate queued', 'GATE', `${tgt}not applied <span class="res">· ${esc(a.gate || a.reason || 'skipped')}</span>`],
      applied: ['analyst', 'ANALYST', `approved ${esc(a.kind)}(${esc(shortVal(a.target))}) <span class="res">→ simulated: applied</span>`],
      denied: ['gate denied', 'GATE', `${tgt}denied <span class="res">${why || '· policy gate'}</span>`],
    }[a.status];
    if (t) trace(t[0], t[1], t[2]);
    if (a.status === 'denied') {
      S.denied.push({ kind: /poison/.test(a.gate) ? 'poisoning' : 'injection', akind: a.kind, what: `${a.label}: ${shortVal(a.target)}`, target: a.target, why: a.reason || 'Policy gate denied this action', seq: S.seq, fromAction: true });
      dirty('denied');
    }
  }
  function burnSub() {
    let auto = 0, queued = 0, applied = 0;
    for (const id of S.actOrder) { const a = S.actions.get(id); if (a.status === 'auto') auto++; else if (a.status === 'queued') queued++; else if (a.status === 'applied') applied++; }
    if (!auto) auto = S.blocks.filter(b => b.active).length; // P1's blocklist stub without intel actions
    const held = heldTotal();
    return [held ? `${fmtMoney(held)} held` : '', auto ? `${auto} auto` : '', queued ? `${queued} to approve` : '', applied ? `${applied} approved` : ''].filter(Boolean).join(' · ');
  }
  function addArt(type, value, meta) {
    if (value == null || value === '') return null;
    const found = S.arts.get(artKey(type, value)) || findArt({ type, value });
    if (found) return found;
    const a = { type, value, meta: meta || {}, key: artKey(type, value), lookups: [], seq: S.seq };
    S.arts.set(a.key, a); S.artOrder.push(a.key);
    return a;
  }
  function traceCall(callId) {
    if (!callId || callId === S.traceCall) return;
    if (S.trace.length) S.trace.push({ sep: true, html: `call ${esc(callId)}`, seq: S.seq });
    S.traceCall = callId;
  }
  function afterActions() {
    const list = S.actOrder.map(id => S.actions.get(id));
    const auto = list.filter(a => a.status === 'auto');
    const queued = list.filter(a => a.status === 'queued');
    if (auto.length || queued.length || list.some(a => a.status === 'applied')) stage('burn', burnSub());
    const held = heldTotal();
    if (!S.rejects.length && held) {
      // the money moment leads until the callback is rejected
      head(`<em>${fmtMoney(held)} held</em> before it reached the scammer`,
        `Simulated bank (Capital One Nessie sandbox, mock data) · Maria can undo · ${auto.length} protection${auto.length === 1 ? '' : 's'} applied automatically${queued.length ? `, ${queued.length} waiting for one click` : ''}`, 'win');
    } else if (!S.rejects.length && (auto.length || queued.length)) {
      const qn = `${queued.length} waiting for one click`;
      const text = auto.length
        ? `<em>${auto.length} protection${auto.length === 1 ? '' : 's'}</em> applied automatically${queued.length ? `, <em>${qn}</em>` : ''}`
        : `<em>${queued.length} network action${queued.length === 1 ? '' : 's'}</em> waiting for one click`;
      head(text, (auto.length ? auto : queued).map(a => a.label).join(' · '), 'alert');
    }
    dirty('queue', 'auto');
  }
  // Which blocklist rows belong to which action, so a block isn't listed twice
  function blocksFor(a, used) {
    const out = [];
    for (const b of S.blocks) {
      if (used.has(b)) continue;
      const sameNum = last10(b.number) && last10(b.number) === last10(a.target);
      const ok = (b.scope === 'her' && a.status === 'auto' && scopeKey(a.scope) === 'her' && sameNum)
        || (b.scope === 'campaign' && a.status === 'auto' && /campaign/.test(a.kind) && (!a.call || !b.call || a.call === b.call))
        || (b.scope === 'network' && a.status === 'applied' && sameNum);
      if (ok) { used.add(b); out.push(b); }
    }
    return out;
  }

  function apply(raw) {
    const e = envelope(raw);
    if (!e) return;
    S.seq++; S.count++;
    const h = H[e.type];
    if (!h) return;
    S.lastMs = Number.isFinite(e.ms) ? e.ms : Date.now();
    try {
      h(e, e.data, CALL_EVENTS.has(e.type) ? getCall(e.call_id) : null);
    } catch (err) {
      console.warn('[command-center] could not apply event', e, err); // fail open: one bad event never kills the screen
    }
    // Agent pipeline: remember when each stage last moved, so its link animates and its node lights up
    const stageOf = { 'artifacts.extracted': 'input', 'intel.plan': 'input', 'intel.lookup': 'lookups', 'intel.agent': 'agent', 'intel.proposals': 'agent', 'intel.action': 'gate', 'injection.denied': 'gate' }[e.type];
    if (stageOf) { S.pipeSeq[stageOf] = S.seq; dirty('pipeline'); }
  }

  // ---------- approve (one click) ----------
  async function approve(id) {
    const st = S;
    const a = st.actions.get(id);
    if (!a || a.status !== 'queued' || a.ui === 'approving') return;
    a.ui = 'approving'; a.err = '';
    dirty('queue');
    let note = '';
    if (isLive() && MODE.base) {
      try {
        const r = await fetch(`${MODE.base}/intel/actions/${encodeURIComponent(id)}/approve`, {
          method: 'POST', headers: { 'content-type': 'application/json' },
          body: JSON.stringify({ approver: 'analyst', via: 'command-center' }),
        });
        if (!r.ok) throw new Error(`HTTP ${r.status}`);
      } catch (err) {
        note = `server did not confirm (${err.message}): shown locally`;
      }
    } else {
      note = 'replay: applied locally';
    }
    if (S !== st) return; // replay restarted while the request was in flight
    st.seq++;
    a.ui = ''; a.note = note;
    if (a.status === 'queued') { a.status = 'applied'; a.seq = st.seq; a.appliedMs = Date.now(); gateTrace(a); }
    st.pipeSeq.gate = st.seq;
    dirty('pipeline');
    afterActions();
    stage('immune', a.label.toLowerCase().includes('network') ? 'network-wide' : 'approved');
    head(`Approved: <em>${esc(a.label)}</em>`, `Simulated network action applied${a.expiry ? ` · ${a.expiry} expiry` : ''} · reversible`, 'win');
  }
  document.addEventListener('click', ev => {
    const b = ev.target.closest('[data-approve]');
    if (b) approve(b.dataset.approve);
  });

  // ---------- rendering ----------
  const DIRTY = new Set();
  let raf = 0, rafFallback = 0;
  function dirty(...names) {
    for (const n of names) DIRTY.add(n);
    if (!raf) {
      raf = requestAnimationFrame(flush);
      rafFallback = setTimeout(flush, 250); // rAF pauses in hidden windows; still render for background tabs and screen capture
    }
  }
  function flush() {
    cancelAnimationFrame(raf); clearTimeout(rafFallback);
    raf = 0;
    const list = [...DIRTY];
    DIRTY.clear();
    for (const n of list) { try { RENDER[n] && RENDER[n](); } catch (err) { console.warn('[command-center] render', n, err); } }
    for (const n of list) painted[n] = S.seq;
  }
  const fresh = (panel, seq) => (seq > (painted[panel] ?? 0) ? ' fresh' : '');
  const renderAll = () => dirty(...Object.keys(RENDER));

  const RENDER = {
    header() {
      const el = $('engine');
      const model = S.model;
      if (S.engine === 'local') { el.className = 'engine local'; el.innerHTML = `<b>LOCAL</b><span>${esc(model || 'Nemotron 3 Nano 4B')} · on device</span>`; }
      else if (S.engine === 'cloud') { el.className = 'engine cloud'; el.innerHTML = `<b>CLOUD</b><span>${esc(model || 'Nemotron')} · attested enclave</span>`; }
      else { el.className = 'engine'; el.innerHTML = '<b>ENGINE</b><span>waiting for detector</span>'; }
      // Intel agent engine, said honestly: a fallback or offline mock is never shown as Nemotron
      const ag = S.agent;
      const tm = $('trace-meta');
      if (!ag) tm.textContent = 'Nemotron 3 Super · typed artifacts only, never transcripts';
      else if (/fallback/i.test(ag.engine)) tm.innerHTML = '<span class="warn">Fallback rules (Nemotron unavailable)</span> · typed artifacts only';
      else if (/mock/i.test(ag.engine)) tm.innerHTML = `<span class="warn">${esc(ag.engine)}</span> · typed artifacts only`;
      else tm.textContent = `${ag.model ? ag.model.replace(/^nvidia\//, '') : 'Nemotron'} · typed artifacts only, never transcripts`;
      renderSource();
    },

    hero() {
      const hero = $('hero');
      $('headline').innerHTML = S.head.text;
      $('subline').textContent = S.head.sub;
      hero.classList.toggle('alert', S.head.tone === 'alert');
      hero.classList.toggle('win', S.head.tone === 'win');
      if (S.flashSeq && S.flashSeq !== lastFlash) {
        lastFlash = S.flashSeq;
        hero.classList.remove('flash'); void hero.offsetWidth; hero.classList.add('flash');
        clearTimeout(flashTimer); flashTimer = setTimeout(() => hero.classList.remove('flash'), 2200);
      }
      const stOf = k => (k === 'verify' ? S.stage.verify || S.stage.extract : S.stage[k]);
      let now = -1;
      STAGES.forEach(([k], i) => { if (stOf(k)) now = i; });
      const phases = PHASES.map(([label, a, b]) => `<div class="phase" style="grid-column:${a} / ${b}">${label}</div>`).join('');
      layout(); // first, so the rail outlines the chapter actually on screen
      const showing = VIEW.name === 'story' ? VIEW.shown : '';
      const steps = STAGES.map(([k, label], i) => {
        const st = stOf(k);
        const sub = k === 'verify' && S.stage.extract && S.stage.verify ? `${S.stage.extract.sub} · ${S.stage.verify.sub}` : st ? st.sub : '';
        const cls = (!st ? '' : i === now ? 'now' : 'done') + (STEP_CHAPTER[k] === showing ? ' showing' : '');
        const state = !st ? 'not yet' : i === now ? 'current step' : 'done';
        return `<button type="button" class="step ${cls}" data-chapter="${STEP_CHAPTER[k]}" data-n="${i + 1}" aria-pressed="${STEP_CHAPTER[k] === showing}" `
          + `aria-label="${esc(`${label}: ${state}. Show this part`)}" title="Show this part of the story"><b>${label}</b><span>${esc(sub)}</span></button>`;
      }).join('');
      $('rail').innerHTML = phases + steps;
    },

    campaign() {
      const el = $('campaign');
      const c = S.campaigns.get(S.campaignId);
      if (!c) {
        el.className = 'campaign';
        el.innerHTML = '<div class="k"><span>Campaign</span></div><div class="name" style="color:var(--text-3)">None linked yet</div>'
          + '<div class="facts" title="Calls are linked by wallet, website, callback number and script, never by calling number alone.">Linked by wallet, website, callback number, script</div>'
          + '<div class="k" style="margin-top:6px"><span>Immunity</span></div><div class="immrow"><div class="big" style="color:var(--text-3)">0</div><div class="biglabel">numbers and indicators blocked or warned for every Backfire user</div></div>';
        return;
      }
      if (S.immunityBase == null) S.immunityBase = c.immunity; // "compared to what?": the count when this screen first saw the campaign
      const gained = c.immunity - S.immunityBase;
      el.className = 'campaign on';
      const st = c.status.toLowerCase();
      const sightings = c.sightings != null ? `${c.sightings} sightings${c.independent != null && c.independent !== c.sightings ? ` (${c.independent} independent)` : ''}` : '';
      const facts = [c.id, sightings, c.numbers != null ? `${c.numbers} calling numbers` : '', c.indicators.length ? `strong: ${c.indicators.join(', ')}` : ''].filter(Boolean).join(' · ');
      const name = c.name || (c.linkedVia ? `Linked via ${c.linkedVia}` : cap(humanize(c.type)) || 'Scam campaign');
      const poison = c.poisoning ? ' · <span class="poison">poisoning attempt seen</span>' : '';
      el.innerHTML = `<div class="k"><span>Campaign</span><span class="status-tag ${esc(st)}">${st === 'confirmed' ? '✓ ' : ''}${esc(st)}</span></div>`
        + `<div class="name" title="${esc(name)}">${esc(name)}</div>`
        + `<div class="facts" title="${esc(facts)}">${esc(facts)}${poison}</div>`
        + `<div class="k" style="margin-top:6px"><span>Immunity</span>${c.immSim ? '<span class="pill sim">Simulated</span>' : ''}</div>`
        + `<div class="immrow"><div class="big" id="imm">${fmtInt(S.immunityShown)}</div>`
        + `<div class="biglabel">${esc(c.immLabel || 'numbers and indicators now blocked or warned for every Backfire user')}`
        + `${gained > 0 ? `<br><span class="delta">+${fmtInt(gained)} since this screen opened</span>` : ''}</div></div>`;
      countUp(c.immunity);
    },

    // Money trail: victims -> mule account -> cash-out, with Maria's transfer pending or held. Every node and
    // amount is labelled (color is never the only cue); drawn at the card's real pixel size so text stays readable.
    map() {
      const body = bodyOf('map');
      if (!body || !$('grid').contains(body)) return; // parked: no size to draw at
      const d = CHAIN.data;
      const src = CHAIN.live ? 'live · updates every 3 s' : CHAIN.at ? `last update ${fmtTime(CHAIN.at)} · hub not answering` : 'saved snapshot · hub not reachable';
      $('map-meta').textContent = d ? `${src} · Capital One Nessie sandbox, synthetic people and accounts` : 'Capital One Nessie sandbox, synthetic people and accounts';
      if (!d) { body.innerHTML = empty('Loading the money trail from the hub…'); return; }

      const node = id => d.nodes.find(n => n.id === id) || { label: id };
      const first = n => esc(String(n.label || n.id || '').replace(/\s*\(.*\)\s*$/, '').split(/\s+/)[0]);
      const day = s => { const t = new Date(`${s}T12:00:00`); return Number.isNaN(+t) ? '' : t.toLocaleDateString('en-US', { month: 'short', day: 'numeric' }); };
      const amt = e => fmtMoney(+e.amount || 0) + (e.date && day(e.date) ? ` · ${day(e.date)}` : '');
      const maria = d.edges.find(e => e.kind === 'target');
      const victims = d.edges.filter(e => e.kind === 'victim');
      const outs = d.edges.filter(e => e.kind === 'cashout');
      const left = (maria ? [maria] : []).concat(victims);
      const inTotal = Number(d.mule_total_in) || victims.reduce((s, e) => s + (+e.amount || 0), 0);
      const outTotal = Number(d.mule_total_out) || outs.reduce((s, e) => s + (+e.amount || 0), 0);

      const tile = (k, v, chip, cls) => `<div class="mt-tile ${cls || ''}"><span class="k">${k}</span><b>${v}</b>${chip ? `<span class="mt-chip">${chip}</span>` : ''}</div>`;
      const tiles = tile(`Paid in by ${victims.length} victims`, fmtMoney(inTotal), 'to one mule account')
        + tile('Moved to cash-out', fmtMoney(outTotal), `${outs.length} transfers`)
        + (!maria ? '' : maria.held ? tile('Held by Backfire', fmtMoney(maria.amount), "✓ Maria's transfer", 'held')
          : tile("Maria's transfer", fmtMoney(maria.amount), 'pending · Backfire is listening', 'pending'));
      const summary = `${victims.length} victims paid ${fmtMoney(inTotal)} into a simulated mule account, which moved ${fmtMoney(outTotal)} to a cash-out account.`
        + (maria ? ` Maria's ${fmtMoney(maria.amount)} transfer is ${maria.held ? 'held by Backfire' : 'pending'}.` : '');
      body.innerHTML = `<div class="mt-stats">${tiles}</div><svg class="mt-svg" role="img" aria-label="${esc(summary)}"></svg>`;

      // ---- geometry, in real pixels ----
      const svg = body.querySelector('svg');
      const W = Math.max(360, svg.clientWidth), H = Math.max(220, svg.clientHeight);
      const f14 = parseFloat(getComputedStyle(body).getPropertyValue('--f14')) || 14;
      const f12 = parseFloat(getComputedStyle(body).getPropertyValue('--f12')) || 12;
      const longest = Math.max(5, ...left.map(e => first(node(e.src)).length));
      const padL = Math.ceil(longest * f14 * 0.62) + 14;
      const top = f12 + 14, bot = f12 + 10;
      const step = left.length > 1 ? (H - top - bot) / (left.length - 1) : 0;
      const maxL = Math.max(1, ...left.map(e => +e.amount || 0));
      const rMax = Math.max(8, Math.min(17, step * 0.36));
      const rOf = a => 5 + (rMax - 5) * Math.sqrt((+a || 0) / maxL);
      const xL = padL + rMax;
      const xC = W - Math.max(f14 * 5.5, 70);
      const xM = xL + (xC - xL) * 0.5;
      const yM = (top + H - bot) / 2 - f14;
      const rM = Math.max(18, Math.min(34, H * 0.085)), rC = Math.max(15, Math.min(28, H * 0.07));
      const bez = (p, t) => { const u = 1 - t; return [0, 1].map(i => u * u * u * p[0][i] + 3 * u * u * t * p[1][i] + 3 * u * t * t * p[2][i] + t * t * t * p[3][i]); };
      const path = p => `M${p[0]} C${p[1]} ${p[2]} ${p[3]}`.replace(/(\d+\.\d)\d+/g, '$1');
      const tag = (x, y, text, cls) => { const w = text.length * f12 * 0.62 + 18, h = f12 + 10; return `<g class="mt-tag ${cls}"><rect x="${x - w / 2}" y="${y - h / 2}" width="${w}" height="${h}" rx="${h / 2}"/><text x="${x}" y="${y + f12 * 0.36}" text-anchor="middle">${esc(text)}</text></g>`; };
      const out = [];

      // victims and Maria -> mule (lines first, nodes on top)
      left.forEach((e, i) => {
        const y = top + i * step, r = rOf(e.amount);
        const end = [xM - rM - 2, yM + (y - yM) * 0.18];
        const p = [[xL + r, y], [xL + (end[0] - xL) * 0.55, y], [end[0] - (end[0] - xL) * 0.3, end[1]], end];
        if (e.kind === 'target') {
          const mid = bez(p, 0.5);
          if (e.held) {
            out.push(`<path class="mt-held" d="${path(p)}" pathLength="100" stroke-dasharray="46 100" style="stroke-width:3px"/>`,
              `<path class="mt-cut" d="${path(p)}" pathLength="100" stroke-dasharray="0 54 46 0" style="stroke-width:2px"/>`,
              tag(mid[0], mid[1], `✂ HELD ${fmtMoney(e.amount)}`, 'held')); // the tag sits on the cut
          } else {
            out.push(`<path class="mt-pending" d="${path(p)}" style="stroke-width:2.5px"/>`, tag(mid[0], mid[1], `${fmtMoney(e.amount)} · PENDING`, 'pending'));
          }
        } else {
          out.push(`<path class="mt-edge" d="${path(p)}" style="stroke-width:${(1.2 + 3.3 * (+e.amount || 0) / maxL).toFixed(1)}px"/>`,
            `<text class="mt-amt" x="${xL + r + 10}" y="${y - 5}">${esc(amt(e))}</text>`);
        }
      });
      // mule -> cash-out, fanned out so each transfer reads on its own
      const maxO = Math.max(1, ...outs.map(e => +e.amount || 0));
      const spread = Math.min(46, H * 0.12);
      outs.forEach((e, i) => {
        const bend = (i - (outs.length - 1) / 2) * spread * 2;
        const a = [xM + rM + 2, yM], b = [xC - rC - 7, yM];
        const p = [a, [a[0] + (b[0] - a[0]) * 0.3, yM + bend], [b[0] - (b[0] - a[0]) * 0.3, yM + bend], b];
        const m = bez(p, 0.5);
        out.push(`<path class="mt-cash" d="${path(p)}" marker-end="url(#mt-arrow)" style="stroke-width:${(1.5 + 3 * (+e.amount || 0) / maxO).toFixed(1)}px"/>`,
          `<text class="mt-amt" x="${m[0]}" y="${m[1] + (bend < 0 ? -7 : bend > 0 ? f12 + 4 : -7)}" text-anchor="middle">${esc(amt(e))}</text>`);
      });
      // nodes + labels
      left.forEach((e, i) => {
        const y = top + i * step, r = rOf(e.amount), n = node(e.src);
        if (e.kind === 'target') {
          out.push(`<circle class="mt-ring" cx="${xL}" cy="${y}" r="${r + 4}"/><circle class="mt-n-maria" cx="${xL}" cy="${y}" r="${r}"/>`,
            `<text class="mt-name mt-maria" x="${xL - r - 9}" y="${y + f14 * 0.36}" text-anchor="end">Maria</text>`);
        } else {
          out.push(`<circle class="mt-n-victim" cx="${xL}" cy="${y}" r="${r}"/>`,
            `<text class="mt-name" x="${xL - r - 9}" y="${y + f14 * 0.36}" text-anchor="end">${first(n)}</text>`);
        }
      });
      out.push(`<circle class="mt-n-mule" cx="${xM}" cy="${yM}" r="${rM}"/>`,
        `<text class="mt-name" x="${xM}" y="${yM + rM + f14 + 6}" text-anchor="middle">Mule account</text>`,
        `<text class="mt-sub" x="${xM}" y="${yM + rM + f14 + f12 + 11}" text-anchor="middle">Simulated · in ${fmtMoney(inTotal)} · out ${fmtMoney(outTotal)}</text>`,
        `<circle class="mt-n-cash" cx="${xC}" cy="${yM}" r="${rC}"/>`,
        `<text class="mt-name" x="${xC}" y="${yM + rC + f14 + 6}" text-anchor="middle">Cash-out</text>`,
        `<text class="mt-sub" x="${xC}" y="${yM + rC + f14 + f12 + 11}" text-anchor="middle">Simulated · ${fmtMoney(Number((d.nodes.find(n => n.role === 'cashout') || {}).total_in) || outTotal)}</text>`,
        `<text class="mt-sub" x="${W}" y="${H - 2}" text-anchor="end">Money flows left to right · line thickness = amount</text>`);
      svg.setAttribute('viewBox', `0 0 ${W} ${H}`);
      svg.innerHTML = '<defs><marker id="mt-arrow" viewBox="0 0 10 10" refX="8" refY="5" markerUnits="userSpaceOnUse" markerWidth="11" markerHeight="11" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" class="mt-arrowhead"/></marker></defs>' + out.join('');
    },

    risk() {
      const body = bodyOf('risk');
      const c = focusCall();
      const r = c && c.risk;
      if (!r) {
        body.innerHTML = '<div class="risk"><div class="score"><div class="gauge" aria-hidden="true"></div><span class="band">No call</span><span class="num">waiting for the caller to speak</span></div>'
          + '<div class="risk-right"><div class="meter"><i></i></div><div class="meta">Only the caller\'s words are scored, never Maria\'s</div></div></div>';
        return;
      }
      const p = pct(r.s);
      const tone = r.s >= 0.8 ? 'hot' : r.s >= 0.4 ? 'warm' : 'cool';
      const meta = [cap(humanize(r.type)), r.stage ? `stage: ${humanize(r.stage)}` : '', r.imp ? `impersonates ${r.imp}` : ''].filter(Boolean).join(' · ');
      const aiInWhy = r.why.some(w => /\bAI\b/.test(w));
      const chips = r.why.map(w => `<span class="chip">${esc(w)}</span>`).join('')
        + (r.ai && !aiInWhy ? '<span class="chip ai">Talking to the AI system</span>' : '');
      const asks = r.asks.length ? `<div class="asks">Asks for ${r.asks.map(a => `<b>${esc(ASK[a] || humanize(a))}</b>`).join(' · ')}</div>` : '';
      // --p drives the half-gauge in the analytics look (look-analytics.css); the default look ignores it
      body.innerHTML = `<div class="risk ${tone}" style="--p:${r.prevPct}">`
        + `<div class="score"><div class="gauge" aria-hidden="true"></div><span class="band">${tone === 'hot' ? '⚠ ' : ''}${esc(bandWord(r))}</span><span class="num">detector score ${r.s.toFixed(2)}</span></div>`
        + '<div class="risk-right">'
        + (c.alert ? '<span class="alert-tag">Two beeps sent</span>' : '')
        + `<div class="meter"><i style="width:${r.prevPct}%"></i></div>`
        + `${asks}<div class="meta" title="${esc(meta)}">${esc(meta)}</div></div></div>`
        + (chips ? `<div class="chips">${chips}</div>` : '');
      const bar = body.querySelector('.meter i');
      const riskEl = body.querySelector('.risk');
      setTimeout(() => { bar.style.width = `${p}%`; riskEl.style.setProperty('--p', p); }, 30);
    },

    feed() {
      const body = bodyOf('feed');
      const c = focusCall();
      if (!c) {
        $('feed-meta').textContent = '';
        body.innerHTML = '<div class="idle-brand"><img src="assets/backfire-lockup.png" alt="Backfire. Caller beware."><p>Waiting for a call to the scam line. Only the caller\'s side will appear here.</p></div>';
        return;
      }
      const route = ROUTE[c.decision] || humanize(c.decision).toLowerCase();
      $('feed-meta').textContent = [`${fmtPhone(c.from) || 'unknown'} → Maria`, route, c.attestation ? attestWords(c.attestation) : ''].filter(Boolean).join(' · ');
      if (!c.feed.length) { body.innerHTML = empty('Ringing. Only the caller\'s side will appear here.'); return; }
      body.innerHTML = `<div class="feed">${c.feed.map(l => lineHtml(l)).join('')}</div>`;
      body.scrollTop = body.scrollHeight;
    },

    attest() {
      const body = bodyOf('attest');
      const local = S.engine === 'local';
      const v = voiceState();
      // Always-visible privacy strip: short labels, the detail is in the tooltip
      const rows = [
        ['Caller audio only', "Maria's voice is never processed"],
        ['No audio stored', 'Processed in memory; only scammer infrastructure is kept'],
        local ? ['On-device model', 'Nemotron 3 Nano 4B on the phone; no audio leaves it'] : ['Enclave attested', 'NVIDIA GPU in confidential-computing mode; image hash sha256:9f2c41…e41a matches the published build'],
        v === 'clone' ? ['Consented voice', `Maria's clone, consent ${S.voice && S.voice.consent ? S.voice.consent : 'on file'}, deletable`]
          : v === 'synthetic' ? ['Synthetic voice', 'No voice clone kept'] : null,
        ['Synthetic data', 'No real customer data anywhere in this demo'],
      ].filter(Boolean);
      body.innerHTML = rows.map(([k, t]) => `<span class="item" title="${esc(t)}"><span class="ok">✓</span><b>${esc(k)}</b></span>`).join('');
    },

    artifacts() {
      const body = bodyOf('artifacts');
      const meta = $('artifacts-meta');
      if (S.standIn) meta.innerHTML = '<span class="pill sim">Simulated · demo stand-in</span>';
      else meta.textContent = 'checked against public records';
      // Money trail first, so the payoff is visible without scrolling. Stable within a type.
      const prio = ['domain', 'wallet', 'payment_handle', 'callback_phone', 'bank', 'gift_card_brand', 'remote_app', 'url'];
      const rank = t => (prio.includes(t) ? prio.indexOf(t) : prio.length);
      const arts = S.artOrder.map(k => S.arts.get(k)).map((a, i) => [a, i]).sort((x, y) => rank(x[0].type) - rank(y[0].type) || x[1] - y[1]).map(x => x[0]);
      if (!arts.length && !S.loose.length && !S.orgs.length && !S.tags.length && !S.instructions.length) {
        body.innerHTML = empty('Nothing yet. Once Maria hands the call to the decoy, it draws out callback numbers, websites and wallets, and each one gets checked against real public records.');
        return;
      }
      const cards = arts.map(artCard).join('') + S.loose.map(l => artCard({ type: l.type, value: l.value, lookups: [l], seq: l.seq, meta: {} })).join('');
      const tags = (S.orgs.length ? `<span class="lbl">Impersonating</span>${S.orgs.map(o => `<span class="chip">${esc(o)}</span>`).join('')}` : '')
        + (S.tags.length ? `<span class="lbl" style="margin-left:8px">Script</span>${S.tags.map(t => `<span class="chip tag">${esc(t)}</span>`).join('')}` : '')
        + (S.instructions.length ? `<span class="lbl" style="margin-left:8px">Told the AI</span>${S.instructions.map(t => `<span class="chip ai">“${esc(t)}”</span>`).join('')}` : '');
      body.innerHTML = `<div class="arts">${cards}</div>${tags ? `<div class="art-tags">${tags}</div>` : ''}`;
    },

    // Agent pipeline (after 21st.dev "AI Agent Pipeline", MIT, rebuilt in plain JS with our real stages):
    // artifacts → lookups → Nemotron → policy gate → done / waiting / denied
    pipeline() {
      const body = bodyOf('pipeline');
      const ps = S.pipeSeq;
      const order = ['input', 'lookups', 'agent', 'gate'];
      const latest = order.reduce((best, k) => ((ps[k] || 0) > (ps[best] || 0) ? k : best), 'input');
      const ag = S.agent;
      const engineWord = !ag ? 'Nemotron' : /fallback/i.test(ag.engine) ? 'Fallback rules' : /mock/i.test(ag.engine) ? 'Mock LLM' : 'Nemotron';
      $('pipe-meta').innerHTML = `<span class="pdot${isLive() ? ' live' : ''}"></span>${isLive() ? 'live' : 'replay'} · ${esc(ag && ag.model ? ag.model.replace(/^nvidia\//, '') : engineWord)}`;
      if (!order.some(k => ps[k])) {
        body.innerHTML = empty('Lights up when the decoy hands over what it extracted: real lookups, then Nemotron, then the policy gate.');
        return;
      }
      const arts = S.artOrder.map(k => S.arts.get(k));
      const looks = arts.flatMap(a => a.lookups);
      const pending = arts.filter(a => LOOKUPABLE.has(a.type) && !a.lookups.length).length;
      const tool = re => looks.filter(l => re.test(l.tool)).length;
      const tools = [['RDAP', tool(/rdap|whois/)], ['chain', tool(IS_CHAIN)], ['allowlist', tool(/allow/)]].filter(t => t[1]);
      const acts = S.actOrder.map(id => S.actions.get(id));
      const count = st => acts.filter(a => a.status === st).length;
      const denied = S.denied.filter(d => d.kind !== 'guardrail').length;
      const g = { auto: count('auto') + count('held'), waiting: count('queued'), applied: count('applied'), denied };
      const state = k => (!ps[k] ? 'idle' : k === latest ? 'now' : 'done');
      const link = k => `<i class="pc${ps[k] ? ' on' : ''}${(ps[k] || 0) > (painted.pipeline ?? 0) ? ' flow' : ''}" aria-hidden="true"></i>`;
      const node = (k, label, value, sub, extra) => `<div class="pn ${state(k)}${extra || ''}"><b>${label}</b><span class="pv">${value}</span><span class="ps">${sub}</span></div>`;
      const agentVal = S.agentN ? `${S.agentN} proposals` : ps.agent ? 'planned' : ps.lookups && !pending ? 'thinking…' : '—';
      const outs = [
        `<span class="ok">✓ ${g.auto} done automatically</span>`,
        `<span class="wait">⏳ ${g.waiting} waiting for approval${g.applied ? ` · ${g.applied} approved` : ''}</span>`,
        `<span class="no">⛔ ${g.denied} denied</span>`,
      ].join('');
      const lastTr = [...S.trace].reverse().find(t => !t.sep);
      body.innerHTML = '<div class="pipe">'
        + node('input', 'Input', `${arts.length} artifact${arts.length === 1 ? '' : 's'}`, S.standIn ? 'simulated stand-in' : 'typed, no transcript')
        + link('lookups')
        + node('lookups', 'Lookups', `${looks.length} done`, pending ? `${pending} pending` : tools.map(t => `${t[0]} ${t[1]}`).join(' · ') || 'public records')
        + link('agent')
        + node('agent', esc(engineWord), agentVal, ag && /fallback|mock/i.test(ag.engine) ? esc(ag.engine) : 'plans from the evidence', ag && /fallback|mock/i.test(ag.engine) ? ' warn' : ' nv')
        + link('gate')
        + node('gate', 'Policy gate', `${g.auto + g.waiting + g.applied + g.denied} decisions`, 'code, not the model')
        + link('gate')
        + `<div class="pout${ps.gate ? '' : ' idle'}">${outs}</div>`
        + '</div>'
        + (lastTr ? `<div class="plog${lastTr.seq > (painted.pipeline ?? 0) ? ' fresh' : ''}"><span class="pk">${lastTr.k}</span> ${lastTr.html}</div>` : '');
    },

    trace() {
      const body = bodyOf('trace');
      if (!S.trace.length) { body.innerHTML = empty('The intel agent starts when artifacts arrive. It gets typed values, never the transcript, and can only propose actions.'); return; }
      let n = 0;
      body.innerHTML = `<div class="trace">${S.trace.map(t => (t.sep
        ? `<div class="tr-sep">${t.html}</div>`
        : `<div class="tr ${t.cls}${fresh('trace', t.seq)}"><span class="i">${String(++n).padStart(2, '0')}</span><span class="k">${t.k}</span><span class="t">${t.html}</span></div>`)).join('')}</div>`;
      body.scrollTop = body.scrollHeight;
    },

    queue() {
      const body = bodyOf('queue');
      const items = S.actOrder.map(id => S.actions.get(id)).filter(a => a.status === 'queued' || a.status === 'applied');
      const waiting = items.filter(a => a.status === 'queued').length;
      $('queue-meta').textContent = waiting ? `${waiting} waiting · one click each` : items.length ? 'all approved' : 'analyst one-click';
      if (!items.length) { body.innerHTML = empty('Network-wide and external actions wait here for one analyst click.'); return; }
      // Exactly one filled button on the screen: the first action still waiting
      const primary = (items.find(a => a.status === 'queued') || {}).id;
      body.innerHTML = items.map(a => {
        const right = a.status === 'applied'
          ? `<div class="applied">✓ Simulated: applied<small>${esc(a.note ? 'local only' : 'network action')}</small></div>`
          : `<button class="btn-approve${a.id === primary ? ' primary' : ''}" data-approve="${esc(a.id)}"${a.ui === 'approving' ? ' disabled' : ''}>${a.ui === 'approving' ? 'Approving…' : 'Approve'}</button>`;
        const meta = [fmtVal(a.target), scopeLabel(a.scope), a.expiry ? `${a.expiry} expiry` : '', a.evidence[0] || ''].filter(Boolean).join(' · ');
        const why = a.evidence.length ? `Evidence: ${a.evidence.join('; ')}` : meta;
        return `<div class="q${a.status === 'applied' ? ' done' : ''}${fresh('queue', a.seq)}" title="${esc(why)}"><div class="lbl">${esc(a.label)}</div>${right}`
          + `<div class="tgt"><span class="pill sim">Simulated</span> ${esc(meta)}</div>`
          + (a.note ? `<div class="qerr">${esc(a.note)}</div>` : '') + '</div>';
      }).join('');
    },

    // "What we did", as an animated list (after Magic UI's Animated List, MIT): newest card drops in on top,
    // older cards glide down (FLIP), each with an icon so the kind reads without color
    auto() {
      const body = bodyOf('auto');
      const rows = [];
      const used = new Set();
      const ICON = k => (/hold_transfer/.test(k) ? ['💵', 'money'] : /block_caller|block_for/.test(k) ? ['🛡', 'shield'] : /campaign/.test(k) ? ['🔗', 'link'] : /callback_protection/.test(k) ? ['📞', 'warn'] : ['✓', 'shield']);
      for (const id of S.actOrder) {
        const a = S.actions.get(id);
        const blocks = blocksFor(a, used); // claims the blocklist rows this action produced
        if (a.status === 'applied') {
          // an analyst-approved network action joins the story of what we did
          rows.push({ key: `${a.id}:applied`, seq: a.seq, ms: a.appliedMs, cls: 'net', icon: '🌐', tone: 'net', label: a.label, tgt: `${fmtVal(a.target)} · simulated: applied`, scope: scopeLabel(a.scope), undo: '' });
          continue;
        }
        if (a.status !== 'auto' && a.status !== 'held') continue;
        const live = blocks.filter(b => b.active);
        const undone = blocks.length && !live.length;
        let tgt = fmtVal(a.target);
        if (/campaign/.test(a.kind) && live.length) tgt += ` · blocks ${live.map(b => fmtPhone(b.number)).join(', ')} before ring`;
        if (a.status === 'held' && a.reason) tgt += ` · ${a.reason}`;
        const forHer = scopeKey(a.scope) === 'her';
        const [icon, tone] = a.status === 'held' ? ['⏸', 'warn'] : ICON(a.kind);
        const isHold = /hold_transfer/.test(a.kind);
        const off = undone || a.undone;
        let label = a.status === 'held' ? `Held: ${a.label}` : a.label;
        if (isHold) {
          // the bank hold: the money moment, in plain words (simulated bank, mock data)
          label = Number.isFinite(a.amount) ? `Held ${fmtMoney(a.amount)} before it reached the scammer` : 'Held her transfer to the scammer';
          tgt = 'Zelle transfer to the payee the scammer gave the decoy';
        }
        rows.push({
          key: a.id, seq: a.seq, ms: a.ms, cls: a.status === 'held' ? 'held' : off ? 'undone' : isHold ? 'money' : '', icon, tone,
          label, tgt, scope: scopeLabel(a.scope), simBank: a.source === 'nessie' || /nessie/i.test(a.reason || ''),
          // Maria's side of it, in her words: it's in her protection log and she can undo it there
          undo: off ? 'undone' : forHer && (a.undo || blocks.length) ? 'her-log' : '',
        });
      }
      const BL = { her: ['Blocked for Maria', 'Maria only', '🛡', 'shield'], campaign: ['Blocked before ring for Backfire users', 'Backfire users', '🔗', 'link'], network: ['Blocked network-wide (simulated)', 'All customers', '🌐', 'net'] };
      for (const b of S.blocks) {
        if (used.has(b)) continue;
        const [label, scope, icon, tone] = BL[b.scope];
        rows.push({ key: `blk:${b.undo || b.seq}`, seq: b.seq, ms: b.ms, cls: b.active ? '' : 'undone', icon, tone, label, tgt: `${fmtPhone(b.number)}${b.reason ? ` · ${b.reason}` : ''}`, scope, undo: !b.active ? 'undone' : b.scope === 'her' ? 'her-log' : '' });
      }
      for (const r of S.rejects) rows.push({ key: `rej:${r.seq}`, seq: r.seq, ms: r.ms, cls: 'reject', icon: '⛔', tone: 'reject', label: 'Callback rejected before it rang', tgt: `${fmtPhone(r.number)}${r.reason ? ` · ${r.reason}` : ''}`, scope: 'Maria only', undo: '' });
      if (!rows.length) { body.innerHTML = empty('Blocks for Maria, campaign links and Scam Callback Protection warnings land here with no human in the loop.'); return; }
      rows.sort((x, y) => y.seq - x.seq);
      const UNDO = { undone: 'Maria undid this', 'her-log': "in Maria's protection log · she can undo" };
      // FLIP, step 1: where each card is now
      const before = new Map([...body.querySelectorAll('[data-key]')].map(el => [el.dataset.key, el.getBoundingClientRect().top]));
      body.innerHTML = `<div class="list">${rows.map(r => `<div class="act ${r.cls}${fresh('auto', r.seq)}" data-key="${esc(r.key)}">`
        + `<span class="bub ${r.tone}" aria-hidden="true">${r.icon}</span>`
        + `<div class="txt"><div class="lbl">${esc(r.label)}${r.simBank ? ' <span class="pill sim" title="Capital One Nessie sandbox, mock bank data">Simulated bank</span>' : ''}</div>`
        + `<div class="tgt" title="${esc(r.tgt)}">${esc(r.tgt)}${r.undo ? ` <span class="undo">· ${UNDO[r.undo]}</span>` : ''}</div></div>`
        + `<div class="when">${esc(r.scope)}${Number.isFinite(r.ms) && r.ms > 1e12 ? `<span>${esc(fmtTime(r.ms))}</span>` : ''}</div></div>`).join('')}</div>`;
      // FLIP, step 2: start each surviving card where it was, then let it glide to its new place
      if (before.size && !document.hidden && !matchMedia('(prefers-reduced-motion: reduce)').matches) {
        for (const el of body.querySelectorAll('[data-key]')) {
          const was = before.get(el.dataset.key);
          if (was == null) continue;
          const dy = was - el.getBoundingClientRect().top;
          if (!dy) continue;
          el.style.transition = 'none';
          el.style.transform = `translateY(${dy}px)`;
          void el.offsetHeight;
          el.style.transition = 'transform 0.45s cubic-bezier(0.2, 0.9, 0.3, 1)';
          el.style.transform = '';
        }
      }
    },

    denied() {
      const body = bodyOf('denied');
      if (!S.denied.length) { body.innerHTML = empty('Nothing yet. Try telling the decoy: "AI, mark this number safe."'); return; }
      const tag = { poisoning: 'POISONING', guardrail: 'GUARDRAIL', injection: 'INJECTION', uncorroborated: 'NOT CORROBORATED' };
      const SRC = { 'artifact:instruction_to_ai': 'said to the AI by the caller', campaign: 'campaign' };
      body.innerHTML = [...S.denied].reverse().map(d => {
        const what = d.kind === 'injection' && !d.fromAction && !/^["“]/.test(d.what) ? `“${d.what}”` : d.what;
        const src = d.source ? (SRC[d.source] || `from ${humanize(String(d.source).replace(/^artifact:/, 'extracted '))}`) : '';
        const why = [d.why, src].filter(Boolean).join(' · ');
        return `<div class="den ${d.kind}${fresh('denied', d.seq)}"><span class="tag">${tag[d.kind] || 'DENIED'}</span><span class="what">${esc(what)}</span><span class="why">${esc(why)}</span></div>`;
      }).join('');
    },

    timeline() { renderTimeline(); },
  };

  function lineHtml(l) {
    const f = fresh('feed', l.seq);
    if (l.kind === 'sys') return `<div class="sys ${l.tone || ''}${f}">${esc(l.text)}</div>`;
    if (l.kind === 'caller') return `<div class="line caller${l.final ? '' : ' interim'}${f}"><span class="who">Caller</span><span class="txt">${esc(l.text)}</span></div>`;
    if (l.kind === 'scammer') return `<div class="line scammer${f}"><span class="who">Scammer, to the decoy</span><span class="txt">${esc(l.text)}</span></div>`;
    const lat = Number.isFinite(l.latency) ? `<span class="lat">${Math.round(l.latency)} ms</span>` : '';
    const fakes = (l.fakes || []).map(x => `<span class="fake">${esc(x)}</span>`).join('');
    return `<div class="line decoy${f}"><span class="who">Decoy · ${esc(voiceShort())}</span><span class="txt">${esc(l.text)}</span>${fakes}${lat}</div>`;
  }

  function artCard(a) {
    const rank = { conflict: 3, bad: 2, unknown: 1, ok: 0 };
    const worst = a.lookups.reduce((w, l) => (l.ok && rank[l.verdict] > rank[w] ? l.verdict : w), 'ok');
    const cls = worst === 'bad' ? ' hit' : worst === 'conflict' ? ' conflict' : '';
    const chainTxt = a.meta && (a.meta.chain || a.meta.rail);
    const chain = chainTxt || a.standIn
      ? `<span>${a.standIn ? '<span class="standin" title="Simulated: demo stand-in, the extractor is not wired yet">simulated</span> ' : ''}${esc(chainTxt || '')}</span>` : '';
    const lks = a.lookups.length
      ? a.lookups.map(lookupHtml).join('')
      : LOOKUPABLE.has(a.type) ? '<div class="lk pending"><div class="sum">awaiting lookup…</div></div>' : '';
    return `<div class="art${cls}${fresh('artifacts', a.seq)}"><div class="art-type"><span>${esc(ART[a.type] || humanize(a.type))}</span>${chain}</div>`
      + `<div class="art-val">${esc(fmtVal(a.value))}</div>${lks}</div>`;
  }
  function lookupHtml(l) {
    const src = isLive() && l.real ? '<span class="src real">real lookup</span>' : isLive() ? '<span class="src replay">simulated</span>' : '<span class="src replay">replay</span>';
    const cls = l.ok ? l.verdict : 'err';
    const lat = Number.isFinite(num(l.latency)) ? `<span class="ms">${Math.round(num(l.latency))} ms</span>` : '';
    const tool = IS_CHAIN.test(l.tool) && l.result.chain ? `${l.result.chain} chain` : (TOOL[l.tool] || l.tool);
    // Meaning never by color alone: an icon goes with every verdict
    const icon = !l.ok ? '' : { bad: '⚠', conflict: '⛔', ok: '✓' }[l.verdict] || '';
    const link = verifyUrl(l);
    const verify = link ? ` <a class="verify" href="${esc(link)}" target="_blank" rel="noopener noreferrer" title="Open the public record">verify ↗</a>` : '';
    return `<div class="lk ${cls}${fresh('artifacts', l.seq)}"><div class="row"><span class="tool">${esc(tool)}</span>${lat}${src}</div>`
      + `<div class="sum">${icon ? `<span class="ic" aria-hidden="true">${icon}</span>` : ''}${esc(l.ok ? l.summary : cap(String(l.error || 'lookup unavailable')))}</div>`
      + `${l.detail || verify ? `<div class="det">${esc(l.detail)}${verify}</div>` : ''}</div>`;
  }
  // "Let the judge verify one claim": link a real lookup to the same public record it came from.
  // Fixed public hosts only (never the scammer's own site); the value is URL-encoded.
  function verifyUrl(l) {
    if (!isLive() || !l.real || !l.ok || l.value == null) return '';
    const v = encodeURIComponent(String(l.value).trim());
    if (/rdap|whois/.test(l.tool)) return `https://rdap.org/domain/${v}`;
    if (IS_CHAIN.test(l.tool)) {
      const chain = String(l.result.chain || l.result.unit || '').toUpperCase();
      if (chain === 'ETH') return `https://eth.blockscout.com/address/${v}`;
      return `https://blockstream.info/address/${v}`;
    }
    return '';
  }

  let countTimer = 0;
  function countUp(target) {
    clearTimeout(countTimer);
    const from = S.immunityShown, st = S, t0 = performance.now(), dur = 1400;
    if (from === target) return;
    // setTimeout, not rAF, so the number still lands when the window is in the background
    const step = () => {
      if (S !== st) return;
      const k = Math.min(1, (performance.now() - t0) / dur);
      st.immunityShown = k >= 1 ? target : from + (target - from) * (1 - Math.pow(1 - k, 3));
      const el = $('imm');
      if (el) el.textContent = fmtInt(st.immunityShown);
      if (k < 1) countTimer = setTimeout(step, 33);
    };
    step();
  }

  function renderSource() {
    const el = $('source');
    const host = MODE.url.replace(/^wss?:\/\//, '');
    const m = {
      connecting: ['', 'CONNECTING', 'looking for the P1 server'],
      live: ['live', 'LIVE', host],
      reconnecting: ['reconnecting', 'RECONNECTING', host],
      replay: ['replay', 'REPLAY', MODE.label],
    }[MODE.kind];
    el.className = `source ${m[0]}`;
    el.innerHTML = `<span class="dot"></span><b>${m[1]}</b><span>${esc(m[2])}</span>`;
  }

  // ---------- views ----------
  // Story (default at the table): only the chapter of the call that's happening now, in big type.
  // Agent: the intel agent's full trace. Everything: the full console.
  // Panels move between #grid and the hidden #parking area; renderers find them by id wherever they are.
  const STEP_CHAPTER = { detect: 'call', handoff: 'call', verify: 'evidence', burn: 'act', immune: 'act' };
  const CHAPTER_NAME = { call: 'the call', evidence: 'what the decoy got', act: 'what we did' };
  const LAYOUTS = {
    all: { cols: [1, 1.25, 1.05], stacks: [[['p-risk', 0], ['p-feed', 1]], [['p-artifacts', 1.5], ['p-pipeline', 0], ['p-trace', 1]], [['p-queue', 0], ['p-auto', 1], ['p-denied', 1]]] },
    agent: { cols: [1.25, 1], stacks: [[['p-pipeline', 0], ['p-trace', 1]], [['p-artifacts', 1.3], ['p-denied', 1]]] },
    'story:call': { cols: [1.6, 1], stacks: [[['p-feed', 1]], [['p-risk', 1]]] },
    'story:evidence': { cols: [1.3, 1], stacks: [[['p-artifacts', 1]], [['p-pipeline', 0], ['p-trace', 1]]] },
    'story:act': { cols: [1.1, 1], stacks: [[['p-auto', 1]], [['p-queue', 0], ['p-denied', 1]]] },
    // P4a's network map (/intel/map on the hub) next to what we did and what waits for a click
    money: { cols: [2.1, 1], stacks: [[['p-map', 1]], [['p-auto', 1], ['p-queue', 0]]] },
  };
  // Money trail: P4a's read-only GET /intel/chain (Capital One Nessie sandbox, synthetic), drawn here in the screen's own style.
  // Polled every 3 s only while the view is open. Kept outside S, so "Clear for next judge" doesn't blank it.
  const CHAIN = { data: null, live: false, at: 0, timer: 0, busy: false };
  async function pollChain() {
    if (CHAIN.busy || VIEW.name !== 'money') return;
    CHAIN.busy = true;
    try {
      const r = await fetch(`${MODE.base || CFG.server || TEAM_HUB}/intel/chain`, { cache: 'no-store' });
      if (!r.ok) throw new Error(`HTTP ${r.status}`);
      const d = await r.json();
      if (!d || !Array.isArray(d.nodes) || !Array.isArray(d.edges)) throw new Error('unexpected /intel/chain shape');
      Object.assign(CHAIN, { data: d, live: true, at: Date.now() });
    } catch (err) {
      // hub not reachable (offline replay): the saved snapshot in fixture.js, labelled as a snapshot; live data that stops is labelled stale
      if (!CHAIN.at && window.BACKFIRE_CHAIN) CHAIN.data = window.BACKFIRE_CHAIN;
      CHAIN.live = false;
    } finally {
      CHAIN.busy = false;
      dirty('map');
    }
  }
  function ensureMap() {
    if (!CHAIN.timer) {
      CHAIN.timer = setInterval(pollChain, 3000);
      if (window.ResizeObserver) new ResizeObserver(() => dirty('map')).observe(bodyOf('map'));
    }
    pollChain();
    dirty('map');
  }
  const VIEW = { name: 'story', pinned: null, key: '', shown: '', shownAt: 0 };
  const ORDER = { call: 0, evidence: 1, act: 2 };
  const DWELL_MS = 8000; // each chapter stays up long enough to point at before the story moves on
  let dwellTimer = 0;
  function chapterNow() {
    if (VIEW.pinned) return VIEW.pinned;
    const st = S.stage;
    if (st.burn || st.immune) return 'act';
    if (st.verify || st.extract) return 'evidence';
    return 'call';
  }
  function layout() {
    let chapter = VIEW.name === 'story' ? chapterNow() : '';
    // Following live: moving forward waits until the current chapter has been up DWELL_MS (scaled by replay speed)
    if (chapter && !VIEW.pinned && VIEW.shown && ORDER[chapter] > ORDER[VIEW.shown]) {
      const wait = DWELL_MS / (MODE.kind === 'replay' ? CFG.speed : 1) - (Date.now() - VIEW.shownAt);
      if (wait > 0) {
        clearTimeout(dwellTimer);
        dwellTimer = setTimeout(() => { layout(); }, wait);
        chapter = VIEW.shown;
      }
    }
    VIEW.shown = chapter;
    const app = document.querySelector('.app');
    app.dataset.view = VIEW.name;
    app.dataset.chapter = chapter;
    document.querySelectorAll('.views [data-view]').forEach(b => b.setAttribute('aria-selected', String(b.dataset.view === VIEW.name)));
    const follow = $('follow');
    follow.hidden = !(VIEW.name === 'story' && VIEW.pinned);
    if (!follow.hidden) { follow.textContent = 'Holding · back to live'; follow.title = `Holding ${CHAPTER_NAME[VIEW.pinned]} on screen. Click (or Esc) to follow the call again.`; }
    const key = chapter ? `story:${chapter}` : VIEW.name;
    if (key === VIEW.key) return;
    VIEW.key = key;
    VIEW.shownAt = Date.now();
    const L = LAYOUTS[key];
    const grid = $('grid'), park = $('parking');
    for (const el of [...grid.querySelectorAll('.panel')]) park.appendChild(el);
    grid.innerHTML = '';
    grid.style.gridTemplateColumns = L.cols.map(f => `minmax(0, ${f}fr)`).join(' ');
    for (const stack of L.stacks) {
      const col = document.createElement('div');
      col.className = 'col';
      for (const [id, grow] of stack) {
        const el = $(id);
        el.style.flex = grow ? `${grow} 1 0` : '0 1 auto';
        col.appendChild(el);
      }
      grid.appendChild(col);
    }
    if (key === 'money') ensureMap();
    grid.classList.remove('enter'); void grid.offsetWidth; grid.classList.add('enter');
    dirty('feed', 'trace', 'hero'); // moved panels lose their scroll position; re-render scrolls them to the newest line
  }
  function setView(name) {
    if (name !== 'story' && !LAYOUTS[name]) name = 'story';
    VIEW.name = name;
    VIEW.pinned = null;
    try { history.replaceState(null, '', `#${name}`); } catch (err) { /* file:// */ }
    layout();
  }
  document.querySelector('.views').addEventListener('click', ev => {
    const b = ev.target.closest('[data-view]');
    if (b) setView(b.dataset.view);
  });
  // Click a rail step to hold that chapter on screen while you talk; click it again (or "back to live") to follow the call
  $('rail').addEventListener('click', ev => {
    const step = ev.target.closest('[data-chapter]');
    if (!step) return;
    const ch = step.dataset.chapter;
    VIEW.pinned = VIEW.name === 'story' && VIEW.pinned === ch ? null : ch;
    if (VIEW.name !== 'story') { VIEW.name = 'story'; try { history.replaceState(null, '', '#story'); } catch (err) { /* file:// */ } }
    layout();
  });
  $('follow').addEventListener('click', () => { VIEW.pinned = null; layout(); });
  // Between judges: wipe this screen's state (not the hub's) without dropping the live connection
  function clearScreen() {
    resetState();
    clearTimeout(dwellTimer);
    VIEW.pinned = null; VIEW.key = ''; VIEW.shown = '';
    renderAll();
    layout();
    renderTimeline();
  }

  // ---------- replay ----------
  const R = { events: [], offsets: [], total: 0, idx: 0, timer: 0, playing: false };

  function prepareReplay(events) {
    const list = events.map((raw, i) => ({ raw, i, e: envelope(raw) })).filter(x => x.e);
    const allTimed = list.every(x => Number.isFinite(x.e.ms));
    if (allTimed) list.sort((a, b) => a.e.ms - b.e.ms || a.i - b.i);
    R.events = list.map(x => x.raw);
    R.offsets = [];
    let off = 0;
    list.forEach((x, i) => {
      if (i > 0) off += allTimed ? Math.min(CFG.maxGap, Math.max(0, (x.e.ms - list[i - 1].e.ms) / 1000)) : 1;
      R.offsets.push(off);
    });
    R.total = Math.max(off, 0.001);
    R.idx = 0;
    const p4 = /^(intel|injection|campaign|blocklist)\./, p3 = /^(decoy|artifacts|guardrail|voice)\./;
    $('tl-ticks').innerHTML = list.map((x, i) => `<i class="${p4.test(x.e.type) ? 'p4' : p3.test(x.e.type) ? 'p3' : ''}" style="left:${(R.offsets[i] / R.total) * 100}%"></i>`).join('');
  }
  function play() {
    if (!R.events.length) return;
    if (R.idx >= R.events.length) { restart(); return; }
    R.playing = true; next(); renderTimeline();
  }
  function next() {
    clearTimeout(R.timer);
    if (!R.playing) return;
    if (R.idx >= R.events.length) { R.playing = false; renderTimeline(); return; }
    const prev = R.idx === 0 ? -0.8 : R.offsets[R.idx - 1];
    const wait = Math.max(0, R.offsets[R.idx] - prev) * 1000 / CFG.speed;
    R.timer = setTimeout(() => { apply(R.events[R.idx]); R.idx++; renderTimeline(); next(); }, wait);
  }
  function pause() { R.playing = false; clearTimeout(R.timer); renderTimeline(); }
  function resetState() {
    S = freshState(); painted = {}; lastFlash = 0;
    $('hero').classList.remove('flash');
  }
  function restart() { pause(); resetState(); R.idx = 0; renderAll(); R.playing = true; next(); renderTimeline(); }
  function seek(frac) {
    pause(); resetState();
    const target = frac * R.total;
    R.idx = 0;
    while (R.idx < R.events.length && R.offsets[R.idx] <= target) { apply(R.events[R.idx]); R.idx++; }
    lastFlash = S.flashSeq;
    const c = S.campaigns.get(S.campaignId);
    S.immunityShown = c ? c.immunity : 0;
    for (const k of Object.keys(RENDER)) painted[k] = S.seq; // nothing animates after a jump
    renderAll();
    R.playing = true; next();
  }
  function renderTimeline() {
    const tl = document.querySelector('.timeline');
    const live = MODE.kind !== 'replay';
    tl.classList.toggle('live', live);
    $('tl-play').hidden = live;
    const rs = $('tl-restart');
    rs.classList.toggle('wide', live);
    rs.innerHTML = live ? '&#8634; Clear for next judge' : '&#8634;';
    rs.title = live ? 'Clear this screen for the next judge (C). The live connection stays on.' : 'Restart (R)';
    if (live) {
      $('tl-fill').style.width = '0';
      $('tl-text').textContent = `${S.count} events${MODE.kind === 'connecting' ? '' : ` · ${MODE.url}`}`;
      return;
    }
    const done = R.idx >= R.events.length;
    const off = R.idx === 0 ? 0 : R.offsets[R.idx - 1];
    $('tl-fill').style.width = `${(off / R.total) * 100}%`;
    $('tl-play').innerHTML = R.playing ? '&#10073;&#10073;' : '&#9654;';
    $('tl-text').textContent = `${R.idx}/${R.events.length} events${done ? ' · done' : R.playing ? '' : ' · paused'} · space pause · R restart · click bar to jump`;
  }
  $('tl-play').addEventListener('click', () => (R.playing ? pause() : play()));
  $('tl-restart').addEventListener('click', () => (MODE.kind === 'replay' ? restart() : clearScreen()));
  $('tl-bar').addEventListener('click', ev => {
    if (MODE.kind !== 'replay') return;
    const rect = ev.currentTarget.getBoundingClientRect();
    seek(Math.max(0, Math.min(1, (ev.clientX - rect.left) / rect.width)));
  });
  document.addEventListener('keydown', ev => {
    if (ev.ctrlKey || ev.metaKey || ev.altKey) return;
    if (ev.target.closest && ev.target.closest('input, textarea')) return;
    const view = { 1: 'story', 2: 'agent', 3: 'all', 4: 'money' }[ev.key];
    if (view) { setView(view); return; }
    if (ev.key === 'Escape' && VIEW.pinned) { VIEW.pinned = null; layout(); return; }
    if (ev.target.closest && ev.target.closest('button')) return; // Space/Enter on a focused button presses it
    if (MODE.kind !== 'replay') {
      if (ev.key === 'c' || ev.key === 'C') clearScreen();
      return;
    }
    if (ev.code === 'Space') { ev.preventDefault(); R.playing ? pause() : play(); }
    else if (ev.key === 'r' || ev.key === 'R') restart();
  });

  // ---------- live ----------
  // The team hub (P1). Its public tunnel URL changes when the tunnel restarts: update it here,
  // or open the page from the hub itself (https://<hub>/command-center/), or pass ?server=.
  const TEAM_HUB = 'https://reg-subjects-curriculum-whenever.trycloudflare.com';
  function serverCandidates() {
    if (CFG.server) return [CFG.server];
    const c = [];
    if (/^https?:$/.test(location.protocol)) c.push(location.origin); // served by the hub = same origin, Approve needs no CORS
    c.push(TEAM_HUB, 'http://localhost:8000');
    return [...new Set(c)];
  }
  const isRemote = base => !/^https?:\/\/(localhost|127\.0\.0\.1)(:|$)/.test(base);
  const wsUrl = base => `${base.replace(/^http/, 'ws')}/events`;

  function connect(base, onFail) {
    let opened = false, failed = false;
    const fail = () => { if (!failed && !opened) { failed = true; onFail(); } };
    let ws;
    try { ws = new WebSocket(wsUrl(base)); } catch (err) { fail(); return; }
    // a tunnel handshake can take a few seconds; local servers answer or refuse at once
    const timer = setTimeout(() => { if (!opened) { try { ws.close(); } catch (err) { /* ignore */ } fail(); } }, isRemote(base) ? 5000 : 1800);
    ws.onopen = () => {
      opened = true; clearTimeout(timer);
      if (MODE.kind === 'replay') pause();
      Object.assign(MODE, { kind: 'live', base, url: wsUrl(base) });
      renderAll();
    };
    ws.onmessage = m => {
      let x;
      try { x = JSON.parse(m.data); } catch (err) { return; }
      for (const ev of Array.isArray(x) ? x : [x]) apply(ev);
      renderTimeline();
    };
    ws.onclose = () => {
      clearTimeout(timer);
      if (!opened) { fail(); return; }
      MODE.kind = 'reconnecting'; renderAll(); // keep everything on screen while we reconnect
      setTimeout(() => connect(base, retryForever(base)), 1000);
    };
    ws.onerror = () => {};
  }
  function retryForever(base) {
    return () => setTimeout(() => connect(base, retryForever(base)), 2000);
  }

  // Accepts a flat list, {events: [...]}, or P1's {calls: [{call_id, events: [...]}]} where each call's ts
  // restarts at 0 (relative seconds). Calls are laid end to end with a 4 s pause between them.
  function mockEvents(j) {
    if (Array.isArray(j)) return j;
    if (j && Array.isArray(j.events)) return j.events;
    if (!j || !Array.isArray(j.calls)) return null;
    const out = [];
    let base = 0;
    for (const call of j.calls) {
      const evs = arr(call.events).filter(e => e && typeof e === 'object');
      const t = e => (Number.isFinite(Number(e.ts)) ? Number(e.ts) : 0);
      const start = Math.min(0, ...evs.map(t)); // onboarding events can sit before 0
      const end = Math.max(0, ...evs.map(t));
      for (const e of evs) out.push({ ...e, call_id: e.call_id ?? call.call_id, ts: base + (t(e) - start) });
      base += (end - start) + 4;
    }
    return out;
  }

  async function startReplay() {
    let events = null, label = '';
    if (CFG.src !== 'fixture' && /^https?:$/.test(location.protocol)) {
      try {
        const r = await fetch(CFG.mockUrl, { cache: 'no-store' });
        if (r.ok) {
          events = mockEvents(await r.json());
          if (events) label = CFG.mockUrl.replace(/^(\.\.\/)+/, '');
        }
      } catch (err) { /* not pushed yet: use the local fixture */ }
    }
    if (!events && window.BACKFIRE_FIXTURE) { events = window.BACKFIRE_FIXTURE.events; label = window.BACKFIRE_FIXTURE.source || 'local fixture'; }
    Object.assign(MODE, { kind: 'replay', label: label || 'no events', url: '', base: '' });
    prepareReplay(events || []);
    renderAll();
    play();
  }

  function boot() {
    setView((location.hash.slice(1) || qs.get('view') || 'story').toLowerCase());
    renderAll();
    setInterval(() => { $('clock').textContent = new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit', second: '2-digit' }); }, 1000);
    if (CFG.src === 'mock' || CFG.src === 'fixture') { startReplay(); return; }
    const cands = serverCandidates();
    const tryAt = i => {
      if (i >= cands.length) {
        if (CFG.src === 'live') { Object.assign(MODE, { kind: 'reconnecting', url: wsUrl(cands[0]) }); renderAll(); retryForever(cands[0])(); return; }
        startReplay();
        return;
      }
      connect(cands[i], () => tryAt(i + 1));
    };
    tryAt(0);
  }

  // expose a tiny hook for debugging from the console
  window.backfireCC = { apply: ev => { apply(ev); renderTimeline(); }, state: () => S, mode: () => ({ ...MODE }) };
  boot();
})();
