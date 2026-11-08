"""Evaluation harness: cloud vs local vs rules-only on the synthetic scam-call scripts.

    .venv/bin/python -m detection.eval.run_eval --engine cloud --split dev
    .venv/bin/python -m detection.eval.run_eval --engine local --split dev
    .venv/bin/python -m detection.eval.run_eval --engine rules --split dev
    .venv/bin/python -m detection.eval.run_eval --freeze            # tune thresholds on dev ONLY -> FROZEN.json
    .venv/bin/python -m detection.eval.run_eval --engine all --split test
    .venv/bin/python -m detection.eval.run_eval --report            # writes RESULTS.md from results/*.jsonl

Each script is replayed line by line (caller lines only, cumulative window of the last WINDOW_LINES lines),
exactly like the live path: window text -> detect(engine) -> s. The per-line scores are cached on disk and
stored in results/<engine>-<split>.jsonl, so threshold sweeps and reports need no model calls.
All data is synthetic. Tuning uses split=dev only; the test split is scored at the frozen threshold.
"""
from __future__ import annotations

import argparse
import asyncio
import hashlib
import json
import math
import os
import pathlib
import subprocess
import time
from collections import defaultdict

ROOT = pathlib.Path(__file__).resolve().parents[2]
EVAL_DIR = pathlib.Path(__file__).resolve().parent
RESULTS_DIR = EVAL_DIR / "results"
CACHE_DIR = EVAL_DIR / ".cache"
FROZEN = EVAL_DIR / "FROZEN.json"
HELDOUT_V2 = EVAL_DIR / "heldout_v2.jsonl"
ROW_FILES = [ROOT / "data" / "eval" / "scripts.jsonl", EVAL_DIR / "extra_rows.jsonl"]

ASKS = {"otp", "card", "ssn", "gift_card", "crypto", "wire", "p2p", "remote_app", "secrecy"}
HARD_ASKS = ASKS - {"secrecy"}
REQ = {"id", "split", "label", "scam_type", "caller_lines", "expected_asks", "expected_alert"}
WINDOW_LINES = 5          # live window ~ last few caller lines
SECONDS_PER_LINE = 3.0    # assumed speech time per caller line
THRESHOLDS = [round(0.30 + 0.05 * i, 2) for i in range(0, 14)]  # 0.30 .. 0.95
DEFAULT_THRESHOLD = 0.80  # "high" band start
MAX_RPM = {"cloud": int(os.environ.get("EVAL_CLOUD_RPM", "8"))}  # team NVIDIA key cap (lead, 2026-11-08: eval <=8 rpm)
ENGINES = ("rules", "prodrules", "cloud", "local")  # rules = plain keyword baseline; prodrules = production detect.quick (rule_scan + merge), what runs live when the LLM fails


# ---------------------------------------------------------------- data
def validate_row(r: dict) -> list[str]:
    """Same rules as data/eval/validate.py."""
    errs = []
    miss = REQ - r.keys()
    if miss:
        errs.append(f"missing {sorted(miss)}")
    if r.get("split") not in {"dev", "test"}:
        errs.append("bad split")
    if r.get("label") not in {"scam", "legit", "adversarial"}:
        errs.append("bad label")
    if not isinstance(r.get("caller_lines"), list) or not r.get("caller_lines"):
        errs.append("caller_lines empty")
    bad = set(r.get("expected_asks", [])) - ASKS
    if bad:
        errs.append(f"unknown asks {sorted(bad)}")
    if not isinstance(r.get("expected_alert"), bool):
        errs.append("expected_alert not bool")
    return errs


def load_rows(paths=None, split: str | None = None) -> list[dict]:
    rows, ids = [], set()
    for p in paths or ROW_FILES:
        p = pathlib.Path(p)
        if not p.exists():
            continue
        for n, line in enumerate(p.read_text().splitlines(), 1):
            if not line.strip():
                continue
            r = json.loads(line)
            errs = validate_row(r)
            if r.get("id") in ids:
                errs.append("duplicate id")
            if errs:
                raise ValueError(f"{p.name}:{n}: {'; '.join(errs)}")
            ids.add(r["id"])
            rows.append(r)
    return [r for r in rows if split in (None, "all") or r["split"] == split]


