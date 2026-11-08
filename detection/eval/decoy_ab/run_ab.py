"""Decoy model A/B harness (eval tool, NOT runtime). Uses the decoy's own prompt code: decoy.core.SYSTEM / chat / guard / Persona,
decoy.playbooks classify / note / PULLS / missing. Only the per-turn glue (history list, steer counters) mirrors decoy/app.py
reply()/steer() (app.py:510-530, 553-562) because DecoyCall needs a live websocket. Scammer turns are fixed (card lines); the
decoy history uses each model's OWN earlier replies (guard()'d, as the app stores them).
Usage: python -m detection.eval.decoy_ab.run_ab out.json [--cards 1,2] ; env NVIDIA_API_KEY (load in a subshell, never printed)."""
import asyncio, json, random, re, sys, time, urllib.request
from decoy import core, playbooks as PB

CAP_S = 180.0
VARIANTS = {  # label -> (model, temperature, max_tokens)
    "bolt-e4b (current)": ("nvidia/nemotron-3.5-bolt-e4b", 0.8, 90),
    "super-vl-120b": ("nvidia/nemotron-3.5-super-vl-120b-a12b", 0.8, 90),
    # P1's candidate SYSTEM (docs/patches/decoy-system-candidate.txt), T0.6/90, same steering note + pre-handoff turn
    "CAND bolt-e4b": ("nvidia/nemotron-3.5-bolt-e4b", 0.6, 90, "cand"),
    "CAND super-vl-120b": ("nvidia/nemotron-3.5-super-vl-120b-a12b", 0.6, 90, "cand"),
}
CAND = open("docs/patches/decoy-system-candidate.txt").read().strip()
import os
OLD_SYSTEM = open(os.environ["OLD_SYSTEM_FILE"]).read().strip() if os.environ.get("OLD_SYSTEM_FILE") else None
# HEAD arms (P3 ab29d8e note on the latest caller turn, P1 93634a8 SYSTEM = core.SYSTEM at HEAD, T0.6/90, generated first line)
HEAD_VARIANTS = {
    "HEAD bolt-e4b": ("nvidia/nemotron-3.5-bolt-e4b", 0.6, 90, None),
    "HEAD super-vl-120b": ("nvidia/nemotron-3.5-super-vl-120b-a12b", 0.6, 90, None),
    "HEAD note + OLD system, super-vl": ("nvidia/nemotron-3.5-super-vl-120b-a12b", 0.6, 90, "old"),
}
HEAD_MODE = os.environ.get("HEAD_MODE") == "1"
if HEAD_MODE: VARIANTS = HEAD_VARIANTS

def cards():
    s = open("data/script-cards-v3-bank.md").read(); out = {}
    for m in re.finditer(r"## Card (\d+): (.+?)\n.*?\n\n((?:\d\. .+\n)+)\n\*\*Payment step:\*\* (.+)", s):
        lines = [re.sub(r'^\d\. "|"$', "", l.strip()).strip('"') for l in m.group(3).strip().split("\n")]
        pay = m.group(4).strip().strip('"')
        out[int(m.group(1))] = (m.group(2), lines, pay)
    return out

def healthz_busy():
    try:
        d = json.load(urllib.request.urlopen("http://localhost:8100/healthz", timeout=3)); return d.get("active_stt_sockets", 0) > 0
    except Exception: return False

