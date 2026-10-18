# Lessons Pass, Edition 2: Chapter 3

*Lessons editor pass against `state/reviews/ed2/u2_lessons.md` (including the orchestrator ruling on lesson 1: the band measures duplication, not length), run 2026-10-18 on `book_src/03_ch03_pjt_rssg_cognitive_bridge.md` (918 lines). Verify log is COMPLETE. Line numbers are the file as of the audit; re-grep the quoted phrase before each edit.*

## Audit

### (a) Metric

- [x] A1. **Before** (`python3 tools/prescriptiveness.py --pre 9ac1c379053d9d0254e9d524d9a40efdec4a2c71`): pre 15,028 words, bullets 17.3%, modal 4.1, imper 1.5, rule 0.8, dialog 6.9, Math Gently 0, Seat 0. Now 35,183 words, bullets 7.1%, modal 3.7, imper 1.3, rule 0.8, dialog 6.8, Math Gently 15, Seat 3. **Growth 2.34×** against the 1.6–1.9× band (24,045–28,553 words). Per the orchestrator ruling, cuts below come only from duplicate tellings, templates and the box budget; single-telling scenes and protected items stay. *Done: before metric recorded; growth 2.34x against the 1.6-1.9x band.*

### (b) Duplication (new telling vs old telling, and which survives)

- [x] B1. Moyer's 85 = 100p + 60(1−p) → 0.625 and the ℚ-not-ℙ point: L45 box and L51 annotation (and the extraction itself). **Survivor:** extraction + annotation; L45 becomes a gloss (D1). *Done: box now two-sentence gloss; annotation keeps 0.625 and Q-point.*
- [x] B2. "93% of the variance is which hump": L75 box and L86. **Survivor:** L86; box becomes a gloss (D1). *Done: zoo box now one-sentence weather gloss; L86 keeps 93%.*
- [x] B3. Markout +146bp (85.75 → 87): L254 box and L264. **Survivor:** L264. *Done: bp box now one-line gloss; definition keeps +146bp example.*
- [x] B4. The Brambleworth hand (6 points, CDX 20bp, Treasuries 10bp, β 1.3, 0.48 and 5.5): L288 box and L320 "The hand, replayed". **Survivor:** L320; box becomes a gloss with no hand numbers. *Done: beta box now harbour gloss; hand numbers live in replay.*
- [x] B5. Shrinkage numbers (150bp, 20bp, 56.25, +300 → +5bp, 56 fills): L300 box solves Exercise 6(b) (lesson 7). **Survivor:** Exercise 6; the box gets its own numbers. *Done: box uses 120bp, 30bp, four fills; Exercise 6 untouched.*
- [x] B6. Half-life crossover (0.10/3 days vs 0.04/120 days → 4.1 days): L551 box solves Exercise 4(b). **Survivor:** Exercise 4; box becomes a gloss pointing to it. *Done: half-life box now coffee gloss pointing to Exercise 4.*
- [x] B7. Small-π asymmetric GM and "coin flip the ex-RSSG banker flags": L146 and L175–181. **Survivor:** the Full Derivation; L146 becomes a one-line pointer. *Done: L146 cut to one-line pointer to the asymmetric derivation.*
- [x] B8. "Translating the hazard move into a spread move requires leaving ℙ" (L477 and L491) and the lazy κ = 1 sentence (L481 and L497, plus "Say this explicitly in every spec"). **Survivor:** one statement with the two-line derivation inline right after (3.3); the "Full Derivation: from a filing to a spread move" heading retires (lesson 10). *Done: one statement, two-line derivation inline; heading and duplicates retired.*
- [x] B9. Elkan is the (3.3) update applied to a whole model, shortcut is first-order: L509 and L523. **Survivor:** the Full Derivation; L509 deleted. *Done: L509 duplicate deleted; Full Derivation keeps the Elkan argument.*
- [x] B10. CUSUM's "two properties" (L615) restates L639 and the box's eight days. **Survivor:** the Full Derivation, moved directly under (3.5); L615 deleted. *Done: properties paragraph deleted; Full Derivation now directly under (3.5).*
- [x] B11. SVB buyers "in the 30s", PIMCO/Centerbridge/Davidson Kempner and PJT: coda L418, Ines L426, Seat box L531. **Survivor:** the coda; the Seat box points back to it. *Done: Seat box points to the coda; quotes and fund names once.*
- [x] B12. SVB 8-K items, \$23.97bn → \$21.45bn, 22 March Item 2.04: coda L418 and §3.4.1 L446. **Survivor:** coda for the numbers; L446 keeps only the item-sequence reading. *Done: rows paragraph keeps item sequence; dollar figures left to coda.*
- [x] B13. WaMu par-plus-interest 2012 and the 7 Nov 2024 stock-and-units plan: L102 and Mags L386 / coda L422. **Survivor:** Mags and the coda; L102 points forward. *Done: L102 points forward to Mags and the coda for WaMu.*
- [x] B14. Serta: the flow signature (Theo L681, then "*The flow.*" L703); the 45/25/70% prior (card L689, then "*The quote.*" L705); the \$403mm (L695 and L725). **Survivor:** Theo's line, the decision card and the L695 arithmetic; L703, L705 and L725 point back. *Done: card states prior; flow, quote, award paragraphs now point back.*
- [x] B15. σ_V units told five times: L185 (Units), L236 ("State loudly, in every spec"), schema L751, Listing 3.1 edge case L768, Spec item 2. **Survivor:** L185 and the Spec; L236 and L768 become pointers. *Done: L236 rewritten as plain statement pointing to Units and Spec.*
- [x] B16. Two "Spec You Hand the Robot" (§3.8 L739 and Debrief L867), and "What the coding agent must not do" (L832) restating the Debrief Spec's "Do not" item for item. **Survivor:** Debrief Spec; L739 retitled "What ROBO built from the vague version"; L832 deleted (lesson 11). *Done: body paragraph retitled ROBO vague version; must-not paragraph deleted.*
- [x] B17. Block openers L762, L774, L786, L810, L822 restate the motivations §3.8's intro (L735) already ties to each scene. **Survivor:** L735; each opener cut to the moment in one or two sentences (lesson 12). *Done: five block openers cut to the scene moment, one sentence each.*
- [x] B18. Syllabus L37 ("By the end of this chapter you will be able to: ...") repeats L35's roadmap and the Debrief bullets. **Survivor:** L35 and the Debrief; L37 deleted. *Done: syllabus paragraph deleted; roadmap and Debrief bullets carry outcomes.*
- [x] B19. Runway column name: the vignette ships `liq_runway_wks_pit_v1` (L114) but the Debrief (L856) says `liquidity_runway_weeks`. Debrief takes the shipped name. *Done: Debrief now names the shipped liq_runway_wks_pit_v1 column.*

