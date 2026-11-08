# 02 - Tool APIs the agent can call

Researched 2026-11-07. Every claim has its source next to it. "Illustrative" = I rebuilt the sample from the docs' field lists, not copied from a sample. UNVERIFIED = could not confirm from a primary source today.

## TL;DR (wire these first)
1. **URL check:** Google Safe Browsing v5 `urls:search` (free, API key, non-commercial) plus a local check of the OpenPhish community feed (a text file, no key). Add URLhaus/ThreatFox (free Auth-Key, about 5 min) as a second opinion. Skip PhishTank: it has not accepted new signups since 2020.
2. **Domain age / look-alike:** `rdap.org/domain/<d>` (no key) for the registration date, plus `dnstwist` (pip, offline) for typosquats of the brand being impersonated. crt.sh is unofficial and flaky, so treat it as optional.
3. **Telecom signals:** mock CAMARA SIM Swap, Device Swap, Number Verification, KYC Match, KYC Tenure and Number Recycling using the exact YAML schemas below. T-Mobile US has no instant sandbox (NDA/BD gate). The only same-day real call is the Vonage Network API playground (SIM Swap, virtual `+990…` numbers).
4. **Payment hold:** Capital One Nessie (GitHub login, key right away). Create a transfer, then `PUT /transfers/{id}` with status `cancelled` or `DELETE /transfers/{id}` as the "hold/cancel" action. Have a local mock fallback.
5. **After the scam:** deep-link only (no prefill APIs) to ReportFraud.ftc.gov, IdentityTheft.gov and SMS 7726. FTC sites showed a **shutdown notice** today, so verify before the demo. Run Presidio (`pip install presidio-analyzer presidio-anonymizer`) on every message before it reaches Nemotron or any third-party API.

## Comparison table

| API | Signup time | Free limit | Auth | Flag |
|---|---|---|---|---|
| Google Safe Browsing v5 | ~10 min (GCP project + API key; UNVERIFIED timing) | Not published on ref page | API key (`key=`; UNVERIFIED on ref page) | **Non-commercial only**; commercial use must go to Web Risk |
| Google Web Risk `uris.search` | ~15 min | 100k calls/month free | GCP auth / API key | **Billing account required**; calling computeDiff reprices lookups to $50/1k |
| VirusTotal v3 | ~5 min | 4 req/min, 500/day | `x-apikey` header | **Not allowed in commercial products**; submissions become public, no PII |
| URLhaus (abuse.ch) | ~5 min | Not published | `Auth-Key` header (mandatory since 2025-06-30) | Need 2 linked social logins |
| ThreatFox (abuse.ch) | same key as URLhaus | Not published | `Auth-Key` header | IOCs older than 6 months not returned |
| PhishTank | **Closed** | n/a | app key | **New registration off since 2020**; dumps only |
| OpenPhish community | 0 (no signup) | 12h refresh | none | Terms of Use apply; no API |
| urlscan.io | ~5 min | Per-action quotas, check `/api/v1/quotas` | `API-Key` header | Public scans are visible to everyone; use `unlisted`/`private` |
| RDAP (rdap.org) | 0 | 10 req / 10 s | none | 429 on burst |
| crt.sh | 0 | ~5 req/min (unofficial) | none | **No official API**, frequent 502/empty |
| dnstwist | 0 (pip) | unlimited (local) | none | Apache-2.0 |
| Twilio Lookup v2 | ~10 min (trial acct) | Basic validation free; line type is paid | HTTP Basic | `sim_swap` package is **private beta, needs sales** |
| numverify | ~5 min | 100 req/month | `access_key` query | Tiny quota |
| FTC DNC complaints API | ~2 min (api.data.gov key; `DEMO_KEY` works) | Not published (429 on limit) | `api_key` / `X-Api-Key` | Data unverified; may be down in shutdown |
| CAMARA specs | 0 (read YAML) | n/a | OIDC/OAuth2 (`openId` scopes) | Mock only; real access needs operator/aggregator |
| Vonage Network playground | ~15 min | Free trial (no card) | App ID + private key JWT | SIM Swap only in the blog walkthrough |
| T-Mobile DevEdge SIM Swap | **Days to weeks** (BD review + NDA) | n/a | n/a | **Approval > 1 hour** |
| Aduna | Contact sales | n/a | n/a | **No self-serve found** |
| Capital One Nessie | ~2 min (GitHub login) | Not published | `?key=` query | Shell could not resolve the host; web docs loaded. Test early |
| ReportFraud / IdentityTheft.gov / 7726 | n/a | n/a | n/a | **No API or prefill**; FTC shutdown banner seen |
| Presidio | 0 (pip) | local | none | Moved from Microsoft GitHub org to data-privacy-stack |

