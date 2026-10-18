# Ch 6 App Z editor-note fixes (numbers editor)

Three NOTE (for the editor) paragraphs found in state/appZ/06_ch06_merton_and_intensity_models.md. All three deleted from the solutions file after ruling.

## 1. Warm-up A (b): the two-state inputs do not fit the price levels
- Note: gap arithmetic gives p = 70.6%, but with p = 12/17 the implied liquidation value L is about 1.8 cents, which contradicts the 53% no-cash coverage and the March trading levels.
- Recomputation (python3): p = 12/17 = 0.7059; L = (69 - 0.7059*97)/0.2941 = 1.80 from the 2025s and (57 - 0.7059*80)/0.2941 = 1.80 from the 2031s. At L = 40 the levels imply p = 50.9% (2025s) and 42.5% (2031s). Book recovery 4,222/3,675 = 114.9% and 2,000/3,675 = 53.4% (unchanged). Reinstatement values rechecked at a 5% yield from 25 Apr 2023: 97.50 and 79.60 (unchanged).
- Ruling: note right (fixed, smallest edit: say the model is a gap-reader, not a level-fit; the 97/80 values are fair and the 70% check stands).
- Chapter (Exercises, Warm-up A (b)): "while a liquidation pays both the same. What probability of reinstatement does a twelve-point gap imply?" -> "while a liquidation pays both the same. Use only the gap: the two-state model is not meant to fit the two price levels. What probability of reinstatement does a twelve-point gap imply?"
- Solution (Z.06.A, How): added after "...without your knowing the recovery." the sentence "Use only the gap. Put $p=0.706$ back into either price and the implied $L$ is under 2 cents, far below the 53% no-cash coverage, so the two-state model reads a probability from the spread but is not meant to fit the two price levels." NOTE deleted.

## 2. Exercise 4: "zero drift" vs black_cox_pd mu
- Note: with mu=0, black_cox_pd returns 73.6%, not the checked 70%; 70.3% needs mu = 0.5*sigma_V^2 = 0.03125 (zero log drift).
- Recomputation (Listing 6.4 copied to /tmp, V0=880, K=800, g=0, sigma=0.25, T=1): mu=0 -> 0.73586; mu=0.03125 -> 0.70302 = 2N(-ln(1.1)/0.25) = 2*0.35151. Matches the note.
- Ruling: note right (fixed). Chapter's §6.5.3 ("roughly zero drift ... 2N(-0.38)") left alone; the check "matching §6.5.3" now agrees with the exercise.
- Chapter (Exercises, item 4): "With zero drift, compute the one-year probability of a covenant breach with `black_cox_pd`." -> "With zero log drift ($\mu=\tfrac12\sigma_V^2$ in `black_cox_pd`), compute the one-year probability of a covenant breach with `black_cox_pd`."
- Solution (Z.06.4, Answer): "With zero *log* drift, the one-year breach probability" -> "With zero log drift ($\mu=\tfrac12\sigma_V^2$ in `black_cox_pd`), the one-year breach probability"; "you get 73.6% instead; see the NOTE." -> "you get 73.6% instead." NOTE deleted.

## 3. Exercise 6 / §6.10.2: Theo's "They lost money on a stock that survived bankruptcy"
- Note: computation agrees (13.75% vs 13.8%); but the $1.53 is only the cash component, and reported valuations of the whole package (about $7-8 per old share, Business Insider and Bloomberg URLs) would put a $5.50 buyer ahead before time value. Not verified against filings.
- Recomputation: E0/F = N(0.2833) - e^-0.04 N(-0.0167) = 0.6115 - 0.9608*0.4934 = 13.75% (check holds, no change). The $7-8 package value cannot be verified from files in state/research/ (the two URLs are not in any dossier; the Business Insider and Bloomberg pieces are not sourced there). Repo facts that are sourced (Ch 16 from the 8-K and Third Circuit footnote: $1.53 cash, 3% of new common, 89.05mm warrants at $13.80, plan value of warrants $769mm) show the package was worth more than the cash alone, so "lost money" is unsupported as a flat statement.
- Ruling: softened (no new number introduced; $7-8 not added).
- Chapter (§6.10.2, Theo's last line): "He stops. "They lost money on a stock that survived bankruptcy."" -> "He stops. "Whether that lost money depends on what the warrants and the new shares were worth, and the cash alone was only \$1.53. The stock survived bankruptcy. The price was still the question.""
- Solution (Z.06.6): text did not quote the "lost money" line; its three reasons (value is not price, who sold, outcome is not decision) still hold. NOTE deleted, no other edit.
- Open for a later pass: if the filings are checked, Mags's and Ines's lines could carry the plan's per-share valuation; Ch 16 §16.6 already cites about $8 (Bloomberg News, 13 May 2021).

<!-- STATUS: COMPLETE -->
