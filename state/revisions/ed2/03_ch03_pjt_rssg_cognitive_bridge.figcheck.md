# Figure check: Chapter 3 (ed2 U4)

Chapter: book_src/03_ch03_pjt_rssg_cognitive_bridge.md. Script: tools/figures/ch03.py. Figures log was COMPLETE. House style read (tools/figures/style.py docstring). All five PNGs were opened with Read, the drawing code was read for each, and each was checked against the chapter paragraph it illustrates. After the script fixes below, ch03.py was re-run (all five figures regenerate, each under 200 KB) and the changed figures were re-viewed.

Embedding (all five): syntax is `![Figure 3.n: ...](assets/figures/ch03_*.png)`, every file exists (tools/check_figures.py reports no ch03 gaps; the six missing files it lists belong to ch02b and ch04d), numbering runs 3.1 to 3.5 in order of appearance, and each image sits directly after the paragraph whose last sentence points to it.

## Figure 3.1, ch03_mixture_vs_gaussian (3.1.2): PASS, one cosmetic fix

- Correctness: mixture p = 0.55/0.25/0.20, mu = 100/70/45, sigma = 0.5/6/12 gives mean 81.5 and sd 22.93, asserted in the script. Recomputed by hand: density ratio at 81.5 is 0.156 (16%), mass within +/-5 points is 3.5% (mixture) and 17.3% (normal), normal mass above par is 21.0%. The spike peak is 0.55/(0.5*sqrt(2*pi)) = 0.44, correctly flagged as off the chart with an arrow. The normal's right tail runs past par (shaded), which is the point of the figure.
- Honesty: caption numbers equal the script's printed values; labelled Illustrative with the chapter's stated model.
- Legibility and style: no collisions, no clipping. Blue = mixture, orange dashed = normal (direct-labelled), one y-axis, text in ink.
- Fix: the "distressed exchange, 25%" label sat up and to the left of its hump; it is now centred over the hump at 70, as the "Chapter 11" label is over its hump.

## Figure 3.2, ch03_gm_half_spread (3.2.1): PASS, one caption fix

- Correctness: derived m - b = Delta q(1-q) pi / ((1-pi)/2 + pi(1-q)) independently from the likelihoods (P(sell|V+) = (1-pi)/2, P(sell|V-) = (1-pi)/2 + pi) and it matches the chapter's formula and the script. Symmetric case reproduces pi*sigma_V with sigma_V = Delta/2 = 10 (asserted). Serta point (q = 0.7, pi = 0.3, Delta = 20) is 2.86, shown as 2.9. Left panel: the q = 0.5 and q = 0.7 curves cross at pi = 0.4 and q = 0.3 stays lowest, as the formula requires. Right panel: peaks near q = 0.52 (pi = 0.1) and 0.58 (pi = 0.3), "near a coin flip" as the caption says.
- Honesty: Illustrative, formula named. The caption used q and Delta without defining them (the definitions come after the figure, in the Full Derivation).
- Legibility and style: no collisions; the aqua curve (slot 3) is direct-labelled; the right-hand panel's grey curves are direct-labelled; the Serta point is orange in both panels.
- Fix: caption now defines q (prior probability of the good outcome) and Delta (gap between the two outcomes).
- Placement kept: the figure stays outside the "Full Derivation" block (203 such blocks in the book), so a reader who skips derivations still meets it.

## Figure 3.3, ch03_hand_replayed (3.3.5): PASS, one script fix and one chapter fix

- Correctness: systematic move 87*(-3.5*1.3*0.0020 + 3.6*0.0010) = -0.4785; capture 1.25; issuer-specific -5.5215; raw 81 - 85.75 = -4.75; IDO -4.2715 (-498bp on 85.75); Theo's counterfactual -4.0215 (-470bp on 85.5). The waterfall bars (1.25, -0.48, -5.52) sum to the raw -4.75, and IDO = 1.25 - 5.52. Bars float from the right levels; connectors line up.
- Honesty: caption numbers match the image; Illustrative with the chapter's inputs. The drift of "6 points" is 87 to 81, correct.
- Legibility and style: no collisions; diverging colours for gain/loss, grey for the market move, orange only for Theo's marker, which is labelled.
- Fix 1 (script): the sum check was `assert ... or True`, which could never fail; replaced with two real assertions (bars sum to raw; IDO = capture + issuer-specific).
- Fix 2 (chapter text, one phrase): the paragraph said the fill was on a Friday and "by Thursday the mid was 81", which is four trading days, while the figure and chapter both call it a five-day markout. Changed to "by the following Friday".