# ---------------------------------------------------------------- rules-only baseline
# Deliberately simple keyword rules: what a non-LLM filter would do. Separate from detect.py's backstop.
import re  # noqa: E402

_RULES = {
    "otp": r"\b(verification|security|six[- ]digit|one[- ]time|6[- ]digit)?\s*(code|passcode)\b.*\b(read|tell|give|say|send)\b|\b(read|tell|give|say)\b.*\bcode\b",
    "card": r"\b(card number|cvv|sixteen digits|security code on the back|card details|debit card number|credit card number)\b",
    "ssn": r"\b(social security|your social\b|ssn)\b",
    "gift_card": r"\bgift cards?\b|\bprepaid cards?\b|\bitunes\b|\bgoogle play\b|\bapple cards?\b",
    "crypto": r"\b(bitcoin|crypto|wallet|btc)\b",
    "wire": r"\b(wire (the|your|\$|two|it|transfer)|wire transfer|safe account|protected account|wire (your )?savings|wire .* to)\b",
    "p2p": r"\b(zelle|venmo|cash ?app)\b",
    "remote_app": r"\b(anydesk|teamviewer|remote (support|access|app|tool)|take control of your)\b",
    "secrecy": r"\b(don'?t tell|do not tell|not tell anyone|keep this (private|between)|do not discuss|keep it secret)\b",
}
_URGENT = r"\b(arrest|warrant|lien|shut off|disconnected|suspended|compromised|hacked|virus|immediately|right now|today)\b"


def rules_score(window_text: str) -> dict:
    t = window_text.lower()
    asks = [a for a, rx in _RULES.items() if re.search(rx, t, re.S)]
    hard = [a for a in asks if a in HARD_ASKS]
    s = 0.05
    if hard:
        s = 0.85 + (0.1 if len(asks) > 1 else 0)
    elif "secrecy" in asks:
        s = 0.5
    elif re.search(_URGENT, t):
        s = 0.35
    return {"s": min(s, 1.0), "asks": asks}


# ---------------------------------------------------------------- scoring (engines)
class RateLimiter:
    def __init__(self, rpm: int):
        self.gap = 60.0 / rpm
        self._next = 0.0
        self._lock = asyncio.Lock()

    async def wait(self):
        async with self._lock:
            now = time.monotonic()
            delay = max(0.0, self._next - now)
            self._next = max(now, self._next) + self.gap
        if delay:
            await asyncio.sleep(delay)


def _sha(*parts: str) -> str:
    return hashlib.sha256("\x1f".join(parts).encode()).hexdigest()[:24]


def pipeline_fingerprint(engine: str) -> str:
    """Anything that changes what a cached score means: prompt, model name, detect.py version."""
    parts = [engine]
    try:
        from detection import prompt
        parts.append(_sha(prompt.SYSTEM_PROMPT))
    except Exception:
        parts.append("noprompt")
    parts.append(os.environ.get("LOCAL_MODEL", "") if engine == "local" else os.environ.get("NVIDIA_MODEL", os.environ.get("CLOUD_MODEL", "")))
    for f in ("detect.py", "schema.py", "engines/cloud.py", "engines/local.py"):
        if engine == "prodrules" and f.startswith("engines/"):
            continue
        p = ROOT / "detection" / f
        if p.exists() and (engine != "local" or f != "engines/cloud.py") and (engine != "cloud" or f != "engines/local.py"):
            parts.append(_sha(p.read_text()))
    return _sha(*parts)


def _cache_path(engine: str) -> pathlib.Path:
    return CACHE_DIR / f"{engine}.jsonl"


def _load_cache(engine: str) -> dict:
    p = _cache_path(engine)
    out = {}
    if p.exists():
        for line in p.read_text().splitlines():
            try:
                d = json.loads(line)
                out[d["key"]] = d["val"]
            except (ValueError, KeyError):
                pass
    return out


import contextvars  # noqa: E402

_PROBE: contextvars.ContextVar = contextvars.ContextVar("probe", default=None)
_PATCHED = False


