# Lessons Pass (Edition 2): Chapter 13

*Editor: lessons editor, Edition 2. File: `book_src/13_ch13_codifying_lmt_game_theory.md` (1,019 lines at start). Inputs read: `state/user_directives_ed2.md` (item 12), `state/reviews/ed2/u2_lessons.md` (lessons 1–16), `state/reviews/ed2/u2_quality_read.md` §§(b)–(d), the Ch 1 table in `state/reviews/ed2/u2_fixes_ch01_05_06.md`, `state/cast_bible.md`, `state/style_bible.md` §8. Verify report carries `STATUS: COMPLETE`. Line numbers below refer to the file at the start of this pass; every paragraph is one line, so re-grep the quoted phrase before editing.*

## (a) Metric, before

`python3 tools/prescriptiveness.py --pre 9ac1c379053d9d0254e9d524d9a40efdec4a2c71 book_src/13_ch13_codifying_lmt_game_theory.md`

| ver | words | bullets% | modal | imper | rule | dialog | mathgently | seat |
| :-- | --: | --: | --: | --: | --: | --: | --: | --: |
| pre (Ed 1) | 12,505 | 8.0 | 2.5 | 1.4 | 1.0 | 10.4 | 0 | 0 |
| before this pass | 32,426 | 3.9 | 2.3 | 1.0 | 1.2 | 10.8 | 14 | 3 |

Growth 32,426 / 12,505 = **2.59×** against the 1.6–1.9× target (20,008–23,760 words). Heaviest sections (tool count): §13.5 3,717; Serta §13.3.1 3,478; §13.4 2,984; Trinseo §13.7.1 2,469; §13.8 2,142 plus its Spec/listing prose 1,904; §13.2 2,007; §13.9 1,967; cold open 1,548. The merges below retire duplicate tellings; no topic is cut.

## (b) Duplication: a new scene retelling what an older paragraph still states

