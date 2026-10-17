# Advisor Brief — Chapter 10: Trend-Following & Time-Series Momentum in Credit (TREND)

**Target file:** `book_src/10_ch10_trend_and_time_series_momentum.md` (7,000–10,000 words)
**Advisor:** Fable, Edition 1 editorial board. Research date: 2026-10-17.
**Status key:** VERIFIED = fetched or read this session; SEARCH-LISTED = URL appeared in a search result but the page was not fetched; CHECK = plausible but unconfirmed, do not state as fact without a source.

---

## 1. Thesis and the "aha" for the ex-PJT-RSSG reader

**Thesis.** Trend-following in credit is the stop-loss the reader has been running by hand for years, written down, sized by DTS, and executed in the one credit instrument that trades like a future: the on-the-run CDX/iTraxx index. Everything that makes trend hard in credit (negative skew of long credit, spread-level-dependent volatility, stale cash prices, jumps from LMTs and defaults, a V-shaped Fed put) follows from credit's payoff shape, and each consequence is derivable.

**Three "aha" moments:**

1. **Volatility scaling in credit *is* DTS scaling.** Ben Dor et al. show spread volatility is linear in spread level with zero intercept (`Ben_Dor p.74`), so $\sigma(r^{ex}) \approx \beta\cdot\text{DTS}$ and the Moskowitz–Ooi–Pedersen position $w_t=\sigma_{\text{tgt}}/\sigma_t$ becomes $w_t \propto 1/\text{DTS}_t$: the trend follower de-risks as spreads widen, exactly like the rating or DTS stop-loss that Ben Dor warns "does well in trending markets and poorly in choppy markets" and can feed "a vicious cycle" (`Ben_Dor p.292`). The reader's old job was the other side of that cycle (buying fallen angels from forced sellers, `Dynkin` Chs 2–3). Kim–Tse–Wald's finding that most of TSMOM's alpha comes from vol scaling rather than the sign lands with special force here.

2. **Carry and trend disagree exactly when it matters.** With $\Delta s_{t+1} = \kappa(\bar s - s_t) + \phi\,\Delta s_t + \epsilon_{t+1}$, expected excess return is $s_t\Delta t - D^{\text{spr}}[\kappa(\bar s - s_t) + \phi\Delta s_t]$: carry/value ($s_t$, $\kappa$) says buy after widening, trend ($\phi$) says sell. 2008 and 2022 were $\phi$-years; March 2020 and April 2025 were $\kappa$-weeks. The chapter sizes both coefficients instead of picking a tribe; Man 2022 notes carry "can have fantastic years and also very poor years" (`Man_Quantitative p.26`).

3. **Equity leads credit, so the best credit trend signal is often not a credit price.** Hilscher–Pollet–Wilson (JFQA 2015) find equity leads CDS at daily and weekly horizons, not the reverse; Dynkin's Equity Momentum in Credit (EMC) earns 6.34%/yr (IR 1.56) in IG and 15.9%/yr in HY before costs, and the top-decile signal has an 83% chance of decaying within three months (`Dynkin pp.607, 610, 628`). The RSSG reader already watches the equity of the names whose debt they trade; the chapter turns that reflex into a specification.

**The PJT bridge in one line:** a restructuring banker knows a bond at 60 "has momentum" toward a process, not toward 40 or 80. Trend formalizes the first half of that sentence and is silent on the second; the chapter must show where the jump (LMT, filing, DIP) breaks the diffusion assumption and how to specify an engine that knows it.

---

## 2. Section outline, anatomy mapping, Trend Watch boxes

Legend: **DF** desk framing · **DER** derivation · **SPEC** AI-coder spec · **SRC** source extraction · **CASE** case study · **RG** resource graph (close every major section) · **TW** Trend Watch.

**Cold open (≤400 words).** Ines asks Theo why the desk's CDX HY position flipped to long protection at 4:02 p.m. the day after the tariff announcement and whether "the model is panicking." Kaz: it has no amygdala, only a 60-day EWMA. Mags: it looks like 2008 and nothing like 2008. Question: *when is a move in spreads information about the next move in spreads, and how much should you bet on it?*

- **10.1 What a trend is, in credit (DF, DER, SRC).** Trend vs cross-sectional momentum (`Paleologo p.74`); instruments (CDX IG/HY, iTraxx Main/Crossover, cash index excess returns, HYG/LQD); why index CDS is the futures-like leg; sign conventions (spread up = price down; "long risk" = sold protection). **TW #1: The index CDS market as the trend follower's venue, 2021–2026.**
- **10.2 The TSMOM engine, adapted (DER, SPEC).** MOP signal, vol targeting, lookbacks; CDS carry-plus-spread-change return; HY price-quoted vs IG spread-quoted; series rolls and splicing (D1).
- **10.3 Vol scaling is DTS scaling (DER, SRC, Ways This Blows Up).** Ben Dor's linear law; Kim–Tse–Wald; the stop-loss feedback loop (`Ben_Dor p.292`, `Dynkin p.397`) (D2). Box: *Desk Myth vs Desk Reality*.
- **10.4 Trend plus carry (DER, SRC, SPEC).** OU-with-inertia model; Koijen et al. carry; Baz et al. complementarity; Man 2022 on carry's volatility (D3).
- **10.5 Cross-asset trend: equity → credit (DER, SRC).** Hilscher et al.; Norden–Weber; Acharya–Johnson (the CDS-leads exception); Lee–Naranjo–Velioglu; Lee–Naranjo–Sirmans CDS momentum; Dynkin EMC construction, decay, sector timing; Haesen residual momentum; Pitkäjärvi et al. as template (D4).
- **10.6 Crisis alpha and the payoff's shape (DER, SRC, CASE).** Trend as a long straddle on the 12-month move; quadratic regression; Daniel–Moskowitz; Paleologo's Merton account of 2009; Fidelity's beta-timing decomposition (D5, D6). **TW #2: CTAs, speed and the 2024–2025 drawdown.**
- **10.7 Case studies: 2008, 2020, 2022, with an April 2025 coda (CASE, SRC).** See §7.
- **10.8 Turnover, costs, capacity (DER, SRC, SPEC).** Sign-flip turnover; EWMA crossovers; `Man_Quantitative p.19`; CFTC and Collin-Dufresne–Junge–Trolle cost facts; cash LCS; break-even math. Optional TW #3: "CTAs slowed down after 2007" (SG heat map).
- **10.9 Trend in the LMT era: jumps, not diffusions (DF, DER).** Single-name gap risk vs index; survival-adjusted signals; Schmid's rating momentum (`p.48`) as fundamental trend; cross-reference Ch 13–14.
- **10.10 Desk Debrief, The Spec You Hand the Robot, exercises.**

---