def _install_probe():
    """Wrap detect._engine_score so we know whether the model really answered (detect() fails open to rules)."""
    global _PATCHED
    if _PATCHED:
        return
    from detection import detect as d
    orig = d._engine_score

    async def wrapped(window_text, metadata, engine):
        out = await orig(window_text, metadata, engine)
        probe = _PROBE.get()
        if probe is not None:
            probe["ok"] = True
        return out
    d._engine_score = wrapped
    _PATCHED = True


async def _pipeline_score(engine: str, call_id: str, window_text: str) -> dict:
    """The real path: detection.detect.detect(...) (rule backstop + LLM merge + fail-open).
    Returns the dict plus "fallback": True when the model failed/timed out and detect fell back to rules."""
    from detection.detect import detect  # eng1
    _install_probe()
    probe = {"ok": False}
    token = _PROBE.set(probe)
    try:
        out = await detect(call_id, window_text, {}, engine)
    finally:
        _PROBE.reset(token)
    return {**out, "fallback": not probe["ok"]}


async def score_window(engine: str, call_id: str, window_text: str, *, cache: dict, fp: str,
                       limiter: RateLimiter | None, scorer=None, cache_file=None) -> dict:
    """Returns {"s","asks","ms","cached"}. scorer overrides the pipeline (used by tests)."""
    key = _sha(fp, window_text)
    if key in cache:
        return {**cache[key], "cached": True}
    if engine in ("rules", "prodrules"):
        t0 = time.perf_counter()
        if engine == "prodrules":
            from detection.detect import quick
            q = quick(window_text, "cloud")
            d = {"s": float(q.get("s", 0.0)), "asks": list(q.get("asks", []))}
        else:
            d = rules_score(window_text)
        val = {"s": d["s"], "asks": d["asks"], "ms": round((time.perf_counter() - t0) * 1000, 3)}
    else:
        if limiter:
            await limiter.wait()
        for attempt in range(3):  # model failures (timeout/429) are retried, never cached
            t0 = time.perf_counter()
            d = await (scorer or _pipeline_score)(engine, call_id, window_text)
            ms = (time.perf_counter() - t0) * 1000
            if not d.get("fallback"):
                break
            await asyncio.sleep(2 * (attempt + 1))
        val = {"s": float(d.get("s", 0.0)), "asks": list(d.get("asks", [])), "ms": round(ms, 1),
               "engine_used": d.get("engine"), "addresses_ai_system": bool(d.get("addresses_ai_system", False)),
               "fallback": bool(d.get("fallback"))}
        if val["fallback"]:
            return {**val, "cached": False}
    cache[key] = val
    if cache_file is not None:
        with cache_file.open("a") as f:
            f.write(json.dumps({"key": key, "val": val}) + "\n")
    return {**val, "cached": False}


async def run_row(engine: str, row: dict, **kw) -> dict:
    lines = row["caller_lines"]
    per_line = []
    for k in range(1, len(lines) + 1):
        window = "\n".join(lines[max(0, k - WINDOW_LINES):k])
        res = await score_window(engine, row["id"], window, **kw)
        per_line.append({"k": k, "s": res["s"], "asks": res["asks"], "ms": res["ms"], "cached": res["cached"],
                         "fallback": bool(res.get("fallback")),
                         "ai": bool(res.get("addresses_ai_system", False))})
    return {"id": row["id"], "split": row["split"], "label": row["label"], "scam_type": row["scam_type"],
            "adversarial_kind": row.get("adversarial_kind"), "expected_asks": row["expected_asks"],
            "expected_alert": row["expected_alert"], "n_lines": len(lines), "engine": engine, "per_line": per_line}


async def run_engine(engine: str, rows: list[dict], scorer=None, concurrency: int = 4) -> list[dict]:
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    cache = _load_cache(engine)
    fp = pipeline_fingerprint(engine)
    limiter = RateLimiter(MAX_RPM[engine]) if engine in MAX_RPM else None
    sem = asyncio.Semaphore(1 if (limiter or engine == 'local') else concurrency)
    cf = _cache_path(engine)

    async def one(r):
        async with sem:
            return await run_row(engine, r, cache=cache, fp=fp, limiter=limiter, scorer=scorer, cache_file=cf)
    return await asyncio.gather(*(one(r) for r in rows))


