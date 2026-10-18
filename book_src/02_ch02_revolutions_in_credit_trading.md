# Chapter 2: The Revolutions in Credit Trading

*Tuesday, 3:41 p.m. Nineteen minutes to the index mark. The desk smells like burnt espresso and somebody else's DV01.*

The ticket on Theo Marsh's screen is the first one that is entirely his: **buy \$4mm, Halvorsen Freight 7.125% senior notes due 2030, B2,** sent all-to-all. (Halvorsen is fictional. The chime is not.) Responders get two minutes. In the old world Theo would have called three dealers, waited for two of them to call back, and spent the wait rereading the restricted payments covenant. In this world eleven responses arrive before he has found the covenant: four banks, two non-bank market makers, three asset managers, a hedge fund, and something whose name is a string of capital letters.

He lifts the best offer. The cover, the second-best response, is three-eighths of a point behind. Done in forty seconds.

"Back in my day," says Marguerite "Mags" Dunleavy, without looking up, "I priced these by phone and by grudge. You called Steve, Steve gave you a number that punished you for something you did in 1997, and the print showed up on TRACE seventy-five minutes later, if it showed up at all."

"Seventy-five minutes?"

"July 2002. The regulator gave us transparency the way a casino gives you a free drink: about five hundred bonds, seventy-five minutes late."

Ines Okafor rolls her chair over and studies the eleven rows the way she once studied a final table. "Eleven players. Nice pot, tight cover. Now tell me which one of them just got off a lender call."

Theo knows exactly what a lender call does to an offer, and he reaches for the indenture out of habit. "But what does the credit agreement say about electronic trading?"

"Nothing, Theo." Dr. Kasimir "Kaz" Lind keeps typing. "The bond doesn't know how it was traded. The dataset does."

That exchange is the whole chapter. A bond's *value* lives in its documents. Its *tradability* lives in its data exhaust: how many prints it gets per day, how many dealers answer an RFQ for it, how far the cover sits from the winner, whether it sits in an ETF redemption basket, and which of its trades the public tape refuses to show you. **The question this chapter answers: what changed in the plumbing of credit trading between 2002 and 2026, how big was each change, and why did those changes, rather than any new factor, make systematic credit possible?**

By the end of this chapter you will be able to: date seven changes in market structure (TRACE plus six "revolutions") and size each with sourced 2018–2026 numbers; read TRACE's size caps as a censoring problem and back out the tail index of hidden block sizes; fit an electronic-adoption S-curve with an honest ceiling; price an RFQ as an order-statistics problem, and show why eleven responders anchored to one composite are worth less than two independent ones; compute Barclays LCS and Man's transaction-cost decomposition with the units right; treat protocol choice (RFQ, all-to-all, portfolio trade, ETF) as cost minimization; and show why a fall in cost per ticket raises the breadth, and so the information ratio, a quant strategy can harvest.

A housekeeping note for Kaz: every expectation in this chapter is under the physical measure $\mathbb{P}$. Market-structure statistics record what traders actually did. A count of RFQ responses has no pricing measure.

## 2.1 The Desk View: Execution Certainty and a Modelable Cost

Start with how a market maker sees a systematic credit book. A quant credit strategy is a function from data to target weights. Every day, or every hour, it says "own more of these 400 bonds and less of those 300." The optimizer behind those targets makes an assumption it never states: that the bonds can actually be traded, at a cost it can predict.

For most of its history, credit broke that assumption. Man Group's systematic team put the barrier plainly:

> **[SOURCE EXTRACTION]** *Man_Revolutions_in_Credit_Trading_2023 p.2:* "The greatest barriers to systematic approaches breaking through in credit have traditionally been execution and the ability to model transaction costs and liquidity within decades-old manual processes."
>
> **Annotation.** Notice what is *not* on the list: signals. By 2023, credit factors (value, momentum, quality, low risk) had more than a decade of published evidence behind them (Chapters 9–12). What was missing was a way to turn a target weight into a fill. The sentence recasts the history of quant credit as a history of plumbing, and that is this chapter's frame. Where the 2026 desk departs: in liquid IG, "manual processes" no longer bind, because most small tickets are electronic and many are auto-executed. They still bind for high-yield blocks, stressed names and anything near a liability-management transaction (Chapters 13–14). The barrier did not disappear. It moved down the credit curve, into Theo's old neighborhood.