- [x] B1. Cold-open seat walk (L27–47) vs Poker Table L456, which retells the three sellers ("A seller who got a seat doesn't sell at 78..."). Survives: cold open (seat two stays dramatized; seats one and three compressed). Poker Table keeps the dealer line and the hand history. **Done:** Seat one compressed; Poker Table keeps dealer line and hand history.
- [x] B2. CLO told four times: cold open L43 (7.5% CCC, lowest-market-value haircut), L313 (LCM lenders are CLO vehicles), CLO seat box L341 (both again, parked mid-Serta between the unblending table and the decision), L420 (CLO expensive; appellants). Survives: cold open for the bucket, L313 for LCM, box for the vehicle's rulebook. Move the box to §13.4 after L420 and strip its repeats; L420 points to the box. **Done:** CLO box moved after Figure 13.2; repeats now point to 7:41.
- [x] B3. Serta losing bidders: L313–315 (Ines: "They were the other bidder") vs L424 (auction section restates it from the opinion). Survives: the scene; L424 becomes a one-line pointer. **Done:** Auction paragraph now points to Ines's 'other bidder' reading in §13.3.1.
- [x] B4. "Who advised the losing group?": Theo says it at L355; L383 gives the same line to Mags as "her own first check". Survives: Theo's L355; L383 retired with C5. **Done:** Mags's duplicate 'who advised the losing group' paragraph deleted; Theo's stays.
- [x] B5. Mitel's same-day ruling told three times: L163 (Family 3, with the quotes), L361 (Serta beat IV), L919 (§13.9). Survives: L163, plus Ines's scene line L375; L361 drops the sentence; L919 points back. **Done:** Mitel sentence cut at Serta IV; §13.9 points back to Family 3.
- [x] B6. Box L254 walks slice → call spread → digital; L258 restates the same shape in prose. Survives: the box; L258 cut to the one line that introduces the approximation. **Done:** Shape restatement cut to one line introducing the digital approximation.
- [x] B7. L369's last sentence ("a put that a court can exercise for you, years later, with 9% interest") vs L377 ("a second option struck at the courthouse ... accrued 9% a year"). Survives: L377 (scene close); L369 sentence cut. **Done:** Trough-put sentence cut; the scene's courthouse option at L377 survives.
- [x] B8. Kaz's 25-versus-99 question answered at L87 (half, deferred), L500–502 and Debrief L953. Survives: L87, L500, Theo's L504 line and the Debrief; L502 retired. **Done:** Duplicate 25-versus-99 answer paragraph retired; Theo's drawer line carries it.
- [x] B9. L492 "Mags was right about the mechanism" restates Mags's L476. Survives: L476; L492 keeps only the new facts (no suit reported; "difficult"). **Done:** Mechanism paragraph keeps only no-suit fact and 'difficult' quote.
- [x] B10. Antitrust mechanism told twice: L542 ("voids the no-separate-deal covenant ... reverts to the §13.4 auction") and Ines at L548. Survives: Ines; L542 keeps Wachtell and Seaton; L552 trimmed to the new parameter point. **Done:** Mechanism left to Ines; Wachtell, Seaton kept; L552 one sentence.
- [x] B11. Wesco/Incora told four times: L446 (Mayer Brown account of the vote dilution, \$250mm, lien release), the §13.9 scene L868–894, L900 (restates the dilution in prose), Docket Diary L902; the 85-to-par run appears at L454 and again at L868; L894 repeats Diary dates. Survives: the §13.9 scene and Diary, L454 for the price run. L446 becomes one sentence and a pointer; L900 keeps only the $g$ arithmetic; L868 points to §13.4; L894 drops what the Diary holds. **Done:** Levers, steps-versus-plans, scene and timeline now point to one telling each.
- [x] B12. Fixed point told three times: Kaz's column (L657–661), L669's slope sentences, box L671 (slope 0.5 again). Survives: the column and the box; L669 keeps the formula and a pointer. **Done:** Slope restatement cut from L669; trimmed box ends with 'next'.
- [x] B13. Trinseo: L723–727 build the revolver, the \$1,508mm note and the upstairs value on the whiteboard; L729 relists all three; L741's Exercise 4 sentence repeats L727. Survives: the scene; L729 keeps the multiple-instability point; L741 sentence cut. **Done:** L729 keeps instability point only; repeated Exercise 4 sentence removed.
- [x] B14. The Eisenberg–Noe pass is described at L673 and again in the listing prose at L828. Survives: L673; L828 points to it. **Done:** Listing prose points to §13.7's loop; keeps only reduce_by detail.
- [x] B15. Roe–Rotaru's 89 told at L133, L759, L774 and L848. Survives: L133 (box) and L759 (scene); L774 and L848 say "the 89". **Done:** L774 and L848 now say 'the 89'; box and scene keep sources.
- [x] B16. Theo's 13-week model as covariate: L213 (canonical PRS-runway beat), L798, L824, L850, L966. Survives: L213 and the Debrief bullet; L798 points back; L824 and L850 drop the gag. **Done:** Three gag repeats replaced by pointers to the §13.2.1 runway beat.
- [x] B17. Moyer p.85 annotation L404 restates the L131 annotation (selective coercion; "invitation probability"). Survives: L131; L404 keeps its p.85 point (the holdout runs the opposite way) and points to §13.1. Extraction text untouched. **Done:** Annotation trimmed to holdout reversal; points to §13.1 invitation probability.
- [x] B18. Two Specs: §13.8 "Specification for AI Implementation" schemas/edge cases/stability (L822) and the Debrief's "The Spec You Hand the Robot" (L971). Survives: the Debrief Spec, with L822's schemas, edge cases and stability merged in; §13.8 keeps the ROBO vignette and the listing prose with a pointer. **Done:** Schemas, edge cases, stability merged into Debrief Spec; body copy deleted.
- [x] B19. Vintage break told at Trend Watch L379 (protected), Bohn–Stein annotation L784 and PRS judgment L796. Survives: both boxes; L796 points to the annotation (done with C8). **Done:** L796 rewritten as Ines's ranking-versus-level line; vintage points to annotation.

