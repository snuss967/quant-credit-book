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

## 15.2 Anatomy and Pricing of the 101 Change-of-Control Put

### 15.2.1 Desk framing: a smoke detector with two licensed inspectors

A high-yield change-of-control put is a smoke detector. When someone acquires control of the issuer (typically more than 50% of the voting stock, or a sale of substantially all of the assets), the issuer must offer to buy back every note at 101% of principal plus accrued and unpaid interest. The offer goes out within a fixed number of days after the event, often 30, and stays open for a window usually measured as 30 to 60 days; then the repurchase settles. Each holder chooses: tender at 101, or keep the bond and live with the new owner.

The investment-grade version is a smoke detector that goes off only if there is a fire *and* two separately licensed inspectors agree, within sixty days, that it is a fire. The defined term is usually "Change of Control Repurchase Event" or "Change of Control Triggering Event," and the EDGAR counts in §15.3 show that one or the other appears in hundreds of registered IG prospectuses a year. The trigger needs a change of control *and* a "Rating Event": the notes are rated below investment grade by each of the named agencies (sometimes all three, sometimes two of three) within a window that typically opens at the earlier of the change of control and its public announcement, runs for about 60 days after the change of control, and stays open while any agency has the notes publicly under review for downgrade. That drafting is typical, not universal. Read the definition in the document you actually own, because the gap between "each of" and "any two of" is a probability you are about to estimate.

Why 101? Because the drafters of the late 1980s wanted the holder to be worth at least par after a leveraged buyout, and a point on top made the tender offer clean. The premium is the tip. The put is the *par*. Remember this the next time someone tells you the 101 is "only a point": on a bond trading at 77, it is twenty-four points.

Mags was there. "In 1988 we learned about event risk from RJR Nabisco, the deal that taught investment-grade bondholders they were lunch. Then we spent two years inventing the poison put." (The measured damage is in Asquith & Wizman (1990) and Warga & Welch (1993); the covenant response is in Crabbe (1991), Lehn & Poulsen (1991) and Cook & Easterwood (1994).)

Theo has a question that he has been asking since his first week. "But what does the indenture say? Not the summary. The definitions." He is right to ask, because every term in the payoff below is a defined term, and each defined term is a parameter.

### 15.2.2 Derivation: the put as a compound option

**Notation for this chapter.** The style bible reserves $\tau$ for default time. The deal-resolution date from §15.1 is the first event this chapter cares about, so we write $\tau_c$ for the closing date when the deal closes, and keep $\tau$ for default where it appears. Leverage collides with loss given default $L = 1-R$, so pro-forma leverage is $\ell_{pf}$, defined as debt over EBITDA (or over $\text{EV}$ where stated). Deal-clock hazards are $h_k(t)$, never $\lambda$, which stays reserved for default intensity.

**Setup.** A bond pays an annual coupon $c$ (percent of par, paid semiannually) and matures at $T$. A deal is signed at $t_0$; if it closes, it closes at a random time $\tau_c$. Let $\mathbf{1}_{\{\text{deal}\}}$ indicate that it closes and $\mathbf{1}_{\{\text{trig}\}}$ that the contractual trigger fires (the change of control alone in HY; the change of control *and* the Rating Event in IG). The strike is $K = 101$ plus accrued interest. Under $\mathbb{Q}$ with short rate $r_u$, the put is worth

$$
V_{\text{CoC}}(t_0) \;=\; \mathbb{E}^{\mathbb{Q}}\!\left[\, e^{-\int_{t_0}^{\tau_c} r_u\,du}\; \mathbf{1}_{\{\text{deal}\}}\,\mathbf{1}_{\{\text{trig}\}}\,\big(K - P^{\text{post}}_{\tau_c}\big)^{+} \,\right],
$$

where $P^{\text{post}}_{\tau_c}$ is the price the bond would trade at immediately after closing if nobody tendered. It is a compound option: an option (the deal closes and triggers) on an option-like payoff (the put is worth something only if the post-close bond trades below the strike).

**Step 1: factor what can be factored.** Assume (A1) the closing time is independent of rates, so the discount factor can be pulled out at the expected close $\bar\tau_c$ as $B(t_0,\bar\tau_c)$, and condition on the deal:

$$
V_{\text{CoC}} \;\approx\; \pi_d\, B(t_0,\bar\tau_c)\; \mathbb{E}^{\mathbb{Q}}\!\left[\mathbf{1}_{\{\text{trig}\}}\,(K - P^{\text{post}})^{+} \,\middle|\, \text{deal}\right],
\qquad \pi_d = \mathbb{Q}(\text{deal}).
$$