---

## 1. URL and domain reputation

### Google Safe Browsing v5 (use this one)
- Base `https://safebrowsing.googleapis.com`. v5 has `GET /v5/urls:search` and `GET /v5/hashes:search`, plus hash-list endpoints. v4 (`POST /v4/threatMatches:find`, etc.) is still listed next to it. https://developers.google.com/safe-browsing/reference/rest
- **Non-commercial only.** Commercial users are sent to Web Risk. https://developers.google.com/safe-browsing/reference/rest
- `urls:search`: the `urls[]` query param takes at most 50 URLs, with an empty body. The response has `threats[]` (each with `url`, `threatTypes[]`) and `cacheDuration`. No match returns 200 with empty `threats`. You must cache results for `cacheDuration` (max 24h when there are no threats). https://developers.google.com/safe-browsing/reference/rest/v5/urls/search
- Auth: API key from Google Cloud Console as `?key=`. The reference page does not state this, so UNVERIFIED (it is the standard Google API key pattern).
- v4 deprecation status: UNVERIFIED. The ref page does not mark v4 deprecated. Build on v5 anyway.

Sample (illustrative):
```
GET https://safebrowsing.googleapis.com/v5/urls:search?urls=http://usps-redelivery-fee.top/pay&key=$GSB_KEY
-> 200 {"threats":[{"url":"http://usps-redelivery-fee.top/pay","threatTypes":["SOCIAL_ENGINEERING"]}],"cacheDuration":"300s"}
```
For demos, Google's test URL `http://testsafebrowsing.appspot.com/s/phishing.html` should trigger a hit (UNVERIFIED for v5).

### Google Web Risk (commercial version)
- `uris.search`: free up to 100,000 calls/month, then $0.50 per 1k. Calling Update API `computeDiff` changes lookup pricing to $50 per 1k. https://cloud.google.com/web-risk/pricing
- Setup requires a project with **billing enabled**. https://docs.cloud.google.com/web-risk/docs/detect-malicious-urls
- Pitch line: "In production we'd swap Safe Browsing for Web Risk, the licensed commercial version."

### VirusTotal v3
- Public API: 4 req/min and 500 req/day. It **must not be used in commercial products**. https://docs.virustotal.com/reference/public-vs-premium-api
- Submit: `POST https://www.virustotal.com/api/v3/urls`, form field `url`, header `x-apikey`. Returns an analysis ID. The docs say not to submit PII, and submitted IOCs join the community dataset. https://docs.virustotal.com/reference/scan-url
- Report: `GET /api/v3/urls/{id}`, where id = URL SHA256 or unpadded base64url of the URL. https://docs.virustotal.com/reference/url-info
- Key response fields: `last_analysis_stats` {harmless, malicious, suspicious, undetected, timeout}, `reputation` (int, community votes), `categories` (by vendor). https://docs.virustotal.com/reference/url-object

