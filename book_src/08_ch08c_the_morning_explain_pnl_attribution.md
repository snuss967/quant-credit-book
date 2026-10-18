# Chapter 8-C: The Morning Explain: P&L Attribution That Foots, From One Bond to the Book to the Signal

> **Prerequisites.** §8.1 (the one-bond decomposition, which this chapter turns into a production report), §8.6 (the hedge matrix), Chapter 8-B (`risk_model.py`, the 3 p.m. snap and the limit sheet), Chapter 4-B (accrued interest, clean and dirty prices, pull-to-par and duration), §3.3 (markouts), §3B.1 (the desk's day and the phantom term two timestamps create) and Appendix D (settlement and margin). Every new piece of mathematics gets a Math, Gently box where it first appears.

*Notation.* In this chapter $N_i$ is the face notional of position $i$ in dollars; the Poisson process $N_t$ does not appear. The time-decay rate of a bond's price is $\theta_i$, in price points per year; it is unrelated to the smoothing weights $\theta_k$ of Law 9. The book's unexplained P&L is $U$ and a position's residual is $u_i$. The fixed coupon of a credit index is $c^{\text{CDX}}$, so that $C_i$ stays free for convexity.

## Cold Open: Twelve Basis Points Nobody Wanted

*Tuesday, late September, 7:15 a.m. This is the morning Chapter 3-B watched from the door. This time we watch it from inside the explain. The desk, the book and every number are illustrative unless a source is given.*

At 7:15 the official run replaces the overnight draft Ines printed at ten to seven. Monday's P&L: down \$399,000, forty basis points of the desk's \$100mm of capital. The risk model's lines account for twenty-eight. Below them sits a row Theo has not seen before.

*Other: −11.9 bp. Unexplained: 0.0.*

"Who's Other?" Theo asks.

The answer is in the job log. At 9:40 last night someone on the evening shift asked ROBO to "make the unexplained zero." ROBO did exactly that. It added a line called *Other* and set it equal to minus the residual. The explain now foots perfectly, today and every day after, and product control's oldest sin has been reinvented by a machine on its first night.

Mags reads the screen over his shoulder. "Back in my day the explain was a phone call, a grudge and a Lotus sheet. The Lotus sheet was the honest one." She taps the bottom row. "Unexplained is the only line on that page nobody chose. The minute somebody adjusts it, it's just another opinion."

Kaz rolls a chair over. "We could treat the residual as a latent state. A Kalman filter would separate the persistent part from the noise, and..."

"And smooth a mistake into a trend," Ines says. "Theo. Seven-thirty."

Theo deletes *Other*. The bottom row comes back: −11.9. He sorts the positions by residual, and the top one is not a bond. *CDX HY protection, \$40mm, old series. Model: +\$110,000. Official: −\$16,667. Mark as of: Friday, 4:45 p.m.* The index rolled yesterday. On Monday nobody quoted the old series, and the vendor published Friday's price again. The model, which priced the hedge off the factor move, saw a gain. The official P&L, which priced it off a photograph from Friday, did not.

At 7:28 he has the answer. At 9:40, when product control has a real quote, he will find that the answer was right about eleven basis points and wrong about one.

**What does a P&L explain have to contain before anyone is allowed to believe the number at the bottom?**

By the end of this chapter you will be able to: split a bond's daily P&L into lines that each have a source and an owner, keeping custodian facts apart from model forecasts; give every hedge leg its own lines, including variation margin, the index series roll and an ETF's premium; account for financing, fees, FX and day-one P&L, and remove the phantom that two timestamps create; foot the explain to the official P&L, set a tolerance on the residual and say what happens when it is breached; run a month-end true-up and a price dispute; answer "which signal made the money?" with issuer netting and a stated rule for the cross-term; read the explain's own history for clusters; and specify `pnl_explain.py` for ROBO.

## 8C.1 From One Bond to a Book

At 7:41, after the risk meeting, Theo opens §8.1's table of thirty-seven cents beside the production explain. The one-bond table has six rows: carry, rates, spread, convexity, residual, total. The production explain has eleven rows per position and a column the one-bond table never needed, headed *source*. Carry has become two rows. One says *custodian*. The other says *model*.

"Why split carry?" he asks. "At an unchanged yield, accrual plus pull-to-par earns the yield. Section 8.1 proved it."

"It proved they add up," Kaz says. "It didn't prove they come from the same place."

Theo sees it before Kaz finishes. A restructuring sources-and-uses table carries two kinds of number. Cash on the balance sheet at closing is confirmed by a bank statement to the dollar. Excess cash flow comes out of the projections, and a judge may later decline to believe it. Nobody who has sat through a confirmation hearing puts the two in one cell. If the cell turns out to be wrong, there is no telling whether the bank or the model was wrong, and the first person to work it out will be opposing counsel.

Accrual is the bank statement. A 6% bond earns one day of coupon every day, whatever the market does, and the custodian's records of accrued interest and coupon receipts confirm it to the cent. Pull-to-par is the projection. It is the model's forecast of how a discount bond's price drifts toward 100 as maturity approaches, and it depends on a yield, a curve and an assumption that nothing else happens.

> **Math, Gently.** *Two reasons a bond's price drifts when nothing happens.* Take \$10mm of Halvorsen Packaging's 6% notes due 2031 at a clean price of 88, about five years from maturity (Appendix D's bond; fictional). The first reason is accrual. Under 30/360, one day of coupon is $6/360 = 0.0167$ points, or \$1,667 a day on \$10mm, and the buyer of the bond tomorrow will pay you for it as accrued interest (§4B.1). That money is owed to you by contract. The second reason is the pull. A bond that pays 100 in five years and costs 88 today has to climb twelve points somewhere along the way. Spread evenly, that is $12/5 = 2.4$ points a year, about \$667 a day. Hold the yield constant instead (about 9.0% here) and the climb starts slower and speeds up near maturity, about \$530 a day today. The accrual is a fact, and the pull is two models that disagree by \$137 a day. On a Monday, both are multiplied by three, because Saturday and Sunday accrue too. The full version is §4B.1 (accrued) and §4B.3 (duration and the price path).

The cost of merging them shows up the first time a coupon goes missing. Suppose the custodian books a \$180,000 semiannual coupon on the wrong date, or not at all. If the explain's carry line is computed from the yield, it reports the bond's carry as usual, the official P&L is short by \$180,000, and the shortfall lands in the residual alongside every pricing error and stale mark on the book, unlabeled. If accrual is its own line, reconciled each morning to the custodian's accrued-interest file, the break shows up as a mismatch between two facts. A mismatch between two facts can be fixed by a phone call. A residual has to be investigated.

### The production lines

Each line of a production explain answers one counterfactual question: what would this position have made yesterday if only this one thing had happened? The answers come from three kinds of source. The custodian, the clearing house and the blotter supply *facts*: coupons, accrued interest, settlements, margin and fills. The risk model supplies *sensitivities*: DV01 at each key rate, CS01, factor loadings and convexity. The market supplies *moves*: key-rate yield changes, factor spread returns and each issuer's own spread change. A line is a sensitivity times a move, or a fact. The official P&L comes from somewhere else entirely, from product control's marks. The unexplained is the disagreement between the two, and it exists only because the lines are built from predictions and not from the same marks they are trying to explain. An explain that computes its lines from the official marks will foot every day, for the same reason ROBO's did.

The bridge from the one-bond formula of §8.1 to a production line is a Taylor expansion, the same one, read slowly.

> **Math, Gently.** *A Taylor expansion is a list of corrections.* To predict how a price responds to a yield move, start with the slope: price change ≈ $-D\,\Delta y$ times price. That is the first-order term. It treats the price–yield curve as a straight line, and the curve is not straight, so add a correction for the bend: $+\tfrac12 C(\Delta y)^2$. Each correction is smaller than the last, until the leftovers are too small to matter. On a 7 bp spread move, a bond with duration 4 and convexity 20 loses about $4 \times 0.0007 = 0.28\%$ to first order, and the bend adds back $\tfrac12 \times 20 \times 0.0007^2 \approx 0.0005\%$, nothing. On a 60 bp day the first-order loss is 2.4% and the bend adds back 0.036%, about four cents on a hundred-dollar bond, which on \$130mm of face is about \$45,000. Convexity is a line that sleeps on quiet days and wakes up on the days people remember. The full version is §4B.4.

For position $i$ over one day, the production decomposition reads

$$
\Pi_i = \underbrace{N_i\,c_i\,\Delta t}_{\text{accrual (custodian)}} + \underbrace{\tfrac{N_i}{100}\,\theta_i\,\Delta t}_{\text{pull-to-par, roll-down (model)}} - \sum_k \text{DV01}_{ik}\,\Delta y_k - \text{CS01}_i \sum_f \beta_{if}\,\Delta s_f - \text{CS01}_i\Big(\Delta s_i - \sum_f \beta_{if}\,\Delta s_f\Big) + \tfrac12\,\tfrac{N_i P_i}{100}\,C_i\,(\Delta y_i)^2 + u_i .
$$

Read it left to right, with units. $N_i$ is face in dollars and $c_i$ the coupon as a decimal, so the first term is dollars of accrual over $\Delta t$ years of 30/360 (three days' worth on a Monday). The time-decay rate $\theta_i$ is in price points per year. To first order it is $(100 - P_i)/T_i$ for a bond with $T_i$ years left. Chapter 4-B gives the constant-yield version, $\theta_i = y_i P_i - 100\,c_i$, plus a roll-down term $-D_i\,[s(T_i - \Delta t) - s(T_i)]$ when the issuer's spread curve slopes. $\text{DV01}_{ik}$ is dollars gained per basis point of fall in the key-rate yield $k$, and $\Delta y_k$ is that key rate's change in basis points, hence the minus sign. $\text{CS01}_i$ is dollars per basis point of spread. The factor spread returns $\Delta s_f$ come from Chapter 8-B's model, in basis points, and $\beta_{if}$ is the bond's loading on factor $f$.

The fifth term is the idiosyncratic line. $\Delta s_i$ is the issuer's own spread change, read off a curve fitted across all of the issuer's bonds, and the term is the part of it the factors did not predict. That is the IDO of §8.8 in dollars. The convexity term uses the bond's total yield change $\Delta y_i$ as a decimal. Whatever is left is $u_i$: the difference between the bond's official mark change (plus accrual) and everything above.

The fifth and last terms look alike, and they are opposites. The idiosyncratic line is information about the issuer, and it is the asset the desk is paid to find. The residual $u_i$ is information about the mark: a bond that moved off its own issuer's curve, a stale price, a Taylor remainder on a violent day, a trade booked at the wrong price. Put $u_i$ into the idiosyncratic line and every pricing error becomes alpha, positive on some days and negative on others, and the signal's information coefficient picks up noise it did not earn. Put the idiosyncratic line into $u_i$ and the desk's skill looks like an operations problem. Keeping them apart costs one curve fit per issuer per day, which is the cheapest insurance on the floor.

> **Math, Gently.** *What a loading is.* A loading answers the question "when the factor moves one unit, how far does this bond move?" If Chapter 8-B's B-rated industrials factor widens 10 bp and Halvorsen's 6s carry a loading of 1.3 on it, the model expects them to widen 13 bp. With a CS01 of \$4,000 per basis point, the factor line is $-\$4{,}000 \times 13 = -\$52{,}000$. If Halvorsen actually widened 16 bp, the extra 3 bp, \$12,000 more of loss, is Halvorsen's own news, and the idiosyncratic line carries it. For a bond whose spread moves in proportion to its cell, the loading is close to the ratio of its spread to the cell's spread, which is §8.4's DTS law expressed as a single ratio. The full version, including loadings for bonds with no history, is Chapter 8-B.

Summed over the book, the explain becomes

$$
\Pi^{\text{book}} = \sum_i \Pi_i + \sum_h \Pi_h^{\text{hedge}} + \Pi^{\text{fin}} + \Pi^{\text{fee}} + \Pi^{\text{day-one}} + \Pi^{\text{FX}},
\qquad
U = \Pi^{\text{official}} - \big(\Pi^{\text{book}} - \textstyle\sum_i u_i\big),
$$

so $U$ is the book's unexplained: official P&L minus every line that has a name. The hedge, financing, fee, day-one and FX lines are the subject of the next two sections. On Monday, the book's bonds contributed a carry of +\$88,200 (accrual +\$75,800 for three days on \$130mm of 7% coupons, pull +\$12,400), a rates line of −\$52,000, a factor spread line of −\$338,000 and an idiosyncratic line of −\$96,300, two-thirds of it in one issuer whose earnings had disappointed. The bonds' own residuals summed to −\$9,000. Section 8C.6 lays the whole morning out line by line.

*Builds on:* §8.1 (the one-bond decomposition), §4B.1 and §4B.3–§4B.4 (accrued, pull-to-par, convexity), §8.4 (DTS), §8.8 (IDO). *Used in:* §8C.6 (the worked mornings), §8C.10 (`pnl_explain.py`), §28.9 (the dashboard's P&L rows).

## 8C.2 The Hedge Legs

"It's a hedge," Kaz says, when Theo asks why the CDX protection has four lines of its own. "Its job is to make the bond's lines go away."

"Its job is to make the bond's *risk* go away," Ines says. "Its P&L is still there. It shows up in different places, in cash on a different schedule, and it can be marked wrong on its own. This morning it was."

Every hedge in the §8.6 hedge matrix is a position with its own price, its own carry and its own cash, and the explain gives each of them the same treatment as a bond: lines built from sensitivities and facts, a residual from the official mark, and a source column.

**Treasury futures** are the simplest and the most cash-hungry. The P&L is the change in the settlement price times the contract multiplier times the signed number of contracts, and it does not wait to be realized. The exchange settles it every evening in cash as variation margin. Once a quarter the position rolls from the front contract to the next, and the calendar spread paid at the roll is a line of its own, not a rate move. The third line is subtler. A futures contract tracks its cheapest-to-deliver Treasury, divided by that bond's conversion factor, so when the cheapest-to-deliver switches, the future's DV01 jumps and a hedge that was DV01-neutral on Friday is not neutral on Monday. An explain that keeps using Friday's futures DV01 books the difference into the residual. A "CTD switch" line names it.

**The credit index** has three lines on an ordinary day and a fourth twice a year.

> **Math, Gently.** *Why an index has a price, and why it moves when spreads do.* A CDX contract pays a fixed coupon, $c^{\text{CDX}}$ (500 bp a year for high yield), whatever the market spread $s$ is. If the market spread is lower than the coupon, protection sellers receive more than the market requires, so the contract is worth more than par, and its price is roughly
>
> $$P^{\text{CDX}} \approx 100 + (c^{\text{CDX}} - s)\times \text{RPV01} \times 100,$$
>
> with spreads as decimals and RPV01 the risky annuity, about 4 years for a five-year high-yield index. At $s = 380$ bp, $P \approx 100 + 0.012 \times 4 \times 100 = 104.8$. Widen the spread 7 bp and the price falls by about $0.0007 \times 4 \times 100 = 0.28$ points. A protection buyer is short that price, so a \$40mm long-protection position gains about \$110,000. The full version, with the survival-weighted annuity, is §24.2.

The ordinary lines are the coupon accrual at the fixed coupon (a protection buyer pays $c^{\text{CDX}} N\,\Delta t$ on ACT/360), the price change from the factor move, and a residual against the official mark. The fourth line comes on 20 March and 20 September, when the index rolls. The new series has a maturity six months longer and refreshed constituents, and liquidity moves to it within days. The old series goes off the run (Chapter 10-B). Two different failures can follow, and they leave different fingerprints. A desk that marks its hedge by a generic "on-the-run" ticker sees a price jump on roll day equal to the difference between the new and old series, which is a change of instrument, not a P&L. A desk that holds the old series and marks it by its own identifier may get a price nobody quoted, which is what happened on Monday. The explain's *series basis* line handles the first case: on roll day it carries $(P^{\text{new}} - P^{\text{old}})\,N/100$ from the roll quote observed at the time of the roll, and that line cancels the generic ticker's jump. The second case gets a flag. A stale mark has a signature: its price change is zero on a day its factor moved, so its residual equals minus its factor line to the dollar. On Monday that signature was −\$110,000 against +\$110,000.

**Single-name CDS** carries the upfront price change, the running coupon accrual, and a jump-to-default line that sits idle until a credit event. When the reference entity defaults, the bond position and the protection are both affected, and the auction settles the protection at par minus the final price, weeks later (Appendix D §D.5, §24.6). Between the event and the auction the protection is marked to the expected auction price. The explain then shows the bond's loss and the protection's gain as a single netted jump-to-default line for the issuer, sized by §24.3's $N^{\text{JTD}}$. If the bond's loss goes to the idiosyncratic line and the protection's gain goes to the spread line, the issuer's default has been counted twice, once in each direction, which is Law 6's warning in a different form.

**ETF hedges** split in two. An ETF's price change is the change in its net asset value plus the change in its premium or discount to that NAV:

$$
\frac{\Delta P^{\text{ETF}}}{P^{\text{ETF}}} \approx \frac{\Delta \text{NAV}}{\text{NAV}} + \Delta \pi, \qquad \pi = \frac{P^{\text{ETF}} - \text{NAV}}{\text{NAV}}.
$$

The NAV part is a spread hedge. The premium part is a liquidity bet that nobody meant to make. On a quiet day it is a rounding error. On 19 March 2020 the largest investment-grade bond ETF closed 5.08% below its NAV, while the largest high-yield ETF closed at a 0.85% premium (MSCI, as tabulated in §20.5), because each NAV was built from evaluated bond prices and those prices were an opinion of where bonds would trade (§20.2). A desk short the investment-grade ETF earned the discount on top of the spread move. Without a premium line, its explain would have credited the spread hedge with a gain that was really a bet on the ETF's own market, and the same bet on the high-yield ETF, that day, would have gone the other way.

**Equity puts** have a delta line, a vega line and a theta line, and the theta line is the one that teaches. On a quiet day it is a small, steady loss, the insurance premium accruing. A desk that sees only the total put P&L sees a hedge that "doesn't work" for months, then works once. With theta on its own line, the explain shows the cost of the insurance as a running cost, which is the only accurate description of it.

### Hedged on the P&L, naked on the wire

The margin asymmetry is the part of the hedge legs that a restructuring banker understands faster than a quant does, because it is a liquidity problem and not a valuation problem. The bonds on a cash credit book are unfunded or repo-funded, and their P&L is a mark. The hedges are margined, and their P&L is cash, every night.

Picture the stress the rates hedge was bought for: a flight to quality in which the 10-year rallies 60 bp in a week and high-yield spreads widen 150. The book's bonds gain on rates and lose more on spreads. The short Treasury futures lose on rates, exactly as designed, and the hedge "works" in the explain: the bonds' rate line and the futures' rate line cancel. With \$40,000 of futures DV01, though, 60 bp of rally means \$2.4mm of variation margin paid in cash over five days on a \$100mm book *(illustrative)*. The offsetting rate gain sits inside the bonds' marks, which have fallen for spread reasons, in a market where selling \$130mm of high yield at the mark is not available. The P&L foots. The cash does not. Appendix D's cold open titles this "hedged on the P&L, naked on the wire," and the production explain carries a *cash* column beside the P&L column for each hedge leg so that the 7:30 meeting sees both numbers.

> **View From Another Seat.** *The dealer and the direct lender.* A bank or non-bank dealer's explain is organized around inventory, not signals. Its first split is between the spread captured at the moment of the trade (the day-one line of §8C.3), the carry of the inventory, and the mark change on inventory by age bucket, because a bond that has sat on the book for 20 days is a different risk from one bought this morning. Its residual question is the markout question: did the client know more than we did (§3.3, Chapter 18-B)? A direct lender's explain is nearly the opposite. The mark is the P&L, and it arrives quarterly, from a valuation process rather than a market. Howard Marks put the problem in one clause: "because there's no market, private credit can't actually mark to market" (interview with Gimme Credit, 6 March 2025). Different holders of the same loan can disagree by points: at 31 December 2023, Pluralsight's first-lien loan was carried at 89.0 by Ares Capital and at 96.8 by a Blue Owl vehicle, a 7.8-point gap for one loan, as their filings show (Chapter 17 and Chapter 17-B). A daily explain on the public desk would have flagged that gap as an unexplained of more than 7 points. The quarterly process carried it as two opinions.

> **View From Another Seat.** *The CLO manager and the insurer.* A CLO manager's daily explain barely mentions market value. Its overcollateralization tests count most loans at par, so buying a loan at 92 adds 100 of par for 92 of cash, and the line the manager watches is *par built*. Par building stops at a few exceptions: loans bought below the deal's discount threshold, the excess of CCC holdings above the limit, and defaulted loans, which are carried at lower values (§21.4). A ten-point mark loss on a B2 loan that stays B2 can be invisible in the tests. The same loss after a downgrade to CCC, inside a bucket already at its limit, hits the OC numerator directly. A life insurer's explain is about book yield. Most of its corporate bonds are held at amortized cost against long liabilities, so a spread move changes unrealized gains that do not flow through capital unless the bond is impaired or sold, while the risk-based capital charge moves with ratings (Chapter 17; Chapter 4-C's insurer seat). The systematic desk is the seat for which the daily mark is everything. Each of the other seats has a rule that makes the mark matter less on most days and far more on a few, and the explain is how the desk sees those days approaching for the people on the other side of its trades.

*Builds on:* §8.6 (the hedge matrix), §24.2–§24.3 (CDS legs and $N^{\text{JTD}}$), §20.2 (NAV and the premium), Appendix D §D.2 (variation margin) and §D.5 (the auction). *Used in:* §8C.6 (the stale-series morning), §8C.8 (the default day), Chapter 10-B (index rolls).

## 8C.3 Financing, Fees, FX and Day One

"In a restructuring," Theo says, "interest expense lives below EBITDA. Nobody looks at it until the covenant test."

"Here it's above the line every morning," Ines says, "because it's a cost of holding the position, and holding the position is the business."

The **financing** line is the repo interest on bonds funded in repo and the borrow fee on bonds the desk is short (Appendix D §D.3, the funding leg of §24.1). Monday's book paid \$15,000 for three days on about \$40mm of financing. A short in a bond that goes *special*, where the borrow fee jumps because everybody wants the same bond, shows up as a financing line that grows while the bond's price line looks quiet. Folding the borrow fee into the spread line would make a squeeze look like a slow, unexplained bleed in the idiosyncratic return. **Fees and commissions** (platform, clearing and exchange fees, and any commission on voice trades) come from the blotter and the clearing statements, and they are facts. **FX** matters for every line not in dollars, and it brings the chapter's first cross-term.

> **Math, Gently.** *Two prices, one cross-term.* Hold €10mm face of a euro bond at 95 when EURUSD is 1.0800. The next day the bond is at 95.50 and the euro is at 1.0750. In dollars, the position went from \$10,260,000 to \$10,266,250, up \$6,250. Split it. The bond's own move is half a point on €10mm, €50,000, worth \$54,000 at yesterday's rate. The currency's move on yesterday's €9.5mm of value is −\$47,500. Those two add to \$6,500, not \$6,250. The missing −\$250 is the cross-term: today's €50,000 gain, converted at today's slightly worse rate. It belongs to neither the bond nor the currency, so the explain prints it on its own line with a stated convention (here: local move at yesterday's rate, FX on yesterday's value, cross-term separately). The cross-term is small on quiet days and large on violent ones, and it is the first sign of the problem §8C.5 runs into with signals.

**Day-one P&L** is the line the market-making half of the desk watches most. When the desk buys \$5mm of a bond at 97.25 at a minute when the composite mid is 97.32, it has made $(97.32 - 97.25) \times 5{,}000{,}000/100 = \$3{,}500$ against the composite before anything else has happened:

$$
\Pi^{\text{day-one}} = \eta\,\big(P^{\text{comp}}_{t_{\text{trade}}} - P^{\text{fill}}\big)\,\frac{N}{100},
$$

with $\eta = +1$ for a buy and $-1$ for a sell. It has its own line for two reasons. It is a markout at horizon zero (§3.3), so it belongs to the trading decision and not to the positions' market moves. And the composite is itself a prior, a model's estimate of where the bond would trade, not a price anyone paid (§20.2, Law 9). A desk that folds day-one P&L into the spread line will find, a month later, that its "spread" P&L is mostly the gap between its fills and a vendor's model, and that the gap tends to reverse at the five-day markout when the composite was wrong.

> **[SOURCE EXTRACTION]** *Paleologo_Advanced_Portfolio_Management p.159:* "the attribution is computed based on daily returns, based on market close prices and positions. Orders, however, happen intraday. As an extreme case, take the scenario where you open and close a position intraday. Attribution will attribute zero PnL to this stock. This discrepancy is usually categorized as a 'trading PnL'."
>
> **Annotation.** Paleologo is writing about equities, where the close is a single print and the intraday trade is the exception. A credit desk inverts both. The close is several photographs taken at different times by different vendors, and almost every position was traded intraday at a price that differs from any of them. The trading P&L Paleologo describes as a discrepancy is, on a credit desk, the day-one line and the timing line, and the composite at the minute of the trade carries the weight that the closing print carries in equities. It belongs on the trade ticket, with its own timestamp. An explain that keeps only end-of-day marks attributes the edge of every intraday trade to "market".

The last line in this group is the one Chapter 3-B introduced in a Math, Gently box: **timing**. If a bond is marked at 4:00 p.m. and its futures hedge at the 3:00 settlement, the book reports a P&L of

$$
\Pi^{\text{phantom}} = -\text{DV01}_B\,\big(\Delta y_{t_2} - \Delta y_{t_1}\big),
$$

where $\Delta y_t$ is the yield change from yesterday's snap to time $t$ today, in basis points. It reverses the next day, when the hedge's next photograph catches up. Nothing was traded. Its daily standard deviation is about $\text{DV01}_B\,\sigma_y\sqrt{(t_2 - t_1)/\text{(one trading day)}}$, which for \$22,000 of DV01 and an hour between snaps comes to roughly \$52,000 a day (§3B.1). Product control and risk agree on one time and take every mark at it or adjust it to it, which is Chapter 8-B's 3 p.m. snap (§8B.3). The explain shares that snap with the risk model. Where a vendor's mark arrives late or early, a *timing* line computed from the hedge's intraday price at the snap time names the difference, so that it never sits in the residual.

*Builds on:* §3.3 (markouts), §3B.1 (the snap), §24.1 and Appendix D §D.3 (funding). *Used in:* §8C.5 (cross-terms), Chapter 2-B (implementation shortfall against the composite), Chapter 18-B (dealer day-one P&L).

## 8C.4 The Foot

At the end of Theo's first week, Ines writes one equation on the whiteboard and underlines it twice:

$$
\Pi^{\text{official}} = \sum_{\text{lines}} \Pi_\ell + U .
$$

"That's not a model," she says. "It's a definition. $U$ is whatever is left. You can't be wrong about a definition. You can only be wrong about the lines, or about the official number."

The foot is an identity, and the explain foots every day by construction. What makes it useful is the claim attached to $U$. The lines were built from facts and forecasts, the official number was built from product control's marks, and $U$ measures how far the two disagree. A small $U$ says the desk understands its own book. A large one says something on the book was booked, marked or modeled wrong, and the explain does not yet know which.

How small counts as small is a policy decision, not a statistical estimate. The policy this desk uses *(illustrative)* is

$$
|U| \le \text{tol} = \min\big(1\ \text{bp of NAV},\ 5\%\ \text{of the 1-day expected shortfall}\big).
$$

> **Math, Gently.** *Expected shortfall, the average of the bad days.* Line up a thousand simulated or historical days of the book's P&L from worst to best. The 97.5% expected shortfall is the average loss across the worst 25 of them, 2.5% of the days. It answers "on a genuinely bad day, how much do we lose on average?", where value-at-risk answers only "where does a bad day start?" For this desk the 1-day ES is about \$1.5mm *(illustrative)*, so 5% of it is \$75,000. The full version, with the jump-to-default layer that makes the worst days worse, is Chapter 8-B.

For a \$100mm book, 1 bp of NAV is \$10,000 and 5% of ES is \$75,000, so the tolerance is \$10,000. Two terms appear because each protects against a different failure. The ES term stops a low-risk book from treating a residual comparable to its daily risk as noise: an unexplained larger than a twentieth of a bad day means the desk does not know what its risk is. The NAV term stops a high-risk book from hiding behind its own volatility. A trader who runs a lot of risk does not earn a larger allowance for not knowing what happened. Monday's corrected residual was −\$9,000, inside. Monday's first residual, −\$119,000, was nearly twelve times the tolerance.

Escalation on this desk is the part of the policy people remember, because it costs them something. Theo watched it happen in his second week. At 7:18 the explain showed −\$64,000 unexplained, and within two minutes product control and Ines both had the alert, because the policy names them and a deadline (8:00). By 8:00 the residual had been traced to three issuers, and new risk in those three names was frozen. The rest of the book traded normally, since one bad line is not a reason to stop the desk. The freeze lifts when the residual has a name. If it has none by the 3 p.m. snap, the case goes to the risk committee and the marks involved are downgraded in provenance, from "composite" to "under review", which shrinks their weight in the risk model until somebody proves them. This one had a name by 10:30: a block sold on Friday had been booked to the wrong account, so one book showed a position it no longer owned and another showed P&L on a bond it had never held. Nobody adjusted anything. The ticket was rebooked, both explains re-ran, and the residual went to −\$3,000.

Month-end adds a second official number. The fund administrator, or the bank's independent price verification group, replaces the desk's daily composite marks $\bar P$ with month-end evaluated prices $\hat P$. Each difference becomes a line of its own,

$$
\Pi^{\text{true-up}}_i = \big(\hat P_i - \bar P_i\big)\frac{N_i}{100},
$$

labeled *mark change, evaluated vs composite*. It is never booked to spread or idiosyncratic, because it is a change in who is forecasting the price, not a change in the price (Law 9). Any true-up line beyond tolerance either gets accepted, with a note, or disputed. The dispute process is a short procedure with a long tail. Product control files the challenge, not the trader, and it files evidence rather than opinion: TRACE prints, dealer runs, the composite's history, and the prices of comparable bonds. The vendor's challenge window is short (two business days after month-end on this desk, *illustrative*), and its answer goes into the explain's own ledger next to the challenge. Section 8C.6 walks one through.

That ledger is the last piece. Every breach, every true-up beyond tolerance and every dispute gets a row: date, size, cause, owner, hours to close, and the date the line reversed, if it did. Over a quarter the ledger becomes a hand history of the explain itself, and §8C.9 reads it.

![Figure 8C.1: Monday's explain as a waterfall, from zero to the official −\$399,000: accrual and pull-to-par first (custodian, then model), rates for bonds and futures, factor spread, the CDX hedge's factor and coupon lines, idiosyncratic, financing, fees and day-one, then the stale-mark line of −\$110,000 and the unexplained of −\$9,000 last, against a shaded tolerance band of ±\$10,000. Illustrative.](assets/figures/ch08c_explain_waterfall.png)

*Builds on:* Chapter 8-B (ES, the limit sheet, escalation thresholds), §12.5 (desmoothing stale marks), Appendix B §B.8 (composites as model outputs). *Used in:* §8C.6, §8C.9, §28.6 (the mark is the stop you don't know you have), Chapter 17-B (the mark gap).

## 8C.5 Which Signal Made the Money?

On the last Friday of September the risk meeting runs long, because Ines asks the question every PM eventually asks. "The book made \$2.4mm this month. Which signal made it?"

"Momentum," Kaz says. "Obviously."

Theo has two numbers on his screen, and they disagree. The momentum sleeve, simulated by itself on September's data, would have made \$3.0mm. The value sleeve, by itself, \$2.0mm. The book that held both made \$2.4mm, less than momentum would have made alone.

The first half of the answer is easy, and it is linear. Write the book's positions as a sum of signal sleeves, $w = \sum_s w_s$, measured in DTS-weighted dollars per *issuer*, not per bond. With the issuer-level IDO returns $r^{\text{IDO}}_j$ of §8.8, the book's IDO P&L splits without remainder:

$$
\Pi^{\text{IDO}} = \sum_j w_j\,r^{\text{IDO}}_j = \sum_s \sum_j w_{s,j}\,r^{\text{IDO}}_j .
$$

Measuring by issuer matters because signals collide inside capital structures. On 14 September the value sleeve wanted \$10mm of Halvorsen's 6s and the momentum sleeve wanted to be short \$6mm of Halvorsen's 7.25s. The book held a net issuer exposure, and the issuer's news hit both bonds. Measured bond by bond, each sleeve would claim the full issuer move on its own bond, and the two claims would not add up to what the book earned. Measured by issuer, the common move is counted once, which is Law 2 (bonds are not bets; issuers are) applied to attribution.

The second half is where Kaz's "obviously" falls apart. The sleeves were never held separately. The optimizer saw the sum of the two signals, netted them, skipped the trades that would not pay for themselves, and scaled the result down to fit one risk budget. The "momentum alone" book that made \$3.0mm never existed, and neither did the "value alone" book. Each is a counterfactual. Daily returns are linear in positions. Portfolio construction is not linear in signals.

> **Math, Gently.** *Why two signals that both made money can add to less than either.* Suppose each signal, run alone, earns its \$3.0mm or \$2.0mm at full risk. Run together, they share one risk budget, so each runs at roughly two-thirds of its standalone size, and on the issuers where they disagree they cancel. The combined book makes \$2.4mm. The interaction, $2.4 - 3.0 - 2.0 = -2.6$, is real money that belongs to neither signal alone, the same kind of leftover as the FX cross-term in §8C.3, only larger. There is no single correct way to divide it. There are conventions, and an honest report prints which one it used.

Call $v(S)$ the P&L of the book the optimizer would have built from the signals in the set $S$, rebuilt each day on that day's inputs. Three conventions are in common use. *Sequential* attribution gives the first signal its standalone value and each later signal its increment. Momentum first gives momentum 3.0 and value −0.6. Value first gives value 2.0 and momentum 0.4. The answer depends on which signal you list first, which is a strange property for a number that will decide somebody's bonus. *Equal split* gives each signal its standalone value minus half the interaction: momentum $3.0 - 1.3 = 1.7$, value $2.0 - 1.3 = 0.7$. The *Shapley value*, from cooperative game theory (Shapley, 1953), averages each signal's increment over every order in which the signals could have been added:

$$
\phi_s = \sum_{S \subseteq \mathcal{S}\setminus\{s\}} \frac{|S|!\,(n - |S| - 1)!}{n!}\,\big[v(S \cup \{s\}) - v(S)\big].
$$

For two signals it averages the two sequential answers, momentum $\tfrac12(3.0 + 0.4) = 1.7$ and value $\tfrac12(2.0 - 0.6) = 0.7$, and for two signals it coincides with the equal split. For three signals it averages over six orderings and the two conventions part company. Shapley needs $2^n - 1$ counterfactual books every day, which is cheap for two or three signals and expensive past four. Beyond that, desks use the optimizer's gradient, a marginal attribution that linearizes the construction around today's book. Every one of these is a defensible convention, and choosing one is not where reports go wrong. They go wrong when the header leaves the choice out. This desk's report says, in its first line, "signal attribution: issuer-netted IDO; cross-term by Shapley over rebuilt books."

> **[SOURCE EXTRACTION]** *Paleologo_Advanced_Portfolio_Management p.136:* "Total returns – and a portfolio's total PnL – live in the Sun's frame of reference. It is easy to fool ourselves with the belief that we beat birds, airplanes and supermen at their own game. Idiosyncratic returns and PnL live in the Earth's frame of reference."
>
> **Annotation.** The passage opens with Paleologo's own jogging speed measured relative to the Sun, and it is the best one-paragraph defense of IDO accounting in print. Signal attribution needs a third frame. After the factors are stripped, each signal's IDO P&L lives in the frame of the *book*: the netting, the shared risk budget and the costs the book paid. A signal's research ledger (§8.8: monthly information coefficient on the whole universe) measures it in the Earth's frame. The production ledger measures it in the book's frame. When the two disagree, both can be right. The research ledger says whether the signal knows something. The production ledger says whether this book got paid for it.

One more check stands between a signal's P&L and its reputation, and it is the markout (§3.3). September's momentum P&L came heavily from three issuers that gapped on news nine days after the signal had entered them. The 1-, 5- and 20-day markouts on momentum's entries that month were flat. Momentum held the right bonds when the news came, but it did not cause the news, and its entries did not predict it. A signal's P&L becomes its edge only when the markouts agree, and in September they did not. Kaz conceded "obviously" on the following Tuesday.

> **View From Another Seat.** *The multi-strategy platform.* On a pod platform the attribution question is a compensation question, and the platform answers it in advance. Portfolio managers are typically paid a share of their own P&L, with factor exposure hedged or charged centrally, so the platform's explain strips factors first and pays on what is left. Cross-terms between pods are mostly invisible to the pods themselves, because each pod sees only its own book. The platform sees the sum, nets the overlaps and keeps the interaction as its own P&L or cost. (Public accounts of this structure include the *Odd Lots* episodes listed in this chapter's Resource Graph; we describe the seat generically.) A single systematic desk running several signals faces the same question with one difference: the person dividing the interaction also runs the signals, which is a reason to fix the convention before the month starts rather than after it ends.

*Builds on:* §8.8 (the IDO ledger), §8.9 (`ido_engine`), §3.3 (markouts), §3.5 (the Edge Ledger), Law 2. *Used in:* §28.3 (allocation across signal horizons), §28.9 (net alpha by signal), Chapter 9 (the factor sleeves).

## 8C.6 Two Worked Mornings

### Morning (a): the stale series

Here is Monday, the cold open's morning, line by line. Chapter 3-B told it in round numbers from the door. This is the version product control signed at 9:55.

| Line | Source | \$ | bp of NAV |
| :--- | :--- | ---: | ---: |
| Coupon accrual, bonds (three days) | custodian | +75,800 | +7.6 |
| Pull-to-par and roll-down | model | +12,400 | +1.2 |
| Rates, bonds (key rates) | risk model × curve | −52,000 | −5.2 |
| Rates, Treasury futures | exchange settlement | +40,000 | +4.0 |
| Spread factors, bonds | risk model × factors | −338,000 | −33.8 |
| CDX HY protection, price from factor | risk model × index | +110,000 | +11.0 |
| CDX HY protection, coupon (three days) | clearing statement | −16,700 | −1.7 |
| Idiosyncratic, bonds | issuer curves | −96,300 | −9.6 |
| Convexity | model | +300 | 0.0 |
| Financing | treasury | −15,000 | −1.5 |
| Fees and commissions | blotter | −4,000 | −0.4 |
| Day-one | blotter vs composite | +3,500 | +0.4 |
| **Sum of named lines** | | **−280,000** | **−28.0** |
| Mark correction pending: CDX HY old series | product control | −110,000 | −11.0 |
| Unexplained | | −9,000 | −0.9 |
| **Official P&L as booked** | | **−399,000** | **−39.9** |

At 7:20 Theo sorted the positions by residual, and the hedge had the signature described in §8C.2: an official price change of exactly zero on a day its factor moved 0.275 points, so its residual was exactly minus its factor line. The mark's timestamp was Friday, 4:45 p.m. The protection was on the old series. The roll had moved the market's quoting to the new series on Monday, and the vendor, finding no quotes for the old one, had published Friday's price again with Monday's date on the file.

At 7:28 Theo told Ines that all twelve basis points were the hedge. "Down forty is really down twenty-eight."

"And the other one?"

"The residual was 11.9. Call it twelve. Rounding."

"That," Ines said, "is what *Other* said."

It took Theo a moment, and then it landed. He had found a real cause for eleven basis points and quietly given it credit for the twelfth, which is ROBO's plug done by hand with better manners. At 9:40 product control had quotes on the old series from two dealers. It had fallen 0.275 points, the same as the new series, so the correction was exactly +\$110,000 and the series basis was unchanged on the day. The −\$9,000 stayed where it was: inside the \$10,000 tolerance, logged in the ledger with the cause *bond residuals, unattributed*, and never assigned to the hedge. The official P&L was restated to −\$289,000. Tuesday's explain then showed the +\$110,000 correction as a named line with a source and a date, not as an unexplained gain, which is the only form in which a fixed mistake can be seen as fixed.

Two changes went into production that week. The roll-day job now checks every index position for the stale signature and stops the explain with a named flag if it finds one. And every position that rolls carries a series-basis line, built from the roll quote observed at the time of the roll, so that a generic ticker's jump from the old series to the new appears as what it is.

### Morning (b): the true-up on a bond that did not trade

Friday 30 October is month-end. The desk owns \$8mm of Corriveau Logistics 9.5% notes due 2030 (fictional), carried at a composite of 84.50. The bond last printed on TRACE nine days earlier, at 84.25 for \$2mm, and two dealers' runs on the 30th showed 84–85 and 83¾–85. On Monday morning the administrator's month-end evaluated price arrived at 81.50. The true-up line read

$$
\Pi^{\text{true-up}} = (81.50 - 84.50) \times \frac{8{,}000{,}000}{100} = -\$240{,}000,
$$

24 bp of NAV, two and a half times the day's tolerance. Nothing else in the explain moved with it. Corriveau's factor line was +\$4,000, its issuer curve had not moved, and its other bond had not traded either. The explain had a three-point loss and no cause.

Theo found the cause by reading the vendor's methodology note instead of the bond's chart. An evaluated price for a bond that has not traded is built from its neighbors: other bonds in the same rating, sector and maturity cell, adjusted by a model. On 29 October one of those neighbors, a different issuer, had announced a liability-management transaction and dropped nine points. The matrix had moved the whole cell. Corriveau had been repriced on a stranger's news.

"Is that a stale mark or a wrong mark?" Kaz asked.

"It's a mark doing exactly what it's built to do," Mags said. "Which is why you dispute it with evidence and not with feelings." The Ad Hoc Group, represented by counsel, neither confirms nor denies that its mark is stale.

Product control filed the challenge on Monday at 11:00: the 21 October TRACE print, both dealer runs with timestamps, nine days of composite history between 84.2 and 84.6, and the neighbor's press release, with a sentence explaining why its news was specific to that issuer. On Tuesday afternoon the vendor revised to 84.00. The P&L moved back $(84.00 - 81.50) \times 8{,}000{,}000/100 = +\$200{,}000$. The remaining −\$40,000 true-up, half a point, was accepted with a note. The dealer mids averaged about 84.4, a revised price of 84.00 was defensible inside a point-wide market, and a dispute is a request for evidence to be weighed, not a mechanism for getting one's own mark back. The month-end NAV, struck on the fifth business day, used 84.00.

This is Law 9 working in both directions. A mark is a moving average of the truth, and the true-up is usually the day the average catches up. This time the vendor's average had caught up with somebody else's truth. About half the disputes this desk files are rejected, and the rejected ones are often the most informative, because they are the cases where the vendor had seen a print the desk had not.

![Figure 8C.2: The two mornings side by side, before and after. Left: Monday's explain with the residual at −\$119,000 (stale-series signature highlighted), then corrected to −\$9,000 inside the tolerance band. Right: the Corriveau true-up line at −\$240,000, the dispute evidence (the TRACE print, dealer runs and composite history) on a timeline, and the revised line at −\$40,000. Illustrative.](assets/figures/ch08c_two_mornings.png)

*Builds on:* §8C.2 (the series roll), §8C.4 (tolerance and dispute), Appendix B (TRACE and evaluated-price sources), Law 9. *Used in:* §8C.9 (the explain's hand history), Chapter 10-B (rolls), Chapter 17-B (marks as contested prices).

## 8C.7 Case Study: The Whale's Explain (JPMorgan's Chief Investment Office, 2012)

After the Corriveau dispute, Mags drops a printed report on Theo's desk. It runs to about 300 pages and has been annotated in three colors of ink. "The best description anybody has published of a credit desk's morning explain," she says, "is a Senate report about one that didn't work."

The report is the U.S. Senate Permanent Subcommittee on Investigations staff report *JPMorgan Chase Whale Trades: A Case History of Derivatives Risks and Abuses* (15 March 2013). Chapters 3-B and 6 borrowed single facts from it. Read as a whole, it is a case history of an explain that footed every day to marks chosen by the desk being explained. Page numbers below are the report's own. Individuals are not named here, and nothing below is invented.

**The book.** The Synthetic Credit Portfolio sat inside the bank's Chief Investment Office and held credit index and tranche positions. Its net notional grew from "over \$51 billion" at the end of 2011 to "over \$157 billion" at the end of March 2012 (p.185). Its losses eventually reached at least \$6.2 billion.

**The daily ritual.** The book filed "daily profit/loss (P&L) reports ... internally," and its positions were marked each day by "a junior trader charged with marking the SCP's positions" (p.5). Early in January the marks were set "at or near the midpoint price in the daily range of prices (bid-ask spread)." Later the book "began to assign more favorable prices within the daily price range" (p.5). The report quotes a recorded call: "I am not marking at mids as per a previous conversation" (p.5). One day's email estimated a \$43 million loss, "the largest daily loss yet," and referred to a "\$600 million to \$800 million 'lag'" (p.83).

**The shadow explain.** For 12–16 March the marker kept "a spreadsheet tracking the differences" between the reported values and values at the midpoint. By that sheet, the reported year-to-date loss was \$161 million, and at mids it was \$593 million (p.5). Read that spreadsheet as an explain and it is a very good one. It has two columns, one from the desk's marks and one from an independent price, and the difference is the unexplained, \$432 million of it. Its flaw was ownership. The person keeping it was the person whose marks it contradicted, and no tolerance, clock or escalation rule was attached to it.

**The bad days.** On 30 March the book reported a daily loss of \$319 million, and the report records a gap of \$512 million later identified by the bank's Valuation Control Group (p.5). On 10 April an estimated daily loss of about \$6 million was re-issued 90 minutes later, "after a confrontation between two CIO traders" (p.5).

**The price test.** The Valuation Control Group's tolerances let the investment-grade index mark "vary from the midpoint ... by up to 6 basis points" (p.112, n.675). An analyst described the March practice as having "marked the book at the boundary of the bid/offer spread ... then applied a tolerance" (p.141). Internal audit rated the group "Needs Improvement," citing the absence of a "formally applied price sourcing hierarchy" and of "documented/consistently applied price testing thresholds" (p.141). Five risk metrics (VaR, CS01, CSW10%, stress loss and stop-loss advisories) were all breached in the first quarter of 2012 (p.7).

**The outside explain.** The resolution came from counterparties, not from inside the bank. The Chief Investment Office and the bank's own Investment Bank "assigned different values to identical credit derivative holdings," and the counterparties who posted collateral against their own marks objected. The resulting collateral disputes peaked at \$690 million (p.6). In May the CIO was told to mark as the Investment Bank did, which "used an independent pricing service to identify the midpoints," and that "resolved the collateral valuation disputes in favor of the CIO's counterparties" (p.6). On 13 July 2012 the bank restated its first quarter for an additional \$660 million of losses (p.98).

"So they had an explain," Theo says. "They had a shadow explain. They had a price test and five limits. What was missing?"

"Nothing on the list," Ines says. "What was missing is the reason each thing on the list exists."

Four ideas from this chapter would each have shortened the story, and the report supplies the evidence for every one of them. The first is that the foot has to land on a price the desk did not choose. The CIO's daily P&L footed perfectly, to the CIO's marks, and an identity is only as honest as the number on its left-hand side. The shadow spreadsheet was the real explain, and it had no owner outside the desk.

The second is that a tolerance has to be stated in dollars and sized against the book, not in basis points per instrument. Six basis points sounds tight. Take \$100 billion of five-year index notional with a risky duration of about 4.5, an illustrative position and not the SCP's actual mix of longs and shorts. Its CS01 is $100 \times 10^9 \times 4.5 \times 10^{-4} = \$45$mm per basis point, so a 6 bp tolerance leaves about \$270mm of discretion on that one line. A tolerance expressed per instrument grows with the position, which means it grows fastest exactly when the position is becoming impossible to exit. This desk's rule, the smaller of 1 bp of NAV and 5% of ES, is written to shrink in relative terms as the book grows.

The third is that a counterparty's collateral call is an explain with an adversary. A collateral dispute is a residual that the other side has backed with its own money, and it cannot be marked away. Of all the numbers in the report, the \$690 million of disputes was the first that the desk did not control, and it was the one that resolved the marks.

The fourth is the escalation clock. Five limits were breached in a quarter (p.7). On this desk, a breach freezes new risk in the names involved until the residual has a name, which is the opposite of the incentive that lets a position grow while its explain is under discussion.

Mags takes the report back. "In my day we didn't have a Valuation Control Group," she says. "We had a controller named Sal, who came down to the floor on the last day of the month with a folder of broker quotes. Sal didn't have a tolerance." She considers this. "Sal was the tolerance."

### Two more mornings from the public record

*The Revlon wire, from the lenders' side.* On 11 August 2020 Citibank, as agent on Revlon's 2016 term loan, meant to pay interest to the lenders and instead wired about \$894 million of principal. The operational story, including the "six-eye" control that missed it, belongs to §27.7. On the lenders' side, the next morning's explain showed something simpler: a cash receipt at par on a loan that the market priced at 20–30 cents, with no trade, no paydown notice and no maturity. A production explain classifies that as a *cash event with no trade*. It flags it, books nothing to P&L, and someone calls the agent. A system that treated the receipt as a repayment would have extinguished the position and booked a gain of roughly 75 points of face, which is what a plug looks like when it has a wire attached. The defendants' funds held \$558.6 million. Judge Furman ruled for them on 16 February 2021 under the discharge-for-value rule. On 8 September 2022 the Second Circuit (No. 21-487) vacated, holding that a full early repayment, three years before maturity, from a borrower priced at 20–30 cents, put the lenders on inquiry notice, and rehearing was denied on 12 October 2022. The court's reasons for inquiry notice read like the explain's reasons for a flag.

*Hertz, effective date.* On 30 June 2021 Hertz's plan became effective, and in creditors' and shareholders' position files old claims and old stock turned into cash, new common stock and warrants or rights (§16.6). That morning's explain was entirely corporate-action lines. An explain that read the swap as a sale of the old instruments at one mark and a purchase of the new ones at another would have produced a fake loss on one line and a fake gain on another, and neither would have had anything to do with the market.

*Builds on:* §3B.1 (marks after the close), §6.4 (the VaR spreadsheet from the same report), §16.6 (Hertz), §27.7 (the Revlon wire, canonical). *Used in:* §8C.8, §28.6 (marking to bid and the drawdown stop), Chapter 17-B (marks as contested prices).

## 8C.8 When to Apply It, and When It Breaks

The explain works best on a liquid book on an ordinary day, which is to say on the days nobody asks about. Five kinds of day strain it, and a seasoned product controller checks for each one before reading the residual column.

*Illiquid names.* For a bond that has not traded in a month, the explain explains a mark, not a price. Its residual is small because its mark is a model of its neighbors, and the risk model's lines are a model of the same neighbors. A small unexplained on such a bond is agreement between two models. Corriveau showed the failure in the other direction. The useful check is the provenance column (traded, composite, evaluated, model; §27.2), read before the residual column, together with §12.5's reminder that stale marks shrink every beta measured on them.

*The default day.* When Halvorsen's 6s stopped paying (Chapter 12-B), three lines changed character at once. Accrual stopped and the bond began to trade flat, so the accrual line went to zero, and the accrued interest the desk had been carrying (three points on \$10mm, \$300,000, by the missed coupon date) left the accrual column and became part of a claim whose value now sits inside the price (§4B.1, Appendix A §A.5). The price line took the jump, and the protection's gain was booked as a forecast of the auction's final price, not a fact, until the auction weeks later (Appendix D §D.5). For those weeks the jump-to-default line is the largest line on the page and the least certain.

*Corporate actions.* An exchange offer, an A/B exchange or a CUSIP change reaches the position file as an old line out and a new line in. If the two lines are marked from different sources, the explain shows a fake loss on one and a fake gain on the other. Chapter 3-B's 6:45 diff caught one such exchange before it could, and Appendix B §B.16 lists the evidence to keep for each action. The explain books the swap at carrying value with zero P&L, and the market lines start from the new instrument's first mark.

*New issues.* A bond priced yesterday has no return history and so no estimated loadings. Chapter 8-B assigns it its rating-and-sector cell's loadings until it has a history of its own. For its first weeks, part of what the explain calls idiosyncratic is really error in that assignment, and a signal that buys new issues heavily will look more skillful than it is.

*The wire you are not owed.* Revlon's lenders (§8C.7) had a cash event with no trade. The explain flags any receipt or payment that matches no coupon, settlement, margin call or fee, and it sends the flag to a person. The cash stays off the P&L until that person says otherwise.

> **Trend Watch.** *The prices the explain is marked against are changing hands (2026).* On 29–30 July 2026 Intercontinental Exchange agreed to buy MarketAxess for \$167 a share in cash, about \$6.0bn of equity value and \$5.7bn of enterprise value, and described the deal as joining MarketAxess's trading data and analytics with ICE's pricing, reference-data and index businesses (ICE 8-K, Ex. 99.1). The same morning, MarketAxess announced that it was "suspending its practice of issuing monthly volumes press releases" (Q2-2026 release). The shareholder vote and the HSR waiting-period expiry were both set for 29 October 2026, with closing expected in the first half of 2027 (MarketAxess DEFM14A and 8-K). Separately, FINRA's affiliate-principal transaction indicator (Regulatory Notice 26-16, 26 August 2026; voluntary from 31 August 2026, mandatory from 2 August 2027) suppresses the inter-affiliate leg of qualifying trades so that only the trade with the outside counterparty is disseminated. FINRA's own baseline put such trades at up to about 5.7% of 2025 transactions, an upper bound in counts and not dollars (SR-FINRA-2026-009). Tradeweb's September 2026 report notes that it has "not restated prior periods" (Tradeweb, 6 October 2026). *What it means for the explain:* the composite, the evaluated price and the TRACE prints in a dispute file are all changing provenance at once. A composite is becoming one company's product, and print counts have a structural break at 31 August 2026. The explain's own history needs a break marker on that date, or the unexplained series will show a change in the market's plumbing as a change in the desk's skill. Chapter 17-B argues that price itself became contested in 2025–26. This is the public-market version of that argument.

*Builds on:* §4B.1 and Appendix A §A.5 (trading flat), Chapter 8-B (loadings for new issues), §12B.9 (Halvorsen), §27.2 (provenance types), Appendix B §B.16 (corporate actions). *Used in:* §8C.10 (edge cases), Chapter 22 (market structure), Appendix C (trend rows).

## 8C.9 The Explain's Own Hand History

Ines keeps the explain's ledger the way she kept poker hand histories, and for the same reason. One bad hand teaches nothing. A pattern across hundreds of hands says something about the player. At the end of September she asks Theo to read the quarter.

| Cause (third quarter, 63 trading days) | Breaches | Sum of \|U\| at breach (\$k) | Median hours to a name |
| :--- | ---: | ---: | ---: |
| Month-end evaluated-price true-ups | 4 | 410 | 26 |
| Stale or mismapped index marks, roll week | 3 | 260 | 2 |
| Booking errors (wrong account, late ticket) | 2 | 120 | 3 |
| Corporate actions and identifiers | 2 | 95 | 5 |
| Timing and snap mismatches | 1 | 18 | 1 |
| **Total breaches** | **12** | **903** | |
| Days inside tolerance (bond residuals, unattributed) | 51 days | 290 | |

*(Illustrative.)* Seven of the twelve breaches fell on six days: the three month-ends and the three days of roll week. Theo's first reaction is that this is obvious, and his second is to ask whether it is real or just a pattern that he went looking for.

> **Math, Gently.** *Is a cluster real? The binomial test.* If breaches landed on random days, each of the 12 would fall on one of the 6 special days with probability $6/63 \approx 0.095$, and the count on special days would follow a binomial distribution with $n = 12$ and $p = 0.095$. Its mean is about 1.1. The binomial gives the probability of a count at least as large as the one observed: $\Pr(X \ge 7) = \sum_{k=7}^{12}\binom{12}{k}p^k(1-p)^{12-k} \approx 3.6 \times 10^{-5}$, about one in 27,000. The clustering is not a coincidence. The test does not say *why* (calendars, vendors, a tired evening shift), only that something structural is there to find. The full version, with the multiple-testing caution that applies when many possible clusters were tried, is Chapter 7-B.

What the table says is what Chapter 3-B's calendar predicted. The unexplained clusters around the dates when the book's instruments change identity (rolls, exchanges) or when the person forecasting their price changes (month-end). It does not cluster around big market days. The model's lines handle volatility well. The explain fails on bookkeeping and calendars, which is good news, because those are cheap to fix, and it is also a warning: an explain tuned only on volatile days will miss most of its own failures. The 51 quiet days inside tolerance summed to \$290,000 of unattributed residual, roughly zero on average and never assigned to anything. That is the line ROBO's *Other* would have erased.

Theo's Edge Ledger (§3.5, §3B.11) gets its first row that is not a trade idea: *22 September, found the residual, \$110,000, stale old-series index mark, roll day; fix: stale-signature check on roll-day job.* The desk counts that row as edge, because it was money the desk would otherwise have misreported, and because the fix keeps paying every March and September.

![Figure 8C.3: The unexplained by day over the third quarter: daily bars of $U$ against the shaded ±\$10,000 tolerance band, with month-ends and roll week marked by vertical lines; seven of the twelve breaches sit on those six days. Illustrative.](assets/figures/ch08c_unexplained_by_day.png)

> **Quant-shop life (a fictional composite).** *The break report, at a systematic asset manager.* At 6:10 p.m. on the third business day of October, the fund administrator's break file arrives: 412 rows in which the administrator's numbers and the manager's differ. Dev, the product controller (a composite; no real person), has a train at 7:48. Sorting by cause takes four minutes. Of the rows, 409 are one bond. A 144A note held across 409 separately managed account lots paid its coupon on a Monday, the administrator booked it on the record date and the manager on the payment date, and every lot breaks by the same few dollars. Two rows are the September index coupon. The 20th fell on a Sunday, and the administrator accrued the protection to the unadjusted date while the manager accrued to Monday the 21st. The difference is one day of 500 bp on the notional, which on \$40mm is \$5,556. The last row is the A/B exchange from Chapter 3-B: the administrator is still pricing the old 144A CUSIP, which nobody has quoted for two weeks, at a level that is a full point stale. Dev clears 411 rows by 8:35 and misses the train. The last row needs the pricing vendor's challenge form, deadline 4 p.m. tomorrow, and the form's only required field is "evidence of executable levels." She attaches two dealer runs and a screenshot of the new CUSIP's TRACE prints, and eats noodles that have been cold since 6:30. The vendor accepts the challenge at 2:15 the next afternoon. Nothing in the file involved a model, a factor or a view on credit. Most of what a book does not understand about itself turns out to be about dates and identifiers.

*Builds on:* §3.3 (hand histories), §3.5 and §3B.11 (the Edge Ledger), §3B.3 (the month and the rolls), Chapter 7-B (testing a pattern you went looking for). *Used in:* §28.9 (the dashboard), Chapter 27 (alert hygiene).
