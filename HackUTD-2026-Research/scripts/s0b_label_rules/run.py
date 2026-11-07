exec(open('cls.py').read())
import re
S2=[]
for k,n,i in S:
    k=k.replace('.','\\.') if k=='.tech' else k
    if k=='ans': continue
    S2.append((k if not k[0].isalnum() else r'\b'+k,n,i))
def spons(t):
    tl=' '+t.lower()+' '
    if re.search(r'\bans\b',tl): return 'GoDaddy','cloud_devtools'
    for k,n,i in S2:
        if re.search(k,tl): return n,i
    return None,'none'
def plc(t):
    tl=t.lower()
    if 'runner' in tl and not re.search(r'2nd|second',tl): return 'HM'
    for p,rx in (('1',r'\b1st\b|(?<![-\w])first (place|overall|prize|best)|^first\b(?! ?time)'),('2',r'\b2nd\b|\bsecond (place|overall|prize|best)|^second\b(?! screen)'),('3',r'\b3rd\b|\bthird (place|overall|prize|best)|^third\b')):
        if re.search(rx,tl): return p
    if re.search(r'4th|finalist|honou?rable|special mention',tl): return 'HM'
    return None
ORD=r"\b(1st|2nd|3rd|first|second|third|place|prize|overall|hack|best|winner|general|the|hackgt|hacknc|vthacks|prize:|ipad|sony|headphone|jbl|speaker|and)\b|[-:–,&]"
def kind2(t,hk,sp,orig,cat):
    tl=t.lower()
    if 'mlh' in tl and not re.search(r'winner pins',tl): return 'mlh'
    if re.search(r"people'?s choice|hacker'?s choice|public choice",tl): return 'peoples_choice'
    if re.search(r'solo',tl): return 'other'
    if re.search(r'overall track|best overall',tl): return 'general'
    if re.search(r'beginner|first[- ]tim|novice|freshman|first hack|emerging',tl): return 'side_beginner'
    if re.search(r'hardware|circuit|mechanical',tl): return 'side_hardware'
    if re.search(r'design|ui/ux|data vis',tl): return 'side_design'
    if sp:
        if re.search(r'financ',tl): return 'sponsor_domain'
        if 'sponsor winner' in orig.lower() or 'sponsor winner' in orig.lower():
            return 'sponsor_api_depth' if re.search('best use of',tl) else 'sponsor_domain'
        if re.search(r'best use of|most interesting use',tl): return 'sponsor_api_depth'
        if hk=='HackUTD': return 'sponsor_domain'
        if re.search(r'challenge|track|build|: ',tl+' '): return 'sponsor_domain'
        return 'sponsor_open'
    if re.search(r'social|impact|societal|public benefit|public health',tl): return 'side_social_impact'
    if re.search(r'overall|grand prize|general|finalist|champion',tl) and not re.search(r'track',tl): return 'general'
    if not re.sub(ORD,'',tl).strip(): return 'general'
    if re.search(r'track|category|sustain|health|educat|entertain|software|web hack|mobile|accessib|medtech|game|ethical|cyber|ar/vr|data protection',tl): return 'theme_track'
    return 'other'
def gen2(i,r):
    pz=r['prize']; hk=r['hackathon']; cat=r['category_as_awarded'] or ''
    parts=[clean(p) for p in pz.split(';') if p.strip()]
    pf=r['placement_field']; aw=[]
    for p in parts:
        sp,ind=spons(p)
        k=kind2(p,hk,sp,pz if 'SPONSOR WINNER' in p.upper() or 'sponsor winner' in pz.lower() and ('SPONSOR WINNER' in pz) else '',cat)
        if k=='general' and 'SPONSOR WINNER' in pz and sp: k='sponsor_domain'
        pl=plc(p)
        if pl is None and len(parts)==1 and pf in ('1st','2nd','3rd'): pl=pf[0]
        if pl=='1' and re.search(r'grand prize',p.lower()) and re.search(r'track|grand prize$',p.lower()) and not re.search(r'1st|first|\|',p.lower()) and k not in('general',): pl=None
        if pl is None: pl='unranked'
        name=re.sub(r'\s*[-–—,:]?\s*\(?\b(1st|2nd|3rd) place\)?|^(1st|2nd|3rd) place\s*','',p,flags=re.I).strip(' -:,') or p
        h=None
        if sp=='NMC2': h='NMC2'
        elif sp=='Spacetime': h='Spacetime'
        elif sp in ('T-Mobile','Capital One','PNC Bank','Goldman Sachs','State Farm','CBRE','EOG Resources','NVIDIA','Photon','Niantic Spatial','Toyota Financial Services'): h=sp
        aw.append(A(name,pl,k,sp,ind if sp else 'none',h))
    return aw