Sample (illustrative):
```
GET /api/v3/urls/aHR0cDovL3VzcHMtcmVkZWxpdmVyeS1mZWUudG9wL3BheQ   (x-apikey: $VT)
-> {"data":{"attributes":{"last_analysis_stats":{"harmless":60,"malicious":7,"suspicious":1,"undetected":12,"timeout":0},"reputation":-12}}}
```

### URLhaus and ThreatFox (abuse.ch)
- Auth became **mandatory on 2025-06-30**. Sign in at https://auth.abuse.ch/ with X/LinkedIn/Google/GitHub, link a second provider, then create an Auth-Key and send it as the `Auth-Key` header. No numeric limits are published. https://abuse.ch/blog/community-first/
- URLhaus lookup: `POST https://urlhaus-api.abuse.ch/v1/url/` with form `url=…`. `query_status` is `ok` or `no_results`. https://github.com/TundraSoft/tundra-connect/wiki/URLhaus-API (third-party wrapper doc, because the official API page blocked fetching)
- ThreatFox: `POST https://threatfox-api.abuse.ch/api/v1/` with JSON `{"query":"search_ioc","search_term":"…","exact_match":true}`. Response `data[]` has `ioc`, `threat_type`, `malware_printable`, `confidence_level` (0-100), `first_seen`, `last_seen`, `tags`. IOCs older than 6 months expire. https://threatfox.abuse.ch/api/
```
curl -H "Auth-Key: $ABUSECH" -X POST https://urlhaus-api.abuse.ch/v1/url/ -d "url=http://example.com/x.exe"
-> {"query_status":"no_results"}      (illustrative)
```
Note: URLhaus focuses on malware URLs, so expect few smishing phish hits. Use it as a secondary signal.

### PhishTank: **do not plan on it**
- New user registration was removed in 2020 because of abuse, and it was still closed as of June 2026. https://en.wikipedia.org/wiki/PhishTank
- What remains is hourly database dumps (JSON/CSV/XML). Without an app key you get a few downloads per day. https://www.phishtank.net/developer_info.php

### OpenPhish community feed (no signup)
- Plain-text feed at `https://raw.githubusercontent.com/openphish/public_feed/refs/heads/main/feed.txt`, refreshed every 12h. Use is under their Terms of Use. No API. https://openphish.com/phishing_feeds.html
- Use: download at startup into a set and do an exact or host match locally. This is fast, private (no URL leaves our server), and works offline in the demo.

### urlscan.io
- Auth header `API-Key`. Quotas apply per action per minute, hour and day. Query yours at `https://urlscan.io/api/v1/quotas`. https://docs.urlscan.io/pages/api-rate-limits
- Submit `POST https://urlscan.io/api/v1/scan/` with body `{"url":…,"visibility":"unlisted"}`. Result is at `GET /api/v1/result/{uuid}/` after about 10-30 s. Search is `GET /api/v1/search/?q=domain:example.com`. UNVERIFIED: the quickstart page would not load. Paths are from prior knowledge of the API.
- Privacy flag: public scans are visible to everyone. Use `unlisted` or `private`, and never scan URLs that carry tokens or PII. The screenshot makes a nice "here's what the page looks like, safely" UI moment.

## 2. Domain age and look-alikes

### RDAP
- `GET https://rdap.org/domain/<domain>` returns a 302 to the authoritative registry RDAP server (follow redirects). No auth. Limit is 10 requests per 10 s, else 429. https://about.rdap.org/
- Registration date is in `events[]` with `eventAction: "registration"` (RFC 9083). Field name is from the RFC and was not shown on the page, so UNVERIFIED there.
```
curl -Ls https://rdap.org/domain/usps-redelivery-fee.top | jq '.events[]|select(.eventAction=="registration").eventDate'
-> "2026-11-05T09:12:44Z"   (illustrative)
```
Risk rule: domain younger than 30 days plus a brand keyword gives a strong signal.

