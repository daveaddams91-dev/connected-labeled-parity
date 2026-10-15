'''Quickstart: verify the main formulas on small n.

This script reproduces the table from the paper showing the 2‑adic
valuation of the number of connected labeled graphs and weakly connected
digraphs for ``n = 1..12`` and checks the known identity
``v2(c_n) - v2((n-1)!) = 1`` iff ``3`` divides ``n``.

The module can be executed as a script (``python -m examples.quickstart``)
or imported and its ``main`` function called programmatically.  All heavy
lifting is delegated to :pymod:`connected_parity`.
'''  # noqa: D400, D401

from __future__ import annotations

import math
import os
import sys
from pathlib import Path
from typing import List, Sequence

# ---------------------------------------------------------------------------
# Ensure the local ``src`` directory is on ``sys.path`` so that the package can
# be imported when the example is run from the repository root, the ``examples``
# directory, or any other location.
# ---------------------------------------------------------------------------
_SRC_ROOT = Path(__file__).resolve().parents[1] / "src"
if str(_SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(_SRC_ROOT))

try:
    from connected_parity import connected_graphs, weakly_connected_digraphs, v2
except ImportError as exc:  # pragma: no cover – defensive import guard
    raise ImportError(
        "Failed to import `connected_parity`. Ensure the package is installed "
        "or that the repository's `src` directory is on the PYTHONPATH."
    ) from exc

__all__ = ["_print_table", "_print_excess", "main"]


def _print_table(c: Sequence[int], w: Sequence[int]) -> None:
    """Print the valuation table for ``n = 1..len(c)``.

    Parameters
    ----------
    c:
        Sequence of the numbers of connected labeled graphs ``c_n``.
    w:
        Sequence of the numbers of weakly connected digraphs ``w_n``.
    """
    if len(c) != len(w):
        raise ValueError(
            f"Sequences must have the same length, got {len(c)} and {len(w)}"
        )
    print("n  v2(c_n)  v2(w_n)")
    for n in range(1, len(c) + 1):
        print(n, v2(c[n - 1]), v2(w[n - 1]))


def _print_excess(c: Sequence[int]) -> None:
    """Print the *graph excess* ``v2(c_n) - v2((n-1)!)``.

    The excess should be ``1`` exactly when ``3`` divides ``n``.
    """
    excess: List[int] = [
        v2(c[n - 1]) - v2(math.factorial(n - 1)) for n in range(1, len(c) + 1)
    ]
    print("Graph excess (should be 1 iff 3|n):", excess)


def _compute_sequences(max_n: int = 12) -> tuple[List[int], List[int]]:
    """Return the ``c`` and ``w`` sequences up to ``max_n``.

    This helper isolates the computational part, making the function easier
    to test and reuse.
    """
    if max_n < 1:
        raise ValueError("max_n must be a positive integer")
    c = connected_graphs(max_n)
    w = weakly_connected_digraphs(max_n)
    return list(c), list(w)


def main(max_n: int = 12) -> None:
    """Entry point for the quick‑start verification.

    Parameters
    ----------
    max_n:
        Upper bound for ``n`` (inclusive).  The original script uses ``12``.
    """
    c, w = _compute_sequences(max_n)

    # Basic sanity checks – the underlying library guarantees the length, but we
    # keep the explicit guard to provide a clear error message if the contract
    # ever changes.
    if len(c) != max_n or len(w) != max_n:
        raise ValueError(
            f"Expected sequences of length {max_n}, got len(c)={len(c)}, len(w)={len(w)}"
        )

    _print_table(c, w)
    _print_excess(c)


if __name__ == "__main__":
    # When executed as a script we honour the original behaviour (fixed ``n=12``).
    main()
