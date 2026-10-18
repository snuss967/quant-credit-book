## Chapter 3: Cognitive Rewiring, From PJT RSSG to Systematic Desk Head

Six exercises, one for each tool in the chapter's engine. Every number below was recomputed from the chapter's equations, and the code-facing ones from Blocks 2, 4 and 6 run on their own seed (Appendix F, Listings 3.2, 3.4 and 3.6). Write your answer down before you read ours; the gap is your markout.

**Z.03.1: Moyer's footnote, with a clock**

**Answer:** (a) Both models price at 85: $0.625(100) + 0.375(60) = 85$ and $0.50(100) + 0.25(80) + 0.25(60) = 85$. Their standard deviations are 19.36 points (A) and 16.58 points (B). (b) For Model A at $\pi = 0.1$, the exact charge is 1.92 points below the mid for a sell RFQ and 1.83 points above it for a buy RFQ, against a symmetric $\pi \times \text{sd} = 1.94$. (c) $\sigma_V(5) = 9.29$ points for A and 8.14 for B, so the bids are about 84.07 and 84.19. Choosing between the models moves the bid by 0.11 points. The horizon moves it by about a point, because pricing to resolution would give bids of 83.06 and 83.34.

**How:** In A the variance is $p(1-p)\Delta^2 = 0.625 \times 0.375 \times 40^2 = 375$. In B it is $0.5(15)^2 + 0.25(5)^2 + 0.25(25)^2 = 275$. Both models are point masses, so all of their variance is between-scenario. For (b), use the asymmetric Glosten–Milgrom formula with $q = 0.625$ and $\Delta = 40$. The buy side is the same formula with $q$ and $1-q$ swapped:

$$
m - b = \frac{\Delta\,q(1-q)\,\pi}{\tfrac{1-\pi}{2} + \pi(1-q)} = \frac{0.9375}{0.4875} = 1.923, \qquad
a - m = \frac{\Delta\,q(1-q)\,\pi}{\tfrac{1-\pi}{2} + \pi q} = \frac{0.9375}{0.5125} = 1.829 .
$$

The sell side is wider because informed sellers appear only in the bad state, and the bad state is the less likely one. A sell RFQ is therefore the bigger surprise and moves the posterior further than a buy, which points where the prior already leans. For (c), apply §3.1.3 to each model and set the bid at $85 - 0.1\,\sigma_V(5)$:

$$
\sigma_V^2(5) \approx \rho\,\operatorname{Var}_{\text{between}} + h\,\sigma_{\text{d}}^2 = 0.2 \times 375 + 5 \times 1.5^2 = 86.25 \;(\text{A}), \qquad 0.2 \times 275 + 11.25 = 66.25 \;(\text{B}).
$$

**The trap:** Pricing the five-day quote off the resolution-day standard deviation (19.36 or 16.58). That gives bids near 83.1 and 83.3, so the client is charged a full point for uncertainty that will not resolve while you hold the bond. In (b), the usual slip is to reuse the sell-side denominator for the buy and get 1.92 both ways. The numbers have a lesson for the banker: arguing about scenario probabilities is the right instinct for the case and the wrong one for the quote.

**If you got this wrong, read:** §3.1.1 (two-point variance), §3.1.2 (the law of total variance), §3.1.3 (the horizon), and in §3.2.1 "The Full Derivation: the Glosten–Milgrom bid" (the asymmetric version).

**Z.03.2: Switch off the winner's curse**

**Answer:** (a) Test A still passes, and so does Test B's first assertion (fills are 49% of the tape). The run stops at `assert mo_fill.mean() < -3 * se(mo_fill)`. On the seeded tape the fill markout is $-0.006$ points with a standard error of 0.005, which is about $-1.2$ standard errors, nowhere near $-3$. This is the correct failure. With $\rho = 0$, winning tells you nothing about the value, and Glosten–Milgrom at the true $\pi(x)$ breaks even on fills just as it does on the whole tape. A test that still passed with its effect switched off would be testing nothing. (b) A winner's curse needs a common value: a prize worth the same to every bidder, which each bidder estimates with error. A bond's post-trade value is the next mid, and that number is the same for every dealer, so it is almost purely common. (c) Cover prices let you test a *larger* shading on history but not a smaller one.

