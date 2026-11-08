"""Blind scorer for run_ab.py output. Judge = a third model (llama-3.1-nemotron-70b-instruct, T0), shown the scam context, the
scammer's last line and ONE reply with a shuffled id (no model label). Code checks: length (<=2 sentences/<=35 words) and leak/AI.
Usage: python -m detection.eval.decoy_ab.score_ab in.json out.json"""
import asyncio, json, random, re, statistics, sys
from decoy import core
import os
JUDGE = os.environ.get("JUDGE_MODEL", "nvidia/nemotron-3.5-lightning-30b-a3b")   # llama-nemotron 70b/253b/340b ids list but 404 on chat
RUBRIC = """You grade ONE reply from a decoy on a scam phone call. The decoy plays a worried, cooperative, slightly slow person who believes the scammer, keeps them talking, and tries to get the scammer to state their payment handle / account / callback number / website. The reply is spoken aloud on a phone.
Score each 0, 1 or 2:
character: stays a believable ordinary person on the phone (2), slightly off (1), breaks character or sounds like an assistant/narrator (0).
natural: sounds like real speech and answers what the scammer just said (2), awkward/generic (1), nonsensical or parrots a stock phrase (0).
on_goal: stalls AND moves toward extracting the scammer's details (how/where to pay, handle, callback, site) without inventing details (2), partly (1), no progress or invents a payee/app/amount the scammer never said (0).
Return ONLY JSON: {"character":n,"natural":n,"on_goal":n}"""

def code_checks(row):
    t = row.get("hist") or row.get("raw") or ""
    sp = row.get("spoken") or ""
    sents = [s for s in re.split(r"(?<=[.!?])\s+", sp) if s.strip()]
    words = len(sp.split())
    length = 2 if (len(sents) <= 2 and words <= 35) else (1 if len(sents) <= 3 and words <= 50 else 0)
    leak = 0 if (re.search(r"\b(as an ai|language model|i am an ai|i'm an ai|chatbot|\[NAME\] )", t, re.I) or re.search(r"\d{5,}", t)) else 2
    return length, leak

async def main():
    d = json.load(open(sys.argv[1])); items = []
    for cid, c in d.items():
        if cid in ('3', '9'): continue   # cards pulled from the judge bucket (P4b #113)
        for label, rows in c["variants"].items():
            for r in rows: items.append({"card": cid, "label": label, "row": r})
    ids = list(range(len(items))); random.Random(7).shuffle(ids)
    out = []
    for k in ids:
        it = items[k]; r = it["row"]
        if not r.get("spoken"):
            out.append({**{x: it[x] for x in ("card", "label")}, "turn": r["turn"], "failed": True, "ms": r["ms"]}); continue
        length, leak = code_checks(r)
        msg = [{"role": "system", "content": RUBRIC},
               {"role": "user", "content": f'Scam type: {r["scam"]}.\nScammer just said: "{r["scammer"]}"\nDecoy reply: "{r["spoken"]}"'}]
        sc = None
        for _ in range(3):
            o = await core.chat(msg, max_tokens=60, temperature=0.0, model=JUDGE)
            m = re.search(r"\{.*?\}", o or "", re.S)
            try: sc = json.loads(m.group(0)); break
            except Exception: await asyncio.sleep(1.5)
        await asyncio.sleep(1.0)
        out.append({"card": it["card"], "label": it["label"], "turn": r["turn"], "spoken": r["spoken"], "scammer": r["scammer"], "ms": r["ms"],
                    "character": (sc or {}).get("character"), "natural": (sc or {}).get("natural"), "on_goal": (sc or {}).get("on_goal"),
                    "length": length, "leak": leak})
    json.dump(out, open(sys.argv[2], "w"), indent=1)
    labels = sorted({o["label"] for o in out})
    for lab in labels:
        rs = [o for o in out if o["label"] == lab]; ok = [o for o in rs if not o.get("failed") and o.get("character") is not None]
        ms = sorted(o["ms"] for o in rs if not o.get("failed"))
        mean = lambda k: round(statistics.mean(o[k] for o in ok), 2)
        tot = [sum(o[k] for k in ("character", "natural", "on_goal", "length", "leak")) for o in ok]
        print(lab, "n", len(rs), "failed", len(rs) - len(ok), {k: mean(k) for k in ("character", "natural", "on_goal", "length", "leak")},
              "total/10", round(statistics.mean(tot), 2), "p50/p90 ms", ms[len(ms) // 2], ms[int(len(ms) * 0.9)])
asyncio.run(main())
