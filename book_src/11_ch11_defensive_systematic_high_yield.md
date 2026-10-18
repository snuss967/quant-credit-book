# Chapter 11: Defensive Systematic High Yield

<!-- WRITER PLAN (sections appended in order as drafted; resume after the last complete "## 11.x" section):
11.0 Cold open; 11.1 The asymmetry; 11.2 Capture ratios and the beta-tilt diagnosis (Trend Watch, Case Study 1, code block 1);
11.3 Structural PD (code block 2); 11.4 Hazard models, labels, ML (code block 3); 11.5 Validation and the 77% (Trend Watch, code block 4);
11.6 The CCC problem (Case Study 3, Docket Diary); 11.7 Quality and low-risk tilts (code block 5);
11.8 Regime-aware exposure (Case Study 2); 11.9 Capacity (Trend Watch, code block 6);
11.10 Desk Debrief; The Spec You Hand the Robot; Exercises; Deep-Dive Resource Graph. -->

## 11.0 Cold Open: The Bow Tie

Thursday, 15 October 2026, 4:05 p.m. The close came up on Theo's second monitor as two numbers that did not look like they belonged to the same asset class. ICE BofA US High Yield Index option-adjusted spread: 323bp. ICE BofA CCC & Lower: 1,278bp.

Ines rolled her chair over without being asked, which was how Theo knew he was about to be taught something.

"What's the pot, Theo?"

"The index says it's a quiet Thursday."

"And the CCC tier?"

"The CCC tier says something happened and nobody told the index."

"So who at this table knows more than you?" She tapped the screen. "Not the index. The index is more than half double-B. It's wearing a 323 basis point bow tie. The CCCs are wearing a 1,278 basis point necktie. Same companies' cousins, different dress code."

Theo reached for the USB stick on his lanyard. The 13-week cash flow model had been his companion through four restructurings and one divorce of a client from its sponsor. It did not cover 2,000 issuers. It covered one, very well, for thirteen weeks.

Kaz looked up from a rating-agency release. "This says the issuer is in *selective default*. Selective like a university?"

"Selective like the sponsor chose which lenders got paid," Theo said.

Mags did not look up at all. "Back in my day, CCCs did minus 30.6% in 2000 and plus 50.8% in 2003, and nobody called either one a regime. We called the first one 'the year' and the second one 'the other year.' The people who avoided all the defaults in 2000 were too scared to buy in 2003. They were very well protected. They were also very poor."

Ines pulled up a single slide from a BlackRock white paper: the average high yield manager, eVestment data, 2005 to 2025. Downside capture 89.56%. Upside capture 92.24%.

"That's a player who folds ten percent of every hand," she said. "Including the ones they would have won. A capture ratio is a hand history, not a skill. Your job is to fold the hands that lose and play the hands that win. That is a different job from playing ten percent smaller."

Theo looked at the bow tie and the necktie. "So the question is how you avoid the defaults without missing the rebounds."

"That," said Ines, "is the whole game."

By the end of this chapter you will be able to: write down the return distribution of a high yield bond as a mixture and say exactly where its negative skew comes from; diagnose a "defensive" track record as a beta tilt or as genuine convexity using capture ratios and an asymmetric-beta regression; build a probability-of-default (PD) engine from distance-to-default and a dynamic logit hazard, label it correctly in an era where most defaults are distressed exchanges, and validate it with power curves; read a vendor claim such as "77% of defaults identified within 24 months" and ask the one question it does not answer; size the CCC bucket by expected loss rather than by fear; construct a DTS-neutral defensive portfolio that keeps its beta at one; and estimate how much money any of this can absorb before the costs eat the alpha.

## 11.1 The Asymmetry: Why High Yield Needs a Defense at All

Ines frames high yield the way a poker player frames selling insurance. "You collect the ante every hand. Most hands, nobody calls. Then one hand, somebody calls, and you pay out the whole pot. A high yield bond is a short put that sends you a coupon." The RSSG reader knows the second half of the sentence from the inside: the restructuring is the hand where the put gets exercised, and the recovery waterfall is the payout schedule.

The upside of a bond is capped near par (call schedules make it worse: a callable B bond trading at 103 is a bond whose issuer is waiting for you to get comfortable). The downside is a jump to recovery. The question for this section is how much of the distribution that jump owns, and the answer is "more than its probability suggests."

### 11.1.1 The mixture return and where the skew comes from

Fix a horizon $h$ (one year). Under the physical measure $\mathbb{P}$, a bond either survives or defaults. If it survives, its excess return over duration-matched Treasuries is carry $c$ minus spread duration times the spread change, $c - D^{\text{spr}}\Delta s$. If it defaults, it jumps from price $P_0$ to recovery $R$ (in price points). Let $J = \mathbb{1}_{\tau \le h}$ be the default indicator with $\mathbb{P}(J=1)=p$, and define the *price-based* loss

$$
L_P \equiv \frac{P_0 - R}{P_0}.
$$

The one-period excess return is the mixture

$$
r = (1-J)\,Y + J\,(-L_P), \qquad Y \equiv c - D^{\text{spr}}\Delta s,
$$

where $Y$ has mean $m$ and variance $v$ and we take $J$ independent of $Y$ (a simplification: in practice spreads widen before default, which only makes the left tail worse). The first moment is immediate:

$$
\mathbb{E}^{\mathbb{P}}[r] = (1-p)\,m - p\,L_P.
$$

For the variance, compute the second moment, $\mathbb{E}[r^2] = (1-p)(v+m^2) + pL_P^2$, and subtract the squared mean $(1-p)^2m^2 - 2p(1-p)mL_P + p^2L_P^2$. Collecting terms, $(1-p)m^2 - (1-p)^2m^2 = p(1-p)m^2$ and $pL_P^2 - p^2L_P^2 = p(1-p)L_P^2$, so

$$
\operatorname{Var}^{\mathbb{P}}[r] = (1-p)\,v + p(1-p)\,(m + L_P)^2 .
$$

The second term is the jump. Its size is set by $m + L_P$, the distance between "survive and clip the coupon" and "default and lose the price," which for a high yield bond is an order of magnitude larger than $\sqrt{v}$.

Now isolate the jump component, $-L_P J$. A Bernoulli variable has skewness $(1-2p)/\sqrt{p(1-p)}$, and multiplying by the negative constant $-L_P$ flips the sign:

$$
\operatorname{Skew}[-L_P J] = -\frac{1-2p}{\sqrt{p(1-p)}}.
$$

At $p = 2\%$ the skew is $-0.96/0.14 = -6.9$; at $p = 5\%$ it is $-0.90/0.218 = -4.1$; at $p = 20\%$ it is $-0.60/0.40 = -1.5$.

Read that table twice, because it is counterintuitive. The *safer* the bond, the *more* skewed its default component. A double-B bond's risk is a rare disaster: small, frequent coupons and one catastrophic outcome that almost never happens. A deep CCC bond's default is common enough that its distribution starts to look like an ordinary, very volatile, merely lopsided asset. This is the precise sense in which a CCC bond is an equity option that wears a tie to work: as $p$ rises the bond's payoff converges on the shape of the residual claim on the firm, and the tie is the coupon. It also tells you why the two halves of high yield need different defenses. In the BB tier the job is to avoid the rare jump; in the CCC tier the jump is the base case and the job is to price it.

### 11.1.2 The credit triangle, with the measure stated

For small $p$, with carry approximately equal to spread ($c \approx s$) and no expected spread change ($m \approx s$), the mean collapses to the credit triangle written under $\mathbb{P}$:

$$
\mathbb{E}^{\mathbb{P}}[r^{xs}] \approx s - \lambda^{\mathbb{P}} L,
$$

with $\lambda^{\mathbb{P}}$ the physical default intensity and $L$ the loss. The break-even physical default rate is $\lambda^\ast = s/L$. Under the recovery-of-market-value (RMV) convention the risk-neutral version $s = \lambda^{\mathbb{Q}} L_P$ holds exactly in continuous time, and that is why $L$ must be measured from *price*: a CCC bond at 70 with a recovery of 28 loses $L_P = 60\%$, not the 72% its par-based loss would suggest.

Three errors live in this one line. The first is mixing measures: a CDS-implied $\lambda^{\mathbb{Q}}$ includes the risk premium, so $s - \lambda^{\mathbb{Q}}L \approx 0$ by construction and tells you nothing about expected return. The second is importing the 40% CDS recovery convention as a $\mathbb{P}$ recovery: Moody's 1970–2002 mean recovery was 43.10% in expansions but 27.85% in recessions (Schmid p.103), and defaults cluster in recessions, so the default-weighted recovery is closer to the second number. The third is the par-versus-price confusion above.

Here is what break-even looks like on the cold-open close, with spreads from FRED for 15 October 2026 (BB 197bp, B 326bp, CCC & lower 1,278bp) and two loss assumptions:

| Tier | OAS (bp) | $\lambda^\ast$ at $L=0.60$ | $\lambda^\ast$ at $L=0.72$ | S&P one-year default rate, 1980–2002 (Schmid p.28) |
| :--- | ---: | ---: | ---: | ---: |
| BB | 197 | 3.3% | 2.7% | 1.53% |
| B | 326 | 5.4% | 4.5% | 6.95% |
| CCC | 1,278 | 21.3% | 17.8% | 31.58% |

