# Cleanup log: facts-12-16-17-22-26 (2026-10-18)

Group items: blue-owl-99.7, ch16-ref, ares-quote, OCC-2011-12, uyeda-speech. No earlier log existed (no COMPLETE marker), so all five items were worked. Web calls used: 6 of 6 (WebFetch of the OBDC II 8-K on sec.gov; WebSearch for the Blue Owl release; WebFetch of the Motley Fool ARCC Q4 2025 transcript; WebSearch for other ARCC transcripts; WebFetch of the Fed SR 11-7 PDF, 404; WebFetch of the SEC Uyeda speech page, succeeded). One saved copy of the SR 11-7 attachment from an earlier session (scratchpad `dl_sr117/sr1107a1.txt`) was read locally with grep.

Files touched: `book_src/12_ch12_multi_asset_credit_allocation.md` (item 1), `book_src/16_ch16_post_reorg_equities_and_claims.md` (item 2), `book_src/17_ch17_private_credit_public_private_convergence.md` and `state/research/perspectives_buyside_credit_managers.md` (item 3), `book_src/26_ch26_ai_agents_and_llms_on_the_credit_desk.md` (item 4), `book_src/22_ch22_market_structure_regulation_trends.md` (item 5). Ch 26's own Blue Owl text (99.7%) was read, not edited.

---

## [blue-owl-99.7] — status: fixed

**Found.** Not already fixed: Ch 12 line 703 still said 99.8%. Ch 17 (lines 472 and 486), Ch 17-B (lines 306, 312) and Ch 26 (line 196) all say 99.7%. The dossier (`trend_private_credit_marks_and_redemptions_2025_2026.md`, row 18 Feb 2026 and §3.2) says 99.8% for the whole \$1.4bn, and `open_items_ch17_ed2.md` item 4 had already noted "dossier says 99.8 (rounding); release quoted at 99.7".

Checked the sources (2 web calls):
- OBDC II's 8-K (sec.gov, `obdc-20260217.htm`): for OBDC II's own \$600.0mm of commitments, fair value "was \$538.3 million, equivalent to 99.8% of par value". So 99.8% is OBDC II's slice only.
- Blue Owl's release of 18 Feb 2026, as reported in the press (Exec Edge via Yahoo Finance; Bloomberg; AltsWire): the three BDCs (OBDC II \$600mm, OTIC \$400mm, OBDC \$400mm) sold \$1.4bn "at fair value, which is equivalent to 99.7% of par value as of February 12, 2026" across all three vehicles. Ch 17's quotation of that sentence matches. (The release page itself was not fetched; the 99.7% rests on the quoted sentence in Ch 17 and the press reports.)
- So the dossier's 99.8% conflated the OBDC II 8-K figure (one fund's piece) with the whole-sale figure. The whole \$1.4bn is 99.7%.

**Fix (Ch 12 §12.7, Beat 3).**
Old: `It sold \$1.4bn of direct loans at 99.8% of par to pension and insurance buyers, \$600mm of it from OBDC II, with a fairness opinion;`
New: `It sold \$1.4bn of direct loans at 99.7% of par to pension and insurance buyers, \$600mm of it from OBDC II, with a fairness opinion;`
Ch 12, Ch 17, Ch 17-B and Ch 26 now agree on 99.7%.

**Follow-up for the dossier owner (not edited, outside the named files).** `state/research/trend_private_credit_marks_and_redemptions_2025_2026.md` line 33 (table row "18 Feb 2026") and line 72 (§3.2 text, and heading "a loan sale at 99.8") should read 99.7% for the whole \$1.4bn, with the note that OBDC II's 8-K gives 99.8% for its \$538.3mm fair value of \$600mm commitments. Left as is so the dossier edit can be made by whoever owns that file.

---

## [ch16-ref] — status: fixed