## 3. Derivation skeletons

All signals and performance statistics are under $\mathbb{P}$; the only $\mathbb{Q}$ object is the CDS risky annuity that converts spread changes to P&L. Say so in the chapter.

### D1. TSMOM signal and position (Moskowitz–Ooi–Pedersen 2012, adapted)

$$
\text{sig}^{(h)}_{i,t} = \operatorname{sign}\!\Big(\textstyle\sum_{k=0}^{h-1} r^{ex}_{i,t-k}\Big), \qquad
w_{i,t} = \frac{\sigma_{\text{tgt}}}{\hat\sigma_{i,t}}\,\text{sig}^{(h)}_{i,t}, \qquad
r^{\text{TSMOM}}_{t+1} = \frac{1}{N}\sum_{i=1}^{N} w_{i,t}\, r^{ex}_{i,t+1}.
$$
$\hat\sigma_{i,t}$: EWMA annualized vol (MOP use a 60-day center of mass and $\sigma_{\text{tgt}}=40\%$ per instrument; state as their choice). Smoother variant: $\text{sig}_t=\tanh\!\big((\text{EWMA}_f(P_t)-\text{EWMA}_s(P_t))/(\hat\sigma_t\sqrt{h})\big)$; SG's "Trend Indicator" is a 20d/120d crossover (SG, May 2025).

