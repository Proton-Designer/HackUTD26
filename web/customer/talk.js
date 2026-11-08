// Talk mode (hub flag MARIA_LEG=talk, or ?talk=1): Maria speaks into the role-play call. Her microphone goes to WS <hub>/talk/<call_id> (subprotocol ['bf-device', token])
// as JSON {payload: base64 PCMU 8 kHz, 160 bytes = 20 ms}. The caller is played via /listen (sim.js). Sending stops while Backfire's decoy talks (handoff) and resumes on restore.
// Fails soft: no mic or no socket = she can still hear and use the buttons.
(() => {
  "use strict";
  const HUB = BF.hub; if (!HUB) return;
  const $ = id => document.getElementById(id);
  let ws = null, wsCid = null, wsExpected = false, wsTry = 0, wsT = null, active = null, lastSend = 0, ctx = null, stream = null, proc = null, src = null, cid = null, muted = false, handed = false, starting = false;
  let acc = new Uint8Array(160), n = 0, sum = 0, cnt = 0, t = 0, level = 0;
  // Echo control. (1) voice gate: send only while the mic is above an adaptive floor (3x median of the last 2 s, with a 300 ms hangover).
  // (2) half-duplex duck: while the caller is audible on the speaker, send only if the mic is clearly louder (+10 dB) than the playback, unless she says she wears earphones.
  const GATE_MIN = 0.006, FLOOR_X = 3, HANG_MS = 300, PLAY_T = 0.01, DUCK_X = 1.6;
  let nf = 0.002, gateUntil = 0, playHist = [], earphones = false, fbuf = null;
  try { earphones = localStorage.getItem("bf.earphones") !== "0"; } catch (e) {}   // demo default: earphones ticked (only an explicit untick stores "0")
  const stats0 = { gate: "closed", duck: false };
  const stats = BF.talkStats = { frames: 0, state: "idle", mic: "off" };
  const ulaw = s => { s = Math.max(-1, Math.min(1, s)) * 32767 | 0; let sign = 0; if (s < 0) { s = -s; sign = 0x80; } s = Math.min(s, 32635) + 132; let e = 7; for (let m = 0x4000; (s & m) === 0 && e > 0; e--, m >>= 1); return ~(sign | (e << 4) | ((s >> (e + 3)) & 15)) & 255; };
  const b64 = u8 => { let s = ""; for (let i = 0; i < u8.length; i++) s += String.fromCharCode(u8[i]); return btoa(s); };
  let gateOpen = false;
  let hubAnswered = false;   // mic frames flow only after the hub's call.answered
  const sending = () => !muted && !handed && hubAnswered && gateOpen && ws && ws.readyState === 1;

  function onAudio(e) {
    const x = e.inputBuffer.getChannelData(0), ratio = ctx.sampleRate / 8000; let peak = 0, ss = 0;
    for (let i = 0; i < x.length; i++) ss += x[i] * x[i];
    const rms = Math.sqrt(ss / x.length), now = Date.now();
    // noise floor: drops to quiet immediately, creeps up only slowly (0.1 %/block), so a long sentence can't raise the floor above her own voice (a plain median would)
    nf = rms < nf ? nf + (rms - nf) * 0.5 : nf + (rms - nf) * 0.001;
    nf = Math.min(nf, 0.03);                                   // room noise never needs a floor above ~-30 dBFS
    const floor = Math.max(GATE_MIN, FLOOR_X * nf);
    let pr = 0; const an = BF.decoyAnalyser;                                    // how loud the caller is on the speaker right now
    if (an && !handed && an.context && an.context.state === "running") {   /* a suspended context would freeze the analyser and duck forever */ try { fbuf = fbuf && fbuf.length === an.fftSize ? fbuf : new Float32Array(an.fftSize); an.getFloatTimeDomainData(fbuf); let s2 = 0; for (let i = 0; i < fbuf.length; i++) s2 += fbuf[i] * fbuf[i]; pr = Math.sqrt(s2 / fbuf.length); } catch (er) {} }
    playHist.push(pr); if (playHist.length > 5) playHist.shift(); const play = Math.max.apply(null, playHist);   // last ~200 ms
    let open = rms > floor;
    stats.duck = !earphones && play > PLAY_T && !(rms > DUCK_X * play);        // caller audible and Maria not clearly louder: treat as echo
    if (stats.duck) open = false;
    if (open) gateUntil = now + HANG_MS;
    gateOpen = now < gateUntil; stats.gate = gateOpen ? "open" : "closed"; stats.rms = +rms.toFixed(4); stats.can = [muted, handed, gateOpen, !!ws, ws && ws.readyState].join(); stats.floor = +floor.toFixed(4); stats.play = +play.toFixed(4);
    for (let i = 0; i < x.length; i++) {
      const v = x[i]; sum += v; cnt++; t += 1; if (Math.abs(v) > peak) peak = Math.abs(v);
      if (t >= ratio) {                                    // box-filter downsample to 8 kHz
        acc[n++] = ulaw(sum / cnt); sum = 0; cnt = 0; t -= ratio;
        if (n === 160) { if (sending()) { try { ws.send(JSON.stringify({ payload: b64(acc) })); stats.frames++; lastSend = Date.now(); } catch (er) {} } n = 0; }
      }
    }
    level = Math.max(peak, level * 0.85); const l = $("talkLevel"); if (l) l.style.width = (muted || handed ? 0 : Math.min(100, level * 160)) + "%";
  }
  async function startMic() {
    if (stream || starting || !BF.talk) return; starting = true;
    try {
      stream = await navigator.mediaDevices.getUserMedia({ audio: { echoCancellation: true, noiseSuppression: true, autoGainControl: true } });
      ctx = new (window.AudioContext || window.webkitAudioContext)(); if (ctx.state === "suspended") ctx.resume().catch(() => {});
      src = ctx.createMediaStreamSource(stream); proc = ctx.createScriptProcessor(2048, 1, 1);
      proc.onaudioprocess = onAudio; src.connect(proc); proc.connect(ctx.destination);   // output stays silent (we never write to outputBuffer)
      stats.mic = "on"; hint("Use earphones so the caller doesn't hear himself.");
    } catch (e) { stats.mic = "blocked"; stream = null; hint("The microphone is blocked. Allow it in your browser, then tap the mic button."); }
    starting = false;
  }
  function stopMic() { try { proc && proc.disconnect(); src && src.disconnect(); } catch (e) {} try { stream && stream.getTracks().forEach(x => x.stop()); } catch (e) {} try { ctx && ctx.close(); } catch (e) {} proc = src = stream = ctx = null; n = 0; sum = cnt = t = 0; stats.mic = "off"; }
  function hint(s) { const h = $("talkHint"); if (h) h.textContent = s; }
  function render() {
    const b = $("micBtn"); if (!b) return;
    b.disabled = handed; b.setAttribute("aria-pressed", String(muted));
    b.textContent = handed ? "🛡" : muted ? "🔇" : "🎤";
    b.setAttribute("aria-label", handed ? "Backfire is talking for you" : muted ? "Muted. Tap to unmute" : "Microphone on. Tap to mute");
    if (handed) hint("Backfire is talking to the caller for you."); else if (muted) hint("You are muted. The caller can't hear you."); else if (stats.mic === "on") hint("Use earphones so the caller doesn't hear himself.");
  }
  const TAB = Math.random().toString(36).slice(2), lock = k => { try { const j = JSON.parse(localStorage.getItem(k) || "null"); return j && j.tab !== TAB && Date.now() - j.ts < 4000; } catch (e) { return false; } };
  const hold = k => { try { localStorage.setItem(k, JSON.stringify({ tab: TAB, ts: Date.now() })); } catch (e) {} };
  setInterval(() => { if (ws && ws.readyState <= 1 && wsCid) hold("bf.lock.talk." + wsCid); }, 1500);
  function open(id) {
    if (!BF.talk || !id) return;
    if (lock("bf.lock.talk." + id)) { stats.state = "other-tab"; return; }   // another tab of this phone already talks on this call
    hold("bf.lock.talk." + id);
    if (ws && wsCid === id && ws.readyState <= 1) return;           // exactly ONE /talk per call: never open a second while one is open/connecting
    clearTimeout(wsT); wsExpected = true; try { ws && ws.close(); } catch (e) {} ws = null;
    cid = id; wsCid = id; wsExpected = false;
    let tok = null; try { tok = BF.deviceToken && BF.deviceToken(); } catch (e) {}
    try {
      const url = HUB.replace(/^http/, "ws") + "/talk/" + encodeURIComponent(id);
      const w = ws = tok ? new WebSocket(url, ["bf-device", tok]) : new WebSocket(url);
      stats.state = "connecting";
      let opened = false; w.onopen = () => { opened = true; stats.state = "open"; wsTry = 0; refused = 0; };
      w.onclose = ev => {
        if (ws === w) ws = null;
        if (!wsExpected && active === id && ((ev && ev.code === 1013) || (!opened && ++refused >= 2))) { observer(); return; }   // 1013 = another device is already talking; a browser reports a refused handshake as 1006, so two never-opened tries count as refused too
        const final = ev && [1000, 1008, 1013].includes(ev.code);   // replaced by another tab/device or ended by the hub: do not reconnect (ping-pong)
        if (wsExpected || final || active !== id || wsTry >= 6) { if (!wsExpected) stats.state = "closed"; return; }
        stats.state = "reconnecting"; wsT = setTimeout(() => { if (active === id && !ws) open(id); }, Math.min(4000, 500 * 2 ** wsTry++));   // died unexpectedly mid-call: back off and retry
      };
      w.onerror = () => { stats.state = "error"; };
    } catch (e) { stats.state = "error"; }
  }
  let refused = 0;
  function observer() {                                   // another phone is the customer's client: watch only (alert, chips, buttons still work; first tap wins on the hub)
    stats.state = "observer"; BF.observer = true; stopMic(); const b = $("talkBox"); if (b) b.hidden = true;
    const o = $("observerMsg"); if (o) o.hidden = false;
  }
  function close() { clearTimeout(wsT); wsExpected = true; try { ws && ws.close(); } catch (e) {} ws = null; wsCid = null; wsTry = 0; stats.state = "idle"; }
  function show(on) { const b = $("talkBox"); if (b) b.hidden = !(on && BF.talk) || !!BF.observer; }
  function end() { active = null; hubAnswered = false; refused = 0; BF.observer = false; { const o = $("observerMsg"); if (o) o.hidden = true; } close(); stopMic(); show(false); handed = false; muted = false; render(); }

  const eb = $("earBox"); if (eb) { eb.checked = earphones; eb.onchange = () => { earphones = eb.checked; try { localStorage.setItem("bf.earphones", earphones ? "1" : "0"); } catch (e) {} }; }
  setInterval(() => { const d = $("micDot"); if (!d) return; const on = !!stream && Date.now() - lastSend < 1000; d.className = "dot " + (on ? "live" : stats.mic === "blocked" || stats.state === "error" ? "bad" : "idle"); d.title = on ? "Your voice is reaching the call" : "Not sending"; d.setAttribute("aria-label", d.title); }, 300);
  $("micBtn").addEventListener("click", () => { if (handed) return; if (!stream) { startMic(); return; } muted = !muted; render(); });   // first tap also (re)starts a blocked mic
  $("answerBtn").addEventListener("click", () => { if (!BF.talk) return; show(true); startMic(); if (hubAnswered) open(cid); });   // the tap is the gesture iOS wants for the mic prompt
  ["endBtn", "btnHang", "declineBtn"].forEach(id => $(id).addEventListener("click", end));
  new MutationObserver(() => { const a = $("alertBox"), b = $("talkBox"); if (a && b) b.classList.toggle("compact", !a.hidden); }).observe($("alertBox"), { attributes: true, attributeFilter: ["hidden"] });
  const prev = BF.onEvent;
  BF.onEvent = ev => {
    if (prev) prev(ev);
    if (!BF.talk || !ev) return;
    switch (ev.type) {
      case "call.incoming": if (active === ev.call_id) break; hubAnswered = false; end(); cid = ev.call_id; active = ev.call_id; break;   // a repeated incoming for the same call must not close the mic/socket
      case "call.answered": cid = ev.call_id || cid; active = cid; hubAnswered = true; if ($("phone").dataset.state === "active") { open(cid); show(true); } break;   // ringing + hub-answered: wait for the customer's Answer tap
      case "handoff.started": handed = true; render(); break;
      case "handoff.restored": handed = false; render(); break;
      case "call.ended": active = null; end(); break;
    }
  };
})();