def P(**kw): return kw
# overrides: idx -> dict applied to every award ('kind','pl','note','conf','sponsor','ind'); or ('full',[awards],conf,note)
def A_(name,pl,k,sp=None,ind=None,hk=None):
    return A(name,pl,k,sp,ind if sp else 'none',hk)
F={}
F[35]=([A_('General','unranked','general'),A_('Hardware Track','unranked','side_hardware')],'low','label merges General and Hardware track; year unconfirmed')
F[20]=([A_('Next Step','unranked','sponsor_open','Next Step','other'),A_('Interview Cake','unranked','sponsor_open','Interview Cake','other')],'medium','two sponsor prizes; no problem stated')
F[68]=([A_('Built for the Real World','1','sponsor_open','Microsoft','cloud_devtools'),A_('Customer Impact Award','2','sponsor_open','Microsoft','cloud_devtools')],'high','')
F[75]=([A_('Web3 Prize: Best AI Agents','1','sponsor_open','EigenCloud','cloud_devtools'),A_('Web3 Prize: Best AI Agents','2','sponsor_open','EigenCloud','cloud_devtools')],'medium','1st and 2nd tiers listed in one label; sponsor inferred from EIGEN')
F[145]=([A_('Catalyst For Care','unranked','theme_track'),A_('Agentverse - Search & Discovery of Agents','unranked','sponsor_api_depth','Fetch.ai','ai_compute')],'medium','Agentverse is Fetch.ai product')
F[146]=([A_('Light The Way','unranked','theme_track'),A_('Figma Make Challenge','unranked','sponsor_api_depth','Figma','cloud_devtools')],'medium','Figma Make is a product')
F[282]=([A_('Finalists','HM','general'),A_('United Nations Sustainable Development Goals Enactus Challenge','unranked','sponsor_domain','Enactus','other'),A_('Best Design','unranked','side_design')],'high','')
F[321]=([A_('Overall winner','unranked','general')],'medium','city not stated')
F[322]=([A_('Grand Winner','unranked','general')],'medium','')
F[106]=([A_('Fundraising / Constituent Intelligence Challenge - 1st Place + Grand Prize','1','sponsor_domain','GiveCampus','other')],'medium','1st place plus grand prize in one label')
F[122]=([A_('Fundraising / Constituent Intelligence Challenge - 2nd Place + Most Production Ready','2','sponsor_domain','GiveCampus','other')],'medium','2nd place plus Most Production Ready in one label')
F[226]=([A_('2nd Place','2','general')],'medium','category note says MLH, but label is overall placement (prizes mention MLH pins only)')
F[225]=([A_('1st Place','1','general')],'medium','category note says MLH, but label is overall placement')
F[227]=([A_('3rd Place','3','general')],'medium','category note says MLH, but label is overall placement')
F[107]=([A_('The Fifth Teammate','2','sponsor_domain','OpenAI','ai_compute'),A_('Make Clinical Trials and Biostatistics Better!','1','sponsor_domain','Regeneron','health')],'medium','Regeneron grand prize treated as 1')
F[110]=([A_('Bringing People Closer Together with AI','1','sponsor_domain','Meta','other'),A_('Best Use of Espressif Hardware & Solutions (in AIoT)','unranked','sponsor_api_depth','Espressif','other')],'high','')
F[98]=([A_('Overall Track','3','general'),A_('The Fifth Teammate','1','sponsor_domain','OpenAI','ai_compute'),A_('Best Use of Dimensional','unranked','sponsor_api_depth','Dimensional','cloud_devtools'),A_('ASUS / Zenni Claw Challenge','1','sponsor_domain','ASUS','other')],'high','')
F[96]=([A_('Overall Track','1','general'),A_('Find the Signal','1','sponsor_domain','Elastic','cloud_devtools')],'high','')
F[109]=([A_("Create What's Next",'2','sponsor_domain','Hackster','other'),A_('Touch Grass: Build Something That Understands the Real World','1','sponsor_domain','Arduino','other')],'high','')
F[113]=([A_('Save Time. Save Money','3','sponsor_domain','Ramp','finance_banking'),A_('Office of the CFO Agent Challenge','HM','sponsor_domain','Maximor AI','finance_banking')],'medium','4th place mapped to HM')
F[458]=([A_('Best Overall (Sponsored by Vobile)','unranked','general','Vobile','other'),A_('Best Game Design Project','unranked','theme_track')],'medium','label lists 1st/2nd/3rd tiers without saying which team got which')
F[459]=([A_('Best Overall (Sponsored by Vobile)','unranked','general','Vobile','other')],'medium','label lists 1st/2nd/3rd tiers; rank not stated')
F[451]=([A_('VTHacks Overall Prize','2','general'),A_('Most Interesting Use of HokieAI','unranked','sponsor_api_depth','Cloudforce','cloud_devtools')],'high','')
F[452]=([A_('VTHacks Overall Prize','3','general'),A_('Best Use of Vultr','unranked','mlh','Vultr','cloud_devtools')],'high','')
F[453]=([A_('Best UI/UX Hack','unranked','side_design'),A_('Best Use of ANS','2','sponsor_api_depth','GoDaddy','cloud_devtools')],'high','')
F[455]=([A_('Best Use of ANS','3','sponsor_api_depth','GoDaddy','cloud_devtools'),A_('Best Use of Presage','unranked','mlh','Presage','other')],'high','')
F[218]=([A_('Best Financial Hack','unranked','sponsor_domain','Capital One','finance_banking'),A_('Best App Dev Track Hack','unranked','theme_track')],'high','')
F[219]=([A_('Real World Prize','unranked','sponsor_open','Ambrook','finance_banking'),A_('Best Champion of Open Source w/ Featherless','unranked','sponsor_open','Featherless','ai_compute'),A_('Best Intermediate Data Science Track Hack','unranked','theme_track')],'medium','Ambrook prize problem unclear; open')
F[413]=([A_('Healthcare Track','1','theme_track'),A_('ActualFood, LLC sponsor award','unranked','sponsor_open','ActualFood','other')],'medium','')
F[323]=None
# single-award patches
Q={}
def q(i,**kw): Q[i]=kw
q(0,kind='general'); q(8,kind='mlh',note='MLH/GoDaddy domain prize'); q(10,kind='sponsor_api_depth',pl='unranked',note='queue notes 3rd place, unverified; Pinata product prize')
q(26,kind='mlh');q(28,kind='mlh');q(51,kind='mlh');q(14,conf='low',note='Frontier entity/industry unclear');q(31,note='Veolia industry assumed other')
q(34,kind='sponsor_open',ind='other',note='Devpost sponsor prize');q(39,kind='other')
q(42,kind='sponsor_api_depth');q(56,kind='sponsor_api_depth');q(18,name='SambaNova');q(46,name='SambaNova')
q(62,kind='sponsor_open');q(72,kind='sponsor_api_depth',note='Claude product');q(86,kind='sponsor_open');q(88,kind='sponsor_open',note='tiers 1st/2nd/3rd listed in category; rank not stated');q(89,kind='sponsor_open',note='tier not stated')
q(92,kind='sponsor_open');q(93,kind='sponsor_open')
for i in (76,78,80): q(i,kind='theme_track',pl='unranked',note='track grand prize')
q(67,pl='unranked');q(73,pl='unranked')
q(105,kind='sponsor_domain');q(116,kind='sponsor_domain')
q(118,kind='sponsor_domain')
q(129,kind='sponsor_api_depth',note='Fetch.ai Agents League track');q(149,kind='sponsor_api_depth',sponsor='Fetch.ai',ind='ai_compute',name='Agentverse - Search & Discovery of Agents',note='Agentverse is Fetch.ai product')
q(134,kind='sponsor_open');q(136,kind='sponsor_open',note='unsure domain vs api_depth');q(139,kind='sponsor_open')
for i in range(153,180):
    pass
