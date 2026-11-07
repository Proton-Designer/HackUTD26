# WiCHacks: project cards (1 projects)

Facts and short paraphrases only; no cross-project analysis. Full records are in the workbook and JSONL.

## WiCHacks 2026

### Income Firewall  (WiCHacks 2026)

- **Prizes:** Winner Capital One: Best Financial Hack [unknown]  (tier: sponsor_winner)
- **Pitch:** Income-volatility planner for freelancers that uses bootstrap Monte Carlo simulation to recommend how much of a large paycheck to set aside, with CSV, sample and Nessie data inputs.
- **Problem / user:** Freelancers with uneven income overspend in good months and panic in bad ones; the issue is allocation, not budgeting. / freelancers, creators and gig workers
- **Domain / idea type:** fintech_finance / data_or_analytics
- **Platforms / hardware / AI:** web / False / False
- **Stack:** langs TypeScript; frontend Next.js; Tailwind CSS; Recharts; react-hook-form; backend Next.js API routes; Zod; db ; hosting Vercel
- **Tech/APIs:** Capital One Nessie API (payments, supporting, sponsor); Bootstrap Monte Carlo engine (framework, core); Next.js (framework, supporting); Recharts (framework, supporting)
- **Sponsor APIs:** Capital One Nessie API | fit: Added a Nessie adapter (with caching and graceful fallback) as one income-data source alongside CSV and synthetic profiles for the income-volatility engine, targeting Best Financial Hack.
- **Repo:** public, commits 14 (before/in/after event: 0/14/0), README detailed
- **Demo/writeup:** video False, live not_checked, screenshots 1, writeup long, impact claims False
- **Notes:** Statistical engine using bootstrap sampling, common random numbers and seasonal buckets, with an adapter pattern for CSV/Nessie/sample inputs and a backtest; solo build with no LLM.
- **Team size:** 1 | **Confidence:** medium | unverified: ui_polish; n_screenshots; what_it_does section holds lessons text; accomplishments/learned/next_steps headings empty on page
- **Links:** [Devpost](https://devpost.com/software/income-firewall) | [GitHub](https://github.com/ash413/income-firewall)
