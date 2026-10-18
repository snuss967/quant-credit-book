# Verification Report, Edition 2 (U2): Chapter 23

Chapter: `book_src/23_ch23_cross_asset_convexity_and_vol_surface.md` (815 lines; was 515 at commit 9ac1c37). Revision log STATUS: COMPLETE confirmed before starting. Verified 2026-10-18 against the brief, `/tmp/pre_23_ch23_cross_asset_convexity_and_vol_surface.md` (commit 9ac1c37) and, as the true pre-writer baseline, commit 5927149 (the last commit before the writer's scenes appear). Web/fetch calls used: 7 (BIS QR June 2005 PDF, Federal Reserve SVB review PDF, FDIC PR-23-016, Debtwire 26 Apr 2023, one search for GM's May 2005 prices, plus two BIS URL misses).

## 1. Nothing removed

Method: python3 comparison of headings, `$$` count, [SOURCE EXTRACTION] blocks, Trend Watch boxes, Desk Myth, Poker Table, Docket Diary, Ways This Blows Up, numbered exercises, Resource Graph bullets and URLs, `#code-` links, `\tag{}` equation numbers; then a line-by-line match of every pre-text line and a number/proper-noun token diff.

- Against 9ac1c37: all 24 headings present; 54 `$$` before and after; 6 source extractions, 4 Trend Watches (all at the end of their sections: 23.2, 23.6, 23.7, 23.9), 2 Desk Myths, 2 Poker Tables, 1 Docket Diary, 3 Ways This Blows Up all present and verbatim; Exercises 1-6 verbatim; all five `#code-23-1..5` links present (13 occurrences with the Finder); equations (23.1)-(23.11) all tagged; all URLs present.
- The three Full Derivation subsections (23.1; 23.3-23.5 Steps 1-6; 23.8 Steps 1-2) hold the moved derivations. The SVB facts table and "Why the surface was wrong" were absorbed into Long Scene 2 as briefed. The GM timeline table and the Wolfspeed case note's reported terms are intact.
- Token diff against the pre-writer baseline 5927149: nothing numeric or named lost ("94%" is now "94 percent" in the cold open; the only other hit was "Use Chapter ..." replaced by the Ch 10 pointer, as briefed).
- Differences from 9ac1c37 that are NOT the writer's (upstream steps between 04:25 and 10:18, already in commit 5927149): figures embedded; the "Code Companion" boxes and `<!-- EXPLAIN -->` comments replaced by the one-line Appendix F pointers (code mover); the two generic podcast bullets replaced by verified episodes and new Talks/Reports bullets (U3 media); fact-check corrections (BS put 1e-24; time-zero ghost inverts the curve). No restoration needed.
- Fixed: none required.

## 2. Facts

New claims about real events were listed with difflib (332 new sentences against 5927149) and checked against the dossiers (`case_carvana_svb_wolfspeed_capital_structure.md`, `rv_credit_pairs_literature_and_mechanics.md`, `perspectives_*`) and primary sources.

