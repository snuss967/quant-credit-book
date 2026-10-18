# Appendix A: Notation, Units & Conventions

This appendix is the reader-facing edition of the book's internal style sheet. Every chapter uses the symbols below with the meanings, units, and conventions below. When a chapter has to deviate, it says so in a sentence at the point of deviation. The appendix is kept in sync with the house style bible every edition; if a symbol appears in a chapter and not here, one of the two is wrong, and it is probably the chapter.

Mags's advice applies to notation as much as to bonds: price is what you pay, and units are what you get, eventually, after the debugging.

## A.1 Three questions to ask of every symbol

Most errors in quantitative credit are not errors of mathematics. They are errors of units and conventions, and they survive because a number with the wrong units looks exactly like a number with the right ones. Before you use any quantity in this book, in a formula or in a specification handed to ROBO, ask:

1. **Which measure?** Physical ($\mathbb{P}$) or risk-neutral ($\mathbb{Q}$)? A default intensity backed out of CDS is a $\mathbb{Q}$ quantity and is systematically larger than the $\mathbb{P}$ intensity you would estimate from default history. Mixing them is the most common single bug in credit models, and it is invisible until a stress test.
2. **Which units?** Decimal, percent, basis points, points of par, years, dollars? A spread of 350 basis points is $0.035$ in a formula and "350bp" in prose, never "3.5" and never "0.35%" unless you want ROBO to build a desk that quotes bonds at a spread of 35,000bp.
3. **Which convention?** Clean or dirty price? Recovery of face, market value, or Treasury? Excess return over Treasuries or over swaps? Annualized or not? Each has a correct answer in context, and the context must be written down.

ROBO asks all three questions every time. It just does not tell you that it asked, and it picks an answer. Tell it the answer first.

## A.2 The master notation table

Typical magnitudes are illustrative and regime-dependent; they are here so you can sanity-check an output, not so you can cite them.

| Symbol | Meaning | Units | Typical magnitude (illustrative) | Notes |
| :--- | :--- | :--- | :--- | :--- |
| $\mathbb{P}$, $\mathbb{Q}$ | Physical and risk-neutral probability measures | none | | Every expectation names its measure: $\mathbb{E}^{\mathbb{Q}}[\cdot]$. |
| $\mathcal{F}_t$ | Filtration: information available at time $t$ | none | | The conditioning set for every price. |
| $\mathbb{E}[\cdot]$ | Expectation | as its argument | | Never written "EV"; that is enterprise value. |
| $t$, $T$ | Time, maturity | years | $T - t$ of $0.25$ to $10$ | Day count stated when it matters (§A.4). |
| $V_t$ | Firm asset value (structural models) | \$ or \$mm | | Unobservable; inferred from $E_t$ and $\sigma_E$. |
| $F$ | Face value of debt (structural models) | \$ or \$mm | | Never $D$, which is duration. Unsubscripted $F$ only. |
| $E_t$ | Equity market value | \$ or \$mm | | |
| $\sigma_V$, $\sigma_E$ | Asset and equity volatility | annualized, decimal | $\sigma_E$ of $0.25$ to $0.60$ for HY issuers; $\sigma_V$ lower by leverage | Equity vol is not asset vol; see Chapters 6 and 23. |
| $r$, $r_t$ | Risk-free rate, short rate | annualized decimal, continuously compounded | $0.03$ to $0.055$ (2023–2026, approx.) | Stated if discretely compounded. |
| $\tau$ | Default time | years | | Never time to maturity; that is $T - t$. |
| $\lambda_t$ | Default intensity (hazard rate) | per year | IG $0.001$ to $0.01$; single-B $0.03$ to $0.08$; CCC $0.10$ to $0.30$ and up, under $\mathbb{Q}$ | Reserved for default. Order arrival uses $\Lambda$. |
| $S(t)$ | Survival probability, $\mathbb{Q}(\tau > t)$ | probability | $e^{-\lambda t}$ under constant intensity | $S^{\mathbb{P}}(t)$ for physical. Parentheses, not a subscript. |
| $R$, $L = 1 - R$ | Recovery rate, loss given default | fraction of par unless stated | $R = 0.40$ is the senior-unsecured CDS convention | Convention (RFV, RMV, RT) named explicitly (§A.6). |
| $s$ | Credit spread | decimal in formulas, bp in prose | IG $70$ to $150$bp; BB $200$ to $350$bp; B $300$ to $500$bp; CCC $700$ to $1{,}200$bp and up (approx.) | Measure named: OAS, $Z$, G, ASW, or PECS (§A.5). |
| $\text{OAS}$, $Z$ | Option-adjusted spread, Z-spread | bp | | $\text{OAS} \le Z$ for callables. |
| $D^{\text{mod}}$, $D^{\text{spr}}$, $D^{\text{emp}}$ | Modified, spread, and empirical duration | years (per unit of decimal yield) | IG $6$ to $8$; HY $3$ to $5$; $D^{\text{emp}} \ll D^{\text{mod}}$ in HY, near zero or negative for CCC | Chapter 8. |
| $\text{DTS}_i = D^{\text{spr}}_i \cdot s_i$ | Duration times spread | years times bp | IG $7 \times 100 = 700$; HY $4 \times 400 = 1{,}600$ | Spread volatility scales with DTS (Ben Dor). |
| $y$, $y^{\text{TSY}}$ | Yield, Treasury yield | annualized decimal | | Semi-annual bond-equivalent for US corporates unless stated. |
| $P$ | Bond price | per 100 of par, clean unless stated | $0$ to $110$; distressed below $70$ | Defaulted bonds trade flat (§A.5). |
| $S_t$ | Generic mid price or underlying | price units | | Market-making chapters. Subscript, not parentheses. |
| $q$ | Inventory | \$ notional (or units) | plus or minus \$5mm to \$50mm per line | Signed: long positive. |
| $\gamma$ | Risk aversion | inverse price | calibrated to inventory limits | Not the option Greek, which is $\Gamma$. |
| $\Lambda(\delta) = A e^{-k\delta}$ | Order-arrival intensity at quote distance $\delta$ | arrivals per day | $A$ of $0.5$ to $20$ per day per bond | $k$ in inverse distance units; written $k_\Lambda$ if a factor index $k$ is nearby. |
| $\delta$ | Quote distance from mid | price units or bp | | Not the option delta, which is $\Delta$. |
| $r^{\text{res}}$ | Reservation price | price units | | Not $r$, the interest rate. |
| $W_t$, $N_t$ | Brownian motion, Poisson process | | | $N(\cdot)$ with parentheses is the standard normal CDF. |
| $J$ | Jump size on default (price points lost) | points of par | $P - 100R$ | Appears in the $q\lambda J$ term. |
| $F_{k,t}$, $\beta_{i,k}$, $\epsilon_{i,t}$ | Factor return, loading, idiosyncratic return | decimal | | Subscripted $F$ is a factor; unsubscripted $F$ is face. |
| IDO | Idiosyncratic return | decimal or bp | | The residual after rates, carry, and factors. |
| $\text{PRS} \in [0,1]$ | Priming Risk Score | probability | | Chapter 13. |
| $\text{EV}$ | Enterprise value | \$mm | | Restructuring valuation; never expected value. |
| IC, IR, BR | Information coefficient, information ratio, breadth | none | IC $0.02$ to $0.10$; live IR $0.3$ to $1.0$ | Chapter 28; breadth corrected for issuer clustering. |
| $\Sigma$, $\mathbf{w}$ | Covariance matrix, portfolio weights | decimal squared, decimal | | Shrinkage is mandatory for stale bonds (Chapter 19). |
| $h$ | Markout horizon | minutes to days | 5 minutes, 1 hour, 1 day, 5 days | §A.7. |
| $\rho$ | Correlation | none | spread–rate $\rho < 0$ in HY | Chapter 8. |
| $\mathcal{N}(\mu,\sigma^2)$, $N(\cdot)$, $\phi(\cdot)$ | Normal distribution, its CDF, its density | | | Kaz's opening move. |
| $d_1$, $d_2$ | Black–Scholes–Merton arguments | none | | Signs verified in Chapter 6. |