### crt.sh (optional)
- `https://crt.sh/?q=%25.example.com&output=json` returns `issuer_name`, `common_name`, `name_value`, `id`. It is unofficial, with no SLA, about 5 req/min, and heavy queries 502. https://cert.imfht.com/crt-sh-api
- Use: "first cert issued 2 days ago" works as a freshness signal. Cache it and give it a short timeout.

### dnstwist
- `pip install dnstwist[full]`. CLI: `dnstwist --registered --format json usps.com`. Python: `dnstwist.run(domain='usps.com', registered=True, format='null')` returns a list of dicts. Apache-2.0. https://github.com/elceef/dnstwist
- Use: precompute look-alikes for about 20 brands scammers impersonate (USPS, T-Mobile, Chase, E-ZPass, etc.). The agent then flags "this domain is a homoglyph of t-mobile.com". Precompute because live runs do DNS lookups and take time.

## 3. Phone number intelligence

### Twilio Lookup v2
- `GET https://lookups.twilio.com/v2/PhoneNumbers/{E164}?Fields=line_type_intelligence` with HTTP Basic auth (API key SID and secret). Basic formatting and validation are free. `line_type_intelligence` and `caller_name` are paid. `sim_swap` is **private beta, carrier approval, contact sales**. https://www.twilio.com/docs/lookup/v2-api.md
- `line_type_intelligence` fields: `type`, `carrier_name`, `mobile_country_code`, `mobile_network_code`, `error_code`. Types include mobile, landline, fixed VoIP, non-fixed VoIP and toll-free. The exact strings (e.g. `nonFixedVoip`) are UNVERIFIED. Same source.

### numverify (apilayer)
- 100 requests/month free, HTTPS included. `GET https://apilayer.net/api/validate?access_key=KEY&number=+14158586273`. Returns `valid`, `carrier`, `line_type`, `location`, `country_code`, and more. https://numverify.com/

### FTC Do Not Call reported calls API
- `GET https://api.ftc.gov/v0/dnc-complaints` with an api.data.gov key (`api_key` param or `X-Api-Key`; `DEMO_KEY` works for tests). Filters: `created_date`, `violation_date[_from/_to]`, `state`, `city`, `area_code`, `is_robocall`, `items_per_page` (max 50), `offset`. Fields: `company-phone-number`, `created-date`, `violation-date`, `consumer-state`, `subject`, `recorded-message-or-robocall`. **There is no filter by phone number.** https://www.ftc.gov/developer/api/v0/endpoints/do-not-call-dnc-reported-calls-data-api
- Data is updated weekdays around noon ET and is unverified. https://www.ftc.gov/policy-notices/open-government/data-sets/do-not-call-data
- Use: you can't look up a number directly. Bulk-pull recent complaints into a local table, then check "this number appeared in N FTC complaints, subject: Imposters". Pull it **tonight**, since it may go offline (see the shutdown note below).

## 4. CAMARA / GSMA Open Gateway (mock these faithfully)

All schemas below come from the `main` branch YAMLs (version `wip`, last commits Oct-Nov 2026), cloned 2026-11-07. Latest release tags: SIMSwap r4.3, DeviceSwap r4.3, NumberVerification r4.2, KnowYourCustomer r2.2, Tenure r3.4, NumberRecycling r3.1 (from `git ls-remote --tags`). Pin a tag in your citations, e.g. `/blob/r4.3/`.

Common to all: `phoneNumber` is E.164 with pattern `^\+[1-9][0-9]{4,14}$`. Request and response carry an optional `x-correlator` header. Auth is OIDC `openId` with per-operation scopes. In 2-legged mode `phoneNumber` goes in the body; in 3-legged mode it comes from the token. https://github.com/camaraproject/SimSwap/blob/main/code/common/CAMARA_common.yaml
Errors follow `{status, code, message}` (CAMARA ErrorInfo).

