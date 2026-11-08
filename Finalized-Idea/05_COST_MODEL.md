# Cost model (rough estimates: recheck prices before putting any on a slide)

## Per screened minute
| Piece | Self-hosted on NVIDIA GPUs | Commercial APIs |
|---|---|---|
| Speech-to-text, caller's side only (Parakeet/Riva on GPU) | ~$0.0001/min | ~$0.004–0.02/min |
| Nemotron scoring (~4×/min, ~6K tokens/min; Nemotron 3 Nano is MoE with ~3B active params; one ~$2.50/hr GPU handles ~100+ concurrent calls) | ~$0.0003/min | ~$0.001–0.005/min |
| **Total** | **≈ $0.0005–0.001/min** | **≈ $0.005–0.025/min** |

## At T-Mobile scale
Assumptions: ~142M customers, 10% opt in, ~20 min/month of unknown-number calls each.
- That's ~280M screened minutes per month.
- **Self-hosted ≈ $3–4M/yr ≈ $0.02 per opted-in user per month.**
- Commercial APIs ≈ $20–80M/yr.
- Decoy (v2): runs only when a customer presses Scammer Get Scammed, so volume is bounded by alerts. Even 1M decoy calls × 5 min costs under ~$250K/yr self-hosted, including voice synthesis.
- Local implementation: detection compute moves to the customer's phone ($0 to T-Mobile), but decoy, voice and intel stay in the cloud.

## Compared with what it protects
- 0.01 point of postpaid churn ≈ **$78M/yr**.
- One assisted care contact ≈ **$13.50**. Avoiding ~250K contacts a year covers the self-hosted cost.
- Scam Shield Premium costs **$4 per line per month**. Compute at ~$0.02 per user per month is ~0.5% of that.

## Local implementation (Nemotron 3 Nano 4B / Bolt E4B on the device): no detection compute bill, but trade-offs
- The model fits (4-bit ≈2.5GB). In production it needs Android (iOS gives apps no call audio and suspends them during calls). In the demo it works on any phone, because the backend relays the caller's audio.
- Smaller model: measure its accuracy against the cloud detector on the same test set.
- Two platforms to build, a ~2.5GB model download, and battery and heat on the customer's phone.
- The cloud is still needed for the decoy, network-wide blocking and burn tools.

## NVIDIA angle
For NVIDIA, cloud inference is revenue, not cost. T-Mobile already works with NVIDIA on AI-RAN (GPUs inside the cell network). Pitch "could run on AI-RAN" as an idea, not a fact.
