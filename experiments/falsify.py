"""Falsification attempts: brute force, recurrence consistency, adversarial residues."""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from connected_parity.enumeration import (
    connected_graphs,
    weakly_connected_digraphs,
    strongly_connected_tournaments,
    connected_hypergraphs,
    v2,
    v2_factorial,
)
from connected_parity.brute import brute_connected_graphs, brute_weak_digraphs


def main() -> None:
    """Entry point — parse arguments and run the main computation.
    
    """
    failures = []
    # 1. Brute-force cross-check (independent implementation).
    c = connected_graphs(6)
    for n in range(1, 6):
        b = brute_connected_graphs(n)
        status = "OK" if b == c[n] else "MISMATCH"
        print(f"graphs n={n}: recurrence={c[n]} brute={b} {status}")
        if b != c[n]:
            failures.append(f"graphs n={n}")
    w = weakly_connected_digraphs(4)
    for n in range(1, 4):
        b = brute_weak_digraphs(n)
        status = "OK" if b == w[n] else "MISMATCH"
        print(f"weak digraphs n={n}: recurrence={w[n]} brute={b} {status}")
        if b != w[n]:
            failures.append(f"weak n={n}")
    # 2. Try to break the graph formula by direct search to n=250 (already in verify).
    cbig = connected_graphs(120)
    bad = [n for n in range(1, 121)
           if v2(cbig[n]) != v2_factorial(n - 1) + (1 if n % 3 == 0 else 0)]
    print(f"graph formula counterexamples to n=120: {bad if bad else 'none'}")
    if bad:
        failures.append("graph formula")
    wbig = weakly_connected_digraphs(60)
    badw = [n for n in range(1, 61) if v2(wbig[n]) != v2_factorial(n - 1)]
    print(f"weak formula counterexamples to n=60: {badw if badw else 'none'}")
    if badw:
        failures.append("weak formula")
    # 3. Adversarial: does the same pattern hold for strong tournaments or hypergraphs?
    s = strongly_connected_tournaments(16)
    bads = [n for n in range(3, 17) if v2(s[n]) == v2_factorial(n - 1)]
    print(f"strong tournaments matching graph pattern (should be FEW): {len(bads)} of 14")
    for k in (3, 4):
        ch = connected_hypergraphs(k, 25)
        badh = [n for n in range(4, 26)
                if v2(ch[n]) == v2_factorial(n - 1) + (1 if n % 3 == 0 else 0)]
        print(f"k={k} hypergraphs matching graph pattern on 4..25: {len(badh)}/22 "
              f"(most should NOT match)")
    # 4. Odd-part check: b_n = c_n/(n-1)! must be a 2-adic integer (v>=0) to n=120.
    neg = [n for n in range(1, 121) if v2(cbig[n]) < v2_factorial(n - 1)]
    print(f"n with v2(c_n) < v2((n-1)!): {neg if neg else 'none (integrality holds)'}")
    if neg:
        failures.append("integrality")
    if failures:
        print("FAILURES:", failures)
        raise SystemExit(1)
    print("All falsification attempts passed (no counterexample to main claims).")


if __name__ == "__main__":
    main()
