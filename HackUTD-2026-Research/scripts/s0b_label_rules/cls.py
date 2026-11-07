import json,re
D='/Users/aymanmohammed/Documents/HackUTD-2026-Research/data/processed/'
rows=[json.loads(l) for l in open(D+'prize_labels_input_part00.jsonl')]
HK={'T-Mobile','AT&T','PNC Bank','Goldman Sachs','Capital One','Toyota Financial Services','State Farm','CBRE','EOG Resources','NVIDIA','NMC2','8090 AI','Niantic Spatial','Spacetime','Axxess','Winstead PC','Photon'}
# key -> (Sponsor, industry)
S=[('pnc','PNC Bank','finance_banking'),('state ?farm','State Farm','insurance'),('goldman','Goldman Sachs','finance_banking'),
('northmark','NMC2','cloud_devtools'),('nvidia','NVIDIA','ai_compute'),('eog','EOG Resources','energy'),('cbre','CBRE','real_estate'),
('toyota financial','Toyota Financial Services','finance_banking'),('toyota','Toyota','auto_mobility'),('t-mobile','T-Mobile','telecom'),
('capital one','Capital One','finance_banking'),('infosys','Infosys','other'),('samba ?nova','SambaNova','ai_compute'),('pinata','Pinata','cloud_devtools'),
('veolia','Veolia','other'),('frontier','Frontier','telecom'),('interview cake','Interview Cake','other'),('next step','Next Step','other'),
('photon','Photon','cloud_devtools'),('spacetime','Spacetime','cloud_devtools'),('niantic','Niantic Spatial','geospatial_ar'),
('livekit','LiveKit','cloud_devtools'),('cartesia','Cartesia','ai_compute'),('microsoft','Microsoft','cloud_devtools'),('convex','Convex','cloud_devtools'),
('apify','Apify','cloud_devtools'),('moss','Moss','cloud_devtools'),('anthropic','Anthropic','ai_compute'),('scrapybara','Scrapybara','ai_compute'),
('tesla','Tesla','auto_mobility'),('openevidence','OpenEvidence','health'),('suno','Suno','ai_compute'),('openai','OpenAI','ai_compute'),
('eigen','EigenCloud','cloud_devtools'),('elastic','Elastic','cloud_devtools'),('dimensional','Dimensional','cloud_devtools'),('asus','ASUS','other'),
('maximor','Maximor AI','finance_banking'),('dropbox','Dropbox','cloud_devtools'),('givecampus','GiveCampus','other'),('regeneron','Regeneron','health'),
('hackster','Hackster','other'),('arduino','Arduino','other'),('meta ','Meta','other'),('espressif','Espressif','other'),('ramp','Ramp','finance_banking'),
('long lake','Long Lake','ai_compute'),('elevenlabs','ElevenLabs','ai_compute'),('fetch','Fetch.ai','ai_compute'),('dain','DAIN','ai_compute'),
('gemini','Google','ai_compute'),('cognition','Cognition','ai_compute'),('figma','Figma','cloud_devtools'),('prizepicks','PrizePicks','other'),
('aramco','Aramco','energy'),('impiricus','Impiricus','health'),('notability','Notability','other'),('nsa','NSA','security_privacy'),
('visa','Visa','finance_banking'),('sideshift','SideShift','other'),('perceptron','Perceptron','ai_compute'),('veyzl','VEYZL','other'),
('spacexai','SpaceXAI','ai_compute'),('bloomberg','Bloomberg','finance_banking'),('ambrook','Ambrook','finance_banking'),('featherless','Featherless','ai_compute'),
('drw','DRW','finance_banking'),('druide','Druide','other'),("taile'd",'TAILE\'D','other'),('desjardins','Desjardins','finance_banking'),('deck -','Deck','other'),
('sap ','SAP','cloud_devtools'),('d3 security','D3 Security','security_privacy'),('beenox','Beenox','other'),('mentormates','MentorMates','other'),
('dialogue','Dialogue','health'),('talsom','Talsom','other'),('front row','Front Row Ventures','finance_banking'),('nobel era','Nobel Era Group','other'),
('skydeck','SkyDeck','other'),('nord security','Nord Security','security_privacy'),('wolfram','Wolfram','cloud_devtools'),('warp','Warp','cloud_devtools'),
('cohere','Cohere','ai_compute'),('intuit','Intuit','finance_banking'),('qnx','QNX','cloud_devtools'),('sentry','Sentry','cloud_devtools'),('solana','Solana','cloud_devtools'),
('american airlines','American Airlines','auto_mobility'),('amazon web','AWS','cloud_devtools'),('arm challenge','Arm','cloud_devtools'),('pimco','PIMCO','finance_banking'),
('actian','Actian','cloud_devtools'),('supermemory','Supermemory','ai_compute'),('john deere','John Deere','auto_mobility'),('d_model','d_model','ai_compute'),
('k2 think','MBZUAI','ai_compute'),('dedalus','Dedalus','cloud_devtools'),('orchids','Orchids','cloud_devtools'),('databricks','Databricks','cloud_devtools'),
('zed','Zed','cloud_devtools'),('klaviyo','Klaviyo','cloud_devtools'),('caterpillar','Caterpillar','auto_mobility'),('huawei','Huawei','other'),
('actualfood','ActualFood','other'),('atlassian','Atlassian','cloud_devtools'),('cloudforce','Cloudforce','cloud_devtools'),('godaddy','GoDaddy','cloud_devtools'),
('vobile','Vobile','other'),('terraform','HashiCorp','cloud_devtools'),('cloudflare','Cloudflare','cloud_devtools'),('vultr','Vultr','cloud_devtools'),
('streamlit','Snowflake','cloud_devtools'),('auth0','Auth0','identity_auth'),('digitalocean','DigitalOcean','cloud_devtools'),('backboard','Backboard','ai_compute'),
('presage','Presage','other'),('.tech','.Tech Domains','cloud_devtools'),('t-mobile','T-Mobile','telecom'),('enactus','Enactus','other'),('sfu courses','SFU','other'),
('sfu satellite','SFU Satellite','other'),('devpost','Devpost','cloud_devtools'),('ans','GoDaddy','cloud_devtools'),('ddoski','',None)]
S=[s for s in S if s[2]]
def spons(t):
    tl=' '+t.lower()+' '
    for k,n,i in S:
        if k=='ans':
            if re.search(r'\bans\b',tl): return n,i
            continue
        if re.search(k if k.endswith(' ') or ' ' in k or '?' in k or '-' in k else k,tl): return n,i
    return None,'none'