q(153,kind='theme_track');q(160,kind='sponsor_open',sponsor='PHRI',ind='health',conf='low',note='PHRI Challenge sponsor unclear');
q(174,pl='unranked',kind='sponsor_domain',note='"Second Screen" is part of challenge name')
q(183,kind='sponsor_open',note='Notability prize; problem unclear')
for i in (195,196,197,206,211): q(i,kind='sponsor_open',note='company prize; problem not stated')
q(198,kind='other',note='DubHacks Next; meaning unclear');q(199,kind='other',note='DubHacks Next; meaning unclear')
for i in (208,209,210): q(i,kind='sponsor_open',note='T-Mobile at non-HackUTD event; problem unclear')
q(207,kind='sponsor_open',note='Photon track winner; problem unclear')
q(194,kind='sponsor_domain')
q(213,kind='sponsor_open',note='Bloomberg public-health themed prize')
for i in (214,215,216,217,220,221,222,223): q(i,kind='theme_track')
q(224,kind='side_beginner')
q(228,pl='1',kind='sponsor_open');q(229,kind='sponsor_api_depth');q(238,kind='sponsor_api_depth')
q(236,kind='side_hardware');q(237,pl='unranked',kind='side_beginner');q(235,kind='sponsor_domain')
q(247,kind='side_social_impact',pl='unranked');q(256,pl='unranked',kind='sponsor_open');q(251,kind='sponsor_open')
for i in (249,250,252,254,255,257): q(i,kind='theme_track',pl='unranked')
q(247,pl='unranked');q(253,kind='general',pl='HM')
q(264,kind='other',note='sponsor unnamed');q(265,kind='other',note='sponsor unnamed')
for i in (269,270,271,280,281): q(i,kind='theme_track')
q(262,kind='sponsor_open');q(263,kind='sponsor_open')
q(289,kind='side_social_impact',sponsor=None,ind='none');q(290,kind='other',note='club challenge')
q(291,kind='theme_track');q(294,kind='theme_track');q(295,kind='theme_track');q(297,kind='theme_track',sponsor=None,ind='none')
q(296,kind='other',sponsor=None,ind='none',conf='low',note='Surge Choice Award unclear');
q(298,kind='theme_track');q(299,kind='theme_track');q(303,kind='side_design',sponsor=None,ind='none')
q(302,sponsor='Huawei',ind='other');q(304,kind='theme_track',sponsor=None,ind='none',note='club/institute track');q(305,kind='theme_track')
q(305,kind='theme_track');q(337,kind='theme_track')
q(300,kind='sponsor_domain');q(285,kind='sponsor_domain')
q(313,kind='side_beginner')
q(319,note='prize name not stated',conf='medium');q(320,kind='general',note='prize name not stated',conf='medium')
q(324,kind=None)
q(329,kind='sponsor_api_depth');q(361,kind='other');q(346,kind='other',note='sponsor unnamed')
q(364,pl='1',kind='side_beginner',note='label silent; placement from field')
q(371,kind='general');q(372,kind='general',note='runner-up wording but ranked 2nd')
q(373,kind='other');q(374,kind='other',sponsor=None,ind='none')
for i in (376,378,379,380,381,382): q(i,kind='theme_track')
q(370,kind='theme_track');q(385,kind='theme_track')
q(383,kind='side_hardware',note='John Deere Mechathon sponsor on hardware track');q(384,kind='side_hardware',note='John Deere Mechathon; Easy Track winner')
q(394,kind='theme_track');q(399,kind='general')
q(400,pl='unranked',kind='sponsor_domain',note='tiers 1st/2nd/3rd listed in label');q(401,kind='sponsor_domain')
q(404,pl='unranked',kind='sponsor_api_depth',note='1st place prize listed');q(405,pl='unranked',kind='sponsor_open',note='1st/2nd listed in label')
q(402,kind='sponsor_api_depth');q(403,kind='sponsor_api_depth',note='top 4 prizes')
q(418,kind='sponsor_api_depth');q(424,kind='sponsor_api_depth')
q(422,kind='other');q(426,pl='unranked',kind='sponsor_open');q(428,kind='other');q(431,kind='sponsor_open');q(430,kind='sponsor_api_depth')
q(436,kind='sponsor_domain');q(445,kind='sponsor_api_depth',note='iMessage agent via Photon');q(446,kind='sponsor_api_depth',note='iMessage agent via Photon')
q(442,kind='theme_track');q(444,kind='theme_track')
q(413,kind=None)
q(104,kind='sponsor_domain')
for i in (153,168,169): q(i,kind='theme_track')
for i in range(154,180):
    if i not in (160,161,162,163,174): q(i,kind=('side_beginner' if 'Emerging' in rows[i]['prize'] else 'theme_track'),note=('Emerging assumed beginner tier' if 'Emerging' in rows[i]['prize'] else ''))
