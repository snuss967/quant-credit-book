# Verification Report: Chapter 27, System Construction, Low-Latency Infrastructure & ASICs/FPGAs (Edition 2)

Verifier pass, 18 Oct 2026. Chapter: `book_src/27_ch27_system_architecture_and_asics.md`. Pre-revision text: commit 9ac1c379 (04:25 UTC, before the figure pass, so the five figures and the Resource Graph upgrade appear as "new" in the diff and were checked as such). Revision log was `<!-- STATUS: COMPLETE -->`. Brief: `27_ch27_system_architecture_and_asics.brief.md`.

Sources used. Web tools: 15 calls (federalreserve.gov FOMC page; FCA search and press release; The DESK x2; Virtu 10-K search; Revlon rehearing search; Revlon 10-K $504mm search; Signals and Threads Ep 20 page; Jane Street blog x3; Fowler; Odd Lots search and omny page). One further attempt, a curl of the SEC Knight order PDF, returned an empty body and is not counted as a source. Primary texts for Knight (SEC Release 34-70694) and the Second Circuit opinion (No. 21-487) were checked against the copies the writer saved in the session scratchpad (`knight/knight.txt`, `ca2_dl/op.txt`), read with python grep. Local cross-checks against Chapters 1-B, 3, 5, 22 and the dossiers in `state/research/`.

## 1. Nothing removed

Script: `cmp.py` and `cmp2.py` (scratchpad), pre vs post.

| Item | Pre | Post | Result |
| :-- | :-- | :-- | :-- |
| Headings (`#` lines) | 38 | 46 | All 38 present verbatim; 8 new (4 x "The Full Derivation", 2 Long Scene, 2 Decision point) |
| Display-math blocks (`$$` tokens) | 38 (19 blocks) | 38 (19 blocks) | Equal; one block differs only in terminal punctuation (the $G_k$/$K_c$ line now ends with a comma because a clause follows) |
| [SOURCE EXTRACTION] blocks | 13 | 13 | All 13 verbatim, annotations unchanged |
| Trend Watch boxes | 4 (6 mentions) | 4 (6 mentions) | All 4 verbatim |
| Exercises | 6 | 7 | 1-6 verbatim; 7 (PB-01) is new |
| Appendix F links (`#code-27-1` to `27-5`) | 5 | 5 | Present |
| Specification blocks / "What ROBO built" lines | 5 / 5 | 5 / 5 | Present, verbatim |
| "The Spec You Hand the Robot" | 1 | 1 | Byte-identical |
| Table rows (feed zoo, e-folding, Serta, order-state, two-budgets, tier) | all | all | No row missing |
| URLs | 13 | 31 | None missing |
| Figures | 0 | 5 | Added by the figure pass; files exist in `assets/figures/` |
| Resource Graph bullets | 26 | 39 | 24 verbatim; 2 not verbatim (see below) |

Derivations moved into "The Full Derivation" subsections (bitemporal, P-K, diffusion/Bachelier, CUSUM) are intact: the math multiset is unchanged.

Two Resource Graph bullets are no longer present: the series-level pointers "Bloomberg Odd Lots (series)" and "Flirting with Models (series)". They were replaced by specific, dated episodes (HRT pair; Angana Jacob S7E26) in the earlier Resource Graph upgrade pass (logged in `27_ch27_system_architecture_and_asics.resgraph.md`), not by the U2 writer. The old lines said "no specific episode was verified" and "series-level pointer only". I did not restore them. If an editor applies "nothing removed" strictly to Resource Graph lines, re-add them as one-line series pointers.

## 2. Facts

New factual claims were listed by sentence-level diff against the pre text, then checked. "Fiction" means labeled fictional composite or illustration in the text; arithmetic inside fiction was recomputed.

