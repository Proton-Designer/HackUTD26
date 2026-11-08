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
  $("answerBtn").addEventListener("click", () => { tapped = true; if (!t0) tapT = setTimeout(() => { t0 = t0 || Date.now(); start(); }, 1500); setTimeout(start, 0); });   // no call.answered within 1.5 s: sync to the tap
  ["declineBtn", "endBtn", "btnHang"].forEach(id => $(id).addEventListener("click", stop));
  const prev = BF.onEvent;
  BF.onEvent = ev => {
    if (prev) prev(ev);
    switch (ev && ev.type) {
      case "call.incoming": stop(); break;
      case "call.answered":
        if (!BF.sim) break;
        t0 = Date.parse(ev.ts) || Date.now();
        if ($("phone").dataset.state === "ringing") $("answerBtn").click();   // no SIP leg to answer: the sim answers for Maria
        else start();
        break;
      case "handoff.started": held = true; if (a) a.pause(); break;
      case "handoff.restored": held = false; play(); break;
      case "call.ended": stop(); break;
    }
  };
})();
