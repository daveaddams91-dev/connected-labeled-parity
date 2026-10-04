# Two-Primary Divisibility in Connected Labeled Structures

One sentence: exact powers of $2$ dividing the numbers of connected labeled graphs and weakly connected digraphs.

## TL;DR
- $c_n$ = connected labeled graphs (A001187): $v_2(c_n) = v_2((n-1)!) + [3 \mid n]$.
- $w_n$ = weakly connected labeled digraphs (A003027): $v_2(w_n) = v_2((n-1)!)$.
- Elementary 2-adic induction; verified to $n=250$ / $n=100$; brute-force cross-checked; boundary cases (hypergraphs, tournaments) documented as failing.

## Research question
Given the labeled exponential family of graphs (resp. digraphs), what structural 2-divisibility is forced on the connected counts? I.e., what is $v_2(c_n)$?

## Main result
**Theorem 1 (graphs).** $v_2(c_n) = v_2((n-1)!) + 1$ if $3\mid n$, else $v_2((n-1)!)$.
**Theorem 2 (weak digraphs).** $v_2(w_n) = v_2((n-1)!)$ for all $n$.
Equivalently $c_n/(n-1)!$ is a 2-adic integer congruent to $1\bmod 4$ ($3\nmid n$) or $2\bmod 4$ ($3\mid n$); $w_n/(n-1)!$ is always odd in $\mathbb{Z}_{(2)}$.

## Why this is interesting
- Exact closed form for a classical sequence (A001187) with a surprising period-3 correction.
- Same method yields an even cleaner second theorem, plus sharp negative results.
- Proof fits on ~2 pages using only $\mathbb{Z}_{(2)}$ and Legendre's formula.

## Repository structure
```
src/connected_parity/  exact recurrences, v2 helpers, brute-force module
tests/                 pytest suite (recurrences, formulas, brute force, boundary)
experiments/           verify_main.py, falsify.py, make_figures.py, run_all.py
results/               CSV tables (regenerated)
figures/               PNG figures (regenerated)
paper/                 main.tex + main.pdf (full paper with proofs)
docs/                  methodology.md, literature.md
examples/              quickstart.py
```

## Reproducing results
```bash
pip install -r requirements.txt
pytest tests/ -q
python experiments/run_all.py
```
This regenerates `results/*.csv` and `figures/*.png` and re-checks both formulas (graphs to 250, digraphs to 100) plus brute-force falsification. Paper: `paper/main.pdf` (source `paper/main.tex`, builds with `tectonic paper/main.tex`).

## Examples
```python
from connected_parity import connected_graphs, v2, predicted_graph_v2
c = connected_graphs(12)
print([(n, v2(c[n]), predicted_graph_v2(n)) for n in range(1, 11)])
```

## Limitations
- 2-primary only; odd primes and higher 2-adic digits (odd parts mod $2^k$) are open.
- Method needs $g_k \in \mathbb{Z}_{(2)}$ with few units; fails for $r$-uniform hypergraphs ($r\ge 3$) and strong tournaments — documented, not fixed.
- Novelty claim is qualified: no prior occurrence found after reasonable search (incl. Mani–Stones 2016, OEIS, textbooks), but not proven absent.

## Related work
Harary–Palmer (enumeration), Stanley EC2 (exponential formula), Mani–Stones 2016 (periodicity mod prime powers), OEIS A001187/A003027, Hardy–Wright (Legendre), Moon (tournaments). See `docs/literature.md` and paper references.

## Citation
```bibtex
@misc{connected-parity-2026,
  title  = {The 2-Adic Valuation of Connected Labeled Graphs and Weakly Connected Digraphs},
  year   = {2026},
  note   = {GitHub repository, v1.0.0}
}
```

## License
MIT — see `LICENSE`.
