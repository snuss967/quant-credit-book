# Advisor Brief: Chapter 11, Defensive Systematic High Yield

*Fable advisor dissection for the writer. Edition 1. Research date: 17 October 2026. Everything marked CHECK was not confirmed against a primary source in this session; everything with a URL was fetched or confirmed this session. All page citations are PDF page indices from `tools/pdf_search.py`.*

---

## 1. Thesis and the "aha" for an ex-PJT-RSSG reader

**Thesis.** High yield is the asset class where the payoff is a put you sold: upside capped near par plus carry, downside a jump to recovery. Every HY manager knows this, and the industry's answer for twenty years has been to run a beta of 0.9 and call it "defense." BlackRock's eVestment study (2005–2025) shows the average manager captured 89.56% of down months and 92.24% of up months: that is not skill, it is a dimmer switch (BlackRock p.3). The systematic answer is to *buy the asymmetry back at the issuer level*: rank thousands of issuers daily by a probability of default built from balance sheets, equity and bond prices, exclude the worst tail, tilt toward low-risk (short, higher-rated) bonds on a DTS-neutral basis, and keep the beta at 1.0 so the rebound is not forfeited. The chapter's math is the arithmetic of capture ratios, the conversion of distance-to-default into a calibrated PD, the hazard-model evolution from Altman (1968) to gradient boosting, the power-curve validation of a "77% of defaults identified within 24 months" claim, and the capacity economics that decide whether any of it scales.

**The aha for the RSSG reader.** You already *are* a default-prediction model. The 13-week cash flow, the liquidity runway, the springing covenant math, the "will the sponsor fund the equity cure" judgment: those are the covariates. What you lacked was *breadth*: you covered 8 names a year with a 300-page memo each; the systematic desk covers 2,000 issuers every night with a 20-line hazard function. The surprising part is which covariates win. Shumway (2001) and Campbell, Hilscher and Szilagyi (2008) found that market variables (excess equity return, idiosyncratic equity volatility, relative size) dominate the accounting ratios RSSG lives by, and Alanis, Chava and Shah (2022) find the same with modern ML: once distance-to-default, accounting and market variables are in, "textual features derived from corporate filings do not improve performance materially" (arXiv:2212.12051). Your edge is not the memo; it is knowing (a) which *label* counts as default in the LMT era (a distressed exchange is a default that files its own press release as "liability management"), (b) which structural features (priming capacity, uptier risk, drop-down baskets) are missing from every vendor PD, and (c) when the model's "avoid" signal is really a CLO CCC-bucket forced seller you should be *buying from*.

**The second aha: defense that is not a beta tilt.** Downside capture below 100% with upside capture at 100% requires *convexity* in the active return, which can only come from security selection (avoid the jump) or regime-aware exposure (add risk when spreads overshoot fundamentals). A beta tilt gives you symmetric capture by construction; that is the Achilles' heel BlackRock diagnoses in both average and top-quartile managers (p.2, p.5).

---

## 2. Section outline (7,000–10,000 words)

**Cold open (≤400 words).** Thursday, 15 October 2026, 4:05 p.m. The ICE BofA HY index OAS closes at 323bp; the CCC & lower index closes at 1,278bp (FRED BAMLH0A0HYM2, BAMLH0A3HYC). Ines: "What's the pot, Theo? The index says calm. The CCC tier says 2020. Who at this table knows more than you?" Theo opens the 13-week model on the USB stick. Kaz asks whether "selective default" is selective "like a university." Mags: "Back in my day CCCs did minus 30.6% in 2000 and plus 50.8% in 2003, and nobody called either one a regime." Ends on the question: *How do you avoid the defaults without missing the rebounds?* Then "By the end of this chapter you will be able to..." (build and validate a PD model, compute capture ratios and diagnose a beta tilt, construct a DTS-neutral low-risk tilt, size the CCC bucket by expected loss, and estimate capacity).

**11.1 The Asymmetry: why HY needs defense at all.** Desk framing (Ines: short put, "you cannot win a pot you do not play"). Derivation: HY excess return as a mixture (survive: carry minus spread move; default: jump to recovery), closed-form mean, variance and skew; show skew of a Bernoulli jump is $-(1-2p)/\sqrt{p(1-p)}$, so at $p=5\%$ the default component alone has skew $\approx -4.1$. Source Extraction: Man 2022 p.26 (asymmetry), Moyer p.25 Table 1-2 (CCC 1999–2003). Case anchor: CCC index 2000 (−30.6%) and 2003 (+50.8%). Resource graph.

