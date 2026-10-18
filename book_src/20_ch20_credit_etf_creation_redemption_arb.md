# Chapter 20: Credit ETF Creation/Redemption Arbitrage (HYG, JNK, LQD, BKLN)

*3:41 p.m. on a Thursday, by the clock of one of Ines's drills. The screens show a composite bad week rather than a real one; the cast is fictional and every number in this scene is illustrative.*

HYG was 77.10 bid. The intraday NAV estimate beside it said 77.82. "Ninety-three basis points," Theo said. "Buy the ETF, hand the shares back to the fund, take the bonds, sell the bonds. That's an arbitrage. That's the thing the textbook says can't exist."

"It is an arbitrage," Kaz agreed. "The ETF is a portfolio, the portfolio is worth the NAV, and the law of one price does the rest. Let's just assume the NAV is—"

"Don't," said Ines. "What's the pot, what are the odds, and who at this table knows more than you?"

"The pot is ninety-three bips on whatever size we do."

"The odds depend on whether 77.82 is a price or a rumor. It's the bid side of a pricing service's opinion of thirteen hundred bonds, half of which haven't traded since Tuesday. And the person who knows more than you is whoever is selling HYG at 3:41 instead of selling bonds. Ask yourself why they aren't selling the bonds."

"Because they tried at 3:30," said Mags.

Theo pulled up the redemption basket the fund had published that morning. It was not the fund. It was 212 bonds out of 1,300, skewed short and wide, and it included a chemicals issuer he had last seen in a forbearance agreement.

Kaz leaned over. "It says 'custom basket.' Is it artisanal? Does it come with a little jar of jam?"

"It comes with the bonds nobody else wants," Mags said. "Back in my day the redemption basket was a fund manager calling you at 4:15 to ask what you'd pay for his whole high yield book. The answer was 'less.' This is better. It's still less."

Theo had spent six years at PJT reading instruments that turn into other instruments, and this one had a familiar shape. "It's a convertible," he said. "The share converts into a slice of the bonds, and the bonds convert back into shares. So it's the three questions you'd ask about any conversion right. Who holds it? What does it cost to exercise? And what do they do with the thing they receive?"

"Go on," said Ines.

"We don't hold it. The right sits with a club of dealers that have signed an agreement with the fund. We can buy the shares, but to hand them back we'd have to pay a member of the club to do it for us." He scrolled the basket. "Exercising it costs two hundred and twelve bonds sold at the bid, plus whatever it costs to own them until they're sold. And what they do with what they receive is sell it." He stopped. "To whom?"

Nobody answered, which was the answer. Theo looked at the chemicals name again, then at the 93 bp. It was a consent fee, he realized. Somebody always pays to turn a promise into cash, and the fee goes to whoever holds the scarce thing. Here the scarce thing was a balance sheet willing to own 212 bonds overnight.

Ines took three index cards from her jacket and dealt them across the desk like a river card she already knew. "Before anyone says *arbitrage* again. Write what you'd bid for the redemption basket, in what size, and who you'd sell it to."

Kaz wrote for four seconds. "Redeem all of it. Whatever the AP will take. Ninety-three bips is ninety-three bips, and the law of one price doesn't care what day of the week it is."

Mags did not pick up her pen. "I was the person you'd sell it to," she said. "In 2020 I sat on a dealer's distressed desk, and when a fund's basket came out the other side of a redemption, the bonds nobody else wanted came to people like me. I bid a third of what you're hoping."

"A third of the size?" Kaz asked.

"A third of the size, at a price you would not enjoy. The other two-thirds you keep, and you find out what they're worth on Monday."

Theo's hand had gone to his pocket, where the USB stick with his old 13-week cash flow model lived. He did not take it out. He did not have to; the stick had only ever asked one question. "How long does the AP have to hold the bonds?" he said. "Receipts lag, disbursements don't. If the AP pays for the shares today and the last bond in that basket sells in two weeks, the ninety-three bips is a fee for two weeks of somebody's balance sheet. I want to know how many weeks, and whose."

Ines looked at the screen for a while. "Is ninety-three outside anywhere a calm high-yield fund ever trades? By a mile. Is that a trade?" She tapped Kaz's card with one finger. "Not yet." Then she turned to the room. "So. Is the ETF cheap, or is the NAV late?"

That is the question this chapter answers. *When a credit ETF trades away from its net asset value, how much of the gap is mispricing, how much is accounting, and how much is a fee for somebody else's liquidity? And what does it cost to make the gap close?* The chapter takes the ninety-three apart. Some of it turns out to be a valuation convention, some of it a pricing service running late, and what is left is a fee for a balance sheet willing to hold 212 bonds overnight, which has a price that can be written down.

By Friday Theo could do what Kaz's card could not. He could tell the two markets of a credit ETF apart in the vocabulary of Rule 6c-11, and split an observed premium into a flow term, a staleness term and a bid-side accounting constant, with an estimate from public data of how late the NAV runs. He could derive the band inside which no AP bothers to create or redeem, first from bond-level trading costs and then for an AP whose balance sheet is the binding constraint, and he could read the fund's custom basket as a quadratic program that says who gains and who pays. He had replayed March 2020, the Fed's corporate facility and the loan ETF's settlement problem through those equations. And he had handed ROBO a spec for a monitor that does not mistake a late NAV for free money.

## 20.1 The Machine: Two Markets, One Wrapper

A credit ETF is two markets bolted together.

In the **secondary market**, shares trade on an exchange among anyone with a brokerage account, a market maker or, in 2020, a Federal Reserve special purpose vehicle. The price is set by supply and demand for *shares*. Nothing about a secondary-market trade touches a bond.

In the **primary market**, a small club of **authorized participants** (APs) trades with the fund itself. They trade in large blocks of shares called **creation units**, in exchange for a **basket** of bonds (or cash) plus a small **cash balancing amount**. The primary market is where shares are born and where they die. The arbitrage lives in the gap between the two markets.

Since 2019 the vocabulary has been statutory. Rule 6c-11 under the Investment Company Act (17 CFR 270.6c-11(a)(1)) defines an authorized participant as "a member or participant of a clearing agency registered with the Commission" that has a written agreement with the fund to place creation and redemption orders. It defines a basket as "the securities, assets or other positions in exchange for which an exchange-traded fund issues" (or redeems) creation units. A creation unit is "a specified number of exchange-traded fund shares that the exchange-traded fund will issue to (or redeem from)" an AP. The cash balancing amount is "an amount of cash to account for any difference between the value of the basket" and the NAV of the creation unit. Hold on to one more definition, because §20.4 is built on it. A **custom basket** is either "a basket that is composed of a non-representative selection of the exchange-traded fund's portfolio holdings," or a representative basket that differs from the initial basket used earlier that business day.

Kaz, who distrusts any definition that has not been drawn, drew the two trades on the whiteboard on Thursday evening as four boxes: the bond market on the left, the fund at the top, the exchange on the right and the AP in the middle with arrows to all three. "Creation first, because it's the cheerful one. The ETF is rich. The AP buys the bonds in the creation basket in the bond market, walks them up to the fund with the cash balancing amount, gets a creation unit of brand-new shares, and sells those shares on the exchange at the rich price." They added a tally beside the fund: shares outstanding, up. "Redemption is the same picture with the arrows reversed. The ETF is cheap. The AP buys shares on the exchange, hands a creation unit back to the fund, receives the redemption basket, and sells the bonds." The tally went down. "That last verb is where your ninety-three went," Ines said from the door.

Theo asked what happened if the fund did not want bonds at all. Some funds, Kaz said, transact **in cash** rather than in kind, for some or all orders: the fund buys or sells the bonds itself and charges the AP a transaction fee to cover the cost. For a corporate bond fund that is a detail. For a loan fund it is the whole problem (§20.6). Figure 20.1 is Kaz's whiteboard, tidied up.

![Figure 20.1: The AP is the only link between the bond market, the fund and the exchange: when the ETF is rich it buys bonds and sells new shares (blue), and when the ETF is cheap it buys shares and sells the redemption basket (orange). Illustrative: schematic of the Rule 6c-11 flows described in §20.1.](assets/figures/ch20_wrapper_flows.png)

Theo's three convertible questions from the cold open (*who holds the conversion right, what does it cost to exercise, and what do they do with the thing they receive?*) organize the rest of the chapter, and the first has a countable answer.

The club is not large, but it is not tiny either. Using Form N-CEN data, BlackRock counted 37 different APs active in US-listed ETFs in 2019, with about 5 active APs per ETF on average. In March 2020, 24 APs created or redeemed iShares US ETFs, against 28 active in 2019. The AP with the largest share of creations and redemptions accounted for less than a quarter of activity by dollar value (BlackRock, *Lessons from COVID-19: ETFs as a Source of Stability*, ViewPoint, July 2020, pp. 3–4). Most of the activity, however, never reaches the club at all. ICI's 2025 Fact Book puts about 83% of domestic high-yield bond ETF activity in the secondary market, so only about 17% involves creation or redemption. Most ETF trades are just investors swapping risk with each other, which is the whole point.

> **View From Another Seat.** *The ETP market maker.* Flow Traders, the Amsterdam-listed market maker in exchange-traded products, reported net trading income of EUR 495.0m for the first quarter of 2020, against EUR 63.1m a year earlier, and added that "No loss days were recorded in the quarter." Its Chief Trading Officer, Folkert Joling, said "the ETF mechanism performed as intended" (Flow Traders, Q1 2020 trading update, 21 Apr 2020). Set that beside the Bank of England's finding, as reported by Investment Executive (21 Sep 2020, citing the Bank's May 2020 report), that some of the largest investment-grade and high-yield corporate bond ETFs traded more than 5% below NAV in mid-March, against no more than 0.1% in January. Both statements are true, because they measure different things. The market maker measures the mechanism by the volume it handled and the spread it captured on that volume; the seller measures it by the price received. The same fortnight that cost a seller five points paid an intermediary that quoted wide on record volume and reported no loss days. The release does not split the quarter by asset class, so how much of it came from credit products is not public. The seat's own later judgment is the coda: in its 2025 annual report (12 Mar 2026) the firm says it "strategically reduced the capital deployed to fixed income in 2025," moving trading capital "to other asset classes which saw greater dislocations." A market maker goes where the dislocations are, and in 2025 it decided they were mostly somewhere other than bonds.

Here are the four funds in the chapter title, as their issuers reported them in mid-October 2026.

| ETF | Inception | AUM | Holdings | Expense ratio | 30-day median bid/ask | Premium/discount | Index |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| HYG (iShares iBoxx \$ High Yield Corporate Bond) | 2007-04-04 | \$17.18bn | 1,334 | 0.49% | 0.01% | +0.02% | iBoxx USD Liquid High Yield |
| LQD (iShares iBoxx \$ Investment Grade Corporate Bond) | 2002-07-22 | \$28.78bn | 3,171 | 0.14% | 0.01% | +0.04% | iBoxx USD Liquid Investment Grade |
| JNK (SPDR Bloomberg High Yield Bond) | 2007-11-28 | \$5.72bn | 1,161 | 0.40% | 0.01% | +0.15% | Bloomberg High Yield Very Liquid |
| BKLN (Invesco Senior Loan) | 2011-03-03 | about \$6.16bn *(secondary source)* | 185 | 0.65% | n/a | n/a | Morningstar LSTA US Leveraged Loan 100 |

*Sources: iShares HYG and LQD product pages (as of 2026-10-16); SSGA JNK page (as of 2026-10-15); Invesco BKLN case study; BKLN AUM from stockanalysis.com (2026-10-16), a secondary source not confirmed against Invesco.*

Theo's eye went to two cells. HYG's 30-day median bid/ask is 0.01%, which is tighter than any bond it holds. That is not an error, and §20.2 explains why a regulator requires the fund to publish it. And BKLN holds 185 loans that settle on a timetable measured in days or weeks, while its shares settle T+1. That mismatch is the subject of §20.6.

Why is the primary market so small relative to the secondary market? Because the secondary market nets. On a heavy selling day the ETF changes hands thousands of times, and buyers and sellers mostly meet each other. Only the *net imbalance*, after market makers have warehoused what they will, reaches an AP. BlackRock's July 2020 ViewPoint (p. 5) put the gap starkly: "the largest high yield bond ETF traded over 168,000 times per day during the week of March 23 to March 27, while the fund's largest five bond holdings traded an average of 25 times per day." The ETF is a netting machine sitting on top of an RFQ market, and it nets a great deal.

> **Desk Myth vs. Desk Reality.** *Myth:* "The ETF makes high yield bonds liquid." *Reality:* the ETF makes high yield *risk* liquid. The bonds are exactly as illiquid as before. When ETF holders and bondholders need to meet, someone pays the bill: the AP in its spread, the redeeming investor in the discount, or the remaining shareholders through the basket. The whole chapter is an accounting of who that someone is.

> **[SOURCE EXTRACTION]** *Man_Quantitative_Credit_Alpha_Early_Mover_2022 p.4:* "(through a combination of ETFs, which are essentially passive quant investing, and more than one third by funds pursuing more active quantitative investing mandates)"
>
> **Annotation.** Man is describing US equity ownership, where "passive" is almost literally true: an S&P 500 ETF can create and redeem in a basket that is the index, to the share. A credit ETF is passive in its *objective* (track the iBoxx or Bloomberg index) and furiously active in its *execution*. The fund cannot buy 1,300 high yield bonds pro rata every time an AP shows up, so it chooses daily which subset to accept and which to deliver. Koont, Ma, Pástor and Zeng call it, in their title, "Active Management of Passive Funds" (NBER w30039, 2022; *RFS* 2025). The 2026 desk should treat a credit ETF as a quant strategy with a published rulebook and a discretionary trading desk attached. The rulebook is the index. The discretion is the basket, and the basket is where the alpha and the costs live.

> **Trend Watch: the wrapper eats the bond market (2019–2026).** *What changed:* on 2019-09-26 the SEC adopted Rule 6c-11, which lets ETFs that meet its conditions "come directly to market without the cost and delay of obtaining an exemptive order." At adoption there were about 2,000 ETFs with more than \$3.3 trillion in net assets, and the SEC had issued more than 300 exemptive orders since 1992 (SEC press release 2019-190). The rule became effective on 2019-12-23 (Release 33-10695). *How big:* bond ETF assets passed \$1.2 trillion in early 2021 (Shim & Todorov, BIS WP 975, 2021). US bond ETFs held \$1.8 trillion at end-2024, 17% of all ETF assets, with net issuance of \$295bn in 2024 against \$201bn in 2023 (ICI 2025 Fact Book, pp. 59–63). Secondary coverage of State Street data reported bond ETF assets above \$2.5 trillion and a record \$64bn monthly bond ETF inflow in May 2026 *(Advisor Perspectives, 2026-06-05)*. *Inside the category:* by October 2026, LQD held \$28.78bn but HYG only \$17.18bn, well below its 2020 size by press accounts, as high-yield money moved toward cheaper broad-market HY ETFs. *What it means:* the ETF is no longer a side door into credit. It is a main entrance, and its primary market is now a standing source of basket-shaped demand for the cash bonds. That demand is what portfolio-trading desks recycle (Chapter 19).

## 20.2 NAV Is an Opinion: Price, Evaluated Prices and the Bid Side

An equity ETF's NAV is a sum of closing prices from a continuous auction. A bond ETF's NAV is a sum of *evaluated prices*: model-based marks from third-party pricing services, built from whatever trades, dealer quotes and comparable bonds were available. Most of the 1,334 bonds in HYG did not trade at size today. Their marks are an informed opinion about where they would trade.