**How:** (a) In Listing 3.2 a rival's effective concession is `conc - eta * rho * sigma_v * u`. At $\rho = 0$ it is independent of $u$. Whether you win then depends on $h^{\text{GM}}(x)$ and on noise unrelated to the value, so

$$
\mathbb{E}[\text{MO} \mid \text{fill}, x] = \mathbb{E}[\text{MO} \mid x] = 0 .
$$

Your fills still lean toward low-$\pi$ RFQs, because a smaller half-spread wins more often. The lean costs nothing, because the GM quote breaks even at every $x$. (b) Under private values each bidder knows what the prize is worth to *it*, so winning reveals nothing. Under common values, winning means your estimate was the most optimistic one in the room. A dealer's private components (inventory, balance sheet, an axe) are small next to "where will this mark in five days?". (c) On a Done RFQ, an extra shading $\Delta$ still wins exactly when the shaded price still beats the cover. If it does, the markout improves by $\Delta$; if it does not, the RFQ drops out of the Done set. Replaying that over history evaluates any larger $w(n)$. A smaller $w(n)$ would also have won some RFQs you lost, and whether it beats the winner depends on the winning level. Losers rarely see that level: "Covered" tells you your rank, not your distance from the winner.

**The trap:** Saying that both Test B assertions fail. The second one, `mo_lost.mean() > mo_fill.mean()`, compares two means that are both zero in expectation, so it is a coin flip. On seed 3 it passes by less than one standard error. On seven other seeds we tried it failed twice. In the listing it never runs, because the assertion before it stops the script. One more thing to see: with $\rho = 0$, Block 2's last line (the $w(n)$ shading) cuts fills from 49% to 3.3% at $+0.17$ points each. Shading against a curse that is not there buys margin by giving away nearly all the volume.

