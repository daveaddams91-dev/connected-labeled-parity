# Literature and novelty audit

## Sources consulted
- F. Harary, E. M. Palmer, *Graphical Enumeration* (1973): classical
  recurrence for connected labeled graphs.
- R. P. Stanley, *Enumerative Combinatorics* Vol. 2 (1999): exponential
  formula, EGF $\exp$ / $\log$ correspondence between all and connected
  labeled structures.
- A. P. Mani, R. J. Stones, "The number of labeled connected graphs modulo
  prime powers", *SIAM J. Discrete Math.* 30 (2016), 1046–1057: proves
  ultimate periodicity mod $p^k$ via group actions. Implies growing
  2-divisibility but no exact valuation. Closest prior work; our results
  are consistent with theirs and strictly more precise at $p=2$, $b=2$.
- OEIS A001187 (connected labeled graphs) and A003027 (weakly connected
  digraphs): initial terms match our recurrences; no 2-adic formula listed.
- G. H. Hardy, E. M. Wright, *An Introduction to the Theory of Numbers*:
  Legendre's formula for $v_p(n!)$.
- J. W. Moon, *Topics on Tournaments* (1968): strong-tournament recurrence
  used only as a boundary contrast.
- Web searches for "2-adic valuation connected labeled graphs",
  "parity of connected labeled graphs", "v_2(c_n)" found no exact formula.

## Novelty matrix
| Existing result | Proves | Relation | Difference |
|---|---|---|---|
| Mani–Stones 2016 | $(c_n)$ periodic mod $p^k$ | same sequence, coarser modulus | no exact $v_2$; our Thm 1 implies a refinement at 2 |
| Stanley EC2 exp. formula | $G = \exp(C)$ over $\mathbb{Q}$ | same recurrence source | enumerative, not 2-adic |
| OEIS data | first values | consistent | no formula |
| Legendre | $v_2((n-1)!)$ | used as yardstick | classical, credited |

## Claim status
- Theorems 1–2: proved here; no prior occurrence found → "apparently new"
  (qualified; not claimed as "first" without reservation).
- Recurrences, Legendre, EGF background: known, credited.
- Hypergraph/tournament non-patterns: empirical + explained ($f(2)<0$ /
  ordered decomposition); presented as boundary observations, not theorems.