*(Break-even rates are our computation; the historical column is the NR-adjusted S&P table reproduced in Schmid.)* On the 1980–2002 table, which contains three recessions, both single-B and CCC would be negative-expectation bets at today's spreads. On Moody's forward one-year PD of 3.2% for the average US high yield company in Q1 2026 (Moody's Analytics, *Lend, extend, and then…*, 18 May 2026), the index as a whole is comfortably paid. Which number applies to the bond in front of you is the subject of the rest of this chapter. The tier average is not the answer, because the tier is a crowd and you are buying one person in it.

> **[SOURCE EXTRACTION]** *Man_Quantitative_Credit_Alpha_Early_Mover_2022 p.26:* "the tightening of a bond on the upside to risk free rates is typically asymmetrically smaller than the jump to recovery in situations of distress. Low-risk factor signals target shorter-dated, higher-rated bonds."
>
> **Annotation.** Man Group puts the whole chapter into two sentences: the asymmetry is the reason a low-risk factor exists at all. The first sentence is the mixture derivation in words: the upside is bounded by the spread you can tighten toward zero, the downside by the price you can lose. The second sentence is a design choice, and it is where a 2026 desk should push back gently. "Shorter-dated, higher-rated" is a proxy for low PD, chosen because ratings and maturity are free and universal. A desk with a calibrated PD can target the thing itself, and the difference matters in exactly the cases an RSSG banker cares about: a short-dated single-B bond with a maturity wall in fourteen months is not low-risk, it is a refinancing event with a coupon, and a long-dated double-B issued by a sponsor-owned company with a large unrestricted-subsidiary basket is higher-rated than its priming risk deserves (Chapter 13). Use the proxy as a fallback feature, not as the definition.

> **[SOURCE EXTRACTION]** *Moyer_Distressed_Debt_Analysis p.25:* "If CCC-rated bonds are, for convenience, used as a proxy for distressed, then the negative market returns for this group over the 1999–2002 period, shown in Table 1-2, illustrate the dangers, while 2003 returns demonstrate the opportunity."
>
> **Annotation.** Moyer's Table 1-2 (CSFB data) is Mags's war story in print: CCC returns of −3.0% in 1999, −30.6% in 2000, −2.1% in 2001, −12.7% in 2002, and +50.8% in 2003. Compound the five years and a dollar becomes about \$0.87: four years of losing, then one year that recovered most of it. Now run the two classic "defensive" responses through it. Exclude CCC entirely and you sidestep 2000 and 2002 but forfeit 2003, and whether that wins the round trip depends entirely on where you parked the money and whether you had the nerve to come back in January 2003 (nobody did). Exclude the CCCs that *default* and you keep most of 2003, because the 2003 rally was earned by the survivors repricing from distressed to merely leveraged. The lesson for a systematic desk is that the tier is the wrong unit of decision. The PD-ranked issuer is the right one, and the rest of this chapter builds it.

## 11.2 The Average Manager's Dimmer Switch: Capture Ratios and the Beta-Tilt Diagnosis

BlackRock's 2025 white paper on systematic high yield opens with a diagnosis that should make every long-only HY allocator slightly uncomfortable. Across eVestment data from 2005 to 2025, net of fees, the average US high yield manager captured 89.56% of down markets and 92.24% of up markets; the top-quartile manager captured 92.00% of the down and 99.00% of the up (BlackRock p.3). The paper's verdict on the average manager is that the defense came "largely" from a lower beta. Ines's verdict is shorter: "A dimmer switch is not a strategy. It's a strategy with the lights turned down."

### 11.2.1 The capture-ratio identity

Split benchmark months into up months $\mathcal{U} = \{t : r_{b,t} > 0\}$ and down months $\mathcal{D} = \{t : r_{b,t} < 0\}$. Using arithmetic means (eVestment uses annualized geometric means; the algebra is the same to first order), upside and downside capture are

$$
U = \frac{\bar r_p^{\,\mathcal{U}}}{\bar r_b^{\,\mathcal{U}}}, \qquad D = \frac{\bar r_p^{\,\mathcal{D}}}{\bar r_b^{\,\mathcal{D}}}.
$$

Suppose the portfolio follows a single-index model $r_{p,t} = \alpha + \beta r_{b,t} + \epsilon_t$ with residuals averaging to zero within each regime. Averaging over up months gives $\bar r_p^{\,\mathcal{U}} = \alpha + \beta\,\bar r_b^{\,\mathcal{U}}$, so

$$
U = \beta + \frac{\alpha}{\bar r_b^{\,\mathcal{U}}}, \qquad D = \beta + \frac{\alpha}{\bar r_b^{\,\mathcal{D}}}.
$$

Because $\bar r_b^{\,\mathcal{D}} < 0$, a positive alpha raises $U$ above $\beta$ and pushes $D$ below it. Subtracting,

$$
U - D = \alpha\left(\frac{1}{\bar r_b^{\,\mathcal{U}}} + \frac{1}{\lvert \bar r_b^{\,\mathcal{D}} \rvert}\right),
$$

which is positive if and only if $\alpha > 0$. Two corollaries do most of the work on a due-diligence call. First, a pure beta tilt ($\alpha = 0$) gives $U = D = \beta$: every point of downside "protection" is paid for with a point of upside. Second, the *gap* $U - D$ measures alpha, and the *level* $(U + D)/2$ is roughly beta.

Put illustrative regime means into the identity: up months average $+1.6\%$ and down months $-2.0\%$ *(illustrative; the paper reports only the capture ratios)*. Then $1/0.016 + 1/0.020 = 112.5$, and

| Manager (BlackRock p.3) | $U$ | $D$ | Implied $\alpha$ (per year) | Implied $\beta$ |
| :--- | ---: | ---: | ---: | ---: |
| Average | 92.24% | 89.56% | $\approx 29$bp | $\approx 0.91$ |
| Top quartile | 99.00% | 92.00% | $\approx 75$bp | $\approx 0.95$ |

*(Our decomposition under the illustrative regime means.)* The average manager is a 0.91-beta portfolio with a small net alpha. The top-quartile manager is better on both counts, but still a sub-one beta: even the good players fold some winning hands.

Why does a 0.91 beta cost money over a cycle? Because high yield's excess return is positive on average and the regimes are lopsided. BlackRock buckets monthly ICE BofA HY Constrained returns at $\pm1.5\%$ and counts 168 positive months against 72 negative ones (BlackRock p.4). A beta of $\beta$ forfeits $(1-\beta)$ of the risk premium in every one of the 168, and recovers $(1-\beta)$ of the losses in each of the 72. Unless the down months are much deeper than the up months are frequent, the dimmer switch loses the round trip.

### 11.2.2 Convexity: the asymmetric-beta regression

Real defense means the portfolio responds *less* to down months than to up months. Write the Henriksson–Merton style asymmetric regression

$$
r_{p,t} = \alpha + \beta^{+}\max(r_{b,t}, 0) + \beta^{-}\min(r_{b,t}, 0) + \epsilon_t .
$$

Averaging within regimes as before, $U = \beta^{+} + \alpha/\bar r_b^{\,\mathcal{U}}$ and $D = \beta^{-} + \alpha/\bar r_b^{\,\mathcal{D}}$. "Good defense" is $\beta^{-} < \beta^{+}$: positive convexity in the active return. Where can convexity come from in a long-only bond portfolio? Only two places. One is security selection that avoids the jump, because defaults and distress cluster in down months, so a portfolio that holds fewer of the bonds that jump has a lower down-beta without a lower up-beta. The other is regime-aware exposure that adds risk after spreads overshoot (§11.8). A uniform beta tilt cannot produce it; it scales both betas together.

Three traps for the person computing these numbers. Compute capture on *excess* returns if the mandate is excess-return; total-return capture smuggles in rate duration. Define regimes on the benchmark, never on the portfolio. And when $\lvert \bar r_b^{\,\mathcal{D}} \rvert$ is small (a short sample with a few mild down months), $D$ explodes; require a floor and report the regime counts.

> **[SOURCE EXTRACTION]** *BlackRock_Systematic_High_Yield_Credit p.3:* "Figure 1 shows the average manager tended to participate in 89.56% of down markets and 92.24% of up markets. This illustrates how the average U.S. high yield manager was building a “defensive” exposure largely by creating a portfolio that has a lower beta than the broad index."
>
> **Annotation.** The quotation marks around "defensive" are BlackRock's, and they are doing honest work. Our identity says the paper's numbers are consistent with a beta of about 0.91 and a small alpha, which is a polite way of saying the industry's defense is mostly cash drag, short duration, and an underweight in the riskiest tier. Two cautions before you repeat the number in a pitch. eVestment figures are net of fees, so the gross alpha of the average manager is larger than our 29bp, and the sample has survivorship in it, because managers who closed are not in the 2025 cross-section. And a sub-one beta is not *wrong* for a client who wants lower volatility; it is wrong for a client who is paying active fees for something they could get by holding 9% cash. The modern desk's response is to make beta a separately managed exposure (index, CDX HY, or ETF overlay, see Chapter 8) and to demand that the active book earn its keep through $\beta^{-} < \beta^{+}$.

> **[SOURCE EXTRACTION]** *BlackRock_Systematic_High_Yield_Credit p.5:* "In many cases, these managers gave up more excess return in subsequent “Very Positive” regimes than was mitigated on the downside during “Very Negative” regimes."
>
> **Annotation.** This is the round-trip cost measured, not argued. BlackRock pairs adjacent regimes (June/July 2013, December 2018/January 2019, March/April 2020, June/July 2022, September/October 2022) and shows the average manager giving back on the rebound what it saved on the drop. In poker terms the hand history shows a player who folds the river every time the flop looks scary, including on the hands where the scary flop was followed by a winning card. The point for a systematic builder is that the defense must be evaluated on *pairs* of regimes, not on down months alone, because a model that looks heroic in March 2020 and is underinvested in April 2020 is a model that has learned fear. Build the evaluation set as regime pairs and you will reject that model before a client does.

> **Trend Watch: The Whipsaw Years, 2022–2026.** *What changed:* high yield stopped trending and started reversing, which is the regime where a beta tilt does worst. *When and how big:* 2022, US HY "down over 11%"; 2023, "up over 13%" (BlackRock p.3, Bloomberg data as of 31 March 2024). The average manager beat the benchmark by 0.47% in 2022 and lagged by 0.68% in 2023 (BlackRock p.4), giving back more than it saved. In 2024 the pattern repeated at a smaller scale: +0.35% versus benchmark in Q1, −0.37% over the rest of the year (BlackRock p.5). The ICE BofA US High Yield total return index returned +8.20% in calendar 2024 and +8.50% in 2025, then fell 3.83% from 28 February to 7 April 2025 on the tariff shock and regained its prior peak on 12 May 2025, a ten-week V; in 2026 it fell 2.87% from 27 August to 1 October and stood +0.15% year-to-date on 15 October *(our computations from FRED series BAMLHYH0A0HYM2TRIV)*. *What it means for the desk:* shallow, fast V-shaped drawdowns are the worst environment for a strategy that de-risks on price, and the best environment for one that de-risks on default probability, because PDs barely move in a ten-week V while prices move a lot. The whipsaw years are the empirical case for issuer-level defense.

### 11.2.3 Case Study 1: The 2022–2023 Round Trip

The benchmark facts are BlackRock's: high yield down more than 11% in 2022 and up more than 13% in 2023, with two regime pairs inside 2022 of −6.8%/+6.0% (June/July) and −4.0%/+2.8% (September/October) (BlackRock p.5, Figure 3). The average manager finished 2022 ahead and 2023 behind, and the cumulative result over the two years was a net giveback (p.4).

Now run three stylized portfolios through the June/July 2022 pair *(illustrative; only the benchmark returns are sourced)*. The beta tilt at $\beta = 0.91$ returns $-6.19\%$ then $+5.46\%$, a cumulative $-1.07\%$ against the benchmark's $-1.21\%$: a 14bp win, almost entirely from compounding on a down-then-up path. The issuer-level defender holds $\beta^{+} = 1.0$ and, by avoiding the bonds that gap in a down month, achieves $\beta^{-} = 0.90$: $-6.12\%$ then $+6.00\%$, a cumulative $-0.49\%$, a 72bp win. The third portfolio is the one a nervous committee builds in real time: it cuts to $\beta = 0.8$ at the end of June after the loss and rides July at that beta, $-6.80\%$ then $+4.80\%$, cumulative $-2.33\%$, a 112bp *loss* to the benchmark it was trying to protect against.

The desk read is that the second portfolio's advantage is not a forecast of the market. It is a forecast of *which bonds* fall more than their spread duration predicts, which is a default and distress forecast. That is what §11.3 through §11.5 build.

### Specification for AI Implementation

**The Spec You Hand the Robot (vague version, and what ROBO built).** Theo's first message was "Build a defensive high yield strategy that avoids defaults." ROBO sold every bond rated below BB and bought Treasury bills. Realized defaults: zero. Downside capture: 0%. Upside capture: 0%. Tracking error to the HY index: roughly the index's own volatility. Clients: also zero. ROBO did exactly what was asked. The precise version says what "defensive" is measured against: *report $U$, $D$, $\beta^{+}$, $\beta^{-}$ on benchmark-defined regimes, on excess returns, with a floor on the down-month mean; the portfolio must hold $w^\top \text{DTS}$ within 2% of the benchmark's.* The code below is the first of six cumulative blocks; later blocks reuse its imports and functions.

**Schema.** `rp`, `rb`: `float64` arrays of shape `(T,)`, monthly excess returns in decimal, aligned by month. `T >= 24`, at least 3 up and 3 down benchmark months. Output of `capture_ratios`: tuple `(U, D)` as decimals. Output of `asymmetric_beta`: dict with `alpha` (per month), `beta_up`, `beta_dn`.

```python
# Block 1: capture ratios and asymmetric beta (Section 11.2)
import numpy as np
import pandas as pd
from scipy import optimize, special, stats

RNG_SEED = 11


def capture_ratios(rp, rb, floor=1e-4):
    """Arithmetic upside/downside capture on benchmark-defined regimes."""
    rp = np.asarray(rp, dtype=float)
    rb = np.asarray(rb, dtype=float)
    if rp.shape != rb.shape or rp.ndim != 1:
        raise ValueError("rp and rb must be aligned 1-D arrays")
    up, dn = rb > 0, rb < 0
    if up.sum() < 3 or dn.sum() < 3:
        raise ValueError("need at least 3 up and 3 down benchmark months")
    mu_up, mu_dn = rb[up].mean(), rb[dn].mean()
    if mu_up < floor or abs(mu_dn) < floor:
        raise ValueError("benchmark regime mean too close to zero; capture undefined")
    return rp[up].mean() / mu_up, rp[dn].mean() / mu_dn


def asymmetric_beta(rp, rb):
    """OLS of rp on [1, max(rb,0), min(rb,0)]; good defense means beta_dn < beta_up."""
    rp = np.asarray(rp, dtype=float)
    rb = np.asarray(rb, dtype=float)
    X = np.column_stack([np.ones_like(rb), np.maximum(rb, 0.0), np.minimum(rb, 0.0)])
    coef, *_ = np.linalg.lstsq(X, rp, rcond=None)
    return {"alpha": coef[0], "beta_up": coef[1], "beta_dn": coef[2]}


rng = np.random.default_rng(RNG_SEED)
rb_demo = rng.normal(0.004, 0.022, 240)          # 20 years of monthly HY excess returns (synthetic)

# Sanity 1: a pure beta tilt has U == D == beta exactly.
U, D = capture_ratios(0.9 * rb_demo, rb_demo)
assert abs(U - 0.9) < 1e-12 and abs(D - 0.9) < 1e-12

# Sanity 2: positive alpha opens the gap U > D (the identity of Section 11.2.1).
U_a, D_a = capture_ratios(0.001 + 0.9 * rb_demo, rb_demo)
assert U_a > 0.9 > D_a

# Sanity 3: the identity U - D = alpha * (1/mu_up + 1/|mu_dn|) holds exactly with zero residual.
mu_up = rb_demo[rb_demo > 0].mean()
mu_dn = rb_demo[rb_demo < 0].mean()
assert abs((U_a - D_a) - 0.001 * (1 / mu_up + 1 / abs(mu_dn))) < 1e-12

# Sanity 4: the asymmetric regression sees through a beta tilt and recovers real convexity.
tilt = asymmetric_beta(0.9 * rb_demo, rb_demo)
assert abs(tilt["beta_up"] - 0.9) < 1e-10 and abs(tilt["beta_dn"] - 0.9) < 1e-10
convex_rp = (0.0005 + 1.0 * np.maximum(rb_demo, 0) + 0.8 * np.minimum(rb_demo, 0)
             + rng.normal(0.0, 0.002, rb_demo.size))
cvx = asymmetric_beta(convex_rp, rb_demo)
assert cvx["beta_dn"] < cvx["beta_up"] - 0.1
print(f"beta tilt: U={U:.4f} D={D:.4f} | convex: beta_up={cvx['beta_up']:.3f} "
      f"beta_dn={cvx['beta_dn']:.3f} alpha/yr={12 * cvx['alpha']:.4f}")
```

**Edge cases for ROBO.** Months where the benchmark return is exactly zero belong to neither regime; they are excluded, not assigned. Missing portfolio months are dropped pairwise, never forward-filled (a forward-filled month is a month of zero return, which is a beta of zero in disguise). Report regime counts alongside every capture ratio.

## 11.3 Default Avoidance I: The Structural PD

Theo's first instinct was the right one, at the wrong scale. An RSSG banker decides whether a company will default by building its liabilities, its liquidity, and its enterprise value, then asking whether the value covers the claims. Merton (1974) is the same judgment written as an option, and its industrial descendant, the KMV expected default frequency, is how firms like BlackRock and Blackstone run the judgment on every issuer every night. BlackRock's signal "centers on a simple economic assumption that default occurs when the value of a firm's assets fall below the value of its liabilities" (BlackRock p.6). That sentence is Merton's model, and also, Theo noted, the first page of every fairness opinion he ever drafted.

> **[SOURCE EXTRACTION]** *Blackstone_Systematic_Credit p.1:* "By relying on these proprietary, computationally derived default probabilities rather than sluggish rating agency downgrades or upgrades, the algorithm can objectively compare creditworthiness across the entire global corporate universe"
>
> **Annotation.** Blackstone's systematic credit platform grew out of its late-2020 acquisition of DCI, whose co-founders created the KMV model (Blackstone p.1–2), so this is the structural-model lineage speaking about itself. The two words that matter are "sluggish" and "compare." Ratings move late (Ben Dor p.288: a spread-based indicator registers deterioration "much faster" than a ratings-based one) and they are ordinal, so a B2 in software and a B2 in retail are not the same risk. A PD is cardinal: it can be multiplied by a loss and subtracted from a spread, which is what the credit triangle of §11.1.2 needs. The modern caution is the word "entire." The structural model needs a traded equity, and a large share of US high yield issuers are sponsor-owned with no listed stock. For those names the "computationally derived" PD is either bond-implied (circular, since you are using the spread to forecast the spread) or accounting-only (slow). Flag which regime each PD came from and let the model treat the flag as a feature.

### 11.3.1 Equity as a call, solved backward

Let the firm's assets $V_t$ follow a geometric Brownian motion under $\mathbb{P}$ with drift $\mu$ and volatility $\sigma_V$, and let debt be a single zero with face $F$ due at $T$. Equity is a European call on the assets:

$$
E = V\,N(d_1) - F e^{-rT} N(d_2), \qquad d_{1,2} = \frac{\ln(V/F) + \left(r \pm \tfrac12\sigma_V^2\right)T}{\sigma_V\sqrt{T}} .
$$

We observe $E$ (market capitalization) and $\sigma_E$ (equity volatility), not $V$ and $\sigma_V$. The second equation comes from Itô's lemma. Write $E = f(V,t)$; then $dE = f_V\,dV + (\ldots)\,dt$, so the diffusion term of $dE$ is $f_V\,\sigma_V V\,dW_t$. Dividing by $E$, the equity volatility is $\sigma_E = f_V \sigma_V V/E$, and since the call's delta is $f_V = N(d_1)$,

$$
\sigma_E\,E = N(d_1)\,\sigma_V\,V .
$$

Two equations, two unknowns. For a fixed $\sigma_V$, the call value is strictly increasing in $V$, so $V(\sigma_V)$ is found by a bracketed root search on $[E,\, E + 2F]$: at $V = E$ the call is worth less than $E$, and at $V = E + 2F$ it is worth at least $V - Fe^{-rT} > E$. Then search over $\sigma_V \in (0, \sigma_E]$ for the root of $\sigma_V V(\sigma_V) N(d_1) - \sigma_E E$. The upper end works because $E \le V N(d_1)$, so the gap is non-negative at $\sigma_V = \sigma_E$; the lower end works because the gap tends to $-\sigma_E E$. The leverage effect is visible in the answer: $\sigma_V = \sigma_E E/(V N(d_1)) < \sigma_E$, and the more debt, the bigger the gap between the two volatilities.

Distance-to-default is the number of asset standard deviations between expected asset value and the default point at the horizon, under the *physical* drift:

$$
\text{DD}_T = \frac{\ln(V/F) + \left(\mu - \tfrac12\sigma_V^2\right)T}{\sigma_V\sqrt{T}} .
$$

Under $\mathbb{Q}$ the same expression with $r$ in place of $\mu$ is $d_2$, and $N(-d_2)$ is the risk-neutral default probability that belongs in pricing, not in a PD forecast. For a firm with coupon debt of many maturities, the Vasicek–Kealhofer convention sets the default point to short-term debt plus half of long-term debt, $F = \text{STD} + \tfrac12\text{LTD}$, an empirical compromise reflecting that long-dated debt does not have to be paid this year but does constrain the firm's ability to borrow.

### 11.3.2 The normal-distribution trap

Kaz ran the model on the cross-section and announced the result with the confidence of someone who has assumed Gaussian. "The median public firm has a distance-to-default above four. $N(-4) = 3.2\times10^{-5}$. So the median public firm has a default probability of three in a hundred thousand."

Mags did not look up. "The median public firm has not been informed."

> **[SOURCE EXTRACTION]** *Bohn_Stein_Active_Credit_Portfolio_Management p.138:* "This convenient distributional assumption is clearly unrealistic. This becomes clear when we observe that empirically the majority of publicly traded firms have DDs greater than 4."
>
> **Annotation.** Bohn and Stein are describing why Moody's KMV never used $N(-\text{DD})$: the tails of realized asset returns are far fatter than Gaussian, so DD is a good *ranking* and a terrible *probability*. The fix is an empirical map $\text{PD} = g(\text{DD})$, estimated by bucketing firm-years into DD cohorts and recording realized default frequencies; under their map a DD of 4 converts to an EDF of almost 1%, about 300 times the Gaussian answer (p.138). The calibration needs data: "at least 1,000 defaults, with a minimum of 400" (p.163). That threshold is an uncomfortable fact for a desk that wants a high-yield-only model, because the US HY universe produces a few dozen issuer defaults in a benign year. The 2026 answer is to calibrate the map on the broadest default history you can license (all rated and unrated corporates, multiple decades, the NUS Credit Research Initiative as a public benchmark) and to fit HY-specific *adjustments* on top, not to fit a fresh map on 300 HY defaults and call it bespoke.

Where the structural PD breaks in high yield, in descending order of how much money it has cost people: the issuer has no listed equity (Chapter 7 cites Dynkin p.651: on 31 May 2018 the US HY index had 784 issuers, of which 576 were public, so about a quarter of issuers have no $E$ to invert); the default point is wrong because a liability management transaction has just put \$800mm of new super-priority debt ahead of the bonds you own, which changes *your* recovery without moving the firm's DD (this is exactly the job of Chapter 13's Priming Risk Score); book equity is negative after years of dividend recaps, which matters for accounting covariates but not for Merton, which uses market values; and equity volatility is stale for thinly traded small caps, which makes $\sigma_E$ too low and DD too high.

