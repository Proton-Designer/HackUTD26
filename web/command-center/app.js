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
    block_caller_for_customer: 'Block caller for the customer', link_campaign: 'Link to campaign, block its numbers before ring',
    callback_protection_warning: 'Add callback number to Scam Callback Protection', network_number_block: 'Block calling number network-wide',
    number_block_network: 'Block calling number network-wide', dns_block_registrar_report: 'DNS block + registrar abuse report',
    exchange_freeze_request: 'Exchange freeze request for the wallet', ftc_ic3_packet: 'FTC + IC3 report packet',
    hold_transfer: 'Stopped the transfer to the scammer', flag_payee_bankwide: 'Flag this account for every customer',
    mark_number_safe: 'Mark number safe', add_trusted_contact: 'Add trusted contact', unblock_number: 'Unblock number', allowlist_add: 'Add to allowlist',
    block_for_customer: 'Block caller for the customer', campaign_link: 'Link to campaign', callback_protection: 'Add to Callback Protection',
    network_block: 'Block number network-wide', dns_block: 'DNS block + registrar report', freeze_request: 'Freeze request',
    report_packet: 'FTC + IC3 report packet', ftc_ic3: 'FTC + IC3 report packet',
  };
  // Trust changes only Maria can make in her app; when they come from untrusted input they're injection attempts
  const TRUST_ASK = { mark_number_safe: t => `Mark ${t} as safe`, add_trusted_contact: t => `Add ${t} as a trusted contact`, unblock_number: t => `Unblock ${t}`, allowlist_add: t => `Allowlist ${t}` };
  const ENDED_BY = { maria: 'the customer', caller: 'the caller', decoy: 'the decoy', system: 'the system', scammer: 'the scammer', network_reject: 'the network' };
  const ROUTE = { NORMAL: 'rang normally', LIVE_GUARD: 'Live Guard on', BLOCKED_BACKFIRE: 'blocked before ring' };
  // Five steps (the kit caps a demo path at five), grouped in the brief's own words: during, after, before the next ring.
  // 'extract' is tracked separately but shown inside Verify.
  const STAGES = [['detect', 'Detect'], ['handoff', 'Hand off'], ['verify', 'Verify'], ['burn', 'Block'], ['immune', 'Immune']];
  const PHASES = [['During the call', 1, 3], ['After the call', 3, 5], ['Before the next ring', 5, 6]];
  // Contract bands as words, never a bare percentage ("honest confidence")
  const BAND = { low: 'Low risk', watch: 'Watch', high: 'Likely scam', critical: 'Scam' };
  const ASK_PHRASE = { otp: 'a one-time code', card: 'a card number', ssn: 'a Social Security number', gift_card: 'gift cards', crypto: 'crypto', wire: 'a wire transfer', p2p: 'a P2P payment', remote_app: 'remote access to the phone', secrecy: 'secrecy' };
  // An alert stays an alert while P2 reports a high/critical band, even when it holds s lower (#103)
  const isHot = r => !!r && (r.s >= 0.8 || ['high', 'critical'].includes(String(r.band || '').toLowerCase()));
  // What the gauge shows: the score, or the call's peak while the alert is held
  const shownPct = r => pct(isHot(r) ? Math.max(r.s, r.peak || 0) : r.s);
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
  const scopeLabel = s => ({ her: 'This customer only', backfire: 'Backfire users', all: 'All customers', external: 'External' }[scopeKey(s)]);

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
  const voiceName = () => ({ clone: "the customer's consented voice", synthetic: 'a synthetic voice', unknown: 'the decoy voice' }[voiceState()]);
  const voiceShort = () => ({ clone: "the customer's voice", synthetic: 'synthetic voice', unknown: 'decoy voice' }[voiceState()]);

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
  // ---------- the money ending (Capital One Nessie sandbox) ----------
  // Where the scammer's money stands, from the bank actions P4a emits: hold_transfer (auto, cancels the customer's
  // pending Zelle in the sandbox) and flag_payee_bankwide (queued for one analyst click, simulated payload).
  function moneyState() {
    const acts = S.actOrder.map(id => S.actions.get(id)).filter(a => a.status !== 'denied');
    const hold = acts.find(a => /hold_transfer/.test(a.kind));
    const flag = acts.find(a => /flag_payee/.test(a.kind));
    const block = acts.find(a => /block_caller/.test(a.kind) && a.status === 'auto');
    const handle = S.artOrder.map(k => S.arts.get(k)).find(a => a.type === 'payment_handle');
    const stopped = !!(hold && hold.status === 'auto' && !hold.undone);
    const amount = hold && Number.isFinite(hold.amount) ? hold.amount : NaN;
    return { hold, flag, block, handle, stopped, amount, flagged: !!(flag && flag.status === 'applied'), rejected: S.rejects.length > 0 };
  }
  const handleText = a => `${a.meta && a.meta.rail ? `${cap(String(a.meta.rail))} · ` : ''}${a.value}`;
  // The banner during the ending: money stopped, then the final line once the account is flagged
  function finale() {
    const m = moneyState();
    const amt = Number.isFinite(m.amount) ? fmtMoney(m.amount) : 'the money';
    if (m.flagged) {
      head('Scammer get scammed. <em>He got $0.</em>',
        [m.stopped ? `The customer kept ${amt}` : '', 'his account is flagged for every customer',
          m.rejected ? 'his callback never rang' : ''].filter(Boolean).join(' · '), 'win');
      S.flashSeq = S.seq;
      return true;
    }
    if (m.stopped) {
      head(`<em>${amt} stopped</em> before it reached the scammer`,
        "Pending Zelle cancelled in Capital One's Nessie sandbox (mock bank data) · the customer can undo", 'win');
      return true;
    }
    return false;
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
        if (!moneyState().flagged) head(`<em>${esc(fmtPhone(c.from))}</em> called back. Rejected before it rang.`, c.reason || 'Confirmed scammer', 'win');
        else finale();
        S.flashSeq = S.seq;
      } else if (c.decision === 'LIVE_GUARD') {
        head('Ringing the customer with <em>Live Guard on</em>', `${fmtPhone(c.from)} · ${c.reason}`, '');
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
      head('The customer answered. Live Guard hears <em>the caller only</em>.', listen ? 'Answered in the Backfire app · the customer’s voice is never processed' : 'The customer’s voice is never processed', '');
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
      c.risk = { s: num(d.s) || 0, band: d.band || '', asks: arr(d.asks), type: d.scam_type || '', stage: d.stage || '', imp: d.impersonates || '', ai: !!d.addresses_ai_system, why: arr(d.why_chips), prevPct: prev ? shownPct(prev) : 0 };
      if (isHot(c.risk)) c.risk.peak = Math.max(prev && prev.peak || 0, c.risk.s);
      if (d.engine) S.engine = String(d.engine).toLowerCase();
      if (d.model) S.model = String(d.model);
      const p = pct(c.risk.s);
      const word = bandWord(c.risk);
      if (c.risk.s >= 0.5) stage('detect', word.toLowerCase());
      if ((!c.handoff || c.restored) && !S.stage.extract) {
        if (isHot(c.risk)) {
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
      c.feed.push({ kind: 'sys', tone: 'hot', seq: S.seq, text: d.level === 'realert' ? 'Risk rose: two more beeps to the customer' : 'Two beeps to the customer: Continue · Fire Back · Hang up' });
      stage('detect');
      dirty('risk', 'feed');
    },
    'user.action'(e, d, c) {
      const a = String(d.action || '');
      const text = { scammer_get_scammed: 'The customer tapped Fire Back', hang_up: 'The customer hung up', continue: 'The customer tapped Continue' }[a] || `Customer: ${humanize(a)}`;
      c.feed.push({ kind: 'sys', tone: a === 'scammer_get_scammed' ? 'hot' : '', text, seq: S.seq });
      if (a === 'scammer_get_scammed') {
        stage('handoff', 'customer tapped it');
        head('The customer tapped <em>Fire Back</em>', 'The network swaps them out. The decoy keeps the scammer talking.', 'alert');
      }
      dirty('feed');
    },
    'handoff.started'(e, d, c) {
      c.handoff = true; c.restored = false; focusOn(c);
      const dlMs = tsMs(d.restore_deadline); // mocks use relative seconds; only show a real clock time
      const dl = Number.isFinite(dlMs) && dlMs > 1e12 ? ` · the customer can step back in until ${fmtTime(dlMs)}` : '';
      c.feed.push({ kind: 'sys', tone: 'hot', text: `Decoy took over in ${voiceName()}${dl}`, seq: S.seq });
      stage('handoff', voiceShort());
      head(`The decoy took over in <em>${esc(voiceName())}</em>`, 'The scammer is now talking to Nemotron. The customer is off the call.', 'alert');
      dirty('feed');
    },
    'handoff.restored'(e, d, c) {
      c.restored = true;
      c.feed.push({ kind: 'sys', text: 'The customer is back on the call (decoy stepped out)', seq: S.seq });
      // The banner must not keep saying "the customer is off the call" (#106); risk.update takes over again below
      head('The customer is <em>back on the call</em>', 'The decoy stepped out', '');
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
      auto: ['gate auto', 'GATE', `${tgt}auto-applied ✓ <span class="res">· affects only this customer or only adds a warning</span>`],
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
    return held ? `${fmtMoney(held)} stopped` : auto ? `${auto} protection${auto === 1 ? '' : 's'}` : queued ? 'waiting for one click' : applied ? 'approved' : '';
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
    if (finale()) {
      // the money leads the banner from here to the close
    } else if (!S.rejects.length && (auto.length || queued.length)) {
      const qn = `${queued.length} waiting for one click`;
      const text = auto.length
        ? `<em>${auto.length} protection${auto.length === 1 ? '' : 's'}</em> applied automatically${queued.length ? `, <em>${qn}</em>` : ''}`
        : `<em>${queued.length} network action${queued.length === 1 ? '' : 's'}</em> waiting for one click`;
      head(text, (auto.length ? auto : queued).map(a => a.label).join(' · '), 'alert');
    }
    dirty('payoff', 'map');
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
    if (stageOf) S.pipeSeq[stageOf] = S.seq;
    if (/^(intel\.action|artifacts\.extracted|call\.routed|blocklist\.updated)$/.test(e.type)) dirty('payoff', 'map');
  }

  // ---------- approve (one click) ----------
  async function approve(id) {
    const st = S;
    const a = st.actions.get(id);
    if (!a || a.status !== 'queued' || a.ui === 'approving') return;
    a.ui = 'approving'; a.err = '';
    dirty('payoff');
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
      note = ''; // replay: applied on this screen only
    }
    if (S !== st) return; // replay restarted while the request was in flight
    st.seq++;
    a.ui = ''; a.note = note;
    if (a.status === 'queued') { a.status = 'applied'; a.seq = st.seq; a.appliedMs = Date.now(); gateTrace(a); }
    st.pipeSeq.gate = st.seq;
    stage('immune', /flag_payee/.test(a.kind) ? 'account flagged' : 'approved');
    afterActions();
    if (!/flag_payee/.test(a.kind)) head(`Approved: <em>${esc(a.label)}</em>`, `Simulated network action applied${a.expiry ? ` · ${a.expiry} expiry` : ''} · reversible`, 'win');
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
      if (!el) return; // engine and source pills are off the screen
      const model = S.model;
      if (S.engine === 'local') { el.className = 'engine local'; el.innerHTML = `<b>LOCAL</b><span>${esc(model || 'Nemotron Nano 4B')} · our server, laptop GPU</span>`; }
      else if (S.engine === 'cloud') { el.className = 'engine cloud'; el.innerHTML = `<b>CLOUD</b><span>${esc(model || 'Nemotron')} · NVIDIA-hosted</span>`; }
      else { el.className = 'engine'; el.innerHTML = '<b>ENGINE</b><span>waiting for detector</span>'; }
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

    // Money trail: victims -> mule account -> cash-out, with the customer's transfer pending or stopped, and the
    // mule tagged once the analyst flags it. Every node and amount is labelled (color is never the only cue).
    map() {
      const body = bodyOf('map');
      if (!body || !$('grid').contains(body)) return; // parked: no size to draw at
      const d = CHAIN.data;
      const src = CHAIN.live ? 'live' : CHAIN.at ? `last update ${fmtTime(CHAIN.at)} · hub not answering` : 'saved snapshot';
      $('map-meta').textContent = CHAIN.live ? 'Capital One Nessie sandbox · mock data' : `Capital One Nessie sandbox · mock data · ${src}`;
      if (!d) { body.innerHTML = empty('Loading the money trail from the hub…'); return; }
      const ms = moneyState(); // the screen's own events can be ahead of the 3 s poll

      const node = id => d.nodes.find(n => n.id === id) || { label: id };
      const first = n => esc(String(n.label || n.id || '').replace(/\s*\(.*\)\s*$/, '').split(/\s+/)[0]);
      const day = s => { const t = new Date(`${s}T12:00:00`); return Number.isNaN(+t) ? '' : t.toLocaleDateString('en-US', { month: 'short', day: 'numeric' }); };
      const amt = e => fmtMoney(+e.amount || 0) + (e.date && day(e.date) ? ` · ${day(e.date)}` : '');
      const target = d.edges.find(e => e.kind === 'target');
      const maria = target && { ...target, held: !!target.held || ms.stopped, amount: Number.isFinite(ms.amount) ? ms.amount : target.amount };
      const victims = d.edges.filter(e => e.kind === 'victim');
      const outs = d.edges.filter(e => e.kind === 'cashout');
      const left = (maria ? [maria] : []).concat(victims);
      const inTotal = Number(d.mule_total_in) || victims.reduce((s, e) => s + (+e.amount || 0), 0);
      const outTotal = Number(d.mule_total_out) || outs.reduce((s, e) => s + (+e.amount || 0), 0);

      const tile = (k, v, chip, cls) => `<div class="mt-tile ${cls || ''}"><span class="k">${k}</span><b>${v}</b>${chip ? `<span class="mt-chip">${chip}</span>` : ''}</div>`;
      const tiles = tile(`Paid in by ${victims.length} victims`, fmtMoney(inTotal), ms.flagged ? '⚑ account flagged' : 'into one account', ms.flagged ? 'flagged' : '')
        + tile('Moved to cash-out', fmtMoney(outTotal), `${outs.length} transfers`)
        + (!maria ? '' : maria.held ? tile('Stopped by Backfire', fmtMoney(maria.amount), '✓ customer kept it', 'held')
          : tile("The customer's transfer", fmtMoney(maria.amount), 'pending · Backfire is listening', 'pending'));
      const summary = `${victims.length} victims paid ${fmtMoney(inTotal)} into a simulated mule account, which moved ${fmtMoney(outTotal)} to a cash-out account.`
        + (maria ? ` The customer's ${fmtMoney(maria.amount)} transfer is ${maria.held ? 'stopped by Backfire' : 'pending'}.` : '')
        + (ms.flagged ? ' The mule account is flagged for every customer.' : '');
      body.innerHTML = `<div class="mt-stats">${tiles}</div><svg class="mt-svg" role="img" aria-label="${esc(summary)}"></svg>`;

      // ---- geometry, in real pixels ----
      const svg = body.querySelector('svg');
      const W = Math.max(360, svg.clientWidth), H = Math.max(220, svg.clientHeight);
      const f14 = parseFloat(getComputedStyle(body).getPropertyValue('--f14')) || 14;
      const f12 = parseFloat(getComputedStyle(body).getPropertyValue('--f12')) || 12;
      const longest = Math.max(5, ...left.map(e => first(node(e.src)).length));
      const padL = Math.ceil(longest * f14 * 0.62) + 14;
      const top = f12 + 14, bot = f12 + 10;
      // the customer sits on top with extra space below, so their line and tag never cross the victims' rows
      const hasT = !!(left[0] && left[0].kind === 'target');
      const slots = left.length - 1 + (hasT ? 0.8 : 0);
      const step = slots > 0 ? (H - top - bot) / slots : 0;
      const yOf = i => top + (i + (hasT && i > 0 ? 0.8 : 0)) * step;
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
      const roomy = step >= f12 * 2.4; // enough height for an amount on every victim row
      const nf = Math.max(9, Math.min(f14, step * 0.78)); // victim names shrink with the row spacing so they never touch
      const wide = W >= 720;           // enough width for dates next to amounts
      const amtW = e => (wide ? amt(e) : fmtMoney(+e.amount || 0));

      // victims and the customer -> mule (lines first, nodes on top)
      left.forEach((e, i) => {
        const y = yOf(i), r = rOf(e.amount);
        const end = [xM - rM - 2, yM + (y - yM) * 0.18];
        const p = [[xL + r, y], [xL + (end[0] - xL) * 0.55, y], [end[0] - (end[0] - xL) * 0.3, end[1]], end];
        if (e.kind === 'target') {
          const label = e.held ? `✂ STOPPED ${fmtMoney(e.amount)}` : `${fmtMoney(e.amount)} · PENDING`;
          const at = [xL + r + 12 + (label.length * f12 * 0.62 + 18) / 2, y]; // just right of the customer, on their own row
          if (e.held) {
            out.push(`<path class="mt-held" d="${path(p)}" pathLength="100" stroke-dasharray="18 100" style="stroke-width:3px"/>`,
              `<path class="mt-cut" d="${path(p)}" pathLength="100" stroke-dasharray="0 44 56 0" style="stroke-width:2px"/>`,
              tag(at[0], at[1], label, 'held'));
          } else {
            out.push(`<path class="mt-pending" d="${path(p)}" style="stroke-width:2.5px"/>`, tag(at[0], at[1], label, 'pending'));
          }
        } else {
          // label on the outside of the curve: above for rows that bend down, below for rows that bend up
          const ly = y > yM ? y + f12 + 5 : y - 6;
          out.push(`<path class="mt-edge" d="${path(p)}" style="stroke-width:${(1.2 + 3.3 * (+e.amount || 0) / maxL).toFixed(1)}px"/>`);
          if (roomy) out.push(`<text class="mt-amt" x="${xL + r + 10}" y="${ly}">${esc(amtW(e))}</text>`);
        }
      });
      // mule -> cash-out, fanned out so each transfer reads on its own
      const maxO = Math.max(1, ...outs.map(e => +e.amount || 0));
      const spread = Math.min(46, H * 0.12);
      outs.forEach((e, i) => {
        const k = outs.length > 1 ? (i - (outs.length - 1) / 2) / ((outs.length - 1) / 2) : 0; // -1 (top) .. 1 (bottom)
        const bend = k * spread * 2;
        // Each transfer meets the cash-out circle at its own point (up to ±34°), aimed at the centre, and stops
        // 6 px outside the circle, so the arrowheads never stack on each other or sit on top of the circle.
        const ang = k * 0.6, R = rC + 6;
        const a = [xM + rM + 2, yM], b = [xC - R * Math.cos(ang), yM + R * Math.sin(ang)];
        const reach = (b[0] - a[0]) * 0.35;
        const p = [a, [a[0] + (b[0] - a[0]) * 0.3, yM + bend], [b[0] - Math.cos(ang) * reach, b[1] + Math.sin(ang) * reach], b];
        const m = bez(p, 0.5);
        out.push(`<path class="mt-cash" d="${path(p)}" marker-end="url(#mt-arrow)" style="stroke-width:${(1.5 + 3 * (+e.amount || 0) / maxO).toFixed(1)}px"/>`,
          `<text class="mt-amt" x="${m[0]}" y="${m[1] + (bend > 0 ? f12 + 4 : -7)}" text-anchor="middle">${esc(amtW(e))}</text>`);
      });
      // nodes + labels
      left.forEach((e, i) => {
        const y = yOf(i), r = rOf(e.amount), n = node(e.src);
        if (e.kind === 'target') {
          out.push(`<circle class="mt-ring" cx="${xL}" cy="${y}" r="${r + 4}"/><circle class="mt-n-maria" cx="${xL}" cy="${y}" r="${r}"/>`,
            `<text class="mt-name mt-maria" x="${xL - r - 9}" y="${y + f14 * 0.36}" text-anchor="end">Customer</text>`);
        } else {
          out.push(`<circle class="mt-n-victim" cx="${xL}" cy="${y}" r="${r}"/>`,
            `<text class="mt-name" x="${xL - r - 9}" y="${y + nf * 0.36}" text-anchor="end" style="font-size:${nf}px">${first(n)}</text>`);
        }
      });
      // under the mule's own labels, where no line runs
      if (ms.flagged) out.push(`<circle class="mt-flag-ring" cx="${xM}" cy="${yM}" r="${rM + 7}"/>`);
      out.push(`<circle class="mt-n-mule" cx="${xM}" cy="${yM}" r="${rM}"/>`,
        `<text class="mt-name" x="${xM}" y="${yM + rM + f14 + 10}" text-anchor="middle">Mule account</text>`,
        ms.flagged ? `<text class="mt-name mt-flagged" x="${xM}" y="${yM + rM + f14 * 2 + 20}" text-anchor="middle">⚑ Flagged</text>` : '',
        `<circle class="mt-n-cash" cx="${xC}" cy="${yM}" r="${rC}"/>`,
        `<text class="mt-name" x="${xC}" y="${yM + rC + f14 + 6}" text-anchor="middle">Cash-out</text>`); // totals live in the tiles above
      svg.setAttribute('viewBox', `0 0 ${W} ${H}`);
      svg.innerHTML = '<defs><marker id="mt-arrow" viewBox="0 0 10 10" refX="8" refY="5" markerUnits="userSpaceOnUse" markerWidth="11" markerHeight="11" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" class="mt-arrowhead"/></marker></defs>' + out.join('');
    },

    risk() {
      const body = bodyOf('risk');
      const c = focusCall();
      const r = c && c.risk;
      if (!r) {
        body.innerHTML = '<div class="risk"><div class="score"><div class="gauge" aria-hidden="true"></div><span class="band">No call</span><span class="num">waiting for the caller to speak</span></div>'
          + '<div class="risk-right"><div class="meter"><i></i></div><div class="meta">Only the caller\'s words are scored, never the customer\'s</div></div></div>';
        return;
      }
      const p = shownPct(r);
      const tone = isHot(r) ? 'hot' : r.s >= 0.4 ? 'warm' : 'cool';
      // P2 holds s at 0.60 after a hard-ask alert (so the customer isn't restored into a scam) while the band stays
      // high/critical: that is a hold, not a measurement, so the score number is replaced by "alert held".
      const held = isHot(r) && r.s < 0.8;
      const meta = [cap(humanize(r.type)), r.stage ? `stage: ${humanize(r.stage)}` : '', r.imp ? `impersonates ${r.imp}` : ''].filter(Boolean).join(' · ');
      const aiInWhy = r.why.some(w => /\bAI\b/.test(w));
      const chips = r.why.map(w => `<span class="chip">${esc(w)}</span>`).join('')
        + (r.ai && !aiInWhy ? '<span class="chip ai">Talking to the AI system</span>' : '');
      const asks = r.asks.length ? `<div class="asks">Asks for ${r.asks.map(a => `<b>${esc(ASK[a] || humanize(a))}</b>`).join(' · ')}</div>` : '';
      // --p drives the half-gauge in the analytics look (look-analytics.css); the default look ignores it
      body.innerHTML = `<div class="risk ${tone}" style="--p:${r.prevPct}">`
        + `<div class="score"><div class="gauge" aria-hidden="true"></div><span class="band">${tone === 'hot' ? '⚠ ' : ''}${esc(bandWord(r))}</span><span class="num">${held ? 'alert held for this call' : `detector score ${r.s.toFixed(2)}`}</span></div>`
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
      $('feed-meta').textContent = [`${fmtPhone(c.from) || 'unknown'} → customer`, route, c.attestation ? attestWords(c.attestation) : ''].filter(Boolean).join(' · ');
      if (!c.feed.length) { body.innerHTML = empty('Ringing. Only the caller\'s side will appear here.'); return; }
      body.innerHTML = `<div class="feed">${c.feed.map(l => lineHtml(l)).join('')}</div>`;
      body.scrollTop = body.scrollHeight;
    },

    attest() {
      const body = bodyOf('attest');
      if (!body) return; // privacy strip is off the screen
      const local = S.engine === 'local';
      const v = voiceState();
      // Always-visible privacy strip: short labels, the detail is in the tooltip
      const rows = [
        ['Caller audio only', "The customer's voice is never processed"],
        ['No audio kept', 'Caller audio is transcribed by NVIDIA-hosted speech-to-text and not saved; short text snippets stay in a local log'],
        local ? ['Local model', 'Nemotron Nano 4B on our server (laptop GPU); NVIDIA-hosted Nemotron is the fallback'] : ['Cloud model', 'NVIDIA-hosted Nemotron'],
        v === 'clone' ? ['Consented voice', `The customer's clone, consent ${S.voice && S.voice.consent ? S.voice.consent : 'on file'}, deletable`]
          : v === 'synthetic' ? ['Synthetic voice', 'No voice clone kept'] : null,
        ['Synthetic data', 'No real customer data anywhere in this demo'],
      ].filter(Boolean);
      body.innerHTML = rows.map(([k, t]) => `<span class="item" title="${esc(t)}"><span class="ok">✓</span><b>${esc(k)}</b></span>`).join('');
    },

    // The ending, one beat per line, ticked off as it happens: payout captured -> customer's Zelle stopped ->
    // the account is a mule -> one click flags it for every customer -> his number can't get through.
    payoff() {
      const body = bodyOf('payoff');
      if (!body) return;
      const m = moneyState();
      const d = CHAIN.data;
      const amt = Number.isFinite(m.amount) ? fmtMoney(m.amount) : 'the';
      const victims = d ? d.edges.filter(e => e.kind === 'victim') : [];
      const inT = d ? Number(d.mule_total_in) || victims.reduce((s, e) => s + (+e.amount || 0), 0) : 0;
      const outT = d ? Number(d.mule_total_out) || 0 : 0;
      const row = (state, title, sub, extra) => `<li class="po ${state}"><span class="po-dot" aria-hidden="true">${state === 'done' ? '✓' : ''}</span>`
        + `<div class="po-txt"><b>${title}</b>${sub ? `<span>${sub}</span>` : ''}${extra || ''}</div></li>`;
      const rows = [];
      rows.push(m.handle ? row('done', 'Got his payout account', esc(handleText(m.handle)))
        : row('now', 'Getting his payout account', 'The decoy keeps asking where to send the money'));
      if (m.stopped) rows.push(row('done', `Stopped ${amt} before it left the customer's account`, 'Pending Zelle cancelled · the customer can undo'));
      else if (m.hold && m.hold.undone) rows.push(row('done', 'The customer released the transfer', 'Their choice, from their app'));
      else if (m.hold && m.hold.status === 'skipped') rows.push(row('wait', 'Bank sandbox not reachable', 'Nothing changed in the bank'));
      else rows.push(row(m.handle ? 'now' : 'wait', "Stop the customer's pending Zelle", 'The transfer he asked for, to that account'));
      rows.push(d && (m.stopped || m.handle)
        ? row('done', `That account took ${fmtMoney(inT)} from ${victims.length} other people`, `${fmtMoney(outT)} already moved to a cash-out account`)
        : row('wait', 'Check who else paid that account', ''));
      if (m.flagged) rows.push(row('done', 'Flagged for every customer', 'Anyone who tries to pay it is warned first (simulated)'));
      else if (m.flag && m.flag.status === 'queued') {
        const busy = m.flag.ui === 'approving';
        rows.push(row('now', 'Flag it for every customer?', 'One analyst click',
          `<button class="po-btn" data-approve="${esc(m.flag.id)}"${busy ? ' disabled' : ''}>${busy ? 'Flagging…' : 'Approve · flag this account'}</button>`));
      } else rows.push(row('wait', 'Flag it for every customer', 'Waits for one analyst click'));
      if (m.rejected) rows.push(row('done', 'He called back: rejected before it rang', esc(fmtPhone(S.rejects[S.rejects.length - 1].number))));
      else if (m.block) rows.push(row('done', "His number can't reach the customer again", esc(fmtPhone(m.block.target))));
      else rows.push(row('wait', 'Block his number', ''));
      const note = m.flag && m.flag.note ? `<div class="po-note">${esc(m.flag.note)}</div>` : '';
      const html = `<ol class="payoff">${rows.join('')}</ol>${note}`;
      if (body.dataset.html !== html) { body.innerHTML = html; body.dataset.html = html; } // never swap the button mid-click
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
  // Two chapters only: the live call, then the money ending (map + the payoff checklist with the one Approve click).
  const STEP_CHAPTER = { detect: 'call', handoff: 'call', verify: 'money', burn: 'money', immune: 'money' };
  const CHAPTER_NAME = { call: 'the call', money: 'the money trail' };
  const LAYOUTS = {
    'story:call': { cols: [1.6, 1], stacks: [[['p-feed', 1]], [['p-risk', 1]]] },
    'story:money': { cols: [1.7, 1], stacks: [[['p-map', 1]], [['p-payoff', 1]]] },
  };
  // Money trail: P4a's read-only GET /intel/chain (Capital One Nessie sandbox, synthetic), drawn here in the screen's own style.
  // Polled every 3 s only while the view is open. Kept outside S, so "Clear for next judge" doesn't blank it.
  const CHAIN = { data: null, live: false, at: 0, timer: 0, busy: false };
  async function pollChain() {
    if (CHAIN.busy || VIEW.shown !== 'money') return;
    CHAIN.busy = true;
    try {
      const r = await fetch(`${MODE.base || CFG.server || TEAM_HUB}/intel/chain`, { cache: 'no-store' });
      if (!r.ok) throw new Error(`HTTP ${r.status}`);
      const d = await r.json();
      if (!d || !Array.isArray(d.nodes) || !Array.isArray(d.edges)) throw new Error('unexpected /intel/chain shape');
      Object.assign(CHAIN, { data: d, live: true, at: Date.now() });
      dirty('payoff');
    } catch (err) {
      // hub not reachable (offline replay): the saved snapshot in fixture.js, labelled as a snapshot; live data that stops is labelled stale
      if (!CHAIN.at && window.BACKFIRE_CHAIN) CHAIN.data = window.BACKFIRE_CHAIN;
      CHAIN.live = false;
    } finally {
      CHAIN.busy = false;
      dirty('map', 'payoff');
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
  const ORDER = { call: 0, money: 1 };
  const DWELL_MS = 8000; // each chapter stays up long enough to point at before the story moves on
  let dwellTimer = 0;
  function chapterNow() {
    if (VIEW.pinned) return VIEW.pinned;
    const st = S.stage;
    return st.burn || st.immune || st.verify || st.extract ? 'money' : 'call';
  }
  function layout() {
    let chapter = chapterNow();
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
    applyBrand(chapter);
    document.querySelectorAll('.views [data-view]').forEach(b => b.setAttribute('aria-selected', String(b.dataset.view === chapter)));
    const follow = $('follow');
    follow.hidden = !VIEW.pinned;
    if (!follow.hidden) { follow.textContent = 'Holding · back to live'; follow.title = `Holding ${CHAPTER_NAME[VIEW.pinned]} on screen. Click (or Esc) to follow the call again.`; }
    const key = `story:${chapter}`;
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
    if (chapter === 'money') ensureMap();
    grid.classList.remove('enter'); void grid.offsetWidth; grid.classList.add('enter');
    dirty('feed', 'trace', 'hero'); // moved panels lose their scroll position; re-render scrolls them to the newest line
  }
  // One brand at a time, never mixed: the Money trail is the Capital One part of the demo, so it switches the whole
  // screen (lockup, title, navy accent) to Capital One; the live call stays T-Mobile. ?brand=capitalone keeps
  // Capital One on for the whole run (Nessie judges).
  const BRAND_URL = /[?&]brand=(capitalone|c1)(&|$)/i.test(location.search);
  function applyBrand(chapter) {
    const c1 = BRAND_URL || chapter === 'money';
    document.documentElement.classList.toggle('brand-c1', c1);
    $('brand-title').textContent = c1 ? 'Fraud desk' : 'Command center';
    document.title = c1 ? 'Backfire × Capital One' : 'Backfire Command Center';
  }
  // A tab holds that chapter on screen; the live tab (or Esc, or "back to live") follows the call again.
  function setView(name) {
    VIEW.name = 'story';
    VIEW.pinned = name === 'money' ? 'money' : name === 'call' && chapterNow() !== 'call' ? 'call' : null;
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
    const view = { 1: 'call', 2: 'money' }[ev.key];
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
    setView((qs.get('view') || '').toLowerCase());
    renderAll();
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
