# Chapter 6-B: Options for Credit People: Replication, Black–Scholes, Greeks, Jump-to-Default and the Two Measures

> **Prerequisites.** Itô's lemma and the volatility tax (§6.1); the Merton payoff and the closed forms it produces (§6.2, where they are stated and then used); default as a surprise with an intensity (§6.6). Spread duration and CS01 come from Chapter 4-B. Nothing else. Read this chapter after Chapter 6 and before Chapter 7. Every later chapter that prices an option, quotes a hazard or says "$\mathbb{Q}$" points back here.

## Cold Open: Vega on a Book With No Options

*Monday, 7:12 a.m.* Theo's first risk report has eleven columns, and he understands eight of them. The ninth says **VEGA (per vol pt): −\$41k**. The tenth says **JTD: −\$6.3mm**. The eleventh says **MEASURE: Q**, in a font that suggests it has been shouted before.

"Who sold options in my book?" he asks. His book is forty-one high-yield bonds and a short CDX hedge. He has never sold an option. He has barely bought lunch.

"You did," Ines says, without looking up. "Every bond you bought. A high-yield bond is a short put that pays a coupon. You wrote forty-one of them. Vega is the risk system telling you that it noticed."

Kaz is already at the whiteboard, writing $V_0N(d_1)-Fe^{-rT}N(d_2)$ with the speed of someone who has written it four thousand times and been asked what it means twice. "It's just Black–Scholes on the firm," they say. "Assume the assets are lognormal and tradeable."

"You cannot short a factory," Mags says. "In 1994 we measured vega by calling the guy who sold us the bonds and asking whether he sounded nervous. One parameter, and he answered the phone."

ROBO, asked on Friday to "remove the vega from Theo's book," had produced a one-line execution plan: sell all forty-one bonds. Vega: zero. Carry: zero. Theo: horrified. ROBO, as always, did exactly what was asked.

"But what does the credit agreement say?" Theo asks, because that is what he asks.

"It says you are short a put to the shareholders," Ines says. "Your loans say you're short a call to the borrower. Your 101 put is long an option that only works if two rating agencies agree. Your portability clause is a digital you sold to the sponsor. Your backstop is a put you sold to the plan. The CLO you sell loans to is running an option book it calls a compliance test. Price them."

Theo looks at the eleventh column. "And which probabilities do I use? Mine, or the market's?"

Nobody answers immediately, which on this desk is how you know a question is good.

**If every instrument on a credit desk is an option, where is the one page that shows how to price one, what each risk-report line means, what happens when the underlying can jump to zero, and whose probabilities go into the expectation?**

By the end of this chapter you will be able to: build any credit payoff from calls, puts and digitals; derive Black–Scholes by replication and say why $N(d_2)$ is a probability nobody believes; read every Greek as a risk-report line, including the one that is not a derivative; explain the left wing of a high-yield vol surface; add a jump to default and get the Carr–Wu result of §23.3 as a corollary with an error term; change measure for an *intensity*; and use the hazard multiplier and the premium ratio as traded quantities, always saying which measure you are in.

## 6-B.1 Payoffs First: The Hockey Stick Is the Atom

### 6-B.1.1 Desk framing: every document is a payoff function

RSSG trained Theo to read a waterfall: who gets paid, in what order, from what pot. An options desk reads the same thing as a function $g(\cdot)$ from a terminal value to a cash flow. Once you can write $g$, pricing is a separate and much more boring problem, and most credit-desk errors happen at the first step: the wrong $g$, written from the summary of the indenture instead of the definitions (Law 8, App E).

Three atoms build every payoff in this book. Let $S_T$ be the value of some underlying at date $T$: a share price, a firm's asset value $V_T$, a post-close bond price, a pool's adjusted par.

$$
\underbrace{(S_T-K)^+}_{\text{call}},\qquad \underbrace{(K-S_T)^+}_{\text{put}},\qquad \underbrace{\mathbf 1_{\{S_T>K\}}}_{\text{digital}},\qquad x^+\equiv\max(x,0).
$$

**Notation for this chapter.** The style bible gives $P$ to the bond price and $S_t$ to a generic underlying. Option values are therefore written $C$ (call), $\text{Put}$ (put) and $\text{Dig}$ (digital), with arguments when they matter: $\text{Put}_{\text{BS}}(S_0,K,T,\sigma,r)$. Survival probabilities always carry their measure as a superscript, $S^{\mathbb{Q}}(T)$ or $S^{\mathbb{P}}(T)$, so they cannot be confused with $S_t$. The letter $q$ stays reserved for inventory; we assume no dividends, and where a dividend matters we say so in words. Merton's debt claim is $B_t$, as in §6.2.

### 6-B.1.2 Put–call parity: the only theorem that needs no model

The identity $(S_T-K)^+-(K-S_T)^+=S_T-K$ holds in every state of the world. A portfolio long a call and short a put therefore pays the same as one share minus $K$ in cash at $T$. If two portfolios pay the same thing in every state, they must cost the same today, or someone buys the cheap one, sells the dear one and goes home early. With a constant riskless rate $r$ and no dividends,

$$
C(K)-\text{Put}(K)=S_0-Ke^{-rT}.
$$

No volatility, no distribution, no drift. Parity is the first sanity check in every engine in this book: if your call and put disagree with it, the bug is in your code or in your data, never in the market. (Listed single-stock options are American and pay attention to dividends and borrow. Parity then becomes a pair of inequalities, and the size of the violation is how §23.4 backs out the borrow fee.)

### 6-B.1.3 Digitals, and the density hidden in the strike axis

Differentiate the call payoff in its strike: $\partial_K(S_T-K)^+=-\mathbf 1_{\{S_T>K\}}$. Take expectations under any pricing rule that is linear and discounts at $r$:

$$
\text{Dig}(K)=e^{-rT}\,\mathbb{Q}(S_T>K)=-\frac{\partial C}{\partial K},\qquad \frac{\partial^2C}{\partial K^2}=e^{-rT}f^{\mathbb{Q}}(K),
$$

where $f^{\mathbb{Q}}$ is the density of $S_T$ under the pricing measure. The second identity is Breeden and Litzenberger (1978). Read it carefully, because it is the cleanest definition of $\mathbb{Q}$ a desk will ever get: **$\mathbb{Q}$ is not a belief. It is the second derivative of the price list.** If you have calls at every strike, you have the risk-neutral density, and you did not have to assume anything about anybody's utility function to get it.

Two consequences. A digital is the limit of a tight call spread, $\big[C(K-\epsilon)-C(K+\epsilon)\big]/(2\epsilon)$, so its gamma is unbounded at the strike near expiry, which is why portability (§15.3) and every other pass-or-fail clause is hard to hedge. And a probability extracted from prices is a $\mathbb{Q}$ probability, always (§6-B.6).

### 6-B.1.4 The capital structure as a ladder of call spreads

Here is the restructuring banker's waterfall, written as an options book. Let a firm have assets $V_T$ at $T$ and debt tranches $j=1,\dots,J$ ordered from senior to junior, with face values $F_j$. Define attachment points $a_1=0$ and $a_{j+1}=a_j+F_j$, so total debt is $a_{J+1}$. Under absolute priority, tranche $j$ receives

$$
\min\!\big((V_T-a_j)^+,\,F_j\big)=(V_T-a_j)^+-(V_T-a_{j+1})^+,
$$

a call spread on the assets struck at its attachment and detachment points. Equity receives $(V_T-a_{J+1})^+$, a plain call struck at total debt. Sum the payoffs: the sum telescopes to $(V_T-0)^+=V_T$. The capital structure distributes the firm and nothing else, which is the conservation law Chapter 13's waterfall engine enforces (§13.7).

```text
Figure 6-B.1  The capital structure as a ladder of call spreads (payoff at T against asset value V_T)

payoff
  |                                                         equity: call struck at a4
  |                                                       /
  |                                                     /
  |                                  junior: call spread [a3,a4]
  |                         ________________________/ 
  |                        /                       
  |      senior unsecured: call spread [a2,a3]     
  |              _________/                         
  |             /                                    
  |   1L: call spread [0,a2]                         
  |___/________|_________|_____________|______________ V_T
  0           a2        a3            a4
                        ^ plan value lands here: the [a3,a4] tranche is the fulcrum
```

Three things fall out of the ladder that RSSG teaches by experience and the desk needs as formulas.

1. **The fulcrum is the at-the-money call spread.** The tranche whose interval $[a_j,a_{j+1}]$ contains the plan value is the one most sensitive to the valuation fight. Tranches above it are deep in the money and tranches below it far out of it, and both have delta near zero. Kaz, who once asked whether the fulcrum was "the tranche that does the most leverage," was accidentally half right.
2. **Seniority is moneyness.** Every liability-management transaction moves strikes: an uptier inserts a tranche at $a=0$ and pushes everyone else's attachment points up by its face (§13.3); a drop-down removes assets from $V_T$ for some tranches but not others (§13.6).
3. **Each tranche is long volatility below its midpoint and short volatility above it.** A call spread is convex near its lower strike and concave near its upper one. The senior secured tranche, with lower strike zero, is all concavity: it is short volatility everywhere. Equity is all convexity. Mezzanine tranches flip sign as the firm deteriorates, which is the structural reason the CCC bond of §8.3 starts behaving like stock.

Price each call with any model you like and the tranche values follow: $\text{value}_j=C(a_j)-C(a_{j+1})$, with $C(0)=V_0$. In Merton's lognormal model this is the §6.2.3 formula applied tranche by tranche. Chapter 23 calls the same picture "one distribution, many strikes" (§23.1).

