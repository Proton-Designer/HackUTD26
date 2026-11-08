import time,glob,os,subprocess,sys,json,math,base64,mimetypes
from playwright.sync_api import sync_playwright
ROOT="/Users/aymanmohammed/Documents/HackUTD26/web/customer"; OUT="/Users/aymanmohammed/Documents/HackUTD26/docs/app-screens/"; PORT=8771; B=f"http://127.0.0.1:{PORT}"
def ulaw(x):
    s=0x80 if x<0 else 0; x=min(abs(x)+132,32635); e=7; m=0x4000
    while e>0 and not (x&m): e-=1; m>>=1
    return ~(s|(e<<4)|((x>>(e+3))&15))&255
FR=json.dumps([base64.b64encode(bytes(ulaw(int(9000*math.sin(2*math.pi*300*(k*160+i)/8000))) for i in range(160))).decode() for k in range(50)])
INIT="""window.__F=@@;window.__sent=[];(()=>{const O=window.WebSocket;window.WebSocket=function(u,pr){if(/\\/(listen|talk)\\//.test(String(u))){const w={u:String(u),readyState:1,close(){clearInterval(w.t)},send(d){window.__sent.push(d)}};setTimeout(()=>{w.onopen&&w.onopen();let k=0;if(/listen/.test(w.u))w.t=setInterval(()=>{if(window.__play===false)return;k++;w.onmessage&&w.onmessage({data:JSON.stringify({track:'caller',payload:window.__F[k%50]})});w.onmessage&&w.onmessage({data:JSON.stringify({track:'decoy',payload:window.__F[(k+7)%50]})})},20)},30);return w}return new O(u,pr)};Object.assign(window.WebSocket,O)})();
navigator.mediaDevices.getUserMedia=async()=>{const c=new AudioContext(),o=c.createOscillator(),g=c.createGain(),d=c.createMediaStreamDestination();o.frequency.value=300;g.gain.value=0.4;window.__micGain=g;o.connect(g);g.connect(d);o.start();return d.stream};""".replace("@@",FR)
srv=subprocess.Popen([sys.executable,"-m","http.server",str(PORT),"--bind","127.0.0.1"],cwd=ROOT,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
state={"enroll":{"voice_id":"v_demo"}}
BLOCKED=[{"number":"+15555550123","reason":"Known scam campaign (IRS impersonation)","ts":time.time()-3600,"undo_token":"u1"},{"number":"+14695550100","reason":"Asked for a one-time code","ts":time.time()-86400,"undo_token":"u2"}]
CALLS=[{"call_id":"c1","from_number":"+15555550123","decision":"LIVE_GUARD","reason":"Caller ID not verified","ts":time.time()-3600}]*3
def hub(route):
    u=route.request.url; path=u.split(str(PORT),1)[1].split("?")[0]
    if path in("/demo/status",): return route.fulfill(status=200,content_type="application/json",body=json.dumps({"flags":{"MARIA_LEG":state.get("leg","")}}))
    if path=="/protection-log":
        if state.get("unpaired"): return route.fulfill(status=401,content_type="application/json",body='{"detail":"pair this device first"}')
        return route.fulfill(status=200,content_type="application/json",body=json.dumps({"blocked":state.get("blocked",BLOCKED),"calls":CALLS}))
    if path=="/voice/enroll": return route.fulfill(status=200,content_type="application/json",body=json.dumps(state["enroll"]))
    if path.startswith("/voice/") or path.startswith("/trusted"): return route.fulfill(status=200,content_type="application/json",body='{"ok":true}')
    if path in("/events",) or path.startswith("/voip") or path=="/pair": return route.abort()
    if path=="/demo/caller.wav": return route.fulfill(status=404)
    return route.continue_()
try:
    time.sleep(1)
    with sync_playwright() as p:
        c=sorted(glob.glob(os.path.expanduser("~/Library/Caches/ms-playwright/chromium-*/chrome-mac*/Chromium.app/Contents/MacOS/Chromium")))
        b=p.chromium.launch(executable_path=c[-1],args=["--use-fake-ui-for-media-stream","--use-fake-device-for-media-stream"])
        def mk(leg="",paired=True,query="",store=None,skip=True,mic=True,hint=False,dev="iPhone 13"):
            state["leg"]=leg; state["unpaired"]=not paired
            ctx=(b.new_context(**p.devices[dev],permissions=["microphone"]) if dev else b.new_context(viewport={"width":1280,"height":800},permissions=["microphone"])); pg=ctx.new_page()
            pg.add_init_script(("" if hint else "localStorage.setItem('bf.a2hs','1');")+INIT+("localStorage.setItem('bf.device','demo-token');" if paired else ""))
            if store: pg.add_init_script("".join(f"localStorage.setItem('bf.{k}','{v}');" for k,v in store.items()))
            pg.route(B+"/**",hub)
            pg.goto(B+"/index.html?server="+B+("&skipsetup" if skip else "")+query); time.sleep(1.3); return pg
        def shot(pg,name,full=False):
            pg.screenshot(path=OUT+name+".png",full_page=full); print("saved",name,flush=True)
        def call(pg,answered=True,cid="c1"):
            pg.evaluate(f"BF.deliver({{type:'call.incoming',call_id:'{cid}',ts:new Date().toISOString(),data:{{from:'+15555550123',attestation:'none',scam_id_score:0.8}}}})")
            pg.evaluate(f"BF.deliver({{type:'call.routed',call_id:'{cid}',data:{{decision:'LIVE_GUARD',reason:'Caller ID not verified'}}}})"); time.sleep(.5)
        def answered(pg,cid="c1"): pg.evaluate(f"BF.onEvent({{type:'call.answered',call_id:'{cid}',ts:new Date().toISOString(),data:{{by:'maria'}}}})")
        ev=lambda pg,t,d="{}",cid="c1": pg.evaluate(f"BF.deliver({{type:'{t}',call_id:'{cid}',ts:new Date().toISOString(),data:{d}}})")
        # 01 pair
        pg=mk(paired=False,skip=False); shot(pg,"01-pair"); pg.context.close()
        # onboarding
        pg=mk(skip=False); shot(pg,"02-onboarding-1-turn-on",True)
        pg.click("#s1on"); time.sleep(.4); shot(pg,"03-onboarding-2-voice-consent",True)
        pg.click("#s2agree"); time.sleep(.4); shot(pg,"04-onboarding-3-record-idle",True)
        pg.click("#recBtn"); time.sleep(4.2); shot(pg,"05-onboarding-4-recording-meter",True)
        pg.click("#recBtn"); time.sleep(.6); shot(pg,"06-onboarding-5-review",True)
        pg.click("#recSave"); time.sleep(1.2); shot(pg,"07-onboarding-6-saved-voice-set-up",True)
        pg.fill("#dnsNumber","(555) 555-0142"); pg.fill("#dnsLabel","Dr. Lee"); pg.click("#dnsAdd"); time.sleep(.3); shot(pg,"09-onboarding-7-do-not-screen-list",True)
        pg.click("#dnsDone"); time.sleep(.3); shot(pg,"10-onboarding-8-done",True); pg.context.close()
        # 08 synthetic fallback
        state["enroll"]={"voice_id":None,"fallback":"synthetic"}
        pg=mk(skip=False); pg.click("#s1on"); pg.click("#s2agree"); pg.click("#recBtn"); time.sleep(3.6); pg.click("#recBtn"); time.sleep(.5); pg.click("#recSave"); time.sleep(1.2); shot(pg,"08-onboarding-6b-voice-not-saved-synthetic",True); pg.context.close()
        state["enroll"]={"voice_id":"v_demo"}
        # idle / ring
        pg=mk(); shot(pg,"11-idle-live-guard-on"); call(pg); shot(pg,"12-incoming-ring-scam-likely"); pg.context.close()
        # listen mode active
        pg=mk(leg="listen"); call(pg); answered(pg); time.sleep(1.5); shot(pg,"13-active-listen-mode"); pg.context.close()
        # talk modes
        pg=mk(leg="talk"); call(pg); answered(pg); pg.evaluate("__play=false"); time.sleep(2.0); shot(pg,"14-active-talk-mic-dot-green")
        pg.click("#micBtn"); time.sleep(.6); shot(pg,"15-active-talk-muted"); pg.click("#micBtn"); pg.evaluate("__play=true"); time.sleep(.8)
        ev(pg,"alert.fired","{level:'first',why_chips:['Claims to be the IRS','Asks for a one-time code','Asks for card details','Known scam campaign']}"); time.sleep(.8); shot(pg,"17-alert-chips-three-buttons")
        ev(pg,"handoff.started"); time.sleep(1.5); shot(pg,"18-handed-off-listening-to-decoy")
        ev(pg,"handoff.restored"); time.sleep(1.0); shot(pg,"19-restored-back-on-the-call")
        ev(pg,"call.ended","{ended_by:'caller',duration_s:62}"); time.sleep(.5); shot(pg,"20-call-ended"); pg.context.close()
        # tap for sound: fresh page, blocked audio context
        pg=mk(leg="listen",query="&notap=1"); pg.add_init_script("") ; call(pg); answered(pg); time.sleep(1.5)
        pg.evaluate("(()=>{const b=document.getElementById('sound');b.textContent='🔇 Tap for sound';b.classList.add('off')})()"); shot(pg,"16-active-tap-for-sound-badge"); pg.context.close()
        # protection
        pg=mk(store={"voice":"v_demo"}); pg.evaluate("BF.view('protView')"); time.sleep(1); shot(pg,"21-protection-tab",True)
        pg.click("#dnsOpen"); time.sleep(.4); shot(pg,"22-protection-do-not-screen-manage",True); pg.context.close()
        # PWA / observer / desktop
        pg=mk(hint=True); shot(pg,"24-add-to-home-screen-hint"); pg.context.close()
        pg=mk(leg="talk"); pg.add_init_script(""); call(pg); answered(pg); time.sleep(.8)
        pg.evaluate("(()=>{BF.observer=true;document.getElementById('talkBox').hidden=true;document.getElementById('observerMsg').hidden=false})()")
        ev(pg,"alert.fired","{level:'first',engine:'server',why_chips:['Claims to be the IRS','Asks for a one-time code']}"); ev(pg,"user.action","{action:'scammer_get_scammed',by:'android phone'}"); time.sleep(.5); shot(pg,"25-observer-other-phone-answering"); pg.context.close()
        pg=mk(dev=None); call(pg); shot(pg,"26-desktop-phone-frame-ring"); pg.context.close()
        # judge
        pj=b.new_context(**p.devices["iPhone 13"]).new_page(); pj.goto(B+"/judge.html"); time.sleep(1); pj.screenshot(path=OUT+"23-judge-card.png",full_page=True); print("saved judge")
finally: srv.terminate()
