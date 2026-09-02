#!/usr/bin/env python3
"""RFQ generator — produces ready-to-send supplier inquiry emails.

Reads data/catalog.json SKUs and emits one email per supplier profile.
Usage:
  python rfq_generator.py --supplier "GL Biochem" --contact info@glbiochem.net
  python rfq_generator.py --list          # show tracked suppliers from data/suppliers.md
"""
import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CATALOG = json.loads((ROOT / "data" / "catalog.json").read_text(encoding="utf-8"))


def build_email(supplier: str, contact: str) -> str:
    skus = ", ".join(f"{p['name']} ({p['size']})" for p in CATALOG["products"])
    body = f"""To: {contact}
Subject: Wholesale RFQ — {supplier} x research reagent distributor (US)

Hello,

We are a US-based distributor of laboratory research reagents (RUO) preparing
a small pilot program. We are requesting quotes on the following catalog items:

  {skus}

To be considered, please provide:

1. Current-lot HPLC chromatogram AND mass-spectrometry identity report for each
   item (documents must reference the actual lot number, not a stock example).
2. Manufacturing plant city and facility type.
3. Pricing for a 10-vial pilot order per SKU, including DHL/FedEx to the US.
4. Price tiers at 10 and 50 vials per SKU.
5. Whether you can ship with our supplied label file (we act as distributor;
   labeling: "FOR LABORATORY RESEARCH USE ONLY / NOT FOR HUMAN OR ANIMAL USE").
6. Willingness to sign a quality agreement including no resale of our brand and
   no retention of our customer information for marketing.

We independently verify every lot before distribution, and we reorder on quality.
We do not purchase compounds that duplicate FDA-approved drug molecules.

Regards,
Northvale Reagents
[pending LLC name / address / phone]
orders@northvalereagents.com
"""
    return body


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--supplier", help="supplier display name")
    ap.add_argument("--contact", help="supplier contact email")
    ap.add_argument("--list", action="store_true", help="list suppliers from tracker")
    ap.add_argument("--out", help="write email to file instead of stdout")
    args = ap.parse_args()

    if args.list:
        text = (ROOT / "data" / "suppliers.md").read_text(encoding="utf-8")
        print(text)
        return
    if not (args.supplier and args.contact):
        ap.error("--supplier and --contact required (or use --list)")
    email = build_email(args.supplier, args.contact)
    if args.out:
        Path(args.out).write_text(email, encoding="utf-8")
        print(f"wrote {args.out}")
    else:
        print(email)


if __name__ == "__main__":
    main()
