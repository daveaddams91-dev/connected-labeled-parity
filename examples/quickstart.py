"""Quickstart: verify the main formulas on small n.

This script reproduces the table from the paper showing the 2-adic
valuation of the number of connected labeled graphs and weakly connected
digraphs for n = 1..12, and checks the known identity
v2(c_n) - v2((n-1)!) = 1 iff 3 divides n.
"""

from __future__ import annotations

import math
import os
import sys
from typing import Sequence

# Ensure the local src directory is on the import path so that
# `connected_parity` can be found when the script is run from the
# repository root or from the examples directory.
sys.path.insert(
    0,
    os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")),
)

try:
    from connected_parity import connected_graphs, weakly_connected_digraphs, v2
except ImportError as exc:  # pragma: no cover - defensive
    raise ImportError(
        "Failed to import `connected_parity`. Make sure the package is installed "
        "or that the repository's `src` directory is on the PYTHONPATH."
    ) from exc


def _print_table(c: Sequence[int], w: Sequence[int]) -> None:
    """Print the valuation table for n = 1..len(c)."""
    print("n  v2(c_n)  v2(w_n)")
    for n in range(1, len(c) + 1):
        print(n, v2(c[n - 1]), v2(w[n - 1]))


def _print_excess(c: Sequence[int]) -> None:
    """Print the graph excess v2(c_n) - v2((n-1)!)."""
    excess = [
        v2(c[n - 1]) - v2(math.factorial(n - 1))
        for n in range(1, len(c) + 1)
    ]
    print("Graph excess (should be 1 iff 3|n):", excess)


def main() -> None:
    """Entry point for the quickstart verification."""
    # Compute values up to n = 12 as in the original script.
    c = connected_graphs(12)
    w = weakly_connected_digraphs(12)

    # Basic sanity checks: sequences should have length 12.
    if len(c) != 12 or len(w) != 12:
        raise ValueError(
            f"Expected sequences of length 12, got len(c)={len(c)}, len(w)={len(w)}"
        )

    _print_table(c, w)
    _print_excess(c)


if __name__ == "__main__":
    main()
