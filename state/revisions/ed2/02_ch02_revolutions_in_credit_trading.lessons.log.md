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
- [x] B12. PT basket arithmetic told three times: covariance box L514 (200 voices, 0.1 → 0.1045), L516 (\$100mm, 200 lines, 1/200, a tenth, 1/n_eff), derivation L536 (same sentences). Survives: derivation; L516 deleted; box gets its own numbers. **Done:** Prose basket paragraph deleted; box uses fifty voices at 0.2.
- [x] B13. The dealer's four terms in prose L512 and again in the derivation gloss L528. Survives: derivation gloss; L512 cut to two sentences. **Done:** Four-term walk cut to one sentence; derivation gloss survives.
- [x] B14. The 2022 PT reversal told six times: Man annotation L508, L518, Kaz L568, Kamenski/eVestment L570, dated spine L584 (eVestment again), annotation L588. Survives: the dated spine L584 (with Kaz's two-terms diagnosis and Kamenski merged in, after the decision card), and L588. L508 and L518 become pointers; L568–570 move below the card (lesson 9: no answer before the card). **Done:** Kaz and Kamenski moved below the card into dated spine.
- [x] B15. "What a systematic desk would have flagged" L594 restates Ines's tell (L578) and her rebalance-log column (L596). Survives: Ines; L594 keeps only the sweetener and regime-switching sentences. **Done:** Flagged list cut; Ines's tell carries it; trading line kept.
- [x] B16. PT numbers from the Trend Watch retold at L590 (18%, 19.8%) and L592 (8 April, 12% of \$89.7bn); average ticket \$560k → \$360k at L158 and L590. Survives: the Trend Watch and the §2.9.3 scene; L590–592 point to them; ticket size stays at L158. **Done:** PT numbers point to Trend Watch, now moved to section end.
- [x] B17. ETF band told three times: L610 (two trades, η), L612 (Todorov 200 bp, HMM inversion), derivation L616–626; the scene retells Todorov (L666) and HMM (L648). Survives: box → derivation; scene keeps Todorov and HMM; L610 deleted; L612 cut to its immediacy-versus-stale-marks reading. **Done:** Band prose deleted; box leads to derivation; scene keeps Todorov, HMM.
- [x] B18. SMCCF timeline told three times: L632, Mags L670, §2.9.3 L790. Survives: Mags's telling L670 with L632's extra facts (ETF wording, "certain"/"additional", Scottsdale line, Dec 2020 expiry, June/July 2021 sales) merged in; L632 deleted; L790 keeps PMCCF and the \$850bn only. **Done:** SMCCF told once, by Mags, with all milestones merged in.
- [x] B19. April 7, 2025 ETF record (\$98.9bn, one cent) told at L628, L804, L848; April 8 \$89.7bn/12% at L808 and L848. Survives: the §2.9.3 scene; L628 points to it; L848 keeps only its new facts (Treasuries \$2.4tn, no facility, FEDS Note). **Done:** April 7–8 numbers live in the replay; recap keeps new facts.
- [x] B20. Kargar 200 bp and Haddad–Moreira–Muir told in the March 2020 scene (L646, L648) and again at L790. Survives: the scene; L790 cut. **Done:** March 2020 recap points to the scene; PMCCF and $850bn kept.
- [x] B21. "How it would have traded" L850 restates Ines's 10:40 answer (L838) and L788's whiteboard summary (which itself says it is the same paragraph). Survives: Ines; L850 keeps the indicators and the lesson; L788 loses its last three sentences. **Done:** Hindsight paragraph cut; Ines's 10:40 answer carries the trade.
- [x] B22. Quant funds' \$116.5bn on Open Trading told at L402 and L668. Survives: L402; L668 points to it. **Done:** Scene points to §2.4's Open Trading figure; number told once.
- [x] B23. LCS trust told twice: annotation L734 ("should check that the two agree before trusting either"; floaters/callables) and L746. Survives: annotation; L746 becomes a scene (C5). **Done:** LCS trust paragraph replaced by scene; annotation points to it.
- [x] B24. Duration tiny number (D=5, 10 bp → 0.50%, 25 bp) in box L736 and L744. Survives: L744; box gets its own number. **Done:** Duration box uses a 25 bp move; L744 keeps cost example.
- [x] B25. Fundamental-law tiny number (12 → 7.5, 2.56, 1.6, 48 → 77) in box L752 and L754. Survives: L754; box gets its own number. **Done:** Box halves the fare; Man's 12-to-7.5 numbers told once.
- [x] B26. Duplicate Specs: body "Specification for AI Implementation" Module/Schemas/Edge cases (L856–860) and the Debrief's "The Spec You Hand the Robot" (L930). Survives: the Debrief Spec, with L858's schemas merged in; L856 and L860 deleted (L866 already holds the clip/centering detail). **Done:** Body Module/Schemas/Edge cases deleted; schemas and guards merged into Debrief Spec.
- [x] B27. Listing 2.2 paragraph L880 relists the §2.3.2 caveats (winner's curse, non-response, cover gap consistent with competition and herding), also in the Debrief. Survives: §2.3.2 and the Debrief; L880 points. **Done:** Listing 2.2 paragraph points to caveats, Poker Table, 9 April.

Second sweep, found after the first fixes (tool count 28,710 = 1.96×, still above 1.9×). Line numbers refer to the file after the first sweep:

- [x] B28. L71 Man p.4 annotation relists what each revolution did to the two numbers; every section's closing line says it again, and the cold-open roadmap promises it. Survives: the section closers; the annotation keeps the definitions and the forecast point. **Done:** Annotation keeps definitions; section closers carry each revolution's effect.
- [x] B29. L87 "That is the RSSG translation" restates Ines's "relationship into a variable" (L85) before Mags's beat challenges it. Survives: Ines and Mags; L87 keeps the PJT contrast in two sentences. **Done:** RSSG translation cut to two sentences after Ines and Mags.
- [x] B30. L432 annotation's last sentence (the table "most often dropped because it 'has no trades in it'") is Ines's line in §2.5.1. Survives: Ines. **Done:** Annotation's dropped-table sentence cut; Ines says it in §2.5.1.
- [x] B31. ETF/lender Seat box L602 restates the band ("the choice that seat faces each afternoon is the band above ... discount closes ... stays open"), which the box, derivation and scene already tell. Survives: the band; the seat box keeps the podcast pointer and the Apollo seat. **Done:** Seat box points to the band instead of retelling it.
- [x] B32. Bank Seat box L670 ends by restating L666's Table C12 reading. Survives: L666; the box ends on utility versus franchise. **Done:** Bank seat box ends pointing to the block counts above.
- [x] B33. Systematic-fund Seat box L400 restates the markout logic of the box above it ("win the hands whose markouts it can live with"). Survives: the markout box; the seat keeps Lam and Kamenski and the slicing warning. **Done:** Markout logic cut from seat box; Lam, Kamenski kept.
- [x] B34. §2.9.3 L792 hand-history paragraph re-derives both stories' winner predictions at length before the verdict. Survives: the two predictions in one sentence each and the April 16 verdict. **Done:** Winner predictions one sentence each; April 16 verdict kept.
- [x] B35. Listing openers L816, L828, L838, L850 each retell their section before the moment (the budget question, the eleven responders, the three dialects, the PM and the head trader). Survives: the moment; each opener trimmed. **Done:** Four listing openers trimmed to the moment the function mattered.
- [x] B36. §2.5 L424 FINRA 82.9% is the fourth telling (Trend Watch, §2.2.1 twice). Survives: §2.2.1; L424 points back without the number. **Done:** Fourth 82.9% telling replaced by pointer to §2.2.1.
- [x] B37. §2.9.3 L744 whiteboard router paragraph restates the router's inputs one by one. Survives: the 200 bp immediacy premium and the "total confidence" line. **Done:** Router inputs compressed to one sentence on the whiteboard.

Third sweep (tool count 28,302 = 1.94×):

- [x] B38. §2.2.1 overnight paragraph re-explains Rule 6730's day edges after Kaz has quoted the rule. Survives: the "third queue" and the timestamp-regime point. **Done:** Overnight paragraph keeps third queue and regime column; edges compressed.
- [x] B39. §2.1 Man p.19 annotation ("logs every unfilled order ... training label (§2.5)") repeats §2.5's attempted-but-not-executed annotation. Survives: §2.5. **Done:** Unfilled-order logging left to §2.5's attempted-but-not-executed annotation.
- [x] B40. §2.6.2 "2021, the boom" spine entry repeats Mags's 2021 story and the p.2 annotation. Survives: Mags; the spine keeps Man's move into PT. **Done:** 2021 spine entry points to Mags; keeps Man's move.
- [x] B41. §2.9.2 payoff paragraph restates the derivation's assumption (bets proportional to turnover; square root against a line) one paragraph before the derivation. Survives: the derivation. **Done:** Payoff paragraph drops the assumption the derivation states next.
- [x] B42. March 2020 scene intro recaps §1.8's whiteboard; the BIS paragraph's "basket at NAV ... never for sale" restates Ines's and Mags's lines. Survives: the dialogue. **Done:** Scene intro and BIS paragraph trimmed; dialogue carries the basket.
- [x] B43. ETF/lender Seat box tells the "edge of the map / ceiling" idea twice in its last four sentences. Survives: one telling. **Done:** Seat box tells the edge-of-map ceiling once.

Fourth sweep (tool count 28,075 = 1.92×):

- [x] B44. Listing 2.1 prose (`fit_adoption` does the work) restates the Debrief Spec's guards (None, clip with warning, 2015 centering, OLS fallback). Survives: the Spec; the prose keeps the sequence of the fit. **Done:** Listing 2.1 prose defers guards to the Spec; fit sequence kept.
- [x] B45. Listing 2.2 prose restates the Spec's input checks, draw count and seed. Survives: the Spec; the prose keeps the broadcast-anchor and `np.partition` mechanics. **Done:** Listing 2.2 prose drops input checks and draw count; mechanics kept.
- [x] B46. §2.9.1 Man TC paragraph's Exercise 4 sentence repeats the Listing 2.3 paragraph. Survives: the listing paragraph. **Done:** Exercise 4 sentence cut; listing paragraph names the bug.
- [x] B47. Lesson 9: the March 2020 BIS beat reveals the next day's 0.19% and the NAV-falling outcome before the 3:30 p.m. card is posed; the §2.9.3 whiteboard answer tells it again. Survives: the answer; the beat ends on "nothing on the screen said how much of each", and "the ETF had been there a day early" moves into the answer. **Done:** 0.19% reveal moved after the card into the whiteboard answer.
- [x] B48. §2.3 Man p.19 annotation lists the RFQ's labeled record (invited, answered, quotes, winner, cover, timestamps, traded), which the §2.3 closer and the §2.5 p.4 annotation tell. Survives: the closer and §2.5. **Done:** RFQ labeled-record list cut; closer and §2.5 carry it.
- [x] B49. "Theo's edge is where the exhaust is thinnest" told four times (§2.1 Man p.2 annotation, §2.2.2, §2.8, Debrief). Survives: §2.2.2's "aha" line, §2.8 and the Debrief; the §2.1 annotation points ahead. **Done:** §2.1 annotation points to §2.8 instead of retelling Theo's edge.
- [x] B50. Dealer Seat box (§2.3) re-tells Mags's run ("binds nobody", stale by the first coffee) a paragraph after she says it. Survives: Mags. **Done:** Seat box drops the run's staleness; Mags's line carries it.
- [x] B51. "No March-2020-style discount spiral" told in the April scene (Mags) and again in the April recap. Survives: the scene. **Done:** Recap drops the discount-spiral clause; Mags's scene keeps it.
- [x] B52. Lesson 9: the April 16 hand-history verdict sits before the 10:40 a.m. card. Move it after Ines's answer (the desk's action), so the card comes before any answer. **Done:** Hand-history verdict moved after Ines's answer; card now precedes answers.
- [x] B53. The stress paradox ("hardest tickets went back to the phone while the marginal provider moved onto the wire") told in the March 2020 scene and in the §2.9.3 Man p.5 annotation. Survives: the annotation (with its extraction); the scene points to it. **Done:** Scene points to Man's p.5 annotation instead of stating paradox.
- [x] B54. §2.2.2 opening restates the caps Kaz explained at 3:56 in the cold open. Survives: Kaz; §2.2.2 points to "the two strings Theo met at 3:56". **Done:** §2.2.2 opens on Theo's 3:56 strings; caps told once by Kaz.
- [x] B55. Censoring box's parenthetical on Ben Dor's "censored"/"truncates" and the p.162 annotation's "the right word" make the same point. Survives: the annotation. **Done:** Box parenthetical cut; annotation names the right word.
- [x] B56. Ben Dor p.364 annotation announces the Pareto extraction ("below we use it to extract a structural fact") that the next paragraph announces again. Survives: Kaz's paragraph. **Done:** Annotation's forward announcement cut; Kaz's paragraph carries it.
- [x] B57. Cold-open roadmap's last sentence ("Each section closes by saying what its revolution did to the two numbers") and the §2.1 Man p.4 annotation say the same. Survives: the annotation, where the two numbers are defined. **Done:** Roadmap's closing sentence cut; §2.1 annotation names the two numbers.
- [x] B58. §2.4 Open Trading launch date: "If your model's first feature is the launch date of its own data source, check the 10-K" is a manual-voice aside after the 10-K is already cited. Cut. **Done:** Manual-voice launch-date aside cut; 10-K citation stays.
- [x] B59. §2.8 opening meta-sentence ("so every number below carries its source and a self-reported flag") describes the hedges the paragraph then applies. Cut to the claim. **Done:** Meta-sentence cut; the hedges themselves stay in the paragraph.
- [x] B60. After the 12 March card, Ines says the band is one of three tools and the other two are ahead; the narration then lists the three again with section numbers. Survives: Ines; narration keeps one pointer. **Done:** Narration cut to one pointer; Ines names the missing tools.

## (c) Templates and detached judgment paragraphs

- [x] C1. L51 Ines's syllabus ("First you date ... Then you read ... You fit ... You price ... You compute ... You treat ... And at the end") — a syllabus in costume. Cut to the one-line answer; the Debrief already gives each outcome to a cast member. **Done:** Syllabus cut; Ines stops counting at one; Debrief carries outcomes.
- [x] C2. L97 detached "When to reach for it" paragraph ("the first thing a seasoned trader checks"). Recast as a Mags/Ines beat at the end of the §2.1 exchange. **Done:** Judgment paragraph now Mags's challenge and Ines's comparable-fills line.
- [x] C3. L304 "So when does the curve earn its place? ... an experienced hand checks three things" — delete; the stress-year and splice points live in Ines's L282/L278, the fitted-ceiling point in L302; the one new idea (PT moves the ceiling) goes to L302 and the Finder row. **Done:** Judgment paragraph deleted; PT-moves-the-ceiling line joins Kaz's paragraph.
- [x] C4. L476 "So the router has a natural territory ... A seasoned desk watches" — recast as Ines's beat after "the formula took its time"; Vanguard quote into the Ways box. **Done:** Territory paragraph now Theo's question and Ines's spoken answer.
- [x] C5. L746 "So which LCS deserves trust? ... The score also breaks in three known places" — replace with a 150–200-word scene (Theo's floater LCS); the callable and price-quoting breaks go to the Finder row. **Done:** Theo's floater scene replaces 'three known places'; others to Finder.
- [x] C6. L388 "Three caveats ... First ... Second ... Third" — recast without enumerators. **Done:** Caveats recast as prose; no enumerators; leads into Poker Table.
- [x] C7. L406 "Third, there is direct evidence" after "two places" — fix the stray enumerator. **Done:** Stray 'Third' replaced with 'And'; two places now read cleanly.
- [x] C8. L390 Poker Table "For Theo, the practical rule:" — give the line to Ines. **Done:** Practical rule now Ines's spoken line to Theo.
- [x] C9. L838 Ines "First you look ... Second, the no-touch fill rate" — drop the enumerators; keep the order in her voice. **Done:** Ines's order kept without enumerators; 'Only then' closes it.
- [x] C10. Listing prose L870, L880, L892, L902: "Use it ... Do not use ... The edge case that bites" ×4. Each keeps its edge case once, opened on the chapter moment (Kaz's K = 0.48; 9 April; Exercise 4's junior; the BBB line's two routers). **Done:** Four 'Use it/edge case' paragraphs open on chapter moments instead.

## (d) Boxes

Count: 12 Math, Gently (L63 P/Q, L138 mixture, L154 censoring, L168 distribution shapes, L294 S-curve, L338 order statistics, L410 markout, L462 random walk, L514 covariance, L608 no-arbitrage band, L736 duration, L752 fundamental law) against a cap of 10. Density fine (1 per ~2,650 words); no two Math, Gently adjacent. Runs of more than two boxed elements: none found (max two: L206–208, L242–246, L420–422).

- [x] D1. L63 P/Q box: survey mention; Ch 1 owns "What 'risk-neutral' really means", Ch 6 owns Q. Demote to a one-sentence gloss with pointers, merged into L61. **Done:** P/Q box demoted to one-sentence gloss pointing to Ch 1, 6.
- [x] D2. L168 "How distributions differ": survey of five shapes (Ch 1 owns normal/Poisson/exponential/fat tails; Ch 5 §5.7 fits tails). Demote: Pareto gets a two-sentence gloss in Kaz's L170; exponential's memorylessness already explained in the L338 box (fix its back-pointer). **Done:** Shapes box retired; Pareto gloss in Kaz's paragraph; pointer fixed.
- [x] D3. L462 random walk: Ch 1 owns the box and §6.1.1 the load-bearing use. Demote to Kaz's two-line answer to Theo with the 0.8 bp number. **Done:** Random-walk box now Kaz's two-line answer with 0.8 bp.
- [x] D4. L138 mixture box: trim "what a distribution is" (Ch 1's box); give it its own number (not FINRA's 82.9%, which L146 states). **Done:** Mixture box retitled, points to Ch 1, own 60% number.
- [x] D5. Boxes that reuse the text's numbers (lesson 7) get their own: L294 (S-curve), L338 (order statistics), L514 (covariance), L736 (duration), L752 (fundamental law). Vary sign-offs ("The full version follows" ×5). **Done:** Five boxes get their own numbers; sign-offs vary, none repeat twice.
- [x] D6. After D1–D3: 9 Math, Gently. Re-check runs and adjacency after B4, B7, B17 moves. **Done:** Nine Math, Gently; none adjacent; longest boxed run is two.

## (e) Research-note leaks and fiction labels

- [x] E1. HTML CHECK comments L21 (Halvorsen) and L662 (Theo's PJT start): resolve under G1/G2 and delete; L680 verification comment ("checked against Ch 1") deleted. **Done:** Both CHECK comments resolved and deleted; verification comment removed.
- [x] E2. Trend Watch "chart reading, CHECK" ×3 (L261, L262, L542): fact-check resolved them as CONFIRMED (`applied_factcheck_ch01_07.md` item 1); drop "CHECK", keep "chart reading". **Done:** Three CONFIRMED chart readings keep 'chart reading', lose 'CHECK'.
- [x] E3. L698 "(self-reported, CHECK)" → "self-reported"; "(title only; not verified here)" → press-report hedge. L702 "an INFERENCE, not a measurement (CHECK)" → plain "an inference". **Done:** Citadel self-reported, HRT headline hedge, inference lower-cased; no CHECK.
- [x] E4. L518 "the trend research suggests", L708 "The trend report puts it plainly", L724 "our trend data say" — recast without internal-report voice. **Done:** Three internal-report phrasings recast; PRS line given to Theo.
- [x] E5. Fiction labels: §2.6.2 scene has none (add at top); March 2020 scene label at end (L678) and April 2025 scene label at end (L844) move to the top of each scene (lesson 13). **Done:** Labels at top of all three scenes; PT scene gains one.

## (f) Reference layer

- [x] F1. Add a Finder table at the top of §2.10 (ten rows: concept · equation · intuition box · judgment scene · listing), carrying the one-line rules retired by C3–C5 and D1–D3. **Done:** Ten-row Finder table added at top of §2.10 with retired rules.
- [x] F2. Promote the three decision points (Feb 2022; 3:30 p.m. 12 Mar 2020; 10:40 a.m. 9 Apr 2025) to `####` headings; the two long scenes already have `####` headings; the §2.6.2 case study is `###`. **Done:** Three decision points now #### headings; long scenes already headed.

## (g) Cast-bible contradictions

- [x] G1. C9: "Halvorsen Freight 7.125% senior notes due 2030, B2" (L5), "Halvorsen is B2" (L37), "a B2 bond" (L366) → Halvorsen Packaging 7.25% senior notes due 2029, B3. Name the story day (cast rule 3). The old "three weeks" put the cold open on Tue 13 Oct, the day Ch 1 §1.3.2 has Halvorsen not trading at all ("The Tuesday after the 8-K"); set it on Tue 20 Oct 2026, week five, "a month on a systematic desk". **Done:** Packaging 7.25% 2029 B3 throughout; dated Tue 20 Oct, clearing Ch 1's halt.
- [x] G2. C3: Theo's March 2020 PJT memory (L660) needs a pre-March-2020 start: "ten weeks into the job" (joined Jan 2020). **Done:** Theo ten weeks into PJT in March 2020; CHECK removed.
- [x] G3. L926 "a decade learning to read" contradicts six years at PJT → "six years". **Done:** Debrief's 'a decade' now 'six years', matching the PJT canon.
- [x] G5. Kaz "spent 2022 at a first quant job" (§2.6.2 spine, moved from the old L568) contradicts the cast bible's Ch 14 canon (postdoc on rough paths until Nov 2023; on the desk by Jan 2025). Drop the 2022 job; Kaz reads the reversal in the four terms without a backstory. **Done:** Kaz's 2022 quant job removed; Ch 14 postdoc canon stands.
- [x] G4. Record new facts in `state/cast_bible.md`: Theo's Ch 2 Halvorsen ticket and PJT start (Jan 2020); Ines's March 2020 seat (IG market making at a dealer); Kaz in a university library in March 2020; Mags's 2021 view from the distressed seat and spring-2020 purchases; Kaz misreads "riskless principal" (tenured professor) and "authorized participant"; Femi (Shop Life, fictional systematic asset manager). **Done:** Cast bible gains Ch 2 rows, PJT start, misreads, Femi.

## (h) Relative-value beat

- [x] H1. `state/rv_thread.md` does not exist (only `state/rv_thread_plan.md`), so no RV beat is assigned this pass; no item to write. **Done:** No rv_thread.md exists; no RV beat assigned; nothing written.

## Metric, after

`python3 tools/prescriptiveness.py --pre 9ac1c379053d9d0254e9d524d9a40efdec4a2c71 book_src/02_ch02_revolutions_in_credit_trading.md`

| ver | words | bullets% | modal | imper | rule | dialog | mathgently | seat |
| :-- | --: | --: | --: | --: | --: | --: | --: | --: |
| pre (Ed 1) | 14,619 | 6.6 | 1.6 | 1.1 | 1.6 | 5.9 | 0 | 0 |
| before this pass | 31,789 | 1.0 | 1.8 | 0.9 | 1.1 | 8.1 | 12 | 4 |
| after this pass | 27,746 | 1.2 | 1.7 | 0.6 | 1.2 | 9.0 | 9 | 4 |

Growth 27,746 / 14,619 = **1.90×** (1.898), inside the 1.6–1.9× band, down from 2.17×. File 951 → 926 lines; `wc -w` 32,229 → 28,524. Imperatives per 1,000 words fell from 0.9 to 0.6, dialogue rose from 8.1 to 9.0. Nothing protected removed: 26 display-math blocks, 17 Source Extractions (text and page numbers byte-identical), three Trend Watches (only "CHECK" dropped from three CONFIRMED chart-reading cells), six exercises (identical), four Appendix F links and every URL kept. No code blocks; `$$` alone on lines; currency escaped; last line `<!-- STATUS: COMPLETE -->`; `tools/check_book.py` reports OK for the chapter.

## Open items (not fixed here)

- The §2.3.1 fit uses 48% for US IG in 2025 while the Trend Watch lists 48% for full-year 2024 and 52% for June 2025 (carried from the verify report); a one-line reconciliation belongs to the next fact pass.
- The chapter has no figures yet (U4 owns the three-figure minimum).
- Cast: Ch 2's cold open now sits on Tue 20 Oct 2026, after Ch 3's Fri 16 Oct in story time; book order and story order differ, as elsewhere in the book.

<!-- STATUS: COMPLETE -->
