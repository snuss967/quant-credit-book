# Chapter 15: Event-Driven M&A, Regulatory Spreads & Change-of-Control

> *"In the case of an acquisition, which the investor judges is a 20% probability, the risk of being short the sub notes is that they potentially will appreciate to 100 (almost a certainty if they contain a change of control put), a loss of 45."* (Moyer_Distressed_Debt_Analysis p.270)

## Cold Open: Friday the Thirteenth, Aisle Four

Friday, December 13, 2024, 7:40 a.m. Theo's EDGAR alert fires on an 8-K from The Kroger Co., Item 2.04: *Triggering Events That Accelerate or Increase a Direct Financial Obligation.* Kroger has delivered a notice of special mandatory redemption on four tranches of the notes it sold in August to pay for Albertsons, \$4.7 billion in all, to be redeemed on December 18 at 101% of principal plus accrued interest. Three days earlier, a federal court in Oregon had enjoined the merger. Albertsons had terminated the agreement the same day.

"I don't understand," Kaz says, which is unusual enough that two people look up. "Nobody defaulted. Nobody was downgraded. Why would a company *mandatorily* redeem bonds at a *premium*?"

"Because they borrowed \$4.7 billion to buy a grocer they're no longer allowed to buy," Theo says, "and the supplemental indenture says that if the grocer goes away, the money goes back. At 101. Within thirty days of notice."

"So it's a refund with a tip."

"Price is what you pay," Mags says. "A hundred and one is what you get, eventually, after the judge."

Ines has already pulled the hand history: every print in the four short Kroger tranches since the August deal. She circles a cluster of client sells in late November, a few cents under par. "What was the pot, what were the odds, and who at this table knew more than us? Somebody sold the 2027s below par two weeks before a ruling that turned them into a 101 claim settling in five days. Either they knew something about the court's calendar that we didn't, or they needed the cash more than the point. The markouts will tell us which."

Theo plugs in the USB stick with his thirteen-week cash flow model, for emotional support. It has a row labelled "Regulatory" that has been blank for six years. He types "Dec 10: PI granted" into it and feels, for the first time, that the row has a purpose.

ROBO, asked to "price the redemption," returns 101.000. It is not wrong. It is just eleven days late.

**The question this chapter answers:** *how do you price a cash flow whose trigger is a federal judge, whose strike was written into an indenture months before anyone knew how the judge would rule, and whose clock is set by a regulator who counts in working days?*

By the end of this chapter you will be able to: write every M&A-contingent cash flow in a bond, loan, convertible or CDS contract as an explicit payoff function of (deal outcome, trigger, price at trigger); price the 101 change-of-control put as a compound option whose moneyness is mostly a coupon-vintage accident; treat portability as a short digital option on leverage that the sponsor gets to choose; back a market-implied deal-break probability out of a special-mandatory-redemption tranche by curve-matching it against the same issuer's non-SMR bonds; model regulatory timelines with Kaplan–Meier, Nelson–Aalen, Cox and competing-risks estimators built from scratch; and recognize the moment a covenant you thought was an option is about to be defeased out from under you.

## 15.1 The Event-Driven Credit Map: Six Cash Flows That Fire on a Deal

### 15.1.1 Desk framing: the merger is the underlying, the regulator is the clock

An equity merger-arbitrage desk sees one number: the gap between the target's share price and the offer. A credit desk sees a cluster of contractual cash flows, each written by a different lawyer in a different year, each switched on by a different event, and each owned by a different kind of holder. The RSSG reader already reads these documents better than anyone on the floor. The new skill is to stop reading them as prose and start reading them as payoff functions.

Here is the one-line version of the whole chapter. Let $\kappa$ be the terminal state of a pending deal (close, abandon, litigated block) and $\tau$ the date it resolves. Every M&A-sensitive instrument has a price of the form

$$
P_0 \;=\; \mathbb{E}^{\mathbb{Q}}\!\left[\, \sum_{k \in \{c,a,b\}} \mathbf{1}_{\{\kappa = k\}}\; e^{-\int_0^{\tau} r_u\,du}\; \Pi_k(\tau) \,\right] \;+\; \text{carry to } \tau,
$$

