# Pitch (P4b, Rayan)

Table pitch for judging: 4 minutes of deck plus live demo, then open Q&A.

- **Deck (Google Slides, 8 slides):** https://docs.google.com/presentation/d/1n5TyV86wL2546wV_2QbDOF7LUigL-KYgmdKjkpfrJDw/edit
  Every slide's spoken line is in its speaker notes.
- **`script.md`:** the full run of show: who says what, slide by slide, the demo steps, the two-line scam card for the demo call, failure lines, and what's still open before judging.
- **`facts.json`:** the words and numbers on the slides, with sources. The deck is generated from this file.
- **`deck-state.json`:** slide IDs and last-written text, so the next deck update can tell if someone edited a slide by hand.

## Deck order

1. Cover (stays up during Kareem's opener and the dunk)
2. Maria, 78: the fake "your bank" fraud-alert call, plus how fast that scam is growing (FTC)
3. $3,000 vs $599: phone-started scams cost the most (FTC)
4. Before / during / after: once a scam call gets through, nothing helps her
5. Caller Beware: the three buttons, plus proof that scammers stay on with AI decoys (GSMA/TPG, two studies)
6. Follow the scam, not the number: what the decoy gets and where T-Mobile uses it
7. Live demo, then how it works (Ayman)
8. Test results: cloud vs local vs keyword rules (placeholders until the eval runs finish), then the close

## Still open

- Slide 8 numbers: cloud, local and keyword rules (Ayman's eval runs).
- Demo card switched to the bank "safe account" scam to match slide 2: run it once on the live line.
- Real demo domain and a team-made wallet in `intel/demo_config.json` (still a placeholder domain and the Bitcoin genesis address).
- Q&A cards and the Devpost draft are still the earlier 2-minute version and haven't been updated yet.
