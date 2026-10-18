## Chapter 20: Credit ETF Creation/Redemption Arbitrage (HYG, JNK, LQD, BKLN)

Six exercises: one on the census, one on Kaz's regression, one on the AP count, one on basket cardinality, one on the Fed's clause and one on the loan sleeve. We checked every number in python3, and the toy runs reuse Listing 20.1 (Appendix F) with its seed. Write your answer down before you read ours.

**Z.20.1: The premium-day census**

**Answer:** $(f^R + k^R)/(2\bar c + f^C + k^C) = 44/206 = 0.214$. Under a uniform premium the redemption door sits about a fifth as far below zero as the creation door sits above it. If the creation door is at the chapter's illustrative $+66$ bp, the redemption door is at about $-14$ bp. In a year of net inflows the uniform assumption is wrong, and it biases the ratio **down**: 0.214 is a floor, and the true lower door is further from zero than the census suggests.

**How:** With pro rata baskets, (20.4) runs from $\pi^{\text{lo}} = -a$ to $\pi^{\text{hi}} = b$, where $a = f^R + k^R$ and $b = 2\bar c + f^C + k^C$. If the premium is uniform on that interval, the share of discount days is the share of the room below zero:

$$
\frac{44}{250} = \frac{a}{a + b} \quad\Longrightarrow\quad \frac{a}{b} = \frac{44}{250 - 44} = \frac{44}{206} = 0.214 .
$$

Now the lean. In steady inflows the APs create at the margin, so the premium spends its time pressed against the upper door, and the density rises toward $\pi^{\text{hi}}$. For any true pair of doors that lean puts *fewer* closes below zero than a uniform would, so inverting the uniform reads the scarce discount days as a lower door close to zero. Here is how big the effect is: if the density rises linearly from the lower door to the upper one, then $P(\pi < 0) = \big(a/(a+b)\big)^2$, and the same 44/250 gives $a/(a+b) = 0.420$ and $a/b = 0.72$, more than three times the uniform answer. A rising market pushes the same way, because a NAV that lags a rally adds a positive staleness term $s_t$ to every close.

**The trap:** Answering $44/250 = 0.176$. That is $a/(a+b)$, the lower door's share of the whole room, but the exercise asks for the lower door over the upper door, $a/b$. The second trap is to think the lean makes 0.214 too high. Inflows pile the premium against the creation door, so the census *under*-counts discount days and makes the redemption door look closer than it is.

**If you got this wrong, read:** §20.3.1, "Reading the band: a census and two doors" (and the Math, Gently box on the room with two doors).

**Z.20.2: Kaz's regression**

**Answer:** Kaz's reading is only one of three that fit $\hat\eta = 0.08$. Taken at face value it is internally consistent: at $\eta = 0.08$ a gap has a half-life of 8.3 trading days, and 43% of it is still open after ten. But the attenuation formula allows two other stories. (1) **A noisy ETF:** the NAV is moderately fast, but flow noise dominates the premium. For example, $\eta = 0.4$ with a staleness share of $0.2$, which needs $\sigma_\ell = 1.5\,\sigma_r$. (2) **A fresh NAV:** the evaluator is quick, so there is almost no staleness to find, and even mild flow noise swamps it. For example, $\eta = 0.9$ with $\sigma_\ell = 0.32\,\sigma_r$, which gives a staleness share of $0.089$. The second regression puts the NAV return on lagged ETF returns, one lag at a time. The ratio of successive slopes is $1 - \eta$, and flow noise does not affect it. On ten years of simulated daily data it reads 0.92, 0.60 and 0.10 in the three cases (5th–95th percentiles 0.88–0.95, 0.53–0.67 and 0.06–0.13), so the three stories separate cleanly.

**How:** The formula from §20.2.2 is $\hat\eta \to \eta\,V_s/(V_s + V_\ell)$, where $V_s = \sigma_r^2(1-\eta)^2/\big(\eta(2-\eta)\big)$. A small slope needs either a small $\eta$ or a small staleness share, and the share can be small for two reasons: $V_\ell$ is large, or $V_s$ is small because $\eta$ is large. So the slope is hump-shaped in $\eta$. With $V_\ell/\sigma_r^2 = 0.10$ it peaks at about 0.39 near $\eta = 0.57$ and returns 0.08 at both $\eta = 0.08$ and $\eta = 0.9$. For the second regression, recall that partial adjustment makes the NAV return a geometric distributed lag of true returns, $\Delta\ln\tilde M_t = \eta\sum_{i \ge 0}(1-\eta)^i r_{t-i}$. The ETF return is $\Delta\ln P_{t-j} = r_{t-j} + \ell_{t-j} - \ell_{t-j-1}$. Regress the first on the second separately for each $j = 0, \dots, 10$:

$$
b_j = \frac{\operatorname{Cov}(\Delta\ln\text{NAV}_t,\ \Delta\ln P_{t-j})}{\operatorname{Var}(\Delta\ln P)} = \frac{\eta(1-\eta)^j\,\sigma_r^2}{\operatorname{Var}(\Delta\ln P)}, \qquad \frac{b_{j+1}}{b_j} = 1 - \eta .
$$

Flow noise is independent of true returns, so it never enters the covariance. It only inflates the common denominator, and the ratio cancels it. Here are the three fingerprints. A slow NAV gives a long, flat tail: about 0.08 at every lag, and still 0.035 at lag 10. A noisy ETF gives small slopes that die within a week, with an extra hump at lag 1 if you run the lags jointly. A fresh NAV puts nearly everything on lag 0. (Instrumenting $p_{t-1}$ with $\Delta\ln P_{t-2}$ recovers $\eta$ too, but in the fresh-NAV case the instrument is weak, because its first stage is $(1-\eta)^2\sigma_r^2$.)

**The trap:** Treating the slope as $\eta$ and stopping there. The wobbling ruler always flattens the slope and never steepens it, so $\hat\eta$ is a lower bound on how fast the NAV catches up, not an estimate of it. The subtler trap is to think the only alternative is "noisy ETF". A very *fresh* NAV also gives a small slope, because there is little staleness for the premium to carry.

NOTE (for the editor): The display just above (20.3) reads $\Delta \ln \text{NAV}_t = \Delta \ln \tilde M_t - \Delta \ln(1 - \bar c_t)$. Since $\text{NAV}_t = \tilde M_t(1 - \bar c_t)$, the sign should be $+\Delta\ln(1-\bar c_t)$. With the printed sign, widening spreads would *raise* NAV returns. The last paragraph of §20.2.2 calls "$-\Delta \ln(1 - \bar c_t)$" a "negative drag", which is true only of $+\Delta\ln(1-\bar c_t)$. The economics is right and the sign is wrong in both places. (20.3) itself is unaffected, because it assumes a constant $\bar c$.

**If you got this wrong, read:** §20.2.2 (the Math, Gently box "A ruler with a wobbling zero" and the attenuation formula), then §20.2.1 for (20.2), and Block 2 of Listing 20.1 (`nav_catchup`).