# ---------------------------------------------------------------- metrics
def wilson(k: int, n: int, z: float = 1.96) -> tuple[float, float]:
    if n == 0:
        return (0.0, 0.0)
    p = k / n
    d = 1 + z * z / n
    c = (p + z * z / (2 * n)) / d
    h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / d
    return (max(0.0, c - h), min(1.0, c + h))


def alert_line(rec: dict, thr: float):
    for pl in rec["per_line"]:
        if pl["s"] >= thr:
            return pl["k"]
    return None


def first_hard_ask_line(rec_rules: dict | None, rec: dict) -> int | None:
    """First line where the (transparent) rules baseline sees a hard ask: the reference for 'ask -> alert' delay."""
    src = rec_rules or rec
    for pl in src["per_line"]:
        if any(a in HARD_ASKS for a in pl["asks"]):
            return pl["k"]
    return None


def pct(k, n):
    if n == 0:
        return "n/a"
    lo, hi = wilson(k, n)
    return f"{100 * k / n:.0f}% ({k}/{n}) [{100 * lo:.0f}-{100 * hi:.0f}]"


def _quantile(xs, q):
    if not xs:
        return float("nan")
    xs = sorted(xs)
    return xs[min(len(xs) - 1, int(math.ceil(q * len(xs))) - 1)]


def compute_metrics(recs: list[dict], thr: float, rules_by_id: dict | None = None) -> dict:
    scams = [r for r in recs if r["expected_alert"]]
    legit = [r for r in recs if not r["expected_alert"]]
    adv = [r for r in recs if r["label"] == "adversarial" and r["expected_alert"]]
    m = {"thr": thr, "n": len(recs)}
    by_type = defaultdict(lambda: [0, 0])
    for r in scams:
        by_type[r["scam_type"]][1] += 1
        by_type[r["scam_type"]][0] += alert_line(r, thr) is not None
    m["recall"] = (sum(v[0] for v in by_type.values()), len(scams))
    m["recall_by_type"] = {t: tuple(v) for t, v in sorted(by_type.items())}
    m["false_alarm"] = (sum(alert_line(r, thr) is not None for r in legit), len(legit))
    m["legit_plain"] = (sum(alert_line(r, thr) is not None for r in legit if r["label"] == "legit"),
                        sum(r["label"] == "legit" for r in legit))
    m["legit_bait"] = (sum(alert_line(r, thr) is not None for r in legit if r["label"] == "adversarial"),
                       sum(r["label"] == "adversarial" for r in legit))
    m["adv_recall"] = (sum(alert_line(r, thr) is not None for r in adv), len(adv))
    inj = [r for r in adv if r.get("adversarial_kind") in ("prompt_injection", "addresses_ai_system", "allowlist_poisoning", "action_target_injection")]
    m["inj_recall"] = (sum(alert_line(r, thr) is not None for r in inj), len(inj))
    # asks (final-line union vs expected), micro-averaged over rows with expected asks or predicted asks
    tp = fp = fn = 0
    for r in recs:
        pred = set()
        for pl in r["per_line"]:
            pred |= set(pl["asks"])
        exp = set(r["expected_asks"])
        tp += len(pred & exp)
        fp += len(pred - exp)
        fn += len(exp - pred)
    m["asks_precision"] = (tp, tp + fp)
    m["asks_recall"] = (tp, tp + fn)
    # delay from first hard ask (per rules reference) to alert, in lines / seconds
    delays, lat = [], [pl["ms"] for r in recs for pl in r["per_line"]]
    for r in scams:
        a = alert_line(r, thr)
        if a is None:
            continue
        h = first_hard_ask_line((rules_by_id or {}).get(r["id"]), r)
        if h is None:
            continue
        delays.append(a - h)
    m["delay_lines"] = delays
    m["delay_lines_mean"] = sum(delays) / len(delays) if delays else float("nan")
    # addresses_ai_system: truth = the script actually talks to the AI (injection / addresses_ai kinds)
    ai_kinds = {"prompt_injection", "addresses_ai_system"}
    no_ai = [r for r in recs if r.get("adversarial_kind") not in ai_kinds]
    yes_ai = [r for r in recs if r.get("adversarial_kind") in ai_kinds]
    m["ai_fp"] = (sum(any(pl.get("ai") for pl in r["per_line"]) for r in no_ai), len(no_ai))
    m["ai_tp"] = (sum(any(pl.get("ai") for pl in r["per_line"]) for r in yes_ai), len(yes_ai))
    m["n_fallback"] = sum(bool(pl.get("fallback")) for r in recs for pl in r["per_line"])
    m["n_windows"] = len(lat)
    m["mean_ms"] = sum(lat) / len(lat) if lat else float("nan")
    m["p95_ms"] = _quantile(lat, 0.95)
    m["p50_ms"] = _quantile(lat, 0.50)
    m["seconds_late"] = m["delay_lines_mean"] * SECONDS_PER_LINE + m["p50_ms"] / 1000
    return m