def plc(t):
    tl=t.lower()
    if 'runner' in tl and not re.search(r'2nd|second',tl): return 'HM'
    for p,rx in (('1',r'\b1st\b|\bfirst (place|overall|prize)|\bfirst\b(?! ?time)|grand prize'),('2',r'\b2nd\b|\bsecond\b'),('3',r'\b3rd\b|\bthird\b')):
        if re.search(rx,tl): return p
    if re.search(r'4th|finalist|honou?rable|special mention',tl): return 'HM'
    return None
def kind(t,hk,sp):
    tl=t.lower()
    if 'mlh' in tl: return 'mlh'
    if re.search(r"people'?s choice|hacker'?s choice|public choice|surge choice",tl): return 'peoples_choice'
    if re.search(r'beginner|first[- ]tim|novice|freshman|first hack',tl): return 'side_beginner'
    if re.search(r'hardware|circuit|mechanical',tl): return 'side_hardware'
    if re.search(r'design|ui/ux|data vis',tl): return 'side_design'
    if re.search(r'social|impact|societal|public benefit|public health|for a cause',tl) and not sp: return 'side_social_impact'
    if sp:
        if re.search(r'best use of|best ai inference|most interesting use',tl): return 'sponsor_api_depth'
        if hk=='HackUTD' : return 'sponsor_domain'
        if re.search(r'challenge|track|build|:',tl) : return 'sponsor_domain'
        return 'sponsor_open'
    if re.search(r'overall|grand prize|general|finalist|^1st place$|^first place$|champion|best \w+ hack$',tl) and not re.search(r'track',tl.replace('grand prize','')) : return 'general'
    if re.search(r'track|category|sustain|health|educat|entertain|software|web hack|mobile|accessib|medtech|game|ethical|cyber',tl): return 'theme_track'
    return 'other'
def clean(t):
    t=re.sub(r'^(winner|sponsor winner)\s*:?\s+','',t.strip(),flags=re.I)
    return t.strip()
def A(name,pl,kind_,sp,ind,hk=None): return dict(prize_name=name,placement=pl,prize_kind=kind_,sponsor=sp,sponsor_industry=ind,hackutd2026_sponsor=hk)
out={}
O={}  # idx -> (awards, conf, note)
def gen(i,r):
    pz=r['prize']; hk=r['hackathon']
    parts=[clean(p) for p in re.split(r';',pz) if p.strip()]
    awards=[];notes=[]
    pf=r['placement_field']
    for p in parts:
        p=clean(p)
        sp,ind=spons(p)
        k=kind(p,hk,sp)
        pl=plc(p)
        if pl is None and len(parts)==1 and pf in ('1st','2nd','3rd'): pl=pf[0]
        if pl is None: pl='unranked'
        name=re.sub(r'\s*[-–—]?\s*\(?\b(1st|2nd|3rd|first|second|third) place\)?','',p,flags=re.I).strip(' -:,')or p
        h=None
        if sp=='NMC2': notes.append('NMC assumed'); h='NMC2'
        elif sp=='Spacetime': notes.append('Spacetime assumed'); h='Spacetime'
        elif sp in HK and hk=='HackUTD' or sp in ('T-Mobile','Capital One','PNC Bank','Goldman Sachs','State Farm','CBRE','EOG Resources','NVIDIA','Photon','Niantic Spatial'): h=sp
        if sp=='NMC2' : h='NMC2'
        if sp=='Toyota':
            h=None
            if hk=='HackUTD': notes.append('Toyota entity unclear')
        if sp=='Toyota Financial Services': h='Toyota Financial Services'
        if k in('general','theme_track','side_design','side_hardware','side_social_impact','side_beginner','peoples_choice','other') and not sp: sp,ind,h=None,'none',None
        if k=='mlh' and sp is None: sp,ind=None,'none'
        awards.append(A(name,pl,k,sp,ind if sp else 'none',h))
    return awards,notes
