# Quant-Shop Life: Public, Citable Accounts of Daily Work Inside Market Makers, Pods, Systematic Managers, Dealer Desks and Distressed Funds

**Item:** What daily life inside credit quant shops, dealer desks and distressed funds is actually like (public accounts)
**Prepared:** 2026-10-18 (researcher, Edition 2 pipeline)
**Feeds:** Ch 1-B "A Week in Five Quant Shops" (primary), Ch 4-C "Other Seats at the Table", Ch 3, Ch 18/18-B, Ch 22, Ch 26, Ch 27, Ch 28, Preface, Desk Debriefs.
**Integrity note:** Every fact below carries a source. Where I could not verify a detail this session it is marked **CHECK** or left out. No quotation is put in a real person's mouth unless it is copied from the cited page. Vignette seeds are composites; real firms appear only for publicly stated practices.

---

## 0. Method and how to read this dossier
(to be filled)

## 1. Headline findings
(to be filled)

## 2. Regulatory and process documents that dictate the day (SR 11-7, TRACE, best execution)
### 2.1 SR 11-7 / OCC 2011-12: the document that makes a bank desk's model changes slow (and an asset manager's fast)

**Source.** Board of Governors / OCC, *Supervisory Guidance on Model Risk Management*, attachment to SR Letter 11-7, 4 April 2011. PDF fetched this session: https://www.federalreserve.gov/boarddocs/srletters/2011/sr1107a1.pdf (22 PDF pages; "PDF p." below is the page of the PDF). The old letter landing page https://www.federalreserve.gov/supervisionreg/srletters/sr1107.htm returned HTTP 404 on 2026-10-18, so cite the PDF.

What a desk member lives with, with the sentence that creates it:

- **Anything quantitative that produces an estimate is a "model".** "[T]he term model refers to a quantitative method, system, or approach that applies statistical, economic, financial, or mathematical theories, techniques, and assumptions to process input data into quantitative estimates" (PDF p.3). It "consists of three components: an information input component ... a processing component ... and a reporting component". Consequence: the RFQ pricing spreadsheet, the axe-ranking script and the liquidity-score function are inventory items, not "just tools".
- **Model risk is defined as consequences of *use*, not just error.** Model risk is "the potential for adverse consequences from decisions based on incorrect or misused model outputs and reports" (PDF p.3). Two named causes: fundamental errors, and "used incorrectly or inappropriately".
- **"Effective challenge" is the organizing principle.** "[C]ritical analysis by objective, informed parties who can identify model limitations and assumptions and produce appropriate changes" (PDF p.4). It "depends on a combination of incentives, competence, and influence", and incentives are "stronger when there is greater separation of that challenge from the model development process". This is why a bank quant cannot validate their own model.
- **Validation has three required elements** (PDF p.11): "Evaluation of conceptual soundness, including developmental evidence; Ongoing monitoring, including process verification and benchmarking; Outcomes analysis, including back-testing."
- **Process verification includes boring code controls.** "Computer code implementing the model should be subject to rigorous quality and change control procedures to ensure that the code is correct, that it cannot be altered except by approved parties, and that all changes are logged and can be audited" (PDF p.12). Also data: inputs must be "accurate, complete, consistent with model purpose and design, and of the highest quality available".
- **Overrides are data.** "In the use of virtually any model, there will be cases where model output is ignored, altered, or reversed based on the expert judgment of model users. Such overrides are an indication that, in some respect, the model is not performing as intended or has limitations. Banks should evaluate the reasons for overrides and track and analyze override performance" (PDF p.13). A trader who skews away from the model's quote is generating the validator's favourite exhibit.
- **Vendor models are in scope.** "[T]he widespread use of vendor and other third-party products--including data, parameter values, and complete models--poses unique challenges"; where the code is closed the bank "may have to rely more on sensitivity analysis and benchmarking" (PDF pp.15-16). Relevant to Bloomberg, MarketAxess CP+, ICE, Aladdin, Yield Book style analytics.
- **Inventory.** "Banks should maintain a comprehensive set of information for models implemented for use, under development for implementation, or recently retired", with "a specific party ... charged with maintaining a firm-wide inventory"; "[a]ny variation of a model that warrants a separate validation should be included as a separate model" (PDF p.20).
- **Internal audit checks the checkers**, including "the accuracy and completeness of the model inventory" and that "procedures for updating models are clearly documented" (PDF p.19).

