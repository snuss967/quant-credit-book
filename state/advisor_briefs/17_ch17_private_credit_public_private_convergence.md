# Advisor Brief: Chapter 17 — Private Credit & the Public–Private Convergence (TREND)

**Target file:** `book_src/17_ch17_private_credit_public_private_convergence.md`
**Prepared:** 2026-10-17 (Fable advisor, Edition 1)
**TOC scope:** The private credit boom, BDC marks vs. public comparables, private-to-public refinancing, systematic approaches to private credit, and what a public-markets quant desk can arbitrage.
**Builds on:** `state/research/trend_private_credit_convergence.md` (COMPLETE; cite it, do not re-derive it), the Nuveen and Man shelf papers, and the web research logged in §6 below.

---

## 1. Thesis and "aha"

**Thesis.** By 2025 private credit and public leveraged finance had become *one borrower pool with two pricing regimes*. The Fed's August 2026 substitution note finds 41% of large middle-market borrowers have used both markets, LL→PC switching peaked near 50% of LL borrowers in early 2023, and takeouts ran "considerably balanced" in both directions through 9M2025 (dossier §2). The same sponsor, the same software company, the same 5.0x of leverage can sit in a CLO as a daily-priced BSL loan or in a BDC as a quarterly-marked unitranche. What differs is not the credit; it is the **measurement**. A public loan is *priced*: daily, noisy, with roughly mean-zero error. A private loan is *marked*: quarterly, model-based, smoothed, and marked by the party that owns it and earns fees on the number. The entire chapter is the mathematics of that filter. Write the reported mark return as a moving average of the true return, $r^{o}_t=\sum_k\theta_k r_{t-k}$ with $\sum_k\theta_k=1$ (Getmansky–Lo–Makarov), and every quantity the desk cares about is a function of $\theta$: reported volatility is deflated by $\sqrt{\sum\theta_k^2}$, correlation with public credit is attenuated by $\theta_0$, the Sharpe ratio is inflated, and the reported NAV series acquires mechanical positive autocorrelation, i.e. "momentum" that is an artefact of measurement rather than of information. Nuveen's own MAC framework proxies middle-market direct lending with the S&P UBS Leveraged Loan B index and gives it a 35% cap; its sector table lists direct-lending volatility as "N/A" (Nuveen pp. 2, 6, 9). That cell is the chapter's epigraph.

**The 2025–26 cycle inverted the filter.** For the first time there are enough *public* observations of *private* marks to estimate $\theta$ and the gap it hides: listed BDC equity at a median 0.74× forward NAV in March 2026 (Reuters/LSEG, CHECK), OBDC's own buybacks at 86% of book, a proposed NAV-for-NAV merger of a listed and a non-listed BDC holding 98%-overlapping portfolios that was pulled in fourteen days, a \$1.4B loan sale "at fair value, which is equivalent to 99.7% of par", non-accruals at 2.8% of cost but 0.8% of fair value in the same portfolio, redemption requests of 11–40% against 5% quarterly caps, a CDS index (CDX Financials) with BDCs in it, Apollo publishing daily prices, and the Fed adding private credit to the Z.1. Each of these is a public price touching a private mark. The desk's job is to build the instrument that measures the touch.

**The aha for the ex-RSSG reader.** You already know this structure; you have just never seen it listed. A BDC is "a CLO in which banks hold the top tranche" (Boston Fed, May 2025): a bank revolver on top, unsecured notes in the middle, listed equity at the bottom, and a manager who both selects and *marks* the collateral. A perpetual BDC facing 16.8% redemption requests with a 5% cap is a liquidity-constrained borrower, and the right tool is the one on Theo's USB stick: a 13-week cash flow where the "maturity wall" is the redemption queue and the "revolver availability" is the undrawn bank line plus the BSL sleeve. "Selective default" (PIK amendments, A&E, covenant holidays, 58% "bad PIK" among PIK payers) is the bilateral market's LMT: the same redefinition of default you watched in Serta and Incora, done quietly, with one lender and no docket. The RSSG instinct to ask "but what does the amendment say?" is, here, the whole signal.

**What a public-markets quant desk can arbitrage.** Not the loans; you cannot buy them. You can trade every public instrument whose price is a function of private marks: BDC equity (cross-sectional RV on scale, software share, bad-PIK share), BDC unsecured bonds against BDC equity against the senior bank line, the CDX Financials basket against a BDC-only basket, PRIV's premium/discount against its firm-bid backstop, the BSL loans that semi-liquid funds sell when gates bind, the BSL *supply* that a PC→BSL takeout wave creates for Ch 21's CLO models, and the insurer rotation that NAIC rating challenges will force. The trend lens runs both ways: a structural trend (loans growing ~20%/yr into a \$1.49T Z.1 line) and a momentum fact (public leads private; smoothed NAVs trend by construction; the listed wrapper moves first).

**One sentence for the monitor:** *Private credit is public credit with the price removed. Our job is to put it back, and to get paid by whoever still believes it was never there.*

## 2. Section outline

Target 8,000–9,500 words. Anatomy tags: **[DF]** desk framing, **[DER]** derivation, **[SPEC]** AI-coder spec, **[SRC]** source extraction, **[CASE]** case study, **[RG]** resource graph. Trend Watch boxes: **TW1–TW4** (minimum two required; four proposed).

**Cold open (≤400 words).** 4:40 p.m., a Tuesday in late June 2026. An RFQ hits: a dealer wants a bid on \$25mm of a listed BDC's unsecured 2029 notes, two hours after its non-traded sibling filed that redemption requests reached 16.8% of shares against a 5% cap. Kaz: "The NAV hasn't moved all quarter. Volatility is literally N/A." Ines: "Then who at this table is selling, and why today?" Mags: "In my day we called a bond with no price 'a bond.'" Theo, quietly: "What does the fund's revolver say about borrowing-base eligibility for PIK loans?" The question the chapter answers: *what is the true value and risk of a portfolio whose only published price is set by its owner, and which public instruments let us trade our answer?* Then: "By the end of this chapter you will be able to..." (estimate a smoothing kernel from four marks a year, convert a BDC price into an implied asset markdown, forecast PC↔BSL flow from a public regime variable, price a redemption queue as a run, and build the public-instrument book that expresses all of it).

**17.1 One borrower pool, two pricing regimes [DF][SRC][TW1][RG]**
- The definitional trap: "private credit" is \$1.3T–\$3T+ depending on loans vs AUM, US vs global, with/without dry powder. State which. Z.1: \$1,493.5B of loans (2025), ~20%/yr, holders PD funds \$532B / BDCs \$456B / RoW \$376B / interval \$76B / MM CLOs \$54B (Fed, 16 Oct 2026).
- Same borrowers, different terms: 2025 issuance PC vs LL median revenue \$223M vs \$902M, 5.0x vs 3.2x, ICR 2.2x vs 3.7x, S+500 vs S+400, 0% vs 28% rated BB+, 15% vs 9% CCC (Fed, 11 Aug 2026).
- [SRC] Nuveen p.2 "Volatility N/A"; p.9 LL B proxy; Man 2022 p.41 data-availability quote.
- **TW1: From niche to Z.1 line item, 2018–2026.** Dated series: ~\$350B vehicle AUM (2012) → >\$2.6T; loans \$1,042.6B (2023) → \$1,253.6B (2024) → \$1,493.5B (2025); semi-liquid net assets \$15B (2018) → \$388B (2025); global AUM >\$2.2T (Mar 2025) with \$4.5T forecast by 2030; the Fed's new series codes (FL893167205 etc.) for App B.

**17.2 The mark as a filter: smoothing, stale prices and the illusion of low volatility [DF][DER][SRC][SPEC][RG]**
- [DER] The GLM smoothing model; variance deflation, autocorrelation profile, Sharpe inflation; Dimson/Scholes–Williams aggregated beta; the Geltner AR(1) inversion and why over-unsmoothing amplifies noise; Couts–Gonçalves–Rossi's common-factor smoothing.
- [SRC] Bohn p.334 ("fitting someone else's model"), p.335 (stair-steps); Dynkin p.623 (autocorrelation as stale-price liquidity proxy), p.124; Ben_Dor p.208 (five unchanged quotes rule).
- Desk Myth vs. Desk Reality: *Myth:* private credit has low volatility and low correlation. *Reality:* it has low *measured* volatility because $\sum\theta_k^2<1$; Asness's "illiquidity discount" (investors may pay for smoothness).
- [SPEC] `estimate_smoothing_kernel` on quarterly CDLI/BDC NAV returns vs. a public LL index, with the sanity check in §4.

**17.3 Marking the unmarked: BDC P/NAV, implied markdowns and the non-accrual gap [DF][DER][CASE][SPEC][RG]**
- The BDC as a listed CLO: revolver (banks; 97% first-lien, Y-14), unsecured notes, equity. Fee drag as a structural discount. 2:1 leverage since 2018.
- [DER] $m=\frac{(1-\phi)-P/\text{NAV}}{1+L}$; implied carrying value of non-accruals $\hat{R}_{NA}=\frac{w^{FV}_{NA}}{w^{C}_{NA}}\cdot\frac{FV}{C}$; cross-holder mark dispersion.
- [CASE] OBDC Nov 2025–Aug 2026 (the natural experiment; §7.1). Octus 40-point same-loan gaps; recoveries ≈50c vs the 70c managers cited (16 Apr 2026).
- Ways This Blows Up: using gross vs net leverage; forward vs trailing NAV; P/NAV>1 names (ARCC, MAIN) where the formula says "negative markdown" and the real answer is franchise/fee value; buybacks at 86% of book that mechanically lift NAV.

**17.4 Two-way takeouts: PC↔BSL migration as a regime-conditional flow [DF][DER][CASE][TW][RG]**
- The Fed's excess-loan-premium regime (tight LL window May 2022–Sep 2024), switching share ~50% early 2023, "steals" rising since 2019, takeouts balanced 2024–9M2025.
- [DER] Competing-risks refinancing hazards (to BSL, to PC, A&E, default) with a regime covariate; expected BSL supply from PC→BSL flow as an input to Ch 21.
- [CASE] Finastra Sep 2023: \$4.82B unitranche + \$500M revolver refinancing US and European leveraged loans (Kirkland release); the reverse flow in 2024 when BSL spreads compressed.
- Optional TW: "Steals and takeouts, 2019–2025" if LCD/KBRA volumes can be sourced (CHECK).

**17.5 Banks moved up the stack, insurers moved down the funnel [DF][SRC][CASE][TW3][RG]**
- Banks: Citi–Apollo \$25B (26 Sep 2024), JPM \$50B + ~\$15B co-lenders (24 Feb 2025); committed lines to PC vehicles ~\$95B, 60% at five GSIBs; bank funding premium +1.1pp to BDCs in 2022; "a CLO in which banks hold the top tranche".
- Insurers: ~\$1.2T PC at YE2025 (NAIC, CHECK), PLRs \$483B (Fitch, CHECK), 106 of 109 private ratings above NAIC staff scores, RBC relief ~10× through CLO/BDC stacks, NAIC discretion over FE designations (2024 authority, operational 2026), Item 2025-19 disclosure from 31 Dec 2026.
- **TW3: The bank–private credit partnership wave, 2023–2026**, dated and sourced; what a "partnership" is in flow-graph terms (origination-and-distribution, senior tranche, not retreat).

