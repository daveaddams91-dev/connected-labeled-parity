"""Exhaustive brute-force checks for small n (falsification)."""
from __future__ import annotations



def _is_connected(n: int, edges: set) -> bool:
    """Is connected.
    
    Args:
        n:
        edges:
    
    Returns:
        bool: Result of type bool
    
    """
    if n <= 1:
        return True
    adj: list[set[int]] = [set() for _ in range(n)]
    for u, v in edges:
        adj[u].add(v)
        adj[v].add(u)
    seen = {0}
    stack = [0]
    while stack:
        u = stack.pop()
        for w in adj[u]:
            if w not in seen:
                seen.add(w)
                stack.append(w)
    return len(seen) == n


def brute_connected_graphs(n: int) -> int:
    """Count connected labeled graphs by enumerating all 2^{C(n,2)}."""
    pairs = [(i, j) for i in range(n) for j in range(i + 1, n)]
    total = 0
    for mask in range(2 ** len(pairs)):
        edges = {pairs[i] for i in range(len(pairs)) if mask & (1 << i)}
        if _is_connected(n, edges):
            total += 1
    return total


def _is_weakly_connected(n: int, arcs: set) -> bool:
    """Is weakly connected.
    
    Args:
        n:
        arcs:
    
    Returns:
        bool: Result of type bool
    
    """
    if n <= 1:
        return True
    adj: list[set[int]] = [set() for _ in range(n)]
    for u, v in arcs:
        adj[u].add(v)
        adj[v].add(u)
    seen = {0}
    stack = [0]
    while stack:
        u = stack.pop()
        for w in adj[u]:
            if w not in seen:
                seen.add(w)
                stack.append(w)
    return len(seen) == n


def brute_weak_digraphs(n: int) -> int:
    """Count weakly-connected digraphs by enumerating all 2^{n(n-1)}."""
    arcs = [(i, j) for i in range(n) for j in range(n) if i != j]
    total = 0
    for mask in range(2 ** len(arcs)):
        s = {arcs[i] for i in range(len(arcs)) if mask & (1 << i)}
        if _is_weakly_connected(n, s):
            total += 1
    return total
