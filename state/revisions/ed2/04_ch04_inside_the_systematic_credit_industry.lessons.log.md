# Lessons Pass (Edition 2): Chapter 4

*Editor: lessons editor, Edition 2. File: `book_src/04_ch04_inside_the_systematic_credit_industry.md` (1,071 lines at start). Inputs read: `state/user_directives_ed2.md` (item 12), `state/reviews/ed2/u2_lessons.md` (lessons 1–16 and the orchestrator ruling on lesson 1), `state/reviews/ed2/u2_quality_read.md` §§(b)–(d), the Ch 1 table in `state/reviews/ed2/u2_fixes_ch01_05_06.md`, `state/cast_bible.md`, `state/style_bible.md` §8, `state/rv_thread.md`, `state/rv_pair_book.md`. Verify report carries `STATUS: COMPLETE`. Line numbers (L) refer to the file at the start of this pass; every edit re-greps the quoted phrase first.*

## (a) Metric, before

`python3 tools/prescriptiveness.py --pre 9ac1c379053d9d0254e9d524d9a40efdec4a2c71 book_src/04_ch04_inside_the_systematic_credit_industry.md`

| ver | words | bullets% | modal | imper | rule | dialog | mathgently | seat |
| :-- | --: | --: | --: | --: | --: | --: | --: | --: |
| pre (Ed 1) | 12,571 | 18.1 | 2.4 | 2.0 | 1.1 | 8.0 | 0 | 0 |
| before this pass | 35,365 | 4.6 | 2.1 | 1.0 | 1.2 | 7.9 | 20 | 4 |

Growth 35,365 / 12,571 = **2.81×** against the 1.6–1.9× target (20,114–23,885 words). Heaviest sections (awk): §4.7 4,535; §4.5 4,488; §4.8 4,103; §4.1 3,801; §4.6 3,410; §4.3 3,299; cold open 2,102. Per the orchestrator ruling on lesson 1, the band measures duplication: the merges below retire second, third and fourth tellings; no single-telling scene, sourced case or protected item is cut to chase the number.

## (b) Duplication: a new scene or box retelling what older text still states

