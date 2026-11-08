// Device pairing (TASK-014). Hub contract: POST /pair {pin} -> {device_token}; protected paths want header x-device-token.
// A pairing link /app/#pair=XXXXXX pairs by itself. The code rides in the URL FRAGMENT, which browsers never send to a server (no hub/Cloudflare
// access log, no Referer); it is stripped from the address bar first (history.replaceState), then POST /pair, then reload.
// The 6-digit box is the fallback. Fail open: if the hub has no /pair (404) or never answers 401, nothing here ever shows.
(() => {
  "use strict";
  const $ = id => document.getElementById(id), HUB = BF.hub; if (!HUB) return;
  const busy = () => ["ringing", "active"].includes($("phone").dataset.state);
  let want = false, note = "";
  // pairing comes first on a fresh phone; onboarding follows after the reload
  function show() { want = false; ["callView", "protView", "setupView"].forEach(v => $(v).hidden = true); $("pairView").hidden = false; $("tabs").hidden = true;
    $("pairMsg").textContent = note; $("pairMsg").classList.toggle("err", !!note);
    $("guard").hidden = true; $("pairBtn").disabled = true;   // nothing is connected yet: no "Live Guard on" badge (UI review bug 3)
    { const a = $("a2hs"); if (a) a.hidden = true; }           // one ask at a time: no install banner over the pairing screen (UI review 2)
    setTimeout(() => $("pairPin").focus(), 50); }
  function request() { want = true; if (!busy()) show(); }          // never interrupt a live call
  BF.onUnauthorized = () => { try { localStorage.removeItem("bf.device"); } catch (e) {} request(); };
  new MutationObserver(() => { if (want && !busy()) show(); }).observe($("phone"), { attributes: true, attributeFilter: ["data-state"] });
  async function post(pin) {
    const r = await fetch(HUB + "/pair", { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify({ pin }) });
    if (!r.ok) throw new Error(String(r.status));
    const j = await r.json(); if (!j.device_token) throw new Error("no token");
    try { localStorage.setItem("bf.device", j.device_token); } catch (e) {}
  }
  async function pair() {
    const pin = $("pairPin").value.replace(/\D/g, ""); if (pin.length !== 6) return;
    $("pairBtn").disabled = true; $("pairMsg").classList.remove("err"); $("pairMsg").textContent = "Connecting…";
    try { await post(pin); location.reload(); }                     // restart cleanly with the token (voip token fetch too)
    catch (e) {
      $("pairPin").value = ""; $("pairMsg").classList.add("err"); $("pairMsg").textContent = String(e.message) === "429" ? "Too many tries. Wait a minute." : "That code did not work. Check it and try again.";
      $("pairBtn").disabled = false;
    }
  }
  $("pairBtn").onclick = pair; $("pairPin").onkeydown = e => { if (e.key === "Enter") pair(); };
  $("pairPin").oninput = () => { const v = $("pairPin").value.replace(/\D/g, "").slice(0, 6); if ($("pairPin").value !== v) $("pairPin").value = v; $("pairBtn").disabled = v.length !== 6; $("pairMsg").classList.remove("err"); };   // Connect only with all 6 digits (bug 5)

  // First run: no token yet -> probe a protected path; 401 shows the pairing screen, anything else means no pairing needed.
  // Every other protected call waits on BF.authReady: it resolves once the probe says no pairing is needed, and never resolves on a 401 (the page reloads after pairing).
  function probe() {
    if (BF.deviceToken()) return Promise.resolve();
    return new Promise(res => { BF.hubFetch("/protection-log", { noWait: true }).then(r => { if (r.status !== 401) res(); }).catch(() => res()); });
  }
  // Pairing link: the code never stays in the address bar, history or a bookmark. Strip it before anything else (and before the reload).
  // Fragment only. A ?pair= query (already sent to the server, so already in its logs) is never used, only removed from the address bar.
  const hs = new URLSearchParams(location.hash.replace(/^#/, "")), qs = new URLSearchParams(location.search), linkPin = (hs.get("pair") || "").replace(/\D/g, "");
  if (hs.has("pair") || qs.has("pair")) {
    hs.delete("pair"); qs.delete("pair"); const q = qs.toString(), h = hs.toString();
    try { history.replaceState(history.state, "", location.pathname + (q ? "?" + q : "") + (h ? "#" + h : "")); } catch (e) {}
  }
  if (linkPin.length === 6) {
    let views = null;   // "Connecting your phone..." while the link pairs (after every script has set its first view)
    const connecting = setTimeout(() => { views = ["callView", "protView", "setupView"].filter(v => !$(v).hidden); views.forEach(v => $(v).hidden = true); $("tabs").hidden = true;
      $("pairView").hidden = false; $("pairView").classList.add("linking"); $("pairMsg").classList.remove("err"); $("pairMsg").textContent = "Connecting your phone…"; { const a = $("a2hs"); if (a) a.hidden = true; } }, 0);
    BF.authReady = new Promise(res => {
      post(linkPin).then(() => location.reload())                   // the URL is already clean, so the reload cannot pair twice
        .catch(e => {
          clearTimeout(connecting); $("pairView").classList.remove("linking"); $("pairMsg").textContent = "";
          note = String(e.message) === "429" ? "Too many tries. Wait a minute, then type your code." : "That link did not work. Type the 6-digit code instead.";
          probe().then(() => { if (!want && $("pairView").hidden === false && views) { $("pairView").hidden = true; views.forEach(v => $(v).hidden = false); if (views.includes("callView")) $("tabs").hidden = false; } res(); });   // hub needs no pairing: back to the app
        });
    });
  } else if (!BF.deviceToken()) BF.authReady = probe();
  // UI review 3 (H): a #pair= link opened in a tab that already shows the app only changes the hash: reload so the normal path pairs
  window.addEventListener("hashchange", () => { if (/[#&]pair=\d{6}/.test(location.hash)) location.reload(); });
})();