## (c) Templates and detached judgment paragraphs

- [ ] C1. L75 "By the end of this chapter you will be able to: ..." (a syllabus). Replace with two sentences that point to Theo's four-factor sheet at 4:50; pose the 7:41 decision as a card at L71 (lesson 9).
- [ ] C2. L103 "Two facts make this useful. First, ... Second, ..." Recast without enumerators.
- [ ] C3. L155 "three questions ... First: ... Second: ... Third: ..." (a table in costume). Dramatize the denominator row only; the amend-the-amendment and lien-release rows become rows in the §13.2.1 feature table.
- [ ] C4. L185 annotation "Two modern departures matter. First, ... Second, ..." Recast (annotation only; extraction untouched).
- [ ] C5. L381 "When to reach for the digital put, and when it breaks" and L383. Delete: the large-minority break is L291's three regions, $\kappa$ is L274, the sale is Boardriders (§13.1) and Lumen (§13.5), lien restoration is Incora (§13.9). One Finder row.
- [ ] C6. L627 "When to reach for the capped forward ... It breaks in three ways ... A seasoned reader checks". Delete: valuation clause is L586, guarantee leverage L623, integrated steps L625; fold STG's 12 Jan 2026 filing into L625. One Finder row.
- [ ] C7. L745–747 "When the clearing engine is the right tool ... The seasoned habit". Delete; give the judgment ("it cannot tell you which one the judge picks") to Kaz in the L739 scene; the single-obligor point goes to the Finder.
- [ ] C8. L794 label "When to trust the PRS, and when not to" and L796 "three things break the level. The first ... The second ... The third". Keep Ines's mirror scene under a narrative label; L796 becomes her ranking-versus-level line with pointers.
- [ ] C9. Listing prose: L832, L844, L856 "Use it when ... Do not use it ... The edge case that bites" (×3) and openers L824, L836, L848 that retell sections. Open each with the chapter moment; state each edge case once.
- [ ] C10. L448 bold label "When the knapsack is the wrong model" → a narrative label for the Robertshaw story (content kept).

## (d) Boxes

Count: 14 Math, Gently (L101, 113, 254, 270, 400, 414, 436, 452, 516, 534, 671, 772, 776, 780) against a cap of 10 and one per 1,200 words. Clusters: §13.4 has four in about 3,000 words; §13.8 has three in about 1,500, with L772 and L776 one paragraph apart; §13.3 has L254 and L270 within 600 words. Runs of more than two boxed elements: none (maximum two: L400–402, L456–458, L514–516, L554–556); re-check after the CLO box moves.

- [ ] D1. L113 distributions/lognormal: Ch 6 §6.1.1 (and Ch 5) owns it. One-sentence gloss with the 0.6%-below-zero number and a pointer.
- [ ] D2. L270 partial expectations, ½s², risk-neutral: ½σ² belongs to Ch 5 §5.2.3 and Ch 6 §6.1, P/Q to Ch 5 §5.1.1 and Ch 6 §6.3. Fold the partial-expectation picture and its 2.3-point number into L268/L272; pointers.
- [ ] D3. L400 payoff matrix: L398 already states weak dominance. Fold the 80/60/25 number into L398; delete the box.
- [ ] D4. L414 knapsack: repeats L412. Fold greedy-overpays and the 4,096 bags into L412; delete the box.
- [ ] D5. L671 fixed points: first load-bearing use in the book (Ch 16 and 25 come later). Keep; cut the slope-0.5 restatement (with B12).
- [ ] D6. L772 hazard and Poisson clock: Ch 3, Ch 5 §5.1.5 and Ch 6 §6.1.4 own it. Gloss with the 10% → 0.105 number.
- [ ] D7. L776 logistic link: Ch 5 §5.5.3 owns the logit. Gloss with 10.0% versus 10.5%.
- [ ] D8. L780 Beta prior and shrinkage: Ch 5 §5.5.2 and Ch 3 §3.3.4 own them. Gloss with Beta(2, 38) and a thin-data pull.
- [ ] D9. L436 auction box repeats L434's Bertrand sentence; trim, and vary the sign-off. Leaves 7 boxes: L101, 254, 436, 452, 516, 534, 671.

