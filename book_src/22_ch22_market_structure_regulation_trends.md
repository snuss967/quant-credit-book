# Chapter 22: Market-Structure Regulation & the Forces Reshaping Liquidity

*Monday 28 September 2026, 3:41 p.m., two business days before quarter-end. Theo's fifth day on the desk. Calloway Industrial is a fictional issuer; the desk, its quoter and its numbers are illustrative.* The RFQ was ordinary in every way a model can see. *Client sells \$15mm Calloway Industrial 5.10% Senior Notes due 2033 (a fictional issuer; Baa2/BBB), four dealers in competition, two minutes to respond.* Same CDS level as last Monday. Same equity. Same news, which was none. And yet the auto-quoter bid three-eighths of a point lower than it had a week earlier, for the same bond in the same size.

Theo did what six years of restructuring work had trained him to do with a number he did not believe: he went and got the other number. The RFQ log for the previous Monday had the same client, the same bond, the same \$15mm, at almost the same minute. He put the two rows side by side. Five-year CDS on Calloway: 112 both days *(illustrative)*. The stock: down eleven cents over the week. Thirty-day spread volatility, desk inventory in the name, the fitted probability of winning at each price: every column the quoter reads was flat to the second decimal. The only column that had moved was the one at the end, the bid. Last Monday it had been 99.10. Today it was 98.725.

"Something's broken," Theo said. "Nothing moved."

"Nothing moved in the features," said Kaz, scrolling. "Spread vol, inventory, the win curve. All flat. I assumed regulation was a constant." They pulled up the quoter's config history, looking for the usual suspects: a stale parameter file, a percent typed where a decimal belongs, a deploy someone pushed on Friday afternoon and forgot to mention. "If it's a bug, it's a tidy one. The last config change was nine days ago."

At 3:43 the RFQ closed. The desk lost. The client sold to someone else at 98.75, a quarter of a cent above the desk's bid, and the venue showed the cover, the second-best price, at 98.70 *(illustrative)*. Theo went back to the previous Monday's ticket. The winner then had paid 99.125. Every dealer in the competition had moved by roughly the same three-eighths, at the same hour, on the same bond, for no reason anybody's features could see.

"Four quoters with the same bug," Theo said. "On the same afternoon."

"What's Wednesday?" Ines asked.

"The thirtieth." He heard it as he said it. "Quarter-end. Half my old clients drew their revolvers the week before it, so the 10-Q would show cash."

"The pot didn't change," said Ines, without looking up. "The table did. Wednesday is quarter-end, and every balance sheet on the Street is getting dressed for a photograph, ours included. Treasury sent the hurdle rate for the snapshot this morning. If we buy this, we're paying rent on it through the photo. And whoever we sell it to has to see our print inside fifteen minutes. Which, you'll be relieved to hear, is still fifteen."

Theo opened a new window out of habit. "But what does the credit agreement say?"

"There isn't one," Ines said. "There's the Federal Register."

"So it's a credit agreement with worse fonts and better enforcement."

"Then read the term sheet," Ines said. "It's in your inbox. Subject line in capitals, from Treasury, sent at 7:02."

It was. The memo ran to a page and a half and read like every internal memo that has ever cost anyone money: polite, numbered, no adjectives. Paragraph 3 said that for positions held over the quarter-end reporting date, the hurdle rate on consumed Tier 1 capital would be 24% annualized instead of the usual 12% *(illustrative)*. Paragraph 4 said desks were "encouraged to manage balance sheet accordingly." Theo had seen the same sentence, in a different font, in a sponsor's letter to a lender group. It had meant the same thing.

"Do the rent," Ines said. "On the margin of the memo. In your handwriting."

Theo wrote it out the way he would have written a fee calculation at PJT. A BBB industrial is bound by risk-based capital, not by the leverage ratio, so the capital it eats is the 10.5% requirement on a 100% risk weight. The desk wants 12% a year on that capital: $0.12 \times 0.105 = 0.0126$, or 126bp a year per dollar of bond. A week of it is seven days out of 365: $126 \times 7/365 \approx 2.4$bp. "And Treasury doubled the hurdle for the photo," he said, "so 4.8. Call it a nickel a hundred." He looked at the two bids again. "The quote moved thirty-seven and a half cents. The rent is a nickel."

"So it's a bug," Kaz said, hopefully.

"It's an invoice," Ines said. "Four dealers got charged this afternoon, and each of them got the same memo from its own Treasury. The rent is the line that came with a memo. The rest of the invoice came without one, and that's the part you'll spend this chapter learning to read."

"Back in my day," said Mags, from behind a stack of 10-Qs, "the regulator was a phone call from the Fed and a fax nobody read." She considered this. "The new way is better, honestly. The fax never told you the effective date." She turned a page. "In March 2020 I sat on a bank desk and watched the invoice become the whole market, and the Fed paid it."

Kaz had stopped scrolling. "So the rule is a feature."

"The rule is a price," Ines said. "And the day it changed is a date in every series you've ever trained on."

Theo looked at his margin note, at the nickel and the thirty-seven and a half cents, and understood that the gap between them was the lesson. Nothing in the bond had moved, and his price had moved. Someone had charged him, and most of the invoice was not on the page in front of him.

*Before reading on, write down the three things a dealer sells, and which one this quote just charged you for. §22.1 grades the card.*

That is the question this chapter answers: *how do you put a price on a rule, and how do you know when a rule changed the data?* The answer comes as two machines, one that reads the invoice (rent, delay, settlement, netting, capacity and clearing, §22.1–§22.6) and one that dates it (the regime table and the event study, §22.2 and §22.8); the Finder table at the top of the Desk Debrief (§22.9) lists every tool with the scene that teaches it.

## 22.1 A Rule Is a Price: Taxes on Balance Sheet, Time, and Information

A restructuring banker learns to read a credit agreement for the trapdoors: the basket that permits the drop-down, the definition that lets the sponsor add back synergies nobody will ever see. The skill transfers intact. An SEC adopting release has effective dates, phase-ins, carve-outs ("natural persons," "sovereign entities," "inter-affiliate"), and a compliance date that slips. Theo read his first one, that week, the way he used to read a covenant package, and found what he would have found there: the places where the liquidity would and would not be.

Ines graded the card the next morning, with Monday's two Calloway tickets still on Theo's screen. "Three things," she said. "A dealer sells exactly three things, and every rule you'll ever read is a tax or a subsidy on one of them."

The first is balance sheet. When the desk buys a client's \$15mm, it is lending the client its capital for as long as the bonds sit on its books, and the leverage ratio, risk-based capital, and the clearing and netting rules set the rent on that loan. That was the nickel in Theo's margin note, and Treasury's memo was the receipt for it.

The second is time, and time was most of the invoice. The settlement cycle sets how long counterparty exposure lasts; Volcker's inventory limits set how long the dealer may wait for the other side; reporting delays set how long the dealer's private information stays private. On Monday the time that mattered was the plainest kind: whoever takes the bond from the client has to hold it until somebody else wants it. The quoter does not read that as a feature. It reads it from a calendar table, expected days to the next buyer by rating and by week of the quarter, and the quarter-end row says three weeks instead of one, because the dealers and clients who would normally take a BBB block off the desk are dressing for the same photograph *(illustrative)*. "You wrote that table in June," Ines told Kaz. "Then you stopped thinking of it as regulation." Triple the hold and the inventory-risk charge on the bid, about an eighth of a point for a week, triples with it, to about three-eighths; the rent on three weeks at the photo's doubled hurdle is $0.24 \times 0.105 \times 21/365 \approx 14.5$bp against last week's 2.4 *(all illustrative)*. A quarter of a point of time and an eighth of balance sheet: that was the three-eighths.

The third is information. TRACE and the security-based swap reporting regime (SBSR) decide who learns what, and when. On Monday the information charge did not change, which is why nobody saw it: the desk's print would show at minute fifteen as "5MM+ sell," exactly as it would have the week before. It is in both bids, and §22.2 prices it.

Most people who do the card write "balance sheet," because the memo was about balance sheet. The memo was the part of the invoice that came in writing. Two-thirds of the three-eighths was time. The table below lists the rules a credit desk lives with, by which of the three things each one taxes.

| Rule (key date) | Input taxed (−) or subsidized (+) | Where it enters the quote | See |
| :--- | :--- | :--- | :--- |
| Supplementary leverage ratio and its enhanced version (eSLR); recalibrated effective 2026-04-01 | Balance sheet (−), the same rate on every dollar | Rent term $c_{\text{reg}}$; binds on low-risk assets | §22.5 |
| Basel III risk-based capital; endgame proposals 2023 and 2026 | Balance sheet (−), risk-weighted | Rent term on risky inventory | §22.5 |
| Volcker Rule (revised 2019, effective 2020-01-01) | Time (−): inventory must track expected customer demand | Caps the holding period $\tau^{\text{hold}}$ | §22.5 |
| T+1 settlement (2024-05-28) | Time (+ for margin, − for operations) | Margin scales like $\sqrt{H}$; fail probability | §22.3 |
| Treasury clearing mandate (cash 2026-12-31, repo 2027-06-30) | Balance sheet (+ via netting), liquidity (− via margin) | Netting factor $\phi(N)$ against IM funding | §22.4 |
| TRACE: 15-minute reporting; \$5mm IG and \$1mm HY dissemination caps | Information (+ for blocks) | Block spread falls with the delay and the cap | §22.2 |
| CDS index clearing (2013), SBSR public dissemination (2022-02-14) | Information and balance sheet | Cost of the CDS hedge | §22.6 |

Compliance with this table is the legal department's job. What the desk does with it is price it, and pricing it has two halves. Every rule shows up as a term in the quote, so the market maker of Chapter 18 acquires a fifth component next to fear, greed, suspicion, and the value of tomorrow's flow: **rent**. And every rule has an effective date, which makes every effective date a candidate structural break in every series the desk trains on. Kaz's calendar table had carried a regulatory date for three months without anyone calling it one. The chapter is therefore two machines: a pricing machine (§22.1–§22.6) and a dating machine (§22.2 and §22.8). Figure 22.1 puts the dating machine's raw material on one axis.

![Figure 22.1: Rule changes on balance sheet, time, and information bunch up in 2022–2027, so a series that spans those years crosses several breaks that have nothing to do with credit, and the shaded bars mark the market-wide stresses that hit every bond at once (filled markers are in force, hollow markers are proposed or scheduled, the cross is a rule approved and never in force, and the grey panel is the future as of October 2026). Source: dates as stated in §22.2–§22.6 (FINRA Regulatory Notices 25-17 and 26-16; SEC, CFTC and Federal Reserve releases); dates marked approx. in the text are approximate here.](assets/figures/ch22_rule_timeline.png)

> **[SOURCE EXTRACTION]** *Bohn_Stein_Active_Credit_Portfolio_Management p.25:* "we view bank regulation similarly to financial accounting—something that has to be done, both for the sake of the bank and the broader financial system, but not something that should be the main driver of an institution's business decisions." Also: "financial institutions scramble to respond to (and sometimes try to arbitrage) the rules."
>
> **Annotation.** Our analysis: Bohn and Stein were writing about the gap between regulatory and economic capital in a bank's credit portfolio, and their advice for a portfolio manager still holds: do not let the regulatory number stand in for the risk number. For a dealer in 2026 the advice runs the other way. When the leverage ratio binds, the regulatory number *is* the economic cost of the marginal trade, because Tier 1 is the scarce input and the hurdle rate on it is real money. The second sentence is the more useful one for a former restructuring banker. "Scramble to respond to (and sometimes try to arbitrage)" describes the liability-management game of Chapter 13 played against a regulator instead of a lender group: find the basket, read the definition, time the phase-in. The quarter-end photograph in the cold open is the market's version of an EBITDA add-back.

### 22.1.1 Derivation: the regulatory cost of carry in the reservation price

Everything in this subsection is under the physical measure $\mathbb{P}$: inventory risk is a real-world variance, and capital ratios are accounting identities, not probabilities.

> **Math, Gently.** *The rent.* Picture a parking garage with a peculiar rate card. It charges by the hour, and the hourly rate is the larger of two numbers: a footprint rate, the same for a hatchback and a limousine, and a value rate that depends on what the car is worth. A cheap car pays the footprint rate, because its value rate is tiny; an expensive car pays the value rate. A bank's balance sheet is that garage, and its Tier 1 capital is the floor space. The footprint rate is the leverage ratio: every dollar of assets, Treasury or junk bond, needs the same slice of capital. The value rate is risk-based capital: a requirement times a risk weight that is close to zero for a Treasury and about 100% for a BBB industrial. The bank pays whichever slice is larger, and it wants a return, the hurdle, on the capital it ties up. Tiny number: a 2-year Treasury with a 5% leverage requirement and a 12% hurdle costs $0.12 \times 0.05 = 0.006$ a year, or 60bp, and a week of that is $60 \times 7/365 \approx 1.15$bp. The dealer earns about half a basis point for crossing the Treasury's bid-ask. A week of parking costs more than twice the fare. In symbols, the rent per year is the hurdle times the larger slice, and the next two paragraphs write it down properly as (22.1).

**Capital per unit of inventory.** A dealer holds signed inventory $q$ (lots) of a bond with mid $S_t$ (points per lot). The Tier 1 capital the position consumes is

$$
K(q) = |q|\,\bar S\,\kappa, \qquad \kappa = \max\!\big(\kappa_{\text{RWA}}\cdot \text{RW},\ \kappa_{\text{LR}}\big),
$$

where $\bar S$ is the price level, frozen at today's mid over a short horizon; $\kappa_{\text{RWA}}$ is the risk-based requirement including buffers (for example, 10.5% for total capital including the conservation buffer); $\text{RW}$ is the risk weight, or the market-risk charge per unit of notional written as an equivalent risk weight; and $\kappa_{\text{LR}}$ is the leverage requirement. Before 2026-04-01, $\kappa_{\text{LR}}$ was 5% for a US G-SIB holding company (the 3% SLR plus a fixed 2% buffer). Since then it has been 3% plus half the bank's Method 1 G-SIB surcharge. The absolute value matters: a short position also consumes balance sheet, through the reverse repo or securities borrow that delivers the bond.

**The rent rate.** Let $h$ be the hurdle: the annual return the bank demands on Tier 1 *in excess of* its funding rate. Funding is already in the carry of the bond, so $h$ must be the excess return or the funding cost gets counted twice. The regulatory cost of carry per dollar-year of gross inventory is

$$
c_{\text{reg}} = h\,\kappa = h\cdot\max\!\big(\kappa_{\text{RWA}}\,\text{RW},\ \kappa_{\text{LR}}\big).
\tag{22.1}
$$

That is the number Theo wrote in the margin of the memo, done properly. The harder question is what the rent does to a quote, and for that the dealer needs a way to say what one more bond is worth to it, which is where the utility of Chapter 18 comes back in.

> **Math, Gently.** *The indifference price, in two parts.* **Part 1: what you would pay not to flip a coin.** A friend offers a bet: heads you win \$50, tails you lose \$50. On average it is worth nothing, and most people would still pay a little to be excused. How much depends on how much the swing bothers you, and the dealer of Chapter 18 has a precise answer: with exponential utility and a small risk aversion $\gamma$, the cost of carrying a gamble is about $\tfrac12\gamma$ times its variance. Here the variance is $50^2 = 2{,}500$, so with $\gamma = 0.01$ per dollar the coin costs $\tfrac12 \times 0.01 \times 2{,}500 = \$12.50$. A dealer's *indifference price* is the same idea applied to one more bond: the bid at which buying it leaves the dealer exactly as content as not buying it. It sits below the mid by the variance charge the extra bond brings and, now, by the extra rent. **Part 2: the kink.** Rent is charged on the size of the position, $|q|$, whichever way it faces, because a short consumes balance sheet through the borrow. Say a week's rent on one lot is 2.4bp. A flat dealer that buys opens a position and pays 2.4bp; one that sells opens a short and pays 2.4bp too. Both quotes move away from the mid by the rent, and the spread widens. A dealer already long ten lots is in a different spot: buying an eleventh adds 2.4bp of rent, but selling one *saves* 2.4bp. Both quotes move down by the rent, the spread stays where it was, and the whole market skews. That is a dealer subletting a room it already rents: it will happily take less for the sublet. The two cases are the two sides of one absolute value; the statement is next, and the algebra closes the subsection.

**What the rent does to the quote.** Put both parts into the Avellaneda–Stoikov dealer of §18.4 and the rent turns up in three places. A dealer already holding inventory moves its reservation price by the rent, in the direction that shrinks the position:

$$
r^{\text{res}}(q) = \tfrac12\big(r^a + r^b\big) = s - q\,\gamma\sigma^2(T-t) - \operatorname{sgn}(q)\,c_{\text{reg}}\bar S\,(T-t),
\tag{22.2}
$$

with $\operatorname{sgn}(0) = 0$. A flat dealer instead widens both quotes by the rent, so its quoted spread acquires a third term next to fear and greed. Write $\tau^{\text{hold}}$ for the expected holding period, which replaces the horizon $T - t$ as in the worked example of §18.4 (the superscript keeps it apart from the default time $\tau$). A flat dealer's quoted spread is then

$$
\delta^a + \delta^b = \underbrace{\gamma\sigma^2\tau^{\text{hold}}}_{\text{fear}} + \underbrace{\tfrac{2}{\gamma}\ln\!\big(1+\tfrac{\gamma}{k}\big)}_{\text{greed}} + \underbrace{2\,c_{\text{reg}}\bar S\,\tau^{\text{hold}}}_{\text{rent}}.
\tag{22.3}
$$

The kink is why a desk running near its balance-sheet limit quotes a sharp offer and a sullen bid. And principal market making pays only if the half bid-ask covers the rent over the hold. In bp of notional, with $c_{\text{reg}}$ in bp per year and $\tau^{\text{hold}}$ in years, the breakeven is

$$
\tau^\ast = \frac{s_{\text{ba}}/2}{c_{\text{reg}}},
\tag{22.4}
$$

where $s_{\text{ba}}$ is the bid-ask in bp of price. Hold the bond for less than $\tau^\ast$ and principal market making beats agency; hold it longer and you are an unpaid warehouse. The algebra behind (22.2) and (22.3) is the Full Derivation at the end of this subsection.

**Numerics** *(illustrative; hurdle $h = 12\%$, 7-calendar-day hold, ACT/365)*:

| Position | Binding constraint | $\kappa$ | $c_{\text{reg}}$ (bp/yr) | 1-week rent (bp) | Half bid-ask (bp of price) | $\tau^\ast$ |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 2y on-the-run Treasury, eSLR before 2026 | Leverage, $\kappa_{\text{LR}} = 5\%$ | 5.0% | 60 | 1.15 | ~0.5 | ~3 days |
| Same, after 2026-04-01 (3% + ½ × 1.5% surcharge) | Leverage | 3.75% | 45 | 0.86 | ~0.5 | ~4 days |
| 10y BBB industrial, equivalent RW 100% | Risk-based, $10.5\% \times 1.0$ | 10.5% | 126 | 2.42 | ~12.5 | ~36 days |

The table explains a decade of market structure. For the corporate bond, rent is a rounding error against a quarter-point market: the dealer can sit on it for a month. For the Treasury, rent *is* the market: three days of inventory eats the half-spread. That single inequality explains why dealers went agency in Treasuries first, why the Federal Reserve's first market-structure tool in March 2020 was a leverage-ratio exclusion (§22.4), and why the November 2025 eSLR rule was sold as relief for "Treasury market intermediation" (§22.5). The risk weight does not tell you what a Treasury costs to hold. The leverage ratio does. Figure 22.2 draws the kink in (22.1) and the breakeven in (22.4).

![Figure 22.2: Rent (left) sits at the leverage floor for every asset below the switching point (47.6% risk weight before 2026-04-01, 35.7% after) and rises with risk weight only above it, so a week of Treasury rent already exceeds the half bid-ask while a BBB bond can sit for about a month (right). Illustrative: hurdle 12%, risk-based requirement 10.5%, leverage requirement 5% then 3.75%, half bid-ask 0.5bp for the Treasury and 12.5bp for the BBB, from (22.1) and (22.4).](assets/figures/ch22_regulatory_rent.png)

> **Ways This Blows Up.** (1) *Units.* $c_{\text{reg}}$ is annual and $\tau^{\text{hold}}$ is in years; ROBO once fed a holding period of seven days into the year slot and concluded that a week in Treasuries costs 4.2% of notional, which would make every repo desk on the Street a charity. (2) *Using $q$ instead of $|q|$.* A short pays rent too, through the borrow. A signed formula says shorting a bond *releases* capital, and the optimizer gets very excited about shorts. (3) *Double counting funding.* $h$ is the excess return over funding. (4) *Gross versus net.* Leverage charges apply to gross positions and risk charges to net-of-hedge positions, so a hedged book is cheap under risk-based capital and expensive under the leverage ratio. Run both and take the max *per legal entity*, not per trade. (5) *Calendar.* $\kappa$ and $h$ are effectively higher around reporting snapshots for some dealers. Model them as calendar features, not constants, or the quarter-end in the cold open becomes an unexplained residual.

#### The Full Derivation: rent in the reservation price

**Frozen-inventory value with rent.** Take the Avellaneda–Stoikov setup of §18.4: the mid follows $dS_t = \sigma\,dW_t$, the dealer has cash $x$ and exponential utility with risk aversion $\gamma$, and the horizon is $T$. If the dealer holds $q$ to $T$ without trading, its terminal wealth is $x + qS_T$ minus the rent paid along the way, $c_{\text{reg}}\bar S|q|(T-t)$. Taking the expectation of $-\exp(-\gamma\,\cdot)$ over the Gaussian $S_T$ gives

$$
v(x,s,q,t) = -\exp\!\Big(-\gamma\big[x + qs - c_{\text{reg}}\bar S\,|q|\,(T-t)\big]\Big)\exp\!\Big(\tfrac12\gamma^2 q^2\sigma^2 (T-t)\Big).
$$