**Step 2: do not factor the trigger.** It is tempting to write the inner expectation as $\pi_{\text{trig}\mid d}\cdot\mathbb{E}[(K-P^{\text{post}})^+]$. That is assumption (A2), independence of trigger and payoff, and it is false in exactly the deals you care about. Write the identity instead:

$$
\mathbb{E}\!\left[\mathbf{1}_{\{\text{trig}\}}(K-P^{\text{post}})^{+}\right]
\;=\; \pi_{\text{trig}\mid d}\;\mathbb{E}\!\left[(K-P^{\text{post}})^{+}\right] \;+\; \operatorname{Cov}\!\left(\mathbf{1}_{\{\text{trig}\}},\,(K-P^{\text{post}})^{+}\right).
$$

The ratings leg fires when the post-close spread $s^{\text{post}}$ is high, and a high spread is precisely when $P^{\text{post}}$ is low and the put is deep in the money. The covariance is positive. Define the **conditional moneyness ratio**

$$
M \;=\; \frac{\mathbb{E}\!\left[(K-P^{\text{post}})^{+}\mid \text{trig}\right]}{\mathbb{E}\!\left[(K-P^{\text{post}})^{+}\right]} \;=\; 1 + \frac{\operatorname{Cov}\!\left(\mathbf{1}_{\{\text{trig}\}},(K-P^{\text{post}})^{+}\right)}{\pi_{\text{trig}\mid d}\,\mathbb{E}\!\left[(K-P^{\text{post}})^{+}\right]},
$$

so that $V_{\text{CoC}} \approx \pi_d\,\pi_{\text{trig}\mid d}\,B\,M\,\mathbb{E}[(K-P^{\text{post}})^+]$. For a sponsor LBO, $M>1$ and the independent approximation understates the put. For a strategic IG acquirer, $\pi_{\text{trig}\mid d}\approx 0$ because the Rating Event cannot fire when the parent is a stronger credit, and the put is worthless however far below 101 the bond trades. Microsoft buying Activision is the textbook strategic case: a AAA parent means the second inspector never shows up.

**Step 3: price the bond at the trigger.** With $t_i$ the remaining coupon times and $y^{\text{TSY}}_t$ the Treasury zero curve,

$$
P^{\text{post}} \;=\; \sum_{i} \tfrac{c}{2}\,e^{-(y^{\text{TSY}}_{t_i} + s^{\text{post}})\,t_i} \;+\; 100\,e^{-(y^{\text{TSY}}_{T} + s^{\text{post}})\,T},
\qquad s^{\text{post}} \;=\; s_{\text{acq}} + \Delta_{\text{struct}} + \Delta_{\text{lev}}(\ell_{pf}),
$$

where $s_{\text{acq}}$ is the acquirer's (or new capital structure's) spread at the relevant tenor, $\Delta_{\text{struct}}$ the penalty for legacy notes left structurally subordinated at an operating company or holding company, and $\Delta_{\text{lev}}$ a Merton-style map from pro-forma leverage to spread (Chapter 6). Discount on the post-close curve, never on the target's pre-deal curve: after the trigger the target's pre-deal curve is a historical document.

**Step 4: coupon vintage dominates.** Differentiate $P^{\text{post}}$ in the coupon:

$$
\frac{\partial P^{\text{post}}}{\partial c} \;=\; \tfrac12\sum_i e^{-(y^{\text{TSY}}_{t_i}+s^{\text{post}})t_i} \;\equiv\; A(s^{\text{post}}),
$$

the annuity factor per point of annual coupon. Price is linear in coupon with slope $A$, so the intrinsic value $(K - P^{\text{post}})^+$ is a hockey stick in $c$ with a kink at the **break-even coupon**

$$
c^{*}(s^{\text{post}}) \;=\; \frac{K - 100\,e^{-(y^{\text{TSY}}_T+s^{\text{post}})T}}{A(s^{\text{post}})}.
$$

Any bond with $c < c^*$ has an in-the-money put if it triggers. Plug in a remaining life of 4.5 years and a flat Treasury zero rate of 4.4% *(illustrative throughout)*. Into a strategic acquirer at 60bp, $y = 5.0\%$, $A \approx 4.08$, $100e^{-yT}\approx 79.9$ and $c^*\approx 5.2\%$. Into a sponsor LBO at 350bp, $y=7.9\%$, $A\approx 3.71$, $100e^{-yT}\approx 70.1$ and $c^*\approx 8.3\%$. The full grid:

