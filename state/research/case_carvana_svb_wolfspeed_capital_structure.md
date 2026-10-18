# Case Autopsy: Capital-Structure Arbitrage Pain Trades (Carvana 2023, SVB March 2023, Wolfspeed 2025)

Dossier for Ch 23 (cross-asset convexity and vol surface), Ch 6 (Merton and intensity models), Ch 15 (event-driven M&A and CoC) and Ch 13-B (Wolfspeed Docket Diary). Compiled 2026-10-18. No CUSIPs. Bracket tags map to Sources. CHECK = secondary, vendor-derived or unconfirmed in a primary document; (calc) = my arithmetic from sourced inputs. Vendor and press prices are indicative, not TRACE prints.

## 0. Why these three, and the one-paragraph thesis

Three episodes in which a hedge that was right under the model lost because a document, not a price process, rewrote the equity-credit map. Carvana (2023): the equity was the issuer's funding source, so the "cheap" stock squeezed the credit's own recovery upward. SVB (March 2023): holdco credit was a residual claim on a bank resolution; equity implied volatility sat near its 39 floor until it printed 167 on 10 Mar (52-week high 280). Wolfspeed (2025): a prepackaged plan fixed one pie of new stock and issued instruments struck at about $12.23, $18.35, $20.14 and $23.95, while old shares kept trading at $0.60 to $1.21 against a plan value of about $0.18 to $0.31. The common failure for a Merton or CreditGrades sleeve is to treat equity as exogenous, continuous and fungible with the old security. Each case is a dated transition (TSA, 8-K and receivership, RSA and exchange ratio) that a document parser sees before a price model does.

## 1. Carvana (2022-2023): exchange terms, the equity squeeze, the cap-arb losses

### 1.1 Dated timeline
- 10 Aug 2021: CVNA peak close $370.10 [YF]
- 26 Apr / 9 May 2022: $80 equity offering (15.625mm shares, $1.2bn net); ADESA acquisition closes 9 May [C-10Q3][C-10K23]
- 7-9 Nov 2022: Morgan Stanley's Adam Jonas pulls rating; stock about -50% in days, $7.36 close [II-Nov22]
- 18 Nov 2022: Bonds 37-48 cents; Fitch expects default in 2023; S&P sees liquidity through end-2023 [AB-BBG]
- 27 Dec 2022: Closing low $3.72 (-99.0% from peak, calc) [YF]
- 22 Mar 2023: Offer for up to $1.0bn second-lien toggle notes; ADESA designated unrestricted first [C-8K]
- 2 Jun 2023: Offer terminated: $500mm minimum participation unmet after extensions (19 Apr, 3 May, 17 May) [C-8K]
- 17-19 Jul 2023: Transaction Support Agreement (TSA) with holders of over 90% (about $5.2bn); stock +40.2% to $55.80 [C-8K][C-10Q3][YF]
- 2 Aug / 18 Aug 2023: Exchange launched; Garcia Parties buy $126mm of equity at $46.31 [C-10Q3]
- 1 Sep 2023: Settlement: 96.4% tendered; $878mm gain on extinguishment [C-10Q3]
- 2024: 2028s repurchased at 101.6 to 105 (calc); Section 382 rights plan ended 4 Jun [C-10K25][C-8K]
- 31 Dec 2025: Stock $422.02 as traded (calc from vendor); 2028s gone; debt $4.98bn [C-10K25][YF]
- 14 Aug 2026: $1.66bn Term Loan B at SOFR+225 refinances the 2030 secured notes [C-8K26]

### 1.2 Instruments and tranches
Pre-deal unsecured stack at 31 Dec 2022 ($mm, tranches by coupon and maturity): 5.625% due 1 Oct 2025, 500; 5.500% due 15 Apr 2027, 600; 5.875% due 1 Oct 2028, 600; 4.875% due 1 Sep 2029, 750; 10.250% due 1 May 2030, 3,275; total 5,725. Ally's floor plan sat ahead on inventory.

Tendered 5,520 (96.4%); cash tender of 2025s took 402 for $341mm (85.0 cents). The other 5,118 became three new senior secured series, each old series receiving the same mix of about 23% / 35% / 42% (calc, 10-K table): 2028s (due 1 Dec 2028; 12% PIK year 1, then 9%/12% toggle, then 9% cash) 981; 2030s (1 Jun 2030; 13% PIK, then 11%/13%, then 9%) 1,471; 2031s (1 Jun 2031; 14% PIK, then 14% PIK in year 2, then 9%) 1,741; total 4,193. Face recovered by old series: 2027s 76.8%, 2028s 66.6%, 2029s 64.9%, 2030s 89.3% (calc: new par over tendered par). The 10.25% 2030s, the largest and highest-coupon line, did best because the ratio was set per series, not per priority. Cash paid for accrued interest $146mm; $40mm premium added to principal; estimated $1.4bn cancellation-of-debt income. Collateral: second liens on the Ally floor-plan collateral and first liens on other identified assets; guarantees from domestic restricted subsidiaries except inventory, receivable and securitization subsidiaries. [C-10Q3][C-10K23]

### 1.3 Price, spread and recovery paths
Stack mark = fair value over carrying value of all senior notes (Level 2 quotes in the 10-K and 10-Qs); equity = vendor close. Break-even hedge ratio h* = bond return / equity return since 30 Dec 2022, the short-stock notional (as a fraction of initial bond market value) at which a long-bond, short-stock pair breaks even before carry (calc).

