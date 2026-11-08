"""G.711 mu-law <-> 16-bit PCM without audioop (removed in Python 3.13)."""
import array

_BIAS, _CLIP = 0x84, 32635


def _enc(s: int) -> int:
    sign = 0x80 if s < 0 else 0
    s = min(abs(s), _CLIP) + _BIAS
    exp = s.bit_length() - 8
    mant = (s >> (exp + 3)) & 0x0F
    return ~(sign | (exp << 4) | mant) & 0xFF


def _dec(u: int) -> int:
    u = ~u & 0xFF
    t = (((u & 0x0F) << 3) + _BIAS) << ((u & 0x70) >> 4)
    return (_BIAS - t) if (u & 0x80) else (t - _BIAS)


_ENC = bytes(_enc(i - 65536 if i >= 32768 else i) for i in range(65536))  # index = sample & 0xFFFF
_DEC = array.array("h", (_dec(u) for u in range(256)))


def encode(pcm16le: bytes) -> bytes:
    """16-bit little-endian PCM -> mu-law bytes (one per sample)."""
    a = array.array("h")
    a.frombytes(pcm16le[: len(pcm16le) & ~1])
    return bytes(_ENC[s & 0xFFFF] for s in a)


def decode(ulaw: bytes) -> bytes:
    """mu-law bytes -> 16-bit little-endian PCM."""
    return array.array("h", (_DEC[b] for b in ulaw)).tobytes()