| # | Claim (section) | Check | Verdict |
| :-- | :-- | :-- | :-- |
| 1 | FOMC decision Wed 28 Oct 2026 (27.0) | federalreserve.gov: Oct 27-28 | Confirmed |
| 2 | Citadel Securities in US IG credit since June 2023 via MarketAxess and Tradeweb; Cila "lives at the nexus of our fixed income and ETF franchises"; Marmoiton (Alken) "No one wants to hold much inventory that is not hedged very well" (27.1) | The DESK, 19 Jul 2023, fetched | Confirmed. Changed "buy-side skeptic" to "buy-side trader" (the article does not support "skeptic") |
| 3 | Cifu quotes, Q4 2021 and Q2 2022 (27.1) | The DESK, 23 Jan 2023, fetched: "We've enhanced and began to be a market maker in fixed income"; "It's still very early in fixed income" | Confirmed. Fixed an ungrammatical truncation of the first quote |
| 4 | Virtu FY2015 10-K "automatically freezes the applicable trading strategy, cancels all applicable open orders" (27.1) | 10-K text via search | Confirmed |
| 5 | Serta $875mm vs $734mm, "§5.6.2 reconciles" (27.3.3) | Ch 5 lines 759-760 carry exactly this reconciliation | Confirmed |
| 6 | Mags: $15mm first lien, sold half at about 20 in Jan 2021 (27.3.3) | Ch 5 lines 727, 755 | Confirmed, consistent |
| 7 | PB-01: Dov Adler, Vantress, $60mm Kestrel 6% 2030 at 96, $39mm Halvorsen 7.25% 2029 at 90, DTS about 72,600 vs 71,600, roll week, 14-month ticket, borrow 50 to 300 bp (27.4.2, Ex 7) | Ch 1-B lines 91-99; Ch 22 line 796 | Confirmed. Added "As opened in April" because Ch 2 and Ch 22 show the pair at later, smaller sizes. Ex 7 now states both DTS figures (72,600 long, 71,600 short) |
| 8 | FIX tags 22, 48, 167, 423 (1/6/9), 699, 64; Rule 15c6-2; 15c3-5 quote (27.4.2) | FIX dictionary and rule text from knowledge; 15c3-5 quote was in pre | Confirmed |
| 9 | Halt drill: 26 Feb 2019 and Thanksgiving 2025 CME halts (27.5.3) | Facts identical to pre text; brief says leave | Unchanged, not re-verified |
| 10 | Flash-rally facts (27.6.3) | Identical to pre text (16 bp, 37 bp range, 6 bp, PTFs over half) | Unchanged |
| 11 | McPartland and FILS Europe lines in the bank-seat box (27.7) | Same wording as the pre Trend Watch; box adds only labeled inference | Confirmed against pre |
| 12 | Knight (27.7.3): RLP start 1 Aug 2012; SMARS "automated, high speed, algorithmic router"; deployment from 27 Jul; Power Peg "discontinued using many years earlier"; one of eight servers not updated; no second technician and no written procedure; 2005 move of the cumulative-quantity function without retest; 8:01 a.m. BNET e-mails, 97 before the open, "did not design these types of messages to be system alerts"; 9.5% limit-price cap that did not apply to the 212 pre-open orders; 33 Account with $2mm gross limit not linked to controls; PMON post-execution, no alerts, no limits shown, delayed and inaccurate; no incident-response procedures; no control comparing orders in and out; uninstall from seven servers made it worse; 212 orders, 45 minutes, 4 million executions, 154 stocks, 397 million shares; 75 stocks over 20% of volume and 5% moves, 37 stocks over 50% and 10% moves; net long $3.5bn in 80 and short $3.15bn in 74; loss over $460mm; $12mm penalty; footnote on P&L auto-shutdown for some groups | Each phrase located in the SEC order text | All confirmed. No words attributed to Knight staff |
| 13 | Revlon wire (27.7.3): 2016 loan $1.8bn, seven-year, Citibank agent, maturity 7 Sep 2023; May 2020 $815mm new money, roll-up rights (opinion: $953mm aggregate; dossier/10-K: $950mm commitment); Elizabeth Arden IP collateral; loan at 20-30 cents; five Angelo Gordon holders; Flexcube; "wash account"; manual quote "ALL of the below field[s] ... FRONT [;] FUND [; and] PRINCIPAL"; six-eye maker/checker/approver; Wipro staff in the team; default wire quote; "stop sign" text with no amount; $894mm principal and $7.8mm interest; "to the penny"; notices mention interest only; 9 a.m. cash-break review on 12 Aug; UMB complaint about 2:06 p.m., about twenty hours later, authorised 30 Jul to 10 Aug; Section 2.11(a) quote and no prior notice; inquiry notice; vacatur 8 Sep 2022 by Leval, Sack, Park | Located in the opinion text | Confirmed, with the fixes in section 3 |
| 14 | Rehearing denied 12 Oct 2022 (27.7.3) | Revlon SEC filings via search | Confirmed (also: funds returned, dismissal with prejudice 19 Jan 2023; the book omits the dismissal) |
| 15 | About $504mm not returned per Revlon FY2020 10-K | Search summary of the 10-K | Confirmed in substance ("holders of about $504 million kept it") |
| 16 | Furman, 16 Feb 2021, discharge-for-value / Banque Worms | Opinion text and search | Confirmed |
| 17 | Jefferies as BrandCo agent; 7 May 2020 date; $3mm junior roll-up (27.7.3) | Dossier [Rev10K] only; the opinion does not mention them | Not independently re-verified (10-K blocked); see section 4 |
| 18 | Citigroup coda (27.7.3): $58mm intended, $444bn created, $255bn blocked, $189bn to algorithm, $1.4bn sold, no hard block, FCA fine GBP 27.77mm, PRA GBP 33.9mm, total GBP 61.6mm | FCA press release fetched; PRA figure from press coverage (GBP 33.88mm) | Confirmed. Reworded "click through without reading" to the FCA's "override ... without being required to scroll down" |
| 19 | Friedberg quotes (27.8), Ep 20 "Solving Puzzles in Production", 7 Oct 2024 | Episode page transcript: all four quoted phrases present | Confirmed verbatim; no invented dialogue for her |
| 20 | CrowdStrike/SGX, ICBC FS, Bloomberg 2015, ICE-MarketAxess (27.8) | Same as pre | Unchanged |
| 21 | Resource Graph: Fowler "6 million orders per second on a single thread", 12 Jul 2011; Jane Street ASIC post 10 Sep 2026 ("we'll pay to fabricate our favorite designs") and results 2 Oct 2026 ("physical layout, but not a netlist"); Advent of FPGA 24 Nov 2025; HRT Odd Lots title and topics | Pages fetched | Confirmed. Fixed the "will pay to fabricate" quotation to the post's wording; added "feed date" to the Odd Lots date (the page prints no date) |
| 22 | Nigito 2020-09-23, Andy Ray 2020-09-09, Doug Patti 2022-04-20, Hauff 2019-02-14, Angana Jacob 2026-02-09 | Dossier `media_episodes_posts_parts_V_VIII.md` only | Not re-fetched |

