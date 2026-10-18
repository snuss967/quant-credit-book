# Lessons Pass (Edition 2): Chapter 2

*Editor: lessons editor, Edition 2. File: `book_src/02_ch02_revolutions_in_credit_trading.md` (951 lines at start). Inputs read: `state/user_directives_ed2.md` (item 12), `state/reviews/ed2/u2_lessons.md` (lessons 1–16), `state/reviews/ed2/u2_quality_read.md` §§(b)–(d), the Ch 1 table in `state/reviews/ed2/u2_fixes_ch01_05_06.md`, `state/cast_bible.md`, `state/style_bible.md` §8. Verify report carries `STATUS: COMPLETE`. Line numbers below refer to the file at the start of this pass; every paragraph is one line, so re-grep the quoted phrase before editing.*

## (a) Metric, before

`python3 tools/prescriptiveness.py --pre 9ac1c379053d9d0254e9d524d9a40efdec4a2c71 book_src/02_ch02_revolutions_in_credit_trading.md`

| ver | words | bullets% | modal | imper | rule | dialog | mathgently | seat |
| :-- | --: | --: | --: | --: | --: | --: | --: | --: |
| pre (Ed 1) | 14,619 | 6.6 | 1.6 | 1.1 | 1.6 | 5.9 | 0 | 0 |
| before this pass | 31,789 | 1.0 | 1.8 | 0.9 | 1.1 | 8.1 | 12 | 4 |

Growth 31,789 / 14,619 = **2.17×** against the 1.6–1.9× target (23,390–27,776 words). Heaviest sections (awk count): §2.9 6,972 (incl. Spec prose ~2,600); §2.3 4,559; §2.2 4,446; §2.7 3,727; §2.6 3,076; cold open ~2,000. The merges below retire duplicate tellings; no topic is cut.

## (b) Duplication: a new scene retelling what an older paragraph still states

