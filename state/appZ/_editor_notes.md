# App Z editor notes (chapter-text discrepancies found while solving)

### 05_ch05_credit_probability_distributions

NOTE (for the editor): The "right-skewed survival leg" comes from §5.9.1's Gaussian $\Delta s$, not from the bond. §5.2.4 says a lognormal spread (skew $+1.1$ at $\kappa = 0.35$) gives a survival-world return skew of "about $-1.1$," which positive convexity pushes back on only "a little." I simulated the same leg with lognormal relative spread changes, $\Delta s = s\,(e^{-\kappa^2/2 + \kappa Z} - 1)$, and four million draws. The skew is $-0.93$ at $C^{\text{spr}} = +8$, $-1.13$ at 0 and $-1.35$ at $-8$. The exercise's "show that the survival leg of a non-call bond is right-skewed" therefore holds only under the Gaussian-$\Delta s$ assumption. I suggest "under §5.9.1's Gaussian spread change, show that…", perhaps with a closing clause noting that with §5.2.3's lognormal spreads the leg stays left-skewed.

### 08_ch08_isolating_ido_and_empirical_duration

NOTE (for the editor): §8.2 ("The two-factor derivation") says that with $\ell \approx -19$ "a B bond at 500 bp has $H \approx 0.03$." With the exact $\ell = -19.25$ the figure is $0.0375$ (0.04), and with $\ell = -19$ it is 0.05. Neither rounds to 0.03. The same paragraph says Theo's bond at 620 bp "comes out slightly below zero." The figure is $-0.19$, a 45-contract long, which may be worth stating.

### 09_ch09_factor_investing_in_credit

NOTE (for the editor): the exercise asks which signal the Blume–Stambaugh mechanism "inflates" more. On the chapter's own noise model (Listing 9.7, iid errors), my run of the extension moves bond momentum by −46bp a month (−5.4% a year against +0.05% clean) and ESI by +0.7bp a month. The noise deflates the bond-price signal, as the $-\sigma_u^2$ covariance of §9.9 predicts for a buy-winners sort. Consider "distort" for "inflate", or ask the reader to predict the sign first.

### 10_ch10_trend_and_time_series_momentum

NOTE (for the editor): $p(1-p)\beta^{\text{ce}}$ is the slope from a *simple* regression of $\Delta m_{t+1}$ on $r^{\text{eq}}_t$. In the VAR that §10.5.3 writes down, and that Listing 10.6(a) runs, the own lag $\Delta m_t$ is uncorrelated with $\Delta m_{t+1}$ but correlated with $r^{\text{eq}}_t$. It acts as a suppressor, and the equity coefficient becomes $p(1-p)\beta^{\text{ce}}/(1 - p^2 R^2_{\text{ce}})$, where $R^2_{\text{ce}}$ is the contemporaneous $R^2$ of true credit moves on equity. At the listing's parameters ($R^2_{\text{ce}} = 0.735$), the coefficient is 0.061 at $p = \tfrac12$, not 0.050 (simulation 0.0613), and it peaks at $p \approx 0.66$, not $\tfrac12$. At $p = 0.9$ it is 0.044 against the formula's 0.018. With the low $R^2_{\text{ce}}$ that real bonds show, the formula and the peak at $\tfrac12$ are close enough. The box might add "in a simple regression" so that a reader who checks the listing's coefficients is not surprised.

### 10_ch10_trend_and_time_series_momentum

NOTE (for the editor): The coda (§10.7, cut two) says a lag of more than a quarter of the 1.5-month V is "about ten days". A quarter of 1.5 months is 0.375 months, which is 7.9 trading days or 11.4 calendar days, and this exercise's check says "roughly eight trading days". Changing the coda to "about eight trading days" would make the two agree.

### 10_ch10_trend_and_time_series_momentum

NOTE (for the editor): The coda's fictional run puts the fast 20/120 sleeve "one session from flipping short" at the close on 3 April, with the slow sleeve held long by the carry hurdle. Listing 10.6, run on the chapter's own FRED series (`BAMLH0A0HYM2`, $D = 4$), gives a different picture. After the drift from 2.62% to 3.55%, the tanh crossover went negative on 17 March and stood at −0.74 on 2 April, so it entered the gap already short, at 62% of full risk, not small. The 12-month return rule was still long at the 3 April close (59 bp of 12-month widening against a 74 bp hurdle). It flipped short at the 4 April close (106 bp), and those are the 13 short days in Figure 10.1, 4–30 April. At unit notional it lost 5.6% from 3 April to 14 May. The CDX sleeve is fictional and may differ. Even so, Ines's grade of Theo's slow-sleeve line ("the carry hurdle doing its job") sits uneasily with the chapter's own tape. One sentence saying that the 12-month signal cleared the hurdle a session later and was whipsawed would square them.

