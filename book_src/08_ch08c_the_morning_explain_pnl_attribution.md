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
> **Annotation.** Paleologo is writing about equities, where the close is a single print and the intraday trade is the exception. A credit desk inverts both. The close is several photographs taken at different times by different vendors, and almost every position was traded intraday at a price that differs from any of them. The trading P&L Paleologo describes as a discrepancy is, on a credit desk, the day-one line and the timing line, and the composite at the minute of the trade carries the weight that the closing print carries in equities. Store it, with its own timestamp, on the trade ticket. An explain that keeps only end-of-day marks attributes the edge of every intraday trade to "market".

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
