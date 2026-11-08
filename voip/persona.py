"""Stand-in decoy persona (SIMULATED): when no real P3 decoy is configured, play a few pre-generated neutral, name-free lines to the caller
instead of echoing the scammer. Synthetic voice (macOS say + ffmpeg -> raw PCMU 8 kHz), generated once into logs/decoy_lines/ (gitignored).
Served as WS /decoy-standin/{call_id} speaking the same frames as P3 (media events with base64 PCMU payload). Env DECOY_STANDIN=persona|echo
(default persona); server/relay.py picks the URL (see wip/eng2-relay-persona.patch.txt). Fail open: if audio can't be generated, it stays silent."""
import asyncio, base64, hashlib, json, logging, os, pathlib, shutil, subprocess, time
from fastapi import APIRouter, WebSocket, WebSocketDisconnect

log = logging.getLogger("voip.persona")
router = APIRouter()
ROOT = pathlib.Path(__file__).resolve().parent.parent
LINES = [  # synthetic; neutral adult, name-free and persona-free (no age, family or backstory)
    "Sorry, which card did you say?",
    "Hold on a second, let me grab that.",
    "Can you spell that again for me?",
    "I'm sorry, the line is bad. Could you say that a little slower?",
    "Okay, give me a moment to write that down.",
    "Right... where do I find the numbers on the back?",
]
GAP_S = float(os.environ.get("DECOY_LINE_GAP_S", "2.5"))
FRAME_BYTES = 160   # 20 ms of PCMU 8 kHz

def lines_dir() -> pathlib.Path:
    d = pathlib.Path(os.environ.get("DECOY_LINES_DIR") or (ROOT / "logs" / "decoy_lines")); d.mkdir(parents=True, exist_ok=True); return d

# Voice: no Enhanced/Premium macOS voices are installed here, so default to "Grandma (English (US))" (the newer, softer elderly-woman
# voice; far less robotic than Samantha) and fall back to Samantha if `say` rejects it. Env DECOY_VOICE / DECOY_RATE override.
VOICE_PREF = ("Grandma (English (US))", "Samantha")
def _voice() -> str: return os.environ.get("DECOY_VOICE") or VOICE_PREF[0]
def _rate() -> str: return os.environ.get("DECOY_RATE", "135")

def _magpie_py():
    """decoy/.venv's python (has the Riva client), only if Magpie is usable here: key set, venv present, not disabled."""
    py = ROOT / "decoy" / ".venv" / "bin" / "python"
    return py if (py.is_file() and os.environ.get("NVIDIA_API_KEY") and os.environ.get("DECOY_TTS", "magpie").lower() != "say") else None

def _tag() -> str:
    """Which voice we ask for: the enrolled clone (decoy/voices) if present, else synthetic Magpie, else macOS say."""
    if _magpie_py():
        try:
            d = pathlib.Path(os.environ.get("DECOY_VOICES_DIR") or (ROOT / "decoy" / "voices"))
            m = json.loads((d / "voices.json").read_text()); vid = max(m, key=lambda k: m[k]["ts"])
            if (d / f"{vid}.wav").exists(): return f"magpie-clone:{vid}"
        except Exception: pass
        return "magpie:" + os.environ.get("DECOY_SYNTH_VOICE", "Magpie-Multilingual.EN-US.Aria.Calm")
    return f"say:{_voice()}|{_rate()}"

FALLBACK_RETRY_S = 600   # a 'say' fallback produced while Magpie was failing is reused this long before Magpie is retried

def _key(text: str) -> str:
    """Cache key: text + voice engine/tag. Files are rebuilt whenever any of them changes."""
    return hashlib.sha1(f"{_tag()}|{text}".encode()).hexdigest()[:16]

def _synth_magpie(text: str, f: pathlib.Path) -> bool:
    py = _magpie_py()
    if not py: return False
    try:
        tmp = f.with_suffix(".tmp")
        r = subprocess.run([str(py), str(ROOT / "voip" / "magpie_tts.py"), str(tmp), text], capture_output=True, timeout=30)
        if r.returncode == 0 and tmp.is_file() and tmp.stat().st_size >= FRAME_BYTES:
            tmp.replace(f); return True
        log.warning("Magpie TTS failed (rc=%s); falling back to say", r.returncode)
    except Exception as e:
        log.warning("Magpie TTS error (%s); falling back to say", type(e).__name__)
    f.with_suffix(".tmp").unlink(missing_ok=True); return False

def _synth(text: str, f: pathlib.Path, force=False) -> bool:
    """NVIDIA Magpie (preferred) else macOS say -> raw PCMU 8 kHz at f (+ f.key). Cached by _key. False when unavailable."""
    kf = f.with_suffix(".key"); key = _key(text); have = f.is_file() and f.stat().st_size >= FRAME_BYTES
    if not force and have and kf.is_file():
        k = kf.read_text()
        if k == key: return True
        if k == key + "|fb" and time.time() - kf.stat().st_mtime < FALLBACK_RETRY_S: return True
    if _synth_magpie(text, f):
        kf.write_text(key); return True
    if not (shutil.which("say") and shutil.which("ffmpeg")): return have   # keep any older file
    aiff = f.with_suffix(".aiff")
    try:
        for v in dict.fromkeys([_voice(), VOICE_PREF[1]]):
            r = subprocess.run(["say", "-v", v, "-r", _rate(), "-o", str(aiff), text], capture_output=True)
            if r.returncode == 0 and aiff.is_file() and aiff.stat().st_size > 1000: break
        else: raise RuntimeError("say failed for every voice")
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(aiff), "-af", "lowpass=f=3400,highpass=f=120,loudnorm=I=-20:TP=-3,adelay=150|150",
                        "-ar", "8000", "-ac", "1", "-f", "mulaw", str(f)], check=True)
        kf.write_text(key + ("|fb" if _magpie_py() else ""))   # fallback while Magpie is configured: retry Magpie after FALLBACK_RETRY_S
        return True
    except Exception as e:
        log.warning("persona audio %s not generated: %s", f.name, e); return False
    finally: aiff.unlink(missing_ok=True)

