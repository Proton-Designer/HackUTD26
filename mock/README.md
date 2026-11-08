# mock/
`events.json`: 3 scripted calls (IRS gift-card -> decoy, legit bank call, crypto -> hang up). Each call has `events[]` in envelope form; `ts` is a **relative offset in seconds** (replayer adds a base time and sleeps between events). Synthetic data, 555 numbers.
`check.py`: validates events.json against the schema dict inside it and that every event type in `contracts/events.md` appears. Run: `python mock/check.py`.
Note: the legit bank call includes one `handoff.restored` purely as a schema example.