Arithmetic recomputed and found correct: e-folding (0.6 day, 0.8 µs, 1.7%); four-times-faster engine (about 0.1 s p99); P-K 233 ms, 1.42 s, 0.8 s at rho 0.5, 4.5 s at 0.9; supermarket (14 min, 1.6 in queue); relay team 63% and 78%; triangle-inequality lanes (0.074 + 0.064 = 0.14); Q.16 (68,813; 1.5e-5); 47 typical moves; CUSUM walk (1.1, 1.5, 3.1, 4.0, 5.0), ARL0 938 and 2,570, ARL1 10.3 and 12.3; Ilse's 88-point decimal move; $100,000 on the "105" fill; Knight forty fills at three-eighths = $300,000; Tomasz 460/4,180 = 11%, 1,900/90 = 21 a day. Calendar: 26 Oct Monday, 28 Oct Wednesday, 29 Sep Tuesday (Theo's week 2), 2 and 4 Nov, 6 Nov, 11 Aug 2020 Tuesday, 15 Oct 2014 Wednesday: all consistent.

Real people and invented words. Every quotation attributed to a real person (Cila, Marmoiton, Cifu, McPartland, Friedberg, Virtu 10-K) was matched to a source. All dialogue belongs to the fictional cast (Ines, Kaz, Mags, Theo, Hana, Ilse, Tomasz, Dov). The Revlon scene keeps Citibank and Wipro staff to their roles (maker, checker, approver) and quotes only the opinion; the Knight scene attributes nothing to Knight staff. Fiction labels are present at the top of the cold open, both Long Scenes, both Quant-Shop Life vignettes, the FIX incident, the Tier-2 incident, the halt drill, the flash-rally replay, the Pair box and Exercise 7.