### (c) Templates (lesson 4) and detached judgment paragraphs (lesson 5)

- [ ] C1. L100 "When the horizon approximation works, and when it breaks" ("It breaks, first... second"; "A seasoned trader checks the calendar first"): the cold open and L98 already show Ines asking about the calendar; stale mids are §3.3's subject. Delete; judgment to a Finder row.
- [ ] C2. L248 "When the Glosten–Milgrom bid works, and when it breaks" ("It breaks in three recognizable ways"; "A seasoned trader asks three questions"): the insurer Seat box carries the relationship client, the Man annotation carries auto-responders. Baldauf–Mollner and the Tradeweb paper move into Ines's "eight dealers" beat in §3.2.2; paragraph deleted; Finder row.
- [ ] C3. L346–348 "#### When markouts work, and when they break" ("They break in three places"; "checks three things in order: first..."): the Tuesday vignette and the Ways box carry staleness and footprint; protocol contamination goes to the §3.2.2 beat. Delete heading and paragraph.
- [ ] C4. L525–527 "#### When the 8-K update works, and when it breaks" ("It breaks, first... second"; "A seasoned reader asks one question"): cleansing survives in §3.6.3 (Wolfspeed, L653, whose pointer is reworded); ratings conditioning survives in "Where the edge is" and the Trend Watch. Delete heading and paragraph.
- [ ] C5. L629 "When the detector works, and when it breaks" ("It breaks, first/second/third"; "a seasoned user checks three things"): the majority-already case becomes a short Ines–Kaz exchange in the Saks scene; co-op silence survives in Serta's counter-technology (L717); the desk's own flow survives in the Debrief's ROBO story. Delete; Finder row.
- [ ] C6. Six listing closers in the U1 template ("Use it as/for... Do not read it as... The edge case that bites": L768, L780, L792, L804, L816, L828). Recast keeping every fact; point to the scene where one already shows the edge.
- [ ] C7. L51 Moyer annotation "Three things the 2026 desk adds. First... Second... Third": recast without enumerators, content kept.
- [ ] C8. L559/L565 "Two practical consequences follow. First, ..." / "Second, ...": recast as narrative links.
- [ ] C9. Ines's seven-field walk (L200–216) is a table in costume: give the seven features as a table (every citation kept: Easley–O'Hara, Pintér–Wang–Zou, Wei–Zhou, Di Maggio–Kermani–Song, PRS Chapter 13) and dramatize the clock, the counterparty and the eight-dealer rows.
- [ ] C10. Prescriptive one-liners: L236 "State loudly, in every spec" (B15); L448 "Two warnings belong in every parser spec"; L601 "Notice what the dealer should and should not do"; L625 "Error-prone spots" (a list in prose). Recast.

### (d) Boxes (lessons 6–8, 10)

