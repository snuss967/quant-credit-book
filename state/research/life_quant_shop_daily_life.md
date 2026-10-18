# Quant-Shop Life: Public, Citable Accounts of Daily Work at Market Makers, Pods, Systematic Managers, Dealer Desks and Distressed Funds

**Item:** What daily life inside credit quant shops, dealer desks and distressed funds is actually like (public accounts).
**Prepared:** 2026-10-18 (researcher, Edition 2 pipeline).
**Feeds:** Ch 1-B "A Week in Five Quant Shops" (primary); Ch 4-C; Ch 3, 18/18-B, 22, 26, 27, 28; Preface; Desk Debriefs; Laws of the Desk (App E).
**Integrity.** Every fact carries a source key [S#] (full URLs in section 11). Quotations are copied from the cited page. Machine transcripts are marked **CHECK** (re-listen before print). Vignette seeds are composites with the fictional cast; no real person speaks words that are not in a cited source.

---

## 0. Method

I read primary pages and transcripts this session (curl and the fetch tool): regulators' texts, a 310-page Senate report, six *Signals and Threads* transcripts, five *Odd Lots* transcripts, Optiver and Flow Traders documents, a Man Numeric transcript, SEC press releases and the shelf's Moyer pages. Page locators are the source's printed pages unless marked "PDF p." Search-result-only items are flagged "not opened". Sections ending "gap" record what I could not find.

## 1. Headline findings

1. **The best public document on a credit-derivatives desk's daily machinery is a Senate report.** The 2013 PSI report on JPMorgan's CIO book [S5] contains the daily P&L email, a "shadow P&L" spreadsheet comparing booked marks with mid-market marks, independent-price-testing tolerances (6 bp on the IG index), five risk limits all breached in Q1 2012, and a VaR model run from hand-keyed spreadsheets. Nothing else public is this granular for credit.
2. **Market makers talk openly about tooling and operations, not P&L.** Jane Street's podcast [S8] gives an intraday support rota, alert fatigue, a risk system that was one Excel workbook, and a point-in-time data archive. Optiver [S9] gives an hour-by-hour day ending in a reflection on "what we didn't do". Flow Traders' report [S11] shows a market maker cutting its fixed-income capital in 2025.
3. **Pods:** the daily rules are stop-losses, factor-neutral books and scope policing [S12, S13]; the only numeric thresholds are press reports about Millennium alone [S14].
4. **Systematic credit:** a Man Numeric transcript [S16] shows the working day as execution choices (voice or electronic, block or slice, venue, protocol); the SEC's Two Sigma order [S17] shows a model-governance backlog that sat four years.
5. **Distressed funds** live on a compliance calendar: signing "confi", being "restricted", big-boy letters [S19]; plus relationship sourcing [S20].
6. **Regulation sets the clock:** TRACE 15 minutes [S3]; best-execution review at least quarterly [S2]; SR 11-7 inventory and validation [S1]; market-access controls certified annually [S4]; off-channel recordkeeping [S21].
7. **Gaps (do not paper over):** no first-person day of a current bank IG/HY credit desk (JPMorgan, Goldman, BofA, Citi, Jefferies, Barclays); nothing first-person for AQR, Robeco, RenTech, Elliott, Silver Point, Monarch, D. E. Shaw or Citadel Securities credit; memoir page numbers unverified (section 8).

## 2. Documents that dictate the day

**2.1 SR 11-7 / OCC 2011-12 model risk guidance [S1]** (PDF pp. as numbered; the Fed's landing page returned 404, cite the PDF).
- Anything that turns inputs into "quantitative estimates" is a model: "an information input component ... a processing component ... and a reporting component" (p.3). Model risk is "adverse consequences from decisions based on incorrect or misused model outputs" (p.3). So the axe-ranker and the RFQ pricer are inventory items.
- "Effective challenge": "critical analysis by objective, informed parties" (p.4), stronger "when there is greater separation of that challenge from the model development process".
- Validation has three parts: "conceptual soundness ... ongoing monitoring, including process verification and benchmarking ... outcomes analysis, including back-testing" (p.11). Code needs "change control procedures ... all changes are logged and can be audited" (p.12).
- Overrides are data: when "model output is ignored, altered, or reversed", banks "should evaluate the reasons for overrides and track and analyze override performance" (p.13).
- Vendor models are in scope (pp.15-16); keep "a comprehensive set of information for models implemented ... under development ... or recently retired" (p.20).
- *Daily reading:* the bank trader's model change is a ticket, an independent review and an inventory update; the fund's is a pull request unless an allocator, regulator or the SEC (section 6.2) forces the same questions.

**2.2 FINRA Rule 5310, best execution [S2].** "[R]easonable diligence to ascertain the best market"; factors include "the character of the market", "size and type of transaction", "accessibility of the quotation" (a)(1). Where order-by-order review is not done, "regular and rigorous reviews ... security-by-security, type-of-order ... at a minimum ... quarterly" (.09). For debt, absent accessible quotes "members are not relieved from taking reasonable steps" (.03). *Daily reading:* the quarterly pack is built from the RFQ log, the same data as the desk's hit-ratio dashboard.

**2.3 FINRA Rule 6730, TRACE reporting [S3].** Report "as soon as practicable, but no later than within 15 minutes of the Time of Execution"; trades before 8:00 a.m. ET or within 15 minutes of close roll to after the next open; required fields include contra-party ID and capacity; later reports are "as/of"; "a pattern or practice of late reporting" can violate Rule 2010 (f). *Daily reading:* an operations seat clears the exception queue; the quant's later back-test inherits cancels, corrections and as/of prints (see `papers_factor_replication_crisis_and_bond_data.md`).

**2.4 SEC Rule 15c3-5, market access [S4].** Controls must "[p]revent the entry of orders that exceed appropriate pre-set credit or capital thresholds" and reject orders breaching "price or size parameters", under "direct and exclusive control" of the broker; reviewed "no less frequently than annually"; the CEO must "on an annual basis, certify". *Daily reading:* the kill switch in Ch 27 is a legal control for exchange-facing hedges (ETFs, futures), not for the bond RFQ.

## 3. Bank credit-trading desks and dealers

**3.1 JPMorgan CIO synthetic credit book, 2012 [S5]** (Senate PSI staff report, 15 Mar 2013; printed page = PDF page minus 8; the Task Force report is quoted only through the Senate report [S6]).
- **Daily P&L email and marker.** The book filed "daily profit/loss (P&L) reports ... internally" (p.5), marked each day by "a junior trader charged with marking the SCP's positions". One day's email estimated a $43 million loss, "the largest daily loss yet", and a "$600 million to $800 million 'lag'" (p.83).
- **Marking convention.** Early January: "at or near the midpoint price in the daily range of prices (bid-ask spread)". Later it "began to assign more favorable prices within the daily price range" (p.5). Recorded call: "I am not marking at mids as per a previous conversation" (p.5).
- **Shadow P&L.** For 12-16 March 2012 the marker kept "a spreadsheet tracking the differences" between reported and mid values: reported YTD loss $161 million versus $593 million at mids (p.5). On 30 March a $319 million daily loss was reported and the Valuation Control Group (VCG) later found a $512 million gap (p.5). On 10 April an estimated $6 million daily loss was re-issued "90 minutes later, after a confrontation between two CIO traders" (p.5).
- **Independent price testing.** VCG tolerances let the IG credit index "vary from the midpoint ... by up to 6 basis points" (fn 675, p.112). An analyst described March practice: "marked the book at the boundary of the bid/offer spread ... then applied a tolerance" (p.141). Internal audit rated VCG "Needs Improvement": no "formally applied price sourcing hierarchy", no "documented/consistently applied price testing thresholds" (p.141).
- **Two marks for one position; collateral calls.** The CIO and the Investment Bank "assigned different values to identical credit derivative holdings"; counterparties objected and "collateral disputes" peaked at $690 million (p.6). In May the deputy CRO told the CIO to mark as the Investment Bank did, "which used an independent pricing service to identify the midpoints" (p.6); that "resolved the collateral valuation disputes in favor of the CIO's counterparties". The Controller's special assessment found the book's value "could legitimately fall anywhere between $719 million and $1.2 billion" (p.98); the bank restated Q1 2012 for an additional $660 million of losses on 13 July 2012 (p.98).
- **Limits.** Five metrics (VaR, CS01, CSW10%, stress loss, stop-loss advisories) were all breached in Q1 2012 (p.7).
- **The VaR spreadsheet.** The model owner "had to manually enter data into multiple spreadsheets each trading day, which often took hours" (p.185). The Task Force: review group noted a "manual process ... 'error prone' and 'not easily scalable'"; the promised automation "was never automated" (p.186); an error "likely had the effect of muting volatility by a factor of two" (p.186). Net notional rose from "over $51 billion" (end-2011) to "over $157 billion" (end-March 2012) (p.185). VaR for five days in April was "understated by appr[o]x[imately] $10m" (p.185). Examiners: "shocking" (p.186).
- *Use:* SR 11-7's three validation parts failing in sequence. Real names appear in the report; the book should use unnamed composites and cite the report for structure.

**3.2 The voice-desk baseline [S7].** *Odd Lots* (31 Jul 2017), Bloomberg's Rob Elson, machine transcript (**CHECK**). Treasury, not credit. Early 1970s at what was then First National City Bank: a salesman shouted "bid 56 is for American Road" (code for Ford) and sold "50 million six-month treasury bills"; a trainee listened to a broker's run of two-year notes, heard "I'll buy the octobers, sell the Novembers" and was told "write the tickets" ("that was my test"). Morning meetings could force a risk call (a 1974 coupon auction, yields then fell ~100 bp). By 2017: "serious risk limits and serious position limits ... capital requirements that were not in play over the years"; "for the vast majority of clients, it's all electronic."

**3.2b The shape of the dealer day has changed [S24].** The DESK (17 Sep 2025) on Barclays FICC research's note "Goodbye, Seasonality" (Zornitsa Todorova): trading 12-1 p.m. is "up from 11.3% to 12.5% in US IG" since 2022; "August and December, once the quietest months, now each account for nearly 8% of annual volumes, up from 6-7% pre-2022"; "As human traders step back, algos and portfolio trades step in"; electronic share exceeds 50% of US and EU IG, rising 5-10 points in holidays and lunch hours; Friday volume has caught up with mid-week; "some seasonality will stick given the primary issuance calendar."

**3.2c Operations on a bank loan desk (court record, cross-reference).** The 11 Aug 2020 Citi/Revlon wire is documented in the S.D.N.Y. and Second Circuit opinions: three reviewers in a "six-eye" control, a loan-servicing screen (Flexcube) with FRONT, FUND and PRINCIPAL fields, and a default that sent about $894 million of principal out by wire. See `case_lmt_autopsies_us_2020_2026.md` for the cited detail; it is the best public account of a loan-servicing maker-checker day and belongs in Ch 27.

**3.3 Gap: today's bank IG/HY dealer desk.** I found no first-person account, only generic summaries of a 7-8 a.m. global morning meeting with overnight European runs and rating actions (search result; not opened). Build the bank-desk week from sections 2-3.2c, section 6.1 (how a buy-side client now trades with dealers), 6.1b (a buy-side trader's written duties) and labelled composites. Do not attribute a routine to any named bank.

## 4. Market makers

**4.1 Jane Street, *Signals and Threads* [S8]** (transcripts read; none is credit-specific, so the book may use them only as analogy).
- *Ep 20, Liora Friedberg, Production Engineer (7 Oct 2024):* "between a quarter and a third of your time you'll actually be on rotation"; support is "not really the same thing as kind of being on call overnight or on the weekends. This is really like, during the trading day you are present and responding to issues that are popping up live"; engineers built a tool asking "What percentage of alerts are we actually actioning? ... snoozing or close themselves?" (18:40); "pages will open and close and you did nothing to resolve them ... taking up mental space" (19:44); training by "incident simulation ... like D&D" (c. 42:29).
- *Ep 29, Eric Mannes (2 Sep 2026):* the commodities risk system was "a large Microsoft Excel spreadsheet, uscommoditiesrisk.xlsm ... you'd press a button ... sometimes it was slow", rebuilt "from first principles"; "every desk across the firm has embedded desk devs". On 20 Apr 2020 crude settled negative: assumptions "baked into your trading and risk systems, like this price will always be positive" broke order entry. Vendors "tell you, whoops, made a mistake"; Jane Street saves "all the data ... along with the time we received it" to avoid "a time machine".
- *Ep 23, Ian Henry (28 May 2025):* "We measure things in microseconds ... a millisecond [means] something has gone horribly wrong"; traders want tools "about six pixels high" and keyboard-only; "fewer per-user knobs and more desk wide."
- *Ep 22 (In Young Cho), Ep 15 (Gord, the trading-data normaliser), Ep 19 (UX):* summaries only.
- *Firm pages [S8b]:* Jane Street "trade[s] continuously on more than 200 electronic exchanges and other venues" and names Bonds among its markets; "feedback on successes and failures is quick and tangible". Its Finance and Operations department is "a constellation of many teams - including accounting, reconciliation, settlements, regulatory, margin, risk, tax, and treasury"; Legal and Compliance advises on "real-time questions about how and where we trade". These are the unglamorous functions around every market-maker seat.

**4.2 Optiver [S9]** (recruiting copy; equity options). Chicago intern: 6:30 wake; 7:30 desk boot; "about 15 minutes going over the news"; morning standup; 10:00 weekly options plus modeling; 1:00 projects (autotraders, earnings-move analysis); 4:00 standup and "close to an hour digging into our trades: what we did, why we did it ... what we didn't do", ending with "a few small but actionable goals". Sydney trader: morning meeting on "how we expect the market to behave at open"; quiet periods go to "visualisation, tools and research"; a written "reflection on the day's trading". A Hong Kong account (third-party copy; not opened) mentions "scripts to check limits and pricing".

**4.3 Virtu and Flow Traders.** Virtu FY2015 10-K [S10]: "real-time risk management system is built into our trading platform"; a control "automatically freezes the applicable trading strategy, cancels all applicable open orders"; 148 employees; no credit. (The widely repeated "one losing day in 1,238" was not in the text read; do not use.) Flow Traders AR 2025 [S11] (printed pages): "over 630 professionals" (p.2); "strategically reduced the capital deployed to fixed income in 2025", fixed-income value traded EUR 795 billion versus 943 billion (p.18); breaches "trigger action from the Risk department", positions "monitored daily by Operations" and VaR at "95% level of confidence" over 1-10 days (p.140); material changes to "limits" need quarterly committee approval (p.31); "Multi-layer monitoring ... teams are immediately notified via multiple different channels" (p.34). Citadel Securities: only self-reported share figures (see `trend_electronification_pt_etf_liquidity.md`); no day-in-life source.

## 5. Multi-strategy pods

**5.1 Giuseppe Paleologo on *Odd Lots* (20 May 2024)** [S12], ex-Citadel and Millennium risk; machine transcript (**CHECK**). Platforms sit between single managers and funds of funds: they "observe the performance of PMs ... from a very close distance", give more capital to winners and "take capital away from them or let them go"; PMs "are paid a percentage of their P&L". Books are "purely market neutral and factor neutral"; a bought factor model is a real-time "x-ray of your body". Risk has three jobs: stop-losses ("a PM is a little bit like somebody who's holding a call option ... a stop loss is effectively a sort of a primitive tail insurance"), true diversification (factor exposure summed "across 300 PMs") and keeping people "in scope". Visibility between pods has shrunk: "you are not seeing what I am having, what I'm holding." One former PM's "biggest drawdown was $90 million".
**5.2 Rich Falk-Wallace (ex-Citadel) on *Odd Lots* (25 Jul 2024)** [S13]: leverage is on the residual, not beta ("what you're levering is just that residual term").
**5.3 Reported pod limits** [S14]: Millennium PMs "who lose 5% of the capital allocated to them typically have their capital halved. If they lose another 2.5%, they're usually fired" (eFinancialCareers, 5 Dec 2025, citing the WSJ; Millennium declined comment); Hedgeweek (10 Mar 2025): "buying power cut in half if losses hit 5%", "a 7.5% drawdown can result in portfolio managers being dismissed, though exceptions can be made", in a piece on a 1.3% February loss "mostly from index-rebalancing trades". Not firm disclosures; do not generalise to other pods.
**5.4 BAM, Davidson Kempner, Centerbridge [S15]** (show notes only, transcripts premium): Balyasny "$21 billion ... 2,000 employees across 15 global offices" (Oct 2023); Davidson Kempner "$40 billion multi-strategy ... opportunistic credit and event-driven" with "Idea generation" and "Risk management" chapters; Centerbridge "$43 billion", "sector teams ... culture and compensation systems to reinforce collaboration". OpenAI's Balyasny case study (6 Mar 2026) is known only through a secondary blog (Applied AI group of ~20 serving ~180 teams; "days to hours" is vendor-reported; not opened).

## 6. Systematic asset managers

**6.1 Man Numeric credit [S16]** (Lam and Kamenski, recorded Mar 2024; speech-recognition transcript). Chain: data to "key drivers of ... credit spreads", robust techniques, then "the hard part ... going from the expected returns that we can research in a theoretical state" to "risk modeling and portfolio construction and liquidity and transaction cost analysis." Execution is a daily choice: "venue selection ... high touch or low touch ... circumstances where the best course of action is to trade voice." 2021 "was the year of portfolio trading"; in 2022 changes in ETF create/redeem made it "harder for those desks to recycle risk" and "transaction costs generally went up substantially". A 10-50 million block through one dealer "might not be the optimal way"; the alternative is "slice it" and route to "the best venue and the best protocol." Earnings season: "a supplier company reporting before a customer company ... multiply that by hundreds of issuers." Share: "very low single digits."
**6.1b What a buy-side credit trader is hired to do [S22b].** A DWS Group posting (New York, posted 7 May 2026, listed on a credit-careers board under Deutsche Bank): "Execute portfolio manager generated Investment Grade Credit and High Yield orders (across multiple venues) in compliance with trading procedures and portfolio guidelines"; "help build automated solutions for the desk's processes and order flow"; take part in "liquidity dialogue" on "relative value, trade ideas, difficult to trade situations ... New Issue color"; "foster successful relationships and interactions with Operations, Technology, Compliance, Risk and Audit"; tools named: "Bloomberg, MarketAxess and Tradeweb", "BRS Aladdin a plus", "Python, JavaScript, SQL"; the team's goal is "best execution results for the firm's clients". A job description, not a diary, but the only dated, firm-specific duty list for a credit trader I could read.

**6.2 Two Sigma [S17]** (SEC Press Release 2025-15, 16 Jan 2025). Employees found model vulnerabilities "in or before March 2019"; the firm "waited until August 2023"; it "failed to supervise one of its employees who made unauthorized changes to more than a dozen models"; $90 million penalty, $165 million repaid. *Reading:* a four-year backlog item is the mirror of SR 11-7's "all changes are logged".
**6.3 BlackRock, Two Sigma research culture [S18]** (show notes only): Rosenberg (S7E19, 18 Aug 2025): "implementation and transaction costs [are] critical challenges compared to equities"; chapters on "Managing and neutralizing factor exposures" and ETF effects; Wellington (S7E32, 6 Jul 2026): "feature collinearity", "life cycle of features", "p-hacking". **Gap:** AQR, Robeco, RenTech first-person routines not reached.

## 7. Distressed funds and the restructuring adviser

**7.1 The restricted-list calendar, Moyer [S19]** (printed pp.62-64). Joining a bondholder committee requires "signing 'confi'", which "can result in the holder becoming 'restricted'"; to "maximize the time period members remain unrestricted" information first goes to "the financial advisors and counsel"; members "cannot become unrestricted until the information becomes public ... Form 8-K, 10-Q, or 10-K, or ... nonmaterial"; "ethical walls" isolate the one recipient; trades need a "big-boy letter" (acknowledgment plus waiver) "arranged by a broker-dealer intermediary"; a restricted seller is like the man who "has just watched the third race" (pp.63-64); a bank-loan holder becomes restricted if the agent's employee "indiscreetly mentions" a pending asset sale (p.64).
**7.2 Sourcing [S20]** (*Odd Lots*, 28 Nov 2024, Milwood Hobbs, Oaktree; machine transcript, **CHECK**): "the relationship is getting the first call ... out of 20 deals, I only care about the last two. So how do I pass 18 times?"; a sponsor's dividend request "take[s] me from violently upset to mildly annoyed."
**7.3 The PJT seat [S21].** SEC Press Release 2025-6 (13 Jan 2025): twelve firms paid $63.1 million for off-channel recordkeeping failures; PJT Partners "self-reported" and paid $600,000. **Gap:** Elliott, Silver Point, Monarch, Davidson Kempner first-person routines (see `perspectives_buyside_credit_managers.md`).

## 8. Memoirs and books (locators unverified unless stated)

Bibliographic records verified on archive.org this session [S22]; page-level text mostly behind lending, so scene locators below are **CHECK in print**. Snippet leaves are scan leaves of the cited copies, not printed pages.

| Book | Verified | Use |
| :--- | :--- | :--- |
| Lewis, *Liar's Poker* (Norton 1989) | Record and snippets: "that most revered of all species: a Big Swinging Dick" and "After the sale of a big block of bonds and ..." (copy `liarspoker0000mcha`, leaf 262) | Status on a bond floor (Ch 1-B bank seed); training-class scenes **CHECK** |
| Derman, *My Life as a Quant* (Wiley 2004) | Record; contents headings "Goldman as home", "Heading the Quantitative Strategies Group", "The Black-Derman-Toy model"; text: candidates "often interviewed who tried to use the Quantitative Strategies Group I ran as a conduit into trading" (copy `mylifeasquantref0000derm`, leaf 310) | Quant/trader relations at Goldman; the quant seat as a route to the desk |
| Zuckerman, *The Man Who Solved the Market* (Portfolio 2019) | Not verified; reader notes say data scrubbing and "tracking down missing price sheets" | Data-cleaning culture; use only after print check |
| Mallaby, *More Money Than God* (Penguin 2010) | Record only | D. E. Shaw, Citadel, Elliott scenes **CHECK** |
| Patterson, *The Quants* (Crown 2010) | Record; "Just thirty-three, Weinstein was head of all credit trading in the United ..."; a "private poker game"; "continued to rack up gains despite the August quant quake. It was on track to pull in $892 million" (leaf 362; the snippet does not show whose gains, **CHECK**) | Credit-desk poker culture; Aug 2007 |
| Tett, *Fool's Gold* (Free Press 2009) | Record; snippet "Blythe Masters cast about for a way to make credit ..." (copy `foolsgoldhowunre00tett`, leaf 358) | JPMorgan's credit-derivatives group origins; scene detail **CHECK** |

## 9. Mundane tasks by day-part (all shop types)

| When | Task | Shop and source |
| :--- | :--- | :--- |
| Pre-open | News, overnight runs, expected-open meeting; scripts check limits and prices | MM [S9]; bank (unverified) |
| Open to close | Support rota, alert triage; high- vs low-touch choice; stop-loss watch | MM [S8]; asset manager [S16]; pod [S12] |
| Intraday (15 min) | TRACE report and exception queue | all dealers [S3] |
| Close | Daily P&L email and marks; mid-vs-mark check | bank [S5] |
| Post-close | Reflection incl. trades not done; factor x-ray | MM [S9]; pod [S12] |
| Weekly/monthly | Alert-history review; VCG price tests; risk committee | MM [S8]; bank [S5] |
| Quarterly | Best-execution review; limits approval | broker-dealer [S2]; MM [S11] |
| Annual | Market-access CEO certification; RCSA; model inventory | [S4], [S11], [S1] |
| Event-driven | Sign "confi", big-boy letters, restricted list | distressed [S19] |
| Continuous | Point-in-time archive, change log, off-channel records | [S8], [S1], [S21] |

### 9b. Week skeletons for Ch 1-B (sourced recurring items only; everything else is composite)

- **Market maker (Jane Street/Optiver pattern):** daily news round, standup, expected-open discussion, scripts that check limits and prices, intraday support rota, end-of-day reflection; weekly alert-history review; quarterly limits committee [S8, S9, S11].
- **Bank credit-derivatives book (JPMorgan CIO pattern):** daily marks and P&L email; daily VaR load; month-end VCG price tests against tolerance; collateral calls and disputes with counterparties; limit-breach escalation; quarterly internal-audit summary [S5].
- **Pod (Paleologo pattern):** daily factor x-ray and P&L against stop; risk call when scope drifts; capital raised or cut on performance [S12].
- **Systematic manager (Man Numeric pattern):** signal refresh in earnings weeks; per-order venue and touch decision; transaction-cost review; model-change governance [S16, S17].
- **Distressed fund:** restricted-list updates when "confi" is signed or an 8-K lands; sourcing calls; big-boy letters on trades [S19, S20].

### 9c. Do not repeat (unverified or over-generalised)

"One losing day in 1,238" for Virtu (secondary only); Millennium's 5%/7.5% as a rule for pods in general; "days to hours" at Balyasny (vendor claim); any named-bank credit-desk routine; machine-transcript quotations without re-listening; real names from the Senate report in a vignette.

## 10. Vignette seeds (21)

Format: shop type; scene; mundane task; concept; sources. Cast (Theo, Ines, Kaz, Mags, ROBO) may appear; real people and firms appear only as the cited source says.

1. **The shadow sheet.** *Bank credit-derivatives book.* A junior marker closes the day at 4:40 p.m. and keeps a second column, booked mark against mid. *Task:* daily marks and the P&L email; month-end price-testing against tolerance. *Concept:* a mark is a choice inside the bid-ask; why independent price verification exists; the P&L explain; two desks holding two marks for one position and the collateral call that settles it. [S5 §3.1, S1]
2. **Four hours of typing.** *Bank risk/quant seat.* The model's owner hand-keys market data into spreadsheets before the VaR runs; the review note called it "error prone"; the automation ticket never closed. *Task:* data load and reconciliation. *Concept:* process verification versus conceptual soundness; why Kaz's elegant model needs an ingestion test. [S5, S1]
3. **Write the tickets.** *Dealer voice-desk legacy.* A trainee misses a spread trade shouted down the phone; the same desk's RFQ screen today logs response time and cover for every request. *Task:* ticket booking. *Concept:* what electronic RFQ logs captured that voice never did, the raw material of Ch 18-B; where voice still wins (10-50 mm blocks). [S7, S16]
4. **The 15-minute clock.** *Dealer operations and compliance.* An analyst clears TRACE exceptions (wrong capacity flag, a late as/of) and later assembles the quarterly best-execution pack from the RFQ log. *Task:* exception queue; review pack. *Concept:* TRACE as the data exhaust a back-test inherits; "regular and rigorous" review as markout analysis. [S3, S2]
5. **The alert that flickers.** *Market maker production rota.* Pages open and close on their own; a rota member builds an alert-history report and moves a threshold. *Task:* triage and alert hygiene. *Concept:* alarm fatigue, false-alarm cost, how a kill-switch threshold is calibrated. [S8 Ep 20, S4]
6. **The price that cannot be negative.** *Market maker desk dev.* An order-entry field rejects a quote; credit version: a defaulted loan quoted at 0.5, a recovery-priced bond, a spread that crosses zero. *Task:* validation ranges. *Concept:* hidden positivity assumptions; fat-finger bands versus real distress prices. [S8 Ep 29, S4]
7. **What we knew when.** *Market maker data team.* A vendor corrects history; the archive keeps what arrived and when. *Task:* point-in-time snapshots; credit analogue: TRACE cancels, rating changes, restated financials. *Concept:* look-ahead bias, "a time machine" in the back-test. [S8 Ep 29, S3]
8. **News, standup, expected open.** *Credit market maker, Optiver-style rhythm.* 7:45: European runs are in, a 15-minute news round, scripts check limits and prices; 8:00: TRACE opens; at close, a reflection on trades not done. *Task:* pre-open checks. *Concept:* markouts on RFQs you lost; the passed trade as data. [S9, S3]
9. **The desk that shrank.** *Market maker risk committee.* Capital shifts away from fixed income to better-returning products. *Task:* quarterly limits and capital review. *Concept:* return on trading capital; opportunity cost of credit inventory; why dealer balance sheet is a choice. [S11]
10. **The 5% line.** *Pod PM.* A PM, two-thirds of the way to a reported capital-halving threshold, sizes down before the call from risk. *Task:* daily P&L against stop. *Concept:* stop-loss as left-tail insurance; the PM as option holder; incentives. Thresholds are press-reported for one firm only. [S12, S14]
11. **The x-ray.** *Pod credit PM.* The factor screen shows spread beta leaking from a long-short; summed across hundreds of PMs it is a firm exposure. *Task:* read the exposure screen; hedge with CDX. *Concept:* "IDO or it didn't happen"; hidden compounding; neutralization. [S12, S13]
12. **In scope.** *Pod risk manager.* A PM drifts from single-name HY into index hedges and CCC; the risk manager calls. *Task:* scope review. *Concept:* strategy drift; "trust, but verify". [S12]
13. **High touch or low touch.** *Systematic asset manager.* A 20 mm sale: one dealer block, or slice across venues and protocols, or add it to a portfolio trade. *Task:* pre-trade routing decision and cost estimate. *Concept:* transaction-cost analysis, venue selection, when voice wins. [S16]
14. **The supplier reports first.** *Systematic asset manager, earnings week.* One issuer's results move the signal for its customers across hundreds of names. *Task:* intraday signal refresh and risk check. *Concept:* read-through, data latency, the earnings-cycle workload. [S16]
15. **The ticket from March 2019.** *Systematic asset manager governance.* A known model weakness sits in the queue; a researcher edits a live parameter. *Task:* change log, access control, ticket aging. *Concept:* SR 11-7's logged changes; backlog as operational risk. [S17, S1]
16. **Signing confi.** *Distressed fund.* An analyst joins an ad hoc group, goes restricted until the next 8-K, and must trade an unrelated bond through a big-boy letter. *Task:* restricted-list calendar. *Concept:* restricted status, information walls, why the systematic desk sees this name stop trading. [S19]
17. **Passing eighteen times.** *Opportunistic credit fund sourcing.* A sponsor calls the top lenders about a dividend; most calls end in a pass. *Task:* the pass log. *Concept:* relationship flow as information; the pass log as a dataset. [S20]
18. **Approved channels.** *Banker-turned-trader, first week.* Compliance training on messaging; the former employer had self-reported a recordkeeping lapse. *Task:* recordkeeping. *Concept:* what leaving a bank's channels costs; Ch 3's cultural bridge. [S21]
19. **Hand history.** *Credit desk culture.* The desk has a private poker game; the mentor reads the day's markouts as a hand history. *Task:* markout review. *Concept:* adverse selection as a card-counting problem. Real-person anecdotes limited to the verified snippets. [S22 Patterson, S22 Lewis]
20. **Days to hours.** *Pod applied-AI group.* An agent reads filings for a credit team; evaluation uses an internal benchmark set before release. *Task:* agent evaluation. *Concept:* hallucination controls, model inventory for LLM tools; treat "days to hours" as vendor-reported. [S15, S1]
21. **The lunch hour nobody covers.** *Dealer desk, September.* Half the humans are at lunch or away; algos and portfolio trades carry a bigger share of the midday volume than they did in 2021. *Task:* coverage rota and auto-execution limits. *Concept:* declining seasonality, intraday liquidity, why a quote engine needs a lunch-hour risk setting. [S24]

## 11. Sources (verified this session, 2026-10-18 unless marked)

"Read" = full text obtained by curl or fetch tool. "Surfaced" = search result only; not opened, not to be cited without a fetch.

- **S1** Fed/OCC, *Supervisory Guidance on Model Risk Management*, SR 11-7 attachment, 4 Apr 2011. Read: https://www.federalreserve.gov/boarddocs/srletters/2011/sr1107a1.pdf (landing page https://www.federalreserve.gov/supervisionreg/srletters/sr1107.htm returned 404).
- **S2** FINRA Rule 5310. Read: https://www.finra.org/rules-guidance/rulebooks/finra-rules/5310
- **S3** FINRA Rule 6730. Read: https://www.finra.org/rules-guidance/rulebooks/finra-rules/6730
- **S4** 17 CFR 240.15c3-5. Read: https://www.law.cornell.edu/cfr/text/17/240.15c3-5
- **S5** Senate PSI, *JPMorgan Chase Whale Trades*, 15 Mar 2013. Read: https://www.hsgac.senate.gov/wp-content/uploads/imo/media/doc/REPORT%20-%20JPMorgan%20Chase%20Whale%20Trades%20(3-15-13).pdf
- **S6** JPMorgan Management Task Force Report, 16 Jan 2013. Quoted only via S5. Surfaced: https://www.sec.gov/Archives/edgar/data/0000019617/000001961713000077/a8-k.htm
- **S7** *Odd Lots*, 31 Jul 2017 (Elson). Read: https://omny.fm/shows/odd-lots/how-the-bond-market-changed-during-a-veteran-trade and https://podscripts.co/podcasts/odd-lots/how-the-bond-market-changed-during-a-veteran-traders-decades-on-wall-street
- **S8** *Signals and Threads* (index https://signalsandthreads.com/). Read: https://signalsandthreads.com/solving-puzzles-in-production/ ; https://signalsandthreads.com/wrestling-the-world-into-rows/ ; https://signalsandthreads.com/building-tools-for-traders/ ; https://signalsandthreads.com/finding-signal-in-the-noise/ ; https://signalsandthreads.com/swapping-the-engine-out-of-a-moving-race-car/ ; https://signalsandthreads.com/from-the-lab-to-the-trading-floor/
- **S8b** Jane Street firm pages. Read: https://www.janestreet.com/join-jane-street/departments/ ; https://www.janestreet.com/what-we-do/overview/ ; https://www.janestreet.com/culture/overview/
- **S9** Optiver. Read: https://www.optiver.com/join-us/stories/day-in-the-life-quant-trader-intern/ ; https://www.optiver.com/join-us/stories/new-the-internship-journey-to-becoming-a-trader/
- **S10** Virtu FY2015 10-K (first 100,000 characters read via fetch tool): https://www.sec.gov/Archives/edgar/data/0001592386/000155837016004397/virt-20151231x10k.htm
- **S11** Flow Traders Annual Report 2025. Read: https://flowtraders.com/media/itid3d0e/flow-traders-annual-report-2025.pdf
- **S12** *Odd Lots*, 20 May 2024 (Paleologo). Read: https://podscripts.co/podcasts/odd-lots/how-to-succeed-at-multi-strategy-hedge-funds
- **S13** *Odd Lots*, 25 Jul 2024 (Falk-Wallace). Read: https://podscripts.co/podcasts/odd-lots/how-the-hottest-hedge-funds-on-wall-street-really-manage-risk (also retrieved, not mined: https://podscripts.co/podcasts/odd-lots/how-the-rise-of-pod-shops-is-reshaping-the-way-markets-trade)
- **S14** Read: https://www.efinancialcareers.com/news/pratik-madhvani-glen-scheinberg ; https://www.hedgeweek.com/millennium-posts-rare-monthly-loss-amid-index-rebalancing-trades/
- **S15** Capital Allocators show notes (read): https://www.capitalallocators.com/podcast/multi-strategy-platform-at-bam/ ; https://www.capitalallocators.com/podcast/forty-years-of-davidson-kempner/ ; https://www.capitalallocators.com/podcast/building-centerbridge-across-the-capital-structure/. Surfaced: https://www.gend.co/blog/balyasny-ai-research-engine-gpt-5-4 (OpenAI's page returned 403).
- **S16** Man Group, "Extra Credit: Algorithmic Advantage". Read: https://www.man.com/maninstitute/extra-credit-algorithmic-advantage
- **S17** SEC Press Release 2025-15. Read: https://www.sec.gov/newsroom/press-releases/2025-15 ; corroboration https://securitiesdocket.beehiiv.com/p/sec-charges-two-sigma-for-failing-to-address-known-vulnerabilities-in-investment-models
- **S18** *Flirting with Models* show notes (read): https://www.flirtingwithmodels.com/episodes/8V74zBaN4jN ; https://www.flirtingwithmodels.com/episodes/mDCRKBfrVHQ
- **S19** Moyer, *Distressed Debt Analysis* (shelf): `state/pdf_pages/Moyer_Distressed_Debt_Analysis/page_0079.txt` to `page_0081.txt`.
- **S20** *Odd Lots*, 28 Nov 2024 (Hobbs). Read: https://podscripts.co/podcasts/odd-lots/how-oaktrees-head-of-sourcing-finds-the-next-great-deal
- **S21** SEC Press Release 2025-6. Read: https://www.sec.gov/newsroom/press-releases/2025-6
- **S22** Books: archive.org records for `mylifeasquantref0000derm`, `moremoneythangod0000mall`, `quantshowsmallba0000patt`, `foolsgoldhowbold0000tett`, `liarspoker0000lewi`; snippets via the Open Library search-inside API (https://openlibrary.org/search/inside.json?q=...; scan leaves, not printed pages).
- **S22b** DWS Group credit-trader posting, 7 May 2026. Read: https://careerportal.creditflowresearch.com/job-post/deutsche-bank-credit-trader-7yqm9f
- **S23** Internal: `media_podcasts_credit_quant.md`, `perspectives_buyside_credit_managers.md`, `trend_electronification_pt_etf_liquidity.md`, `papers_factor_replication_crisis_and_bond_data.md`.
- **S24** The DESK, 17 Sep 2025, Barclays "Goodbye, Seasonality". Read: https://www.fi-desk.com/insights-analysis-technology-upends-traditional-credit-trading-liquidity-patterns-barclays-says/

## 12. Book placement

| Chapter | Use | Items |
| :--- | :--- | :--- |
| **Ch 1-B** A Week in Five Quant Shops | Backbone: market maker = §4.1-4.2 (rota, alerts, spreadsheet, standup); pod = §5.1-5.3; systematic = §6.1-6.2; bank = §3.1-3.2 plus composites; distressed = §7.1-7.2 | V1-V21 |
| **Ch 4-C** Other Seats | Pod, dealer, systematic and distressed perspectives; real firms only as cited | §5, §6.3, §7, §3.2 |
| **Ch 2** Revolutions | Shape-of-day data (lunch hour, August/December), voice-to-electronic oral history | §3.2, §3.2b, V3, V21 |
| **Ch 3** PJT-to-desk bridge | Records and channels; restricted-list view from the other side | V16, V18, §7.3 |
| **Ch 7 / 7-B / 9-B** data | Point-in-time archive; TRACE corrections | V7, §2.3 |
| **Ch 18 / 18-B** RFQ | Logs as raw material; quarterly pack; markouts | V3, V4, V8, V19 |
| **Ch 22** regulation | TRACE 15-minute clock; 5310; 15c3-5; off-channel rules | §2.2-2.4, §7.3 |
| **Ch 26** AI agents | Evaluation and model inventory for LLM tools | V20, §6.3 |
| **Ch 27** systems | Kill switch, alert hygiene, spreadsheet-to-system migrations, validation ranges | V2, V5, V6, §4.1, §4.3 |
| **Ch 28** PM playbook | Stop-loss, scope, factor x-ray, governance backlog | V10-V12, V15, §5 |
| **Preface / Desk Debriefs** | Opening line: the most senior question on a desk is a spreadsheet | §3.1, §4.1 |
| **App B / App C** | Add S1-S5, S11, S16-S17 to the source atlas and trend rows (Flow Traders FI cut; Two Sigma order) | §4.3, §6.2 |
| **App E** Laws | Candidate laws: "a mark is a choice"; "the model owner must not run the model"; "save what you knew when you knew it" | §3.1, §4.1 |

**Open research list:** a first-person current IG/HY bank desk day; AQR, Robeco, RenTech routines; Citadel Securities credit; Elliott, Silver Point, Monarch, Davidson Kempner day-in-life; print page numbers for memoirs; the Task Force PDF (read directly, not via S5).

<!-- STATUS: COMPLETE -->