On the next page of the same paper, Man named the two conditions a systematic strategy needs:

> **[SOURCE EXTRACTION]** *Man_Revolutions_in_Credit_Trading_2023 p.4:* "Two of the key challenges for such systematic techniques are having a high certainty of execution and having a relatively good sense of the likely transaction costs, as quantitative approaches depend on being able to model accurately which securities can be traded and at what cost."
>
> **Annotation.** These are the two inputs a portfolio optimizer cannot do without. One is a *feasible set*: which bonds can be traded. The other is a *cost function*: at what price. Write them as $\Pr(\text{fill}\mid x)$ and $\mathbb{E}[c \mid \text{fill}, x]$, where $x$ is a vector of ticket features such as size, rating, age, recent prints, and the number of dealers who answered the last RFQ. Every revolution in this chapter improves one or both. TRACE made $\mathbb{E}[c]$ estimable after the fact. RFQ platforms made it measurable at the moment of trade. All-to-all and automation raised $\Pr(\text{fill})$ for small tickets. Portfolio trading and ETFs created fills for baskets that no single-bond RFQ could absorb. The modern departure is that by 2026 both quantities are *forecast*, not just measured, and §2.5 shows them feeding a router rather than a spreadsheet.

Man's earlier paper explains why this matters to an optimizer. The subject of the sentence is the optimizer's solution:

> **[SOURCE EXTRACTION]** *Man_Quantitative_Credit_Alpha_Early_Mover_2022 p.19:* "is no longer really optimal if that bond is not available for purchase. In addition, unfilled orders can lead to unintended and potentially unmodelled risk exposures."
>
> **Annotation.** An optimal portfolio you cannot buy is not optimal, and an unfilled order is not a zero. It is an *unintended position*. If you sold the bond you meant to swap out of but failed to buy its replacement, you are now short beta you never chose. A modern desk logs every unfilled order, and the realized fill rate becomes a training label (§2.5). The desk motto applies to execution as much as to alpha: *IDO or it didn't happen*. A backtest that assumes every target fills is reporting the alpha of a market that does not exist.

Here is the RSSG translation, because Theo needs one. At PJT the unit of analysis was a document and a process. Prices arrived by phone, late, from a dealer who was also your counterparty. That world had one kind of liquidity information, which was whatever Steve said. A systematic desk needs liquidity to be a *variable*: measured for every bond every day, forecastable, and comparable across 10,000 CUSIPs. Electronification is the process that turned liquidity from a relationship into a variable. The rest of this chapter dates that process, sizes it, and shows where it has still not reached.

## 2.2 Revolution 0: TRACE, or the Dataset Appears

Before you can trade a bond on a model, the model needs training data. For US corporates that data is TRACE, FINRA's Trade Reporting and Compliance Engine. It underlies everything that follows, so we call it Revolution 0. It did not change how bonds traded. It changed what anyone could *know* about how they traded.

> **[SOURCE EXTRACTION]** *Bohn_Stein_Active_Credit_Portfolio_Management p.91:* "In the past, credit markets have been hampered by lack of transparency in pricing, making it difficult to mark a portfolio to market let alone hedge or trade a particular exposure."
>
> **Annotation.** Bohn and Stein wrote when TRACE was a few years old, and their footnote 6 on the same page dates its origin: in September 1998 the SEC asked the NASD (now FINRA) to provide more transparency in corporate debt. The sentence lists three uses in rising order of difficulty: mark, hedge, trade. A systematic desk needs all three every day for every bond in its universe. Where the 2026 desk departs: transparency is no longer the scarce input for the liquid half of the market. The scarce input is *clean* transparency, meaning duplicate prints, processed voice trades and capped sizes have all been dealt with. That is the subject of the rest of this section.

### 2.2.1 The dissemination timeline

