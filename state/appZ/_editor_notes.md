# App Z editor notes (chapter-text discrepancies found while solving)

### 01_ch01b_a_week_in_five_quant_shops

NOTE (for the editor): §1B.4 and the Desk Debrief both say "a mark is a choice made inside the bid-ask spread," but the scene's composite is 77 bid, 78.50 offered, and Hal marks at 79. That is 0.50 above the offer and 1.25 above the 77.75 mid, so the mark is outside the spread, not inside it. The \$75,000 and the "about 70 bp of spread" (my check: 1.25 points on \$6mm is \$75,000, and \$75,000 / \$1,076 a bp is 69.7 bp) are right for a 79 mark; it is the sentence about the spread that fails. Either the composite's offer needs to be at least 79 or the senior trader's instruction needs to be at most 78.50.

### 02_ch02b_transaction_cost_analysis_for_credit

NOTE (for the editor): This exercise is titled "Ninety minutes on one leg," but the text says the long leg fills "45 minutes before the short," and the chapter's check (\$42,500 and \$28,100) uses 45. The 90 comes from the April PB-01 opening in §2B.7, where the pod was one-legged from 9:50 to 11:20. At 90 minutes the same inputs give \$60,048 unhedged and \$39,718 with the 0.75 bridge. The check values are right for 45 minutes; the title should say "Forty-five minutes" or the text should say 90.

### 02_ch02b_transaction_cost_analysis_for_credit

NOTE (for the editor): §2B.6 concludes that "nearly all of Mags's jump was the market getting smaller on paper," using an 8% cut: $18.6\% / 0.92 = 20.2\%$, which is 1.6 of the 1.7 points observed (95%). But 8% is the top of MarketAxess's "up to 8%" for June 2026, and FINRA's own baseline is up to 5.7% (in trades, not dollars). At 5.7%, 18.6% becomes 19.7%, only 1.1 points or 66% of the jump, and September's like-for-like reading is 19.1%, not 18.6%. "Inflated by up to 8%" can also mean reported volume was 1.08 times true, which is 7.4% removed and gives 20.1%. Consider "most of" in place of "nearly all," or say which reading of the 8% is used.


### 03_ch03b_your_first_year_on_the_desk

NOTE (for the editor): the dates here are a week away from the dates in §12B. The cold open of Chapter 12-B is Monday 23 November 2026 and says the coupon was missed "on Friday", which is 20 November, and §12B.9 puts day 28 on "the Friday before Christmas week", which is 18 December (20 November plus 28 days; the grace period would end on Sunday 20 December). This exercise, the Listing 3-B.1 test (`date(2026, 11, 13) + timedelta(days=28) == date(2026, 12, 11)  # day 28: RSA and petition (12B.9)`), Figure 3-B.4 and the Pair Book all use 13 November, 11 December and 13 December. The arithmetic is right in both chapters; they disagree by exactly seven days. Moving §3B's dates a week later (20 November, 18 December, 20 December, rolled to Monday 21 December) would reconcile them and would keep every weekday statement true (Friday, Friday, Sunday), though Figure 3-B.4 and the listing's tests would need a rerun. The exercise labels its date illustrative, but its heading and its check both tie day 28 to §12B.9, which places it elsewhere.

### 04_ch04d_getting_the_seat

NOTE (for the editor): §28.4 pairs the slope $-2.69$ with "a recovery is known to perhaps $\pm 15$ points, which moves it by about 32". Multiplying 2.69 by 0.15 gives 40, not 32. The 32 is the exact move to $L = 0.75$ ($0.969/0.75 - 0.969/0.6 = -0.323$), which is smaller because $f^*$ is convex in $L$. The 36 for PD, by contrast, is slope times change. One clause in §28.4 saying the recovery figure is the exact change would stop a careful reader from checking it against the slope. §4D.5's "takes it to 60%" is exact and fine.

### 13_ch13_codifying_lmt_game_theory