- [ ] B1. Man's 30%/60% → over 90% electronic told four times: §4.3 L216 (verbatim quote), Source Extraction L680, L726 ("The real firm in this story..."), Trend Watch L738. Survives: the extraction and the Trend Watch (protected); L216 keeps the "tipping point / best execution" quote and points to §4.7; L726 keeps only its new p.5 quotes.
- [ ] B2. Man's 2021 PT year and H1 2022 cost spike told in the case-study intro L678 and again in the scene L694–698 (ETF baskets, balance sheet). Survives: the scene; L678 becomes one framing sentence.
- [ ] B3. Man's four routing scores told four times: Ines's card L654, annotation L682 (protected), Ines again L684, hand history L708. Survives: L654 and the annotation; L684 deleted; L708 points to the card.
- [ ] B4. "Cost is a state, not a parameter" told four times: annotation L650, L672 (with Barclays 1.15%/0.64% repeated from L666), L724 ("The first is..."), coda L732. Survives: annotation and coda; L672 deleted; L724 keeps only the line-by-line (4.6) point, as Theo's recognition.
- [ ] B5. Truncation bias told three times: box L419 (0.027σ, 4%, 11bp), L421 (same setup, same numbers, 1.3% a year), Full Derivation L427/L439 (setup and 11bp again). Survives: box (picture) → one-line statement → derivation; L421 keeps only the leg-asymmetry point; derivation ends at 0.027σ.
- [ ] B6. Pure-noise swap told three times: z-score box L577, L579, derivation L589 (60bp, 50bp, 11.5%, 1.4% each time). Survives: L579 and the derivation; box retired under D1.
- [ ] B7. Two-haircuts box L664 computes 4% / 40bp → 5 turns, which L668 computes for the momentum tilt. Survives: L668; box deleted (D1).
- [ ] B8. Capacity-hill box L761 quotes the worked example's \$1.85bn / 40bp / \$134mm (L777). Survives: the worked example; box merged with L753 and given its own numbers (D1).
- [ ] B9. Capture-ratio box L866 quotes 0.91 / 2.1bp that the BlackRock annotation L878 derives. Survives: the annotation; box gets its own numbers.
- [ ] B10. Recall and flag rate argued in L880 and again in box L882. Survives: L880 with the box's 1,800 / 30 / 300 / 23 example folded in; box retired (D1).
- [ ] B11. Contrarian rebalancing as a same-day crowded trade told at L884 and L896. Survives: L884; L896 deleted.
- [ ] B12. DTS edges told four times: Ben Dor annotation L551 (both edges), L555, scene L557 (tight edge), L559 (distressed edge, near-verbatim of L551). Survives: annotation and the L557 scene; L555's "it adds" sentence moves to L547; L559 becomes one Theo line.
- [ ] B13. Nuveen's breaks told at annotation L606 (YTW optionality; BB mix 37% → 51%), L612 (Q-measure gives zero), then L632–634 again. Survives: annotation and L612; the transparency and moving-lamppost repair join Theo's 13-week beat (L614); L632–634 deleted.
- [ ] B14. Value identity's breaks: L319 (risk premium loses in a widening), the distributor scene (the clip), then L355–357 ("It breaks in three places"). Survives: the scene, extended by one beat (C5).
- [ ] B15. Friday meeting's three spec lines told in the scene L521 and again as a numbered list L525–527. Survives: L521; list deleted; L523 keeps the competitive-frontier reading.
- [ ] B16. Bond A computed twice: P/Q box L311 (380bp, 2.5%, 0.6 → 6.3%, 230bp) and the worked example L321. Survives: the worked example, told as Theo's and Kaz's two numbers; box demoted (D1).
- [ ] B17. Effective breadth 1,800 → 960 computed in the variance box L253 and in the worked example L265; the design-effect box L263 names the factor a third time. Survives: the worked example; merged box gets its own numbers; design effect becomes a gloss.
- [ ] B18. ROBO's 47 bonds told at L809 and retold at L818. Survives: L809; L818 opens with the moment.
- [ ] B19. Body Spec bullets L811–816 (Units, Shapes, Guards, Sanity asserts) duplicate the Debrief's Spec L1017. Survives: the Debrief Spec, with the missing shapes, floors, `np.minimum.reduce` and the α(A→0) and market-value-weight asserts merged in; body bullets deleted.
- [ ] B20. Ares/BlueCove told three times: Seat box L127, timeline bullet L915, prose L937. Survives: the Seat box; L915 a dated one-liner with sources; L937 keeps "two platforms, five years apart, bought rather than built".
- [ ] B21. KMV → DCI → Blackstone facts told in the timeline L910–914 and retold in the story L927–935 (Moody's 2002, DCI 2004 with Solo, \$7.5bn, 40% / 85%, \$443.0bn 10-K). Survives: the timeline for dates and sizes; the story keeps Mags's fax, the interpretation and Theo's reading.
- [ ] B22. "How a systematic desk reads it" L939 tells engine / distribution / data a third time (story; insurer Seat L941). Survives: story and Seat; L939 cut to the A* sentence.
- [ ] B23. Merton told three times: annotation L904, box L906, story L927. Survives: annotation and story; box becomes a gloss inside the story (D1).
- [ ] B24. Cost-function box L646 retells the menu/kitchen metaphor of L638 and the cold open. Survives: L638; the box's 50bp becomes Ines's line (D1).
- [ ] B25. Man's \$2.0 → 3.1bn / \$19.8 → 37.5bn: Trend Watch L188 and Theo's scene L192, with the Trend Watch's "What it means" making Mags's point first. Survives: both (Trend Watch protected); Trend Watch moves to the end of §4.2 so the scene tells it first (D3).

## (c) Templates (lesson 4) and detached judgment paragraphs (lesson 5)

- [ ] C1. L69, "Theo can do six things... He can... He can..." (a syllabus in costume). Cut to two sentences; the Debrief bullets and the new Finder carry the outcomes.
- [ ] C2. L99–103, "two things... First,... Second,...". Recast without the ordinals.
- [ ] C3. L196, five ranked answers ("The best supported... The second... The fifth"): a table in costume. Give a five-row table; dramatize the yield row with Mags.
- [ ] C4. L281–291: "wrong in three instructive ways", "A seasoned risk manager's first question", detached L291. Ines owns the stressed-ρ question; L291 becomes a Finder row; heading retitled to the scene.
- [ ] C5. L353–357, "When the value identity works... It breaks in three places... an experienced PM". Replace with a ~150-word beat after the distributor: Kaz prints the top twenty, Ines asks for the worst months, Mags names the volatility-as-PD trap; heading deleted.
- [ ] C6. L553–559, "When DTS is the right ruler": scene kept; "The check an experienced risk manager runs first" cut; heading retitled (with B12).
- [ ] C7. L591–597, "When headroom helps": near-miss scene leads, slow and event clocks become Ines's line, "The first question to ask" cut; heading retitled.
- [ ] C8. L630–634, "When the identity works... It breaks in three places... a seasoned allocator checks first": deleted (B13).
- [ ] C9. L670–674, "When break-even turnover is a ceiling... The check an experienced PM runs": L672 deleted (B4); L674's involuntary turnover becomes Mags's beat; heading deleted.
- [ ] C10. L724, "Two things... The first... The second...": one line (B4).
- [ ] C11. L771–775, Ines's "The first question... The second question... The third question": keep the scene, drop the ordinal frame.
- [ ] C12. L789–791, "The first is... The second... The third..." and "The question an experienced risk manager asks": a three-row table of Ines's series; the exit-days question becomes hers.
- [ ] C13. L892, "a good first question to ask... The first is... The second is...": Theo counts BlackRock's down months; heading retitled; L896 deleted (B11).
- [ ] C14. L939, "Three things... The first... The second... The third...": B22.
- [ ] C15. Listing explanations L818–852: "Use it to/for... Do not mistake... The edge that bites" ×4 (lesson 12). Open each with the chapter's moment; keep the content, drop the template phrases.

## (d) Boxes (lessons 6–8, 10)

- [ ] D1. 20 Math, Gently in 35,365 words (limit 10, at most one per 1,200 words, never two adjacent); ten are second tellings of boxes in Ch 1, 1-B, 2, 3 and 3-B. Keep 8: L249+L253 merged (sqrt-N recalled from Ch 3-B in one sentence; thermometers, own numbers); L415 sealed envelope; L419 trimming a tail (bell intro cut to a pointer); L505 432 tickets (audit numbers left to Friday); L565 optimizer; L610 leash (random-walk half cut to a pointer to Ch 3-B); L753+L761 merged (square root; the hill in miniature, own numbers); L866 capture ruler (own numbers). Demote to glosses with pointers: L263 design effect; L311 two measures (Ch 3-B); L331 handicap (Ch 3-B, Ch 8); L537 points or percent (Ch 1 §1.4); L577 z-score (Ch 3); L646 cost function (Ines); L805 three ceilings (prose); L882 recall (Ch 3, §7.5); L906 Merton (Ch 1 §1.5, Ch 6). Delete L664 (B7). Vary the "The full version is" sign-offs.
- [ ] D2. Adjacency and runs: L646 + L648 + L652 is three boxed elements in a row (fixed by D1); L415/L419 one line apart (move the envelope above its equation, lesson 10); L753/L761 (merged); L797 + L805 and L902 + L906 (fixed by D1).
- [ ] D3. Lesson 8: §4.2 Trend Watch L179 sits before the scene that uses its numbers. Move it to the end of §4.2; rewrite L192's "the Man line" so the scene stands first.

## (e) Research-note leaks and fiction labels (lesson 13)

- [ ] E1. Trend Watch L183, "(per press reports, IFR, c. early 2022; date unconfirmed)": hedge as "(as reported by IFR in early 2022)"; log the open item in `state/open_items_ed2.md`.
- [ ] E2. Table L94, "no public source for a pod's credit book was found"; L229, L231, L232 "Silent (none found)"; L96 "(approx.; aggregator data: stockanalysis.com)". Reword as reader-facing hedges.
- [ ] E3. L133 Quant-Shop Life label calls the setting a different firm, yet Theo (third week) is in it and §4.3/§4.5 call it the desk's own. Relabel to the desk's own report, naming what is invented.
- [ ] E4. L557 tight-decile numbers (60bp, 10bp) lack "(illustrative)".
- [ ] E5. Resource Graph "(title only)" ×3 (L1033, L1034, L1047): Edition 1 text, diffed identical by the verifier; left for U3, not edited here.

## (f) Finder table and headings (lesson 11)

- [ ] F1. Add a ten-row Finder table (concept · eq. · intuition (box) · judgment (scene) · code) at the top of §4.12, before the six o'clock scene.
- [ ] F2. Promote the decision points L517 and L714 to `####` headings; retitle the surviving "When ..." headings as scenes (breadth engine, tight decile, exchange-offer near miss, seventy-two down months, three measured series).

## (g) Cast bible

- [ ] G1. June 2022 hand history L690–722 has Kaz and Mags arguing *in* June 2022 ("Before Kaz trusted me"; "Kaz, in June 2022, had done"; "'Pay it,' Kaz had said"; Mags "she said"), but Kaz was in a postdoc until 2023 and on the desk by Jan 2025, and Mags reached this desk in 2023. Make it a replay: Ines cuts the file at the June 2022 quotes and Kaz and Mags argue it blind now; Ines's 2022 decision stays hers.
- [ ] G2. L483, "Two years ago, building the vendor panel, Kaz winsorized" (autumn 2024) sits at the edge of Kaz's start. Change to "last year".
- [ ] G3. L921, Mags's EDF fax "Mid-nineties" against the canonical 1996 start. Change to 1997, her second year.
- [ ] G4. Add to `state/cast_bible.md`: Ines's November 2008 dealer seat (cold open) and her June 2022 rebalance file (replayed); Mags's autumn-1998 telecom fade and 1997 EDF fax; Kaz's 3.1 → 0.9 backtest and 2025 vendor panel; Theo's retailer and distributor (fictional composites, generic work).

## (h) Relative-value beat

- [ ] H1. `state/rv_thread.md` assigns Ch 4 a scene in §4.1 (fee waterfall, T12). Present at L105–123 (Dov's PB-01 at Ch 1-B sizes, Mercer's 20-gross-for-10-net, pay per pod and risk per fund, the corner, figure placeholder). Ch 4 opens, stresses and closes no pair, so `state/rv_pair_book.md` needs no row change. Verify only; nothing to write.
