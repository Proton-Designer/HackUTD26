# 02 — APIs the agent can call tonight
**Research date: 2026-11-07 | “Usable tonight” means public docs and a plausible no-payment path, not authenticated testing.**

## TL;DR — use first
1. Use **Google Safe Browsing v5** for non-commercial URL checks; cache results, and don't assume clean means safe.
2. Use **URLhaus + ThreatFox** as additional malicious-indicator signals; get abuse.ch keys immediately if needed.
3. Use **local RDAP + dnstwist** to detect recently registered, look-alike sender domains without paid providers.
4. **Mock CAMARA telecom APIs** from official OpenAPI schemas; access to a real T-Mobile/Aduna carrier network is not demonstrated.
5. **Mock bank hold/cancellation** in your own simulator; never imply Capital One Nessie can stop an actual payment.

## API readiness matrix
Signup times are **planning estimates, not a verified provider SLA**; quotas can change. `key` or `token` are placeholders. Example responses illustrate shapes or demo fixtures and are NOT live service responses. No unauthorized data or real-person identifiers are required.

| Service and docs | Setup / auth / free limits | Key request | Example response (illustrative) | Build / pitch use |
|---|---|---|---|---|
| **Google Safe Browsing v5** [docs](https://developers.google.com/safe-browsing/reference), [noncommercial rules](https://developers.google.com/safe-browsing/reference/Appropriate.Usage) | ~10–30m Google Cloud project + API key; **free, NON-COMMERCIAL only**, project-specific quota **UNVERIFIED** | `GET https://safebrowsing.googleapis.com/v5/urls:search?urls=https%3A%2F%2Fexample.com&key=$KEY` (**exact query encoding/schema: verify v5 docs**) | `{ "threats": [] }` (no listed match ≠ safe) | One quick live URL-reputation check for demo. |
| **Google Web Risk** [API](https://cloud.google.com/web-risk/docs/lookup-api), [pricing](https://cloud.google.com/web-risk/pricing) | ~20–60m Cloud + billing setup may be needed; **first 100,000 `uris.search` lookups/month free**; excess **PAID** | `GET https://webrisk.googleapis.com/v1/uris:search?uri=https%3A%2F%2Fexample.com&threatTypes=SOCIAL_ENGINEERING&key=$KEY` | `{}` or `{ "threat": { "threatTypes": ["SOCIAL_ENGINEERING"] } }` | Commercial path later; **do not enable paid usage** for hackathon unless existing no-cost account. |
| **VirusTotal Public API v3** [URL info](https://docs.virustotal.com/reference/url-info), [limits](https://docs.virustotal.com/reference/public-vs-premium-api) | ~5–20m account, `x-apikey`; **4 req/min, 500/day**, noncommercial limits; **RATE-LIMITED** | `GET https://www.virustotal.com/api/v3/urls/<base64url(URL)_without_padding>` | `{ "data": { "attributes": { "last_analysis_stats": { "malicious": 0, "suspicious": 0 } } } }` | Evidence from multiple engines; don't block on VT. |
| **URLhaus (abuse.ch)** [API](https://urlhaus.abuse.ch/api/) | ~5–20m abuse.ch auth key; fair-use terms / **limit not published as fixed entitlement** | `POST` request per currently documented URLhaus endpoint and request fields (**version-specific endpoint UNVERIFIED**; do not hardwire legacy `/v1/url/` without testing) | `{ "query_status": "no_results" }` | Good for known *malware distribution* URLs, not comprehensive phishing. |
| **ThreatFox (abuse.ch)** [API](https://threatfox.abuse.ch/api/) | ~5–20m abuse.ch auth key (`Auth-Key`); fair-use / **RATE-LIMITED** | `POST https://threatfox-api.abuse.ch/api/v1/` + `{ "query":"search_ioc", "search_term":"domain.example", "exact_match":true }` | `{ "query_status":"no_result" }` | Cross-check known bad hostnames/indicators. |
| **PhishTank** [site](https://phishtank.org/) | Community/API availability, current registration, allowable API usage **UNVERIFIED** | Public feeds/API access **UNVERIFIED** | **UNVERIFIED** | Never place on live critical path; optional offline sample only with license check. |
| **OpenPhish Community** [feeds](https://openphish.com/phishing_feeds.html) | No-login community URL feed; updated on provider schedule, paid premium feeds | `GET https://openphish.com/feed.txt` (**verify service currently returns it**) | Plaintext list of phishing URLs | Preload a local hash/set for offline lookup; **never click or fetch listed malware URLs**. |
| **urlscan.io** [submit docs](https://docs.urlscan.io/apis/urlscan-openapi/scanning/submitscan), [quotas](https://docs.urlscan.io/pages/api-rate-limits) | ~5–20m API key, `API-Key`; tier-specific throttles / **RATE-LIMITED**; public scans expose submitted URLs | `POST https://urlscan.io/api/v1/scan/` with `{ "url":"https://example.com", "visibility":"unlisted" }` | `{ "uuid":"...", "result":"https://urlscan.io/result/..." }` | Optional external visual evidence; don't submit private personal URLs or block demo awaiting async scan. |
| **ICANN RDAP** [ICANN](https://www.icann.org/rdap), [public bootstrap](https://rdap.org/) | No signup/auth for public RDAP, server-specific throttles | `GET https://rdap.org/domain/example.com` | `{ "events":[{"eventAction":"registration", "eventDate":"2026-09-01T00:00:00Z"}] }` | “Registered 3 days ago” demo signal using fixture; age alone not proof. |
| **crt.sh certificate transparency** [search](https://crt.sh/) | No auth; **unofficial/variable availability, rate-limited** | `GET https://crt.sh/?q=%25.example.com&output=json` | `[ { "name_value":"www.example.com" } ]` | Collect suspect sister domains; not an authoritative verification. |
| **dnstwist** [open-source](https://github.com/elceef/dnstwist) | `pip install dnstwist`, local no API key; DNS lookups may be slow | CLI `dnstwist --registered bank.example` | Terminal list of registered variants | Flag brand-lookalikes; apply safe allowlist for common legitimate variants. |
| **Twilio Lookup v2** [docs](https://www.twilio.com/docs/lookup/v2-api), [trial](https://www.twilio.com/docs/usage/trials/try-out-lookup), [pricing](https://www.twilio.com/en-us/user-authentication-identity/pricing/lookup) | ~10–30m trial; HTTP Basic SID/token. Basic validation free; **line-type/carrier paid** after trial; trial capacity depends on account | `GET https://lookups.twilio.com/v2/PhoneNumbers/%2B14155550100?Fields=line_type_intelligence` | `{ "valid":true, "line_type_intelligence": {"type":"mobile"} }` | Normalize numbers; **mock line type** unless free trial confirmed. Never show phone number = scam. |
| **FTC Do Not Call complaints open data** [official](https://www.ftc.gov/developer/api/v0/endpoints/do-not-call-dnc-reported-calls-data-api) | Public data; key/rate and direct endpoint **UNVERIFIED** | Query from documented FTC API rather than hardcoding an unverified path | `{ "number":"...", "complaints":0 }` **SIMULATED** | Weak contextual signal only; FTC says complaints are *unverified*. [DNC Data Book](https://ftc.gov/reports/national-do-not-call-registry-data-book-fiscal-year-2025). |

**Sample reproducible `curl` (key-required services):**

```bash
# Web Risk (commercial API, zero-rated first 100k monthly lookups; billing may be required)
curl -G 'https://webrisk.googleapis.com/v1/uris:search' \
  --data-urlencode 'uri=https://example.com' \
  --data-urlencode 'threatTypes=SOCIAL_ENGINEERING' \
  --data-urlencode "key=${WEB_RISK_KEY}"

# VirusTotal URL ID = base64url(url), with trailing = removed.
URL_ID=$(python -c 'import base64; print(base64.urlsafe_b64encode(b"https://example.com/").decode().rstrip("="))')
curl -H "x-apikey: ${VT_KEY}" "https://www.virustotal.com/api/v3/urls/${URL_ID}"

# RDAP registration events
curl -s 'https://rdap.org/domain/example.com'

# ThreatFox JSON IOC lookup; test the chosen IOC format and auth on the actual service.
curl -s 'https://threatfox-api.abuse.ch/api/v1/' \
  -H "Auth-Key: ${ABUSECH_KEY}" -H 'Content-Type: application/json' \
  -d '{"query":"search_ioc","search_term":"example.com","exact_match":true}'
```

## Telecom network signals: CAMARA/GSMA Open Gateway

Official API registry: [GSMA descriptions](https://gsma.com/solutions-and-impact/gsma-open-gateway/gsma-open-gateway-api-descriptions), [CAMARA documentation](https://camaraproject.org/resources), [CAMARA Spring25 release](https://camaraproject.org/2025/03/31/camara-the-global-telco-api-alliance-unveils-its-spring25-meta-release-cutting-edge-apis-for-seamless-network-functions-access). **Do not conflate an open OpenAPI spec with access to the mobile operator network.** OAuth2 and subscriber consent/operator arrangements are required for production. **T-Mobile US or Aduna self-service sandbox availability for this exact hackathon: UNVERIFIED / likely approval >1 hour.** Use mocks conforming to the checked *release-tagged* OpenAPI definitions.

| Capability / official repo | Request/response meaning, illustrative | Build / pitch use |
|---|---|---|
| **SIM Swap** [OpenAPI v2.1 YAML](https://github.com/camaraproject/SimSwap/blob/r3.3/code/API_definitions/sim-swap.yaml) | `POST /sim-swap/v2/check`, `{"phoneNumber":"+15550000000","maxAge":24}` -> `{"swapped":true}`; OAuth bearer. *Check deployed base path/version against selected YAML; fixture fields align with CAMARA semantics.* | If recent change, recommend independent verification before account-reset or payment; **never auto-lock customer**. |
| **SIM swap retrieve-date** [same spec](https://github.com/camaraproject/SimSwap/blob/r3.3/code/API_definitions/sim-swap.yaml) | `POST /sim-swap/v2/retrieve-date` -> example `{"latestSimChange":"2026-11-07T12:00:00Z"}`; response may include a monitoring window; operator may suppress date for privacy. | Explain *why* stronger authentication is recommended. |
| **Device Swap** [OpenAPI repo](https://github.com/camaraproject/DeviceSwap) | Checks handset change in time window, similar conceptual boolean/time pattern; exact current path and response field **UNVERIFIED**. | Compare SIM vs device signals before flagging account-takeover risk. |
| **Number Verification** [OpenAPI repo](https://github.com/camaraproject/NumberVerification) | `POST /number-verification/{version}/verify` / `{"phoneNumber":"+15550000000"}` -> commonly documented `{"devicePhoneNumberVerified":true}`; exact current schema/version **UNVERIFIED**. | Verify device-bound possession, with explicit consent. |
| **Know Your Customer Match** [repo](https://github.com/camaraproject/KnowYourCustomerMatch) | Compares consenting supplied attributes against carrier KYC; field-level boolean/match semantics; **exact schemas/version UNVERIFIED**. | Give corroborating identity signal, not raw operator profile. |
| **KYC Tenure** [repo search](https://github.com/camaraproject) / [GSMA directory](https://gsma.com/solutions-and-impact/gsma-open-gateway/gsma-open-gateway-api-descriptions) | Evaluate whether number was active by a threshold date, commonly `tenureDateCheck: boolean`, optional contract type; **exact OpenAPI version UNVERIFIED**. | Add account age signal; avoid discriminating on prepaid status. |
| **Number Recycling** [repo search](https://github.com/camaraproject) / [CAMARA resource](https://camaraproject.org/resources) | Whether subscriber identity changed after a date, with boolean answer; exact field **UNVERIFIED**. | Avoid mistakenly contacting a new phone-number owner in recovery. |

**Fully mocked telecom request / response used in your app** (these are **simulation fixtures, not real carrier results**):

```http
POST /mock/camara/sim-swap/v2/check
Content-Type: application/json

{"phoneNumber":"+15550000000","maxAge":24}

HTTP/1.1 200 OK
Content-Type: application/json
{"swapped":true,"_mock":true,"_source":"synthetic_fixture"}
```

**Architecture:** `telecom_adapter.py` should expose consistent `check_sim_swap`, `check_device_swap`, `verify_number`, `check_tenure` calls; the production adapter remains disabled. The demo makes 2–3 visible calls but only synthetic fixtures answer. Provider URLs/auth stay in server environment variables.

## STIR/SHAKEN is a signal, not a scam verdict

- **A attestation (Full)**: originating provider authenticated customer and association/right to use the number. **B (Partial)**: authenticated customer, not verified association to the specific number. **C (Gateway)**: provider authenticated gateway entry but not the originating caller. This verifies aspects of *caller identification*, **not whether the caller is honest**. [FCC rulemaking documentation](https://www.fcc.gov/call-authentication), [2026 Federal Register](https://www.govinfo.gov/content/pkg/FR-2026-07-09/html/2026-13874.htm). **Use:** combine with unusual request patterns; never say attestation A proves safety. **How a consumer app obtains this network-layer signal directly: UNVERIFIED**; demo a mocked input.

## Banking and action tools

- **Capital One Nessie** — [Reimagine Banking API](https://api.reimaginebanking.com/). Hackathon-oriented **mock** bank customer/account/transaction/transfer API, historically API-keyed via portal. Typical operations include `GET /accounts?key=<KEY>` and `POST /accounts/{id}/transfers?key=<KEY>`, with JSON bodies for transfer details; **exact signup/limits and current endpoint availability UNVERIFIED**. **Critically: NO verified endpoint to hold or cancel an already initiated transfer.** **Use:** simulate a transaction in a standalone bank sandbox only, or easier: use your own `mock_hold_payment(transaction_id)` that changes a synthetic transaction from `PENDING` to `HELD_SIMULATED` after user approval; do not claim a real payment was stopped.

```http
POST /mock-bank/transactions/demo-1001/hold
{"reason":"possible_fraud","approved_by_user":true}

HTTP/1.1 200 OK
{"transactionId":"demo-1001","oldStatus":"PENDING","newStatus":"HELD_SIMULATED","source":"synthetic_bank_fixture"}
```

- **Reporting FTC** — [ReportFraud.ftc.gov](https://reportfraud.ftc.gov/), [FTC spam-text instructions](https://consumer.ftc.gov/articles/how-recognize-and-report-spam-text-messages). Consumer can manually submit online; **public API or supported query-field prefill UNVERIFIED**. **Use:** generate copyable incident narrative, open official reporting home page; do not auto-submit.
- **Forward SMS to 7726 (SPAM)** — [FTC guidance](https://consumer.ftc.gov/articles/how-recognize-and-report-spam-text-messages). Many mobile carriers support forwarding suspicious texts to `7726`, followed by the originating number. **Use:** user-guided instructions; direct API automation **UNVERIFIED**.
- **IdentityTheft.gov** — [official](https://www.identitytheft.gov/). Creates tailored recovery plans for victims of identity theft, with account/report flows. **Use:** present an “I shared information” recovery checklist and official link; **prefill/deep-link beyond homepage UNVERIFIED**.

## PII redaction with Microsoft Presidio
- [Presidio install](https://microsoft.github.io/presidio/installation/), [analyzer docs](https://microsoft.github.io/presidio/analyzer/): open-source detection/redaction of names, numbers, emails and other entities. Local install often needs a spaCy NLP model; **setup can exceed 1 hour** on a constrained machine. **Use:** redact sender number, name and account info before any remote Nemotron/VT request. Presidio is imperfect: also use explicit regex and masking.

```bash
pip install presidio-analyzer presidio-anonymizer
python -m spacy download en_core_web_lg
```

```python
from presidio_analyzer import AnalyzerEngine
from presidio_anonymizer import AnonymizerEngine
text = "Call 415-555-0199; email test.person@example.com"
findings = AnalyzerEngine().analyze(text=text, language="en")
redacted = AnonymizerEngine().anonymize(text=text, analyzer_results=findings).text
print(redacted)
```

## Decision rule when an API is missing or rate-limited
Never convert `no_results`, `null`, `404`, a timeout or `429` into “safe.” Report **“not found in source / unavailable”**, reduce certainty, and continue with local heuristic + user verification guidance. **Critical-path shortlist:** Nemotron + local fixtures + one working URL reputation API + RDAP; all other integrations are optional enhancements.
