"""Generate paper figures (matplotlib, no seaborn)."""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from connected_parity.enumeration import (
    connected_graphs, weakly_connected_digraphs, connected_hypergraphs, v2, v2_factorial,
)

os.makedirs("figures", exist_ok=True)
N = 99
c = connected_graphs(N)
w = weakly_connected_digraphs(N)
vc = [v2(c[n]) for n in range(1, N + 1)]
vf = [v2_factorial(n - 1) for n in range(1, N + 1)]
diff = [vc[i] - vf[i] for i in range(N)]
vw = [v2(w[n]) for n in range(1, N + 1)]

plt.figure(figsize=(7, 4))
plt.plot(range(1, N + 1), vc, marker="o", ms=3, label=r"$v_2(c_n)$")
plt.plot(range(1, N + 1), vf, marker="s", ms=3, label=r"$v_2((n-1)!)$")
plt.xlabel("n")
plt.ylabel("2-adic valuation")
plt.title("Connected labeled graphs: $v_2(c_n)$ vs $v_2((n-1)!)$")
plt.legend()
plt.tight_layout()
plt.savefig("figures/graph_v2_vs_factorial.png", dpi=150)

plt.figure(figsize=(7, 3))
plt.stem(range(1, N + 1), diff)
plt.xlabel("n")
plt.ylabel(r"$v_2(c_n)-v_2((n-1)!)$")
plt.title("Excess valuation is 1 iff $3\\mid n$ (period 3)")
plt.tight_layout()
plt.savefig("figures/graph_excess_period3.png", dpi=150)

plt.figure(figsize=(7, 4))
plt.plot(range(1, N + 1), vw, marker="o", ms=3, label=r"$v_2(w_n)$")
plt.plot(range(1, N + 1), vf, marker="s", ms=3, label=r"$v_2((n-1)!)$")
plt.xlabel("n")
plt.ylabel("2-adic valuation")
plt.title("Weakly-connected digraphs: exact match $v_2(w_n)=v_2((n-1)!)$")
plt.legend()
plt.tight_layout()
plt.savefig("figures/weak_v2_match.png", dpi=150)

ch3 = connected_hypergraphs(3, 40)
vh3 = [v2(ch3[n]) if ch3[n] != 0 else -1 for n in range(1, 41)]
plt.figure(figsize=(7, 4))
plt.plot(range(1, 41), vh3, marker="o", ms=4, label=r"$v_2(c^{(3)}_n)$")
plt.plot(range(1, 41), [v2_factorial(n - 1) for n in range(1, 41)],
         marker="s", ms=4, label=r"$v_2((n-1)!)$")
plt.xlabel("n")
plt.ylabel("2-adic valuation")
plt.title("3-uniform hypergraphs: no clean formula (boundary case)")
plt.legend()
plt.tight_layout()
plt.savefig("figures/hypergraph_boundary.png", dpi=150)
print("wrote 4 figures")
