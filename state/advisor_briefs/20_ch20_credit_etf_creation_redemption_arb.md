# Advisor Brief — Chapter 20: Credit ETF Creation/Redemption Arbitrage (HYG, JNK, LQD, BKLN)

**Target file:** `book_src/20_ch20_credit_etf_creation_redemption_arb.md` (7,000–10,000 words)
**Advisor:** Fable, Edition 1 editorial board. Research date: 2026-10-17.
**TOC scope:** AP mechanics, custom baskets, NAV vs. price, arbitrage bands, and March 2020.
**Status key:** VERIFIED-URL = fetched or read this session; SEARCH-LISTED = URL seen in a search result but not fetched; TITLE-ONLY = cite by title/author/year with no link; CHECK = plausible but unconfirmed, do not state as fact without a source.
**Upstream dossier:** `state/research/trend_electronification_pt_etf_liquidity.md` (complete; feeds §6 below and the Trend Watch boxes).

---

## 1. Thesis and the "aha"

(pending)

## 2. Section outline (20.1, 20.2, …), anatomy mapping, Trend Watch boxes

(pending)

## 3. Derivation skeletons (LaTeX), assumptions, measure, error-prone spots

(pending)

## 4. Code spec and sanity check

(pending)

## 5. Source map (book_id p.N + exact quote ≤60 words)

(pending)

## 6. RESEARCH DOSSIER (dated, sourced; CHECK = unconfirmed)

Facts are appended as found (durability rule), grouped by topic. Each line names its source; CHECK marks anything not confirmed from a primary document this session.

### 6.1 Regulatory plumbing: Rule 6c-11 and custom baskets

