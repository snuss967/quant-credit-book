# Verification Report, Edition 2: Chapter 7 (ML on Small-Sample, Non-Stationary Credit Data)

Chapter: `book_src/07_ch07_ml_on_small_sample_credit_data.md` (1,020 lines after fixes; pre-revision text from commit 9ac1c37, 622 lines).
Revision log gate: `07_ch07_...log.md` carries `<!-- STATUS: COMPLETE -->`; no prior verify report existed.
Web calls used: 8 of 15 (WBS x3, arXiv PDF, Fed SR 11-7 PDF, Aarhus seminar page, Open Bond Asset Pricing, one web search for Bloomberg show notes). Full text of the 2026 audit (arXiv:2604.07880) and SR 11-7 were read from the saved PDFs.

## Check 1. Nothing removed

Method: python3 comparison of pre and post by headings, display math, inline math, boxes, extractions, exercises, links, and sentence-level coverage.

| Item | Pre | Post | Result |
| :--- | :--- | :--- | :--- |
| Headings (all pre headings present) | 22 | 30 | 0 missing; 8 new `####` subsections (5 "When to ..." practitioner passages and 3 "The Full Derivation" subsections) |
| `$$` delimiters (display blocks) | 42 (21 blocks) | 42 (21 blocks) | every pre block present verbatim, whitespace-normalised |
| Inline math expressions | 254 | 349 | 0 pre expressions missing |
| [SOURCE EXTRACTION] blocks | 13 | 13 | all verbatim |
| Trend Watch boxes (the two boxes) | 2 | 2 | intact (the count of the phrase rose 4 to 5 only because Scene 2 refers to the box) |
| Ways This Blows Up / Poker Table / Desk Myth boxes | 5 / 2 / 1 | 5 / 2 / 1 | intact |
| Exercises and their Checks | 6 / 6 | 6 / 6 | intact |
| Appendix F links `#code-7-1` to `#code-7-6` | 6 | 6 | intact |
| Resource Graph items | 40 | 42 | none missing; 2 added (Paleologo, Ralph Smith) |
| Tape-these-to-the-monitor list, Ad Hoc Group note, Coase epigraph, "open market purchase", Four defined term | present | present | intact |

Sentence-level coverage: 34 pre sentences are not found verbatim. All accounted for:
- Cold-open syllabus (i)-(viii): rewritten as the two-paragraph promise; all eight competencies are present in prose (checked one by one).
- "Start with the desk framing" and "The rest of the chapter is a repair manual": folded into the Theo-archaeology opening of §7.1.
- §7.6 "From uniqueness to weights": turned into the Kaz/Theo/Mags dialogue. Return attribution formula, time decay, normalisation to the label count, Kish size, and "use with care in credit" are all still present.
- §7.7 "The group" and "Group by parent" paragraphs: content moved into the Model Review Tuesday vignette (§7.5) and the §7.7 text; the two-way split formula and cost sentence are retained (only the connective "You need both." is gone).
- Bold lead-ins "The derivation." and "The scale, derived.": replaced by the new "The Full Derivation" headings; the derivations themselves are intact.
- Six `Code Companion: Listing 7.x` stubs and six `<!-- EXPLAIN -->` placeholders in §7.12: replaced by the listing explanations and a `*The full listing is [Listing 7.x in Appendix F](#code-7-x).*` line. The Appendix F links are preserved. This replacement is the U1 pass's work, not the Ed2 writer's (the log marks §7.12 as BRIDGE only); noted, not restored.

Restored: nothing needed.

## Check 2. Facts (new claims, verified against the dossier and primary sources)

