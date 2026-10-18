# Credit relative value: the literature and the mechanics of long-one-credit, short-another

Researcher dossier for the book "Systematic & Quantitative Credit: From PJT RSSG to the Automated Desk" (second edition queue, slug `rv_credit_pairs_literature_and_mechanics`). Compiled 2026-10-18. Serves user directive 13 (the RV thread, `state/rv_thread_plan.md`): chiefly Ch 8, 8-B, 8-C, 24, 28, with beats in Ch 3, 4-B, 5, 6, 7, 9, 10, 12-B to 16, 18 to 20, 22. Evidence table, mechanics with worked numbers, and chapter placement follow the annotated bibliography.

## 1. Scope and status

Scope. The pod-shop trade: long one credit, short another (or an index, ETF, CDS), hedged so that what is left is issuer-specific. This dossier covers (a) the literature on whether that trade pays and what it risks, (b) the mechanics a desk must get right: shorting, short-leg choice, hedge ratios, jump-to-default, carry and funding, P&L attribution. It builds on, and does not repeat: `papers_factor_replication_crisis_and_bond_data.md` (factor and cost literature, B-numbers), `trend_systematic_credit_industry.md` (industry and leverage), `trend_listed_credit_futures_and_index_microstructure.md` (CDX, futures, margins), `trend_electronification_pt_etf_liquidity.md` (ETF stress), `life_quant_shop_daily_life.md` (pod rules, S12-S14), `perspectives_dealers_and_systematic_shops.md`. Book chapters 8 (sections 8.4, 8.6) and 24 already derive DTS-neutral pairs and the basis; this file supplies the evidence and the missing mechanics around them.

Status. 24 handles (R1-R24, more than 40 papers, reports and rules). Nine were read at full-text level (R1, R3, R7, R11, R14, R15, R22 and, in part, R20 and R24); the rest at abstract or record level; each entry says which. Dates: today is 2026-10-18; the newest sources are the IMF blog of 6 Oct 2026 and the SEC order of 3 Dec 2025. Worked numbers in Section 5 are illustrative inputs; the arithmetic was run by script. Every quotation was on a fetched page or a shelf page.

## 2. Findings in brief

1. **The published case for credit RV is one window and its failure.** Capital-structure arbitrage (short rich CDS, hedge with stock) earned a Sharpe near 1.2 over 2001-2004 on 48 monthly returns but needed $45 to $90 of capital per $100 CDS notional for 10% volatility, and "convergence occurs for only a small fraction of the individual trades" (R1, R2). Over 2005-2009 the classical rule had negative Sharpe ratios and tracked a fixed-income-arbitrage index returning -4.84% a year (R3).
2. **Pairs evidence on cash bonds is thin.** No peer-reviewed pairs test on cash corporate bonds, one CDS pairs paper with no performance numbers (R5), and one hedge-ratio experiment on CDS (R7). The pod's core trade rests on mechanism and practice, not a published backtest; the book should say so and give a replication spec (Section 8).
3. **A hedge ratio is a model, and the models disagree.** On 392 CDS pairs DTS gave the lowest volatility (11.2 bp a week) and a stable ratio; empirical beta looked best on market correlation (0.11) only because oversized random errors cancelled; in 2007-2008 every hedge degraded (R7). Near default DTS fails: match on market value.
4. **"Idio" is whatever the factor model leaves, and not all of it is idiosyncratic.** Residuals are highly cross-correlated, mostly one latent factor (R9). Equity deltas hedge bonds well; analytical duration over-hedges rates (R8). Residual signals beat total-return signals (R10). Test an idio claim by checking whether residual P&L correlates across the book's own pairs.
5. **Shorting a cash bond is cheap on average and hard where it matters.** Average fees 18 to 33 bp (2004-2007), steep above 70% on loan, 173 to 245 bp around bankruptcies, recallable on demand; no public bond short-interest tape and Rule 10c-1a reporting delayed to 2028 (R11, R16). Bonds costly to short are rich to CDS (R12, R17), so borrow fee and basis are one variable, and CDS, CDX and ETFs become the practical short, each with a basis (5.2).
6. **Two-leg books die in funding and crowding.** GM/Ford 2005 (hedge leg failed 4 May, credit leg 5 May, crowded correlation trades) and the post-Lehman basis, where hedge funds, not dealers, drove the dislocation (R20, R22, R23). Official sources cite 30x gross leverage and a 12% NAV loss per 100 bp for relative value funds (R24); there is no public data on credit-RV pod crowding.
7. **A pair's P&L is judged on idio and paid on the net.** In the worked month (Section 5.6) idio P&L is $40.5k, the net is $13.3k: hedge leakage and frictions took 67% of the thesis.

## 3. Annotated bibliography

Tags: [FT] full text read, [ABS] abstract or record read, [REC] bibliographic record only, [SEC] secondary summary only. Links only where fetched this session.

### 3.A Strategy-level evidence: does credit RV pay, and for what risk?

**R1. Duarte, Longstaff, Yu (2007), "Risk and Return in Fixed-Income Arbitrage: Nickels in Front of a Steamroller?", Review of Financial Studies 20(3), 769-811. [FT]** https://www.johnhcochrane.com/s/Duarte_Longstaff_Yu_nickelsRFS.pdf (author-hosted copy). Five rule-based strategies scaled to 10% annual volatility; yield-curve, mortgage and capital-structure alphas are significant after factor controls, and an equal-weighted portfolio of those "intellectual capital" strategies stays significant after 2/20 fees. Capital-structure arbitrage (Section 5): CreditGrades model spread versus Markit 5-year CDS, 261 North American obligors, 135,759 daily spreads, Jan 2001 to Dec 2004; if the market spread exceeds the model by a trigger, short $100 of CDS and short stock by the model delta; exit on convergence or after 180 days; 5% CDS bid-ask. Equal-weighted: mean 0.705% a month (t = 1.70), Sharpe 1.203, alpha t = 2.11, about 0.68% a month net of fees. Capital needed per $100 notional for 10% volatility: $44.9 to $90.5 (equal-weighted $66.25) versus $3.7 to $15.8 for swap-spread arbitrage, because "convergence occurs for only a small fraction of the individual trades". At a 0.5 trigger the mean is zero or negative. The GM vignette (2002, May 2005) is the canonical hedge-leg failure. Caveat: 48 monthly returns.

