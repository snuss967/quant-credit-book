# Chapter 6: Stochastic Calculus, Intensity Models & Structural Frameworks

> *"In many discussions of credit risk, Merton (1974) is the first—and occasionally also the last—model considered."* (Bolder_Credit_Risk_Modelling p.257)

## Cold Open: Column N

It is 1:07 a.m. and Theo is porting his thirteen-week cash flow model into the desk's Python stack one column at a time, like a man moving house with a teaspoon. The USB stick is in the laptop. Emotional support is being provided.

Kaz leans over. "Why is column N called 'Liquidity Runway (weeks)'?"

"Because that's how many weeks until the revolver is fully drawn and the minimum liquidity covenant trips."

"And column O is the probability you get through week $k$, given you got through week $k-1$?"

"It's the share of our forty downside scenarios that hit the floor that week."

Kaz writes on the whiteboard: $S(t_k)=\prod_{j\le k}(1-\lambda_j\Delta t)$. "That's a piecewise-constant hazard curve. You've been bootstrapping survival functions since analyst year one. Just with worse fonts."

Mags, who is reading a disclosure statement for pleasure, does not look up. "Price is what you pay. Recovery is what you get, eventually, after the lawyers. Which one is column N?"

"Neither," Theo says. "It's *when*."

"Good," Ines says, rolling her chair over. "What's the pot, what are the odds, and who at this table knows more than you?" She taps the screen. "The pot is the bond. The odds are column O. The person who knows more than you is whoever is offering you five-year protection on this name at 480 and would love for you to lift it." *(illustrative)*

"The CDS desk has a hazard curve too," Kaz says. "Theirs lives in $\mathbb{Q}$. Yours lives in $\mathbb{P}$. The difference between them is somebody's bonus."

ROBO, asked to "compute the default probability," returns 100%. Every firm defaults eventually if you wait long enough. It is technically correct, which is ROBO's favorite kind of correct.

Theo looks at the ticker in the corner of his screen. The issuer's stock is down 40% in a month and its realized volatility is 95%. "If the stock is a call option on the assets," he says slowly, "then the stock price already knows something about column O."

"It does," Kaz says. "It will tell you, if you can solve two nonlinear equations by Friday."

**The question this chapter answers:** *how do you turn a balance sheet and a stock price into a probability of default, how do you turn a CDS curve into another one, and how do you know which measure each number lives in before you trade the difference?*

By the end of this chapter you will be able to: derive Itô's lemma and explain its $\tfrac12\sigma^2$ "volatility tax"; price Merton (1974) equity, debt, and spread in closed form and explain why its short-end spread is zero; move a default probability between $\mathbb{P}$ and $\mathbb{Q}$ and say what the gap is worth; solve the KMV inverse problem for asset value and asset volatility; compute a Black–Cox first-passage probability with a covenant barrier, in closed form and by bias-corrected Monte Carlo; price defaultable bonds under the three recovery conventions with a Cox-process intensity; get CIR survival curves in closed form; bootstrap a piecewise-constant hazard curve from CDS quotes; and specify all of it to ROBO precisely enough that it cannot report a 0.00% PD for the high-yield index.

## 6.1 Itô's Lemma: The Volatility Tax

### 6.1.1 Desk framing: every claim is a function of something random

Theo's waterfalls have always been functions. The equity recovery in his plan-of-reorganization model was $\max(\text{EV}-\text{claims ahead},0)$; the second-lien recovery was a ramp that started at the first-lien's par and stopped at its own. What he never had to do was ask how fast those functions *move* when enterprise value wiggles every day. On a systematic desk that is the whole job, because the hedge ratio, the expected return, and the volatility of every security are derivatives of a payoff function with respect to a random state variable.

Ordinary calculus says $df = f'(V)\,dV$. Kaz's position is that ordinary calculus is a fine tool for things that do not wiggle, like bridges and Mags's opinion of adjusted EBITDA. For things that do, there is a correction term, and it is not optional.

### 6.1.2 The derivation

Let the firm's asset value follow geometric Brownian motion under the physical measure $\mathbb{P}$:

$$
dV_t=\mu V_t\,dt+\sigma_V V_t\,dW_t,
$$

where $\mu$ is the expected asset return (annualized), $\sigma_V$ is the asset volatility (annualized, decimal), and $W_t$ is a standard Brownian motion with respect to the filtration $\mathcal{F}_t$. Take any smooth function $f(t,V)$ and expand it to second order:

$$
df=f_t\,dt+f_V\,dV+\tfrac12 f_{VV}\,(dV)^2+f_{tV}\,dt\,dV+\tfrac12 f_{tt}\,(dt)^2+\cdots
$$

The rules that make stochastic calculus different are the multiplication table $(dt)^2=0$, $dt\,dW_t=0$, and $(dW_t)^2=dt$. The last one is the surprise. Over $[0,T]$ split into $n$ steps of length $\Delta t=T/n$, the sum $\sum_i(\Delta W_i)^2$ has mean $\sum_i\Delta t=T$ and variance $\sum_i 2\Delta t^2=2T^2/n\to0$. So the sum of squared increments converges to the deterministic number $T$: Brownian motion's squared wiggles do not vanish, they add up to time itself. Hence

$$
(dV_t)^2=\sigma_V^2V_t^2\,(dW_t)^2=\sigma_V^2V_t^2\,dt,
$$

and the second-order term that ordinary calculus discards is now first order. Collecting terms gives **Itô's lemma**:

$$
df=\Big(f_t+\mu V f_V+\tfrac12\sigma_V^2V^2 f_{VV}\Big)dt+\sigma_V V f_V\,dW_t.
$$

Apply it to $f=\ln V$, with $f_V=1/V$, $f_{VV}=-1/V^2$, $f_t=0$:

$$
d\ln V_t=\Big(\mu-\tfrac12\sigma_V^2\Big)dt+\sigma_V\,dW_t,\qquad V_T=V_0\exp\!\Big[\big(\mu-\tfrac12\sigma_V^2\big)T+\sigma_V W_T\Big].
$$

So $\ln V_T$ is normal with mean $\ln V_0+(\mu-\tfrac12\sigma_V^2)T$ and variance $\sigma_V^2T$. The mean of $V_T$ is $V_0e^{\mu T}$, but the median is $V_0e^{(\mu-\frac12\sigma_V^2)T}$, lower by the factor $e^{-\frac12\sigma_V^2T}$.

That factor is the volatility tax. Itô's lemma is the tax code of stochastic calculus: the $\tfrac12\sigma_V^2$ is withheld at source from every log return, and the only refund is convexity. If you own a payoff with $f_{VV}>0$, the drift of your claim picks up $+\tfrac12\sigma_V^2V^2f_{VV}\,dt$. In a levered firm the equity holders own the convexity and the bondholders sold it to them, which is the entire Merton model in one sentence, previewed.

### 6.1.3 Annualize or die

The $\sigma_V$ in every formula in this chapter is annualized. Daily equity returns give a daily standard deviation; multiply by $\sqrt{252}$ (trading days) or, for weekly data, $\sqrt{52}$. The $\sqrt{\cdot}$ comes straight from $(dW)^2=dt$: variance scales with time, so volatility scales with its square root.

> **Ways This Blows Up.** *The unannualized sigma.* A stock with 6% daily volatility has an annualized volatility of about $0.06\sqrt{252}\approx 95\%$. Feed the 6% into a Merton solver as if it were annual and the model concludes that the firm's assets barely move, its distance to default is enormous, and its one-year PD rounds to zero. The error is silent: nothing crashes, the numbers simply look like an investment-grade utility. Two guards belong in every spec: assert that $\sigma_E$ lies in a plausible annual range (say 5%–300%) and store the sampling frequency next to every volatility field. The reverse error, simulating with $\mu$ instead of $\mu-\tfrac12\sigma_V^2$ in the log drift, biases every simulated path upward by the volatility tax and makes high-volatility names look safer than they are.

> **[SOURCE EXTRACTION]** *Veronesi_Fixed_Income_Securities p.552:* "Ito's lemma (Equation 14.37) says that the capital gain dollar return of a bond has two components: The first component is a predictable "dt" component that depends on the curvature of the function F(X). The second component is a random term given by the sensitivity of the bond price to changes in the underlying variable"
>
> **Annotation.** Veronesi's state variable is an interest rate; ours is asset value $V_t$ or, from §6.6 on, a default intensity $\lambda_t$. The structure transfers exactly: the predictable term depending on curvature is the convexity refund, and the random term is the hedge ratio times the shock. What changes in credit is the *sign* of the curvature across the capital structure. Equity is convex in $V$; senior debt is concave (it is short a put), so a bondholder's expected return carries a negative convexity term that must be paid for in spread. Where the 2026 desk departs from Veronesi: his $X$ is observable on a screen, while $V_t$ is not. Every structural credit model applies Itô to a latent variable and must first back that variable out of equity prices, which is the inverse problem of §6.4. Veronesi's p.562 list of what Itô buys (expected returns, price volatility, hedge ratios) is precisely the list of outputs a credit desk's structural engine produces daily.

### 6.1.4 Column N, renamed

Return to Theo's spreadsheet. Column O holds the conditional probability $h_k$ of hitting the liquidity floor in week $k$ given survival through week $k-1$. The probability of surviving $k$ weeks is the product of the per-week survival probabilities:

$$
S(t_k)=\prod_{j=1}^{k}(1-h_j),\qquad h_j=\lambda_j\Delta t,\quad \Delta t=\tfrac{1}{52}.
$$

Take logs and use $\ln(1-x)=-x+O(x^2)$:

$$
\ln S(t_k)=\sum_{j=1}^k\ln(1-\lambda_j\Delta t)=-\sum_{j=1}^k\lambda_j\Delta t+O(\Delta t)\;\longrightarrow\;-\int_0^{t}\lambda_s\,ds,
$$

so in the continuous limit $S(t)=\exp\!\big(-\int_0^t\lambda_s\,ds\big)$. The weekly hazard $\lambda_j$ is constant within each week: a piecewise-constant hazard curve, which is exactly the object a CDS bootstrap produces in §6.8. Theo renames column N from "Runway" to $S(t)$. Kaz updates the fonts. The thirteen-week model has been reborn as a survival curve; it was always one, it just did not know the Greek.

## 6.2 Merton 1974: Equity Is a Call, Debt Is a Short Put

### 6.2.1 Desk framing: every waterfall is a payoff diagram

Merton's firm has one asset worth $V_t$ and one zero-coupon debt claim with face value $F$ due at $T$. At maturity, if $V_T\ge F$ the debt is paid in full and equity keeps the rest; if $V_T<F$ the bondholders take the firm. So

$$
E_T=\max(V_T-F,0),\qquad B_T=\min(V_T,F)=F-\max(F-V_T,0).
$$

We write the market value of the debt claim as $B_t$ (B for bond). The style bible reserves $D$ for duration and $P(t,T)$ for the riskless discount factor, so neither is available.

Theo has drawn this picture a hundred times, labeled "Recovery by Class." Equity is a call struck at the debt. The debt is a riskless bond minus a put that the bondholders wrote to the shareholders. The fulcrum security, the class that converts into the new equity, is the tranche whose strike sits where the asset distribution has its mass: the class that is neither deep in the money (paid in full) nor so far out of the money that the plan gives it a tip. RSSG trained Theo to find the fulcrum by reading the waterfall. Merton finds it by reading the option.

> **[SOURCE EXTRACTION]** *Ben_Dor_Quantitative_Credit_Portfolio_Management p.105:* "The key insight provided by Merton is that, in this setup, the firm's equity is equivalent to a European option on the firm's asset value and can be valued using the Black-Scholes option pricing equation."
>
> **Annotation.** Ben Dor and coauthors use Merton as the theoretical foundation for Duration Times Spread: if debt is a riskless bond minus a put, then spread changes scale with the spread level, and on p.109 they show the relationship between spread and spread volatility is close to linear in the investment-grade range. That linearity is why DTS works as a risk measure (Chapter 8). The 2026 desk keeps the insight and drops the literal model: nobody prices an IG bond off a single-maturity Merton put, but every systematic credit risk model that scales spread volatility by spread level is quietly using it. Where the desk departs: the "European" part. Real debt has many maturities, coupons, covenants, and an issuer that can call a lender meeting before $T$; §6.5 and §6.9 deal with what the European assumption hides.

### 6.2.2 Replication and the pricing PDE

Assume for now that $V_t$ is traded (Kaz: "assume it's traded"; Mags: "you cannot short a factory"; both are right, and §6.4 deals with the consequences). Form a portfolio long one unit of equity and short $\Delta$ units of the asset: $\Pi=E-\Delta V$. By Itô's lemma applied to $E(t,V)$,

$$
d\Pi=\Big(E_t+\mu VE_V+\tfrac12\sigma_V^2V^2E_{VV}-\Delta\mu V\Big)dt+\big(E_V-\Delta\big)\sigma_VV\,dW_t.
$$

Choose $\Delta=E_V$. The $dW_t$ term vanishes, so the portfolio is riskless and must earn the riskless rate, $d\Pi=r\Pi\,dt=r(E-VE_V)\,dt$. Equating drifts, the $\mu$ terms cancel and

$$
E_t+rVE_V+\tfrac12\sigma_V^2V^2E_{VV}-rE=0,
$$

with terminal condition $E(T,V)=\max(V-F,0)$ and boundary condition $E(t,0)=0$. This is the Black–Scholes PDE (Bohn and Stein give the same replication argument in their Appendix 3A, Bohn_Stein_Active_Credit_Portfolio_Management p.206). The physical drift $\mu$ has disappeared: the price is the same as if assets grew at $r$, which is the statement that prices are expectations under the risk-neutral measure $\mathbb{Q}$. Default probabilities, which are about what will actually happen, still need $\mu$. Keeping those two facts in separate drawers is §6.3.

### 6.2.3 Closed forms

The solution is the Black–Scholes call on $V$:

$$
E_0=V_0N(d_1)-Fe^{-rT}N(d_2),\qquad d_1=\frac{\ln(V_0/F)+(r+\tfrac12\sigma_V^2)T}{\sigma_V\sqrt T},\qquad d_2=d_1-\sigma_V\sqrt T,
$$

where $N(\cdot)$ is the standard normal CDF. The debt is whatever is left:

$$
B_0=V_0-E_0=Fe^{-rT}N(d_2)+V_0N(-d_1)=Fe^{-rT}-\underbrace{\Big[Fe^{-rT}N(-d_2)-V_0N(-d_1)\Big]}_{\text{put on }V\text{ struck at }F}.
$$

Read the middle expression as a waterfall: with risk-neutral probability $N(d_2)$ the bondholders receive $F$, discounted; otherwise they receive the assets, whose risk-neutral value conditional on default contributes $V_0N(-d_1)$. The risk-neutral default probability is $\mathbb{Q}(V_T<F)=N(-d_2)$.