| Bond (4.5 years remaining, *illustrative*) | Coupon | $P^{\text{post}}$, strategic buyer (60bp) | $P^{\text{post}}$, sponsor LBO (350bp) | Intrinsic if triggered, LBO |
| :-- | --: | --: | --: | --: |
| 2021 vintage | 1.85% | ≈87.4 | ≈77.0 | ≈24.0 |
| 2023 vintage | 5.00% | ≈100.3 | ≈88.7 | ≈12.3 |
| 2009-style high coupon | 6.875% | ≈107.9 | ≈95.6 | ≈5.4 |

Same issuer, same acquirer, same trigger: a four-to-one spread in what the put is worth, driven entirely by the year the bond was printed. The put does not care about the credit story. It cares about $101 - P$. This is aha number one of the chapter: **moneyness is a coupon-vintage accident**, and the 2020–21 vintage of sub-3% IG coupons turned every one of those bonds into a deep-in-the-money LBO put the day rates went to 4%.

Kaz looks at the table. "So the most valuable covenant in the IG market was written by a bond that nobody wanted to buy in 2021."

"Nobody wanted to buy it at 1.85% either," Mags says. "They bought it anyway. Now they get paid for their regret."

**Step 5: the trigger probability.** The ratings leg is a classification problem. A serviceable model is a logistic

$$
\pi_{\text{trig}\mid d} \;=\; \sigma\!\left(\alpha + \beta_{\ell}\,\ell_{pf} + \beta_{s}\,\mathbf{1}_{\text{sponsor}} + \beta_{r}\,\text{notch}_{\text{acq}}\right),\qquad \sigma(z) = \frac{1}{1+e^{-z}},
$$

fit on past deals, with $\text{notch}_{\text{acq}}$ the acquirer's rating in notches below AAA. It returns roughly one for sponsor LBOs that add five or more turns of debt and roughly zero for IG strategics. The interesting cases are in the middle: an IG acquirer that levers up for a large deal and promises to deleverage, where the agencies' "under review" language holds the window open and the answer depends on whether the issuer's deleveraging plan is believed.

**Step 6: say which measure.** A $\pi_d$ backed out of the equity merger-arbitrage spread is a risk-adjusted, $\mathbb{Q}$-like number: Mitchell & Pulvino (2001) show that risk-arbitrage returns behave like a short position in index puts, so market-implied failure probabilities exceed physical ones, especially in bad markets. A hazard estimated from historical deal outcomes (§15.5) is $\mathbb{P}$. Never put the two in one formula without a risk-premium adjustment and a sentence saying so.

**Step 7: bound the Bermudan error.** The holder actually has a window of 30–60 days to tender, so the put is Bermudan-ish, not European. Treat it as European at $\tau_c$ and bound the error by the value of waiting: over a 45-day window the post-close bond moves by roughly $D^{\text{spr}}\,\sigma_s\sqrt{45/365}$, a point or two for a four-year bond with 150bp of annual spread volatility. That is small against twenty-four points of intrinsic and large against half a point; the bound tells you when to care.

> **Ways This Blows Up.** (1) *The covenant is not the cash flow.* A consent solicitation can strip the change-of-control covenant before the trigger (Warner Bros. Discovery, June 2025, §15.8), and covenant defeasance can release the issuer from it after the trigger (Electronic Arts, August 2026, below). Model the issuer's counter-option or your put is a payoff without its knock-out barrier. (2) *Accrued interest and record dates.* The repurchase price is 101 plus interest accrued to, but excluding, the repurchase date; if that date falls after a record date, the coupon goes to the record holder and the repurchase price drops accordingly. Off-by-one-coupon errors are worth 1–3 points on a high-coupon bond. (3) *Structural subordination.* Tapestry's 2023 prospectus states that the new notes would be "structurally subordinated to certain indebtedness assumed in connection with the Capri Acquisition"; legacy target notes left at an operating subsidiary can be senior *or* junior to the new money, and $\Delta_{\text{struct}}$ can have either sign. (4) *The wrong curve.* Discounting at the target's pre-deal spread overstates $P^{\text{post}}$ for LBOs and understates it for strategic buyers. (5) *The definition you did not read.* "Each of" versus "any two of" the agencies; a window that ends 60 days after the change of control versus 60 days after its announcement. Each is a different $\pi_{\text{trig}\mid d}$.

