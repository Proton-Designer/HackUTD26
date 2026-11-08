"""Known-campaign similarity: char n-gram TF-IDF (numpy) of window sentences vs caller lines of confirmed scam scripts.
Corpus = data/script-cards.md + dev-split scam rows of data/eval/scripts.jsonl (test split is held out of the eval).
A campaign hit needs >=2 distinct sentences each matching a line of the SAME script (so one generic opener never fires)."""
from __future__ import annotations
import json, re
from pathlib import Path
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
SIM_THRESHOLD = 0.65
MIN_LINES = 2
BOOST = 0.1
CHIP = "Known scam campaign"
N = (3, 4)

_IDX = None


def _grams(text: str) -> dict:
    t = " " + " ".join(re.sub(r"[^a-z0-9$ ]", " ", text.lower()).split()) + " "
    g = {}
    for n in N:
        for i in range(len(t) - n + 1):
            g[t[i:i + n]] = g.get(t[i:i + n], 0) + 1
    return g


def _sentences(text: str) -> list[str]:
    return [s.strip() for s in re.split(r"(?<=[.!?])\s+", text) if len(s.strip()) >= 12]


def _corpus() -> list[tuple[str, str]]:
    rows = []
    try:
        cards = re.split(r"^# Card \d+:.*$", (ROOT / "data/script-cards.md").read_text(), flags=re.M)[1:]
        for i, c in enumerate(cards):
            lines = re.findall(r'^\d\. \*\*"(.+?)"\*\*', c, re.M) + re.findall(r'### Payment step\s+\*\*"(.+?)"\*\*', c, re.S)
            rows += [(f"card{i + 1}", l) for l in lines]
    except Exception:
        pass
    try:
        for line in (ROOT / "data/eval/scripts.jsonl").read_text().splitlines():
            r = json.loads(line)
            if r.get("label") == "scam" and r.get("split") == "dev":
                rows += [(r["id"], l) for l in r.get("caller_lines", [])]
    except Exception:
        pass
    return [(sid, s) for sid, l in rows for s in (_sentences(l) or [l])]


def _build():
    global _IDX
    rows = _corpus()
    docs = [_grams(l) for _, l in rows]
    vocab = {}
    for d in docs:
        for g in d:
            vocab.setdefault(g, len(vocab))
    df = np.zeros(len(vocab))
    for d in docs:
        for g in d:
            df[vocab[g]] += 1
    idf = np.log((1 + len(docs)) / (1 + df)) + 1
    M = np.zeros((len(docs), len(vocab)), dtype=np.float32)
    for i, d in enumerate(docs):
        for g, c in d.items():
            M[i, vocab[g]] = c * idf[vocab[g]]
    M /= np.maximum(np.linalg.norm(M, axis=1, keepdims=True), 1e-9)
    _IDX = (M, vocab, idf, [s for s, _ in rows])


def match(window_text: str) -> str | None:
    """Return the matched script id, or None. Cheap, no I/O after first call."""
    global _IDX
    try:
        if _IDX is None:
            _build()
        M, vocab, idf, ids = _IDX
        if not len(ids):
            return None
        hits: dict[str, set] = {}
        for si, sent in enumerate(_sentences(window_text or "")):
            v = np.zeros(len(vocab), dtype=np.float32)
            for g, c in _grams(sent).items():
                j = vocab.get(g)
                if j is not None:
                    v[j] = c * idf[j]
            nv = np.linalg.norm(v)
            if nv == 0:
                continue
            sims = M @ (v / nv)
            j = int(np.argmax(sims))
            if sims[j] >= SIM_THRESHOLD:
                hits.setdefault(ids[j], set()).add(si)
        for sid, s in hits.items():
            if len(s) >= MIN_LINES:
                return sid
    except Exception:
        return None
    return None
