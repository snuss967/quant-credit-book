## Chapter 22: Market-Structure Regulation & the Forces Reshaping Liquidity

Six exercises: two on rent and clocks, two on the tape and the netting set, and two on dates, which is where this chapter's money is. Write your card before you read ours.

**Z.22.1: The ante**

**Answer:** $\tau^\ast = 0.25/60$ years $= 0.00417$ years $\approx 1.52$ calendar days at $\kappa_{\text{LR}} = 5\%$, and $0.25/45$ years $= 0.00556$ years $\approx 2.03$ days at $3.75\%$. At a two-day hold the dealer paid 0.33bp of rent against a 0.25bp half-spread under the old floor, losing about 0.08bp per round trip. That is an agent with extra steps, and an unpaid warehouse. Under the new floor the rent is 0.247bp against 0.25bp, so it breaks even: a principal that earns nothing on the hold. In both regimes, principal market making pays only if the dealer turns its Treasuries in under about two calendar days.

**How:** The bid-ask is 0.5bp of price, so the numerator of (22.4) is the *half* spread, 0.25bp. Rent per year is

$$
c_{\text{reg}} = h\,\kappa_{\text{LR}} = 0.12 \times 0.05 = 0.006 = 60\text{bp/yr}, \qquad 0.12 \times 0.0375 = 45\text{bp/yr}.
$$

