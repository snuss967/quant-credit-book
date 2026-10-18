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

Two further entries are not cash flows at all but *counter-options held by the issuer or acquirer*: the consent solicitation that strips covenants before the trigger, and legal or covenant defeasance, which replaces the issuer's promises with a box of Treasuries. Both kill entry 1. Both appear in the case studies (§15.2, §15.8). An RSSG banker has drafted all eight. A systematic desk has to store all eight as fields in its security master, because a CoC put without its defeasance article is a payoff without its knock-out barrier.

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

> **Trend Watch.** *The 2023–2026 mega-deal and IG take-private wave.* The aggregate value of transactions reported under the Hart–Scott–Rodino (HSR) Act rose from about \$1.6 trillion in FY2023 *(approx.; FY2023 report, not rechecked)* to \$2.1 trillion in FY2024 and \$2.5 trillion in FY2025, while the number of reported transactions stayed roughly flat (1,805, 2,031 and 2,006); transactions above \$1 billion were "approximately one-fourth" of reported transactions in FY2024 and 31.8% in FY2025 (FTC/DOJ *Hart-Scott-Rodino Annual Reports*, FY2023–FY2025, Appendix A). Fewer, bigger deals means more of the market's event risk sits in IG capital structures. The marquee examples are all 2025–26: Electronic Arts agreed on September 29, 2025 to be taken private by PIF, Silver Lake and Affinity Partners at \$210 per share, about \$55bn of enterprise value, described in the announcement as "the largest all-cash sponsor take-private investment in history" (EA press release, Sept. 29, 2025, EDGAR); Union Pacific agreed on July 29, 2025 to acquire Norfolk Southern at about \$85bn of enterprise value, filing an application of roughly 7,000 pages with the Surface Transportation Board on December 19, 2025, which the Board rejected as incomplete on January 16, 2026; the railroads refiled on April 30, 2026, and on May 28, 2026 the Board found the revised application complete but asked for supplemental information (Surface Transportation Board decisions; Union Pacific releases, EDGAR); and Warner Bros. Discovery signed with Netflix in early December 2025 before signing with Paramount Skydance on February 27, 2026 at \$31.00 per share in cash plus a per-diem ticking fee, closing October 6, 2026 (WBD 8-Ks, EDGAR). What it means for the desk: a sponsor buying an IG company with 2020–21 vintage low-coupon bonds outstanding creates a deep-in-the-money CoC put on an IG security, which the IG market had not had to price at scale for a generation, and the issuer's response (tender, consent strip, defeasance) is now the main determinant of what that put pays.

### Deep-Dive Resource Graph

- **Podcasts:** Bloomberg *Odd Lots* episodes on merger arbitrage and on antitrust enforcement under the 2021–2024 FTC (titles and dates to be confirmed before linking); *Capital Allocators* conversations with event-driven managers (episode-level references to be confirmed).
- **Practitioner Writing:** Matt Levine, *Money Stuff* (Bloomberg), columns on the Kroger–Albertsons injunction, the Electronic Arts take-private and the Warner Bros. Discovery bidding contest (dates to be confirmed); Moody's Investors Service, *Covenant Quality* commentary on change-of-control protection in IG and HY bonds (title-only).
- **Academic Papers:** Billett, King & Mauer (2004), *Bondholder Wealth Effects in Mergers and Acquisitions*, Journal of Finance, DOI 10.1111/j.1540-6261.2004.00628.x; Furfine & Rosen (2011), *Mergers Increase Default Risk*, Journal of Corporate Finance, DOI 10.1016/j.jcorpfin.2011.03.003; Renneboog & Szilagyi (2008), *Corporate Restructuring and Bondholder Wealth*, European Financial Management, DOI 10.1111/j.1468-036X.2007.00414.x.
- **Data & Code:** SEC EDGAR full-text search, https://www.sec.gov/edgar/search/ (API root https://efts.sec.gov/LATEST/search-index); FTC Premerger Notification Program, https://www.ftc.gov/enforcement/premerger-notification-program; FTC/DOJ HSR Annual Report FY2025, https://www.ftc.gov/system/files/ftc_gov/pdf/fy_2025_hsr_annual_report_for_transmittal_to_congress.pdf.


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


## 15.4 Special Mandatory Redemptions: The Deal-Break Gauge in the Acquirer's Curve

### 15.4.1 Desk framing: a bond with a deal-break digital stapled to it

An acquirer that has signed a deal but not closed it has a timing problem. It wants its financing locked now, because a committed bridge loan is expensive and the bond market can shut in a week. It does not want to own \$5bn of debt and no target if the regulator says no. The special mandatory redemption solves both. The acquirer sells bonds today; if the merger agreement is terminated, or the deal has not closed by an outside date, it must redeem them, usually at 101 plus accrued, within days of a notice. Kroger's supplemental indenture sets the redemption date "no earlier than the third business day and no later than 30 days following the date of such notice" (Kroger 8-K, Exhibit 4.3, Aug. 27, 2024, EDGAR).

Three drafting details decide the price, and the RSSG reader will find all three in the description of notes:

- **No escrow.** Synopsys's March 2025 prospectus says it plainly: "The proceeds from this offering will not be deposited into an escrow account" (Synopsys 424B5, Mar. 2025, EDGAR). The 101 is an unsecured promise by the acquirer, so between issue and redemption the holder is long the acquirer's credit.
- **An extendable outside date.** Tapestry's SMR fired if Capri was not acquired by February 10, 2025 "(or such later date mutually agreed between us and Capri)" (Tapestry 424B5, Nov. 2023, EDGAR). The clock belongs to the two parties who most want the deal to live.
- **The tranche carve-out.** Kroger put the SMR on its four short tranches (2026, 2027, 2029, 2031; \$4.7bn of \$10.5bn) and not on the 2034, 2054 and 2064 bonds. HPE did the reverse for Juniper: SMR on the 2029, 2031, 2034 and 2054 notes, none on the 2026 and 2027 notes. Synopsys put it on the 2027, 2028, 2030 and 2032 notes and not on the 2035 and 2055 notes (prospectuses on EDGAR).

Kaz reads the Kroger description of notes and asks whether "special mandatory" is stronger or weaker than ordinary mandatory.

"It's the kind of mandatory," Ines says, "that the issuer and the target can agree to postpone."

The carve-out is a gift. Same issuer, same day, same ranking, same lawyers, and one tranche carries an option the next one does not. Whatever price gap the curve cannot explain belongs to the option, and the option's only underlying is whether the deal dies.

### 15.4.2 Derivation: the implied break probability and the duration jump

**Setup.** An SMR tranche pays coupon $c$ (percent of par, semiannual) and matures at $T$. Collapse the deal's resolution to a single date $T_f$ on which the redemption would settle if the deal failed, and let $\pi_f = \mathbb{Q}(\text{deal fails by } T_f)$. The **fail leg** is the value today of the coupons paid on or before $T_f$ plus the redemption price:

$$
G_f \;=\; \sum_{t_i \le T_f} \tfrac{c}{2}\,e^{-y_f t_i} \;+\; \big(101 + \text{AI}_{T_f}\big)\,e^{-y_f T_f},
\qquad y_f \;=\; y^{\text{TSY}}_{T_f} + s_{\text{acq}}(T_f),
$$

where $\text{AI}_{T_f}$ is interest accrued since the last coupon date (30/360 on US corporates) and $y_f$ is the acquirer's short yield, not the Treasury rate, because without escrow the 101 is the acquirer's credit risk. The **close leg** $P^{\text{close}}$ is what the same cash flows would be worth as an ordinary bond of the acquirer, read off the issuer's non-SMR curve at maturity $T$.

**Assumptions.** (B1) The resolution date is known; a random $T_f$ adds a time integral but changes none of the algebra. (B2) The acquirer's curve is the same whether the deal closes or breaks. (B2) is the weak link and gets its own blow-up below.

**Price and inversion.** Under (B1)–(B2),

$$
P_0 \;=\; \pi_f\,G_f \;+\; (1-\pi_f)\,P^{\text{close}}
\qquad\Longrightarrow\qquad
\hat\pi_f \;=\; \frac{P^{\text{close}} - P_0}{P^{\text{close}} - G_f},\qquad P^{\text{close}} \ne G_f .
$$

**The sign flips with rates.** Differentiate:

$$
\frac{\partial P_0}{\partial \pi_f} \;=\; G_f - P^{\text{close}} .
$$

If rates or the acquirer's spread have risen since issue, $P^{\text{close}} < G_f$ and the SMR is a free put on the deal: the holder is paid 101 for a bond worth less, and roots for the judge. If rates have fallen, $P^{\text{close}} > G_f$ and the holder is short a digital: a break takes away a bond worth more than 101. In between, near $P^{\text{close}} = G_f$, the SMR price carries no information about $\pi_f$ at all and $\hat\pi_f$ explodes. The gauge's resolution is proportional to $|P^{\text{close}} - G_f|$. A thermometer that reads only when it is out of equilibrium is still a thermometer; you just have to know when it is switched off.

**A worked number** *(illustrative)*. Take a three-year 4.60% SMR tranche, the shape of Kroger's 2027s, whose non-SMR-curve value is $P^{\text{close}} = 99.00$. The ruling is expected in a quarter, so $T_f = 0.25$, and $y_f = 4.60\%$. No coupon falls before $T_f$; accrued is $4.60 \times 0.25 = 1.15$; so $G_f = 102.15\,e^{-0.0115} \approx 100.98$. If the tranche trades at 99.40,

$$
\hat\pi_f \;=\; \frac{99.00 - 99.40}{99.00 - 100.98} \;=\; \frac{-0.40}{-1.98} \;\approx\; 0.20 .
$$

The bond market thinks there is a one-in-five chance the judge blocks the deal. That number is free of the takeover premium, the target's standalone value and the equity arbitrageurs' borrow costs, which is why it is cleaner than the one backed out of the target's stock.

**Probabilistic duration.** Dollar durations add across the two legs, so with $D_f \approx T_f$ the fail leg's duration and $D^{\text{close}}$ the close leg's,

$$
P_0\,D^{\text{SMR}} \;=\; \pi_f\,G_f\,D_f + (1-\pi_f)\,P^{\text{close}}\,D^{\text{close}}
\qquad\Longrightarrow\qquad
D^{\text{SMR}} \;=\; w\,D_f + (1-w)\,D^{\text{close}},\quad w = \frac{\pi_f\,G_f}{P_0},
$$

which collapses to the probability-weighted $\pi_f D_f + (1-\pi_f) D^{\text{close}}$ when both legs are near par. In the example, $w \approx 0.20$ and $D^{\text{close}} \approx 2.8$, so $D^{\text{SMR}} \approx 2.3$. On ruling day it becomes either 0.25 or 2.8. The hedge ratio does not drift; it jumps, on a date the court has published. Ben Dor documents the same discontinuity for rating changes, where a downgraded IG bond's limit hedge ratio "decreased from 1.00 to 0.45 after the rating change" (Ben_Dor_Quantitative_Credit_Portfolio_Management pp.212–213). The SMR does by contract what a downgrade does by repricing.

**Measure.** $\hat\pi_f$ is a $\mathbb{Q}$ number. The survival models of §15.5 produce $\mathbb{P}$ numbers. The gap between the two is the deal-break risk premium, and Mitchell & Pulvino (2001) tell you which way it points.

> **[SOURCE EXTRACTION]** *Moyer_Distressed_Debt_Analysis p.267:* "Demand and supply would quickly act to create a price discrepancy, which would represent the premium that investors are willing to pay for the early redemption option. The size of the premium would implicitly reflect the probability that investors placed on the refinancing."
>
> **Annotation.** Moyer's example is two senior issues of the same distressed company with different maturities, where a refinancing would take out one of them early: the price gap between them is the market's probability of the refinancing, expressed in points. Replace "refinancing" with "deal break" and you have the SMR gauge, down to the insistence that the comparison be made within one issuer's capital structure so that credit and ranking cancel. Where the 2026 desk departs: Moyer's investor eyeballs the gap and forms a view. The systematic desk inverts it with a fitted issuer curve, guards the denominator, marks $\hat\pi_f$ every day as a time series, and compares it with a physical-measure hazard model, so that the trade is the spread between two probabilities rather than an opinion about one.

> **Ways This Blows Up.** (1) *The control group is contaminated.* Assumption (B2) says the non-SMR tranches price the same in both states. They do not. On the day Kroger terminated it also announced a \$7.5bn buyback including a \$5bn accelerated share repurchase (Kroger release, Dec. 11, 2024, EDGAR), which is not nothing to the holders of the 2034s. If a break moves the acquirer's curve, $P^{\text{close}}$ is itself a mixture, and $\hat\pi_f$ is biased toward whatever the long bonds were pricing. (2) *Extrapolation.* Kroger's SMR tranches were the short ones and its new non-SMR tranches all matured in 2034 or later; curve-matching the 2027s means extrapolating to the short end unless you add the issuer's legacy short bonds as nodes. The code flags it. (3) *The outside date moves.* With a mutually extendable date, the gauge prices "fails by $T_f$," not "fails ever." (4) *Accrued.* Use the indenture's convention to the redemption date; a quarter's accrued on a 4.6% coupon is more than a point, which is most of the signal. (5) *The switched-off thermometer.* When $|P^{\text{close}} - G_f|$ is a few cents, report "no information," not 0.97.