### Specification for AI Implementation

**Schema.** Per issuer-date: `E` (market cap, \$mm, `> 0`), `sigma_E` (annualized decimal equity vol, `> 0`), `STD`, `LTD` (\$mm), `r` (continuously compounded, decimal), `mu` (physical asset drift, decimal), `T = 1.0` years. Output: `V`, `sigma_V`, `DD`, `PD` (12-month, $\mathbb{P}$). Issuers with `E <= 0` or no listed equity raise in the solver and must be routed to the accounting-only model with `no_equity_flag = 1`.

```python
# Block 2: Merton inversion, distance-to-default, empirical PD map (Section 11.3)

def _merton_call(V, sigma_V, F, r, T):
    sq = sigma_V * np.sqrt(T)
    d1 = (np.log(V / F) + (r + 0.5 * sigma_V ** 2) * T) / sq
    d2 = d1 - sq
    E = V * stats.norm.cdf(d1) - F * np.exp(-r * T) * stats.norm.cdf(d2)
    return E, d1, d2


def merton_solve(E, sigma_E, F, r, T=1.0):
    """Recover (V, sigma_V) from observed (E, sigma_E) by nested bracketed root searches."""
    if min(E, sigma_E, F, T) <= 0:
        raise ValueError("E, sigma_E, F, T must be positive; route issuer to accounting-only PD")
    v_hi = E + 2.0 * F * max(1.0, np.exp(-r * T))

    def V_of(sV):
        return optimize.brentq(lambda V: _merton_call(V, sV, F, r, T)[0] - E,
                               E, v_hi, xtol=1e-12, rtol=1e-14, maxiter=500)

    def gap(sV):
        V = V_of(sV)
        return sV * V * stats.norm.cdf(_merton_call(V, sV, F, r, T)[1]) - sigma_E * E

    if gap(sigma_E) <= 0.0:          # no leverage effect left (F negligible)
        return V_of(sigma_E), sigma_E
    sV = optimize.brentq(gap, 1e-6, sigma_E, xtol=1e-14, rtol=1e-14, maxiter=500)
    return V_of(sV), sV


def distance_to_default(V, sigma_V, F, mu, T=1.0):
    return (np.log(V / F) + (mu - 0.5 * sigma_V ** 2) * T) / (sigma_V * np.sqrt(T))


def kmv_default_point(std, ltd):
    return std + 0.5 * ltd


def empirical_pd(dd, a=-0.718, b=0.9718, pd_floor=1e-4, pd_cap=0.35):
    """Illustrative monotone DD -> 12m PD map: PD(4) ~ 1%, PD(0.5) ~ 30%, capped at 35%."""
    return np.clip(np.exp(a - b * np.asarray(dd, dtype=float)), pd_floor, pd_cap)


# Sanity 1: round trip. Generate (E, sigma_E) from known (V, sigma_V), then recover them.
for V0, sV0, F0 in [(100.0, 0.30, 75.0), (100.0, 0.25, 95.0)]:
    E0, d1_0, _ = _merton_call(V0, sV0, F0, 0.04, 1.0)
    sE0 = stats.norm.cdf(d1_0) * sV0 * V0 / E0
    V_hat, sV_hat = merton_solve(E0, sE0, F0, 0.04, 1.0)
    assert abs(V_hat / V0 - 1) < 1e-6 and abs(sV_hat / sV0 - 1) < 1e-6
    assert sV_hat < sE0                       # leverage effect: asset vol below equity vol

# Sanity 2: the empirical map is monotone and the Gaussian map is the Kaz trap.
grid = np.linspace(-2.0, 8.0, 201)
assert np.all(np.diff(empirical_pd(grid)) <= 0.0)
assert abs(float(empirical_pd(4.0)) - 0.01) < 5e-4
assert stats.norm.cdf(-4.0) < 1e-4            # 3.2e-5: "three in a hundred thousand"

# A sponsor-levered B issuer (illustrative, $mm): E=2,000, sigma_E=55%, STD=600, LTD=3,000.
F_hy = kmv_default_point(600.0, 3000.0)
V_hy, sV_hy = merton_solve(2000.0, 0.55, F_hy, 0.04, 1.0)
dd_hy = distance_to_default(V_hy, sV_hy, F_hy, mu=0.06)
assert dd_hy > 0 and float(empirical_pd(dd_hy)) > stats.norm.cdf(-dd_hy)
print(f"V={V_hy:,.0f} sigma_V={sV_hy:.3f} DD={dd_hy:.2f} "
      f"PD_emp={float(empirical_pd(dd_hy)):.3%} vs N(-DD)={stats.norm.cdf(-dd_hy):.3%}")
```

**Edge cases for ROBO.** Stale prices give `sigma_E = 0`: raise, do not divide. Equity vol must be annualized from daily returns with the same day count every time ($\sqrt{252}$), and estimated over a window long enough to be stable (one year) but short enough to see a crisis. Never feed equity vol in as asset vol. Never use `N(-DD)` as a PD.

## 11.4 Default Avoidance II: Hazard Models, Labels, and Gradient Boosting

If you asked Theo to list the covariates in his last distress memo, he would give you twenty: leverage, interest coverage, the springing covenant cushion, the revolver availability, the sponsor's fund vintage, the ABL borrowing base, the maturity wall, and the 13-week cash flow. The empirical literature's answer to "which of these predict default" is humbling. Shumway (2001), using a hazard model on bankruptcies, found that market size, past stock returns, and idiosyncratic return volatility are strongly related to bankruptcy, and that about half of the classic accounting ratios are statistically insignificant once those are in. Chava and Jarrow (2004) found that monthly data improves prediction substantially and that accounting variables add little once market variables are included. Campbell, Hilscher and Szilagyi (2008) built the canonical modern specification and found, as a bonus, that distressed stocks earn anomalously *low* returns, the equity cousin of the low-risk effect in §11.7.

The equity market, in other words, is running Theo's memo every day for free, and the price is the conclusion. The RSSG edge is not in the covariates the market already sees. It is in the label, in the structure, and in the forced sellers, which is where this section and §11.6 go.

### 11.4.1 Altman's Z, and the units trap

> **[SOURCE EXTRACTION]** *Moyer_Distressed_Debt_Analysis p.183:* "Z = 0.012 X1 + 0.014 X2 + 0.033 X3 + 0.006 X4 + 0.999 X5" … "Z-scores of <1.81 have been shown as highly predictive of a bankruptcy as long as two years in advance."
>
> **Annotation.** Altman's (1968) discriminant function: working capital, retained earnings, and EBIT over total assets, market equity over book liabilities, and sales over total assets. Moyer prints the original coefficients, which assume $X_1$ through $X_4$ are entered as *percentages* (so 12% is 12) and $X_5$ as a ratio. ROBO, handed the printed formula and a data feed of decimal ratios, built a model in which every firm's Z-score was 0.999 times its asset turnover plus rounding error. "The dominant factor is sales over assets," Kaz observed, "so the model's main question is whether the company does things." The familiar 1.2, 1.4, 3.3, 0.6, 1.0 version is the same model for decimal inputs. The modern desk keeps Altman for two reasons: as a fast accounting-only fallback for private issuers, and as a reminder that any model handed over without units will be implemented without units. Neither use justifies the 1968 cutoffs on a 2026 sponsor-owned balance sheet, where negative retained earnings are a capital-structure choice, not a symptom.

