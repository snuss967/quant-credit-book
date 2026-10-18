# Verification Report, Edition 2: Chapter 20 (Credit ETF Creation/Redemption Arbitrage)

*Verifier pass, 18 Oct 2026. Chapter: `book_src/20_ch20_credit_etf_creation_redemption_arb.md`. Pre text: commit 9ac1c37 (12,655 words). Writer's starting text: commit cea2d0d (13,973 words, with the five figures and the resource graph already in). Post text: 23,090 words after this pass. Revision log carried STATUS: COMPLETE. Web calls: 14 of 15 (several returned 403/404 or snippets only; noted below).*

## 1. Nothing removed

Checked with python3 against both the 9ac1c37 text and the 13,973-word text the writer started from.

| Item | Pre | Post | Result |
| :-- | :-- | :-- | :-- |
| Headings | 25 | 41 | All pre headings present except two that were renamed or demoted by design: `### 20.5.1 The tape` is now `#### The tape` (end of the March 2020 scene, per brief item 14), and `### 20.5.3 How a systematic desk would have flagged and traded it` is now `### 20.5.3 Grading the cards: how a systematic desk would have flagged and traded it`. Sixteen new headings (Full Derivation subsections, two scenes, decision points, Quant-Shop Life). |
| Display math (`$$` pairs) | 25 | 24 | Equations (20.1)-(20.8) all present with their `\tag`s and unchanged forms. Two differences, both benign: (a) the attenuation formula lost its closing period and gained a comma (same content); (b) the definition of $\mathcal{D}$ is no longer its own display block. It now sits verbatim as an inline definition in the main text just before (20.7), and is referred back to ("as defined above") in the Full Derivation. Nothing deleted; left as is. |
| [SOURCE EXTRACTION] blocks | 4 | 4 | Quotations identical. One annotation (Dynkin p.702) lost "First ... Second ..." enumerators ("two ways" is kept; it now reads "LCS describes ... And LCS was built ..."). Content intact; left as the writer's list-to-narrative hygiene. |
| Trend Watch boxes | 3 | 3 | Identical except the removed CHECK markers (brief item 21): "by press accounts" for HYG's 2020 size, and the CHECK note on the \$64bn inflow dropped. Logged in `open_items_ch20_ed2.md`. (A fourth "Trend Watch" hit is only a pointer in the April 2025 scene.) |
| Exercises | 6 | 6 | All identical to pre. One repair, see below: Exercise 3 said "corollary (b)", but the three corollaries became narration and no "(b)" label exists any more. Changed to "the AP-count paragraph of §20.3.2". This is the only edit to an exercise. |
| Appendix F links (`#code-`) | 1 | 1 | `(#code-20-1)` present. |
| Resource Graph | 22 items / 27 URLs | 28 items / 36 URLs | Every pre URL present; post equals the 13,973-word text item for item. The two generic pre podcast bullets ("No specific episode was verified") were replaced by specific episodes in the earlier U3 pass, not by this writer. |
| Desk Myth vs Desk Reality, three Poker Tables, Ways This Blows Up, Ines's hand history, Spec schema and guards, Debrief Spec and bullets | present | present | Identical text. |
| Figures 20.1-20.5 | 0 (pre-dates figure step) | 5 + 4 `<!-- FIGURE -->` placeholders | Present with captions; not touched. |

Nothing needed restoring.

## 2. Facts

Method: python3 difflib sentence diff of pre vs post (and vs the 13,973-word text, which isolates figure-step text from writer text), every new sentence with a date, number, name or quotation read, then checked against the dossiers named in the brief and, where a quotation was printed, against a primary or transcript source.

### Verified (primary or dossier, nothing changed)