Verified without change:
- Cold open: SIVB close \$267.83 (8 Mar), \$106.04 (9 Mar, -60.4%); implied vol floor 39, 167 premarket on 10 Mar, 52-week range 39-280 (Market Rebellion via dossier); 10-K unrealised losses \$17.7bn vs common equity \$12.4bn = 143%; HTM \$15.2bn vs total equity \$16.0bn (matches Ch 6); 94% uninsured, 6.2-year duration (Fed review, re-read); holdco \$3.3bn of notes over 59.2mm shares = about \$56; deposits \$173.1bn; \$21bn AFS sale, \$1.8bn after-tax loss, \$2.25bn raise (Fed review, re-read).
- Long Scene 2: Fed quotes "relatively stable ... before deteriorating sharply", 12 Buy / 11 Hold / 1 Sell on 1 Mar, deposit outflows over \$40bn and \$100bn expected (re-read in the Fed PDF); FDIC PR-23-016 \$209.0bn assets and \$175.4bn deposits (fetched); Fed says CDFPI closed the bank on the morning of 10 Mar (so "by midday" stands); 12 Mar joint statement; holdco "recourse only to the Company" 8-K quote (dossier); Chapter 11 on 17 Mar; 69 / 57 on 25 Apr (Debtwire, fetched); Aug 2026 N.D. Cal. ruling on the \$1.71bn claim (dossier, American Banker / PYMNTS).
- Debtwire (fetched): PIMCO, Centerbridge and Davidson Kempner "formed a group and retained PJT Partners ... according to a WSJ report"; the text attributes this to Debtwire citing the WSJ and says nothing about their reasoning. Howard Marks quote and 17 Apr 2023 date match the dossier's string-matched memo table.
- GM: BIS QR June 2005 p.5-6 (re-read): about 3% of IG and up to 15% of global HY; "lost money on both legs" quote exact; correlation-trade quotes exact; "similar in nature, albeit certainly not in magnitude" exact. GM closed \$27.77 on 3 May 2005 and Tracinda's \$31 was a 13.43% premium (search result quoting the offer documents), so the scene's "stock at twenty-seven (illustrative)" is close to the real print. DLY (2007) \$66.25 per \$100 and Avino-Lazar (70 obligors, 2005-2009, negative Sharpe both sub-periods) match the RV dossier. P&L arithmetic in the scene re-derived: 40,000 shares x \$27 x 18% = \$194k; 195bp x 4.2 x \$10mm = \$819k; total about -\$967k = -\$937k convergence + \$3.6k carry - \$33k gamma; Mags about -\$380k.
- Carvana PB-05: \$3.72 on 27 Dec 2022, -99%; stack mark 44.8; 2 Jun 2023 offer terminated (\$500mm minimum); TSA over 90%; +40% to \$55.80; 1 Sep 2023 settlement at 96.4%; \$350mm equity trigger; Garcia Parties \$126mm at \$46.31; 47% of float short; h* never above 18.9% (all dossier §1). ADESA unrestricted designation, 8-K of 22 Mar 2023 (dossier §1.4).
- Wolfspeed spine: 28 Mar 2025 \$2.59 (-50%), 2 Jun grace period, RSA 22-23 Jun, 26% marks, 25-30% plan range, 29 Sep open \$18.00 / close \$22.10 / plan value \$22.02, strikes 18 to 49 times spot (dossier §3).
- Two Sigma posting and Bloomberg 15 May 2019 / Israelov quotes match `perspectives_dealers_and_systematic_shops.md`; Hertz 8-K Ex. 99.1 quotes match `perspectives_buyside_credit_managers.md`; CS AT1 and UBS figures are the pre-existing cited ones.
- Math boxes recomputed in python: 58.25 and 0.91; 10,100 vs 10,000; 2 x N(-1) = 0.317 (box says 0.318 from 2 x 0.159); e^-0.05 = 0.951 and 103.0; 6.6 and 69 days, 0.23 and 0.071; 4% - 0.1% = -3.9%; 0.48/10 = 4.8%; the 7.50/2.50 spread at 45c = 9% and about 575bp; \$5 put 24 cents and 2e-24; 23.1 table 82.1 / 32.6 / 11.2 and 46 / 73 / 117%; Dana's 41 -> 29 -> 22 -> 12 -> 3 funnel and "38 names".