| API | Spec YAML | Path(s) | Request | Response |
|---|---|---|---|---|
| SIM Swap | https://github.com/camaraproject/SimSwap/blob/main/code/API_definitions/sim-swap.yaml | `POST /sim-swap/{v}/retrieve-date`, `POST /check` | retrieve: `{phoneNumber}`; check: `{phoneNumber, maxAge}` with maxAge = **hours**, 1-2400, default 240 | retrieve: `{latestSimChange: RFC3339 or null, monitoredPeriod: days 1-999}`; check: `{swapped: bool}` |
| Device Swap | https://github.com/camaraproject/DeviceSwap/blob/main/code/API_definitions/device-swap.yaml | `POST /device-swap/{v}/retrieve-date`, `POST /check` | same shape as SIM Swap (maxAge 1-2400, default 240) | `{latestDeviceChange, monitoredPeriod}` / `{swapped}` |
| Number Verification | https://github.com/camaraproject/NumberVerification/blob/main/code/API_definitions/number-verification.yaml | `POST /number-verification/{v}/verify`, `GET /device-phone-number` | `{phoneNumber}` or `{hashedPhoneNumber}` (SHA-256 hex) | `{devicePhoneNumberVerified: bool}` / `{devicePhoneNumber}` |
| KYC Match | https://github.com/camaraproject/KnowYourCustomer/blob/main/code/API_definitions/kyc-match.yaml | `POST /kyc-match/v0.3/match` | `phoneNumber, idDocument, name, givenName, familyName, address, postalCode, birthdate, email, gender…` | per field `xxxMatch: "true"/"false"/"not_available"` plus optional `xxxMatchScore` (int) |
| KYC Tenure | https://github.com/camaraproject/Tenure/blob/main/code/API_definitions/kyc-tenure.yaml | `POST /kyc-tenure/{v}/check-tenure` | `{phoneNumber, tenureDate: "YYYY-MM-DD"}` | `{tenureDateCheck: bool, contractType: PAYG/PAYM/Business}` |
| Number Recycling | https://github.com/camaraproject/NumberRecycling/blob/main/code/API_definitions/number-recycling.yaml | `POST /number-recycling/{v}/check` | `{phoneNumber, specifiedDate: "YYYY-MM-DD"}` | `{phoneNumberRecycled: bool}` |

Notes for faithful mocking:
- SIM Swap `latestSimChange` can be `null` when the operator withholds it for privacy. In that case only `monitoredPeriod` comes back. Mock this case too, because it shows honest uncertainty. (sim-swap.yaml lines ~234-243)
- Scopes: `sim-swap:check`, `sim-swap:retrieve-date`, `device-swap:check`, `number-verification:verify`, `kyc-match:match`, `kyc-tenure:check-tenure`, `number-recycling:check` (from the YAML `security` blocks).
- KYC Age Verification and KYC Fill-in also exist in the same KYC repo (`kyc-age-verification.yaml` v0.1, `kyc-fill-in.yaml` v0.3).

Mock sample (from the schema):
```
POST /sim-swap/v2/check   Authorization: Bearer <mock>
{"phoneNumber":"+14695550123","maxAge":72}
-> 200 {"swapped":true}
POST /sim-swap/v2/retrieve-date  {"phoneNumber":"+14695550123"}
-> 200 {"latestSimChange":"2026-11-06T22:41:08.312-06:00"}
```
(The `v2` in the path is illustrative. main uses `vwip`.)

