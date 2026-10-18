# Verification report, Ed. 2 revision of Ch 6-B (Options for Credit People)

Verifier run 2026-10-18. Chapter: `book_src/06_ch06b_options_and_measures_for_credit.md` (943 lines after fixes). Pre text: commit 9ac1c37 (612 lines). Log `...06_ch06b_options_and_measures_for_credit.log.md` ends with `<!-- STATUS: COMPLETE -->`. Web calls used: 9 of 15 (SEC exhibit fetch, Debtwire fetch, 7 searches).

## 1. Nothing removed: PASS (no restoration needed)

Script comparison of pre and post:

| Item | Pre | Post | Verdict |
| :-- | --: | --: | :-- |
| Headings (`#`) | 43 | 52 | all 43 present; 9 added (Wolfspeed scene and its card, SVB scene and its card, Shop life, three "Full Derivation" subsections, Halvorsen card) |
| Display-math blocks (`$$` pairs) | 35 | 37 | every pre block present verbatim (whitespace-normalised); 2 new (old-share payoff g; B-S formula stated in the new box) |
| `[SOURCE EXTRACTION]` blocks | 3 | 3 | Veronesi p.611, Bohn-Stein p.516, p.181 extraction text identical; the p.181 annotation's "rule 4" was repointed (the four rules became the `to_q` scene) and "Trend Watch above" became "at the end of this section" |
| Trend Watch boxes | 1 box (2 hits) | same | paragraph is verbatim, moved to the end of §6-B.6 as briefed |
| Exercises | 4 | 4 | text intact; Checks added to 2 and 3 |
| Appendix F links (`#code-`) | 1 | 1 | `#code-6b-1` kept; the "Code Companion" box was reduced to the book-wide "*The full listing is [Listing 6-B.1 in Appendix F](#code-6b-1).*" line (same form as Ch 4, 4-B, 4-C, 5) and the `<!-- EXPLAIN -->` marker dropped |
| Resource Graph | 4 bullets | 4 + sub-list | all original items and URLs kept; 7 URLs added by the separate resgraph pass (log in `...resgraph.md`) |
| Equations (6B.1)-(6B.6), Figures 6-B.2 to 6-B.6, Desk Myth, Poker Table, §6-B.7 table, 3 Ways This Blows Up | | | present; Ways This Blows Up (§6-B.9) gained one clause pointing to Rafael |

Paragraph-level audit: 45 of 232 pre paragraphs are not verbatim in the post text. All 45 are (a) briefed scene replacements (cold open, §6-B.1.4 list, §6-B.6.6 rules, Halvorsen "what kills it"), (b) briefed prose conversions (§6-B.5 bullets), (c) trims with the substance kept (checked word-by-word: the only deletions are connective phrases, "Underneath, it is a third of a share of the firm plus a short put with a large vega", and the "is not short a call in any meaningful sense" clause, both covered elsewhere), or (d) additions of figure pointers. The proofs were moved under "The Full Derivation" headings, not deleted. A correction the writer made: §6-B.3.4 bond delta for the 216 bp firm, 0.120 to 0.119 (recomputed: N(-1.178) = 0.1194; correct).

## 2. Facts

Method: difflib on the pre/post texts (60 inserted or replaced hunks) read against the dossiers (WOLF §3, SVB §2, LIFE §4, PERSP-D, Ch 6 and Ch 16 in the book) and the web. Every numeric claim was also recomputed in Python (private folder `scratchpad/v06b_verify/`).

### Verified, no change