## A.3 Collisions and how the book resolves them

Any symbol set this large collides with itself. The rule is: distinguish by decoration, and say so in the text. The standing resolutions:

- $F$ (face value) versus $F_{k,t}$ (factor return): the factor always carries subscripts.
- $k$ (factor index) versus $k$ (arrival-intensity decay): when both appear in one section, the decay parameter becomes $k_\Lambda$.
- $r$ (rate) versus $r^{\text{res}}$ (reservation price) versus returns: returns are written $\text{TR}$, $\text{XR}$, or $x_{i,t}$ (§A.7); if a chapter borrows $r_{i,t}$ for a return, it moves the rate to $r_f$ for that section and says so.
- $\lambda$ is default intensity, always. Arrivals are $\Lambda$. Kyle's lambda, when it appears in Chapter 18, is $\lambda^{\text{Kyle}}$.
- $D$ is duration, always. Debt face is $F$; debt market value, when needed, is $B_t$.
- $S(t)$ (survival, parentheses) versus $S_t$ (mid price, subscript). When a market-making section needs both, survival is written in full as $S^{\mathbb{Q}}(t)$.
- $\sigma$ with no subscript is the mid-price volatility in price units per square-root year in market-making sections and an annualized decimal in structural sections; each section says which in its first equation.
- $\gamma$ (risk aversion) versus the option gamma, which is $\Gamma$; $\delta$ (quote distance) versus the option delta, which is $\Delta$.
- EV is enterprise value; $\mathbb{E}[\cdot]$ is expectation. "The EV of the trade" is a phrase the book does not use.
- $\tau$ is the default time, never time to maturity (that is $T - t$) and never a transaction-cost parameter.

## A.4 Time, dates, and day counts

$t$ is measured in years everywhere. Converting calendar time into years requires a day-count basis, and the basis depends on the instrument. When a formula mixes instruments, convert each to a year fraction on its own basis and say so. A specification that says "time in years" without a basis is a specification ROBO will fill in with calendar days over 365, which is right for none of the instruments below.

| Instrument | Day count | Coupon or payment | Settlement | Notes |
| :--- | :--- | :--- | :--- | :--- |
| US corporate bonds (fixed) | 30/360 | semi-annual | T+1 (since May 28, 2024; T+2 before) | Quoted clean, settled dirty. |
| US Treasuries | ACT/ACT | semi-annual | T+1 | Benchmark for G-spread and excess returns. |
| CDS (SNAC) | ACT/360 | quarterly on 20 March, June, September, December | T+1, with upfront | Fixed coupon of 100bp (IG) or 500bp (HY); accrued rebated at trade; indices roll in March and September. |
| Leveraged loans | ACT/360 | per interest period (often 1 or 3 months) at term SOFR plus margin, often with a floor | T+7 par, T+20 distressed (LSTA convention; delayed compensation thereafter) | Chapter 21. |
| Money market, repo | ACT/360 | at maturity | T+0 or T+1 | The funding leg of the basis. |
| Equity options | calendar days over 365 for expiry; 252 trading days for volatility | | T+1 | Chapter 23. |

Calendar conventions the restructuring chapters rely on: Chapter 11 deadlines run in calendar days from the petition date, with the debtor's exclusive period to file a plan at 120 days and to solicit acceptances at 180 days, each extendable by the court to a cap of 18 and 20 months respectively. Credit-agreement test dates are fiscal-quarter ends, and the quarter that matters for basket capacity is the most recently ended one for which financial statements have been delivered, which is rarely the one you were thinking of.

## A.5 Prices, yields, and spreads

**Price.** Per 100 of par. One point is one percent of par, or \$10,000 per \$1 million of face. The integer part of a price is its "handle." Bonds are quoted clean (excluding accrued interest) and settle dirty (clean plus accrued). Bonds in default trade flat: no accrued interest is added, and the price embeds whatever claim to accrued the holder has. Loans quote on price per 100 plus a margin over the reference rate.

**Yield.** US corporates quote a semi-annual bond-equivalent yield; formulas in this book use continuous compounding unless they say otherwise. The conversion is $r^{\text{cc}} = 2 \ln\!\left(1 + \tfrac{y}{2}\right)$. Callable bonds quote yield-to-worst, the lowest yield across all call and maturity dates on the assumption that the issuer exercises against you, which it will.

**Basis points.** 1bp $= 0.01\% = 0.0001$. Spreads are written in basis points in prose and tables and in decimal in formulas, and code carries the unit in the variable name (`spread_bp`, `spread_dec`). "Spreads widened 25bp," never "0.25%."

**Dollar sensitivities.** DV01 is the dollar change in a position's value for a one-basis-point move in yield; CS01 is the same for spread. For a bullet bond,

$$\text{DV01} \approx D^{\text{mod}} \times \frac{P}{100} \times \text{Face} \times 0.0001 .$$

A \$10 million position at a price of 95 with $D^{\text{mod}} = 6$ has a DV01 of about $6 \times 0.95 \times 10{,}000{,}000 \times 0.0001 = 5{,}700$ dollars per basis point *(illustrative)*.

**Spread measures.** "The spread" is at least five different numbers, and the basis between a bond and its CDS depends on which one you chose.

| Measure | Definition | Use | Trap |
| :--- | :--- | :--- | :--- |
| G-spread | Yield minus the interpolated Treasury yield at the same maturity | Quick IG comparisons | Ignores curve shape and coupon. |
| I-spread | Yield minus the interpolated swap rate | Swap-funded investors | The swap curve (SOFR) choice matters. |
| Z-spread ($Z$) | Constant spread added to every zero rate on a discount curve so that discounted cash flows equal the dirty price | Bullet bonds; the standard input to a basis | Name the curve (Treasury or swap). Ignores embedded options. |
| OAS | Z-spread after removing option value with an interest-rate model | Callable and putable bonds; HY index analytics | Model-dependent; $\text{OAS} \le Z$ for callables, the gap being option cost in bp. |
| ASW (par-par) | Margin over floating such that a package of the bond bought at par plus a coupon-for-floating swap is worth zero | Funded investors; basis against CDS | Diverges from $Z$ when price is far from par; a market-value variant exists. |
| PECS | The flat CDS spread whose implied survival curve, with the CDS recovery assumption, reprices the bond | The right bond spread for a CDS basis | Depends on the assumed recovery. |
| Discount margin | For floaters and loans, the spread over the reference rate that equates PV to price, assuming forwards equal the current rate | Loans and FRNs | State whether the floor is priced. |
| CDS quoted spread | A quoting convention converted to an upfront payment by the ISDA Standard Model under a flat hazard rate and a fixed recovery | Quoting | Not the par spread of a term-structure model; the upfront is the traded number. |

The book's **basis** is $\text{basis} = s^{\text{CDS}} - s^{\text{bond}}$, with the bond measure named ($Z$ or PECS). Negative basis means the bond is cheap relative to protection: buy the bond, buy protection, and discover what funding costs in a crisis (Chapter 24).

**Price versus spread quoting.** Bonds trade on spread while a spread is informative and on price once it is not. The common rule of thumb is that a spread above roughly 1,000bp, or a price in the low 80s or below, means the bond is "trading on price" *(convention; approximate)*, because the yield-to-maturity arithmetic assumes the coupons will be paid, and at that point nobody believes it.