Two more results fall out of Itô. Applying the lemma to $E(t,V)$, the diffusion coefficient of equity is $\sigma_VVE_V=\sigma_VVN(d_1)$, so

$$
\sigma_EE_0=N(d_1)\,\sigma_VV_0\qquad\Longleftrightarrow\qquad \sigma_E=\sigma_V\cdot\frac{V_0}{E_0}N(d_1).
$$

Equity volatility is asset volatility times a leverage multiplier. And under $\mathbb{P}$ the log asset value at $T$ is normal with mean $\ln V_0+(\mu-\tfrac12\sigma_V^2)T$, so the physical default probability is $N(-DD)$ with the **distance to default**

$$
DD=\frac{\ln(V_0/F)+(\mu-\tfrac12\sigma_V^2)T}{\sigma_V\sqrt T},
$$

the number of standard deviations of $\ln V_T$ separating the expected log asset value from the default point. Note that $d_2$ is $DD$ with $\mu$ replaced by $r$. Mixing the two inside one formula is the most common bug in Merton code that compiles.

### 6.2.4 The spread, a worked example, and the short-end embarrassment

The continuously compounded credit spread over the riskless rate is defined by $B_0=Fe^{-(r+s)T}$:

$$
s(T)=-\frac1T\ln\frac{B_0}{Fe^{-rT}}=-\frac1T\ln\!\Big[N(d_2)+\frac{N(-d_1)}{\ell}\Big],\qquad \ell=\frac{Fe^{-rT}}{V_0},
$$

where $\ell$ is quasi-leverage. Spread depends only on $\ell$, $\sigma_V\sqrt T$, and $T$: leverage and volatility are the two inputs that matter, as Bohn and Stein put it (p.137), "asset volatility is much more important to default prediction than is asset drift."

*Worked example (illustrative).* Take $V_0=100$, $F=80$, $r=4\%$, $\sigma_V=25\%$, $T=1$. Then $\ln(1.25)=0.2231$, $d_1=(0.2231+0.0713)/0.25=1.178$, $d_2=0.928$, $N(d_1)=0.881$, $N(d_2)=0.823$, and $Fe^{-rT}=76.86$. Equity is $E_0\approx 88.05-63.27=24.78$; debt is $B_0\approx75.22$; the spread is $s\approx-\ln(75.22/76.86)\approx 2.16\%$, or about 216 bp; and $\mathbb{Q}(\tau\le1)=N(-0.928)\approx17.7\%$. The implied equity volatility is $\sigma_E\approx0.25\times(100/24.78)\times0.881\approx89\%$, a leverage multiplier of about 3.6. With $\mu=8\%$, $DD\approx1.09$ and the physical PD is about 13.8%.

Look at what the model says about recovery. A 17.7% risk-neutral default probability and a 216 bp spread imply a risk-neutral loss given default of roughly $0.0216/0.177\approx12\%$: Merton's defaulted firm recovers about 88 cents. That is because default in a diffusion model happens to firms that missed par *by a little*, with $V_T$ just under $F$. Mags's defaulted firms miss by a lot, then pay advisers for eighteen months. Endogenous recovery that is too high is the first reason pure Merton spreads come out too tight.

The second reason is the short end. For $V_0>F$, as $T\downarrow0$, $d_2\approx\ln(V_0/F)/(\sigma_V\sqrt T)\to+\infty$. The Mills-ratio bound $N(-x)\le\phi(x)/x$ means $N(-d_2)$ decays like $\exp(-c/T)$, faster than any power of $T$, and $N(-d_1)$ does the same. So the bracket in $s(T)$ tends to 1 and

$$
\lim_{T\downarrow0}s(T)=0.
$$

A Merton firm cannot default tomorrow unless it is already dead today. Mags has a list of firms that disagree, alphabetized. In the worked example the three-month Merton spread is about 70 bp and the two-and-a-half-week spread is under 1 bp, while CCC paper of any tenor trades hundreds of basis points wide. Duffie and Lando (2001, p.634) state the problem precisely: "With perfect information, yield spreads for surviving firms are zero at zero maturity, and are relatively small for small maturities, regardless of the riskiness of the firm." Their fix, noisy accounting information, is the bridge to the reduced-form models of §6.6: if investors cannot see exactly how close $V_t$ is to the barrier, default arrives as a surprise with an intensity, and short spreads become strictly positive.

> **[SOURCE EXTRACTION]** *Schmid_Credit_Risk_Pricing_Models p.118:* "But Franks & Torous (1994) find that the strict absolute priority rule was violated in 78% of the bankruptcies they considered. Thus, the assumptions of the Merton model are highly stylized versions of reality."
>
> **Annotation.** Merton's payoff $\min(V_T,F)$ assumes absolute priority holds to the penny. Mags's view is that absolute priority is a starting bid. Franks and Torous documented deviations in the 1980s Chapter 11 world, when old equity routinely got a tip to vote yes; the 2020s versions are different but larger: non-pro-rata uptiers, drop-downs, and "open market purchases" that re-rank creditors *within* a class before any court sees them. For the systematic desk, the practical consequence is that the strike $F$ is not a constant read off the balance sheet but a function of who is in the room. §6.5 makes that a barrier problem; Chapter 13 makes it a game. The Merton payoff diagram stays right in shape. What it gets wrong is the *location* of the kink and the *date* on which it is evaluated.

> **Desk Myth vs. Desk Reality.** *Myth:* "Merton is a textbook model; nobody trades off it." *Reality:* nobody trades off the 1974 single-zero-coupon version. Structural default models, fed daily equity prices and refreshed capital structures, underpin some of the largest systematic credit platforms in the market (Trend Watch below). The model did not die; it moved from the pricing desk to the signal library, and it picked up a data feed and an empirical calibration on the way. Bolder's joke that Merton is often "the first—and occasionally also the last—model considered" is accurate about textbooks. On the systematic desk it is the first model considered and then the third feature in the alpha model, behind value and momentum.

> **Trend Watch.** *The structural renaissance on the systematic desk (2010–2026).* Three data points mark how far structural models have travelled from the 1974 paper. **(1) Blackstone.** Blackstone's systematic credit platform (Blackstone Corporate Bond Strategies, BCBS) describes itself as "the largest pure-play quantitative credit operation in the world, with over \$40 billion in assets under management," and traces its engine to Diversified Credit Investments (DCI), acquired in late 2020 and co-founded by the creators of the KMV model (Blackstone_Systematic_Credit p.1; the shelf document is undated, so treat the AUM figure as of its publication). **(2) BlackRock.** BlackRock's systematic high-yield team reports that its proprietary probability-of-default signal "has successfully identified 77% of the defaulted bonds in the ICE BofA High Yield Index within 24 months of its default since 2010," data as of March 31, 2024 (BlackRock_Systematic_High_Yield_Credit p.6). **(3) Barclays research.** Dynkin and coauthors report that Merton-based analytical equity hedge ratios predict bond-to-equity sensitivity reasonably well, with Merton ratios roughly 5% lower than empirically matched ones in both IG and HY over January 1993 to December 2019 (Dynkin_Systematic_Investing_in_Credit p.87–88, p.115). What it means for the desk: the 2026 use of a structural model is not "price this bond." It is "rank 3,000 issuers daily by how close equity says they are to the default point, compare that with what the spread says, and trade the difference," which is the $\mathbb{P}$-versus-$\mathbb{Q}$ gap of §6.3 dressed as a factor. The academic trend runs the same way: Goyal, Bali, Huang, Jiang, and Wen (2020 working paper), *Predicting Corporate Bond Returns: Merton Meets Machine Learning*, report that imposing Merton structure on machine-learning models improves out-of-sample bond return prediction (bridge to Chapter 7).

> **[SOURCE EXTRACTION]** *Blackstone_Systematic_Credit p.1:* "It uses structural default models (similar to the Merton model) that analyze a company's capital structure, cash flows, leverage, and real-time equity market signals to calculate daily, dynamic default probabilities for thousands of corporate issuers."
>
> **Annotation.** Each phrase maps to a section of this chapter. "Capital structure" and "leverage" set $F$ and the default point (§6.4). "Real-time equity market signals" supply $E_t$ and $\sigma_E$, from which $(V_t,\sigma_V)$ are inverted daily (§6.4). "Daily, dynamic default probabilities for thousands of issuers" is a cross-sectional engine, which means the solver has to be vectorized, guarded, and robust to the 5% of names where it fails (§6.11). "Cash flows" is the part the 1974 model never had; it is the hook for Theo's thirteen-week model as a feature. Where we depart: a vendor PD is a $\mathbb{P}$ quantity calibrated to historical defaults. The trading signal is its gap to the $\mathbb{Q}$ hazard in the CDS or bond spread, and the gap only means something after you strip the risk premium you were *supposed* to earn. IDO or it didn't happen.

> **[SOURCE EXTRACTION]** *BlackRock_Systematic_High_Yield_Credit p.6:* "Our proprietary probability of default signal that has underpinned all of our credit strategies for over 20 years has successfully identified 77% of the defaulted bonds in the ICE BofA High Yield Index within 24 months of its default since 2010."
>
> **Annotation.** Read the metric carefully: a hit rate on defaulters within a 24-month window, not a calibration statement and not a false-positive rate. A signal that flags every CCC name catches most defaulters too. The desk's question is the ROC curve and the cost of the flags that did not default: how many performing bonds were sold early, at what markout. Chapter 7 turns this into purged cross-validation; here the lesson is that structural PDs are *ranking* devices first and *probability* devices second, which is also why the KMV mapping from DD to EDF in §6.4 is empirical rather than Gaussian.

### Deep-Dive Resource Graph

- **Podcasts:** Bloomberg *Odd Lots* episodes on systematic credit and on credit-equity linkages (search the archive; episode titles not verified this session, so no links).
- **Practitioner Writing:** Blackstone, *Systematic Credit* (shelf: Blackstone_Systematic_Credit); BlackRock, *Systematic High Yield Credit* (shelf: BlackRock_Systematic_High_Yield_Credit); Dynkin et al., *Systematic Investing in Credit*, chapters on equity-credit hedge ratios (shelf p.87–88).
- **Academic Papers:** Merton (1974), *On the Pricing of Corporate Debt: The Risk Structure of Interest Rates*, Journal of Finance 29(2); Duffie and Lando (2001), *Term Structures of Credit Spreads with Incomplete Accounting Information*, Econometrica 69(3), https://econometricsociety.org/publications/econometrica/2001/05/01/term-structures-credit-spreads-incomplete-accounting ; Schaefer and Strebulaev (2008), *Structural Models of Credit Risk Are Useful: Evidence from Hedge Ratios on Corporate Bonds*, Journal of Financial Economics; Goyal, Bali, Huang, Jiang, and Wen (2020), *Predicting Corporate Bond Returns: Merton Meets Machine Learning*, Swiss Finance Institute working paper.
- **Data & Code:** SEC EDGAR full-text search and filings for capital-structure inputs, https://www.sec.gov/edgar ; the `merton_prices` reference implementation in §6.11.

## 6.3 $\mathbb{P}$ to $\mathbb{Q}$: The Credit Risk Premium

### 6.3.1 Desk framing: what happens versus what it costs to find out

RSSG trained Theo in $\mathbb{P}$. A recovery analysis asks what will actually happen: how much EBITDA, what multiple, which classes get paid. A CDS quote lives in $\mathbb{Q}$: it is the price at which someone will take the other side of that question, and that someone wants paying for the risk that the answer arrives in a recession, when everything else in their book is also losing money.

> **Poker Table.** Ines draws two columns on a napkin: "$\mathbb{P}$: what happens. $\mathbb{Q}$: what the table charges you to find out." Physical PDs are the true odds of the hand. Risk-neutral PDs are the odds implied by the price of the bet, and they are always worse for the buyer of protection, because default risk is concentrated in states of the world where everyone's chips are worth more. "The difference is the rake," she says. "And on this desk, we are the house." Then the hand history. Theo's first week: a vendor model gave a name a 2% one-year $\mathbb{P}$-PD, the CDS curve implied a 3.4% $\mathbb{Q}$ hazard, and Theo wanted to sell protection because "the market is too scared." The twenty-day markout was flat. Nothing was mispriced. He had rediscovered the risk premium, which is not alpha. It is carry with a jump in it, and the jump is what you are paid to own. *(illustrative)*

### 6.3.2 The measure change

Girsanov's theorem says that if we define

$$
dW^{\mathbb{Q}}_t=dW_t+\frac{\mu-r}{\sigma_V}\,dt,
$$

then $W^{\mathbb{Q}}$ is a Brownian motion under a measure $\mathbb{Q}$ equivalent to $\mathbb{P}$, and substituting into the asset dynamics,

$$
dV_t=\mu V_t\,dt+\sigma_VV_t\Big(dW^{\mathbb{Q}}_t-\frac{\mu-r}{\sigma_V}dt\Big)=rV_t\,dt+\sigma_VV_t\,dW^{\mathbb{Q}}_t.
$$

The volatility is unchanged; only the drift moves, from $\mu$ to $r$. The quantity $(\mu-r)/\sigma_V$ is the asset's market price of risk. To pin it down, Bohn and Stein (Appendix 3B) use the CAPM: $\mu-r=\beta_A(\mu_M-r)$ with asset beta $\beta_A=\rho\,\sigma_V/\sigma_M$, where $\rho$ is the correlation of asset returns with the market and $\sigma_M$ is market volatility. Write the market Sharpe ratio as $\text{SR}_M=(\mu_M-r)/\sigma_M$ (not $\lambda$, which this book reserves for default intensity). Then $(\mu-r)/\sigma_V=\rho\,\text{SR}_M$ and, comparing $d_2$ with $DD$ from §6.2.3,

$$
DD^{\mathbb{Q}}=DD^{\mathbb{P}}-\rho\,\text{SR}_M\sqrt T,\qquad \text{PD}^{\mathbb{Q}}=N\!\Big(N^{-1}\big(\text{PD}^{\mathbb{P}}\big)+\rho\,\text{SR}_M\sqrt T\Big).
$$

Because $N$ is increasing and the shift is positive whenever $\rho>0$, $\text{PD}^{\mathbb{Q}}>\text{PD}^{\mathbb{P}}$.

*Worked example (illustrative).* In the §6.2.4 firm, $\mu-r=4\%$ and $\sigma_V=25\%$ give a market price of risk of $0.16$, which is what $\rho=0.4$ and $\text{SR}_M=0.4$ deliver. The one-year shift is $0.16$: $DD^{\mathbb{P}}\approx1.09$ becomes $DD^{\mathbb{Q}}\approx0.93=d_2$, and the PD rises from about 13.8% to about 17.7%, a ratio of 1.3. Now take a safe issuer with $DD^{\mathbb{P}}=3.0$. The same shift moves the PD from $N(-3.0)\approx0.135\%$ to $N(-2.84)\approx0.226\%$, a ratio of 1.7. The same additive shift in DD space is a larger *multiplicative* shift for safer names, because the normal tail is steeper further out. That is the structural-model version of a stylized fact every IG trader knows: investment-grade spreads are many multiples of expected loss, while distressed spreads are closer to it. Note also the $\sqrt T$: the premium grows with horizon, so five-year $\mathbb{Q}$ PDs are further from $\mathbb{P}$ than one-year PDs.

