# Appendix D: Plumbing: Settlement, Clearing, Margin, Financing and the ISDA Credit-Event Machine

## D.0 Cold Open: Hedged on the P&L, Naked on the Wire

*Tuesday, 4:52 p.m.* The sticky-note trade from Chapter 24 had gone through on Monday: \$10mm Halvorsen Packaging 6% 2031 at 88, and \$10mm of five-year Halvorsen protection. (Halvorsen is fictional; all numbers illustrative.) The risk system showed the package as flat. The operations queue showed four lines in red.

*Halvorsen 6% 2031: FAIL. Counterparty short, chain fail.* *Repo: unfunded, collateral not received.* *CDS: initial margin call, \$600,000, posted 09:02.* *Larkspur Foam 2029 TLB: pending agent consent, day 12.*

"The trade is hedged," Theo said. "Why is my screen red?"

"Because the hedge lives on the P&L," Ines said, "and the queue lives on the wire. Different tables, different chips. The P&L tells you what you'll have. The wire tells you whether you'll still be seated when you get it."

"It's a timing difference," said Kaz. "In expectation it's zero."

"So is a margin call you can't meet," said Mags, "for about a day." She did not look up. "Back in my day a fail meant a messenger with a bag of certificates who got lost on Water Street. At least you knew where the bond was. It was in the bag."

Kaz brightened. "Wait, if the seller failed to deliver, is that a Failure to Pay? Do we trigger the swap?"

"A fail is when the bond doesn't show up," Mags said. "Failure to Pay is when the coupon doesn't. One costs the seller a day's interest. The other costs somebody par minus recovery. Please never ask that in front of a Determinations Committee."

Theo had told ROBO on Friday to "make sure everything settles." ROBO did exactly that: it set every settlement date equal to the trade date. The backtest P&L was perfect, and the bank account was not.

**Between the handshake and the money, who holds what, for how long, against how much collateral, and what does a contract mean by "default" when the money does not arrive?**

By the end of this appendix you will be able to: read the settlement calendar of every instrument the book trades and price a fail or a settlement gap; tell initial margin from variation margin and compute a netted margin; turn a repo haircut into leverage, return on equity and a forced-selling schedule; name the funding leg of every basis in the book; compute a CDS's day-one cash, including the upfront and the accrued rebate; walk a credit event from the missed coupon to the auction's final price; and check a deliverable, a successor and an orphan against the rules.

**How to use this appendix.** It is a reference, so it is mostly tables. The derivations already live elsewhere: settlement clocks and clearing economics in §22.3–22.6, loan settlement in §21.2, ETF settlement gaps in §20.6, and CDS legs, funding, cheapest-to-deliver, the auction and succession in §24.2 and §24.4–24.8. This appendix gives each mechanism one table and one formula, with a back-reference to its derivation. Each section ends with a **Used in:** line so you can go from a term to the places it matters.

> **Prerequisites.** Clean and dirty prices and day counts (Chapter 4-B; App A §A.4); the risky annuity RPV01 and the credit triangle (§6.8); the two legs of a CDS (§24.2).

*Notation.* In this appendix a roman T+k is a settlement offset of $k$ business days after trade date. An italic $t+1$ is still the next period of a time series, as App A §A.3 resolves that collision. The haircut is $h$, the repo funding spread is $\phi$, and repo specialness is $\ell$, as in §24.4. The margin period of risk is $H$ (in days), as in (22.8). Where Chapter 22's netting factor appears, it is written $\phi^{\text{net}}$ so that it cannot be confused with the funding spread.

**Used in:** Chapter 24's cold open (the same trade, priced); §D.8 (the same trade, through the pipes); App E (the Law numbers that tag §D.10).

## D.1 The Settlement Clock: Four Instruments, Four Calendars

A trade is two promises with a gap between them. At T you agree a price; at T+k one side delivers the asset and the other delivers the cash. In between, each side is exposed to the other's failure to perform, which costs the price move since T if the counterparty disappears and a day of interest if it is merely late. Clearing houses margin the first risk (§D.2). Market convention prices the second. Everything else in this section is a calendar.

**Table D.1. Settlement cycles and fail regimes (US unless stated; simplified).**

| Instrument | Convention | What actually happens | Ledger and rails | If it fails | Built in |
| :--- | :--- | :--- | :--- | :--- | :--- |
| US Treasuries | T+1 (market convention; T+0 common) | Same day for many dealer trades | Fedwire Securities; FICC nets members' trades | TMPG fails charge, so the cost of failing is $\max(r^{\text{ref}}, 3\%)$, eq. (22.9) | §22.3.2, §22.4 |
| US corporate bonds (IG, HY, 144A) | T+1 since 2024-05-28 (T+2 from 2017-09-05, T+3 before) | New issues often settle on a longer, expressly agreed cycle *(approx.)* | DTC book entry; NSCC compares and nets eligible trades | Seller loses the use of the cash; the buyer's remedy is a buy-in under the FINRA Uniform Practice Code (Rule 11810; check the current text) | §22.3 |
| European corporate bonds | T+2; T+1 from 2027-10-11 | The UK targets the same date | Euroclear, Clearstream, T2S | CSDR cash penalties per day of fail (since 2022-02-01); mandatory buy-ins not in force | Trend Watch, §D.7 |
| Par leveraged loans (LSTA) | T+7, with delayed compensation after T+7 | Average about 20 business days *(approx.; §21.2.1)* | Agent bank's register; assignment agreement; ClearPar | No fail as such; delayed compensation shifts the carry (§21.2.2) | §21.2 |
| Distressed loans (LSTA) | T+20 | Months are not unusual; Moyer reports up to 120 days in 2004 | Agent register; purchase-and-sale agreement with the upstream chain | Settlement risk on the chain of prior sellers | §21.2.1 |
| Single-name CDS and CDX/iTraxx | Step-in T+1 (calendar); upfront cash T+3 business days | No principal changes hands | CCP (ICE Clear Credit, LCH CDSClear) or bilateral under an ISDA/CSA; DTCC Trade Information Warehouse | Nothing to fail: margin calls instead (§D.2) | §24.2, §D.4 |
| Credit ETF shares (HYG, JNK, LQD, BKLN) | T+1 | Secondary trades settle like equities | NSCC CNS, DTC | CNS fail; equity close-out rules apply to short sales | Ch 20 |
| ETF primary market (create, redeem) | Generally T+1, matching the shares | In-kind bond baskets settle T+1; loan funds deliver or raise cash on loan timelines | AP and fund agent; custom baskets | The fund or AP finances the gap | §20.1, §20.6.1 |
| Listed credit futures | Daily variation margin; final cash settlement | | CME, Cboe, ICE and Eurex clearing | Margin default, not a fail | Ch 10-B |
| Repo | T+0 or T+1 start; overnight or term | Mostly overnight | Tri-party (BNY), bilateral, FICC sponsored | Treasury fails charge on the collateral leg | §D.3 |
| Bankruptcy trade claims | No convention | Weeks; transfer is noticed under Bankruptcy Rule 3001(e) | Claims agent's register | Objection risk, not a fail | Ch 12-B, §16.5 |

