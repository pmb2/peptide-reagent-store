#!/usr/bin/env python3
"""Claims linter — compliance tripwire for the reagent store.

Scans any text file (or all files under store/ and data/) for language that
converts a research-reagent business into an unapproved-drug operation.
Banned terms come from the Grok compliance conversation + FDA intended-use logic.

Exit codes: 0 = clean, 1 = violations found, 2 = usage error.
"""
import re
import sys
from pathlib import Path

# Words/phrases that imply human use, outcomes, or consumer marketing.
BANNED = [
    # outcome / health claims
    r"heal\w*", r"\bcure\b", r"treat\w*", r"therapeut\w*", r"anti-?aging",
    r"weight loss", r"fat loss", r"recovery", r"recover(y)? (faster|time)",
    r"\bglow\w*", r"transform\w*", r"regenerat\w*", r"repair\w*",
    r"anti-?inflammator\w*", r"\bwound\b", r"\btendon\w*", r"\bgut\b",
    r"joint pain", r"muscle growth", r"lean mass", r"\bbenefits?\b",
    # human-use language
    r"inject\w*", r"sub-?q\b", r"subcutaneous", r"pin(ned|ning)?\b",
    r"dosage", r"\bdose[sd]?\b", r"\bdosing\b", r"\bunits?\b.*(syringe|per day|daily)",
    r"reconstitut\w*", r"bacteriostatic", r"\bbac water\b", r"\bcycle\b",
    r"stack\w*", r"protocol\w*", r"before.{0,12}after", r"results",
    # consumer-funnel language
    r"peptide therapy", r"ozempic", r"semaglutide", r"tirzepatide",
    r"tesamorelin", r"retatrutide", r"ghrp", r"\bbio-?hack\w*",
    r"anti-?inflammatory", r"\b libido\b", r"testosterone boost\w*",
    r"skin care", r"cosmetic", r"anti-?wrinkle",
]
# Terms allowed ONLY inside compliance/disclaimer contexts are handled by
# ALLOW_CONTEXT below (lines containing these markers are exempt).
ALLOW_CONTEXT = ["not for human", "research use only", "no ", "do not", "never",
                 "banned word", "banned term", "not drugs", "disclaimer"]

COMPILED = [re.compile(p, re.I) for p in BANNED]


def scan_text(text: str, filename: str = "<text>") -> list[str]:
    violations = []
    for i, line in enumerate(text.splitlines(), 1):
        # Exempt obvious prohibition/compliance lines ("We do not sell...", disclaimers)
        low = line.lower()
        if any(ctx in low for ctx in ALLOW_CONTEXT):
            continue
        for rx in COMPILED:
            m = rx.search(line)
            if m:
                violations.append(f"{filename}:{i}: banned term '{m.group(0)}' -> {line.strip()[:110]}")
                break
    return violations


def main():
    if len(sys.argv) > 1:
        paths = [Path(p) for p in sys.argv[1:]]
    else:
        root = Path(__file__).resolve().parent.parent
        paths = [p for pat in ("store/**/*", "data/catalog.json")
                 for p in root.glob(pat) if p.is_file()]
    all_v = []
    for p in paths:
        if not p.exists():
            print(f"skip (missing): {p}", file=sys.stderr)
            continue
        try:
            text = p.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        all_v += scan_text(text, str(p))
    if all_v:
        print(f"CLAIMS LINTER: {len(all_v)} violation(s)\n")
        print("\n".join(all_v))
        sys.exit(1)
    print("CLAIMS LINTER: clean — no banned terms found.")
    sys.exit(0)


if __name__ == "__main__":
    main()
