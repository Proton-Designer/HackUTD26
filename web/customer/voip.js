// Telnyx WebRTC: Maria's phone registers as a SIP user and rings for real. Optional: if there is no hub, no token or the SDK fails to
// load, the app keeps working on hub events / mock replay (fail open). The token comes from the hub (GET /voip/webrtc-token) and
// goes only to Telnyx. ?devtoken= is for local testing only. No credentials are stored in this app.
// Note: the call audio is the real phone call; Backfire's analysis only ever uses the caller side on the server.
(() => {
  "use strict";
  const SDK = "https://cdn.jsdelivr.net/npm/@telnyx/webrtc@2.28.1/lib/bundle.js";
  const qs = new URLSearchParams(location.search);
  const HUB = BF.hub, dev = ["localhost", "127.0.0.1"].includes(location.hostname) ? qs.get("devtoken") : null;   // a link must not be able to swap in someone else's SIP account
  const status = t => { const s = document.getElementById("src"); if (s) s.dataset.voip = t; console.log("[backfire] voip:", t); BF.voipStatus = t; };
  let client = null, call = null, wantAnswer = 0;   // wantAnswer (timestamp, honoured for 4 s only): user tapped Answer before the SIP leg arrived (hub call.incoming can beat the INVITE by ~1 s)
  if (!dev && !(HUB && !qs.has("novoip") && location.pathname.startsWith("/app")) && !qs.has("webrtc")) { status("off"); return; }

  const audio = document.createElement("audio"); audio.autoplay = true; audio.setAttribute("playsinline", ""); document.body.append(audio);

  async function getToken() {
    if (dev) return { login_token: dev };
    const r = await BF.hubFetch("/voip/webrtc-token"); if (!r.ok) throw new Error("token " + r.status);
    const j = await r.json();   // {token} (JWT) or {login, password} (SIP credentials, paired device only); held in memory, never stored
    if (j.token) return { login_token: j.token };
    if (j.login && j.password) return { login: j.login, password: j.password };
    throw new Error("no credentials in response");
  }
  function loadSdk() {
    return new Promise((res, rej) => { if (window.TelnyxWebRTC) return res(); const s = document.createElement("script"); s.src = SDK; s.onload = res; s.onerror = () => rej(new Error("sdk load")); document.head.append(s); });
  }
  function onCall(c) {
    const st = c.state;
    (BF.voipEvents = BF.voipEvents || []).push(Date.now() + " " + st + " " + (c.direction || "") + " rs=" + !!c.remoteStream + (c.cause ? " cause=" + c.cause : "") + (c.causeCode ? " code=" + c.causeCode : "") + (c.sipCode ? " sip=" + c.sipCode : "") + (c.sipReason ? " reason=" + c.sipReason : ""));   // debug trail for call-state transitions
    if (st === "ringing" && c.direction === "inbound") {
      call = c;
      if (wantAnswer && Date.now() - wantAnswer < 4000) { wantAnswer = 0; try { c.answer(); } catch (e) { status("answer failed: " + e); } }
      // normally the hub's call.incoming drives the ring screen; if it hasn't arrived shortly, ring from the SIP call itself
      setTimeout(() => { if (call === c && !["ringing", "active"].includes(BF.ui())) BF.deliver({ type: "call.incoming", call_id: "sip_" + c.id, ts: new Date().toISOString(), data: { from: c.remoteCallerNumber || "Unknown caller", scam_id_score: 0, attestation: "C" } }); }, 1500);
    } else if (st === "active" && c.remoteStream) {
      audio.srcObject = c.remoteStream; audio.play().catch(e => { (BF.voipEvents = BF.voipEvents || []).push(Date.now() + " play() rejected: " + e); });
    } else if (["hangup", "destroy"].includes(st) && call === c) {
      call = null; wantAnswer = 0; audio.srcObject = null;
      if (["ringing", "active"].includes(BF.ui())) BF.endUI("Call ended.");
    }
  }
  BF.voip = {
    answer() { if (call) { try { call.answer(); } catch (e) { status("answer failed: " + e); } } else wantAnswer = Date.now(); },
    hangup() { wantAnswer = 0; if (call) { try { call.hangup(); } catch (e) {} call = null; } }
  };
  (async () => {
    try {
      if (await BF.simP) { status("sim (no Telnyx)"); return; }   // phone-free mode: never log in to Telnyx
      const creds = await getToken(); await loadSdk();
      client = new TelnyxWebRTC.TelnyxRTC(creds);
      client.on("telnyx.ready", () => status("ready"));
      client.on("telnyx.error", e => status("error: " + (e && (e.message || (e.error && (e.error.message || e.error.code)) || JSON.stringify(e)) || e)));
      client.on("telnyx.socket.close", () => status("closed"));
      client.on("telnyx.notification", n => { (BF.voipEvents = BF.voipEvents || []).push(Date.now() + " notif " + n.type + (n.error ? " err=" + JSON.stringify(n.error).slice(0, 120) : "")); if (n.type === "callUpdate" && n.call) onCall(n.call); });
      client.connect(); status("connecting");
    } catch (e) { status("unavailable: " + e.message); }   // fail open: the rest of the app is unaffected
  })();
})();
