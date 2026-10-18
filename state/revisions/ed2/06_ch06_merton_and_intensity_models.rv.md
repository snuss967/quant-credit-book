# RV weave log: Ch 6 (Merton and intensity models), Edition 2, user directive 13

*RV weaver, 2026-10-18. Thread entry: `state/rv_thread.md` §(e), row `06_ch06_merton_and_intensity_models` (scene, replay; PB-04 opened; tool: Merton, KMV, equity leads credit; H equity delta, I the CDS–equity gap, L the rate delta and the delta at a stock jump; event: 2001–04 window, Sharpe 1.2, \$66 per \$100 notional, PAIRS R1; home Ch 23 §23.6). Preconditions checked: thread COMPLETE; this log did not exist; `06_ch06_merton_and_intensity_models.log.md` ends COMPLETE (no reviser mid-flight).*

## What I wrote, and where

1. **New scene, §6.9.2, lines ~792–833:** `#### The Pair Book, PB-04: General Motors, a replay cut off at the close of 3 May 2005` (1,993 words including heading and label). Placed after the log-linear-intensity Math, Gently box and before §6.9.3 (First Brands, "a firm with no equity ticker"), so the chapter goes from the hedge that needs a stock to the firm that has none. Prose, not a box, so no three-boxes-in-a-row problem.
   - **Frame.** Ines's Friday replay (C14), cut off at the close of Tue 3 May 2005; Owen Achterberg as Theo's guest (Theo knew him before the desk); Mags sits out ("I was there"). Fiction label in italics at the top; model outputs on GM marked "the desk's fictional run"; costs marked illustrative.
   - **Chapter tool.** KMV inversion (§6.4) → Merton five-year spread too tight for nearly everyone (§6.2.4, §6.3.3), so the signal is the gap against GM's own history. Hedge ratio derived from §6.2.3 by the chain rule, one display equation (unnumbered): $\partial B/\partial E=N(-d_1)/N(d_1)$; stock short per \$100 of protection $=100\,N(-d_1)E_0/(N(d_1)F)$. Fictional run $N(d_1)=0.75$, $E_0/F=0.12$ (checked consistent with Merton: $V/F\approx0.91$, $\sigma_V\approx8.2\%$, $T=5$, model spread ~68 bp) → ratio 1/3, \$4 per \$100, \$0.4mm against \$10mm sold.
   - **Isolation, explicit.** Legs: sell \$10mm GM 5y protection (long credit, unfunded) / short \$0.4mm GM common, borrowed. Hedge removes: firm direction (Schaefer–Strebulaev "quite accurate predictions..."; Barclays ~5% in §6.2 Trend Watch). Idio left: the CDS–equity gap; GM stock–CDS correlation −0.32 (DLY p.789, minus sign verified in the PDF glyph) so the best hedge removes ≈10% of variance, ~90% is the gap; hence \$66 per \$100 capital (IG rows \$45–\$52; swap-spread about \$8, DLY Tables 1 and 5); Owen books \$4.7mm. Leaks: rate delta (~\$1,000/bp, check number: §6.2.4 firm at T = 5, ∂s/∂r ≈ −0.25 bp/bp, × RPV01 4 × \$10mm) left open on Schaefer–Strebulaev's "does not capture the interest rate sensitivity of corporate debt"; short vega twice (§6.2.4 firm, σV 25 → 30%: E 24.78 → 25.87, spread 216 → 362 bp, debt −1.09, short stock −0.15 at h = 0.135); the delta at a stock jump (Theo's list of equity-holder events that are not moves in V); a forced-seller factor one notch from HY; JTD unhedged (\$6mm at R 40 vs \$0.4mm).
   - **Costs.** Running premium at an illustrative 500 bp (\$500k/yr); DLY 5% bid–ask → 25 bp wide → \$50k each way; GC borrow 25 bp (\$1k/yr) offset by rebate; dividends owed at an illustrative 7% (\$28k/yr); 180-day carry ≈ \$136k, 2.9% on \$4.7mm; idio worth \$4,000 per bp of convergence.
   - **Decision card** posed before the answers; four cards that disagree (Owen: vol; Theo: equity-holder events/downgrade; Kaz: re-estimate the delta after a >10% move; Mags: "who else is in it", crowding, T11); sealed in a *4 May* envelope, graded in Ch 23.
   - **Cross-reference to canonical home:** the last sentence, "the two trading days after the cut-off are Chapter 23's to deal (§23.6)". No 4–5 May facts told here (blind replay; Ch 23 Case Study A owns them).
