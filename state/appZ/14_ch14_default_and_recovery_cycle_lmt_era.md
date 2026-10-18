## Z.14 Chapter 14: The Default & Recovery Cycle in the LMT Era

Six exercises. Every number below was recomputed in Python. Exercise 3 uses `coop_break_prob` from Listing 14.3, and Exercise 6 runs `fit_ms2` from Listing 14.4 (Appendix F) on 200 simulated histories at each sample size. There are three notes for the editor, in Z.14.2, Z.14.3 and Z.14.6. Write your card before you read ours.

**Z.14.1: Two rates, two hazards**

**Answer:** The all-cause intensity is $\lambda = -\ln(1 - 0.058) = 0.0598$ a year. The ex-DE rate says 2.1 of the 5.8 points were hard defaults, so split $\lambda$ in that proportion: $\lambda_H = 0.0216$ and $\lambda_D = 0.0381$ a year, and $\lambda_D/\lambda_H = 3.7/2.1 =$ **1.76**. Over three years, **$F_H(3) = 5.9\%$** and **$F_D(3) = 10.5\%$**, and 83.6% of the cohort has had no event. The chapter's rounded 0.022 and 0.038 give 6.0% and 10.4%, the numbers carried into §14.3.3. Converting 2.1% directly gives $-\ln(0.979) = 0.0212$. That leaves $\lambda_D = 0.0385$ and a ratio of 1.82: close, but the split is the version consistent with competing risks.

For the PM: "Standard North American CDS, and so the CDX, pays on bankruptcy and failure to pay. It does not pay on a distressed exchange. The hazard you back out of CDX spreads is therefore a hard-default hazard, and the only agency number it can be set against is the ex-DE rate, 2.1%, an intensity of about 2.2% a year. It cannot be set against the 5.8% headline, whose intensity is 6.0%. Put an implied hazard of 5% (illustrative: 300 bp at the 40% quoting convention) next to the headline and the market seems to be underpricing default. Put it next to the hard rate and the market is charging 2.3 times what was realized, which is an ordinary risk premium. Before you trust even that ratio, replace the 40% with a recovery that fits these names, and check that the index and the agency cohort cover the same borrowers."

**How:** A twelve-month rate is a one-year cumulative incidence, not a hazard. With constant hazards, $F_k(1) = (\lambda_k/\lambda)(1 - e^{-\lambda})$ and $\sum_k F_k(1) = 1 - e^{-\lambda} = 0.058$. That fixes $\lambda$, and the ratio of the two observed incidences is the ratio of the hazards:

$$
\frac{\lambda_D}{\lambda_H} = \frac{F_D(1)}{F_H(1)} = \frac{0.058 - 0.021}{0.021} = 1.76 .
$$

Three years out, $1 - e^{-3\lambda} = 1 - e^{-0.179} = 0.164$, so $F_H(3) = 0.362 \times 0.164 = 0.059$ and $F_D(3) = 0.638 \times 0.164 = 0.105$. The direct conversion, $-\ln(1 - 0.021)$, reads 2.1% as the chance of a hard default in a world without exchanges. In this world, exchanges remove issuers before they can file, so the direct conversion slightly understates $\lambda_H$ (0.0212 against 0.0216). It is the Kaplan–Meier trap run backwards.

**The trap:** Adding odometer readings: $3 \times 5.8\% = 17.4\%$ in total, or $3 \times 3.7\% = 11.1\%$ for exchanges. A subtler slip is computing each cause as if it were the only one, $1 - e^{-3\lambda_D} = 10.8\%$ and $1 - e^{-3\lambda_H} = 6.3\%$. Each ignores the other tap draining the same bucket, so between them they lose 17.1% of a cohort that only loses 16.4%. In the PM paragraph the trap is the 7:10 note itself: dividing the CDS hazard by the 6.0% headline intensity and calling the shortfall a mispricing.