> **[SOURCE EXTRACTION]** *Veronesi_Fixed_Income_Securities p.470:* "The key to the dynamic replication is that the issuer behaves as the model prescribes it should. However, exercising an American option optimally is not mandatory, and it is perfectly reasonable that the issuer may exercise sub-optimally."
>
> **Annotation.** Veronesi is writing about callable bonds, where the issuer's option is to call early and the model assumes it does so optimally. The change-of-control put inverts the roles but keeps the lesson: the *holder* owns the put, and the *issuer* owns a set of counter-options (tender below 101, strip the covenant by consent, defease, refinance through an exchange offer) that the textbook payoff omits. A 2026 desk prices the put net of those counter-options, and the issuer's choice among them is not a random variable with a nice distribution; it is a cost-minimization problem the sponsor solves with expensive lawyers. Where the modern desk departs from Veronesi: we do not assume the counterparty is sub-optimal by accident. We assume it is optimal for a payoff we forgot to write down, and we go find the clause.

> **[SOURCE EXTRACTION]** *Schmid_Credit_Risk_Pricing_Models p.153:* "Credit options offer protection against changing default free interest rates and changing credit spreads. Hence, they allow hedging of mark-to-market exposure to fluctuations in spreads and interest rates: hedging long positions with puts, and short positions with calls."
>
> **Annotation.** Schmid's credit put is a traded instrument whose strike is a spread. The change-of-control put is a credit put embedded in the bond, with a strike fixed in price (101), a trigger written by a lawyer, and an exercise window set by an indenture. The table above shows why the embedded version is also a *rates* option: most of the intrinsic value on the 1.85% notes comes from Treasury yields, not from the LBO spread. A desk that hedges an LBO-candidate portfolio with CDS index protection is hedging the spread leg and staying unhedged on the leg that drives moneyness. Where the modern desk departs: the embedded put is not tradeable on its own, so its value shows up only as a cross-sectional spread anomaly across coupon vintages of the same issuer (exercise 3).

### Specification for AI Implementation

**What ROBO built from the vague version.** Theo typed "price the CoC put on the U.S. Steel 6.875% 2029s." ROBO priced a vanilla European put struck at 101 on the bond using the target's pre-deal spread volatility, ignored the acquirer, ignored the trigger, and returned a healthy number for a bond that was about to migrate onto a stronger parent's curve and trade above 101. It did exactly what it was told.

**The precise spec.** Implement `price_coc_put` with the payoff conditional on deal × trigger, the post-close bond priced on the post-close curve, the trigger allowed to depend on the post-close spread (to capture $M>1$), and an optional issuer counter-option (defeasance or strip) that may depend on how far in the money the put is.

- **Inputs.** `deal_prob` $\pi_d\in[0,1]$ (state the measure); `trigger_prob_given_deal`, a float or a callable mapping spreads (decimal, shape `(n,)`) to per-path probabilities; `post_spread_sampler(rng, n)` returning decimal spreads of shape `(n,)`; `coupon` in percent of par; `maturity_years` and `t_close` in years (ACT/365 clock; coupons 30/360 semiannual, valued on a coupon date so accrued is zero); `defeasance_prob`, a float or a callable of intrinsic value.
- **Outputs.** A dict with `value` (points per 100 face at signing), `stderr`, `moneyness_ratio` $M$, and `mean_intrinsic`.
- **Edge cases.** `deal_prob == 0`, a scalar trigger probability of 0, or a scalar defeasance probability of 1 returns exactly 0. A bond maturing before `t_close` returns 0 with a warning. Spreads are clipped at 0. $M$ is `nan` when intrinsic value is zero everywhere.
- **Variance reduction.** Integrate the deal and trigger Bernoullis analytically (Rao–Blackwellization): simulate only the spread.

