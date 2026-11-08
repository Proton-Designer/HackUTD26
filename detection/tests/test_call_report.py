from detection.scripts import call_report as R

LOG = """12:00:00.100 INFO p2.stream stt ws c1 first frame: event=connected
12:00:01.000 INFO p2.stream stt final c1-u1: 0.31s after endpoint: 'This is the IRS'
12:00:01.500 INFO p2.alert risk.update call=c1 s=0.90 band=critical engine=cloud src=fast-final asks=gift_cards
12:00:01.510 INFO p2.alert alert.fired call=c1 level=first src=fast-final s=0.90
12:00:02.000 WARNING p2.detect detect c1 engine=cloud fell back to rules: HTTPStatusError status=429
12:00:02.100 WARNING p2.detect detect c1 failover: cloud HTTPStatusError -> local
12:00:02.200 INFO p2.detect demo cache hit
12:00:03.000 INFO p2.alert user.action continue seen call=c1
12:00:09.000 INFO p2.alert drop late final: audio ended before Continue call=c1
12:00:10.000 INFO p2.alert risk.update call=c1 s=0.00 band=low engine=local src=llm asks=-
INFO:p2.stream:stt final c2-u1: 0.2s after endpoint: 'old format line'
"""

def test_report_parses_timeline_and_summary(tmp_path):
    p = tmp_path / "p2.log"; p.write_text(LOG)
    calls = R.parse(p.read_text().splitlines())
    assert list(calls) == ["c1", "c2"]
    out = R.report("c1", calls["c1"])
    assert "ALERT first (fast path (rules)" in out and "FAILOVER" in out and "dropped late final" in out and "demo cache hit" in out and "user Continue" in out
    assert "first alert +1.4s · final s 0.00 · alerts 1 · failovers 1 · 429s 1" in out
    assert "'old format line'" in R.report("c2", calls["c2"]) and "--" in R.report("c2", calls["c2"])


def test_report_cli_last_and_missing(tmp_path, capsys):
    p = tmp_path / "p2.log"; p.write_text(LOG)
    assert R.main([str(p), "--last", "1"]) == 0 and "call c2" in capsys.readouterr().out
    assert R.main([str(p), "--call", "zzz"]) == 1
    assert R.main([str(tmp_path / "nope.log")]) == 2
