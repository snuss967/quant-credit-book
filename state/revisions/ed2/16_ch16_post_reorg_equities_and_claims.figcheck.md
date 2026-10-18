# Figure check: Chapter 16 (ed2)

Checked against tools/figures/style.py (house style), tools/figures/ch16.py, the chapter derivations in §16.2.2, §16.3.2, §16.3.4, §16.5.3, §16.6 and §16.8.1, and each PNG viewed after the final re-run. All five PNGs are under 500 KB; embeds are numbered 16.1 to 16.5 in order, files exist, syntax is `![Figure 16.N: ...](assets/figures/ch16_*.png)`, and each image sits directly after the paragraph that points to it.

## Figure 16.1, ch16_overhang_delivery_lag.png (section 16.2.2)

- Correctness: OK. Instant release is -A exp(-theta s); staggered path is the chapter's two-compartment solution. Recomputed: trough -6.61% at s* = ln(theta/alpha)/(theta-alpha) = 0.2412 y (2.89 months); -4.41% at 1 month, -1.25% at 12 months (match the Poker Table's -4.4%, -6.6%, -1.2%); half-life ln 2 / 3.4 = 2.45 months; instant path at half-life = -7.5%. 200 trading days = 9.5 months, consistent with the §16.1.2 "about four half-lives" remark.
- Honesty: OK. Caption says Illustrative and names the model and parameters.
- Legibility/style: FIXED. The 200-day dashed line ran through the legend text ("on", "mean"). Legend now has an opaque white background, so the line stops behind it. One y-axis, BLUE/ORANGE in fixed order, text in ink.
- Embedding: OK.
- Verdict: pass after fix.

## Figure 16.2, ch16_backstop_put_and_fee.png (section 16.3.2)

- Correctness: OK. Left: rights = f (x-K)+ with f = m/(n0+m) = 163.5/454.75 = 0.36, backstop = -f (K-x)+ per plan share, kinks at K = 0.75. Right: fair fee = 0.64 * BS put (zero rate, sigma 70%) / K; recomputed table 8.89/12.51, 2.96/6.26, 0.28/1.61, identical to the chapter table (8.9/12.5, 3.0/6.3, 0.3/1.6). Hertz fee 10% and share counts match §16.3.4.
- Honesty: OK. Illustrative; 6% Seth and 10% Hertz 8-K/A are cited. Caption extended (small edit) to state the left-panel parameters K = 0.75 and m/(n0+m) = 0.36, which were not stated anywhere.
- Legibility/style: FIXED. The orange T = 0.25 curve ran through the legend text. Legend removed; the two curves are now direct-labelled with short leaders, "T = commitment-to-funding window" added to the in-panel note, and the note moved clear of the 10% reference label. Reference-line labels raised from 7.5 pt to 8 pt. No twinx; two panels.
- Embedding: OK.
- Verdict: pass after fixes.

## Figure 16.3, ch16_claim_recovery_pool_risk.png (section 16.5.3)

- Correctness: OK. E[R] = Phi(a) + (V/m) e^{s^2} Phi(-a-s), a = (ln(V/m) + s^2/2)/s, as in the chapter. Recomputed 0.9167 at V/m = 1, s = 0.30 and 0.3282 at V/m = 0.30; s = 0.60 gives 0.882 and 0.416, so "a wider pool widens both effects" holds. Curves are monotone increasing in V/m and tend to 1; the dashed benchmark is min(1, V/m) with its kink at 1.
- Honesty: OK. Caption says Illustrative and cites the closed form.
- Legibility/style: OK. No collisions; legend clear of data; only slots 0 and 1 plus neutral.
- Embedding: OK.
- Verdict: pass, no changes.

## Figure 16.4, ch16_hertz_timeline.png (section 16.6)

- Correctness: OK. Event dates match the Docket Diary (22 May 2020, 12 Jun 2020, 11 May 2021, 10/15/30 Jun 2021, 8 Nov 2021, 10 Sep 2024, Jun 2026 approx., 16 Oct 2026). Price points ($10.00, $29.00, about $3) and the $13.80 strike with 30 Jun 2051 expiry all appear in the chapter; $29 > $13.80 > $3 supports the caption's in/out-of-the-money statement.
- Honesty: OK. Caption lists sources (Hertz 8-K/A, 8-K, press release, Third Circuit No. 23-1169, press reports) and flags the June 2026 date and price as approximate; the panel states that no price path is implied.
- Legibility/style: FIXED (minor). Label text was 7.5 pt; raised to 8 pt, and the 11 May 2021 label re-wrapped to five shorter lines so it stays inside the canvas. Event text in ink, single blue series, no overlaps.
- Embedding: OK. Dollar signs are escaped in the caption.
- Verdict: pass after fix.

## Figure 16.5, ch16_post_reorg_return_distribution.png (section 16.8.1)

- Correctness: OK. R = (1-J)(e^X - 1) - J with s = sqrt(2 ln 1.4), p_J = 5%. Simulated single-name mean +33.3% and median -5.0% (analytic median -5.3%); 20-name book mean +32.9%, median +29.1%, P(book < 0) = 12.0%; P(single > +300%) = 4.3%, as printed on the panel. The jump spike lands in the first bin, and the cut at +300% is stated on the axis label.
- Honesty: OK. Illustrative, seed stated. Caption extended (small edit) to say the right panel groups the 400,000 draws into 20,000 books of 20 names.
- Legibility/style: FIXED. In the left panel the one-line "median -5%" label hung past the y-axis and the jump leader line cut through it. Mean and median labels are now two-line, sit directly above the line tops in both panels, and the jump annotation has been moved up so its leader clears everything. Y-limits raised to make room.
- Embedding: OK.
- Verdict: pass after fixes.

## Fixes made

- tools/figures/ch16.py: legend background (16.1); legend replaced by direct labels, note moved, 8 pt reference labels (16.2); 8 pt text and re-wrapped label (16.4); two-line mean/median labels and relocated jump annotation (16.5). Script re-run; all five PNGs regenerated and re-viewed.
- book_src chapter: two caption edits only (Figure 16.2 left-panel parameters; Figure 16.5 book grouping).
- Not changed, noted: in Figure 16.2 BLUE and ORANGE mean call/put in the left panel and T = 0.50/0.25 in the right panel; each is directly labelled, so left as is.
<!-- STATUS: COMPLETE -->