**Spread duration versus modified duration.** $D^{\text{spr}}$ is the sensitivity of price to spread; $D^{\text{mod}}$ to yield. For fixed-rate bullets they are nearly equal. For floaters, $D^{\text{mod}}$ is roughly the time to the next reset while $D^{\text{spr}}$ is roughly the remaining life, which is why loans have almost no rate risk and plenty of credit risk.

**DTS.** $\text{DTS} = D^{\text{spr}} \times s$ with $s$ in basis points, in units of years times bp. Its justification is empirical: relative spread changes have similar volatility across bonds, so absolute excess-return volatility is proportional to DTS. A bond with DTS 1,600 is about twice as risky as one with DTS 800, regardless of which has the longer duration (Chapter 8).

## A.6 Recovery conventions

Recovery is a rate, a convention, and an argument, in that order.

**Symbol.** $R$ is the recovery rate and $L = 1 - R$ the loss given default, both as fractions of the relevant base. The base is the convention:

- **Recovery of face value (RFV).** On default the holder receives $R$ times face (plus, in some setups, accrued). This is how CDS settle (the auction yields a price per 100 of par) and how the book prices bonds unless it says otherwise. It makes a bond's default payoff independent of its coupon and maturity, which is realistic for claims in bankruptcy.
- **Recovery of market value (RMV).** On default the holder receives $R$ times the bond's market value an instant before default (Duffie–Singleton). It produces the elegant risky discount rate $r + \lambda L$, which lets you price defaultable cash flows on a spread-adjusted curve as if they were riskless. "Forty percent of whatever it was worth a second ago" is not what happens in a courtroom, but the mathematics is clean enough that it is worth knowing when the approximation is harmless (Chapter 6).
- **Recovery of Treasury (RT).** On default the holder receives $R$ times the value of an otherwise identical riskless bond (Jarrow–Turnbull). Useful in rating-transition models; rare on a desk.

**Market conventions.** The ISDA Standard Model converts quoted CDS spreads to upfront payments using assumed recoveries of 40 percent for senior unsecured and 20 percent for subordinated North American corporate reference entities. These are quoting conventions, not forecasts, and a desk that treats 40 percent as an expected recovery for a CCC retailer with a drop-down in progress has confused a unit with a fact.

**Realized recoveries.** Two different measurements share the name: the trading price of the defaulted instrument about 30 days after default, and the ultimate recovery at emergence, discounted back to the default date. They can differ substantially and in either direction. Any cited recovery statistic in this book names which one it is. Recoveries fall with seniority and collateral (first-lien loans at the top, subordinated bonds at the bottom); the sourced numbers and their dispersion are in Chapter 5, where recovery is modeled as a Beta distribution with mass points at zero and one.

**Physical versus risk-neutral.** A recovery backed out of market prices is a $\mathbb{Q}$ quantity. The credit triangle $s \approx \lambda(1 - R)$ shows why this matters: one observed spread is consistent with infinitely many $(\lambda, R)$ pairs, and the market's split between them is not identified from the spread alone. Recovery locks exist to trade the split directly.

**Recovery in the LMT era.** Recovery is now a property of the instrument and the transaction, not the issuer. A priming transaction changes $R$ for left-behind lenders without any default occurring, which is why the default and recovery distributions of Chapter 5 are re-estimated under the regime shifts of Chapter 14.

## A.7 Return conventions

- **Total return** ($\text{TR}$): price change plus coupon income plus reinvestment over the period, per unit of starting dirty price, in decimal.
- **Excess return** ($\text{XR}$): total return minus the return of a duration-matched Treasury portfolio over the same period. Matching is ideally by key-rate duration, not by a single number. This is the book's default meaning of "excess return" in Part III. Excess return over swaps is used for asset-swap-based analysis and is named as such.
- **Spread return approximation:** $\text{XR} \approx -D^{\text{spr}}\,\Delta s + \tfrac{1}{2} C^{\text{spr}} (\Delta s)^2 + \text{carry}$, with $s$ in decimal and $C^{\text{spr}}$ the spread convexity. **OAS carry** is $\text{OAS} \times \Delta t$; **yield carry** includes the Treasury component; **roll-down** is reported separately.
- **Simple versus log returns:** simple returns aggregate across positions; log returns aggregate across time. Each chapter says which it is using.
- **Annualization:** means by 252 (daily) or 12 (monthly); volatilities by $\sqrt{252}$ or $\sqrt{12}$. Bonds with stale prices understate short-horizon volatility and correlation, which is why Chapter 8 uses lag-sum betas and Chapter 19 shrinks covariances.
- **Markout:** $\text{markout}_h = \text{side} \times \left(m_{t+h} - P_{\text{trade}}\right)$, with $\text{side} = +1$ when the desk bought and $-1$ when it sold, $m$ the composite mid, and $h$ the horizon (5 minutes, 1 hour, 1 day, 5 days). Reported in bp of price or bp of spread, stated which. A persistently negative average markout on a counterparty's flow is the definition of toxic flow. Ines calls the markout log the hand history and reads it before she reads anything else.
- **Sharpe ratio and information ratio:** annualized; Sharpe in excess of funding, IR relative to the named benchmark; always reported with the sample length, and in Chapter 7 with the deflated version that accounts for the number of strategies tried.
- **IDO:** the residual $\epsilon_{i,t}$ after removing rates, carry, and factor exposures (Chapter 8). Reported in bp per period. The desk's unit of alpha.
- **DTS-scaled returns:** $\text{XR} / \text{DTS}$, making bonds of different risk comparable.
- **In code:** returns and spreads are decimals inside arrays; conversion to bp and percent happens at the input and output boundaries; variable names carry units.

## A.8 Sizes, signs, and desk arithmetic

- **Units of size.** \$mm is millions and \$bn is billions. Face (notional) and market value are different numbers: \$10mm face at a price of 60 is \$6mm of market value and \$10mm of claim.
- **Risk is reported four ways:** DV01 (rates), CS01 (spread), DTS-weighted market value (proportional spread risk), and jump-to-default, $\text{JTD} = \text{MV} - R \times \text{Face}$ for a long position, the loss if the issuer defaults now.
- **Sign conventions.** Long credit means long the bond or short protection; the protection buyer pays the premium and is short credit. Spreads up means prices down means long credit loses. In a return decomposition the rate term is $-D\,\Delta y$; a plus sign there is the most common bug in a first implementation.
- **Rounding.** Bond prices in decimals (historically eighths); spreads to the basis point; CDS upfronts to a hundredth of a point.
- **TRACE dissemination.** Prints above the dissemination caps display with a capped size; the caps and reporting times have changed over the period this book covers and are detailed in Chapters 18 and 22.

## A.9 Glossary of desk and restructuring terms

One line each, alphabetical, with a joke where the term can bear one.

