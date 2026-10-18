# Case Autopsy: Capital-Structure Arbitrage Pain Trades (Carvana 2023, SVB March 2023, Wolfspeed 2025)

Dossier for Ch 23 (cross-asset convexity and vol surface), Ch 6 (Merton and intensity models) and Ch 15 (event-driven M&A and CoC); possible feed for Ch 13-B (Wolfspeed Docket Diary). Compiled 2026-10-18. No CUSIPs are used. Source tags in square brackets map to the Sources list. CHECK marks a figure that is secondary, vendor-derived, or not confirmed in a primary document this session. Vendor and press price quotes are indicative, not TRACE prints.

## 0. Why these three, and the one-paragraph thesis

(pending)

## 1. Carvana (2022-2023): exchange terms, the equity squeeze, the cap-arb losses

### 1.1 Dated timeline
(pending)

### 1.2 Instruments and tranches
(pending)

### 1.3 Price, spread and recovery paths
(pending)

### 1.4 Legal and structural mechanics
(pending)

### 1.5 Players
(pending)

## 2. SVB Financial Group (March 2023): the holdco note path

### 2.1 Dated timeline
(pending)

### 2.2 Instruments and tranches
(pending)

### 2.3 Price, spread and recovery paths
(pending)

### 2.4 Legal and structural mechanics
(pending)

### 2.5 Players
(pending)

## 3. Wolfspeed (2025): one distribution, many strikes

### 3.1 Dated timeline
(pending)

### 3.2 Instruments and tranches
(pending)

### 3.3 Price, spread and recovery paths
(pending)

### 3.4 Legal and structural mechanics
(pending)

### 3.5 Players
(pending)

## 4. Outcome and later rulings

(pending)

## 5. What a systematic desk could have observed beforehand, and how it would have flagged and traded it

(pending)

## 6. Which model assumptions broke

(pending)

## 7. What the RSSG banker saw that the quant missed

(pending)

## Sources

(pending)

## Book placement

(pending)