- **2019-09-26.** SEC adopted Rule 6c-11 (the "ETF Rule"). Press release 2019-190 (VERIFIED-URL https://www.sec.gov/news/press-release/2019-190): ETFs meeting the conditions may "come directly to market without the cost and delay of obtaining an exemptive order"; more than 300 exemptive orders issued since 1992; approximately 2,000 ETFs with over \$3.3 trillion in net assets at adoption. Scope: open-end ETFs only; UITs, leveraged/inverse, multi-class and non-transparent ETFs excluded.
- **Custom baskets (6c-11(c)(3)).** Baskets that are not pro rata, or that differ from the initial basket used the same business day, are permitted if the ETF adopts written policies and procedures; they must be "in the best interests of the ETF and its shareholders," with recordkeeping of each custom basket. Before the rule, only sponsors with older exemptive orders (pre-2006-era relief; CHECK the exact cutoff year) could use custom baskets freely, so the rule leveled the field. This is the legal fact that makes the "redemption basket as liquidity sink" story (Shim–Todorov, Koont et al.) a general feature, not an iShares quirk.
- **Website disclosure.** Rule requires daily portfolio transparency plus historical premium/discount and bid-ask spread disclosure "to inform investors about trading costs and the efficiency of the arbitrage process" (press release paraphrase). Effective 60 days after Federal Register publication; one-year transition for Form N-1A/N-8B-2; prior exemptive relief rescinded one year after effectiveness. Exact dates: CHECK against the Federal Register notice (expected: effective 2019-12-23, compliance 2020-12-22).

### 6.2 March 2020 and the Fed's SMCCF (primary sources)

- **2020-03-23.** Fed "established the Secondary Market Corporate Credit Facility (SMCCF) on March 23, 2020" (VERIFIED-URL https://www.federalreserve.gov/monetarypolicy/smccf.htm). Treasury equity via the ESF/CARES Act into one SPV shared with the PMCCF. Term sheet dated 2020-07-28 (PDF link on the page). Purchases ended **2020-12-31**. Wind-down announced **2021-06-02**. Monthly transaction-specific disclosures (XLSX) posted January–October 2021; page last updated 2021-10-13. Still to confirm from the term sheet/NY Fed FAQ: ETF purchase start (CHECK: 2020-05-12), bond purchase start (CHECK: 2020-06-16), total ETF purchases (CHECK: about \$8.7bn), ETF eligibility limits (CHECK: no ETF whose price "materially exceeds" NAV; ≤20% of any ETF's assets; "preponderance" IG with the remainder HY).
- **BIS Bulletin No. 6 (Aramonte & Avalos, 2020-04-14).** Headline: "corporate bond exchange-traded funds (ETFs) traded at steep discounts to underlying asset values in March," attributed to "high market volatility, reduced risk-taking by dealers and investors' reaction to policy decisions." Landing page VERIFIED-URL https://www.bis.org/publ/bisbull06.htm; numeric discounts live in the PDF (fetched below if available).
- **Haddad, Moreira & Muir, "When Selling Becomes Viral" (NBER w27168, May 2020; RFS 34(11), 2021, pp. 5309–5351).** VERIFIED-URL https://www.nber.org/papers/w27168. Findings: losses concentrated at the *safe* end (investors sold what they could sell); bond–CDS basis widest for safer bonds; "liquid bond ETFs traded well below NAV," with larger discounts for Treasury, muni and IG ETFs than for HY; the March 23 announcement lowered IG spreads (short maturities, high quality) with "virtually no effect on high yield"; the April 9 expansion moved both IG and HY, including HY bonds that could only benefit indirectly. Useful as the chapter's "quality-flight inverts the usual ordering" point.
- **Gilchrist, Wei, Yue & Zakrajšek, "The Fed Takes on Corporate Credit Risk" (NBER w27809, Sept 2020; J. Monetary Economics 2024, doi 10.1016/j.jmoneco.2024.103573).** VERIFIED-URL https://www.nber.org/papers/w27809. Eligibility-boundary RD: announcements cut eligible-bond spreads about 70bp; within-issuer DiD about 20bp; March 23 cut bid-ask about 10bp within ten days; actual purchases a further about 5bp on spreads and 2bp on bid-ask. Largest April 9 effect on fallen angels.

### 6.3 Basket research (the academic spine of the chapter)

- **Shim & Todorov, "ETFs, illiquid assets, and fire sales" (BIS WP 975, 2021-11-03).** VERIFIED-URL https://www.bis.org/publ/work975.htm. "Fractional baskets": about 10% of holdings in creation baskets and about 20% in redemption baskets for corporate bond ETFs vs. close to 100% for equity and Treasury ETFs; baskets turn over frequently; redemption baskets have shorter duration and larger bid-ask than holdings, creation baskets longer duration and tighter bid-ask; ETFs with fractional baskets show persistent premiums/discounts linked to NAV returns adjusting slowly to ETF returns; APs act as a buffer that can limit fire sales. Bond ETF AUM > \$1.2tn early 2021. (Note the different coverage numbers from Todorov's BIS QR March 2021 piece, which gives about 20% / 35%; both are sample-dependent. Cite each to its own paper.)
- **Koont, Ma, Pástor, Zeng (& Sialm), "Steering a Ship in Illiquid Waters: Active Management of Passive Funds" (NBER w30039, May 2022; RFS 38(10), 2025, pp. 2887–2935, doi 10.1093/rfs/hhaf034).** VERIFIED-URL https://www.nber.org/papers/w30039. ETFs "actively manage their portfolios" by trading off index tracking against liquidity transformation; baskets include cash and only a subset of index bonds, more so when bonds are illiquid; baskets are adjusted to correct portfolio imbalances while facilitating arbitrage; basket inclusion improves bond liquidity in normal times but worsens it when creations/redemptions are highly imbalanced (COVID-19).
- **Todorov, "The anatomy of bond ETF arbitrage" (BIS Quarterly Review, March 2021).** From the upstream dossier: creation baskets cover about 20% of holdings and redemption baskets about 35%; holdings' bid-ask about 17× the ETF's; March 2020 tracking error > 200bp vs. a 0.7bp average. VERIFIED-URL https://www.bis.org/publ/qtrpdf/r_qt2103d.htm.

### 6.4 Shelf hits (Man Group) that frame the trend

- Man 2023 p.2 attributes the 2021 portfolio-trading boom to "the growth of bond ETF trading and the advances made by algorithmic market-making desks on fixed income." Man 2023 p.3: in H1 2022 PT costs rose and "The loss of customised baskets for the ETF creation/redemption process is likely to have been another aggravating factor." That sentence is the chapter's bridge from Ch 19 (PT) to Ch 20: the custom basket is the cheapest way for a dealer to recycle a PT.
- Man 2022 p.4 calls ETFs "essentially passive quant investing"; p.9: "The rise of passive bond ETFs has potentially created further distortions that will drive pricing away from fundamentals and produce opportunities for active investment strategies."

### 6.5 Rule 6c-11, exact text (VERIFIED from the SEC adopting release PDF, https://www.sec.gov/rules/final/2019/33-10695.pdf, and the LII mirror of 17 CFR 270.6c-11, https://www.law.cornell.edu/cfr/text/17/270.6c-11)

- **Effective date 2019-12-23** ("DATES: Effective Date: This rule is effective December 23, 2019."). Compliance dates for the form amendments: one year after the amendments' effective date (section II.L of the release; CHECK the exact calendar day, expected 2020-12-22). Prior exemptive relief for ETFs that can rely on the rule terminates one year after the rule's effective date.
- **Definitions, 6c-11(a)(1).** *Authorized participant*: "a member or participant of a clearing agency registered with the Commission" with a written agreement to place creation/redemption orders. *Basket*: "the securities, assets or other positions in exchange for which an exchange-traded fund issues" (or redeems) creation units. *Creation unit*: "a specified number of exchange-traded fund shares that the exchange-traded fund will issue to (or redeem from)" an AP in exchange for a basket and a cash balancing amount. *Cash balancing amount*: "an amount of cash to account for any difference between the value of the basket" and the creation unit's NAV. *Custom basket*: (A) "A basket that is composed of a non-representative selection of the exchange-traded fund's portfolio holdings"; or (B) a representative basket that differs from the initial basket used in transactions on the same business day.
- **Website disclosure, 6c-11(c)(1).** Daily NAV, market price and premium/discount as of the prior close; "median bid-ask spread, expressed as a percentage rounded to the nearest hundredth," computed from quotes sampled over the last 30 calendar days; and "If the exchange-traded fund's premium or discount is greater than 2% for more than seven consecutive trading days," the fund must say so and discuss the contributing factors, kept on the website "for at least one year thereafter." (This is why every issuer page now shows a "30-day median bid/ask" of 0.01% for HYG/LQD/JNK: the chapter can joke that the rule mandated the statistic that makes the ETF look more liquid than anything it holds.)
- **Basket policies, 6c-11(c)(3).** The ETF "must adopt and implement written policies and procedures that govern the construction of baskets"; for custom baskets they must "Set forth detailed parameters for the construction and acceptance of custom baskets" and "Specify the titles or roles of the employees of the exchange-traded fund's investment adviser" who review each custom basket. **Recordkeeping, 6c-11(d)(2)(ii):** each basket record states whether it was custom and, if so, that it complied with the (c)(3) policies; five-year retention.

### 6.6 SMCCF term sheet (effective 2020-07-28; VERIFIED from the PDF https://www.federalreserve.gov/newsevents/pressreleases/files/monetary20200728a1.pdf) and NY Fed operations page (VERIFIED-URL https://www.newyorkfed.org/markets/secondary-market-corporate-credit-facility)

- The SPV "will purchase in the secondary market (i) eligible individual corporate bonds; (ii) eligible corporate bond portfolios in the form of exchange-traded funds ("ETFs"); and (iii) eligible corporate bond portfolios that track a broad market index." Treasury equity \$75bn for SMCCF + PMCCF combined, initial allocation \$50bn PMCCF / \$25bn SMCCF; combined size "up to \$750 billion." (March 23 release: "up to \$300 billion in new financing" across TALF/PMCCF/SMCCF with \$30bn Treasury equity; April 9 release: the three programs "will now support up to \$850 billion in credit backed by \$85 billion in credit protection provided by the Treasury." VERIFIED-URL https://www.federalreserve.gov/newsevents/pressreleases/monetary20200323b.htm and .../monetary20200409a.htm.)
- **Eligible ETFs (exact):** "U.S.-listed ETFs whose investment objective is to provide broad exposure to the market for U.S. corporate bonds. The preponderance of ETF holdings will be of ETFs whose primary investment objective is exposure to U.S. investment-grade corporate bonds, and the remainder will be in ETFs whose primary investment objective is exposure to U.S. high-yield corporate bonds."
- **Fallen angels:** issuer "rated at least BBB-/Baa3 as of March 22, 2020"; if subsequently downgraded, "must be rated at least BB-/Ba3 as of the date on which the Facility makes a purchase." Bonds: remaining maturity 5 years or less.
- **Leverage:** 10:1 on IG bonds and IG ETFs; 7:1 on HY bonds; 3:1–7:1 "depending on risk" on other eligible assets (i.e., HY ETFs).
- **Limits:** 1.5% of the combined facility size per issuer; 10% of an issuer's maximum bonds outstanding (2019-03-22 to 2020-03-22); "The Facility will not purchase shares of a particular ETF if after such purchase the Facility would hold more than 20 percent of that ETF's outstanding shares."
- **Pricing (the arbitrage-relevant clause):** "The Facility will avoid purchasing shares of eligible ETFs when they trade at prices that materially exceed the estimated net asset value of the underlying portfolio." Termination of purchases "no later than December 31, 2020."
- **Timeline (NY Fed):** BlackRock FMA retained as investment manager 2020-03-24; "The SMCCF began purchases of eligible ETFs on May 12, 2020, and of eligible corporate bonds on June 16, 2020" (NY Fed FAQ, VERIFIED-URL https://www.newyorkfed.org/markets/primary-and-secondary-market-faq/corporate-credit-facility-faq); approximately \$14.2bn of eligible assets at the first weekly report after purchases ended; ETF holdings "account for over half of the SMCCF portfolio"; ETF sales began 2021-06-07, bond sales 2021-07-12; "As of August 31, 2021, all of the SMCCF's holdings of corporate bonds either matured or were sold and its ETFs were sold"; SPV terminated 2021-12-17. Sale-side mirror clause: "The SMCCF will avoid selling shares of an ETF at times when it is trading at a price that is materially below" estimated NAV. Total ETF purchases (CHECK: about \$8.7bn across 16 ETFs, with LQD the largest single holding; confirm from the transaction-specific disclosure XLSX before stating).

### 6.7 ETF facts as of 2026-10-16 (issuer pages fetched this session; secondary where noted)

| ETF | Inception | AUM | Holdings | ER | 30-day median bid/ask | Prem/disc | Index | Other |
|---|---|---|---|---|---|---|---|---|
| HYG (iShares iBoxx \$ High Yield Corporate Bond) | 2007-04-04 | \$17.18bn (2026-10-16) | 1,334 | 0.49% | 0.01% | +0.02% | iBoxx USD Liquid High Yield | 30-day ADV 64.6m shares; 30-day SEC yield 7.29% |
| LQD (iShares iBoxx \$ Investment Grade Corporate Bond) | 2002-07-22 | \$28.78bn (2026-10-16) | 3,171 | 0.14% | 0.01% | +0.04% | iBoxx USD Liquid Investment Grade | 30-day ADV 35.0m shares; SEC yield 5.99% |
| JNK (SPDR Bloomberg High Yield Bond) | 2007-11-28 | \$5.72bn (2026-10-15) | 1,161 (index 1,051) | 0.40% | 0.01% | +0.15% | Bloomberg High Yield Very Liquid | NAV \$92.49; 61.87m shares; days at premium/discount: 2025 = 206/44; Q1-26 47/14; Q2-26 53/9; Q3-26 49/15 |
| BKLN (Invesco Senior Loan) | 2011-03-03 ("the first bank loan ETF," Invesco case study) | \$6.16bn (stockanalysis.com, 2026-10-16; secondary, CHECK against Invesco) | 185 | 0.65% | n/a | n/a | Morningstar LSTA US Leveraged Loan 100 | "will normally invest at least 80% of its total assets" in index components (Invesco) |

Sources: HYG https://www.ishares.com/us/products/239565/ishares-iboxx-high-yield-corporate-bond-etf; LQD https://www.ishares.com/us/products/239566/ishares-iboxx-investment-grade-corporate-bond-etf; JNK https://www.ssga.com/us/en/intermediary/etfs/spdr-bloomberg-high-yield-bond-etf-jnk; BKLN case study https://www.invesco.com/us/en/insights/case-study-bkln-enabling-access-senior-loans.html (all VERIFIED-URL). Creation-unit sizes were not shown on any page (CHECK the prospectuses; Invesco's boilerplate lists 10,000–150,000 share units as typical). Note the trend hidden in the table: HYG's AUM (about \$17bn) is far below its 2020 peak (CHECK: about \$30bn in mid-2020) as flows migrated to cheaper broad HY ETFs (USHY; CHECK AUM) while LQD stayed near \$29bn. The JNK premium-day counts (206 vs. 44 in 2025) are the visible footprint of bid-side NAV marking (see §6.9).

### 6.8 Trend data 2024–2026 (search-listed secondary coverage; CHECK before quoting precisely)

- Bond ETF AUM above \$2.5tn and a record \$64bn monthly bond-ETF inflow (May 2026 State Street data via Advisor Perspectives, 2026-06-05; SEARCH-LISTED https://www.advisorperspectives.com/commentaries/2026/06/05/bond-etfs-hit-record-64b-as-investors-pivot-to-broad-beta). Bond ETF YTD inflows \$407bn through August 2026 vs. a 2025 full-year record of \$448bn (Wealth Professional, SEARCH-LISTED); a 2026-09-15 commentary says \$446bn through 2026-09-11 "already above full-year 2025" (the two figures conflict; CHECK against State Street's Flash Flows). US-listed ETF assets \$15.8tn at mid-2026 with \$2.3tn full-year inflow projected (SSGA H1 2026 note, SEARCH-LISTED https://www.ssga.com/us/en/institutional/insights/etf-inflows-set-records-in-first-half).
- Upstream dossier (verified there): credit ETF ADNV \$7.7bn in 2024 (−7%) while cash bonds grew 21%; ETF-to-cash volume ratio 23.2% (2022) → 16.6% (2024) (Coalition Greenwich); \$99bn of FI ETFs traded on 2025-04-07, about 60% iShares (The DESK); US bond ETFs \$1.8tn at end-2024, 17% of ETF assets, with about 17% of HY bond ETF activity in the primary market (ICI 2025 Fact Book); Man 2023 p.3 on the loss of custom baskets in H1 2022.
- **ETF share classes.** SEC order granting Dimensional exemptive relief for ETF share classes of mutual funds, 2025-11-17 (Seward & Kissel 40 Act blog, 2025-11-19, SEARCH-LISTED https://40actblog.sewkis.com/blog/sec-issues-order-for-dfa-exemptive-application-opening-the-door-to-etf-share-classes); combined notice to 30 applicants 2025-12-22 (same blog); Vanguard's patent on the structure expired in 2023. Relevance: a mutual fund with an ETF share class can push redemptions out in kind through the ETF class, which exports the fund's liquidity transformation into the AP channel; a bond-fund version would make the custom-basket machinery of this chapter the exit door for \$-trillions of 1940-Act bond money. CHECK which bond complexes have launched ETF classes by late 2026.
- **Private credit in an ETF wrapper.** SPDR SSGA Apollo IG Public & Private Credit ETF (PRIV) launched late February 2025; the SEC sent State Street a public letter the day after launch raising Rule 22e-4 (15% illiquid cap), valuation and naming concerns; Apollo contractually provides firm intraday bids on the private credit it sources (CFRA via Benzinga/InvestmentNews, SEARCH-LISTED). CHECK the letter date (reported 2025-02-27) and State Street's response (reported: rename and cap illiquid at 15%). Relevance for Ch 17 and this chapter's §20.9 (what the basket can contain).
- **Rule 22e-4 (adopted 2016-10-13, SEC press release 2016-215, VERIFIED-URL https://www.sec.gov/news/pressrelease/2016-215.html):** four liquidity buckets; 15% illiquid cap (illiquid = cannot be sold within seven calendar days without significantly changing market value); highly liquid investment minimum; "In-Kind ETFs" exempted from parts of the rule and flagged on Form N-CEN; compliance 2018-12-01 (large complexes) and 2019-06-01 (< \$1bn). BKLN, which cannot settle loans in seven days, lives under this rule: its cash/HY-bond sleeve is the regulatory artifact. Loan settlement averaged 17 days in Q2-2016 (Markit via Morningstar/Benzinga 2017, secondary; CHECK LSTA's current T+ figures, which Ch 21 owns).
- **BKLN mechanics (secondary; CHECK):** about 10% in cash and more-liquid HY bonds, tilt to the largest loans, and a line of credit for "emergency liquidity events" (Morningstar via Benzinga, 2017); pre-2020 maximum discount about 38bp in one year with a 67bp spike (etf.com, undated). The March 2020 BKLN discount and whether creations/redemptions ran in cash were not confirmed this session (etf.com returned 403); the writer must mark any number *illustrative* or find Invesco's 2020 annual report.

## 7. Case studies

(pending)

## 8. Humor beats using the canon cast

(pending)

## 9. Resource candidates (VERIFIED-URL / TITLE-ONLY)

(pending)

## 10. Exploratory-space notes

(pending)
