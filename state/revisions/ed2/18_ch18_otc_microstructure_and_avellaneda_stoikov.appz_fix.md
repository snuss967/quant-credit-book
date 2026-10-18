# Ch 18 App Z editor-note fixes

## Note 1: "Random jump sizes" (§18.6.1) tells the reader to replace $e^{\gamma qJ}$ with $M_J(\gamma q)$, which is wrong if applied literally to the factored bid term of (18.7)
- Recomputation (python3, scipy quad; s=91.25, gamma=0.005, q=3, lambda_P*tau=0.025, mean recovery 40, J_bar=51.25): bid jump term with J fixed = 3.150; Beta(40,60) difference form = 3.188 (cost 0.037); Beta(2,3) difference form M_J(g(q+1)) - M_J(gq) = 3.776 (cost 0.626, sd 20.0); literal swap M_J(gq)(M_J(g)-1) = 3.362; with e^{g J_bar} kept in the second factor = 3.290; short dealer (q=-3) bids 0.048 higher under Beta(2,3); small-gamma expansion gives 0.175 against the exact 0.63.
- Ruling: FIXED (note right). The replacement is exact inside theta(q); the factored form e^{gqJ}(e^{gJ}-1) holds only for fixed J, and the bid needs the difference of MGFs.
- Edit, book_src/18_ch18_otc_microstructure_and_avellaneda_stoikov.md, §18.6.1 "Random jump sizes":
  - OLD: "Replace $e^{\gamma qJ}$ with the moment generating function $M_J(\gamma q) = \mathbb{E}[e^{\gamma q J}]$, computed by quadrature. By Jensen's"
  - NEW: "In $\theta(q)$, replace $e^{\gamma qJ}$ with the moment generating function $M_J(\gamma q) = \mathbb{E}[e^{\gamma q J}]$, computed by quadrature, and take the difference as before: the bid's jump term is $\frac{\lambda^{\mathbb{P}}\tau}{\gamma}\big[M_J(\gamma(q+1)) - M_J(\gamma q)\big]$, not the factored $e^{\gamma qJ}(e^{\gamma J}-1)$ of (18.7), which holds only for a fixed $J$. By Jensen's"
- App Z: Z.18.2 already used the difference form and the values 3.15 / 3.19 / 3.78 / 3.36 / 0.04 / 0.63 / 0.05 / 0.175, all confirmed; no text change. NOTE paragraph deleted.

## Note 2: Ines's line in §18.9.1 ("a fat $e_n$-sized discount from each of them") with three desks
- Recomputation (python3, scipy quad, plus a numeric best-response check of the equilibrium b_n(x) = x - sigma(a_n + 1/h_n)): e_3 = 0.846, e_30 = 2.043 (e_n GROWS with n, as the Math, Gently box and §18.9 say). Equilibrium discount to own read: 1.507 sigma at n=3, 2.163 sigma at n=30. Seller's expected shortfall from value, sigma(a_n + 1/h_n - e_n): 0.661 sigma at n=3, 0.262 at n=8, 0.120 at n=30 (Monte Carlo agrees: 0.662 and 0.120). Best-response check: optimal bid for a signal of 0 is -1.5074 (n=3) and -1.6855 (n=8), matching -(a_n + 1/h_n).
- Ruling: FIXED (note right). With three desks the e_n piece is smaller than with thirty; what is fatter is the winner's strategic shade, i.e. the seller's shortfall. Only the winner pays a discount, so "from each of them" was also off.
- Edit, book_src/18_ch18_otc_microstructure_and_avellaneda_stoikov.md, §18.9.1 (Ines at the whiteboard, after the 0.405):
  - OLD: "three envelopes and a fat $e_n$-sized discount from each of them."
  - NEW: "three envelopes and a fat discount from the winner."
- App Z: Z.18.4 numbers (0.50 vs 0.20 shortfall at the 0.75-point-sigma example, 1.13 vs 1.26 own-read shading) are unaffected; no text change. NOTE paragraph deleted.

Summary: 2 notes handled, 2 fixed, 0 ruled wrong, 0 softened. No figure script or listing changed.
<!-- STATUS: COMPLETE -->
