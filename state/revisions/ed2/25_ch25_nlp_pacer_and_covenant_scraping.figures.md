# Figures log: Chapter 25 (ed2 U4)

Plan (no brief file and no figure dossier existed for Ch 25; figures chosen from the chapter text; the chapter had no figures). Data are either sourced facts quoted in the chapter or an Illustrative stated model.
1. ch25_definition_graph (25.2.3): the definition graph of Listing 25.1 with its two loops and a blast radius.
2. ch25_addback_capacity (25.3.4): "after giving effect" cap and Halyard capacity vs covenant EBITDA.
3. ch25_jcrew_mincut (25.4.2): the J.Crew trapdoor as a minimum cut, two readings.
4. ch25_token_vs_capacity (25.5.1): token-diff cosine change vs capacity-vector change.
5. ch25_docket_state_machine (25.7.2): docket state chain with the Hughes path.

All five drawn by tools/figures/ch25.py (matplotlib patches and arrows, house style), each PNG viewed and cleaned (label collisions, clipped y-label, hidden return arc, overlapping docket cards all fixed). Sizes 109 to 133 KB.

## Embedded figures

- **Figure 25.1, ch25_definition_graph.png** (§25.2.3, after the "Cycles are real; condense them" paragraph): the 16 terms of the synthetic Section 1.01 as a directed graph (arrow = definition of tail uses head), with the two strongly connected components outlined (Consolidated EBITDA / Run-Rate Cost Savings / Pro Forma Basis; Restricted / Unrestricted Subsidiary / Material Intellectual Property) and the blast radius of Consolidated EBITDA shaded (beta = 3); Excluded Taxes beta = 0. Data: Illustrative, edges from the Listing 25.1 matcher on the book's synthetic agreement text; the script asserts the SCCs and blast radii. NOTE for cleanup queue: Listing 25.1 as printed finds only one loop (regex `means\s+` skips "Pro Forma Basis ... means,"); the figure uses the edges the listing returns once that regex accepts `means[,\s]`, which matches the chapter prose ("two loops").
- **Figure 25.2, ch25_addback_capacity.png** (§25.3.4, after "each dollar of add-back buys 4.85"): left, add-back allowed as % of pre-add-back EBITDA under the "before" (c) and "after" (c/(1-c)) readings of a cap c, with 25% to 33.3% marked and the c^2/(1-c) gap shaded; right, K(E) = max(0, 4.5E - 900) + max(75, 0.35E) with the $75mm and $393.3mm points (E = $200mm and $266.7mm). Data: Illustrative, the Halyard terms of §25.3.4 (script asserts 75.0 and 393.333).
- **Figure 25.3, ch25_jcrew_mincut.png** (§25.4.2, after the "trapdoor did not create new capacity" paragraph): three-node graph (Loan parties, non-guarantor restricted subs, unrestricted subs), $150mm and $100mm parallel baskets and the trapdoor; top panel trapdoor = 0 (cut on the trapdoor, Phi = 0), bottom panel trapdoor = infinity (cut on the two baskets, Phi = $250mm, flow drawn thick). Data: basket sizes and $250mm IP interest as disclosed by J.Crew and summarized by Torys (May 2019) and King & Spalding, as quoted in §25.4.2; flow and cut computed with the Listing 25.3 Edmonds-Karp routine (script asserts Phi and the cut arcs).
- **Figure 25.4, ch25_token_vs_capacity.png** (§25.5.1, after the "one part in two million" paragraph): left, 1 - cos = k^2/||x||^2 against the number k of amended occurrences (log-log), with k = 1 at 4.2e-7 and the 1% line crossed at k = 155; right, ratio-basket capacity vs permitted multiple m, 4.50x ($300mm) to 5.25x ($500mm), +$200mm. Data: Illustrative, the §25.5.1 count-vector model (n = 150,000, d = 10,000, E||x||^2 = d(lambda^2 + lambda) = 2.4e6, Exercise 4) and Halyard's E = $266.7mm with $900mm first-lien net debt.
- **Figure 25.5, ch25_docket_state_machine.png** (§25.7.2, after the MLE paragraph, before the Docket Diary): chain Quiet, Organized, Contested, Standstill, Plan, Confirmed with the entry types that trigger each step, and the Hughes path in blue with its three docket entries (Docs. 154, 320, 369) and dwell times of 31 and 10 days; the q-hat = N/T estimator noted. Data: sourced, Hughes Satellite Systems Corp., Bankr. S.D. Tex. No. 26-90739, entry dates and titles exactly as quoted in the Docket Diary of §25.7.2.

Chapter edits: five embeds, each with one short pointer sentence appended to the illustrated paragraph; nothing else changed.
<!-- STATUS: COMPLETE -->
