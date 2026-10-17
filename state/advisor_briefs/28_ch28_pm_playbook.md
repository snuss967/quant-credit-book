# Advisor Brief — Chapter 28: What a Desk Head / Senior PM Must Know to Extract Maximum Alpha

Prepared by the Fable advisor, Edition 1 (2026-10-17). Target file: `book_src/28_ch28_pm_playbook.md`. Spine: `Paleologo_Advanced_Portfolio_Management` (sizing, alpha vs. beta, PM process), with `Ben_Dor_Quantitative_Credit_Portfolio_Management` (DTS, LCS, liquidity cost) and `Dynkin_Systematic_Investing_in_Credit` (horizons, turnover, capacity). Anything not verified in-session is marked CHECK. Section headings below are the required ten; each is appended as drafted.

## 1. Thesis and the "aha"

## 2. Section outline (7,000–10,000 words)

## 3. Derivation skeletons

## 4. Code spec and sanity check

## 5. Source map (book_id p.N; verbatim quotes ≤60 words)

All quotes below were read from `state/pdf_pages/` this session. Page numbers are PDF pages as `tools/pdf_search.py` reports them.

**Paleologo (the spine)**

- Paleologo_Advanced_Portfolio_Management p.88 (why Sharpe, why leverage): "Return on GMV is performance relative to a capital budget. But the real scarce resource is not capital; it is risk." → Opens §28.2: the desk head allocates *risk*, not dollars; dollars are a consequence.
- Paleologo p.91 (sizing objectives): "If your goal were to maximize expected returns and your expected returns forecasts were accurate, the investment decision would be straightforward: the portfolio would hold a single stock, the one with highest expected returns. Those who follow this rule need to read this book the most, but probably don't have enough money to buy it." → Joke that teaches; the credit version is "hold the one CCC with the fattest spread."
- Paleologo p.92 (sizing rules): "The realized Sharpe Ratio is consistently higher for risk parity and for the proportional ratio than for the mean-variance." → Why the chapter prefers proportional/risk-parity sizing of IDO ideas over full MV in credit (ill-conditioned covariances, Ch 8).
- Paleologo p.100, Insight 6.2: "Using target positions that are proportional to the forecasted expected returns of a stock beats other common methods." → Also Procedure 6.3 (p.101): regress $\alpha$ on loadings $B$, standardize residuals, size to GMV — the factor-neutralization step that makes "IDO or it didn't happen" operational.
- Paleologo p.148 (the fundamental law in hit-rate form): "(Inf. Ratio) = [2 × (hitting probability) − 1] × √(252 × (effective number of stocks))" → Base equation for §28.3 breadth; credit needs the *issuer-clustered* effective number.
- Paleologo p.149 (breadth): "The power of diversification is great. It is not a skill: it is a skill multiplier." and "Beyond a certain threshold, coverage and breadth increase at the expense of accuracy." → The team-design section: adding ex-RSSG analysts adds breadth without diluting hit rate only if their hit rate matches the PM's.
- Paleologo p.150, Procedure 8.1: "H = sum[%GMV²(stock i)] … (effective number of stocks) = 1/H" → The Herfindahl breadth; we extend to issuer/sector/factor clustering.
- Paleologo p.150 (measurement noise): "The standard error associated to this yearly hitting rate is 0.33%. This is a very large value, comparable to the 'edge' of 0.5%." → Why one year of pod P&L cannot distinguish skill from noise; feeds the drawdown-rule critique.
- Paleologo p.163 (stop-loss taxonomy): "Stop-and-Shutdown … Stop-and-Restart … Within the same firm, a PM with a long track record is stopped and then restarted, while a new one is not given the benefit of the doubt." and "There is the stop-loss that you have, and the one you don't know you have."
- Paleologo p.164 (PM option): "Stop-loss rules are a partial hedge for the PM call option. … it is in the interest of the manager to run with the highest possible volatility, independently of her skill." → The incentive derivation in §28.6.
- Paleologo p.166 (opportunity cost): "Stop-loss exists to ensure survival of a firm, not to improve the performance of a strategy. There is a price to pay."
- Paleologo p.167 (simulation design): "a two-threshold one (cut capital in half when loss reaches (x/2)%, and liquidate at x% loss). To approximate heavy-tailed returns … returns distribution in the simulation is not Gaussian, but a Student with 6 degrees of freedom." and "The price of safety is higher for lower-Sharpe PMs than higher-Sharpe ones." → The two-threshold rule is exactly the reported multi-manager 5%/7.5% convention (see §6).
- Paleologo p.174 (leverage identity): "(return) = s × σ/√n × L (10.1)" and "L ≥ √n/σ × (min return)/s (10.2)".
- Paleologo p.175 (the κ fudge): "in large drawdown events, it is always the case that the realized volatility is a multiple of the predicted volatility; investors experience two, three, even six sigma events. … we … assume that realized portfolio volatility is inflated by a positive factor κ … with values between 1 (if we really believe in models) and 3 (if we are skeptical)."
- Paleologo p.176 (leverage ceiling): "L ≤ √n/σ × (max d.d.%)/(−κF⁻¹(p_loss) − s) (10.3) … In practice, we want to set −κF⁻¹(p_loss) between 4 and 6." → In credit, $\sigma$ is spread vol × DTS, $n$ is issuer-effective breadth, and the drawdown must include the LVaR add-on.
- Paleologo p.178 (idio share): "When the percentage idio p_idio increases, it works its magic on both sides of the equation: the lower admissible leverage decreases and the highest admissible leverage increases."
- Paleologo p.131 (multi-PM platforms): "If you are managing a multi-PM hedge fund … You may still decide to maintain a strict autonomy among PMs, essentially managing the platform as a fund of funds. The hidden cost in this choice is the opportunity cost of not adopting more advanced techniques."
- Paleologo p.199–202 (optimal event trading): alpha curve $\alpha(t)$ known on $[0,T]$ with quadratic costs; "Optimal Policy with Long-Horizon Liquidation" (p.202). → Skeleton for trading into a known catalyst (lender call, maturity wall date) with alpha decay.