- **363 sale.** A sale of a debtor's assets under Section 363 of the Bankruptcy Code, outside the ordinary course and "free and clear" of liens, usually with a stalking-horse bidder and an auction. Faster than a plan, which is why buyers like it and some creditors do not.
- **503(b)(9) claim.** An administrative-expense priority claim for the value of goods (not services) a debtor received in the 20 days before filing. The one time in bankruptcy when being a late supplier is good news.
- **Absolute priority rule.** Under Section 1129(b), a plan can be confirmed over a rejecting class only if no class junior to it receives or retains anything until that class is paid in full. It binds in cram-down against a rejecting class, not in every plan: where every affected class votes yes, a tip to old equity or a gift from a senior class is routine, which squares with Franks and Torous (Chapter 6, §6.2) finding the rule violated in 78 percent of the bankruptcies they considered. Once a class rejects, the deviation stops being free (*DBSD*, 2d Cir. 2011, refused a senior class's gift to old equity over an unsecured objector). Honored in principle, negotiated in practice, and the reason the fulcrum matters.
- **Ad hoc group.** An informal group of creditors holding the same instrument who hire common counsel to negotiate collectively. Disclosed in Rule 2019 statements. Speaks in unison, mostly in footnotes.
- **Adequate protection.** Compensation a secured creditor receives in bankruptcy for the diminution in value of its collateral while the automatic stay is in effect. "Adequate" is doing a lot of work in that sentence.
- **All-to-all trading.** An electronic protocol in which any participant, not only dealers, can respond to a request for quote. The moment the bazaar got a second set of stalls.
- **Asset swap (ASW).** A package of a fixed-rate bond and an interest-rate swap converting its coupon to floating; the asset swap spread is the margin over the floating rate that makes the package worth par.
- **Authorized participant (AP).** A dealer permitted to create and redeem ETF shares in kind with the fund, exchanging baskets of bonds for creation units. The people who open the sealed boxes.
- **Available Amount basket.** A builder basket for restricted payments and investments whose capacity grows with retained earnings (or a fraction of net income or EBITDA) since closing. Capacity you did not know the sponsor had.
- **Backstop.** A commitment, usually by an ad hoc group, to purchase any portion of a rights offering not taken up by other holders, in exchange for a fee and often a discount. The committed capital is real; so is the fee.
- **Basis (CDS–bond).** The difference between the CDS spread and the bond's spread on a comparable measure (Z, ASW, or PECS). Negative basis: bond cheap to CDS. The trade that works until funding disappears.
- **Blocker.** A covenant provision drafted after a famous transaction to prevent the next one: a J.Crew blocker (restricts transfers of material IP to unrestricted subsidiaries), a Serta blocker (requires pro rata treatment in any uptier), a Chewy blocker (restricts guarantor release via partial equity sales). Named like hurricanes, for the damage.
- **BWIC / OWIC.** Bids (or offers) wanted in competition: a list of bonds or loans put out for auction, typically by a fund or CLO. Every dealer who sees the list learns something, which is the leakage problem.
- **CCC bucket.** The maximum share (commonly 7.5 percent) of a CLO's portfolio that may be rated CCC or below before excess holdings are carried at market value for overcollateralization tests. The reason CLOs sell at the worst time.
- **CDX / iTraxx.** The standardized credit default swap indices for North America (CDX IG, 125 names; CDX HY, 100 names) and Europe (iTraxx Main and Crossover), rolling to a new series each March and September. The most liquid thing in credit; the hedge everyone uses and nobody loves.
- **Change-of-control (CoC) put.** The bondholder's right to put bonds to the issuer at 101 upon a change of control, often coupled with a ratings-decline trigger. An option that pays only if the deal closes and the trigger is met.
- **Cheapest-to-deliver (CTD).** In CDS settlement, the protection buyer's right to deliver (or the auction's tendency to price) the lowest-priced qualifying obligation. A free option embedded in a product sold as insurance.
- **Clean / dirty price.** Clean excludes accrued interest; dirty includes it. Bonds are quoted clean and settled dirty. Defaulted bonds trade flat.
- **CLO.** Collateralized loan obligation: a vehicle that buys leveraged loans and issues tranches from AAA to equity, managed subject to coverage and quality tests during a reinvestment period. The largest buyer of loans and a mechanical seller under stress.
- **Composite price.** A vendor's estimate of a bond's current mid built from TRACE prints, dealer quotes, and models. Several named products exist; the book calls them composites. Not a price; a prior.
- **Cooperation agreement.** An agreement among lenders to act together and not to participate in a non-pro-rata transaction without the group. Increments the counter.
- **Covenant-lite.** A loan without financial maintenance covenants, relying on incurrence tests only. "Lite" refers to the lender's protection, not the document's weight.
- **Cram-down.** Confirmation of a plan over the objection of an impaired class under Section 1129(b), subject to the absolute priority rule and the fair-and-equitable test. Usually aimed down the stack at a junior class; aimed the other way, it is a cram-up.
- **Cram-up.** Confirmation of a plan over the objection of a senior secured class, either by reinstating its debt under Section 1124(2) (the class is then unimpaired and does not vote) or through Section 1129(b) by handing it replacement notes at a rate it calls too low. *Charter* (2009) is the reinstatement case; *Momentive* (2d Cir. 2017) is the rate case, where the court looked first for an efficient market rate and fell back on the *Till* formula rate only when no such market exists. The mechanism that turns cheap legacy debt into an asset of the estate. Somebody does get crammed up.
- **Creation unit.** The block size (often tens of thousands of shares) in which an ETF's shares are created or redeemed by authorized participants.
- **Credit event.** The ISDA-defined triggers for CDS: bankruptcy, failure to pay, and (where applicable) restructuring, plus others for sovereigns. Determined by a Determinations Committee, and the subject of more creative lawyering than the drafters anticipated.
- **Cross-default / cross-acceleration.** A default under one debt instrument triggers a default under another (cross-default), or does so only once the first debt is actually accelerated (cross-acceleration). The difference is a quarter of negotiation.
- **Custom basket.** A creation or redemption basket that differs from a pro rata slice of the fund, permitted under the 2019 ETF rule. How bond ETFs stay liquid when their bonds are not.
- **D2C / D2D.** Dealer-to-client and dealer-to-dealer trading. TRACE flags which is which; the information content differs.
- **Debtor-in-possession (DIP) financing.** New money lent to a debtor in bankruptcy with super-priority status, often with liens priming prepetition lenders. The first-mover advantage in Chapter 11.
- **DIP roll-up.** A DIP structured so that prepetition loans held by the DIP lenders are converted into (rolled into) the super-priority DIP. The lenders who provide new money get their old money promoted.
- **Discount margin.** For a floating-rate instrument, the spread over the reference rate that equates the present value of cash flows to the price, assuming forward rates equal the current rate.
- **Distressed exchange.** An out-of-court transaction in which creditors accept new securities or cash worth less than the original claim, to avoid a bankruptcy. Counted as a default by the rating agencies; counted as a feature by the sponsor.
- **Double-dip.** A structure that gives new lenders two claims against the same credit group: one direct (or via a guarantee) and one via an intercompany loan from the borrowing entity. Two tickets, one seat.
- **Drop-down.** The transfer of assets (classically intellectual property) to an unrestricted subsidiary outside the collateral package, which then raises new debt against them. J.Crew, 2016. The door was in the blueprint.
- **DTS (Duration Times Spread).** Spread duration multiplied by spread, in years times bp. The best single measure of a bond's credit risk, because spread volatility scales with spread level.
- **DV01 / CS01.** The dollar change in a position for a one-basis-point move in yield (DV01) or credit spread (CS01).
- **EBITDA add-backs.** Adjustments to EBITDA permitted by the credit agreement, including projected cost savings and synergies, often capped at a percentage of EBITDA, and often not. Mags's least favorite word is "adjusted."
- **Exclusivity period.** The window (initially 120 days from the petition date to file a plan and 180 days to solicit acceptances, extendable up to 18 and 20 months) during which only the debtor may propose a plan. The clock the whole case runs on.
- **Fallen angel / rising star.** A bond downgraded from investment grade to high yield (fallen angel) or upgraded the other way (rising star). Forced-seller flow in both directions.
- **First-day motions.** The motions a debtor files at the start of a case to keep operating: cash management, wages, critical vendors, DIP approval. The first signal of who is in charge.
- **Fulcrum security.** The class in the capital structure at which value runs out, which therefore receives most of the reorganized equity. Not a physics thing, Kaz.
- **General unsecured claim (GUC).** A claim with no collateral and no statutory priority; the residual class, usually paid in cents, stock, or litigation-trust interests.
- **Hit rate.** The share of RFQs a dealer wins. A high hit rate is good news until the markouts arrive.
- **IDO.** Idiosyncratic return: what remains of a bond's return after removing rates, carry, and factor exposure. The desk's unit of alpha. IDO or it didn't happen.
- **iNAV.** The intraday indicative value of an ETF, published periodically during the trading day from the fund's basket. A number that is correct about a basket nobody can trade.
- **Impaired class.** A class of claims whose legal rights are altered by the plan; only impaired classes vote. Being unimpaired sounds nice and means you have no say.
- **Incurrence vs. maintenance covenant.** A maintenance covenant must be satisfied at every test date; an incurrence covenant is tested only when the borrower takes an action (incurs debt, pays a dividend). Covenant-lite means the maintenance covenants went away.
- **Investment grade / high yield.** Rated Baa3/BBB- or better by the agencies, or not. The boundary with the most forced sellers on either side.
- **J.Crew trapdoor.** The combination of investment baskets that allowed J.Crew in 2016 to move intellectual property into an unrestricted subsidiary and borrow against it. Now a common noun.
- **Jump-to-default (JTD).** The loss a position suffers if the issuer defaults immediately: market value minus recovery times face. The risk that no diffusion model sees coming.
- **Key-rate duration.** The sensitivity of price to a move in one maturity point of the yield curve, holding the others fixed. The thing a "duration-matched" hedge usually is not.
- **Liability management transaction (LMT).** An out-of-court transaction (uptier, drop-down, double-dip, exchange) that changes the priority or collateral of existing debt, typically with the consent of a majority but not all lenders. The genus, not the species.
- **Liquidity cost score (LCS).** A bond-level estimate of round-trip transaction cost as a fraction of price, built from quotes and trades (Barclays methodology; Ben Dor). The number that turns paper alpha into real alpha, or does not.
- **Markout.** The change in a composite mid after a trade, signed by the dealer's side, at a fixed horizon. The hand history: it tells you whether the counterparty knew something.
- **Most-favored-nation (MFN).** A provision requiring that if the borrower issues new pari passu debt at a wider spread, existing lenders' spread is raised to match, often subject to a cushion and a sunset. A spread floor with an expiry date.
- **NAV.** Net asset value of a fund per share, struck once a day from the fund's marks; for bond ETFs, usually a bid-side valuation.
- **Negative pledge.** A covenant barring the borrower from granting liens to others without equally securing the covenanted creditor. Plain-vanilla bonds have them; the exceptions are where the structuring happens.
- **OAS (option-adjusted spread).** The constant spread over the discount curve that reprices the bond after accounting for embedded options under an interest-rate model.
- **OC / IC tests.** Overcollateralization and interest-coverage tests in a CLO; failing one diverts cash flows from junior tranches to pay down senior notes. The automatic deleveraging that makes CLOs sell loans into weakness.
- **Open market purchase.** The exception in many credit agreements allowing a borrower to buy back loans from individual lenders without a pro rata offer. The three words on which the Serta uptier rested; the Fifth Circuit disagreed on the last day of 2024. The most expensive three words in finance.
- **Orphaned CDS.** A credit default swap whose reference entity no longer has deliverable debt, usually after a refinancing at a different entity, leaving protection that pays nothing on a default that cannot technically occur.
- **Pari passu.** Of equal rank. The thing minority lenders believed they were until the amendment passed.
- **Pari-plus.** A liability management structure in which new debt ranks pari passu with existing debt at the original borrower and also holds an additional claim elsewhere in the group. A double-dip with better branding.
- **PECS (par-equivalent CDS spread).** A bond's spread restated as the flat CDS spread that would reprice it under the CDS survival curve and recovery assumption, so that bond and CDS can be compared directly.
- **PIK (payment-in-kind).** Interest paid by issuing more of the same instrument rather than cash. The borrower's way of saying "later."
- **Plan of reorganization.** The document that specifies how claims are classified, treated, and paid in a Chapter 11 case; confirmed by the court after creditor voting.
- **Portability.** A provision allowing a change of control without triggering the CoC put if a leverage or ratings test is met. A short option bondholders wrote without being asked.
- **Portfolio trade (PT).** A single transaction in which a basket of bonds (often 50 to several hundred lines) is bought or sold at one price with one counterparty, typically a dealer who hedges with ETF creation or redemption. The basket is now the unit of liquidity.
- **Pre-pack / pre-negotiated.** A bankruptcy in which the plan is negotiated (and in a pre-pack, voted) before filing, so that the case lasts weeks instead of years.
- **Priming.** Placing new debt ahead of existing debt in priority or collateral, whether by a DIP, an uptier, or a drop-down. The Priming Risk Score estimates its probability.
- **Priming Risk Score (PRS).** This book's model-based probability, in $[0,1]$, that an issuer executes a priming transaction within a horizon, built from document features, sponsor behavior, and liquidity runway. Defined in Chapter 13.
- **Pro rata sharing.** The requirement that payments and collateral proceeds be shared among lenders in proportion to holdings. A sacred right in most agreements; the thing the uptier is designed to route around.
- **Recovery lock.** A derivative fixing the recovery rate on a reference entity, isolating recovery risk from default-timing risk. Exists because the credit triangle has two unknowns.
- **Reinstatement.** A plan treatment under Section 1124(2) that cures defaults, restores the original maturity, and otherwise leaves the creditor's rights unaltered, so the class is unimpaired and does not vote. The debtor keeps its old coupon in a new market; the lender holds a claim worth that coupon discounted at today's spread, which can be well below par. See cram-up.
- **Reinvestment period.** The years (commonly four to five) during which a CLO manager may reinvest principal proceeds in new loans; after it ends, the vehicle amortizes. The age at which CLOs stop buying.
- **Request for quote (RFQ).** An electronic request to one or more dealers for a price on a specified size, with a response window. The unit of interaction on the modern credit desk; the adverse-selection problem in three seconds.
- **Restricted payments (RP) basket.** Capacity under the credit agreement for dividends, distributions, and certain investments, built from fixed amounts, builder amounts, and ratio-based tests. Where the money leaves.
- **Restricted / unrestricted subsidiary.** Subsidiaries inside the covenant and collateral package (restricted) or designated outside it (unrestricted). Assets that move from one to the other have left the building.
- **Rights offering.** An offering of new equity in a reorganized company to existing claimholders, often at a discount to plan value and usually backstopped. The entry fee for the post-reorg equity.
- **Risky PV01 (RPV01).** The present value of one basis point of CDS premium paid until default or maturity: the survival-weighted annuity. The number that converts a spread into an upfront.
- **Rule 2019 statement.** A disclosure under Federal Rule of Bankruptcy Procedure 2019 by a group or committee representing multiple creditors, listing members and their holdings. The Ad Hoc Group's only unscripted speech.
- **Sacred rights.** Amendments that require the consent of each affected lender rather than a majority: pro rata sharing, payment terms, release of all or substantially all collateral. No priest is involved.
- **SNAC (Standard North American Corporate) contract.** The post-2009 CDS contract with fixed coupons (100 or 500 basis points), standardized dates, and an upfront payment, enabling fungibility and central clearing.
- **Special mandatory redemption (SMR).** A provision requiring the issuer to redeem acquisition-financing bonds, usually at 101, if the acquisition fails to close by a deadline. An option on the deal breaking.
- **Springing lien / springing maturity.** A lien that attaches, or a maturity that accelerates, upon a trigger such as a ratings change or the failure to refinance another tranche by a date. Yes, Kaz, it springs. At you.
- **Succession event.** ISDA rules determining which entity a CDS references after a merger, spin-off, or debt transfer. Where orphaned CDS are born.
- **Toxic flow.** Order flow whose counterparties, on average, know more than the market maker, so that filling it loses money after the fact. Measured by markouts; priced by the adverse-selection penalty.
- **TRACE.** FINRA's Trade Reporting and Compliance Engine, which has disseminated corporate bond transaction prices since 2002. The origin of the dataset, and thus of this book.
- **Uptier.** A transaction in which a majority of lenders amend the agreement to allow new super-priority debt, exchange their holdings into it, and leave non-participating lenders subordinated. Serta, 2020. The floors were reordered overnight.
- **Waterfall.** The ordered allocation of value among claims by priority and collateral, under a plan, a CLO indenture, or an intercreditor agreement. A correct waterfall conserves value; test yours.
- **Yield-to-worst.** The lowest yield across all call and maturity dates for a callable bond, assuming the issuer exercises against you. The yield you should assume.
- **Z-spread.** The constant spread added to every point on a zero-coupon discount curve so that discounted cash flows equal the bond's dirty price.
- **Zero floor.** A minimum level (often zero, sometimes higher) for the reference rate in a floating-rate loan, so the coupon cannot fall below margin plus floor. An interest-rate option the borrower sold without pricing it.