TRACE did not arrive all at once. FINRA phased it in by issue size and rating and cut the reporting clock in steps. The dates below come from the FINRA TRACE Fact Book (2025 edition) and FINRA's reporting-timeframes page. The one-minute saga comes from SEC and FINRA releases.

> **Trend Watch.** **The reporting clock, 2002–2026: a twenty-four-year countdown that stopped at fifteen minutes.**
>
> | Date | Change | Source |
> | :-- | :-- | :-- |
> | Sept 1998 | SEC asks NASD for corporate-debt transparency | `Bohn_Stein p.91`, fn. 6 |
> | July 1, 2002 | TRACE launches with 75-minute reporting. Phase I disseminates IG issues of \$1bn or more plus the "FIPS 50" HY names: about 520 securities by end-2002 | FINRA TRACE Fact Book 2025 |
> | Mar 3 and Apr 14, 2003 | Phase IIa (AAA/AA/A issues of \$100mm or more) and Phase IIb (120 BBB plus 50 HY names): about 4,650 bonds | Fact Book |
> | Oct 1, 2003 | Clock cut to 45 minutes | Fact Book |
> | Oct 1, 2004 | Phase IIIa; clock cut to 30 minutes | Fact Book |
> | Feb 7, 2005 | Phase IIIb: about 99% of public transactions and 95% of par value disseminated immediately | Fact Book |
> | July 1, 2005 | Clock cut to 15 minutes | Fact Book |
> | Jan 9, 2006 | Immediate dissemination of all public TRACE-eligible corporates | Fact Book |
> | June 30, 2014 | Rule 144A corporate trades disseminated | Fact Book |
> | May 15, 2023 | Portfolio-trade modifier required on corporate bond reports | Fact Book; FINRA RN 22-12 |
> | Jan 11, 2024 | FINRA files SR-FINRA-2024-004 to cut the 15-minute outer limit to one minute | SEC Rel. 34-101121 |
> | Sept 20, 2024 | SEC approves the one-minute rule | SEC Rel. 34-101121 |
> | Feb 5, 2025 | FINRA says it will not set an effective date | Mayer Brown, *Free Writings*, Feb 10, 2025 |
> | Dec 4, 2025 | FINRA "is not moving forward"; the 15-minute standard stays | FINRA RN 25-17 |
> | June 8, 2026 | Optional aggregate allocation reporting begins | FINRA RN 25-17 |
> | Aug 31, 2026 | Expanded affiliate-principal indicator becomes available on a voluntary basis (mandatory Aug 2, 2027) | FINRA RN 26-16 |
>
> **What it means for the desk.** The headline clock (75, then 45, 30 and 15 minutes) understates how fast the market actually is. FINRA's own statistics, summarized in the SEC's 2024 approval order, show that in 2022, 82.9% of trades executed between 8:00 a.m. and 6:15 p.m. ET were already reported within one minute, and 90.6% within three. The rule would have accelerated "up to 16.4% of current annual trading volume, or up to 6.1 million trades and 20 trillion dollars in par value" (SEC Rel. 34-101121). So FINRA spent 2022 to 2025 trying to make the market report in one minute, found that 83% of it already did, and dropped the rule. It was the most TRACE-like thing TRACE has ever done: the information arrived, late, and changed nothing. For a quant, the interesting number is the remaining 17%. The trades that still report slowly are the manual ones, and manual trades are where blocks and distressed names live.

Model the print delay $\ell$ as a two-component mixture:

$$
\Pr(\ell \le u) = \pi\,F_{\text{fast}}(u) + (1-\pi)\,F_{\text{slow}}(u), \qquad 0 \le u \le 15 \text{ min}.
$$

Here $F_{\text{fast}}$ is the delay distribution of straight-through electronic reports (seconds), $F_{\text{slow}}$ is the delay distribution of manually booked voice trades (minutes), and $\pi$ is the weight on the electronic component. FINRA's 2022 statistic pins down one point of the mixture: $\Pr(\ell \le 1\text{ min}) = 0.829$. What matters for feature design is that $\pi$ is *not constant across bonds*. It is lowest exactly where the information is richest: large, stressed, voice-traded tickets. So a feature like "minutes since last print" means different things in different bonds. In an IG bond a stale print means nobody traded. In a CCC bond it may mean somebody traded big and the ticket is still being booked.