**Ben Dor (liquidity cost, the "5×")**

- Ben_Dor_Quantitative_Credit_Portfolio_Management p.112 (LCS definition): "We define LCS as the bond's OASD multiplied by this spread. Consequently, a bond's LCS can be interpreted as the cost, in percentage points, of immediately executing a roundtrip transaction." and "Over this time period, the LCS for the IG Index ranged from 0.59% to 3.40%." (Jan 2007–Jun 2009) and "the index's LCS values had already doubled between June 2007 and September 2007".
- Ben Dor p.112 (sell the illiquid first?): "a strategy of selling illiquid bonds at the beginning of a liquidity crisis may be more productive than selling liquid bonds first." → The liquidation-ordering question in §28.5; contrast with the 2020 evidence that investors sold the liquid bonds first (O'Hara–Zhou).
- Ben Dor p.113 (dispersion): "at the beginning of 2007 the LCS for the HY Index was approximately 40 bps greater than that for the IG Index. By the end of 2008, however, the gap had widened to more than 400 bps." and "Not only did the mean LCS score increase to 3.40%, but the standard deviation of the distribution increased sharply." → The 0.59% → 3.40% move is a 5.8× widening of round-trip cost: the TOC's "bid-ask widens 5×" is the 2007–2008 IG index experience, not a hypothetical.
- Ben Dor p.128 (LCS vs volume): "LCS is negatively related to a bond's trading volume."

**Man Group 2022 (transaction costs by size)**

- Man_Quantitative_Credit_Alpha_Early_Mover_2022 p.19: "We cannot overstate the importance of transaction cost and liquidity modelling for quant credit participants" and "Momentum tends to have the highest turnover of any factor approach while both Size and Quality see the least churn." and the "if filled" trades line.
- Man 2022 p.20: "the bid-ask spread for AAA-rated corporate bonds was estimated at 25bps, while for CCC-rated bonds it was 180bps" (Chen, Lesmond & Wei 2007) and "while bid-offer spreads gap out in times of crisis like February/March 2020, levels swiftly return to normal".
- Man 2022 p.21: "TC = Inside Market Spread + Slippage + Spread Calibration".
- Man 2022 p.22: charts of HY transaction costs by ticket size (\$1mm, 5mm, 10mm, 15mm, 20mm), y-axis 0.5–4.0%, 2004–Feb 2021; IG 0.4–1.8%. → Cost is a function of *size*: the LVaR must be size-dependent, not a bond-level constant.

**Dynkin (horizons and turnover)**

- Dynkin_Systematic_Investing_in_Credit p.520: "limited liquidity in credit markets makes high-turnover strategies less practical and necessitates long investment horizons consistent with fundamental views." → Opening of the horizon-allocation section.
- Dynkin p.610: "Investment horizons along with turnover and transaction costs all need to be considered to assess the practi[cality]".
- Dynkin ch. 18 (p.690 ff.): "Integrating Systematic Strategies into Credit Portfolio Construction", with LCS (p.702), turnover buffers (p.707) and turnover budgets (p.715). [Pages to be quoted below once read.]

**Bolder / Bohn–Stein (tail measures and concentration)**

- Bolder_Credit_Risk_Modelling p.393: argues "for the use of expected shortfall as one's economic-capital measure"; p.391 shows "top-ten contributors to both VaR and expected shortfall". → Risk contributions by issuer for the JTD budget.
- Bohn_Stein_Active_Credit_Portfolio_Management p.489: on the "circumstances under which an investor or counterparty can be rewarded for taking on concentrations of default risk."

## 6. Research dossier (dated, sourced; CHECK = unconfirmed)

### 6.1 Evidence table (appended as found)

| Date | Fact / number | Source (verified this session unless CHECK) |
|---|---|---|
| Jan 2007–Jun 2009 | Barclays LCS for the US IG index ranged 0.59% to 3.40% (round-trip cost in price points); IG LCS doubled between Jun and Sep 2007; mean 0.59% (Jan 2007) → 3.40% (Nov 2008) → 1.97% (Jun 2009). HY–IG LCS gap ≈40 bp in early 2007 → >400 bp by end-2008. | Shelf: Ben Dor p.112–113 |
| Feb–Mar 2020 | IG transaction costs rose "from around 30 basis points … in February to nearly 90 basis points in mid-March" (≈3×); IG block trades "only 24 bps in February, had jumped to over 150 bps by March 23" (>6×); customer-to-customer trade costs reached 165 bp mid-March. Bond mutual fund net outflows in March exceeded \$250bn (~5% of AUM); short-term IG funds lost 8% of assets. | Sharpe & Zhou, FEDS Note, Oct 7 2020, https://www.federalreserve.gov/econres/notes/feds-notes/the-corporate-bond-market-crises-and-the-government-response-20201007.html |
| Mar 17 / Mar 23 / Apr 9 2020 | PDCF announced Mar 17 (operations Mar 20); SMCCF announced Mar 23 with \$10bn Treasury equity, leverage up to 10:1; Apr 9 expansion to \$25bn equity, HY leverage 7:1, fallen angels downgraded after Mar 22 eligible. SMCCF bought ETFs from May 12 and bonds from Jun 16; by Jul 31 it had used just over \$12bn of a \$250bn allotment. Bonds just under the 5-year cutoff tightened an extra 21 bp in the week after the SMCCF announcement. | Same FEDS Note |
| Mar 2020 | Customers' willingness to pay for immediacy rose by about 200 bp per dollar traded at the peak; customers shifted from risky-principal to slower agency trades; dealers' marginal costs rose and did not fully recede. | Kargar, Lester, Lindsay, Liu, Weill & Zúñiga, *Corporate Bond Liquidity During the COVID-19 Crisis*, NBER WP 27355 (Jun 2020, rev. May 2021; RFS 2021 version adds Goldstein), https://www.nber.org/papers/w27355 |
| Reported (WSJ via eFC, Dec 5 2025) | Millennium PMs "who lose 5% of allocated capital typically have it halved. If they lose another 2.5%, they're usually fired." Two large index-rebalancing pods (20+ people each) were reported down \$900m in Q1 2025 (Bloomberg) and "hundreds of millions" in Nov 2025 (Business Insider); one pod reportedly made \$3bn in 2020. Millennium declined to comment. | eFinancialCareers, Dec 5 2025, https://www.efinancialcareers.com/news/pratik-madhvani-glen-scheinberg — **CHECK**: secondary reporting of a WSJ report; mark "commonly reported" in text |
| 2024 data (pub. Oct 2025) | Multi-manager pass-through expense ratios ranged 0.87%–12.99%, mean 5.93%, median 4.53%; variable compensation is generally charged on top of a fund-level incentive fee (netting risk). | Cambridge Associates, *Hedge Fund Discretionary Expense Summary 2024* (Oct 2025), PDF title seen in search only — **CHECK** numbers at source before quoting |
| 2007 (cited 2022) | Chen, Lesmond & Wei (2007) bid-ask estimates: AAA 25 bp, CCC 180 bp; Man says both "markedly tighter" by 2022; HY 20-day average bid-ask chart (Bloomberg) spikes in Feb/Mar 2020 and normalizes within months. | Shelf: Man 2022 p.20 |
| 2004–Feb 2021 | Man's modelled HY full transaction cost by ticket (\$1mm to \$20mm) spans roughly 0.5%–4.0% of price over the period, IG 0.4%–1.8%: cost rises with ticket size and spikes in 2008–09 and 2020. | Shelf: Man 2022 p.22 (chart; read values approximate) |
| 31 Jul 2019 | Barclays computes LCS for >20,000 fixed income securities (~\$50trn outstanding); bond-level LCS history for US IG/HY index constituents since Jan 2007, Pan-European since May 2010. LCS for spread-quoted bonds = bid–offer spread × spread duration; for price-quoted bonds = (offer − bid)/bid. | Shelf: Dynkin p.702 |
| — | Turnover buffers (do not trade bonds with intermediate signal values) vs. turnover budgets (hard monthly turnover cap plus explicit exposure constraints); buffers risk "large rebalancing events" and make exposure control hard. | Shelf: Dynkin p.707, p.715 |
| — | Rating-based stop-loss rules "lead to lower portfolio returns" across all rating thresholds; the volatility/drawdown reduction is "much less than proportional to the decline in return"; downgraded bonds outperform rating peers; prefer rating as an *entry* rule, not a liquidation rule, or set the threshold far from the portfolio's target rating (e.g., A portfolio, stop at B). | Shelf: Dynkin p.419 |
| — | "Unlike equities, however, debt has no upside potential to offset the potential for large losses … there are no practical circumstances under which an investor or counterparty can be rewarded for taking on concentrations of default risk." | Shelf: Bohn–Stein p.489 |
| — | In a 100-obligor one-factor t-threshold portfolio, "One half of the total risk can … be allocated to the 16 largest obligors"; VaR contributions need ~100m simulations for \$2–5 confidence bands while ES contributions are "certainly less than \$1"; ES ranking ≠ VaR ranking; VaR-matched ES (Bluhm et al. 2003) as a pragmatic middle ground, with $\alpha^* \approx 0.9997$ in the example. | Shelf: Bolder p.391, p.393 |
| Jan 5 2026 | 2025 returns: Millennium +10.5%, Citadel +10.2%, ExodusPoint +18%, Schonfeld flagship +12.5%, Bridgewater Pure Alpha +33%; S&P 500 +16.5%. Millennium and Citadel "lost money early in 2025 amid the US trade war, then recovered." | Hedgeweek (relaying FT), Jan 5 2026, https://www.hedgeweek.com/millennium-and-citadel-post-double-digit-2025-gains-but-lag-smaller-hedge-funds/ |
| Mar 2026 | Iran-war shock: multi-strats gave back Jan–Feb gains. Reported: Balyasny −4.3% in March (−3.8% Q1); Millennium −1.2% to −1.3% in March (YTD ≈ +1%); Citadel Wellington −1.9% in March (YTD ≈ +1%), Citadel equities +0.7%; Millennium and Point72 together lost ≈\$1.5bn "during the worst stretch"; Millennium +≈2.3% in early April after a ceasefire. Losses attributed to "a rapid unwind of consensus macro and relative-value trades that many pods across multiple firms were simultaneously positioned in." | Bloomberg (Apr 2 2026, via BGov headline), Goldman Sachs-sourced figures via nasdaq.com/quiverquant; hedgeco.net Apr 2026 — **CHECK**: secondary; figures vary by outlet; fetch primary before quoting exact numbers |
| ~2025 | Goldman Sachs executive: multi-strategy managers attracted ≈\$500bn of new assets in a year (~25% growth) while sector headcount rose ~10–11%. 2024 headcount: Millennium +260 net investment staff, Citadel +62, Point72 +186, ExodusPoint +32 PMs, Balyasny −13. | Hedgeweek "Multi-strats may need to accelerate PM hiring as assets surge"; eFinancialCareers "biggest multistrategy hedge funds" — **CHECK** dates at source |
| Dec 9–16 2015 | Third Avenue Focused Credit Fund: board adopted a liquidation plan Dec 9 2015 and suspended redemptions effective Dec 10; investors had pulled ≈\$1.1bn in 2015 to Dec 9, leaving ≈\$789m; SEC issued a temporary order under §22(e)(3) of the Investment Company Act on Dec 16 2015 (IC-31943); the SEC said institutional holders would otherwise have redeemed first "to the detriment of retail investors"; the unwind took roughly a year. | SEC, Investment Company Act Release No. 31943, https://www.sec.gov/files/rules/ic/2015/ic-31943.pdf ; Boston Globe Dec 16 2015 (search snippets; fetch IC-31943 to confirm figures) |
| 1998/1999 | Bangia, Diebold, Schuermann & Stroughair, *Modeling Liquidity Risk, With Implications for Traditional Market Risk Measurement and Management*, NYU Stern/Wharton FIC WP 99-06: separates exogenous liquidity risk (bid-ask distribution, outside the trader's control) from endogenous (position-size-driven); LVaR adds a spread-based cost of liquidation to parametric VaR. | https://ideas.repec.org/p/wop/pennin/99-06.html ; PDF https://archive.nyu.edu/bitstream/2451/27135/2/wpa99062.pdf (formula to be confirmed below) |
| 2019 / 2026 | Kelly with jumps: Garivaltis, *Game-Theoretic Optimal Portfolios for Jump Diffusions*, Games 10(1) 2019, arXiv:1812.04603 (first-order condition for the growth-optimal fraction with a jump term); Bermin & Holm, *Kelly trading when asset prices have jumps*, Decisions in Economics and Finance (2026): Merton's continuous approximation "can largely underestimate the risk of bankruptcy (when high leverage is applied)"; discrepancy small for jumps <25%. | https://arxiv.org/abs/1812.04603 (verified listing); Bermin–Holm seen as PDF link only — **CHECK** citation details |
| 2023 (effective) | Basel FRTB MAR33 (internal models, effective 1 Jan 2023) assigns regulatory liquidity horizons per risk factor; the ES is scaled by $\sqrt{LH_j/10}$ and summed in quadrature across horizon buckets. Credit-spread IG/HY horizons to be quoted from the chapter text. | https://www.bis.org/basel_framework/chapter/MAR/33.htm (landing page confirmed; paragraph text pending) |

## 7. Case studies

## 8. Humor beats (canon cast)

## 9. Resource-graph candidates

## 10. Exploratory-space notes