- Wolfspeed stack, dates and counts (dossier WOLF §3.1-3.3): converts 575/750/1,750 with conversion prices, secured notes 1,521.2, Renesas 2,062, total 6,658.2, cash 955.4; 28 Mar 2025 failure and $2.59; 2 Jun missed interest; 30 Jun filing, 8 Sep confirmation (day 70), 29 Sep effective; $18.00 open, $8.05 low, $22.10 close vs $22.02; 24,533,760 / 1,306,896 / 871,287 / 16,852,372 shares; 0.008352 and 0.005568 ratios (recomputed 0.0083518 and 0.0055680); 156.48mm old shares; $48mm, 31 and 18 cents; 94mm at 60 cents; 3% and 5% of 43.56mm shares (3.0002%, 5.0004%); strikes 18x, 46x, 49x spot; 26 Mar 2026 1.5-lien convert at $20.14 and the four strikes; $73.50 on 26 May 2026 (3.34x plan). The $0.28, $0.0672-$0.1846 and $1.02 calculations reproduce.
- RSA release (SEC ex. 99.1, fetched): "holders of more than 97% of its senior secured notes"; exchange of "$5.2 billion of existing convertible notes and Renesas' existing loan" for "$500 million of new notes and 95% of the new common equity"; shareholders "pro rata share of 3% or 5% of new common equity," "subject to ... potential reduction from certain events"; release dated 22 June 2025.
- SVB: $267.83, $106.04 (-60.4%), >$40bn outflow, 8-K capital raise, equity $15.9bn vs $3.3bn senior notes (4.8x), default probability order 1e-7 (hedge ratio 1e-8, recomputed 8e-9), "recourse only to the Company" quote, Market Rebellion 167 / 39-280 / 1.1:1, CDFPI closure and FDIC receivership 10 Mar, Chapter 11 on 17 Mar (S.D.N.Y. 23-10367), all seven series accelerated, TRACE 37-42 at the 10 Mar close (BNN Bloomberg article, confirmed by search), Debtwire 26 Apr 2023 with 69 and 57 (page fetched: MarketAxess, prices of the afternoon of 25 Apr, "some probability of reinstatement"), Barr report 28 Apr 2023.
- AQR (PERSP-D plus search): Bloomberg 15 May 2019 via WealthManagement.com, Israelov, four exposures, up to 76%, "enhanced liquidity and cash efficiency"; Israelov would not say whether AQR would use it (dossier).
- Optiver rhythm (LIFE §4.2: 15 minutes of news, standup, 4:00 review "what we didn't do") and Jane Street (LIFE §4.1; *Signals and Threads* Ep. 29, "Wrestling the World into Rows", Eric Mannes, released 2 Sep 2026, confirmed by search): the three quoted phrases ("a large Microsoft Excel spreadsheet", "whoops, made a mistake", "all the data ... along with the time we received it") are real quotes in the dossier, attributed to the firm's podcast, not invented.
- Hertz June 2026 financing (search, Davis Polk, Las Vegas Sun/PRN, Stockopedia): $350mm upsized from $300mm, 6.75% exchangeable first-lien secured PIK notes due 2030, priced 24 Jun 2026; 37,037,037 shares at $2.70 (about $100mm) loaned to J.P. Morgan for noteholders' hedging; stock -41% to about $3. This also settles item 1 of `open_items_ch16_ed2.md` for these figures. The chapter's hedge ("figures approximate") stands.
- PB-07 Hertz 2020 legs and facts ($0.59 to $5.50, $29mm sale, "could ultimately be worthless", $2.00 close on 17 Jun, notes at 27, CDS auction about 26, $1.53 + 3% + warrants, solvent-debtor fight) are Ch 6 §6.10.2 and Ch 16 canon; consistent. Owen, Vantress, Wen Zhao, Marcus are fictional composites, labeled.
- Numbers recomputed and correct: parity lunchbox (96.08, 3.92; call 13.75 so put 9.83), butterfly 14/8/4 = 2, factory 6.67 and 2/3, gamma rent 70 a year (28 cents a day), N(d1) 0.61154, N(d2) 0.49335, bump table 14.37/13.15/0.61/0.38/38.3, skew box (strike 73.42, 12.41 vs 5.41, ratio 2.29), funeral and floor (0.914, 0.047), ridge (1.657, 1.609, 0.785), compromise delta (-0.72, 14.4x, 6.9x), clock and bill (0.865; 150+150+120), cold-open vega (-0.199 x 200,000 = -39,800; 97%; residual about -1,200), the §6-B.3.4 table (all lines recomputed), exercise Checks (2.25 / 2.31; $0.49 and $2.04 by the bound, $0.75 and $2.72 by the leak), SVB hedge size (950,000; 3,547 shares; +$574k on Thursday), put spread (about four cents).
- Cross-references checked: Ch 6 has Mags buying holdco paper "at 38" and the structural-model failure; Ch 8 Case Study B is the SVB hedger replay; Ch 16 says vendors differ on Wolfspeed's 29 Sep prints.

### Fixed in the chapter

