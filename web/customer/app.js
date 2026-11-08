(() => {
  "use strict";
  const $ = id => document.getElementById(id);
  const qs = new URLSearchParams(location.search);
  const SERVER = qs.get("server");            // e.g. ws://localhost:8000/events ; absent -> in-app replay
  const DEBUG = qs.has("debug");
  window.__userActions = [];                  // test hook: every user.action emitted

  const st = { callId: null, answered: false, alerted: false, ctx: null, timer: null, t0: 0, replay: [], tos: [] };

  const log = (...a) => { console.log("[backfire]", ...a); if (DEBUG) { const l = $("log"); l.hidden = false; l.textContent += a.map(x => typeof x === "string" ? x : JSON.stringify(x)).join(" ") + "\n"; } };
  const show = id => { for (const s of ["incoming", "active", "ended"]) $(s).hidden = s !== id; };

  // ---- audio: unlock on a user tap (mobile autoplay), then beeps are local-only ----
  function unlockAudio() {
    try { st.ctx = st.ctx || new (window.AudioContext || window.webkitAudioContext)(); if (st.ctx.state === "suspended") st.ctx.resume(); } catch (e) { log("audio unavailable", String(e)); }
  }
  function beep(at, dur) {
    const c = st.ctx; if (!c) return;
    const o = c.createOscillator(), g = c.createGain();
    o.frequency.value = 880; o.connect(g); g.connect(c.destination);
    const t = c.currentTime + at;
    g.gain.setValueAtTime(0.0001, t); g.gain.exponentialRampToValueAtTime(0.4, t + 0.02); g.gain.exponentialRampToValueAtTime(0.0001, t + dur);
    o.start(t); o.stop(t + dur + 0.02);
  }
  const twoBeeps = () => { beep(0, 0.18); beep(0.3, 0.18); if (navigator.vibrate) navigator.vibrate([150, 100, 150]); };

  // ---- the ONE place user actions leave the app. Adapt here when interfaces.md lands. ----
  let ws = null;
  function emitUserAction(action) {
    const msg = { type: "user.action", call_id: st.callId, ts: new Date().toISOString(), data: { action } };
    window.__userActions.push(msg);
    log("user.action", msg);
    if (ws && ws.readyState === 1) ws.send(JSON.stringify(msg));
    return msg;
  }

  // ---- rendering ----
  function tick() { const s = Math.floor((Date.now() - st.t0) / 1000); $("timer").textContent = String(Math.floor(s / 60)).padStart(2, "0") + ":" + String(s % 60).padStart(2, "0"); }
  function renderChips(chips) { const ul = $("chips"); ul.replaceChildren(...(chips || []).map(c => { const li = document.createElement("li"); li.textContent = c; return li; })); }
  function endCall(msg) {
    clearInterval(st.timer); st.answered = false; show("ended"); $("endedMsg").textContent = msg || "";
    $("phone").dataset.state = "ended";
  }

  function onEvent(ev) {
    if (!ev || !ev.type) return;
    if (st.callId && ev.call_id && ev.call_id !== st.callId && ev.type !== "call.incoming") return;
    const d = ev.data || {};
    switch (ev.type) {
      case "call.incoming":
        st.callId = ev.call_id; st.alerted = false;
        $("callerNumber").textContent = d.from || "";
        $("scamLabel").hidden = !(d.scam_id_score >= 0.5);
        $("attest").textContent = d.attestation === "A" ? "Caller ID verified" : "Caller ID not verified";
        $("phone").dataset.state = "ringing"; show("incoming"); break;
      case "call.routed": $("guard").hidden = d.decision !== "LIVE_GUARD"; break;
      case "call.answered": break; // UI answers on tap
      case "call.ended": if (st.callId === ev.call_id) endCall(d.ended_by === "caller" ? "The caller hung up." : "Call ended."); break;
      case "alert.fired":
        if (d.level === "first" && st.alerted) break;      // re-alert only on level: realert
        st.alerted = true; renderChips(d.why_chips);
        $("alertBox").hidden = false; $("idleMsg").hidden = true; $("handoffMsg").hidden = true;
        twoBeeps(); break;
      case "handoff.started": showHandoff(); break;
      default: break;
    }
  }
  function showHandoff() { $("alertBox").hidden = true; $("idleMsg").hidden = true; $("handoffMsg").hidden = false; }

  // ---- buttons ----
  $("answerBtn").onclick = () => {
    unlockAudio();                                   // tap unlocks audio so the alert beeps can play
    st.answered = true; st.t0 = Date.now(); st.timer = setInterval(tick, 500); tick();
    $("activeName").textContent = $("callerNumber").textContent || "Unknown caller";
    $("phone").dataset.state = "active"; show("active");
    if (!SERVER) scheduleAfterAnswer();
  };
  $("declineBtn").onclick = () => endCall("You declined the call.");
  $("endBtn").onclick = () => { emitUserAction("hang_up"); stopReplay(); endCall("You ended the call."); };
  $("btnContinue").onclick = () => { emitUserAction("continue"); $("alertBox").hidden = true; $("idleMsg").hidden = false; };
  $("btnGets").onclick = () => { emitUserAction("scammer_get_scammed"); showHandoff(); };
  $("btnHang").onclick = () => { emitUserAction("hang_up"); stopReplay(); endCall("You hung up."); };
  $("replayBtn").onclick = start;

  // ---- sources ----
  function stopReplay() { st.tos.forEach(clearTimeout); st.tos = []; }
  function startReplay() {
    stopReplay(); const fx = window.BACKFIRE_FIXTURE || [];
    st.replay = fx.filter(e => e.afterAnswer);
    fx.filter(e => !e.afterAnswer && !e.onAnswer).forEach(e => st.tos.push(setTimeout(() => onEvent(e), e.t)));
  }
  function scheduleAfterAnswer() { st.replay.forEach(e => st.tos.push(setTimeout(() => onEvent(e), e.t))); }

  function connectWS() {
    ws = new WebSocket(SERVER);
    ws.onmessage = m => { try { onEvent(JSON.parse(m.data)); } catch (e) { log("bad msg", String(e)); } };
    ws.onclose = () => setTimeout(connectWS, 2000);
    ws.onerror = () => ws.close();
  }

  function start() {
    $("guard").hidden = false; $("alertBox").hidden = true; $("handoffMsg").hidden = true; $("idleMsg").hidden = false;
    st.callId = null; window.__userActions.length = 0; show("ended"); $("endedMsg").textContent = "Waiting for a call…"; $("replayBtn").hidden = !!SERVER;
    $("src").textContent = SERVER ? "· live" : "· demo replay";
    if (SERVER) { if (!ws) connectWS(); } else startReplay();
  }

  setInterval(() => { const n = new Date(); $("clock").textContent = (n.getHours() % 12 || 12) + ":" + String(n.getMinutes()).padStart(2, "0"); }, 1000);
  start();
})();
