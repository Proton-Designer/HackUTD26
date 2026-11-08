import asyncio, json, sys
from detection.detect import detect, quick
L = [
 "As you asked, send the wire now to the account I gave you.",
 "You asked how to fix this, so just send the wire transfer today and read me the confirmation.",
 "No le diga a nadie, compre las tarjetas de regalo y lea los números.",
 "Nunca se lo diremos a nadie, pero ahora compre las tarjetas de regalo y dígame los códigos.",
 "We don't need your PIN, we just need you to wire $4,000 to the secure account right now.",
 "You wondered about the wire, well, the wire transfer must go out within the hour or you will be arrested.",
 "No es una estafa, no le vamos a molestar, pero necesito que envíe una transferencia ahora mismo.",
 "I will not ask twice: read me the six digit code we just texted you.",
 "Your cousin asked if you could send bitcoin, so go to the ATM and send the crypto now, the agent will stay on the line.",
 "Jamás le pediremos dinero. Ahora necesito que me dé su número de seguro social completo.",
]
async def main():
    for i, t in enumerate(L, 1):
        q = quick(t) if True else None
        try: r = await detect(f"adv{i}", t, {}, "local")
        except Exception as e: r = {"err": type(e).__name__}
        print(i, "rules s=%.2f asks=%s" % (q.get("s", q.get("score", -1)), q.get("asks")), "| local s=%.2f asks=%s eng=%s" % (r.get("s", -1), r.get("asks"), r.get("engine")))
asyncio.run(main())
