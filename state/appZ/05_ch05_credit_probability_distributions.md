## Z.05 Chapter 5: Probability Distributions in Distressed & High-Yield Credit

Six exercises. I recomputed every number in Python. Exercise 3's simulation extends Listing 5.3 (Appendix F) on seed 7 with a million paths, using that listing's other Kou inputs. None of the chapter's exercises carries a [Read]/[Derive]/[Build] tag. Exercise 3 is a build in all but name, and Exercise 5(c) is a modelling exercise with more than one defensible answer, so its solution shows one worked choice and the reasons for it.

**Z.05.1: Two bonds, one VaR**

**Answer:** (a) The BB, at $q = 0.8\%$, has skew $-11.0$ and excess kurtosis $120$. The CCC, at $q = 12\%$, has skew $-2.34$ and excess kurtosis $3.5$. (b) The BB's 95% VaR never sees default. Since $0.8\% < 5\%$, the 5th percentile sits in the survival world. The CCC's VaR does see it. Since $12\% > 5\%$, the 5th percentile sits inside the default lump, at about the 42nd percentile of the recovery distribution ($5/12$). (c) The screen is measuring $1/q$, which is how *rarely* the bond defaults, not how much it loses when it does. The CCC looks "safer" because it defaults so often that default has become part of the body of its distribution.

**How:** Pin both worlds to points. The return is then an affine function of a Bernoulli, and its shape depends on $q$ alone:

$$
\text{skew} = -\frac{1-2q}{\sqrt{q(1-q)}}, \qquad \text{exkurt} = \frac{1-6q(1-q)}{q(1-q)}.
$$

For the BB, $q(1-q) = 0.007936$. The skew is $-0.984/0.0891 = -11.05$ and the excess kurtosis is $(1 - 0.0476)/0.007936 = 120.0$. For the CCC, $q(1-q) = 0.1056$. The skew is $-0.76/0.325 = -2.34$ and the excess kurtosis is $(1-0.634)/0.1056 = 3.47$. For (b), a 95% VaR stands on the 5% mark of the whole distribution, and the default world is the bottom $q$ of it. If $q < 5\%$, the mark falls among the survival wobbles. If $q > 5\%$, it falls among the recoveries. Price, recovery and survival volatility enter neither part. The jump size $J$ sets the variance, never the shape.

**The trap:** The usual mistake is reading kurtosis (or the size of the skew) as a riskiness score and concluding the BB is the dangerous bond. Kurtosis does not depend on units or position size. It measures how much of the variance comes from a rare outlier rather than the crowd, so it rewards a bond for defaulting *often*. The other slip, in (b), is calling the CCC's VaR "blind too" by reflex. At 12% the default world is a big enough slice that the 95% VaR lands in it. The BB's VaR stays blind until you go past 99.2%.

**If you got this wrong, read:** §5.1.3, "Skew is minus one over root PD," then the 95% VaR row of the §5.1.4 table and the paragraph under it.

**Z.05.2: The convexity tax**

**Answer:** $\sigma_X = 6.74\%$, the survival-leg skew is $-0.13$, and the convexity tax is $|c|\,v = 14.8$ bp (about 15). Flip to $C^{\text{spr}} = +8$ and the volatility does not change. The skew becomes $+0.13$, and the 14.8 bp becomes a convexity *bonus* to the mean. Now put that non-call survival leg into Theo's bond ($q = 4\%$, $P_0 = 0.92$, recovery Beta with mean 40 and s.d. 27.5). The mixture skew is still about $-4.1$.

**How:** Here $v = \kappa^2 s^2 h = (0.35 \times 0.055)^2 = 0.000371$ and $c = \tfrac12 C^{\text{spr}} = -4$. The exact moments of §5.9.1 give

$$
\sigma_X^2 = (D^{\text{spr}})^2 v + 2c^2v^2 = 12.25 \times 0.000371 + 32 \times (0.000371)^2 = 0.004544,
$$

so $\sigma_X = 6.74\%$. The convexity term adds almost nothing to the variance. The third moment is $\mu_{3,X} = 6(D^{\text{spr}})^2 c\, v^2 + 8c^3v^3 = -4.04\times10^{-5}$, and dividing by $\sigma_X^3 = 3.06\times10^{-4}$ gives a skew of $-0.132$. The mean is $x_0 + c\,v$, so the tax is $|c|\,v = 4 \times 0.000371 = 0.00148$.