```python
# ---- Chapter 15 reference engine, block 1: bond math and the 101 CoC put ----
import warnings
import numpy as np
import pandas as pd
from scipy import optimize
from scipy.stats import norm
from scipy.interpolate import PchipInterpolator


def tsy_zero_curve(t):
    """Illustrative continuously compounded UST zero rate (decimal) at tenor t (years).
    A Nelson-Siegel shape chosen to look like 2025-26. NOT market data."""
    t = np.maximum(np.asarray(t, dtype=float), 1e-6)
    b0, b1, b2, lam = 0.0450, -0.0060, 0.0040, 1.8
    x = t / lam
    f = (1.0 - np.exp(-x)) / x
    return b0 + b1 * f + b2 * (f - np.exp(-x))


def bond_price(coupon, maturity_years, spread, curve=tsy_zero_curve, freq=2):
    """Price per 100 face. coupon in percent of par per year; spread decimal, scalar or (m,).
    Coupon dates are counted back from maturity. Keep maturity_years on the half-year grid
    so we value on a coupon date (clean = dirty). Returns shape (m,)."""
    s = np.atleast_1d(np.asarray(spread, dtype=float))
    n = int(np.ceil(maturity_years * freq - 1e-9))
    if n <= 0:
        return np.full(s.shape, 100.0)
    t = maturity_years - np.arange(n)[::-1] / freq                    # (n,), all > 0
    y = curve(t)                                                       # (n,)
    cf = np.full(n, coupon / freq)
    cf[-1] += 100.0
    disc = np.exp(-(y[None, :] + s[:, None]) * t[None, :])            # (m, n)
    return disc @ cf


def price_coc_put(deal_prob, trigger_prob_given_deal, post_spread_sampler, coupon,
                  maturity_years, curve=tsy_zero_curve, t_close=0.75, strike=101.0,
                  defeasance_prob=0.0, n_paths=200_000, seed=7):
    """Value at signing (points per 100 face) of a 101 change-of-control put."""
    if not 0.0 <= deal_prob <= 1.0:
        raise ValueError(f"deal_prob must be in [0,1], got {deal_prob}")
    zero = dict(value=0.0, stderr=0.0, moneyness_ratio=np.nan, mean_intrinsic=0.0)
    if maturity_years <= t_close:
        warnings.warn("bond matures before the expected close: put is worthless")
        return zero
    scalar_trig = not callable(trigger_prob_given_deal)
    scalar_def = not callable(defeasance_prob)
    if deal_prob == 0.0 or (scalar_trig and trigger_prob_given_deal == 0.0) \
            or (scalar_def and defeasance_prob == 1.0):
        return zero
    rng = np.random.default_rng(seed)
    s = np.clip(np.asarray(post_spread_sampler(rng, n_paths), dtype=float), 0.0, None)
    p_post = bond_price(coupon, maturity_years - t_close, s, curve)   # (n,)
    intrinsic = np.maximum(strike - p_post, 0.0)                       # (n,)
    p_trig = (np.full(n_paths, float(trigger_prob_given_deal)) if scalar_trig
              else np.clip(np.asarray(trigger_prob_given_deal(s), dtype=float), 0.0, 1.0))
    p_def = (np.full(n_paths, float(defeasance_prob)) if scalar_def
             else np.clip(np.asarray(defeasance_prob(intrinsic), dtype=float), 0.0, 1.0))
    disc = float(np.exp(-curve(t_close) * t_close))
    per_path = deal_prob * disc * p_trig * (1.0 - p_def) * intrinsic
    mean_int = float(intrinsic.mean())
    ratio = (float((p_trig * intrinsic).mean() / p_trig.mean() / mean_int)
             if mean_int > 0.0 and p_trig.mean() > 0.0 else np.nan)
    return dict(value=float(per_path.mean()),
                stderr=float(per_path.std(ddof=1) / np.sqrt(n_paths)),
                moneyness_ratio=ratio, mean_intrinsic=mean_int)


# --- sanity checks, block 1 ---
def const_sampler(s0):
    return lambda rng, n: np.full(n, s0)

# (1) a degenerate spread sampler reproduces the closed form pi_d * pi_trig * B * (K - P)^+
v = price_coc_put(0.85, 0.9, const_sampler(0.035), 1.85, 5.25, t_close=0.75)
p_star = bond_price(1.85, 4.5, 0.035)[0]
closed = 0.85 * 0.9 * float(np.exp(-tsy_zero_curve(0.75) * 0.75)) * max(101.0 - p_star, 0.0)
assert abs(v["value"] - closed) < 1e-10, (v, closed)

# (2) a high-coupon bond into a tight acquirer curve: the put is exactly worthless
v_otm = price_coc_put(0.9, 1.0, const_sampler(0.005), 6.875, 3.75, t_close=0.75)
assert bond_price(6.875, 3.0, 0.005)[0] > 101.0 and v_otm["value"] == 0.0

# (3) an LBO with a spread-dependent ratings leg: M > 1, and independence understates
lbo_spread = lambda rng, n: 0.035 * np.exp(0.35 * rng.standard_normal(n) - 0.5 * 0.35 ** 2)
ratings_leg = lambda s: 1.0 / (1.0 + np.exp(-(s - 0.025) / 0.004))   # both agencies cut
lbo = price_coc_put(0.85, ratings_leg, lbo_spread, 1.85, 5.25, t_close=0.75)
pbar = float(ratings_leg(lbo_spread(np.random.default_rng(7), 200_000)).mean())
lbo_indep = price_coc_put(0.85, pbar, lbo_spread, 1.85, 5.25, t_close=0.75)
assert lbo["moneyness_ratio"] > 1.0 and lbo["value"] > lbo_indep["value"]

# (4) a sponsor that defeases whenever the put is more than 5 points in the money
lbo_def = price_coc_put(0.85, ratings_leg, lbo_spread, 1.85, 5.25, t_close=0.75,
                        defeasance_prob=lambda intr: (intr > 5.0).astype(float))
assert lbo_def["value"] < lbo["value"]
print(f"1.85% LBO put: {lbo['value']:.2f} +/- {lbo['stderr']:.3f} pts, M = {lbo['moneyness_ratio']:.3f}; "
      f"independent: {lbo_indep['value']:.2f}; with defeasance: {lbo_def['value']:.2f}")
```