def youden(m: dict) -> float:
    rk, rn = m["recall"]
    fk, fn = m["false_alarm"]
    return (rk / rn if rn else 0) - (fk / fn if fn else 0)


def tune_threshold(recs_dev: list[dict]) -> tuple[float, list]:
    """Pick the threshold maximizing recall - false_alarm on DEV only (ties -> higher threshold: fewer alarms)."""
    sweep = [(t, youden(compute_metrics(recs_dev, t))) for t in THRESHOLDS]
    best = max(sweep, key=lambda x: (round(x[1], 6), x[0]))
    return best[0], sweep


# ---------------------------------------------------------------- results files + report
def write_results(engine: str, split: str, recs: list[dict]):
    RESULTS_DIR.mkdir(exist_ok=True)
    p = RESULTS_DIR / f"{engine}-{split}.jsonl"
    p.write_text("".join(json.dumps(r) + "\n" for r in recs))
    return p


def read_results(engine: str, split: str) -> list[dict]:
    p = RESULTS_DIR / f"{engine}-{split}.jsonl"
    return [json.loads(x) for x in p.read_text().splitlines()] if p.exists() else []


def git_sha() -> str:
    try:
        return subprocess.check_output(["git", "-C", str(ROOT), "rev-parse", "--short", "HEAD"], text=True).strip()
    except Exception:
        return "unknown"


def freeze(engines) -> dict:
    cur = json.loads(FROZEN.read_text()) if FROZEN.exists() else {"thresholds": {}}
    out = cur
    out.setdefault("thresholds", {})
    for e in engines:
        dev = read_results(e, "dev")
        if not dev:
            print(f"freeze: no dev results for {e}, skipped")
            continue
        thr, sweep = tune_threshold(dev)
        out["thresholds"][e] = {"threshold": thr, "tuned_on": "dev", "n_dev": len(dev),
                                "dev_youden": round(dict(sweep)[thr], 3), "git_sha": git_sha()}
    out.setdefault("git_sha", git_sha())
    out["frozen_at"] = time.strftime("%Y-%m-%dT%H:%M:%S%z")
    FROZEN.write_text(json.dumps(out, indent=2) + "\n")
    return out


def scored_only(recs):
    """Rows where every window was really scored by the model (no rules fallback); the rest are 'not scored'."""
    good = [r for r in recs if not any(pl.get("fallback") for pl in r["per_line"])]
    return good, len(recs) - len(good)


def _read_before(engine: str) -> list[dict]:
    f = EVAL_DIR / "results" / "before" / f"{engine}-test.jsonl"
    return [json.loads(l) for l in f.read_text().splitlines() if l.strip()] if f.exists() else []