### 2.2.2 The caps: censoring as a data problem

Two strings in the TRACE feed matter more to a credit quant than any others: `5MM+` and `1MM+`. FINRA disseminates the exact size of an IG trade only up to \$5mm and of an HY trade only up to \$1mm, and anything larger prints as the capped string. The cap is the bond market's version of "a source familiar with the matter": you know something big happened, but not how big.

> **[SOURCE EXTRACTION]** *Ben_Dor_Quantitative_Credit_Portfolio_Management p.162 (note 3):* "disseminates trade-by-trade corporate bond execution information within 15 minutes to all market participants. At this time, TRACE data are censored at \$5 million for investment grade and \$1 million for high-yield securities."
>
> **Annotation.** The Barclays authors use the right word: *censored*. A censored observation is not missing data. It tells you the true value is at least the cap, which is information, so you should neither drop it nor treat it as equal to the cap. The caps have not moved since this was written. FINRA still disseminates `5MM+` for IG and `1MM+` for HY, and RN 25-17 applies the same caps to the new allocation reports. The *ticket* has moved: average trade size fell from about \$560k to about \$360k over the four years to 2024 (IFR, citing MarketAxess data), so a larger share of trades now prints uncapped. The capped minority is the part of the market an RSSG veteran knows best.

Every TRACE-based turnover model needs the following derivation. Let $X$ be the true size of a trade, with CDF $G$, and let the cap be $c$. TRACE shows $\tilde X = \min(X, c)$. For any nonnegative random variable, $\mathbb{E}[X] = \int_0^\infty \Pr(X > x)\,dx$, so

$$
\mathbb{E}[\tilde X] = \int_0^{c} \big(1 - G(x)\big)\,dx, \qquad \mathbb{E}[X] - \mathbb{E}[\tilde X] = \int_c^{\infty} \big(1 - G(x)\big)\,dx \;\ge\; 0 .
$$

Volume summed from capped prints therefore biases turnover *down*, by the area under the size distribution's tail beyond the cap. Ben Dor and coauthors flag exactly this:

> **[SOURCE EXTRACTION]** *Ben_Dor_Quantitative_Credit_Portfolio_Management p.364 (note 8):* "TRACE truncates the sizes of large transactions at \$1 million and \$5 million for high-yield and investment-grade bonds, respectively, which may cause our estimates of turnover to be downward biased."
>
> **Annotation.** The same note then gives the fix. Capped trades are assigned larger sizes, chosen so that the sum of individual trades matches TRACE's aggregate volume figures, which "yields higher transaction limits of \$4 million and \$12.5 million for high-yield and investment-grade bonds, respectively." That is a moment-matching estimator, and below we use it to extract a structural fact about block sizes. Where the modern desk departs: academic and enhanced TRACE files with uncapped sizes are released with a lag (Appendix B), so a backtest can use true sizes, but a live model sees only the capped feed. Train on what you will see at decision time. Otherwise your turnover feature is look-ahead bias in a lab coat.

Now make the imputation tell us something. Suppose block sizes above the cap follow a Pareto tail, the standard model for heavy-tailed sizes:

$$
\Pr(X > x \mid X > c) = \left(\frac{x}{c}\right)^{-\alpha}, \qquad x \ge c,\quad \alpha > 1 .
$$

Then the mean size of a capped trade is

$$
\mathbb{E}[X \mid X > c] = c + \int_c^\infty \left(\frac{x}{c}\right)^{-\alpha} dx = c + \frac{c}{\alpha - 1} = \frac{c\,\alpha}{\alpha - 1}.
$$

Ben Dor's imputed limit $m$ is this conditional mean. Set $m = c\alpha/(\alpha-1)$ and solve for the tail index:

$$
\hat\alpha = \frac{m}{m - c}.
$$

For IG, $c = 5$ and $m = 12.5$, so $\hat\alpha = 12.5/7.5 = 5/3 \approx 1.67$. For HY, $c = 1$ and $m = 4$, so $\hat\alpha = 4/3 \approx 1.33$.

