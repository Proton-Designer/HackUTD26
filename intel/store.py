"""SQLite intel store: campaigns, indicators, sightings, actions, blocklist.

Table ownership with P1 must be agreed with Ayman: P1's /routing/lookup can call
`is_blocked(number)` (or GET /intel/blocked) instead of reading tables directly.
"""
from __future__ import annotations

import json
import os
import sqlite3
import threading
import time
import uuid
from pathlib import Path

from .lookups import norm_phone

SCHEMA = """
CREATE TABLE IF NOT EXISTS campaigns(id TEXT PRIMARY KEY, scam_type TEXT, impersonated_org TEXT,
  status TEXT, script_tags TEXT, stages TEXT, conflict INTEGER DEFAULT 0, created REAL, updated REAL);
CREATE TABLE IF NOT EXISTS indicators(type TEXT, value TEXT, campaign_id TEXT, strong INTEGER,
  first_call TEXT, created REAL, PRIMARY KEY(type, value));
CREATE TABLE IF NOT EXISTS sightings(id INTEGER PRIMARY KEY AUTOINCREMENT, campaign_id TEXT, call_id TEXT,
  calling_number TEXT, carrier TEXT, day TEXT, created REAL);
CREATE TABLE IF NOT EXISTS actions(id TEXT PRIMARY KEY, call_id TEXT, campaign_id TEXT, kind TEXT, scope TEXT,
  target TEXT, status TEXT, approval TEXT, simulated INTEGER, evidence TEXT, payload TEXT, created REAL, updated REAL);
CREATE TABLE IF NOT EXISTS blocklist(undo_token TEXT PRIMARY KEY, number TEXT, scope TEXT, campaign_id TEXT,
  reason TEXT, active INTEGER, created REAL);
CREATE TABLE IF NOT EXISTS callback_warnings(number TEXT PRIMARY KEY, campaign_id TEXT, created REAL);
CREATE TABLE IF NOT EXISTS denied(id INTEGER PRIMARY KEY AUTOINCREMENT, call_id TEXT, kind TEXT, target TEXT,
  reason TEXT, created REAL);
CREATE TABLE IF NOT EXISTS holds(undo_token TEXT PRIMARY KEY, action_id TEXT, call_id TEXT, transfer_id TEXT,
  amount INTEGER, destination TEXT, active INTEGER, created REAL);
"""

BLOCK_REASON = {"her": "Confirmed scammer (blocked for this customer)",
                "campaign": "Linked to a confirmed scam campaign",
                "network": "Network-wide block (analyst approved, simulated)"}