- Ramji, BlackRock Q1 2020 call, 16 Apr 2020: LQD "traded almost 90,000 times, while its top five holdings traded an average of 37 times" (Fool transcript, fetched this pass). Title "global head of iShares" is a short form of "Global Head of iShares and Index Investments".
- Fink, same call, reply to Patrick Davitt: "I object to your -- the way you framed it as a bailout." Verbatim in the transcript.
- Todorov, BIS Quarterly Review, March 2021: tracking error "above 200 basis points for some funds in March-April 2020", against "the historical average of 0.7 bp"; creation/redemption baskets about 20%/35% of holdings for US corporate bonds; holdings' bid-ask 17 times the ETF's. All match the chapter's wording ("for some bond ETFs", "March-April").
- Reuters (Kate Duguid, 23 Mar 2020, via Investing.com): Markit IG CDX bid spread "dropped as low as 120.5 basis points ... from 155.5 before the announcement". PB-13 carry arithmetic checks: 155.5 bp x \$90mm / 52 = about \$26,900 a week; LQD 0.14% x \$50mm / 52 = about \$1,350 a week.
- Zito, Apollo "Private Credit, Now in an ETF" (Bloomberg Invest conversation of 4 Mar 2026, posted 15 May 2026): title "Co-President, Apollo Asset Management"; the "CUSIP market" clause confirmed on the Apollo page; the opening of the sentence ("We're in this unique time ...") is verbatim in the dossier row 20 (the fetch tool truncated its quote).
- Virtu Q2 2025 call (30 Jul 2025): CEO Cifu, "our ETF block business, which had another record quarter", and "The volumes and volatility surrounding Liberation Day and the ongoing tariff news drove elevated client demand". The call does not mention fixed income (see fix below).
- Flow Traders (EUR 495.0m vs EUR 63.1m; "No loss days were recorded in the quarter"; Joling, "the ETF mechanism performed as intended"; AR 2025 "strategically reduced the capital deployed to fixed income"), Bank of England via Investment Executive, NY Fed Terms of Assignment clauses (27 Mar 2020), D. E. Shaw quotations and the B-1 "just below 50 on 7 April", CLO ETF \$50bn (BofA via Octus, 7 Jul 2026), JAAA \$30bn (Janus Henderson, 13 Aug 2026), \$99bn / 60% iShares (7 Apr 2025), \$89.7bn / 12% PT (8 Apr 2025): all match the dossiers (`perspectives_dealers_and_systematic_shops.md` §2.3, §5B.6, §5B.7, §5B.9, §5B.10; `trend_electronification_pt_etf_liquidity.md` rows 66, 97; `trend_loans_clos.md` rows 41-42; `perspectives_buyside_credit_managers.md` row 20). The dossier fetches were not re-run (web budget).
- Dates and weekdays: Thu 12 Mar, Fri 13 Mar, Thu 19 Mar, Mon 23 Mar, Fri 27 Mar 2020; Wed 2, Mon 7, Tue 8, Wed 9 Apr 2025 are all correct. LQD 5.0% on 12 Mar and 0.19% on 13 Mar agree with Chapter 1 §1.8.2. PB-13 (Dov Adler, Vantress, fictional composite) agrees with Chapter 12 and `state/rv_thread.md`. Noor, `holder_hhi` and the point-in-time archive agree with Chapters 13 and 15.
- Arithmetic checked: 10% x sqrt(17/365) = 2.16%, x2 = 4.3% (the old "43 bp" slip is fixed); 28/24 - 1 = 17%; resistor example (gamma-bar 1 to 2); \$50mm to \$12.5mm hill example; two-bond example (mu* = -1.2, tilts +/-0.8/theta); 1.003/0.997 = 1.006018; relay example (-2.73% in logs); thermostat series (8.33 = 25/3); wobbling-ruler slope (eta/4, 0.10); 9.2%/4.4 weeks = 2.1% a week, runway 4.8 weeks.

### Fixed in the chapter

