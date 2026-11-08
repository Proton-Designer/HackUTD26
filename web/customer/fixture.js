// Local fixture built from 00_SHARED_RULES §3. Swap for mock/events.json once eng1 commits it.
// t = ms after replay start.
window.BACKFIRE_FIXTURE = [
  { t: 500,  type: "call.incoming", call_id: "demo-1", data: { from: "+1 (214) 555-0147", to: "+1 (972) 555-0100", attestation: "C", scam_id_score: 0.82 } },
  { t: 600,  type: "call.routed",   call_id: "demo-1", data: { decision: "LIVE_GUARD", reason: "Caller ID not verified" } },
  { t: 0,    type: "call.answered", call_id: "demo-1", data: { ended_by: null }, onAnswer: true },
  { t: 4000, type: "transcript.caller", call_id: "demo-1", data: { utterance_id: "u1", text: "This is the IRS. There is a warrant for your arrest.", is_final: true }, afterAnswer: true },
  { t: 9000, type: "risk.update", call_id: "demo-1", data: { s: 0.93, band: "ALERT", asks: ["gift_card"], scam_type: "gov_impersonation", stage: "pressure", impersonates: "IRS", addresses_ai_system: false, why_chips: ["Claims to be the IRS", "Asked for a gift card", "Known scam campaign"], engine: "cloud" }, afterAnswer: true },
  { t: 9100, type: "alert.fired", call_id: "demo-1", data: { level: "first", why_chips: ["Claims to be the IRS", "Asked for a gift card", "Known scam campaign"] }, afterAnswer: true }
];
