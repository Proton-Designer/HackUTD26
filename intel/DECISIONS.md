# intel/ decisions (P4a)

- Lookups are plain functions with a CLI, not a service yet: fastest to test and easy for the intel agent to call as tools later.
- RDAP via rdap.org: one public endpoint that redirects to the right registry for any TLD, no key.
- BTC via blockstream.info (gives total received + tx count, no key). ETH via eth.blockscout.com (no key; gives balance + tx count, not total received). Demo wallet should be BTC so "total received" shows.
- Fail open: any network error or timeout returns status "unavailable" and still emits an event. Never raises.
- Allowlist is a seeded JSON of published bank/agency numbers and domains, marked seed data. A match is never actioned; when a scammer gives one, the gate flags attempted poisoning.
- Events: printed as contract envelopes; also POSTed to BACKFIRE_EVENTS_URL if P1 exposes a publish endpoint (to agree with Ayman).
- Only public read-only lookups. Nothing contacts scammer infrastructure.
