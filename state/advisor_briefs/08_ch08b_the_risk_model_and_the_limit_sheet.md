# Advisor Brief — Chapter 8-B: The Risk Model You Run Every Morning: Factors, Idiosyncratic Variance, Jump-to-Default, Stress and the Limit Sheet

**Target file:** `book_src/08_ch08b_the_risk_model_and_the_limit_sheet.md` · **Target length:** 10,000–12,000 words (hard cap 12k) · **Advisor:** Fable, Edition 2 · **Date:** 2026-10-18

Method note: no web research. Dated stress numbers come from the canonical homes (§20.5 March 2020, §10.7 Coda April 2025, §18.9.1 LDI BWIC week, §6.4.4 and §8.7B SVB, §28.0's FRED print of 15 Oct 2026: HY 323 bp, CCC 1,278 bp) and from `state/research/case_carvana_svb_wolfspeed_capital_structure.md` for SVB; anything else is CHECK. Prerequisites box: 4-B (DV01, KRD), 7-B (EWMA, Ledoit–Wolf, PCA, bootstrap), §8.1–8.8, §12.5, §5.5 (LGD Beta), §24.3 ($N^{\text{JTD}}$). Ships `risk_model.py` to `book_src/lib/` via App F; 8-C, Ch 9, 12, 19, 28 import it. Obey the Voice Amendments.

---

## 1. Thesis and the "aha"

**Thesis.** A risk model is two things that must never be folded into each other: a covariance you can defend at 7:30 a.m. (factors, loadings, idiosyncratic variance, all estimated from a panel where most bonds did not trade yesterday) and a **jump layer** you refuse to make Gaussian (issuer-level default with a Beta recovery, charged once). The limit sheet is the risk model's contract with the PM: it says which numbers, at which thresholds, trigger which conversation. Edition 1 has risk *concepts* everywhere and risk *models* at two scales (eleven MAC sectors in §12.5, a 150-line basket in §19.5); nothing in between, nothing backtested, no limits. This chapter is the 2,000-line book's model, its backtest and its limit sheet.

**The aha for the ex-banker.** The risk pack is the desk's 13-week model: a forecast of how much can go wrong before the next re-forecast, judged by its own backtest. And the thing you were best at (the name that can default next quarter) is precisely the thing the Gaussian layer is worst at, which is why the JTD overlay exists and why "Issuer JTD top ten" is the one limit line an ex-RSSG analyst can own in month one.

**Five beats.** (1) Variance adds in quadrature; correlation is shared movement; a 2,000-line book has maybe forty independent bets (§28.2). (2) DTS is the unit (§8.4), so loadings are DTS-scaled and a rating migration moves exposure even when nothing trades. (3) Below 80 the bond stops being a bond (§8.3); the model must switch regimes, not widen a vol. (4) Default is a jump; put it in its own layer with its own distribution and its own limit, and charge it once (Law 6). (5) The model is wrong at a measurable rate; count the exceptions, and never retune it in the drawdown that produced them.

---

## 2. Section outline

**Cold Open: Fourteen-Sigma Tuesday, the Sequel (≤400 words).** 7:31 a.m. Theo's inbox: *LIMIT BREACH, Issuer JTD top-10: Halvorsen (soft), DTS B-rated Industrials (hard), ES 1d 99% (soft)*. The bond gapped from 92 to 78 overnight (the Ch 1 Monday). Kaz: "The model said fourteen sigma." Ines: "Then your model has the wrong sigma. What's the pot, and which line do we cut?" Mags: "A limit is something you breach politely, in writing, before lunch." ROBO, asked to "keep risk under the limit," has pre-drafted an order to sell the entire book at 9:31 and buy it back at 3:59 ("flat overnight, bankrupt by commissions"). Bold question: *what is the number on the risk report supposed to be, and what do you do when it is wrong?*

- **8B.1 What the Model Is For.** Three questions (how much, where, what to do) and one non-question (it is not a return forecast). **Math, Gently:** variance adds in quadrature; correlation as shared movement; with a tiny two-bond number.
- **8B.2 The Factor Taxonomy.** Key-rate DV01s (4-B); rating × sector spread factors in DTS units; a liquidity factor from LCS changes; the Collin-Dufresne–Goldstein–Martin common residual (§8.8) promoted to a named factor; basis factors (CDX–cash, ETF–NAV, futures–index) from §8.6 and 10-B. $r_i=-\sum_k \text{KRD}_{ik}\Delta y_k-\text{DTS}_i\sum_f\beta_{if}f_f+\varepsilon_i$. **Figure 1:** the factor tree with the book's exposures on it.
- **8B.3 Loadings When Nothing Trades.** Dimson sums for stale bonds (§8.5), issuer-level fallbacks, the new-issue rule (Man's recipe from §9.8.1, made explicit), and the one-timestamp snap (3 p.m. futures settle, 3 p.m. CDX, 3 p.m. composite): say which, and make risk and P&L share it.
- **8B.4 Idiosyncratic Variance by Rating and Price Bucket.** Estimated from the residual panel; the sub-80 switch (§8.3: below 80 the bond loads on the issuer's equity, not on spread factors) as a regime, not a vol multiplier. **Math, Gently:** what a lognormal is and why a price near 100 and a price near 40 cannot share a distribution.
- **8B.5 The Jump Layer.** Issuer-level JTD using Ch 5's LGD distributions: $\text{JTD}_i=N_i(P_i-R_i)$ with $R_i\sim\text{Beta}$ conditioned on seniority (§5.5); issuer netting across bonds, loans, CDS and equity puts; never folded into the Gaussian; "charge the jump once" (Law 6: the JTD in the risk pack is the same JTD as in the hazard, §6.8, and in the quote, §18.6). **View From Another Seat:** the dealer desk (JTD per unit of inventory, 18-B), the CLO manager (the CCC bucket and OC test as the limit, §21.4), the insurer (capital charge, not ES), the systematic fund (issuer caps and effective breadth).
- **8B.6 ES on the Mixture.** 1-day and 10-day; the $\sqrt h$ rule fails for jumps; historical vs parametric mixture; report ES and JTD beside any VaR (the book's rule finally gets an engine). **Math, Gently:** VaR is the threshold, ES is the average of the bad days.
- **8B.7 The Stress Library.** Six dated scenarios as factor shocks, each one sentence plus its canonical §: March 2020 (§20.5), the 2022 rates year (§10.7C), the LDI BWIC week of Oct 2022 (§18.9.1), SVB March 2023 (§6.4.4, §8.7B), April 2025 (§10.7 Coda, FRED-verified), the 2026 CCC decompression (Ch 28 §28.0, Box C). Plus the scenario the §8.6 annotation demands: hedge basis widening *with* spreads. Scenarios shock factors, not stories. **Figure 2:** the book's P&L under each scenario, with the JTD layer shown separately.
- **8B.8 The Backtest.** Ex-ante vs realized vol by bucket; exception counts; Kupiec's proportion-of-failures test and Christoffersen's independence test; what a failing backtest licenses (a documented change through Ch 27 §27.9's ladder) and what it does not (retuning in the drawdown, which is look-ahead). **Math, Gently:** counting exceptions as coin flips.
- **8B.9 The Limit Sheet.** DTS by rating × sector; CS01 ladder; KRD DV01; issuer JTD top ten; ES 1d/10d; days-to-liquidate (§28.5); percent of issue outstanding; soft and hard thresholds; the override procedure; the escalation path with names of roles, not people. Limits as a conversation, not a wall. **Figure 3:** the Fourteen-Sigma Tuesday risk report (engagement §5) grown into the limit sheet. A short scene: the risk committee asks "why is this number different from yesterday?" and the answer is a rating migration that re-bucketed forty bonds.
- **8B.10 When to Apply It, and When It Breaks.** $\rho_{y,s}$ changed sign twice since 2021 (§8.2, §8.7): make it a regime input from §12.4, and fix §12.5's hard-coded zero by reference; correlations go to one in the scenarios you built the model for; stale marks understate vol (desmooth, §12.5); the model is only as good as the security master (§27.3) and the corporate-actions feed (App B §B.16); and the rebalance band: hedge less and rebalance less, with the cube-root shape stated and §8.6 (expanded) owning the derivation. Trend Watch (dated, sourced): MarketAxess suspended its monthly volume releases on 30 Jul 2026, the morning ICE announced its acquisition (\$167 a share, equity value about \$6.0bn; MarketAxess Q2-2026 release pp. 4–5, 9), and FINRA's affiliate-principal indicator (voluntary 31 Aug 2026, mandatory 2 Aug 2027; Regulatory Notice 26-16) will suppress the inter-affiliate leg of roughly 5.7% of 2025 secondary prints (SR-FINRA-2026-009 pp. 19–21): both change the inputs to any liquidity factor built from volumes (`trend_part_v_market_structure_2026`).
- **Specification for AI Implementation: `risk_model.py`.** Prose; code to App F and `book_src/lib/`. Schemas: positions (instrument, issuer, notional, price, provenance type, seniority, rating, sector, price bucket); factor-return panel; loadings table; idiosyncratic-variance table by bucket; issuer JTD table (net notional, $P$, Beta parameters for $R$). Functions: `build_loadings` (Dimson, fallbacks, new-issue rule), `factor_cov` (EWMA plus Ledoit–Wolf from `creditstats.py`), `idio_var`, `jtd_overlay`, `es_mixture` (1d, 10d; historical and parametric), `stress` (library of named factor shocks), `backtest_exceptions` (Kupiec, Christoffersen), `limit_sheet` (thresholds, soft/hard, breach list). Guards: condition-number alarm on $\Sigma_F$; refuse a bond with no loading and no fallback; never add JTD variance into the Gaussian; snap timestamps must match across inputs. ROBO's vague version: "keep risk under the limit" (the cold open).
- **Desk Debrief (scene + 5–8 bullets, Laws tagged).** A week later: the breach was real, the model's sigma was wrong because Halvorsen had crossed 80 and the loading had not switched; the JTD line had it right all along. Bullets: "DTS is the unit; a migration moves risk when nothing trades" (Law 3); "Charge the jump once, in its own layer" (Law 6); "A model has an exception rate; count it" (Law 12); "A limit is a conversation with a timestamp" (Law 11); "Below 80, it is not a bond" ; "Risk and P&L share one snap or they share nothing" (Law 9).
- **Exercises (4–6, tagged, with Check:).** Compute the portfolio variance for two bonds with DTS 400 and 900 at $\rho=0.6$; show that the 10-day ES of a book with a 2% one-day JTD probability is not $\sqrt{10}$ times the 1-day; run Kupiec on 7 exceptions in 250 days at 99% (Check: reject at 5%); build the limit sheet for the Halvorsen book of 12-B §12B.9.

---

## 3. Key derivations and formulas

**The covariance.** $\Sigma=B\,\Sigma_F\,B^\top+D$, with $B$ the $n\times K$ loading matrix (KRDs, DTS-scaled factor betas, liquidity and basis betas), $\Sigma_F$ the factor covariance (EWMA with half-life $h$, shrunk toward a structured target by Ledoit–Wolf; 7-B), $D$ diagonal idiosyncratic variance by rating × price bucket. Portfolio variance $w^\top\Sigma w$; marginal contribution $\partial\sigma_p/\partial w_i=(\Sigma w)_i/\sigma_p$; the decomposition into factor and idio pieces is the risk pack's first table.

**DTS-scaled loadings.** For spread factor $f$, $\beta_{if}=\text{DTS}_i\,b_{g(i),f}$ with $b$ estimated per rating × sector cell $g$; a migration changes $g(i)$ and therefore risk with no trade (§8.4, §9.2 back-reference). Dimson: $\hat\beta=\sum_{\ell=-1}^{1}\hat\beta_\ell$ on lagged and led factor returns for stale bonds (§8.5).

**The sub-80 switch.** For $P_i<80$, replace the spread loading by an equity-factor loading $\beta^{E}_{i}$ estimated from the issuer's equity (or sector equity when none), per §8.3's discontinuity; the switch is a regime indicator, not a vol multiplier.

**The jump layer.** Loss over horizon $h$:
$$L=L^{\text{Gauss}}+\sum_i \mathbf 1\{\tau_i\le h\}\,N_i\,(P_i-R_i),\qquad R_i\sim\text{Beta}(a_{s(i)},b_{s(i)}),\quad \mathbb{P}(\tau_i\le h)=1-e^{-\lambda^{\mathbb{P}}_i h}.$$
Say which measure: $\lambda^{\mathbb{P}}$ from §6.8/§11.4, never the CDS-implied $\lambda^{\mathbb{Q}}$ (Law 4). Issuer netting: $N_i$ is the net JTD across bonds, loans, CDS (with $N^{\text{JTD}}=(P-R)/(1-R)$, §24.3) and equity puts.

**ES on the mixture.** $\text{ES}_\alpha=\mathbb{E}[L\mid L\ge \text{VaR}_\alpha]$; for the mixture use historical simulation of the Gaussian layer plus Monte Carlo of the jump layer (7-B's standard-error rule for the number of paths); show that $\text{ES}^{10d}\ne\sqrt{10}\,\text{ES}^{1d}$ once jumps matter, with a one-line reason (jump probability scales with $h$, not $\sqrt h$).

**Kupiec and Christoffersen.** With $x$ exceptions in $n$ days at coverage $p$: $\text{LR}_{\text{POF}}=-2\ln\frac{(1-p)^{n-x}p^{x}}{(1-x/n)^{n-x}(x/n)^{x}}\sim\chi^2_1$; independence tests the exception sequence's transition matrix ($\text{LR}_{\text{ind}}\sim\chi^2_1$); conditional coverage is their sum ($\chi^2_2$). Worked: 7 exceptions in 250 days at $p=0.01$.

**Days-to-liquidate and the percent-of-issue cap.** Import §28.5's LVaR; $\text{DTL}_i=N_i/(\kappa\,\text{ADV}_i)$ with participation $\kappa$; the issue-share cap bounds the forced-seller problem of §16.2 from the desk's side.

**The rebalance band (intuition only; derivation in §8.6 expanded).** Band width $\propto(\text{cost}/\text{variance})^{1/3}$: costly hedges are rebalanced less often; volatile ones more.

---

## 4. Case studies (canonical homes respected)

- **SVB, March 2023** (canonical §6.4.4; hedge lens §8.7B; dossier `case_carvana_svb_wolfspeed_capital_structure`): the scenario in which the rates hedge and the spread hedge lost together; this chapter's lens is "the hedge-basis-with-spreads scenario" and the bank-sub-debt JTD that no Gaussian layer carried. Pull dated prices from the dossier; do not retell the run.
- **April 2025** (canonical §10.7 Coda, FRED-verified): calibrates the spread-factor shock and the CDX–cash basis shock; one sentence plus §.
- **LDI BWIC week, Oct 2022** (canonical §18.9.1): the liquidity factor's defining observation.
- **The 2026 CCC decompression** (Ch 28 §28.0, FRED 15 Oct 2026: HY 323 bp, CCC 1,278 bp): the idiosyncratic-variance-by-price-bucket argument on live data.
- **Fictional:** the Halvorsen breach (cold open), the forty-bond migration (8B.9), the Larkspur Foam retune-in-a-drawdown (one paragraph; the full autopsy belongs to Ch 27 §27.9).

---

## 5. Humor beats with the canon cast

- Kaz: "Let's just assume Gaussian." The chapter is the rebuttal; by 8B.5 Kaz is drawing the Beta by hand and calling it "a Gaussian with opinions."
- ROBO's vague version: "keep risk under the limit" → sell at 9:31, buy at 3:59. Second attempt, "set sensible limits," → ROBO sets every limit to the current exposure plus one dollar, so the desk is in breach by 9:32.
- Mags: "In my day the risk report was a man named Gerry who walked over and asked if you were sure."
- Ines: "The pot is the ES, the odds are the model, and the player who knows more than you is the one who sold you Halvorsen at 78."
- Theo's 13-week model gets a sibling: the 13-day model (days-to-liquidate). The USB stick now has two files.
- The Ad Hoc Group asks to be added to the risk factor list "as a matter of record."
- One "IDO or it didn't happen" (Debrief); counter unchanged.

---

## 6. Cross-references into existing chapters

4-B (DV01, KRD, price–yield), 7-B (EWMA, Ledoit–Wolf, PCA, bootstrap, Monte Carlo standard error), §5.5 (LGD Beta by seniority), §5.10 (ES beside VaR rule: now points here), §6.8 and §11.4 ($\lambda^{\mathbb{P}}$), 6-B (say which measure), §8.1–8.8 (all; §8.3 switch, §8.4 DTS, §8.5 Dimson, §8.6 hedge matrix and its expansion, §8.8 common residual), §9.8 (the optimizer imports this covariance), §12.4–12.5 (regime $\rho$; desmoothing; fix by reference), §16.2 (forced sellers), §18.6 and 18-B (JTD in the quote), §19.5 (basket residual covariance: now a special case), §21.4 (OC test as a limit), §24.3 ($N^{\text{JTD}}$), §27.3 (security master), Ch 27 §27.9 (promotion ladder; no retuning in a drawdown), §28.2 (effective breadth), §28.5 (LVaR, DTL), §28.9 (dashboard: the risk-vs-limits panel is this chapter's output), 8-C (imports `risk_model.py`), App B §B.16 (corporate actions), App D (margin), App E Laws 3, 4, 6, 9, 11, 12.

**Resource Graph (specific items):** Odd Lots, "How the Hottest Hedge Funds on Wall Street Really Manage Risk" (25 Jul 2024); Odd Lots, "The Math That Explains How Multi-Strategy Hedge Funds Make Money" (7 Oct 2024, Dan Morillo); Odd Lots, "Giuseppe Paleologo on Quant Investing at Multi-Strat Hedge Funds" (21 Jun 2025) with `Paleologo_Advanced_Portfolio_Management` on the shelf; Flirting with Models, "Jeff Rosenberg – The Past, Present, and Future of Systematic Fixed Income (S7E19)" (18 Aug 2025); MarketAxess Q2-2026 earnings release (30 Jul 2026); FINRA Regulatory Notice 26-16 (26 Aug 2026); Kupiec (1995) and Christoffersen (1998) by title (verify DOIs before linking).

**Figures (≥3):** `ch08b_factor_tree.png`, `ch08b_stress_library.png` (Gaussian vs JTD layer per scenario), `ch08b_limit_sheet.png` (the risk report grown into the limit sheet).

<!-- STATUS: COMPLETE -->