Flipping the sign of $C^{\text{spr}}$ flips the sign of $c$. The variance and $\mu_{4,X}$ contain only even powers of $c$, while $\mu_{3,X}$ is odd in $c$, so the skew becomes $+0.132$.

For the mixture, compare the pieces of the full third moment (the Full Derivation at the end of §5.1.4). The survival leg contributes $(1-q)\,\mu_{3,X} = +0.00004$. The between-world term $-q(1-q)(1-2q)J^3$, with $J \approx 0.62$, contributes $-0.0085$. The cross term $3q(1-q)J(\sigma_X^2 - \sigma_Y^2)$ adds $-0.0061$, because the recovery lump is much wider than the survival hump. The coin outweighs the convexity by a factor of about 200.

**The trap:** There are two. The first is getting the tax wrong. $|C^{\text{spr}}|\,v$ gives 30 bp, but the half belongs in $c$. Writing it as $\tfrac12 |C^{\text{spr}}|\,\kappa s$ is also wrong, because $v$ is a variance, $\kappa^2 s^2 h$. The second trap is concluding from the positive survival skew that a non-call bond "has right-skewed returns." The survival leg is a lump sitting next to a coin, and its skew is two orders of magnitude too small to change the overall shape.

NOTE (for the editor): The "right-skewed survival leg" comes from §5.9.1's Gaussian $\Delta s$, not from the bond. §5.2.4 says a lognormal spread (skew $+1.1$ at $\kappa = 0.35$) gives a survival-world return skew of "about $-1.1$," which positive convexity pushes back on only "a little." I simulated the same leg with lognormal relative spread changes, $\Delta s = s\,(e^{-\kappa^2/2 + \kappa Z} - 1)$, and four million draws. The skew is $-0.93$ at $C^{\text{spr}} = +8$, $-1.13$ at 0 and $-1.35$ at $-8$. The exercise's "show that the survival leg of a non-call bond is right-skewed" therefore holds only under the Gaussian-$\Delta s$ assumption. I suggest "under §5.9.1's Gaussian spread change, show that…", perhaps with a closing clause noting that with §5.2.3's lognormal spreads the leg stays left-skewed.

**If you got this wrong, read:** §5.9.1, "One last derivation: exact moments of the DTS survival leg," and then the Full Derivation at the end of §5.1.4 for the cross term.

**Z.05.3: Find the jump**

**Answer:** $\eta_2 = \ln 3/\ln 1.5 = 2.71$, $\mathbb{E}[V_\tau/B] = 2.71/3.71 = 0.730$, and the expected recovery given a jump default is $0.7 \times 0.730 = 51.1\%$. Then add the Brownian-bridge check to `simulate_kou_jd` and run it with Listing 5.3's other inputs ($\mu = 5\%$, $\sigma_V = 25\%$, $\eta_1 = 10$), weekly steps, seed 7 and a million paths. The one-year default probability rises from 15.75% to 17.10%, about 1.3 points or 8.5% of the uncorrected number. The whole rise is in the diffusive defaults, which go from 6.6% to 8.1%. Jump defaults stay at about 9.1%. A 2,520-step run with the bridge gives 17.08%, so the corrected weekly grid is effectively the continuous-monitoring answer. A daily grid *without* the bridge gives 16.51%, still half a point short. At the listing's own $\eta_2 = 4$ the rise is similar, from 13.74% to 15.14%.

**How:** Set the Result 1 intensity equal to the target:

$$
\lambda^{V}(1-p)\left(\frac{B}{V}\right)^{\eta_2} = 0.5 \times 0.6 \times 1.5^{-\eta_2} = 0.10.
$$

That gives $1.5^{\eta_2} = 3$, so $\eta_2 = 1.0986/0.4055 = 2.71$. Memorylessness makes the undershoot $U \sim \text{Exp}(\eta_2)$, so $\mathbb{E}[e^{-U}] = \eta_2/(1+\eta_2) = 0.730$. With $B = F$ and $\alpha = 0.3$,

$$
\mathbb{E}[R \mid \text{jump default}] = (1-\alpha)\,\frac{B}{F}\,\frac{\eta_2}{1+\eta_2} = 0.7 \times 0.730 = 51.1\%.
$$

That lies between the 52.5% and 46.7% rows of the §5.3.3 table, as it should for an $\eta_2$ between 3 and 2.