**Found.** Not already fixed: Ch 16 line 176 (§16.2.2, "Supply") still read "Chapter 1's box in §1.8.1". Confirmed the targets: Ch 1 line 557 (§1.8.1) now carries the two-sentence gloss ("the way a cup of coffee cools, with a half-life of ln 2/theta ... §9.4 cools the same cup for a signal"); Ch 9's box *Half-life, or how fast the coffee goes cold* sits in §9.4.1 (line 366), and its closing sentence says "Chapter 1 cooled the same cup to show price pressure fading after a forced sale".

**Fix (Ch 16 §16.2.2).**
Old: `(Chapter 1's box in §1.8.1 has the same curve for price pressure; we fit $\theta$ in §16.2.3)`
New: `(Chapter 1's §1.8.1 has the same curve for price pressure, and the box in Chapter 9, §9.4.1, cools it for a signal; we fit $\theta$ in §16.2.3)`
(Points at §9.4.1, the subsection that holds the box, rather than §9.4.)

**Not edited, for the owners of those files.** `book_src/03_ch03_pjt_rssg_cognitive_bridge.md` line 892 ("box in §1.8.1") and `book_src/99_appZ_solutions_hints_and_self_assessment.md` line 507 ("the half-life box in §1.8.1") carry the same stale reference; the box is now in §9.4.1 (Ch 1 has the gloss).

---

## [ares-quote] — status: fixed (quote replaced with an attributed paraphrase; dossier marked UNVERIFIED)

**Found.** Not already fixed: Ch 17 line 101 still quoted "We will walk away from transactions based on documentation terms" as Jim Miller's; the dossier carried it at lines 48 and 52.

Re-verification (2 web calls):
- Motley Fool transcript of the ARCC Q4 2025 call (4 Feb 2026): gives the sentence "We will walk away from transactions based on documentation terms." to Jim Miller, President, after RBC's Kenneth Lee asked about loosening terms; also gives Miller "...there's probably a heightened focus on documentation terms just given some of the headlines around LME transactions". The AOL and Finviz copies are syndications of the same Fool text, not independent.
- MarketBeat transcript (per the Ch 25 verify log, fetched twice there): the answer is by CEO Kort Schnabel and reads "We won't walk away from transactions based on documentation terms."
- A search for a third transcript found only those two families (Fool/AOL/Finviz and MarketBeat) plus Fintool and allmind pages that were not readable in the search result. No primary source (ARCC-hosted transcript, audio or 8-K) was reached. The "will"/"won't" difference reverses the meaning, so the quote cannot be printed verbatim with a named speaker.
- Side finding: in the Fool transcript the first-lien LTV phrase "in the high 30% to low 40% range" is in Kort Schnabel's prepared remarks on 2025 originations, not Miller's; the 1.8% non-accrual (at cost) and 3.8% BDC-average figures are Miller's, in the prepared credit remarks. Ch 17 attributed all three to Miller.

**Fix (Ch 17 "View From Another Seat. The direct lender", line 101).**
Old: `its president Jim Miller said, "We will walk away from transactions based on documentation terms," put the portfolio's first-lien loan-to-values "in the high 30% to low 40% range," and reported non-accruals of 1.8% at cost against a 3.8% average for BDCs.`
New: `management, asked whether deal terms were loosening, said that if anything there was "a heightened focus on documentation terms" after the liability-management headlines in the broadly syndicated market, put the portfolio's first-lien loan-to-values "in the high 30% to low 40% range," and reported non-accruals of 1.8% at cost against a 3.8% average for BDCs.`
(Same treatment as Ch 25: only the phrase both transcripts share is quoted, attributed to "management". The numbers are unchanged; the speaker label is dropped for all three because the sources disagree on who spoke.)
Closing note of the box, old: `(Quoted words are the speakers' own, from the calls cited; the reading of them is ours.)`
New: `(Quoted words are the speakers' own, from the calls cited; the reading of them is ours. Published transcripts of the 4 February call disagree on who made a further remark about walking away from deals over documentation, and on its wording, so we attribute only the phrase they share to "management" and quote nothing else from that exchange.)`
The Arougheti 31 July 2026 quote in the same box is untouched (dossier: Q2 call via Motley Fool/Webull; not part of this dispute).