| Date | CVNA close | Equity multiple | Stack mark | Bond return | h* |
|---|---|---|---|---|---|
| 30 Dec 2022 | 4.74 | 1.00 | 44.8 | 0% | n/a |
| 31 Mar 2023 | 9.79 | 2.07 | 53.8 | +20% | 18.9% |
| 30 Jun 2023 | 25.92 | 5.47 | 74.0 | +65% | 14.6% |
| 29 Sep 2023 | 41.98 | 8.86 | 77.7 | +73% | 9.3% |
| 29 Dec 2023 | 52.94 | 11.17 | 84.7 | +89% | 8.8% |

A pair hedged at a delta-style 20% to 50% of bond value lost money in every period; by December the equity leg had lost 2 to 6 times the bond gain (calc). Other marks: unsecured bonds 37 to 48 cents in Nov 2022 [AB-BBG]; the March 2023 second-lien offer paid 63.3 to 80.9 cents per $1,000 of old paper, called a premium to trading, and was declined [C-8K]; the August tender for 2025s paid 85.0; 2028 secured notes were bought back at about 101.6 (2024, open market) and redeemed at about 102.3 (2025) (calc, [C-10K25]). S3 Partners counted $646mm of short losses on 19 Jul 2023 alone and $2.18bn year to date, with 47% of float short [S3-Yahoo]; 2022's best short returned 323.77% [II-Nov22]. No public source quantified bond-long, stock-short losses; that inference is mine.

### 1.4 Legal and structural mechanics
Four mechanics mattered more than the stock price. (1) Unrestricted designation: before the March 2023 offer Carvana designated ADESA US Auction, LLC unrestricted under the unsecured indentures, releasing its guarantees, and planned a FinCo for finance-platform IP: a J.Crew-style asset move on the bond stack, done under existing baskets, disclosed with the offer release [C-8K]. (2) Holdout design: the offer carried a $500mm minimum participation condition and acceptance priority by series; holders coordinated as an ad hoc group (over 90% by the July TSA) and refused, so the minimum failed [C-8K]. (3) Coercion by consent: the August exchange paired a cash tender for 2025s, exit consents stripping covenants and certain defaults from the unsecured indentures (majority per series; supplemental indentures 30 Aug 2023), and a TSA whose termination triggers included less than $350mm gross new equity within 20 business days of launch [C-8K]. (4) Equity as the funding source: a $1.0bn / 35mm-share ATM (19 Jul 2023) sold 7.2mm shares at $46.94 in Q3, and the Garcia Parties' $126mm purchase at $46.31 partly funded the cash tender [C-10Q3]; the TSA made the deal contingent on equity the rally supplied. PIK mechanics: 2031s accreted from 1,741 to 2,269 by Dec 2025 (calc). A Section 382 rights plan (18 Jul 2023) protected tax attributes and was ended 4 Jun 2024 [C-8K].

### 1.5 Players
Company: Carvana Co. and the controlling Garcia Parties. Advisors named in the 19 Jul 2023 release: Moelis (financial) and Kirkland & Ellis (legal) for Carvana; PJT Partners (financial) and White & Case (legal) for the noteholder group; Apollo, PIMCO and Ares named as working with the group (exact role CHECK) [C-8K]. Holders of the newest secured and ADESA-backed paper in Nov 2022 included Apollo, PIMCO and Franklin per Bloomberg (Eliza Ronalds-Hannon, Carmen Arroyo) [AB-BBG]. Floor-plan lender: the Ally Parties. Morgan Stanley's Adam Jonas pulled coverage in Nov 2022; Sosin Partners was reported down more than 70% [II-Nov22]. S3 Partners' Ihor Dusaniwsky supplied the short-interest counts [S3-Yahoo].

## 2. SVB Financial Group (March 2023): the holdco note path

### 2.1 Dated timeline
- Jan 2021 / 2021: Portfolio shifted to held-to-maturity (HTM); $8.8bn reclassified from available-for-sale (AFS) with $132mm of pretax losses [FED-BARR][S-10K]
- 15 Nov 2021: SIVB equity peaks; assets pass $200bn in Dec 2021 [FED-BARR]
- 31 Dec 2022: HTM $91.3bn at cost vs $76.2bn fair value; deposits $173.1bn (down $16.1bn); FHLB advances $15.0bn [S-10K]
- 24 Feb 2023: 10-K filed; 1 Mar: analysts 12 Buy, 11 Hold, 1 Sell [S-10K][FED-BARR]
- 8 Mar 2023: AFS sale ($23.97bn book, $21.45bn proceeds, to Goldman Sachs); $2.25bn raise announced; rating agencies flagged; Silvergate winds down [S-8K][FED-BARR]
- 9 Mar 2023: Stock -60.4% to $106.04; over $40bn of deposits leave [FED-BARR][CA-notice]
- 10 Mar 2023: Stock halted; CDFPI closes the bank, FDIC receiver; offerings terminated [S-8K]
- 12-13 Mar 2023: Treasury/Fed/FDIC statement; a Treasury official says equity and junior holders will be "wiped out" (CHECK); holdco restructuring committee and CRO [FED-BARR][S-8K]
- 17 Mar 2023: Holdco Chapter 11 (S.D.N.Y. 23-10367) [S-8K]
- 25 Apr 2023: FDIC has frozen the holdco's $2bn deposit; 2025 notes 69, 2031 notes 57 [DW-Apr23]
- Jan / 2 Aug 2024: RSA with ad hoc group members (Jan, Davis Polk summary, CHECK); plan confirmed 2 Aug [S-8K24][DP]
- 7 Nov 2024: Plan effective; liquidating trust formed [S-8K24]
- 25 Jun 2025: Judge Glenn dismisses First-Citizens' IP suit [FL]
- Late Aug 2026: N.D. Cal. rejects the trust's $1.71bn claim against the FDIC [AB-Sep26][PYMNTS]

