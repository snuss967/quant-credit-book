# Advisor Brief — Chapter 5: Probability Distributions in Distressed & High-Yield Credit

*Fable advisor dissection for Edition 1. Target file: `book_src/05_ch05_credit_probability_distributions.md`. Research date: 2026-10-17. Web-search budget was exhausted mid-session; everything below marked VERIFIED was fetched or read directly this session, everything marked CHECK came from a search summary or a secondary aggregator and must be confirmed against the named primary before it is stated as fact.*

---

## 1. Thesis and the "aha" for an ex-PJT-RSSG reader

**Thesis.** A high-yield bond's return is not a noisy number; it is a *mixture*: with probability $1-q$ the bond survives and its return is a small, nearly Gaussian spread wiggle plus carry; with probability $q$ it jumps to recovery. Everything strange about credit distributions (negative skew, enormous kurtosis, bounded price support, "fat" tails that are really a second mode) falls out of that two-line sentence, and the recovery leg is itself a bounded random variable that a Beta distribution describes well *only after you condition on collateral, seniority, debt cushion, and, since 2020, whose side of the cooperation agreement you were on.* Lévy and jump-diffusion processes are the continuous-time grammar for the jump; extreme-value theory is the right tool for *unbounded* objects (spread changes, index and ETF losses) and the wrong tool for a single bond whose loss is capped at 100 points.