## Figure 3.4, ch03_svb_filings_timeline (3.4): PASS, two fixes in the text

- Correctness, checked independently against EDGAR (data.sec.gov submissions for CIK 719739, and the filing texts on sec.gov): seven March 2023 8-Ks with the same accession numbers, items and UTC acceptance times as tools/figures/data/ch03_svb_8k_filings.csv. Eastern conversions are right (EST before the 12 March clock change, EDT after): 8 Mar 5:16 pm, 10 Mar 5:23 pm, 13 Mar 8:27 am and 4:59 pm, 14 Mar 5:18 pm, 17 Mar 1:46 pm, 22 Mar 4:36 pm. Filing text confirms: 7.01 with $1.25bn common, $500mm mandatory convertible and $500mm General Atlantic ($2.25bn); 1.03 "The Company is no longer the parent company of the Bank"; 8.01 restructuring committee of five directors advised by Centerview, Sullivan & Cromwell and Alvarez & Marsal; 5.02 appointing William Kosturos (former CRO of Washington Mutual); 2.01 $23.97bn book for $21.45bn; 2.04 listing seven note series totalling $3.3bn. Weekday labels are right (7 March 2023 was a Tuesday); the weekend bands cover 11-12 and 18-19 March. Chapter 11 on 17 March, No. 23-10367, matches the scene.
- Honesty: Real data, source cited. The Federal Reserve review does support "over $40bn of deposits lost on 9 March" but does not give the share-price fall, so the caption's attribution of both 9 March items to the review was too broad. Day-only events are drawn as rings and the legend says so; the drill is flagged fictional.
- Legibility and style: one row per event, no collisions or clipping, legend clear, colours by role (blue EDGAR, violet drill, red petition, grey not-on-EDGAR).
- Fix 1 (caption): sources now split, the deposit outflow from the Fed review, the share fall from Nasdaq closing prices for SIVB, the 12 March event from that day's joint statement.
- Fix 2 (chapter text, decision-point note): the note said the committee 8-K had been public "forty minutes" and called it the Item 5.02 filing accepted at 4:59 pm, which contradicts the figure and EDGAR. It now says thirty-five minutes, the committee 8-K accepted at 8:27 a.m., and the Item 5.02 filing naming the CRO at 4:59 p.m. (the part the drill pulls into the morning). This resolves the observation the figures log had left open.

## Figure 3.5, ch03_cusum_detector (3.6.2): PASS, one layout fix

- Correctness: ell = (mu1/sigma^2)(y - mu1/2), S_t = max(0, S_{t-1} + ell_t), as in (3.5). Thresholds h = h0 - ln(PRS/(1-PRS)) give 3.80 (PRS 0.9) and 8.20 (PRS 0.1), asserted. Alarm day 47 is 7 days into the accumulation (days 41 to 47) and day 53 is 13 days in; the six-day gap matches the caption, and expected delays h/K = 7.6 and 16.4 give the "about nine" of Exercise 5(c). Before day 40 the tally peaks at 2.8, under both lines, as the caption says. The accumulation line is at day 40.5, between the last null day and the first shifted day.
- Honesty: Illustrative, seed 3, model stated; the script's seed search is disclosed in the figures log and caption says "one path".
- Legibility and style: the second alarm label and the top-panel note ran past the right edge of the axes, ending 7 px from the image border. Direct labels on the thresholds and alarms; alarm marks use the critical status colour with a text label; one y-axis per panel.
- Fix: x-limit widened to NS + 7 so the labels sit inside the axes; re-viewed, nothing clipped or crowded.

## Other edits to the script (no change to any image)

Stale docstring lines corrected: figure 4 no longer says "Monday 13 March zoomed"; figure 5 now points to section 3.6.2 and eq. 3.5; the figure 4 section comment now says "the fortnight of SVB 8-Ks".

## Files changed

- tools/figures/ch03.py (assert fix, mixture label, CUSUM x-limit, docstrings)
- assets/figures/ch03_*.png (all five regenerated; visibly changed: mixture label, CUSUM axis)
- book_src/03_ch03_pjt_rssg_cognitive_bridge.md (four small edits: 3.2 caption definitions, "by the following Friday", decision-point note timing, 3.4 caption sources)

## Left for the writer

- None from the figures. The "cooperation agreements signed so far: 1" vs "0" item in the figures log concerns the Serta counter and is outside the figures.

<!-- STATUS: COMPLETE -->