- [ ] D1. Fifteen Math, Gently against a cap of ten and one per 1,200 words; clusters at L45/L55, L75/L90, L254/L288/L300 (three in ~700 words), L454/L479/L501 (three in ~900 words). Nine are not first load-bearing uses and become one-to-three-sentence glosses keeping the picture, with pointers: distribution and risk-neutral (L45; §1.3.1, §1.5), shapes (L75; §2.2.2, Ch 5), random walk (L90; §1.5, §6.1.1), odds (L191; §1.3.3), bp of price (L254; §1B.4, Ch 4-B), beta (L288; §1B.2), exponential clock (L454; §1.5), ℙ vs ℚ (L479; §1.5, §5.1.1), half-life (L551; §1.8.1). Keep six: variance (§3.1.1), conditioning on a trade (§3.2.1, trimmed to defer the odds arithmetic to §1.3.3), winner's curse (§3.2.3, pointer to §2.3.2), shrinkage (§3.3.4, new numbers), base rates (§3.4.3), two bells (§3.6.2). Fix every reference to a retired box.
- [ ] D2. Sign-off tic on the kept boxes ("The full version is..."): vary; say "next" where it is next.
- [ ] D3. Runs of more than two boxed elements: §3.2.3 Poker Table → Trend Watch → Man extraction (L240–244). Move the Trend Watch to the end of §3.2.3 and thread a line of narration before the Man extraction. Script-check every run after the edits.
- [ ] D4. Trend Watch placement (lesson 8): the 8-K token Trend Watch (L529) sits under a judgment heading → end of §3.4.2 after "Where the edge is", with the SVB distressed-fund Seat after it; the §3.6.2 Trend Watch (L627) sits mid-section → end of §3.6.2.
- [ ] D5. Derivation order (lesson 10): §3.6.2 Full Derivation moves directly under (3.5) and "The prior" gets its own `####` heading; §3.4.3 runs box → (3.4) → extraction → Full Derivation.

### (e) Research-note leaks and fiction labels (lesson 13)

- [ ] E1. L422 "*(the syndicated copy of that report is unclear on the exact wording)*": hedge the sentence ("press reports put...") and log the open item in `state/cleanup_queue.md`.
- [ ] E2. L715 "*(the summary we have does not reconcile those percentages with the \$186mm figure...)*": cut the \$62mm–\$94mm range, keep the 29–43% and the tenth-of-the-position conclusion; log the open item.
- [ ] E3. L703 "(the event study is on the Edition 2 list)": production note in book text; cut and log.
- [ ] E4. L585 "as summarized in the sources cited" → plain source line; L661 "as summarized by Mayer Brown" → "as reported in Mayer Brown's July 2026 note".
- [ ] E5. Fiction labels: the cold open's label sits mid-paragraph (L5) → italic at the top; Serta's second label (L721) is a duplicate → delete; Serta's top label names Mags's position (G4). Re-grep for "CHECK", "secondary", "search" after edits.

### (f) Finder table and headings (lesson 11)

- [ ] F1. §3.9 has bullets and the Spec but no Finder: add a ten-row table at the top (concept · equation · intuition · judgment · code), carrying the judgments retired in C1–C5 once.
- [ ] F2. Promote scenes and decision points: "## Cold Open" heading (Ch 5 precedent); `####` decision points for SVB (9:02 a.m., 13 March 2023), Saks (last week of May 2025) and Serta (2:40 p.m., 19 June 2020).

### (g) Cast-bible contradictions

- [ ] G1. L9 "three years at PJT RSSG" → six (C3).
- [ ] G2. L23 Mags "since the bonds came with coupons you could physically clip" → cut (C5: started 1996).
- [ ] G3. L23 the seller "Steve" → "Stan" (C12: Steve is the dealer); L573 "Steve's card" → "Stan's card".
- [ ] G4. L673 Mags "at a fund she does not name, she held a loan that was left outside a deal like this one" → C4 canon: fifteen million of this first lien on a bank's book, left outside on 22 June 2020 (outside holder, illustrative; Ch 1 and Ch 14 tell it).
- [ ] G5. L717 co-op counter "1" → "0" (C6 canon; supersedes the brief's "stays at 1").
- [ ] G6. Story clock: the SVB drill on Theo's "third Saturday" (10 Oct) precedes the Brambleworth Friday (16 Oct, C10), yet the Debrief treats SVB as the lesson after Brambleworth → the fourth weekend, the Saturday after Brambleworth (17 Oct; Monday drill 19 Oct); "first moment in three weeks" → "four weeks".
- [ ] G7. Add Ch 3's facts to `state/cast_bible.md` (Theo six years; Stan; Mags's Serta canon applied in Ch 3; counter 0; SVB drill dates; Ines's 36 covered).

### (h) Relative-value beat

- [ ] H1. `state/rv_thread.md` now exists (it appeared during this pass). Its Pair Book assigns Ch 3 the opening of **PB-06** (Serta first-lien / second-lien term loan, 19 Jun 2020 blotter, long the fulcrum, short the junior, recovery-weighted market value, outside-holder) and the foreshadow of T7 (seniority is a document variable). The chapter has no RV beat. Write a `> **The Pair.**` box in §3.7 after Ines's "afterwards when" (Theo's RSSG instinct as a pod trade; what the hedge removes, what remains, what leaks: the window), and record PB-06 as opened in `state/rv_pair_book.md`.

### (i) Close

- [ ] Z1. Re-run the metric, record **after**, re-check box spacing, runs and `$$` balance.

## Fix notes
