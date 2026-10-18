# Ch 23 App Z editor-note fixes (numbers editor, ed2)

Chapter: book_src/23_ch23_cross_asset_convexity_and_vol_surface.md. Solutions: state/appZ/23_ch23_cross_asset_convexity_and_vol_surface.md. Two notes found, both handled and deleted from the solutions file.

## Note 1 (Z.23.1): "selling hard" at V = 75 with sigma_V constant

- Note: the scene says the vol-targeting overlay "is selling hard" at V = 75, but with constant asset vol it never sells a share; only the weight falls.
- Recomputation (/tmp/ch23_n1.py, Merton F = 70, r = 3%, T = 1, sigma_V = 25%): V = 150/100/75 gives E = 82.07/32.61/11.19, N(d1) = 1.000/0.953/0.699, sigma_E = 45.7/73.0/117.1%. Dollar vol per share sigma_V V N(d1) = 37.5/23.8/13.1, so shares per \$100 of risk capital = 0.267/0.420/0.763 (rises; with rebalancing at the rows through NAV 0.267/0.364/0.603). Target weight 0.10/sigma_E = 21.9 (21.7 at the rounded 46%)/13.7/8.5%, a 61% cut. A buy-and-hold position would be 3.7% of NAV 81.1. The note is right: weight falls, shares bought.
- Ruling: FIXED (note right).
- Chapter edits (§23.1, "Sliding the assets down the table"):
  - "At 75 it is selling hard into a stock whose only news is arithmetic" -> "At 75 its target weight is down by more than half, in a stock whose only news is arithmetic"
  - "How much it sells on the way down is Exercise 1's problem" -> "How much weight it gives up on the way down is Exercise 1's problem"
  - Exercise 1: "compute how much ROBO sells as assets fall from 150 to 75." -> "compute how much ROBO cuts its weight, and whether it sells any shares, as assets fall from 150 to 75."
- Solution: already correct (ROBO never sells a share; weight 21.7% -> 8.5%); NOTE paragraph deleted, no other change.

## Note 2 (Z.23.5): Wolfspeed half cannot be built as series; stock \$2.70 vs chapter \$2.59

- Note: dossier records no TRACE series, CDS or option surface; only datable convert points are "near 60" (about 28 Mar 2025, secondary, CHECK) and 26% of principal on 29 Jun (10-K); the secondary source gives the stock at \$2.70 against the chapter's \$2.59.
- Checks: the dossier (case_carvana_svb_wolfspeed_capital_structure.md §3.3 and its evidence-gap line) confirms no TRACE, CDS or option series ("OPRA and ICE data would close it"). The \$2.59 close on 28 Mar 2025 is tagged [W-DS], the company's Disclosure Statement (SEC exhibit); the \$2.70 appears only in case_lmt_private_and_european_2024_2026.md as a TipRanks item tagged "secondary, CHECK". Strike ratios in the case note (47.32/2.59 = 18.3, 127.22/2.59 = 49.1) are consistent with \$2.59. Recomputed the solution's CG inputs with the Listing 23.1 code (/tmp/ch23_n2.py, /tmp/ch23_n2c.py): F_ps = 6,658.2/156.48 = 42.55; at \$2.59, \$2.70 the one-year ghost is 54.6%, 53.6%.
- Ruling, price: NOTE WRONG on \$2.59 vs \$2.70. The chapter's \$2.59 stands (primary source; the \$2.70 is a CHECK-tagged secondary). No edit.
- Ruling, series: SOFTENED (note right). Exercise 5 said the series could be rebuilt "from public data", which the sources do not support. Chapter edit (Exercise 5):
  - "from public data, and say which flag fired first." -> "from whatever public data you can find (we found no free bond-price, CDS or option-surface history for the name), and say which flag fired first."
- Solution edits (Z.23.5, Wolfspeed). The note said the solution labels its inputs as assumptions; it did not clearly, and its CG ranges did not reproduce at the stated R = 27% (they match R of about 29-30%). Recomputed with the book's own code, sigma_E 80-120%, R = 27%:
  - one-year spread at \$7.20: 3,692-5,080bp (was "3,600-4,900"); ghost 24.5% (25% stands);
  - one-year spread at \$2.59: 9,404-9,997bp (was "9,100-9,600"); ghost 54.6% (55% stands);
  - convert floor: 87.1 at 16.4% for a 1 May 2026 maturity (T = 1.093 from 28 Mar 2025) reproduces "about 87"; flat-hazard spread implied by a price of 60 at R = 27%: 5,320bp ("about 5,200" was R = 25%); CG at the same 1.09-year tenor: 8,656-9,246bp; z = -0.385 to -0.425. The 1 May 2026 maturity date is not in the repo's sources, so the solution now labels it an assumption; likewise the 85/16.4% secured mark is a 29 June 10-K figure standing in for March.
  - Old -> new: "(16.4% at 85) give about 87, against a market near 60." -> "(assumed: a 1 May 2026 maturity, and the secured notes' 10-K mark of 85 on 29 June, a yield of 16.4%, standing in for the March curve): the 2026s' cash flows give about 87, against a market near 60 around 28 March (a secondary report)."
  - "CG with $\sigma_E$ at 80-120% and $R = 27\%$ (the plan range) ... 3,600-4,900bp ... 9,100-9,600bp." -> "CG with $\sigma_E$ assumed at 80-120% and $R$ assumed at 27% (inside the plan's 25-30% range for the converts) ... 3,700-5,100bp ... 9,400-10,000bp (8,700-9,200bp at the converts' own 1.09-year tenor)."
  - "The converts at 60 imply about 5,200bp, so $z \approx -0.43$ to $-0.46$." -> "The converts at 60 imply about 5,300bp (flat hazard to maturity, $R = 27\%$), so $z \approx -0.39$ to $-0.42$ at the same tenor."
  - Answer paragraph: "on by 28 March 2025 at the latest:" -> "on by 28 March 2025 at the latest, on a secondary report:"; "$z$ ... about $-0.43$ to $-0.46$" -> "$-0.39$ to $-0.42$"; "The put floor cannot be rebuilt from free data." -> "These are single dated points under stated assumptions, not series: no free bond-price, CDS or option-surface history for Wolfspeed was found, so the put floor cannot be rebuilt."
  - |z| stays below Yu's lowest threshold of 0.5, so the "points the wrong way (buy the stock)" reading is unchanged.
- NOTE paragraph deleted. state/appZ/_editor_notes.md (an aggregate of notes) was not touched.

<!-- STATUS: COMPLETE -->