Two things to notice in the output. First, the 1.85% bond's put is worth something like eighteen to nineteen points at signing under these illustrative inputs, which is most of the gap between where an LBO candidate's low-coupon bonds trade and where its high-coupon bonds trade. Second, check (4) sends the value to roughly zero: a sponsor that defeases whenever defeasing is cheaper than paying 101 leaves the holder with nothing but the scheduled cash flows. That is not a hypothetical.

### Case Study: Electronic Arts 2025–26, the In-the-Money Put That Got Defeased

**The deal.** On September 29, 2025, Electronic Arts agreed to be acquired by PIF, Silver Lake and Affinity Partners for \$210 per share in cash, about \$55 billion of enterprise value and a 25% premium to the unaffected close of \$168.32 on September 25, with PIF rolling its existing 9.9% stake. The announcement called it "the largest all-cash sponsor take-private investment in history" (EA press release, Sept. 29, 2025, EDGAR). All regulatory approvals were in hand by July 30, 2026, and the deal closed on August 4, 2026: about ten months from signing to close.

**The legacy bonds.** EA had two series outstanding from February 2021: \$750mm of 1.850% Senior Notes due 2031 and \$750mm of 2.950% Senior Notes due 2051. Their prospectus supplement gives holders a "Change of Control Repurchase Event" offer at "101% of the aggregate principal amount of the notes to be repurchased plus any accrued and unpaid interest" (EA 424B2/424B5 prospectus supplement, Feb. 2021, EDGAR). Run them through Step 4. With 2026 Treasury yields in the 4s, the 2031s were worth roughly 89–90 at Treasury flat and the 2051s, a 2.95% coupon with a quarter-century left, far less *(illustrative)*. Add any LBO spread and both are deep in the money. Mark this as the cleanest real-world example of aha number one: the most valuable thing about the EA 2031s was the year they were printed.

**The new capital structure.** The August 4, 2026 closing 8-K describes the financing: a first-lien term loan B of \$6,125mm plus €1,725mm, a term loan A of \$3,250mm, a \$500mm revolver, and notes issued on April 8, 2026 consisting of \$2,875mm of 7.250% senior secured notes due 2033, €1,080mm of 6.250% senior secured notes due 2033 and \$2,500mm of 8.750% senior notes due 2034, with 40% equity claws at 107.25, 106.25 and 108.75 (EA 8-K, Aug. 4, 2026, EDGAR). A 7.25% secured coupon on the new money tells you where $s^{\text{post}}$ was going to be for the old money.

**The tender.** The legacy notes were the subject of tender offers launched February 10, 2026 and expiring July 30, 2026. Only \$68.830mm of the 2031s and \$7.922mm of the 2051s were tendered, leaving \$681.170mm and \$742.078mm outstanding (same 8-K). About 5% of the face accepted. We do not reproduce the tender consideration here; pull the offer documents before citing it. What the participation tells you is that 95% of holders preferred whatever came next.

**What came next.** At closing, Parent "caused the Company to defease certain obligations" under the 2016/2021 indenture by irrevocably depositing U.S. Government Obligations sufficient to pay principal, premium, if any, and interest when due (same 8-K). Our reading, which the reader should check against the indenture's defeasance article and the agencies' rating actions: a deposit of Treasuries that covers every scheduled payment satisfies the payment obligations, and under a covenant-defeasance provision it releases the issuer from covenants including the repurchase covenant. The holders now own a Treasury-collateralized 1.85% or 2.95% bond that pays on schedule. They do not get 101 today. The sponsor's arithmetic is the Step 4 table read backwards: defeasing costs the present value of the remaining cash flows at Treasury yields, about 89–90 per 100 for the 2031s and considerably less for the 2051s *(illustrative)*, against 101 for a put that pays in cash. On roughly \$1.4bn of remaining face, the saving is in the low hundreds of millions *(illustrative)*.

