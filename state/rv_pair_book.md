# The Pair Book: Ledger

*Running ledger of the fictional pod's pairs (Dov Adler's pod at Vantress Capital Management, a labeled fictional composite; Owen Achterberg's capital-structure pod next door). Design: `state/rv_thread.md` §(d). Every writer who opens, stresses or closes a pair updates its row in the same commit. Positions, prices and P&L are illustrative; issuers, instruments and dated events are real unless marked fictional. Status values: `planned` → `open` (chapter) → `stressed` (chapter) → `closed` (chapter) → `declined`. Columns after Status are filled as chapters are written: the hedge ratio's value at open, the idio share of P&L at the last explain, the capture ratio, and what leaked.*

| ID | Owner | Pair (long / short) | Legs (instrument, descriptive) | Hedge method | Opened in | Stressed in | Closed in | Status | Ratio at open | Idio share | Capture | What leaked |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| PB-01 | Dov | Kestrel Roofing / Halvorsen Packaging (both fictional) | Long $60mm Kestrel 6% senior notes due 2030; short $39mm Halvorsen 7.25% senior unsecured notes due 2029, borrowed via the platform's prime broker | Market-value DTS at inception; CDX HY to trim beta residue | Ch 1-B (written, entry 1B-1) | Ch 5, 8-C, 8-D, 11, 22 | Ch 28 | planned (open in print as 1B-1; renumber) | 0.65 by face | — | — | DTS drift as the short's view paid; exchange jump; borrow recall; fee 50 → 300 bp |
| PB-02 | Owen | Halvorsen secured / Halvorsen unsecured (fictional) | Long $10mm face 7.25% secured notes at 79; short $3.8mm face 6% unsecured notes due 2031 at 55 | Recovery-weighted market value (jump-neutral at recoveries 60 / 5) | Ch 4-C (written, unnumbered box) | Ch 12-B, 12-C, 13 | Ch 16 | planned (open in print; number it) | 0.38 by face | — | — | Attachment points move with the DIP and admin burn |
| PB-03 | Dov | Ford Motor Credit / GM Financial | Long Ford Motor Credit senior unsecured notes (fallen angel, 25 Mar 2020); short GM Financial senior unsecured notes in borrow, beta residue in CDX | DTS; rating-bucket factor left open | Ch 8 | Ch 7-B, 9, 24 | Ch 24 | planned | — | — | — | Rating-bucket factor; index-exclusion timing; basis reverts after the downgrade |
| PB-04 | Owen (replay) | GM CDS / GM stock (2005) | Long 5-year GM CDS protection; short GM common by the CreditGrades delta | Model delta (Duarte–Longstaff–Yu rule) | Ch 6 | Ch 23 | Ch 23 | planned | — | — | — | Both legs lost 4–5 May 2005 |
| PB-05 | Owen (replay) | Carvana bonds / Carvana stock (2022–23) | Long Carvana senior unsecured notes; short Carvana common | Equity delta, resized monthly | Ch 5 | Ch 6 | Ch 14 | planned | — | — | — | The categorical default: the exchange, not the filing |
| PB-06 | Owen (replay) | Serta first lien / Serta second lien (2020) | Long Serta Simmons 2016 first-lien term loan due 2023 (outside holder, no group); short Serta second-lien term loan | Recovery-weighted market value | Ch 3 | Ch 13 | Ch 13-B | planned | — | — | — | Seniority inverted by the 22 Jun 2020 uptier |
| PB-07 | Owen (replay) | Hertz bonds / Hertz stock (2020–21) | Long Hertz senior unsecured notes; short Hertz Global common | Delta from a Merton read of the plan | Ch 6-B | Ch 12-C | Ch 16 | planned | — | — | — | The "worthless" equity's option value; unsecured paid in full |
| PB-08 | Dov | Level 3 secured / Lumen unsecured (2023–24) | Long Level 3 Financing senior secured notes; short Lumen Technologies senior unsecured notes (borrow) | DTS within the issuer family, participation overlay | Ch 13 | Ch 25 | Ch 13-B | planned | — | — | — | Which entity the collateral reaches; the excluded holder's markout |
| PB-09 | Dov | Kroger SMR notes / Kroger non-SMR notes (2023–24) | Long Kroger notes carrying the 101 special mandatory redemption; short matched-duration Kroger notes without it | Same issuer, matched duration | Ch 15 | Ch 15 | Ch 15 | planned | — | — | — | Acquirer-curve duration jump at termination (Dec 2024) |
| PB-10 | Dov | EA CoC-put notes / EA defeasance-article notes (2025–26) | Long EA notes with the change-of-control put; short EA notes governed by the base indenture's defeasance article | Same issuer, matched duration | Ch 15 | Ch 15 | Ch 15 | planned | — | — | — | The defeasance moved the put |
| PB-11 | Dov (replay) | Windstream bonds / Windstream CDS (2017–19) | Long Windstream Services senior notes; buy Windstream CDS protection, par for par, PECS-adjusted | Negative-basis package | Ch 24 | Ch 24, 25 | Ch 24 | planned | — | — | — | Deliverables, successor answer, the 15 Feb 2019 ruling |
| PB-12 | Dov | Hovnanian: declined (2017–18) | No short leg exists once the credit event is manufactured | — | Ch 24 | — | — | declined (planned) | — | — | — | The CDS payoff became a negotiation |
| PB-13 | Dov (replay) | LQD / CDX IG (Mar 2020) | Long LQD; buy on-the-run CDX IG protection, DV01-matched | DV01 with the ETF premium as its own line | Ch 12 | Ch 20 | Ch 20 | planned | — | — | — | Discount to NAV near 5%; basis worst when needed |
| PB-14 | Owen | Altice France secured / Altice France Holding unsecured (20 Mar 2024) | Long Altice France senior secured notes; short Altice France Holding senior unsecured notes (borrow) | Recovery-weighted market value | Ch 18 | Ch 18-B | Ch 18 | planned | — | — | — | Legging: the unsecured gapped before the secured filled |
| PB-15 | Dov | Trinseo loan / Trinseo bonds (2023–26) | Long Trinseo first-lien term loan; short Trinseo senior unsecured notes (verify instruments against Ch 13 §13.7.1) | DTS with CLO forced-sale index covariate | Ch 21 | Ch 21 | Ch 21 | planned | — | — | — | Settlement lag; two holder bases; the double-dip |
| PB-16 | Dov | OBDC / HYG (Nov 2025–Aug 2026) | Long Blue Owl Capital Corp common at a discount to NAV; short HYG | Equity-beta and DTS proxy, both admitted | Ch 17 | Ch 17-B | Ch 17-B | planned | — | — | — | Listed-BDC equity beta; floating rate; the proxy shorts the wrong thing |
| PB-17 | Dov | BKLN / HYG (Apr 2025) | Long BKLN; short HYG, DTS-matched | DTS, rates left open | Ch 21 §21.6 | Ch 20, 21 | Ch 21 | planned | — | — | — | T+N settlement; stale loan marks; JAAA queue |

## Book-level lines (filled by Ch 8 §8.8, 8-B, 8-C, 28 as written)

| Metric | Definition | Where computed | Value |
| :-- | :-- | :-- | :-- |
| Residual correlation $\rho_{\text{resid}}$ | Mean pairwise correlation of the pairs' idio P&L | Ch 8 §8.8 | — |
| Book beta to CDX HY | DTS-weighted, limit ±0.05 of gross | Ch 8-B | — |
| Capture ratio | Net P&L / idio P&L, book level | Ch 8-C, Ch 28 | — |
| Largest JTD, long and short | At risk-model recovery; limit $5mm | Ch 8-B | — |
| Borrow fee, book | Weighted on short market value | Ch 22, 8-D | — |
| Stop distance | Peak-to-trough drawdown vs −3.5 / −5 / −7.5% | Ch 8-B, 28 | — |

<!-- STATUS: COMPLETE -->
