import asyncio
import json
import pytest
from detection.eval import run_eval as ev


def test_all_rows_valid_and_unique():
    rows = ev.load_rows()
    assert len(rows) >= 90
    assert {r["split"] for r in rows} == {"dev", "test"}
    assert sum(r["label"] == "legit" for r in rows) >= 30
    assert sum(r["label"] == "adversarial" for r in rows) >= 20


def test_validate_row_catches_errors():
    assert ev.validate_row({"id": "a"})
    bad = {"id": "a", "split": "dev", "label": "scam", "scam_type": "x", "caller_lines": ["hi"],
           "expected_asks": ["bogus"], "expected_alert": True}
    assert any("unknown asks" in e for e in ev.validate_row(bad))


def test_wilson_and_alert_line():
    lo, hi = ev.wilson(8, 10)
    assert 0.49 < lo < 0.50 and 0.94 < hi < 0.95
    assert ev.wilson(0, 0) == (0.0, 0.0)
    rec = {"per_line": [{"k": 1, "s": 0.2}, {"k": 2, "s": 0.9}]}
    assert ev.alert_line(rec, 0.8) == 2 and ev.alert_line(rec, 0.95) is None


def test_rules_positive_and_negative_control():
    assert ev.rules_score("Buy gift cards and read me the numbers")["s"] >= 0.8
    assert ev.rules_score("Your prescription is ready for pickup")["s"] < 0.4


def _rec(id_, label, exp, ss, asks=()):
    return {"id": id_, "split": "dev", "label": label, "scam_type": "t" if exp else "none", "adversarial_kind": None,
            "expected_asks": list(asks), "expected_alert": exp, "n_lines": len(ss), "engine": "x",
            "per_line": [{"k": i + 1, "s": s, "asks": list(asks) if s > 0.5 else [], "ms": 10, "cached": False} for i, s in enumerate(ss)]}


def test_metrics_and_threshold_tuning():
    recs = [_rec("a", "scam", True, [0.1, 0.9], ["otp"]), _rec("b", "scam", True, [0.1, 0.6], ["otp"]),
            _rec("c", "legit", False, [0.1, 0.55]), _rec("d", "legit", False, [0.1, 0.1])]
    m = ev.compute_metrics(recs, 0.8)
    assert m["recall"] == (1, 2) and m["false_alarm"] == (0, 2)
    m = ev.compute_metrics(recs, 0.5)
    assert m["recall"] == (2, 2) and m["false_alarm"] == (1, 2)
    thr, _ = ev.tune_threshold(recs)
    assert 0.6 <= thr <= 0.9  # J=1 for any thr in [0.6, 0.9]


def test_run_engine_with_mock_scorer_caches(tmp_path, monkeypatch):
    monkeypatch.setattr(ev, "CACHE_DIR", tmp_path)
    calls = []

    async def scorer(engine, call_id, window):
        calls.append(window)
        return {"s": 0.9 if "gift" in window else 0.1, "asks": [], "engine": engine}

    rows = ev.load_rows(split="dev")[:2]
    r1 = asyncio.run(ev.run_engine("local", rows, scorer=scorer))
    n = len(calls)
    assert n > 0 and all(r["engine"] == "local" for r in r1)
    asyncio.run(ev.run_engine("local", rows, scorer=scorer))
    assert len(calls) == n  # second run fully cached


def test_report_builds(tmp_path, monkeypatch):
    monkeypatch.setattr(ev, "RESULTS_DIR", tmp_path)
    monkeypatch.setattr(ev, "FROZEN", tmp_path / "FROZEN.json")
    recs = asyncio.run(ev.run_engine("rules", ev.load_rows(split="test")))
    ev.write_results("rules", "test", recs)
    out = ev.build_report()
    assert "split = test" in out and "false alarm" in out and "synthetic" in out
