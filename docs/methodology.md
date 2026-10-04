# Methodology

## Discovery loop
Hypothesis (parity grows) -> small-n enumeration (v2 table) -> pattern
$v_2(c_n)-v_2((n-1)!) \in \{0,1\}$ -> refinement (period 3 in $n$) ->
counterexample search (to $n=250$, brute force $n\le 5$, hypergraph/tournament
analogues) -> proof attempt ($b_n = c_n/(n-1)!$ in $\mathbb{Z}_{(2)}$) ->
verification -> boundary analysis -> final theorems.

## Proof technique
Work in $\mathbb{Z}_{(2)}$ (rationals with odd denominator).
Normalize $b_n = c_n/(n-1)!$, $g_k = 2^{E(k)}/k!$, $f(k)=v_2(g_k)$.
The component recurrence becomes $b_n = ng_n - \sum b_m g_{n-m}$.
If only $g_0,g_1,g_2$ are units (graphs) the sum collapses mod 4 to
$b_n \equiv -(b_{n-1}+b_{n-2})$; the $\mathbb{F}_2$ dynamics has period 3,
and the mod-4 lift fixes the exact valuation. For digraphs only $g_1$
is a unit and everything collapses mod 2 to $b_n \equiv b_{n-1}$.

## Falsification-first
- Independent brute-force enumerators (separate code path) for graphs $n\le 5$,
  digraphs $n\le 3$.
- Recurrence self-consistency: totals reconstructed from connected counts.
- Formula checked to $n=250$ (graphs) / $n=100$ (digraphs).
- Adversarial analogues: hypergraphs $k=3,4$ and strong tournaments checked
  against the same pattern and shown to fail systematically (0/22 matches),
  confirming sharpness rather than overfitting.

## Reproducibility
Deterministic (no randomness). Exact integer arithmetic only.
`python experiments/run_all.py` regenerates all CSVs and PNGs from scratch.