The build extends Listing 5.3 (Appendix F). In each step, keep the log-distance $x_t$ from before the diffusion move. For every path still above zero after that move, draw a uniform. If the uniform is below $\exp\!\left(-2x_t\,x_{t+\Delta t}/(\sigma_V^2\Delta t)\right)$, default the path and log it as diffusive, with `ratio` 1.0. The check belongs after the diffusion move and before the jumps, because the bridge formula applies only over a stretch of pure diffusion.

**The trap:** In the first part, the common slip is solving $(B/V)^{\eta_2} = 0.10$ and forgetting the $\lambda^{V}(1-p) = 0.3$ in front. That gives $\eta_2 = \ln 10/\ln 1.5 = 5.68$, a thin-jump world with an 85% undershoot. Another is to stop at 73% and call it the recovery. The 0.73 is assets over the barrier, before the 30% bankruptcy cost. In the build, don't apply the bridge probability to paths already below zero, because that double-counts them. And don't feed it $x$ after the jumps, because that slips a jump into what must be a pure-diffusion bridge. Finally, don't expect the one-year default probability to equal the 10% intensity. The intensity is instantaneous. Over a year the drift moves firms away from the barrier, so the jump-only default probability is about 9.1%, and diffusion adds another 8.

**If you got this wrong, read:** §5.3.3, Results 1 and 2 and the table that follows them, and then item (2) of the Ways This Blows Up box at the end of §5.9 for the bridge.

**Z.05.4: ROBO minimizes kurtosis**

**Answer:** The cap $\text{exkurt} \le 10$ holds exactly when $q(1-q) \ge 1/16$, that is, for $6.7\% \le q \le 93.3\%$. Every bond with a default probability below 6.7% fails it, and almost all distressed paper passes. At $q = \tfrac12$ the excess kurtosis is $-2$, the lowest any distribution can have. Here is a limit that does what the PM meant *(illustrative numbers)*: "Maximize yield subject to two limits. For every name, the jump-to-default loss $N_i\,(P_{0,i} - \mathbb{E}[R_i])$ must be at most 0.5% of NAV. For the book, the one-year 99% expected shortfall under $\mathbb{P}$, with defaults drawn on the common factor of §5.5.4, must be no worse than $-6\%$ of NAV." Theo's bond has a JTD of 52 points, so under that rule it can be at most $0.5\%/0.52 = 0.96\%$ of NAV in face.

**How:** Write $u = q(1-q)$. The skeleton's excess kurtosis is $(1-6u)/u = 1/u - 6$, so

$$
\frac{1}{u} - 6 \le 10 \iff u \ge \frac{1}{16} \iff q^2 - q + \tfrac{1}{16} \le 0 \iff \frac{1-\sqrt{3}/2}{2} \le q \le \frac{1+\sqrt{3}/2}{2},
$$

which is $0.067 \le q \le 0.933$. The cap acts as a *floor* on the default probability. At $q = \tfrac12$, $u = \tfrac14$ and $1/u - 6 = -2$.

That is the floor for any distribution, not just a bond. For a standardized $Z$, $\mathbb{E}[Z^4] - (\mathbb{E}[Z^2])^2 = \operatorname{Var}(Z^2) \ge 0$, so kurtosis is at least 1 and excess kurtosis at least $-2$. Equality needs $Z^2$ to be constant, which means two values with equal weight: a fair coin. The bond the metric scores best is therefore one equally likely to pay par or recovery. Yield rises with $q$, so the objective pulls the same way, and ROBO's ideal holding is a coin flip with a coupon attached.