<!-- RAW FACTS LOG (working notes; to be consolidated into the sections above and then deleted before the COMPLETE marker) -->
### RAW C1: Carvana exchange, primary (Carvana 10-Q for quarter ended 30 Sep 2023, fetched this session from sec.gov/Archives/edgar/data/1690820/000169082023000323/cvna-20230930.htm)
- Pre-exchange unsecured stack at 31 Dec 2022 ($mm): 5.625% due 1 Oct 2025 = 500; 5.500% due 15 Apr 2027 = 600; 5.875% due 1 Oct 2028 = 600; 4.875% due 1 Sep 2029 = 750; 10.250% due 1 May 2030 = 3,275; total 5,725. Remaining at 30 Sep 2023: 98 / 32 / 22 / 26 / 27 = 205 total.
- Tendered/accepted ($mm, % of outstanding): 2025 402 (80.3%); 2027 568 (94.7%); 2028 578 (96.3%); 2029 724 (96.6%); 2030 3,248 (99.2%); total 5,520 (96.4% of 5,725). Of which cash tender (2025s only) $341mm = 85.0% of par on $402mm; the other $5.1bn exchanged into three new secured series.
- New senior secured notes issued (par $mm): 2028s due 1 Dec 2028 = 981 (Yr1 PIK 12%; Yr2 cash/PIK toggle 9%/12%; then 9% cash); 2030s due 1 Jun 2030 = 1,471 (13% PIK; 11%/13%; then 9%); 2031s due 1 Jun 2031 = 1,741 (14% PIK; 14% PIK in Yr 2; then 9%). Total 4,193. Interest semi-annual 15 Feb and 15 Aug from 15 Feb 2024. Allocation of old paper to new: 2027 old 568 -> 436 new (76.8%); 2028 old 578 -> 385 (66.6%); 2029 old 724 -> 470 (64.9%); 2030 old 3,248 -> 2,902 (89.3%). (Computed by me from the table: new par / tendered par.) Note the 2030s old (10.25% coupon) got the highest recovery of face: 89.3 cents of secured par vs 65-77 for the 4.875-5.875% coupons.
- $146mm cash paid for accrued and unpaid interest; $66mm unamortized debt issuance costs written off; gain on debt extinguishment $878mm; $40mm premium added to principal of secured notes; estimated $1.4bn CODI for tax.
- Collateral: second-priority liens on certain assets pledged to the Ally Parties under the Floor Plan Facility, and first-priority liens on certain other assets identified in the indentures. Guaranteed by domestic restricted subsidiaries other than inventory/finance-receivable/securitization subsidiaries. ADESA and subsidiaries designated unrestricted under the unsecured indentures in March 2023. Redemption: make-whole before specified dates; up to 35% of 2028s and 2030s at 109% with equity proceeds; 101 CoC put. Exit consents stripped substantially all restrictive covenants and certain EoDs from the unsecured indentures (supplemental indentures 30 Aug 2023).
- Equity-side: Transaction Support Agreement dated 17 Jul 2023 per 10-Q (Garcia Parties committed to buy up to $126mm of equity); 8-K ex 99.1 press release dated 19 Jul 2023 announcing >90% (about $5.2bn) of unsecured holders signed. Garcia Parties bought 3.4mm Class A Units + 2.7mm Class B shares on 18 Aug 2023 at $46.31 per Class A share equivalent (= weighted avg ATM price), $126mm, proceeds used to partially fund the cash tender. ATM programme of up to $1.0bn or 35mm shares (distribution agreement 19 Jul 2023); Q3 2023 sold 7.2mm shares at weighted-average $46.94, gross $336mm, net $327mm. Apr 2022 public offering: 15.625mm Class A at $80, net $1.2bn (Garcia Parties bought 5.4mm of them).
- Advisors named in 19 Jul 2023 release (WebFetch of ex 99.1): Moelis (financial) and Kirkland & Ellis (legal) for Carvana; PJT Partners (financial) and White & Case (legal) for the noteholder group; Apollo, PIMCO and Ares named as participating in / working with the ad hoc group (CHECK exact role language). Release: eliminates >83% of 2025 and 2027 unsecured maturities; total debt reduced by >$1.2bn; cash interest down >$430mm per year for next two years.
### RAW C2: CVNA equity path (vendor data: Yahoo Finance chart API daily bars, fetched this session; vendor series is split-adjusted for a 5:1 split dated 8 May 2026, so I multiplied by 5 to recover as-traded prices; CHECK against exchange data before publishing exact decimals)
- Peak close 10 Aug 2021 $370.10 (intraday high $376.83). 31 Dec 2021 $231.79. 26 Apr 2022 (day of $80 offering) $70.49. 2022 low close $3.72 (27 Dec 2022); intraday low $3.55 on 7 Dec 2022 (volume 118.5mm shares that day). Peak close to low close = -99.0%. 30 Dec 2022 $4.74.
- 2023 closes: 3 Jan $4.63; 6 Jan $4.41 (2023 low close); 31 Jan $10.17; 28 Feb $9.42; 31 Mar $9.79; 28 Apr $6.94; 31 May $12.92; 30 Jun $25.92; 18 Jul $39.80; 19 Jul $55.80 (+40.2% day of the announcement); 20 Jul $46.73; 18 Aug $39.21 (Garcia purchase priced at $46.31, the ATM weighted average); 31 Aug $50.35; 1 Sep $50.85 (exchange settlement); 29 Sep $41.98; 31 Oct $27.00; 30 Nov $31.32; 19 Dec $59.80 (2023 high close); 29 Dec $52.94. 30 Dec 2022 to 29 Dec 2023: +1,017% (4.74 -> 52.94). 31 Dec 2024 $203.36.
- Computed by me from vendor bars; a file of the full daily series is in the session scratchpad only (not in the repo).
### RAW C3: Carvana failed spring-2023 exchange and TSA terms (primary: Carvana 8-Ks and prospectus supplement, fetched this session from sec.gov/Archives/edgar/data/1690820/: 000119312523076322/d820769dex992.htm [22 Mar 2023 release]; 000169082023000122 [19 Apr]; 000169082023000172 [17 May]; 000169082023000176 [1 Jun 8-K]; 000169082023000243 [1-2 Aug 8-K]; 000119312523189218/d723413d424b5.htm [ATM prospectus supplement])
- 22 Mar 2023 "Project Coupe" private exchange offers (name appears in the filename of the SEC exhibit; treat as CHECK for naming): up to $1.0bn (the "Maximum Amount") of new 9.0%/12.0% cash/PIK toggle Senior Secured SECOND LIEN Notes due 2028; minimum participation condition $500mm; acceptance priority 1 to 5. Total consideration per $1,000 (incl. $20 early premium): 5.625% 2025s 808.75 (priority 1); 10.250% 2030s 793.75 (2); 5.500% 2027s 658.75 (3); 5.875% 2028s 646.25 (4); 4.875% 2029s 632.50 (5). The release said the offer was "at a premium to current trading prices". Second-lien on Ally collateral (Ally floor plan holds first lien; payments on new notes from Ally collateral blocked if an Ally default notice is outstanding). Before launch Carvana designated ADESA US Auction, LLC as an UNRESTRICTED subsidiary (released ADESA subsidiaries from guarantees of the existing notes; ADESA would not guarantee the new notes) and planned to contribute the finance platform IP to a new FinCo (Carvana FAC, LLC), "permitted under its existing debt arrangements". This is the J.Crew/unrestricted-sub playbook applied to a bond stack before any exchange.
- 19 Apr 2023: expiry extended to 3 May; 2025s consideration raised to 838.75 (858.75 total). 3 May: extended again. 17 May: extended to 1 Jun with withdrawal deadline moved to 24 May. 2 Jun 2023 announcement (8-K dated 1 Jun): offers EXPIRED AND TERMINATED because the $500mm minimum participation was not met; all tendered notes returned. The unsecured holders (ad hoc group) refused a $1.0bn second-lien swap at 63-81 cents of face-equivalent and waited. 2025s: even with 83.9 offered.
- 17 Jul 2023: Transaction Support Agreement among Carvana Co., Carvana Group, the Garcia Parties and an ad hoc group >90% of existing notes (about $5.2bn per press release). TSA terms (prospectus supplement): (i) new equity of at least $350mm gross (Class A and/or LLC units); (ii) exchange into three tranches of senior secured notes due 2028/2030/2031 of up to $4.376bn; (iii) cash tender of certain 2025 notes; (iv) consent solicitations; (v) Garcia Parties buy pro rata portion of new equity, not to exceed $126mm, commitment terminating when $700mm gross raised. TSA termination triggers: exchange not launched by 2 Aug 2023; new notes not issued; 2025 cash repurchase not made within 5 business days of close; ATM or underwritten offering not launched by 8:00am ET on the 3rd business day after Q2 results; <$350mm gross equity by the 20th business day after exchange launch; Garcia failure; no closing by 30 Sep 2023. First Amendment to TSA dated 1 Aug 2023 changed consideration allocation for the cash tender.
- 2 Aug 2023 launch: exchange for up to $4.275bn of three secured tranches: up to $1.0bn 9.0%/12.0% cash/PIK due 2028; up to $1.5bn 11.0%/13.0% due 2030; up to $1.775bn 9.0%/14.0% due 2031; PLUS cash tender for any and all 2025s for up to $425.0mm at 85.0% ($850 per $1,000) plus accrued; exchange limited to 2027/2028/2029/2030 notes; consent solicitation for exit consents (majority per series). Closed 1 Sep 2023 (see C1).
- Fair-value-to-carrying proxy for the whole unsecured/secured senior note stack (Level 2 quoted prices, per 10-K/10-Qs; computed ratios are mine): 31 Dec 2021 FV 2,411 / carrying 2,422 = 99.5%; 31 Dec 2022 2,533 / 5,649 = 44.8% (about 44.2% of 5,725 par); 31 Mar 2023 3,040 / 5,652 = 53.8%; 30 Jun 2023 4,186 / 5,655 = 74.0%; 30 Sep 2023 3,444 / 4,432 = 77.7% (new stack incl. PIK accrual); 31 Dec 2023 3,866 / 4,566 = 84.7%.
- Equity vs credit over 2023 (equity close from C2): 30 Dec 2022 $4.74 and stack at 44.8%; 31 Mar $9.79 / 53.8%; 30 Jun $25.92 / 74.0%; 29 Sep $41.98 / 77.7%; 29 Dec $52.94 / 84.7%. So equity +1,017% while the debt mark rose 1.9x: a bond-long / stock-short hedged at a Merton-style ratio lost on the equity leg by a factor of roughly 5.
- Financials (10-Q Q3 2023): Q3 2023 net income $741mm incl. $878mm gain on debt extinguishment; Adjusted EBITDA Q3'23 $148mm (5.3% margin) vs $(186)mm Q3'22; 9M'23 Adj EBITDA $279mm vs $(750)mm; 9M interest expense $467mm vs $333mm; Q3 revenue $2,773mm vs $3,386mm. Floor Plan Facility resized to $1.5bn and extended to 30 Apr 2025 (1 Nov 2023). Finance receivable facilities outstanding $312mm (30 Sep 2023) vs $965mm (31 Dec 2022).
- Press/market colour (secondary): Bloomberg (Eliza Ronalds-Hannon, Carmen Arroyo), 18 Nov 2022 via American Banker ASReport: bonds 37-48 cents, a "collapsing bond stack" (near and 10-year paper at similar prices); newest secured/ADESA-backed bonds largest holders include Apollo, PIMCO, Franklin; Fitch expected default next year; S&P said liquidity lasts through end of 2023. Institutional Investor (Michelle Celarier), 9 Nov 2022: Carvana shares -50% in days after Morgan Stanley's Adam Jonas pulled rating ("might be worth only $1"); stock closed $7.36 that Tuesday, -97% YTD; S3 Partners: Carvana best-performing short of 2022 by % (323.77%), $4.2bn mark-to-market gains; Sosin Partners down >70%. Bloomberg 8 Jun 2023 (via search snippet; not fetched): shorts lost >$1bn, stock +411% YTD, S3 Partners MTM loss $1.04bn, ~56% of free float short (Ortex 54% on 18 Jul 2023).