class Store:
    def __init__(self, path: str | None = None):
        self.path = path or os.getenv("INTEL_DB", str(Path(__file__).with_name("intel.db")))
        self.db = sqlite3.connect(self.path, check_same_thread=False)
        self.db.row_factory = sqlite3.Row
        self.lock = threading.Lock()
        self.db.executescript(SCHEMA)

    def q(self, sql: str, *a) -> list[dict]:
        with self.lock:
            return [dict(r) for r in self.db.execute(sql, a).fetchall()]

    def x(self, sql: str, *a) -> None:
        with self.lock:
            self.db.execute(sql, a)
            self.db.commit()

    # ---- blocklist ----
    def add_block(self, number: str, scope: str, reason: str | None = None, campaign_id: str | None = None) -> tuple[str, bool]:
        """Returns (undo_token, created_new)."""
        n = norm_phone(number)
        row = self.q("SELECT undo_token FROM blocklist WHERE number=? AND scope=? AND active=1", n, scope)
        if row:
            return row[0]["undo_token"], False
        tok = "undo-" + uuid.uuid4().hex[:10]
        self.x("INSERT INTO blocklist VALUES(?,?,?,?,?,1,?)", tok, n, scope, campaign_id,
               reason or BLOCK_REASON.get(scope, scope), time.time())
        return tok, True

    def undo(self, token: str) -> dict | None:
        row = self.q("SELECT * FROM blocklist WHERE undo_token=? AND active=1", token)
        if not row:
            return None
        self.x("UPDATE blocklist SET active=0 WHERE undo_token=?", token)
        # F16 (#93): the customer's undo must make the number ring again, so lift the campaign and network blocks on
        # that same number too (routing checks every scope). Demo = one customer; production would add a per-customer
        # exception instead of lifting blocks that protect others.
        also = self.q("SELECT * FROM blocklist WHERE number=? AND active=1", row[0]["number"])
        if also:
            self.x("UPDATE blocklist SET active=0 WHERE number=? AND active=1", row[0]["number"])
        return {**row[0], "also_undone": also}

    # ---- Nessie transfer holds (mock bank) ----
    def add_hold(self, action_id: str, call_id: str, transfer_id: str, amount, destination: str) -> str:
        tok = "hold-" + uuid.uuid4().hex[:10]
        self.x("INSERT INTO holds VALUES(?,?,?,?,?,?,1,?)", tok, action_id, call_id, transfer_id, amount, destination,
               time.time())
        return tok

    def undo_hold(self, token: str) -> dict | None:
        row = self.q("SELECT * FROM holds WHERE undo_token=? AND active=1", token)
        if not row:
            return None
        self.x("UPDATE holds SET active=0 WHERE undo_token=?", token)
        return row[0]

    def is_blocked(self, number: str) -> tuple[bool, str | None]:
        rows = self.q("SELECT scope, reason FROM blocklist WHERE number=? AND active=1", norm_phone(number))
        if not rows:
            return False, None
        order = {"her": 0, "campaign": 1, "network": 2}
        rows.sort(key=lambda r: order.get(r["scope"], 9))
        return True, rows[0]["reason"]

    def add_callback_warning(self, number: str, campaign_id: str | None) -> bool:
        n = norm_phone(number)
        if self.q("SELECT 1 FROM callback_warnings WHERE number=?", n):
            return False
        self.x("INSERT INTO callback_warnings VALUES(?,?,?)", n, campaign_id, time.time())
        return True

    # ---- actions / denied ----
    def add_action(self, a: dict) -> None:
        now = time.time()
        self.x("INSERT INTO actions VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?)", a["id"], a.get("call_id"), a.get("campaign_id"),
               a["kind"], a["scope"], a.get("target"), a["status"], a.get("approval"), int(a.get("simulated", True)),
               json.dumps(a.get("evidence", [])), json.dumps(a.get("payload")), now, now)

    def set_action(self, action_id: str, status: str, approval: str) -> None:
        self.x("UPDATE actions SET status=?, approval=?, updated=? WHERE id=?", status, approval, time.time(), action_id)

    def get_action(self, action_id: str) -> dict | None:
        r = self.q("SELECT * FROM actions WHERE id=?", action_id)
        return _decode(r[0]) if r else None

    def actions(self, status: str | None = None) -> list[dict]:
        rows = self.q("SELECT * FROM actions WHERE status=? ORDER BY created", status) if status \
            else self.q("SELECT * FROM actions ORDER BY created")
        return [_decode(r) for r in rows]

    def add_denied(self, call_id, kind, target, reason) -> None:
        self.x("INSERT INTO denied(call_id,kind,target,reason,created) VALUES(?,?,?,?,?)",
               call_id, kind, target, reason, time.time())

    def immunity(self) -> int:
        """Numbers/indicators now blocked or warned for every Backfire user."""
        b = self.q("SELECT COUNT(*) c FROM blocklist WHERE active=1 AND scope IN ('campaign','network')")[0]["c"]
        w = self.q("SELECT COUNT(*) c FROM callback_warnings")[0]["c"]
        n = self.q("SELECT COUNT(*) c FROM actions WHERE status='simulated: applied' AND kind!='network_number_block'")[0]["c"]
        return b + w + n

    def state(self) -> dict:
        camps = self.q("SELECT * FROM campaigns ORDER BY created")
        for c in camps:
            c["script_tags"], c["stages"] = json.loads(c["script_tags"] or "[]"), json.loads(c["stages"] or "[]")
            c["sightings"] = self.q("SELECT COUNT(*) c FROM sightings WHERE campaign_id=?", c["id"])[0]["c"]
            c["indicators"] = self.q("SELECT type, value FROM indicators WHERE campaign_id=?", c["id"])
        return {"campaigns": camps, "queue": self.actions("pending_approval"), "actions": self.actions(),
                "denied": self.q("SELECT * FROM denied ORDER BY id"),
                "blocklist": self.q("SELECT * FROM blocklist WHERE active=1"),
                "callback_warnings": self.q("SELECT * FROM callback_warnings"),
                "holds": self.q("SELECT * FROM holds WHERE active=1"), "immunity": self.immunity()}


def _decode(r: dict) -> dict:
    r["evidence"], r["payload"], r["simulated"] = json.loads(r["evidence"] or "[]"), json.loads(r["payload"] or "null"), bool(r["simulated"])
    return r


_default: Store | None = None


def default_store() -> Store:
    global _default
    if _default is None:
        _default = Store()
    return _default


def is_blocked(number: str, store: Store | None = None) -> tuple[bool, str | None]:
    """For P1's pre-ring /routing/lookup: (blocked?, reason)."""
    return (store or default_store()).is_blocked(number)
