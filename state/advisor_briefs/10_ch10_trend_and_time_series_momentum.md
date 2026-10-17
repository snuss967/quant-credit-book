# Advisor Brief — Chapter 10: Trend-Following & Time-Series Momentum in Credit (TREND)

**Target file:** `book_src/10_ch10_trend_and_time_series_momentum.md` (7,000–10,000 words)
**Advisor:** Fable, Edition 1 editorial board. Research date: 2026-10-17.
**Status key:** VERIFIED = fetched or read this session; SEARCH-LISTED = URL appeared in a search result but the page was not fetched; CHECK = plausible but unconfirmed, do not state as fact without a source.

---

## 1. Thesis and the "aha" for the ex-PJT-RSSG reader

**Thesis.** Trend-following in credit is not a different religion from the RSSG seat; it is the stop-loss the reader has been running by hand for years, written down, sized by DTS, and executed in the one credit instrument that actually trades like a future: the on-the-run CDX/iTraxx index. Everything that makes trend hard in credit (negative skew of long credit, spread-level-dependent volatility, stale cash prices, jumps from LMTs and defaults, a V-shaped Fed put) is a direct consequence of credit's payoff shape, and every one of those consequences is derivable.

**Three "aha" moments to build the chapter around:**

1. **Volatility scaling in credit *is* DTS scaling.** Ben Dor et al. show spread volatility is linear in spread level with a zero intercept (`Ben_Dor p.74`). Therefore $\sigma(r^{ex}) \approx D^{\text{spr}} \cdot \beta s = \beta \cdot \text{DTS}$, and the Moskowitz–Ooi–Pedersen position $w_t = \sigma_{\text{tgt}}/\sigma_t$ becomes $w_t \propto 1/\text{DTS}_t$. A credit trend follower automatically de-risks as spreads widen and re-risks as they tighten. That is the same mechanical behavior as a rating-based or DTS-based stop-loss, which Ben Dor warns "does well in trending markets and poorly in choppy markets" and can feed "a vicious cycle" (`Ben_Dor p.292`). The reader's old job was to be on the other side of that cycle (buying fallen angels from forced sellers, `Dynkin` Chs 2–3). Now they are specifying the seller. Kim–Tse–Wald's critique that much of TSMOM's alpha comes from vol scaling rather than the sign (Quantpedia summary, VERIFIED) lands with special force in credit.

2. **Carry and trend disagree exactly when it matters.** Under a spread process with both mean reversion and short-run inertia, $\Delta s_{t+1} = \kappa(\bar s - s_t) + \phi\,\Delta s_t + \epsilon_{t+1}$, expected excess return is $s_t\Delta t - D^{\text{spr}}[\kappa(\bar s - s_t) + \phi\Delta s_t]$. The carry/value term ($s_t$, $\kappa$) says buy after widening; the trend term ($\phi$) says sell. 2008 and 2022 were $\phi$-years; March 2020 and April 2025 were $\kappa$-weeks. The chapter's job is to let the reader see both coefficients and size them, not to pick a tribe. Man 2022 says it plainly: carry "can have fantastic years and also very poor years" (`Man_Quantitative p.26`).

3. **Equity leads credit, so the best credit trend signal is often not a credit price.** Hilscher–Pollet–Wilson (JFQA 2015, VERIFIED) find equity returns lead CDS at daily and weekly horizons, not the reverse; Dynkin's Equity Momentum in Credit (EMC) earns 6.34%/yr (IR 1.56) in IG and 15.9%/yr in HY before costs, with an 83% chance the top-decile signal decays within three months (`Dynkin pp.607, 610, 628`). The RSSG reader already watches the equity for the companies whose debt they trade; this chapter turns that reflex into a specification.

**The PJT bridge in one line:** a restructuring banker knows that a bond at 60 "has momentum" toward a process, not toward 40 or 80. Trend-following formalizes the first half of that sentence and is silent on the second; the chapter must show where the jump (the LMT, the filing, the DIP) breaks the diffusion assumption and how to specify a trend engine that knows it.

---

## 2. Section outline (10.1 … 10.10), anatomy mapping, Trend Watch boxes

Anatomy legend: **DF** desk framing · **DER** derivation · **SPEC** AI-coder spec · **SRC** source extraction · **CASE** case study · **RG** resource graph · **TW** Trend Watch.

**Cold open (≤400 words).** Theo, three weeks in, is asked by Ines to explain why the desk's CDX HY position flipped from long risk to long protection at 4:02 p.m. the day after the tariff announcement and whether "the model is panicking." Kaz says the model cannot panic because it has no amygdala, only a 60-day EWMA. Mags says it looks like 2008 to her and nothing like 2008 to her at the same time. Question the chapter answers: *when is a move in spreads information about the next move in spreads, and how much should you bet on it?*

- **10.1 What a trend is, in credit (DF, DER, SRC).** Trend vs cross-sectional momentum (`Paleologo p.74`). Instruments: CDX IG/HY, iTraxx Main/Crossover, cash index excess returns, HYG/LQD. Why index CDS is the futures-like leg (ISDA volumes, below). Sign conventions: spread up = price down; "long risk" = sold protection. **TW #1: The index CDS market as the trend follower's venue (2021–2026).**
- **10.2 The TSMOM engine, adapted (DER, SPEC).** Moskowitz–Ooi–Pedersen signal, vol targeting, lookbacks; translation of futures excess return to CDS carry-plus-spread-change return; CDX HY price-quoted vs IG spread-quoted; series rolls and splicing. Derivation 1 and 2 below.
- **10.3 Why vol scaling in credit is DTS scaling (DER, SRC, Ways This Blows Up).** Ben Dor linear vol-spread law; Kim–Tse–Wald; the stop-loss feedback loop (`Ben_Dor p.292`, `Dynkin p.397`). Box: *Desk Myth vs Desk Reality* ("trend is a view on direction" vs "half of it is a view on volatility").
- **10.4 Trend plus carry (DER, SRC, SPEC).** OU-with-inertia model; Koijen et al. carry definition; Baz et al. finding that TS momentum and carry combine best; Man 2022 on carry's volatility. Derivation 3.
- **10.5 Cross-asset trend: equity → credit lead–lag (DER, SRC, CASE-lite).** Hilscher et al.; Norden–Weber; Acharya–Johnson (the CDS-leads exception: bad news, bank-relationship names); Lee–Naranjo–Velioglu (CDS leads bonds, especially private issuers); Lee–Naranjo–Sirmans CDS momentum 7.1%/yr with cross-market spillovers; Dynkin EMC construction, decay table, sector timing (5–8 bp per 1%/m equity momentum, `Dynkin p.644`); Haesen et al. residual momentum halves default-risk exposure. Pitkäjärvi et al. cross-asset TSMOM (bond→equity positive, equity→bond negative, government bonds) as the template. Derivation 4.
- **10.6 Crisis alpha and the shape of the payoff (DER, SRC, CASE).** Trend as a long straddle on the 12-month move; the quadratic regression; Daniel–Moskowitz momentum crashes (short side, panic states); Paleologo's Merton explanation of the 2009 short-side squeeze (`Paleologo p.77`); Fidelity decomposition (76% of trend risk is beta timing). Credit-specific: negative skew of long credit means the short-credit leg of trend is the convex one. **TW #2: CTAs, speed and the 2024–2025 drawdown.**
- **10.7 Case studies: 2008, 2020, 2022 (CASE, SRC).** See §7. Add April 2025 as a coda ("Liberation Day") with FRED-verified spreads.
- **10.8 Turnover, costs and capacity (DER, SRC, SPEC).** Sign-flip turnover; EWMA crossovers; Man 2022 on momentum turnover (`p.19`); CDX cost facts (CFTC 2017: ~0.3 bp price impact on >$500mm CDX HY; Collin-Dufresne–Junge–Trolle two-tier market); cash LCS; break-even math.
- **10.9 Trend in the LMT era: jumps, not diffusions (DF, DER, Docket Diary-lite).** Why single-name trend is exposed to gap risk the index is not; survival-adjusted signals; cross-reference Ch 13–14. Schmid's rating momentum (`Schmid p.48`) as the fundamental analogue of price trend: non-Markov transitions.
- **10.10 Desk Debrief, The Spec You Hand the Robot, exercises.**