**Daily-life translation (analysis, not quotation).** On a bank desk a pricing-model change goes: owner proposes -> independent validation group reviews conceptual soundness and benchmarks -> inventory is updated -> release. On a hedge fund or asset manager SR 11-7 does not bind by statute, but allocators' operational due diligence and (since Jan 2025) the SEC's Two Sigma action make the same questions unavoidable (see section 6.4).

### 2.2 FINRA Rule 5310 (best execution): the quarterly review that someone on the desk must prepare

**Source.** FINRA Rule 5310, https://www.finra.org/rules-guidance/rulebooks/finra-rules/5310 (fetched 2026-10-18; page shows effective date 9 May 2014 for the current text, amendment SR-FINRA-2014-023).

- A member must "use reasonable diligence to ascertain the best market for the subject security". The factors are "the character of the market for the security", "the size and type of transaction", "the number of markets checked", "accessibility of the quotation", and "the terms and conditions of the order which result in the transaction" (5310(a)(1)(A)-(E)).
- If the firm does not review order by order, Supplementary Material .09 requires "regular and rigorous reviews" of execution quality, "conducted on a security-by-security, type-of-order basis", "at a minimum ... on a quarterly basis", asking "whether any material differences in execution quality exist" among markets.
- For debt, Supplementary Material .03: where quotations are available FINRA "will consider the accessibility of such quotations", and "[i]n the absence of accessibility, members are not relieved from taking reasonable steps".
- **Daily-life translation.** In OTC credit there is often no consolidated quote; the "best market" evidence is the RFQ log (dealers asked, cover, response times, hit/miss). That is why a dealer's best-execution committee reads a quarterly pack built from the same RFQ database that powers the desk's hit-ratio dashboard. (Analysis; the pack's contents are firm-specific and I found no public example.)

### 2.3 FINRA Rule 6730 (TRACE): the 15-minute clock

**Source.** FINRA Rule 6730, https://www.finra.org/rules-guidance/rulebooks/finra-rules/6730 (fetched 2026-10-18).

- "Each member that is a Party to a Transaction in a TRACE-Eligible Security must report the transaction." Dealer-to-dealer: both report; member-to-customer: member reports.
- Standard: "as soon as practicable, but no later than within 15 minutes of the Time of Execution." Trades executed 12:00 a.m.-7:59:59 a.m. ET are reported after TRACE opens, within 15 minutes of opening; trades less than 15 minutes before close or after hours are reported after the next business day's open.
- Required fields (6730(c)): identifier, size, price (or elements to compute it), buy/sell indicator, contra-party identifier, capacity ("Principal or Agent (with riskless principal reported as principal)"), Time of Execution, give-up/commission/settlement date and modifiers.
- Late reports must carry an "as/of" designation and the date of execution. "A pattern or practice of late reporting without exceptional circumstances or reasonable justification" can be a Rule 2010 violation (6730(f)).
- ETF creation/redemption transfers and some other categories are excluded (6730(e)).
- **Daily-life translation.** The trader's job ends at "done"; an operations or middle-office role watches the 15-minute clock, fixes the contra ID or capacity flag, and clears TRACE exception queues. A desk that books trades late creates both a compliance exception and, for a quant, a data-quality problem: the tape the desk later back-tests against contains the same cancels, corrections and as/of prints (see `papers_factor_replication_crisis_and_bond_data.md`).

### 2.4 SEC Rule 15c3-5 (market access): the pre-trade checks that sit between a model and the market

**Source.** 17 CFR 240.15c3-5, https://www.law.cornell.edu/cfr/text/17/240.15c3-5 (fetched 2026-10-18).

- Brokers with market access must "[p]revent the entry of orders that exceed appropriate pre-set credit or capital thresholds" and reject orders "that exceed appropriate price or size parameters" (erroneous or duplicate orders); the controls are "under the direct and exclusive control of the broker or dealer".
- The firm must review the business "no less frequently than annually" and the CEO must "on an annual basis, certify that such risk management controls and supervisory procedures comply".
- **Daily-life translation.** The kill-switch and fat-finger limit that Ch 27 specifies is, for an exchange-facing broker, a legal requirement and an annual CEO certification. In credit the rule bites mainly on listed ETFs, futures hedges and equity hedges that a credit desk sends to exchanges and ATSs, not on the RFQ itself (analysis; the rule's "market access" definition is tied to exchanges and ATSs).

(to be filled)

## 3. Bank credit-trading desks and dealers
### 3.1 The best-documented bank credit-derivatives desk day on public record: JPMorgan's CIO synthetic credit book, 2012 (the "London Whale")

**Why it is the anchor source for a bank-desk vignette.** It is not a client-facing dealer desk (it sat in the Chief Investment Office), but two public documents, one of them 300+ pages of emails, recorded calls and audit extracts, describe the *mundane control machinery* of a credit-derivatives book: the daily P&L email, the marking convention, the independent price testing, the VaR spreadsheet, the limit table and the model-review queue. Nothing else public is this granular for credit.

**Sources.**
- U.S. Senate Permanent Subcommittee on Investigations (Levin/McCain), *JPMorgan Chase Whale Trades: A Case History of Derivatives Risks and Abuses*, majority and minority staff report, 15 March 2013, 310 PDF pages. Fetched this session: https://www.hsgac.senate.gov/wp-content/uploads/imo/media/doc/REPORT%20-%20JPMorgan%20Chase%20Whale%20Trades%20(3-15-13).pdf. **Page convention below: printed page = PDF page minus 8.** Hearing record: Senate Hearing 113-96, https://www.govinfo.gov/content/pkg/CHRG-113shrg85162/html/CHRG-113shrg85162.htm (surfaced by search; I did not open it).
- JPMorgan Chase & Co., *Report of JPMorgan Chase & Co. Management Task Force Regarding 2012 CIO Losses*, 16 January 2013 (129 pages per press accounts). I did not open the Task Force PDF this session; every Task Force statement below is as quoted *inside* the Senate report (footnotes cite "2013 JPMorgan Chase Task Force Report, at N"). 8-K announcing it: https://www.sec.gov/Archives/edgar/data/0000019617/000001961713000077/a8-k.htm (surfaced by search; not opened).

**Concrete mundane details (all from the Senate report).**

1. **The daily P&L email and the marker.** The Synthetic Credit Portfolio (SCP) filed "daily profit/loss (P&L) reports ... internally within the bank" (printed p.5). A "junior trader charged with marking the SCP's positions on a daily basis", Julien Grout, produced the marks; his supervisor, head trader Bruno Iksil, led the book (p.5). Two traders "circulated the daily profit-loss email for the SCP" and estimated a daily loss of $43 million, "the largest daily loss yet", with a "$600 million to $800 million 'lag'" (p.83 area, report text around footnote 532; the CIO head said she never read that email).
2. **Marking convention as the lever.** In early January 2012 "the CIO had typically established the daily value of a credit derivative by marking it at or near the midpoint price in the daily range of prices (bid-ask spread)". Later in Q1 it "began to assign more favorable prices within the daily price range" (p.5). The recorded-call line the Subcommittee quotes: "I am not marking at mids as per a previous conversation" (p.5).
3. **The "shadow P&L" spreadsheet.** For five days (12-16 March 2012) Grout "prepared a spreadsheet tracking the differences between the daily SCP values he was reporting and the values that would have been reported using midpoint prices." By 16 March: reported YTD loss $161 million; at mids $593 million (+$432 million) (p.5). On 23 March Iksil estimated in an email that the SCP "had lost about $600 million using midpoint prices and $300 million using the 'best' prices", yet the book reported a daily loss of only $12 million (p.5). 30 March (quarter-end): $319 million reported daily loss, and the Valuation Control Group (VCG) later found a $512 million gap between mid and favourable marking by 31 March (p.5).
4. **A P&L number revised in 90 minutes.** On 10 April 2012 the CIO "initially reported an estimated daily loss of $6 million, but 90 minutes later, after a confrontation between two CIO traders, issued a new P&L report" (p.5).
5. **Independent price testing = tolerances.** A footnote lists VCG tolerance levels for 18 positions, with the IG credit index allowed to "vary from the midpoint market prices by up to 6 basis points" (p.112, fn 675). An analyst described March practice: "The desk marked the book at the boundary of the bid/offer spread depending on whether the position was long or short. We then applied a tolerance to make sure the prices were within tolerance and the majority of positions were" (p.141). The internal-audit review (Q1 2012 continuous audit summary, OCC-SPI-00033688) rated VCG practices "Needs Improvement" for "the absence of a formally applied price sourcing hierarchy", missing concentration reserves, and "lack of formally documented/consistently applied price testing thresholds" (p.141).
6. **Five risk metrics, all breached.** The CIO used VaR, CS01, CSW10% (credit spread widening 10%), stress-loss limits and stop-loss advisories; "the SCP trades breached the limits on all five" during Q1 2012 (p.7). The Subcommittee's remedy proposal: those alerted to a breach should "investigate the cause" and the position "reduced or unwound ... within a few days, without raising the relevant risk limit" (p.214).
7. **The VaR spreadsheet.** A new CIO VaR model went live 27 January 2012. Its author, Patrick Hagan, said "he had to manually enter data into multiple spreadsheets each trading day, which often took hours", and that faulty results went undetected until April or May (p.185). The Task Force, quoted: the Model Review Group "noted that the VaR computation was being done on spreadsheets using a manual process and it was therefore 'error prone' and 'not easily scalable'"; "Data were uploaded manually without sufficient quality control"; "frequent formula and code changes were made" (p.186). A formula/hazard-rate/correlation error "likely had the effect of muting volatility by a factor of two" (p.186, fn 1048). On 18 April 2012 a market-data issue meant VaR for five business days "was understated by appr[o]x[imately] $10m" (p.185). The model was revoked in May 2012.
8. **Size.** Net notional of SCP derivatives "over $51 billion" at end-2011 and "over $157 billion" at end-March 2012 (p.185).
9. **Audit chatter.** The OCC's head capital-markets examiner called the VaR implementation "shocking" and "absolutely unacceptable" (p.186).

**Use.** This is the best public worked example of SR 11-7's three validation elements failing in sequence: model approved despite known operational weakness (conceptual soundness vs process verification), no follow-up on the promised automation (ongoing monitoring), P&L marked inside the spread and tested against tolerance bands (outcomes analysis / independent price verification). It also shows the mundane artefact a desk actually keeps: a *mid-vs-marked spreadsheet*. Vignette caution: all named individuals are real; the book should use composite, unnamed characters and cite the report for the structure of the process.

(to be filled)

## 4. Market makers (Citadel Securities, Jane Street, Optiver, Flow Traders, Virtu, SIG)
(to be filled)

## 5. Multi-strategy pods (Millennium, Citadel, Balyasny, DE Shaw)
(to be filled)

## 6. Systematic asset managers (AQR, Man, Two Sigma, BlackRock systematic, Robeco, RenTech)
(to be filled)

## 7. Distressed funds and restructuring advisers (Elliott, Silver Point, Centerbridge, Davidson Kempner, Monarch, and the PJT seat)
(to be filled)

## 8. Memoirs and books: page-referenced scenes
(to be filled)

## 9. Cross-cutting mundane tasks (a day-part checklist)
(to be filled)

## 10. Vignette seeds (15+)
(to be filled)

## 11. Sources (URLs verified this session)
(to be filled)

## 12. Book placement
(to be filled)
