# RV weave log: Ch 5, Probability Distributions (Edition 2, user directive 13)

*RV weaver, 2026-10-18. Thread row: `05_ch05_credit_probability_distributions` = box + one line in §5.6; PB-01 (jumps, stressed), PB-05 (opened); tool = survive-or-jump mixture and the categorical default; truths T4 (owner) and T8 (foreshadow); home Ch 8-D §8D.4, Ch 14; RV figure = pair P&L histogram with two spikes.*

## Preconditions

- `state/rv_thread.md` present, ends COMPLETE. No prior `.rv.md`. `05_ch05...log.md` ends COMPLETE (no reviser mid-flight). Chapter not in `git status` as modified.

## What was written, and where

1. **§5.1.4, after the View From Another Seat (pod) box: one narration line + `> **The Pair.**` box (PB-01, ~580 words) + one narration line + Figure 5.1.** Dov reruns his April pair through §5.1.2's mixture. Legs: long \$60mm Kestrel 6% 2030 at 96 (350 bp, SD 3.6); short \$39mm Halvorsen 7.25% 2029 at 90 (600 bp, 3.4), borrowed via the prime broker (real short leg named; CDS alternative pointed to Ch 24). Hedge: market-value DTS (72,600 vs 71,600; 0.65 by face). Coins at R 40: −\$33.6mm / +\$19.5mm; odds spread/(1−R) = 5.8% / 10% (labelled $\mathbb{Q}$, §5.5.6). Removes: market and the expected jump cost (\$1.95mm vs \$1.96mm, net ≈ −\$10k/yr). Idio: Kestrel vs Halvorsen; thesis 100 bp/yr ≈ \$1.2mm inside a \$3.1mm wobble (30% relative spread vol, illustrative). Leaks: between-world variances add (jump s.d. \$9.8mm vs \$7.9mm for the long alone; coins ≈ 91% of variance; skew −3.8 → −1.4); one Kestrel default = 28 years of thesis and > the \$24mm to Dov's first line (§1B.2); Beta recovery smear \$17–50mm; ρ_D = 0.05 trims ≈ 5% (§5.7.4); CDX moves neither spike; only same-issuer structure cancels a coin (PB-02, §4C.3); third face on the short (§5.6.1). Costs: April carry ≈ flat (6% on \$60mm, 7.25% on \$39mm, ≈ \$0.6mm financing, 50 bp fee; reset to 300 bp per §1B.2); CDS short pays 60 vs bond short 50 on the default card; two half-spreads ≈ \$0.5mm. Cross-references to canonical home: **§8D.4** (two jump processes) and §8D.5 (sizing to the stop); Exercise 6.
2. **Figure 5.1** `assets/figures/ch05_pair_two_spikes.png`, script `tools/figures/ch05_rv.py` (kept apart from a future `ch05.py`). Two panels, log y: recovery fixed at 40 (hump + two spikes + 0.6% both-default bar) and Beta recovery (smears); dashed first line at −\$24mm; MC mean +\$1.05mm, P(< −\$24mm) 3.8% with Beta. Caption carries the fiction label. Ch 5 had no figures before; the later Ch 1–7 figures pass may renumber.
3. **§5.6.1, after the "When the third state earns its parameters" paragraph, before the Trend Watch: one paragraph (~230 words) opening PB-05 and foreshadowing T8.** The third face on the short side gaps *up* (the \$3.9mm line of 1-B; Ch 14 owns it). PB-05: Owen's pod, replay cut at the close Fri 2 Jun 2023; long Carvana 5.875% 2028s in the mid-50s, short common at 0.30 of bond MV, structural-model delta resized monthly; carry (5.875% on face; stock-borrow fee); H = court face + shared firm-value wobble; I = which face lands; L = the exchange face, both legs rise, short-stock loss uncapped. Outcome pointed to §5.6.2 (told once), Ch 6 (stress), Ch 14 (close).
4. **§5.6.2 Carvana paragraph:** the existing sentence "A bond-long, stock-short trade hedged at a structural-model ratio lost heavily…" now carries "which is PB-05's shape (§5.6.1)", so the outcome is told once and tied to the ledger.
5. **Exercises: new Exercise 6, "Two coins after the trim"** (Tuesday post-trim sizes \$60mm / \$35mm at 97 / 78; Checks: −\$34.2mm at 5.6%, +\$13.3mm at 23.3%; expected +\$1.19mm/yr; jump s.d. ≈ \$9.7mm; split +\$0.57mm (price/duration) / +\$0.62mm (excess DTS filled with CDX); (d) ROBO's "long default, at no cost" vs the short coupon and the 300 bp fee). Box uses April numbers so it does not solve the exercise (u2 lesson 7).

## Retired (one telling per fact)

- **View From Another Seat (pod), §5.1.4:** the clause "they hedge jump-to-default explicitly, usually with single-name or index CDS, so that the strategy's monthly Sharpe is measured on a book whose default world is small" replaced by "they run the book as pairs, a short against every long, so that the monthly Sharpe is earned on a residual rather than on carry". The Pair box now tells what a short leg does to the default world, and the old clause wrongly implied index CDS hedges single-name JTD. Nothing protected removed (no equation, Source Extraction, Trend Watch, exercise, figure, App F link or URL touched).

## Decisions and open items

- **PB-01 numbers, not PAIRS §5.4's.** The thread's L column quotes PAIRS §5.4 (−\$5.79m / +\$8.88m, a generic \$10m/\$15m pair). Rule 9 fixes PB-01's legs, and the 8-D brief puts the PAIRS numbers in §8D.4, so Ch 5 uses PB-01's own April numbers and points to §8D.4. Same truth (T4), no duplicate telling.
- **Cast.** Ch 1-B in print names Dov's analyst Bea Castellanos and his risk manager Gordon Pike; the thread and the 8-D brief use Wen Zhao and Marcus Oyelaran. Ch 5 names neither; flag for the 1-B / 8-D weavers. Allocation kept at 1-B's \$400mm (thread mandate says \$250mm).
- **JTD limit conflict (flagged in the ledger).** PB-01's Kestrel JTD is \$33.6mm at R 40, far above the ledger's book-level "\$5mm" JTD line and the thread mandate's 2%-of-capital cap. The chapter states no limit number; 8-B / 8-D should reconcile with the 1-B sizes.
- **Probabilities** are spread-implied ($\mathbb{Q}$) and labelled so in the box, consistent with §5.5.6.
- **Cast bible** updated: Dov (Ch 5 §5.1.4 box, Ex 6) and Owen (Ch 5 §5.6.1, PB-05 booked to his pod).
- **Ledger** `state/rv_pair_book.md`: PB-01 → stressed (Ch 5), What leaked extended; PB-05 → open (Ch 5), legs, ratio 0.30 of bond MV, leak.
- `tools/check_book.py --file` passes (35,491 words). Pandoc renders the box's inline math correctly. Chapter's last line remains `<!-- STATUS: COMPLETE -->`.

<!-- STATUS: COMPLETE -->
