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

> **Trend Watch.** *Single-name CDS: episodic liquidity, central clearing, and a curve migration (2018–2026).* ISDA's May 2023 *Single-name CDS Market Update* reported quarterly single-name traded notional ranging between about \$405 billion and \$1.1 trillion over 2018 to Q1 2023, with a trough in Q4 2020 and a five-year peak of \$1.1 trillion in Q1 2023 as the bank failures drove hedging demand. Breadth shrank: the number of reference entities trading in a quarter fell from 854 in Q1 2018 to 719 in Q1 2023; of 1,169 entities that traded at least once in five years, about 600 traded less than once a quarter, while 496 traded every quarter and accounted for more than 80% of activity. In Q1 2023, 51.2% of single-name notional and 87.4% of index notional was centrally cleared. BIS statistics put total CDS notional at \$8.5 trillion at end-December 2023, down from \$9.9 trillion six months earlier, with 65% centrally cleared (BIS, May 16, 2024), and credit derivatives at \$9.2 trillion at end-June 2024, down 9% year on year (BIS, November 21, 2024). Plumbing changed too: the ISDA CDS Standard Model, open-source C code administered by S&P Global Market Intelligence, announced in June 2026 that its standard rate curves were moving to a new S&P Global site, with the old site shutting after August 15, 2026 (cdsmodel.com). What it means for the desk: for most issuers, a full single-name CDS curve is a stale or synthetic object. Bootstrap where the curve trades, and elsewhere build $\lambda$ from bond spreads, index-implied intensities, or structural signals. Store the date of the last real trade next to every hazard curve, and check the curve source URL in your config before the next migration breaks it at 6 a.m.

### Deep-Dive Resource Graph

- **Podcasts:** ISDA's podcast series (an episode index exists at https://www.isda.org ; no credit-model-specific episode verified this session).
- **Practitioner Writing:** ISDA, *Single-name CDS Market Update* (May 2023), https://www.isda.org/a/0jLgE/Single-name-CDS-Market-Update.pdf ; BIS OTC derivatives statistics, https://www.bis.org/publ/otc_hy2405.htm and https://www.bis.org/publ/otc_hy2411.htm ; O'Kane and Turnbull (2003), *Valuation of Credit Default Swaps*, Lehman Brothers Quantitative Credit Research.
- **Academic Papers:** Jarrow and Turnbull (1995), *Pricing Derivatives on Financial Securities Subject to Credit Risk*, Journal of Finance 50(1); Duffie and Singleton (1999), *Modeling Term Structures of Defaultable Bonds*, Review of Financial Studies 12(4); Lando (1998), *On Cox Processes and Credit Risky Securities*, Review of Derivatives Research; Cox, Ingersoll, and Ross (1985), *A Theory of the Term Structure of Interest Rates*, Econometrica; O'Kane (2008), *Modelling Single-name and Multi-name Credit Derivatives*, Wiley; Lando (2004), *Credit Risk Modeling*, Princeton.
- **Data & Code:** ISDA CDS Standard Model, https://cdsmodel.com/ ; MathWorks `cdsbootstrap` documentation, https://www.mathworks.com/help/finance/cdsbootstrap.html ; *Arbitrage Opportunities in CDS Term Structure*, https://arxiv.org/pdf/1811.08038 ; BIS statistics portal, https://www.bis.org/statistics ; the `cds_legs` and `bootstrap_hazard` reference implementations in §6.11.

