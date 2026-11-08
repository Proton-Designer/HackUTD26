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
  let hubAnswered = false;   // the hub's call.answered has arrived for this call (nothing is opened before it, and never before the customer taps Answer)
  function afterAnswer() { start(); if (BF.listen && !lws && lastCid) { want = "caller"; stats.frames = 0; stats.late = 0; decoyStart(lastCid); } }
  $("answerBtn").addEventListener("click", () => { tapped = true; setTimeout(() => { if (hubAnswered) afterAnswer(); }, 0); });   // if the hub already answered the caller while it was ringing, start now; otherwise wait for call.answered
  ["declineBtn", "endBtn", "btnHang"].forEach(id => $(id).addEventListener("click", stop));
  // ---- decoy listen-in: after handoff the page plays Backfire's decoy live (WS /listen/{call_id}, {track:'caller'|'decoy', payload: base64 PCMU 8 kHz 20 ms}) ----
  const ULAW = (() => { const t = new Float32Array(256); for (let i = 0; i < 256; i++) { const u = ~i & 255, s = u & 128 ? -1 : 1, e = (u >> 4) & 7, m = u & 15; t[i] = s * (((m << 3) + 132) * (1 << e) - 132) / 32768; } return t; })();
  let lws = null, lwsCid = null, lwsExpected = false, lwsTry = 0, lwsT = null, active = null, dctx = null, dgain = null, dnext = 0, dcid = null, want = "decoy", lastCid = null;   // want: which /listen track to play ('caller' in listening mode until handoff, then 'decoy')
  const stats = BF.decoyStats = { frames: 0, bytes: 0, late: 0, state: "idle" };
  function decoyLabel(on) { const l = $("decoyMsg"); if (l) { l.textContent = want === "caller" ? "🎧 Listening to the caller" : "🎧 Listening to Backfire's decoy"; l.hidden = !on; } }
  function decoyStop() { clearTimeout(lwsT); lwsExpected = true; try { lws && lws.close(); } catch (e) {} lws = null; lwsCid = null; lwsTry = 0; dnext = 0; decoyLabel(false); stats.state = "idle"; try { dgain && dgain.disconnect(); } catch (e) {} dgain = null; }
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
  const TAB = Math.random().toString(36).slice(2), lock = k => { try { const j = JSON.parse(localStorage.getItem(k) || "null"); return j && j.tab !== TAB && Date.now() - j.ts < 4000; } catch (e) { return false; } };
  const hold = k => { try { localStorage.setItem(k, JSON.stringify({ tab: TAB, ts: Date.now() })); } catch (e) {} };
  setInterval(() => { if (lws && lws.readyState <= 1 && lwsCid) hold("bf.lock.listen." + lwsCid); }, 1500);
  function decoyStart(cid) {
    if (!(BF.sim || BF.listen) || !cid) return;
    if (lock("bf.lock.listen." + cid)) { stats.state = "other-tab"; return; }   // another tab of this phone already listens to this call: never fight it
    hold("bf.lock.listen." + cid);
    if (lws && lwsCid === cid && lws.readyState <= 1) return;     // exactly ONE /listen per call: never open a second while one is open/connecting
    clearTimeout(lwsT); lwsExpected = true; try { lws && lws.close(); } catch (e) {} lws = null;   // a socket for another call is replaced
    dcid = cid; lwsCid = cid; lwsExpected = false;
    let tok = null; try { tok = BF.deviceToken && BF.deviceToken(); } catch (e) {}
    try {
      const url = HUB.replace(/^http/, "ws") + "/listen/" + encodeURIComponent(cid);   // token travels as a subprotocol, never in the URL
      const w = lws = tok ? new WebSocket(url, ["bf-device", tok]) : new WebSocket(url);
      stats.state = "connecting";
      w.onopen = () => { stats.state = "open"; lwsTry = 0; };
      w.onmessage = m => { let j; try { j = JSON.parse(m.data); } catch (e) { return; } if (j && j.track === want && j.payload) { if (!stats.frames) decoyLabel(true); decoyPlay(j.payload); } };
      w.onclose = ev => {
        if (lws === w) lws = null;
        const final = ev && [1000, 1008, 1013].includes(ev.code);   // 1000 = the hub REPLACED this socket (another tab/device took over) or ended it: reconnecting would ping-pong forever
        if (lwsExpected || final || active !== cid || lwsTry >= 6) { if (!lwsExpected) stats.state = "closed"; return; }
        stats.state = "reconnecting"; lwsT = setTimeout(() => { if (active === cid && !lws) decoyStart(cid); }, Math.min(4000, 500 * 2 ** lwsTry++));   // unexpected close during the call: back off, retry
      };
      w.onerror = () => { stats.state = "error"; };   // fail soft: the handoff screen still works
    } catch (e) { stats.state = "error"; }
  }
  const prev = BF.onEvent;
  BF.onEvent = ev => {
    if (prev) prev(ev);
    switch (ev && ev.type) {
      case "call.incoming": if (active === ev.call_id) break; hubAnswered = false; lastCid = ev.call_id; active = ev.call_id; decoyStop(); stop(); break;   // a repeated incoming for the same call must not tear the sockets down
      case "call.answered":
        if (!BF.sim && !BF.listen) break;
        lastCid = ev.call_id || lastCid; active = lastCid; hubAnswered = true; if (!t0) t0 = Date.parse(ev.ts) || Date.now();
        if ($("phone").dataset.state === "ringing") { if (qs.has("autoanswer")) $("answerBtn").click(); }   // NEVER answers by itself; ?autoanswer=1 is for automated test harnesses only
        else afterAnswer();                                                                                    // the customer already tapped Answer: audio starts now
        break;
      case "handoff.started":
        held = true; if (a) a.pause(); want = "decoy"; stats.frames = 0; stats.late = 0; dnext = 0; decoyLabel(false);
        if (BF.listen && lws) {} else decoyStart(ev.call_id);   // listening mode keeps its socket, only the wanted track changes
        break;
      case "handoff.restored":
        held = false;
        if (BF.listen) { want = "caller"; stats.frames = 0; dnext = 0; decoyLabel(false); } else { decoyStop(); play(); }
        break;
      case "call.ended": active = null; hubAnswered = false; decoyStop(); stop(); break;
    }
  };
})();