**What the desk should have flagged.** Not "LBO candidate, low coupon, long the put." The right flag was "LBO candidate, low coupon, *and the base indenture contains a covenant-defeasance article that the CoC covenant does not survive*." That is a document feature, and it belongs in the security master as a field alongside the trigger definition (Chapter 13 treats document features as state variables; Chapter 25 extracts them with NLP). In the pricing engine, it is the `defeasance_prob` callable: the issuer's counter-option is exercised when it saves money, which is exactly when the put is deep in the money. Kaz priced the put. Theo read the defeasance section. Theo was right.

Mags, finishing her 1988 story: "Then in 2026 a sponsor learned about the poison put and spent one afternoon inventing a Treasury deposit." She considers this. "It's good work. I hate it."

The book's most expensive three words, "open market purchase," have a cousin, and it is "defease certain obligations."

> **Desk Myth vs. Desk Reality.** *Myth:* the 101 put protects you in an LBO. *Reality:* it protects you if the bond trades below 101, the trigger fires, both inspectors agree inside the window, the covenant survives every consent solicitation between signing and closing, and nobody defeases it. Otherwise it protects the billing of the sponsor's counsel.

## 15.3 Portability: The Short Option You Did Not Know You Sold

### 15.3.1 Desk framing

Kaz hears the word in a morning meeting and brightens. "Portability. Like a phone number? Bondholders keep their coupon when they switch carriers?"

"Close," Ines says. "The issuer keeps the number. You get dropped."

A portability clause, usually drafted as a "Specified Change of Control Event" or a "Permitted Change of Control" carve-out, says that a change of control which would otherwise trigger the 101 put does *not* trigger it if conditions hold. Typical conditions, in the order a covenant analyst checks them: the change of control happens within a window after issue (two or three years is common); pro-forma leverage on the closing date is at or below a test, often the leverage at issuance or a fixed multiple; the carve-out can be used once; and sometimes the acquirer must meet a size or experience test. The details vary by deal and the analyst's job is to read them. The pricing job is the same every time: the holder sold the issuer a digital option on leverage, and the sponsor gets to choose the leverage.

### 15.3.2 Derivation: a short digital on a number the counterparty chooses

**Exogenous version.** If pro-forma leverage at the change of control, $\ell_{\tau_c}$, were an exogenous random variable, the holder's put would survive portability only when the test fails:

$$
V^{\text{port}}_{\text{CoC}} \;=\; V_{\text{CoC}}\cdot \mathbb{Q}\!\left(\ell_{\tau_c} > \bar\ell \,\middle|\, \text{deal},\text{trig}\right),
$$

and the issuer's digital is worth $V_{\text{CoC}}\cdot\mathbb{Q}(\ell_{\tau_c}\le\bar\ell\mid\cdot)$. With $\ln \ell_{\tau_c}\sim\mathcal{N}(\ln \ell_0 + \mu\tau_c,\ \sigma_\ell^2\tau_c)$, the survival probability is $\Phi\!\left(\frac{\ln\ell_0 + \mu\tau_c - \ln\bar\ell}{\sigma_\ell\sqrt{\tau_c}}\right)$, a barrier problem with a known answer. It is also the wrong model.

**Endogenous version.** The acquiring sponsor sets new debt $F_{\text{new}}$ *after* reading $\bar\ell$. Let $E^{\text{rep}}$ be reported EBITDA at closing, $a\ge 0$ the add-back ratio the definition permits, so that the test is computed on $E^{\text{adj}} = (1+a)E^{\text{rep}}$, and let $F_{\min}$ be the least debt that finances the purchase given the largest equity cheque the sponsor will write. The sponsor can pass the test whenever $F_{\min} \le \bar\ell\,(1+a)\,E^{\text{rep}}$, and it will pass whenever the cost of the 101 offer exceeds the value of the turns of leverage it gives up. Take the limiting case in which the put is always more expensive than the forgone leverage (true for the deep-in-the-money puts in §15.2). The put survives only on the event

$$
\mathcal{A} \;=\; \left\{ E^{\text{rep}} < \frac{F_{\min}}{\bar\ell\,(1+a)} \right\}.
$$

With $\ln E^{\text{rep}}\sim\mathcal{N}(-\tfrac12\sigma_E^2,\ \sigma_E^2)$ normalized so that $\mathbb{E}[E^{\text{rep}}]=1$ at signing,

$$
\mathbb{P}(\mathcal{A}) \;=\; \Phi\!\left(\frac{\ln\!\big(F_{\min}/(\bar\ell(1+a))\big) + \tfrac12\sigma_E^2}{\sigma_E}\right),
\qquad \frac{\partial\,\mathbb{P}(\mathcal{A})}{\partial a} \;=\; -\frac{\varphi(\cdot)}{\sigma_E\,(1+a)} \;<\; 0 .
$$