1. **SRLN quotation was not the page's wording.** The chapter printed "on a trade-date basis including unsettled positions" as a quotation from the SSGA SRLN page; that was the dossier's paraphrase. The page (fetched, as of 15 Oct 2026, net assets \$5,384.74m) says: "Calculations are performed on a trade date basis and are intended to include both settled and unsettled positions." The sentence now quotes that, and the inference is restated as ours ("on paper the fund counts loans it has not finished buying, and has stopped counting loans it has sold but not finished delivering"). Theo's quip now says "the page" instead of "the holdings file".
2. **Virtu.** The text said Virtu called Q2 2025 a "record" for ETF block trading and then generalised ("on the evidence of the calls, the firms paid best ..."). The call is a single call, never mentions bond ETFs, and Cifu's words are "another record quarter". Rewritten with the verbatim phrase, an explicit note that the call did not break out bond ETFs, and the link to this wrapper labeled as our inference.
3. **Flow Traders box.** "an intermediary who was hedged, quoted wide on record volume and never had to sit with the basket" asserted facts about the firm's risk that no source gives (Joling actually cites "heightened risk"). Now: "an intermediary that quoted wide on record volume and reported no loss days."
4. **PRIV SEC letter timing.** "sent the day after" is not established (coverage this pass places the letter on or about the launch date, 26-27 Feb 2025). Now "Press coverage in the days around the launch reported a public letter from SEC staff raising liquidity (Rule 22e-4), valuation and naming concerns."
5. **CDX carry.** CDX IG trades on a fixed 100 bp coupon plus upfront, so "pays the index spread" was loose and "on the morning of 23 March" over-read Reuters' "before the announcement". Now "In spread-equivalent terms the protection leg pays the index level, which Reuters put at a 155.5 bp bid before the Fed's announcement on the morning of 23 March".
6. **Coalition Greenwich 8 Apr record.** The dossier flags a conflicting \$92bn record on 30 Apr 2025. "a record of its own" is now "a then-record of its own".
7. **BlackRock Systematic Fixed Income chair.** The dossier says the systematic arm's paper is undated and quotes 2022-2023 figures, with the 2020 link "mine, not the authors'". The text implied it was a March 2020 view. Now: "its own undated high yield paper argues that the average manager turns defensive at the wrong time (the paper's figures are for 2022 and 2023, not 2020)", and the closing contrast of the three chairs is prefaced "On our reading".
8. **Exercise 3 cross-reference** (dangling "corollary (b)"), as in section 1.
9. **Currency escape.** `$50mm` in the `ch20_pb13_attribution.png` FIGURE comment is now `\$50mm`.

### Real people and fiction labels

No invented words for any real person. The only words in real mouths are verbatim quotations from sources: Ramji, Fink, Joling, Zito, Cifu (via the verified phrase), D. E. Shaw and Flow Traders (firm statements). Everything said by Ines, Kaz, Theo, Mags, Noor, Dov, the sponsor's capital markets desk and the vendors is fictional and labeled: the cold open (italic note), the 8 April 2025 scene (italic note, "(fictional)" and "(the desk's fictional run)" on every desk number, no HYG premium printed), the 19 March 2020 scene (italic note: cast, cards and Pair Book sizes fictional, market facts real), PB-13 ("fictional composite"), the assignment clause ("generic, a composite of common market language"), and Quant-Shop Life ("A fictional composite"). Mags's employer is never named ("a dealer's distressed desk", "the bank"), consistent with the cast bible.

## 3. Hygiene

- No code fences anywhere in the chapter (none needed; no ```text diagrams are present).
- `$$` count 48 (even); no paragraph with unbalanced inline `$`; brace and `\left/\right` counts balance in every display and inline expression.
- Currency: all dollar amounts are `\$`; the one stray (item 9 above) is fixed.
- No `---` lines in the chapter.
- Last line is `<!-- STATUS: COMPLETE -->`; the file ends with a single newline.
- Cross-references checked: §20.5.1 "The tape", §20.4.3 scene, Trend Watch pointers, Finder table sections, `#code-20-1`.

## What remains doubtful

1. Four items rest on the dossiers' own fetches and were not re-read at source: the NY Fed Terms of Assignment quotations (27 Mar 2020), the D. E. Shaw paper (including the B-1 level, which the dossier calls a paraphrase), the Flow Traders release and the Investment Executive article. The Coalition Greenwich \$89.7bn / 12% figures are Trumid-sourced secondary coverage with a conflicting report in the dossier.
2. The Ramji and Virtu quotations come from a machine-assisted transcript (Fool); wording matches, but audio was not checked.
3. The first half of the Zito sentence is verified through the dossier, not through this pass's fetch.
4. PRIV: launch date (26 or 27 Feb 2025) and the exact date of the SEC letter are still not nailed down; the chapter now avoids stating either. The "contractual arrangement for Apollo to provide intraday bids" is carried from the pre text and was not re-verified.
5. `open_items_ch20_ed2.md` rows 12-14, 17 and 18 are now closed by this pass; row 18's quotation has been corrected. Rows 1-8 (BKLN AUM, \$64bn May 2026 inflow, HYG peak size, pre-rule exemptive orders, 17-day settlement, BKLN sleeve and cash practice, PRIV letter, ETF share classes) remain open and are hedged in the text.
6. Story-clock note, not a fact error: the 8 April scene says "in his fifth week", while the cast bible puts Ch 10 (15 Oct) at week four. Left for the cast-bible pass.

<!-- STATUS: COMPLETE -->