## A.10 The Phrasebook: RSSG to Quant

On his second morning Theo told the desk that "the fulcrum is the seconds," and three people heard three different sentences. Ines heard a position and asked what the short was. Mags heard a recovery, eventually, after the lawyers. Kaz heard a lever and asked, with real interest, whether it was a first-class lever. Nobody misheard him. That was the problem.

Section A.9 defines words; this section translates them. A restructuring banker arrives on a desk already owning a word for almost everything, and most of those words survive the trip with their spelling intact and their meaning turned a few degrees. A false friend is worse than a foreign word, because nobody stops to look it up. "Recovery" still means recovery. It now comes with a measure, a distribution and a quoting convention, and the one you meant is rarely the one on the screen.

Each row reads left to right as one sentence: the banker says this, the desk means that, here is the tool, here is where the book builds it, and here is what moved. Read the last column twice. Symbols follow §A.2, and sections are cited where an idea is built, not everywhere it appears. Seventy-one rows will not cover every word Theo brought in his carry-on, but they cover the ones that cost him money in his first quarter, which is how any good phrasebook chooses.

### A.10.1 Capital structure

Home ground first, because it is where the drift is hardest to hear. You have used every word below correctly a thousand times in a room whose question was *who gets what at the end*. The desk's question is *what is this worth between now and Friday, and what moves it*, and the same words answer it with a probability attached.