**If you got this wrong, read:** §14.1 (the odometer-and-speedometer box and Moody's 5.8% and 2.1%), §14.2.1 for the constant-hazard CIF and the two-cause split, and §14.7.2 for the definitional wedge and the 7:10 note.

**Z.14.2: Kaz's parole question**

**Answer:** Fact 3 gives $\eta = 2/1.204^{1/k}$. Hazards are per year, and pp means percentage points:

| $k$ | $\eta$ (years) | $h_H(0.5)$ | $h_H(2)$ | $h_H(6)$ | Year-six increment $p\,[S_0(5)-S_0(6)]$ |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 0.8 | 1.586 | 0.116 | 0.044 | 0.0070 | 0.66 pp |
| 1.0 | 1.661 | 0.119 | 0.055 | 0.0054 | 0.56 pp |
| 1.2 | 1.713 | 0.115 | 0.066 | 0.0033 | 0.39 pp |
| 1.5 | 1.767 | 0.101 | 0.082 | 0.0010 | 0.17 pp |

Only **$k = 1.2$ and $k = 1.5$** satisfy all four facts. $k = 0.8$ fails fact 4 clearly and $k = 1.0$ narrowly; the pass line sits at $k \approx 1.07$. The four facts set a floor on $k$ and no ceiling, so they cannot choose between 1.2 and 1.5. For shorting, the answer is timing. With $k > 1$ the population hazard is lowest at the closing. For most of the first year it then stays within a few points of its peak of about 0.115 a year, which comes at 0.47 years for $k = 1.2$ and 0.97 years for $k = 1.5$. It is still 0.07–0.08 at two years and is below 0.01 by year five. So short a post-LME loan inside the first two years, timed to the name's own runway cliff. On the closing day you pay carry while the new money is still in the bank. After year three you are short a population that is mostly cured, against a hazard that is under 4% and falling.

**How:** Facts 1 and 3 are spent on the calibration: fact 1 sets $p = 0.25$, and fact 3, $1 - S_0(2) = 0.70$, gives $(2/\eta)^k = -\ln 0.30$. Fact 2 is about a different event (a hard default *or* another exchange), so it sets $p \approx 0.35$–$0.40$ for that event and says nothing about $k$. The second half of fact 4, two-thirds clean within a decade, holds for every shape, because $p\,[1 - S_0(10)]$ lies between 0.247 and 0.250 here (and is 0.35 at the fact-2 $p$). The discriminating fact is the first half of fact 4, and year six is its binding year, because the increments shrink every year after it. The population hazard is

$$
h_H(u) = \frac{p\,f_0(u)}{(1-p) + p\,S_0(u)} = \underbrace{\frac{k}{\eta}\left(\frac{u}{\eta}\right)^{k-1}}_{\text{hazard if susceptible}} \times \underbrace{\frac{p\,S_0(u)}{(1-p) + p\,S_0(u)}}_{\mathbb{P}(\text{susceptible}\,\mid\,U > u)} .
$$

For $k > 1$ the first factor rises without limit and the second collapses as the susceptible fail out. Their product rises and then falls, and that hump is the parole window. For $k \le 1$ the hump disappears and day one is the riskiest day. One nuance on $k = 1$: Moody's says *more than* 70% within two years, and at 71.7% the constant-hazard clock passes fact 4. The chapter's "borderline" is fair.

**The trap:** The first trap is the "weakest fail first" intuition, which reaches for $k < 1$. That curve passes the two-year anchor and then leaves 0.66 pp a year in the tail, against Moody's half point, and its hazard is highest on the closing day, so it tells you to short immediately. The second trap is reading the susceptible hazard as the population's. At $k = 1.2$ the susceptible hazard at $u = 6$ is 0.90 a year and still rising. The population hazard is 0.0033, because almost nobody susceptible is left. Mixing the two up is how a desk ends up shorting a six-year survivor because "the hazard is still rising."

NOTE (for the editor): §14.8.2 says Mitel, filing 29 months after its uptier, failed "inside the high-hazard window that the $k > 1$ calibration predicts." On the pooled clock of §14.3.2 ($p = 0.25$, $k = 1.2$, $\eta = 1.71$), 78% of eventual defaulters have already failed by 29 months, and the population hazard there is 0.051 a year, less than half its 0.115 peak. §14.8.1 calls Serta's 31 months, where the same figures are 80% and 0.046, "a late failure." Both cannot be right on one clock. Mitel fits only with a name-specific scale stretched by its roughly 2.5-year runway (§14.3.2's covariate story). For example, $\eta_i \approx 3.3$ makes 29 months the median susceptible failure time. Suggest "inside the window its own runway set, though late on the pooled clock."