**Indifference prices.** The reservation bid $r^b$ is the price at which the dealer is indifferent to buying one more lot, $v(x - r^b, s, q+1, t) = v(x, s, q, t)$. The reservation ask $r^a$ solves $v(x + r^a, s, q-1, t) = v(x, s, q, t)$. Take logs, cancel the common terms, and use $(q\pm1)^2 - q^2 = \pm 2q + 1$:

$$
r^b(q) = s - \tfrac12(2q+1)\,\gamma\sigma^2(T-t) - c_{\text{reg}}\bar S\,(T-t)\,\big(|q+1| - |q|\big),
$$

$$
r^a(q) = s - \tfrac12(2q-1)\,\gamma\sigma^2(T-t) + c_{\text{reg}}\bar S\,(T-t)\,\big(|q-1| - |q|\big).
$$

The absolute value puts a kink at $q = 0$, so the two cases behave differently.

*Flat dealer ($q = 0$).* Then $|q+1| - |q| = 1$ and $|q-1| - |q| = 1$, so the bid falls and the ask rises by the full rent:

$$
r^a(0) - r^b(0) = \gamma\sigma^2(T-t) + 2\,c_{\text{reg}}\bar S\,(T-t).
$$

*Long dealer ($q \ge 1$).* Then $|q+1| - |q| = 1$ but $|q-1| - |q| = -1$: buying adds rent and selling saves it. Both indifference prices shift down by the same amount, so the spread is unchanged and the midpoint $\tfrac12(r^a + r^b)$ moves by $-c_{\text{reg}}\bar S\,(T-t)$ on top of the usual inventory skew $-q\gamma\sigma^2(T-t)$. That is (22.2); the short case is the mirror image, which is where $\operatorname{sgn}(q)$ comes from.

The Avellaneda–Stoikov first-order condition from §18.4 still places each quote at the indifference price plus the markup $\tfrac{1}{\gamma}\ln(1 + \tfrac{\gamma}{k})$, because the rent enters only through $r^a$ and $r^b$. Add the markup to both of the flat dealer's indifference prices and replace $T - t$ with $\tau^{\text{hold}}$, and the quoted spread is (22.3).

#### Where the warehouse went

The rent explains why a dealer's quote moves on a calendar. It also explains, over fifteen years, where the warehouse went, which is the part a buy-side reader feels as "liquidity."

> **Desk Myth vs. Desk Reality.** *Myth:* "Post-crisis regulation killed bond-market liquidity." *Reality:* It re-priced balance sheet and moved the warehouse. By most published measures, average costs for small and mid-sized IG tickets fell over the decade as electronic venues and dealer competition (§22.2) did their work, while the cost of moving a large block in a stressed week rose *(qualitative; see the dealer-capacity evidence in §22.4)*. "Liquidity" was never one number. Regulation raised the price of the dealer's balance sheet and left the price of matching buyers to sellers alone, so every protocol that matches without warehousing grew. A desk that measures liquidity by the median ticket thinks regulation helped. A desk that measures it by the 99th-percentile block in March 2020 thinks regulation broke the market. Both are right about their own sample.

> **View From Another Seat.** *Two dealers, two rents.* Bank of America runs its flow-credit franchise on a deposit-funded balance sheet of about \$3.5 trillion (Q1 2026). On the 14 October 2026 earnings call, as transcribed by The Motley Fool, CFO Alastair Borthwick said "we happen to have a bigger fixed income shop than we do equities," and explained a weak FICC quarter in one line: "It just happens when rates go up 85 basis points in a quarter, that tends not to be good for those businesses. Clients tend to slow their activity." Jefferies sits in a different seat. It is not a bank holding company, so the leverage floor of (22.1) does not set its rent; its balance sheet costs whatever the group's own debt and equity cost, and its Level 3 assets were 3.1% of inventory. At its 16 October 2025 investor day (SEC Exhibit 99.1), Global Head of Fixed Income Fred Orlan described a strategy of "quality share over simple market share" and one high-yield book across electronic, portfolio and voice trading, where "seamless integration between our low touch electronic trading and our high touch voice desks is essential." *The book's reading, not either firm's:* for the deposit-funded bank, a BBB like Calloway is risk-bound and cheap to carry, and the expensive part of the trade at quarter-end is the leverage-bound Treasury hedge and its repo, so it can warehouse the block if it can turn it within days. A dealer paying for its own balance sheet in the bond market has an explicit hurdle on every dollar every day, quarter-end or not, so it bids what it can place, and the rest becomes an agency order or a line in a portfolio trade. Same bond, same afternoon, two different invoices.

Figure 22.3 plots the NY Fed series week by week; the Trend Watch below it gives the longer history and the trade-press reading of 2026.

