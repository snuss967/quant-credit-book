# Figure check (Edition 2): Chapter 12-B, The Restructuring Process as a State Machine

Script: tools/figures/ch12b.py. Five embeds, numbered 12-B.1 to 12-B.5 in order, each file present in assets/figures/, each with a pointer sentence in the text next to the image. All PNGs re-viewed after the final run; all under 500 KB.

## Figure 12-B.1, ch12b_out_of_court_machine.png (§12B.4)
- Correctness: PASS. Nodes and edges match the §12B.4 transition table: Performing to Stressed, Stressed to Grace to Event of default, Grace or EoD to Forbearance (Grace edge dashed), Stressed to Post-LMT with the s >= theta_eff and 90% tender guards, the Post-LMT to Stressed re-default edge highlighted, any distressed state to RSA-signed (2/3 in amount, over 1/2 in number) and to Petition (free-fall), RSA to Petition (prepack), Petition to Chapter 11. Clocks (30-day grace invariant, 20 business days under Rule 14e-1) match the table.
- Honesty: PASS. Source given (transition table, Rule 14e-1, §1126(b)), "no particular borrower".
- Legibility and style: PASS. No collisions or clipping; text in ink or muted; border colours explained by an in-image key (colour is state kind, not a series); smallest text 7.4 pt.
- Embedding: PASS. After the "Two edges carry most of the desk's risk" paragraph, which ends with the pointer sentence.
- Fixes: none needed.

## Figure 12-B.2, ch12b_chapter11_clocks.png (§12B.5)
- Correctness: FIXED. Periods verified against the chapter's clock table and the rules (Rule 6003 21 d; Rule 1007(c) 14 d; Rule 4001(c) at least 14 d; Rule 2003(a) days 21-40; §1121(b) 120 d / 18 mo; §1121(c)(3) 180 d / 20 mo; §365(d)(4) 120 + 90 d; §502(b)(9) 180 d; §546(a) 2 years; §547(b)(4) 90 d / 1 yr insiders; §503(b)(9) 20 d). Problem: the §546(a) clock is a fixed 730 days but was drawn as an open-ended arrow stopping at about day 690, so the bar ended before its own label. Now a solid bar to exactly day 730 (axis widened to 760); only the automatic stay keeps the open-ended arrow.
- Labels: "Real-property leases" changed to "Nonresidential leases" in the figure, since §365(d)(4) covers only nonresidential real property. (The chapter's clock table still says "Real-property leases"; left unchanged, flagged for the chapter editor.)
- Honesty: PASS. Source list matches the rows; caption states the challenge period is a typical DIP-order term drawn from the petition. "Four clocks run out within six weeks" matches the image (Rule 6003, 1007(c), 4001(c), §341).
- Legibility and style: FIXED. (a) The bar colours (blue, orange, violet) carried grouping with no key; added a figure-level key above the axes (first days: court-set procedure; bargaining windows; claims and estate value). (b) The "light" weight was keyed as "court may extend, to the cap" but is also used for the insiders' one-year look-back; key now reads "longer period: cap, or insiders". (c) The "180 d; cap 20 months" label ran to the right edge of the canvas; exclusivity labels now sit inside the light extension bar. No collisions after the change.
- Embedding: PASS. After the effective-date paragraph that holds the pointer sentence, before the clock table heading.

## Figure 12-B.3, ch12b_waterfall_call_spreads.png (§12B.6)
- Correctness: PASS. Left: stacked cumulative payments with kinks at K = 100, 400, 800, 1,000; bands sum to V (old equity is the residual above 1,000); V = 450 correctly sits in Class 3's band. Right: delta = pi/C x 1e4 recomputed by hand under lognormal(median 450, sigma 0.40): pi = 0.00, 0.38, 0.54, 0.05; deltas 0.0, 12.8, 13.5, 2.6 points per +100mm. Matches the chapter's pi_j / C_j.
- Honesty: PASS. Caption says Illustrative and states claims, V distribution and formula.
- Legibility and style: PASS. Two panels, one y-axis each; slots 2-3 (green, yellow) are direct-labelled on the left panel and by tick labels on the right; ink text; no collisions.
- Embedding: PASS. After the fulcrum-delta paragraph, which ends with the pointer sentence.
- Fixes: none needed.

## Figure 12-B.4, ch12b_plan_value_transfer.png (§12B.6)
- Correctness: PASS. R1 = V/Vplan and R2 = (Vplan - C1)V/(C2 Vplan) match the chapter; at Vplan = V = 1,000 senior 100% and junior 33.3%; both reach 71.4% at 1,400; monotone (senior falling, junior rising) as the chapter's derivatives require.
- Honesty: FIXED. For Vplan below 1,000 the senior curve exceeds 100% (125% at 800), which the chapter says a plan may not provide on purpose, but the caption said the senior is "made whole only when" Vplan = V. Caption now says the senior receives exactly its claim only at Vplan = V, is paid in shares worth less than its claim above it, and would be overpaid below it (not providable on purpose). Illustrative label and parameters were already correct.
- Legibility and style: FIXED. The "Senior" and "Junior" labels floated far from their curves (dots off the lines). Each label now has its dot on its own curve with the text beside it. Ink text, two colours in fixed order (blue senior, orange junior), no collisions.
- Embedding: PASS. After the "high plan value is the senior class selling equity" paragraph, which ends with the pointer sentence.

## Figure 12-B.5, ch12b_halvorsen_waterfall.png (§12B.9)
- Correctness: PASS. Sources 250 + 960 + 90 = 1,300; destinations 150 + 760 + 300 + 75 + 15 = 1,300; flows reconcile to each node (ABL 150 + 100; term-loan collateral 660 + 300; unencumbered 75 + 15); first lien 100 + 660 = 760; ratios 760/1,250 = 60.8% and 15/1,020 = 1.5% match the chapter's five waterfall steps. No ribbon crossings.
- Honesty: PASS. Labelled Illustrative, fictional company, in millions.
- Legibility and style: PASS. Slots 3-5 (yellow, magenta, green) are direct-labelled at the destination bars; ink text; no clipping.
- Embedding: PASS. After the "plan delivers an exit ABL" paragraph, which ends with the pointer sentence.
- Fixes: none needed.

## Edits made
- tools/figures/ch12b.py: Figure 12-B.2 rewritten for the points above (730-day bar, inside labels, colour key, legend wording, label "Nonresidential leases", taller canvas); Figure 12-B.4 direct labels moved onto the curves. All five PNGs regenerated.
- book_src/12_ch12b_the_restructuring_process_as_a_state_machine.md: Figure 12-B.4 caption only.

## Open note for the chapter editor
- The clock table row "Real-property leases" (§365(d)(4)) should read "Nonresidential real-property leases".
<!-- STATUS: COMPLETE -->