### 11.4.2 From static logit to the dynamic hazard

> **[SOURCE EXTRACTION]** *Bohn_Stein_Active_Credit_Portfolio_Management p.236:* "this class of discrete-choice models will produce biased estimates since they ignore the periods prior to default when a defaulting firm did not default but may have had a similar financial profile."
>
> **Annotation.** This is Shumway's critique as Bohn and Stein summarize it. A static model takes one observation per firm, usually the last year before default for defaulters, and throws away every earlier year in which the same firm looked just as sick and survived. The model then over-attributes default to whatever a sick firm looks like, and its PDs are too high for sick survivors. The fix is to use every firm-period as an observation. On a 2026 desk the lesson generalizes: any sample that selects on the outcome (one row per default, matched to a "similar" survivor) will flatter the model, which is Bohn and Stein's paired-sample warning at p.226 in another costume.

The discrete-time hazard for issuer $i$ in month $t$, given covariates observed $\ell$ months earlier, is

$$
h_i(t \mid x_{i,t-\ell}) = \mathbb{P}\big(\tau_i \in (t, t+1] \mid \tau_i > t,\, \mathcal{F}_{t-\ell}\big) = \frac{1}{1 + \exp\!\big(-(\alpha_0 + \beta^\top x_{i,t-\ell})\big)} .
$$

Shumway's equivalence result is that the likelihood of this hazard model is the likelihood of a logit estimated on firm-months, so a standard logit routine estimates it, with one correction: because each firm contributes many dependent rows, the logit's test statistics are overstated, and Shumway divides the chi-squared statistics by the average number of firm-periods per firm (Bohn–Stein p.237). The modern equivalent is an issuer-clustered sandwich covariance, which the code below uses. A 12-month PD is then either the compounded monthly hazard, $1 - \prod_{j=1}^{12}(1 - h_{i,t+j})$, or a logit fit directly to a 12-month-ahead label; the second is simpler but its overlapping windows make clustering mandatory.

The Campbell–Hilscher–Szilagyi covariates are worth memorizing as a checklist: net income over market-valued total assets (averaged), total liabilities over market-valued total assets, excess equity return over the index (averaged), idiosyncratic equity volatility, relative size, cash over market assets, market-to-book, and log price. To these the RSSG desk adds one covariate the literature does not have:

$$
x^{\text{runway}}_{i,t} = \min\!\left(13,\; \text{weeks until projected liquidity falls below the minimum-liquidity covenant}\right).
$$

"Why cap it at 13?" Kaz asked.

"Because that's a quarter," Theo said.

"Of what?"

"Of the year, Kaz." The 13-week model, reborn as a hazard covariate, turns out to be informative precisely where market covariates are blind: private issuers whose liquidity is visible in lender reporting and compliance certificates but not in an equity price.

If the model is fit on a sample whose default rate $\pi_s$ differs from the population rate $\pi$ (oversampled defaults, or a 2008-heavy window), shift the intercept:

$$
\operatorname{logit} \hat p^{\,\text{pop}} = \operatorname{logit} \hat p^{\,s} + \ln\frac{\pi\,(1 - \pi_s)}{\pi_s\,(1 - \pi)} .
$$

This follows from Bayes' rule: resampling changes the prior odds of default by the factor $\frac{\pi/(1-\pi)}{\pi_s/(1-\pi_s)}$ and leaves the likelihood ratio, and therefore the ranking, untouched. Bohn and Stein's point that "a poorly calibrated PD model can still be useful for ranking obligors as long as the model has predictive power" (p.247) is the same statement read the other way: power and calibration are separate repairs.

### 11.4.3 The label is the model

Here the RSSG reader stops being a student and becomes the teacher. In 2025, 65% of all corporate defaults counted by Moody's were distressed exchanges, not hard defaults (Moody's Analytics, *Lend, extend, and then…*, 18 May 2026). A distressed exchange is a default that files its own press release as "liability management." If your training set calls it survival, the model learns that the way never to default is to default softly, and every sponsor-owned issuer with a drop-down basket becomes, in the model's eyes, a survivor.

Kaz read the rating-agency definition aloud, more or less: an exchange in which holders receive a diminished financial obligation, undertaken to help the issuer avoid a default.

"So the purpose of the default is to avoid default," Kaz said.

The Ad Hoc Group, in unison, represented by counsel: "We object to the characterization."

The desk label is therefore *any* of: missed payment beyond grace, bankruptcy filing, distressed exchange, or an LME that impairs the holder (uptier, drop-down with guarantee release, par-reducing exchange), within the horizon. The label must be date-stamped at the transaction's announcement, not its closing, or the model will learn from news it could not have had. And the label must be *issuer-level*. A company with 47 bonds outstanding is one default, not 47; fitting on bonds teaches the model that defaults are clustered in large capital structures, which is true and useless.

### 11.4.4 What machine learning adds, measured honestly