Divide: $\tau^\ast = 0.25/60$ and $0.25/45$ years, then multiply by 365 (the chapter's ACT/365 convention). For the two-day check, compare the half-spread with $60 \times 2/365 = 0.329$bp and $45 \times 2/365 = 0.247$bp. The risk weight never enters, because a 5-year on-the-run Treasury sits far below the switching point (22.14), so the leverage floor is the whole rent.

**The trap:** The usual slip is to put the full 0.5bp on top of (22.4) and get 3.0 and 4.1 days. Those match the §22.1 table, but that table priced a 2-year that was 1bp wide, with a half-spread of 0.5bp. With them, a two-day hold looks comfortably principal, and the conclusion flips. The runner-up is a calendar slip: $\tau^\ast$ is in calendar days, so "two days" held over a weekend is four, and that dealer is underwater under either floor.

**If you got this wrong, read:** §22.1.1 (eq. 22.4 and the numerics table), then the ante in §22.5.1.

**Z.22.2: Pooling at the cap**

**Answer:** The cap is neutral at $Q = mC = 2.5 \times \$5\text{mm} = \$12.5$mm for IG (the HY twin is $4 \times \$1\text{mm} = \$4$mm). It moves the competitive half-spread by exactly $\lambda(mC - Q)(1 - \Delta/T_u)^+$, which is positive, a widening, for every $C < Q < mC$. With the worked-example parameters ($\lambda = 0.5$, $\Delta = 15$, $T_u = 120$, $\sigma = 2.5$, $\gamma = 0.001$):

| $Q$ (\$mm) | uncapped (bp) | capped (bp) | cap's effect |
| :-- | :-- | :-- | :-- |
| 6 | 3.38 | 6.22 | +2.84 |
| 10 | 5.63 | 6.72 | +1.09 |
| 12.5 | 7.03 | 7.03 | 0 |
| 15 | 8.44 | 7.34 | −1.09 |
| 25 | 14.06 | 8.59 | −5.47 |

The worst place to be is just above the cap: a ticket one dollar over \$5mm pays 3.28bp more than one at \$5mm.

**How:** Above the cap the market prices the conditional mean, so the inferred size in the leak term of (22.6) becomes $mC$ while the inventory term keeps the true $Q$:

$$
\frac{s_B^{\text{cap}}}{2} - \frac{s_B^\ast}{2} = \lambda\,(mC - Q)\Big(1 - \frac{\Delta}{T_u}\Big)^+ .
$$

The inventory term $\gamma\sigma^2 Q T_u/6$ cancels, so the neutral point is $Q = mC$ whatever $\lambda$, $\gamma$ or $\sigma$ are, as long as $\Delta < T_u$. (If the unwind finishes before the print, the cap is irrelevant at every size.) With $m = \alpha/(\alpha-1) = 2.5$ from Ben Dor's imputed \$12.5mm, the sign is the sign of $mC - Q$. Here is how Ines would put the politics. A desk whose blocks are \$5–12.5mm is taxed by the pool, so it wants a higher cap or finer size buckets: the 2019 pilot's \$10mm cap would have let its \$6–10mm tickets print at their true size. A desk whose blocks are above \$12.5mm is subsidized, so it defends the \$5mm cap. It accepts a higher one only with compensation, which is what the 2019 pilot's 48-hour delay was. With $\alpha$ fixed, a \$10mm cap puts $mC$ at \$25mm, which turns a \$15mm block from a 1.09bp subsidy into a 4.38bp tax. Same tape, opposite comment letters.

**The trap:** The common wrong answer is "the cap always helps the dealer, because hiding size is good", or a neutral point at $Q = C$. The cap does not hide size. It replaces it with the pool's average, and the average is \$12.5mm, which is bigger than most capped trades. A \$6mm ticket is being priced as if it were twice its size.

**If you got this wrong, read:** §22.2.2 (eq. 22.7 and the pooling paragraph), with (22.6) from §22.2.1; Beat 3 of §22.2.3 for the 2019 pilot.

**Z.22.3: Negative specials**

**Answer:** The floor on the special repo rate is $r^{\text{sp}} = \min(0,\ r^{\text{ref}} - 3\%)$. That is $-2.75\%$ at $r^{\text{ref}} = 0.25\%$ and $0\%$ at $r^{\text{ref}} = 4\%$. At near-zero rates the fails charge lets specials go about 2.75 points negative. At 4% the charge is asleep, and the old zero bound is back.

**How:** Measure both choices against delivering on time and investing the proceeds at $r^{\text{ref}}$. Failing costs (22.9), $\max(r^{\text{ref}}, 3\%)$: you lose the interest and pay the charge. Borrowing the bond means lending your sale proceeds in repo at $r^{\text{sp}}$ to get it, so you give up $r^{\text{ref}} - r^{\text{sp}}$. Set the two equal:

$$
r^{\text{ref}} - r^{\text{sp}} = \max(r^{\text{ref}}, 3\%) \;\Longrightarrow\; r^{\text{sp}} = r^{\text{ref}} - \max(r^{\text{ref}}, 3\%) = \min(0,\ r^{\text{ref}} - 3\%).
$$

Below that rate the short fails instead, so no bond lender can push repo lower. Now Veronesi's May 2009. With the policy rate near zero and failing free (cost $\approx r^{\text{ref}} \approx 0$), the floor sat at zero. Specials piled up there, and fails were the cheap alternative. The 3% penalty from 1 May 2009 dropped the floor to about $-2.75\%$ ($-3\%$ if you take the reference as exactly zero). That made room for the negative special repo rates Veronesi records that same day. The floor is a bound, not a forecast: the 2009 specials did not have to go anywhere near $-2.75\%$.

**The trap:** One slip is to drop the $\min$ and report $+1\%$ at a 4% reference rate, as if a special could not trade below 1%. Above 3% the charge is zero, failing costs only the lost interest, and specials can go all the way to zero. The other is $-3\%$ at 0.25%, which forgets that the failing seller also loses the 0.25% of interest.

**If you got this wrong, read:** §22.3.2 (eq. 22.9 and the Veronesi annotation).

**Z.22.4: When does netting give up?**

**Answer:** The floor is $\phi_\infty = 0.5/0.8956 = 0.558$. By simulation (20,000 paths) and by closed form, $\phi(5) \approx 0.651$, $\phi(10) \approx 0.580$, $\phi(25) \approx 0.559$ and $\phi(100) \approx 0.558$. It is within 5% of the floor (at or below 0.586) from $N = 10$. $N = 9$ misses by a hair, at 5.03% above, which 20,000 paths cannot reliably tell apart from $N = 10$. Past about ten members, more clearing members buy nothing in a one-way market. Clearing removes at most 44% of gross exposure, where the two-way formula promises 67% at $N = 10$ and 90% at $N = 100$.

**How:** Draw $x_{ij} = 0.5 + Z_{ij}$ ($\sigma_x = 1$) in $N - 1$ columns, and divide the mean absolute row sum by the mean row sum of absolute values. This is [Listing 22.4](#code-22-4)'s `netting_factor_mc` with `common_component=0.5`. Check it against the exact factor. With $n = N - 1$ and $f(a) = \mathbb{E}|a + Z| = \sqrt{2/\pi}\,e^{-a^2/2} + a\,\operatorname{erf}(a/\sqrt2)$,

$$
\phi(N) = \frac{f(\sqrt{n}\,m)}{\sqrt{n}\,f(m)}, \qquad f(0.5) = 0.8956 .
$$

Convergence is fast because the only thing separating $\phi(N)$ from the floor is the chance that the netted position flips sign, $\Phi(-\sqrt{n}\,m/\sigma_x)$. That chance is 6.7% at $N = 10$ and 0.7% at $N = 25$. Once the sum has a sign, there is nothing left to cancel.

**The trap:** The usual wrong answer is the two-way formula $1/\sqrt{N-1}$: 0.50, 0.33, 0.20 and 0.10. It says a 100-member clearing house removes 90% of exposure, when a market leaning half a standard deviation one way keeps 56%. Two smaller slips: reading "within 5%" as 0.05 absolute, which gives $N = 7$, and using $N$ columns instead of $N - 1$ counterparties, which matters only at small $N$.

**If you got this wrong, read:** §22.4.1, especially (22.11) and "The Full Derivation: the netting factor with a common direction."

**Z.22.5: Kaz's event date**

**Answer:** 2025-12-31 is the stale date. The December 2023 adopting release set it, and on 2025-02-25 the SEC moved cash compliance to 2026-12-31 and repo to 2027-06-30. Nothing became mandatory on 2025-12-31, so Kaz would be measuring a year-end and crediting it to a rule. Turned around, that same date is the best placebo the study has. The design:

- **Event** $t_0$ = 2026-12-31, a Thursday that is also year-end, a G-SIB measurement snapshot, and the eve of a market holiday.
- **Treated** are Treasury flows the mandate newly pulls into clearing: cash trades on interdealer-broker platforms, and trades between clearing members and non-member broker-dealers or government securities dealers that used to settle bilaterally. For the credit desk, that means its own Treasury hedges with in-scope counterparties.
- **Controls** are flows that do not change on the date: trades already cleared member-to-member at FICC, and exempt ones (central banks, sovereigns, international financial institutions, natural persons, inter-affiliate).
- **Placebos** are 2025-12-31 (the same calendar position and the same photograph, with no rule) and 2024-12-31, plus one or two mid-quarter fake dates whose post-windows end well before Q4 2026.
- **Distrust trigger:** a significant "effect" at 2025-12-31 of the same sign and similar size as the one at 2026-12-31. That would mean the estimate is the year-end, not the mandate.

**How:** First take the date from the latest release, not the first one. Keep adoption (2023-12-13), the extension (2025-02-25), margin separation (2025-09-30), the CME and ICE approvals, and each compliance date as separate columns, the way Ines's card did for the one-minute rule. Then run (22.17) with bond- or segment-level changes, so the date effect $\bar\mu^{\text{post}} - \bar\mu^{\text{pre}}$, which here is mostly year-end balance-sheet dressing, cancels against controls that dress for the same photograph. Keep the repo date a separate event, and keep every placebo window clear of the real dates. Two more results should shake you. One is a pre-trend: treated flows diverging through 2026 as dealers migrate early (Uyeda put daily cleared Treasury volume about 165% above pre-proposal levels in September 2026). That means the pre-window is already treated and a sharp-window $\hat\delta$ measures the stragglers. The other is controls that move with the treated, because the same dealers clear both segments and sponsored repo already nets at the sponsor. That is Kaz's affiliate-indicator problem again. A last detail: the listing's business-day count has no holiday calendar, so a window across 2027-01-01 holds one fewer trading day than it thinks.

**The trap:** The common answer is "wrong date, use 2026-12-31" and stop there. The right date is still a year-end, so a before-and-after, or a weak control group, will hand the quarter-end photograph to the rule. The stale date is valuable precisely because it shares that calendar position.

**If you got this wrong, read:** §22.8.1 (placebo dates and the affiliate-indicator run), §22.4 (the rule and its Trend Watch: "give each one a placebo twin"), and the fourth envelope of §22.2.3.

**Z.22.6: ROBO maximizes transparency**

**Answer:** With $\Delta = 0$ and $C = \infty$, every principal block pays the full leak on its full true size: $s_B^\ast/2 = \lambda Q + \gamma\sigma^2 Q T_u/6$. On the worked example, a \$15mm block unwound over two hours goes from 7.34bp today (15 minutes, priced as the pooled \$12.5mm) to 9.38bp, up 28%. A \$25mm block goes from 8.59bp to 15.63bp, up 82%. A \$15mm block unwound in fifteen minutes goes from 0.23bp to 7.73bp. A \$1mm ticket barely moves, from 0.56bp to 0.63bp.

- **What survives:** small tickets; agency crosses; riskless-principal trades whose other side is done before the print; and trades the market reads as uninformative (small $\lambda$).
- **What dies:** principal risk transfer of blocks worked over an hour or two, which are exactly the trades the delay and the cap were protecting.
- **Where the rest goes:** portfolio trades (Chapter 19), where a basket price, flagged by the PT modifier, dilutes any one bond's signal; ETF creation and redemption (Chapter 20), where size moves in kind in the primary market and the price risk trades as a fund share; and agency and all-to-all protocols that match without warehousing.
- **The result that should worry ROBO's sponsor:** Asquith, Covert and Pathak found that transparency cut costs (high-yield costs down 22.9%, about \$600mm a year in savings), but that "trading activity does not increase and, by one measure, decreases." By that measure, high-yield activity fell 71.1%. Maximum transparency lowers the price of liquidity and shrinks the quantity on offer.

**How:** Put $\Delta = 0$ into (22.6). The positive part $(1 - 0/T_u)^+ = 1$ for every $T_u > 0$, so the dealer is fully exposed when the print appears. Only a trade with no inventory at execution ($T_u = 0$) escapes. With $C = \infty$, the inferred size is the true $Q$, so the pooling subsidy of (22.7) disappears for every block above \$12.5mm. Both terms are now linear in $Q$, so total cost grows like $Q^2$. That pushes size into protocols where nobody warehouses it or where the print says less. One honest caveat: (22.6) holds $\lambda$ fixed. Asquith, Covert and Pathak's cost result is the evidence that transparency lowers the average price too. Their volume result is the evidence that the block dealer's side of (22.6) is real.

**The trap:** The usual answer is "more information means less asymmetry, so spreads fall everywhere." That is true of the average ticket, and the average ticket is a \$1mm trade the auto-quoter crosses riskless. In (22.6) the delay and the cap are subsidies to the block dealer. Removing them raises the price of the trades a principal dealer exists to do, and the volume moves elsewhere or does not happen.

**If you got this wrong, read:** §22.2.1 (the delay as an option), §22.2.2 (pooling), and the Asquith, Covert and Pathak paragraph that opens §22.2; then Chapters 19 and 20 for the protocols.

<!-- STATUS: COMPLETE -->
