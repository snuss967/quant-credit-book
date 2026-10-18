## Z.8-D Chapter 8-D: The Pair Book: Long One Credit, Short Another

Seven solutions: the chapter's one try-first prompt (the card at 7:30, in the Cold Open, which comes first in the chapter's own order and so is Z.8-D.1) and the six numbered Exercises 1 to 6 at the end of the chapter (Z.8-D.2 to Z.8-D.7). The exercises carry topical tags (*ruler*, *jump*, *stop*, *menu*, *explain*, *replication*), not [Read]/[Derive]/[Build]; only Exercise 6 is a build, and it extends Listing 8-D.1 (`ratio` and `pnl`, Appendix F). The "replication you can run" in §8D.3 is the real-data twin of Exercise 6 and is folded into Z.8-D.7, since it needs vendor CDX and lending data. I did not copy the printed checks: I recomputed every number in Python and ran Listing 8-D.1, whose asserts all pass. The printed checks are right. The seven NOTEs below are about units, a pointer, a transaction-cost mismatch, a rounding, and how the chapter describes Ben Dor's adjusted beta. Only Z.8-D.3 is in the risk-neutral measure (its intensities come from spreads); everything else is scenario arithmetic, realised P&L bookkeeping or a physical-measure simulation. Money is in \$mm of market value unless I say face; spreads are in basis points a year.

**Z.8-D.1: The card at 7:30**

**Answer:** Size first: the largest Ford Credit long the stop allows is \$22.5 million of market value (\$22.45mm, about \$23.6mm face), not the \$40 million on the book. Ratio: DTS, 1.50 on the bonds (\$33.75mm of GM Financial notes against \$22.5mm of Ford Credit) and about 1.64 on a five-year GM contract (\$36.8mm of protection), with the rating-bucket exposure written on the ledger as open, not hedged. Short leg: GM five-year CDS, once someone has answered which entity the contract references; the borrowed bond is the bridge until the protection is filled. Not "cut", and not "do nothing".

**How:** The book is \$11mm under its high-water mark and the first line (capital halved) is \$24mm under it, so the loss budget is the *distance*, \$13mm. One Ford Credit default at 95 with recovery 40 costs a fraction $(95-40)/95 = 57.9\%$ of market value:

$$
N^{\text{stop}}_{\max} = \frac{24 - 11}{(95-40)/95} = \frac{13}{0.579} = \$22.45\text{mm}.
$$

The borrow is a second cap: 20% of the lender's \$300mm, less the \$20mm Wen expects back, over the ratio, $(0.20\times 300 - 20)/1.50 = \$26.7$mm. The smaller binds, so the stop does (`max_long` returns `binds: stop`). For the ratio, the rulers read 1.00 (DV01), 1.50 (DTS), 2.14 (a noisy 24-week beta) and 1.65 (the platform's factor model); DTS is the prior, and 1.65 would hedge away the rating-bucket toll that *is* the thesis, so the 0.05 of gross stays open and written down. For the leg, bonds cost $120 + 70 = 190$ bp (\$1.14mm a year on \$60mm), CDS 110 bp (\$0.66mm); at \$22.5mm of long the DTS-equivalent protection is $22.5 \times 180/110 = \$36.8$mm. The saving is bought with an ISDA, an auction and a basis, so the first line on the ledger is the reference-entity question. Cutting gives up an intact thesis for two spreads. The stop is a physical-world rule about dollars lost; the CDS levels are risk-neutral prices.

**The trap:** Sizing to the line instead of the distance. $24/0.579 = \$41.5$mm, which blesses the \$40mm pair and ignores the \$11mm already spent; the budget is what is left. The close second is choosing the leg first and the size afterwards, which is how a pair gets opened at \$40 million.

**If you got this wrong, read:** §8D.5 ("Sizing to the Stop") first, then §8D.3 ("Three Rulers, One Alpha") and §8D.2 ("The Short-Leg Menu"); §1B.2 for where the \$24mm line comes from.

NOTE (for the editor): The Cold Open gives the lender's inventory as \$300 million *face* and the short as \$60 million market value (about \$61 million face), but §8D.5 says the 20% cap "on \$300 million is \$60 million, exactly the current short", and Listing 8-D.1 documents `inventory` as "lendable market value, \$mm". In one unit the two do not match. In face the cap is \$60.0mm against a current short of \$61.2mm face, so the pod is already \$1.2mm over; in market value the cap is \$58.8mm against \$60.0mm. The borrow-based size is then \$26.1mm rather than \$26.7mm. The stop still binds at \$22.5mm, so nothing downstream moves. Suggest stating the unit once and saying "about the current short".