Alanis, Chava and Shah (2022, *Benchmarking Machine Learning Models to Predict Corporate Bankruptcy*, arXiv:2212.12051) run the cleanest horse race available: 2,585 bankruptcies from 1990 to 2019, walk-forward one-year-ahead prediction, out-of-sample AUC. With distance-to-default and industry only, a LASSO logit scores 0.551 while a random forest scores 0.833 and XGBoost 0.837: trees extract the nonlinearity in DD that a linear logit cannot. Adding accounting variables lifts XGBoost to 0.907, adding market variables to 0.916, and macro variables add nothing (0.915). Excess stock returns, idiosyncratic risk, and relative size are the most important features (Shumway's three, twenty years later), and text features from 10-K filings do not improve performance materially. The lesson is not "use XGBoost." It is that the step from a linear DD score to a nonlinear multi-covariate model is worth about 8 points of AUC, and every further idea has to fight for the next half point.

> **Ways This Blows Up.** *Paired samples:* matching each defaulter to a healthy survivor makes the test easy, because "it is easier to tell the difference between a Aaa and a defaulting firm than between a lower-quality firm and a defaulter" (Bohn–Stein p.226). *Look-ahead on filing dates:* a 10-K for fiscal year 2025 is dated 31 December 2025 in most databases and filed in March 2026; lag every accounting feature to its filing date. *Survivorship via exchanges:* bonds that leave the index through a distressed exchange vanish from a bond-return panel, so a backtest built on index constituents never sees the loss. *Forty-seven bonds per issuer:* one issuer, one observation (Chapter 7). *Regime calibration:* a model calibrated on 2010–2019, a benign decade with few hard defaults, deployed into 2026's soft-default regime, ranks well and is calibrated wrong.

### Specification for AI Implementation

**Schema.** Panel, one row per `issuer_id`–`month` (int, int): `DD` (float, observed with noise), `runway` (weeks, float in $[0, 13]$), `exret` (monthly excess equity return proxy, decimal), `default_12m` (int 0/1: any default event in months $[t, t+12)$), `de_flag` (int 0/1: that event was a distressed exchange). Rows whose 12-month window extends past the sample end are dropped (censored). Features enter lagged by `lag` months within issuer. Cross-validation folds are issuer-disjoint and time-purged with a 12-month embargo (Chapter 7, §7.7).

```python
# Block 3: synthetic HY panel, dynamic logit, clustered SEs, purged issuer-grouped CV (Section 11.4)

def simulate_hy_universe(n_issuers=600, n_months=120, de_share=0.30, seed=RNG_SEED):
    """Issuer-month panel: persistent latent DD with a common factor (default clustering),
    a liquidity-runway covariate capped at 13 weeks, and a distressed-exchange flag."""
    g = np.random.default_rng(seed)
    mu_dd = g.uniform(0.5, 5.5, n_issuers)
    dd = mu_dd + g.normal(0.0, 0.5, n_issuers)
    runway = np.clip(g.normal(9.0, 3.0, n_issuers), 0.0, 13.0)
    alive = np.ones(n_issuers, dtype=bool)
    default_month = np.full(n_issuers, -1)
    DD = np.full((n_months, n_issuers), np.nan)
    RUN = np.full_like(DD, np.nan)
    EXR = np.full_like(DD, np.nan)
    for t in range(n_months):
        dd_new = (mu_dd + 0.92 * (dd - mu_dd) + g.normal(0.0, 0.20)
                  + g.normal(0.0, 0.35, n_issuers))
        exret = 0.08 * (dd_new - dd) + g.normal(0.0, 0.03, n_issuers)
        dd = dd_new
        runway = np.clip(runway + 0.6 * np.tanh(dd - 1.5) + g.normal(0.0, 0.7, n_issuers), 0.0, 13.0)
        DD[t, alive] = dd[alive] + g.normal(0.0, 0.25, alive.sum())
        RUN[t, alive] = runway[alive]
        EXR[t, alive] = exret[alive]
        hazard = special.expit(-3.4 - 1.0 * dd - 0.12 * runway)     # true monthly hazard
        d_now = alive & (g.random(n_issuers) < hazard)
        default_month[d_now] = t
        alive &= ~d_now
    t_idx, i_idx = np.nonzero(~np.isnan(DD))
    panel = pd.DataFrame({"issuer_id": i_idx, "month": t_idx, "DD": DD[t_idx, i_idx],
                          "runway": RUN[t_idx, i_idx], "exret": EXR[t_idx, i_idx]})
    dm = default_month[i_idx]
    panel["default_12m"] = ((dm >= t_idx) & (dm < t_idx + 12)).astype(int)
    is_de = g.random(n_issuers) < de_share
    panel["de_flag"] = ((panel["default_12m"].to_numpy() == 1) & is_de[i_idx]).astype(int)
    panel = panel[panel["month"] <= n_months - 12].reset_index(drop=True)   # censored labels out
    return panel, default_month


def lag_features(panel, cols, lag):
    out = panel.sort_values(["issuer_id", "month"]).copy()
    lagged_cols = [c + "_lag" for c in cols]
    for c, cl in zip(cols, lagged_cols):
        out[cl] = out.groupby("issuer_id")[c].shift(lag)
    return out.dropna(subset=lagged_cols).reset_index(drop=True)


def fit_logit(X, y, groups=None, max_iter=100):
    """Newton-Raphson logit with step halving; issuer-clustered sandwich SEs when groups given."""
    X1 = np.column_stack([np.ones(len(X)), np.asarray(X, dtype=float)])
    y = np.asarray(y, dtype=float)
    ybar = np.clip(y.mean(), 1e-6, 1 - 1e-6)
    b = np.zeros(X1.shape[1])
    b[0] = np.log(ybar / (1 - ybar))

    def nll(beta):
        z = X1 @ beta
        return np.sum(np.logaddexp(0.0, z) - y * z)

    f = nll(b)
    for _ in range(max_iter):
        p = special.expit(X1 @ b)
        H = (X1 * (p * (1 - p))[:, None]).T @ X1
        step = np.linalg.solve(H + 1e-10 * np.eye(len(b)), X1.T @ (y - p))
        t = 1.0
        while nll(b + t * step) > f + 1e-12 and t > 1e-8:
            t *= 0.5
        b = b + t * step
        f = nll(b)
        if np.max(np.abs(t * step)) < 1e-9:
            break
    p = special.expit(X1 @ b)
    Hinv = np.linalg.inv((X1 * (p * (1 - p))[:, None]).T @ X1)
    if groups is None:
        cov = Hinv
    else:
        G = pd.DataFrame(X1 * (y - p)[:, None]).groupby(np.asarray(groups)).sum().to_numpy()
        cov = Hinv @ (G.T @ G) @ Hinv
    return b, np.sqrt(np.diag(cov))


def predict_logit(b, X):
    return special.expit(b[0] + np.asarray(X, dtype=float) @ b[1:])


def prior_shift(p, pi_sample, pi_pop):
    p = np.clip(np.asarray(p, dtype=float), 1e-12, 1 - 1e-12)
    shift = np.log(pi_pop * (1 - pi_sample) / (pi_sample * (1 - pi_pop)))
    return special.expit(special.logit(p) + shift)


def auc(score, default):
    """Mann-Whitney AUC: P(score of a defaulter > score of a survivor); ties count one half."""
    score = np.asarray(score, dtype=float)
    d = np.asarray(default).astype(bool)
    n1, n0 = int(d.sum()), int((~d).sum())
    if n1 == 0 or n0 == 0:
        return np.nan
    ranks = stats.rankdata(score)
    return (ranks[d].sum() - n1 * (n1 + 1) / 2.0) / (n1 * n0)


def purged_group_cv(panel, n_splits=5, embargo=12, seed=RNG_SEED):
    """Issuer-disjoint folds; training rows within `embargo` months of the test block are purged."""
    g = np.random.default_rng(seed)
    issuers = g.permutation(panel["issuer_id"].unique())
    fold_of = np.empty(int(issuers.max()) + 1, dtype=int)
    for k, chunk in enumerate(np.array_split(issuers, n_splits)):
        fold_of[chunk] = k
    f = fold_of[panel["issuer_id"].to_numpy()]
    m = panel["month"].to_numpy()
    for k, block in enumerate(np.array_split(np.sort(panel["month"].unique()), n_splits)):
        lo, hi = block[0], block[-1]
        test = (f == k) & (m >= lo) & (m <= hi)
        train = (f != k) & ((m < lo - embargo) | (m > hi + embargo))
        yield np.flatnonzero(train), np.flatnonzero(test)


FEATURES = ["DD", "runway", "exret"]
XCOLS = [c + "_lag" for c in FEATURES]
panel, default_month = simulate_hy_universe()
lagged = lag_features(panel, FEATURES, lag=3)
X_all, y_all = lagged[XCOLS].to_numpy(), lagged["default_12m"].to_numpy()
assert (default_month >= 0).sum() >= 50                       # enough defaults to say anything

b_full, se_cl = fit_logit(X_all, y_all, groups=lagged["issuer_id"])
_, se_naive = fit_logit(X_all, y_all)
assert b_full[1] < 0 and b_full[2] < 0       # higher DD, longer runway -> lower PD
assert se_cl[1] > se_naive[1]                # overlapping 12m labels: clustering widens SEs

oos = []
for tr, te in purged_group_cv(lagged):
    if y_all[te].sum() == 0:
        print("fold skipped: no defaults in test block")
        continue
    b_cv, _ = fit_logit(X_all[tr], y_all[tr])
    oos.append(auc(predict_logit(b_cv, X_all[te]), y_all[te]))
oos_auc = float(np.mean(oos))
assert len(oos) >= 3 and oos_auc > 0.75

# Look-ahead warning: a feature that peeks at the label looks like genius.
g_leak = np.random.default_rng(RNG_SEED + 1)
X_leak = np.column_stack([X_all, y_all + g_leak.normal(0.0, 0.3, len(y_all))])
b_leak, _ = fit_logit(X_leak, y_all)
auc_leak = auc(predict_logit(b_leak, X_leak), y_all)
assert auc_leak > 0.97

# Label contamination: treating distressed exchanges as survival understates PD.
y_hard = ((y_all == 1) & (lagged["de_flag"].to_numpy() == 0)).astype(int)
b_hard, _ = fit_logit(X_all, y_hard)
assert predict_logit(b_hard, X_all).mean() < 0.9 * y_all.mean()

assert abs(float(prior_shift(0.5, 0.5, 0.03)) - 0.03) < 1e-12
print(f"defaults={(default_month >= 0).sum()} beta_DD={b_full[1]:.3f} "
      f"SE ratio clustered/naive={se_cl[1] / se_naive[1]:.2f} OOS AUC={oos_auc:.3f} "
      f"leaky AUC={auc_leak:.3f} (WARNING: look-ahead)")
```

**Edge cases for ROBO.** A cross-validation fold with no defaults in its test block has an undefined AUC: skip it and log it, never score it as 0.5. Aggregate bonds to the issuer before fitting. Lag accounting features to the filing date, not the period end. Keep the distressed-exchange flag as a separate column so the label definition can be audited and changed without rebuilding the panel.

## 11.5 Validation: Power Curves and What "77% Within 24 Months" Means

Every systematic HY pitch book contains a sentence like BlackRock's. The sentence is true, and it is also a single point on a curve whose other coordinate is not printed. Ines reads such sentences the way she reads a player who says he won 77% of his showdowns. "Great. How many hands did you fold to get there?"

> **[SOURCE EXTRACTION]** *BlackRock_Systematic_High_Yield_Credit p.6:* "Our proprietary probability of default signal that has underpinned all of our credit strategies for over 20 years has successfully identified 77% of the defaulted bonds in the ICE BofA High Yield Index within 24 months of its default since 2010."
>
> **Annotation.** The footnote dates the statistic (BlackRock and ICE BofA data, as of 31 March 2024, since January 2010), and the same page tells you the model's horizon is a forward 12-month PD built from accounting, equity and bond market data, ratings, and macro variables. Three things are not on the page, and a diligent allocator asks for all three. First, the exclusion rate: what fraction of the index was flagged to catch the 77%? Second, the unit: "defaulted bonds" is a bond count, and a capital structure with 47 bonds counts 47 times. Third, the horizon mismatch: a 12-month PD scored against a 24-month window gets two years to be right. None of this makes the claim weak; a modern PD with an accuracy ratio around 0.7 would produce numbers like this honestly. It makes the claim *incomplete*, and the rest of this section shows how to complete it.

### 11.5.1 CAP, ROC, and an identity worth knowing

Sort issuers from riskiest to safest by model score. The cumulative accuracy profile (CAP) plots, for each cutoff, the fraction of *all* issuers flagged ($x$) against the fraction of *defaulters* flagged ($Y(x)$). The ROC curve plots the same defaulter fraction against the fraction of *survivors* flagged ($x'$). With $d$ defaulters among $n$ issuers and base rate $f = d/n$, the accuracy ratio is the area between the model's CAP and the diagonal, divided by the same area for a perfect model:

$$
\text{AR} = \frac{\int_0^1 Y(x)\,dx - \tfrac12}{\tfrac12(1-f)} = \frac{2\int_0^1 Y(x)\,dx - 1}{1-f} .
$$

The area under the ROC is a probability (Bohn–Stein p.410, below): $\text{AUC} = \mathbb{P}(\text{score}_D > \text{score}_{ND})$, the Mann–Whitney statistic. The two measures are not merely related; they are the same number in two units. Every step down the sorted list moves $x$ by $1/n$, and $1/n$ splits exactly as $dx = f\,dY + (1-f)\,dx'$, because a defaulter step has $dY = 1/d$ and a survivor step has $dx' = 1/(n-d)$. Integrating $Y$ against both pieces, $\int Y\,dY = \tfrac12$ and $\int Y\,dx' = \text{AUC}$, so

$$
\int_0^1 Y(x)\,dx = \tfrac{f}{2} + (1-f)\,\text{AUC} \quad\Longrightarrow\quad \text{AR} = 2\,\text{AUC} - 1
$$

exactly, for scores without ties (Engelmann, Hayden and Tasche showed this in 2003). Report either; never compare an AR from one universe with an AR from another universe with a different base rate as if the difference were skill (Bohn–Stein p.426).

> **[SOURCE EXTRACTION]** *Bohn_Stein_Active_Credit_Portfolio_Management p.410:* "The quantity A, the area under the ROC, is equivalent to the probability that a randomly chosen defaulting loan will be ranked worse than a randomly chosen nondefaulting loan by a specific model"
>
> **Annotation.** This is the most useful sentence in model validation, because it converts an abstract area into a bet anyone at the desk can price. Pick one defaulter and one survivor at random; AUC is the chance your model ranks them correctly. Alanis, Chava and Shah's 0.916 means the model gets that coin flip right eleven times in twelve. Two cautions. "Randomly chosen" must mean randomly chosen *issuers*, or the 47-bond capital structure turns one correct ranking into 47. And AUC is a ranking statistic, blind to calibration: a model that ranks perfectly and says every PD is 50% scores 1.0 and would destroy you in the credit triangle. Validate power with AUC, calibration with realized-versus-predicted default rates by PD bucket, and do both on issuer-disjoint, time-purged folds.

### 11.5.2 From a hit rate to a return

Let the model exclude a fraction $q$ of the index (set $X$) and keep the rest ($K$, weight $1-q$), and let the defensive portfolio hold $K$ scaled to full weight. Its active return against the index is $r_K - [q\,r_X + (1-q)\,r_K] = q\,(r_K - r_X)$. Apply the credit triangle to each set, $\mathbb{E}^{\mathbb{P}}[r] \approx s - \pi L$ with $\pi$ the set's default rate:

$$
\mathbb{E}^{\mathbb{P}}[r_{\text{active}}] \approx q\Big[(\pi_X - \pi_K)\,L - (s_X - s_K)\Big].
$$

Default avoidance pays if and only if the excluded set's *excess default loss* exceeds its *excess spread*. Now plug in the BlackRock-style claim on a universe with a 3% default rate. If the 77% hit rate came from excluding $q = 20\%$, the flagged set defaults at $\pi_X = 0.77 \times 3\%/0.20 = 11.6\%$ and the kept set at $\pi_K = 0.23 \times 3\%/0.80 = 0.86\%$. With $L = 0.6$ and an excess spread of 420bp in the excluded set, the active return is $0.2 \times (6.41\% - 4.20\%) \approx +44$bp a year. If the same 77% required $q = 40\%$, then $\pi_X = 5.8\%$, $\pi_K = 1.15\%$, and against a 300bp excess spread the active return is $0.4 \times (2.78\% - 3.00\%) \approx -9$bp *(all inputs illustrative)*. Same hit rate, opposite sign. And the base-rate trap is visible in the first case: even the good model flags 17.7% of the index that does not default, which is 18% of all survivors, whose carry you have handed to someone else.

"A model that flags everyone catches 100% of defaults," Ines said. "That is not defense. That is leaving the casino."

> **Trend Watch: The Soft-Default Regime, 2024–2026.** *What changed:* the definition of default drifted from "missed a coupon" toward "agreed to be paid less," and the default rate split by market. *When and how big:* S&P reported the US trailing-12-month speculative-grade default rate at 5.1% in December 2024 and put distressed exchanges at about 68% of 2025 defaults through April, the highest year-to-date share since 2008 *(approx.; S&P reports via search summaries, primary pages not accessed)*. Moody's counted distressed exchanges as 65% of all corporate defaults in 2025 and put the average forward one-year PD for US high yield companies at 3.2% in Q1 2026 (Moody's Analytics, 18 May 2026). Fitch forecast 2026 default rates of 2.5–3.0% for US high yield and 4.5–5.0% for US leveraged loans (Investment Executive, 3 December 2025), and its US private credit default rate hit a record 6% in April 2026 (The DESK, 27 May 2026). UBS put the 2025 USD HY default expectation at 4.8%, but 3.1% excluding two large distressed capital structures (UBS AM, 17 January 2025). *What it means for the desk:* a par-weighted default rate is driven by a handful of large names, so breadth beats tier; private credit is now the leading indicator for the public CCC tier; and any PD model trained on hard defaults alone is calibrated to a world in which two-thirds of today's defaults would have counted as survival.

### Specification for AI Implementation

**Schema.** `score`: float array, higher means riskier (a PD). `default`: int 0/1 array, issuer-level, aligned. `q`: exclusion fraction in $(0,1)$. Outputs: CAP points, AUC, AR, hit rate $\text{HR}(q) = Y(q)$, and the active-return decomposition.

```python
# Block 4: CAP curve, accuracy ratio, hit rate, exclusion economics (Section 11.5)

def cap_curve(score, default):
    order = np.argsort(-np.asarray(score, dtype=float), kind="mergesort")
    d = np.asarray(default, dtype=float)[order]
    if d.sum() == 0:
        raise ValueError("no defaults: CAP undefined")
    x = np.concatenate([[0.0], np.arange(1, d.size + 1) / d.size])
    y = np.concatenate([[0.0], np.cumsum(d) / d.sum()])
    return x, y


def accuracy_ratio(score, default):
    x, y = cap_curve(score, default)
    area = np.sum(np.diff(x) * (y[1:] + y[:-1]) / 2.0)        # trapezoid rule
    f = float(np.mean(default))
    return (2.0 * area - 1.0) / (1.0 - f)


def hit_rate(score, default, q):
    x, y = cap_curve(score, default)
    return float(np.interp(q, x, y))


def exclusion_active_return(q, pi_X, pi_K, s_X, s_K, L):
    """q * [(pi_X - pi_K) * L - (s_X - s_K)], all decimals per year, P-measure."""
    return q * ((pi_X - pi_K) * L - (s_X - s_K))


# Sanity 1: AR = 2*AUC - 1 exactly for untied scores.
g4 = np.random.default_rng(RNG_SEED + 4)
dflt = (g4.random(5000) < 0.05).astype(int)
sc = g4.normal(0.0, 1.0, 5000) + 1.2 * dflt
assert abs(accuracy_ratio(sc, dflt) - (2 * auc(sc, dflt) - 1)) < 1e-10

# Sanity 2: a perfect ranking scores AR = 1; random scores average AR ~ 0 over 20 seeds.
assert abs(accuracy_ratio(dflt + 0.5 * g4.random(5000), dflt) - 1.0) < 1e-9
ar_rand = []
for s in range(20):
    gs = np.random.default_rng(1000 + s)
    ar_rand.append(accuracy_ratio(gs.random(5000), (gs.random(5000) < 0.05).astype(int)))
assert abs(np.mean(ar_rand)) < 0.05

# Sanity 3: the worked example of Section 11.5.2.
act_20 = exclusion_active_return(0.20, 0.77 * 0.03 / 0.20, 0.23 * 0.03 / 0.80, 0.0420, 0.0, 0.6)
act_40 = exclusion_active_return(0.40, 0.77 * 0.03 / 0.40, 0.23 * 0.03 / 0.60, 0.0300, 0.0, 0.6)
assert act_20 > 0 > act_40

# Apply to the Block 3 panel: in-sample PDs from the full model, one row per issuer-month.
pd_in = predict_logit(b_full, X_all)
print(f"panel AR={accuracy_ratio(pd_in, y_all):.3f} AUC={auc(pd_in, y_all):.3f} "
      f"HR(10/20/30%)={[round(hit_rate(pd_in, y_all, q), 2) for q in (0.1, 0.2, 0.3)]} "
      f"active 20%={act_20:.4%} active 40%={act_40:.4%}")
```

**Edge cases for ROBO.** Tied scores (a capped PD, or a rating-based score with 20 notches) make the CAP depend on sort order; break ties by averaging, or report the AUC, which the rank formula already tie-corrects. Score at the issuer level. State the horizon of the score and the horizon of the hit window in the output, and refuse to compare them when they differ.

## 11.6 The CCC Problem

"CCC is where the defaults live and where the rallies live," Mags said, "which is the same sentence." She meant that the tier's return is a bet on which of its members survive, and that both the 2000 disaster and the 2003 rally were the same population answering the same question differently.

The tier is also the index's risk budget. Wellington put CCC-rated bonds at 13% of the high yield index in a note dated 30 September 2026, and Loomis Sayles found that at year-end 2024 CCCs accounted for nearly 25% of the index's OAS. A tier that is an eighth of the market value and a quarter of the spread is where most of the index's credit risk is concentrated, and where any defensive strategy will place most of its bets, whether it means to or not.

### 11.6.1 Why tier exclusion is the wrong tool

Three facts from the historical tables, each a reason not to treat CCC as one asset. The S&P one-year transition matrix for 1980–2002 (Schmid p.28) puts the CCC-to-default rate at 31.58% and the probability of *staying* CCC at 55.82%: the tier is sticky, so a CCC bond is usually still a CCC bond a year later, collecting a coupon. CSFB's default rates by rating *at issuance* for 1993–2003 (Moyer p.44) show B at 4.23% and CCC at 4.28%, almost identical, which Moyer flags with mild surprise: the rating at issuance separates CCC from B much less than the rating after a downgrade does, because a newly issued CCC has fresh money and a fallen CCC has a problem. And recoveries are cyclical (Schmid p.103), so the same CCC default costs more in a recession, exactly when the tier's spread is widest.

The structure of the right tool follows from Bolder.

> **[SOURCE EXTRACTION]** *Bolder_Credit_Risk_Modelling p.324:* "if a credit counterparty has a large default probability, then much of its inherent default risk is idiosyncratic and, as such, it is less highly correlated with other credit counterparties. Conversely, very low risk counterparties predominately face systematic risk"
>
> **Annotation.** Bolder is explaining why the Basel IRB asset correlation falls as PD rises, from 0.24 for the safest obligors toward 0.12 for the riskiest. The insight for a CCC book is that high-PD risk diversifies. A CCC company defaults mostly because of *its own* problems (a maturity wall, a lost contract, a sponsor that stopped writing checks), and those problems are largely uncorrelated with the next CCC company's. That is the formal case for breadth: 150 CCC issuers at 0.1% each are a far safer bucket than 15 at 1% each, even with the same average PD, because the idiosyncratic part of the default variance shrinks as $1/n$. It is also why the BB tier is the place to fear the cycle: its rare defaults arrive together. A systematic desk takes the opposite of the instinctive position: concentrated and careful in BB, broad and quantitative in CCC.

Sizing by expected loss rather than by fear then becomes a one-line rule. Set an annual expected-loss budget $\text{EL}^{\max}$ for the portfolio (for example 1.0%, illustrative). Fill the CCC bucket in descending order of default-adjusted carry per unit of risk, $(s_i - \hat\lambda_i L_i)/\text{DTS}_i$, subject to

$$
\sum_{i \in \text{CCC}} w_i\,\hat\lambda_i\,L_i \;\le\; \text{EL}^{\max} - \sum_{i \notin \text{CCC}} w_i\,\hat\lambda_i\,L_i, \qquad w_i \le w^{\max}_{\text{issuer}} .
$$

The bucket's size is an *output*: large when the model finds CCC names whose spread overpays their PD, small when the tier's spread is all default. There is no 5% CCC limit in this rule, which will alarm the risk committee. Show them the issuer cap.

One flow fact belongs next to the model. Most CLOs face a limit of roughly 7.5% on CCC assets, above which the excess is carried at the lower of market value and par in the overcollateralization tests (Chapter 21). A wave of downgrades into CCC therefore produces forced sellers who care about rating, not PD. When your model says "avoid" and the seller is a CLO manager defending an OC test, check whether the model is seeing distress or seeing the flow. Ines put it more simply: "When someone *has* to fold, buy their chips."

> **Docket Diary. After the soft default, 1979–2026.** Moody's Analytics studied 1,173 borrowers that went through a distressed exchange or similar soft credit event between 1979 and 2026 (Moody's Analytics, David Hamilton, *Lend, extend, and then…*, 18 May 2026). Roughly two-thirds avoided a hard default or a repeat event within a decade; about one in four ended in a hard default; and more than 70% of eventual hard defaults following a distressed restructuring occurred within the first two years. The same note puts Moody's private credit default proxy at 1.6% excluding distressed exchanges and 4.7% including them. *For the model:* an LME is not the end of the story; it resets the hazard clock to a higher level for about 24 months, and "months since last LME" belongs in the feature set. *The Ad Hoc Group, represented by counsel:* "The transaction was value-maximizing for all stakeholders who were invited."

