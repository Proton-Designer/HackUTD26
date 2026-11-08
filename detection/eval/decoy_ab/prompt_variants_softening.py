import sys, os, json, time, asyncio, random, re, urllib.request
sys.path.insert(0, '.')
from dotenv import dotenv_values
for k, v in dotenv_values('.env').items():
    if k.startswith('NVIDIA_API_KEY'): os.environ[k] = v
from decoy import core, playbooks as PB
BOLT = "nvidia/nemotron-3.5-bolt-e4b"
SOFT = "- Then, only if their last sentence was about paying, moving money or what to do next, move them one step toward the payment details you still don't have. Otherwise just react to what they said and let them lead."
HARD = "- Then, in the same reply, move them one step toward the payment details you still don't have."
assert SOFT in core.SYSTEM
SYS = {"W": core.SYSTEM, "N": core.SYSTEM.replace(SOFT, HARD)}
def live():
    try: return int(json.load(urllib.request.urlopen('http://localhost:8100/healthz', timeout=3)).get('active_stt_sockets', 0))
    except Exception: return 0
def cards():
    s = open("data/script-cards-v3-bank.md").read(); out = {}
    for m in re.finditer(r"## Card (\d+): (.+?)\n.*?\n\n((?:\d\. .+\n)+)\n\*\*Payment step:\*\* (.+)", s):
        lines = [re.sub(r'^\d\. "|"$', "", l.strip()).strip('"') for l in m.group(3).strip().split("\n")]
        out[int(m.group(1))] = (m.group(2), lines, m.group(4).strip().strip('"'))
    return out
async def run_one(cid, arm, lines):
    persona = core.Persona(f"w-{cid}-{arm}"); given = set(); pre = [lines[0]]; turns_in = lines[1:5]; scam = PB.classify(pre, "generic")
    hist = [{"role": "user", "content": "<caller>" + core.clean(" ".join(pre)) + "</caller>"}, {"role": "assistant", "content": "Sorry, I'm here. What do I need to do?"}]
    seen, rows = [], []
    for i, text in enumerate(turns_in):
        seen.append(text); scam = PB.classify(pre + seen, scam)
        money_now = bool(PB.MONEY_TALK.search(text)); money = any(PB.MONEY_TALK.search(l) for l in pre + seen)
        h = [dict(m) for m in hist] + [{"role": "user", "content": f"<caller>{core.clean(text)}</caller>"}]
        h[-1]["content"] += "\n" + PB.note(scam, [], max(1, int((180 - 15 * (i + 1)) / 15)), money)
        while live(): await asyncio.sleep(10)
        t0 = time.monotonic(); out = await core.chat([{"role": "system", "content": SYS[arm]}] + h, max_tokens=90, temperature=0.6, model=BOLT); ms = int((time.monotonic() - t0) * 1000)
        hs, sp = core.guard(out or "", persona, given, lambda *a: None)
        hist += [{"role": "user", "content": f"<caller>{core.clean(text)}</caller>"}, {"role": "assistant", "content": hs}]
        rows.append(dict(turn=i + 1, scammer=text, money_line=money_now, money_so_far=money, spoken=sp, ms=ms)); await asyncio.sleep(1.5)
    return rows
async def main():
    cs = cards(); res = []
    for cid in (1, 4, 7):
        for arm in "WN":
            res.append(dict(card=cid, arm=arm, rows=await run_one(cid, arm, cs[cid][1]))); json.dump(res, open(sys.argv[1], "w"), indent=1); print("done", cid, arm, flush=True)
asyncio.run(main())
