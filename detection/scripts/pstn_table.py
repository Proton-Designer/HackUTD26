"""Render pstn_cards.py JSON rows (riva and/or whisper) into the markdown tables of detection/eval/PSTN_CARDS.md. Usage: pstn_table.py rows.json [rows2.json ...]"""
import json, sys
def main(paths):
    rows = [r for p in paths for r in json.load(open(p))]
    out = ["| card | stt | variant | words matched | finals/lines | max s | alert vs first-ask line end (s) | final latency (s) | ask line |", "|---|---|---|---|---|---|---|---|---|"]
    for r in rows:
        al = "NO ALERT" if not r["fired"] else ("n/a" if r["alert"] is None else f"{r['alert']:+.2f}")
        out.append(f"| {r['card']} {r['title']} | {r['stt']} | {r['variant']} | {r['words']:.0%} | {r['finals']}/{r['lines']} | {r['smax']:.2f} | {al} | {'n/a' if r['lat'] is None else format(r['lat'], '.2f')} | {r['ask_line'] or '-'} |")
    sc = [r for r in rows if r["card"].startswith("s")]; bn = [r for r in rows if r["card"].startswith("b")]
    out += ["", f"scam rows: {len(sc)}, alerted: {sum(r['fired'] for r in sc)}; benign rows: {len(bn)}, false alarms: {sum(r['fired'] for r in bn)} (max s {max([r['smax'] for r in bn] or [0]):.2f})"]
    print("\n".join(out))
main(sys.argv[1:])
