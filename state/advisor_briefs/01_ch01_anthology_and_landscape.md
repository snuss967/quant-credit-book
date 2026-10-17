# Advisor Brief: Chapter 1, The Anthology of the Desk & the Modern Quant Credit Landscape

*Fable advisor, Edition 1. Target file: `book_src/01_ch01_anthology_and_landscape.md`. Research date: 2026-10-17. Facts below are VERIFIED (fetched this session, URL given) unless marked CHECK (seen only in a search summary, or in a page we could not open). Shelf quotations were copied from `state/pdf_pages` text; page numbers are PDF page indices as `tools/pdf_search.py` prints them.*

---

## 1. Thesis and the "aha" for an ex-PJT-RSSG reader

**Thesis.** Credit is not one market; it is a plumbing diagram of holders who each carry a *contractual or regulatory trigger that converts a rating, a test, or a redemption into a sale at a known time and a knowable size*. Insurers sell on downgrade because capital charges jump at the IG/HY line; IG index funds and ETFs sell at the month-end rebalance after a fallen-angel event; CLOs sell (or stop reinvesting) when CCC buckets breach ~7.5% and OC cushions thin; open-end HY funds sell whatever is liquid when redemptions arrive; banks and CDOs dump post-reorg equity because they are "not natural holders"; trade-claim holders sell because they cannot wait for a plan. Every one of those sales is *information-free about the bond and information-rich about the seller*. The whole systematic-credit industry, from Blackstone's "contrarian liquidity provider" optimizer to Man Numeric's fallen-angel program to the SIG-style RFQ engine, is a set of machines for standing on the other side of those flows at the right price. The shelf, read this way, is one book: Ben Dor tells you how to size the risk you take when you catch the flow (DTS); Bohn–Stein and Schmid tell you how to price the default you might be catching (DD, intensity); Bolder tells you what happens when the flows correlate (threshold models); Dynkin and Man tell you which flows are systematically harvestable (fallen angels, equity momentum); Moyer and Houlihan Lokey tell you where the flows end up when the company breaks (fulcrum, 363); Paleologo tells you how to tell whether you actually made money doing it (IDO).

**The aha.** An RSSG banker already knows the *triggers* better than any quant: which test, which clause, which date. What they have never done is write the triggers down as a **forced-supply function** $Q^{\text{sell}}(\text{event})$ with a size and a timestamp, and then price the *other* leg: how much of that supply the natural buyers absorb before the price has to move. The quant desk's entire edge is that function. Man Group says the quiet part out loud on the shelf: quant credit "is yet to move into distressed debt – this is a high-touch asset class that requires a significant degree of human intervention" (Man 2022 p.42). The reader is the human intervention, pre-packaged. Chapter 1's job is to make them see their old job as a feature pipeline, and the ecosystem as a graph whose edges they can already label.

**Second aha (the bid equation).** The seed's §1.1 bid formula is not decoration; it is the reservation price of a CARA dealer plus a Glosten–Milgrom adverse-selection term, and each of its three pieces maps to one part of the book: fair value (Parts II, VI), inventory skew (Parts V, VIII), toxicity (Parts III, IV, VII). Derive it in Chapter 1 so the rest of the book is a commentary on three terms.

---

## 2. Section outline (7,000–10,000 words)

Keep the seed's §1.1 and §1.2; rebuild and expand from §1.3. The six anatomy elements are marked [F]raming, [D]erivation, [S]pec, [X]traction, [C]ase, [R]esource graph.

- **Cold open (≤400 words).** Theo's third week. 2:58 p.m. Friday; an all-to-all RFQ for \$15mm of a B3 bond whose lender call ended at 2 p.m. Ines: "What's the pot, what are the odds, and who at this table knows more than you?" Theo opens the credit agreement; the RFQ timer has 11 seconds left. Question the chapter answers: *who is selling, why now, and what is that worth?* Then "By the end of this chapter you will be able to..."

- **1.1 The Epistemological Clash (keep; tighten).** [F] Add the three-term reading of the bid equation and a forward pointer map.

- **1.2 The Market Set (keep table; add two rows).** Add rows for *Insurers / annuity writers (ratings- and capital-constrained; private-placement tilt)* and *Open-end HY mutual funds & bond ETFs (NAV-redemption sellers)*. Add a "What they are forced to do, and when" column.

- **1.3 The Bid Equation, Derived.** [D][S] CARA/mean-variance reservation bid $\Rightarrow$ $B^* = m - \tfrac12\gamma\sigma^2_{\text{IDO}}h(2q+\Delta q)$; Glosten–Milgrom conditioning $\Rightarrow$ $m = S_t - \pi J$. First `### Specification for AI Implementation` (the `reservation_bid` function with units and tests). Poker Table box (Ines). Ways This Blows Up box (Kaz: the Gaussian CE ignores jump-to-default; pointer to Ch 18).

- **1.4 The Anthology, Part A: Measuring the Risk You Catch (Ben Dor; Veronesi).** [X][D] DTS: proportional spread changes, $\sigma(r^{\text{xs}}) \approx \text{DTS}\cdot\sigma_{\text{rel}}$, crisis steepening; LCS as the cost of catching. Extractions from Ben Dor p.61, p.39, p.26; Veronesi p.120 on which rate you take durations against. Desk Myth vs Desk Reality: "spread duration is the risk measure."

- **1.5 The Anthology, Part B: Pricing the Default You Might Be Catching (Bohn–Stein; Schmid; Bolder; BlackRock; Blackstone).** [X][D] Distance-to-default and the empirical DD→EDF map; intensity models and the credit triangle $s \approx \lambda(1-R)$ under $\mathbb{Q}$; one-factor threshold correlation. Extractions from Bohn–Stein p.128, p.138; Schmid p.15, p.128; Bolder p.597; BlackRock p.6 (77% of defaults flagged within 24 months); Blackstone p.1 (DCI/KMV lineage). Kaz gag #5 lands here.

- **1.6 The Anthology, Part C: Which Flows Are Harvestable (Dynkin; Man 2022; Man 2023; Nuveen; Paleologo).** [X] Fallen-angel reversal as structural segmentation (Ben Dor p.349; Dynkin p.158, p.361, p.396, p.135), equity momentum in credit (Dynkin p.606; Man p.31), Man's IR ladder (p.28), electronification as the enabling condition (Man 2023 p.2–5), z-scores and regimes (Nuveen p.4), and the discipline of IDO (Paleologo p.111, p.139, p.38). **Trend Watch #1: Electronification and portfolio trading, 2018–2026** (dated figures in §6.A–B). **Trend Watch #3 (strategy trend): Equity-momentum-in-credit and the replication crisis** (Dynkin deciles; Man IRs; Dickerson–Mueller–Robotti 2023; Dickerson–Robotti–Rossetti 2026).

- **1.7 The Anthology, Part D: Where the Flows End Up (Moyer; Houlihan Lokey).** [X] Forced sellers of post-reorg equity (Moyer p.370), CDO operating rules (p.55), fallen-angel forced sellers and forced *buyers* (p.35), trade claims (p.310); 363 free-and-clear (HL p.35). Docket Diary box: Serta timeline (2016 → 2020 → Dec 31 2024 → Jul 7 2026). Cooperation-agreement counter starts at 1 if the writer mentions one; otherwise leave for Part IV.

- **1.8 The Ecosystem as a Forced-Seller Flow Graph.** [D][S][C] The holder × trigger matrix; expected forced supply; absorption capacity; a linear temporary-impact model with decay that reproduces the Ellul/Ben Dor drop-and-reversal. Second `### Specification for AI Implementation`: the `forced_seller_graph` engine with its conservation check. **Trend Watch #2: Who holds credit now, 2003 → 2026** (CLO share of loans ~3% → >20% → ~65%; life insurers' private placements 14% → 22% of corporates, 37% → 48% of all bonds; US bond ETFs ~\$2tn; non-bank LPs 26% of global markets revenue; dealer inventories ~1% of outstanding). Case Study A: Ford and the March 2020 fallen-angel wave. Case Study B: March 12, 2020, LQD at a 5.0% discount and the SMCCF.