> **Docket Diary.** *Kroger–Albertsons, signing to redemption (EDGAR filings; CourtListener docket for FTC v. The Kroger Co., D. Or. No. 3:24-cv-00347).* **Oct. 13, 2022:** merger agreement signed. **Feb. 26, 2024:** FTC and co-plaintiffs sue in Oregon. **Aug. 15, 2024:** Kroger launches exchange offers of up to \$7,441,608,000 of new Kroger notes for Albertsons-family notes; \$6,819,427,000 is tendered by the early date. **Aug. 27, 2024:** \$10.5bn of new notes in seven tranches, SMR on the four shortest (\$4.7bn). **Dec. 10, 2024:** preliminary injunction granted; Albertsons terminates the same day. **Dec. 11:** Kroger delivers its termination notice and announces the buyback. **Dec. 12:** SMR notice. **Dec. 18:** the 2026, 2027, 2029 and 2031 notes are redeemed at 101% plus accrued (Kroger 8-K, Item 2.04, Dec. 13, 2024). The \$5.8bn of long tranches stay outstanding. Signing to block: about 26 months. The Ad Hoc Group, represented by counsel, notes for the record that this is the first redemption in the book that nobody had to sue over.

The other three 2023–25 SMR deals fill in the outcome distribution, and a desk should price all of them, not only the dramatic one:

| Deal | SMR tranches | Clock | Outcome |
| :-- | :-- | :-- | :-- |
| Kroger–Albertsons | 2026, 2027, 2029, 2031 (\$4.7bn of \$10.5bn) | Signed Oct. 2022; PI Dec. 10, 2024 | Triggered; redeemed at 101 on Dec. 18, 2024 |
| Tapestry–Capri | USD and EUR series issued Nov. 2023 | FTC suit Apr. 23, 2024; terminated Nov. 14, 2024 | Triggered; \$6.1bn at 101 from cash on hand, \$61.1mm premium expensed (Tapestry 8-K, Nov. 2024) |
| HPE–Juniper | 2029, 2031, 2034, 2054 (not 2026, 2027) | DOJ suit Jan. 30, 2025; settlement June 28, 2025 | Nearly triggered; deal closed, SMR expired unexercised |
| Synopsys–Ansys | 2027, 2028, 2030, 2032 (not 2035, 2055) | Announced Jan. 16, 2024; closed July 17, 2025 | SMR expired worthless; about 18 months to close |

Tapestry's \$61.1mm premium on \$6.1bn is the 101 in its purest form: one point, paid for the privilege of having borrowed in advance for a handbag company the FTC would not let it buy.

### Specification for AI Implementation

**What ROBO built from the vague version.** "Back out the break probability from the Kroger SMR bonds." ROBO divided the SMR tranche's price by 101 and reported 0.98. It was a ratio. It was not a probability. It never complains.

**The precise spec.** Fit a Z-spread curve through the issuer's non-SMR tranches by maturity (PCHIP, flat beyond the last node, with an `extrapolated` flag), price each SMR tranche on that curve to get $P^{\text{close}}$, compute the fail leg $G_f$ with accrued interest and the acquirer's short yield, invert for $\hat\pi_f$ with a denominator guard and clipping report, and return the value-weighted probabilistic duration. Schema: a DataFrame with columns `tranche_id` (str), `coupon` (percent), `maturity` (years, on the half-year grid so that `bond_price` values on a coupon date), `price` (full price per 100), `is_smr` (bool). Raise if fewer than two non-SMR tranches or duplicate non-SMR maturities.

```python
# ---- block 3: special mandatory redemption gauge ----
def z_spread(price, coupon, maturity_years, curve=tsy_zero_curve):
    """Constant spread (decimal) over the UST zero curve that reprices the bond."""
    f = lambda s: bond_price(coupon, maturity_years, s, curve)[0] - price
    return optimize.brentq(f, -0.05, 1.0, xtol=1e-12)


def curve_match_close_price(tranches, curve=tsy_zero_curve):
    """P_close for each SMR tranche from the issuer's non-SMR tranches (PCHIP in Z-spread)."""
    need = {"tranche_id", "coupon", "maturity", "price", "is_smr"}
    if need - set(tranches.columns):
        raise KeyError(f"missing columns: {need - set(tranches.columns)}")
    smr = tranches["is_smr"].astype(bool)
    base = tranches.loc[~smr].sort_values("maturity")
    mats = base["maturity"].to_numpy(dtype=float)
    if mats.size < 2 or np.any(np.diff(mats) <= 0):
        raise ValueError("need >= 2 non-SMR tranches with distinct maturities")
    z = np.array([z_spread(p, c, m, curve) for p, c, m in
                  zip(base["price"], base["coupon"], base["maturity"])])
    interp = PchipInterpolator(mats, z, extrapolate=False)
    out = tranches.loc[smr, ["tranche_id", "coupon", "maturity", "price"]].copy()
    m = out["maturity"].to_numpy(dtype=float)
    out["z_close"] = interp(np.clip(m, mats[0], mats[-1]))      # flat beyond the nodes
    out["extrapolated"] = (m < mats[0]) | (m > mats[-1])
    out["p_close"] = [bond_price(c, mm, zz, curve)[0]
                      for c, mm, zz in zip(out["coupon"], m, out["z_close"])]
    return out.reset_index(drop=True)


def smr_fail_leg(coupon, t_f, y_f, k=101.0, freq=2):
    """Value today of coupons paid on or before t_f plus (k + accrued) at t_f, at yield y_f."""
    if t_f <= 0.0:
        raise ValueError("t_f must be positive")
    n_cpn = int(np.floor(t_f * freq + 1e-9))
    pay = np.arange(1, n_cpn + 1) / freq
    accrued = coupon * (t_f - n_cpn / freq)
    return float(np.sum(coupon / freq * np.exp(-y_f * pay)) + (k + accrued) * np.exp(-y_f * t_f))


def smr_price(pi_f, p_close, g_f):
    if not 0.0 <= pi_f <= 1.0:
        raise ValueError("pi_f must be in [0,1]")
    return pi_f * g_f + (1.0 - pi_f) * p_close


def smr_implied_break_prob(p_obs, p_close, g_f, tol=1e-6):
    denom = p_close - g_f
    if abs(denom) < tol:
        raise ValueError("P_close ~ G_f: the SMR price carries no information about pi_f")
    raw = (p_close - p_obs) / denom
    return dict(pi_f=float(np.clip(raw, 0.0, 1.0)), raw=float(raw), clipped=not 0.0 <= raw <= 1.0)


def smr_duration(pi_f, g_f, d_fail, p_close, d_close):
    """Value-weighted probabilistic duration of an SMR tranche."""
    w = pi_f * g_f / smr_price(pi_f, p_close, g_f)
    return w * d_fail + (1.0 - w) * d_close


def spread_duration(coupon, maturity_years, s, curve=tsy_zero_curve, h=1e-4):
    up, dn = bond_price(coupon, maturity_years, [s + h, s - h], curve)
    return float((dn - up) / (2.0 * h * bond_price(coupon, maturity_years, s, curve)[0]))


# --- sanity checks, block 3 ---
g = smr_fail_leg(4.60, 0.25, 0.046)
assert abs(g - 102.15 * np.exp(-0.046 * 0.25)) < 1e-12              # the worked number
for pi in np.linspace(0.0, 1.0, 11):                                  # round trip
    assert abs(smr_implied_break_prob(smr_price(pi, 99.0, g), 99.0, g)["pi_f"] - pi) < 1e-10
assert smr_price(0.5, 103.0, g) < smr_price(0.2, 103.0, g)            # rates fell: holder short the digital
true_z = lambda m: 0.0060 + 0.0008 * m                                # a linear issuer curve
book = pd.DataFrame({"tranche_id": ["L26", "L28", "N34", "N54", "S27", "S31"],
                     "coupon": [3.50, 4.50, 5.00, 5.50, 4.60, 4.90],
                     "maturity": [1.5, 3.5, 9.5, 29.5, 2.5, 6.5],
                     "is_smr": [False, False, False, False, True, True]})
book["price"] = [bond_price(c, m, true_z(m))[0] for c, m in zip(book["coupon"], book["maturity"])]
fit = curve_match_close_price(book)
assert np.allclose(fit["z_close"], true_z(fit["maturity"].to_numpy()), atol=1e-9)   # PCHIP is exact on lines
assert not fit["extrapolated"].any()
obs = fit["p_close"].to_numpy() + np.array([0.30, 0.45])              # SMR tranches trade rich
gs = [smr_fail_leg(c, 0.25, tsy_zero_curve(0.25) + true_z(0.25)) for c in fit["coupon"]]
pis = [smr_implied_break_prob(o, pc, gg)["pi_f"] for o, pc, gg in zip(obs, fit["p_close"], gs)]
d_close = spread_duration(4.60, 2.5, true_z(2.5))
print("implied break probs:", np.round(pis, 3),
      "| SMR duration:", round(smr_duration(pis[0], gs[0], 0.25, fit["p_close"][0], d_close), 2))
```

