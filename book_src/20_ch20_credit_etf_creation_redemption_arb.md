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

**Reading one: the ETF was the price, and the NAV was late ($s_t$ dominates).** BlackRock's ViewPoint argued that the ETF was "acting as a price discovery vehicle" while many underlying bonds "had not traded over the period." The SEC staff's October 2020 credit-markets report noted that "ETF market prices are viewed by some market participants as a more reliable indicator of actionable value than the ETF's NAV."

**Reading two: the ETF was what people could sell ($\ell_t$ dominates).** Haddad, Moreira and Muir ("When Selling Becomes Viral," NBER w27168, 2020; *RFS* 2021) found the largest discounts in Treasury, municipal and IG ETFs, not in high yield, and wrote: "there was no discount in high yield in mid March when there was a large discount for the other categories ... This is evidence against a pure price staleness story." Staleness should be worst in the least liquid bonds, so if staleness were the whole story, HY should have shown the deepest discount. Instead, investors sold the safest liquid wrappers to raise cash, pushing $\ell_t$ deeply negative where the selling was concentrated.

**Reading three: there was no single "true" value ($M_t$ is an interval).** MSCI (Bohák & Janosik, 2020-04-08) documented that same-day traded-price dispersion in IG bonds peaked on March 19, the day LQD closed at a 5.08% discount. If identical bonds trade at prices several points apart on the same afternoon, $M_t$ is a band of width $2u_t$, not a number. A premium with $|p_t - \bar c| < u_t$ is not statistically distinguishable from zero.

All three readings are right about something, and the desk does not have to choose among them. Equation (20.1) is the bookkeeping that lets you hold all three at once. Staleness is estimated with (20.3), measurement width with same-day TRACE dispersion, and whatever is left is flow. Only the flow term is a trade.

> **[SOURCE EXTRACTION]** *Man_Quantitative_Credit_Alpha_Early_Mover_2022 p.9:* "The rise of passive bond ETFs has potentially created further distortions that will drive pricing away from fundamentals and produce opportunities for active investment strategies."
>
> **Annotation.** Equation (20.1) tells you where to look for those distortions. The staleness term creates a predictable component in *bond* marks: when HYG trades 2% below NAV on a fast down day, the evaluated prices of its constituents will very probably fall tomorrow. That matters to anyone whose performance, collateral or risk limits are struck on evaluated prices. The flow term creates temporary pressure on the bonds that appear in redemption baskets (§20.4), which is a short-horizon reversal opportunity for anyone with a balance sheet. And the basket choice itself, the "active management of passive funds," creates persistent liquidity differences between bonds that are in baskets and bonds that are not. The modern desk departs from the 2022 framing in one respect. These are not mainly *fundamental* mispricings to hold for months. They are *plumbing* mispricings that decay in days, and they belong to whoever can bear basket risk overnight at the lowest cost.