NOTE (for the editor): §8D.4 calls a \$23.2 million loss "5.8% of capital" that is "past the first of the two lines" (5% and 7.5%). Dov's own first line is \$24 million (§1B.2), which is 6.0% of \$400 million, not 5% (\$20 million). From a flat book \$23.2mm leaves \$0.8mm of room under \$24mm; it breaches only because the book is already \$11mm down (the distance is \$13mm). Either say "past the 5% line of the press-reported template" or give Vantress a \$20mm first line.

**Z.8-D.2: Three rulers on someone else's pair**

**Answer:** Short \$36.5mm under DV01, \$26.7mm under DTS, \$21.9mm under beta. On a 10% relative widening (A +38 bp, B +52 bp) the \$40mm long loses \$0.638mm and the three shorts make \$0.874mm, \$0.638mm and \$0.524mm, so the pair nets +\$0.235mm (DV01: net short the market), \$0 (DTS) and −\$0.114mm (beta). The beta ruler leaves the pair long the market.

**How:** The hedge ratios per dollar of long are

$$
h_{\text{DV01}} = \frac{4.2}{4.6} = 0.913,\qquad h_{\text{DTS}} = \frac{4.2 \times 380}{4.6 \times 520} = 0.667,\qquad h_\beta = 0.60 \times \frac{4.2}{4.6} = 0.548 ,
$$

and multiplying by \$40mm gives the three shorts. The long loses $4.2 \times 0.0038 \times 40 = \$0.638$mm; a short of size $S$ gains $S \times 4.6 \times 0.0052$. DTS matches the long's loss by construction, so the other two are read off their size: a short bigger than \$26.7mm is net short the market, a smaller one is net long. A quick diagnostic: the DTS-consistent bp-beta of A on B is $s_A/s_B = 380/520 = 0.73$, so the trailing 0.60 is 18% too low, the short is 18% too small, and the unhedged remainder is 18% of the long's \$0.638mm, which is the \$0.114mm. Everything here is empirical (physical measure) hedging; units are \$mm, bp and years.

**The trap:** "DV01 is the one that leaves you long the market." That is PB-19's lesson (−\$108,000 under DV01, +\$138,000 under beta in §8D.3), and it holds only when the long is the *wider* name. Here the long is the tighter one (380 against 520), so DV01 over-hedges and the order flips. The other slip is to treat beta as the neutral ruler because it is estimated from market data; its sign is whatever the last 24 weeks happened to say.

**If you got this wrong, read:** §8D.3 ("Three Rulers, One Alpha"); §8.4 ("DTS-neutral pairs, and why they carry nothing"); §4B.3 for spread duration.

NOTE (for the editor): The §8D.3 scenario table (\$85.6mm; +138, +205 and +385 in \$000) is built on the rounded ratio 2.14. At the unrounded 2.142857 that Listing 8-D.1's `scenarios` and self-check use, the same cells read \$85.7mm, +139, +206 and +386. The listing's own assert (0.2057 at `atol=1e-3`) passes either way. One clause ("at a ratio rounded to 2.14") would stop a reader who reproduces the table from missing by \$1,000.

**Z.8-D.3: The two spikes**

**Answer:** If L defaults the pair loses \$5.79mm; if S defaults it gains \$8.88mm; the expected jump P&L under $\mathbb{Q}$ is about +\$3,900 a year (\$3,867 unrounded). If both default, the pair makes +\$3.09mm.

**How:** Convert market value to face, then take price minus recovery per unit of face. For L, face $= 10/0.95 = 10.53$ and the loss is $10.53 \times (0.95 - 0.40) = 10 \times 55/95 = \$5.79$mm. For S, face $= 15/0.98 = 15.31$ and the gain is $15 \times 58/98 = \$8.88$mm. The risk-neutral intensities come from the credit triangle (§6.8), $\lambda = s/(1-R)$: $\lambda_L = 0.018/0.60 = 3.0\%$ and $\lambda_S = 0.012/0.60 = 2.0\%$ a year. Then

$$
\mathbb{E}^{\mathbb{Q}}[J] = 0.02 \times 8.878 - 0.03 \times 5.789 = 0.1776 - 0.1737 = +\$0.0039\text{mm a year}.
$$

The mean is near zero because the ratio is the DTS-neutral 1.5 (spread times duration tracks the loss rate), but the shape is two spikes: about 2.9% a year of −\$5.79mm (L alone), about 1.9% of +\$8.88mm (S alone), and nothing the rest of the time. The 30 bp thesis on \$10mm is $4.5 \times 0.0030 \times 10 = \$135{,}000$ a year, so one default on L erases $5.789/0.135 = 42.9 \approx 43$ years of it. The intensities are $\mathbb{Q}$ quantities, risk premium included. If physical default rates are a common fraction $1/k$ of them, the mean falls to \$3,900$/k$; the spikes keep their size.