The check that matters most is the round trip, and the check that will save you money is the one you cannot assert: if two SMR tranches of the same issuer imply very different $\hat\pi_f$, the deal has not acquired two probabilities; your curve has a kink, or one tranche is $|P^{\text{close}} - G_f| \approx 0$ and is telling you nothing loudly.

### Deep-Dive Resource Graph

- **Podcasts:** none verified for SMR mechanics specifically; the *Odd Lots* merger-arbitrage episodes listed after §15.1 cover the equity leg.
- **Practitioner Writing:** Mayer Brown and Sidley client notes on special mandatory redemption drafting (title-only); Matt Levine, *Money Stuff*, on the Kroger redemption (date to be confirmed).
- **Academic Papers:** Mitchell & Pulvino (2001), *Characteristics of Risk and Return in Risk Arbitrage*, Journal of Finance, DOI 10.1111/0022-1082.00401; Officer (2003), *Termination Fees in Mergers and Acquisitions*, Journal of Financial Economics, DOI 10.1016/S0304-405X(03)00119-3; David (1998), *Pricing the Strategic Value of Poison Put Bonds*, FEDS 1998-06, DOI 10.17016/feds.1998.06.
- **Data & Code:** Kroger Fiftieth Supplemental Indenture, https://www.sec.gov/Archives/edgar/data/56873/000110465924093481/tm2421523d7_ex4-3d1.htm ; Kroger SMR 8-K, https://www.sec.gov/Archives/edgar/data/56873/000110465924128106/tm2430972d1_8k.htm ; Tapestry termination 8-K, https://www.sec.gov/Archives/edgar/data/1116132/000114036124046713/ef20038690_8k.htm ; CourtListener docket, FTC v. Kroger, https://www.courtlistener.com/docket/68284514/federal-trade-commission-v-kroger-company/ ; EA closing 8-K (defeasance), https://www.sec.gov/Archives/edgar/data/712515/000114036126031157/ef20079099_8k.htm .


## 15.5 Antitrust and Regulatory Timelines as Survival Analysis

### 15.5.1 Desk framing: the regulator counts in working days

Every payoff in §15.2–15.4 fires on a date. The date is set by a process the RSSG reader knows as a sequence of filings: HSR notification and a 30-day initial waiting period (15 days for a cash tender offer), which a Second Request extends until 30 days after the parties certify "substantial compliance" (15 U.S.C. §18a); a European Phase I of 25 working days and a Phase II of 90 working days, extendable by 15 or 20 (European Commission merger procedures page); CFIUS, the Surface Transportation Board, state attorneys general, and a district judge with a calendar. The desk's job is to turn that sequence into a survival curve.

Theo opens the USB stick. He renames the 13-week model's columns from "Week 1 ... Week 13" to "weeks since signing," deletes the cash rows, and keeps one: "Regulatory." It is now a Kaplan–Meier curve with a spreadsheet's personality.

The base rates are lopsided in the way that makes survival analysis worth doing. Almost every HSR filing clears in the initial period; the event risk lives in a few dozen deals a year.

| FY | Adjusted transactions | Second Requests (FTC + DOJ) | Share of adjusted | Early terminations granted |
| :-- | --: | --: | --: | --: |
| 2016 | 1,772 | 54 | 3.0% | 1,102 |
| 2018 | 2,028 | 45 | 2.2% | 1,170 |
| 2020 | 1,580 | 48 | 3.0% | 861 |
| 2021 | 3,413 | 66 | 1.9% | 417 |
| 2022 | 3,029 | 47 | 1.6% | 5 |
| 2023 | 1,735 | 37 | 2.1% | 0 |
| 2024 | 1,973 | 59 | 3.0% | 3 |
| 2025 | 1,944 | 41 | 2.1% | 265 |

*Source: FTC/DOJ Hart-Scott-Rodino Annual Reports, FY2023–FY2025, Appendix A. FY2021 Second Requests per the FY2025 table (the FY2023 table shows 65).*

> **[SOURCE EXTRACTION]** *Bohn_Stein_Active_Credit_Portfolio_Management p.232:* "But what happens if some of the firms drop out of the sample due to, say, a merger or acquisition? In this case, adjustments can be made to sample survival functions of the sort shown in Figure 4.3 to account for this censorship. This results in a particular form of survival function estimator called the Kaplan-Meier (sometimes called the product limit) estimator"
>
> **Annotation.** In default modelling a merger is a nuisance: it removes a firm before you learn whether it would have defaulted, so you censor it. In this chapter the roles reverse. The merger *is* the event, and the nuisances are the deals still pending at the data cutoff, the deals whose outside date was extended, and the deals that died for reasons other than the one you are modelling. The estimator is the same; the bookkeeping is inverted. Where the desk departs from the textbook: in deal data, censoring is often *informative*. An outside date gets extended precisely when a deal is in trouble, so "still pending" is not independent of the hazard, and a naive Kaplan–Meier is optimistic about closing.

### 15.5.2 Derivation: Kaplan–Meier to competing risks

Put $t=0$ at signing (or at HSR filing; say which). Each deal ends in one of three causes, $k=c$ (close), $a$ (abandon), $b$ (litigated block), or is right-censored at the cutoff. Let $t_1 < t_2 < \dots$ be the distinct event times, $n_i$ the number of deals pending just before $t_i$, $d_{k,i}$ the number ending in cause $k$ at $t_i$, and $d_i = \sum_k d_{k,i}$.