The fix has to measure the *size* of the loss, and kurtosis cannot, because it does not depend on position size: double the position and the kurtosis stays the same. JTD prices the default card in dollars. The 99% ES averages the worst 1% of outcomes, which for any name with $q > 1\%$ means averaging inside the default lump (§5.1.4's $-92\%$).

**The trap:** The usual mistake is treating a kurtosis cap as conservative because "fat tails are bad." Excess kurtosis is about $1/q$, large when default is *rare*, so capping it bans the safe names and admits the distressed ones. The tempting repair, capping skew as well, fails the same way, because in the skeleton skew is also a function of $q$ alone. A limit that contains no position size and no loss amount cannot be a risk limit.

**If you got this wrong, read:** §5.1.3 for the two skeleton formulas, the VaR and expected-shortfall rows of the §5.1.4 table, and "95% VaR is blind whenever $q < 5\%$" in §5.10.

**Z.05.5: The 13-week model, one more time**

**Answer:** (a) $S = 0.998^8 \times 0.985^5 = 0.9841 \times 0.9272 = 0.9125$, so the 13-week default probability is $q = 8.75\%$. (b) The skeleton skew is $-2.92$ and the excess kurtosis 6.5. Because $q > 5\%$, a 13-week 95% VaR does see the default world. The 5% mark sits at about the 57th percentile of the default lump ($5/8.75$). (c) One defensible split uses §5.6.1's Moody's share of about 65% distressed exchanges: $q_{\text{DE}} \approx 5.7\%$, $q_{\text{HD}} \approx 3.1\%$, and survival 91.25%. The mixture is

$$
R_h = \mathbf{1}_{\{E=\text{S}\}}\,X + \mathbf{1}_{\{E=\text{DE}\}}\left(\frac{R_{\text{DE}}}{P_0} - 1\right) + \mathbf{1}_{\{E=\text{HD}\}}\left(\frac{R_{\text{HD}}}{P_0} - 1\right), \qquad E \sim \text{Categorical}(0.9125,\, 0.057,\, 0.031),
$$

with $R_{\text{HD}} \sim \text{Beta}(0.87, 1.30)$ (mean 40, s.d. 27.5) and

$$
f_{R_{\text{DE}}}(r) = w_{\text{in}}\,\text{Beta}(r;\, 5.59,\, 1.96) + (1-w_{\text{in}})\,\text{Beta}(r;\, 0.92,\, 2.77).
$$

The participant component is centred at 74 (s.d. 15) and the non-participant component at 25 (s.d. 20). All of (c) is *illustrative*.

**How:** (a) The survival curve is the product of one minus each week's hazard. The hazard view also tells you *when*: only 1.6 of the 8.75 points arrive in weeks 1–8, and the rest come after the revolver is gone. (b) Use Exercise 1's skeleton with $q = 0.0875$: $q(1-q) = 0.0798$, so the skew is $-0.825/0.2826 = -2.92$. The horizon is 13 weeks, so this is a 13-week VaR, not a one-year one.

(c) A default probability with no event type attached is now ambiguous (the §5.6.1 Trend Watch). Moody's June 2025 rates, 5.8% with distressed exchanges and 2.1% without, put the exchange share at $1 - 2.1/5.8 = 64\%$, and its 2025 full-year share was about 65%. For a sponsor-backed name whose agreement lets a simple majority do a non-pro-rata uptier, Mags's "runs out of patience in about week six" argues for at least that share.

The hard-default face takes §5.5.2's senior unsecured Beta. The exchange face takes two Betas, split by participation and fitted by the method of moments: $k = \mu(1-\mu)/\sigma^2 - 1$, $a = \mu k$, $b = (1-\mu)k$, which gives $k = 7.55$ for participants and $3.69$ for outsiders. The participant mean follows Serta's 74 exchange price and its 73.7–100 plan range. The outsider mean follows the remand court's 25. The weight $w_{\text{in}}$ is the probability that *you* are invited: about 0.1 for a small passive holder, close to 1 for a group member. At $w_{\text{in}} = 0.1$ the expected exchange recovery is $0.1 \times 74 + 0.9 \times 25 = 30$, *below* the hard default's 40, and that inversion is the lesson.

A full model would also send the exchange face into the re-default corridor, $\Pr(\text{HD by } t) = 0.25\,(1-e^{-0.60\,t})$. Within 13 weeks that moves at most 3.5% of the exchange mass, so it can be dropped at this horizon. At one year it is 11%, and it cannot.

**The trap:** In (a), adding the hazards, $8 \times 0.2\% + 5 \times 1.5\% = 9.1\%$. That is close here but wrong in principle, because you can only default in week 9 if you survived to it. In (b), calling the VaR "blind" by reflex. Blindness needs $q < 5\%$. At 8.75% the VaR lands in the lump, and its value then depends on the recovery Beta, which is where the work is. In (c), the classic error is setting $w_{\text{in}}$ to the participation share (52.6% at Serta, or "the group had 70%"). The other is giving the exchange face a single Beta with a middling mean, which averages two lumps into a hump that no holder will ever actually be paid.

**If you got this wrong, read:** §5.1.5 and its hazard-rate box for (a), and §5.1.3 for (b). For (c), read §5.6.1 (the three doors, the re-default clock, and "When the third state earns its parameters") and the Serta case in §5.6.2.

**Z.05.6: Two coins after the trim**

**Answer:** (a) The Kestrel spike is $60 \times (0.97 - 0.40) = -\$34.2$mm, at odds of $0.0335/0.6 = 5.6\%$ a year. The Halvorsen spike is $35 \times (0.78 - 0.40) = +\$13.3$mm, at $0.14/0.6 = 23.3\%$. (b) The expected jump P&L is $0.2333 \times 13.3 - 0.0558 \times 34.2 = 3.10 - 1.91 = +\$1.19$mm a year, and the jump standard deviation is $\sqrt{61.7 + 31.6} = \$9.66$mm. (c) Matching Kestrel's DTS takes $70{,}190/(0.78 \times 2.3 \times 1{,}400) = \$27.9$mm of Halvorsen face, and that short alone leaves $+\$0.57$mm. The other \$7.05mm of short adds $+\$0.625$mm. (d) Two lines. The short owes the lender Halvorsen's 7.25% coupon on \$35mm, about \$2.54mm a year. The borrow fee, reset to 300 bp on \$27.3mm of market value, is about \$0.82mm a year. Together that is \$3.36mm of cash cost against \$1.19mm of expected jump gain.

**How:** Strip each leg to §5.1.2's coin: a spike of face times (price minus recovery), with $\mathbb{Q}$ odds $\lambda \approx s/(1-R)$. Independent coins add their means and also their between-world variances:

$$
\operatorname{Var} = 34.2^2 \times 0.0558 \times 0.9442 + 13.3^2 \times 0.2333 \times 0.7667 = 61.7 + 31.6 = 93.3 .
$$

The jump s.d. has barely moved from April's \$9.8mm, but its make-up has. The long alone is \$7.85mm. The coins-only skew of the pair is now about $-1.8$, against $-1.4$ in April, because the short's spike has shrunk from \$19.5mm to \$13.3mm and offsets less of the Kestrel tail.

For (c), DTS per dollar of face is $P\,D^{\text{spr}}\,s$, and the expected jump per dollar of face is $s\,(P-R)/(1-R)$. Their ratio does not contain the spread:

$$
\frac{\text{expected jump}}{\text{DTS}} = \frac{P-R}{(1-R)\,P\,D^{\text{spr}}} .
$$

It is 0.272 for Kestrel and 0.353 for Halvorsen. In April the two were 0.270 and 0.272, which is why the April match netted to about $-\$10{,}000$. Halvorsen's fall in duration from 3.4 to 2.3 raises its ratio by 48%. Its fall in price from 90 to 78 lowers it by 12%, because there is less room to fall to 40. So even a DTS-matched \$27.9mm short carries \$0.57mm more expected default gain than the long carries expected loss. The \$7.05mm the 2:40 trim left above the match adds $0.2333 \times 7.05 \times 0.38 = \$0.625$mm.

For (d), the +\$1.19mm is a $\mathbb{Q}$ number. The 23.3% is what the market charges for Halvorsen's coin, and the short pays that charge every year Halvorsen survives: in the coupon it owes the lender, and in the pull to par running against it. The fee's jump from 50 bp to 300 bp is the price of a crowd wanting to hold the same coin. Add the long's \$3.6mm coupon and roughly \$0.6mm of financing, and the pair now runs at about $-\$0.36$mm a year before the CDX HY carry.

**The trap:** In (b), people net the spikes ($34.2 - 13.3 = \$20.9$mm) and call that the pair's tail, or they subtract the variances. Independent coins add variance even when their means offset. In (c), the trap is assuming a DTS match is a jump match. It is one only when prices and durations are close, as they were in April, because DTS scales with duration and the jump does not (§5.3.1). A second trap is putting all of the +\$1.19mm down to the DTS overhang and treating the CDX HY sale as the fix. The index moves neither spike. In (d), the trap is taking a positive expected jump P&L as free. At $\mathbb{Q}$ odds the short's expected gain is just what it pays in carry. Under $\mathbb{P}$ the odds are lower and the gain is smaller, while the coupon and the fee go out in cash every day.

**If you got this wrong, read:** The Pair box at the end of §5.1.4 (PB-01 in April), then §1B.2 for the orange line, the 2:40 trim and the carry lines. §8D.4, "Two Jump Processes," has the expected-jump formula, and §5.3.1's Dynkin annotation explains why a jump to default ignores duration.

<!-- STATUS: COMPLETE -->