**Dossier (`state/research/perspectives_buyside_credit_managers.md`).** Line 48 (the Miller table row) now reads speaker and quote **UNVERIFIED; do not quote**, with the Fool-versus-MarketBeat conflict spelled out. Line 52 (the "Miller also said a heightened focus ..." paraphrase) now says the speaker is UNVERIFIED, to attribute to "management", and records the LTV-phrase speaker finding.

**Follow-ups for other chapter owners (not edited; other agents are working in these files).** The same unverified quote, attributed to Jim Miller, is still printed in:
- `book_src/04_ch04_inside_the_systematic_credit_industry.md` line 125 (quote plus the "merits of not being a benchmark-style investor" line; that second quote is also from the same call and should be re-checked for speaker).
- `book_src/04_ch04c_other_seats_at_the_table.md` line 201 (verbatim quote at the end; also attributes the LTV range to Miller).
- `book_src/14_ch14_default_and_recovery_cycle_lmt_era.md` line 448 (quoted, "Jim Miller, ARCC Q4 2025 earnings call").
- `book_src/06_ch06_merton_and_intensity_models.md` line 880 (paraphrase: "Ares Capital's president ... will walk away"; the paraphrase carries the disputed will/won't meaning and the speaker).
Suggested fix for each: cut to "Ares Capital's management ... a heightened focus on documentation terms", as in Ch 25 and now Ch 17.

---

## [OCC-2011-12] — status: softened

**Found.** Not already fixed: Ch 26 §26.8 (line 562) read "that the Federal Reserve and the OCC issued on 4 April 2011 (OCC Bulletin 2011-12)". The number came from the synthesis; the dossier (`life_quant_shop_daily_life.md` §2.1) carries it as "SR 11-7 / OCC 2011-12" and says the Fed's landing page returned 404.

What could be checked:
- The saved SR 11-7 attachment (federalreserve.gov `boarddocs/.../sr1107a1.pdf`, read earlier by the Ch 7 verify pass and re-read here from the saved text) confirms: a joint document of the Board of Governors and the Office of the Comptroller of the Currency, dated April 4, 2011, titled "Supervisory Guidance on Model Risk Management". It does not itself print the OCC bulletin number (the number sits on the cover letters); it mentions only the OCC's earlier bulletin OCC 2000-16 (30 May 2000).
- A fresh fetch of `federalreserve.gov/supervisionreg/srletters/sr1107a1.pdf` returned 404, and occ.gov had returned 404 in the red-pen pass. The web budget was then spent (Uyeda page fetch), so the number could not be confirmed from a page in this pass. The number 2011-12 is what the dossier carries and what the editor recalls as the OCC's numbering for this guidance, but "recalls" is not verification, and the OCC bulletin's exact title was not seen.

**Fix (Ch 26 §26.8, line 562).** Dropped the unconfirmed parenthetical and kept what the attachment supports (joint issue, date).
Old: `that the Federal Reserve and the OCC issued on 4 April 2011 (OCC Bulletin 2011-12), organizes validation`
New: `that the Federal Reserve and the OCC issued jointly on 4 April 2011, organizes validation`
Line 881 of Ch 26 already cites "SR 11-7 (Fed/OCC, 2011)" with no bulletin number, so nothing else changes.

**Owner follow-up.** If the owner wants the bulletin cited, confirm on occ.gov (search "OCC Bulletin 2011-12", "Sound Practices for Model Risk Management: Supervisory Guidance on Model Risk Management", 4 April 2011) or on the Fed's SR 11-7 letter page, then restore "(OCC Bulletin 2011-12)" after "4 April 2011". The dossier line `life_quant_shop_daily_life.md` 26 ("OCC 2011-12") is unchanged and should be treated as unconfirmed until then.

---

## [uyeda-speech] — status: fixed

**Found.** Not already fixed: Ch 22 Resource Graph (line 977) still carried the "As fetched for the dossier (check the SEC page before printing numbers)" process note, the figures "about 165%" and "two more clearing agencies", and a quoted "will not be extended". WebFetch (not curl) reaches sec.gov, so the speech page itself was read (1 web call), which settles it:
- Title, speaker, date: "Remarks at the 2026 U.S. Treasury Market Conference", Commissioner Mark T. Uyeda, New York, 22 September 2026. Matches.
- 165%: "daily cleared Treasury volumes are now approximately 165% higher than before the Commission's proposal" (main text; footnote 4, citing DTCC, adds that FICC daily cleared volumes rose from roughly \$4.5 trillion in 2022 to more than \$12 trillion). So the 165% is the speech's own figure and its baseline is the pre-proposal period, not specifically FICC.
- "In the past year, the Commission also approved the registration of two additional clearing agencies": CME Securities Clearing and ICE Clear Credit (names per the fetch summary and the Part V dossier).
- Dates: "The compliance date for cash Treasury transactions is quickly approaching on December 31, 2026" and "The compliance date for repo transactions follows shortly after, on June 30, 2027."
- Extension: "as the SEC does not currently intend to extend these deadlines". The phrase "will not be extended" is NOT in the speech; the book's quotation marks around it were wrong.

**Fix (Ch 22, Resource Graph entry for the Uyeda remarks).**
Old: `As fetched for the dossier (check the SEC page before printing numbers): cleared Treasury volume has risen sharply (FICC daily cleared volume reported about 165% above the pre-proposal level), two more clearing agencies were approved, and the 31 Dec 2026 (cash) and 30 Jun 2027 (repo) compliance dates "will not be extended." A dated`
New: `Daily cleared Treasury volumes are "approximately 165% higher than before the Commission's proposal," the Commission approved two more clearing agencies (CME Securities Clearing and ICE Clear Credit) in the past year, and the compliance dates of 31 Dec 2026 (cash) and 30 Jun 2027 (repo) stand because the SEC "does not currently intend to extend these deadlines." A dated`
Checked that "will not be extended" appears nowhere else in `book_src/`. The dossiers (`media_episodes_posts_parts_V_VIII.md` line 69 and 187) still carry the old wording; the Part V dossier (`trend_part_v_market_structure_2026.md` line 38) already has the correct "does not currently intend to extend". Follow-up: correct the `media_episodes_posts_parts_V_VIII.md` row to the verified wording.

---

## Summary

| Item | Status |
| :-- | :-- |
| blue-owl-99.7 | fixed (Ch 12 now 99.7%; dossier follow-up noted) |
| ch16-ref | fixed |
| ares-quote | fixed (Ch 17 paraphrase; dossier UNVERIFIED; four other chapters flagged) |
| OCC-2011-12 | softened (bulletin number dropped; unconfirmed) |
| uyeda-speech | fixed (verified against the SEC page; one quotation corrected) |

<!-- STATUS: COMPLETE -->

## Review

Reviewer pass (2026-10-18). Each changed passage was read in the file; stragglers were found by grepping `book_src/` (and `state/appZ/`, the App Z source parts) for the old values and phrases.

**blue-owl-99.7: confirmed.** Ch 12 line 703 reads 99.7% for the whole \$1.4bn, with \$600mm from OBDC II. Ch 17 (lines 472, 663, 963), Ch 17-B (line 306, which also gives 99.8% for OBDC II's own \$600mm share per its 8-K) and Ch 26 (line 196) agree. No "99.8% of par" remains in `book_src/`; the only other 99.8 hits are the Zayo bond in Ch 13-B and Ch 17-B. The paragraph's currency escapes are intact. The dossier follow-up stands.

**ch16-ref: confirmed.** Ch 1 §1.8.1 carries the coffee gloss ("§9.4 cools the same cup for a signal"). The box *Half-life, or how fast the coffee goes cold* is in Ch 9 §9.4.1 (line 366), and §16.2.3 is the fitting subsection. The Ch 16 sentence and its math delimiters (12 `$`, balanced) are undamaged. Stragglers fixed, one Edit each, all now pointing to §9.4.1:
- Ch 3 line 539, "the half-life box is in §1.8.1" (not on the fixer's list)
- Ch 3 line 892, "box in §1.8.1"
- App Z line 507, "the half-life box in §1.8.1"
- the `state/appZ/03_ch03_pjt_rssg_cognitive_bridge.md` source copy of the App Z line, so a reassembly does not restore it
App Z line 87 ("§1.8.1 ... half-life gloss") is correct and unchanged.

**ares-quote: confirmed, with one correction.**
- Ch 17 line 101 now carries the attributed paraphrase ("management ... 'a heightened focus on documentation terms'"), identical in treatment to Ch 25 line 232. The closing note is intact and no unescaped `$` appears.
- Correction: the same sentence said management "put the *portfolio's* first-lien loan-to-values 'in the high 30% to low 40% range'". The fixer's own side finding, and Ch 17-B line 89, place that phrase in Schnabel's prepared remarks on *2025 originations*. It now reads "the loan-to-values on its 2025 first-lien originations".
- Stragglers fixed (the "We will walk away ..." quote or its paraphrase, with Miller or "president" as speaker):
  - Ch 4 line 125: speaker changed to "ARCC's management", and the quote replaced with the shared phrase. The "merits of not being a benchmark-style investor" quote is kept, now attributed to management. Its wording and speaker are still unverified, which a future pass should check.
  - Ch 4-C line 201: the LTV range is now attributed to chief executive Kort Schnabel and to 2025 first-lien originations, matching Ch 17-B. The "walk away" quote is replaced by "a heightened focus on documentation terms".
  - Ch 14 line 448: "ARCC's management has said publicly that there is 'a heightened focus on documentation terms'", with the Miller attribution dropped.
  - Ch 6 line 880: paraphrase changed from "will walk away" to "described a heightened focus on documentation terms".
- Not edited: `state/research/perspectives_buyside_credit_managers.md` line 39 still attributes the LTV phrase to Miller. Dossier follow-up.

**OCC-2011-12: confirmed (softened).** Ch 26 line 562 reads "the Federal Reserve and the OCC issued jointly on 4 April 2011, organizes validation ...". The sentence is grammatical, and the attachment supports "jointly" and the date. No "OCC Bulletin" or "2011-12" remains in `book_src/`. I tried one fetch of the occ.gov bulletin URL, which returned 404, so the number stays unconfirmed and out of the text.

**uyeda-speech: confirmed, with one straggler.** The Ch 22 line 977 entry now uses the verified wording ("approximately 165% higher than before the Commission's proposal"; the two named clearing agencies; "does not currently intend to extend these deadlines"). The process note and the false quotation are gone, and "will not be extended" appears nowhere in `book_src/`. The straggler was App Zb line 576, "Uyeda put FICC cleared volume about 165% above pre-proposal levels". The speech says daily cleared Treasury volumes, not FICC, so it now reads "daily cleared Treasury volume". The same fix went into the `state/appZ/22_ch22_market_structure_regulation_trends.md` source copy. Ch 22 line 512 still carries "(approx.; check the SEC orders)" on the CME and ICE approval dates. That is a separate claim and was left alone. The speech's "in the past year" is consistent with December 2025 and early 2026.

**Net:** 5 of 5 items confirmed. 1 fix corrected (Ch 17 LTV scope). 11 stragglers fixed in 9 files: Ch 3 (2), App Z (1), Ch 4, Ch 4-C (2), Ch 6, Ch 14, App Zb, and the 2 `state/appZ` source copies.

<!-- STATUS: COMPLETE -->
