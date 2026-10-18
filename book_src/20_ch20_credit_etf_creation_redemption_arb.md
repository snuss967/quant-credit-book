# Chapter 20: Credit ETF Creation/Redemption Arbitrage (HYG, JNK, LQD, BKLN)

*3:41 p.m., the Thursday of a bad week. Every number in this scene is illustrative.*

HYG was 77.10 bid. The intraday NAV estimate beside it said 77.82. Theo had done the arithmetic before he finished reading the ticker. "Ninety-three basis points," he said. "Buy the ETF, hand the shares back to the fund, take the bonds, sell the bonds. That's an arbitrage. That's the thing the textbook says can't exist."

"It is an arbitrage," Kaz agreed. "The ETF is a portfolio, the portfolio is worth the NAV, and the law of one price does the rest. Let's just assume the NAV is—"

"Don't," said Ines, without looking up. "What's the pot, what are the odds, and who at this table knows more than you?"

"The pot is ninety-three bips on whatever size we do."

"The odds depend on whether 77.82 is a price or a rumor. It's the bid side of a pricing service's opinion of thirteen hundred bonds, half of which haven't traded since Tuesday. And the person who knows more than you is whoever is selling HYG at 3:41 instead of selling bonds. Ask yourself why they aren't selling the bonds."

"Because they tried at 3:30," said Mags, from across the row.

Theo pulled up the redemption basket the fund had published that morning. It was not the fund. It was 212 bonds out of 1,300, skewed short and wide, and it included a chemicals issuer he had last seen in a forbearance agreement.

Kaz leaned over. "It says 'custom basket.' Is it artisanal? Does it come with a little jar of jam?"

"It comes with the bonds nobody else wants," Mags said. "Back in my day the redemption basket was a fund manager calling you at 4:15 to ask what you'd pay for his whole high yield book. The answer was 'less.' This is better. It's still less."

Theo looked at the chemicals name again, then at the 93 bp. It was a consent fee, he realized. Somebody always pays to turn a promise into cash, and the fee goes to whoever holds the scarce thing. Here the scarce thing was a balance sheet willing to own 212 bonds overnight.

"So," Ines said. "Is the ETF cheap, or is the NAV late?"

That is the question this chapter answers. *When a credit ETF trades away from its net asset value, how much of the gap is mispricing, how much is accounting, and how much is a fee for somebody else's liquidity? And what does it cost to make the gap close?*

By the end of this chapter you will be able to:

- explain the primary and secondary markets of a credit ETF in the language of Rule 6c-11;
- decompose an observed premium into a flow component, a staleness component and a bid-side accounting constant, and estimate how stale the NAV is from public data;
- derive the creation/redemption no-arbitrage band from bond-level liquidity costs, and extend it to a risk-averse AP whose balance sheet is the binding constraint;
- solve the custom-basket problem as a constrained quadratic program and say who gains and who pays;
- replay March 2020, the SMCCF and the loan-ETF settlement problem through those equations;
- hand ROBO a spec for an arbitrage-band monitor that does not mistake a late NAV for free money.

## 20.1 The Machine: Two Markets, One Wrapper

A credit ETF is two markets bolted together.

In the **secondary market**, shares trade on an exchange among anyone with a brokerage account, a market maker or, in 2020, a Federal Reserve special purpose vehicle. The price is set by supply and demand for *shares*. Nothing about a secondary-market trade touches a bond.

In the **primary market**, a small club of **authorized participants** (APs) trades with the fund itself. They trade in large blocks of shares called **creation units**, in exchange for a **basket** of bonds (or cash) plus a small **cash balancing amount**. The primary market is where shares are born and where they die. The arbitrage lives in the gap between the two markets.

Since 2019 the vocabulary has been statutory. Rule 6c-11 under the Investment Company Act (17 CFR 270.6c-11(a)(1)) defines an authorized participant as "a member or participant of a clearing agency registered with the Commission" that has a written agreement with the fund to place creation and redemption orders. It defines a basket as "the securities, assets or other positions in exchange for which an exchange-traded fund issues" (or redeems) creation units. A creation unit is "a specified number of exchange-traded fund shares that the exchange-traded fund will issue to (or redeem from)" an AP. The cash balancing amount is "an amount of cash to account for any difference between the value of the basket" and the NAV of the creation unit. Hold on to one more definition, because §20.4 is built on it. A **custom basket** is either "a basket that is composed of a non-representative selection of the exchange-traded fund's portfolio holdings," or a representative basket that differs from the initial basket used earlier that business day.

The two trades are mirror images.

- **Creation (the ETF is rich).** The AP buys the bonds in the creation basket, delivers them to the fund with the cash balancing amount, receives a creation unit of new shares, and sells those shares on the exchange. Shares outstanding go up.
- **Redemption (the ETF is cheap).** The AP buys shares on the exchange, delivers a creation unit to the fund, receives the redemption basket, and sells the bonds. Shares outstanding go down.

Some funds transact **in cash** rather than in kind, for some or all orders. The fund then buys or sells the bonds itself and charges the AP a transaction fee to cover the cost, which matters enormously for loans (§20.6).

For a restructuring banker, the cleanest analogy is a convertible. An ETF share is convertible into a slice of the bond portfolio, and the bonds are convertible back into shares. The conversion right sits with a small club, and exercising it costs money. Everything in this chapter follows from asking the questions you would ask about any conversion right: *who holds it, what does it cost to exercise, and what do they do with the thing they receive?*

The club is not large, but it is not tiny either. Using Form N-CEN data, BlackRock counted 37 different APs active in US-listed ETFs in 2019, with about 5 active APs per ETF on average. In March 2020, 24 APs created or redeemed iShares US ETFs, against 28 active in 2019. The AP with the largest share of creations and redemptions accounted for less than a quarter of activity by dollar value (BlackRock, *Lessons from COVID-19: ETFs as a Source of Stability*, ViewPoint, July 2020, pp. 3–4). Most of the activity, however, never reaches the club at all. ICI's 2025 Fact Book puts about 83% of domestic high-yield bond ETF activity in the secondary market, so only about 17% involves creation or redemption. Most ETF trades are just investors swapping risk with each other, which is the whole point.

Here are the four funds in the chapter title, as their issuers reported them in mid-October 2026.

| ETF | Inception | AUM | Holdings | Expense ratio | 30-day median bid/ask | Premium/discount | Index |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| HYG (iShares iBoxx \$ High Yield Corporate Bond) | 2007-04-04 | \$17.18bn | 1,334 | 0.49% | 0.01% | +0.02% | iBoxx USD Liquid High Yield |
| LQD (iShares iBoxx \$ Investment Grade Corporate Bond) | 2002-07-22 | \$28.78bn | 3,171 | 0.14% | 0.01% | +0.04% | iBoxx USD Liquid Investment Grade |
| JNK (SPDR Bloomberg High Yield Bond) | 2007-11-28 | \$5.72bn | 1,161 | 0.40% | 0.01% | +0.15% | Bloomberg High Yield Very Liquid |
| BKLN (Invesco Senior Loan) | 2011-03-03 | about \$6.16bn *(secondary source; CHECK)* | 185 | 0.65% | n/a | n/a | Morningstar LSTA US Leveraged Loan 100 |

*Sources: iShares HYG and LQD product pages (as of 2026-10-16); SSGA JNK page (as of 2026-10-15); Invesco BKLN case study; BKLN AUM from stockanalysis.com (2026-10-16), not yet confirmed against Invesco.*

Two things in that table deserve a second look. First, HYG's 30-day median bid/ask is 0.01%, which is tighter than any bond it holds. That is not an error, and §20.2 explains why a regulator requires the fund to publish it. Second, BKLN holds 185 loans that settle on a timetable measured in days or weeks, while its shares settle T+1. That mismatch is the subject of §20.6.

Why is the primary market so small relative to the secondary market? Because the secondary market nets. On a heavy selling day the ETF changes hands thousands of times, and buyers and sellers mostly meet each other. Only the *net imbalance*, after market makers have warehoused what they will, reaches an AP. BlackRock's July 2020 ViewPoint (p. 5) put the gap starkly: "the largest high yield bond ETF traded over 168,000 times per day during the week of March 23 to March 27, while the fund's largest five bond holdings traded an average of 25 times per day." The ETF is a netting machine sitting on top of an RFQ market, and it nets a great deal.

