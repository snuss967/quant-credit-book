# Advisor Brief — Chapter 14: The Default & Recovery Cycle in the LMT Era (TREND)

**Target file:** `book_src/14_ch14_default_and_recovery_cycle_lmt_era.md`
**Prepared by:** Fable advisor, Edition 1 (research date 2026-10-17)
**Research note:** Web search budget was exhausted mid-session; everything below marked VERIFIED was read directly from the primary page, opinion text, or PDF this session. Everything from a search-engine summary only, or from memory, is marked **CHECK**. Do not upgrade a CHECK to a fact without re-fetching.

---

## 1. Thesis and the "aha" for an ex-PJT-RSSG reader

**Thesis.** Between roughly 2020 and 2026 the corporate default process changed shape, not just level. Default stopped being one absorbing state ("Chapter 11, see you in 18 months") and became a *multi-state, repeated* process: a distressed exchange or LME, then a re-default clock, then (one time in four) a hard default with a recovery that depends less on your seniority than on *which side of the lender table you sat on*. Moody's puts distressed exchanges at ~63% of all defaults in 2024 and ~65% in 2025, the highest shares on record (VERIFIED, Moody's Asset Management Research, 6 Mar 2025 and 28 Apr 2026). The quant consequence is that the two objects every credit model consumes, the default intensity $\lambda$ and the recovery $R$, each have to be re-specified: $\lambda$ splits into competing cause-specific hazards (soft vs. hard), and $R$ becomes a *mixture over coalition membership* rather than a Beta indexed by seniority. The chapter models the whole thing as a regime shift in the joint law of $(\tau, R)$ and shows how to estimate, simulate, and trade it.

**The aha for the RSSG reader.** You already know the mechanics: Serta, Mitel, Incora, the co-op, the "open market purchase." What you have not been made to do is *integrate over them*. On a systematic desk the question is not "is this uptier legal?" but "what is the cumulative incidence of hard default within 24 months conditional on an LME, and how much of the recovery variance is explained by a single binary variable, `in_majority_group`?" The answer, from Moody's own 1,173-borrower study, is that a quarter of soft credit events end in hard default and 70% of those happen inside two years (VERIFIED, Hamilton, Moody's, 18 May 2026). From Fitch's 2024 emergence sample, first-lien recoveries were 23% for issuers that had done an LME versus 53% for those that had not (CHECK: PitchBook summary of the Fitch report; PitchBook page returned 403). Your RSSG instincts about *who* gets primed are a covariate the PhDs don't have. This chapter turns them into a hazard-rate covariate and a recovery-mixture weight.

**The one-sentence version for the monitor:** "Default rate" is now two numbers, "recovery rate" is now two humps, and the gap between each pair is where the alpha lives.

---

## 2. Section outline (7,000–10,000 words)

Six anatomy elements mapped per section: **[DF]** desk framing, **[DER]** derivation, **[SPEC]** AI-coder spec, **[SRC]** source extraction, **[CASE]** case study, **[RG]** resource graph. Trend Watch boxes marked **TW**.

**Cold open (≤400 words).** 2:40 p.m. Theo gets an RFQ to buy \$12mm of a B3 first-lien term loan that "did an LME last year." Kaz: "So it already defaulted once. Is it immune now?" Mags: "No. It's on parole." Ines: "What's the pot, and who at this table was in the majority group?" The question the chapter answers: *what is the law of (time-to-next-default, recovery) for a credit that has already been restructured once, and how is it different from 2015?* Then "By the end of this chapter you will be able to..."