- [x] B1. Cold open: Mags's "seventy-five minutes / about five hundred bonds" told twice (L9–13 and L31). Survives: L31 (after Kaz's Rule 6730); L11–13 cut, L9 keeps the Steve line. **Done:** One telling after Rule 6730; casino line folded into it.
- [x] B2. Censoring told four times: box L154, Ben Dor annotation L158 ("neither drop it nor treat it as equal to the cap"), L160 ("biases turnover down, by the area under ... tail"), derivation L182 (same sentence verbatim). Survives: box (picture) and derivation; L158 keeps the cap/ticket-size facts; L160 becomes a one-line bridge. **Done:** Annotation points to the scale; bridge cut to one sentence.
- [x] B3. Pareto arithmetic told three times: distribution box L168 (5/3 → 12.5, 4/3 → 4), Kaz L170, derivation L202. Survives: Kaz L170 (scene) and derivation. Box retired under D2. **Done:** Box retired; Kaz's paragraph and derivation carry the arithmetic.
- [x] B4. Riskless-principal echo: Ways This Blows Up L206 (MarketAxess 8% June 2026, affiliate indicator 31 Aug 2026/2 Aug 2027, "tag the regime") retold by the Shop Life vignette L212–216 with the same numbers. Survives: the vignette; box deleted, Kaz's "tenured professor" misread kept as one narration line threading into the vignette. **Done:** Box deleted; Kaz's misread now threads narration into the vignette.
- [x] B5. Hendershott et al. 2026 (15% best-quote win rate, 16–40% trade-throughs, 6–7 bp) in the dealer Seat box L246 and again at L406. Survives: L406 (evidence); the box keeps its reading and points to §2.4. **Done:** Seat box keeps its reading; numbers live once in §2.4.
- [x] B6. S-curve numbers told three times: box L294 (IG 0.25→0.92, r 0.131, 5.3 yrs), L296 (HY 3.5 yrs, 64%/56%), derivation L328 (all again); K=0.8 sensitivity at L300 and L330. Survives: derivation for the arithmetic, L300 for the ceiling insight (results only); box gets its own numbers; L296 deleted. **Done:** Box uses toy odds; numbers live once in the derivation.
- [x] B7. Splicing denominators: Ines's L278 ("which 'electronic' it means and what it divides by") vs Ways This Blows Up L332. Survives: Ines; the box's Bondwave/TRACE-share examples move into her line; box deleted. **Done:** Splicing box deleted; Bondwave and TRACE-share examples now Ines's.
- [x] B8. Best-of-n told twice: L340–342 (three-eighths cover; 1/n; anchoring; 0.45 → 2; 1/φ; equicorrelated) vs derivation L366–386 (same sentences verbatim). Survives: derivation; L340–342 deleted; box gets its own numbers. **Done:** Prose retellings deleted; derivation carries best-of-n; box uses five dealers.
- [x] B9. 9 April 2025 previewed at L344 (13.2 → 6.6, 11.3, θ vs φ) and told in the §2.9.3 scene (L812–840). Survives: the scene; L344 compressed to the n_eff-barely-moves point after the derivation, with a pointer. **Done:** April 9 preview compressed after derivation; scene keeps the numbers.
- [x] B10. Router odds arithmetic told in Ines's walk-through L472 and again in the derivation L492. Survives: the scene; derivation keeps only the J_{A→R} line and points back. **Done:** Derivation keeps J line only; threshold arithmetic stays in scene.
- [x] B11. Router breaks in stress: detached L476 (Vanguard FILS quote; "auto-ex fills drying up") vs Ways This Blows Up L494 (Swiss Life; March 2026). Survives: Ines's line as a scene beat; Vanguard quote joins the Ways box (C4). **Done:** Ines carries the auto-ex tell; Vanguard quote joins Ways box.
- [ ] B12. PT basket arithmetic told three times: covariance box L514 (200 voices, 0.1 → 0.1045), L516 (\$100mm, 200 lines, 1/200, a tenth, 1/n_eff), derivation L536 (same sentences). Survives: derivation; L516 deleted; box gets its own numbers.
- [ ] B13. The dealer's four terms in prose L512 and again in the derivation gloss L528. Survives: derivation gloss; L512 cut to two sentences.
- [ ] B14. The 2022 PT reversal told six times: Man annotation L508, L518, Kaz L568, Kamenski/eVestment L570, dated spine L584 (eVestment again), annotation L588. Survives: the dated spine L584 (with Kaz's two-terms diagnosis and Kamenski merged in, after the decision card), and L588. L508 and L518 become pointers; L568–570 move below the card (lesson 9: no answer before the card).
- [ ] B15. "What a systematic desk would have flagged" L594 restates Ines's tell (L578) and her rebalance-log column (L596). Survives: Ines; L594 keeps only the sweetener and regime-switching sentences.
- [ ] B16. PT numbers from the Trend Watch retold at L590 (18%, 19.8%) and L592 (8 April, 12% of \$89.7bn); average ticket \$560k → \$360k at L158 and L590. Survives: the Trend Watch and the §2.9.3 scene; L590–592 point to them; ticket size stays at L158.
- [ ] B17. ETF band told three times: L610 (two trades, η), L612 (Todorov 200 bp, HMM inversion), derivation L616–626; the scene retells Todorov (L666) and HMM (L648). Survives: box → derivation; scene keeps Todorov and HMM; L610 deleted; L612 cut to its immediacy-versus-stale-marks reading.
- [ ] B18. SMCCF timeline told three times: L632, Mags L670, §2.9.3 L790. Survives: Mags's telling L670 with L632's extra facts (ETF wording, "certain"/"additional", Scottsdale line, Dec 2020 expiry, June/July 2021 sales) merged in; L632 deleted; L790 keeps PMCCF and the \$850bn only.
- [ ] B19. April 7, 2025 ETF record (\$98.9bn, one cent) told at L628, L804, L848; April 8 \$89.7bn/12% at L808 and L848. Survives: the §2.9.3 scene; L628 points to it; L848 keeps only its new facts (Treasuries \$2.4tn, no facility, FEDS Note).
- [ ] B20. Kargar 200 bp and Haddad–Moreira–Muir told in the March 2020 scene (L646, L648) and again at L790. Survives: the scene; L790 cut.
- [ ] B21. "How it would have traded" L850 restates Ines's 10:40 answer (L838) and L788's whiteboard summary (which itself says it is the same paragraph). Survives: Ines; L850 keeps the indicators and the lesson; L788 loses its last three sentences.
- [ ] B22. Quant funds' \$116.5bn on Open Trading told at L402 and L668. Survives: L402; L668 points to it.
- [ ] B23. LCS trust told twice: annotation L734 ("should check that the two agree before trusting either"; floaters/callables) and L746. Survives: annotation; L746 becomes a scene (C5).
- [ ] B24. Duration tiny number (D=5, 10 bp → 0.50%, 25 bp) in box L736 and L744. Survives: L744; box gets its own number.
- [ ] B25. Fundamental-law tiny number (12 → 7.5, 2.56, 1.6, 48 → 77) in box L752 and L754. Survives: L754; box gets its own number.
- [ ] B26. Duplicate Specs: body "Specification for AI Implementation" Module/Schemas/Edge cases (L856–860) and the Debrief's "The Spec You Hand the Robot" (L930). Survives: the Debrief Spec, with L858's schemas merged in; L856 and L860 deleted (L866 already holds the clip/centering detail).
- [ ] B27. Listing 2.2 paragraph L880 relists the §2.3.2 caveats (winner's curse, non-response, cover gap consistent with competition and herding), also in the Debrief. Survives: §2.3.2 and the Debrief; L880 points.

## (c) Templates and detached judgment paragraphs

- [ ] C1. L51 Ines's syllabus ("First you date ... Then you read ... You fit ... You price ... You compute ... You treat ... And at the end") — a syllabus in costume. Cut to the one-line answer; the Debrief already gives each outcome to a cast member.
- [ ] C2. L97 detached "When to reach for it" paragraph ("the first thing a seasoned trader checks"). Recast as a Mags/Ines beat at the end of the §2.1 exchange.
- [x] C3. L304 "So when does the curve earn its place? ... an experienced hand checks three things" — delete; the stress-year and splice points live in Ines's L282/L278, the fitted-ceiling point in L302; the one new idea (PT moves the ceiling) goes to L302 and the Finder row. **Done:** Judgment paragraph deleted; PT-moves-the-ceiling line joins Kaz's paragraph.
- [x] C4. L476 "So the router has a natural territory ... A seasoned desk watches" — recast as Ines's beat after "the formula took its time"; Vanguard quote into the Ways box. **Done:** Territory paragraph now Theo's question and Ines's spoken answer.
- [ ] C5. L746 "So which LCS deserves trust? ... The score also breaks in three known places" — replace with a 150–200-word scene (Theo's floater LCS); the callable and price-quoting breaks go to the Finder row.
- [x] C6. L388 "Three caveats ... First ... Second ... Third" — recast without enumerators. **Done:** Caveats recast as prose; no enumerators; leads into Poker Table.
- [x] C7. L406 "Third, there is direct evidence" after "two places" — fix the stray enumerator. **Done:** Stray 'Third' replaced with 'And'; two places now read cleanly.
- [x] C8. L390 Poker Table "For Theo, the practical rule:" — give the line to Ines. **Done:** Practical rule now Ines's spoken line to Theo.
- [ ] C9. L838 Ines "First you look ... Second, the no-touch fill rate" — drop the enumerators; keep the order in her voice.
- [ ] C10. Listing prose L870, L880, L892, L902: "Use it ... Do not use ... The edge case that bites" ×4. Each keeps its edge case once, opened on the chapter moment (Kaz's K = 0.48; 9 April; Exercise 4's junior; the BBB line's two routers).

## (d) Boxes

Count: 12 Math, Gently (L63 P/Q, L138 mixture, L154 censoring, L168 distribution shapes, L294 S-curve, L338 order statistics, L410 markout, L462 random walk, L514 covariance, L608 no-arbitrage band, L736 duration, L752 fundamental law) against a cap of 10. Density fine (1 per ~2,650 words); no two Math, Gently adjacent. Runs of more than two boxed elements: none found (max two: L206–208, L242–246, L420–422).

- [ ] D1. L63 P/Q box: survey mention; Ch 1 owns "What 'risk-neutral' really means", Ch 6 owns Q. Demote to a one-sentence gloss with pointers, merged into L61.
- [x] D2. L168 "How distributions differ": survey of five shapes (Ch 1 owns normal/Poisson/exponential/fat tails; Ch 5 §5.7 fits tails). Demote: Pareto gets a two-sentence gloss in Kaz's L170; exponential's memorylessness already explained in the L338 box (fix its back-pointer). **Done:** Shapes box retired; Pareto gloss in Kaz's paragraph; pointer fixed.
- [x] D3. L462 random walk: Ch 1 owns the box and §6.1.1 the load-bearing use. Demote to Kaz's two-line answer to Theo with the 0.8 bp number. **Done:** Random-walk box now Kaz's two-line answer with 0.8 bp.
- [ ] D4. L138 mixture box: trim "what a distribution is" (Ch 1's box); give it its own number (not FINRA's 82.9%, which L146 states).
- [ ] D5. Boxes that reuse the text's numbers (lesson 7) get their own: L294 (S-curve), L338 (order statistics), L514 (covariance), L736 (duration), L752 (fundamental law). Vary sign-offs ("The full version follows" ×5).
- [ ] D6. After D1–D3: 9 Math, Gently. Re-check runs and adjacency after B4, B7, B17 moves.

## (e) Research-note leaks and fiction labels

- [ ] E1. HTML CHECK comments L21 (Halvorsen) and L662 (Theo's PJT start): resolve under G1/G2 and delete; L680 verification comment ("checked against Ch 1") deleted.
- [ ] E2. Trend Watch "chart reading, CHECK" ×3 (L261, L262, L542): fact-check resolved them as CONFIRMED (`applied_factcheck_ch01_07.md` item 1); drop "CHECK", keep "chart reading".
- [ ] E3. L698 "(self-reported, CHECK)" → "self-reported"; "(title only; not verified here)" → press-report hedge. L702 "an INFERENCE, not a measurement (CHECK)" → plain "an inference".
- [ ] E4. L518 "the trend research suggests", L708 "The trend report puts it plainly", L724 "our trend data say" — recast without internal-report voice.
- [ ] E5. Fiction labels: §2.6.2 scene has none (add at top); March 2020 scene label at end (L678) and April 2025 scene label at end (L844) move to the top of each scene (lesson 13).

## (f) Reference layer

- [ ] F1. Add a Finder table at the top of §2.10 (ten rows: concept · equation · intuition box · judgment scene · listing), carrying the one-line rules retired by C3–C5 and D1–D3.
- [ ] F2. Promote the three decision points (Feb 2022; 3:30 p.m. 12 Mar 2020; 10:40 a.m. 9 Apr 2025) to `####` headings; the two long scenes already have `####` headings; the §2.6.2 case study is `###`.

## (g) Cast-bible contradictions

- [ ] G1. C9: "Halvorsen Freight 7.125% senior notes due 2030, B2" (L5), "Halvorsen is B2" (L37), "a B2 bond" (L366) → Halvorsen Packaging 7.25% senior notes due 2029, B3. Name the story day (cast rule 3): Tue 13 Oct 2026, week four, after Ch 1's Fri 9 Oct lender call.
- [ ] G2. C3: Theo's March 2020 PJT memory (L660) needs a pre-March-2020 start: "ten weeks into the job" (joined Jan 2020).
- [ ] G3. L926 "a decade learning to read" contradicts six years at PJT → "six years".
- [ ] G4. Record new facts in `state/cast_bible.md`: Theo's Ch 2 Halvorsen ticket and PJT start (Jan 2020); Ines's March 2020 seat (IG market making at a dealer); Kaz in a university library in March 2020 and a first quant job in 2022; Mags's 2021 view from the distressed seat and spring-2020 purchases; Kaz misreads "riskless principal" (tenured professor) and "authorized participant"; Femi (Shop Life, fictional systematic asset manager).

## (h) Relative-value beat

- [ ] H1. `state/rv_thread.md` does not exist (only `state/rv_thread_plan.md`), so no RV beat is assigned this pass; no item to write.

<!-- items above are ticked below as they are fixed -->