**If you got this wrong, read:** §14.3.2: the lightbulb box, Moody's four facts, the calibration table and its Full Derivation. Then §14.9 for Kaz's "inside the hump" at fourteen months.

**Z.14.3: Which hump are you in?**

**Answer:** At $c = 0.70$ the co-op holds a blocking position, because $1 - c = 0.30 < 0.501$. A deal needs defectors holding $m + c - 1 = 20.1\%$ of the class. At 7% per member, that is $d^\ast = \lceil 2.87 \rceil = 3$ members. At $\varphi = 0.10$ the probability of a non-pro-rata deal is $\mathbb{P}(\mathrm{Bin}(10, 0.10) \ge 3) =$ **7.0%**. Once the sponsor buys defectors up to $\varphi = 0.35$, it is **73.8%**, more than ten times as likely. Read the co-op as the room: if a deal is done, members are inside at 74 and holders outside it are primed to 25. Then joining is worth at most $\Pi \times (\mu_{\text{in}} - \mu_{\text{out}}) = 0.738 \times 49 \approx$ **36 points**, about \$3.6mm on your \$10mm. Before the sponsor started paying ($\varphi = 0.10$), the same seat was worth 3.4 points (\$0.34mm). Both figures are ceilings, before the cost of the transfer restriction you would be signing.

**How:** Each of the ten members walks independently with probability $\varphi$, and the deal needs three to walk. $\mathbb{P}(X \le 2)$ is 0.930 at $\varphi = 0.10$ and 0.262 at $\varphi = 0.35$. Given a deal, the coalition mixture puts a holder's expected recovery at $\pi\mu_{\text{in}} + (1-\pi)\mu_{\text{out}}$. With no deal, the whole class is treated pro rata, and membership changes nothing. So a seat is worth

$$
\Pi(c)\,\big(\pi_{\text{member}} - \pi_{\text{outsider}}\big)\,(\mu_{\text{in}} - \mu_{\text{out}}) = 0.738 \times (1 - 0) \times 0.49 = 0.362 \text{ of par}.
$$

Notice how steep the tail is. $\Pi$ crosses one half at $\varphi = 0.26$, so a modest backstop fee turns the co-op from a wall into a coin flip, and the price of your seat moves almost one for one with what the sponsor pays defectors. That is "defection is not a coin flip, it is a price" in numbers.

**The trap:** Paying the full 49 points. The gap between the humps is the value of a seat only if a deal is certain. The opposite slip is pricing the seat at $\varphi = 0.10$, 3.4 points, after the sponsor has started paying: that trusts the independence a sponsor with a fee is paid to break. The third is using the blended mean, $0.526 \times 0.74 + 0.474 \times 0.25 = 0.51$, as "the" recovery. Membership belongs to the holder, not the loan, and a blended number prices nobody's actual position.

NOTE (for the editor): The exercise never says who is inside when the co-op breaks, and the arithmetic of §14.5.1 points the other way. Three defectors hold 21% of the class, so the sponsor's 50.1% needs 29.1 of the 30 points held outside the co-op. If the sponsor fills that gap from outsiders at random, then, given a break, an outsider is inside with probability 0.92 at $\varphi = 0.10$ and 0.70 at $\varphi = 0.35$, and it is the loyal members who get primed. On that reading a seat is worth at most $0.738 \times (1 - 0.70) \times 49 \approx 11$ points, and that only if a member can always sell its vote; for a member who stays loyal, it is worth less than nothing. The 36-point answer needs one more sentence, such as "assume that a deal, if done, is done with co-op members and primes everyone outside the co-op" (the Lumen shape of §14.5, where the group was the deal). Alternatively, recast "you" as a co-op member deciding whether to defect.