Verified and left as written:
- Dickerson, Mueller, Robotti, "Priced risk in corporate bonds", JFE 150(2), 103707, Nov 2023; "with traded liquidity as the only marginal exception" (dossier B2, Crossref abstract).
- Bai, Bali, Wen, JFE 131(3), four factors; retraction notice JFE 150(3), 103721, Dec 2023; "fourteen months after the PM's request" (14 Oct 2022 to Dec 2023) is correct. 14 Oct 2022 was a Friday; 14 March 2017 a Tuesday (Kaz's label scene); 15 October 2026 close shown on Friday 16 October.
- Warwick Business School, 10 September 2024 (Robotti's first-person article): quotes re-read on the page. "two of the remaining three factors had a 'lead error', while the third factor had a 'lag error'", "while artificially capping their losses over a given holding period", "has been cited more than 400 times in other papers according to Google Scholar", "This is the first time this has happened." All verbatim.
- Warwick, 9 September 2024, Fama-DFA Prize news item: winners named Robotti and Mueller; the quote "Once we corrected these errors, we found the formula provided no investment advantage at all." is on that page (not the 10 September page), exactly as the chapter says ("a day earlier").
- Robotti, Aarhus finance seminar, 11 April 2024, "Common pitfalls in the evaluation of corporate bond strategies": abstract does say microstructure noise in transaction-based prices and ad hoc, asymmetric winsorization/trimming.
- Open Bond Asset Pricing hosts the "correctly constructed" BBW four factors (site wording).
- 2026 audit (DRR, "The Corporate Bond Factor Replication Crisis", arXiv:2604.07880): 108 signals; 432 specifications; 26 survive BH-FDR; 65 of 432 with CAPM-B alpha t above 1.96 (dossier IA.3); four BH panels (VW/EW by single-sort/within-firm); 25 of 26 within-firm and bond age (EW) the lone single-sort survivor (dossier); footnote-9 example (noise of +/-0.50% gives a 1.00% measured long-short against a true zero); 6-month momentum 0.30% to zero; 57-78% of ivol and downside-risk alpha from ex-post filtering; placebo Table B.1 (43-67% of 30 price-based factors, 0.13-0.30%/month; 10-18% of 78 non-price factors, 0.03-0.10%); cumulative $12 vs $1.1 (adjusted signal) and $1.4 (adjusted return).
- SR 11-7, p.12: "...change control procedures to ensure that the code is correct, that it cannot be altered except by approved parties, and that all changes are logged and can be audited." The chapter's two quoted fragments are faithful.
- Paleologo: Bloomberg's summary calls him former director of risk and quantitative analysis at Citadel and head of enterprise risk at Millennium; the chapter's biography matches. Odd Lots episode date 20 May 2024 confirmed. The chapter paraphrases and quotes nothing; transcript is machine-made and flagged unverified.
- Ralph Smith (BlueCove), Flirting with Models S5E7, 11 July 2022, and Robeco 23 June 2023: match the dossiers and the existing fact-checked Trend Watch box.
- Math numbers re-derived: BH thresholds (p below 0.00012, t about 3.85; 26th at 0.003, t about 2.97), $\Phi$ sizing map (0.44, 0.82), weights for d = 0.4 (partial sum 0.37; about 7% at 280 lags), ADF half-lives (35 and 690 days), shuffled K-fold neighbours (124, about 100 in training), overlap factor 190, Kish 1.2, SE example, best-of-3,000 about 0.23/month, denominator 1.08.
- Internal cross-references (§3.1.2, §3.1.3, §3.2.2, §5.1.1, §5.1.3, §5.2.3, §6.3, §21.4.1, Chapter 18) all exist and cover what the box says.

Wrong, fixed in the chapter:
1. **Short-term reversal -0.09% (t = -0.51) was labelled "month-begin return".** The paper's Table 1 and text (p.17) say it is the signal-adjusted (signal gap) figure; the month-begin (return-adjusted) figure is -0.17%. This error came from the brief and was also in the Ed1 text. Fixed in four places: Scene 2 numbers paragraph, Kaz/Theo exchange after it ("a few days", not "one business day"), the §7.9 "The fix is a gap" paragraph, and Case Study C. The 91% share is the signal-gap figure and stays.
2. **"worst day of April 2025" for the CCC OAS** (Scene in §7.1): the FRED figure in the Ed1 text is 11.37% at the April 2025 panic; reworded to "the 11.37% it had reached at the April 2025 panic".
3. **Resource Graph, Fama-DFA item** said the prize was awarded to Dickerson, Mueller, and Robotti; the 9 September 2024 page names Mueller and Robotti. Reworded to "won by Mueller and Robotti for the paper they wrote with Dickerson".

Hedged or softened:
- "Forty energy issuers in late 2015" (an unsourced count): now "Dozens of energy issuers".
- Open Bond Asset Pricing "rebuilt with the corrected timing": now quotes the site's own phrase, "correctly constructed".
- Scene 2: "from August 2002" cumulative dollar changed to "start of the 2002 sample" (the paper's Figure 3 sample runs 2002-09 to 2024-12); "the paper's own toy example" now says the example is turned into a reversal trade (the paper's footnote uses a generic price-based signal).
- Paleologo box: added that the risk-desk reading of Kaz's slide is the book's, not the guest's; Resource Graph "Why" tag no longer attributes the multiple-testing reading of PM hiring and the stop-loss-as-out-of-sample-test idea to the guest.

Real people and quotes: Dickerson, Mueller, Robotti, Rossetti, Paleologo, Ralph Smith, and the Bianchi-Buchner-Tamoni-Hoogteijling authors appear only through published or press-quoted words or labelled paraphrase. No invented dialogue for any real person. Scenes 1 and 2, the Model Review Tuesday vignette, Case A/B/C desk epilogues, and the Debrief composite company are labelled fictional/illustrative in their openers or inline. The CLO seat is generic with hedged "typical terms" (7.5% CCC bucket, discount-obligation 80-85 threshold; Ch 21 states the same convention).

## Check 3. Hygiene

- Code blocks: one fence pair, ```text (the ROBO spec diagram). No other fences.
- Math delimiters: 42 `$$` (even, all blocks closed); no line with an odd number of inline `$`; no prose-looking math spans, so no unescaped currency was swallowed as math. Five `\$` currency escapes present (\$12, \$1.10, \$1.40 in Scene 2, and the two amounts in the §7.10 plumbing bullet).
- No standalone `---` lines. No em dashes. One HTML comment in the file, the final status line.
- Last line is `<!-- STATUS: COMPLETE -->`.

## What remains doubtful

1. Ch 5 §5.1.1 already carries a bookmaker/horse box for $\mathbb{P}$ vs $\mathbb{Q}$ (the brief said cross-reference instead of duplicating if so). The Ch 7 box uses a different number (400bp CDS, 6.7%) and cross-references §5.1.1 and §6.3, but the horse-race analogy is repeated. Left in place; the editor may want to trim the analogy to one sentence.
2. The §7.12 listing explanations (35,934 labels, N_eff near 2,700, AUC 0.71 vs 0.50, DSR 0.59, and so on) were written by the U1 pass and were not re-run here.
3. Paleologo's episode is paraphrased from an unverified machine transcript; the chapter says so. The biography line relies on Bloomberg's show-note summary seen through a search result, not the paywalled page.
4. The dossier's "typical about one business day" gap and the paper's "1 to 10 business days" signal gap are both used correctly now; the dossier note that the DRR paper is under revise-and-resubmit (v4.2.1 pipeline) means numbers may move in later versions.
5. Scene 1 and Case A treat October 2022 as a replay run in 2026 (consistent with Theo's PJT tenure 2020 to September 2026 in the cast bible); Case A says the memo was "three years late" relative to the December 2023 retraction, which is approximate.

<!-- STATUS: COMPLETE -->
