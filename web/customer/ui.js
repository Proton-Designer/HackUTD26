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
    const r = await fetch(HUB + path, { method, headers: { "Content-Type": "application/json" }, body: body ? JSON.stringify(body) : undefined });
    if (!r.ok) throw new Error(method + " " + path + " " + r.status);
    return r.json();
  }

  // ---- guard badge ----
  function applyGuard() { const b = $("guard"); b.textContent = state.guardOn ? "🛡 Live Guard on" : "Live Guard off"; b.classList.toggle("off", !state.guardOn); }

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
    $("callsCount").textContent = state.calls;
    $("guardState").textContent = state.guardOn ? "On. Backfire is watching the caller's side of calls from numbers it doesn't know." : "Off. Calls are not being checked.";
    $("guardToggle").textContent = state.guardOn ? "Turn Live Guard off" : "Turn Live Guard on";
    $("voiceState").textContent = state.voiceId ? "Saved. Used only if you press Scammer Get Scammed." + (HUB ? "" : " (Simulated)") : "No voice profile.";
    $("voiceDelete").hidden = !state.voiceId; $("voiceSetup").hidden = !!state.voiceId;
    applyGuard();
  }
  async function undo(b) {
    try { if (HUB) await hub("POST", "/protection-log/undo", { undo_token: b.undo_token }); }
    catch (e) { console.log("[backfire] undo failed", String(e)); return; }   // keep the row if the hub refused
    state.blocked = state.blocked.filter(x => x !== b); renderProtection();
  }
  $("guardToggle").onclick = () => { state.guardOn = !state.guardOn; store.set("on", state.guardOn ? "1" : "0"); renderProtection(); };

  // events from the hub / replay
  BF.onEvent = ev => {
    const d = ev.data || {};
    if (ev.type === "blocklist.updated" && d.scope === "her" && !state.blocked.some(b => b.undo_token === d.undo_token))
      state.blocked.push({ number: d.number, reason: "Caught after Scammer Get Scammed", undo_token: d.undo_token });
    if (ev.type === "call.ended") state.calls++;
    if (ev.type === "voice.enrolled") { state.voiceId = d.voice_id; store.set("voice", d.voice_id); }
    if (ev.type === "voice.deleted") { state.voiceId = null; store.set("voice", null); }
  };

  // ---- voice delete ----
  async function deleteVoice() {
    try { if (HUB && state.voiceId) await hub("DELETE", "/voice/" + encodeURIComponent(state.voiceId)); }
    catch (e) { console.log("[backfire] voice delete failed", String(e)); $("voiceState").textContent = "Could not delete right now. Try again."; return; }
    state.voiceId = null; store.set("voice", null); renderProtection();
  }
  $("voiceDelete").onclick = deleteVoice;
  $("voiceSetup").onclick = () => { setup(2); };

  // ---- onboarding ----
  function setup(step) {
    VIEWS.forEach(x => $(x).hidden = x !== "setupView"); $("tabs").hidden = true;
    ["step1", "step2", "step3"].forEach((s, i) => $(s).hidden = i + 1 !== step);
  }
  function finish(msg) { $("doneMsg").textContent = msg; setup(3); }
  $("s1on").onclick = () => { store.set("on", "1"); state.guardOn = true; store.set("done", "1"); setup(2); };
  $("s2skip").onclick = () => finish("Backfire is on. You can set up your voice later in Protection.");
  $("s3done").onclick = () => { view("callView"); applyGuard(); if (BF.pendingStart) { const f = BF.pendingStart; BF.pendingStart = null; f(); } };

  const SENTENCES = ["The little blue boat drifted past the old stone bridge.", "My neighbor grows tomatoes and sweet peas by the garden gate.", "On Sunday we walked to the market and bought warm bread.", "The clock in the hall strikes every hour, loud and clear.", "A gentle rain fell on the quiet street all morning."];
  function newParagraph() {
    const pick = [...SENTENCES].sort(() => Math.random() - 0.5).slice(0, 3);
    const digits = Array.from({ length: 4 }, () => Math.floor(Math.random() * 10)).join(" ");
    return pick.join(" ") + " Today's code word is " + digits + ".";
  }
  $("consent").onchange = e => {
    $("recordBox").hidden = !e.target.checked;
    if (e.target.checked) $("paragraph").textContent = newParagraph();
  };

  let rec = null, chunks = [];
  const b64 = blob => new Promise(res => { const r = new FileReader(); r.onload = () => res(String(r.result).split(",")[1] || ""); r.readAsDataURL(blob); });
  async function enroll(blob) {
    $("recStatus").textContent = "Saving…";
    try {
      let voice_id;
      if (HUB) voice_id = (await hub("POST", "/voice/enroll", { recording: await b64(blob), consent_version: CONSENT_VERSION })).voice_id;
      else voice_id = "v_simulated_" + Math.random().toString(36).slice(2, 8);   // no hub configured: simulated
      state.voiceId = voice_id; store.set("voice", voice_id);
      finish("Your voice is saved" + (HUB ? "" : " (simulated)") + ". Backfire is on. You can delete your voice any time in Protection.");
    } catch (e) { console.log("[backfire] enroll failed", String(e)); $("recStatus").textContent = "That didn't save. Press the red button to try again."; $("recBtn").textContent = "● Start recording"; rec = null; }
  }
  $("recBtn").onclick = async () => {
    if (rec) { rec.stop(); return; }                       // second press = stop
    if (!$("consent").checked) return;
    try {
      if (!navigator.mediaDevices) throw new Error("no mic API");
      const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
      chunks = []; rec = new MediaRecorder(stream);
      rec.ondataavailable = e => chunks.push(e.data);
      rec.onstop = () => { stream.getTracks().forEach(t => t.stop()); const blob = new Blob(chunks, { type: rec.mimeType || "audio/webm" }); rec = null; $("recBtn").textContent = "● Start recording"; enroll(blob); };
      rec.start(); $("recBtn").textContent = "■ Stop when finished"; $("recStatus").textContent = "Recording… read the words above.";
    } catch (e) {
      $("recStatus").textContent = "We couldn't use the microphone. Allow it in your browser and try again.";
      if (qs.has("fakemic")) enroll(new Blob(["x"], { type: "audio/webm" }));   // test hook only
    }
  };

  // ---- boot ----
  applyGuard();
  if (!store.get("done") && !qs.has("skipsetup")) setup(1); else view("callView");
  BF.setup = setup; BF.view = view; BF._enroll = enroll;
})();