**If you got this wrong, read:** §14.5.1 (the threshold game, the jury, and "Defection is not a coin flip. It is a price."), §14.4.1 and §14.4.2 for the mixture and Stage 0, and the Lumen replay in §14.5 for what a closed door costs.

**Z.14.4: The best-performing tranche**

**Answer:** Nine percent simple interest from 22 June 2020 to the 7 July 2026 judgment runs for 6.04 years, which lifts the award from \$261.13mm to \$403.2mm, or **45.0 points per 100 of excluded face**. On \$5mm face that is \$2.25mm if collected, against \$1.0mm paid in January 2021: **2.25x, and a 13.4% IRR** over the 6.5 years to July 2027. At 60% the expected payoff is \$1.35mm, an **expected multiple of 1.35x**, and the IRR of that expected cash flow is **4.8% a year**. That is good, but not spectacular. The trade breaks even at a 44% chance of collection, and it needs 92% to clear the 12% litigation-finance hurdle of Kaz's tree. Even with the 2026 award and the 60% handed to you in advance, the claim discounted at 12% was worth about 13 points of face in January 2021, not the 20 paid. It is the best trade in the capital structure only on the branch where it gets paid.

The assumptions a litigation-finance desk would attack:

1. *Title.* Does a claim for a June 2020 breach travel with a loan bought in January 2021? That depends on the assignment documents and on whether the seller kept the claim. The award ran to the plaintiffs' \$895mm, and a buyer outside that group owns a loan, not a claim. The \$1mm price does at least clear New York's \$500,000 safe harbor from champerty.
2. *The measure.* Damages run on face because of the sharing clause, §2.18(c). An appeal that moved to a market-value measure would shrink them, and the defendants will argue that a buyer at 20 bought after the harm and lost nothing.
3. *Interest.* The 9% runs to judgment. Post-judgment interest in federal court accrues at the one-year Treasury rate, not 9%, and both the rate and the start date can be appealed.
4. *The binary.* 60/40 leaves out the middle branches, a settlement at 70 cents on the dollar or a partial reversal, which is why Kaz's tree has three branches.
5. *Timing.* July 2027 assumes no appeal, or a fast one. Paid in July 2029 instead, the expected IRR falls to 3.6%.
6. *Collection.* Liability is several, allocated by each defendant's holdings, so each slice of the award is only as good as the particular fund behind it.
7. *Costs.* Counsel, the funder's share, financing \$1mm for six and a half years, and tax all come out of the 2.25x.
8. *Hindsight.* Every input is a 2026 fact. In January 2021 the buyer still faced the March 2023 loss on summary judgment and the plan's indemnity for the participants, so the ex-ante odds were far below 60%.

**How:** The award per unit of excluded face is $261.13/895 = 29.2$ points. The 2,206 days to judgment are 6.044 years:

$$
V = 5 \times \frac{261.13\,(1 + 0.09 \times 6.044)}{895} = 5 \times 0.4505 = \$2.252\text{mm}.
$$

The expected payoff is $0.6 \times 2.252 = 1.351$ on 1.0 paid. The IRR solves $(1 + r)^{6.47} = 1.351$ (bought mid-January 2021, paid 7 July 2027; moving either date by a few weeks changes the result by a few basis points), so $r = 4.8\%$. The break-even probability is $1.0/2.252 = 0.444$. Clearing 12% needs $1.12^{6.47}/2.252 = 0.92$. If the 9% kept running to payment, the payoff would be 47.7 points and the expected multiple 1.43x (5.7%).