### 11.6.2 Case Study: The 2026 CCC Decompression

On 15 October 2026 the ICE BofA US High Yield OAS closed at 323bp, BB at 197bp, single-B at 326bp, and CCC & lower at 1,278bp, one day after a three-year high of 1,282bp (FRED series BAMLH0A0HYM2, BAMLH0A1HYBB, BAMLH0A2HYB, BAMLH0A3HYC). The ratio of CCC OAS to index OAS, using month-end values, went from 2.61 in January 2025 to 2.54 in April 2025 (the tariff shock widened everything, so the ratio briefly *compressed*), then 3.15 in December 2025, 3.53 in June 2026, and 3.96 in August and October 2026 *(our computation from FRED)*. The index is calm because it is mostly double-B and short: State Street's global high yield universe was 62% BB-rated with a 3.1-year duration at year-end 2025, and Nuveen puts the BB share of the US index at 51% at year-end 2024, against 37% in 2004 (Nuveen p.4). The tier is not calm.

The backdrop is a private credit default rate at a Fitch record of 6% in April 2026, distressed exchanges at 94% of downgrades to default or selective default in the twelve months to February 2026 by a rating-agency count reported in The DESK (27 May 2026), and Morgan Stanley forecasting high yield defaults of 3.5%. Any story about *why* the tier decompressed (software issuers facing AI disruption, private-credit stress spilling into public CCC capital structures) is interpretation, and we label it so.

How three desks would have traded it *(illustrative)*. The tier excluder sold its CCCs in 2025 and looks brilliant in October 2026; its exposure to a 2003-style rebound is zero, and if the rebound comes, it will look exactly as brilliant as Mags's friends who sat out 2003. The beta-tilter held 90% of everything, including the 10% of CCC names that will default, and earned 90% of a bad year. The PD-ranked selector excluded the CCC names whose model PD exceeded their spread-implied break-even (§11.1.2), kept the CCCs whose spread overpaid their PD (often the sticky, newly issued, sponsor-supported ones), sized the bucket by expected loss, and used the 2026 widening to *add* to survivors as their spreads crossed the break-even line. Only the third desk has a plan for the rebound.

## 11.7 Quality and Low-Risk Tilts

Kaz had a theory, delivered with the serenity of someone who has never read a credit agreement. "The low-volatility anomaly is just leverage aversion. Investors who can't borrow buy risky assets to get return, so risky assets are overpriced and safe ones are cheap. Frazzini and Pedersen. Done."

"In equities," Theo said. "In high yield the risky assets also have a lawyer."

Both are right. Frazzini and Pedersen (2014) find alphas declining in beta across equities, Treasuries, credit, and futures; Houweling and van Zundert (2017) define the credit low-risk factor as short maturity and high rating and find significant alpha. Kaz's story explains why the effect exists everywhere. Theo's explains why it is *stronger* in high yield: the riskiest bonds carry jump risk that their spreads systematically underprice relative to their volatility, which is the asymmetry of §11.1 showing up in the cross-section.

> **[SOURCE EXTRACTION]** *Dynkin_Systematic_Investing_in_Credit p.59:* "two in particular are responsible for the majority of credit return outperformance over the replicating portfolio: equity and bond volatility risk premia (VRP) and the low risk anomaly."
>
> **Annotation.** Dynkin and coauthors decompose credit returns against a replicating portfolio of equities and Treasuries and ask what is left that only credit pays. Two things: selling volatility, and the low-risk anomaly. Read that as a job description for defensive HY. The VRP part is the short put you cannot avoid owning; the low-risk part is the one premium you can harvest *by being defensive*, which is why a well-built defensive book need not be a lower-return book. Dynkin p.95 adds the maturity version ("Short-maturity bonds had better risk-adjusted and even non-risk-adjusted performance than long-maturity bonds"). The 2026 caveat: the HY index is now majority BB and short, so the low-risk trade is crowded at exactly the front end where it lives. Measure your low-risk exposure relative to the index, not in absolute terms.

### 11.7.1 Why low risk wins, in one line of DTS

Ben Dor's DTS framework rests on a Merton result: spread volatility is nearly proportional to spread (Ben Dor p.104), $\sigma(\Delta s_i) \approx k\,s_i$. A bond's excess-return volatility is then $D^{\text{spr}}_i\,k\,s_i = k\,\text{DTS}_i$. Divide the credit triangle by it:

$$
\frac{\mathbb{E}^{\mathbb{P}}[r^{xs}_i]}{\sigma(r^{xs}_i)} \approx \frac{s_i - \lambda_i L_i}{k\,D^{\text{spr}}_i\,s_i} = \frac{1}{k\,D^{\text{spr}}_i}\left(1 - \frac{\lambda_i L_i}{s_i}\right).
$$

Two predictions drop out. Risk-adjusted return falls with spread duration, even though the spread curve slopes upward: Dynkin's finding that information ratios decline with maturity (Dynkin p.454–457). And it falls as the share of the spread that is expected loss, $\lambda_i L_i/s_i$, rises. On the 1980–2002 default table at October 2026 spreads with $L = 0.6$, that share is 0.47 for BB, 1.28 for B, and 1.48 for CCC *(our computation; the historical table is pessimistic, as §11.1.2 showed)*: rising down the rating scale under any default table you choose. Low risk is not an anomaly in this framing; it is the credit triangle divided by DTS.

### 11.7.2 The long-only contradiction, and three ways out

The textbook betting-against-beta portfolio in credit levers the low-risk leg and delevers the high-risk leg to equal DTS:

$$
r^{\text{BAB}}_t = \frac{\text{DTS}_{\text{mkt}}}{\text{DTS}_L}\,r^{xs}_{L,t} - \frac{\text{DTS}_{\text{mkt}}}{\text{DTS}_H}\,r^{xs}_{H,t} .
$$

A long-only HY fund cannot short and is usually forbidden to lever. Tilt it toward short, high-rated bonds on a market-value basis and its DTS falls below the benchmark's, which means its beta falls, which means you have rebuilt the dimmer switch and called it a factor. "IDO or it didn't happen," Ines said, looking at a market-value-neutral backtest with a beta of 0.85 and a beautiful Sharpe ratio. Run DTS-neutral, the alpha halved. "And half of it didn't."

There are three honest exits. Overlay: hold the low-risk book and buy back the missing DTS with CDX HY or a total-return swap on the index (Chapter 8), so the active book is pure selection. Re-spend: keep the DTS budget equal to the benchmark's but spend it on the spread of *low-PD* issuers, in longer maturities of good BB and B credits, which gives up some of the maturity effect to avoid the default tail. Or accept the beta and say so in the factsheet. Paleologo's warning applies to all three: "If we make a mistake of 5% in the expected return forecast on a low-volatility stock, we pay a much higher cost than if we make the same mistake on the high-volatility one" (Paleologo p.99), because risk-based sizing puts the most weight where a forecast error costs the most. Cap issuer weights.

Equity momentum belongs here too, because it is a default-avoidance signal in disguise. Dynkin reports a top-minus-bottom quintile return of 15.9% a year with an information ratio of 1.74 for equity momentum in HY credit over January 1993 to May 2017, and calls it "a highly informative signal for lower quality names" (Dynkin p.609).

> **[SOURCE EXTRACTION]** *Dynkin_Systematic_Investing_in_Credit p.739:* "top‐EMC portfolios tend to have lower credit exposures than their bottom counterparts during volatile episodes when safer, low‐OAS issuers tend to have less negative equity momentum."
>
> **Annotation.** This is the trap inside the good signal. Equity momentum in credit (EMC) works in drawdowns partly because, in a selloff, the stocks that fall least belong to the safest issuers, so a top-EMC portfolio quietly becomes a low-beta portfolio exactly when beta is being punished. Some of its "alpha" in 2008 or March 2020 is the dimmer switch again. Dynkin's remedy is to match the long and short legs on DTS so that the signal is measured net of its credit exposure, and the same page reports that EMC and its companion signal still work in drawdowns once matched. For a defensive HY book the lesson is procedural: every defensive signal must be tested DTS-neutral before it is credited with skill, or you will pay active fees for a beta you could have bought for two basis points.

### Specification for AI Implementation

**The Spec You Hand the Robot.** "Exclude the worst PD quintile, tilt toward default-adjusted carry per unit of DTS, hold $w^\top\text{DTS}$ within 1% of the benchmark, long-only, fully invested, issuer cap 3%." **Schema.** One cross-section: `pd_hat` (12m PD, decimal), `spread` (OAS, decimal), `dur` ($D^{\text{spr}}$, years), `bench_w` (sums to 1). Defaulted issuers enter with DTS set to zero and are excluded before optimization. Output: weights `w` (same order), `keep` mask, solver result.