"There were two phone calls at 4:15 in my day," Mags said, when Theo asked how anyone decides what a bond that has not traded is worth. "One was the fund manager asking what you'd pay for his book, which you've heard about. The other was the pricing service asking where you'd mark it. You gave them a number, they wrote it down, on a good day they rang three other people and took the middle, and the next morning it was in somebody's NAV as if it had come down from the mountain." The calls are feeds now, and the feeds are far better, but the product is still an opinion, and three things about that opinion decide whether a discount is money.

The first is which side of the market it is struck on. "The auditor's thumb on the scale," Mags called it. For most US bond ETFs the NAV uses bid-side evaluated prices, the level at which a holder could sell, while the ETF itself is quoted, and closes, near the midpoint of its own tight market. A share priced at mid against a portfolio priced at bid looks rich on a day when nothing is happening. Vanguard's adviser education material and Morningstar both describe the convention, and both conclude that bond ETFs therefore *tend* to trade at a small premium to NAV in normal markets (Vanguard, "4 things to know about bond ETFs"; Morningstar, "NAV premiums and discounts"). A few funds use mid prices, which is why the desk reads the convention from each prospectus rather than hard-coding it. JNK's own page shows the footprint: in 2025 it closed at a premium on 206 days and at a discount on 44 (SSGA, accessed 2026-10-15).

The second is the clock. ICE has noted that a bond NAV may be struck at 3 p.m. while the exchange closes at 4 p.m. (ICE Data Services via FOW, 2020-06-22). "So a rally between three and four," Theo said, "prints as a premium." "As a premium that is really the clock," said Mags. "We called it the hour nobody owned."

The third is speed. An evaluated price moves when the evaluator sees evidence, and in a fast market evidence arrives late, so the mark trails the level at which the bond would actually clear. On the days nobody picked up Mags's phone, her marks trailed too.

Regulators know all of this, and Rule 6c-11 responds with disclosure. Every ETF must publish, daily, its NAV, market price and premium or discount as of the prior close, plus a "median bid-ask spread, expressed as a percentage rounded to the nearest hundredth," computed over the last 30 calendar days. And "if the exchange-traded fund's premium or discount is greater than 2% for more than seven consecutive trading days," the fund must say so on its website and discuss the contributing factors, for at least a year (17 CFR 270.6c-11(c)(1)). That is why every issuer page shows a median bid/ask of 0.01%. The rule mandated a statistic that makes the fund look more liquid than anything it owns, and the statistic is correct, which is the joke.

### 20.2.1 Derivation: three reasons a price differs from a NAV

> **Math, Gently.** *A ratio is a chain, and a logarithm turns the chain into a sum.* **(a) The log premium.** A premium is a ratio, price over NAV, minus one. Take the cold open's screen: $77.10 / 77.82 = 0.99075$, a simple premium of $-0.925\%$, or $-92.5$ bp. The natural log of the same ratio is $\ln 0.99075 = -0.930\%$, or $-93.0$ bp. For gaps this small the two readings agree to within half a basis point, which is why the desk says "ninety-three" for both; they drift apart only for big gaps (at a 5% discount the log reading is about 13 bp deeper). So why bother with logs? Because of part (b). **(b) The telescoping identity.** Picture a relay with three handoffs. The exchange price hands the baton to the true value of the bonds, the true value hands it to the pricing service's opinion of that value, and the opinion hands it to the bid-side NAV. Each handoff is a ratio, and the whole race, price over NAV, is the product of the three ratios, because every runner in the middle appears once on top and once underneath and cancels. A log turns that product into a sum, so the total drift of the baton is the sum of the three legs' drifts. Tiny number: the ETF is 0.5% below the true value of its bonds (price over truth $= 0.995$), the evaluator's opinion sits 2.5% above the truth (truth over opinion $= 0.975$), and marking at the bid shaves 30 bp off the opinion (opinion over NAV $= 1/(1 - 0.003) = 1.003$). The legs are about $-0.5\%$, $-2.5\%$ and $+0.3\%$, so the printed discount is about $-2.7\%$ (exactly $-2.73\%$ in logs), and only half a point of it is the ETF being cheap. The same relay, with symbols, is next.

Let the fund hold $n_i$ units of bond $i = 1, \dots, N$ per ETF share (ignore cash, accrued interest and fees for now; they add a known constant). Let $m_{i,t}$ be the true executable mid price of bond $i$ at the NAV strike time on day $t$. It exists in principle and is never observed directly. The pricing service publishes an evaluated mid $\tilde m_{i,t}$ and an evaluated bid $\tilde m_{i,t}(1 - c_i)$, where $c_i$ is bond $i$'s half bid–offer as a fraction of price. Define the per-share aggregates

$$
M_t = \sum_{i=1}^{N} n_i\, m_{i,t}, \qquad \tilde M_t = \sum_{i=1}^{N} n_i\, \tilde m_{i,t}, \qquad \text{NAV}_t = \sum_{i=1}^{N} n_i\, \tilde m_{i,t}(1 - c_i) = \tilde M_t\,(1 - \bar c_t),
$$

where $\bar c_t = \sum_i n_i \tilde m_{i,t} c_i / \tilde M_t$ is the value-weighted half-spread of the portfolio. Let $P_t$ be the ETF's closing price (the midpoint of its own bid and ask). The premium is $\pi_t = P_t / \text{NAV}_t - 1$; we work with the log premium $p_t = \ln(P_t/\text{NAV}_t)$, which equals $\pi_t$ to first order.

Multiply and divide by $M_t$ and $\tilde M_t$, and take logs:

$$
p_t \;=\; \underbrace{\ln \frac{P_t}{M_t}}_{\ell_t \;(\text{flow})} \;+\; \underbrace{\ln \frac{M_t}{\tilde M_t}}_{s_t \;(\text{staleness})} \;+\; \underbrace{-\ln\left(1 - \bar c_t\right)}_{\approx\, \bar c_t \;(\text{bid-side convention})}. \tag{20.1}
$$

Equation (20.1) is an identity. It needs no assumptions, which is why it is useful: every argument about bond ETF premiums is an argument about which of the three terms is large, and each term has its own villain. In the **flow term** $\ell_t$, the ETF price differs from the true value of what it holds; this is the only term an AP can arbitrage, and only outside the band of §20.3. In the **staleness term** $s_t$, the true value differs from the pricing service's opinion. Nobody can arbitrage that, because nobody can trade at the evaluated price, but it is a *forecast*: the NAV will move toward the ETF. And the **accounting term** $\bar c_t$ is a near-constant positive premium created by marking at the bid, about 10 bp for an IG fund with a value-weighted half-spread of 10 bp and about 30 bp for an HY fund at 30 bp *(illustrative magnitudes)*. Mags's thumb on the scale, in other words, has a size.

Now give staleness a model, one that matches how Mags's evaluators actually behaved.

> **Math, Gently.** *The evaluator who closes half the gap.* Picture a thermostat that, at every tick, moves the room halfway to the setting. Throw the setting five degrees down and the room is 2.5 degrees too warm after the first tick, 1.25 after the second, 0.625 after the third, and it never quite arrives. A pricing service that sees evidence slowly behaves the same way: each day it closes a fraction $\eta$ of the gap between its mark and the level at which the bonds would really clear. Take $\eta = 0.5$ and one bad day on which the bonds' true value falls 5%. That evening the NAV overstates value by 2.5%, so an ETF priced *exactly* at fair value prints a 2.5% discount *(illustrative)*. The ETF isn't at a discount. The NAV is at a premium. It's the same number with a different villain. The next evening the staleness is $-1.25\%$, then $-0.625\%$, halving each day. Square each day's staleness and add: $6.25 + 1.56 + 0.39 + \dots = 8.33$, exactly one third of the shock squared ($25$). That one third is $(1-\eta)^2 / \big(\eta(2-\eta)\big) = 0.25/0.75$, and when shocks arrive every day at random it becomes the ratio of the staleness variance to the daily return variance. A fresher evaluator ($\eta = 0.8$) shrinks it to $0.04/0.96$, about 4%; a sleepier one ($\eta = 0.2$) inflates it to $0.64/0.36$, nearly 1.8, so the staleness is noisier than the market it is late about. The geometric series that makes this exact is next.

In symbols, **partial adjustment** makes staleness an exponentially weighted sum of recent true log returns $r_t = \ln M_t - \ln M_{t-1}$:

$$
s_t = \sum_{j=0}^{\infty} (1 - \eta)^{j+1}\, r_{t-j}. \tag{20.2}
$$

#### The Full Derivation: staleness as a geometric series

Each day the evaluated level closes a fraction $\eta \in (0, 1]$ of the gap to the truth,

$$
\ln \tilde M_t = \ln \tilde M_{t-1} + \eta\,\left(\ln M_t - \ln \tilde M_{t-1}\right).
$$

Subtract both sides from $\ln M_t$ and use the true log return $r_t$:

$$
s_t = \ln M_t - \ln \tilde M_t = (1 - \eta)\left(\ln M_t - \ln \tilde M_{t-1}\right) = (1 - \eta)\left(s_{t-1} + r_t\right).
$$

Iterating backwards gives (20.2). If true returns are i.i.d. with mean zero and variance $\sigma_r^2$ under $\mathbb{P}$, then $\mathbb{E}^{\mathbb{P}}[s_t] = 0$ and

$$
\operatorname{Var}^{\mathbb{P}}(s_t) = \sigma_r^2 \sum_{j=0}^{\infty} (1-\eta)^{2(j+1)} = \frac{(1-\eta)^2}{1 - (1-\eta)^2}\,\sigma_r^2 = \frac{(1-\eta)^2}{\eta\,(2 - \eta)}\,\sigma_r^2.
$$

The boundary cases check out. At $\eta = 1$ the evaluator is perfectly fresh and $s_t \equiv 0$. As $\eta \to 0$ the variance explodes: a NAV that never updates eventually differs from the truth by the entire cumulative return.

<!-- FIGURE: ch20_staleness_variance.png (curve: Var(s)/sigma_r^2 = (1-eta)^2/(eta(2-eta)) over eta in (0,1], eta = 0.5 -> 1/3 marked) -->

<!-- FIGURE: ch20_premium_decomposition.png (stacked: simulated 60-day path with one -5% day, eta = 0.5, c-bar = 30 bp, 2 bp price noise; l_t, s_t, c-bar stacked to p_t per (20.1)). Caption: "The same discount, three villains: after a 5% drop the staleness term is most of the printed discount for a week while the flow term is noise." -->


### 20.2.2 Measuring staleness: does the NAV catch up?

Equation (20.2) has a testable implication. The NAV's own log return is

$$
\Delta \ln \text{NAV}_t = \Delta \ln \tilde M_t + \Delta \ln(1 - \bar c_t) = \eta\,\left(s_{t-1} + r_t\right) + \Delta \ln(1 - \bar c_t).
$$

Suppose the flow term is small ($\ell_t \approx 0$) and the spread is stable ($\bar c_t \approx \bar c$). Then (20.1) gives $s_{t-1} = p_{t-1} - \bar c$, and

$$
\Delta \ln \text{NAV}_t = \eta\, (p_{t-1} - \bar c) + \eta\, r_t. \tag{20.3}
$$

Regress the NAV's daily log return on yesterday's log premium. The slope estimates $\eta$, the speed at which the NAV catches up to the ETF, and the intercept estimates $-\eta \bar c$. Under i.i.d. true returns, $r_t$ is uncorrelated with $p_{t-1}$, so ordinary least squares is consistent. This is the regression version of a finding that Shim and Todorov (BIS WP 975, 2021) report for ETFs with fractional baskets: persistent premiums and discounts, linked to NAV returns that adjust slowly to ETF returns.

Theo asked what a small slope would mean, and Kaz, who likes a regression best when it can embarrass somebody, said it depends on what else is hiding in the premium. If the flow term is not negligible and is independent of staleness, then $p_{t-1} - \bar c = s_{t-1} + \ell_{t-1}$, and the premium on the right-hand side is staleness read through a noisy instrument.

> **Math, Gently.** *A ruler with a wobbling zero.* Chapter 1's box on regression slopes says what a slope is; this is what happens when the variable on the horizontal axis is measured badly. Suppose you want to know how much a plant grows per hour of sunlight, but your light meter's zero wobbles at random every time you read it. Some of the days that look sunny are days on which the meter read high by accident, and on those days the plant grows only as much as the real sunlight allows. The line through the points comes out flatter than the truth, never steeper, and how much flatter depends on how much of the meter's variation is wobble. The premium is that meter: it reads staleness plus flow, and only the staleness predicts tomorrow's NAV. Tiny number: staleness variance 4 and flow variance 12 (both in squared basis points). The staleness share of the premium's variance is $4/(4+12) = 1/4$, so the slope reads $\eta/4$. An evaluator that closes 40% of the gap each day ($\eta = 0.4$) shows up as a slope of 0.10, and looks like one that closes a tenth. The same scatter tells two stories, a slow NAV beside a quiet ETF or a quick NAV beside a noisy one. The formula follows.

Formally, the slope is attenuated to

$$
\hat\eta \;\to\; \eta \cdot \frac{\operatorname{Var}(s)}{\operatorname{Var}(s) + \operatorname{Var}(\ell)},
$$

