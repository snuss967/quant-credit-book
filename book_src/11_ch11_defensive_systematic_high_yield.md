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

"So who at this table knows more than you?" She tapped the screen. "Not the index. The index is sixty percent double-B. It's wearing a 323 basis point bow tie. The CCCs are wearing a 1,278 basis point necktie. Same companies' cousins, different dress code."

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

Kaz read the definition aloud. "A distressed exchange is when the issuer offers holders a new security that amounts to a diminished financial obligation, and the purpose is to avoid default."

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
