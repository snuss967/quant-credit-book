# Figure check: Chapter 13 (ed2 figcheck)

Script: tools/figures/ch13.py (re-run end to end after the fixes; all asserts pass; every PNG under 135 KB, 150 dpi). Chapter: book_src/13_ch13_codifying_lmt_game_theory.md. Each PNG was viewed before and after the fixes. All five figures are "Illustrative" evaluations of the chapter's own formulas; none uses a market data series, so there are no real-data claims to source.

## Figure 13.1, ch13_serta_uptier_waterfall.png (section 13.3.1). Verdict: PASS after fixes

- Correctness: K1 = 200 + 875 = 1,075 and K2 = 2,275 match section 13.3.1. Stack equals min(V, K2) (asserted). Loss is 44.8 points at K1, crosses zero at V = 2,150 (derived: V/F = (V - K1)/((1-p)F)), bottoms at -5.2 at K2, is 0 at V >= F. Dashed pro rata line (V/2 up to V = 2,400, then 1,200) is right. Caption's "gain only above 2,150" is correct (the chapter prose ties the gain to K2 <= V < F, which is the non-positive third region; the gain actually starts at 2,150 inside the middle region, so the caption is the more precise statement).
- Honesty: caption says Illustrative, gives F, N, p, x and the Fifth Circuit source. OK.
- Legibility: slots 3 (first-out) is used and is direct-labelled. One y-axis per panel. Fixes: annotation text raised from 7.5 pt to 8 pt, reflowed so it no longer touches the blue band edge.
- Embedding: after the Serta mapping paragraph, "Figure 13.1 plots the whole schedule." Fixes: caption "K1" changed to "K₁".
- Added: assertion that each tranche is nondecreasing in V.

## Figure 13.2, ch13_sponsor_knapsack.png (section 13.4). Verdict: PASS after fixes

- Correctness: register and costs match Listing 13.2 (Appendix F). The script's exact min-cost coalition is four funds (50%) plus the 4% CLO = 54%, litigator out (asserted). Sorting by cost then size is right.
- Honesty: Illustrative, names the listing and theta, eps. OK.
- Legibility: Fixes: (1) holder names were numbered in register order but displayed in cost order (Fund 1, 4, 2, 3), now numbered in display order; (2) the free-floating "Blue/Gray" text note, which crowded the bar labels, replaced by a proper patch legend; (3) colors: invited coalition was BLUE, the opposite of the chapter's role rule (BLUE = excluded lender in 13.1), now ORANGE = invited (beneficiary) and BLUE = left out (excluded).
- Embedding: after the cost-vector paragraph, "Figure 13.2 runs the knapsack..." OK.

## Figure 13.3, ch13_coop_bargaining_shapley.png (section 13.5). Verdict: PASS after fixes

- Correctness: (a) Pi_C = d_C + eta(Pi - d_C - d_sp) gives 44/60/76 at d_sp = 0 and 20 at d_sp = 80, slope -eta, no deal beyond 80 (matches the section). (b) Shapley by enumeration for weights 25/6/3/3 at quota 1/3 equals (5/12, 5/12, 1/12, 1/12) (asserted); pro rata shares 68/16/8/8 and Shapley 42/42/8/8 each sum to 100.
- Honesty: caption says Illustrative, gives Pi, d_C, theta. OK.
- Legibility: Fixes: (1) the "no deal" label straddled the edge of the shaded band and ran past the axes, now the band is widened (xlim 112) and the label sits inside it at 8 pt; (2) Shapley bars were ORANGE (beneficiary color) although co-op members are existing lenders (BLUE in panel a and in 13.1), now BLUE, with the pro rata share staying gray (baseline).
- Embedding: after the Shapley paragraph, "Figure 13.3 plots both splits." OK.

## Figure 13.4, ch13_digital_put_vs_forward.png (section 13.6). Verdict: PASS after fixes

- Correctness: uptier loss repeats the 13.1 schedule (peak 44.8 at K1, small negative to -5.2 at K2). Drop-down loss = (min(V,F) - min((V-T)+, F))/F: V/F up to V = T = 480, flat 20 points to V = F, then declines to 0 at F + T = 2,880 (asserted max = T/F). Note: the chapter's displayed piecewise formula for DeltaR gives T/F for "V <= F" and so omits the V/F branch below T; the figure and the caption ("below V = T the loss is V/F") are right. Chapter math left untouched (outside figure scope); flagged for the prose pass.
- Honesty: Illustrative, parameters stated. Caption said the uptier loses most "where enterprise value is low", but the loss is 0 at V = 0 and peaks at K1; fixed to "when enterprise value sits near K₁". Caption's raw "D_u = T" replaced by words.
- Legibility: the label mentioned K2 but K2 was not marked; added the K2 event line. Uptier label nudged clear of the descending line.
- Embedding: after the capacity-bound paragraph, "Figure 13.4 puts the two shapes on one axis." OK.

## Figure 13.5, ch13_double_dip_structure_recovery.png (section 13.7). Verdict: PASS after fixes

- Correctness: closed form 2V/(F1+2F2) and V/(F1+2F2) below V = 1,000, then (V-F2)/F1 for the first lien to 100% at V = 1,500; 80 / 40 / 53.3 cents at V = 800 match the text. Kinks at 1,000 and 1,500 are right. Cross-checked in the script against the Listing 13.1 clearing engine at six values of V. Added: monotonicity in V, double-dipper >= first lien, full recovery at the kinks, and conservation (F2*dd + F1*first = min(V, F1+F2)).
- Honesty: Illustrative; caption now says the note is held "through the SPV" (the chapter: the new lenders collect the note payment through the SPV) and uses F₁, F₂.
- Legibility: the legend had no background, so the dashed kink lines ran through its text; the legend now has an opaque white box. Diagram arrows follow claim direction; boxes use ink text; no collisions. The kink lines are labelled by the x ticks (1,000 and 1,500).
- Embedding: after the closed-form numbers paragraph, "Figure 13.5 draws the structure and the recoveries." OK.

## Chapter-level checks

- Syntax: five `![Figure 13.n: ...](assets/figures/ch13_*.png)` lines, each alone between blank lines; all five files exist; numbered 13.1 to 13.5 in order of appearance (lines 201, 244, 316, 357, 393); no other chapter or appendix cites a Figure 13.x.
- Style: no in-image titles, no twinx, one y-axis, lines at LW, bars with white gaps, ink text, colored marks only. Role colors now consistent across the chapter: BLUE = excluded/existing lenders (13.1, 13.2 left out, 13.3 co-op, 13.4 uptier, 13.5 first lien); ORANGE = beneficiary (13.1 second-out, 13.2 invited, 13.4 drop-down series 2, 13.5 new money); gray = baseline.
- Open item for the prose pass (not a figure issue): the DeltaR displayed cases in section 13.6 omit the V/F branch for V < T.

<!-- STATUS: COMPLETE -->
