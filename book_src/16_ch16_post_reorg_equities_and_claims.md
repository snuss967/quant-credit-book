# Chapter 16: Post-Reorganization Equities, Rights Offerings & Bankruptcy Claims

> *"The latter, of course, suggests that knowledgeable insiders had a strong view that the equity was undervalued."* (Moyer_Distressed_Debt_Analysis p.374)

## Cold Open: Effective Date, 9:31 a.m.

Tuesday, 9:31 a.m. A trucking-and-warehousing company that yesterday existed only as a first-lien term loan opens on the OTC market as common stock. The new ticker is five consonants long. At the plan's equity value the market cap is \$140mm. (The company and its numbers are fictional; the mechanics are not.)

"Eleven bids," Theo says. "One offer."

"Whose offer?" Ines doesn't look up.

Theo has three windows open: the plan's distribution schedule, the ad hoc group's Rule 2019 statement, and a CLO trustee report he still has from his old life. "A CLO manager. They held twenty-two percent of the term loan. Now they hold twenty-two percent of the equity, and their indenture carries equity at zero in the overcollateralization test."

"So every share they keep costs them cushion and pays them nothing." Now Ines looks. "What's the pot, what are the odds, and who at this table is *required* to fold, and by when?"

"I've been reading the disclosure statement," Kaz says. "It says the first-lien lenders were the fulcrum. Is that a gymnastics term?"

"It's the class where the value runs out," Theo says. "The debt above it gets paid, the debt below it gets warrants and apologies, and the fulcrum gets the company."

"So it's the point where the beam balances." Kaz considers this. "Mechanically, that's correct. Why does the beam want to sell itself?"

Mags arrives with coffee and the air of someone who has seen this film. "In 2003 we called these back-end equities. We bought them by phone from people who were embarrassed to own them. The trick was never the valuation. The trick was knowing who *had* to sell and waiting for them to get bored."

"We don't wait for people to get bored anymore," Ines says. "We model how fast they get bored."

Theo looks at the screen. The plan says \$140mm. The bids say less. The CLO's offer sits there like a confession. Somewhere in this stock's first ninety days there is a return. The desk's question is how much of it is a *flow we can schedule*, meaning a known seller working down a known position against slow-arriving capital, and how much is *value we have to underwrite* the old way, with a model of a trucking business and a strong stomach.

By the end of this chapter you will be able to: (1) map every security a plan of reorganization distributes to the holder who is forbidden to keep it; (2) model forced selling as a decaying supply process and turn it into a signal with a built-in expiry date; (3) price a rights offering as a call and its backstop as a put, and decompose the backstop party's all-in take; (4) price long-dated plan warrants with dilution and back out the volatility a plan implicitly assumed; (5) value a bankruptcy claim whose denominator is a random variable, and trade a 503(b)(9) claim against a general unsecured claim as a pure bet on pool risk; and (6) walk Hertz from its 2020 filing to its 2026 return to the restructuring room, instrument by instrument.

A word on measures before we start. None of these instruments has a liquid hedge on the day it is born. Every expectation in this chapter is therefore under the physical measure $\mathbb{P}$ unless we say otherwise, and any $\mathbb{Q}$ that appears is the measure of some traded proxy (when-issued stock, peer equities, the high-yield index), not a true risk-neutral measure for the instrument itself. Kaz will try to write $\mathbb{E}^{\mathbb{Q}}$ out of habit. We will stop Kaz.

A word on notation, too. Arbitrage capital is $M_t$ (not $K$, which is a strike in §16.3); the warrant dilution ratio is $\omega$ (not $q$, which is inventory elsewhere in the book); distributable value and the allowed claim pool in §16.5 are $\mathcal{V}$ and $\mathcal{C}$ (calligraphic, so they cannot be confused with firm value $V_t$, a call price, or duration $D$).

## 16.1 The Back-End Equity Problem: What Emerges and Who Is Not Allowed to Hold It

### 16.1.1 Desk framing: a plan is a security factory with a distribution problem

At PJT you built the factory. You sat in the room where the waterfall was negotiated, you ran the recovery tables, and you watched the plan equity value move \$300mm in an afternoon because one side wanted more shares per dollar of claim and the other side wanted the juniors out of the money. You therefore already know the most important fact in this chapter: **the plan equity value is a negotiated number, not an estimate.** Moyer makes the same point from the buy side (Moyer_Distressed_Debt_Analysis p.355 and p.369): investors who will control the reorganized company prefer conservative valuations, because a lower value means more shares for their claims and a cleaner path past the classes below them.

A plan converts claims into a basket of new instruments. The desk translates each one into option language, because that is the only language in which they can be compared:

| Instrument | In option language | Typical recipient | Who cannot comfortably hold it |
| :--- | :--- | :--- | :--- |
| New common stock | A call on enterprise value struck at the new debt (Merton, Chapter 6) | Fulcrum class | CLOs (carried at zero in OC tests), banks (disposition clock), insurers (capital charges) |
| Warrants | A call on that call, usually long-dated and out of the money | Junior classes, old equity | Anyone who needs liquidity (see §16.4) |
| Subscription rights | A short-dated call struck at the rights price | Eligible members of a class | Holders with no cash, ineligible holders |
| Backstop commitment | A short put plus a fee | "The party" (§16.3) | Everyone not invited into the room |
| Take-back debt | Debt, with a recovery haircut baked in | Senior classes | Nobody, which is why CLOs ask for it |
| Litigation-trust interests | A non-transferable lottery ticket on lawsuits | General unsecured creditors | Anyone who wants to sell it |
| Cash | Cash | Administrative, 503(b)(9) and convenience claims | Nobody has ever objected |

The last column is where the trading lives. Each instrument is born in the hands of a holder chosen by the legal waterfall, not by the market, and the waterfall does not care whether that holder is permitted to own what it receives. A CLO that held the fulcrum loan gets stock its documents treat as worthless. A bank that took equity in a debt-for-equity swap has a regulatory clock and an unpleasant capital charge while it waits (Moyer p.370). An insurer pays a far higher risk-based capital charge on common stock than on the bond it used to own. Index funds cannot own the stock until it lists and seasons. The old equity holders, who were told for a year that they would get nothing, get warrants they did not ask for and cannot value. The only natural holders on the first day are hedge funds, and they know they are the only natural holders.

So the first quantity the desk writes down is not a valuation. It is the **overhang share**: constrained holdings as a fraction of the stock that can actually trade.
$$\phi^{\text{OH}} = \frac{\sum_{j\in\mathcal{J}^{c}} n_j}{n^{\text{float}}}, \qquad n^{\text{float}} = n^{\text{out}} - n^{\text{ctrl}} - n^{\text{lock}},$$
where $\mathcal{J}^{c}$ is the set of constrained holders (CLOs, banks, insurers), $n_j$ is holder $j$'s share count from the plan's distribution schedule, $n^{\text{out}}$ is shares outstanding, $n^{\text{ctrl}}$ is shares held by a controlling holder who will not sell, and $n^{\text{lock}}$ is shares under a post-confirmation lock-up (Moyer p.372 discusses why controllers sometimes restrict trading early on). In the cold open, if a sponsor holds a locked 35% and the CLOs hold 22%, the investable float is 65% of the company and the overhang share is $22/65 \approx 34\%$ *(illustrative)*. A third of everything that can trade is in the hands of someone who has to sell it. Moyer's related point (p.369) is that the investable equity cap, not the headline cap, is the "technical factor" that determines who can even look at the stock: a controller holding half the shares halves the cap a fund can buy into.