> **[SOURCE EXTRACTION]** *Bohn_Stein_Active_Credit_Portfolio_Management p.210:* "The risk-neutral DD is smaller than the physical DD, reflecting the adjustment that results in a higher PD, all else equal."
>
> **Annotation.** The adjustment is one line of algebra; getting it wrong is a career. Two errors recur on desks. First, double counting: applying the $\mathbb{P}\to\mathbb{Q}$ shift to a PD that was *already* backed out of spreads, so the premium is charged twice and every bond looks rich. Tag every PD field with its measure in the schema, not in a comment. Second, sign confusion in the reverse direction: going from a CDS-implied hazard to a $\mathbb{P}$-PD for a loss forecast requires *subtracting* the premium, and the premium is not observable, so the honest output is a range. Where the 2026 desk departs from the textbook shift: the CAPM diffusion premium is too small to explain investment-grade spreads, as the next paragraph explains, so a desk that uses only this adjustment will think IG credit is persistently cheap and will be persistently wrong about why.

### 6.3.3 The credit spread puzzle, and why the premium has a jump in it

Calibrate a diffusion structural model to historical default rates and ask what spread it implies for a BBB bond. For two decades the answer was "much less than the market spread," which became known as the credit spread puzzle. Feldhütter and Schaefer (2018), *The Myth of the Credit Spread Puzzle* (Review of Financial Studies 31(8)), argued that once you calibrate Black–Cox carefully to a long default history, it fits investment-grade spreads and actually *under*-prices high yield, partly because of illiquidity. Bai, Goldstein, and Yang (2020), *Is the Credit Spread Puzzle a Myth?* (Journal of Financial Economics 137(2)), reversed the conclusion when calibrating to market rather than book debt values, rejected geometric Brownian motion for asset value, and found that a large jump-risk premium is needed: the puzzle is real, and it lives in investment grade. The desk takeaway does not depend on who wins. The $\mathbb{Q}/\mathbb{P}$ gap has a diffusive part, which the formula above captures, and a jump part, which it does not. The jump part is the premium for owning the Tuesday on which a BBB name announces an accounting restatement. It is paid most generously in the names where it looks least necessary.

## 6.4 KMV and Distance to Default: The Inverse Problem

### 6.4.1 Desk framing: two equations, two unknowns, one deadline

