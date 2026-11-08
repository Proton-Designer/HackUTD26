// Command-center alert-path check (TASK-078, eng1). Drives the REAL web/command-center/app.js + index.html in jsdom with a mock
// WebSocket (no hub, no browser, nothing posted anywhere). Prints headline / hero class / risk panel for: watch -> alert -> HELD
// (s=0.60, band critical) -> control (0.60, band watch) -> handoff -> restored. Expect: held keeps the red headline, meter at the peak,
// "alert held for this call"; control shows "detector score 0.60"; after restored the headline must NOT still say the decoy has the call (#106).
// Run (repo root):  mkdir -p /tmp/ccj && cd /tmp/ccj && npm i jsdom && cd -
//   .venv/bin/python -m http.server 8103 --bind 127.0.0.1 &  (note the PID; kill only that PID afterwards)
//   NODE_PATH=/tmp/ccj/node_modules node detection/eval/tools/cc_alert_harness.js
const {JSDOM,ResourceLoader,VirtualConsole}=require('jsdom');
const U='http://localhost:8103/web/command-center/?server=http://localhost:8193&src=live';
let ws=null;
const vc=new VirtualConsole(); vc.on('jsdomError',e=>{if(!/Could not parse CSS|not implemented/i.test(e.message))console.log('ERR',e.message.slice(0,120))});
JSDOM.fromURL(U,{runScripts:'dangerously',resources:'usable',pretendToBeVisual:true,virtualConsole:vc,beforeParse(w){
  w.WebSocket=class{constructor(u){ws=this;this.url=u;setTimeout(()=>{this.readyState=1;this.onopen&&this.onopen({})},20)}send(){}close(){}};
  w.fetch=()=>Promise.reject(new Error('no net')); w.scrollTo=()=>{}; w.HTMLElement.prototype.scrollIntoView=()=>{}; w.matchMedia=w.matchMedia||(()=>({matches:false,addListener(){},addEventListener(){}}));
}}).then(async dom=>{
  const w=dom.window,d=w.document; const sleep=ms=>new Promise(r=>setTimeout(r,ms));
  await sleep(1500);
  const hist=[]; new w.MutationObserver(()=>hist.push(d.getElementById('headline').textContent.replace(/\s+/g,' ').slice(0,70)+' ['+d.getElementById('hero').className+']')).observe(d.getElementById('hero'),{childList:true,subtree:true,characterData:true,attributes:true});
  const C='c_chk'; let n=0;
  const send=(type,data)=>ws.onmessage({data:JSON.stringify({type,call_id:C,ts:Date.now()/1000+(n++)*0.4,data})});
  const risk=(s,band,asks,why)=>({s,band,asks,why_chips:why,engine:'local',model:'nemotron-nano-4b',scam_type:'bank_fraud',stage:'pressure',impersonates:'Chase',addresses_ai_system:false});
  const q=(sel,f)=>{const e=d.querySelector(sel);return e?f(e):null};
  const snap=async name=>{await sleep(700);console.log('\n== '+name);console.log(' headline:',d.getElementById('headline').textContent.replace(/\s+/g,' ').trim().slice(0,90));console.log(' hero class:',d.getElementById('hero').className,'| sub:',(d.getElementById('subline').textContent||'').slice(0,70));
   console.log(' risk panel: class=',q('.risk',e=>e.className),'| band=',q('.risk .band',e=>e.textContent),'| num=',q('.risk .num',e=>e.textContent),'| meter=',q('.risk .meter i',e=>e.style.width),'| tag=',q('.alert-tag',e=>e.textContent));};
  send('call.incoming',{from:'+15125550101',to:'+15125550102',attestation:'C',scam_id_score:0.6});send('call.routed',{decision:'LIVE_GUARD',reason:'x'});send('call.answered',{by:'customer'});
  send('transcript.caller',{utterance_id:'u1',text:'This is your bank fraud team.',is_final:true});send('risk.update',risk(0.47,'watch',[],['Claims to be a bank']));await snap('1 watch 0.47');
  send('risk.update',risk(0.97,'critical',['ssn'],['Asks for SSN','Claims to be a bank']));send('alert.fired',{level:'first',why_chips:['Asks for SSN']});await snap('2 alert critical 0.97');
  send('risk.update',risk(0.60,'critical',['ssn'],['Asks for SSN']));await snap('3 HELD s=0.60 band=critical');
  send('risk.update',risk(0.60,'critical',['ssn'],['Asks for SSN']));await snap('3b HELD again');
  send('risk.update',risk(0.60,'watch',[],[]));await snap('3c CONTROL s=0.60 band=watch (not held)');
  send('risk.update',risk(0.60,'critical',['ssn'],['Asks for SSN']));
  send('user.action',{action:'scammer_get_scammed'});send('handoff.started',{restore_deadline:new Date(Date.now()+40000).toISOString()});await snap('4 handoff (held score)');
  send('risk.update',risk(0.60,'critical',['ssn'],['Asks for SSN']));await snap('4b held risk.update during handoff');
  send('handoff.restored',{});send('risk.update',risk(0.05,'low',[],[]));await snap('5 restored, low');
  console.log('\nHEADLINE/HERO CHANGES (flicker check):');hist.forEach((h,i)=>console.log(' ',i,h));
  process.exit(0);
}).catch(e=>{console.log('FAIL',e);process.exit(1)});