> **[SOURCE EXTRACTION]** *Moyer_Distressed_Debt_Analysis p.370:* "Banks and collateralized debt obligations (CDOs) are not natural holders of equity securities. The business model of these entities causes them to significantly prefer income earning assets as opposed to equities. ... Similarly, CDOs usually have contractual limitations on the absolute amount of and length of time they are allowed to hold equity."
>
> **Annotation.** Moyer wrote this in 2004 about CDOs. In 2026 the relevant vehicle is the broadly syndicated loan CLO, and the sentence has become more true, not less. Moyer treats the forced seller as a qualitative hazard that a careful investor "will certainly consider" (same page) and that a careful plan designer avoids by offering the constrained class a non-equity recovery (p.371). The systematic desk reads the same paragraph as a *specification*: "absolute amount" is a position cap, "length of time" is a deadline, and together they define a supply schedule with a start date, a size, and an end date. That is something you can forecast, and anything you can forecast you can trade ahead of. The modern departure is in the docs: post-2020 CLO indentures let managers hold restructured *loans* more patiently (Trend Watch in §16.2), which means plans now hand CLOs take-back paper wherever the debt capacity exists. Where it does not, because the business can only support so much new debt, the equity overhang that remains is *more* concentrated in CLO hands and *more* predictable.

### 16.1.2 What history says the stock does next

The academic record on post-reorg equity is a textbook example of an anomaly that was published, studied, and then eaten by the people who read the studies.

> **Trend Watch.** *The post-reorg premium: discovered 1999, gone by 2010.*
> - **1980–1993.** Eberhart, Altman & Aggarwal (1999), *The Equity Performance of Firms Emerging from Bankruptcy*, *Journal of Finance* 54(5): 131 emerging firms earned 200-trading-day cumulative abnormal returns of 22.8% to 29.6% (medians 16.8% to 22.2%) depending on the benchmark. The authors read it as an expectational error, not a risk premium.
> - **2001–2003.** Moyer (p.374), citing Imperial Capital and Bloomberg data, reports that back-end equities from the 2001 and 2002 emergence vintages beat the S&P 500 handily in 2003, and cites a study of 117 post-reorg equities over 1986–2003 that also found outperformance.
> - **1981–2019.** Jiang, Wang & Yang, *The Disappearing Outperformance of Post-reorg Equity* (summarized on the Duke FinReg Blog, 17 Sep 2021), track every US public filer with at least \$50mm of assets that filed in 1981–2016 and emerged public. Mean 200-day abnormal returns are 40% to 50%, but **the median abnormal return is zero**: the gains live in the right tail. An equal-weighted, monthly rebalanced portfolio from 1992 (about 20 stocks at a time) beat risk-adjusted benchmarks by 7.2% a year, concentrated in OTC names. Five-factor alpha was 0.8% to 1.2% a month in 2000–2010 and **zero after 2010**, and exchange-listed post-reorg stocks earned *negative* alpha in the most recent decade. Institutional ownership of post-reorg equity rose from about 40% in the 1990s to about 80% in the 2000s.
> - **What it means for the desk.** Buy-and-hold "post-reorg beta" is dead. What survives is (a) right-tail skew, which only a diversified book harvests (§16.8), (b) the OTC and illiquid segment where institutions still cannot or will not go, and (c) the *timing* of forced flow, which is the subject of §16.2.

Read the third bullet twice. "Mean 40%, median zero" is not a footnote; it is the whole strategy. A single post-reorg stock is a lottery ticket with a positive expected value and a coin-flip chance of doing nothing. The premium is a property of a *portfolio* of such stocks, and it is only available to someone who can own twenty of them at once without moving the price. We come back to that arithmetic in §16.8, with a jump-to-zero added, because Spirit Airlines insists.

> **[SOURCE EXTRACTION]** *Moyer_Distressed_Debt_Analysis p.374:* "A 1998 study concluded that outperformance is most pronounced during the first 200 days after a stock emerges and in those situations where institutional investors demanded to receive only equity in the restructuring."
>
> **Annotation.** Two features in one sentence. The first is the 200-day window, which reappears in every later study and which §16.2 explains mechanically: 200 trading days is about four supply half-lives for a seller that executes at the rate the fallen-angel data imply, which is the point by which roughly 93% of the forced supply has cleared. The second is the more interesting one for a former restructuring banker: *who elected equity.* Many plans offer creditors a choice between a cash-out (or take-back paper) and stock, and the election results are disclosed in ballot certifications and distribution notices. A sophisticated holder that elects stock over cash at the plan value is revealing a private valuation, which is exactly Moyer's next sentence about insiders who thought the equity was cheap. The desk turns this into a feature, the equity-election share of informed holders. The modern departure is that Jiang, Wang & Yang's rise in institutional ownership means the informed electors are now usually the marginal holders on day one, so the signal is weaker than it was in 1998, and it is strongest precisely where the electors are few and the forced sellers are many.

### Deep-Dive Resource Graph

- **Podcasts:** *Bloomberg Odd Lots* has run several conversations on distressed debt and bankruptcy investing; search its archive for "distressed" (no single episode cited here).
- **Practitioner Writing:** Duke FinReg Blog, "Has Post-reorg Equity Outperformed in the Last Three Decades?" (17 Sep 2021), https://sites.duke.edu/thefinregblog/2021/09/17/has-post-reorg-equity-outperformed-in-the-last-three-decades/ ; Moyer, *Distressed Debt Analysis* (2004), Chapter 13, "Postreorganization Considerations."
- **Academic Papers:** Eberhart, Altman & Aggarwal (1999), *The Equity Performance of Firms Emerging from Bankruptcy*, *Journal of Finance* 54(5): 1855–1868; Jiang, Wang & Yang, *The Disappearing Outperformance of Post-reorg Equity* (working paper; title only); Jiang, Li & Wang (2012), *Hedge Funds and Chapter 11*, *Journal of Finance* (title only).
- **Data & Code:** SEC EDGAR full-text search for plan distribution schedules and Forms 13D/13G/4, https://www.sec.gov/edgar ; CourtListener REST API for dockets and Rule 2019 statements, https://www.courtlistener.com/help/api/

## 16.2 Forced Selling as a Supply Process: From Fallen Angels to Orphan Equity

### 16.2.1 Desk framing: borrow the cleanest experiment on the shelf

We do not have a clean, large-sample study of CLO-driven selling in post-reorg stocks. We do have one of the cleanest natural experiments in all of credit: the fallen angel. When a bond is downgraded from investment grade to high yield, a large population of holders with investment-grade mandates is *required* to sell, regardless of what they think the bond is worth. That is the post-reorg CLO problem with a different label on the folder. Dynkin's account (Dynkin_Systematic_Investing_in_Credit p.140, p.151, p.158) and Ben Dor's (Ben_Dor_Quantitative_Credit_Portfolio_Management p.27, p.341) give us the shape: trading volume roughly quadruples around the event while bid-ask spreads *widen* (sellers paying for immediacy, not information), downgraded issuers underperform their peers by 15.09% into the event, and the price recovers over the following one to two years.

> **[SOURCE EXTRACTION]** *Ben_Dor_Quantitative_Credit_Portfolio_Management p.27:* "We present strong empirical evidence of the transient price pressure experienced by these securities due to forced selling driven by investment constraints. A study of the time course of this effect shows that this price pressure tends to peak about three months after the downgrade. Over a period of one to two years following the downgrade, most securities recover."
>
> **Annotation.** Three facts a model must reproduce: the pressure is *transient* (it mean-reverts, so it is not information), it *peaks after the event* (so the sellers do not all hit the bid on day one), and it decays over *one to two years* (so there is a slow component, too). A model in which constrained holders dump everything at the open fails the second fact; a model with a single exponential decay will fail the third, as we show in §16.2.3. For post-reorg equity, the "event" is the effective date or the end of a lock-up, and the "investment constraint" is a CLO indenture rather than an investment-grade mandate. The departure from the bond setting is that equity has no coupon to pay you while you wait, and the post-reorg stock may have no analyst coverage at all (Moyer p.371), so the arbitrage capital that eventually absorbs the overhang arrives even more slowly.

