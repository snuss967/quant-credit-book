## Chapter 25: NLP for Credit Agreements, Indentures & PACER Dockets

Six exercises: one on a recursive cap, one on a regex, one on a min cut, one on a cosine, one on a vote, and one on a pager. Every number below was recomputed from the chapter's inputs and from Listings 25.1 to 25.9 (Appendix F), run in order in one interpreter. Write your own answer before you read ours; on this chapter the trap is usually the answer that arrives first.

**Z.25.1: The four most expensive words, again**

**Answer:** Measured "after giving effect," a 30% cap lets add-backs reach $c/(1-c) = 0.3/0.7 = 42.9\%$ of pre-add-back EBITDA $\mathcal{E}_0$, against 30% on the "before" reading. The gap is 12.9 points of $\mathcal{E}_0$, which is exactly $c^2/(1-c) = 0.09/0.7$. The "after" reading doubles the "before" reading at $c = 1/2$ (50% becomes 100%). At Halyard's $\mathcal{E}_0 = \$200$mm, the cap goes from \$60mm to \$85.7mm, so the sponsor's whole \$80mm claim now fits under it, and incremental debt capacity goes from \$361mm to \$458mm.

**How:** The add-back counts toward the base that caps it, so the constraint is $A \le c(\mathcal{E}_0 + A)$. Collect $A$ on the left:

$$
A(1-c) \le c\,\mathcal{E}_0 \quad\Longrightarrow\quad A \le \frac{c}{1-c}\,\mathcal{E}_0 .
$$

Subtract the "before" cap $c\,\mathcal{E}_0$ and put it over one denominator: $\frac{c}{1-c} - c = \frac{c - c(1-c)}{1-c} = \frac{c^2}{1-c}$. For doubling, set $\frac{c}{1-c} = 2c$; divide by $c > 0$ to get $1 - c = \tfrac12$. Notice that the ratio of the two readings is $1/(1-c)$, so it climbs steeply: 1.33 at 25%, 1.43 at 30%, 2 at 50%. The iteration $A_{k+1} = \min\big(80,\ 0.3(200 + A_k)\big)$ in `addback_fixed_point` (Listing 25.2) agrees: it stops at the \$80mm claim, because the fixed point (85.7) is above it.

**The trap:** Running one round of the loop and stopping: $0.3 \times (1 + 0.3) = 39\%$. That is the cap after the add-back has been fed back once, not after it has settled; the remaining 3.9 points come from feeding the extra back again, and again. The geometric series $c + c^2 + c^3 + \dots = c/(1-c)$ is the same answer written as an iteration. On the doubling question, the slip is to solve $c/(1-c) = 2$ and report $c = 2/3$. That doubles $\mathcal{E}_0$, not the "before" reading.

**If you got this wrong, read:** §25.3.3 (Equation 25.1 and the "Fixed points and contractions" box), then the Full Derivation "the cycle as a contraction"; §25.3.4 for what each added dollar of EBITDA buys in capacity.

