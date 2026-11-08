// Phone-free sim mode: when the hub runs a simulated call there is no SIP leg, so this page plays the caller's audio itself so judges hear the scammer.
// Rings/answers from hub events (call.incoming / call.answered), plays GET <hub>/demo/caller.wav (override: ?simwav=/path on the same hub) synced to call start,
// pauses while Backfire has the call (handoff) and resumes at the live offset on handoff.restored. Fails soft: no WAV = silent call, text still works.
(() => {
  "use strict";
  const HUB = BF.hub; if (!HUB) return;
  const qs = new URLSearchParams(location.search), $ = id => document.getElementById(id);
  const p = qs.get("simwav"), WAV = HUB + (p && /^\/[^/]/.test(p) ? p : "/demo/caller.wav");   // same hub only
  let a = null, t0 = null, tapped = false, held = false, tapT = null;
  const off = () => Math.max(0, (Date.now() - t0) / 1000);
  function stop() { clearTimeout(tapT); if (a) { try { a.pause(); } catch (e) {} a = null; } t0 = null; tapped = false; held = false; }
  function play() {
    if (!BF.sim || !a || held) return;
    try { a.currentTime = off(); } catch (e) {}
    const r = a.play(); if (r && r.catch) r.catch(() => {    // autoplay blocked: next tap anywhere starts it
      const b = $("sound"); if (b) { b.textContent = "🔇 Tap for sound"; b.classList.add("off"); }
      document.addEventListener("pointerdown", () => { play(); const s = $("sound"); if (s) { s.textContent = "🔊 Sound on"; s.classList.remove("off"); } }, { once: true });
    });
  }
  function start() {
    if (!BF.sim || a || !tapped || !t0 || $("phone").dataset.state !== "active") return;
    a = new Audio(WAV); a.preload = "auto"; a.setAttribute("playsinline", ""); a.onerror = () => { console.warn("[backfire] sim caller audio unavailable:", WAV); };
    BF.simAudio = a; a.addEventListener("loadedmetadata", play, { once: true }); a.load(); play();
  }
  $("answerBtn").addEventListener("click", () => { tapped = true; if (!t0) tapT = setTimeout(() => { t0 = t0 || Date.now(); start(); if (BF.listen && !lws && lastCid) { want = "caller"; decoyStart(lastCid); } }, 1500); setTimeout(start, 0); });   // no call.answered within 1.5 s: sync to the tap
  ["declineBtn", "endBtn", "btnHang"].forEach(id => $(id).addEventListener("click", stop));
  // ---- decoy listen-in: after handoff the page plays Backfire's decoy live (WS /listen/{call_id}, {track:'caller'|'decoy', payload: base64 PCMU 8 kHz 20 ms}) ----
  const ULAW = (() => { const t = new Float32Array(256); for (let i = 0; i < 256; i++) { const u = ~i & 255, s = u & 128 ? -1 : 1, e = (u >> 4) & 7, m = u & 15; t[i] = s * (((m << 3) + 132) * (1 << e) - 132) / 32768; } return t; })();
  let lws = null, dctx = null, dgain = null, dnext = 0, dcid = null, want = "decoy", lastCid = null;   // want: which /listen track to play ('caller' in listening mode until handoff, then 'decoy')
  const stats = BF.decoyStats = { frames: 0, bytes: 0, late: 0, state: "idle" };
  function decoyLabel(on) { const l = $("decoyMsg"); if (l) { l.textContent = want === "caller" ? "🎧 Listening to the caller" : "🎧 Listening to Backfire's decoy"; l.hidden = !on; } }
  function decoyStop() { try { lws && lws.close(); } catch (e) {} lws = null; dnext = 0; decoyLabel(false); stats.state = "idle"; try { dgain && dgain.disconnect(); } catch (e) {} dgain = null; }
  function decoyPlay(b64) {
    let bin; try { bin = atob(b64); } catch (e) { return; }
    const n = bin.length; if (!n) return;
    if (!dctx) { try { dctx = new (window.AudioContext || window.webkitAudioContext)(); } catch (e) { return; } }
    if (dctx.state === "suspended") { dctx.resume().catch(() => {}); const b = $("sound"); if (b) { b.textContent = "🔇 Tap for sound"; b.classList.add("off"); } document.addEventListener("pointerdown", () => { try { dctx.resume(); } catch (e) {} const s2 = $("sound"); if (s2) { s2.textContent = "🔊 Sound on"; s2.classList.remove("off"); } }, { once: true }); }
    if (!dgain) { dgain = dctx.createGain(); dgain.connect(dctx.destination); BF.decoyAnalyser = dctx.createAnalyser(); dgain.connect(BF.decoyAnalyser); }
    const buf = dctx.createBuffer(1, n, 8000), ch = buf.getChannelData(0);
    for (let i = 0; i < n; i++) ch[i] = ULAW[bin.charCodeAt(i)];
    const src = dctx.createBufferSource(); src.buffer = buf; src.connect(dgain);
    const now = dctx.currentTime; if (dnext < now + 0.02) { if (dnext) stats.late++; dnext = now + 0.12; }   // small jitter buffer (120 ms); re-prime after an underrun
    src.start(dnext); dnext += n / 8000; stats.frames++; stats.bytes += n;
  }
  function decoyStart(cid) {
    decoyStop(); dcid = cid; if (!(BF.sim || BF.listen) || !cid) return;
    let tok = null; try { tok = BF.deviceToken && BF.deviceToken(); } catch (e) {}
    try {
      const url = HUB.replace(/^http/, "ws") + "/listen/" + encodeURIComponent(cid);   // token travels as a subprotocol, never in the URL
      lws = tok ? new WebSocket(url, ["bf-device", tok]) : new WebSocket(url);
      stats.state = "connecting";
      lws.onopen = () => { stats.state = "open"; };
      lws.onmessage = m => { let j; try { j = JSON.parse(m.data); } catch (e) { return; } if (j && j.track === want && j.payload) { if (!stats.frames) decoyLabel(true); decoyPlay(j.payload); } };
      lws.onclose = () => { if (stats.state !== "idle") stats.state = "closed"; };
      lws.onerror = () => { stats.state = "error"; };   // fail soft: no decoy audio, the handoff screen still works
    } catch (e) { stats.state = "error"; }
  }
  const prev = BF.onEvent;
  BF.onEvent = ev => {
    if (prev) prev(ev);
    switch (ev && ev.type) {
      case "call.incoming": lastCid = ev.call_id; decoyStop(); stop(); break;
      case "call.answered":
        if (!BF.sim && !BF.listen) break;
        lastCid = ev.call_id || lastCid; t0 = Date.parse(ev.ts) || Date.now();
        if ($("phone").dataset.state === "ringing") $("answerBtn").click();   // no SIP leg to answer: the page answers for Maria
        else start();
        if (BF.listen) { want = "caller"; stats.frames = 0; stats.late = 0; decoyStart(lastCid); }   // listening mode: the real caller, live
        break;
      case "handoff.started":
        held = true; if (a) a.pause(); want = "decoy"; stats.frames = 0; stats.late = 0; dnext = 0; decoyLabel(false);
        if (BF.listen && lws) {} else decoyStart(ev.call_id);   // listening mode keeps its socket, only the wanted track changes
        break;
      case "handoff.restored":
        held = false;
        if (BF.listen) { want = "caller"; stats.frames = 0; dnext = 0; decoyLabel(false); } else { decoyStop(); play(); }
        break;
      case "call.ended": decoyStop(); stop(); break;
    }
  };
})();