```python
# Block 5: DTS-neutral defensive portfolio (Section 11.7)

def defensive_portfolio(pd_hat, spread, dur, bench_w, L=0.6, exclude_q=0.20,
                        issuer_cap=0.03, tilt=1.0):
    pd_hat, spread, dur, bench_w = (np.asarray(a, dtype=float) for a in (pd_hat, spread, dur, bench_w))
    dts = dur * spread
    dts_bench = float(bench_w @ dts)
    keep = pd_hat <= np.quantile(pd_hat, 1.0 - exclude_q)
    score = (spread - pd_hat * L) / dts                       # default-adjusted carry per unit DTS
    zk = (score[keep] - score[keep].mean()) / score[keep].std()
    w0 = bench_w[keep] * np.exp(tilt * np.clip(zk, -2.0, 2.0))
    w0 = w0 / w0.sum()
    dk = dts[keep]
    if not (dk.min() <= dts_bench <= dk.max()):
        raise ValueError("benchmark DTS unreachable long-only: refuse rather than lever")
    cons = [{"type": "eq", "fun": lambda w: w.sum() - 1.0, "jac": lambda w: np.ones_like(w)},
            {"type": "eq", "fun": lambda w: w @ dk / dts_bench - 1.0, "jac": lambda w: dk / dts_bench}]
    res = optimize.minimize(lambda w: 5e3 * np.sum((w - w0) ** 2), w0,
                            jac=lambda w: 1e4 * (w - w0), method="SLSQP",
                            bounds=[(0.0, issuer_cap)] * int(keep.sum()), constraints=cons,
                            options={"maxiter": 500, "ftol": 1e-14})
    w = np.zeros_like(bench_w)
    w[keep] = res.x
    return w, keep, w0, dts, dts_bench


g5 = np.random.default_rng(RNG_SEED + 5)
n_iss = int(lagged["issuer_id"].max()) + 1
dur_by_issuer = g5.uniform(1.5, 6.5, n_iss)
size_by_issuer = g5.lognormal(0.0, 0.5, n_iss)
held_def, bench_def = 0.0, 0.0
for t0 in (24, 36, 48, 60, 72):
    cs = lagged[lagged["month"] == t0]
    iid = cs["issuer_id"].to_numpy()
    pd_t = predict_logit(b_full, cs[XCOLS].to_numpy())
    spr_t = 0.015 + 0.35 * empirical_pd(cs["DD"].to_numpy()) * np.exp(g5.normal(0.0, 0.2, len(cs)))
    bw = size_by_issuer[iid] / size_by_issuer[iid].sum()
    w, keep, w0, dts_t, dts_b = defensive_portfolio(pd_t, spr_t, dur_by_issuer[iid], bw)
    assert abs(w @ dts_t / dts_b - 1.0) < 0.01            # DTS-neutral within 1%
    assert abs(w.sum() - 1.0) < 1e-6 and w.min() > -1e-9 and np.all(w[~keep] == 0.0)
    assert (w0 @ dts_t[keep]) / dts_b < 0.95                # market-value tilt = dimmer switch
    y_t = cs["default_12m"].to_numpy()
    held_def += w @ y_t
    bench_def += bw @ y_t
assert held_def < bench_def                                  # fewer realized defaults held
print(f"avg 12m default exposure: held={held_def / 5:.3%} bench={bench_def / 5:.3%}; "
      f"last MV-tilt DTS ratio={(w0 @ dts_t[keep]) / dts_b:.2f}")
```

**Edge cases for ROBO.** If the benchmark DTS cannot be reached long-only within issuer caps, raise; never "solve" it with negative weights or leverage. Recompute DTS after every spread update; a bond that has defaulted carries zero DTS, or a 5,000bp spread will dominate the neutrality constraint. Turnover: penalize changes from yesterday's weights, not from the benchmark, in production.

## 11.8 Defense Without Sacrificing Offense: Regime-Aware Exposure

BlackRock's paper says the quiet part plainly: "it is not always prudent to be looking for safety, irrespective of the macro-economic environment" (BlackRock p.6). Blackstone's systematic credit book describes contrarian rebalancing when spreads widen without fundamental deterioration (Blackstone p.1). Both are describing the second source of convexity from §11.2.2: adding risk when the market overpays for it.

The signal is the gap between the spread the market charges and the spread the PD justifies. Let $\hat s_i = s_0 + m\,\widehat{\text{PD}}_i\,L_i$ be a model spread (expected loss times a risk-premium multiple $m$, plus a liquidity floor $s_0$), and define the residual and its DTS-weighted aggregate

$$
z_i = \ln\frac{s_i}{\hat s_i}, \qquad \bar z_t = \frac{\sum_i w_i\,\text{DTS}_i\,z_i}{\sum_i w_i\,\text{DTS}_i} .
$$

The portfolio's DTS target scales with the residual relative to its own history, bounded:

$$
\text{DTS}^{\text{target}}_t = \text{DTS}^{\text{bench}}_t \cdot \operatorname{clip}\!\big(1 + \kappa(\bar z_t - \bar z^{\text{ref}}),\; 0.9,\; 1.2\big), \qquad \text{DTS}^{\text{target}}_t \le \text{DTS}^{\max}_t ,
$$

where $\text{DTS}^{\max}_t$ is the largest DTS a long-only, capped portfolio can hold: the no-leverage guard. If spreads and PDs widen together, $z_i$ is unchanged and the budget stays at one. If spreads gap while PDs sit still, $\bar z$ jumps and the budget rises.

> **[SOURCE EXTRACTION]** *Dynkin_Systematic_Investing_in_Credit p.384:* "we set our downgrade scalar to 2 (and upgrade scalar to 0.5) and adjust probabilities of unchanged ratings (along the diagonal) such that each row sums to 100%."
>
> **Annotation.** Dynkin conditions the rating transition matrix on the spread environment: in a wide-spread regime downgrades are scaled up and upgrades down, and the diagonal absorbs the difference so each row remains a probability distribution. That is the honest version of "spreads are wide, so buy": wide spreads *do* forecast more downgrades, and a model that ignores that will overbuy. The z-signal above should therefore be computed with spread-conditioned PDs, not PDs frozen at their calm-market values. The residual that survives the conditioning is the overpayment worth buying.

### 11.8.1 Case Study: The April 2025 Tariff Shock, a Ten-Week V

The ICE BofA US High Yield OAS went from 259bp on 22 January 2025 to 461bp on 7 April 2025; the CCC tier went from 690bp to 1,137bp over the same window (FRED). The total return index fell 3.83% from 28 February to 7 April and regained its prior peak on 12 May 2025 *(our computation from FRED BAMLHYH0A0HYM2TRIV)*. Calendar 2025 finished at +8.50%, and State Street put the trailing global high yield default rate at 1.6% at year-end.

