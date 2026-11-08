(() => {
  "use strict";
  const $ = id => document.getElementById(id);
  const qs = new URLSearchParams(location.search);
  // ?server=<hub base URL> (http://host:8000, or ws://host:8000/events) -> live; absent -> replay of mock/events.json
  // Served by the hub at /app -> live against that hub by default (same-origin); elsewhere -> mock replay.
  const SERVER_RAW = qs.get("server") || (location.pathname.startsWith("/app") ? location.origin : null);
  // Security: the hub URL comes from the query string, and voice recordings go to it, so only trust same-origin or localhost hubs.
  function trustedHub(raw) {
    try {
      const u = new URL(raw.replace(/\/events\/?$/, "").replace(/^ws/, "http"));
      const ok = u.origin === location.origin || ["localhost", "127.0.0.1"].includes(u.hostname);
      return ok ? u.origin + u.pathname.replace(/\/$/, "") : null;
    } catch (e) { return null; }
  }
  const HUB = SERVER_RAW ? trustedHub(SERVER_RAW) : null;
  if (SERVER_RAW && !HUB) console.warn("[backfire] ignoring untrusted ?server= (must be same-origin or localhost)");
  const SERVER = HUB ? HUB.replace(/^http/, "ws") + "/events" : null;
  const MOCK_URL = qs.get("mock") || "../../mock/events.json";
  const MOCK_CALL = qs.get("call") || "irs";   // substring of the mock call_id: irs | bank | crypto
  const DEBUG = qs.has("debug");
  window.BF = window.BF || {}; BF.hub = HUB; BF.onEventRef = null;
  // footer tells the truth about the mode: demo replay / recorded replay / simulated call / live call (Telnyx)
  BF.footer = () => { const f = document.getElementById("src"); if (f) f.parentNode.hidden = !qs.has("debug"); if (f) f.textContent = !HUB ? "Demo replay" : BF.replay ? "Replay · recorded demo" : BF.sim ? "Simulated call" : "Live call · Telnyx"; };
  // Phone-free sim mode (?sim=1 or hub flag SIM_MODE): no Telnyx login, the page rings/answers from hub events and plays the caller audio itself (sim.js). Fails soft to false.
  BF.modeP = qs.has("sim") ? Promise.resolve({ sim: true }) : qs.has("talk") ? Promise.resolve({ listen: true, talk: true }) : qs.has("listen") ? Promise.resolve({ listen: true }) : HUB ? fetch(HUB + "/demo/status?format=json").then(r => r.json()).then(j => { const f = (j && j.flags) || {}; if (typeof f.CUSTOMER_NAME === "string") { try { document.title = f.CUSTOMER_NAME ? "Backfire \u00b7 " + f.CUSTOMER_NAME : "Backfire"; } catch (e) {} } return { sim: !!f.SIM_MODE, listen: f.MARIA_LEG === "listen" || f.MARIA_LEG === "talk", talk: f.MARIA_LEG === "talk" }; }).catch(() => ({})) : Promise.resolve({});
  BF.simP = BF.modeP.then(m => !!(m.sim || m.listen));   // true = no Telnyx login (phone-free sim, or listening mode where Maria's leg is not a SIP client)
  BF.modeP.then(m => { BF.listen = !!m.listen; BF.talk = !!m.talk; BF.sim = !!m.sim && !m.listen; BF.footer(); });
  // Device pairing (TASK-014): the hub issues a per-device token after the PIN is entered once. Every hub call goes through hubFetch.
  BF.deviceToken = () => { try { return localStorage.getItem("bf.device"); } catch (e) { return null; } };
  BF.authReady = Promise.resolve();   // pair.js replaces this on a fresh phone: protected routes wait until the device is paired (no 401 noise before pairing)
  BF.hubFetch = async (path, opts) => {
    opts = opts || {}; if (!opts.noWait) await BF.authReady; const h = { ...(opts.headers || {}) }; const t = BF.deviceToken(); if (t) h["x-device-token"] = t;
    const r = await fetch(HUB + path, { ...opts, headers: h });
    if (r.status === 401 && BF.onUnauthorized) BF.onUnauthorized();
    return r;
  };
  window.__userActions = [];                  // test hook: every user.action emitted

  const st = { callId: null, answered: false, alerted: false, ctx: null, timer: null, t0: 0, replay: [], tos: [], badge: "watching" };

  const log = (...a) => { console.log("[backfire]", ...a); if (DEBUG) { const l = $("log"); l.hidden = false; l.textContent += a.map(x => typeof x === "string" ? x : JSON.stringify(x)).join(" ") + "\n"; } };
  const show = id => { for (const s of ["incoming", "active", "ended"]) $(s).hidden = s !== id; };

  // ---- audio: unlock on a user tap (mobile autoplay), then beeps are local-only ----
  BF.soundBadge = on => { const sb = $("soundBanner"); if (sb) sb.hidden = !!on; const b = $("sound"); if (!b) return; b.classList.toggle("off", !on); b.setAttribute("aria-label", on ? "Sound on" : "Sound off. Tap to turn sound on"); b.title = on ? "Sound on" : "Tap for sound"; };   // icon-only chip (CSS draws the speaker / muted speaker)
  function unlockAudio() {
    try { st.ctx = st.ctx || new (window.AudioContext || window.webkitAudioContext)(); if (st.ctx.state === "suspended") st.ctx.resume(); } catch (e) { log("audio unavailable", String(e)); }
    const on = !!st.ctx && st.ctx.state !== "closed"; BF.soundBadge(on);
  }
  // Ringtone as an <audio> element (P1 08:12, "incoming call is silent"): Web Audio is muted by the iPhone ring/silent
  // switch and gets suspended when the page is backgrounded; a media element primed by a tap keeps playing.
  const ringEl = (() => { try {
    const sr = 8000, n = sr * 3, b = new ArrayBuffer(44 + n * 2), v = new DataView(b), w = (o, s) => [...s].forEach((c, i) => v.setUint8(o + i, c.charCodeAt(0)));
    w(0, "RIFF"); v.setUint32(4, 36 + n * 2, true); w(8, "WAVEfmt "); v.setUint32(16, 16, true); v.setUint16(20, 1, true); v.setUint16(22, 1, true);
    v.setUint32(24, sr, true); v.setUint32(28, sr * 2, true); v.setUint16(32, 2, true); v.setUint16(34, 16, true); w(36, "data"); v.setUint32(40, n * 2, true);
    for (let i = 0; i < n; i++) { const t = i / sr, on = t < 2 && (t % 1) < 0.9;   // US ring: 440+480 Hz, 2 s on, 1 s off
      v.setInt16(44 + i * 2, on ? Math.round(6000 * (Math.sin(2 * Math.PI * 440 * t) + Math.sin(2 * Math.PI * 480 * t))) : 0, true); }
    const a = new Audio(URL.createObjectURL(new Blob([b], { type: "audio/wav" }))); a.loop = true; a.preload = "auto"; return a;
  } catch (e) { return null; } })();
  let ringPrimed = false;
  function primeRing() { if (!ringEl || ringPrimed) return; ringEl.muted = true;
    const p = ringEl.play(); if (p && p.then) p.then(() => { ringEl.pause(); ringEl.currentTime = 0; ringEl.muted = false; ringPrimed = true; }).catch(() => { ringEl.muted = false; }); }
  BF.ringEl = ringEl;
  document.addEventListener("pointerdown", () => { unlockAudio(); primeRing(); });   // every tap (not once): iOS suspends audio after backgrounding
  document.addEventListener("visibilitychange", () => { if (!document.hidden && st.ctx && st.ctx.state !== "running") st.ctx.resume().catch(() => {}); });
  $("sound").addEventListener("click", unlockAudio); $("soundBanner").addEventListener("click", () => { unlockAudio(); primeRing(); });   // full-width "Tap to turn on call sounds" until the first tap (UI review 2) BF.unlockAudio = () => { unlockAudio(); primeRing(); };   // first tap anywhere unlocks beeps

  // ---- Live Guard badge: watching / alert / handed off / off ----
  const fmtNum = n => /^\+1\d{10}$/.test(n || "") ? `+1 (${n.slice(2, 5)}) ${n.slice(5, 8)}-${n.slice(8)}` : (n || "");
  const BADGES = { watching: "Live Guard on", alert: "Scam Likely", handed: "Handled for you", off: "Live Guard off" };
  function setBadge(k) { if (k) st.badge = k; const key = BF.guardOn === false ? "off" : st.badge; const b = $("guard"); b.textContent = BADGES[key]; b.className = "badge guard " + key; }
  BF.renderBadge = () => setBadge();
  function beep(at, dur) {
    const c = st.ctx; if (!c) return;
    const o = c.createOscillator(), g = c.createGain();
    o.frequency.value = 880; o.connect(g); g.connect(c.destination);
    const t = c.currentTime + at;
    g.gain.setValueAtTime(0.0001, t); g.gain.exponentialRampToValueAtTime(0.4, t + 0.02); g.gain.exponentialRampToValueAtTime(0.0001, t + dur);
    o.start(t); o.stop(t + dur + 0.02);
  }
  const twoBeeps = () => { beep(0, 0.18); beep(0.3, 0.18); if (navigator.vibrate) navigator.vibrate([150, 100, 150]); };

  // ---- phone feel: ringtone (WebAudio, needs the tap-unlocked context), vibrate, 45 s no-answer, screen wake lock ----
  const RING_TIMEOUT_MS = 45000; let ringI = null, ringTO = null, wake = null;
  function ringBurst() { const c = st.ctx; if (c && c.state === "running") for (const [at, f] of [[0, 440], [0.45, 480], [0.9, 440], [1.35, 480]]) { const o = c.createOscillator(), g = c.createGain(); o.type = "sine"; o.frequency.value = f; o.connect(g); g.connect(c.destination); const t = c.currentTime + at; g.gain.setValueAtTime(0.0001, t); g.gain.exponentialRampToValueAtTime(0.25, t + 0.03); g.gain.exponentialRampToValueAtTime(0.0001, t + 0.38); o.start(t); o.stop(t + 0.42); } if (navigator.vibrate) navigator.vibrate([700, 300, 700, 300]); }
  function startRing() { stopRing();
    let viaEl = false; if (ringEl) { try { ringEl.currentTime = 0; const p = ringEl.play(); viaEl = true; if (p && p.catch) p.catch(() => { viaEl = false; ringBurst(); ringI = ringI || setInterval(ringBurst, 3000); }); } catch (e) { viaEl = false; } }
    if (!viaEl) { if (st.ctx && st.ctx.state !== "running") st.ctx.resume().catch(() => {}); ringBurst(); ringI = setInterval(ringBurst, 3000); }
    else if (navigator.vibrate) { navigator.vibrate([700, 300, 700, 300]); ringI = setInterval(() => navigator.vibrate && navigator.vibrate([700, 300, 700, 300]), 3000); } ringTO = setTimeout(() => { if ($("phone").dataset.state === "ringing") { emitUserAction("decline"); if (BF.voip) BF.voip.hangup(); endCall("Missed call."); } }, RING_TIMEOUT_MS); }
  function stopRing() { clearInterval(ringI); clearTimeout(ringTO); ringI = ringTO = null; if (ringEl) { try { ringEl.pause(); ringEl.currentTime = 0; } catch (e) {} } if (navigator.vibrate) navigator.vibrate(0); }
  async function lockScreen() { try { if (navigator.wakeLock && !wake && document.visibilityState === "visible") { wake = await navigator.wakeLock.request("screen"); wake.addEventListener("release", () => { wake = null; }); } } catch (e) { wake = null; } }
  function unlockScreen() { try { wake && wake.release(); } catch (e) {} wake = null; }
  let hiddenAt = 0;
  document.addEventListener("visibilitychange", () => {
    const inCall = $("phone").dataset.state === "active";
    if (document.visibilityState === "visible") { if (inCall) { lockScreen(); if (hiddenAt && Date.now() - hiddenAt > 2000) { const k = $("keepOpen"); if (k) { k.hidden = false; k.textContent = "You left Backfire for a moment. Keep it open during calls so the call audio keeps playing."; } } } hiddenAt = 0; }
    else if (inCall) hiddenAt = Date.now();
  });
  const IOS = /iP(hone|ad|od)/.test(navigator.userAgent) || (navigator.platform === "MacIntel" && navigator.maxTouchPoints > 1);

  // ---- the ONE place user actions leave the app. Adapt here when interfaces.md lands. ----
  let ws = null;
  function emitUserAction(action) {
    const msg = { type: "user.action", call_id: st.callId, ts: new Date().toISOString(), data: { action } };
    window.__userActions.push(msg);
    log("user.action", msg);
    if (HUB) BF.hubFetch("/user/action", { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify({ call_id: st.callId, action }) })
      .catch(e => log("POST /user/action failed (fail open, screen keeps working)", String(e)));
    return msg;
  }

  // ---- rendering ----
  function tick() { const s = Math.floor((Date.now() - st.t0) / 1000); $("timer").textContent = String(Math.floor(s / 60)).padStart(2, "0") + ":" + String(s % 60).padStart(2, "0"); }
  const ACR = s => String(s).replace(/\b(Irs|Ssa|Fbi|Dea|Ftc|Usps|Cdc|Dhs)\b/g, m => m.toUpperCase());   // server title-cases impersonated agencies
  function renderChips(chips) { const ul = $("chips"); ul.replaceChildren(...(chips || []).map(c => { const li = document.createElement("li"); li.textContent = ACR(c); return li; })); }
  function endCall(msg) {
    $("active").dataset.handoff = ""; $("handoffMsg").hidden = true; $("alertBox").hidden = true; BF.resumed = false; clearTimeout(st.handT); stopRing(); unlockScreen(); { const k = $("keepOpen"); if (k) k.hidden = true; }
    { const n = $("actedMsg"); if (n) n.hidden = true; }
    clearInterval(st.timer); st.answered = false; setBadge("watching"); renderSummary(msg); show("ended"); { const missed = /^Missed/.test(msg || ""); $("endedTitle").textContent = missed ? "Missed call" : "Call ended"; $("endedMsg").textContent = missed ? "You did not answer. Backfire is still watching your calls." : (msg || ""); }
    $("phone").dataset.state = "ended";
  }

  function onEvent(ev) {
    if (!ev || !ev.type) return;
    // F1: while a call is ringing or in progress, EVERYTHING about another call (incl. its call.incoming) is ignored, by this file and by sim.js/talk.js (they hang off BF.onEvent)
    if (st.callId && ev.call_id && ev.call_id !== st.callId && ["ringing", "active"].includes($("phone").dataset.state)) { log("ignored event for another call while busy", ev.type); return; }
    if (window.BF && BF.onEvent) BF.onEvent(ev);
    if (st.callId && ev.call_id && ev.call_id !== st.callId && ev.type !== "call.incoming") return;
    const d = ev.data || {};
    switch (ev.type) {
      case "call.incoming":
        st.callId = ev.call_id; st.blockedNow = false; clearTimeout(st.sumT); st.alerted = false; st.risk = 0; st.chips = []; st.handed = false; st.haul = 0; st.lastFrom = String(d.from || "").replace(/\D/g, "").slice(-10);
        $("active").dataset.handoff = ""; $("handoffMsg").hidden = true; $("alertBox").hidden = true; $("idleMsg").hidden = false; setBadge("watching");   // a new call never starts on the previous call's handoff/alert screen
        $("callerNumber").textContent = fmtNum(d.from);
        $("scamLabel").hidden = !(d.scam_id_score >= 0.5);
        $("attest").textContent = d.attestation === "A" ? "Caller ID verified" : "Caller ID not verified";
        // Hold the ring until call.routed: a blocked call must never ring Maria's phone. Live source only; 1s fallback if routed never comes.
        if (SERVER) { clearTimeout(st.ringT); st.ringT = setTimeout(ring, 1000); } else ring(); break;
      case "call.routed":
        if (d.decision === "BLOCKED_BACKFIRE") { clearTimeout(st.ringT); st.callId = null; break; }
        $("guard").hidden = d.decision !== "LIVE_GUARD"; setBadge("watching"); clearTimeout(st.ringT); ring(); break;
      case "call.answered": break; // UI answers on tap
      case "call.ended": if (st.callId === ev.call_id) endCall(d.ended_by === "caller" ? "The caller hung up." : "Call ended."); break;
      case "alert.fired":
        if (d.level === "first" && st.alerted) break;      // re-alert only on level: realert
        st.alerted = true; setBadge("alert"); renderChips(d.why_chips);
        { const tg = $("alertTag"), n = (d.why_chips || []).length, s = Math.max(+d.s || 0, st.risk || 0), tier = s >= 0.85 ? "High risk" : s >= 0.6 ? "Elevated risk" : n >= 2 ? "High risk" : "Possible risk";
          if (tg) { tg.textContent = tier + (n ? " \u00b7 " + n + " signal" + (n > 1 ? "s" : "") : ""); tg.hidden = false; } st.chips = [...new Set([...(st.chips || []), ...(d.why_chips || []).map(ACR)])]; }   // red flags accumulate across alerts (UI review 3, B)
        { const sub = document.querySelector("#btnGets .b-sub"); if (sub) sub.textContent = "Backfire talks to them in " + BF.voiceWord(); }
        $("alertBox").hidden = false; $("idleMsg").hidden = true; $("handoffMsg").hidden = true; $("active").dataset.handoff = "";
        twoBeeps(); break;
      case "user.action": {                               // first tap wins on the hub; show an action taken on ANOTHER phone
        const mine = (window.__userActions || []).some(m => m.call_id === ev.call_id && m.data && m.data.action === d.action && Date.now() - Date.parse(m.ts) < 4000);
        const who = d.by || d.device || d.client || "another phone", n = $("actedMsg");
        if (!mine && n && d.action) { n.textContent = ({ continue: "Continue", scammer_get_scammed: "Fire Back", hang_up: "Hang up" }[d.action] || d.action) + " was chosen on " + (/^another/.test(who) ? who : "the " + who) + "."; n.hidden = false; }
        break; }
      case "handoff.started": clearTimeout(st.handT); st.handed = true; showHandoff(); break;
      case "risk.update": st.risk = Math.max(st.risk || 0, +d.s || 0); break;
      case "artifacts.extracted": st.haul = (d.artifacts || d.items || []).length || +d.n_artifacts || st.haul || 0; break;
      case "blocklist.updated": if (st.lastFrom && String(d.number || "").replace(/\D/g, "").slice(-10) === st.lastFrom) { st.blockedNow = true; clearTimeout(st.sumT); const b = $("sumBlocked"); if (b) { b.textContent = "Blocked for you"; b.className = "ok"; b.parentNode.hidden = false; } } break;
      case "handoff.failed": failHandoff(d.reason); break;   // F3: the hub could not hand the call to Backfire: she is still on the call
      case "handoff.restored": st.alerted = false; clearTimeout(st.handT); twoBeeps(); setBadge("watching");   // F5: a later alert must fire again; F20: she hears/feels that she is back on the call
        $("alertBox").hidden = true; $("idleMsg").hidden = true; setHandoffUI("restored"); break;
      default: break;
    }
  }
  // Call-ended summary (UI review: the ended screen wasted the payoff). Filled from what this page saw during the call.
  // "Number" row: only a real blocklist.updated for this number says "Blocked for you"; otherwise it resolves after ~5 s (UI review 2, bug 1) instead of "Checking…" forever.
  const SUM_WAIT_MS = 5000;
  BF.voiceWord = () => (BF.hasVoice && BF.hasVoice()) ? "your voice" : "a synthetic voice";
  function renderSummary(msg) {
    const box = $("summary"); if (!box) return;
    clearTimeout(st.sumT);
    const secs = st.t0 && st.answered !== undefined ? Math.max(0, Math.floor((Date.now() - st.t0) / 1000)) : 0;
    const rows = [];
    if (st.callId && !/^Missed|declined/.test(msg || "")) rows.push(["Duration", String(Math.floor(secs / 60)).padStart(2, "0") + ":" + String(secs % 60).padStart(2, "0"), ""]);
    if ($("callerNumber").textContent) rows.push(["Caller", $("callerNumber").textContent, ""]);
    if (st.alerted || (st.chips || []).length) rows.push(["Red flags", (st.chips || []).length ? st.chips : ["Scam signs detected"], "warn flags"]);
    if (st.handed) rows.push(["Backfire", "Took the call in " + BF.voiceWord() + (st.haul ? " \u00b7 saved " + st.haul + " detail" + (st.haul > 1 ? "s" : "") + " about the scammer" : ""), "ok"]);
    if (st.handed || st.alerted) rows.push(st.blockedNow ? ["Number", "Blocked for you", "ok", "sumBlocked"] : ["Number", "Checking\u2026", "", "sumBlocked"]);
    box.replaceChildren(...rows.map(([k, v, cls, id]) => { const li = document.createElement("li"); const a = document.createElement("span"); a.textContent = k; const b = document.createElement("b");
      if (Array.isArray(v)) v.forEach(x => { const l = document.createElement("span"); l.textContent = x; b.append(l); }); else b.textContent = v;
      if (cls) b.className = cls; if (id) b.id = id; li.append(a, b); return li; }));
    box.hidden = !rows.length;
    const handed = st.handed;
    if (!st.blockedNow && $("sumBlocked")) st.sumT = setTimeout(() => { const b = $("sumBlocked"); if (!b || b.className === "ok") return;
      if (handed) b.textContent = "Sent to Backfire"; else b.parentNode.hidden = true; }, SUM_WAIT_MS);   // no block for this number (Continue, not a scam, or the event never came)
  }
  function ring() { if (st.callId && !st.answered && $("phone").dataset.state !== "ringing") { $("phone").dataset.state = "ringing"; show("incoming"); startRing(); } }
  // Handoff screen states (F3): pending -> done ("Backfire has the call") | failed (still on the call). data-view picks the layout.
  const HANDOFF = {
    pending: ["Handing off…", "Backfire is taking the call. Stay on the line for a moment.", "Don't hang up yet.", ""],
    done: ["Backfire has the call", "It's talking to the caller in your voice and saving what they reveal.", "You can put the phone down.", "We'll tell you when it's over."],
    failed: ["", "", "Couldn't hand off. You're still on the call.", ""],
    restored: ["", "", "You're back on the call.", "Backfire stepped aside."]
  };
  function setHandoffUI(kind) {
    const h = HANDOFF[kind]; $("active").dataset.handoff = kind;
    $("handoffTitle").textContent = h[0]; $("handoffLead").textContent = h[1].replace("your voice", BF.voiceWord()); $("handoffMain").textContent = h[2]; $("handoffSub").textContent = h[3]; $("handoffSub").hidden = !h[3];
    $("handoffMsg").hidden = false; syncView();
  }
  function syncView() { const act = $("active"), k = act.dataset.handoff; act.dataset.view = !$("alertBox").hidden ? "alert" : (!$("handoffMsg").hidden && (k === "pending" || k === "done")) ? "handoff" : "call"; }
  new MutationObserver(syncView).observe($("alertBox"), { attributes: true, attributeFilter: ["hidden"] });
  new MutationObserver(syncView).observe($("handoffMsg"), { attributes: true, attributeFilter: ["hidden"] });
  function pendingHandoff() { clearTimeout(st.handT); $("alertBox").hidden = true; $("idleMsg").hidden = true; setHandoffUI("pending"); st.handT = setTimeout(() => failHandoff(), 8000); }
  function failHandoff() { clearTimeout(st.handT); if ($("phone").dataset.state !== "active") return; setBadge("alert"); $("alertBox").hidden = false; $("idleMsg").hidden = true; setHandoffUI("failed"); }
  function showHandoff() { setBadge("handed"); $("alertBox").hidden = true; $("idleMsg").hidden = true; setHandoffUI("done"); }

  // ---- buttons ----
  // UI review 3 (D): a double tap must not send two actions. Short lock, not a permanent disable (a failed handoff re-shows Fire Back).
  const tapLock = {}; function once(id) { const now = Date.now(); if (tapLock[id] && now - tapLock[id] < 1500) return false; tapLock[id] = now; return true; }
  $("answerBtn").onclick = () => { if (!once("answerBtn")) return;
    stopRing(); lockScreen(); emitUserAction("answer");   // the iOS keep-open tip is a one-time line on Home now, not on the call screen
    unlockAudio();                                   // tap unlocks audio so the alert beeps can play
    if (BF.voip) BF.voip.answer();                   // real WebRTC call, if one is ringing
    st.answered = true; st.t0 = Date.now(); st.timer = setInterval(tick, 500); tick();
    $("activeName").textContent = $("callerNumber").textContent || "Unknown caller";
    $("phone").dataset.state = "active"; show("active");
    if (!SERVER) scheduleAfterAnswer();
  };
  $("declineBtn").onclick = () => { if (!once("declineBtn")) return; stopRing(); emitUserAction("decline"); if (BF.voip) BF.voip.hangup(); endCall("You declined the call."); };
  $("endBtn").onclick = () => { if (!once("endBtn")) return; emitUserAction("hang_up"); if (BF.voip) BF.voip.hangup(); stopReplay(); endCall("You ended the call."); };
  $("btnContinue").onclick = () => { if (!once("btnContinue")) return; emitUserAction("continue"); setBadge("watching"); $("alertBox").hidden = true; $("idleMsg").hidden = false; };
  $("btnGets").onclick = () => { if (!once("btnGets")) return; emitUserAction("scammer_get_scammed"); if (SERVER) pendingHandoff(); else showHandoff(); };
  $("btnHang").onclick = () => { if (!once("btnHang")) return; emitUserAction("hang_up"); if (BF.voip) BF.voip.hangup(); stopReplay(); endCall("You hung up."); };
  $("replayBtn").onclick = start;

  // ---- sources ----
  function stopReplay() { st.tos.forEach(clearTimeout); st.tos = []; }
  // The UI itself produces user.action / handoff.started / call.answered in replay, so those mock events are skipped.
  const SKIP = new Set(["user.action", "handoff.started", "call.answered"]);
  async function startReplay() {
    stopReplay(); st.replay = [];
    try {
      const doc = await (await fetch(MOCK_URL)).json();
      const call = doc.calls.find(c => c.call_id.includes(MOCK_CALL)) || doc.calls[0];
      const evs = call.events.filter(e => e.ts >= 0 && !SKIP.has(e.type));
      const answerAt = ((call.events.find(e => e.type === "call.answered") || {}).ts) || 3;
      evs.filter(e => e.ts <= answerAt).forEach(e => st.tos.push(setTimeout(() => onEvent(e), e.ts * 1000)));
      st.replay = evs.filter(e => e.ts > answerAt).map(e => ({ ...e, delay: Math.max(0, (e.ts - answerAt) * 1000) }));
      BF.footer();
    } catch (e) { log("could not load mock", String(e)); $("endedMsg").textContent = "Could not load mock/events.json"; }
  }
  function scheduleAfterAnswer() { st.replay.forEach(e => st.tos.push(setTimeout(() => onEvent(e), e.delay))); }

  function connectWS() {
    ws = new WebSocket(SERVER);
    ws.onmessage = m => { try { onEvent(JSON.parse(m.data)); } catch (e) { log("bad msg", String(e)); } };
    ws.onclose = () => setTimeout(connectWS, 2000);
    ws.onerror = () => ws.close();
  }


  // F10: rejoin a call that is already in progress (page reloaded or resumed): no ring, no extra 'answer' action; sockets re-subscribe through the normal call.answered path.
  function resumeCall(x) {
    const id = typeof x === "string" ? x : x && x.call_id; if (!id || st.callId || ["ringing", "active"].includes($("phone").dataset.state)) return;
    const info = typeof x === "object" && x ? x : {}; st.callId = id; st.alerted = false; st.answered = true;
    st.t0 = Date.now() - 1000 * (+info.age_s || 0); clearInterval(st.timer); st.timer = setInterval(tick, 500); tick();
    $("callerNumber").textContent = fmtNum(info.from); $("activeName").textContent = fmtNum(info.from) || "Call in progress";
    $("phone").dataset.state = "active"; show("active"); setBadge("watching"); lockScreen();
    BF.resumed = true; const ts = new Date().toISOString(); BF.onEvent && BF.onEvent({ type: "call.answered", call_id: id, ts, data: { by: "resume" } });
    if (info.handoff === true || info.handoff === "started") { BF.onEvent && BF.onEvent({ type: "handoff.started", call_id: id, ts, data: {} }); showHandoff(); }
  }

  function needsSetup() { try { return !localStorage.getItem("bf.done") && !qs.has("skipsetup"); } catch (e) { return false; } }
  function start() {
    setBadge("watching"); $("guard").hidden = false; $("alertBox").hidden = true; $("handoffMsg").hidden = true; $("idleMsg").hidden = false;
    st.callId = null; window.__userActions.length = 0; show("ended"); $("endedMsg").textContent = "Waiting for a call…"; $("replayBtn").hidden = !!SERVER;
    BF.footer();
    if (SERVER) {
      if (!ws) connectWS();
      // F10: a reload / iOS resume in the middle of a call must not lose it: ask the hub for the active call (paired /demo/status: active_call_ids = ["id"] or [{call_id, from, age_s, handoff}], top level or in flags) and re-subscribe /listen + /talk.
      BF.hubFetch("/demo/status?format=json").then(r => r.ok ? r.json() : null).then(j => { const f = (j && j.flags) || {}, det = j && (j.active_calls_detail || f.active_calls_detail), ids = j && (j.active_call_ids || f.active_call_ids);
        if (Array.isArray(det) && det.length) { const c = det.filter(x => x && x.call_id && x.answered !== false).pop(); if (c) resumeCall(c); }   // active_calls_detail: [{call_id, from, age_s, handoff, answered}] (paired only); a call that is still ringing is not resumed
        else if (Array.isArray(ids) && ids.length) resumeCall(ids[ids.length - 1]); }).catch(() => {});
      // Honest footer: a hub in fallback/demo mode is replaying a recorded story, not a live phone line (fail soft: keep "live" if unknown).
      fetch(HUB + "/demo/status?format=json").then(r => r.json()).then(j => { const f = (j && j.flags) || {}; if (f.FALLBACK || f.DEMO_MODE) { BF.replay = true; BF.footer(); } }).catch(() => {});
    }
    else if (needsSetup()) BF.pendingStart = startReplay;      // demo call waits until onboarding is finished
    else startReplay();
  }

  // "Add to Home Screen" hint: first visit, iOS Safari (not yet installed). Dismissed once = never again.
  (function () { try { const standalone = window.matchMedia("(display-mode: standalone)").matches || navigator.standalone; if (standalone || localStorage.getItem("bf.a2hs") === "1") return; const h = $("a2hs"); if (!h) return;
    const android = /Android/.test(navigator.userAgent); if (!IOS && !android) return;
    $("a2hsText").textContent = IOS ? "Add Backfire to your Home Screen: tap Share, then Add to Home Screen." : "Add Backfire to your Home Screen: open the browser menu, then Install app.";
    h.hidden = false; $("a2hsClose").onclick = () => { h.hidden = true; try { localStorage.setItem("bf.a2hs", "1"); } catch (e) {} }; } catch (e) {} })();
  // iOS: one-time "keep Backfire open" tip on Home (UI review 2: not on the call screen)
  (function () { try { const t = $("iosTip"); if (!t || !IOS || localStorage.getItem("bf.iostip") === "1") return; t.hidden = false; $("iosTipOk").onclick = () => { t.hidden = true; try { localStorage.setItem("bf.iostip", "1"); } catch (e) {} }; } catch (e) {} })();
  window.BF.deliver = onEvent; BF.endUI = endCall; BF.ui = () => $("phone").dataset.state;
  start();
})();
