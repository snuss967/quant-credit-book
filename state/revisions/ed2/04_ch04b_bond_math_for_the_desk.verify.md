# Verification report: Ch 4-B, Bond Math for the Desk (Ed2 U2)

Verifier pass on `book_src/04_ch04b_bond_math_for_the_desk.md` after the writer's revision (log: COMPLETE). Web calls used: 3 of 15 (one search, two fetches).

## Baseline note (read first)

The commit named in the task, 9ac1c37, holds the pre-U1 chapter (445 lines, 8.2k words, ending at the make-whole, no Case Study, Spec, Debrief, Exercises or Resource Graph). The brief's "12.7k words" chapter is commit cea2d0d (599 lines, 12,679 words), the last state before U2. All three checks were run against both baselines. The 9ac1c37 comparison is trivially satisfied (everything U1 and U2 added is "new"); the cea2d0d comparison is the meaningful one and is what the fact check below uses. Post-revision chapter: 830 lines, 20,566 words (wc), inside the brief's 20-23k target.

## Check 1. Nothing removed

Python comparison of headings, display math, extraction boxes, tables, boxes, links, exercises and the Resource Graph, plus a line-level difflib pass over every pre line that is not verbatim in the post.

- Headings: against cea2d0d, four are gone and each has a successor. "Properties, with proofs" is now "#### The Full Derivation" (derivation intact). "Rows that are only rulers", "Rows that moved" and "Rows that became prices again" are now Beats 2, 3 and 4 of the promoted Long Scene. Against 9ac1c37 the only missing heading is "Properties, with proofs" (same successor).
- Display math: 24 blocks in the pre (48 `$$`), 24 in the post, and a whitespace-normalised multiset comparison shows none missing and none changed. The Full Derivation moves (premium identity proof, dD/dy, periodic C-mod, ASW package valuation, Ho-Lee theta fitting) all kept their displays.
- Source Extractions: 6 boxes in pre and post (Veronesi pp.158 and 467, Schmid p.159 twice, Ben Dor p.191, Bohn-Stein p.68), all verbatim with their annotations. The Veronesi pp.162 and 464 quotes survive inline (p.464 sentence verified in place).
- Table rows: 54 in the pre, 64 in the post, none missing (Table 4B.1 with footnote, three-meanings, eight-spreads, "When to reach for which number", Brambleworth YTW table; new rows are the Finder table).
- Trend Watch (1), Poker Table (1), Ways This Blows Up (3), the two original View From Another Seat boxes, "Six rulers, one length" Math Gently, make-whole proposition and proof, hand lattice and four identities, Exercises 1-5 with solutions, Spec, Resource Graph (including the MIT 15.401 and Davies entries), `*Used in:*` lines (10 and 10) and the `#code-4b-1` Appendix F link: all present, unchanged.
- Line-level pass: 44 pre lines are not verbatim in the post; every one is a deliberate rewrite or relocation under the brief (retired cold-open paragraphs, the three spread-duration bullets turned into Kaz's whiteboard, derivations moved under "The Full Derivation", the case study split into beats). Spot reads of the low-similarity ones (L196-198, L320, L332, L346, L408, L521) found their content carried into the new text. Nothing needed restoring.
- Exercise numbers: no new box reuses an exercise solution's numbers.

## Check 2. Facts

Diffed pre (cea2d0d) against post by section; every new claim about real events, firms, people, dates, amounts or rulings was checked against the dossiers the brief names (`case_carvana_svb_wolfspeed_capital_structure.md` §2, `media_episodes_posts_parts_I_II.md` 4-B block, `life_quant_shop_daily_life.md`, `rv_pod_platforms_and_risk.md` §5.2), the SEC 8-Ks already in the scratchpad, and the web.

Confirmed as written:
- SVB: 10-K filed Fri 24 Feb 2023; HTM $91.3bn cost vs $76.2bn fair value; unrealized losses $17.7bn vs $12.4bn common equity (143%); deposits $173.1bn, down $16.1bn; FHLB advances $15.0bn vs none; 94% uninsured (Fed review); 8 Mar raise of $2.25bn; Silvergate wind-down; stock $267.83 to $106.04 (-60.4%); 30-day implied vol 167 against a 52-week range of 39 to 280; seven holdco series, $3.3bn, 3.50% Jan 2025 to 4.570% Apr 2033; 1.800% Feb 2031 exists ($500mm); holdco bonds in the 30s-40s afterwards (press reports, hedged in text). All weekday names check (6, 7, 8 Oct 2026 Tue/Wed/Thu; 8, 9, 10 Mar 2023 Wed/Thu/Fri).
- Trial: fetched PYMNTS (Reuters, 31 Aug 2026) and American Banker (Sep 2026). Both confirm U.S. District Court in San Jose (N.D. Cal.), Judge Beth Labson Freeman, 12-day bench trial, ruling that the FDIC keeps the $1.71bn; American Banker confirms it was the holding company's cash deposited at the bank. The chapter's "late August 2026... federal court in California... twelve-day bench trial" is right and names no judge and quotes nothing.
- Davies / Odd Lots, 14 Mar 2023, "reached for yield buying long-dated Treasuries": matches the feed description in the dossier; Kaz's version is in Kaz's own words and Davies is not quoted.
- Jane Street *Signals and Threads* Ep 29 (2 Sep 2026): dossier transcript read supports "saves all the data along with the time we received it" (the "time machine"); paraphrase only.
- MIT OCW 15.401 Fall 2008, Lectures 4-6 and Recitation 2a (Andrew Lo): matches dossier entries.
- Liberty Street Economics, 16 Feb 2022 (downgrades of early 2020 exceeded the GFC total) and QML Solutions, 17 Dec 2025 (1,188 bonds, 56bp to 278bp): match the dossier rows.
- Fed 23 Mar 2020 corporate-credit facilities announced and not yet buying; S&P still IG on Ford on 23 Mar (cut 25 Mar); 9 Apr facility extension: consistent with the brief's dated spine.
- Cast facts (Theo ten weeks into PJT in March 2020 and six years at PJT; Kaz finishing a thesis; Ines tournament-scorecard handwriting and dealer IG book; Mags on a dealer distressed desk, "When I started there was one spread"; Ines "Cut it at 23 March. Trade it blind. Nobody looks at April."): match `state/cast_bible.md` including its new Ch 4-B section.
- All invented dialogue belongs to cast members. No real person (Davies, Lo, Schmid, Veronesi, Ben Dor, SVB officers, Ford's treasurer, the judge) has invented dialogue or an invented quote. Fiction labels are present once at the top of each scene (cold open, SVB replay, 23 March replay, Quant-Shop Life vignettes, Pair box "fictional composite", CLO seat "generic, no firm named"). Invented desk marks carry "(illustrative)".
- Arithmetic re-done: Pair box (36.5 / 26.7 / 21.9; all P&L cells; carry -$0.07m, -17bp), cheque stack 90.48, one-year 6.06%, bootstrap 0.9615 / 0.9066 / 4.90%, trucks 164 vs 100, Jensen coin 60.65 / 54.88 / 67.03 / 60.96 (0.5%), one-step tree 92.49 vs 91.78 (0.71), DTS 10% vs 1.25%, explain +6.7 / -55.0 / +12.8 / -2.1 = -37.65, 0.545 hedge and $4.05mm, 31st-rule \$1,250, 2.7bp compounding bug. All correct.

Fixed in the chapter (small edits):
1. SVB 8-K attribution. The $23.97bn / $21.45bn / 10.5% figures were presented as the evening-of-8-March announcement. The 8 March 8-K (SEC 0001193125-23-064680) says only "substantially all of its AFS portfolio" and an after-tax loss of about $1.8bn; the book value and proceeds first appear in the 13 March 8-K. The sentence now gives the 8 March facts and puts the later figures in a parenthesis ("a filing the following week"), with 10.5% labelled before tax (a calculation).
2. "Five days after the bank failed" (Davies, 14 Mar) corrected to "Four days".
3. "By midday the California regulator had closed..." replaced by "Before the day was out" (the hour is unverified); the more than $40bn of Thursday withdrawals is now attributed to the Federal Reserve's review (the dossier's tag), not to "the closing order".
4. "There was no single-name CDS to read a curve from" (a market claim I could not confirm; one search found nothing) rewritten as "The replay's data held no usable CDS curve for the name".
5. PECS at 40 (own-code claim). The scene, the Spec's "Where it refuses" paragraph and the Finder row said `pecs` raises on the SVB note at 40 with R = 40%. Running Listing 4-B.1 on the 16-coupon 1.800% note shows it does not: at 40 it returns about 3,500 to 6,000bp depending on the discount rate (4.5% to 3.5%), because the price is almost flat in the hazard; it raises only below about 39.8. The three places now say what the code does (returns an unusable number at 40, raises at 39); the Debrief bullet was widened to "refusal, or a spread that swings with the discount rate".

Hygiene-adjacent factual fix: none further.

## Check 3. Hygiene

- Code blocks: one fence pair, a ```text diagram (Sketch 4B.1 at lines 597-612). No other fences.
- Math: 48 `$$` (even, paired as blocks); zero lines with an odd number of unescaped inline `$` after the fix below; no currency inside math mode.
- Currency: one unescaped `($100)` inside the Veronesi p.464 quote (pre-existing) changed to `(\$100)`. Every other dollar amount is `\$`.
- No `---` lines in the chapter. No block element (box, table) touches an unseparated text line.
- Last line: the file ended with a blank line after the status marker; trimmed so the last line is `<!-- STATUS: COMPLETE -->`.

## What remains doubtful

- SVB desk numbers. The chapter's yield 5.77%, modified duration 7.11, DV01 \$5,340 at 75 (8.48%, 6.94, \$4,310 at 62; 6.5 at 40) reproduce with Listing 4-B.1 only at n = 16 coupons and w of about 0.86 with dirty = clean + 0.13, i.e. a settlement near the end of February. With the true 9 March T+1 settlement (w = 0.794) the figures are 5.79%, 7.08, \$5,319 (8.50%, 6.90, \$4,293; 6.48). Differences are under 2bp of yield and 0.04 of duration, the marks are labelled illustrative, and every downstream number (14.5-point slope loss, \$8.9mm hedge) survives; left as is. A one-line settlement note in the scene would close it if the editor wants it.
- Chapter 8 (not this chapter, not edited): Case Study B tells the 8 March evening 8-K as carrying \$23.97bn and \$21.45bn. Same misattribution as fixed here; flag for the Ch 8 verifier.
- The 52-week implied-vol range (39 to 280) rests on one secondary source tagged [MR] in the dossier. The post-failure holdco prices (30s-40s) rest on press-summary rows the dossier tags CHECK; the text says "press reports".
- Davies's episode is characterised from the feed description, not a transcript; Eric Mannes's episode from the dossier's transcript notes. Neither was re-fetched.
- The American Banker and PYMNTS ruling dates differ (28 vs 31 Aug); "late August" is safe.
- The Fed-review figures (94% uninsured; more than \$40bn on 9 March) were taken from the dossier's FED-BARR tags, not re-opened.
- The brief's CLO pointer said "Ch 22"; the writer pointed to §21.1 / §21.4, which exist and are correct.

<!-- STATUS: COMPLETE -->