Two conclusions. First, every point of permitted add-back lowers the probability that the holder keeps the put, and the derivative is largest exactly where the test is close to binding. Mags has been "deeply suspicious of anything called adjusted" for thirty years; here is the derivative that justifies her. Second, the put that survives lives on $\mathcal{A}$, the states in which EBITDA came in low. Those are the states where the holder most wants the put, so the residual is not worthless. What the holder sold is the put's value in the *good* states, where the bond would have traded a few points below 101 and the sponsor would otherwise have had to pay up. This is a contract-design argument under $\mathbb{P}$; pricing the residual put is under $\mathbb{Q}$ and uses the §15.2 engine restricted to $\mathcal{A}$.

Ines turns it into a hand. "You are not playing against the deck. You are playing against a player who sees the test before choosing the bet. If he can make the bet that passes, he will. You only get paid when he cannot."

```python
# ---- block 2: portability as a short digital on sponsor-chosen leverage ----
def portability_put_survival(addback, lev_test=5.0, ebitda_sigma=0.25, ev_multiple=11.0,
                             max_equity_share=0.45, n_paths=100_000, seed=21):
    """Probability that a portable CoC put survives a sponsor who reads the test first.
    Reported EBITDA at close is lognormal with mean 1.0 (signing EBITDA = 1).
    Returns (survival_prob, mean EBITDA | put survives, mean EBITDA | deal ported)."""
    if addback < 0.0 or lev_test <= 0.0:
        raise ValueError("addback must be >= 0 and lev_test > 0")
    rng = np.random.default_rng(seed)
    ebitda = np.exp(ebitda_sigma * rng.standard_normal(n_paths) - 0.5 * ebitda_sigma ** 2)
    f_min = (1.0 - max_equity_share) * ev_multiple            # minimum debt, turns of signing EBITDA
    survives = f_min > lev_test * (1.0 + addback) * ebitda    # sponsor cannot pass the test
    bad = float(ebitda[survives].mean()) if survives.any() else np.nan
    good = float(ebitda[~survives].mean()) if (~survives).any() else np.nan
    return float(survives.mean()), bad, good


# --- sanity checks, block 2 ---
grid = [0.0, 0.1, 0.2, 0.3, 0.4]
surv = [portability_put_survival(a)[0] for a in grid]
assert all(x >= y for x, y in zip(surv, surv[1:]))            # more add-backs, fewer surviving puts
s20, bad20, good20 = portability_put_survival(0.20)
closed20 = norm.cdf((np.log(0.55 * 11.0 / (5.0 * 1.2)) + 0.5 * 0.25 ** 2) / 0.25)
assert abs(s20 - closed20) < 4.0 * np.sqrt(closed20 * (1.0 - closed20) / 100_000)
assert bad20 < good20                                          # surviving puts live in bad states
print("put survival by add-back ratio:", dict(zip(grid, np.round(surv, 3))))
```

With these illustrative inputs a sponsor needing 6.05 turns of signing EBITDA, against a 5.0x test, ports the deal whenever adjusted EBITDA clears about 1.2 times its signing level with no add-backs, and whenever reported EBITDA clears about 1.0 with 20% add-backs. The survival probability falls from the mid-80s percent to below 40% across the grid. Same bond, same sponsor, same test; the only thing that moved was the word "adjusted."

> **Trend Watch.** *Portability's migration into US public filings, 2018–2026.* A full-text search of EDGAR for the portability term "Specified Change of Control Event" finds 1 filing in 2018, 4 in 2019, 8 in 2020, 11 in 2021, 2 in 2022, 3 in 2023, 5 in 2024, 5 in 2025 and 10 in 2026 through mid-October (EDGAR full-text search, run 2026-10-17; approximate). Over the same years, registered 424B2/424B5 prospectuses using the IG double-trigger terms ran at roughly 230–400 a year for "Change of Control Triggering Event" and 90–230 a year for "Change of Control Repurchase Event." Read the portability series for its *existence*, not its level: it counts filings rather than deals, double-counts preliminary and final prospectuses, and misses almost all high-yield bonds, which are sold under Rule 144A and never filed. The covenant-research providers (Covenant Review, Xtract Research, 9fin) publish the share of HY deals with portability; we have not verified their figures for this edition, and the practitioner consensus that European HY has long carried portability more often than US HY should be checked against their data before it is quoted. What it means for the desk: portability is a document feature with a price, it is spreading into the documents a systematic desk can parse, and Chapter 25's extraction pipeline should pull the leverage test, the window, the one-time-use flag and the add-back definition as four separate fields, because each one moves $\mathbb{P}(\mathcal{A})$.

<!-- PASS 2 END -->