| Banker says | Desk says | Formula or tool | Built in | What changes |
| :--- | :--- | :--- | :--- | :--- |
| "The fulcrum" | The class whose recovery moves with value: the tranche with the most jump-to-default per point of enterprise value | $j^\star(V) = \min\{j : K_j > V\}$; expected delta $\pi_j / C_j$ | §12B.6, §12C.2 | A place in the stack becomes a probability per class, and it moves when the DIP primes. |
| "The waterfall" | A strip of call spreads on distributable value | $R_j = \min\{(V - K_{j-1})^+, C_j\} / C_j$ | §12B.6, §12C.9 | One plan value in, one recovery out becomes a density $f_V$ in and a recovery distribution out. |
| "Recovery" | $R$ under $\mathbb{P}$ or $\mathbb{Q}$: a Beta with mass at 0 and 1 | $s \approx \lambda(1 - R)$; Beta regression on lien and collateral | §5.5, §5.5.6, §A.6 | Your number was a $\mathbb{P}$ forecast at emergence. The screen's 40 is a $\mathbb{Q}$ quoting convention, and one spread cannot separate $\lambda$ from $R$. |
| "We're first lien, we're covered" | Seniority as a document variable | Uptier transfer; Priming Risk Score | §13.3, §13.8 | Priority is a state the documents can change after you buy. On 22 June 2020 a non-participating first lien became junior to new money. |
| "Equity cushion" | Distance to default | $\text{DD} = [\ln(V_0/F) + (\mu - \tfrac12\sigma_V^2)T] / (\sigma_V\sqrt{T})$ | §6.4 | Cushion in turns of EBITDA becomes cushion in standard deviations, and asset volatility matters as much as the gap. |
| "Covenant headroom" | Distance to a barrier | Black–Cox first-passage probability | §6.5, §6.5.3 | The covenant you modeled for ninety hours is a barrier. Cov-lite deletes it; an uptier moves it after the fact. |
| "The equity is out of the money" | A call on $V$, with vega | $E_t = V_t N(d_1) - F e^{-r(T-t)} N(d_2)$ | §6.2, §6-B.1, §16.6 | "Worthless" is a price for an option, and in 2021 Hertz's had a vega its shorts had not priced. |
| "It's still a bond" | A short put; below about 80, an equity option that wears a tie | $B_t = F e^{-r(T-t)} - \text{Put}_t$; $D^{\text{emp}} \to 0$ | §6.2, §8.3 | Below the low 80s it trades with the stock, and DTS hedges break. |
| "The DIP" | A package of derivatives with different owners | Fee stack, roll-up transfer, conversion option | §12C.4 | The coupon is the smallest piece; the roll-up moves every attachment point below it. |

### A.10.2 Valuation

Bankers value things once, carefully, as of a date. Desks value things continuously, roughly, over a horizon, and then check whether they were right. Nearly every row below is the same move: a point estimate grows a distribution, and the distribution grows a measure.

| Banker says | Desk says | Formula or tool | Built in | What changes |
| :--- | :--- | :--- | :--- | :--- |
| "Comps" | The factor model; excess spread to peers | $x_{i,t} = \sum_k \beta_{i,k} F_{k,t} + \epsilon_{i,t}$; ESP within peer cells | §9.3.1, §8B.2, §7-B.5 | You picked the peers; the desk fits them monthly. "Cheap to comps" is a residual: cheapness, or information the peers lack (§9.3.4). |
| "Trading levels" | A composite mid: a prior, not a price | Vendor composite; markout against it | §3B.6 (mistake 1), §20.2, §B.8 | Someone's model of where it might trade. Tell a client 92 when the bid is 89½ and they become someone else's client. |
| "Where is it marked?" | An evaluated price, which is a filter | Smoothing model; Dimson betas | §17.2, Law 9 | A mark is a moving average of the truth, and part of a quarterly mark's calm is the averaging. |
| "Six turns of leverage" | A denominator for spread | $\text{SPiDER} = s / (\text{Debt} / \overline{\text{EBITDA}}^{\,\text{LT}})$ | §9.3.2 | Leverage stops being the answer and becomes the unit in which spread is cheap or rich. |
| "Adjusted EBITDA" | A fixed point | Add-back recursion in basket capacity | §25.3.3, §3B.6 (mistake 10) | Add-backs feed capacity, which permits more add-backs. Mags's suspicion of anything called "adjusted" turns out to be a theorem. |
| "Base case" | The $\mathbb{P}$ mean of a survive-or-jump mixture | Carry if it survives, a jump if not | §5.1 | A mixture's mean is a state nobody lives in: the bond survives or jumps, and almost never earns the average. |
| "Downside case" | The left tail: one-day 99% expected shortfall | $\text{ES}_{99}$ on the mixture | §5.1, §8B.6 | A scenario you wrote becomes a tail the model computes, and someone asks why it changed since yesterday. |
| "The market is pricing in" | A $\mathbb{Q}$ quantity, never a forecast | $\lambda^{\mathbb{Q}}$ from CDS; premium ratio $s / (\lambda^{\mathbb{P}} L)$ | §6.3, §6-B.6, Law 4 | The price contains a risk premium. Feed a $\mathbb{Q}$ default probability to a Kelly sheet and it tells you to hold nothing (§3B.6, mistake 7). |
| "Liquidity runway" | A first-passage time, then a hazard covariate | $\hat\tau = \min\{w : C_w < C_{\min}\}$ | §5.1.5, §3.5, §12C.9 | The 13-week model is a hazard rate with a spreadsheet problem. Mags adds that sponsors run out of patience before cash, so it needs a competing risk (§5.6). |
| "The yield" | Yield-to-worst, then one of eight spreads | YTW; $Z$, OAS, ASW, PECS | §4B.6, §4B.7, §A.5 | "The spread" is at least five numbers. Name the measure, or ROBO will choose one. |
| "Plan value" | A negotiated random variable with a date on it | $f_V$; three values of one company | §12C.1, §12C.2, §12C.11 | The valuation fight is the distribution, not noise around it, and the effective date is an input. |
| "We hold to maturity" | A horizon $h$ | $\sigma_V^2(h) = \operatorname{Var}(\mathbb{E}[V \mid \mathcal{F}_{t+h}] - \mathbb{E}[V \mid \mathcal{F}_t])$ | §3.1.3 | The desk never holds to resolution. A lender call inside $h$ is a trapdoor, not a step. |

