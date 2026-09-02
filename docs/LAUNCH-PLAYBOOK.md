# Launch Playbook — Northvale Reagents

Built from the Grok peptide e-commerce research (see `KNOWLEDGE-BASE.md`).
This playbook sequences the $100 bootstrap so cash only converts when
validated steps pass.

---

## The model (decided up front)

**Strict RUO research-reagent distributor.** Private label into our own control
is the later upgrade; consumer "peptide therapy" retail is never the model.
No GLP-1s, no approved-drug molecules, no protocols, no outcome copy, ever.

## What is already built (this repo, $0)

| Asset | Status |
|---|---|
| Live storefront with age gate + typed attestation + COA links | ✅ https://pmb2.github.io/peptide-reagent-store/ |
| Quote/invoice checkout (PO / wire / ACH — processor-agnostic) | ✅ live |
| Claims linter (compliance tripwire on every build) | ✅ tested, catches violations |
| RFQ email generator (3 pilot SKUs, 6-point requirements) | ✅ tested |
| Unit-economics calculator (breakeven, margin warnings) | ✅ tested |
| Order & lot tracker (blocks shipping untested lots) | ✅ tested |
| Supplier tracker + red-flag list | ✅ |
| Knowledge base + verified sources | ✅ |
| Budget model | ✅ `BUDGET-100.md` |

## The $100 allocation (committed now)

- **$10–12** — domain (Namecheap/Porkbun). Do this first; point it at the
  GitHub Pages site + Zoho Mail free-tier email. Everything else stays $0.
- **$50 held** — inventory match: releases only when a supplier quote with a
  real lot-COA comes back under $15/vial landed.
- **$38 held** — first independent test co-pay: releases with pilot revenue or
  alongside the inventory release.

## 30-day sequence

### Week 1 — paper + presence ($12)
1. Buy domain, wire to Pages, create `orders@` mailbox (Zoho free tier).
2. One-hour consult with a food-and-drug lawyer ($400–750 — this is the one
   cash item NOT in the $100; save for it or defer inventory one week). Ask:
   RUO resale to individuals in NY, SKUs to avoid, residential shipping policy.
3. File NY LLC online ($200 — again outside the $100; sequence at week 2–3 from
   savings/revenue). Glenville/Schenectady office keeps publication upstate.
   Publication must complete within 120 days.
4. EIN (free, same day). Business checking. Never mix funds.

### Week 2 — suppliers ($0 until quotes land)
5. Send RFQs via `python tools/rfq_generator.py --supplier "<name>" --contact <email>`
   to: GL Biochem, Chinese Peptide Company, Inno Peptides, Aavant Research.
6. Score replies against the red-flag list in `docs/data/suppliers.md`.
   No lot-matched COA → walk. Won't name plant city → walk.
7. Log everything in the supplier tracker.

### Week 3–4 — pilot buy + test ($50 reserve + ~$150–400 testing)
8. Order 10 vials each of 2–3 SKUs ONLY from a supplier who passed step 6–7.
   Treat the wire as money that might vanish (customs).
9. On arrival: photograph packaging, freeze retain samples, send 1 vial/SKU to
   Janoshik or MZ Biolabs ($150–400 each).
10. `add-lot --result pass/fail` — fail = destroy, document, switch supplier.
11. Link real COAs in `docs/data/catalog.json` (vial lot = COA lot = report lot).
    **The store lists nothing until this line exists.**

### Week 4–5 — first revenue ($0 media)
12. Publish only passing lots. Price per `unit_economics.py` defaults ($42–49).
13. Outreach (the bootstrap channel): LinkedIn/email to CRO and university lab
    managers; your local research contacts. 20 contacts/week. Personalized,
    boring, institutional. No health language — ever.
14. Orders via quote flow → attestation → `add-order` in tracker (untested lots
    are blocked automatically) → ship as laboratory reagents, disclaimer on
    pack slip. Cancel any order that reads like personal use; refund fast.

### Month 2 — consolidation
15. 20+ clean orders → apply to a high-risk merchant account with the live
    site. Expect 3.5–6% + 5–10% reserve 90–180 days. Never Stripe, never cloak.
16. Reorder 50-vial boxes of winners only. Dual-source the hero SKU.
17. Only now consider $10–20/day ads: supplier-positioned copy, chromatogram
    creative, lab-manager targeting. Landing page more conservative than the ad.
18. Owner draw stays $0 until 90 days of processing history.

## Pitfall register (each one is a business-killer)

| Pitfall | Control |
|---|---|
| FDA intended-use drift (copy, kits, consumer vibes) | Claims linter on every build; institutional tone; no blog |
| Untested/misfilled lots with our label | Tracker blocks untested lots; independent test per lot; retain samples |
| Customs seizure of China shipment | Budgeted as possible loss; first order sized to survive it |
| Processor freeze/MATCH-listing | Never Stripe; never cloak; apply only with clean live site |
| Shopify/warehouse-apps de-platforming | Static own-domain site (Pages) + invoice rails |
| Supplier clones storefront/customer list | Quality agreement clause in RFQ; brand files owned by us |
| Cash trapped in processor reserve | Plan cash as if 10% doesn't exist for 180 days |
| NY LLC publication lapse (120d) | Calendar it at formation |
| Personal-use orders polluting intended use | Attestation + cancel-and-refund discipline |
| GLP-1 gravity (easy money temptation) | Hard no — blocked in catalog data and this playbook |

## Profitability math (defaults in `unit_economics.py`)

- Contribution ≈ **$22/vial** ($49 list, $12 landed, shipping+fees+reserve in)
- Software-only fixed ≈ $35/mo → **breakeven ≈ 2 vials/month**
- 10-vial pilot per SKU sells through at ~1–2 orders/week per SKU from pure
  outreach → Month-2 reorder is funded by revenue, not the $100.
- Target state, day 60: 3 SKUs live, 30–40 vials/mo, ≈ $700–900 contribution,
  zero debt, reserve accumulating for the licensed-channel option later.

## When to walk away

If after 4 RFQs no supplier produces a lot-matched COA, or the lawyer says RUO
resale to individuals is a non-starter in NY, stop. The $12 domain is the total
loss. That is the point of this structure — the downside is capped at noise,
and every expensive step is gated behind a validated cheap one.