Fixed (small Edits):
1. GM timeline table row "June 1: Both names leave the CDX and iTraxx indices at the roll" was wrong (CDX/iTraxx roll in March and September). The BIS chart footnote puts the 1 June series break in the JPMorgan euro investment-grade industrials index. Row corrected. (Protected table, but a wrong fact.)
2. Theo's index speech said "the index providers use an average of three ratings" and "every holder that tracks an IG index becomes a seller on a date you can write down". BIS says "several of the largest" providers, and that Ford stayed in some IG indices. Speech narrowed to match, and the BIS's own counterweight added after the 1998 sentence: cash markets "appeared to adjust in an orderly way" because the downgrade "had long been anticipated"; derivatives gapped.
3. Debtwire citation for the 69 / 57 prices said "April 25, 2023"; the article is dated 26 April and the prices are of the 25th (as Ch 6 already says). Corrected.
4. Theo's SVB Monday outcome said the notes "were still worth more than he paid", which overstates an unclosed recovery. Replaced with the dossier's July 2024 mark (1.8% 2026s at 63.625, TRACE via Bloomberg) and an explicit "final recovery is not closed".
5. "\$2.3bn deposit gap ... which consolidation nets out" was stated as fact; now marked as my reconciliation, not audited.
6. Another Seat (opportunistic): "distressed buyers paying around 30 cents ... that week" changed to "in the 30s" (Debtwire's wording, no week asserted).
7. Convertible desk / replicator box: "see the same convertible and see opposite things" was inaccurate (the AQR paper is about corporate bonds, not converts) and attributed a belief ("thinks") to a real party. Reworded to the paper's finding, the Two Sigma "reason" softened to a reading, "in this chapter's reading" added to the Moyer split.
8. Wolfspeed: "on 29 June the FY2025 10-K marked ..." (the 10-K was filed in August; 29 June is the balance-sheet date). Reworded.
9. Carvana PB-05 box: "By the spring the equity surface still said default" was an unsupported claim about the options surface. Replaced with the dossier's 31 Mar 2023 close (\$9.79); the \$55 note price marked illustrative.
10. Hygiene tie-in: one unescaped "\$17 billion" in the Resource Graph (Credit Edge item) escaped.

Invented speech and labels: no quotation is attributed to a real person beyond published text (Marks memo, Israelov via Bloomberg, Fed, FINMA, UBS, BIS, SVB / Hertz 8-Ks). Kerkorian appears only inside the BIS quote and as the 1995 Chrysler allusion in Mags's mouth; Centerbridge, Davidson Kempner and PIMCO are named only through Debtwire / WSJ and no reasoning is attributed. Fictional pieces are labelled: replay headers (cold open, GM, SVB, CS), Ines's hand history (fictional composite), Dana's vignette (fictional composite), PB-05 box (fictional composite pod, illustrative hedge ratios), Mags's 1999 story (her story, unnamed issuer, illustrative).

## 3. Hygiene

- No code fences of any kind (the chapter has no ```text diagrams). No indented code blocks.
- 54 `$$` lines (even); no inline line with an odd count of `$` after the fix; braces balanced in inline math; no `\(` or `\[` delimiters.
- Currency: every `$` followed by a digit outside math is escaped (the only unescaped hit, "\$17 billion" in the Resource Graph, fixed); remaining `$` + digit matches are math (`$0.6 \times 100$`, `$10^{-24}$`, and similar).
- No `---` rule lines anywhere.
- Last line is `<!-- STATUS: COMPLETE -->`.
- Five `<!-- FIGURE (brief §3) -->` placeholders remain for U4 (GM two-leg P&L, persistence, Carvana h*, SVB holdco vs put wing, CS AT1 waterfall).

## What remains doubtful

- Holdco bond prices (near 90 / mid-80s before; 37-42 on 10 Mar; 40 vs 47-50 on 13 Mar; about 60 on 17 Mar; "in the 30s") rest on press and search summaries, hedged in the text. Closing them needs TRACE.
- Docket Diary (protected, left verbatim): "\$3,279mm of senior notes" is carrying value (principal \$3,300mm) and "about \$2bn" of cash vs \$1.71bn at trial.
- Two Sigma posting is undated and may be gone; Hertz "\$239mm of cash to old equity" is secondary; Tracinda row details (4.95%, 3.89%, 9 May / 7 June tender dates) are pre-existing and were not re-fetched this pass.
- The \$2.3bn deposit difference being the holdco's intercompany cash is suggestive (parent-only cash \$2,258mm) but unaudited.
- Pre-existing wording not changed: the GM table's "May 3: Last trading day before Tracinda's announcement (Schedule 14D-9)" and the Table 23.1 N(d1) = 0.999 at V = 150 (computed 0.99951, rounds to 1.000; the 0.999 is a truncation); both protected.
- Figure caption for the GM P&L must show the gamma bar as negative for Kaz's book (already noted for U4 in the chapter comment and open_items row 9).
- `state/research/open_items_ch23_ed2.md` updated with a "Verifier pass" section (rows 5, 6, 7 superseded).

<!-- STATUS: COMPLETE -->