### A.10.3 Process and documents

Here the ex-banker is the expert in the room, and the translation runs in the flattering direction: the desk wants what you know, in a form a machine can refresh overnight. Kaz has read every row and still suspects a springing lien is seasonal.

| Banker says | Desk says | Formula or tool | Built in | What changes |
| :--- | :--- | :--- | :--- | :--- |
| "What does the credit agreement say?" | A typed program: the definition graph | Reachability and blast radius | §25.1, §25.2 | Theo's favorite question becomes a graph traversal with tests. He is still usually right; now ROBO can be right overnight. |
| "Basket capacity" | Node arithmetic on that graph | Ratio basket, builder basket, add-back fixed point | §25.3 | Ninety hours of reading become a function, rerun on every amendment. |
| "Sacred rights"; "Required Lenders" | Voting thresholds | $\theta$ by action and by class | §12B.3 | Who can change the contract, and who can stop them, become numbers. Kaz still wants to know about the priest. |
| "The lenders" | A holder vector with a blocking threshold | $w_i$; a coalition $S$ wins if $\sum_{i \in S} w_i > \theta$ | §13.4, §25.7 | The room you advised is a coalition game. Rule 2019 filings give the vector, and the pivotal holder is computable. |
| "The co-op" | A commitment device in a repeated game | Payoffs that make defection expensive | §13.5, §14.5 | A signature is priced, not admired: it changes $u^{\text{in}}$, the value of being inside. |
| "The uptier" | A recovery transfer from excluded to participating holders | $u^0 - u^{\text{out}} = \mathbb{E}[\Delta R^{\text{excl}}]$ | §13.3 | A transaction becomes a transfer you can price before it is announced. |
| "The drop-down" | Collateral leakage | Leakage arithmetic; the min-cut | §13.6, §25.4 | Value walks through a door the document left open, and the door has a measurable width. |
| "The blocker" | A feature bit | J.Crew, Serta and Chewy flags; the "open market purchase" token | §3.5, §13.2.1 | Protection becomes a covariate. "Open market purchase" is the most expensive three words in finance, and also a string match. |
| "The amendment" | An event, read as a diff | Versioned documents | §25.5 | Text diffs are blind where it matters. At Windstream the loss lived in one defined term (§25.5.2). |
| "The milestones" | Contract clocks | Event calendar; timed state machine | §3B.4, §12B.5, §12B.7 | A date in an RSA is a feature known in advance, and time itself is a claim with a price. |
| "Cramdown" | A strike the court sets | $P/S = 1 - (y - c)\,a_n(y)$ | §12B.6 | The rate fight is an option on whether $c$ lands near $y$ or near prime plus two. |
| "Change of control" | A compound option: the 101 put | Two-trigger put; portability as a short digital | §15.2, §15.3 | A smoke detector with two licensed inspectors. Portability means you may already have sold it. |
| "The court will decide" | A random variable with timestamps | Ruling as a jump; courts as a regime | §13.9, §14.6, Law 16 | Legal risk becomes a jump with a date, which you can size, which is more than you can do with a judge. |
| "We're restricted" | The information wall, seen from the public side | Wall-crossing, cleansing, the public tape | §3.6.3, §3B.5, §3B.6 (mistake 11) | On a private-side team the reflex is *don't*. On a public desk a public 8-K is information to trade on, and refusing it has a cost. |

### A.10.4 Risk and P&L

At PJT the P&L arrived as a success fee, once, if the plan was confirmed. On the desk it arrives every morning before seven and has to foot. These are the rows where a banker's instinct is closest to a trader's and furthest from a risk manager's.

| Banker says | Desk says | Formula or tool | Built in | What changes |
| :--- | :--- | :--- | :--- | :--- |
| "A \$10mm position" | DTS, then jump-to-default | $\text{DTS} = D^{\text{spr}} \cdot s$ | §8.4, §4B.5, Law 3 | Face is the size of your claim; DTS is the size of your risk. \$10mm of a CCC can carry three times the DTS of \$10mm of a B. |
| "Our exposure" | Four lines: DV01, CS01, DTS and JTD | $\text{JTD} = \text{MV} - R \cdot \text{Face}$ | §A.8, §8B.5, §6-B.5 | The loss if it defaults this afternoon is its own line, and the jump is charged once (Law 6). |
| "We're hedged" | Hedged to which ruler, in which state? | The hedge matrix | §8.6, §3B.6 (mistake 2) | Ten of protection against ten of bonds at 88 is hedged to face, not to the jump. |
| "We made money" | The explain, which foots | Line items with start-of-day betas | §8C.1–§8C.4 | P&L you cannot attribute is a story, and the risk committee does not accept stories. |
| "The thesis worked" | IDO | $\epsilon_{i,t}$ after rates, carry and factor beta | §8.8, Law 1 | IDO or it didn't happen. Until the beta is stripped it is a benchmark with a hat on. |
| "High conviction" | A Kelly fraction with a jump in it | Discrete Kelly with JTD; fractional Kelly | §28.4 | Conviction becomes a size. Fractional Kelly is full Kelly for people with standard errors. |
| "I know this name cold" | Effective breadth, corrected for issuer clustering | $\text{IR} \approx \text{IC}\sqrt{\text{BR}}$ with clustered breadth | §28.2, §3B.6 (mistake 5) | Depth on one name is one bet. In debt the upside stops at par, so concentration is not rewarded. |
| "If I'm wrong I'll get out" | A stop, which is a size | $\text{MV}_{\max} = \text{budget} \times P / (P - R)$ | §8D.5, §28.6 | The stop does not care why P&L moved, and it sets the largest position you may hold. |
| "Double down, it's cheaper" | Exercising the PM option in a drawdown | Payout as a call on P&L | §3B.6 (mistake 6), §28.6 | Averaging down spends the platform's capital on your option; the stop exists to take it away. |

### A.10.5 Execution

The banker's market was a phone call to Steve. The desk's market is a screen that answers in milliseconds and remembers every answer, so getting something done turns into what doing it cost.