$\eta$ times the staleness share of premium variance. A small slope can mean a fresh NAV or a noisy ETF, and only a second instrument (the ETF's own lagged returns, or a matched fund) can tell which.

The spread itself is the other thing hiding in the regression. $\bar c_t$ is not constant in stress: spreads widen, so $+\Delta \ln(1 - \bar c_t)$ becomes a negative drag on NAV returns in exactly the weeks when everyone most wants the estimate. That is why the desk estimates $\eta$ on calm windows and then asks, as a separate question, whether it falls in stress.

### 20.2.3 The three readings of a discount

In March 2020, three serious readings of the same discount appeared, and each one is a claim about which term of (20.1) dominated.

**Reading one: the ETF was the price, and the NAV was late ($s_t$ dominates).** BlackRock's ViewPoint argued that the largest US floating-rate bond ETF, which closed at an 8% discount on March 12, was "acting as a price discovery vehicle" because many of its underlying bonds "had not traded over the period." The SEC staff's October 2020 credit-markets report noted that "ETF market prices are viewed by some market participants as a more reliable indicator of actionable value than the ETF's NAV." This is Kaz's reading, and Kaz holds it the way a physicist holds a conservation law: "Before I believe any discount, I want to know how much of it is the NAV still catching up. That part isn't a trade. It's a weather forecast for the marks."

**Reading two: the ETF was what people could sell ($\ell_t$ dominates).** Haddad, Moreira and Muir ("When Selling Becomes Viral," NBER w27168, 2020; *RFS* 2021) found the largest discounts in Treasury, municipal and IG ETFs, not in high yield, and wrote: "there was no discount in high yield in mid March when there was a large discount for the other categories ... This is evidence against a pure price staleness story." Staleness ought to be worst in the least liquid bonds, so if staleness were the whole story, HY would have shown the deepest discount. Instead, investors sold the safest liquid wrappers to raise cash, pushing $\ell_t$ deeply negative where the selling was concentrated. Ines reads it as a poker player reads a table where everyone is short of chips: "When everybody needs cash at once, the safest wrapper is the one people can sell, so it's the one they sell first. Quality doesn't protect you from that. Quality is why you get picked."

**Reading three: there was no single "true" value ($M_t$ is an interval).** MSCI (Bohák & Janosik, 2020-04-08) documented that same-day traded-price dispersion in IG bonds peaked on March 19, the day LQD closed at a 5.08% discount. If identical bonds trade at prices several points apart on the same afternoon, $M_t$ is a band of width $2u_t$, not a number. A premium with $|p_t - \bar c| < u_t$ is not statistically distinguishable from zero. Mags, who marked bonds through that week from the other side of a dealer's desk, puts it more shortly: "There was no true price. There was a range, and it depended on who you called."

All three readings are right about something, and the desk does not have to choose among them. Equation (20.1) is the bookkeeping that lets it hold all three at once. Staleness is estimated with (20.3), measurement width with same-day TRACE dispersion, and whatever is left is flow. Only the flow term is a trade. Section 20.5 gives each reader a card on 19 March 2020 and grades it against these three papers.

> **[SOURCE EXTRACTION]** *Man_Quantitative_Credit_Alpha_Early_Mover_2022 p.9:* "The rise of passive bond ETFs has potentially created further distortions that will drive pricing away from fundamentals and produce opportunities for active investment strategies."
>
> **Annotation.** Equation (20.1) tells you where to look for those distortions. The staleness term creates a predictable component in *bond* marks: when HYG trades 2% below NAV on a fast down day, the evaluated prices of its constituents will very probably fall tomorrow. That matters to anyone whose performance, collateral or risk limits are struck on evaluated prices. The flow term creates temporary pressure on the bonds that appear in redemption baskets (§20.4), which is a short-horizon reversal opportunity for anyone with a balance sheet. And the basket choice itself, the "active management of passive funds," creates persistent liquidity differences between bonds that are in baskets and bonds that are not. The modern desk departs from the 2022 framing in one respect. These are not mainly *fundamental* mispricings to hold for months. They are *plumbing* mispricings that decay in days, and they belong to whoever can bear basket risk overnight at the lowest cost.

## 20.3 The Arbitrage Band, Derived

An options market maker would describe the AP's position in one sentence: it owns a call and a put on the ETF's premium, struck at the costs of creation and redemption. The band between those strikes is the most important object in this chapter, and Ines's "not yet" in the cold open was a statement about where its lower edge sat, so we derive it twice: once with costs as constants, and once with a balance sheet that charges for risk.

### 20.3.1 The static band

> **Math, Gently.** *The band as two strikes, or a room with two doors.* Picture the premium as someone wandering about a room. Inside the room nobody cares where it goes: buyers and sellers of shares push it around and no AP lifts a finger. The room has two doors. The upper door is creation: when the premium reaches it, an AP buys bonds, makes new shares and sells them, and the selling pushes the premium back inside. The lower door is redemption, the same trip in reverse. Each door has a toll keeper, and the toll is the cost of exercising: the half-spread on the bonds bought or sold, the fund's fee, and everything else. A door sits exactly where the premium just pays its toll. One oddity: because the NAV is struck at the bid, the room is not centred on zero, and its floor is already lifted by the bid-side constant. Tiny number, for the upper door of a calm high yield fund with $\bar c = 30$ bp and a pro rata creation basket ($c^C = 30$ bp): buying the basket at the offer costs $1.003$ of mid, and dividing by a bid-side NAV of $0.997$ of mid gives $1.003/0.997 = 1.006018$ per dollar of NAV. The shortcut of simply adding the two half-spreads, $1 + 0.0030 + 0.0030 = 1.0060$, is off by 0.2 bp, which is why the band can be written as a plain sum of costs. The derivation follows.

Work per \$1 of NAV and per creation unit, with every cost written as a fraction of NAV. The fund's fixed creation and redemption fees, divided by the creation unit's value, are $f^C$ and $f^R$. The value-weighted half-spreads of the *creation* and *redemption* baskets, which need not equal the portfolio's $\bar c$, are $c^C$ and $c^R$. Everything else (market impact beyond the half-spread, financing over the settlement gap, and the risk premium of §20.3.2) goes into $k^C$ and $k^R$. In a calm market, where the evaluated mid is the true mid ($s_t = 0$ in (20.1)), no arbitrage confines the premium to the band (20.4) derived below.

#### The Full Derivation: the static band

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

#### Reading the band: a census and two doors

Theo read (20.4) the way he used to read a fee letter, looking for who gets paid, and when. With pro rata baskets, where both baskets look like the fund ($c^C = c^R = \bar c$), the band runs from $-f^R - k^R$ to $2\bar c + f^C + k^C$. Its width, $2\bar c + f^C + f^R + k^C + k^R$, is the round-trip cost of the portfolio and does not care how the NAV is struck. Its *center*, $\bar c + \tfrac12(f^C + k^C - f^R - k^R)$, does. Under a mid-price NAV the room would sit symmetrically around zero, $-\bar c - f^R - k^R \le \pi_t \le \bar c + f^C + k^C$; bid-side marking slides the whole room up by $\bar c$. "So that's why a calm high yield ETF trades at a premium," Theo said. "It isn't demand. It's a decimal point in the valuation policy." Then he pulled up JNK's page. A room that begins near zero and extends to $2\bar c$ above it is mostly premium territory, and where the premium leans inside it says which way the money is moving: in steady inflows APs create at the margin and the premium presses on the upper door, $\pi^{\text{hi}}$, while in steady outflows it presses on the lower one, $\pi^{\text{lo}}$. A census of 206 premium closes against 44 discount closes in 2025 is what such a room looks like from the inside. (Exercise 1 asks what the census says about the doors.)

Ines read the same inequality as a seating chart. "The fund decides who walks through which door, and what the toll is." Custom baskets move the two doors independently. A creation basket of tight bonds ($c^C < \bar c$) lowers $\pi^{\text{hi}}$, so creating gets cheaper and the upper door moves in. A redemption basket of wide bonds ($c^R > \bar c$) lowers $\pi^{\text{lo}}$, so the discount has to be deeper before redeeming pays, and the lower door moves out. "That's the fund exporting its illiquidity to the AP," she said, "and the AP sending the bill back through the discount." The fund's liquidity management shows up directly in the price.

Put in numbers *(all illustrative)*. A high yield fund with $\bar c = 30$ bp, a redemption basket at $c^R = 45$ bp, a pro rata creation basket, fees of 1 bp each way and $k = 5$ bp has $\pi^{\text{lo}} = 30 - 45 - 1 - 5 = -21$ bp and $\pi^{\text{hi}} = 30 + 30 + 1 + 5 = 66$ bp. An IG fund with $\bar c = 8$ bp, $c^R = 10$ bp, fees of 1 bp and $k = 3$ bp has $\pi^{\text{lo}} = -6$ bp and $\pi^{\text{hi}} = 20$ bp. Both are consistent with the small positive premiums on the issuer pages in §20.1. In the cold open, HYG's 93 bp discount is far outside any calm-market band, which tells you that $k^R$, the term we have been treating as a constant, is not one. Figure 20.2 draws the two bands.

![Figure 20.2: Calm-market premiums of HYG, JNK and LQD sit inside their no-arbitrage bands, while the 93 bp discount of the cold open lies far outside the high-yield band and so cannot be a calm-market arbitrage. Source: issuer premiums from iShares (HYG, LQD; 2026-10-16) and SSGA (JNK; 2026-10-15). Illustrative: the band edges are the worked example of §20.3.1 and the cold-open discount is the opening scene's.](assets/figures/ch20_arbitrage_band.png)

**The cash-redemption wrinkle.** When a fund redeems in cash, it sells the bonds itself and charges the AP a variable fee to cover the cost. That fee has a ceiling. BlackRock's ViewPoint (p. 6) notes that under the 1940 Act "the amount funds can charge to APs on redemptions to mitigate against the potential dilutive impact of cash redemptions is capped at 2% of the value of the shares redeemed," and that above that level "the excess would be absorbed by the ETF to the detriment of the ETF's remaining shareholders." In (20.4), the AP's redemption cost $f^R$ is capped at 2% even when the true liquidation cost is higher. The lower edge of the band then stops at about $-2\%$ plus whatever the AP charges for risk, and the remainder of the cost moves to the people who stayed in the fund. That is a first-mover advantage, which is the textbook ingredient of a run, and loans (§20.6) are where it bites.

> **[SOURCE EXTRACTION]** *Dynkin_Systematic_Investing_in_Credit p.702:* "LCS measures the cost of an immediate round-trip transaction of a typical institutional size and is expressed as a percentage of a bond price ... For bonds quoted on spread, LCS is calculated as a product of bid–offer spread and spread duration."
>
> **Annotation.** This is $2c_i$ in (20.4), already computed for you. For an IG bond quoted on spread, a 6 bp bid–offer on a bond with $D^{\text{spr}} = 7$ gives an LCS of 42 bp of price, so $c_i = 21$ bp. For a high yield bond quoted on price, LCS is simply the offer minus the bid, as a percentage of price. Value-weight the half-LCS across the basket and you have $c^C$, $c^R$ and $\bar c$, and therefore both edges of the static band, from data a systematic desk already holds. The 2026 desk departs from the textbook in two ways. LCS describes an *immediate* trade of *typical* size, while an AP liquidating a 212-bond redemption basket is trading neither immediately nor at typical size. The size and time terms live in $k^R$, and §20.3.2 prices them. And LCS was built on one dealer's two-way quotes. In a market that is now about half electronic in IG and about a third in HY, the better input is a composite of streaming and RFQ prices, but the formula is the same.

### 20.3.2 The band with a balance sheet

In calm markets, $k$ is a few basis points and the static band is the whole story. In stress, $k$ is almost all of the story, and almost all of $k$ is the price of *risk*. Between buying ETF shares and selling the last bond of a redemption basket, the AP owns a bond position it did not choose. It can hedge the market component with CDX HY, index futures or the ETF itself, but the residual (basket minus hedge) remains on its books until the bonds are sold.

Model that residual. Let $X$ be the NAV value, in dollars, of one creation unit. Let $Q \ge 0$ be the number of creation units an AP redeems ($Q$ is a count of units, not the measure $\mathbb{Q}$). Let $T^{\text{h}}$ be the holding period in years until the basket is sold, and let $\sigma_b$ be the annualized volatility of the hedged basket's return, the **basis volatility**. Write $\kappa^R = f^R + c^R - \bar c$ for the static redemption cost from (20.4), so that the AP's edge per dollar is $e_t = -\pi_t - \kappa^R$. A mean-variance AP with risk aversion $\gamma$ (per dollar) maximizes

$$
U(Q) = Q X\, e_t - \frac{\gamma}{2}\, Q^2 X^2 \sigma_b^2\, T^{\text{h}}.
$$

> **Math, Gently.** *A hill, and risk tolerances that add like resistors.* **(a) Mean-variance as a hill.** The AP's utility has two parts. The edge it earns grows in a straight line with size: twice the redemption, twice the edge. The fear, the penalty for holding a basket it cannot hedge, grows with the square of size, because a position twice as large has four times the variance. A straight line minus a parabola is a hill. At first each extra million adds more edge than fear, then less, and the top of the hill is the best size, $Q^*$; at the top the slope is zero, which is all a "first-order condition" says. Tiny number: an edge of 100 bp and a fear coefficient $\gamma \sigma_b^2 T^{\text{h}}$ of 0.0002 per \$1mm of basket. The top sits where the edge, 0.01, equals the fear coefficient times size, so the AP redeems $0.01/0.0002 = \$50$mm. Double the basis volatility and the fear coefficient quadruples to 0.0008; the size falls to \$12.5mm. Same edge, a quarter of the balance sheet. **(b) Risk tolerances add like resistors in parallel.** Risk tolerance is the inverse of risk aversion, $1/\gamma$: how much risk an AP will carry per unit of edge. When several APs face the same edge their tolerances add, the way conductances add for resistors wired side by side, so the street behaves like a single AP with $\bar\gamma = 1/\sum_j (1/\gamma_j)$. Two APs at $\gamma = 2$ each have a combined tolerance of $\tfrac12 + \tfrac12 = 1$, so the street acts like one AP at $\bar\gamma = 1$. If one leaves, the tolerance halves, $\bar\gamma$ doubles to 2, and so does the discount that the same selling produces. With twenty APs one departure barely registers; with two it is everything. The algebra is next.

Solve each AP's hill, add the street's tolerances, and clear the market against $F$ dollars of net ETF selling that secondary-market liquidity providers will not hold overnight. The premium that results is

$$
\pi_t^* = -\kappa^R - \psi\, F, \qquad \psi \equiv \bar\gamma\, \sigma_b^2\, T^{\text{h}}. \tag{20.5}
$$

#### The Full Derivation: price impact of the AP channel

The first-order condition $X e_t - \gamma Q X^2 \sigma_b^2 T^{\text{h}} = 0$ gives

$$
Q^* = \frac{(e_t)^+}{\gamma\, X\, \sigma_b^2\, T^{\text{h}}}, \qquad X Q^* = \frac{(e_t)^+}{\gamma\, \sigma_b^2\, T^{\text{h}}},
$$

where $(\cdot)^+ = \max(\cdot, 0)$ because an AP never redeems at a loss. The second-order condition holds because $U''(Q) = -\gamma X^2 \sigma_b^2 T^{\text{h}} < 0$.

Now let $J$ APs, with risk aversions $\gamma_1, \dots, \gamma_J$, face the same edge. Their combined redemptions, in dollars, are

$$
\sum_{j=1}^{J} X Q_j^* = \frac{(e_t)^+}{\sigma_b^2\, T^{\text{h}}} \sum_{j=1}^{J} \frac{1}{\gamma_j} = \frac{(e_t)^+}{\bar\gamma\, \sigma_b^2\, T^{\text{h}}}, \qquad \bar\gamma \equiv \left(\sum_{j=1}^{J} \gamma_j^{-1}\right)^{-1}.
$$

The street's risk tolerance is the sum of its members' risk tolerances, so $\bar\gamma$ is the aggregate risk aversion. Finally, clear the market. The $F$ dollars of net selling must be redeemed, so $F = (e_t)^+ / (\bar\gamma \sigma_b^2 T^{\text{h}})$, and solving for the premium with $e_t = -\pi_t - \kappa^R$ gives (20.5). Check the units: $\bar\gamma$ is per dollar, $\sigma_b^2 T^{\text{h}}$ is dimensionless, and $F$ is in dollars, so $\psi F$ is a pure number, as a premium must be.

#### What the price of balance sheet says on a desk

$\psi$ is the price impact of the AP channel: discount per dollar of net selling. It has the same shape as Kyle's $\lambda$ (Chapter 18), and $\psi F$ is the inventory "fear" term $\gamma \sigma^2 \tau q$ of the Avellaneda–Stoikov quotes, with one difference of motive: Kyle's dealer fears the informed trader, while the AP fears the basket. The AP is a market maker whose inventory happens to be a portfolio.

Kaz liked (20.5) at once, because it multiplies, and things that multiply are where Kaz's intuitions go to be humbled. The ratio of stressed to calm price impact is

$$
\frac{\psi^{\text{stress}}}{\psi^{\text{calm}}} = \frac{\bar\gamma^{\text{stress}}}{\bar\gamma^{\text{calm}}} \cdot \left(\frac{\sigma_b^{\text{stress}}}{\sigma_b^{\text{calm}}}\right)^{2} \cdot \frac{T^{\text{h, stress}}}{T^{\text{h, calm}}}.
$$

Suppose risk aversion doubles, basis volatility goes from 2% to 12% annualized (a factor of 36 in variance), and the time to work out a basket goes from 2 days to 8 days. The multiplier is $2 \times 36 \times 4 = 288$ *(illustrative)*. A flow that cost 1 bp of discount in February costs about 2.9% in March. That is the order of magnitude of the IG ETF discounts of March 2020, and producing it requires no story in which the arbitrage "broke." Stress multiplies; it does not add. The arbitrage worked, at a price. Figure 20.3 shows the multiplication.

![Figure 20.3: One billion dollars of net selling costs the AP channel about 1 bp of discount in calm markets and about 2.9% in stress, because risk aversion (×2), basis variance (×36) and hold time (×4) multiply to 288. Illustrative: the price-impact model of §20.3.2, with the calm slope set to 1 bp per billion dollars.](assets/figures/ch20_ap_price_impact.png)

Theo, who had sat in lender meetings where the number of banks in a syndicate was treated as a measure of safety, went straight to the AP count. With $J$ identical APs, $\bar\gamma = \gamma / J$, so going from 28 active APs to 24 raises $\bar\gamma$, and with it $\psi$, by $28/24 - 1 \approx 17\%$. Beside the factor of 36 from basis volatility, the head count is second-order. BlackRock's observation that APs did not step away in March 2020 is correct, and it is also beside the point. They stayed and charged more, because each unit of their balance sheet had become more expensive.

The lever the fund itself controls is $\sigma_b$, the volatility of the redemption basket relative to whatever the AP can hedge with. A basket that looks like CDX HY is cheap to hold, while a basket of short, wide, idiosyncratic bonds is expensive, and those are exactly the bonds the fund would like to deliver, to protect the shareholders who remain. That tension is §20.4.

> **Poker Table.** Ines put it in terms Theo could not argue with. "The AP's right to redeem is an option, not an obligation. It's a player who sees the board and chooses whether to call. In February it calls every hand worth three basis points. In March it folds everything under three percent. Nobody left the table. The price of calling changed. When you look at a discount, don't ask whether the arbitrage is broken. Ask what the cheapest balance sheet in the room charges for a night with those bonds, and whether yours is cheaper." Theo asked what happens if nobody's is. "Then the Fed buys a seat," she said. (§20.5.)

On a multi-strategy platform Ines's question has a sharper edge, because the balance sheet belongs to someone who pays only for what is left after the hedge. Ines keeps one such trade in her replay folder, and she ran it for Theo that week.

> **The Pair.** *Pair Book entry PB-13, Dov Adler's pod at Vantress Capital Management (fictional composite), opened as a trigger in Chapter 12 and replayed here as Ines's ritual over 12–23 March 2020, cut off at each close; sizes, carry and P&L are illustrative.* **Legs.** Long \$50mm of LQD at the discount; buy protection on the on-the-run 5-year CDX IG, DV01-matched on the ETF's spread duration, which takes about \$90mm of index notional because LQD's bonds run longer than five years; Treasury futures for the rate DV01 the index leaves behind. **What the hedge removes.** IG spread beta and rates. **The idio that remains.** The wrapper's discount, $\ell_t + s_t$ of (20.1), with the bid-side $\bar c$ booked on its own line so that a return to the ordinary calm-day premium is not mistaken for alpha. Only part of that idio pays. If the discount closes because the price rises to meet the bonds, that is $\ell_t$ converging and the pod collects; if it closes because the NAV falls to meet the price, that is $s_t$ converging, the ETF has not moved, and neither has the P&L. The pair is long $\ell$ and merely watching $s$. **What leaks.** The CDX–cash basis, which was at its worst in exactly these weeks (Chapter 24 owns it); the mismatch between a basket of a few thousand longer bonds and an index of 125 five-year names; a discount that can reopen before it closes for good (LQD's 5.0% on 12 March was 0.19% at the next close, as Chapter 1 tells it, and 5.08% again on the 19th, while a UCITS IG ETF had already printed 7.5% on the 12th; the tape is in §20.5), so a pod that bought the first discount had to sit through the second; and an exit that arrived as an announcement on 23 March rather than as any law of convergence. **What it costs to carry and to short.** In spread-equivalent terms the protection leg pays the index level, which Reuters put at a 155.5 bp bid before the Fed's announcement on the morning of 23 March: on \$90mm, about \$27,000 a week. LQD's 0.14% fee adds about \$1,300 a week on \$50mm. The long's own spread income covers most of that, so the carry while waiting is roughly flat to slightly negative, which is affordable for a fortnight and ruinous for a year. **The short-leg mirror.** Any pair in the Pair Book that used HYG as its high-yield beta short saw HYG close at a 0.85% *premium* on 19 March while the bonds it hedged were being marked down, and Todorov measured tracking error above 200 bp for some bond ETFs in March–April 2020 against a 0.7 bp average (BIS Quarterly Review, March 2021). An ETF is usually the easiest short in credit to borrow, and its basis is worst exactly when the hedge is most needed. **Sizing.** To the pod's stop, not to the edge: a doubling of the discount, to about ten points on the long, has to be survivable without the risk manager calling. Section 20.5 fills, stresses and closes it.

<!-- FIGURE: ch20_pb13_attribution.png (waterfall: hypothetical \$50mm LQD long, 19 to 23 Mar 2020: rates (futures), IG spread beta (CDX), discount convergence, basis leak, fees. Caption: "IDO or it didn't happen: only the convergence bar is the arbitrage." Illustrative) -->

## 20.4 Custom Baskets: The Liquidity Sink

A pro rata basket is fair and expensive. If HYG redeemed by delivering a 1/N slice of all 1,334 bonds, every redeeming AP would receive dozens of odd lots it would have to sell into the bid, and the band's lower edge would sit wherever the least liquid bond's bid sat. Real credit ETFs do not work that way. They use **custom baskets**: non-representative subsets, negotiated with the AP and changed from order to order.

### 20.4.1 The rule and the regulator's worry

Rule 6c-11(c)(3) permits custom baskets on two conditions. The ETF "must adopt and implement written policies and procedures that govern the construction of baskets," and for custom baskets those procedures must "set forth detailed parameters for the construction and acceptance of custom baskets" and "specify the titles or roles of the employees of the exchange-traded fund's investment adviser" who review each one. Each basket is recorded, with a note on whether it was custom and whether it complied, and the record is kept for five years (6c-11(d)(2)(ii)). Before the rule, the freedom to use custom baskets depended on the vintage of a sponsor's exemptive order, so the rule made the practice available to everyone who wrote the procedures.

The SEC's adopting release (Release 33-10695, 2019) spelled out the game the procedures are meant to police, in two words. An AP "potentially could pressure an ETF into accepting those securities in its basket in exchange for liquid ETF shares (i.e., dumping)." Or it could press the fund "into including in its basket certain desirable securities in exchange for ETF shares tendered for redemption (i.e., cherry-picking)." The release also acknowledged that "under certain market conditions, custom baskets can lead to greater price volatility and dislocation from NAV." And it anticipated the empirical literature by several years. Some ETFs, the release observed, "may choose to decrease, rather than increase, the weight of more liquid securities and increase the weight of less liquid securities in their basket compared to their portfolio in order to reduce transaction costs borne by an ETF's existing/remaining shareholders."

"In kind," Kaz said, reading over Theo's shoulder. "As opposed to redeeming unkindly?"

"In March 2020," Mags said, "it was both."

### 20.4.2 What the baskets actually look like

On Friday morning Ines printed two files, a high yield fund's published baskets for the day and its holdings file, and read one against the other aloud with a highlighter, the way she reads a hand history. "Ten percent of the fund going in, twenty coming out, and the twenty is shorter and wider." Her files were one day's illustration; three research programs, each on its own sample, say the shape is general. Shim and Todorov ("ETFs, illiquid assets, and fire sales," BIS WP 975, 2021) find that creation baskets of corporate bond ETFs contain about 10% of the fund's holdings and redemption baskets about 20%, against close to 100% for equity and Treasury ETFs, and that redemption baskets have *shorter* duration and *wider* bid–ask spreads than the holdings while creation baskets run longer and tighter. The fund takes in liquid, index-relevant bonds and hands out short, illiquid ones; redemption baskets are where liquidity goes to be disposed of. Todorov's BIS Quarterly Review article ("The anatomy of bond ETF arbitrage," March 2021) reports coverage of about 20% and 35% on its own sample, with the holdings' bid–ask about 17 times the ETF's. The ratios differ because the samples do, and each belongs to its own paper, but the direction is the same. Koont, Ma, Pástor and Zeng (NBER w30039; *RFS* 2025) supply the reason. Bond ETFs "actively manage their portfolios," trading off index tracking against liquidity transformation: their baskets include cash and a subset of index bonds, more so when the bonds are illiquid, and are adjusted to correct portfolio imbalances while still facilitating arbitrage. Basket inclusion improves a bond's liquidity in normal times and worsens it when creations and redemptions are highly imbalanced, as in COVID-19. "So the basket is the fund's trading desk," Theo said. "With a rulebook," said Ines, "and a person with a title."

Mags had sat on the AP's side of that desk. "At the bank, a client would ring wanting a bond nobody was offering, and the cheapest place to find it was inside an ETF. You redeemed, the bond came out in your basket, and the risk report filed the whole thing under arbitrage, because that was the box it fit." The AP side has its own conflict, and it has been measured. Pan and Zeng ("ETF Arbitrage under Liquidity Mismatch," ESRB Working Paper No. 59, 2017) use AP-level data to document "a conflict between APs' dual roles as bond dealers and as ETF arbitrageurs." When the conflict is small, the liquidity mismatch simply reduces arbitrage capacity. As it grows, "an inventory management motive arises that may even distort ETF arbitrage, leading to large relative mispricing." An AP that is also a dealer may redeem in order to source bonds it has been asked for, or decline to create in order to avoid buying bonds it is already long. Its arbitrage decisions are partly inventory decisions.

### 20.4.3 Derivation: the custom basket as a quadratic program

Make the negotiation explicit. On a redemption of fraction $\rho$ of the fund, the fund chooses value weights $w \in \mathbb{R}^N$, with $\mathbf{1}^\top w = 1$, for the basket it delivers. The portfolio weights are $h$, with $\mathbf{1}^\top h = 1$; the pro rata basket is $w = h$. Three costs depend on $w$, and each belongs to somebody different. The AP must sell the basket, at cost $c_i - a_i$ per unit of bond $i$, where $a_i \ge 0$ is the AP's **axe**, which lowers the cost of a bond the AP has a client bid for, or a short to cover; competition among APs passes this cost through to the discount, and so to the fund's investors. The fund avoids a cost of its own: every unit of bond $i$ it delivers in kind is a unit it never has to sell for cash later, a shadow value $\ell_i \ge 0$ that is large for illiquid bonds it would like to be rid of. And delivering $w \ne h$ makes the remaining portfolio drift from the index. For a small redemption the drift is proportional to $\rho\,(w - h)$, so the variance cost is $\tfrac{\theta}{2} (w - h)^\top \Sigma (w - h)$, where $\Sigma$ is the covariance of bond returns and $\theta > 0$ is the fund's price of tracking variance, which scales with $\rho$.

Collect the linear terms into a net cost vector $k_i = c_i - a_i - \ell_i$ (a negative $k_i$ means the bond is worth more out of the fund than its cost to the AP). The fund's problem is

$$
\min_{w}\; J(w) = k^\top w + \frac{\theta}{2}\,(w - h)^\top \Sigma\,(w - h) \quad \text{subject to} \quad \mathbf{1}^\top w = 1.
$$

> **Math, Gently.** *Pegs on springs inside a rubber band, and an average that knows the covariance.* Picture each bond's weight as a peg that starts at its pro rata position. A bond with a low net cost pulls its peg up (put more of it in the basket), and a bond with a high one pulls its peg down. Left alone the pegs would fly off, and two things hold them. The tracking cost is a spring on each peg, stiffer for a bond whose returns are noisy, because moving a noisy bond moves the fund's tracking error more. And the budget is a rubber band round all the pegs: the weights must still add to one, so every peg that rises is paid for by pegs that fall, and the tilts sum to zero. The line between "pull up" and "pull down" sits at an average cost, but not the plain average; it is the average that weights each bond by the inverse of its variance, so quiet bonds count for more. Tiny number: two bonds with return variances 1 and 4 and net costs $-2$ and $+2$. The plain average is 0. The covariance-aware average is $\mu^* = (-2/1 + 2/4)/(1/1 + 1/4) = -1.5/1.25 = -1.2$, pulled toward the quiet bond. Bond 1 sits 0.8 below that line and bond 2 sits 3.2 above it. Divide each gap by the bond's variance and by $\theta$, and flip the sign: the tilts are $+0.8/\theta$ on bond 1 and $-3.2/(4\theta) = -0.8/\theta$ on bond 2. They sum to zero, and the noisy bond, four times further from the line, is tilted no more than the quiet one. The algebra is next.

The solution tilts the pro rata basket by the inverse-covariance-weighted gap between each bond's net cost and that covariance-aware average $\mu^*$:

$$
\mu^* = \frac{\mathbf{1}^\top \Sigma^{-1} k}{\mathbf{1}^\top \Sigma^{-1} \mathbf{1}}, \qquad w^* = h - \frac{1}{\theta}\, \Sigma^{-1}\left(k - \mu^* \mathbf{1}\right). \tag{20.6}
$$

The value of that freedom, against the pro rata basket, is the dispersion of the gaps, $\mathcal{D} \equiv (k - \mu^* \mathbf{1})^\top \Sigma^{-1} (k - \mu^* \mathbf{1}) \ge 0$, divided by twice the tracking aversion:

$$
J(h) - J(w^*) = \frac{\mathcal{D}}{2\theta}. \tag{20.7}
$$

$\mu^*$ is the generalized-least-squares average net cost. The optimal basket overweights bonds whose net cost lies below that average (the AP is axed, or the fund wants them gone) and underweights bonds above it. The $\Sigma^{-1}$ makes the tilts hedge each other, so the fund swaps substitutes for substitutes rather than simply dumping the worst bond. The value of custom baskets is the *dispersion* of net costs, measured in the metric of the inverse covariance, divided by twice the fund's tracking aversion. It is zero when every bond costs the same, and it is large when one AP's axes are concentrated in bonds the fund wants to shed. Forbidding custom baskets forces $w = h$ and destroys $\mathcal{D}/(2\theta)$ of value per redemption, and somebody pays for that. The cleanest case, a dealer holding a 150-line portfolio trade it needs to recycle (Chapter 19), is the scene at the end of this section.

<!-- FIGURE: ch20_custom_basket_tilt.png (bar: the two-bond Math, Gently example extended to five bonds; bars of w* - h against k_i, with the GLS average mu* as a line. Caption: "The optimal basket tilts toward bonds whose net cost lies below the covariance-weighted average, and the tilts sum to zero.") -->

#### The Full Derivation: the custom-basket program

The Lagrangian is $\mathcal{L} = k^\top w + \frac{\theta}{2}(w - h)^\top \Sigma (w - h) - \mu\,(\mathbf{1}^\top w - 1)$. Setting its gradient to zero gives $k + \theta \Sigma (w - h) - \mu \mathbf{1} = 0$, so

$$
w = h - \frac{1}{\theta}\, \Sigma^{-1} \left(k - \mu \mathbf{1}\right).
$$

Impose the budget constraint. Because $\mathbf{1}^\top h = 1$, we need $\mathbf{1}^\top \Sigma^{-1}(k - \mu \mathbf{1}) = 0$, which pins down the multiplier at $\mu^*$ and gives (20.6). The boundary cases are sensible. As $\theta \to \infty$ (tracking is all that matters), $w^* \to h$, the pro rata basket. As $\theta \to 0$, the tilts grow without bound, and the nonnegativity constraint $w \ge 0$, which (20.6) ignores, takes over. Corner solutions are fractional baskets, but how fractional depends on $\theta$: at the tracking aversion of Listing 20.1's Block 4 ($\theta = 50$) the basket still covers 92% of its lines, so reaching the 10–35% in the data takes a much smaller $\theta$ or a fixed cost per line (Exercise 4).

To value the freedom, substitute $w^*$ into $J$. The linear term saves $k^\top (h - w^*) = \frac{1}{\theta} k^\top \Sigma^{-1}(k - \mu^* \mathbf{1})$. Because $\mathbf{1}^\top \Sigma^{-1}(k - \mu^* \mathbf{1}) = 0$, we may subtract $\mu^* \mathbf{1}^\top$ inside, which turns that saving into $\frac{1}{\theta}\mathcal{D}$, with $\mathcal{D}$ as defined above. The tracking cost at the optimum is $\frac{\theta}{2} \cdot \frac{1}{\theta^2}\mathcal{D} = \frac{1}{2\theta}\mathcal{D}$. The saving less the tracking cost is (20.7).

#### Who sits at the basket

The quadratic program also names the agency problem the SEC worried about. The AP's axe $a_i$ and the fund's shadow cost $\ell_i$ enter $k_i$ with the same sign, but they belong to different people. Dumping is an AP inflating the fund's apparent $\ell_i$ (or hiding its own $a_i$) to get junk accepted at the fund's expense. Cherry-picking is the same move run in the other direction on a redemption. The rule's written procedures and named reviewers exist to keep $k$ honest.

> **Poker Table.** "Look at who's sitting at this hand," Ines said, pointing at (20.6). "The fund sees every AP's request, so it knows more than any single AP about the flow. The AP knows its own axes, so it knows more than the fund about $a$. The remaining shareholders hold the biggest stack and aren't at the table at all. Their interests are represented by a written policy and a person with a title. That's what the procedures in 6c-11 are: a seat for the absent player." Theo said that sounded like an ad hoc group. "Represented by counsel," Ines agreed.

#### Eight April 2025: the basket, the wrapper and the bid

*A replay, run for Theo from the desk's own blotter in his fifth week. The desk, its people, the ETF's sponsor, the client and every desk number are fictional, and the desk's numbers are illustrative; the dated market facts are real and cited where they appear.*

Ines ran this one on a Monday afternoon with the blotter face down, the way she runs all of them: she reads the tape up to a cut-off, everyone writes a card, and only then does the paper turn over. Kaz and Mags had both been at their desks on the real day, which Ines said made it a better drill rather than a worse one. She covered their 2025 decisions with yellow sticky notes and told them to write as if they could not remember. Kaz said they could not remember. Mags said she remembered everything and would write anyway.

"Context," Ines said. On Wednesday 2 April 2025 the United States announced sweeping new tariffs, and markets spent the next three sessions working out what that meant. Monday 7 April was the day the wrapper took over the bond market's job: about \$99bn of fixed income ETFs traded, roughly 60% of it in iShares funds (The DESK, 10 Jun 2025). "That's the Monday. We are at 7:45 on Tuesday the eighth."

**7:45 a.m.** The first thing on the desk's screen that morning had been a ratio. The desk tracks credit ETF volume against cash bond volume, because the ratio says which instrument the market is using to move risk. In a calm year it drifts; Coalition Greenwich put it at 16.6% for 2024, down from 23.2% in 2022 (the Trend Watch at the end of this section). On the desk's own blotter for the Monday it was running at a multiple of the calm number *(the desk's fictional run)*. "When that ratio jumps, the ETF is the market and the bonds are a rumour of one," Ines said. "Whatever we do today goes through the wrapper or it doesn't go." On the cash side Tuesday would become a then-record of its own, \$89.7bn of US corporate bonds traded, 12% of it in portfolio trades by Trumid's count (Coalition Greenwich, 14 Apr 2025). Nobody at 7:45 knew that. What they knew was that the phones had been lit since six.

**9:20 a.m.** The request came in over the portfolio-trading protocol for a 10:00 response: one price for 150 high yield bonds, \$250mm of face, mostly single-B, a dozen of them names that had not printed on TRACE since the previous Thursday *(illustrative)*. Kaz's engine had a level before the coffee arrived. Chapter 19 builds that engine; what mattered here was the exit. A dealer that buys 150 bonds at once owns 150 inventory problems, and Kaz did not intend to solve most of them one at a time. The desk had an AP agreement with the sponsor of a large high yield ETF *(fictional)*, and about 110 of the 150 lines sat in that fund's index. "Custom creation basket," Kaz said. "We deliver those 110 lines straight into the fund, take shares, and sell the shares into a market doing ninety-nine billion a day. The PT is our axe vector. It's the textbook case."

It was. In (20.6) the AP's axe $a$ is whatever it already owns and wants gone, and here that was the portfolio the desk was about to buy; the custom basket is the fund agreeing to tilt toward exactly those bonds. The other forty lines, the off-index names, Kaz would work the old way, one RFQ at a time. The engine wanted composite minus 90 bp of price for the package, a level that assumed the basket. Its own run of (20.7) on the 110 index lines valued the custom basket at about 40 bp of the package *(the desk's fictional run)*. Without the basket the same engine would have wanted composite minus 130: forty basis points of the bid's generosity existed only because a fund was expected to take the bonds off the desk's hands that afternoon and give back shares the desk could sell in a minute.

**9:52 a.m.** Ines's phone rang. The sponsor's capital markets desk, the people who review custom baskets under the written procedures of Rule 6c-11 (§20.4.1), was calling its APs one at a time with the same message: until further notice, creations and redemptions in the high yield fund would be pro rata only, no custom baskets *(fictional; nothing here describes a real sponsor's decision)*. It was a reasonable call for a fund to make. In a week when every AP wanted to hand the fund its least favourite bonds, the procedures existed to keep $k$ honest, and the simplest way to keep $k$ honest was to stop negotiating it.

Kaz's exit was gone. A pro rata creation would have meant buying the other twelve hundred bonds in the fund to go with the 110 the desk was about to own, which was not an exit but a second problem. With $w$ forced to $h$, (20.7) says what was lost: all of $\mathcal{D}/(2\theta)$, the forty basis points that two minutes earlier had been part of the bid. The quadratic program had priced a basket the sponsor was willing to negotiate. It had nothing to say about whether the sponsor would, and at 9:52 that was the only question on the table.

Mags had watched it happen before, from the client's chair. "First half of 2022," she said. "I was at a fund that was getting smaller, and we sold by portfolio trade because we had to sell by something. The bids kept coming back worse than the rates move explained, worse than the spread move explained, and nobody on the phone would tell me why." Man's quants put it in writing a year later: the loss of customised baskets for ETF creation and redemption was "likely to have been another aggravating factor" in the rise of portfolio-trading costs in the first half of 2022 (the Source Extraction after this scene). "It was the basket," Mags said. "The dealers had lost their back door, and they charged it to my front door."

#### Decision point: 9:55 a.m., 8 April 2025

Ines put the tape down. "Five minutes to the response. Write three things. Your bid for the package, in basis points of price to composite. Whether you make it conditional on a custom basket. And what you do with 150 lines at four o'clock if nobody takes them off you." If you are reading along, write yours before the next paragraph.

Kaz wrote "−90, firm, deliver the index lines when the sponsor reopens, work the rest." Ines peeled back the yellow note over the 2025 blotter: −90, firm, sent at 9:58, six minutes after the sponsor's call. "I thought they'd reopen by Thursday," Kaz said. "I still think that's what I'd have thought." Theo wrote two prices, the way he used to write the two tranches of a fee letter: "−140 firm now. −90 if the sponsor reopens custom baskets before the client has to trade; say so in the response. At four: hedge the spread risk with CDX HY and the ETF, and sell down in whatever size the street will take." The fifty-point gap was the forty the basket was worth plus ten for the extra days of holding forty-odd more lines *(illustrative)*. Mags's 2025 note said "Pass. Not our balance sheet this week," and her replay card said the same thing in fewer words.

The grading started with what happened. In 2025 the desk sent Kaz's −90; Ines had let it go, and said so. The desk won the trade at 10:00, because on a day like that an unconditional bid near composite is what wins. By four it had sold twenty-odd lines through single-bond RFQs, hedged about half of the remaining spread risk with CDX HY and a short in the ETF, and carried 120-odd bonds into the night *(the desk's fictional blotter)*. On the Wednesday afternoon, 9 April, the White House announced a 90-day pause on most of the new tariffs, and risk rallied hard. The desk's unhedged half made money. Thursday's explain, run the way the desk runs every explain, told a different story. Strip the rally (beta, which anyone could have bought through an index for a few basis points) and the trade had lost almost exactly the forty basis points that the sponsor's phone call took away, on the bonds sold before the announcement and on the hedges' slippage after it *(the desk's fictional run)*. "You were paid by the White House," Ines told Kaz, "not by the model. IDO or it didn't happen."

So the cards were graded against that. Kaz's unconditional bid gave away $\mathcal{D}/(2\theta)$ the moment the basket was refused, and was rescued by an announcement no card had mentioned. Theo's two-price card would probably have lost the trade, and it lost nothing; it priced the basket as what it was, a state variable that could flip at 9:52, and it is the bid that Man's 2022 experience endorses. Mags's pass was right for a desk whose balance sheet was already spoken for, and it would have been wrong for a dealer with room, because room is exactly what the wrapper was paying for that week. If your card assumed the basket without saying so, you made Kaz's bid. If it bid as though the basket might vanish, you made Theo's. And if it asked whose balance sheet would hold 150 lines at four o'clock before it asked what they were worth, you were asking the cold open's question in a different week.

Somebody was paid to be the wrapper's balance sheet that week. Three months later Virtu Financial told its shareholders that its ETF block business had "another record quarter," on client demand around the tariff volatility (Q2 2025 earnings call, 30 Jul 2025). The call did not break out bond ETFs, so tying it to this wrapper is our inference, not Virtu's: the firms paid for that week's volume were the ones that traded the wrapper in size, which is a different job from owning the bonds inside it.

"A custom basket isn't ours," Ines said, turning the blotter face down again. "It's a favour a fund does an AP when the fund can afford to. The day you need it most is the day it can't."

**Ines's hand history.** Ines replays custom baskets through markouts. For each bond that appears in a redemption basket on day $t$, she records its composite price change, net of the move in CDX HY, from the basket date to $t + 1$, $t + 5$ and $t + 20$. *IDO or it didn't happen*: without the CDX adjustment, a market-wide sell-off would look like a basket effect. On the desk's synthetic replay, redemption-basket bonds underperform their hedged peers over the first few days, as the APs' bids hit the street, and then partly recover *(illustrative; the pattern matches the basket-pressure mechanism in Koont et al., but the magnitudes are the desk's toy numbers, not a published estimate)*. The first leg is the cost the AP charged for the basket. The recovery is the fee a patient balance sheet earns for buying what the AP had to sell.

> **[SOURCE EXTRACTION]** *Man_Revolutions_in_Credit_Trading_2023 p.3:* "The new market environment of higher volatility and quantitative tightening may also have left dealers inclined to commit less of their balance sheets to bond trading. The loss of customised baskets for the ETF creation/redemption process is likely to have been another aggravating factor."
>
> **Annotation.** Man is explaining why portfolio-trading costs rose in the first half of 2022, and both of its causes appear in our equations. "Less balance sheet" is a higher $\bar\gamma$ in (20.5). "The loss of customised baskets" is the forced $w = h$ in (20.7), which removes the outlet a PT dealer used to recycle basket risk into an ETF. The two are complements, not substitutes. A dealer with less balance sheet needs the custom basket *more*, because it cannot afford to hold the PT's odd lots while it works them. Man attributes the loss only in general terms, and we do not know which sponsors narrowed their basket practices or for how long. The 2026 desk should therefore treat custom-basket availability as a time-varying state variable. Estimate it from the overlap between published baskets and holdings (the Shim–Todorov coverage ratio), and widen PT bids when it falls.

> **Trend Watch: the basket triangle, ETF ↔ portfolio trade ↔ cash (2021–2026).** *What changed:* portfolio trading and ETF primary flow became substitute ways to move basket risk. Man calls 2021 "the year of portfolio trading," attributing the boom partly to bond ETF growth (Man 2023 p.2), and records PT costs rising in H1 2022 as custom baskets were lost (p.3). *How big:* credit ETF average daily notional volume was \$7.7bn in 2024, down 7%, while cash-bond volume grew 21%, so the ETF-to-cash volume ratio fell from 23.2% in 2022 to 16.6% in 2024 (Coalition Greenwich, January 2025). In February 2024 credit ETFs were 17% of bond notional volume, the lowest since Q2 2021 (The DESK, citing Coalition Greenwich, 2024-03-19). The TRACE portfolio-trade modifier became mandatory on 2023-05-15 (FINRA Regulatory Notice 22-12), which made PT flow visible. *Stress check:* ETFs reclaimed the stage when markets broke. About \$99bn of fixed income ETFs traded on 2025-04-07, roughly 60% of it in iShares funds (The DESK, 2025-06-10). *What it means:* in calm markets, institutions move risk in the bonds themselves through PT and the ETF share of volume falls. In stress, the ETF is again the only instrument that trades at size. A desk's routing logic should switch between ETF hedges, PT and cash execution using the ETF-to-cash ratio and the ETF discount as regime signals, and it should price custom-basket availability into PT bids.

## 20.5 Case Study: March 2020, When the ETF Was the Only Price in Town

"Back in 2008," Mags said, "there was no ETF to blame. The bonds just stopped trading, and we marked them wherever the auditors would let us. Nobody saw the discount, because there was nothing to be at a discount *to*." She paused. "In 2020 the ETF told everyone the truth at 4 p.m. every day, and they hated it. I'll give it that. It was honest."

*A replay, run as Ines's ritual: the clock is cut at each close and the cast trade it blind. The cast, their cards and the Pair Book's sizes are fictional and illustrative; every market fact is real, and is cited where it appears or in the tape at the end of §20.5.1. Mags spent the real March 2020 on a dealer's distressed desk, and Chapter 1 has her run sheets.*

### 20.5.1 Nineteen March 2020: the only price in town

#### Recalled: Thursday 12 March

Ines started the clock a week early, for one paragraph, because the week before was what everyone in the room was carrying. On Thursday 12 March LQD "traded almost 90,000 times," while "its top five holdings traded an average of 37 times" (Salim Ramji, global head of iShares, BlackRock Q1 2020 earnings call, 16 Apr 2020). That evening a UCITS investment-grade ETF closed about 7.5% below NAV and the largest US floating-rate bond ETF about 8% below (the tape). Chapter 1 (§1.8.2) replays that Thursday and the Friday after it, when LQD's own 5.0% discount came in to 0.19% because, in Mags's telling, the bonds had caught down to the ETF. "That was the rehearsal," Ines said. "This is the show."

#### Thursday 19 March: three readings, one discount

"Close, Thursday 19 March," Ines said, and wrote two numbers on the whiteboard. LQD had closed at a 5.08% discount to NAV. HYG had closed at a 0.85% *premium*. On the same afternoon, MSCI found later, the dispersion of traded prices for identical IG bonds reached its peak (the tape). Then she sat back and let the three readings of §20.2.3 have their argument.

Kaz went first and began where their own reading says to begin, with the staleness term, because it is the one piece of a discount that can be measured from public data before anyone has an opinion. They ran (20.3) on a calm window from the previous autumn, took the slope as $\eta$, and pushed the ETF's own returns for the past fortnight through (20.2) as a stand-in for the true returns. "After a fortnight like this, with an evaluator that closes a fraction of the gap each day, the model says a good part of the five points is the NAV being late. Two of them, maybe three *(the desk's fictional run)*. That part isn't a trade. It's tomorrow's marks." Ines pointed at the second number on the board. "And high yield?" Kaz looked at it for a long time. "Staleness should be worst where the bonds trade least. If staleness were the whole story, high yield would have the deeper discount." It had a premium.

That was Ines's opening, and she took it. "Then something pushed investment grade's flow term far below high yield's. Who sells IG in a panic? People who need cash and can still sell something. They sold what they could sell." Put through (20.1), the high yield premium is the most informative number on the board: a staleness-only story predicts the deeper discount in high yield, the data show the opposite, and Haddad et al. name the force that did it, investors selling the most sellable risky asset they owned, which in March 2020 was a large, liquid, high-quality bond ETF. "Quality-flight usually means buying quality," Ines said. "When the problem is cash, it means selling it."

Mags had her run sheets out again. "I was marking IG paper that week from the other side of a dealer's desk. Same CUSIP, three prints, three points apart, same afternoon. Ask me where the true price was and I'll tell you it was somewhere in a range, and on half those names the range was wider than your discount." MSCI's dispersion peak is her run sheet turned into a statistic, and a discount inside that range, $|p_t - \bar c| < u_t$, cannot be told apart from zero. Figure 20.4 puts the reported discounts on the same date axis as an investment-grade spread.

![Figure 20.4: The Baa-Treasury spread peaked on March 23, the day the Fed announced the SMCCF, after ETFs had closed 5 to 8% below NAV on March 12 and March 19 while HYG closed at a premium on March 19. Source: FRED BAA10Y (Moody's Baa yield minus the 10-year Treasury yield, daily); premiums and discounts as reported by BlackRock ViewPoint (July 2020) and MSCI (Bohák & Janosik, 2020-04-08); SMCCF dates from the Federal Reserve and NY Fed.](assets/figures/ch20_march2020_tape.png)

<!-- FIGURE: ch20_lqd_hyg_premium_mar2020.png (data series: LQD and HYG daily premium/discount, 2 Mar to 30 Apr 2020, from iShares premium/discount history; markers at 12, 19, 23 Mar and 9 Apr; CDX IG overlay if a source is available, else BAA10Y. Caption: "LQD at -5.08% and HYG at +0.85% on the same close: the discount lived in the wrapper people could sell." RV thread figure for PB-13) -->

#### Decision point: 3:40 p.m., 19 March 2020

Ines dealt three cards. "LQD is five under. Write one of three things, redeem, buy-and-hedge or pass. Then a size. Then what you need to be true." If you are reading along, write yours too.

Kaz wrote: "Redeem, \$100mm. Need: the basket sells at NAV less the half-spread within a week." Take the staleness out, Kaz reasoned, and two-odd points of flow were left, far outside any band, and an AP's edge is an AP's edge.

Theo wrote: "Buy \$50mm LQD. Buy CDX IG protection, DV01-matched; Treasury futures for the rates. Need: the discount is mostly flow, and something stops the selling before my stop does." It was PB-13, the pair in §20.3.2, and the size came from (20.5) rather than from the edge. Theo had read $\psi$ the way he used to read a revolver's springing covenant, for the condition under which it bites, and that week every factor in $\psi = \bar\gamma \sigma_b^2 T^{\text{h}}$ was blowing out together: dealer balance sheets were constrained, so $\bar\gamma$ rose; the basis between any redemption basket and any hedge turned violent, so $\sigma_b$ rose; and the time to work out a basket of short, wide IG paper stretched from days into weeks, so $T^{\text{h}}$ rose. Meanwhile $F$, the net selling, was peaking. A multiplicative price impact meeting a flow spike is the 288 of §20.3.2 in motion, and it can double before it halves. So he sized for a doubling: ten points on \$50mm is \$5mm, which the pod's stop could absorb, and on Kaz's \$100mm it would not have been *(illustrative)*. "The edge tells you whether to play," he said. "$\psi$ tells you how wrong you can afford to be about when."

Mags wrote "Pass," and under it one line: "The basket is the bonds I can't sell." "On the nineteenth I was the one being offered those baskets," she said. "The bid side of my run sheet is what you'd be selling into, Kaz, and it wasn't there."

Ines collected the cards and graded nothing. "Turn the tape over."

#### The tape

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

The rows after the nineteenth are the rest of the replay, and the first of them changed every card on the table.

### 20.5.2 The Fed buys a seat at the table

On Monday 23 March the Fed announced the SMCCF, and the IG ETF rose about 7%, roughly 70 bp of yield on a duration near 9.5 years, while high yield barely moved (the tape). The March 23 announcement and the July 28 term sheet are worth reading as market-microstructure documents, because the Fed wrote the arbitrage band into them. The SPV would buy "eligible corporate bond portfolios in the form of exchange-traded funds," with "the preponderance" in ETFs targeting US investment-grade bonds and "the remainder" in high yield ETFs. Leverage was 10:1 on IG ETFs and 3:1 to 7:1 "depending on risk" on other eligible assets. The facility would not hold "more than 20 percent of that ETF's outstanding shares." And it would "avoid purchasing shares of eligible ETFs when they trade at prices that materially exceed the estimated net asset value of the underlying portfolio" (SMCCF term sheet, effective 2020-07-28). The mirror clause for the exit was that it would "avoid selling shares of an ETF at times when it is trading at a price that is materially below" estimated NAV (NY Fed).

In the language of (20.4), the Fed promised to buy *inside the band, never above it*. It would not pay a premium the APs could arbitrage away by creating shares against it. It would also not sell into a discount that it had itself been brought in to close.

Four days after the announcement the New York Fed signed a "Terms of Assignment" with BlackRock's Financial Markets Advisory unit to manage the secondary-market facility (27 Mar 2020), and its conflict clauses read like a seating plan drawn for the absent player of §20.4.3. The staff on the engagement were "segregated from other BlackRock engagements and activities." BlackRock would charge "no asset management fee on the value of any exchange traded funds" held by the facility, and would credit back the fees it earned on its own iShares there. It would "treat BlackRock-sponsored ETFs on the same neutral footing as third-party ETFs." And if the facility's holdings of BlackRock ETFs exceeded BlackRock's market share of corporate bond ETFs, the firm had to tell the New York Fed, which "may direct portfolio adjustments at any time." The buyer of last resort was built with a conflict-of-interest architecture because its manager also sponsored the product that would become its largest holding.

The Fed has been doing open market purchases since long before the phrase became the most expensive three words in leveraged finance. In 2020 it did one in LQD. The transaction-level disclosure for January 2021 shows what it bought (Federal Reserve, SMCCF transaction-specific disclosure, "Position Summary-ETF" tab). Sixteen ETFs had a combined market value of about \$8.78bn at 2020-12-31 (our sum of the tab). LQD was the largest position at \$2.47bn, followed by VCSH at \$1.52bn and VCIT at \$1.44bn. The seven high yield funds (ANGL, HYG, HYLB, JNK, SHYG, SJNK, USHY) together came to about \$1.16bn, roughly 13% of the ETF book: JNK \$576mm, HYG \$338mm, the rest smaller. That is what "preponderance" looks like in a spreadsheet.

The striking fact is how little buying it took. ETF purchases did not start until May 12, seven weeks after the announcement, by which point the discounts were long gone. Gilchrist, Wei, Yue and Zakrajšek ("The Fed Takes on Corporate Credit Risk," NBER w27809; *JME* 2024) estimate that the announcements cut eligible-bond spreads by about 70 bp in an eligibility-boundary design (about 20 bp within issuer), and that the March 23 announcement cut bid–ask spreads by about 10 bp within ten days. Actual purchases added only about 5 bp on spreads and 2 bp on bid–ask. In (20.5), the announcement worked by lowering $\bar\gamma$ and $\sigma_b$ for every AP at once. A dealer that knows a buyer with a \$750bn combined facility stands behind the basket's tail risk is a dealer with a lower price of risk. The Fed did not need to fill the hole. It needed the APs to believe the hole had a floor.

> **Poker Table.** "The Fed is the only player who can announce its hand and still win," Ines said. "It showed everyone a stack, said it would only call at fair value, and the table repriced before it put a chip in." Theo asked whether that counted as bluffing. "It's the opposite. A bluff is a bet you can't back. This was a bet so big nobody wanted to see it."

One firm, meanwhile, was sitting in more than one seat at that table.

> **View From Another Seat.** *The sponsor with three chairs.* In March 2020 BlackRock sat on three sides of the same market. As the sponsor of iShares, its global head of iShares, Salim Ramji, gave the 90,000-against-37 count for LQD quoted above, and on the same earnings call (16 Apr 2020) Larry Fink, asked about criticism of the Fed buying ETFs, replied "I object to your -- the way you framed it as a bailout." As the Fed's agent, its advisory unit worked under the 27 March Terms of Assignment, with the fee waivers, the "same neutral footing" clause and the market-share notice. And as a systematic credit manager, BlackRock Systematic Fixed Income ran quant credit portfolios, and its own undated high yield paper argues that the average manager turns defensive at the wrong time (the paper's figures are for 2022 and 2023, not 2020). On our reading, each chair measured the month differently: the sponsor by the trades its wrapper absorbed, the agent by the rules that kept it from favouring its own product, the systematic manager by whether it bought or sold into the dislocation. The clauses are there because the chairs face different directions.

### 20.5.3 Grading the cards: how a systematic desk would have flagged and traded it

Ines graded on the Friday, with the explain sheet in front of her instead of the tape.

Kaz's redemption worked, and it worked for a reason that was not on Kaz's card. Redeeming \$100mm of LQD on the nineteenth would have handed Kaz short, wide IG paper at the bid on one of the worst days of the year, and with it the whole $\sigma_b^2 T^{\text{h}}$ that the AP channel was charging for. The desk would have owned those bonds into Monday's announcement, which rescued them, as the Ways This Blows Up box below records. "You needed the Fed to be true," Ines said, "and you didn't write it down."

Theo's hedged long earned the convergence and, under the desk motto, only the convergence. LQD's roughly 7% jump on March 23 was mostly spread tightening, which is beta anyone could have bought in any IG instrument, and the CDX leg gave most of it back, by design. Only the part attributable to convergence of the discount was the arbitrage. On PB-13's \$50mm, bought at a 5% discount and hedged for rates and CDX IG beta, the convergence leg was worth on the order of \$2.5mm if the discount fully closed *(illustrative: the exact split between beta and convergence depends on the hedge ratio and on which NAV you believe)*. The leaks of the Pair box took their share, the CDX–cash basis most of all, and the carry was a few days of index premium. Measured net of the hedge, the pair made money; measured any other way, it made a claim. IDO or it didn't happen.

Mags was right about the basket and wrong about the trade. The basket was exactly the bonds nobody could sell, which is why Kaz's card needed a miracle and Theo's card never touched the basket at all. "You were right about what was in the box," Ines told her. "The trade was the box."

> **View From Another Seat.** *The quant-fundamental fund as the forced seller's counterparty.* In the same fortnight, across a different discount, D. E. Shaw says it "purchased in excess of \$400 million in CAS and STACR bonds at a significant discount to par" over March and April 2020. Those are mortgage credit-risk-transfer bonds, and the firm says the asset managers and REITs that held them "were put under stress by redemption requests and margin calls"; it puts the B-1 index of the bonds just below 50 on 7 April (D. E. Shaw group, "Assessing U.S. Mortgage-Backed Credit Stress in 2020," originally November 2020). Our inference, not the firm's: the seat that profits from a forced sale is the one whose own capital cannot be redeemed that week, which is the property Theo was buying when he sized PB-13 to survive a doubling.

The reader's card is graded against the papers. A card that redeemed because the NAV was late has Haddad, Moreira and Muir against it: there was no discount in high yield when the IG discounts were deepest, which is evidence against a pure staleness story (§20.2.3), and a late NAV is nothing an AP can redeem its way into. A card that bought and hedged in expectation of convergence learns from Gilchrist and coauthors where the payment came from, mostly the announcement and barely the purchases (§20.5.2). And a card that passed was in good company and in the wrong seat. Passing was the right card for a holder of bonds; buying the wrapper was the card a holder of spare balance sheet could afford to play.

What each card lacked is a monitor the desk now runs, and each comes from a piece of this chapter. Kaz's card lacked a band-breach flag that knows what it is for. With live half-LCS inputs, (20.4) puts LQD's calm lower edge at about −6 bp, and −5% was some 500 bp outside it, which is a regime flag, not an entry signal. It also lacked the staleness share, done to the end: estimate $\eta$ from (20.3) on a trailing calm window, compute the staleness that the ETF's recent returns imply, and if the implied $s_t$ explains most of the discount, the NAV is late, the "discount" will close by itself as the marks fall, and there is nothing to trade. Mags carried the third monitor in her head and on her run sheets: the measurement width, the same-day dispersion $u_t$ of TRACE prints across the basket's bonds, inside which a discount is noise. Theo's card had the fourth without naming it. Back out $\psi$ from (20.5), using the change in shares outstanding as $F$; a rising $\psi$ means the AP channel is congested. The trade that survives all four filters is not "buy ETF, redeem, sell bonds," which hands the redeemer the basket and its $\sigma_b^2 T^{\text{h}}$. It is to **supply balance sheet in the wrapper**: PB-13, hedged for rates and spread beta, sized so that a doubling of the discount is survivable, and waiting for $F$ to normalize.

> **Ways This Blows Up.** *The NAV-return backtest.* A backtest that computes ETF strategy returns from NAV instead of traded prices buys at stale marks and sells at stale marks, and it reports a smooth equity curve through March 2020 that no one could have traded. *The redemption that kills you.* An AP that redeemed LQD on March 19 owned the basket's bonds into the March 23 announcement, which worked out. One that redeemed a cash-only fund paid fees capped at 2% (§20.3.1) and was the lucky one, at the remaining holders' expense. *The phantom arbitrage.* A monitor that alerts on $P_t - \text{NAV}_t$ without the bid-side constant $\bar c$ flags every calm day as a "premium" and stops being read by Tuesday.

## 20.6 BKLN: The Basket That Cannot Settle

"But what does the credit agreement say?" Theo asked. For once, it was exactly the right question about an ETF.

Nobody answered, so he answered it himself. He opened a syndicated term loan agreement of the kind he had read a few hundred of at PJT, scrolled past the definitions to the article on successors and assigns, and read the clause aloud in the voice he used to use for the parts of a document a client had not read. *(The clause is generic, a composite of common market language rather than any particular agreement.)* "'Each Lender may assign to one or more assignees all or a portion of its rights and obligations under this Agreement, with the prior written consent of the Borrower, such consent not to be unreasonably withheld or delayed; *provided* that the Borrower shall be deemed to have consented unless it objects by written notice to the Administrative Agent within ten Business Days; and with the consent of the Administrative Agent; *provided further* that no assignment shall be made to a Disqualified Institution.'"

"Disqualified," Kaz said. "For a false start?"

"For being a competitor of the borrower," said Theo, "or a fund the sponsor doesn't want in the room when the company needs an amendment."

"For being me," said Mags.

That clause is the whole of §20.6. A leveraged loan is not a security that clears at DTC. It moves by **assignment** under the credit agreement, which typically requires the administrative agent's consent, often the borrower's consent (which may be deemed given after a set number of days, as in Theo's ten Business Days), and a check against the **disqualified lender list**. Settlement has historically taken weeks rather than days: Markit data reported an average of 17 days in Q2-2016 *(Markit data via Morningstar, 2017, a secondary source; Chapter 21 owns current LSTA settlement statistics)*. ETF shares settle T+1. A loan ETF that redeems on a Monday owes cash on Tuesday for loans it will not be paid for until well into the following month. The fund pages admit it in their own fine print. State Street's SRLN, a senior loan ETF, says on its fund page that its calculations "are performed on a trade date basis and are intended to include both settled and unsettled positions" (SSGA SRLN fund page, data as of 15 Oct 2026): on paper the fund counts loans it has not finished buying, and has stopped counting loans it has sold but not finished delivering. "So the page is a 13-week forecast," Theo said, "with the receipts already booked."

That is why BKLN's structure looks the way it does. The fund "will normally invest at least 80% of its total assets" in the components of the Morningstar LSTA US Leveraged Loan 100 Index (Invesco). Press and fund literature describe the rest as a sleeve of cash and more liquid high yield bonds of about 10%, a tilt toward the largest loans and a line of credit for "emergency liquidity events" (Morningstar via Benzinga, 2017), and describe loan ETFs generally as meeting redemptions largely in cash; the current prospectus is the document that settles both points for any given year. Rule 22e-4 (adopted 2016-10-13, SEC press release 2016-215) caps illiquid investments at 15% of net assets, where "illiquid" means an asset that cannot be sold within seven calendar days without significantly changing its market value. For loan ETFs, in-kind delivery of assignments to an AP is impractical, so the cash channel and its 2% fee ceiling are the relevant economics.

### 20.6.1 Derivation: the settlement gap and the liquidity runway

First, the band. For a cash redemption, the fund pays out on day $t + 1$ and receives loan-sale proceeds after a lag of $L$ years. The redemption cost in (20.4) gains two terms. One is the financing of the gap, $r L$. The other is the price risk on loans sold but not settled, which a risk manager charges in proportion to the square root of the lag.

> **Math, Gently.** *Risk grows with the square root of time.* Picture a drunk leaving a lamppost, taking one step a second, each step left or right at random. After a hundred steps he is not a hundred steps away; most of the steps cancel, and his typical distance is about ten steps, the square root of a hundred. Variances add over time, so the standard deviation, the typical size of the move, grows with the square root of time. A loan sold today and settled in seventeen days is a drunk the fund has to keep an eye on for seventeen days. Tiny number: a loan price volatility of 10% a year, in stress, and $L = 17/365$ of a year. Then $10\% \times \sqrt{17/365} = 10\% \times 0.216 = 2.16\%$ is one standard deviation over the lag, and a risk manager who wants two of them ($z = 2$) charges about 4.3%. Set that beside the financing term at 5% a year, $5\% \times 17/365 \approx 0.23\%$. For short lags the risk term dwarfs the financing, because the square root of a small number is much bigger than the number itself. Halve the lag and the financing halves, but the risk term falls only by about 29%. The algebra follows.

The redemption cost becomes

$$
k^R_{\text{loan}} = k^R + r L + z\, \sigma_{\text{loan}} \sqrt{L}.
$$

At $L = 17/365$, $r = 5\%$ and $\sigma_{\text{loan}} = 10\%$ in stress, the financing term is about 23 bp and the risk term with $z = 2$ is about 4.3% *(illustrative)*. Most of that cost is not charged to the AP, because the fund absorbs the gap through its sleeve.

Second, the sleeve. Let $\phi_t$ be the sleeve as a fraction of the fund and $R_t$ the redemptions in week $t$ as a fraction of the fund, with loan-sale proceeds arriving $L_w$ weeks after the sale. Under a constant redemption rate $\bar R$, the sleeve survives the settlement gap if and only if it covers the lag, and its runway is cash over burn:

$$
\phi_0 > \bar R\, L_w, \qquad \text{runway} = \frac{\phi_0}{\bar R} \text{ weeks}. \tag{20.8}
$$

#### The Full Derivation: the settlement gap

Suppose that each week the fund pays redemptions out of the sleeve and sells loans to refill it, with sale proceeds arriving $L_w$ weeks later. Then

$$
\phi_{t+1} = \phi_t - R_t + R_{t - L_w},
$$

and the sleeve survives as long as $\phi_t > 0$. Under a constant redemption rate $R_t = \bar R$ starting at week 0, the sleeve falls by $\bar R$ per week for the first $L_w$ weeks and is flat afterwards (inflow equals outflow), so it survives if and only if $\phi_0 > \bar R L_w$, which is (20.8).

#### The runway in March 2020's weather

Plug in March 2020's pace. The SEC staff report records that Morningstar high-yield bond funds and ETFs lost 9.2% of January assets in March, or about 2.1% a week. With $L_w \approx 2.4$ weeks, the requirement is $\phi_0 > 5\%$. A 10% sleeve has a runway of nearly five weeks, comfortably more than the lag *(illustrative; this uses the HY category's outflow rate, not loan funds' own March 2020 outflows)*. Double the pace to 4.2% a week, as if the same outflow were concentrated into half the time and kept up through the whole settlement lag, however, and the requirement doubles, which is when the credit line earns its fee. Figure 20.5 draws both cases.

![Figure 20.5: A loan ETF's liquidity sleeve must cover the weekly redemption rate times the 2.4-week settlement lag, so a 5% sleeve falls just short of a steady 2.1% weekly outflow, and doubling the outflow rate doubles the sleeve needed. Illustrative: the sleeve recursion (20.8) with each outflow rate held constant from week 0, the 17-day loan settlement lag (Markit, Q2 2016, via Morningstar) and the weekly rate implied by the 9.2% March 2020 outflow from high-yield bond funds in the SEC staff report.](assets/figures/ch20_sleeve_runway.png)

Theo stared at (20.8) for a long time. Then he took the USB stick out of his pocket, which on Thursday he had only touched. "This is the 13-week model," he said. "It's the sentence I said in the cold open with a number attached. You survive if your cash covers the lag, and the runway is cash over burn." He turned the stick over. "And it lies the way my 13-weeks used to lie. It treats the lag as a constant. In a bad week the lag gets longer in the same week the burn gets faster, because the agents are as swamped as everyone else, and then the recursion is right and the inputs are wrong." Kaz wrote that down, which from Kaz is the highest compliment on offer. The 13-week cash flow model has now been a survival curve, a state-space feature and the liquidity-runway input to the Priming Risk Score. Here it reappears as the liquidity sleeve of a \$6bn ETF, and it has never been better dressed.

### 20.6.2 What the wrapper is now being asked to hold

The loan ETF is the cautionary template for the wrappers of 2025–2026. The SPDR SSGA Apollo IG Public & Private Credit ETF (PRIV) launched in late February 2025 with a contractual arrangement for Apollo to provide intraday bids on the private credit it sources. Press coverage in the days around the launch reported a public letter from SEC staff raising liquidity (Rule 22e-4), valuation and naming concerns. From Apollo's own seat the wrapper exists for the assets, not the plumbing. A year later its co-president John Zito put the case this way: "We're in this unique time where we need multiple trillions of dollars, for AI, power, infrastructure, chips and all of that requires very bespoke, long-duration capital that's not traditional to the CUSIP market" (Apollo, "Private Credit, Now in an ETF," 4 Mar 2026). Read beside (20.8), "not traditional to the CUSIP market" is the settlement problem stated as a selling point: the more bespoke the asset, the longer its $L$, and the more of the band lives in somebody's contractual bid rather than in an AP's spreadsheet.

The loan wrapper, meanwhile, grew in a different direction. US CLO ETF assets passed \$50bn in July 2026, per BofA research as reported by Octus (7 Jul 2026), and JAAA, the largest, passed \$30bn in August (Janus Henderson, 13 Aug 2026). A CLO tranche is a security that clears like a bond rather than an assignment that settles like a loan, which may be part of why that wrapper scaled faster than BKLN's; Chapter 21 takes up the loans and the CLOs behind it. On 2025-11-17 the SEC granted Dimensional exemptive relief to offer ETF share classes of mutual funds, followed by a combined notice to 30 applicants on 2025-12-22 (Seward & Kissel 40 Act blog). A bond mutual fund with an ETF share class could route redemptions through the ETF class, which would make the custom-basket machinery of §20.4 the exit door for a much larger pool of 1940 Act bond money, to the extent that bond complexes take up the relief. Every one of these structures inherits (20.8). The question for each is the same one Theo asked about BKLN: what is the settlement lag of the assets, and what covers it?

> **Trend Watch: the regulatory plumbing of the wrapper (2016–2026).** *2016-10-13:* the SEC adopts Rule 22e-4, with its four liquidity buckets, a 15% illiquid cap and a carve-out for "In-Kind ETFs"; compliance followed on 2018-12-01 for large fund complexes and 2019-06-01 for smaller ones (SEC press release 2016-215). *2019-09-26:* Rule 6c-11 adopted, effective 2019-12-23, which standardizes baskets, custom-basket procedures and premium/discount disclosure (SEC press release 2019-190; Release 33-10695). *2020-03-23 to 2021-12-17:* the SMCCF is announced, buys ETFs from 2020-05-12, ends purchases on 2020-12-31, begins selling ETFs on 2021-06-07 and has sold all of them by 2021-08-31; the SPV is terminated on 2021-12-17 (Federal Reserve; NY Fed). *2024-05-28:* the US equity and corporate bond settlement cycle moves to T+1, which widens the gap between ETF settlement and loan settlement by a day. *2025:* PRIV launches with a contractual liquidity provider, and the SEC grants the first ETF-share-class relief. *What it means:* every rule since 2016 has made the wrapper easier to launch and more transparent, while the assets going into it have become harder to settle. The arbitrage band has therefore moved from the AP's spreadsheet into the fund's liquidity policy, and that policy is now the thing to model.

## 20.7 Building the Arbitrage Monitor

### Quant-Shop Life: Two Premiums for One Fund

*(A fictional composite. The shop, its people, its vendors, their documentation and their numbers are invented; HYG and Rule 6c-11 are real, and nothing here describes a real vendor's methodology.)*

On a Wednesday in October 2026, at the systematic asset manager where Noor now works on the data team (she owned `holder_hhi` in Chapter 13 and argued for the point-in-time archive in Chapter 15), the first ticket of the day is two numbers that should be one. The shop buys ETF analytics from two vendors. For Tuesday's close, Vendor A says HYG traded at a premium of +14 bp to NAV; Vendor B says −22 bp. The portfolio manager who filed the ticket wants to know which vendor is wrong, by lunch, because a rebalancing rule keys off the sign.

Noor starts where she has learned to start, by believing neither. She pulls both vendors' NAVs instead of their premiums. The ETF's closing price is the same in both files to the cent, so the whole disagreement lives in the denominator. Vendor A's documentation, three clicks deep, says its NAV is built from bid-side evaluated prices struck at 3 p.m., set against the 4 p.m. close. Vendor B computes its own indicative NAV from mid evaluated prices at 4 p.m. The bid–mid gap on a high yield book is about thirty basis points, and the hour between three and four, on a Tuesday when high yield drifted up, is worth about six more. Thirty-six basis points of disagreement, and each vendor exactly right by its own convention. The model review that approved the PM's rebalancing rule had checked its logic and never asked where its input came from, which is how a sign flip survived a sign-off.

That takes until 10:15. The second hour goes to the basket file. The rule also reads the fund's published redemption basket, and Noor wants to check Tuesday's basket against the holdings. The file in the shop's archive is stamped 9:10 a.m. Wednesday. The fund had published one version on Tuesday morning and a restated one on Wednesday, and the archive, built to keep "the latest," kept only the latest. Every backtest that used the basket as of Tuesday morning had been reading a file that did not exist on Tuesday morning. Nobody did anything wrong; a time machine had simply been left running.

Her fix is two lines in a design document and three days of plumbing. The ETF table gets a `nav_convention` field, bid or mid, read from the source's documentation, with no default, so that a missing value fails loudly instead of quietly taking whatever the last engineer assumed, and a `nav_strike_time` field beside it. The basket files join the point-in-time archive, which stores what arrived and when rather than what is true now. She answers the ticket at 11:50: "Neither vendor is wrong. They measure different things. Never subtract one from the other." Nobody upstairs notices the change, which on a data team is the whole point. The schema below has the same two fields for the same reason.

### Specification for AI Implementation

**The Spec You Hand the Robot (first draft).** *Vague version:* "Alert me when HYG trades away from NAV." *What ROBO built:* an alert on every close where price exceeded NAV. On a JNK-like year that is 206 alerts, all of them the bid-side constant $\bar c$. Theo said "only the big ones," so ROBO set the threshold at 2%, because that number appears in Rule 6c-11. It then stayed silent for eleven months and fired fifteen times in one week of March, each time after the close. *Precise version:* the six blocks below, in order. They run in one interpreter, each block uses the ones before it, and every block ends with sanity asserts.

**Data schema (one row per fund per day, plus holdings).**

| Table | Field | Type / unit | Notes |
| :--- | :--- | :--- | :--- |
| `etf_daily` | `date`, `ticker` | date, str | NAV strike date, not trade date, if they differ |
| | `close_px`, `nav` | float, \$ per share | `close_px` is the closing bid/ask midpoint; never the last trade |
| | `shares_out` | float | daily change × NAV is the primary flow $F$ |
| | `nav_convention` | {"bid", "mid"} | from the prospectus; required, no default |
| | `nav_strike_time` | time, ET | 15:00 vs. 16:00 matters for (20.1) |
| `holdings` | `bond_id`, `units`, `eval_mid` | str, float, points | evaluated mid per the pricing service |
| | `half_lcs` | float, fraction of price | $c_i$; LCS/2, see Dynkin p.702 |
| | `in_create`, `in_redeem` | bool | from the published basket files |
| `trace_disp` | `bond_id`, `date`, `u` | fraction of price | same-day half-range of institutional prints |

**Guards.** All premiums and costs are fractions of NAV; convert to bp only for display. Refuse to compute a band when `nav_convention` is missing. Drop days on which no NAV was struck (holidays, early closes). Flag any fund whose basket overlap with holdings falls below 5% for a review, because custom baskets are a state variable, not a constant.

By now the chapter has handed Theo six separate pieces of machinery, and a single premium alert needs all of them at once. The band comes from §20.3.1, the staleness measure from §20.2, the price of balance sheet from §20.3.2, the basket negotiation from §20.4.3, the runway from §20.6.1, and a final label decides which of those explains today's number. Done by hand at 3:40 p.m. on a day when HYG closes 60 bp under NAV, that is six derivations and one very tired vice president, and each derivation can quietly use the wrong convention. The desk's answer is the lesson of ROBO's 206 alerts. Write each piece as a function that carries its own test, run the pieces in order, and let an assert the night before catch the change that breaks a neighbor, instead of a P&L the morning after.

Listing 20.1 runs the six blocks of the specification in one interpreter, on a synthetic 120-bond high yield fund, and ends every block with asserts that tie the code to a numbered equation. Block 1 builds the fund, strikes a bid-side NAV and computes the value-weighted cost $\bar c$, about 36 bp on the seed. `static_band` returns the two edges of (20.4) as fractions of NAV. Block 2 simulates 4,000 days of a true log value, a stale NAV that closes 35% of the gap each day and an ETF price with 2 bp of noise. It checks the identity (20.1), then `nav_catchup` regresses the NAV change on the lagged premium and the slope is compared with $\eta$ times the staleness share. Block 3 prices the balance sheet. `clearing_premium` finds the premium at which identical mean-variance APs absorb \$2bn of net selling, and `ap_redemptions` confirms that the market clears. Calm and stress runs turn a 1 bp slope cost into 3.4%. Block 4 solves the custom basket twice, once in closed form (20.6) and once as an SLSQP program with $w \ge 0$, and asserts the value of freedom (20.7). Block 5 iterates the sleeve recursion (20.8) and returns the path with the first week it is exhausted. Block 6 is `classify`, where the order of the tests is the logic: inside the band, then measurement noise, then late NAV, and only then a flow label whose sign says redeem or create.

Use it as the regression suite for the chapter: change a convention and the asserts name the equation that moved. Do not use it as an estimator, because the data are simulated.

The edge case that bites is the NAV convention, the one Noor spent a Wednesday morning on above, and the code makes it easy to miss. `static_band` takes no `nav_convention` argument and silently assumes a bid-side NAV, so on the seed the band runs from about $-6$ bp to $+78$ bp. Block 1 recenters it for a mid-price NAV by shifting both edges down by $\bar c$, which gives roughly $\pm 42$ bp. The width never changes, only the center. A premium measured against mid NAV and judged against the bid-side band is therefore off by about 36 bp: $+50$ bp reads as inside the band when it is 8 bp past the edge. Read the convention from the prospectus first, or the schema's required field is decoration.

*The full listing is [Listing 20.1 in Appendix F](#code-20-1).*

The spec carries three more warnings, each learned from a different way the toy differs from production. A covariance matrix $\Sigma$ for 1,300 bonds is singular in practice, so the production version of Block 4 swaps `np.linalg.solve` for a factor-model covariance (Chapter 9) plus a diagonal, solved with a Cholesky factor. `nav_catchup` is biased toward zero whenever the flow term is noisy, which is the wobbling ruler of §20.2.2, so $\hat\eta$ is reported together with its attenuation bound and never on its own. And `classify` uses the model's $\hat s_t$, so it inherits the model's errors: on the day the pricing service changes its methodology, $\eta$ changes too, and the monitor falls back to `measurement_noise` until a new $\eta$ has been estimated.

## 20.8 Desk Debrief

The Finder: where each idea in this chapter is stated, felt, judged and coded.

| Concept | Equation | Intuition (box) | Judgment (scene) | Code (Listing 20.1) |
| :--- | :--- | :--- | :--- | :--- |
| Premium = flow + staleness + bid-side constant | (20.1) | A ratio chain and a relay (§20.2.1) | The cold open's 93 bp; three readings on 19 Mar 2020 (§20.5.1) | Block 2, identity check; Block 6, `classify` |
| Staleness as partial adjustment | (20.2) | The evaluator who closes half the gap (§20.2.1) | Kaz's staleness run before the card (§20.5.1) | Block 2 |
| Measuring how late the NAV is | (20.3) | A ruler with a wobbling zero (§20.2.2) | High yield's premium against Kaz's model (§20.5.1); Noor's two vendors (§20.7) | Block 2, `nav_catchup` |
| The static band | (20.4) | A room with two doors (§20.3.1) | Ines's "not yet" (cold open); JNK's census (§20.3.1) | Block 1, `static_band` |
| The price of AP balance sheet | (20.5) | A hill, and resistors in parallel (§20.3.2) | Theo sizes PB-13 for a doubling (§20.5.1) | Block 3, `clearing_premium` and `ap_redemptions` |
| The custom basket | (20.6) | Pegs on springs inside a rubber band (§20.4.3) | The 150-line PT and its exit (§20.4.3) | Block 4, closed form and SLSQP |
| What custom baskets are worth | (20.7) | Same box | The sponsor's 9:52 call, 8 Apr 2025 (§20.4.3) | Block 4, asserts |
| The settlement runway | (20.8) | The drunk and the lamppost (§20.6.1) | Theo, the stick and the lag that lengthens (§20.6.1) | Block 5, `sleeve_path` |

- **A credit ETF is two markets and a conversion right.** The secondary market nets; only the residual reaches the APs, and the band is the price of converting.
- **Premium = flow + staleness + bid-side constant** (20.1). Only the flow term is a trade. Staleness is a forecast of tomorrow's marks, and $\bar c$ is a decimal point in the valuation policy.
- **The band is $[\bar c - c^R - f^R - k^R,\ \bar c + c^C + f^C + k^C]$** (20.4). Bid-side NAVs slide it up by $\bar c$, which is why calm HY ETFs "trade at a premium." Custom baskets move the two edges independently.
- **In stress, price impact multiplies**: $\psi = \bar\gamma \sigma_b^2 T^{\text{h}}$ (20.5). Two times 36 times 4 turns a 1 bp flow into a 3% discount without anyone leaving the table.
- **Custom baskets are worth $\mathcal{D}/(2\theta)$** (20.7): the dispersion of net costs over the fund's tracking aversion. They are how PT dealers recycle risk, and losing them in H1 2022 showed up in PT pricing.
- **March 2020 was not a broken arbitrage.** IG's flow term collapsed because it was the most sellable risky asset. The Fed fixed it by lowering everyone's price of risk, mostly before it bought a share.
- **Loan ETFs live or die by (20.8):** sleeve over burn rate against the settlement lag. It is Theo's 13-week model in a 40 Act wrapper.
- **IDO or it didn't happen:** an ETF discount trade earns only the convergence, net of rate and spread beta.

**The Spec You Hand the Robot.** *Vague:* "Build me an ETF arb monitor." *What ROBO built:* see §20.7, all 206 alerts of it. *Precise:* Build `etf_arb.monitor(date, ticker) -> Signal`. **Inputs:** `etf_daily` and `holdings` per the schema in §20.7, published creation and redemption baskets, TRACE same-day dispersion `u`, and the change in shares outstanding as $F$. **Compute:** $\bar c$, $c^C$ and $c^R$ from half-LCS weights; the static band (20.4) with the fund's fee schedule; $\hat\eta$ from (20.3) on a trailing 250-day calm window, reported with its attenuation bound; $\hat s_t$ from (20.2) using ETF returns as the proxy for true returns; $\hat\psi$ from (20.5) as the regression slope of the premium on $F$ over a rolling window; the regime label from `classify`. **Guards:** fractions of NAV everywhere; refuse to run without `nav_convention`; skip days with no NAV strike; mark any day with a pricing-methodology change as `measurement_noise`; never emit a trade signal from the premium alone. **Outputs:** the regime label, the band edges, the three components of (20.1), $\hat\psi$, and for loan funds the runway from (20.8). **Tests:** the asserts in Blocks 1–6, plus one replay of 2020-03-09 to 2020-03-27 that must label LQD's March 19 discount `flow_dislocation_redeem` and HYG's same-day premium `inside_band` or `measurement_noise`.

### Exercises

1. **The premium-day census.** JNK closed at a premium on 206 trading days of 2025 and at a discount on 44. Assume pro rata baskets and that the premium is uniformly distributed on the band (20.4). What value of $(f^R + k^R)/(2\bar c + f^C + k^C)$ does the census imply? Now explain why "uniform" is wrong in a year of net inflows, and in which direction it biases your answer.
2. **Kaz's regression.** Kaz ran (20.3) on HYG and found $\hat\eta = 0.08$. He concluded that HY evaluated prices take more than two weeks to adjust. Using the attenuation formula of §20.2.2, give two other explanations, and design a second regression, using lagged ETF returns, that distinguishes among the three.
3. **The departing AP.** Twenty APs share risk tolerance equally, except one, which supplies 40% of the total. That AP leaves. By how much does $\psi$ rise? Compare your answer with the AP-count paragraph of §20.3.2, and write one sentence for a regulator explaining why counting APs is the wrong statistic.
4. **Cardinality.** Add a fixed cost $\chi$ per bond line included in the basket to the problem in §20.4.3. Show that the problem becomes a mixed-integer QP. Propose a greedy heuristic, and explain why the resulting baskets look like the 10–35% coverage ratios in the data.
5. **The Fed's clause.** Suppose the SMCCF had bought LQD at a premium $\pi > \pi^{\text{hi}}$. Show that APs would create shares and sell them to the Fed, and compute the transfer from the taxpayer to the APs per dollar purchased. Then explain, in one paragraph, why "materially exceed" was the most important phrase in the term sheet.
6. **The sleeve and the line.** A loan ETF has a 7% sleeve, a three-week settlement lag and a credit line of size $B$ that costs 50 bp a year undrawn. Using `sleeve_path`, find the smallest $B$ that survives a 9% outflow concentrated in two weeks. Then tell Theo what his 13-week model would have said about the same company.

### Deep-Dive Resource Graph

**Podcasts**
- **A Longstanding Fear About The Corporate Debt Market May Finally Be Coming True** (Bloomberg *Odd Lots*, Chris White of Viable Markets, 2020-03-23). Recorded in the March 2020 meltdown, it frames the reach for yield, heavy issuance and the plumbing of the corporate bond market as a setup for forced selling: the mood behind the discount tape of §20.5.1. https://omny.fm/shows/odd-lots/a-longstanding-fear-about-the-corporate-debt-marke
- **Why the True Price of a Bond Can Still Be Hard To Know** (Bloomberg *Odd Lots*, Maciej Kowara and Eric Jacobson of Morningstar, 2021-04-05). Bond pricing for infrequently traded paper is "a matter of opinion", so two firms can disagree about what the same bond is worth: the premise of §20.2, where the NAV is an opinion. https://omny.fm/shows/odd-lots/why-the-true-price-of-a-bond-can-still-be-hard-to
- **Jeff Rosenberg: The Past, Present, and Future of Systematic Fixed Income (S7E19)** (*Flirting with Models*, Corey Hoffstein, 2025-08-18). The head of BlackRock Systematic Fixed Income, the firm behind HYG and LQD, on quant fixed income from the sell side to the buy side; read it for the practitioner view of systematic credit, since it is not an episode about creation and redemption. https://www.flirtingwithmodels.com/episodes/8V74zBaN4jN
- **The ETF Story 3: The Approval** (*Trillions*, Eric Balchunas and Joel Weber, 2023-01-29; re-release of a 2018 series). The 1988-1993 back-and-forth between the SEC and the SPY team over "logistics, structure, and the creation-redemption process, which was inspired by commodities warehouses": the origin of the AP machine in §20.1. https://omny.fm/shows/trillions/the-etf-story-3-the-approval
- **Words of Wisdom From Mr. ETF** (*Trillions*, guest Reggie Browne of GTS, a market maker, 2022-03-31). A live Bloomberg event in which a market maker covers how ETFs are born, the nearest audio to the market-making side of the band in §20.3. https://omny.fm/shows/trillions/words-of-wisdom-from-mr-etf

**Practitioner Writing**
- BlackRock, *Lessons from COVID-19: ETFs as a Source of Stability*, ViewPoint, July 2020 (https://www.blackrock.com/corporate/literature/whitepaper/viewpoint-lessons-from-covid-19-etfs-as-a-source-of-stability-july-2020.pdf).
- MSCI (Bohák & Janosik, 2020-04-08), "Bond ETFs and underlying price uncertainty" (https://www.msci.com/research-and-insights/blog-post/bond-etfs-and-underlying-price-uncertainty).
- ICE Data Services (Heckert) via FOW, "Exchange-traded funds in volatile markets," 2020-06-22 (https://www.fow.com/insights/3694910-exchange-traded-funds-in-volatile-markets).
- Vanguard, "4 nuances to know about bond ETFs" (https://advisors.vanguard.com/insights/article/4-nuances-to-know-about-bond-etfs), on bid-side NAVs.
- etf.com, "Bond ETF Premiums Become Discounts" (https://www.etf.com/sections/news/bond-etf-premiums-become-discounts).
- The DESK, "Commentary: Inside the fixed income ETF primary market" (https://www.fi-desk.com/commentary-inside-the-fixed-income-etf-primary-market/).
- Man Institute, *Quantitative Credit Alpha: Early Mover* (2022) and *Revolutions in Credit Trading* (2023) (shelf copies; cited by page above).
- **New Insights from N-CEN: Liquidity Management at Open-End Funds and Primary Market Concentration of ETFs** (Federal Reserve Board FEDS Note, 2023-01-11). Finds "a high degree of concentration of APs, especially for fixed income ETFs", about four active APs per ETF (2018-2021 N-CEN data): how many dealers actually stand behind the band of §20.3.2. https://www.federalreserve.gov/econres/notes/feds-notes/new-insights-from-n-cen-liquidity-management-at-open-end-funds-and-pmc-of-etfs-20230111.html
- **Measuring the Forest through the Trees: The Corporate Bond Market Distress Index** (NY Fed *Liberty Street Economics*, 2021-02-22). Introduces the CMDI, one measure of joint dislocations in primary and secondary corporate bond markets: a stress gauge to overlay on the March 2020 discount tape of §20.5.1 and a candidate regime feature for the monitor of §20.7. https://libertystreeteconomics.newyorkfed.org/2021/02/measuring-the-forest-through-the-trees-the-corporate-bond-market-distress-index/

**Academic Papers**
- Shim & Todorov (2021), "ETFs, illiquid assets, and fire sales," BIS WP 975 (https://www.bis.org/publ/work975.htm).
- Todorov (2021), "The anatomy of bond ETF arbitrage," *BIS Quarterly Review*, March (https://www.bis.org/publ/qtrpdf/r_qt2103d.htm).
- Koont, Ma, Pástor & Zeng (2022/2025), "Steering a Ship in Illiquid Waters: Active Management of Passive Funds," NBER w30039 (https://www.nber.org/papers/w30039); *RFS* 38(10).
- Haddad, Moreira & Muir (2020/2021), "When Selling Becomes Viral," NBER w27168 (https://www.nber.org/papers/w27168); *RFS* 34(11).
- Gilchrist, Wei, Yue & Zakrajšek (2020/2024), "The Fed Takes on Corporate Credit Risk," NBER w27809 (https://www.nber.org/papers/w27809); *JME*.
- Aramonte & Avalos (2020), BIS Bulletin No. 6, on corporate bond ETF discounts in March 2020 (https://www.bis.org/publ/bisbull06.htm).
- Pan & Zeng (2017), "ETF Arbitrage under Liquidity Mismatch," ESRB Working Paper No. 59 (title only).
- SEC staff, *U.S. Credit Markets: Interconnectedness and the Effects of the COVID-19 Economic Shock* (October 2020) (https://www.sec.gov/files/US-Credit-Markets_COVID-19_Report.pdf).
- **ETF (Mis)pricing** (FCA Occasional Paper 68, first published 2025-05-30; updated 2026-06-03). A dynamic equilibrium model linking APs' inventory management and investor demand to mispricing, validated on regulatory data from 128 ETFs, 2018-2022: the theory behind the band with a balance sheet in §20.3.2. https://www.fca.org.uk/publications/occasional-papers-fca-research/occasional-paper-68-etf-mispricing (recorded as a Microstructure Exchange talk by Andrei Kirilenko: https://youtu.be/-OVIAs967AI).

**Data & Code**
- Rule 6c-11: SEC press release 2019-190 (https://www.sec.gov/news/press-release/2019-190); adopting release 33-10695 (https://www.sec.gov/rules/final/2019/33-10695.pdf); rule text, 17 CFR 270.6c-11 (https://www.law.cornell.edu/cfr/text/17/270.6c-11).
- Rule 22e-4: SEC press release 2016-215 (https://www.sec.gov/news/pressrelease/2016-215.html).
- SMCCF: Federal Reserve facility page with term sheets and transaction-specific disclosures (https://www.federalreserve.gov/monetarypolicy/smccf.htm); term sheet effective 2020-07-28 (https://www.federalreserve.gov/newsevents/pressreleases/files/monetary20200728a1.pdf); NY Fed operations page (https://www.newyorkfed.org/markets/secondary-market-corporate-credit-facility) and FAQ (https://www.newyorkfed.org/markets/primary-and-secondary-market-faq/corporate-credit-facility-faq).
- Issuer pages with daily NAV, premium/discount and baskets: HYG (https://www.ishares.com/us/products/239565/ishares-iboxx-high-yield-corporate-bond-etf), LQD (https://www.ishares.com/us/products/239566/ishares-iboxx-investment-grade-corporate-bond-etf), JNK (https://www.ssga.com/us/en/intermediary/etfs/spdr-bloomberg-high-yield-bond-etf-jnk), BKLN case study (https://www.invesco.com/us/en/insights/case-study-bkln-enabling-access-senior-loans.html).
- SEC EDGAR (https://www.sec.gov/edgar) for Form N-CEN AP data and prospectus NAV-convention language; FINRA TRACE (https://www.finra.org/filing-reporting/trace) for same-day dispersion $u_t$; ICI *Investment Company Fact Book* (2025 edition) for primary versus secondary ETF activity (title only).

<!-- STATUS: COMPLETE -->
