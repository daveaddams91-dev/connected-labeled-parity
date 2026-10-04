"""Quickstart: verify the main formulas on small n."""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from connected_parity import connected_graphs, weakly_connected_digraphs, v2

c = connected_graphs(12)
w = weakly_connected_digraphs(12)
print("n  v2(c_n)  v2(w_n)")
for n in range(1, 13):
    print(n, v2(c[n]), v2(w[n]))
print("Graph excess (should be 1 iff 3|n):",
      [v2(c[n]) - v2(__import__('math').factorial(n - 1)) for n in range(1, 13)])