**11.2 The Average Manager's Dimmer Switch: capture ratios and the beta-tilt diagnosis.** Desk framing (BlackRock's eVestment numbers). Derivation: capture ratios in terms of $\alpha$ and $\beta$; asymmetric-beta regression $r_p=\alpha+\beta^+ r_b^+ + \beta^- r_b^- + \epsilon$; show a pure beta tilt gives $U=D=\beta$; "good defense" is $\beta^-<\beta^+$. Regime clustering (BlackRock's four monthly regimes, p.4). AI spec: `capture_ratios()` and the asymmetric regression with a built-in identity check. Source Extraction: BlackRock p.3, p.4, p.5. **Trend Watch #1: the 2022–2025 whipsaws** (2022 −11%+, 2023 +13%+, Q1 2024 +0.35% then −0.37% for the rest of 2024, April 2025 −3.83% round trip in ten weeks). Case study 1 (2022–2023). Resource graph.

**11.3 Default Avoidance I: the structural PD.** Desk framing (Blackstone/DCI: "computationally derived default probabilities rather than sluggish rating agency downgrades," Blackstone p.1). Derivation: Merton equity-as-call, the two-equation system for $(V,\sigma_V)$, distance-to-default under $\mathbb P$ (drift $\mu$) vs $d_2$ under $\mathbb Q$ (drift $r$), KMV default point $F = \text{STD} + \tfrac12\text{LTD}$, empirical DD→PD mapping (Bohn–Stein p.138, p.161–163). Where it breaks for HY: sponsor-owned issuers with no listed equity (Man 2022 p.35), LMT-created liabilities missing from the default point, negative book equity. AI spec: `distance_to_default()` fixed-point solver with a round-trip sanity check. Source Extraction: Bohn–Stein p.138, p.163; Blackstone p.1. Resource graph.

**11.4 Default Avoidance II: hazard models, dynamic logit and gradient boosting.** Desk framing (Theo's memo covariates vs Shumway's three market variables). Derivation: Altman Z (Moyer p.183, with the units trap), Shumway's firm-month hazard $h_i(t)=1/(1+e^{-x_i'\beta})$ and why one-observation-per-firm logits are inconsistent (Bohn–Stein p.236), CHS covariates, prior-probability recalibration, issuer-clustered standard errors. The LMT-era label problem (distressed exchange = default; Moody's: ~65% of 2025 defaults were distressed exchanges). ML: Alanis–Chava–Shah AUC table (DD-only trees 0.83; XGBoost 0.92 with accounting and market variables). Ways This Blows Up: paired samples, look-ahead on filing dates, survivorship via exchanges, 47 bonds of one issuer. AI spec: panel builder, purged issuer-grouped CV (link Ch 7), calibrated PD. Source Extraction: Bohn–Stein p.226, p.236, p.247; Moyer p.183. Resource graph.

**11.5 Validation: power curves and what "77% within 24 months" means.** Desk framing (how to read a vendor's claim). Derivation: CAP and ROC, AUC as $\Pr(\text{score}_D>\text{score}_{ND})$ (Mann–Whitney), $AR=\frac{2\int_0^1 Y(x)dx-1}{1-f}$ (Bohn–Stein p.409), hit rate at a given exclusion rate, the base-rate trap (a 20% exclusion that catches 77% of defaults in a 3% default-rate universe still mislabels ~19% of the index). AI spec: `cap_curve`, `auc`, `accuracy_ratio` with the identity check $AR\approx 2\,\text{AUC}-1$. **Trend Watch #2: the default regime 2024–2026** (S&P 5.1% US spec-grade Dec 2024 CHECK; Moody's forward 1y PD 3.2% Q1 2026; Fitch 2026 forecasts HY 2.5–3%, loans 4.5–5%; private credit 6% April 2026; distressed exchanges 65–68% of defaults). Source Extraction: BlackRock p.6; Bohn–Stein p.410. Resource graph.

**11.6 The CCC Problem.** Desk framing (Mags: "CCC is where the defaults live and where the rallies live, which is the same sentence"). Derivation: tier economics $\mathbb E[r^{xs}_{\text{tier}}]\approx s - \lambda^{\mathbb P}L$ with the S&P one-year CCC→D rate of 31.58% (1980–2002, Schmid p.28) and Moody's recession recoveries of 27.85% (Schmid p.103); CCC rating stickiness (55.82% stay CCC); CLO 7.5% CCC buckets as forced sellers (link Ch 21); why CCC drives dispersion (Loomis: CCC ≈ 25% of index OAS at YE2024); Bolder's Basel point that high-PD risk is idiosyncratic, i.e. diversifiable with breadth (p.324). Docket Diary: LMEs and re-default hazards (Moody's 1,173-borrower study: >70% of eventual hard defaults within two years). Case study 3 (the 2026 CCC decompression). Source Extraction: Schmid p.28; Moyer p.44; Bolder p.324. Resource graph.

**11.7 Quality and Low-Risk Tilts.** Desk framing (Kaz: "the low-vol anomaly is just leverage aversion; also I have never read a credit agreement"). Derivation: Houweling–van Zundert low-risk (short maturity, high rating), Frazzini–Pedersen BAB in credit, the DTS-neutral long-only implementation, Dynkin's maturity result (IR declines with maturity, p.454–457), spread/DTS Sharpe argument via Ben Dor's Merton DTS (p.104–106), Paleologo's warning that low-vol sizing amplifies forecast error (p.99). Combining with equity momentum in credit (EMC): Dynkin p.609 (HY Q5–Q1 15.9%/yr, IR 1.74) and p.739 (DTS-matched legs make EMC and ESP both work in drawdowns). AI spec: `defensive_portfolio()` with DTS-neutrality check. Source Extraction: Dynkin p.59, p.95, p.609, p.739; Man 2022 p.26. Resource graph.

**11.8 Defense Without Sacrificing Offense: regime-aware exposure.** Desk framing (BlackRock p.6: "it is not always prudent to be looking for safety"; Blackstone p.1: contrarian rebalancing when spreads widen without fundamental deterioration). Derivation: spread-conditioned transition matrices (Dynkin p.384: downgrade multiplier equal to spread/long-run spread, mean reversion in 2–3 years), the PD-vs-spread divergence signal $z_i = \ln(s_i/\hat s_i(\text{PD}_i,L_i))$, and a risk budget $\text{DTS}_{\text{target}}(z)$ that rises when spreads exceed model spreads. Case study 2 (April 2025: spreads 259→461bp while forward PDs barely moved; full recovery by 12 May 2025). Ways This Blows Up: "cheap because it is about to be primed" (link Ch 13 PRS). AI spec: regime-conditioned DTS budget with a no-leverage guard. Resource graph.

**11.9 Capacity of Systematic HY.** Desk framing (Theo: "if this works, why isn't it \$1 trillion?"). Derivation: square-root impact capacity formula; Dynkin's fallen-angel capacity table (Sharpe 1.14→0.95 from \$125mn to \$2bn, p.209); Man's HY transaction-cost curves by trade size (p.22); electronification (Man 2023 p.3: >90% of Man Numeric order flow electronic by May 2023); sizes in the wild (Blackstone BCBS >\$40bn across IG/HY/EM; HYDB \$1.52bn). **Optional Trend Watch #3: HY e-trading and portfolio trading 2019–2026.** Source Extraction: Dynkin p.209; Man 2023 p.3. Resource graph.

**11.10 Desk Debrief, The Spec You Hand the Robot, Exercises.**

---

## 3. Derivation skeletons

### 3.1 The mixture return and its skew ($\mathbb P$)

One-period excess return of a bond with carry $c$, spread duration $D^{\text{spr}}$, spread change $\Delta s$, default indicator $\mathbb 1_{\tau\le h}$ with $\mathbb P$-probability $p$, price $P_0$ and recovery $R$:

$$r = (1-\mathbb 1_{\tau\le h})\,(c - D^{\text{spr}}\Delta s) + \mathbb 1_{\tau\le h}\,\frac{R-P_0}{P_0}.$$

With $L_P \equiv (P_0-R)/P_0$ and the surviving component having mean $m$ and variance $v$:

$$\mathbb E[r] = (1-p)m - pL_P,\qquad \text{Var}[r] = (1-p)v + p(1-p)(m+L_P)^2,$$

$$\text{Skew of the jump component} = -\frac{1-2p}{\sqrt{p(1-p)}}\;\;(\approx -4.1 \text{ at } p=0.05,\; -2.1 \text{ at } p=0.20).$$

The credit-triangle approximation $\mathbb E[r^{xs}] \approx s - \lambda^{\mathbb P}L$ follows for small $p$ with $c\approx s$. **Error-prone spots:** mixing $\lambda^{\mathbb Q}$ (from CDS) into a $\mathbb P$ expected-return formula; using the 40% CDS recovery convention as a $\mathbb P$ recovery (Moody's recession mean 27.85%, Schmid p.103); forgetting that $L_P$ is measured from *price*, not par, so a 60-dollar CCC bond has far less jump loss than its spread implies.

### 3.2 Capture ratios and the beta-tilt identity

Up months $\mathcal U=\{t: r_{b,t}>0\}$, down months $\mathcal D$. Arithmetic capture (eVestment uses geometric annualized means; the algebra is the same to first order):

$$U = \frac{\bar r_p^{\,\mathcal U}}{\bar r_b^{\,\mathcal U}},\qquad D = \frac{\bar r_p^{\,\mathcal D}}{\bar r_b^{\,\mathcal D}}.$$

If $r_{p,t} = \alpha + \beta r_{b,t} + \epsilon_t$ with $\epsilon$ orthogonal to the regime, then

$$U \approx \beta + \frac{\alpha}{\bar r_b^{\,\mathcal U}},\qquad D \approx \beta + \frac{\alpha}{\bar r_b^{\,\mathcal D}},\qquad U - D \approx \alpha\left(\frac{1}{\bar r_b^{\,\mathcal U}} - \frac{1}{\bar r_b^{\,\mathcal D}}\right) > 0 \text{ iff } \alpha>0.$$

A pure beta tilt ($\alpha=0$) gives $U=D=\beta<1$: downside "protection" paid for one-for-one with upside. BlackRock's average manager ($U=92.24\%$, $D=89.56\%$) is consistent with $\beta\approx 0.9$ and a small positive $\alpha$ *(illustrative decomposition; the paper reports only the capture ratios)*. Convex defense is the asymmetric-beta model

$$r_{p,t} = \alpha + \beta^+ \max(r_{b,t},0) + \beta^-\min(r_{b,t},0) + \epsilon_t,$$

where "good defense" means $\beta^- < \beta^+$ (positive convexity, Henriksson–Merton flavour). **Error-prone spots:** computing capture on total returns when the mandate is excess-return; regime defined on the benchmark, never on the portfolio; small-sample $\bar r_b^{\mathcal D}$ near zero blows up $D$ (require $|\bar r_b^{\mathcal D}|$ above a floor). Measure: all $\mathbb P$, realized.

### 3.3 Distance-to-default ($\mathbb P$ for PD, $\mathbb Q$ for pricing)

Merton equity as a call on assets with face $F$ at $T$:

$$E = V N(d_1) - F e^{-rT} N(d_2),\qquad d_{1,2} = \frac{\ln(V/F) + (r \pm \tfrac12\sigma_V^2)T}{\sigma_V\sqrt T},$$

$$\sigma_E E = N(d_1)\,\sigma_V V \quad(\text{Itô: } dE = \partial_V E\, dV + \dots).$$

Solve the two equations for $(V,\sigma_V)$ by fixed-point iteration (or the KMV time-series iteration). Physical distance-to-default uses the *physical* drift $\mu$:

$$\text{DD}_T = \frac{\ln(V/F) + (\mu - \tfrac12\sigma_V^2)T}{\sigma_V\sqrt T},\qquad \text{PD}^{\mathbb P} = g(\text{DD}) \neq N(-\text{DD}),$$

with $g$ an empirical monotone map (Bohn–Stein p.161–163: median default frequency per half-sigma DD cohort, fit with a Weibull or polynomial, cap PD near 20–40% for DD < 0.5, need ≥400 and ideally ≥1,000 defaults). Default point for a coupon-paying firm: $F = \text{STD} + \tfrac12\text{LTD}$ (Vasicek–Kealhofer convention). **Error-prone spots:** $N(-\text{DD})$ gives PD $\approx 0$ for most public firms because most have DD > 4 (Bohn–Stein p.138: "a DD of 4 converts into an EDF of almost 1 percent" under the empirical map); unannualized $\sigma_E$; equity vol used as asset vol; sponsor-owned HY issuers have no $E$ (fall back to bond-implied or accounting-only PD and *flag the model regime in the feature set*); an uptier or drop-down changes $F$ for the bond you hold without changing firm-level DD, which is exactly the Ch 13 Priming Risk Score's job.

### 3.4 Dynamic logit hazard, calibration and clustering ($\mathbb P$)

Firm-month panel, covariates lagged by filing availability:

$$h_i(t\mid x_{i,t-\ell}) = \frac{1}{1+\exp\!\big(-(\alpha_0 + \beta' x_{i,t-\ell} + \gamma \ln t)\big)},$$

estimated as a logit on firm-months (Shumway's equivalence to a discrete-time hazard, Bohn–Stein p.237). CHS-style covariates: $\text{NIMTAAVG}$, $\text{TLMTA}$, $\text{EXRETAVG}$, $\text{SIGMA}$, $\text{RSIZE}$, $\text{CASHMTA}$, $\text{MB}$, $\text{PRICE}$ (Campbell, Hilscher and Szilagyi 2008). Add the RSSG covariate: liquidity runway in weeks (Theo's 13-week model reborn). Prior-shift recalibration from sample default rate $\pi_s$ to population $\pi$:

$$\text{logit}\,\hat p^{\text{pop}} = \text{logit}\,\hat p^{\text{s}} + \ln\frac{\pi(1-\pi_s)}{\pi_s(1-\pi)}.$$

Test statistics: divide logit chi-squares by average firm-months per firm (Shumway's adjustment, Bohn–Stein p.237), or cluster by issuer. **Error-prone spots:** paired samples (Bohn–Stein p.226); accounting data dated at fiscal period end instead of filing date (look-ahead); treating a distressed exchange or LME as survival (Moody's: ~65% of 2025 defaults were distressed exchanges, so the "no" label is contaminated); 47 bonds per issuer (one issuer is one observation); overlapping 12-month horizons inflate significance; calibrating on 2010–2019 (benign) and deploying into 2026.

### 3.5 Power curves ($\mathbb P$, realized)

For score cutoff $k$, CAP plots the share of defaults with score worse than $k$ against the share of *all* firms worse than $k$; ROC uses non-defaulters on the x-axis. With defaults $d$, non-defaulters $n$, $f=d/(n+d)$:

$$\text{AUC} = \Pr(\text{score}_D > \text{score}_{ND}) \;(\text{Mann–Whitney}),\qquad AR = \frac{2\int_0^1 Y(x)\,dx - 1}{1-f} \approx 2\,\text{AUC}-1 \text{ for small } f.$$

Hit rate at exclusion rate $q$: $\text{HR}(q) = Y_{\text{CAP}}(q)$. The "77% of defaulted bonds identified within 24 months" (BlackRock p.6) is a point on a CAP curve whose x-coordinate (what fraction of the index was flagged) is not reported; the writer must say so. **Error-prone spots:** AUC on a universe with duplicate bonds per issuer; mixing horizons (12-month PD, 24-month hit window); comparing ARs across samples with different base rates (Bohn–Stein p.426).

### 3.6 Low-risk tilt, DTS-neutral

Betting-against-beta in credit (Frazzini and Pedersen 2014), with risk measured by DTS:

$$r^{\text{BAB}}_t = \frac{\text{DTS}_{\text{mkt}}}{\text{DTS}_L}\,r^{xs}_{L,t} - \frac{\text{DTS}_{\text{mkt}}}{\text{DTS}_H}\,r^{xs}_{H,t}.$$

Long-only HY implementation: weights $w$ solve $\max_w\, w'\hat\mu$ s.t. $w'\text{DTS} = \text{DTS}_{\text{bench}}$, $w\ge0$, issuer and sector caps, turnover budget, where $\hat\mu_i = s_i - \hat\lambda_i L_i$ (spread net of model expected loss). Why it works, in one line from Ben Dor's Merton DTS (p.104–106): spread volatility is near-linear in spread, so per-unit-of-risk compensation is $\frac{s_i-\lambda_iL_i}{k\,s_i\,D_i}$, which falls as $\lambda_i L_i/s_i$ rises, and empirically $\lambda L/s$ rises steeply into CCC (S&P 1980–2002: CCC→D 31.58% vs B→D 6.95%, a 4.5× jump in default rate against a 2–3× jump in spread). Dynkin's maturity result (p.454–457): IR declines with maturity even though the spread curve is upward sloping. **Error-prone spots:** market-value-neutral instead of DTS-neutral (the tilt becomes a short-beta bet and you are back to the dimmer switch); Paleologo p.99: mean-variance sizing on low-vol names multiplies forecast error; low-risk crowding at the short end of BB in 2024–2026 when the index is 62% BB.

### 3.7 Capacity

Square-root impact with annual turnover $\text{TO}$ and participation in HY average daily volume $V_{\text{ADV}}$:

$$\alpha_{\text{net}}(C) = \alpha_0 - \kappa\,\text{TO}\sqrt{\frac{C}{V_{\text{ADV}}\cdot H}},\qquad C^\* = V_{\text{ADV}} H\left(\frac{\alpha_0-\alpha_{\min}}{\kappa\,\text{TO}}\right)^2,$$

with $H$ the trading horizon in days. Default avoidance is an *exclusion* strategy with low turnover (high capacity); the low-risk tilt sits in the most liquid part of HY (high capacity); the CCC-reversal and fallen-angel buying is where capacity binds (Dynkin p.209). **Error-prone spots:** using index turnover rather than signal turnover; ignoring that $V_{\text{ADV}}$ collapses exactly when the defensive signal fires (Ben Dor p.177: liquidity only prices in HY spreads during stress).

---

## 4. Code spec: `defensive_hy_engine` (reference implementation)

**What it computes (numpy/scipy/pandas only, `rng = np.random.default_rng(11)`):**

1. `simulate_hy_universe(n_issuers=600, n_months=120)`: latent asset values follow GBM with a common factor and issuer jumps; liabilities $F_i$; default when $V<F$ at horizon; 10% of defaults are relabelled "distressed exchange" with a flag so the writer can show the label-contamination effect; spreads $s_i = a + b\,g(\text{DD}_i) + \text{noise}$; ratings tiers assigned by spread quantile; bonds get maturity and $D^{\text{spr}}$. Returns a tidy `DataFrame` with schema `issuer_id, month, E, sigma_E, F, r, T, DD_true, spread, dspr, tier, default_12m, de_flag`.
2. `merton_solve(E, sigma_E, F, r, T)`: fixed-point solve for $(V,\sigma_V)$; `distance_to_default(V, sigma_V, F, mu, T)`. **Sanity check:** generate $(E,\sigma_E)$ from known $(V,\sigma_V)$ and recover them to `1e-6` relative error; assert $\text{PD}^{\mathbb P}$ from the empirical map is monotone decreasing in DD.
3. `fit_hazard_logit(panel, features, lag=3)`: firm-month logit with issuer-clustered standard errors and prior-shift calibration; `purged_group_cv(panel, n_splits=5, embargo=12)` groups by issuer and purges overlapping label windows (link Ch 7). **Sanity check:** on the synthetic panel the fitted sign on `DD` is negative and out-of-sample AUC exceeds 0.75; a deliberately look-ahead version (lag=0 on the realized default-month feature) gets AUC near 1.0, printed as a warning example.
4. `cap_curve(score, default)`, `auc(score, default)`, `accuracy_ratio(score, default)`: AUC via rank statistic. **Sanity check:** `abs(accuracy_ratio - (2*auc-1)*(1/(1-f)) ...)` consistent with the exact formula; perfect ranking gives AR=1; random scores give AR within $\pm 0.05$ of 0 over 20 seeds.
5. `capture_ratios(rp, rb)` and `asymmetric_beta(rp, rb)`. **Sanity check:** for `rp = 0.9*rb` exactly, `U == D == 0.9` to `1e-12`; for `rp = 0.001 + 0.9*rb`, `U > D`.
6. `defensive_portfolio(panel_t, pd_hat, bench_w, exclude_q=0.2)`: drop the worst PD quintile, re-weight toward low DTS subject to $w'\text{DTS}=\text{DTS}_{\text{bench}}$ via a bounded least-squares projection. **Sanity check:** portfolio DTS within 1% of benchmark DTS; realized 12-month default rate of the held set is below the benchmark's in-sample.
7. `capacity(alpha0, alpha_min, adv, horizon_days, kappa, turnover)`: closed form and a numeric root via `scipy.optimize.brentq`. **Sanity check:** the two agree to `1e-8`.

**Edge cases to warn ROBO about:** negative equity (clip $E$ at a floor and set `no_equity_flag`); `sigma_E=0` for stale prices; months with zero defaults in a CV fold (AUC undefined, skip and log); duplicate bonds per issuer (aggregate to issuer before fitting); DTS of defaulted bonds (set to zero once defaulted, do not let a 5,000bp spread dominate the neutrality constraint).

**The Spec You Hand the Robot (one paragraph for the chapter close):** "Build a firm-month panel from the security master; one row per issuer-month; label = any of {missed payment, Chapter 11, distressed exchange, LME with impairment} within the next 12 months; features lagged to filing date; fit a calibrated dynamic logit and an XGBoost-style model with purged issuer-grouped CV; report CAP, AUC, AR and hit rate at 10/20/30% exclusion; construct a portfolio that excludes the worst-PD quintile and tilts to low DTS with $w'\text{DTS}$ equal to the benchmark; report up/down capture and $\beta^\pm$; stop if the portfolio's DTS deviates by more than 2% from the benchmark or if leverage is implied."

---

## 5. Source map (shelf pages with the exact quotation to use)

| Citation | Why | Verbatim quotation (≤60 words) |
| :--- | :--- | :--- |
| BlackRock_Systematic_High_Yield_Credit p.3 | The capture-ratio diagnosis | "Figure 1 shows the average manager tended to participate in 89.56% of down markets and 92.24% of up markets. This illustrates how the average U.S. high yield manager was building a "defensive" exposure largely by creating a portfolio that has a lower beta than the broad index." |
| BlackRock p.4 | Regime clustering result | "We saw that high yield managers delivered the bulk of their excess returns in "Very Negative" regimes, and trailed index performance in "Very Positive" regimes" |
| BlackRock p.5 | Why beta-tilt defense loses the round trip | "In many cases, these managers gave up more excess return in subsequent "Very Positive" regimes than was mitigated on the downside during "Very Negative" regimes." |
| BlackRock p.6 | The PD-signal claim to be dissected with a CAP curve | "Our proprietary probability of default signal that has underpinned all of our credit strategies for over 20 years has successfully identified 77% of the defaulted bonds in the ICE BofA High Yield Index within 24 months of its default since 2010." |
| Man_Quantitative_Credit_Alpha_Early_Mover_2022 p.26 | Asymmetry as the root of low-risk | "the tightening of a bond on the upside to risk free rates is typically asymmetrically smaller than the jump to recovery in situations of distress. Low-risk factor signals target shorter-dated, higher-rated bonds." |
| Dynkin_Systematic_Investing_in_Credit p.59 | Credit's non-replicable return is VRP plus low-risk | "two in particular are responsible for the majority of credit return outperformance over the replicating portfolio: equity and bond volatility risk premia (VRP) and the low risk anomaly." |
| Dynkin p.95 | Low-vol inside credit | "Short‐maturity bonds had better risk‐adjusted and even non‐risk‐adjusted performance than long‐maturity bonds (Ambastha et al. 2008, Chapter 11)." |
| Dynkin p.396 | Stop-loss rules vs default avoidance | "In fact, only a relatively small proportion of downgraded bonds proceeds to default, while the majority mature at par and generally perform well post‐downgrade." |
| Dynkin p.409 | Loss given downgrade is pro-cyclical | "Assuming a 5.5‐year duration, the loss given downgrade could reach 12.5% (227bp × 5.5year) in the peak of the financial crisis 2008. Second, downgrade rates and spread differentials (and hence losses given downgrade) are positively correlated. Their correlation is 66% in our sample." |
| Dynkin p.609 | Equity momentum as a HY default-avoidance signal | "Equity momentum appears to be a highly informative signal for lower quality names." (Table 15.2: HY Q5–Q1 15.9%/yr, IR 1.74, Jan 1993–May 2017) |
| Dynkin p.739 | Why EMC is defensive and why DTS-matching matters | "top‐EMC portfolios tend to have lower credit exposures than their bottom counterparts during volatile episodes when safer, low‐OAS issuers tend to have less negative equity momentum." |
| Dynkin p.384 | Spread-conditioned transition matrices | "we set our downgrade scalar to 2 (and upgrade scalar to 0.5) and adjust probabilities of unchanged ratings (along the diagonal) such that each row sums to 100%." |
| Dynkin p.209 | Capacity of a HY niche strategy | "the Sharpe ratio decreases to 0.95 (from 1.14) for a portfolio size of $2bn, well above that of the High Yield Index (0.65)." |
| Dynkin p.206 | Fallen angels default less than other HY | "These figures translate into a default rate of 15%, compared with almost twice that rate (24%) among other HY issuers." |
| Bohn_Stein_Active_Credit_Portfolio_Management p.138 | The $N(-\text{DD})$ trap | "This convenient distributional assumption is clearly unrealistic. This becomes clear when we observe that empirically the majority of publicly traded firms have DDs greater than 4." |
| Bohn–Stein p.163 | Data needed to calibrate DD→PD | "In our experience, a well-calibrated model requires at least 1,000 defaults, with a minimum of 400." |
| Bohn–Stein p.226 | Why paired samples flatter a model | "it is easier to tell the difference between a Aaa and a defaulting firm than between a lower-quality firm and a defaulter." |
| Bohn–Stein p.236 | Shumway's critique of static logits | "this class of discrete-choice models will produce biased estimates since they ignore the periods prior to default when a defaulting firm did not default but may have had a similar financial profile." |
| Bohn–Stein p.247 | Power before calibration | "Remember that a poorly calibrated PD model can still be useful for ranking obligors as long as the model has predictive power." |
| Bohn–Stein p.410 | AUC as a probability | "The quantity A, the area under the ROC, is equivalent to the probability that a randomly chosen defaulting loan will be ranked worse than a randomly chosen nondefaulting loan by a specific model" |
| Moyer_Distressed_Debt_Analysis p.183 | Z-score with the units trap | "Z = 0.012 X1 + 0.014 X2 + 0.033 X3 + 0.006 X4 + 0.999 X5" and "Z-scores of <1.81 have been shown as highly predictive of a bankruptcy as long as two years in advance." |
| Moyer p.25 | CCC as a distressed proxy, 1999–2003 returns | "If CCC-rated bonds are, for convenience, used as a proxy for distressed, then the negative market returns for this group over the 1999–2002 period, shown in Table 1-2, illustrate the dangers, while 2003 returns demonstrate the opportunity." (Table 1-2: 1999 −3.0%, 2000 −30.6%, 2001 −2.1%, 2002 −12.7%, 2003 50.8%; CSFB) |
| Moyer p.44 | Ratings at issuance vs realized default | "the predictive power of initial ratings is generally a good predictor of default rates, although one might have expected a larger increase between the B and CCC categories." (Table 2-6 averages 1993–2003: BBB 0.88%, BB 1.96%, B 4.23%, CCC 4.28%, NR 9.95%) |
| Schmid_Credit_Risk_Pricing_Models p.28 | One-year CCC default and stickiness | Table 2.3 (S&P, 1980–2002, NR-adjusted): CCC row "0.10 0.00 0.31 0.63 1.57 9.97 55.82 31.58"; B→D 6.95; BB→D 1.53 |
| Schmid p.103 | Recovery is cyclical | Table 2.33 (Moody's 1970–2002Q2): "Recessions 27.85 ... Expansions 43.10 ... All 40.07" |
| Ben_Dor_Quantitative_Credit_Portfolio_Management p.281 | Timing of downgrade losses | "We find that the majority of the price impact from a downgrade occurs in the final few months before the event, with the largest underperformance in the month of the downgrade and the two months preceding it." |
| Ben Dor p.288 | Spreads lead ratings | "As the credit quality of a particular issuer deteriorates, a spread-based indicator will register the increase in risk much faster than a ratings-based indicator." |
| Ben Dor p.177 | HY spreads carry a risk-aversion premium beyond default and liquidity | "The intercept is larger for high yield, suggesting that risk aversion, unrelated to the bond's default or liquidity characteristics, may drive a large proportion of high-yield spreads." |
| Ben Dor p.104 | Merton basis for DTS (spread vol ∝ spread) | "the relationship between spread and spread volatilities can be shown to be nearly linear over a range of parameter values that is most relevant to credit markets." |
| Paleologo_Advanced_Portfolio_Management p.99 | Low-vol sizing amplifies forecast error | "If we make a mistake of 5% in the expected return forecast on a low-volatility stock, we pay a much higher cost than if we make the same mistake on the high-volatility one." |
| Blackstone_Systematic_Credit p.1 | PD instead of ratings as the common yardstick | "By relying on these proprietary, computationally derived default probabilities rather than sluggish rating agency downgrades or upgrades, the algorithm can objectively compare creditworthiness across the entire global corporate universe" |
| Blackstone p.2 | Penetration trend | "While systematic strategies manage roughly 20% of global equities, they account for less than 2% of the fixed-income universe." |
| Nuveen_Multi_Asset_Credit_Quant_Framework p.4 | Index quality migration | "At year-end 2024, 51% of the index was rated BB, compared to 37% in 2004" |
| Nuveen p.3 | Expected-return decomposition with expected credit loss | "Forward return estimates = yield – estimated credit loss – ∆rates MTM – ∆spread MTM" (Figure 3, 19 Nov 2025: 6.97, 2.55, 0.37, 0.49, 3.56; our reading of the waterfall is yield 6.97 − spread MTM 2.55 − rates MTM 0.37 − credit loss 0.49 = 3.56; CHECK figure layout) |
| Man_Revolutions_in_Credit_Trading_2023 p.3 | HY execution went electronic | "We have therefore moved from having roughly 30% of our order flow in high yield and 60% in investment grade going through electronic venues, to over 90% of our order flow going through electronic-trading venues." |
| Man 2022 p.13 | HY heterogeneity | "there is a wide dispersion in the volatility of bonds, particularly in high yield names." |
| Bolder_Credit_Risk_Modelling p.324 | High-PD risk is idiosyncratic (diversifiable with breadth) | "if a credit counterparty has a large default probability, then much of its inherent default risk is idiosyncratic and, as such, it is less highly correlated with other credit counterparties. Conversely, very low risk counterparties predominately face systematic risk" |

---

## 6. RESEARCH DOSSIER

### 6.1 Market state and the 2024–2026 trend data (primary, FRED/ICE, fetched 17 Oct 2026)

ICE BofA US High Yield Index OAS, FRED series BAMLH0A0HYM2 (https://fred.stlouisfed.org/series/BAMLH0A0HYM2; CSV https://fred.stlouisfed.org/graph/fredgraph.csv?id=BAMLH0A0HYM2):
- 31 Dec 2024: 2.92%. 2025 low: 2.59% on 22 Jan 2025. 2025 high: **4.61% on 7 Apr 2025** (tariff shock). 31 Dec 2025: 2.81%. 2026 high: 3.46% on 30 Mar 2026. 2026 low: 2.60% on 28 Aug 2026. **15 Oct 2026: 3.23%.**

ICE BofA CCC & Lower US HY OAS, FRED BAMLH0A3HYC (https://fred.stlouisfed.org/series/BAMLH0A3HYC):
- 31 Dec 2024: 7.46%. 2025 low: 6.90% (23 Jan 2025). 2025 high: 11.37% (7 Apr 2025). 31 Dec 2025: 8.85%. 2026 low: 8.38% (28 Jan 2026). **14 Oct 2026: 12.82% (highest in the three-year window); 15 Oct 2026: 12.78%.**
- **CCC/HY OAS ratio** (our computation from month-end values): 2.61 (Jan 2025), 2.54 (Apr 2025, the shock compressed the ratio), 3.15 (Dec 2025), 3.53 (Jun 2026), 3.96 (Aug 2026), 3.96 (Oct 2026). The tier is decompressing while the index is calm: the central Trend Watch of §11.6.

ICE BofA BB OAS (BAMLH0A1HYBB): 1.97% on 15 Oct 2026. Single-B OAS (BAMLH0A2HYB): 3.26% on 15 Oct 2026 (https://fred.stlouisfed.org/series/BAMLH0A1HYBB, https://fred.stlouisfed.org/series/BAMLH0A2HYB).

ICE BofA US HY Total Return Index, FRED BAMLHYH0A0HYM2TRIV (CSV https://fred.stlouisfed.org/graph/fredgraph.csv?id=BAMLHYH0A0HYM2TRIV), our computations:
- Calendar 2024 total return **+8.20%**; calendar 2025 **+8.50%**; 2026 YTD to 15 Oct **+0.15%**.
- April 2025 drawdown: peak 28 Feb 2025 (1,755.84) to trough 7 Apr 2025 (1,688.55) = **−3.83%**; the index regained its prior peak on **12 May 2025** (ten weeks round trip). This is the chapter's cleanest "V" for the capture-ratio argument.
- 2026 drawdown: 27 Aug 2026 (1,918.22) to 1 Oct 2026 (1,863.13) = −2.87%.
- Note: FRED holds only three years of these ICE series from April 2026, so 2022–2023 must come from the BlackRock paper (2022 HY "down over 11%", 2023 "up over 13%", p.3) or another source. CHECK exact 2022/2023 index returns (Bloomberg/ICE).

### 6.2 Index composition and quality migration
- State Street Investment Management, *Global high yield—2025 in review and 2026 outlook* (Q4 2025 Insights, data as of 31 Dec 2025; https://www.ssga.com/library-content/assets/pdf/global/fixed-income/2026/2025-global-high-yield-update-fixed-income.pdf): global HY ($-hedged) 2025 total return 8.45% (spread return 2.77%, Treasury return 5.68%); trailing 12-month global HY default rate 1.6%; gross issuance \$335bn (post-COVID high), net \$120bn (four-year high); \$18.9bn flows into US HY; universe **62% BB-rated**, duration **3.1 years**; "spreads in their richest historical decile."
- Nuveen (shelf p.4): BB share of US HY index 51% at YE2024 vs 37% in 2004.
- Wellington, *CCC junk bonds appear undervalued and overlooked* (page dated 30 Sep 2026; https://www.wellington.com/en/insights/ccc-junk-bonds-appear-undervalued-and-overlooked): "CCC rated bonds represent 13% of the high-yield index"; HY spreads "roughly 280 basis points"; BB 175bp, B 275bp; "CCCs are yielding close to 11%"; dispersion within CCC "significant." CHECK the as-of date of the figures.
- Lord Abbett (June 2025, from search summary only; page returned 404): BB over 50% of the index; CCC allocation "near the lowest levels in 20 years"; defaults typically come from the CCC bucket. CHECK.
- Loomis Sayles, *Quarterly Credit Update 4Q24* (https://info.loomissayles.com/hubfs/FD%20Quarterly%20Credit%20Update_4Q24%20FINAL.pdf): CCC-rated securities "accounted for nearly 25% of the overall index option-adjusted spread (OAS)"; dispersion elevated in H1 2024 from CCC underperformance, lowest in H2 2024 as CCC outperformed. (CCC is ~13% of market value but ~25% of index spread: the tier is the index's risk budget.)
- Man 2022 p.39: fallen angels up to a quarter of HY market value in some years; 4.6% of BBB companies downgraded per year; fallen angels outperform HY by ~12% in the 12 months after the event (Man Numeric).

### 6.3 Default and distressed-exchange regime (2024–2026)
- Moody's Analytics, David Hamilton, *Lend, extend, and then…* (18 May 2026; https://www.moodys.com/web/en/us/insights/credit-risk/private-credit/lend-extend-and-then.html): "65% of all corporate defaults in 2025 were distressed exchanges — not hard defaults"; average forward-looking one-year PD for US HY companies 3.2% (Q1 2026); Moody's Ratings baseline speculative-grade default rate drifting toward 3.2% by year-end 2026; private credit proxy default rate 1.6% ex-DEs vs 4.7% including them; of 1,173 borrowers with soft credit events 1979–2026: roughly two-thirds avoid a hard default or repeat event within a decade, about one in four ends in hard default, and "More than 70% of eventual hard defaults following a distressed restructuring occur within the first two years." (Use this as the re-default hazard after an LME in §11.6.)
- Fitch Ratings via Investment Executive (3 Dec 2025; https://www.investmentexecutive.com/news/u-s-leveraged-loan-defaults-to-ease-in-2026-fitch/): 2026 forecasts US leveraged loans 4.5–5.0%, US HY 2.5–3.0%; Europe loans 3–3.5%, HY 3.75–4.25%; "Default rates will decline in 2026 from elevated 2025 levels"; telecom, cable, broadcasting and media expected to drive HY default volume.
- The DESK (Dan Barnes, 27 May 2026; https://www.fi-desk.com/defaults-creep-higher-in-leveraged-credit-markets/): Fitch US private credit default rate a record 6% in April 2026; private-credit-backed borrowers 9.2% default rate in 2025; "Distressed exchanges accounted for 94% of downgrades to default or selective default in the 12 months ending February 2026" (attribution in the article is to a rating-agency count; CHECK which agency); Morgan Stanley forecasts loans 5.5%, private credit 8%, HY 3.5%; Morningstar DBRS: default events up 78% YoY in 2025; private credit now ~30% of leveraged debt vs 13% ten years ago; software and smaller borrowers the pressure points.
- S&P Global Ratings (from search summaries; pages returned 403): US trailing-12-month speculative-grade default rate 5.1% in Dec 2024, expected 3.5% by Dec 2025 (Feb 2025 report); distressed exchanges ~90% of April 2025 defaults and 68% of 2025 YTD defaults through April, "the highest year-to-date proportion since 2008" (14 May 2025 report). CHECK both.
- UBS Asset Management, *2025 fixed income default study* (17 Jan 2025; https://www.ubs.com/us/en/assetmanagement/insights/asset-class-perspectives/fixed-income/articles/2025-fixed-income-default-study.html): 2025 USD HY expected default rate 4.8%, falling to 3.1% excluding two large distressed capital structures; healthcare and telecom the US outliers. (Good illustration of how a few large idiosyncratic names drive the par-weighted rate: breadth matters more than tier.)
- Northern Trust (Dec 2024, search summary; page 503): defaults expected "well below the 4% historical average." CHECK. Neuberger Berman (search summary): 2025–26 cumulative default estimate 3.75–4.75%. CHECK.
- PitchBook via The DESK: software companies 21% of distressed exchanges and similar maneuvers in 2025. CHECK.

### 6.4 The BlackRock framework (shelf, with as-of dates)
- Authors: Tom Parker (CIO Systematic Fixed Income), Scott Radell, Aaron Aguiar, Jesse Kang (Global Head of Systematic Credit); document code BSYSH1225U (PDF created 3 Dec 2025); eVestment data June 2005–June 2025, net of fees (p.2–4).
- Average manager 2022 +0.47% vs benchmark, 2023 −0.68% (p.4); Q1 2024 +0.35%, rest of 2024 −0.37% (p.5); Figure 3 regime pairs: Jun/Jul 2013 (−2.6%/+1.9%), Dec 2018/Jan 2019 (−2.2%/+4.6%), Mar/Apr 2020 (−11.8%/+3.8%), Jun/Jul 2022 (−6.8%/+6.0%), Sep/Oct 2022 (−4.0%/+2.8%) (p.5).
- Regime definition: monthly ICE BofA HY Constrained returns bucketed at ±1.5%; 168 positive vs 72 negative months (p.4).
- PD signal: 12-month horizon, "default occurs when the value of a firm's assets fall below the value of its liabilities," inputs accounting, equity and bond market data, ratings, macro (p.6); 77% of ICE BofA HY defaults identified within 24 months since 2010 (p.6, as of 31 Mar 2024).
- Crowdfund Insider summary of the paper (22 Jun 2025; https://www.crowdfundinsider.com/?p=242950; secondary): methodology "screening out the lowest-quality quintile of bonds"; BHYIX institutional share class excess return 0.34%/yr over the Bloomberg US HY 2% Issuer Capped Index since 1998; top-third peer ranking over 15 years. CHECK against BlackRock primary.
- Product: iShares High Yield Systematic Bond ETF (HYDB), inception 11 Jul 2017, expense ratio 0.35%, AUM \$1.52bn, 260 holdings, tracks the BlackRock High Yield Systematic Bond Index selected and weighted by "default probability, default-adjusted spreads, and volatility"; 1-year total return 0.39%, since-inception average 5.01% (stockanalysis.com, checked 17 Oct 2026; https://stockanalysis.com/etf/hydb/). Search results also name the index "BlackRock High Yield Defensive Bond Index"; CHECK whether the index was renamed.

### 6.5 Peer frameworks and industry size
- Blackstone BCBS (shelf p.1–2): >\$40bn AUM, largest pure-play quant credit platform; DCI acquisition late 2020 (DCI co-founded by creators of the KMV model); value, carry and contrarian rebalancing; systematic ~20% of global equities vs <2% of fixed income.
- Man Group 2022 (shelf p.26–27): Henke, Kaufmann, Messow and Fang-Klingler (2020) find Quality "bears very little relation to performance, at least in investment grade credit"; factor correlation table for HY (Quality–Carry −0.17; Value–Quality 0.23).
- Man Group 2023 (shelf p.3): Man Numeric order flow >90% electronic by 1 May 2023, from ~30% HY / 60% IG previously.
- SIFMA US Corporate Bonds Statistics (page dated 14 Oct 2026; https://www.sifma.org/resources/research/statistics/us-corporate-bonds-statistics/): total US corporate ADV \$66.7bn through Sep 2026 (+13.4% YoY); issuance \$2,195.1bn (+24.5% YoY); outstanding \$12.1tn (2Q26). HY-specific ADV sits in the downloadable file: CHECK (commonly reported in the \$12–16bn/day range in 2024–2025; mark approximate until confirmed).
- Systematic credit AUM trend (Bloomberg/FT reporting on quant credit growth 2024–2026): not fetched this session. CHECK; Ch 4 brief should carry it.

### 6.6 Academic and model literature (verified vs title-only)
- **VERIFIED-URL** Shumway, T. (2001), *Forecasting Bankruptcy More Accurately: A Simple Hazard Model*, Journal of Business 74(1): 101–124, DOI 10.1086/209665 (https://ideas.repec.org/a/ucp/jnlbus/v74y2001i1p101-24.html). Market size, past returns and idiosyncratic return volatility strongly related to bankruptcy; about half the classic accounting ratios insignificant.
- **VERIFIED-URL** Chava, S. and Jarrow, R. (2004), *Bankruptcy Prediction with Industry Effects*, Review of Finance 8(4): 537–569, DOI 10.1093/rof/8.4.537 (https://ideas.repec.org/a/oup/revfin/v8y2004i4p537-569..html). Monthly data substantially improves prediction; accounting variables add little once market variables are in; industry effects matter.
- **VERIFIED-URL** Campbell, J., Hilscher, J. and Szilagyi, J. (2008), *In Search of Distress Risk*, Journal of Finance 63(6): 2899–2939; NBER WP 12362 (2006) (https://www.nber.org/papers/w12362). Distressed stocks earn anomalously low returns since 1981 despite higher betas and volatility: the distress anomaly, the equity cousin of the credit low-risk effect.
- **VERIFIED-URL** Alanis, E., Chava, S. and Shah, A. (2022), *Benchmarking Machine Learning Models to Predict Corporate Bankruptcy*, arXiv:2212.12051 (https://arxiv.org/abs/2212.12051). 2,585 bankruptcies 1990–2019; walk-forward one-year-ahead; Table 2 Panel A out-of-sample AUC: DD + industry only: LASSO 0.551, Random Forest 0.833, XGBoost 0.837; + accounting: XGBoost 0.907; + market: XGBoost 0.916; + macro: 0.915; survival random forest 0.872 with all variables. Excess stock returns, idiosyncratic risk and relative size most important; 10-K text features do not help materially.
- **VERIFIED-URL** Houweling, P. and van Zundert, J. (2017), *Factor Investing in the Corporate Bond Market*, Financial Analysts Journal 73(2); SSRN 2516322 (https://papers.ssrn.com/abstract=2516322, listing confirmed by search; page itself returned 403). Low-risk defined as short maturity and high rating; size, low-risk, value, momentum each produce significant alpha; multi-factor combination raises IR.
- **VERIFIED-URL** Frazzini, A. and Pedersen, L. H. (2014), *Betting Against Beta*, Journal of Financial Economics 111(1): 1–25 (citation confirmed at https://www.lhpedersen.com/research). Alphas decline in beta across equities, Treasuries, credit and futures.
- **VERIFIED-URL** Dick-Nielsen, J., Feldhütter, P., Pedersen, L. H. and Stolborg, C., *Corporate Bond Factors: Replication Failures and a New Framework*, Review of Financial Studies forthcoming, SSRN 4586652 (confirmed at https://www.lhpedersen.com/research). Essential for the "which credit factors survive" box; link to Ch 9.
- **VERIFIED-URL** Dickerson, A., Mueller, P. and Robotti, C. (2023), *Priced Risk in Corporate Bonds*, Journal of Financial Economics (confirmed at https://openbondassetpricing.com/, which also hosts the Bai–Bali–Wen 2019 factors, 108 bond factors from Dickerson, Robotti and Rossetti, and a 341-predictor bond-level ML panel 2002–2022). The site's summary: "it is optimal to simply hold the market portfolio" relative to the four BBW factors.
- **VERIFIED-URL** NUS Credit Research Initiative (https://nuscri.org/en/): daily PD curves 1–60 months for 90,000+ exchange-listed companies; the public forward-intensity PD (Duan, Sun and Wang 2012) is the free benchmark to compare a desk model against.
- **TITLE-ONLY** Altman, E. (1968), *Financial Ratios, Discriminant Analysis and the Prediction of Corporate Bankruptcy*, Journal of Finance 23(4). Merton, R. (1974), *On the Pricing of Corporate Debt*, Journal of Finance 29(2). Bharath, S. and Shumway, T. (2008), *Forecasting Default with the Merton Distance to Default Model*, Review of Financial Studies 21(3). Duffie, D., Saita, L. and Wang, K. (2007), *Multi-period Corporate Default Prediction with Stochastic Covariates*, Journal of Financial Economics 83(3). Duan, J.-C., Sun, J. and Wang, T. (2012), *Multiperiod Corporate Default Prediction: A Forward Intensity Approach*, Journal of Econometrics 170(1). Correia, M., Kang, J. and Richardson, S. (2018), *Asset Volatility*, Review of Accounting Studies 23. Israel, R., Palhares, D. and Richardson, S. (2018), *Common Factors in Corporate Bond Returns*, Journal of Investment Management 16(2) (defensive factor in credit; AQR page not found this session). Ilmanen, A., Byrne, R., Gunasekera, S. and Minikin, R. (2004), *Which Risks Have Been Best Rewarded?*, Journal of Portfolio Management. Henke, H., Kaufmann, H., Messow, P. and Fang-Klingler, J. (2020), *Factor Investing in Credit*, Journal of Index Investing (per Man 2022 p.26–27). Jostova, G., Nikolova, S., Philipov, A. and Stahel, C. (2013), *Momentum in Corporate Bond Returns*, Review of Financial Studies 26(7) (momentum concentrated in non-IG; per Man 2022 p.25). Bai, J., Bali, T. and Wen, Q. (2019), *Common Risk Factors in the Cross-Section of Corporate Bond Returns*, Journal of Financial Economics 131(3). Kelly, B., Palhares, D. and Pruitt, S. (2023), *Modeling Corporate Bond Returns*, Journal of Finance 78(4). Ng, K. Y. and Phelps, B. (2011), *Capturing Credit Spread Premium*, Financial Analysts Journal (cited Dynkin p.396). Ellul, A., Jotikasthira, C. and Lundblad, C. (2011), *Regulatory Pressure and Fire Sales in the Corporate Bond Market*, Journal of Financial Economics 101(3) (cited Dynkin p.158). Kaminski, K. and Lo, A. (2014), *When Do Stop-Loss Rules Stop Losses?*, Journal of Financial Markets (cited Dynkin p.423). Avramov, D., Chordia, T., Jostova, G. and Philipov, A. (2013), *Anomalies and Financial Distress*, Journal of Financial Economics 108(1). Asness, C., Frazzini, A. and Pedersen, L. H. (2012), *Leverage Aversion and Risk Parity*, Financial Analysts Journal (cited Dynkin p.95). Robeco monthly factor return data sets for corporate bonds (size, low-risk, value, momentum; IG and HY), described on robeco.com (search-listed; page not fetched).

### 6.7 Long-run default and recovery parameters to label as historical
- S&P 1980–2002 one-year transitions (Schmid p.28): CCC→D 31.58%, B→D 6.95%, BB→D 1.53%; CCC→CCC 55.82%; CCC→B 9.97%.
- Moody's 1970–2002Q2 recoveries (Schmid p.103): recessions 27.85% mean, expansions 43.10%, all 40.07%; recovery variance explained ~51% by the aggregate default rate (Altman et al., linear), ~60% with log/power forms.
- CSFB default rates by rating at issuance 1993–2003 (Moyer p.44): BBB 0.88%, BB 1.96%, B 4.23%, CCC 4.28%, NR 9.95%.
- Moody's 1970–2014 one-year transition frequencies and average OAS 1994–2015 by rating (Dynkin p.398 Table 9.1): Ba OAS 350bp, B 515bp, Caa 913bp; Caa→default ~13% (last column truncated in the page text; CHECK).
- Downgrade-based diversification (Ben Dor p.282, Table 11.2, 1988–2007): Baa downgrade probability 5.78%/yr, mean loss given downgrade −14.28%, implying position-size ratios Aaa–Aa : A : Baa of 8.9 : 3.1 : 1. (Fallen-angel default rates are in the source map, Dynkin p.206.)

---

## 7. Case studies

### Case 1: The 2022–2023 round trip (BlackRock's own exhibit)
- 2022: US HY "down over 11%", S&P 500 down over 18%, US Agg down over 13% (BlackRock p.3, Bloomberg as of 31 Mar 2024). Average HY manager +0.47% vs benchmark (p.4).
- 2023: US HY "up over 13%", S&P 500 up over 26%, Agg up over 5% (p.3). Average manager −0.68% (p.4). Net of the round trip the average manager *lost* ground: the dimmer switch in two numbers.
- Regime pairs inside the period: Jun/Jul 2022 benchmark −6.8%/+6.0%; Sep/Oct 2022 −4.0%/+2.8% (p.5, Figure 3).
- Systematic read: a PD-ranked exclusion with beta held at 1.0 keeps the July and October rebounds; a 0.9-beta tilt gives back in July what it saved in June. The writer should show the asymmetric-beta regression on these months *(illustrative numbers; only the benchmark returns are sourced)*.

### Case 2: The April 2025 tariff shock, a ten-week V
- HY OAS 2.59% (22 Jan 2025) to 4.61% (7 Apr 2025); CCC OAS 6.90% (23 Jan) to 11.37% (7 Apr) (FRED, §6.1).
- HY total-return index: −3.83% from 28 Feb to 7 Apr 2025; prior peak regained 12 May 2025 (FRED TRIV, our computation).
- Calendar 2025 finished +8.50% (US HY TRIV); global HY $-hedged +8.45% with defaults at 1.6% (State Street, 31 Dec 2025).
- Systematic read: spreads moved ~200bp while 12-month forward PDs (balance-sheet driven) barely moved and realized defaults kept falling, so the model-spread residual $z_i$ flagged "overcompensated" (Blackstone's contrarian rebalancing logic, p.1; BlackRock p.6 "not always prudent to be looking for safety"). The defensive-beta manager who de-risked on 7 April bought back above where he sold. Mark the PD-stability statement as our inference unless a vendor's aggregate PD series is sourced (NUS CRI aggregate 1-year PD by country is a free candidate; CHECK values).

### Case 3: The 2026 CCC decompression (the chapter's live exhibit)
- 15 Oct 2026: HY OAS 3.23%, BB 1.97%, B 3.26%, CCC 12.78% (14 Oct: 12.82%, the highest in the three-year window). CCC/HY ratio ~4.0 vs ~2.6 in January 2025 (FRED, §6.1). HY index 2026 YTD +0.15%; drawdown −2.87% from 27 Aug to 1 Oct 2026.
- Backdrop: Fitch private-credit default rate a record 6% in April 2026 and 9.2% for private-credit-backed borrowers in 2025; distressed exchanges 94% of downgrades to D/SD in the 12 months to Feb 2026; software LMEs; Morgan Stanley HY default forecast 3.5% (The DESK, 27 May 2026); Moody's forward 1-year US HY PD 3.2% (Q1 2026).
- Reading: the index is "calm" because it is 62% BB with 3.1 years of duration (State Street), while the 13% CCC tail carries ~25% or more of the index spread (Loomis, YE2024 figure; higher now by construction). This is the CCC problem in one chart: tier exclusion looks brilliant in 2026 and will look terrible in the 2003-style rebound; PD-ranked selection *inside* CCC is the systematic answer. Any statement about why the tier decompressed (AI disruption of software, private-credit spillover) is interpretation; label it.

### Optional Case 4: Fallen angels as the mirror image
- Dynkin p.140–158 and Ben Dor p.349–351: forced selling, four-fold volume with wider bid-ask, reversal within 24 months, default rates lower than other HY (15% vs 24%). Defensive systematic HY that excludes recent fallen angels on a "momentum is negative" rule is selling to the reversal; the right model conditions on PD, not on the downgrade.

---

## 8. Humor beats (each rides on a correct idea)

1. **Cold open, Ines:** "Downside capture 89.56%, upside capture 92.24%. That's a player who folds ten percent of every hand, including the ones they would have won. A capture ratio is a hand history, not a skill." (Beta tilt gives $U=D=\beta$.)
2. **ROBO literalism (spec box, §11.2):** Told to "avoid defaults," ROBO sold everything below BB and bought T-bills. Downside capture 0%, upside capture 0%, tracking error 100%, client 0. The precise spec says: exclude the worst PD quintile *and hold $w'\text{DTS}$ equal to the benchmark.*
3. **Kaz and $N(-\text{DD})$ (§11.3):** "Under the normal distribution the median public firm has a default probability of three in a hundred thousand." Mags: "The median public firm has not been informed." (Bohn–Stein p.138.)
4. **The Z-score units trap (§11.4):** ROBO built Altman's model from Moyer's printed coefficients (0.012, 0.014, 0.033, 0.006, 0.999) and fed it decimal ratios; every firm scored 0.99 times asset turnover and nothing else. The 0.012 version wants percentages. "Also, the dominant factor is sales over assets, so the model's main question is whether the company does things."
5. **Kaz's legal term of the chapter (§11.4):** Kaz: "Selective default. Selective like a university?" Theo: "Selective like the sponsor chose which lenders got paid." The Ad Hoc Group, in unison, represented by counsel: "We object to the characterization." (Label definition: a distressed exchange is a default that files its own press release as "liability management." If the training set calls it survival, the model learns that the way to never default is to default softly.)
6. **Mags's "back in my day" (§11.6):** "CCCs did minus 30.6% in 2000 and plus 50.8% in 2003. We predicted defaults by whether the CFO returned your call. Now you have 341 predictors and a gradient-boosted forest. The CFO still doesn't return your call." (openbondassetpricing.com's 341-predictor panel; Moyer p.25.)
7. **A CCC bond is an equity option that wears a tie to work (§11.6):** "In October 2026 the tie is 1,278 basis points wide and the index is wearing a 323bp bow tie. Same company, different dress code." (FRED, 15 Oct 2026.)
8. **The 13-week model reborn (§11.4):** Theo's USB-stick model becomes a hazard covariate: $x_{\text{runway}}=$ weeks until cash falls below the minimum-liquidity covenant, capped at 13 because that is where the spreadsheet ends. Kaz: "Why 13?" Theo: "Because that's a quarter." Kaz: "Of what?" Theo: "Of the year, Kaz."
9. **Ines on the 77% (§11.5):** "Seventy-seven percent of defaults flagged within 24 months is a great number until you ask what fraction of the table you folded to get it. A model that flags everyone catches 100% of defaults. That is not defense; that is leaving the casino."
10. **IDO or it didn't happen (§11.7):** The low-risk tilt run market-value-neutral has a beta of 0.85 and a Sharpe that looks like alpha. DTS-neutral, the alpha shrinks by half and is real. "IDO or it didn't happen; and half of it didn't."

---

## 9. Resource-graph candidates

**Podcasts (all TITLE-ONLY; episode URLs not verified this session):** Bloomberg *Odd Lots* episodes on high yield, CCC bonds and liability management (CHECK episode titles and dates); Bloomberg *The Credit Edge* (series page returned 403; CHECK); *Flirting with Models* (Corey Hoffstein) episodes on systematic credit and factor investing in bonds (CHECK guests); Man Institute podcast on quant credit (CHECK); BlackRock *The Bid* on systematic fixed income (CHECK).

**Practitioner writing:**
- VERIFIED-URL BlackRock, *A systematic approach to high yield credit* (Parker, Radell, Aguiar, Kang; Dec 2025), https://www.blackrock.com/gls-download/literature/whitepaper/systematic-high-yield-credit.pdf (also on the shelf).
- VERIFIED-URL Moody's Analytics, David Hamilton, *Lend, extend, and then…* (18 May 2026), https://www.moodys.com/web/en/us/insights/credit-risk/private-credit/lend-extend-and-then.html
- VERIFIED-URL State Street Investment Management, *Global high yield—2025 in review and 2026 outlook*, https://www.ssga.com/library-content/assets/pdf/global/fixed-income/2026/2025-global-high-yield-update-fixed-income.pdf
- VERIFIED-URL Loomis Sayles, *Quarterly Credit Update 4Q24*, https://info.loomissayles.com/hubfs/FD%20Quarterly%20Credit%20Update_4Q24%20FINAL.pdf
- VERIFIED-URL UBS AM, *2025 fixed income default study*, https://www.ubs.com/us/en/assetmanagement/insights/asset-class-perspectives/fixed-income/articles/2025-fixed-income-default-study.html
- VERIFIED-URL Wellington, *CCC junk bonds appear undervalued and overlooked*, https://www.wellington.com/en/insights/ccc-junk-bonds-appear-undervalued-and-overlooked
- VERIFIED-URL The DESK, *Defaults creep higher in leveraged credit markets* (27 May 2026), https://www.fi-desk.com/defaults-creep-higher-in-leveraged-credit-markets/
- VERIFIED-URL Investment Executive, *U.S. leveraged loan defaults to ease in 2026: Fitch* (3 Dec 2025), https://www.investmentexecutive.com/news/u-s-leveraged-loan-defaults-to-ease-in-2026-fitch/
- TITLE-ONLY: Robeco research notes on the low-risk anomaly in credits and conservative credits (Houweling and co-authors); AQR Insights on defensive credit; Barclays QPS notes on EMC and ESP; S&P Global Ratings *Default, Transition, and Recovery* series (site returned 403); Fitch *U.S. Leveraged Finance Default Insight* monthly.

**Academic papers:** see §6.6 (verified: Shumway 2001; Chava–Jarrow 2004; Campbell–Hilscher–Szilagyi 2008/NBER w12362; Alanis–Chava–Shah 2022; Houweling–van Zundert 2017 SSRN 2516322; Frazzini–Pedersen 2014; Dick-Nielsen et al. SSRN 4586652; Dickerson–Mueller–Robotti 2023).

**Data & code:**
- VERIFIED-URL FRED ICE BofA series: BAMLH0A0HYM2, BAMLH0A1HYBB, BAMLH0A2HYB, BAMLH0A3HYC, BAMLHYH0A0HYM2TRIV (https://fred.stlouisfed.org/series/BAMLH0A0HYM2 etc.; CSV endpoint `https://fred.stlouisfed.org/graph/fredgraph.csv?id=<SERIES>`). Note the three-year history limit from April 2026.
- VERIFIED-URL Open Source Bond Asset Pricing, https://openbondassetpricing.com/ (TRACE panel, 108 bond factors, 341-predictor ML panel, Bai–Bali–Wen factors).
- VERIFIED-URL NUS Credit Research Initiative, https://nuscri.org/en/ (PD term structures 1–60 months, 90,000+ firms).
- VERIFIED-URL SIFMA US Corporate Bonds Statistics, https://www.sifma.org/resources/research/statistics/us-corporate-bonds-statistics/
- VERIFIED-URL stockanalysis.com HYDB page, https://stockanalysis.com/etf/hydb/
- Canonical roots: https://www.sec.gov/edgar (EX-10 exhibits for covenant features), FINRA TRACE data at https://www.finra.org/finra-data/fixed-income (root; CHECK exact path), Kenneth French data library and AQR data library (cited by Dynkin p.615; roots only).

---

## 10. Exploratory-space notes (future sections and chapters)

1. **Ch 11-B candidate: Default prediction in the LMT era.** Labeling soft defaults (DE, LME, uptier with impairment, maturity extension), the re-default hazard after a restructuring (Moody's 1,173-borrower study: >70% of eventual hard defaults within two years), and feature engineering from Ch 13's Priming Risk Score (priming capacity, blocker presence, cooperation-agreement coverage) as PD covariates. Distinct from Ch 14 (which models the aggregate cycle) because it is issuer-level prediction and validation.
2. **Private-issuer PD coverage.** Most HY issuers by count are sponsor-owned with no listed equity; the structural model is blind to them (Man 2022 p.35). A section on bond-implied and loan-implied PDs, accounting-only RiskCalc-style models, and "model-regime flags" as features; a Trend Watch on private-credit defaults (Fitch 6% record, April 2026) leaking into public HY.
3. **The CCC tier as its own asset class.** CLO 7.5% CCC-bucket flows and OC-test selling (Ch 21), CCC portfolio-trade liquidity, dispersion as a signal (Loomis), the CCC/HY OAS ratio as a regime indicator (2.6→4.0 from Jan 2025 to Oct 2026), and PD-sorted selection within CCC vs tier exclusion.
4. **Rising stars and fallen angels inside defensive HY.** Dynkin Ch 2–4 (FAR scorecard) and Man 2022 p.38–39: a defensive strategy that buys forced-sold fallen angels with low PD is defense *and* offense; needs its own section with capacity tables (Dynkin p.209).
5. **Convexity overlays instead of beta tilts.** Buying the downside with HYG/JNK puts or CDX HY payer spreads while holding beta at 1.0; cost versus the forgone upside of a 0.9 beta; links to Ch 23 (skew as jump-to-default) and Ch 20 (ETF basis).
6. **Text and LLM features for default prediction.** Alanis–Chava–Shah find 10-K text adds little to 1990–2019 forecasts; the 2024–2026 LLM literature (CHECK specific papers) claims otherwise for earnings and covenant text; a careful horse race with purged CV belongs in Ch 26 or here.
7. **Capital-aware defensive HY for insurers.** Blackstone p.2 (Solvency II capital-charge optimization); NAIC designations; the low-risk tilt as a capital-efficiency play; Trend Watch on insurer HY allocations.
8. **Default clustering and breadth.** Bolder p.324: asset correlation decreasing in PD means CCC risk is largely idiosyncratic, which is the formal case for breadth over concentration in systematic CCC; connect to Vasicek single-factor loss distributions and the Ch 28 Kelly-with-JTD sizing.
9. **Trend Tracker entries for Appendix C:** HY index 62% BB and 3.1y duration at YE2025 (State Street); distressed exchanges 65% of 2025 defaults (Moody's) and 94% of D/SD downgrades in the 12 months to Feb 2026 (The DESK, CHECK attribution); CCC OAS 12.78% vs HY 3.23% on 15 Oct 2026 (FRED); private credit default rate 6% April 2026 (Fitch via The DESK); Man Numeric >90% electronic order flow (May 2023).

<!-- STATUS: COMPLETE -->