### Sandboxes
- **T-Mobile US DevEdge SIM Swap**: described as CAMARA/GSMA-compatible, but access goes through a lead form, a BD review and an **NDA**, and no sandbox is mentioned. Not usable this weekend. https://devedge.t-mobile.com/Sim-swap
- **Aduna** (Ericsson + operator JV; T-Mobile listed among the 12 founding operators, USA covered): no self-serve signup or sandbox found, just "contact our experts". https://www.adunaglobal.com/ and https://tools.prnewswire.com/en-us/live/20823/release/20260303EN98152
- **GSMA Open Gateway sandbox** page lists SIM Swap, Number Verification, QoD and Device Location, with auth flows Client Credentials, CIBA, Auth Code and JWT Bearer. It names no signup process or speed. https://open-gateway.gsma.com/sandbox
- **Vonage Network API Playground (fastest real call)**: free Vonage account, enable Network Registry, choose Playground. A Virtual CSP returns deterministic results for `+990…` numbers (`maxAge` < 500 gives `swapped:false`, >= 500 gives `true`). Python: `vonage_client.network_sim_swap.check(SimSwapCheckRequest(phone_number='+990491793'))` returns `{'swapped': True}`. https://developer.vonage.com/ja/blog/make-your-first-network-api-call-using-the-sandbox
- Recommendation: run our own CAMARA-shaped mock server. Optionally add one live Vonage playground call to show "this plugs into real operator APIs".

## 5. STIR/SHAKEN

- **A, Full:** the signing provider originated the call, has an authenticated relationship with the customer, and has verified the customer may use that number. **B, Partial:** it knows the customer but not their right to the number. **C, Gateway:** the call only entered its network (e.g. an international gateway), with no relationship to the caller. Definitions are in ATIS-1000074. https://sti-ga.atis.org/wp-content/uploads/2020/04/SHAKEN101_-MitigatingIllegalRobocalling01302019.pdf
- FCC 24-120 (third-party signing) confirms that A/B need a direct authenticated customer relationship and that A also needs a verified right to the number. It defers the full definitions to ATIS-1000074. https://public-inspection.federalregister.gov/2025-15809.pdf
- Attestation is not spam blocking. Terminating carriers combine it with analytics (Hiya, First Orion, TNS, YouMail, …). An A call can still be spam, and a B call should not be auto-blocked. https://bandwidth.com/blog/abcs-of-attestation-and-analytics
- **What apps can actually see:** Android 10+ `CallScreeningService` exposes `Call.Details.getCallerNumberVerificationStatus()` with values `VERIFICATION_STATUS_PASSED`, `FAILED` or `NOT_VERIFIED`. That is a pass/fail verdict, **not the A/B/C letter**. https://developer.android.com/develop/connectivity/telecom/dialer-app/screen-calls?hl=en
- iOS exposes no attestation level to third-party apps (UNVERIFIED; no primary doc found). Carriers show their own labels: T-Mobile shows **"Caller Verified"** on supported devices for authenticated calls. https://www.t-mobile.com/news/press/inter-carrier-stir-shaken-launch
- How we use it: a mock call event carries `attest: A|B|C|none`. The risk engine treats C or none plus "claims to be your bank" as high risk, and A as lowering risk without clearing it, because spoofing is not the only threat (real numbers get used too). Be honest in the pitch: a carrier-side product like Scam Shield can see the letter, while a normal app only gets pass/fail on Android.

## 6. Capital One Nessie (mock bank)

