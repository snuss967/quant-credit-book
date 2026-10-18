# Figures log: Chapter 7 (ed2 U4)

Plan. Chapter already had one figure (Figure 7.1 in the first edition of this pass, the pair corridor of section 7.4, drawn by tools/figures/ch07_rv.py, data Illustrative). Five more chosen from section 3 of the brief (state/revisions/ed2/07_ch07_ml_on_small_sample_credit_data.brief.md), one per technique the chapter builds: fractional differentiation (7.3), the hat count (7.6), purged and embargoed folds (7.7), the noise maximum behind the deflated Sharpe ratio (7.8), and the reversal gap (7.9, the only figure with real data). Skipped on purpose: the brief's triple-barrier DTS path (the pair corridor already draws the barrier, the vertical wall and the dead zone in 7.4). Because the FFD figure sits in 7.3, ahead of the existing corridor, the corridor is renumbered from 7.1 to 7.2 (its caption and the one sentence that points to it, nothing else in either).

Final order of appearance: 7.1 ffd_weights (7.3), 7.2 pair_corridor (7.4, existing), 7.3 hat_count (7.6), 7.4 purged_folds (7.7), 7.5 dsr_noise_max (7.8), 7.6 reversal_gap (7.9).

All five new figures are drawn by tools/figures/ch07.py (python3 tools/figures/ch07.py; seeds fixed, np.random.default_rng(7) for the simulation dots). Colour roles follow ch07_rv.py and ch07b.py: orange = naive/textbook answer, blue = honest/corrected answer, neutral = reference. Each PNG was viewed and cleaned (log-axis tick labels, end-label collisions, clipped y-labels and an embargo caption crossing the axis fixed). All PNGs are under 140 KB.

## Embedded figures