**R2. Yu (2006), "How Profitable Is Capital Structure Arbitrage?", Financial Analysts Journal 62(5), 47-62 (DOI 10.2469/faj.v62.n5.4282). [ABS]** https://rpc.cfainstitute.org/research/financial-analysts-journal/2006/how-profitable-is-capital-structure-arbitrage (record; full text member-only, unread). Same panel and CreditGrades benchmark as R1 (Yu is R1's third author). Individual trades can lose substantially because CDS spreads and equity prices are weakly correlated; an equal-weighted portfolio earns Sharpe ratios like other fixed-income arbitrage and hedge fund benchmarks.

**R3. Avino, Lazar (2012), "Rethinking Capital Structure Arbitrage", MPRA Paper 42850. [FT]** https://mpra.ub.uni-muenchen.de/42850/2/MPRA_paper_42850.pdf (extracted locally). Out-of-sample sequel: for 70 obligors, Jan 2005 to Dec 2009 (pre-crisis to Jul 2007, crisis from Aug 2007), the classical strategy "generated negative Sharpe ratios" in both sub-periods; the CSFB/Tremont AllHedge Fixed Income Arbitrage Index over 2005-2009 had mean -4.84% a year, volatility 12.82%, Sharpe -0.38, skewness -3.1, excess kurtosis 16.17, and the classical strategy's returns correlate highly with it. A 10% CDS bid-ask is assumed (R1: 5%). Four alternative rules weighting equity versus CDS by price discovery do better in the crisis (best Sharpe 1.24), not before it. Working paper.

**R4. Kapadia, Pu (2012), "Limited arbitrage between equity and credit markets", Journal of Financial Economics 105(3), 542-564. [ABS]** https://ideas.repec.org/a/eee/jfinec/v105y2012i3p542-564.html. Short-horizon equity-credit pricing gaps are common and a meaningful share are anomalous; the degree of integration moves with liquidity in both markets and idiosyncratic risk. Companion: Hilscher, Pollet, Wilson (2015), JFQA 50(3), 543-567 [SEC, search summary only]: equity returns predict CDS changes, not the reverse.

**R5. Kato, Nakamura (2023), "Cointegration analysis of hazard rates and CDSs: Applications to pairs trading strategy", Physica A 612, 128489. [ABS]** https://ideas.repec.org/a/eee/phsmap/v612y2023ics0378437123000444.html. Cointegrated hazard-rate (VECM) model, Japanese corporate CDS; the abstract reports no performance numbers. The only peer-reviewed CDS pairs paper I could open.

### 3.B Hedge ratios and what "idio" means

**R6. Ben Dor, Dynkin, Hyman, Houweling, van Leeuwen, Penninga (2007), "DTS (Duration Times Spread)", Journal of Portfolio Management 33(2), 77-100 (DOI 10.3905/jpm.2007.674795). [SEC]** Citation from Crossref; content from Robeco's explainer https://www.robeco.com/en-sg/insights/2024/08/duration-times-spread-a-measure-of-spread-exposure-in-credit-portfolios (the paper itself and the CFA Digest PDF were unreadable). Spread volatility scales with spread level, so credit moves in relative terms and excess-return volatility is proportional to duration times spread. Robeco's example: spread duration 1 at 500 bp and 10 at 50 bp share DTS = 500 and move 10% together. A 2026 reassessment by Ben Dor, Dynkin, Hyman and Polbennikov, "Twenty Years of Duration Times Spread (DTS)", Journal of Fixed Income 36(2), 89-115, exists (Crossref record, DOI 10.3905/jfi.2026.018) [REC]; its content is unread.

**R7. Ben Dor et al., "Hedging the Market Risk in Pairs Trades" (chapter 8) and its 2007-2008 re-run (chapter 10), Quantitative Credit Portfolio Management (shelf id `Ben_Dor_Quantitative_Credit_Portfolio_Management`, PDF pp. 228-237, 270-274). [FT of pages]** The best public pair-hedging experiment. Weekly 5-year CDX.NA.IG constituent CDS, Nov 2003 to Dec 2006; 63 issuers in five industries; 392 same-industry pairs; each leg sized to one unit of market risk; hedges: risky PV01 (equal notionals), DTS, empirical beta (24-week window; 52-week in Table 8.2). Table 8.1 (24-week beta), in that order: P&L volatility 13.3 / 11.2 / 18.0 bp a week; hedge-ratio standard deviation 0.0 / 0.3 / 1.3; average absolute market correlation 0.37 / 0.23 / 0.11; systematic variance share 18.6% / 12.6% / 18.9%. The beta hedge's low correlation is spurious: when a trailing beta nears zero the short is hugely oversized, errors land randomly, like a coin-flip strategy that goes long or short the market each week. The DTS ratio predicts next-period beta with R-squared 0.36 (26 weeks) and 0.50 (52 weeks), unbiased (slope 1.09, 1.05), against 0.19 and 0.23 for the prior empirical beta, which mean-reverts halfway to 1 (Table 8.3). Halving the DTS short leaves a trade beta of about 0.5. Crisis re-run (2007-2008, 26-week betas): volatility 159.1 / 117.5 / 137.3 bp a week; systematic share 21.6% / 25.6% / 41.1% (ex-financials, DTS lowest at 19.2%); "all hedging methods were less effective" than pre-crisis. Chapter 9 (printed p.220): near default, bonds "trade on price rather than spread" and long-short positions "should be matched on a market-value basis rather than DTS-hedged"; a utility steepener lost 4.73% in July 2002 (El Paso, PSEG Energy Holdings, Williams), information ratio 0.2 with that month and 0.8 without. Caveat: CDS not cash, directional views randomly assigned (a test of hedges, not of alpha). Ch 8 section 8.4 already uses the 1.4 versus 0.6 hedge-ratio dispersion from the bond version.

**R8. Schaefer, Strebulaev (2008), "Structural models of credit risk are useful: Evidence from hedge ratios on corporate bonds", Journal of Financial Economics 90(1), 1-19. [ABS]** https://ideas.repec.org/a/eee/jfinec/v90y2008i1p1-19.html. Structural models predict bond prices poorly but give "quite accurate predictions of the sensitivity of corporate bond returns to changes in the value of equity"; the Merton model "does not capture the interest rate sensitivity of corporate debt", which is substantially lower than duration implies; bond prices load on market factors such as Fama-French SMB that the models do not predict. The equity delta is the hedge that works; the analytical rate hedge is the one that over-hedges.

