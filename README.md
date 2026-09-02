# Northvale Reagents — Bootstrap Peptide Reagent Store

A **research-reagent (RUO) storefront + operations toolkit** built from the Grok
peptide e-commerce research. Name is a placeholder — swap after counsel review.

## What's here

| Path | What it is |
|---|---|
| `docs/KNOWLEDGE-BASE.md` | Synthesized findings from the Grok conversations (suppliers, costs, compliance rules) |
| `docs/SOURCES.md` | Verified external sources with status |
| `docs/BUDGET-100.md` | The $100 allocation model |
| `docs/LAUNCH-PLAYBOOK.md` | 30-day launch sequence, pitfalls, profitability plan |
| `store/` | Static storefront (catalog, age gate, attestation, COA links) |
| `tools/` | Python automation: RFQ generator, claims linter, unit economics, order tracker |
| `data/` | JSON data: catalog, suppliers, orders, test results |

## Compliance position (non-negotiable)

This is a **laboratory research-reagent business**. No health claims, no protocols,
no dosing guidance, no consumer kits, no syringes/BAC water, no GLP-1 compounds.
The claims linter enforces this on every build.