### 12_ch12_multi_asset_credit_allocation

NOTE (for the editor): In "The Queue" (§12.7), the grading of Kaz's card says a 90-day $\tau$ "would have been wrong ... by something nearer seven at the technology fund." With requests of about 40% of shares against a 5% gate, $Q/g = 8$. That is both the dollar-weighted mean exit (in quarters) under a stationary line and the number of quarters to drain a line that stops growing, so the text should say "nearer eight" unless the request share was nearer 35%. The HPS figure checks: $9/5 = 1.8$, "a factor of two."

### 13_ch13_codifying_lmt_game_theory

NOTE (for the editor): In §13.3.1's unblending table, the middle row ("first-lien second-out only") builds $K_1 = 934$ from June 2020 holdings ($992 \times 0.74$) but divides by the 2016 face of 1,950, giving 47.9. On the June 2020 face of 1,887, the one the remand court's ratable share uses, the row reads $934/1{,}887 = 49.5$, and the sentence below the table would say "between five and twelve points" rather than "between three and twelve." The other two rows check (44.8 and 57.0).

### 13_ch13_codifying_lmt_game_theory

NOTE (for the editor): The whiteboard's arithmetic puts the guarantee in OpCo's pool at its full \$1,266mm on top of the \$735mm collected upstairs, and "Ways This Blows Up" item (2) says the engine assumes full face against each obligor. Listing 13.1's pari-plus wiring does the opposite: `opco_guar` carries `reduce_by=["fsub_guar"]`, and §13.7 describes it as "double-dip OpCo for the deficiency." A reader who copies `dd_recoveries` gets OpCo 6.35% and Super HoldCo 68.3% at the whiteboard inputs, not 5.0% and 69%. With the note struck the gap is wider (14.0% against 8.8%). Suggest saying in the pari-plus paragraph, or in item (2), that the listing nets and the whiteboard does not.

### 15_ch15_event_driven_mna_and_coc

NOTE (for the editor): After the Listing 15.1 description, §15.2 says "Under these illustrative inputs the 1.85% bond's put comes out at eighteen to nineteen points at signing." The listing as printed reports 15.55 ± 0.02 points for its check-(3) LBO ($M = 1.052$; 14.78 independent), and the constant-350bp check-(1) inputs give 17.82. Neither is eighteen to nineteen. Suggest "about fifteen and a half points (about eighteen at a constant 350bp)".

### 15_ch15_event_driven_mna_and_coc

NOTE (for the editor): The paragraph on the four checks gives the mean-preserving lognormal as an example "with $\sigma = 0.5$", median $e^{-0.125} \approx 88\%$ of a 350bp mean. Readers will take that as check (3)'s setting, but the listing uses $\sigma = 0.35$, whose median is $e^{-0.061} \approx 94\%$ of the mean (329bp, which matches the simulated median). Either change the example to 0.35 or say that the listing uses a smaller $\sigma$.

### 15_ch15_event_driven_mna_and_coc

NOTE (for the editor): "The sign flips with rates" in §15.4.2 says "If rates have fallen, $P^{\text{close}} > G_f$ and the holder is short a digital." On the section's own three-year 4.60% example, a tranche issued at par still has $P^{\text{close}} < G_f$ (100.00 against 100.99) after any rally smaller than about 38bp. The ruler box gets it right ("When rates fall far enough"). Suggest "If rates have fallen far enough (about 40bp on a three-year tranche issued at par)".

### 16_ch16_post_reorg_equities_and_claims