### 2.2 Instruments and tranches
Holdco senior unsecured notes, all one class, issuer SVB Financial Group only, indenture of 20 Sep 2010 with U.S. Bank National Association: 3.50% due Jan 2025, $350mm; 1.800% due Oct 2026, $650mm; 2.100% due May 2028, $500mm; fixed/floating due Apr 2028, $350mm (coupon 4.345% in the 10-K tables, 4.435% in the 10-K narrative and the 22 Mar 2023 8-K, CHECK; floats at compounded SOFR + 1.713% from Apr 2027); 3.125% due Jun 2030, $500mm; 1.800% due Feb 2031, $500mm; 4.570% fixed/floating due Apr 2033, $450mm (SOFR + 1.967% from Apr 2032). Total $3,300mm (calc). Junior layers: Boston Private trust-preferred debentures, about $100mm (Trust II, LIBOR + 1.68%, cumulative) guaranteed by the holdco; five series of preferred stock, $3,646mm carrying (Series A listed as SIVBP). Parent-only balance sheet, 31 Dec 2022: cash $2,258mm; investment in the Bank $15,456mm of $19,679mm total assets (78.5%, calc); long-term debt $3,370mm. Bank-level secured and wholesale funding that ranked ahead of everything the holdco could claim: FHLB advances $15.0bn, repo $525mm, deposits $173.1bn of which 94% uninsured. [S-10K][S-8K]

### 2.3 Price, spread and recovery paths
| Date | Instrument | Mark | Tag |
|---|---|---|---|
| 8 Mar 2023 | SIVB equity close | $267.83 (market cap $15.9bn on 59.2mm shares, calc) | [CA-notice][S-10K] |
| 9 Mar | SIVB equity close | $106.04 (-60.4%) | [CA-notice] |
| 10 Mar premarket | SIVB 30-day implied vol | 167 (52-week range 39 to 280); calls:puts 1.1:1; KBE 33, First Republic 56 | [MR] |
| week of 6 Mar | holdco bonds | "nearly 90 cents" (Reuters summary, CHECK) | |
| 10 Mar close | holdco bonds | 37 to 42 (Bloomberg/Trace summary, CHECK) | |
| 13 Mar | holdco bonds | 47 to 50 (Bloomberg, CHECK) or about 40 (Reuters, CHECK) | |
| 17 Mar | senior holdco bonds | about 60 (summary, CHECK); distressed buyers paid about 30 (WSJ via Axios, CHECK) | |
| 25 Apr | 3.5% 2025 / 1.8% 2031 | 69 / 57 (MarketAxess) | [DW-Apr23] |
| 1 Jul 2024 | 1.8% 2026 | 63.625 (Trace) | [BBG-Randles] |

Four readings. (1) Pre-event, implied vol sat at 39 to 50, market equity covered the $3.3bn of senior notes 4.8 times, and a one-year Merton default probability on holdco inputs is about 1e-7 (calc: asset value $19.3bn, asset vol 33%, rate 4.5%): the diffusion model priced the notes as riskless. (2) The move came from the funding side: over $40bn left on 9 Mar (23% of year-end deposits, calc) and $100bn more was expected on 10 Mar, roughly 85% of the base [FED-BARR]. (3) Dollar prices mislead across tranches: a 1.8% 2031 note is below par before any distress, so compare spreads at a stated recovery; the 12-point 2025-versus-2031 gap in April is a reinstatement bet on one claim class [DW-Apr23]. (4) Bonds bought in the 30s were in the 50s and 60s within weeks and the 2026s at 63.6 in July 2024; the plan paid in units and stock (2.4), so recovery is not closed. The holdco's $1.71bn deposit claim is 52% of the senior notes (calc) and was lost at trial in Aug 2026 (Section 4).

### 2.4 Legal and structural mechanics
(1) Separate legal entities: holdco notes are "recourse only to the Company and ... not guaranteed by the Company's subsidiaries" and rank behind all Bank creditors; the holdco's own cash on deposit at the Bank ($1.71bn at trial) became a claim against the FDIC receivership [S-8K][DW-Apr23]. (2) Resolution regime: the 12 Mar Treasury/Fed/FDIC statement protected depositors, not holdco creditors or shareholders (CHECK the statement text); the 17 Mar filing accelerated all seven notes and the trust-preferred debentures (the receivership itself was already a default under the Boston Private debentures), enforcement stayed [S-8K]. (3) Plan mechanics: the confirmed plan (2 Aug 2024; effective 7 Nov 2024) moved assets to a liquidating trust and made the debtor a subsidiary of MNSN Holdings; senior noteholders took new common stock (Qualified Holders) plus Class A-1 trust units and trustee fees; other unsecured creditors took stock plus Class A-2 units or a 45% cash election (claims above $11mm capped); subordinated debentures took Class A-3 units; preferred took Class C units; common and Section 510(b) claimants nothing; the bank stock was abandoned on 6 Nov 2024 for a worthless-stock deduction [S-8K24]. (4) Tax: the IRS reduced a claim from about $649mm to $43mm in Jul 2024, a gating item for the plan [BBG-Randles]. (5) Offsets: the FDIC said the receivership and holdco claims could be netted [DW-Apr23].