Minimum two Trend Watch boxes (TW #1 in 10.1, TW #2 in 10.6); a third candidate, "CTAs slowed down after 2007" (SG heat-map finding), fits 10.8.

---

## 3. Derivation skeletons

All signal construction and performance statistics are under $\mathbb{P}$. The only $\mathbb{Q}$ object is the CDS risky annuity used to convert spread changes to P&L; say so explicitly in the chapter.

### D1. TSMOM signal and position (Moskowitz–Ooi–Pedersen 2012, adapted)

Lookback-$h$ sign signal on instrument $i$ with excess return $r^{ex}_{i,t}$:
$$
\text{sig}^{(h)}_{i,t} = \operatorname{sign}\!\Big(\textstyle\sum_{k=0}^{h-1} r^{ex}_{i,t-k}\Big), \qquad
w_{i,t} = \frac{\sigma_{\text{tgt}}}{\hat\sigma_{i,t}}\,\text{sig}^{(h)}_{i,t}, \qquad
r^{\text{TSMOM}}_{t+1} = \frac{1}{N}\sum_{i=1}^{N} w_{i,t}\, r^{ex}_{i,t+1}.
$$
$\hat\sigma_{i,t}$ is an exponentially weighted annualized volatility; MOP use a 60-day center of mass and $\sigma_{\text{tgt}}=40\%$ per instrument (state as their choice, not a law). Smoother alternative: EWMA crossover $\text{sig}_t = \tanh\!\big((\text{EWMA}_{f}(P_t)-\text{EWMA}_{s}(P_t))/(\hat\sigma_t\sqrt{h})\big)$, with SG's 20d/120d crossover as the industry's "Trend Indicator" benchmark (SG note, May 2025, VERIFIED).

**Credit excess return.** For a funded long-risk position in an index CDS with running coupon $c$ (100 bp IG, 500 bp HY by convention; CHECK current contract terms before stating), par spread $s_t$ and risky annuity $A_t$ (RPV01, a $\mathbb{Q}$ quantity from the ISDA standard model):
$$
r^{ex}_{t+1} \;\approx\; \underbrace{s_t\,\Delta t}_{\text{carry}} \;-\; \underbrace{A_t\,(s_{t+1}-s_t)}_{\text{mark-to-market}} \;+\; \underbrace{\tfrac12\,\Gamma_t (s_{t+1}-s_t)^2}_{\text{convexity}},
$$
and for a cash index, $r^{ex}_{t+1} \approx s_t\Delta t - D^{\text{spr}}_t\,\Delta s_{t+1}$ over duration-matched Treasuries (Dynkin's data definition, `p.605`). **Error-prone spots:** (i) the sign of the mark-to-market term; (ii) CDX HY is price-quoted, so build the return from price plus accrued coupon, not from a converted spread; (iii) upfront vs running conventions on the roll; (iv) splicing on-the-run series at the semiannual roll (roll notional is 25–50% of a quarter's volume per ISDA footnote 8) creates artificial returns if you difference across series; (v) ACT/360 accrual for $\Delta t$; (vi) do not feed index OAS levels into a sign rule without converting to returns, because a 12-month *level* comparison and a 12-month *return* sum differ by carry, which has the opposite sign of the spread move.

### D2. Volatility scaling in credit is DTS scaling

Ben Dor's spread-volatility law: $\sigma(\Delta s_i) = \alpha + \beta\, s_i$ with $\alpha \approx 0$ (`Ben_Dor p.74`). With $\sigma(r^{ex}_i) \approx D^{\text{spr}}_i\,\sigma(\Delta s_i)$:
$$
\sigma(r^{ex}_{i,t}) \approx \beta\, D^{\text{spr}}_{i,t}\, s_{i,t} = \beta\,\text{DTS}_{i,t}
\quad\Longrightarrow\quad
w_{i,t} = \frac{\sigma_{\text{tgt}}}{\beta\,\text{DTS}_{i,t}}\,\text{sig}_{i,t}.
$$
Consequences to derive and state: position in spread-DV01 terms is constant *per unit of spread*, so dollar notional shrinks as spreads widen; realized trend P&L decomposes into a "sign" component and a "vol-timing" component (Kim–Tse–Wald: 1.27% vs 0.41% monthly alpha with and without scaling on 55 futures, 1985–2013, Quantpedia summary). Assumptions: $\beta$ stable within rating bucket; Ben Dor's $\gamma$ nonlinearity at low spreads (vol roughly constant below ~20 bp) breaks the proportionality for tight IG. **Measure:** $\mathbb{P}$. **Ways This Blows Up:** vol estimated from stale cash prices is biased low (then the position is too big); Paleologo's dispersion result (`p.98`) shows vol scaling is most dangerous when the universe's volatilities are heterogeneous, which is exactly a cross-rating credit book.

### D3. Trend plus carry under an OU-with-inertia spread process

Model the (log or level) spread as
$$
\Delta s_{t+1} = \kappa(\bar s - s_t) + \phi\,\Delta s_t + \epsilon_{t+1}, \qquad \epsilon_{t+1}\sim(0,\,\beta^2 s_t^2\Delta t)\ \text{under }\mathbb{P}.
$$
Then
$$
\mathbb{E}_t[r^{ex}_{t+1}] = s_t\Delta t - D^{\text{spr}}\big[\kappa(\bar s - s_t) + \phi\,\Delta s_t\big].
$$
Carry ($s_t\Delta t$) and value ($-D\kappa(\bar s - s_t)$, positive when $s_t > \bar s$) favor buying wide spreads; trend ($-D\phi\Delta s_t$) favors selling after widening when $\phi>0$. The optimal linear combination weights each predictor by its coefficient over its forecast variance; show that with $\phi$ small and $\kappa$ small, carry dominates at monthly horizon, and with $\phi$ large (2008, 2022) trend dominates. Koijen et al. (JFE 2018, VERIFIED) define carry as the return if prices do not change and find it predicts returns in credit among other classes; Baz et al. (Man AHL 2015, Quantpedia summary) find time-series momentum and carry are complementary and best combined. **Error-prone:** estimating $\kappa$ and $\phi$ jointly on monthly OAS with a 25-year sample gives standard errors as large as the coefficients; the book should say so and show the confidence region rather than a point estimate. Also, Nuveen's house assumption that "spreads tend to mean revert" (`Nuveen p.4`) is a prior on $\kappa$, not evidence against $\phi$.

### D4. Equity → credit lead–lag

Predictive regression at issuer or index level:
$$
r^{\text{cr}}_{t+1} = a + b\, r^{\text{eq}}_{t} + c\, r^{\text{cr}}_{t} + \varepsilon_{t+1},
$$
with Granger tests in a VAR(1). Dynkin's EMC signal: equal-weighted 1-, 3- and 6-month equity returns "rescaled for different lengths of the respective formation periods" (`p.606`, footnote 9; the exact rescaling is not on the page, CHECK the appendix; propose dividing each horizon's return by $\sqrt{h}$ as the vol-neutral default). Sector translation: $\approx$ 5–8 bp/month of excess return per 1%/month of equity momentum (`Dynkin p.644`). **Error-prone:** stale bond prices manufacture a spurious lead (Dynkin tests this by sorting on Trade Efficiency Scores, `p.621`, and by lagging the signal 1–3 days, `p.630`); non-synchronous closes between US equity and European CDS; the credit exposure of a momentum long–short flips sign across the cycle (`p.613`), so a "lead–lag alpha" that is not beta-neutralized is mostly timing. Haesen et al. (JBF 2017, VERIFIED): ranking on firm-specific rather than total equity returns roughly halves default-risk exposure and doubles the Sharpe ratio; Dynkin finds the opposite in their sample (`p.631`). Put both on the page; it is a real disagreement.