**17.6 Semi-liquid vehicles and the redemption game [DF][DER][CASE][TW2][RG]**
- [DER] The 5% cap as pro-rata rationing; first-mover advantage when NAV is smoothed; the run condition; liquidity runway in quarters (the 13-week model for a fund); the BSL-sleeve spillover into public loan prices.
- [CASE] Q1–Q3 2026: Barings 11.3% (fill ~44%), OCIC ~20% and OTIC ~40%, ADS 11.2% then 16.8% (\$2.4B), BCRED ~10% (\$4.3B), KKR FS Income Trust 6.3%, Cliffwater ~16%; ~\$13B requested, ~\$4.6B trapped (Bloomberg Law); OBDC II's switch from tenders to return-of-capital distributions funded by the \$1.4B sale.
- **TW2: The listed discount and the redemption queue, Nov 2025–Sep 2026.** P/NAV median 0.74 (Mar 2026); average discount 23% vs 7% a year earlier (9fin, CHECK); Q1 2026 the first quarter in which accepted redemptions exceeded inflows (Fed FSR May 2026); IMF 5–7 quarter buffers.

**17.7 The plumbing that turns marks into prices [DF][SRC][TW4][RG]**
- Apollo daily pricing (1 Jul 2026 IG → 1 Oct 2026 all credit; asset-level from 30 Oct 2026); ICE 5,000+ private IDs; \$30B+ Apollo secondary desk; secondaries market \$226B record in 2025 with PC GP-led +~300%; CDX Financials (25 names, BDCs inside, trading from Apr 2026); PRIV's firm-bid wrapper (\$802.8M, 22.1% Apollo-sourced, 15 Oct 2026); PCR.
- [SRC] Man 2022 p.41 as a prediction scored four years later.
- **TW4: From "no price" to five price sources, 2022–2026.**

**17.8 Systematic approaches to private credit [DF][DER][SRC][SPEC][RG]**
- What "systematic" can mean with four marks a year: look-through security master from BDC schedules of investments (Davydiuk et al. prove the corpus is research-grade); sector/AI-exposure loadings (software ≈ one-fifth of DL loans, >50% of NAV in some vehicles); diversification as a factor (ROE 9.5% for >200 borrowers vs 6.1% for <100); hidden-default series (PIK 7.3% of CDLI income; 58% bad PIK); net-of-fee alpha ≈ 0 (Erel–Flanagan–Weisbach).
- [SRC] Bohn p.235 fn 11 (small-sample covariates). Cross-ref Ch 7 (purged CV with quarterly data), Ch 9 (factor construction), Ch 25 (SOI parsing).
- [DER] The public-leads-private lead–lag regression and the Dimson aggregated beta as the chapter's main empirical engine; the "NAV momentum" result and why it is measurement, not information.

**17.9 What a public-markets quant desk can arbitrage [DF][CASE][SPEC][RG]**
- The menu, each with instrument, signal, hedge, and failure mode: BDC equity RV; BDC capital structure (revolver > notes > equity); CDX Financials vs BDC basket; PRIV premium/discount; event-driven (merger/termination, tender-to-RoC conversions, private-to-listed conversions, portfolio sales at "fair value"); gate-driven BSL sleeve selling; PC→BSL supply ahead of CLO demand; NAIC-calendar insurer rotation.
- Poker Table (Ines): the redemption queue as a hand where the first to fold wins.
- Ways This Blows Up: CDX Financials is 25 names with ~12% private credit, so the hedge ratio to a BDC basket is small and unstable; BDC equity borrow; buyback squeezes; the "sale at fair value" that is also a sale of the best loans (adverse selection in partial-interest sales).

**17.10 Desk Debrief** (6–8 bullets), **The Spec You Hand the Robot** (the Mark-Gap Monitor), **Exercises** (4–6; see §8 for the funny ones).

## 3. Derivation skeletons

All expectations are under the physical measure $\mathbb{P}$; nothing here is priced under $\mathbb{Q}$ (there is no liquid hedge for a single private loan, which is the point). Time index $t$ is **quarters** unless stated; convert autocorrelations and volatilities explicitly before comparing with monthly public data.

### 3.1 The mark as a moving-average filter (Getmansky–Lo–Makarov)

**Assumptions.** True (unobservable) excess return $r_t$ is covariance-stationary with mean $\mu$, variance $\sigma^2$, and no serial correlation. The reported (NAV) return is
$$
r^{o}_t=\sum_{k=0}^{K}\theta_k\,r_{t-k},\qquad \theta_k\in[0,1],\qquad \sum_{k=0}^{K}\theta_k=1 .
$$
The unit-sum constraint says marks eventually catch up: nothing is hidden forever, only delayed. (In a fraud, $\sum\theta_k<1$; see First Brands.)

**Consequences (derive each in the chapter).**
$$
\mathbb{E}[r^{o}_t]=\mu,\qquad
\operatorname{Var}(r^{o}_t)=\sigma^2\sum_{k}\theta_k^2\;\le\;\sigma^2,\qquad
\rho^{o}_j=\frac{\sum_{k}\theta_k\theta_{k+j}}{\sum_k\theta_k^2},
$$
$$
\text{SR}^{o}=\frac{\text{SR}}{\sqrt{\sum_k\theta_k^2}}\;\ge\;\text{SR},\qquad
\beta^{o}_{0}=\operatorname{Cov}(r^o_t,F_t)/\operatorname{Var}(F_t)=\theta_0\,\beta
$$
for a public factor $F_t$ (e.g., the LL index excess return) that is itself serially uncorrelated. The contemporaneous beta to public credit is attenuated by exactly $\theta_0$; the rest of the beta is parked at lags. **Worked check for the writer:** $\theta=(0.5,0.3,0.2)$ gives $\sum\theta_k^2=0.38$, so reported vol is $\sqrt{0.38}=0.616$ of true vol, the Sharpe is inflated by $1/0.616=1.62$, $\rho^o_1=(0.15+0.06)/0.38=0.553$, $\rho^o_2=0.10/0.38=0.263$, and the contemporaneous beta is half the true beta.

**Recovering the beta (Dimson 1979 / Scholes–Williams 1977).** Regress $r^o_t$ on current and $K$ lagged factor returns:
$$
r^o_t=\alpha+\sum_{k=0}^{K} b_k F_{t-k}+\epsilon_t,\qquad \hat\beta^{\text{agg}}=\sum_{k=0}^{K}\hat b_k ,
$$
and under the model $b_k=\theta_k\beta$, so $\hat\beta^{\text{agg}}\to\beta$. This is also the **public-leads-private test**: $b_1,b_2>0$ with $t$-stats is the lead–lag. The tradable restatement is the one-quarter-ahead forecast $\mathbb{E}_t[r^o_{t+1}]=\alpha+\sum_{k\ge1}b_k F_{t+1-k}$, which is known at $t$ because it only uses $F_t,F_{t-1},\dots$