> **[SOURCE EXTRACTION]** *Dynkin_Systematic_Investing_in_Credit p.151:* "In the case of forced selling, upgraded issuers should not exhibit a reversal, since they are not subject to induced buying (or selling) by investors."
>
> **Annotation.** This is identification by asymmetry, and it is the best idea in this section. Overreaction would predict reversals in both directions; a constraint predicts a reversal only on the side where somebody is forced to trade. Dynkin finds upgraded issuers outperform by only about a third as much (5.66% vs. −15.09%, same page) and without the reversal. The post-reorg analogue gives us a cross-sectional test the desk can actually run: compare emergences where the fulcrum class was held mainly by CLOs (large forced supply) with emergences where it was held mainly by hedge funds (almost none). If the post-emergence drift is a constraint effect, it should scale with the CLO share of the fulcrum, and it should be absent where that share is near zero.

Theo's 13-week cash flow model makes its appearance here in an unexpected costume. In his old life the 13-week model was a schedule of cash *inflows and outflows by week*, with known dates and estimated sizes. The overhang model is the same object for shares: a schedule of forced *outflows by week*, with known start dates (the effective date, the lock-up expiry) and estimated sizes (the distribution schedule). Theo's USB stick, it turns out, contained the right data structure all along.

### 16.2.2 Derivation: overhang, slow capital, and the drift you can schedule

Let $v_t$ be the fundamental log value of the stock, which we treat as a $\mathbb{P}$-martingale over a 90-day horizon (we ignore the equity risk premium, which is small over that horizon compared with the effect we are measuring, and we will strip peer returns before fitting, as in Chapter 8). Let $Q_t \ge 0$ be the **overhang**: shares that constrained holders are required to sell and have not yet sold, measured in dollars at the plan value. Let $M_t > 0$ be the **arbitrage capital** willing to absorb that supply, in the same units. Three assumptions define the model.

*Supply.* Constrained holders execute a fixed fraction of what remains per unit time:
$$dQ_t = -\theta\, Q_t\,dt, \qquad Q_{t_0} = Q_0,$$
where $\theta > 0$ is the execution rate (per year) and $t_0$ is the effective date or the lock-up expiry, whichever comes later.

*Capital.* Arbitrage capital arrives slowly, in the spirit of Duffie's (2010) slow-moving capital:
$$dM_t = \rho\,(M^{*} - M_t)\,dt, \qquad M_{t_0} = M_0,$$
with $M^{*}$ the long-run capital that will eventually cover the name and $\rho$ its arrival speed (per year). The solution is $M_t = M^{*} + (M_0 - M^{*})e^{-\rho(t-t_0)}$.

*Price.* The observed log price carries a liquidity discount proportional to overhang per unit of capital:
$$p_t = v_t - \kappa\,\frac{Q_t}{M_t},$$
where $\kappa > 0$ is the price-impact coefficient (log points per unit of overhang-to-capital ratio).

The tradeable object is the expected *excess* drift, the part of the return that is not fundamental. Differentiate the ratio with the quotient rule:
$$\frac{d}{dt}\left(\frac{Q_t}{M_t}\right) = \frac{\dot Q_t}{M_t} - \frac{Q_t\,\dot M_t}{M_t^{2}} = -\theta\,\frac{Q_t}{M_t} - \frac{Q_t\,\dot M_t}{M_t^{2}}.$$
Since $v_t$ is a martingale, $\tfrac{d}{dt}\mathbb{E}^{\mathbb{P}}_{t_0}[v_t] = 0$, and the deterministic discount is all that remains:
$$\mu_t \equiv \frac{d}{dt}\,\mathbb{E}^{\mathbb{P}}_{t_0}\!\left[p_t - v_t\right] = \kappa\left(\theta\,\frac{Q_t}{M_t} + \frac{Q_t\,\dot M_t}{M_t^{2}}\right).$$
Both terms are positive while capital is still arriving ($\dot M_t > 0$): the stock drifts up because the sellers are running out *and* because the buyers are showing up. With constant capital ($\rho = 0$, $M_t \equiv M$) everything is closed-form:
$$p_t - v_t = -\frac{\kappa Q_0}{M}\,e^{-\theta (t - t_0)}, \qquad \int_{t_0}^{\infty}\mu_t\,dt = \frac{\kappa Q_0}{M}, \qquad t_{1/2} = \frac{\ln 2}{\theta}.$$
The total abnormal return available to a buyer at $t_0$ is the initial discount $\kappa Q_0/M$, and half of it is gone after one half-life. The boundary conditions are sensible: if $Q_0 = 0$ (hedge funds held the fulcrum) there is no drift at all, and as $M \to \infty$ (a large, well-covered name) the discount vanishes.

**Why the discount peaks late.** The constant-capital solution has its largest discount at $t_0$, which contradicts Ben Dor's "about three months after." The fix is to recognize that constrained holders do not receive all their shares on the effective date. Distributions settle over weeks, claims are allowed in batches, a when-issued market may trade before the shares are delivered (Moyer p.370), and lock-ups expire on a ladder. Let shares flow *into* constrained hands at rate $Q_0\,\alpha e^{-\alpha (t-t_0)}$, so that a total of $Q_0$ arrives with mean lag $1/\alpha$, while those holders keep selling at rate $\theta$. Writing $s = t - t_0$ and starting from $Q = 0$:
$$\dot Q_s = Q_0\,\alpha\,e^{-\alpha s} - \theta\,Q_s \quad\Longrightarrow\quad Q_s = \frac{Q_0\,\alpha}{\theta - \alpha}\left(e^{-\alpha s} - e^{-\theta s}\right), \qquad \theta \neq \alpha .$$
(Verify by substitution: $\dot Q_s + \theta Q_s = \frac{Q_0\alpha}{\theta-\alpha}\left[(\theta - \alpha)e^{-\alpha s}\right] = Q_0\alpha e^{-\alpha s}$.) The overhang, and with constant capital the discount, peaks where inflow equals outflow, $\dot Q_s = 0$:
$$-\alpha e^{-\alpha s^{*}} + \theta e^{-\theta s^{*}} = 0 \quad\Longrightarrow\quad s^{*} = \frac{\ln(\theta/\alpha)}{\theta - \alpha},$$
with the limit $s^{*} = 1/\theta$ when $\theta = \alpha$. The peak is always *after* the event, which is the second fact in Ben Dor's paragraph, and its timing tells you the ratio of two speeds that you can estimate separately: how fast shares are delivered (from the claims agent's distribution notices) and how fast constrained holders sell (from volume and holdings filings).

Kaz, reading over Theo's shoulder, says this is "just a two-compartment pharmacokinetic model, the kind used for a drug dose moving from the gut into the bloodstream." Kaz is right, and we will let Kaz have this one, because the analogy is exact: the plan is the dose, the CLO is the gut, the market is the bloodstream, and the alpha is the side effect.

### 16.2.3 Fitting the execution rate to published aggregates

