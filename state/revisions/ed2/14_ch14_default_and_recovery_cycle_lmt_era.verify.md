# Verification Report, Edition 2: Chapter 14 (The Default & Recovery Cycle in the LMT Era)

Chapter: `book_src/14_ch14_default_and_recovery_cycle_lmt_era.md`. Pre-revision text: commit 9ac1c379 (609 lines, 78.9k characters). Post-revision text: 1,075 lines, about 210k characters. The revision log carries its completion marker. Dossiers used: `case_lmt_autopsies_us_2020_2026.md`, `case_courts_as_regime_variables.md`, `perspectives_buyside_credit_managers.md`, `media_episodes_posts_parts_III_IV.md`, `trend_re_default_and_recovery_dataset.md`, `trend_loans_clos.md`, `state/advisor_briefs/14_*.md`, `state/reviews/ed2/applied_factcheck_ch08_14.md`. Web: 8 calls of the 15 allowed (one fetch returned 403).

## 1. Nothing removed

Scripted comparison of pre and post:

| Item | Pre | Post | Result |
| :--- | :--- | :--- | :--- |
| Headings (outside code) | 31 | 38 | All 31 present; 7 added (5 "The Full Derivation", "Measuring the reaction, and the Lions Gate caution", "Calibrating the jumps") |
| Display-math blocks (`$$`) | 21 blocks (42 delimiters) | 21 (42) | Every pre block found verbatim in post (whitespace-normalized); the proofs moved into "The Full Derivation" subsections |
| [SOURCE EXTRACTION] blocks and their annotations | 10 | 10 | All verbatim |
| Trend Watch boxes | 3 | 3 | Present; two lines deliberately changed (Incora dates, Optimum 10-Q), as the brief required |
| Docket Diary, Poker Table, Ways This Blows Up | 1 each | 1 each | Present; Docket Diary Robertshaw/Incora/Wesco lines updated per the brief |
| Exercises | 6 | 6 | All six, original text intact, "Where this came up" pointers appended |
| Appendix F links (`#code-14-1` to `-5`) | 5 | 5 | All present; the anchors exist in `95_appF_code_companion.md` |
| Resource Graph sections | 4 | 4 | Every pre item present except the two channel-level podcast lines (Cloud 9fin, Odd Lots), replaced by the dated episodes the brief specifies |

Also retained: the five `<!-- EXPLAIN -->` stubs were replaced by 150-400 word listing explanations (directive U1), each keeping its Appendix F link; the "By the end of this chapter" paragraph was folded into Ines's closing speech with every item on the list still named; the four traps, the three-stage LGD model, the four Hamilton implementation details and the five trading signals are all present as narrative. No restorations were needed.

I also re-ran the five Appendix F listings (14.1 to 14.5) end to end: every PASS check passes, and the numbers quoted in the new listing explanations reproduce (65% vs 25% exponential default probability, 5.9%/10.2%/7.9% three-year EL, 0.230 vs 0.285 ten-year F_D when cures are mis-handled, the 0.245 Serta SD, the 7.0% co-op tail).

## 2. Facts

New factual claims were found by sentence-level diff by section (269 new sentences carrying a date or amount, concentrated in 14.5, 14.5.1, 14.6, 14.8.1, the Resource Graph), then read in full. Verified against dossier unless noted.