Used in: §6.2.1 (Merton's two-tranche case), §8.3, §13.3, §13.7, §15.3, §16.3, §21.4, §23.1.

## 6-B.2 Replication: One Hedge Ratio, No Opinion About the Drift

### 6-B.2.1 Desk framing: the price of an option is the cost of the factory that makes it

Ines: "You don't price a hand by guessing the river. You price it by what it costs to make the same hand from the cards on the table." A dealer who sells a call needs no view on the stock, only a recipe that turns shares and cash into the call's payoff in every state; the recipe's cost *is* the price. Theo's thirteen-week model plays no part. Replication does not care what you think, only what you can trade.

### 6-B.2.2 One period, two states, and the probability that is a ratio of prices

Let the underlying be worth $S$ today and either $uS$ or $dS$ after one period of length $\Delta t$, with $d<e^{r\Delta t}<u$ (otherwise one of the assets dominates the other and there is an arbitrage). A claim pays $C_u$ or $C_d$. Buy $\Delta$ units of the underlying and invest $b$ in the riskless asset, and choose them so the portfolio pays the claim in both states:

$$
\Delta\,uS+b\,e^{r\Delta t}=C_u,\qquad \Delta\,dS+b\,e^{r\Delta t}=C_d.
$$

Subtracting, $\Delta=(C_u-C_d)/\big((u-d)S\big)$. Substituting back and writing the cost $C_0=\Delta S+b$,

$$
C_0=e^{-r\Delta t}\Big[\tilde q\,C_u+(1-\tilde q)\,C_d\Big],\qquad \tilde q=\frac{e^{r\Delta t}-d}{u-d}\in(0,1).
$$

Look at what is missing: the physical probability $p$ that the up state happens. It never enters. The weight $\tilde q$ looks like a probability (it is between 0 and 1 and the weights sum to 1), and pricing *as if* it were one, then discounting at $r$, gives the right answer. That is all a risk-neutral probability is: a ratio of prices that behaves like a probability. Cox, Ross and Rubinstein (1979) turned this one-period argument into the binomial tree.

**The credit version, and the fix §3.1 needs.** Replace the share with a one-period zero-coupon bond that pays 100 if the issuer survives and $R$ (in points) if it defaults. If it trades at $P_0$,

$$
P_0=e^{-r\Delta t}\Big[(1-\pi^{\mathbb{Q}})\,100+\pi^{\mathbb{Q}}R\Big]\quad\Longrightarrow\quad \pi^{\mathbb{Q}}=\frac{100-P_0e^{r\Delta t}}{100-R}.
$$

At $P_0=90$, $r=4\%$, $\Delta t=1$ and $R=40$, $P_0e^{r\Delta t}=93.67$ and $\pi^{\mathbb{Q}}=6.33/60\approx10.5\%$ *(illustrative)*. This is the default probability *implied by the price*, not the one Theo believes after reading the 10-Q. The two-point bond of §3.1 should be read this way: priced under $\mathbb{Q}$, then forecast under $\mathbb{P}$, with the gap between $\pi^{\mathbb{Q}}$ and Theo's $\pi^{\mathbb{P}}$ being the premium of §6-B.6 rather than an inconsistency.

### 6-B.2.3 Continuous time: delta hedging and the Black–Scholes PDE

Section 6.2.2 ran the delta-hedging argument for Merton's equity $E(t,V)$. Here is the general version, with one addition that matters more to a trader than the PDE itself.

Let the underlying follow $dS_t=\mu S_t\,dt+\sigma S_t\,dW_t$ under $\mathbb{P}$, and let $f(t,S)$ be a claim paying $g(S_T)$. Hold the claim and short $\Delta$ units of the underlying, $\Pi=f-\Delta S$. Itô's lemma (§6.1) gives

$$
d\Pi=\Big(f_t+\mu Sf_S+\tfrac12\sigma^2S^2f_{SS}-\Delta\mu S\Big)dt+(f_S-\Delta)\,\sigma S\,dW_t .
$$

Set $\Delta=f_S$. The noise disappears, so $\Pi$ is riskless and must earn $r$: $d\Pi=r(f-Sf_S)\,dt$. The $\mu$ terms cancel, leaving the Black–Scholes PDE

$$
f_t+rSf_S+\tfrac12\sigma^2S^2f_{SS}-rf=0,\qquad f(T,S)=g(S).
$$

The Feynman–Kac theorem turns the PDE into an expectation. The solution is

$$
f(t,S)=e^{-r(T-t)}\,\mathbb{E}^{\mathbb{Q}}\big[g(S_T)\mid S_t=S\big],\qquad dS_t=rS_t\,dt+\sigma S_t\,dW^{\mathbb{Q}}_t,
$$

which is the continuous-time version of the binomial weights: price as if the underlying grew at $r$, then discount at $r$. The drift that Theo would spend a week estimating appears nowhere.

### 6-B.2.4 The gamma rent: what a hedged option actually earns

The PDE assumes the hedger knows $\sigma$. Nobody does. Suppose a dealer sells a claim priced at implied volatility $\sigma_i$, hedges with the delta computed at $\sigma_i$, and the underlying then realizes volatility $\sigma_r$, so that $(dS)^2=\sigma_r^2S^2\,dt$. The dealer is long the hedge and short the claim; take the mirror image, a trader long the claim and short $\Delta=f_S$, with $f$ evaluated at $\sigma_i$. Itô gives

$$
d\Pi=f_t\,dt+\tfrac12f_{SS}\,\sigma_r^2S^2\,dt .
$$

The PDE at $\sigma_i$ says $f_t=rf-rSf_S-\tfrac12\sigma_i^2S^2f_{SS}$. Substituting, and writing $\Gamma=f_{SS}$,

$$
d\Pi-r\Pi\,dt=\tfrac12\,\Gamma S^2\big(\sigma_r^2-\sigma_i^2\big)\,dt .
$$

This is the most useful equation in options trading, and it is why traders talk about volatility instead of prices. A delta-hedged long option earns, every instant, half its dollar gamma times the gap between realized and implied *variance*. Long gamma means you are paid when the underlying moves more than the price assumed; short gamma means you collect a rent when it moves less. In practice the rent is collected in discrete hedges, so the realized P&L is path-dependent, and the dollar gamma $\tfrac12\Gamma S^2$ is largest exactly when the underlying sits near the strike close to expiry.

Now translate. A Merton bondholder is short a put on the firm (§6.2.1), so a hedged bondholder is short gamma on the assets: paid a rent when assets are calmer than the spread implied, billed $\tfrac12\Gamma V^2(\sigma_r^2-\sigma_i^2)$ when they are not, with $\Gamma$ largest near the default point. That is the precise sense in which "high yield is a short put that pays a coupon" (§11.1): the coupon is the rent and the bad weeks are the gamma bill.

> **[SOURCE EXTRACTION]** *Veronesi_Fixed_Income_Securities p.611:* "If the model is correct, then at maturity [$T_O$] the replicating portfolio will deliver exactly the payoff of the option we sold today."
>
> **Annotation.** Veronesi's setting is an option on a zero-coupon Treasury, hedged dynamically with bonds; the replication logic is identical to ours, and the load-bearing words are the first five. "If the model is correct" covers three assumptions that fail in credit, in increasing order of severity. Volatility is not known: the gamma-rent equation above says exactly what that costs. Rebalancing is not continuous: a high-yield bond trades a few times a day at a half-point bid–ask, so the hedger rebalances on bands and carries the residual. And the underlying can jump, which no amount of delta replicates (§6-B.5). The 2026 desk keeps the replication argument as the *definition* of a fair price and treats every failure of its assumptions as a separately reported risk line (§6-B.3).

### 6-B.2.5 The Black–Scholes formula, and the two probabilities of one event

Under $\mathbb{Q}$, $\ln S_T=\ln S_0+(r-\tfrac12\sigma^2)T+\sigma\sqrt T\,Z$ with $Z\sim\mathcal N(0,1)$. Split the call payoff:

$$
e^{rT}C=\mathbb{E}^{\mathbb{Q}}\big[S_T\mathbf 1_{\{S_T>K\}}\big]-K\,\mathbb{Q}(S_T>K).
$$

The second term is direct: $S_T>K$ iff $Z>-d_2$, with

$$
d_2=\frac{\ln(S_0/K)+(r-\tfrac12\sigma^2)T}{\sigma\sqrt T},\qquad \mathbb{Q}(S_T>K)=N(d_2).
$$

For the first term, change numeraire. Define a new measure $\mathbb{Q}^S$ by the density $d\mathbb{Q}^S/d\mathbb{Q}=S_T/(S_0e^{rT})=\exp(\sigma\sqrt T Z-\tfrac12\sigma^2T)$. That density is positive and has expectation 1, so $\mathbb{Q}^S$ is a probability measure. Under it, $Z$ is normal with mean $\sigma\sqrt T$ (complete the square in the exponent), so $\ln S_T$ has mean $\ln S_0+(r+\tfrac12\sigma^2)T$ and

$$
\mathbb{E}^{\mathbb{Q}}\big[S_T\mathbf 1_{\{S_T>K\}}\big]=S_0e^{rT}\,\mathbb{Q}^S(S_T>K)=S_0e^{rT}N(d_1),\qquad d_1=d_2+\sigma\sqrt T .
$$

Putting the pieces together, and using parity for the put:

$$
C=S_0N(d_1)-Ke^{-rT}N(d_2),\qquad \text{Put}=Ke^{-rT}N(-d_2)-S_0N(-d_1).
$$

Both $N(d_1)$ and $N(d_2)$ are probabilities of the *same* event, exercise at expiry, under two different measures. $N(d_2)$ uses cash as the numeraire; $N(d_1)$ uses the share. Neither is the probability that the option will actually finish in the money: that would need $\mu$ in place of $r$, and it is $N(DD)$ in Merton's language (§6.2.3). Two correct probabilities of one event, neither of which anybody believes. Welcome to derivatives.

For Merton, $N(-d_2)=\mathbb{Q}(V_T<F)$ is the risk-neutral default probability that Chapter 6 stated; the physical $N(-DD)$ swaps $r$ back to $\mu$, and the gap is §6-B.6.

Used in: §3.1 (the two-point bond, read correctly), §6.2.2–6.2.3, §6.4 (the KMV inversion), §11.1, §16.3–16.4 (rights, backstops and warrants priced with these formulas), §23.1–23.2.

## 6-B.3 The Greeks as Lines on a Risk Report

### 6-B.3.1 Desk framing: a Greek is a question somebody asks at 7 a.m.

A Greek is a partial derivative with a job title. *Delta:* if the underlying moves a dollar, what do I make? *Gamma:* how wrong is my delta after it moves? *Vega:* if everyone decides the world is more volatile, what do I lose, even if nothing moves? *Theta:* what does waiting cost? *Rho:* what if rates move? And one that is not a derivative at all, *JTD:* what if the issuer is not there tomorrow? A credit desk asks all six. It just calls them CS01, convexity, "spread vol," carry, DV01 and "the jump," and then wonders why the options desk upstairs can hedge and it can't.

### 6-B.3.2 The five derivatives, in closed form

Differentiate the §6-B.2.5 formulas. Write $\phi(x)=e^{-x^2/2}/\sqrt{2\pi}$ for the standard normal density, and use the identity $S_0\phi(d_1)=Ke^{-rT}\phi(d_2)$, which follows from expanding $d_1^2-d_2^2=2\ln(S_0e^{rT}/K)$ and saves a page of algebra:

| Greek | Call | Put | Units |
| :-- | :-- | :-- | :-- |
| Delta $\Delta=\partial f/\partial S$ | $N(d_1)$ | $-N(-d_1)$ | per \$1 of underlying |
| Gamma $\Gamma=\partial^2f/\partial S^2$ | $\dfrac{\phi(d_1)}{S_0\sigma\sqrt T}$ | same | per \$1, per \$1 |
| Vega $\nu=\partial f/\partial\sigma$ | $S_0\phi(d_1)\sqrt T$ | same | per 1.00 of vol; divide by 100 for a vol point |
| Theta $\Theta=\partial f/\partial t$ | $-\dfrac{S_0\phi(d_1)\sigma}{2\sqrt T}-rKe^{-rT}N(d_2)$ | $-\dfrac{S_0\phi(d_1)\sigma}{2\sqrt T}+rKe^{-rT}N(-d_2)$ | per year of calendar time |
| Rho $\rho^{\text{opt}}=\partial f/\partial r$ | $KTe^{-rT}N(d_2)$ | $-KTe^{-rT}N(-d_2)$ | per 1.00 of rate |

(The superscript on $\rho^{\text{opt}}$ keeps it apart from the correlation $\rho$ of §6.3.2.) Gamma and vega are the same for calls and puts because parity makes their difference linear in $S$, and linear things have no curvature and no opinion about volatility.

### 6-B.3.3 The theta–gamma identity: the rent and the bill

Substitute the Greeks into the PDE of §6-B.2.3 and it becomes an accounting identity:

$$
\Theta+rS\Delta+\tfrac12\sigma^2S^2\Gamma=rf .
$$

For a delta-hedged position the middle term is offset by the financing of the hedge, and what remains is $\Theta-r(f-S\Delta)=-\tfrac12\sigma^2S^2\Gamma$. Read it as the desk reads it: **theta is the rent you pay for gamma**, charged at the implied variance. Combine it with the gamma-rent equation of §6-B.2.4 and the whole economics of a hedged option fits in one line. You pay $\tfrac12\Gamma S^2\sigma_i^2$ per unit time in decay and collect $\tfrac12\Gamma S^2\sigma_r^2$ from the moves. A short-gamma book reverses the signs. It collects the decay and pays for the moves, and its P&L distribution has the shape every high-yield manager knows: many small good days and a few large bad ones (§11.1). There is no free gamma. There is only gamma whose rent somebody mispriced.

### 6-B.3.4 Merton debt, Greek by Greek

In Merton, $B=Fe^{-rT}-\text{Put}(V,F)$. Every Greek of the bond is the negative of the put's Greek, plus the riskless bond's rho:

$$
\frac{\partial B}{\partial V}=N(-d_1),\qquad \frac{\partial^2B}{\partial V^2}=-\frac{\phi(d_1)}{V_0\sigma_V\sqrt T},\qquad \frac{\partial B}{\partial\sigma_V}=-V_0\phi(d_1)\sqrt T,\qquad \frac{\partial s}{\partial\sigma_V}=\frac{V_0\phi(d_1)\sqrt T}{B_0T}.
$$

The bondholder is long a little of the firm, short gamma on its assets, and short volatility. The last formula converts the bond's vega into spread units by differentiating $s=-T^{-1}\ln(B_0/Fe^{-rT})$.

*Worked example (illustrative).* Take the §6.2.4 firm ($V_0=100$, $F=80$, $r=4\%$, $\sigma_V=25\%$, $T=1$; a 216 bp, double-B-ish credit) and a CCC cousin with the same assets but $F=95$ and $\sigma_V=40\%$.

| Line | §6.2.4 firm ($F=80$, $\sigma_V=25\%$) | CCC cousin ($F=95$, $\sigma_V=40\%$) |
| :-- | --: | --: |
| $d_1$, $d_2$ | 1.178, 0.928 | 0.428, 0.028 |
| Equity $E_0$ / debt $B_0$ | 24.78 / 75.22 | 19.91 / 80.09 |
| Put on firm (= $Fe^{-rT}-B_0$) | 1.64 | 11.19 |
| Spread $s$ | 216 bp | 1,307 bp |
| $\mathbb{Q}(\tau\le T)=N(-d_2)$ | 17.7% | 48.9% |
| Bond delta $\partial B/\partial V$ | 0.120 | 0.334 |
| Bond gamma $\partial^2B/\partial V^2$ | −0.0080 | −0.0091 |
| Bond vega, per asset-vol point | −0.199 | −0.364 |
| Spread vega, per asset-vol point | +26.5 bp | +45.4 bp |
| Bond per \$1 of equity, $N(-d_1)/N(d_1)$ | 0.136 | 0.502 |
| Elasticity hedge ratio $h$ (23.10) | 0.045 | 0.125 |

Three readings. The CCC bond is a third of the firm by delta, and it moves fifty cents per dollar of equity, against fourteen for the double-B. Its vega is nearly twice as large per vol point, on a bond whose spread is six times wider, so vega *per basis point of spread* falls as the credit worsens while vega in dollars rises. And the Merton recovery problem of §6.2.4 is still there: 1,307 bp on a 48.9% default probability is a loss given default of about 25% (the bond is $1-e^{-sT}=12.3\%$ below its riskless value), a recovery near 75 cents that Mags has not seen on an unsecured bond since the Clinton administration. The Greeks are right in shape and wrong in level for the same reason the spreads are: the diffusion has no jump in it. §6-B.5 adds one.

### 6-B.3.5 The risk report, line by line

| Risk-report line | Option definition | Credit reading | What hedges it | Built / applied |
| :-- | :-- | :-- | :-- | :-- |
| Delta | $\partial f/\partial S$ | CS01 in spread space; shares per bond in stock space | CDX; the stock | Ch 4-B; §23.5 |
| Gamma | $\partial^2f/\partial S^2$ | Spread convexity; the bondholder's short gamma on assets | Options on CDX; listed puts | §23.5; Ch 10-B |
| Vega | $\partial f/\partial\sigma$ | Short $\sigma_V$; the cold open's −\$41k per vol point | Index swaptions; the equity surface | §23.2 |
| Theta | $\partial f/\partial t$ | Carry plus roll-down: the rent | Nothing; it is why you are there | Ch 4-B; §9 carry |
| Rho | $\partial f/\partial r$ | DV01, and the hedge ratio that is not modified duration | Treasury futures | Ch 4-B; §8.2 |
| JTD | $f(\text{post})-f(\text{pre})$ | $R-P$ per bond; $(1-R)-\text{MTM}$ per unit of bought CDS | Put spreads; CDS | §6-B.5; §23.5; §28.4 |

The last line is the one an equity-options desk forgets and a credit desk lives on. JTD is a finite difference across the default event, and it does not shrink when you look more closely. The cold open's −\$6.3mm is the sum over Theo's bonds of (recovery minus price) times face *(illustrative)*. Law 6 (App E): charge the jump once, on this line, and not again in the spread, the skew and the position size (§28.4).

Used in: §8.3 (bond-to-equity sensitivity), §11.1, §19 (basket risk lines), §21.4 (pool-level Greeks), §23.5 (the Natenberg map, in spread space), §28.1 and §28.4 (risk budgets and Kelly with a jump).

## 6-B.4 Implied Volatility and Skew: A Price Quoted in the Wrong Units, on Purpose

### 6-B.4.1 Desk framing

Options trade in volatility for the same reason bonds trade in spread: the unit strips out the boring parts of the price (moneyness, time, rates) and leaves the part people disagree about. A \$2.10 put is not information. A 74% implied volatility on a 20-delta put, when the at-the-money vol is 48%, is.

### 6-B.4.2 Definition, existence, and a solver that does not embarrass you

The implied volatility $\sigma_{\text{imp}}(K,T)$ is the number that makes Black–Scholes match the market price: $C_{\text{BS}}(S_0,K,T,\sigma_{\text{imp}},r)=C^{\text{mkt}}$. It exists and is unique whenever the price lies strictly inside the no-arbitrage bounds,

$$
\big(S_0-Ke^{-rT}\big)^+<C^{\text{mkt}}<S_0,\qquad \big(Ke^{-rT}-S_0\big)^+<\text{Put}^{\text{mkt}}<Ke^{-rT},
$$

because vega is strictly positive, so $C_{\text{BS}}$ is strictly increasing in $\sigma$. It tends to intrinsic value as $\sigma\downarrow0$ and to $S_0$ as $\sigma\uparrow\infty$. Outside the bounds there is no implied vol, and the right output is not a number but a reason: a stale quote, an American premium being fed to a European formula, a borrow fee being treated as volatility, or a crossed market.

The solver every desk eventually writes is Newton's method, $\sigma_{n+1}=\sigma_n-\big(C_{\text{BS}}(\sigma_n)-C^{\text{mkt}}\big)/\nu(\sigma_n)$, started near the Brenner and Subrahmanyam (1988) at-the-money approximation $\sigma_0\approx\sqrt{2\pi/T}\,C^{\text{mkt}}/S_0$. Newton diverges in the wings, where vega is tiny, so the §6-B.9 solver keeps a bisection bracket, rejects any step that leaves it, and declares convergence in *price* units, not vol units. A vol that is correct to $10^{-8}$ on a price nobody can trade is not precision. It is decoration.

### 6-B.4.3 Skew: two credit reasons the left wing is steep

If Black–Scholes were the truth, $\sigma_{\text{imp}}$ would be flat in $K$. It never is. By §6-B.1.3 a non-flat implied vol curve is the market telling you that its $\mathbb{Q}$-density is not lognormal. For a leveraged firm there are two reasons the low strikes are expensive, and both are credit.

*Leverage.* In Merton, equity is a call on assets, and a call's elasticity $\Omega=VN(d_1)/E$ is at least 1 (a convex payoff through the origin always has $E\le VE_V$) and rises as the call moves out of the money. So $\sigma_E=\Omega\,\sigma_V$ rises as $V$ falls. Low equity strikes correspond to states with low assets and high leverage, where the stock is more volatile. That is the compound-option skew of §23.1, and CreditGrades (§23.2) is built on it.

*Jump-to-default.* The stock can go to zero in a single print. A diffusion cannot produce that at any volatility, so the implied vol of a deep out-of-the-money put has to rise without bound to price it. §6-B.5.5 proves how fast.

The fingerprints differ in prices, not vols: if the stock cannot reach zero, $\text{Put}(K)/K\to0$ as $K\to0$; under jump-to-default it flattens to a positive floor (the `floor_ratio` test of §23.4).

> **Desk Myth vs. Desk Reality.** *Myth:* "Implied vol is the market's forecast of realized volatility." *Reality:* it is the break-even volatility of the gamma-rent equation, priced under $\mathbb{Q}$. It contains a variance risk premium (sellers of insurance want paying) and, in a high-yield name, a default premium. The gamma-rent equation tells you what a forecast is worth: you profit from a long hedged option when $\sigma_r>\sigma_i$, *weighted by where the dollar gamma happened to be*. Volatility that happens far from the strike earns nothing; Ines calls it "being right in a room nobody was in."

Used in: Ch 10-B (index option skew, payer versus receiver), §16.4 (warrant vol on an unlisted reorganized equity), §23.1–23.4 (the surface engine), §23.6 (cap-structure signals).

## 6-B.5 Jump-to-Default: Merton 1976 With One Jump, and Carr–Wu for Free

### 6-B.5.1 Desk framing: the Tuesday that is not in the diffusion

"In textbooks companies die by diffusion," Mags says. "They drift down, they touch a barrier, they stop. In my experience they die on a Tuesday at 7 a.m. in a press release with the word 'regrettably' in it." §6.2.4 showed what the diffusion costs: zero short-dated spreads and recoveries near 90 cents. The repair is to let the underlying jump, and the simplest jump that matters to credit is the one to zero.

### 6-B.5.2 The model

Let $N_t$ be a Poisson process with constant $\mathbb{Q}$-intensity $\lambda$ and let $\tau$ be its first jump: default. The stock is worth zero from $\tau$ on. Before default, under $\mathbb{Q}$,

$$
\frac{dS_t}{S_{t^-}}=(r+\lambda)\,dt+\sigma\,dW^{\mathbb{Q}}_t-dN_t .
$$

The $-dN_t$ term takes the stock to zero at the jump. The extra $+\lambda\,dt$ is the compensator: $\mathbb{E}^{\mathbb{Q}}[dN_t]=\lambda\,dt$, so $\mathbb{E}^{\mathbb{Q}}[dS_t/S_{t^-}]=r\,dt$ and the discounted stock is a $\mathbb{Q}$-martingale, as it must be for any traded asset. The survivors pay a hazard tax to the estate of the dead, and that tax is part of their drift. Solving,

$$
S_t=\tilde S_t\,\mathbf 1_{\{\tau>t\}},\qquad \tilde S_t=S_0\exp\!\Big\{\big(r+\lambda-\tfrac12\sigma^2\big)t+\sigma W^{\mathbb{Q}}_t\Big\},\qquad \mathbb{Q}(\tau>t)=S^{\mathbb{Q}}(t)=e^{-\lambda t}.
$$

This is Merton (1976) with one jump size, minus 100%: equity is a call on assets until a surprise (fraud, a lost lawsuit, an LMT that leaves equity nothing) makes it worthless whatever the diffusion was doing.

### 6-B.5.3 Calls and puts: one formula and one decomposition

A call pays only if the firm survives, and the survival indicator is independent of $W$:

$$
C^{\text{JTD}}=e^{-rT}e^{-\lambda T}\,\mathbb{E}\big[(\tilde S_T-K)^+\big]=C_{\text{BS}}\big(S_0,K,T,\sigma,\;r+\lambda\big),
$$

because $\tilde S$ grows at $r+\lambda$ and the combined discount is $e^{-(r+\lambda)T}$, which is exactly the Black–Scholes call at the rate $r+\lambda$. A put pays $K$ in every default state and $(K-\tilde S_T)^+$ in every survival state:

$$
\text{Put}^{\text{JTD}}(K)=\underbrace{K\,e^{-rT}\big(1-e^{-\lambda T}\big)}_{K\,\times\,U^{\text{Eur}}(T)}+\underbrace{\text{Put}_{\text{BS}}\big(S_0,K,T,\sigma,\;r+\lambda\big)}_{\text{diffusive put at the hazard-shifted rate}} . \tag{6B.1}
$$

**A put on a defaultable stock is $K$ unit recovery claims plus a diffusive put priced at a hazard-shifted rate.** Expand the second term and (6B.1) is the §23.4 formula (23.8) term for term; check parity and it holds, since $C^{\text{JTD}}-\text{Put}^{\text{JTD}}=S_0-Ke^{-rT}$. Two consequences that later chapters use:

- *Calls get more valuable, holding the share price fixed.* Rho is positive, so raising the rate from $r$ to $r+\lambda$ raises the call. The strike is paid only in survival states, and the surviving stock must outperform to pay for the dead. This is why Kaz's $e^{-\lambda T}$ haircut on the Hertz warrants charged the funeral twice (§16.4).
- *Puts get a floor.* As $K\to0$ the second term vanishes faster than $K$, so $\text{Put}^{\text{JTD}}(K)/K\to U^{\text{Eur}}(T)$. The floor ratio is the hazard.

### 6-B.5.4 Corollary 1: the Carr–Wu corridor, with an error term

Take two strikes $A<B$ and divide the put spread by its width. From (6B.1),

$$
\frac{\text{Put}^{\text{JTD}}(B)-\text{Put}^{\text{JTD}}(A)}{B-A}=U^{\text{Eur}}(T)+\varepsilon(A,B),\qquad 0\le\varepsilon(A,B)\le e^{-(r+\lambda)T}\,N\!\big(-\tilde d_2(B)\big), \tag{6B.2}
$$

with $\tilde d_2(B)=\big[\ln(S_0/B)+(r+\lambda-\tfrac12\sigma^2)T\big]/(\sigma\sqrt T)$. *Proof.* The error is $\varepsilon=e^{-(r+\lambda)T}\,\mathbb{E}\big[(B-\tilde S_T)^+-(A-\tilde S_T)^+\big]/(B-A)$. The bracket divided by $B-A$ lies in $[0,1]$ and is zero whenever $\tilde S_T\ge B$, so $\varepsilon$ is non-negative and at most the discounted probability that the surviving path ends below $B$. $\square$

That is the European Carr–Wu result as a corollary: the put spread is a pure default claim plus a *corridor leak*, the chance that a live stock diffuses down into the strikes, which vanishes when the strikes sit far below spot relative to $\sigma\sqrt T$. Carr and Wu's exact American statement (§23.3) replaces the leak with an assumption: if the pre-default stock never trades below $B$, then $\varepsilon=0$ identically, early exercise happens at $\tau$, and the claim being priced becomes the American one, $U^{\text{Am}}(T)=\frac{\lambda}{r+\lambda}\big(1-e^{-(r+\lambda)T}\big)$. The model sizes the leak when the assumption is only approximately true, which is the number a desk needs.

*Worked example (illustrative).* A \$6 stock, $\sigma=80\%$, $r=4\%$, $\lambda=14.5\%$, $T=1$, and a \$1 put ($A=0$, $B=1$). Then $U^{\text{Eur}}=0.9608\times(1-e^{-0.145})=0.1297$. The bound in (6B.2) is $e^{-0.185}N(-2.071)\approx0.016$; the actual leak is $\text{Put}_{\text{BS}}(6,1,1,0.8,0.185)\approx0.0037$. The \$1 put is 97% default claim and 3% diffusion. §6-B.8 uses exactly this chain.

### 6-B.5.5 Corollary 2: the wing must blow up, and how fast

**Proposition.** In the jump-to-default model, the Black–Scholes implied volatility of a put struck at $K$ below the forward $F_0=S_0e^{rT}$ satisfies

$$
\sigma_{\text{imp}}(K)\sqrt T\;\ge\;-c+\sqrt{c^2+2\ln(F_0/K)},\qquad c=N^{-1}\big(S^{\mathbb{Q}}(T)\big)=N^{-1}\big(e^{-\lambda T}\big). \tag{6B.3}
$$

*Proof.* For any Black–Scholes put, $\text{Put}_{\text{BS}}(K;\sigma)/K\le e^{-rT}N(-d_2(\sigma))$, since the subtracted term $S_0N(-d_1)$ is positive. By (6B.1) the jump put is at least $KU^{\text{Eur}}=Ke^{-rT}(1-e^{-\lambda T})$. At the implied vol the two prices are equal, so $N(-d_2)\ge1-e^{-\lambda T}$, that is, $d_2\le c$. Write $x=\sigma_{\text{imp}}\sqrt T$ and $L=\ln(F_0/K)>0$, so $d_2=(L-\tfrac12x^2)/x$. Then $d_2\le c$ is $x^2+2cx-2L\ge0$, whose positive root gives (6B.3). $\square$

The default probability alone puts a floor under the wing. With $\lambda=5\%$ and $T=1$, $c=N^{-1}(0.951)=1.657$, and at $K/F_0=0.2$ the bound is 78.5%, which the §23.4 table (about 100% at that moneyness) respects. As $K\to0$ the bound grows like $\sqrt{2\ln(F_0/K)/T}$: implied variance rises linearly in log-moneyness with slope 2. That is the steepest left wing Lee's (2004) moment formula allows. A stock that can reach zero sits exactly on the boundary. A stochastic-volatility model can make the wing steep, and an exotic one can even match the slope, but no model without mass at zero produces a positive floor in $\text{Put}(K)/K$. The floor ratio, not the slope, is how you tell the two apart in data.

### 6-B.5.6 Hedging a jump with an instrument that diffuses

A claim $f(t,S)$ on a defaultable stock has two risks: the diffusion, with sensitivity $f_S$, and the jump, which changes its value by $f(t,0)-f(t,S)$ while the stock changes by $-S$. Hedge with $\Delta$ shares. Under $\mathbb{P}$, with physical intensity $\lambda^{\mathbb{P}}$ (the hedge is about what will happen, so it uses the physical intensity), the instantaneous variance of the hedged position is

$$
\frac{\operatorname{Var}^{\mathbb{P}}}{dt}=\sigma^2S^2\big(f_S-\Delta\big)^2+\lambda^{\mathbb{P}}S^2\big(j-\Delta\big)^2,\qquad j\equiv\frac{f(t,S)-f(t,0)}{S}.
$$

Here $j$ is the *jump delta*: the hedge ratio that would exactly offset the default. Minimizing over $\Delta$ is a weighted average:

$$
\Delta^{*}=\frac{\sigma^2\,f_S+\lambda^{\mathbb{P}}\,j}{\sigma^2+\lambda^{\mathbb{P}}},\qquad \min\frac{\operatorname{Var}^{\mathbb{P}}}{dt}=\frac{\sigma^2\lambda^{\mathbb{P}}}{\sigma^2+\lambda^{\mathbb{P}}}\,S^2\big(f_S-j\big)^2 .
$$

The residual is zero only if $f_S=j$, which means the claim is linear between 0 and $S$, a share or cash. For anything with curvature, one hedge instrument cannot neutralize two risks. One instrument, two risks: one equation short. For bought CDS hedged with stock, $j$ is roughly minus the protection payout divided by the share price, a large negative number, and $f_S$ is the small negative CreditGrades delta, so $\Delta^*$ is a compromise that hedges neither risk properly. That is the §23.5 observation that the stock "leaves almost all of the jump on the table," now with the formula behind it. The repair is a second instrument that also jumps: a put spread, which by (6B.2) jumps by its width at default and barely diffuses. Two instruments, two risks, solved.

Notice which intensity went where: the *price* uses $\lambda^{\mathbb{Q}}$, the variance-minimizing *hedge* uses $\lambda^{\mathbb{P}}$, and one engine needs both, labelled (§6-B.6).

> **Ways This Blows Up.** *The slow bleed.* A name that drifts to zero over years (GM 2005–09, §23.3) diffuses through every corridor, so the leak is the whole price and your "default claim" is a vol position. *Borrow.* Hard-to-borrow puts are rich because shorting is expensive, not because default is likely; strip borrow from parity first (§23.4). *Which default?* The put floor measures the intensity of *equity wipe-out*. A distressed exchange can default the bonds and leave the equity alive, and an uptier can crush the excluded bonds while the stock rallies (§14.1, §23.6). The put chain cannot see the distressed-exchange intensity $\lambda_D$ of §14.2. Comparing a put-implied hazard with a bond-implied hazard compares two different events unless you say which one. *American versus European.* Listed puts are American: use $U^{\text{Am}}$, and tag every chain with its convention.

Used in: §5.3 (jumps in continuous time), §8.3, §10.9 (trend when the underlying jumps), §16.4 (warrants), §18.6 (the HJB with jump-to-default, which inherits the $\mathbb{P}$-hedge/$\mathbb{Q}$-price split), §23.3–23.5, §28.4 (Kelly with a jump).

## 6-B.6 The Two Measures: Girsanov for Intensities and the Premium Ratio

### 6-B.6.1 Desk framing: the eleventh column

Section 6.3 gave Ines's napkin: $\mathbb{P}$ is what happens, $\mathbb{Q}$ is what the table charges you to find out. It then changed measure for a diffusion, where only the drift moves. Credit's main risk is a jump with an intensity, and the measure change for a jump changes *how often the bad thing happens*, which is precisely the number a CDS quote and an agency default study disagree about. This section derives it, names the multiplier, and makes it something a desk can rank and trade.

### 6-B.6.2 Girsanov for a Brownian motion, with the density written down

§6.3.2 stated the result; here is the object that does the work. Fix a horizon $T$ and a constant market price of asset risk $\eta=(\mu-r)/\sigma_V$. (Chapter 6 wrote this ratio out longhand; $\theta$ is taken by the CIR long-run level of §6.7.) Define

$$
Z_T=\frac{d\mathbb{Q}}{d\mathbb{P}}\bigg|_{\mathcal F_T}=\exp\!\Big(-\eta W_T-\tfrac12\eta^2T\Big).
$$

$Z_T$ is positive with $\mathbb{E}^{\mathbb{P}}[Z_T]=1$, so it defines an equivalent measure: the same events are possible, with different weights. Under $\mathbb{Q}$ the moment generating function of $W_T$ is $\mathbb{E}^{\mathbb{P}}[Z_Te^{uW_T}]=\exp(\tfrac12u^2T-u\eta T)$, which says $W_T\sim\mathcal N(-\eta T,T)$. So $W^{\mathbb{Q}}_t=W_t+\eta t$ is a $\mathbb{Q}$-Brownian motion, and $dV_t=\mu V_t\,dt+\sigma_VV_t\,dW_t=rV_t\,dt+\sigma_VV_t\,dW^{\mathbb{Q}}_t$. The density reweights paths: it makes the bad paths (low $W_T$) heavier and the good paths lighter, by exactly enough that the asset is priced as if it earned $r$. The volatility does not change, because equivalent measures agree on which paths are possible, and quadratic variation is a property of the path.

### 6-B.6.3 Girsanov for an intensity: the hazard multiplier

Now let $N_t$ count defaults, with constant $\mathbb{P}$-intensity $\lambda^{\mathbb{P}}$. For any constant $\xi>0$ define

$$
Z_T=\xi^{N_T}\,e^{-(\xi-1)\lambda^{\mathbb{P}}T}.
$$

(Here $\xi$ is the hazard multiplier; Chapters 5, 12 and 14 use $\xi$ locally for unrelated quantities.) The Poisson generating function $\mathbb{E}^{\mathbb{P}}[z^{N_T}]=e^{\lambda^{\mathbb{P}}T(z-1)}$ gives $\mathbb{E}^{\mathbb{P}}[Z_T]=1$, so $Z_T$ is a density. Under the new measure,

$$
\mathbb{Q}(N_T=n)=\mathbb{E}^{\mathbb{P}}\big[Z_T\mathbf 1_{\{N_T=n\}}\big]=\xi^ne^{-(\xi-1)\lambda^{\mathbb{P}}T}\,e^{-\lambda^{\mathbb{P}}T}\frac{(\lambda^{\mathbb{P}}T)^n}{n!}=e^{-\xi\lambda^{\mathbb{P}}T}\frac{(\xi\lambda^{\mathbb{P}}T)^n}{n!},
$$

which is Poisson with intensity $\xi\lambda^{\mathbb{P}}$. So

$$
\lambda^{\mathbb{Q}}=\xi\,\lambda^{\mathbb{P}},\qquad S^{\mathbb{Q}}(T)=e^{-\xi\lambda^{\mathbb{P}}T}=\big(S^{\mathbb{P}}(T)\big)^{\xi}. \tag{6B.4}
$$

**Risk-neutral survival is physical survival raised to the power $\xi$.** With time-varying, even stochastic, multipliers the same construction gives $\lambda^{\mathbb{Q}}_t=\xi_t\lambda^{\mathbb{P}}_t$ (Brémaud's theorem for point processes is the general statement). The diffusion Girsanov could only tilt the drift. The jump Girsanov changes the *rate*, and any $\xi>0$ gives an equivalent measure. No-arbitrage alone does not pin $\xi$: a stock and a riskless bond cannot span a jump, so many $\mathbb{Q}$'s fit the same share price. Only something that pays at default (a CDS, a bond, a low-strike put) pins $\lambda^{\mathbb{Q}}$, only a $\mathbb{P}$ model (a default study, Theo's waterfall) supplies $\lambda^{\mathbb{P}}$, and the multiplier is their ratio.

### 6-B.6.4 Two premia and a recovery premium

The spread pays for three things, and the identity that separates them is exact:

$$
s=\lambda^{\mathbb{Q}}L^{\mathbb{Q}}=\underbrace{\lambda^{\mathbb{P}}L^{\mathbb{P}}}_{\text{expected loss}}+\underbrace{(\lambda^{\mathbb{Q}}-\lambda^{\mathbb{P}})\,L^{\mathbb{P}}}_{\text{hazard (event) premium}}+\underbrace{\lambda^{\mathbb{Q}}\big(L^{\mathbb{Q}}-L^{\mathbb{P}}\big)}_{\text{recovery premium}} . \tag{6B.5}
$$

(Expand the right side and the cross terms cancel.) The credit triangle (§6.8) sits on the left; the desk's job is the right. Two further distinctions matter in practice.

*The event premium versus the premium on the intensity's motion.* If $\lambda_t$ is stochastic (CIR, §6.7), Girsanov applies twice: to the Brownian motion driving $\lambda_t$, which changes its $\mathbb{Q}$-dynamics and puts a premium for spread *risk* into the curve's slope, and to the default jump itself, which is $\xi$. Jarrow, Lando and Yu (2005) show that if defaults are conditionally diversifiable (independent given the common factors), then $\xi=1$ and every premium lives in the intensity's dynamics. The empirical answer is that $\xi$ is above one and moves around. Driessen (2005) estimates a ratio of risk-neutral to physical default intensity of about 2.3 for ten-year BBB bonds (as summarized in Federal Reserve Bank of New York Staff Report 577).

*Liquidity and tax.* A bond spread also pays for illiquidity and state taxes, both material in Driessen's decomposition; strip them before trusting (6B.5) (§24.3).

> **[SOURCE EXTRACTION]** *Bohn_Stein_Active_Credit_Portfolio_Management p.516:* "CDS prices provide an estimate of risk-neutral expected loss; however, a model is needed to break apart the default probability, the LGD"
>
> **Annotation.** This is the identification problem in one clause: a spread identifies the product $\lambda^{\mathbb{Q}}L^{\mathbb{Q}}$, never the factors, so every "CDS-implied default probability" on a screen has a recovery assumption hidden inside it, usually the 40% convention that Law 7 (App E) calls a quoting convention rather than a forecast. Bohn and Stein's answer is a model. The 2026 desk has a second answer that their 2009 book could not count on: a liquid listed put chain. By (6B.1) the low-strike put floor measures $\lambda^{\mathbb{Q}}$ of equity wipe-out *without* any recovery input, so put floor plus bond spread together identify the market's recovery, subject to the "which default?" caveat of §6-B.5. §6-B.8 does it on Halvorsen.

> **Trend Watch.** *The premium moves, and the instruments that read it moved too (2002–2026).* **The ratio is not a constant.** Berndt, Douglas, Duffie and Ferguson (NBER Working Paper 24213, 2018), using Markit CDS against Moody's Analytics EDFs, find premia peaking in 2002, 2008–09 and the second half of 2011; normalized by expected loss, median premia move by more than a factor of ten, and the premium per unit of expected loss rises in distress, more so for investment grade. **The single-name market thinned.** By one 2025 count of cleared volumes, single-name CDS was on the order of 6% of index notional *(approx.; see §23.3)*, so for most high-yield issuers $\lambda^{\mathbb{Q}}$ must now be read from bonds (with a recovery assumption) or from listed puts (with a corridor assumption). **What it means for the desk:** a $\xi$ fitted in 2021 is not a parameter in 2026. It is a state variable, countercyclical, and largest exactly where expected loss looks smallest. Store it as a time series per issuer, not as a constant in a config file.

### 6-B.6.5 The premium ratio as a traded quantity

Define the **premium ratio** of issuer $i$ as spread over physical expected loss:

$$
\text{PR}_i=\frac{s_i}{\lambda^{\mathbb{P}}_iL^{\mathbb{P}}_i}=\xi_i\,\frac{L^{\mathbb{Q}}_i}{L^{\mathbb{P}}_i}.
$$

It is a traded quantity in the most literal sense: selling protection is going long it. Take a single name with $L^{\mathbb{Q}}=L^{\mathbb{P}}=L$, sell protection at $s=\xi\lambda^{\mathbb{P}}L$ for a year and approximate the default count as Poisson. The expected P&L under $\mathbb{P}$, per unit notional, is $s-\lambda^{\mathbb{P}}L=(\xi-1)\lambda^{\mathbb{P}}L$, and the standard deviation of the default loss is $L\sqrt{\lambda^{\mathbb{P}}}$. The single-name Sharpe ratio of harvesting the premium is therefore

$$
\text{SR}=\frac{(\xi-1)\lambda^{\mathbb{P}}L}{L\sqrt{\lambda^{\mathbb{P}}}}=(\xi-1)\sqrt{\lambda^{\mathbb{P}}} . \tag{6B.6}
$$

Recovery drops out, and two numbers are left. A high-yield name with $\lambda^{\mathbb{P}}=2\%$ and $\xi=2$ gives $\text{SR}\approx0.14$. An investment-grade name with $\lambda^{\mathbb{P}}=0.2\%$ and $\xi=4$ gives $3\times0.045\approx0.13$. The larger multiplier in investment grade is not a free lunch: a small $\lambda$ eats a large $\xi$ under the square root. The Sharpe of a *book* scales with the square root of effective breadth, and default correlation is what caps that breadth (Law 2; §28.2). That is also why the premium exists in the first place: if defaults diversified away, Jarrow–Lando–Yu says nobody would be paid for the jump itself.

Ranked cross-sectionally, $\text{PR}_i$ is a signal: a DTS-neutral book selling protection on high-PR names and buying it on low-PR names is long the premium and short the error in the desk's $\mathbb{P}$ model, and its returns are not alpha until the premium it was *supposed* to earn is stripped out (Law 1). The same structure links the Priming Risk Score, a $\mathbb{P}$ object (§13.8), to the SMR break probability, a $\mathbb{Q}$ gauge (§15.4): their gap is a premium ratio for an event that is not default.

### 6-B.6.6 The rule: say which measure you are in

Law 4 (App E) is the rule, and here is its implementation.

1. **Every expectation carries a superscript.** $\mathbb{E}^{\mathbb{P}}$ or $\mathbb{E}^{\mathbb{Q}}$, in the text and in the code. An unlabelled $\mathbb{E}$ is a bug report waiting for an owner.
2. **Every probability field in a schema carries a measure tag**: `P`, `Q`, or `Q_nominal`. Conversions happen only through an explicit, sourced multiplier ($\xi$, or the structural shift of §6.3.2), never by reuse. Double-counting the premium, by applying a $\mathbb{P}\to\mathbb{Q}$ shift to a PD that was already backed out of a spread, is the commonest error in this whole subject.
3. **`Q_nominal` is a confession, labelled as one.** When nothing traded spans the risk (a backstop on unlisted equity, §16.3; a warrant before listing, §16.4; a CoC put on a deal that may not close, §15.2), the "risk-neutral" price is a $\mathbb{P}$ model with drift set to $r$. Report it as a range over $\xi$ or drift.
4. **Prices, hedges and sizes use different measures.** Prices and implied quantities (spreads, put floors, implied vols) are $\mathbb{Q}$. Default forecasts, loss budgets, hedge ratios that minimize realized variance (§6-B.5.6) and position sizes (§28.4) are $\mathbb{P}$. A CDS hazard is not an agency default rate, and an agency default rate is not a hazard until the distressed-exchange intensity has been separated out (§14.1).

> **[SOURCE EXTRACTION]** *Bohn_Stein_Active_Credit_Portfolio_Management p.181:* "If our objective is valuation of other securities, then we can in fact use the PDs directly estimated from this approach, as risk-neutral PDs are what we require. However, if our objective is to build a portfolio risk model, we need physical PDs, so some transformation will be necessary based upon an estimate and functional form for the market price of risk."
>
> **Annotation.** That is rule 4, written in 2009 about PDs backed out of debt prices. The modern desk adds two things. First, the "transformation" is a premium ratio that moves by a factor of ten over a cycle (Trend Watch above), so a fixed functional form is a regime bet. Second, Bohn and Stein note on the same page that risk-neutral PDs may be acceptable for *ranking* obligors, because the transformation rarely reorders them, except among firms with similar risk-neutral PDs and very different systematic risk. That exception is where a premium-ratio book makes its money: two names at one spread, one cyclical and one not, share $\lambda^{\mathbb{Q}}$ but not $\lambda^{\mathbb{P}}$, and only $\text{PR}$ tells them apart.

Used in: §1.3.1 (the bid equation's measure), §3.1, §6.3 (extended here), §11.3–11.4 (PD models are $\mathbb{P}$), §13.8 (PRS), §14.1 and §14.9 (two default rates), §15.4 (the SMR gauge), §16.3 (`Q_nominal`), §24.3 (stripping liquidity before decomposing), §28.4.

## 6-B.7 The Desk's Option Book: Eight Instruments You Already Own

This section is the single home for the option readings that Parts III–V use. Each later chapter applies one entry and back-references it here.

| Instrument | Payoff, in this chapter's atoms | Measure | Home |
| :-- | :-- | :-- | :-- |
| CCC bond | Call spread on assets near its lower strike | $\mathbb{Q}$ price, $\mathbb{P}$ size | §8.3 |
| HY bond | Riskless bond minus a put on assets | $\mathbb{Q}$ | Ch 11 |
| 101 CoC put | Digital(deal) × digital(trigger) × put on post-close price | `Q_nominal` | §15.2 |
| Portability | Short digital on leverage the issuer controls | `Q_nominal` | §15.3 |
| Right / backstop | Call / short put on pre-money value | `Q_nominal` | §16.3 |
| Plan warrant | Diluted long-dated call on a call | $\mathbb{Q}$ once listed | §16.4 |
| Leveraged loan | Floater minus a borrower call at par | $\mathbb{Q}$ | §21.1, §21.5 |
| CLO OC test | Short puts, barrier digitals, short order statistics | $\mathbb{Q}$ prices, $\mathbb{P}$ defaults | §21.4 |

**The CCC bond is an equity option that wears a tie to work (§8.3).** The table in §6-B.3.4 says it in numbers: at 1,307 bp the Merton bond has a delta of a third of the firm, moves fifty cents per dollar of equity, and carries nearly twice the vega of the double-B. It has a coupon, a CUSIP and a trustee, which is the tie. Underneath, it is a third of a share of the firm plus a short put with a large vega. Its interest-rate duration collapses for the same reason (§8.3's recovery route): the payoff is dominated by the default leg, which does not discount at the Treasury curve. In a multi-tranche structure, a junior bond whose call spread sits near its *lower* strike is even long volatility, like equity, which is the §6-B.1.4 picture.

**High yield is a short put that pays a coupon (Ch 11).** From $e^{-sT}=B_0/(Fe^{-rT})=1-\text{Put}/(Fe^{-rT})$, the spread is the put premium paid in installments: $s\approx\text{Put}/(Fe^{-rT}T)$. For the §6.2.4 firm that is $1.64/76.86\approx2.13\%$ against the exact 2.16%. The P&L shape is the gamma rent of §6-B.3.3: collect the decay, pay for the moves. The Bernoulli default leg has skewness $-(1-2p)/\sqrt{p(1-p)}$, which is why Chapter 11 calls BB defense tail avoidance and CCC defense pricing (§11.10).

**The 101 change-of-control put (§15.2)** pays $\mathbf 1_{\{\text{deal}\}}\mathbf 1_{\{\text{trig}\}}(K-P^{\text{post}})^+$ with $K=101$ plus accrued. It is a put gated by two digitals, and the rating-event digital is positively correlated with the put's moneyness (§15.2's ratio $M>1$), so multiplying the probabilities underprices it. Nothing listed spans a deal closing: `Q_nominal`.

**Portability as a digital (§15.3).** A carve-out that cancels the put when pro-forma leverage is below a test $\bar\ell$ makes the holder short $V_{\text{CoC}}\times\mathbf 1_{\{\ell\le\bar\ell\}}$: a digital. §6-B.1.3 says a digital's gamma is unbounded at the strike. §15.3 adds the twist that matters: the counterparty *chooses* $\ell$ after reading $\bar\ell$, so the probability of passing is a decision variable, not a distribution. Kaz's diagnosis is correct, for once: "It's a digital where the other side sets the spot." Ines: "That's not a digital. That's a gift."

**Rights and backstops (§16.3).** The right attached to a plan share is $\frac{m}{n_0+m}(x-K)^+$, a diluted call on pre-money value. The backstop is $-\frac{mn_0}{n_0+m}(K-x)^+$, a short put whose fair fee is its Black–Scholes value, under `Q_nominal` because nothing trades on a company that has not emerged (§16.3 says so).

**Plan warrants (§16.4).** A warrant is $1/(1+\omega)$ calls on the diluted equity value, solved as a fixed point; by §6-B.5.3 a jump to zero raises it at a fixed share price. Thirty-year warrants are mostly vega and survival; the Hertz warrants live in §16.6.

**The leveraged loan is short a call (§21.1).** When the borrower can refinance at will, the lender holds $\min(P^{\text{nc}},100)=P^{\text{nc}}-(P^{\text{nc}}-100)^+$, where $P^{\text{nc}}$ is the value of the same loan without the call. In the 101 soft-call window the strike is 101 for repricings. The call caps the price near par and makes the loan negatively convex in spread: tightening is given away, widening is kept. That is §21.5's repricing wave, the borrower exercising. When the borrower is sick the call is far out of the money, and the loan becomes what Merton says every debt claim is, a short put on the firm. Larkspur Foam's 2029 first-lien term loan at 84 (Chapter 13's cold open) is not short a call in any meaningful sense; it is short a put struck where the drop-down basket lets the sponsor move the assets. **A loan is short a call when it is healthy and short a put when it is sick. The one thing it is never long is optionality.**

**The OC test as an option book (§21.4).** The adjusted collateral principal amount (21.5) is a sum of option payoffs on loan prices. The pool is short a put on each defaulted loan struck at the agency recovery, short barrier digitals on discount obligations, and short the lowest order statistics of its own CCC bucket. The cushion $\kappa_k$ of each test is a function of those prices. The diversion of interest when $\kappa_k<0$ is a digital on the cushion, which is where the gamma lives: one CCC downgrade near the trigger moves the equity tranche's cash flow discontinuously. That is the mechanism behind the forced sellers of §11.6 and §16.2.

Used in: §8.3, Ch 11 (especially §11.1 and §11.6), Ch 13 (Larkspur, from the cold open to §13.6), §15.2–15.3, §16.2–16.4, §16.6, §21.1, §21.4–21.5.

## 6-B.8 Worked Case: Halvorsen on Monday, One Bond, One Put, Three Measures

*Halvorsen is fictional; its capital structure is in the issuer bible of the front matter. All numbers are illustrative.* It is the Monday after Chapter 1's lender call. The Halvorsen 7.25% senior unsecured notes due 2029 have opened at 78. The stock is \$6.00. The one-year listed \$1 put is \$0.136 mid, and the at-the-money implied vol is 80%. `bondmath.py` (Chapter 4-B) gives the notes a Z-spread of 1,150 bp. Theo's own numbers are $\mathbb{P}$ numbers: the desk's structural model gives a one-year default probability of 6.0%, and his RSSG waterfall, run on the documents and not the summary, recovers 40 cents for the notes.

**Step 1: the put gives the hazard, without a recovery ($\mathbb{Q}$).** By (6B.1) and (6B.2), the \$1 put is a default claim plus a corridor leak. At 80% vol the leak is about \$0.004 (§6-B.5.4), so the American unit recovery claim is about 0.132, and solving $U^{\text{Am}}(\lambda)=0.132$ gives $\lambda^{\mathbb{Q}}\approx14.5\%$. No recovery assumption was needed: in a wipe-out the stock goes to roughly zero whatever the bonds recover.

**Step 2: the bond gives the product, so the pair gives the recovery ($\mathbb{Q}$).** The credit triangle on the flat-curve approximation gives $L^{\mathbb{Q}}=s/\lambda^{\mathbb{Q}}=0.115/0.145=0.793$, so the market's recovery is about 21 cents. Every "CDS-implied PD at 40% recovery" screen hides that number.

**Step 3: Theo's numbers ($\mathbb{P}$).** $\lambda^{\mathbb{P}}=-\ln(1-0.06)=6.19\%$ and $L^{\mathbb{P}}=0.60$. The hazard multiplier is $\xi=14.5/6.19=2.34$, close to the Driessen benchmark: the market's fear of default *frequency* is ordinary. The premium ratio is $\text{PR}=0.115/(0.0619\times0.60)=3.10$.

**Step 4: decompose the spread with (6B.5).**

| Component | Formula | bp |
| :-- | :-- | --: |
| Expected loss | $\lambda^{\mathbb{P}}L^{\mathbb{P}}$ | 371 |
| Hazard premium | $(\lambda^{\mathbb{Q}}-\lambda^{\mathbb{P}})L^{\mathbb{P}}$ | 499 |
| Recovery premium | $\lambda^{\mathbb{Q}}(L^{\mathbb{Q}}-L^{\mathbb{P}})$ | 280 |
| Spread | $\lambda^{\mathbb{Q}}L^{\mathbb{Q}}$ | 1,150 |

The disagreement is not about whether Halvorsen defaults. It is about what the notes are worth when it does: 280 bp of the spread is the market paying Theo to hold a recovery view. Mags reads the table twice. "Twenty-one cents for a senior unsecured with a drop-down basket in the credit agreement? I've seen worse. I've seen twelve. But I've also read this one, and the basket's been used." Theo has read it too. Recovery is the one question on this desk where an ex-RSSG banker has a genuine edge, and this chapter has been about extracting it cleanly enough to bet on.

**Step 5: isolate the recovery view.** Buy the notes and buy enough \$1 puts that the default payoff is zero *at the market's recovery*. Per 100 face the notes lose $78-21=57$ points at default, so buy 57 points of put payout: \$570,000 of \$1 strikes, 5,700 contracts per \$1mm face, costing about \$77,500. In the recovery-of-market-value approximation of §6.6.3, with constant intensities and payment at default, the expected excess return per year in points is, for the notes, $\lambda^{\mathbb{Q}}(78-R^{\mathbb{Q}})-\lambda^{\mathbb{P}}(78-R^{\mathbb{P}})$, and for the puts $-(\lambda^{\mathbb{Q}}-\lambda^{\mathbb{P}})\times57$. Add them and the hazard premium cancels exactly:

$$
\mathbb{E}^{\mathbb{P}}[\text{excess return}]\approx\lambda^{\mathbb{P}}\big(R^{\mathbb{P}}-R^{\mathbb{Q}}\big)=0.0619\times19\approx1.2\text{ points per year}.
$$

All of it arrives in the default state: plus 19 points if Theo's 40 is right, nothing at 21, and a loss below 21. If Theo's recovery were certain, the Sharpe ratio would be $\lambda^{\mathbb{P}}\Delta R/(\Delta R\sqrt{\lambda^{\mathbb{P}}})=\sqrt{\lambda^{\mathbb{P}}}\approx0.25$, the same shape as (6B.6). Uncertainty about recovery only lowers it. This is a recovery bet with the default probability hedged out. It is the RSSG trade, finally isolated, and it is small, honest and slow.

**What kills it.** *Which default?* A distressed exchange that leaves the equity alive pays the puts nothing while the notes take the haircut: the worst state, and the $\lambda_D$ the put chain cannot see (§14.1–14.2). *The corridor.* The leak is 3% here and all of it in a slow bleed. *The recovery is a mixture.* Theo's 40 must be conditioned on coalition membership (§14.4) and come out of the Chapter 12-B state machine, not a pre-LMT waterfall.

> **Poker Table.** Ines replays the hand twenty days later: notes 80, puts \$0.12, position flat within a quarter point *(illustrative)*. Theo is disappointed. "That's what a hedged recovery bet does before the river," Ines says. "Nothing. You bought the right to be paid for being right about one number on one day. If it makes money before that day, find the risk you forgot to hedge."

Used in: Ch 1 cold open (Halvorsen), §13.8 (PRS as the $\mathbb{P}$ input), §14.1–14.4 (which default, which recovery), §23.3–23.6 (the put-surface engine and cap-structure trades), §24.3 (stripping basis effects before using the bond's spread), Ch 12-B.

## 6-B.9 Specification for AI Implementation: `credit_options.py`

**The Spec You Hand the Robot.** *What ROBO built from the vague version* ("price Halvorsen's puts"): a Black–Scholes pricer at the 80% at-the-money vol that valued the \$1 put at \$0.007 and reported "default probability: 0.0%." Every line was correct, and the answer was wrong by a factor of 20, because nobody told ROBO that the stock can jump to zero. The precise spec follows.

*Module.* `credit_options.py`, imported by Chapters 8, 11, 15, 16, 21, 23 and 28. Pure Python plus `numpy`; no `scipy`, so that normal tails are computed with `math.erfc` and stay accurate below $10^{-10}$.

*Units and conventions.* Prices per unit of underlying (or points per 100 face); rates, vols and intensities as annual decimals; $T$ in years, with day count converted by the caller. No dividends; borrow is stripped before the call. Every probability object carries `measure ∈ {"P","Q","Q_nominal"}`.

*Edge cases and guards.* $T\to0$ and $\sigma\sqrt T\to0$ return discounted intrinsic, not NaN. Implied vol outside no-arbitrage bounds returns NaN with a reason string. Newton steps that leave the bisection bracket are replaced by bisection. Convergence is tested in price units. `MeasuredPD.to_q` refuses anything that is not a $\mathbb{P}$ probability and refuses an unsourced multiplier, which makes double-counting the premium a runtime error instead of a career event. `hazard_from_put` raises if the quoted put is cheaper than its own diffusive part (bad vol, borrow or stale quote).

```python
"""credit_options.py (Chapter 6-B). Units as in the spec; every PD is measure-tagged."""
import math
from dataclasses import dataclass

import numpy as np

SQRT2 = math.sqrt(2.0)
EPS_T = 1e-10                 # below this an option is at expiry
VOL_LO, VOL_HI = 1e-4, 10.0   # implied-vol bracket
MEASURES = ("P", "Q", "Q_nominal")


def norm_cdf(x):
    """N(x) via erfc, accurate in the far left tail where 1 - N(-x) is not."""
    return 0.5 * math.erfc(-x / SQRT2)


def norm_pdf(x):
    return math.exp(-0.5 * x * x) / math.sqrt(2.0 * math.pi)


def norm_ppf(p, lo=-12.0, hi=12.0):
    """Inverse normal CDF by bisection: slow, monotone, and never wrong by much."""
    if not 0.0 < p < 1.0:
        raise ValueError("p must lie in (0, 1)")
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if norm_cdf(mid) < p:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def _d1_d2(S, K, T, sigma, rate):
    sig_rt = sigma * math.sqrt(T)
    d1 = (math.log(S / K) + (rate + 0.5 * sigma * sigma) * T) / sig_rt
    return d1, d1 - sig_rt


def bs_price(S, K, T, sigma, rate, kind="call"):
    """Black-Scholes European price. `rate` may be r, or r + lambda (6B.1)."""
    if S <= 0.0 or K <= 0.0:
        raise ValueError("S and K must be positive; default states belong to jtd_price")
    disc_K = K * math.exp(-rate * T)
    if T < EPS_T or sigma * math.sqrt(T) < 1e-12:       # zero-vol limit
        fwd = S - disc_K
        return max(fwd, 0.0) if kind == "call" else max(-fwd, 0.0)
    d1, d2 = _d1_d2(S, K, T, sigma, rate)
    if kind == "call":
        return S * norm_cdf(d1) - disc_K * norm_cdf(d2)
    if kind == "put":
        return disc_K * norm_cdf(-d2) - S * norm_cdf(-d1)
    raise ValueError("kind must be 'call' or 'put'")


def bs_greeks(S, K, T, sigma, rate, kind="call"):
    """Delta, gamma, vega (per 1.00 vol), theta (per year), rho (per 1.00 rate)."""
    if T < EPS_T:
        raise ValueError("Greeks undefined at expiry: report intrinsic and a JTD line")
    d1, d2 = _d1_d2(S, K, T, sigma, rate)
    pdf1, rt = norm_pdf(d1), math.sqrt(T)
    disc_K = K * math.exp(-rate * T)
    out = {"gamma": pdf1 / (S * sigma * rt), "vega": S * pdf1 * rt}
    decay = -S * pdf1 * sigma / (2.0 * rt)
    if kind == "call":
        out.update(delta=norm_cdf(d1), theta=decay - rate * disc_K * norm_cdf(d2),
                   rho=T * disc_K * norm_cdf(d2))
    else:
        out.update(delta=-norm_cdf(-d1), theta=decay + rate * disc_K * norm_cdf(-d2),
                   rho=-T * disc_K * norm_cdf(-d2))
    return out


def implied_vol(price, S, K, T, rate, kind="call", tol_price=1e-6, max_iter=100):
    """Safeguarded Newton. Returns (sigma, status); status is 'ok' or a reason."""
    disc_K = K * math.exp(-rate * T)
    lower = max(S - disc_K, 0.0) if kind == "call" else max(disc_K - S, 0.0)
    upper = S if kind == "call" else disc_K
    if not lower < price < upper:
        return float("nan"), "outside no-arbitrage bounds (stale, American, borrow or crossed)"
    lo, hi = VOL_LO, VOL_HI
    if bs_price(S, K, T, hi, rate, kind) < price:
        return float("nan"), "price needs a vol above VOL_HI"
    sigma = min(max(math.sqrt(2.0 * math.pi / T) * price / S, 0.05), 3.0)  # Brenner-Subrahmanyam
    for _ in range(max_iter):
        diff = bs_price(S, K, T, sigma, rate, kind) - price
        if abs(diff) < tol_price:
            return sigma, "ok"
        if diff > 0.0:
            hi = sigma
        else:
            lo = sigma
        vega = bs_greeks(S, K, T, sigma, rate, kind)["vega"]
        step = sigma - diff / vega if vega > 1e-12 else -1.0
        sigma = step if lo < step < hi else 0.5 * (lo + hi)
    return sigma, "max_iter reached"


@dataclass(frozen=True)
class MeasuredPD:
    """A cumulative default probability that always knows its measure (Law 4)."""
    value: float
    measure: str
    horizon: float

    def __post_init__(self):
        if self.measure not in MEASURES:
            raise ValueError(f"measure must be one of {MEASURES}")
        if not 0.0 <= self.value < 1.0 or self.horizon <= 0.0:
            raise ValueError("need 0 <= PD < 1 and a positive horizon")

    def hazard(self):
        return -math.log1p(-self.value) / self.horizon

    def to_q(self, xi, source):
        """P -> Q through (6B.4), S^Q = (S^P)**xi. Refuses to convert twice."""
        if self.measure != "P":
            raise ValueError("only a P probability converts; this one already holds a premium")
        if xi <= 0.0 or not source:
            raise ValueError("xi must be positive and sourced")
        return MeasuredPD(1.0 - (1.0 - self.value) ** xi, "Q", self.horizon)


def merton(V, F, T, sigma_V, r):
    """Merton (1974): debt = riskless bond - put on assets (sections 6.2, 6-B.3.4)."""
    put = bs_price(V, F, T, sigma_V, r, "put")
    g = bs_greeks(V, F, T, sigma_V, r, "put")
    d1, d2 = _d1_d2(V, F, T, sigma_V, r)
    riskless = F * math.exp(-r * T)
    B = riskless - put
    return {"E": V - B, "B": B, "put": put, "spread": -math.log(B / riskless) / T,
            "pd": MeasuredPD(norm_cdf(-d2), "Q", T),
            "bond_delta": -g["delta"], "bond_gamma": -g["gamma"],
            "bond_vega_per_pt": -g["vega"] / 100.0,
            "spread_vega_bp_per_pt": g["vega"] / (B * T) * 100.0,
            "bond_per_equity": norm_cdf(-d1) / norm_cdf(d1)}


def urc_eur(T, r, lam):
    """European unit recovery claim: $1 at T if default by T."""
    return math.exp(-r * T) * (1.0 - math.exp(-lam * T))


def urc_am(T, r, lam):
    """Unit recovery claim paid at default: the American corridor claim (23.3)."""
    if r + lam <= 0.0:
        return lam * T
    return lam / (r + lam) * (1.0 - math.exp(-(r + lam) * T))


def jtd_price(S, K, T, sigma, r, lam, kind="call"):
    """Merton (1976) with one jump to zero at Q-intensity lam (6B.1)."""
    if kind == "call":
        return bs_price(S, K, T, sigma, r + lam, "call")
    return K * urc_eur(T, r, lam) + bs_price(S, K, T, sigma, r + lam, "put")


def corridor_leak(S, A, B, T, sigma, r, lam):
    """epsilon(A, B) in (6B.2): the diffusive part of a put spread per unit width."""
    upper = bs_price(S, B, T, sigma, r + lam, "put")
    lower = bs_price(S, A, T, sigma, r + lam, "put") if A > 0.0 else 0.0
    return (upper - lower) / (B - A)


def corridor_leak_bound(S, B, T, sigma, r, lam):
    _, d2 = _d1_d2(S, B, T, sigma, r + lam)
    return math.exp(-(r + lam) * T) * norm_cdf(-d2)


def hazard_from_put(put_price, S, K, T, sigma, r, american=True, lam_hi=5.0):
    """Q-intensity of equity wipe-out from a low-strike put (6-B.8): put/K = U(lam)
    + diffusive put at r + lam over K. American early exercise of the diffusive
    part is ignored. The right side increases in lam, so bisection is safe."""
    urc = urc_am if american else urc_eur

    def gap(lam):
        return urc(T, r, lam) + bs_price(S, K, T, sigma, r + lam, "put") / K - put_price / K

    lo, hi = 0.0, lam_hi
    if gap(lo) > 0.0:
        raise ValueError("put is cheaper than its diffusive part: check vol, borrow, quote")
    if gap(hi) < 0.0:
        raise ValueError("put implies a hazard above lam_hi")
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if gap(mid) > 0.0:
            hi = mid
        else:
            lo = mid
    return 0.5 * (lo + hi)


def wing_floor_vol(S, K, T, r, lam):
    """Lower bound (6B.3) on the BS implied vol of a put on a defaultable stock."""
    L = math.log(S * math.exp(r * T) / K)
    if L <= 0.0:
        return 0.0
    c = norm_ppf(math.exp(-lam * T))
    return (-c + math.sqrt(c * c + 2.0 * L)) / math.sqrt(T)


def jump_hedge_ratio(f_S, f_alive, f_dead, S, sigma, lam_P):
    """Min-variance share hedge under P (section 6-B.5.6). Takes lam_P, not lam_Q."""
    j = (f_alive - f_dead) / S
    w = sigma * sigma + lam_P
    delta = (sigma * sigma * f_S + lam_P * j) / w
    resid_var = sigma * sigma * lam_P / w * S * S * (f_S - j) ** 2
    return delta, resid_var


def spread_decomposition(s, lam_Q, lam_P, L_P):
    """(6B.5) in decimals per year; the market's L^Q is implied as s / lam_Q."""
    L_Q = s / lam_Q
    parts = {"expected_loss": lam_P * L_P,
             "hazard_premium": (lam_Q - lam_P) * L_P,
             "recovery_premium": lam_Q * (L_Q - L_P)}
    assert abs(sum(parts.values()) - s) < 1e-12
    parts.update(L_Q=L_Q, xi=lam_Q / lam_P, premium_ratio=s / (lam_P * L_P))
    return parts


def harvest_sharpe(xi, lam_P):
    """(6B.6): single-name Sharpe of selling protection, Poisson approximation."""
    return (xi - 1.0) * math.sqrt(lam_P)


def mc_jtd_put(S, K, T, sigma, r, lam, n_paths=400_000, seed=6):
    """Seeded Monte Carlo of the jump put under Q; returns (price, standard error)."""
    rng = np.random.default_rng(seed)
    z = rng.standard_normal(n_paths)
    if lam > 0.0:
        alive = rng.exponential(1.0 / lam, n_paths) > T
    else:
        alive = np.ones(n_paths, dtype=bool)
    s_T = S * np.exp((r + lam - 0.5 * sigma ** 2) * T + sigma * math.sqrt(T) * z) * alive
    pay = math.exp(-r * T) * np.maximum(K - s_T, 0.0)
    return float(pay.mean()), float(pay.std(ddof=1) / math.sqrt(n_paths))


def _self_test():
    # 1. Put-call parity: the model-free check of the pricer.
    c = bs_price(100.0, 90.0, 1.0, 0.3, 0.04, "call")
    p = bs_price(100.0, 90.0, 1.0, 0.3, 0.04, "put")
    assert abs((c - p) - (100.0 - 90.0 * math.exp(-0.04))) < 1e-10
    # 2. The section 6.2.4 firm and its CCC cousin (table in 6-B.3.4).
    bb = merton(100.0, 80.0, 1.0, 0.25, 0.04)
    assert abs(bb["E"] - 24.78) < 0.02 and abs(bb["spread"] * 1e4 - 216.0) < 1.0
    assert abs(bb["spread_vega_bp_per_pt"] - 26.5) < 0.2
    ccc = merton(100.0, 95.0, 1.0, 0.40, 0.04)
    assert abs(ccc["spread"] * 1e4 - 1307.0) < 2.0 and abs(ccc["bond_per_equity"] - 0.502) < 0.005
    # 3. JTD: reduces to BS at lam = 0, keeps parity, and its floor is the URC.
    assert abs(jtd_price(100, 80, 1.0, 0.3, 0.04, 0.0, "put") - bs_price(100, 80, 1.0, 0.3, 0.04, "put")) < 1e-12
    cj = jtd_price(100, 80, 1.0, 0.3, 0.04, 0.05, "call")
    pj = jtd_price(100, 80, 1.0, 0.3, 0.04, 0.05, "put")
    assert abs((cj - pj) - (100.0 - 80.0 * math.exp(-0.04))) < 1e-10
    assert abs(jtd_price(100, 1.0, 1.0, 0.3, 0.04, 0.05, "put") - urc_eur(1.0, 0.04, 0.05)) < 1e-6
    # 4. Implied vols of jump puts round-trip and respect the wing floor (6B.3).
    for K in (40.0, 60.0, 100.0):
        target = jtd_price(100.0, K, 1.0, 0.3, 0.04, 0.05, "put")
        iv, status = implied_vol(target, 100.0, K, 1.0, 0.04, "put")
        assert status == "ok" and iv >= wing_floor_vol(100.0, K, 1.0, 0.04, 0.05) - 1e-9
    # 5. The $1 put on a $6 stock (6-B.5.4): the leak sits inside its bound.
    leak = corridor_leak(6.0, 0.0, 1.0, 1.0, 0.8, 0.04, 0.145)
    assert 0.0 <= leak <= corridor_leak_bound(6.0, 1.0, 1.0, 0.8, 0.04, 0.145)
    assert abs(leak - 0.0037) < 0.0005
    # 6. Halvorsen (6-B.8): put -> lam_Q; decomposition; the measure guard bites.
    lam_Q = hazard_from_put(0.136, 6.0, 1.0, 1.0, 0.8, 0.04, american=True)
    assert abs(lam_Q - 0.145) < 0.01
    pd_P = MeasuredPD(0.06, "P", 1.0)
    dec = spread_decomposition(0.115, 0.145, pd_P.hazard(), 0.60)
    assert abs(dec["L_Q"] - 0.793) < 0.001 and abs(dec["xi"] - 2.34) < 0.01
    try:
        MeasuredPD(0.10, "Q", 1.0).to_q(2.0, "Driessen 2005")
        raise AssertionError("a Q -> Q conversion must be refused")
    except ValueError:
        pass
    # 7. Monte Carlo agrees with (6B.1) within four standard errors.
    mc, se = mc_jtd_put(100.0, 80.0, 1.0, 0.3, 0.04, 0.05)
    assert abs(mc - jtd_price(100.0, 80.0, 1.0, 0.3, 0.04, 0.05, "put")) < 4.0 * se
    return "credit_options self-test passed"


print(_self_test())
```

> **Ways This Blows Up.** `1 - norm_cdf(9)` is exactly 0.0 in double precision and `norm_cdf(-9)` is not, so every tail is computed on its small side. `bs_greeks` returns vega per 1.00 of vol and the risk report shows it per point: the factor of 100 is the commonest unit bug in vol code.

Used in: §8.3 and §8.8 (bond-to-equity sensitivities), §11.3 (structural PDs, tagged $\mathbb{P}$), §15.2–15.3 (`Q_nominal` digitals), §16.3–16.4 (backstops and warrants), §21.4 (pool Greeks), §23.2–23.5 (the surface engine imports `jtd_price`, `hazard_from_put` and `implied_vol`), §28.4.