**The cash at settlement.** Bonds are quoted clean and settle dirty, with accrued interest counted to the *settlement* date, not the trade date. For face $N$, clean price $P^{\text{clean}}$ in points and an annual coupon $c$ on 30/360:

$$
\text{Cash}_{\text{settle}} = N\left(\frac{P^{\text{clean}}}{100} + c\,\frac{d_{30/360}\big(t_{\text{cpn}^-},\,t_{\text{settle}}\big)}{360}\right),
$$

where $t_{\text{cpn}^-}$ is the last coupon date. The invoice is fixed at the *contractual* settlement date. If the seller fails, the buyer pays the same invoice later, so the seller bears the cost of the delay: the interest on the cash it has not received, $\text{Cash}_{\text{settle}}\cdot r^{\text{ref}}\cdot d^{\text{fail}}/360$, plus any penalty. In Treasuries the TMPG charge puts a floor of 3% a year under that cost, eq. (22.9). In US corporates there is no charge, so the discipline comes from buy-ins and from the counterparty's memory.

**The settlement gap.** When two legs of one position settle $\Delta d$ days apart, somebody finances the cash for the difference:

$$
C^{\text{gap}} = \text{Cash}\cdot r^{\text{fund}}\cdot\frac{\Delta d}{360}.
$$

A loan fund that owes redemption cash at T+1 against loans whose sale settles in about 20 business days (call it 28 calendar days) finances \$100mm for 27 days. At a 5% funding rate that is about \$375,000 *(illustrative)*, or 38 bp of the redemption, paid by the holders who stay. That is §20.6.1's "basket that cannot settle" in one line. The gap is also why ROBO's cold-open shortcut fails: setting every settlement date equal to the trade date silently books $C^{\text{gap}} = 0$ on every trade.

> **Ways This Blows Up.** (1) *Holiday calendars.* The bond market follows SIFMA's calendar, not the stock exchange's: SIFMA recommends a full close on Columbus Day and Veterans Day while the NYSE is open, so a T+1 bond trade done the Friday before Columbus Day settles on Tuesday, while a T+1 ETF trade settles on Monday. A basket trade that mixes the two has a one-day settlement gap built into the calendar. (2) *Accrued to the wrong date.* Accruing to trade date rather than settlement date is one day of coupon on every trade; across a 150-line portfolio trade it is a systematic P&L leak, and it is invisible in a backtest that never settles. (3) *Treating "T+7" as a date.* For loans it is the day delayed compensation starts, not the day cash moves; model the settlement lag as a random variable (§21.2.2), not a constant.

**Used in:** Chapter 4-B (clean, dirty, day counts); §20.1 and §20.6.1 (ETF settlement and the loan-fund gap); §21.2.1–21.2.2 (loan settlement, delayed compensation); §22.3 (T+1 and fails); App A §A.4 (day-count table).

## D.2 Clearing, Netting and the Two Margins

A central counterparty (CCP) steps between buyer and seller by *novation*: the original trade is replaced by two trades, each against the CCP. The CCP then nets each member's trades into one position and asks for two kinds of collateral. "It's the only player at the table who never bluffs and never leaves," Ines says. "It just makes everyone post a stack before the cards come out, and it counts the stack again every night."

**Variation margin (VM)** settles the day's mark-to-market in cash: $\text{VM}_t = V_t - V_{t-1}$, paid by the loser to the winner, usually the next morning. Across the market VM sums to zero. CCPs credit or charge interest on accumulated VM (price alignment interest) so that a cleared trade's economics match an uncleared one's. **Initial margin (IM)** covers the loss the CCP could suffer between a member's default and the close-out of its book, the margin period of risk $H$. In the square-root form of §22.3.1, for a position $x$ with daily volatility $\sigma$,

$$
\text{IM} = z_\alpha\,\sigma\sqrt{H}\,|x|.
$$

VM is a transfer and IM is a tax on the horizon. A hedged book pays almost no net VM, but it still posts IM on any risk that does not net, and IM is funded at the desk's funding spread $f$.

**Netting, derived.** For a book of positions $x \in \mathbb{R}^n$ with daily covariance $\Sigma$, portfolio IM is $z_\alpha\sqrt{H}\sqrt{x^\top\Sigma x}$, against a gross sum of standalone margins $z_\alpha\sqrt{H}\sum_i\sigma_i|x_i|$. Take $n$ equal long positions with common volatility $\sigma$ and pairwise correlation $\rho$. Then $x^\top\Sigma x = x^2\sigma^2\big(n + n(n-1)\rho\big)$ and

$$
\frac{\text{IM}_{\text{port}}}{\sum_i \text{IM}_i} = \frac{\sigma\,x\sqrt{n + n(n-1)\rho}}{n\,\sigma\,x} = \sqrt{\frac{1+(n-1)\rho}{n}}.
$$

The inverse square of this ratio is $n/(1+(n-1)\rho)$, the effective breadth of Law 2 (§28.2). The CCP charges you for the number of independent bets you actually hold, which makes it the only counterparty in the building that has read Chapter 28. With $n = 100$ and $\rho = 0.3$ the ratio is $\sqrt{30.7/100} = 0.554$, so netting saves 45% of gross margin. A long-index, short-constituents book nets almost everything, which is why §22.6.1 finds clearing cheapest for dealers who hold the index *and* its single names at one CCP.

**The jump.** A volatility-scaled IM sees spreads, not defaults. A protection seller on one name can lose $N(1-R)$ overnight, which no $\sqrt{H}$ scaling of spread volatility captures. CCPs therefore add a jump-to-default charge on net sold protection, roughly $N_i\,(1 - R^{\text{stress}})$ less the position's mark, on the largest exposures, and size the default fund to survive the default of the two members to which they are most exposed (the "Cover 2" standard of the CPMI–IOSCO *Principles for Financial Market Infrastructures*, 2012, for systemically important CCPs). The jump is charged once, in its own line (Law 6). Netting it away against spread hedges is how a margin model fails on the morning it is needed.