**The trap:** Adding the 25 back. The "about 70 cents on face" in §14.8.1 is the court's closing valuation plus the award. But the 25 is a valuation, not cash: the plan paid non-participants about 0.6–2.4% (Chapter 13-B, PB-06), and the exercise tells you to ignore it. Count the 25 and the expected multiple jumps to 2.1x. The second slip is computing damages on the 20 you paid rather than on face. The third is averaging IRRs: $0.6 \times 13.4\% + 0.4 \times (-100\%) = -32\%$ is not the IRR of anything. Quote the IRR of the expected cash flow, and quote the conditional 13.4% beside it.

**If you got this wrong, read:** §14.8.1, Act II (Mags's January 2021 sale) and Act III (the remand award, Kaz's 6.04 years and three-branch tree), then §14.6 on Robertshaw for "the remedy comes before the merits."

**Z.14.5: Fix ROBO**

**Answer:** One spec, 115 words:

> Build `default_rates(events, ratings)`, monthly. For each month-end t, the cohort is every issuer rated at t − 12m; a rating withdrawn later is censored at withdrawal, never a default. Over (t − 12m, t], count each issuer once: `n_hard` (bankruptcy or missed payment, including one after an earlier exchange) and `n_de_only` (a distressed exchange with no hard default in the window). Output one row per t: `asof`, `n_cohort`, `n_hard`, `n_de_only`, `dr_all_mdy` = (`n_hard` + `n_de_only`)/`n_cohort`, `dr_ex_de_mdy` = `n_hard`/`n_cohort`, issuer-count fractions of the cohort over twelve months, not percent, not hazards. Never delete rows: an exchanger stays in the cohort, and its later hard default or second exchange is recorded and counted. Assert `set(de_ids) <= set(cohort_ids)`.

**How:** "Exclude" is the word ROBO misread, so the spec never uses it. It defines the ex-DE rate as a *numerator* choice over an unchanged denominator. Hard defaults after an exchange count as hard defaults, because that is what CDS pays on and what the parole clock of §14.3 exists to catch. Each issuer is counted once per window, so `dr_all_mdy` minus `dr_ex_de_mdy` equals `n_de_only`/`n_cohort` by construction. The units clause blocks the two silent conversions: a twelve-month rate is not a hazard until it goes through $-\ln(1 - r)$, and 0.021 is not 2.1. The source suffix and "issuer-count" answer Hana's and Ines's questions (§14.1, §14.2.2) before anyone has to open a ticket. Withdrawals are censored for the reason in the attendance-register box. The assert tests for the exact failure ROBO produced: if any exchanger has gone missing from the denominator, the run stops.

**The trap:** Deleting the rows. In the denominator it hardly shows: $2.1\%/(1 - 0.037) = 2.18\%$ instead of 2.10%, which is why nobody notices. The damage is in what the deleted issuers would have done next. At the rates of Z.14.1 and the clock of §14.3.2 ($p = 0.25$, $k = 1.2$), issuers already on parole account for about a fifth of a cohort's hard defaults in year two and 27–33% in years three to five. Delete them, and the "benign" ex-DE rate is missing a quarter to a third of its hard defaults, the very issuers about to re-default. The other common slip is naming the columns without their units. ROBO builds the most literal reading of whatever it is given, which is how §14.7.1 got its zero-and-one `regime` column, and a rate column with no units will come back as 2.1 on one refresh and 0.021 on the next.

