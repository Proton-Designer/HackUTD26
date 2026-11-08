// Minimal WebRTC signaling server for the demo VoIP app.
// Protocol (JSON over WebSocket):
//   client -> server: {type:"register", id}
//   server -> client: {type:"registered", id} | {type:"users", ids:[...]} | {type:"error", message}
//   relayed (client sets "to", server adds "from"):
//     {type:"offer",  to, callId, sdp}
//     {type:"answer", to, callId, sdp}
//     {type:"ice",    to, callId, sdpMid, sdpMLineIndex, candidate}
//     {type:"reject"|"bye", to, callId}
//
// Backfire (optional, set BACKFIRE_HUB=http://127.0.0.1:8000): this server plays the phone carrier.
//   - Before an offer reaches the callee it asks the hub POST /android/route. BLOCKED_BACKFIRE -> the caller gets
//     {type:"reject", reason:"blocked"} and the callee never rings. Otherwise the offer carries backfire:{decision, reason}.
//   - answer / bye / reject are reported to POST /android/call so the hub emits call.answered / call.ended.
//   - It listens on the hub's WS /events. On user.action=scammer_get_scammed it sends the caller
//     {type:"transfer", callId, to:"decoy"} (the caller's phone silently re-offers to the decoy peer) and the callee
//     {type:"bye", reason:"handoff"}.
//   Fail open: if the hub is down, calls connect as plain calls.
import { WebSocketServer, WebSocket } from "ws";
import os from "node:os";
import http from "node:http";
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const PORT = Number(process.env.PORT || 8090);
const RELAYED = new Set(["offer", "answer", "ice", "reject", "bye"]);
const clients = new Map(); // id -> ws
const HUB = (process.env.BACKFIRE_HUB || "").replace(/\/$/, "");
const HUB_TOKEN = process.env.HUB_TOKEN || "";
const DECOY_ID = process.env.DECOY_ID || "decoy";
const DECOY_SECRET = process.env.DECOY_SECRET || "";
const ROUTE_TIMEOUT_MS = 800;
// callId -> {caller, callee, decision, answered, handedOff}; only calls the hub knows about.
const calls = new Map();

// HTTP on the same port serves the web phone (web/: iPhone or any browser); WebSocket upgrades are signaling.
const WEB = path.join(path.dirname(fileURLToPath(import.meta.url)), "web");
const TYPES = { ".html": "text/html; charset=utf-8", ".json": "application/manifest+json", ".svg": "image/svg+xml" };
const httpServer = http.createServer((req, res) => {
  const name = decodeURIComponent((req.url || "/").split("?")[0]).replace(/^\/+/, "") || "index.html";
  const file = path.join(WEB, path.basename(name));   // flat folder: no path traversal
  fs.readFile(file, (err, body) => {
    if (err) { res.writeHead(404); return res.end("not found"); }
    res.writeHead(200, { "Content-Type": TYPES[path.extname(file)] || "application/octet-stream", "Cache-Control": "no-cache" });
    res.end(body);
  });
});
const wss = new WebSocketServer({ server: httpServer });
httpServer.listen(PORT, "0.0.0.0");

function send(ws, msg) {
  if (ws.readyState === ws.OPEN) ws.send(JSON.stringify(msg));
}
function broadcastUsers() {
  const ids = [...clients.keys()].filter((id) => id !== DECOY_ID); // the decoy can't be called directly
  for (const ws of clients.values()) send(ws, { type: "users", ids });
}

wss.on("connection", (ws, req) => {
  let myId = null;
  console.log(`[conn] ${req.socket.remoteAddress}`);

  ws.on("message", (raw) => {
    let msg;
    try { msg = JSON.parse(raw.toString()); } catch { return send(ws, { type: "error", message: "bad json" }); }

    if (msg.type === "register") {
      const id = String(msg.id || "").trim();
      if (!id) return send(ws, { type: "error", message: "empty id" });
      if (id === DECOY_ID && DECOY_SECRET && msg.secret !== DECOY_SECRET) return send(ws, { type: "error", message: "reserved id" });
      const old = clients.get(id);
      if (old && old !== ws) old.close(4000, "replaced");
      myId = id;
      clients.set(id, ws);
      console.log(`[register] ${id}`);
      send(ws, { type: "registered", id });
      return broadcastUsers();
    }

    if (!myId) return send(ws, { type: "error", message: "register first" });

    if (RELAYED.has(msg.type)) {
      const target = clients.get(msg.to);
      if (!target) {
        // Tell the caller the peer is gone so it can hang up.
        if (msg.type === "offer") send(ws, { type: "bye", from: msg.to, callId: msg.callId, reason: "offline" });
        return;
      }
      const call = calls.get(msg.callId);
      // After a handoff, Maria (the old callee) is out of the call: nothing she sends reaches the scammer.
      if (call && call.handedOff && myId === call.maria) return;
      if (msg.type !== "ice") console.log(`[${msg.type}] ${myId} -> ${msg.to} (${msg.callId})`);
      if (msg.type === "offer" && HUB && !(call && call.handedOff && msg.to === DECOY_ID)) {
        return routeOffer(ws, myId, target, msg);
      }
      send(target, { ...msg, from: myId });
      if (call) trackCall(call, myId, msg);
    }
  });

  ws.on("close", () => {
    if (myId && clients.get(myId) === ws) {
      clients.delete(myId);
      console.log(`[leave] ${myId}`);
      broadcastUsers();
    }
  });
});

