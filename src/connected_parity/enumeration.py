"""Connected labeled structures: exact enumeration recurrences."""
from __future__ import annotations

from math import comb


def v2(num: int) -> int:
    """2-adic valuation. Returns large sentinel for 0 (used for empty counts)."""
    if num == 0:
        return 10**9
    v = 0
    while num % 2 == 0:
        v += 1
        num //= 2
    return v


def v2_factorial(m: int) -> int:
    """v_2(m!) via Legendre: m - popcount(m) in binary."""
    return m - bin(m).count("1")


def connected_graphs(limit: int) -> list[int]:
    """c[n]: connected labeled graphs on n vertices (OEIS A001187).

    c_n = 2^{C(n,2)} - sum_{m=1}^{n-1} C(n-1,m-1) c_m 2^{C(n-m,2)}.
    """
    c = [0] * (limit + 1)
    for n in range(1, limit + 1):
        total = 2 ** (n * (n - 1) // 2)
        acc = 0
        for m in range(1, n):
            acc += comb(n - 1, m - 1) * c[m] * 2 ** ((n - m) * (n - m - 1) // 2)
        c[n] = total - acc
    return c


def weakly_connected_digraphs(limit: int) -> list[int]:
    """w[n]: weakly-connected labeled simple digraphs (no loops).

    Total digraphs on n vertices: 2^{n(n-1)}.
    Same component recurrence with E(n) = n(n-1).
    """
    w = [0] * (limit + 1)
    for n in range(1, limit + 1):
        total = 2 ** (n * (n - 1))
        acc = 0
        for m in range(1, n):
            acc += comb(n - 1, m - 1) * w[m] * 2 ** ((n - m) * (n - m - 1))
        w[n] = total - acc
    return w


def strongly_connected_tournaments(limit: int) -> list[int]:
    """s[n]: strongly-connected (strong) labeled tournaments.

    s_n = T_n - sum_{k=1}^{n-1} C(n,k) s_k T_{n-k}, T_n = 2^{C(n,2)}.
    Ordering of strong components is total, hence C(n,k).
    """
    t = [0] * (limit + 1)
    for n in range(1, limit + 1):
        t[n] = 2 ** (n * (n - 1) // 2)
    s = [0] * (limit + 1)
    for n in range(1, limit + 1):
        acc = 0
        for k in range(1, n):
            acc += comb(n, k) * s[k] * t[n - k]
        s[n] = t[n] - acc
    return s


def connected_hypergraphs(k: int, limit: int) -> list[int]:
    """c[n]: connected labeled k-uniform hypergraphs.

    Uses component-of-vertex-1 recurrence with E(n) = C(n,k).
    Convention c_1 = 1; recurrence forces c_m = 0 for 2 <= m < k.
    """
    c = [0] * (limit + 1)
    if limit >= 1:
        c[1] = 1
    for n in range(2, limit + 1):
        acc = 0
        for m in range(1, n):
            acc += comb(n - 1, m - 1) * c[m] * 2 ** comb(n - m, k)
        c[n] = 2 ** comb(n, k) - acc
    return c


def predicted_graph_v2(n: int) -> int:
    """Conjectured/proven: v_2(c_n) = v_2((n-1)!) + (1 if 3|n else 0)."""
    return v2_factorial(n - 1) + (1 if n % 3 == 0 else 0)


def predicted_weak_digraph_v2(n: int) -> int:
    """Conjectured/proven: v_2(w_n) = v_2((n-1)!)."""
    return v2_factorial(n - 1)