### D5. Crisis alpha as convexity

Regress trend returns on index returns and their square over the horizon the trend is designed for:
$$
r^{\text{TF}}_{t} = \alpha + \beta_1\, r^{\text{HY}}_{t} + \beta_2\, (r^{\text{HY}}_{t})^2 + u_t,
$$
$\beta_2>0$ is the smile. Fung–Hsieh's lookback-straddle interpretation (TITLE-ONLY) gives the intuition; Daniel–Moskowitz (JFE 2016, VERIFIED) show momentum's short side has option-like payoffs in panic states, which is why the losses come on the rebound. Credit twist: because long credit is short a put on firm assets (Merton), the short-credit leg of trend is long that put; trend in credit is more convex on the downside than trend in equities for the same lookback. Fidelity (data to Dec 2025, VERIFIED) finds SG Trend's correlation to the S&P 500 is −0.11 unconditionally and −0.31 in down months, and that 76% of a simple trend strategy's risk is beta timing. **Error-prone:** the convexity exists at 6–12 month horizons and not at daily ones; a quadratic fit on daily data finds nothing and the writer will conclude trend is not convex. Speed matters: SG shows faster models did best in 2020 and slower ones since 2008.

### D6. Whipsaw arithmetic (short, for 10.6/10.7)

For a V-shaped move of depth $d$ over $T$ months and a trend with effective lag $L$ months ($L<T/2$): the trend captures roughly $(T/2 - L)/(T/2)$ of the down leg and gives back $L/(T/2)$ of the up leg before flipping, so net capture $\approx d\,(T/2 - 2L)/(T/2)$, negative when $L > T/4$. March 2020 had $T \approx 2$ months; April 2025 had $T\approx 2$ months; 2008 had $T\approx 20$ months. Label this a stylized model.

---

## 4. Code spec: `credit_tsmom.py` (reference implementation)

**Inputs.** (a) Daily OAS series for US HY and US IG (FRED `BAMLH0A0HYM2`, `BAMLC0A0CM`, decimal percent), loaded from CSV if present; (b) an optional daily equity total-return series; (c) if data is absent, a seeded simulator of the OU-with-inertia spread process in D3 (parameters: $\bar s=4.5\%$, $\kappa=0.03$/month, $\phi \in \{0, 0.25\}$, $\beta$ such that annualized spread vol is 25% of level; label illustrative).

**Computes.**
1. Excess returns from spreads: $r^{ex}_t = s_{t-1}\Delta t - D^{\text{spr}}\Delta s_t$ with $D^{\text{spr}}=4.0$ for HY and $7.0$ for IG (illustrative), ACT/360 $\Delta t$.
2. Signals: sign TSMOM at 1, 3, 6, 12 months; EWMA crossover 20/120 days; an ensemble average.
3. Scaling: EWMA volatility (60-day center of mass) and the DTS alternative $\hat\sigma_t = \hat\beta\, D^{\text{spr}} s_t$ with $\hat\beta$ fitted by regressing rolling spread vol on spread level with zero intercept; target 10% annualized.
4. Trend + carry blend with weights from D3's linear forecast.
5. Equity → credit predictive regression and Granger test when an equity series is supplied.
6. Outputs: annualized return, vol, Sharpe, max drawdown, turnover (sum of absolute weight changes), convexity regression ($\beta_2$ with HAC standard errors), and a crisis-window table for 2007-06→2009-06, 2020-02→2020-06, 2022-01→2022-10, 2025-02→2025-05 whenever the data covers them.