2. **Consistency fix, §6.10.1 Decision point (line ~892).** The Carvana re-hedge said the model wanted "*more* short stock per bond" as DD rose; the ratio $N(-d_1)/N(d_1)$ falls as $N(d_1)$ rises, so it now says "*less* ... a trim rather than a cut" and points to §6.9.2. Ines's half-cut and Kaz's dissent still read correctly.
3. **Finder table (§6.13), new row** after the log-linear intensity row: Merton equity hedge ratio · $\partial B/\partial E=N(-d_1)/N(d_1)$ (§6.9.2) · box §6.2.3 · scenes PB-04 (§6.9.2) and Kaz's trim (§6.10.1) · `_d1d2` in Listing 6.2.
4. **Resource Graph after §6.10.3 (line ~962):** added Duarte, Longstaff and Yu (2007) with the author-hosted URL from the PAIRS dossier, and BIS QR June 2005 URL. Nothing removed.

## One telling per fact

No older paragraph told the capital-structure pair on GM, the DLY evidence or Schaefer–Strebulaev in Ch 6 (Schaefer–Strebulaev was only in a Resource Graph), so nothing was retired. Theo's §6.2.4 notebook line ("hedge ratios ... survives the model's other sins") stays as the claim; the scene is the test, and it points back to the §6.2 Trend Watch instead of restating it. No topic, equation, Source Extraction, Trend Watch, exercise, figure, Appendix F link or URL was removed. Chapter 36,927 → 39,033 words (wc).

## Sources used

DLY 2007 read in full for this beat (PDF fetched to the scratchpad from the dossier's URL): sample p.788; GM vignette, "ever more expensive", Oct 2002 >440 vs <300, Feb 2003, Aug 2002, correlation −0.32 on p.789; rule, 180 days, 5% bid–ask, "convergence occurs for only a small fraction" on p.790; Table 5 on p.791; trigger 0.5 on p.792. BIS QR June 2005 p.6 via PAIRS R22 (3% IG, 15% HY). Schaefer–Strebulaev 2008 via PAIRS R8 (abstract quotes). GM at BBB- before 5 May inferred from Ch 23's "two notches to BB" (stated as "last rung of investment grade at S&P").

## State files updated

- `state/rv_pair_book.md` PB-04: legs corrected and filled, method, opened Ch 6 §6.9.2, status open (replay as of 3 May 2005), ratio at open, idio share (~0.90 of CDS-leg variance), what leaked, carry.
- `state/cast_bible.md`: Theo row (Ch 6, GM replay card), Mags row (sits out, "who else is in it"), Owen line (first on-page meeting with the desk, PB-04 opened, two lines).

## Open items for the orchestrator

- **Thread wording.** `rv_thread.md` §(d) row PB-04 reads "GM 5-year CDS protection / GM common stock"; with the ledger's old "Long 5-year GM CDS protection" this was short credit on both legs. DLY's rule (and Ch 23 §23.6's) sells protection when CDS is rich. Ledger now says "sell protection (long GM credit)"; the thread file was not edited.
- **RV figure not drawn.** The thread allows one (capital per \$100 notional, DLY Table 5). Ch 6 has no figures yet and no `tools/figures/ch06.py`; left to the U4 figure stage. Table 5 values: IG \$47.0 / \$52.3 / \$44.9, HY \$86.9 / \$90.5 / \$75.9, EW \$66.25; swap-spread from Table 1.
- **PB-05 in Ch 6.** The ledger lists Ch 6 as PB-05's stress chapter and Ch 5 §5.6.1 books PB-05 to Owen's pod; Ch 6 §6.10.1 Scene B already stresses the Carvana bond/stock pair on Ines's desk, unnumbered. A later pass may label it PB-05 or leave Scene B as the desk's own version.
- **Exercise.** No pair exercise added (App Z handles "one pair exercise per chapter"); a natural one is the vega check at different numbers (e.g. σV 20 → 25% on the §6.2.4 firm).

<!-- STATUS: COMPLETE -->