**14.1 Two default rates, two recovery rates [DF][SRC][TW]**
- The definitional fork: S&P/Moody's count distressed exchanges as defaults; ISDA North American corporate CDS (No-Restructuring convention since 2009) generally does not. Schmid p.336 quote (S&P definition).
- Moody's "dual-track" numbers: June 2025 trailing HY default rate 5.8% including DEs, 2.1% excluding the 51 distressed restructurings (VERIFIED).
- **TW 1: The soft-default takeover, 2008–2025.** DE share of defaults: ~63% (2024), 64% (H1 2025), ~65% (2025), highest on record with data back to the 1980s (Moody's, VERIFIED); S&P 2024: 59.3% of 145 global defaults, highest since 2008 (CHECK). Moyer p.87's 2004 line that out-of-court restructuring succeeds "less than 10% of the time" as the before picture.

**14.2 The competing-risks decomposition of $\lambda$ [DER][SPEC]**
- Cause-specific hazards $\lambda_H, \lambda_D$; cumulative incidence functions; the DE share as $\lambda_D/(\lambda_H+\lambda_D)$; Aalen–Johansen estimator; Fine–Gray subdistribution hazard for regression on covariates (sponsor-owned, loan-only structure, docs vintage, co-op presence).
- Spec: `aalen_johansen`, `cause_specific_nelson_aalen`.

**14.3 The re-default clock: survival after a soft default [DER][SRC][CASE][TW]**
- Semi-Markov chain: Performing → {DE, Hard, Cured}; DE → {Hard, DE again, Cured}. Bolder p.682 (absorbing states) quoted, then: *a DE is not absorbing*.
- Mixture-cure (Boag–Farewell) Weibull for time-since-DE; calibrate to Moody's: 25% eventual hard default, 70% of those within 2 years, hazard <0.5 pp/yr after year 5 (VERIFIED). Derive $\eta$ from the 70%-within-2-years condition.
- The 13-week model returns: re-default hazard as a function of liquidity runway added by the LME (new money vs. pure maturity extension).
- **TW 2: The re-default ledger.** Dated LME → bankruptcy intervals: Serta (Jun 2020 → 23 Jan 2023), Mitel (Oct 2022 → 10 Mar 2025), Incora (Mar 2022 → 1 Jun 2023), Robertshaw (2023 LME → 15 Feb 2024), Del Monte (Aug 2024 → 1 Jul 2025). Filing dates VERIFIED on CourtListener dockets; LME dates partly CHECK (see §6).

**14.4 Recovery is a mixture over coalition membership [DER][SRC][CASE]**
- Beta-mixture recovery; between-group variance $\pi(1-\pi)(\mu_{in}-\mu_{out})^2$; "recovery compression" is really *bimodalization*.
- Serta remand arithmetic (July 7, 2026) as a court literally computing $\mathbb{E}[R_{in}]-\mathbb{E}[R_{out}]$: \$734mm second-out consideration, \$1.887bn class, 47.43% ratable share, \$348mm but-for, \$261.13mm damages plus 9% NY prejudgment interest from 22 June 2020 (VERIFIED from opinion text).
- Bohn–Stein p.305/p.316: lookup tables carry ~40% of LGD predictive power; two-stage (probit then regression) models. Add the new first-stage variable: $P(\text{in majority})$.
- Schmid p.103 table: recessions 27.85% vs. expansions 43.10% mean recovery (1970–2002Q2), the classic regime shift; we add a second regime axis (LME'd vs. not).

**14.5 Cooperation agreements: the lender cartel as a repeated game [DF][SRC][CASE][TW]**
- Moyer p.86 (poker, credible bluff, the regulars) → Ines's Poker Table box.
- **TW 3: From 4 a year to 45.** ~45 US co-ops in 2024 vs. an average of ~4/yr 2018–2023 (VERIFIED as cited in the Optimum complaint via 9fin). Offensive / defensive / carve-out variants (Seaton via HBRT, 14 Apr 2026, VERIFIED). Optimum (f/k/a Altice USA) v. Co-op Lenders, S.D.N.Y., Sherman Act price-fixing and group boycott, alleging the Co-op Lenders hold 88% of the "Leveraged-Finance Market" (VERIFIED via Cleary, 18 Dec 2025). Warner Bros. Discovery 2025 bonds with "anti-cartel" provisions (VERIFIED via HBRT). European backlash 2025 (VERIFIED, Baker McKenzie Jan 2026).
- Model: a threshold public-good game with a co-op as a commitment device; transfer restrictions as a change to the arrival process of "defectors"; hazard of non-pro-rata LME conditional on co-op coverage ratio $c \in [0,1]$.
- Increment the cooperation-agreement counter.

**14.6 The courts as a regime variable: Dec 31, 2024 → Jul 7, 2026 [DF][CASE][SRC]**
- Docket Diary: Serta (5th Cir., Nos. 23-20181 c/w 23-20363, 23-20450, 23-20451), Mitel (*Ocean Trails CLO VII v. MLN TopCo*, 2024 NY Slip Op 06660, 1st Dep't), both decided the same New Year's Eve, opposite outcomes on different words. Serta remand damages, 7 Jul 2026. Del Monte adversary (Bankr. D.N.J. 26-01018, 23 Jan 2026) and district-court suit (3:26-cv-02379, 6 Mar 2026). CPPIB v. Deutsche Bank Trust Co. Americas (N.Y. Sup. Ct., 17 Mar 2026) as a CHECK lead.
- How to encode a ruling as a jump in the prior on $P(\text{priming succeeds})$ for every contract with the same words; the Fifth Circuit's own line that open-market exceptions "will often not justify an uptier."
- Link to the Ch 13 Priming Risk Score: PRS inputs shift discretely at ruling dates.

**14.7 Regime shifts in the joint law of $(\tau,R)$: a Markov-switching engine [DER][SPEC]**
- Two-state Hamilton filter on the DE share and on mean LGD; why annual data (≈45 points) is too short and what to do (monthly counts, pooled cross-section, Bayesian priors from the ruling calendar).
- $\mathbb{P}$ vs. $\mathbb{Q}$: everything above is physical; CDS spreads imply a $\mathbb{Q}$-hazard against an ISDA event definition that excludes most DEs under No-R. The wedge: with $R^{\mathbb{Q}}=40\%$ conventional and $R^{\mathbb{P}}\approx 23\%$ for LME'd first liens, the implied hazard from a given spread differs by a factor $0.60/0.77\approx 0.78$.
- Full reference implementation (`lme_cycle_engine.py`) and sanity checks.

**14.8 Case studies.** Serta 2020→2026 (full arc); Mitel 2022→2025 (legal win, economic loss); Del Monte 2024→2026 (the fast re-default; facts CHECK).

**14.9 Trading the regime [DF].** Signals: (i) post-LME re-default hazard vs. market-implied; (ii) coalition-membership proxies from Rule 2019 statements and co-op announcements (Ch 25 feeds); (iii) docs-vintage factor (pre/post "Serta blocker"); (iv) the dual default rate spread as a cycle indicator. Where "IDO or it didn't happen" bites: DE-share trend is beta; predicting your own table side is alpha.

**14.10 Desk Debrief, The Spec You Hand the Robot, Exercises.**

Resource graphs after 14.1, 14.4, 14.5, 14.6, 14.7 (at minimum) and at chapter end.

---

## 3. Derivation skeletons

All physical-measure ($\mathbb{P}$) unless stated. Time $t$ in years. Recovery $R$ as fraction of par (RFV convention unless stated).

### 3.1 Competing risks: splitting the default intensity

Let $\tau$ be the time of the *first* credit event and $K\in\{H,D\}$ its type (hard default, distressed exchange). Cause-specific hazards:
$$\lambda_k(t)=\lim_{h\downarrow 0}\frac{\mathbb{P}(t\le\tau<t+h,\ K=k\mid \tau\ge t)}{h},\qquad \lambda(t)=\lambda_H(t)+\lambda_D(t).$$
Survival $S(t)=\exp\!\big(-\int_0^t\lambda(u)\,du\big)$. Cumulative incidence (sub-distribution) functions:
$$F_k(t)=\mathbb{P}(\tau\le t,\ K=k)=\int_0^t S(u)\,\lambda_k(u)\,du,\qquad F_H(t)+F_D(t)+S(t)=1.$$
With constant hazards:
$$F_D(t)=\frac{\lambda_D}{\lambda_H+\lambda_D}\big(1-e^{-(\lambda_H+\lambda_D)t}\big),\qquad \text{DE share}=\frac{\lambda_D}{\lambda_H+\lambda_D}.$$
A 65% DE share implies $\lambda_D\approx1.86\,\lambda_H$. From Moody's June 2025 numbers (5.8% including DEs, 2.1% excluding), $\lambda\approx-\ln(1-0.058)=0.0597$, split $\lambda_D\approx0.038$, $\lambda_H\approx0.022$ *(approx.; converting rates to hazards)*.

Nonparametric estimation: Nelson–Aalen for each cause, $\hat\Lambda_k(t)=\sum_{t_i\le t} d_{k,i}/n_i$, and the Aalen–Johansen CIF $\hat F_k(t)=\sum_{t_i\le t}\hat S(t_{i}^-)\,d_{k,i}/n_i$.

**Error-prone spots.** (a) Treating $1-\text{KM}$ with the other cause censored as a probability: it overstates $F_k$ because it pretends the competing event never happens. (b) Regressing on covariates: a Cox model on $\lambda_D$ tells you about the *rate* of DEs among survivors, not about the *probability* of eventually having a DE; for the latter use Fine–Gray (1999) on the subdistribution hazard. (c) Agency default rates are issuer-count rates over trailing 12 months, not hazards; convert before mixing with CDS-implied intensities. (d) Dollar-weighted vs. count-weighted DE shares differ materially; state which.

### 3.2 The re-default clock: a mixture-cure Weibull after a DE

Let $U$ be time since the DE. Moody's (1979–2026, 1,173 borrowers): ~1/4 of soft events end in hard default; >70% of those within two years; after year five the hazard adds <0.5 pp/yr; ~2/3 clean for a decade (VERIFIED). A mixture-cure model matches all four facts:
$$\mathbb{P}(U>u)=(1-p)+p\,\exp\!\big[-(u/\eta)^k\big],\qquad p\in(0,1)\ \text{the "susceptible" fraction}.$$
Population hazard $h(u)=\dfrac{p\,f_0(u)}{(1-p)+p\,S_0(u)}$ with $f_0,S_0$ the Weibull density/survival. Calibration: set $p=0.25$ for hard default (or $\approx0.35$–$0.40$ for "hard default or another DE"). The condition $F(2)/p=0.70$ gives $(2/\eta)^k=-\ln 0.30=1.204$. With $k=1$, $\eta\approx1.66$ years (baseline hazard among the susceptible $\approx0.60$/yr); with $k=0.7$ (decreasing hazard, the empirically plausible case), $\eta\approx1.53$. Initial population hazard at $u=0^+$ for $k=1$: $0.25\times0.60=0.15$/yr, decaying toward zero, which is exactly the "<0.5 pp after year five" shape.

Covariates enter through $p$ (logistic) and $\eta$ (log-linear): `new_money_fraction`, `maturity_extension_years`, `liquidity_runway_weeks` (the 13-week model, reborn), `sponsor_backed`, `loan_only_structure`, `uptier_vs_dropdown_vs_A&E`, `coop_in_place`, `docs_vintage`.

**Error-prone spots.** (a) Right-censoring: 2024–2025 LMEs have at most 1–2 years of follow-up; a naive estimate of $p$ is biased low. ROBO's literal implementation sets the hazard to zero after the last observed event. (b) Identifiability of $p$ vs. $\eta$ with short follow-up: fix $k$ or put a prior on it. (c) Left truncation if the sample is "issuers that were still around when the database started."

### 3.3 Expected loss with a soft-default path

Horizon $T$. Let $L_H=1-R_H$ be LGD on a hard default with no prior LME, $L_D$ the immediate economic haircut at the DE (depends on coalition side), $q$ the probability of hard default within the remaining horizon given a DE, and $L_{H\mid D}$ the LGD on a hard default *after* an LME. Then
$$\mathrm{EL}(T)=F_H(T)\,L_H+F_D(T)\Big[L_D+(1-L_D)\,q\,L_{H\mid D}\Big].$$
*Illustrative* inputs: $\lambda_H=0.022,\lambda_D=0.038,T=3$ ⇒ $F_D(3)\approx0.102$, $F_H(3)\approx0.058$; $L_H=0.47$ (Fitch no-LME 53% recovery, CHECK); $L_{H\mid D}=0.77$ (Fitch 23%, CHECK); $q=0.25$. Majority-side holder ($L_D=0.26$, the Serta exchange ratio): EL $\approx6.8\%$. Excluded holder ($L_D=0.75$, the \$0.25 closing-date price in the Serta remand): EL $\approx10.9\%$. Naive single-state model with 47% LGD on the total 16% three-year default probability: $7.5\%$. The spread between 6.8% and 10.9% is the coalition variable. Mark all three *illustrative*.

### 3.4 Recovery as a coalition mixture

$$R\mid\text{default}\sim\pi\,\mathrm{Beta}(a_{in},b_{in})+(1-\pi)\,\mathrm{Beta}(a_{out},b_{out}),\quad \pi=\mathbb{P}(\text{in majority group}).$$
$\mathbb{E}[R]=\pi\mu_{in}+(1-\pi)\mu_{out}$ and
$$\mathrm{Var}[R]=\pi\sigma_{in}^2+(1-\pi)\sigma_{out}^2+\pi(1-\pi)(\mu_{in}-\mu_{out})^2.$$
Serta numbers *(from the remand opinion; the value interpretation is illustrative)*: $\pi\approx0.526$ (participating lenders held ~\$992mm of a \$1.887bn class), $\mu_{in}\approx0.74$, $\mu_{out}\approx0.25$ ⇒ $\mathbb{E}[R]\approx0.51$ and a between-group standard deviation of $\approx0.245$ *from membership alone*. That is the whole historical cross-sectional dispersion of recoveries (Schmid p.103: std ≈27%) generated by one binary. Method-of-moments Beta fits per group; the Bohn–Stein two-stage model gets a new first stage: $\pi$ from a logistic on holdings concentration, CLO share, co-op membership, and fund type.

Link to Ch 5: the zero- and one-inflated Beta remains; the inflation masses now have coalition-specific weights.

### 3.5 Regime switching in $(\lambda_D/\lambda,\ \mathbb{E}[L])$

Two-state hidden Markov model, states $s_t\in\{0,1\}$ ("pre-LME regime", "LME regime"), transition matrix $P$. Observables: annual DE share $y_t$ (or monthly DE counts as binomial draws) and mean LGD. Hamilton filter: with $\eta_t=[f(y_t\mid s_t=0),f(y_t\mid s_t=1)]^\top$,
$$\hat\xi_{t\mid t}=\frac{\hat\xi_{t\mid t-1}\odot\eta_t}{\mathbf 1^\top(\hat\xi_{t\mid t-1}\odot\eta_t)},\qquad \hat\xi_{t+1\mid t}=P^\top\hat\xi_{t\mid t},$$
log-likelihood $\sum_t\log\mathbf 1^\top(\hat\xi_{t\mid t-1}\odot\eta_t)$. Recovery regime: Beta mean $\mu_s$ with $\mu_0\approx0.43$ (expansions) and $\mu_1\approx0.28$ (recessions) from Schmid p.103 as a *macro* regime; the LME regime is a second, orthogonal switch on $\pi$ and $\mu_{out}$.

**Error-prone spots.** Label switching; ~45 annual observations cannot identify four parameters plus $P$; use counts not shares (binomial likelihood); put the ruling calendar in as an exogenous regressor on $P$ (time-varying transition probabilities); do the filter in log space.

### 3.6 $\mathbb{P}$ vs. $\mathbb{Q}$ and the ISDA definitional wedge

CDS par spread $s\approx\lambda^{\mathbb{Q}}(1-R^{\mathbb{Q}})$. Market convention $R^{\mathbb{Q}}=0.40$ (Dynkin p.354 uses it as the representative assumption on the $\mathbb{P}$ side too). For a given spread, $\lambda^{\mathbb{Q}}=s/0.60$ under convention and $s/0.77$ if the realistic post-LME first-lien recovery (~23%) were used: a 22% lower implied hazard. More important, under North American "No-Restructuring" CDS most DEs are not credit events at all *(general market knowledge; cross-reference Ch 24 and have the writer state the ISDA 2014 Definitions / standard North American corporate convention without a URL)*, so an agency default rate that is 65% DEs cannot be compared with a CDS-implied hazard without first removing $\lambda_D$. The clean statement: CDS prices $\lambda_H^{\mathbb{Q}}$ (plus failure-to-pay-like events); agencies report $\lambda_H^{\mathbb{P}}+\lambda_D^{\mathbb{P}}$. Mixing them is the single most common error in "the market is underpricing defaults" notes.

---

## 4. Code spec: `lme_cycle_engine.py`

**Purpose.** A seeded, numpy/scipy/pandas reference implementation that (1) simulates an issuer cohort through the semi-Markov LME-era default process under a regime-switching environment, (2) estimates the competing-risk and re-default objects from the simulated event table, (3) prices expected loss by coalition side, and (4) runs a two-state Hamilton filter on the DE share. Everything executes top-to-bottom in one interpreter.

**Data schema (event table, pandas DataFrame):**
`issuer_id:int64`, `t_event:float64` (years from cohort start), `event:int8` ∈ {0 censored, 1 hard default, 2 distressed exchange, 3 cured/refinanced}, `time_since_de:float64` (NaN unless the issuer had a prior DE), `regime:int8`, `in_majority:int8` (0/1, drawn at DE time with prob $\pi$), `recovery:float64` (fraction of par, NaN unless event∈{1,2}), `new_money_frac:float64`, `coop:int8`.

**Parameter dataclass:** `lam_H:(2,)`, `lam_D:(2,)` per regime; `P:(2,2)` regime transition matrix (annual); cure-Weibull `(p, k, eta)` for post-DE hard default; `pi` for coalition membership; Beta `(a,b)` for `R_in`, `R_out`, `R_hard_noLME`, `R_hard_postLME`; `T_max` and `censor_rate`.

**Functions.**
1. `simulate_cohort(n, params, seed) -> DataFrame`: competing exponential clocks per regime year; on DE draw `in_majority` and `recovery_D`; then draw post-DE time via the cure-Weibull (inverse CDF; cured issuers get $+\infty$ then censored at `T_max`); regime path simulated once per cohort (systematic) with the option of independent paths for a sanity mode.
2. `nelson_aalen_cause(df, cause) -> (times, Lambda_hat)` and `aalen_johansen(df) -> DataFrame[time, S, F_H, F_D, F_C]`.
3. `fit_cure_weibull(u, delta) -> (p, k, eta, loglik)`: MLE with right-censoring via `scipy.optimize.minimize` on log-parameters; log-sum-exp for the mixture survival.
4. `expected_loss(params, T, side) -> float` closed form (§3.3) and `expected_loss_mc(df, T, side)` from the simulated table.
5. `hamilton_filter(y, mu, sigma, P) -> (xi_filtered, loglik)` and `fit_ms2(y, seed)` with a few random restarts; input $y$ = annual DE share produced by `simulate_cohort` aggregated by year.
6. `coalition_mixture_moments(pi, ab_in, ab_out) -> (mean, var, between_var)`.

**Built-in sanity checks (asserts, printed PASS/FAIL):**
- With `lam_D=0`, the Aalen–Johansen $F_H(t)$ is within 3 MC standard errors of $1-e^{-\lambda_H t}$ at $t\in\{1,3,5\}$.
- $F_H+F_D+F_C+S=1$ at every jump time to 1e-12.
- Simulated DE share converges to $\lambda_D/(\lambda_H+\lambda_D)$ in a single-regime run.
- `coalition_mixture_moments` mean equals the sample mean of simulated recoveries within 0.01; between-group variance formula matches the sample decomposition.
- `fit_cure_weibull` recovers $(p,k,\eta)$ within the 95% bootstrap interval on a 20,000-issuer simulation, and the fitted $F(2)/p$ is ≈0.70 when calibrated to Moody's.
- Hamilton filter probabilities lie in [0,1], rows sum to 1, log-likelihood is non-decreasing across EM iterations (if EM is used) and the filtered regime agrees with the simulated regime >85% of years when regimes are well separated.

**Numerical guards.** Clip Beta parameters ≥1e-6; guard `log(0)` in hazards; work with log-survival; handle tied event times by processing causes jointly at each distinct time; `np.random.default_rng(seed)` everywhere; never index by issuer order (sort by `t_event` with a stable sort). Edge cases: issuers with two DEs before a hard default (allow at most `max_de=2` to keep the state space small, document it), DE at $t=0$ (disallow, start clocks at $t>0$), horizon $T$ beyond `T_max` (raise).

**What ROBO built from the vague version** (for the box): told to "exclude distressed exchanges from the default rate," ROBO deleted the rows and reported 2.1%, then flagged the credit cycle as "benign." Told to "model re-default," it fit an exponential to a sample with 14 months of follow-up and reported a 9-year expected time to hard default with a straight face.

---

## 5. Source map (shelf pages; quotations verbatim, ≤60 words)

| Citation | Why | Quote for the writer |
|---|---|---|
| Schmid_Credit_Risk_Pricing_Models p.336 | S&P's definition of default makes DEs defaults; the definitional fork of §14.1 | "Distressed exchanges, on the other hand, are considered defaults whenever the debtholders are offered substitute instruments with lower coupons, longer maturities, or any other diminished financial terms." |
| Moyer_Distressed_Debt_Analysis p.228 | Coercive vs. noncoercive exchange, the 2004 ancestor of the uptier | "Exchange offers are “coercive” when they compel cooperation by exposing nonparticipants to the risk of being made worse off." |
| Moyer_Distressed_Debt_Analysis p.229 | Moyer describes, in 2004, priming the holdouts with new senior secured paper | "Thus, old note holders that choose to hold out and not participate would retain their full claim, but would be at risk of receiving very little in a bankruptcy (which, given the facts, is a fairly high risk) due to the subordination." |
| Moyer_Distressed_Debt_Analysis p.85 | Holdout problem as prisoner's dilemma; the co-op is the cooperative equilibrium device | "This is referred to as the “holdout” problem: those not participating in the exchange may be better off than those that do, but if too many hold out, all will be worse off." |
| Moyer_Distressed_Debt_Analysis p.86 | Poker, repeated game among "the regulars"; Ines's box | "However, as in poker, which is analogous because the “multiple-hand” format of the game is similar to the series of transactions in the distressed marketplace, to be effective one must have a credible “bluff.”" |
| Moyer_Distressed_Debt_Analysis p.87 | The before picture for TW 1 | "Given the relative simplicity of the out-of-court restructuring, one might well wonder why it is successfully employed less than 10% of the time." |
| Moyer_Distressed_Debt_Analysis p.336 | Prepack scarcity and 85–90% thresholds; contrast with bare-majority uptiers | "Table 12-1 presents data on completed prepacks, which in the 1998–2002 period represented less than 7% of cases." |
| Moyer_Distressed_Debt_Analysis p.405 | Moody's C-ratings encode expected severity; rating as recovery signal | "Moody’s attempts to use its C ratings to indicate severity of ultimate loss. Thus, a Caa rating implies a full or nearly full recovery, a Ca rating implies a partial recovery, and a C rating implies little to no recovery." |
| Schmid_Credit_Risk_Pricing_Models p.103 | The original recovery regime shift (recession vs. expansion); Table 2.33 numbers in annotation: means 27.85% / 43.10% / 40.07%, std ≈27% | "The table supports our opinion that recovery rates decrease during recessions and increase during expansions." |
| Schmid_Credit_Risk_Pricing_Models p.102 | Frye's downturn LGD; Hu–Perraudin −0.22 correlation | "Frye finds that in a severe downturn, recovery rates might decline 20 - 25 percentage points from their normal year average." |
| Schmid_Credit_Risk_Pricing_Models p.100 | PD–LGD dependence as a modeling postulate (Bakshi–Madan–Zhang) | "In fact, recovery and default rates are inversely related (see, e.g., Altman (2001)). Hence, for modeling purposes one can postulate that the recovery rate is a function of the default rate." |
| Schmid_Credit_Risk_Pricing_Models p.94 | Intensity framework handles regimes and censoring; justifies §14.7 | "The dependence on external covariates and changes in regimes can be formulated, tested and quantified." |
| Bohn_Stein_Active_Credit_Portfolio_Management p.288 | Why LGD modeling lagged; "legal proceedings" is now the main driver | "LGD realizations can depend on many hard-to-quantify factors, from the quality of a defaulting firm’s assets and franchise to the vagaries of the resolution of legal proceedings and bankruptcy rulings." |
| Bohn_Stein_Active_Credit_Portfolio_Management p.305 | Lookup tables are weak; secured ≠ safe | "However, in our own research, we have found that they account for only about 40 percent of the power we are able to attain in predicting levels of recoveries." |
| Bohn_Stein_Active_Credit_Portfolio_Management p.316 | Two-stage LGD; we add the coalition stage | "We have had relatively good success in specifying LGD models in two stages: the first stage being a discrete choice (probit) model to predict the probability of observing a loss greater than zero, given default" |
| Bohn_Stein_Active_Credit_Portfolio_Management p.311 | Selection bias (Heckman) in LGD; post-LME samples are selected twice | "This implies that the LGD values we observe are actually conditional on default having occurred." |
| Bolder_Credit_Risk_Modelling p.357 | The independence assumption our chapter breaks | "Its precise distribution is not given, but it is assumed to be independent of default and any other recovery events." |
| Bolder_Credit_Risk_Modelling p.682 | Default as absorbing state; a DE is not | "Default, for example, is a quite reasonable description of an absorbing state." |
| Bolder_Credit_Risk_Modelling p.83 | Recovery as a random variable; severity identity | "R ∈(0, 1) is typically termed the recovery rate; again, this is, in principle, an unknown random variable." |
| Ben_Dor_Quantitative_Credit_Portfolio_Management p.297 | Baa realized default/recovery 1990–2009 for the spread-premium computation | "During this period, their average annual default rate was 0.41% and their average recovery rate was 44.6% (meaning that the average loss given default was 55.4%)." |
| Dynkin_Systematic_Investing_in_Credit p.354 | 40% as a convention; forced-seller framing | "A representative average recovery rate of 40% is assumed, such that a loss of 60% is assumed to be incurred with the specified probability." |
| BlackRock_Systematic_High_Yield_Credit p.6 | Default-avoidance signal; annotate: which default definition? Structural PD models see asset value, not LME incentives | "Our proprietary probability of default signal that has underpinned all of our credit strategies for over 20 years has successfully identified 77% of the defaulted bonds in the ICE BofA High Yield Index within 24 months of its default since 2010." |
| Nuveen_Multi_Asset_Credit_Quant_Framework p.3 | Expected credit loss input to allocation; annotate: incl. or excl. DEs changes the 5-year HY forward return | "Estimated credit loss Derived from credit default rate forecasts and expected recovery rates" |
| Houlihan_Lokey_Distressed_MA p.52 | Dual-track out-of-court / 363 as the ancestor of the LME-then-prepack path | "All parties agree to attempt to effectuate an out-of-court deal. However, if impediments arise, the deal will be consummated through a Chapter 11 Section 363 asset sale." |
| Schmid_Credit_Risk_Pricing_Models p.373 | Verified bibliographic anchor for Franks & Torous (1994), the classic DE-vs-Ch 11 recontracting paper | (bibliography entry; cite as Franks & Torous (1994), *Journal of Financial Economics* 35: 349–370) |

---

## 6. RESEARCH DOSSIER

### 6.1 The default mix: distressed exchanges take over

- **Moody's Ratings, 2024:** distressed exchanges "accounted for about 63% of defaults, the highest annual share on record, with data going back to the 1980s." VERIFIED: Moody's Asset Management Research, *"Growth Recession" Hounds Parts of Corporate Credit Market*, 6 March 2025 (David Hamilton, Joanna Su), https://www.moodys.com/web/en/us/insights/resources/growth-recession-hounds-parts-of-corporate-credit-market.pdf. Same report: average one-year PD of US listed companies reached a post-GFC high of 9.2% at end-2024; "More distressed restructurings rather than hard default events are likely."
- **Moody's, H1 2025:** DEs were 64% of all defaults in H1 2025, "about the same pace as all of 2024"; loan market most distressed, "particularly borrowers with loan-only capital structures backed by private equity firms." Trailing HY (bond + loan) default rate 5.8% in June 2025 including DEs; removing the 51 distressed restructurings gives 2.1%, "almost one-third" of the headline; loan defaults expected to "drift sideways around the 7% level." VERIFIED: Moody's AMR, *Corporate Credit Risk Looking for a Catalyst to Break Out*, 7 August 2025, https://www.moodys.com/web/en/us/insights/resources/us-report-july-2025.pdf. Footnote cites Moody's Ratings Monthly Default Report, July 2025 ("Default count fell in June, but the dollar volume more than doubled").
- **Moody's, full-year 2025:** "Distressed restructurings accounted for approximately 65% of all defaults." Private credit proxy default rate 1.6% excluding DEs vs. 4.7% including. Average PD, US listed companies, 7.9% in March 2026 (from 9.1% a year earlier); US HY PD 3.2%. Corporate lending AUM forecast >\$2tn in 2026, toward \$4tn by end of decade. VERIFIED: Moody's, *America's corporate credit is at a tipping point*, 28 April 2026, https://www.moodys.com/web/en/us/insights/credit-risk/private-credit/us-corporate-default-risk-in-2026.html.
- **S&P Global Ratings, 2024 annual study (published 27 Mar 2025):** 145 global corporate defaults; distressed exchanges 59.3% of defaults, highest since 2008; repeat defaulter count "remained elevated." **CHECK** (search-engine summary; S&P pages return 403). URL to retry: https://www.spglobal.com/ratings/en/research/articles/250327-default-transition-and-recovery-2024-annual-global-corporate-default-and-rating-transition-study-13452126.
- **S&P's narrower DE count:** 45% / 54% / 52% of defaults in 2023 / 2024 / 2025-through-August. **CHECK** (search summary only). The methodological gap vs. Moody's (~63–65%) is itself a teaching point: the "record" depends on whose definition.
- **Moody's, "DEs and LMEs roughly 70% of US defaults since early 2022."** **CHECK** (search summary).
- **S&P, *Distressed Exchanges Reached Their Highest Level Since 2009* (15 Aug 2024) and *Distressed Exchanges Underpin Rise In North American Selective Defaults* (28 Oct 2024).** Titles VERIFIED from search listing; contents 403. Key claims per summary (CHECK): many DEs are followed by another default within a short period; repeat defaulters re-emerge into CCC/CC.
- **S&P, *The Rise of Repeat Defaulters* (11 April 2024).** Title referenced in S&P studies; numbers not retrieved. **CHECK** before citing any percentage.

### 6.2 Re-default after soft defaults

- **Moody's Analytics (David Hamilton), *Lend, extend, and then...*, 18 May 2026.** Moody's Default & Recovery Database, 1979–2026, 1,173 unique borrowers with a soft credit event: roughly two-thirds suffered no hard default or repeat credit event within a decade; about one in four ended in a hard default; more than one in three ended in a hard default *or* another distressed credit event; more than 70% of eventual hard defaults occurred within the first two years; after year five the hazard adds fewer than half a percentage point per year. VERIFIED: https://www.moodys.com/web/en/us/insights/credit-risk/private-credit/lend-extend-and-then.html. Bloomberg covered it 19 May 2026 as "Distressed-Debt Deals Often End in 'Hard Default,' Moody's Warns" (title from search listing; article not fetched).
- **Re-default ledger (dates):**
  - Serta Simmons: uptier closed 22 June 2020 (VERIFIED, remand opinion); Chapter 11 filed 23 January 2023, S.D. Tex. Case 23-90020 (VERIFIED, Jones Day memo and opinion caption); plan confirmed 14 June 2023, effective ~29 June 2023 (VERIFIED, Jones Day / remand). Interval ≈31 months.
  - Mitel: uptier October 2022 (VERIFIED, Paul Weiss memo 10 Jan 2025); Chapter 11 filed 10 March 2025, S.D. Tex. Case 25-90094 (lead 25-90090, 9 Mar 2025) (VERIFIED, CourtListener dockets; Jones Day); prepackaged plan confirmed April 2025 (VERIFIED via Mayer Brown May 2025, date-level CHECK). Interval ≈29 months.
  - Incora / Wesco Aircraft: 2022 notes transaction (March 2022, CHECK on month); Chapter 11 filed 1 June 2023, S.D. Tex. Case 23-90611, with adversary 23-03091 *Wesco Aircraft Holdings v. SSD Investments Ltd.* filed the same day (VERIFIED, CourtListener). Judge Isgur's 2024 ruling that the 2022 transaction breached the indenture: **CHECK** date and holding (commonly reported as July 2024).
  - Robertshaw: Chapter 11 filed 15 February 2024, S.D. Tex. Case 24-90052; adversary 24-03024 with Invesco Senior Secured Management as defendant, terminated 1 July 2026 (VERIFIED, CourtListener). The 2023 LME and Judge Lopez's June 2024 ruling: **CHECK**.
  - Del Monte Foods: Chapter 11 filed 1 July 2025, Bankr. D.N.J. lead Case 25-16984 (VERIFIED, CourtListener); adversary 26-01018 filed 23 January 2026 with "Members of the Ad Hoc Term Lender Group" and "Certain Members of the Ad Hoc Group of Minority Secured Lenders" as parties (VERIFIED); *Ad Hoc Group of Minority Secured Lenders v. Del Monte Foods Corp.*, D.N.J. 3:26-cv-02379, filed 6 March 2026 (VERIFIED); bankruptcy appeal 3:26-cv-06259 filed 28 May 2026 (VERIFIED). The 2024 LME (reported as an August 2024 non-pro-rata financing): **CHECK** all deal terms.
  - Envision (Apr 2022 LME → May 2023 Ch 11), Revlon (2020 BrandCo → June 2022 Ch 11), J.Crew (Dec 2016 drop-down → May 2020 Ch 11): all **CHECK**; useful for the ledger if confirmed.
- **Baker McKenzie, *In the Know: Leveraged Finance Annual Report 2026* (Jan 2026):** "there was also an increase in repeat restructurings, with some deals effectively being recapitalizations in disguise, often including a partial equity element." VERIFIED (PDF text extracted), https://www.bakermckenzie.com/en/insight/publications/2026/01/-/media/files/insight/publications/2026/01/lev-fin-annual-report-2026.pdf.

### 6.3 Recovery compression / bimodalization

- **Fitch (2024 emergences), via PitchBook:** weighted-average first-lien recovery 23% for issuers that had done an LME vs. 53% for those that had not; single-tranche first-lien lenders recovered 56% vs. 35% in multi-tranche structures, a reversal of the usual pattern; non-participating LME lenders fared worst. **CHECK** (search summary; https://pitchbook.com/news/articles/lmes-impaired-first-lien-debt-recoveries-in-2024-bankruptcies-fitch-report returned 403).
- **Fitch (2023 emergences), via CreditSights:** issuers with pre-filing LMTs averaged 47% first-lien recovery vs. 57% without; Serta non-participating third-out lenders ≈1.5%. **CHECK**.
- **Fitch, 2025:** "Recovery prospects for U.S. broadly syndicated loan first-lien instruments weakened in 2025," middle-market first-lien expectations concentrated in RR3 (Fitch post on X; no numbers). **CHECK**.
- **Serta remand opinion, 7 July 2026 (Bankr. S.D. Tex., Adv. 23-09001, Doc. 742, 48 pp.):** VERIFIED from the opinion text. Class of First Lien Term Loans ≈\$1.887bn; Participating Lenders ≈\$992mm (52.6%), Plaintiffs ≈\$895mm (47.4%); participants exchanged into ≈\$734mm of First Lien Second Out super-priority at \$0.74 per dollar ("the 26-cent discount"); but-for ratable share $734\times47.43\%=\$348$mm; damages measured as of the 22 June 2020 breach date: but-for value ≈\$484.88mm vs. actual ≈\$223.75mm (\$895mm at a \$0.25 price) ⇒ **\$261.13mm**, plus prejudgment interest at 9.00% per annum from 22 June 2020 to 7 July 2026, allocated severally by each defendant's holdings; one plaintiff's damages halved per a May 2023 stipulation. Defendants' mitigation expert (Austin) testified up to \$186mm face of First Lien Term Loans traded between June 2020 and 31 Dec 2021 and constructed but-for sales of \$62–94mm (29–43% of observed volume); the court recited Bloomberg chats with the Barclays market maker. Serta itself won summary judgment in November 2025 on discharge grounds (Mayer Brown, July 2026, VERIFIED). Trial held March 2026.
- **Long-run regime data (shelf):** Moody's 1970–2002Q2 mean recovery 27.85% in recessions vs. 43.10% in expansions (Schmid p.103); Baa 1990–2009 average recovery 44.6% (Ben Dor p.297); 40% convention (Dynkin p.354).

### 6.4 Cooperation agreements

- **Counts:** "around 45 co-op agreements were entered into in the US in 2024, up from an average of just four a year between 2018-2023," a statistic 9fin notes was cited in the original Optimum antitrust complaint. VERIFIED: 9fin, *A crash course on co-ops* (lesson 1 of 5; undated, ©2026), https://www.9fin.com/insights/cooperation-agreement-crash-course.
- **Seaton, Brett (Wharton), *The Value and Legality of Lender Cooperation Agreements*.** Harvard Law School Bankruptcy Roundtable, 14 April 2026 (VERIFIED): variants = offensive, defensive (origin: SpectraSite), carve-out (fastest-growing; allows disparate treatment such as backstop fees and advantaged exchange ratios); borrower countermeasures = anti-cartel provisions (Warner Bros. Discovery 2025 bonds) and NDAs, which "met significant market resistance"; equity reacts negatively immediately, firm value rises modestly, debt mixed. SSRN abstract 5247506 (URL from search listing; page 403 on fetch) reports no significant CARs overall and significant negative equity returns in weeks +1 to +2 (CHECK the magnitudes). https://bankruptcyroundtable.law.harvard.edu/2026/04/14/the-value-and-legality-of-lender-cooperation-agreements/
- **Optimum/Altice antitrust suit:** *Optimum Communications, Inc. (f/k/a Altice USA) and CSC Holdings v. the Co-op Lenders*, S.D.N.Y.; Sherman Act price-fixing (steering committee negotiates for all) and group boycott (no transacting with Optimum without supermajority approval); treble damages and a declaration the co-op is void; alleges Co-op Lenders hold 88% of the "Leveraged-Finance Market." Defenses canvassed: no per se violation, rule of reason, market definition ignores other capital (including the ABL Optimum later obtained), *Sharon Steel v. Chase Manhattan* (2d Cir. 1982) ("collective activity reduces... the costs of borrowing"). VERIFIED: Cleary Gottlieb, *Cooperation, Not a Cartel*, 18 December 2025 (Brody, Calsyn, Cooper, Kay, O'Neal, Reinker, Weinberg). Filing date and docket number: **CHECK**.
- **PitchBook, *Co-ops offer 'false sense of security' against LMEs*:** names large groups at Dish, Bausch Health, Altice. **CHECK** (403).
- **Europe:** "a growing backlash against cooperation agreements" in 2025; contentious cases Victoria PLC, Ardagh, Selecta, Hunkemöller, where "non-pro rata LMEs sidestepped sacred rights using intercreditor clauses, slim majority thresholds, and distressed disposals"; new documentation "typically contains 'LME blockers' or cooperation agreements"; prediction that "new LME solutions will be coming in 2026." VERIFIED: Baker McKenzie LevFin Annual Report 2026.
- **Parikh, Samir D., *Creditors Strike Back: The Return of the Cooperation Agreement*, 73 Duke L.J. Online 1 (2023).** Citation VERIFIED (cited in the Fifth Circuit opinion, which also quotes Parikh calling uptiers "acts of financial war").

### 6.5 Court rulings 2024–2026 (Docket Diary material)

- **Serta, Fifth Circuit, 31 Dec 2024** (*Excluded Lenders v. Serta Simmons Bedding*, No. 23-20181 c/w 23-20363, 23-20450, 23-20451; revised 21 Jan 2025 and 14 Feb 2025). VERIFIED from opinion text (https://www.ca5.uscourts.gov/opinions/pub/23/23-20181-CV0.pdf; CourtListener /opinion/10306402/). Facts recited: 2016 first-lien agreement \$1.95bn (plus \$450mm second lien per Duane Morris); 2020 Uptier: \$200mm new money first-out super-priority; \$1.2bn of first- and second-lien loans exchanged into ≈\$875mm second-out super-priority (first lien at 74, second lien at 39 per Jones Day). Holdings: (i) an "open market purchase" requires a market "generally open to participation by various buyers and sellers," here "the secondary market for syndicated loans"; privately negotiated exchanges with a subset of lenders fall outside; (ii) equitable mootness does not bar review; (iii) the plan "settlement indemnity" is an end-run around §502(e)(1)(B) and violates §1123(a)(4), excised. Quotable: "The 2020 Uptier was the first major uptier... But it was far from the last"; "such exceptions will often not justify an uptier." Scholarship the court relies on (all citations VERIFIED from the opinion): Buccola & Nini, *The Loan Market Response to Dropdown and Uptier Transactions*, 53 J. Legal Stud. 489 (2024); Buccola, *Efficacious Answers to the Non-Pro Rata Workout*, 171 U. Pa. L. Rev. 1859 (2023); Buccola, *Sponsor Control*, 90 U. Chi. L. Rev. 1 (2023); Dick, *Hostile Restructurings*, 96 Wash. L. Rev. 1333 (2021); Lubben, *Holdout Panic*, 96 Am. Bankr. L.J. 1 (2022); Sunuu, S&P Global Ratings, 15 June 2021. Lower-court history: bankruptcy court partial summary judgment 28 March 2023 holding "open market purchase" unambiguous; confirmation 14 June 2023; direct appeal certified 26 July 2023. Law-firm memos VERIFIED: Jones Day (Mar 2025), DLA Piper (14 Jan 2025), Sidley (17 Jan 2025), Duane Morris (3 Feb 2025), Proskauer (2 Jan 2025), Paul Weiss (10 Jan 2025), ABI/Restructuring GlobalView (Jan 2025), Mayer Brown (May 2025; July 2026).
- **Mitel, N.Y. App. Div. 1st Dep't, 31 Dec 2024** (*Ocean Trails CLO VII v. MLN TopCo Ltd.*, 2024 NY Slip Op 06660, Index No. 651327/23; CourtListener /opinion/10309794/; Paul Weiss cites 2024 WL 5248898). Facts (Paul Weiss, VERIFIED): October 2022; participating majority lenders provided ≈\$156mm new-money super-priority first-out and exchanged first-lien loans into second-out at a 5% discount and second-lien loans into third-out at an 18% discount; excluded lenders not invited. Holding: the undefined "purchases" exception (no "open market" qualifier) was unambiguous and satisfied; consideration could be new loans rather than cash; subordination was only an *indirect* effect on the excluded lenders' loans so sacred rights were not triggered; implied-covenant, tortious-interference, and fraudulent-transfer claims dismissed; economic-interest defense available to the sponsor. Mitel filed Chapter 11 on 10 March 2025 anyway.
- **Serta remand damages, Bankr. S.D. Tex., 7 July 2026**: see §6.3. The Mayer Brown write-up calls it a "landmark damages ruling" (VERIFIED, https://www.mayerbrown.com/en/insights/publications/2026/07/serta-simmons-bedding-the-fifth-circuits-uptier-decision-and-the-landmark-damages-ruling-on-remand).
- **Incora (Isgur, 2024)** and **Robertshaw (Lopez, 2024)**: docket facts VERIFIED (§6.2); holdings **CHECK**.
- **Del Monte (2025–2026)**: dockets VERIFIED (§6.2); substance **CHECK**. Writer should describe it as "lender-group litigation following the 2024 financing and the July 2025 filing" until the complaint is read.
- **CPPIB Credit Investments II Inc. v. Deutsche Bank Trust Co. Americas, 2026 NY Slip Op 50460(U) (Sup. Ct. N.Y. Cnty., 17 March 2026), Index No. 654398/2024**: appears in a CourtListener full-text search for "uptier"; parties include many BlackRock-managed funds, Starz Entertainment (f/k/a Lions Gate Entertainment) and Starz Capital Holdings. Likely a noteholder-vs-trustee dispute over a 2024 Lions Gate/Starz exchange. **CHECK** before using; a 2026 New York ruling on exchange mechanics would be valuable for §14.6.
- **LCM XXII Ltd. v. Serta Simmons Bedding (S.D.N.Y. 2022)** cited in the Fifth Circuit opinion as the pre-bankruptcy New York action; state-court injunction denied in June 2020 (VERIFIED via remand opinion background).

### 6.6 2026 trend data

- **9fin, *H1 2026 LME update: equity handovers eclipse coercive uptiers*, 28 Aug 2026:** "9fin logged 25 completed LMEs in the first half of 2026," marginally ahead of 24 in H1 2025; "equity handovers and consensual amend-and-extends now dominate"; coercive uptier structures "that defined 2025" have "all but vanished." VERIFIED: https://www.9fin.com/insights/h1-2026-lme-update (full breakdowns paywalled).
- **9fin, *BDC Watchlist and Non-Accrual reports Q2 26*, 30 Sep 2026:** ≈118 names, ≈\$4.19bn exposure (VERIFIED title/summary; https://www.9fin.com/insights/bdc-watchlist-and-non-accrual-reports-q2-26).
- **FTI Consulting, *2026 Leveraged Loan Market Survey*, 17 Feb 2026** (bank and non-bank lenders surveyed 18 Nov–19 Dec 2025): 58% expect loan defaults/workouts to increase slightly and 19% substantially (77% total, vs. 50% a year earlier); top distress sectors Retail & Consumer, Restaurants, Healthcare. VERIFIED: https://www.fticonsulting.com/insights/reports/2026-leveraged-loan-market-survey.
- **Federal Reserve FEDS Notes (VERIFIED URLs):** *Private Credit and Leveraged Loan Markets: Similarities, Differences, and Substitution*, 11 Aug 2026, https://www.federalreserve.gov/econres/notes/feds-notes/private-credit-and-leveraged-loan-markets-similarities-differences-and-substitution-20260811.html; *The Price of Bank Funding Behind Private Credit: Evidence from BDCs*, 7 Aug 2026; *Introducing Private Credit into the Financial Accounts of the United States*, 16 Oct 2026. Contents not read; use for Ch 17 cross-reference and the private-credit DE discussion.
- **Moody's baseline:** speculative-grade default rate drifting toward 3.2% by year-end 2026; GDP ≈1.5% (VERIFIED, May 2026).

### 6.7 Academic and modeling literature

- Franks & Torous (1994), *A comparison of financial recontracting in distressed exchanges and Chapter 11 reorganizations*, JFE 35:349–370 (citation VERIFIED via Schmid p.373).
- Altman & Karlin (2009), *The Re-emergence of Distressed Exchanges in Corporate Restructurings*, Journal of Credit Risk — TITLE-ONLY (CHECK volume/issue).
- Altman, Brady, Resti & Sironi (2005), *The Link between Default and Recovery Rates: Theory, Empirical Evidence, and Implications*, Journal of Business 78(6) — DOI 10.1086/497044 resolves (VERIFIED redirect to JSTOR).
- Jankowitsch, Nagler & Subrahmanyam (2014), *The determinants of recovery rates in the US corporate bond market*, JFE — DOI 10.1016/j.jfineco.2014.06.001 resolves (VERIFIED redirect).
- Fine & Gray (1999), *A proportional hazards model for the subdistribution of a competing risk*, JASA 94(446) — DOI 10.1080/01621459.1999.10474144 resolves (VERIFIED redirect).
- Ellias & Stark (2020), *Bankruptcy Hardball*, 108 Cal. L. Rev., DOI 10.15779/Z38K35MF1Z (VERIFIED page: https://www.californialawreview.org/print/bankruptcy-hardball); cases discussed include PetSmart, Cumulus, Forest Oil/Sabine, Colt.
- Buccola & Nini (2024), J. Legal Stud. 53:489 (VERIFIED citation): documents the rise of "uptier blockers" after 2020 and that many contracts still carry open-market exceptions.
- Frye (2000) *Collateral Damage*; Hu & Perraudin (2002); Bakshi, Madan & Zhang (2001); Gupton & Stein (2002, 2005) LossCalc; Schuermann (2004) *What Do We Know About Loss Given Default?* — all TITLE-ONLY (shelf-cited via Schmid pp.102–103 and Bohn–Stein).
- Hamilton (1989) regime switching, Econometrica; Boag (1949) and Farewell (1982) cure models; Aalen & Johansen (1978) — TITLE-ONLY standard references.
- Seaton (2025/26) SSRN 5247506 — VERIFIED-URL via search listing, content via HBRT.

---

## 7. Case studies

### Case 1: Serta Simmons Bedding, 2020 → 2026 (the whole regime in one name)
- 2016: \$1.95bn first-lien TL, \$450mm second lien (Duane Morris, VERIFIED).
- 22 June 2020: uptier closes; \$200mm new first-out; ≈\$1.2bn exchanged into ≈\$875mm second-out (first lien at 74, second lien at 39); majority held ≈52.6% of the first-lien class (remand opinion). Excluded lenders' loans marked at ≈\$0.25 at closing (remand).
- June 2020: NY state court denies injunction (remand background); 2022: second suit (Jones Day).
- 23 Jan 2023: Chapter 11, S.D. Tex.; 28 Mar 2023 partial SJ for Serta ("open market purchase" unambiguous); 14 Jun 2023 confirmation; plan cut debt from ≈\$1.9bn to ≈\$315mm (Duane Morris, CHECK); effective 29 June 2023.
- 31 Dec 2024: Fifth Circuit reverses; indemnity excised.
- Nov 2025: Serta gets SJ on discharge; Mar 2026 trial; 7 Jul 2026: \$261.13mm damages + 9% from 22 Jun 2020 (≈6 years of 9% simple interest ≈ 54% on top, *approx.*).
- Systematic read: the coalition mixture (§3.4) with $\pi=0.526$; the excluded-lender claim became a litigation asset whose best-performing component was New York's statutory interest rate. Flagging signals: 2020 RFQs in the loan ahead of the deal; Rule 2019 group formation; price gap between participating and excluded paper.

### Case 2: Mitel Networks, 2022 → 2025 (win the case, lose the credit)
- Oct 2022 uptier: ≈\$156mm new money; exchanges at 5% (1L) and 18% (2L) discounts (Paul Weiss, VERIFIED).
- 31 Dec 2024: 1st Dep't dismisses excluded lenders' claims: "purchases" exception unambiguous; subordination only indirect.
- 10 Mar 2025: Chapter 11 (S.D. Tex. 25-90094); prepack confirmed April 2025 (CHECK date).
- Lesson: legal validity of the LME and the re-default hazard are nearly independent; the uptier bought ≈29 months. Use it to motivate the cure model: Mitel was in the "susceptible" 25%.

### Case 3: Del Monte Foods, 2024 → 2026 (the fast clock) — facts CHECK beyond dockets
- 2024 non-pro-rata financing (reported Aug 2024) → Chapter 11 1 July 2025 (D.N.J. 25-16984) → adversary between the Ad Hoc Term Lender Group and minority secured lenders filed 23 Jan 2026 → district-court action 6 Mar 2026 → appeal 28 May 2026 (all docket dates VERIFIED).
- Interval LME→filing ≈11 months, well inside Moody's two-year window. Writer must fetch the first-day declaration (EDGAR will not have it; use the claims agent or PACER/RECAP) before stating amounts.

(Optional Case 4, light touch to avoid duplicating Ch 13: Incora, March 2022 → 1 June 2023, ≈15 months.)

---

## 8. Humor beats (all riding on a correct idea)

1. **Cold open, Mags:** "It's not immune. It's on parole." Teaches: a DE moves the issuer to a transient state with its own hazard, not to an absorbing one (Bolder p.682 contrast).
2. **Kaz vs. legal vocabulary:** Kaz hears "selective default" and asks whether the issuer gets to pick which quarter. Later: "soft default" is "a default with a bedside manner." Teaches: SD is an S&P rating state; soft/hard is Moody's Analytics' event taxonomy.
3. **"Open market purchase," the three most expensive words:** the Fifth Circuit priced them at \$261.13mm plus 9% simple interest for six years. Mags: "The best-performing tranche in the Serta capital structure was New York CPLR interest." Teaches: litigation claims are a recovery component with their own duration.
4. **ROBO literalism (spec box):** "Exclude distressed exchanges from the default rate" → ROBO reports 2.1% and declares the cycle over. Teaches: the dual default rate; always carry $\lambda_H$ and $\lambda_D$ separately.
5. **Cooperation-agreement counter:** when the chapter reaches the 45-in-2024 statistic, the Ad Hoc Group speaks in unison: "We are represented by counsel. We have signed a cooperation agreement. We decline to transact with the Company on a non-pro-rata basis." "(Cooperation agreements signed in this book so far: N+1.)" Then Optimum sues them for being a cartel. Teaches: commitment devices have antitrust exposure.
6. **Ines's Poker Table:** Moyer p.86 literally says the distressed market is a multi-hand poker game with credible bluffs. Ines: "A co-op is the table agreeing not to be bluffed. The sponsor's response is to find a new table." Hand history: the excluded lenders' 2020 markouts.
7. **The 13-week model, reborn:** an amend-and-extend that adds no new money "moves the cliff three years right and leaves the car in the same gear"; the re-default hazard covariate is runway, not maturity date. Theo's USB stick is now a column in the hazard regression.
8. **Two humps, not one bell:** "A 40% average recovery with a 25-point standard deviation isn't a distribution, it's two distributions that were introduced at a conference." Teaches: between-group variance $\pi(1-\pi)(\Delta\mu)^2$.
9. **Mags's "back in my day":** "We used to call it a coercive exchange and it needed 90% to work. Now it needs 50.1% and a dictionary." (Moyer p.87 threshold vs. bare-majority uptier.) Followed by grudging respect for the Fifth Circuit's reading of "open market."
10. **"IDO or it didn't happen":** "Knowing DEs are 65% of defaults is beta. Knowing which 52.6% of the class you're in is alpha." Place at the end of 14.9.

---

## 9. Resource-graph candidates

**Podcasts**
- *Cloud 9fin* (9fin's podcast; episode "Shall I compare thee to an English restructuring?", 14 Oct 2026) — VERIFIED title via 9fin insights listing; no episode URL captured → TITLE-ONLY.
- *Bloomberg Odd Lots* episodes on creditor-on-creditor violence and LMEs — TITLE-ONLY, **CHECK** exact titles/dates before citing (Apple Podcasts page fetch did not surface them).
- *Petition* (petition11.com) — site VERIFIED (archive at https://www.petition11.com/archive); specific LME posts not captured → cite the site root only.

**Practitioner writing (VERIFIED-URL unless noted)**
- Moody's AMR, 6 Mar 2025; 7 Aug 2025; 28 Apr 2026; 18 May 2026 (URLs in §6).
- 9fin, co-op crash course; H1 2026 LME update; BDC watchlist Q2 26 (URLs in §6).
- Cleary Gottlieb, *Cooperation, Not a Cartel* (18 Dec 2025) — VERIFIED-URL.
- Harvard Law School Bankruptcy Roundtable, Seaton (14 Apr 2026) — VERIFIED-URL.
- Law-firm memos on Serta/Mitel: Jones Day, DLA Piper, Sidley, Duane Morris, Mayer Brown (×2), ABI feed item — VERIFIED-URL (listed in §6.5).
- Baker McKenzie LevFin Annual Report 2026 — VERIFIED-URL (PDF).
- FTI 2026 Leveraged Loan Market Survey — VERIFIED-URL.
- PitchBook/LCD Fitch-recovery article and co-op "false sense of security" piece — TITLE-ONLY (403).
- S&P Global Ratings DE/repeat-defaulter notes (Apr, Jun, Aug, Oct 2024; Mar 2025) — TITLE-ONLY (403).

**Academic papers**
- Buccola & Nini (2024) 53 J. Legal Stud. 489 — VERIFIED citation, no URL.
- Buccola (2023) 171 U. Pa. L. Rev. 1859; Buccola (2023) 90 U. Chi. L. Rev. 1; Dick (2021) 96 Wash. L. Rev. 1333; Lubben (2022) 96 Am. Bankr. L.J. 1; Parikh (2023) 73 Duke L.J. Online 1 — VERIFIED citations via the Fifth Circuit opinion, no URLs.
- Ellias & Stark (2020) — VERIFIED-URL.
- Altman et al. (2005), Jankowitsch et al. (2014), Fine & Gray (1999) — DOIs VERIFIED to resolve.
- Franks & Torous (1994) — VERIFIED citation via shelf.
- Seaton SSRN 5247506 — VERIFIED-URL (listing).
- Altman & Karlin (2009), Gupton & Stein (2002/2005), Frye (2000), Schuermann (2004), Hamilton (1989), Farewell (1982), Aalen & Johansen (1978) — TITLE-ONLY.

**Data & code**
- CourtListener REST API (canonical root https://www.courtlistener.com/help/api/) — used this session for every docket date above; v4 search endpoint works unauthenticated, opinion-text endpoint requires a token.
- Fifth Circuit opinions root https://www.ca5.uscourts.gov/ (PDF VERIFIED).
- SEC EDGAR root https://www.sec.gov/edgar for 8-Ks announcing LMEs.
- Federal Reserve FEDS Notes (URLs in §6.6).
- Moody's Default & Recovery Database, Fitch Leveraged Finance recovery studies, LCD/PitchBook default tracker, 9fin LME tracker — named as vendor datasets, no URLs.

---

## 10. Exploratory-space notes (for Edition 2+)

1. **Ch 14-B: The Re-Default Clock.** A full survival-analysis chapter: Aalen–Johansen, Fine–Gray, mixture-cure, time-varying covariates from Ch 25 (Rule 2019 filings, 8-K LME announcements), with a hand-built LME→outcome dataset (every US LME 2016–2026 with dates). Moody's 1,173-borrower study gives the target moments; the book should assemble a public replica from dockets.
2. **Ch 14-C: Cooperation Agreements as Repeated Games and Cartels.** Threshold games, transfer restrictions as flow control, the carve-out co-op as a mechanism-design response to free riding, and the antitrust frontier (Optimum v. Co-op Lenders; *Sharon Steel*). Needs the complaint and any 2026 motion-to-dismiss ruling.
3. **Ch 13-B: The Documentation Arms Race as a Time Series.** Serta blockers, J.Crew/Chewy/Envision/Pluralsight blockers, anti-co-op "anti-cartel" clauses (WBD 2025), tracked as adoption curves by vintage (Buccola & Nini 2024 is the seed). This is the docs-vintage factor for Ch 9.
4. **Ch 24 cross-section: DE ≠ credit event.** The ISDA restructuring-clause wedge under North American No-R; what CDS actually prices in an LME regime; orphaning and succession events after drop-downs. Possibly its own section in Ch 24 rather than a new chapter.
5. **Ch 17-B: Measuring Default in Private Credit.** Moody's proxy (1.6% vs 4.7%), BDC non-accruals and PIK toggles (9fin Q2 26: ≈118 names, ≈\$4.19bn), the Fed's 2026 FEDS Notes on private credit vs. leveraged loans. A systematic desk can arbitrage the public/private definitional gap.
6. **European LMEs and the Part 26A / WHOA toolkit.** Victoria PLC, Ardagh, Selecta, Hunkemöller, Altice France, Intrum; cross-class cramdown as a different regime for $(\tau,R)$; the 2025 European co-op backlash.
7. **The 2026 "consensual turn."** 9fin: coercive uptiers "all but vanished" in H1 2026 while equity handovers dominate. Is this a durable regime switch (courts + blockers) or a cyclical pause? Track quarterly; this is exactly the Hamilton-filter use case and belongs in the Trend Tracker (App C).
8. **Litigation claims as a recovery tranche.** Serta's \$261mm plus 9% is a six-year zero-coupon with judicial optionality; a section on valuing and trading excluded-lender claims (and litigation finance in restructurings) would be new to the shelf.
9. **Recovery by coalition membership: a dataset chapter.** Collect, for every LME since 2016, the participating vs. excluded recovery outcomes at emergence; estimate $(\pi,\mu_{in},\mu_{out})$ by year and by LME type. This would be the book's most-cited table if built.
10. **Prediction markets and insolvency (HBRT, 13 Oct 2026, Organek & Packin).** An oddity worth a Trend Watch in Ch 26 or 28: market-implied bankruptcy probabilities from prediction venues vs. CDS and our hazard models.