- Key: log in with GitHub at the Nessie site, then copy the key from your profile and add it as the `key` query param. Customer endpoints act on your own data. Enterprise endpoints are read-only. http://api.nessieisreal.com/
- Live check: the home and documentation pages loaded through WebFetch today (2026-11-07). From the sandbox shell, DNS for `api.nessieisreal.com` failed, so the API itself is UNVERIFIED. One third-party MCP server uses base `https://prod-api.nessieisreal.com` (https://glama.ai/mcp/servers/lllNuggetslll/nessie-mcp-server). Try both hosts and **keep a local mock fallback**.
- Transfer endpoints (from a client library doc, https://shwheelz.github.io/capital_one/Transfer.html):
  - `GET /accounts/{accId}/transfers[?type=payer|payee]`
  - `POST /accounts/{accId}/transfers`
  - `GET /transfers/{id}`
  - `PUT /transfers/{id}` (update)
  - `DELETE /transfers/{id}` (cancel)
- Other: `GET/POST /customers/{id}/accounts`, `GET /accounts/{id}`. Path names are standard Nessie, but I did not fetch them today, so UNVERIFIED.
- **Hold/cancel pattern:** create the transfer with `"status":"pending"`. When the agent flags the scam, `PUT` with `"status":"cancelled"` or `DELETE` it. The body fields `medium` ("balance"), `payee_id`, `amount`, `transaction_date`, `status` (pending/cancelled/completed) and `description` are UNVERIFIED (from memory of the Nessie docs).
```
POST /accounts/ACC1/transfers?key=$NESSIE
{"medium":"balance","payee_id":"ACC_SCAMMER","amount":950,"transaction_date":"2026-11-07","status":"pending","description":"Zelle to 'USPS fee'"}
-> 201 {"code":201,"message":"Created transfer","objectCreated":{"_id":"T123",...}}   (illustrative)
PUT /transfers/T123?key=$NESSIE   {"status":"cancelled"}   (illustrative)
```

## 7. Reporting and recovery

- **7726 (SPAM):** forward the text to 7726 so the carrier can spot and block similar messages. Also use the phone's built-in "report junk", and report at ReportFraud.ftc.gov. No API. https://consumer.ftc.gov/articles/how-recognize-and-report-spam-text-messages
  - App use: an `sms:7726?body=<original text>` link opens the composer prefilled. That is the OS URI scheme, not an FTC/carrier API (UNVERIFIED on iOS body handling; iOS uses `&body=`).
- **ReportFraud.ftc.gov:** no public API, prefill or category deep link found. **Today the page shows a "service unavailable due to government shutdown" notice.** https://reportfraud.ftc.gov/
- **FTC closure banner** says the FTC closed from 2026-01-31 for a funding lapse, and that DNC Registry, ReportFraud, IdentityTheft.gov and econsumer.gov are unavailable. The same page carries Nov 2026 items, so the current status is UNVERIFIED. https://www.ftc.gov/ftc-is-closed
- **IdentityTheft.gov:** report identity theft and get a step-by-step personal recovery plan (limit damage, report, fix credit). No API or deep link found; only the homepage and info pages are public. https://www.identitytheft.gov/ The FTC Identity Theft Report, the account and the prefilled letters are mentioned in page metadata but not detailed (UNVERIFIED specifics). https://www.identitytheft.gov/Steps
- How we use it: the agent generates a **case summary** (timeline, scam URL, number, amount, what we already did) as a copy-to-clipboard block, then opens these sites. Pitch it as "we do the paperwork, you just paste". Never claim we file automatically. If FTC sites are down, show the fallback: carrier report, bank fraud line, local police non-emergency.

## 8. PII redaction: Presidio

- Install: `pip install presidio-analyzer presidio-anonymizer` then `python -m spacy download en_core_web_lg`. A transformers variant exists too. https://presidio.dataprivacystack.org/getting_started/getting_started_text/
- Project moved: docs now live at presidio.dataprivacystack.org and the repo at github.com/data-privacy-stack/presidio (redirected from microsoft.github.io/presidio). https://presidio.dataprivacystack.org/getting_started/
```python
from presidio_analyzer import AnalyzerEngine
from presidio_anonymizer import AnonymizerEngine
text = "Hi Maria, your Chase acct 4417 is locked, call 214-555-0199"
res = AnalyzerEngine().analyze(text=text, language="en")   # omit entities= to detect all
print(AnonymizerEngine().anonymize(text=text, analyzer_results=res).text)
# -> "Hi <PERSON>, your Chase acct 4417 is locked, call <PHONE_NUMBER>"  (illustrative)
```
- Use: redact before logging and before Nemotron. **Keep URLs and the scammer's number unredacted** in a separate field, because the tools need them. Redact the victim's name, account numbers and addresses. Custom `PatternRecognizer` for account or OTP codes: see the "Developing PII recognizers" docs (not fetched).