where $\Pi_k(\tau)$ is the value of the instrument immediately after outcome $k$ arrives at time $\tau$. Two hard problems hide in that expectation. The first is $\Pi_k$: what the bond, loan or convert is worth in each terminal state, which is where option theory, covenants and the acquirer's curve live (§15.2–15.4). The second is the joint law of $(\kappa,\tau)$: which outcome, and when, which is where HSR waiting periods, Second Requests, European Phase II, CFIUS, the Surface Transportation Board and district-court calendars live (§15.5). Practitioners spend their time on the first and guess the second. The second is where the money is, because the market prices the payoffs well and the clock badly (§15.6).

Ines puts it in poker terms. "The payoff is the pot. The clock is how many streets are left. Most people at the table can count the pot. Almost nobody can tell you the odds that the river gets dealt before the outside date."

### 15.1.2 The six contingent cash flows

| # | Clause | Typical trigger | Payoff to the holder at trigger | Who owns the option | Forced flow it creates |
| :-- | :-- | :-- | :-- | :-- | :-- |
| 1 | Change-of-control (CoC) put | HY: CoC alone. IG: CoC *and* a downgrade below investment grade by the named agencies within a window ("double trigger") | $(101 + \text{AI} - P^{\text{post}})^{+}$ via a repurchase offer | Holder | IG funds selling new fallen angels; HY funds tendering |
| 2 | Special mandatory redemption (SMR) | Deal terminated, or not closed by the SMR outside date | $101 + \text{AI}$ in cash within days, versus holding $P^{\text{close}}$ | Holder long a digital whose sign depends on rates | Short-tranche holders forced to reinvest; issuer forced to fund |
| 3 | Make-whole / optional call | Issuer chooses, usually post-close refinancing | $\max(\text{PV at } y^{\text{TSY}}+\text{spread}_{\text{mw}},\,100)$ | Issuer | Acquirer refinancing target debt |
| 4 | Convertible fundamental-change put and make-whole table | Cash merger, delisting | Par put, plus a conversion-rate increase read off a table indexed by stock price and date | Holder (put), contractual (table) | Convert-arb hedge unwind; delta collapses |
| 5 | Loan CoC event of default | Consummation of the CoC | Acceleration, so repayment at par or a refinanced loan | Lenders (often waived, priced as a consent) | CLO reinvestment; repricing |
| 6 | CDS successor determination | Succession event under the ISDA Definitions | Reference entity reassigned, or orphaned | Protection buyer and seller | Basis dislocation; orphaned protection |

Two further entries are not cash flows at all but *counter-options held by the issuer or acquirer*: the consent solicitation that strips covenants before the trigger, and legal or covenant defeasance, which replaces the issuer's promises with a box of Treasuries. Both kill entry 1. Both appear in the case studies (§15.8, §15.9). An RSSG banker has drafted all eight. A systematic desk has to store all eight as fields in its security master, because a CoC put without its defeasance article is a payoff without its knock-out barrier.

Kaz reads the table twice. "Entry five. The loan *defaults* when the deal *succeeds*?"

"Technically," Theo says. "It's an event of default because the lenders underwrote the old owner. In practice it means the loan gets refinanced at par, which a CLO loan trading at 99 thinks is the best news it's had all year."

"Your industry has a strange relationship with the word 'default.'"

"You should see what we do with 'open market purchase.'"

### 15.1.3 The forced-flow view

Chapter 1 drew the credit ecosystem as a graph of who is a forced seller to whom. M&A adds edges to that graph on dates the deal calendar announces in advance, which is the rare case where a forced flow is both large and predictable:

- **The fallen-angel edge.** An IG target bought by a sponsor is downgraded to high yield at or near close. Every IG-index-constrained holder becomes a seller within days, and HY funds become buyers only after the bond enters their index at a month-end rebalance. Dynkin's evidence that fallen angels outperform after the downgrade "due to price pressures around the downgrade event" (Dynkin_Systematic_Investing_in_Credit p.411) is the price of that edge. When the bond also carries a CoC put struck at 101 and trades in the 80s, the edge is short-circuited: holders do not sell to HY funds, they put the bond back to the issuer. Unless the issuer finds a cheaper door (§15.8).
- **The SMR edge.** When a deal dies, the SMR tranches are redeemed in cash within a few weeks. Kroger repaid \$4.7bn in December 2024; Tapestry repaid about \$6.1bn in November 2024. The holders of those tranches receive cash they did not plan to have, in a size that moves the short end of an issuer curve and of the IG index.
- **The convert edge.** A cash merger collapses a convertible's equity delta to zero on the close date and converts the bond into a par-plus-make-whole claim. The arbitrageur's short-stock hedge must be bought back, and the stock-borrow fees that subsidized the trade disappear.
- **The CLO edge.** A loan CoC repaid at par hands CLO managers cash to reinvest and removes a loan from the collateral pool, which matters most for loans trading below par or bucketed in CCC (Chapter 21).