**The trap:** Stopping at the mean. "+\$3,900, so the pair is jump-neutral and hedged" mistakes the average for the distribution; the stop does not see the mean, it sees −\$5.79mm on an afternoon. A numerical version of the same slip is to use $1-R = 0.6$ on market value (loss \$6.0mm, gain \$9.0mm), which makes the mean exactly zero and hides the price effect that produces the \$3,900.

**If you got this wrong, read:** §8D.4 ("Two Jump Processes"); §5.1 (the survive-or-jump mixture); §6.8 (the credit triangle).

**Z.8-D.4: The training sheet**

**Answer:** \$25.9mm of face (about \$25.3mm of market value) for the 7.5% line; \$8.6mm of face (\$8.4mm of market value) if one default may cost only 2.5%. The capital-structure pair on the same sheet needs \$11.2mm of face of second-lien short against \$20mm of first lien.

**How:** On \$200mm of capital the 7.5% line is \$15mm and 2.5% is \$5mm. A bond bought at 98 with recovery 40 loses $98 - 40 = 58$ points per 100 of face on default, so

$$
N_{\max} = \frac{B}{0.58}:\qquad \frac{15}{0.58} = \$25.9\text{mm},\qquad \frac{5}{0.58} = \$8.6\text{mm}.
$$

These are face amounts, because the loss is per unit of face; Dov's own sheet in §8D.5 uses market value, which is the same arithmetic times the price (here $\times 0.98$). For the pair: \$20mm of first lien at 98 with recovery 70 loses $20 \times 0.28 = \$5.6$mm. A second lien at 70 with recovery 20 gains 50 points per unit of face shorted, so $N \times 0.50 = 5.6$ gives $N = \$11.2$mm of face (\$7.84mm of market value). This is scenario arithmetic, so no measure is needed.

**The trap:** Two slips. First, sizing off par instead of price: $15/0.60 = \$25.0$mm. You paid 98, so you lose 98 − 40, not 100 − 40. Second, and the one that matters, calling the capital-structure pair "hedged" and exempting it from the stop. It is flat only at the assumed recoveries. If the first lien recovers 60 instead of 70, the default costs \$2.0mm; if the second lien recovers 30 instead of 20, it costs \$1.1mm; if the recoveries are 80 and 10 the pair makes \$3.1mm. Jump-neutral by sizing means sized on a recovery guess.

**If you got this wrong, read:** §8D.5 ("Sizing to the Stop"); §4C.3 (Owen's Halvorsen capital-structure pair); §28.6 (the two-threshold stop).

**Z.8-D.5: Cash or CDS**

**Answer:** The cash short costs \$232,500 a year (155 bp on \$15mm); the CDS short costs \$165,000 (110 bp on \$15mm). The difference is \$67,500 a year. At a 100 bp cash rate the 35 bp fee is a 65 bp rebate.

**How:** Short the bond and you owe the lender its coupon, $r + Z$, while the cash collateral earns the rebate $r - \text{fee}$; the net cost is $Z + \text{fee} = 120 + 35 = 155$ bp, and $0.0155 \times 15 = \$0.2325$mm. Buy protection instead and you pay the running price: 110 bp is the 100 bp standard coupon plus an upfront of about $(110 - 100) \times 4.5 = 0.45$ points, which amortised over a 4.5-year risky duration is another 10 bp, so $0.0110 \times 15 = \$0.165$mm all-in. The \$67,500 is the 35 bp fee plus the 10 bp by which the bond's Z-spread sits above the CDS, 45 bp on \$15mm. It is paid for with an ISDA and margin, an auction in place of a bond on the day of a default, a check on which entity the contract references, and a basis (−10 bp today) that the pod now owns. One more thing the numbers hide: a bond short also shorts rate duration and a CDS does not, so a long bond hedged with protection leaves its rate DV01 on the book. Both costs are annual running costs in dollars; nothing needs pricing, so no measure question arises.

**The trap:** Calling the fee the cost of being short: $0.0035 \times 15 = \$52{,}500$. That forgets the coupon you owe the lender and makes the bond look \$112,500 cheaper than the swap. The opposite slip is to compare 120 with 110 (a \$15,000 gap) and miss that the fee is what makes the swap cheaper.

**If you got this wrong, read:** §8D.2 ("The Short-Leg Menu", including the Math, Gently box on the rebate); Appendix D §D.3 (financing a short); §24.3 for the basis.

