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
  // Phone-free sim mode (?sim=1 or hub flag SIM_MODE): no Telnyx login, the page rings/answers from hub events and plays the caller audio itself (sim.js). Fails soft to false.
  BF.modeP = qs.has("sim") ? Promise.resolve({ sim: true }) : qs.has("talk") ? Promise.resolve({ listen: true, talk: true }) : qs.has("listen") ? Promise.resolve({ listen: true }) : HUB ? fetch(HUB + "/demo/status?format=json").then(r => r.json()).then(j => { const f = (j && j.flags) || {}; if (typeof f.CUSTOMER_NAME === "string") { try { document.title = "Backfire \u00b7 " + (f.CUSTOMER_NAME ? f.CUSTOMER_NAME + "\u2019s phone" : "phone"); } catch (e) {} } return { sim: !!f.SIM_MODE, listen: f.MARIA_LEG === "listen" || f.MARIA_LEG === "talk", talk: f.MARIA_LEG === "talk" }; }).catch(() => ({})) : Promise.resolve({});
  BF.simP = BF.modeP.then(m => !!(m.sim || m.listen));   // true = no Telnyx login (phone-free sim, or listening mode where Maria's leg is not a SIP client)
  BF.modeP.then(m => { BF.listen = !!m.listen; BF.talk = !!m.talk; BF.sim = !!m.sim && !m.listen; const f = document.getElementById("src"); if (f && BF.talk) f.textContent = "· live call · talk mode"; else if (f && BF.listen) f.textContent = "· live call · listening mode"; else if (f && BF.sim) f.textContent = "· simulated call (no phone line)"; });
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
  function unlockAudio() {
    try { st.ctx = st.ctx || new (window.AudioContext || window.webkitAudioContext)(); if (st.ctx.state === "suspended") st.ctx.resume(); } catch (e) { log("audio unavailable", String(e)); }
    const on = !!st.ctx && st.ctx.state !== "closed"; $("sound").textContent = on ? "🔊 Sound on" : "🔇 Sound off"; $("sound").classList.toggle("off", !on);
  }
  document.addEventListener("pointerdown", unlockAudio, { once: true });   // first tap anywhere unlocks beeps

  // ---- Live Guard badge: watching / alert / handed off / off ----
  const BADGES = { watching: "🛡 Live Guard on", alert: "⚠ Possible scam", handed: "✓ Handled for you", off: "Live Guard off" };
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
  function startRing() { stopRing(); ringBurst(); ringI = setInterval(ringBurst, 3000); ringTO = setTimeout(() => { if ($("phone").dataset.state === "ringing") { emitUserAction("decline"); if (BF.voip) BF.voip.hangup(); endCall("Missed call."); } }, RING_TIMEOUT_MS); }
  function stopRing() { clearInterval(ringI); clearTimeout(ringTO); ringI = ringTO = null; if (navigator.vibrate) navigator.vibrate(0); }
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
    clearTimeout(st.handT); stopRing(); unlockScreen(); { const k = $("keepOpen"); if (k) k.hidden = true; }
    { const n = $("actedMsg"); if (n) n.hidden = true; }
    clearInterval(st.timer); st.answered = false; show("ended"); $("endedMsg").textContent = msg || "";
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
        st.callId = ev.call_id; st.alerted = false;
        $("callerNumber").textContent = d.from || "";
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
        { const tg = $("alertTag"); const e = String(d.engine || d.source || "").toLowerCase(); if (tg) { tg.textContent = !e ? "" : /device|local|on-?device/.test(e) ? "Checked on this phone" : "Checked by Backfire's server"; tg.hidden = !tg.textContent; } }
        $("alertBox").hidden = false; $("idleMsg").hidden = true; $("handoffMsg").hidden = true;
        twoBeeps(); break;
      case "user.action": {                               // first tap wins on the hub; show an action taken on ANOTHER phone
        const mine = (window.__userActions || []).some(m => m.call_id === ev.call_id && m.data && m.data.action === d.action && Date.now() - Date.parse(m.ts) < 4000);
        const who = d.by || d.device || d.client || "another phone", n = $("actedMsg");
        if (!mine && n && d.action) { n.textContent = ({ continue: "Continue", scammer_get_scammed: "Scammer Get Scammed", hang_up: "Hang up" }[d.action] || d.action) + " was chosen on " + (/^another/.test(who) ? who : "the " + who) + "."; n.hidden = false; }
        break; }
      case "handoff.started": clearTimeout(st.handT); showHandoff(); break;
      case "handoff.failed": failHandoff(d.reason); break;   // F3: the hub could not hand the call to Backfire: she is still on the call
      case "handoff.restored": setBadge("watching"); $("handoffMsg").textContent = "You're back on the call. Backfire stepped aside."; $("handoffMsg").hidden = false; $("alertBox").hidden = true; $("idleMsg").hidden = true; break;
      default: break;
    }
  }
  function ring() { if (st.callId && !st.answered && $("phone").dataset.state !== "ringing") { $("phone").dataset.state = "ringing"; show("incoming"); startRing(); } }
  // F3: "We've got it" only after the hub confirms handoff.started. Until then: "Handing off…"; on handoff.failed (or no answer in 8 s) she is told she is still on the call and the buttons come back.
  function pendingHandoff() { clearTimeout(st.handT); $("alertBox").hidden = true; $("idleMsg").hidden = true; const m = $("handoffMsg"); m.textContent = "Handing off… please stay on the line."; m.hidden = false; st.handT = setTimeout(() => failHandoff(), 8000); }
  function failHandoff() { clearTimeout(st.handT); if ($("phone").dataset.state !== "active") return; setBadge("alert"); const m = $("handoffMsg"); m.textContent = "Couldn't hand off. You're still on the call."; m.hidden = false; $("alertBox").hidden = false; $("idleMsg").hidden = true; }
  function showHandoff() { setBadge("handed"); $("handoffMsg").textContent = "We've got it. You can put the phone down."; $("alertBox").hidden = true; $("idleMsg").hidden = true; $("handoffMsg").hidden = false; }

  // ---- buttons ----
  $("answerBtn").onclick = () => {
    stopRing(); lockScreen(); emitUserAction("answer"); { const k = $("keepOpen"); if (k) { k.textContent = "Keep Backfire open during calls. If you switch apps, the call audio can pause."; k.hidden = !IOS; } }
    unlockAudio();                                   // tap unlocks audio so the alert beeps can play
    if (BF.voip) BF.voip.answer();                   // real WebRTC call, if one is ringing
    st.answered = true; st.t0 = Date.now(); st.timer = setInterval(tick, 500); tick();
    $("activeName").textContent = $("callerNumber").textContent || "Unknown caller";
    $("phone").dataset.state = "active"; show("active");
    if (!SERVER) scheduleAfterAnswer();
  };
  $("declineBtn").onclick = () => { stopRing(); emitUserAction("decline"); if (BF.voip) BF.voip.hangup(); endCall("You declined the call."); };
  $("endBtn").onclick = () => { emitUserAction("hang_up"); if (BF.voip) BF.voip.hangup(); stopReplay(); endCall("You ended the call."); };
  $("btnContinue").onclick = () => { emitUserAction("continue"); setBadge("watching"); $("alertBox").hidden = true; $("idleMsg").hidden = false; };
  $("btnGets").onclick = () => { emitUserAction("scammer_get_scammed"); if (SERVER) pendingHandoff(); else showHandoff(); };
  $("btnHang").onclick = () => { emitUserAction("hang_up"); if (BF.voip) BF.voip.hangup(); stopReplay(); endCall("You hung up."); };
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
      $("src").textContent = "· demo replay: " + call.call_id;
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
    $("callerNumber").textContent = info.from || ""; $("activeName").textContent = info.from || "Call in progress";
    $("phone").dataset.state = "active"; show("active"); setBadge("watching"); lockScreen();
    const ts = new Date().toISOString(); BF.onEvent && BF.onEvent({ type: "call.answered", call_id: id, ts, data: { by: "resume" } });
    if (info.handoff) { BF.onEvent && BF.onEvent({ type: "handoff.started", call_id: id, ts, data: {} }); showHandoff(); }
  }

  function needsSetup() { try { return !localStorage.getItem("bf.done") && !qs.has("skipsetup"); } catch (e) { return false; } }
  function start() {
    setBadge("watching"); $("guard").hidden = false; $("alertBox").hidden = true; $("handoffMsg").hidden = true; $("idleMsg").hidden = false;
    st.callId = null; window.__userActions.length = 0; show("ended"); $("endedMsg").textContent = "Waiting for a call…"; $("replayBtn").hidden = !!SERVER;
    $("src").textContent = SERVER ? "· live" : "· demo replay";
    if (SERVER) {
      if (!ws) connectWS();
      // F10: a reload / iOS resume in the middle of a call must not lose it: ask the hub for the active call (paired /demo/status: active_call_ids = ["id"] or [{call_id, from, age_s, handoff}], top level or in flags) and re-subscribe /listen + /talk.
      BF.hubFetch("/demo/status?format=json").then(r => r.ok ? r.json() : null).then(j => { const ids = j && (j.active_call_ids || (j.flags && j.flags.active_call_ids)); if (Array.isArray(ids) && ids.length) resumeCall(ids[ids.length - 1]); }).catch(() => {});
      // Honest footer: a hub in fallback/demo mode is replaying a recorded story, not a live phone line (fail soft: keep "live" if unknown).
      fetch(HUB + "/demo/status?format=json").then(r => r.json()).then(j => { const f = (j && j.flags) || {}; if (f.FALLBACK || f.DEMO_MODE) { $("src").textContent = "· replay (recorded demo)"; BF.replay = true; } }).catch(() => {});
    }
    else if (needsSetup()) BF.pendingStart = startReplay;      // demo call waits until onboarding is finished
    else startReplay();
  }

  // "Add to Home Screen" hint: first visit, iOS Safari (not yet installed). Dismissed once = never again.
  (function () { try { const standalone = window.matchMedia("(display-mode: standalone)").matches || navigator.standalone; if (standalone || localStorage.getItem("bf.a2hs") === "1") return; const h = $("a2hs"); if (!h) return;
    const android = /Android/.test(navigator.userAgent); if (!IOS && !android) return;
    $("a2hsText").textContent = IOS ? "Add Backfire to your Home Screen: tap Share, then Add to Home Screen." : "Add Backfire to your Home Screen: open the browser menu, then Install app.";
    h.hidden = false; $("a2hsClose").onclick = () => { h.hidden = true; try { localStorage.setItem("bf.a2hs", "1"); } catch (e) {} }; } catch (e) {} })();
  setInterval(() => { const n = new Date(); $("clock").textContent = (n.getHours() % 12 || 12) + ":" + String(n.getMinutes()).padStart(2, "0"); }, 1000);
  window.BF.deliver = onEvent; BF.endUI = endCall; BF.ui = () => $("phone").dataset.state;
  start();
})();