- **1.9 Toxic Flow: When the Seller Knows (bridge to Ch 3 and Part IV).** [C] Case Study C: Serta 2020 as the market maker's nightmare: the counterparties who had been on the call. **Trend Watch #4: LMEs as a share of defaults, 2024–2026** (>60–68% in 2024; ~65% in 2025; 1-in-4 soft defaults re-default). Ines's hand history: replay the RFQ through markouts.

- **1.10 Desk Debrief** (5–8 bullets), **The Spec You Hand the Robot** (the flow-graph + bid engine, prompt-ready), **Exercises** (3–6).

- **Deep-Dive Resource Graph** at the end of §1.3, §1.6, §1.8 and the chapter (see §9).

---

## 3. Derivation skeletons

### 3.1 The dealer's reservation bid (measure: $\mathbb{P}$, the desk's own beliefs)

Setup: inventory $q$ (notional, long positive) in a bond with current mid $S_t$; residual (post-hedge) P&L variance per unit time $\sigma^2_{\text{IDO}}$; holding horizon $h$ years; CARA risk aversion $\gamma$ with Gaussian P&L, so certainty equivalent $= \mathbb{E} - \tfrac12\gamma\,\mathrm{Var}$. Let $m = \mathbb{E}^{\mathbb{P}}[S_{t+h}\mid \mathcal{F}_t, \mathcal{O}_t]$ be the conditional fair value *given the order*.

Indifference between not trading and buying $\Delta q$ at price $B$:

$$
(q+\Delta q)\,m - B\,\Delta q - \tfrac12\gamma\sigma^2_{\text{IDO}}h\,(q+\Delta q)^2 \;=\; q\,m - \tfrac12\gamma\sigma^2_{\text{IDO}}h\,q^2
$$

$$
\Rightarrow\quad B^{\text{res}} \;=\; m \;-\; \tfrac12\,\gamma\,\sigma^2_{\text{IDO}}\,h\,(2q+\Delta q). \tag{1.1}
$$

Glosten–Milgrom conditioning: with probability $\pi$ the seller is informed and expects $S_{t+h} = S_t - J$ (the post-event mark, e.g. after an LMT or an 8-K); with probability $1-\pi$ the seller is a liquidity/forced seller and $\mathbb{E}[S_{t+h}] = S_t$. Then

$$
m = S_t - \pi J, \qquad
B^* = S_t - \underbrace{\pi(\mathbf{x})\,J}_{\Lambda_{\text{tox}}} - \tfrac12\gamma\sigma^2_{\text{IDO}}h\,(2q+\Delta q) - c(\Delta q), \tag{1.2}
$$