**Table D.2. The CCP default waterfall (generic order; each CCP's rulebook governs).**

| Layer | Whose money | Note |
| :--- | :--- | :--- |
| 1 | Defaulter's initial margin | Sized to cover $H$ days at high confidence |
| 2 | Defaulter's default-fund contribution | |
| 3 | CCP's own capital ("skin in the game") | Small by design |
| 4 | Surviving members' default-fund contributions | Mutualized loss: your money, their default |
| 5 | Assessments on surviving members | Usually capped |
| 6 | Recovery tools (VM gains haircutting, tear-up) | The layer nobody wants to test |

**Table D.3. What is cleared, where, and how it is margined (approx.; check each CCP's current methodology).**

| Product | Clearing status | Main venues | IM | VM |
| :--- | :--- | :--- | :--- | :--- |
| CDX.NA.IG/HY, iTraxx Main/Crossover (standard tenors) | Mandatory for US persons since 2013 (CFTC, §22.6) | ICE Clear Credit; LCH CDSClear | Spread scenarios plus jump-to-default and liquidity add-ons; multi-day $H$ | Daily, cash |
| Single-name CDS | Voluntary (SEC security-based swaps; no mandate); dealer-to-dealer largely cleared | ICE Clear Credit; LCH CDSClear | As above; portfolio-margined against the indices | Daily, cash |
| Uncleared CDS, iBoxx total return swaps, bespokes | Bilateral under ISDA Master and CSA | None | Uncleared-margin rules for in-scope firms: ISDA SIMM, 10-day $H$, €50mm threshold; final phase from 2022-09-01 for groups above €8bn notional | Daily since 2017-03-01 for in-scope pairs |
| Treasury cash and repo | Mandate phasing in: cash 2026-12-31, repo 2027-06-30 | FICC (direct, sponsored, done-away) | VaR-based with add-ons | Daily |
| Listed credit futures | Exchange-cleared | CME, Cboe, ICE, Eurex clearing | Exchange margin, short $H$ | Daily, cash |
| Corporate bonds, ETF shares | Cash settlement through NSCC and DTC | NSCC | Clearing fund for broker-dealers, eq. (22.8) | Mark-to-market add-on |
| Leveraged loans | Not cleared | Agent bank | None; counterparty risk until settlement | None |

**Procyclicality.** Because IM scales with $\sigma$, it rises when volatility rises: the margin you post in a crisis is the margin your model wished you had posted before. In March 2020, IM at CCPs worldwide rose by roughly \$300bn *(approx.; BCBS–CPMI–IOSCO, Review of margining practices, 2022)*, at the same time as dealers were raising haircuts (§D.3) and ETF discounts were widening (§20.5). Plumbing is correlated in stress, and that correlation is a supply schedule for forced selling (Law 15).

**Used in:** §10.1 (index CDS as an unfunded, margined instrument); Chapter 10-B (futures margin and the trend sleeve's cash); §22.4 (the netting factor $\phi^{\text{net}}$ against IM); §22.6.1 (when clearing a CDS is cheaper, eq. 22.15); §24.4 (IM on the CDS leg of the basis); §28.5 and §28.7 (liquidity runway and the leverage band).

## D.3 Financing: Repo, Haircuts, Specials and the Funding Leg of Every Basis

A bond position has two prices: the price of the bond and the price of the money you hold it with. The first is on the screen. The second is agreed every morning with someone who can change their mind, which is why Mags calls a repo haircut "a margin call that's been patient" (Chapter 24's cold open).

A repurchase agreement is a sale of a bond for cash with a promise to buy it back at a fixed higher price. Legally it is a sale; economically it is a secured loan; in bankruptcy it is something the restructuring banker should note at once. The safe harbors of the Bankruptcy Code (§§555, 559 and 561 for securities contracts, repos and master netting agreements) exempt the lender's close-out from the automatic stay. The stay of Chapter 12-B, which freezes almost every other creditor on the petition date, does not reach your repo dealer, who may sell your bonds the morning you file.

> **[SOURCE EXTRACTION]** *Veronesi_Fixed_Income_Securities p.52:* "The profit to the trader is then $P_T - P_t$ − Repo interest. In percentage terms, the trader only put up the haircut (the margin) as own capital." And: "The position is highly leveraged and entails quite large risks."
>
> **Annotation.** Our analysis: Veronesi's haircut is a dollar amount subtracted from the price; ours is a fraction $h$ of market value, so his "return on capital" is our carry divided by $h$. The textbook is about Treasuries, where $h$ is about 2% and sticky. The modern credit desk departs in two ways. First, for corporate collateral $h$ is a *state variable*: it is set by a dealer's risk committee, it rises with volatility, and in bilateral repo it rose sharply in 2008–2009 while tri-party haircuts barely moved (Copeland, Martin and Walker 2014, *Repo Runs: Evidence from the Tri-Party Repo Market*; Gorton and Metrick 2012, *Securitized Banking and the Run on Repo*). Second, the "quite large risks" are not only price risk. A rise in $h$ forces selling before the price has moved at all, which the derivation below makes exact.

**The arithmetic.** Buy market value $A$ (dirty) with haircut $h$. The dealer lends $L = (1-h)A$ at the repo rate $r^{\text{repo}} = r + \phi$, ACT/360, and you post equity $E = hA$. Leverage is $A/E = 1/h$. Per unit of asset, the annual excess carry over the riskless rate on all capital is the asset's spread less the funding spread on the borrowed part,

$$
\pi = s - \phi\,(1-h), \qquad \text{ROE}^{\text{excess}} = \frac{\pi}{h},
$$

which is the long leg of §24.4's negative-basis package. A short seller works the other way: it borrows the bond through a reverse repo and lends cash at the special rate. If the bond is in demand, that rate sits below general collateral (GC) by the specialness $\ell = r^{\text{GC}} - r^{\text{spec}} \ge 0$, so the short pays $\ell$ a year for the privilege. The fails charge of (22.9) bounds specialness. Failing to deliver costs $\max(r^{\text{ref}}, 3\%)$ a year, and nobody pays more to borrow a bond than it costs to fail, so $r^{\text{spec}} \gtrsim r^{\text{ref}} - \max(r^{\text{ref}}, 3\%) = \min(0,\ r^{\text{ref}} - 3\%)$: a floor at zero when rates are above 3%, and the reason special rates went negative in 2009 when they were not.

**Haircuts force selling before prices move: derivation.** Hold equity $E = hA$ against position $A$. Let the price fall by a fraction $u$ and the haircut rise from $h$ to $h'$. Equity becomes $E' = E - uA = (h-u)A$, and the largest position it can support is $E'/h'$. The position is now worth $A(1-u)$, so the fraction that must be sold is

$$
q^{\text{sell}} = 1 - \frac{E'/h'}{A(1-u)} = 1 - \frac{h-u}{h'\,(1-u)}, \qquad 0 \le u < h,
$$

with $q^{\text{sell}} = 1$ when $u \ge h$ (the equity is gone and the dealer liquidates). The case $u = 0$ isolates the plumbing: a haircut move alone forces the sale of $1 - h/h'$ of the book. Mags's 2008 story, $h$ from 10% to 25%, means selling 60% of the position before any price has moved. Add a 5% price drop and it is $1 - 0.05/(0.25 \times 0.95) = 78.9\%$. The buyers are the dealers who raised the haircut, which is why Mags tells the story without names. Haircut schedules are published, or at least predictable, and so the selling they force is a supply schedule you can read in advance (Law 15).

**Table D.4. Haircuts by collateral (approx. and illustrative; dealer terms vary).**

| Collateral | Tri-party median *(approx.; NY Fed tri-party statistics, 2010–2015 snapshots)* | Bilateral or prime broker, calm *(illustrative)* | Bilateral or prime broker, stress *(illustrative)* | Note |
| :--- | :--- | :--- | :--- | :--- |
| US Treasuries | about 2% | 0–2% | 2–5% | FICC sponsored repo nets it |
| IG corporates | 5% | 5–10% | 10–20% | |
| HY corporates | 8% | 10–20% | 25–50% | 2008 bilateral moves of this size are the Mags story |
| Leveraged loans | not standard repo collateral | financed through TRS, SPV or warehouse lines, 20–35% equity | 40%+ or the line is pulled | §17.6, §21.3 |
| Credit ETF shares | equity-style | 15–25% | 30%+ | Prime-broker margin, not repo |
| CDS (any) | unfunded | IM a few % of notional | IM ×2–3 | §D.2 |

**Table D.5. The funding leg of every basis in the book.**

| Basis | What the long leg costs to hold | What the short leg costs | The funding term that moves the band | Derivation |
| :--- | :--- | :--- | :--- | :--- |
| Bond–CDS, negative (long bond, buy protection) | Repo at $r+\phi$ on $(1-h)$; equity $h$ | IM on the CDS, funded at $f$ | $\phi$, $h$, CDS IM | §24.4 |
| Bond–CDS, positive (short bond, sell protection) | IM on sold protection | Specialness $\ell$ on the borrowed bond | $\ell$ | §24.4 |
| ETF premium or discount (create or redeem) | AP's bond inventory, in repo or at a prime broker | ETF stock-borrow fee on a short | $h$ on the bonds, borrow fee, settlement gap $\Delta d$ | §20.3, §20.6.1 |
| Credit futures against ETF or cash | Futures embed financing near SOFR | ETF or TRS financing | SOFR plus the desk's funding spread | Chapter 10-B |
| CDX index against its intrinsic value | IM on the index | IM on 100 or 125 single names | Portfolio margining at one CCP | §D.2, Chapter 10-B |
| Loan bought but not settled | Delayed compensation: a forced repo at the base rate | | Base rate $b$ against the desk's own funding | §21.2.2 |
| Portfolio-trade basket against its lines | Dealer balance-sheet rent | | Capital and leverage-ratio rent | §22.1, §19.2 |
| Treasury cash against futures (the rates twin) | Repo | Futures margin | Repo rate, IM at FICC and CME | §22.4 |

Every basis in the book is a price difference plus a financing difference. A "riskless" basis whose funding leg is overnight and whose convergence is six months away is a short option on the repo desk's mood.

**Used in:** §12.7 (liquidity tiers as the binding constraint); §17.6 (borrowing-base haircuts on PIK loans); §20.3 (the ETF arbitrage band); §21.2.2 (delayed compensation as a forced repo); §22.3.2 and §22.4 (fails, specials and Treasury clearing); §24.4 (basis carry and the arbitrage band); §28.7 (the leverage band); Chapter 12-B (the automatic stay that the safe harbors escape).

## D.4 The CDS Contract as a Calendar: Coupons, Dates and the Day-One Cash

Since the 2009 "Big Bang" and "Small Bang" protocols, a CDS trades like a bond with a standard coupon: everyone pays the same fixed coupon on the same dates, and the difference between the fair spread and the coupon is settled up front. Kaz assumed "IMM date" was a term from measure theory. It is the International Monetary Market, the CME division whose quarterly futures calendar CDS borrowed, keeping the months and moving the day to the 20th.

**Table D.6. Standard contract terms (simplified; the ISDA Definitions and the standard-terms supplements govern).**

| Field | North American corporate (SNAC) | European corporate | Indices (CDX, iTraxx) |
| :--- | :--- | :--- | :--- |
| Fixed coupon | 100 or 500 bp | 25, 100, 300, 500, 750 or 1,000 bp | CDX IG 100, CDX HY 500; iTraxx Main 100, Crossover 500 |
| Credit events | Bankruptcy, Failure to Pay | Bankruptcy, Failure to Pay, Restructuring (Mod-Mod-R) | Each constituent's standard terms |
| Premium dates and day count | 20 Mar, Jun, Sep, Dec; ACT/360; business-day adjusted; the final period includes the maturity date | Same | Same |
| Standard maturities | Roll semiannually: on 20 Mar and 20 Sep the on-the-run five-year moves to a 20 Jun or 20 Dec maturity (since December 2015) | Same | New series launched each 20 Mar and 20 Sep |
| Step-in and cash | Protection and accrual from T+1 (calendar); upfront paid T+3 business days | Same | Same |
| First coupon | Full coupon on the first payment date; the seller pays the accrued rebate at T+3 | Same | Same |
| Lookback (backstop) | Credit events: 60 calendar days; succession events: 90 days | Same | Same |
| Failure to Pay thresholds | Payment Requirement \$1mm after the obligation's grace period (at least three business days if it has none) | Same, in euros | Same |
| Settlement | The auction (§D.5); physical delivery as fallback | Same | Defaulted name paid through the same auction; the index changes version |
| Quoting | Spread (IG names) or points upfront (stressed names) | Same | CDX IG in spread, CDX HY in price |

**The day-one cash.** Write the points-upfront in the first-order form of §24.2, $\text{PUF} = (s^{\text{par}} - c)\,\text{RPV01}$, where $s^{\text{par}}$ is the par spread, $c$ the fixed coupon and RPV01 the risky annuity in years (the ISDA Standard Model computes it from a flat hazard curve; §6.8 and §24.2 build both). The protection buyer will pay a full coupon on the next IMM date although it was protected only from step-in, so the seller pays back the coupon accrued since the last coupon date. With $a$ accrued days (counted per the Standard Model), an index factor $f$ ($f = 1$ for a single name), and notional $N$, the cash from buyer to seller at T+3 is

$$
\text{Cash}_{\text{B}\to\text{S}} = N f\left[\text{PUF} - c\,\frac{a}{360}\right].
$$

A negative value means the seller pays the buyer. For the cold-open trade, $s^{\text{par}} = 370$ bp, $c = 500$ bp, $\text{RPV01} = 4.20$ and $a = 30$ give $\text{PUF} = -5.46$ points and a rebate of $0.4167$ points, so the protection buyer *receives* \$587,667 on \$10mm. Theo's first reaction, "they're paying me to buy insurance," is the usual one and is wrong. The upfront is the present value of the excess coupon he has agreed to pay, and the CCP holds his IM against exactly that.

**Index defaults.** If constituent $i$ with weight $w_i$ (1% of CDX HY's 100 names, 0.8% of CDX IG's 125) has a credit event, the index protection buyer receives $N w_i(1 - \text{FP}_i/100)$ at the auction's final price $\text{FP}_i$. The index factor falls from $f$ to $f - w_i$, the contract continues as a new version on the remaining names, and the running coupon is paid on $N(f - w_i)$ from then on. A trend model that reads an index's notional without its factor will mistake each default for a position change (§10.1).

**Used in:** §6.8 (the bootstrap from standard-coupon quotes); §10.1–10.2 (index CDS returns and the roll); Chapter 10-B (roll windows and series basis); §24.2 (CDS legs, upfront and running spread); App A §A.4 (the CDS row of the day-count table, where "T+1" is the step-in date).

## D.5 The ISDA Credit-Event Machine: Events, the Committee and the Auction

The bond defaults under its indenture. The swap defaults under the ISDA Definitions, when a committee says so. Most of the time the two agree, and §24.8 covers the times they don't. The machine runs in five steps: an event, a question, a resolution, a list of deliverables, and an auction. Each step has a clock.

**Table D.7. Credit events (2014 Definitions; simplified, and the Definitions govern).**

| Credit event | In one line | Threshold | Standard for |
| :--- | :--- | :--- | :--- |
| Bankruptcy | Insolvency proceedings, a petition, an assignment for creditors, a written admission of inability to pay | None | All corporates |
| Failure to Pay | Failure to pay an Obligation when due, after its grace period | Payment Requirement \$1mm | All |
| Restructuring | A binding cut in coupon or principal, a postponement, a change of ranking or currency, on a Multiple Holder Obligation (more than three unaffiliated holders, two-thirds to consent), resulting from credit deterioration | Default Requirement \$10mm | European corporates (Mod-Mod-R), sovereigns; *not* SNAC |
| Obligation Acceleration or Default | Obligations accelerated, or capable of being accelerated | \$10mm | Some EM and legacy contracts |
| Repudiation/Moratorium | The issuer disclaims or suspends its obligations | \$10mm | Sovereigns |
| Governmental Intervention | A binding change imposed by a government or resolution authority: bail-in, expropriation | \$10mm | Financials (added in 2014) |

The SNAC row is the one that matters most for this book. With only Bankruptcy and Failure to Pay on the menu, a distressed exchange or an uptier that pays every coupon is not a credit event, however much value it moves. That is why the book has two default rates (§14.1) and why recovery is a U (Law 7). It is also why a coupon can be "failed" on purpose (§24.8).

**The Determinations Committee.** Five regional committees (Americas, EMEA, Asia ex-Japan, Japan, Australia–New Zealand) decide the questions, with DC Administration Services, Inc. (DCAS) as secretary, having taken over the role from ISDA *(2018; approx.)*. Voting members are dealers and non-dealers, and the clearing houses sit as CCP members. DCAS's announcement of the committees effective 2026-04-29 lists Bank of America, Barclays, BNP Paribas, Citibank, Deutsche Bank, Goldman Sachs International and JPMorgan Chase Bank among the global dealer voting members; Citadel, Elliott and PIMCO as non-dealer voting members; and ICE Clear Credit and LCH SA as CCP members *(approx.; from press-release copies; check cdsdeterminationscommittees.org)*. Any eligible market participant can submit a question, with Publicly Available Information attached. Most questions need an 80% supermajority, and a question that fails to reach it goes to an External Review panel. The committee publishes its decisions and its votes, which makes it one of the few places in credit where the hand history is free.

**The clock, in the order a desk lives it** (stylized; DC timetables vary):

```text
Day 0           Potential event: coupon missed, petition filed, bail-in announced.
Day 0 + grace   Failure to Pay crystallizes when the obligation's grace period ends
                (at least three business days if it has none).
Day q           DC Question submitted. Backstop: events up to 60 calendar days
                before q are caught (90 days for succession questions).
q + days        DC resolves: credit event or not, its date, whether to hold an auction.
r + about 1 wk  Initial list of deliverables; two days to add, three to challenge;
                80% to include or exclude, else External Review.
r + 2 to 4 wks  Auction: stage 1 sets the Inside Market Midpoint, stage 2 the Final Price.
FP + 3 to 5 bd  Cash settlement of CDS; physical settlement of auction-formed trades.
```

On a credit event the protection buyer receives $N(1 - \text{FP}/100)$ and pays the premium accrued up to the event determination date. The stage-1 and stage-2 formulas, the Adjustment Amount and the cap logic are derived in §24.6.1. The parameters below are the ones a simulator needs.

**Table D.8. Auction parameters, with one real set for scale.**

| Parameter | What it does | Windstream Services, 18 Mar 2019 (DC decision of 6 Mar 2019) |
| :--- | :--- | :--- |
| Initial Market Quotation Amount | Size of each dealer's stage-1 two-way market | \$2mm |
| Maximum bid–offer spread | Width of each two-way | 3 points |
| Minimum valid submissions | Quorum for stage 1 | 8 |
| Cap Amount | How far FP may sit beyond the IMM against the open interest | 1 point |
| Pricing increment | Tick | 1/8 point |
| Timetable | Stage 1, 9:45–10:00 a.m., IMM 10:30; stage 2, 12:45–1:00 p.m., FP 2:00 | |
| Settlement | | The later of T+3 and 21 Mar 2019 |

(Windstream's story has its canonical home in §25.5.2, with the CDS side in §24.8.3; only the parameters are borrowed here.)

> **[SOURCE EXTRACTION]** *Schmid_Credit_Risk_Pricing_Models p.159:* "The price of the defaulted asset is typically determined via a dealer poll conducted within 14-30 days of the credit event. The purpose of the delay is to let the recovery rate stabilize." And: "Current market standards for banks and corporates require that the protection buyer pays the accrued premium to the credit event; sovereign default swaps do not require a payment of accrued premium."
>
> **Annotation.** Our analysis: Schmid describes the market before the 2009 hardwiring, when cash settlement meant a poll of dealers, each of whom might hold the position the poll would settle. The auction replaced the poll and kept its two-to-four-week delay, and the delay now does a different job: it lets the open interest form, so stage 2 knows who must sell bonds (§24.6). "Let the recovery rate stabilize" became "let the forced sellers line up," which is why auction-day prices undershoot and then bounce (Chernov, Gorbenko and Makarov 2013). The accrued-premium rule survives unchanged for corporates, and a payout engine that forgets it overstates every credit-event P&L by up to a quarter's coupon.

**Restructuring, where it still applies.** Restructuring credit events are settled through auctions run in maturity buckets (2.5, 5, 7.5, 10, 12.5, 15, 20 and 30 years, *approx.*), because the old cheapest-to-deliver problem is worst when only some obligations are restructured. The variants limit which maturities can be delivered:

| Variant | Where | Deliverable maturity limit (simplified) |
| :--- | :--- | :--- |
| XR (no Restructuring) | SNAC | Not applicable |
| MR (Modified Restructuring) | Legacy North American | About 30 months after the restructuring date, but no earlier than the swap's maturity |
| MMR (Modified-Modified) | European corporates | 60 months for the restructured obligation, 30 months for others, no earlier than the swap's maturity |
| CR (full Restructuring) | Sovereigns, some EM | Up to 30 years |

**Used in:** §6.8 (the protection leg); §10.2.3 (index returns across a credit event); §13.6 and Chapter 12-B (why an LMT is usually not a credit event); §14.1 and §14.7.2 (two default rates, and the definitional wedge between agency and ISDA defaults); §24.6 (the auction derived); §24.8 (events that are engineered).

## D.6 Deliverables, the Reference Obligation and the Cheapest-to-Deliver

The swap pays par minus the price of something, and this section is about what that something is. The *Final List* $\mathcal{D}$ is the set of obligations the DC accepts as deliverable. The payout per unit of notional is set by the cheapest of them,

$$
\Pi^{\text{CDS}} = 1 - \min_{j \in \mathcal{D}} \frac{P_j}{100},
$$

because in the auction the participants who sell bonds deliver the cheapest one they own (§24.5). When all pari obligations accelerate in a bankruptcy, they trade on the same claim and $\min_j P_j$ barely differs from any $P_j$, so the option is close to worthless (regime 1 of §24.5.1). When they do not accelerate, as in a Failure to Pay with no cross-acceleration, each trades on its own cash flows, so the long, low-coupon bond is cheapest and the option can be worth half of par (regime 2).

**Table D.9. Deliverable obligation characteristics, North American standard (simplified).**

| Characteristic | Meaning | Why the desk cares |
| :--- | :--- | :--- |
| Category: Bond or Loan | Bonds and loans both qualify | A loan or a secured bond can be the CTD |
| Not Subordinated | Ranks at least pari passu in *payment* with the reference obligation; collateral and liens are ignored | An excluded first lien that an uptier has pushed down the lien stack stays deliverable, and is often the cheapest thing on the list |
| Standard Specified Currency | US dollar, euro, sterling, yen, Swiss franc, Canadian dollar | |
| Transferable; Not Bearer | Freely transferable registered obligations | Restricted forms can be excluded (the 2026 DISH DBS question, §24.5) |
| Assignable Loan; Consent Required Loan | Loans transferable by assignment, with or without consent | Sears 2018 went to External Review on this (§24.8.3) |
| Maximum Maturity 30 years | | A 22-year 5% bond qualified at Hovnanian (§24.8.2) |
| Outstanding Principal Balance (2014) | The deliverable amount is the principal claim, net of any principal already written down or discounted | The 2026 Ardagh challenge argued that bonds slated for equitization had zero outstanding principal; per a 9fin episode, the EMEA DC rejected it in a split vote *(confirm against the DC record)* |
| Asset Package Delivery (2014; financials, sovereigns) | After a bail-in or forced exchange, the resulting package is deliverable | The fix for the 2013 SNS Reaal expropriation |
| Qualifying Guarantee ("All Guarantees" in North America) | Another entity's debt is deliverable if the Reference Entity guarantees it | A drop-down financing at an unguaranteed subsidiary is not deliverable |

The *Standard Reference Obligation* (SRO) list, introduced in 2014, fixes each entity's reference obligation for each seniority level. The SRO sets the seniority of the contract; "Not Subordinated" is measured against it.

The second row deserves Theo's catchphrase. Under the Definitions, subordination means contractual *payment* subordination, and the presence or absence of collateral does not count. §12B.2 separates lien subordination from payment subordination for the bankruptcy court; the Determinations Committee makes the same distinction. So in a Serta-style uptier (§13.3.1), the excluded lenders' term loan, now effectively third in line for the collateral, is still Not Subordinated, still deliverable, and probably the cheapest thing on the list. The clause that hurt the excluded lender raises the payout on the CDS it may have bought against exactly that risk. Every clause is a payoff function (Law 8), and sometimes it pays the victim.

**Used in:** §13.3.1 and §13.6 (uptiers and drop-downs seen from the swap); §14.1 (why auction recovery and ultimate recovery differ); §24.5 (the CTD option derived); §24.8.2 (Hovnanian); §12B.2 (lien versus payment subordination).

## D.7 Succession and Orphaning

When debt moves to new entities in a spin-off, merger, exchange or drop-down, the swap follows the debt according to thresholds on the share of the Reference Entity's Relevant Obligations (its bonds and loans) that each entity *assumes*. With $w_e$ the share assumed by entity $e$ and $w_0$ the share retained (derived in §24.8.1):

**Table D.10. Successor rules (simplified; the 2014 Definitions govern).**

| Case | Condition | Successor(s) | The swap becomes |
| :--- | :--- | :--- | :--- |
| 1 | Some $w_e \ge 75\%$ | That entity alone | One swap on $e$ |
| 2 | One or more $w_e > 25\%$, and $w_0 \le 25\%$ | Each such entity | $m$ swaps of notional $1/m$ |
| 3 | One or more $w_e > 25\%$, and $w_0 > 25\%$ | Each such entity *and* the original | $m$ swaps of notional $1/m$ |
| 4 | No $w_e > 25\%$, original survives | None | Unchanged |
| 5 | No $w_e > 25\%$, original ceases to exist | The entity with the largest share | One swap on it |
| — | One entity assumes *all* obligations and the original ceases to exist | That entity, as Universal Successor, even outside the backstop | One swap on it |

The succession backstop looks back 90 days from the date of the succession question. Thresholds that are discontinuous invite engineering: moving 25.0% of the debt does nothing, and moving 25.1% halves your swap.

**Orphaning** is the case the table does not cover. If debt is *repaid* or refinanced at an entity that is neither the Reference Entity nor guaranteed by it, nothing has been assumed, so nothing succeeds. The swap keeps referencing an entity whose deliverable set $\mathcal{D}$ shrinks, and as $\mathcal{D} \to \varnothing$ the protection leg goes to zero, while the seller keeps collecting premium. Kaz asked whether an orphaned swap is assigned a guardian. "It gets a hedge fund," Mags said, "and it's always the one that sold the protection." (§24.8 has the full scene, and Hovnanian, §24.8.2, has the inverse trick of manufacturing a deliverable rather than removing them.)

> **Trend Watch: the plumbing calendar, 2009–2027.** *What changed:* almost every number in this appendix was set by a dated rule, and each date is a regime break in any feature built across it. *The dates:* 2009-04-08, the Big Bang protocol hardwires auctions, Determinations Committees and the 100/500 bp coupons in North America, with the Small Bang extending auctions to restructurings that summer. 2013-03-11, first compliance date for mandatory clearing of CDX and iTraxx (§22.6). 2014-09-22, the 2014 Definitions take effect for cleared contracts at ICE Clear Credit (SEC Release 34-72701). 2015-12-20, single-name CDS move to semiannual rolls. 2016-09-01, the LSTA's delayed-compensation protocol begins (§21.2.1). 2017-03-01, uncleared variation margin for in-scope swaps; 2017-09-05, US securities move to T+2. 2019-07-15, ISDA publishes the Narrowly Tailored Credit Event Supplement (§24.8.4). 2022-02-01, CSDR cash penalties for settlement fails in the EU; 2022-02-14, public dissemination of security-based swaps under Regulation SBSR; 2022-09-01, the last phase of uncleared initial margin. 2023-06-07, SEC Rule 9j-1 (§22.6); 2023-12-13, the Treasury clearing rule (§22.4). 2024-05-28, US T+1 (§22.3). 2025-10-14, the EU's T+1 amendment to CSDR is published in the Official Journal, applying from 2027-10-11 (the UK targets the same date). 2026-04-29, new DC memberships take effect. 2026-12-31 and 2027-06-30, mandatory clearing of Treasury cash and repo trades. *What it means for the desk:* put every date in the event calendar of §22.8. A settlement offset, a margin series or a recovery series that crosses one of these dates has changed definition, and a model fit across it without a regime flag is fitting the rulebook. As of this writing the 2014 Definitions, as supplemented in 2019, remain the standard for credit; we found no replacement published in 2025–2026 *(web check, October 2026)*.

**Used in:** §13.6 (drop-downs: assets move, debt may not); §24.8 (successors, orphans and manufactured events); §25.5.2 (Windstream, the canonical case); §22.8 (the event calendar).

## D.8 Worked Example: Halvorsen's Bad Week, Through the Pipes

Chapter 24 priced the sticky-note trade. Here we follow its cash. All numbers are illustrative, and the code in §D.9 reproduces the ledger.

**Day 0 (Monday).** The desk buys \$10mm face of Halvorsen 6% 2031 at 88 clean, with 75 days of accrued (30/360), and finances it in bilateral repo at a 15% haircut and a 4.80% repo rate. It buys \$10mm of five-year protection at a par spread of 370 bp against the 500 bp standard coupon, with RPV01 = 4.20 and 30 days since the last IMM date, and the CCP sets IM at 6% of notional. Separately, it buys \$5mm of the Larkspur Foam 2029 term loan at 84 on distressed documents, and treasury reserves \$4.2mm for a settlement date nobody can name. (Assume the cold open's fail cleared that evening; under §D.1 its cost fell on the failing seller, not on the desk.)

**Day 5 (the following Monday).** Halvorsen says a finance subsidiary will not pay the coupon on its 3% 2045 notes, which Halvorsen guarantees; the grace period is 30 days. The 2045 holders do not accelerate, so the 2031s keep trading on their own cash flows, at 62. The CDS goes to 1,500 bp with RPV01 = 3.20. The repo dealer marks the collateral and raises the haircut to 35%; the CCP raises IM on the name to 15%.

**Table D.11. The cash ledger (dollars; + is cash in).**

| When | Item | Formula | Cash |
| :--- | :--- | :--- | ---: |
| Day 1 | Repo lends against the bonds | $0.85 \times 8{,}925{,}000$ | +7,586,250 |
| Day 1 | Pay the dirty invoice | $10\text{mm}\,(0.88 + 0.06 \times 75/360)$ | −8,925,000 |
| Day 1 | Post CDS IM | $6\% \times 10\text{mm}$ | −600,000 |
| Day 3 | Receive CDS upfront and accrued rebate | §D.4: $-10\text{mm}\,[-0.0546 - 0.05 \times 30/360]$ | +587,667 |
| Day 5 | Repo margin call | $7{,}586{,}250 - 0.65 \times 6{,}333{,}333$ | −3,469,583 |
| Day 5 | CCP IM add-on | $(15\% - 6\%) \times 10\text{mm}$ | −900,000 |
| Day 6 | CDS variation margin received (next morning) | $10\text{mm}\,(0.32 + 0.0546)$ | +3,746,000 |
| Day 23 | Larkspur loan finally settles, paid from its Day-0 reservation | $0.84 \times 5\text{mm}$ | −4,200,000 |
| Day 35 | Grace period ends: Failure to Pay | DC question filed Day 36 | 0 |
| About Day 60 | Auction Final Price 50 (CTD: the 3% 2045) | $10\text{mm}\,(1 - 0.50)$, net of VM already received; buyer pays premium accrued to the event determination date | settled through the CCP |

Read the ledger in three ways.

*As P&L,* Day 5 is a good day. The bonds lost $26$ points, or \$2.60mm, and the CDS made \$3.746mm: net **+\$1.146mm**, because a par instrument over-hedges a bond at 88 (§24.1). Kaz's "timing difference" is, on this line, a profit.

*As cash,* Day 5 is a bad day. The repo call and the IM add-on are due on Day 5, and the VM that pays for them arrives on Day 6. The basis package's cumulative cash position, computed in the order the wires move (the Larkspur payment comes out of its own reservation), hits its low of **−\$5.72mm** on Day 5, against −\$1.94mm on Day 1. The margin ROBO would have quoted at inception is a third of the cash the trade actually needed. Even after the VM arrives, the package has absorbed \$624,000 of net cash on the shock: hedged on the P&L, naked on the wire.

*As liquidity planning,* the \$4.2mm Larkspur reservation sat idle in the wrong place for 23 days. Had the loan settled on Day 5 instead of Day 23, the desk would have needed \$9.92mm that day. A settlement date that is a random variable (§21.2.2) belongs in the stress, not in a footnote.

The general rule is the one the spec implements. With signed cash flows $c_k$ ordered by day and intraday sequence, the buffer a desk must hold is the worst cumulative shortfall,

$$
B = \max_k\left(-\sum_{j \le k} c_j\right)^{+},
$$

and the stress is a distribution over the haircut, the IM rate, the price drop and the settlement lags, not a single path. Ines's version: "The pot was good. You nearly left the table anyway, because your chips arrive one hand after the bet is due."

**Used in:** §24.1 (the same trade, priced); §24.4 (its carry and band); §28.5 (days-to-liquidate and the runway); §28.9 (the 13-week model as a PM dashboard: this ledger is its plumbing row).

## D.9 The Plumbing Ledger in Code

### Specification for AI Implementation

**The Spec You Hand the Robot.** *Vague version:* "Tell me how much margin the basis trade needs." *What ROBO built:* the sum of the haircut and the CDS IM on the trade date, \$1.94mm, reported to the cent and computed for a world in which haircuts never change and variation margin arrives before it is needed. *Precise version:* build `plumbing.py` with the functions below. Every cash amount is in dollars, every rate an annual decimal, every price in points per 100 of face, every spread a decimal (0.0370, not 370). Day counts: 30/360 for bond accrual, ACT/360 for repo and CDS premium. Settlement offsets are business days on the instrument's own holiday calendar (SIFMA for bonds, NYSE for ETF shares). The buffer is computed from flows ordered by `(day, intraday_order)`, with VM arriving on the next business day.

**Data schema.**

| Record | Fields (type, unit) |
| :--- | :--- |
| `Trade` | `trade_id` (str); `instrument` in {bond, loan, cds, cdx, etf, repo}; `trade_date` (date); `settle_lag_bd` (int, or a distribution for loans); `notional` (float, \$); `price_pts` (float); `coupon` (float, decimal); `accrued_days` (int); `haircut` (float, decimal); `im_rate` (float, decimal of notional); `index_factor` (float, $(0,1]$) |
| `CashFlow` | `day` (int, business days from Day 0); `order` (int, intraday sequence); `cash` (float, \$, + in); `label` (str) |
| `EventQuestion` | `question_date` (date); `kind` in {credit, succession}; `final_list_prices` (list of float, points) |

**Edge cases and guards.** Reject negative day counts, haircuts outside $[0,1)$ and index factors outside $(0,1]$. If the price drop meets or exceeds the haircut, the forced-sale fraction is 1 (the dealer liquidates). Successor thresholds are strict at 25% and inclusive at 75%; compare with the floats as given and never round the shares first. An empty Final List returns a payout of zero, which is the stylized orphan, not a bug. Treat a loan's settlement lag as a draw, not a constant. Never net the jump-to-default IM line against spread hedges.

<!-- EXPLAIN: Listing D.1 -->
> **Code Companion: Listing D.1.** Accrued interest as a fraction of face (coupon an annual decimal, days on 30/360). The full python listing is in [Appendix F, Listing D.1](#code-d-1).

**What to check before trusting it.** The upfront is first-order; production uses the ISDA Standard Model (§24.2). The CDS-points-per-bond-point ratio of 1.44 is read off one illustrative path; estimate it from the desk's own history, and expect it to fall as the bond approaches recovery. The repo call ignores accrued repo interest and the dealer's minimum transfer amount.

**Used in:** §20.7 (the arbitrage monitor's settlement-gap input); §24.4 (basis package carry and stress); §28.5 (LVaR and runway); Chapter 27 (the security master's settlement-calendar fields).

## D.10 Desk Debrief

- **The hedge lives on the P&L; the margin call lives on the wire.** Size liquidity to the worst cumulative intraday cash need under stressed haircuts and IM, never to inception margin: in §D.8 they differ by a factor of three. (Law 11)
- **Every basis is a price difference plus a financing difference.** Name the funding leg (Table D.5) before you call anything riskless; an overnight funding leg against a six-month convergence is a short option on the repo desk. (Law 10)
- **A haircut is a forced-selling schedule.** A move from $h$ to $h'$ sells $1 - h/h'$ of the book before any price moves, and the buyers are the people who raised it. (Law 15)
- **The CCP charges you for effective breadth.** Netted IM scales with $\sqrt{(1+(n-1)\rho)/n}$; the jump-to-default line is charged once and never netted against spread hedges. (Laws 2 and 6)
- **Under SNAC, only Bankruptcy and Failure to Pay pay.** An LMT that keeps paying coupons moves value without triggering the swap, which is why there are two default rates. (Law 7)
- **The swap pays par minus the cheapest thing on the Final List, and liens don't count.** The excluded lender's loan is usually still deliverable and often the cheapest. (Law 8)
- **Successor thresholds are cliffs at 25% and 75%, and repaid debt orphans the swap.** Read the debt map before the spread. (Law 8)
- **Every date in the Trend Watch is a definitional break.** Flag it in the event calendar or your model is fitting the rulebook. (Law 11)

**Used in:** App E (Laws 2, 6, 7, 8, 10, 11, 15); front matter, *Tape to Your Monitor* (Part-level bullets).

### The Spec You Hand the Robot

"Build `plumbing.py`: a cash-and-collateral ledger for bonds, loans, CDS, index CDS, ETF shares and repo. Inputs are `Trade` records and stress parameters (haircut path, IM path, price shock, loan settlement-lag distribution); outputs are the signed `CashFlow` list ordered by business day and intraday sequence, the worst cumulative shortfall $B$, and its seeded stress distribution. Use 30/360 for bond accrual and ACT/360 for repo and CDS premium; dirty prices to the settlement date; points upfront net of the accrued rebate at T+3; VM on the next business day; the forced-sale fraction $1 - (h-u)/(h'(1-u))$, capped at 1; backstops of 60 and 90 days; successor thresholds strict at 25% and inclusive at 75%; payout of par minus the cheapest Final List price. Reject negative day counts, haircuts outside $[0,1)$ and index factors outside $(0,1]$. Never assume settlement date equals trade date."

## D.11 Exercises

1. *The Columbus Day basket.* A \$40mm in-kind ETF redemption delivers bonds that settle on Tuesday (SIFMA closed Monday) against ETF shares that settle on Monday. At a 5% funding rate, what does the one-day gap cost, and who pays it? (Answer: about \$5,556, paid by whoever delivers cash first.)
2. *The patient margin call.* A HY book runs at an 8% haircut. The dealer moves it to 20% and prices fall 3%. What fraction must be sold? (Answer: $1 - 0.05/(0.20 \times 0.97) = 74.2\%$.) Now compute it again with the price drop at 9%.
3. *Index arithmetic.* You are long \$50mm of CDX HY protection at an index factor of 0.97. A constituent defaults, and its auction prints at 30. What do you receive, what is the new factor, and on what notional do you now pay coupon? (Answer: \$350,000; 0.96; \$48mm.)
4. *Successors.* Entities A and B each assume 26% of a reference entity's bonds and loans, and the original keeps 48%. How many swaps do you own afterwards, and on what notionals? Now move 23 points from the original to A, and explain why your swap count falls.
5. *Kaz's hedge.* Kaz proposes buying CDS on a counterparty that keeps failing to deliver Treasuries to the desk. Explain in two sentences why a settlement fail is not a Failure to Pay, and name the price that actually compensates the desk for the fail (§D.1, eq. 22.9).

**Used in:** §D.1–D.7 (each exercise checks against a function in §D.9); §24.10 (the basis exercises these extend).

### Deep-Dive Resource Graph

**Podcasts**
- ISDA podcast, "Episode 60: Modelling Margin" (2026-10-01). https://www.isda.org/2026/10/01/episode-60-modelling-margin/
- *Odd Lots* (Bloomberg), "How The Crisis Nearly Blew Up One Of The World's Safest Trades," with Josh Younger (2020-03-26): the funding leg of a basis in a dash for cash. https://omny.fm/shows/odd-lots/how-the-crisis-nearly-blew-up-one-of-the-world-s-s
- *Cloud 9fin*, "Distressed Diaries — Ardagh CDS and the empty glass paradox" (2026-01-21): outstanding principal and the Final List. https://share.transistor.fm/s/903a348d
- *Cloud 9fin*, "Bringing loan data from fax to the future" (2025-03-06): why loans settle slowly. https://share.transistor.fm/s/14a1ade2

**Practitioner Writing**
- Credit Derivatives Determinations Committees: decisions, votes, Final Lists and auction terms. https://www.cdsdeterminationscommittees.org
- European Commission, "A shorter settlement cycle" (2025-07-03). https://finance.ec.europa.eu/news/shorter-settlement-cycle-2025-07-03_en
- BNP Paribas Securities Services, "T+1 in Europe: what's next for the EU, the UK and Switzerland?" https://securities.cib.bnpparibas/t1-settlement-ready/
- Federal Reserve Bank of New York, tri-party repo margin and haircut statistics. https://www.newyorkfed.org/tripartyrepo/margin_data
- Matt Levine, *Money Stuff* (Bloomberg Opinion), columns on manufactured credit events and Hovnanian, 2018 (no link verified).

**Academic Papers**
- Copeland, Martin and Walker (2014), *Repo Runs: Evidence from the Tri-Party Repo Market*, Journal of Finance.
- Gorton and Metrick (2012), *Securitized Banking and the Run on Repo*, Journal of Financial Economics.
- Duffie and Zhu (2011), *Does a Central Clearing Counterparty Reduce Counterparty Risk?*, Review of Asset Pricing Studies.
- Chernov, Gorbenko and Makarov (2013), *CDS Auctions*, Review of Financial Studies.
- Du and Zhu (2017), *Are CDS Auctions Biased and Inefficient?*, Journal of Finance.
- CPMI–IOSCO (2012), *Principles for Financial Market Infrastructures*; BCBS–CPMI–IOSCO (2022), *Review of margining practices*.

**Data & Code**
- SEC Release No. 34-72701 (ICE Clear Credit's adoption of the 2014 Definitions). https://www.sec.gov/file/rel-no-34-72701
- ISDA (Definitions, protocols, SIMM). https://www.isda.org
- DTCC (settlement statistics, the Trade Information Warehouse). https://www.dtcc.com
- FINRA (Uniform Practice Code, TRACE). https://www.finra.org
- LSTA (loan settlement and delayed-compensation documents). https://www.lsta.org
- CDS public data and TRACE fields: App B §B.1 and §B.13.

<!-- STATUS: COMPLETE -->