### 2.5 Players
Debtor: CEO Greg Becker signed the 10 and 13 Mar 8-Ks; the restructuring committee of five independent directors hired Centerview (financial), Sullivan & Cromwell (legal, Jim Bromley) and Alvarez & Marsal (William Kosturos as CRO, formerly WaMu's CRO) [S-8K]. Senior noteholder group: Davis Polk (Angela Libby at the second-day hearing) with PJT Partners as financial advisor; a cross-holder group with White & Case; the creditors' committee used Berkeley Research Group, Lazard, Akin Gump and Cole Schotz [S-8K24][DW-Apr23]. Identified holders (WSJ and FT via Debtwire, CHECK): PIMCO, Centerbridge, Davidson Kempner; Appaloosa held bonds and preferred. Counterparties: Goldman Sachs bought the AFS book; General Atlantic committed $500mm of the equity raise [S-8K]. FDIC counsel Derek Baker of Reed Smith [DW-Apr23]. Judges: Martin Glenn (Bankr. S.D.N.Y.), Beth Labson Freeman (N.D. Cal.).

## 3. Wolfspeed (2025): one distribution, many strikes

### 3.1 Dated timeline
- 23 Jun / 5 Jul 2023: $1.25bn Senior Secured Notes due 2030 sold (net $1.149bn); Renesas deposit agreement for up to $2.0bn, drawn $1.0bn, then $0.5bn (27 Feb 2024) and $0.5bn (26 Jun 2024) [W-10K25]
- 11-22 Oct 2024: Amended indenture permits $750mm more; $250mm issued; Renesas deposit amended to allow 15% PIK [W-10K25]
- 9 Dec 2024 / Jan 2025: At-the-market programme set up; 27.79mm shares sold for about $200mm (about $7.20, calc) [W-10K25][W-DS]
- Feb 2025: Company hires J.P. Morgan, Perella Weinberg and Latham; Finance Committee meets over 90 times [W-DS]
- 28 Mar 2025: Out-of-court exchange fails; stock about -50% to $2.59, market cap about $400mm [W-DS]
- 30 Mar-May 2025: Secured ad hoc group's "SSN Framework" becomes the template; Renesas and 2026-convert proposals rejected [W-DS]
- 2 Jun 2025: Interest on 2029 converts not paid; 30-day grace period used [W-10K25]
- 22-23 Jun 2025: Restructuring Support Agreement (RSA); old stock about -33% to about $0.60 [W-8K-RSA][PR-Jun23]
- 27 / 30 Jun 2025: Solicitation begins; prepackaged Chapter 11 filed, S.D. Tex. (Houston) [W-8K-Jul]
- 8 Sep 2025: Confirmation order, day 70 [W-8K-Sep]
- 29 Sep 2025: Plan effective; new stock opens at $18.00, closes $22.10 [W-8K-Exit][YF]
- 29 Jan 2026: CFIUS clears Renesas equity; contingent shares released [W-8K-Jan26]
- 26 Mar 2026: $379mm 1.5-lien convertible and $96.9mm of stock fund a $475.9mm first-lien redemption [W-8K-Mar26]
- 26 May 2026: New stock closes $73.50 (3.3 times the $22.02 plan value, calc) [YF]
- 7 Oct 2026: Conditional $1.5bn U.S. government loan commitment, conditional on equitizing converts [W-8K-Oct26]

### 3.2 Instruments and tranches
Old stack at 29 Jun 2025 ($mm principal): 1.75% convertible notes due 2026, 575 (conversion about $47.32); 0.25% converts due 2028, 750 ($127.22); 1.875% converts due 2029, 1,750 ($118.88); Senior Secured Notes due 2030, 1,521.2 (9.875% plus 2% payable in kind; scheduled to step to 10.875% or 11.875% from 23 Jun 2025 and to 13.875% or 15.875% from 23 Jun 2026; $750mm liquidity covenant from Apr 2025); Renesas deposits, 2,062.0 (unsecured, due 5 Jul 2033, 6% base, 15% when PIK). Total $6,658.2mm; cash and short-term investments $955.4mm, down $1.22bn in the year. [W-10K25]

New stack at 29 Sep 2025 ($mm): New Senior Secured Notes due 2030, 1,259.2 (plus $277.5mm of old notes redeemed at 109.875%); 2.5% Convertible Second-Lien Notes due 2031, 331.4 including the $30.3mm backstop premium (conversion about $12.23); Renesas 2.5% second-lien converts, 203.6 (about $18.35); 7.00%/12.00% second-lien PIK-toggle takeback notes, 296.4; Renesas warrant, 4,943,555 shares at $23.95; 25,840,656 shares issued (24,533,760 to converts, 1,306,896 to old equity), plus 16,852,372 to Renesas and 871,287 more to old equity on CFIUS clearance. In Mar 2026 a 3.5% 1.5-lien convertible (conversion about $20.14) was inserted between the first and second liens. Four strikes (about $12.23, $18.35, $20.14, $23.95) sit around a plan equity value of $22.02 per share (calc, 959.4 / 43.56mm shares). [W-8K-Exit][W-10K26]

### 3.3 Price, spread and recovery paths
| Date | Security | Mark | Tag |
|---|---|---|---|
| Jan 2025 | Old stock, ATM sales | about $7.20 average (calc) | [W-DS] |
| 28 Mar 2025 | Old stock | $2.59 (-50%); market cap about $400mm | [W-DS] |
| 12 months to 29 Jun 2025 | Old stock closing range | $0.41 to $24.99 | [W-10K25] |
| 20-23 Jun 2025 | Old stock | about $0.90, then $0.75 premarket, about $0.60 intraday (-33%), -86% year to date | [PR-Jun23] CHECK |
| 29 Jun 2025 | 2026/2028/2029 converts, fair value over principal | $0.8bn / $3.075bn = 26% (Level 2) | [W-10K25] |
| 29 Jun 2025 | Senior secured notes | $1.3bn / $1.521bn = 85% (Level 3) | [W-10K25] |
| 29 Jun 2025 | Renesas deposits | $0.6bn / $2.062bn = 29% (Level 3) | [W-10K25] |
| 27 Jun 2025 | Plan recovery estimates | secured 86%; converts 25 to 30%; Renesas 27 to 29%; trade 100%; equity 5% (3% if the "Distribution Event") | [W-DS] |
| 15 Sep 2025 | Old stock short interest | 32.6% of float (MarketBeat, vendor, CHECK); 64% was quoted in May 2025 (Benzinga Pro via Webull, CHECK) | |
| 26 Sep 2025 | Old stock close | about $1.21 (one aggregator, CHECK) | |
| 29 Sep 2025 | New stock | open $18.00, low $8.05, close $22.10; plan value $22.02 | [YF][W-10K26] |
| 30 Sep 2025 | New stock | $28.60 (Reuters: +33%) | [YF][RTR] |
| 31 Dec 2025 / 31 Mar 2026 / 29 May 2026 | New stock | $17.41 / $16.32 / $59.28 | [YF] |

Old equity economics (calc): 2,178,190 new shares at about $22 is $48mm for 156.48mm old shares, $0.31 each with the CFIUS shares and $0.18 without; the old stock's market value was about $94mm at $0.60 (2.0 times plan value) and $189mm at $1.21 (3.9 times). The CFIUS-contingent 871,287 shares were worth about $15mm, $0.10 per old share (at the $17.33 Renesas mark). Convert delta was nil: at $2.59 the strikes of $47.32, $118.88 and $127.22 were 18, 46 and 49 times spot, so the notes traded as recovery claims, and their fair-value marks of 26 to 29% sat inside the plan's 25 to 30% eight weeks before the RSA. The surprise was in the equity: a short at $1.21 earned about 75% to 85% over the exchange, a long lost it. No Wolfspeed CDS series or listed-option surface was found (evidence gap; OPRA and ICE data would close it).

### 3.4 Legal and structural mechanics
(1) Order of operations: an out-of-court exchange (March 2025) failed to garner sufficient support (the disclosure statement's words) with a 2026 maturity, a Renesas deposit and three convert issues in the room; the secured group's framework (30 Mar) then set the template and the deal moved in-court as a prepackage with the votes cast before filing [W-DS]. (2) Priority was honoured at the top and bent below: the secured notes were reinstated in substance (new 1L plus a $277.5mm paydown at 109.875%, funded by the rights offering and a sale of MACOM shares), while converts and Renesas, unsecured and pari passu, split the fulcrum in different currencies: stock and second-lien paper for converts, a smaller note, a warrant and 16.85mm shares for Renesas [W-8K-Exit]. (3) The "many strikes" were issued by the plan: two second-lien converts struck at about $12.23 and $18.35, a warrant at $23.95, a later 1.5-lien convert at about $20.14, all against 43.56mm plan shares, plus a Black-Scholes protection clause on the warrant for two years [W-8K-Exit][W-8K-Mar26]. (4) Binary hooks: the Regulatory Trigger Deadline made Renesas's contingent consideration (2.0% of stock, $15mm cash, $15mm takeback notes, a warrant extension) and the equity's 5% versus 3% a digital option on CFIUS clearance, paid out on 29 Jan 2026 [W-8K-Jan26]. (5) Old equity was deemed to reject yet kept 3 to 5% as a negotiated settlement of subordination and other rights; the doctrinal question of an equity "gift" over unpaid seniors was not researched here (CHECK). (6) Backstop economics: $301.1mm of 2L converts offered at 91.3242 of face ($275mm cash), a $30.25mm premium in notes, 40% of the offering reserved to the backstop group (20% to the initial backstop parties, 20% holdback allocation) and only 60% open pro rata to all convert holders [W-DS]. (7) Securities-law exits: new securities issued under Bankruptcy Code Section 1145, and resale S-1s filed within 45 days [W-8K-Exit][W-10K26].

### 3.5 Players
CEO Robert Feurle; Chairman Tom Werner replaced by Anthony M. Abate at emergence. Company advisors: Latham & Watkins, Hunton Andrews Kurth, Perella Weinberg Partners, J.P. Morgan, FTI Consulting, Epiq. Secured group: Paul, Weiss and Moelis. Convertible groups: Ropes & Gray and Ducera (26s/28s/29s); Paul Hastings and Houlihan Lokey (26s only). Renesas: Kirkland & Ellis, PJT Partners (financial) and BofA Securities (structuring); Renesas designee Aris Bolisay joined the board 2 Feb 2026. Government actors: CFIUS (clearance 29 Jan 2026) and the Department of War's Office of Strategic Capital (Oct 2026 commitment letter). Names of the funds in the ad hoc and backstop groups were not found in the documents parsed, so none are given [W-DS][W-8K-Exit].

## 4. Outcome and later rulings

Carvana: the exchange closed on 1 Sep 2023 with 96.4% participation; no court test of the ADESA designation or the exit consents appears in the sources read (CHECK a docket search). The equity went from $3.72 (27 Dec 2022) to $422.02 as traded (31 Dec 2025), the 2028 secured notes were retired at about 101.6 to 105 in 2024 and 2025, and a $1.66bn Term Loan B at SOFR + 225 took out the 2030s in Aug 2026 [C-10K25][C-8K26]. SVB: plan confirmed 2 Aug 2024 and effective 7 Nov 2024 (mostly units and stock, little cash); Judge Glenn dismissed First-Citizens' trademark suit on 25 Jun 2025; and in late Aug 2026 Judge Freeman held after a 12-day bench trial that the trust cannot recover its $1.71bn deposit claim because the holdco's officers "negligently caused billions of dollars in losses by their imprudent investment strategy that favored yield over safety" [S-8K24][FL][AB-Sep26][PYMNTS]. That claim was 52% of the senior notes (calc); whether the trust appeals, and what the notes' final recovery will be, was not found. Wolfspeed: effective 29 Sep 2025, CFIUS clearance 29 Jan 2026, a 1.5-lien refinancing on 26 Mar 2026, and on 7 Oct 2026 a conditional U.S. government loan whose condition is equitizing the converts; no contested ruling was found [W-8K-Exit][W-8K-Jan26][W-8K-Mar26][W-8K-Oct26].

## 5. What a systematic desk could have observed beforehand, and how it would have flagged and traded it

Method: a feature is listed only if it was machine-readable on a stated date from a filing, a vendor field or an exchange series.

| Case | Observable and date | Flag | Trade it implies |
|---|---|---|---|
| Carvana | Dec 2022 stack mark 44.8 vs 99.5 a year earlier; near and 2030 bonds at similar prices (Nov 2022); 8-K of 22 Mar 2023 (unrestricted subsidiary, $500mm minimum, per-series priority); TSA of 17 Jul with a $350mm equity-raise trigger; ATM filed 19 Jul; short interest 47% of float | Liability-management event with a closing condition that depends on the equity price | Long the bonds, but size any equity hedge by scenario, not delta: h* never exceeded 19% in 2023, so the hedge is a long call spread or none; read the TSA as a high-probability deal, not a default probability |
| SVB | 10-K of 24 Feb 2023: unrealised losses $17.7bn vs common equity $12.4bn (143%, calc), 94% uninsured (Fed), deposits -$16.1bn, FHLB advances $15.0bn vs none a year earlier; FINRA short interest rising from Apr 2022; implied vol at its 39 floor | A funding-run candidate before 8 Mar; the 8 Mar 8-K (AFS sale at a 10.5% loss, $2.25bn raise, Silvergate wind-down) is the trigger date | Before: buy 1-3 month puts at 40 to 50 vol (the year's floor was 39), underweight holdco notes as a jump-to-default; after 10 Mar: all tranches share one claim class, so a same-claim pair (long the lowest-priced tranche, short the highest) isolates the reinstatement option |
| Wolfspeed | 10-K Note 9 (26 Aug 2025 filing, marks as of 29 Jun): cash $955mm vs a $750mm first-lien-account covenant and $1.22bn of annual burn (about $305mm a quarter, calc); 2026 convert maturity; 2 Jun 2025 grace-period election; 28 Mar 2025 failed exchange (-50% to $2.59) | A 30-day clock to the RSA's 1 Jul petition deadline, then a document-fixed exchange ratio | Short old equity from the RSA (borrow and recall risk not researched): plan value $0.18 to $0.31 vs $0.60 to $1.21; long the secured paper (86% estimated recovery) or the converts at 26 against a 25 to 30% plan range only with a view on the fulcrum; do not delta-hedge the converts (strikes 18 to 49 times spot) |

Three generic rules. (1) Parse the scoreboard of each 8-K item: 1.01, 1.03, 2.04, 3.02 and 5.01 carry the exchange ratio, the stock share and the dates, and are readable within minutes of filing. (2) When the instrument's payoff is set by a document (an exchange ratio, a TSA trigger, a regulatory-trigger deadline), price it as a digital on the event date, not as an option on a diffusion. (3) Never mark a pair by dollar price across tranches with different coupons; compare spread at a stated recovery, or price per dollar of allowed claim.

## 6. Which model assumptions broke

1. Equity is exogenous (Carvana). The issuer sold 7.2mm shares at $46.94, the TSA required at least $350mm of new equity, and the controlling holder bought $126mm: the equity price was a closing condition of the credit's recovery. 2. A short-stock hedge has bounded loss (Carvana). The bond leg was capped by par while the short was a short call on a stock with 47% of float already short; h* fell from 18.9% to 8.8%. 3. Default is a diffusion crossing a barrier (SVB). A holdco-level Merton PD is about 1e-7 (calc), a bank-level model gives another answer, and both miss a $40bn one-day deposit jump priced by a 39-vol surface; the holdco note is a call on a call, ranked behind depositors, the FHLB and the FDIC. 4. Priority fixes recovery (all three). Carvana's recovery ran from 64.9% to 89.3% of face by series; SVB's tranches shared one claim yet sat 12 points apart; Wolfspeed's secured notes were reinstated in substance (86% plan estimate) while Renesas took 27 to 29% in different paper. Recovery is a negotiated vector, not a scalar. 5. Delta is a hedge ratio (Wolfspeed). Strikes of $47.32 to $127.22 against $2.59 make delta zero; the plan then re-struck at $12.23 to $23.95. 6. A ticker is a security (Wolfspeed). The same symbol went from $1.21 to $22.10, a spurious +1,726% (calc) in a naive return series; the vendor history of the new line starts 29 Sep 2025. 7. The barrier is book debt (Wolfspeed). The effective barrier was a $750mm first-lien-account covenant against $1.22bn of annual burn, not $6.66bn of debt.

## 7. What the RSSG banker saw that the quant missed

The seat that reads the 8-K item list, the signature page and the advisor paragraph first. Carvana: (a) designating ADESA unrestricted before any offer is the tell of a coming liability-management deal, since the asset left the old guarantee package first; (b) a minimum-participation condition and a priority order gave the ad hoc group (over 90%; PJT Partners and White & Case advised it) a veto over price and timing, so the March offer's 63 to 81 cents was a negotiating bid, not a market; (c) the 2030s, 3,275 of 5,725, were the swing block, and their 89.3% recovery shows who the deal was written for; (d) the exchange was gated on an equity raise, so the rally was the transaction. SVB: the banker asks what the holdco owns, not what the bank is worth: $2.26bn of cash, mostly deposited at the Bank and frozen, stubs in SVB Capital and SVB Securities, against $3.3bn of senior notes in one class and an FDIC set-off argument; bonds at 30 to 40 were a bet on one $1.71bn claim, which the trust that pays those holders lost at trial. Wolfspeed: the swing creditor was a customer, Renesas, with a wafer-supply agreement and a CFIUS dependency, which made recovery a digital on a regulator; the RSA calendar (petition by 1 Jul, confirmation within 75 days, effectiveness within four months) fixed the dates; NDAs were released on 28 Mar and re-imposed in late May, the cleansing deck came with the RSA 8-K on 23 Jun, and the 2 Jun grace-period election started a 30-day clock. The quant had the prices; the banker had the calendar, the coalition and the counterparty.

## Sources

All URLs returned HTTP 200 on 2026-10-18 or were read via WebFetch (FindLaw gave curl a 403).

Carvana
- [C-10Q3] Q3 2023 10-Q: https://www.sec.gov/Archives/edgar/data/1690820/000169082023000323/cvna-20230930.htm
- [C-10K23] FY2023 10-K: https://www.sec.gov/Archives/edgar/data/1690820/000169082024000093/cvna-20231231.htm
- [C-10K25] FY2025 10-K: https://www.sec.gov/Archives/edgar/data/1690820/000169082026000009/cvna-20251231.htm
- [C-8K] 22 Mar 2023 release: https://www.sec.gov/Archives/edgar/data/1690820/000119312523076322/d820769dex992.htm ; ATM supplement: https://www.sec.gov/Archives/edgar/data/1690820/000119312523189218/d723413d424b5.htm ; 6 Jun 2024 8-K: https://www.sec.gov/Archives/edgar/data/1690820/000169082024000232/cvna-20240603.htm
- [C-8K26] 14 Aug 2026 8-K: https://www.sec.gov/Archives/edgar/data/1690820/000169082026000059/cvna-20260814.htm
- [S3-Yahoo] S3 Partners via Yahoo Finance, 19 Jul 2023: https://finance.yahoo.com/news/carvana-stock-is-up-1000-this-year-leaving-short-sellers-with-a-2-billion-loss-162312603.html
- [II-Nov22] Michelle Celarier, Institutional Investor, 9 Nov 2022; [AB-BBG] Eliza Ronalds-Hannon and Carmen Arroyo, Bloomberg, 18 Nov 2022, as carried by American Banker: authors and dates recorded in an earlier pass, not re-fetched (no link given).

SVB Financial Group
- [FED-BARR] Review of the Federal Reserve's Supervision and Regulation of SVB, 28 Apr 2023: https://www.federalreserve.gov/publications/files/svb-review-20230428.pdf
- [S-10K] FY2022 10-K: https://www.sec.gov/Archives/edgar/data/719739/000071973923000021/sivb-20221231.htm
- [S-8K] 8-Ks of 8, 10, 13 (two), 14, 17, 22 Mar 2023: https://www.sec.gov/Archives/edgar/data/719739/000119312523064680/d430920d8k.htm , .../000119312523067777/d450664d8k.htm , .../000119312523068535/d404655d8k.htm , .../000119312523070254/d487554d8k.htm , .../000119312523073665/d485308d8k.htm , .../000119312523076760/d487549d8k.htm
- [S-8K24] 8 Nov 2024 8-K and 7 Nov release: https://www.sec.gov/Archives/edgar/data/719739/000119312524254186/d904756d8k.htm , https://www.sec.gov/Archives/edgar/data/719739/000119312524254186/d904756dex993.htm
- [DW-Apr23] Debtwire, 26 Apr 2023: https://ionanalytics.com/insights/debtwire/svb-debt-trading-price-discrepancy/
- [BBG-Randles] Jonathan Randles, Bloomberg, 2 Jul 2024, via Accounting Today: https://accountingtoday.com/articles/svb-financial-bonds-rise-after-600m-cut-to-tax-bill
- [MR] Market Rebellion IV report, 10 Mar 2023: https://marketrebellion.com/news/pre-market-iv-report-march-10-2023 ; SpotGamma, 11 Mar 2023: https://spotgamma.com/silicon-valley-bank-collapse-options-market-reaction/ ; Oaktree 1Q2023: https://www.oaktreecapital.com/insights/insight-commentary/market-commentary/performing-credit-quarterly-1q2023
- [FL] In re SVB Financial Group, Bankr. S.D.N.Y., 25 Jun 2025: https://caselaw.findlaw.com/court/us-ban-crt-s-d-new-yor/117422670.html
- [AB-Sep26] American Banker, 9 Sep 2026: https://www.americanbanker.com/news/fdic-wont-have-to-return-1-71-billion-to-svb-creditors ; [PYMNTS] 31 Aug 2026 (Reuters): https://www.pymnts.com/legal/2026/fdic-prevails-in-1-71-billion-court-case-involving-svb-collapse/
- Search-result summaries only (CHECK, no link): Bloomberg and Reuters bond prices of 13 Mar 2023; WSJ via Axios, 17-18 Mar 2023; class-action notices for the $267.83 and $106.04 closes [CA-notice]; Davis Polk's case summary [DP].

Wolfspeed
- [W-8K-RSA] 23 Jun 2025 8-K and ex 99.1: https://www.sec.gov/Archives/edgar/data/895419/000119312525144083/d937053d8k.htm , https://www.sec.gov/Archives/edgar/data/895419/000119312525144083/d937053dex991.htm
- [W-8K-Jul] 1 Jul 2025 8-K and [W-DS] Disclosure Statement (ex 99.1): https://www.sec.gov/Archives/edgar/data/895419/000119312525153145/d755867d8k.htm , https://www.sec.gov/Archives/edgar/data/895419/000119312525153145/d755867dex991.htm
- [W-8K-Sep] 10 Sep 2025: https://www.sec.gov/Archives/edgar/data/895419/000119312525199310/d36059d8k.htm
- [W-8K-Exit] 29 and 30 Sep 2025: https://www.sec.gov/Archives/edgar/data/895419/000119312525223057/d69265d8k.htm , https://www.sec.gov/Archives/edgar/data/895419/000119312525224251/d22768d8k.htm
- [W-8K-Jan26] 30 Jan 2026: https://www.sec.gov/Archives/edgar/data/895419/000119312526030582/d39825d8k.htm
- [W-8K-Mar26] 19 and 26 Mar 2026: https://www.sec.gov/Archives/edgar/data/895419/000119312526116036/d75349d8k.htm , https://www.sec.gov/Archives/edgar/data/895419/000119312526126483/d916941d8k.htm
- [W-8K-Oct26] 7 Oct 2026: https://www.sec.gov/Archives/edgar/data/895419/000119312526416987/d122407d8k.htm
- [W-10K25] FY2025 10-K: https://www.sec.gov/Archives/edgar/data/895419/000089541925000110/wolf-20250629.htm ; Q1 FY2026 10-Q: https://www.sec.gov/Archives/edgar/data/895419/000089541925000132/wolf-20250928.htm ; [W-10K26] FY2026 10-K: https://www.sec.gov/Archives/edgar/data/895419/000089541926000054/wolf-20260628.htm
- [RTR] Reuters, 30 Sep 2025, via Yahoo Finance: https://finance.yahoo.com/news/wolfspeed-shares-rally-chipmaker-exits-113149062.html
- [PR-Jun23] Finviz (Motley Fool), 23 Jun 2025: https://finviz.com/news/86229/why-wolfspeed-plunged-today ; Asianet Newsable: https://newsable.asianetnews.com/markets/wolfspeed-stock-plunges-premarket-after-confirming-chapter-11-plan-restructuring-retail-stays-pessimistic/articleshow-wfe1z4i

Vendor data and shelf
- [YF] Yahoo Finance chart API daily bars for CVNA and the new WOLF line (vendor, CHECK; no old-WOLF history). Short-interest quotes from search summaries. Shelf: Moyer, Distressed Debt Analysis, pp. 259-266 (capital structure arbitrage); Dynkin et al., Systematic Investing in Credit, pp. 87-91 (Merton hedge ratios).
- Evidence gaps: no TRACE print series, SVBFG or Wolfspeed CDS, or Wolfspeed option surface was obtainable; fund-level holder lists were not found.

## Book placement

Ch 23 is the home (Case Study B SVB, Case Study C Carvana, Wolfspeed exhibit). Add: (a) the Carvana squeeze lens with the 1.3 h* table and a short function returning break-even hedge ratio from two marks; (b) SVB: replace "mid-80s" and flagged marks with the Debtwire pair (69 and 57 on 25 Apr 2023) and the 167 vs 39 implied-vol pair; fix the Docket Diary ($3,279mm is carrying value, principal is $3,300mm [S-8K]; the deposit claim was $1.71bn at trial, earlier "about $2bn"); add the Aug 2026 Freeman ruling; (c) Wolfspeed: replace the "not reconstructed" note with the strike ladder ($12.23, $18.35, $20.14, $23.95) against the $22.02 plan value, and answer Exercise 5 with the parity arithmetic (81.7508 x $22.02 = $1,800 per $1,000 of 2L convert against a 91.3242 purchase price, calc).
Ch 6: §6.4.4 says 86-89% uninsured; $151.5bn / $173.1bn = 87.5% is US offices only, the Fed's 94% includes all, so say which; add a holdco-as-call-on-a-call box (holdco-only Merton PD about 1e-7). §6.10.1 can cite per-series Carvana recoveries (64.9% to 89.3%). Ch 15: the CFIUS "Distribution Event" as a digital (871,287 shares, about $15mm) and the rights offering at 91.3242 with its backstop split. Ch 13-B: Wolfspeed Docket Diary from 3.1 and 3.4; Carvana as a one-paragraph LME cameo. Ch 16: the 0.008352 and 0.013920 stub ratios. Ch 9-B: ticker reuse (+1,726% splice) as a corporate-action filter case. Ch 25: the 4.345% / 4.435% mismatch inside one 10-K; 8-K Items 1.01, 1.03, 2.04, 3.02 as parse targets. Ch 28: scenario-sized hedges and a squeeze kill-switch (short interest above 40% of float plus issuer ATM capacity). App C rows: 14 Aug, 31 Aug and 7 Oct 2026.
New sections justified: "23.9 The hedge that is a short call" (Carvana and Wolfspeed old equity), "6.4.5 Holdco as a call on a call", and a Ch 23 exercise on pricing a document-fixed exchange ratio as a digital. A new chapter is not justified: the three cases fit Chapters 6, 15 and 23.
<!-- STATUS: COMPLETE -->
