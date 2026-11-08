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
  // a call always takes over the screen; tabs return when it is over
  new MutationObserver(() => {
    const s = $("phone").dataset.state;
    if (s === "ringing" || s === "active") { VIEWS.forEach(x => $(x).hidden = x !== "callView"); $("tabs").hidden = true; }
    else if ($("setupView").hidden) $("tabs").hidden = false;
  }).observe($("phone"), { attributes: true, attributeFilter: ["data-state"] });

  // ---- hub helpers (fail soft: the screen never breaks if the hub is down) ----
  async function hub(method, path, body) {
    const r = await BF.hubFetch(path, { method, headers: { "Content-Type": "application/json" }, body: body ? JSON.stringify(body) : undefined });
    if (!r.ok) throw new Error(method + " " + path + " " + r.status);
    return r.json();
  }

  // ---- guard badge ----
  function applyGuard() { BF.guardOn = state.guardOn; if (BF.renderBadge) BF.renderBadge(); }

  // ---- protection log ----
  const fmt = n => /^\+1\d{10}$/.test(n || "") ? `+1 (${n.slice(2, 5)}) ${n.slice(5, 8)}-${n.slice(8)}` : (n || "");
  async function renderProtection() {
    if (HUB) {
      try { const d = await hub("GET", "/protection-log"); state.blocked = d.blocked || []; state.calls = (d.calls || []).length; }
      catch (e) { console.log("[backfire] protection-log unavailable", String(e)); }
    }
    const ul = $("blockedList"); ul.replaceChildren();
    state.blocked.forEach(b => {
      const li = document.createElement("li"); const d = document.createElement("div");
      d.textContent = fmt(b.number); const sm = document.createElement("small"); sm.textContent = b.reason || "Blocked for you"; d.append(sm);
      const u = document.createElement("button"); u.className = "undo"; u.textContent = "Undo"; u.setAttribute("aria-label", "Undo block of " + fmt(b.number));
      u.onclick = () => undo(b);
      li.append(d, u); ul.append(li);
    });
    $("blockedEmpty").hidden = state.blocked.length > 0;
    $("callsCount").textContent = state.calls; $("statCalls").textContent = state.calls; $("statBlocked").textContent = state.blocked.length;
    $("guardState").textContent = state.guardOn ? "On. Backfire is watching the caller's side of calls from numbers it doesn't know." + (state.voiceId ? " Turning it off also deletes your voice." : "") : "Off. Calls are not being checked.";
    $("guardToggle").textContent = state.guardOn ? "Turn Live Guard off" : "Turn Live Guard on";
    $("voiceState").textContent = state.voiceId ? "Set up. Backfire keeps only a short voice sample, used only if you press Scammer Get Scammed." + (HUB ? "" : " (Simulated)") : "No voice profile.";
    $("voiceDelete").hidden = !state.voiceId; $("voiceSetup").hidden = !!state.voiceId;
    applyGuard();
  }
  async function undo(b) {
    try { if (HUB) await hub("POST", "/protection-log/undo", { undo_token: b.undo_token }); }
    catch (e) { console.log("[backfire] undo failed", String(e)); return; }   // keep the row if the hub refused
    state.blocked = state.blocked.filter(x => x !== b); renderProtection();
  }
  // Consent promises the voice is deleted if she turns Backfire off, so turning it off deletes it (stays on if the delete fails).
  $("guardToggle").onclick = async () => {
    if (state.guardOn && state.voiceId && !(await deleteVoice())) return;
    state.guardOn = !state.guardOn; store.set("on", state.guardOn ? "1" : "0"); renderProtection();
  };

  // events from the hub / replay
  BF.onEvent = ev => {
    const d = ev.data || {};
    if (ev.type === "blocklist.updated" && d.scope === "her" && !state.blocked.some(b => b.undo_token === d.undo_token))
      state.blocked.push({ number: d.number, reason: "Caught after Scammer Get Scammed", undo_token: d.undo_token });
    if (ev.type === "call.ended") state.calls++;
    if (ev.type === "blocklist.updated" || ev.type === "call.ended") setTimeout(renderProtection, 0);   // live update while she is looking at the log
    if (ev.type === "voice.enrolled" && d.voice_id) { state.voiceId = d.voice_id; store.set("voice", d.voice_id); }
    if (ev.type === "voice.deleted") { state.voiceId = null; store.set("voice", null); }
  };

  // ---- voice delete ----
  async function deleteVoice() {
    try { if (HUB && state.voiceId) await hub("DELETE", "/voice/" + encodeURIComponent(state.voiceId)); }
    catch (e) { console.log("[backfire] voice delete failed", String(e)); $("voiceState").textContent = "Could not delete your voice right now. Try again."; return false; }
    state.voiceId = null; store.set("voice", null); renderProtection(); return true;
  }
  $("voiceDelete").onclick = deleteVoice;
  $("voiceSetup").onclick = () => { setup(2); };

  // ---- onboarding: 1 turn on -> 2 voice consent (separate, optional) -> rec read-aloud -> dns Do Not Screen (optional) -> 3 done ----
  const STEPS = ["step1", "step2", "stepRec", "stepDns", "step3"], STEP_NO = { 1: 0, 2: 1, rec: 2, dns: 3, 3: 4 };
  function setup(step) {
    VIEWS.forEach(x => $(x).hidden = x !== "setupView"); $("tabs").hidden = true;
    STEPS.forEach((s, i) => $(s).hidden = i !== STEP_NO[step]);
    if (step === "dns") renderDns();
    window.scrollTo(0, 0);
  }
  function finish(msg) { $("doneMsg").textContent = msg; setup(3); }
  function toDns(msg) { state.doneMsg = msg; $("dnsNote").textContent = msg; if (state.fromSettings) { state.fromSettings = false; view("protView"); } else setup("dns"); }
  $("s1on").onclick = () => { store.set("on", "1"); state.guardOn = true; store.set("done", "1"); setup(2); };
  $("s2skip").onclick = () => toDns("Backfire is on. Scammers will hear a synthetic voice. You can set up your voice later in Protection.");
  $("s2agree").onclick = () => { $("paragraph").textContent = newParagraph(); resetRec(); setup("rec"); };
  $("recSkip").onclick = () => { if (lowQ) { lowQ = false; toDns("Your voice is set up. Backfire is on. It keeps only a short voice sample, used only if you press Scammer Get Scammed. You can delete it any time in Protection."); return; } stopMeter(); if (rec) { discard = true; rec.stop(); } toDns("Backfire is on. Scammers will hear a synthetic voice. You can set up your voice later in Protection."); };
  $("s3done").onclick = () => { view("callView"); applyGuard(); if (BF.pendingStart) { const f = BF.pendingStart; BF.pendingStart = null; f(); } };
  $("voiceSetup").onclick = () => setup(2);
  $("dnsOpen").onclick = () => { state.fromSettings = true; setup("dns"); };
  $("dnsDone").onclick = () => { if (state.fromSettings) { state.fromSettings = false; view("protView"); } else finish(state.doneMsg || "Backfire is on."); };

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
    $("dnsNumber").value = ""; $("dnsLabel").value = ""; renderDns();
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
  function newParagraph() {
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
        $("recStatus").textContent = "Saved, but the recording sounds like phone quality" + (why ? " (" + why + ")" : "") + (above4k != null ? ", " + above4k + "% of the sound above 4 kHz" : "") + ". For a closer match, record again in a quiet room.";
        $("recSkip").hidden = false; $("recSkip").textContent = "Keep this voice and continue"; return;
      }
      toDns("Your voice is set up" + (HUB ? "" : " (simulated)") + (quality === "ok" ? " (recording quality: good)" : "") + ". Backfire is on. It keeps only a short voice sample, used only if you press Scammer Get Scammed. You can delete it any time in Protection.");
    } catch (e) {
      console.log("[backfire] enroll failed", String(e)); done();
      $("recStatus").textContent = /\b401\b/.test(String(e)) ? "Please pair this phone first, then try again." : "Your voice wasn't saved. Press Save to try again, or skip to use a synthetic voice.";   // handled errors stay out of Maria's face; BF.onUnauthorized shows the pair screen itself
    }
  }
  $("recSave").onclick = () => { if (blob) enroll(blob); };
  $("recAgain").onclick = () => { $("paragraph").textContent = newParagraph(); resetRec(); };   // a fresh paragraph each time
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
      tick = setInterval(() => { const s = (Date.now() - t0) / 1000; $("recTime").textContent = mmss(s); if (s >= MIN_S) $("recBtn").disabled = false; if (s >= MAX_S && rec) rec.stop(); }, 250);
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
})();