NOTE (for the editor): §16.2.3 says the capital-arrival term $Q_t\dot M_t/M_t^2$ "decays at the speed of the slow money ($\rho$), not the speed of the sellers ($\theta$)", and this exercise says the model's single-exponential undershoot is like Dynkin's. In the model, that term decays at $\theta + \rho$, and the whole discount decays at $\theta + \dot M/M \ge \theta$, so $w_3/w_2 < e^{-\theta\Delta}$ always. At $\theta = 3.42$ and $w_2 = 1.04\%$, the third window can be at most 0.188%, while the data show 0.86% (checked by grid search over $\rho$ and $M_0/M^{*}$). Here slow capital lifts $w_3$ by 7.5% (0.588% against 0.547%), whereas Dynkin's third window is 4.5 times the single-exponential line (0.86% against 0.19%). Fitting Dynkin's three numbers inside this model needs $\theta \le 0.38$ a year, with capital as the *fast* component; one exact fit is $\theta = 0.38$, $\rho \approx 25$, $M_0/M^{*} \approx 0.62$. That is the opposite of the chapter's labeling, and of Ines's "fast decay is the seller, slow decay is the table filling up." Suggest rewording §16.2.3, or adding a second, slower seller compartment to the model.

### 16_ch16_post_reorg_equities_and_claims

NOTE (for the editor): §16.3.3's Desk Myth ("The fee is the smallest of four legs") and the Debrief's fourth sentence ("the fee is its smallest leg") contradict this exercise, where the fee is the *largest* leg and the put is the smallest in absolute value. They also contradict the chapter's own 25%/70%/six-month case. There the fee in shares is about $0.10 \times 0.91 = 9.1\%$ of the raise, against a put of 6.3%, and the reserved slice would beat the fee only if more than about 57% of the offering were reserved. The sentence probably means "the put (the fair fee) is the smallest leg." Separately, the $\Pi^{\text{BP}}$ formula charges the put on all $m$ shares, $-N_{\text{eff}}(K - x)^{+}$. The reserved slice's downside, though, is already in the linear second leg, so the put should be $-(1-a)\,N_{\text{eff}}(K-x)^{+}$. Here that gives a put leg of \$8.4mm, not \$10.5mm, and an all-in of \$96.9mm, not \$94.8mm. Our table follows the formula as printed.

### 16_ch16_post_reorg_equities_and_claims

NOTE (for the editor): §16.5.3 says the dollarized claimant is "short a call on the asset, struck at the petition-date price, and was paid nothing for it." Against a solvent payer that is not quite right: dollarization also hands the claimant a put at the same strike, and at zero rate the at-the-money call and put are both worth \$7,441, so the swap would be fair. It is "paid nothing" because the put was written by an insolvent estate holding the same asset. Suggest adding a clause such as "except a put written by an estate holding the same asset."

### 17_ch17_private_credit_public_private_convergence

NOTE (for the editor): The exercise and §17.4.2 ("it overstates most in exactly the stressed regime") hold for block 3's parameters only in proportional terms: 1.30% at $\zeta=-1$ against 2.57% at $\zeta=+1$. In dollars the overstatement falls, from \$105.4mm to \$43.8mm, because tight-regime supply is \$1,705mm against \$8,091mm loose. Suggest "by a larger fraction" in both places.

### 18_ch18_otc_microstructure_and_avellaneda_stoikov

NOTE (for the editor): the "Random jump sizes" paragraph of §18.6.1 says to "Replace $e^{\gamma qJ}$ with the moment generating function $M_J(\gamma q)$." That is exact inside $\theta(q)$. In (18.7) as printed, though, $e^{\gamma qJ}$ multiplies $(e^{\gamma J} - 1)$ in $r^b$, and $\sinh(\gamma J)$ in $r^{\text{res}}$, and a literal swap there gives $M_J(\gamma q)(M_J(\gamma) - 1) = 3.36$ points, or 3.29 if $e^{\gamma\bar J}$ is kept in the second factor, against the correct $M_J(\gamma(q+1)) - M_J(\gamma q)$ of 3.78 (inputs above, $\text{Beta}(2,3)$ recovery). Suggest adding "in $\theta(q)$", or writing the bid's jump term in the difference form.

### 18_ch18_otc_microstructure_and_avellaneda_stoikov