def before_after_section(fz: dict) -> list[str]:
    """BEFORE (1242399 numbers, code at 20ca58a) vs AFTER (current trunk), same frozen thresholds, split=test."""
    rules_after = {r["id"]: r for r in read_results("rules", "test")}
    rules_before = {r["id"]: r for r in _read_before("rules")}
    L = ["## Before vs after TASK-022/023 (split = test, thresholds unchanged)", "",
         f"BEFORE = results/before/ (scored on code at `{fz.get('git_sha', 'n/a')}`, prior to AI-address gating, clause negation, request-verb gate, few-shots). "
         f"AFTER = trunk `{fz.get('test_run_sha_after', git_sha())}` (local+rules runs). No retuning; thresholds tuned on dev only. The rules row is the standalone keyword baseline in run_eval.py, so it is identical by construction.", ""]
    for e in ("local", "rules"):
        b_all, a_all = _read_before(e), read_results(e, "test")
        if not b_all or not a_all:
            continue
        t = fz["thresholds"].get(e, {}).get("threshold", DEFAULT_THRESHOLD)
        bg, bn = scored_only(b_all)
        ag, an = scored_only(a_all)
        mb = compute_metrics(bg, t, rules_before)
        ma = compute_metrics(ag, t, rules_after)
        L += [f"**{e}** (thr {t}); rows scored before {mb['n']} (not scored {bn}), after {ma['n']} (not scored {an})", "",
              "| metric | before | after |", "|---|---|---|"]
        for name, k in [("scam recall", "recall"), ("adversarial recall", "adv_recall"),
                        ("false alarm, all legit", "false_alarm"), ("false alarm, keyword-bait legit", "legit_bait"),
                        ("addresses_ai false positives", "ai_fp"), ("asks precision", "asks_precision"),
                        ("asks recall", "asks_recall")]:
            L.append(f"| {name} | {pct(*mb[k])} | {pct(*ma[k])} |")
        L.append(f"| /detect latency p50 (ms) | {mb['p50_ms']:.0f} | {ma['p50_ms']:.0f} |")
        L.append("")
    return L


def heldout_section(fz: dict) -> list[str]:
    have = [e for e in ("rules", "prodrules", "local") if read_results(e, "v2")]
    if not have:
        return []
    rb = {r["id"]: r for r in read_results("rules", "v2")}
    ms = {}
    for e in have:
        good, bad = scored_only(read_results(e, "v2"))
        ms[e] = compute_metrics(good, fz["thresholds"].get(e, {}).get("threshold", DEFAULT_THRESHOLD), rb)
        ms[e]["not_scored"] = bad
    kinds = {}
    for r in load_rows([HELDOUT_V2]):
        kinds[r["id"]] = r.get("v2_kind")
    L = ["## Held-out v2 (40 fresh synthetic rows, scored ONCE, thresholds frozen on dev, no tuning)", "",
         f"File `heldout_v2.jsonl` (written before the engines saw it; not in the default row files). Scored on trunk `{git_sha()}`. "
         "20 scams (8 no-classic-keywords, 4 Spanish/Spanglish, 4 AI-directed injection, 4 slow-build) + 20 legit (10 keyword-bait, 10 ordinary). "
         "n is tiny: read every interval.", "",
         "| metric | " + " | ".join(f"{e} (thr {ms[e]['thr']})" for e in have) + " |", "|---|" + "---|" * len(have)]
    def row(name, fn):
        L.append(f"| {name} | " + " | ".join(fn(ms[e]) for e in have) + " |")
    row("rows scored / not scored", lambda m: f"{m['n']} / {m['not_scored']}")
    row("scam recall", lambda m: pct(*m["recall"]))
    row("adversarial recall (injection + Spanish)", lambda m: pct(*m["adv_recall"]))
    row("false alarm, all legit", lambda m: pct(*m["false_alarm"]))
    row("false alarm, keyword-bait legit", lambda m: pct(*m["legit_bait"]))
    row("false alarm, plain legit", lambda m: pct(*m["legit_plain"]))
    row("asks precision", lambda m: pct(*m["asks_precision"]))
    row("asks recall", lambda m: pct(*m["asks_recall"]))
    row("addresses_ai false positives", lambda m: pct(*m["ai_fp"]))
    row("windows fallen back to rules", lambda m: f"{m['n_fallback']}/{m['n_windows']}")
    row("/detect latency p50 (ms)", lambda m: f"{m['p50_ms']:.0f}")
    L.append("")
    thr = {e: fz["thresholds"].get(e, {}).get("threshold", DEFAULT_THRESHOLD) for e in have}
    L += ["Scam recall by v2 style (alerted / n):", "", "| style | " + " | ".join(have) + " |", "|---|" + "---|" * len(have)]
    for kind in ("no_keywords", "spanish", "injection", "slow_build"):
        cells = []
        for e in have:
            good, _ = scored_only(read_results(e, "v2"))
            rs = [r for r in good if kinds.get(r["id"]) == kind]
            cells.append(f"{sum(1 for r in rs if alert_line(r, thr[e]) is not None)}/{len(rs)}")
        L.append(f"| {kind} | " + " | ".join(cells) + " |")
    L.append("")
    return L