1. Wolfspeed: "the press release the next morning" became "dated that Sunday" (release is dated 22 Jun 2025).
2. Wolfspeed: "press reports put it at 59 and 60 cents" became "at 60 cents, down 33 to 34 per cent" (search found 60 cents and 33.2-34.4%, no 59).
3. Wolfspeed: removed "new stock near \$17" on 29 Jan 2026 (no source for a January print); replaced with the sourced 2025 year-end close of \$17.41 and "the folder holds no January print"; "wandered from \$22 to \$17" became "closed the year at \$17.41".
4. Wolfspeed: "no listed-option surface ... worth fitting" overstated an evidence gap (WOLF had listed options); now "no option-chain data it trusts ... the research behind this replay found neither, an evidence gap that vendor data would close".
5. SVB: Friday 10 Mar said there was "no first print after Thursday's close". Wrong: shares traded premarket, down as much as 69%, until Nasdaq halted them at 8:35 a.m. Rewritten (premarket prints existed; listed options do not trade premarket; no fill at a price worth having) and Kaz's grade line adjusted ("stopped trading before it could be sold at a price that mattered").
6. SVB: fictional run's put figures did not reproduce (\$19.96 / \$19.69 / \$5.29). Recomputed at S = K = \$106.04, sigma 45%, r 4%, one month, lambda solved for 167 vol (2.48 a year, 18.7% in the month): \$19.99 / \$19.71 / \$5.31; wing floor 203% and model 343% confirmed. Text now names the \$106.04 stock and uses the recomputed numbers.
7. SVB: "implied volatility that had lived between 39 and 50 for a year" contradicts the 52-week range up to 280; now "until that week".
8. SVB: Ines's "In the real world, on desks like this one, nobody read that line" was an unverifiable claim about real desks; now "On a desk like this one, nobody would have".
9. AQR seat: removed the invented cost "for a few basis points".
10. Bohn-Stein p.181 annotation: "Ines's last clause" repointed to "right measure for the job" (the clause that carries the Q-for-prices, P-for-risk rule).

### Real people, dialogue and labels

- No real person has invented dialogue. Real people appear only in sourced paraphrase or real quotes (Israelov via Bloomberg; Mannes via the podcast; Wilmott and Eifert only in Resource Graph blurbs taken from episode descriptions). All speech belongs to the fictional desk (Ines, Kaz, Mags, Theo, Rafael) and the fictional pod (Owen, Wen, Marcus).
- Fiction labels present on every scene: Wolfspeed and SVB replays (italic "A replay. The desk's ... fictional"), Rafael vignette ("A fictional composite"), PB-07 ("fictional composites ... illustrative"), cold open and Halvorsen ("fictional and illustrative"). Invented desk numbers carry "(illustrative)" at first use. No "CHECK" remains in the text.

### Remains doubtful

- Forward reference: the Wolfspeed scene says "the dated docket is Chapter 13-B's Wolfspeed Docket Diary". Ch 13-B is in the TOC plan (`state/open_items_ed2.md`) but no file exists in `book_src/` yet; if 13-B is not written, repoint to §13.3 or drop the clause.
- Hertz PB-07 prices (notes at 27, stock at \$2.00 on 17 Jun 2020) and the Hertz 2020-21 facts were inherited from Ch 6 and Ch 16, not re-checked against primary sources here.
- The fictional SVB 2031-note mark of 76 is plausible (about 76.5 at a 5.5% yield, my calc) but invented, and is labeled "(illustrative)".
- The dossier's old-WOLF 26 Sep 2025 \$1.21 and short-interest figures remain unverified; the chapter correctly does not use them.
- Resource Graph additions (7 URLs) were verified by the resgraph pass, not re-fetched here.
- Cross-references to §13.3 (uptier), §13.6 (drop-downs), §14.1, §15.2, §21.1, §23.1 and §28.4 resolve to existing section headings; their content was not re-read beyond the heading titles.

## 3. Hygiene: PASS

- Code fences: exactly one pair, ```` ```text ```` (the Figure 6-B.1 ASCII ladder, lines 105-122); no other code blocks.
- `$$` count 74 (even); inline `$` balanced in all paragraphs (0 odd); no unescaped currency found (every `$digit` hit was a math opener).
- No line beginning `---`; no horizontal rule directly before text.
- Last line is `<!-- STATUS: COMPLETE -->` (single occurrence).

## Housekeeping note

I wrote five scratch files with generic names (`check1.py`, `check1b.py`, `diff2.py`, `added.txt`, `nums.py`) into the shared scratchpad before noticing it holds other runs' files; they may have replaced same-named files. Everything after that went into `scratchpad/v06b_verify/`.

<!-- STATUS: COMPLETE -->
