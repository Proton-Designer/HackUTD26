# PNC Bank - HackUTD 2026 brief
Legend: [V] verified from a page I fetched; [U] unverified/inferred.

## 1. Who they are
- PNC Financial Services: large US retail, corporate and institutional bank. [U: general knowledge, no page fetched]
- Publishes commercial payments APIs: RTP Bank Eligibility, Send RTP Credit, Direct-to-Debit-Card, Bank Routing Number Verification, Account Verification (Verify/Authenticate), Check Deposit. [V: pnc.com "A look at PNC's APIs"]

## 2. HackUTD 2026 prize/challenge
- Tier: Platinum sponsor. [V: zeroday.hackutd.co]
- PNC Workshop Saturday 2:30pm (Nov 7). [V: same page]
- Event: Nov 7-8, 2026, ECSW. Page says "24-hour hackathon" (your brief said 36h - check). [V]
- Challenge text: NOT PUBLIC. Site says "This year's challenge tracks will be announced once hacking starts." [V] Prize amounts for 2026: not public.
- Reference, 2025 prizes (not 2026): 1st PlayStation 5 Slim, 2nd Ray-Ban Meta AI Sunglasses, 3rd Yaber T1 Pro-Mini projector; 2025 challenge statements were in a "hackerpack" released when hacking starts; max 2 sponsor challenges per submission (MLH ones excluded). [V: hackutd-2025.devpost.com]

## 3. Products/APIs
- PNC APIs (list above): https://www.pnc.com/insights/corporate-institutional/gain-market-insight/a-look-at-pncs-apis.html [V that they exist]
- Dev portal: https://developer.pnc.com - fetched page only says it covers payments and account verification; sandbox/signup/docs details NOT confirmed. [V partial] These are commercial treasury APIs and likely need a business relationship; assume no self-serve access in 36h unless PNC provides a sandbox/mock at the workshop. [U]
- Any hackathon-specific credits/tooling: not public.

## 4. Prior hackathon sponsorship
- HackUTD 2025 (Nov 2025): PNC prize listed, see above. [V] Winning PNC projects: could not identify; gallery pages did not show prize labels (367 submissions). https://hackutd-2025.devpost.com/project-gallery
- HackUTD 2023 (X) and 2022 (IX) Devpost pages (hackutd-x / hackutd-ix.devpost.com): PNC not listed. [V] (year mapping to 2022/2023 inferred from "10th installment Nov 4" Mercury article.) PNC appears as a past HackUTD sponsor logo on hackutd.co. [V]
- HackUTD 2024: Devpost page not fetchable; PNC role unknown. Other Texas events: not found in my searches. [U]
- Search result noted 2025 gallery themes: many PM tooling, API-regression, vendor-onboarding (TrustIssues.AI, Stamped) projects - but not tied to PNC. [V as projects; U as PNC winners]

## 5. Judging values and project directions (INFERENCE)
- Evidence is thin: no public rubric. Their API portfolio (payments, verification, check deposit) suggests fintech/fraud/payments relevance. [U]
- Directions [all inference]:
  1. Account/payee verification and fraud-prevention flow mocking PNC Verify/Authenticate + routing validation.
  2. Instant-payout (RTP/debit-push) tool for gig workers or small business with eligibility fallback logic.
  3. Mobile check-deposit / document-capture assistant with AI validation and accessibility focus.

## 6. Questions for the booth
- What are the challenge tracks and judging rubric? Is it the same "hackerpack" format as 2025?
- Are any PNC APIs available in a sandbox or mock for the weekend? How to get keys (do not paste into repos)?
- Can we use real-looking data? Compliance restrictions?
- Does the workshop at 2:30pm cover API access? Do prizes go per team member?
- Is there a recruiting/internship angle for winners?

## Sources
- https://zeroday.hackutd.co [V]
- https://hackutd.co [V]
- https://hackutd-2025.devpost.com and /project-gallery [V]
- https://hackutd-x.devpost.com, https://hackutd-ix.devpost.com [V]
- https://www.pnc.com/insights/corporate-institutional/gain-market-insight/a-look-at-pncs-apis.html [V]
- https://developer.pnc.com [V partial]
- https://utdmercury.com/?p=27550 (10th installment) [search snippet only]