def build_report() -> str:
    fz = json.loads(FROZEN.read_text()) if FROZEN.exists() else {"thresholds": {}}
    engines = [e for e in ENGINES if read_results(e, "dev") or read_results(e, "test")]
    missing = [f"{e}/{sp}" for e in ENGINES for sp in ("dev", "test") if not read_results(e, sp)]
    L = ["# P2 detection evaluation: cloud vs local vs rules-only", "",
         "**All data is synthetic** (hand-written scam scripts, legit look-alikes, adversarial rows). "
         "Small n: read every cell with its interval (Wilson 95%). Thresholds were tuned on split=dev only and frozen "
         f"before scoring split=test (`FROZEN.json`, git `{fz.get('git_sha', 'n/a')}`).", "",
         f"Setup: caller lines replayed one at a time, window = last {WINDOW_LINES} lines, alert when s >= threshold. "
         f"'Rules' = a plain keyword baseline (`rules_score` in run_eval.py), not an LLM; 'prodrules' = the production rule path (`detect.quick`: rule_scan + merge, what runs live when the LLM fails). Seconds assume ~{SECONDS_PER_LINE:.0f} s of speech per line.", ""]
    rules_cache = {sp: {r["id"]: r for r in read_results("rules", sp)} for sp in ("dev", "test")}
    for sp in ("test", "dev"):
        have = [e for e in engines if read_results(e, sp)]
        if not have:
            continue
        L += [f"## split = {sp}" + ("  (the headline numbers)" if sp == "test" else "  (used for tuning, optimistic)"), ""]
        ms = {}
        for e in have:
            t = fz["thresholds"].get(e, {}).get("threshold", DEFAULT_THRESHOLD)
            good, bad = scored_only(read_results(e, sp))
            ms[e] = compute_metrics(good, t, rules_cache[sp])
            ms[e]["not_scored"] = bad
        hdr = "| metric | " + " | ".join(f"{e} (thr {ms[e]['thr']})" for e in have) + " |"
        L += [hdr, "|---|" + "---|" * len(have)]
        def row(name, fn):
            L.append(f"| {name} | " + " | ".join(fn(ms[e]) for e in have) + " |")
        row("rows scored / not scored (429 or model failure)", lambda m: f"{m['n']} / {m['not_scored']}")
        row("scam recall (all alert-worthy)", lambda m: pct(*m["recall"]))
        row("adversarial recall", lambda m: pct(*m["adv_recall"]))
        row("injection-only recall", lambda m: pct(*m["inj_recall"]))
        row("false alarm, all legit", lambda m: pct(*m["false_alarm"]))
        row("false alarm, plain legit", lambda m: pct(*m["legit_plain"]))
        row("false alarm, keyword-bait legit", lambda m: pct(*m["legit_bait"]))
        row("asks precision", lambda m: pct(*m["asks_precision"]))
        row("asks recall", lambda m: pct(*m["asks_recall"]))
        row("lines from first hard ask to alert (mean)", lambda m: "n/a" if math.isnan(m["delay_lines_mean"]) else f"{m['delay_lines_mean']:+.2f} (n={len(m['delay_lines'])})")
        row("approx seconds late (lines*3s + p50 latency)", lambda m: "n/a" if math.isnan(m["seconds_late"]) else f"{m['seconds_late']:+.1f}")
        row("addresses_ai flag: false positives (scripts that never address the AI)", lambda m: pct(*m["ai_fp"]))
        row("addresses_ai flag: detected (scripts that do)", lambda m: pct(*m["ai_tp"]))
        row("windows where the model failed (fell back to rules)", lambda m: f"{m['n_fallback']}/{m['n_windows']}")
        row("/detect latency p50 / p95 / mean (ms)", lambda m: f"{m['p50_ms']:.0f} / {m['p95_ms']:.0f} / {m['mean_ms']:.0f}")
        L.append("")
        types = sorted({t for e in have for t in ms[e]["recall_by_type"]})
        L += ["Recall by scam type (n per cell; cells with n<5 are anecdotes):", "",
              "| scam_type | " + " | ".join(have) + " |", "|---|" + "---|" * len(have)]
        for t in types:
            L.append(f"| {t} | " + " | ".join("{}/{}".format(*ms[e]["recall_by_type"].get(t, (0, 0))) for e in have) + " |")
        L.append("")
    L += before_after_section(fz)
    L += heldout_section(fz)
    if missing:
        L += ["**Not scored (no results yet, e.g. NVIDIA key 429):** " + ", ".join(missing), ""]
    L += ["## Honest caveats", "",
          "- Scripts are short (4-5 lines) and written by the team, so models see cleaner text than a real STT stream.",
          "- Test n is small; intervals are wide. A 5-point gap between engines is not a finding.",
          "- 'First hard ask' is located by the rules baseline, so delay is relative to that reference, not human labels.",
          "- No audio, no real callers, no real PII anywhere.",
          "- Cloud test is not scored (NVIDIA 429); rows with any model-failure window are excluded and counted as not scored."]
    lat = EVAL_DIR / "LATENCY.md"
    if lat.exists():
        L += ["", lat.read_text().rstrip(), ""]
    return "\n".join(L) + "\n"


