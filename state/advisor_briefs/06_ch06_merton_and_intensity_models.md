# Advisor Brief — Chapter 6: Stochastic Calculus, Intensity Models & Structural Frameworks

**Target file:** `book_src/06_ch06_merton_and_intensity_models.md` · **Edition 1** · Advisor: Fable
**Length target for the writer:** 7,000–10,000 words. Research dated 2026-10-17. Anything marked **CHECK** was not confirmed against a primary source this session.

---

## 1. Thesis and the "aha" for an ex-PJT-RSSG reader

**Thesis.** Every credit model is a statement about *when* $\tau$ happens and *what you get* when it does. Structural models (Merton, Black–Cox, KMV) say $\tau$ is the first time a diffusing asset value hits a boundary you can read off a balance sheet; reduced-form models (Jarrow–Turnbull, Lando, Duffie–Singleton) say $\tau$ is a surprise whose arrival rate $\lambda_t$ you read off a CDS curve. The desk needs both, in the right measure, with the right recovery convention, wired into one engine. The chapter's job is to build that engine from Itô's lemma up and to show where each model's assumptions were quietly repealed by the 2020–2026 market (cov-lite, uptiers, distressed exchanges, private credit with no equity ticker).

**The four ahas, in the order they should land on Theo:**

1. **Your 13-week model is a hazard rate wearing a spreadsheet.** The probability of running out of liquidity in week $k$ *given you survived week $k-1$* is $\lambda_k\,\Delta t$. The survival column is $S(t_k)=\prod_{j\le k}(1-\lambda_j\Delta t)\to e^{-\int_0^{t}\lambda_s ds}$. The reader has been building piecewise-constant hazard curves for years without the Greek letter (running gag #1 pays off here).
2. **Equity is a call; the fulcrum is the strike.** Merton (1974): $E_0 = V_0N(d_1)-Fe^{-rT}N(d_2)$; debt $=Fe^{-rT}-\text{Put}$. Every waterfall the reader ever built is a payoff diagram; the "fulcrum security" is the tranche whose strike sits where the asset distribution has mass. Hertz 2020–21 is the diagram made flesh: old equity got \$1.53 cash plus 3% of the new company plus warrants/rights because the call was not, in fact, out of the money (SEC S-1, 2021).
3. **The covenant you spent 90 hours modeling is a Black–Cox barrier, and the LMT you structured moved the barrier for someone else.** Black and Cox (1976) literally called it a "safety covenant." Cov-lite removed the barrier; a non-pro-rata uptier raises the effective default point of the left-behind lenders without touching the issuer's asset process. The modern "default" is a negotiated barrier crossing: distressed exchanges were ~65% of Q4 2024 defaults (S&P, Feb 2025; **CHECK** exact figure, bot-blocked).
4. **The market quotes $\mathbb{Q}$; RSSG trained you in $\mathbb{P}$; the gap is the premium systematic desks harvest.** $DD^{\mathbb{Q}} = DD^{\mathbb{P}} - \rho\,\lambda_{\text{Sharpe}}\sqrt{T}$ (Bohn–Stein App. 3B). Blackstone's "value" signal is exactly spread vs. model PD (Blackstone p.1); BlackRock's PD screen caught 77% of HY defaulters within 24 months (BlackRock p.6). Structural models did not die in 1984; they moved to the systematic desk and got a data feed.

---

## 2. Section outline (7,000–10,000 words)

**Cold open (≤400 words).** 1 a.m. Theo is porting his 13-week model to the desk's Python stack. Kaz asks why column N is called "Liquidity Runway (weeks)" and not $S(t)$. Mags: "Price is what you pay; recovery is what you get, eventually, after the lawyers." Ines: "What's the pot, what are the odds?" Ends on: *how do you turn a balance sheet and a stock price into a probability of default by Friday, and how do you check it against the CDS curve?* Then "By the end of this chapter you will be able to…" (price Merton debt, solve KMV, compute a Black–Cox PD with and without MC, bootstrap a CDS curve, state which measure every number lives in).

| § | Title | Anatomy elements carried | Boxes |
| :-- | :-- | :-- | :-- |
| 6.1 | Itô's Lemma: The Volatility Tax | Desk framing (Kaz); derivation (Itô, GBM, $d\ln V$); source (Veronesi p.552, p.562) | Ways This Blows Up (unannualized $\sigma$) |
| 6.2 | Merton 1974: Equity Is a Call, Debt Is a Short Put | Derivation (PDE via replication, Bohn–Stein p.206; closed forms; spread; short-end zero); sources (Ben_Dor p.105, Schmid p.118, Bolder p.257); mini AI spec | **Trend Watch #1: The Structural Renaissance on the Systematic Desk** (Blackstone/DCI, BlackRock PD, S&P Market Signal PD on SVB); Desk Myth vs Reality ("Merton is dead") |
| 6.3 | $\mathbb{P}$ to $\mathbb{Q}$: The Credit Risk Premium | Derivation (Girsanov sketch; $DD^{\mathbb{Q}}=DD-\rho\lambda\sqrt T$; Bohn–Stein p.209–210); Bai–Goldstein–Yang jump premium | Poker Table (Ines: "the premium is where the bonuses live") |
| 6.4 | KMV / Distance-to-Default: The Inverse Problem | Derivation ($\sigma_E E=N(d_1)\sigma_V V$; VK iteration; default point; empirical DD→EDF); sources (Bohn–Stein p.136–137, 159–161, 168–169); **Case Study A: SVB 2023, and why banks break Merton** (Nagel–Purnanandam); AI spec (solver) | Ways This Blows Up (DD ≥ 4 for 60% of firms); ROBO gag |
| 6.5 | Black–Cox: First Passage and Covenant Barriers | Derivation (reflection principle; down-and-out call; barrier $Ke^{-\gamma(T-t)}$); sources (Bohn–Stein p.150–152, Schmid p.121); Feldhütter–Schaefer; MC with Brownian bridge | **Trend Watch #2: Default Is Now a Negotiation** (distressed-exchange share, Serta 5th Cir., Moody's default rates 2025–26); Docket Diary (Ad Hoc Group on where the barrier is) |
| 6.6 | Reduced-Form I: Cox Processes, Jarrow–Turnbull, Duffie–Singleton, and Three Recoveries | Derivation (Cox construction; $S=\mathbb{E}^{\mathbb{Q}}e^{-\int\lambda}$; RMV discount $r+\lambda L$; RFV; RT); sources (Schmid p.71, 95, 128–130; Bohn–Stein p.328, 348); Duffie–Lando bridge | Desk Myth vs Reality ("40% recovery") |
| 6.7 | Reduced-Form II: CIR Intensities in Closed Form | Derivation (affine ODEs; $A,B$; Feller; noncentral $\chi^2$); sources (Bohn–Stein p.341, Veronesi p.597) | Ways This Blows Up (Euler goes negative) |
| 6.8 | Hazard Bootstrapping from CDS and the Credit Triangle | Derivation (legs, RPV01, piecewise-constant $\lambda$, upfront, accrual on default); ISDA model conventions; AI spec (bootstrap) | **Trend Watch #3: Single-Name CDS, Episodic Liquidity, and Clearing** (ISDA May 2023; BIS 2024) |
| 6.9 | Hybrids: Structural Signals Inside Intensity Models | Bohn–Stein p.354–355 two-stage fit; Berndt et al.; equity→credit lead–lag (Man 2022 p.31; Dynkin p.87–88); the "DD momentum" feature (bridge to Ch 10); **Case Study C (short): First Brands 2025, a firm with no equity ticker** | Trend thread: private credit has no $\sigma_E$ |
| 6.10 | Case Study B: Carvana 2022–23 and Hertz 2020–21 | Full autopsy with sourced facts; how the desk would have flagged it | Poker Table (Hertz 2-outer) |
| 6.11 | Specification for AI Implementation | The chapter's engine (see §4 below) with sanity checks | ROBO literalism paragraph |
| 6.12 | Ways This Blows Up (consolidated) | Traps list (§3.10 below) | |
| 6.13 | Desk Debrief · The Spec You Hand the Robot · Exercises | | |

Deep-Dive Resource Graph after 6.2, 6.5, 6.8, 6.10 and at chapter end. Running gags to hit: 13-week model → survival curve (6.1, 6.8); ROBO literalism (6.4, 6.11); Kaz misreads one legal term (6.5: "springing lien"); Mags "back in my day" (6.6, 6.8); Ines hand history (6.3, 6.10); "IDO or it didn't happen" (6.9).

---

## 3. Derivation skeletons

Notation per style bible: $V_t$ assets, $F$ face, $E_t$ equity, $\sigma_V,\sigma_E$, $r$, $\tau$, $\lambda_t$, $S(t)$, $R$, $L=1-R$, $s$. Say the measure every time.

### 3.1 Itô and GBM ($\mathbb{P}$)
$dV_t=\mu V_t\,dt+\sigma_V V_t\,dW_t$. For $f(t,V)$: $df=\big(f_t+\mu V f_V+\tfrac12\sigma_V^2V^2 f_{VV}\big)dt+\sigma_V V f_V\,dW_t$. With $f=\ln V$:
$$d\ln V_t=\Big(\mu-\tfrac12\sigma_V^2\Big)dt+\sigma_V\,dW_t,\qquad V_T=V_0\exp\!\Big[\big(\mu-\tfrac12\sigma_V^2\big)T+\sigma_V W_T\Big].$$
The $-\tfrac12\sigma_V^2$ is the tax; it comes from $(dW_t)^2=dt$. Error-prone: forgetting the tax when simulating (drift biased up by $\tfrac12\sigma^2$); using daily $\sigma$ without $\sqrt{252}$.

### 3.2 Merton (1974) ($\mathbb{Q}$ for prices, $\mathbb{P}$ for PDs)
Single zero-coupon debt of face $F$ at $T$; equity $E_T=\max(V_T-F,0)$; debt $D_T=\min(V_T,F)=F-\max(F-V_T,0)$. Replication (Bohn–Stein p.206) gives the Black–Scholes PDE $\tfrac12\sigma_V^2V^2E_{VV}+rVE_V+E_t-rE=0$. Closed forms:
$$E_0=V_0N(d_1)-Fe^{-rT}N(d_2),\qquad d_{1}=\frac{\ln(V_0/F)+(r+\tfrac12\sigma_V^2)T}{\sigma_V\sqrt T},\quad d_2=d_1-\sigma_V\sqrt T.$$
$$D_0=V_0-E_0=Fe^{-rT}N(d_2)+V_0N(-d_1)=Fe^{-rT}-\underbrace{\big[Fe^{-rT}N(-d_2)-V_0N(-d_1)\big]}_{\text{Put}}.$$
Spread (verified signs; define quasi-leverage $\ell=Fe^{-rT}/V_0$):
$$s(T)=-\frac1T\ln\frac{D_0}{Fe^{-rT}}=-\frac1T\ln\!\Big[N(d_2)+\frac{V_0e^{rT}}{F}N(-d_1)\Big]=-\frac1T\ln\!\Big[N(d_2)+\frac{N(-d_1)}{\ell}\Big].$$
Short end: for $V_0>F$, as $T\downarrow0$, $N(d_2)\to1$ and $N(-d_1)\to0$ faster than any power of $T$, so $s(T)\to0$: *a Merton firm cannot default tomorrow unless it is already dead today.* Risk-neutral PD $=N(-d_2)$. Physical PD $=N(-DD)$ with
$$DD=\frac{\ln(V_0/F)+(\mu-\tfrac12\sigma_V^2)T}{\sigma_V\sqrt T}.$$
Equity vol link (Itô on $E=f(V,t)$): $\sigma_E E_0=N(d_1)\,\sigma_V V_0$. Error-prone: mixing $\mu$ and $r$ inside one $d$; using $\sigma_E$ as $\sigma_V$ (overstates PD by the leverage factor $V/E\cdot N(d_1)$); calling face value $D$ (reserved for duration).

### 3.3 $\mathbb{P}\to\mathbb{Q}$ (Bohn–Stein App. 3B)
Girsanov: $dW^{\mathbb{Q}}_t=dW_t+\frac{\mu-r}{\sigma_V}dt$. With CAPM $\mu-r=\beta(\mu_M-r)$, $\rho=\text{corr}(r_A,r_M)$ and Sharpe $\lambda_{\text{Sharpe}}=(\mu_M-r)/\sigma_M$:
$$DD^{\mathbb{Q}}=DD-\rho\,\lambda_{\text{Sharpe}}\sqrt T,\qquad PD^{\mathbb{Q}}=N\!\big(N^{-1}(PD^{\mathbb{P}})+\rho\lambda_{\text{Sharpe}}\sqrt T\big)>PD^{\mathbb{P}}.$$
Error-prone: applying the shift to a PD that already came from spreads (double counting); forgetting the $\sqrt T$ (the premium scales with horizon). Bai–Goldstein–Yang (2020) is the reminder that a *jump* risk premium is needed to reconcile historical default rates with IG spreads, so the diffusion-only shift under-prices the premium.

### 3.4 KMV / Vasicek–Kealhofer ($\mathbb{P}$)
Two unknowns $(V_0,\sigma_V)$, two equations: $E_0=\text{BSM}(V_0,\sigma_V)$ and $\sigma_E E_0=N(d_1)\sigma_VV_0$. Newton/fsolve on $(\ln V_0,\ln\sigma_V)$ with the Jacobian; or the VK iteration (Bohn–Stein p.169): 156 weekly equity returns → guess $\sigma_V$ → invert $E=f(V)$ each week → asset returns → new $\sigma_V$ → repeat to convergence. Default point $X=\text{STD}+\tfrac12\text{LTD}$ (Crosbie–Bohn 2003; TITLE-ONLY) after removing deferred taxes/minority interest and *adding* material off-balance-sheet liabilities (Bohn–Stein p.159). KMV's reported DD is the simplified $(V_0-X)/(V_0\sigma_V)$ at a 1-year horizon, mapped to EDF through an empirical, monotone DD→EDF table (≥400 defaults minimum, 1,000 recommended, half-sigma cohorts 0–16; Bohn–Stein p.161–162). Bharath–Shumway (2008): a "naive" DD using $\sigma_V\approx\frac{E}{E+F}\sigma_E+\frac{F}{E+F}(0.05+0.25\sigma_E)$ forecasts about as well as the iterated solution; the functional form, not the solver, carries the information. Error-prone: ill-conditioned when $E\ll F$ (deep distress: $N(d_1)\to0$, Jacobian singular; bound $\sigma_V\in[0.01,3]$ and $V_0\ge E_0$); nonstationary $\sigma_E$ from leverage changes (Bohn–Stein p.136 fn.12); normal DD→PD gives zero PD for 60% of firms (p.160).

### 3.5 Black–Cox first passage ($\mathbb{P}$ or $\mathbb{Q}$ by drift)
Barrier $K_t=Ke^{-\gamma(T-t)}$; default $\tau=\inf\{t:V_t\le K_t\}$. Let $X_t=\ln(V_t/K_t)$, $x_0=\ln(V_0/K_0)>0$, drift $m=\mu-\tfrac12\sigma_V^2-\gamma$ (replace $\mu\to r-q$ under $\mathbb{Q}$ with payout $q$). Reflection principle for Brownian motion with drift:
$$\mathbb{P}(\tau\le T)=N\!\Big(\frac{-x_0-mT}{\sigma_V\sqrt T}\Big)+e^{-2mx_0/\sigma_V^2}\,N\!\Big(\frac{-x_0+mT}{\sigma_V\sqrt T}\Big).$$
Check: $m=0$ gives $2N(-x_0/\sigma_V\sqrt T)=2\,pd$, the "$pd_a=2pd$" line on Bohn–Stein p.151. Equity = down-and-out call; debt = $Fe^{-rT}$ − put + rebate at barrier (Bohn–Stein p.152 boundary conditions). Covenant mapping: a maintenance leverage test $\text{Debt}/\text{EBITDA}\le c$ is a barrier in EBITDA space; translate via $V\approx m_{\text{EV}}\cdot\text{EBITDA}$ so $K=\text{Debt}\cdot m_{\text{EV}}/c$. Cov-lite: $K\to$ payment default only (barrier at coupon/maturity dates, i.e., Geske-style discrete monitoring). Uptier: left-behind lenders' $F$ is effectively subordinated to new super-priority debt $F^{+}$, so *their* strike moves from $F$ to $F+F^{+}$ while $V_t$ is unchanged. Monte Carlo trap: discrete monitoring underestimates hitting; Brownian-bridge correction per step, with log-values $x_i,x_{i+1}$ above log-barrier $b$:
$$p_i=\exp\!\Big(-\frac{2(x_i-b)(x_{i+1}-b)}{\sigma_V^2\Delta t}\Big),$$
draw $U_i\sim\text{Unif}$, hit if $U_i<p_i$ (Glasserman 2004, TITLE-ONLY). Feldhütter–Schaefer (2018): Black–Cox calibrated to historical default rates fits IG spreads; under-prices HY, partly illiquidity.

### 3.6 Cox processes, Jarrow–Turnbull, Duffie–Singleton ($\mathbb{Q}$ unless stated)
Construction (Schmid p.71): $\tau=\inf\{t:\int_0^t\lambda_sds\ge\Theta\}$, $\Theta\sim\text{Exp}(1)$ independent of the factor filtration. Then $S(t,T)=\mathbb{E}^{\mathbb{Q}}\big[e^{-\int_t^T\lambda_udu}\,\big|\,\mathcal{F}_t\big]$ and the zero-recovery bond (Lando 1998; Schmid p.129):
$$P^{d,0}(t,T)=\mathbb{E}^{\mathbb{Q}}\Big[e^{-\int_t^T(r_u+\lambda_u)du}\Big|\mathcal{F}_t\Big].$$
Three recoveries (Schmid p.95; Bohn–Stein p.348): **RMV** (Duffie–Singleton): recover fraction $R$ of pre-default market value → discount at $r_t+\lambda_tL_t$, instantaneous spread $s_t=\lambda_t^{\mathbb{Q}}L_t$; **RFV** (recovery of par, CDS convention): $P^d=P^{d,0}+R\int_t^T P(t,u)\,\big(-\partial_uS(t,u)\big)du$; **RT** (Jarrow–Turnbull): recover $R$ riskless bonds of same maturity, $P^d=P(t,T)\big[R+(1-R)S(t,T)\big]$ under independence. Jarrow–Turnbull (1995) is the constant-$\lambda$, RT special case. Error-prone: converting a 40% RFV quote into RMV for a bond trading at 60 (different numeraire; Schmid p.95); independence of $r$ and $\lambda$ assumed in RT formula. Duffie–Lando (2001) bridge: with noisy accounting, a structural model *acquires* an intensity and short spreads become strictly positive — the "why reduced-form at the short end" argument in one paper.

### 3.7 CIR intensity ($\mathbb{Q}$)
$d\lambda_t=\kappa(\theta-\lambda_t)dt+\sigma\sqrt{\lambda_t}\,dW_t$. Affine ansatz $S(t,T)=A(\tau)e^{-B(\tau)\lambda_t}$, $\tau=T-t$, Riccati ODEs $B'=1-\kappa B-\tfrac12\sigma^2B^2$, $A'/A=-\kappa\theta B$, $A(0)=1,B(0)=0$. With $\gamma=\sqrt{\kappa^2+2\sigma^2}$:
$$B(\tau)=\frac{2(e^{\gamma\tau}-1)}{(\gamma+\kappa)(e^{\gamma\tau}-1)+2\gamma},\qquad A(\tau)=\Big[\frac{2\gamma e^{(\kappa+\gamma)\tau/2}}{(\gamma+\kappa)(e^{\gamma\tau}-1)+2\gamma}\Big]^{2\kappa\theta/\sigma^2}.$$
Feller: $2\kappa\theta\ge\sigma^2$ keeps $\lambda>0$. Transition is noncentral $\chi^2$ (Veronesi p.597; exact simulation available via `scipy.stats.ncx2`). Error-prone: Euler scheme produces negative $\lambda$ → use full truncation $\sqrt{\max(\lambda,0)}$ or exact sampling; $\kappa,\theta$ weakly identified from one curve (fix $\kappa$ by prior); matching the sign convention $A,B$ vs. Lando's $\alpha,\beta$ (Bohn–Stein p.341 note).

### 3.8 CDS bootstrap and the credit triangle ($\mathbb{Q}$)
Premium leg (coupon $c$, accrual fractions $\Delta_i$ ACT/360 on IMM dates), protection leg with RFV recovery $R$, discount $P(0,t)$:
$$\text{PV}_{\text{prem}}=c\sum_i\Delta_iP(0,t_i)\Big[S(t_i)+\tfrac12\big(S(t_{i-1})-S(t_i)\big)\Big],\qquad \text{PV}_{\text{prot}}=(1-R)\sum_j P(0,t_j^m)\big(S(t_{j-1})-S(t_j)\big)$$
on a fine grid $t_j^m$ (midpoint discounting). Par spread $s=\text{PV}_{\text{prot}}/\text{RPV01}$ with $\text{RPV01}=\text{PV}_{\text{prem}}/c$; upfront $=(s-c)\cdot\text{RPV01}$ (standard coupons 100/500 bp since 2009). Bootstrap: piecewise-constant $\lambda_k$ on $(T_{k-1},T_k]$, solve sequentially by Brent on $\lambda_k$ so the $T_k$ quote reprices with earlier $\lambda$'s fixed (MathWorks `cdsbootstrap`; ISDA model). Credit triangle: flat $\lambda$, continuous premium, $P\equiv$ const ⇒ $s=\lambda(1-R)$ exactly; with discrete coupons $s\approx\lambda(1-R)$. Error-prone: inverted distressed curves produce negative $\lambda_k$ (MathWorks warns on "non-monotone default probabilities") — cap at a floor and flag; quoted recovery differs by seniority (40% senior, 20% subordinated — standard model defaults, **CHECK** for current ISDA tables); day count mismatch (ACT/360 premium vs. ACT/365 discounting); forgetting accrual on default; treating points-upfront quotes as running spreads.

### 3.9 Hybrid two-stage fit (Bohn–Stein p.355)
Stage 1: fit $\lambda^{\mathbb{P}}$ dynamics to equity-based PDs via $1-\text{cpd}_t=e^{-\int_0^t h}$. Stage 2: fit the market price of risk so $\lambda^{\mathbb{Q}}=\lambda^{\mathbb{P}}\cdot\Pi_t$ reprices CDS. Berndt et al. (EDF vs. CDS) is the empirical template; the ratio $\lambda^{\mathbb{Q}}/\lambda^{\mathbb{P}}$ is a tradable "premium" time series (Blackstone's value signal in another costume).

### 3.10 Consolidated traps (feed 6.12)
$\mathbb{P}/\mathbb{Q}$ mixing · unannualized $\sigma_E$ · $\sigma_E$ for $\sigma_V$ · Merton short-end zero · DD normality · barrier discretization bias · negative hazards · RMV/RFV numeraire · CIR negativity · $\kappa$–$\theta$ identifiability · banks' concave assets (Nagel–Purnanandam) · off-balance-sheet liabilities in the default point (First Brands) · the barrier is not where the credit agreement says when the agreement can be amended by 50.1%.

---

## 4. Code spec (reference implementation; do not run here)

**Module `ch06_structural_intensity_engine` (one ```python block, numpy/scipy only, `rng = np.random.default_rng(42)`).**

Data schemas: `MertonInputs{V0:float, F:float, r:float, sigma_V:float, T:float, mu:float|None}`; `KMVInputs{E_series: np.ndarray (N_weeks,), F:float, r:float, T:float=1.0}`; `CDSQuotes{tenors: np.ndarray (K,) years, spreads_bp: np.ndarray (K,), R:float=0.4, discount: callable t→P(0,t)}`; batch shape convention `(n_issuers, n_tenors)`.

Functions and sanity checks (each prints PASS/FAIL with tolerance):
1. `merton_prices(V0,F,r,sigma_V,T) -> (E0,D0,spread,pd_Q)` and `merton_pd_P(...,mu)`. **Check A:** $E_0+D_0=V_0$ to $10^{-10}$; **Check B:** Monte Carlo debt value $e^{-rT}\mathbb{E}^{\mathbb{Q}}[\min(V_T,F)]$ with 200k antithetic paths within 3 SE of closed form; **Check C:** $s(T)\to0$ as $T\to10^{-3}$ for $V_0>F$.
2. `solve_kmv(E0,sigma_E,F,r,T) -> (V0,sigma_V)` via `scipy.optimize.fsolve` on log-parameters with analytic Jacobian, bounds guard; `kmv_iterate(E_series,F,r,T)` VK loop (tolerance $10^{-6}$, max 100 iters). **Check D:** round trip: generate $(V_0,\sigma_V)$ → $(E_0,\sigma_E)$ → solve → recover to $10^{-6}$. **Check E:** `naive_dd` (Bharath–Shumway) within 0.5 of iterated DD on the synthetic case.
3. `black_cox_pd(V0,K,gamma,mu,sigma_V,T) -> pd` closed form; `black_cox_mc(..., n_steps, bridge: bool)`. **Check F:** bridge MC within 3 SE of closed form; naive MC (no bridge, 12 steps) lower than closed form (prints the bias). **Check G:** $m=0$ case equals $2\cdot N(-x_0/\sigma\sqrt T)$.
4. `cir_survival(lam0,kappa,theta,sigma,T) -> S` closed form; `cir_mc(..., exact=True)` using `ncx2`. **Check H:** closed form vs MC within 3 SE; asserts Feller.
5. `cds_legs(lambda_piecewise, tenors, c, R, discount) -> (pv_prem, pv_prot, rpv01)`; `bootstrap_hazard(quotes) -> lambda_k`; `credit_triangle(s,R)`. **Check I:** repricing error of every input quote $<10^{-8}$ in spread; **Check J:** flat 300 bp curve with $R=0.4$ gives $\lambda\approx0.05$ within 2 bp of $s/(1-R)$; **Check K:** inverted curve case (5y < 1y) triggers the negative-hazard warning path.
6. `merton_spread_vs_cds(...)`: given $(V_0,F,\sigma_V,r,T)$ produce Merton $s(T)$ for $T\in\{1,3,5,7,10\}$ and bootstrap the implied hazard curve from them; plot-free table. **Check L:** implied $\lambda(T)$ is hump-shaped/increasing from near zero (the structural short-end problem, numerically).

Numerical guards: `np.clip(sigma_V,1e-4,5)`, `np.log` on positive-checked args, `norm.cdf` from `scipy.stats`, `erfcx` for extreme $d$'s if needed, vectorized over tenors, no Python loops inside MC except the time-step loop.

---

## 5. Source map (book_id p.N · why · exact quotation ≤60 words)

1. **Veronesi p.552** · Itô for bond prices, convexity intuition · "Ito's lemma (Equation 14.37) says that the capital gain dollar return of a bond has two components: The first component is a predictable "dt" component that depends on the curvature of the function F(X). The second component is a random term given by the sensitivity of the bond price to changes in the underlying variable"
2. **Veronesi p.562** · what Itô buys you · "Ito's lemma is useful in finance as it provides the rules to compute: (a) The expected change in value of interest rate securities (e.g., the expected capital gain E[dPt]); (b) The volatility of interest rate security prices induced by variation in interest rates; (c) The hedge ratios needed for interest rate risk management"
3. **Ben_Dor p.105** · Merton's key insight, DTS lineage · "The key insight provided by Merton is that, in this setup, the firm's equity is equivalent to a European option on the firm's asset value and can be valued using the Black-Scholes option pricing equation."
4. **Ben_Dor p.109** · Merton ⇒ DTS linearity (bridge to Ch 8) · "This model allows us to develop an analytical relationship between spread and spread volatility, and confirms that this relationship is very close to linear within the investment-grade range of spreads."
5. **Schmid p.118** · Merton's stylization; APR violated (Mags) · "But Franks & Torous (1994) find that the strict absolute priority rule was violated in 78% of the bankruptcies they considered. Thus, the assumptions of the Merton model are highly stylized versions of reality."
6. **Schmid p.121** · Black–Cox = safety covenants · "Black & Cox (1976) introduce so called safety covenants which provide the bondholders the right to force the firm into bankruptcy as soon as the firm value hits some deterministic time-dependent threshold."
7. **Schmid p.71** · Cox process definition · "Such a model is called a Cox process or doubly stochastic Poisson process model."
8. **Schmid p.95** · recovery conventions are numeraires; PD and LGD errors symmetric · "Different recovery models can be transformed into each other. Basically, the value of the defaultable security at default is expressed using different numeraires." (also: "A proportional error in either the probability of default or recovery rate affects potential credit losses identically.")
9. **Schmid p.128** · why reduced form; its drawback · "Secondly, the default time is unpredictable and therefore the behavior of credit spreads for short maturities can be captured more realistically." and "their main draw-back is the missing link between firm value and corporate default."
10. **Schmid p.129** · Lando's zero-recovery formula intuition · "From a technical point of view, pricing of defaultable discount bonds is the same as pricing of non-defaultable discount bonds."
11. **Bohn_Stein p.136** · equity vs asset vol trap · "Note that a firm can have stationary asset volatility and still have nonstationary equity volatility as the firm changes its leverage over time."
12. **Bohn_Stein p.137** · vol matters, drift doesn't · "As is the case in classic option pricing, asset volatility is much more important to default prediction than is asset drift."
13. **Bohn_Stein p.151** · first-passage realism · "This case is not realistic as a firm will typically default at whatever time its market asset value falls through its default barrier."
14. **Bohn_Stein p.159** · default point adjustments (First Brands hook) · "large levels of off-balance-sheet liabilities can make a difference and should be included in the DD calculation."
15. **Bohn_Stein p.160** · DD normality fails · "Empirical research, however, found that nearly 60 percent of its sample of over 25,000 firms have DDs that are 4 or greater. Recall that under the normal distribution, a DD of 4 is nearly equal to zero."
16. **Bohn_Stein p.161** · data needed for DD→PD · "At a bare minimum, a sample (ideally unbiased) of 400 defaults in a range of credit qualities is needed to develop a reasonable estimate of the empirical DD distribution. A sample of at least 1,000 defaults is recommended"
17. **Bohn_Stein p.169** · VK iteration · "We then run the equity value equation backwards to determine an implied asset value."
18. **Bohn_Stein p.182** · jumps for short tenors · "Even so, jump-diffusion models may be useful when looking at very short-dated instruments (e.g., less than three months). More standard structural models are well-known to be unable to generate sensible spreads observed at short tenors."
19. **Bohn_Stein p.210** · P→Q · "The risk-neutral DD is smaller than the physical DD, reflecting the adjustment that results in a higher PD, all else equal."
20. **Bohn_Stein p.328** · intensity philosophy · "The key assumption of reduced-form models is that the intensity process implies a distribution for the time to default. Said another way, all firms are assumed to default eventually and the riskier ones default earlier."
21. **Bohn_Stein p.341** · CIR in practice · "The Cox, Ingersoll, and Ross (CIR) specification is quite popular among academics but is less widely used in practice."
22. **Bohn_Stein p.348** · $s=h^{\mathbb{Q}}L$ · "this version of DSL now models the instantaneous, risk-neutral expected rate of loss of market value, which is a function of default intensity and instantaneous LGD at time t resulting from default."
23. **Bohn_Stein p.355** · hybrid fit precedent · "Berndt, Douglas, Duffie, Ferguson, and Schranz (2004) use EDF and CDS data to do exactly this sort of estimation."
24. **Bolder p.257** · epigraph and the first-and-last joke · "In many discussions of credit risk, Merton (1974) is the first—and occasionally also the last—model considered."
25. **Bolder p.283** · Merton ⇒ Gaussian threshold (bridge to Ch 5/Bolder) · "If, instead of using market information to inform the distance-to-default, one infers the liability threshold from the default probability, much of the mathematical complexity of Merton (1974) dissipates. What remains is a Gaussian threshold model."
26. **Dynkin p.87** · Merton hedge ratios work · "Research has shown that analytical equity hedge ratios based on the Merton model make reasonably accurate predictions of how corporate bond returns vary given the corresponding equity returns (Schaefer and Strebulaev 2008)."
27. **Dynkin p.88** · and where they fail · "it uses the leverage ratio as one of the few inputs to determine a firm's hedge ratio and ignores other important aspects of a firm's operations, such as cash flows and profitability."
28. **Blackstone p.1** · Trend Watch #1 · "It uses structural default models (similar to the Merton model) that analyze a company's capital structure, cash flows, leverage, and real-time equity market signals to calculate daily, dynamic default probabilities for thousands of corporate issuers."
29. **BlackRock p.6** · Trend Watch #1 · "Our proprietary probability of default signal that has underpinned all of our credit strategies for over 20 years has successfully identified 77% of the defaulted bonds in the ICE BofA High Yield Index within 24 months of its default since 2010."
30. **Man_Quant 2022 p.31** · equity lead–lag (bridge to Ch 10) · "the only spill-over to achieve meaningful statistical significance is equity Momentum, which generates a higher alpha than corporate bond Momentum itself."

Also useful without quotation: Bohn_Stein p.150 (structural-model history: Jones–Mason–Rosenfeld to KMV), p.152 (BC boundary conditions), p.157 (VK features), p.206–209 (App. 3A derivation), p.336 (deterministic intensity), p.354 (Duffee 1998 <10 bp fit); Schmid p.68–70 (intensity theorems), p.75 (affine taxonomy), p.130 (affine bond formula, RMV); Veronesi p.587–588, 597 (CIR stationary and transition laws); Bolder p.268 (GBM, $d_1$), p.282 (indirect Merton simulation algorithm), p.670 (Black–Scholes appendix, measure change).

---

## 6. RESEARCH DOSSIER (dated, sourced)

### 6A. Foundational papers (verified this session unless flagged)
- Merton, R. C. (1974), *On the Pricing of Corporate Debt: The Risk Structure of Interest Rates*, J. Finance 29(2): 449–470. DOI 10.1111/j.1540-6261.1974.tb03058.x (DOI resolves to Wiley; page bot-blocked).
- Black, F. & Cox, J. (1976), *Valuing Corporate Securities: Some Effects of Bond Indenture Provisions*, J. Finance 31(2): 351–367. DOI 10.1111/j.1540-6261.1976.tb01891.x (resolves; bot-blocked).
- Jarrow, R. & Turnbull, S. (1995), *Pricing Derivatives on Financial Securities Subject to Credit Risk*, J. Finance 50(1): 53–85. DOI 10.1111/j.1540-6261.1995.tb05167.x (resolves; bot-blocked).
- Duffie, D. & Singleton, K. (1999), *Modeling Term Structures of Defaultable Bonds*, Rev. Financial Studies 12(4): 687–720. DOI 10.1093/rfs/12.4.687 (VERIFIED: resolves to the OUP article page with this title).
- Lando, D. (1998), *On Cox Processes and Credit Risky Securities*, Review of Derivatives Research 2: 99–120. TITLE-ONLY (DOI lookup failed this session).
- Cox, Ingersoll & Ross (1985), *A Theory of the Term Structure of Interest Rates*, Econometrica 53(2): 385–407. TITLE-ONLY.
- Duffie, D. & Lando, D. (2001), *Term Structures of Credit Spreads with Incomplete Accounting Information*, Econometrica 69(3): 633–664, DOI 10.1111/1468-0262.00208. VERIFIED: https://econometricsociety.org/publications/econometrica/2001/05/01/term-structures-credit-spreads-incomplete-accounting ; PDF https://www.darrellduffie.com/uploads/1/4/8/0/148007615/duffielando2001.pdf . Exact quote from p.634: "With perfect information, yield spreads for surviving firms are zero at zero maturity, and are relatively small for small maturities, regardless of the riskiness of the firm." and "With imperfect information, however, yield spreads are strictly positive at zero maturity because investors' are uncertain about the nearness of current assets to the trigger level".
- Bharath, S. & Shumway, T. (2008), *Forecasting Default with the Merton Distance to Default Model*, RFS 21(3): 1339–1369. DOI 10.1093/rfs/hhn044 (VERIFIED title/volume via OUP). Key claim (from knowledge; **CHECK** numbers): naive DD performs about as well as the iterated KMV solution out of sample.
- Feldhütter, P. & Schaefer, S. (2018), *The Myth of the Credit Spread Puzzle*, RFS 31(8): 2897–2942, DOI 10.1093/rfs/hhy032. VERIFIED: https://lbsresearch.london.edu/id/eprint/953 . Black–Cox calibrated to historical default rates fits IG spreads; HY spreads too low, partly illiquidity.
- Bai, J., Goldstein, R. & Yang, F. (2020), *Is the Credit Spread Puzzle a Myth?*, JFE 137(2): 297–319, DOI 10.1016/j.jfineco.2020.02.009. VERIFIED: https://ideas.repec.org/a/eee/jfinec/v137y2020i2p297-319.html . Reverses FS when calibrated to market (not book) debt values; rejects GBM; needs a large jump-risk premium → puzzle is IG, not HY.
- Nagel, S. & Purnanandam, A. (2020), *Banks' Risk Dynamics and Distance to Default*, RFS 33(6): 2421–2467, DOI 10.1093/rfs/hhz125; NBER w25807 (May 2019) VERIFIED: https://www.nber.org/papers/w25807 . Bank assets are short puts on borrowers' assets (concave payoff); constant-vol Merton understates bank default risk in good times; bank equity is a mezzanine claim, not a call. (One fetch summary wrongly listed a third author; the paper has two.)
- Schaefer & Strebulaev (2008), *Structural Models of Credit Risk Are Useful: Evidence from Hedge Ratios on Corporate Bonds*, JFE. TITLE-ONLY (cited Dynkin p.87).
- Crosbie & Bohn (2003), *Modeling Default Risk*, Moody's KMV. TITLE-ONLY. Moody's CreditEdge quick reference (defines DD as standard deviations between asset value and default point): https://www.moodys.com/sites/products/productattachments/ce_quickreference.pdf (search-listed; not fetched).
- O'Kane & Turnbull (2003), *Valuation of Credit Default Swaps*, Lehman Brothers (cited by MathWorks as the bootstrap reference). TITLE-ONLY. O'Kane (2008), *Modelling Single-name and Multi-name Credit Derivatives*, Wiley. TITLE-ONLY.
- Goyal, Bali, Huang, Jiang & Wen (2020 WP), *Predicting Corporate Bond Returns: Merton Meets Machine Learning* (SFI 20-110): imposing Merton structure on ML improves out-of-sample bond return prediction. https://www.sfi.ch/en/publications/n-20-110-the-cross-sectional-pricing-of-corporate-bonds-using-big-data-and-machine-learning (search-listed). Bridge to Ch 7.
- Equity-implied rating model for unrated firms, *Journal of Computational Finance* (year **CHECK**): https://www.risk.net/journal-of-computational-finance/7959593/an-equity-implied-rating-model-for-unrated-firms (search-listed).
- *Arbitrage Opportunities in CDS Term Structure* (arXiv 1811.08038): ISDA model bootstraps piecewise-constant hazards; documents negative-hazard arbitrage. https://arxiv.org/pdf/1811.08038 (search-listed).

### 6B. Trend data: structural models on the systematic desk (2020–2026)
- Blackstone BCBS: ">\$40 billion" AUM, "largest pure-play quantitative credit operation"; DCI acquired "late-2020," DCI "co-founded by the creators of the KMV model"; daily structural PDs for thousands of issuers (Blackstone p.1; undated shelf paper, **CHECK** AUM date).
- BlackRock Systematic HY: PD signal "identified 77% of the defaulted bonds in the ICE BofA High Yield Index within 24 months of its default since 2010," data as of March 31, 2024 (BlackRock p.6).
- S&P Global Market Intelligence Market Signal PD (Merton-based, equity-vol driven) on SVB: first flag September 2022 when 1-yr PD rose 1.1%→2.5% in 10 days; peak Dec 6, 2022 at 6% ('b-' implied score), ~5× the US regional-bank median 1.27%. Source: S&P MI blog "Silicon Valley Bank: uncovering regional bank stress with equity-driven credit models" https://www.spglobal.com/marketintelligence/en/news-insights/blog/silicon-valley-bank-uncovering-regional-bank-stress-with-equity-driven-credit-models (search summary; page bot-blocked; **CHECK** figures).
- Barclays/Dynkin: Merton analytical hedge ratios ~5% lower than empirical sensitivity-matched ratios in both IG and HY; bond-over-replication IRs 0.41 IG / 0.37 HY (Dynkin p.87–88; sample Jan 1993–Dec 2019 per p.115).
- Man 2022: equity momentum spills into credit more strongly than bond momentum itself (p.31, citing Houweling et al. 2016; Bektic et al. 2016 attribute it to faster information incorporation in equities).

### 6C. Trend data: the default barrier moved (LMT era)
- S&P Global Ratings, Feb 20, 2025: distressed exchanges ≈65% of all defaults in Q4 2024; through end-2024 the distressed-exchange default rate was 3.2% vs 2% for all other default types; US spec-grade default-rate forecast 3.5% by Dec 2025 (range 2.25–6%). URL https://www.spglobal.com/ratings/en/research/articles/250220-default-transition-and-recovery-the-u-s-speculative-grade-corporate-default-rate-could-fall-to-3-5-by-dec-13420343 (search summary; bot-blocked; **CHECK**).
- Oaktree Q4 2024 "The LME Wave" (as cited by Quinn Emanuel, Jan 1, 2026): "over 50% of corporate defaults now occur through Liability Management Exercises." Quinn Emanuel also cites: *In re Serta Simmons Bedding*, 125 F.4th 555 (5th Cir. Dec. 31, 2024) invalidating the uptier; *Ocean Trails CLO VII v. MLN Topco* (Mitel), N.Y. App. Div. 1st Dep't, Dec. 31, 2024, upholding; Travelport subordinated recovery estimates 75%→0% (S&P); "more than ten" cooperation agreements in H1 2024 (Reorg). URL https://www.quinnemanuel.com/the-firm/publications/creditor-on-creditor-violence-how-liability-management-exercises-became-the-new-bankruptcy/ (VERIFIED). The article's "approximately 14% of companies executing LMEs successfully avoid subsequent bankruptcy" line reads ambiguously — **CHECK** against S&P/Moody's re-default studies before quoting.
- Moody's spec-grade default rates (via First Trust "Factoid," June 22, 2026, VERIFIED secondary): global TTM 4.3% (May 2026) vs 4.1% (Dec 2025); baseline 3.1% by Dec 2026; historical average 4.2%; US 5.0% (May 2026), baseline 3.5% Dec 2026. https://www.ftportfolios.com/blogs/InvestBlog/2026/6/22/factoid---monday,-june-22,-2026 . Earlier Moody's forecasts for Dec 2025 (~2.6% global/2.7% US) were missed (First Trust July 2025 factoid, search summary; **CHECK**).
- A "73% of the default universe at the 2025 peak, up from ~9% in early 2020" LME figure circulates attributed to the Harvard Law School Bankruptcy Roundtable; not verifiable this session — do **not** print without a primary source.
- UBS AM 2025 Fixed Income Default Study (Jan 17, 2025): USD HY 2025 expected default 4.8% (3.1% ex two large distressed names); EUR HY 3.3%; maturity walls for 2025/2026 ~40%/25% lower than a year earlier. https://www.ubs.com/global/en/assetmanagement/insights/asset-class-perspectives/fixed-income/articles/2025-fixed-income-default-study.html (VERIFIED).

### 6D. Trend data: CDS market structure for the bootstrap section
- ISDA, *Single-name CDS Market Update*, May 2023 (VERIFIED PDF https://www.isda.org/a/0jLgE/Single-name-CDS-Market-Update.pdf): quarterly single-name traded notional ranged \$405bn–\$1.1tn over 2018–Q1 2023, trough Q4 2020, five-year peak \$1.1tn in Q1 2023 (bank-failure hedging); names trading per quarter fell from 854 (Q1 2018) to 719 (Q1 2023); 1,169 entities traded at least once in five years, 600 traded less than once a quarter, 496 traded every quarter and made up >80% of activity; only a handful average ≥10 trades/day (≤3% of names); Q1 2023 clearing: 87.4% of index CDS notional, 51.2% of single-name; year-end 2022 CCP open interest ≈\$2.9tn, IM \$70.1bn; real-time public reporting of US single-name CDS since February 2022.
- BIS OTC derivatives statistics, end-Dec 2023 (pub. May 16, 2024, VERIFIED https://www.bis.org/publ/otc_hy2405.htm): CDS notional \$8.5tn (down from \$9.9tn at mid-2023); 65% centrally cleared (70% at mid-2023); total OTC notional \$667tn. End-June 2024 (pub. Nov 21, 2024, VERIFIED https://www.bis.org/publ/otc_hy2411.htm): credit derivatives \$9.2tn, −9% y/y.
- ISDA CDS Standard Model (VERIFIED https://cdsmodel.com/): open-source C code, "copyright of ISDA," administered by S&P Global Market Intelligence; purpose: standardize upfront↔spread conversion; ISDA Standard Rate Curves migrating from rfr.ihsmarkit.com to rfr.spglobal.com, old site shut after Aug 15, 2026 (news dated June 15, 2026). MathWorks `cdsbootstrap` (VERIFIED https://www.mathworks.com/help/finance/cdsbootstrap.html): "the survival probability is defined in terms of a piecewise constant hazard rate," default recovery 0.4, warns on "non-monotone default probabilities (that is, negative hazard rates)."

### 6E. Case-study facts (see §7 for narrative)
- **SVB** (Wikipedia, VERIFIED secondary; **CHECK** against FDIC/Fed reports): Mar 8, 2023 sold >\$21bn securities at \$1.8bn loss and announced \$2.25bn raise; Mar 9 \$42bn withdrawals; Mar 10 seized; \$209bn assets (Dec 31, 2022 call report); ~86–89% uninsured deposits; >\$15bn unrealized HTM losses on \$91.3bn portfolio.
- **Hertz** (SEC Form S-1, Oct 2021, VERIFIED https://www.sec.gov/Archives/edgar/data/1657853/000110465921126784/tm2128732-1_s1.htm): old common got \$1.53 cash/share + pro rata 3% of new common + choice of public warrants (89,049,029 warrants, \$13.80 strike, expiring June 30, 2051) or rights (\$10.00/share, up to \$1.6bn; \$1.3bn subscribed; backstop fee \$164mm in stock). Emergence June 30/July 1, 2021. Wikipedia (VERIFIED secondary): filed May 22, 2020; stock from \$0.59 to \$5.50 (≈1000%) in June 2020; June 11, 2020 sought up to \$1bn equity sale with "could ultimately be worthless" warning; \$29mm sold before SEC halted; delisted Oct 2020.
- **Carvana** (SEC 8-K Ex. 99.1, July 19, 2023, VERIFIED https://www.sec.gov/Archives/edgar/data/1690820/000119312523189188/d537573dex991.htm ; 10-Q Q3 2023 VERIFIED https://www.sec.gov/Archives/edgar/data/1690820/000169082023000323/cvna-20230930.htm): TSA with holders of >90% (~\$5.2bn) of senior unsecured notes; completed Sept 1, 2023 with 96.4% participation; \$5.52bn unsecured exchanged for \$4.2bn new senior secured notes (ADESA/Carvana collateral) plus \$341mm cash tender for 2025s; debt cut >\$1.2–1.325bn; cash interest savings >\$430–455mm/yr for two years; FY2023 10-K records \$878mm gain on extinguishment. Equity path (approx., **CHECK**): ≈\$370 peak Aug 2021; ≈\$3.7 low Dec 2022; strong 2023–25 recovery; \$58.83 close Oct 16, 2026 (stockanalysis.com, VERIFIED).
- **First Brands** (Wikipedia, VERIFIED secondary; **CHECK** dockets): Ch. 11 Sept 2025, S.D. Tex., Case 25-90399; liabilities \$10–50bn vs assets \$1–10bn; Raistone said \$2.3bn "simply vanished"; UBS O'Connor >\$500mm exposure; Jefferies/Point Bonita \$715mm receivables; Norinchukin/Mitsui JV \$1.75bn; prosecutors allege double-pledged receivables; indictments Jan 29, 2026; converted to Ch. 7 Sept 1, 2026.

### 6F. Open questions for later editions (unresolved this session)
Moody's EDF9/EDF-X methodology changes 2022–2026 (**CHECK**); ISDA model's SOFR-discounting switch date (**CHECK**); 2024–2026 single-name CDS volume rebound figures (DTCC/ISDA SwapsInfo, **CHECK**); current ISDA standard recovery assumptions by seniority/region (**CHECK**); peer-reviewed DD-based SVB studies (none found; only vendor PD series).

---

## 7. Case studies

**A. SVB, March 2023: the structural model that fired, and the structural model that can't fire.** Vendor Merton-type PD flagged SVB from Sept 2022 and peaked at 6% on Dec 6, 2022 (S&P MI; **CHECK**). Yet Nagel–Purnanandam show *why* bank DD is structurally understated: bank assets are short puts on borrowers' assets, so $\sigma_V$ rises as asset values fall, and a \$91.3bn HTM book with >\$15bn of unrealized losses is a mark-to-model asset in a mark-to-market model. The desk lesson: for financials, replace lognormal $V$ with a concave payoff and let $\sigma_V$ be state-dependent; treat the Mar 9 \$42bn run as a jump, not a diffusion. Hand-off to Ch 23 for the vol-surface view.

**B. Carvana 2022–23 / Hertz 2020–21: the call option that would not expire.** Carvana's equity fell ~99% peak-to-trough (approx.) while unsecured notes traded at deep discounts; a Merton DD computed on Dec 2022 inputs would have been near zero. The July 19, 2023 TSA with >90% of holders exchanged \$5.52bn unsecured into \$4.2bn secured (completed Sept 1, 2023), cutting debt >\$1.2bn and cash interest >\$430mm/yr: a *negotiated barrier move* (the strike for old unsecureds fell; collateral was pledged; $F$ shrank; time value was bought). Equity then rallied for two years. Hertz: equity at \$0.59 post-filing, \$5.50 in June 2020, \$29mm sold under a "could be worthless" warning before the SEC stopped it; at emergence old holders received \$1.53 cash + 3% equity + warrants/rights worth real money. Both show Merton's payoff diagram is right and his *timing* assumption (default at $T$, absorbing barrier) is what breaks: exchanges reset $F$ and $T$. Systematic flag: DD momentum turning up while CDS curve inverted; equity–credit hedge ratio (Dynkin p.87) collapsing to the HY tail.

**C. First Brands 2025 (short, in §6.9): no equity, no DD.** A private issuer with \$10–50bn liabilities, opaque receivables financing, and alleged double-pledging. Bohn–Stein p.159's warning about off-balance-sheet liabilities in the default point is the whole case. Desk lesson: for private credit you must infer $\sigma_V$ from peer equity, loan marks, or an intensity fitted to syndicated-loan prices; "the model had no input" is not a defense. Bridge to Ch 17.

---

## 8. Humor beats (canon cast; each rides a correct idea)

1. **Itô as the IRS of randomness** (style bible calibration line): extend — "the $\tfrac12\sigma^2$ is withheld at source, and no, you cannot deduct it against convexity."
2. **Kaz misreads "springing lien"** in 6.5: asks whether it is seasonal. Theo: "It springs when a ratio is breached." Kaz: "So it's a barrier with a Heaviside function." Correct, and the section's point.
3. **The 13-week model reborn** (6.1/6.8): Theo renames column N from "Runway" to $S(t)$; Kaz points out he has been bootstrapping piecewise-constant hazards since analyst year one, "just with worse fonts."
4. **ROBO literalism** (6.4): told "compute distance to default," ROBO returned 1,420 miles — the distance from the desk to the Southern District of Texas. The precise spec gives units: standard deviations of $\ln V$ at a 1-year horizon.
5. **ROBO literalism** (6.11): told "use equity volatility," ROBO used 1-day $\sigma_E$ unannualized and reported a 0.00% PD for the entire HY index; Mags asked if it had been reading rating-agency outlooks.
6. **Mags on the credit triangle** (6.8): "Forty percent recovery is a convention. In thirty years I have never been handed exactly forty." Correct idea: $R$ in $s\approx\lambda(1-R)$ is a $\mathbb{Q}$ quoting convention, not a forecast (Schmid p.95: numeraires).
7. **Ines's hand** (6.10): Hertz equity in June 2020 was a drawing hand — retail paid \$5.50 for a call that paid \$1.53 + 3% + warrants. "Pot odds were bad; the hand still hit. Don't confuse the two." Markouts replay: who sold them the stock (the company, via an ATM) and what that said.
8. **Merton's short-end problem** (6.2): "A Merton firm cannot default tomorrow unless it is already dead today. Mags has a list of firms that disagree, alphabetized."
9. **Cov-lite as deleted barrier** (6.5): "A maintenance covenant is a Black–Cox barrier. A cov-lite loan is a Black–Cox barrier that was removed in 2017 and nobody told the model."
10. **Feller condition** (6.7): "Keep $2\kappa\theta\ge\sigma^2$ or your hazard rate will visit zero and ROBO will declare the issuer immortal."
11. **$\mathbb{P}$ vs $\mathbb{Q}$** (6.3, Ines): "Physical PDs are what happens. Risk-neutral PDs are what the table charges you to find out. The difference is the rake, and on this desk we are the house."

---

## 9. Resource-graph candidates

**VERIFIED-URL (fetched or search-listed this session):** cdsmodel.com (ISDA CDS Standard Model) · MathWorks cdsbootstrap https://www.mathworks.com/help/finance/cdsbootstrap.html · ISDA Single-name CDS Market Update PDF https://www.isda.org/a/0jLgE/Single-name-CDS-Market-Update.pdf · BIS OTC stats https://www.bis.org/publ/otc_hy2405.htm and https://www.bis.org/publ/otc_hy2411.htm · NBER w25807 https://www.nber.org/papers/w25807 · Duffie–Lando PDF https://www.darrellduffie.com/uploads/1/4/8/0/148007615/duffielando2001.pdf · Econometrica page (above) · IDEAS Bai–Goldstein–Yang https://ideas.repec.org/a/eee/jfinec/v137y2020i2p297-319.html · LBS Feldhütter–Schaefer https://lbsresearch.london.edu/id/eprint/953 · SEC Carvana 8-K/10-Q and Hertz S-1 (above) · Quinn Emanuel LME article (above) · UBS 2025 default study (above) · First Trust factoid (above) · SFI 20-110 Goyal et al. (search-listed) · arXiv 1811.08038 (search-listed) · risk.net JCF equity-implied rating (search-listed) · Moody's CreditEdge quick reference PDF (search-listed) · Python `merton` package docs https://merton.readthedocs.io/en/stable/api/merton/calibration/kmv_iterative/index.html (search-listed) · R `credule` vignette https://ftp.kaist.ac.kr/CRAN/web/packages/credule/vignettes/credule.Rmd (search-listed) · canonical roots: https://www.sec.gov/edgar , https://www.isda.org , https://www.bis.org/statistics .

**TITLE-ONLY:** Lando (1998) RDR; CIR (1985); Crosbie & Bohn (2003); O'Kane & Turnbull (2003); O'Kane (2008); Lando (2004) *Credit Risk Modeling*; Schönbucher (2003); Brigo & Mercurio (2006); Glasserman (2004) *Monte Carlo Methods in Financial Engineering*; Vasicek (1984); Kealhofer (2003a,b) FAJ; Leland (1994); Leland & Toft (1996); Zhou (2001); Eom, Helwege & Huang (2004); Huang & Huang (2012); Vassalou & Xing (2004); Campbell, Hilscher & Szilagyi (2008); Duffie, Saita & Wang (2007); Berndt, Douglas, Duffie & Ferguson (2018); Schaefer & Strebulaev (2008); Du, Elkamhi & Ericsson (2019) (**CHECK**); Culp, Nozawa & Veronesi (2018) (**CHECK**).

**Podcasts:** not verifiable this session (search budget exhausted). Give TITLE-ONLY search targets for the writer: Bloomberg *Odd Lots* episodes on LMEs and private credit; *Flirting with Models* episodes on credit factor investing; ISDA's own podcast series (an episode page exists at https://www.isda.org/2026/10/01/episode-60-modelling-margin/ — VERIFIED-URL but not credit-model specific). Do not invent episode numbers.

---

## 10. Exploratory-space notes (future sections / chapters)

1. **Ch 6-B "Incomplete Information and the Structural–Reduced-Form Ladder":** Duffie–Lando, Giesecke, CreditGrades (2002), and a desk recipe for choosing the model by horizon and data quality; the Duffie–Lando intensity formula in terms of accounting noise. (New chapter.)
2. **"Banks Are Not Merton Firms":** Nagel–Purnanandam concave-asset model, state-dependent $\sigma_V$, deposit-run jumps; SVB/First Republic/Credit Suisse 2023 as the dataset. (Section in 6-B or Ch 23.)
3. **"The Barrier Is Negotiable: First-Passage Models in the LMT Era":** multi-tranche first-passage with priority ladders; uptier as a strike shift for non-participants; drop-down as a reduction in $V$ available to the restricted group; distressed exchange as partial absorption (re-default hazard after an LME). Needs S&P/Moody's re-default data. (Section for Ch 13/14, derivation here.)
4. **"Structural Models Without Equity":** private credit, BDC marks, peer-equity $\sigma_V$ transfer, intensity fitted to loan marks; First Brands/Tricolor as cases. (Section for Ch 17; derivation seed here.)
5. **"Affine Jump-Diffusion Intensities and the Jump Premium":** Duffie–Pan–Singleton transforms; Bai–Goldstein–Yang's jump risk premium; CDS-implied jump-to-default for market-making (feeds Ch 18 JTD term).
6. **"Hazard Curve Trading":** inverted curves in distress, negative-hazard arbitrage (arXiv 1811.08038), upfront/standard-coupon mechanics, SOFR curve migration; bridge to Ch 24 basis.
7. **"Merton Meets Machine Learning":** structure-constrained ML (Goyal et al.), DD as a feature with purged CV (Ch 7), isotonic DD→PD mapping as a spec; equity-implied ratings for unrated firms.
8. **"DD Momentum and Equity→Credit Lead–Lag as Trend Signals":** time series of $DD$ and $\lambda^{\mathbb{Q}}/\lambda^{\mathbb{P}}$ as trend inputs; Man 2022 p.31 spillover evidence; test in 2020/2022/2025 drawdowns. (Section for Ch 10.)
9. **"Endogenous Default and the Sponsor's Option":** Leland–Toft, Anderson–Sundaresan strategic debt service → the sponsor's LME option as a real option; links Ch 13 game theory to this chapter's barrier math.
10. **Appendix candidate:** a verified table of ISDA standard-model conventions (coupons, recovery by seniority/region, IMM roll dates, day counts, curve sources) once primary ISDA documentation is fetched.

<!-- STATUS: COMPLETE -->