NOTE (for the editor): In §13.3.1's unblending table, the middle row ("first-lien second-out only") builds $K_1 = 934$ from June 2020 holdings ($992 \times 0.74$) but divides by the 2016 face of 1,950, giving 47.9. On the June 2020 face of 1,887, the one the remand court's ratable share uses, the row reads $934/1{,}887 = 49.5$, and the sentence below the table would say "between five and twelve points" rather than "between three and twelve." The other two rows check (44.8 and 57.0).

### 13_ch13_codifying_lmt_game_theory

NOTE (for the editor): The whiteboard's arithmetic puts the guarantee in OpCo's pool at its full \$1,266mm on top of the \$735mm collected upstairs, and "Ways This Blows Up" item (2) says the engine assumes full face against each obligor. Listing 13.1's pari-plus wiring does the opposite: `opco_guar` carries `reduce_by=["fsub_guar"]`, and §13.7 describes it as "double-dip OpCo for the deficiency." A reader who copies `dd_recoveries` gets OpCo 6.35% and Super HoldCo 68.3% at the whiteboard inputs, not 5.0% and 69%. With the note struck the gap is wider (14.0% against 8.8%). Suggest saying in the pari-plus paragraph, or in item (2), that the listing nets and the whiteboard does not.

### 14_ch14_default_and_recovery_cycle_lmt_era

NOTE (for the editor): §14.8.2 says Mitel, filing 29 months after its uptier, failed "inside the high-hazard window that the $k > 1$ calibration predicts." On the pooled clock of §14.3.2 ($p = 0.25$, $k = 1.2$, $\eta = 1.71$), 78% of eventual defaulters have already failed by 29 months, and the population hazard there is 0.051 a year, less than half its 0.115 peak. §14.8.1 calls Serta's 31 months, where the same figures are 80% and 0.046, "a late failure." Both cannot be right on one clock. Mitel fits only with a name-specific scale stretched by its roughly 2.5-year runway (§14.3.2's covariate story). For example, $\eta_i \approx 3.3$ makes 29 months the median susceptible failure time. Suggest "inside the window its own runway set, though late on the pooled clock."

### 14_ch14_default_and_recovery_cycle_lmt_era

NOTE (for the editor): The exercise never says who is inside when the co-op breaks, and the arithmetic of §14.5.1 points the other way. Three defectors hold 21% of the class, so the sponsor's 50.1% needs 29.1 of the 30 points held outside the co-op. If the sponsor fills that gap from outsiders at random, then, given a break, an outsider is inside with probability 0.92 at $\varphi = 0.10$ and 0.70 at $\varphi = 0.35$, and it is the loyal members who get primed. On that reading a seat is worth at most $0.738 \times (1 - 0.70) \times 49 \approx 11$ points, and that only if a member can always sell its vote; for a member who stays loyal, it is worth less than nothing. The 36-point answer needs one more sentence, such as "assume that a deal, if done, is done with co-op members and primes everyone outside the co-op" (the Lumen shape of §14.5, where the group was the deal). Alternatively, recast "you" as a co-op member deciding whether to defect.

### 27_ch27_system_architecture_and_asics

NOTE (for the editor): The exercise says "rerun block 3 with $c_s^2 = 1$." Block 3 (Listing 27.3) hard-codes the $c_s^2 = 4$ answers, so with `CS2 = 1.0` it stops at its first assert, `abs(ew - 233.33) < 0.01`, because the mean wait is now 93.3 ms; the p99-sojourn assert (1,000 to 2,400 ms) would fail as well, at about 610 ms. Suggest adding "and update the asserts," or readers will think they broke the listing.

### 27_ch27_system_architecture_and_asics

NOTE (for the editor): §27.7.2 says that to first order $\text{ARL}_1 \approx \ln(\text{ARL}_0)/\mathcal{K}$. As an asymptote that is right, but at the chapter's own example ($\delta = 1$, $c = 5$, $\text{ARL}_0 = 938$) it gives 13.7 fills against the 10.3 quoted in the same paragraph, and at this exercise's $\delta = 0.75$ it gives 29.7 against Siegmund's 21.6. The next-order form $\big(\ln(\mathcal{K}\,\text{ARL}_0) - 1\big)/\mathcal{K}$ gives 10.3 and 21.6. Suggest using it, or adding "overstates the delay by about a third at these settings."