Read that slowly, because it is the book's first quant "aha" for an RSSG reader. Both tail indices are below 2, so the implied block-size distribution has *infinite variance*. (Kaz, who was going to assume Gaussian, now regrets it.) The HY tail is also fatter. Relative to its cap, the average hidden HY block is four times the cap, against two and a half times in IG, so `1MM+` hides proportionally more of HY than `5MM+` hides of IG. The trades the tape conceals most completely are large HY and stressed trades, the ones where knowing who sold, and how much, is worth the most. The RSSG skill set is most valuable exactly where the data exhaust is thinnest.

(A caveat for the exercises: a Pareto tail fitted from one moment is a sketch, not an estimate. Chapter 22 fits the tail directly from the uncapped academic file.)

> **Ways This Blows Up.** *The riskless-principal echo.* Kaz once asked whether a "riskless principal" trade involved a principal with no risk, "like a tenured professor." Close. It is a dealer who buys from one customer and sells to another at nearly the same moment. The dealer carries no inventory risk, and one economic trade can generate two TRACE reports. Affiliated desks reporting to each other add more echoes. MarketAxess reported that duplicate trade reports inflated US high-grade TRACE volume by up to 8% in June 2026. FINRA's expanded affiliate-principal indicator exists to suppress them (voluntary from Aug 31, 2026, mandatory Aug 2, 2027; RN 26-16). A volume-based liquidity score fitted on 2020–2026 data therefore has a structural break built in. Tag the regime and deduplicate before you fit anything.

Last, a period piece from the shelf, included because it explains why some of Mags's habits survive:

> **[SOURCE EXTRACTION]** *Moyer_Distressed_Debt_Analysis p.416 (note 62):* "However, most of the securities required to be posted do not constitute distressed securities."
>
> **Annotation.** Moyer was writing in TRACE's phased-in early years, when dissemination mostly covered larger issues, and the same note expands the acronym as "Trade Reporting and Comparison Entry Source," an artifact of its vintage. For the distressed investor of that era, the new tape was something that happened to other people. Today every public TRACE-eligible corporate is disseminated, stressed ones included. But the caps and the slow manual component from §2.2.1 still make distressed trading the least transparent corner of a transparent market. That is why Mags still prices some things by grudge, and why she is still, irritatingly, right about some of them.

### Deep-Dive Resource Graph

**Podcasts.** *Bloomberg Odd Lots* has covered bond-market structure several times. We list no specific episodes because we could not verify titles and dates for this edition.

**Practitioner Writing.** FINRA, *TRACE Fact Book 2025*: https://www.finra.org/sites/default/files/2026-02/TRACE_FactBook_2025.pdf. FINRA, *TRACE Reporting Timeframes*: https://www.finra.org/filing-reporting/trade-reporting-and-compliance-engine-trace/trace-reporting-timeframes. Mayer Brown, *Free Writings* (Feb 10, 2025), on the one-minute effective date: https://www.freewritings.law/2025/02/finra-will-not-set-an-effective-date-for-amendments-to-trace-rules-establishing-one-minute-reporting-requirement-finra-to-prepare-new-filing-for-public-comment/

**Academic Papers.** Bessembinder, Maxwell & Venkataraman (2006), *Market transparency, liquidity externalities, and institutional trading costs in corporate bonds* (JFE). Edwards, Harris & Piwowar (2007), *Corporate bond market transaction costs and transparency* (JF). Goldstein, Hotchkiss & Sirri (2007), *Transparency and liquidity: a controlled experiment on corporate bonds* (RFS). Harris (2015), *Transaction costs, trade throughs, and riskless principal trading in corporate bond markets*.

**Data & Code.** SEC Release 34-101121 (one-minute approval): https://www.sec.gov/files/rules/sro/finra/2024/34-101121.pdf. FINRA Regulatory Notice 22-12 (portfolio-trade modifier): https://www.finra.org/rules-guidance/notices/22-12. FINRA Regulatory Notice 25-17: https://www.finra.org/rules-guidance/notices/25-17. FINRA Regulatory Notice 26-16 (affiliate indicator): https://www.finra.org/rules-guidance/notices/26-16.