# ---------------------------------------------------------------- CLI
def _summary(engine, split, recs, thr):
    m = compute_metrics(recs, thr)
    print(f"{engine}/{split} n={m['n']} thr={thr}: recall {pct(*m['recall'])}  false-alarm {pct(*m['false_alarm'])}  "
          f"adv {pct(*m['adv_recall'])}  p50 {m['p50_ms']:.0f}ms p95 {m['p95_ms']:.0f}ms")


async def amain(a) -> int:
    engines = list(ENGINES) if a.engine == "all" else [a.engine] if a.engine else []
    if a.report:
        (EVAL_DIR / "RESULTS.md").write_text(build_report())
        print("wrote", EVAL_DIR / "RESULTS.md")
        return 0
    if a.freeze:
        print(json.dumps(freeze(engines or list(ENGINES)), indent=2))
        return 0
    if not engines:
        print("need --engine, --freeze or --report")
        return 2
    splits = ["dev", "test"] if a.split == "all" else [a.split]
    if a.heldout:
        if "cloud" in engines:
            print("refusing: held-out v2 is scored for local/rules/prodrules only (no NVIDIA calls)")
            return 2
        splits = ["v2"]
    fz = json.loads(FROZEN.read_text()) if FROZEN.exists() else {"thresholds": {}}
    for sp in splits:
        if sp == "test" and not FROZEN.exists() and not a.allow_unfrozen:
            print("refusing to score split=test before FROZEN.json exists (tune on dev, then --freeze)")
            return 2
        rows = load_rows([HELDOUT_V2], split=None) if sp == "v2" else load_rows(split=sp)
        if a.limit:
            rows = rows[: a.limit]
        for e in engines:
            recs = await run_engine(e, rows)
            if not a.limit:
                write_results(e, sp, recs)
            thr = fz["thresholds"].get(e, {}).get("threshold", DEFAULT_THRESHOLD)
            _summary(e, sp, recs, thr)
    return 0


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--heldout", action="store_true", help="score heldout_v2.jsonl (writes results/<engine>-v2.jsonl); never tune on it")
    ap.add_argument("--engine", choices=[*ENGINES, "all"])
    ap.add_argument("--split", choices=["dev", "test", "all"], default="dev")
    ap.add_argument("--limit", type=int, default=0, help="first N rows only (smoke test; does not write results)")
    ap.add_argument("--freeze", action="store_true", help="tune thresholds on dev results and write FROZEN.json")
    ap.add_argument("--report", action="store_true", help="write RESULTS.md from results/*.jsonl")
    ap.add_argument("--allow-unfrozen", action="store_true")
    return asyncio.run(amain(ap.parse_args(argv)))


if __name__ == "__main__":
    raise SystemExit(main())
