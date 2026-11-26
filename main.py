#!/usr/bin/env python3
"""The Self-Checkout Is Judging You.

One line in the voice of a smug self-checkout machine, to a shopper
buying twelve yoghurts and nothing else: it has scanned enough baskets
to tell meal prep from a cry for help, and this basket is the second one.
"""

import os

ENTRY = (
    "Twelve yoghurts, zero other food. I've seen meal prep, "
    "and I've seen a cry for help. This is the second one."
)


def main() -> None:
    output_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as handle:
        handle.write(ENTRY + "\n")
    os.chmod(output_path, 0o644)


if __name__ == "__main__":
    main()
