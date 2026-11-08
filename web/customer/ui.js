// Onboarding, voice consent/enroll, protection log. Talks to the hub only via BF.hub (null = local simulation).
(() => {
  "use strict";
  const $ = id => document.getElementById(id);
  const HUB = BF.hub;
  const CONSENT_VERSION = "v1";
  const store = {
    get: k => { try { return localStorage.getItem("bf." + k); } catch (e) { return null; } },
    set: (k, v) => { try { v == null ? localStorage.removeItem("bf." + k) : localStorage.setItem("bf." + k, v); } catch (e) {} }
  };
  const qs = new URLSearchParams(location.search);
  const state = { blocked: [], calls: 0, guardOn: store.get("on") !== "0", voiceId: store.get("voice") };

  // ---- views ----
  const VIEWS = ["callView", "protView", "setupView"];
  function view(v) {
    VIEWS.forEach(x => $(x).hidden = x !== v);
    document.querySelectorAll("#tabs button").forEach(b => b.classList.toggle("on", b.dataset.v === v));
    $("tabs").hidden = v === "setupView" || ["ringing", "active"].includes($("phone").dataset.state);
    if (v === "protView") renderProtection();
  }
  document.querySelectorAll("#tabs button").forEach(b => b.onclick = () => view(b.dataset.v));
  // Fixed bottom bar (UI review 2): screens get bottom padding only while the bar is up, so it never covers content.
  const padTabs = () => $("phone").classList.toggle("tabs-on", !$("tabs").hidden);
  new MutationObserver(padTabs).observe($("tabs"), { attributes: true, attributeFilter: ["hidden"] }); padTabs();
  // a call always takes over the screen; tabs return when it is over
  new MutationObserver(() => {
    const s = $("phone").dataset.state;
    if (s === "ringing" || s === "active") { VIEWS.forEach(x => $(x).hidden = x !== "callView"); $("tabs").hidden = true; document.querySelectorAll("#tabs button").forEach(b => b.classList.toggle("on", b.dataset.v === "callView")); }
    else if ($("setupView").hidden) $("tabs").hidden = false;
  }).observe($("phone"), { attributes: true, attributeFilter: ["data-state"] });

  // ---- hub helpers (fail soft: the screen never breaks if the hub is down) ----
  async function hub(method, path, body) {
    const r = await BF.hubFetch(path, { method, headers: { "Content-Type": "application/json" }, body: body ? JSON.stringify(body) : undefined });
    if (!r.ok) throw new Error(method + " " + path + " " + r.status);
    return r.json();
  }

  // ---- guard badge ----
  function applyGuard() { BF.guardOn = state.guardOn; if (BF.renderBadge) BF.renderBadge();
    // UI review 3 (A): never say "protected" while Live Guard is off
    const on = state.guardOn, t = $("homeTitle"), l = $("homeLead"), h = $("incomingHint");
    if (t) t.textContent = on ? "You're protected" : "Live Guard is off";
    if (l) l.textContent = on ? "Backfire listens to the caller's side of calls from numbers you don't know." : "Calls on this phone aren't being checked. Turn Live Guard on in Protection.";
    if (h) h.textContent = on ? "If you answer, Backfire listens to the caller only." : "Live Guard is off for this phone.";
    const sb = $("statsBox"); if (sb) sb.hidden = !(state.calls > 0 || state.blocked.length > 0);   // no 0 / 0 on a fresh install
  }

  // ---- protection log ----
  const fmt = n => /^\+1\d{10}$/.test(n || "") ? `+1 (${n.slice(2, 5)}) ${n.slice(5, 8)}-${n.slice(8)}` : (n || "");
  async function renderProtection() {
    paintProtection();   // local state first: the screen is never blank while the hub answers (UI review bug 4)
    if (HUB) {
      try { const d = await hub("GET", "/protection-log"); state.blocked = d.blocked || []; state.calls = (d.calls || []).length; }
      catch (e) { console.log("[backfire] protection-log unavailable", String(e)); }
    }
    paintProtection();
  }
  function paintProtection() {
    const ul = $("blockedList"); ul.replaceChildren();
    state.blocked.forEach(b => {
      const li = document.createElement("li"); const d = document.createElement("div");
      d.textContent = fmt(b.number); const sm = document.createElement("small"); sm.textContent = b.reason || "Blocked for you"; d.append(sm);
      const u = document.createElement("button"); u.className = "undo"; u.textContent = "Undo"; u.setAttribute("aria-label", "Undo block of " + fmt(b.number));
      u.onclick = () => undo(b);
      li.append(d, u); ul.append(li);
    });
    $("blockedEmpty").hidden = state.blocked.length > 0;
    $("callsCount").textContent = state.calls; $("blockedCount").textContent = state.blocked.length; renderDns(); $("statCalls").textContent = state.calls; $("statBlocked").textContent = state.blocked.length;
    $("guardState").textContent = state.guardOn ? "On. Backfire is watching the caller's side of calls from numbers it doesn't know." : "Off. Calls are not being checked.";
    $("guardToggle").setAttribute("aria-checked", String(!!state.guardOn));   // UI review 3: a real switch (role=switch), not a text button
    $("voiceState").textContent = state.voiceNote ? state.voiceNote : state.voiceId ? "Set up. Backfire keeps only a short voice sample, used only if you press Fire Back." + (HUB ? "" : " (Simulated)") : "No voice profile.";
    $("voiceDelete").hidden = !state.voiceId; $("voiceSetup").hidden = !!state.voiceId; paintHome();
    applyGuard();
  }
  async function undo(b) {
    try { if (HUB) await hub("POST", "/protection-log/undo", { undo_token: b.undo_token }); }
    catch (e) { console.log("[backfire] undo failed", String(e)); return; }   // keep the row if the hub refused
    state.blocked = state.blocked.filter(x => x !== b); renderProtection();
  }
  // Turning Live Guard off never touches the voice by itself. Only the separate, unticked-by-default "Also delete my voice" box does (and the hub may still refuse: 409 = locked).
  function setGuard(on) { state.guardOn = on; store.set("on", on ? "1" : "0"); renderProtection(); }
  $("guardToggle").onclick = () => {
    if (state.guardOn && state.voiceId) { $("guardAlso").checked = false; $("guardOffBox").hidden = false; $("guardToggle").hidden = true; $("guardOffNo").focus(); return; }
    setGuard(!state.guardOn);
  };
  $("guardOffNo").onclick = () => { $("guardOffBox").hidden = true; $("guardToggle").hidden = false; };
  $("guardOffYes").onclick = async () => {
    const del = $("guardAlso").checked; $("guardOffBox").hidden = true; $("guardToggle").hidden = false;
    setGuard(false);
    if (del) await deleteVoice();   // on failure (e.g. 409 locked) deleteVoice leaves its message on screen
  };

  // events from the hub / replay
  BF.onEvent = ev => {
    const d = ev.data || {};
    if (ev.type === "blocklist.updated" && d.scope === "her" && !state.blocked.some(b => b.undo_token === d.undo_token))
      state.blocked.push({ number: d.number, reason: "Caught after Fire Back", undo_token: d.undo_token });
    if (ev.type === "call.ended") state.calls++;
    if (ev.type === "blocklist.updated" || ev.type === "call.ended") setTimeout(renderProtection, 0);   // live update while she is looking at the log
    if (ev.type === "voice.enrolled" && d.voice_id) { state.voiceId = d.voice_id; store.set("voice", d.voice_id); paintHome(); }
    if (ev.type === "voice.deleted") { state.voiceId = null; store.set("voice", null); paintHome(); }
  };

  // ---- voice delete ----
  async function deleteVoice() {
    try { if (HUB && state.voiceId) await hub("DELETE", "/voice/" + encodeURIComponent(state.voiceId)); }
    catch (e) { console.log("[backfire] voice delete failed", String(e)); state.voiceNote = /\b409\b/.test(String(e)) ? "Voice is locked for the demo." : "Could not delete your voice right now. Try again."; $("voiceState").textContent = state.voiceNote; return false; }
    state.voiceNote = ""; state.voiceId = null; store.set("voice", null); renderProtection(); return true;
  }
  // Deleting the voice always needs an explicit in-page confirmation (it is the voice Backfire uses for every call).
  $("voiceDelete").onclick = () => { state.voiceNote = ""; $("voiceConfirm").hidden = false; $("voiceDelete").hidden = true; $("voiceNo").focus(); };
  $("voiceNo").onclick = () => { $("voiceConfirm").hidden = true; $("voiceDelete").hidden = !state.voiceId; };
  $("voiceYes").onclick = async () => { $("voiceConfirm").hidden = true; await deleteVoice(); };

  // ---- onboarding: 1 turn on -> 2 voice consent (separate, optional) -> rec read-aloud -> dns Do Not Screen (optional) -> 3 done ----
  // ---- onboarding (UI review 2): one screen, one button, straight to Home. Voice is offered later from a Home card (consent -> record). ----
  const STEPS = ["step1", "step2", "stepRec"], STEP_NO = { 1: 0, 2: 1, rec: 2 };
  function setup(step) {
    VIEWS.forEach(x => $(x).hidden = x !== "setupView"); $("tabs").hidden = true;
    STEPS.forEach((s, i) => $(s).hidden = i !== STEP_NO[step]);
    window.scrollTo(0, 0);
  }
  function home() { view("callView"); applyGuard(); paintHome(); if (BF.pendingStart) { const f = BF.pendingStart; BF.pendingStart = null; f(); } }
  function finish(msg) { $("homeNote").textContent = msg || ""; home(); }
  function paintHome() { const c = $("voiceCard"); if (c) c.hidden = !!state.voiceId || state.hubVoice === true || !state.guardOn; }
  BF.renderVoiceCard = () => paintHome();
  // end of the voice flow (the Do Not Screen list now lives in Protection only)
  function toDns(msg) { state.doneMsg = msg; if (state.fromSettings) { state.fromSettings = false; view("protView"); } else finish(msg); }
  // The one tap: turns Live Guard on, unlocks call sounds (same gesture) and asks for the mic now, with the reason on screen, so the prompt never comes mid-call.
  $("s1on").onclick = () => {
    store.set("on", "1"); state.guardOn = true; store.set("done", "1");
    try { BF.unlockAudio && BF.unlockAudio(); } catch (e) {}
    try { if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) navigator.mediaDevices.getUserMedia({ audio: true }).then(s => s.getTracks().forEach(t => t.stop())).catch(() => {}); } catch (e) {}
    finish("");
  };
  $("voiceCard").onclick = () => { state.fromSettings = false; setup(2); };
  $("s2skip").onclick = () => toDns("");
  $("s2agree").onclick = () => { const p = newParagraph(); if (!CONVO) $("paragraph").textContent = p; resetRec(); setup("rec"); };
  $("recSkip").onclick = () => { if (lowQ) { lowQ = false; toDns("Your voice is set up. Backfire is on. It keeps only a short voice sample, used only if you press Fire Back. You can delete it any time in Protection."); return; } stopMeter(); if (rec) { discard = true; rec.stop(); } toDns("Backfire is on. Scammers will hear a synthetic voice. You can set up your voice later in Protection."); };
  $("voiceSetup").onclick = () => { state.fromSettings = true; setup(2); };
  function dnsForm(open) { $("dnsForm").hidden = !open; $("dnsOpen").hidden = open; $("dnsOpen").setAttribute("aria-expanded", String(open)); if (open) $("dnsNumber").focus(); }
  $("dnsOpen").onclick = () => dnsForm(true);
  $("dnsCancel").onclick = () => { $("dnsNumber").value = ""; $("dnsLabel").value = ""; dnsForm(false); };

  // Do Not Screen list: kept on the phone; sent to the hub's trusted list when it has one (POST /trusted, fail soft).
  const dns = () => { try { return JSON.parse(store.get("dns") || "[]"); } catch (e) { return []; } };
  const saveDns = l => store.set("dns", JSON.stringify(l));
  function renderDns() {
    const l = dns();
    $("dnsList").replaceChildren(...l.map((x, i) => { const li = document.createElement("li"), s = document.createElement("span"), r = document.createElement("button"); s.textContent = (x.label ? x.label + " · " : "") + x.number; r.className = "undo"; r.textContent = "Remove"; r.setAttribute("aria-label", "Remove " + x.number); r.onclick = () => { const n = dns(); n.splice(i, 1); saveDns(n); HUB && hub("DELETE", "/trusted/" + encodeURIComponent(x.number)).catch(() => {}); renderDns(); }; li.append(s, r); return li; }));
  }
  $("dnsAdd").onclick = () => {
    const number = $("dnsNumber").value.replace(/[^\d+]/g, ""), label = $("dnsLabel").value.trim().slice(0, 40);
    if (number.replace(/\D/g, "").length < 7) { $("dnsNumber").focus(); return; }
    const l = dns(); if (!l.some(x => x.number === number)) { l.push({ number, label }); saveDns(l); HUB && hub("POST", "/trusted", { number, label }).catch(() => {}); }
    $("dnsNumber").value = ""; $("dnsLabel").value = ""; renderDns(); dnsForm(false);
  };

  // A random paragraph from a pool of 8, plus a random code word, so a recording can't simply be replayed. Each takes about 35-50 s at an easy pace.
  const PARAS = [
    "The little blue boat drifted slowly past the old stone bridge while the morning mist lifted off the water. A man on the bank waved to us, and we waved back. By noon the sun was warm, the bells in the village rang twelve times, and we shared bread, cheese, and sweet red grapes on the grass.",
    "My neighbor grows tomatoes and sweet peas by the garden gate. Every summer she leaves a basket on my porch with a note that says to enjoy them while they are fresh. In return, I bring her lemon cake on Sundays, and we sit together and talk about the weather and our grandchildren.",
    "On Saturday we walked to the market and bought warm bread, a jar of honey, and a bunch of yellow flowers. The baker knows my name and always adds one extra roll. We carried everything home slowly, stopping to rest on the bench by the fountain and watch the pigeons.",
    "The clock in the hall strikes every hour, loud and clear. When I was a girl, it woke me for school, and now it keeps me company in the evenings while I knit by the window. Outside, the streetlights come on one by one, and the whole neighborhood grows quiet and calm.",
    "A gentle rain fell on the quiet street all morning. I made a pot of tea, opened the book my sister gave me, and sat in the big green chair by the window. Later the clouds broke, a bright rainbow stretched over the rooftops, and the children ran outside to splash in the puddles.",
    "Last spring we planted a small apple tree in the back yard. It has grown taller than the fence, and this year it is full of white blossoms. My grandson says he will climb it when he is older, and I told him that apples taste best when you pick them yourself in the autumn.",
    "Every Thursday afternoon the library holds a story hour for the neighborhood. I sit near the back, and the librarian reads in a soft, steady voice. Afterward there are oatmeal cookies and warm cider, and we all trade recommendations for the next good book to borrow and enjoy.",
    "When the weather is fine, we drive out to the lake and have a picnic beside the water. I pack sandwiches, sliced pears, and a thermos of coffee. We watch the sailboats drift by, listen to the birds in the tall pines, and stay until the sky turns pink and gold."
  ];
  const CODE_WORDS = ["maple", "river", "lantern", "orchard", "copper", "meadow", "harbor", "violet"];
  // Conversational enrollment (?enroll=talk, or localStorage bf.enroll=talk; off by default: not shipped until P3 confirms it clones better): 3 casual questions answered out loud instead of reading a paragraph.
  // Zero-shot clones copy the reference's delivery, and read-aloud speech is flat. Same recorder settings, same /voice/enroll upload.
  const CONVO = qs.get("enroll") === "talk" || store.get("enroll") === "talk";
  const PROMPTS = ["Tell us about your weekend, like you're talking to a friend.", "What did you have for dinner last night?", "Tell us about a place you like to go, and why.", "What is something that made you laugh lately?", "Describe your morning, from when you woke up.", "Tell us about someone you enjoy spending time with.", "What would you do with a free afternoon?", "Tell us about your favorite meal and how it is made.", "What is the best trip you ever took?"];
  function newPrompts() { const p = [...PROMPTS].sort(() => Math.random() - 0.5).slice(0, 3); return p; }
  let curPrompts = [];
  function showPrompts() {
    curPrompts = newPrompts(); const bq = $("paragraph"); bq.replaceChildren();
    const ol = document.createElement("ol"); ol.className = "prompts"; curPrompts.forEach((t, i) => { const li = document.createElement("li"); li.textContent = t; if (i === 0) li.className = "now"; ol.append(li); }); bq.append(ol);
    const h = $("stepRec").querySelector("h1"); if (h) h.textContent = "Just talk to us";
    const b = $("stepRec").querySelector(".body"); if (b) b.innerHTML = "Press the red button and answer the questions out loud, <b>like you're chatting with a friend</b>. Don't read: just talk, about 30 to 60 seconds in all. Press <b>Stop</b> when you are done.";
  }
  const promptNow = s => { if (!CONVO) return; const lis = document.querySelectorAll("#paragraph .prompts li"); const k = Math.min(lis.length - 1, Math.floor(s / 17)); lis.forEach((li, i) => li.classList.toggle("now", i === k)); };
  function newParagraph() {
    if (CONVO) { showPrompts(); return ""; }
    const p = PARAS[Math.floor(Math.random() * PARAS.length)], w = CODE_WORDS[Math.floor(Math.random() * CODE_WORDS.length)];
    const digits = Array.from({ length: 4 }, () => Math.floor(Math.random() * 10)).join(" ");
    return p + " Today's code words are " + w + " " + digits + ".";
  }

  // ---- recording: MediaRecorder, 30-60 s, live level meter, review + re-record ----
  const MIN_S = 3, MAX_S = 60;   // Stop works after ~3 s; 60 s auto-stop
  let lowQ = false, rec = null, chunks = [], discard = false, blob = null, t0 = 0, tick = null, actx = null, raf = 0;
  const mmss = s => Math.floor(s / 60) + ":" + String(Math.floor(s % 60)).padStart(2, "0");
  function stopMeter() { clearInterval(tick); cancelAnimationFrame(raf); $("recLevel").style.width = "0%"; try { actx && actx.close(); } catch (e) {} actx = null; }
  function resetRec() { lowQ = false; $("recSkip").textContent = "Skip, use a synthetic voice"; stopMeter(); blob = null; chunks = []; $("recTime").textContent = "0:00"; $("recBtn").hidden = false; $("recBtn").disabled = false; $("recBtn").textContent = "● Start recording"; $("recReview").hidden = true; $("recStatus").textContent = ""; $("recSkip").hidden = false; }
  const b64 = blob => new Promise(res => { const r = new FileReader(); r.onload = () => res(String(r.result).split(",")[1] || ""); r.readAsDataURL(blob); });
  function busyMsg(t) { const s = $("recStatus"); s.textContent = ""; const i = document.createElement("span"); i.className = "spin"; i.setAttribute("aria-hidden", "true"); s.append(i, document.createTextNode(" " + t)); }
  async function enroll(b) {
    busyMsg("Saving your voice…"); $("recSave").disabled = true; $("recAgain").disabled = true; $("recSkip").disabled = true;
    const done = () => { $("recSave").disabled = false; $("recAgain").disabled = false; $("recSkip").disabled = false; };
    try {
      let voice_id, quality, above4k;
      if (HUB) {
        const body = { recording: await b64(b), mime: (b.type || "audio/webm").split(";")[0], consent_version: CONSENT_VERSION };
        const r = await Promise.race([hub("POST", "/voice/enroll", body), new Promise((_, rej) => setTimeout(() => rej(new Error("timeout")), 30000))]);
        voice_id = r && r.voice_id; quality = r && r.quality; above4k = r && r.above_4k_pct;
      } else voice_id = "v_simulated_" + Math.random().toString(36).slice(2, 8);   // no hub configured: simulated
      if (!voice_id) {                                      // {voice_id:null, fallback:"synthetic"}: the voice service is not connected. Never claim she is enrolled.
        state.voiceId = null; store.set("voice", null); done();
        toDns("Your voice wasn't saved; Backfire will use a synthetic voice. You can try again later in Protection.");
        return;
      }
      state.voiceId = voice_id; store.set("voice", voice_id); done();
      if (quality && quality !== "ok") {                       // the hub graded the recording as poor: offer a re-record (the saved sample still works)
        lowQ = true; const why = String(quality).replace(/^RE-RECORD:?\s*/i, "").trim();
        $("recStatus").textContent = "Saved, but the recording sounds like phone quality" + (why ? " (" + why + ")" : "") + "" + ". For a closer match, record again in a quiet room.";
        $("recSkip").hidden = false; $("recSkip").textContent = "Keep this voice and continue"; return;
      }
      toDns("Your voice is set up" + (HUB ? "" : " (simulated)") + (quality === "ok" ? " (recording quality: good)" : "") + ". Backfire is on. It keeps only a short voice sample, used only if you press Fire Back. You can delete it any time in Protection.");
    } catch (e) {
      console.log("[backfire] enroll failed", String(e)); done();
      $("recStatus").textContent = /\b401\b/.test(String(e)) ? "Please connect this phone to Backfire first, then try again." : "Your voice wasn't saved. Press Save to try again, or skip to use a synthetic voice.";   // handled errors stay out of Maria's face; BF.onUnauthorized shows the pair screen itself
    }
  }
  $("recSave").onclick = () => { if (blob) enroll(blob); };
  $("recAgain").onclick = () => { const p = newParagraph(); if (!CONVO) $("paragraph").textContent = p; resetRec(); };   // a fresh paragraph each time
  $("recBtn").onclick = async () => {
    if (rec) { if ((Date.now() - t0) / 1000 >= MIN_S) rec.stop(); return; }   // second press = stop
    try {
      if (!navigator.mediaDevices) throw new Error("no mic API");
      const stream = await navigator.mediaDevices.getUserMedia({ audio: { echoCancellation: false, noiseSuppression: false, autoGainControl: false, channelCount: 1, sampleRate: 48000 } });
      chunks = []; blob = null;
      const mime = ["audio/webm;codecs=opus", "audio/mp4", "audio/ogg"].find(t => { try { return MediaRecorder.isTypeSupported(t); } catch (e) { return false; } });   // iOS Safari records audio/mp4
      rec = mime ? new MediaRecorder(stream, { mimeType: mime, audioBitsPerSecond: 128000 }) : new MediaRecorder(stream, { audioBitsPerSecond: 128000 });
      rec.ondataavailable = e => chunks.push(e.data);
      rec.onstop = () => {
        stream.getTracks().forEach(t => t.stop()); stopMeter(); const r = rec; rec = null;
        if (discard) { discard = false; chunks = []; resetRec(); return; }
        blob = new Blob(chunks, { type: r.mimeType || mime || "audio/webm" });
        $("recBtn").hidden = true; $("recReview").hidden = false; $("recSave").disabled = false; $("recSkip").hidden = false;
        $("recStatus").textContent = "Recorded " + mmss((Date.now() - t0) / 1000) + ". Save it, or record again.";
      };
      // level meter (fail soft: recording still works without it)
      try { actx = new (window.AudioContext || window.webkitAudioContext)(); const an = actx.createAnalyser(); an.fftSize = 512; actx.createMediaStreamSource(stream).connect(an); const buf = new Uint8Array(512);
        const loop = () => { an.getByteTimeDomainData(buf); let m = 0; for (const v of buf) m = Math.max(m, Math.abs(v - 128)); $("recLevel").style.width = Math.min(100, m / 80 * 100) + "%"; raf = requestAnimationFrame(loop); }; loop(); } catch (e) {}
      rec.start(); t0 = Date.now(); $("recBtn").textContent = "■ Stop"; $("recBtn").disabled = true; $("recSkip").hidden = true; $("recStatus").textContent = "Recording… read the words above.";
      tick = setInterval(() => { const s = (Date.now() - t0) / 1000; $("recTime").textContent = mmss(s); promptNow(s); if (s >= MIN_S) $("recBtn").disabled = false; if (s >= MAX_S && rec) rec.stop(); }, 250);
    } catch (e) {
      $("recStatus").textContent = "We couldn't use the microphone. Allow it in your browser and try again, or skip.";
      if (qs.has("fakemic")) { blob = new Blob(["x"], { type: "audio/webm" }); enroll(blob); }   // test hook only
    }
  };

  // ---- boot ----
  renderProtection();   // fills the idle stats (calls handled / numbers blocked); waits for pairing, fails soft
  applyGuard();
  if (!store.get("done") && !qs.has("skipsetup")) setup(1); else view("callView");
  BF.setup = setup; BF.view = view; BF._enroll = enroll;
  BF.hasVoice = () => !!state.voiceId || state.hubVoice === true;   // the decoy's voice is per hub: a clone enrolled on another phone counts
  if (HUB) BF.hubFetch("/voice/status").then(r => r.ok ? r.json() : null).then(j => { if (j && typeof j.cloned === "boolean") { state.hubVoice = j.cloned; if (BF.renderVoiceCard) BF.renderVoiceCard(); } }).catch(() => {});   // app.js words the handoff/summary as "your voice" only when a voice is enrolled
})();