**The aha for the RSSG reader.** You have been building recovery distributions for years and calling them "waterfalls." Moyer's Table 10-9 (Moyer p.251) is a recovery *function*: pick an EV multiple, run the absolute-priority waterfall, read off recovery per class. The quant's Beta recovery model is the same object with one extra step: put a probability distribution on the EV multiple and integrate the waterfall over it. Moody's did exactly this in 2006 — firm-wide recovery drawn from a Beta on $[0, 120\%]$ of liabilities with mean 50.21% and standard deviation 26.46%, then pushed through the priority-of-claims waterfall (Moody's LGD methodology, Aug 2006, VERIFIED). Your 13-week cash-flow model is the physical-measure hazard rate for the next quarter (running gag #1 lands here: weeks-of-liquidity is $\Pr(\tau \le 13\text{ weeks})$ wearing a spreadsheet). The thing the RSSG seat gives you that a PhD lacks is the *conditioning set*: you know which covenant flags move the Beta's mean, and you know that "first lien" on a loan-only, cov-lite, sponsor-backed structure with 75%+ of the debt stack pari passu is a label, not a cushion.

Three memorable results the chapter should hang on the wall:

1. **Skew is minus one over root PD.** For a pure survive-or-jump mixture, skewness is $-(1-2q)/\sqrt{q(1-q)}\approx -1/\sqrt{q}$ and excess kurtosis is $\approx 1/q$. A 1% default probability gives skew $\approx -10$ and excess kurtosis $\approx 100$. Kaz's Gaussian has skew 0 and a résumé.
2. **Recovery is U-shaped, not bell-shaped.** Ultimate recoveries pile up at 0 and 100 (Bohn–Stein p.297: "recovery can be an all-or-nothing process"). Method-of-moments Betas fit to Moody's long-run senior-unsecured moments come out with $a<1$ (spike at zero); fit to first-lien loans they come out with $b<1$ (spike at par). The LME era adds a third spike: Serta's plan put participating lenders at 73.7–100% and non-participants at 0.6–2.4% (VERIFIED).
3. **"40% recovery" is a conversion convention, not a forecast.** It is the number the CDS standard model uses to turn spreads into upfronts (Dynkin p.354 calls it "a representative average"); the physical, instrument-level distribution has a standard deviation around 27 points (Schmid p.103) and a mean that has been falling for first-lien loans for a decade (§6).

---

## 2. Section outline (7,000–10,000 words)

Anatomy key: **DF** desk framing · **DER** derivation · **SPEC** AI-coder specification · **SRC** source extraction · **CASE** case study · **RG** resource graph.

**Cold open (≤400 words).** Theo's first risk report on the new desk: a B3 bond with 4.1% annualized vol "and therefore" a 1-in-10,000 chance of losing 15 points. Mags: "It loses 55 points, once, and the model calls that a seven-sigma event every eighteen months." Kaz: "Let's just assume Gaussian." Ines: "What's the pot, and what are the odds the pot is 2.4 cents?" Question the chapter answers: *what is the right shape for a credit return, and how do you specify it so ROBO cannot build the wrong one?*

**5.1 One Bond, Two Worlds: The Survive-or-Jump Mixture.** DF (Ines's pot odds; Mags on seven-sigma Tuesdays) · DER (mixture moments; Bernoulli limit; the $-1/\sqrt{q}$ result; DTS-scaled survival leg) · SPEC (`mixture_moments` + seeded MC check) · SRC (Bohn–Stein p.513, p.18; Man 2022 p.26) · RG.

**5.2 Price, Spread, Return: Three Distributions That Are Not the Same.** DF (the trader quotes price, the PM hedges spread, the investor eats return) · DER (bounded price support $[R, K_{\text{call}}]$, negative convexity cap on the right, recovery floor on the left; right-skewed spread vs left-skewed return; lognormal-ish spreads from DTS proportionality) · SRC (Dynkin p.426; Veronesi p.669; Schmid p.280) · **Trend Watch #1: dispersion** (HY OAS 323 bp vs CCC OAS 1,278 bp on 2026-10-15, FRED VERIFIED; what a 4:1 ratio says about where the mixture weight sits).

**5.3 Jumps in Continuous Time: Merton, Kou, and the Short End.** DF (Dynkin p.465: JTD prices to recovery "with little relationship to the maturity") · DER (Merton 1976 compound-Poisson mixture density; Kou double-exponential; memoryless overshoot gives recovery-given-jump in closed form; short-maturity spread limit $\lambda^{\mathbb{Q}} p_{\downarrow}(B/V)^{\eta_2} L$) · SPEC (jump simulator with analytic check) · SRC (Bohn–Stein p.182; Bolder p.45) · RG.

**5.4 Lévy Processes: What Is Useful and What Is Decoration.** DF (Kaz loves VG; Ines asks what it changes about the bid) · DER (Lévy–Khintchine in one paragraph; VG as Brownian motion on a gamma clock; NIG; moments; why infinite-activity models fit CDX option skews and daily ETF returns but cannot be calibrated from stale TRACE prints) · SRC (Bolder p.229, p.238, p.227 on tail dependence) · verdict table: *use* compound Poisson + Gaussian for single names, Kou for analytic first passage, VG/NIG for index/ETF/option surfaces; *decoration*: infinite-activity Lévy fits to single-name HY bond returns.

**5.5 Recovery as a Random Variable: Beta Models Conditioned on Collateral and Seniority.** DF (Mags: "Price is what you pay. Recovery is what you get, eventually, after the lawyers.") · DER (Beta density and moments; method of moments by seniority; Ferrari–Cribari-Neto Beta regression with logit mean; zero-one inflation; Gupton–Stein Beta-to-normal transform; Moody's family-recovery-times-waterfall construction; downturn LGD and PD–LGD correlation via a shared systematic factor; $\mathbb{P}$ vs $\mathbb{Q}$ recovery and the identification problem) · SPEC (schema + Beta-regression fit with parameter-recovery test) · SRC (Bohn–Stein p.313, p.316, p.297, p.300; Schmid p.104, p.103, p.96; Bolder p.84; Moyer p.251) · CASE (Serta: participation status as a covariate) · **Trend Watch #2: recovery compression and the death of the debt cushion** (§6 data) · RG.

**5.6 The Default Is Now a Negotiation: Distressed Exchanges, Re-Default, and Regime Mixtures.** DF (the Ad Hoc Group speaks) · DER (the "default" component is itself a mixture: hard default vs distressed exchange; DE followed by a re-default hazard; two-regime Beta with Markov switching, Bruche–González-Aguado style) · **Trend Watch #3: DE share of defaults 2022→2026** · Docket Diary (Serta 5th Cir. 12/31/2024; Mitel 1st Dep't 12/31/2024; Wesco/Incora 2025; ConvergeOne 9/25/2025) · CASE (Hertz: the right tail, $R>1$) · RG.

**5.7 Tails: Hill, Peaks-over-Threshold, and Why Single Bonds Have No Power Tail.** DF (Paleologo p.76: factor returns are heavy-tailed; momentum's left tail) · DER (Hill estimator; GPD; VaR/ES from POT; bounded support means a single bond's loss is in the Weibull domain, so EVT belongs to spreads, indices, ETFs, and portfolios; t-copula tail dependence $\lambda_U=2t_{\nu+1}\!\left(-\sqrt{(\nu+1)(1-\rho)/(1+\rho)}\right)$) · SPEC (Hill on simulated $t_3$ recovers $\alpha\approx3$; Hill on the bounded mixture misbehaves, on purpose) · SRC (Bolder p.211, p.222; Schmid p.280; Paleologo p.76) · Ways This Blows Up (Hill plot threshold choice; stale prices create fake thin tails) · RG.

**5.8 Desk Debrief** (5–8 bullets), **The Spec You Hand the Robot**, **Exercises** (3–6).

---

## 3. Derivation skeletons

### 3.1 The mixture and its moments (measure: $\mathbb{P}$ for risk, $\mathbb{Q}$ for pricing; say which)

Horizon $h$ years, full price $P_0$ per unit par, default indicator $D\sim\text{Bernoulli}(q)$ with $q = 1 - S^{\mathbb{P}}(h)$. Survival return (rates hedged, so excess-return space):

$$X = y\,h - D^{\text{spr}}\,\Delta s + \tfrac12 C^{\text{spr}}(\Delta s)^2,\qquad \Delta s \sim \text{(Gaussian or } t\text{), } \sigma_{\Delta s} = \kappa\, s \text{ (DTS scaling)}.$$

Default return $Y = R/P_0 - 1$ with $R\sim\text{Beta}(a,b)$ (plus optional point masses, §3.4). Mixture $R_h = (1-D)X + DY$. With $J \equiv \mu_X - \mu_Y$:

$$\mathbb{E}[R_h] = \mu_X - qJ,\qquad \operatorname{Var}[R_h] = (1-q)\sigma_X^2 + q\sigma_Y^2 + q(1-q)J^2,$$

$$\mu_3 = -q(1-q)(1-2q)J^3 + 3q(1-q)J(\sigma_X^2-\sigma_Y^2) + (1-q)\mu_{3,X} + q\,\mu_{3,Y},$$

$$\mu_4 = (1-q)\!\left[q^4J^4 + 6q^2J^2\sigma_X^2 + 4qJ\mu_{3,X} + \mu_{4,X}\right] + q\!\left[(1-q)^4J^4 + 6(1-q)^2J^2\sigma_Y^2 - 4(1-q)J\mu_{3,Y} + \mu_{4,Y}\right].$$

Bernoulli limit ($\sigma_X=\sigma_Y=0$): $\text{skew} = -(1-2q)/\sqrt{q(1-q)}$, $\text{exkurt} = (1-6q(1-q))/(q(1-q))$. **Error-prone spots:** (i) using $\mathbb{Q}$ default probabilities (from CDS) in a $\mathbb{P}$ risk report, which overstates $q$ by a risk-premium multiple (Bohn–Stein App. 3B maps PD to PD$^{\mathbb{Q}}$); (ii) forgetting the coupon collected before default; (iii) $J$ must use $R/P_0$, not $R$: a bond bought at 60 that recovers 40 lost 33%, not 60%; (iv) mixing excess and raw kurtosis in sanity checks.

### 3.2 Bounded price support and the three distributions

Callable bond: $P = P^{\text{straight}}(s) - C(s)$, so as $s\downarrow$, $P\to K_{\text{call}}$ and $\partial P/\partial s \to 0$ (negative convexity, same mechanism as Veronesi's prepayment cap p.338–340). At default $P\to R$. Support is $[R, K_{\text{call}}+\epsilon]$, which is why a long-horizon *price* distribution is itself Beta-shaped on a shifted interval, and why "the bond is 102 bid, what's my upside" is a question with a cap. Spread: DTS says $\sigma(\Delta s)\propto s$ (Ben Dor Ch.1), so $\log s$ is roughly homoskedastic and $s$ is right-skewed; the return is then left-skewed by $-D^{\text{spr}}$. Keep three ledgers.

### 3.3 Jump-diffusion and Lévy skeletons (measure: $\mathbb{Q}$ when pricing, $\mathbb{P}$ when simulating risk; parameters differ)

**Merton (1976).** $dV_t/V_{t^-} = (\mu-\lambda k)dt + \sigma dW_t + (e^{Y}-1)dN_t$, $Y\sim N(\mu_J,\sigma_J^2)$, $k = e^{\mu_J+\sigma_J^2/2}-1$. Log-return over $T$ is a Poisson mixture of Gaussians:

$$f(x) = \sum_{n=0}^{\infty} \frac{e^{-\lambda T}(\lambda T)^n}{n!}\,\phi\!\left(x;\ (\mu - \tfrac12\sigma^2 - \lambda k)T + n\mu_J,\ \sigma^2 T + n\sigma_J^2\right).$$

**Kou (2002) double exponential.** $f_Y(y) = p\,\eta_1 e^{-\eta_1 y}\mathbf{1}_{y\ge0} + (1-p)\,\eta_2 e^{\eta_2 y}\mathbf{1}_{y<0}$, $\eta_1>1$ for finite $\mathbb{E}[e^Y]$. Memorylessness makes first passage analytic (Kou–Wang 2003; Chen–Kou 2009 in a Leland–Toft setting). Two results the writer should derive: (a) instantaneous jump-to-default intensity with barrier $B<V$: $\lambda(1-p)(B/V)^{\eta_2}$, hence the short-maturity spread $s(0^+) = \lambda^{\mathbb{Q}}(1-p)(B/V)^{\eta_2}\,L^{\mathbb{Q}}$, non-zero (the diffusion-only Merton short spread is zero); (b) **recovery given a jump default is the barrier times an exponential undershoot**: $V_\tau = B e^{-O}$, $O\sim\text{Exp}(\eta_2)$, so $\mathbb{E}[V_\tau/B] = \eta_2/(1+\eta_2)$. Fatter downward jumps (small $\eta_2$) mean both more defaults *and* worse recoveries from the same parameter: PD–LGD correlation for free.

**Variance gamma (Madan–Seneta 1990; Madan–Carr–Chang 1998).** $X_t = \theta G_t + \sigma W_{G_t}$, $G_t\sim\Gamma(t/\nu, \nu)$. $\varphi_{X_t}(u) = (1 - iu\theta\nu + \tfrac12\sigma^2\nu u^2)^{-t/\nu}$; $\operatorname{Var}=(\sigma^2+\theta^2\nu)t$; for $\theta=0$, skew $0$ and excess kurtosis $3\nu/t$. **NIG (Barndorff-Nielsen 1997).** $\varphi(u) = \exp\!\big(iu\mu t + \delta t[\sqrt{\alpha^2-\beta^2} - \sqrt{\alpha^2-(\beta+iu)^2}]\big)$, mean $\mu+\delta\beta/\gamma$, variance $\delta\alpha^2/\gamma^3$, skew $3\beta/(\alpha\sqrt{\delta\gamma})$, excess kurtosis $3(1+4\beta^2/\alpha^2)/(\delta\gamma)$, $\gamma=\sqrt{\alpha^2-\beta^2}$. **Error-prone spots:** $\mathbb{P}$ vs $\mathbb{Q}$ parameters of the jump (the risk premium lives mostly in $\lambda$ and the jump mean); Bohn–Stein p.182 on jump-parameter instability; Bolder p.229: gamma and GIG mixing variables have no power tail, so VG/NIG give kurtosis without tail dependence; excess kurtosis of VG decays like $1/t$, so a daily fit says nothing about a quarterly horizon.

### 3.4 Beta recovery: moments, regression, inflation, conditioning, measure

Density $f(r) = r^{a-1}(1-r)^{b-1}/B(a,b)$ on $(0,1)$. $\mu = a/(a+b)$, $\sigma^2 = \mu(1-\mu)/(a+b+1)$, skew $= 2(b-a)\sqrt{a+b+1}/\big((a+b+2)\sqrt{ab}\big)$, excess kurtosis $= 6[(a-b)^2(a+b+1) - ab(a+b+2)]/[ab(a+b+2)(a+b+3)]$. Method of moments (Bohn–Stein p.315): $a = \mu\left[\mu(1-\mu)/\sigma^2 - 1\right]$, $b = (1-\mu)\left[\mu(1-\mu)/\sigma^2 - 1\right]$, feasible only if $\sigma^2 < \mu(1-\mu)$. Hand-computed illustrations from stated moments (*author's arithmetic, illustrative*): senior unsecured bonds $\mu=0.40,\sigma=0.275$ (Schmid p.103 Moody's 1970–2002Q2: mean 40.07%, s.d. 27.50%) give $a\approx0.87$, $b\approx1.30$, a density that *spikes at zero*; a first-lien loan book with $\mu\approx0.70,\sigma\approx0.30$ gives $a\approx0.93$, $b\approx0.40$, a spike at par; Moody's family recovery on $[0,1.2]$ (mean 50.21%, s.d. 26.46%) rescales to $a\approx1.68$, $b\approx2.33$, interior mode.

**Beta regression (Ferrari–Cribari-Neto 2004).** $r_i\sim\text{Beta}(\mu_i\phi, (1-\mu_i)\phi)$, $\operatorname{logit}\mu_i = x_i^\top\beta$, log-likelihood per observation
$$\ell_i = \ln\Gamma(\phi) - \ln\Gamma(\mu_i\phi) - \ln\Gamma((1-\mu_i)\phi) + (\mu_i\phi - 1)\ln r_i + ((1-\mu_i)\phi - 1)\ln(1-r_i)$$
(this is exactly the form on Bohn–Stein p.315–316). Covariates the RSSG reader can supply: seniority class, collateral coverage ratio (collateral value / claim, continuous), debt cushion (share of the stack junior to the claim), loan-only flag, cov-lite flag, sponsor flag, prior-LME flag (re-default), industry-distress indicator (Acharya–Bharath–Srinivasan 2007), trailing 12-month speculative default rate (Altman et al. 2005; Gupton–Stein's LossCalc), jurisdiction flag (Bohn–Stein p.313), and, post-2020, *participation status* in the last LME.

**Zero-one inflation (Ospina–Ferrari 2010).** $\Pr(r=0)=\pi_0$, $\Pr(r=1)=\pi_1$, continuous part $(1-\pi_0-\pi_1)\text{Beta}$; model $(\pi_0,\pi_1)$ with a multinomial logit on the same covariates. Bohn–Stein p.316 describe the two-stage probit-then-regression version. The FDIC simulation study (Li–Zhang–Zhao 2018, VERIFIED) finds that *mean* predictions are similar across OLS, fractional response, censored/two-tier gamma, inflated Beta and Beta regression, but the bimodal-aware models win "by a large margin" on the *predicted distribution*, which is what a mixture model consumes.

**Downturn LGD.** Shared factor: $\operatorname{logit}\mu_t = x^\top\beta - \kappa Z_t$ with the same $Z_t$ that drives default (Frye 2000 "Collateral Damage"); empirically annual default rates explain 51% (linear) to about 60% (log/power) of annual recovery variation (Altman et al. 2005, as summarized on Schmid p.103); Moody's recession vs expansion means 27.85% vs 43.10% (Schmid p.103 table). Markov-switching version: Bruche–González-Aguado (2010).

**$\mathbb{P}$ vs $\mathbb{Q}$ recovery.** A 30-day post-default price is a risk-neutral discounted expectation of ultimate recovery (Bohn–Stein p.300); ultimate discounted recovery is the physical realization. CDS spreads identify only $\lambda^{\mathbb{Q}}L^{\mathbb{Q}}$ (the credit triangle, Ch 6); separating them needs recovery locks or digital CDS (Berd 2005, arXiv VERIFIED) or term-structure/structural restrictions (Pan–Singleton 2008; Doshi–Elkamhi–Ornthanalai 2018). **Error-prone spots:** observations at exactly 0 or 1 give $\ell=-\infty$ in a plain Beta (ROBO returns NaN and considers the job done): inflate or squeeze $(r(n-1)+0.5)/n$; recoveries above par are real (Hertz, §7) so either cap at 1 with a $\pi_1$ mass or use a $[0,1.2]$ support as Moody's does; never pool trading-price and ultimate recoveries in one regression; RMV/RFV/RT conventions must be named.

### 3.5 Extreme-value skeleton (measure: $\mathbb{P}$)

Order statistics $X_{(1)}\ge\dots\ge X_{(n)}$ of losses; Hill (1975): $\hat\alpha_k = \Big[\tfrac1k\sum_{i=1}^{k}\ln\big(X_{(i)}/X_{(k+1)}\big)\Big]^{-1}$, tail index $\xi=1/\alpha$. Peaks over threshold $u$: $F_u(y)\approx 1-(1+\xi y/\beta)^{-1/\xi}$,
$$\text{VaR}_p = u + \frac{\beta}{\xi}\Big[\Big(\tfrac{n}{N_u}(1-p)\Big)^{-\xi}-1\Big],\qquad \text{ES}_p = \frac{\text{VaR}_p}{1-\xi} + \frac{\beta-\xi u}{1-\xi}\ (\xi<1).$$
**The point the chapter must make:** a single bond's loss is bounded by $1-R/P_0\le1$, so its tail is in the Weibull domain ($\xi<0$) and the Hill estimator on single-bond returns is measuring the jump mass, not a power law. EVT applies to spread *changes*, to index/ETF returns (HYG, JNK, CDX), and to portfolio losses, which Bolder shows are "highly skewed and heavily fat-tailed" even under a Gaussian copula (p.222), with tail dependence only under power-tailed mixing (p.227) or a $t$-copula (p.211). **Error-prone spots:** Hill-plot threshold choice (the plateau is a matter of faith); stale TRACE prices thin the empirical tail and fatten the autocorrelation; de-GARCH first (standardized residuals), then Hill.

---

## 4. Code spec: `credit_mixture_lab.py` (reference implementation, numpy/scipy/pandas, seeded)

**Inputs / schema.**
- `BondState`: `price0: float` (per 1.0 par), `coupon: float`, `spread_bp: float`, `spr_duration: float`, `spr_convexity: float`, `horizon_yrs: float`, `pd_P: float` (physical, horizon), `dts_vol_kappa: float` (annualized vol of $\Delta s/s$), `call_price: float|None`, `recovery: RecoverySpec`.
- `RecoverySpec`: `a: float, b: float, pi0: float, pi1: float, support_max: float = 1.0` (Moody's-style 1.2 allowed), `convention: {"RFV","RMV","RT"}`.
- `RecoveryPanel` (pandas): columns `issuer_id, instrument_id, default_date, seniority ∈ {1L_loan, 2L_loan, sr_sec_bond, sr_unsec_bond, sub_bond}, collateral_cov: float, debt_cushion: float∈[0,1], loan_only: bool, cov_lite: bool, sponsor: bool, prior_lme: bool, participant: {in, out, na}, industry_distress: bool, trailing_dr: float, rec_trading_30d: float|NaN, rec_ultimate_disc: float|NaN`. Never mix the last two columns in one fit; the function takes a `target` argument and refuses otherwise.

**What it computes.**
1. `mixture_moments(bond)` → closed-form mean, variance, skew, excess kurtosis from §3.1 (survival leg Gaussian in $\Delta s$ with $\sigma_{\Delta s} = \kappa s$, convexity term handled by delta-method or exact Gaussian moments; default leg Beta with inflation). `simulate_mixture(bond, n=200_000, seed=7)` → the same four moments by Monte Carlo. **Sanity check 1:** relative error of all four within 2% (kurtosis within 5%); assert.
2. `beta_mom(mu, sd, support_max)` and `beta_regression_fit(panel, target, covariates)` (scipy `minimize` on the §3.4 log-likelihood with logit mean and log precision; zero-one inflation via multinomial logit). **Sanity check 2:** generate a synthetic panel from known $(\beta,\phi,\pi_0,\pi_1)$ with seed; the fit must recover coefficients within 2 standard errors; also assert `beta_mom` raises on $\sigma^2\ge\mu(1-\mu)$.
3. `simulate_kou_jd(V0, barrier, mu, sigma, lam, p, eta1, eta2, T, dt, n, seed)` → default indicator, time, and $V_\tau/B$. **Sanity check 3:** as $T\to$ small, the simulated default rate divided by $T$ converges to $\lambda(1-p)(B/V_0)^{\eta_2}$ (tolerance 10% at $T=1/52$ with $n\ge10^6$ or antithetic), and the mean undershoot $V_\tau/B$ given a jump default $\approx\eta_2/(1+\eta_2)$.
4. `hill_estimator(x, k)` and `hill_plot_table(x, ks)`; `gpd_var_es(x, u, p)`. **Sanity check 4:** on `scipy.stats.t(df=3)` draws (seed), $\hat\alpha_k\in[2.5,3.5]$ for $k$ in the middle range; on the bounded mixture's loss sample, report that $\hat\alpha$ drifts with $k$ and flag "bounded support: EVT not applicable" when the sample maximum equals the cap within tolerance.
5. `t_copula_tail_dep(rho, nu)` vs a simulated conditional exceedance frequency at the 99.5th percentile. **Sanity check 5:** agree within Monte Carlo error; Gaussian copula result near zero.

**Edge cases and guards.** `price0` in $(0, 1.5]$; `pd_P` in $[0,1)$; Beta parameters $>0$; recoveries exactly 0 or 1 routed to inflation masses; `support_max>1` rescales before fitting; warn if `pd_P` looks risk-neutral (e.g., exceeds a user-supplied `pd_Q` bound); all randomness through `numpy.random.default_rng(seed)`. Tensor shapes: simulations are `(n,)` float64; panel fits return a `pandas.Series` of coefficients and a `(k,k)` covariance.

**"What ROBO built from the vague version."** Asked to "fit a Beta to recoveries," it fit `scipy.stats.beta.fit` to a column containing 0.0 and 1.0, got a log-likelihood of $-\infty$, returned `nan, nan`, and reported success.

---

## 5. Source map (shelf pages; quotations copied verbatim from the page text, ≤60 words)

| Page | Why | Quotation |
| :-- | :-- | :-- |
| Bohn_Stein p.313 | Beta as the LGD distribution of record | "One common approach to modeling such distributions is to posit a beta distribution as the underlying distribution for the LGD process." |
| Bohn_Stein p.297 | Bimodality of ultimate recoveries | "Note the characteristic U-shape of the ultimate recoveries, suggesting that in many cases, recovery can be an all-or-nothing process." |
| Bohn_Stein p.300 | Post-default price is a $\mathbb{Q}$ object | "When using post-default prices of recovery, either in a look-up table or through the use of a model, the predicted value is a risk-neutral measure of the expected discounted future recovery." |
| Bohn_Stein p.316 | Two-stage zero-inflated LGD | "the first stage being a discrete choice (probit) model to predict the probability of observing a loss greater than zero, given default; and the second the regression model of the actual LGD" |
| Bohn_Stein p.182 | Why desks distrust jump calibration | "The primary difficulty in implementation involves the instability of parameters governing the jump risk. The rare-event nature of credit data makes it difficult to estimate precisely the components of the jump process." |
| Bohn_Stein p.513 | The skew intuition | "There is always a large probability of relatively small losses, and a small probability of rather large losses. This skewness leads to an unintuitive result: A very high percentage of the time (say 80 percent), the actual losses will be less than the average loss (expected loss)." |
| Bohn_Stein p.514 | Sigma counts are meaningless | "for a portfolio with a skewed loss distribution there is an economically significant chance of realized losses that are six to eight standard deviations in excess of the expected loss." |
| Bohn_Stein p.18 | Chapter epigraph candidate | "Any quantitative analysis of credit begins with the skewed, non-normal return distributions typical of both individual credit exposures and portfolios of those exposures." |
| Schmid p.104 | Beta shape (note OCR spelling; quote as printed with [sic]) | "Because of the highly asymmetrie nature of recovery rate distributions (left-side peak, right-side skew) a Beta distribution is a good approximation." |
| Schmid p.103 | PD–LGD link, numbers | "They find that one can explain 51% of the variation in the annual recovery rates with the level of default rates in a linear model, and approximately 60% with logarithmic and power relationships." (table on same page: recessions 27.85%, expansions 43.10%, all 40.07%, s.d. 27.50%) |
| Schmid p.96 | Against table averages | "Typically, they are estimated by appealing to historical averages although the extreme range of the historical data makes one doubt about its use." |
| Schmid p.280 | Empirical kurtosis of spread changes | "The large values of the excess kurtosis are caused by fat tails in the probability density function. There are much more extreme events than would have been in the case of a normal distribution." (tables p.281–282: excess kurtosis 4–24 for Italy–Germany spread changes 1999–2000) |
| Bolder p.84 | Why Beta for severity | "There are many different possible distributions that might be employed, but the beta distribution is a popular choice since its support, like the default severity, is restricted to the unit interval." |
| Bolder p.45 | Default is a jump, exit is slow | "Default is a binary event. It either happens or it doesn't. Once it happens, default is also typically a permanent state. After arrival in default, exit is, in general, a slow and messy process." |
| Bolder p.227 | Tail dependence needs a power-tailed mixer | "if V possesses a power tail, then the subsequent normal-variance mixture will be positive tail dependent." |
| Bolder p.229 | VG/NIG caveat | "Since neither the gamma nor the generalized inverse-Gaussian laws possess a power tail, sadly these models do not exhibit positive tail dependence." |
| Bolder p.238 | VG shape | "The variance-gamma distribution has a very thin waist with probability mass extending far into the tails." |
| Bolder p.222 | Gaussian copula still gives fat loss tails | "even in the case of a Gaussian joint distribution for the risk factor, the loss distribution is no longer Gaussian. In fact, it is highly skewed and heavily fat-tailed." |
| Man_2022 p.26 | Asymmetry in practitioner words | "bonds tend to experience more volatility on the downside than on the upside: the tightening of a bond on the upside to risk free rates is typically asymmetrically smaller than the jump to recovery in situations of distress." |
| Man_2022 p.16 | Why construction differs in credit | "given the wide breadth of volatility and asymmetric nature of jump risk in credit, we have found credit strategies need far more refined and granular approaches to each of these layers than other asset classes." |
| BlackRock p.3 | Industry framing | "The asymmetric return profile of high yield bonds cautions most portfolio managers to position for downside risk rather than upside potential." |
| BlackRock p.6 | Default-avoidance hit rate | "successfully identified 77% of the defaulted bonds in the ICE BofA High Yield Index within 24 months of its default since 2010." |
| Dynkin p.465 | JTD and maturity | "Jump to defaults would typically trigger price to expected recovery values with little relationship to the maturity of the bond." |
| Dynkin p.400 | Stop-losses vs jumps | "Rating‐based stop‐loss rules do not protect against jump to default." |
| Dynkin p.354 | The 40% convention named | "A representative average recovery rate of 40% is assumed, such that a loss of 60% is assumed to be incurred with the specified probability." |
| Dynkin p.426 | Recovery floor and discount bonds | "bonds trading at a discount are better shielded from default risk by recovery values." |
| Moyer p.251 | Waterfall = recovery function of EV | "Again, note that the valuation assumption determines the total amount of recovery, particularly to junior classes. This should reinforce why the issue of valuation is so hotly contested in the plan negotiation." |
| Paleologo p.76 | Factor tails | "Factor returns are heavier-tailed than the norm." and "The price to pay is the risk of large, sudden losses." |
| Veronesi p.669 | Negative skew from a sold option | "the distribution is heavily negatively skewed, meaning that the probability of large losses is higher than the probability of symmetrically large gains." |
| Ben_Dor p.297 | A sourced recovery input | Table 12.1: Baa average recovery 44.6% (LGD 55.4%), 1990–2009, "From Moody's Corporate Default and Recovery Rates, 1920–2009, February 2010." |
| Houlihan_Lokey p.55 | Recovery as an auction outcome | "unsecured creditors receive 47.9 cents on the dollar" (Table 28, auction's effect on recovery; use in the Serta/363 contrast) |

---

## 6. RESEARCH DOSSIER (dated, sourced; VERIFIED = fetched/read this session, CHECK = search summary or secondary source)

### 6.1 Distressed exchanges are now most defaults (Trend Watch #3 data)

- **Fitch, 2023 Annual Manual (Mar 30, 2023), VERIFIED:** "DDEs accounted for 45% and 50% of the 2022 defaults in volume and count, respectively." Source: https://your.fitch.group/rs/732-CKH-767/images/The-2023-Annual-Manual-(A-Primer-on-the-U.S.-Leveraged-Finance-Market)_10229378.pdf
- **S&P 2024 Annual Global Corporate Default and Rating Transition Study (Mar 27, 2025), CHECK (search summary of a mirrored PDF):** 145 global defaults in 2024 vs 153 in 2023; distressed exchanges 59.3% of defaults, highest since 2008; global speculative-grade default rate 3.9%; US 5.13%; 97 of 130 rated defaulters began the year at CCC/C.
- **Moody's Analytics, US Credit Review & Outlook (July 2025), VERIFIED:** "distressed exchanges accounted for 64% of all defaults in the first half of 2025, about the same pace as all of 2024, which itself was the highest annual share on record." All-HY (bond+loan) issuer default rate 5.8% in June 2025; "Removing the 51 distressed restructurings… the high-yield default rate is almost one-third lower at 2.1%." HY bond default rate 4.2% (June 2025); projected 3.2% for 2025, above 4% by Q1 2026; leveraged-loan default rate projected 7.5% at YE2025, 7.9% Q1 2026. HY spread 286 bp on July 30, 2025 "tight given the 3.4% average PD." "the loan market exhibited the most distress, particularly borrowers with loan-only capital structures backed by private equity firms." Source: https://www.moodys.com/web/en/us/insights/resources/us-report-july-2025.pdf
- **Moody's, "Lend, extend, and then…" (May 18, 2026), VERIFIED:** ~65% of all 2025 corporate defaults were distressed exchanges. Re-default study of 1,173 borrowers with a soft credit event (1979–2026): about one in four soft events ends in a hard default; more than one in three ends in a hard default or another distressed event; "More than 70% of eventual hard defaults following a distressed restructuring occur within the first two years"; after year five the hazard adds under half a point per year. Source: https://www.moodys.com/web/en/us/insights/credit-risk/private-credit/lend-extend-and-then.html
- **Moody's via American Banker (Sept 28, 2026), VERIFIED:** Moody's "Corporate Defaults and Recoveries" (Sept 22, 2026): DEs and LMEs "roughly 70% of defaults since early 2022"; default rate 5.3% in August 2026; "recovery rates tend to decline further when issuers that executed LMEs classified as DEs subsequently re-default." Source: https://asreport.americanbanker.com/news/moodys-clos-have-prepped-for-worsening-credit-quality
- **PitchBook LCD, CHECK (search summary):** LMEs/DEs have outpaced payment defaults and bankruptcies in every rolling-12-month reading since January 2024; leveraged-loan payment default rate 1.34% by issuer count at June 30, 2026 vs 1.51% ten-year average (via kadenwoodcapital, Aug 2026).
- **Octus, "The Year in LMEs" (Jan 8, 2026), VERIFIED:** 28 uptier/drop-down/pari-plus transactions in 2025 vs 34 in 2024 vs 23 in 2023; 13 attempts to insert anti-cooperation language in 2025, 3 succeeded (Warner Bros. Discovery, Getty Images, Optimum Communications); "LME-squared" repeat names Robertshaw, Apex Tool. Source: https://octus.com/resources/articles/the-year-in-lmes/
- **Simpson Thacher, Liability Management Expresso (Feb 2025), VERIFIED:** "Covenant Review tracked over 30 transactions that involved LME elements in 2024. In contrast, less than 20 comparable LMEs were tracked in 2023." Next-generation blockers broader than Serta/Chewy/J.Crew blockers; two-tier co-ops emerging. Source: https://www.stblaw.com/docs/default-source/publications/liabilitymanagementexpresso_feb_2025.pdf
- **S&P CreditWeek (Feb 20, 2025), CHECK (paywalled; search summary):** 15 non-pro-rata loan LMTs in 2024, a record; 33% of those companies later filed for bankruptcy.

### 6.2 Recovery compression and the death of the debt cushion (Trend Watch #2 data)

- **Long-run baselines (Moody's data as reproduced by the Bermuda Monetary Authority, Sept 5, 2024), VERIFIED:** trading-price recoveries 1983–2023: 1st-lien bank loan 65%, 1st-lien bond 55%, senior unsecured bond 38%. Ultimate recoveries 1987–2023: revolvers 87%, term loans 71%, senior secured bonds 62%, senior unsecured bonds 47%. Calendar-year first-lien loan trading-price recoveries ranged ~53%–88% (1990–2023). S&P long-term US first-lien recoveries 75%–80%, "below historical averages in recent years and gradually declining"; first-lien and priority debt "more than 75% of total debt." Source: https://cdn.bma.bm/documents/2024-09-05-11-50-00-Private-Credit---Deep-dive-on-Direct-Loans-CLOs-and-Private-Placements.pdf
- **Fitch, 2023 Annual Manual, VERIFIED:** first-lien institutional leveraged loan 30-day post-default prices 2007–2022: average 59.5%, median 62.8%; emergence prices average 59.9%, median 62.5%; first-lien Recovery Ratings concentrated at RR1 (91–100%) but RR2/RR3 share rising "as companies increasingly relied on first-lien heavy structures."
- **Moody's Annual Default Study (Feb 28, 2025), CHECK (figures via ctacquisitions.com, a secondary page dated June 24, 2026):** 2024 first-lien term-loan recovery 49.2% vs 76.4% long-run (1987–2024); second lien 14.5% vs 46.5%; senior unsecured bonds 32.0% vs 37.7%; subordinated 8.5% vs 25.3%; prior first-lien years 65.7% (2020), 71.4% (2021), 58.9% (2022), 51.3% (2023). Same page: Fitch 2025 database update, 2024 sponsor-backed first-lien mean ultimate recovery 51% (non-sponsor 63%), median 41%, "lowest since Fitch's database began in 2003"; S&P 2024 sponsor-backed first-lien 53% (non-sponsor 67%), second lien 11%; Cliffwater DLI 2024 private-credit recovery 63.6%. Source: https://ctacquisitions.com/guides/pe-bankruptcy-recovery-rate-report-2020-2026/ (confirm every number against the agency primaries before printing).
- **Moody's (Sept 22, 2026 report, via American Banker), VERIFIED:** projecting "first-lien loan recoveries declining to 55%."
- **Fitch (Apr 6, 2026), CHECK:** "US first-lien recoveries fell to a ten-year low in 2025" (headline via kadenwoodcapital; figure paywalled). Fitch (June 10, 2026), CHECK: retail first-lien recoveries averaged ~49% 2016–2025 ex asset-based. Fitch on X (2026), CHECK: BSL first-lien recovery prospects weakened in 2025; middle-market first-lien expectations concentrated at RR3.
- **S&P (Aug 7, 2024), CHECK (paywalled; search summary):** first-lien recovery ratings fell to the mid-to-low 60% range over six years vs 75–80% long-term actuals; drivers higher leverage, thinner junior cushions, cov-lite.
- **Moody's LGD methodology (Aug 2006), VERIFIED:** firm-wide ultimate recovery from "over 400 US bankruptcies and distressed exchanges" has mean 50% and s.d. 26%, modeled as Beta on $[0,120\%]$ of liabilities (mean 50.21%, s.d. 26.46%); firms with very little bank debt have LGD "about 65%", all-bank-debt firms "about 35%"; regulated utilities ~35%; LGD1–LGD6 buckets (0–10, 10–30, 30–50, 50–70, 70–90, 90–100). Source (mirror): https://care-mendoza.nd.edu/assets/152347/loss-given-default-rating-methodology.pdf
- **Case-level 2024–2026 recoveries (secondary, CHECK):** Pluralsight (Aug 2024) first lien ~65c; Empire Today (Nov 2024) excluded lenders ~25–35c vs participants ~70–80c; Steward Health first-lien TL 48–58% (plan supplement, Sept 2025); Rite Aid second case first-lien TL ~14% (2025); Prospect Medical first-lien 38–45% (Mar 2026). Octus (May 11, 2026): private-credit recoveries averaging ~50c vs the ~70% "many managers had cited."

### 6.3 Private credit: the measurement problem

- **Moody's (Apr 28, 2026), VERIFIED:** 2025 private-credit default rate "likely ranged from 1.6% to 4.7%, depending on whether distressed exchanges are included"; US HY PD 3.2% (Mar 2026); private corporate lending AUM to exceed \$2tn in 2026, toward \$4tn by decade-end. Source: https://www.moodys.com/web/en/us/insights/credit-risk/private-credit/us-corporate-default-risk-in-2026.html
- **Moody's Ratings, "Risk assessments within private credit signal a 5.8% default rate" (Oct 14, 2026), VERIFIED:** 607 credit-estimate issuers across 47 middle-market CLOs, 12 months to June 2026: 24 reported defaults (4.0%); adding PIK amendments and maturity extensions for distressed issuers, 35 events (5.8%); Caa-equivalents are more than half of 2027–28 maturities. Source: https://www.moodys.com/web/en/us/site-assets/risk-assessments-within-private-credit.pdf
- **Moody's, "Beyond the maturity wall" (Sept 29, 2026), VERIFIED:** 32 BDCs, 6,570 loans, \$112.2bn principal; loans maturing in 2026 marked at 88.8% of cost vs 99.7% for 2030+; 691 loans (11%) marked below 90; 24.9% of 2026–28 maturities discounted below 95 vs 8.9% for 2029+. Source: https://www.moodys.com/web/en/us/insights/credit-risk/private-credit/beyond-the-maturity-wall.html
- **Default-rate zoo (via kadenwoodcapital, Aug 2026; each CHECK against the named primary):** Proskauer 2.51% (Q2 2026, payment/covenant only); Fitch 6.0% TTM Q2 2026, a record (full agency definition); KBRA 3.3% by count / 2.4% by debt (12m to June 2026); Fitch privately monitored portfolio 9.2% for 2025 (Mar 6, 2026); Lincoln covenant defaults 3.1% (Q1 2026). Fitch 2026 forecasts (reaffirmed July 16, 2026): leveraged loans 4.5–5.0%, HY 2.5–3.0%. Source: https://kadenwoodcapital.com/perspectives/special-situations-into-2027
- **Zou (arXiv 2603.14491, Mar 15, 2026), VERIFIED:** private credit AUM from \$158bn (2010) to nearly \$2tn (mid-2024); persistent spread premium over BSL; average fund's risk-adjusted return largely consumed by fees. Source: https://arxiv.org/abs/2603.14491

### 6.4 Spread levels and dispersion today (Trend Watch #1 data)

- **FRED, VERIFIED (Oct 15, 2026 close):** ICE BofA US High Yield OAS 3.23% (BAMLH0A0HYM2); ICE BofA CCC & Lower OAS 12.78% (BAMLH0A3HYC). A CCC/HY ratio near 4:1 with the index at ~320 bp is the mixture in one picture: the index spread is BB carry, the CCC spread is the jump leg. Sources: https://fred.stlouisfed.org/series/BAMLH0A0HYM2 and https://fred.stlouisfed.org/series/BAMLH0A3HYC
- **For the 2020 and 2022 comparisons** the writer should pull month-end values from the same FRED series rather than quote memory (the March 2020 HY OAS peak was on the order of 1,000 bp; *approximate, verify on FRED*).
- **Daily HY effective-yield moments (arXiv 2412.06193, CHECK):** skewness −0.28, kurtosis 5.74 for the ICE BofA HY effective yield, May 2014–June 2024 (raw vs excess kurtosis unclear).

### 6.5 Court rulings that moved recovery distributions (Docket Diary data)

- **Serta Simmons:** 2020 uptier of \$200mm new money plus \$850mm priority term loans exchanged for \$1bn of existing exposure; Chapter 11 filed January 2023 (S.D. Tex., Judge Jones); summary judgment March 28, 2023 that the exchange "clearly" fell within "open market purchase"; proposed plan recoveries 73.7%–100% (participating) vs 0.6%–2.4% (non-participating and other unsecureds) (Norton Rose Fulbright, Q3 2023, VERIFIED: https://www.nortonrosefulbright.com/en-us/knowledge/publications/e245aa48/liability-management-transactions). Fifth Circuit, Dec 31, 2024, 125 F.4th 555, revised Feb 14, 2025: privately negotiated exchange is not an "open market purchase"; plan indemnity for participants violated §1123(a)(4) and was excised (HSG, Dec 22, 2025, VERIFIED: https://www.hsgllp.com/about-news-Liability-Management-Exercises-and-the-Courts-in-2025).
- **Mitel** (*Ocean Trails CLO VII v. MLN Topco*, N.Y. App. Div. 1st Dep't, Dec 31, 2024, 233 A.D.3d 614): uptier was a "purchase" not requiring pro rata treatment; implied-covenant and tortious-interference claims dismissed (HSG, VERIFIED).
- **Wesco/Incora:** bankruptcy court found the 2022 transactions violated the indentures (Jan 2025; HSG says Jan 17, CreditSights deck says Jan 15, CHECK); district court (Judge Crane) reversed, oral ruling Sept 2025, written opinion Dec 8, 2025 (Octus and HSG, VERIFIED).
- **ConvergeOne** (S.D. Tex., Sept 25, 2025): exclusive equity rights offering and backstop violated §1123(a)(4) (HSG, VERIFIED).
- **Hertz:** see §7.2.
- Pending antitrust challenges to cooperation agreements: *Optimum Communications v. Apollo* (S.D.N.Y. 25-cv-9785) and *Deltroit v. Selecta* (S.D.N.Y. 25-cv-08956) (HSG, VERIFIED; allegations only).

### 6.6 Academic and methodological anchors (DOI-RESOLVES = doi.org redirected to the publisher this session; titles from memory, confirm on landing page)

- Altman, Brady, Resti, Sironi (2005), *The Link between Default and Recovery Rates: Theory, Empirical Evidence, and Implications*, J. Business 78(6):2203–2228, DOI 10.1086/497044 — VERIFIED via https://ideas.repec.org/a/ucp/jnlbus/v78y2005i6p2203-2228.html ; 2002 working paper VERIFIED at https://archive.nyu.edu/bitstream/2451/26493/2/02-49.pdf
- Jankowitsch, Nagler, Subrahmanyam (2014), *The determinants of recovery rates in the US corporate bond market*, JFE — DOI 10.1016/j.jfineco.2014.06.001 DOI-RESOLVES
- Acharya, Bharath, Srinivasan (2007), *Does industry-wide distress affect defaulted firms? Evidence from creditor recoveries*, JFE — DOI 10.1016/j.jfineco.2006.05.011 DOI-RESOLVES
- Bruche, González-Aguado (2010), *Recovery rates, default probabilities, and the credit cycle*, JBF — DOI 10.1016/j.jbankfin.2009.04.009 DOI-RESOLVES
- Altman, Kalotay (2014), *Ultimate recovery mixtures*, JBF — DOI 10.1016/j.jbankfin.2013.11.021 DOI-RESOLVES (mixture-of-Gaussians on transformed recoveries: the natural bridge between §5.1 and §5.5)
- Qi, Zhao (2011), *Comparison of modeling methods for Loss Given Default*, JBF — DOI 10.1016/j.jbankfin.2011.03.011 DOI-RESOLVES
- Calabrese (2014), *Downturn Loss Given Default: Mixture distribution estimation*, EJOR — DOI 10.1016/j.ejor.2014.01.043 DOI-RESOLVES
- Ferrari, Cribari-Neto (2004), *Beta regression for modelling rates and proportions*, J. Applied Statistics — DOI 10.1080/0266476042000214501 DOI-RESOLVES
- Ospina, Ferrari (2010), *Inflated beta distributions*, Statistical Papers — DOI 10.1007/s00362-008-0125-4 DOI-RESOLVES
- Li, Zhang, Zhao (2018), *Modeling Loss Given Default*, FDIC CFR WP 2018-03 — VERIFIED https://www.fdic.gov/analysis/cfr/working-papers/2018/cfr-wp2018-03.pdf
- Huang, Oosterlee (2011), *Generalized beta regression models for random loss given default*, J. Credit Risk — TITLE-ONLY
- Gupton, Stein (2002), *LossCalc: Moody's model for predicting loss given default*, Moody's — TITLE-ONLY (described on Schmid p.103–105 and Bohn–Stein p.314)
- Frye (2000), *Collateral Damage*, Risk — TITLE-ONLY; Frye, Jacobs (2012), *Credit loss and systematic loss given default*, J. Credit Risk — TITLE-ONLY
- Merton (1976), *Option pricing when underlying stock returns are discontinuous*, JFE — DOI 10.1016/0304-405X(76)90022-2 DOI-RESOLVES
- Kou (2002), *A jump-diffusion model for option pricing*, Management Science — DOI 10.1287/mnsc.48.8.1086.166 DOI-RESOLVES; Kou, Wang (2003) first-passage — TITLE-ONLY
- Chen, Kou (2009), *Credit spreads, optimal capital structure, and implied volatility with endogenous default and jump risk*, Mathematical Finance — DOI 10.1111/j.1467-9965.2009.00375.x DOI-RESOLVES
- Zhou (2001), *The term structure of credit spreads with jump risk*, JBF — DOI 10.1016/S0378-4266(00)00168-0 DOI-RESOLVES
- Madan, Carr, Chang (1998), *The Variance Gamma Process and Option Pricing*, European Finance Review 2(1):79–105 — DOI 10.1023/A:1009703431535 DOI-RESOLVES (redirect confirms rof 2/1/79)
- Madan, Seneta (1990), J. Business 63(4):511–524 — cited on Bolder p.256
- Barndorff-Nielsen (1997), *Normal inverse Gaussian distributions and stochastic volatility modelling*, Scand. J. Statistics — TITLE-ONLY
- Cariboni, Schoutens, *Pricing credit default swaps under Lévy models*, J. Computational Finance (year CHECK, likely 2007); Schoutens, Cariboni (2009), *Lévy Processes in Credit Risk*, Wiley — TITLE-ONLY
- Hill (1975), *A Simple General Approach to Inference About the Tail of a Distribution*, Annals of Statistics 3(5) — DOI 10.1214/aos/1176343247 DOI-RESOLVES (title in redirect URL)
- McNeil, Frey, Embrechts (2015), *Quantitative Risk Management*, 2nd ed.; Embrechts, Klüppelberg, Mikosch (1997), *Modelling Extremal Events* — books, no link
- Bai, Bali, Wen (2019), *Common risk factors in the cross-section of corporate bond returns*, JFE — DOI 10.1016/j.jfineco.2018.08.002 DOI-RESOLVES (downside-risk factor)
- Giesecke, Longstaff, Schaefer, Strebulaev (2011), *Corporate bond default risk: A 150-year perspective*, JFE — DOI 10.1016/j.jfineco.2011.01.011 DOI-RESOLVES (default clustering)
- Pan, Singleton (2008), *Default and Recovery Implicit in the Term Structure of Sovereign CDS Spreads*, J. Finance — DOI 10.1111/j.1540-6261.2008.01399.x DOI-RESOLVES
- Das, Hanouna (2009), *Implied recovery*, JEDC — DOI 10.1016/j.jedc.2009.04.005 DOI-RESOLVES
- Doshi, Elkamhi, Ornthanalai (2018), *The Term Structure of Expected Recovery Rates*, JFQA — DOI 10.1017/S0022109018000558 DOI-RESOLVES
- Berd (2005/2010), *Recovery Swaps*, J. Credit Risk 1(3); arXiv:1001.0783 — VERIFIED https://arxiv.org/abs/1001.0783 ("the fair forward recovery rate used in recovery swaps must contain a convexity premium")
- Schuermann (2004), *What Do We Know About Loss Given Default?* — TITLE-ONLY (SSRN blocked this session); the source of the four-stage timeline on Schmid p.96

### 6.7 What is still unconfirmed (hand to the writer as CHECK list)

Moody's Annual Default Study (Feb 2025 and the Feb 2026 edition) instrument-level recovery table; S&P 2024 recovery study by seniority; the exact Markit/ISDA standard-model recovery conventions (40% senior unsecured is standard; the 20% subordinated / 25% EM figures were not confirmed this session); First Brands Group 2025 facts (§7.3); Odd Lots episode titles (§9); JPMorgan 2026–27 default forecasts; CreditSights in-group vs out-group recovery data (gated).

---

## 7. Case studies

### 7.1 Serta Simmons (2020–2025): recovery conditioned on a signature

Facts (VERIFIED unless noted): 2020 uptier with \$200mm new money and \$850mm of super-priority term loans exchanged for \$1bn of existing first-lien exposure; Chapter 11 January 2023 (S.D. Tex.); summary judgment March 28, 2023 for the debtor and participating lenders on "open market purchase"; plan recoveries proposed at 73.7–100% for participants vs 0.6–2.4% for non-participants and other unsecureds; Fifth Circuit reversal Dec 31, 2024 (125 F.4th 555, revised Feb 14, 2025) on the OMP reading and the §1123(a)(4) indemnity. **How the chapter uses it:** the same first-lien tranche, same collateral, same seniority label, and two recovery distributions four orders of magnitude apart; "participant" is a covariate with a coefficient larger than seniority's. The systematic desk's flags: a credit agreement with "open market purchase" language and a simple-majority amendment threshold, a sponsor, and an ad hoc group forming (Rule 2019 statements) are features for the Priming Risk Score (Ch 13). Running gag: "open market purchase," the most expensive three words in finance. Mark dollar prices of the Serta loans as *illustrative* unless the writer sources TRACE/LCD prints.

### 7.2 Hertz (2020–2026): the right tail of recovery, $R>1$

Facts (VERIFIED via Nelson Mullins, Apr 10, 2026; Third Circuit figures also in search summaries): Chapter 11 filed May 2020; the plan paid unsecured noteholders principal in full and distributed about \$1.1bn of value to old equity; Hertz declined the make-whole "Applicable Premiums" and offered post-petition interest at the federal judgment rate; the Third Circuit (2024, 120 F.4th 1181, 2–1) held the make-wholes are unmatured interest barred by §502(b)(2) but, because the debtor was solvent, the noteholders were owed post-petition interest at the contract rate plus the premium amounts ("more than a quarter billion dollars of interest"); Supreme Court denied certiorari January 12, 2026. **How the chapter uses it:** the recovery random variable has mass above 1.0, which is why Moody's supports $[0,120\%]$ and why a plain Beta on $[0,1]$ is a modeling choice, not a law; also a clean example of a one-inflated outcome (full recovery) in an unsecured class, driven by equity-market beta (used-car prices and a 2021 equity rally), i.e., a recovery that was a call option on the systematic factor.

### 7.3 First Brands Group (Sept–Oct 2025): the left tail is a cliff, not a slope (all facts CHECK)

The PitchBook headline "Leveraged loan default rate jumps as First Brands takes fast track to bankruptcy" was located but the article could not be fetched. The writer should confirm from PitchBook/LCD, the docket, and press: filing date (late September 2025, S.D. Tex., CHECK), funded debt and off-balance-sheet factoring/supply-chain finance totals (reported on the order of \$10bn+, CHECK), term-loan price path from the high 90s to the 30s within weeks (CHECK), and lender/fund exposures. If confirmed it is the ideal "jump, not diffusion" exhibit: the pre-event vol was unremarkable, the move was a single jump to a recovery level nobody could estimate because the collateral itself (receivables) was in dispute. If it cannot be confirmed, substitute SVB 2023 holdco bonds (Ch 23 owns the full autopsy) or keep §7.1–7.2 only.

---

## 8. Humor beats (every joke rides on a correct idea)

1. **Cold open, Mags on sigmas.** "It loses 55 points, once, and the model calls that a seven-sigma event every eighteen months." (Bohn–Stein p.514: six-to-eight sigma losses are economically significant in skewed portfolios.)
2. **Kaz's Gaussian.** "Let's just assume Gaussian." Theo computes skew $=-1/\sqrt{q}$: "At one percent PD the skew is minus ten. Your Gaussian has a skew of zero and a résumé." Kaz regrets it, per canon.
3. **Kaz vs legal vocabulary (one term this chapter): "debt cushion."** Kaz assumes it is an ergonomic benefit. Mags: "It's the junior debt that gets wiped out before you do. There used to be some." (Trend Watch #2.)
4. **Ines's Poker Table.** "You are not betting on the hand. You are betting on the size of the pot after the dealer takes 2.4 cents and the other table takes 73.7 to 100." (Serta.) Hand replayed through markouts: the bonds that traded to the desk the week before the uptier announcement.
5. **ROBO literalism.** "Fit a Beta to recoveries" produces `nan, nan` and a green checkmark, because the data had exact zeros and ones; the precise spec adds inflation masses. Second beat: "minimize kurtosis" makes ROBO hold T-bills, whose kurtosis is also zero and whose carry is also a résumé.
6. **The 13-week model reborn.** Theo's USB-stick model is a survival curve: thirteen weekly cash balances are thirteen conditional survival probabilities, and the first week the balance goes negative is $\hat\tau$. "The 13-week model is a hazard rate with a spreadsheet problem."
7. **Mags's back-in-my-day.** "We assumed 40 recovery because the bonds were actually senior to something. Now the first lien is senior to the other first lien, depending on counsel." Followed by grudging respect for the Beta regression's participation flag.
8. **The Ad Hoc Group (Greek chorus).** "We are represented by counsel. Our recovery is seventy-three point seven to one hundred. Yours is a rounding error." (Cooperation agreements signed in this book so far: 0, pending Part IV.)
9. **The tie-wearing option, extended.** "A CCC bond is an equity option that wears a tie to work. A loan-only, cov-lite first lien is a senior unsecured bond wearing a name tag that says FIRST LIEN."
10. **The Hill plot.** "It is called a Hill plot because you climb it, look around, and still cannot see the threshold." Then the real lesson: on a single bond there is no hill, only a cliff at $1-R/P_0$.

---

## 9. Resource-graph candidates

**Podcasts (all TITLE-ONLY; episode titles and dates must be confirmed before linking):** Bloomberg *Odd Lots* episodes on liability management and "creditor-on-creditor violence" (2023–2025); Bloomberg Intelligence *The Credit Edge* (recovery and LME episodes); Corey Hoffstein's *Flirting with Models* (any systematic-credit or tail-risk episode); Octus/Reorg and Petition podcasts on Serta and Mitel rulings.

**Practitioner writing:** Matt Levine, *Money Stuff* (Serta, "open market purchase," Hertz make-wholes) — TITLE-ONLY; Octus "The Year in LMEs" (Jan 8, 2026) VERIFIED-URL https://octus.com/resources/articles/the-year-in-lmes/ ; Octus "2025 Distressed Outlook" (Jan 6, 2025) VERIFIED-URL https://octus.com/resources/articles/2025-distressed-outlook/ ; Holwell Shuster & Goldberg, "Liability Management Exercises and the Courts in 2025" (Dec 22, 2025) VERIFIED-URL https://www.hsgllp.com/about-news-Liability-Management-Exercises-and-the-Courts-in-2025 ; Simpson Thacher *Liability Management Expresso* (Feb 2025) VERIFIED-URL (above); Creditor Rights Coalition "Creditor Corner 2025 Special Feature" VERIFIED-URL https://creditorcoalition.org/creditor-corner-2025-special-feature/ ; Nelson Mullins on Hertz after cert denial (Apr 10, 2026) VERIFIED-URL (above); Moody's insights pages (May 18, 2026; Apr 28, 2026; Sept 29, 2026) VERIFIED-URL (above); CreditSights LME webinar deck (Oct 2025) VERIFIED-URL https://know.creditsights.com/wp-content/uploads/LME-Webinar-Episode-1-Overview-and-Uptiering-10-21-25.pdf

**Academic papers:** the §6.6 list with DOI status as marked.

**Data & code:** FRED ICE BofA series BAMLH0A0HYM2, BAMLH0A3HYC, BAMLHYH0A0HYM2TRIV (total return, for computing monthly skew/kurtosis) VERIFIED-URL roots https://fred.stlouisfed.org/ ; SEC EDGAR https://www.sec.gov/edgar (canonical root); CourtListener REST https://www.courtlistener.com/help/api/ (canonical root); Moody's Default & Recovery Database and Ultimate Recovery Database — TITLE-ONLY (user guide fetch blocked); Fitch U.S. Leveraged Loan Default Index — TITLE-ONLY; Moody's LGD methodology (Aug 2006) mirror VERIFIED-URL https://care-mendoza.nd.edu/assets/152347/loss-given-default-rating-methodology.pdf ; FDIC CFR WP 2018-03 VERIFIED-URL (above); arXiv:1001.0783 and arXiv:2603.14491 VERIFIED-URL.

---

## 10. Exploratory-space notes (new sections and chapters for future editions)

1. **Ch 5-B, "Stochastic Recovery: Locks, Swaps, and the Term Structure of $R^{\mathbb{Q}}$."** Berd's convexity premium, digital CDS, Pan–Singleton identification, Doshi–Elkamhi–Ornthanalai term structure of expected recovery; how a desk marks $R^{\mathbb{Q}}$ by seniority when the 40% convention is obviously wrong (first-lien loan CDS, LCDX history).
2. **§ in Ch 14, "The Default Is a Mixture: Hard Default vs Distressed Exchange, and the Re-Default Hazard."** Build the two-stage survival model from Moody's 2026 numbers (1 in 4 soft events to hard default; >70% within two years) and the Fitch/Moody's DE shares 2022–2026; regime-switching Beta recoveries (Bruche–González-Aguado) with an LME-history covariate.
3. **§ in Ch 13 and Ch 21, "Participation Status as a Priced Covariate" and "Loan-Only Structures and the Death of the Debt Cushion."** Serta/Mitel/Wesco/ConvergeOne outcomes as a labeled dataset; the >75% first-lien share of debt stacks; Moody's family-recovery assumptions (65% recovery for all-bank-debt firms) that no longer describe sponsor-backed loan-only borrowers.
4. **§ in Ch 17, "Private Credit Default Rates From 1.6% to 9.2%: A Measurement Problem, Not a Fact."** PIK amendments and maturity extensions as hidden defaults (Moody's Oct 2026: 4.0% reported vs 5.8% adjusted); BDC marks by maturity bucket (88.8 vs 99.7) as an implied recovery/default surface.
5. **§ in Ch 6 or Ch 28, "Copulas, Tail Dependence, and Why the Mixing Variable Matters."** Bolder's $t$- and normal-variance-mixture threshold models; power-tailed mixers; implications for portfolio-level jump-to-default limits and LVaR.
6. **§ in Ch 23, "Calibrating Jumps to CDX Option Skews and ETF Returns."** Where VG/NIG earn their keep: liquid daily data, option surfaces, and the equity-to-credit skew map.
7. **§ in Ch 16, "Post-Petition Interest and the Solvent-Debtor Exception: When $R>1$."** Hertz 2024–2026 as the template; make-whole case law across the Second, Third, Fifth, and Ninth Circuits (CHECK).
8. **§ in Ch 11, "Return Distributions Under a Sell Discipline."** Dynkin's long-horizon return model conditioned on spread regime and sell rules (p.353–354, p.400): the distribution a defensive HY mandate actually faces, including the fallen-angel forced-sale penalty.
9. **§ in Ch 12, "Dispersion as a Mixture-Weight Signal."** CCC/HY OAS ratio history (FRED) as a regime indicator for multi-asset credit allocation.
10. **Appendix C Trend Tracker entries to add:** DE share of defaults by year (2022: 45–50%; 2024: 59.3% S&P / record Moody's; 2025: ~65%); first-lien recovery by year (Moody's series 2020–2024, CHECK) and the 55% projection (Sept 2026); LME counts (23/34/28 for 2023/2024/2025, Octus); ruling dates (§6.5); private-credit AUM (\$158bn 2010 → ~\$2tn 2024 → >\$2tn 2026).