> **Desk Myth vs. Desk Reality.** *Myth:* "The ETF makes high yield bonds liquid." *Reality:* the ETF makes high yield *risk* liquid. The bonds are exactly as illiquid as before. When ETF holders and bondholders need to meet, someone pays the bill: the AP in its spread, the redeeming investor in the discount, or the remaining shareholders through the basket. The whole chapter is an accounting of who that someone is.

> **[SOURCE EXTRACTION]** *Man_Quantitative_Credit_Alpha_Early_Mover_2022 p.4:* "(through a combination of ETFs, which are essentially passive quant investing, and more than one third by funds pursuing more active quantitative investing mandates)"
>
> **Annotation.** Man is describing US equity ownership, where "passive" is almost literally true: an S&P 500 ETF can create and redeem in a basket that is the index, to the share. A credit ETF is passive in its *objective* (track the iBoxx or Bloomberg index) and furiously active in its *execution*. The fund cannot buy 1,300 high yield bonds pro rata every time an AP shows up, so it chooses daily which subset to accept and which to deliver. Koont, Ma, Pástor and Zeng call it, in their title, "Active Management of Passive Funds" (NBER w30039, 2022; *RFS* 2025). The 2026 desk should treat a credit ETF as a quant strategy with a published rulebook and a discretionary trading desk attached. The rulebook is the index. The discretion is the basket, and the basket is where the alpha and the costs live.