**All-cause survival.** The Kaplan–Meier estimator and Greenwood's variance are

$$
\hat S(t) \;=\; \prod_{t_i \le t}\Big(1 - \frac{d_i}{n_i}\Big),
\qquad
\widehat{\operatorname{Var}}\big(\hat S(t)\big) \;=\; \hat S(t)^2 \sum_{t_i \le t} \frac{d_i}{n_i(n_i - d_i)},
$$

and the Nelson–Aalen cumulative hazard is $\hat\Lambda(t) = \sum_{t_i\le t} d_i/n_i$. (We write $\Lambda$ for a cumulative deal hazard only inside this section; $\lambda$ stays reserved for default intensity.)

**Cause-specific hazards with covariates.** For each cause, $h_k(t\mid x) = h_{0,k}(t)\,e^{x'\beta_k}$. Bohn and Stein state the restriction exactly: "the shape of the hazard function (and the corresponding survival function) is arbitrary, but the impact ratio of the hazards over time is constant" (Bohn_Stein_Active_Credit_Portfolio_Management p.233). With $R_i = \{j: t_j \ge t_i\}$ the risk set, the Breslow partial log-likelihood for cause $k$ is

$$
\ell_k(\beta) \;=\; \sum_{i:\,\text{cause}_i = k}\Big[x_i'\beta - \log\!\sum_{j\in R_i} e^{x_j'\beta}\Big],
\qquad
\nabla \ell_k \;=\; \sum_{i:\,\text{cause}_i = k}\big(x_i - \bar x_w(t_i)\big),
$$

