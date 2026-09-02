# Knowledge Base — from Grok conversations (verified extraction, Sep 2 2026)

Source conversations (grok.com, exported via REST API):
- ★ `Peptides E-commerce Compliance Guide` (a66e0cda) — 6 turns, strategy/suppliers/costs
- `Ipamorelin Tesamorelin Dosage Guide` (471ebbe2) — 22 turns, personal-use protocol notes
- `Expired peptide blend safety and dosing` (5cc7dd00) — 10 turns, stability/safety notes

Raw transcripts: `C:\Users\TBA\Documents\grok-peptides\convo_*.md`

## 1. The regulatory core (why the model is what it is)

- Selling peptides as unapproved drugs for human use is the core FD&C Act problem.
  "For research use only" only holds if **everything** looks like reagent sales to labs:
  no protocols, no before/after, no health/outcome copy, no syringe+BAC-water kits,
  no consumer targeting.
- FDA judges **intended use** from the whole operation: site copy, ads, accessories,
  reviews, who you ship to — not the RUO badge. Residential drop-ship of injectable-
  looking peptides to people with personal cards is the exact pattern FDA treats as
  human-use evidence.
- **Highest-risk SKUs to never stock**: molecules identical to approved drugs
  (semaglutide, tirzepatide, tesamorelin, etc.).
- Enforcement, vendor shutdowns, and processor bans all increased 2024–2026.
- Two real businesses exist: (1) strict RUO reagent distributor ← this build;
  (2) licensed channel (clinician + 503A/503B + LegitScript) — different capital class.

## 2. Suppliers (from conversation, to be validated by RFQ)

### Manufacturers worth the first RFQ
| Supplier | Role | Cost tier | Note |
|---|---|---|---|
| GL Biochem (Shanghai) | Largest research-peptide mfr | Mid | `info@glbiochem.net` — first wholesale inquiry |
| Chinese Peptide Company | Direct mfr/exporter | Competitive | Large public third-party test footprint |
| WuXi TIDES | Pharma CRDMO | Premium | Quality ceiling, not a shopping cart |
| GenScript | US contract possible | Higher | Cleaner vendor-of-record for a US LLC |
| Hybio Pharmaceutical | Listed peptide API co | Mid-premium | Better paper trail than Telegram resellers |
| Bachem / PolyPeptide | Western GMP | Highest | Only for a licensed channel later |

### Cost labs (Finnrick-style Aug 2026 snapshot — treat names/domains as unstable)
- Better score/cost: Inno Peptides (88%, ~$0.70/mg, 29 tests), Marvel Pep (88%, ~$1.00, 18),
  Chimera (87%, ~$1.00, 23), Retalux (87%, ~$0.93, 17)
- Lowest $/mg (highest prove-it burden): Wuhan Newtop ~$0.09 (6 tests), Jinan Elitepeptide
  ~$0.30 (12), Lotus Bio ~$0.34 (5)
- US-facing quotes: Aavant Research ~$0.65 (21 tests), Amino Lair ~$1.27 (19)

### Quality rule (non-negotiable)
Lot-specific HPLC chromatogram + MS identity per lot; send first lots to an independent
lab (Janoshik, MZ Biolabs, or ISO 17025 lab, $150–400/sample). Vial lot = COA lot =
lab-report lot. Dual-source hero SKUs. Failed lot = destroy, don't sell, document, switch.

## 3. Unit economics (lean, from conversation)

- Landed cost target: 10 mg vial at **~$10–15 all-in**; list **$45–55** as a reagent.
- Example: $12 landed / $49 list / $8.50 ship / 4.5% processing / 8% reserve-refund buffer
  → variable ≈ $27/vial → contribution ≈ **$22/vial**
- Lean overhead ≈ $335/mo → **breakeven ≈ 16 vials/month**
- China wholesale often starts at 1 box = 10 vials; 50-vial tiers once real.
- High-risk processors: 3.5–6% + 5–10% rolling reserve for 90–180 days.
- Retail reference 2026: ~$25–50 for 5 mg BPC-157; ~$30–60 for 5 mg TB-500.

## 4. Compliance feature list for the site (from conversation)

- Age gate + typed research attestation at entry and at checkout
- Lot COAs linked on every product page
- Boring institutional copy; LLC name, address, phone in footer
- No blog, no "peptide therapy", no dosing, no outcomes
- Banned words in copy: heal, tendon, gut, weight loss, inject, units, cycle,
  Ozempic, peptide therapy, glow, transform (+ dosage, dose, injection, results)
- Payments: high-risk merchant account or invoice/ACH/wire/crypto rails — never
  apply to Stripe as a peptide shop; never cloak. Shopify dies often; WooCommerce
  on own domain is the stack processors will review. This build: static store +
  invoice/quote checkout until processor is approved.

## 5. Ads lane (only after site is conservative end-to-end)

- Advertise the **supplier**, not outcomes. Target lab managers, chemists, CRO procurement.
- Creative: chromatograms and plain RUO vials; never syringes-in-hand or before/after.
- Brand-search easier than non-brand. Influencer "I ran BPC" content = intended-use
  evidence against you. $10–20/day cap, research-supplier copy only, expect rejections.

## 6. 30-day sequence (from conversation, adapted)

1. Lawyer + LLC + bank + domain
2. RFQ GL Biochem + one mfr + two cost labs
3. RUO site live; apply to high-risk processor
4. Pilot 2–3 non-GLP-1 reagents (10 vials each)
5. Independent tests; sell only passing lots
6. Soft launch to lab contacts (LinkedIn/email outreach — the bootstrap channel)
7. Ads only after 20+ clean orders

## 7. From the personal-use conversations (context only, NOT for the store)

- The user's own protocol notes (Tesamorelin/Ipamorelin 6/2 blend, BAC reconstitution,
  fasted timing, side-effect management) are personal-journal material. They must
  never appear in store copy — they are exactly the "protocol/dosing" content that
  converts a reagent store into an unapproved-drug operation.
- Expired-peptide stability discussion reinforces the QC rule: potency is not
  guaranteed past EXP; independent testing per lot is the control.
