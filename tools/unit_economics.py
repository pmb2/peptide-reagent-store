#!/usr/bin/env python3
"""Unit economics calculator — vial-level P&L and breakeven.

Defaults carry the Grok conversation's lean model ($12 landed / $49 list).
Usage:
  python unit_economics.py                       # defaults
  python unit_economics.py --landed 11 --list 45 --ship 8.50 --fee 4.5 --reserve 8
"""
import argparse

PCT = 100.0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--landed", type=float, default=12.0, help="all-in cost per vial ($)")
    ap.add_argument("--list", type=float, default=49.0, help="list price per vial ($)")
    ap.add_argument("--ship", type=float, default=8.50, help="shipping cost per order ($)")
    ap.add_argument("--fee", type=float, default=4.5, help="processing fee (%% of revenue)")
    ap.add_argument("--reserve", type=float, default=8.0, help="reserve+refund buffer (%% of revenue)")
    ap.add_argument("--fixed", type=float, default=35.0, help="monthly fixed overhead ($)")
    ap.add_argument("--vials", type=float, default=1.0, help="vials per order")
    a = ap.parse_args()

    revenue = a.list * a.vials
    processing = revenue * a.fee / PCT
    buffer = revenue * a.reserve / PCT
    variable = a.landed * a.vials + a.ship + processing + buffer
    contribution = revenue - variable
    margin = contribution / revenue * PCT
    be = a.fixed / contribution if contribution > 0 else float("inf")

    print(f"""
══════════════════════════════════════════════════
 UNIT ECONOMICS — per order of {a.vials:.0f} vial(s)
══════════════════════════════════════════════════
 Revenue              ${revenue:8.2f}
 Landed product cost  -${a.landed * a.vials:8.2f}
 Shipping             -${a.ship:8.2f}
 Processing ({a.fee}%)     -${processing:8.2f}
 Reserve/refund ({a.reserve}%) -${buffer:8.2f}
 ────────────────────────────────────────
 Variable cost        ${variable:8.2f}
 CONTRIBUTION         ${contribution:8.2f}   ({margin:.1f}% margin)
 Monthly fixed        ${a.fixed:8.2f}
 BREAKEVEN            {be:.1f} vials/month
══════════════════════════════════════════════════
 Reference (Grok lean model): $12 landed / $49 list
   → contribution ≈ $22/vial, breakeven ≈ 16 vials/mo
     at $335/mo overhead. Software-only overhead here
     (~$35/mo) drops breakeven to ~2 vials/mo.
""")
    if margin < 35:
        print("⚠️  Margin under 35% — renegotiate landed cost or raise list price before scaling.")
    if be < 3:
        print("✅ Breakeven under 3 vials/month — very defensible for a bootstrap.")


if __name__ == "__main__":
    main()