with $\bar x_w(t_i)$ the $e^{x'\beta}$-weighted mean of the covariates in $R_i$. Deals ending in other causes are censored for cause $k$; that is correct for cause-specific hazards and wrong for anything else.

**Cumulative incidence.** The probability of ending in cause $k$ by $t$ is not $1 - e^{-\Lambda_k(t)}$, because a deal that is blocked cannot later close. The Aalen–Johansen estimator is

$$
\hat F_k(t) \;=\; \sum_{t_i \le t} \hat S(t_{i}^{-})\,\frac{d_{k,i}}{n_i},
\qquad
\sum_k \hat F_k(t) \;=\; 1 - \hat S(t),
$$

and the identity on the right is exact, which makes it the best unit test in the chapter.

**From clocks to PnL.** For a position whose price jumps by $\Pi_k(t)$ on outcome $k$ at $t$, under $\mathbb{P}$,

$$
\mathbb{E}^{\mathbb{P}}[\text{PnL}] \;=\; \int_0^{\infty} e^{-rt}\,S(t)\,\big[h_c(t)\Pi_c(t) + h_a(t)\Pi_a(t) + h_b(t)\Pi_b(t)\big]\,dt \;+\; \text{carry}.
$$

**Silence is data.** Each milestone that passes quietly (the 30-day wait expires with no Second Request; Phase I ends without Phase II; a complaint deadline passes) updates the deal probability by Bayes' rule, with $q_d$ and $q_b$ the probabilities of a quiet milestone under "deal" and "break," conditional on quiet so far:

$$
\pi_d^{+} \;=\; \frac{\pi_d\, q_d}{\pi_d\, q_d + (1-\pi_d)\, q_b},
$$

which rises whenever $q_d > q_b$. Giglio & Shue (2014) show that equity markets underreact to the information in the passage of time during pending mergers. If the credit market does the same, a target bond's spread should drift tighter through silent milestones; that is Chapter 10's trend signal with a legal calendar for a clock.

> **Poker Table.** Ines on the Second Request: "It's a tell, but a cheap one. In FY2024 the agencies issued 59 Second Requests and brought 32 merger enforcement actions, most of them consents and abandonments; the FTC litigated six. A Second Request means the hand goes to the river, not that you lose it. The expensive tell is the one nobody announces: the timing agreement with the agency, which you infer when the parties stop guiding to a close date." Replay the hand: markouts on the target's bonds over the ten days after each Second Request, split by eventual outcome. If the bonds that eventually closed sold off as hard as the ones that were blocked, the market was paying you to know the base rate.

> **Trend Watch.** *Regulatory regime as a shift in the baseline hazard, 2016–2026.* Early terminations of the HSR waiting period, the fast lane for clean deals, ran at 1,102 in FY2016 and 1,220 in FY2017, fell to 417 in FY2021 after the agencies suspended the practice, to 5 in FY2022 and 0 in FY2023, and came back to 265 in FY2025 (FTC/DOJ HSR Annual Reports, Appendix A). The second-request rate meanwhile oscillated between 1.6% and 3.0% of adjusted transactions. In procedure, the new HSR form took effect February 10, 2025; a federal district court vacated it on February 12, 2026 (FTC notice dated February 13, 2026); the Fifth Circuit granted an administrative stay on February 19 and then denied a stay pending appeal on March 19, 2026, and the agencies now accept filings on either form (FTC Premerger Notification Program page). What it means for the desk: the baseline $h_{0,c}(t)$ in the first 30 days is not stationary across administrations, so never pool FY2016–2019 clocks with FY2022–2024 clocks without a regime covariate, and expect the first month of every filing in 2025–26 to carry procedural variance that had nothing to do with antitrust.

### Specification for AI Implementation

**What ROBO built from the vague version.** "Estimate how long the deal will take." ROBO averaged signing-to-close times over closed deals and returned seven months. Every deal that had been blocked, abandoned or was still pending had been dropped as "missing data." Survivorship bias, delivered with confidence.

**The precise spec.** From-scratch estimators (no `lifelines`): `kaplan_meier` with Greenwood bands, `nelson_aalen`, `aalen_johansen` for cumulative incidence, `cox_ph` by Breslow partial likelihood with analytic gradient and Hessian through `scipy.optimize`, a seeded synthetic cohort with known cause-specific Weibull hazards, and the Bayesian milestone path. Shapes: `times (n,)` in years ACT/365, `event (n,)` in $\{0,1\}$, `cause (n,)` in $\{0,1,2,3\}$ with 0 = pending, `X (n,p)`. Cox returns `beta (p,)`, `se (p,)`, baseline cumulative hazard `(m,2)` at $x=0$, and Schoenfeld-residual time correlations (reported, not asserted). Working-day calendars are converted to years by the caller, never inferred.

```python
# ---- block 4: deal clocks as competing-risks survival data, from scratch ----
COVARIATES = ["second_request", "horizontal", "log_value", "n_jurisdictions", "sponsor", "regime"]
BETA_TRUE = {1: np.array([-1.20, -0.30, -0.15, -0.10, 0.20, -0.40]),   # close
             2: np.array([0.60, 0.20, -0.10, 0.05, 0.30, 0.30]),       # abandon
             3: np.array([1.50, 1.00, 0.20, 0.00, -0.50, 0.80])}       # litigated block
WEIBULL = {1: (1.6, 0.55), 2: (1.1, 6.0), 3: (1.3, 12.0)}              # (shape, scale in years)


def synthetic_deal_cohort(n=600, seed=11):
    rng = np.random.default_rng(seed)
    X = pd.DataFrame({"second_request": rng.binomial(1, 0.15, n), "horizontal": rng.binomial(1, 0.40, n),
                      "log_value": rng.standard_normal(n), "n_jurisdictions": rng.poisson(2.0, n),
                      "sponsor": rng.binomial(1, 0.30, n), "regime": rng.binomial(1, 0.50, n)})
    xv = X[COVARIATES].to_numpy(dtype=float)
    latent = np.column_stack([b * (rng.exponential(size=n) / np.exp(xv @ BETA_TRUE[k])) ** (1.0 / a)
                              for k, (a, b) in WEIBULL.items()])           # inverse-CDF Weibull PH
    t_event, cause = latent.min(axis=1), latent.argmin(axis=1) + 1
    t_cens = rng.uniform(0.5, 4.0, n)                                      # independent data cutoff
    X["time"] = np.minimum(t_event, t_cens)
    X["cause"] = np.where(t_event <= t_cens, cause, 0)
    return X


def _risk_table(times, events):
    times, events = np.asarray(times, dtype=float), np.asarray(events, dtype=int)
    if times.ndim != 1 or times.shape != events.shape or np.any(times < 0):
        raise ValueError("times and events must be 1-d, same length, times >= 0")
    ut, d = np.unique(times[events == 1], return_counts=True)
    n_risk = times.size - np.searchsorted(np.sort(times), ut, side="left")
    return ut, n_risk, d


def kaplan_meier(times, events, z=1.96):
    ut, n, d = _risk_table(times, events)
    S = np.cumprod(1.0 - d / n)
    with np.errstate(divide="ignore", invalid="ignore"):
        gw = np.cumsum(np.where(n > d, d / (n * (n - d)), np.inf))       # Greenwood
        se = np.where(S > 0, S * np.sqrt(gw), 0.0)
    return pd.DataFrame({"t": ut, "n_risk": n, "d": d, "S": S, "se": se,
                         "lo": np.clip(S - z * se, 0, 1), "hi": np.clip(S + z * se, 0, 1)})


def nelson_aalen(times, events):
    ut, n, d = _risk_table(times, events)
    return pd.DataFrame({"t": ut, "H": np.cumsum(d / n), "var": np.cumsum(d / n ** 2)})


def aalen_johansen(times, cause, n_causes=3):
    times, cause = np.asarray(times, dtype=float), np.asarray(cause, dtype=int)
    ut, n, d = _risk_table(times, (cause > 0).astype(int))
    S = np.cumprod(1.0 - d / n)
    S_minus = np.concatenate(([1.0], S[:-1]))
    out = {"t": ut, "S": S}
    for k in range(1, n_causes + 1):
        tk, ck = np.unique(times[cause == k], return_counts=True)
        dk = np.zeros(ut.size)
        dk[np.searchsorted(ut, tk)] = ck
        out[f"F{k}"] = np.cumsum(S_minus * dk / n)
    return pd.DataFrame(out)


def cox_ph(times, event, X):
    t, e, X = (np.asarray(times, dtype=float), np.asarray(event, dtype=int), np.asarray(X, dtype=float))
    order = np.argsort(-t, kind="mergesort")
    t, e, X = t[order], e[order], X[order]
    last = np.searchsorted(-t, -t, side="right") - 1        # risk set of row i = rows 0..last[i]
    Xc, ev = X - X.mean(axis=0), e == 1                     # centring leaves beta unchanged
    if not ev.any():
        raise ValueError("no events")

    def parts(beta):
        eta = Xc @ beta
        w = np.exp(eta - eta.max())                         # log-sum-exp guard
        s0 = np.cumsum(w)[last]
        s1 = np.cumsum(w[:, None] * Xc, axis=0)[last]
        s2 = np.cumsum(w[:, None, None] * Xc[:, :, None] * Xc[:, None, :], axis=0)[last]
        xbar = s1[ev] / s0[ev, None]
        ll = np.sum(eta[ev] - eta.max() - np.log(s0[ev]))
        info = np.sum(s2[ev] / s0[ev, None, None] - xbar[:, :, None] * xbar[:, None, :], axis=0)
        return ll, np.sum(Xc[ev] - xbar, axis=0), info, xbar

    res = optimize.minimize(lambda b: (-parts(b)[0], -parts(b)[1]), np.zeros(X.shape[1]), jac=True,
                            hess=lambda b: parts(b)[2], method="trust-exact", options={"gtol": 1e-6})
    beta = res.x
    _, _, info, xbar = parts(beta)
    se = np.sqrt(np.diag(np.linalg.inv(info)))
    eta = X @ beta                                          # uncentred: baseline at x = 0
    s0 = np.cumsum(np.exp(eta - eta.max()))[last] * np.exp(eta.max())
    ut, d = np.unique(t[ev], return_counts=True)
    H0 = np.cumsum(d / s0[np.searchsorted(-t, -ut, side="left")])
    resid = Xc[ev] - xbar                                   # Schoenfeld residuals
    ph_corr = np.array([np.corrcoef(t[ev], resid[:, j])[0, 1] for j in range(X.shape[1])])
    return dict(beta=beta, se=se, baseline=np.column_stack([ut, H0]), ph_corr=ph_corr,
                converged=bool(res.success))


def bayes_deal_prob_path(pi0, milestones):
    """milestones: (t, q_deal, q_break) = P(milestone passes quietly | quiet so far, hypothesis)."""
    if not 0.0 < pi0 < 1.0:
        raise ValueError("pi0 must be in (0,1)")
    rows, pi = [(0.0, pi0)], pi0
    for t, q_d, q_b in milestones:
        if not (0.0 < q_d <= 1.0 and 0.0 < q_b <= 1.0):
            raise ValueError("quiet probabilities must be in (0,1]")
        pi = pi * q_d / (pi * q_d + (1.0 - pi) * q_b)
        rows.append((t, pi))
    return pd.DataFrame(rows, columns=["t", "pi_d"])


# --- sanity checks, block 4 ---
t_nc = np.random.default_rng(3).exponential(1.0, 50)                # no censoring: KM = 1 - ECDF
assert np.allclose(kaplan_meier(t_nc, np.ones(50, dtype=int))["S"], 1.0 - np.arange(1, 51) / 50)
cohort = synthetic_deal_cohort()
aj = aalen_johansen(cohort["time"], cohort["cause"])
assert np.allclose(aj[["F1", "F2", "F3"]].sum(axis=1), 1.0 - aj["S"], atol=1e-12)
km = kaplan_meier(cohort["time"], (cohort["cause"] > 0).astype(int))
assert np.allclose(km["S"].to_numpy(), aj["S"].to_numpy())
fit = cox_ph(cohort["time"], (cohort["cause"] == 1).astype(int), cohort[COVARIATES])
assert np.all(np.abs(fit["beta"] - BETA_TRUE[1]) < 4.0 * fit["se"]), (fit["beta"], fit["se"])
path = bayes_deal_prob_path(0.80, [(30 / 365, 0.97, 0.55), (0.15, 0.95, 0.70), (0.50, 0.99, 0.90)])
assert path["pi_d"].iloc[0] == 0.80 and path["pi_d"].is_monotonic_increasing
print("close-hazard beta:", np.round(fit["beta"], 2), "+/-", np.round(fit["se"], 2))
print("P(block by 2y):", round(float(np.interp(2.0, aj["t"], aj["F3"])), 3),
      "| PH-check corr:", np.round(fit["ph_corr"], 2), "| pi_d path:", np.round(path["pi_d"].to_numpy(), 3))
```

Read the printed Second Request coefficient as a time multiplier: with a Weibull shape near 1.6, a close hazard multiplied by $e^{-1.2}\approx 0.30$ stretches the median clock by about $0.30^{-1/1.6}\approx 2.1$ times. That is the 30-days-versus-a-year gap in the HSR data, recovered from a seeded cohort, which is the point: before you fit real deals, prove the engine finds the parameters you planted.

### Deep-Dive Resource Graph

- **Podcasts:** *Bloomberg Odd Lots* episodes on the 2021–2024 FTC and merger enforcement (titles and dates to be confirmed before linking).
- **Practitioner Writing:** Dechert, *DAMITT* (Dechert Antitrust Merger Investigation Timing Tracker) reports on the duration of significant US and EU merger investigations (title-only).
- **Academic Papers:** Giglio & Shue (2014), *No News Is News: Do Markets Underreact to Nothing?*, Review of Financial Studies, DOI 10.1093/rfs/hhu052; Dikova, Sahib & van Witteloostuijn (2010), *Cross-Border Acquisition Abandonment and Completion*, Journal of International Business Studies, DOI 10.1057/jibs.2009.10; Wollmann (2019), *Stealth Consolidation: Evidence from an Amendment to the Hart-Scott-Rodino Act*, AER: Insights, DOI 10.1257/aeri.20180137.
- **Data & Code:** FTC/DOJ HSR Annual Reports, FY2023 https://www.ftc.gov/system/files/ftc_gov/pdf/fy2023hsrreport.pdf and FY2024 https://www.ftc.gov/system/files/ftc_gov/pdf/FY24-HSR-ANNUAL-REPORT-FOR-TRANSMITTAL-TO-CONGRESS.pdf ; European Commission merger procedures, https://competition-policy.ec.europa.eu/mergers/procedures_en ; CourtListener REST API, https://www.courtlistener.com/help/api/ .


## 15.6 Target vs. Acquirer: Spread Compression, Acquirer Widening, and Event Momentum

The academic base rates are short and worth memorizing. Billett, King & Mauer (2004) find that target bondholders gain on average, with the gains concentrated in below-investment-grade targets bought by better-rated acquirers, while acquirer bondholders do not share in them. Furfine & Rosen (2011) find that mergers raise the acquirer's default risk on average. Acharya & Johnson (2010) find that the equity and CDS of LBO targets move before the announcement, and more so when more insiders are involved, which is Ines's hand history in academic form: somebody at this table knew more than you.

The trade the chapter's machinery suggests is event momentum. Run `bayes_deal_prob_path` on each pending deal; go long target bonds whose $\pi_d(t)$ is rising through silent milestones faster than their spread is tightening toward the acquirer's curve; size by Paleologo's rule that a shorter runway to the event means a smaller position, because "there is less time to build it" (Paleologo_Advanced_Portfolio_Management p.152). Then, before anyone says the word alpha, strip the acquirer's own spread change, the rates leg, carry and the market factor from the target's return. Most of what a target bond does after announcement is the acquirer's beta wearing the target's CUSIP. IDO or it didn't happen.

## 15.7 When the Deal Dies: The Merger as the Credit

For a weak target, the bond price before resolution is a mixture of two curves:

$$
P^{\text{tgt}}_t \;=\; \pi_d(t)\,P^{\text{acq}}_t \;+\; \big(1-\pi_d(t)\big)\,P^{\text{sa}}_t,
\qquad
\Delta P^{\text{tgt}}\big|_{\text{block}} \;=\; -\,\pi_d(t^-)\,\big(P^{\text{acq}}_t - P^{\text{sa}}_t\big),
$$

where $P^{\text{sa}}$ is the standalone value. A block is a jump of known sign and estimable size on a date the court publishes, which a diffusion VaR will understate every time (Chapter 5's mixtures; Chapter 14's distress dynamics).

Spirit Airlines is the template. On January 16, 2024 the District of Massachusetts enjoined the JetBlue merger; three days later Spirit reported \$1.3bn of liquidity at year-end and sale-leasebacks of 25 aircraft. On March 4, 2024 the parties terminated by mutual agreement; JetBlue paid Spirit \$69mm, and Spirit's stockholders had already received about \$425mm of prepayments while the agreement was in effect. On November 18, 2024 Spirit filed a prearranged Chapter 11 with a restructuring support agreement signed by a supermajority of its loyalty-program and convertible noteholders: a \$350mm backstopped equity investment, equitization of \$795mm of funded debt, and a \$300mm DIP from existing bondholders (Spirit 8-Ks and releases, EDGAR). Signing to block took about 18 months; block to bankruptcy took about ten.

Mags reads the prepayment line twice. "The ticking money went to the equity. The ticking clock went to the bonds."

## 15.8 Case Study: Warner Bros. Discovery 2025–26, the Covenant Strip and the Ticking Fee

**The strip came first.** On June 9, 2025, before any buyer had signed, WBD launched tender offers and consent solicitations for substantially all the notes of Discovery Communications, WarnerMedia Holdings, Warner Media LLC and Historic TW. Requisite consents arrived on June 16, and the supplemental indentures "eliminate substantially all of the restrictive covenants" and certain events of default once operative (WBD 8-K, June 13, 2025, EDGAR). Which protections survived in each series, the change-of-control offer included, must be checked supplemental indenture by supplemental indenture. The structural lesson does not wait for that check: the issuer exercised its counter-option *before* the put could be in the money, when consent was cheap.

**The loan said what it was.** A \$15bn bridge was documented as the "Non-Investment Grade Leveraged Bridge Loan Agreement" (June 26, 2025). Kaz: "They named the loan after its rating?" Theo: "It's the only honest title in the data room." It was refinanced on June 4, 2026 with a \$13bn term loan B at SOFR+250 and a €1,717mm term loan B at EURIBOR+250 at Discovery Global Holdings, maturing June 4, 2033, whose change of control, "such as the consummation of the previously disclosed proposed acquisition of the Company by Paramount Skydance Corporation," permits acceleration (WBD 8-K, June 2026). Entry 5 of the §15.1 table, with the trigger named in advance.

**Three suitors, one clock.** WBD signed with Netflix in early December 2025, amended on January 19, 2026 to \$27.75 a share in all cash, and then signed with Paramount Skydance on February 27, 2026 at \$31.00 in cash plus "Ticking Consideration" of \$0.00277778 per share per day after September 30, 2026, capped at \$0.25 per 90 days. Stockholders approved on April 23, 2026. The deal closed on October 6, 2026 at \$31.01666668 a share: exactly six days of ticking ($6 \times 0.00277778$), or \$41,886,975.78 in aggregate. At closing WBD repaid the June 2026 term loans and its October 2024 revolver, and WBD subsidiaries guaranteed Skydance's new notes and credit agreement (WBD 8-Ks, EDGAR).

**Pricing the ticking fee.** Annualized, $0.00277778 \times 365 \approx \$1.014$, about 3.3% a year on \$31. That compensates shareholders for time, not for break risk, which they still carry. A survival model prices the rest: the expected ticking payment is $0.00277778 \times \mathbb{E}\big[(\tau_c - t^{*})^{+}\big]$ in days, with $t^{*}$ = September 30, 2026, and the competing-risks curve of §15.5 supplies the law of $\tau_c$.

**What the desk should have flagged.** For the legacy bondholders, the decisive date was June 16, 2025, eight months before the buyer was chosen. Our reading, to be checked against the guarantee documents: once WBD subsidiaries guarantee acquisition debt, the new money has claims at the same entities as the legacy notes, and stripped indentures no longer police it. The strip, not the merger, was the credit event.

## 15.9 Desk Debrief

- **Every deal clause is a payoff function.** Write it as (outcome, trigger, price at trigger), and store the issuer's counter-options (consent strip, defeasance, exchange offer) next to it in the security master.
- **CoC moneyness is coupon vintage.** The put cares about $101 - P$, not the credit story. The IG double trigger needs both inspectors, and for LBOs the trigger and the payoff covary ($M > 1$).
- **Portability is a short digital on a number the sponsor chooses.** Every point of permitted add-back lowers the odds that your put survives.
- **The SMR is a $\mathbb{Q}$ break gauge inside the acquirer's curve.** Its resolution is $|P^{\text{close}} - G_f|$, its control group is contaminated, and its duration jumps on ruling day.
- **Regulatory clocks are competing-risks survival data.** Censoring is informative, regimes shift $h_0$, and $\sum_k F_k = 1 - S$ is your unit test.
- **Silence is data, and beta is not alpha.** Update $\pi_d$ through quiet milestones, then strip the acquirer's beta before claiming the event. IDO or it didn't happen.
- **The most expensive three words have a cousin:** "defease certain obligations."

**The Spec You Hand the Robot.** "Build `event_credit_engine.py` (numpy, scipy, pandas; seeded). (1) `price_coc_put`: Monte Carlo over post-close spreads (decimal), deal × trigger × issuer-counter-option probabilities integrated analytically, bond priced on the post-close curve, return value in points per 100, stderr and $M$; exact zeros for degenerate inputs. (2) `curve_match_close_price`, `smr_fail_leg`, `smr_implied_break_prob`, `smr_duration`: PCHIP Z-spread curve over non-SMR tranches with an extrapolation flag; accrued to the redemption date; raise when $|P^{\text{close}} - G_f| < 10^{-6}$; clip and report. (3) `kaplan_meier`, `nelson_aalen`, `aalen_johansen`, `cox_ph` (Breslow, log-sum-exp, analytic gradient and Hessian), `bayes_deal_prob_path`. Assert: closed-form match for a constant spread; SMR round trip to $10^{-10}$; KM equals $1-$ECDF without censoring; CIFs sum to $1-\hat S$ within $10^{-12}$; Cox recovers planted $\beta$ within four standard errors. Units: years ACT/365 for clocks, 30/360 accrued, spreads decimal, prices per 100 face. Never pool regimes without a regime covariate. Never mix $\mathbb{P}$ and $\mathbb{Q}$ without saying so."

### Exercises

1. **The defeasance arithmetic.** With block 1, price the put on 1.85% and 2.95% bonds with 4.5 and 24.5 years remaining under an LBO spread of 350bp *(illustrative)*. Then compute what a sponsor saves per 100 face by depositing Treasuries instead of paying 101. Explain why 95% of EA's legacy holders declined the tender, and whether they were right.
2. **The blind thermometer.** Find the parallel Treasury move after issue at which a 4.60% three-year SMR tranche has $P^{\text{close}} = G_f$. Explain why $\hat\pi_f$ is undefined there and which instrument you would use instead.
3. **The vintage anomaly.** For an IG issuer on a take-private watch list, regress same-issuer Z-spreads on coupon with maturity controls. Derive the sign the embedded put predicts for the coupon coefficient, and design the test that tells the put apart from the low-coupon bonds' lower convexity and better index eligibility.
4. **Was the ticking fee generous?** Fit a Weibull to time-to-close from the Paramount Skydance signing with a median of seven months *(illustrative)*, and compute the expected ticking consideration per share. Compare it with the \$0.0167 realized and with a 2026 cash yield. Who wrote the better option?
5. **Kaz assumes Gaussian.** Kaz proposes a normal distribution for days-to-clearance. Using the HSR table, show that a two-component mixture (cleared in the initial period versus Second Request) beats every Gaussian on log-likelihood, and explain what the Gaussian implies about deals clearing before they file.

### Deep-Dive Resource Graph

- **Podcasts:** *Bloomberg Odd Lots* episodes on merger arbitrage and antitrust; *Capital Allocators* conversations with event-driven managers; *Petition* coverage of Spirit Airlines' Chapter 11 (all title-only; confirm episodes before linking).
- **Practitioner Writing:** Matt Levine, *Money Stuff*, on the WBD bidding contest and the EA take-private (dates to be confirmed); Covenant Review, Xtract Research and 9fin reports on portability and change-of-control terms (title-only).
- **Academic Papers:** Asquith & Wizman (1990), *Event Risk, Covenants, and Bondholder Returns in Leveraged Buyouts*, JFE, DOI 10.1016/0304-405X(90)90026-V; Crabbe (1991), *Event Risk: An Analysis of Losses to Bondholders and "Super Poison Put" Bond Covenants*, JF, DOI 10.1111/j.1540-6261.1991.tb02680.x; Billett, Jiang & Lie (2010), *The Effect of Change-in-Control Covenants on Takeovers*, JCF, DOI 10.1016/j.jcorpfin.2009.09.005; Acharya & Johnson (2010), *More Insiders, More Insider Trading*, JFE, DOI 10.1016/j.jfineco.2010.08.002.
- **Data & Code:** WBD–Paramount Skydance agreement 8-K, https://www.sec.gov/Archives/edgar/data/1437107/000143710726000018/disca-20260227.htm ; WBD closing 8-K, https://www.sec.gov/Archives/edgar/data/1437107/000119312526415055/d200872d8k.htm ; WBD consent-solicitation 8-K, https://www.sec.gov/Archives/edgar/data/1437107/000143710725000151/disca-20250613.htm ; Spirit termination release, https://www.sec.gov/Archives/edgar/data/1498710/000149871024000124/a240304pressreleasefinal.htm .

<!-- STATUS: COMPLETE -->