NOTE (for the editor): in §18.9.1 Ines says, "Send the list to three desks and you get three envelopes and a fat $e_n$-sized discount from each of them." But $e_n$ is *smaller* at three ($0.85\sigma_\varepsilon$) than at thirty ($2.04\sigma_\varepsilon$). Each bidder's equilibrium discount to its own read is also smaller at three ($1.51\sigma_\varepsilon$ against $2.16\sigma_\varepsilon$). What is fatter at three is the seller's expected shortfall from value, $0.66\sigma_\varepsilon$ against $0.12\sigma_\varepsilon$: the best of three reads sits lower, and the strategic shade is wider. Suggest "a fat discount from the winner" in place of "a fat $e_n$-sized discount from each of them."

### 19_ch19_portfolio_trading_pricing_engines

NOTE (for the editor): §19.7.2 (Two Tapes) says that at $s=2$ "the eviction loop exhausts its $\alpha$ budget, 15% of the market value handed back", and the §19.6.2 annotation says the loop "hit the $\alpha$ budget before reaching $\kappa^\star$". With Listing 19.5's defaults it is $k_{\max}$ that binds. The loop stops at 10 lines and 14.4% of MV (315.7bp at $s=2$, 286.9bp at $s=1.85$), and $\alpha$ binds only if $k_{\max}$ is lifted (11 lines, 15.0%).

### 19_ch19_portfolio_trading_pricing_engines

NOTE (for the editor): The exercise says the variance version "distorts $\mathbf{h}^\star$", and §19.5's Ways This Blows Up (3) says it "over-hedges it". In Listing 19.3's factor model $\mathbf{h}^\star$ does not depend on `sig_idio`, so the hedge is unchanged: \$79.8mm of ETF and \$157.1mm of CDX in both versions. An over-hedge (+\$86.7mm, to \$109.0mm of ETF and \$214.6mm of CDX) appears only if the bump also scales L117's factor loadings, and a different hedge appears only through a changed eviction (multipliers of 9× or less). Suggest rewording to "distorts the eviction ranking and, if applied to the whole return series, $\mathbf{h}^\star$".

### 19_ch19_portfolio_trading_pricing_engines

NOTE (for the editor): The exercise asks for "a 150-line IG program" with "$\Sigma$ from §19.5", but §19.5 builds $\Sigma$ only for the HY cold-open basket, and the exercise gives no $c^{\text{retry}}$. The numbers above use `b0` at $T=1$, and an IG program would come out lower. Suggest saying "use `b0` as the program" and giving a retry cost, such as 5bp per dollar.

### 20_ch20_credit_etf_creation_redemption_arb

NOTE (for the editor): The display just above (20.3) reads $\Delta \ln \text{NAV}_t = \Delta \ln \tilde M_t - \Delta \ln(1 - \bar c_t)$. Since $\text{NAV}_t = \tilde M_t(1 - \bar c_t)$, the sign should be $+\Delta\ln(1-\bar c_t)$. With the printed sign, widening spreads would *raise* NAV returns. The last paragraph of §20.2.2 calls "$-\Delta \ln(1 - \bar c_t)$" a "negative drag", which is true only of $+\Delta\ln(1-\bar c_t)$. The economics is right and the sign is wrong in both places. (20.3) itself is unaffected, because it assumes a constant $\bar c$.

### 20_ch20_credit_etf_creation_redemption_arb

NOTE (for the editor): §20.4.3 says "the fractional baskets in the data are the corner solutions of this problem." Listing 20.1's own Block 4 prints `basket coverage 92%` at the $w \ge 0$ corners, and our scaled runs give about 80% at $\chi = 0$. The 10–35% in the data needs the per-line cost of this exercise as well. Suggest "partly the corner solutions of this problem, and partly a fixed cost per line (Exercise 4)."

### 22_ch22_market_structure_regulation_trends

NOTE (for the editor): In the §22.2.3 Poker Table, Ines says "nobody at this table will ever vote to *lower* the cap." Under (22.7) with $\alpha$ fixed, lowering the cap *helps* her \$15mm block: a \$3mm cap gives $mC = \$7.5$mm and a subsidy of $0.5 \times 7.5 \times 0.875 = 3.28$bp, against 1.09bp at \$5mm. Raising the cap is what hurts it: at \$10mm, $mC = \$25$mm and the block pays a 4.38bp tax. "Raise" or "lift" looks like the intended word.

### 23_ch23_cross_asset_convexity_and_vol_surface

