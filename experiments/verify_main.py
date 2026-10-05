"""Verify the two main 2-adic formulas and dump results tables."""
import csv
import os
import sys
import time

sys.set_int_max_str_digits(100000)

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from connected_parity.enumeration import (
    connected_graphs,
    weakly_connected_digraphs,
    connected_hypergraphs,
    v2,
    v2_factorial,
    predicted_graph_v2,
    predicted_weak_digraph_v2,
)

GRAPH_N = 250
DIGRAPH_N = 100
HYPER_N = 30


def main() -> None:
    """Entry point — parse arguments and run the main computation.
    
    """
    os.makedirs("results", exist_ok=True)
    t0 = time.time()
    c = connected_graphs(GRAPH_N)
    t1 = time.time()
    w = weakly_connected_digraphs(DIGRAPH_N)
    t2 = time.time()
    rows_g = []
    for n in range(1, GRAPH_N + 1):
        vc = v2(c[n])
        pred = predicted_graph_v2(n)
        rows_g.append([n, str(c[n]) if n <= 20 else f"{len(str(c[n]))} digits",
                       vc, v2_factorial(n - 1), 1 if n % 3 == 0 else 0, pred, vc == pred])
    with open("results/graph_v2.csv", "w", newline="") as f:
        csv.writer(f).writerow(["n", "c_n_or_digits", "v2_c", "v2_fact", "delta3", "pred", "match"])
        csv.writer(f).writerows(rows_g)
    rows_w = []
    for n in range(1, DIGRAPH_N + 1):
        vw = v2(w[n])
        pred = predicted_weak_digraph_v2(n)
        rows_w.append([n, vw, v2_factorial(n - 1), pred, vw == pred])
    with open("results/weak_digraph_v2.csv", "w", newline="") as f:
        csv.writer(f).writerow(["n", "v2_w", "v2_fact", "pred", "match"])
        csv.writer(f).writerows(rows_w)
    # Hypergraph boundary table (k=3,4): show formula fails
    for k in (3, 4):
        ch = connected_hypergraphs(k, HYPER_N)
        with open(f"results/hypergraph_k{k}_v2.csv", "w", newline="") as f:
            wr = csv.writer(f)
            wr.writerow(["n", "c_n", "v2_c", "v2_fact", "graph_pred", "match_graph_pred"])
            for n in range(1, HYPER_N + 1):
                wr.writerow([n, ch[n], v2(ch[n]), v2_factorial(n - 1),
                             predicted_graph_v2(n), v2(ch[n]) == predicted_graph_v2(n)])
    assert all(r[-1] for r in rows_g), "graph formula mismatch"
    assert all(r[-1] for r in rows_w), "digraph formula mismatch"
    print(f"graphs to {GRAPH_N}: enum {t1-t0:.2f}s; digraphs to {DIGRAPH_N}: {t2-t1:.2f}s; total {time.time()-t0:.2f}s")
    print(f"ALL {GRAPH_N} graph values and {DIGRAPH_N} digraph values match predictions.")


if __name__ == "__main__":
    main()
