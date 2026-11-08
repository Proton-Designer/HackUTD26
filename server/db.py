"""SQLite routing store. Tables: confirmed_scammers, campaign_numbers, trusted, calls."""
import os, sqlite3, threading, time, uuid
DB_PATH = os.environ.get("HUB_DB", os.path.join(os.path.dirname(__file__), "hub.db"))
_lock = threading.RLock()
_conn = None

SCHEMA = """
CREATE TABLE IF NOT EXISTS confirmed_scammers(number TEXT PRIMARY KEY, undo_token TEXT, reason TEXT, ts REAL);
CREATE TABLE IF NOT EXISTS campaign_numbers(number TEXT PRIMARY KEY, campaign_id TEXT, ts REAL);
CREATE TABLE IF NOT EXISTS trusted(number TEXT PRIMARY KEY, label TEXT);
CREATE TABLE IF NOT EXISTS calls(call_id TEXT PRIMARY KEY, from_number TEXT, decision TEXT, reason TEXT, ts REAL);
"""

def conn():
    global _conn
    with _lock:
        if _conn is None:
            _conn = sqlite3.connect(DB_PATH, check_same_thread=False)
            _conn.row_factory = sqlite3.Row
            _conn.executescript(SCHEMA)
        return _conn

def configure(path):
    """Switch DB (tests use ':memory:')."""
    global DB_PATH, _conn
    with _lock:
        if _conn is not None:
            _conn.close()
        _conn = None
        DB_PATH = path

def q(sql, args=()):
    with _lock:
        c = conn(); cur = c.execute(sql, args); c.commit(); return cur

def norm(n):
    n = (n or "").strip().replace(" ", "").replace("-", "").replace("(", "").replace(")", "")
    if n and not n.startswith("+"):
        n = "+1" + n if len(n) == 10 else "+" + n
    return n

def add_confirmed(number, reason="decoy session ended"):
    number = norm(number); token = "undo_" + uuid.uuid4().hex[:10]
    q("INSERT OR REPLACE INTO confirmed_scammers VALUES(?,?,?,?)", (number, token, reason, time.time()))
    return token

def undo(token):
    cur = q("DELETE FROM confirmed_scammers WHERE undo_token=?", (token,))
    return cur.rowcount > 0

def add_campaign(number, campaign_id="camp"):
    q("INSERT OR REPLACE INTO campaign_numbers VALUES(?,?,?)", (norm(number), campaign_id, time.time()))

def add_trusted(number, label=""):
    q("INSERT OR REPLACE INTO trusted VALUES(?,?)", (norm(number), label))

def has(table, number):
    return q(f"SELECT 1 FROM {table} WHERE number=?", (norm(number),)).fetchone() is not None

def list_confirmed():
    return [dict(r) for r in q("SELECT * FROM confirmed_scammers ORDER BY ts DESC").fetchall()]

def reset_all(seed=True):
    for t in ("confirmed_scammers", "campaign_numbers", "trusted", "calls"):
        q(f"DELETE FROM {t}")
    if seed:
        add_trusted("+15555550188", "Her bank (synthetic)")

def log_call(call_id, from_number, decision, reason):
    q("INSERT OR REPLACE INTO calls VALUES(?,?,?,?,?)", (call_id, norm(from_number), decision, reason, time.time()))

def list_calls():
    return [dict(r) for r in q("SELECT * FROM calls ORDER BY ts DESC LIMIT 50").fetchall()]