for i in range(188,194): q(i,kind='theme_track')
q(153,kind='theme_track',note='')
q(396,note='')

for i in (142,324,327):
    pass
POST={142:1,324:1,327:1}

final=[]
for i,r in enumerate(rows):
    if i in F and F[i]:
        aw,conf,note=F[i]
    else:
        aw=gen2(i,r); conf='high'; note=''
        p=Q.get(i,{})
        if p.get('kind') is None and 'kind' in p: p=dict(p); del p['kind']
        for a in aw:
            if 'kind' in p: a['prize_kind']=p['kind']
            if 'pl' in p: a['placement']=p['pl']
            if 'name' in p: a['prize_name']=p['name']
            if 'sponsor' in p: a['sponsor']=p['sponsor']
            if 'ind' in p: a['sponsor_industry']=p['ind']
        conf=p.get('conf',conf); note=p.get('note',note)
        for a in aw:
            sp=a['sponsor']
            if sp=='NMC2': a['sponsor']='Northmark Compute & Cloud'; a['hackutd2026_sponsor']='NMC2'; note=(note+'; ' if note else '')+'NMC assumed'
            if sp=='Spacetime': note=(note+'; ' if note else '')+'Spacetime assumed'
            if sp=='Toyota' and r['hackathon']=='HackUTD': note=(note+'; ' if note else '')+'Toyota entity unclear'
            if sp=='SambaNova': a['sponsor']='SambaNova'
            if a['prize_kind'] in ('general','theme_track','side_beginner','peoples_choice','other','side_design','side_social_impact') and a['sponsor'] is None: a['sponsor_industry']='none'
            if a['sponsor'] is None: a['sponsor_industry']='none'
        if len(aw)>1 and not note: note=''
        if note and conf=='high': conf='medium'
    # conflict check: label vs placement_field
    pf=r['placement_field']
    if pf in('1st','2nd','3rd') and len(aw)==1 and aw[0]['placement'] not in (pf[0],) and not note:
        note=f'placement_field {pf} vs label {aw[0]["placement"]}'
    # grand prize w/ 'Grand Prize (2nd)' covered
    if i in (142,324,327): aw[1]['prize_kind']='sponsor_open'
    final.append(dict(label_id=r['label_id'],awards=aw,confidence=conf,note=note))
with open(D+'prize_labels_classified_part00.jsonl','w') as f:
    for x in final: f.write(json.dumps(x,ensure_ascii=False)+'\n')
for i,x in enumerate(final):
    print(i,rows[i]['prize'][:50],'=>',[(a['placement'],a['prize_kind'],a['sponsor']) for a in x['awards']],x['confidence'],x['note'])
