# Tricks & Tips — succeeding inside the constraints

The Grok research gave the compliance frame and the math. These are the
operational tricks that fit the actual constraints ($100, one person, NY
resident, WY LLC, no ads budget, hostile processors).

## The five leverage points

### 1. Sell the documents, not the powder
Every competitor's site says "third-party tested." Almost none show the actual
lot documents before you buy. Our entire storefront is built around publishing
lot-matched COAs per product — the COA link IS the marketing. When a lab manager
compares two $45 vials, the one with a public chromatogram wins. This costs
nothing extra: the tracker already generates the paper trail.
**Tip:** when a lot passes, add the test date and lab name to the product page
edit — "Lot C74530, tested by Janoshik 2026-09-18" reads as receipts, not claims.

### 2. One hero SKU until it pays for the other two
The instinct is a broad catalog. Resist. GHK-Cu (50 mg) is the lowest-heat SKU
(cosmetics/materials-science demand, no injectable-adjacent signaling) with the
best margin ratio. Sell ONLY GHK-Cu plus one BPC-157 size until 15 orders exist,
then add TB-500. Fewer SKUs = fewer lots to test = the $38 test reserve covers
reality, not fantasy. 3 tested lots beat 10 untested listings in every way.

### 3. The outreach machine (free channel)
The conversation says "LinkedIn/email lab managers." Make it mechanical:
- Scratch lists: university department pages (chemistry, biology, materials
  science), CRO staff pages, NIH grant award searches (public) — PIs who just
  won grants have money and needs.
- The email that works is 4 sentences: who we are (RUO distributor), what makes
  the vials different (lot-level independent docs, link), price point, "want the
  current COA?"
- The free sample trick: offer the DOCUMENT as the sample, not the vial. Sending
  a PDF COA costs zero and qualifies the buyer. Vial samples come only after
  they ask for a quote.
- 20/day, 5 days/week, tracked in suppliers.md-style notes. At ~2% conversion
  that's 2 qualified quotes/week from $0 spend.

### 4. Processor strategy: earn the boring way first
Never cloak Stripe — MATCH-listing is forever. Sequence:
1. First sales: invoice + ACH/wire/PO. Institutions pay this way natively; it's
   a FEATURE for credibility ("we bill like a vendor, not a storefront").
2. After 20+ clean orders and 60–90 days of bank history, apply to a
   high-risk MCA with: live site, LLC docs, COAs, clean bank statements.
3. Keep the invoice rail forever — reserve-holdups at processors (5–10% for
   90–180 days) hurt cash flow; institutional ACH doesn't have that problem.
Crypto settlement (if a payment partner offers it) is a last resort only —
it signals exactly what compliance reviewers worry about.

### 5. Cash-flow rules that keep you alive
- The processor reserve is invisible money. Assume 10% of every card sale is
  gone for 6 months when you compute what you can spend.
- Reorder trigger: reorder a 50-vial box when the current box hits 30% remaining
  (not when empty — China freight + customs is a 2–4 week cycle).
- Keep the "$88 conditional reserve" of the $100 untouched until a supplier has
  a signed quote; then release it against ONE SKU only.
- Owner draw $0 for 90 days. The compounding here is the customer list, not
  early profit.

## Constraint-specific tips

**One person:** every automated tool in this repo exists because you have no
staff. Run the linter before every site edit, run the economics before every
price change, run the tracker before every shipment. The system enforces the
discipline a co-founder would.

**NY resident / WY LLC:** see `LLC-STATE-DECISION.md`. One 15-minute lawyer
question (NY foreign qualification for online-only revenue) settles it. If NY
nexus is forced, use a registered-agent office address, never the home address,
in both the articles and the storefront footer — the publication requirement
prints addresses in newspapers.

**$100 budget:** the budget's real function is forcing the revenue-before-
inventory sequence. If you cannot sell the first 10-vial box to institutions
at $42–49 with pure outreach, a bigger inventory would not have saved the
business — it would have hidden the failure until it was $3k deep.

**Hostile processors/ads:** the store never needs Meta or Google. The buyers are
findable by email (that's how lab supply actually works — purchases are
initiated by quotes, not impulse clicks). This is the quiet advantage of the
vertical: the "marketing channel" is a spreadsheet and a mail client.

**Compliance drift:** the linter is the tripwire, but the human rule is simpler:
if a sentence would sound normal on a wellness influencer's page, it does not go
on this site — or in your personal posts about the business. FDA reads intended
use from everything, including the founder's profile.

## Milestones (revised for WY + one-person ops)

| When | Milestone | Proof |
|---|---|---|
| Day 7 | Domain live on the store, RFQs out to 4 suppliers | suppliers.md statuses |
| Day 14 | Counsel answer on WY; WY LLC filed; EIN; bank open | LLC-STATE-DECISION.md checked |
| Day 21 | Pilot paid (one SKU, 10 vials); retain samples frozen | orders.json |
| Day 28 | Lot passes; COA published; store goes from "quotes" to "in stock" | catalog COA links |
| Day 45 | 10 orders; second SKU added; MCA pre-application | order_tracker summary |
| Day 60 | 20+ clean orders; MCA approved; 50-vial reorder | first reserve cycle survived |
| Day 90 | 2–4 vials/day run rate; owner draw starts | $700–900/mo contribution |
