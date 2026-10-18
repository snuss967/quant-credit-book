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

**Z.27.2: Add LQD and CDX IG to the table**

**Answer:** By the method of §27.6.1, with LQD as the bond's only credit hedge, $\beta_{i,\text{LQD}} = P_i D^{\text{spr}}_i \kappa^{\text{IG}}_i/(H_{\text{LQD}} D_{\text{LQD}}) \approx 1.30$ bond points per LQD dollar; CDX IG on the same footing gives $-0.180$ points per bp. In one row with TY the three must share the work. Split the credit exposure evenly between LQD and CDX IG and take LQD's rate content out of the TY beta, and the row is $\boldsymbol\beta_i = (0.158,\ 0.648,\ -0.0898)$, in bond points per TY point, per LQD dollar and per CDX IG basis point. With $\theta_i = 0.14$ points and the stress-window volatilities below, the budget splits as $\theta_{ij} = (0.014,\ 0.086,\ 0.040)$ points, so the thresholds are 0.089 TY points, \$0.133 of LQD and 0.44 bp of CDX IG. A flight to quality (TY up 6/32, LQD up \$0.09, CDX IG 1.25 bp wider) moves fair value by $-0.024$ points: the joint rule stays quiet, and the per-instrument rule pulls on TY and on CDX. In 200,000 fat-tailed simulated moves the joint rule pulls in 33% of windows and the per-instrument rule in 70%. False pulls are 37% of all windows (53% of the cheap rule's pulls), and the cheap rule misses no joint pull: zero in each of three seeds.

**How:** Inputs, all illustrative: the cold-open bond ($P_i = 95$, $D^{\text{spr}}_i = 8$, 130 bp, $\text{DV01}_i = 0.076$ points per bp, $\kappa^{\text{rate}} = 0.9$); LQD at \$108 with a duration of 8.3, so \$0.0896 per bp; the IG cash index at 85 bp; CDX IG at 55 bp. The DTS betas are $\kappa^{\text{IG}} = 130/85 = 1.53$ and $\kappa^{\text{CDX}} = 130/55 = 2.36$, so

$$
\beta_{i,\text{LQD}} = \frac{95 \times 8 \times 1.53}{108 \times 8.3} = 1.30, \qquad \beta_{i,\text{CDX}} = -\frac{95 \times 8 \times 2.36}{10^{4}} = -0.180 .
$$

Each formula assumes its instrument is the only credit hedge, and LQD's price also carries eight years of rate duration. In a shared row, give each credit hedge half the credit exposure, and read the IG spread change from LQD as $-\Delta H_{\text{LQD}}/0.0896 + \Delta H_{\text{TY}}/0.065$; the second term comes off the TY beta, $1.052 - \tfrac12 (1.53)(0.076/0.065) = 0.158$. Check the row on pure moves: a 1 bp rally gives $0.158(0.065) + 0.648(0.0896) = 0.0684 = 0.9 \times 0.076$, and a 1 bp IG widening gives $-0.116 = -0.076 \times 1.53$. Then allocate as in §27.6.1: $\theta_{ij} = c\,|\beta_{ij}|\,\sigma_j$ with $c = \theta_i/\sum_j |\beta_{ij}|\sigma_j = 0.886$, and $\tau_{ij} = \theta_{ij}/|\beta_{ij}| = c\,\sigma_j$. Our covariance for one stress window: volatilities of 0.10 TY points, \$0.15 of LQD and 0.5 bp of CDX IG; correlations TY–LQD $+0.75$, TY–CDX $+0.35$ (TY rallies when CDX widens) and LQD–CDX $-0.25$. Fat tails come from Listing 27.4's chi-squared(4) scale mixture, with moves rounded to grids of 1/64, \$0.01 and 0.05 bp. This extends Listing 27.4 from two hedges to three. The zero-miss count is the triangle inequality at work, not luck: it holds draw by draw, whatever the covariance.

**The trap:** Pasting the three one-hedge betas into one row (1.05, 1.30, $-0.180$). That counts rates twice (TY and LQD) and credit twice (LQD and CDX): a 1 bp rally reads as 0.185 points instead of 0.068, and a 1 bp IG widening as $-0.232$ instead of $-0.116$. The cheap rule built on that row pulls in 95% of stress windows, and its joint rule still misses about one true pull in a thousand windows, because it weighs offsetting moves wrongly. The safety theorem protects you relative to the $\boldsymbol\beta$ you wrote down, not relative to the bond.

**If you got this wrong, read:** §27.6.1 (the trigger table, the "two detours" box, the theorem and the paragraph on allocating the budget); Listing 27.4 in Appendix F, which this exercise extends; Chapter 8 for the empirical rate beta and the DV01 ratios.

**Z.27.3: The J.Crew drop-down as rows**

**Answer:** The rows are below. A backtest of Chapter 25's covenant-flag signal must use the knowledge-time snapshot at its decision time, $Q(k, a;\ t^{v} \le t,\ t^{k} = t)$, and must read the parser's output the same way. If the vendor's "point-in-time" file is valid-time only, it answers $Q(\cdot;\ t^{v} = t,\ t^{k} = \text{now})$. The IP then leaves the collateral on the transfer's effective date rather than when anyone outside the company knew, the signal fires before the 5 December 2016 disclosure, and the backtest trades the term loan at prices from before the market had read the filing. Every later correction leaks backwards too: a 2019 re-parse, or a `jcrew_blocker` field back-filled onto agreements signed before the move that named it, reads as if it had been known all along.

Notation: $t_0$ is the date the desk onboarded the loan, $t_x$ the transfer's effective date as the filing states it (on or before 2016-12-05), and $k_1$ = 2016-12-05 18:00, when the desk's event feed confirmed it *($t_0$ and the 18:00 are illustrative; keys are internal surrogates)*. ASSET-JC-USIP is the interest in the US marks that the 2017 notes were later secured on (72.04%, per Chapter 13).

| Key | Attribute | Value | Valid from | Valid to | Known from | Known to |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| ASSET-JC-USIP | owner | ENT-JC-LOANPARTY | $t_0$ | ∞ | $t_0$ | $k_1$ |
| ASSET-JC-USIP | owner | ENT-JC-LOANPARTY | $t_0$ | $t_x$ | $k_1$ | ∞ |
| ASSET-JC-USIP | owner | ENT-JC-DOMBRAND | $t_x$ | ∞ | $k_1$ | ∞ |
| INS-JC-TL | collateral | all assets incl. ASSET-JC-USIP | $t_0$ | ∞ | $t_0$ | $k_1$ |
| INS-JC-TL | collateral | all assets incl. ASSET-JC-USIP | $t_0$ | $t_x$ | $k_1$ | ∞ |
| INS-JC-TL | collateral | all assets excl. ASSET-JC-USIP | $t_x$ | ∞ | $k_1$ | ∞ |
| ENT-JC-DOMBRAND | parent | ENT-JC-NGRS (non-guarantor restricted sub) | $t_x$ | ∞ | $k_1$ | ∞ |
| ENT-JC-DOMBRAND | obligor_role | unrestricted; not a guarantor or grantor of INS-JC-TL | $t_x$ | ∞ | $k_1$ | ∞ |
| EVT-JC-2016-12 | event | drop_down: ASSET-JC-USIP to ENT-JC-DOMBRAND; INS-JC-TL collateral reduced; source: company filing, 2016-12-05 | $t_x$ | n/a | $k_1$ | ∞ |

**How:** Follow the Serta pattern of §27.3.3. Rows the desk believed before $k_1$ are closed in knowledge time at $k_1$, never edited, which is invariant (I2); the corrected history and the new facts all open at $k_1$, whatever their valid dates. The guarantor map is the dated graph of §27.3.1: the new box ENT-JC-DOMBRAND gets a dated arrow to its parent and a role outside the obligor group, so the question "is the IP inside the term lenders' collateral?" has two dated answers. If the filing dates the two hops separately (loan party to the non-guarantor restricted subsidiary, then on to the unrestricted one), each hop gets its own owner row and its own event row. The July 2017 exchange is a second event: it creates the 13% notes of J.Crew Brand, LLC and J.Crew Brand Corp. with their own collateral row, and retires part of the PIK notes. For the backtest, a decision at noon on 5 December sees the IP still with the loan party, even though $t^{v} \ge t_x$; a decision on the morning of 6 December sees it gone. Chapter 25's signal is built from the parsed capacity vector and the obligor map, so it inherits both knowledge times: the master's, and that of the parse it read.

**The trap:** Stamping the new rows "known from $t_x$" because that is when the transfer happened. That one choice turns the archive into the wiki: the drop-down looks known before it was disclosed, and the signal looks prescient for the same reason Theo's Serta backtest did. The other slip is to edit the old owner row's valid-to in place, which erases what the desk believed on 4 December.

**If you got this wrong, read:** §27.3.2 (the two invariants, the theorem and the corollary on valid-time-only "point-in-time" files); §27.3.3 (Serta as rows, and Mags's three questions); §27.3.1 for the dated obligor graph; Chapter 13's J.Crew Docket Diary for the facts; §25.9 on when a text signal is executable.