We can calibrate $\theta$ without a single post-reorg trade, by borrowing the fallen-angel reversal. Dynkin p.158 reports the reversal for the worst-hit bucket of downgraded bonds over three successive six-month windows after formation: +5.75%, +1.04% and +0.86%. Under the single-exponential model with constant capital, the reversal earned in window $k$ (each of length $\Delta = 0.5$ years) is the drop in the discount over that window:
$$w_k = A\,e^{-\theta(k-1)\Delta}\left(1 - e^{-\theta\Delta}\right), \qquad A = \frac{\kappa Q_0}{M}.$$
The ratio of consecutive windows depends only on $\theta$:
$$\frac{w_2}{w_1} = e^{-\theta\Delta} \quad\Longrightarrow\quad \hat\theta = -\frac{1}{\Delta}\ln\frac{w_2}{w_1} = -2\ln\frac{1.04}{5.75} \approx 3.42 \text{ per year},$$
a half-life of $\ln 2/3.42 \approx 0.20$ years, or about 2.4 months, and an implied total reversal $\hat A = 5.75/(1 - e^{-1.71}) \approx 7.0\%$ *(illustrative fit to published aggregates)*. The model then predicts a third window of $w_3 = w_2\,e^{-\theta\Delta} \approx 0.19\%$. The data say 0.86%. The single exponential is wrong in the tail, and it is wrong in exactly the direction Ben Dor's "one to two years" warned about: there is a second, slower component. In our model that component already exists. It is the capital-arrival term $Q_t\dot M_t/M_t^2$, which decays at the speed of the slow money ($\rho$), not the speed of the sellers ($\theta$). Fitting $(\theta, \rho)$ jointly needs more than three numbers, which is why Exercise 2 hands you a panel instead.

Ines, who has been listening with the expression of someone watching a stranger misplay a hand, translates: "The fast decay is the forced seller folding. The slow decay is the table filling up with players who could have sat down on day one but didn't know the game was running. You get paid for the first by being early. You get paid for the second by being *patient.* Different edges, different capital."

### 16.2.4 From model to signal: momentum with an expiry date