async def run_one(card_id, label, model, temp, mx, name, lines, pay, system=None):
    persona = core.Persona(f"ab-{card_id}-{label}")
    given, used, asks = set(), set(), {}
    rnd = random.Random(f"{card_id}")          # same 'pull' picks for every model
    pre = [lines[0]]; turns_in = lines[1:5]   # 4 scammer turns after the pre-handoff line (lead's 08:02 spec); payment step not used
    scam = PB.classify(pre, "generic")
    history = [{"role": "user", "content": "<caller>" + core.clean(" ".join(pre))[-1500:] + "</caller>"}]
    seen, rows = [], []
    SYS = system or core.SYSTEM
    if HEAD_MODE:   # decoy/app.py warm(): first line generated from the pre-handoff story, recorded once in history
        first = await core.chat([{"role": "system", "content": SYS}] + history + [{"role": "system", "content": "[private] You are picking the call back up after a two-second pause. Say your first line now: one short sentence reacting to what the caller said, then ask what to do next. Don't mention the pause or the line."}], max_tokens=mx, temperature=temp, model=model)
        h0, sp0 = core.guard(first, persona, given, lambda t, d: None, " ".join(pre)) if first else (core.OPENER_SHORT, core.OPENER_SHORT)
        history.append({"role": "assistant", "content": h0})
        rows.append({"turn": 0, "scammer": pre[0], "raw": first, "hist": h0, "spoken": sp0, "ms": 0, "scam": scam})
    else:
        history.append({"role": "assistant", "content": core.OPENER})
    for i, text in enumerate(turns_in):
        seen.append(text)
        scam = PB.classify(pre + seen, scam)
        history.append({"role": "user", "content": f"<caller>{core.clean(core.fix_zelle(text) if HEAD_MODE else text)}</caller>"})
        need = [t for t in PB.missing(scam, []) if t != "impersonated_org"]
        pull = None
        if need:
            asks[need[0]] = asks.get(need[0], 0) + 1
            fresh = [p for p in PB.PULLS.get(need[0], []) if p not in used]
            if fresh: pull = rnd.choice(fresh); used.add(pull)
        left = max(1, int((CAP_S - 15 * (i + 1)) / 15))
        if HEAD_MODE:
            money = any(PB.MONEY_TALK.search(l) for l in pre + seen)
            steer = PB.note(scam, [], left, money)
            hh = [dict(m) for m in history[-16:]]; hh[-1]["content"] += "\n" + steer     # note rides on the latest caller turn
            msgs = [{"role": "system", "content": SYS}] + hh
        else:
            steer = PB.note(scam, [], left, pull)
            msgs = [{"role": "system", "content": SYS}] + history[-16:] + [{"role": "system", "content": steer}]
        t0 = time.monotonic()
        out = await core.chat(msgs, max_tokens=mx, temperature=temp, model=model)
        ms = int((time.monotonic() - t0) * 1000)
        if out is None:
            rows.append({"turn": i + 1, "scammer": text, "raw": None, "spoken": None, "ms": ms, "scam": scam}); await asyncio.sleep(1.5); continue
        trips = []
        hist, spoken = core.guard(out, persona, given, lambda t, d: trips.append(d.get("rule") or t), " ".join(pre + seen))
        history.append({"role": "assistant", "content": hist})
        rows.append({"turn": i + 1, "scammer": text, "raw": out, "hist": hist, "spoken": spoken, "ms": ms, "trips": trips, "scam": scam, "steer": steer})
        await asyncio.sleep(1.3)
    return rows

async def main():
    out = sys.argv[1]; sel = None
    if "--cards" in sys.argv: sel = {int(x) for x in sys.argv[sys.argv.index("--cards") + 1].split(",")}
    only = sys.argv[sys.argv.index("--only") + 1].split(",") if "--only" in sys.argv else None
    res = {}
    for cid, (name, lines, pay) in cards().items():
        if sel and cid not in sel: continue
        if not sel and cid in (3, 9): continue   # pulled from the judge bucket
        while healthz_busy(): print("live call open: pausing", flush=True); await asyncio.sleep(10)
        for label, v in VARIANTS.items():
            if only and not any(o in label for o in only): continue
            model, temp, mx = v[:3]; system = (CAND if v[3] == "cand" else OLD_SYSTEM if v[3] == "old" else None) if len(v) > 3 else None
            res.setdefault(str(cid), {"name": name, "variants": {}})["variants"][label] = await run_one(cid, label, model, temp, mx, name, lines, pay, system)
            print("card", cid, label, "done", flush=True)
        json.dump(res, open(out, "w"), indent=1)
asyncio.run(main())