Verified without change: Lumen timeline and terms (31 Oct 2023 TSA, 22 Jan 2024 amended TSA, 22 Mar 2024 closing, participation 94.4/98.5/99.5%, maturities cut, 17 Sep 2024 offers, 2 Feb 2026 AT&T sale, 20 May 2026 tender; CreditSights prices); Houlihan Lokey "exclusive financial adviser to an ad hoc group of crossholders holding about \$11bn" (confirmed on the firm's own page); amended TSA dated 22 Jan 2024 and announced 25 Jan (Lumen 8-K exhibits); Robertshaw (all dates, amounts, 662 B.R. 300, credit bid, plan); Optimum calendar (25 Nov 2025 suit, No. 1:25-cv-09785, 6 and 19 Feb 2026, late-March amici, 4 Aug 2026 ECF 132, 30 Jun 2026 10-Q); Lions Gate prices and 2025 BCSC 1293; Serta Fifth Circuit dates (argued 10 Jul 2024, decided 31 Dec 2024, revised 14 Feb 2025, rehearing denied 18 Feb 2025), cert denied 10 Nov 2025 in No. 24-1322 on a petition by Barings and other participating lenders (Supreme Court docket coverage, Bloomberg Law, Octus), the \$261.13mm and 9% arithmetic, the \$186mm and \$62-94mm mitigation evidence, the defendants' names; Mitel plan figures (Paul Weiss: \$1.15bn, \$135mm, \$125mm); ARCC Pluralsight marks (89.0, 48.0, \$54.7mm, \$60mm) and the 96.8 second-lender mark; Jim Miller's quote; Loomis Sayles quote; Elliott/Veritas quote; Kundu quotes; all podcast and essay titles, dates and guests; Incora dates now match Ch 13 and `case_lmt_autopsies` section 4 (10 Jul 2024 oral, 17 Jan 2025 written, 8 Dec 2025 Crane, filing 14 months after 28 Mar 2022).

Fixed in the chapter:

1. **Lumen backstop economics.** The text said "a \$200mm fee plus 5% of the new money, about \$60mm". The \$200mm could not be confirmed in any source and does not fit a \$1.2bn raise. Removed; now "5% of the new money, about \$60mm" (CreditSights per dossier).
2. **Furniture Today date.** Cited as November 2025; the article is dated 12 December 2025. Fixed in the Resource Graph and the Act III citation; added the Supreme Court docket number.
3. **Serta June 2020 injunction.** The plaintiffs' names (Apollo, Angelo Gordon, Gamut) and Justice Masley were attributed to Mayer Brown's June 2020 note, which names neither the plaintiffs nor says "sacred rights". Names confirmed via Bloomberg Law/Reorg reporting; citation split accordingly, and Mayer Brown's actual holding (no likelihood of success, no irreparable harm because damages are available) added.
4. **CLO manager 2025 paragraph.** "A few fewer and a little more consensual" understated a fall from 38 to 24, and the "fewer coercive uptiers" claim belonged to 9fin's H1 2026 report, not 2025 (uptiers were still 12 of 17 LMTs in Q1 2025). Now "about a third fewer", and the 9fin "all but vanished" language is dated to H1 2026.
5. **"ECB-system study"** for Kundu: it is an ESRB working paper. Now "European Systemic Risk Board study".
6. **Five p's lead-in.** "46% within two years" corrected to "by April 2025" (the box's wording); added a note that the Roe-Rotaru "56% had filed" and the S&P/Wellington "56% re-defaulted or CCC+" are two different figures that share a number.
7. **"Chapter 5 called it 'what we knew when'".** Chapter 5 never uses the phrase (it has the point-in-time snapshot of vendor marks). Rewritten as Hana's Chapter 5 experience; the later "what we knew when" back-reference in 14.7.1 now has an antecedent.
8. **Cross-references.** Random-walk, Itô and risk-neutral boxes also exist in section 1.5 (earlier than the "first-use" sections named); exponential box in 1.5 added; "racecourse" was in 5.1.1 only, not 1.5. Corrected.
9. **Invented speech by real groups.** The Del Monte chorus put "We have not signed a cooperation agreement with each other" in the mouths of two real lender groups. Replaced with a generic "We reserve all rights" and a note that the chorus is the book's device.
10. **Rule 2019 in "How a systematic desk flags it".** Rule 2019 statements exist only after a filing; for the out-of-court June 2020 deal the signal is dealer and press evidence. Corrected (inherited error from the pre text).
11. **Listing 14.3 explanation.** "In one trial run ... p near 0.13 and a shape above 2" was a cherry-picked draw. Re-ran 60 trials: p median 0.22, from 0.10 to the ceiling of 1 (25% of runs above 0.9), shape 0.8 to 2.1. Text now reports that.
12. **Composite labels.** Added "(a composite; the holders are invented)" to Mags's Rule 2019 statement and "(a composite; no real note is meant)" to the 7:10 a.m. research note. Softened "hundreds of CLOs" to "many CLOs" for the Serta first lien.

Real people and dialogue: every spoken line belongs to the book's cast (Ines, Theo, Kaz, Mags, Hana, ROBO) or to unnamed fictional composites. Judges, firms and officers appear only through public records or verbatim quotes (Fifth Circuit, Loomis, Miller, Hedgeweek, Kundu, CreditSights). Fictional composites carry labels: Quillfeather, the CLO manager, Hana's forty-one issuers (count marked invented), the regime-explain committee, Mags's fund and \$15mm position, and the dealer desk seat. No further changes needed.

## 3. Hygiene

- Code blocks: one, a ```text diagram (the five-state semi-Markov chart). None other.
- Math delimiters: 42 `$$` (even, all paired); no line has an odd inline `$` after removing `\$`.
- Currency: all dollar amounts are `\$`-escaped; the 30 `$digit` hits are all legitimate math openers.
- No `---` lines anywhere.
- Fixed two merged paragraphs (the "Act II" and "Act III" openers had no blank line before them).
- Last line is the completion marker (verified).

## What remains doubtful

- **Lumen details single-sourced to the dossier** (CreditSights and 8-K reading by the research agent): the 11% first-lien 2029 notes (corroborated by later filings), the 5%/\$60mm backstop, 85% term-loan super-priority, \$975/\$700/\$860 offer prices and tender percentages, and the 99.4% tender figure (the dossier's own arithmetic). Prices are vendor-indicative and the chapter says so.
- **Optimum defendants.** The dossiers disagree (six names in one, eight including BlackRock and J.P. Morgan in another). The chapter says "Apollo, Ares and BlackRock, along with other large credit managers". The complaint was not read. No dismissal ruling found as of mid-October 2026.
- **Serta remand specifics** (the 7 Jul 2026 award, \$186mm of trading, the Barclays market-maker chats) rest on the advisor brief's reading of the opinion and on Mayer Brown; the opinion itself was not re-fetched. "Nobody had said" about an appeal is true as of 8 July only; the dossier lists the appeal status as CHECK.
- **Robertshaw and Mitel plan figures** come from Paul Weiss memos via the dossier, not re-fetched.
- **Del Monte August 2024 date** stays marked unverified, as the brief required.
- **Cross-reference spot checks** covered the sections named in the Math, Gently boxes, not every pointer in the chapter.
- **Cosmetic:** Chapter 5's ticket is RISK-2291, Chapter 14's is DATA-2291; harmless, possibly intended as an echo.
- **Figures** were not part of this pass; the brief's five proposed new figures are still to come from the figures pass.

Summary: 8 web calls; 12 fixes in the chapter; nothing removed; one hedge removed (the Lumen \$200mm fee); two items left hedged by design (Del Monte date, Serta appeal status).

<!-- STATUS: COMPLETE -->