**R9. Collin-Dufresne, Goldstein, Martin (2001), "The Determinants of Credit Spread Changes", Journal of Finance 56(6), 2177-2207. [ABS]** https://ideas.repec.org/a/bla/jfinan/v56y2001i6p2177-2207.html. Theory-motivated variables explain little of monthly spread changes; the residuals "are highly cross-correlated", driven mostly by "a single common factor" the authors cannot proxy; changes are "principally driven by local supply/demand shocks". For the pair book: the regression residual is not idiosyncratic, and its common part is what a crowded unwind trades on. (The "75% unexplained" figure that circulates is not in the abstract; unused.)

**R10. Haesen, Houweling, van Zundert (2017), "Momentum spillover from stocks to corporate bonds", Journal of Banking & Finance 79, 28-41 (SSRN 2131032, 2012). [SEC]** Robeco summary https://robeco.com/en-uk/insights/2012/08/residual-equity-momentum-for-corporate-bonds: ranking issuers on the firm-specific (residual) part of stock returns lowers factor exposures and roughly halves volatility versus raw momentum, raising the Sharpe ratio. A search summary adds figures (1994-2011; volatility 6.16% total versus 3.25% residual) that I did not verify. Related [REC, Crossref only]: Gebhardt, Hvidkjaer, Swaminathan (2005), JFE 75(3), 651-690; Campbell, Taksler (2003), "Equity Volatility and Corporate Bond Yields", JF 58(6), 2321-2350 (idiosyncratic equity volatility prices into spreads); Chung, Wang, Wu (2019), JFE 133(2), 397-417. Factor papers are in `papers_factor_replication_crisis_and_bond_data.md` (B9, B11, B12).

### 3.C Shorting and borrow

**R11. Asquith, Au, Covert, Pathak (2013), "The market for borrowing corporate bonds", Journal of Financial Economics 107(1), 155-182 (DOI 10.1016/j.jfineco.2012.08.007); NBER WP 16282 (Aug 2010). [FT of the NBER version]** https://nber.org/papers/w16282 and https://dspace.mit.edu/handle/1721.1/73466 (the NBER PDF was read in full). Data: one large custodian lender, 2004-2007, 367,000+ loans on almost 10,000 bonds, $193bn average loanable inventory (2.9% of $6.6tn outstanding), 7.4% on loan. Mean and median annual borrowing cost 33 and 18 bp (19 and 13 bp by 2007; abstract: "between 10 and 20 basis points"); flat near 30 bp until about 70% of inventory is on loan, then more than 10 bp for each further 10%; a full-letter downgrade adds about 9.7 bp (38.4 bp average before, 52.3 bp after); bankruptcy filers pay 173 bp in the 30 days before and 245 bp after; the dearest loan seen is 14.5% on a Calpine bond. Mechanics (their Section 2): three days to locate; 102% cash collateral marked daily (99.6% of loans); Reg T investors post 50% more; loans are "on demand", recallable at any time, so rolled nightly; the fee is the market collateral rate minus the rebate (20 bp fee at a 100 bp rate gives an 80 bp rebate; negative rebates occur); 31.2% of loans shrink before closing; coupons are paid back to the lender. Shorting is about 19.1% of corporate bond trades (their estimate); matched stock and bond loans are within 10 bp 60.1% of the time; no evidence of private information and no excess return from trading on borrow cost; bonds with CDS are lent more, so CDS growth has not replaced bond shorting. Caveats: one lender, pre-crisis, no prime-broker view.

**R12. Nashikkar, Pedersen (2007), "Corporate Bond Specialness", NBER/AQR working paper. [ABS]** https://www.aqr.com/Insights/Research/Working-Paper/Corporate-Bond-Specialness (abstract; PDF returned the abstract only). Custodian data: about 3% of bonds on loan; fees highest for risky, low-rated bonds, especially around downgrades, and for small, old bonds; bonds with high shorting costs are overpriced relative to CDS (a more positive bond-CDS basis), and equity specialness predicts the same. A search summary of the author's CV mentions 11% of loaned bonds above 50 bp; unverified, unused.

**R13. Hendershott, Kozhan, Raman (2020), "Short Selling and Price Discovery in Corporate Bonds", JFQA 55(1), 77-115. [ABS]** https://ideas.repec.org/a/cup/jfinqa/v55y2020i1p77-115_3.html. Bond short selling predicts returns, especially in high yield and after Lehman, in the shorted bond and the issuer's other bonds; information flows from stocks to bonds, not back. In tension with R11.

**R14. Dynkin et al., Systematic Investing in Credit, chapter 21 (`Dynkin_Systematic_Investing_in_Credit`, PDF pp. 793-797). [FT of intro and data section]** Equity short interest predicts bond underperformance and downgrades; issuers with the highest short interest within a rating bucket are the likeliest downgrades over 3 to 12 months; bond short interest is "subsumed" by equity short interest and is not useful in IG because IG bonds "are likely shorted as part of market-making activity"; combined with excess spread to peers it earns "almost twice the risk-adjusted return". The FIS Astec lending data (loan stages include "recalled") are a lower bound.

**R15. Man Group (2022), "Quantitative Credit: Alpha Opportunities for Early Movers", pp. 10-11 (`Man_Quantitative_Credit_Alpha_Early_Mover_2022`). [FT of pages]** A manager's statement, not independent evidence: long-short quant credit leverage "starts at 4-5x"; prime-broker lending desks give "daily feeds with firm borrow availability and fees across the entire investable cash bond universe", once "manual and ad hoc"; cash bonds preferred to CDS because only about 100 US CDS names trade regularly (perhaps 200 more sporadically) against 10,000+ bonds, and because of manufactured credit events.

