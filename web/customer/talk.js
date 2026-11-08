// Talk mode (hub flag MARIA_LEG=talk, or ?talk=1): Maria speaks into the role-play call. Her microphone goes to WS <hub>/talk/<call_id> (subprotocol ['bf-device', token])
// as JSON {payload: base64 PCMU 8 kHz, 160 bytes = 20 ms}. The caller is played via /listen (sim.js). Sending stops while Backfire's decoy talks (handoff) and resumes on restore.
// Fails soft: no mic or no socket = she can still hear and use the buttons.
(() => {
  "use strict";
  const HUB = BF.hub; if (!HUB) return;
  const $ = id => document.getElementById(id);
  let ws = null, ctx = null, stream = null, proc = null, src = null, cid = null, muted = false, handed = false, starting = false;
  let acc = new Uint8Array(160), n = 0, sum = 0, cnt = 0, t = 0, level = 0;
  const stats = BF.talkStats = { frames: 0, state: "idle", mic: "off" };
  const ulaw = s => { s = Math.max(-1, Math.min(1, s)) * 32767 | 0; let sign = 0; if (s < 0) { s = -s; sign = 0x80; } s = Math.min(s, 32635) + 132; let e = 7; for (let m = 0x4000; (s & m) === 0 && e > 0; e--, m >>= 1); return ~(sign | (e << 4) | ((s >> (e + 3)) & 15)) & 255; };
  const b64 = u8 => { let s = ""; for (let i = 0; i < u8.length; i++) s += String.fromCharCode(u8[i]); return btoa(s); };
  const sending = () => !muted && !handed && ws && ws.readyState === 1;

  function onAudio(e) {
    const x = e.inputBuffer.getChannelData(0), ratio = ctx.sampleRate / 8000; let peak = 0;
    for (let i = 0; i < x.length; i++) {
      const v = x[i]; sum += v; cnt++; t += 1; if (Math.abs(v) > peak) peak = Math.abs(v);
      if (t >= ratio) {                                    // box-filter downsample to 8 kHz
        acc[n++] = ulaw(sum / cnt); sum = 0; cnt = 0; t -= ratio;
        if (n === 160) { if (sending()) { try { ws.send(JSON.stringify({ payload: b64(acc) })); stats.frames++; } catch (er) {} } n = 0; }
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
      stats.mic = "on"; hint("Wear earphones so the caller doesn't hear themselves.");
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
    if (handed) hint("Backfire is talking to the caller for you."); else if (muted) hint("You are muted. The caller can't hear you."); else if (stats.mic === "on") hint("Wear earphones so the caller doesn't hear themselves.");
  }
  function open(id) {
    close(); cid = id; if (!BF.talk || !id) return;
    let tok = null; try { tok = BF.deviceToken && BF.deviceToken(); } catch (e) {}
    try {
      const url = HUB.replace(/^http/, "ws") + "/talk/" + encodeURIComponent(id);
      ws = tok ? new WebSocket(url, ["bf-device", tok]) : new WebSocket(url);
      stats.state = "connecting"; ws.onopen = () => { stats.state = "open"; }; ws.onclose = () => { if (stats.state !== "idle") stats.state = "closed"; }; ws.onerror = () => { stats.state = "error"; };
    } catch (e) { stats.state = "error"; }
  }
  function close() { try { ws && ws.close(); } catch (e) {} ws = null; stats.state = "idle"; }
  function show(on) { const b = $("talkBox"); if (b) b.hidden = !(on && BF.talk); }
  function end() { close(); stopMic(); show(false); handed = false; muted = false; render(); }

  $("micBtn").addEventListener("click", () => { if (handed) return; if (!stream) { startMic(); return; } muted = !muted; render(); });   // first tap also (re)starts a blocked mic
  $("answerBtn").addEventListener("click", () => { if (!BF.talk) return; show(true); startMic(); });   // the tap is the gesture iOS wants for the mic prompt
  ["endBtn", "btnHang", "declineBtn"].forEach(id => $(id).addEventListener("click", end));
  new MutationObserver(() => { const a = $("alertBox"), b = $("talkBox"); if (a && b) b.classList.toggle("compact", !a.hidden); }).observe($("alertBox"), { attributes: true, attributeFilter: ["hidden"] });
  const prev = BF.onEvent;
  BF.onEvent = ev => {
    if (prev) prev(ev);
    if (!BF.talk || !ev) return;
    switch (ev.type) {
      case "call.incoming": end(); cid = ev.call_id; break;
      case "call.answered": cid = ev.call_id || cid; open(cid); show(true); break;
      case "handoff.started": handed = true; render(); break;
      case "handoff.restored": handed = false; render(); break;
      case "call.ended": end(); break;
    }
  };
})();
