// Device pairing (TASK-014). Hub contract: POST /pair {pin} -> {device_token}; protected paths want header x-device-token.
// Fail open: if the hub has no /pair (404) or never answers 401, nothing here ever shows.
(() => {
  "use strict";
  const $ = id => document.getElementById(id), HUB = BF.hub; if (!HUB) return;
  const busy = () => ["ringing", "active"].includes($("phone").dataset.state);
  let want = false;
  // pairing comes first on a fresh phone; onboarding follows after the reload
  function show() { want = false; ["callView", "protView", "setupView"].forEach(v => $(v).hidden = true); $("pairView").hidden = false; $("tabs").hidden = true; $("pairMsg").textContent = ""; $("pairMsg").classList.remove("err");
    $("guard").hidden = true; $("pairBtn").disabled = true;   // nothing is connected yet: no "Live Guard on" badge (UI review bug 3)
    setTimeout(() => $("pairPin").focus(), 50); }
  function request() { want = true; if (!busy()) show(); }          // never interrupt a live call
  BF.onUnauthorized = () => { try { localStorage.removeItem("bf.device"); } catch (e) {} request(); };
  new MutationObserver(() => { if (want && !busy()) show(); }).observe($("phone"), { attributes: true, attributeFilter: ["data-state"] });
  async function pair() {
    const pin = $("pairPin").value.replace(/\D/g, ""); if (pin.length !== 6) return;
    $("pairBtn").disabled = true; $("pairMsg").classList.remove("err"); $("pairMsg").textContent = "Checking…";
    try {
      const r = await fetch(HUB + "/pair", { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify({ pin }) });
      if (!r.ok) throw new Error(String(r.status));
      const j = await r.json(); if (!j.device_token) throw new Error("no token");
      try { localStorage.setItem("bf.device", j.device_token); } catch (e) {}
      location.reload();                                              // restart cleanly with the token (voip token fetch too)
    } catch (e) {
      $("pairMsg").classList.add("err"); $("pairMsg").textContent = String(e.message) === "429" ? "Too many tries. Wait a minute." : "That code did not work. Check it with the Backfire team.";
      $("pairBtn").disabled = false;
    }
  }
  $("pairBtn").onclick = pair; $("pairPin").onkeydown = e => { if (e.key === "Enter") pair(); };
  $("pairPin").oninput = () => { const v = $("pairPin").value.replace(/\D/g, "").slice(0, 6); if ($("pairPin").value !== v) $("pairPin").value = v; $("pairBtn").disabled = v.length !== 6; $("pairMsg").classList.remove("err"); };   // Pair only with all 6 digits (bug 5)
  // first run: no token yet -> probe a protected path; 401 shows the pairing screen, anything else means no pairing needed
  // Every other protected call waits on BF.authReady: it resolves once the probe says no pairing is needed, and never resolves on a 401 (the page reloads after pairing).
  if (!BF.deviceToken()) {
    BF.authReady = new Promise(res => {
      BF.hubFetch("/protection-log", { noWait: true }).then(r => { if (r.status !== 401) res(); }).catch(() => res());
    });
  }
})();
