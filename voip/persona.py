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

def standin_mode() -> str:
    return "echo" if os.environ.get("DECOY_STANDIN", "persona").strip().lower() == "echo" else "persona"

@router.websocket("/decoy-standin/{call_id}")
@router.websocket("/decoy/{call_id}")   # alias: P3_DECOY_URL=ws://127.0.0.1:<hub port> makes the relay use the persona with no relay change
async def decoy_standin(ws: WebSocket, call_id: str):
    """Built-in stand-in decoy (SIMULATED). Plays the persona lines in real time with silence between, looping until the call ends."""
    await ws.accept()
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
    finally: rx.cancel()