The signal the desk actually trades is the model's expected excess drift, estimated name by name:
$$\hat\mu_t = \hat\kappa\,\hat\theta\,\frac{\hat Q_t}{\hat M_t}, \qquad \hat Q_t = \hat Q_{t_0}\,\big(1 - \hat x_t\big),$$
where $\hat Q_{t_0}$ is the constrained holders' allocation from the plan's distribution schedule (cross-referenced against the ad hoc group's Rule 2019 statements and CLO trustee reports, which list loan positions by holder), $\hat x_t \in [0,1]$ is the fraction already executed (from 13D/13G amendments, Form 4 filings for 10% holders, quarterly 13F changes, and volume above a peer-implied baseline), and $\hat M_t$ is a capital proxy (13F holder count, average daily volume, borrow availability).

This is time-series momentum, the subject of Chapter 10, with two differences that make it better than ordinary momentum. First, the *sign* is known before the first return prints: as long as $\hat Q_t > 0$, the expected drift is positive. Second, the signal carries its own **expiry date**. When the constrained holders' filings show them out, $\hat Q_t \approx 0$ and the drift is zero by construction. At that point the desk is no longer trading a flow; it is long an uncovered small-cap, and it should either underwrite the business properly or leave. Ordinary trend-followers find out that a trend has ended by losing money. This one tells you in a 13G amendment.

> **Ways This Blows Up.**
> 1. *Using the plan value as $v_t$.* Plan values are biased low by the controlling creditors (Moyer p.355, p.369), so the stock can open *above* the plan value with a large overhang, the measured "discount" is negative, and the fit explodes. Anchor $v_t$ to the when-issued price or a peer-multiple band, never to the disclosure statement.
> 2. *Stale OTC prints.* Equal-weighted portfolios of illiquid stocks inherit bid-ask bounce as fake alpha (Blume and Stambaugh's classic bias). Jiang, Wang & Yang's surviving alpha is concentrated in OTC names, partly for this reason. Use quote midpoints and skip-a-day returns.
> 3. *Survivorship.* Spirit Airlines' first post-reorg equity went from emergence to a second Chapter 11 in under six months (§16.7). A backtest that drops delisted names will report a beautiful drift.
> 4. *Fundamental news in the residual.* The first earnings release after emergence moves the stock more than the overhang does. Strip peer and factor returns first (Chapter 8's IDO step) and exclude event windows. IDO or it didn't happen.
> 5. *$\theta$ is not a constant.* Sellers accelerate into liquidity. Dynkin p.140 reports volumes about four times normal with *wider* spreads around the fallen-angel event; a seller who sees bids will hit them. Let $\theta$ depend on depth, or at least refit it after any volume spike.

> **Trend Watch.** *CLO documents got patient with debt, not with equity, 2020–2026.*
> - **Before 2020.** Most broadly syndicated CLO indentures gave managers little room to hold or fund anything that was not a conforming loan. Law-firm guidance from the 2020 downturn (O'Melveny, *CLO Issues in Workouts and Debt Restructurings*, 2020; Seward & Kissel client notes) describes severe restrictions on acquiring and holding equity, and general prohibitions on providing new money in exchange for equity or other non-conforming assets.
> - **2021–2022.** S&P Global Ratings described the spread of "loss mitigation" and workout-loan language (a video briefing of 10 Mar 2021, and *Par Wars: U.S. CLO Document Provisions Evolve To Provide Managers More Flexibility*, 23 Sep 2022): workout loans that broadly meet the collateral-obligation definition are typically carried as defaulted obligations, while restructured assets further from that definition are carried at zero. Industry tallies reported a sharp rise in the share of new European CLOs with such language between 2020 and 2021 *(approx.; secondary summaries, primary source not verified)*.
> - **2023–2024.** S&P published a Credit FAQ on uptier priming and drop-down provisions in US CLOs (26 Jul 2023), and Weil's June 2024 note on CLOs as restructuring creditors observed that managers generally want to avoid a restructured asset being treated as equity, because equity may be discounted entirely in the OC test or, if it qualifies as a loss-mitigation loan, receive punitive treatment.
> - **What it means for the desk.** The forced-seller channel is contractual, not regulatory, and the contracts now distinguish sharply between restructured debt (holdable) and equity (not). Plans respond by giving CLOs take-back term loans wherever the business can carry them. The equity overhang that survives is therefore concentrated in cases where the fulcrum was a CLO-heavy loan *and* the debt capacity was thin: precisely the cases you can identify from the plan's capital structure before the effective date.

### Specification for AI Implementation

**The Spec You Hand the Robot.** *Vague version:* "Buy post-reorg stocks where CLOs have to sell." *What ROBO built:* a strategy that buys at the open on the effective date, the moment the overhang is largest and before a single share has been delivered, and then holds forever, because nobody told it when "have to sell" stops. *Precise version:* build `ForcedSellerOverhang`, a deterministic model of overhang $Q_s$, capital $M_s$, discount $-\kappa Q_s/M_s$ and drift $\mu_s$ on $s = t - t_0 \ge 0$ in years; support both instantaneous release and exponential delivery at rate $\alpha$; fit $\theta$ from window reversals and from a panel of IDO-stripped residuals; emit a signal that is exactly zero once the constrained holders have executed.

*Input schema (holder registry, one row per holder per instrument per as-of date):* `instrument_id` (internal string; never a guessed CUSIP), `holder_id`, `holder_type` in {`CLO`, `bank`, `insurer`, `hedge_fund`, `sponsor`, `retail`, `other`}, `shares` (float, millions), `source` in {`plan_schedule`, `rule_2019`, `13D`, `13G`, `form_4`, `13F`, `trustee_report`}, `as_of` (date), `lockup_end` (date or null). *Panel shapes:* time grid `s` of shape `(n_days,)` on a 252-day year; residual panel of shape `(n_names, n_days)`. *Edge cases:* $\theta = \alpha$ (use the limit formula), $M_0 \le 0$ (reject), zero overhang (signal zero, no division), negative mean residuals near zero in the log fit (mask them).

```python
import numpy as np
from dataclasses import dataclass
from typing import Optional
from scipy.stats import norm
from scipy.optimize import brentq

RNG = np.random.default_rng(16)   # chapter seed; every block below reuses it
TRADING_DAYS = 252


def trap(y, x):
    """Trapezoid rule (avoids numpy version differences in trapz/trapezoid)."""
    y, x = np.asarray(y, float), np.asarray(x, float)
    return float(np.sum(0.5 * (y[1:] + y[:-1]) * np.diff(x)))


@dataclass
class ForcedSellerOverhang:
    """Overhang Q (USD mm at plan value), arbitrage capital M (USD mm), discount -kappa*Q/M.

    theta, rho, alpha are per year; s = t - t0 in years (s >= 0); physical measure P.
    alpha=None: the whole overhang lands at t0. Otherwise it is delivered at rate alpha.
    """
    Q0: float
    theta: float
    M0: float
    M_star: float
    rho: float
    kappa: float
    alpha: Optional[float] = None

    def __post_init__(self):
        if self.Q0 < 0 or self.kappa < 0 or self.rho < 0:
            raise ValueError("Q0, kappa, rho must be non-negative")
        if self.theta <= 0 or self.M0 <= 0 or self.M_star <= 0:
            raise ValueError("theta, M0, M_star must be positive")
        if self.alpha is not None and self.alpha <= 0:
            raise ValueError("alpha must be positive")

    def Q(self, s):
        s = np.asarray(s, float)
        if self.alpha is None:
            return self.Q0 * np.exp(-self.theta * s)
        a, th = self.alpha, self.theta
        if abs(th - a) < 1e-10:                       # limit theta -> alpha
            return self.Q0 * a * s * np.exp(-a * s)
        return self.Q0 * a / (th - a) * (np.exp(-a * s) - np.exp(-th * s))

    def Qdot(self, s):
        s = np.asarray(s, float)
        inflow = 0.0 if self.alpha is None else self.Q0 * self.alpha * np.exp(-self.alpha * s)
        return inflow - self.theta * self.Q(s)

    def M(self, s):
        s = np.asarray(s, float)
        return self.M_star + (self.M0 - self.M_star) * np.exp(-self.rho * s)

    def Mdot(self, s):
        return self.rho * (self.M_star - self.M(s))

    def discount(self, s):
        """E^P[p_s - v_s]: log-price discount (<= 0)."""
        return -self.kappa * self.Q(s) / self.M(s)

    def drift(self, s):
        """mu_s = d/ds E^P[p_s - v_s], per year."""
        Q, M = self.Q(s), self.M(s)
        return self.kappa * (-self.Qdot(s) / M + Q * self.Mdot(s) / M**2)

    def half_life(self):
        return np.log(2.0) / self.theta

    def peak_time(self):
        """Time of maximum overhang (= peak discount when capital is constant)."""
        if self.alpha is None:
            return 0.0
        a, th = self.alpha, self.theta
        if abs(th - a) < 1e-10:
            return 1.0 / th
        return np.log(th / a) / (th - a)


def theta_from_windows(w1, w2, window_years=0.5):
    """Single-exponential fit: w2 / w1 = exp(-theta * window)."""
    if not (w1 > w2 > 0):
        raise ValueError("need w1 > w2 > 0")
    return -np.log(w2 / w1) / window_years


def simulate_residual_panel(model, n_names=200, years=1.0, noise_daily=0.02, rng=RNG):
    """IDO-stripped log-price deviations p - v for n_names emergences: discount + iid noise."""
    s = np.arange(int(years * TRADING_DAYS) + 1) / TRADING_DAYS
    eps = rng.normal(0.0, noise_daily, size=(n_names, s.size))
    return s, model.discount(s)[None, :] + eps


def fit_theta_loglinear(s, panel, max_years=0.5, floor=0.005):
    """Fit log(-mean deviation) = log(A) - theta * s on the early, well-identified window."""
    mean_dev = panel.mean(axis=0)
    mask = (s <= max_years) & (-mean_dev > floor)
    slope, intercept = np.polyfit(s[mask], np.log(-mean_dev[mask]), 1)
    return -slope, np.exp(intercept)


def overhang_signal(Q_hat, M_hat, kappa_hat, theta_hat, executed_frac):
    """Expected excess drift (per year). Exactly zero once constrained holders are out."""
    Q_rem = np.clip(np.asarray(Q_hat, float) * (1.0 - np.asarray(executed_frac, float)), 0.0, None)
    return kappa_hat * theta_hat * Q_rem / np.maximum(np.asarray(M_hat, float), 1e-9)


# --- calibration to the fallen-angel aggregates (Dynkin p.158; illustrative) ---
theta_fa = theta_from_windows(5.75, 1.04)
A_fa = 5.75 / (1.0 - np.exp(-theta_fa * 0.5))
w3_pred = A_fa * np.exp(-theta_fa) * (1.0 - np.exp(-theta_fa * 0.5))
assert 3.3 < theta_fa < 3.5, theta_fa
assert 2.3 < 12 * np.log(2) / theta_fa < 2.5            # half-life in months
assert w3_pred < 0.86                                     # data need a slow component

# --- sanity checks on the model ---
s = np.linspace(0.0, 3.0, 3001)
ovh = ForcedSellerOverhang(Q0=30.0, theta=theta_fa, M0=60.0, M_star=60.0, rho=0.0, kappa=0.3)
assert abs(trap(ovh.drift(s), s) - (ovh.discount(3.0) - ovh.discount(0.0))) < 1e-4
assert abs(ovh.discount(ovh.half_life()) - 0.5 * ovh.discount(0.0)) < 1e-12
assert abs(-ovh.discount(0.0) - 0.15) < 1e-12              # kappa*Q0/M = 15% total

ovh_sched = ForcedSellerOverhang(Q0=30.0, theta=theta_fa, M0=60.0, M_star=60.0,
                                 rho=0.0, kappa=0.3, alpha=5.0)
grid = np.linspace(0.0, 2.0, 200001)
s_num = grid[np.argmin(ovh_sched.discount(grid))]
assert abs(s_num - ovh_sched.peak_time()) < 1e-4
assert 0.2 < ovh_sched.peak_time() < 0.3                   # about three months

ovh_slow = ForcedSellerOverhang(Q0=30.0, theta=theta_fa, M0=30.0, M_star=60.0, rho=1.0, kappa=0.3)
assert np.all(ovh_slow.drift(s) > ovh.drift(s))            # slow capital adds drift
assert abs(trap(ovh_slow.drift(s), s) - 0.3) < 1e-3        # total = kappa*Q0/M0

# --- panel fit recovers theta ---
s_d, panel = simulate_residual_panel(ovh)
theta_hat, A_hat = fit_theta_loglinear(s_d, panel)
assert abs(theta_hat / theta_fa - 1.0) < 0.10, theta_hat
assert abs(A_hat / 0.15 - 1.0) < 0.10, A_hat
assert overhang_signal(30.0, 60.0, 0.3, theta_hat, 1.0) == 0.0

print(f"theta={theta_fa:.2f}/yr  half-life={12*np.log(2)/theta_fa:.1f}m  "
      f"peak={12*ovh_sched.peak_time():.1f}m  panel theta_hat={theta_hat:.2f}")
```

### Deep-Dive Resource Graph

- **Podcasts:** *Flirting with Models* (Corey Hoffstein) has repeatedly covered trend-following design, the right background for treating a forced-flow drift as momentum with an expiry (no single episode cited).
- **Practitioner Writing:** S&P Global Ratings, *Par Wars: U.S. CLO Document Provisions Evolve To Provide Managers More Flexibility* (23 Sep 2022) and *Credit FAQ: A Closer Look At Uptier Priming And Asset Drop-Down Provisions In U.S. CLOs* (26 Jul 2023); Weil, Gotshal & Manges, note on CLOs as restructuring creditors (Jun 2024); O'Melveny, *CLO Issues in Workouts and Debt Restructurings* (2020). Titles only; links not verified this session.
- **Academic Papers:** Duffie (2010), *Presidential Address: Asset Price Dynamics with Slow-Moving Capital*, *Journal of Finance*; Ellul, Jotikasthira & Lundblad (2011), *Regulatory Pressure and Fire Sales in the Corporate Bond Market*, *Journal of Financial Economics*; Ben Dor et al., the fallen-angel chapters of *Quantitative Credit Portfolio Management* (Ben_Dor p.27, p.341); Dynkin et al., *Systematic Investing in Credit* (Dynkin p.140–158).
- **Data & Code:** SEC EDGAR for 13D/13G/Form 4/13F, https://www.sec.gov/edgar ; CourtListener for Rule 2019 statements, https://www.courtlistener.com/help/api/ ; CLO trustee reports via your loan-data vendor (Chapter 21).

## 16.3 Rights Offerings and Backstops: Pricing the Put You Sold

### 16.3.1 Desk framing: the backstop is the player who agrees to call any bet

A rights offering is a capital raise in which a class of creditors is offered new shares at a price set off the plan equity value, which (see §16.1) is a number the people setting it had every reason to set low. A backstop is a commitment, signed weeks or months before the offering funds, to buy every share the class does not take. The backstop party is paid a fee for this, usually in shares.

"Translate," says Ines, when Theo explains this. Then she does it herself. "The backstop is the player who agrees in advance to call any bet. Nobody does that for free. You do it if you're paid a fee, if you get to buy chips at a discount, and if you get to see everybody's cards before they decide whether to play. In a rights offering you get all three. That's why the seat is so crowded and the door is so narrow."

The reason the instrument exists at all is legal, and Moyer states it precisely.

> **[SOURCE EXTRACTION]** *Moyer_Distressed_Debt_Analysis p.362:* "Thus, an unsecured creditor is extremely vulnerable when the debtor's circumstances are such that exit financing cannot be obtained in an amount sufficient to pay off all administrative claims; frequently this is a reason why a rights offering to raise new cash from creditors is included in plans of reorganization."
>
> **Annotation.** Administrative claims must be paid in full in cash on the effective date unless the holder agrees otherwise, so a plan that cannot raise enough exit cash cannot be confirmed. The rights offering is the plan's way of making its own creditors the lender of last resort. Moyer frames it as protection for unsecured creditors; the modern data (Trend Watch below) show that in practice it has become the dominant form of exit equity and a large transfer *within* a class, from the members who are not in the backstop group to the members who are. The desk's departure from Moyer is to stop asking "does the plan need the cash?" and to start asking "what is the put worth, and who got to sell it?"

> **[SOURCE EXTRACTION]** *Houlihan_Lokey_Distressed_MA p.24:* "A backstopped rights offering maintains fairness for all existing shareholders and assures that the needed capital is raised, but, in turn, requires extra consideration for the "backstop" investor."
>
> **Annotation.** "Extra consideration" is the polite phrase for an option premium. Houlihan's example is a family-owned company with a well-capitalized insider as backstop, and its "fairness" claim holds when every holder can participate on equal terms. The 2025 *ConvergeOne* decision (Trend Watch below) is the legal system discovering what the derivation below shows mathematically: when only *some* members of a class are allowed to sell the put and collect the premium, the offering is not fair to the members who are left out, however equal the rights themselves look on paper.

### 16.3.2 Derivation: the right is a call, the backstop is a put

**Setup.** Let $n_0$ be the plan shares distributed before the offering (to creditors and direct investors, excluding fee shares), $m$ the number of rights-offering shares, and $K$ the subscription price, so the offering raises $mK$. Let $E$ be the pre-money value of the reorganized equity at the funding date, random as of the commitment date, and write the per-share pre-money value as $x \equiv E/n_0$. After the offering the company holds $E + mK$ of value across $n_0 + m$ shares:
$$S^{\text{post}} = \frac{E + mK}{n_0 + m} = \frac{n_0 x + mK}{n_0 + m}.$$
Subtracting $K$ from both sides gives the identity that drives everything:
$$S^{\text{post}} - K = \frac{n_0\,(x - K)}{n_0 + m}, \qquad\text{so}\qquad S^{\text{post}} > K \iff x > K.$$

**The right.** A rational holder subscribes if and only if $x > K$. Each eligible plan share carries $m/n_0$ rights, so the value of the rights attached to one plan share at funding is
$$\text{Right}(x) = \frac{m}{n_0}\left(S^{\text{post}} - K\right)^{+} = \frac{m}{n_0 + m}\,(x - K)^{+},$$
a call on the *pre-money* per-share value, struck at the subscription price, scaled by a single dilution factor. (The "theoretical ex-rights price" of equity-capital-markets folklore is just $S^{\text{post}}$ evaluated at today's $x$.)

**The backstop.** If $x < K$, nobody subscribes, and the backstop party must buy all $m$ shares at $K$, each worth $S^{\text{post}}$. Its loss is $m(K - S^{\text{post}}) = \frac{m n_0}{n_0+m}(K - x)$. If $x > K$, everybody subscribes and the backstop buys nothing. So the backstop's payoff is a short put:
$$\Pi^{\text{BS}}(x) = -N_{\text{eff}}\,(K - x)^{+}, \qquad N_{\text{eff}} = \frac{m\,n_0}{n_0 + m}.$$
Let $\text{Put}(x_0, K; \sigma, T)$ be the value of a put on $x$ struck at $K$, with $\sigma$ the volatility of the reorganized equity and $T$ the time from commitment to funding. The fair fee, expressed as a fraction of the capital raised, sets the fee equal to the put:
$$f^{*}\,mK = N_{\text{eff}}\,\text{Put}(x_0, K;\sigma,T) \quad\Longrightarrow\quad f^{*} = \frac{n_0}{n_0+m}\cdot\frac{\text{Put}(x_0, K;\sigma,T)}{K}.$$
Because no liquid option exists on a company that has not emerged yet, we evaluate the put with the Black–Scholes formula under the assumption that $x$ is a driftless lognormal under $\mathbb{P}$ over the short commitment window (so the "$\mathbb{Q}$" here is nominal: zero rate, zero drift). Kaz asks why we don't just use the risk-neutral measure. Theo asks Kaz to name the traded instrument that spans it. Kaz goes quiet.

**Worked number.** Put $x_0 = 1$, a rights price at a 25% discount to fair value, $K = 0.75$ (the average plan-value discount Buccola, Marcovich Gross & McBrady report; Trend Watch below), $\sigma = 0.70$ and $T = 0.5$:
$$d_1 = \frac{\ln(1/0.75) + \tfrac12(0.49)(0.5)}{0.70\sqrt{0.5}} = \frac{0.2877 + 0.1225}{0.4950} \approx 0.829, \qquad d_2 = d_1 - 0.4950 \approx 0.334,$$
$$\text{Put} = K\,\Phi(-d_2) - x_0\,\Phi(-d_1) \approx 0.75(0.3693) - 0.2036 \approx 0.0734, \qquad \frac{\text{Put}}{K} \approx 9.8\%.$$
With Hertz's dilution factor, $n_0/(n_0 + m) = 291.25/454.75 \approx 0.64$ (share counts in §16.3.4), the fair fee is $f^{*} \approx 0.64 \times 9.8\% \approx 6.3\%$ *(illustrative)*. That is almost exactly the 6% average fee that Seth reports for hedge-fund backstops. On this metric the market prices the backstop like a Black–Scholes put at 70% volatility.

Now vary the two inputs nobody negotiates in public:

| Discount to fair value | Fair fee, $T = 0.25$ y | Fair fee, $T = 0.50$ y |
| :--- | :--- | :--- |
| 0% ($K = x_0$) | ≈ 8.9% | ≈ 12.5% |
| 25% ($K = 0.75\,x_0$) | ≈ 3.0% | ≈ 6.3% |
| 50% ($K = 0.50\,x_0$) | ≈ 0.3% | ≈ 1.6% |

*(Illustrative: $\sigma = 0.70$, dilution factor 0.64, zero rate; the code below reproduces the table.)* The table makes the chapter's central point about backstops. **The fee and the discount are substitutes.** A deep discount makes the put nearly worthless, because the equity would have to fall by half before the backstop lost a dollar. A backstop party that receives a 50% discount *and* a 10% fee is being paid twice for one risk, and the second payment is the larger one.

**The all-in transfer.** The backstop party's take has four legs, not one:
$$\Pi^{\text{BP}} = \underbrace{f\,m\,S^{\text{post}}}_{\text{fee, paid in shares}} \;+\; \underbrace{a\,m\,(S^{\text{post}} - K)}_{\text{reserved allocation at a discount}} \;+\; \underbrace{(1-a)\,\eta\,m\,(S^{\text{post}} - K)^{+}}_{\text{exclusivity option}} \;-\; \underbrace{N_{\text{eff}}\,(K - x)^{+}}_{\text{the put}},$$
where $a$ is the fraction of the offering reserved for the backstop parties outright and $\eta$ is the fraction of in-the-money rights that other holders fail to exercise (ineligible holders, holders without cash, retail holders who never read the notice). Three things in this expression are routinely mispriced. The fee is paid in *shares*, so it is worth $f\,m\,S^{\text{post}}$, not $f\,m\,K$: when the discount is real, the fee is worth more than its headline. The reserved allocation is a pure transfer whenever $x_0 > K$. And the exclusivity option, the right to absorb whatever others leave on the table, is a free call. (We have ignored the small extra dilution from the fee shares themselves, which the code handles by valuing fee shares at the post-money price.)

> **Trend Watch.** *Rights offerings took over exit financing, and the courts noticed, 2003–2026.*
> - **Prevalence.** Gunjan Seth (USC Marshall), *Do Rights Offerings Reduce Bargaining Complexity in Chapter 11?* (CLS Blue Sky Blog, 11 Mar 2025): rights offerings financed about 35% of large Chapter 11 cases over 2003–2021 on an asset-weighted basis, rising to about 87% by 2019, with roughly \$46bn raised; hedge-fund backstoppers charge about 6% of the amount raised, buy about 43% of the equity, and appoint about 40% of the board; participants earn about 50% within three months; instrumental-variable estimates suggest rights offerings raise total creditor recoveries by about 40% and shorten cases by about seven months. (The paper's NBER abstract, February 2024, gives 47% of bankruptcies on a different basis.)
> - **The transfer.** Buccola, Marcovich Gross & McBrady, *The Backstop Party*, *American Bankruptcy Law Journal* 100(1) (2026): 49 confirmed plans with backstopped rights offerings, January 2016 to June 2024. Average discount to plan value 25%, about 50% effective; all-in backstop compensation 20.1% of the amount raised (25.1% in cases with market-priced values), against 3–7% underwriting spreads for IPOs and seasoned offerings. Per dollar of *identical* claim, backstop parties recovered about 21 cents more than non-participants measured at plan values (21c vs. 8c of value transferred) and 35c vs. 19c at market values.
> - **The legal regime shift.** The Fifth Circuit's *Serta* decision (31 Dec 2024) held that an uptier indemnity for some lenders violated the equal-treatment rule of §1123(a)(4), looking at a plan's actual effect rather than its form. On 25 Sep 2025, in *ConvergeOne*, the district court for the Southern District of Texas reversed confirmation of a prepackaged plan insofar as it gave a subset of first-lien lenders an exclusive backstop of a \$245mm rights offering, with a 10% fee and no market test, as unequal treatment. The debtors noticed an appeal on 22 Oct 2025; our October 2026 search found no Fifth Circuit ruling. In contrast, LATAM's \$5.4bn backstop for a subset of unsecured creditors was approved after court-ordered mediation, on business-judgment grounds.
> - **What it means for the desk.** Model the fee leg as fee times $\Pr(\text{exclusive backstop survives} \mid \text{circuit, market test})$, with a jump in that probability at 25 Sep 2025 for Fifth Circuit cases with no market test. Commentators noted that the *ConvergeOne* court pointed to *Serta*'s "open market purchase" analysis as guidance on what a market test might look like, which means the most expensive three words in finance now also help decide who may sell the put.

### 16.3.3 Desk Myth vs. Desk Reality

> **Desk Myth vs. Desk Reality.** *Myth:* "The backstop fee is the price of the backstop." *Reality:* The fee is the smallest of four legs. In a 25%-discount offering at 70% volatility the put is worth about 6% of the raise; the discount on the backstop party's reserved allocation and the exclusivity option are worth more, and the fee itself is paid in shares that are worth more than their face whenever the discount is real. If you are not in the backstop group, your rights are worth exactly what the derivation says. If you are, your seat is worth several times that.

### 16.3.4 Case Study: the Hertz rights offering, June 2021

The Hertz plan (§16.6 has the whole docket) raised \$1.635bn in a rights offering at \$10.00 per share, priced off an equity value of about \$4.7bn (Hertz 8-K/A, 14 May 2021). The offering was made first to Hertz's old stockholders, who could take either the rights *or* a package of 30-year warrants, but not both, and unexercised rights flowed to eligible holders of unsecured funded debt. The plan sponsors and other commitment parties backstopped it for a 10% premium paid in common stock at the same valuation. The rights expired on 15 Jun 2021. The share counts in the 8-K filed after the effective date (7 Jul 2021) are worth writing down exactly, because they let us audit every number:

| Item | Shares | Note |
| :--- | :--- | :--- |
| Rights shares to participants | 127,362,114 | Includes 7,858,805 to commitment parties |
| Unsubscribed shares to commitment parties | 36,137,887 | The put "exercised" against the backstop: the shares nobody else took |
| Backstop fee shares | 16,350,000 | $16.35/163.5 = 10.0\%$ of the offering, paid in stock at \$10 |
| Plan sponsors' direct purchase | 277,119,438 | \$2.781bn at the rights price |
| Old stockholders' 3% | 14,133,075 | |
| Total new common outstanding | 471,102,514 | The five rows sum exactly |

So $m = 127.36 + 36.14 = 163.50$mm shares (\$1.635bn at \$10), $n_0 = 277.12 + 14.13 = 291.25$mm, and the dilution factor in the derivation is $291.25/454.75 \approx 0.64$. Three observations a systematic desk would have made in real time:

1. **The put was short-dated.** The commitment-to-funding window ran from the May 2021 auction result to the 30 Jun 2021 effective date, about $T \approx 0.1$ to $0.15$ years. At $T = 0.1$ and 70% volatility, even an at-the-money put is worth only about 5.6% of the raise after dilution *(illustrative)*. A 10% fee was rich by the Black–Scholes yardstick before counting any discount.
2. **The unsubscribed block was large and in the money.** About 22% of the offering went unsubscribed, largely because old stockholders who preferred warrants could not also take rights. That is the exclusivity option in our formula, with a large $\eta$ supplied by the plan's own either-or election.
3. **Ex post, the seat was worth a fortune.** At the \$29 re-IPO price of 8 Nov 2021, the 36.14mm unsubscribed shares bought at \$10 carried a gain of about \$687mm, and the 16.35mm fee shares were worth about \$474mm, together about \$1.16bn on a \$1.635bn commitment *(approx.; derived from sourced share counts and prices, before any hedging or financing cost)*. Most of that is the stock's re-rating, not the put premium, which is exactly the point of the Buccola findings: the backstop seat is a levered long position in the plan's own discount.

Mags, who backstopped a rights offering in 2009 "with a fax machine and a prayer," reads the table twice. "Back in my day the backstop was the guy nobody else would lend to. Now it's the guy everybody wants to be. That's how you know the price is wrong."

```python
# --- Block 2: rights offerings and backstops (reuses RNG, norm, trap) ---

def _d1d2(S, K, T, sigma, r):
    vs = sigma * np.sqrt(T)
    d1 = (np.log(S / K) + (r + 0.5 * sigma**2) * T) / vs
    return d1, d1 - vs


def bs_call(S, K, T, sigma, r=0.0):
    S, K = np.asarray(S, float), np.asarray(K, float)
    if T <= 0 or sigma <= 0:
        return np.maximum(S - K * np.exp(-r * max(T, 0.0)), 0.0)
    d1, d2 = _d1d2(S, K, T, sigma, r)
    return S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)


def bs_put(S, K, T, sigma, r=0.0):
    S, K = np.asarray(S, float), np.asarray(K, float)
    if T <= 0 or sigma <= 0:
        return np.maximum(K * np.exp(-r * max(T, 0.0)) - S, 0.0)
    d1, d2 = _d1d2(S, K, T, sigma, r)
    return K * np.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)


@dataclass
class RightsOffering:
    """n0: plan shares before the offering, excluding fee shares (mm); m: rights shares (mm);
    K: subscription price per share. x: pre-money value per plan share at funding."""
    n0: float
    m: float
    K: float

    def __post_init__(self):
        if min(self.n0, self.m, self.K) <= 0:
            raise ValueError("n0, m, K must be positive")

    @property
    def dilution(self):
        return self.n0 / (self.n0 + self.m)

    @property
    def n_eff(self):
        return self.m * self.n0 / (self.n0 + self.m)

    def post_money(self, x):
        return (np.asarray(x, float) * self.n0 + self.m * self.K) / (self.n0 + self.m)

    def right_value_per_plan_share(self, x):
        return self.m / (self.n0 + self.m) * np.maximum(np.asarray(x, float) - self.K, 0.0)

    def backstop_payoff(self, x):
        """USD mm P&L of taking all unsubscribed shares under rational subscription."""
        return -self.n_eff * np.maximum(self.K - np.asarray(x, float), 0.0)

    def fair_fee(self, x0, sigma, T, r=0.0):
        """Fee (fraction of m*K, cash-equivalent) equal to the put the backstop sells."""
        return self.dilution * float(bs_put(x0, self.K, T, sigma, r)) / self.K


# Hertz share counts (8-K, 7 Jul 2021), in millions
HZ_RIGHTS_PART, HZ_UNSUB, HZ_FEE = 127.362114, 36.137887, 16.35
HZ_SPONSOR, HZ_OLD3PCT, HZ_TOTAL = 277.119438, 14.133075, 471.102514
hz_m = HZ_RIGHTS_PART + HZ_UNSUB
hz_n0 = HZ_SPONSOR + HZ_OLD3PCT
assert abs(hz_m * 10.0 - 1635.0) < 1e-3                       # $1.635bn at $10
assert abs(hz_m + hz_n0 + HZ_FEE - HZ_TOTAL) < 1e-6           # rows sum exactly
assert abs(HZ_FEE / hz_m - 0.10) < 1e-6                       # 10% fee in shares
hz = RightsOffering(n0=hz_n0, m=hz_m, K=10.0)
assert 0.63 < hz.dilution < 0.65

# identities
x_test = np.array([5.0, 10.0, 15.0])
assert np.allclose(hz.post_money(x_test) - 10.0, hz.dilution * (x_test - 10.0))
assert abs(bs_call(1.0, 0.75, 0.5, 0.7) - bs_put(1.0, 0.75, 0.5, 0.7) - 0.25) < 1e-12   # parity, r=0

# worked number: 25% discount, 70% vol, six months
gen = RightsOffering(n0=hz_n0, m=hz_m, K=0.75)
assert abs(float(bs_put(1.0, 0.75, 0.5, 0.7)) / 0.75 - 0.0979) < 0.002
f_star = gen.fair_fee(1.0, 0.70, 0.5)
assert 0.058 < f_star < 0.067, f_star

# Monte Carlo check of the short put (driftless lognormal under P)
sig, T = 0.70, 0.5
Z = RNG.standard_normal(400_000)
x_T = np.exp(-0.5 * sig**2 * T + sig * np.sqrt(T) * Z)
mc = gen.backstop_payoff(x_T).mean()
cf = -gen.n_eff * float(bs_put(1.0, 0.75, T, sig))
assert abs(mc / cf - 1.0) < 0.02, (mc, cf)

# fee table: fee and discount are substitutes
fee_table = {}
for disc in (0.0, 0.25, 0.50):
    for T_ in (0.25, 0.50):
        ro = RightsOffering(n0=hz_n0, m=hz_m, K=1.0 - disc)
        fee_table[(disc, T_)] = ro.fair_fee(1.0, 0.70, T_)
assert fee_table[(0.0, 0.5)] > fee_table[(0.25, 0.5)] > fee_table[(0.5, 0.5)]
assert 0.08 < fee_table[(0.0, 0.25)] < 0.10 and 0.115 < fee_table[(0.0, 0.5)] < 0.135

# Hertz, short window: even at the money the put is worth well under 10%
assert hz.fair_fee(10.0, 0.70, 0.10) < 0.07

# Hertz ex post at the $29 re-IPO price (USD mm)
fee_value = HZ_FEE * 29.0
unsub_gain = HZ_UNSUB * (29.0 - 10.0)
assert 1150 < fee_value + unsub_gain < 1170

for (disc, T_), f in sorted(fee_table.items()):
    print(f"discount {disc:4.0%}  T={T_:.2f}y  fair fee {f:6.2%}")
print(f"Hertz ex post: fee shares ${fee_value:,.0f}mm + unsubscribed gain ${unsub_gain:,.0f}mm")
```

### Deep-Dive Resource Graph

- **Podcasts:** *Bloomberg Odd Lots* and the *Petition* team's writing have covered backstop economics in the context of liability management; no specific episode cited.
- **Practitioner Writing:** Gunjan Seth, *Do Rights Offerings Reduce Bargaining Complexity in Chapter 11?*, CLS Blue Sky Blog (11 Mar 2025), https://clsbluesky.law.columbia.edu/2025/03/11/do-rights-offerings-reduce-bargaining-complexity-in-chapter-11/ ; Lowenstein Sandler, *ConvergeOne Decision: Fifth Circuit Weighs In On Unequal Treatment, Plan Finality* (via Mondaq, Dec 2025), https://www.mondaq.com/unitedstates/insolvencybankruptcy/1719792/convergeone-decision-fifth-circuit-weighs-in-on-unequal-treatment-plan-finality-video ; Bloomberg Law, *Fifth Circuit Decisions Level the Playing Field for Creditors* (30 Jan 2026), https://news.bloomberglaw.com/business-and-practice/fifth-circuit-decisions-level-the-playing-field-for-creditors
- **Academic Papers:** Buccola, Marcovich Gross & McBrady, *The Backstop Party*, *American Bankruptcy Law Journal* 100(1) (2026); Seth, *Do Rights Offerings Reduce Bargaining Complexity in Chapter 11?* (working paper, NBER conference version 2024).
- **Data & Code:** Hertz 8-K/A on the plan sponsor auction (14 May 2021), https://www.sec.gov/Archives/edgar/data/1657853/000110465921066944/tm2116104d2_8k.htm ; Hertz 8-K on the effective date (7 Jul 2021), https://www.sec.gov/Archives/edgar/data/1657853/000110465921089858/tm2121430d1_8k.htm