> **Trend Watch: the wrapper eats the bond market (2019–2026).** *What changed:* on 2019-09-26 the SEC adopted Rule 6c-11, which lets ETFs that meet its conditions "come directly to market without the cost and delay of obtaining an exemptive order." At adoption there were about 2,000 ETFs with more than \$3.3 trillion in net assets, and the SEC had issued more than 300 exemptive orders since 1992 (SEC press release 2019-190). The rule became effective on 2019-12-23 (Release 33-10695). *How big:* bond ETF assets passed \$1.2 trillion in early 2021 (Shim & Todorov, BIS WP 975, 2021). US bond ETFs held \$1.8 trillion at end-2024, 17% of all ETF assets, with net issuance of \$295bn in 2024 against \$201bn in 2023 (ICI 2025 Fact Book, pp. 59–63). Secondary coverage of State Street data reported bond ETF assets above \$2.5 trillion and a record \$64bn monthly bond ETF inflow in May 2026 *(Advisor Perspectives, 2026-06-05; CHECK against State Street's own release)*. *Inside the category:* by October 2026, LQD held \$28.78bn but HYG only \$17.18bn, well below its 2020 size *(peak figure CHECK)*, as high-yield money moved toward cheaper broad-market HY ETFs. *What it means:* the ETF is no longer a side door into credit. It is a main entrance, and its primary market is now a standing source of basket-shaped demand for the cash bonds. That demand is what portfolio-trading desks recycle (Chapter 19).

## 20.2 NAV Is an Opinion: Price, Evaluated Prices and the Bid Side

An equity ETF's NAV is a sum of closing prices from a continuous auction. A bond ETF's NAV is a sum of *evaluated prices*: model-based marks from third-party pricing services, built from whatever trades, dealer quotes and comparable bonds were available. Most of the 1,334 bonds in HYG did not trade at size today. Their marks are an informed opinion about where they would trade.

Three features of that opinion matter for the arbitrage.

1. **It is struck on the bid side.** For most US bond ETFs the NAV uses bid-side evaluated prices, while the ETF itself is quoted, and closes, near the midpoint of its own tight market. Vanguard's adviser education material and Morningstar both describe the convention, and both conclude that bond ETFs therefore *tend* to trade at a small premium to NAV in normal markets (Vanguard, "4 things to know about bond ETFs"; Morningstar, "NAV premiums and discounts"). A few funds use mid prices, so check the prospectus fund by fund before you hard-code it. JNK's own page shows the footprint: in 2025 it closed at a premium on 206 days and at a discount on 44 (SSGA, accessed 2026-10-15).
2. **It is struck at a time.** ICE has noted that a bond NAV may be struck at 3 p.m. while the exchange closes at 4 p.m. (ICE Data Services via FOW, 2020-06-22). A rally between 3 and 4 shows up as a "premium" that is really just the clock.
3. **It is slow.** An evaluated price moves when the evaluator sees evidence. In a fast market evidence arrives late, so the mark lags the true clearing level.

Regulators know all of this, and Rule 6c-11 responds with disclosure. Every ETF must publish, daily, its NAV, market price and premium or discount as of the prior close, plus a "median bid-ask spread, expressed as a percentage rounded to the nearest hundredth," computed over the last 30 calendar days. And "if the exchange-traded fund's premium or discount is greater than 2% for more than seven consecutive trading days," the fund must say so on its website and discuss the contributing factors, for at least a year (17 CFR 270.6c-11(c)(1)). That is why every issuer page shows a median bid/ask of 0.01%. The rule mandated a statistic that makes the fund look more liquid than anything it owns, and the statistic is correct, which is the joke.

### 20.2.1 Derivation: three reasons a price differs from a NAV

Let the fund hold $n_i$ units of bond $i = 1, \dots, N$ per ETF share (ignore cash, accrued interest and fees for now; they add a known constant). Let $m_{i,t}$ be the true executable mid price of bond $i$ at the NAV strike time on day $t$. It exists in principle and is never observed directly. The pricing service publishes an evaluated mid $\tilde m_{i,t}$ and an evaluated bid $\tilde m_{i,t}(1 - c_i)$, where $c_i$ is bond $i$'s half bid–offer as a fraction of price. Define the per-share aggregates

$$
M_t = \sum_{i=1}^{N} n_i\, m_{i,t}, \qquad \tilde M_t = \sum_{i=1}^{N} n_i\, \tilde m_{i,t}, \qquad \text{NAV}_t = \sum_{i=1}^{N} n_i\, \tilde m_{i,t}(1 - c_i) = \tilde M_t\,(1 - \bar c_t),
$$

where $\bar c_t = \sum_i n_i \tilde m_{i,t} c_i / \tilde M_t$ is the value-weighted half-spread of the portfolio. Let $P_t$ be the ETF's closing price (the midpoint of its own bid and ask). The premium is $\pi_t = P_t / \text{NAV}_t - 1$; we work with the log premium $p_t = \ln(P_t/\text{NAV}_t)$, which equals $\pi_t$ to first order.

Multiply and divide by $M_t$ and $\tilde M_t$, and take logs:

$$
p_t \;=\; \underbrace{\ln \frac{P_t}{M_t}}_{\ell_t \;(\text{flow})} \;+\; \underbrace{\ln \frac{M_t}{\tilde M_t}}_{s_t \;(\text{staleness})} \;+\; \underbrace{-\ln\left(1 - \bar c_t\right)}_{\approx\, \bar c_t \;(\text{bid-side convention})}. \tag{20.1}
$$

Equation (20.1) is an identity. It needs no assumptions, which is why it is useful: every argument about bond ETF premiums is an argument about which of the three terms is large.

- $\ell_t$ is the **flow term**: the ETF price differs from the true value of what it holds. This is the only term an AP can arbitrage, and only within the band of §20.3.
- $s_t$ is the **staleness term**: the true value differs from the pricing service's opinion. Nobody can arbitrage it, because nobody can trade at the evaluated price. It is a *forecast*: the NAV will move toward the ETF.
- $\bar c_t$ is the **accounting term**: a near-constant positive premium created by marking at the bid. For an IG fund with a value-weighted half-spread of 10 bp it is about 10 bp; for an HY fund at 30 bp it is about 30 bp *(illustrative magnitudes)*.

Now give staleness a model. The simplest one that matches how evaluators behave is **partial adjustment**: each day the evaluated level closes a fraction $\eta \in (0, 1]$ of the gap to the truth,

$$
\ln \tilde M_t = \ln \tilde M_{t-1} + \eta\,\left(\ln M_t - \ln \tilde M_{t-1}\right).
$$

Subtract both sides from $\ln M_t$, and write $r_t = \ln M_t - \ln M_{t-1}$ for the true log return:

$$
s_t = \ln M_t - \ln \tilde M_t = (1 - \eta)\left(\ln M_t - \ln \tilde M_{t-1}\right) = (1 - \eta)\left(s_{t-1} + r_t\right).
$$

Iterating backwards,

$$
s_t = \sum_{j=0}^{\infty} (1 - \eta)^{j+1}\, r_{t-j}. \tag{20.2}
$$

Staleness is an exponentially weighted sum of recent true returns. If true returns are i.i.d. with mean zero and variance $\sigma_r^2$ under $\mathbb{P}$, then $\mathbb{E}^{\mathbb{P}}[s_t] = 0$ and

$$
\operatorname{Var}^{\mathbb{P}}(s_t) = \sigma_r^2 \sum_{j=0}^{\infty} (1-\eta)^{2(j+1)} = \frac{(1-\eta)^2}{1 - (1-\eta)^2}\,\sigma_r^2 = \frac{(1-\eta)^2}{\eta\,(2 - \eta)}\,\sigma_r^2.
$$

The boundary cases check out. At $\eta = 1$ the evaluator is perfectly fresh and $s_t \equiv 0$. As $\eta \to 0$ the variance explodes: a NAV that never updates eventually differs from the truth by the entire cumulative return.

The stress case is a single large move. If the portfolio's true value falls 5% in one day and the evaluator closes half the gap ($\eta = 0.5$), then $s_t = 0.5 \times (-5\%) = -2.5\%$. The NAV overstates value by 2.5%, so an ETF priced *exactly* at fair value prints a 2.5% discount *(illustrative)*. The ETF isn't at a discount. The NAV is at a premium. It's the same number with a different villain.

### 20.2.2 Measuring staleness: does the NAV catch up?

Equation (20.2) has a testable implication. The NAV's own log return is

$$
\Delta \ln \text{NAV}_t = \Delta \ln \tilde M_t - \Delta \ln(1 - \bar c_t) = \eta\,\left(s_{t-1} + r_t\right) - \Delta \ln(1 - \bar c_t).
$$

Suppose the flow term is small ($\ell_t \approx 0$) and the spread is stable ($\bar c_t \approx \bar c$). Then (20.1) gives $s_{t-1} = p_{t-1} - \bar c$, and

$$
\Delta \ln \text{NAV}_t = \eta\, (p_{t-1} - \bar c) + \eta\, r_t. \tag{20.3}
$$

Regress the NAV's daily log return on yesterday's log premium. The slope estimates $\eta$, the speed at which the NAV catches up to the ETF, and the intercept estimates $-\eta \bar c$. Under i.i.d. true returns, $r_t$ is uncorrelated with $p_{t-1}$, so ordinary least squares is consistent. This is the regression version of a finding that Shim and Todorov (BIS WP 975, 2021) report for ETFs with fractional baskets: persistent premiums and discounts, linked to NAV returns that adjust slowly to ETF returns.

Two caveats keep the regression honest. First, if the flow term is not negligible and is independent of staleness, then $p_{t-1} - \bar c = s_{t-1} + \ell_{t-1}$, and the slope is attenuated to

$$
\hat\eta \;\to\; \eta \cdot \frac{\operatorname{Var}(s)}{\operatorname{Var}(s) + \operatorname{Var}(\ell)}.
$$

The slope is therefore $\eta$ times the staleness share of premium variance. A small slope can mean a fresh NAV or a noisy ETF, and you need a second instrument (the ETF's own lagged returns, or a matched fund) to tell which. Second, $\bar c_t$ is not constant in stress: spreads widen, so $-\Delta \ln(1 - \bar c_t)$ becomes a negative drag on NAV returns exactly when you are running the regression. Estimate on calm windows, then test whether $\eta$ falls in stress.

### 20.2.3 The three readings of a discount

In March 2020, three serious readings of the same discount appeared, and each one is a claim about which term of (20.1) dominated.

**Reading one: the ETF was the price, and the NAV was late ($s_t$ dominates).** BlackRock's ViewPoint argued that the largest US floating-rate bond ETF, which closed at an 8% discount on March 12, was "acting as a price discovery vehicle" because many of its underlying bonds "had not traded over the period." The SEC staff's October 2020 credit-markets report noted that "ETF market prices are viewed by some market participants as a more reliable indicator of actionable value than the ETF's NAV."

**Reading two: the ETF was what people could sell ($\ell_t$ dominates).** Haddad, Moreira and Muir ("When Selling Becomes Viral," NBER w27168, 2020; *RFS* 2021) found the largest discounts in Treasury, municipal and IG ETFs, not in high yield, and wrote: "there was no discount in high yield in mid March when there was a large discount for the other categories ... This is evidence against a pure price staleness story." Staleness should be worst in the least liquid bonds, so if staleness were the whole story, HY should have shown the deepest discount. Instead, investors sold the safest liquid wrappers to raise cash, pushing $\ell_t$ deeply negative where the selling was concentrated.

**Reading three: there was no single "true" value ($M_t$ is an interval).** MSCI (Bohák & Janosik, 2020-04-08) documented that same-day traded-price dispersion in IG bonds peaked on March 19, the day LQD closed at a 5.08% discount. If identical bonds trade at prices several points apart on the same afternoon, $M_t$ is a band of width $2u_t$, not a number. A premium with $|p_t - \bar c| < u_t$ is not statistically distinguishable from zero.

All three readings are right about something, and the desk does not have to choose among them. Equation (20.1) is the bookkeeping that lets you hold all three at once. Staleness is estimated with (20.3), measurement width with same-day TRACE dispersion, and whatever is left is flow. Only the flow term is a trade.

> **[SOURCE EXTRACTION]** *Man_Quantitative_Credit_Alpha_Early_Mover_2022 p.9:* "The rise of passive bond ETFs has potentially created further distortions that will drive pricing away from fundamentals and produce opportunities for active investment strategies."
>
> **Annotation.** Equation (20.1) tells you where to look for those distortions. The staleness term creates a predictable component in *bond* marks: when HYG trades 2% below NAV on a fast down day, the evaluated prices of its constituents will very probably fall tomorrow. That matters to anyone whose performance, collateral or risk limits are struck on evaluated prices. The flow term creates temporary pressure on the bonds that appear in redemption baskets (§20.4), which is a short-horizon reversal opportunity for anyone with a balance sheet. And the basket choice itself, the "active management of passive funds," creates persistent liquidity differences between bonds that are in baskets and bonds that are not. The modern desk departs from the 2022 framing in one respect. These are not mainly *fundamental* mispricings to hold for months. They are *plumbing* mispricings that decay in days, and they belong to whoever can bear basket risk overnight at the lowest cost.

## 20.3 The Arbitrage Band, Derived

An options market maker would describe the AP's position in one sentence: it owns a call and a put on the ETF's premium, and the strikes are the costs of creation and redemption. Inside the strikes the ETF price can wander wherever secondary-market supply and demand push it. Outside them, someone exercises, and the exercise pushes the price back toward the band. The band is the most important object in this chapter, so we derive it twice: once with costs as constants, and once with a balance sheet that charges for risk.

### 20.3.1 The static band

Work per \$1 of NAV and per creation unit, and write every cost as a fraction of NAV:

- $f^C, f^R$: the fund's fixed creation and redemption transaction fees, divided by the creation unit's value;
- $c^C, c^R$: the value-weighted half-spreads of the *creation* and *redemption* baskets (which need not equal the portfolio's $\bar c$);
- $k^C, k^R$: everything else, meaning market impact beyond the half-spread, financing over the settlement gap, and the risk premium of §20.3.2.

Assume a calm market, so the evaluated mid is the true mid ($s_t = 0$ in (20.1)).

**Creation.** The AP buys the creation basket at the offer, $\tilde M_t(1 + c^C)$ per share, delivers it, and sells the new shares at $P_t$. Its profit per \$1 of NAV is

$$
\Pi^C_t = \frac{P_t - \tilde M_t(1 + c^C)}{\text{NAV}_t} - f^C - k^C = (1 + \pi_t) - \frac{1 + c^C}{1 - \bar c} - f^C - k^C \approx \pi_t - \left(\bar c + c^C\right) - f^C - k^C,
$$

using $\text{NAV}_t = \tilde M_t(1 - \bar c)$ and $\frac{1 + c^C}{1 - \bar c} \approx 1 + c^C + \bar c$ to first order in the spreads.

**Redemption.** The AP buys shares at $P_t$, redeems them, and sells the redemption basket at the bid, $\tilde M_t(1 - c^R)$:

$$
\Pi^R_t = \frac{\tilde M_t(1 - c^R) - P_t}{\text{NAV}_t} - f^R - k^R \approx \left(\bar c - c^R\right) - \pi_t - f^R - k^R.
$$

No arbitrage means neither trade is profitable, $\Pi^C_t \le 0$ and $\Pi^R_t \le 0$:

$$
\underbrace{\left(\bar c - c^R\right) - f^R - k^R}_{\pi^{\text{lo}}} \;\le\; \pi_t \;\le\; \underbrace{\left(\bar c + c^C\right) + f^C + k^C}_{\pi^{\text{hi}}}. \tag{20.4}
$$

Read (20.4) three ways.

1. **With pro rata baskets** ($c^C = c^R = \bar c$), the band is $-f^R - k^R \le \pi_t \le 2\bar c + f^C + k^C$. Its width, $2\bar c + f^C + f^R + k^C + k^R$, is the round-trip cost of the portfolio and does not depend on the NAV convention. Its *center*, $\bar c + \tfrac12(f^C + k^C - f^R - k^R)$, does. With a mid-price NAV the band would be symmetric around zero, $-\bar c - f^R - k^R \le \pi_t \le \bar c + f^C + k^C$. Bid-side marking slides the whole band up by $\bar c$. That is the entire reason a calm high yield ETF "trades at a premium." It is not demand. It is a decimal point in the valuation policy.
2. **The premium's position inside the band reveals the flow regime.** In steady inflows, APs create at the margin and the premium sits near $\pi^{\text{hi}}$. In steady outflows it sits near $\pi^{\text{lo}}$. A band that starts near zero and extends to $2\bar c$ above it produces many more premium days than discount days, which is JNK's 206-to-44 record for 2025.
3. **Custom baskets move the two edges independently.** A creation basket of tight bonds ($c^C < \bar c$) lowers $\pi^{\text{hi}}$, so creations become cheaper. A redemption basket of wide bonds ($c^R > \bar c$) lowers $\pi^{\text{lo}}$, so the discount must be deeper before redemption pays. The fund's liquidity management therefore shows up directly in the price: the fund exports its illiquidity to the AP, and the AP charges for it through the discount.

Put in numbers *(all illustrative)*. A high yield fund with $\bar c = 30$ bp, a redemption basket at $c^R = 45$ bp, a pro rata creation basket, fees of 1 bp each way and $k = 5$ bp has $\pi^{\text{lo}} = 30 - 45 - 1 - 5 = -21$ bp and $\pi^{\text{hi}} = 30 + 30 + 1 + 5 = 66$ bp. An IG fund with $\bar c = 8$ bp, $c^R = 10$ bp, fees of 1 bp and $k = 3$ bp has $\pi^{\text{lo}} = -6$ bp and $\pi^{\text{hi}} = 20$ bp. Both are consistent with the small positive premiums on the issuer pages in §20.1. In the cold open, HYG's 93 bp discount is far outside any calm-market band, which tells you that $k^R$, the term we have been treating as a constant, is not one.

**The cash-redemption wrinkle.** When a fund redeems in cash, it sells the bonds itself and charges the AP a variable fee to cover the cost. That fee has a ceiling. BlackRock's ViewPoint (p. 6) notes that under the 1940 Act "the amount funds can charge to APs on redemptions to mitigate against the potential dilutive impact of cash redemptions is capped at 2% of the value of the shares redeemed," and that above that level "the excess would be absorbed by the ETF to the detriment of the ETF's remaining shareholders." In (20.4), the AP's redemption cost $f^R$ is capped at 2% even when the true liquidation cost is higher. The lower edge of the band then stops at about $-2\%$ plus whatever the AP charges for risk, and the remainder of the cost moves to the people who stayed in the fund. That is a first-mover advantage, which is the textbook ingredient of a run. Keep it in mind for loans (§20.6).

> **[SOURCE EXTRACTION]** *Dynkin_Systematic_Investing_in_Credit p.702:* "LCS measures the cost of an immediate round-trip transaction of a typical institutional size and is expressed as a percentage of a bond price ... For bonds quoted on spread, LCS is calculated as a product of bid–offer spread and spread duration."
>
> **Annotation.** This is $2c_i$ in (20.4), already computed for you. For an IG bond quoted on spread, a 6 bp bid–offer on a bond with $D^{\text{spr}} = 7$ gives an LCS of 42 bp of price, so $c_i = 21$ bp. For a high yield bond quoted on price, LCS is simply the offer minus the bid, as a percentage of price. Value-weight the half-LCS across the basket and you have $c^C$, $c^R$ and $\bar c$, and therefore both edges of the static band, from data a systematic desk already holds. The 2026 desk departs from the textbook in two ways. First, LCS describes an *immediate* trade of *typical* size, while an AP liquidating a 212-bond redemption basket is trading neither immediately nor at typical size. The size and time terms live in $k^R$, and §20.3.2 prices them. Second, LCS was built on one dealer's two-way quotes. In a market that is now about half electronic in IG and about a third in HY, the better input is a composite of streaming and RFQ prices, but the formula is the same.

### 20.3.2 The band with a balance sheet

In calm markets, $k$ is a few basis points and the static band is the whole story. In stress, $k$ is almost all of the story, and almost all of $k$ is the price of *risk*. Between buying ETF shares and selling the last bond of a redemption basket, the AP owns a bond position it did not choose. It can hedge the market component with CDX HY, index futures or the ETF itself, but the residual (basket minus hedge) remains on its books until the bonds are sold.

Model that residual. Let $X$ be the NAV value, in dollars, of one creation unit. Let $Q \ge 0$ be the number of creation units an AP redeems ($Q$ is a count of units, not the measure $\mathbb{Q}$). Let $T^{\text{h}}$ be the holding period in years until the basket is sold, and let $\sigma_b$ be the annualized volatility of the hedged basket's return, the **basis volatility**. Write $\kappa^R = f^R + c^R - \bar c$ for the static redemption cost from (20.4), so that the AP's edge per dollar is $e_t = -\pi_t - \kappa^R$. A mean-variance AP with risk aversion $\gamma$ (per dollar) maximizes

$$
U(Q) = Q X\, e_t - \frac{\gamma}{2}\, Q^2 X^2 \sigma_b^2\, T^{\text{h}}.
$$

The first-order condition $X e_t - \gamma Q X^2 \sigma_b^2 T^{\text{h}} = 0$ gives

$$
Q^* = \frac{(e_t)^+}{\gamma\, X\, \sigma_b^2\, T^{\text{h}}}, \qquad X Q^* = \frac{(e_t)^+}{\gamma\, \sigma_b^2\, T^{\text{h}}},
$$

where $(\cdot)^+ = \max(\cdot, 0)$ because an AP never redeems at a loss. The second-order condition holds because $U''(Q) = -\gamma X^2 \sigma_b^2 T^{\text{h}} < 0$.

Now let $J$ APs, with risk aversions $\gamma_1, \dots, \gamma_J$, face the same edge. Their combined redemptions, in dollars, are

$$
\sum_{j=1}^{J} X Q_j^* = \frac{(e_t)^+}{\sigma_b^2\, T^{\text{h}}} \sum_{j=1}^{J} \frac{1}{\gamma_j} = \frac{(e_t)^+}{\bar\gamma\, \sigma_b^2\, T^{\text{h}}}, \qquad \bar\gamma \equiv \left(\sum_{j=1}^{J} \gamma_j^{-1}\right)^{-1}.
$$

The street's risk tolerance is the sum of its members' risk tolerances, so $\bar\gamma$ is the aggregate risk aversion. Finally, clear the market. Suppose investors sell $F$ dollars of the ETF, net, that secondary-market liquidity providers will not hold overnight. That amount must be redeemed, so $F = (e_t)^+ / (\bar\gamma \sigma_b^2 T^{\text{h}})$. Solving for the premium,

$$
\pi_t^* = -\kappa^R - \psi\, F, \qquad \psi \equiv \bar\gamma\, \sigma_b^2\, T^{\text{h}}. \tag{20.5}
$$

$\psi$ is the price impact of the AP channel: discount per dollar of net selling. Check the units: $\bar\gamma$ is per dollar, $\sigma_b^2 T^{\text{h}}$ is dimensionless, and $F$ is in dollars, so $\psi F$ is a pure number, as a premium must be. Equation (20.5) has the same shape as Kyle's $\lambda$ from Chapter 18, and $\psi F$ is the same expression as the inventory "fear" term $\gamma \sigma^2 \tau q$ in the Avellaneda–Stoikov quotes. The source of the impact is different: Kyle's dealer fears the informed trader, while the AP fears the basket. The AP is a market maker whose inventory happens to be a portfolio.

Three corollaries make (20.5) useful on a desk.

**(a) Stress multiplies; it does not add.** The ratio of stressed to calm price impact is

$$
\frac{\psi^{\text{stress}}}{\psi^{\text{calm}}} = \frac{\bar\gamma^{\text{stress}}}{\bar\gamma^{\text{calm}}} \cdot \left(\frac{\sigma_b^{\text{stress}}}{\sigma_b^{\text{calm}}}\right)^{2} \cdot \frac{T^{\text{h, stress}}}{T^{\text{h, calm}}}.
$$

Suppose risk aversion doubles, basis volatility goes from 2% to 12% annualized (a factor of 36 in variance), and the time to work out a basket goes from 2 days to 8 days. The multiplier is $2 \times 36 \times 4 = 288$ *(illustrative)*. A flow that cost 1 bp of discount in February costs about 2.9% in March. That is the order of magnitude of the IG ETF discounts of March 2020, and producing it requires no story in which the arbitrage "broke." The arbitrage worked, at a price.

**(b) The AP count is second-order.** With $J$ identical APs, $\bar\gamma = \gamma / J$. Going from 28 active APs to 24 raises $\bar\gamma$, and so $\psi$, by $28/24 - 1 \approx 17\%$. Compare that with the factor of 36 from basis volatility. BlackRock's observation that APs did not step away in March 2020 is correct, and it is also beside the point. They stayed and charged more, because each unit of their balance sheet had become more expensive.

**(c) Basis risk is the lever the fund controls.** $\sigma_b$ is the volatility of the redemption basket relative to whatever the AP can hedge with. A basket that looks like CDX HY is cheap to hold, while a basket of short, wide, idiosyncratic bonds is expensive. The fund would like to deliver exactly those bonds, to protect the shareholders who remain. That tension is §20.4.

> **Poker Table.** Ines put it in terms Theo could not argue with. "The AP's right to redeem is an option, not an obligation. It's a player who sees the board and chooses whether to call. In February it calls every hand worth three basis points. In March it folds everything under three percent. Nobody left the table. The price of calling changed. When you look at a discount, don't ask whether the arbitrage is broken. Ask what the cheapest balance sheet in the room charges for a night with those bonds, and whether yours is cheaper." Theo asked what happens if nobody's is. "Then the Fed buys a seat," she said. (§20.5.)

## 20.4 Custom Baskets: The Liquidity Sink

A pro rata basket is fair and expensive. If HYG redeemed by delivering a 1/N slice of all 1,334 bonds, every redeeming AP would receive dozens of odd lots it would have to sell into the bid, and the band's lower edge would sit wherever the least liquid bond's bid sat. Real credit ETFs do not work that way. They use **custom baskets**: non-representative subsets, negotiated with the AP and changed from order to order.

### 20.4.1 The rule and the regulator's worry

Rule 6c-11(c)(3) permits custom baskets on two conditions. The ETF "must adopt and implement written policies and procedures that govern the construction of baskets," and for custom baskets those procedures must "set forth detailed parameters for the construction and acceptance of custom baskets" and "specify the titles or roles of the employees of the exchange-traded fund's investment adviser" who review each one. Each basket is recorded, with a note on whether it was custom and whether it complied, and the record is kept for five years (6c-11(d)(2)(ii)). Before the rule, the freedom to use custom baskets depended on the vintage of a sponsor's exemptive order (the exact cutoff is a CHECK item), so the rule made the practice available to everyone who wrote the procedures.

The SEC's adopting release (Release 33-10695, 2019) spelled out the game the procedures are meant to police, in two words. An AP "potentially could pressure an ETF into accepting those securities in its basket in exchange for liquid ETF shares (i.e., dumping)." Or it could press the fund "into including in its basket certain desirable securities in exchange for ETF shares tendered for redemption (i.e., cherry-picking)." The release also acknowledged that "under certain market conditions, custom baskets can lead to greater price volatility and dislocation from NAV." And it anticipated the empirical literature by several years. Some ETFs, the release observed, "may choose to decrease, rather than increase, the weight of more liquid securities and increase the weight of less liquid securities in their basket compared to their portfolio in order to reduce transaction costs borne by an ETF's existing/remaining shareholders."

"In kind," Kaz said, reading over Theo's shoulder. "As opposed to redeeming unkindly?"

"In March 2020," Mags said, "it was both."

### 20.4.2 What the baskets actually look like

Three research programs, each with its own sample, agree on the shape.

- **Baskets are fractional.** Shim and Todorov ("ETFs, illiquid assets, and fire sales," BIS WP 975, 2021) find that creation baskets of corporate bond ETFs contain about 10% of the fund's holdings and redemption baskets about 20%, against close to 100% for equity and Treasury ETFs. Todorov's BIS Quarterly Review article ("The anatomy of bond ETF arbitrage," March 2021) reports about 20% and 35% on its sample, and finds the holdings' bid–ask about 17 times the ETF's. The numbers differ by sample, so cite each to its own paper; the direction is the same.
- **Redemption baskets are where liquidity goes to be disposed of.** In Shim and Todorov's data, redemption baskets have *shorter* duration and *wider* bid–ask spreads than the holdings, while creation baskets have longer duration and tighter spreads. The fund takes in liquid, index-relevant bonds and hands out short, illiquid ones.
- **The basket is a portfolio-management tool.** Koont, Ma, Pástor and Zeng (NBER w30039; *RFS* 2025) show that bond ETFs "actively manage their portfolios," trading off index tracking against liquidity transformation. Baskets include cash and a subset of index bonds, more so when the bonds are illiquid, and are adjusted to correct portfolio imbalances while still facilitating arbitrage. Basket inclusion improves a bond's liquidity in normal times and worsens it when creations and redemptions are highly imbalanced, as in COVID-19.

The AP side has its own conflict. Pan and Zeng ("ETF Arbitrage under Liquidity Mismatch," ESRB Working Paper No. 59, 2017) use AP-level data to document "a conflict between APs' dual roles as bond dealers and as ETF arbitrageurs." When the conflict is small, the liquidity mismatch simply reduces arbitrage capacity. As it grows, "an inventory management motive arises that may even distort ETF arbitrage, leading to large relative mispricing." An AP that is also a dealer may redeem in order to source bonds it has been asked for, or decline to create in order to avoid buying bonds it is already long. Its arbitrage decisions are partly inventory decisions.

### 20.4.3 Derivation: the custom basket as a quadratic program

Make the negotiation explicit. On a redemption of fraction $\rho$ of the fund, the fund chooses value weights $w \in \mathbb{R}^N$, with $\mathbf{1}^\top w = 1$, for the basket it delivers. The portfolio weights are $h$, with $\mathbf{1}^\top h = 1$; the pro rata basket is $w = h$. Three costs depend on $w$.

- **The AP's liquidation cost.** The AP must sell the basket, at cost $c_i - a_i$ per unit of bond $i$. Here $a_i \ge 0$ is the AP's **axe**: it is lower for a bond the AP has a client bid for, or a short to cover. Competition among APs passes this cost through to the discount, and so to the fund's investors.
- **The fund's avoided cost.** Every unit of bond $i$ the fund delivers in kind is a unit it never has to sell for cash later. Write $\ell_i \ge 0$ for that shadow value, which is large for illiquid bonds the fund would like to be rid of.
- **Tracking error.** Delivering $w \ne h$ makes the remaining portfolio drift from the index. For a small redemption, the drift is proportional to $\rho\,(w - h)$, so the variance cost is $\tfrac{\theta}{2} (w - h)^\top \Sigma (w - h)$. Here $\Sigma$ is the covariance of bond returns and $\theta > 0$ is the fund's price of tracking variance, which scales with $\rho$.

Collect the linear terms into a net cost vector $k_i = c_i - a_i - \ell_i$ (a negative $k_i$ means the bond is worth more out of the fund than its cost to the AP). The fund's problem is

$$
\min_{w}\; J(w) = k^\top w + \frac{\theta}{2}\,(w - h)^\top \Sigma\,(w - h) \quad \text{subject to} \quad \mathbf{1}^\top w = 1.
$$

The Lagrangian is $\mathcal{L} = k^\top w + \frac{\theta}{2}(w - h)^\top \Sigma (w - h) - \mu\,(\mathbf{1}^\top w - 1)$. Setting its gradient to zero gives $k + \theta \Sigma (w - h) - \mu \mathbf{1} = 0$, so

$$
w = h - \frac{1}{\theta}\, \Sigma^{-1} \left(k - \mu \mathbf{1}\right).
$$

Impose the budget constraint. Because $\mathbf{1}^\top h = 1$, we need $\mathbf{1}^\top \Sigma^{-1}(k - \mu \mathbf{1}) = 0$, which pins down the multiplier:

$$
\mu^* = \frac{\mathbf{1}^\top \Sigma^{-1} k}{\mathbf{1}^\top \Sigma^{-1} \mathbf{1}}, \qquad w^* = h - \frac{1}{\theta}\, \Sigma^{-1}\left(k - \mu^* \mathbf{1}\right). \tag{20.6}
$$

$\mu^*$ is the generalized-least-squares average net cost. The optimal basket overweights bonds whose net cost lies below that average (the AP is axed, or the fund wants them gone) and underweights bonds above it. The $\Sigma^{-1}$ makes the tilts hedge each other, so the fund swaps substitutes for substitutes rather than simply dumping the worst bond. The boundary cases are sensible. As $\theta \to \infty$ (tracking is all that matters), $w^* \to h$, the pro rata basket. As $\theta \to 0$, the tilts grow without bound, and the nonnegativity constraint $w \ge 0$, which (20.6) ignores, takes over. The fractional baskets in the data are the corner solutions of this problem.

How much is the freedom worth? Substitute $w^*$ into $J$. The linear term saves $k^\top (h - w^*) = \frac{1}{\theta} k^\top \Sigma^{-1}(k - \mu^* \mathbf{1})$. Because $\mathbf{1}^\top \Sigma^{-1}(k - \mu^* \mathbf{1}) = 0$, we may subtract $\mu^* \mathbf{1}^\top$ inside, which turns that saving into $\frac{1}{\theta}\mathcal{D}$, where

$$
\mathcal{D} \equiv (k - \mu^* \mathbf{1})^\top \Sigma^{-1} (k - \mu^* \mathbf{1}) \ge 0.
$$

The tracking cost at the optimum is $\frac{\theta}{2} \cdot \frac{1}{\theta^2}\mathcal{D} = \frac{1}{2\theta}\mathcal{D}$. Therefore

$$
J(h) - J(w^*) = \frac{\mathcal{D}}{2\theta}. \tag{20.7}
$$

The value of custom baskets is the *dispersion* of net costs, measured in the metric of the inverse covariance, divided by twice the fund's tracking aversion. It is zero when every bond costs the same, and it is large when one AP's axes are concentrated in bonds the fund wants to shed. A dealer that has just bought a 150-line portfolio trade is the cleanest example (Chapter 19). Its axe vector $a$ is the PT, and a custom creation basket lets it deliver those bonds straight into an ETF. Forbidding custom baskets forces $w = h$ and destroys $\mathcal{D}/(2\theta)$ of value per redemption. Somebody pays for that in a wider portfolio-trade price.

The quadratic program also names the agency problem the SEC worried about. The AP's axe $a_i$ and the fund's shadow cost $\ell_i$ enter $k_i$ with the same sign, but they belong to different people. Dumping is an AP inflating the fund's apparent $\ell_i$ (or hiding its own $a_i$) to get junk accepted at the fund's expense. Cherry-picking is the same move run in the other direction on a redemption. The rule's written procedures and named reviewers exist to keep $k$ honest.

> **Poker Table.** "Look at who's sitting at this hand," Ines said, pointing at (20.6). "The fund sees every AP's request, so it knows more than any single AP about the flow. The AP knows its own axes, so it knows more than the fund about $a$. The remaining shareholders hold the biggest stack and aren't at the table at all. Their interests are represented by a written policy and a person with a title. That's what the procedures in 6c-11 are: a seat for the absent player." Theo said that sounded like an ad hoc group. "Represented by counsel," Ines agreed.

**Ines's hand history.** Ines replays custom baskets through markouts. For each bond that appears in a redemption basket on day $t$, she records its composite price change, net of the move in CDX HY, from the basket date to $t + 1$, $t + 5$ and $t + 20$. *IDO or it didn't happen*: without the CDX adjustment, a market-wide sell-off would look like a basket effect. On the desk's synthetic replay, redemption-basket bonds underperform their hedged peers over the first few days, as the APs' bids hit the street, and then partly recover *(illustrative; the pattern matches the basket-pressure mechanism in Koont et al., but the magnitudes are the desk's toy numbers, not a published estimate)*. The first leg is the cost the AP charged for the basket. The recovery is the fee a patient balance sheet earns for buying what the AP had to sell.

> **[SOURCE EXTRACTION]** *Man_Revolutions_in_Credit_Trading_2023 p.3:* "The new market environment of higher volatility and quantitative tightening may also have left dealers inclined to commit less of their balance sheets to bond trading. The loss of customised baskets for the ETF creation/redemption process is likely to have been another aggravating factor."
>
> **Annotation.** Man is explaining why portfolio-trading costs rose in the first half of 2022, and both of its causes appear in our equations. "Less balance sheet" is a higher $\bar\gamma$ in (20.5). "The loss of customised baskets" is the forced $w = h$ in (20.7), which removes the outlet a PT dealer used to recycle basket risk into an ETF. The two are complements, not substitutes. A dealer with less balance sheet needs the custom basket *more*, because it cannot afford to hold the PT's odd lots while it works them. Man attributes the loss only in general terms, and we do not know which sponsors narrowed their basket practices or for how long. The 2026 desk should therefore treat custom-basket availability as a time-varying state variable. Estimate it from the overlap between published baskets and holdings (the Shim–Todorov coverage ratio), and widen PT bids when it falls.

> **Trend Watch: the basket triangle, ETF ↔ portfolio trade ↔ cash (2021–2026).** *What changed:* portfolio trading and ETF primary flow became substitute ways to move basket risk. Man calls 2021 "the year of portfolio trading," attributing the boom partly to bond ETF growth (Man 2023 p.2), and records PT costs rising in H1 2022 as custom baskets were lost (p.3). *How big:* credit ETF average daily notional volume was \$7.7bn in 2024, down 7%, while cash-bond volume grew 21%, so the ETF-to-cash volume ratio fell from 23.2% in 2022 to 16.6% in 2024 (Coalition Greenwich, January 2025). In February 2024 credit ETFs were 17% of bond notional volume, the lowest since Q2 2021 (The DESK, citing Coalition Greenwich, 2024-03-19). The TRACE portfolio-trade modifier became mandatory on 2023-05-15 (FINRA Regulatory Notice 22-12), which made PT flow visible. *Stress check:* ETFs reclaimed the stage when markets broke. About \$99bn of fixed income ETFs traded on 2025-04-07, roughly 60% of it in iShares funds (The DESK, 2025-06-10). *What it means:* in calm markets, institutions move risk in the bonds themselves through PT and the ETF share of volume falls. In stress, the ETF is again the only instrument that trades at size. A desk's routing logic should switch between ETF hedges, PT and cash execution using the ETF-to-cash ratio and the ETF discount as regime signals, and it should price custom-basket availability into PT bids.

## 20.5 Case Study: March 2020, When the ETF Was the Only Price in Town

"Back in 2008," Mags said, "there was no ETF to blame. The bonds just stopped trading, and we marked them wherever the auditors would let us. Nobody saw the discount, because there was nothing to be at a discount *to*." She paused. "In 2020 the ETF told everyone the truth at 4 p.m. every day, and they hated it. I'll give it that. It was honest."

### 20.5.1 The tape

| Date (2020) | What happened | Source |
| :--- | :--- | :--- |
| Mar 1–20 | LQD and HYG fell "by about 20% from peak to trough," with IG "actually suffering slightly larger losses" than HY over Mar 1–20 | Haddad, Moreira & Muir (NBER w27168) |
| Mar 6–26 | The Markit iBoxx USD Liquid Investment Grade index fell 18.9% peak to trough | MSCI (Bohák & Janosik, 2020-04-08) |
| Mar 12 | A UCITS USD IG ETF closed about 7.5% below NAV after changing hands "more than 1,000 times," while its top five holdings traded "an average of only 37 times each"; the largest US floating-rate bond ETF closed at an 8% discount | BlackRock ViewPoint (July 2020), pp. 5–6 |
| Mar 19 | LQD closed at a 5.08% discount while HYG closed at a 0.85% *premium*; same-day traded-price dispersion of IG bonds peaked | MSCI blog |
| Mar 23 | Fed announces the SMCCF; the IG ETF rises about 7% (duration about 9.5 years, so roughly 70 bp of yield); HY barely moves | Fed release; Haddad et al. |
| Mar 23–27 | The largest HY ETF trades "over 168,000 times per day" against an average of 25 trades a day in its five largest holdings | BlackRock ViewPoint p. 5 |
| March | US fixed income ETF volume averages \$33.5bn a day, more than 3× the 2019 average; 24 APs active in iShares US ETFs | BlackRock ViewPoint pp. 3–4 |
| Apr 9 | SMCCF extended to fallen angels and HY ETFs; LQD +3% on the announcement and +4.7% by the close, the HY ETF +6% | Haddad et al. |
| May 12 / Jun 16 | SMCCF begins buying eligible ETFs, then eligible bonds | NY Fed SMCCF FAQ |
| Dec 31 | Purchases end | Federal Reserve SMCCF page |

The HY *premium* on March 19 is the single most informative row. Put it through (20.1). High yield bonds are less liquid than IG bonds, so their evaluated prices should be staler, so a staleness-only story predicts the *deeper* discount in HY. The data show the opposite. Something had pushed IG's flow term $\ell_t$ far below HY's, and Haddad et al. identify it: investors sold what they could sell, and in March 2020 the most sellable risky asset was a large, liquid, high-quality bond ETF. "Quality-flight" usually means buying quality. When the problem is cash, it means *selling* it.

Now put the same week through (20.5). Every factor in $\psi = \bar\gamma \sigma_b^2 T^{\text{h}}$ blew out together. Dealer balance sheets were constrained, so $\bar\gamma$ rose. The basis between a redemption basket and any available hedge became violent, so $\sigma_b$ rose. And the time to work out a basket of short, wide IG paper stretched from days into weeks, so $T^{\text{h}}$ rose. Meanwhile $F$, the net selling of the ETF, peaked. A multiplicative price impact met a flow spike, and a 5% discount is what that produces.

### 20.5.2 The Fed buys a seat at the table

The March 23 announcement and the July 28 term sheet are worth reading as market-microstructure documents, because the Fed wrote the arbitrage band into them. The SPV would buy "eligible corporate bond portfolios in the form of exchange-traded funds," with "the preponderance" in ETFs targeting US investment-grade bonds and "the remainder" in high yield ETFs. Leverage was 10:1 on IG ETFs and 3:1 to 7:1 "depending on risk" on other eligible assets. The facility would not hold "more than 20 percent of that ETF's outstanding shares." And it would "avoid purchasing shares of eligible ETFs when they trade at prices that materially exceed the estimated net asset value of the underlying portfolio" (SMCCF term sheet, effective 2020-07-28). The mirror clause for the exit was that it would "avoid selling shares of an ETF at times when it is trading at a price that is materially below" estimated NAV (NY Fed).

In the language of (20.4), the Fed promised to buy *inside the band, never above it*. It would not pay a premium the APs could arbitrage away by creating shares against it. It would also not sell into a discount that it had itself been brought in to close.

The Fed has been doing open market purchases since long before the phrase became the most expensive three words in leveraged finance. In 2020 it did one in LQD. The transaction-level disclosure for January 2021 shows what it bought (Federal Reserve, SMCCF transaction-specific disclosure, "Position Summary-ETF" tab). Sixteen ETFs had a combined market value of about \$8.78bn at 2020-12-31 (our sum of the tab). LQD was the largest position at \$2.47bn, followed by VCSH at \$1.52bn and VCIT at \$1.44bn. The seven high yield funds (ANGL, HYG, HYLB, JNK, SHYG, SJNK, USHY) together came to about \$1.16bn, roughly 13% of the ETF book: JNK \$576mm, HYG \$338mm, the rest smaller. That is what "preponderance" looks like in a spreadsheet.

The striking fact is how little buying it took. ETF purchases did not start until May 12, seven weeks after the announcement, by which point the discounts were long gone. Gilchrist, Wei, Yue and Zakrajšek ("The Fed Takes on Corporate Credit Risk," NBER w27809; *JME* 2024) estimate that the announcements cut eligible-bond spreads by about 70 bp in an eligibility-boundary design (about 20 bp within issuer), and that the March 23 announcement cut bid–ask spreads by about 10 bp within ten days. Actual purchases added only about 5 bp on spreads and 2 bp on bid–ask. In (20.5), the announcement worked by lowering $\bar\gamma$ and $\sigma_b$ for every AP at once. A dealer that knows a buyer with a \$750bn combined facility stands behind the basket's tail risk is a dealer with a lower price of risk. The Fed did not need to fill the hole. It needed the APs to believe the hole had a floor.

> **Poker Table.** "The Fed is the only player who can announce its hand and still win," Ines said. "It showed everyone a stack, said it would only call at fair value, and the table repriced before it put a chip in." Theo asked whether that counted as bluffing. "It's the opposite. A bluff is a bet you can't back. This was a bet so big nobody wanted to see it."

### 20.5.3 How a systematic desk would have flagged and traded it

A 2026 desk replaying March 2020 would have run four monitors, each from a piece of this chapter.

1. **Band breach.** Compute $\pi^{\text{lo}}$ and $\pi^{\text{hi}}$ from (20.4) with live half-LCS inputs. LQD at −5% was some 500 bp outside a calm band of about −6 bp. That is a regime flag, not an entry signal.
2. **Staleness share.** Estimate $\eta$ from (20.3) on a trailing calm window, and compute the staleness the model implies from the recent sequence of ETF returns. If the implied $s_t$ explains most of the discount, the NAV is late: the "discount" will close by itself as the marks fall, and there is nothing to trade.
3. **Measurement width.** Compute the same-day dispersion $u_t$ of TRACE prints for the basket's bonds. A discount inside $\pm u_t$ is noise.
4. **Price impact.** Back out $\psi$ from (20.5) using the change in shares outstanding as $F$. A rising $\psi$ means the AP channel is congested.

The trade that survives all four filters is not "buy ETF, redeem, sell bonds." Redeeming hands you short, wide IG paper at the bid on the worst day of the year, and you inherit $\sigma_b^2 T^{\text{h}}$ yourself. The trade is to **supply balance sheet in the wrapper**: buy the ETF at the discount, hedge rates with Treasury futures and spread beta with CDX IG, and wait for $F$ to normalize. The risk is that $F$ gets worse first, and in 2020 it did, for a week: the 7.5% UCITS discount came on March 12 and LQD's 5.08% on March 19. Size it so that a doubling of the discount is survivable.

For the P&L, apply the desk motto: IDO or it didn't happen. LQD's roughly 7% jump on March 23 was mostly spread tightening, which is beta you could have bought in any IG instrument. Only the part attributable to convergence of the discount was the arbitrage. On a hypothetical \$50mm LQD position bought at a 5% discount, hedged for rates and CDX IG beta, the convergence leg was worth on the order of \$2.5mm if the discount fully closed *(illustrative: the exact split between beta and convergence depends on the hedge ratio and on which NAV you believe)*. Measure it net of the hedge, or don't claim it.

> **Ways This Blows Up.** *The NAV-return backtest.* A backtest that computes ETF strategy returns from NAV instead of traded prices buys at stale marks and sells at stale marks, and it reports a smooth equity curve through March 2020 that no one could have traded. *The redemption that kills you.* An AP that redeemed LQD on March 19 owned the basket's bonds into the March 23 announcement, which worked out. One that redeemed a cash-only fund paid fees capped at 2% (§20.3.1) and was the lucky one, at the remaining holders' expense. *The phantom arbitrage.* A monitor that alerts on $P_t - \text{NAV}_t$ without the bid-side constant $\bar c$ flags every calm day as a "premium" and stops being read by Tuesday.

## 20.6 BKLN: The Basket That Cannot Settle

"But what does the credit agreement say?" Theo asked. For once, it was exactly the right question about an ETF.

A leveraged loan is not a security that clears at DTC. It moves by **assignment** under the credit agreement, which typically requires the administrative agent's consent, often the borrower's consent (which may be deemed given after a set number of days), and a check against the **disqualified lender list**. Settlement has historically taken weeks rather than days: Markit data reported an average of 17 days in Q2-2016 *(secondary source via Morningstar, 2017; CHECK; Chapter 21 owns current LSTA settlement statistics)*. ETF shares settle T+1. A loan ETF that redeems on a Monday owes cash on Tuesday for loans it will not be paid for until well into the following month.

That is why BKLN's structure looks the way it does. The fund "will normally invest at least 80% of its total assets" in the components of the Morningstar LSTA US Leveraged Loan 100 Index (Invesco). Secondary coverage has described the rest as a sleeve of cash and more liquid high yield bonds of about 10%, a tilt toward the largest loans, and a line of credit for "emergency liquidity events" *(Morningstar via Benzinga, 2017; CHECK against the current prospectus)*. Rule 22e-4 (adopted 2016-10-13, SEC press release 2016-215) caps illiquid investments at 15% of net assets, where "illiquid" means an asset that cannot be sold within seven calendar days without significantly changing its market value. Whether BKLN currently creates and redeems mainly in cash is a CHECK item for its prospectus. For loan ETFs generally, in-kind delivery of assignments to an AP is impractical, so the cash channel and its 2% fee ceiling are the relevant economics.

### 20.6.1 Derivation: the settlement gap and the liquidity runway

First, the band. For a cash redemption, the fund pays out on day $t + 1$ and receives loan-sale proceeds after a lag of $L$ years. The redemption cost in (20.4) gains two terms. One is the financing of the gap, $r L$. The other is the price risk on loans sold but not settled, which a risk manager charges as $z\, \sigma_{\text{loan}} \sqrt{L}$ for a confidence multiplier $z$:

$$
k^R_{\text{loan}} = k^R + r L + z\, \sigma_{\text{loan}} \sqrt{L}.
$$

At $L = 17/365$, $r = 5\%$ and $\sigma_{\text{loan}} = 10\%$ in stress, the financing term is about 23 bp and the risk term with $z = 2$ is about 43 bp *(illustrative)*. Most of that cost is not charged to the AP, because the fund absorbs the gap through its sleeve.

Second, the sleeve. Let $\phi_t$ be the sleeve as a fraction of the fund, and let $R_t$ be redemptions in week $t$ as a fraction of the fund. Suppose that each week the fund pays redemptions out of the sleeve and sells loans to refill it, with sale proceeds arriving $L_w$ weeks later. Then

$$
\phi_{t+1} = \phi_t - R_t + R_{t - L_w},
$$

and the sleeve survives as long as $\phi_t > 0$. Under a constant redemption rate $R_t = \bar R$ starting at week 0, the sleeve falls by $\bar R$ per week for the first $L_w$ weeks and is flat afterwards (inflow equals outflow). It therefore survives if and only if

$$
\phi_0 > \bar R\, L_w, \qquad \text{runway} = \frac{\phi_0}{\bar R} \text{ weeks}. \tag{20.8}
$$

Plug in March 2020's pace. The SEC staff report records that Morningstar high-yield bond funds and ETFs lost 9.2% of January assets in March, or about 2.1% a week. With $L_w \approx 2.4$ weeks, the requirement is $\phi_0 > 5\%$. A 10% sleeve has a runway of nearly five weeks, comfortably more than the lag *(illustrative; this uses the HY category's outflow rate, and loan funds' March 2020 outflows were not confirmed this session)*. Concentrate the same outflow into two weeks, however, and the requirement doubles, which is when the credit line earns its fee.

Theo stared at (20.8) for a long time. Then he took the USB stick out of his pocket. "This is the 13-week model," he said. "Receipts lag. Disbursements don't. You survive if your cash covers the lag, and the runway is cash over burn." The 13-week cash flow model has now been a survival curve, a state-space feature and the liquidity-runway input to the Priming Risk Score. Here it reappears as the liquidity sleeve of a \$6bn ETF, and it has never been better dressed.

### 20.6.2 What the wrapper is now being asked to hold

The loan ETF is the cautionary template for the wrappers of 2025–2026. The SPDR SSGA Apollo IG Public & Private Credit ETF (PRIV) launched in late February 2025 with a contractual arrangement for Apollo to provide intraday bids on the private credit it sources. The SEC staff reportedly sent a public letter the day after launch raising liquidity (Rule 22e-4), valuation and naming concerns *(secondary coverage; letter date and the sponsor's response CHECK)*. On 2025-11-17 the SEC granted Dimensional exemptive relief to offer ETF share classes of mutual funds, followed by a combined notice to 30 applicants on 2025-12-22 (Seward & Kissel 40 Act blog). A bond mutual fund with an ETF share class could route redemptions through the ETF class, which would make the custom-basket machinery of §20.4 the exit door for a much larger pool of 1940 Act bond money *(which bond complexes have launched such classes by late 2026 is a CHECK item)*. Every one of these structures inherits (20.8). The question for each is the same one Theo asked about BKLN: what is the settlement lag of the assets, and what covers it?

> **Trend Watch: the regulatory plumbing of the wrapper (2016–2026).** *2016-10-13:* the SEC adopts Rule 22e-4, with its four liquidity buckets, a 15% illiquid cap and a carve-out for "In-Kind ETFs"; compliance followed on 2018-12-01 for large fund complexes and 2019-06-01 for smaller ones (SEC press release 2016-215). *2019-09-26:* Rule 6c-11 adopted, effective 2019-12-23, which standardizes baskets, custom-basket procedures and premium/discount disclosure (SEC press release 2019-190; Release 33-10695). *2020-03-23 to 2021-12-17:* the SMCCF is announced, buys ETFs from 2020-05-12, ends purchases on 2020-12-31, begins selling ETFs on 2021-06-07 and has sold all of them by 2021-08-31; the SPV is terminated on 2021-12-17 (Federal Reserve; NY Fed). *2024-05-28:* the US equity and corporate bond settlement cycle moves to T+1, which widens the gap between ETF settlement and loan settlement by a day. *2025:* PRIV launches with a contractual liquidity provider, and the SEC grants the first ETF-share-class relief. *What it means:* every rule since 2016 has made the wrapper easier to launch and more transparent, while the assets going into it have become harder to settle. The arbitrage band has therefore moved from the AP's spreadsheet into the fund's liquidity policy, and that policy is now the thing to model.