| Banker says | Desk says | Formula or tool | Built in | What changes |
| :--- | :--- | :--- | :--- | :--- |
| "Short it" | Borrow the bond, buy CDS protection, short CDX or the ETF, sell the future, or short the stock: each with a cost and a basis | Rebate $= r^{\text{cash}} - \text{fee}$; the six-row menu | §8D.2, §D.3, §24.4 | At PJT "short" was a word in a pitch. Here it is a loan the lender can recall, at a fee that averaged 33 bp and reached 245 bp after a filing (2004–07). |
| "Where's the bid?" | A reservation price, skewed by inventory, plus a markup | $r^{\text{res}} = S_t - q\gamma\sigma^2(T - t)$ | §18.4, Law 5 | A bid is a posterior, not a markup, and winning is information. |
| "Who's the seller?" | The probability that the other side knows more | Glosten–Milgrom $\pi(x)$; shrunken counterparty score | §3.2, §3.3.4 | Curiosity becomes a likelihood ratio, updated on every RFQ. |
| "Did we get a good price?" | A markout at horizon $h$, beta stripped | $\text{markout}_h = \text{side} \times (m_{t+h} - P_{\text{trade}})$ | §3.3, §A.7 | Graded afterward, against the mid. Ines reads this hand history before she reads anything else. |
| "It trades" | A liquidity cost score, days to liquidate, LVaR | Per-line LCS; credit LVaR | §19.3, §28.5 | Liquidity used to be a relationship and is now a variable (§2.10). |
| "Run a sale process" | A BWIC: a first-price auction with a leaky list | Bid shading under leakage | §18.9 | The list leaks, the winner is cursed, and the auction tells everyone what you owned. |
| "Sell them the whole book" | A portfolio trade, priced as one lump | Four-term basket price; eviction | §19.2, §19.6, §19.8 | The dealer prices the basket, finds your best short at line 117, and charges for it. |
| "The ETF is the market" | A wrapper with an arbitrage band | NAV against price; the band with a balance sheet | §20.2, §20.3 | In March 2020 the ETF was the only price in town, and the NAV was the opinion. |

### A.10.6 Relative value

"Long the fulcrum, short the junior" was always a pair; it just never had a borrow fee. A pod lives on the part of a pair that survives the hedge, and Chapter 8-D's Pair Book is where each row below is built, stressed and paid.

| Banker says | Desk says | Formula or tool | Built in | What changes |
| :--- | :--- | :--- | :--- | :--- |
| "Here's my pitch" | The pair ticket: a thesis sentence with a date, the short leg, the ruler, the size and the exit | One row of the Pair Book ledger | §8D.1, §8D.6, §3B.6 (mistake 12) | Forty pages become five lines the platform can read, and the date is the day you agreed in advance to admit you were wrong. |
| "Long the fulcrum, short the junior" | A recovery-weighted pair, jump-neutral by sizing | $N_{\text{2L}} / N_{\text{1L}} = (P_{\text{1L}} - R_{\text{1L}}) / (P_{\text{2L}} - R_{\text{2L}})$ | §3.7, §12B.6, §8D.4 | The instinct is right, but the hedge is for the judge, not the majority: an uptier can swap which leg is senior. |
| "The hedge ratio" | Three rulers that disagree when it matters | Spread duration, DTS, empirical beta | §8D.3, §4B.5 | The alpha is about the size of the ruler error, so choosing the ruler is part of the trade. |
| "Market neutral" | DTS-neutral, which is jump-neutral only on average | The difference of two jump processes | §8D.4, §5.1 | One default on the long can erase decades of convergence. Near default, match on market value. |
| "It's company-specific" | Idio: the residual differential, defined relative to a named factor model | $\epsilon_{A,t} - \epsilon_{B,t}$; residual correlation across the book | §8.8, §9.7 | A missing factor makes a factor bet look like alpha. If the book's residuals correlate, the idio had a common part. |
| "The trade worked" | The capture ratio | $\kappa = \text{net}/\text{idio}$, where net $=$ idio $+$ leak $+$ friction | §8D.6 | Judged on idio, paid on net. Not §11.2's up/down capture, which shares only the name. |
| "Cap structure arb" | CDS against equity through a structural model | CreditGrades delta | §23.2, §23.6 | Single trades lose. On 4 and 5 May 2005 both legs of the GM trade lost, one day each. |
| "The basis" | $s^{\text{CDS}} - s^{\text{bond}}$, with the bond measure named | Funding, cheapest-to-deliver, deliverables | §24.3, §24.4, §24.5 | A negative basis is not free, and the borrow fee and the basis are one variable seen from two sides. |
| "It's crowded" | A borrow fee that is rising | Fee against the share of inventory on loan | §22.6, §9.10 | Credit crowding has no tape. The fee is the only gauge the pod can see. |
| "The catalyst" | The date in the thesis sentence, and an exit written before the entry | The ledger's exit rule | §8D.1, §8D.7 | A catalyst you wait for becomes a deadline you set for yourself. |
| "Post-reorg value" | Forced selling as a supply schedule | Overhang, slow capital, a drift you can schedule | §16.2, §16.8.3, Law 15 | The emergence discount has a timetable, and a "worthless" short leg can turn out to be the fulcrum's option. |

### A.10.7 Careers

The last table translates the job itself. Most of these words name a person or a ritual at the old firm; on the desk the person has usually become a number and the ritual a log file. It is less bleak than it sounds. The log file is fairer.

| Banker says | Desk says | Formula or tool | Built in | What changes |
| :--- | :--- | :--- | :--- | :--- |
| "The deal team" | One of five businesses, each with its own clock | Market maker, pod, systematic manager, bank desk, distressed fund | §4.1, §1B.6, Chapter 4-C | "Systematic credit" names five different jobs. Choose the room by its clock, not by the sign on the door. |
| "The MD signed off" | The risk manager, the limit sheet and the model review | Model risk under SR 11-7 | §8B.9, §26.8 | Approval becomes a test someone else can rerun, and a question: why is today's number different from yesterday's? |
| "My track record" | A hit rate with a standard error | $\text{SE}(\hat p) = \sqrt{p(1-p)/n}$ | §3B.7, §28.2 | Twenty-two wins in forty bets cannot be told apart from a coin. Ask to be judged on calibration and the log. |
| "The model I built" | An Edge Ledger row with a decay horizon | $\text{IC}(h) = \text{IC}_0 \cdot 2^{-h/h_{1/2}}$ | §3.5 | Your work is a feature with a refresh rate, a half-life and a list of who else has it. |
| "My analyst will turn it" | ROBO, and a spec | The Spec You Hand the Robot; the citation contract | §26.4, §26.9 | ROBO builds exactly what you asked, and "minimize drawdown" holds cash forever. Units and edge cases are now your job. |
| "The backtest shows" | A Sharpe deflated by the number of trials | Deflated Sharpe ratio | §7.8, Law 12 | Count your trials. A slide with a Sharpe of 2.9 and no count of attempts is a CIM without footnotes. |
| "The bonus" | A call on the pod's P&L, with a stop the platform holds | Payout $\varphi\,\Pi^+$; pay per pod, risk per fund | §28.1, §28.6 | The PM is long volatility by contract, which is why the stop exists and binds before the alpha does. |
| "My first ninety days" | A calendar, a log and twelve mistakes | `desk_calendar.py` | §3B.1, §3B.6, §3B.8 | Day one starts at 6:47 a.m. with a security-master diff and a late vendor file. That is the job, not an obstacle to it. |

Theo keeps a printout of these tables under his keyboard, next to the USB stick, and marks a row each time the desk catches him using the old meaning. By December the marks cluster in valuation and relative value, which Ines says is the right place: those are the rows where the old meaning was not wrong, only unpriced. The language keeps moving, so this section is revised each edition with Appendix C. A desk word that is not here probably means something you already know, with a probability attached. That is the whole phrasebook in one sentence.

<!-- STATUS: COMPLETE -->
