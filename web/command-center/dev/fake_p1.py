"""Stand-in for P1's server, only for testing the command center's live mode. Python stdlib only.

  python web/command-center/dev/fake_p1.py                 # port 8765, sends a short built-in call
  python web/command-center/dev/fake_p1.py --events mock/events.json --port 8765
  then open  .../web/command-center/?server=http://localhost:8765

- WS  /events                         broadcasts contract envelopes {type, call_id, ts, data}
- POST /intel/actions/{id}/approve    replies 200 and broadcasts intel.action status=approved
- POST /publish (or /events)          broadcasts the posted envelope, so P4a's intel/lookups.py can
                                      push real lookups here: BACKFIRE_EVENTS_URL=http://localhost:8765/publish
P1's real server replaces all of this; nothing here is on the demo path.
"""
import argparse
import base64
import hashlib
import json
import re
import struct
import threading
import time
import urllib.parse
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

GUID = "258EAFA5-E914-47DA-95CA-C5AB0DC85B11"
clients: set = set()
lock = threading.Lock()
first_client = threading.Event()


def frame(text: str) -> bytes:
    data = text.encode()
    n = len(data)
    if n < 126:
        head = struct.pack("!BB", 0x81, n)
    elif n < 65536:
        head = struct.pack("!BBH", 0x81, 126, n)
    else:
        head = struct.pack("!BBQ", 0x81, 127, n)
    return head + data


def broadcast(ev: dict) -> None:
    f = frame(json.dumps(ev))
    with lock:
        for s in list(clients):
            try:
                s.sendall(f)
            except OSError:
                clients.discard(s)
    print("->", ev.get("type"), flush=True)


def env(type_: str, call_id, data: dict) -> dict:
    return {"type": type_, "call_id": call_id, "ts": time.time(), "data": data}


def builtin_events() -> list:
    c, scammer = "call-live-test", "+12145550123"
    return [
        env("call.incoming", c, {"from": scammer, "to": "+14695550188", "attestation": "C", "scam_id_score": 0.6}),
        env("call.routed", c, {"decision": "LIVE_GUARD", "reason": "Unknown caller: ring with Live Guard on"}),
        env("call.answered", c, {}),
        env("transcript.caller", c, {"utterance_id": "u1", "text": "This is the IRS. You owe back taxes.", "is_final": True}),
        env("risk.update", c, {"s": 0.91, "band": "high", "asks": ["gift_card"], "scam_type": "government_impersonation",
                               "stage": "ask", "impersonates": "IRS", "addresses_ai_system": False,
                               "why_chips": ["Claims to be the IRS", "Asks for gift cards"], "engine": "local"}),
        env("artifacts.extracted", c, {"artifacts": [{"type": "domain", "value": "example.com"},
                                                     {"type": "callback_phone", "value": "+12145550147"}]}),
        env("intel.action", c, {"action_id": "act-live-1", "kind": "network_block", "label": "Block calling number network-wide",
                                "target": scammer, "scope": "all_customers", "approval": "analyst", "status": "queued",
                                "simulated": True, "expiry": "30 days"}),
    ]


class Handler(BaseHTTPRequestHandler):
    protocol_version = "HTTP/1.1"

    def log_message(self, *args):
        pass

    def _reply(self, code: int, body: bytes = b"", ctype: str = "application/json"):
        self.send_response(code)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "content-type")
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        if body:
            self.wfile.write(body)

    def do_OPTIONS(self):
        self._reply(204)

    def do_GET(self):
        path = self.path.split("?")[0]
        if path == "/events" and self.headers.get("Upgrade", "").lower() == "websocket":
            key = self.headers["Sec-WebSocket-Key"]
            accept = base64.b64encode(hashlib.sha1((key + GUID).encode()).digest()).decode()
            self.send_response(101)
            self.send_header("Upgrade", "websocket")
            self.send_header("Connection", "Upgrade")
            self.send_header("Sec-WebSocket-Accept", accept)
            self.end_headers()
            self.wfile.flush()
            sock = self.connection
            with lock:
                clients.add(sock)
            first_client.set()
            print("client connected", flush=True)
            try:
                while sock.recv(1024):
                    pass  # client frames are ignored; recv returns b"" on close
            except OSError:
                pass
            with lock:
                clients.discard(sock)
            self.close_connection = True
            return
        self._reply(200 if path == "/health" else 404, b'{"ok": true}' if path == "/health" else b"")

    def do_POST(self):
        path = self.path.split("?")[0]
        n = int(self.headers.get("Content-Length") or 0)
        raw = self.rfile.read(n) if n else b""
        m = re.fullmatch(r"/intel/actions/([^/]+)/approve", path)
        if m:
            aid = urllib.parse.unquote(m.group(1))
            self._reply(200, json.dumps({"ok": True, "action_id": aid, "status": "approved"}).encode())
            broadcast(env("intel.action", None, {"action_id": aid, "status": "approved", "approval": "analyst", "simulated": True}))
            return
        if path in ("/publish", "/events", "/events/publish"):
            try:
                ev = json.loads(raw or b"{}")
            except ValueError:
                self._reply(400)
                return
            for e in ev if isinstance(ev, list) else [ev]:
                broadcast(e)
            self._reply(200, b'{"ok": true}')
            return
        self._reply(404)


def play(events: list, max_gap: float) -> None:
    first_client.wait()
    time.sleep(1.0)
    prev = None
    for ev in events:
        ts = ev.get("ts")
        try:
            t = float(ts) if not isinstance(ts, str) else time.mktime(time.strptime(ts[:19], "%Y-%m-%dT%H:%M:%S"))
        except (TypeError, ValueError):
            t = None
        gap = 1.0 if t is None or prev is None else max(0.0, min(max_gap, t - prev))
        prev = t if t is not None else prev
        time.sleep(gap)
        broadcast({**ev, "ts": time.time()})


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--port", type=int, default=8765)
    ap.add_argument("--events", help="JSON file: a list of envelopes or {events: [...]}")
    ap.add_argument("--gap", type=float, default=2.0, help="max seconds between replayed events")
    a = ap.parse_args()
    if a.events:
        data = json.loads(Path(a.events).read_text(encoding="utf-8"))
        events = data["events"] if isinstance(data, dict) else data
    else:
        events = builtin_events()
    threading.Thread(target=play, args=(events, a.gap), daemon=True).start()
    srv = ThreadingHTTPServer(("127.0.0.1", a.port), Handler)
    srv.daemon_threads = True
    print(f"fake P1 on http://localhost:{a.port}  (WS /events, {len(events)} events queued)", flush=True)
    srv.serve_forever()


if __name__ == "__main__":
    main()
