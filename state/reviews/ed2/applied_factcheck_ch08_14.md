# Applied fact-check changes, Chapters 8-14 (Edition 2, WP1)

Source: `state/reviews/ed1/factcheck_ch08_14.md`. Applied 2026-10-18 with the Edit tool only. Each entry: file, verdict class, before, after.

Counts: 5 CORRECTED applied (find/replace pairs 1-5, all matched exactly once, no re-location needed); 0 STALE (none in report); 15 hedge edits for UNVERIFIABLE items covering 17 of the 24 UNVERIFIABLE claims (report pairs 6-11 plus table-suggested hedges). Total 20 Edit calls, 6 files, 15 diff hunks. Web calls: 0. Final `<!-- STATUS: COMPLETE -->` line is intact as the last line of all seven chapter files.

## A. CORRECTED (5)

### A1. `book_src/08_ch08_isolating_ido_and_empirical_duration.md` line 280 (Box 8.2, mixed dates; report pair 1)
- Before: The CCC OAS reached 12.82% on October 14, 2026, while the broad HY OAS was 3.23% and IG 0.84% (computed 2026-10-17).
- After: The CCC OAS reached 12.82% on October 14, 2026 (HY 3.25%, IG 0.84% that day); on October 15 the CCC OAS was 12.78%, the broad HY OAS 3.23% and IG 0.84% (computed 2026-10-17).

### A2. `book_src/10_ch10_trend_and_time_series_momentum.md` line 389 (Box 10.2, Man's "only twice" includes 2025; report pair 2)
- Before: a 12-month loss deeper than 15% had happened only twice before (Man Group, *Trend Following and Drawdowns: Is This Time Different?*)
- After: the index had lost more than 15% over a rolling 12 months only twice in its history, this episode and January 2019 at −16.0% (Man Group, *Trend Following and Drawdowns: Is This Time Different?*)

### A3. `book_src/12_ch12_multi_asset_credit_allocation.md` line 455 (Box 12.4, 26 trading days; report pair 3)
- Before: *What happened:* a regime transition in about 25 trading days. The HY OAS moved from 259 bp (January 22) to 461 bp (April 7);
- After: *What happened:* a regime transition in about 26 trading days of drawdown (February 28 to April 7). The HY OAS moved from 259 bp (January 22) to 461 bp (April 7);

### A4. `book_src/12_ch12_multi_asset_credit_allocation.md` line 455 (Box 12.4, MacKay quote wording; report pair 4)
- Before: "22 bps wider than the post-2008 tights earlier in 2025," after 12 straight quarterly gains, the longest run since 1997
- After: "only 22 bps wider than the post-2008 tights reached earlier in 2025," after 12 straight quarterly gains, the longest run since 1997

### A5. `book_src/14_ch14_default_and_recovery_cycle_lmt_era.md` line 382 (Box 14.3, 8-K date vs preferred sale date; report pair 5)
- Before: On 1 June 2026 Optimum moved Optimum East and its 50.01% Lightpath stake into an unrestricted "Unsub Topco" and raised \$300mm of preferred (Optimum 8-K, 1 June 2026).
- After: In an 8-K filed on 1 June 2026, Optimum disclosed that it had moved Optimum East and its 50.01% Lightpath stake into an unrestricted "Unsub Topco", which sold \$300mm of preferred on 29 May 2026.

## B. STALE (0)

None in the report.

## C. UNVERIFIABLE, hedge applied (15 edits)