**If you got this wrong, read:** §3.2.3 (the winner's curse and the Poker Table on cover prices), §3.3.5 (Done, Covered, Traded Away), and Block 2 of §3.8 with Listing 3.2 in Appendix F.

**Z.03.3: Kaz's bag of words, de-biased**

**Answer:** (a) $p^{*} = 0.218$. (b) Kaz's shortcut gives $p\,T/S = 0.054$, which is four times too low. As $p \to 1$ the corrected value goes to 1, while the shortcut can never exceed $T/S = 0.06$. (c) With $T = 0.15$ the corrected value is 0.614 and the shortcut 0.27. (d) About 2,280bp. The hazards are $-\ln(1 - 0.218) = 0.2456$ and $-\ln(1 - 0.054) = 0.0555$, and $0.6 \times 2 \times 0.1901 = 0.228$. (e) One answer: "The model learned how much more often defaulters use the phrase than survivors do, not how often users of the phrase default, and only the second number trades."

**How:** Elkan's correction is an odds update, scaled by the ratio of the live base-rate odds to the sample's:

$$
\frac{p^{*}}{1-p^{*}} = \frac{p}{1-p}\cdot\frac{T/(1-T)}{S/(1-S)} = 9 \times \frac{0.03/0.97}{1} = 0.278
\;\;\Rightarrow\;\; p^{*} = \frac{0.278}{1.278} = 0.218 .
$$

At $S = 0.5$ the sample odds are 1, so the correction reduces to multiplying the model's odds by the live odds. In (c) the live odds are $0.15/0.85 = 0.176$, the posterior odds are 1.59, and $p^{*} = 0.614$. The shortcut rescales the probability rather than the odds. That is the first-order version of the update and holds only while $p$ is small. At $p = 0.9$ the model's odds are 9, and the shortcut discards them. For (d), convert each answer to a one-year hazard, $\lambda = -\ln(1-p)$, and apply $\Delta s \approx L\,\kappa\,\Delta\lambda$.

**The trap:** §3.4.3 warns that the $T/S$ shortcut *overstates* and can exceed one, so readers expect it to err high here. That warning is for $T > S$, Bohn and Stein's case. Kaz's balanced sample has $S = 0.5 > T$, so the shortcut errs low, and the error is largest on the highest-scoring filings, which are the names you most need to price. In (d), the usual slip is to difference probabilities instead of hazards: $(0.218 - 0.054) \times 1.2 \times 10^4 \approx 1{,}965$bp.

**If you got this wrong, read:** §3.4.3 and "The Full Derivation: Elkan's correction is a Bayes update"; §3.4.2 for the hazard inversion and the explicit $\kappa$; Listing 3.5 in Appendix F (`elkan`, `hazard_from_pd`).

**Z.03.4: Put the Ledger on a clock**

**Answer:** (a) The flow signal has an IC of 0.079 at 1 day and 0.031 at 5 days. The fulcrum view has 0.040 and 0.039. (b) $h^\star = 4.07$ business days, from the closed form and from a numerical root alike. (c) The flow signal belongs in $\pi(x)$ only. The fulcrum view belongs in both, because it beats the flow signal at the 5-day markout horizon (0.039 against 0.031) and dominates at 20 days (0.036 against 0.001). (d) One definition: a counterparty's lie rate is the shrunk fraction of the axes or indications it showed the desk that were followed, within $k$ business days, by its own RFQs or trades in the opposite direction. You can build it from your own RFQ and axe logs. Give it a long half-life, months to years, because a grudge lasts.

**How:** Use $\text{IC}(h) = \text{IC}_0\,2^{-h/h_{1/2}}$, set the two features equal, and take logs:

$$
\ln 0.10 - \frac{h\ln 2}{3} = \ln 0.04 - \frac{h\ln 2}{120}
\;\;\Rightarrow\;\;
h^\star = \frac{\ln(0.10/0.04)}{\ln 2\,\big(1/3 - 1/120\big)} = \frac{0.9163}{0.2253} = 4.07 .
$$

By day 20 the flow signal has been through almost seven half-lives, while the fulcrum view has lost about a tenth of its power. Shrink the lie rate with the same estimator as §3.3.4, so that one broken axe does not condemn an account.

**The trap:** Ranking the features by $\text{IC}_0$ and putting the flow signal everywhere because 0.10 beats 0.04. The ranking flips after four days, which is inside the RFQ engine's own five-day horizon. The banker's version of the mistake runs the other way: keeping the fulcrum view out of $\pi(x)$ because it is "a portfolio view" that took ninety hours to build. At five days it beats the tape. A mechanical slip is to write $e^{-h/h_{1/2}}$ for $2^{-h/h_{1/2}}$, which treats the half-life as an e-folding time and gives $h^\star = 2.8$ days.

**If you got this wrong, read:** §3.5 (the decay column, the IC formula and Paleologo's common clock), the half-life box in §9.4.1, and §3.3.4 for shrinking the lie rate.

**Z.03.5: Detector economics**

**Answer:** (a) At $h = 4$ the bound is at most $400 \times 252 / e^{4} \approx 1{,}846$ false alarms a year; at $h = 8$ it is about 34. (b) $K = 1/2$, so detection takes about 8 days at $h = 4$ and 16 days at $h = 8$, leaving about 22 and 14 days of warning. (c) The thresholds are $h = 3.80$, 6.00 and 8.20 for PRS 0.9, 0.5 and 0.1, with delays of about 7.6, 12 and 16.4 days. Reading the documents buys about 8.8 days of warning across that range. (d) $h \ge \ln(400 \times 252/52) = \ln 1{,}938 = 7.57$. Under the chapter's Gaussian model, the realized rate at that threshold is about 8 alarms a year, not 52.

**How:** Lorden says the null average run length is at least $e^{h}$, so each tranche raises at most $252/e^{h}$ false alarms a year; multiply by 400. The delay is about $h/K$ with $K = \mu_1^2/(2\sigma_y^2) = \tfrac12$, so it is simply $2h$ days. The PRS threshold is

$$
h(\text{PRS}) = h_0 - \ln\frac{\text{PRS}}{1-\text{PRS}} = 6 \mp \ln 9 = 6 \mp 2.197 .
$$

All three values sit inside Listing 3.6's floor of 2.5 and cap of 10, so the clip never binds. For (d), the realized rate is lower because $e^{h}$ is a floor on the run length, not its value. Under the null, each day's evidence has a mean of $-K$, and the tally keeps resetting at zero, so it takes far longer to drift to $h$ than the bound allows. Siegmund's approximation and a 2,000-path simulation of (3.5) agree on the size of the gap. The run length is about 331 days against a bound of 55 at $h = 4$, consistent with Block 6's censored 304. At $h = 7.57$ it is about 12,000 days against 1,939. The simulated delays come out a few tenths of a day above $h/K$ (8.4 at $h = 4$, 16.4 at $h = 8$), because the tally overshoots the line. The PRS gap is still about 8.7 days.

**The trap:** Treating $e^{h}$ as *the* run length, then setting $h = 7.57$ and budgeting for 52 alarms a year. Compliance will see about eight. The overcorrection is just as wrong. Under independent Gaussian flow, $h \approx 5.75$ would already deliver about 52 real alarms a year, but real ADV-scaled flow is fat-tailed and autocorrelated. §3.8 calls $e^{h}$ a design target, not a guarantee, so keep it. A smaller slip: dropping the 400 tranches, which gives 4.6 alarms a year at $h = 4$, or using 365 calendar days instead of 252 trading days.

**If you got this wrong, read:** §3.6.2, including "The Full Derivation: Page's CUSUM" and "The prior: the documents set the fuse"; Block 6 of §3.8 and Listing 3.6 in Appendix F.

**Z.03.6: ROBO and the lucky client**

**Answer:** (a) ROBO ranks clients by raw mean markout. The one-fill client's $+300$bp puts it at the top, so it gets the tightest quote on the platform. It keeps that quote until its next trade, which comes quickly, because the best price on the platform is now being shown to it. (b) $\sigma^2/\tau^2 = 56.25$, so $k = 0.017$, 0.151 and 0.640 for $n = 1$, 10 and 100. The one-fill client's shrunk score is about $+5$bp ($0.0175 \times 300 = 5.2$). (c) For example: "Score each counterparty by the empirical-Bayes shrunk mean of its 5-day IDO markouts, in bp of price, re-estimating the between-counterparty variance monthly and flooring it at zero. Tighten quotes by at most `c` bp of price per bp of shrunk score, never on a raw mean, and log every override for a counterparty with fewer than `n_min` fills." (d) Selecting the top of many noisy scores selects for noise.

**How:** With $\sigma = 150$bp and $\tau = 20$bp,

$$
k = \frac{n}{n + \sigma^2/\tau^2}: \qquad \frac{1}{57.25} = 0.017, \qquad \frac{10}{66.25} = 0.151, \qquad \frac{100}{156.25} = 0.640 .
$$

A client needs 56 fills before its own record gets half the weight. The IDO requirement in (c) is what keeps the score from charging a client for the tide (§3.3.3). For (d), if you rank many clients by score $= \theta_c + \text{noise}$, the top of the list is selected for positive noise, so $\mathbb{E}[\text{noise} \mid \text{ranked first}] > 0$. It is the winner's curse again, with you as the auctioneer and your own scores as the bidders.

**The trap:** Using $\sigma/\tau = 7.5$ instead of $\sigma^2/\tau^2 = 56.25$, which gives $k(1) = 0.118$ and a score of 35bp. Another slip is to plug in Block 4's *estimated* $\hat\tau \approx 42$bp. That gives $\sigma^2/\hat\tau^2 \approx 12.5$, $k(1) = 0.074$ and a score of 22bp. The exercise asks for the true spread, and an estimate that comes out at double the truth on a seeded panel is the reason the spec re-estimates and floors $\tau^2$ rather than trusting a single fit. Watch the sign as well: a $+300$bp markout is *good* for the dealer, so ROBO's error is generosity to a lucky client, not suspicion of a toxic one.

**If you got this wrong, read:** §3.3.4 (counterparty scores, shrunk, and the batting-average box), §3.3.3 (IDO markouts), §3.2.3 (the winner's curse), and Listing 3.4 in Appendix F (`shrunk_cpty_scores`).

<!-- STATUS: COMPLETE -->
