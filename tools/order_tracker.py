#!/usr/bin/env python3
"""Order & lot tracker — JSON-backed CRM for the pilot phase.

Commands:
  python order_tracker.py add-order --org "Univ. Lab" --sku BPC157-5 --qty 2 --price 42 --lot C74530
  python order_tracker.py add-lot --sku BPC157-5 --lot C74530 --tested-by Janoshik --result pass --coa data/coa/BPC157-5-C74530.pdf
  python order_tracker.py list
  python order_tracker.py summary
"""
import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DB = ROOT / "data" / "orders.json"


def load():
    if DB.exists():
        return json.loads(DB.read_text(encoding="utf-8"))
    return {"orders": [], "lots": []}


def save(db):
    DB.write_text(json.dumps(db, indent=2), encoding="utf-8")


def now():
    return datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)

    o = sub.add_parser("add-order")
    o.add_argument("--org", required=True)
    o.add_argument("--sku", required=True)
    o.add_argument("--qty", type=int, required=True)
    o.add_argument("--price", type=float, required=True)
    o.add_argument("--lot", required=True, help="MUST match a tested lot before shipping")
    o.add_argument("--status", default="pending-attestation",
                   choices=["pending-attestation", "confirmed", "shipped", "cancelled"])

    l = sub.add_parser("add-lot")
    l.add_argument("--sku", required=True)
    l.add_argument("--lot", required=True)
    l.add_argument("--tested-by", required=True, help="independent lab name")
    l.add_argument("--result", required=True, choices=["pass", "fail"])
    l.add_argument("--coa", required=True, help="path to COA document")

    sub.add_parser("list")
    sub.add_parser("summary")

    a = ap.parse_args()
    db = load()

    if a.cmd == "add-order":
        tested = [x for x in db["lots"] if x["lot"] == a.lot and x["result"] == "pass"]
        order = {"date": now(), "org": a.org, "sku": a.sku, "qty": a.qty,
                 "price": a.price, "lot": a.lot, "status": a.status,
                 "lot_tested": bool(tested)}
        db["orders"].append(order)
        save(db)
        if not tested:
            print(f"⚠️  LOT {a.lot} HAS NO PASSING INDEPENDENT TEST ON FILE. "
                  f"Do not ship until 'add-lot --result pass' exists for it.", file=sys.stderr)
        else:
            print(f"✅ order recorded; lot {a.lot} verified pass.")
        print(json.dumps(order, indent=2))

    elif a.cmd == "add-lot":
        rec = {"date": now(), "sku": a.sku, "lot": a.lot, "tested_by": a.tested_by,
               "result": a.result, "coa": a.coa}
        db["lots"].append(rec)
        save(db)
        print(f"recorded lot {a.lot} ({a.result}) tested by {a.tested_by}")

    elif a.cmd == "list":
        print("LOTS:")
        for x in db["lots"]:
            print(f"  {x['date']} {x['sku']} lot={x['lot']} {x['result'].upper()} by {x['tested_by']} coa={x['coa']}")
        print("ORDERS:")
        for x in db["orders"]:
            flag = "OK" if x["lot_tested"] else "⚠ UNTESTED LOT"
            print(f"  {x['date']} {x['org']} {x['sku']}×{x['qty']} ${x['price']:.2f} lot={x['lot']} [{x['status']}] {flag}")

    elif a.cmd == "summary":
        revenue = sum(o["qty"] * o["price"] for o in db["orders"]
                      if o["status"] in ("confirmed", "shipped"))
        untested = [o for o in db["orders"] if not o["lot_tested"]
                    and o["status"] != "cancelled"]
        print(f"orders: {len(db['orders'])} | lots tested: {len(db['lots'])}")
        print(f"booked revenue: ${revenue:.2f}")
        if untested:
            print(f"⚠️  {len(untested)} order(s) on untested lots — resolve before shipping")


if __name__ == "__main__":
    main()
