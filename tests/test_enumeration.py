"""Tests for enumeration recurrences and 2-adic formulas."""
import math
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from connected_parity.enumeration import (
    v2,
    v2_factorial,
    connected_graphs,
    weakly_connected_digraphs,
    connected_hypergraphs,
    predicted_graph_v2,
    predicted_weak_digraph_v2,
)
from connected_parity.brute import brute_connected_graphs, brute_weak_digraphs


def test_known_graph_values():
    # OEIS A001187: 1, 1, 4, 38, 728, 26704, 1866256 for n = 1..7
    c = connected_graphs(7)
    assert [c[n] for n in range(1, 8)] == [1, 1, 4, 38, 728, 26704, 1866256]


def test_known_weak_digraph_values():
    # Cross-checked totals: sum over components; w_1=1, w_2=3, w_3=54?
    # Verify recurrence internal consistency instead of hardcoding:
    # total_n = sum_{m} C(n-1,m-1) w_m 2^{(n-m)(n-m-1)}
    from math import comb
    w = weakly_connected_digraphs(6)
    assert w[1] == 1
    assert w[2] == 3  # 4 digraphs total, 1 disconnected (empty)
    for n in range(1, 7):
        total = 2 ** (n * (n - 1))
        recon = sum(comb(n - 1, m - 1) * w[m] * 2 ** ((n - m) * (n - m - 1)) for m in range(1, n + 1))
        assert recon == total


def test_graph_recurrence_consistency():
    from math import comb
    c = connected_graphs(12)
    for n in range(1, 13):
        total = 2 ** (n * (n - 1) // 2)
        recon = sum(comb(n - 1, m - 1) * c[m] * 2 ** ((n - m) * (n - m - 1) // 2) for m in range(1, n + 1))
        assert recon == total


def test_v2_factorial_matches_math():
    for m in range(0, 50):
        assert v2_factorial(m) == v2(math.factorial(m)) if m >= 1 else v2_factorial(0) == 0


def test_graph_formula_small():
    c = connected_graphs(40)
    for n in range(1, 41):
        assert v2(c[n]) == predicted_graph_v2(n), f"fail at n={n}"


def test_weak_digraph_formula_small():
    w = weakly_connected_digraphs(30)
    for n in range(1, 31):
        assert v2(w[n]) == predicted_weak_digraph_v2(n), f"fail at n={n}"


def test_brute_graphs():
    c = connected_graphs(5)
    for n in range(1, 5):
        assert brute_connected_graphs(n) == c[n]


def test_brute_weak_digraphs():
    w = weakly_connected_digraphs(4)
    for n in range(1, 4):
        assert brute_weak_digraphs(n) == w[n]


def test_hypergraph_boundary_breaks_pattern():
    # For 3-uniform hypergraphs the clean formula fails: exhibit explicit n.
    ch = connected_hypergraphs(3, 15)
    fails = [n for n in range(1, 16) if v2(ch[n]) != v2_factorial(n - 1) + (1 if n % 3 == 0 else 0)]
    assert len(fails) > 0