**Credit excess return.** Funded long-risk index CDS with coupon $c$ (100 bp IG, 500 bp HY by convention; CHECK), par spread $s_t$, risky annuity $A_t$ (a $\mathbb{Q}$ quantity from the ISDA standard model):
$$
r^{ex}_{t+1} \approx \underbrace{s_t\,\Delta t}_{\text{carry}} - \underbrace{A_t\,(s_{t+1}-s_t)}_{\text{mark-to-market}} + \underbrace{\tfrac12\,\Gamma_t (s_{t+1}-s_t)^2}_{\text{convexity}},
$$
and for a cash index $r^{ex}_{t+1} \approx s_t\Delta t - D^{\text{spr}}_t\,\Delta s_{t+1}$ over duration-matched Treasuries (Dynkin's data definition, `p.605`). **Error-prone:** sign of the MTM term; CDX HY is price-quoted, so build returns from price plus accrued coupon; upfront vs running conventions; splicing on-the-run series (ISDA: the roll window carries 25–50% of quarterly notional) manufactures returns if you difference across series; ACT/360 for $\Delta t$; a 12-month OAS *level* comparison differs from a 12-month *return* sum by carry, whose sign opposes the spread move.

### D2. Volatility scaling in credit is DTS scaling

Ben Dor: $\sigma(\Delta s_i) = \alpha + \beta s_i$ with $\alpha\approx 0$ (`p.74`). With $\sigma(r^{ex}_i)\approx D^{\text{spr}}_i\,\sigma(\Delta s_i)$:
$$
\sigma(r^{ex}_{i,t}) \approx \beta\,\text{DTS}_{i,t}
\quad\Longrightarrow\quad
w_{i,t} = \frac{\sigma_{\text{tgt}}}{\beta\,\text{DTS}_{i,t}}\,\text{sig}_{i,t}.
$$
Consequences: spread-DV01 is constant per unit of spread, so notional shrinks as spreads widen; P&L splits into a sign component and a vol-timing component (Kim–Tse–Wald: 1.27% vs 0.41% monthly alpha with and without scaling, 55 futures, 1985–2013). Assumptions: $\beta$ stable within rating bucket; Ben Dor's nonlinearity below ~20 bp breaks proportionality for tight IG. **Ways This Blows Up:** vol from stale cash prices is biased low (position too big); Paleologo (`p.98`) shows vol scaling is most dangerous when universe volatilities are heterogeneous, which describes any cross-rating credit book.

### D3. Trend plus carry under an OU-with-inertia spread process

$$
\Delta s_{t+1} = \kappa(\bar s - s_t) + \phi\,\Delta s_t + \epsilon_{t+1},\quad \epsilon_{t+1}\sim(0,\beta^2 s_t^2\Delta t)\ \text{under }\mathbb{P};\qquad
\mathbb{E}_t[r^{ex}_{t+1}] = s_t\Delta t - D^{\text{spr}}\big[\kappa(\bar s - s_t) + \phi\,\Delta s_t\big].
$$
Carry ($s_t\Delta t$) and value ($-D\kappa(\bar s-s_t)$, positive when $s_t>\bar s$) favor buying wide spreads; trend ($-D\phi\Delta s_t$) favors selling after widening when $\phi>0$. The optimal linear blend weights each predictor by coefficient over forecast variance; with small $\phi,\kappa$ carry dominates at monthly horizon, with large $\phi$ (2008, 2022) trend dominates. Koijen et al. (JFE 2018) define carry as the return if prices do not change and find it predicts credit returns; Baz et al. (2015) find TS momentum and carry are best combined. **Error-prone:** joint estimation of $\kappa,\phi$ on 25 years of monthly OAS gives standard errors as large as the coefficients; show the confidence region. Nuveen's "spreads tend to mean revert" (`p.4`) is a prior on $\kappa$, not evidence against $\phi$.

### D4. Equity → credit lead–lag

$$
r^{\text{cr}}_{t+1} = a + b\, r^{\text{eq}}_{t} + c\, r^{\text{cr}}_{t} + \varepsilon_{t+1},
$$
with Granger tests in a VAR(1). Dynkin's EMC signal: equal-weighted 1-, 3-, 6-month equity returns "rescaled for different lengths of the respective formation periods" (`p.606`, footnote 9; exact rescaling not on the page, CHECK; default to dividing by $\sqrt{h}$). Sector elasticity: 5–8 bp/month per 1%/month of equity momentum (`p.644`). **Error-prone:** stale bond prices manufacture a spurious lead (Dynkin tests via Trade Efficiency Scores, `p.621`, and 1–3 day lags, `p.630`); non-synchronous US equity vs European CDS closes; the long–short's credit beta flips sign across the cycle (`p.613`), so un-neutralized "lead–lag alpha" is mostly timing. Haesen et al. (2017): firm-specific equity returns halve default-risk exposure and double Sharpe; Dynkin finds the opposite in their sample (`p.631`). Put both on the page.

### D5. Crisis alpha as convexity

$$
r^{\text{TF}}_{t} = \alpha + \beta_1\, r^{\text{HY}}_{t} + \beta_2\, (r^{\text{HY}}_{t})^2 + u_t,\qquad \beta_2>0 \text{ is the smile.}
$$
Fung–Hsieh's lookback-straddle reading gives the intuition; Daniel–Moskowitz show momentum's short side has option-like payoffs in panic states, so losses arrive on the rebound. Credit twist: long credit is short a put on firm assets (Merton), so the short-credit leg of trend is long that put and more convex on the downside than equity trend at the same lookback. Fidelity (data to Dec 2025): SG Trend correlation to the S&P 500 −0.11 unconditionally, −0.31 in down months; 76% of a simple trend strategy's risk is beta timing. **Error-prone:** convexity lives at 6–12 month horizons; a daily quadratic fit finds nothing. Speed: SG shows faster models won in 2020 and slower ones since 2008.

### D6. Whipsaw arithmetic (stylized)

For a V of depth $d$ over $T$ months and a trend with effective lag $L<T/2$: net capture $\approx d\,(T/2-2L)/(T/2)$, negative when $L>T/4$. March 2020 and April 2025 had $T\approx 2$; 2008 had $T\approx 20$.

---

## 4. Code spec: `credit_tsmom.py`

**Inputs.** Daily OAS for US HY and IG (FRED `BAMLH0A0HYM2`, `BAMLC0A0CM`, decimal percent) from CSV if present; optional daily equity total-return series; otherwise a seeded simulator of D3 ($\bar s=4.5\%$, $\kappa=0.03$/month, $\phi\in\{0,0.25\}$, annualized spread vol 25% of level; label illustrative).

**Computes.** (1) Excess returns $r^{ex}_t = s_{t-1}\Delta t - D^{\text{spr}}\Delta s_t$, $D^{\text{spr}}=4.0$ HY, $7.0$ IG (illustrative), ACT/360. (2) Sign TSMOM at 1/3/6/12 months, 20/120-day EWMA crossover, ensemble. (3) EWMA vol (60-day center of mass) and the DTS alternative $\hat\sigma_t=\hat\beta D^{\text{spr}}s_t$, $\hat\beta$ from a zero-intercept regression of rolling spread vol on level; 10% target. (4) Trend + carry blend from D3. (5) Equity → credit regression and Granger test when an equity series is supplied. (6) Return, vol, Sharpe, max drawdown, turnover (sum of absolute weight changes), convexity regression ($\beta_2$, HAC errors), crisis-window table (2007-06→2009-06, 2020-02→2020-06, 2022-01→2022-10, 2025-02→2025-05) when covered.

**Shapes.** `S[T,N]` spreads, `R[T,N]` returns, `G[T,N] ∈ [-1,1]` signals, `W[T,N]` weights, `P[T]` P&L; signals at $t$ apply to $r_{t+1}$ (one-day lag; a second day mirrors Dynkin's lag test).

**Built-in sanity checks (asserted, seeded).** Random walk ($\kappa=\phi=0$): 12-month sign Sharpe within $\pm2/\sqrt{\text{years}}$ of zero. $\phi=0.25$: Sharpe exceeds the random-walk case by ≥0.3. Realized vol within 25% of the 10% target. A monotone widening path flips the position short within one lookback and earns positive P&L thereafter (sign guard). Constant spreads: cumulative excess return equals $s\times$ ACT/360 year fraction to 1e-10 (carry guard). Turnover of the pure sign strategy equals $2\times$ the number of sign flips. Pure numpy/pandas, seeded, no network calls inside the chapter block; the FRED download goes in a commented preamble.

---

## 5. Source map (shelf pages, why, exact quotation)

| Page | Why | Quotation (verbatim, ≤60 words) |
| :-- | :-- | :-- |
| `Dynkin p.603` | Opening claim | "Stock price returns and subsequent excess returns of corporate bonds tend to be positively related." |
| `Dynkin p.606` | Decile spread, IG 1993–2017 | "It delivered negative average excess return of –4.7% per year between 1993 and 2017. In contrast, the average excess return of the top decile portfolio (D10), with the strongest equity momentum, was +4.01% per year." |
| `Dynkin p.607` | Multi-horizon confirmation | "combining momentum signals at different horizons helps to validate (confirm) trends in stock prices. Indeed, a stock with continuing upward price trend over the previous six months has a stronger combined signal than a stock with positive price return over the past month only." |
| `Dynkin p.610` | Signal decay | "an issuer with equity momentum in the top 10% (D10) has only a 17% probability of remaining top ranked after three months" |
| `Dynkin p.613` | Time-varying credit beta | "the strategy net spread tends to decline and become negative during equity down‐cycles." |
| `Dynkin p.617` | Crisis performance | "While the corporate index has average returns of –8.07%/yr in drawdown episodes and 4.12%/yr in recovery times, the EMC strategy performed well in both regimes: 11.53%/yr in credit drawdowns and 4.30%/yr in recoveries." |
| `Dynkin p.628` | Summary | "The EMC strategy has been negatively correlated with equity and credit markets but positively correlated with a quality factor. Returns of the EMC strategy have been particularly strong during credit down‐cycles." |
| `Dynkin p.631` | Turning-point risk | "Haesen et al. (2017) argued that this varying exposure can make the strategy vulnerable in periods of market turning points, for example when a market downturn is followed by a recovery." |
| `Dynkin p.644` | Sector elasticity | "average excess returns tend to increase with equity momentum with each 1%/m of additional equity momentum translating into an extra 5 to 8bp of bond excess returns." |
| `Dynkin p.647` | Sector rotation | "A portfolio strategy that systematically invests in sectors with strong equity momentum outperformed the index by 2.38%/yr in US IG, by 4.04%/yr in US HY, and by 1.77%/yr in Euro IG in the 10 years between 2007 and 2017, with information ratios above one before transaction costs." |
| `Man_Quantitative p.25` | Issuer-level trends | "We generally find trends to be consistent across a capital structure and indeed across broader groups/ecosystems as well; these trends therefore tend to be less issue-specific and more at an issuer-level." |
| `Man_Quantitative p.25` | IG vs HY | "further analysis by Jostova et al. (2013) indicated minimal effects from following Momentum strategies in investment grade, but a more meaningful impact in the high yield market." |
| `Man_Quantitative p.19` | Turnover | "Within classic quant, Momentum tends to have the highest turnover of any factor approach while both Size and Quality see the least churn." |
| `Man_Quantitative p.26` | Carry's volatility | "Over the long run, Carry appears to offer a significant premium, but with incredibly high volatility of returns. This lack of consistency means that Carry as a signal can have fantastic years and also very poor years in terms of benchmark relative performance." |
| `Paleologo p.74` | Definition | "“Momentum” has a different meaning from trend-following, because it is based on relative performance, whereas the latter is based on absolute performance." |
| `Paleologo p.77` | 2009 crash | "During 2008, Momentum experienced higher volatility but did not lose money (see Figure 5.9). However, in 2009 the stocks that had experienced large losses in the previous year rallied as the market rebounded." |
| `Paleologo p.106` | Why vol targeting works | "Volatility is persistent and partially predictable, while PnL has no strong relationship to volatility." |
| `Ben_Dor p.74` | Linear vol–spread law | "The estimates of α are always insigniﬁcant, indicating once more that the relation between spread volatility and spread level is best described by a linear function that intersects the origin (i.e., α is equal to zero)." |
| `Ben_Dor p.292` | Stop-loss = momentum | "Generally, a momentum strategy like this one does well in trending markets and poorly in choppy markets. If enough market participants adopt this approach, it could lead to destabilizing behavior in which spread widening and asset sales reinforce each other in a vicious cycle." |
| `Ben_Dor p.388` | CDX vs cash in crises | "However, during the crisis, spreads of cash bonds widened by much more than CDS due to liquidity effects." |
| `Ben_Dor p.390` | Basis reversal | "the CDX-cash basis became very negative as the credit crisis unfolded but reverted back toward zero as the crisis abated." |
| `Schmid p.48` | Rating momentum | "Rating momentum means that prior rating changes may have predictive power for the direction of future rating changes. For example, downgrade rating momentum suggests that an obligor downgraded to B is more likely to be further downgraded than upgraded within the next year." |
| `Nuveen p.4` | Mean-reversion prior | "Typically, the process begins with the assumption that spreads tend to mean revert over time, usually fluctuating within a historical range rather than continually widening or tightening." |

Supporting pages: `Dynkin pp.608–609` (EMC 6.34%/yr, IR 1.56; 9.71%/yr Jul 2007–May 2017; Aaa–A 3.9%, Baa 8.8%, HY 15.9%), `pp.616–619` (six down-cycles; EMC +35.4% in Mar 2007–Nov 2008 vs index −24.2%), `p.620` (Fed cycles), `pp.629–630` (horizon and lag robustness), `pp.215–216` (2008 average CDX HY 788 bp vs HY index 899 bp; 2009: 950 vs 991), `p.397` (Aa stop-loss costs −18 bp/yr), `Ben_Dor p.73`, `Paleologo p.98`, `Man_Quantitative p.20` (HY bid-ask gapped Feb/Mar 2020), `BlackRock p.4` (HY managers earn excess returns in "Very Negative" regimes), `Bohn_Stein p.42` (dated).

---

## 6. RESEARCH DOSSIER (dated, sourced)

### 6.1 Canon papers (bibliography verified unless marked)

- **Moskowitz, Ooi, Pedersen (2012), "Time Series Momentum,"** *JFE* 104(2): 228–250, DOI 10.1016/j.jfineco.2011.11.003. 58 futures (equity index, FX, commodity, bond); 1–12 month persistence then partial reversal; diversified TSMOM "performs best during extreme markets"; speculators profit, hedgers pay. **No credit indices in the sample.** VERIFIED.
- **Hurst, Ooi, Pedersen (2017), "A Century of Evidence on Trend-Following Investing,"** *JPM* 44(1). Simulated back to 1880 (67 markets per secondary sources, CHECK). VERIFIED (AQR).
- **Kim, Tse, Wald, "Time Series Momentum and Volatility Scaling."** 55 futures 1985–2013: monthly alpha 1.27% with vol scaling vs 0.41% without; XSMOM 0.95%. *J. Financial Markets* 2016 (CHECK venue). VERIFIED via Quantpedia.
- **Baz, Granger, Harvey, Le Roux, Rattray (2015), "Dissecting Investment Strategies in the Cross Section and Time Series,"** Man AHL. TS momentum works, XS momentum poorly, carry both, best combined. SSRN 2695101 per Quantpedia (SSRN 403). SEARCH-LISTED.
- **Hamill, Rattray, van Hemert, "Trend Following: Equity and Bond Crisis Alpha,"** SSRN 2831926 (SEARCH-LISTED). 1960–2015; strong in the worst equity and bond environments.
- **Babu, Levine, Ooi, Schroeder, Stamelos (2020), "You Can't Always Trend When You Want,"** *JPM*. Post-GFC shortfall from muted market moves, not signal decay. VERIFIED.
- **Daniel & Moskowitz (2016), "Momentum Crashes,"** *JFE* 122(2): 221–247, DOI 10.1016/j.jfineco.2015.12.002. Crashes in panic states after declines with high vol; short side option-like; dynamic strategy roughly doubles Sharpe. VERIFIED.
- **Barroso & Santa-Clara (2015), "Momentum Has Its Moments,"** *JFE* 116(1): 111–120, DOI 10.1016/j.jfineco.2014.11.010. Managing momentum risk "virtually eliminates crashes and nearly doubles" Sharpe. VERIFIED.
- **Citation-only, VERIFIED on IDEAS:** Moreira & Muir (2017), "Volatility-Managed Portfolios," *JF* 72(4): 1611–1644; Asness, Moskowitz, Pedersen (2013), "Value and Momentum Everywhere," *JF* 68(3): 929–985; Kwan (1996), "Firm-specific information and the correlation between individual stocks and bonds," *JFE* 40(1): 63–80.
- **Koijen, Moskowitz, Pedersen, Vrugt (2018), "Carry,"** *JFE* 127(2): 197–225, DOI 10.1016/j.jfineco.2017.11.002. Carry predicts returns in equities, bonds, commodities, Treasuries, **credit**, options. VERIFIED.
- **Pitkäjärvi, Suominen, Vaittinen (2020), "Cross-asset signals and time series momentum,"** *JFE* 136(1): 63–85, DOI 10.1016/j.jfineco.2019.02.011. 20 countries; past bond returns predict equities positively, past equity returns predict government bonds negatively; cross-asset TSMOM Sharpe 45% higher; "slow-moving capital." VERIFIED.
- **Jostova, Nikolova, Philipov, Stahel (2013), "Momentum in Corporate Bond Returns,"** *RFS* 26(7): 1649–1693, DOI 10.1093/rfs/hht022. 81,491 bonds 1973–2011; 1991–2011 momentum 59 bp/month all bonds, 192 bp/month non-IG, 282 bp/month NIG bonds of private firms; not explained by risk, frictions, or equity momentum. VERIFIED. FDIC WP 2010-04 version: 77,150 bonds, 64 bp/month 1991–2008, 190 bp/month NIG, profits from winners, vanish after removing the worst-rated ~8%. VERIFIED PDF.
- **Gebhardt, Hvidkjaer, Swaminathan (2005), "Stock and bond market interaction: Does momentum spill over?"** *JFE* 75(3): 651–690. IG bonds reverse rather than trend at 3–12 months; equity momentum spills into same-firm bonds, stronger for lower-grade debt; underreaction to changing default risk. SEARCH-LISTED.
- **Haesen, Houweling, van Zundert (2017), "Momentum spillover from stocks to corporate bonds,"** *JBF* 79: 28–41, DOI 10.1016/j.jbankfin.2017.03.003. Firm-specific equity returns halve default-risk exposure, double Sharpe, cut bear→bull drawdowns. VERIFIED.
- **Bali, Subrahmanyam, Wen (2021), "Long-term reversals in the corporate bond market,"** *JFE* 139(2): 656–677, DOI 10.1016/j.jfineco.2020.08.007. 1977–2017; reversals strongest for high-credit-risk bonds and binding constraints; driven by long-term losers. VERIFIED. (Also lists Ho & Wang 2018 and Medhat & Schmeling 2022, TITLE-ONLY.)
- **Lee, Naranjo, Sirmans (2021), "CDS Momentum: Slow-Moving Credit Ratings and Cross-Market Spillovers,"** *RAPS* 11(2): 352–401, DOI 10.1093/rapstu/raaa025. CDS momentum ≈7.1%/yr; cross-market alphas ≈10.3%/yr in stocks, 7.3%/yr in bonds; strongest in liquid contracts ahead of slow rating changes. VERIFIED.
- **Hilscher, Pollet, Wilson (2015), "Are Credit Default Swaps a Sideshow?"** *JFQA* 50(3): 543–567, DOI 10.1017/S0022109015000228. Equity leads CDS daily and weekly; CDS reacts faster on salient news days. VERIFIED.
- **Norden & Weber (2009), "The Comovement of CDS, Bond and Stock Markets,"** *EFM* 15(3): 529–562. 2000–2002: stocks lead CDS and bond spreads; CDS leads bonds; stronger for lower-rated and US firms. VERIFIED.
- **Acharya & Johnson (2007), "Insider trading in credit derivatives,"** *JFE* 84(1): 110–141. Incremental information in CDS, bad news only, rising with bank relationships. VERIFIED.
- **Lee, Naranjo, Velioglu (2018), "When do CDS spreads lead?"** *JFE* 130(3): 556–578, DOI 10.1016/j.jfineco.2018.07.011. 3,470 S&P rating events 2001–2013; one-way CDS→bond flow, strongest for private entities; CDS returns predict idiosyncratic stock returns. VERIFIED.
- **Oehmke & Zawadowski (2017), "The Anatomy of the CDS Market,"** *RFS* 30(1): 80–119. Speculation concentrates in CDS; hedging links bond and CDS volumes. VERIFIED.
- **Collin-Dufresne, Junge, Trolle (2020), "Market Structure and Transaction Costs of Index CDSs,"** *JF* 75(5): 2719–2763, DOI 10.1111/jofi.12953. Two-tiered market persists; client trades large, infrequent, informed; dealers price-discriminate on expected impact. VERIFIED.
- **Dick-Nielsen, Feldhütter, Pedersen, Stolborg (2023), "Corporate Bond Factors: Replication Failures and a New Framework,"** SSRN 4586652 (per AQR page). Most factors fail to replicate; several equity signals work for bonds. Whether bond momentum survives: CHECK in the tables. VERIFIED (AQR).
- **Haynes & McPhail (CFTC OCE, June 2017), "The Liquidity of Credit Default Index Swap Networks."** Bloomberg SEF May 2014–Sep 2016: CDX IG ADV $7.05bn, 108 trades/day; peak $22.7bn (331 trades) 9 Feb 2016; price impact of CDX HY trades >$500mm ≈0.3 bp (≈0.5% of spread); dealer-to-dealer ≈15% of volume in IG/iTraxx, 8% in HY. VERIFIED PDF.
- **CFM (May 2015), "Trend Following: A Persistent Market Anomaly"** (from *J. Investment Strategies* 3: 41–61, 2014): two centuries, 100-day SMA, constant risk; Sharpe 0.72, "10 sigma"; CTA AUM $317bn at Q4 2014. VERIFIED PDF.

### 6.2 Industry research and practitioner evidence

- **SG Prime Services, "CTA Industry Update: Keeping Up with the Trend Followers" (May 2025).** SG Trend Index −4.9% in April 2025, −9.3% YTD; SG Short-Term Traders −0.9%/−0.9%; 2024 pairwise correlation among constituents 0.78 with ~15% return range; industry AUM ≈$340bn (BarclayHedge Q4 2024); Trend Indicator = 20d/120d MA crossover; since 2007 the Trend Index "behaves more like a much slower model"; faster models "delivered the best hypothetical returns" in 2020. Quotable: CTAs show "a level of adaptability akin to the Kardashians." VERIFIED PDF.
- **Cambridge Associates (Aug 2025).** SG Trend +20.9% in 2008 (MSCI ACWI −42.2%), +27.4% in 2022 (ACWI −18.4%); −20.4% May 2024–May 2025, second-largest drawdown since 2000; 16 drawdowns >10% since 2000. VERIFIED.
- **Kaminski & Wen, AlphaSimplex (June 2025), "Market Cycles and Managed Futures Drawdowns."** SG Trend drawdowns >10%: "Liberation day" −21.8% (15 Apr 2024–14 May 2025); "Trade War 1.0" −23.0% (2015–2019); "GFC Recovery" −11.3% from 9 Mar 2009; "Fed Inflation Fight Reversal" −10.1% (14 Jun–10 Aug 2022); "SVB" −15.4% (20 Oct 2022–17 Mar 2023); "2008 Commodity Collapse" −10.7% (Jul–Sep 2008). VERIFIED PDF.
- **Man Group, Korgaonkar (mid-2025), "Trend Following and Drawdowns: Is This Time Different?"** SG Trend 12-month return to 30 Apr 2025 −18.6% (below −15% only twice before); trend repositioned after the 2 April tariff shock and was positive by 9 April. VERIFIED.
- **Man Group, Georgiades, Wong, Abou Zeid, "A Trend Following Deep Dive: The Dynamics of Dispersion" (data to Dec 2024).** Best-to-worst SG Trend constituent gap ~10 pp/yr; pairwise correlation fell from 0.87 (pre-2007) to 0.78; adding alternative markets "such as power, synthetic credit indices and interest rate swaps" improved performance, more for slower systems. VERIFIED.
- **Man Institute, Robertson (May 2023), "Trend-Following: What's Not to Like?"** BTOP50 since 1986: 7.0% annualized vs 7.7% world stocks, vol 9.6% vs 14.4%, max DD −16.1% vs −50.4%; +17% in the credit crisis (Jul 2007–Feb 2009), −2% COVID (Feb–Mar 2020), +19% Jan–Sep 2022; flat 2009–2019; "typically 3–6 months" to find a new trend. VERIFIED PDF.
- **Fidelity, Croce, Hazrachoudhury, Carton (data to Dec 2025), "Trend-following crisis alpha: Does it come from beta timing or market selection?"** SG Trend excess return 4.2%/yr, vol 13.4%, Sharpe 0.31; correlation to S&P −0.11, −0.31 in down months; strong in 2000, 2007, 2022; "did not contribute positively" in COVID 2020 or Q4 2018; 76% of simple-trend risk is beta timing. VERIFIED PDF.
- **Hedge Fund Journal (2013), "AHL Evolution."** Credit was the programme's first asset class (2005); exposure via selling protection on CDX and iTraxx, able to flip to buying protection; short credit in 2008; corporate credit and EM debt "produced more persistent trends than most other asset classes"; fixed income the bulk of 2012's 23.6%. VERIFIED. HFJ (Nov/Dec 2017): Man AHL ~600 markets, 25–50 new per year. VERIFIED.

### 6.3 The venue: index CDS market data 2021–2026

- **ISDA Research Note (29 July 2026), "CDS Market Dynamics: Five Years of Activity and a Record 2025."** Total CDS activity $41.8tn in 2025 (prior peak $38.7tn in 2022; $31.4tn 2023); index 93.3%, record $39.0tn ($36.4tn 2022; $28.1tn 2023); single-name peak $3.3tn 2023, $2.8tn 2025; index/single-name ratio 15.7× (2022), 8.5× (2023), 13.8× (2025); 2025 index shares: CDX.NA.IG 43.4%, iTraxx Europe 32.4%, CDX.NA.HY 10.4%, iTraxx Crossover 7.7%; average IG index trade ≈$90mm vs ≈$25mm HY; CDX.NA.IG 500–900 trades/day (>900 in Q2 2025); Q1 2020 index +78.1% vs trailing average (single-name +16.1%); Q1 2023 single-name +84.8% (index +4.5%); Q2 2025 index +20.9%, single-name −20.7%; rolls ~March 20 and September 20, roll window 25–50% of quarterly notional; H1 2026 total $27.4tn (+27.8% YoY). VERIFIED.
- **ISDA SwapsInfo H1 2025.** Index credit derivatives +91.9% to $10.5tn (partly a reporting-threshold change from Oct 2024); CDX IG $4.0tn (+111.1%), CDX HY $1.2tn (+44.5%), iTraxx Europe $2.3tn (+73.7%); >99% of the three benchmarks cleared; SEF share 98.0% IG, 97.6% HY, 96.5% iTraxx Europe; corporate single-name $257.1bn (−1.2%). VERIFIED PDF.
- **Clarus (10 June 2026).** Cleared USD CDX $3.94tn in March 2026 (+46% YoY); SDR-reported CDX $2.18tn (IG $1.67tn, HY $407bn, EM $70.8bn); cleared EUR iTraxx $2.97tn (+51%); cleared CDX swaptions $52.9bn (+80%); iTraxx swaptions +133%; ICE ≈91% of cleared USD credit in Q1 2026. VERIFIED.
- **LCH CDSClear Q3 2025.** Record $198bn of CDX and iTraxx cleared in one day (22 Sep 2025, +110% vs the Sep 2024 roll); client index roll volume +66% YoY; record €7.025tn cleared Sep 2025 YTD vs €5,437bn in all of 2024. VERIFIED PDF.
- **ECB FSR (Dec 2006):** iTraxx launched summer 2004, 125 names, semiannual roll. VERIFIED (history).

### 6.4 Spread levels for the crisis windows

- **FRED, ICE BofA US HY OAS (`BAMLH0A0HYM2`), verified daily Oct 2023–Oct 2026:** 2.62% (18 Feb 2025); 3.42% (2 Apr); **4.61% (7 Apr 2025, 2025 high)**; 4.57% (8 Apr); 4.37% (9 Apr); 3.31% (30 May); 2.81% (31 Dec 2025); 2026 high 3.46% (30 Mar 2026); 3.23% (15 Oct 2026); 2024 high 3.93% (5 Aug 2024); late-2023 high 4.53% (27 Oct 2023). **IG OAS (`BAMLC0A0CM`):** 2025 high 1.21% (9 Apr 2025); 2026 high 0.94% (16 Mar 2026); 0.84% (15 Oct 2026). Full history before Oct 2023 could not be pulled through the proxy; the chapter code should fetch it.
- **2008:** US HY OAS record roughly 2,000 bp in Nov/Dec 2008 (secondary sources disagree on date; CHECK on FRED). Sourced alternative: Dynkin Table 3.9 averages for 2008: HY index 899 bp, CDX HY 788 bp; 2009: 991 vs 950 (`p.216`). Cash-CDS basis very negative (`Ben_Dor p.390`).
- **2020:** HY OAS peak ≈1,100 bp around 23 March 2020 (secondary; CHECK). CDX HY/IG peaks: CHECK.
- **2022:** HY OAS peak ≈600 bp in July 2022 (secondary; CHECK). Index CDS activity $36.4tn record that year (ISDA).
- **2023 (SVB):** single-name CDS activity +84.8% in Q1 2023 (ISDA); spread peak CHECK.

---

## 7. Case studies

**A — 2008–2009: the trend that paid and the rebound that charged.** SG Trend +20.9% in 2008 (Cambridge Associates); BTOP50 +17% Jul 2007–Feb 2009 vs world stocks −49% (Man 2023); AHL Evolution short credit via index protection (HFJ 2013); EMC +35.4% in Mar 2007–Nov 2008 vs IG index −24.2% (`Dynkin p.618`); 2008 average CDX HY 788 bp vs cash HY 899 bp (`Dynkin p.216`), basis "very negative" (`Ben_Dor p.390`). Then the "GFC Recovery" drawdown −11.3% from 9 Mar 2009 (AlphaSimplex) and momentum's short-side crash (`Paleologo p.77`; Daniel–Moskowitz). Lesson: right for 20 months, wrong for the two that cost the most; the exit rule is the strategy.

**B — February–June 2020: the V that trend could not trade.** Index CDS activity +78.1% vs trailing average in Q1 2020 (ISDA); HY bid-ask gapped then normalized (`Man_Quantitative p.20`); BTOP50 −2% Feb–Mar 2020 (Man 2023); SG Trend "did not contribute positively" (Fidelity); faster models best in 2020 (SG). HY OAS ≈1,100 bp late March (CHECK). Lesson via D6: $T\approx2$ months is shorter than most trend lags; the Fed facilities are the $\kappa$ shock; the only trend that paid was fast, and fast is expensive in cash credit but not in CDX.

**C — 2022: the slow grind, trend's best year, and a reversal inside it.** SG Trend +27.4% (Cambridge Associates); BTOP50 +19% Jan–Sep 2022 (Man 2023); "Fed Inflation Fight Reversal" −10.1% drawdown 14 Jun–10 Aug 2022 (AlphaSimplex); index CDS record $36.4tn (ISDA); short duration and short spread both trended; EMC historically weaker in tightening (`Dynkin p.620`). HY OAS ≈600 bp July 2022 (CHECK). Lesson: convexity at the 9-month horizon and whipsaw at the 2-month one, in the same year.

**Coda — April 2025 "Liberation Day" (FRED-verified).** HY OAS 2.62% (18 Feb) → 3.42% (2 Apr) → 4.61% (7 Apr) → 3.31% (30 May); IG OAS peak 1.21% (9 Apr). SG Trend −4.9% April, −9.3% YTD (SG); 12-month return to 30 Apr −18.6% (Man); −21.8% drawdown Apr 2024–May 2025 (AlphaSimplex); index CDS activity +20.9% vs trailing average, single-name −20.7% (ISDA); trend repositioned and positive by 9 April per Man. Present the sources together, not as a verdict.

---

## 8. Humor beats (canon cast; each rides on a correct idea)

1. **Kaz vs legal vocabulary:** Kaz hears "iTraxx Crossover" and starts drafting a cross-default clause. Ines: "It's 75 sub-investment-grade names, Kaz. The only thing it crosses is your P&L in March." (Crossover is the European HY index, not a covenant.)
2. **Mags, back in my day:** "We had trend-following in credit. It was called 'Sal stopped picking up.'" Grudging respect for a 60-day EWMA that at least returns calls. (Dealer withdrawal was the original trend signal.)
3. **ROBO literalism:** Vague spec: "Follow the trend and don't get whipsawed." What ROBO built: a strategy that trades once a decade and was short CDX HY at 100% of risk on 24 March 2020. (Speed is a parameter, not a vibe.)
4. **The 13-week model, reborn:** Theo's 13-week model is a 65-trading-day lookback, within rounding of MOP's 60-day vol window. (13 weeks is a liquidity horizon, not a trend horizon; the chapter says why.)
5. **Ines, Poker Table:** "Who at this table knows more than you? In credit, the equity market, by about a week. Trend-following is sitting to its left and calling." (Hilscher et al.; EMC.)
6. **IDO or it didn't happen:** Fidelity finds 76% of trend risk is beta timing. "Trend is beta that changed its mind. It is still beta. Strip it before you call it alpha."
7. **On the 83% decay (`Dynkin p.610`):** "An equity momentum signal has the half-life of an ad hoc group: by the time counsel is retained, the top decile has left the building."
8. **Desk Myth vs Desk Reality:** Myth: a credit trend follower has a view on spreads. Reality: half its P&L is a view on volatility, and credit volatility is spread times duration, so the position is sized by the thing it is forecasting. Kaz: "Let's just assume Gaussian." Everyone: "No."
9. **The Kardashian line (real, SG May 2025):** CTAs "showcase a level of adaptability akin to the Kardashians." Trend Watch epigraph; managers run many speeds at once.
10. **"Open market purchase":** A long-protection trend position is not an open market purchase of anyone's bonds; it is a bet that dealers who quote CDX IG 900 times a day keep doing so. In 2020 they did (ISDA +78%); the cash market did not (`Man_Quantitative p.20`).

---

## 9. Resource-graph candidates

**VERIFIED-URL (fetched this session)**
- IDEAS: MOP 2012 `https://ideas.repec.org/a/eee/jfinec/v104y2012i2p228-250.html`; Koijen et al. 2018 `https://ideas.repec.org/a/eee/jfinec/v127y2018i2p197-225.html`; Pitkäjärvi et al. 2020 `https://ideas.repec.org/a/eee/jfinec/v136y2020i1p63-85.html`; Barroso–Santa-Clara 2015 `https://ideas.repec.org/a/eee/jfinec/v116y2015i1p111-120.html`; Daniel–Moskowitz 2016 `https://ideas.repec.org/a/eee/jfinec/v122y2016i2p221-247.html`; Acharya–Johnson 2007 `https://ideas.repec.org/a/eee/jfinec/v84y2007i1p110-141.html`; Haesen et al. 2017 `https://ideas.repec.org/a/eee/jbfina/v79y2017icp28-41.html`; Lee–Naranjo–Velioglu 2018 `https://ideas.repec.org/a/eee/jfinec/v130y2018i3p556-578.html`; Bali et al. 2021 `https://ideas.repec.org/a/eee/jfinec/v139y2021i2p656-677.html`; Oehmke–Zawadowski 2017 `https://ideas.repec.org/a/oup/rfinst/v30y2017i1p80-119..html`; Collin-Dufresne et al. 2020 `https://ideas.repec.org/a/bla/jfinan/v75y2020i5p2719-2763.html`; Jostova et al. 2013 `https://ideas.repec.org/a/oup/rfinst/v26y2013i7p1649-1693.html`; Lee–Naranjo–Sirmans 2021 `https://ideas.repec.org/a/oup/rasset/v11y2021i2p352-401..html`; Norden–Weber 2009 `https://ideas.repec.org/a/bla/eufman/v15y2009i3p529-562.html`; Moreira–Muir 2017 `https://ideas.repec.org/a/bla/jfinan/v72y2017i4p1611-1644.html`; Kwan 1996 `https://ideas.repec.org/a/eee/jfinec/v40y1996i1p63-80.html`; Asness–Moskowitz–Pedersen 2013 `https://ideas.repec.org/a/bla/jfinan/v68y2013i3p929-985.html`.
- Hilscher–Pollet–Wilson 2015 `https://www.cambridge.org/core/journals/journal-of-financial-and-quantitative-analysis/article/abs/are-credit-default-swaps-a-sideshow-evidence-that-information-flows-from-equity-to-cds-markets/F7CCD2FFB20AAEACE1E093D12EEF7A31`.
- AQR: `https://www.aqr.com/Insights/Research/Journal-Article/A-Century-of-Evidence-on-Trend-Following-Investing`; `https://www.aqr.com/Insights/Research/Journal-Article/You-Cant-Always-Trend-When-You-Want`; `https://www.aqr.com/Insights/Research/Working-Paper/Corporate-Bond-Factors-Replication-Failures-and-a-New-Framework` (SSRN 4586652 listed there).
- Man Group: `https://www.man.com/insights/deep-dive-trend-following`; `https://www.man.com/insights/is-this-time-different`; Robertson 2023 PDF (hosted copy) `https://americanbeaconfunds.com/wp-content/uploads/2025/08/Trend-Following-Whats-Not-to-Like_AHL-TREND-WP-1.pdf`.
- Cambridge Associates `https://www.cambridgeassociates.com/insight/does-trend-followings-recent-struggle-signal-that-the-strategy-is-structurally-broken/`; AlphaSimplex `https://www.alphasimplex.com/assets/files/2025.06---market-cycles-and-managed-futures---kaminski-and-wen.pdf`; SG `https://content.sgmarkets.com/CTA_UPDATE_KEEPING_UP_WITH_THE_TRENDFOLLOWERS_2025`; Fidelity `https://institutional.fidelity.com/app/proxy/content?literatureURL=%2F9922231.PDF`.
- ISDA `https://www.isda.org/2026/07/29/cds-market-dynamics-five-years-of-activity-and-a-record-2025/`, PDF `https://www.isda.org/a/Pa0iE/CDS-Market-Dynamics-Five-Years-of-Activity-and-a-Record-2025.pdf`, SwapsInfo H1 2025 `https://www.isda.org/a/4cpgE/SwapsInfo-First-Half-of-2025-and-the-Second-Quarter-of-2025.pdf`, weekly `https://analysis.swapsinfo.org/2025/06/interest-rate-and-credit-derivatives-weekly-trading-volume-week-ending-june-20-2025/`; Clarus `https://www.clarusft.com/us-firms-powered-march-2026-itraxx-swaps-volume-growth/`; LCH `https://www.lseg.com/content/dam/post-trade/en_us/documents/lch/resources/cdsclear-dashboard-q3-2025.pdf`.
- CFTC `https://www.cftc.gov/sites/default/files/idc/groups/public/@economicanalysis/documents/file/oce_credit_swap_liquidity.pdf`; FDIC `https://www.fdic.gov/analysis/cfr/working-papers/2010/2010-04.pdf`; CFM `https://www.cfm.com/wp-content/uploads/2022/12/298-2015-CFM-Trend-Following-a-Persistent-Market-Anomaly.pdf`; ECB `https://www.ecb.europa.eu/pub/pdf/fsr/art/ecb.fsrart200612_02.en.pdf`; Quantpedia `https://quantpedia.com/deconstructing-the-time-series-momentum-strategy/`; Hedge Fund Journal `https://thehedgefundjournal.com/ahl-evolution/`, `https://thehedgefundjournal.com/man-ahl-marks-30-years/`.
- Podcasts: Top Traders Unplugged, Systematic Investor ep. 422, Katy Kaminski (17 Oct 2026) `https://www.toptradersunplugged.com/podcast/why-trend-following-rewards-patience-ft-katy-kaminski/`; ep. 153, Patrick Welton (30 Sep 2026) `https://www.toptradersunplugged.com/podcast/why-investors-keep-getting-trend-following-wrong-ft-patrick-welton/`; Flirting with Models S7E19, Jeff Rosenberg on systematic fixed income (18 Aug 2025) `https://www.flirtingwithmodels.com/episodes/8V74zBaN4jN`; S7E25, Takahe Capital on trend-following spreads (12 Jan 2026) `https://www.flirtingwithmodels.com/episodes/1iIqmQ7piJd`.
- Data: `https://fred.stlouisfed.org/series/BAMLH0A0HYM2`, `https://fred.stlouisfed.org/series/BAMLC0A0CM`.

**SEARCH-LISTED (cite title and authors; link optional with a flag):** Hamill, Rattray, van Hemert (SSRN 2831926); Baz et al. 2015 (SSRN 2695101); Gebhardt et al. 2005; Fung & Hsieh 2001, "The Risk in Hedge Fund Strategies: Theory and Evidence from Trend Followers" (*RFS*); Pu et al., "Network Momentum across Asset Classes" (arXiv 2308.11294).

**TITLE-ONLY:** Baltas & Kosowski, "Demystifying Time-Series Momentum Strategies"; Israel, Palhares, Richardson (2018), "Common Factors in Corporate Bond Returns," *JIM*; Houweling & van Zundert (2017), *FAJ*; Brooks, Palhares, Richardson (2018), "Style Investing in Fixed Income," *JPM*; Greyserman & Kaminski (2014), *Trend Following with Managed Futures*; Robertson & Goodall (2023), "Trend-Following: A Different Point of Skew"; Kaminski (2025), "Themes of 2024: Slow and Steady Wins the Race"; Naik, Trinh, Rennison (2002); Lin, Wang, Wu (2013); Khang & King (2004); Pospisil & Zhang (2010); Ho & Wang (2018); Medhat & Schmeling (2022). Bloomberg *Odd Lots*: no episode verified this session; name the show only.

---

## 10. Exploratory-space notes

1. **Ch 10-B: Credit index microstructure for systematic traders.** Rolls (25–50% of quarterly notional in the roll window; LCH's $198bn day), index skew vs intrinsic, series basis, swaptions growing faster than indices (Clarus), dealer price discrimination (Collin-Dufresne et al.). A roll-adjusted return series is unspecified anywhere on the shelf.
2. **Speed as a regime variable.** SG: CTAs slowed after 2007 yet fast models won in 2020 and 2025. Multi-speed ensembles and short-term CTA strategies in credit with explicit cost curves (fast trend is uneconomic in cash, possibly not in CDX).
3. **Trend convexity via swaptions.** Payer swaptions as the short-credit leg; break-even vol vs trend lag (Ch 23 or 10-C).
4. **Cross-asset lead–lag networks.** Extend Pitkäjärvi et al. and Lee–Naranjo–Sirmans to equity → CDS → bonds → loans, with Ch 25 news-timing features (Hilscher's salient-news result).
5. **Rating momentum as fundamental trend.** Schmid's non-Markov transitions and the "slow-moving ratings" channel: predicting rating drift and its P&L (Ch 11 or 14).
6. **Trend in the LMT era.** Survival-adjusted single-name trend where the jump is a liability-management event; link to the Priming Risk Score (Ch 13) and post-LMT re-default rates (Ch 14).
7. **Replication risk in bond momentum.** Apply Dick-Nielsen et al.'s framework to momentum in Edition 2; read the tables.
8. **Flows, slow-moving capital and trend.** Fund flows, ETF creations (Ch 20) and dealer inventories as the mechanism; connect to `Ben_Dor p.292`'s "destabilizing behavior."
9. **Exchange-traded credit futures.** CME's Bloomberg corporate index futures (CHECK launch dates, open interest, CTA adoption) for Appendix C and Ch 22.
10. **Private credit marks and spurious momentum.** Smoothed BDC/private marks create untradable serial correlation (Ch 17 box).
11. **Appendix C Trend Tracker entries from this brief:** every dated figure in §6.3 and §6.4, plus CTA AUM ≈$340bn (flat vs $317bn in 2014), SG Trend 2008 +20.9% and 2022 +27.4%, the 2024–25 drawdown (−20.4%/−21.8%), CTAs slower and more dispersed since 2007, and synthetic credit indices as a standard "alternative market."

<!-- STATUS: COMPLETE -->
