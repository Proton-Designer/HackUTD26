import datetime as dt
from detection.eval import replay_call as rc

LOG = """03:06:05.000 INFO p2.stream stt final c1-u1: 0.30s after endpoint: 'x'
03:06:07.000 INFO p2.alert risk.update call=c1 s=0.10 band=low engine=local src=llm asks=-
03:06:09.000 INFO p2.stream stt final c1-u2: 3.00s after endpoint: 'y'
03:06:09.500 INFO p2.stream stt final c1-u3: 1.00s after endpoint: 'z'
03:06:11.000 INFO p2.alert risk.update call=c1 s=0.90 band=high engine=cloud src=llm asks=-
03:06:11.100 INFO p2.alert alert.fired call=c1 level=high src=llm s=0.90
03:06:11.200 INFO p2.stream stt final other-u1: 9.00s after endpoint: 'no'
""".splitlines()

def test_parse_and_summarize():
    day0 = dt.datetime.combine(dt.date.today(), dt.time()).timestamp()
    f, r, a = rc.parse_log(LOG, "c1", day0)
    assert [x["u"] for x in f] == [1, 2, 3] and len(r) == 2 and len(a) == 1      # other call ignored
    t_start = day0 + 3 * 3600 + 6 * 60              # 03:06:00
    s = rc.summarize(f, r, a, t_start)
    assert s["finals_max"] == 3.0 and s["finals_p50"] == 1.0
    assert s["rows"][0]["end_to_risk_s"] == 2.3                    # risk 07.000 - endpoint 04.700
    assert s["rows"][2]["shared_risk"] is True and s["first_alert_s"] == 11.1