Read through the z-signal *(illustrative; the PD stability is our inference, since no vendor's aggregate PD series is sourced here)*: index spreads rose 78% in ten weeks while balance-sheet PDs, which move with quarterly filings and equity-implied leverage, moved far less, so $\bar z$ jumped by roughly $\ln(461/259) \approx 0.58$ and a budget with $\kappa = 0.5$ hit its 1.2 cap. The price-based de-risker sold on 7 April and bought back in May above where it sold. The PD-based desk added DTS into the low. Ines replayed the hand through markouts: "Same cards, same flop. One player folded because the pot got big. The other called because the odds got good."

> **Ways This Blows Up.** *Cheap because it is about to be primed.* A bond whose spread exceeds its PD-implied spread may be pricing something the PD cannot see: a drop-down basket, an uptier-permissive amendment provision, a sponsor that has hired restructuring counsel. The z-signal flags it as overcompensated; the credit agreement flags it as next. Gate every z-driven purchase on the Priming Risk Score of Chapter 13, and treat a high PRS with a high z as a short, not a long.

## 11.9 Capacity of Systematic HY

"If this works," Theo asked, "why isn't it a trillion dollars?" Blackstone's answer is that systematic strategies run about 20% of global equities but less than 2% of the fixed income universe (Blackstone p.2). Part of the gap is data and history; part is capacity, which is a cost curve.

Let $\alpha_0$ be gross annual alpha, $\text{TO}$ annual turnover, $V_{\text{ADV}}$ the relevant average daily volume, $H$ the days over which the strategy trades, and $\kappa$ a square-root impact coefficient. Net alpha at capital $C$ and the capacity $C^\ast$ at which it falls to a hurdle $\alpha_{\min}$ are

$$
\alpha_{\text{net}}(C) = \alpha_0 - \kappa\,\text{TO}\sqrt{\frac{C}{V_{\text{ADV}}\,H}}, \qquad C^\ast = V_{\text{ADV}}\,H\left(\frac{\alpha_0 - \alpha_{\min}}{\kappa\,\text{TO}}\right)^{2}.
$$

The square means capacity is brutally sensitive to turnover: halve $\text{TO}$ and capacity quadruples. That ranks the defensive toolkit. Default avoidance is an *exclusion* rule with low turnover, so it scales. The low-risk tilt sits in the most liquid part of HY, so it scales. CCC reversal and fallen-angel buying need high turnover in the least liquid bonds at the worst moments, so they do not. Liquidity is also state-dependent: Ben Dor finds that liquidity costs show up in HY spreads mainly in stress (p.177), which is when the defensive signal fires.

> **[SOURCE EXTRACTION]** *Dynkin_Systematic_Investing_in_Credit p.209:* "the Sharpe ratio decreases to 0.95 (from 1.14) for a portfolio size of \$2bn, well above that of the High Yield Index (0.65)."
>
> **Annotation.** This is a rare published capacity curve for a HY niche: Dynkin's fallen-angel strategy, net of transaction costs, losing about a sixth of its Sharpe ratio as it grows to \$2bn, and still beating the index. Two readings. The optimistic one: niche HY strategies are not as capacity-constrained as folklore says, because the forced sellers are large. The realistic one: \$2bn is a single sleeve at a large manager, so the fallen-angel and CCC-reversal components of a defensive book should be sized as satellites around a core that scales: exclusion plus DTS-neutral low risk. The trading-cost inputs have also improved since that study, which the Trend Watch below quantifies.

> **Trend Watch: Electronic HY and the Systematic Share, 2019–2026.** *What changed:* HY execution became electronic enough that a systematic book can trade hundreds of line items without a phone. *How big:* Man Numeric moved from roughly 30% of its HY and 60% of its IG order flow on electronic venues to over 90% of all order flow by May 2023 (Man 2023 p.3). Total US corporate bond ADV reached \$66.7bn through September 2026, up 13.4% year on year, with \$12.1tn outstanding at 2Q26 (SIFMA, US Corporate Bonds Statistics, page dated 14 October 2026). Sizes in the wild: Blackstone's systematic credit platform manages more than \$40bn across IG, HY and EM (Blackstone p.1–2); the iShares High Yield Systematic Bond ETF (HYDB), launched July 2017 and selected and weighted by default probability, default-adjusted spread, and volatility, held \$1.52bn at a 0.35% expense ratio (stockanalysis.com, checked 17 October 2026). *What it means:* the cost coefficient $\kappa$ fell, so capacity rose with its square; but systematic HY is still a small share of a large market, which is good news for capacity and a warning about how short the live track records are. Portfolio trading's role in this shift is Chapter 19's story.

### Specification for AI Implementation

**Schema.** Cross-section arrays `spread`, `s_hat`, `dts`, `w` (decimals; weights sum to 1); scalars `z_ref`, `kappa`, band `(lo, hi)`, `dts_max_ratio` (largest achievable long-only DTS over benchmark DTS). Capacity inputs in decimals per year and dollars; `adv` is \$ per day.

```python
# Block 6: regime-aware DTS budget and capacity (Sections 11.8-11.9)

def model_spread(pd_hat, L=0.6, m=1.8, s0=0.005):
    return s0 + m * np.asarray(pd_hat, dtype=float) * L


def dts_multiplier(spread, s_hat, dts, w, z_ref, kappa=0.5, band=(0.9, 1.2), dts_max_ratio=np.inf):
    z = np.log(np.asarray(spread, dtype=float) / np.asarray(s_hat, dtype=float))
    z_bar = float(np.sum(w * dts * z) / np.sum(w * dts))
    mult = float(np.clip(1.0 + kappa * (z_bar - z_ref), band[0], band[1]))
    return min(mult, dts_max_ratio), z_bar                      # no-leverage guard


def alpha_net(C, alpha0, adv, horizon_days, kappa, turnover):
    return alpha0 - kappa * turnover * np.sqrt(C / (adv * horizon_days))


def capacity_closed_form(alpha0, alpha_min, adv, horizon_days, kappa, turnover):
    return adv * horizon_days * ((alpha0 - alpha_min) / (kappa * turnover)) ** 2


def capacity_numeric(alpha0, alpha_min, adv, horizon_days, kappa, turnover):
    f = lambda C: alpha_net(C, alpha0, adv, horizon_days, kappa, turnover) - alpha_min
    hi = adv * horizon_days
    while f(hi) > 0:
        hi *= 4.0
    return optimize.brentq(f, 0.0, hi, xtol=1e-6, rtol=1e-14, maxiter=500)


# Regime test on the last Block 5 cross-section.
pd_c = predict_logit(b_full, cs[XCOLS].to_numpy())
s_hat_c = model_spread(pd_c)
w_eq = np.full(len(cs), 1.0 / len(cs))
dts_c = dur_by_issuer[iid] * spr_t
_, z_ref = dts_multiplier(spr_t, s_hat_c, dts_c, w_eq, z_ref=0.0)
m_calm, _ = dts_multiplier(spr_t, s_hat_c, dts_c, w_eq, z_ref)
m_shock, _ = dts_multiplier(spr_t * 461 / 259, s_hat_c, dts_c * 461 / 259, w_eq, z_ref)
m_fund, _ = dts_multiplier(spr_t * 461 / 259, s_hat_c * 461 / 259, dts_c * 461 / 259, w_eq, z_ref)
m_guard, _ = dts_multiplier(spr_t * 461 / 259, s_hat_c, dts_c, w_eq, z_ref, dts_max_ratio=1.05)
assert abs(m_calm - 1.0) < 1e-12 and abs(m_fund - 1.0) < 1e-12   # fundamentals: no add
assert m_shock > 1.0 and m_guard <= 1.05                          # overshoot: add, but never lever

# Capacity: a scalable core versus a CCC / fallen-angel satellite (all inputs illustrative).
core = dict(alpha0=0.010, alpha_min=0.0025, adv=14e9, horizon_days=20, kappa=0.03, turnover=0.6)
niche = dict(alpha0=0.030, alpha_min=0.0100, adv=1.5e9, horizon_days=20, kappa=0.05, turnover=2.0)
for spec in (core, niche):
    c_cf, c_num = capacity_closed_form(**spec), capacity_numeric(**spec)
    assert abs(c_num / c_cf - 1.0) < 1e-8
assert capacity_closed_form(**core) > 10 * capacity_closed_form(**niche)
print(f"DTS multiplier calm={m_calm:.2f} shock={m_shock:.2f} fundamental={m_fund:.2f} "
      f"guarded={m_guard:.2f}; capacity core=${capacity_closed_form(**core) / 1e9:.1f}bn "
      f"niche=${capacity_closed_form(**niche) / 1e9:.2f}bn")
```

*(The capacity inputs, including HY ADV of about \$14bn a day, are illustrative; SIFMA publishes the high yield split in its downloadable statistics, which we did not verify. With them the core sleeve's capacity is about \$49bn and the satellite's about \$1.2bn, the same order of magnitude as Blackstone's platform and Dynkin's \$2bn fallen-angel curve.)*

## 11.10 Desk Debrief

Theo unplugged the USB stick at 7:40 p.m. The 13-week model had become a covariate, capped at 13, and was now one of three features in a hazard function that covered 2,000 issuers. It seemed to be taking the demotion well.

- **High yield is a short put that pays a coupon.** The default jump carries skew of $-(1-2p)/\sqrt{p(1-p)}$: about $-6.9$ at a 2% PD, $-1.5$ at 20%. BB defense is tail avoidance; CCC defense is pricing.
- **$U = D = \beta$ is a dimmer switch.** A pure beta tilt gives equal capture ratios, and only alpha opens the gap. The average manager's 92.24%/89.56% reads as roughly a 0.91 beta with a small net alpha. Real defense is $\beta^{-} < \beta^{+}$, tested on pairs of regimes.
- **DD is a ranking, not a probability.** Map it to PD empirically, never with $N(-\text{DD})$, and send no-equity issuers to a separate, flagged model.
- **The label is the model.** With distressed exchanges at 65% of 2025 defaults, a PD trained on hard defaults is calibrated to a world that no longer exists. Label at the issuer, date it at announcement, and include LMEs that impair the holder.
- **A hit rate without an exclusion rate is half a sentence.** Default avoidance pays when $(\pi_X - \pi_K)L > s_X - s_K$; the same 77% can be +44bp or −9bp depending on how much of the table you folded.
- **CCC is a crowd, not a person.** Size the bucket by expected loss, choose inside it by PD, diversify it with breadth (high-PD risk is mostly idiosyncratic), and buy from forced sellers whose problem is a rating, not a balance sheet.
- **IDO or it didn't happen.** Every defensive signal is tested DTS-neutral first; a market-value-neutral low-risk tilt is beta wearing a factor's name tag.
- **Capacity is a square.** Halve turnover and capacity quadruples: exclusion and low risk scale into tens of billions, CCC reversal and fallen angels into low single-digit billions.

### The Spec You Hand the Robot

"Build an issuer-month panel from the security master, one row per ultimate parent per month. Label equals 1 if any of {payment default beyond grace, bankruptcy filing, distressed exchange, LME that impairs the holder} is *announced* in months $[t, t+12)$; drop rows whose window runs past the data. Features: empirically mapped distance-to-default (with `no_equity_flag`), CHS market and accounting covariates lagged to filing date, liquidity runway in weeks capped at 13, months since last LME, and the Chapter 13 PRS. Fit a calibrated dynamic logit with issuer-clustered errors and a gradient-boosted model, both with issuer-disjoint, 12-month-embargoed cross-validation; report AUC, AR (assert $\text{AR} = 2\,\text{AUC} - 1$ on untied scores), hit rate at 10/20/30% exclusion, and realized-versus-predicted default rates by PD decile. Portfolio: exclude the worst-PD quintile, tilt toward $(s_i - \hat\lambda_i L_i)/\text{DTS}_i$, hold $w^\top\text{DTS}$ within 1% of the benchmark times a regime multiplier in $[0.9, 1.2]$ driven by the DTS-weighted spread-to-model-spread residual, issuer cap 3%, long-only, no leverage. Report $U$, $D$, $\beta^{+}$, $\beta^{-}$ on benchmark regimes. Halt and alert if portfolio DTS deviates from target by more than 2%, if any weight is negative, if the target DTS is unreachable without leverage, or if a z-signal purchase has a PRS above threshold."

ROBO acknowledged the spec. It did not ask what "impairs the holder" meant, because the spec now had a list.

### Exercises

1. **The top-quartile hand history.** The top-quartile manager captured 99.00% of up markets and 92.00% of down markets (BlackRock p.3). With regime means of +1.6% and −2.0% a month, recover $\alpha$ and $\beta$ from the identity in §11.2.1. Then find the zero-alpha asymmetric portfolio ($\beta^{+}, \beta^{-}$) that produces the same two capture ratios, and explain to a consultant why the two portfolios are indistinguishable on capture ratios and very different on a regime-pair test.
2. **Skew by tier.** Show that $-\frac{1-2p}{\sqrt{p(1-p)}}$ is increasing in $p$ on $(0, \tfrac12)$, that is, the jump component gets *less* negatively skewed as the PD rises. Compute it at 1% and 10%. Write one paragraph on what this implies for the size of a BB position versus a CCC position at equal expected loss.
3. **Ines's question, answered.** Assume a binormal score model: defaulters' scores are $N(\mu, 1)$, survivors' $N(0, 1)$, with base rate 3% and AUC 0.85. Using $\text{AUC} = \Phi(\mu/\sqrt2)$, find the exclusion fraction $q$ at which the hit rate is 77%. (You should get about 25%.) Then compute the active return from §11.5.2 with $L = 0.6$ and an excess spread of 400bp in the excluded set, and state whether the claim is good news.
4. **The soft-default world.** Re-run Block 3 with `de_share=0.65`, Moody's 2025 share. Train on the hard-default label, score against the full label, and report the calibration error by PD decile. Can the prior-shift formula of §11.4.2 repair it? (It repairs the level. Explain why it cannot repair the ranking when distressed exchanges are concentrated in sponsor-owned issuers with drop-down capacity, and add a feature that can.)
5. **ROBO, defensively.** Theo's next spec reads "minimize realized defaults while beating the index." List three portfolios ROBO could build that satisfy the sentence literally and that you would never run (hint: one involves holding a single BB bond, one involves leverage, one involves the definition of "default"), and write the constraint that rules each one out.
6. **Capacity is a square.** Prove from the formula of §11.9 that halving turnover multiplies capacity by four. Compute the niche sleeve's capacity at a turnover of 1.0 instead of 2.0, and then explain why, in practice, cutting turnover in a CCC-reversal strategy also cuts $\alpha_0$, so the quadrupling never fully arrives.

### Deep-Dive Resource Graph

**Podcasts** *(episode-level titles and links not verified this session; search the series archives)*
- Bloomberg *Odd Lots*: episodes on high yield, CCC credit, and liability management.
- *Flirting with Models* (Corey Hoffstein): episodes on systematic fixed income and factor investing in bonds.
- Man Institute and BlackRock podcasts on systematic credit.

**Practitioner Writing**
- BlackRock (Parker, Radell, Aguiar, Kang), *A systematic approach to high yield credit* (December 2025): https://www.blackrock.com/gls-download/literature/whitepaper/systematic-high-yield-credit.pdf
- Moody's Analytics (David Hamilton), *Lend, extend, and then…* (18 May 2026): https://www.moodys.com/web/en/us/insights/credit-risk/private-credit/lend-extend-and-then.html
- State Street Investment Management, *Global high yield—2025 in review and 2026 outlook*: https://www.ssga.com/library-content/assets/pdf/global/fixed-income/2026/2025-global-high-yield-update-fixed-income.pdf
- Loomis Sayles, *Quarterly Credit Update 4Q24*: https://info.loomissayles.com/hubfs/FD%20Quarterly%20Credit%20Update_4Q24%20FINAL.pdf
- Wellington, *CCC junk bonds appear undervalued and overlooked*: https://www.wellington.com/en/insights/ccc-junk-bonds-appear-undervalued-and-overlooked
- UBS Asset Management, *2025 fixed income default study* (17 January 2025): https://www.ubs.com/us/en/assetmanagement/insights/asset-class-perspectives/fixed-income/articles/2025-fixed-income-default-study.html
- The DESK (Dan Barnes), *Defaults creep higher in leveraged credit markets* (27 May 2026): https://www.fi-desk.com/defaults-creep-higher-in-leveraged-credit-markets/
- Investment Executive, *U.S. leveraged loan defaults to ease in 2026: Fitch* (3 December 2025): https://www.investmentexecutive.com/news/u-s-leveraged-loan-defaults-to-ease-in-2026-fitch/
- Title only: Robeco research on low-risk and conservative credits; Barclays QPS notes on equity momentum in credit; S&P Global Ratings *Default, Transition, and Recovery* series; Fitch *U.S. Leveraged Finance Default Insight*.

**Academic Papers**
- Shumway, T. (2001), *Forecasting Bankruptcy More Accurately: A Simple Hazard Model*, Journal of Business 74(1): https://ideas.repec.org/a/ucp/jnlbus/v74y2001i1p101-24.html
- Chava, S. and Jarrow, R. (2004), *Bankruptcy Prediction with Industry Effects*, Review of Finance 8(4): https://ideas.repec.org/a/oup/revfin/v8y2004i4p537-569..html
- Campbell, J., Hilscher, J. and Szilagyi, J. (2008), *In Search of Distress Risk*, Journal of Finance 63(6); NBER WP 12362: https://www.nber.org/papers/w12362
- Alanis, E., Chava, S. and Shah, A. (2022), *Benchmarking Machine Learning Models to Predict Corporate Bankruptcy*: https://arxiv.org/abs/2212.12051
- Houweling, P. and van Zundert, J. (2017), *Factor Investing in the Corporate Bond Market*, Financial Analysts Journal 73(2): https://papers.ssrn.com/abstract=2516322
- Frazzini, A. and Pedersen, L. H. (2014), *Betting Against Beta*, Journal of Financial Economics 111(1); and Dick-Nielsen, J., Feldhütter, P., Pedersen, L. H. and Stolborg, C., *Corporate Bond Factors: Replication Failures and a New Framework* (both listed at https://www.lhpedersen.com/research)
- Title only: Altman (1968), *Financial Ratios, Discriminant Analysis and the Prediction of Corporate Bankruptcy*; Merton (1974), *On the Pricing of Corporate Debt*; Bharath and Shumway (2008), *Forecasting Default with the Merton Distance to Default Model*; Duan, Sun and Wang (2012), *Multiperiod Corporate Default Prediction: A Forward Intensity Approach*; Engelmann, Hayden and Tasche (2003), *Testing Rating Accuracy*; Israel, Palhares and Richardson (2018), *Common Factors in Corporate Bond Returns*.

**Data & Code**
- FRED, ICE BofA US High Yield OAS and tiers: https://fred.stlouisfed.org/series/BAMLH0A0HYM2, https://fred.stlouisfed.org/series/BAMLH0A1HYBB, https://fred.stlouisfed.org/series/BAMLH0A2HYB, https://fred.stlouisfed.org/series/BAMLH0A3HYC (CSV via `https://fred.stlouisfed.org/graph/fredgraph.csv?id=<SERIES>`; ICE series carry a rolling three-year history on FRED).
- Open Source Bond Asset Pricing (TRACE panels, bond factors, ML predictor panel): https://openbondassetpricing.com/
- NUS Credit Research Initiative (free PD term structures for listed firms, a public benchmark for your model): https://nuscri.org/en/
- SIFMA US Corporate Bonds Statistics: https://www.sifma.org/resources/research/statistics/us-corporate-bonds-statistics/
- iShares HYDB summary data: https://stockanalysis.com/etf/hydb/
- SEC EDGAR (credit agreements and indentures for covenant and basket features): https://www.sec.gov/edgar

<!-- STATUS: COMPLETE -->
