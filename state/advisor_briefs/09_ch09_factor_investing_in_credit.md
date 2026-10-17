# Advisor Brief — Chapter 9: Factor Investing in Corporate Credit

*Fable advisor dissection for Edition 1. Target file: `book_src/09_ch09_factor_investing_in_credit.md`. Research date: 2026-10-17. Shelf citations are PDF page indices from `tools/pdf_search.py`. Web facts carry the URL fetched this session; anything I could not confirm is marked CHECK. Note to writer: this turn's web-search budget was exhausted mid-dossier (shared across agents), so several secondary items are flagged TITLE-ONLY rather than linked. Everything marked VERIFIED was fetched and read.*

---

## 1. Thesis and the "aha" for an ex-PJT-RSSG reader

**Thesis.** A credit factor is a *rule for sorting bonds* that, after you strip out the one thing every sort secretly loads on (spread risk, measured as DTS), still earns money net of a transaction cost that is five to twenty times larger than in equities. Everything in the chapter is a consequence of three facts that have no equity analogue:

1. **Spread is both the signal and the risk.** In equities, a value sort is not a beta sort. In credit, every sort on anything spread-adjacent (value, carry, "cheapness") is mechanically a sort on DTS, and DTS *is* beta: under Ben Dor's proportional-spread law, $\beta_i \approx \text{DTS}_i/\text{DTS}_m$. Market-value-neutral long-short credit factors are therefore long-beta portfolios wearing a hedge-fund costume. Dynkin's Table 19.4 shows the costume coming off: ESP's correlation with the IG index falls from +44% to −22% once you DTS-match the legs (Dynkin p.741).
2. **Costs are first-order, not a footnote.** Barclays' top-decile equity-momentum portfolio made 6.34%/yr over the index with IR 1.90 *before* costs and was *negative after* costs at 73%/month turnover (Dynkin p.633). Factor investing in credit is a turnover-budgeting problem with a signal attached.
3. **The data lie, and they lie asymmetrically.** TRACE prices carry measurement error that sits in both the sorting signal and the return denominator; filtering returns after seeing them embeds look-ahead. Those two mechanisms inflated the published literature so badly that a JFE paper was retracted (Bai–Bali–Wen 2019, retraction notice JFE 150(3), 2023), only ~23% of literature factors survive Dick-Nielsen–Feldhütter–Pedersen–Stolborg's clean framework (QuantPedia summary, VERIFIED), and the April 2026 Dickerson–Robotti–Rossetti paper finds most of 108 signals have no bond-CAPM alpha after correction (arXiv 2604.07880, VERIFIED).

**The RSSG "aha."** The reader has spent years deciding whether *one* bond is cheap given its covenant package, collateral, and the sponsor's appetite for an uptier. A credit factor model is that same judgment run on 10,000 CUSIPs with the covenant read replaced by three ratios (leverage, net debt/EBITDA, interest coverage) inside a peer group (rating × sector × maturity). The aha is twofold: (a) the ESP regression residual is literally "the spread the market is paying you that the fundamentals don't explain," which is the RSSG analyst's day job expressed as $\epsilon_i$; and (b) the factor zoo's biggest documented alpha-killer is not competition but *bad prices*, which the reader already knows from marking a B3 loan to a stale dealer run. Man's remark that value is "particularly CUSIP-specific" (Man 2022 p.25) is the invitation: within a capital structure, after controlling for subordination and duration, residual mispricing remains, and the person who can read *why* (a guarantor gap, a springing lien, an LMT-blocker) has a feature nobody else's regression contains. Chapter 13's Priming Risk Score is the obvious extra regressor; set that hook here.

**The trend spine.** Three dated arcs run through the chapter: the 2019–2026 replication crisis (a trend in *epistemics*); the collapse of transaction costs from Chen–Lesmond–Wei's 25bp/180bp world to LCS of ~0.6% round-trip (a trend in *implementability*, which is why systematic credit is $90–140bn and growing); and the regime arc from 2020's spread spike through 2022's rates shock to Sept-2025 IG OAS at ~72bp, the tightest since 1998 (SSGA, VERIFIED), which compresses the value dispersion every factor feeds on.

---

## 2. Section outline (7,000–10,000 words)

Anatomy key: **DF** desk framing · **DER** derivation · **SPEC** AI spec block · **SRC** source extraction · **CASE** case study · **RG** resource graph · **TW** Trend Watch.