Each edge is a known flow on an unknown date. The rest of the chapter is about estimating the date.

> **Trend Watch.** *The 2023–2026 mega-deal and IG take-private wave.* The aggregate value of transactions reported under the Hart–Scott–Rodino (HSR) Act rose from about \$1.6 trillion in FY2023 to \$2.1 trillion in FY2024 and \$2.5 trillion in FY2025, while the number of reported transactions stayed roughly flat (1,805, 2,031 and 2,006); transactions above \$1 billion were "approximately one-fourth" of filings in FY2024 and 31.8% in FY2025 (FTC/DOJ *Hart-Scott-Rodino Annual Reports*, FY2023–FY2025, Appendix A). Fewer, bigger deals means more of the market's event risk sits in IG capital structures. The marquee examples are all 2025–26: Electronic Arts agreed on September 29, 2025 to be taken private by PIF, Silver Lake and Affinity Partners at \$210 per share, about \$55bn of enterprise value, described in the announcement as "the largest all-cash sponsor take-private investment in history" (EA press release, Sept. 29, 2025, EDGAR); Union Pacific agreed on July 29, 2025 to acquire Norfolk Southern at about \$85bn of enterprise value, filing an application of roughly 7,000 pages with the Surface Transportation Board on December 19, 2025 (Union Pacific releases, EDGAR); and Warner Bros. Discovery signed with Netflix on December 4, 2025 before signing with Paramount Skydance on February 27, 2026 at \$31.00 per share in cash plus a per-diem ticking fee, closing October 6, 2026 (WBD 8-Ks, EDGAR). What it means for the desk: a sponsor buying an IG company with 2020–21 vintage low-coupon bonds outstanding creates a deep-in-the-money CoC put on an IG security, which the IG market had not had to price at scale since the late 1980s, and the issuer's response (tender, consent strip, defeasance) is now the main determinant of what that put pays.

### Deep-Dive Resource Graph

- **Podcasts:** Bloomberg *Odd Lots* episodes on merger arbitrage and on antitrust enforcement under the 2021–2024 FTC (titles and dates to be confirmed before linking); *Capital Allocators* conversations with event-driven managers (episode-level references to be confirmed).
- **Practitioner Writing:** Matt Levine, *Money Stuff* (Bloomberg), columns on the Kroger–Albertsons injunction, the Electronic Arts take-private and the Warner Bros. Discovery bidding contest (dates to be confirmed); Moody's Investors Service, *Covenant Quality* commentary on change-of-control protection in IG and HY bonds (title-only).
- **Academic Papers:** Billett, King & Mauer (2004), *Bondholder Wealth Effects in Mergers and Acquisitions*, Journal of Finance, DOI 10.1111/j.1540-6261.2004.00628.x; Furfine & Rosen (2011), *Mergers Increase Default Risk*, Journal of Corporate Finance, DOI 10.1016/j.jcorpfin.2011.03.003; Renneboog & Szilagyi (2008), *Corporate Restructuring and Bondholder Wealth*, European Financial Management, DOI 10.1111/j.1468-036X.2007.00414.x.
- **Data & Code:** SEC EDGAR full-text search, https://www.sec.gov/edgar/search/ (API root https://efts.sec.gov/LATEST/search-index); FTC Premerger Notification Program, https://www.ftc.gov/enforcement/premerger-notification-program; FTC/DOJ HSR Annual Report FY2025, https://www.ftc.gov/system/files/ftc_gov/pdf/fy_2025_hsr_annual_report_for_transmittal_to_congress.pdf.

<!-- PASS 1 END -->