Merton needs $V_0$ and $\sigma_V$. Neither is on a screen. What is on a screen is the stock price, from which the desk computes market capitalization $E_0$ and realized or implied equity volatility $\sigma_E$. The KMV insight (Vasicek and Kealhofer, commercialized by KMV and later Moody's) is to treat the Merton equity formula and the Itô volatility link as two equations in the two unknowns, solve them for each firm every day, and then throw away the Gaussian part of the model at the last step.

Theo asked ROBO to "compute distance to default." ROBO returned 1,420 miles: approximately the great-circle distance from the desk in Manhattan to Houston, seat of the Southern District of Texas bankruptcy court. It was not a bad guess about where the firm was headed. The precise spec gives units: *distance to default is measured in standard deviations of the log asset value at a one-year horizon.*

### 6.4.2 The solver

The system is

$$
g_1(V_0,\sigma_V)=V_0N(d_1)-Fe^{-rT}N(d_2)-E_0=0,\qquad g_2(V_0,\sigma_V)=N(d_1)\,\sigma_VV_0-\sigma_EE_0=0.
$$

Solve on log-parameters $z=(\ln V_0,\ln\sigma_V)$ so that positivity is automatic. The Jacobian uses three Black–Scholes partials: $\partial E/\partial V=N(d_1)$, vega $\partial E/\partial\sigma_V=V\phi(d_1)\sqrt T$, and $\partial d_1/\partial\sigma_V=-d_2/\sigma_V$, where $\phi$ is the standard normal density. With $\partial/\partial z_1=V\,\partial/\partial V$ and $\partial/\partial z_2=\sigma_V\,\partial/\partial\sigma_V$,

$$
J=\begin{pmatrix} VN(d_1) & \sigma_VV\phi(d_1)\sqrt T\\[4pt] \sigma_VVN(d_1)+V\phi(d_1)/\sqrt T & \sigma_VV\big[N(d_1)-\phi(d_1)\,d_2\big]\end{pmatrix}.
$$

A good starting point is $V_0^{(0)}=E_0+Fe^{-rT}$ and $\sigma_V^{(0)}=\sigma_EE_0/V_0^{(0)}$, the "equity plus book debt" guess. Newton converges in a handful of steps for ordinary firms.

The **Vasicek–Kealhofer (VK) iteration** avoids trusting a single $\sigma_E$, which is nonstationary whenever leverage changes. Take about three years (156 weeks) of equity values $E_t$. Guess $\sigma_V$. For each week, invert the call formula $E_t=C(V_t;\sigma_V)$ for $V_t$. Compute the weekly log asset returns, annualize their standard deviation to get a new $\sigma_V$, and repeat until it stops moving. Bohn and Stein describe the key step:

> **[SOURCE EXTRACTION]** *Bohn_Stein_Active_Credit_Portfolio_Management p.169:* "We then run the equity value equation backwards to determine an implied asset value."
>
> **Annotation.** "Run the equation backwards" is the whole trick, and it is cheap because the call price is strictly increasing and convex in $V$, so Newton's method from the right of the root converges monotonically and can be vectorized across all 156 weeks at once (§6.11). The VK loop then extracts $\sigma_V$ from a *time series* of implied asset values rather than from today's equity volatility, which matters because, as Bohn and Stein note on p.136, "a firm can have stationary asset volatility and still have nonstationary equity volatility as the firm changes its leverage over time." A leveraged recapitalization doubles equity vol overnight without changing the business. Where the 2026 desk departs: the 156-week window is too slow for a name in an active liability-management process, where the capital structure itself changes month to month. Desks recompute $F$ at every 8-K and use implied equity vol from listed options, when they exist, as a faster input (Chapter 23).

### 6.4.3 The default point and the empirical mapping

KMV does not set the default point to total face value. The convention (Crosbie and Bohn 2003, *Modeling Default Risk*, Moody's KMV) is

$$
X=\text{STD}+\tfrac12\,\text{LTD},
$$

short-term debt plus half of long-term debt, after removing items such as deferred taxes and minority interest and adding material off-balance-sheet liabilities. Bohn and Stein are explicit that "large levels of off-balance-sheet liabilities can make a difference and should be included in the DD calculation" (p.159), a sentence that will reappear, with feeling, in the First Brands case of §6.9. The reported distance to default is the simplified one-year version

$$
DD^{\text{KMV}}=\frac{V_0-X}{V_0\,\sigma_V},
$$

which for $V_0$ near $X$ is close to $\ln(V_0/X)/\sigma_V$, the Merton DD with the drift dropped (drift matters little at one year; volatility matters a lot).

Then comes the step that makes KMV a commercial product rather than a homework exercise: the DD is *not* pushed through $N(-\cdot)$. It is mapped to an Expected Default Frequency (EDF) through an empirical, monotone table estimated from historical defaults, sorted into cohorts by DD.

> **[SOURCE EXTRACTION]** *Bohn_Stein_Active_Credit_Portfolio_Management p.160:* "Empirical research, however, found that nearly 60 percent of its sample of over 25,000 firms have DDs that are 4 or greater. Recall that under the normal distribution, a DD of 4 is nearly equal to zero."
>
> **Annotation.** Under the normal, $N(-4)\approx3\times10^{-5}$, so a Gaussian mapping would assign effectively zero default probability to most of the corporate universe, which then defaults at a few basis points a year anyway. The fix is an empirical mapping, and Bohn and Stein are blunt about the data required: "At a bare minimum, a sample (ideally unbiased) of 400 defaults in a range of credit qualities is needed," with "at least 1,000 defaults" recommended (p.161). A desk building its own DD-to-PD table should fit an isotonic regression on half-sigma DD buckets with that many events or more, and should never let ROBO extrapolate the Gaussian tail beyond the last bucket. The deeper point, which Bharath and Shumway made empirically, is that DD is mostly a *ranking* variable. The structure of the formula (leverage scaled by volatility) carries the information; the probability scale comes from data.

Bharath and Shumway (2008), *Forecasting Default with the Merton Distance to Default Model* (Review of Financial Studies 21(3)), showed that a "naive" DD that skips the solver entirely forecasts default about as well as the iterated one. Their naive asset volatility is a weighted average of equity volatility and a debt volatility proxy:

$$
\sigma_V^{\text{naive}}=\frac{E_0}{E_0+F}\,\sigma_E+\frac{F}{E_0+F}\big(0.05+0.25\,\sigma_E\big),
$$

with $V_0\approx E_0+F$ and the past equity return standing in for $\mu$. The lesson is not that solvers are useless. It is that most of the signal is in the *functional form*, and a solver that fails on 3% of the universe is worse than a naive formula that never fails, unless the failures are flagged and filled.

> **Ways This Blows Up.** *The KMV solver in distress.* When $E_0\ll F$, $N(d_1)\to0$, the second row of the Jacobian collapses, and Newton wanders off to $\sigma_V=4$ or $V_0<E_0$. Guards: bound $\sigma_V\in[0.01,3]$, require $V_0\ge E_0$, check that the residuals are actually small rather than trusting the solver's exit code, and fall back to the naive DD with a flag when any guard trips. Second failure: stale equity. A stock that trades by appointment (post-reorg equity, a delisted name on the pink sheets) has a realized $\sigma_E$ that is mostly bid-ask bounce. Third: the default point is wrong for financials, whose "debt" is deposits and whose assets are not lognormal at all, which is the next case.

### 6.4.4 Case Study: Silicon Valley Bank, March 2023, and why banks break Merton

**The facts (approx.; secondary sources; confirm against FDIC and Federal Reserve reports before trading on them).** Silicon Valley Bank reported about \$209 billion of assets at December 31, 2022, funded largely by deposits, of which roughly 86–89% were uninsured. It held a held-to-maturity (HTM) securities portfolio of about \$91.3 billion carrying more than \$15 billion of unrealized losses, roughly the size of its book equity (approx.). On March 8, 2023 it announced that it had sold more than \$21 billion of available-for-sale securities at a loss of about \$1.8 billion and planned a \$2.25 billion capital raise. On March 9 depositors withdrew about \$42 billion. On March 10 the bank was closed and the FDIC appointed receiver.

**What the structural model saw.** An equity-driven, Merton-type vendor PD flagged the bank well before the run: S&P Global Market Intelligence reported that its Market Signal PD for SVB first jumped in September 2022, from about 1.1% to 2.5% in ten days, and peaked at about 6% on December 6, 2022, roughly five times the US regional-bank median of 1.27% (as reported by the vendor in a blog post; figures not independently verified this edition). Equity fell, equity volatility rose, DD fell. The model fired.

**What the structural model could not see.** Nagel and Purnanandam (2020), *Banks' Risk Dynamics and Distance to Default* (Review of Financial Studies 33(6); NBER working paper w25807), explain why a bank is not a Merton firm. A bank's assets are themselves loans and bonds, which are short puts on *borrowers'* assets. So bank asset value is a concave function of the economy, its volatility rises as its value falls, and bank equity is a mezzanine claim on a pool of short puts, not a call on a lognormal asset. A constant-$\sigma_V$ Merton model calibrated in good times understates bank default risk precisely when it is building. SVB adds two features the model has no slot for: an HTM book carried at amortized cost (the accounting $V$ was a mark-to-model asset in a mark-to-market model), and a deposit base that could leave in a day. The March 9 run was a jump in $F$'s *maturity*, not a diffusion in $V$: \$42 billion of demand deposits became due at once.

**How the desk would have flagged and traded it.** Three signals were available from public data. (1) DD momentum: a falling DD over September to December 2022, at a time when the bank's senior unsecured bonds were not repricing by a comparable amount (we lack verified bond marks, so treat this as the qualitative pattern the signal looks for). (2) A financials-specific adjustment: replace lognormal $V$ with a concave, state-dependent volatility, as Nagel and Purnanandam suggest, which lowers DD further for a bank with a long-duration securities book in a rising-rate year. (3) A jump overlay: uninsured deposit share as a run-intensity covariate, treated as a jump to default, not a diffusion. The trade was underweight the bank's senior unsecured debt, or long protection where it traded, sized as a jump-to-default position rather than a spread-duration one (Chapter 18). Chapter 23 revisits SVB through the equity-volatility surface.

> **Ways This Blows Up.** *DD is not a rating.* A DD of 4 for a bank and a DD of 4 for an industrial are not the same distance. The industrial's asset volatility is measured on a convex claim's denominator; the bank's is measured on a pool of short puts whose volatility is lowest right before it explodes. Desks that pool financials and non-financials in one DD-to-PD table are averaging a ruler and a rubber band.

## 6.5 Black–Cox: First Passage and Covenant Barriers

### 6.5.1 Desk framing: the covenant you spent ninety hours modeling

Merton lets the firm default only at $T$. Bohn and Stein are polite about it: "This case is not realistic as a firm will typically default at whatever time its market asset value falls through its default barrier" (p.151). Black and Cox (1976) fixed it by adding a barrier that can be hit at any time, and they gave it a name every RSSG banker will recognize.

> **[SOURCE EXTRACTION]** *Schmid_Credit_Risk_Pricing_Models p.121:* "Black & Cox (1976) introduce so called safety covenants which provide the bondholders the right to force the firm into bankruptcy as soon as the firm value hits some deterministic time-dependent threshold."
>
> **Annotation.** A safety covenant is a maintenance covenant, and the 1976 paper is the first formal model of the thing Theo spent his analyst years computing headroom against. The insight is that a covenant converts the bondholders' European short put into a *barrier* option: lenders get control as soon as value crosses the line, not when the debt matures. What the 2026 desk must add: Black and Cox assumed the covenant is exercised mechanically. In practice a breach starts a negotiation (waiver fee, margin step-up, amend-and-extend), so a barrier crossing is a *repricing option* held by the lenders, not a default. And since the cov-lite wave, most institutional term loans carry no maintenance covenant at all. A maintenance covenant is a Black–Cox barrier. A cov-lite loan is a Black–Cox barrier that was removed years ago, and nobody told the model.

Kaz, reading a revolver term sheet for the first time, asks whether a "springing lien" is seasonal. Theo explains that it springs into existence when a trigger is hit, a downgrade for the lien or, for the covenant cousin, revolver utilization above some threshold such as 35%. Kaz thinks about it. "So it's a barrier multiplied by a Heaviside function of utilization." That is exactly right, and it is the section's point: a springing covenant is a barrier that switches on only when the firm is already drawing on its liquidity, which is to say only when it is already in trouble.

### 6.5.2 The first-passage probability

Let the barrier grow at a deterministic rate $g$ toward $K$ at $T$: $K_t=Ke^{-g(T-t)}$. (We use $g$ for the barrier growth rate because $\gamma$ is reserved for risk aversion.) Default is the first time assets touch the barrier, $\tau=\inf\{t\ge0:V_t\le K_t\}$. Work in log distance to the barrier, $X_t=\ln(V_t/K_t)$, which by §6.1 is a Brownian motion with drift:

$$
dX_t=m\,dt+\sigma_V\,dW_t,\qquad m=\mu-\tfrac12\sigma_V^2-g,\qquad x_0=\ln\frac{V_0}{K_0}>0.
$$

Under $\mathbb{Q}$, replace $\mu$ by $r-q$, where $q$ is the payout rate. For driftless Brownian motion the reflection principle says every path that touches 0 and ends above it has a mirror-image path that ends below it, so $\mathbb{P}(\min_{s\le T}X_s\le0)=2\,\mathbb{P}(X_T\le0)$. With drift, the mirror path is reweighted by the Girsanov density, and the first-passage probability is

$$
\mathbb{P}(\tau\le T)=N\!\Big(\frac{-x_0-mT}{\sigma_V\sqrt T}\Big)+e^{-2mx_0/\sigma_V^2}\,N\!\Big(\frac{-x_0+mT}{\sigma_V\sqrt T}\Big).
$$

Three checks make this formula trustworthy. First, the first term alone is $\mathbb{P}(X_T\le0)$, the probability of being below the barrier at $T$; with $g=0$ and $K=F$ it is the Merton PD $N(-DD)$, and the second term counts the paths that crossed and came back. Second, with $m=0$ both terms equal $N(-x_0/\sigma_V\sqrt T)$ and the PD is exactly twice the Merton number (the "$pd_a=2pd$" line in Bohn and Stein, p.151). Third, as $T\to\infty$ with $m>0$ the first term vanishes and the second tends to $e^{-2mx_0/\sigma_V^2}<1$: a firm with positive drift has a positive probability of never defaulting, while for $m\le0$ default is certain eventually, which is what ROBO meant.

Valuation follows the same machinery. Equity is a down-and-out call on $V$; debt is the riskless bond minus a put plus a rebate paid when the barrier is hit (Bohn and Stein give the boundary conditions on p.152). The formulas are longer than Merton's and add nothing conceptually beyond the passage probability, so the reference implementation in §6.11 prices the PD and leaves the claim values to the exercises.

### 6.5.3 Covenants, cov-lite, and uptiers as barrier mechanics

**A maintenance covenant is a barrier in EBITDA space.** A total leverage test $\text{Debt}/\text{EBITDA}\le c$ becomes a barrier on value once you write $V\approx m_{\text{EV}}\cdot\text{EBITDA}$ for an enterprise-value multiple $m_{\text{EV}}$:

$$
\frac{\text{Debt}}{\text{EBITDA}}\le c\quad\Longleftrightarrow\quad V\ge K\equiv\frac{m_{\text{EV}}}{c}\,\text{Debt}.
$$

*Example (illustrative).* \$600mm of debt, \$110mm of EBITDA (5.45x), a 6.0x covenant, and an 8x multiple give $V=880$, $K=800$, and $x_0=\ln1.1\approx0.095$. With $\sigma_V=25\%$ and roughly zero drift, the one-year passage probability is about $2N(-0.38)\approx70\%$. A tight maintenance covenant is hit most years, and most hits end in an amendment fee rather than a default, which is why lenders fought to keep them: the barrier is an option to reprice.

**Cov-lite deletes the barrier.** With no maintenance test, the only barriers left are payment dates and maturity: the model reverts to a discretely monitored, Geske-style compound option in which default happens only when a coupon or a maturity cannot be paid or refinanced. Passage probabilities fall, recoveries fall further (by the time a cov-lite borrower misses a coupon, value is far below the old barrier), and the lender's repricing option is gone.

**An uptier moves the barrier for someone else.** In a non-pro-rata uptier, a majority group exchanges into new super-priority debt $F^{+}$ that ranks ahead of the left-behind lenders. The asset process $V_t$ does not change. But the left-behind lenders' payoff becomes $\min\big(\max(V_T-F^{+},0),F\big)$: their effective strike rises from $F$ to $F+F^{+}$ and their recovery in default falls. The participating lenders bought a lower strike with the left-behind lenders' collateral. That is the barrier math of the LMT era, and Chapter 13 turns it into a game.

### 6.5.4 Monte Carlo and the Brownian bridge

Simulating first passage on a grid of $n$ steps misses every crossing that happens between grid points and comes back. The bias is downward and large: on a monthly grid, a material fraction of barrier hits never show up. The fix is exact. Conditional on two consecutive log values $x_i$ and $x_{i+1}$, both above a log barrier $b$, the probability that the path touched $b$ in between is

$$
p_i=\exp\!\Big(-\frac{2(x_i-b)(x_{i+1}-b)}{\sigma_V^2\,\Delta t}\Big),
$$

and this holds for Brownian motion with *any* constant drift, because conditioning on both endpoints removes the drift. Draw $U_i\sim\text{Unif}(0,1)$ and record a hit if $U_i<p_i$ (Glasserman 2004, *Monte Carlo Methods in Financial Engineering*). The bridge-corrected simulation is unbiased on a coarse grid, which §6.11 checks against the closed form.

Empirically, Feldhütter and Schaefer (2018) found that Black–Cox calibrated to long-run default rates prices investment-grade spreads well, while Bai, Goldstein, and Yang (2020) dispute it (§6.3.3). The desk does not need to adjudicate. It needs the barrier in the right place, which in 2026 is a harder question than the math.

> **Trend Watch.** *Default is now a negotiation (2020–2026).* The barrier in a structural model is supposed to be a contractual fact. In the liability-management era it became a negotiated one. **(1) Share of defaults.** S&P Global Ratings reported in February 2025 that distressed exchanges made up about two-thirds of US speculative-grade defaults in Q4 2024 and that the distressed-exchange default rate ran at about 3.2% through end-2024 against about 2% for all other default types combined (approx.; S&P Global Ratings, February 20, 2025, as summarized; not independently verified this edition). A law-firm survey citing Oaktree's Q4 2024 commentary put the share of corporate defaults occurring through liability management exercises at "over 50%" (Quinn Emanuel, *Creditor-on-Creditor Violence*, January 2026). **(2) The courts.** On December 31, 2024, the Fifth Circuit held in *In re Serta Simmons Bedding* (125 F.4th 555) that Serta's 2020 uptier was not an "open market purchase" under its credit agreement; the same day, the New York Appellate Division, First Department, upheld the Mitel uptier in *Ocean Trails CLO VII v. MLN Topco* (Quinn Emanuel, January 2026). The location of the barrier now depends on a sentence in Section 2 of a credit agreement and on which court reads it. **(3) The level.** Moody's global speculative-grade trailing-twelve-month default rate was 4.3% in May 2026, up from 4.1% in December 2025, against a historical average of 4.2%; the US rate was 5.0%, with Moody's baseline forecasting declines to 3.1% globally and 3.5% in the US by December 2026 (First Trust, *Factoid*, June 22, 2026, citing Moody's). A year earlier UBS Asset Management had projected a 4.8% default rate for USD high yield in 2025, or 3.1% excluding two large distressed names (UBS AM, *2025 Fixed Income Default Study*, January 17, 2025). What it means for the desk: model "default" as a categorical event (payment default, bankruptcy, distressed exchange) with different recoveries and a re-default hazard after an exchange (Chapter 5, §5.6), and treat the barrier as a random variable whose distribution depends on documentation quality and lender cohesion. A structural model with a fixed barrier is calibrated to a world that ended in 2020.

> **Docket Diary.** *Where is the barrier?* **June 2020:** Serta Simmons completes a non-pro-rata uptier with a majority lender group, issuing new super-priority debt and leaving the minority behind. **January 2023:** Serta files for Chapter 11 in the Southern District of Texas. **2023:** the bankruptcy court upholds the uptier. **December 31, 2024:** the Fifth Circuit reverses, holding the exchange was not an "open market purchase" (125 F.4th 555). The Ad Hoc Group, represented by counsel, issues a statement in unison: "The barrier is wherever 50.1% of the lenders say it is, subject to appeal." Mags adds that "open market purchase" has now cost more in legal fees than most of the bonds she has ever owned. Kaz asks whether the Fifth Circuit's ruling is a reflection principle. It is not, but it did reflect the path.

### Deep-Dive Resource Graph

- **Podcasts:** Bloomberg *Odd Lots* episodes on liability management exercises and creditor-on-creditor violence (titles to be confirmed before linking).
- **Practitioner Writing:** Quinn Emanuel, *Creditor-on-Creditor Violence: How Liability Management Exercises Became the New Bankruptcy* (January 2026), https://www.quinnemanuel.com/the-firm/publications/creditor-on-creditor-violence-how-liability-management-exercises-became-the-new-bankruptcy/ ; UBS Asset Management, *2025 Fixed Income Default Study* (January 2025), https://www.ubs.com/global/en/assetmanagement/insights/asset-class-perspectives/fixed-income/articles/2025-fixed-income-default-study.html ; First Trust, *Factoid* (June 22, 2026), https://www.ftportfolios.com/blogs/InvestBlog/2026/6/22/factoid---monday,-june-22,-2026 .
- **Academic Papers:** Black and Cox (1976), *Valuing Corporate Securities: Some Effects of Bond Indenture Provisions*, Journal of Finance 31(2); Feldhütter and Schaefer (2018), *The Myth of the Credit Spread Puzzle*, Review of Financial Studies, https://lbsresearch.london.edu/id/eprint/953 ; Bai, Goldstein, and Yang (2020), *Is the Credit Spread Puzzle a Myth?*, Journal of Financial Economics, https://ideas.repec.org/a/eee/jfinec/v137y2020i2p297-319.html ; Nagel and Purnanandam (2020), *Banks' Risk Dynamics and Distance to Default*, https://www.nber.org/papers/w25807 ; Bharath and Shumway (2008), *Forecasting Default with the Merton Distance to Default Model*, Review of Financial Studies; Crosbie and Bohn (2003), *Modeling Default Risk*, Moody's KMV; Glasserman (2004), *Monte Carlo Methods in Financial Engineering*.
- **Data & Code:** SEC EDGAR for 10-K/10-Q debt schedules and 8-Ks announcing exchanges, https://www.sec.gov/edgar ; the `solve_kmv`, `kmv_iterate`, `black_cox_pd`, and `black_cox_mc` reference implementations in §6.11.

## 6.6 Reduced Form I: Cox Processes, Jarrow–Turnbull, Duffie–Singleton, and Three Recoveries

### 6.6.1 Desk framing: default as a surprise with a rate

Structural models explain *why* a firm defaults and then struggle to make it happen on time. Reduced-form models give up on why. Default is the first jump of a counting process whose arrival rate $\lambda_t$ you read off market prices, and the short end works by construction because a jump can arrive tomorrow. Mags approves, grudgingly. "Back in my day we priced bonds by phone and by grudge. The grudge was the intensity. You just didn't write it down."

> **[SOURCE EXTRACTION]** *Bohn_Stein_Active_Credit_Portfolio_Management p.328:* "The key assumption of reduced-form models is that the intensity process implies a distribution for the time to default. Said another way, all firms are assumed to default eventually and the riskier ones default earlier."
>
> **Annotation.** "All firms default eventually" is ROBO's 100% from the cold open, stated as a modeling axiom. It is harmless for pricing, because a 30-year survival probability of 20% and one of 25% differ by little in present value, and it is the reason reduced-form models are the language of CDS desks: they price the *timing* of default directly. What they give up, as Schmid puts it below, is any link to the balance sheet. The 2026 desk runs both: intensities for pricing and hedging, structural signals for ranking and for telling it when the intensity is about to move (§6.9).

### 6.6.2 The Cox construction and the zero-recovery bond

Let $\lambda_t\ge0$ be adapted to a filtration generated by economic factors, and let $\Theta\sim\text{Exp}(1)$ be independent of those factors. Define default as the moment the accumulated hazard exhausts the exponential clock:

$$
\tau=\inf\Big\{t:\int_0^t\lambda_s\,ds\ge\Theta\Big\}.
$$

This is a Cox, or doubly stochastic Poisson, process (Schmid p.71 gives the construction). Conditional on the factor path, $\mathbb{Q}(\tau>T\mid\text{factors})=\mathbb{Q}(\Theta>\int_0^T\lambda_s ds)=e^{-\int_0^T\lambda_sds}$, so by the tower property

$$
S(t,T)=\mathbb{E}^{\mathbb{Q}}\Big[e^{-\int_t^T\lambda_u\,du}\,\Big|\,\mathcal{F}_t\Big],
$$

on $\{\tau>t\}$. The same conditioning prices a zero-recovery defaultable bond (Lando 1998):

$$
P^{d,0}(t,T)=\mathbb{E}^{\mathbb{Q}}\Big[e^{-\int_t^Tr_u\,du}\,\mathbf 1_{\{\tau>T\}}\,\Big|\,\mathcal{F}_t\Big]=\mathbb{E}^{\mathbb{Q}}\Big[e^{-\int_t^T(r_u+\lambda_u)\,du}\,\Big|\,\mathcal{F}_t\Big].
$$

> **[SOURCE EXTRACTION]** *Schmid_Credit_Risk_Pricing_Models p.129:* "From a technical point of view, pricing of defaultable discount bonds is the same as pricing of non-defaultable discount bonds."
>
> **Annotation.** Replace $r$ by $r+\lambda$ and every term-structure tool you own (affine models, trees, the Veronesi toolkit) prices credit. That is the engineering win of reduced form, and it is why the CDS bootstrap in §6.8 is a rates bootstrap with one extra curve. The catch Schmid flags a page earlier is the price of that convenience: reduced-form models capture short spreads "more realistically," but "their main draw-back is the missing link between firm value and corporate default" (p.128). On a 2026 desk that drawback is a feature request: the hybrid of §6.9 puts the link back by making $\lambda$ a function of distance to default.

### 6.6.3 Three recovery conventions, which are three numeraires

What the bondholder receives at $\tau$ decides the pricing formula. Write $L=1-R$.

**Recovery of market value (RMV; Duffie and Singleton 1999).** At default the holder receives a fraction $R$ of the bond's pre-default market value. Then the defaultable bond is a riskless bond discounted at an adjusted short rate,

$$
P^{d}(t,T)=\mathbb{E}^{\mathbb{Q}}\Big[e^{-\int_t^T(r_u+\lambda_uL_u)\,du}\,\Big|\,\mathcal{F}_t\Big],\qquad s_t=\lambda^{\mathbb{Q}}_tL_t,
$$

so the instantaneous spread is intensity times loss. Bohn and Stein describe this version of the model as one that "models the instantaneous, risk-neutral expected rate of loss of market value, which is a function of default intensity and instantaneous LGD at time t resulting from default" (Bohn_Stein_Active_Credit_Portfolio_Management p.348).

**Recovery of face value (RFV, the CDS and bankruptcy convention).** The holder receives $R$ times par at $\tau$. With $r$ independent of $\lambda$ and $P(t,u)$ the riskless discount factor,

$$
P^{d}(t,T)=P^{d,0}(t,T)+R\int_t^TP(t,u)\big(-\partial_uS(t,u)\big)\,du.
$$

**Recovery of Treasury (RT; Jarrow and Turnbull 1995).** The holder receives $R$ riskless zeros of the same maturity, so under independence $P^{d}(t,T)=P(t,T)\big[R+(1-R)S(t,T)\big]$. Jarrow and Turnbull's 1995 model is the constant-$\lambda$ special case.

> **Desk Myth vs. Desk Reality.** *Myth:* "40% recovery is 40% recovery." *Reality:* it depends on the numeraire. A bond trading at 60 the day before default that recovers 40 of par has an RFV recovery of 40% and an RMV recovery of $40/60\approx67\%$. Plug an RFV quote into an RMV formula and you understate loss by a third. Schmid makes the general point: "Different recovery models can be transformed into each other. Basically, the value of the defaultable security at default is expressed using different numeraires" (Schmid_Credit_Risk_Pricing_Models p.95). Store the convention as an enum field next to every recovery number.

The **Duffie–Lando bridge** (2001) ties the two families together. If investors observe asset value only through noisy accounting reports, a first-passage structural model *acquires* an intensity: default remains a barrier crossing in the firm's true value, but from the investor's filtration it arrives as a surprise. In their words, "with imperfect information, however, yield spreads are strictly positive at zero maturity because investors' are uncertain about the nearness of current assets to the trigger level" (p.634). This is the cleanest argument for using intensities at the short end and structural signals for the long end: they are the same model seen through different information sets.

## 6.7 Reduced Form II: CIR Intensities in Closed Form

Let the intensity follow a Cox–Ingersoll–Ross square-root diffusion under $\mathbb{Q}$:

$$
d\lambda_t=\kappa(\theta-\lambda_t)\,dt+\sigma_\lambda\sqrt{\lambda_t}\,dW_t,
$$

with mean-reversion speed $\kappa$, long-run level $\theta$, and intensity volatility $\sigma_\lambda$ (subscripted to keep it apart from $\sigma_V$). By Feynman–Kac, $S(t,\lambda)=\mathbb{E}^{\mathbb{Q}}[e^{-\int_t^T\lambda_udu}]$ solves

$$
S_t+\kappa(\theta-\lambda)S_\lambda+\tfrac12\sigma_\lambda^2\lambda S_{\lambda\lambda}-\lambda S=0,\qquad S(T,\lambda)=1.
$$

Try the affine ansatz $S=A(\tau)e^{-B(\tau)\lambda}$ with time to maturity $\tau=T-t$. Then $S_t=(-A'/A+B'\lambda)S$, $S_\lambda=-BS$, and $S_{\lambda\lambda}=B^2S$. Substituting and collecting the terms in $\lambda$ and the constant terms separately gives two Riccati ODEs:

$$
B'(\tau)=1-\kappa B-\tfrac12\sigma_\lambda^2B^2,\qquad \frac{A'(\tau)}{A(\tau)}=-\kappa\theta B(\tau),\qquad A(0)=1,\;B(0)=0.
$$

With $\eta=\sqrt{\kappa^2+2\sigma_\lambda^2}$ the solution is

$$
B(\tau)=\frac{2(e^{\eta\tau}-1)}{(\eta+\kappa)(e^{\eta\tau}-1)+2\eta},\qquad A(\tau)=\left[\frac{2\eta\,e^{(\kappa+\eta)\tau/2}}{(\eta+\kappa)(e^{\eta\tau}-1)+2\eta}\right]^{2\kappa\theta/\sigma_\lambda^2}.
$$

The **Feller condition** $2\kappa\theta\ge\sigma_\lambda^2$ keeps $\lambda_t$ strictly positive. Violate it and the hazard visits zero, at which point ROBO declares the issuer immortal. The transition law is a scaled noncentral chi-square (Veronesi p.597): given $\lambda_s$, $\lambda_{s+\Delta}=c\,Y$ with $c=\sigma_\lambda^2(1-e^{-\kappa\Delta})/(4\kappa)$ and $Y$ noncentral $\chi^2$ with $4\kappa\theta/\sigma_\lambda^2$ degrees of freedom and noncentrality $\lambda_se^{-\kappa\Delta}/c$, so paths can be simulated exactly with no discretization error.

> **[SOURCE EXTRACTION]** *Bohn_Stein_Active_Credit_Portfolio_Management p.341:* "The Cox, Ingersoll, and Ross (CIR) specification is quite popular among academics but is less widely used in practice."
>
> **Annotation.** Why practitioners hesitate: one CDS curve barely identifies $\kappa$ and $\theta$ separately (a fast reversion to a high level and a slow reversion to a low one can price the same five tenors), the square-root diffusion cannot produce the sudden jumps that distressed curves show, and the closed form invites overfitting. Where CIR earns its keep on a 2026 desk: anywhere you need *dynamics* rather than today's curve, such as scenario generation for a CVA or jump-to-default overlay, options on spreads, and stress tests. Fix $\kappa$ from a cross-sectional prior, fit $\theta$ and $\lambda_0$ to the curve, and report the sensitivity to $\kappa$. Bohn and Stein also warn that sign conventions for $A$ and $B$ differ across texts (Lando writes $\alpha,\beta$); test against a Monte Carlo before trusting any formula you copied, including this one.

> **Ways This Blows Up.** *Euler goes negative.* The naive Euler step $\lambda_{t+\Delta}=\lambda_t+\kappa(\theta-\lambda_t)\Delta+\sigma_\lambda\sqrt{\lambda_t\Delta}\,Z$ can push $\lambda$ below zero, and then $\sqrt{\lambda}$ is NaN and the simulation silently produces garbage. Use exact noncentral-$\chi^2$ sampling, or full truncation ($\sqrt{\max(\lambda,0)}$ in the diffusion and $\max(\lambda,0)$ in the drift and the integral), and count how many paths hit zero as a diagnostic.

## 6.8 Hazard Bootstrapping from CDS and the Credit Triangle

### 6.8.1 Desk framing: the 13-week model, industrialized

A CDS contract pays $(1-R)$ times notional at default in exchange for a running coupon $c$ until default or maturity. Since the 2009 standardization, North American single-name contracts trade with fixed coupons of 100 or 500 bp plus an upfront payment, and the ISDA CDS Standard Model converts between upfront and par spread. Mags remembers it differently: "Back in my day we quoted running spreads, confirmed by fax, and settled arguments over the recovery by lunch." She concedes the standard model is an improvement. "Now everyone is wrong in the same way, which is what a market is."

### 6.8.2 The two legs

Let $t_1<\dots<t_n=T$ be the quarterly premium dates with accrual fractions $\Delta_i$ (ACT/360 in production; we use year fractions in the reference code), $P(0,t)$ the riskless discount curve, and $S(t)$ the $\mathbb{Q}$ survival curve. The premium leg includes accrued premium on default, approximated by half a period:

$$
\text{PV}_{\text{prem}}=c\sum_{i=1}^n\Delta_iP(0,t_i)\Big[S(t_i)+\tfrac12\big(S(t_{i-1})-S(t_i)\big)\Big]\equiv c\cdot\text{RPV01}.
$$

The protection leg pays $1-R$ at default, computed on a fine grid $u_0<u_1<\dots$ with midpoint discounting:

$$
\text{PV}_{\text{prot}}=(1-R)\sum_jP\big(0,\tfrac{u_{j-1}+u_j}{2}\big)\big(S(u_{j-1})-S(u_j)\big).
$$

The par spread equates the legs, $s=\text{PV}_{\text{prot}}/\text{RPV01}$, and for a standard-coupon contract the upfront paid by the protection buyer is $(s-c)\cdot\text{RPV01}$ per unit notional.

### 6.8.3 The bootstrap and the credit triangle

Make $\lambda$ piecewise constant on the quote buckets: $\lambda(t)=\lambda_k$ for $t\in(T_{k-1},T_k]$, so $S(t)=\exp\!\big(-\sum_k\lambda_k\cdot|(T_{k-1},T_k]\cap(0,t]|\big)$. Solve for $\lambda_1$ so the $T_1$ quote reprices, then hold it fixed and solve for $\lambda_2$ from the $T_2$ quote, and so on, each step a one-dimensional root search (Brent's method). This is the procedure the ISDA model and MathWorks' `cdsbootstrap` implement, the latter documenting that "the survival probability is defined in terms of a piecewise constant hazard rate."

The credit triangle drops out when $\lambda$ is flat and the premium is paid continuously. Then $\text{PV}_{\text{prot}}=(1-R)\int_0^TP(0,t)\lambda S(t)\,dt$ and $\text{PV}_{\text{prem}}=s\int_0^TP(0,t)S(t)\,dt$. The integrands differ by the constant factor $\lambda$, so

$$
s=\lambda(1-R)\qquad\text{exactly, for any deterministic discount curve,}
$$

and approximately when coupons are paid quarterly in arrears (the discrete premium leg is worth slightly less, so the bootstrapped $\lambda$ comes out slightly below $s/(1-R)$; §6.11 measures the gap). A flat 300 bp curve with $R=40\%$ implies $\lambda\approx5\%$ a year. Run the same arithmetic on the ICE BofA CCC & Lower index OAS of 1,278 bp in mid-October 2026 (Chapter 5, Trend Watch, from FRED) and the risk-neutral hazard is about 21% a year.

Mags, on the triangle: "Forty percent recovery is a convention. In thirty years I have never been handed exactly forty." She is right, and it does not matter for the bootstrap: a CDS spread identifies only the product $\lambda^{\mathbb{Q}}(1-R)$, so the conventional $R$ is a quoting device for turning spreads into upfronts. It is not a forecast. If you change $R$ you change $\lambda$ in the opposite direction and reprice every quote identically. The hazard curve you hand the risk system inherits the convention, so ship $R$ with it.

> **Ways This Blows Up.** *Bootstrapping a distressed curve.* (1) *Negative hazards.* Distressed curves invert: 1-year protection costs more than 5-year because the market expects default soon or not at all. Steep enough inversion makes the forward hazard on a later bucket negative, which is an arbitrage in the model and a data error or a recovery-assumption error in practice; MathWorks warns about "non-monotone default probabilities (that is, negative hazard rates)." Flag the bucket, floor it only in a separate output, and never silently floor the curve you use to reprice. (2) *Points upfront treated as running spread.* A distressed name quoted at 35 points upfront plus 500 bp running is not a 500 bp credit. (3) *Day counts.* ACT/360 premium accrual against ACT/365 discounting is a few basis points of error that compounds across a book. (4) *Forgetting accrual on default,* which overstates the premium leg's value to the protection seller. (5) *The wrong recovery by seniority:* subordinated contracts conventionally use a lower recovery than senior ones; check the current standard assumptions for your region and tier rather than hard-coding them.

> **Trend Watch.** *Single-name CDS: episodic liquidity, central clearing, and a curve migration (2018–2026).* ISDA's May 2023 *Single-name CDS Market Update* reported quarterly single-name traded notional ranging between about \$405 billion and \$1.1 trillion over 2018 to Q1 2023, with a trough in Q4 2020 and a five-year peak of \$1.1 trillion in Q1 2023 as the bank failures drove hedging demand. Breadth shrank: the number of reference entities trading in a quarter fell from 854 in Q1 2018 to 719 in Q1 2023, and has since held in a narrow range of about 710 to 760 names (751 in Q4 2025; ISDA, July 2026); of 1,169 entities that traded at least once in five years, about 600 traded less than once a quarter, while 496 traded every quarter and accounted for more than 80% of activity. In Q1 2023, 51.2% of single-name notional and 87.4% of index notional reported in the US was centrally cleared; by 2025 the shares were 63.1% and 78.1% (ISDA, July 2026). BIS statistics put total CDS notional at \$8.5 trillion at end-December 2023, down from \$9.9 trillion six months earlier, with 65% centrally cleared (BIS, May 16, 2024), and credit derivatives at \$9.2 trillion at end-June 2024, down 9% year on year (BIS, November 21, 2024). Plumbing changed too: the ISDA CDS Standard Model, open-source C code administered by S&P Global Market Intelligence, announced in June 2026 that its standard rate curves were moving to a new S&P Global site, with the old site shutting after August 15, 2026 (cdsmodel.com). What it means for the desk: for most issuers, a full single-name CDS curve is a stale or synthetic object. Bootstrap where the curve trades, and elsewhere build $\lambda$ from bond spreads, index-implied intensities, or structural signals. Store the date of the last real trade next to every hazard curve, and check the curve source URL in your config before the next migration breaks it at 6 a.m.

### Deep-Dive Resource Graph

- **Podcasts:** ISDA's podcast series (an episode index exists at https://www.isda.org ; no credit-model-specific episode verified this session).
- **Practitioner Writing:** ISDA, *Single-name CDS Market Update* (May 2023), https://www.isda.org/a/0jLgE/Single-name-CDS-Market-Update.pdf ; BIS OTC derivatives statistics, https://www.bis.org/publ/otc_hy2405.htm and https://www.bis.org/publ/otc_hy2411.htm ; O'Kane and Turnbull (2003), *Valuation of Credit Default Swaps*, Lehman Brothers Quantitative Credit Research.
- **Academic Papers:** Jarrow and Turnbull (1995), *Pricing Derivatives on Financial Securities Subject to Credit Risk*, Journal of Finance 50(1); Duffie and Singleton (1999), *Modeling Term Structures of Defaultable Bonds*, Review of Financial Studies 12(4); Lando (1998), *On Cox Processes and Credit Risky Securities*, Review of Derivatives Research; Cox, Ingersoll, and Ross (1985), *A Theory of the Term Structure of Interest Rates*, Econometrica; O'Kane (2008), *Modelling Single-name and Multi-name Credit Derivatives*, Wiley; Lando (2004), *Credit Risk Modeling*, Princeton.
- **Data & Code:** ISDA CDS Standard Model, https://cdsmodel.com/ ; MathWorks `cdsbootstrap` documentation, https://www.mathworks.com/help/finance/cdsbootstrap.html ; *Arbitrage Opportunities in CDS Term Structure*, https://arxiv.org/pdf/1811.08038 ; BIS statistics portal, https://www.bis.org/statistics ; the `cds_legs` and `bootstrap_hazard` reference implementations in §6.11.

## 6.9 Hybrids: Structural Signals Inside Intensity Models

### 6.9.1 The two-stage fit

The desk does not have to choose. Bohn and Stein (p.354–355) sketch a two-stage hybrid. **Stage 1** fits a physical intensity $\lambda^{\mathbb{P}}_t$ to equity-based default probabilities through $1-\text{cpd}(t)=\exp(-\int_0^t\lambda^{\mathbb{P}}_s\,ds)$, where cpd is the cumulative PD term structure from the structural model. **Stage 2** fits a market price of default risk $\Pi_t$ so that $\lambda^{\mathbb{Q}}_t=\Pi_t\,\lambda^{\mathbb{P}}_t$ reprices the CDS or bond curve.

> **[SOURCE EXTRACTION]** *Bohn_Stein_Active_Credit_Portfolio_Management p.355:* "Berndt, Douglas, Duffie, Ferguson, and Schranz (2004) use EDF and CDS data to do exactly this sort of estimation."
>
> **Annotation.** The Berndt et al. template turns the ratio $\Pi_t=\lambda^{\mathbb{Q}}_t/\lambda^{\mathbb{P}}_t$ into a time series per issuer, and that series is the cleanest version of the systematic "value" signal: credit is cheap when the market charges a large multiple of the structural default rate *relative to that issuer's own history and its peers*. The 2026 desk adds two things the 2004 paper could not: daily structural PDs for thousands of issuers from vendors or in-house engines (Trend Watch, §6.2), and the discipline that the ratio is a signal only after factor exposures are stripped. A high $\Pi_t$ in a CCC name during a risk-off week is beta wearing a disguise. IDO or it didn't happen.

### 6.9.2 Equity leads credit

The second hybrid use is speed. Equity prices incorporate news faster than bonds, so changes in DD lead changes in spread.

> **[SOURCE EXTRACTION]** *Man_Quantitative_Credit_Alpha_Early_Mover_2022 p.31:* "the only spill-over to achieve meaningful statistical significance is equity Momentum, which generates a higher alpha than corporate bond Momentum itself."
>
> **Annotation.** A structural model is a principled way to turn equity momentum into a *credit* signal: the Merton hedge ratio $\partial B/\partial E$ tells you how much a given equity move should have moved the bond, so "DD momentum" (the change in DD over one to three months) measures the information the bond market has not yet priced. Chapter 10 builds it as a trend feature. The limit, as Dynkin and coauthors note, is that the Merton hedge ratio "ignores other important aspects of a firm's operations, such as cash flows and profitability" (Dynkin_Systematic_Investing_in_Credit p.88), which is the opening for Theo's thirteen-week liquidity runway as a covariate in the intensity: $\lambda_t=\exp(\beta_0+\beta_1DD_t+\beta_2\,\text{Runway}_t+\cdots)$.

### 6.9.3 Case Study: First Brands, 2025, a firm with no equity ticker

**The facts (secondary sources; confirm against the docket).** First Brands Group, a privately held auto-parts supplier, filed for Chapter 11 in September 2025 in the Southern District of Texas (Case No. 25-90399), listing liabilities in the \$10–50 billion range against assets in the \$1–10 billion range. Its financing relied heavily on off-balance-sheet receivables and supply-chain finance. After the filing, a supply-chain finance provider said roughly \$2.3 billion of funds could not be accounted for; reported exposures included more than \$500 million at a UBS O'Connor fund, about \$715 million of receivables exposure at a Jefferies-affiliated fund, and a \$1.75 billion exposure at a Norinchukin–Mitsui joint venture (as reported). Federal prosecutors alleged that receivables had been pledged more than once; indictments followed on January 29, 2026, and the case converted to Chapter 7 on September 1, 2026.

**The model lesson.** There was no stock price, so there was no $E_t$, no $\sigma_E$, and no DD. Worse, the part of the capital structure that mattered was not on the balance sheet at all, which is precisely Bohn and Stein's warning that "large levels of off-balance-sheet liabilities can make a difference and should be included in the DD calculation" (p.159). A default point built from reported debt would have been too low by an amount nobody outside the company knew. "The model had no input" is not a defense; it is a finding, and it should have been a flag.

**How the desk handles a firm with no equity.** Borrow $\sigma_V$ from listed peers and de-lever it. Fit an intensity to syndicated-loan marks where the loans trade. Treat opacity itself as a covariate: a large, rising share of receivables financing, factoring, and supplier finance relative to reported debt should *raise* $\lambda$, not leave it unchanged. And size such names as jump-to-default positions. Chapter 17 takes up private credit, where this is the normal case rather than the exception.

## 6.10 Case Study: Carvana 2022–23 and Hertz 2020–21, the Call Option That Would Not Expire

### 6.10.1 Carvana: a negotiated barrier move

**The facts.** Carvana's stock fell roughly 99% from its August 2021 peak (about \$370) to its December 2022 low (about \$3.70) (approx.), while its senior unsecured notes traded at deep discounts. On July 19, 2023, Carvana announced a transaction support agreement with holders of more than 90% (about \$5.2 billion) of its senior unsecured notes (SEC Form 8-K, Exhibit 99.1, July 19, 2023). The exchange, completed September 1, 2023 with 96.4% participation, swapped about \$5.52 billion of unsecured notes for about \$4.2 billion of new senior secured notes, plus a \$341 million cash tender for the 2025 notes, cutting total debt by more than \$1.2 billion and annual cash interest by more than \$430 million for two years, in part because the new notes allowed interest to be paid in kind in the early years (Form 10-Q, Q3 2023). Carvana's FY2023 10-K recorded an \$878 million gain on debt extinguishment. The equity then rallied hard through 2023–25 (approx.).

**The Merton reading.** In December 2022 a Merton DD on Carvana would have been near zero: equity a deep out-of-the-money call, debt mostly a short put. But Merton assumes $F$ and $T$ are fixed until maturity. The exchange changed both. Face value fell (a lower strike for equity), maturities extended (more time value for the call), and the old unsecured holders who participated moved up the priority ladder by taking secured paper at a discount to face. It was a *negotiated barrier move*: the call did not expire worthless because the people short the put agreed to restrike it. For the participating noteholders this was rational: a secured claim at 76% of face beat an unsecured claim on a firm heading toward the barrier.

### 6.10.2 Hertz: the hand that hit

**The facts.** Hertz filed for Chapter 11 on May 22, 2020. Its stock then rose from about \$0.59 to about \$5.50 in June 2020, roughly a 1,000% move. On June 11, 2020 the company sought to sell up to \$1 billion of new stock under a prospectus warning that the shares "could ultimately be worthless"; it sold about \$29 million before the SEC raised objections and the program stopped, and the stock was delisted in October 2020 (secondary sources). At emergence on June 30, 2021, old common stockholders received \$1.53 in cash per share, a pro rata share of 3% of the new common stock, and a choice of warrants (89,049,029 warrants with a \$13.80 strike, expiring June 30, 2051) or rights to buy new stock at \$10.00 per share as part of a \$1.6 billion offering, of which \$1.3 billion was subscribed (SEC Form S-1, October 2021). The fleet, Hertz's main asset, had risen in value as used-vehicle prices climbed through 2020–21 (approx.).

**The Merton reading.** Equity is a call on $V$. In June 2020 the call looked dead by every recovery analysis Theo's old shop would have run. Then $V$ moved: the asset was a fleet of cars, and used-car prices rose. The out-of-the-money call moved into the money while the company was still in court, so old equity was not wiped out. Merton's payoff diagram was right. What broke was the RSSG instinct that a bankruptcy filing means the strike has already been evaluated. In Chapter 11 it has not. The option keeps its time value until confirmation.

> **Poker Table.** Ines replays the hand. "Retail paid \$5.50 for a ticket that eventually paid \$1.53, plus 3% of the company, plus warrants. The pot odds were terrible. The hand still hit." She turns over the cards. "Don't confuse the two. Ninety-nine times out of a hundred, post-petition equity at a 1,000% rally is the worst bet at the table." Then the markout: who sold the stock to those buyers? The company itself, through an equity offering that said, in writing, that the stock could be worthless. "When the most informed seller at the table offers to sell you chips and tells you they might be fake, the hand history writes itself." That the buyers got lucky later does not change who knew more at the time.

### 6.10.3 How the desk would have flagged both

Three systematic signals were available from public data. **(1) DD momentum turning up while the CDS or bond curve stayed inverted**: equity says the distance is growing while credit still prices near-term default, which is the equity-leads-credit pattern of §6.9.2. **(2) Hedge-ratio breakdown**: when the empirical bond-to-equity sensitivity falls far below the Merton ratio, the capital structure is being renegotiated rather than diffused, and Dynkin's p.87 warning about analytical hedge ratios applies with force in the HY tail. **(3) Liability-management covariates**: a transaction support agreement, a cooperation agreement among holders, or new secured capacity under the indenture should shift the model from "barrier fixed" to "barrier negotiable," with a categorical outcome (exchange, bankruptcy, survival) instead of a binary one (Chapter 5, §5.6). The trade in Carvana's case was the capital-structure pair: long the unsecured notes that would be invited into the exchange, against equity or against the notes that would be left behind (Chapter 22).

### Deep-Dive Resource Graph

- **Podcasts:** Bloomberg *Odd Lots* episodes on post-bankruptcy equity rallies and on distressed exchanges (titles to be confirmed before linking).
- **Practitioner Writing:** Carvana, Form 8-K Exhibit 99.1 (July 19, 2023), https://www.sec.gov/Archives/edgar/data/1690820/000119312523189188/d537573dex991.htm ; Carvana, Form 10-Q for Q3 2023, https://www.sec.gov/Archives/edgar/data/1690820/000169082023000323/cvna-20230930.htm ; Hertz Global Holdings, Form S-1 (October 2021), https://www.sec.gov/Archives/edgar/data/1657853/000110465921126784/tm2128732-1_s1.htm .
- **Academic Papers:** Berndt, Douglas, Duffie, Ferguson, and Schranz (2004), on EDF-implied and CDS-implied default risk premia (title as cited in Bohn_Stein p.355); Schaefer and Strebulaev (2008), *Structural Models of Credit Risk Are Useful*, Journal of Financial Economics.
- **Data & Code:** SEC EDGAR, https://www.sec.gov/edgar ; CourtListener API for docket monitoring, https://www.courtlistener.com/help/api/ .

## 6.11 The Engine: One Module for Structural and Intensity Models

### Specification for AI Implementation

**What ROBO built from the vague version.** Theo's first spec said "estimate PDs from equity volatility." ROBO used one-day $\sigma_E$, unannualized, and reported a one-year PD of 0.00% for every issuer in the high-yield index. Mags asked whether it had been reading rating-agency outlooks. The precise spec below fixes units, measures, horizons, and failure behavior.

**The Spec You Hand the Robot.** Build `ch06_structural_intensity_engine`, numpy/scipy only, seeded with `rng = np.random.default_rng(42)`. Every volatility is annualized and decimal; every spread is decimal in code and basis points in output; every PD carries its measure ($\mathbb{P}$ or $\mathbb{Q}$) in the variable name; every recovery carries its convention (RFV unless stated). Functions must vectorize over issuers and tenors, raise on invalid inputs instead of returning NaN, and print a PASS/FAIL line for each sanity check below.

| Schema | Fields (type, unit) | Notes |
| :--- | :--- | :--- |
| `MertonInputs` | `V0` float \$mm; `F` float \$mm face; `r` float cont. comp.; `sigma_V` float annual; `T` float years; `mu` float or None | `mu` only for $\mathbb{P}$ PDs |
| `KMVInputs` | `E_series` ndarray `(n_weeks,)` \$mm market cap; `F` float default point \$mm; `r`; `T`=1.0 | $F = \text{STD} + \tfrac12\text{LTD}$ plus material off-balance-sheet items |
| `CDSQuotes` | `tenors` ndarray `(K,)` years; `spreads_bp` ndarray `(K,)`; `R`=0.4 RFV; `discount` callable $t\mapsto P(0,t)$, vectorized | quarterly premium, accrual on default |
| Batch convention | arrays shaped `(n_issuers,)` or `(n_issuers, n_tenors)` | broadcasting, no Python loops over issuers |

Sanity checks: **A** $E_0+B_0=V_0$ to $10^{-10}$; **B** Monte Carlo Merton debt within 3 SE; **C** Merton spread $\to0$ at $T=10^{-3}$; **D** KMV round trip to $10^{-6}$ and VK iteration recovers $\sigma_V$; **E** naive DD ranks like the solved DD; **F** bridge MC within 3 SE of the Black–Cox closed form and naive MC biased low; **G** $m=0$ doubles the terminal PD; **H** CIR closed form vs exact-sampling MC within 3 SE; **I** CDS bootstrap reprices every quote to $10^{-8}$; **J** credit triangle; **K** inverted curve trips the negative-hazard flag; **L** Merton short end near zero and hump-shaped.

The blocks below run in order in one interpreter.

```python
# Block 0: imports, seed, and the PASS/FAIL helper
import warnings
import numpy as np
from scipy.stats import norm, spearmanr
from scipy.optimize import fsolve, brentq

rng = np.random.default_rng(42)


def check(label, ok, detail=""):
    """Print PASS/FAIL and stop the run on failure."""
    print(f"[{'PASS' if ok else 'FAIL'}] {label}  {detail}")
    assert ok, label
```

Block 1 is Merton under $\mathbb{Q}$ for prices and $\mathbb{P}$ for PDs. The spread uses `log1p` on the put fraction so that tiny spreads do not vanish into rounding.

```python
# Block 1: Merton (1974)
def _d1d2(V0, F, r, sigma_V, T):
    V0, F, T = np.asarray(V0, float), np.asarray(F, float), np.asarray(T, float)
    sigma_V = np.clip(np.asarray(sigma_V, float), 1e-4, 5.0)
    if np.any(V0 <= 0) or np.any(F <= 0) or np.any(T <= 0):
        raise ValueError("V0, F and T must be strictly positive")
    srt = sigma_V * np.sqrt(T)
    d1 = (np.log(V0 / F) + (r + 0.5 * sigma_V**2) * T) / srt
    return d1, d1 - srt


def merton_prices(V0, F, r, sigma_V, T):
    """Q-measure Merton. Returns (E0, B0, spread, pd_Q); spread is decimal, continuously compounded."""
    d1, d2 = _d1d2(V0, F, r, sigma_V, T)
    T = np.asarray(T, float)
    disc_F = F * np.exp(-r * T)
    E0 = V0 * norm.cdf(d1) - disc_F * norm.cdf(d2)
    B0 = disc_F * norm.cdf(d2) + V0 * norm.cdf(-d1)
    put_frac = norm.cdf(-d2) - V0 * norm.cdf(-d1) / disc_F          # put / (F e^{-rT}), >= 0
    spread = -np.log1p(-np.maximum(put_frac, 0.0)) / T
    return E0, B0, spread, norm.cdf(-d2)


def merton_pd_P(V0, F, mu, sigma_V, T):
    """P-measure distance to default and PD at horizon T."""
    sigma_V = np.clip(np.asarray(sigma_V, float), 1e-4, 5.0)
    T = np.asarray(T, float)
    dd = (np.log(np.asarray(V0, float) / F) + (mu - 0.5 * sigma_V**2) * T) / (sigma_V * np.sqrt(T))
    return dd, norm.cdf(-dd)


V0, F, r, sV, T = 100.0, 80.0, 0.04, 0.25, 1.0
E0, B0, s1, pdQ = map(float, merton_prices(V0, F, r, sV, T))
dd_P, pd_P = map(float, merton_pd_P(V0, F, 0.08, sV, T))
print(f"E0={E0:.4f}  B0={B0:.4f}  s={1e4 * s1:.1f} bp  PD_Q={pdQ:.4f}  DD_P={dd_P:.3f}  PD_P={pd_P:.4f}")
check("A: E0 + B0 = V0", abs(E0 + B0 - V0) < 1e-10, f"err={abs(E0 + B0 - V0):.1e}")

n_half = 100_000
z = rng.standard_normal(n_half)
z = np.concatenate([z, -z])                                            # antithetic pairs
VT = V0 * np.exp((r - 0.5 * sV**2) * T + sV * np.sqrt(T) * z)
pay = np.exp(-r * T) * np.minimum(VT, F)
pair = 0.5 * (pay[:n_half] + pay[n_half:])
mc, se = pair.mean(), pair.std(ddof=1) / np.sqrt(n_half)
check("B: MC debt within 3 SE of closed form", abs(mc - B0) < 3 * se,
      f"MC={mc:.4f} CF={B0:.4f} SE={se:.4f}")

s_short = float(merton_prices(V0, F, r, sV, 1e-3)[2])
check("C: Merton short-end spread -> 0", abs(s_short) < 1e-8, f"s(0.001y)={s_short:.1e}")
```

Block 2 is KMV: the two-equation solver with the analytic Jacobian of §6.4.2, the vectorized equity inversion, the VK iteration, and the Bharath–Shumway naive DD.

```python
# Block 2: KMV inverse problem
def merton_equity_vol(V0, F, r, sigma_V, T):
    """Equity value and the Ito-implied equity volatility sigma_E = N(d1) sigma_V V0 / E0."""
    d1, _ = _d1d2(V0, F, r, sigma_V, T)
    E = merton_prices(V0, F, r, sigma_V, T)[0]
    return E, norm.cdf(d1) * np.asarray(sigma_V, float) * V0 / E


def solve_kmv(E0, sigma_E, F, r, T=1.0):
    """Solve E0 = C(V0, sigma_V) and sigma_E E0 = N(d1) sigma_V V0 on log-parameters."""
    if not (0.05 <= sigma_E <= 3.0):
        raise ValueError(f"sigma_E={sigma_E} outside [5%, 300%]: is it annualized?")
    sq, disc_F = np.sqrt(T), F * np.exp(-r * T)

    def resid(zz):
        V, s = np.exp(zz)
        d1, d2 = _d1d2(V, F, r, s, T)
        return np.array([(V * norm.cdf(d1) - disc_F * norm.cdf(d2)) / E0 - 1.0,
                         norm.cdf(d1) * s * V / (sigma_E * E0) - 1.0])

    def jac(zz):
        V, s = np.exp(zz)
        d1, d2 = _d1d2(V, F, r, s, T)
        Nd1, nd1 = norm.cdf(d1), norm.pdf(d1)
        return np.array([[V * Nd1 / E0, s * V * nd1 * sq / E0],
                         [(s * V * Nd1 + V * nd1 / sq) / (sigma_E * E0),
                          s * V * (Nd1 - nd1 * d2) / (sigma_E * E0)]])

    V_init = E0 + disc_F
    z0 = np.log([V_init, max(sigma_E * E0 / V_init, 0.01)])
    zz = fsolve(resid, z0, fprime=jac, xtol=1e-10)
    V, s = np.exp(zz)
    if np.max(np.abs(resid(zz))) > 1e-9 or not (0.01 <= s <= 3.0) or V < E0:
        raise RuntimeError(f"KMV solve failed: V={V:.4g}, sigma_V={s:.4g}; fall back to naive DD and flag")
    return float(V), float(s)


def invert_equity(E, F, r, sigma_V, T, tol=1e-12, max_iter=100):
    """Vectorized Newton for V with C(V) = E. C is increasing and convex in V, so Newton
    started right of the root (V = E + F e^{-rT}) converges monotonically."""
    E = np.asarray(E, float)
    disc_F = F * np.exp(-r * T)
    V = E + disc_F
    for _ in range(max_iter):
        d1, d2 = _d1d2(V, F, r, sigma_V, T)
        step = (V * norm.cdf(d1) - disc_F * norm.cdf(d2) - E) / np.maximum(norm.cdf(d1), 1e-12)
        V = V - step
        if np.max(np.abs(step) / V) < tol:
            return V
    raise RuntimeError("equity inversion did not converge")


def kmv_iterate(E_series, F, r, T=1.0, periods_per_year=52, tol=1e-6, max_iter=100):
    """Vasicek-Kealhofer iteration. Returns (implied asset path, sigma_V, iterations)."""
    E = np.asarray(E_series, float)
    sig_E = np.std(np.diff(np.log(E)), ddof=1) * np.sqrt(periods_per_year)
    sig = max(sig_E * E[-1] / (E[-1] + F * np.exp(-r * T)), 0.01)
    for it in range(1, max_iter + 1):
        V = invert_equity(E, F, r, sig, T)
        sig_new = np.std(np.diff(np.log(V)), ddof=1) * np.sqrt(periods_per_year)
        if abs(sig_new - sig) < tol:
            return V, float(sig_new), it
        sig = sig_new
    raise RuntimeError("VK iteration did not converge")


def naive_dd(E0, sigma_E, F, mu, T=1.0):
    """Bharath-Shumway (2008) naive distance to default (P-measure; mu = past equity return)."""
    w = E0 / (E0 + F)
    sig_V = w * sigma_E + (1.0 - w) * (0.05 + 0.25 * sigma_E)
    return (np.log((E0 + F) / F) + (mu - 0.5 * sig_V**2) * T) / (sig_V * np.sqrt(T))


E_true, sE_true = map(float, merton_equity_vol(V0, F, r, sV, T))
V_hat, sV_hat = solve_kmv(E_true, sE_true, F, r, T)
err_D = max(abs(V_hat / V0 - 1.0), abs(sV_hat / sV - 1.0))
check("D1: KMV round trip recovers (V0, sigma_V)", err_D < 1e-6,
      f"sigma_E={sE_true:.3f} -> V0={V_hat:.6f}, sigma_V={sV_hat:.6f}")

n_weeks, dt_w = 156, 1.0 / 52
steps = (0.08 - 0.5 * sV**2) * dt_w + sV * np.sqrt(dt_w) * rng.standard_normal(n_weeks - 1)
V_path = V0 * np.exp(np.concatenate([[0.0], np.cumsum(steps)]))
E_path = merton_prices(V_path, F, r, sV, T)[0]
_, sV_vk, n_it = kmv_iterate(E_path, F, r, T)
check("D2: VK iteration recovers sigma_V", abs(sV_vk - sV) < 0.05,
      f"sigma_V={sV_vk:.4f} after {n_it} iterations")

F_x = rng.uniform(10.0, 90.0, 200)
sV_x = rng.uniform(0.10, 0.50, 200)
E_x, sE_x = merton_equity_vol(V0, F_x, r, sV_x, T)
dd_true, _ = merton_pd_P(V0, F_x, r, sV_x, T)
rho_E, _ = spearmanr(dd_true, naive_dd(E_x, sE_x, F_x, r, T))
check("E: naive DD ranks like the solved DD", rho_E > 0.8, f"Spearman={rho_E:.3f}")
```

Block 3 is Black–Cox, with the second term of the passage formula computed in log space so that a large $e^{-2mx_0/\sigma_V^2}$ cannot multiply a tiny $N(\cdot)$ into `inf * 0`.

```python
# Block 3: Black-Cox first passage
def black_cox_pd(V0, K, g, mu, sigma_V, T):
    """First-passage PD by T for barrier K_t = K exp(-g (T - t)). Use mu = r - q under Q."""
    x0 = np.log(V0 / (K * np.exp(-g * T)))
    if np.any(x0 <= 0):
        raise ValueError("asset value is already at or below the barrier")
    m, srt = mu - 0.5 * sigma_V**2 - g, sigma_V * np.sqrt(T)
    second = np.exp(-2.0 * m * x0 / sigma_V**2 + norm.logcdf((-x0 + m * T) / srt))
    return norm.cdf((-x0 - m * T) / srt) + second


def black_cox_mc(V0, K, g, mu, sigma_V, T, n_paths=200_000, n_steps=12, bridge=True):
    """Monte Carlo on the log distance to the barrier, with optional Brownian-bridge correction."""
    dt = T / n_steps
    m = mu - 0.5 * sigma_V**2 - g
    x = np.full(n_paths, np.log(V0 / (K * np.exp(-g * T))))
    alive = np.ones(n_paths, dtype=bool)
    for _ in range(n_steps):                                    # the only Python loop: time steps
        x_new = x + m * dt + sigma_V * np.sqrt(dt) * rng.standard_normal(n_paths)
        hit = x_new <= 0.0
        if bridge:
            p_cross = np.exp(-2.0 * np.maximum(x, 0.0) * np.maximum(x_new, 0.0) / (sigma_V**2 * dt))
            hit |= rng.uniform(size=n_paths) < p_cross
        alive &= ~hit
        x = x_new
    pd_hat = 1.0 - alive.mean()
    return pd_hat, np.sqrt(pd_hat * (1.0 - pd_hat) / n_paths)


bc = dict(V0=100.0, K=70.0, g=0.02, mu=0.06, sigma_V=0.25, T=5.0)
pd_cf = float(black_cox_pd(**bc))
pd_br, se_br = black_cox_mc(**bc, n_steps=12, bridge=True)
pd_nv, _ = black_cox_mc(**bc, n_steps=12, bridge=False)
check("F1: bridge MC within 3 SE of closed form", abs(pd_br - pd_cf) < 3 * se_br,
      f"CF={pd_cf:.4f} bridge={pd_br:.4f} SE={se_br:.4f}")
check("F2: naive discrete monitoring is biased low", pd_nv < pd_cf, f"bias={pd_nv - pd_cf:+.4f}")

mu_zero = 0.5 * 0.25**2 + 0.02                                  # makes m = 0
x0_g = np.log(100.0 / (70.0 * np.exp(-0.02 * 5.0)))
pd_m0 = float(black_cox_pd(100.0, 70.0, 0.02, mu_zero, 0.25, 5.0))
check("G: m = 0 gives twice the terminal PD",
      abs(pd_m0 - 2.0 * norm.cdf(-x0_g / (0.25 * np.sqrt(5.0)))) < 1e-12, f"PD={pd_m0:.6f}")
```

Block 4 is the CIR intensity: closed form, exact simulation, and a diagnostic that shows how often naive Euler goes negative when Feller fails.

```python
# Block 4: CIR intensity
def cir_survival(lam0, kappa, theta, sigma, T):
    """Closed-form Q-survival S(0,T) = A(T) exp(-B(T) lam0)."""
    eta = np.sqrt(kappa**2 + 2.0 * sigma**2)
    e = np.expm1(eta * T)
    den = (eta + kappa) * e + 2.0 * eta
    B = 2.0 * e / den
    A = (2.0 * eta * np.exp(0.5 * (kappa + eta) * T) / den) ** (2.0 * kappa * theta / sigma**2)
    return A * np.exp(-B * lam0)


def cir_mc(lam0, kappa, theta, sigma, T, n_paths=50_000, n_steps=100):
    """Exact noncentral chi-square transitions; trapezoid rule for the integrated intensity."""
    if 2.0 * kappa * theta < sigma**2:
        raise ValueError("Feller condition violated: 2 kappa theta < sigma^2")
    dt = T / n_steps
    c = sigma**2 * (1.0 - np.exp(-kappa * dt)) / (4.0 * kappa)
    dof = 4.0 * kappa * theta / sigma**2
    lam = np.full(n_paths, float(lam0))
    integral = np.zeros(n_paths)
    for _ in range(n_steps):
        lam_new = c * rng.noncentral_chisquare(dof, lam * np.exp(-kappa * dt) / c)
        integral += 0.5 * (lam + lam_new) * dt
        lam = lam_new
    disc = np.exp(-integral)
    return disc.mean(), disc.std(ddof=1) / np.sqrt(n_paths)


def cir_euler_negative_share(lam0, kappa, theta, sigma, T, n_paths=20_000, n_steps=260):
    """Diagnostic only: share of naive-Euler paths that visit lambda < 0."""
    dt = T / n_steps
    lam = np.full(n_paths, float(lam0))
    went_negative = np.zeros(n_paths, dtype=bool)
    for _ in range(n_steps):
        shock = sigma * np.sqrt(np.maximum(lam, 0.0) * dt) * rng.standard_normal(n_paths)
        lam = lam + kappa * (theta - lam) * dt + shock
        went_negative |= lam < 0.0
    return went_negative.mean()


cir = dict(lam0=0.03, kappa=0.5, theta=0.04, sigma=0.10, T=5.0)
S_cf = float(cir_survival(**cir))
S_mc, se_cir = cir_mc(**cir)
check("H: CIR closed form vs exact-sampling MC", abs(S_mc - S_cf) < 3 * se_cir,
      f"CF={S_cf:.5f} MC={S_mc:.5f} SE={se_cir:.5f}")
print(f"Euler paths visiting lambda<0 with sigma=0.30 (Feller fails): "
      f"{cir_euler_negative_share(0.03, 0.5, 0.04, 0.30, 5.0):.1%}")
```

Block 5 is the CDS engine of §6.8: piecewise-constant hazards, both legs, a sequential Brent bootstrap that flags rather than hides negative buckets, and the credit triangle.

```python
# Block 5: CDS legs, hazard bootstrap, credit triangle
def cum_hazard(t, knots, lams):
    """Integrated piecewise-constant hazard; lams[k] applies on (knots[k-1], knots[k]], flat beyond."""
    t = np.atleast_1d(np.asarray(t, float))
    knots, lams = np.asarray(knots, float), np.asarray(lams, float)
    lo = np.concatenate(([0.0], knots[:-1]))
    hi = knots.copy()
    hi[-1] = np.inf
    overlap = np.clip(np.minimum(t[:, None], hi[None, :]) - lo[None, :], 0.0, None)
    return overlap @ lams


def cds_legs(knots, lams, T, c, R, discount, freq=4, n_sub=12):
    """Returns (pv_premium, pv_protection, rpv01) per unit notional. T must be a multiple of 1/freq."""
    pay = np.arange(1, int(round(T * freq)) + 1) / freq
    prev = np.concatenate(([0.0], pay[:-1]))
    S_pay = np.exp(-cum_hazard(pay, knots, lams))
    S_prev = np.exp(-cum_hazard(prev, knots, lams))
    rpv01 = np.sum((pay - prev) * discount(pay) * (S_pay + 0.5 * (S_prev - S_pay)))
    grid = np.linspace(0.0, T, int(round(T * freq * n_sub)) + 1)
    S_g = np.exp(-cum_hazard(grid, knots, lams))
    pv_prot = (1.0 - R) * np.sum(discount(0.5 * (grid[1:] + grid[:-1])) * (S_g[:-1] - S_g[1:]))
    return c * rpv01, pv_prot, rpv01


def par_spread(knots, lams, T, R, discount):
    _, prot, rpv01 = cds_legs(knots, lams, T, 1.0, R, discount)
    return prot / rpv01


def bootstrap_hazard(tenors, spreads_bp, R, discount):
    """Sequential Brent bootstrap. Negative buckets are flagged and warned, never silently floored."""
    tenors = np.asarray(tenors, float)
    s = np.asarray(spreads_bp, float) / 1e4
    lams = np.zeros(tenors.size)
    negative = np.zeros(tenors.size, dtype=bool)
    for k in range(tenors.size):
        def err(lk, k=k):
            trial = lams.copy()
            trial[k] = lk
            return par_spread(tenors, trial, tenors[k], R, discount) - s[k]
        lams[k] = brentq(err, -1.0, 5.0, xtol=1e-14)
        if lams[k] < 0.0:
            negative[k] = True
            warnings.warn(f"negative hazard {lams[k]:.4f} on bucket ending {tenors[k]}y: check quotes/recovery")
    return lams, negative


def credit_triangle(s, R):
    return s / (1.0 - R)


disc4 = lambda t: np.exp(-0.04 * np.asarray(t, float))
disc0 = lambda t: np.ones_like(np.asarray(t, float))
ten = np.array([1.0, 3.0, 5.0, 7.0, 10.0])
quotes = np.array([150.0, 210.0, 260.0, 290.0, 310.0])
lam_k, neg_k = bootstrap_hazard(ten, quotes, 0.4, disc4)
reprice = max(abs(par_spread(ten, lam_k, T_k, 0.4, disc4) - q / 1e4) for T_k, q in zip(ten, quotes))
check("I: bootstrap reprices every quote", reprice < 1e-8 and not neg_k.any(),
      f"max err={reprice:.1e}; lambdas={np.round(lam_k, 5)}")

tri = credit_triangle(0.03, 0.4)
lam_f0, _ = bootstrap_hazard([5.0], [300.0], 0.4, disc0)
lam_f4, _ = bootstrap_hazard([5.0], [300.0], 0.4, disc4)
check("J1: credit triangle exact with flat discounting", abs(lam_f0[0] - tri) < 2e-4,
      f"lambda={lam_f0[0]:.5f} vs s/(1-R)={tri:.5f}")
check("J2: credit triangle approximate with r = 4%", abs(lam_f4[0] - tri) < 1e-3,
      f"lambda={lam_f4[0]:.5f} (discrete coupons paid in arrears)")

with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    lam_inv, neg_inv = bootstrap_hazard([1.0, 3.0, 5.0], [1500.0, 300.0, 250.0], 0.4, disc4)
check("K: inverted curve trips the negative-hazard flag", bool(neg_inv.any()),
      f"lambdas={np.round(lam_inv, 4)}")
```

Block 6 closes the loop: it computes the Merton term structure of spreads for the §6.2.4 firm and asks what a CDS desk would infer from it.

```python
# Block 6: the structural short end, seen through the CDS bootstrap
ten_m = np.array([0.05, 0.25, 1.0, 3.0, 5.0, 7.0, 10.0])
s_m = merton_prices(V0, F, r, sV, ten_m)[2]
for T_k, s_k in zip(ten_m, s_m):
    print(f"  Merton T={T_k:5.2f}y  s={1e4 * s_k:7.1f} bp")
peak = int(np.argmax(s_m))
check("L: structural short end ~0 and hump-shaped curve",
      s_m[0] < 0.05 * s_m.max() and 0 < peak < ten_m.size - 1,
      f"s(0.05y)={1e4 * s_m[0]:.2f} bp, peak at {ten_m[peak]}y")
with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    lam_m, neg_m = bootstrap_hazard(ten_m[2:], 1e4 * s_m[2:], 0.4, disc4)
print("CDS-style hazards implied by Merton spreads (R = 40% convention):", np.round(lam_m, 4),
      "| negative buckets:", neg_m)
print("All chapter 6 checks passed.")
```

**Edge cases ROBO must handle, in writing.** Negative or zero $E_0$, $F$, or $T$ raise. $\sigma_E$ outside 5%–300% raises with a message asking whether it was annualized. A KMV solve that fails its residual or bound checks raises, and the batch wrapper catches it, falls back to the naive DD, and sets `dd_method="naive"`. A bootstrap that produces a negative bucket returns the raw curve plus a boolean mask; any floored curve is a separate output named `*_floored`. Every output table carries `measure`, `recovery_convention`, `sigma_frequency`, and `as_of` columns.

## 6.12 Ways This Blows Up: The Consolidated List

> **Ways This Blows Up.** *Tape this next to the risk system.* (1) $\mathbb{P}/\mathbb{Q}$ mixing: a $\mathbb{Q}$ hazard in a loss forecast, or a premium shift applied twice. (2) Unannualized $\sigma_E$, which turns the high-yield index into a list of utilities. (3) $\sigma_E$ used as $\sigma_V$, which overstates PD by the leverage multiplier. (4) Trusting Merton at the short end, where its spread is zero by construction. (5) Gaussian DD-to-PD mapping, which assigns zero risk to most of the universe. (6) Discrete-monitoring bias in barrier Monte Carlo; bridge it. (7) Negative hazards from inverted curves, silently floored. (8) RMV recovery confused with RFV recovery; the numeraire matters. (9) CIR Euler schemes that go negative, and $\kappa$ and $\theta$ that one curve cannot separate. (10) Banks treated as Merton firms (concave assets, run risk). (11) Off-balance-sheet liabilities left out of the default point. (12) A barrier read off a credit agreement that 50.1% of the lenders can amend by Friday.

## 6.13 Desk Debrief

- **Every credit model answers two questions: when is $\tau$, and what is $R$.** Structural models make $\tau$ a barrier crossing you read off a balance sheet; reduced-form models make it a surprise whose rate $\lambda_t$ you read off a curve. The desk runs both, in labeled measures.
- **Itô's tax is $\tfrac12\sigma^2$, and the convexity refund goes to whoever owns the option.** In a levered firm that is the equity; the bondholders sold it.
- **Equity is a call, debt is a riskless bond minus a put, and the fulcrum is the strike where the asset distribution has mass.** Merton gets the shape right and the short end wrong: zero spread at zero maturity. Jumps and noisy information fix it.
- **$\mathbb{Q}$ PDs exceed $\mathbb{P}$ PDs by a premium that grows with $\sqrt T$ and is proportionally largest for safe names.** The premium is carry, not alpha. IDO or it didn't happen.
- **Distance to default is a ranking variable first.** The probability scale comes from at least 400 defaults, preferably 1,000, through an empirical, monotone mapping. A naive DD that never fails beats a solver that fails silently.
- **A maintenance covenant is a Black–Cox barrier; cov-lite deleted it; an uptier moves it for someone else.** In 2026, default is a negotiation, so model it as a categorical event with a negotiable barrier, and bridge your Monte Carlo.
- **$s\approx\lambda(1-R)$, and $R$ is a quoting convention.** Bootstrap piecewise-constant hazards, reprice every quote, and flag negative buckets rather than hiding them.
- **The thirteen-week model was a hazard curve all along.** Its liquidity runway goes into the intensity as a covariate, next to DD momentum.

**The Spec You Hand the Robot.** *"Build `ch06_structural_intensity_engine` in numpy/scipy, seeded `default_rng(42)`. Inputs: per-issuer market cap series (weekly, \$mm), default point $F=\text{STD}+\tfrac12\text{LTD}$ plus material off-balance-sheet liabilities (\$mm), riskless rate (continuous), and CDS quotes (tenors in years, spreads in bp, RFV recovery, vectorized discount function). Outputs per issuer and date: $V_0$, $\sigma_V$ (annual), $DD^{\mathbb{P}}$ in standard deviations of $\ln V$ at one year, $\text{PD}^{\mathbb{P}}$ from an empirical DD map (not $N(\cdot)$), $\text{PD}^{\mathbb{Q}}$ and the piecewise-constant $\lambda^{\mathbb{Q}}$ curve from CDS, the ratio $\lambda^{\mathbb{Q}}/\lambda^{\mathbb{P}}$, a Black–Cox PD for any supplied covenant barrier, and flags `dd_method`, `negative_hazard_mask`, `measure`, `recovery_convention`, `sigma_frequency`, `as_of`. Raise on non-positive inputs and on $\sigma_E$ outside 5%–300%. Never floor a hazard curve in place. Pass checks A–L of §6.11 before any output is written."*

### Exercises

1. **The vol trade inside a bond.** For the §6.2.4 firm ($V_0=100$, $F=80$, $r=4\%$, $T=1$), compute the Merton spread at $\sigma_V=15\%$ and $35\%$. Show analytically that $\partial B_0/\partial\sigma_V=-\text{vega}<0$, and explain in one sentence to Theo why a bondholder is short volatility, and why a sponsor considering a risky acquisition knows it.
2. **Is it cheap or is it the rake?** A vendor model gives an issuer a one-year $\text{PD}^{\mathbb{P}}=1.5\%$. Take asset-market correlation $\rho=0.5$ and $\text{SR}_M=0.35$. Compute $\text{PD}^{\mathbb{Q}}$ at one and five years with the Bohn–Stein shift. The five-year CDS trades at 180 bp with $R=40\%$. Use the credit triangle to get $\lambda^{\mathbb{Q}}$, compare, and list the three things you must strip before calling the difference alpha.
3. **ROBO receives $\sigma_E=0.04$ for a CCC issuer.** Name the guards in §6.11 that should fire, write the error message ROBO should print, and compute the PD ROBO would have reported if no guard existed. (Mags would like a copy for the rating-agency outlook file.)
4. **Covenants and uptiers as barrier mechanics.** A borrower has \$600mm of debt, \$110mm of EBITDA, a 6.0x maintenance covenant, an 8x multiple, and $\sigma_V=25\%$. With zero drift, compute the one-year probability of a covenant breach with `black_cox_pd`. Then a majority group issues \$200mm of new super-priority debt in a non-pro-rata uptier. Under Merton with $T=3$, compute the left-behind lenders' value before and after, holding $V_0$ fixed, and identify how much value moved to the participating group. Kaz would like to know whether this was an open market purchase. Answer him using only the payoff diagram.
5. **Mags's recovery.** Bootstrap the one-year hazard from a 500 bp quote at $R=40\%$, then again at $R=23\%$, Mags's actual recovery on her last senior unsecured name. Show that both curves reprice the quote exactly, compute the upfront on a 100 bp standard-coupon contract under each, and explain which number changes when the name defaults tomorrow.
6. **"A bankrupt company's equity is worthless."** Using Merton with $V_0=F$, $\sigma_V=30\%$, $r=4\%$, and $T=1$ (one year to plan confirmation), compute $E_0$ as a fraction of $F$ and compare it with the rule of thumb $E_0\approx0.4\,\sigma_V\sqrt T\,V_0$ for at-the-money calls. Then explain, with reference to Hertz in 2020–21 and Ines's hand history, why the model being right about the value does not make the June 2020 trade a good one.

### Deep-Dive Resource Graph

- **Podcasts:** Bloomberg *Odd Lots* (episodes on liability management, private credit, and the 2023 bank failures; titles to be verified before linking); *Flirting with Models* by Corey Hoffstein (episodes on systematic credit; titles to be verified); ISDA's podcast series, https://www.isda.org .
- **Practitioner Writing:** Blackstone, *Systematic Credit* (shelf: Blackstone_Systematic_Credit); BlackRock, *Systematic High Yield Credit* (shelf: BlackRock_Systematic_High_Yield_Credit); Man Group, *Quantitative Credit Alpha: An Early Mover Advantage* (2022; shelf: Man_Quantitative_Credit_Alpha_Early_Mover_2022); Quinn Emanuel, *Creditor-on-Creditor Violence* (January 2026), https://www.quinnemanuel.com/the-firm/publications/creditor-on-creditor-violence-how-liability-management-exercises-became-the-new-bankruptcy/ ; ISDA, *Single-name CDS Market Update* (May 2023), https://www.isda.org/a/0jLgE/Single-name-CDS-Market-Update.pdf ; Moody's, *CreditEdge* quick reference on distance to default (title only; not fetched this session).
- **Academic Papers:** Merton (1974), *On the Pricing of Corporate Debt*, Journal of Finance; Black and Cox (1976), *Valuing Corporate Securities*, Journal of Finance; Jarrow and Turnbull (1995), Journal of Finance; Lando (1998), *On Cox Processes and Credit Risky Securities*; Duffie and Singleton (1999), *Modeling Term Structures of Defaultable Bonds*, Review of Financial Studies; Duffie and Lando (2001), Econometrica, PDF at https://www.darrellduffie.com/uploads/1/4/8/0/148007615/duffielando2001.pdf ; Bharath and Shumway (2008), Review of Financial Studies; Feldhütter and Schaefer (2018), https://lbsresearch.london.edu/id/eprint/953 ; Bai, Goldstein, and Yang (2020), https://ideas.repec.org/a/eee/jfinec/v137y2020i2p297-319.html ; Nagel and Purnanandam (2020), https://www.nber.org/papers/w25807 ; Leland (1994) and Leland and Toft (1996) on endogenous default (title only); Schönbucher (2003), *Credit Derivatives Pricing Models* (title only); Bohn and Stein (2009), *Active Credit Portfolio Management in Practice* (shelf).
- **Data & Code:** ISDA CDS Standard Model, https://cdsmodel.com/ ; MathWorks `cdsbootstrap`, https://www.mathworks.com/help/finance/cdsbootstrap.html ; BIS derivatives statistics, https://www.bis.org/statistics ; SEC EDGAR, https://www.sec.gov/edgar ; CourtListener API, https://www.courtlistener.com/help/api/ ; Python `merton` package documentation for a KMV iterative solver, https://merton.readthedocs.io/en/stable/api/merton/calibration/kmv_iterative/index.html ; the chapter's reference engine in §6.11.

<!-- STATUS: COMPLETE -->
