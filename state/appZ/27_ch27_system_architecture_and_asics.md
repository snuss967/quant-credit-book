## Chapter 27: System Construction, Low-Latency Infrastructure & ASICs/FPGAs

Seven exercises: a queue, a trigger row, a drop-down written as rows, a stopping rule, a spec, a memo and a pair with one leg missing. Every number below was recomputed from the chapter's inputs, and from Listings 27.3 to 27.5 (Appendix F) where an exercise extends them, with simulations run fresh. Where an exercise asks you to choose an input, ours is stated and marked illustrative. Write your own answer before you read ours. In this chapter the trap is usually the number the system would have reported: the mean, the per-leg view, the field that reads "OK."

**Z.27.1: Kaz's engine on a CPI morning**

**Answer:** The approximate p99 *wait* reaches 500 ms at $\rho \approx 0.31$. To stay inside a 500 ms budget the engine must run at or below that, so the desk has to shed or batch $1 - 0.31/0.5 \approx 38\%$ of quote refreshes at $\rho = 0.5$, and $1 - 0.31/0.9 \approx 65\%$ at $\rho = 0.9$. A Lindley simulation puts the ceiling a little lower, near $\rho = 0.27$ (46% and 70%), because the exponential tail is slightly optimistic at light load when $c_s^2 = 4$. With $c_s^2 = 1$ at $\rho = 0.7$, the mean wait falls from 233 ms to 93 ms, the p99 wait from 1.42 s to 0.57 s, and the p99 sojourn from about 1.5 s to about 0.61 s. The ceiling rises to $\rho \approx 0.66$: nothing needs shedding at 0.5, and 26% at 0.9. The sentence for the risk meeting: *every refresh waits behind whatever the engine is already working on, so the queue is set by the rare slow jobs, not the typical one; halving the lattice jobs cuts the p99 wait from 1.4 s to 0.33 s, while halving the trivial refreshes, which makes the average 25% faster, only gets it to 1.06 s.*

**How:** With $\mathbb{E}[S] = 40$ ms and $(1 + c_s^2)/2 = 2.5$, Pollaczek–Khinchine gives $\mathbb{E}[W_q] = 100\rho/(1-\rho)$ ms, and the tail quantile of §27.5.1 becomes

$$
t_{0.99} \approx \frac{\mathbb{E}[W_q]}{\rho}\,\ln\frac{\rho}{0.01} = \frac{100}{1-\rho}\,\ln(100\rho)\ \text{ms}.
$$

Set it equal to 500 and solve $\ln(100\rho) = 5(1-\rho)$ numerically: $\rho^\star = 0.312$. Check the ends against the chapter: 782 ms at $\rho = 0.5$ and 4.5 s at 0.9. Shedding a refresh, or coalescing several refreshes of one quote into one, removes an arrival, and utilisation is proportional to the arrival rate, so the share to remove is $1 - \rho^\star/\rho$. With $c_s^2 = 1$ the same steps give $t_{0.99} = \frac{40}{1-\rho}\ln(100\rho)$, which is exact for M/M/1. For the sentence, write the mean wait as $\mathbb{E}[W_q] = \Lambda^{\text{q}}\,\mathbb{E}[S^2]/\big(2(1-\rho)\big)$ and model Kaz's 40 ms as 95% trivial refreshes of 21.6 ms and 5% lattices of 389 ms (an illustrative mixture with $c_s^2 = 4$). The lattices supply 94% of $\mathbb{E}[S^2]$. Halving either kind brings the mean to about 30 ms, but halving the lattices cuts $\mathbb{E}[S^2]$ by 71% and halving the trivial refreshes cuts it by 4%.

**The trap:** Two of them. The first is to read the mean: at $\rho = 0.5$ the mean wait is 100 ms, comfortably inside 500, so "no shedding needed." The p99 is 782 ms. The second is to subtract utilisations: going from 0.9 to 0.31 is 59 points of utilisation, but the share of refreshes you have to remove is $0.59/0.9 = 65\%$.

NOTE (for the editor): The exercise says "rerun block 3 with $c_s^2 = 1$." Block 3 (Listing 27.3) hard-codes the $c_s^2 = 4$ answers, so with `CS2 = 1.0` it stops at its first assert, `abs(ew - 233.33) < 0.01`, because the mean wait is now 93.3 ms; the p99-sojourn assert (1,000 to 2,400 ms) would fail as well, at about 610 ms. Suggest adding "and update the asserts," or readers will think they broke the listing.

**If you got this wrong, read:** §27.5.1 (both parts of the queues box, then the Full Derivation and the tail quantile); the usage note under Listing 27.3 on feeding the stress hour's load rather than the day's; §27.1.1's grading of the cold-open card.