![Figure 22.3: US primary dealers' net corporate-bond inventory averaged \$16bn long in 2017 and has since drifted down through zero: the 2026 average to date is -\$2.3bn for all corporate bonds and -\$4.9bn for investment-grade bonds alone, and the investment-grade book turned short first (annual average of -\$0.9bn in 2025). Averages are of the weekly observations. Source: NY Fed Primary Dealer Statistics (FR 2004), series PDPOSCSBND-* (long minus short, investment-grade and below-investment-grade bonds, notes and debentures, all maturities; weekly, 2015-01-07 to 2026-10-07).](assets/figures/ch22_dealer_inventory.png)

> **Trend Watch: dealer corporate-bond inventories, 2007–2026.** *What changed:* US primary dealers stopped warehousing corporate bonds. *How big:* Federal Reserve FR 2004 data put dealer corporate holdings at a peak of roughly \$235bn in 2007, cut by about three-quarters by 2012 *(approx.; the pre-2013 series lumps corporates with other credit, so treat the peak as an upper bound)*. Average long inventories were about \$16bn in 2017. Trade press citing Crisil Coalition Greenwich analysis of FR 2004 data reports that primary dealers have averaged a **net short** position of about \$4bn in US corporate bonds so far in 2026, "the first time in at least 25 years" *(approx.; check against the NY Fed primary dealer statistics before relying on it)*. In late 2024 Coalition Greenwich was already describing dealers as net short in longer-dated IG corporates *(late-2024 figure not independently verified)*. *What it means for the desk:* the inventory function has moved to the customer: all-to-all venues, ETF creation and redemption (Chapter 20), and portfolio trades (Chapter 19). The bank dealer is now a router with a risk budget, and its $\tau^{\text{hold}}$ is measured in hours. Your liquidity model's "dealer capacity" variable should say which kind of dealer it means.

The idea that a dealer's holding cost is funding plus capital times a hurdle is older than the leverage ratio. Here it is in a 2004 textbook, priced on a total return swap.

> **[SOURCE EXTRACTION]** *Schmid_Credit_Risk_Pricing_Models p.163:* "the cost of the trade will depend mainly on the funding cost of the total return payer and any regulatory capital charge incurred ... If the total return payer is a bank, it also depends on the BIS risk weight of the asset, with 20% for OECD bank debt and 100% for corporate debt."
>
> **Annotation.** Our analysis: this is (22.1) in its 2004 form. Schmid prices a total return swap as funding plus a capital charge driven by the Basel I risk weight, and the logic carries over to a dealer's inventory one for one. What changed is the *max*. In Schmid's world the risk weight was the only constraint, so a Treasury, with a zero weight, was free to hold, and corporate debt at 100% was the expensive asset. Since the leverage ratio arrived, every asset carries the floor $\kappa_{\text{LR}}$, and for low-risk assets the floor binds. The modern desk keeps Schmid's decomposition, funding plus capital times hurdle, and replaces the risk weight with $\max(\kappa_{\text{RWA}}\text{RW}, \kappa_{\text{LR}})$. One more departure: a TRS desk in 2026 also asks whether the trade is cleared, because clearing changes the counterparty term and the margin term (§22.4, §22.6).

The first buy-side price tag on all of this came eight years later.

> **[SOURCE EXTRACTION]** *Dynkin_Systematic_Investing_in_Credit p.348 (n.1):* "Konstantinovsky and Phelps (2012) document the decline in US corporate bond market liquidity as dealer inventories have fallen since 2008 in response to various regulatory changes. They estimate that the inventory decline led to an 18% drop in illiquidity, which translates to approximately 13bp/year in additional transaction cost for a portfolio with 100% yearly turnover."
>
> **Annotation.** Our analysis: thirteen basis points a year is the first serious price tag anyone put on post-crisis regulation from the buy side, and it is a useful prior even now. Read the units carefully: 13bp a year *at 100% turnover*. A systematic credit strategy with 200% turnover pays twice that, and a quarterly-rebalanced factor portfolio of the kind in Chapter 9 pays perhaps half. The modern desk departs from the 2012 estimate in two ways. First, the cost did not stay with the dealer; it moved into new protocols (portfolio trades, all-to-all) whose costs are lower on average and lumpier in stress. Second, the "18% drop in illiquidity" averages over calm and stressed regimes, and §22.4 shows that the regulatory cost is convex in dealer utilization: small in calm markets, very large when balance sheets fill.

### Specification for AI Implementation

**The Spec You Hand the Robot.** *Vague version:* "minimize regulatory capital." *What ROBO built:* a desk with zero inventory, zero capital consumption, and zero revenue, which ROBO reported as a 100% improvement. *Precise version:* compute the balance-sheet rent of each position as (22.1) times the holding period, in bp of $|$notional$|$ and in dollars, with decimals for every ratio (5% is `0.05`), calendar days on ACT/365, and $\kappa$ taken as the max of the risk-based and leverage charges. Compute the breakeven holding period (22.4) from a bid-ask in bp of price. Reject negative ratios, ratios above one, non-positive holding periods, and a zero binding capital rate in the breakeven. Every block in this chapter runs in order in one interpreter; this first block defines the imports.

A napkin handles the three rows of the numerics table in §22.1.1. It stops working at 2:58 p.m. on a Friday, when a trader holds a \$15mm ticket of a BBB industrial and asks whether it is worth warehousing over the weekend, and the same question is arriving, in slightly different clothes, for four hundred other positions with four hundred risk weights and four hundred guesses about how long each will sit. The rent in (22.1) is a one-line formula. The hazards are all in the plumbing around it: a percent typed where a decimal belongs, a short that appears to release capital, a seven-day hold fed into a slot that wants years. A desk automates this block not because the formula is hard but because it is easy to get wrong in a way that still looks plausible.

The listing is four small functions and a block of self-checks. `capital_rate` is the $\kappa$ of (22.1): it takes the risk-based ratio, the risk weight and the leverage ratio and returns the larger of `kappa_rwa * RW` and `kappa_lr`, element by element, so it accepts a scalar or a whole column of risk weights. Before computing anything it rejects ratios outside zero to one and negative risk weights, which is the entire defense against someone typing `5` for 5%. `regulatory_carry_bp` multiplies that rate by the hurdle, by `holding_days / 365` (calendar days, ACT/365) and by 10,000, and returns the rent for the hold in bp of notional. `breakeven_holding_days` is (22.4): it converts hurdle times binding rate into bp per year, halves the quoted bid-ask, and returns the number of days at which the rent eats the half-spread. It raises an error when the binding rate is zero, because a breakeven of infinity is a fact about your inputs, not about the market. `carry_table` is the desk-facing wrapper: hand it a table of `bond_id`, signed `notional`, `rw` and `holding_days`, and it returns a copy with `carry_bp` and `carry_usd`, the dollar figure computed on absolute notional because a short pays rent through its borrow.

The assertions at the bottom reproduce the numerics table to three decimals: 1.15bp for a week of Treasuries, 2.42bp for the BBB, 0.86bp after the 2026 leverage change, and breakevens of roughly three, four and 36 days. They also check that a long and a short of the same size cost the same dollars, and that percent-style inputs raise.

Use it to attribute balance-sheet cost to positions and to put a price on inventory in a quote or a limit. Do not read the table total as the bank's capital bill. The function takes the max trade by trade, but a regulator takes the max of two aggregates, so the output is an allocation, not the entity's number. The edge case that bites is in the signature of `breakeven_holding_days`: `kappa_rwa` and `risk_weight` default to zero, so a call that supplies only the leverage ratio quietly prices a Treasury. Forget them for the 25bp-wide BBB quote and you get about 76 days instead of 36, a flattering answer to a question you did not ask. The argument order also differs from `regulatory_carry_bp`, which does not help.

*The full listing is [Listing 22.1 in Appendix F](#code-22-1).*

*Further reading for this section:* Duffie (2012), *Market Making Under the Proposed Volcker Rule*; Konstantinovsky and Phelps (2012) as summarized in Dynkin et al.; the NY Fed's primary dealer statistics (links in the Deep-Dive Resource Graph at the end of the chapter).

## 22.2 TRACE, 2002–2027: The Transparency Ledger

**Quant-Shop Life (fictional composite): the denominator moved.** *An operations analyst on a large bank's credit-trading desk, not this book's desk. The bank, Tamsin, the exceptions and the desk's own shares are invented; the TRACE volumes, Tradeweb's footnote, FINRA's notice and FINRA's figures are real and sourced.*

Tuesday 6 October 2026, 6:50 p.m. The traders left at five. Tamsin is on the last of the day's TRACE exceptions, which is the operations seat's version of a close: a queue of trades the bank reported to FINRA that a compliance check thinks it reported wrong. The first is a capacity flag, a riskless-principal trade reported as principal because the ticket was booked from the wrong blotter; she corrects it and writes one line in the late-report log, because a correction is a report too. The second is a late as-of: a \$3mm high-yield trade done at 4:58 p.m. on Friday, booked on Monday morning, reported as of Friday, outside the fifteen-minute outer limit by most of a weekend. The trader's explanation, in the ticket's comment field, is "Friday." The third is a portfolio-trade line, one bond out of a 140-line basket that someone re-booked by hand after an allocation change, and which went to TRACE without the portfolio-trade modifier that FINRA has required since May 2023. On the tape it looks like a single-bond trade at a price that was never a single-bond price. She fixes it, links the ticket to the basket, and closes the queue at 7:20.

Then the job she actually stayed for: the monthly volume pack, eleven slides for Thursday's business review. Page four is market share, the desk's high-grade volume divided by TRACE high-grade volume, and it is the page people read. September's TRACE high-grade average daily volume, from Tradeweb's monthly report published that morning, is \$47.04bn, up 10.1% from August's \$42.71bn. The desk's share has risen from 2.9% to 3.3% *(illustrative)*, which would be the best month of the year, and Tamsin has worked in operations long enough to distrust the best month of the year.

The reason is in a footnote, and Chapter 2's Femi, at an asset manager across town, will find the same footnote from the buy side the next morning (§2.2.2). The SEC approved, in July, FINRA's extension of the affiliate-principal transaction indicator to member affiliates. When two affiliated broker-dealers pass a bond between them on its way to an outside customer, the firm can now flag the inter-affiliate leg, and TRACE suppresses it, so only the trade with the outside customer is disseminated. Regulatory Notice 26-16 (2026-08-26) made it voluntary from 2026-08-31 and mandatory from 2027-08-02. September was the first month. Tradeweb's report says the change "lowered reported U.S. High Grade TRACE volumes" and that prior periods were not restated. What it does not say is by how much. The best number Tamsin can find is FINRA's own, in its rule filing (SR-FINRA-2026-009): about 5.7% of 2025 transactions in the covered products were between affiliated members with an offsetting outside trade. It is an upper bound, and it counts trades, not dollars.

Her own bank flipped its switch on day one, which makes it worse. The desk's reported volume lost its own affiliate legs, and the denominator lost the affiliate legs of every other firm that also flipped its switch, and nobody publishes which firms those were. The September share is not comparable with August's, the August 2027 mandatory date will move it again, and the honest slide says so.

At Thursday's review the head of the business asks the question every risk committee asks of every number: "Why is this different from last month?" The desk head has a sentence ready about client engagement. Tamsin has the footnote, FINRA's 5.7%, and a sentence of her own: "Some of it is us, and some of it is that the denominator lost a leg, and I can't yet tell you the split." The page goes out with a footnote of its own and a dotted line at 31 August.

Afterwards she adds a row to a tab in her workbook called *definitions*, which nobody has asked for: date, rule, what it does to the denominator, and a column headed "comparable before?" that says no. There are already rows for the portfolio-trade modifier (2023-05-15) and the optional allocation reports (2026-06-08). It is the dating machine of this chapter being born in a back office, by hand, by someone who wanted to go home. Table 22.1 is the same tab with sources; §22.8 is what it grows into.

Information is the third thing a dealer sells, and TRACE is the rule that decides how much of it the dealer gets to keep. Mags remembers the pre-TRACE world with the fondness people reserve for wars they survived. "Back in my day the tape was the guy at the next desk who'd heard something. You priced a bond by phone and by grudge." She will also tell you, grudgingly, that the distressed desk barely noticed TRACE for its first few years, and the shelf agrees with her.

> **[SOURCE EXTRACTION]** *Moyer_Distressed_Debt_Analysis p.416 (n.62):* "The National Association of Securities Dealers requires that trades in specified bonds, usually larger issue sizes or of large capitalization firms, be electronically recorded by broker-dealers into the Trade Reporting and Comparison Entry Source (TRACE). However, most of the securities required to be posted do not constitute distressed securities."
>
> **Annotation.** Our analysis: two things are dated in this footnote, and both are useful. The acronym is wrong (TRACE is the Trade Reporting and Compliance Engine), which tells you how much attention a distressed investor of the mid-2000s paid to it. More importantly, the coverage claim was true when Moyer wrote it: dissemination was phased in by issue size and rating, and immediate dissemination of *all* public TRACE-eligible corporate bonds began only on 2006-01-09 (FINRA TRACE FactBook 2025). For a systematic desk, this means any distressed-bond liquidity series that starts before 2006 has a selection problem baked in: the bonds you can see are the large, liquid ones, which is exactly the sample that does not default. Start the panel in 2006, or carry a dissemination-phase flag.

The ledger since then, as a quant needs it, is a list of dates on which the information set changed. Table 22.1 below is that list. The academic verdict on the original 2002–2006 rollout is unusually unanimous on costs and unusually split on volume. Bessembinder, Maxwell and Venkataraman (2006), Edwards, Harris and Piwowar (2007), and Goldstein, Hotchkiss and Sirri (2007) all found that trading costs fell for bonds that became transparent; the last of these was a literal controlled experiment on a set of BBB bonds, the regulatory event study in its purest form (§22.8). Asquith, Covert and Pathak (NBER w19417, 2013, revised 2019) found that costs fell across all bond types, with high-yield costs down 22.9%, and estimated total savings of about \$600mm a year. They also found that "trading activity does not increase and, by one measure, decreases," and that by that measure high-yield activity fell 71.1%. Transparency lowered the average price of liquidity and reduced the quantity dealers were willing to supply at the margin. That is not a paradox. It is what happens when you tax the dealer's information, and the derivation below shows where the tax lands.

> **[SOURCE EXTRACTION]** *Ben_Dor_Quantitative_Credit_Portfolio_Management p.162 (n.3):* "Trade Reporting and Compliance Engine (TRACE) ... disseminates trade-by-trade corporate bond execution information within 15 minutes to all market participants. At this time, TRACE data are censored at \$5 million for investment grade and \$1 million for high-yield securities."
>
> **Annotation.** Our analysis: "at this time" was 2010, and the striking fact for a 2026 desk is that both numbers in the sentence are still the rule. FINRA Regulatory Notice 25-17 (2025-12-04) retained the 15-minute outer limit and restated the caps: investment-grade trades above \$5mm print as "5MM+" and non-investment-grade trades above \$1mm as "1MM+," with uncapped sizes released in the Historic Corporate Bond Data Set six months after quarter-end. Fifteen years of electronification, two serious attempts to change the parameters (one from each direction, both in the case study below), and the market is still running on Ben Dor's footnote. When a parameter survives that much pressure from both sides, it is an equilibrium, and an equilibrium can be priced.

### 22.2.1 Derivation: the reporting delay is an option the block dealer holds

Work under $\mathbb{P}$ with Kyle-style linear impact. Kyle's $\lambda$ is the price impact per unit of order flow the market sees: because some of the flow might be informed, the price moves against a known seller by an amount proportional to what was sold, and §18.3 builds it from the market maker's side. Here, once the market learns of a signed block of size $Q$, the mid moves against the dealer by $\lambda Q$, where $\lambda$ is impact per unit of size the market *infers*. A dealer buys a block of $Q$ (\$mm) at $t = 0$, earning a concession of $\tfrac{s_B}{2}$ (bp of price) per unit, and works it out linearly over an unwind time $T_u$, so its remaining inventory at $t$ is $Q(1 - t/T_u)$. The print becomes public after a delay $\Delta$: fifteen minutes today, one minute under the rule that died, end of day for on-the-run Treasuries.

> **Math, Gently.** *The variance of a triangle.* Draw the dealer's inventory against time: it starts at $Q$ and falls in a straight line to zero at $T_u$, a triangle. The risk of holding it is not the area of the triangle, because a price move hurts in proportion to how much you hold *and* variance grows with the square of the holding. So the right picture is the *squared* line, a curve that starts at $Q^2$ and sags toward zero. Its area is exactly a third of the rectangle $Q^2 \times T_u$ (the area under $x^2$ from 0 to 1 is $\tfrac13$), which is why a steady unwind carries a third of the variance of holding the whole block until the end. Tiny number: $Q = 15$, $T_u = 120$ minutes and $\sigma = 2.5$bp per square-root minute give $\sigma^2 Q^2 T_u/3 = 6.25 \times 225 \times 40 = 56{,}250$ in (bp$\cdot$\$mm)$^2$, against $168{,}750$ for sitting on all fifteen for two hours. Selling as you go buys back two-thirds of the variance. The integral is in the Full Derivation below.

The dealer's utility-adjusted P&L is the concession, less the *leak*, which is the impact $\lambda Q$ times the inventory still held when the print goes public, $Q(1 - \Delta/T_u)^+$, less the mean-variance penalty $\tfrac12\gamma$ times the triangle's variance:

$$
\Pi(\Delta) = \frac{s_B}{2}\,Q - \lambda Q^2\Big(1-\frac{\Delta}{T_u}\Big)^+ - \frac{\gamma\sigma^2 Q^2 T_u}{6}.
\tag{22.5}
$$

Setting $\Pi = 0$ gives the competitive block half-spread and its sensitivity to the delay:

$$
\frac{s_B^\ast}{2}(\Delta) = \lambda Q\Big(1-\frac{\Delta}{T_u}\Big)^+ + \frac{\gamma\sigma^2 Q\,T_u}{6},
\qquad
\frac{\partial s_B^\ast}{\partial \Delta} = -\frac{2\lambda Q}{T_u} \quad (\Delta < T_u).
\tag{22.6}
$$

The derivative says that a shorter delay means a wider block spread, and that the effect grows with the block. The positive part says where it lives. A riskless-principal trade, matched before it prints ($T_u \le \Delta$), pays no leak at fifteen minutes or at one. A block worked over three days barely notices the difference between one minute and fifteen, because almost all of it is still on the books either way. The trades that care are the ones where $\Delta$ and $T_u$ are comparable: the risk-transfer blocks worked out in an hour or two through ETFs, CDS and portfolio trades. And if the aim were to protect a multi-day unwind, the delay would have to be measured in days, which is why the 2019 block proposal paired higher caps with a 48-hour delay.

*Worked example (illustrative):* $\lambda = 0.5$bp per \$mm, $Q = 15$, $T_u = 120$ minutes, $\sigma = 2.5$bp$/\sqrt{\text{min}}$ (about 50bp of price a day, a 10-year BBB), $\gamma = 0.001$ per bp·\$mm. The inventory term is $0.001 \times 6.25 \times 15 \times 120/6 = 1.875$bp. At $\Delta = 15$ the leak term is $7.5 \times 0.875 = 6.56$bp, for a half-spread of 8.44bp; at $\Delta = 1$ it is $7.5 \times 0.992 = 7.44$bp, for 9.31bp. The one-minute rule would have widened this block by about 0.9bp, roughly 10%, which on a desk printing a few thousand such blocks a year is a line item someone would write a comment letter about. Figure 22.4 shows how the sensitivity to the delay depends on the unwind time.

![Figure 22.4: A shorter reporting delay widens the block spread only when the unwind time is comparable to the delay: moving from 15 minutes to 1 minute costs a 2-hour unwind about 0.9bp and a 15-minute unwind about 7bp, but a 10-hour unwind only about 0.2bp. Illustrative: eq. (22.6) with impact 0.5bp per \$mm, block size \$15mm, volatility 2.5bp per square-root minute, and risk aversion 0.001.](assets/figures/ch22_block_spread_delay.png)

#### The Full Derivation: the delay as an option

The leak is the impact times the inventory still held at publication:

$$
\text{Leak}(\Delta) = \lambda Q \cdot Q\Big(1 - \frac{\Delta}{T_u}\Big)^+ .
$$

The inventory-risk cost is the mean-variance penalty on the unwind. With mid volatility $\sigma$ (bp per $\sqrt{\text{minute}}$), the P&L variance of a linear unwind is $\int_0^{T_u}\sigma^2 Q^2 (1 - t/T_u)^2\,dt = \sigma^2 Q^2 T_u/3$ (substitute $u = 1 - t/T_u$ and the integral becomes $T_u\int_0^1 u^2\,du$), so the penalty is $\tfrac12\gamma\sigma^2Q^2T_u/3$. Concession minus leak minus penalty is (22.5); dividing $\Pi = 0$ by $Q$ gives the half-spread in (22.6), and differentiating the positive part in $\Delta$ gives its slope. The delay is an option in the plain sense: it is a right the block dealer holds, worth $2\lambda Q/T_u$ of spread per unit of delay while it is in the money ($\Delta < T_u$) and nothing once the unwind is done before the print.

### 22.2.2 Derivation: what hides behind "5MM+"

> **Math, Gently.** *Tails that have no variance.* A distribution is a rule for how likely each size is. Ask one a desk question: of the trades that print as "5MM+," how big is a typical one? Picture a month of those blocks laid along a shelf in order of size, and find the point where the shelf balances, its center of mass, which is the mean. Three shapes give three very different shelves. A *normal*, the bell, puts the blocks symmetrically around the middle, so the balance point and the middle block, the median, coincide, and its tail is so thin that a block five standard deviations out essentially never turns up. A *lognormal* is a bell drawn on the logarithm of size: it cannot go below zero and it leans right, so the mean sits above the median, but the far end of the shelf is still sparse enough that the spread of sizes, the variance, is a finite number. A *Pareto* is a power law: the chance of a block bigger than $x$ falls like $x^{-\alpha}$, so doubling the size divides the odds only by $2^{\alpha}$. Tiny number: ten blocks above the cap, nine between \$5mm and \$10mm averaging \$7mm, and one at \$60mm. The median is about \$7mm, the mean is $(63 + 60)/10 = \$12.3$mm, and one block carries half the volume. Move the giant and the balance point jumps, which is what it means in practice for the variance not to exist. For a Pareto the mean is finite only when $\alpha > 1$ and the variance only when $\alpha > 2$, because the far end of the shelf is weighted by size squared and that sum never settles when $\alpha \le 2$. On a desk the normal is a fair first guess for daily spread changes in a calm week, the lognormal for prices and spread levels, which cannot go negative and compound, and the Pareto for trade sizes and portfolio losses. Chapter 5 builds the family (§5.7.2 and §5.8); the next paragraph needs only the Pareto.

Printed size is $\tilde Q = \min(Q, C)$ plus a flag, with $C = 5$ (\$mm, IG) or $C = 1$ (HY). The market cannot see $Q$ above the cap, so it updates on $\mathbb{E}[Q \mid Q > C]$. Suppose sizes above the cap are Pareto with tail index $\alpha > 1$: $\mathbb{P}(Q > x \mid Q > C) = (C/x)^{\alpha}$ for $x \ge C$. Then

$$
\mathbb{E}[Q \mid Q > C] = \int_C^\infty x\,\frac{\alpha C^\alpha}{x^{\alpha+1}}\,dx = \frac{\alpha}{\alpha - 1}\,C \equiv m\,C,
\qquad
\alpha = \frac{m}{m-1}.
\tag{22.7}
$$

Every capped print therefore moves the market by the same $\lambda m C$, whatever its true size. Two consequences follow. The cap **pools** blocks: a \$25mm block is subsidized (the market infers less than the truth), and a \$6mm block just over the cap is taxed (the market infers more). And the dealer that did the trade knows $Q$, so it holds an information edge of $\lambda(Q - mC)$ until the uncapped historic file appears six months after quarter-end.

The shelf gives us $m$ directly, which is a pleasing accident.

> **[SOURCE EXTRACTION]** *Ben_Dor_Quantitative_Credit_Portfolio_Management p.364 (n.8):* "TRACE truncates the sizes of large transactions at \$1 million and \$5 million for high-yield and investment-grade bonds, respectively ... Alternative transaction caps can be imputed based on equating the sum of individual trades with the aggregate volume figures reported by TRACE. This procedure yields higher transaction limits of \$4 million and \$12.5 million"
>
> **Annotation.** Our analysis: Ben Dor and coauthors used the imputed caps to fix a volume series. We can use them to back out a tail index. Matching the sum of trades to aggregate volume is exactly estimating $\mathbb{E}[Q \mid Q > C]$, so $m_{\text{IG}} = 12.5/5 = 2.5$ and $m_{\text{HY}} = 4/1 = 4$. By (22.7) that gives $\alpha_{\text{IG}} = 5/3 \approx 1.67$ and $\alpha_{\text{HY}} = 4/3 \approx 1.33$. Both are below 2, so the variance of block size above the cap does not exist. That is why averaging capped sizes produces garbage, and why the median capped IG block ($C \cdot 2^{1/\alpha} \approx$ \$7.6mm) sits so far below the mean (\$12.5mm). The modern desk departs from the footnote in one respect: estimate $\alpha$ from the uncapped historic file, by rating bucket and year, rather than from a single 2010-era aggregate match. Portfolio trading has fattened the tail since then.

### 22.2.3 Case Study: The One-Minute Rule That Died (2022–2025), and the Block Pilot That Never Lived (2019)

Two attempts were made to change TRACE's parameters in the last seven years, one from each direction, and both failed. The desk learned the episode the way it learns most things, by replaying it blind.

#### Long Scene: the rule that was approved and never happened

*A replay, run on Friday 2 October 2026 at 3:30 p.m., with Ines's folder cut at each date shown: nothing after a cut date is on the table until she opens the next envelope. The desk's cards, flags and illustrative numbers are invented; the FINRA notices, the SEC order, the dates and every quotation are real.*

Friday replays are Ines's ritual: a real episode, cut off at a date and traded blind (Ch 1 §1.8.2). This one had no bond in it. The folder on the conference-room table said *FINRA, 2019–2025* in her handwriting and held four envelopes, and Theo, at the end of his second week, had already learned that the number of envelopes is the number of times somebody will be wrong.

**Beat 1: Thursday 11 January 2024.** The first envelope held two documents. FINRA Regulatory Notice 22-17, dated 2 August 2022, asked for comment on cutting TRACE's outer reporting limit from fifteen minutes to one. The second was what came of it seventeen months later: rule filing SR-FINRA-2024-004, filed with the SEC that Thursday, which would "reduce the 15-minute TRACE reporting timeframe to one minute," with "exceptions for member firms with de minimis reporting activity and for manual trades."

Kaz read the first page and opened a laptop. "Easy. A flag. `one_minute_rule`, False until the SEC approves it, True after. Every spread model gets an interaction term, and we're done before the coffee's cold."

"True from when?" Ines asked.

"From approval. Approval is the event. That's when quoting changes."

Theo was on the page where restructuring bankers live, the one with the exceptions. "Manual trades are exempt." He read it again. "Who books manual trades?"

"Voice desks," Mags said. "Blocks. Anything too big or too strange to go through a pipe."

"So it's a carve-out." Theo had drafted dozens. "When a credit agreement has a basket that applies to everyone except one kind of transaction, somebody in the room did that kind of transaction for a living."

"Or somebody in the room was going to lose money on it," Ines said. "Let me show you which." She took the Calloway ticket from the Monday before quarter-end, the one the desk had lost by a quarter of a cent, and played it as if they had won it.

> **Poker Table.** Ines replays the cold open as a hand history. "We buy fifteen million. The print shows at minute fifteen as '5MM+ sell,' and the table assumes twelve and a half, not fifteen, so the cap just hid two and a half million of our size, worth about a basis point and a quarter of impact *(illustrative, at $\lambda = 0.5$bp per \$mm)*. By minute fifteen we've worked out an eighth of it. Markouts: flat at five minutes, down 4bp at thirty, down 6 at the close *(illustrative)*. Under a one-minute rule the thirty-minute markout comes at minute one, before we've sold anything. Same hand, worse position at the table. That's why the block desks folded the one-minute rule, and why nobody at this table will ever vote to lower the cap."

Kaz looked up from the laptop. "You said 'folded.' Past tense."

"I'm the dealer," Ines said. "I'm allowed to know how the hand ended. You're not allowed to know when."

**Beat 2: the same afternoon, pricing it.** Kaz built the pricing first, because pricing is the part Kaz trusts. Equation (22.6) needs only the worked example's parameters, impact of half a basis point per \$mm, a \$15mm block, 2.5bp of volatility per square-root minute and the desk's risk aversion, and one more number: how long the block takes to work out. Kaz ran three unwind times and put them on the screen, which is how Figure 22.4 was born. For a block worked out over two hours, cutting the delay from fifteen minutes to one widens the competitive half-spread from 8.44bp to 9.31bp, about 0.9bp. For a block worked out in fifteen minutes, it costs about 7bp, because at fifteen minutes the dealer is already flat when the print appears, and at one minute it is still holding almost all of it. For a block worked over ten hours, it costs about 0.2bp, because the dealer is holding nearly everything at minute one *and* at minute fifteen, and the extra fourteen minutes of secrecy were never protecting much.

"So for most of the book it costs nothing," Kaz said.

"For most of the *tickets* it costs nothing," Theo said. He had the desk's RFQ log open, sorted by size. The auto-quoter answers most of the desk's tickets, and most of those it answers riskless or nearly so: it has the other side lined up before the print, so $T_u \le \Delta$ and the positive part in (22.6) is zero at fifteen minutes or at one. Those engines were indifferent to the rule. The blocks were not, and the blocks that minded most were the risk-transfer trades worked out in an hour or two through ETFs, CDS and portfolio trades, which is where the desk earns the spread it can actually see. "And the manual-trade exception lands on exactly those," Theo said. "Whoever wrote it had read (22.6), or had a client who had."

"Nobody reads my equations," Kaz said.

"FINRA read the comment letters," said Mags. "Same thing, with more lawyers."

**Beat 3: 2019, from the other end.** Mags had brought her own envelope, which is against the rules of the replay and which Ines allowed because it was older than the cut. It held FINRA Regulatory Notice 19-12. In 2019 FINRA had sought comment on a pilot, recommended by the SEC's Fixed Income Market Structure Advisory Committee, that would have raised the dissemination caps to \$10mm for investment grade and \$5mm for high yield, and delayed dissemination of trades above the new caps by 48 hours. Some commenters warned that more size transparency would make dealers "even more reluctant to position bonds." The pilot was not adopted.

"Same fight," Mags said. "Turned round. In 2019 they wanted to show the size and offered the block desks two days of quiet to pay for it. Now they want to show the print faster and they're offering nothing." She tapped the two notices. "They tried it from both ends and the middle held."

Kaz put the 2019 version through (22.6) out of curiosity. A 48-hour delay pushes $\Delta$ past any unwind shorter than two days, so the positive part goes to zero and the leak disappears for every block a dealer could reasonably work out. That was the subsidy, sized to multi-day unwinds. The tax was the size: under higher caps the market would see \$10mm where it used to see "5MM+," a more precise signal about exactly the trades a block dealer would rather keep vague (§22.2.2 prices that). One proposal bought more size information with more delay; the other wanted less delay and offered no compensation. Each moved one parameter in the transparency advocates' favor and needed a compensating move in the block dealers' favor.

"So which is it in February?" Theo asked. "Does this one get its compensation or not?"

"That," Ines said, "is the card."

#### Decision point: February 2024

*It is February 2024. The filing is public, the SEC has not yet ruled, and the 2019 pilot is five years dead. Write three things: which population of your trades you reprice, from which date you flag the regime, and what you will record if the rule dies.*

Kaz's card was the fastest and the most confident. *Reprice every trade by the one-minute leak. Flag from the approval date. If it dies, delete the flag.* Theo's was narrower. *Reprice blocks with unwind times between fifteen minutes and a few hours; leave the auto-quoter alone. Flag from the effective date, not the approval.* On the third line he had written, and crossed out, "nothing to record," and left the line blank. Mags's card said: *Reprice nothing until there is an effective date. If it dies, I buy lunch.* Ines's own card went into the fourth envelope, sealed, the way she always did it, and Theo noticed for the first time that she wrote her card before the replay started.

Write yours before reading on.

**Beat 4: the envelope, 20 September 2024 to 4 December 2025.** The fourth envelope was thicker than the others. On top was the SEC's order of 20 September 2024 (Release 34-101121), approving the one-minute rule as modified by a partial amendment. Kaz's flag would have switched on that day.

Underneath, there was very little. No effective date was set; FINRA signalled in early 2025 that it would not set one (Chapter 2 has the trade-press account). On 2025-09-16 the SEC approved the rescission. And on 2025-12-04, Regulatory Notice 25-17: "FINRA is not moving forward with its proposal to reduce the 15-minute TRACE reporting outer limit to one minute." The stated reason was that "firms raised additional concerns and questions in connection with aspects of the approved reduced reporting time regime," and the notice added the line Ines had printed in large type and taped to the inside of the envelope: "While the Securities and Exchange Commission approved these amendments, they have not taken effect." The same notice restated the caps at \$5mm and \$1mm. Fifteen minutes and \$5mm/\$1mm had survived both attacks.

The grading took ten minutes, which at Ines's table is mercy.

Kaz's flag switched on in September 2024 and never switched off. A model trained across it would have learned that "the one-minute regime" coincided with everything else that happened afterwards, the April 2025 tariff week included, and would have credited a rule that never took effect with the widest block spreads of the year. It is the same mistake as ROBO's in the Spec below, made by a human with a PhD, which Kaz took well. "A dummy that's on during a stress," they said, "is a stress dummy with a regulatory name."

Theo had the right population. Equation (22.6) says the rule taxed exactly one kind of trade, the block unwound in an hour or two, and his card repriced exactly that kind. His instinct to wait for the effective date was right too, as far as the flag went. What he had missed was the second flag. Quoting behavior can move on an approval, because dealers price the rule they expect, so the approval date deserves its own column, separate from the effective date, even if nothing moves on it. And his blank third line was the most expensive blank on the table.

Mags's card was the cheapest and very nearly right about prices, since nothing changed in the quotes. It recorded nothing, so it taught the model nothing.

Ines opened her own. *Flag proposal (2022-08-02), filing (2024-01-11), approval and effective date as separate columns. Price blocks under both regimes and keep the switch ready. If it dies, record the death as a date.*

"Why the death?" Theo asked. "Nothing happened."

"That's why," Ines said. "Kaz, what's the hardest thing to find when you want to know whether a rule moved your data?"

Kaz did not need long. "A date where everything else happened and the rule didn't." They looked at the card again. "Approved, announced, priced by everybody in the market, and never in force. If my event study finds a liquidity effect on 4 December 2025, my event study is broken."

"So the best control date in the book," Ines said, "is the one on which nothing happened."

Mags bought lunch anyway, on the grounds that she had been right about the prices and wanted it on the record. Kaz added a row to `REGIME_DATES` with `one_minute_rule = False` for every date there has ever been, and a separate column called `approved_never_effective`. Theo filled in his blank third line, in ink, after the fact, which Ines allowed, since that is what a hand history is for. Section 22.8 builds the event study that uses the date.

Kaz's flag is item (5) of the Ways This Blows Up box below, and Table 22.1, in the Trend Watch, is the regime table the replay ended with.

> **Trend Watch: TRACE and adjacent reporting regimes as a table of structural breaks (Table 22.1).** *What changed:* the information set, about once a year. *Sources:* FINRA TRACE FactBook 2025; FINRA Regulatory Notices 22-12, 25-17, 26-16; SEC releases as noted; dates marked *approx.* rest on secondary sources.
>
> | Effective | Change | What breaks in your data |
> | :--- | :--- | :--- |
> | 2002-07 | TRACE dissemination begins, phased by size and rating | Pre-2006 samples overweight large, liquid bonds |
> | 2006-01-09 | Immediate dissemination of all public TRACE-eligible corporates | Coverage break in any distressed liquidity series |
> | 2017-07-10 | Treasuries reportable (regulatory use only) | Treasury data exist from here, but not publicly |
> | 2022-02-14 | SBSR public dissemination of security-based swaps, including single-name CDS *(approx.; trade press)* | Single-name CDS prints become observable (§22.6) |
> | 2022-09-01 | Covered depository institutions report Treasury trades | Treasury coverage jumps |
> | 2023-05-15 | Portfolio-trade modifier mandatory (≥10 issues, single basket price) | PT prints separable; "price" of a PT line is not a bond-level price |
> | 2024-03-25 | End-of-day dissemination of individual on-the-run nominal Treasury trades *(approx.; FINRA Rule 6750 materials)* | Public Treasury trade data begin |
> | 2024-05-28 | T+1 settlement for corporates (§22.3) | Settlement-date fields shift by a day |
> | 2025-09-16 | One-minute reporting rescinded (SEC approved the rescission on 2025-09-16; FINRA announced it on 2025-12-04; the 2024 approval never took effect) | Nothing. Use it as a placebo |
> | 2026-06-08 | Optional aggregate allocation reports (Rule 6730.08) for dual BD/IA firms | Print counts fall for the same economic volume |
> | 2026-08-31 | Affiliate indicator extended to member affiliates, voluntary | Duplicate affiliate prints begin to be flagged |
> | 2027-08-02 | Affiliate indicator mandatory | Volume series de-inflates; one June 2026 industry estimate put duplicate affiliate prints at up to 8% of HG TRACE volume *(approx.)* |
>
> *What it means for the desk:* a liquidity feature built on raw TRACE volume from 2020 to 2027 crosses at least four definitional breaks. Volume did not change on those dates; the meaning of a print did.

> **Ways This Blows Up.** (1) *A liquidity model fit on 2020–2026 volume* straddles the PT modifier and the allocation-report change, so the fitted "trend in liquidity" is partly a trend in reporting conventions. (2) *Averaging capped sizes at the cap* understates IG block volume by a factor of $m = 2.5$ on the capped share; averaging them at \$12.5mm is right on average and wrong for every individual trade. (3) *Fitting $\alpha$ on the live feed* is impossible, since the live feed is censored by construction; use the historic file. (4) *PT prints as bond prices.* A portfolio-trade line carries a basket-level price allocated across bonds. Feed those prints to a bond-level fair-value model and it learns the dealer's allocation scheme. (5) *Setting `one_minute_rule = True` from the approval date* because the approval was in the news: the rule was approved and never took effect.

### Specification for AI Implementation (TRACE regime layer)

**The Spec You Hand the Robot.** *Vague version:* "clean TRACE and flag the regime changes." *What ROBO built:* a flag for every FINRA notice ever published, all of them set from the publication date, including a one-minute flag that switched on in 2024 and never switched off. *Precise version:* implement the block half-spread (22.6) with the positive-part guard, the censored-size impact and tail index (22.7), and a regime-flag layer driven by one dated table (`REGIME_DATES`) that every other chapter imports. Inputs: `trade_dt` timezone-aware (reject naive timestamps), `bond_id` (str, never a made-up CUSIP), `size_mm` as disseminated (\$mm), `side`, `price`, `rating_bucket` in {"IG", "HY"}. Flags compare the New York *calendar date* of the trade with the effective date. `one_minute_rule` is always False. Units are bp of price, \$mm, and minutes.

Two jobs follow from everything above, and they look unrelated until you try to do them badly. The first is economic: a block dealer wants to know what a trade is worth when the world finds out about it in fifteen minutes rather than one, and what the market will believe about a print that says only "5MM+." The second is clerical and much less glamorous: someone has to decide, for every row of a TRACE file, which rulebook was in force on the day it printed. A liquidity model that skips the second job will cheerfully learn a trend in reporting conventions and call it a trend in liquidity. A desk automates both so that the answer comes from one dated table and one tested formula, rather than from whichever analyst last read the FINRA notices.

The listing has three numerical functions and one data-cleaning layer. `block_half_spread` implements (22.6). It takes the impact per \$mm the market infers, the true block size, the reporting delay and unwind time in minutes, risk aversion, and volatility in bp per square-root minute. It returns the zero-profit half-spread in bp: a leak term, impact times inferred size times the unwound-after-publication fraction `max(0, 1 - delay / unwind_time)`, plus the inventory term `gamma * sigma^2 * Q * unwind_time / 6`. The positive-part guard is what makes a 48-hour delay collapse the leak to zero while leaving the inventory cost standing. `pareto_alpha_from_imputed_mean` inverts (22.7), turning an assumed mean above the cap into a tail index, and `censored_impact` returns the impact that every capped print carries, `lam * m * cap`. Both reject inputs that would make the tail mean infinite or undefined.

`trace_regime_flags` is the clerical layer. It refuses naive timestamps, refuses any `rating_bucket` other than IG or HY, converts each trade to its New York calendar date, and sets one boolean per entry in `REGIME_DATES`, plus `size_capped` and `dup_risk`. The `one_minute_rule` column is hard-wired to False, because that rule was approved and never took effect. The assertions reproduce the worked example (8.44bp at fifteen minutes, 9.31bp at one), check that the spread never rises with the delay, and confirm that a Friday-afternoon and a Monday-morning print differ only on the portfolio-trade modifier.

Use it for scenario work on block pricing and as the first cleaning pass on any multi-year TRACE panel. Do not use it to estimate $\lambda$ or $\alpha$ from the live feed, which is censored by construction. The edge case that bites is `inferred_size`. It defaults to the true size, which is right for a \$5mm trade and wrong for a \$25mm block that printed "5MM+": the market inferred \$12.5mm, and the dealer's information edge is the difference. Also note that `size_capped` uses `>=`, because a disseminated size equal to the cap is the cap, not a trade of exactly that size.

*The full listing is [Listing 22.2 in Appendix F](#code-22-2).*

*Further reading for this section:* Asquith, Covert and Pathak (2013/2019); Goldstein, Hotchkiss and Sirri (2007); FINRA Regulatory Notices 19-12, 22-12, 22-17, 25-17 and 26-16; FINRA Rule 6730 (links at the end of the chapter).

## 22.3 T+1 and the Settlement Clock

Time is the second thing a dealer sells, and the settlement cycle is the most literal clock in the business: the number of days between the handshake and the money. To a restructuring banker a settlement cycle looks like plumbing; to a risk manager it is a horizon, and horizons are where square roots live.

The SEC adopted T+1 on 2023-02-15, moving most broker-dealer securities transactions from two business days to one, and the industry switched on 2024-05-28, the Tuesday after Memorial Day. The rule also required same-day affirmation "as soon as technologically practicable and no later than the end of trade date," made investment advisers keep records of allocations, confirmations and affirmations, and required central matching service providers to adopt straight-through-processing policies. The SEC chair at the time said it "will reduce latency, lower risk, and promote efficiency." Treasuries were never part of this: as exempt securities they already settled T+1 by market convention.

### 22.3.1 Derivation: why T+1 cut margin by about a quarter

> **Math, Gently.** *Why risk grows with the square root of time.* A drunk leaves a lamppost and takes steps of one metre, each one left or right at random. After one step he is a metre away. After a hundred steps he is not a hundred metres away, because half his steps undo the other half; on average he is about ten metres away, the square root of a hundred. The steps cancel, and what survives the cancelling grows like $\sqrt{n}$. A price that moves by independent daily shocks is the same walk, a *random walk*. Tiny number: if a bond moves 1% a day, two days of moves give a typical move of $\sqrt2 \times 1\% \approx 1.41\%$, not 2%, because the second day is as likely to undo the first as to repeat it. Run it backwards and a clearing house that used to cover two days and now covers one needs $\sqrt{1/2} \approx 0.707$ of the margin, not half of it. That is the whole of (22.8) below, plus the close-out days. The cancelling is also the weakness: in a trending market today's move predicts tomorrow's, the steps stop undoing each other, and risk grows closer to linearly with time. Chapter 5 builds the random walk properly (§5.2.3).

A clearing agency's margin covers the loss on a member's open positions between trade and close-out. If the member defaults, the clearing agency is exposed from the trade until settlement, and then for however long it takes to liquidate, so the horizon is $H = T_{\text{settle}} + T_{\text{co}}$ days. Under $\mathbb{P}$, with daily price changes independent and of volatility $\sigma$, the loss over $H$ days has standard deviation $\sigma\sqrt{H}$. A value-at-risk-style margin at a fixed confidence level scales the same way, $\text{IM} = z_{\alpha}\,\sigma\sqrt{H}\cdot|\text{position}|$. The confidence multiplier, the volatility, and the position all cancel in the ratio:

$$
\frac{\text{IM}_{T+1}}{\text{IM}_{T+2}} = \sqrt{\frac{1 + T_{\text{co}}}{2 + T_{\text{co}}}} =
\begin{cases} 0.707 & (T_{\text{co}} = 0):\ -29\% \\ 0.816 & (T_{\text{co}} = 1):\ -18\% \end{cases}
\tag{22.8}
$$

The two brackets correspond to whether liquidation is instantaneous or takes a day, so the theory says T+1 should have cut the volatility part of clearing margin by between 18% and 29%. The case study below holds that bracket up against DTCC's published numbers.

*Error-prone spots.* NSCC margin has a volatility component plus add-ons (mark-to-market, liquidity, concentration, backtesting) that do not scale with $\sqrt{H}$, so apply (22.8) to the volatility component only. The square root also assumes independent daily changes. In a trending, autocorrelated market the horizon effect is closer to linear, so a T+1 saving computed in calm data overstates the saving in a crisis. The clock helps least when you need it most, a theme that will recur.

### 22.3.2 Fails, and the identity hiding in the fails charge

A shorter cycle shrinks the *window* of counterparty exposure and raises the *probability* of a fail, because there is less time to locate the bond. The cost of failing has a clean identity. A seller who fails to deliver does not receive the cash until it does, so it forgoes interest at roughly the short rate $r^{\text{ref}}$. The Treasury Market Practices Group (TMPG) fails charge adds $\max(0,\ 3\% - r^{\text{ref}})$ per year, accrued as $\text{Par}\times\text{rate}\times\text{days}/360$. Adding the two, and taking the reference rate as the seller's reinvestment rate:

$$
\text{cost of failing (per year)} = r^{\text{ref}} + \max\!\big(0,\ 3\% - r^{\text{ref}}\big) = \max\!\big(r^{\text{ref}},\ 3\%\big).
\tag{22.9}
$$

The charge is a floor on the cost of failing. Above 3% it is zero and the market's own interest rate disciplines fails. Below 3%, without it, failing at zero rates is free, which is exactly what happened in 2008–2009. Check the TMPG's current definition of the reference rate before using (22.9) in production; the structure is what matters here.

> **[SOURCE EXTRACTION]** *Veronesi_Fixed_Income_Securities p.57:* "Starting May 1, 2009, the Federal Reserve imposed a penalty charge of 3% over its Fed funds rate for failing to deliver the bonds in the repo transactions the Federal Reserve conducts daily in its open market operations." And: "on May 1, 2009, the repo rate for some Treasury securities that were on special became negative."
>
> **Annotation.** Our analysis: Veronesi's textbook records the moment a fails penalty changed the sign of an interest rate. With the policy rate near zero, a bond on special could not trade below a 0% repo rate as long as failing was free; once failing cost 3%, lenders of cash would accept a negative repo rate to get the bond rather than fail. (The Fed's own penalty in the quotation was set relative to the fed funds rate; the industry fails charge in (22.9) is stated as 3% *minus* a reference rate. Both put a floor under the cost of failing.) The 2026 desk departs from 2009 in the regime: with reference rates above 3% for most of 2023–2025 *(approx.)*, the charge has been near zero and fails have been disciplined by carry, not by penalty. The day rates fall back toward zero, the charge wakes up, specials can again go negative, and any short-financing model calibrated on 2023–2025 will be wrong in exactly that direction.

The 2024 fail data matched the identity's prediction of "not much changes": the continuous net settlement (CNS) fail rate on the switch is in the case study below, and it averaged 2.12% in July 2024 *(approx.; DTCC after-action reporting)*. The cost moved to the operations desk, which now affirms on trade date, and to the people whose other legs did not move: a non-US buyer funding in FX that settles on a T+2 spot convention must pre-fund or trade FX for same-day settlement; an ETF authorized participant matching creation baskets against bonds settling T+1 runs a funding gap whenever the fund's own cycle differs (Chapter 20); and a loan trade still settles in days to weeks, so a CLO that sells bonds to buy loans is short cash for the gap (Chapter 21). The EU and UK plan their move to T+1 for 2027-10-11 *(ESMA and FCA announcements; approx.)*, which will move the FX-mismatch problem from New York to London.

### 22.3.3 Case Study: May 28–29, 2024, the Weekend the Clock Moved

*A day on this desk retold from its own operations log. Wednesday 29 May 2024 happened, and Mags was here for it; Theo and Kaz were not, and they hear it on Wednesday 14 October 2026. The desk's internal counts are illustrative; DTCC's figures are approximate, from the DTCC/SIFMA/ICI after-action reporting of 2024.*

Theo found the log by accident, looking for something else: a shared folder called *T1 cutover*, last modified in June 2024, with a checklist, a spreadsheet of trade counts and a file named `wednesday.txt` that turned out to be a minute-by-minute diary kept by the desk's operations lead. He asked Mags about it, because Mags had been on the desk then and because she was the only person in the room who would admit to remembering an operations cutover with affection.

"The Wednesday," she said. "Double settlement." Monday 27 May 2024 was Memorial Day. Trades done on Friday the 24th still settled T+2 under the old cycle, which put them on Wednesday the 29th. Trades done on Tuesday the 28th, the first day of T+1, settled one business day later, which was also Wednesday the 29th. Two days of trades, one settlement day. "Everybody's nightmare was the affirmations. In January only about 73% of trades got affirmed by DTC's cutoff. Affirmation is the buyer and seller both saying yes, that's the trade, before it settles. Under T+2 you had a day of slack to chase the stragglers. Under T+1 you had the evening."

The diary agreed with her. The operations team was in at six. By noon the desk had two days' worth of trades in the settlement queue, about 1.8 times a normal Wednesday's count *(illustrative)*, and a single unaffirmed client allocation from Friday that sat at the top of the exceptions list until 4:15 p.m., when the client's back office, which had also been in at six, sent the confirmation with an apology that the diary records in full. "Back in my day," Mags said, "which in this case is September 2017, when we went from T+3 to T+2, the exceptions list had forty lines on it by lunch and we finished at eleven at night. This was better. It was boring. Boring is what an operations cutover is for."

What happened, market-wide, is in DTCC's numbers. On 29 May 2024, 94.55% of transactions were affirmed by the 9:00 p.m. ET DTC cutoff, a rise of more than twenty points in four months. The continuous net settlement fail rate was 1.90% on the first T+1 day, against a May 2024 T+2 average of 2.01%. Nothing broke.

Theo read the affirmation number twice. "Twenty points in four months," he said. "Because there was a date." He had seen the mechanism at PJT more times than he could count: nothing gets a borrower's reporting package delivered on time like a covenant with a hard test date. Nobody had made the back offices of the buy side faster by asking nicely for seven years. A Tuesday in May did it.

Kaz cared about a different line in the after-action report, the one about margin, and went quiet in the way that means they are checking something they would rather not be wrong about. Equation (22.8) had been on the whiteboard since the morning: if clearing margin covers the settlement window plus the close-out, and risk grows like the square root of the window, then going from two days to one should cut the volatility part of the margin to between 0.707 and 0.816 of its old size, depending on whether liquidation takes no time or a day. According to the DTCC/SIFMA/ICI after-action reporting, NSCC's clearing fund fell from \$12.8bn under T+2 to \$9.1bn in an early snapshot (−29%) and to \$9.8bn on a three-month average basis (−23%) *(approx.; DTCC, 2024)*. That is a fall of \$3.0bn, or 23%, on the average.

"Twenty-nine percent is the bottom of the bracket," Kaz said, "and twenty-three is close to the middle." They exhaled. "A one-line derivation, a published number, and an honest fit, not a cherry-pick. The empirical ratio is in the range the theory allows. It would have been embarrassing if it weren't." The more durable number, the three-month average, is the one near the middle. Kaz's reading was that the early snapshot had caught a quiet week, and that by the average the add-ons that do not scale with $\sqrt{H}$ had settled back in; the after-action report does not say.

Then Kaz did the boring thing, which was the useful thing. They searched the desk's carry code for the settlement offset and found it, hard-coded as `2`, in a function last touched in 2023 *(illustrative)*. Every accrual on every trade after 28 May 2024 had been computed with a settlement date one business day late, which on a 5% bond is about 1.4 cents per hundred of accrued interest, per trade, all of it in the same direction. "One day of accrual," Kaz said. "On every trade since the switch. That's not a bug, that's a regime."

"It's both," Ines said, from the next desk. "Put it in the table." The `t_plus_1` row went into the regime table with 2024-05-28 as its date (Table 22.1), and every settlement-date field in the training data shifted with it. Ines added two expectations of her own, both of which the data had borne out: lower clearing-fund calls for broker-dealer affiliates, and slightly higher fail *probabilities* for hard-to-borrow shorts, because a shorter cycle leaves less time to find the bond. And she made Kaz put the double-settlement Wednesday itself into the event-study calendar of §22.8 as a known liquidity-supply shock, a day when two days of settlements competed for the same cash and the same operations staff, so that no future model would find it in the residuals and call it noise.

*Money Stuff*'s podcast led with the switch three days later ("T+Lunchtime," 31 May 2024, in the Resource Graph), which is about the level of excitement the day deserved, and is the highest compliment an operations team ever receives.

### Specification for AI Implementation (settlement clock)

**The Spec You Hand the Robot.** *Vague version:* "estimate the margin saving from T+1." *What ROBO built:* the ratio $1/2$, because one day is half of two days, and a report claiming margin had halved. *Precise version:* implement (22.8) as `margin_ratio(t_old, t_new, closeout_days)` with the square root applied to the horizon *including* close-out, reject negative day counts, and check that DTCC's published ratios fall inside the $T_{\text{co}} \in \{0, 1\}$ bracket. Implement (22.9) returning both the total cost of failing and the charge, as annual decimals.

Every settlement-cycle change produces the same meeting. Treasury or the prime broker asks how much margin the new cycle frees, someone says "half, because two days became one," and the room nods because the arithmetic is the kind that survives a nod. It is also wrong, and against a clearing fund of \$12.8bn the gap between halving and the square-root answer is billions of dollars. The corrective is two lines of code, which is exactly why it belongs in a tested function rather than in the memory of whoever was in the meeting last time. The fails charge is the same story in miniature: a floor that matters only when rates fall, and so is forgotten until the quarter it matters.

The listing holds two functions and four assertions. `margin_ratio` implements (22.8): it takes the old settlement horizon, the new one, and the close-out days, and returns the square root of `(t_new + closeout) / (t_old + closeout)`. The square root is the whole point. The close-out days sit inside both horizons, which is why a one-day close-out lifts the T+2 to T+1 ratio from 0.707 to 0.816 rather than leaving it at 0.5. The function rejects negative day counts and a non-positive old horizon, so the denominator cannot vanish. `fail_cost_annual` implements (22.9). Given a reference rate as a decimal, it returns a pair: the total annual cost of failing and the fails charge, `max(0, floor - r_ref)`, with the 3% floor as a default argument. The total is simply the larger of the reference rate and the floor.

The assertions do the checking that matters. They pin both brackets of (22.8) to five decimals, confirm that the two published NSCC clearing-fund ratios, 9.1 over 12.8 and 9.8 over 12.8, land between them, check that the failing cost is 3% at a zero rate and the bare rate at 4.5%, and assert that the answer is not 0.5.

Use `margin_ratio` for a first-pass estimate of how a horizon change moves the volatility-driven part of a clearing requirement, and for sanity-checking a clearinghouse's announced change. Do not use it for the total margin call. The edge case that bites is exactly that: NSCC margin carries mark-to-market, liquidity, concentration and backtesting add-ons that do not scale with the square root of the horizon, and the function has no way to know which part of your number it is being applied to. That the published totals fall inside the bracket is a plausibility check, not a license. Note too that `fail_cost_annual` returns an annual decimal. The charge itself accrues on par over 360, so the day-count conversion is yours to make.

*The full listing is [Listing 22.3 in Appendix F](#code-22-3).*

*Further reading for this section:* SEC press release 2023-29 (T+1 adoption); the DTCC/SIFMA/ICI T+1 after-action report (2024); TMPG best-practice materials on fails charges (title only).

## 22.4 The Treasury Clearing Mandate: Netting, Margin, and the Price of a Very Large Market

Why does a credit desk care about Treasury clearing? Three reasons, in increasing order of how much they cost when ignored. Every IG bond the desk owns is hedged with Treasuries or Treasury futures. Every bond the desk owns is financed in repo. And the same dealer balance sheet intermediates both, so when Treasury intermediation consumes the balance sheet, the corporate desk's rent goes up. March 2020 (the case study below) was a Treasury event that became a corporate bond event in about four days.

**The rule.** The SEC adopted amendments to Rule 17ad-22 on 2023-12-13. Covered clearing agencies must require their members to clear (i) all Treasury repo and reverse repo the member enters into, with exceptions for state and local governments, other clearing organizations, and inter-affiliate trades; and (ii) cash Treasury purchases and sales where the member is an interdealer broker, or between a clearing member and a registered broker-dealer or government securities dealer. Central banks, sovereigns, international financial institutions, and natural persons are exempt. At adoption the SEC chair described the Treasury market as "\$26 trillion" and said that "70 to 80 percent of the Treasury funding market is uncleared, and at least 80 percent of the cash market is uncleared." On 2025-02-25 the SEC extended the compliance dates by a year, to 2026-12-31 for cash and 2027-06-30 for repo. Trade press and an FIA paper report SEC approval of CME Securities Clearing as a second Treasury clearing house in December 2025 and of ICE in early 2026 *(approx.; check the SEC orders)*; FICC remains the incumbent.

"And done-away trades?" Theo asked, reading the Treasury Borrowing Advisory Committee's list of open issues.

"If they've been done away with," said Kaz, "why are we still clearing them?"

"Done-away means you execute with one dealer and clear through another," Theo said. "Like buying a car at one dealership and getting it serviced at a different one. Except the second one is allowed to say it's too busy."

That is the access problem in one line. A mandate is only as good as the customer's ability to reach a clearing member who will take the trade on terms that do not depend on who executed it.

### 22.4.1 Derivation: what multilateral netting buys, and when it stops

Dealer $i$ faces $N - 1$ counterparties, with signed exposure $x_{ij}$ to counterparty $j$. Assume, under $\mathbb{P}$, $x_{ij} = m + \sigma_x z_{ij}$ with $z_{ij}$ i.i.d. standard normal: $m$ is a common directional component (everyone on the same side), and $\sigma_x$ the idiosyncratic scale. Bilaterally, the dealer's gross exposure is $G_i = \sum_{j \ne i}|x_{ij}|$. Novated to a central counterparty, the exposures net to a single position $|\sum_{j \ne i} x_{ij}|$. The **netting factor** is

$$
\phi(N) = \frac{\mathbb{E}\,\big|\sum_{j\ne i} x_{ij}\big|}{\mathbb{E}\,\sum_{j\ne i} |x_{ij}|}.
$$

> **Math, Gently.** *Netting, in two parts.* **Part 1: why netting shrinks like one over a square root.** Picture a dealer that has done one trade with each of its counterparties, and each trade leaves it owed or owing a random amount, as likely to be one as the other. Bilaterally it must hold capital and collateral against every one of those amounts, the gross. Put a central counterparty in the middle and only the sum is left, and the sum cancels the way the drunk's steps did in §22.3.1: the gross grows with the number of counterparties, the sum only with its square root. Tiny number: with four counterparties the netted exposure is about half the gross ($1/\sqrt4$); with twenty-four it is about a fifth. **Part 2: why it stops.** Cancelling needs both signs. Four counterparties owing +2, −1, +1 and −2 have a gross of 6 and a net of zero; four owing +2, +1, +1 and 0 have a gross of 4 and a net of 4, and clearing them saves nothing. A real market sits between the two pictures, and the more one way it leans, the higher the floor under the netting factor. The closed forms come next, and their derivation closes the subsection.

Under the normal model both parts of the box have closed forms. With no common direction ($m = 0$), the netted exposure grows with $\sqrt{N-1}$ and the gross with $N-1$:

$$
\phi(N) = \frac{\sqrt{N-1}\,\sigma_x\sqrt{2/\pi}}{(N-1)\,\sigma_x\sqrt{2/\pi}} = \frac{1}{\sqrt{N-1}}, \qquad \phi(25) = 0.204 .
\tag{22.10}
$$

With 25 symmetric counterparties, clearing shrinks the exposure to a fifth of its gross.

With a common direction ($m \ne 0$), the net grows like $(N-1)|m|$ and the gross like $(N-1)$ times the average size of one exposure, so the netting factor converges to a floor:

$$
\phi(N) \xrightarrow[N\to\infty]{} \phi_\infty = \frac{|m|}{\mathbb{E}|m + \sigma_x Z|},
\qquad
\mathbb{E}|m + \sigma_x Z| = \sigma_x\sqrt{\tfrac{2}{\pi}}\,e^{-m^2/2\sigma_x^2} + m\,\operatorname{erf}\!\Big(\frac{m}{\sigma_x\sqrt 2}\Big).
\tag{22.11}
$$

For $m = \sigma_x$, $\phi_\infty = 0.857$: netting saves only 14%. **Netting stops helping exactly when the market is one-way**, which is the basis-trade case (every leveraged fund long cash Treasuries and short futures against the same dealers) and the March 2020 case (everyone selling). The balance sheet that clearing "creates" in calm markets disappears in the state of the world where it was supposed to help.

A back-of-envelope calibration *(illustrative)*: DTCC reported that its Sponsored Service peaked at \$2.48trn on 2025-06-30 and provided "\$1.14 trillion in balance sheet capacity" *(approx.; DTCC press release)*. Read as a netting factor, that is $\phi \approx 1 - 1.14/2.48 = 0.54$, which in (22.11) corresponds to a directional component about half the idiosyncratic scale, plausible for a market where money funds lend and hedge funds borrow. Figure 22.5 plots the whole family of netting curves.

![Figure 22.5: In a two-way market netting shrinks exposure like 1/√(N−1), to 0.204 of gross at 25 dealers, but any common direction puts a floor under the netting factor (0.558 when the directional component is half the idiosyncratic scale, 0.857 when it equals it), so more clearing members stop helping once the market leans one way. Illustrative: closed forms (22.10) and (22.11); the dashed 0.54 line is the DTCC Sponsored Service reading of this section (DTCC press release, approx.).](assets/figures/ch22_netting_factor.png)

**The mandate as a trade.** Balance sheet saved per dealer per year is $(1 - \phi)\,G\,\kappa_{\text{LR}}\,h$, using the rent of (22.1). The price is initial margin, funded at a spread $f$, plus the annual cost of the default-fund contribution, $\text{DF}$. The mandate pays when

$$
(1 - \phi)\,G\,\kappa_{\text{LR}}\,h \;>\; \text{IM}\cdot f + \text{DF}.
\tag{22.12}
$$

The left side shrinks as the market turns directional; the right side grows, because IM is procyclical. Clearing converts counterparty risk into liquidity risk, and buys back balance sheet with netting, at a price that is lowest in calm markets and highest in stress. *Error-prone spots:* done-with and done-away trades may land in different netting sets; cross-margining between FICC and CME changes IM, not $\phi$; and sponsored repo already nets at the sponsor, which is why DTCC says it clears "nearly half" of the repo the mandate covers, and why the marginal gain from the mandate is smaller than the gross numbers suggest.

#### The Full Derivation: the netting factor with a common direction

*No direction.* The sum of $N-1$ independent $N(0, \sigma_x^2)$ is $N(0, (N-1)\sigma_x^2)$, and $\mathbb{E}|Z| = \sqrt{2/\pi}$ for a standard normal, so the numerator of $\phi$ is $\sqrt{N-1}\,\sigma_x\sqrt{2/\pi}$ and the denominator is $N-1$ copies of $\sigma_x\sqrt{2/\pi}$, which is (22.10).

*With direction.* The numerator is now $\mathbb{E}|(N-1)m + \sqrt{N-1}\,\sigma_x Z|$. Divide by $N-1$: the term $\sigma_x Z/\sqrt{N-1}$ vanishes as $N$ grows, so the numerator is $\approx (N-1)|m|$ for large $N$, while the denominator is exactly $(N-1)\,\mathbb{E}|m + \sigma_x Z|$. Their ratio is the floor in (22.11). The closed form for the denominator is the mean of a folded normal. Write $a = m/\sigma_x$, $\varphi$ for the standard normal density and $\Phi$ for its distribution function. Split the expectation where $m + \sigma_x Z$ changes sign, at $Z = -a$:

$$
\mathbb{E}|m + \sigma_x Z| = \mathbb{E}\big[(m + \sigma_x Z)\mathbf{1}\{Z > -a\}\big] - \mathbb{E}\big[(m + \sigma_x Z)\mathbf{1}\{Z < -a\}\big].
$$

Using $\mathbb{E}[Z\,\mathbf{1}\{Z > -a\}] = \varphi(a)$ and $\mathbb{E}[Z\,\mathbf{1}\{Z < -a\}] = -\varphi(a)$, the two pieces are $m\Phi(a) + \sigma_x\varphi(a)$ and $m\Phi(-a) - \sigma_x\varphi(a)$, so

$$
\mathbb{E}|m + \sigma_x Z| = m\big(2\Phi(a) - 1\big) + 2\sigma_x\varphi(a) = m\,\operatorname{erf}\!\Big(\frac{m}{\sigma_x\sqrt 2}\Big) + \sigma_x\sqrt{\tfrac{2}{\pi}}\,e^{-m^2/2\sigma_x^2},
$$

which is the second half of (22.11). At $m = \sigma_x$ it equals $\sigma_x(0.484 + 0.683) = 1.167\,\sigma_x$, and $\phi_\infty = 1/1.167 = 0.857$.

### 22.4.2 Derivation: dealer capacity as a convex state variable

Duffie, Fleming, Keane, Nelson, Shachar and Van Tassel (2023), *Dealer Capacity and U.S. Treasury Market Functionality* (NY Fed Staff Report 1070), measure dealer balance-sheet utilization $U_t \in [0,1]$ from weekly FR 2004 dealer-level positions (risk-adjusted gross fixed-income positions relative to a sample-record scale). They find that yield volatility explains most of the time variation in Treasury illiquidity, but that when utilization is high, "liquidity is much worse than predicted by yield volatility alone." A stylized hinge, the hockey stick of the box below, captures the shape *(our representation, not the paper's specification)*:

> **Math, Gently.** *A hockey stick.* An ordinary regression draws one straight line through a cloud of points: every extra unit of $x$ adds the same amount of $y$. Some relationships refuse to behave that way. A motorway's travel time barely changes as traffic grows from light to moderate, then climbs once the road nears capacity. Drawn, it is a hockey stick: a flat blade, a rising handle, and a bend at a threshold. A *hinge* writes that shape with one extra term, $(x - x^\ast)^+$, which is zero below the threshold $x^\ast$ and grows one for one above it, so its coefficient is the slope of the handle. Each piece is straight; the bend is what makes the whole curve convex. Tiny number: put the bend at 50% full and let the handle rise by 2 units per 10 points. At 40% the hinge adds nothing, at 60% it adds 2, at 90% it adds 8. One straight line fitted through the 40% and 90% points would say 1.6 units per 10 points everywhere, and be wrong at both ends: too pessimistic in the calm, too optimistic at the edge. Next, dealer balance sheets take the motorway's place.

In symbols, with utilization $U_t$ as the traffic and volatility as the weather:

$$
\text{Illiq}_t = a + b\,\sigma^{y}_t + c\,\big(U_t - U^\ast\big)^+ + \epsilon_t .
\tag{22.13}
$$

Two of their sentences pin down $c$ and $U^\ast$. "When dealer capacity utilization rises from 40% to 80%, Treasury illiquidity is estimated to increase by roughly three standard deviations beyond the level of illiquidity predicted by volatility," so if the kink lies below 40%, $c \times 0.4 = 3$ and $c = 7.5$ standard deviations per unit of utilization. "When dealer capacity utilization is 60%, Treasury illiquidity is predicted to be about two standard deviations above the level predicted by contemporaneous volatility," so $7.5\,(0.6 - U^\ast) = 2$ and $U^\ast = 1/3$, consistent with the assumption. On 2020-03-12 utilization hit its sample record of 96%, where the hinge predicts about 4.7 standard deviations of excess illiquidity. The paper reports the first principal component of Treasury illiquidity at 5.4 standard deviations above its mean that day, volatility included.

For the desk, $U_t$ is a slow state variable, not a trade trigger: it is weekly and published with a lag. Proxy it with FR 2004 positions, FICC volumes, and your own RFQ hit-rate decay, and make the liquidity-cost model of Chapter 19 convex in it. Rent (22.1) is the price of balance sheet when the balance sheet has room. The hinge is the price when it doesn't.

### 22.4.3 Case Study: The March 2020 Dash for Cash

The rent of §22.1 is the price of balance sheet when the balance sheet has room. Twice in this chapter a number has hinted at what happens when it has none: the record utilization of §22.4.2 and the netting floor of §22.4.1. Both belong to one fortnight, and one person on the desk was on a dealer's credit desk for it.

#### Long Scene: the fortnight the invoice was the market

*A war story and a replay. Mags tells it after the close on Tuesday 13 October 2026, and Ines turns the second Friday into a card. Mags's bank is unnamed and its trades, sizes and prices are invented (illustrative); every dated event, figure and quotation is real and sourced.*

It started because Kaz asked a question Kaz considered technical. They had (22.13) on the whiteboard, the hinge with its bend at a third of utilization and its handle climbing at 7.5 standard deviations per unit, and they wanted to know what the handle felt like from the inside. "Does anybody here," Kaz said, "remember being at ninety-six percent?"

"I remember the fax," said Mags. Then she put the 10-Q down, which on this desk is how a story starts. "I was on a bank's credit desk in March 2020. You want the fortnight, you get the fortnight."

**Beat 1: Thursday 12 March 2020, the ETF is the market.** "The first thing you need to understand," Mags said, "is that for about ten days the bonds stopped being the market. The fund was the market. The bonds were rumours of a market." BlackRock's head of iShares, Salim Ramji, put a number on it on the firm's first-quarter call a month later: on 12 March "the iShares investment grade bond ETF LQD traded almost 90,000 times," "while its top five holdings traded an average of 37 times." Mags had not known the number at the time. She had known the feeling. "Clients would call and ask for a bid on a bond, and I'd look at the screen, and the last print was from Tuesday. So you'd look at the ETF instead, which was printing every second, and work backwards."

"I was running an investment-grade book at another dealer," Ines said, without turning round. "We went from principal to agency in about a week. I spent the second half of March as a phone book." (Chapter 2 has that story; she tells it rarely.)

The ETF was printing every second at a price nobody liked. Within days the largest investment-grade and high-yield bond ETFs were quoted more than 5% below the value of the bonds inside them, against no more than 0.1% in January, by the Bank of England's account as reported in the trade press. (Chapter 20 takes the ETF side of this apart, including LQD's 5.08% discount on 19 March.)

What was driving it was not, at first, corporate credit at all. Foreign official holders, leveraged basis traders and mutual funds meeting redemptions were all selling Treasuries in the same two weeks. Kaz saw it immediately in their own notation. "That's $m$," they said. "In (22.11). The common direction. Everybody on the same side." It had gone from small to enormous. On 2020-03-12, the paper on the whiteboard says, dealer utilization reached its sample record of 96%, and Treasury illiquidity hit 5.4 standard deviations above its mean (Duffie et al., 2023). The safest asset in the world became expensive to sell, and because investment-grade bonds are hedged and financed through the same dealer balance sheets, the corporate market dislocated in the days that followed. It was a Treasury event that became a corporate-bond event in about four days.

"I was ten weeks into PJT," Theo said. "We spent that fortnight drawing revolvers. Every client, the whole facility, the same week."

"I know," Mags said. "We were the bank on the other end of some of them. Every one of those draws was balance sheet we didn't have."

**Beat 2: the balance sheet is full.** "Here's the bit nobody puts in the histories," Mags said. "On the Wednesday, the eighteenth, risk sent an email to every trading desk in the building. Value-at-risk limits breached, please reduce positions by close of business. Polite. Numbered. No adjectives." Theo recognized the genre from the cold open's memo. "Every desk in every bank got the same email that week, give or take the font. Reduce to whom? Everybody you'd sell to had the same email." She shrugged. "That's your $m$, Kaz. It isn't a parameter. It's an inbox."

Ines had been listening from the next desk, and she came over with a folder, which meant the war story was about to become a replay. "Here's what the desk's numbers looked like by the end of the next week," she said, and wrote three on the board. Treasury volatility: highest in a decade. Dealer positions in the weekly FR 2004 data: rising, every week, since late February. The desk's own hit rate on its IG bids: collapsing *(all three as the public series and a typical desk log showed them; the desk's hit rate is illustrative)*. "Three slow signals," she said. "Every one of them was visible before the twelfth. Fed into (22.13), they say you're on the handle, not the blade. Rent is a number for the blade."

Kaz looked at the hinge and did the arithmetic out loud: at 96% utilization the stylized hinge predicts about 4.7 standard deviations of excess illiquidity, against a paper that reports 5.4 with volatility included. "So the handle explains most of it."

"The handle *is* it," Ines said. "Now play the hand."

*Odd Lots* recorded the other half of the story six days later, on 26 March, with JPMorgan's Josh Younger walking through how the leveraged Treasury basis trade, long cash bonds and short futures, nearly blew up as the dash for cash overwhelmed it ("How The Crisis Nearly Blew Up One Of The World's Safest Trades," in the Resource Graph). The basis trade is $m$ again: every leveraged fund on the same side of the same dealers.

#### Decision point: Friday 20 March 2020

*A client asks you to bid \$25mm of a ten-year BBB industrial. Dealer utilization is at or near the record. The big investment-grade ETF has been trading several percent below NAV. Your book is already long more than it wants to be. Write three things: what you bid, in what size, and why.*

Kaz's card was a calculation, which was the problem with it. *Rent per (22.1): 126bp a year on a BBB, a week's hold, 2.4bp. Bid screen minus a quarter for the half-spread, minus 2.4bp for the rent. Full size.* "And for the record," Kaz added, "in March 2020 I emailed a friend about LQD at a 5% discount with the subject line 'free money?'" (Chapter 2 has the email.)

Ines's card was the systematic one. *Half size, \$12.5mm. Widen the bid by the convex term, not the rent: the hinge says liquidity is several standard deviations worse than volatility alone predicts, so the bid goes back by points, not basis points. Don't treat the ETF discount as an arbitrage until the balance sheet that would arbitrage it comes back.*

Mags's card said: *I bought ten and told him to come back Monday* (illustrative).

The tools in this chapter grade the three cards, and the grading is not close. Kaz's card priced the blade when the market was on the handle. Rent in (22.1) is the price of balance sheet that exists; on 20 March 2020 the marginal unit of balance sheet did not exist at any rent, and the error in Kaz's bid was not a couple of basis points but an order of magnitude or two.

Kaz pushed back, as Kaz does. "The rent is real. Triple the hurdle and it's still only about seven basis points on a week."

"It's real and it's small," Ines said. "On that Friday a bid that actually traded in that kind of size was two or three points under the last screen *(illustrative)*. Two hundred basis points of price isn't rent. It's the handle. The formula you used is right on the blade and silent on the handle, and the handle is where the money was." Ines's card got the shape right, and so did Mags's, by instinct. Equation (22.2) says a dealer that is already long does not widen symmetrically: it *skews*, because selling saves rent and buying adds it, so its offer stays sharp and its bid goes sullen. A full book in March 2020 was the long dealer of (22.2) with the rent replaced by the hinge, and the right response was a lower bid and a smaller size, not a wider market on both sides. Equation (22.11) explains why nobody could net their way out: with $m$ that large, the netting floor sits near one, and the balance sheet that clearing "creates" in calm markets was exactly the balance sheet that had disappeared.

What none of the cards could see was the calendar. Mags's "come back Monday" sent the client to Monday 23 March 2020, which turned out to be the morning the Federal Reserve announced its corporate credit facilities. "I didn't know that," Mags said. "Nobody knew that. I just knew I didn't have room for twenty-five, and I knew Friday was the worst day of the week to find out what a bond was worth. Time was the only thing I had to sell him, so I sold him the weekend."

Ines graded the reader's card the way she grades everyone's. The trade was never a directional bet. It was a sizing decision: halve block sizes, widen block quotes by the convex term, and stop treating the ETF discount as free money until somebody's balance sheet reappeared to arbitrage it.

**Beat 3: the Fed sets $\kappa_{\text{LR}}$ to zero.** The policy response is easiest to read as a sequence of price changes, in the notation of §22.1. On 2020-03-23 the Federal Reserve established the Secondary Market Corporate Credit Facility (SMCCF), which bought US-listed corporate bond ETFs and individual bonds and "ceased purchasing eligible assets on December 31, 2020." Four days later, on 27 March, the New York Fed signed Terms of Assignment with BlackRock's Financial Markets Advisory unit to manage the facility, with a clause Theo read twice: BlackRock was to "treat BlackRock-sponsored ETFs on the same neutral footing as third-party ETFs," and if the facility's holdings of its own ETFs exceeded its market share, it had to say so. "A buyer of last resort that sells the product it's buying," Theo said. "We'd have called that a related-party transaction and asked for a fairness opinion."

On 2020-04-01 the Fed issued an interim final rule excluding "U.S. Treasury securities and deposits at Federal Reserve Banks" from the holding-company supplementary leverage ratio "until March 31, 2021," which it said would "temporarily decrease tier 1 capital requirements of holding companies by approximately 2 percent in aggregate," because "liquidity conditions in Treasury markets have deteriorated rapidly." The exclusion expired on schedule. In the notation of §22.1, the Fed set $\kappa_{\text{LR}}$ to zero for Treasuries and reserves, collapsing the rent term for exactly the asset where (22.4) said rent was the whole business. Kaz stared at the numerics table of §22.1 for a while. "It's the first row," they said. "They deleted the first row." It was the first time the leverage ratio was used as a market-structure tool, and the November 2025 eSLR rule (§22.5) made a milder version permanent.

"In the cold open you said the Fed paid the invoice," Theo said to Mags.

"It paid it by deleting the first row of your table and buying the ETF," Mags said. "The rest of us paid the part in between: everything that happened from the twelfth to the twenty-third, at whatever price the handle said."

**Beat 4: the warehouse reopens.** The facilities re-opened the warehouse, and the people with balance sheet came back to use it. D. E. Shaw, a quantitative-fundamental manager, says in its own published account that it bought "in excess of \$400 million in CAS and STACR bonds at a significant discount to par" in March and April 2020, from "investors ... put under stress by redemption requests and margin calls." It was on the other side of a forced seller, and its balance sheet was the one that had not been full. The intermediaries who were hedged and positioned to set prices had the opposite of a bad month. Flow Traders, an exchange-traded-product market maker, reported first-quarter net trading income of EUR 495.0m against EUR 63.1m a year earlier, and its release said "No loss days were recorded in the quarter," with its chief trading officer adding that "the ETF mechanism performed as intended." Both accounts are true. A market maker earns the width of a widened spread on record volume precisely because the ETF price moved to where it could clear; the cost fell on whoever needed to sell at a 5% discount. On the dealer side, the quarter's numbers told the same story from both ends of one franchise. On JPMorgan's first-quarter call on 14 April 2020, CFO Jennifer Piepszak said "Fixed income was up 34%, driven by strong client activity," while "the high yield market was effectively closed," and "our bridge book commitments were marked down by \$820 million." A bank could have a strong trading quarter and lose on its underwriting book in the same ninety days, because the trading desk sold balance sheet at the new price and the bridge book had promised it at the old one.

"So what did you do with the ten?" Theo asked.

"Sold them in May," Mags said. "Higher than I paid. Don't write that down as skill." She picked the 10-Q back up. "Write down that I had room for ten and not for twenty-five, and that I knew which."

Ines wrote something else on the board, under the three slow signals: *2020-03-23* and *2020-04-01*. "Structural breaks," she said. "The desk that had a regime table flagged both, and it did not train its post-crisis liquidity model on a period when the central bank was the marginal buyer. That fortnight is in every series you'll ever fit. Know which rows it is."

The clearing mandate that came out of this fortnight, and the dates it has already missed, are tracked in the box below.

> **Trend Watch: Treasury clearing volumes and the compliance path, 2023–2026.** *What changed:* central clearing of Treasuries went from a dealer convenience to a legal requirement with a moving date. *Path:* adopted December 2023 (cash 2025-12-31, repo 2026-06-30) → extended 2025-02-25 (cash 2026-12-31, repo 2027-06-30; margin separation enforced from 2025-09-30) → second and third clearing houses approved, CME in December 2025 and ICE in early 2026 *(approx.)* → no further delay found as of October 2026 *(check before relying on it)*. *How big:* FICC's Government Securities Division cleared a peak of \$11.8trn on 2025-06-30 (prior peak \$11.4trn on 2025-04-09), and Sponsored Service activity hit a record \$2.48trn the same day *(approx.; DTCC press releases)*. Money-market-fund FICC-cleared reverse repo rose by \$132bn (11%) to \$1.3trn in June 2026 *(approx.; OFR data via trade press)*. *What it means for the desk:* repo financing of the bond book is migrating to cleared, margined, netted structures, so your financing cost becomes a function of IM and the netting set, not just a repo rate. Model the compliance dates as structural breaks, and give each one a placebo twin in case it slips again.

### Specification for AI Implementation (netting and capacity)

**The Spec You Hand the Robot.** *Vague version:* "simulate how much clearing saves." *What ROBO built:* a simulation with $N = 2$, where netting saves nothing and ROBO recommended against clearing. *Precise version:* Monte Carlo the netting factor for $N$ counterparties with a common directional component $m$ and idiosyncratic scale $\sigma_x$; return the simulated factor, the no-direction theory $1/\sqrt{N-1}$, and the large-$N$ floor (22.11). Provide a bisection that maps an observed netting factor to the implied $m$; implement (22.12); and calibrate the hinge (22.13) from two published sentences. Seeded; at least 1,000 simulations; reject $N < 2$.

The March 2020 case study ends in a sizing decision, and sizing decisions want numbers on a schedule rather than a seminar. Three questions come back every time a compliance date moves, and it has moved. How much netting survives when everyone is on the same side of the trade? After margin and the default fund, does the mandate still pay a dealer for the balance sheet it frees? And how far up the capacity hinge is the market this week? Each answer is a few lines of arithmetic, and each has a trap. A simulation asked about two dealers returns a netting factor of one and a very persuasive recommendation against clearing, which is the sort of mistake ROBO makes with a straight face. A desk automates the set so the answers can be rerun, with the same seeds, when the date slips again.

The listing has five functions. `folded_normal_mean` is the closed form for $\mathbb{E}|m + sZ|$ in (22.11), the denominator that sets the netting floor. `netting_factor_mc` draws an array of `n_sims` by `n_dealers - 1` exposures, each the common component plus a scaled standard normal, and returns the average absolute net divided by the average gross, matching the definition of $\phi$ in §22.4.1. Alongside it come two benchmarks: the no-direction value $1/\sqrt{N-1}$ and the large-$N$ directional floor. It demands at least two dealers, 1,000 simulations and a positive scale, and it is seeded. `implied_common_component` runs the formula backwards: given an observed netting factor, it bisects on the floor, which rises with $m$, and returns the directional component in units of the idiosyncratic scale. `mandate_net_benefit` is (22.12), left side minus right: balance sheet saved, $(1-\phi)$ times gross times the leverage ratio times the hurdle, less margin times the funding spread plus the default-fund cost. A positive number means the mandate pays. `capacity_hinge` turns two sentences from Duffie et al. into a slope of 7.5 and a kink at one-third, and raises if the kink lands above the lower anchor, because then the two-point arithmetic does not hold.

The assertions check 0.204 at 25 symmetric dealers, the 0.857 floor at $m = \sigma_x$, an implied component between 0.4 and 0.6 from DTCC's sponsored figures, a calm market beating a one-way one, and 4.70 standard deviations of excess illiquidity at 96% utilization.

Use these for scenario analysis of financing costs and sizing, not for a live trading trigger, since utilization is weekly and lagged. `mandate_net_benefit` uses the leverage ratio alone, so it describes Treasuries, where that ratio binds, and not an asset whose risk weight does. The edge case that bites is the inversion. `implied_common_component` inverts the large-$N$ floor, but a real dealer has finitely many counterparties, whose observed factor sits above the floor. Feed it that factor and it overstates how one-sided the market is.

*The full listing is [Listing 22.4 in Appendix F](#code-22-4).*

*Further reading for this section:* SEC press release 2023-247 (clearing mandate); Duffie et al. (2023), NY Fed Staff Report 1070; Duffie (2020), *Still the World's Safe Haven?* (Hutchins Center); Federal Reserve releases of 2020-03-23 (SMCCF) and 2020-04-01 (SLR exclusion).

## 22.5 Dealer Capital: Volcker, the Leverage Ratio, and the Endgame

Three capital rules, three different taxes. Risk-based capital taxes *risk*, the leverage ratio taxes *size*, and the Volcker Rule taxes *time*. Section 22.1 put the first two inside a max. The switching point between them is the equivalent risk weight at which they tie:

$$
\text{RW}^\dagger = \frac{\kappa_{\text{LR}}}{\kappa_{\text{RWA}}}, \qquad \text{leverage binds for } \text{RW} < \text{RW}^\dagger .
\tag{22.14}
$$

For the illustrative G-SIB of §22.1, $\text{RW}^\dagger = 0.05/0.105 = 47.6\%$ before 2026-04-01 and $0.0375/0.105 = 35.7\%$ after. Every asset below the switching point costs the same rent, whatever its risk. The 2026 eSLR rule did two things in this picture: it cut the rent on everything below the line by a quarter, and it moved the line down, so a band of short-dated, high-grade assets became risk-bound and cheaper still.

The Volcker Rule enters differently. Its market-making exemption requires inventory designed not to exceed the reasonably expected near-term demand of clients, customers, and counterparties (RENTD, in the acronym every Volcker compliance officer can say in their sleep). In the language of Chapter 18, that is a constraint $|q| \le \bar\Lambda\,\bar{Q}\,\tau^{\text{hold}}_{\max}$: inventory no larger than expected customer flow (arrival rate times average size) over a permitted horizon. It caps $\tau^{\text{hold}}$ directly, so it binds hardest exactly when customer demand on one side vanishes, in stress, which is the finding of Bao, O'Hara and Zhou (2018), *The Volcker Rule and Corporate Bond Market Making in Times of Stress* (*Journal of Financial Economics*): around rating downgrades, Volcker-affected dealers supplied less liquidity, and other dealers did not fully replace them (see the paper for magnitudes). The 2019 revision ("Volcker 2.0," adopted 2019-10-08, effective 2020-01-01) tiered compliance so that "firms with significant trading activity will have more stringent compliance requirements," while "the universe of trades that are considered prohibited proprietary trading will remain generally the same."

> **[SOURCE EXTRACTION]** *Bolder_Credit_Risk_Modelling p.329:* "The Basel IRB approach ... is a broad, formulaic, one-size-fits-all methodology for the computation of default-risk capital requirements. Its underlying assumption of portfolio invariance ... is nevertheless not particularly well suited for serious risk management and assessment."
>
> **Annotation.** Our analysis: Bolder means this as a criticism, and as risk management it is one. For a trading desk it is a specification. A rule that is "formulaic" (Bolder p.317 calls for "a simplified, formulaic approach to determining appropriate levels of regulatory capital") can be coded, which means its marginal cost can be computed before the trade, which is what (22.1) does. "Portfolio invariance" means the capital for a position does not depend on what else the bank holds, so concentration is free in regulatory terms and diversification earns no credit. Wherever the regulatory function ignores something the economic function cares about, a desk will find the gap; that is Bohn and Stein's "sometimes try to arbitrage" with a formula attached. The modern departure is that the binding constraint for market making is rarely the IRB default charge. It is the leverage ratio or the market-risk charge, and both are even more formulaic.

### 22.5.1 Case Study: The Basel III Endgame Saga, 2023–2026

*Act I: up 16%.* On 2023-07-27 the Federal Reserve, FDIC and OCC proposed standardizing credit, market, operational and CVA risk for banks with \$100bn or more of assets, which they estimated as "an aggregate 16 percent increase in common equity tier 1 capital requirements for affected bank holding companies," "principally affecting the largest and most complex banks" (the widely quoted figure of about 19% for G-SIBs comes from the agencies' impact analysis; *approx.*). For a risk-bound bond book, rent scales with the requirement: the BBB of §22.1 would go from 126bp a year to about 146bp *(illustrative)*, with larger increases for high-yield and less liquid bonds under standardized market-risk charges.

*Act II: up 9%.* On 2024-09-10 Vice Chair for Supervision Barr recommended a re-proposal that "would increase aggregate common equity tier 1 capital requirements for the G-SIBs" by 9%, would "facilitate banks' ability to use internal models" for market risk, largely carve out banks between \$100bn and \$250bn except for recognition of unrealized securities gains and losses (AOCI), and would "not adopt the proposed changes to capital requirements associated with client clearing."

*Interlude: the leverage ratio.* On 2025-11-25 the agencies finalized the eSLR rule, effective 2026-04-01 (optional from 2026-01-01). The holding-company buffer became 50% of the Method 1 G-SIB surcharge instead of a fixed 2%, and depository subsidiaries' buffer was capped at 1% ("no more than four percent" in total). Tier 1 requirements for the affected holding companies fall "by less than two percent" in aggregate, depository subsidiaries see greater reductions, and the stated aim was to reduce disincentives to "lower-risk activities, such as intermediating in U.S. Treasury markets."

*A desk conversation on Thursday 8 October 2026; the numbers are the illustrative ones of §22.1.*

Theo read Acts I and II and the interlude in one sitting, the way he used to read a sponsor's amendment history, and brought Ines the question everybody asks of a regulatory saga. "So which way does it go next? Up or down?"

"I don't know," Ines said, "and neither does anybody who'd tell you. Don't forecast the politics. Ask which inventories are leverage-bound and which are risk-bound, and price each act as a change in $\kappa$." She pulled up the numerics table of §22.1 and put her finger on the first row. "Do this one. The ante."

Theo did it on the back of the cold open's memo, which he had kept. A 2-year on-the-run Treasury is leverage-bound: its risk weight sits far below the switching point of (22.14), so it pays the floor. Before 1 April 2026 the floor was 5%, and at a 12% hurdle that is 60bp a year, 1.15bp for a week, against a half bid-ask of about half a basis point, a breakeven hold of about three days. After the eSLR rule, for an illustrative G-SIB with a 1.5% surcharge, the floor is 3% plus half of 1.5%, or 3.75%: 45bp a year, 0.86bp a week, a breakeven of about four days. "A quarter off the rent," he said. "One more day before the hold eats the spread."

"Now do the BBB."

"Untouched. It's risk-bound; the leverage ratio was never its rent." He turned back to Act I. "And Act I did the opposite. It raised the rent on risk-bound inventory, high yield and long-dated investment grade, from 126 to about 146bp a year on our BBB, and left the Treasuries alone."

"So two acts moved two different inventories in two different directions," Ines said. "A desk that priced balance sheet by asset class saw dealer appetite move each time in the predicted direction. A desk that tracked 'regulation, hawkish or dovish' saw noise, because it was averaging a Treasury with a high-yield bond and calling the average a signal."

"And when volatility moves at the same time?" Kaz asked from the whiteboard.

"Then it's both, and you can't tell them apart without a control group, which is §22.8's problem." She found the line she wanted. The Man research team had seen the 2022 version of the same mechanism when it noted that "the new market environment of higher volatility and quantitative tightening may also have left dealers inclined to commit less of their balance sheets to bond trading" (`Man_Revolutions_in_Credit_Trading_2023 p.3`): capital is the rent, volatility is the risk, and both feed the same quote.

> **Poker Table.** "A two-year Treasury is the ante," Ines said. "You can't sit at this table without one. You hedge with them, you finance with them, your clients want them. The leverage ratio made the ante expensive, so the big stacks stopped playing small pots. The eSLR rule cut the ante by a quarter. It didn't change who's good at poker; it changed how many players can afford to sit down. Watch the number of dealers answering your Treasury RFQs. That's the tell."

> **View From Another Seat.** *The market maker whose $\kappa$ is a coupon.* A non-bank liquidity provider sits outside almost everything in this section. It has no supplementary leverage ratio, no Volcker clock and no G-SIB surcharge, and since the dealer rule was vacated (§22.6 has the dates) it sits outside dealer registration too. That does not make its balance sheet free; it makes the rent explicit. On 2026-09-01 Jane Street issued \$14.6bn of senior secured notes due 2031, 2033 and 2036, at coupons from 7.294% to 8.088%, rated BB by S&P, with the proceeds retiring \$11.1bn of loans and notes and, in the trade-press account, providing "additional trading capital" (The DESK). Where a bank's hurdle is charged on a capital ratio, this kind of firm's marginal balance sheet costs a high-yield coupon, every day, quarter-end or not, with no photograph to dress for. On the credit side, Citadel Securities says in a whitepaper reported on 2026-10-08 that by its own estimates it holds a 14.2% share of US investment-grade "block risk transfer" (The DESK; self-reported, on a denominator it has not published, not independently verified), and it argues publicly for regulation tailored to non-bank market makers. *The book's reading, not either firm's:* a market maker that buys its balance sheet in the bond market faces one hurdle rather than a max of two, so the leverage floor of §22.1, which makes a week of Treasuries cost a bank more than their bid-ask, does not bind it the same way, and Ines's tell, counting the dealers who answer, has to count it too. TRACE cannot help with the count: it identifies reporting firms only by an MPID and carries no bank or non-bank flag.

*Act III: down, modestly.* On 2026-03-19 the agencies released a revised proposal implementing "the final components of the Basel III agreement," under which overall capital would "modestly decrease," and "the market risk aspect of the framework would apply only to banks with significant trading activity," with a separate Fed proposal on G-SIB surcharge measurement. Comments were due 2026-06-18. As of October 2026 it is a proposal, not a final rule *(check before relying on it)*. A law-firm summary of the agencies' own impact estimates for the nine largest holding companies (Debevoise & Plimpton, 2026-03-20) put trading-related CET1 up 9.2% inside an all-in change of −4.8% once the G-SIB-surcharge and stress-test changes are counted: cheaper capital for the bank, dearer capital for its trading book *(secondary source; the agencies' release itself gives no percentages)*. For a desk that is the whole saga in one pair of numbers. The aggregate tells you nothing about the marginal bond.

Act III has a coda in a regulator's own words. On 2026-10-01, looking back at the leverage-ratio recalibration in a speech titled "Modernizing Financial Regulation: Initial Observations from eSLR," Vice Chair for Supervision Michelle Bowman said the old ratio "was imposing a binding constraint on many large bank dealers, curtailing their capacity to provide liquidity." That is (22.1) and (22.4), stated from the podium. The opposing prior is worth hearing in full before anyone on the desk treats it as settled: Anat Admati, who has long argued that banks should fund themselves with far more equity, discussed the post-crisis rules and the design of the endgame with David Beckworth in "Anat Admati on the US Banking System and the Basel III Endgame" (*Macro Musings*, 2024-03-18; both are in the Resource Graph). Ines's rule survives either reading. The desk does not need to know who is right about the politics; it needs to know which row of the table each act touches.

> **Trend Watch: the capital-rule timeline, 2013–2026, and what each step did to dealer inventories.** Volcker final rule (December 2013; *approx.*) and the US eSLR final rule (2014, effective 2018; *approx.*): the warehouse shrinks, inventories fall about three-quarters from the 2007 peak (§22.1). Volcker 2.0 (2019-10-08; effective 2020-01-01): compliance tiering, prohibited activity "generally the same." SLR exclusion (2020-04-01 to 2021-03-31): Treasuries briefly rent-free. Basel III endgame proposal (2023-07-27, +16% CET1), Barr re-proposal outline (2024-09-10, +9% for G-SIBs), eSLR final (2025-11-25, effective 2026-04-01, holding-company Tier 1 down "less than two percent"), endgame re-proposal (2026-03-19, "modestly decrease"). Over the same span, dealer corporate inventories went from roughly \$16bn long in 2017 to net short in 2026 *(approx.; §22.1)*. *What it means for the desk:* the capital timeline is a list of dated changes in $\kappa$; put each one in the regime table with the asset classes it hits.

## 22.6 CDS: From the Index Clearing Mandate to SBSR, Rule 9j-1, and the Dealer Rule That Wasn't

If TRACE is the rule that taxed dealers' information, the swaps rules are the ones that *created* a public information set where there was none. They also explain why credit's most liquid instrument is a cleared, publicly reported index swap.

**The day the index became the hedge.** On 2012-11-28 the CFTC issued its first clearing determination, covering CDX.NA.IG (3Y, 5Y, 7Y, 10Y), CDX.NA.HY (5Y), iTraxx Europe (5Y, 10Y), iTraxx Crossover (5Y) and iTraxx HiVol (5Y), together with major interest-rate swaps. Compliance arrived in three waves: 2013-03-11 for swap dealers and active private funds, 2013-06-10 for other financial entities, and 2013-09-09 for third-party managed accounts and ERISA plans. By the autumn of 2013 the index was a cleared, margined, standardized contract that everyone traded on the same terms, which is most of what it takes to become the hedge. Single-name CDS took a different road. They are security-based swaps under SEC jurisdiction and have never been subject to a clearing mandate; they clear because margin and capital rules make clearing cheaper, which (22.15) below prices.

**The day single names became visible.** For a decade after that, a single-name CDS print was something you heard about. Public dissemination of security-based swap trades under Regulation SBSR began on 2022-02-14 *(approx.; trade press)*, and from then on a desk could count single-name activity instead of guessing at it, which is what makes the stress classifier of §22.6.2 possible. The SEC followed with conduct rules. On 2023-06-07 it adopted Rule 9j-1, an antifraud and anti-manipulation rule for security-based swaps that reaches conduct "in connection with the execution, early termination, assignment or similar transfer of, or extinguishing of any rights or obligations under, a security-based swap," aimed among other things at manufactured credit events. Proposed Rule 10B-1, large position reporting for security-based swaps, was not adopted.

"Manufactured credit event," Kaz read aloud. "Where's the factory?"

"Usually in the indenture," said Mags, "next to the subsidiary that agrees to miss a coupon. Chapter 24 has the tour."

**The question left open: the dealer rule that wasn't.** On 2024-02-06 the SEC adopted Rules 3a5-4 and 3a44-2, further defining when a firm trades "as a part of a regular business" and must register as a dealer, aimed at principal trading firms and some funds that provide liquidity like dealers. The SEC chair said that "Congress did not intend for registration and regulatory requirements to apply to some dealers and not to others." On 2024-11-21 the Northern District of Texas vacated the rules, and in early 2025 the SEC dropped its appeal *(per law-firm client alerts; approx.)*. Non-bank liquidity providers therefore remain outside dealer registration, with their own $\gamma$, their own $k$, and none of the bank capital rules of §22.5, which is a competitive fact as much as a regulatory one (§22.7).

### 22.6.1 Derivation: when clearing a CDS is cheaper than not

> **Math, Gently.** *What "risk-neutral" means, and why CVA uses it.* "Risk-neutral" is not a belief that investors do not mind risk, and it is not a forecast. It is a set of probabilities chosen so that any payoff priced with them costs what the market charges to hedge it, which is why a price computed that way cannot be arbitraged against the hedge. Picture a fire insurer that knows a house in its book burns down once in ten years but charges as if it were once in seven, because fires tend to arrive in bad years when its own capital is thin. The premium implies a probability, and that implied probability, not the actuarial one, is what you would use to price another policy against it. Credit works the same way. Tiny number: a counterparty you believe has a 10% chance of defaulting within a year in the real world, $\mathbb{P}$, may have CDS that price its default as if the chance were 15%, $\mathbb{Q}$, because the market pays extra for losses that arrive in bad states. With \$1mm of exposure and 40% expected recovery, the cost of that counterparty risk at market prices is $0.6 \times \$1\text{mm} \times 15\% = \$90{,}000$, not the \$60,000 your own forecast would say. That is a one-period CVA, and it is the number a clearing house replaces. The one-period construction of the pricing probability is in §6-B.2.2, the full CVA machinery is in Chapter 24, and the inequality is next.

This is the one place in the chapter where the risk-neutral measure $\mathbb{Q}$ appears, because counterparty credit valuation adjustment is a price. Uncleared, a protection buyer bears CVA on the dealer and posts or receives bilateral initial margin under the uncleared-margin rules. Cleared, CVA is replaced by exposure to the clearing house's default fund, and initial margin is set by the CCP over a multi-day margin period of risk (check the CCP's current methodology). Per dollar of notional per year, clearing is cheaper when

$$
\underbrace{(1-R^{\text{cp}})\int_0^T \mathbb{E}^{\mathbb{Q}}\big[\text{EE}(t)\big]\,d\text{PD}^{\text{cp}}(t)}_{\text{CVA, annualized}} \;+\; \text{IM}^{\text{bil}}\,f \;>\; \text{IM}^{\text{CCP}}\,f + \text{DF} + \text{fee},
\tag{22.15}
$$

where $R^{\text{cp}}$ is the counterparty's recovery, $\text{EE}(t)$ the expected positive exposure, $\text{PD}^{\text{cp}}(t)$ the counterparty's cumulative risk-neutral default probability, and $f$ the funding spread on margin. The CCP side wins most for a dealer that holds the index *and* its constituents at one clearing house, because portfolio margining nets the index against the single names and lowers $\text{IM}^{\text{CCP}}$. That, plus the mandate, is why the clearing rates in the Trend Watch below differ by fifteen points. The full CVA machinery lives in Chapter 24; the inequality is all this chapter needs.

### 22.6.2 Case Study: Two Stresses, Two Instruments (Q1 2023 and April 2025)

*Two mornings from the desk's own history, retold for Theo on a slow afternoon in October 2026. The desk's flows and conversations are invented (illustrative); ISDA's and MarketAxess's figures are real and sourced.*

**Monday 13 March 2023, 7:30 a.m.** Silicon Valley Bank had failed on the Friday, and Signature Bank had been closed on the Sunday. Ines's desk came in to a phone that rang with one kind of question, in a dozen variations: what is your offer on protection on *this* bank, and on *that* one, and how about the one that reports on Thursday? By the following week the same question had moved across the Atlantic to Credit Suisse. Almost nobody asked about the index. Ines's entry in the desk log that evening is one line long: *Everybody wants insurance on the house next door. Nobody wants insurance on the street.* ISDA's analysis of DTCC swap-data-repository data, *CDS Market Dynamics: Five Years of Activity and a Record 2025* (2026), later put numbers on the quarter: in the first quarter of 2023, during the regional-bank failures and the Credit Suisse rescue, single-name CDS activity rose 84.8% while index activity rose 4.5%.

**Wednesday 9 April 2025, 8:05 a.m.** A week after the sudden increase in US tariffs, the desk's morning looked like the 2023 one turned inside out. Kaz had been on the desk for three months. The phones wanted CDX, in size, now, and the single-name screens were quiet in the way a room is quiet after a fire alarm. The cash market was thinner still. MarketAxess later reported that the average number of dealer responses to a US high-grade RFQ on its platform "dropped from 13.2 to 6.6 on April 9" and "rebounded to 11.3 within a week," and that high-grade bid-asks widened "by as much as 231%" (MarketAxess, published 2025-07-14). ISDA's numbers for the month are the mirror of 2023: index activity rose 20.9% against its trailing average, while single-name activity *fell* 20.7%. In ISDA's words, "During the 2020 pandemic and following the sudden increase in US tariffs in 2025, index CDS activity increased more than single-name CDS trading."

At 8:20 Kaz brought Ines a hedge. The desk was long a block of a single-B industrial it had bought the afternoon before, and Kaz wanted to buy single-name protection on the same issuer, "because the hedge should match the risk."

"It should," Ines said. "Who's going to sell it to you this morning?" She pulled up the weekly ratio she had kept since the swap prints went public in 2022: index activity divided by single-name activity, built from SBSR and swap-data-repository prints. It had been climbing for a week. "An idiosyncratic stress makes people want protection on specific names, so single-name volume spikes and this number falls. A systematic stress makes them want a macro hedge in the most liquid thing there is, so the index spikes, the single names get abandoned, and this number rises. When the multiple falls, hedge single-name: the single names are liquid and an index basis trade is the risky one. When it rises, hedge with the index, and expect single-name bid-asks to widen. This morning it's rising."

"So I take basis risk on purpose," Kaz said.

"You take basis risk you can trade instead of a perfect hedge nobody will quote you." She bought CDX HY protection sized to the block's spread-duration risk, and accepted that the issuer's own news, if any arrived, would not be hedged. At about 1:20 that afternoon the tariff pause was announced, the index rallied, and the hedge lost money while the bond made more. Kaz spent the evening computing how much of the day's P&L was basis. Ines spent it asleep.

The ratio is a stress-type classifier that did not exist before public reporting. On ISDA's annual numbers the index-to-single-name volume multiple was 15.7× in 2022, 8.5× in 2023, 13.8× in 2025 and 15.1× in the first half of 2026, and the weekly version moved the same way within days in both stresses. Both regimes are now in the training data, because the regulators made the data public.

> **Trend Watch: CDS activity and clearing, 2021–H1 2026.** *What changed:* index CDS set records while single names stayed small. *How big (ISDA, 2026; DTCC SDR data):* global CDS activity reached "a record \$41.8 trillion in 2025, surpassing the previous peak of \$38.7 trillion in 2022"; index CDS accounted for 93.3% of 2025 activity (a record \$39.0trn), while single-name activity peaked at \$3.3trn in 2023 and eased to \$2.8trn in 2025. The first half of 2026 reached \$27.4trn, up 27.8% year on year. "In 2025, 78.1% of index credit derivatives traded notional reported in the US was cleared, along with 63.1% of single-name CDS traded notional." Breadth is thin: "only 20 of 751 reference entities" averaged 10 or more trades a day in the fourth quarter of 2025. ICE Clear Credit reported record USD single-name clearing of \$2.57trn in 2025, up from \$2.17trn, and more than \$28trn of USD index *(approx.; ICE press release, 2026-01-06)*; ICE Clear Europe had ceased CDS clearing in October 2023. *What it means for the desk:* the hedge you can count on in stress is the index; the single-name hedge exists for about twenty names a day. Size single-name hedging strategies to that breadth, not to the notional headline.

#### A rule is a price, on the short leg

*Dov Adler's pod at Vantress Capital Management, its prime broker and its lender are fictional composites; Kestrel Roofing and Halvorsen Packaging are fictional issuers; positions, prices, fees, utilization and P&L are illustrative. The research findings, the rules and their dates are real and sourced.*

Every rule in this chapter so far has been a price on the dealer's side of a trade. A pod on a multi-manager platform across town pays them too, and it pays twice.

Tuesday 20 October 2026, 7:40 a.m. Wen Zhao makes the call she makes every morning, to the prime broker's securities-lending desk, for availability and fee on every bond Dov's book is short. Most mornings it takes four minutes and produces a column of numbers nobody reads. This morning she reads one row back twice. Halvorsen Packaging's 7.25% notes due 2029, the short leg of Pair Book entry PB-01: fee 300bp, unchanged. The agent lender reports 85% of its Halvorsen inventory on loan. And the lender has recalled a tenth of the pod's borrow, \$3.5mm of the \$35mm, for return by Thursday.

Wen keeps every borrowed bond's history as a time series, and she calls it the weather. Halvorsen's weather is easy to read from the bottom of the sheet up. The fee was 50bp from April, when Dov put the pair on. In mid-September, 61% of the lender's inventory was on loan and nobody had recalled anything (Chapter 8-D). In the week of the lender call the fee was reset to 300 (Chapter 1-B). Since then the share on loan has crept from the sixties to 85% as other pods found the same short (Chapter 11), and this morning the lender started taking bonds back.

At 8:15 she takes it to Dov, who asks the question a former dealer would ask. "What does the tape say? Who else is short?"

"There is no tape," Wen says. In equities there are short-interest reports; in corporate bonds there is no public short-interest series at all. The SEC's securities-lending rule, Rule 10c-1a, which would have had loans reported to FINRA, was delayed by an SEC order of 3 December 2025 to 28 September 2028, after the Fifth Circuit remanded it in August 2025; whether it will cover corporate-bond loans in a form a pod could use, the book has not been able to confirm. Regulation SHO's locate requirement, the rule that makes a short seller show it can borrow before it sells, reads "any equity security." "The rules were written for stocks," Wen says. "For bonds we have the lender's word and the fee."

Dov turns to Marcus Oyelaran, the platform's risk manager, who has walked over because Wen copied him, as she always does on a recall. Marcus's overnight x-ray of the pod's book is good at what the book is long without meaning to be. It is blind to crowding in a short. "I can see your beta and your sector and your rates," Marcus says. "I can't see how many other books on this floor or any other are short the same Halvorsen bond. The only number that knows is the fee."

The fee knows a lot. The one careful study of the corporate-bond lending market, Asquith, Au, Covert and Pathak (2013), using one large custodian's loans from 2004 to 2007, found the cost of borrowing a bond flat near 30bp until about 70% of a lender's inventory was on loan, then rising by more than 10bp for each further 10%. At 85%, the slope alone would say something like 45bp. Halvorsen costs 300. The same study found 173bp in the 30 days before a bankruptcy filing and 245bp after. "We're paying more than the average bankrupt bond paid in their sample," Wen says. "The lender isn't pricing utilization. It's pricing a vote." Holders who want a say in a consent or an exchange want their bonds back exactly when the short most wants to keep them, and the recall right is the lender's to use.

> **The Pair.** *Pair Book PB-01, stressed on the borrow.* **Legs.** Long \$60mm Kestrel 6% 2030 at about 96; short \$35mm Halvorsen 7.25% 2029 at about 78, borrowed through the prime broker from one asset manager's agent lender, with a small CDX HY sale for the beta the September trim left behind. **What the hedge removes.** Market-value DTS matched at inception takes out high-yield beta and most of the housing-cycle sector factor; two fixed-rate legs of similar duration take out most of the rates. **What idio remains.** Halvorsen's 2027 revolver and its sponsor against Kestrel's covenant room, which is the view. **What leaks.** The fee, which is now a position of its own: 300bp against a slope that would say about 45. The recall right the lender keeps: loans are on demand and roll nightly, and a tenth went this morning. And the mismatch between a bond short and the rules written for equity shorts: no locate rule, no tape, no public short interest, so the crowd is visible only through its price. **What it costs to carry and to short.** Carry: \$3.6mm a year of Kestrel coupon against about \$2.54mm of Halvorsen coupon owed to the lender. Borrow: 300bp on about \$27.3mm of market value, roughly \$0.82mm a year, where April's 50bp would have cost about \$0.14mm. Financing the long net of the rebate on the short's cash collateral: about \$0.5mm. Net, the pair that carried roughly flat in April now costs about a quarter of a million dollars a year before trading costs, and an exit pays two half-spreads, about a quarter-point on Kestrel and three-quarters on Halvorsen in a lender-call week, roughly \$0.41mm, or \$0.83mm a year over a six-month horizon. For scale: at 35bp, \$15mm of borrowed bonds cost \$52.5k a year, 52.5bp on a \$10mm long; at 300bp the same \$15mm costs \$450k.

*The fee is 300bp and the lender has recalled a tenth. Write three things before reading on: what you do with the short, what you do with the long, and the date by which the thesis has to have paid.*

The pod argues about it the way pods do, quickly and in front of the risk manager. Wen's first instinct is the cheapest-looking one: return the recalled \$3.5mm and re-borrow it from a second lender. She has already asked. The second lender has bonds, at an indicative 450bp, and its own recall right. "So we'd swap one lender who's about to want a vote for another one who is," she says, and talks herself out of it.

Marcus's instinct is the platform's: the pod's \$35mm was exactly 20% of the lender's \$175mm of inventory, the platform's limit for a borrow from a single lender, and its rule is that a borrow at the limit needs a written recall plan. "This is the recall plan," he says. "You're executing it."

Dov's answer is the one the ledger records. Cover the recalled tenth in the market rather than chase it at 450. Do not replace it with CDX: an index short would take out beta the pair no longer has much of and leave the idio unhedged, so the pair would quietly become a long Kestrel position with a hat on, the failure Chapter 11 warned about. Leave the long alone; Kestrel has not done anything wrong. And move the thesis date. In April the pair carried flat, so time was free and the thesis could take until the 2027 revolver. At 300bp, time costs about a quarter of a million dollars a year plus the risk of the next recall. "If the fee is 300," Dov says, "the thesis has to pay 300 a year faster than I thought." He writes a new date in the ledger, the end of the first quarter of 2027, and a line under it: if Halvorsen's lenders have not organized by then, the trade is a carry trade he did not mean to own.

Grade your card against the three questions. A card that kept the full short at any fee treated the borrow as plumbing, which is what Dov did in April. A card that switched to the index kept the beta hedge and gave up the view. A card that cut the pair entirely may be right, but it was reacting to the fee and not to the thesis, and nobody can know which yet. The only card that is plainly wrong is the one that never mentioned a date.

Marcus has one more thing before he goes, and it is not about Halvorsen. In its December 2025 Quarterly Review the BIS laid out what happened to a much bigger relative-value trade built on someone else's balance sheet. Hedge funds' swap-spread trade, long Treasuries against swaps, grew from about \$281bn in the first quarter of 2024 to a peak of about \$707bn in March 2025, then fell 11% to \$631bn by June as, in the BIS's words, "traders were caught wrong-footed" in April 2025. The book's reading: it was a trade whose economics lived on dealer balance sheets, and the eSLR recalibration of §22.5 repriced exactly that balance sheet. "Same lesson, bigger font," Marcus says.

Dov puts the phone down on the lending desk for the second time that morning. "Every trade we do is priced by the dealer's rules twice," he says. "Once on the long, when they finance it, and once on the short, when they lend it. In April I priced the first one."

The full borrow mechanics, from locate to rebate to recall, are in Chapter 8-D (§8D.2).

## 22.7 The Regulated Venue: Consolidation, Tapes, and the Non-Bank Question

*The morning meeting, Theo's regime calendar and the desk's remarks are fictional; the deal terms, filing dates, tape dates, court dates and capital factors are real and sourced where they appear.*

The last force is the venue itself, and on this desk it arrives the way most regulation arrives: as an agenda item at the morning meeting, read aloud by the most junior person in the room.

Monday 19 October 2026, 7:10 a.m. Since the Calloway afternoon three weeks earlier, Theo has owned the part of the regime table that has not happened yet. Ines calls it the calendar. Kaz calls it "the future rows," with the mild distaste of a statistician for data that does not exist yet. Every Monday, before the overnight P&L, Theo reads the calendar out loud, and every Monday Ines asks each row the one question she thinks a venue rule can answer: after this date, who answers the RFQ, and what do they see before they answer?

The first row this morning is the biggest. On 29 July 2026 ICE agreed to buy MarketAxess for \$167 a share in cash, about \$6.0bn of equity value, announced on 2026-07-30 with closing expected in the first half of 2027 (MarketAxess 8-K, Exhibit 99.1). Theo has added two dates since the summer. The merger proxy, filed on 18 September, set MarketAxess's shareholder vote for a special meeting on 29 October. And a later 8-K says the companies withdrew their antitrust filing on 25 September and refiled it on the 29th "to provide the DOJ with additional time," which moves the end of the waiting period to 29 October as well (MarketAxess DEFM14A and 8-K). Ten days out, both dates are still pending, and the closing is a range with an outside date of 29 July 2027 that can extend twice, to 2028.

"What changes for us?" Ines asks.

Kaz has read the exhibit, because Kaz always reads the exhibit. ICE's own description of the deal joins MarketAxess's "trading data and analytics" to ICE's pricing, reference data and index businesses. "So the venue that sees our RFQs and the vendor that marks our book at four o'clock become one company," Kaz says. "Same data, two products. I'd like to know which way it flows before I train on it." Theo's point is smaller and duller, and it matters more this morning. In the same 30 July release, MarketAxess said it was "suspending its practice of issuing monthly volumes press releases." The volume pack in §22.2 lost its denominator's definition in August; one of the public numerators a desk used to check its own share against went quiet in July. "Two rows, then," Ines says. "Neither one says the market got better or worse. They say the comparison changed, which is all a regime table ever says."

The second row is Europe, and its date cell is empty. ESMA selected Ediphy (fairCT) as the first EU bond consolidated tape provider on 2025-07-03, for a five-year term under ESMA's direct supervision once authorised. ESMA's update of 2026-04-01 said that "authorisation processes for both CTPs are currently ongoing," and Theo has found no authorisation or go-live date since. Kaz would like to delete the row until it has a date. Ines will not let him. "You spent February 2024 learning what an approved rule with no effective date does to a model," she says, meaning the one-minute rule of §22.2.3. "Leave it in. When the date arrives you'll want to know how long everyone waited for it, and what they did while they waited."

The third row is the United Kingdom, and it has two dates, which Theo reads as two different treatments. The UK's new bond transparency regime took effect on 2025-12-01 *(approx.; FCA announcement)*: that one changed what gets published and how fast. The UK bond consolidated tape, run by Etrading Software, went live on 22 June 2026 with 98% contributor coverage by notional at launch (The DESK): that one put the prints from venues and over-the-counter reports into a single feed. A sterling corporate RFQ answered in July was answered by dealers who could see more of the market's recent history in one place than they could in May. Whether they priced it differently is a question for §22.8, and the desk does not trade enough sterling credit to answer it.

The fourth row has no date at all, and Theo has labeled it *open*. The non-bank market makers of §22.5 (the second View From Another Seat there, with Citadel Securities' self-reported block share) are arguing publicly for rules of their own, a debate that the vacatur of the dealer rule (§22.6) left unresolved. "That's the one that could matter most," Ines says, "and it's the one we can least put a date on." Each of these changes who answers an RFQ and what they see before answering, and so each belongs in the regime table.

Mags has been listening with the expression she uses for vendor demonstrations. "You've read me four rows about where bonds trade," she says. "The biggest flow on this desk this quarter won't come from a venue. It'll come from a customer whose regulator has a calendar, and the calendar has a date on it that every one of them knows." Then she tells Theo which row he forgot, and it belongs to a different seat.

> **View From Another Seat.** *The insurer, whose regulator publishes the date.* From a life insurer's investment office, the dealer's quarter-end photograph in (22.1) is somebody else's problem. The insurer's own rent is a lookup table keyed to a rating, and its regulator has just reprinted the table. Under the CLO factors the NAIC adopted in June and July 2026, effective for risk-based capital as of 31 December 2026, the pre-tax charge on a CLO tranche climbs gently from 0.04% at Aaa to 3.28% at Baa3, and then jumps to 15.13% at Ba1; §21.8 has the thickness surcharge and the comparison with corporate bonds. In the margin: \$10mm of a Baa3 tranche ties up about \$328k of pre-tax required capital; one notch lower, the same \$10mm ties up about \$1.51mm, four and a half times as much for one letter from a rating agency. Two other dates sit on the same calendar. Since 13 August 2026 the NAIC's securities office has described its discretion over designations assigned through the filing-exemption process as "operational," so a rating is no longer a passport the regulator cannot inspect (Chapter 17 tells that story). And in Europe the Solvency II amendments of Directive (EU) 2025/2 apply from 30 January 2027. The industry argued about the shape in public. In the NAIC comment record the life insurers' trade association, the ACLI, warned of a "cliff" at exactly those boundaries, A2 to A3 and Baa3 to Ba1, and asked for disclosure only in 2026, while Athene backed the actuaries' model with refinement in 2027. *The book's reading, not any insurer's:* the insurer never saw Calloway's three-eighths; what it sees is a year-end and a notch. Its question is when to leave a bucket it is about to be charged nearly five times as much to stay in. Selling early and in pieces costs time and a little spread; selling into the date costs whatever the bid has learned about the date. For the dealer, a customer whose regulator publishes the date is a customer whose hand is face up.

Theo adds the row: *2026-12-31, NAIC CLO C-1 factors, treatment: insurers' below-IG CLO holdings; what to watch: dealer inventory and bid depth in BB CLO tranches in the six weeks before.* Ines reads it over his shoulder and adds nothing, which on this desk is praise. The asset managers who run money for insurers say the same thing from the other side of the table, in their own documents.

> **[SOURCE EXTRACTION]** *Blackstone_Systematic_Credit p.2:* "dynamically adjust portfolios to minimize capital charges for insurance clients under regulatory frameworks like Solvency II"
>
> **Annotation.** Our analysis: this is the buy-side mirror of (22.1). An insurer pays rent on its holdings too, through Solvency II in Europe and NAIC risk-based capital in the US, and its rent jumps at rating boundaries. Nuveen's framework makes the same point, describing the need to "limit exposure to certain sectors due to regulatory capital requirements" (`Nuveen_Multi_Asset_Credit_Quant_Framework p.5`). The flow consequence is predictable selling: fallen angels sold by insurers, CCC buckets cured by CLOs, and sector limits enforced at quarter-ends. A dealer that knows the customer's capital function knows when the customer is a forced seller, which in Ines's vocabulary is the most valuable thing at the table: an opponent who must fold. Where the modern desk departs from the asset manager's framing is in the direction of the optimization: Blackstone minimizes the client's charge, and the market maker prices the trades that minimization forces.

Mags has one more row, and she admits it is not a venue, a dealer or a customer. "Sometimes the issuer has a regulator too," she says, "and then the regulator writes the revenue line." Her example is Thames Water, whose regulated operating company sits inside a whole-business securitisation with senior Class A debt and junior Class B debt. On 19 December 2024 Ofwat's final determination allowed bills to rise 35% against the 53% the company had asked for. On 18 February 2025 the High Court sanctioned an interim Part 26A restructuring plan over the Class B creditors' vote, 84.5% of which was against: the judge found that the relevant alternative was special administration and that Class B would be out of the money in it, so the class was crammed down, and on 17 March the Court of Appeal dismissed the appeals. In October 2026 the second plan was still open, and a press report that month put Class B's agreed recovery at about 5.9%, in post-restructuring equity. "No rent formula in this chapter has that row in it," Mags says. "A price-review determination is a rule with a date, and the bond knew the date." Theo does not add it to the calendar, because the desk does not trade sterling utilities. He writes it on a sticky note instead, which on this desk is where rows go to wait for a reason.

## 22.8 The Regulatory Event-Study Engine

Every section of this chapter ended in a date. This section turns the dates into a tool that answers the second half of the cold-open question: *did the rule change the data, or did something else?*

### 22.8.1 Derivation: difference-in-differences around an effective date

> **Math, Gently.** *The two-by-two table.* Draw two lines on one chart. The first is the average half-spread of the bonds a rule touches; the second is the average of similar bonds it leaves alone. Before the effective date they wander up and down together, a roughly constant distance apart, because the same weather (rates, a bank failure, a quarter-end) rains on both. After the date, if the rule did anything, the first line steps away from the gap it used to keep. Difference-in-differences measures that step and nothing else. In the margin: over the month after a rule, the treated bonds' half-spread fell 3bp and the untouched bonds' fell 2bp. A before-and-after on the treated bonds alone hands the rule all 3bp. The table hands the market the 2bp that fell on everyone and the rule only the 1bp that fell on the treated bonds alone: $(-3) - (-2) = -1$. Four averages, two subtractions; that is the whole machine. The weak point is a bet nobody can observe directly: that without the rule the two lines would have stayed parallel. Everything careful about the method, from pre-trend charts to placebo dates, exists to test that bet indirectly. The fixed effects in the model are bookkeeping that lets the same subtraction run on hundreds of bonds and days at once; §7-B.1 has the within transformation behind them, and the model is next.

Written as a model, the table becomes a regression. Let $y_{it}$ be an outcome for bond $i$ on business day $t$ (an effective half-spread in bp, a TRACE volume, a dealer hit rate), $D_i \in \{0,1\}$ mark the bonds the rule touches (treated), and $\text{Post}_t = \mathbf{1}\{t \ge t_0\}$ mark the dates on or after the effective date $t_0$. The two-way fixed-effects model is

$$
y_{it} = \alpha_i + \mu_t + \delta\,D_i\,\text{Post}_t + \epsilon_{it},
\tag{22.16}
$$

with $\alpha_i$ a bond effect (its permanent liquidity level), $\mu_t$ a date effect (everything that hits all bonds at once: rates, the VIX, quarter-end, the healing after the March 2023 bank stress), and $\delta$ the effect of the rule. The estimator is the margin's subtraction, done on bond-level changes $d_i = \bar y_i^{\text{post}} - \bar y_i^{\text{pre}}$:

$$
\hat\delta = \bar d_{\text{T}} - \bar d_{\text{C}} = \delta + \big(\bar{\Delta\epsilon}_{\text{T}} - \bar{\Delta\epsilon}_{\text{C}}\big),
\tag{22.17}
$$

the average change of the treated bonds minus the average change of the controls, equal to the rule's effect plus a noise term that the parallel-trends bet says averages to zero.

#### The Full Derivation: two-way fixed effects around a date

Average (22.16) for bond $i$ over the pre-window and over the post-window, and subtract. The bond effect $\alpha_i$ is the same in both windows, so it cancels within the bond. In a balanced panel every bond sees the same dates, so the date effects average to the same $\bar\mu^{\text{post}} - \bar\mu^{\text{pre}}$ for every bond. What is left is

$$
d_i = \big(\bar\mu^{\text{post}} - \bar\mu^{\text{pre}}\big) + \delta\,D_i + \Delta\epsilon_i, \qquad \Delta\epsilon_i = \bar\epsilon_i^{\text{post}} - \bar\epsilon_i^{\text{pre}}.
$$

Average $d_i$ over the treated bonds and over the controls. The market term $\bar\mu^{\text{post}} - \bar\mu^{\text{pre}}$ appears in both averages and cancels in their difference; $\delta$ appears only in the treated average. That is (22.17). It is unbiased if the treated and control groups would have moved in parallel without the rule, $\mathbb{E}[\Delta\epsilon_i \mid D_i = 1] = \mathbb{E}[\Delta\epsilon_i \mid D_i = 0]$. That parallel-trends assumption is the whole identification, and it is testable only indirectly: with pre-trend checks and with **placebo dates**, fake effective dates on which $\hat\delta$ should be zero. Errors are correlated within a bond over time, so the standard error comes from a cluster bootstrap that resamples whole bonds.

A before-and-after comparison with no control group is the regulatory version of reporting raw returns. It attributes $\bar\mu^{\text{post}} - \bar\mu^{\text{pre}}$, the market, to the rule. In the margin's numbers, it is the 2bp of weather booked as rule. IDO or it didn't happen.

*Worked example.* The PT modifier went live on 2023-05-15. Treated bonds: issues that appear often in portfolio trades (index-eligible, recently issued, high PT share in 2022). Controls: matched bonds by rating, maturity, and size that rarely appear in PTs. Outcome: TRACE-measured effective half-spread. The obvious confounder is that market-wide liquidity was healing after the March 2023 stress, which pushes every bond's measured costs down at the same time; the control group absorbs it, and a naive before-and-after on the treated bonds alone would report the healing as a rule effect. Placebos: two pre-event dates, plus the best placebo in the book, 2025-12-04, when the one-minute rule was abandoned without ever having taken effect. The long scene of §22.2.3 is how the desk earned that date: a rule that was approved, priced, feared and never switched on is a day on which nothing in the reporting changed, as close to a known zero as a real date ever gets.

*The desk's run and every number in it are fictional (illustrative); FINRA's indicator and its dates are real (§22.2).*

The first live question Kaz put to the method was the one rule in this chapter that a back office noticed before a front office did. Thursday 15 October 2026, after the close, Kaz turned the screen toward Theo with the satisfaction of someone who has found good news in a footnote.

"FINRA's affiliate indicator went voluntary on 31 August," Kaz said. "Treated: bonds where affiliate pairs were a big share of 2025 trades. Controls: matched bonds where they were rare. Outcome: the share of each bond's volume that goes dealer to dealer, the hot-potato share. Treated bonds fell 4.1 points relative to controls *(illustrative)*, the bootstrap standard error is 0.9, and two placebo dates in June and July give nothing. Dealers are passing bonds around less. Liquidity improved."

Theo read it twice. "Which bonds were treated?"

"The high-affiliate ones. I said."

"Treated by what? The rule didn't touch a bond. It touched a report. A bank buys from a customer in one broker-dealer and hands the bond to its affiliate, and before September that second leg printed as a dealer-to-dealer trade. Now the firm can flag it and TRACE suppresses it. Nobody passed the bond around any less. They stopped printing the pass." Volume had fallen for a definition, not for liquidity.

"And your controls?" Ines asked from the next desk, without looking up.

Kaz checked, and the answer took a minute to arrive. The switch is flipped by a reporting firm, not by a bond, and the same large dealers that flipped it on day one also report trades in the control bonds. The controls had lost their affiliate legs too, only fewer of them. "So the treated group got the definition change," Ines said, "and the control group got a smaller dose of the same definition change. Your 4.1 points is the gap between two doses of bookkeeping."

Kaz deleted nothing, which Theo noticed and filed away. They moved the run into a folder called *definitions*, the word an operations analyst at another bank had used for her tab in §22.2, and added a line to the regime table's notes column: *2026-08-31: changes anything counted from prints; no clean control exists at the bond level.* "I had a control group," Kaz said, mostly to the screen. "It had taken the same medicine."

### Specification for AI Implementation (event-study engine)

**The Spec You Hand the Robot.** *Vague version:* "measure the effect of the new rule." *What ROBO built:* the mean of $y$ after the date minus the mean before it, on the treated bonds only, which correctly attributed the 2023 recovery in bank stocks to a FINRA reporting modifier. *Precise version:* implement (22.17) on a panel `[date (datetime64, New York calendar), bond_id (str), treated (bool), y (float)]`; the window is in business days relative to $t_0$, with the event day counted as post; use only bonds observed on both sides; return the 2×2 table of means, $\hat\delta$, and a cluster-bootstrap standard error (resample bonds within the treated and control groups, seeded); and provide `placebo(panel, dates, **kw)`. Reject panels with fewer than two treated or control bonds. Validate on a synthetic panel with a known effect and a concurrent market-wide shock.

Every desk has sat through the meeting where someone shows a chart of spreads tightening after a rule took effect and concludes that the rule worked. The chart is usually accurate and the conclusion usually belongs to the market. The only defense is a control group, applied the same way each time, across a dozen rules and three liquidity measures, by people who would like to go home. That is a job for a function. Once the study is a function, the skeptic on the risk committee can rerun it on dates of her own choosing, and the placebo check costs one more line instead of one more week.

The listing has two functions and a synthetic test bed. `event_study_did` takes a long panel with `date`, `bond_id`, a treated flag and an outcome `y`, plus the effective date and a window in business days. It counts each row's business-day distance from the event with `numpy`'s `busday_count`, keeps rows inside the window, and marks the event day itself as post. It then averages the outcome within each bond on each side of the date, so the bond's permanent liquidity level cancels, and drops any bond not observed on both sides. The estimate is the mean change of the treated bonds minus the mean change of the controls, which is (22.17). The standard error comes from a seeded bootstrap that resamples the bond-level changes within the treated and control groups. The function refuses fewer than two bonds in either group, and returns the 2×2 table of means, the estimate, the standard error and the group counts. `placebo` simply calls it on a list of fake dates and returns the estimates as a series; all should sit near zero.

The test bed builds 80 bonds with large fixed effects, a drifting market factor that falls 3bp on the real date, and a true 2bp rule effect on the treated half. The assertions show that the naive treated before-and-after change is negative while the estimate lands on +2bp inside its own error band, and that two fake dates give nothing.

The function answers any effective-date question that has a plausible control group, and it has no way of knowing when the group is not plausible. Kaz's affiliate-indicator run is the case of controls touched by the same rule; a treated group picked because its bonds were already trending is the other way to fool it. The quieter trap sits in the placebo window. Nothing stops a fake date whose post window reaches the real event, and the "placebo" then returns part of the true effect, which is why the listing narrows the window to forty days for its fake dates. The business-day count has no holiday calendar either, so a window that spans a market holiday holds one fewer trading day than the code believes.

*The full listing is [Listing 22.5 in Appendix F](#code-22-5).*

## 22.9 Desk Debrief

- **A dealer sells balance sheet, time, and information, and every rule is a tax or a subsidy on one of them.** The desk does not comply with rules; it prices them, and it dates them.
- **Rent is $h\cdot\max(\kappa_{\text{RWA}}\text{RW}, \kappa_{\text{LR}})\cdot\tau^{\text{hold}}$.** A flat dealer widens both sides; a long dealer skews. For a 2-year Treasury, rent is the whole spread (breakeven hold of three to four days); for a BBB, it is a rounding error (about a month). That inequality explains why Treasuries went agency first.
- **A reporting delay is an option the block dealer holds**, worth $2\lambda Q/T_u$ of spread per unit of delay. The fifteen-minute, \$5mm/\$1mm equilibrium has survived attacks from both sides since 2019. It is priced into every block you quote.
- **Behind "5MM+" is a Pareto tail** with $\alpha \approx 1.67$ for IG and $1.33$ for HY, so block-size variance does not exist. Use the historic file, medians, and rating-specific tails; never average at the cap.
- **Square roots and floors.** T+1 cut the volatility component of margin by between $1-\sqrt{2/3}$ and $1-\sqrt{1/2}$, and DTCC's 23–29% landed inside the bracket. Netting shrinks exposure by $1/\sqrt{N-1}$ in a two-way market and by almost nothing in a one-way market, which is the only market in which you need it.
- **Dealer capacity is a hinge:** rent in calm markets, convex in stress, with the kink near a third of utilization. Make the liquidity model's dealer term a slow state variable, not a constant.
- **Capital rules are dated changes in $\kappa$.** For each one, ask which inventories are leverage-bound and which are risk-bound; the 2023–2026 endgame saga moved them in opposite directions.
- **Every effective date is a structural break, and every abandoned rule is a placebo.** No control group, no effect: IDO or it didn't happen.

### The Spec You Hand the Robot

*Vague version:* "make the models regulation-aware." *What ROBO built:* a dummy variable for every page of the Federal Register since 2002, a model with more regulatory features than bonds, and a perfect in-sample fit. *Precise version (prompt-ready):*

> Build `reg_cost_engine.py` (numpy and pandas only; every random draw seeded). (1) `regulatory_carry_bp(kappa_rwa, risk_weight, kappa_lr, hurdle, holding_days)`: $10^4\,h\,\max(\kappa_{\text{RWA}}\text{RW}, \kappa_{\text{LR}})\,\text{days}/365$, decimals only, reject ratios outside [0, 1] and non-positive days; `breakeven_holding_days` per (22.4); `carry_table` over a positions frame using $|$notional$|$. (2) `block_half_spread` per (22.6) with the positive-part guard and an optional inferred size; `pareto_alpha_from_imputed_mean` and `censored_impact` per (22.7), with $\alpha > 1$ enforced. (3) `margin_ratio` per (22.8) on the horizon including close-out; `fail_cost_annual` per (22.9). (4) `netting_factor_mc` returning simulated, theoretical ($1/\sqrt{N-1}$) and directional-floor (22.11) factors; `mandate_net_benefit` per (22.12); `capacity_hinge` calibrated from two published sentences. (5) `REGIME_DATES` as the single dated table, and `trace_regime_flags`, which rejects naive timestamps, compares New York calendar dates, keeps `one_minute_rule` False forever, and flags capped sizes by rating bucket. (6) `event_study_did` per (22.17) with a cluster bootstrap by bond, and `placebo`. Acceptance tests: the asserts in this chapter, unchanged, including: Treasury rent 1.15bp a week at 5% and 12%; margin ratios 0.7071 and 0.8165 bracketing DTCC's 0.71 and 0.77; netting factor within 2% of 0.204 at $N = 25$; a synthetic +2bp rule effect recovered within four standard errors despite a −3bp concurrent market move; placebo estimates below 0.25bp. Do not invent bond identifiers; use descriptive `bond_id` strings.

### Exercises

1. **The ante.** A 5-year on-the-run Treasury trades 0.5bp of price wide. With $h = 12\%$, compute the breakeven holding period at $\kappa_{\text{LR}} = 5\%$ and at $3.75\%$. A dealer's average holding period in Treasuries is two days. Is it a principal market maker or an agent with extra steps? *(Answer sketch: $\tau^\ast = 0.25/60$ years, about 1.5 days, and 0.25/45 years, about 2.0 days; the eSLR rule moved this dealer from losing money on the hold to breaking even.)*
2. **Pooling at the cap.** Using (22.6) and (22.7) with the IG parameters of §22.2, find the block size $Q$ at which the cap neither helps nor hurts the dealer, and show that for $C < Q < mC$ the cap *widens* the competitive block spread. Explain, as Ines would, why small-block dealers and large-block dealers lobby differently on the caps.
3. **Negative specials.** Using (22.9), show that a short seller who can either fail or borrow the bond in repo at the special rate $r^{\text{sp}}$ is indifferent when $r^{\text{sp}} = \min(0,\ r^{\text{ref}} - 3\%)$. Compute the floor for $r^{\text{ref}} = 0.25\%$ and $r^{\text{ref}} = 4\%$, and reconcile the first number with Veronesi's account of May 2009.
4. **When does netting give up?** For $m = 0.5\sigma_x$, compute $\phi(N)$ by simulation for $N \in \{5, 10, 25, 100\}$ and find the $N$ at which it is within 5% of the floor (22.11). What does that say about the benefit of adding more clearing members in a one-way market?
5. **Kaz's event date.** Kaz proposes studying the Treasury clearing mandate with an event date of 2025-12-31, "because that's the date in the release." Explain what is wrong with this, design a treated and control set and a placebo set for the actual cash compliance date (2026-12-31, or whatever it has become by the time you read this), and say what result would make you distrust your own estimate.
6. **ROBO maximizes transparency.** ROBO is told to "maximize transparency" and sets $\Delta = 0$ and $C = \infty$. Using (22.6), describe the block market it builds, which trades survive, and which protocols (Chapters 19 and 20) absorb the rest. Then cite the empirical result from Asquith, Covert and Pathak that would most worry ROBO's sponsor.

### Deep-Dive Resource Graph

**Podcasts**
- **"T+Lunchtime: Settlement, Musk, Hwang"** (*Money Stuff: The Podcast*, Matt Levine and Katie Greifeld, 2024-05-31). Published three days after the 28 May 2024 switch to T+1; the first topic on the page is the move to T+1 stock settlement. One topic of four, so an informal companion to §22.3.3 rather than a primer. https://omny.fm/shows/money-stuff-the-podcast/t-lunchtime-settlement-musk-hwang
- **"Preparing for US Treasury Clearing: Industry Readiness and the Done-Away Framework"** (*The SIFMA Podcast*, SIFMA COO Joe Seidel with Rob Toomey, Bill Thum and Steve Byron, 2026-07-31). The trade association's own walk-through of the SEC clearing rule ahead of the December 2026 cash-clearing deadline: purpose and market impact, operational readiness, SIFMA's new done-away documentation and broker-dealer capital considerations. The industry-side primary for §22.4. https://www.sifma.org/news/podcasts/preparing-for-us-treasury-clearing-industry-readiness-and-the-done-away-framework
- **"Samim Ghamami on How to Reform the Treasury Market"** (*Macro Musings with David Beckworth*, 2024-08-19). The basics of the Treasury market and the case for the reform path that became the clearing mandate, from an SEC economist who speaks for himself, two years before the deadline: the "why" behind §22.4 (netting, margin and the price of a very large market). https://macromusings.libsyn.com/samim-ghamami-on-how-to-reform-the-treasury-market
- **"How The Crisis Nearly Blew Up One Of The World's Safest Trades"** (*Odd Lots*, guest Josh Younger of JPMorgan, 2020-03-26). Recorded mid-crisis: popular trades arbing Treasuries against Treasury futures started to fail as the flight to cash overwhelmed the market, the basis-trade half of the dash for cash in §22.4.3. https://omny.fm/shows/odd-lots/how-the-crisis-nearly-blew-up-one-of-the-world-s-s
- **"Anat Admati on the US Banking System and the Basel III Endgame"** (*Macro Musings with David Beckworth*, 2024-03-18). The opposing prior: Admati (Stanford; *The Bankers' New Clothes*) on the effectiveness of post-crisis rules and the design and impact of the Basel III endgame. Read it against Bowman's speech below for the two sides of §22.5.1. https://macromusings.libsyn.com/anat-admati-on-the-us-banking-system-and-the-basel-iii-endgame

**Practitioner Writing**
- **"Remarks at the 2026 U.S. Treasury Market Conference"** (SEC Commissioner Mark T. Uyeda, 2026-09-22). As fetched for the dossier (check the SEC page before printing numbers): cleared Treasury volume has risen sharply (FICC daily cleared volume reported about 165% above the pre-proposal level), two more clearing agencies were approved, and the 31 Dec 2026 (cash) and 30 Jun 2027 (repo) compliance dates "will not be extended." A dated regulator statement for the §22.4 timeline. https://www.sec.gov/newsroom/speeches-statements/uyeda-remarks-2026-u-s-treasury-market-conference-092226
- **"Modernizing Financial Regulation: Initial Observations from eSLR"** (Federal Reserve Vice Chair for Supervision Michelle W. Bowman, Atlantic Council CEO & Senior Management Summit, 2026-10-01). States that the eSLR "was imposing a binding constraint on many large bank dealers, curtailing their capacity to provide liquidity," that the Fed temporarily eased it in spring 2020, and that the Board has since recalibrated it: the regulator's own account of the dealer-capital link in §22.5. https://www.federalreserve.gov/newsevents/speech/bowman20261001a.htm
- **"How Efficiency Enhances Resilience in the Financial System"** (ISDA *derivatiViews*, Scott O'Malia, 2026-10-13). Argues that cross-margining (CME-FICC) cuts Treasury margin but could raise SA-CCR capital unless the capital framework recognises the offset, "restricting balance sheet capacity" for client clearing: the derivatives industry's version of the margin-versus-capital trade-off in §22.4-§22.5. https://www.isda.org/2026/10/13/how-efficiency-enhances-resilience-in-the-financial-system/
- **"Overnight Corporate Bond Trading"** (The Microstructure Exchange webinar, Farshid Abdi with Marco Rossi and Botao Wu, 2026-09-15). Trades between 6:30 p.m. and 8:00 a.m. are not disseminated on TRACE until the next morning; per the abstract they are larger, move prices more persistently and concentrate among large dealers: a current fact about the dissemination clock of §22.2; the season page links the recording and the paper. https://microstructure.exchange/season
- FINRA Regulatory Notice 25-17 (2025-12-04; one-minute rule dropped, allocation reports, caps restated): https://www.finra.org/rules-guidance/notices/25-17
- FINRA Regulatory Notice 19-12 (block-size dissemination pilot): https://www.finra.org/rules-guidance/notices/19-12
- FINRA Regulatory Notice 22-12 (PT modifier): https://www.finra.org/rules-guidance/notices/22-12
- FINRA Regulatory Notice 22-17 (one-minute proposal): https://www.finra.org/rules-guidance/notices/22-17
- FINRA Regulatory Notice 26-16 (affiliate indicator): https://www.finra.org/rules-guidance/notices/26-16
- FINRA rule filing SR-FINRA-2024-004: https://www.finra.org/rules-guidance/rule-filings/sr-finra-2024-004
- SEC press release 2023-247 (Treasury clearing mandate): https://www.sec.gov/news/press-release/2023-247
- SEC press release 2023-29 (T+1 adoption): https://www.sec.gov/news/press-release/2023-29
- SEC press release 2024-14 (dealer rule): https://www.sec.gov/news/press-release/2024-14
- SEC press release 2025-43 (Treasury clearing compliance extension, 2025-02-25) *(title only)*.
- Federal Reserve, Basel III endgame proposal (2023-07-27): https://www.federalreserve.gov/newsevents/pressreleases/bcreg20230727a.htm
- Federal Reserve, Barr speech on the capital re-proposal (2024-09-10): https://www.federalreserve.gov/newsevents/speech/barr20240910a.htm
- Federal Reserve, eSLR final rule (2025-11-25): https://www.federalreserve.gov/newsevents/pressreleases/bcreg20251125b.htm
- Federal Reserve, Basel III re-proposal (2026-03-19): https://www.federalreserve.gov/newsevents/pressreleases/bcreg20260319a.htm
- Federal Reserve, SLR temporary exclusion (2020-04-01): https://www.federalreserve.gov/newsevents/pressreleases/bcreg20200401a.htm
- Federal Reserve, Volcker Rule revisions (2019-10-08): https://www.federalreserve.gov/newsevents/pressreleases/bcreg20191008a.htm
- Federal Reserve, Secondary Market Corporate Credit Facility: https://www.federalreserve.gov/monetarypolicy/smccf.htm
- CFTC press release 6429-12 (first swap clearing determination, 2012-11-28): https://www.cftc.gov/PressRoom/PressReleases/6429-12
- ISDA research portal (including *CDS Market Dynamics: Five Years of Activity and a Record 2025*): https://www.isda.org/category/research/
- ESMA, consolidated tape providers: https://www.esma.europa.eu/esmas-activities/markets-and-infrastructure/consolidated-tape-providers
- MarketAxess 8-K Exhibit 99.1 (ICE transaction announcement, 2026): https://www.sec.gov/Archives/edgar/data/1278021/000119312526324933/d159148dex991.htm
- DTCC, SIFMA and ICI, T+1 after-action report (2024) *(title only)*; FINRA TRACE FactBook 2025 *(title only)*. Manufactured credit events (§22.6): see the Deep-Dive Resource Graph of Chapter 24.

**Academic Papers**
- Asquith, Covert and Pathak (2013, rev. 2019), *The Effects of Mandatory Transparency in Financial Market Design: Evidence from the Corporate Bond Market*, NBER w19417: https://www.nber.org/papers/w19417
- Duffie, Fleming, Keane, Nelson, Shachar and Van Tassel (2023), *Dealer Capacity and U.S. Treasury Market Functionality*, NY Fed Staff Report 1070: https://www.newyorkfed.org/research/staff_reports/sr1070
- *Title only:* Bessembinder, Maxwell and Venkataraman (2006), *Market Transparency, Liquidity Externalities, and Institutional Trading Costs in Corporate Bonds*; Edwards, Harris and Piwowar (2007), *Corporate Bond Market Transaction Costs and Transparency*; Goldstein, Hotchkiss and Sirri (2007), *Transparency and Liquidity: A Controlled Experiment on Corporate Bonds*; Bao, O'Hara and Zhou (2018), *The Volcker Rule and Corporate Bond Market Making in Times of Stress*; Duffie (2012), *Market Making Under the Proposed Volcker Rule*; Duffie (2020), *Still the World's Safe Haven?*; Avellaneda and Stoikov (2008), *High-Frequency Trading in a Limit Order Book*; Kyle (1985), *Continuous Auctions and Insider Trading*.

**Data & Code**
- NY Fed primary dealer statistics (FR 2004): https://www.newyorkfed.org/markets/counterparties/primary-dealers-statistics
- FINRA Rule 6730 (TRACE reporting): https://www.finra.org/rules-guidance/rulebooks/finra-rules/6730
- FINRA Rule 6750 (TRACE dissemination, including Treasuries): https://www.finra.org/rules-guidance/rulebooks/finra-rules/6750
- SEC EDGAR: https://www.sec.gov/edgar
- FRED (Federal Reserve Economic Data): https://fred.stlouisfed.org/
- This chapter's `REGIME_DATES` table, which Chapters 19, 20, 24 and Appendix C import as the single dated source for regulatory structural breaks.

<!-- STATUS: COMPLETE -->
