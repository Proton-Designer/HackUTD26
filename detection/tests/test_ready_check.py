from detection.scripts import ready_check as R

H = {"ok": True, "engines": {"primary": "local", "local_reachable": True, "local_probe_ms": 15}, "cloud_breaker": {"state": "closed", "retry_in_s": 0.0},
     "stt": {"backend": "riva", "primary_bypassed": False, "primary_failures": 0, "whisper_fallback_loaded": True}, "active_stt_sockets": 0}

def states(h): return {n: s for n, s, d, hint in R.check_health(h)}

def test_healthy_all_pass():
    assert set(states(H).values()) == {"PASS"}

def test_each_failure_is_flagged():
    import copy
    h = copy.deepcopy(H); h["engines"]["primary"] = "cloud"; assert states(h)["engines.primary == local"] == "FAIL"
    h = copy.deepcopy(H); h["engines"]["local_reachable"] = False; assert states(h)["llama reachable (local_reachable)"] == "FAIL"
    h = copy.deepcopy(H); h["cloud_breaker"]["state"] = "open"; assert states(h)["cloud breaker closed"] == "WARN"
    h = copy.deepcopy(H); h["stt"]["primary_bypassed"] = True; assert states(h)["STT primary not bypassed"] == "WARN"
    h = copy.deepcopy(H); h["active_stt_sockets"] = 2; assert states(h)["no active STT sockets"] == "WARN"
    assert states({})["healthz ok"] == "FAIL"

def test_hints_only_on_non_pass():
    assert all(hint == "" for n, s, d, hint in R.check_health(H))

def test_tunnel_match():
    assert R.tunnel_matches(H, dict(H))[0]
    t = dict(H, engine="cloud"); ok, d = R.tunnel_matches(dict(H, engine="local"), t); assert not ok and "engine" in d

def test_env_flag_reads_only_the_key_and_never_returns_values():
    env = b"A=1\0P2_DUMP_AUDIO=1\0NVIDIA_API_KEY=secret\0"
    assert R.env_flag(env) == "on" and R.env_flag(b"P2_DUMP_AUDIO=0\0") == "off" and R.env_flag(b"X=1\0") == "unset"
    assert R.env_flag(b"P2_DUMP_AUDIO_X=1\0") == "unset"

def test_tag_status():
    tags = {"p2-known-good-0250": "aaa111", "p2-known-good-0334": "bbb222", "other": "ccc333"}
    assert R.tag_status("bbb222", tags)[0] and not R.tag_status("ccc333", tags)[0] and not R.tag_status("zzz999", tags)[0]

def test_stale_code():
    assert R.stale_code(100, 200) and not R.stale_code(200, 100) and not R.stale_code(100, 100)

def test_controls():
    c = R.controls({"band": "critical", "s": 1.0}, {"band": "low", "s": 0.0}); assert all(ok for _, ok, _ in c)
    c = R.controls({"band": "high"}, None); assert not any(ok for _, ok, _ in c)


def test_tag_status_same_code_after_non_p2_commits():
    tags = {"p2-known-good-0535": "aaa111"}
    ok, d = R.tag_status("bbb222", tags, lambda t: True)
    assert ok and "p2-known-good-0535" in d
    assert not R.tag_status("bbb222", tags, lambda t: False)[0]
    assert not R.tag_status("bbb222", tags, lambda t: 1 / 0)[0]