## 3. Fixes made (small Edits to the chapter)

1. Cifu quotation: restored the full quoted sentence "We've enhanced and began to be a market maker in fixed income".
2. Marmoiton: "buy-side skeptic" to "buy-side trader".
3. Flexcube: "the only practical way" to the opinion's "the easiest (or perhaps only)" way.
4. Revlon 12 Aug sequence: removed "and it asked for the money back" from the "within the hour" sentence (Citibank's recall notices started at about 2:25 p.m., after the 2:06 p.m. UMB complaint); added the 2:25 p.m. recall-notice sentence.
5. Citi coda: pop-up alert wording and "ineffective" real-time monitoring now follow the FCA text.
6. Exercise 7: both DTS values stated (72,600 long, 71,600 short); "sale of protection" corrected to the purchase of protection (a short in the index), since the survivor is a long.
7. Pair box: "As opened in April" added for continuity with Chapters 2 and 22.
8. Resource Graph: Jane Street quotation corrected to the post's wording; "feed date" added to the Odd Lots date.
9. `state/research/open_items_ch27_ed2.md`: appended a closure table for its six items.

## 4. Hygiene

- Code fences: three, all ```text (the two-speed diagram, the Man reference architecture, the Spec You Hand the Robot).
- Math: every display block closed; no line with an odd count of unescaped `$`; no unescaped currency (`\$` throughout; the two `\$` inside math at the dollar-duration symbol and the $5,500 loss line are intentional).
- No `---` rule lines anywhere.
- Last line of the chapter is `<!-- STATUS: COMPLETE -->`.
- All five figure files exist; all `#code-27-n` links present.

## 5. What remains doubtful

- Knight and Second Circuit texts were verified against the writer's saved copies, because my own fetch of the SEC PDF returned an empty body. The copies match the known public record on every point checked.
- Revlon BrandCo details that rest on the 10-K only (Jefferies as agent, 7 May 2020, $3mm junior roll-up, IP moved to non-guarantor BrandCos, $950mm vs the opinion's $953mm) could not be re-read (sec.gov blocked). The $504mm figure was confirmed through a search summary, not by opening the filing.
- CME Globex halt times (6:39 to 9:45 p.m. CT, 26 Feb 2019) and the Thanksgiving 2025 ten-hour duration are unchanged from the pre text and were not re-verified here.
- Episode dates for Nigito, Ray, Patti, Hauff and Jacob come from the dossier; the HRT Odd Lots date is a feed date.
- The 2:00 p.m. statement time on FOMC day is standard practice, not printed on the calendar page.
- Chapter 1-B's later pair sizes in Chapters 2 and 22 (31.5mm, 35mm) differ from the opening sizes used here; the Pair box now says "as opened in April".
- Two series-level Resource Graph pointers are gone (section 1); restore if a strict reading applies.

<!-- STATUS: COMPLETE -->