- **Cold open (≤400 words).** Theo's first factor backtest: value L/S, Sharpe 1.9, Kaz delighted. Ines asks for the beta. It is 0.6. Mags: "So you built the index with extra steps and called it alpha." Chapter question: *what is left after you take the spread risk out?* "By the end of this chapter you will be able to..."
- **9.1 What a factor is in credit, and why it is not what it is in equities.** DF (the spread-is-signal-and-risk problem). SRC: Dynkin p.514–515 (unique challenges), Man 2022 p.23. TW #1: *Systematic credit's share of the market, 2018–2026* (Blackstone "20% of equities vs <2% of FI"; Barclays QPS $90–140bn via Impax; BCBS >$40bn CHECK; Robeco MFC EUR 1.04bn; SSGA SAFI conversion Dec 31 2023).
- **9.2 DTS: the beta you did not know you had.** DER: proportional spread changes → $\sigma(r^{xs}) \propto \text{DTS}$ → $\beta_i = \text{DTS}_i/\text{DTS}_m$ → why MV-neutral L/S is long beta → DTS-neutral construction. SRC: Ben Dor p.34, p.51, p.61; Dynkin p.739, p.741. SPEC: DTS-neutral leg scaler.
- **9.3 Value: ESP, SPiDER, and the fair-spread family.** DER: within-cell regression, residual ranking; SPiDER as model-free; structural fair spread (Correia–Richardson–Tuna) with the $\mathbb{P}\to\mathbb{Q}$ step; Man's `OAS/(ND/EBITDA).clip(0.1)`. SRC: Dynkin p.524, p.528 (decile table), p.553; Man p.24–25. CASE (mini): Man Numeric telecom 2016–17 signal path (Man p.29–30).
- **9.4 Momentum: bond momentum, equity momentum in credit, and the decay clock.** DER: formation windows, EMC scaling, transition-matrix half-life, break-even turnover. SRC: Dynkin p.606, p.610, p.633; Man p.25. Cross-reference Ch 10 (time-series trend) and Ch 3 (equity→credit lead-lag as information flow).
- **9.5 Carry and low-risk (defensive): the two factors that are really one risk sort in disguise.** DER: carry = OAS + roll-down; IPR's defensive = leverage, gross profitability, low duration; the maturity-IR decline (Dynkin ch. 11); Man's asymmetry argument. SRC: Man p.26; Dynkin p.454–456; IPR 2018 (web, VERIFIED).
- **9.6 Quality, size (the factor that isn't), and the "informed investor."** DER: ESI = shares on loan / shares outstanding; why bond short interest is subsumed in IG (market-making shorts); Bayesian reading of short interest as informed flow (ties to Ch 3 Glosten–Milgrom). SRC: Dynkin p.679 (size), p.793–794 (ESI); Man p.26–27.
- **9.7 Combining factors: correlations, IC-weighting, and the Henke matrix.** DER: $IR_{combo}$ from component IRs and the correlation matrix; effective breadth under issuer clustering; IPR's combined Sharpe 2.19 vs best single 1.75. SRC: Man p.27–28 (correlation matrix and IR chart, with the "no costs" footnote); IPR Table 4.
- **9.8 Portfolio construction under costs: LCS, TES, turnover buffers, turnover budgets, long-only.** DER: the optimizer with DTS cell-matching, KRD matching, issuer DTS caps, LCS cost term, turnover constraint; hysteresis buffers. SRC: Ben Dor p.118, p.153; Dynkin p.703, p.711, p.538; Man p.19–21 (TC = inside spread + slippage + calibration). SPEC: full reference implementation (see §4). TW #2: *The cost curve 2007–2026* (LCS 0.4%→2.8%→0.6%; Chen–Lesmond–Wei 25/180bp; Robeco fund 0.20%/yr; Man's HY bid-ask spike Feb–Mar 2020).
- **9.9 The replication debate, 2019–2026.** DER: Blume–Stambaugh upward bias from price noise, correlated errors-in-variables when sorting on noisy prices, look-ahead from ex-post return filters, survivorship from dropping defaults. CASE: the Bai–Bali–Wen retraction and the Open Bond Asset Pricing project. TW #3: *Timeline of the factor-zoo cull* (BBW 2019 → DMR JFE 2023 → retraction 2023 → DFPS 2023/RFS forthcoming → OBAP site Nov 2025 → DRR & DJM Apr 2026).
- **9.10 Crowding, capacity, and the 2020/2022 drawdowns.** DF (Paleologo's "copy of the same portfolio"); measures (overlap, factor valuation spread, leg-level short interest); Dynkin's DTS-neutral drawdown table; PGGM's "KISS vs sophisticated" survey (TITLE-ONLY); 2022 as the low-risk/duration year; Sept-2025 tights. CASE: March 2020 through the factor lens.
- **9.11 Desk Debrief**, **The Spec You Hand the Robot**, exercises. RG after every major section.

---

## 3. Derivation skeletons

All expectations state their measure. Factor construction is under $\mathbb{P}$ (we forecast realized excess returns); only the structural fair-spread leg of value touches $\mathbb{Q}$.

### 3.1 DTS and the hidden beta (§9.2)

Excess return over duration-matched Treasuries, one period, bond $i$:
$$
r^{xs}_{i,t+1} \;\approx\; \underbrace{s_{i,t}\,\Delta t}_{\text{carry}} \;-\; D^{\text{spr}}_{i,t}\,\Delta s_{i,t+1} \;+\; \text{(convexity, default jump)}.
$$
Ben Dor's empirical law: spread changes are proportional to spread level, $\Delta s_i = s_i\,\eta_i$ with $\eta_i$ the *relative* spread change. Then
$$
r^{xs}_{i} \approx s_i\Delta t - \text{DTS}_i\,\eta_i,\qquad \text{DTS}_i \equiv D^{\text{spr}}_i\, s_i,\qquad
\sigma(r^{xs}_i)\approx \text{DTS}_i\,\sigma_\eta .
$$
(Ben Dor p.34 eq. 1.4; p.51: regression of excess-return vol on DTS has 98% fit and slope 8.8%/month in that sample.) Decompose $\eta_i = \eta_{m} + \tilde\eta_i$ (common relative move plus idiosyncratic). Market excess return $r_m \approx -\text{DTS}_m\,\eta_m$ (carry aside). Therefore
$$
\beta_i \;=\; \frac{\operatorname{Cov}(r^{xs}_i, r_m)}{\operatorname{Var}(r_m)} \;=\; \frac{\text{DTS}_i}{\text{DTS}_m}.
$$
**Consequence for a factor sort.** A long-short portfolio with legs $L,S$ and market-value weights has $\beta_{LS} = (\text{DTS}_L - \text{DTS}_S)/\text{DTS}_m$. Any sort correlated with spread (value, carry, "cheap vs. rich") has $\text{DTS}_L > \text{DTS}_S$, hence positive beta: the "alpha" is partly carry on borrowed beta. **DTS-neutral construction:** scale leg $k$'s returns by $\text{DTS}^\ast/\text{DTS}_{k,t}$ with a common target (Barclays uses 12, the IG index's time-average DTS in years × %) (Dynkin p.739). Equivalent weight statement: choose $w$ with $\sum_{i\in L} w_i\text{DTS}_i = \sum_{i\in S} w_i\text{DTS}_i$, ideally per rating × sector cell.

**Error-prone spots.** (i) Units: DTS in years × percent vs years × bp differs by 100; say which. (ii) Using OAS duration vs. modified duration on callables. (iii) DTS-matching on *beginning-of-month* DTS only; re-scaling with end-of-month DTS is look-ahead. (iv) In HY the proportionality weakens near distress because the default jump is not a relative spread change: cap DTS-based scaling for $s > $ ~1,000bp or treat distressed names separately (Ch 5/14). (v) Within-issuer: Man p.13–14 shows bonds of one issuer diverge massively; DTS-neutral at issuer level is not DTS-neutral at bond level.

### 3.2 Value (§9.3)

**ESP (Barclays).** For peer group $g$ = rating × sector × maturity bucket, run monthly
$$
s_{i,t} = a_{g(i),t} + b_{1,t}\,\text{Lev}_{i,t} + b_{2,t}\,\frac{\text{ND}}{\text{EBITDA}}_{i,t} + b_{3,t}\,\text{ICov}_{i,t} + \epsilon_{i,t},
\qquad \text{ESP}_{i,t} = \operatorname{rank}_{\text{index}}(\hat\epsilon_{i,t})\in\{1,\dots,10\}.
$$
(Dynkin p.692–693 gives exactly these three ratios; financials use LT debt / LT assets only.) High residual = cheap. Dynkin p.528 decile table with leverage: D1 −1.10%/yr (IR −0.27), D10 +3.29%/yr (IR 0.53); L/S IR > 1.5 (p.545).

**SPiDER (Barclays).** Model-free, aggregable across time and sectors:
$$
\text{SPiDER}_{i,t} = \frac{s_{i,t}}{\text{Debt}_{i,t}/\overline{\text{EBITDA}}^{\text{LT}}_{i,t}} .
$$
Man's raw value signal is the same idea with a floor: `OAS / (Net Debt/EBITDA).clip(lower=0.1)` (Man p.24), then risk-adjust (size, PD, vol) and compare within rating/sector.

**Structural fair spread (Correia–Richardson–Tuna 2012; CHECK details).** From a Merton/KMV physical PD, map to $\mathbb{Q}$ and to spread:
$$
\text{PD}^{\mathbb{Q}}_T = N\!\left(N^{-1}(\text{PD}^{\mathbb{P}}_T) + \lambda_{\text{SR}}\sqrt{T}\right),\qquad
s^{\text{fair}}_i \approx -\frac{1}{T}\ln\!\left(1-\text{PD}^{\mathbb{Q}}_T\,L\right)\approx \lambda^{\mathbb{Q}} L,
$$
value $= s_i - s^{\text{fair}}_i$. **Measure trap:** if you skip the $\mathbb{P}\to\mathbb{Q}$ step you call every bond cheap (physical PDs are too small). A cross-sectional *rank* is unaffected by a monotone mapping, but any *level* comparison (e.g., "spread per unit of expected loss") is not. Dynkin p.553 states the trade-off plainly: regression fair spreads overfit and have unstable coefficients; structural ones are parameter-hungry and opaque; SPiDER is neither.

**Error-prone spots.** Negative/tiny EBITDA (hence the clip); book vs market leverage; point-in-time fundamentals (lag ≥ 3 months, no restatements); OAS vs Z-spread on callable HY (use OAS or you "find" value in every make-whole); peer cells with < ~15 bonds → pool or shrink $b$ toward the global estimate; winsorize residuals at 1/99 before ranking; and the biggest: residual = cheapness *or* information you lack (an LMT, a guarantee gap). That is the RSSG edge and the Ch 13 hook.

### 3.3 Momentum (§9.4)

Credit momentum (IPR 2018): trailing six-month bond excess return, $\text{MOM}^{\text{cr}}_{i,t}=\sum_{k=1}^{6} r^{xs}_{i,t-k}$ (skip-month convention: CHECK per paper). Equity momentum in credit (Barclays):
$$
\text{EMC}_{i,t} = \tfrac13\sum_{h\in\{1,3,6\}} \frac{R^{E}_{i,t-h\to t}}{h}\quad\text{(scaled per month)},
$$
ranked 1–10 at issuer level (Dynkin p.693). **Decay:** Dynkin p.610's 3-month transition matrix: only 17% of D10 issuers remain D10. Treat the decile rank as a Markov chain; estimate a half-life from the diagonal: $\tau_{1/2} = -3\ln 2/\ln(p_{\text{stay}})$ months (a crude but honest "signal clock"; with $p_{\text{stay}}=0.17$ this is about 1.2 months, which is why monthly rebalancing is barely enough and quarterly is a compromise). Realized decay of returns (p.611): 35, 22, 19bp in months 1–3; 95bp cumulative over six months, ~80% in the first three.

**Break-even turnover.** With one-way turnover $\text{TO}$ per month and round-trip cost $c$ (LCS), $\mathbb{E}^{\mathbb{P}}[r_{\text{net}}] = \mathbb{E}^{\mathbb{P}}[r_{\text{gross}}] - \text{TO}\cdot c$. Dynkin p.633: $\text{TO}=73\%$/month, gross 6.34%/yr over index, net negative. Solve $c^\ast$ and show the writer's table: at LCS 0.6% round-trip, break-even monthly turnover for 2.5%/yr gross is about 35%.

### 3.4 Carry and low-risk (§9.5)

Carry (Koijen–Moskowitz–Pedersen–Vrugt definition, via Man p.26 and IPR p.7–8): return if prices do not change. For a bond, $\text{carry}_i = s_i\,\Delta t + \text{roll-down}_i$, with roll-down $\approx -D^{\text{spr}}_i\,(\partial s/\partial T)\,\Delta t$ along the issuer curve. IPR use OAS alone and say why (flat-curve approximation; curve-fitting adds opacity). Carry's Q5−Q1 Sharpe in IPR is 0.35, the only characteristic without a $t\ge3$ premium: carry is mostly DTS.

Low-risk/defensive: IPR's composite = low market leverage, high gross profitability, low duration; they *exclude* beta and volatility because DTS confounds duration (good) with spread (carry). The maturity evidence (Dynkin ch. 11): IRs fall almost monotonically with maturity over 1994–2019, decomposed into roll-down, bear-steepening, and downgrade drift. Man p.26's asymmetry: the upside tightening is bounded by the risk-free rate; the downside is a jump to recovery. Formally, with $R$ the recovery, the one-period payoff distribution is a mixture (Ch 5): capped at roughly $P + D^{\text{spr}} s$ and floored at $R$, so expected-return-per-unit-vol falls as $s$ rises if the jump intensity rises faster than linearly in spread.

### 3.5 Informed investor (§9.6)

$$
\text{ESI}_{j,t} = \frac{\text{shares on loan}_{j,t}}{\text{shares outstanding}_{j,t}},\qquad
\text{BSI}_{i,t} = \frac{\text{par on loan}_{i,t}}{\text{par outstanding}_{i,t}} .
$$
Dynkin p.793–794: high ESI (within rating) predicts downgrades over 3–12 months and index underperformance; BSI is subsumed by ESI, and useless in IG because IG shorts are dealer inventory shorts. Bayesian framing for Ch 3 continuity: short interest is the posterior-shifting signal $\Pr(\text{informed}\mid \text{ESI})$; the *change* in ESI, not the level, is the news. Man's version adds options positioning ("call/put positioning," Man p.27). Man's standalone IR for Informed Investor is 0.79 (simulated, no costs; Man p.28), the lowest of their four, but Dynkin p.794 reports that ESI+ESP "achieves almost twice the risk-adjusted return" of either alone: it is a *combination* factor.

### 3.6 Combination (§9.7)

With component IRs $\text{IR}_k$, weights $w$ and factor-return correlation $\rho$:
$$
\text{IR}_{\text{combo}} = \frac{w^\top \text{IR}}{\sqrt{w^\top \rho\, w}} .
$$
Use Henke et al.'s IG matrix as reproduced in Man p.27 (Value–Carry 0.52, Value–Size −0.10, Quality–Carry −0.21, Momentum–Quality −0.07, Momentum–Carry 0.02, Value–Momentum 0.00, Value–Quality −0.04; HY analogues on the same page). IPR Table 4: Q5−Q1 Sharpe carry 0.35, defensive 1.11, momentum 0.85, value 1.75, combined (equal-risk) 2.19. Then the breadth caveat: $\text{IR}=\text{IC}\sqrt{\text{BR}}$ with effective breadth $\text{BR}_{\text{eff}} \approx N/(1+(\bar n-1)\bar\rho_{\text{within}})$ for $\bar n$ bonds per issuer with within-issuer correlation $\bar\rho_{\text{within}}$ ("47 bonds from one issuer are one data point wearing 47 hats", Ch 7).

### 3.7 Portfolio construction with costs (§9.8)

$$
\max_{w}\; \alpha^\top w - \tfrac{\gamma}{2}\,w^\top\Sigma w - \sum_i c_i\,|w_i - w_{i,0}|
$$
subject to: $\sum_{i\in \text{cell}} w_i\,\text{DTS}_i = \text{DTS}^{\text{bm}}_{\text{cell}}$ for each rating × sector cell (Ben Dor p.33–34: express active bets as DTS contributions); key-rate durations matched to benchmark (Man p.10); issuer DTS contribution $w_j\,D_j\,s_j \le \kappa$ (Ben Dor p.61: with $\kappa=5$ in % × years × %, a 100bp/5y issuer can be 1%, a 150bp/10y issuer 0.33%); liquidity filter $\text{TES}_i \le 3$ (Dynkin p.710); one-way turnover $\le 10\%$/month (IPR); long-only $w\ge0$ where mandated. Cost $c_i = \tfrac12\text{LCS}_i$ per side with $\text{LCS}_i = (\text{ask}-\text{bid})_{\text{spread}}\times \text{OASD}_i$ for spread-quoted bonds or $(P^{\text{ask}}-P^{\text{bid}})/P^{\text{bid}}$ for price-quoted (Ben Dor p.118). Covariance $\Sigma$: Man's DTS-adjusted statistical factor model (Man p.15: normalize returns by DTS, PCA, fill new issues from issuer-level loadings, rescale by current DTS). **Turnover buffer** as hysteresis: buy if score $\ge \theta_B$, sell if $\le \theta_S$, hold otherwise; Dynkin p.538 shows IR falling 1.52 → 1.31 → 1.20 as the buffer widens 0 → 10% → 15% *before* costs, while the net picture improves. **Error-prone spots:** $\ell_1$ cost term needs a solver that handles it (reformulate with $w = w_0 + u^+ - u^-$); ill-conditioned $\Sigma$ for 10,000 bonds with 2,000 issuers (shrink; Ch 8); DTS cells with one bond; fills are probabilistic (Man p.19: an unfilled order leaves an unmodelled exposure).

### 3.8 Replication mechanics (§9.9)

Observed price $\tilde P_t = P_t(1+u_t)$, $u_t$ iid, $\mathbb{E}u=0$, $\operatorname{Var}u=\sigma_u^2$. Computed return $\tilde r_{t+1} = \tilde P_{t+1}/\tilde P_t - 1$. Then
$$
\mathbb{E}[\tilde r_{t+1}] \approx \mathbb{E}[r_{t+1}] + \sigma_u^2
$$
(Blume–Stambaugh 1983 bias; TITLE-ONLY), largest where $\sigma_u$ is largest: small, illiquid, low-priced, high-yield bonds. Sorting on a noisy price-based signal makes it worse: conditioning on a low $\tilde P_t$ selects negative $u_t$, which mean-reverts, so $\mathbb{E}[\tilde r_{t+1}\mid \tilde P_t\text{ low}] > \mathbb{E}[r_{t+1}]$: a spurious "reversal/value/illiquidity" premium. Dickerson–Robotti–Rossetti call this *correlated errors-in-variables* because the error sits in both the sort and the return denominator (arXiv 2604.07880 abstract, VERIFIED). Second mechanism: filtering out returns after observing them (e.g., dropping $|r|>x$ or bounce-backs asymmetrically) is conditioning on the future. Third: dropping defaulted bonds truncates the left tail of exactly the high-carry portfolios. The fix set used by DFPS: automated error filters, individual review of extreme outliers, keep default-month returns, value-weight, tertiles, double-sort on rating group, test alphas against CMKT and TERM (QuantPedia summary of SSRN 4586652, VERIFIED).

---

## 4. Code spec: the reference implementation

**Name:** `credit_factor_lab.py` (single block or sequential blocks; numpy/pandas only, seeded).

**What it builds.**
1. **Synthetic universe:** $N=2{,}000$ bonds from $J=400$ issuers (Poisson bonds per issuer, mean 5), each with sector (8), rating bucket (Aaa–A, Baa, Ba, B, CCC), maturity (1–30y), OAS drawn lognormally by rating, OASD from maturity, leverage/ND-EBITDA/coverage drawn with rating-dependent means, plus an *issuer-level* equity return series.
2. **Data-generating process for excess returns (monthly, $T=240$):** $r^{xs}_{i,t} = s_i/12 - \text{DTS}_i(\eta_{m,t} + \eta_{\text{sec},t} + \tilde\eta_{i,t}) + \text{jump}_{i,t} + \text{alpha}_{i,t}$, where the planted alpha loads on (a) the ESP residual with a small IC (~0.03), (b) lagged issuer equity return (EMC) with decay, and (c) nothing for size. Jumps: rating-dependent default intensity with recovery 40% *(illustrative)*.
3. **Signals:** `esp_score()` (within-cell OLS on the three ratios, rank residual 1–10), `spider()`, `credit_momentum()` (6m sum), `emc()` (1/3/6-month scaled), `esi()` (random with planted link to downgrades), `low_risk()` (short maturity × high rating).
4. **Portfolios:** market-value-weighted decile L/S vs **DTS-neutral** L/S (legs rescaled to a target DTS at the beginning of each month); long-only optimized tilt with cell-level DTS matching and a turnover cap (greedy or simple quadratic solve; no cvxpy).
5. **Costs:** LCS-like cost per bond $= \text{bidask}_{\text{spread}}\times\text{OASD}$ with rating- and size-dependent bid-ask; net returns $= $ gross $-$ one-way turnover × cost.
6. **Replication module:** add iid multiplicative price noise $u$ with $\sigma_u$ rising for small/HY bonds; recompute returns from noisy prices; re-run a "short-term reversal" and a "value" sort.

**Outputs:** table of gross/net annualized return, vol, IR, beta to market, turnover for each factor under MV-neutral vs DTS-neutral construction; combination IR with and without DTS neutrality; the noise-bias table.

**Built-in sanity checks (asserts, with tolerances):**
- **DTS-beta check:** under the DGP with no alpha, the OLS beta of a random DTS-sorted long-short must be within 10% of $(\text{DTS}_L-\text{DTS}_S)/\text{DTS}_m$; the DTS-neutral version must have $|\beta| < 0.05$.
- **Vol-linearity check:** regress excess-return vol on DTS across 30 buckets; slope > 0, intercept not significantly different from zero (Ben Dor Figure 1.12 analogue).
- **Blume–Stambaugh check:** the mean of noisy returns exceeds the mean of clean returns by $\sigma_u^2 \pm 20\%$ when $\sigma_u$ is homogeneous; the reversal L/S built on noisy prices shows a positive "alpha" that disappears (within $t<1$) when the sort uses *lagged* clean mid prices.
- **Combination check:** equal-risk combo IR $\ge$ max single-factor IR when the empirical factor-return correlation matrix has all off-diagonals $<0.3$ (else print a warning rather than fail).
- **Cost check:** net return is monotone decreasing in turnover cap; top-decile EMC with no buffer has lower net return than the 10%-buffered version.

**Edge cases to state in the spec:** months where a peer cell has < 5 bonds (fallback to coarser cell); bonds that default (return = recovery − price, then drop next month, never retroactively); new issues (no momentum history → NaN, excluded from momentum but not value); negative EBITDA (clip to 0.1× as Man does); DTS of zero/negative OAS (floor at 1bp).

---

## 5. Source map (shelf pages, with the exact short quotation to use)

| Cite | Why | Verbatim quotation (≤60 words) |
|---|---|---|
| Ben_Dor p.34 | DTS definition, the core identity | "just as spread duration is the sensitivity to an absolute change in spread (e.g., spreads widen by 5 bps), DTS (D · s) is the sensitivity to a relative change in spread." |
| Ben_Dor p.51 | Equal-DTS portfolios are equally risky | "a portfolio of high-spread bonds with short duration can be as risky as a portfolio comprised of low-spread bonds with high duration as long as they both have roughly the same DTS." |
| Ben_Dor p.61 | Issuer limits via DTS contribution | "a position in issuer A, with a spread of 100 bps and a duration of five years, could be up to 1% of portfolio market value; while a position in issuer B, with a spread of 150 and an average duration of 10 years, would be limited to 0.33%." |
| Ben_Dor p.118 | LCS definition | "A bond's LCS, therefore, represents the roundtrip cost, as a percent of the bond's value, of immediately executing a standard institutional transaction." |
| Dynkin p.45 | The "uncrowded space" claim (dated book, 2020-ish; use as a trend marker) | "Scientific credit investing stands today where scientific equity investing stood at the turn of the century: in an uncrowded space and on the threshold of considerable secular growth." |
| Dynkin p.524 | ESP definition | "We identify relative value as the portion of excess spread over peers unexplained by fundamental factors and call this measure excess spread to peers (ESP)." |
| Dynkin p.528 | ESP decile table (rebuild as our own table: D1 −1.10%/yr IR −0.27 … D10 3.29%/yr IR 0.53) | (table; cite numbers, do not transcribe wholesale) |
| Dynkin p.553 | Taxonomy of fair-spread methods | "While a regression is able to control for multiple risk characteristics at the same time, it is vulnerable to statistical problems, such as overfitting and instability in coefficients." |
| Dynkin p.606 | EMC decile spread | "The bottom decile portfolio (D1) contains bonds with the weakest or most negative equity momentum. It delivered negative average excess return of –4.7% per year between 1993 and 2017. In contrast, the average excess return of the top decile portfolio (D10), with the strongest equity momentum, was +4.01% per year." |
| Dynkin p.610 | Momentum decay | "an issuer with equity momentum in the top 10% (D10) has only a 17% probability of remaining top ranked after three months" |
| Dynkin p.633 | Costs eat momentum | "Turnover is very high (73% per month) and performance before transaction costs is also very high (return of 7.31%/yr, or 6.34%/yr in excess of the index, with information ratio of 1.90 over the index) but transaction costs are so large that, once accounted for, both absolute and relative performance becomes negative." |
| Dynkin p.679 | Size is not a credit factor | "Our findings generally do not support the existence of a size factor that could be exploited by credit investors the same way many equity investors systematically favor smaller‐capitalization stocks with a view to enhance returns." |
| Dynkin p.693 | ESP's three ratios | "Three fundamental ratios are used to capture variation in excess spreads: financial leverage, net debt to earnings before interest, tax, and depreciation (EBITDA), and interest coverage." |
| Dynkin p.703 | LCS time series (trend) | "The average LCS of the corporate market overall increased from 0.4% in 2007 to 2.8% in 2008 and then declined to 0.6% in 2018–2019." |
| Dynkin p.711 | Net-of-cost strategy | "Accounting for the rebalancing costs reduces relative returns from 2.66%/yr to 1.78%/yr, while the tracking error volatility remains virtually unchanged at 1.41%/yr." |
| Dynkin p.739 | DTS-neutral legs | "We address potential exposure mismatches between the long and short legs of all strategies by normalizing the DTS exposures of each leg to a common target level of 12, the time average DTS of the credit index." |
| Dynkin p.741 | Directionality removed | "In the case of ESP, adjusting for DTS reduces correlations with US Corporate Index excess returns from 34% to –6% in drawdown episodes and from 44% to –22% in other (benign) periods." |
| Dynkin p.794 | Bond short interest in IG | "bond short interest is not a useful indicator in the IG space as IG bonds are likely shorted as part of market‐making activity." |
| Man_2022 p.24 | Man's value signal | "We begin by processing the raw data for the investment universe, looking at OAS per unit of leverage measured as Net Debt to EBITDA." (and the schematic line `OAS / (Net Debt/EBITDA).clip(lower=0.1)`) |
| Man_2022 p.25 | CUSIP-specific value | "Value stands out as being particularly CUSIP-specific, that is to say that within the same capital structure, even after accounting for liquidity, subordination, duration, etc., mispricing can remain." |
| Man_2022 p.26 | Size verdict; low-risk asymmetry | "We have seen little evidence to suggest that Size is a meaningful factor in quant credit, especially after transaction costs" / "the tightening of a bond on the upside to risk free rates is typically asymmetrically smaller than the jump to recovery in situations of distress." |
| Man_2022 p.27 | Informed Investor definition | "The Informed Investor style factor looks to exploit information about investor activity to drive investment decisions, working along a 'wisdom of crowds' thesis. This harnesses data points such as short interest and call/put positioning to build a picture of investor activity across markets." |
| Man_2022 p.28 | The IR chart and its footnote | "Value IR 2.15 Momentum IR 1.69 Quality IR 1.55 Informed Investor IR 0.79 Final IR 2.35" and, from footnote 12: "These results do not directly account for liquidity, transaction costs, and borrow costs." (Jan 1, 2005–Dec 31, 2020, simulated.) |
| Man_2022 p.19 | Turnover by factor | "Within classic quant, Momentum tends to have the highest turnover of any factor approach while both Size and Quality see the least churn." |
| Man_2022 p.20 | Stale academic cost assumptions | "In that paper, the bid-ask spread for AAA-rated corporate bonds was estimated at 25bps, while for CCC-rated bonds it was 180bps. Both of these figures would be markedly tighter in the current market." |
| Man_2022 p.21 | TC model | "TC = Inside Market Spread + Slippage + Spread Calibration" |
| Blackstone p.2 | Penetration trend | "While systematic strategies manage roughly 20% of global equities, they account for less than 2% of the fixed-income universe." |
| BlackRock p.6 | Quality as default avoidance (bridge to Ch 11) | "Our proprietary probability of default signal that has underpinned all of our credit strategies for over 20 years has successfully identified 77% of the defaulted bonds in the ICE BofA High Yield Index within 24 months of its default since 2010." |
| Paleologo p.71 | Crowding definition (writer: confirm the sentence opening on the page) | "every hedge fund holds a copy of the same portfolio, then this factor is a measure of “crowding”" |
| Paleologo p.27 | Division of labor alpha/beta | "To estimate 𝛼 as accurately as possible is the job of the fundamental investor. To estimate 𝛽, identify the correct benchmarks m, and the returns 𝜖 is the job of the quantitative risk manager." |

Also useful, no quote needed: Dynkin p.454–456 (maturity IR decline, 1994–2019); p.570–572 (DTS-implied vs realized vol, DTS-matched IRs); p.659/682 (small issuers' LCS >50% higher; SML −67bp/yr IG, −32bp/yr HY, 1994–2018); p.702–704 (LCS coverage; July 2019 IG 0.608%, HY 0.941%; TES); p.729 n.11 (DTS introduced by Barclays QPS with Robeco, 2005); Man p.10–11 (10,000 bonds/2,000 issuers vs ~100 liquid US CDS names; L/S leverage "starts at 4-5x"); Man p.15 (DTS-adjusted SFRM); Man p.29–30 (telecom case); Man p.30 (PGGM "KISS" survey); Ben Dor p.153–154 (LCS-constrained tracking portfolios); BlackRock p.3 (2022: HY −11%, Agg −13%; 2023: HY +13%).

---

## 6. RESEARCH DOSSIER (dated, sourced)

### 6.1 The replication crisis, 2019–2026 (the chapter's epistemic trend)

- **Bai, Bali & Wen (2019)**, "Common risk factors in the cross-section of corporate bond returns," *JFE* 131(3): 619–642 — the downside-risk/credit-risk/liquidity-risk factor model that became the field's benchmark. **Retracted.** Retraction notice: *JFE* 150(3), 2023, article 103721, DOI 10.1016/j.jfineco.2023.103721, authors Bai, Bali, Wen (EconPapers listing, VERIFIED: https://econpapers.repec.org/article/eeejfinec/v_3a150_3ay_3a2023_3ai_3a3_3as0304405x23001617.htm). Per the search-engine summary of the ScienceDirect notice (page itself 403'd; CHECK wording): authors requested retraction after Dickerson, Mueller & Robotti identified a temporal misalignment of data series; in corrected data the factors add no explanatory power over the bond market factor, with the marginal exception of the liquidity factor. Month reported as December 2023 — CHECK.
- **Dickerson, Mueller & Robotti (2023)**, "Priced risk in corporate bonds," *JFE* 150(2). arXiv version 2604.05699 posted 7 Apr 2026 (VERIFIED: https://arxiv.org/abs/2604.05699). Abstract: common factor pricing in corporate bonds "is exceedingly difficult to establish"; previously proposed bond factors have no incremental power over the bond market factor, traded liquidity a "marginal exception"; the bond CAPM is not dominated in pairwise or multiple-model tests.
- **Dick-Nielsen, Feldhütter, Pedersen & Stolborg (2023→)**, "Corporate Bond Factors: Replication Failures and a New Framework." SSRN 4586652 (listing VERIFIED via AQR page; SSRN itself 403'd); AQR working-paper page dated 5 Oct 2023 (VERIFIED: https://www.aqr.com/Insights/Research/Working-Paper/Corporate-Bond-Factors-Replication-Failures-and-a-New-Framework). Status "Review of Financial Studies, forthcoming" per Dick-Nielsen's research page (search summary; CHECK). Key findings per QuantPedia's summary (VERIFIED: https://quantpedia.com/corporate-bond-factors-replication-failures-and-a-new-framework/): "only 23% of the factors considered significant in the literature have significant alphas using our framework"; under original papers' own data choices only one factor stays significant; under other papers' choices none; framework = clean data with individual review of outliers, keep returns around defaults, value weights, tertiles, double sorts on three rating groups, firm-level representative bonds, alphas vs CMKT and TERM; several equity signals work for bonds; CAPM also fails. Data: Lasse Pedersen's data page links "Data on corporate bond factors" hosted at stolborg.com/data (VERIFIED listing: https://www.lhpedersen.com/data; the stolborg link currently redirects to a 404 — CHECK).
- **Dickerson, Robotti & Rossetti (2026)**, "The Corporate Bond Factor Replication Crisis," arXiv 2604.07880, submitted 9 Apr 2026 (VERIFIED: https://arxiv.org/abs/2604.07880). Two inflation mechanisms: measurement error in transaction prices entering both sorting signals and return denominators (correlated errors-in-variables), and asymmetric ex-post return filtering (look-ahead). Applied to 108 signals in nine thematic clusters; after correction most do not produce significant bond-CAPM alphas. Releases "Open Bond Asset Pricing."
- **Dickerson, Julliard & Mueller (2026)**, "The Co-Pricing Factor Zoo," arXiv 2604.04430, submitted 6 Apr 2026 (VERIFIED: https://arxiv.org/abs/2604.04430). ~18 quadrillion candidate models; once Treasury term-structure risk is accounted for, equity and nontradable factors explain bond premia, making the bond factor literature "largely redundant" for that purpose; a Bayesian-model-averaged SDF over dozens of factors reaches an out-of-sample Sharpe of 1.5–1.8. Origin: Inquire Europe project "The Corporate Bond Factor Zoo," announced 26 Nov 2023, scheduled to finish Summer 2024 (VERIFIED: https://www.inquire-europe.org/news/new-reseach-started-the-corporate-bond-factor-zoo/).
- **Open Bond Asset Pricing** (VERIFIED: https://openbondassetpricing.com/). Contributors: Dickerson (UNSW), Mueller & Robotti (Warwick), Julliard (LSE), Nozawa (Toronto), Rossetti (Warwick), Fang (Drexel). Provides: daily/monthly TRACE-based bond data via WRDS Contributed Data; a TRACE pipeline (Stage 0 transaction cleaning; Stage 1 daily panel, public beta 2025-12-11); 108 bond factors (DRR 2026); 341 factors from excess bond returns ("Factor Investing with Delays," Dickerson–Nozawa–Robotti 2024); Co-Pricing Factor Zoo factors; ML panel of 341 bond and stock predictors, 2002-07 to 2022-12; duration-matched Treasury returns from van Binsbergen, Nozawa & Schwert (2024; "Duration-Based Valuation of Corporate Bonds," forthcoming *RFS*); corrected Bai–Bali–Wen factors. Site announced 2025-11-06; main paper under R&R so data may change.
- **Kelly, Palhares & Pruitt (2023)**, "Modeling Corporate Bond Returns," *Journal of Finance*, DOI 10.1111/jofi.13233, pp. 1967–2008 (bibliographic data from search; Wiley page 403'd). Conditional five-factor model with time-varying loadings; large improvement over prior models; "high out-of-sample Sharpe ratio suggests that the credit risk premium is notably larger than previously estimated." Method is IPCA — CHECK (not confirmed from fetched text).
- **Chordia, Goyal, Nozawa, Subrahmanyam & Tong (2017)**, "Are Capital Market Anomalies Common to Equity and Corporate Bond Markets?" *JFQA* 52(4): 1301–1342, DOI 10.1017/S0022109017000515 (VERIFIED: https://www.cambridge.org/core/product/identifier/S0022109017000515/type/journal_article). Past equity returns positively predict bond returns (equity leads); profitability and asset growth *negatively* related to bond returns (collateral/risk story); after trading costs most predictors do not deliver high Sharpe ratios. The earliest clear "costs kill it" warning.
- **Dick-Nielsen & Rossi (2019)**, "The Cost of Immediacy for Corporate Bonds," *RFS* 32(1) (journal page VERIFIED by title/volume; authors from the citation trail, CHECK numbers before quoting).

**Writer's framing of the trend:** the number that survived the cull is small but not zero. What survives looks like (i) equity-derived signals (momentum spillover, profitability/quality), (ii) value-type signals built on clean prices with DTS control, and (iii) low-risk/short-duration. What died looks like anything built on noisy price levels (short-term reversal, naive illiquidity, "downside risk" from bond return history). That maps exactly onto practitioner behavior (Man, Barclays, Robeco) and is the chapter's reconciliation of academia and the desk.

### 6.2 The canonical practitioner papers (with the numbers the writer should use)

- **Houweling & van Zundert (2017)**, "Factor Investing in the Corporate Bond Market," *FAJ* 73(2), 1 Apr 2017, DOI 10.2469/faj.v73.n2.1 (VERIFIED: https://rpc.cfainstitute.org/research/financial-analysts-journal/2017/factor-investing-in-the-corporate-bond-market); SSRN 2516322 (listing seen in search; not fetched). Factors: size (small issuers by bonds outstanding), low-risk (short maturity, high rating), value (spread vs model fair spread), momentum (past returns). Alphas economically and statistically significant; multi-factor has lower TE and higher IR; results survive costs, alternative definitions, liquid-subsample; credit factors add value beyond equity factors in multi-asset. Note the one disagreement with Barclays and Man: size. Dynkin p.679 and Man p.26 say no; H&vZ say yes; the reconciliation is liquidity (Dynkin p.659: small issuers' LCS >50% higher; Blume–Stambaugh bias concentrates there).
- **Israel, Palhares & Richardson (2018)**, "Common Factors in Corporate Bond Returns," *JOIM* 16(2): 17–46 (VERIFIED from the AQR-hosted PDF, text extracted). Sample Jan 1997–Apr 2015, US IG+HY. Definitions: carry = OAS; defensive = low market leverage (net debt / (net debt + equity)), high gross profitability (Novy-Marx), low duration, explicitly *excluding* beta and vol because DTS confounds duration and spread; momentum = trailing 6-month bond excess return and 6-month issuer equity return; value = spread vs fundamentals. Characteristics demeaned within five ex-ante DTS quintiles (duration and carry exempt). Fama–MacBeth $t\ge3$ for all but carry. Table 4 Q5−Q1 Sharpe: carry 0.35, defensive 1.11, momentum 0.85, value 1.75, combined 2.19 (constant-vol versions 0.19/1.21/1.12/1.80/2.32). Long-only optimized portfolio with turnover ≤10% and transaction costs: net Sharpe 1.03 vs benchmark 0.69; active net return 2.20%/yr, IR 0.86, TE 2.56%. They deliberately exclude size "as the corporate bond market is notoriously expensive to trade."
- **Henke, Kaufmann, Messow & Fang-Klingler (2020)**, "Factor Investing in Credit" (journal CHECK; cited by Man p.26–27 for (a) quality's weak relation to IG performance and (b) the pairwise factor correlation matrices reproduced on Man p.27). TITLE-ONLY.
- **Koijen, Moskowitz, Pedersen & Vrugt (2018)**, "Carry," *JFE* (DOI 10.1016/j.jfineco.2017.11.002 resolves to an Elsevier PII but the page was not read; CHECK volume/pages). Man p.26 quotes carry Sharpe 0.4–0.5 across asset classes.
- **Jostova, Nikolova, Philipov & Stahel (2013)**, "Momentum in Corporate Bond Returns," *RFS* 26(7), July 2013 (journal page VERIFIED by title/issue; authors from citation trail). Momentum is in non-investment grade, not IG (Man p.25 paraphrase). Headline 64bp/month in HY — CHECK.
- **Haesen, Houweling & van Zundert (2017)**, "Momentum Spillover from Stocks to Corporate Bonds," *JBF* 79: 28–41 (citation from Dynkin p.728; DOI 10.1016/j.jbankfin.2017.03.001 redirects to Elsevier, page not read). Residual (market-stripped) equity momentum improves risk properties; Dynkin p.631 finds it does *not* improve their EMC. Good "two desks, two answers" box.
- **Correia, Richardson & Tuna (2012)**, "Value Investing in Credit Markets," *Review of Accounting Studies* 17(3): 572–609 (citation from Dynkin p.728; Springer page behind cookie wall). Structural fair spread via $\mathbb{P}\to\mathbb{Q}$ PD.
- **Asquith, Au, Covert & Pathak (2013)**, "The Market for Borrowing Corporate Bonds," *JFE* — TITLE-ONLY (DOI guess resolved to Elsevier, not read). Background for bond short interest's weak signal.
- **Hendershott, Kozhan & Raman**, "Short Selling and Price Discovery in Corporate Bonds," *JFQA* (2020) — TITLE-ONLY. (Note: a DOI I tried resolved to an unrelated Bollerslev–Li–Zhao paper; do not cite any DOI for this one.)
- **Alquist, Israel & Moskowitz (2018)**, "Fact, Fiction, and the Size Effect," *JPM* — TITLE-ONLY (Man p.26 cites it against size in bonds).
- **AQR Alternative Thinking (Oct 2017)**, "The Illusion of Active Fixed Income Alpha" — TITLE-ONLY (Man p.23 n.9 quotes: "we detect little evidence of manager skill"; my URL guess 404'd).
- **Blume & Stambaugh (1983)**, "Biases in Computed Returns: An Application to the Size Effect," *JFE* — TITLE-ONLY; the $\sigma_u^2$ bias.
- **Frazzini & Pedersen (2014)**, "Betting Against Beta," *JFE* — TITLE-ONLY (DOI redirect not read); includes credit evidence per IPR's citation.

### 6.3 Industry and AUM trend data (2018–2026)

- **Penetration:** Blackstone BCBS paper: "systematic strategies manage roughly 20% of global equities, they account for less than 2% of the fixed-income universe" (Blackstone p.2, shelf).
- **Size of the quant-credit pool:** "between US$90bn and US$140bn" AUM in funds using quantitative screening in IG/HY, forecast to grow faster than fixed income overall; source Barclays QPS & Credit Research, Mateer et al. 2024, "QPS & Credit Research: Better Together," as cited by Impax, 19 Sep 2025 (VERIFIED: https://impaxam.com/insights-and-news/blog/quant-meets-credit-enhancing-fundamental-analysis-through-systematic-screening/). Same source for the *quantamental* numbers: issuer-return hit rate in US IG rose from ~58% to ~66% when analyst and quant signals aligned and fell to ~52% when they conflicted; focusing on aligned decisions raised excess return from 2.0% to 3.7%/yr and IR from 1.09 to 1.71; doubling exposure to aligned signals gave 4.1% and IR 1.83. Use in §9.6/9.10 as the Barclays answer to "do we need the humans."
- **Blackstone Corporate Bond Strategies (ex-DCI):** "over $40 billion in AUM… largest pure play systematic credit manager" per the search-engine excerpt of blackstone.com/corporate-bond-strategies (page 403'd; undated; CHECK).
- **Robeco QI Global Multi-Factor Credits** (FH EUR share class LU1235145304; VERIFIED fund page as of 30-09-2026: https://www.robeco.com/en-int/products/funds/isin-lu1235145304/robeco-qi-global-multi-factor-credits-fh-eur): inception 15-06-2015; fund size EUR 1,039mm; benchmark Bloomberg Global Aggregate Corporates (hedged); 1y −2.69% vs −2.77%; 3y 3.14% vs 3.45%; 5y −2.00% vs −1.64%; since inception 0.63% vs 0.87% (annualized, net); transaction costs 0.20%/yr (3-year average). Attribution to 30-09-2026: value slightly positive; the **low-risk/quality factor was the largest detractor, driven by an underweight in longer-dated bonds**; momentum neutral; size slightly negative. This is a live, dated example of the defensive factor's duration tilt costing money when the long end rallies: the writer should use it as the honest counterweight to the backtests. Robeco's 2022 piece (search summary only; CHECK): 45bp/yr outperformance since launch, Sharpe 0.36 vs 0.25, +51bp 2022-YTD.
- **Robeco Guide to Credits (c. Q1 2017, PDF VERIFIED):** credit team EUR 23bn (end-2016); "over EUR 26 billion in factor strategies in credit and equity"; two factor credit strategies, Conservative Credits (low-risk) and Multi-Factor Credits (Low Risk, Value, Momentum, Size); "We are wary of crowded trades where investors stretch the models"; DTS developed 2004 with Barclays (Dynkin p.729 n.11 says introduced 2005). Also on the SSRN 2014 origin of Houweling–van Zundert.
- **State Street SAFI Q3 2025 commentary**, 25 Nov 2025 (VERIFIED: https://www.ssga.com/us/en/institutional/insights/fixed-income-q3-2025-safi-commentary): two Systematic US High Quality Corporate strategies converted to the systematic process effective 31 Dec 2023; Q3 2025 value contributed +14bp (intermediate) and +43bp (long), momentum flat/+4bp; since-inception IRs 2.89 and 2.63 (short sample); max relative drawdown since Jan 2024 −5bp vs peer average −44bp; during the Q1 2025 credit drawdown SAFI was roughly flat net while average credit managers underperformed by 35bp in March–April; IG OAS tightened from ~77bp (4 Jul 2025) to ~72bp (Sep 2025), "the tightest since 1998." Dated, sourced, perfect for the tight-spread Trend Watch.
- **Man Group 2022 (shelf):** cash-bond universe >10,000 instruments / ~2,000 issuers vs ~100 regularly traded US CDS names plus ~200 sporadic (p.10–11); L/S leverage "starts at 4-5x" (p.11); prime brokers now provide daily borrow availability across the cash-bond universe (p.11); PGGM survey "Will corona be a watershed moment for credit factor investing?" (IPE, 2020; URL in Man's footnote; page returned 405 — TITLE-ONLY).
- **Barclays' own trend statement:** Dynkin p.49–50 (book intro): systematic approaches growing "as a result of the increased availability of fixed income data, improved price transparency, and the influence of established quantitative insights from the equity markets."

### 6.4 Transaction-cost trend data

- Chen, Lesmond & Wei (2007) estimates still used by academics: 25bp (AAA) to 180bp (CCC) bid-ask; "markedly tighter" today (Man p.20).
- Barclays LCS, IG index average: 0.4% (2007) → 2.8% (2008) → 0.6% (2018–19) (Dynkin p.703); July 2019: IG 0.608%, HY 0.941%, Treasuries 0.028% (Dynkin p.703 table); 2007–09 IG range 0.59%–3.40% (Ben Dor p.112).
- Man's HY 20-day-average bid-ask spiked in Feb–Mar 2020 and normalized within months (Man p.20 chart; levels not legible in text, describe qualitatively).
- Net-of-cost outcomes: Barclays ESP+EMC liquid strategy portfolio 2.66%→1.78%/yr, cost drag 1.15%/yr in 2007–12 vs 0.64%/yr in 2013–19 (Dynkin p.711): the cost drag *halved* across the electronification decade. Robeco MFC realized 0.20%/yr transaction costs (fund page, 2026).
- IPR long-only: gross 5.72% → net 5.26%/yr with ≤10% monthly turnover.

### 6.5 Drawdowns and regimes (for §9.10 and the Trend Watch boxes)

- **2008 and 2020 through DTS-neutral eyes:** without DTS matching ESP is pro-cyclical and EMC contra-cyclical (flight to quality lowers top-EMC DTS); with DTS matching both "delivered strong performance during all drawdown episodes" and correlations with the market collapse (Dynkin p.739–741; sample Jan 1993–Mar 2020).
- **2020:** IG spread path Feb 2020–Feb 2021 (Man p.12 chart: launch in January → large March MTM loss → recouped by year-end); PGGM's "KISS vs sophisticated" split (Man p.30).
- **2022:** HY −11%, Agg −13%, S&P −18% (BlackRock p.3); 2023: HY +13%, S&P +26%, Agg +5%. The low-risk factor = short-duration tilt, so 2022 is the defensive factor's year in total-return space even though excess-return factor math is duration-hedged; make the writer distinguish the two.
- **2025:** Q1 credit drawdown (SAFI flat vs peers −35bp); September IG OAS ~72bp, tightest since 1998 (SSGA). Low dispersion compresses value's opportunity set: Dynkin p.545 notes ESP outperformance "is larger when there is a high dispersion in ESP."
- **2026 live attribution:** Robeco MFC's low-risk/quality detraction from the long-end underweight (fund page).

### 6.6 Crowding and capacity

- Paleologo p.71–72: AMH factor as crowding proxy; deleveraging cycle diagram; p.29 crowding as "the thesis with respect to the consensus among informed investors."
- Dynkin p.45: "uncrowded space" (as of the book's writing, ~2020).
- Robeco (2017 guide): "wary of crowded trades where investors stretch the models."
- Man p.41–42 (search snippet): expects edge to be "spread over more quant investors" as electronification continues; Man p.30: simple models decay faster, complex ones risk overfitting.
- Quantitative crowding measures the writer can define (no external source needed): pairwise holdings overlap between factor portfolios; factor valuation spread $VS_t = \bar s_{\text{cheap}}/\bar s_{\text{rich}}$ within DTS-matched cells; leg-level ESI/BSI; turnover-weighted share of TRACE volume in top-decile names. Mark all numbers illustrative.

---

## 7. Case studies

### Case 1 — The retraction: Bai–Bali–Wen (2019) and the birth of Open Bond Asset Pricing (2019–2026)
Facts (all from §6.1): JFE 131(3) 2019 paper; DMR "Priced risk in corporate bonds," JFE 150(2) 2023 shows no incremental power after fixing a temporal misalignment; authors' retraction notice JFE 150(3) 2023, DOI 10.1016/j.jfineco.2023.103721; DFPS (AQR WP 5 Oct 2023; SSRN 4586652): 23% survive; OBAP site 6 Nov 2025, TRACE pipeline beta 11 Dec 2025, WRDS contributed data; DRR 9 Apr 2026 (108 signals, errors-in-variables + ex-post filtering); DJM 6 Apr 2026 (co-pricing, BMA SDF OOS Sharpe 1.5–1.8). **How a systematic desk reads it:** every in-house factor library needs (a) a prices-from-mid-not-last-trade rule, (b) a no-ex-post-filter rule, (c) defaults kept in the sample, (d) DTS double sorts, (e) a replication against OBAP's public series as a CI test. **Humor hook:** Kaz finds out that the benchmark paper for his whole thesis was retracted and asks whether a journal can "reorganize under Chapter 11."

### Case 2 — March 2020 through the factor lens
Facts: IG spread spike and round trip (Man p.12); HY bid-ask spike and normalization (Man p.20); Barclays drawdown table showing raw ESP losing and raw EMC winning, both winning once DTS-matched (Dynkin p.739–741); PGGM survey split (Man p.30; TITLE-ONLY); cost drag halved 2007–12 → 2013–19 (Dynkin p.711) as context for why 2020's liquidity hole was survivable. Price paths beyond these should be marked *approximate*. **Desk lesson:** a factor book's March 2020 P&L was mostly its net DTS, not its signals.

### Case 3 — Man Numeric's telecom, 2016–2017 (the multi-factor signal in one issuer)
Facts (Man p.29–30, anonymized issuer): 2016 company events (customer retention stabilizes, liquidity concerns relieved, \$500mm cost cuts; 2017 FCF breakeven, EBITDA margin 25%→30%); value and quality strengthen from distressed levels; Informed Investor turns cautiously positive on bond and equity short interest; cross-asset (ecosystem) momentum turns positive; OAS chart runs from roughly 1,200bp to tights *(approximate, read from chart)* and the combined signal flips from strongly positive to monetizing. **Why it matters:** it is the only shelf example that shows the four Man factors disagreeing and then agreeing, which is the whole argument for combination (§9.7). Pair with the live 2025–26 vignette (SSGA Q1 2025; Robeco 2026 attribution) so the chapter has one anonymized backtest and two dated, named, sourced live results.

---

## 8. Humor beats (each rides a correct idea)

1. **Cold open:** Theo's "Sharpe 1.9" value strategy has beta 0.6. Ines: "What's the pot, what are the odds, and who at this table knows more than you? Right now the answer to the third one is 'the index.'" Mags: "You built the index with extra steps." (Idea: MV-neutral spread sorts are long beta; $\beta = \text{DTS}_L/\text{DTS}_S$-driven.)
2. **ROBO literalism:** Theo specs "neutralize spread exposure." ROBO sets both legs to zero DTS by buying only Treasuries. Precise spec: equalize *beginning-of-month* DTS contributions per rating × sector cell at a target of 12 (years × %). (Idea: DTS-neutral ≠ zero DTS; units and timing.)
3. **Kaz vs legal vocabulary:** Kaz hears "fallen angel" and asks which Greek letter that is. Mags: "It's the one where the insurance company sells you a BBB− bond at 11 a.m. because its policy says so and buys it back from you at 2 p.m. because its other policy says so." (Idea: index/ratings constraints are structural factors; bridge to Dynkin Part II.)
4. **"IDO or it didn't happen":** Kaz's momentum backtest, IR 1.90, at 73% monthly turnover. Ines runs the hand history with LCS: the strategy pays the dealer more than it makes. "Congratulations, you've invented a very elaborate way to tip." (Dynkin p.633.)
5. **The 13-week model returns:** Theo asks why the value regression has three ratios and no "weeks of liquidity." Kaz: "Because nobody put it in the panel." Theo puts it in the panel. It helps in B/CCC and does nothing in A. (Idea: the RSSG feature belongs where default risk is near; foreshadows Ch 11/13.)
6. **Mags's "back in my day":** on bond borrow. "In 1998 shorting a bond meant calling a man named Sal and asking nicely. Now your prime broker emails you a spreadsheet." Then grudging respect: "Fine. The spreadsheet is better than Sal." (Man p.11.)
7. **Size, the factor that wasn't:** "In equities, small is beautiful. In credit, small is a bond nobody will quote you, whose price is a rumor, whose return is the rumor's variance." (Blume–Stambaugh $\sigma_u^2$; Dynkin p.659/679; Man p.26.)
8. **The retraction:** Kaz discovers the benchmark paper was retracted and asks whether a journal can file under Chapter 11. Mags: "It did an out-of-court restructuring. The creditors were Dickerson, Mueller, and Robotti." (Cooperation agreements signed in this book so far: unchanged.)
9. **Desk Myth vs. Desk Reality box:** *Myth:* "Carry is a factor." *Reality:* "Carry is the price of DTS. If your carry factor has alpha after DTS-matching, you have found a value factor and should rename it before compliance does." (IPR: carry $t<3$, Sharpe 0.35.)
10. **Poker Table (Ines) on crowding:** "Everyone at the table has the same hand history, the same model, and the same exit. That's not an edge, that's a fire drill." (Paleologo p.71–72 deleveraging cycle.)

---

## 9. Resource-graph candidates

**Academic papers**
- VERIFIED-URL: Dickerson, Robotti & Rossetti (2026), *The Corporate Bond Factor Replication Crisis*, https://arxiv.org/abs/2604.07880
- VERIFIED-URL: Dickerson, Mueller & Robotti (2023/2026 arXiv), *Priced Risk in Corporate Bonds*, https://arxiv.org/abs/2604.05699 (JFE 150(2), 2023)
- VERIFIED-URL: Dickerson, Julliard & Mueller (2026), *The Co-Pricing Factor Zoo*, https://arxiv.org/abs/2604.04430
- VERIFIED-URL: Dick-Nielsen, Feldhütter, Pedersen & Stolborg (2023), *Corporate Bond Factors: Replication Failures and a New Framework*, https://www.aqr.com/Insights/Research/Working-Paper/Corporate-Bond-Factors-Replication-Failures-and-a-New-Framework (SSRN 4586652)
- VERIFIED-URL: Bai, Bali & Wen retraction notice, JFE 150(3) 2023, DOI 10.1016/j.jfineco.2023.103721, https://econpapers.repec.org/article/eeejfinec/v_3a150_3ay_3a2023_3ai_3a3_3as0304405x23001617.htm
- VERIFIED-URL: Houweling & van Zundert (2017), FAJ 73(2), DOI 10.2469/faj.v73.n2.1, https://rpc.cfainstitute.org/research/financial-analysts-journal/2017/factor-investing-in-the-corporate-bond-market
- VERIFIED-URL: Israel, Palhares & Richardson (2018), JOIM 16(2), https://www.aqr.com/-/media/AQR/Documents/Journal-Articles/Common-Factors-in-Corporate-Bond-Returns.pdf
- VERIFIED-URL: Chordia, Goyal, Nozawa, Subrahmanyam & Tong (2017), JFQA 52(4), https://www.cambridge.org/core/product/identifier/S0022109017000515/type/journal_article
- VERIFIED-URL: Inquire Europe project note (26 Nov 2023), https://www.inquire-europe.org/news/new-reseach-started-the-corporate-bond-factor-zoo/
- TITLE-ONLY: Kelly, Palhares & Pruitt (2023), *Modeling Corporate Bond Returns*, JF (DOI 10.1111/jofi.13233 from search; page not fetched)
- TITLE-ONLY: Jostova, Nikolova, Philipov & Stahel (2013), *Momentum in Corporate Bond Returns*, RFS 26(7)
- TITLE-ONLY: Koijen, Moskowitz, Pedersen & Vrugt (2018), *Carry*, JFE
- TITLE-ONLY: Correia, Richardson & Tuna (2012), *Value Investing in Credit Markets*, RAS 17(3)
- TITLE-ONLY: Haesen, Houweling & van Zundert (2017), *Momentum Spillover from Stocks to Corporate Bonds*, JBF 79
- TITLE-ONLY: Henke, Kaufmann, Messow & Fang-Klingler (2020), *Factor Investing in Credit*
- TITLE-ONLY: Dick-Nielsen & Rossi (2019), *The Cost of Immediacy for Corporate Bonds*, RFS 32(1)
- TITLE-ONLY: Asquith, Au, Covert & Pathak (2013), *The Market for Borrowing Corporate Bonds*, JFE
- TITLE-ONLY: Hendershott, Kozhan & Raman (2020), *Short Selling and Price Discovery in Corporate Bonds*, JFQA
- TITLE-ONLY: Alquist, Israel & Moskowitz (2018), *Fact, Fiction, and the Size Effect*, JPM
- TITLE-ONLY: Blume & Stambaugh (1983), *Biases in Computed Returns*, JFE
- TITLE-ONLY: van Binsbergen, Nozawa & Schwert (forthcoming RFS), *Duration-Based Valuation of Corporate Bonds*
- TITLE-ONLY: Chen, Lesmond & Wei (2007), *Corporate Yield Spreads and Bond Liquidity*, JF

**Practitioner writing**
- VERIFIED-URL: Impax, "Quant meets credit" (19 Sep 2025), https://impaxam.com/insights-and-news/blog/quant-meets-credit-enhancing-fundamental-analysis-through-systematic-screening/ (carries the Barclays QPS $90–140bn and "Better Together" numbers)
- VERIFIED-URL: State Street SAFI Q3 2025 commentary (25 Nov 2025), https://www.ssga.com/us/en/institutional/insights/fixed-income-q3-2025-safi-commentary
- VERIFIED-URL: Robeco QI Global Multi-Factor Credits fund page, https://www.robeco.com/en-int/products/funds/isin-lu1235145304/robeco-qi-global-multi-factor-credits-fh-eur
- VERIFIED-URL: Robeco, "A prudent route to effective factor timing" (12 Jul 2023; equities, factor-momentum-after-costs), https://www.robeco.com/en-us/insights/2023/07/a-prudent-route-to-effective-factor-timing
- VERIFIED-URL: Robeco, *Guide to Credits* (c. 2017 PDF), https://www.robeco.com/files/docm/docu-guide-to-credits.pdf
- VERIFIED-URL: QuantPedia summary of DFPS, https://quantpedia.com/corporate-bond-factors-replication-failures-and-a-new-framework/
- TITLE-ONLY: Barclays QPS, Mateer et al. (2024), *QPS & Credit Research: Better Together*
- TITLE-ONLY: AQR Alternative Thinking (Oct 2017), *The Illusion of Active Fixed Income Alpha*
- TITLE-ONLY: PGGM / IPE (2020), *Will corona be a watershed moment for credit factor investing?*
- TITLE-ONLY: Robeco (Jun 2022), *Ten years of successful factor investing in credit markets*
- TITLE-ONLY: Blackstone, *Corporate Bond Strategies* page (AUM claim >$40bn; CHECK)
- Shelf (cite by page): Man 2022; Man 2023; Blackstone BCBS; BlackRock Systematic HY; Nuveen MAC.

**Data & code**
- VERIFIED-URL: Open Bond Asset Pricing, https://openbondassetpricing.com/ (TRACE pipeline, 108 and 341 factor sets, ML panel 2002–2022, corrected BBW factors, duration-matched Treasury returns; WRDS Contributed Data)
- VERIFIED-URL: Lasse H. Pedersen data page (links DFPS factor data), https://www.lhpedersen.com/data
- Canonical roots: https://www.sec.gov/edgar (fundamentals), FINRA TRACE specifications (title only), WRDS Bond Returns (title only).

**Podcasts** — none verified this session (the Flirting with Models front page lists only four recent episodes, none on credit). Writer should search for and verify before linking: Flirting with Models episodes with credit-factor guests (e.g., Robeco or AQR credit researchers); Bloomberg Odd Lots on quant credit; Excess Returns / Resolve Riffs on fixed-income factors. Until verified: TITLE-ONLY, no episode numbers.

---

## 10. Exploratory-space notes (future editions)

1. **New chapter candidate, "Ch 9-B: The Bond Data Problem."** Building a clean corporate-bond return panel from TRACE: dissemination caps, cancels/corrections, interdealer vs customer prints, bounce-back filters, duration-matched Treasury returns (van Binsbergen–Nozawa–Schwert), price-level vs. transaction-weighted mids, and a CI harness that replicates OBAP's public series. This is now the single biggest determinant of whether a credit factor exists; it deserves its own chapter and a data-engineering spec for ROBO.
2. **New section in Ch 9 (or Ch 11): quality as default avoidance.** BlackRock p.6's 77%-within-24-months PD screen and the quality-vs-value Sharpe comparison; reconcile with Man/Henke's "quality barely matters in IG": quality is a HY factor and an IG non-factor because IG default risk is too small to sort on.
3. **New section: structural/"index" factors.** Fallen angels, inclusion-delay indices, issuance concessions, rating-stop-loss costs (Dynkin Part II; Ben Dor ch. 12–13): forced-seller premia as factors, with the forced-seller flow graph from Ch 1.
4. **New section: equity-event signals in credit.** PEAD in bonds (Dynkin ch. 20) and ESI (ch. 21) as a family of "equity-leads-credit" factors; Bayesian updating link to Ch 3; what changes when the issuer has no listed equity (private credit, Ch 17).
5. **Factor timing in credit** (Robeco 2023 equity evidence: valuation spreads and seasonality fail after costs, factor momentum half-survives): does the same hold in credit where costs are 5–20× higher? Dynkin p.545's dispersion result suggests a value-spread timing rule worth testing.
6. **Credit factors in CDS and index tranches.** Man p.10–11 argues cash bonds for breadth; a future section on CDX/iTraxx single-name factor portfolios (no price-noise problem, but ~100 liquid names) and on using CDX to hedge the DTS of a long-only factor book.
7. **Crowding measurement for credit factors.** A dedicated section defining and backtesting overlap, factor valuation spreads, and leg-level short-interest crowding; the 2007 quant-quake analogue in credit has not happened yet and the book should pre-write the autopsy template.
8. **Systematic active credit ETFs and model portfolios (TREND).** SSGA's conversions (Dec 2023) and the broader move of factor credit into ETF wrappers; needs fresh AUM and launch-date research (web budget was exhausted this session).
9. **ML factor zoos for bonds.** OBAP's 341-predictor panel (2002–2022) and the DJM Bayesian-model-averaged SDF (OOS Sharpe 1.5–1.8) as the Ch 7 frontier: purged, issuer-grouped CV applied to the bond zoo, and the deflated Sharpe for 108 signals.
10. **The RSSG feature set as a factor.** Convert Ch 13's Priming Risk Score and Ch 25's covenant-capacity variables into a cross-sectional "document-risk" factor; test whether it is spanned by value/quality or is new. This is the book's own contribution and should be queued as a research target with a synthetic-panel first draft.

<!-- STATUS: COMPLETE -->