with $\pi(\mathbf{x}) = \big(1+e^{-\theta^\top \mathbf{x}}\big)^{-1}$ on features $\mathbf{x}$ = (size, minutes since the lender call, days to earnings, counterparty type, dealers in competition, counterparty's past markouts), and $c(\Delta q)$ the hedge half-spread plus expected liquidation cost (the LCS of Ben Dor Ch 5 is one estimate). This is exactly the seed's formula with $\sigma^2 h$ written as per-horizon variance.

Error-prone spots: (i) units: $S$ per 100 of par and $q$ in millions gives $B$ in nonsense units unless $\gamma$ is per \$ of P&L; (ii) $h$ in days with $\sigma$ annualized; (iii) using total bond variance instead of residual variance after the CDX/UST/ETF hedge (that is Ch 8's job); (iv) conditioning twice (if $m$ already conditions on the RFQ, do not subtract $\pi J$ again); (v) the $\Delta q^2$ term is routinely dropped, which under-skews large RFQs; (vi) Gaussian CE with jump-to-default is wrong; small-$\gamma$ expansion gives an extra $q\lambda L h$ term (Ch 18). All expectations are $\mathbb{P}$; $S_t$ may come from a $\mathbb{Q}$ model, but the markout is a $\mathbb{P}$ object.

### 3.2 DTS: spread changes are proportional to spread (measure: none; empirical)

Excess return over duration-matched Treasuries: $r^{\text{xs}} \approx -D^{\text{spr}}\,\Delta s$. If $\Delta s = s\,\varepsilon$ with $\varepsilon$ the relative spread change, $\mathrm{sd}(\varepsilon)=\sigma_{\text{rel}}$ stable across sectors and time (Ben Dor p.39: 5% to a bit over 10% per month), then

$$
\sigma(r^{\text{xs}}) \approx D^{\text{spr}}\, s\,\sigma_{\text{rel}} = \text{DTS}\cdot\sigma_{\text{rel}}, \qquad
\text{exposure to a sector's relative move} = \sum_i w_i D^{\text{spr}}_i s_i. \tag{1.3}
$$

Issuer limit: cap $w_i D_i s_i \le \kappa$ (Ben Dor p.61's worked example: 5 = 1% at 100 bp × 5y, 0.33% at 150 bp × 10y). Error spots: spread duration, not modified duration; OAS for callables; state units (bp vs decimal: the relative vol is unitless, DTS is years×spread); the slope steepens in crises (Ben Dor p.26); for bonds quoted on dollar price (distressed), $s$ loses meaning and the risk moves to price/recovery space, which is the Mags objection and the Part IV hand-off.

### 3.3 Distance to default and its mapping (measure: $\mathbb{P}$ for DD/EDF; $\mathbb{Q}$ for $d_2$)

Merton: $E_t = V_t N(d_1) - F e^{-r(T-t)} N(d_2)$, $d_{1,2} = \dfrac{\ln(V_t/F) + (r \pm \tfrac12\sigma_V^2)(T-t)}{\sigma_V\sqrt{T-t}}$. The physical distance to default replaces $r$ with the asset drift $\mu_V$:

$$
\text{DD}_t = \frac{\ln(V_t/F) + (\mu_V - \tfrac12\sigma_V^2)(T-t)}{\sigma_V\sqrt{T-t}}, \qquad
\text{PD}^{\mathbb{P}}_{\text{BSM}} = N(-\text{DD}). \tag{1.4}
$$

Bohn–Stein p.138: most public firms have DD > 4, which Gaussian maps to ~0.00003; MKMV's empirical map turns DD = 4 into an EDF of "almost 1 percent." Error spots: $\sigma_E \ne \sigma_V$ (need $\sigma_E E = \sigma_V V N(d_1)$, Ch 23); $\mu_V$ vs $r$; the default point convention (short-term liabilities plus half of long-term is the commonly reported KMV choice; mark as such); one-year horizon.

### 3.4 The credit triangle (measure: $\mathbb{Q}$)

Constant hazard $\lambda$, flat $r$, continuous premium, recovery $R$ of par at default:

$$
\text{PV}_{\text{prot}} = (1-R)\int_0^T \lambda e^{-(r+\lambda)t}\,dt,\quad
\text{PV}_{\text{prem}} = s\int_0^T e^{-(r+\lambda)t}\,dt
\;\Rightarrow\; s = \lambda(1-R) \tag{1.5}
$$

exactly in this idealization; with quarterly ACT/360 accrual it is approximate. Error spots: feeding a $\mathbb{P}$ EDF into (1.5); $\lambda^{\mathbb{Q}}/\lambda^{\mathbb{P}}$ is well above 1 for IG (state as "commonly reported," derive the ratio in Ch 6); "40% recovery" is a CDS convention, not a fact (Ch 5).

### 3.5 The forced-seller flow graph and the drop-and-reversal (measure: $\mathbb{P}$)

Holder types $i=1..n$, bond segments $k$, triggers $\tau \in \{\text{IG}\to\text{HY},\ \to\text{CCC},\ \text{default},\ \text{NAV outflow of } x\%\}$. Holdings $H_{k,i}$ (par), forced-sale fraction $f_{i}(\tau)$ over response window $w_i(\tau)$ (insurers: quarters; index funds: the month-end rebalance; CLOs: when the bucket binds; open-end funds: days). Expected forced supply and net imbalance:

$$
Q^{\text{sell}}_k(\tau) = \sum_i H_{k,i}\, f_i(\tau), \qquad
I_k(\tau) = Q^{\text{sell}}_k(\tau) - \sum_j A_{k,j}(\tau), \tag{1.6}
$$

where $A_{k,j}$ is natural-buyer capacity (HY funds' forced *buying* at index inclusion, Moyer p.35; systematic fallen-angel programs; dealers' balance sheet). Price with a permanent (information) and a temporary (pressure) component:

$$
p_t = p^* - \kappa\,\frac{\max(I,0)}{\text{ADV}}\, e^{-\theta (t - t_0)}, \qquad t \ge t_0, \tag{1.7}
$$

so the expected 6-month return to the buyer at $t_0$ is the recovered temporary component, which is what Ben Dor p.349 and Dynkin p.158 document and Ellul et al. (2011) identify with insurer concentration. Error spots: double-counting holders (a CLO's loan is not also the bank's); window alignment (insurer sales are slow, index sales are a date); $\kappa$ is not stable across regimes; absorption capacity collapses exactly when supply peaks (March 2020), so $A$ must be state-dependent; and the model is silent on the permanent component, which is where the toxicity term of (1.2) lives.

---

## 4. Code spec (reference implementation for §1.3 and §1.8)

One Python module, numpy/pandas only, seeded. Three public functions and one engine class.

1. `reservation_bid(S, q, dq, gamma, sigma_ido, h_years, pi, J, c=0.0) -> float` implements (1.2). Inputs: `S` price per 100, `q`/`dq` in \$mm par, `sigma_ido` in price points per $\sqrt{\text{year}}$, `gamma` per \$mm² of P&L. Guards: `dq > 0`, `0 <= pi <= 1`, `h_years > 0`. Built-in checks: `B <= S` when `q >= 0`; `dB/dq < 0`; `dB/dpi < 0`; with `pi = q = 0`, `B == S - c` to 1e-12.

2. `dts_vol(D_spr, s_bp, sigma_rel) -> float` implements (1.3) in bp of excess return per period. Built-in check: a seeded Monte Carlo of lognormal spread moves, $\Delta s = s(e^{\sigma_{\text{rel}}Z - \sigma_{\text{rel}}^2/2}-1)$, over 200k draws reproduces $\sigma(-D\Delta s)$ within 2% of `dts_vol` for $\sigma_{\text{rel}} \le 0.10$.

3. `glosten_milgrom_markout(pi, J, n=200_000, seed=7)` simulates informed/uninformed sellers and returns the average markout; check: equals `pi*J` within 3 standard errors. This is Ines's "hand history" made numeric.

4. `class ForcedSellerGraph`: holds `holdings: DataFrame[segment × holder]` (par, \$bn), `rules: dict[holder -> dict[trigger -> (fraction, window_days)]]`, `capacity: DataFrame[segment × buyer × trigger]`. Methods `forced_supply(trigger, segment)`, `imbalance(...)`, `price_path(I, adv, kappa, theta, days)` per (1.7), and `to_edges()` returning a list of (seller, buyer, size) edges for a graph figure. Shapes: $H \in \mathbb{R}^{n_k \times n_i}$, $f \in [0,1]^{n_i \times n_\tau}$, $A \in \mathbb{R}_{\ge 0}^{n_k \times n_j \times n_\tau}$.

Built-in sanity checks (assert on construction and on `run()`): (a) **conservation**: every unit sold is bought by a named absorber or lands in `dealer_residual`, so `sum(sells) == sum(buys) + dealer_residual` to 1e-9; (b) no holder sells more than it holds (`f <= 1`); (c) with `theta > 0` the price path returns to within 1 bp of $p^*$ by `days = 10/theta`; (d) monotonicity: a larger `pi` never raises the bid; (e) a "March 2020" stress toggle sets all `capacity` to zero and must produce `dealer_residual == forced_supply`. Illustrative calibration only; the chapter must label every number in the demo as *(illustrative)*, except the ones in §6 that carry a source.

---

## 5. Source map (shelf pages, why, and the exact quotation to use)

| Citation | Why | Verbatim quotation (≤60 words) |
|---|---|---|
| Ben_Dor_Quantitative_Credit_Portfolio_Management p.61 | The DTS finding in one sentence | "we demonstrate that spread changes are proportional to the level of spread. Systematic changes in spread across a sector tend to follow a pattern of relative spread change, in which bonds trading at wider spreads experience larger spread changes." |
| Ben_Dor p.39 | Why absolute spread vol is the wrong state variable | "absolute spread volatility is highly unstable and tends to rise with increasing spread. Computing volatilities based on relative spread change generates a more stable time series." |
| Ben_Dor p.26 | Out-of-sample test in 2007–09 | "We find that the relationship between spread and spread volatility remains strongly linear, albeit with a steeper slope." |
| Ben_Dor p.349 | Fallen-angel reversal is segmentation, not overreaction | "The primary driver of this phenomenon does not seem to be overreaction to information, but rather the structural inefficiency stemming from the segmentation between the investment and non-investment-grade markets." |
| Bohn_Stein_Active_Credit_Portfolio_Management p.128 | The structural model's minimal assumption | "we need only stipulate that the market is attempting to fairly value a firm, most typically through its equity." |
| Bohn_Stein p.138 | DD to PD, and why Gaussian fails | "under MKMV's empirical distribution and using the VK model described later in this chapter, a DD of 4 converts into an EDF of almost 1 percent." |
| Schmid_Credit_Risk_Pricing_Models p.15 | Merton in one line (verbatim, including "less then") | "Merton assumes that default occurs when the value of the firm's assets is less then the value of the debt at expiry." |
| Schmid p.128 | Why intensity models exist, and their weakness | "the default time is unpredictable and therefore the behavior of credit spreads for short maturities can be captured more realistically." and "their main draw-back is the missing link between firm value and corporate default." |
| Bolder_Credit_Risk_Modelling p.597 | Correlation is where the complexity lives; Feynman epigraph for the AI-specifier | "If one assumes independence of default, then default risk is entirely idiosyncratic." and "Relaxing this unrealistic choice, however, is the source of most of the complexity in this field." Epigraph on the same page: "What I cannot create, I do not understand." |
| Veronesi_Fixed_Income_Securities p.120 | Which curve durations are measured against | "We will rarely use the variation in the semi-annually compounded yield to maturity for risk management purposes, and rather use the variation in the continuously compounded spot curve." |
| Dynkin_Systematic_Investing_in_Credit p.606 | Equity momentum in credit, the headline numbers (1993–2017) | "It delivered negative average excess return of –4.7% per year between 1993 and 2017. In contrast, the average excess return of the top decile portfolio (D10), with the strongest equity momentum, was +4.01% per year." |
| Dynkin p.158 | Forced selling is not uniform; link to Ellul et al. | "Hence, forced selling should not uniformly affect all issuers. Poor performers during the formation period were more likely to be subject to forced selling and, therefore, to experience a subsequent reversal, unlike top performers." |
| Dynkin p.361 | Sell discipline priced as a probability | "For Baa‐rated debt, the probability that a forced sale will occur at some time over the five‐year horizon is 23.7% if forced to sell upon any downgrade to Ba or lower, and 7.2% under the less aggressive policy of selling upon a downgrade to B or lower." |
| Dynkin p.396 | Why the IG/HY stop-loss is expensive | "only a relatively small proportion of downgraded bonds proceeds to default, while the majority mature at par and generally perform well post‐downgrade." |
| Dynkin p.135 | Sell discipline is part of asset allocation | "the long‐term risk/return performance of a given asset class is determined in part by the sell discipline that is in place for the portfolio." |
| Man_Quantitative_Credit_Alpha_Early_Mover_2022 p.38 | The fallen-angel flow, dated to the rebalance | "When a company is downgraded to below investment grade status by the ratings agencies, it drops out of the index at the next monthly rebalancing and there is a significant wave of forced selling around the event." |
| Man_2022 p.42 | The chapter's aha | "Quant credit is yet to move into distressed debt – this is a high-touch asset class that requires a significant degree of human intervention, but further data capture and analysis around restructurings and recovery may make this possible." |
| Man_2022 p.6 | Quant funds as price makers (verbatim, including "drive") | "The rise of quant credit drive greater liquidity and wider participation in electronic trading platforms, while larger players in quant credit have begun to make markets on the all-to-all electronic platforms, meaning that they are price makers as well as price takers." |
| Man_2022 p.11 | Why cash bonds, not CDS; leverage levels | "breadth is key for quant strategies and is simply not available in synthetic form yet." and "typical leverage for long-short strategies currently active in the market starts at 4-5x" |
| Man_2022 p.28 | IR ladder (chart labels; cite as figure) | "Value IR 2.15 Momentum IR 1.69 Quality IR 1.55 Informed Investor IR 0.79 Final IR 2.35" (backtest; label as model returns) |
| Man_2022 p.31 | The equity→credit spillover | "the only spill-over to achieve meaningful statistical significance is equity Momentum, which generates a higher alpha than corporate bond Momentum itself." |
| Man_Revolutions_in_Credit_Trading_2023 p.2 | Execution was the barrier | "The greatest barriers to systematic approaches breaking through in credit have traditionally been execution and the ability to model transaction costs and liquidity within decades-old manual processes." |
| Man_2023 p.3 | The 90% number | "We have therefore moved from having roughly 30% of our order flow in high yield and 60% in investment grade going through electronic venues, to over 90% of our order flow going through electronic-trading venues." |
| Man_2023 p.4 / p.5 | Two aphorisms | "an optimised portfolio is not optimal if you can't trade it." and "2021 was the year of portfolio trading; 2022 was the year of electronic trading." |
| Blackstone_Systematic_Credit p.1 | The flow-catching machine, in the vendor's words | "The systematic optimizer naturally acts as a contrarian liquidity provider. When credit spreads widen aggressively (often due to market panic rather than fundamental deterioration), the model algorithmically increases credit exposure." |
| BlackRock_Systematic_High_Yield_Credit p.6 | Default avoidance as the defensive core | "Our proprietary probability of default signal that has underpinned all of our credit strategies for over 20 years has successfully identified 77% of the defaulted bonds in the ICE BofA High Yield Index within 24 months of its default since 2010." |
| Nuveen_Multi_Asset_Credit_Quant_Framework p.4 | Z-scores are necessary, not sufficient | "A commonly used metric for assessing credit relative value is the z-score, which indicates the number of standard deviations from the historical average. However, relying solely on this measure is insufficient" |
| Moyer_Distressed_Debt_Analysis p.370 | Post-reorg forced sellers | "Banks and collateralized debt obligations (CDOs) are not natural holders of equity securities." and "when such entities are known to be large holders of the postreorganization equity, other market participants will certainly consider their net sell disposition." |
| Moyer p.55 | CLO operating rules as a sell trigger | "When an investment in the portfolio is downgraded to B– or CCC, the manager may be forced to sell something (again without regard to the portfolio manager's view of fair value) to remain in compliance with the CDO-ORs." |
| Moyer p.35 | Forced sellers and forced buyers at the IG/HY line | "This can result in supply–demand technicals that potentially lead to selling at below "fair value," which exacerbates losses. On the other side of the equation, many BB-oriented asset managers can become "forced" buyers." |
| Moyer p.310 | Trade claims: the forced seller who cannot wait | "The claim holder may not have the financial wherewithal to wait until the completion of a bankruptcy case to realize full value of the claim and thus is a forced seller." |
| Houlihan_Lokey_Distressed_MA p.35 | 363 in one clause | "Under Section 363, for example, a debtor with Court approval may sell assets free and clear of all liens, claims and encumbrances (which attach only to the proceeds of such sales)." |
| Paleologo_Advanced_Portfolio_Management p.111 | Separation of concerns; the fiduciary line | "Performance can be decomposed into systematic and idiosyncratic components. Most importantly, these components are investable." and "your investors are not paying you to replicate the market, ride momentum, or short already shorted stocks." |
| Paleologo p.139 | The motto's parent | "factors can find infinite ways to mar your performance, but cannot tell you how to be profitable." |
| Paleologo p.38 | Why decompose | "any argument in favor of conflating beta and alpha is weaker than the simple argument in favor of decomposing them." |

Also useful but not for quotation: Moyer p.55 Figure 2-18 (CDO share of low-rated loans and bonds, ~3% in 1993 to >20% by 2003), the anchor for Trend Watch #2; Man 2022 p.6 and Man 2023 p.2 Figure 1 (Greenwich MarketView e-trading share 2019–2020, chart only, read approximately); Man 2023 p.4 Figure 4 (protocol mix 2021 vs 2022: disclosed RFQ 48%→42%, PT etc.).

---

## 6. RESEARCH DOSSIER (dated, sourced; CHECK where not fetched)

### 6.A Market size, volume, electronification

1. US corporate bond trading averaged **over \$50bn/day in 2025, the first time on record, +11% vs the 2024 record**; single-day record **\$84.7bn on 30 Sep 2025, 18% of it via portfolio trades**. Coalition Greenwich, Kevin McPartland, "U.S. corporate bond trading in 2025 by the numbers," 27 Jan 2026. VERIFIED: https://www.greenwich.com/node/158274
2. 2025 detail (Coalition Greenwich via The DESK, Lucy Carter, 30 Jan 2026): ADNV **\$51bn (+11%)**; average trade size **\$398k (+8.8%)**; **128,141 trades/day**; **IG e-trading just under 50%** of IG volume, **HY e-trading 32%**, both flat vs 2024; IG e-volume \$20.8bn/day (+11%), HY \$3.9bn (+18%); **disclosed-RFQ share fell to 38.6%**; Tradeweb overtook MarketAxess in IG e-trading. VERIFIED: https://www.fi-desk.com/?p=27374
3. 2024 detail (Coalition Greenwich via The DESK, 21 Jan 2025): ADNV **\$46bn (+21%)**, third straight year of growth; 125,723 trades/day (+17%); avg size \$381k; **daily turnover 0.33% (2021) → 0.44% (2024)**; e-trading **44% overall, 48% IG, 33% HY**; IG dealer revenue 20% electronic, HY 10%; platform share of US IG e-trading **MarketAxess 37%, Tradeweb 34%, Trumid 13%, Bloomberg 11%**; e-PT ADNV \$3.3bn (+76%), ~85% of all PT electronic, **Tradeweb >2/3 of e-PT**; corporate bond ETF ADNV −7% (second annual decline). VERIFIED: https://www.fi-desk.com/coalition-greenwich-e-trading-boom-to-outpace-market-growth-in-2025/
4. Jane Street estimate (Bloomberg, 7 May 2024): IG e-trading **42% in 2023 vs 34% two years earlier; HY 31% vs 25%**; Citadel Securities began IG market making in 2024. CHECK (search summary; page 403): https://www.advisorperspectives.com/articles/2024/05/07/high-tech-trading-race-bond-market-turf
5. Shelf anchors for the time series: Man 2022 p.6 (Greenwich chart, Dec 2018–Dec 2020, IG rising toward the high 30s %, HY low 20s %, read from chart, approximate); Man 2023 p.3 (Man Numeric's own flow 30% HY / 60% IG → >90% electronic by 1 May 2023).
6. TRACE: FINRA page confirms 15-minute reporting since 1 Jul 2005 (NTM 05-28) and a 2022 request for comment on one-minute reporting (RN 22-17); the page does not state a 2002 launch date or dissemination caps (both are standard facts; cite FINRA generally). VERIFIED root: https://www.finra.org/filing-reporting/trace . The PT flag in enhanced TRACE dates from **May 2023** (per Morgan Stanley via The DESK, item 6.B.1).

### 6.B Portfolio trading (the fastest-growing protocol)

1. Morgan Stanley (via The DESK, Dan Barnes, 19 Feb 2026): US PT capped volume **~\$1.3tn in 2025 (+52%)**; uncapped estimate **~\$1.8tn vs \$1.1tn in 2024**; PT share of corporate bond trading **11% (2024) → 15% (FY2025)**, **peak 17% in July 2025**, 16% at year-end; **IG PT \$1.1tn (+44%)**, HY PT **+116%**, Q4 HY PT record **\$56bn**, HY PT share **16% FY, 18% in December**; TTM IG volume \$9.6tn (+5%), HY at a record. VERIFIED: https://www.fi-desk.com/ig-credit-sees-portfolio-trading-plateau-while-hy-hits-records/
2. Barclays (via IFR, 2025): H1 2025 PT **\$823bn (+54%)**; **22% of US IG dealer-to-client volume** (15% H1 2024; 5% 2023); **14% of HY**; **a portfolio trade every six minutes vs every 41 minutes in 2020**; April 2025 monthly record **\$172bn**; MarketAxess total US corporate volume H1 2025 \$6.6tn (+14%); Tradeweb: a single PT with **>4,000 line items**; PT reached 20% of HY activity on some April 2025 days. VERIFIED: https://www.ifre.com/topic-codes/2293541/portfolio-trading-continues-dizzying-growth
3. Tradeweb 2024: PT ~9% of US corporate volume, >\$1tn (Bloomberg, 23 Jan 2025). CHECK (search; paywalled).

### 6.C Non-bank liquidity providers and dealer balance sheets

1. Citadel Securities claims **14.2% market share of IG "block risk transfer," \$406bn traded YTD** (own estimate; Tradeweb and Bloomberg declined comment). The DESK, 8 Oct 2026. VERIFIED: https://www.fi-desk.com/citadel-securities-reveals-glimpse-of-credit-platform-broker-rankings/
2. Non-bank trading firms' revenue pool **\$114bn in 2025 (+45%)**; market-making **\$30.2bn (+20%)**; banks **\$260.7bn (+13%)**; Citadel Securities, Jane Street and Hudson River ~**\$27bn in Q1 2026**. FT/Crisil Coalition Greenwich via Hedgeweek, 3 Jun 2026. VERIFIED: https://www.hedgeweek.com/non-bank-trading-firms-surge-as-jane-street-and-citadel-securities-drive-record-114bn-revenue-pool/
3. BCG: non-banks **26% of global markets revenue in 2024 vs 12% in 2018**; Jane Street 2024 trading revenue **\$20.5bn** (IFR). CHECK (search).
4. Primary dealer corporate inventories fell **~76% from Oct 2007 to \$57.49bn** (Bloomberg, c. 2014) and were **~\$50bn in 2015 vs >\$250bn in 2007** while the market grew ~\$3.2tn → ~\$5tn (St. Louis Fed FRED blog); Better Markets cautions the pre-2013 series included private-label MBS. CHECK; mark *approximate*. Current market: SIFMA puts US corporate bonds outstanding near \$11tn (CHECK; cite SIFMA statistics root https://www.sifma.org/resources/research/statistics/ TITLE-ONLY until fetched).
5. Shelf: Man 2022 p.6 and Man 2023 p.2 on algorithmic market making and quant funds as price makers.

### 6.D ETFs

1. **US fixed income ETF AUM reached ~\$2tn in June 2025**; **\$186bn inflows in H1 2025 (34% of all ETF sales)**; record \$18bn in June. The Daily Upside, 2 Jul 2025. VERIFIED: https://www.thedailyupside.com/etf/industry-news-etf/fixed-income-etf-assets-hit-record-2t/
2. Global bond ETF AUM **~\$2.6tn end-2024, +20% organic**; BlackRock projects **\$6tn by 2030**. CHECK (etf.com; 403).
3. **12 Mar 2020: LQD closed at a 5.0% discount to NAV; 0.19% on 13 Mar**; VCIT 3.2%, SPIB 3.1%. WealthManagement.com, 16 Mar 2020. VERIFIED: https://www.wealthmanagement.com/etfs/under-market-stress-fixed-income-etfs-trade-with-wide-discount . BoE (May 2020) reported several of the largest IG and HY ETFs at >5% discounts in mid-March (CHECK).
4. SMCCF: **established 23 Mar 2020**; broad-portfolio bond buying announced 15 Jun 2020; purchases **ceased 31 Dec 2020**; wind-down announced 2 Jun 2021; eligible: IG issuers as of 22 Mar 2020 and US-listed broad corporate bond ETFs. VERIFIED: https://www.federalreserve.gov/monetarypolicy/smccf.htm . First ETF purchases on **12 May 2020** is widely reported but not on that page; T. Rowe Price says "about a month later, in May." CHECK the exact day.
5. CLO ETFs: **>\$20bn end-2024 from \$2.25bn in 2023; net +\$15bn in 2024 ≈ 7% of \$202bn new issuance**. Deutsche Bank flow, 11 Feb 2025. VERIFIED: https://flow.db.com/trust-and-agency-services/outlook-for-clos-in-2025-reason-for-optimism

### 6.E CLOs (the mechanical holder)

1. **US CLOs ~\$1tn outstanding, ~65% of a ~\$1.5tn institutional leveraged loan market**; captive funds supplied up to **80% of CLO equity for new issues in 2025**; 2025 refi/reset activity at record levels. Maples/Nuveen Q&A, 13 Apr 2026. VERIFIED: https://maples.com/knowledge/bringing-you-closer-an-insightful-clo-qa . Deutsche Bank put outstanding at ~\$1.1tn at the start of 2025 (CHECK).
2. 2024 records: US new issue **\$202bn**, resets **\$223bn**, MM/private credit CLOs **\$38bn**; Europe €48bn new issue; median equity distributions **16% US / 19% Europe**. DB flow (above), VERIFIED. S&P (via American Banker, 14 Feb 2025): 2024 BSL \$163.45bn + MM \$38.50bn; 2025 forecast \$205bn; refi/reset **\$306.94bn (2024) → \$353bn forecast (2025)**; AAA spreads **SOFR+160 (early 2024) → +130 (YE2024) → <+115 (Jan 2025)**; CCC baskets trending down. VERIFIED: https://asreport.americanbanker.com/news/s-p-global-forecasts-record-2025-clo-volume . LSTA/DealCatalyst recap (KBRA, 2 May 2025): ~\$200bn 2024 issuance; ~\$45bn Q1 2025. VERIFIED: https://www.kbra.com/publications/kSrnWLdM
3. Mechanics: typical **7.5% CCC limit; excess carried at market value in the OC test; OC breach diverts cash from equity to seniors; >2/3 of CLOs saw cash diversion in the GFC; European median CCC bucket peaked 10–12%, some 15–20%+; CELF 2006-1 peaked ~22.5% CCC and still repaid rated notes at par.** Vontobel, 20 Mar 2020. VERIFIED: https://am.vontobel.com/insights/clos-lessons-from-the-past
4. Whether breaches *force* sales is contested: 2024 commentary says downgrades do not force sales but managers pre-emptively exit (American Banker, CHECK); Kundu's model of covenant-driven fire sales (sell the highest-priced CCC loans to get back under 7.5%) (AEA materials, TITLE-ONLY: Shohini Kundu, "The Externalities of Fire Sales: Evidence from Collateralized Loan Obligations," CHECK venue/year). S&P (12 Feb 2025) on the Altice France downgrade: CCC buckets up short term, breach unlikely, 7.5% post-reinvestment condition may impair reinvestment (CHECK; 403).
5. Shelf: Moyer p.55 Figure 2-18 (CDO share of low-rated loans and bonds ~3% in 1993 → >20% by 2003) makes the 20-year trend: **~3% → >20% → ~65%**.

### 6.F Insurers (the ratings- and capital-constrained holder)

1. Ellul, Jotikasthira, Lundblad, "Regulatory Pressure and Fire Sales in the Corporate Bond Market," *JFE* 101(3), 2011, 596–620, DOI 10.1016/j.jfineco.2011.03.020: insurers hold **more than one-third of IG corporates**; constrained insurers sell downgraded bonds; price declines then reversals, larger when the sector is stressed. VERIFIED: https://kenaninstitute.unc.edu/?p=1554
2. Life insurers' **private placements rose from 14% (2016) to 22% (2024) of their corporate bond holdings**; private placements "are thinly traded and have limited disclosures," so forced sales "could have an outsized price impact." Chicago Fed Insights, Meisenzahl, Polacek, Overpeck, May 2026. VERIFIED: https://www.chicagofed.org/publications/chicago-fed-insights/2026/assessing-life-insurers-interconnectedness
3. **Privately placed bonds were 48.4% of life-industry bonds at YE2025 vs 37.4% five years earlier**; life general-account bond book **~\$4tn** (72.8% issuer credit obligations, of which 74.1% corporates); NAIC Principles-Based Bond Definition **effective 1 Jan 2025**. S&P GMI via Insurance Business, 10 Aug 2026. VERIFIED: https://www.insurancebusinessmag.com/us/news/life-insurance/private-credit-now-dominates-life-insurer-bonds-as-naic-rewrites-the-rulebook-585542.aspx
4. Offshore loop: reinsurers held **41% of ~\$1.61tn of US reserve credits at YE2025 (vs ~21% in 2016)**; ~56% of ceded annuity reserves offshore; BIS: US life insurers ceded \$2.1tn by 2023 vs \$0.5tn in 2017, 40% offshore. Retirement Income Journal (Oct 2026 archive page, citing AM Best, BIS, IMF). VERIFIED page, figures CHECK against the primary reports. Moody's: **\$807bn of private illiquid bonds at YE2025, top-10 hold 44%** (CHECK). AM Best: life/annuity private credit ~\$1.7tn (2023) (CHECK).
5. Shelf: Man 2022 p.38 (capital charges on speculative-grade holdings); Dynkin p.396 (sell thresholds at higher ratings for insurers and central banks).

### 6.G Fallen angels (the cleanest forced-seller event)

1. **March 2020: >\$90bn downgraded from IG in one month, nearly twice the prior monthly record of \$48bn (2005); H1 2020 \$197bn, the largest on record** (J.P. Morgan data); **Ford's ~\$36bn** downgraded in March 2020; passive IG ETFs must sell once a bond leaves the IG universe; fallen angels have outperformed IG and HY by ~3%+ annualized since 1998 (T. Rowe Price research, approximate). T. Rowe Price, Nov 2020. VERIFIED: https://www.troweprice.com/institutional/ch/en/insights/articles/2020/q4/navigating-fallen-angels-post-coronavirus-landscape.html
2. S&P downgraded Ford on **25 Mar 2020**; its two HY ratings removed **\$35.8bn** from the Bloomberg Barclays IG index at month-end (IFR); S&P counted \$323bn of global fallen-angel debt in H1 2020 vs the 2005 record \$487.86bn; the Fed on **9 Apr 2020** extended eligibility to issuers that were IG as of 23 Mar 2020 (Invesco). CHECK (search summaries).
3. Shelf: Ben Dor Ch 13 (p.327–363), Dynkin Ch 2–4 (p.135–264: FA tilt, capacity, FAR scorecard), Man 2022 p.38, Moyer p.35.

### 6.H LMEs, defaults, and the courts (toxic-flow fuel)

1. **Serta**: Nov 2016 **\$1.95bn** first-lien term loan; June 2020 exchange of **~\$992mm** first-lien loans into **~\$734mm** of "First Lien Second Out" super-priority debt plus **\$200mm new money**; participating lenders held **52.6% of ~\$1.887bn**; excluded lenders **47.4% (~\$895mm)**; **Fifth Circuit, 31 Dec 2024**: not an "open market purchase," sacred right breached; **remand, 7 Jul 2026**: participating lenders liable, **\$261.13mm damages as of 22 Jun 2020 plus 9% NY prejudgment interest**; cashless exchange held to be a "payment." Mayer Brown, Jul 2026. VERIFIED: https://www.mayerbrown.com/en/insights/publications/2026/07/serta-simmons-bedding-the-fifth-circuits-uptier-decision-and-the-landmark-damages-ruling-on-remand . Proskauer, 2 Jan 2025: "An open market is a designated market" (the secondary market for syndicated loans); indemnity struck; expect fewer LMEs relying on the exception. VERIFIED: https://www.proskauer.com/alert/the-end-of-non-pro-rata-uptiers
2. **Mitel**: NY Appellate Division, First Dept., **31 Dec 2024**, unanimously upheld the uptier: the agreement allowed Mitel to "purchase" loans with **no "open market" qualifier**; subordination of non-participants was an "indirect" effect; Mitel filed Chapter 11 March 2025, prepack confirmed April 2025. Mayer Brown, 30 May 2025. VERIFIED: https://www.mayerbrown.com/en/insights/publications/2025/05/serta-and-mitel-the-latest-major-court-decisions-on-uptier-transactions
3. **Wesco/Incora**: Bankruptcy Court (Isgur) ruling **17 Jan 2025** unwound the 2026-notes leg; **District Court (Crane) reversed 8 Dec 2025**, finding the multi-step uptier lawful under both indentures and refusing an implied sacred right; appeal to the Fifth Circuit pending. Mayer Brown, Jan 2026. VERIFIED: https://www.mayerbrown.com/en/insights/publications/2026/01/the-state-of-play-on-uptiers-district-court-reversal-in-wesco-blesses-multistep-transactions
4. Distressed exchanges **>60% of default volume in 2024 YTD, highest since at least 2000**; 2024 default rates **HY 1.4% incl. DEs vs 0.3% excl.; loans 4.0% vs 1.5%**; trailing recoveries on DEs higher than on traditional defaults (48.2% higher for HY, 18.3% for loans). Marquette Associates, 18 Dec 2024. VERIFIED: https://www.marquetteassociates.com/damsel-in-distress/ . JPM: LMEs **68% of 2024** default + DE volume (record), 42% YTD May 2025; Fitch: ~68% of 90 defaulted US issuers in 2024 were DDEs (CHECK).
5. Moody's (18 May 2026): **~65% of 2025 corporate defaults were distressed restructurings**; of 1,173 soft credit events (1979–2026), **~1 in 4 ended in hard default, >1 in 3 in hard default or another distressed event, >70% of eventual hard defaults within two years**; proxy direct-lending default rate **1.6% ex-DE / 4.7% incl.**; US HY one-year PD 3.2% (Q1 2026); baseline spec-grade default rate drifting to 3.2% by YE2026. VERIFIED: https://www.moodys.com/web/en/us/insights/credit-risk/private-credit/lend-extend-and-then.html

### 6.I The systematic credit industry (sizing the competition)

1. Blackstone BCBS: **>\$40bn AUM, DCI acquired late 2020**, structural (KMV-lineage) default models, value + carry + contrarian rebalancing (shelf, Blackstone p.1; no date on the document; label "as stated in the paper").
2. Man Group active credit AUM **\$59.6bn as at 30 Jun 2026** (includes Man Varagon direct lending; unlevered; overlaps). VERIFIED: https://www.man.com/credit-capabilities . Man 2023 paper authors: Robert Lam and Paul Kamenski; >90% of Man Numeric flow electronic as of 1 May 2023. VERIFIED: https://www.man.com/insights/revolutions-in-credit-trading
3. **Ares acquiring BlueCove (~\$5.5bn AUM, 60-person team), announced 31 Oct 2025, closing Q1 2026**; Ares Credit Group ~\$377bn; Kipp deVeer cites the "quantitative credit investment revolution." VERIFIED: https://www.fi-desk.com/ares-acquires-bluecove-launches-systematic-credit-strategy/
4. Robeco (Sept 2026, PDF unreadable): eVestment shows **quant strategies ~6.5% of fixed income AUM in 2026**. CHECK. Bloomberg (May 2024) "It's PhDs vs. MBAs in credit investing as quants jump in" (TITLE-ONLY; 403).

### 6.J Factor research and the replication crisis (for Trend Watch #3)

1. Dickerson, Mueller, Robotti, "Priced risk in corporate bonds," *JFE* 150(2), 2023, art. 103707 (DOI resolves): previously proposed bond factors, with traded liquidity the only marginal exception, add nothing over the bond market factor; **Fama–DFA Prize**; Bai–Bali–Wen (JFE 2019) **retracted in 2023** after a one-month timing error. CHECK the retraction wording (search summary).
2. Dickerson, Robotti, Rossetti, "The Corporate Bond Factor Replication Crisis," arXiv:2604.07880, **9 Apr 2026**: 108 signals in nine clusters; measurement error in transaction prices and asymmetric ex-post return filtering inflate premia; **"the majority of previously documented factors do not produce statistically significant bond CAPM alphas after correction."** VERIFIED: https://arxiv.org/abs/2604.07880 . Open Source Bond Asset Pricing (error-corrected TRACE, 108 factors, BBW corrected factors, trace-data-pipeline on GitHub; Dickerson, Mueller, Robotti, Julliard, Nozawa, Rossetti, Fang). VERIFIED: https://openbondassetpricing.com/
3. Kelly, Palhares, Pruitt, "Modeling Corporate Bond Returns," *JF* 78(4), 2023, 1967–2008, DOI 10.1111/jofi.13233 (resolves; page 403): conditional five-factor model with time-varying loadings. CHECK pages.
4. Jostova, Nikolova, Philipov, Stahel, "Momentum in Corporate Bond Returns," *RFS* 26(7), July 2013 (momentum concentrated in non-IG). VERIFIED title/volume: https://academic.oup.com/rfs/article-lookup/doi/10.1093/rfs/hht022
5. Kargar, Lester, Lindsay, Liu, Weill, Zúñiga, "Corporate Bond Liquidity during the COVID-19 Crisis," *RFS* 34(11), 2021. VERIFIED title/volume: https://academic.oup.com/rfs/article/34/11/5352/6279757 (authors from general knowledge; CHECK).
6. TITLE-ONLY (not fetched; do not give links): Haddad, Moreira, Muir (2021), *When Selling Becomes Viral: Disruptions in Debt Markets in the COVID-19 Crisis and the Fed's Response*, RFS; O'Hara and Zhou (2021), *Anatomy of a Liquidity Crisis: Corporate Bonds in the COVID-19 Crisis*, JFE; Goldstein, Jiang, Ng (2017), *Investor Flows and Fragility in Corporate Bond Funds*, JFE; Choi, Hoseinzade, Shin, Tehranian (2020), *Corporate Bond Mutual Funds and Asset Fire Sales*, JFE; Bessembinder, Jacobsen, Maxwell, Venkataraman (2018), *Capital Commitment and Illiquidity in Corporate Bonds*, JF; Moskowitz, Ooi, Pedersen (2012), *Time Series Momentum*, JFE; Houweling and van Zundert (2017), *Factor Investing in the Corporate Bond Market*, FAJ 73(2); Israel, Palhares, Richardson (2018), *Common Factors in Corporate Bond Returns*, JIM; Ambrose, Cai, Helwege (2008), *Forced Selling of Fallen Angels*, JPM; Coval and Stafford (2007), *Asset Fire Sales (and Purchases) in Equity Markets*, JFE; Lee, Naranjo, Sirmans (2021), *CDS Momentum*, Review of Asset Pricing Studies (CHECK).

### 6.K Private credit (the holder that is eating the public market)

1. Preqin: private credit AUM **~\$2.28tn in 2025, projected \$4.5tn by 2030** (S&P GMI, 13 Nov 2025; CHECK, 403); ACC/Houlihan Lokey: **\$3.5tn end-2024 (+17%)** (CHECK). Definitions differ (dry powder, leverage, BDCs). Moody's direct-lending default proxy 1.6%/4.7% (VERIFIED above).

### 6.L Trend data for the two mandatory Trend Watch boxes (ready to paste, with the sources above)

- **Trend Watch #1 (execution):** e-trading share IG ~34% (2021) → 42% (2023) → ~48–50% (2024–25); HY ~25% → 31% → 32–33%; PT share 5% of IG D2C (2023) → 15% (H1 2024) → 22% (H1 2025); PT overall 11% (2024) → 15% (2025), peak 17% (Jul 2025); ADV \$46bn (2024) → >\$50bn (2025); one PT every 41 minutes (2020) → every 6 minutes (2025); Man Numeric 30/60% → >90% electronic (2023).
- **Trend Watch #2 (holders):** CLO share of leveraged loans ~3% (1993) → >20% (2003) → ~65% (2026), ~\$1tn of ~\$1.5tn; CLO ETFs \$2.25bn (2023) → >\$20bn (2024); US bond ETFs ~\$2tn (Jun 2025); life insurers' private placements 14% → 22% of corporates (2016–2024), 37.4% → 48.4% of all bonds (2020–2025); reinsurers 21% → 41% of reserve credits (2016–2025); non-banks 12% → 26% of global markets revenue (2018–2024); dealer inventories from >\$250bn (2007) to ~\$50bn (2015), approx.

---

## 7. Case studies (sourced key facts)

**A. Ford and the March 2020 fallen-angel wave (the flow graph lights up).** S&P cut Ford to junk on 25 Mar 2020 (CHECK date); ~\$36bn of debt left the IG index at month-end (T. Rowe Price, VERIFIED; IFR says \$35.8bn, CHECK); March 2020 saw >\$90bn of fallen-angel debt vs a \$48bn prior monthly record, \$197bn by June (J.P. Morgan via T. Rowe, VERIFIED); the Fed's SMCCF (23 Mar 2020, VERIFIED) and the 9 Apr 2020 extension to issuers IG as of 23 Mar (CHECK) turned a forced-seller event into a forced-buyer event. Teaching point: the index date is known; insurer selling is slow; HY index funds are forced *buyers* at inclusion (Moyer p.35); the systematic desk's job is to estimate $Q^{\text{sell}}$ by holder and the absorption $A$ by date. Pair with Ben Dor p.349 and Dynkin p.158. How a desk flags it: DD collapsing in February (Bohn–Stein p.128 logic), equity momentum bottom decile (Dynkin p.606), CDS–cash basis blowout (Ben Dor p.363).

**B. 12 March 2020: LQD at a 5.0% discount and the SMCCF (the arbitrage band breaks).** LQD closed at a 5.0% discount to NAV on 12 Mar 2020 and 0.19% on 13 Mar; VCIT 3.2%, SPIB 3.1% (WealthManagement, VERIFIED). The SMCCF was established 23 Mar 2020 and bought broad corporate bond ETFs; purchases ceased 31 Dec 2020 (Fed, VERIFIED); first ETF buys in May 2020 (12 May widely reported, CHECK). Teaching point: the ETF price led the stale NAV; APs stop arbitraging when they cannot sell the basket; the bid equation's $\sigma_{\text{IDO}}$ and $c(\Delta q)$ terms exploded together. Hand off to Ch 20.

**C. Serta 2020 → 2026 (the counterparty who knew).** Facts in §6.H.1 (VERIFIED). Teaching point for Chapter 1: an RFQ to sell first-lien paper in the weeks before 22 Jun 2020 from an account that was in the negotiating group is the purest toxic flow; $\pi$ is not a prior, it is a function of who is on the call. The damages ruling (\$261.13mm plus 9%) prices the sacred right ex post; the market maker had to price it ex ante. Docket Diary box with the four dates; the Ad Hoc Group speaks once.

---

## 8. Humor beats (all ride on a correct idea)

1. **Cold open, gag #1.** Theo's 13-week model has 13 columns; the RFQ has an 11-second timer. Ines: "One of those is going to be reborn. Guess which." (Sets up the 13-week model's return as a survival curve in Ch 5.)
2. **Kaz, gag #5.** On hearing "fulcrum security": "A fulcrum is where the lever balances, so it is the tranche with zero duration?" Mags: "It is the tranche that gets the equity and the lawsuits." (Teaches: fulcrum = the class whose recovery straddles the enterprise value.)
3. **Ines's Poker Table.** "An RFQ from a lender who was on the 2 p.m. call is a raise from a player who just looked at the river card. You do not need to know what he saw. You need to know he saw it." (Teaches: $\pi(\mathbf{x})$ depends on observable counterparty state, not on the bond.)
4. **Mags, gag #7.** "Back in my day a portfolio trade was a fax with forty CUSIPs and a prayer. Now it is four thousand line items and no prayer." Then, grudging: "The pricing is better. I hate it." (Barclays/Tradeweb facts.)
5. **ROBO, gag #2.** Vague spec: "map the forced sellers." ROBO returns a one-node graph labeled "Everyone, March 2020." Precise spec follows: holders, triggers, windows, capacities, conservation check.
6. **"IDO or it didn't happen," gag #8.** Theo: fallen angels return "3% a year over HY." Kaz: strip the HY beta, the DTS, and the index-inclusion bid, then tell me. (Teaches Paleologo's decomposition, and that the FA premium is partly a flow you have to be there for.)
7. **"Open market purchase," gag #4.** "The three most expensive words in finance: \$261.13 million, plus nine percent, compounding since June 2020, for a phrase nobody defined." (Serta remand.)
8. **The Ad Hoc Group.** In unison, in a Rule 2019 statement: "We were represented by counsel. We were not, the Fifth Circuit has now clarified, represented in an open market." (Cooperation agreements signed in this book so far: 0; the counter starts in Part IV.)
9. **CLO one-liner.** "A CLO is a buy-and-hold investor with a 7.5% allergy. It does not sell because it wants to. It sells because the indenture sneezes." (Vontobel mechanics; Moyer p.55.)
10. **Kaz's Gaussian, gag.** "Let's just assume Gaussian." Bohn–Stein p.138: a DD of 4 is a 0.003% default under the normal and almost 1% under MKMV's map. Kaz: "...I regret it already." (Ways This Blows Up.)

---

## 9. Resource-graph candidates

**Podcasts** (TITLE-ONLY unless noted): Bloomberg *Odd Lots*, "Under the Hood of the \$8 Trln Corporate Bond Market" with Chris White (2015, TITLE-ONLY) and its later Chris White episode on odd-lot desks (2019, TITLE-ONLY); any 2023–2025 *Odd Lots* episodes on portfolio trading, LMEs, or private credit (TITLE-ONLY, CHECK titles before naming); *Flirting with Models* (Corey Hoffstein), site VERIFIED-URL https://www.flirtingwithmodels.com/ , no credit episode confirmed on the landing page, name episodes TITLE-ONLY; S&P Global *Capital Markets Connect* podcast on portfolio trading (~12% of IG volume via PT, TITLE-ONLY); Risk.net podcast with MarketAxess on liquidity scores in portfolio trading (TITLE-ONLY).

**Practitioner writing:** Coalition Greenwich MarketView credit notes (VERIFIED-URL: greenwich.com/node/158274); The DESK coverage of e-trading and PT (VERIFIED-URLs in §6.A–B); IFR on portfolio trading (VERIFIED-URL); Man Institute, *The Revolutions in Credit Trading* (VERIFIED-URL: https://www.man.com/insights/revolutions-in-credit-trading); Man Group, *Quantitative Credit: Alpha Opportunities for Early Movers* (2022, on the shelf; TITLE-ONLY for the web); Proskauer, Mayer Brown, Jones Day alerts on Serta/Mitel/Wesco (VERIFIED-URLs in §6.H); Marquette, *A Damsel in Distress* (VERIFIED-URL); Moody's, *Lend, extend, and then...* (VERIFIED-URL); Chicago Fed Insights on life insurers (VERIFIED-URL); Vontobel, *CLOs: Lessons From The Past* (VERIFIED-URL); Deutsche Bank flow, *Outlook for CLOs in 2025* (VERIFIED-URL); Maples CLO Q&A (VERIFIED-URL); T. Rowe Price on fallen angels (VERIFIED-URL); Matt Levine, *Money Stuff* (TITLE-ONLY); PETITION (site redirects to petition11.com, TITLE-ONLY until fetched); AQR Insights and Barclays QPS (TITLE-ONLY).

**Academic papers:** Ellul–Jotikasthira–Lundblad 2011 (VERIFIED-URL via Kenan listing; DOI 10.1016/j.jfineco.2011.03.020); Dickerson–Robotti–Rossetti 2026 (VERIFIED-URL arXiv:2604.07880); Dickerson–Mueller–Robotti 2023 (DOI 10.1016/j.jfineco.2023.103707 resolves; page not opened); Kelly–Palhares–Pruitt 2023 (DOI 10.1111/jofi.13233 resolves; page not opened); Jostova et al. 2013 (VERIFIED-URL OUP lookup); Kargar et al. 2021 (VERIFIED-URL OUP); all others in §6.J.6 TITLE-ONLY.

**Data & code:** Open Source Bond Asset Pricing (VERIFIED-URL https://openbondassetpricing.com/ ; GitHub trace-data-pipeline referenced there); FINRA TRACE (VERIFIED-URL https://www.finra.org/filing-reporting/trace); Federal Reserve SMCCF page (VERIFIED-URL); SEC EDGAR root https://www.sec.gov/edgar (canonical); CourtListener REST API https://www.courtlistener.com/help/api/ (canonical); Fed Z.1 Financial Accounts root https://www.federalreserve.gov/releases/z1/ (canonical root; holder shares not fetched, CHECK before quoting numbers); SIFMA statistics (TITLE-ONLY).

---

## 10. Exploratory-space notes (future sections and chapters)

1. **Chapter 1-B, "The Holder Map."** A dated, sourced table of who owns US corporates and loans (Fed Z.1 by sector; CLO share of loans; insurer private-placement share; ETF AUM; dealer net positions) with the trigger and window for each holder, refreshed every edition alongside Appendix C. The flow-graph engine of §4 becomes its code. Needs the Z.1 fetch we could not do this session.
2. **Insurers and the offshore reinsurance loop as a credit-demand engine.** The 14% → 22% / 37% → 48% private-placement migration, the PBBD rule (1 Jan 2025), reserve credits 21% → 41% reinsured, and what it does to IG new-issue demand and fallen-angel supply. Fits after Ch 17 (public–private convergence) or as a new chapter in Part IV.
3. **The corporate bond factor replication crisis.** DMR 2023, the BBW retraction, DRR 2026's 108-signal zoo, and Open Bond Asset Pricing as the book's default research dataset. Deserves a full chapter after Ch 9 (and a data appendix entry), with a section on which *trend/momentum* constructions survive error correction.
4. **Captive CLO equity, resets, and CLO ETFs.** 80% of 2025 CLO equity from captive funds; resets \$223bn (2024) → forecast \$353bn (2025); CLO ETFs \$2.25bn → >\$20bn in one year; the implication for loan demand elasticity and for the CCC-bucket sell trigger. Extend Ch 21.
5. **Re-default hazards after soft credit events.** Moody's 1,173-event sample (1 in 4 hard default; >70% within two years) as a competing-risks model; recovery compression after LMEs. Extend Ch 14, link to the Priming Risk Score.
6. **Non-bank liquidity provider economics.** Citadel Securities' 14.2% block-risk-transfer claim, the \$114bn non-bank revenue pool, and how an algorithmic IG market maker's bid equation differs from a bank's (capital, inventory horizon, ETF hedge). Extend Ch 2 and Ch 18.
7. **The TRACE portfolio-trade flag (May 2023) as a data source.** PT identification lets a desk measure PT adverse selection directly; Ch 19 should build on it.
8. **April 2025 tariff volatility as a liquidity case study.** PT monthly record \$172bn; HY PT 20% of activity on some days; e-trading held up (Man 2023's thesis that stress accelerates electronification). Ch 19–20 case study candidate.
9. **Quant credit in distressed.** Man 2022 p.42 says it has not happened; the book's Part IV is the argument that it can. Chapter 1 should promise it and Ch 13–16 should deliver the codification.
10. **Open research questions to chase next edition:** Fed Z.1 holder shares (exact 2025 numbers); the May 12, 2020 SMCCF ETF purchase date; Jane Street/Citadel Securities credit shares from a non-self-reported source; the Altice France CLO exposure figures; the Robeco/eVestment 6.5% quant share; a verified Odd Lots episode list on credit market structure; CDX index volumes 2025; HYG/LQD/JAAA AUM at YE2025.

<!-- STATUS: COMPLETE -->