**Unsmoothing (Geltner 1991/1993, AR(1) case).** If $r^o_t=(1-\theta)r_t+\theta r^o_{t-1}$, then
$$
\hat r_t=\frac{r^o_t-\theta\,r^o_{t-1}}{1-\theta},\qquad \operatorname{Var}(\hat r_t)=\frac{1+\theta^2}{(1-\theta)^2}\operatorname{Var}(r^o_t)-\frac{2\theta}{(1-\theta)^2}\operatorname{Cov}(r^o_t,r^o_{t-1}).
$$
**Error-prone spots.** (i) Estimating $\theta$ from 20–40 quarterly observations: the MLE of an MA(2) on 30 points has standard errors comparable to the coefficients; report intervals, not points, and say so (Bohn p.235 fn 11 is the shelf's warning). (ii) Any measurement noise $\eta_t$ in $r^o_t$ is amplified by $1/(1-\theta)$ in $\hat r_t$; with $\theta=0.7$ noise variance grows $11\times$. (iii) Couts–Gonçalves–Rossi: funds holding the same loans share a *common* smoothing factor, so fund-by-fund unsmoothing leaves correlated residual lag; estimate $\theta$ on a cross-holder panel. (iv) Quarterly vs monthly: $\rho_1$ at quarterly frequency is not comparable with the Dynkin monthly buckets without aggregation. (v) The unit-sum constraint is an assumption; test it by regressing cumulative marks on cumulative public returns over long windows.

### 3.2 From a listed BDC price to an implied asset markdown

**Assumptions.** BDC balance sheet $A=D+E$ at reported marks; leverage $L=D/E$ (use **net** debt / NAV as the companies report it; state which). The market's valuation of the assets is $A(1-m)$ with $m\ge 0$ the implied markdown; the equity also carries a structural fee drag with present value $\phi\,E$ (base + incentive fees on gross assets capitalized at the equity's required return). Debt is assumed money-good (first-order; relax in §3.3).
$$
P = E(1-\phi) - mA \;\Longrightarrow\; \frac{P}{\text{NAV}} = (1-\phi) - m(1+L)
\;\Longrightarrow\;
m=\frac{(1-\phi)-P/\text{NAV}}{1+L}.
$$
**Numbers for the writer** (OBDC, Q4 2025): $P/\text{NAV}=0.86$ (the company's own buyback print), $L=1.19$, $\phi=0.05$ *(illustrative)* $\Rightarrow m=(0.95-0.86)/2.19=4.1\%$ of assets. At the March 2026 sector median $P/\text{NAV}=0.74$ with $L=1.1$: $m=(0.95-0.74)/2.1=10.0\%$. At a 50% discount: $m\approx 21\%$, i.e., the market is saying the loans are worth 79 on a book that says 98–100.
**Boundary conditions.** If $P/\text{NAV}>1-\phi$ the formula returns $m<0$: floor $m$ at zero and attribute the premium to franchise value (NII in excess of dividend, fee-earning growth); ARCC and MAIN are the live examples. **Error-prone spots.** Forward vs trailing NAV (the 0.74 median was on *forward* NAV); unfunded commitments (not in $A$ but a call on liquidity); preferred equity and JV structures sitting between $D$ and $E$; buybacks at $P<\text{NAV}$ mechanically raise NAV/share, so $P/\text{NAV}$ can fall while NAV rises; and the fee drag is not a constant, it rises when the hurdle is close.

### 3.3 The non-accrual gap and the implied carrying value of bad loans

BDCs report non-accruals as a share of the portfolio at **cost** and at **fair value**. Let $w^C_{NA}$ and $w^{FV}_{NA}$ be those shares, and $FV/C$ the whole-portfolio ratio. Then the implied carrying value of the non-accrual bucket, as a fraction of its cost, is
$$
\hat R_{NA}=\frac{w^{FV}_{NA}\cdot FV}{w^{C}_{NA}\cdot C}=\frac{w^{FV}_{NA}}{w^{C}_{NA}}\cdot\frac{FV}{C}.
$$
OBDC 30 Jun 2026: $w^C_{NA}=2.8\%$, $w^{FV}_{NA}=0.8\%$, $FV/C\approx0.98$ *(approx.)* $\Rightarrow \hat R_{NA}\approx 0.28$. The manager is carrying its defaulted loans at about 28 cents, while the industry has been quoting 70-cent recoveries and Octus finds ~50 (16 Apr 2026). The **gap series** $g_t=w^C_{NA,t}-w^{FV}_{NA,t}$ is a hidden-loss gauge: it rose from 1.2pp to 2.0pp at OBDC between Dec 2025 and Jun 2026 even as $w^{FV}_{NA}$ fell. **Error-prone spot:** $\hat R_{NA}$ is a mark, not a recovery; compare with Ch 14's realized-recovery mixture, and remember non-accrual status is a management decision (loans can be amended into PIK to avoid it: 58% "bad PIK").

### 3.4 PC↔BSL migration as a regime-conditional competing-risks problem

For each loan $i$ outstanding at $t$, four competing exits: refinance into BSL ($B$), refinance into PC ($P$), amend-and-extend ($X$), default ($\tau$). Cause-specific hazards with a public regime covariate $z_t$ (the Fed's excess loan premium, or its sign relative to the median) and the DL–BSL spread differential $\Delta s_t$:
$$
\lambda^{(j)}_i(t)=\lambda^{(j)}_0(t)\exp\!\big(\gamma_j z_t+\delta_j\Delta s_t+\boldsymbol{\beta}_j^\top \mathbf{x}_i\big),\quad j\in\{B,P,X,\tau\},
$$
with $\mathbf{x}_i$ = size, sector (software flag), rating/credit estimate, sponsor, years to maturity. The expected BSL *supply* from private takeouts over the next quarter is
$$
Q^{P\to B}_{t+1}=\sum_{i\in\text{PC}}\text{Face}_i\cdot\Big(1-e^{-\lambda^{(B)}_i(t)\Delta t}\Big),
$$
an input to Ch 21's CLO-demand and repricing-wave models. **Assumptions:** proportional hazards within regime; migration decisions observed with a lag (announcements, not closings). **Error-prone spots:** the regime variable is itself estimated and revised; dual-track processes mean the "cause" is only known ex post; the Fed's regime (tight LL = May 2022–Sep 2024) is one sample, so $\gamma_j$ is a two-regime estimate with wide intervals.

### 3.5 The redemption queue as a run with a pro-rata cap

Semi-liquid fund with NAV per share $N$ (smoothed), true value $N(1-m)$, quarterly cap $c=5\%$ of shares, request fraction $q_t$. Fill fraction $f_t=\min(1,c/q_t)$. A redeemer receives $N$ per share filled; stayers absorb the shortfall. With $S$ shares outstanding and $f_tq_tS$ redeemed at $N$, the post-redemption true value per remaining share is
$$
N^{\text{true}}_{\text{stay}}=\frac{N(1-m)S-N f_tq_tS}{S(1-f_tq_t)}=N\cdot\frac{(1-m)-f_tq_t}{1-f_tq_t}<N(1-m)\quad\text{whenever } m>0 .
$$
Requesting is a weakly dominant strategy as soon as $m>0$ is common knowledge; the cap does not remove the first-mover advantage, it rations it, and it pushes $q_{t+1}$ up because unfilled requests roll. **Liquidity runway** (quarters) for a vehicle:
$$
T=\frac{\text{Cash}+\text{Undrawn lines}+\text{Liquid sleeve}\times(1-h)}{c\cdot \text{NAV}+\text{Unfunded draws}+\text{Debt maturities}},
$$
with haircut $h$ on the BSL sleeve under stress. The IMF's 5–7 quarters under moderate shock is the calibration target; non-traded BDCs hold 0.2% short-term liquid assets (Fed, Oct 2026), so $T$ is a function of bank lines and the sleeve, not cash. **Error-prone spots:** the sale of the sleeve *is* the spillover into public loan prices (a reflexive $h$); gates convert to return-of-capital distributions (OBDC II) which change $c$; the model must treat $m$ as unknown to the fund's own investors, which is the whole reason $q_t$ jumps when a listed sibling prints 0.86.

### 3.6 Where the measure matters

Everything above is $\mathbb{P}$. The only place $\mathbb{Q}$ appears in this chapter is CDX Financials and single-name CDS on BDC unsecured notes: there the spread embeds a risk premium over the BDC's default intensity $\lambda_t$ (Ch 6, Ch 24 conventions), and converting it into an implied markdown on *collateral* requires a structural map through the BDC's own leverage (a Merton-on-a-CLO exercise, flagged in §10). Do not mix a $\mathbb{Q}$ spread with a $\mathbb{P}$ markdown without saying so.

## 4. Code spec and sanity check

**Engine name:** `mark_gap` — the Mark-Gap Monitor. One module, five pure functions, one simulation-based sanity check. Numpy/pandas only. Written to run as-is; the writer should paste it into the chapter's `### Specification for AI Implementation` block and, in the cleanup pass, execute it once.

**The Spec You Hand the Robot (vague version, for the gag).** "ROBO, estimate the volatility of private credit." ROBO returns the standard deviation of quarterly CDLI returns, 2.1% annualized *(illustrative)*, and marks the asset class safer than Treasuries. The precise version follows.

**Data schemas (pandas DataFrames; one row per key; all money in USD, all shares in decimals, dates as quarter-end `datetime64`).**

| table | key | columns (dtype) | source |
|---|---|---|---|
| `bdc_quarterly` | (`bdc_id`, `qdate`) | `nav_ps` float; `price` float or NaN (non-traded); `net_debt_to_equity` float; `w_na_cost`, `w_na_fv` float (decimals, not %); `fv_total`, `cost_total` float; `pik_income`, `total_income` float; `first_lien_pct` float; `n_companies` int; `restated` bool | 10-Q/10-K, press releases |
| `soi` | (`bdc_id`, `qdate`, `facility_id`) | `borrower` str; `ice_id` str or None; `lien` {1,2,3,"unsecured","equity"}; `ref_rate` str; `spread_bp` float; `pik_flag` bool; `par`, `cost`, `fv` float; `maturity` date; `industry` str | schedules of investments (Ch 25 parser) |
| `redemptions` | (`fund_id`, `qdate`) | `request_pct` float; `cap_pct` float (default 0.05); `fill_pct` float; `nav_total` float; `mode` {"tender","roc_distribution","gated"} | 8-K, SC TO-I, N-23c-3 |
| `public_index` | `date` | `ll_excess_ret` float (monthly or quarterly, state which); `hy_excess_ret`; `cdx_fin_spread_bp` | vendor; App B |

**Edge cases the robot must handle:** non-calendar fiscal quarters (align to the nearest calendar quarter end, flag it); restated NAVs (keep both vintages; never overwrite); `price` NaN for non-traded vehicles (P/NAV undefined, do not fill with 1.0); `w_na_cost == 0` (return NaN, not inf); the same facility held by several BDCs (join on `ice_id` when present, else fuzzy borrower name + maturity + spread); percentages reported as "2.8%" strings; and the unit-sum constraint on $\theta$ (clip to $[0,1]$, renormalize, and report whether the clip bound).

**Numerical guards:** require at least $10(K+1)$ observations for a Dimson regression with $K$ lags; use `lstsq` (SVD) rather than normal equations because lagged factor returns are nearly collinear in smooth regimes; standardize $F$ before regression and rescale coefficients back; never unsmooth with $\theta\ge0.9$ (noise amplification $>100\times$) without a warning.

```python
import numpy as np

def simulate_smoothed(n, theta, beta=1.0, sigma_f=0.04, sigma_e=0.02, seed=17):
    """True return r = beta*F + e; reported r_obs = sum_k theta_k r_{t-k}. Quarterly units."""
    rng = np.random.default_rng(seed)
    theta = np.asarray(theta, float); theta = theta / theta.sum()
    K = len(theta) - 1
    F = rng.normal(0.0, sigma_f, n)
    r_true = beta * F + rng.normal(0.0, sigma_e, n)
    r_obs = np.full(n, np.nan)
    for t in range(K, n):
        r_obs[t] = float(np.dot(theta, r_true[t - K:t + 1][::-1]))
    return F, r_true, r_obs

def autocorr(x, j):
    x = np.asarray(x, float); x = x[~np.isnan(x)]; x = x - x.mean()
    return float(np.dot(x[j:], x[:-j]) / np.dot(x, x))

def dimson_beta(r_obs, F, K):
    """Regress reported returns on current and K lagged factor returns; return (b_k, sum b_k)."""
    r_obs = np.asarray(r_obs, float); F = np.asarray(F, float)
    T = len(r_obs)
    if T - K < 10 * (K + 1):
        raise ValueError("too few observations for K lags")
    rows, y = [], []
    for t in range(K, T):
        if np.isnan(r_obs[t]):
            continue
        rows.append([1.0] + [F[t - k] for k in range(K + 1)])
        y.append(r_obs[t])
    X = np.asarray(rows); y = np.asarray(y)
    coef, *_ = np.linalg.lstsq(X, y, rcond=None)
    return coef[1:], float(coef[1:].sum())

def unsmooth_ar1(r_obs, theta):
    if not 0.0 <= theta < 0.9:
        raise ValueError("theta outside [0, 0.9): noise amplification too large")
    r = np.asarray(r_obs, float); out = np.full_like(r, np.nan)
    out[1:] = (r[1:] - theta * r[:-1]) / (1.0 - theta)
    return out

def implied_markdown(p_nav, lev, fee_drag=0.0):
    """Market-implied markdown on BDC assets as a fraction of reported asset value; floored at 0."""
    if np.isnan(p_nav):
        return np.nan
    return max(((1.0 - fee_drag) - p_nav) / (1.0 + lev), 0.0)

def implied_nonaccrual_mark(w_fv, w_cost, fv_over_cost=1.0):
    """Carrying value of the non-accrual bucket as a fraction of its cost."""
    if w_cost <= 0:
        return np.nan
    return (w_fv / w_cost) * fv_over_cost

def redemption_fill(q, cap=0.05):
    return 1.0 if q <= 0 else min(1.0, cap / q)

def stayer_value(N, m, q, cap=0.05):
    """True value per remaining share after pro-rata redemptions at smoothed NAV N."""
    f = redemption_fill(q, cap)
    return N * ((1.0 - m) - f * q) / (1.0 - f * q)

def runway_quarters(cash, undrawn, sleeve, haircut, nav, cap, unfunded, maturities):
    outflow = cap * nav + unfunded + maturities
    return np.inf if outflow <= 0 else (cash + undrawn + sleeve * (1.0 - haircut)) / outflow

# ---- sanity checks (assert; seeded) ----
theta = (0.5, 0.3, 0.2)
F, r_true, r_obs = simulate_smoothed(20000, theta, beta=1.0)
var_ratio = np.nanvar(r_obs) / np.var(r_true)
assert abs(var_ratio - 0.38) < 0.02, var_ratio          # sum theta_k^2 = 0.38
assert abs(autocorr(r_obs, 1) - 0.553) < 0.03             # (0.15+0.06)/0.38
assert abs(autocorr(r_obs, 2) - 0.263) < 0.03             # 0.10/0.38
b0, agg0 = dimson_beta(r_obs, F, 0)
bK, aggK = dimson_beta(r_obs, F, 2)
assert abs(agg0 - 0.5) < 0.05, agg0                        # contemporaneous beta = theta_0 * beta
assert abs(aggK - 1.0) < 0.05, aggK                        # aggregated beta recovers 1.0
assert abs(implied_markdown(0.86, 1.19, 0.05) - 0.0411) < 1e-3
assert implied_markdown(1.02, 1.0, 0.05) == 0.0
assert abs(implied_nonaccrual_mark(0.008, 0.028, 0.98) - 0.28) < 0.005
sv = stayer_value(1.0, 0.05, 0.168, 0.05)
assert sv < 0.95 and abs(sv - 0.9474) < 1e-3
assert abs(runway_quarters(0.002, 0.10, 0.10, 0.10, 1.0, 0.05, 0.02, 0.0) - 2.743) < 0.01
print("mark_gap sanity checks passed")
```

**Why each check is there.** The variance ratio and the two autocorrelations are the closed-form GLM identities; if the simulation disagrees, the kernel convention (which index is "today") is reversed. The two Dimson runs show attenuation ($\theta_0\beta$) and recovery ($\sum b_k\to\beta$) in one picture. The `implied_markdown` numbers are the OBDC Q4 2025 print and a premium name (floor). The non-accrual check reproduces the ≈28c carrying value derived in §3.3. The `stayer_value` check shows the first-mover transfer at ADS-sized requests (16.8%). The runway check is a non-traded BDC with 0.2% cash, a 10%-of-NAV line and a 10% BSL sleeve: under three quarters of a 5% run, which is below the IMF's 5–7.

**Second-stage spec (text only, for the chapter):** `estimate_theta_panel(nav_returns_by_fund, F, K)` fits a shared MA($K$) kernel across funds by pooled OLS of $r^o_{i,t}$ on $F_{t-k}$ with fund fixed effects (Couts–Gonçalves–Rossi logic), returns $\hat\theta_k=\hat b_k/\sum\hat b_k$ with a bootstrap over quarters (block length 4), and refuses to report a point estimate when the 90% interval for $\theta_0$ spans more than 0.4.

## 5. Source map (shelf)

Each entry: `book_id p.N`, an exact quote (≤60 words), and the annotation angle for the `> [SOURCE EXTRACTION]` block.

1. **Nuveen_Multi_Asset_Credit_Quant_Framework p.9** — "Middle market direct lending (Private Credit): Proxy Index using S&P UBS Leveraged Loan B Index." *Angle:* the industry's own MAC optimizer uses a public B-rated loan index as the private-credit return series; show the bias (5.0x vs 3.2x leverage, 0% vs 28% BB, more software) and the fix (desmooth, stress, liquidity tier). Cross-ref Ch 12.
2. **Nuveen p.6** — "Solving for the highest risk-adjusted return (as measured by the forward Sharpe ratio), portfolio six has the optimal allocation, with a return of 6.20%." plus Figure 5's constraint row "Middle market direct lending 0 35%". *Angle:* a 35% cap on a sector whose volatility input is a proxy; the optimizer rewards whatever is smoothest.
3. **Nuveen p.2** (Figure 1, table) — row "Middle market direct lending": "Yield target 9–11% … Liquidity: Illiquid … Volatility: N/A". *Angle:* the epigraph; "N/A" is not zero, it is unmeasured, and §3.1 says what it would be.
4. **Man_Quantitative_Credit_Alpha_Early_Mover_2022 p.41** — "While loans and other private credit instruments are obviously problematic from a data availability perspective at present, we believe that the momentum of quant activity in other areas of the fixed income markets will drive innovation and transparency in these historically opaque areas." *Angle:* score the prediction in 2026: ICE IDs, Apollo daily prices, CDX Financials, Z.1.
5. **Bohn_Stein_Active_Credit_Portfolio_Management p.334** — "Essentially, unwary modelers may inadvertently end up fitting someone else's model." and "Many supposedly profitable trading strategies end up being the result of an inadvertent fitting of a matrix model as reflected in matrix prices reported by a data vendor." *Angle:* a BDC NAV is the manager's model; a backtest on CDLI is a backtest on the manager's valuation committee.
6. **Bohn_Stein p.335** — "a time series plot that shows stair-stepped trends in price … will likely reflect matrix pricing as new levels for the price are bled into the reported price, creating auto-correlation in the data." *Angle:* the stair-step is the smoothing kernel seen by eye; the chapter's first figure should be a BDC NAV path next to a LL index.
7. **Bohn_Stein p.235 fn 11** — "it would be unusual in the private credit risk setting to have more than 10 year-end financial statements and quarterly financial statements." *Angle:* small-sample covariates; why $\theta$ needs panels and intervals (Ch 7 cross-ref).
8. **Dynkin_Systematic_Investing_in_Credit p.623** — "if corporate bond prices are only updated infrequently and are subject to 'stale' pricing, their returns are likely to be positively correlated as new information slowly gets priced in." *Angle:* autocorrelation as a liquidity measure, taken to its limit: a private loan is the TES-10 bucket with the volume column deleted.
9. **Dynkin p.124** — "There might be high autocorrelation in bond monthly returns, which increases volatilities of the bond portfolios. We adjust for possible serial correlation in the volatilities". *Angle:* the shelf already corrects public bond Sharpe ratios for autocorrelation; apply the same correction to CDLI's 9.3%/low-vol and watch the Sharpe halve *(illustrative until computed)*.
10. **Ben_Dor_Quantitative_Credit_Portfolio_Management p.208** — "all bonds comprising the Corporate and High Yield indexes with a sequence of five or more unchanged quotes in any month are excluded from the eligible population of bonds for that month." *Angle:* a stale-mark filter for the SOI panel: a facility marked at the same FV/par for five quarters while its public comparables moved is a candidate for mark convergence.
11. **Ben_Dor p.166** — "Long-term investors, with reduced mark-to-market constraints, can choose to provide liquidity to the market and buy the bond, comfortable with the low default risk." *Angle:* the honest case for private credit (a liquidity-provision premium for patient capital) versus the dishonest one (a premium for not looking); semi-liquid retail money removed the "reduced mark-to-market constraints" condition.
12. **Moyer_Distressed_Debt_Analysis p.313** — "one of the sources of opportunity in distressed debt investing is the fact that the securities are often illiquid. Liquidity, of course, is a matter of degree." *Angle:* Mags's voice; the secondary market for private loans (\$30B+ Apollo desk, 32/34-style quotes) is the 1990s distressed market being rebuilt.

## 6. RESEARCH DOSSIER (dated, sourced; CHECK = unconfirmed)

### 6.0 Working log of facts (appended as found; VERIFIED = fetched/read this session, CHECK = unconfirmed)

**Shelf facts (read directly from `state/pdf_pages`):**
- Nuveen_Multi_Asset_Credit_Quant_Framework p.9 endnote 2: "Middle market direct lending (Private Credit): Proxy Index using S&P UBS Leveraged Loan B Index." VERIFIED. The private-credit sleeve of the MAC optimizer is literally a public loan sub-index.
- Nuveen p.6 Figure 5: sector constraint "Middle market direct lending 0 35%"; Figure 6 portfolio 6 = forward return 6.20%, forward vol 6.29%, yield 8.24, duration 1.44, fwd Sharpe 0.40. VERIFIED.
- Nuveen p.2 Figure 1: Middle market direct lending yield target 9–11%, Liquidity "Illiquid", Secured "Yes", Rate sensitivity "Low", **Volatility "N/A"** (MM junior capital: 11–14%, Illiquid, Volatility "N/A"). VERIFIED. (The table literally has no volatility entry for the only sectors with no prices. That is the chapter in one cell.)
- Nuveen p.5: CMAs "Source: Nuveen, as at 19 Nov 2025", five-year horizon; Figure 4 places "Middle market direct lending" at roughly 9–10% forward return with ~5% forward vol (read off chart; approximate). VERIFIED (chart reading approximate).
- Man_Quantitative_Credit_Alpha_Early_Mover_2022 p.41: "While loans and other private credit instruments are obviously problematic from a data availability perspective at present, we believe that the momentum of quant activity in other areas of the fixed income markets will drive innovation and transparency in these historically opaque areas. Already both Refinitiv and IHS Markit are providing daily pricing on 6,500 loan facilities." VERIFIED.
- Bohn_Stein_Active_Credit_Portfolio_Management p.235 fn 11: "it would be unusual in the private credit risk setting to have more than 10 year-end financial statements and quarterly financial statements." VERIFIED (small-sample covariate problem; feeds Ch 7 cross-ref).
- Bohn_Stein p.334–335: matrix prices / evaluated prices for funds that must strike daily NAV; stair-step price paths "as new levels for the price are bled into the reported price, creating auto-correlation" (exact wording to be pulled below). TO QUOTE.
- Dynkin_Systematic_Investing_in_Credit p.771, p.623–624: autocorrelation of daily excess returns used as an illiquidity proxy (TES buckets 1–3 liquid, 4–7, 8–10 illiquid); p.124: "Adjusting for Autocorrelation in Computing Portfolio Returns Did Not Account for Higher Sharpe Ratio in Bonds"; p.660: autocorrelations of excess returns much higher for small-size portfolios. TO QUOTE.
- Ben_Dor_Quantitative_Credit_Portfolio_Management p.204, 208: stale-price identification and exclusion in index return studies (sequence of unchanged prices); p.166: investors "with reduced mark-to-market constraints, can choose to provide liquidity to the market". TO QUOTE.

**Web facts, round 1:**
- Getmansky, Lo, Makarov, "An Econometric Model of Serial Correlation and Illiquidity in Hedge Fund Returns", NBER WP 9571, March 2003 (DOI 10.3386/w9571); 908 TASS funds; proposes smoothing profiles and smoothing-adjusted Sharpe. VERIFIED-URL https://www.nber.org/papers/w9571 (published JFE 2004, 74(3): 529–609; journal cite from memory, CHECK volume/pages).
- Citi–Apollo \$25B private credit / direct lending program announced 26 Sep 2024 (Mubadala as Apollo strategic partner; Athene may participate; North America first; "approximately \$25 billion of debt opportunities over the next several years"). Press release at https://www.citigroup.com/global/news/press-release/2024/citi-and-apollo-announce-25-billion-private-credit-direct-lending-program (URL from search listing; fetch below to upgrade to VERIFIED-URL).
- Ellias & de Fontenay, "The Credit Markets Go Dark", 134 Yale L.J. 779 (2025); PDF https://www.yalelawjournal.org/pdf/134.3.ElliasdeFontenay_b1he64cu.pdf (search listing; fetch to confirm); SSRN abstract id 4879742 reported by search (CHECK before printing the id). Thesis: corporate debt following equity into private hands; public information about large firms is lost.
- Search-only items (all CHECK): a headline that "big banks and S&P Global tie up for first credit-default swaps index linked to private credit" (2026); one Blue Owl non-traded fund received withdrawal requests of 40.7% of shares in the quarter to 31 Mar 2026 against a 5% cap; Pimco bought the full \$400m of a Blue Owl BDC bond at a 6.5% yield in Apr 2026 with only one later TRACE print; public BDC unsecured spreads clustered ~150–200bp (ARCC, BXSL, OBDC, GBDC) with dispersion widening on AI/software exposure; Moody's negative outlook on OCIC while Fitch affirmed BBB-/stable.

**Shelf quotes pulled (exact text, for §5):**
- Bohn_Stein p.334: "Essentially, unwary modelers may inadvertently end up fitting someone else's model. ... Many supposedly profitable trading strategies end up being the result of an inadvertent fitting of a matrix model as reflected in matrix prices reported by a data vendor." VERIFIED.
- Bohn_Stein p.335: "a time series plot that shows stair-stepped trends in price (i.e., the same price for several days and then a jump to a new level ...) will likely reflect matrix pricing as new levels for the price are bled into the reported price, creating auto-correlation in the data." VERIFIED.
- Dynkin p.623: "if corporate bond prices are only updated infrequently and are subject to 'stale' pricing, their returns are likely to be positively correlated as new information slowly gets priced in." Sorts bonds by trailing-12m autocorrelation into low 30% / mid 40% / high 30% buckets. VERIFIED.
- Dynkin p.124: "There might be high autocorrelation in bond monthly returns, which increases volatilities of the bond portfolios. We adjust for possible serial correlation in the volatilities". VERIFIED.
- Ben_Dor p.208: "all bonds comprising the Corporate and High Yield indexes with a sequence of five or more unchanged quotes in any month are excluded from the eligible population of bonds for that month." VERIFIED (a stale-price filter rule the desk can reuse on BDC marks: five unchanged quarterly marks = suspicious).
- Ben_Dor p.166: "Long-term investors, with reduced mark-to-market constraints, can choose to provide liquidity to the market and buy the bond, comfortable with the low default risk." VERIFIED.

**Web facts, round 2 (VERIFIED unless marked):**
- Citi–Apollo program: press release dated 26 Sep 2024, VERIFIED-URL https://www.citigroup.com/global/news/press-release/2024/citi-and-apollo-announce-25-billion-private-credit-direct-lending-program . Exact: "maintain the flexibility to significantly expand the size of the program beyond the initial \$25 billion"; "initially in North America, with the potential to expand to additional geographies"; "designed to significantly enhance access for corporate and sponsor clients to the private lending capital pool." Mubadala as strategic partner; Athene participates.
- J.P. Morgan: 24 Feb 2025, at its 30th Global Leveraged Finance Conference, raised its direct-lending balance-sheet commitment to \$50B plus "nearly \$15 billion from multiple co-lenders"; "Since 2021, J.P. Morgan has successfully deployed over \$10 billion across more than 100 private credit transactions". Press release URL (search listing, Business Wire 20250224176509) https://www.jpmorgan.com/about-us/corporate-news/2025/jpmorgan-increases-direct-lending-commitment-to-50-billion — fetched below for upgrade.
- Ellias & de Fontenay: Yale L.J. vol. 134, published 30 Jan 2025 (issue 3; page 779 from search listing). VERIFIED-URL https://www.yalelawjournal.org/article/the-credit-markets-go-dark . Numbers in article: private-credit strategy assets ~\$400M (2000), ~\$300B (2010), ~\$1.6T (2023), projection \$3.5T by 2028; private-credit BDC assets grew >10x 2010–2022 and their loan count rose from 1,395 to 20,182. Hypotheses: more distress episodes, fewer bankruptcies (fewer lenders → less coordination failure), risk of under-marking and "zombie firms", judges may need a more active role.
- Davydiuk, Marchuk, Rosen, "Direct Lenders in the U.S. Middle Market", Journal of Financial Economics 162 (2024) 103946, DOI 10.1016/j.jfineco.2024.103946 (search listing from ideas.repec; TITLE+DOI, treat DOI as VERIFIED via listing). Uses BDC schedule-of-investments data; three exogenous credit-supply shocks (bank regulation, a finance-company collapse) show BDC capital substitutes for bank financing. Important for us: the paper is proof that the BDC SOI corpus is a research-grade dataset.
- Blue Owl press-release index (VERIFIED-URL https://www.blueowlcapitalcorporation.com/investors/news-events/press-releases ): 5 Nov 2025 Q3 results; **19 Nov 2025 "Blue Owl Capital Corporation and Blue Owl Capital Corporation II Announce Termination of Merger"** (detail/87); **18 Feb 2026 "Certain Blue Owl BDCs to Sell \$1.4 Billion of Assets to Institutional Investors"** (detail/89); 18 Feb 2026 Q4 2025 results (detail/90); 6 May 2026 Q1 2026 results (detail/92); 5 Aug 2026 Q2 2026 results (detail/94). This upgrades two dossier CHECK items (merger termination date; \$1.4B sale) to VERIFIED on the company's own site; details fetched below.
- CDX Financials (S&P Dow Jones Indices): announcement PDF dated 25 Feb 2026 at https://www.spglobal.com/spdji/en/documents/index-news-and-announcements/20260225-cdx-financials-index-launch.pdf and a 4 Mar 2026 updated-launch-date notice (search listing; fetched below). Search summary: 25 North American financial entities incl. banks, insurers, REITs and BDCs; equal-weighted; semi-annual roll; private-credit managers ~12% of the index; trading expected from 13 Apr 2026; press described it as the first CDS index linked to private credit; constituent names (Apollo, Blackstone, Ares, Carlyle; Blue Owl reportedly dropped after feedback) are CHECK until the PDF is read.
- BDC unsecured issuance (search listing, individual deals; no aggregate found): Barings BDC \$300M 5.200% due 2028 (Sep 2025; \$1,275.0M unsecured notes outstanding at 30 Sep 2025, per 8-K exhibit on sec.gov); Goldman Sachs BDC \$400M 5.650% due 2030 (Sep 2025) and \$400M 5.100% due 2029 (Jan 2026); Kayne Anderson BDC \$200M private placement (Sep 2025); Crescent Capital BDC up to \$185M (Oct 2025); BCRED \$750M (2026; ~36% of drawn borrowings unsecured at 31 Mar 2026, CHECK); Apollo Debt Solutions BDC \$300M add-on taking a series to \$800M (CHECK). Aggregate "record" claim: CHECK (need Fitch/KBW/LSEG tally).

**Web facts, round 3 (VERIFIED unless marked):**
- **OBDC/OBDC II merger termination, 19 Nov 2025** (VERIFIED-URL https://www.blueowlcapitalcorporation.com/investors/news-events/press-releases/detail/87/blue-owl-capital-corporation-and-blue-owl-capital ): "we are no longer pursuing the merger at this point given current market conditions"; "current market volatility is cause to reevaluate alternatives in the future" (Craig W. Packer, CEO of both). OBDC II to reinstate its tender program in Q1 2026 subject to Board approval; "every quarterly tender since inception has been fully satisfied"; OBDC's \$200M buyback stays. OBDC II since 2017 inception: ~80% cumulative net return, 9.3% annualized, 23bp loss rate since inception, non-accruals <2% at FV. At 30 Sep 2025: OBDC 238 companies / \$17.1B; OBDC II 190 companies / \$1.7B. The release never mentions the stock price or the NAV/NAV exchange ratio, which is the whole story.
- **\$1.4B Blue Owl asset sale, 18 Feb 2026** (VERIFIED-URL https://www.blueowlcapitalcorporation.com/investors/news-events/press-releases/detail/89/certain-blue-owl-bdcs-to-sell-1-4-billion-of-assets-to ): sellers OBDC II (\$600M, ~34% of its commitments incl. unfunded), OTIC (\$400M, ~6%), OBDC (\$400M, ~2%); buyers "four" unnamed North American public pension and insurance investors; 97% senior secured, avg position ~\$5M, 128 companies, 27 industries, internet software & services largest at 13%; partial interests in each borrower. **"The investments will be sold at fair value, which is equivalent to 99.7% of par value as of February 12, 2026."** OBDC II: return-of-capital distribution up to \$2.35/share (~30% of 31 Dec 2025 NAV) by 31 Mar 2026, "about six times" the planned 5% tender; board intends quarterly return-of-capital distributions instead of tender offers going forward. OTIC/OBDC: debt paydown. (Upgrades dossier CHECK on the \$1.4B sale; note it is framed as a sale at fair value, not a discount, and the "permanent restriction" of withdrawals is the shift from tenders to RoC distributions — the FT/Bloomberg framing remains CHECK.)
- **OBDC Q4 2025 results, 18 Feb 2026** (VERIFIED-URL https://www.blueowlcapitalcorporation.com/investors/news-events/press-releases/detail/90/blue-owl-capital-corporation-announces-december-31-2025 ): NAV/share \$14.81 (vs \$14.89 at 30 Sep 2025; \$15.26 at 31 Dec 2024); GAAP NII \$0.38, adj. NII \$0.36; dividend \$0.37 (10.0% annualized yield on NAV); portfolio \$16.5B FV, 234 companies in 30 industries; weighted avg yield on accruing debt 10.0% at FV / 10.1% at cost; **non-accruals 1.1% at FV vs 2.3% at cost** (Q3: 1.3% / 2.7%); net D/E 1.19x (Q3 1.22x); first lien 73.1% at FV; Q4 buybacks ~\$148M at "86% of price-to-book value" (i.e., P/NAV ≈ 0.86), "accretive to net asset value per share"; new \$300M program replaces \$200M. FY2025 PIK income ≈ \$127.4M of \$1,851.3M total investment income ≈ 6.9% (derived by fetch tool from the statement of operations; CHECK arithmetic against 10-K). NAV decline attributed "primarily" to credit-related markdowns on a small number of names. Release says OBDC's \$400M slice sells at 99.8% of par (vs 99.7% for the pooled sale).
- **Public BDC P/NAV, 2026** (search listing; each number CHECK against its primary): Reuters/LSEG: median price-to-forward-NAV ≈ 0.74 at end-Mar 2026, widest since Oct 2020 (deepest in >5.5 years); 9fin: average public BDC discount ≈ 23.2% vs ≈ 6.9% a year earlier (Q1 2026); Octus: "nearly 20% discount", some large names near 50%; a 45-fund tally: average 17% discount; name-level (prices 17 Sep 2026 vs 30 Jun 2026 NAV, marketcrash.net, CHECK): FSK ≈ −36%, OBDC ≈ −20%, BXSL ≈ −1%, ARCC ≈ +2%, MAIN ≈ +68%; Prospect Capital DEF 14A (sec.gov, 11 Mar 2026): 57.2% discount (CHECK exact wording). Dispersion, not the mean, is the signal.
- **NAIC / insurers** (search listing of NAIC resource page and Fitch; CHECK each until fetched): NAIC estimates US insurers held ≈ \$1.2T of private credit at YE2025 (≈13% of cash and invested assets, ≈21% of bonds); privately rated bonds + BDCs + private credit funds = \$544B; Fitch: private letter ratings (PLRs) \$483B at YE2025 vs \$420B at YE2024, 58% of PLR exposure Level 3; NAIC 2024 adopted procedures letting regulators challenge/override FE designations, challenge process live from start of 2026 (dossier says "operational" per Aug 2026 IDAWG); reporting Item 2025-19 effective 31 Dec 2026 requires insurers to quantify every PLR-only private placement; NAIC staff study: in 106 of 109 cases (2023) the private rating was higher than NAIC's own score, some by up to six notches. NAIC resource page: https://content.naic.org/resource-center/private-credit-insurance-regulation (fetch to verify).
- **Finastra refinancing, 2023** (law-firm releases; Kirkland URL https://www.kirkland.com/news/press-release/2023/09/kirkland-advises-finastra-group-on-53-billion-refinancing , fetch to verify): \$4.82B senior secured unitranche term loan + \$500M multicurrency revolver, >20 lenders (Oak Hill, Blue Owl, HPS among them per Bloomberg syndication), Sep 2023; KBRA DLD called it the largest US private credit loan ever at the time; purpose was to **refinance debt raised in the US and European leveraged loan markets** (a BSL→private "steal"); prior record Zendesk ≈ \$5B (2022). Early reporting had Vista seeking \$6B with a \$5.3–5.4B unitranche. CHECK lender names.
- **Secondaries 2025** (search listing; Evercore/Campbell Lutyens/Ropes & Gray; CHECK exact figures until fetched): total secondaries volume record ≈ \$226B (Evercore, +41%; LP-led \$120B +34%, GP-led \$106B +51%) / ≈ \$225B (Campbell Lutyens; LP-led \$121B +54%, GP-led \$93B +42%) / \$240B (Ropes & Gray, +48%). Private credit: GP-led PC secondaries ≈ +300% YoY (Ropes & Gray); GP-led = 61% of PC secondary activity, PC LP-led +45% (Campbell Lutyens); PC ≈ 11% of GP-led volume (Evercore). No single authoritative PC dollar total found.
- **J.P. Morgan \$50B**: VERIFIED-URL https://www.jpmorgan.com/about-us/corporate-news/2025/jpmorgan-increases-direct-lending-commitment-to-50-billion (dateline Miami, 24 Feb 2025); "Additional details around the co-lending arrangements have not been disclosed"; Dimon: "We proudly bank 80,000 companies globally through our Commercial and Investment Bank".
- **Asness, "The Illiquidity Discount?", 19 Dec 2019**: VERIFIED-URL https://www.aqr.com/Insights/Perspectives/The-Illiquidity-Discount . Exact: "What if investors will actually pay a higher price and accept a lower expected return for very illiquid assets?" and "Attractive smoothness of returns may not come for free." The phrase "volatility laundering" does NOT appear in this piece (it is from later Asness writing; cite as Asness, 2023, "Volatility Laundering" only as TITLE-ONLY/CHECK).
- S&P CDX Financials launch PDF (25 Feb 2026) returned HTTP 403; constituent details remain CHECK. Search summary: 25 NA financial entities, equal-weighted, semi-annual roll, BDCs/private-credit managers ≈ 12%, trading from 13 Apr 2026 (per 4 Mar 2026 update), Barclays-led demand commentary; name list CHECK.

**Web facts, round 4 (VERIFIED unless marked):**
- **OBDC quarterly series (company releases, VERIFIED-URLs detail/90, /92, /94 on blueowlcapitalcorporation.com):**

| Quarter end | NAV/sh | Non-accrual % at cost | at FV | Net D/E | Portfolio FV | Companies | Adj. NII/sh | Note |
|---|---|---|---|---|---|---|---|---|
| 31 Dec 2024 | \$15.26 | – | – | – | – | – | – | – |
| 30 Sep 2025 | \$14.89 | 2.7% | 1.3% | 1.22x | \$17.1B | 238 | \$0.36 | merger announced 5 Nov, pulled 19 Nov |
| 31 Dec 2025 | \$14.81 | 2.3% | 1.1% | 1.19x | \$16.5B | 234 | \$0.36 | Q4 buybacks ~\$148M at 86% of book |
| 31 Mar 2026 | \$14.41 | 2.0% | 1.0% | 1.13x | \$15.3B | 230 | \$0.31 | \$1.5B sales+repayments; base div cut to \$0.31 from Q2 |
| 30 Jun 2026 | \$14.26 | 2.8% | 0.8% | 1.11x | \$15.0B | 229 | \$0.34 | shares 499.4M→493.1M (Dec→Jun); Q2 PIK ≈ \$31.6M |

  Implied carrying value of the non-accrual bucket at 30 Jun 2026 ≈ (0.8/2.8) × (portfolio FV/cost) ≈ 0.29 × ~0.98 ≈ 28% of cost (derived; FV/cost ratio approximate). The release language for the Q2 NAV drop: "markdowns on a small number of names". Annualized dividend yield on NAV 9.3% (Q2 2026) vs 10.0% (Q4 2025). OBDC Q1 2026 release does not mention the \$400M sale; it reports \$1.5B total sales and repayments.
- **Octus, 16 Apr 2026** (VERIFIED-URL https://octus.com/resources/blog/bdcs-trading-at-50-discount-to-nav-but-nonaccruals-ticking-downward/ ): "BDCs now trade at nearly a 20% discount to net asset value, with certain large names approaching a 50% discount"; non-accruals "ticked lower to just 1.45% of cost" (from 1.47% in Q3 2025); adjusting for commonly held loans "increases nonaccruals as a percent of cost to 2.18%"; "Octus identified pricing gaps of nearly 40 points as measured by fair value divided by par" in widely held stressed loans; private credit restructuring recoveries "approximately 50 cents on the dollar", "well below the 70% previously cited by many managers". (The commonly-held adjustment is the same-loan cross-holder dispersion idea from the dossier, now with a number.)
- **NAIC resource page** (VERIFIED-URL https://content.naic.org/resource-center/private-credit-insurance-regulation ): definition "Private credit generally means debt investments that are not publicly issued or traded." Timeline: 2021 private rating rationale reports, revised bond RBC factors; 2022 structured-securities RBC project, PE-owned-insurer considerations; 2023 investment-oversight modernization, AG 53; **2024 "Authorized regulators to challenge or override NAIC Designations assigned through the filing exemption process"**; 2025 RBC principles, AG 55, Invested Assets Task Force created; 2025–26 enhanced statutory reporting for private placements effective with 2026 reporting; "Regulators are updating capital treatment for complex investments, including collateralized loan obligations". No dollar figures on the page; the \$1.2T / \$544B / \$483B PLR numbers remain CHECK (Insurance Business / Fitch via search).
- **FactSet Insight, Stewart Johnson, 29 May 2026** (VERIFIED-URL https://insight.factset.com/almost-one-fifth-of-insurer-held-private-securities-are-not-rated-but-disclosure-is-changing ): "At year-end 2025, 19.7% of all filings were unresolved"; "Private investments reached 38.7% of corporate bond holdings in 2024"; life-insurer private placement bonds +6.3% in 2024; Item 2025-19 effective 31 Dec 2026 "will require insurers to quantify every private placement on their books" supported only by PLRs, with fair value and book value.
- **Finastra, Kirkland & Ellis release, 14 Sep 2023** (VERIFIED-URL https://www.kirkland.com/news/press-release/2023/09/kirkland-advises-finastra-group-on-53-billion-refinancing ): "a \$4.82 billion senior secured unitranche term loan facility" and "a \$500 million senior secured multicurrency revolving credit facility"; "the refinancing of its existing credit facilities"; "a Vista Equity Partners portfolio company"; "more than twenty lenders and borrowers in multiple jurisdictions"; lenders unnamed (Davis Polk for agent/arrangers). Lender names (Oak Hill, Blue Owl, HPS) and "largest US private credit loan" (KBRA DLD) remain CHECK via Bloomberg syndication.
- **Cliffwater Direct Lending Index** (search listing; fact page https://cliffwater.com/files/cdli/docs/CDLI_Fact_Page.pdf , fetch to verify): launched 2015, reconstructed back to 30 Sep 2004 from quarterly SEC filings of BDCs whose primary assets are US middle-market loans; measures "unlevered, gross of fee performance ... as represented by the asset-weighted performance of the underlying assets of BDCs"; loss-rate (not default-count) methodology; ~14,800 loans / \$315B (31 Dec 2023); ~17,300 / ~\$393B (Nov 2024); a secondary source says ~21,000 / \$549B (date CHECK); Cliffwater release 31 Mar 2026: CDLI 2025 total return 9.3%, 2025 loss rate 0.70% vs historical average 1.01%. CHECK all until fact page fetched.
- **Private-credit ETFs/wrappers** (search listing): PRIV launched 26 Feb 2025; by its first anniversary ~\$850M AUM with ~\$745M inflows since start of 2026 (etftrends, CHECK; the dossier has \$802.8M on 15 Oct 2026 from SSGA, VERIFIED); expense ratio reported as 0.55% vs 0.70% in different sources (CHECK; issuer cut fee); Simplify VettaFi Private Credit Strategy ETF (PCR) launched Sep 2025, tracks a BDC/closed-end-fund index with a long/short credit hedge (CHECK). BondBloxx/Virtus private-credit CLO ETFs not found this session (CHECK; do not cite tickers).
- **Couts, Gonçalves, Rossi, "Unsmoothing Returns of Illiquid Funds", Review of Financial Studies 37(7), 2024, 2110–2155, DOI 10.1093/rfs/hhae006** (search listing incl. ideas.repec; SSRN id 3544854 appears in a USC-hosted filename): funds with similar holdings share a common source of spurious autocorrelation that standard unsmoothing misses, so systematic risk is underestimated; generalized unsmoothing; applied to hedge funds and private CRE funds; average illiquid-fund alpha lower than previously thought. TITLE+DOI (treat as VERIFIED citation).
- **Q1–Q2 2026 redemption quarter** (search listing; Reuters 6 Apr 2026 and others; CHECK each): Barings Private Credit Corp capped at 5% after Q1 requests of 11.3% of shares, filling ~44.3% of each request (fund ≈ \$4.9B); Blue Owl Credit Income Corp (OCIC) requests ≈ 21.9% of shares in the quarter to 31 Mar 2026 (another listing said 40.7% — conflicting, CHECK which fund/measure), Moody's moved OCIC outlook to negative (8 Apr 2026); "most large managers, including Apollo, Blue Owl, Ares, and BlackRock, capped withdrawals at 5% in the first quarter"; Apollo Debt Solutions (~\$26B) throttled after requests rose to 17% (InvestmentNews, CHECK); Apollo Debt Solutions and Blackstone's flagship credit fund (BCRED) imposed 5% limits in Q2 2026 (CHECK); Bloomberg Law: investors waiting to pull ~\$5B (CHECK); KKR restricted withdrawals from a PC vehicle (CHECK). Moody's negative outlook on the whole US BDC sector (dossier, Reuters 7 Apr 2026) could not be fetched (Reuters blocked): remains CHECK.

**Web facts, round 5 (VERIFIED unless marked):**
- **Cliffwater CDLI release, 31 Mar 2026** (VERIFIED-URL via Cision mirror https://digital-release.kxan.com/business/press-releases/cision/20260331LA23388/cliffwater-direct-lending-index-data-supports-strength-of-private-credit ): "CDLI returned 9.3% for the calendar year" 2025; "Interest income equaled 10.4% for the year and remained the main driver of return"; "~21,000 directly originated US middle market loan holdings totaling \$549 billion in assets"; "payment-in-kind (PIK) interest income steady at 0.7% (7.3% of total income)"; 20-year average 9.5% with one negative year (2008); non-accruals and realized losses "held steady or improved and remain well-below historical averages"; index "has not been reviewed by an independent accounting firm". The Cliffwater fact-page PDF returned 503; methodology wording (asset-weighted, gross of fees, unlevered, back-filled to 30 Sep 2004 from BDC SEC filings) remains from search listing, CHECK.
- **Apollo Debt Solutions (ADS), InvestmentNews 23 Jun 2026** (VERIFIED-URL https://www.investmentnews.com/alternatives/apollo-throttles-withdrawals-from-26b-private-credit-fund-after-exit-requests-rise-to-17/267119 ): "\$26-billion private credit fund"; Q2 2026 redemption requests "reached 16.8% – equivalent to \$2.4 billion"; capped at 5% of shares, "the standard limit for such vehicles" (pro-rata fill ≈ 30%, derived); Blue Owl: April exit requests from two non-traded BDCs "roughly 20% and 40%" (this reconciles the 21.9% / 40.7% conflict: two different funds, OCIC ≈ 20% and OTIC ≈ 40%, CHECK mapping); Blackstone \$79B BCRED repurchase requests "amounting to 10% of shares outstanding" for the quarter to 30 Jun 2026; Morgan Stanley North Haven Private Income Fund limited to 5% in March.
- **Bloomberg Law, 26 Mar 2026** (paywalled; headline and lede only, VERIFIED-URL https://news.bloomberglaw.com/banking-law/private-credit-funds-trap-5-billion-as-investors-rush-for-exit ): investors sought ≈ \$13B from "over a dozen funds" in Q1 2026; with 5%-of-net-assets quarterly caps they could access ≈ two-thirds; "more than \$4.6 billion of investor capital trapped behind withdrawal limits".
- **PipelineRoad redemption tag page** (aggregator; each item CHECK against its cited primary): 24 Mar 2026 ADS Q1 requests "exceeded 11.2%", cap 5%; 2 Apr 2026 Blue Owl OTIC + OCIC requests "around \$5.4 billion" combined, limited to 5%; 2 Apr 2026 KKR FS Income Trust Q1 requests 6.3% of shares; 7 Apr 2026 Barings Private Credit Corp 11.3%, cap 5%; 8 Apr 2026 Moody's revised outlook on Blue Owl's "\$36bn OCIC fund to negative"; 4 Sep 2026 BCRED Q3 repurchase requests "about \$4.3bn" (~10%), honoring 5%; 14 Sep 2026 HPS Corporate Lending Fund (\$23.1bn, BlackRock) Q3 requests fell (Reuters); 26 Mar 2026 Ares Strategic Income Fund had its "largest monthly decline since inception in February"; Cliffwater fund requests ~16% capped at 5%; Carlyle also listed.
- Shelf: Moyer_Distressed_Debt_Analysis p.313 (VERIFIED): "one of the sources of opportunity in distressed debt investing is the fact that the securities are often illiquid. Liquidity, of course, is a matter of degree." Also the 32/34 quote example: "an investor could sell \$5 million at 32 and buy that amount at 34."

### 6.1 Dated synthesis: the twenty facts the chapter must carry (newest first)

| date | fact | status / source |
|---|---|---|
| 16 Oct 2026 | Fed Z.1 adds private credit: loans \$1,042.6B (2023) → \$1,253.6B (2024) → \$1,493.5B (2025); holders PD funds \$532B, BDCs \$456B, RoW \$376B, interval \$76B, MM CLOs \$54B; PC = 6% of nonfinancial business debt vs 3% syndicated loans | VERIFIED (dossier; Brinkman et al. FEDS Note) |
| 15 Oct 2026 | PRIV: \$802.8M AUM, 363 holdings, 22.1% Apollo-sourced; Apollo must post daily firm bids | VERIFIED (dossier; SSGA page) |
| 14 Oct 2026 | Semi-liquid net assets \$15B (2018) → \$388B (2025); non-traded BDCs 0.2% liquid assets, 0.90 D/E | VERIFIED (dossier; George & Shin) |
| 1 Oct 2026 | Apollo daily pricing extended to all credit vehicles; asset-level from 30 Oct 2026; ICE >5,000 private IDs; >\$30B Apollo secondary volume since 2024 | VERIFIED (dossier; Apollo release) |
| 4–14 Sep 2026 | BCRED Q3 requests ≈ \$4.3B (~10%), honoring 5%; HPS Corporate Lending Fund (\$23.1B) requests fell | CHECK (aggregator citing Blackstone statement / Reuters) |
| 5 Aug 2026 | OBDC Q2 2026: NAV \$14.26; non-accruals 2.8% cost / 0.8% FV; net D/E 1.11x; \$15.0B, 229 companies | VERIFIED (company release) |
| 11 Aug 2026 | PC vs LL 2025 issuance: 5.0x vs 3.2x; S+500 vs S+400; 0% vs 28% BB+; 41% of large firms used both | VERIFIED (dossier; Banegas et al.) |
| 7 Aug 2026 | Banks charged BDCs +1.1pp in 2022; bank loans ≈ 40% of BDC debt; top-10 banks 82% of commitments | VERIFIED (dossier; Haque & Wang) |
| 23 Jun 2026 | ADS (\$26B) Q2 requests 16.8% ≈ \$2.4B, capped at 5%; Blue Owl April requests ≈ 20% and 40% at two non-traded BDCs; BCRED Q2 ≈ 10% | VERIFIED-URL (InvestmentNews) |
| 29 May 2026 | Insurers: 19.7% of private-security filings unresolved at YE2025; private investments 38.7% of corporate bond holdings (2024); Item 2025-19 PLR disclosure from 31 Dec 2026 | VERIFIED-URL (FactSet) |
| 8 May 2026 | Fed FSR: semi-liquid \$425B gross / \$241B net; Q1 2026 redemptions exceeded inflows for the first time; LL spreads widened on software concentration before PC spreads "ticked up" | VERIFIED (dossier) |
| 16 Apr 2026 | BDCs ≈ 20% discount, some near 50%; non-accruals 1.45% of cost (2.18% adjusted for commonly held loans); ~40-point same-loan FV/par gaps; recoveries ≈ 50c vs 70c cited | VERIFIED-URL (Octus) |
| 6–8 Apr 2026 | Barings PCC 11.3% requests, 5% cap, ~44% fill; KKR FS Income Trust 6.3%; Moody's negative outlook on OCIC (\$36B); sector-wide Moody's BDC outlook cut | Barings/KKR/OCIC CHECK (aggregators citing Reuters/PEW); sector outlook CHECK (Reuters blocked) |
| 31 Mar 2026 | CDLI 2025: 9.3% total return, 10.4% interest income, PIK 7.3% of income, ~21,000 loans / \$549B; median public BDC P/forward NAV ≈ 0.74 (Reuters/LSEG) | CDLI VERIFIED-URL; P/NAV CHECK |
| 26 Mar 2026 | ≈ \$13B of Q1 redemption requests across >12 funds; ≈ \$4.6B trapped behind 5% caps | VERIFIED-URL headline/lede (Bloomberg Law, paywalled) |
| 18 Feb 2026 | Blue Owl BDCs sell \$1.4B "at fair value, which is equivalent to 99.7% of par"; OBDC II RoC distribution ≈ 30% of NAV replaces tenders; OBDC Q4 2025 NAV \$14.81, buybacks at 86% of book, non-accruals 2.3% cost / 1.1% FV | VERIFIED (company releases) |
| 19 Nov 2025 | OBDC/OBDC II merger terminated "given current market conditions", 14 days after announcement; 98% portfolio overlap; NAV/NAV exchange when OBDC ≤ NAV | VERIFIED (company releases; overlap and ratio from 5 Nov release in dossier) |
| 24 Feb 2025 | JPM \$50B balance-sheet direct lending + ~\$15B co-lenders; >\$10B in >100 deals since 2021 | VERIFIED-URL |
| 26 Sep 2024 | Citi–Apollo \$25B program; Mubadala, Athene participate | VERIFIED-URL |
| 14 Sep 2023 | Finastra: \$4.82B unitranche + \$500M revolver refinances US and European leveraged loans | VERIFIED-URL (Kirkland); "largest ever" and lender names CHECK |

### 6.2 Older anchors (from the dossier; all VERIFIED there)
2010–2015: ~one-third of middle-market loans from nonbanks at ~190bp premium (Chernenko–Erel–Prilmeier). 23 Feb 2024: DL recoveries ~33% vs 52% syndicated vs 39% HY; ICR 2.0x vs 2.7x (Cai & Haque). 8 Apr 2024: PC ~\$2.1T global; PC assets "tended to show smaller markdowns during stress than leveraged loans" (IMF). 11 Mar 2025: BDC D/E 0.4 → >1 supplied ~150bp of funding-cost convergence; HHI 0.74 vs 0.2 (BIS). 21 Mar 2025: CLO/BDC packaging cuts RBC ~10×; affiliated BDCs >\$100B (Fed). 21 May 2025: 97% of Y-14 bank exposure to BDCs is first-lien; "a CLO in which banks hold the top tranche" (Boston Fed). 23 May 2025: \$95B committed lines, \$56B drawn, +145% in five years (Fed). 14 Apr 2026: software ≈ one-fifth of DL loans, >50% of NAV in some levered vehicles; 5–7 quarter buffers under moderate shock (IMF). Jan 2026: BDCs with >200 borrowers 9.5% ROE vs 6.1% for <100 (Cliffwater via BlackRock primer). 4Q2025: 58.3% "bad PIK" among PIK payers (Lincoln via BlackRock chartbook).

### 6.3 Academic and legal anchors added this session
Getmansky–Lo–Makarov (NBER w9571, 2003; JFE 2004, CHECK volume/pages) — smoothing model. Couts–Gonçalves–Rossi (RFS 37(7), 2024, DOI 10.1093/rfs/hhae006) — common smoothing across funds. Davydiuk–Marchuk–Rosen (JFE 162, 2024, 103946) — BDC SOI data as a credit-supply laboratory. Ellias & de Fontenay, *The Credit Markets Go Dark*, 134 Yale L.J. (Jan 2025) — BDC loan count 1,395 → 20,182 (2010–2022); fewer bankruptcies but more forbearance and "zombie firms". Asness, *The Illiquidity Discount?* (AQR, 19 Dec 2019) — "Attractive smoothness of returns may not come for free." Erel–Flanagan–Weisbach (NBER w32278, 2024) — net-of-fee alpha insignificant. Dimson (1979, JFE 7:197–226) and Scholes–Williams (1977, JFE 5:309–327) — aggregated betas (TITLE-ONLY, standard). Geltner (1991, J. Real Estate Fin. Econ. 4:327–345; 1993, J. Real Estate Research 8:325–345) — appraisal unsmoothing (TITLE-ONLY, standard).

### 6.4 CHECK list (do not print in prose without re-fetching)
1. Median public BDC P/forward NAV ≈ 0.74 at end-Mar 2026 (Reuters/LSEG via aggregator); 9fin average discount 23.2% vs 6.9% a year earlier; Prospect 57.2% discount (DEF 14A wording).
2. Moody's cut of the *sector* US BDC outlook to negative, 7 Apr 2026 (Reuters, blocked). OCIC-specific negative outlook (8 Apr 2026) via aggregator.
3. Barings PCC 11.3% / 44.3% fill; KKR FS Income Trust 6.3%; Cliffwater fund ~16%; Morgan Stanley North Haven 5% limit (Mar 2026); BCRED \$4.3B Q3 (Sep 2026).
4. Which Blue Owl non-traded BDC had ~20% and which ~40% (OCIC vs OTIC) in Q1 2026; the "\$5.4B combined" figure.
5. CDX Financials constituent list, the 12% private-credit weight, the 13 Apr 2026 first trading date, and whether Blue Owl was dropped (S&P PDFs returned 403).
6. Insurer figures: \$1.2T PC at YE2025, \$544B in PLR bonds + BDCs + PC funds (NAIC), PLRs \$483B vs \$420B and 58% Level 3 (Fitch), 106-of-109 notch study.
7. CDLI methodology wording (asset-weighted, gross of fees, unlevered, back-filled to Sep 2004) and the 1.01% historical loss rate; CDLI fact page returned 503.
8. Finastra lender names (Oak Hill, Blue Owl, HPS) and "largest US private credit loan" (KBRA DLD); Zendesk \$5B prior record.
9. Secondaries dollar figures (\$226B Evercore / \$225B Campbell Lutyens / \$240B Ropes & Gray) and the PC GP-led ≈ +300%; Ropes & Gray page returned 403.
10. PRIV expense ratio (0.55% vs 0.70%) and ~\$850M at first anniversary; Simplify PCR launch details.
11. OBDC FY2025 PIK ≈ 6.9% of total investment income (fetch-tool arithmetic; confirm in 10-K).
12. Getmansky–Lo–Makarov JFE citation details; SSRN ids for Ellias–de Fontenay (4879742) and Couts et al. (3544854) appear only in search listings.
13. Dossier CHECKs still open: First Brands amounts, Tricolor SEC charges, MFS figures, Preqin \$129B 9M2026 fundraising, Jefferies 87% of NAV LP pricing.

## 7. Case studies

### 7.1 The natural experiment: OBDC / OBDC II, 5 Nov 2025 → 18 Feb 2026 (the chapter's anchor case)
**Facts (all VERIFIED on Blue Owl's site unless marked).** 5 Nov 2025: merger proposed; ~98% portfolio overlap; exchange ratio NAV-for-NAV if OBDC trades at or below NAV, so non-traded OBDC II holders would receive listed shares worth *less than NAV* at market; OBDC II suspends tenders pending close (dossier). 19 Nov 2025: terminated "given current market conditions"; OBDC II to reinstate tenders in Q1 2026; OBDC keeps a \$200M buyback. 18 Feb 2026: OBDC Q4 NAV \$14.81 (from \$14.89), buybacks of ~\$148M at 86% of book; non-accruals 2.3% at cost vs 1.1% at FV; the same day, three Blue Owl BDCs sell \$1.4B of partial interests (97% senior secured, 128 borrowers, software 13%) to four pension/insurance buyers "at fair value, which is equivalent to 99.7% of par"; OBDC II uses its \$600M (34% of commitments) to pay a return-of-capital distribution of up to \$2.35/share (~30% of NAV) and moves from quarterly tenders to RoC distributions. Then NAV \$14.41 (Mar), \$14.26 (Jun) with non-accruals 2.8% cost / 0.8% FV.
**Why it is the perfect case.** Same loans, two wrappers, three prices in one quarter: the listed price (0.86 of book), the fair-value mark (≈1.00 of book), and a transaction (99.7% of par) between a seller who needed liquidity and buyers who were told it was fair value. §3.2 turns 0.86 into $m\approx4\%$ of assets; §3.3 turns 2.8/0.8 into a 28c carrying value on bad loans; the \$1.4B print says the *good* loans clear at par, which is exactly what adverse selection in a partial-interest sale predicts (you sell the loans a pension fund will buy). **How a systematic desk would have traded it:** short OBDC vs long a diversified BDC basket into the merger announcement (the NAV/NAV ratio with OBDC below NAV is a transfer from OBDC II holders, which investors would resist), cover on termination; long OBDC unsecured notes vs short OBDC equity through Q1 2026 (deleveraging from 1.22x to 1.11x and asset sales at par are bondholder-positive, equity-neutral); monitor the redemption queue of OCIC/OTIC as the leading indicator for further sales. Cooperation agreements signed in this chapter: 0; return-of-capital distributions substituted for tenders: 1.

### 7.2 The BSL→private "steal" and its reversal: Finastra 2023 and the 2024 dual-track year
**Facts.** 14 Sep 2023 (Kirkland release, VERIFIED): \$4.82B senior secured unitranche + \$500M multicurrency revolver refinancing Finastra's existing US and European leveraged-loan facilities; Vista-owned; >20 lenders and borrowers. Reported as the largest US private credit loan at the time (KBRA DLD via Bloomberg, CHECK), with Oak Hill, Blue Owl, HPS among lenders (CHECK). Context: the Fed's "tight LL" regime (May 2022–Sep 2024) and LL→PC switching near 50% of LL borrowers in early 2023; by 2024–9M2025 takeouts were "considerably balanced" as BSL spreads compressed and borrowers ran dual tracks. **Lesson for §17.4:** flow direction is a function of a public regime variable; a desk with the LL excess-loan-premium series could have forecast both the 2023 steal wave and the 2024 reverse wave. **Trade:** the PC→BSL reverse wave is new BSL supply; short CLO BB/B tranches or long CLO AAA spread duration ahead of a supply bulge (cross-ref Ch 21).

### 7.3 The Q1–Q3 2026 redemption quarter(s)
**Facts (dated; VERIFIED-URL unless marked).** Q1 2026: ≈\$13B requested across >12 funds, ≈\$4.6B trapped (Bloomberg Law, 26 Mar); Barings PCC 11.3% requests, 5% cap, ≈44% fill (CHECK); KKR FS Income Trust 6.3% (CHECK); ADS >11.2% (CHECK); Blue Owl OCIC/OTIC ≈20% and ≈40%, ≈\$5.4B combined (InvestmentNews/aggregators, CHECK mapping); Moody's negative outlook on OCIC (8 Apr, CHECK); Fed FSR (8 May): accepted redemptions exceeded inflows for the first time. Q2 2026: ADS 16.8% ≈ \$2.4B, capped at 5% (InvestmentNews, 23 Jun); BCRED ≈10% of shares. Q3 2026: BCRED ≈\$4.3B (~10%), honoring 5% (CHECK); HPS Corporate Lending Fund requests fell (CHECK). **Model mapping:** §3.5's run condition and runway. With $q=0.168$ and $c=0.05$ the fill is ≈30%; unfilled requests roll into $q_{t+1}$; the fund's choices are sell the sleeve (public loan prices fall), draw the line (bank funding premium rises as in 2022), or convert to RoC distributions (OBDC II). **Desk signal:** the 8-K/N-23c-3 request percentage per fund is a public, dated, numeric series that leads BDC equity and BDC bond spreads; build the `redemptions` table in §4 first.

### 7.4 The double-pledge trilogy: First Brands, Tricolor, Market Financial Solutions (Sep 2025–Sep 2026)
From the dossier (all CHECK on amounts): First Brands Ch. 11 (Case 25-90399) with ~\$2.3B allegedly missing via double-pledged receivables, converted to Ch. 7 on 1 Sep 2026; Tricolor Ch. 7 with loans allegedly pledged to multiple ABS deals; MFS administration with an alleged £930M shortfall. **Role in the chapter:** the case where $\sum\theta_k<1$ (the marks never catch up because the collateral was not there) and the reason the Mark-Gap Monitor needs a collateral-uniqueness tell (UCC lien overlap; receivables purchased off-platform). Keep it short; Ch 14 and Ch 25 own the forensic detail.

### 7.5 The wrapper that posts a bid: PRIV (Feb 2025–Oct 2026)
VERIFIED (dossier/SSGA): launched 26–27 Feb 2025 with a 10–35% private-credit policy; \$802.8M AUM, 363 holdings, 22.1% Apollo-sourced at 15 Oct 2026; Apollo must post daily firm, executable bids and buy back within stress-redemption limits. **Role:** the first ETF whose NAV for the private sleeve is a *contractual bid*, which converts the smoothing problem into a counterparty problem; premium/discount arbitrage (Ch 20 mechanics) is bounded by the firm-bid facility's limits rather than by AP creation costs.

### 7.6 Banks move up the stack: Citi–Apollo (26 Sep 2024) and J.P. Morgan (24 Feb 2025)
Both VERIFIED-URL. **Role:** evidence for TW3 and the flow graph: banks originate and distribute into private vehicles while holding the senior revolver (Y-14: 97% first-lien; \$95B committed lines); the "partnership" is a senior tranche plus a fee, not a retreat. Use Dimon's "80,000 companies" line as the origination-funnel fact and Boston Fed's CLO analogy as the structure.

## 8. Humor beats (canon cast)

(pending)

## 9. Resource candidates

(pending)

## 10. Exploratory-space notes

(pending)