**R16. Market data and rules.** EquiLend FY2025: corporate bond lender-to-broker revenue $463m (+8%), balances +22%, fees -12% (https://mondovisione.com/media-and-resources/news/equilend-securities-lending-revenue-soars-to-all-time-highs-of-153-billion-202616/; all-asset revenue $15.3bn per https://www.hedgeweek.com/global-securities-lending-revenue-hits-record-15-3bn-in-2025/). Hu, Pan, Wang (2021, JFQA 56(1); NBER WP 21502), https://www.nber.org/papers/w21502 [ABS]: tri-party repo haircut dispersion is largest for corporate-bond and equity collateral, set mostly by the lending fund family's policy. Regulation SHO's locate rule applies to "any equity security" (https://www.sec.gov/rules/2004/07/short-sales); SEC Rule 10c-1a (loan reporting to FINRA) was delayed by the SEC's 3 Dec 2025 order to 28 Sep 2028 (public dissemination later still) after the Fifth Circuit remanded it in Aug 2025 (https://www.proskauer.com/blog/sec-again-extends-short-sale-and-securities-lending-rules-compliance-deadlines-to-2028-while-it-considers-response-to-court-ruling; the earlier July 2025 dates are at https://www.dechert.com/knowledge/onpoint/2025/8/sec-extends-compliance-deadlines-for-securities-lending-transpar.html). Corporate-bond coverage by 10c-1a is unconfirmed.

### 3.D The basis as a trade, and as the short leg

**R17. Bai, Collin-Dufresne (2019), "The CDS-bond basis", Financial Management 48(2), 417-439. [ABS]** https://ideas.repec.org/a/bla/finmgt/v48y2019i2p417-439.html. Basis deviations are larger for bonds with more trading illiquidity, funding cost, counterparty risk and weaker collateral; the basis becomes more negative when the bond lending fee is higher, read as arbitrageurs avoiding negative-basis trades when short interest is high.

**R18. Nashikkar, Subrahmanyam, Mahanti (2011), "Liquidity and Arbitrage in the Market for Credit Risk", JFQA 46(3), 627-656. [ABS]** https://ideas.repec.org/a/cup/jfinqa/v46y2011i03p627-656_00.html. Bonds with higher "latent liquidity" are expensive relative to CDS, as are illiquid bonds of uncertain firms (shorting them is costly); "the CDS spread does not fully capture the credit risk of the bond".

**R19. Garleanu, Pedersen (2011), RFS 24(6), 1980-2022 (NBER WP 16777). [ABS]** https://www.nber.org/papers/w16777. With margin-constrained agents, identical cash flows with different margins trade at different prices ("bases"); bases widen when margin constraints bind; tested on CDS-bond bases.

**R20. Choi, Shachar (2013), "Did Liquidity Providers Become Liquidity Seekers?", NY Fed Staff Report 650. [FT of abstract and introduction]** https://www.newyorkfed.org/medialibrary/media/research/staff_reports/sr650.html. After Lehman, dealers absorbed client selling and their inventories rose; hedge funds unwinding pre-crisis basis trades were the main driver of the large negative basis; losses concentrated in bonds with CDS and high basis-trade activity; limited arbitrage capital kept the basis open.

**R21. Oehmke, Zawadowski (2017), "The Anatomy of the CDS Market", RFS 30(1), 80-119. [ABS]** https://ideas.repec.org/a/oup/rfinst/v30y2017i1p80-119..html. "Speculative trading concentrates in the CDS"; the basis trade compresses the negative basis and lowers bond price impact. D'Amico, Kurakula, Lee (2020), Chicago Fed WP 2020-14 [SEC, search only]: ETF and CDX reactions to the March and April 2020 Fed facility announcements.

### 3.E Crowding, funding and leverage

**R22. BIS (2005), box "Stress testing of credit markets: the downgrade of General Motors and Ford", BIS Quarterly Review, June 2005, p. 6. [FT of box]** https://www.bis.org/publications/qr-200506.pdf (text extracted locally). GM and Ford were about 3% of the IG bond market, potentially 15% of global high yield; cash adjusted in an orderly way, credit derivatives "gapped". "It is easier to take positions – especially short positions – in credit derivatives markets than in corporate bond markets." Two RV trades "suffered large mark to market losses": (1) GM convertibles versus a replicating portfolio, "lost money on both legs" (4 May GM stock +18% on Kerkorian's bid; 5 May bond and CDS widening on S&P's downgrade); (2) long correlation (sell iTraxx Europe equity-tranche protection, buy index protection), earning 300 to 400 bp in early 2005 until default correlation fell sharply on idiosyncratic worries and unwinds pushed mezzanine and index spreads in opposite directions. "Many leveraged investors had similar positions, and this concentration of activity magnified the deleveraging process", akin to 1998 though hedge funds were "significantly less leveraged".

**R23. Mitchell, Pulvino (2012), "Arbitrage crashes and the speed of capital", JFE 104(3), 469-490. [ABS]** https://ideas.repec.org/a/eee/jfinec/v104y2012i3p469-490.html. Prime-broker failure risk in 2008 cut hedge-fund leverage; "seemingly long-term debt capital became short-term capital"; arbitrageurs could not keep similar assets similarly priced. Records only [REC]: Brunnermeier, Pedersen (2009), RFS 22(6); Stein (2009), JF 64(4), 1517-1548; Khandani, Lo (2007), SSRN 1015987.

**R24. Official leverage and concentration data. [FT/ABS]** ESRB EU NBFI Risk Monitor 2025 (https://www.esrb.europa.eu/pub/nbfi/html/esrb.nbfi202509.en.html, Section 2.1, end-2023 data): relative value hedge funds' gross leverage "often exceeding 30 times their NAV"; self-reported CS01 implies "losses of about 12% of NAV for relative value hedge funds" per 100 bp of spread widening (most others lose under 10%). It is a leveraged EU AIF sample, not US credit RV; it settles the "(CHECK)" on 30x in `trend_systematic_credit_industry.md`. IMF GFSR April 2026, ch. 1, Fig. 1.9 and p.14 (https://www.imf.org/-/media/files/publications/gfsr/2026/april/english/ch1.pdf, extracted locally): multistrategy, relative-value and macro funds raised prime-brokerage and repo borrowing sharply; the top 10 hedge funds "now account for more than one-third of the gross" notional; fixed-income-arbitrage fund returns are more tightly tied to financial stress since 2020 (R-squared 0.69 versus 0.26, later sample higher); Treasury-centred. IMF blog, 6 Oct 2026 (https://www.imf.org/en/blogs/articles/2026/10/06/hedge-funds-improve-market-functioning-but-can-also-amplify-stress): gross AUM $13tn, gross notional about $40tn. BoE FSR July 2026 (https://www.bankofengland.co.uk/financial-stability-report/2026/july-2026, first 100,000 characters read): "a relatively high use of leverage by a small number of hedge funds ... pursuing similar trading strategies" in sovereign bonds. No official source on credit-RV crowding found.

## 4. The five must-reads

1. **Duarte, Longstaff, Yu (2007)**, R1: the template for a rule-based RV backtest (fixed volatility target, capital per notional as the honest leverage number, alpha after factors and fees) and the GM hedge-leg story. Read with Avino-Lazar (R3) as its out-of-sample answer.
2. **Ben Dor et al. (2007) DTS, with the pairs-hedging chapters (R6, R7)**: the only public experiment on how to size the two legs of a credit pair, including its crisis re-run and the near-default exception.
3. **Asquith, Au, Covert, Pathak (2013)** (R11): the mechanics and cost of shorting a corporate bond. Read the NBER version for Section 2 (locate, collateral, rebate, recall) and the downgrade and bankruptcy figures.
4. **Collin-Dufresne, Goldstein, Martin (2001)** (R9), with Schaefer-Strebulaev (2008) (R8): what the residual of a credit model is, and which hedge ratios survive. It is the discipline behind "isolate the idio".
5. **BIS Quarterly Review, June 2005, box on the GM and Ford downgrade** (R22), with Mitchell-Pulvino (2012) (R23): a primary account of RV pairs failing together. Next five if space allows: Kapadia-Pu (R4), Bai-Collin-Dufresne (R17), Nashikkar-Pedersen (R12), Choi-Shachar (R20), Haesen et al. (R10).

## 5. Mechanics in plain language, with worked numbers

All prices, spreads and sizes below are illustrative inputs; the arithmetic was run by script. The pod holds $10m market value of bond L and shorts $15m of S. Spread duration (SD) is 4.5 for both; spreads are L 180 bp, S 120 bp; the index spread is 100 bp.

### 5.1 How a cash corporate bond is actually shorted

You borrow the exact bond from an owner, sell it, and must return the same bond later. Source is R11 unless stated.
- **Locate and borrow.** The bond must be located (three days allowed), through a custodian or agent lender; in a pod the prime broker does it and, per Man, publishes daily availability and fee feeds (R15).
- **Collateral and fee.** You post 102% cash collateral, marked daily, and earn a rebate on it. The fee is the market cash rate minus the rebate (20 bp fee, 100 bp cash rate: 80 bp rebate; a negative rebate means you pay). You also owe every coupon.
- **Recall.** The loan is "on demand" and rolls nightly. If the lender recalls, you re-borrow elsewhere or buy back; 31.2% of loans shrank before closing.
- **Cost.** Small on average (mean 33 bp, median 18 bp, 2004-2007), flat near 30 bp until about 70% of inventory is on loan, then above 10 bp per further 10%; it jumps with distress (downgrade 38.4 to 52.3 bp; bankruptcy 173 bp before, 245 bp after).
- **For the pod.** The best short ideas from an RSSG seat (distress, downgrade, weak documents) are where fee, recall and "cannot find it" bite: the fee is a function of the signal. Nashikkar-Pedersen (R12): high shorting cost goes with bonds rich to CDS.
- **Data.** No public bond short-interest tape; Rule 10c-1a reporting is delayed to 28 Sep 2028 (R16); vendor data are a lower bound (R14). EquiLend FY2025 (balances +22%, fees -12%) is an average, not a name.
- **Worked number.** Short $15m of S at a 35 bp fee: $15.3m collateral, $52.5k a year, or 52.5 bp on the $10m long. At 85% on loan the Asquith slope gives above about 45 bp; at 245 bp (bankruptcy) it is $367.5k a year.

### 5.2 When CDS, CDX or an ETF is the real short leg

| Short leg | What it is really short | Basis or mismatch introduced | Practical limit |
| :--- | :--- | :--- | :--- |
| Borrowed cash bond | the exact bond | none on the bond; fee, recall, specials (R11, R12) | availability in the names you want most; no public tape |
| Single-name CDS (buy protection) | the issuer's reference obligation family | CDS-bond basis: moves with bond illiquidity, funding, counterparty and the bond lending fee (R17, R18); cheapest-to-deliver and manufactured-event risk (Ch 24) | only about 100 US names trade regularly (R15); single-name notional $375.7bn in H1 2026 against 33 times that in indices (existing dossier, ISDA) |
| CDX / iTraxx | an index of issuers | intrinsic basis to duration-weighted constituents, near zero normally and 60 bp in 2008-09, and a jump each roll (existing dossier, Bai-Shachar); beta mismatch to a single name | deep and 99% cleared; issuer-specific default not hedged |
| Credit ETF (HYG, LQD) | a wrapper on a portfolio | premium or discount to NAV; March 2020 tracking error above 200 bp against 0.7 bp on average (existing dossier, Todorov, BIS); basket mismatch | easy to short; the basis is worst when you most need the hedge |
| Credit futures (IBHY, IBIG, CME) | index close built from evaluated prices | futures-index basis; end-of-day price distortion reported near 19 bp (existing dossier, Rapp et al., search summary only) | open interest about $3.8bn; margins 2.46% / 1.21% against CDX HY 8.12% / 5.34% |
| Same issuer's equity | the junior claim | unstable hedge ratio (R1, R3); GM stock +18% on 4 May 2005 (R22) | equity is liquid; the correlation is not |

Rule of thumb from the sources: IG names with CDS are shorted in CDS; single-name HY without CDS in borrowed bonds, accepting recall risk; beta in the index, future or ETF; a name in distress in neither (borrow 173 to 245 bp, CDS already prices default), so the junior security or equity is the vehicle. Worked number: Z-spread 120 bp, CDS 110 bp (basis -10 bp), fee 35 bp: the cash short costs 155 bp and the CDS short 110 bp, or $232.5k against $165k a year on $15m, a $67.5k saving bought with ISDA, clearing and auction risk. Speculative trading concentrates in CDS (R21).

### 5.3 Four hedge-ratio rulers, one pair

Pair: long L, short S as above. The ratio is how many dollars of S to short per dollar of L.

| Ruler | How it sizes | Short per $1 long | P&L for +10 bp market spread (% of long) | Spread carry (bp a year on long) |
| :--- | :--- | :--- | :--- | :--- |
| Notional or spread duration | same spread duration, same dollars | 1.00 | -0.27% | +60 |
| DTS | 4.5 x 180 over 4.5 x 120 | 1.50 | 0.00% | 0 |
| Empirical beta | trailing bp-betas, noisy at 1.5 and 0.7 (true 1.8 and 1.2) | 2.14 | +0.35% | -77 |
| Factor-model residual | regress each leg on market, sector, rating, size and momentum; size so net factor exposure is zero | model-dependent | zero on the factors in the model, by construction | model-dependent |

Reading it. (1) The spread-duration hedge leaves the pair long the market: +60 bp of carry pays for a 0.27% loss per 10 bp of widening, so 22 bp of widening wipes out a year's carry. (2) DTS is neutral in relative terms and carries nothing when spread durations match (Ben Dor, printed p.198); it is the right prior (R7). (3) A short-window beta can over-hedge: the pair turns short the market and pays 77 bp a year to be so. (4) The factor-model ruler generalises DTS to sector, rating and equity-driven moves; its failure mode is R9: omit a common factor and a factor bet shows up as idio. Ben Dor's ranking: DTS lowest volatility and systematic share (12.6%); beta lowest correlation but 18.9% systematic; all worse in 2007-2008, worst for financials. Practical blend, already in Ch 8: DTS as prior, shrink a rolling beta toward it ((1 + beta) / 2 cut the ratio's standard deviation from 0.7 to 0.2).

### 5.4 Jump-to-default asymmetry in a pair

A bond pair is two jump processes, not one. Inputs: L at 95, S at 98, recovery 40 for both; intensity about spread over (1 - recovery): L 3.0% a year, S 2.0%.
- If L defaults: the $10m long loses 57.9%, **$5.79m**.
- If S defaults: the $15m short gains 59.2%, **$8.88m**.
- Expected jump P&L is nearly zero: 2.0% x $8.88m - 3.0% x $5.79m = +$3.9k a year, because spread times duration tracks the loss rate. DTS-neutral is roughly jump-neutral in expectation.
- The shape is not neutral: about 3% odds of losing $5.79m on the leg you like, 2% odds of gaining $8.88m. A 30 bp convergence thesis is worth 4.5 x 30 bp x $10m = $135k a year, so one default on L erases 43 years of alpha; on $50m of allocated capital it is 11.6%, past the 5% and 7.5% lines press-reported for Millennium (existing dossier, life S14; not firm disclosure, not general to pods).
- **Near default the ratio flips.** If L slides to 60 at 2,000 bp (SD 3), DTS says short $11.1 of S per $1 of L; L's jump is 33% and S's 59%. Ben Dor: size on market value, and hedge L's default only with L's own capital structure (R7).
- **Correlation** helps only when both default (net +$3.1m here); a default wave also brings recalls, margin calls and wider fees at once (R22).
- **In CDS form** the short pays one minus the auction price (60 cents here); the jump hedge is cleaner on the same issuer than across issuers (Ch 24).

### 5.5 Carry and funding

With matched spread durations a DTS-neutral pair has about zero spread carry, so expected P&L is convergence minus frictions. Example: carry 0; fee -$52.5k a year; long-leg financing at 40 bp over cash on $10m, -$40k; two legs of half-spread amortised over a 3-month hold, say -$60k a year; against a 30 bp thesis worth +$135k. Net about -$17.5k before the pod's capital charge (all frictions illustrative except the fee mechanics). Sources: (a) repo haircuts on corporate bonds reflect lender policy, not bond risk (R16); (b) funding tightens exactly when bases widen (R19, R20, R23); (c) leverage multiplies it: relative value funds at gross leverage often above 30 times NAV lose 12% of NAV per 100 bp of widening (R24); quant credit long-short typically starts at 4 to 5 times (R15).

### 5.6 Attributing a pair's P&L

One month, same pair, hedge ratio 1.5. Market widened 8% in relative terms; L's true relative beta was 1.1 and S's 0.9 (so DTS leaves a residue); L tightened a further 6 bp on its own, S widened a further 2 bp.

| Line | $ | How computed |
| :--- | :--- | :--- |
| Market, long leg | -71,280 | -4.5 x (180 x 1.1 x 8% = 15.84 bp) x $10m |
| Market, short leg | +58,320 | +4.5 x (120 x 0.9 x 8% = 8.64 bp) x $15m |
| **Market leak (hedge residue)** | **-12,960** | the DTS ratio ignored betas of 1.1 and 0.9 |
| Idio, long | +27,000 | 4.5 x 6 bp x $10m |
| Idio, short | +13,500 | 4.5 x 2 bp x $15m |
| **Idio** | **+40,500** | the thesis |
| Spread carry | 0 | 180 bp x $10m less 120 bp x $15m, per month |
| Borrow fee | -4,375 | 35 bp x $15m / 12 |
| Financing | -3,333 | 40 bp x $10m / 12 |
| Transaction cost | -5,000 | illustrative amortised half-spread |
| Rates residue | -1,500 | illustrative duration mismatch |
| **Net** | **+13,332** | |

Read: idio is 3.0 times the net; leak and frictions took 67% of it. Proposed Ch 8-C convention: idio P&L, leak (market, rates, basis), friction (fee, funding, cost) and capture ratio (net over idio). Compute the market line with betas fixed at the start of the day; an ex post regression hides the hedge error. Benchmark: 9% to 26% of a DTS-hedged pair's variance is systematic in R7.

## 6. Evidence table

| date | fact | source |
| :--- | :--- | :--- |
| 2001-2004 | Capital-structure arbitrage, 261 obligors, 135,759 daily CDS spreads: equal-weighted mean 0.705% a month, Sharpe 1.203; capital $66.25 per $100 notional for 10% volatility versus $8.45 for swap-spread arbitrage | R1, Duarte-Longstaff-Yu (2007), Tables 1 and 5 |
| 4-5 May 2005 | GM stock +18% on Kerkorian's offer (4 May); S&P cut GM and Ford to junk and bond and CDS spreads widened (5 May); convertible-arbitrage buyers "lost money on both legs" | R22, BIS Quarterly Review, Jun 2005, p. 6 |
| early 2005 to May 2005 | Long-correlation trade (sell iTraxx Europe equity-tranche protection, buy index protection) earned 300-400 bp; default correlation then "fell sharply"; mezzanine and index moved in opposite directions | R22, BIS, Jun 2005, p. 6 |
| 2005-2009 | Classical capital-structure arbitrage had negative Sharpe ratios, pre-crisis and in-crisis; CSFB/Tremont FI Arbitrage index -4.84% a year, volatility 12.82%, Sharpe -0.38, skewness -3.1 | R3, Avino-Lazar (2012) |
| 2003-2006 | 392 same-industry CDS pairs, hedge-ratio standard deviation 0.0 (notional), 0.3 (DTS), 1.3 (24-week beta); systematic variance share 18.6%, 12.6%, 18.9% | R7, Ben Dor et al., Table 8.1 |
| 2003-2006 | DTS ratio predicts next-period beta with R-squared 0.36 (26 weeks) and 0.50 (52 weeks) against 0.19 and 0.23 for prior empirical beta | R7, Table 8.3 |
| 2007-2008 | All hedges less effective: pair P&L volatility 159.1 (notional), 117.5 (DTS), 137.3 (beta) bp a week; ex-financials 73.0, 57.7, 66.0 | R7, Table 10.3 |
| Jul 2002 | Issuer-matched DTS utility steepener lost 4.73% in one month on defaults; information ratio 0.2 with the month, 0.8 without | R7, chapter 9, printed p.220 |
| 2004-2007 | Corporate-bond borrow cost, mean 33 bp and median 18 bp; 19 and 13 bp by 2007; flat near 30 bp until 70% of inventory is on loan, then above 10 bp per extra 10% | R11, Asquith et al. |
| 2004-2007 | Bond borrow cost around bankruptcies: 173 bp in the 30 days before, 245 bp after; full-letter downgrade: 38.4 bp before, 52.3 bp after | R11 |
| 2004-2007 | Shorting about 19.1% of corporate bond trades (authors' estimate); 102% cash collateral; loans on demand; 31.2% of loans shrank before closing | R11 |
| 2007 | About 3% of corporate bonds on loan; fees highest for low-rated bonds around downgrades; high shorting cost goes with bond rich to CDS | R12, Nashikkar-Pedersen |
| 2020 | Bond short selling predicts bond returns, mainly in high yield and after Lehman; no evidence of private information in the earlier agent-lender data | R13 versus R11 |
| 2008-2009 | Hedge funds unwinding basis trades were the main driver of the negative CDS-bond basis; dealer inventories rose | R20, Choi-Shachar, NY Fed SR 650 |
| 2022 | Quant long-short credit leverage "starts at 4-5x"; prime brokers publish daily borrow availability and fees; about 100 US CDS names trade regularly | R15, Man (2022), pp. 10-11 |
| 2025 | Corporate bond lending: revenue $463m (+8%), balances +22%, fees -12% | R16, EquiLend via Mondo Visione, Jan 2026 |
| end-2023 (pub. 2025) | Relative value hedge funds: gross leverage often above 30 times NAV; +100 bp credit spreads costs about 12% of NAV | R24, ESRB NBFI Monitor 2025 |
| Apr 2026 | Top 10 hedge funds hold over one-third of gross notional; multistrategy and relative-value borrowing up sharply | R24, IMF GFSR Apr 2026, Fig. 1.9 |
| 2020-03 | Bond ETF tracking error above 200 bp against 0.7 bp on average | Existing dossier trend_electronification_pt_etf_liquidity (Todorov, BIS) |

## 7. Book placement

Chapters follow `book_src`; the thread plan is `state/rv_thread_plan.md`.

- **Ch 3 (RSSG bridge).** The RSSG instinct as intra-capital-structure RV; GM 2005 as a pair whose hedge leg failed; document and process knowledge as the idio a quant cannot replicate. R1, R22.
- **Ch 4-B (bond math).** DTS hedge ratio, zero carry of a DTS-neutral pair, the four-ruler table (5.3). R6, R7.
- **Ch 5 (distributions).** Pair P&L as two jump processes, expected-zero but skewed (5.4); default correlation. R7, R22.
- **Ch 6, 6-B, 23 (structural models, cross-asset).** Capital-structure arbitrage as the textbook pair; equity delta works, rate delta does not; GM 2005; negative Sharpe 2005-2009. R1-R4, R8.
- **Ch 7, 7-B (ML, panels).** Predict the residual, not the spread; the latent common factor as the reason for clustered inference; short interest as a feature. R9, R10, R13, R14.
- **Ch 8 (canonical home).** Four rulers, near-default rule, idio definition with the R9 warning, idio-share metric; reproduce the Ben Dor comparison and rerun it on recent data (Section 8). R6-R10.
- **Ch 8-B (risk model).** JTD limit per pair, leak budget, pod stop arithmetic (11.6% example), gross and net, crowding monitor; BIS 2005 as the case. R22-R24.
- **Ch 8-C (explain).** The attribution table (5.6): idio, leak, friction, capture ratio. R11.
- **Ch 9, 10, 11 (factors, trend, HY).** Long-short books pay borrow and recall on the short side (add to the cost curve, papers dossier B14); residual momentum; low-rated shorts cost most. R10-R13.
- **Ch 12-B to 16 (restructuring).** Bankruptcy-window borrow of 173 to 245 bp makes bond shorts dear when the process is the thesis; fulcrum-versus-junior pairs use CDS or equity as the short. R11, R12.
- **Ch 18, 19, 27 (execution).** Two-leg legging risk; derivatives gapped while cash adjusted. R22.
- **Ch 20 (ETF arbitrage).** ETF as short leg: basis, 200 bp stress tracking error, DTS-matched basket (5.2).
- **Ch 22 (regulation).** Reg SHO scope, Rule 10c-1a delay, haircut policy. R16.
- **Ch 24 (basis).** Basis as the short leg; borrow fee and basis as one variable; CDS versus cash short cost. R12, R17-R21.
- **Ch 28, App B, App A.** Crowding and capacity (30x, 12% NAV, concentration); data atlas for borrow (EquiLend, S&P, FIS Astec), CDS, CDX; notation for h, idio share, capture ratio. R14-R16, R24.

Not covered here (other sources needed): Ch 25 weak-docs pairs, Ch 26 LLM screening, Ch 21 loan versus bond, Ch 17 public proxy versus private marks.

## 8. Open items and unverified claims

- **Read at abstract level only:** Yu (2006) full text; Kapadia-Pu; Schaefer-Strebulaev; Collin-Dufresne et al.; Hendershott et al.; Garleanu-Pedersen; Bai-Collin-Dufresne; Oehmke-Zawadowski. The DTS original and the 2026 "Twenty Years of DTS" were not read.
- **Search-summary only, not opened:** Hilscher-Pollet-Wilson; D'Amico-Kurakula-Lee; the Haesen et al. numbers; a 2012 paper attributed to Del Viva, possibly the EFMA 2012 "Corporate bond hedging" paper (its PDF returned HTTP 503), reporting that very few bonds have equity hedge ratios within 10 points of the model; Risk.net's March 2020 bases of -186 bp (IG) and -401 bp (HY) from JPMorgan data (secondary; leads for Ch 24); a Jarrow-Li-Ye paper on statistical arbitrage in CDS spreads that I could not open (HTTP 403) and could not confirm in Crossref.
- **Not found:** a peer-reviewed pairs test on cash corporate bonds; current (2020s) public borrow-fee levels for HY and IG; any public data on credit-RV pod crowding or P&L; confirmation that corporate bonds are in Rule 10c-1a; the lender behind Asquith et al. (the NBER note carries a State Street disclaimer).
- **Conflicts to keep visible:** Asquith et al. (no private information in bond shorts) versus Hendershott et al. (predictive, in high yield); Yu's positive Sharpe (2001-2004) versus Avino-Lazar's negative (2005-2009); ESRB's 30x is an EU AIF sample.
- **Suggested replication (spec for Ch 8):** rebuild the Ben Dor 392-pair test on 2022-2026 CDX IG constituents (or TRACE bonds) with the same four hedges, adding a factor-residual ruler and a borrow-fee scenario from EquiLend or S&P data; report volatility, systematic share and ratio stability, and test whether residuals of the pairs are cross-correlated.
- **Leads for Ch 28, surfaced by search and not opened:** Fed Financial Stability Report, May 2026 (leverage section) and the FEDS Note of 22 Jun 2026 on hedge funds' Treasury exposures; ECB Financial Stability Review, May 2026 (relative value leverage ratios around 25); FSB reports of 2023 and Feb 2026 on leverage and repo. All Treasury-centred.

## Sources (URLs verified this session)

Fetched and read this session (page text, or PDF text extracted locally):
- https://www.johnhcochrane.com/s/Duarte_Longstaff_Yu_nickelsRFS.pdf (redirects to a static1.squarespace.com copy; read in full)
- https://rpc.cfainstitute.org/research/financial-analysts-journal/2006/how-profitable-is-capital-structure-arbitrage
- https://mpra.ub.uni-muenchen.de/42850/2/MPRA_paper_42850.pdf
- https://ideas.repec.org/a/eee/jfinec/v105y2012i3p542-564.html
- https://ideas.repec.org/a/eee/phsmap/v612y2023ics0378437123000444.html
- https://www.robeco.com/en-sg/insights/2024/08/duration-times-spread-a-measure-of-spread-exposure-in-credit-portfolios
- https://ideas.repec.org/a/eee/jfinec/v90y2008i1p1-19.html
- https://ideas.repec.org/a/bla/jfinan/v56y2001i6p2177-2207.html
- https://robeco.com/en-uk/insights/2012/08/residual-equity-momentum-for-corporate-bonds
- https://nber.org/papers/w16282 and https://www.nber.org/system/files/working_papers/w16282/w16282.pdf (full text); https://dspace.mit.edu/handle/1721.1/73466
- https://www.aqr.com/Insights/Research/Working-Paper/Corporate-Bond-Specialness
- https://ideas.repec.org/a/cup/jfinqa/v55y2020i1p77-115_3.html
- https://mondovisione.com/media-and-resources/news/equilend-securities-lending-revenue-soars-to-all-time-highs-of-153-billion-202616/
- https://www.hedgeweek.com/global-securities-lending-revenue-hits-record-15-3bn-in-2025/
- https://www.nber.org/papers/w21502
- https://www.sec.gov/rules/2004/07/short-sales (first 100,000 characters)
- https://www.dechert.com/knowledge/onpoint/2025/8/sec-extends-compliance-deadlines-for-securities-lending-transpar.html
- https://www.proskauer.com/blog/sec-again-extends-short-sale-and-securities-lending-rules-compliance-deadlines-to-2028-while-it-considers-response-to-court-ruling
- https://ideas.repec.org/a/bla/finmgt/v48y2019i2p417-439.html
- https://ideas.repec.org/a/cup/jfinqa/v46y2011i03p627-656_00.html
- https://www.nber.org/papers/w16777
- https://www.newyorkfed.org/medialibrary/media/research/staff_reports/sr650.html (returned the PDF)
- https://ideas.repec.org/a/oup/rfinst/v30y2017i1p80-119..html
- https://ideas.repec.org/a/eee/jfinec/v104y2012i3p469-490.html
- https://www.bis.org/publications/qr-200506.pdf
- https://www.esrb.europa.eu/pub/nbfi/html/esrb.nbfi202509.en.html (first 100,000 characters)
- https://www.imf.org/-/media/files/publications/gfsr/2026/april/english/ch1.pdf
- https://www.imf.org/en/blogs/articles/2026/10/06/hedge-funds-improve-market-functioning-but-can-also-amplify-stress
- https://www.bankofengland.co.uk/financial-stability-report/2026/july-2026 (first 100,000 characters)
- Crossref API (api.crossref.org/works), used for volume, page and DOI checks: R2, R6 and its 2026 sequel, R8, R4, R10 and Gebhardt et al., R16 (Hu et al.), R23 records.
- Local shelf (not URLs): `Ben_Dor_Quantitative_Credit_Portfolio_Management` PDF pp. 228-237, 246, 250, 270-274; `Man_Quantitative_Credit_Alpha_Early_Mover_2022` pp. 10-11; `Dynkin_Systematic_Investing_in_Credit` pp. 793-797; Ch 8 and 24 of `book_src`.

Surfaced by search, not opened (do not cite as read): Hilscher-Pollet-Wilson (https://resolve.cambridge.org/core/journals/journal-of-financial-and-quantitative-analysis/article/abs/are-credit-default-swaps-a-sideshow-evidence-that-information-flows-from-equity-to-cds-markets/F7CCD2FFB20AAEACE1E093D12EEF7A31); D'Amico-Kurakula-Lee (https://chicagofed.org/publications/working-papers/2020/2020-14); the FDIC working version of Yu (https://www.fdic.gov/analysis/cfr/2005/apr/fyu.pdf); OFR Hedge Fund Monitor leverage charts (https://www.financialresearch.gov/hedge-fund-monitor/categories/leverage/; the page lists charts but gave no values).

<!-- STATUS: COMPLETE -->