**Tensor shapes.** Spread panel `S[T, N]` float64; returns `R[T, N]`; signals `G[T, N] ∈ [-1, 1]`; weights `W[T, N]`; P&L `P[T]`. Signals at $t$ use data through $t$ and are applied to $r_{t+1}$ (one-day lag; add a second day for CDS settlement if the writer wants to mirror Dynkin's lag test).

**Built-in sanity checks (asserted, seeded).**
- On a simulated random walk ($\kappa=\phi=0$), the 12-month sign strategy's Sharpe lies within $\pm 2/\sqrt{\text{years}}$ of zero.
- With $\phi=0.25$, the strategy's Sharpe exceeds the random-walk case by at least 0.3.
- Realized volatility of the vol-scaled strategy is within 25% of the 10% target over the full sample.
- A monotone widening path flips the position to short risk within one lookback and produces positive P&L thereafter (sign-convention guard).
- With constant spreads, cumulative excess return equals $s\cdot$(ACT/360 year fraction) to 1e-10 (carry guard).
- Turnover of the pure sign strategy equals $2\times$ the number of sign flips (weights ±1 before scaling).

Keep it pure numpy/pandas, seeded, no network calls inside the chapter's code block; data download goes in a commented preamble.

---

## 5. Source map (shelf pages, why, and the exact quotation)

| Page | Why | Quotation (verbatim, ≤60 words) |
| :-- | :-- | :-- |
| `Dynkin p.603` | Opening claim for cross-asset trend | "Stock price returns and subsequent excess returns of corporate bonds tend to be positively related." |
| `Dynkin p.606` | Decile spread, IG 1993–2017 | "It delivered negative average excess return of –4.7% per year between 1993 and 2017. In contrast, the average excess return of the top decile portfolio (D10), with the strongest equity momentum, was +4.01% per year." |
| `Dynkin p.607` | Multi-horizon signal as trend confirmation | "combining momentum signals at different horizons helps to validate (confirm) trends in stock prices. Indeed, a stock with continuing upward price trend over the previous six months has a stronger combined signal than a stock with positive price return over the past month only." |
| `Dynkin p.610` | Signal decay and turnover | "an issuer with equity momentum in the top 10% (D10) has only a 17% probability of remaining top ranked after three months" |
| `Dynkin p.613` | Time-varying credit beta of momentum | "the strategy net spread tends to decline and become negative during equity down‐cycles." |
| `Dynkin p.617` | Crisis performance of EMC | "While the corporate index has average returns of –8.07%/yr in drawdown episodes and 4.12%/yr in recovery times, the EMC strategy performed well in both regimes: 11.53%/yr in credit drawdowns and 4.30%/yr in recoveries." |
| `Dynkin p.628` | Summary stats and correlations | "The EMC strategy has been negatively correlated with equity and credit markets but positively correlated with a quality factor. Returns of the EMC strategy have been particularly strong during credit down‐cycles." |
| `Dynkin p.631` | Turning-point vulnerability; residual momentum debate | "Haesen et al. (2017) argued that this varying exposure can make the strategy vulnerable in periods of market turning points, for example when a market downturn is followed by a recovery." |
| `Dynkin p.644` | Sector timing elasticity | "average excess returns tend to increase with equity momentum with each 1%/m of additional equity momentum translating into an extra 5 to 8bp of bond excess returns." |
| `Dynkin p.647` | Sector-rotation results | "A portfolio strategy that systematically invests in sectors with strong equity momentum outperformed the index by 2.38%/yr in US IG, by 4.04%/yr in US HY, and by 1.77%/yr in Euro IG in the 10 years between 2007 and 2017, with information ratios above one before transaction costs." |
| `Dynkin p.397` | Stop-loss as momentum, with a price tag | "The effect on the performance of the Aa portfolio is therefore –18bp/year (= –187 × 9.6%)." |
| `Man_Quantitative p.25` | Issuer-level trends across the capital structure | "We generally find trends to be consistent across a capital structure and indeed across broader groups/ecosystems as well; these trends therefore tend to be less issue-specific and more at an issuer-level." |
| `Man_Quantitative p.25` | IG vs HY momentum literature | "further analysis by Jostova et al. (2013) indicated minimal effects from following Momentum strategies in investment grade, but a more meaningful impact in the high yield market." |
| `Man_Quantitative p.19` | Turnover | "Within classic quant, Momentum tends to have the highest turnover of any factor approach while both Size and Quality see the least churn." |
| `Man_Quantitative p.26` | Carry's volatility | "Over the long run, Carry appears to offer a significant premium, but with incredibly high volatility of returns. This lack of consistency means that Carry as a signal can have fantastic years and also very poor years in terms of benchmark relative performance." |
| `Paleologo p.74` | Trend vs momentum definition | "“Momentum” has a different meaning from trend-following, because it is based on relative performance, whereas the latter is based on absolute performance." |
| `Paleologo p.77` | The 2009 short-side crash via Merton | "During 2008, Momentum experienced higher volatility but did not lose money (see Figure 5.9). However, in 2009 the stocks that had experienced large losses in the previous year rallied as the market rebounded." |
| `Paleologo p.106` | Why vol targeting works | "Volatility is persistent and partially predictable, while PnL has no strong relationship to volatility." |
| `Ben_Dor p.74` | Linear vol–spread law (basis of D2) | "The estimates of α are always insigniﬁcant, indicating once more that the relation between spread volatility and spread level is best described by a linear function that intersects the origin (i.e., α is equal to zero)." |
| `Ben_Dor p.292` | Stop-loss = momentum, feedback loop | "Generally, a momentum strategy like this one does well in trending markets and poorly in choppy markets. If enough market participants adopt this approach, it could lead to destabilizing behavior in which spread widening and asset sales reinforce each other in a vicious cycle." |
| `Ben_Dor p.388` | Why CDX and cash trends diverge in crises | "However, during the crisis, spreads of cash bonds widened by much more than CDS due to liquidity effects." |
| `Ben_Dor p.390` | Basis reversal | "the CDX-cash basis became very negative as the credit crisis unfolded but reverted back toward zero as the crisis abated." |
| `Schmid p.48` | Rating momentum (non-Markov) | "Rating momentum means that prior rating changes may have predictive power for the direction of future rating changes. For example, downgrade rating momentum suggests that an obligor downgraded to B is more likely to be further downgraded than upgraded within the next year." |
| `Nuveen p.4` | The mean-reversion prior to contrast with trend | "Typically, the process begins with the assumption that spreads tend to mean revert over time, usually fluctuating within a historical range rather than continually widening or tightening." |
| `BlackRock p.4` | Regime framing for HY managers | "high yield managers delivered the bulk of their excess returns in “Very Negative” regimes, and trailed index performance in “Very Positive” regimes" |
| `Bohn_Stein p.42` | Indices as the hedging venue (dated, use as history) | "The availability of credit indexes such as the iTraxx and CDX makes it much easier to hedge portfolio exposure." |

Supporting pages without a quotation: `Dynkin pp.608–609` (Table 15.1/15.2: EMC 6.34%/yr IR 1.56 overall; 9.71%/yr Jul 2007–May 2017; Aaa–A 3.9%, Baa 8.8%, HY 15.9%), `Dynkin pp.616–619` (six credit down-cycles; EMC +35.4% in Mar 2007–Nov 2008 vs index −24.2%), `Dynkin p.620` (Fed cycles: EMC strongest in easing), `Dynkin pp.629–630` (horizon robustness; 1–3 day lags change little), `Dynkin pp.215–216` (Table 3.9: 2008 average CDX HY spread 788 bp vs HY index 899 bp; 2009: 950 vs 991), `Ben_Dor p.73` (vol vs median spread scatter for CDX.IG/XO and iTraxx), `Paleologo p.98` (vol-scaling hazard under heterogeneous vols), `Man_Quantitative p.20` (HY bid-ask gapped in Feb/Mar 2020 then normalized).

---

## 6. RESEARCH DOSSIER (dated, sourced)

### 6.1 Canon papers (bibliography verified unless marked)

- **Moskowitz, Ooi, Pedersen (2012), "Time Series Momentum,"** *JFE* 104(2): 228–250, DOI 10.1016/j.jfineco.2011.11.003. 58 liquid futures (equity index, FX, commodity, bond); 1–12 month persistence then partial reversal; diversified TSMOM "performs best during extreme markets"; speculators profit, hedgers pay. **No credit indices in the sample.** VERIFIED (IDEAS).
- **Hurst, Ooi, Pedersen (2017), "A Century of Evidence on Trend-Following Investing,"** *JPM* 44(1), Fall 2017. Simulated back to 1880. VERIFIED (AQR page). Secondary sources list 67 markets, 1880–2016 (SEARCH-LISTED; CHECK before quoting counts).
- **Kim, Tse, Wald, "Time Series Momentum and Volatility Scaling,"** 55 futures 1985–2013: monthly alpha 1.27% with vol scaling vs 0.41% without; XSMOM 0.95%. Journal of Financial Markets 2016 (CHECK venue). VERIFIED via Quantpedia summary.
- **Baz, Granger, Harvey, Le Roux, Rattray (2015), "Dissecting Investment Strategies in the Cross Section and Time Series,"** Man AHL; TS momentum works well, XS momentum poorly, carry works in both, best combined. SSRN 2695101 as cited by Quantpedia (SSRN itself returned 403). SEARCH-LISTED.
- **Hamill, Rattray, van Hemert, "Trend Following: Equity and Bond Crisis Alpha,"** SSRN 2831926 (SEARCH-LISTED; not fetched). 1960–2015; TSMOM strong in worst equity and bond environments. TITLE-ONLY for URL.
- **Babu, Levine, Ooi, Schroeder, Stamelos (2020), "You Can't Always Trend When You Want,"** *JPM*; post-GFC underperformance due to muted market moves, not signal decay. VERIFIED (AQR page).
- **Daniel & Moskowitz (2016), "Momentum Crashes,"** *JFE* 122(2): 221–247, DOI 10.1016/j.jfineco.2015.12.002. Crashes in panic states after declines with high vol; short side option-like; dynamic strategy roughly doubles Sharpe. VERIFIED.
- **Barroso & Santa-Clara (2015), "Momentum Has Its Moments,"** *JFE* 116(1): 111–120, DOI 10.1016/j.jfineco.2014.11.010. Managing momentum risk "virtually eliminates crashes and nearly doubles" Sharpe. VERIFIED.
- **Moreira & Muir (2017), "Volatility-Managed Portfolios,"** *JF* 72(4): 1611–1644. VERIFIED citation (IDEAS page has no abstract).
- **Koijen, Moskowitz, Pedersen, Vrugt (2018), "Carry,"** *JFE* 127(2): 197–225, DOI 10.1016/j.jfineco.2017.11.002. Carry predicts returns in global equities, bonds, commodities, Treasuries, **credit**, options. VERIFIED.
- **Asness, Moskowitz, Pedersen (2013), "Value and Momentum Everywhere,"** *JF* 68(3): 929–985. VERIFIED citation.
- **Pitkäjärvi, Suominen, Vaittinen (2020), "Cross-asset signals and time series momentum,"** *JFE* 136(1): 63–85, DOI 10.1016/j.jfineco.2019.02.011. 20 countries; past bond returns predict equities positively, past equity returns predict (government) bonds negatively; cross-asset TSMOM Sharpe 45% higher; "slow-moving capital." VERIFIED.
- **Jostova, Nikolova, Philipov, Stahel (2013), "Momentum in Corporate Bond Returns,"** *RFS* 26(7): 1649–1693, DOI 10.1093/rfs/hht022. 81,491 bonds 1973–2011; 1991–2011 momentum 59 bp/month all bonds, 192 bp/month non-IG, 282 bp/month NIG bonds of private firms; not explained by risk or frictions; not a reflection of equity momentum. VERIFIED (IDEAS). 2010 FDIC WP version: 77,150 bonds, 64 bp/month 1991–2008, 190 bp/month NIG, profits from winners, disappear after removing worst-rated ~8% (VERIFIED PDF).
- **Gebhardt, Hvidkjaer, Swaminathan (2005), "Stock and bond market interaction: Does momentum spill over?"** *JFE* 75(3): 651–690. IG bonds show reversals not momentum at 3–12 months; equity momentum spills into same-firm bonds, stronger for lower-grade debt and high equity volume; underreaction to changing default risk. SEARCH-LISTED (Kellogg page 404; IDEAS URL in search results).
- **Haesen, Houweling, van Zundert (2017), "Momentum spillover from stocks to corporate bonds,"** *JBF* 79: 28–41, DOI 10.1016/j.jbankfin.2017.03.003. Firm-specific equity returns halve default-risk exposure, double Sharpe, cut drawdowns at bear→bull turns. VERIFIED.
- **Bali, Subrahmanyam, Wen (2021), "Long-term reversals in the corporate bond market,"** *JFE* 139(2): 656–677, DOI 10.1016/j.jfineco.2020.08.007. 1977–2017; reversals strongest for high-credit-risk bonds and binding constraints; driven by long-term losers. VERIFIED. (Same page lists Ho & Wang 2018, "Momentum lost and found in corporate bond returns," and Medhat & Schmeling 2022, "Short-term Momentum," TITLE-ONLY.)
- **Lee, Naranjo, Sirmans (2021), "CDS Momentum: Slow-Moving Credit Ratings and Cross-Market Spillovers,"** *RAPS* 11(2): 352–401, DOI 10.1093/rapstu/raaa025. CDS return momentum ≈7.1%/yr; cross-market strategies from past CDS performance ≈10.3%/yr alpha in stocks and 7.3%/yr in bonds; strongest in liquid contracts ahead of slow rating changes. VERIFIED.
- **Hilscher, Pollet, Wilson (2015), "Are Credit Default Swaps a Sideshow?"** *JFQA* 50(3): 543–567, DOI 10.1017/S0022109015000228. Equity leads CDS at daily and weekly horizons; CDS reacts faster on salient news days. VERIFIED.
- **Norden & Weber (2009), "The Comovement of CDS, Bond and Stock Markets,"** *EFM* 15(3): 529–562. 2000–2002: stocks lead CDS and bond spreads; CDS leads bonds; stronger for lower-rated and US firms. VERIFIED.
- **Acharya & Johnson (2007), "Insider trading in credit derivatives,"** *JFE* 84(1): 110–141. Incremental information in CDS, bad-news only, increasing in number of bank relationships. VERIFIED.
- **Lee, Naranjo, Velioglu (2018), "When do CDS spreads lead?"** *JFE* 130(3): 556–578, DOI 10.1016/j.jfineco.2018.07.011. 3,470 S&P rating events 2001–2013; CDS→bond one-way flow, strongest for private entities; CDS returns predict idiosyncratic stock returns. VERIFIED.
- **Kwan (1996), "Firm-specific information and the correlation between individual stocks and bonds,"** *JFE* 40(1): 63–80. VERIFIED citation only.
- **Oehmke & Zawadowski (2017), "The Anatomy of the CDS Market,"** *RFS* 30(1): 80–119. Speculative trading concentrates in CDS; hedging links bond and CDS volumes. VERIFIED.
- **Collin-Dufresne, Junge, Trolle (2020), "Market Structure and Transaction Costs of Index CDSs,"** *JF* 75(5): 2719–2763, DOI 10.1111/jofi.12953. Two-tiered market persists post-Dodd-Frank; client trades larger, infrequent, informed; dealers price-discriminate on expected impact. VERIFIED.
- **Dick-Nielsen, Feldhütter, Pedersen, Stolborg (2023), "Corporate Bond Factors: Replication Failures and a New Framework,"** AQR working paper, SSRN 4586652 (as listed on AQR page). Most factors fail to replicate; several equity signals work for bonds. VERIFIED (AQR page). Whether bond momentum survives is not stated on the page: CHECK in the paper before claiming.
- **Haynes & McPhail (CFTC OCE, June 2017), "The Liquidity of Credit Default Index Swap Networks."** Bloomberg SEF data May 2014–Sep 2016: CDX IG ADV $7.05bn, 108 trades/day; peak $22.7bn (331 trades) on 9 Feb 2016; price impact of CDX HY trades >$500mm ≈0.3 bp (≈0.5% of spread); dealer-to-dealer ≈15% of BSEF volume in IG/iTraxx, 8% in HY; customers with more dealer connections pay less. VERIFIED PDF.
- **Lempérière et al. / CFM (May 2015), "Trend Following: A Persistent Market Anomaly,"** condensed from *J. Investment Strategies* 3: 41–61 (2014): two centuries, 100-day SMA, constant-risk sizing; Sharpe 0.72, "10 sigma"; CTA industry $317bn at Q4 2014. VERIFIED PDF.

### 6.2 Industry research and practitioner evidence

- **SG Prime Services, "CTA Industry Update: Keeping Up with the Trend Followers" (May 2025, data to 13 May 2025).** SG Trend Index −4.9% in April 2025, −9.3% YTD; SG Short-Term Traders Index −0.9% April, −0.9% YTD; dispersion among trend followers ~15% range in 2024 with pairwise correlation 0.78; industry AUM ≈ $340bn (BarclayHedge Q4 2024); the SG Trend Indicator is a 20d/120d MA crossover; since 2007 the Trend Index "behaves more like a much slower model"; faster models "delivered the best hypothetical returns" in 2020. Quotable line: CTAs show "a level of adaptability akin to the Kardashians." VERIFIED PDF.
- **Cambridge Associates (Aug 2025), "Does Trend-Following's Recent Struggle Signal That the Strategy Is Structurally Broken?"** SG Trend +20.9% in 2008 (MSCI ACWI −42.2%), +27.4% in 2022 (ACWI −18.4%); −20.4% from May 2024 to May 2025, second-largest drawdown since 2000; 16 drawdowns >10% since 2000. VERIFIED.
- **Kaminski & Wen, AlphaSimplex (June 2025), "Market Cycles and Managed Futures Drawdowns."** Table of SG Trend drawdowns >10% since 2000: "Liberation day" −21.8% (15 Apr 2024–14 May 2025); "Trade War 1.0" −23.0% (2015–2019); "GFC Recovery" −11.3% from 9 Mar 2009; "Fed Inflation Fight Reversal" −10.1% (14 Jun–10 Aug 2022); "SVB Banking Crisis" −15.4% (20 Oct 2022–17 Mar 2023); "2008 Commodity Collapse" −10.7% (Jul–Sep 2008). VERIFIED PDF.
- **Man Group, Korgaonkar (mid-2025), "Trend Following and Drawdowns: Is This Time Different?"** SG Trend rolling 12-month return to 30 Apr 2025: −18.6%; only twice before below −15%; trend strategies repositioned after the 2 April tariff shock and were positive by 9 April. VERIFIED.
- **Man Group, Georgiades, Wong, Abou Zeid, "A Trend Following Deep Dive: The Dynamics of Dispersion" (data to Dec 2024).** Best-to-worst SG Trend constituent gap ~10 pp/yr; including alternative markets "such as power, synthetic credit indices and interest rate swaps" improved performance, more so for slower systems. VERIFIED.
- **Man Institute, Robertson (May 2023), "Trend-Following: What's Not to Like?"** BTOP50 since 1986: 7.0% annualized vs 7.7% world stocks, vol 9.6% vs 14.4%, max DD −16.1% vs −50.4%; crisis table: +17% in the credit crisis (Jul 2007–Feb 2009), −2% in COVID (Feb–Mar 2020), +19% in Jan–Sep 2022; BTOP50 flat 2009–2019; trend takes "typically 3–6 months" to find a new trend. VERIFIED PDF.
- **Fidelity, Croce, Hazrachoudhury, Carton (data Jan 2000–Dec 2025), "Trend-following crisis alpha: Does it come from beta timing or market selection?"** SG Trend excess return 4.2%/yr, vol 13.4%, Sharpe 0.31; correlation to S&P −0.11, −0.31 in down months; trend added strongly in 2000, 2007, 2022 drawdowns and "did not contribute positively" in COVID 2020 or Q4 2018; 76% of a simple trend strategy's risk is beta timing. VERIFIED PDF.
- **Hedge Fund Journal (2013), "AHL Evolution."** Credit was the first asset class the programme traded (2005); exposure via selling CDS protection on CDX and iTraxx, able to flip to buying protection; short credit during 2008; corporate credit and EM debt "produced more persistent trends than most other asset classes"; fixed income was the bulk of the 2012 return (23.6%). VERIFIED. Hedge Fund Journal (Nov/Dec 2017), "Man AHL Marks 30 Years": ~600 markets, 25–50 new markets per year. VERIFIED.

### 6.3 The venue: index CDS market data 2021–2026

- **ISDA Research Note (29 July 2026), "CDS Market Dynamics: Five Years of Activity and a Record 2025."** Total CDS activity $41.8tn in 2025 (prior peak $38.7tn in 2022; $31.4tn in 2023); index CDS 93.3% of activity, record $39.0tn (prior $36.4tn 2022; $28.1tn 2023); single-name peaked $3.3tn in 2023, $2.8tn in 2025; index-to-single-name ratio 15.7× (2022), 8.5× (2023), 13.8× (2025); CDX.NA.IG 43.4% and iTraxx Europe 32.4% of index activity in 2025, CDX.NA.HY 10.4%, iTraxx Crossover 7.7%; average IG index trade ≈$90mm vs ≈$25mm for HY benchmarks; CDX.NA.IG 500–900 trades/day (>900 in Q2 2025); Q1 2020 index activity +78.1% vs trailing four-quarter average (single-name +16.1%); Q1 2023 single-name +84.8% (index +4.5%); Q2 2025 (tariffs) index +20.9%, single-name −20.7%; rolls around March 20 and September 20 with the two-week roll window 25–50% of quarterly notional; H1 2026 total $27.4tn (+27.8% YoY). VERIFIED PDF and HTML.
- **ISDA SwapsInfo H1 2025.** Index credit derivatives notional +91.9% to $10.5tn (partly a reporting-threshold change effective Oct 2024, footnote 4); CDX IG $4.0tn (+111.1%), CDX HY $1.2tn (+44.5%), iTraxx Europe $2.3tn (+73.7%); >99% of CDX HY/IG and iTraxx Europe notional cleared; SEF share 98.0% IG, 97.6% HY, 96.5% iTraxx Europe; corporate single-name $257.1bn (−1.2%). VERIFIED PDF.
- **Clarus (10 June 2026).** Cleared USD CDX $3.94tn in March 2026 (+46% YoY); SDR-reported CDX $2.18tn (IG $1.67tn, HY $407bn, EM $70.8bn); cleared EUR iTraxx $2.97tn (+51%); cleared CDX swaptions $52.9bn (+80%); iTraxx swaptions +133%; ICE ≈91% of cleared USD credit in Q1 2026. VERIFIED.
- **LCH CDSClear Q3 2025 dashboard.** Record $198bn of CDX and iTraxx cleared in one day (22 Sep 2025, +110% vs the Sep 2024 roll); client index roll volume +66% YoY; record €7.025tn cleared Sep 2025 YTD vs €5,437bn in all of 2024. VERIFIED PDF.
- **ECB FSR (Dec 2006) special feature:** iTraxx launched summer 2004; 125 names; rolled every half year. VERIFIED PDF (historical color).

### 6.4 Spread levels for the crisis windows

- **FRED, ICE BofA US HY OAS (`BAMLH0A0HYM2`), verified daily data Oct 2023–Oct 2026:** 2.62% on 18 Feb 2025; 3.42% on 2 Apr 2025; **4.61% on 7 Apr 2025** (2025 high); 4.57% on 8 Apr; 4.37% on 9 Apr; 3.31% on 30 May 2025; 2.81% on 31 Dec 2025; 2026 high 3.46% on 30 Mar 2026; 3.23% on 15 Oct 2026; 2024 high 3.93% on 5 Aug 2024; late-2023 high 4.53% on 27 Oct 2023. **IG OAS (`BAMLC0A0CM`):** 2025 high 1.21% on 9 Apr 2025; 2026 high 0.94% on 16 Mar 2026; 0.84% on 15 Oct 2026. VERIFIED (downloaded; full history before Oct 2023 could not be pulled through the proxy, so the chapter code should fetch the full series).
- **2008:** US HY OAS record roughly 2,000 bp in Nov/Dec 2008 (secondary sources disagree on the exact date; CHECK against FRED in the chapter). Sourced alternative: Dynkin Table 3.9 average month-end spreads 2008: HY index 899 bp, CDX HY 788 bp; 2009: 991 vs 950 (`Dynkin p.216`). Cash-CDS basis very negative in the crisis (`Ben_Dor p.390`).
- **2020:** US HY OAS peak ≈1,100 bp around 23 March 2020 (secondary; CHECK exact value and date on FRED). CDX HY/IG peak levels: CHECK before stating.
- **2022:** US HY OAS peak ≈600 bp in July 2022 (secondary; CHECK). 2022 was the prior record year for index CDS activity ($36.4tn, ISDA, VERIFIED).
- **2023 (SVB):** single-name CDS activity +84.8% in Q1 2023 (ISDA, VERIFIED); spread peak CHECK.

### 6.5 Trend data points for the chapter's trend narrative (2018–2026)

- CTAs got slower: SG heat map shows the Trend Index correlating with faster MA models in 2000–2006 and with "a much slower model" since 2007 (SG 2025, VERIFIED).
- Trend AUM ≈ $340bn (BarclayHedge Q4 2024 via SG) vs ≈ $317bn at Q4 2014 (CFM): roughly flat for a decade in nominal terms. VERIFIED.
- Dispersion rose after 2007: average pairwise correlation among SG Trend constituents fell from 0.87 to 0.78 (Man deep dive, VERIFIED).
- Alternative markets, including synthetic credit indices, became a standard differentiator (Man deep dive; AHL Evolution history). VERIFIED.
- Index CDS activity and clearing hit records in 2025–2026 with swaptions growing faster than indices (ISDA, Clarus). VERIFIED.
- Credit index futures on exchanges (CME Bloomberg corporate index futures): CME page unreachable this session; CHECK launch dates and open interest before including.
- Podcast evidence of the 2024–26 debate: Top Traders Unplugged, Systematic Investor ep. 422 with Katy Kaminski (17 Oct 2026) on patience and crisis alpha in an inflationary world; Top Traders Unplugged ep. 153 with Patrick Welton (30 Sep 2026) on the four drivers of trend returns (economic carry, financial carry, information diffusion, reflexivity). VERIFIED pages.

---

## 7. Case studies

**Case A — 2008–2009: the trend that paid and the rebound that charged.** Facts: SG Trend +20.9% in 2008 (Cambridge Associates); BTOP50 +17% Jul 2007–Feb 2009 while world stocks −49% (Man 2023); AHL Evolution was short credit via index protection in 2008 (HFJ 2013); EMC +35.4% in the Mar 2007–Nov 2008 credit down-cycle vs IG index −24.2% (`Dynkin p.618`); average 2008 CDX HY spread 788 bp vs HY cash index 899 bp (`Dynkin p.216`), the cash-CDS basis "very negative" (`Ben_Dor p.390`). Then: SG Trend "GFC Recovery" drawdown −11.3% from 9 Mar 2009 (AlphaSimplex); equity momentum's 2009 crash from the short side (`Paleologo p.77`; Daniel–Moskowitz). Systematic desk lesson: the long-protection trend was right for 20 months and wrong for the two that cost the most; the exit rule is the strategy.

**Case B — February–June 2020: the V that trend could not trade.** Facts: index CDS activity +78.1% vs trailing average in Q1 2020 (ISDA); HY bid-ask gapped in Feb/Mar 2020 then normalized (`Man_Quantitative p.20`); BTOP50 −2% Feb–Mar 2020 (Man 2023); SG Trend "did not contribute positively" in the COVID drawdown (Fidelity); faster models did best in 2020 (SG). HY OAS ≈1,100 bp peak late March (CHECK exact). Lesson via D6: $T\approx 2$ months is shorter than most trend lags; the Fed facility announcements are the $\kappa$ shock; the only trend that made money was fast, and fast is expensive in cash credit.

**Case C — 2022: the slow grind, trend's best year, and its own reversal inside it.** Facts: SG Trend +27.4% (Cambridge Associates); BTOP50 +19% Jan–Sep 2022 (Man 2023); the "Fed Inflation Fight Reversal" −10.1% drawdown 14 Jun–10 Aug 2022 (AlphaSimplex); index CDS activity record $36.4tn (ISDA). Credit specifics: both legs (short duration, short spread) trended; EMC is historically weaker in tightening regimes (`Dynkin p.620`). HY OAS ≈600 bp July 2022 (CHECK). Lesson: the convexity shows up at the 9-month horizon and the whipsaw at the 2-month one, in the same year.

**Coda — April 2025 "Liberation Day" (FRED-verified).** HY OAS 2.62% (18 Feb) → 3.42% (2 Apr) → 4.61% (7 Apr) → 3.31% (30 May); IG OAS peak 1.21% on 9 Apr. SG Trend −4.9% in April, −9.3% YTD (SG); 12-month return to 30 Apr −18.6% (Man); the −21.8% drawdown from Apr 2024 to May 2025 (AlphaSimplex); index CDS activity +20.9% vs trailing average while single-name fell 20.7% (ISDA). Trend repositioned and was positive by 9 April per Man, which the chapter should present alongside the SG and AlphaSimplex numbers rather than as a verdict.

---

## 8. Humor beats (canon cast; each rides on a correct idea)

1. **Kaz vs legal vocabulary:** Kaz hears "iTraxx Crossover" and starts drafting a cross-default clause. Ines: "It's 75 sub-investment-grade names, Kaz. The only thing it crosses is your P&L in March." (Correct idea: Crossover is the European HY index, not a covenant.)
2. **Mags, back in my day:** "We had trend-following in credit. It was called 'Sal stopped picking up.' When the phone went quiet for a week, you were short whether you liked it or not." Then grudging respect for a 60-day EWMA that at least returns calls. (Correct idea: dealer liquidity withdrawal is the original trend signal.)
3. **ROBO literalism (spec box opener):** Vague spec: "Follow the trend in credit and don't get whipsawed." What ROBO built: a strategy that trades once a decade and was short CDX HY at 100% of risk on 24 March 2020. Precise spec follows. (Correct idea: speed is the parameter, not a vibe.)
4. **The 13-week model, reborn:** Theo discovers that his 13-week cash flow model is a 65-trading-day lookback, which is within rounding of MOP's 60-day volatility window. "The only lookback a restructuring banker ever trusted." (Correct idea: horizon choice; the joke is that 13 weeks is a liquidity horizon, not a trend horizon, and the chapter says why.)
5. **Ines, Poker Table:** "Who at this table knows more than you? In credit, the equity market, by about a week. Trend-following is sitting to its left and calling." (Correct idea: Hilscher et al.; EMC.)
6. **IDO or it didn't happen:** Fidelity finds 76% of a trend strategy's risk is beta timing. Desk translation: "Trend is beta that changed its mind. It is still beta. Strip it before you call it alpha." (Correct idea: beta-timing vs relative-value decomposition.)
7. **On the 83% decay (`Dynkin p.610`):** "An equity momentum signal has the half-life of an ad hoc group: by the time counsel is retained, the top decile has left the building." (Correct idea: signal decay and turnover.)
8. **Desk Myth vs Desk Reality:** Myth: a credit trend follower has a view on spreads. Reality: half of its P&L is a view on volatility, and in credit volatility is spread times duration, so the position is sized by the thing it is forecasting. Kaz: "Let's just assume Gaussian." Everyone: "No."
9. **The Kardashian line (real, attributable):** SG's May 2025 note says CTAs "showcase a level of adaptability akin to the Kardashians." Use it as a Trend Watch epigraph; it is a verified quotation from a primary source, and it teaches that managers run many speeds at once.
10. **"Open market purchase":** When the index widens 200 bp in a week, a long-protection trend position is not an open market purchase of anybody's bonds; it is a bet that the dealers who quote CDX IG 900 times a day will keep doing so. They did in 2020 (ISDA volumes rose 78%); the cash market did not (Man 2022 bid-ask chart). (Correct idea: venue liquidity under stress.)

---

## 9. Resource-graph candidates

**VERIFIED-URL (fetched this session)**
- IDEAS pages: MOP 2012 `https://ideas.repec.org/a/eee/jfinec/v104y2012i2p228-250.html`; Koijen et al. 2018 `https://ideas.repec.org/a/eee/jfinec/v127y2018i2p197-225.html`; Pitkäjärvi et al. 2020 `https://ideas.repec.org/a/eee/jfinec/v136y2020i1p63-85.html`; Barroso–Santa-Clara 2015 `https://ideas.repec.org/a/eee/jfinec/v116y2015i1p111-120.html`; Daniel–Moskowitz 2016 `https://ideas.repec.org/a/eee/jfinec/v122y2016i2p221-247.html`; Acharya–Johnson 2007 `https://ideas.repec.org/a/eee/jfinec/v84y2007i1p110-141.html`; Haesen et al. 2017 `https://ideas.repec.org/a/eee/jbfina/v79y2017icp28-41.html`; Lee–Naranjo–Velioglu 2018 `https://ideas.repec.org/a/eee/jfinec/v130y2018i3p556-578.html`; Bali et al. 2021 `https://ideas.repec.org/a/eee/jfinec/v139y2021i2p656-677.html`; Oehmke–Zawadowski 2017 `https://ideas.repec.org/a/oup/rfinst/v30y2017i1p80-119..html`; Collin-Dufresne et al. 2020 `https://ideas.repec.org/a/bla/jfinan/v75y2020i5p2719-2763.html`; Jostova et al. 2013 `https://ideas.repec.org/a/oup/rfinst/v26y2013i7p1649-1693.html`; Lee–Naranjo–Sirmans 2021 `https://ideas.repec.org/a/oup/rasset/v11y2021i2p352-401..html`; Norden–Weber 2009 `https://ideas.repec.org/a/bla/eufman/v15y2009i3p529-562.html`; Moreira–Muir 2017 `https://ideas.repec.org/a/bla/jfinan/v72y2017i4p1611-1644.html`; Kwan 1996 `https://ideas.repec.org/a/eee/jfinec/v40y1996i1p63-80.html`; Asness–Moskowitz–Pedersen 2013 `https://ideas.repec.org/a/bla/jfinan/v68y2013i3p929-985.html`.
- Hilscher–Pollet–Wilson 2015 (Cambridge) `https://www.cambridge.org/core/journals/journal-of-financial-and-quantitative-analysis/article/abs/are-credit-default-swaps-a-sideshow-evidence-that-information-flows-from-equity-to-cds-markets/F7CCD2FFB20AAEACE1E093D12EEF7A31`.
- AQR: Hurst–Ooi–Pedersen `https://www.aqr.com/Insights/Research/Journal-Article/A-Century-of-Evidence-on-Trend-Following-Investing`; Babu et al. `https://www.aqr.com/Insights/Research/Journal-Article/You-Cant-Always-Trend-When-You-Want`; Dick-Nielsen et al. `https://www.aqr.com/Insights/Research/Working-Paper/Corporate-Bond-Factors-Replication-Failures-and-a-New-Framework` (SSRN 4586652 listed there).
- Man Group: `https://www.man.com/insights/deep-dive-trend-following`; `https://www.man.com/insights/is-this-time-different`; Robertson 2023 PDF (hosted copy) `https://americanbeaconfunds.com/wp-content/uploads/2025/08/Trend-Following-Whats-Not-to-Like_AHL-TREND-WP-1.pdf`.
- Cambridge Associates `https://www.cambridgeassociates.com/insight/does-trend-followings-recent-struggle-signal-that-the-strategy-is-structurally-broken/`.
- AlphaSimplex `https://www.alphasimplex.com/assets/files/2025.06---market-cycles-and-managed-futures---kaminski-and-wen.pdf`.
- SG Prime Services `https://content.sgmarkets.com/CTA_UPDATE_KEEPING_UP_WITH_THE_TRENDFOLLOWERS_2025`.
- Fidelity `https://institutional.fidelity.com/app/proxy/content?literatureURL=%2F9922231.PDF`.
- ISDA note `https://www.isda.org/2026/07/29/cds-market-dynamics-five-years-of-activity-and-a-record-2025/` and PDF `https://www.isda.org/a/Pa0iE/CDS-Market-Dynamics-Five-Years-of-Activity-and-a-Record-2025.pdf`; SwapsInfo H1 2025 `https://www.isda.org/a/4cpgE/SwapsInfo-First-Half-of-2025-and-the-Second-Quarter-of-2025.pdf`; SwapsInfo weekly `https://analysis.swapsinfo.org/2025/06/interest-rate-and-credit-derivatives-weekly-trading-volume-week-ending-june-20-2025/`.
- Clarus `https://www.clarusft.com/us-firms-powered-march-2026-itraxx-swaps-volume-growth/`; LCH `https://www.lseg.com/content/dam/post-trade/en_us/documents/lch/resources/cdsclear-dashboard-q3-2025.pdf`.
- CFTC `https://www.cftc.gov/sites/default/files/idc/groups/public/@economicanalysis/documents/file/oce_credit_swap_liquidity.pdf`; FDIC WP 2010-04 `https://www.fdic.gov/analysis/cfr/working-papers/2010/2010-04.pdf`; CFM 2015 `https://www.cfm.com/wp-content/uploads/2022/12/298-2015-CFM-Trend-Following-a-Persistent-Market-Anomaly.pdf`; ECB FSR Dec 2006 `https://www.ecb.europa.eu/pub/pdf/fsr/art/ecb.fsrart200612_02.en.pdf`.
- Quantpedia (Kim–Tse–Wald summary) `https://quantpedia.com/deconstructing-the-time-series-momentum-strategy/`; Hedge Fund Journal `https://thehedgefundjournal.com/ahl-evolution/`, `https://thehedgefundjournal.com/man-ahl-marks-30-years/`.
- Podcasts: Top Traders Unplugged ep. 422 `https://www.toptradersunplugged.com/podcast/why-trend-following-rewards-patience-ft-katy-kaminski/`; ep. 153 `https://www.toptradersunplugged.com/podcast/why-investors-keep-getting-trend-following-wrong-ft-patrick-welton/`; Flirting with Models S7E19 Jeff Rosenberg (systematic fixed income, 18 Aug 2025) `https://www.flirtingwithmodels.com/episodes/8V74zBaN4jN`; S7E25 Takahe Capital, trend-following spreads (12 Jan 2026) `https://www.flirtingwithmodels.com/episodes/1iIqmQ7piJd`.
- Data: FRED series roots `https://fred.stlouisfed.org/series/BAMLH0A0HYM2`, `https://fred.stlouisfed.org/series/BAMLC0A0CM` (canonical).

**SEARCH-LISTED (URL seen in results, page not fetched; cite title and authors, link optional with flag)**
- Hamill, Rattray, van Hemert, "Trend Following: Equity and Bond Crisis Alpha" (SSRN 2831926). Baz et al. 2015 (SSRN 2695101, per Quantpedia). Gebhardt et al. 2005 (IDEAS `v75y2005i3p651-690`). Fung & Hsieh 2001, "The Risk in Hedge Fund Strategies: Theory and Evidence from Trend Followers" (*RFS*). Pu et al., "Network Momentum across Asset Classes" (arXiv 2308.11294).

**TITLE-ONLY (no link)**
- Baltas & Kosowski, "Demystifying Time-Series Momentum Strategies: Volatility Estimators, Trading Rules and Pairwise Correlations." Israel, Palhares, Richardson (2018), "Common Factors in Corporate Bond Returns," *JIM*. Houweling & van Zundert (2017), "Factor Investing in the Corporate Bond Market," *FAJ*. Brooks, Palhares, Richardson (2018), "Style Investing in Fixed Income," *JPM*. Greyserman & Kaminski (2014), *Trend Following with Managed Futures*. Robertson & Goodall (2023), "Trend-Following: A Different Point of Skew" (Man). Kaminski (2025), "Themes of 2024: Slow and Steady Wins the Race" (AlphaSimplex). Naik, Trinh, Rennison (2002); Lin, Wang, Wu (2013); Khang & King (2004); Pospisil & Zhang (2010), all as cited in Dynkin/Man. Ho & Wang (2018); Medhat & Schmeling (2022). Bloomberg *Odd Lots* episodes on CTAs: none verified this session; name the show only.

---

## 10. Exploratory-space notes (future sections and chapters)

1. **Ch 10-B: Credit index microstructure for systematic traders.** Rolls (ISDA: roll windows carry 25–50% of quarterly notional; LCH's $198bn record day on 22 Sep 2025), index skew vs intrinsic, series basis, swaptions (growing faster than indices per Clarus), dealer-to-client price discrimination (Collin-Dufresne et al.). Trend signals that straddle a roll need a roll-adjusted return series; nobody on the shelf specifies one.
2. **Speed as a regime variable.** SG's finding that CTAs slowed after 2007 while fast models won in 2020 and 2025 argues for a section on multi-speed ensembles and short-term CTA strategies in credit, with explicit cost curves (fast trend in cash credit is uneconomic; in CDX it may not be).
3. **Trend convexity via swaptions.** Replacing the short-credit leg of trend with payer swaptions converts path risk into premium; a derivation of break-even vol vs trend lag belongs in Ch 23 or a new 10-C.
4. **Cross-asset lead–lag networks.** Extend Pitkäjärvi et al. and Lee–Naranjo–Sirmans to a credit-centered network (equity → CDS → bonds → loans), with a Ch 25 tie-in to NLP-derived news timing (Hilscher's salient-news-day result).
5. **Rating momentum as fundamental trend.** Schmid's non-Markov transitions and Lee–Naranjo–Sirmans's "slow-moving ratings" channel: a section on predicting rating drift and its P&L in Ch 11 or 14.
6. **Trend in the LMT era.** Survival-adjusted trend signals for single names where the jump is a liability-management event rather than a default; link to the Priming Risk Score (Ch 13) and to re-default rates after LMTs (Ch 14).
7. **Replication risk in bond momentum.** Dick-Nielsen et al.'s framework should be applied to momentum specifically in Edition 2 (the paper's page does not say whether bond momentum survives; read the tables).
8. **Flows, slow-moving capital and trend.** Mutual-fund flows, ETF creations (Ch 20) and dealer inventories as the mechanism behind credit trend; connect to the "destabilizing behavior" warning in `Ben_Dor p.292`.
9. **Exchange-traded credit futures as a trend venue.** CME's Bloomberg corporate index futures (CHECK launch dates, open interest, and whether CTAs have adopted them) for Appendix C and Ch 22.
10. **Private credit marks and spurious momentum.** Smoothing in BDC/private marks creates serial correlation that looks like trend and is not tradable; a Ch 17 box.
11. **Appendix C Trend Tracker entries from this brief:** ISDA 2025 record ($41.8tn), index share 93.3%, CDX IG share 43.4%, CDX IG trades/day 500–900, H1 2025 CDX IG +111%, March 2026 cleared CDX $3.94tn, LCH record day Sep 2025, CTA AUM ≈$340bn, SG Trend 2008 +20.9%, 2022 +27.4%, 2024–25 drawdown −20.4%/−21.8%, April 2025 HY OAS peak 4.61%.
