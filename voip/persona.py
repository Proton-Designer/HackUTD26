"""Stand-in decoy persona (SIMULATED): when no real P3 decoy is configured, play a few pre-generated "confused elderly Maria" lines to the caller
instead of echoing the scammer. Synthetic voice (macOS say + ffmpeg -> raw PCMU 8 kHz), generated once into logs/decoy_lines/ (gitignored).
Served as WS /decoy-standin/{call_id} speaking the same frames as P3 (media events with base64 PCMU payload). Env DECOY_STANDIN=persona|echo
(default persona); server/relay.py picks the URL (see wip/eng2-relay-persona.patch.txt). Fail open: if audio can't be generated, it stays silent."""
import asyncio, base64, json, logging, os, pathlib, shutil, subprocess
from fastapi import APIRouter, WebSocket, WebSocketDisconnect

log = logging.getLogger("voip.persona")
router = APIRouter()
ROOT = pathlib.Path(__file__).resolve().parent.parent
LINES = [  # synthetic; no real people
    "Oh dear, which card did you say?",
    "Hold on, let me find my glasses.",
    "Can you spell that again for me, dear?",
    "I am sorry, I do not hear so well. Could you say that slower?",
    "My grandson usually helps me with this. Is that alright?",
    "Oh my. Where do I find the numbers on the back?",
]
GAP_S = float(os.environ.get("DECOY_LINE_GAP_S", "2.5"))
FRAME_BYTES = 160   # 20 ms of PCMU 8 kHz

def lines_dir() -> pathlib.Path:
    d = pathlib.Path(os.environ.get("DECOY_LINES_DIR") or (ROOT / "logs" / "decoy_lines")); d.mkdir(parents=True, exist_ok=True); return d

def generate_lines(force=False) -> list[pathlib.Path]:
    """Generate each line once (raw PCMU, 8 kHz mono). Returns the existing/created files; [] when say/ffmpeg are unavailable."""
    d = lines_dir(); out = []
    for i, text in enumerate(LINES):
        f = d / f"line{i}.ulaw"
        if force or not f.is_file() or f.stat().st_size < FRAME_BYTES:
            if not (shutil.which("say") and shutil.which("ffmpeg")): continue
            aiff = d / f"line{i}.aiff"
            try:
                subprocess.run(["say", "-v", "Samantha", "-r", "140", "-o", str(aiff), text], check=True, capture_output=True)
                subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(aiff), "-ar", "8000", "-ac", "1", "-f", "mulaw", str(f)], check=True)
            except Exception as e:
                log.warning("persona line %d not generated: %s", i, e); continue
            finally: aiff.unlink(missing_ok=True)
        if f.is_file() and f.stat().st_size >= FRAME_BYTES: out.append(f)
    return out

HELLO_TEXT = "Hello? ... Yes?"

def generate_hello(force=False):
    """MARIA_LEG=listen greeting: raw PCMU 8 kHz in lines_dir()/hello.ulaw (generated once). None when say/ffmpeg are unavailable."""
    f = lines_dir() / "hello.ulaw"
    if force or not f.is_file() or f.stat().st_size < FRAME_BYTES:
        if not (shutil.which("say") and shutil.which("ffmpeg")): return None
        aiff = f.with_suffix(".aiff")
        try:
            subprocess.run(["say", "-v", "Samantha", "-r", "140", "-o", str(aiff), HELLO_TEXT], check=True, capture_output=True)
            subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(aiff), "-ar", "8000", "-ac", "1", "-f", "mulaw", str(f)], check=True)
        except Exception as e:
            log.warning("hello line not generated: %s", e); return None
        finally: aiff.unlink(missing_ok=True)
    return f if f.is_file() and f.stat().st_size >= FRAME_BYTES else None

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