NOTE (for the editor): §23.1 says that at $V = 75$ the overlay "is selling hard into a stock whose only news is arithmetic." With $\sigma_V$ held constant, as both the scene and this exercise stipulate, it never sells a share. Dollar vol per share, $\sigma_V V N(d_1)$, falls from \$37.5 to \$13.1, so shares per \$100 of risk capital rise from 0.267 to 0.763. What falls is the *weight*, from 21.7% to 8.5%, which leaves it 13 points underweight a constant-weight book. It sells shares only if $\sigma_V$ itself rises. Suggest "trims its weight" or "runs underweight" in the scene, or let asset vol rise there. The table's figures (46%, 73%, 117%; $E$ = 82.1, 32.6, 11.2) and Figure 23.2's 626bp all check.

### 23_ch23_cross_asset_convexity_and_vol_surface

NOTE (for the editor): The Wolfspeed half cannot be built as *series* from what the book cites. The research dossier (`case_carvana_svb_wolfspeed_capital_structure.md` §3.3) records no TRACE series, no CDS and no option surface. The only datable convert points are "near 60" around 28 March 2025 (secondary, tagged CHECK) and 26% of principal on 29 June (10-K). The same secondary source gives the stock at \$2.70 on that day, against the chapter's \$2.59. The solution therefore gives the method and the datable points, and labels its $\sigma_E$ and recovery inputs as assumptions.

### 25_ch25_nlp_pacer_and_covenant_scraping

NOTE (for the editor): §25.7.3 says, below the Rule 2019 table, that "only three of the seven rows move a term-loan recovery." By the table's own rows, four do: Docs. 69, 75, 389 and 1116, the two lender groups. Three do not: 273, 289 and 311, the utilities and the equity group. Suggest "four of the seven rows" or "three of the seven rows do not."

### 26_ch26_ai_agents_and_llms_on_the_credit_desk

NOTE (for the editor): The Full Derivation in §26.6 says "Let the harness retry a rejected step up to $m$ times". Its formula $a_R(1 - r^m)/(1 - r)$, and every number after it, treat $m$ as the total number of attempts: $m = 1$ gives coverage 0.83, the first-try acceptance rate, and §26.12 says "going from one try to three". Read literally, "retry up to $m$ times" means $m + 1$ attempts, and Exercise 2's $m = 2$ would then give 0.948 and 0.974 instead of the stated 0.953 and 0.944. Suggest "Let the harness make up to $m$ attempts at a step, retrying after each rejection."

### 27_ch27_system_architecture_and_asics

NOTE (for the editor): The exercise says "rerun block 3 with $c_s^2 = 1$." Block 3 (Listing 27.3) hard-codes the $c_s^2 = 4$ answers, so with `CS2 = 1.0` it stops at its first assert, `abs(ew - 233.33) < 0.01`, because the mean wait is now 93.3 ms; the p99-sojourn assert (1,000 to 2,400 ms) would fail as well, at about 610 ms. Suggest adding "and update the asserts," or readers will think they broke the listing.

### 27_ch27_system_architecture_and_asics

NOTE (for the editor): §27.7.2 says that to first order $\text{ARL}_1 \approx \ln(\text{ARL}_0)/\mathcal{K}$. As an asymptote that is right, but at the chapter's own example ($\delta = 1$, $c = 5$, $\text{ARL}_0 = 938$) it gives 13.7 fills against the 10.3 quoted in the same paragraph, and at this exercise's $\delta = 0.75$ it gives 29.7 against Siegmund's 21.6. The next-order form $\big(\ln(\mathcal{K}\,\text{ARL}_0) - 1\big)/\mathcal{K}$ gives 10.3 and 21.6. Suggest using it, or adding "overstates the delay by about a third at these settings."

### 28_ch28_pm_playbook

NOTE (for the editor): "a Beta recovery of mean 0.6" literally means 60% recovery (mean loss 0.4). The bond's base case and Listing 28.3's `kelly_random_loss(0.045, 0.031, 3.0, 2.0, 1.00)` both use a Beta *loss* of mean 0.6 (recovery 40%). The exercise also gives no shape, and the answer depends on it: at these inputs every mean-0.6 Beta with $b \ge 2$ returns the boundary (1.00) and $b < 2$ returns less ($\text{Beta}(1.5, 1)$: 0.95). The literal reading, with $\text{Beta}(2, 3)$, also gives 1.00. Suggest "a Beta(3, 2) loss of mean 0.6, as in Listing 28.3".