## (e) Research-note leaks and fiction labels

- [ ] E1. L133 Desk Myth "(...; secondhand)" → "as quoted by".
- [ ] E2. L187 "a 2022 drop-down whose details we treat as illustrative" → name Envision's 2022 drop-down (on the §13.9 scoreboard).
- [ ] E3. L454 "(a secondary account; we have not seen the prints)" → "by press accounts".
- [ ] E4. L623 "*(approx.; Wikipedia, citing Reuters, the FT and the WSJ)*" → "by contemporaneous press accounts".
- [ ] E5. L888 "(by a secondary account)", "(also a secondary figure)" → "press accounts put".
- [ ] E6. L1000, L1003 "title only", "titles only" process notes removed.
- [ ] E7. Log E1–E5 in `state/research/open_items_ch13_ed2.md`.
- [ ] E8. Fiction labels at the top of each scene, in italics: cold open (Larkspur and the desk; the parenthesis moves into the italic line); replay labels for Serta (L303), Lumen (L468), Incora (L866) and Trinseo (L701; see G5).

## (f) Finder and headings

- [ ] F1. Finder table at the top of §13.10 (10 rows: transfer function, uptier put, knapsack, auction, global games, co-op Nash/Shapley, drop-down forward, double-dip clearing, PRS/EPL, steps versus plans), absorbing the judgments retired in C5–C8.
- [ ] F2. Promote scenes to headings: "## Cold Open" (Ch 5 and 6 precedent); `####` for the Serta decision (19 Jun 2020), the Lumen scene and its decision (10 Nov 2023), the Trinseo decision (24 Jun 2026), the Incora board (28 Mar 2022) and the 4:50 Debrief scene.

## (g) Cast-bible contradictions

- [ ] G1. Co-op counter (C6 canon for Ch 13 is 1, 2, 2): L464 says 2 → 1; L490 says 3 → 2; L964 says 3 → 2.
- [ ] G2. Priya as a documents analyst (C11: rename the Ch 13 analyst): rename the vignette's analyst "Noor"; move the vignette (L629, parked in the drop-down section) to the end of §13.2.1 beside `holder_hhi` (lesson 12); update the pointers at L215, L759, L796.
- [ ] G3. Kaz misreads (C7): the springing lien at L189–193 repeats Ch 3's misread → Kaz heads it off as a callback. The beta blocker at L195–203 is a second blocker misread in the chapter (the first is Ch 5's club bouncer; Ch 13 keeps the mattress protector) → cut.
- [ ] G4. Mags "In 1991 this was a steering committee" (L466) contradicts C5 (she started in 1996) → "When I started".
- [ ] G5. Story clock (C1, rule 3): Theo reads Trinseo's May 2026 disclosure statement "on Tuesday" as if live, four months before his 22 Sep 2026 Day One → label it a replay, docket cut off 24 Jun 2026.
- [ ] G6. Larkspur runway: §13.2.1 says eleven months; the listing prose (L854) scores "7 months" → reconcile in L854.
- [ ] G7. Update `state/cast_bible.md` (Noor; Ch 13 misread ledger; counter applied; Trinseo replay).

## (h) Relative-value beat

- [x] H1. `state/rv_thread.md` does not exist (only `state/rv_thread_plan.md`, which assigns Ch 13 "long the likely participant, short the likely excluded"). By the brief no item is opened; the Trinseo pair (L729, L741) stays and is noted for the RV pass. No change to `state/rv_pair_book.md`.

## Fix notes