**If you got this wrong, read:** §14.1 (Hana's forty-one issuers and the "what we knew when" table), §14.2.2 on rates versus hazards and count- versus dollar-weighting, and the Specification for AI Implementation in §14.7 ("What ROBO built from the vague version").

**Z.14.6: Regime detection**

**Answer:** At 90 defaults a year the filter calls the switch **in year 30, the switch year itself**. In 200 simulated histories, each a fixed switch, Poisson default counts and binomial exchange counts, put through `fit_ms2` on the full 40 years, the filtered LME probability first exceeded 0.9 in year 30 in 199 runs and in year 31 in the last one. None crossed before the switch. At 12 defaults a year, the first crossing at or after the switch came in year 30 in 16% of runs, year 31 in 44%, year 32 in 22%, year 33 in 14%, and years 34–37 in the remaining 6%. That is a median of **one year late** (mean 1.5 years), with three years or more in about one history in five. In 6% of the runs the filter also cried wolf, passing 0.9 at least once before year 30. So the small sample buys you **about one to two years** of "it's just noise," and three or more in a bad draw.

**How:** Each year's count is evidence. Its expected log-likelihood ratio in the LME regime is $n$ times a Kullback–Leibler distance:

$$
n\left[0.63\ln\frac{0.63}{0.30} + 0.37\ln\frac{0.37}{0.70}\right] = 0.2315\,n \text{ nats},
$$

which is 20.8 nats a year at 90 defaults and 2.8 at 12. The filter enters year 30 at the fitted switching probability, $1 - \hat P_{00} = 0.022$, a log-odds of $-3.8$, and reading 0.9 needs $+2.2$, a gap of 6 nats. One public-market year covers that gap three times over. At private-credit size it takes about two years of average evidence, and longer after an unlucky draw. This is the umbrella box's seven-of-ten against 105-of-150, played out over time. Two caveats about the full-sample fit. First, its parameters have already read the post-switch years, so its "filtered" path is better than anything you could have known at the time. Second, its $\hat P_{11} = 0.964$, an expected LME life of 28 years, is pinned by Listing 14.4's stationary start rather than by any exit it has seen. Start the recursion in the pre-LME state and $\hat P_{11}$ runs to the $1 - 10^{-6}$ clip. That is §14.7.2's warning about $1/(1 - P_{11})$, in numbers.

**The trap:** The tempting answer is "the same lag at both sizes, because the share is 63% either way." The filter weighs counts, not shares, and a 63% month out of 12 defaults is weak evidence. The second slip is building the history with the listing's `simulate_de_share_series`, which draws its own Markov regime path, so a given seed may switch in year 12 or never. Fix the path at year 30. The third is "fixing" the look-ahead by refitting each year on the data to date and stopping at the first crossing. That *looks* faster (at 12 defaults, 55% of runs cross in year 30 itself), but only because the refit is trigger-happy. Fit a two-state model to data that hold one regime and it finds two anyway: on pre-switch data alone the refit passed 0.9 in 64% of 50 runs at 12 defaults and 60% of 25 runs at 90, with a "high-exchange" share near 0.36 rather than 0.63. A real-time filter needs a guard, either a test of one state against two or a prior that anchors $\rho_1$ to the documented LME share, before its 0.9 means anything.

NOTE (for the editor): §14.7.2 says that "on about 45 annual points the switch date is uncertain by years, worse when each year holds fewer defaults." In this exercise's own setup the date is not uncertain at public-market size: 199 of 200 full-sample fits call it in the switch year. The years appear only at private-credit size (median lag one year, 90th percentile three), or once the binomial model is wrong. With the share overdispersed around each regime's mean (beta-binomial, standard deviation about 0.07), the same filter at 90 defaults a year passes 0.9 before the switch in 19 of 40 histories. With the share drifting from 0.30 to 0.63 over years 25–35, the first crossing falls anywhere from year 29 to year 32 (10th to 90th percentile). I suggest: "the switch date is sharp only if the counts are clean binomial draws around a share that jumps; with private-credit-sized counts, extra-binomial noise or a share that drifts, it is uncertain by years."

**If you got this wrong, read:** §14.7.1: the umbrella box (counts, not shares), the filter's update and prediction steps, and Kaz's paragraph on label switching and priors on $P$. Then §14.7.2's last paragraph on the switch date, and the risk-committee scene for why the desk publishes filtered, not smoothed, numbers.

<!-- STATUS: COMPLETE -->