// ---------------------------------------------------------------- Backfire carrier role

async function hubPost(path, body, timeoutMs = 1500) {
  const r = await fetch(HUB + path, {
    method: "POST",
    headers: { "Content-Type": "application/json", ...(HUB_TOKEN ? { "x-hub-token": HUB_TOKEN } : {}) },
    body: JSON.stringify(body),
    signal: AbortSignal.timeout(timeoutMs),
  });
  if (!r.ok) throw new Error(`${path} -> HTTP ${r.status}`);
  return r.json();
}
const report = (callId, event, extra = {}) =>
  hubPost("/android/call", { call_id: callId, event, ...extra }).catch((e) => console.warn(`[backfire] report ${event} failed: ${e.message}`));

async function routeOffer(ws, from, target, msg) {
  let d = { decision: "NORMAL", reason: "Hub unreachable, fail open" };
  try {
    d = await hubPost("/android/route", { call_id: msg.callId, from, to: msg.to }, ROUTE_TIMEOUT_MS);
  } catch (e) {
    console.warn(`[backfire] route failed (${e.message}); fail open`);
  }
  console.log(`[route] ${from} -> ${msg.to} (${msg.callId}): ${d.decision} (${d.reason})`);
  if (d.decision === "BLOCKED_BACKFIRE") {
    return send(ws, { type: "reject", from: msg.to, callId: msg.callId, reason: "blocked" }); // never rings
  }
  calls.set(msg.callId, { caller: from, maria: msg.to, decision: d.decision, answered: false, handedOff: false });
  send(target, { ...msg, from, backfire: { decision: d.decision, reason: d.reason } });
}

function trackCall(call, from, msg) {
  const id = msg.callId;
  if (msg.type === "answer") {
    if (from === DECOY_ID) report(id, "answered", { by: "decoy" });
    else if (from === call.maria && !call.answered) { call.answered = true; report(id, "answered", { by: "maria" }); }
  } else if (msg.type === "bye" || msg.type === "reject") {
    const endedBy = from === call.caller ? "caller"
      : from === DECOY_ID || msg.reason === "decoy_done" || (call.phoneDecoy && from === call.maria) ? "decoy" : "maria";
    calls.delete(id);
    report(id, "ended", { ended_by: endedBy });
  }
}

function handoff(callId) {
  const call = calls.get(callId);
  if (!call || call.handedOff || !call.answered) return;
  const caller = clients.get(call.caller), maria = clients.get(call.maria);
  if (!clients.get(DECOY_ID)) {
    console.warn(`[handoff] ${callId}: decoy peer is offline; leaving the call as is`);
    if (maria) send(maria, { type: "backfire", callId, status: "decoy_offline" });
    return;
  }
  if (!caller) return;
  call.handedOff = true;
  console.log(`[handoff] ${callId}: ${call.caller} now talks to ${DECOY_ID}; ${call.maria} leaves`);
  // The caller's phone keeps showing Maria's name; it just renegotiates with the decoy.
  send(caller, { type: "transfer", from: call.maria, callId, to: DECOY_ID });
  if (maria) send(maria, { type: "bye", from: call.caller, callId, reason: "handoff" });
  report(callId, "handoff");
}

function hangUp(callId) {
  const call = calls.get(callId);
  if (!call || call.handedOff) return;
  console.log(`[hang_up] ${callId}: ending the call for ${call.maria}`);
  calls.delete(callId);
  const caller = clients.get(call.caller), maria = clients.get(call.maria);
  if (caller) send(caller, { type: "bye", from: call.maria, callId, reason: "remote_hangup" });
  if (maria) send(maria, { type: "bye", from: call.caller, callId, reason: "backfire_hangup" });
  report(callId, "ended", { ended_by: "maria" });
}

function watchHub() {
  const url = HUB.replace(/^http/, "ws") + "/events" + (HUB_TOKEN ? `?token=${encodeURIComponent(HUB_TOKEN)}` : "");
  const hub = new WebSocket(url);
  hub.on("open", () => console.log(`[backfire] watching ${HUB}/events`));
  hub.on("message", (raw) => {
    let ev;
    try { ev = JSON.parse(raw.toString()); } catch { return; }
    if (ev.type !== "user.action" || !ev.data) return;
    if (ev.data.action === "scammer_get_scammed") {
      if (ev.data.by === "phone") { const c = calls.get(ev.call_id); if (c) c.phoneDecoy = true; } // decoy runs on Maria's phone
      else handoff(ev.call_id);
    }
    else if (ev.data.action === "hang_up") hangUp(ev.call_id); // Backfire runs in its own app, so the network ends the call
  });
  hub.on("close", () => setTimeout(watchHub, 2000));
  hub.on("error", () => {}); // close follows; retry
}
if (HUB) watchHub();

// Keep connections alive through Wi-Fi/NAT idle timeouts.
setInterval(() => { for (const ws of wss.clients) ws.ping(); }, 20000);

const addrs = Object.values(os.networkInterfaces()).flat()
  .filter((a) => a && a.family === "IPv4" && !a.internal).map((a) => a.address);
console.log(`Signaling server listening on port ${PORT}`);
console.log(HUB ? `Backfire carrier mode: hub ${HUB}` : "Backfire off (set BACKFIRE_HUB=http://127.0.0.1:8000 to enable)");
for (const a of addrs) console.log(`  ws://${a}:${PORT}   (web phone: http://${a}:${PORT}/ ; iPhone needs an https URL, see README)`);