def generate_lines(force=False) -> list[pathlib.Path]:
    """Generate each line once per (voice, rate, text). Returns the files; [] when say/ffmpeg are unavailable."""
    d = lines_dir(); out = []
    for i, text in enumerate(LINES):
        f = d / f"line{i}.ulaw"
        if _synth(text, f, force) and f.is_file() and f.stat().st_size >= FRAME_BYTES: out.append(f)
    return out

HELLO_TEXT = "Hello? ... Yes, this is Maria."   # default; the live text comes from hello_text() (env CUSTOMER_NAME)

def hello_text() -> str:
    """Greeting for MARIA_LEG=listen/talk: 'Hello? ... Yes, this is <CUSTOMER_NAME>.' or just 'Hello?' when the name is empty. Cosmetic: ids/enums stay 'maria'."""
    n = os.environ.get("CUSTOMER_NAME")
    n = "Maria" if n is None else "".join(ch for ch in n if ch.isalnum() or ch in " .'-").strip()[:40]
    return f"Hello? ... Yes, this is {n}." if n else "Hello?"

def cached_hello():
    """The cached greeting file if there is one (regardless of cache key), else None. Instant; used at call time."""
    f = lines_dir() / "hello.ulaw"
    if not (f.is_file() and f.stat().st_size >= FRAME_BYTES):
        return None
    try:   # a rename must not play the old name from the cache: only reuse a file synthesized from the current text
        if (lines_dir() / "hello.txt").read_text() != hello_text(): return None
    except Exception:
        if hello_text() != HELLO_TEXT: return None
    return f

def generate_hello(force=False):
    """MARIA_LEG=listen greeting: raw PCMU 8 kHz in lines_dir()/hello.ulaw (rebuilt when voice/rate/text change). None when unavailable."""
    f = lines_dir() / "hello.ulaw"
    text = hello_text()
    ok = _synth(text, f, force) and f.is_file() and f.stat().st_size >= FRAME_BYTES
    if ok:
        try: (lines_dir() / "hello.txt").write_text(text)
        except Exception: pass
    return f if ok else None

def standin_mode() -> str:
    return "echo" if os.environ.get("DECOY_STANDIN", "persona").strip().lower() == "echo" else "persona"

_gen_lock = None
_active = 0
MAX_CONC = 4

async def decoy_standin(ws: WebSocket, call_id: str):
    global _gen_lock, _active
    """Built-in stand-in decoy (SIMULATED). Plays the persona lines in real time with silence between, looping until the call ends."""
    from . import router as _r   # lazy: voip.router imports this module
    if not (_r.direct_local(ws) and call_id in _r.CALLS and not _r.CALLS[call_id].get("ended")) or _active >= MAX_CONC:
        await ws.close(code=1008); return   # only the hub's own relay (direct loopback, no tunnel headers) for a live call it knows
    await ws.accept(); _active += 1
    if _gen_lock is None: _gen_lock = asyncio.Lock()
    async with _gen_lock:   # say/ffmpeg at most once at a time; files are cached on disk afterwards
        files = await asyncio.get_running_loop().run_in_executor(None, generate_lines)
    if not files: log.warning("persona decoy: no audio available (say/ffmpeg missing?); staying silent")
    async def drain():   # keep reading so a close from the relay ends us promptly
        try:
            while True: await ws.receive_text()
        except (WebSocketDisconnect, RuntimeError): pass
    rx = asyncio.create_task(drain())
    try:
        i = 0
        while files and not rx.done():
            data = files[i % len(files)].read_bytes(); i += 1
            for k in range(0, len(data), FRAME_BYTES):
                if rx.done(): return
                await ws.send_text(json.dumps({"event": "media", "media": {"payload": base64.b64encode(data[k:k + FRAME_BYTES]).decode()}}))
                await asyncio.sleep(0.02)
            end = asyncio.get_running_loop().time() + GAP_S
            while asyncio.get_running_loop().time() < end:
                if rx.done(): return
                await asyncio.sleep(0.1)
        if not files: await rx
    except (WebSocketDisconnect, RuntimeError): pass
    finally:
        rx.cancel(); _active -= 1

router.add_api_websocket_route("/decoy-standin/{call_id}", decoy_standin)
if os.environ.get("DECOY_PERSONA_ALIAS") == "1":   # only when P3 is deliberately substituted: P3_DECOY_URL=ws://127.0.0.1:<hub port> -> /decoy/{call_id}
    router.add_api_websocket_route("/decoy/{call_id}", decoy_standin)