### C1. `book_src/08_ch08_...md` line 187 (Box 8.1, 0.58; report pair 6)
- Before: It turned positive in 2021 and was roughly 0.58 for full-year 2022 and 2023 (approx.; same source).
- After: It turned positive in 2021 and was roughly 0.58 for full-year 2022 (approx.; secondary summaries of Morningstar's data, which differ on 2023).

### C2. `book_src/08_ch08_...md` line 531 (Box 8.3, HYGH effective duration and "roughly 4% of HYG"; report pair 7; covers two UNVERIFIABLE claims)
- Before: it showed an effective duration of −0.01 years and net assets of about \$652mm, roughly 4% of HYG's size (ishares.com)
- After: it showed an effective duration near zero and net assets of about \$652mm, a small fraction of HYG's size (ishares.com)

### C3. `book_src/09_ch09_factor_investing_in_credit.md` line 469 (Box 9.2, "fivefold overnight"; report pair 8)
- Before: in a stress month it can jump fivefold overnight
- After: in a stress episode it can rise several-fold within months (Barclays IG LCS: 0.4% in 2007, 2.8% in 2008)

### C4. `book_src/10_ch10_...md` line 389 (Box 10.2, YTD at end-April 2026; report pair 11)
- Before: +10.13% year to date by end-April
- After: about +10% year to date by end-April

### C5. `book_src/10_ch10_...md` line 389 (Box 10.2, Man AHL AUM; table hedge "about $39bn (Man AHL, mid-2026)")
- Before: Man AHL reports \$39.4bn of trend-following AUM across "900+ traditional and alternative markets" as of 30 June 2026.
- After: Man AHL reports about \$39bn of trend-following AUM across "900+ traditional and alternative markets" as of mid-2026.

### C6. `book_src/11_ch11_defensive_systematic_high_yield.md` line 634 (Box 11.2, S&P 5.1% and 68%; table hedges; two UNVERIFIABLE claims in one sentence; the existing "(approx.; S&P reports via search summaries, primary pages not accessed)" parenthetical is kept)
- Before: S&P reported the US trailing-12-month speculative-grade default rate at 5.1% in December 2024 and put distressed exchanges at about 68% of 2025 defaults through April, the highest year-to-date share since 2008 *(approx.;
- After: S&P put the US trailing-12-month speculative-grade default rate near 5% at the end of 2024 and put distressed exchanges at well over 60% of defaults in early 2025 *(approx.;

### C7. `book_src/11_ch11_...md` line 876 (Box 11.3, HYDB methodology; table hedge)
- Before: selected and weighted by default probability, default-adjusted spread, and volatility, held
- After: selected and weighted by a systematic default-risk model, held

### C8. `book_src/14_ch14_...md` line 55 (Box 14.1 Baseline, S&P shares; table hedge, "as cited by FTI Consulting" attribution kept)
- Before: S&P counted distressed exchanges at about 32% of rated US corporate defaults over 2010–2023, then at roughly 50% for three consecutive years to mid-2024 (S&P,
- After: S&P counted distressed exchanges at roughly one-third of US defaults over 2010–2023 and about half in the years to mid-2024 (S&P,

### C9. `book_src/14_ch14_...md` line 56 (Box 14.1 2024, Moody's 63% and quote; table hedge)
- Before: Distressed exchanges were about 63% of Moody's-rated defaults, "the highest annual share on record, with data going back to the 1980s" (Moody's AMR, 6 March 2025).
- After: Distressed exchanges were roughly three in five Moody's-rated defaults, a record share (Moody's AMR, 6 March 2025).

### C10. `book_src/14_ch14_...md` line 57 (Box 14.1 H1 2025; table hedge)
- Before: **H1 2025.** 64% of defaults, "about the same pace as all of 2024," concentrated in
- After: **H1 2025.** About 60% of defaults in the first half of 2025, similar to 2024, concentrated in

### C11. `book_src/14_ch14_...md` line 244 (Box 14.2, repeat exchanges counted as re-defaults; table hedge "reportedly counts")
- Before: That figure counts repeat exchanges as re-defaults.
- After: That figure reportedly counts repeat exchanges as re-defaults.

### C12. `book_src/14_ch14_...md` line 246 (Box 14.2, CLO view; table hedge, with the two other relayed figures kept but softened to "about" so no content is deleted)
- Before: After an LME, 33% of issuers filed for bankruptcy, 56% re-defaulted or were rated CCC+ or below, and 10% repaid or reached B- or better (S&P BSL CLO research, as cited by Wellington, 1 April 2026; secondary).
- After: S&P CLO research, as relayed by Wellington (1 April 2026; secondary), finds that roughly a third of issuers filed after an LME, about 56% re-defaulted or were rated CCC+ or below, and about 10% repaid or reached B- or better.

### C13. `book_src/14_ch14_...md` line 247 (Box 14.2, Mitel; report pair 9)
- Before: Mitel: uptier October 2022, Chapter 11 on 10 March 2025, about 29 months
- After: Mitel: uptier October 2022, Chapter 11 in March 2025, about 29 months

### C14. `book_src/14_ch14_...md` line 247 (Box 14.2, Del Monte; report pair 10)
- Before: Del Monte Foods: a 2024 financing (reported as August 2024; terms not verified here), Chapter 11 on 1 July 2025, about 11 months
- After: Del Monte Foods: a 2024 financing (reported as August 2024; terms not verified here), Chapter 11 in July 2025, about 11 months (docket date not verified)

### C15. `book_src/14_ch14_...md` line 382 (Box 14.3, 10-Q going-concern warning and maturities; table hedge)
- Before: Its Q2 2026 10-Q carries a going-concern warning, with \$4.12bn maturing in April 2027 and \$2.225bn in July 2027.
- After: Optimum's filings flag substantial near-term maturities (details to be checked in the Q2 2026 10-Q).

## D. UNVERIFIABLE, no change (7 claims; the report gives no hedge wording, says "consistent", or recommends no change)

- Ch8 Box 8.3: HYG effective duration about 3.2 years vs 4.2-4.8 in Ben Dor (no hedge suggested; context only).
- Ch14 Box 14.2: Serta 22 Jun 2020 to 23 Jan 2023; Wesco/Incora 1 June 2023; Robertshaw 15 Feb 2024 (all marked "consistent").
- Ch14 Box 14.3: "a June 2024 co-op claims about 99% of it" (marked "partly"; no hedge wording given); Sharon Steel v. Chase Manhattan defense ("No change recommended"); Baker McKenzie Jan 2026 backlash claim (no figures).

## E. Notes for the next editor (observed, not changed, outside this report's instructions)

- `14_ch14...md` line 247 still ends the Box 14.2 names bullet with "Filing dates are from the S.D. Tex. and D.N.J. dockets." The fact-check could not access the dockets (Mitel, Del Monte, Wesco, Robertshaw dates), so this sentence overstates the sourcing; consider softening in WP1/WP6.
- `14_ch14...md` line 406 (chapter-body timeline, not a Trend Watch box) gives "Del Monte Foods. Chapter 11 on 1 July 2025 (Bankr. D.N.J. 25-16984)". It was not in this report's scope and was left as is, but it carries the same unverified date.
- `13_ch13` has no CORRECTED or UNVERIFIABLE rows and was not touched. `grep -c CHECK` on ch8-14 shows 0 flags (the four hits in ch08 are the `CHECKS` Python dict, not fact flags).
- Word counts moved by at most 0.1% per chapter (ch08 18142 to 18159, ch09 17331 to 17341, ch10 17538 to 17551, ch11 15573 to 15568, ch12 15560 to 15569, ch14 14536 to 14534).

<!-- STATUS: COMPLETE -->
