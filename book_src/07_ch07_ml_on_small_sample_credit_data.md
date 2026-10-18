# Chapter 7: Machine Learning on Small-Sample, Non-Stationary Credit Data


## 7.0 Cold Open: Forty-Seven Hats

*The desk, its people, Kaz's model and every number on the slide are fictional and illustrative. The review falls in Theo's third week on the desk, early October 2026.*

The invitation had arrived at 11:42 the night before, from a calendar Theo had not known he was on: *Model Review: HY Cross-Section GBM v3 (Kaz). 9:30–10:00. Optional.* At PJT nothing called "optional" had ever been optional, and Theo assumed the systematic desk worked the same way. He was right, though not for the reason he thought. Here "optional" meant that nobody would stop you from not coming, and that the model would be approved by whoever did.

The attachment was one slide. It had a title (*GBM v3: Top–Bottom Decile, HY Excess Returns, 2004–2024*), a cumulative-return line that climbed from the lower left to the upper right with the serenity of a stock photograph, and a box in the corner with three numbers: *Sharpe (IS) 2.9. Hit rate 61%. Turnover 38%/mo.* There was no footnote. There was no issuer count. There was not even a page number, which Theo found more unsettling than anything else, because years of reading confidential information memoranda had taught him that the page number is where a document admits it has other pages.

He read it the way he had read every CIM that ever crossed his desk at RSSG: from the bottom up, looking for the footnote that is doing the work. In a CIM the work is always somewhere. Adjusted EBITDA is adjusted for something; the run-rate synergies run at a rate somebody chose; the liquidity line includes a revolver the company cannot draw without springing a covenant. The headline is the sponsor's opinion and the footnotes are the facts. A slide with no footnotes was not a slide without assumptions. It was a slide whose assumptions had been moved somewhere he could not see.

He wrote three questions on the back of a printed term sheet, which was the paper he had on hand. *How many companies? How many things tried? What day is each return knowable?* Then he went to bed and did not sleep especially well.

At 9:28 the next morning the review was moved to 2 p.m., because the risk committee chair was stuck on a call about a vendor feed that had delivered Tuesday's prices twice. At 9:31 Kaz arrived at Theo's desk with a laptop, unable to wait.

Kaz had the screen angled toward Theo the way a cat presents a dead bird: proudly, and slightly too close.

"Gradient-boosted trees," Kaz said. "Two hundred and twelve thousand bond-months, eighty-one features, high-yield excess returns, 2004 to 2024. In-sample Sharpe of 2.9 on the top-minus-bottom decile."

Theo had been on the desk three weeks. He had learned that quants say "in-sample" the way bankers say "pro forma": a sincere description of a world that does not exist. He pointed at the top decile.

"How many issuers are in there?"

Kaz scrolled. Scrolled again. "Nine."

"And how many bonds?"

"Fifty-eight. Well. One of the issuers has eleven."

"So the model's best idea is one company in eleven maturities."

"It's a very good company," Kaz said. "Its bonds all go up together."

"That's what makes it one company."

Ines drifted over with a coffee she drank black, at a temperature that suggested she had once lost a bet about it. She looked at the Sharpe ratio for exactly as long as it deserved.

"What's the pot," she said, "and how many hands did you fold before you showed me this one?"

Kaz did the arithmetic out loud, which was brave. "Four model families. Six label horizons. Three winsorization rules. Forty-odd feature sets. Call it three thousand?"

"So you're showing me the best of three thousand hands. Of course it's a good hand. The question is whether it's a good hand *for a guy who looked at three thousand of them*."

From two desks over, without looking up, Mags said: "Back in my day we overfit by hand. We called it conviction. It had a beautiful track record, because nobody wrote down the trades that didn't work."

Theo took the USB stick out of his pocket (the 13-week cash flow model, carried for emotional support) and set it on the desk like a chess piece. "In restructuring, nobody ever asked me whether a bond would go up. They asked whether the thesis was right, how sure I was, and how much to put on. Can the model answer *that*?"

Kaz looked at the stick, then at the screen, then at the nine issuers, and said nothing, which on this desk counted as a concession.

The review happened at two, lasted eleven minutes, and ended with the phrase "let's take it offline," which on a systematic desk means what it means everywhere else. Afterward Theo stayed at his desk while the floor drifted toward the 4 p.m. marks, and did the thing a restructuring banker does when a number looks too good: he opened the file.

Kaz had shared the top-decile holdings as a CSV with one row per bond-month. Theo sorted by ticker. Nine tickers, as advertised. Then he did what nobody on the systematic desk had thought to do, because nobody on the systematic desk had ever built a capital-structure chart at 3 a.m. for a creditor committee: he looked up who owned whom.

Two of the nine "issuers" were not separate companies. One ticker carried a holding company's senior unsecured notes; another, three rows down, carried the operating subsidiary's secured notes, issued by the entity that actually owned the plants. A second pair told the same story in a different industry: an OpCo that issued the bonds and a HoldCo that had issued PIK toggle notes secured by nothing but the OpCo's stock. Any banker who has pitched a creditor committee knows that relationship cold, because the whole fight in a restructuring is about which side of the structural-subordination line your paper sits on. To the data vendor they were four tickers. To the model they were four independent opinions that happened, by remarkable coincidence, to agree every month.

Nine issuers were really seven ultimate parents. Fifty-eight bonds, eleven of them from one company, and two pairs that any credit agreement would have revealed as the same balance sheet seen from two different floors. Theo wrote *ultimate parent?* on the term sheet under his three earlier questions and underlined it twice. It would come back in the cross-validation fight of §7.7.

He did not yet know how to say what was wrong with the slide in a language Kaz would accept. He knew what he would have said at RSSG: the deck showed him a conclusion and hid the denominator. The model had seen 212,000 rows. The question was how much evidence that was.

So here is the question this chapter answers: **how do you learn anything from about 800 issuers, 20 years, three regimes, and prices that are sometimes a rumor, and how do you know when you have learned nothing at all?** Theo's shorter version, the one he would write on a sticky note by the end of the month, is this: *how much evidence do I actually have, and how would I know if the answer were none?*

The chapter answers the sticky note four times, at four layers, in the order the month delivered them to Theo: count the hats, not the rows (§7.1, §7.6); make the label honest about scale, path, exits and carry (§7.3, §7.4); let the model peek at nothing (§7.7, §7.9), which is where the two biases that built and then demolished the bond-factor zoo between 2019 and 2026 come in; and deflate for the hands you folded (§7.8). Meta-labeling (§7.5) is the reward for doing the counting honestly. It is where his credit-agreement read becomes the primary model, and the machine learns only when to trust it and how much to bet.

One measure convention for the whole chapter. Every expectation and probability below is under the physical measure $\mathbb{P}$, because we forecast realized excess returns and realized labels. Risk-neutral objects (OAS, a CDS-implied hazard $\lambda_t$, a Merton distance-to-default) appear only as *features*. Features may be $\mathbb{Q}$ quantities; labels and losses are always $\mathbb{P}$. In Chapter 5's race (§5.1.1), $\mathbb{Q}$ is the bookmaker's book and $\mathbb{P}$ the race card after the race, and §6.3 writes out the change of measure: a one-year CDS at 400bp with 40% recovery implies a $\mathbb{Q}$ intensity of about $0.04/0.6 \approx 6.7\%$ a year, single-B issuers have often defaulted at something like half that rate *(illustrative)*, and a model that forecasts the race card may use the 6.7% only as one more column describing what the market is charging.

## 7.1 Why Credit Is the Worst Machine-Learning Dataset in Liquid Finance

*Theo's week of data archaeology, the desk's data and Kaz's classifier are fictional; the SMU study, the FRED series and their values are real and cited where they appear.*

Theo spent the week after the review doing what he privately called data archaeology. Kaz had the model; Theo wanted the dig site. He started from a comparison Ines gave him on Monday morning, in the tone of someone describing the weather. An equity stat-arb researcher has about 3,000 liquid US names, each with one share class, a closing auction that produces a real price every day, and decades of clean history. A credit researcher has a panel with five structural defects, and each one breaks a textbook machine-learning assumption in a specific, predictable direction. "Find all five," she said, "before the model finds them for you." He found them in the order the week delivered them, one a day, and the rest of the chapter is a repair manual, one defect at a time.

On Monday he asked the data team for "a price" for a single-B retailer's 2029 notes on every business day of 2023. He received 250 numbers, and it took him until lunch to discover that fewer than a third of them were trades. The rest were marks, and they were very well behaved.

**Defect 1: the price is sometimes a rumor.** Most corporate bonds do not trade on most days. A 2026 study from SMU's Cox School (Venkataraman, Jacobsen, and Xu, *Illiquidity Meets Intelligence: AI-Driven Price Discovery in Corporate Bonds*, under review; sample 2017–2023) reports that 60% of corporate bonds did not trade in institutional size on a given day, and 27% did not trade for an entire week. What fills the gap is a mark: an evaluated price, a matrix price, a dealer run, or an AI composite such as MarketAxess CP+. Marks are smooth, and smoothness is a lie with a statistical signature. It lowers measured volatility, induces positive autocorrelation in returns, and makes a backtest's Sharpe ratio look better than anything you could have traded.

> **[SOURCE EXTRACTION]** *Ben_Dor_Quantitative_Credit_Portfolio_Management p.204:* "the magnitude of decline between the top and bottom quintiles (despite the generally higher duration of bonds in the bottom quintile) increases as credit quality deteriorates, consistent with a potentially larger degree of stale pricing for lower credit qualities."
>
> **Annotation.** Ben Dor and coauthors sorted bonds into TRACE-volume quintiles within each rating and found that the least-traded bonds show *lower* daily price-return volatility even though they carry *more* duration. Risk did not fall; information arrival did. The page's second finding (return correlation between volume quintiles falls as the quintiles move apart) says the illiquid bonds are reporting the same news *later*. For machine learning both findings run in the dangerous direction. Staleness is worst exactly where the alpha is supposed to live, down the quality spectrum in single-B and CCC names, and any feature built from lagged returns of illiquid bonds will "predict" their future returns, because the future return is just the mark catching up to news that the liquid market priced last week. Your model will discover this, will call it momentum, and will be unable to trade it, because the only counterparty willing to sell at the stale mark is the pricing service, and the pricing service does not take orders. The modern desk keeps the lesson and changes the tooling. The 2026 desk measures staleness directly (days since last institutional-size print, a composite-versus-last-trade gap) and feeds it to the model as a feature *and* as a sample filter, so that the model is told which observations are prices and which are rumors.

On Tuesday he asked for "the issuer" of every bond in Kaz's top decile and received a list of CUSIPs, each tagged with a six-character issuer code that the vendor had assigned to whichever legal entity signed the indenture. The holding company and the operating company he had found on the night of the review had different codes. As far as the database was concerned, they had never met.

**Defect 2: the issuer is the observation.** A bond panel counts rows by CUSIP. Default, restructuring, LMT risk, and most of the idiosyncratic spread variance live at the issuer, or more precisely at the ultimate parent.

> **[SOURCE EXTRACTION]** *Dynkin_Systematic_Investing_in_Credit p.651:* "As of 31 May 2018, US Corporate IG and HY indices included 629 and 784 issuers (column 1 of each panel) or 573 and 576 public issuers (column 2 of each panel) domiciled in the United States."
>
> **Annotation.** Here is the number that should appear on the first slide of every credit ML pitch. Whatever your bond-month count says, the US high-yield cross-section was 784 issuers on that date, and only 576 of them had public equity, which matters because public equity is where most of the timely information in credit comes from (Chapter 9 on equity-to-credit signals). Forty-seven bonds from one issuer are one data point wearing forty-seven hats. Count rows and you will believe you have 200,000 observations. Count issuers and you have a few hundred per cross-section, with monthly cross-sections that are heavily autocorrelated because issuers change slowly. Section 7.6 makes this quantitative with an effective sample size $N_{\text{eff}}$, and §7.7 makes it structural by forcing every bond of an ultimate parent into the same cross-validation fold. The RSSG reader should feel at home: the organizational chart in a first-day credit agreement review (HoldCo, OpCo, restricted and unrestricted subsidiaries, guarantors) is exactly the grouping key the model needs, and a pure quant who groups by ticker will leak information between a parent and the unrestricted subsidiary its best assets were just dropped into.

On Wednesday he went looking for the paper that had been swapped out in the uptier and drop-down exchanges of 2020–2022, the Serta-style transactions he had spent two years of his life on at RSSG, and found that several of the old bonds had simply left the panel. Their final status read "exchanged." The corporate-action field beside it read "voluntary." Theo, who had sat in rooms where the lenders who were not invited to an exchange learned what voluntary meant, laughed out loud, and Kaz asked him what was funny.

**Defect 3: the sample curates itself.** Bonds leave the panel through calls, tenders, maturities, defaults, and distressed exchanges, and each exit is informative. A tender is usually at a premium to market; a distressed exchange is usually a loss dressed as a choice. "Open market purchase," still the most expensive three words in finance, also turns out to be one of the most expensive data-cleaning problems: a bond that disappears through an exchange labeled voluntary is survivorship bias wearing a trench coat. Section 7.4 handles exits as censoring.

On Thursday he asked Kaz when the second-quarter leverage feature entered the model. "At the end of the second quarter," Kaz said, and Theo asked how, given that the 10-Q did not exist yet. Kaz opened the feature pipeline, read it for a while, and said, "Ah."

**Defect 4: the features arrive late.** Ratings lag spreads. Fundamentals arrive with a 10-Q filing lag of up to 40 or 45 days after quarter-end (and longer for 10-Ks and for private filers). A feature that is "Q2 leverage" is not knowable on June 30. Dickerson, Nozawa, and Robotti built a whole paper around this (*Factor Investing with Delays*, 2024): signals must be stamped with the date they became *available*, not the date they *describe*. This is the label-timestamp problem in miniature, and §7.11 shows how a one-month version of it got a top-journal paper retracted.

On Friday the regime label fooled them both.

**Defect 5: the world changes regime, and the panel is short.** Twenty years of TRACE contains roughly three credit regimes (2008, March 2020, the 2022 rates shock) plus the April 2025 tariff spike, and even the calm stretches hide dispersion. A regime label computed at the index level is one hat on nineteen hundred heads.

The scene that made the point was small and happened before nine. Kaz's regime classifier, a hidden-Markov model fitted on the index OAS, printed its morning state in the corner of the risk dashboard: *CALM (p = 0.91)*. Theo, who distrusted any single word in a box the way he distrusted any defined term in capital letters, pulled up the CCC-and-lower series beside it. The dashboard was showing the 15 October close. The index OAS was 3.23%, not far above the 2.59% it had touched on 22 January 2025. The CCC tier was 12.78%, wider than the 11.37% it had reached at the April 2025 panic, when the index itself had touched 4.61% on 7 April and people on the floor had used the word "unprecedented" before lunch (ICE BofA series on FRED, BAMLH0A0HYM2 and BAMLH0A3HYC, fetched 2026-10-17).

"Your model says calm," Theo said. "The bottom of the market is wider than it was on the day everybody thought the world was ending."

Kaz pointed out, correctly, that the classifier had been trained on the index and was faithfully reporting the index. Ines pointed out, also correctly, that the desk's book was not the index. They were both right, which is what makes this defect dangerous. A regime label is a summary statistic of the panel, and a summary of 1,900 bonds can be serene while the 200 that matter to a distressed book are not. Worse, even a perfect regime label gives you very few regimes to learn from: three or four in twenty years, and the count does not grow when you sample daily. That last fact turned out to be the one underneath all the others.

**And underneath all five: sampling faster does not buy you a better mean.** This is the defect that sells the most bad backtests, so it is worth deriving.

> **Math, Gently.** *Standard error, $\sqrt n$, and why daily data does not help you estimate a mean.* A **standard error** is the wobble of Chapter 4's bathroom scale (§4.6): how much your estimate would move if you could rerun history and measure again. Averaging $n$ independent readings shrinks that wobble by a factor of $\sqrt n$: four readings halve it, a hundred cut it to a tenth. The trap is assuming that slicing the same year into more pieces gives you more readings of the thing you care about. Picture measuring a river's annual flow by dipping a gauge every second. You will learn the river's *choppiness* exactly, and its *annual total* no better than one good year of records would tell you, because every second's reading is a tiny slice of the same one year. Tiny number: a strategy earns $\alpha = 2\%$ a year with $\sigma = 4\%$ a year. One annual observation gives a mean of 2% with a standard error of 4%, a ratio of 2. Twelve monthly observations give a monthly mean of about $0.17\%$, monthly volatility of $4\%/\sqrt{12} \approx 1.15\%$, and a standard error of the monthly mean of $1.15\%/\sqrt{12} = 4\%/12 \approx 0.33\%$, the same ratio of 2. You did twelve times the work and bought exactly zero extra certainty about the mean. The full version, in three lines of algebra, is in the Paleologo annotation just below.

> **[SOURCE EXTRACTION]** *Paleologo_Advanced_Portfolio_Management p.49:* "But the relative size of the error doesn't depend on n!"
>
> **Annotation.** Paleologo's point, rebuilt in our notation: suppose an annual excess return has mean $\alpha$ and volatility $\sigma$. Split the year into $n$ periods (months, days). Each period's return has mean $\alpha/n$ and volatility $\sigma/\sqrt n$. The sample mean of $n$ period returns estimates $\alpha/n$ with standard error $(\sigma/\sqrt n)/\sqrt n = \sigma/n$. The relative error is $(\sigma/n)/(\alpha/n) = \sigma/\alpha$, which does not depend on $n$. Daily data estimates *volatility* beautifully and estimates the *mean* no better than one annual observation per year. Over $T$ years the $t$-statistic of the mean is $(\alpha/\sigma)\sqrt T$. A credit signal with an honest information ratio of 0.5 and a 20-year history has $t \approx 0.5\sqrt{20} \approx 2.2$, which, as §7.8 will show, is not enough once you have tried more than a handful of signals. The only way to get more independent evidence about a mean is more *calendar time* or more *independent cross-sectional bets*, and Defect 2 just told you the cross-section is smaller than it looks. This is why credit ML is a small-sample problem even when the dataset is measured in gigabytes.

Kaz read the annotation twice, then wrote the myth on the whiteboard, in order to cross it out.

> **Desk Myth vs. Desk Reality.** *Myth:* "We have 212,000 bond-month observations, so a gradient-boosted model with 81 features is comfortably identified." *Reality:* you have about 800 issuers, roughly 20 independent years for anything that depends on the market regime, overlapping labels that duplicate each other, and marks that are partly the pricing service's opinion. The model is identified the way a 300-page credit agreement is "clear": only to the person who wrote it.

## 7.2 Trend Watch: The Bond-Factor Replication Crisis, 2019–2026

**Long Scene 1: The Four-Factor File.** *The desk, its people, its rebuild, and every number attributed to the desk are fictional and illustrative. The papers, the retraction, the dates, and every quoted word from a real person are on the public record and cited where they appear.*

Once a quarter, on a Saturday, Ines runs a replay. Chapter 1 has the rules: pick an episode, put the calendar back to its first day, use only what was known on each day, and whoever mentions the ending buys lunch. This quarter she did not pick a crisis. She picked a Friday afternoon in October 2022, and the reason was a file.

It lived in a folder on the desk's shared drive called `/benchmarks/academic/`, which nobody had opened in years, and it was named `bbw_factors_2022-10-14.csv`. A portfolio manager who had since left the firm had asked for it that Friday. Ines wrote the request on the whiteboard in his own words, which she had kept, because she keeps everything:

*Need a proper benchmark for IDO stripping before the consultant review. Use the standard four-factor bond model. It's in the JFE. Monday please.*

"That's the hand," Ines said. "It's 14 October 2022. You have this desk's TRACE history as of that night, this desk's code as of that night, and the file. The PM wants it Monday. Go."

Mags, who had been on the desk in October 2022 and knew how the story ended, folded her hands on the table and said nothing, in the manner of a woman who has decided in advance to be expensive about it.

Kaz opened the file. It was beautifully small: a date column and four return columns, one row per month, for the bond market factor, the downside-risk factor, the credit-risk factor, and the liquidity factor of Bai, Bali, and Wen's 2019 paper in the *Journal of Financial Economics* (volume 131, issue 3), a paper a good part of the empirical bond literature had started citing in its opening pages. The desk motto is "IDO or it didn't happen," and the motto needs a benchmark, because idiosyncratic alpha is whatever is left after you strip out what the benchmark explains. Kaz had the regressions running in under ten minutes: every bond's monthly excess return on the four factors, rolling 36-month betas, residuals stacked into the IDO series the desk reported to clients. The desk's alpha shrank, which everyone in the room found reassuring. A benchmark that makes you look worse feels conservative, and conservative feels correct.

"Done," Kaz said. "We could send it tonight. Published, refereed, widely used. That's what a standard is."

Theo was looking at the date column. It held a year and a month on each row, from the early TRACE years down to the last update, and nothing else.

"What's the as-of date of each return?" he said.

"It's the month."

"Which month, though? The month it describes, or the month you could have known it?"

Kaz looked at him the way a mathematician looks at someone who has asked whether zero counts as a number. "Those are the same month. A January return is a January return."

"In a credit agreement they're never the same day." Theo reached for the nearest paper, which was a printout of the PM's request, and drew a timeline on the back. "The leverage covenant tests as of the last day of the quarter. The compliance certificate that tells you whether you passed is delivered forty-five days later. Same test, two dates, and they're two different defined terms. I've sat in a room where a company tripped a covenant on March 31 and nobody, including the company, knew until the middle of May. Anyone who traded in April on the March 31 number was trading on a document that didn't exist yet." He tapped the date column. "This says 'January.' It doesn't say whether the January number used anything that wasn't printed until February."

"That's a footnote problem," Kaz said.

"Footnotes," said Mags, unable to help herself, "are where I made my money." Ines raised an eyebrow, and Mags held up both palms. "I'm not saying anything about the ending. I'm saying something about 1998. Back in my day there was a bond, I won't say which, where the whole trade was a definition on page 140 of the indenture of when a payment counted as 'made.' Everybody priced it off the coupon date. I priced it off the definition. The definition won." She folded her hands again. "That's all. Carry on."

Kaz's position, which they argued well, was that a refereed series is the thing you check your own work *against*, not the thing you check. Theo's position was that he had spent six years watching refereed, audited, board-approved things turn out to have a definition on page 140. Ines ended the argument the way she ends most arguments, by turning it into something that could be measured.

"Rebuild one," she said. "One factor, from raw prints, with every number stamped with the moment you could have seen it. Then compare."

So the afternoon went to the least glamorous job on a systematic desk, which is most of the job. Theo picked the credit-risk factor, on the theory that its ingredients, ratings and returns, were things he understood without a glossary. Kaz pulled the TRACE history: every reported trade in every bond in the universe, together with the cancellations, corrections, and reversals that dealers' operations teams file when a print turns out to have been wrong, each of which has to be matched to the right original trade before a single price can be believed. The cleaning took ninety minutes and produced, as cleaning always does, a list of several hundred bonds whose prices jumped from 98 to 9.8 and back the same afternoon, which turned out to be somebody putting a decimal point in the wrong place years earlier. Mags, who had once watched people do this with a ruler and a printout, said nothing about that either, at visible cost.

Then Theo asked for the column.

He wanted one more field on every row of the rebuild: the earliest moment at which every input to that row could have been observed by somebody outside the building. For a month-end price, that is when the last qualifying trade was disseminated. For a rating used to sort bonds into portfolios, it is the date of the rating action, not the month the rating describes. For a month's return, it is the first business day after the month closes. He called it `available_at`, and he specified it to ROBO in one sentence, because it was getting late.

ROBO built it in four minutes. Every row of the rebuild now carried `available_at = 2022-10-14 16:02:11`, the moment ROBO had written the file. That was accurate, ROBO noted in its log: it was when the data had become available to ROBO.

Theo rewrote the spec in the form it should have had in the first place: the timestamp at which the *last-arriving input* to the row became observable to a market participant, as a UTC datetime, bounded below by the event it describes and above by the moment the row is first used. ROBO rebuilt it correctly in eleven minutes. Kaz built the credit-risk factor from the rebuild as the paper described it, and lined the two series up.

They did not match. That was expected; nothing ever matches. What was not expected was the *shape* of the mismatch. Month by month, Theo's rebuild and the published credit-risk factor had a correlation of about 0.4 *(illustrative; the desk's rebuild is fictional)*. Kaz shifted the published series by one row, the kind of sanity check you run to make sure a correlation is not hiding a typo, and the correlation jumped to about 0.9. The published file's March looked like Theo's April. Its April looked like his May. For most of the sample, the published series ran one month ahead of the rebuild.

Nobody said anything for a moment. Then Kaz said the thing Kaz was right to say.

"That proves nothing." Kaz pulled a chair closer. "Nobody has ever rebuilt a factor from a paper and matched it to the second decimal. Different cleaning, different filters, different breakpoints, different treatment of defaulted bonds. I've tried it with six papers and matched none. Monthly factor returns are autocorrelated, so any series correlates a little with its own shadow a month over. And we're on a different TRACE vintage from theirs. Give me two forecasts of the same storm, one issued a day late, and they'll line up better shifted than unshifted. You wouldn't conclude that anybody made a mistake. You'd conclude that storms move."

It was a good argument, and on most Fridays it would have been the correct one. Rebuilds are noisy. Correlations between autocorrelated series flatter and mislead. A careful researcher who finds a gap between her rebuild and a refereed paper suspects her rebuild first, and Kaz, who had been burned by rebuilds before, was doing exactly what careful researchers do.

Ines let it land, and then dealt a different hand.

"I don't care whether your rebuild matches," she said. "Matching is a question about you and them. I care about a question that's only about the money. The factor has a premium: on average, it earns something every month. Was that premium payable to a person sitting where we sit, at the moment it was earned?" She uncapped the marker. "So play it at the time it could have been played. Form the portfolio from information with an `available_at` before the return month starts, and take the return over the month *after*. Then do it again with the return window one month earlier, the way the published file is lined up against your rebuild. If the premium survives the honest timing, it's real, your mismatch is cleaning noise, and Kaz wins. If it only shows up when the return window overlaps the information, somebody was paid for reading tomorrow's print."

"That isn't a test of their file," Kaz said slowly. "It's a test of whether their file's timing could have made money."

"It's the only test of their file you can run from this chair. You don't have their code. You have their output and the tape. The tape doesn't care who refereed what."

It took twenty minutes. Built with the honest timing, Theo's credit-risk premium was about 0.1% a month and statistically indistinguishable from nothing. Built with the return window lined up the way the published series was lined up, so that each month's return overlapped the information used to form that month's portfolio, the premium came back at roughly the size the published file showed *(illustrative)*. The difference between the two bars was not cleaning noise. Cleaning noise, as Kaz put it, staring at them, "doesn't know what month it is."

That was the moment Kaz changed sides, and Kaz did it the way Kaz does everything, completely. "If the benchmark earns a premium nobody could have collected," Kaz said, "then every IDO number we strip against it is off by that premium times our beta to it. In the months the benchmark peeked at the right answer we'd understate our alpha, in the months it peeked at the wrong one we'd overstate it, and the error would move with next month's market. We'd be stripping our returns against a time machine."

Theo wrote it on the back of the PM's request, under the timeline: *what caught it was not a better model. It was a column.* He underlined `available_at` twice.

Ines put down the marker and stopped the clock, which in a replay means everyone gets an index card.

"It's six o'clock on Friday, 14 October 2022," she said. "Your rebuild and the published benchmark disagree by one month. Your rebuild could be the thing that's wrong; Kaz has told you three ways it might be. The published series is refereed, cited, and standard, and it's the one the consultant will recognize. The PM wants a benchmark on Monday. Do you ship the published series, your rebuild, or neither? And what do you put in writing?"

Theo wrote three lines. Kaz wrote one, crossed it out, and wrote two. Mags wrote nothing at all, then stood up and announced that she was buying lunch anyway, "as a fee for six hours of keeping my mouth shut, which is a personal record and should be priced accordingly."

Over lunch, with the clock stopped for good, she told them the ending. All of it is on the public record.

Alexander Dickerson, Philippe Mueller, and Cesare Robotti had been replicating the 2019 factors while writing their own paper, and in the course of it they found errors in the data. Their paper, "Priced risk in corporate bonds," appeared in the *Journal of Financial Economics* in November 2023, and its conclusion was blunter than anything said at the whiteboard: previously proposed bond factors, "with traded liquidity as the only marginal exception," add nothing to the corporate bond market factor. The 2019 paper was retracted in December 2023; the citations are in the Trend Watch below. On 10 September 2024 Warwick Business School published an account in which Robotti described what the replication had found: "two of the remaining three factors had a 'lead error', while the third factor had a 'lag error'," and an after-the-fact filter had been "artificially capping their losses over a given holding period." The same account noted that the paper "has been cited more than 400 times in other papers according to Google Scholar." A day earlier, announcing that Mueller and Robotti had won the Fama-DFA Prize for "Priced risk in corporate bonds," the school had quoted Robotti's verdict on the corrected factors: "Once we corrected these errors, we found the formula provided no investment advantage at all." The record states the errors and the retraction. It says nothing about how the errors arose, and neither does this book.

Robotti had widened the point in a seminar at Aarhus University on 11 April 2024, "Common pitfalls in the evaluation of corporate bond strategies," whose abstract argues that the large abnormal returns of many bond strategies come mostly from microstructure noise in transaction prices and from ad hoc winsorization. Those two phrases are the two biases of §7.9, and the 2026 audit in the box below is that argument run across the entire zoo. The four factors, which the site describes as "correctly constructed," are now posted on the Open Bond Asset Pricing site, which is the right place to start a rebuild today and the wrong place to stop one.

Theo listened to the ending and then looked at his index card, and noticed something that he would spend the rest of the month trying to put into words. Knowing the ending told them who had been right. It did not tell them what to do at six o'clock on a Friday with a 0.4, a 0.9, a good argument from Kaz, and no ending, which is the only position anyone ever actually trades from. The retraction came fourteen months after the PM's request. A desk that shipped the published series on that Monday would have reported IDO against a time machine for over a year, and would have been in excellent, refereed company while doing it. On the back of the card he wrote the distinction he had been reaching for. A published factor file is a fine *hypothesis list*: it says which characteristic somebody found interesting, in which universe, over which years, with which sign. As a *benchmark*, a set of numbers you subtract from your own returns before you call the rest alpha, it hands you every timing choice inside it. Rebuilding even one factor with an `available_at` stamp on every input is what turns a file you trust into a file you have audited.

Your own card from six o'clock is still face down. The chapter turns it over twice: §7.7 explains why even a flawless purged cross-validation could not have caught this, because the leak sat upstream of the validation, inside a file the desk treated as ground truth, and Case Study A in §7.11 reads Theo's.

The replay covered one file. The literature around it was running the same experiment at scale. Between 2019 and 2026 the academic corporate-bond literature ran the most expensive cross-validation experiment in its history, and most of the published factors failed it. Here is the dated record.

> **Trend Watch.** *The corporate-bond factor zoo, built and audited.*
>
> - **2019.** Bai, Bali, and Wen publish "Common risk factors in the cross-section of corporate bond returns," *Journal of Financial Economics* 131(3): 619–642: a four-factor model (bond market, downside risk, credit risk, liquidity) that becomes a standard benchmark.
> - **2023 (January, first draft).** Dick-Nielsen, Feldhütter, Pedersen, and Stolborg circulate "Corporate Bond Factors: Replication Failures and a New Framework" (AQR working-paper page dated 5 October 2023; Best Paper, 2024 Utah Winter Finance Conference). Built on a clean database with outliers reviewed one by one and returns around defaults kept in, it reports that "only 23% of the factors considered significant in the literature have significant alphas" (as quoted by Quantpedia, 14 May 2024). Reproducing each paper with that paper's own data choices, only one factor premium stays significant; with the other papers' choices, none do.
> - **2023.** Dickerson, Mueller, and Robotti, "Priced risk in corporate bonds," *JFE* 150(2), 103707: previously proposed bond factors add essentially nothing beyond the bond market factor. While replicating, they find data errors in the 2019 factors, and the 2019 paper is retracted (retraction notice, *JFE* 150(3)). Warwick Business School's account (10 September 2024) says two factors had a one-month "lead error," a third a "lag error," and some extreme losses had been removed; it calls the retraction a first for the journal ("This is the first time this has happened"). Mueller and Robotti receive the Fama-DFA Prize.
> - **2023, the counterweight.** Jensen, Kelly, and Pedersen, "Is There a Replication Crisis in Finance?" (*Journal of Finance* 78(5), 2023), argue with a Bayesian hierarchical model that most *equity* factors do replicate. Keep this in view: the crisis is not "all factors are fake," it is "bond factors were measured badly."
> - **2026 (9 April).** Dickerson, Robotti, and Rossetti post "The Corporate Bond Factor Replication Crisis" (arXiv:2604.07880): 108 signals in nine thematic clusters, August 2002–December 2024 (269 months, 52,656 unique bonds). Of 432 specifications (108 signals × 2 weightings × 2 sorts), 26 (6.0%) survive a Benjamini–Hochberg false-discovery correction. Short-term reversal falls from −0.99% per month ($t=-4.46$) to −0.09% ($t=-0.51$) once the signal and the return stop sharing the same noisy price. The abstract's verdict: "the majority of previously documented factors do not produce statistically significant bond CAPM alphas after correction." The authors release the cleaned data and code as Open Bond Asset Pricing.
>
> *What it means for the desk.* The binding constraint in credit ML from 2019 to 2026 was never model capacity. It was label timestamps, price noise shared between signal and return, and return filters that peek. Every one of those is a cross-validation failure in disguise, and every one is fixable with the machinery in §7.3–§7.9. A desk that adopts the 2026 protocol starts where the literature finished; a desk that downloads a 2019 factor file starts with someone else's lead error.

What stands out is the speed. The canonical four-factor bond model went from publication to retraction in four years, and the field's largest factor zoo went from "hundreds of anomalies" to "26 of 432 survive" in seven. In equities the same audit took two decades. Credit compressed it because the errors were *data* errors, which are verifiable, rather than *multiplicity* errors, which are arguable. And the direction is the one Defect 1 predicts: the price-based signals (reversal, momentum, volatility) were hit hardest, for reasons §7.9 derives.

> **Math, Gently.** *False-discovery correction, or how the bar moves down the list.* Chapter 4 (§4.5) bought the 432 lottery tickets: about 22 of them clear $t > 1.96$ by luck alone, the 2026 audit found 65, and so *some* signal exists in the pile without anyone yet saying which tickets carry it. The Benjamini–Hochberg procedure sets the bar so that, among the tickets you keep, only about 5% are expected to be lucky. Line the p-values up from smallest to largest. The best one has to beat $0.05/432$, the second $2 \times 0.05/432$, the $k$-th $k \times 0.05/432$, and you keep every ticket down to the last one that clears its own bar. Tiny number, as if the procedure were run on all 432 at once: the best specification needs $p < 0.00012$, a $t$ of about 3.85, and if 26 are to be kept, the 26th has to beat $26 \times 0.05/432 \approx 0.003$, a $t$ near 2.97. The bar loosens as you move down the list, because each extra winner you keep is itself evidence that the pile is not all noise. (Dickerson, Robotti, and Rossetti run the procedure separately within each of their four panels of 108; the logic is the same.) The Sharpe-ratio version of this idea, which deflates the single best result for the number of tickets bought, is §7.8.

#### The one-day placebo

The 2026 audit ran a cheap cousin of Ines's test across the whole zoo, a placebo that reads almost like a list of suspects. Dickerson, Robotti, and Rossetti compared, for every signal in their zoo, the return measured from one month-end to the next with a return that starts from the first price of the following month, typically about a business day later. If nothing were leaking, the two would differ only by noise. Among their 30 price-based factors, the gap was statistically significant for 43–67% of them across the paper's specifications, averaging 0.13–0.30% a month in absolute size. Among the 78 factors built from something other than the bond's own price (ratings and estimated betas, for example), it was significant for only 10–18%, at 0.03–0.10% a month (Dickerson, Robotti, and Rossetti 2026, Table B.1). A factor that uses the same print in its signal and its return is a suspect by construction. A factor built from ratings is, at worst, guilty of being slow.

The same shift is a test a desk can run on somebody else's file in minutes, without reproducing the paper: a premium that survives has earned the weeks a full rebuild costs, one that halves is telling you how much of it was timing, and one that disappears was never there to collect, however often it has been cited. Its two blind spots, noise shared inside a single month-end price and filters fitted after the fact, are the two biases of §7.9.

## 7.3 Stationarity With Memory: Fractional Differentiation of Log Spreads

The first thing Theo asked to see, the Monday after the replay, was the feature Kaz's model leaned on hardest. It was the level of log OAS, and its partial-dependence plot (the model's average prediction as that one feature is swept from low to high, everything else held fixed) looked less like an economic relationship than like a calendar: flat across most of the range, then a cliff at exactly the spread levels the index had visited in late 2008 and in March 2020 *(illustrative)*. "It's learned that wide spreads get followed by tightening," Kaz said. Theo looked at the cliff for a while. "It's learned that two particular months got followed by tightening."

Kaz's model in the cold open used the *level* of log OAS as a feature. That is defensible on economics (wide spreads mean-revert; valuation is a level concept, see Chapter 9) and indefensible on statistics: a level that wanders across regimes means the model learns "2008 was wide" rather than "wide predicts tightening." The textbook fix is to difference, using $\Delta \log s_t$. That is stationary, and it is also amnesiac. It throws away exactly the level information that made the feature worth having. The desk wants a dial between "level, non-stationary, full memory" and "change, stationary, no memory." Fractional differentiation is that dial (Hosking 1981; López de Prado, *Advances in Financial Machine Learning*, 2018, ch. 5).

*Stationary* has a precise meaning here. A series is stationary when its average and its spread do not drift over time, and a model needs that, because it learns from the past on the assumption that the past is a fair sample of the future. A random walk is the opposite case (Chapter 6, §6.1.1, has the walker): each step adds to all the previous ones, so the level wanders further with the square root of time while the steps stay the same size. A spread level lives between the two. It wanders like the walker for years and then, eventually, mean-reverts, which is why it is neither safe to feed to a model raw nor wise to difference away.

**Why log spreads and not spreads.** Before anything gets dialed, there is a quieter choice about *which* series gets dialed. Spreads cannot go below zero, blow out more violently than they compress, and move in proportion to where they already sit, which is the lognormal shape rather than the normal bell (Chapter 5, §5.2.3, draws both). In logs a 10% move is the same event at any spread level, and a normal model of spread levels that allows a 50bp shock to a 40bp spread is quietly assigning probability to a negative spread. Ben Dor's evidence for the proportional picture comes next.

> **[SOURCE EXTRACTION]** *Ben_Dor_Quantitative_Credit_Portfolio_Management p.39:* "These results clearly indicate that absolute spread volatility is highly unstable and tends to rise with increasing spread. Computing volatilities based on relative spread change generates a more stable time series."
>
> **Annotation.** This is the empirical foundation of DTS (Chapter 8), and it doubles as a feature-engineering rule. If spread changes are roughly proportional to spread levels, then $\Delta s_t \approx s_{t-1}\,\Delta \log s_t$, and the stable object is the relative change $\Delta \log s_t$, with sector volatilities that Ben Dor and coauthors report clustered between about 5% and a bit over 10% per month on the same page. Feed a model raw spreads, and a 50bp move means one thing for a 100bp BBB and another for an 800bp B3. Feed it log spreads, and the scale is comparable across ratings and across regimes, which is what lets one model span 2008 and 2021 without learning a separate world for each. Where the modern desk departs: the proportionality breaks near default (a bond at 3,000bp quotes on price, not spread) and near zero (the structural floor Ben Dor's own regressions show as a positive intercept). The desk caps the log transform's domain, switches distressed names to price-based features, and says so in the spec.

**The dial, before the algebra.** Ordinary differencing replaces today's log spread with today minus yesterday: a weight of $+1$ on today, $-1$ on yesterday, and nothing on anything older. Leaving the level alone is the other extreme: $+1$ on today, zeros everywhere else, and all of history still baked into today's number. Fractional differentiation picks an exponent $d$ between 0 and 1 and produces weights in between: $+1$ on today, then a string of small negative weights on the past that shrink slowly with age. Each weight comes from the one before by a one-line rule, $w_k = -w_{k-1}(d-k+1)/k$, starting from $w_0 = 1$. The weights fade roughly like $k^{-(d+1)}$, rather than stopping dead after one lag (the ordinary difference) or never fading at all (the raw level), and the running sum of the weights is the share of the original level still left inside the feature.

> **Math, Gently.** *The dial between level and change, read as a memory.* Read each weight as how much of a past day the feature still remembers, with a minus sign because the feature is today *net of* that memory. With $d = 0.5$ the weights are $1, -0.5, -0.125, -0.0625, -0.039, \ldots$: today counts in full, yesterday is subtracted at a half, the day before at an eighth, and the memories keep fading without ever quite reaching zero. Add the first five weights and you get $1 - 0.5 - 0.125 - 0.0625 - 0.039 \approx 0.27$: after four lags, about 27% of the raw level is still inside the feature. Carry the sum out to 200 lags and about 4% survives. With $d = 1$ the weights are $1, -1, 0, 0, \ldots$, the sum is zero after one lag, and none of the level survives; with $d = 0$ the weights are $1, 0, 0, \ldots$ and all of it does. The 4% sliver at $d = 0.5$ is the whole point. It is enough of the level for the feature to remember that the bond is wide, and little enough that the feature's average stops wandering with the regime. The algebra behind every number in this box is in "The Full Derivation: the fractional weights" below, and Exercise 2 asks for the same five weights at $d = 0.4$.

**Fixed-width window (FFD).** The expanding-window version uses more weights for later observations, which makes the transformed series non-stationary by construction (its variance depends on $t$). Fix a weight tolerance $\tau$ and keep only $k \le K(\tau)$ with $|w_k| \ge \tau$:

$$
\tilde x_t = \sum_{k=0}^{K(\tau)} w_k\, x_{t-k}.
$$

Then choose the smallest $d$ that makes the series stationary:

$$
d^\star = \min\big\{ d \in \{0, 0.05, \ldots, 1\} : \text{ADF}\big(\tilde x^{(d)}\big)\ \text{rejects a unit root at } 5\% \big\},
$$

and report $\rho\big(\tilde x^{(d^\star)}, x\big)$, the correlation between the transformed and raw series, as "memory retained." In plain terms, $d^\star$ is the least amnesia that still makes the feature stationary. Fractional differentiation is how much you remember after a closing night: enough to be stationary in the morning, not so much that you remember the covenant you agreed to at 3 a.m.

> **Math, Gently.** *What an ADF test asks.* The augmented Dickey–Fuller test asks one question of a series: when it is far from its average, does it tend to come back? It regresses each day's change on the previous day's level, plus a few lagged changes (the "augmented" part) to soak up short-term wiggles. A clearly negative slope means high levels tend to be followed by falls and low levels by rises, which is mean reversion, and the test "rejects a unit root." A slope indistinguishable from zero means the series is a random walk, with no pull toward home. Tiny number: a slope of $-0.02$ a day closes about 2% of any gap from the average each day, a half-life of $\ln 2/0.02 \approx 35$ days. A slope of $-0.001$ means a half-life of about 690 trading days, nearly three years, and a twenty-year sample holds only a handful of such half-lives, so it can barely tell that pull apart from none at all. That weakness is why the test has low power on spread levels, and why $d^\star$ is a noisy estimate rather than a constant of nature.

One result from the derivation is needed to price the window. For large lags the weights shrink like $|w_k| \approx k^{-d-1}/|\Gamma(-d)|$, where $\Gamma$ is the Gamma function, the factorial extended to non-integers ($\Gamma(n+1) = n!$). That single line turns "how long a memory" into "how many days of history before the first usable value."

**The warm-up cost, computed.** The window length is not a detail. With $d = 0.4$, $|\Gamma(-0.4)| = \Gamma(0.6)/0.4 \approx 1.489/0.4 \approx 3.72$, so $|w_k| \approx k^{-1.4}/3.72$. Setting this equal to $\tau = 10^{-4}$ gives $k^{1.4} \approx 2{,}690$, or $K \approx 280$ trading days, more than a year of warm-up before the first usable value. With $\tau = 10^{-3}$, $K \approx 54$ days. A bond issued 14 months ago has no FFD feature at $\tau = 10^{-4}$, and new issues are exactly where a lot of the relative-value action lives. The fix is to compute FFD on an *issuer-level* constant-maturity log spread (interpolated from the issuer's curve, Chapter 8) and map it to the new bond, rather than on the bond's own short history.

#### The Full Derivation: the fractional weights

Let $B$ be the backshift operator, $B x_t = x_{t-1}$. Ordinary differencing is $(1-B)x_t = x_t - x_{t-1}$. For a real exponent $d \ge 0$, define $(1-B)^d$ by the binomial series:

$$
(1-B)^d \;=\; \sum_{k=0}^{\infty} \binom{d}{k}(-B)^k \;=\; \sum_{k=0}^{\infty} w_k B^k,
\qquad w_k = (-1)^k \binom{d}{k} = (-1)^k\,\frac{d(d-1)\cdots(d-k+1)}{k!}.
$$

Take the ratio of consecutive weights. The numerator gains the factor $(d-k+1)$, the denominator gains $k$, and the sign flips:

$$
\frac{w_k}{w_{k-1}} = -\,\frac{d-k+1}{k}
\quad\Longrightarrow\quad
w_0 = 1,\qquad w_k = -\,w_{k-1}\,\frac{d-k+1}{k}.
$$

So $w_1 = -d$, $w_2 = d(d-1)/2$, $w_3 = -d(d-1)(d-2)/6$. For $d = 1$ the recursion gives $w_2 = 0$ and every later weight vanishes, recovering $x_t - x_{t-1}$. For $0 < d < 1$, every weight after $w_0$ is negative (each step multiplies by $-(d-k+1)/k$, which is positive once $k > d+1$, so the sign set at $w_1 = -d$ persists) and the magnitudes decay *hyperbolically*. Writing the weights with Gamma functions, $w_k = \Gamma(k-d)/\big(\Gamma(-d)\,\Gamma(k+1)\big)$, and using $\Gamma(k-d)/\Gamma(k+1) \sim k^{-d-1}$:

$$
|w_k| \;\sim\; \frac{k^{-d-1}}{|\Gamma(-d)|}\qquad (k \to \infty).
$$

That slow decay is the "long memory": a shock from 200 days ago still carries weight, unlike an ARMA filter whose weights decay geometrically.

How much of the level survives? Use the partial-sum identity $\sum_{k=0}^{K} (-1)^k\binom{d}{k} = (-1)^K\binom{d-1}{K}$, whose magnitude behaves like $K^{-d}/\Gamma(1-d)$. As $K \to \infty$ the full filter's weights sum to $(1-1)^d = 0$, so an infinitely long fractional difference annihilates a constant level, just as ordinary differencing does. But the decay is slow, and a *truncated* filter keeps a sliver of the level proportional to $K^{-d}$. That sliver is the memory we wanted to keep. Small $d$ keeps more; $d=1$ keeps none.

#### The refit: a cliff becomes a slope

Kaz refit the model that week with $d^\star = 0.35$ on log OAS, chosen inside each training fold, and the cliff in the partial-dependence plot turned into a slope *(illustrative)*. The slope was less impressive and, as it turned out, more durable. Theo asked whether every feature should get the same treatment, and Kaz's answer was the list of features that had earned it: the *level-type* ones observed over long histories (log OAS, log DTS, leverage, interest coverage), whose value means something because of where it sits rather than how it just moved, with enough years behind them that a 280-day warm-up is a rounding error.

Ines did not ask for the ADF statistic. She asked for a picture: the transformed series plotted over the raw one, with the memory-retained correlation printed in the corner. Kaz's log OAS still looked like the spread's history, wide in 2008, wide in March 2020, tight in 2021, and the correlation was high, so the feature had kept its memory. "And if it looks like a seismograph?" Theo asked. "Then the dial has differenced it in all but name," Ines said, "and thrown away the level that was the reason for using a level. If the correlation is below about 0.3, call it a change feature and label it as one." *(The 0.3 is the desk's illustrative threshold, not a standard.)*

> **Ways This Blows Up.** *Three ways fractional differentiation lies to you in credit.* (1) **Jumps.** A jump-to-default or an LMT announcement is a level shift that no $d<1$ makes stationary. One Serta-style uptier in the sample will dominate the ADF statistic and push $d^\star$ toward 1. Estimate $d^\star$ on a jump-filtered series (or on IG and HY separately), apply it to the raw one, and handle jumps as events, not as noise. (2) **Stale marks.** A stale bond's spread series is a step function. That manufactures positive autocorrelation in changes and makes the level look more persistent, so you can get a "low $d^\star$" from an illiquid bond whose low $d^\star$ is a liquidity artifact. Dynkin p.771 makes the same point about return autocorrelation; here it contaminates the memory estimate. (3) **Look-ahead in $d^\star$ itself.** Choosing $d^\star$ on the full sample and then backtesting uses the future to pick a preprocessing parameter. Choose $d^\star$ inside each training fold, or fix it once on a burn-in period you never test on.

## 7.4 Labels That Respect Credit: The Triple Barrier in DTS Space

The default label in a first-draft notebook is $y = \operatorname{sign}(r_{t \to t+h})$: did the bond's excess return over the next $h$ days end up positive? It fails credit on path, scale and exits. It ignores the *path*: a bond that fell 9 points in week 2, triggering every risk limit on the desk, and then recovered to $+0.1$ by week 13 is labeled a winner. It ignores *scale*: a 1% move is noise for a CCC and a career event for an A-rated utility. And it ignores *exits*: the bond that was tendered at 101 in week 5 has no week-13 return at all. The triple-barrier method fixes all three. Credit needs one more adjustment, which is to measure the barriers in DTS units. Duration times spread is a bond's risk clock: spreads move by percentages of themselves (Ben Dor's evidence in §7.3), so a bond's excess-return volatility scales with $D^{\text{spr}} \times s$, and a five-year bond at 400bp ($0.20$) ticks five times as fast as a two-year bond at 200bp ($0.04$). Chapter 1-B (§1B.2) draws the ruler, Chapter 8 builds it from the ground up, and the Full Derivation at the end of this section works one bond through.

**The picture before the formulas.** Think of every label as a bond walking down a corridor that begins on the formation date. The corridor has a ceiling, a floor, and a wall at the far end. The ceiling is the profit-taking barrier: if the bond's cumulative residual return reaches it, the label closes as a win on the day it gets there, whatever happens afterward. The floor is the stop, and in credit it is less a floor than a trapdoor, because the worst exits do not arrive as a gentle slide; they arrive as a jump from 92 to 55 between two marks. The wall is the vertical barrier, the horizon $h$, which this book sets at thirteen weeks for reasons the USB stick will explain shortly; a bond that reaches the wall without touching ceiling or floor is labeled by the sign of where it ended up. Two more features make it a *credit* corridor. Its height is not fixed. A quiet short-dated BBB walks a low corridor and a long-dated single-B walks a tall one, because the ceiling and the floor are drawn in DTS units, scaled by $\hat\sigma_{\text{rel},t}$ (the typical percentage move of the spread per period) and by the square root of the time allowed. And the corridor has side doors: a tender, a call, or an exchange can take the bond out of the building before it reaches anything, and the label has to record which door it used. Three sample walks make the picture concrete *(illustrative)*. A bond at DTS 0.20, with a corridor half-height of about 3.5% over thirteen weeks, touches the ceiling in week 6 and is labeled $+1$ that day. A second falls through the trapdoor in week 9 and is labeled $-1$, with a realized loss many corridor-heights deep. A third is tendered at 101 in week 5 and leaves by a side door, labeled `touch = "exit"`. The formulas below are this picture written down.

**The barriers.** For bond $i$ at formation date $t$, let $X_{i,t}(u) = \sum_{v=1}^{u} r^{\text{xs}}_{i,t+v}$ be cumulative excess return after $u$ days, and let $h$ be the horizon in the same units as $\hat\sigma_{\text{rel}}$. Define

$$
\bar b_{i,t} = +\,\bar m\;\text{DTS}_{i,t}\,\hat\sigma_{\text{rel},t}\sqrt{h},
\qquad
\underline b_{i,t} = -\,\underline m\;\text{DTS}_{i,t}\,\hat\sigma_{\text{rel},t}\sqrt{h},
$$

with a vertical barrier at $u = h$. The label is $y_{i,t} = +1$ if $\bar b$ is touched first, $-1$ if $\underline b$ is touched first, and $\operatorname{sign}\big(X_{i,t}(h)\big)$ at the vertical barrier (optionally $0$ inside a dead zone $|X| < \epsilon$). Record the touch time $t_{1,i}$. The *label interval* $[t_{0,i}, t_{1,i}]$ with $t_{0,i}=t$ is the object that §7.6 and §7.7 need: it defines which labels overlap and therefore which ones must be purged.

> **[SOURCE EXTRACTION]** *Ben_Dor_Quantitative_Credit_Portfolio_Management p.50:* "a portfolio with a weighted spread of 200 bps and spread duration of two years is equally risky as a portfolio with a spread of 100 bps and spread duration of four years."
>
> **Annotation.** Both portfolios have the same DTS (2 × 200 = 4 × 100 = 400 in the bp-years convention), so they get the same barrier. That is the entire argument for DTS-scaled labels, in one sentence. A barrier set at a fixed 2% would label the long-duration IG bond's ordinary month as an event and the HY bond's ordinary month as nothing. A DTS barrier puts both on a common risk clock. Ben Dor's group also estimates the slope of excess-return volatility on DTS directly: 8.8% per month for corporates, and 9.8% for the Aaa Agency debentures used as a cross-check on p.57 (with DTS measured in years × percent, so a DTS of 20 maps to roughly $0.088 \times 20 \approx 1.8\%$ per month). That slope *is* $\sigma_{\text{rel}}$, so the book's default prior for the barrier scale is "about 9–10% relative spread volatility per month" before any estimation, and an estimated $\hat\sigma_{\text{rel},t}$ that comes out at 3% or 30% should trigger a data check, not a celebration. The modern departure: estimate $\hat\sigma_{\text{rel},t}$ with an exponentially weighted window per rating bucket, because the 2022 and April 2025 episodes showed relative vol itself moves with the regime.

**Strip the carry, or the label learns the coupon.** Here is a number that surprises people. Take $h = 13$ weeks $= 3$ months, $\text{DTS} = 0.20$, $\sigma_{\text{rel}} = 10\%$ per month, $\bar m = \underline m = 1$. The barrier half-width is $0.20 \times 0.10 \times \sqrt 3 \approx 3.5\%$. A 500bp bond accrues carry of $0.05 \times 0.25 = 1.25\%$ over the same 13 weeks, about 36% of the barrier width *(illustrative)*. Raw excess-return labels in high yield are therefore tilted toward $+1$ by carry alone, and a model trained on them learns to buy the highest-spread bonds, which is the always-long-carry strategy with extra steps. Build the labels on carry-adjusted, market-beta-stripped residual returns (the IDO return of Chapter 8) instead. The desk motto applies to labels too: IDO or it didn't happen.

**The trapdoor.** Because the floor of the corridor gives way rather than holding, the realized return at touch can sit many barrier-widths below $\underline b$, and the sign alone throws that depth away. The label keeps it, $X_{i,t}(t_{1,i}-t)$, beside the $-1$: §7.6 uses it for return-attribution weights, and the sizing layer in §7.5 needs to know that $-1$ labels in CCC carry fatter losses than $+1$ labels carry gains (Chapter 5's mixture distributions). The same asymmetry argues for $\underline m < \bar m$ in the lowest ratings, a tighter stop on the side where the distribution has a jump component, which is how a risk manager would actually run the position.

**The 13-week model, reborn.** How long should $h$ be? Theo's answer was immediate, and for once the data agrees with the emotional-support USB stick.

> **[SOURCE EXTRACTION]** *Dynkin_Systematic_Investing_in_Credit p.611:* "The number of issuers that remain above median drops by 31% in the first month after momentum signal formation. After six months, 52% of issuers drop out."
>
> **Annotation.** This is signal-decay evidence for equity-momentum-based bond portfolios, and it sets the vertical barrier. If a third of the signal's membership churns in month one and half by month six, a 12-month label mostly measures what happened *after* the information was spent, and adds overlap (every daily label shares 11 months with its neighbor) without adding evidence. The book's default is $h = 13$ weeks, which sits where Dynkin's evidence says most of the effect has arrived and also where Theo's 13-week cash flow model has always stopped forecasting. That running gag is now a hyperparameter. The departure: decay rates differ by signal family. Value signals in credit decay more slowly than momentum (Chapter 9), so a value label can justify a longer vertical barrier, and the purging in §7.7 must then widen with it.

**Censoring: when the bond leaves before the label finishes.** Bonds exit through calls, tenders, maturities, defaults, and exchanges. The practitioner literature has a standard way of handling exits in *portfolio* studies:

> **[SOURCE EXTRACTION]** *Ben_Dor_Quantitative_Credit_Portfolio_Management p.338:* "If an issuer left the sample before the end of the analysis window, because all its outstanding bonds matured, were called, or defaulted, we assumed that it continued to earn the same return as its peer group for all remaining months."
>
> **Annotation.** For the question Ben Dor's group was asking (how fallen angels perform relative to peers over a long window), peer-return imputation is sensible: it keeps the cohort intact and prevents the survivors-only bias that would flatter the distribution. For a *supervised label*, the same move is a leak. The exit itself carries information. A tender at a premium is a positive outcome the model should learn to anticipate, and a distressed exchange (an "open market purchase" in a trench coat) is a negative one. Replacing either with the peer-group return teaches the model that exits are average, which is exactly backward. The label rule for this book: close the label at the exit date and exit value (the tender price, the call price, or the market value of the exchange package), set `touch = "exit"`, record the exit type, and set `censored = True` when the exit occurs before the vertical barrier. The model sees what really happened, and the analyst can later decide whether to train on censored labels, drop them, or model exits as a competing risk (Chapter 14).

> **Ways This Blows Up.** *Touches on stale marks.* A barrier "touch" on an evaluated price that reverts the next day is not an event; it is the pricing service sneezing. Require a touch to be confirmed by an institutional-size print, or by two consecutive marks beyond the barrier, before closing the label. The 2026 replication literature added a bounce-back filter to TRACE cleaning for the same reason (Dickerson, Robotti, and Rossetti 2026): a price that jumps and immediately jumps back is usually an error. And never compute the feature and the first day of the label from the same month-end price; §7.9 shows that this single shortcut manufactured most of a published factor.

Theo asked what the corridor would look like from the chair of the lenders he used to negotiate against at RSSG, the CLOs.

> **View From Another Seat.** *The CLO manager.* Walk the same corridor from a CLO manager's chair and the trapdoor looks different. For the desk, a fall through the lower barrier is a $-1$ label and a realized loss. For a CLO it is an event in the deal's own rulebook, and the rulebook has its own calendar. A downgrade to CCC moves the loan into a bucket that is typically capped at 7.5% of the portfolio; par above the cap is carried at market value instead of par in the overcollateralization tests, and a loan bought cheaply enough (often below 80 to 85) can be carried at its purchase price as a discount obligation (typical terms; every indenture differs, and §21.4.1 writes the adjusted numerator out). So the CLO manager does not much want a label at all. What the seat wants is the probability that a given loan or bond is downgraded into the bucket, or marked below the discount threshold, *before the next determination date*, because that is the day the tests are run and the day a failure diverts cash away from the junior notes. The horizon the CLO would choose is not thirteen weeks because of a USB stick; it is however many weeks remain until the indenture next looks. The barrier it would choose is not a multiple of DTS; it is a rating notch and a price, 80, written into a legal document. Neither seat is wrong. The point for this chapter is that $h$ and the barrier heights are business choices disguised as hyperparameters, and the honest way to set them is to ask who will act on the label and on what date their rulebook bites.

#### The Full Derivation: why the barrier is proportional to DTS

Over a short interval the excess return of bond $i$ is carry minus spread duration times the spread change (Chapter 8 has the full decomposition):

$$
r^{\text{xs}}_{i,t} \;\approx\; s_{i,t-1}\,\Delta t \;-\; D^{\text{spr}}_{i,t-1}\,\Delta s_{i,t}.
$$

If spread changes are proportional to spread levels (the Ben Dor result quoted in §7.3), write $\Delta s_{i,t} = s_{i,t-1}\,\Delta \log s_{i,t}$. Then the volatility term is

$$
D^{\text{spr}}_{i,t-1}\,\Delta s_{i,t} \;=\; \underbrace{D^{\text{spr}}_{i,t-1}\, s_{i,t-1}}_{\text{DTS}_{i,t-1}}\;\Delta \log s_{i,t}
\quad\Longrightarrow\quad
\sigma\big(r^{\text{xs}}_{i}\big) \;\approx\; \text{DTS}_{i}\,\sigma_{\text{rel}},
$$

where $\sigma_{\text{rel}} = \sigma(\Delta \log s)$ is the relative spread volatility per period. Units matter here: with $D^{\text{spr}}$ in years and $s$ in decimal, a five-year bond at 400bp has $\text{DTS} = 5 \times 0.04 = 0.20$; with $\sigma_{\text{rel}} = 10\%$ per month, its excess-return volatility is about $0.20 \times 0.10 = 2\%$ per month.

## 7.5 Meta-Labeling: The RSSG Analyst as the Primary Model

The question Theo asked in the cold open, with the USB stick on the desk like a chess piece, is the chapter's main idea for the reader who came from restructuring: **you already do meta-labeling for a living.** López de Prado's meta-labeling splits the problem the way a restructuring banker does, into the thesis, the confidence and the size. A *primary model* decides the side. A *secondary model* is trained only to predict whether the primary is right, and its probability becomes the bet size.

The division of labor is the whole point. The pure quant cannot build a good primary model for special situations, because the primary model is legal prose converted into state space: drop-down capacity in the unrestricted-subsidiary basket, an open-market-purchase clause loose enough to drive a Serta uptier through, a 13-week liquidity runway that ends before the next coupon. That is the Priming Risk Score of Chapter 13, the structural distance-to-default of Chapter 6, and the cash runway Theo keeps on the USB stick. The banker, meanwhile, has never been made to estimate the *precision* of their own calls, let alone condition it on the spread regime, the sector, or how many dealers are already short the bond. Meta-labeling is where the two halves meet.

**The math.** The primary model produces a side $\hat y^{(1)}_{i,t} \in \{-1, +1\}$. Given the triple-barrier label $y_{i,t}$ from §7.4, define the meta-label

$$
y^{(2)}_{i,t} = \mathbf 1\big\{\hat y^{(1)}_{i,t}\, y_{i,t} > 0\big\},
$$

that is, 1 when the primary was right. The secondary model estimates $p_{i,t} = \mathbb{P}\big(y^{(2)}_{i,t} = 1 \mid \mathcal{F}_t\big)$ from features the primary does not use (spread regime, staleness, dealer positioning, issuer dispersion). Map the probability to a size with the test statistic for "is $p$ different from a coin flip":

$$
z_{i,t} = \frac{p_{i,t} - \tfrac12}{\sqrt{p_{i,t}(1-p_{i,t})}},
\qquad
m_{i,t} = 2\,\Phi(z_{i,t}) - 1 \in (-1, 1),
\qquad
\text{size}_{i,t} = \max(m_{i,t}, 0)\cdot \hat y^{(1)}_{i,t}.
$$

Here $\Phi$ is the standard normal CDF, the bell curve's running total ($\Phi(0) = 50\%$, $\Phi(1) \approx 84\%$, $\Phi(2) \approx 98\%$), and $z$ is the z-score of Chapter 4 (§4.6): how far $p$ sits from a coin flip, measured in the wobble a coin-flip estimate would have. Then $2\Phi(z) - 1$ squashes that distance into a number between $-1$ and $1$. The numbers are worth carrying around: $p = 0.5$ gives size 0; $p = 0.75$ gives $z = 0.25/0.433 = 0.58$ and $m \approx 0.44$; $p = 0.9$ gives $z = 0.4/0.3 = 1.33$ and only $m \approx 0.82$, because the map is deliberately reluctant near the top. Truncating at zero means the secondary can only shrink or veto a primary call, never reverse it. That is deliberate: the secondary model knows *when* the analyst is reliable, not *what* the analyst knows.

> **Poker Table.** Ines, to Theo: "Your read on the covenant is your hand. The meta-model is the part of you that remembers how often that hand wins at *this* table, with *these* players, at *this* hour. You don't bet your opinion. You bet your confidence in your opinion. Most people at this table bet their opinion, which is why I like this table." Then, replaying the hand history: "Your drop-down calls were right 61% of the time overall. When the bond had already moved five points on no news, you were right 78% of the time, because someone else had read the same basket. When the bond hadn't moved, 52%. Same hand, different table. Size accordingly."

**Precision, recall, and the marketing sentence.** The natural division of labor tunes the primary for *recall* (miss no candidate trapdoor) and the secondary for *precision* (bet only when the call is likely right). The desk pays for the combination, summarized by $F_1 = 2PR/(P+R)$. A real-world sentence shows why reporting one side of this trade-off is uninformative.

> **Math, Gently.** *Precision, recall, and the four-cell table.* Every yes-or-no flag lands in one of four cells. Flagged, and it happened: a true positive. Flagged, and it did not: a false alarm. Not flagged, and it happened: a miss. Not flagged, and it did not: the quiet majority. That two-by-two grid is the **confusion matrix**. **Recall** asks, of the things that happened, what share you flagged. **Precision** asks, of the things you flagged, what share happened. A smoke alarm that goes off whenever anyone makes toast has perfect recall and dreadful precision; one that never goes off has no false alarms and a recall of zero. $F_1$ is the harmonic mean of the two, which punishes whichever is worse. Tiny number: flag 20 bonds as trapdoor candidates; 5 of them later fall through, and 5 bonds you did not flag fall through too. Precision is $5/20 = 25\%$, recall is $5/10 = 50\%$, and $F_1 = 2(0.25)(0.5)/0.75 \approx 0.33$. The annotation just below runs the same arithmetic on a real marketing sentence, where only one cell of the four was published.

> **[SOURCE EXTRACTION]** *BlackRock_Systematic_High_Yield_Credit p.6:* "Our proprietary probability of default signal that has underpinned all of our credit strategies for over 20 years has successfully identified 77% of the defaulted bonds in the ICE BofA High Yield Index within 24 months of its default since 2010."
>
> **Annotation.** Seventy-seven percent is a *recall*: of the bonds that defaulted, the share that had been flagged. It is a perfectly honest number, and on its own it tells you nothing about how useful the signal is, because a signal that flags every bond in the index has 100% recall. A marketing sentence is a confusion matrix with one cell filled in; ask for the other three. Here is an illustration with made-up round numbers *(illustrative, not BlackRock's)*: a 1,000-bond universe with a 6% 24-month default rate has 60 defaulters, so 77% recall catches about 46 of them. If the signal flags 200 bonds, precision is $46/200 = 23\%$, nearly four times the 6% base rate: a valuable underweight list. If it flags 400 bonds, precision is 11.5% and the lift is under 2×. Same recall, very different signal. The page also says the signal's logic is structural (default when asset value falls below liabilities), which makes it a natural *primary* model in our framework: high-recall, economically grounded, and in need of a secondary model to say when its flags deserve size.

Kaz's first secondary model, fitted that week to Theo's drop-down calls, walked into the first two of these leaks before lunch *(illustrative)*.

> **Ways This Blows Up.** *Three meta-labeling leaks.* (1) **Training the secondary on in-sample primary calls.** If the primary model was fit on the same data, its calls are overfit and look right too often; the secondary learns to trust an illusion. Generate primary calls out of sample (walk-forward) *before* building meta-labels. (2) **Class imbalance from carry.** If the primary is "long high spread" and HY drifts up on carry, the primary is right about 70% of the time *(illustrative)* and "always bet" has 70% accuracy. Report $F_1$, the Brier score, and the IDO-stripped PnL, never raw accuracy. (3) **Feeding the primary's score as a feature without normalizing it.** A PRS distribution that drifts as documents get looser (2020–2026 saw exactly this, Chapter 13) is a non-stationary feature; rank-transform it within each date.

**Quant-shop life: Model Review Tuesday.** *A systematic asset manager. A fictional composite: the firm, the people, and every number are invented and illustrative; the quoted guidance is real.*

At a systematic credit manager in a converted warehouse across the river from Theo's desk, Tuesday is model review day, and model review day begins with the mapping table.

The table has no glamorous name. In the code it is `issuer_parent_map`, and it has four columns that matter: a bond's issuer code, the ultimate parent the firm assigns it to, the date the assignment took effect, and the initials of whoever made it. It holds about 9,000 rows. In a normal week perhaps a dozen of them change. Ana, a data analyst two years into the job, owns it, which in practice means she is the person who gets the email when it is wrong.

This Tuesday's first email arrived at 7:52 from the corporate-actions feed. A software company in the high-yield universe had formed a new subsidiary, designated it unrestricted under its credit agreement, and transferred a package of intellectual property into it. The new entity had issued nothing yet. The feed had nevertheless created an issuer code for it, because the 8-K mentioned a financing commitment and the vendor's rule was to create a code on first mention. A new code with no parent maps, by default, to itself.

Ana's question was one Theo would have recognized from a hundred creditor-committee calls: does this entity belong to the parent's group or not? The answer lives in the credit agreement, not in the feed. An unrestricted subsidiary sits outside the covenant group by design; that is the point of designating it. But the parent owns it, its value came out of the parent's assets, and if it ever issues debt, that debt will move with the parent's fortunes in exactly the way that matters to a cross-validation fold. She spent the morning on it: the 8-K, the agreement's definition of "Unrestricted Subsidiary," the investment basket that had permitted the transfer, and a twenty-minute call with the firm's one former leveraged-finance lawyer, who confirmed that the IP was the parent's best collateral and that the lenders who had not been consulted were, in her phrase, about to be. Ana mapped the new code to the parent, effective on the transfer date, and wrote a two-line rationale in the change log. Under the firm's model governance policy the change was a ticket, reviewed by a second person and logged. The firm is not a bank, but it had copied its policy almost line for line from the Federal Reserve's SR 11-7 guidance after its largest allocator asked to see one, and that guidance calls for "change control procedures" under which "all changes are logged and can be audited" (SR 11-7, p.12).

At two o'clock the model risk committee met: five people, one screen, and a deck of twenty-two slides, of which the committee looked at one. The headline number on it, the effective number of independent issuers in the training panel (the $N_{\text{eff}}$ of §7.6), had fallen from 412 to 398 since last month. The bond count had risen by 140.

"Why is this number different from last month?" the chair asked. It is the only question model risk committees ever really ask, and it is the right one.

The modeler presenting did not know. Ana did. Two issuers in the panel had merged in September. The acquirer had assumed the target's bonds, and on the closing date she had remapped every one of the target's CUSIPs to the acquirer's parent id, so two parents had become one. The new bonds in the panel were mostly additional maturities of issuers already in it, which add rows without adding much independent evidence. More bonds, fewer hats, and the effective count fell.

The chair nodded, asked for the explanation to go into the deck's notes, and moved on to the next item, which was why the vendor's evaluated price for a utility bond had not changed in nine days. The meeting ran forty minutes. Nothing in it was interesting. All of it mattered.

The mapping table is the grouping key for the cross-validation of §7.7: every bond with the same parent id goes into the same fold, so that the model is never tested on a company it has already met in training. Had the new unrestricted subsidiary kept its default self-mapping, its first bond would one day have appeared as a "new issuer" in a test fold while its parent's bonds sat in the training set, and the model would have been graded on predicting a company it had in fact studied. No one on the modeling team could have caught that by reading code, because the code was correct. The only person able to audit the grouping key was a person who had read the credit agreement. That is the meta-labeling idea in its humblest form: the analyst's legal read is not decoration on the machine, it is an input the machine cannot produce for itself.

## 7.6 Sample Weights: Uniqueness and the Forty-Seven-Hat Problem

Return to the cold open. Kaz's 212,000 bond-months were not 212,000 pieces of evidence, for two separate reasons. *Time overlap:* if a label is formed every day with a 13-week vertical barrier, each label shares most of its window with the 60-odd labels on either side of it. *Sibling overlap:* if an issuer has eleven bonds, eleven labels formed on the same day mostly record the same issuer news at eleven durations. Both inflate the count; neither adds information. The fix is to weight each label by how much of its window it shares with no one else.

> **Math, Gently.** *Hats, not rows.* At a shareholder meeting, eleven people wearing the same company's badge do not get eleven votes on a motion about their own company; they are one interest, however many chairs they fill. A **weighted sample** applies the same courtesy to data: each observation counts in proportion to its weight, so eleven near-copies of one fact can share a single vote between them. When the weights are unequal, the **Kish effective sample size**, $(\sum w_i)^2/\sum w_i^2$, says how many equally weighted observations the sample is worth. Tiny number: two rows with weights 1 and 0.1 give $(1.1)^2/(1 + 0.01) = 1.21/1.01 \approx 1.2$: two rows, one and a fifth observations. The definitions that make this exact for overlapping credit labels follow.

**Uniqueness, defined.** For label $i$ with interval $[t_{0,i}, t_{1,i}]$ on bond $b(i)$ of ultimate parent $g(i)$, define the *issuer concurrency* at date $t$ as the number of labels on any bond of the same parent that are live at $t$:

$$
c^{\text{iss}}_{g,t} \;=\; \sum_{j\,:\,g(j) = g} \mathbf 1\{t_{0,j} \le t \le t_{1,j}\}.
$$

The *average uniqueness* of label $i$ is the average, over its own window, of the share of the issuer's live labels it represents:

$$
\bar u_i \;=\; \frac{1}{t_{1,i} - t_{0,i} + 1}\sum_{t = t_{0,i}}^{t_{1,i}} \frac{1}{c^{\text{iss}}_{g(i),t}} \;\in\; (0, 1].
$$

Counting concurrency within the parent, rather than across the whole universe, is the credit-specific choice. López de Prado's original definition counts every concurrent label in a single series. In a cross-section, two labels from *different* issuers on the same day are not duplicates: they carry different idiosyncratic news, and their shared market component is handled by the cross-validation purge in §7.7. Two labels from the *same* parent on overlapping windows are duplicates in the sense that matters, because the default, the LMT, and most of the idiosyncratic spread variance are parent-level events. Counting within the parent therefore corrects for both time overlap (the same bond's neighboring labels) and sibling overlap (the other bonds) in one formula.

**The hat count.** The sum of uniquenesses, $N_{\text{eff}} = \sum_i \bar u_i$, is approximately the number of non-overlapping issuer-windows in the data. Check it on the simplest case: one issuer with $B$ bonds, daily labels for $T$ days, horizon $h$. Concurrency is about $Bh$ in the interior, so each label has $\bar u_i \approx 1/(Bh)$, and $N_{\text{eff}} \approx BT \cdot 1/(Bh) = T/h$, independent of $B$. Eleven bonds, one hat. Now scale up *(illustrative)*: 800 parents, about three bonds each, 20 years of daily labels ($T \approx 5{,}000$ trading days) with $h = 63$ days gives about 12 million label rows, roughly 576,000 bond-months, and

$$
N_{\text{eff}} \;\approx\; 800 \times \frac{5{,}000}{63} \;\approx\; 63{,}000.
$$

That is about one-ninth of the bond-month count and one two-hundredth of the label count. And it is still an *upper bound* on the independent evidence for any conclusion that depends on the market regime, because all 800 issuers live through the same 79 non-overlapping 13-week windows. A model that times high yield as a whole has about 79 observations, not 63,000. That is why this book prints $N_{\text{eff}}$ next to every backtest result, and why, if ROBO is told only one thing in this chapter, it is told that.

**From uniqueness to weights.** The uniqueness goes into the loss function as a sample weight: each label's contribution is multiplied by $\bar u_i$, so that duplicated labels share one unit of influence between them. Nobody on the desk argued about that part. The argument was about the two refinements the literature calls standard, and it happened on a Wednesday afternoon across Kaz's second monitor.

"Time decay," Kaz said. "Down-weight old labels, linearly or exponentially. It's a crude but honest admission that the 2005 market is not the 2026 market."

Theo scrolled to a label formed in the spring of 2005, a single-B industrial whose indenture had debt and restricted-payment baskets tighter than anything he had seen in a new-issue document in years. "Does this deserve a vote in 2026?" he asked, and then answered himself before Kaz could. "Less of one. The documents it was written under don't exist anymore. But if you decay hard enough to make 2005 irrelevant, you'll make 2008 irrelevant too, and 2008 is the only time in the sample the whole asset class fell through the trapdoor at once." They settled on a slow decay and a standing check, the model's behavior on a 2008 hold-out printed beside every refit, so that forgetting would at least be visible.

"Return attribution," Kaz went on. The refinement multiplies each label's weight by the absolute residual return it earned, attributed by concurrency, $\big|\sum_{t} r^{\text{xs}}_{i,t}/c^{\text{iss}}_{g(i),t}\big|$, so that windows in which something happened count more than windows in which nothing did. "The quiet months are mostly noise. Weight the months where the bond actually moved."

"In credit," said Mags, without turning around, "the months where the bond actually moved are defaults. Weight by the size of the move and you'll have a model trained on twelve bankruptcies and a lot of footnotes. It'll be a default memoir. Very moving. Useless on a Tuesday." She was right about the mechanism, and Kaz conceded it: a few default jumps can dominate return-attribution weights, which is why the refinement is used with care in credit, capped or applied to labels inside a rating bucket rather than across the whole panel.

Whatever the desk chose, the bookkeeping afterwards was the same. The weights were rescaled to sum to the number of labels, so that regularization strengths tuned on unweighted data kept their meaning, and whenever they were unequal, Kish's effective size from the box above went on the slide beside $N_{\text{eff}}$.

> **Math, Gently.** *What a bootstrap is.* A bootstrap resamples your own data, with replacement, many times over, recomputes the answer on each resample, and reads how much the answer wobbles; the wobble stands in for the uncertainty you would see if history could be rerun. Tiny number: resample 100 monthly returns 1,000 times and the resampled Sharpe ratios might run from 0.3 to 1.1 around a reported 0.7 *(illustrative)*, which says the 0.7 is a neighborhood, not a point. The trick works only when the resampled pieces are close to independent, which is exactly what overlapping credit labels are not.

**The sequential bootstrap, sketched.** Bagging over overlapping labels has the same disease: a bootstrap sample drawn uniformly is full of near-duplicates, so the bagged trees are more correlated than they look. The sequential bootstrap draws labels one at a time, each with probability proportional to its average uniqueness *given the labels already drawn*, so the sample spreads itself across distinct windows. In a credit panel, run it within parent groups (draw parents first, then labels within a parent), which is the block bootstrap the RSSG reader would have invented anyway: you would never test a recovery model by resampling the same company's eleven bonds as eleven independent bankruptcies.

Before the Wednesday argument broke up, Theo asked the question a banker asks of any new process: was it worth the run time? Kaz answered with a multiplication on the corner of the whiteboard, the horizon in label-formation steps times the average number of bonds per parent. Daily labels with a 63-day horizon on issuers with three bonds each came to an overlap of about 190, and at that ratio an unweighted model trains mostly on copies, which describes almost every high-yield panel anyone builds. Monthly labels with a one-month horizon and one bond per issuer came to about one: every $\bar u_i$ sits near 1, the weights change nothing but the run time, and the only thing worth keeping is the $N_{\text{eff}}$ printout that proves it.

Mags, still with her back to them, supplied the case the formula cannot see. "Late 2015," she said. "Dozens of energy names. Dozens of parents, one oil price. Your weights give every one of them its own hat." Kaz conceded that too. Concurrency counted within the parent does not notice parents that share one driver, and the purge in §7.7 removes only the shared market component, so $N_{\text{eff}}$ overstates the evidence for any conclusion that is really about a sector, just as it does for any conclusion about the market as a whole.

## 7.7 Cross-Validation That Cannot Peek: Purged, Embargoed, Issuer-Grouped

*A desk scene: the bond, the label, the folds and the 1.8 are illustrative.*

Kaz's in-sample Sharpe of 2.9 had a cousin, and Kaz brought it to Theo's desk the morning after the hat count, the way a patient brings a second opinion to a doctor who did not like the first. It was a cross-validated Sharpe of 1.8 from shuffled K-fold.

"This is the conservative number," Kaz said. "Five folds. Every label is scored by a model that never saw it. Out of sample, every one."

Theo had learned to distrust the word "every" the way he distrusted "including without limitation." "Pick one test label," he said. "Any one."

Kaz picked one: a 13-week label on a single-B chemicals bond, formed on a Tuesday in March 2017. "Fold three. Scored by a model trained on folds one, two, four, and five."

"What day was it formed?"

"Tuesday the fourteenth."

"And the label on the same bond formed on Monday the thirteenth. Which fold is that in?"

Kaz looked. "Fold one. Training."

"Wednesday the fifteenth?"

"Fold four. Training." A pause. "Thursday's in fold two."

"So the model learned this bond's next thirteen weeks from Monday's label, which covers all of Tuesday's window except one day, and from Wednesday's, which covers all of it except one day at the other end. Then you asked it to predict Tuesday."

Kaz scrolled through the fold assignments of the label's neighbors, then the neighbors' neighbors, then a sibling bond from the same issuer whose labels from that week were scattered across the training folds as well, and said, quietly and to their very great credit, "Oh."

The leakage is mechanical, not subtle, and it is fatal in credit, where labels are long and issuers repeat. The 1.8 was not the conservative number. It was a measurement of how well the model could remember.

> **Math, Gently.** *What K-fold does, and why shuffling is cheating here.* Cross-validation estimates how a model will do on data it has not seen by hiding part of the data you have. **K-fold** cuts the sample into $K$ pieces, trains on $K - 1$ of them, tests on the one held out, and rotates until every piece has served as the test once. Shuffling the rows before cutting is harmless, even wise, when each row is an independent draw. Credit labels are not independent draws. Shuffling them is like grading a student on an exam whose questions were photocopied from yesterday's homework: the score is real, and what it measures is memory. Tiny number: with daily labels and a 63-day horizon, every test label shares part of its window with 124 other labels on the same bond, 62 formed on the days before it and 62 after. Shuffled five-fold puts about four in five of them, roughly 100, into training, and the nearest overlap the test label's window on all but a day or two. Add two sibling bonds from the same parent and the count triples. The cure, below, is to stop cutting by row and start cutting by time and by company.

The credit-risk modeling tradition knew a version of this decades before machine learning arrived on bond desks.

> **[SOURCE EXTRACTION]** *Bohn_Stein_Active_Credit_Portfolio_Management p.465:* "Finally, the most robust procedure is shown in the lower right quadrant and should be the preferred sampling method for credit risk models. In addition to being segmented in time, the data are also segmented across the population of obligors."
>
> **Annotation.** Bohn and Stein's validation figure is a two-by-two grid: split by time or not, split by obligor or not. Their preferred quadrant splits both ways at once, so no obligor in the test set was seen in training and no test date precedes the training window. That is purged, issuer-grouped cross-validation, described for default models before the term existed. What the modern desk adds is precision about *where* the split sits. Labels have duration, so a time split must remove training labels whose windows overlap the test window (the purge), plus a buffer after the test window (the embargo). Issuers have org charts, so the obligor split must group at the ultimate parent, not at the ticker. The quadrant was right; the boundaries need to be drawn in label time and in corporate-family space.

**The purge, formally.** Let the test fold be the set of labels $\mathcal T$, spanning label time $[T_0, T_1]$ with $T_0 = \min_{i \in \mathcal T} t_{0,i}$ and $T_1 = \max_{i \in \mathcal T} t_{1,i}$. A training label $j$ is purged if its interval overlaps the test span:

$$
t_{0,j} \le T_1 \quad\text{and}\quad t_{1,j} \ge T_0.
$$

**The embargo.** Even after purging, features computed from trailing windows leak forward: a 12-month momentum feature for a training label formed just after $T_1$ is built from prices *inside* the test window. So also drop training labels with $t_{0,j} \in (T_1, T_1 + \eta]$, where $\eta$ is at least the longest feature lookback that touches price data. The textbook default is $\eta \approx 1\%$ of the sample length. In credit, set $\eta$ to the maximum of that and the feature lookback, which usually makes it months, not days. Mags, on the embargo: "So the model isn't allowed to call the bond desk for a month after the test. Fine. Neither were we, after Enron."

**The group.** Assign every label to a fold by ultimate parent, so no parent appears on both sides. Grouping removes *issuer-specific* leakage: the model cannot learn in training that this particular company defaulted in 2021 and then "predict" its 2019 deterioration in the test. Grouping does *not* remove *time* leakage through the common factor, because other issuers' labels from the same weeks still carry the market move. Purging does not remove issuer leakage, because a parent's labels from other years still identify the parent. Neither split does the other's job. The resulting scheme is a two-way split: the test set is (parents in group $G_k$) during (time block $B_m$); the training set is (parents not in $G_k$) during (times outside $B_m$, purged and embargoed). As a picture, draw time blocks running left to right and parent groups stacked top to bottom. The test fold is one cell of that grid: one group of parents during one block of time. Training is every cell that shares neither its row nor its column, minus a hatched strip on either side of the test column where training labels' windows reach into the test span (the purge) and a further band after it, as wide as the longest feature lookback, which for a fractionally differentiated feature can be the 280 days of §7.3 (the embargo). Everything else in the test cell's row and column is set aside, and that is where the cost comes from. With $K$ parent groups and $M$ time blocks, each test fold trains on roughly $(1 - 1/K)(1 - 1/M)$ of the data, less the purge. That is expensive. It is also the true price of an honest estimate, and it is cheaper than finding out in production.

**Group by parent, not ticker, especially in the LMT era.** The interesting bonds of 2016–2026 often live in entities created to receive assets: the unrestricted subsidiary that received J.Crew's intellectual property, the new-money super-priority tranche issued through a fresh financing SPV, the HoldCo and OpCo notes of the same family. A ticker-level grouping sends the drop-down entity to the training fold and the parent to the test fold, and the model learns the parent's fate from the child's price. The grouping key is the corporate-family tree from the security master (Chapter 27), and the RSSG reader is the person on the desk best qualified to audit it. Theo's two HoldCo/OpCo pairs from the night of the review were exactly this case. Under the desk's ticker grouping, one holding company's notes sat in fold two and its operating company's in fold four, and when he asked who maintained the mapping from ticker to parent, the answer was a vendor file that nobody had reconciled in years. The *ultimate parent?* he had underlined on the term sheet turned out to be the grouping key for the entire test.

**Walk-forward is the special case you already trust.**

> **[SOURCE EXTRACTION]** *Bohn_Stein_Active_Credit_Portfolio_Management p.467:* "Fit the model using all the data available on or before the selected year. Once the model's form and parameters are established for the selected time period, generate the model outputs for all the firms available during the following year"
>
> **Annotation.** This is walk-forward testing, step two and step three of Bohn and Stein's recipe: fit through year $y$, predict year $y+1$, roll. It is a purged CV in which the folds are ordered and the embargo is implicit (nothing after the training window is ever used), and it emulates how the model will actually be run. Its weakness is that it produces *one* backtest path, so its performance estimate has the variance of a single history, and the early folds train on very little data. Combinatorial purged cross-validation (CPCV) generalizes it: split the time axis into $N$ blocks, choose every combination of $k$ blocks as the test set, purge and embargo around each, and stitch the test predictions into $\binom{N}{k}\,k/N$ distinct backtest paths. For $N = 6$ and $k = 2$ that is 15 splits and 5 paths, enough to see a *distribution* of Sharpe ratios rather than one lucky number. Run walk-forward as the production rehearsal and CPCV as the research diagnostic, and keep the parent grouping in both.

And then there is the footnote that every credit modeler should have taped to the monitor, right below the issuer count.

> **[SOURCE EXTRACTION]** *Bohn_Stein_Active_Credit_Portfolio_Management p.466:* "It can be argued that there is no truly honest out-of-sample test since most modelers use portions of the data to test early models as they converge on a functional form for the model."
>
> **Annotation.** Footnote 31 is the bridge from cross-validation to multiple testing. Purging and grouping protect a *single* model evaluation from leakage. They do nothing about the fact that the modeler evaluated forty versions, looked at the test results each time, and kept the best. Each glance at the test fold turns it, a little, into training data. That is the 2019–2026 bond-factor story in one sentence, and it is why the next section exists. The practical response is to log every evaluation (the trial count $N$ in §7.8 is a number you *record*, not one you estimate afterwards) and to lock away a final hold-out period that no one is allowed to look at until the research is frozen.

> **Ways This Blows Up.** *Four ways a purged CV still leaks.* (1) Purging on calendar months while labels are event-timed: a label that closed early at a barrier has a shorter interval, and one that closed late (a stale mark held it open) has a longer one. Purge on the recorded $t_{1,i}$, not on the nominal horizon. (2) Forgetting that fractional differentiation (§7.3) has a window of up to $K \approx 280$ days, which is a feature lookback and therefore sets the embargo. (3) Hyperparameter search *outside* the CV loop: choosing the tree depth on the full sample and then cross-validating the chosen depth. Nest the search inside each training fold. (4) Cross-sectional standardization (z-scoring features by date) is safe; *global* standardization with full-sample means and standard deviations is a small look-ahead that compounds with everything else.

#### What no split can catch

Of the three schemes, purged, embargoed, parent-grouped K-fold is the everyday tool for model *selection* (feature sets, tree depths, label horizons), where the ranking of the alternatives matters more than the level of any one of them and using every observation in every role is worth more than honoring the arrow of time inside the training folds; walk-forward and CPCV keep the jobs the Bohn and Stein annotation gives them. All three fail when the leak is longer than the guard or the tuning happens outside the loop, which is the box above. And none of them can catch a leak that sits upstream of the data. In the four-factor replay, a flawless purged, embargoed, parent-grouped cross-validation run on the published file would have reported, faithfully and with excellent hygiene, the premium of a misdated series. The purge protects you from your own pipeline. It cannot audit somebody else's.

Kaz ran the purged, parent-grouped version of the 1.8 that afternoon, beside the shuffled one, because the gap between the two costs a single extra run and measures how much of the original result was remembering. The answer is on the screen in the Desk Debrief, and §7.12 runs the same demonstration on synthetic data.

## 7.8 Multiple Testing and the Deflated Sharpe Ratio

Purging makes one evaluation honest. It does not make the *best of many* evaluations honest. Kaz tried about 3,000 configurations, so the right question about the winner is Ines's: how good would the best of 3,000 hands look if every hand were dealt at random?

> **Poker Table.** "The deflated Sharpe ratio asks the only question that matters about a guy showing you his winning hands: how many did he fold first? And the embargo is the dealer burning a card. You don't get to see the card right after the one you bet on, because that card is correlated with yours."

> **Math, Gently.** *The expected maximum of noise, or the tallest of a hundred strangers.* Line up a hundred strangers chosen at random and the tallest of them will be strikingly tall, for a reason that has nothing to do with basketball: you looked at a hundred people and kept the extreme one. Backtests work the same way. Give a hundred strategies a true Sharpe of exactly zero, let each one's measured Sharpe wobble by its standard error, and pick the best. The winner's measured Sharpe is not zero. It sits about 2.5 standard errors above zero, because that is where the tallest of a hundred draws from a bell curve typically lands. Tiny number: over five years of months the standard error of a monthly Sharpe near zero is about $1/\sqrt{60} \approx 0.13$, so the best of a hundred noise strategies shows about $0.13 \times 2.5 \approx 0.32$ a month, a little over 1 annualized, with nothing inside it. The bar rises with the size of the search, slowly but without limit, roughly with the square root of the logarithm of the number of tries. Kaz's 3,000 push the multiplier from 2.5 to about 3.6, and the Full Derivation at the end of this section, Euler–Mascheroni constant and all, turns that into the bar Kaz's winner has to clear.

**What the deflated Sharpe ratio does, in words.** The probabilistic Sharpe ratio turns a measured Sharpe into a probability: given how long the track record is and how lopsided and fat-tailed the returns are, how likely is it that the true Sharpe beats some benchmark? Lopsided and fat-tailed are skewness and kurtosis, the shape numbers of Chapter 5 (§5.1); monthly high-yield returns have a long porch built out on the left and a thick rim, and both widen the wobble of a Sharpe estimate. Against a benchmark of zero, Kaz's winner looks overwhelming. The *deflated* Sharpe ratio changes one input. It sets the benchmark not at zero but at the expected best of 3,000 noise strategies, the bar the grid would have cleared with no skill at all, and asks the same question. The answer is a coin flip. Nothing about the winner changed; only the honesty of the comparison did. The arithmetic, with the minimum track record length and the probability of backtest overfitting that travel with the deflated ratio in this book's reports, is in the Full Derivation at the end of this section.

**Thresholds from the literature.** Harvey, Liu, and Zhu (*Review of Financial Studies*, 2016) catalogued 316 equity factors and argued that a new factor should clear $t > 3.0$, not 2.0. Chordia, Goyal, and Saretto (*RFS*, 2020), using more than two million random strategies, put the bar near $t \approx 3.8$ for time-series tests and $3.4$ for cross-sectional ones. The 2026 bond audit used Benjamini–Hochberg false-discovery control and found that 6% of specifications survive (§7.2). Paleologo frames the same discipline for the PM seat:

> **[SOURCE EXTRACTION]** *Paleologo_Advanced_Portfolio_Management p.159:* "there are ways to assign a "Sharpe haircut" to a backtested strategy. This is a quantitative topic and you could work with a quantitative analyst to establish some selection principle"
>
> **Annotation.** The surrounding page draws the line that matters: a *confirmatory* test (you believe a specific dataset improves a specific estimate, so you add it and check) versus an *exploratory* search (you try many combinations and keep the best). Confirmatory tests deserve something close to their nominal $t$-statistic; exploratory searches deserve a haircut that grows with the number of trials, and the deflated Sharpe ratio is one explicit form of that haircut. For the ex-RSSG reader, this is the most transferable idea in the chapter: a covenant-driven primary model (§7.5) is confirmatory by nature, because the hypothesis ("loose open-market-purchase language predicts uptier losses") was written down before the data was touched, while a gradient-boosted search over 81 features is exploratory by nature, and this desk reports the two differently. Where the modern desk goes further: the trial count $N$ must include *every* configuration evaluated, by anyone on the team, on the same data, and correlated trials should be collapsed by clustering the trial-return correlation matrix into an effective number of independent trials, so that 400 near-identical momentum variants count as a handful, not as 400.

> **Ways This Blows Up.** *Your Sharpe is inflated before you deflate it.* Smoothed marks lower measured volatility (§7.1), so a backtest on evaluated prices overstates $\widehat{SR}$, and positive autocorrelation from staleness means the usual $\sqrt{12}$ annualization overstates it again (the variance of a sum of positively autocorrelated returns exceeds the sum of variances). Unsmooth returns first, or compute Sharpe from executable prices only, and use an autocorrelation-adjusted annualization. Deflation corrects for *search*; it cannot correct for a numerator and denominator that were both measured on rumors.

Kaz's 3,000 were one search. A multi-strategy platform runs a larger one, and its trials have names.

> **View From Another Seat.** *The multi-strategy pod's risk desk.* One level up, a multi-strategy platform faces Kaz's problem in a different suit. It hires many portfolio managers, gives each a book, keeps the ones whose results are good, and must then decide whether the survivors' track records are skill or the expected maximum of a large, noisy search. Giuseppe Paleologo, formerly head of enterprise risk at Millennium and director of risk and quantitative analysis at Citadel (per Bloomberg's show notes), described the platform model on *Odd Lots* ("How to Succeed at Multi-Strategy Hedge Funds," 20 May 2024) in roughly these terms (paraphrased here, not quoted): the platform watches each PM's performance from very close up, adds capital to those who perform and takes it away from those who do not, and treats stop-losses as a crude insurance policy on each PM's left tail. From that seat, Kaz's slide reads differently (the reading is this book's, not the guest's). The risk desk would barely look at the 2.9. It would ask instead for the trial count, and not only Kaz's 3,000 configurations: every version of this idea the platform has already funded and defunded, because the platform itself is a search, and its survivors are deflated by its own hiring history. And it would ask whether the residual the PM proposes to lever is really residual: whether, once market, rates, sector, and carry have been stripped out, anything is left that the risk desk has not already seen in twenty other books. IDO or it didn't happen, enforced by the people who allocate the capital. The stop-loss, in this light, is an out-of-sample test that runs in real time, and it is the one test in the building that nobody can rerun with a different random seed.

#### The Full Derivation: PSR, DSR, MinTRL and PBO

**The expected maximum of noise.** Suppose $N$ strategies have true Sharpe zero and their estimated Sharpe ratios are roughly normal with variance $V = \operatorname{Var}[\widehat{SR}_n]$ across trials. Extreme-value theory gives the expected maximum (Bailey and López de Prado, *The Deflated Sharpe Ratio*, 2014; the bound is the "false strategy theorem" of their 2021 paper):

$$
SR^\ast \;=\; \mathbb{E}\Big[\max_n \widehat{SR}_n\Big] \;\approx\; \sqrt{V}\,\Big[(1-\gamma)\,\Phi^{-1}\!\Big(1 - \tfrac1N\Big) + \gamma\,\Phi^{-1}\!\Big(1 - \tfrac{1}{N e}\Big)\Big],
$$

where $\gamma \approx 0.5772$ is the Euler–Mascheroni constant and $e$ is Euler's number. Put in Kaz's numbers *(illustrative)*: $N = 3{,}000$ trials on $T = 240$ months gives $V \approx 1/T$ for monthly Sharpe ratios near zero, so $\sqrt V \approx 0.065$. The quantiles are $\Phi^{-1}(1 - 1/3000) \approx 3.40$ and $\Phi^{-1}(1 - 1/8155) \approx 3.67$, so

$$
SR^\ast \approx 0.065 \times (0.423 \times 3.40 + 0.577 \times 3.67) \approx 0.065 \times 3.56 \approx 0.23 \text{ per month} \approx 0.80 \text{ annualized}.
$$

The best of 3,000 *pure-noise* strategies over 20 years shows an annualized Sharpe of about 0.8. That is the bar *before* the model has done anything, and it is the number Ines was asking for when she asked how many hands Kaz had folded.

**The probabilistic and deflated Sharpe ratios.** With $T$ observations, sample Sharpe $\widehat{SR}$ (per period), sample skewness $\hat\gamma_3$, and sample kurtosis $\hat\gamma_4$ (not excess), the probability that the true Sharpe exceeds a benchmark $SR_0$ is

$$
\widehat{\text{PSR}}(SR_0) \;=\; \Phi\!\left[\frac{(\widehat{SR} - SR_0)\sqrt{T-1}}{\sqrt{1 - \hat\gamma_3\,\widehat{SR} + \frac{\hat\gamma_4 - 1}{4}\,\widehat{SR}^2}}\right].
$$

The denominator is the standard error of a Sharpe estimate under non-normal returns: negative skew ($\hat\gamma_3 < 0$) and fat tails ($\hat\gamma_4 > 3$) both widen it, and monthly high-yield excess returns have both. The *deflated* Sharpe ratio sets the benchmark to the noise maximum, $\widehat{\text{DSR}} = \widehat{\text{PSR}}(SR^\ast)$. Run Kaz's winner through it: with $\widehat{SR} = 0.23$, $T = 240$, $\hat\gamma_3 = -0.5$, $\hat\gamma_4 = 5$ *(illustrative)*, the denominator is $\sqrt{1 + 0.115 + 0.053} \approx 1.08$ and $\widehat{\text{PSR}}(0) = \Phi(0.23 \times 15.5 / 1.08) = \Phi(3.3) \approx 0.9995$. A naive report says 99.95% confident. The deflated ratio, with $SR_0 = SR^\ast = 0.23$, is $\Phi(0) = 0.5$: a coin flip. The best noise strategy is, by construction, about as good as the expected best noise strategy.

Two companion statistics belong in every report. The **minimum track record length** is the number of periods needed for $\widehat{\text{PSR}}(SR_0)$ to reach confidence $1-\alpha$:

$$
T^\ast = 1 + \Big[1 - \hat\gamma_3\,\widehat{SR} + \tfrac{\hat\gamma_4 - 1}{4}\,\widehat{SR}^2\Big]\left(\frac{z_{1-\alpha}}{\widehat{SR} - SR_0}\right)^2.
$$

The **probability of backtest overfitting** (PBO; Bailey, Borwein, López de Prado, and Zhu 2017) uses combinatorially symmetric cross-validation (CSCV). Split the $T \times N$ matrix of trial returns into $S$ time blocks. For each of the $\binom{S}{S/2}$ ways to choose half the blocks as "in-sample," find the in-sample best trial $n^\ast$, compute its relative rank $\bar\omega \in (0,1)$ among all trials out of sample, and take the logit $\ell = \log\big(\bar\omega/(1-\bar\omega)\big)$, the log of the odds that Chapter 5 (§5.5) uses to stretch a share onto the whole real line: a share of one-half has a logit of 0, a share of 0.8 about 1.39. PBO is the share of splits with $\ell \le 0$: how often the in-sample winner is below median out of sample. Noise gives PBO near 0.5. Skill gives PBO near 0.

## 7.9 The Two Biases That Built the Bond-Factor Zoo

**Long Scene 2: The Reversal That Was a Bid–Ask Spread.** *The desk, its sleeve, its P&L, and every number attributed to the desk are fictional and illustrative. The paper, its numbers, and its dates are on the public record (Dickerson, Robotti, and Rossetti 2026, arXiv:2604.07880).*

Kaz's contribution to this section came on a Tuesday. Kaz had found the TRACE field `As Of Indicator`, seen that a value of `R` means "reversal," and spent the morning building a short-term-reversal factor out of trade cancellations. Theo had to explain that in FINRA's historic TRACE layout, a reversal is the cancellation of a trade reported more than 20 business days earlier, which is a data-cleaning event, and that a reversal *factor* is a different thing. Both, he added, would ruin your month. Then he realized the joke had a serious point, because the second kind of reversal had been built out of something almost as accidental as the first.

That evening Ines sent Theo a PDF with no message, which on this desk is a message. It was the 2026 audit from the Trend Watch box in §7.2, the paper Dickerson, Robotti, and Rossetti had posted to arXiv on 9 April 2026 as "The Corporate Bond Factor Replication Crisis," and it had been sitting in her reading folder since the spring. Theo read the abstract on the train home and the tables on the train in. By the time he reached his desk he had circled one row of Table 1, the row for short-term reversal, and drawn an arrow from it to a sticky note that said *Kaz's sleeve?*

Kaz's sleeve was the desk's one live experiment with a price-based signal. It bought the high-yield bonds whose prices had fallen most over the previous month, sold the ones that had risen most, rebalanced at month-end, and had been in paper trading since July. It was up. Not by a lot, but up in every month but one, which on a desk that had spent a year arguing about whether anything worked made it something of a celebrity. Kaz kept the cumulative paper P&L as a chart on the second monitor, the way some people keep a photograph of their children.

**Round one.** "It doesn't apply," Kaz said, before Theo had finished the question. "That paper is about backtests. My sleeve's been running since July on a model frozen in June. Paper P&L is out of sample by definition. Nobody can overfit the future."

It was, again, a good argument, and Theo did not have an answer to it. Ines did, and it was a question.

"What price is the paper P&L marked at?"

"The end-of-day evaluated price. Same vendor as the backtest, so the numbers are comparable."

"And the signal? Last month's return, measured from what price?"

"The month-end evaluated price." Kaz stopped.

"So your out-of-sample test," Ines said, "was run on the same rumor as your in-sample test. The future isn't the problem. The price is. If the month-end mark on a loser is too low, the backtest buys it at too low a price and sells it a month later at a fair one, and so does your paper trade, because your paper trade is a backtest that runs at the speed of a calendar. The only thing out of sample is the date."

Theo, who had once watched a sponsor's model "validate" its projections against the sponsor's own management accounts, recognized the shape of it. A test is independent of the thing it tests only when it is measured with a different ruler.

**Round two.** The whiteboard came out after lunch, and Theo did the arithmetic, because he had circled the row and felt it was his to defend. He used the paper's own toy example, with its numbers, turned into a reversal trade. Two bonds, he wrote, with true returns of exactly zero this month and next. Bond A's month-end price is recorded half a percent too low, and bond B's half a percent too high. Last month A therefore shows a return of $-0.5\%$ and B a return of $+0.5\%$: A is a loser and B a winner, though nothing happened to either. The reversal strategy buys A and sells B. Next month the prices are drawn fresh, without the error, so A shows $+0.5\%$ as its mark returns to fair value and B shows $-0.5\%$. The long-short return is $+1.00\%$, against a true return of zero.

"A point a month," Theo said, "out of noise of half a point. And the noise doesn't have to be large, or biased, or anybody's mistake. It just has to be in both places: in the price you sort on and in the price your return starts from."

Kaz did not argue the arithmetic. Kaz argued the size. "Half a point of noise is a lot for a month-end mark."

"For a BBB that trades every day, maybe. For a single-B that last printed nine days ago in a two-hundred-thousand-dollar lot, half a point is a polite estimate."

Then they put up the paper's numbers. Built the textbook way, with month-end prices in both the signal and the return, corporate-bond short-term reversal earned $-0.99\%$ a month with a $t$-statistic of $-4.46$ over 2002–2024, one of the strongest results in the zoo. (The sign is the paper's convention, recent winners minus recent losers; Kaz's sleeve, long the losers, owned the mirror image.) Built with a signal gap, so that the signal was read from a price observed one to ten business days before the month-end price the return starts from, it earned $-0.09\%$, with a $t$ of $-0.51$; starting the return from a month-begin price instead, about a business day into the next month, left $-0.17\%$. A dollar in the unadjusted version, invested at the start of the 2002 sample, would have grown to about \$12 by the end of 2024. Adjusted, it grew to between \$1.10 and \$1.40, depending on the adjustment.

"Minus ninety-nine to minus nine," Kaz said. "That's ninety-one percent of it." And then, after a while: "A few days. A few days of separation between the price you sort on and the price you start from, and ninety-one percent goes away."

"It isn't about the days," Theo said. "It's about the draw. Month-end's mark and a mark from a few days earlier are two different guesses. As long as you sort on one and start from the other, the guesser's error can't pay you."

**Round three.** Mags had listened to both rounds without turning her chair. Now she turned it.

"Back in my day," she said, "you could trade short-term reversal any time you liked. You picked up the phone. You said, I'll buy the bond that's down two points this month. The dealer said, sure, here's my offer, and the offer was a point and a half above where it last printed, because the last print was some small account selling to him at his bid. You bought it. You were very pleased with your reversal. It was called the bid–ask spread, and you were on the wrong side of it." She turned the chair back. "It's nice that it has a paper now."

Ines said that was the hand history, that she would write it up properly for the file (it is Case Study C in §7.11), and that in the meantime the question was what to do about the sleeve.

**Coda.** Kaz stayed late. The sleeve had a second component nobody had looked at in months: before ranking bonds on last month's return, the pipeline winsorized returns at the 0.5th and 99.5th percentiles, to protect against data errors. Kaz opened the configuration file to see how the percentiles were computed. They were computed once, over the full sample, 2002 to 2025. The filter meant to protect the backtest from bad prints had been told, by construction, which months were going to be extreme.

That is the second bias of this section, and the audit measures it too; its numbers come below, after the algebra. Kaz's filter was symmetric, which helped, and full-sample, which did not. At 9:40 p.m. Kaz sent the desk a one-line email: *The winsorization is look-ahead. Fixing. Numbers tomorrow.* Nobody replied, which on this desk counts as gratitude.

*So here is the decision as it stood the next morning. The audit says about 91% of the reversal premium is bias. Your sleeve is up in paper trading, measured at the same marks. The go-live review is in three weeks. Do you kill it, re-form it with a signal gap and ex-ante filters, or run it only in bonds that printed in institutional size that week? And what evidence would change your answer?* Case Study C in §7.11 reads the hand history and records what the desk changed. First, the algebra the whiteboard was gesturing at.

> **Math, Gently.** *Covariance, and why shared noise shows up with a minus sign.* **Covariance**, Chapter 2's measure of whether two quantities move together (§2.6), can be manufactured by a measuring error alone. Picture a bathroom scale that was mis-zeroed once, on the last day of the month, so that it read half a kilo light that day only. This month's weight change, measured as the end reading minus the start, comes out half a kilo too low. Next month's change, measured *from* that same bad reading, comes out half a kilo too high. The one error enters the first difference with a plus sign and the second with a minus sign, so consecutive changes acquire a negative covariance equal to minus the variance of the error, even when the true weight changes have nothing to do with each other. Tiny number: with mark noise of $\sigma_\delta = 0.5\% = 0.005$, the shared error contributes $-\sigma_\delta^2 = -(0.005)^2 = -0.000025$ to the covariance of consecutive monthly returns. That looks negligible. When true month-to-month returns are nearly unrelated, it is the entire measured covariance, and a sort on last month's return across thousands of bonds turns it into the point-a-month premium on the whiteboard.

**Latent implementation bias: noise in both the signal and the return.** Let the observed log price be the true log price plus noise, $\tilde p_t = p_t + \delta_t$, where $\delta_t$ is i.i.d. with variance $\sigma_\delta^2$ (bid–ask bounce, a stale mark, a dealer-side mix). The observed returns are

$$
\tilde r_t = r_t + \delta_t - \delta_{t-1},
\qquad
\tilde r_{t+1} = r_{t+1} + \delta_{t+1} - \delta_t .
$$

The two returns share $\delta_t$ with opposite signs. With the true returns independent of the noise,

$$
\operatorname{Cov}(\tilde r_t, \tilde r_{t+1}) \;=\; \operatorname{Cov}(r_t, r_{t+1}) \;-\; \sigma_\delta^2 .
$$

Pure noise manufactures reversal. A portfolio that buys last month's losers and sells last month's winners is, in part, buying bonds whose month-end price was recorded too *low* ($\delta_t < 0$) and selling bonds recorded too *high*, then collecting $-\delta_t$ when the next price is drawn fresh. The premium is real in the data and unavailable in the market, because you cannot buy at the mis-recorded price. This is Roll's (1984) bid–ask model wearing a factor's clothes: Chapter 18 uses the same covariance to *estimate* the spread, as $2\sqrt{-\operatorname{Cov}}$. Dickerson, Robotti, and Rossetti (2026) call the general problem latent implementation bias, because the same noisy price sits in the sort and in the denominator of the next return.

**The fix is a gap.** Form the signal from the month-end price, but measure the return from the first feasible execution price the next month (the "month-begin" price), so the two prices are different draws of noise:

$$
\tilde r^{\text{gap}}_{t+1} = (p_{t+1} + \delta_{t+1}) - (p_{t^+} + \delta'_{t^+}),
\qquad
\operatorname{Cov}(\delta'_{t^+}, \delta_t) = 0
\;\Longrightarrow\;
\operatorname{Cov}(\tilde r_t, \tilde r^{\text{gap}}_{t+1}) = \operatorname{Cov}(r_t, r_{t^+ \to t+1}).
$$

The scene's whiteboard numbers (reversal falling from −0.99% to −0.09% a month) and §7.2's placebo, which flags far more price-based factors than non-price ones, are this identity at work. That asymmetry is the fingerprint of noise rather than economics: if the premia were real compensation for risk, the timing of the first trade would not matter much.

**Look-ahead bias in the return filter.** The second bias is quieter. Researchers winsorize or trim extreme returns to protect against data errors, which is reasonable. But if the thresholds are percentiles computed from the *full sample*, the filter uses future information. If the trimming is *asymmetric* (cutting the left tail harder than the right, or deleting returns around defaults), it deletes exactly the outcomes a long-short portfolio is most exposed to, and it chooses them with knowledge of which bonds were about to crash. Dickerson, Robotti, and Rossetti report that 6-month momentum's 0.30% per month premium comes entirely from asymmetric ex-post winsorization and is zero without it, and that 57–78% of the alpha of idiosyncratic-volatility and downside-risk factors comes from ex-post filtering. Their measure of "researcher degrees of freedom" is also worth knowing: across 648 filtering configurations, the interquartile range of factor premia averages 0.35% per month against an average premium of 0.33%. The choice of cleaning rule moves the answer by more than the answer.

The fix is ex-ante filtering: thresholds computed only from data available at the formation date, applied symmetrically, with returns around defaults *kept* (Dick-Nielsen and coauthors made the same choice). The gap matters only for signals built from the bond's own price, but the ex-ante filter matters for every signal: a full-sample trim leaks the future whatever the signal is made of, and the audit's list of factors whose significance depends on trimming includes macro-uncertainty and liquidity betas alongside the price-based ones. A model that never sees a default in training will be very confident about bonds that are about to default. That is not caution; it is a CLO manager's nightmare with a nice ROC curve.

#### Within the firm: what survived

Whether a composite's month-begin price is a clean gap is Exercise 5's question, and the answer matters most in the months when a reversal strategy trades hardest.

Theo found the evidence that would change his card on the train in, in the audit's list of survivors. Of the 26 specifications that survive false-discovery control, 25 are within-firm constructions: bonds of the same issuer sorted against each other, long one bond and short a sibling, so that issuer news cancels and what remains is the bond-level effect. The only single-sort survivor is bond age, equal-weighted. To an RSSG banker that is a capital-structure pair, the kind of intra-issuer trade Owen Achterberg's pod runs (Chapter 4-C). A price-based signal that works across issuers and dies within them was probably being paid by issuer news or by the mark, not by the characteristic. Same-issuer pairs cost more to run and are harder to short than a long-only tilt, which makes them a cost question for Chapter 9. As a diagnostic, they are cheap and sharp.

## 7.10 Trend Watch: The ML-for-Bonds Frontier and the Data Stack

Picture the spring of 2017 from a high-yield trading desk. Most bonds in the universe have not traded today, and the number beside each one on the screen is a pricing service's end-of-day opinion or a dealer's morning run. In May, MarketAxess launches Composite+, a price built by machine learning from trades, quotes, and related bonds, after about eighteen months of experimentation, and for the first time a model is producing the *input* that every other model on the desk will consume. Over the next few years the academic literature arrives from the other direction. By 2021 researchers are fitting trees and neural networks to bond returns, and one of the most careful of those papers publishes its own correction in the same volume of the *Review of Financial Studies*.

Then the question itself moves. Between 2023 and 2026 the conversation shifts from whether machine learning can predict bond returns to whether the inputs can be trusted: conditional factor models in which characteristics drive the loadings; practitioners describing tree-based fair-value models whose main benefit was lower risk rather than higher return; a 2025 paper whose strongest predictors turned out to be the very price-based signals the 2026 audit would flag; and finally, in 2026, a "glass box" model that can show which interactions it learned, and turns out to have rediscovered the structural model of Chapter 6. Meanwhile the plumbing keeps growing, and the share of it run by systematic investors stays small. Read the box as a timeline this chapter's scenes have already walked through. Each entry is a moment when somebody found out that the hard part was the data.

> **Trend Watch.** *Machine learning reaches corporate bonds, 2017–2026.*
>
> - **May 2017.** MarketAxess launches Composite+ (CP+), an ML-built pricing engine, after about 18 months of experimentation; by the company's later account it covers more than 350,000 bonds and refreshes as often as every 15 seconds (company claims, reported by FI Desk). The SMU Cox study cited in §7.1 (March 2026) finds CP+ more informative about future trade prices than the last trade, tracking efficient prices well in March 2020 but converging slowly during fire sales. AI composites are now both a *feature* (a better denominator than the last print, which shrinks latent implementation bias) and a *counterparty* (the price a market maker is adversely selected against; Chapter 18).
> - **2021.** Bianchi, Büchner, and Tamoni, "Bond Risk Premiums with Machine Learning," *RFS* 34(2), on Treasuries, followed by a corrigendum in the same volume (§7.11).
> - **2023.** Kelly, Palhares, and Pruitt, "Modeling Corporate Bond Returns," *Journal of Finance* 78(4): a conditional five-factor model (IPCA) with loadings driven by bond characteristics. Robeco (23 June 2023) describes regression-tree fair-value models for credit value investing, with the main benefit reported as lower active risk, especially in high yield.
> - **2025.** Feng, He, Wang, and Wu, "Predicting individual corporate bond returns," *Journal of Banking & Finance* 171, report an out-of-sample $R^2$ of 4.48%; their leading predictors include downside risk, short-term reversal, and skewness, three of the price-based signals the 2026 audit flags for latent implementation bias. BondBERT (arXiv:2511.01869, October 2025) fine-tunes a language model on about 30,000 UK bond-news articles, because good news for a company's equity is often bad news for its bonds.
> - **2026.** Bell, Kakhbod, Lettau, and Nazemi, "Glass Box Machine Learning and Corporate Bond Returns" (NBER WP 33320; *JFE* 181, 2026), use an explainable boosting machine with 81 predictors on 1,207 firms (July 2002–August 2020), with a deliberately long nine-year test window; the value-weighted 10−1 portfolio earns 0.67% per month with an alpha of 0.55% ($t = 4.22$). The most important interaction is financial-uncertainty shocks times spread, which is a structural-model prediction (Chapter 6) rediscovered by a model that can show its work.
> - **Market plumbing.** SIFMA reports US corporate-bond average daily volume of \$66.7 billion through September 2026, up 13.4% year on year (fetched 2026-10-17). Man Group's 2022 paper notes that, per one data provider, less than \$150 billion of US bonds had been traded electronically by quantitative investors in the prior year (Man 2022 p.3).
>
> *What it means for the desk.* The frontier moved from "can ML predict bond returns?" (2019–2021) to "can we trust the inputs?" (2023–2026) to "can the model explain itself?" (2026). The models that held up share three traits: long, untouched test windows; firm-level aggregation (one hat per issuer); and economic structure built in (Merton links, interpretable shape functions).

One number is missing from the timeline, and it is the one that explains why the frontier is still so thin.

> **[SOURCE EXTRACTION]** *Blackstone_Systematic_Credit p.2:* "While systematic strategies manage roughly 20% of global equities, they account for less than 2% of the fixed-income universe."
>
> **Annotation.** The adoption gap is the commercial case for this chapter and also a warning. A tenfold gap means the field is early, and early fields reward the managers who get the data right: Blackstone's own paper credits electronic trading, better pricing data, and computing power for closing it. But the same gap means most of the published evidence was produced on short samples by people who had never traded the bonds, which is how a four-factor model got retracted. Man Group's 2022 forecast was that "the future of quant credit will be one of increasing data sophistication, of the increasing use of machine learning" (Man 2022 p.41); the 2023–2026 record says the order of those two clauses matters. Data sophistication comes first.

> **View From Another Seat.** *The systematic asset manager, on the record.* A systematic credit manager reads this frontier from a different chair than the academic. The academic asks whether a model predicts returns; the manager asks what the model would let it *own*, at what size and at what cost. The public record from that seat is consistent. Robeco's regression trees, in the 2023 entry of the timeline above, made the portfolio's bets cleaner, not bigger. Ralph Smith of BlueCove, on *Flirting with Models* ("Ralph Smith - Scientific Investing in Fixed Income," S5E7, 11 July 2022), described how breadth and liquidity differ between credit and rates, and how the assumption a backtest makes about whether a bond is actually *available* to trade can move its results materially (paraphrased). Put together with Blackstone's adoption gap, the seat's verdict is the chapter's: in credit, capacity and availability decide what is tradeable, and model class comes a distant third. The desk's own refits kept confirming the corollary *(illustrative)*: a gradient-boosted model and a linear one, fed the same honestly timestamped, honestly priced panel and restricted to bonds that could really have been bought, disagree far less than either one disagrees with itself fed marks.

## 7.11 Case Studies: Three Autopsies of Credit-ML Failure

### Case Study A: The One-Month Lead (Bai–Bali–Wen, 2019–2023)

*What happened.* Mags told it at the end of the replay in §7.2, and the Trend Watch there carries the citations: two factor series led by a month, a third lagged, some extreme losses removed, and a retraction in December 2023.

*How the desk caught it.* Not with cross-validation, which §7.7 showed cannot reach a leak upstream of the data, but with the implementation audit Ines ran at the whiteboard: a rebuild stamped with `available_at`, played at the time it could have been played. *Lesson for Theo:* label timestamps are covenants. Read them the way you would read the definition of "Consolidated EBITDA."

*What the desk changed on Monday.* Theo turned his index card over at the next desk meeting, and it read, in full: *Ship neither as "the" benchmark. Ship the bond market factor alone, and say why. Attach the rebuild, the shift test, and a list of what would change our mind.* That was close to what the public record later supported, since Dickerson, Mueller, and Robotti's conclusion was that the earlier factors added essentially nothing beyond the bond market factor, though nobody at the whiteboard could have known it at six o'clock on a Friday. Kaz's card added two lines: rebuild all four factors before relying on any one of them, and make the one-month shift a standing test on every external file. Then Ines told them the part of the ending that was not on the public record. In October 2022 the desk had shipped the published series on the Monday, as asked; Mags's objection had been a two-line email that nobody answered. The desk's IDO reports had been stripped against the file until the retraction notice of December 2023, when the benchmark was switched to the market factor without a word in writing. The replay had been Ines's way of getting the memo written three years late. The desk wrote it that week: which reports had used the file, what their IDO numbers became against the market factor alone, and what changed in the process. Then it changed the folder. Every file in `/benchmarks/academic/` now carries a provenance row (source, version, download date, and its `available_at` convention) and a quarterly check that the source has not been corrected or retracted since the download. Two other files failed the provenance check on the first pass. Neither turned out to be wrong. Both were rebuilt anyway.

### Case Study B: The Honest Corrigendum (Bianchi–Büchner–Tamoni, 2021)

*What happened.* The *RFS* published both the original paper and, in the same volume, a corrigendum with an added coauthor (Hoogteijling) that corrects the analysis for "using information not available when the forecasts were made." Out-of-sample $R^2$ fell; predictability remained significant.

*Why it matters.* This is the gold standard of error handling, and it shows that look-ahead is usually a *pipeline* property (data vintages, revised macro series, forward-filled values), not a modeling choice. Pair it with Bohn and Stein's footnote 31 in §7.7: most leaks are things the researcher did not know they knew. The desk control is a point-in-time feature store in which every value carries the timestamp at which it became available, and ROBO is forbidden to join on anything else.

*The same mistake, on our own desk.* The desk's version of this case arrived on a Thursday, through ROBO. Theo had asked for a macro feature, the monthly change in nonfarm payrolls, joined to the bond panel "as of each date," and a fundamental, quarterly leverage, forward-filled between filings. ROBO did both exactly as asked. For the macro series it downloaded the full history from FRED, which serves the latest revised vintage of every number, and attached each month's value to the bonds on the last day of that month. For leverage it attached each 10-Q to the panel from the fiscal quarter-end the filing described and carried it forward until the next one. Both joins were correct as joins and wrong as history. The payroll number the model saw for March 2009 was the value as revised in later years, not the one printed the following month, and it was attached to March 31, before even the first release existed. The second-quarter leverage figure sat in the panel from June 30, forty-odd days before the filing that reported it: Defect 4 from §7.1, coming back through a door labeled "forward-fill."

The fix was not a better model. It was a second date on every value. The St. Louis Fed's ALFRED archive keeps macro series as they were published on each date, so the desk rebuilt the macro features from vintages: for each date, the latest value that had actually been released by then. Fundamentals were re-keyed on the filing timestamp instead of the period end. ROBO's spec gained one line, the same line the four-factor replay had produced: join on `available_at`, and on no other date. The backtest's out-of-sample $R^2$ fell by an amount that made Kaz wince and Mags shrug *(illustrative)*, and the signal survived, smaller.

Then the desk wrote it up, and the corrigendum was the template. The published correction states what the original analysis had used that was not available when the forecasts were made, reports the corrected numbers, and says what survived. The desk's memo had the same three paragraphs: what was wrong, what the corrected numbers are, what still holds. Nobody's name appeared in the first paragraph. Ines sent it to the whole floor with a one-line cover note: "This is what a good mistake looks like."

*What the desk changed on Monday.* A standing rule in the feature store: every value carries two dates, the date it describes and the date it became available, and joins use the second. Macro series are stored by vintage. And a new template on the shared drive, titled "Corrigendum," which three people used in its first month, a number the desk chose to count as a success.

### Case Study C: How a Bid–Ask Bounce Became a Factor (Short-Term Reversal, 2026)

*What happened.* The numbers are Round two of the §7.9 scene: −0.99% a month built on one shared month-end price, −0.09% once the signal and the return stop sharing it. The covariance identity in §7.9 explains the whole gap.

*How the desk would have traded it, and why it would have lost.* On an RFQ desk you cannot buy at last month's stale print; the first executable price already reflects the bounce. Ines's write-up of the hand history was Mags's Round three with timestamps attached: every "loser" the backtest bought was a bond whose last print was a small account selling at a dealer's bid, and the desk would have paid the offer. Chapter 9 picks up what survives (value and some equity-informed signals), and Chapter 10 rebuilds credit momentum on clean returns.

*What the desk changed on Monday.* The sleeve did not go live. Kaz re-formed it with a gap, measuring the return from the first institutional-size print after month-end, and with winsorization thresholds computed only from data available at each formation date, and ran the re-formed version in paper trading for the three weeks before the review. It was flat *(illustrative)*, which is what the audit predicted and roughly what Ines had bet Kaz a coffee it would be. The interesting part came at the review itself. If the reversal premium is mostly the bid–ask spread, Ines pointed out, then the desk already owned a business that earns it honestly: the market-making book, which is paid that spread for standing on the right side of it. So the signal moved there, not as an alpha but as one input to inventory skew, because a bond that has just printed well below its composite on a small sell is a bond a dealer can bid for with slightly more confidence (Chapter 18). The evidence that would revive the sleeve as a standalone strategy went into the review minutes: a within-firm version, traded at executable prices, that survives delay and transaction costs over a test window nobody has looked at. Nobody on the desk expects to see it soon.

## 7.12 The Credit ML Lab: A Reference Implementation

### Specification for AI Implementation

**What ROBO built from the vague version.** Theo's first spec said: "Find a strategy with a Sharpe above 2." ROBO ran 12,000 feature combinations overnight and returned the best one: in-sample Sharpe 2.1, deflated Sharpe ratio 0.48. It had done exactly what was asked. The precise spec below asks for something else: every reported result must carry its trial count $N$, the cross-trial Sharpe variance $V$, the deflated Sharpe ratio, the probability of backtest overfitting, and the effective sample size $N_{\text{eff}}$, and the pipeline must refuse to print a Sharpe ratio without them.

The lab exists for a reason that has little to do with elegance. Every number in the Desk Debrief that follows (the AUC that falls from 0.61 to 0.52, the hat count, the deflated Sharpe) is a claim about a pipeline, and a claim about a pipeline is worth exactly as much as somebody else's ability to rerun it and get the same answer. The four-factor replay turned on a file nobody had rebuilt; Case B turned on a join nobody had checked. So the lab is built as the opposite of a one-slide deck: six blocks on a synthetic panel whose truth is known, so that each defect of §7.1 can be switched on and its damage measured, and each repair of §7.3–§7.9 can be shown to remove that damage and nothing else. Theo's reason for wanting it was simpler. The next time somebody showed him a number with no footnote, he wanted "run it through the lab" to mean something precise.

**Data schemas (all arrays NumPy `float64` unless stated; day index $t = 0, \ldots, T-1$).**

| Object | Shape / type | Meaning and units |
| :--- | :--- | :--- |
| `xs` | `[T, NB]` | Daily excess return per bond from *marks* (decimal); `xs[0] = 0`; zero after exit |
| `spread`, `dts` | `[T, NB]` | Spread (decimal) and $\text{DTS} = D^{\text{spr}} \cdot s$ (years × decimal) |
| `issuer_of` | `[NB]` int | Ultimate-parent id (not ticker) |
| `exit_day` | `[NB]` int | Day of call, tender, maturity, or exchange; `T + 1` means never |
| `labels` | DataFrame | `bond, issuer, t0, t1` (int days, `t1` inclusive), `label` ∈ {−1, 0, 1}, `ret`, `touch` ∈ {upper, lower, vertical, exit}, `censored` (bool), `u` (uniqueness) |
| `X` | `[n_labels, F]` | Features using information available at `t0` only (point-in-time) |
| `R` | `[T_m, N]` | Returns of *every* trial evaluated, for DSR and PBO |

The edge cases ROBO must handle without guessing are written once, in the Spec at the end of the Desk Debrief.

The six blocks below run in order in one interpreter (NumPy, SciPy, pandas only), are seeded, and end each step with numerical sanity checks. The synthetic panel's parameters are illustrative.

Every model in this chapter eats features, and the first feature Kaz fed theirs was the worst one: the raw level of log OAS, which teaches a model that 2008 was wide. Section 7.3 built the repair, a dial between the level (all memory, no stationarity) and the daily change (all stationarity, no memory). The dial has a practical catch. Someone has to set it, for every series, and set it again inside every training fold without glancing at the test period. Done in a notebook, the setting becomes a number in somebody's head (was it 0.4? 0.35?). Done as a function, it becomes a rule with a tolerance, a grid, and a printout, which is the only kind of preprocessing parameter a model-risk committee will let you keep. So the first block builds the dial and then, before anything is allowed to depend on it, tries to break it.

`ffd_weights(d, tau)` runs the §7.3 recursion, starting from a weight of one and multiplying each new weight by $-(d-k+1)/k$, and stops at the first weight smaller than `tau`. That weight is discarded, so the array holds only weights worth keeping. `frac_diff(x, d, tau)` applies them as one "valid" convolution, so output $t$ is the weighted sum of today's value and the previous $K$ values. The first $K$ outputs are NaN on purpose, because a zero in a warm-up row is a fact the model will happily learn. `df_tstat` is a bare Dickey–Fuller regression (the change on a constant and the lagged level, no augmentation lags), and `min_d` walks the grid 0, 0.05, up to 1, returning the first `d` whose statistic beats the approximate 5% critical value of $-2.86$ together with the correlation between transformed and raw series, the "memory retained" of §7.3. If nothing passes it returns 1.0 and NaN.

The assertions are the point. The recursion must equal signed binomial coefficients to $10^{-12}$; the warm-up at $d = 0.4$ must land near 280 days at $\tau = 10^{-4}$ and near 54 at $10^{-3}$; $d = 1$ must reproduce ordinary differencing; and on a simulated random walk the change must test stationary and the level must not.

The desk runs it on issuer-level constant-maturity log spreads, with $d^\star$ chosen inside each training fold, and never on jump-contaminated or stale series, where §7.3's Ways box says the answer is an artifact. Kaz found two surprises in the first week. Warm-up is not monotone in $d$: with these defaults $d = 0.05$ needs 361 lagged terms, $d = 0.15$ needs 526, and $d = 0.4$ only 281. `min_d` silently skips any grid point that leaves fewer than 101 usable values, so on a short history it jumps over the small-$d$ candidates with the longest windows and reports a larger $d^\star$ without a word, which is why Kaz now prints $K$ beside $d^\star$. And the last line prints a $d^\star$ for a pure random walk that, with this seed, is 0.15, nowhere near 1. The truncated filter keeps a share of the level (the weights at $d = 0.15$ sum to about 0.35), so its output still contains a unit root that an unaugmented test is nonetheless able to reject. On the desk $d^\star$ is a screen applied identically to every series, not an estimate of anyone's true order of integration.

*The full listing is [Listing 7.1 in Appendix F](#code-7-1).*

A reference implementation has a chicken-and-egg problem. The chapter's claims are about defects in real data (prices that are rumors, one issuer wearing forty-seven hats, bonds that vanish through exchanges), and real data will not tell you how much of any number is the defect, because the truth the marks are smoothing is exactly the thing you never see. To find out whether a pipeline survives the five defects, a desk needs a world where the answer is printed on the back of the card: a panel in which the true spread, the stale mark, the parent-level shocks, and the exits are all planted by hand, so every later block can be graded against something known. It is also the only way to hand ROBO an acceptance test. A spec that says "marks must understate volatility" can be checked only where you know what the volatility is. The second block builds that fixture.

`simulate_panel` draws five years (1,260 trading days) of 120 ultimate parents, each with one plus a Poisson(2) number of bonds; the default seed gives 330. Each parent gets a base spread drawn log-uniformly between 100 and 800bp, and each bond gets a spread duration between 2 and 8 years, a fixed basis, and a mark speed `theta` between 0.2 and 1, where 1 is a live mark. The true log spread is the sum of the parent's base, the bond's basis, a slow market factor shared by everyone, a parent-level factor shared by that parent's bonds that also takes a rare jump (about once in ten years per parent, half a log point wide, then decaying), and bond-level noise. Sharing the parent factor is Defect 2 by construction: siblings move together because one company's news moves them.

The marks are the true log spread passed through partial adjustment, each day closing a fraction `theta` of the gap; a bond with `theta` of 0.2 is the evaluated price that wakes up on Thursday. Excess return, carry on yesterday's spread minus duration times the spread change, is then computed twice: from true spreads (`xs_true`, for diagnosis only) and from marks (`xs`, the only series later blocks may use). Finally 30% of bonds exit on a random date after the first quarter of the sample, two-thirds by tender (adding 2% to that day's return) and the rest by distressed exchange (subtracting 15%), with zeros afterwards and `exit_day` set to $T+1$ for survivors. The function returns `[T, NB]` arrays plus `issuer_of`, `exit_day`, and a DTS built from the marked spread, which is what a desk would see. The two assertions pick the slowest-marking bond that never exits and check that its marked volatility is below 80% of the true figure and its lag-one autocorrelation higher by more than 0.2, the two fingerprints of the first defect.

It is a fixture, never a calibration; every parameter is illustrative. The exits are where it surprises people. They are added to the marked return after the smoothing, so they arrive as clean jumps on an otherwise smoothed series, and `xs_true` knows nothing about them. After a bond's exit date the two series are different animals, which is why the assertions test a survivor.

*The full listing is [Listing 7.2 in Appendix F](#code-7-2).*

"Did the bond go up over 13 weeks?" is a question with a sign. "Did the bond do something a risk manager would call an event?" is a question with a path, a scale, and a clock. Theo's old 13-week model ran to its horizon and stopped, and so does the naive label. A label worth training on needs a barrier whose width means the same thing for a 100bp BBB and an 800bp B3, a rule for the day the bond is called out from under you, and a record of exactly which days the label spans, because §7.7 will use those days to decide what may be trained on. Tens of thousands of these are not going to be hand-labeled, and the conventions must not drift between the analyst who labels on Monday and the one who labels on Friday. So the third block writes them down once.

`triple_barrier` takes the panel's excess returns, DTS, parent ids, and exit days, plus a 63-day horizon, a new label every 10 days per bond, barrier multipliers of one, and 9% monthly relative spread volatility, the Ben Dor prior from §7.4. It cumulates `xs`, so the path after formation date `t0` is the difference of two rows. The barrier half-width is DTS on day `t0` times 9% scaled by the square root of three months, so only what was known at `t0` sets the width. For each bond still alive at `t0` it finds the first day the path crosses the upper barrier, the first day it crosses the lower one, and the day the bond exits. The earliest wins; if none occurs the label closes on the vertical barrier at day 63, and a tie on the same day goes to the exit, then the lower barrier, then the upper. The label is $+1$ or $-1$ for a touch, and the sign of the realized return for a vertical or exit close. The output keeps the realized return `ret` (the depth of the trapdoor), the inclusive close day `t1`, the `touch` type, and a `censored` flag for exits. Formation dates stop 63 days before the end, so no vertical barrier ever falls outside the sample.

With the defaults, 330 bonds produce 35,934 labels: 58% vertical, 29% upper, 11% lower, 1.3% exit. The lopsided touch shares are the carry tilt of §7.4 arriving on schedule, because the barriers sit on raw excess return, coupon income included; in production, feed the function the IDO return instead. The assertions check that labels lie in $\{-1, 0, 1\}$, that every window has positive length, that upper touches earned positive returns and lower touches negative ones, and that exits exist without dominating.

The labels keep two blind spots. Touches happen on marks, with no confirmation by an institutional-size print, so a pricing service's sneeze counts as an event. And the censored rows are the ones a tidy-minded analyst deletes. They are 1.3% of the table and exactly the tenders and distressed exchanges; dropping them brings back the survivorship bias that §7.1 gave a whole defect to, which is why the flag stays and the purge runs on `t1`, the exit date for these rows rather than day 63.

*The full listing is [Listing 7.3 in Appendix F](#code-7-3).*

Tens of thousands of labels, 330 bonds, 120 parents. How many independent pieces of evidence is that? Kaz answered by counting rows, and the right answer is the one the forty-seven hats already taught: far fewer, and the number belongs on the first line of every result. Computing it is not hard, but it is easy to compute badly. The textbook definition loops over every label and every day it covers, once per parent, which is fine in a notebook and miserable for a panel rebuilt nightly. A desk wants the hat count as a function that runs in seconds, reproduces a toy case exactly, and is called by the pipeline itself, so that nobody can print a Sharpe ratio without it. The fourth block is that function.

`issuer_uniqueness` works one parent at a time. For that parent's labels it writes a difference array, plus one at each `t0` and minus one on the day after each `t1`, and a cumulative sum of it is the issuer concurrency of §7.6: how many of the parent's labels, across all its bonds, are live on each day. A second cumulative sum, of one over concurrency, lets any window's average be read from two lookups, so the average uniqueness of a label costs the same whether its window is 5 days or 63, and total work is linear in labels and days rather than their product. The `np.maximum(conc, 1)` guards only days on which none of the parent's labels is live, which no label's own window touches. Results are written back by position, so `u` lines up with the rows as passed.

The toy test is the definition in miniature: two siblings with identical windows get 0.5 each, and a lone label from another parent gets 1.0. On the panel, `n_eff` is the sum of `u`, and the assertions require every `u` in $(0, 1]$ and $N_{\text{eff}}$ under a quarter of the row count. The default run prints 35,934 rows against an $N_{\text{eff}}$ near 2,700, a ratio of 0.076, so each independent observation is wearing about thirteen label rows. Even a parent with a single bond has a median `u` of 0.17, since a 63-day window launched every ten days is shared by six or seven labels at once.

`u` goes into the loss as the sample weight and into a sequential bootstrap as the draw probability. $N_{\text{eff}}$ is not evidence about the market. Concurrency is counted within a parent, so 120 parents hit by the same week of widening each keep their own tidy `u` while jointly delivering one observation of the regime; with 1,260 days and a 63-day horizon there are about 20 non-overlapping windows, and 20 is the honest ceiling for a model that times credit as a whole. The trap is that `u` is relative to the table you hand the function. Drop the censored rows or split off a fold afterwards and the survivors still carry the discount for siblings that have left, so the weights err small; the pipeline computes `u` on the rows the model will train on and records which table $N_{\text{eff}}$ describes.

*The full listing is [Listing 7.4 in Appendix F](#code-7-4).*

Kaz reported a cross-validated Sharpe of 1.8 with the straight face of someone who had used the conservative method. The argument of §7.7 is that it was not conservative, and arguments of that kind have a half-life of about one meeting. What turns them into policy is a demonstration in which the answer is known: take features that carry no information about the outcome by construction, run them through a leaky splitter and an honest one, and see which finds alpha in noise. A desk keeps that experiment in the repository as a standing canary, and every new cross-validator or feature pipeline has to pass it before it touches real labels. Ines would call it checking the deck before you sit down. The fifth block is the canary.

Two splitters compete. `shuffled_kfold` assigns each label to one of five folds at random by row. `purged_group_kfold` implements §7.7: it assigns whole parents to five group folds at random, cuts formation dates into four equal-width time blocks, and treats every (group fold, time block) pair as a test set, twenty in all, so each label is tested exactly once. For each test set it takes the earliest test start $T_0$ and the latest test end $T_1$, then removes from training every other-parent label whose window overlaps the span from $T_0$ to $T_1$ plus `embargo` days. Purge and embargo are one inequality. What remains from the other parents, before and after the block, trains the model.

The model is deliberately gullible. `knn_scores` averages the outcomes of a test label's 10 nearest training labels, in batches to bound memory, because a nearest-neighbor lookup is the purest way to exploit a leak. `cv_auc` pools the out-of-fold scores into one rank-based AUC; about seven in ten labels are positive here (the carry tilt again), which is why the score is AUC and not accuracy. The features are four columns for 25 randomly chosen parents (6,661 labels on 61 bonds by default): a persistent parent trait plus a slowly wandering bond-level drift. They are noise by construction, independent of the label, but they identify the parent and the date, so a test label's nearest neighbors are its siblings and its neighbors in time, whose outcomes share its window. Shuffled K-fold lets the model look them up and scores about 0.71; the purged, grouped scheme scores about 0.50. The assertions demand a gap of at least 0.03 and an honest score within 0.06 of a coin flip.

Every new splitter or feature pipeline on the desk goes through this canary before it touches real labels; a splitter that finds alpha in noise is leaking. It cannot catch a feature stamped with the wrong availability date, because here the features are clean by construction. And its `embargo=21` is a trap for whoever copies it. Section 7.7 sets the embargo at no less than the longest feature lookback, and the fractionally differenced features of §7.3 carry a window near 280 days. The noise features here have no lookback, so 21 is harmless in this experiment, and nothing in the function warns you when real features go in.

*The full listing is [Listing 7.5 in Appendix F](#code-7-5).*

The demonstration is Kaz's "oh" from §7.7, made repeatable. Kaz asked for the block to be added to the desk's onboarding notebook, on the grounds that everyone deserves to say "oh" once, in private, on synthetic data, rather than in a model review on real money.

Everything so far has protected a single evaluation. The last block protects the report, which is where a research process most comfortably lies to itself. Kaz did not report one backtest; Kaz reported the best of about 3,000, and a human memory of how many were tried is not an input anyone should accept. The statistics that fix this need three things a notebook rarely keeps: the full matrix of returns from every configuration ever run, the number of columns in it, and the spread of Sharpe ratios across them. That is why the refusal at the top of this section exists. The sixth block holds those calculations, plus the one function that turns a meta-label probability into a position.

`bet_size` is the §7.5 map: clip the probability away from 0 and 1, convert it to $z = (p - 0.5)/\sqrt{p(1-p)}$, take $2\Phi(z) - 1$, floor at zero, and multiply by the primary model's side. The checks reproduce the chapter's numbers ($p = 0.75$ gives 0.44; $p = 0.9$ on a short gives $-0.82$) and confirm that $p = 0.4$ gives exactly zero: the secondary model may veto the analyst, never reverse her.

The rest works on a matrix `R` of shape `[T, N]`, one column per trial. `sharpe` is the plain column mean over the sample standard deviation with no annualization, and every statistic below inherits that per-period unit. `psr` is the probability that the true Sharpe beats a benchmark given skewness and non-excess kurtosis. `expected_max_sr` is the extreme-value formula for the best of $N$ noise strategies. `deflated_sharpe` picks the column with the best Sharpe, measures its skewness and kurtosis, sets the benchmark to the expected maximum computed from the number of columns and the variance of Sharpe across them, and returns the Sharpe, the benchmark, the PSR against zero, and the deflated ratio. `min_trl` solves the PSR formula for the periods needed. `pbo_cscv` cuts time into ten blocks, runs all 252 half-and-half splits, finds the in-sample winner in each, ranks it out of sample, and reports the share of splits in which it lands at or below the median.

With 1,000 pure-noise strategies over 120 months, the simulated best Sharpe matches the formula within 10%, and the winner looks significant at a naive 95% (PSR near 1) while its deflated ratio is 0.59, barely better than a coin flip. The PBO of noise comes out at 0.55 and falls to 0.16 once one strategy with a monthly Sharpe of 0.6 is planted. A Sharpe of 0.3 against 0.1, with skew $-0.5$ and kurtosis 5, needs 85 months.

The trap in this block is the matrix itself, and it is Kaz's 3,000 in miniature. `deflated_sharpe` learns $N$ and the cross-trial variance from the columns it is handed. Hand it only the survivors and it computes a smaller $N$ and a smaller spread, a lower bar, and a flattering answer; it cannot know about a column that was never saved, which is why the spec makes ROBO write every configuration's returns into `R`, failures included. It also treats trials as independent, so 400 near-identical momentum variants count as 400 unless someone collapses them first.

*The full listing is [Listing 7.6 in Appendix F](#code-7-6).*

Porting the lab to the real panel means replacing `simulate_panel` with the point-in-time TRACE and pricing-composite feed (Appendix B) and keeping every assert as a production test.

## 7.13 Desk Debrief

*Kaz's rerun, Theo's report and every number on both are fictional and illustrative.*

Two weeks after the cold open, Kaz reran the gradient-boosted model through the lab. The screen was much less exciting, which on this desk is how you know a number has been near the truth.

The row count was unchanged: 212,000 bond-months. Above it, in a font Kaz had made deliberately large, sat the hat count, $N_{\text{eff}} \approx 24{,}000$. Below it: shuffled K-fold AUC 0.61, purged and parent-grouped AUC 0.52; 3,000 trials; an out-of-sample Sharpe ratio of 0.30 per month across the purged folds; deflated Sharpe ratio 0.84; PBO 0.41 *(all illustrative)*. The top decile still held nine issuers. It no longer had a reason to.

"It isn't a strategy," Kaz said. "It isn't nothing, either. It's mostly carry and one company."

"Strip the carry," Theo said, "and then show me the one company." IDO or it didn't happen.

Theo had run something smaller. His primary model was the credit-agreement read turned into flags: drop-down capacity through unrestricted subsidiaries, non-pro-rata uptier risk, and a liquidity runway from the 13-week model shorter than two quarters. That came to about forty flags a year across the high-yield universe. The secondary model, trained on purged, parent-grouped folds, learned only *when those flags were right* and sized them. He had tried four sizing models, and he wrote the number four at the top of the report as if it were a defined term. Out of sample, the result was a Sharpe ratio of 0.20 per month over 96 months, with skew −1.5 and kurtosis 8. Against the four-trial benchmark ($SR^\ast \approx 0.02$), the deflated Sharpe ratio was 0.93, and the minimum track record length was about 115 months, so he needs roughly a year and a half more of live trading before the number means what he wants it to mean *(illustrative)*.

The forty flags were not forty ideas. On inspection they were about a dozen kinds of sentence. Most were drop-down flags: an unrestricted-subsidiary basket wide enough, and an investment covenant loose enough, that a company could move its best intellectual property or its best plants out of the lenders' reach without asking them. A smaller group were uptier flags, credit agreements whose amendment provisions let a simple majority of lenders subordinate the minority, the Serta pattern Theo had spent two years of his life inside. The rest were runway flags, companies whose 13-week cash flow, rebuilt from public filings, ran out before the second coupon. Each flag was a position in waiting, and the secondary model's job was to say which of them deserved size.

The one Theo got most wrong was a drop-down flag on a consumer-products company with a famously loose agreement *(a fictional composite)*. The basket was there, the sponsor was aggressive, and the bonds traded as if nobody had read page 140. He flagged it with the highest conviction he had. Nothing happened. Over the following year the business improved, the sponsor sold the company to a strategic buyer, and the buyer's financing took out the bonds at par. The flag had been a correct reading of the document and a wrong reading of the world. The capacity to harm lenders is not the intention to, and a company that does not need new money does not need to strip collateral to raise it. The secondary model had, as it happened, sized that flag small: in the training folds, drop-down flags on companies with more than a year of runway had been right barely more often than a coin. Theo's conviction had been highest exactly where his hit rate was lowest. It was the most useful thing the meta-labeling layer told him all month, and it is why the drop-down flag now carries the runway as a condition.

Then the four. He set it at the top of the report, above the Sharpe ratio, in bold, followed by a definition in the style of the documents he used to read for a living: *"Trials" means each sizing model, feature set, label horizon, or threshold evaluated on the Validation Data by any member of the desk, whether or not reported; "Four" means the number of Trials.* Kaz read it twice and asked whether it was legally binding. Theo said it was more binding than that. It was in the trial log.

"Now," Ines said, "you're showing me a hand *and* the number of hands you folded. Sit down."

Mags looked at the four. "Back in my day we had one sizing model. It was called the PM's mood, and it had an excellent track record, because the PM was the one who kept it."

At the bottom of the monitor Kaz had taped the epigraph that Dickerson, Robotti, and Rossetti chose for their 2026 audit, Ronald Coase's line: "if you torture the data enough, nature will always confess." By lunch a sticky note had appeared beneath it in the unmistakable register of the Ad Hoc Group: *The data, represented by counsel, will not confess to anything absent a cooperation agreement.* None was signed, so the counter waits for Part IV.

Theo put the USB stick back in his pocket. It had been a 13-week cash flow model when he arrived. It was now a vertical barrier, a primary model, and a reason to distrust anything labeled "adjusted," which Mags said was the first sign he might last.

Mags, who distrusts lists on principle, printed this one herself, folded it once, and handed it to Theo with the only compliment she gives: "It's short enough that you'll actually read it on the day it's going wrong."

Tape these to the monitor.

- **Count hats, not rows.** The issuer is the observation: the ultimate parent, not the ticker. Print $N_{\text{eff}} = \sum_i \bar u_i$ next to every result. In Kaz's panel, 212,000 bond-months come to about 24,000 hats. A model that times the whole high-yield market has roughly one observation per non-overlapping 13-week window, which is about 79 in twenty years.
- **A mark is not a price.** Stale and smoothed marks lower measured volatility, manufacture autocorrelation, and inflate the Sharpe ratio *before* any deflation. Treat staleness as a feature and as a filter. It is worst in single-B and CCC bonds, exactly where the alpha is supposed to live.
- **Keep the memory, lose the trend.** Fractionally difference log spreads to the smallest $d$ that passes a unit-root test. Taking $d = 1$ throws away the level information that makes a spread a spread. Warm-up rows are NaN, never zero, and the FFD window counts toward the embargo.
- **Label the trade you would actually make.** Use triple barriers scaled by DTS, set on IDO returns (strip the carry, or the label learns the coupon), with a 13-week vertical barrier. Censor exits at the exit value rather than imputing them from peers. A distressed exchange is not an average outcome, however politely the press release calls it an "open market purchase."
- **The credit agreement picks the side; the model picks the size.** Meta-labeling is what RSSG already did by hand. The secondary model may veto a trade. It may never reverse one.
- **Cross-validate as if the bonds were watching.** Purge overlapping labels, embargo past the longest lookback, and group by ultimate parent. Shuffled K-fold finds signal in pure noise, and block 5 of §7.12 will demonstrate it on demand.
- **Report the folded hands.** Every Sharpe ratio travels with $N$, $V[\widehat{SR}_n]$, the DSR, the PBO, and the MinTRL, and a new factor should clear roughly $t > 3$. ROBO refuses to print a Sharpe ratio without them, and so should you.
- **Timestamps are covenants.** Measure returns from the first feasible price after formation (the gap), filter ex-ante and symmetrically, keep the defaults, and join only on availability time. Between a retraction, a corrigendum, and 26 surviving specifications out of 432, the 2019–2026 record says credit ML is a data-integrity discipline first and a modeling discipline second.

### The Spec You Hand the Robot

Paste the block below into ROBO's prompt. It compresses §7.3–7.12 into one engine. The six Python blocks in §7.12 are the executable reference, and their asserts are the acceptance tests.

```text
ROBO: build credit_ml_lab, a leakage-proof research harness for bond-level ML.
Implement exactly this. Where something is unspecified, stop and ask; do not guess.

INPUTS (point-in-time; every field carries available_at; join on nothing else)
  xs[T,NB]       daily excess return vs duration-matched Treasuries, decimal, from marks
  s[T,NB]        spread, decimal;  D_spr[T,NB] in years;  DTS = D_spr * s
  stale[T,NB]    trading days since the last institutional-size TRACE print
  parent[NB]     ULTIMATE-PARENT id (not ticker; unrestricted subs map to their parent)
  exit_day[NB]   call/tender/maturity/exchange/default day, T+1 if none; exit_type[NB]
  primary[T,NB]  side in {-1, 0, +1} from the analyst/covenant model (Chapter 13 flags)

PIPELINE
  1 FFD features on log s: d* = smallest d on 0.00:0.05:1.00 with DF t < -2.86
    (approximate 5%); tau = 1e-4, or 1e-3 if the warm-up exceeds the embargo budget.
    Warm-up rows are NaN and are dropped.
  2 Labels: triple barrier on IDO returns (carry and factor beta stripped, Chapter 8);
    half-width = m * 0.09 * sqrt(h/21) * DTS[t0], m = 1, h = 63 trading days.
    An exit before t0+h closes the label at the exit value: touch="exit", censored=True.
    Never form a label whose vertical barrier lies past the last date.
  3 Weights: parent-level average uniqueness u in (0,1]; N_eff = sum(u); Kish size;
    weights normalized to sum to n_labels. Single-bond parents get u from time overlap only.
  4 CV: purged, embargoed, parent-grouped K-fold x time blocks, plus annual walk-forward.
    embargo >= max(h, longest feature lookback including the FFD window).
    A fold with no positive labels is skipped and reported.
  5 Meta-label: secondary model -> p, clipped to [1e-6, 1-1e-6];
    size = max(2*Phi((p-0.5)/sqrt(p*(1-p))) - 1, 0) * primary.  Veto yes, reversal never.
  6 Evaluation returns start at the first feasible price AFTER signal formation (gap).
    Return filters are ex-ante and symmetric; returns around defaults are kept.

OUTPUT (one JSON record per experiment, appended to an immutable trial log)
  n_trials_raw, n_trials_clustered, var_sr, sr, psr0, dsr, min_trl, pbo (CSCV, S=10),
  n_labels, n_eff, kish, auc_shuffled, auc_purged, share_censored, share_stale_gt5d

REFUSE
  - to print any Sharpe ratio without n_trials, var_sr, dsr, pbo and n_eff beside it
  - to estimate kurtosis or the DSR from fewer than 30 returns (report "unavailable")
  - to delete a trial from the log, ever

ACCEPTANCE TESTS (keep in CI)
  - pure-noise features: auc_shuffled > auc_purged + 0.03 and |auc_purged - 0.5| < 0.06
  - 1,000 noise strategies x 120 months: mean max SR within 10% of the formula;
    the best has psr0 > 0.95 and dsr < 0.95
  - FFD weights equal (-1)^k binom(d, k) to 1e-12; d = 1 reproduces np.diff
  - two sibling bonds on identical windows get u = 0.5 each; a lone bond gets u = 1.0
```

The refusal to delete a trial is the line that matters most. A deflated Sharpe ratio is only as honest as the trial count fed into it, and the cheapest way to raise a DSR is to forget the 2,999 configurations that never made the slide. ROBO does not forget, which is the one respect in which it is a better researcher than any of us.

### Exercises

Each exercise replays a scene from this chapter with the numbers in your hands: Kaz's hats, the closing-night dial, Theo's forty flags, the report that had to be deflated twice, the composite that is not a clean gap, and ROBO's literal reading of "the future."

1. **Count Kaz's hats.** One issuer has 11 bonds. Each bond produces a daily triple-barrier label with $h = 63$ trading days over $T = 1{,}260$ days, and every label runs to its vertical barrier. (a) Show that an interior label has $\bar u_i \approx 1/(11 \times 63)$ and that the issuer contributes $N_{\text{eff}} \approx T/h \approx 20$, whatever the number of bonds. (b) Seven of the 11 bonds are guaranteed OpCo notes. Four are HoldCo notes that were primed last quarter by a drop-down into an unrestricted subsidiary. Do they remain one group for cross-validation? What new label does the drop-down create, and how would you validate a model of it? (c) Compute the Kish effective size of the weights $w = (1, 1, 1, 1, 6)$.
   *Check:* (a) Concurrency is about $11 \times 63 = 693$ in the interior, and roughly $11 \times 1{,}197$ labels divided by 693 gives about 19. (b) They remain one group. The ultimate parent is the information unit, and splitting it lets the model read the OpCo bonds' answers off the HoldCo bonds. The drop-down does create a legitimate *within-parent* target, the OpCo–HoldCo basis, but it can only be validated across time blocks, because there is no other parent to hold out. (c) $(\sum w)^2 / \sum w^2 = 100/40 = 2.5$: five rows, two and a half opinions.

2. **Memory after a closing night.** (a) Compute the first five FFD weights for $d = 0.4$ from $w_k = -w_{k-1}(d-k+1)/k$. (b) Prove that $\sum_{k=0}^{K} w_k = (-1)^K \binom{d-1}{K}$, that this partial sum is strictly positive for every finite $K$ when $d \in (0,1)$, and that it tends to zero as $K \to \infty$. (c) Block 5 of §7.12 uses a 21-day embargo because its features have no lookback. Suppose you add FFD features with $d = 0.4$ and $\tau = 10^{-4}$, whose warm-up is about 280 days (block 1). What embargo does the edge-case rule require, and how much of a 1,260-day sample split into four time blocks does it remove after each test block? What does raising $\tau$ to $10^{-3}$ buy, and what does it cost?
   *Check:* (a) $(1, -0.4, -0.12, -0.064, -0.0416)$. (b) Since $w_k = (-1)^k \binom{d}{k}$, Pascal's rule $\binom{d}{k} = \binom{d-1}{k} + \binom{d-1}{k-1}$ makes the alternating sum telescope to $(-1)^K \binom{d-1}{K} = \prod_{j=1}^{K} (j-d)/j$. Every factor is positive for $d \in (0,1)$, and the product behaves like $K^{-d}/\Gamma(1-d) \to 0$. (c) The embargo must be at least 280 days. That is close to 90% of a 315-day block, and more than a fifth of the sample, removed after every test block. At $\tau = 10^{-3}$ the window falls to about 54 days, and the horizon $h = 63$ sets the embargo again. The cost is a larger leftover weight sum, so the filtered series carries more of the trending level, and the smallest $d$ that passes the unit-root test usually rises. You pay for the extra training data in memory.

3. **Size Theo's hand.** Theo's primary model raises 40 flags a year with a precision of 35%. A winning flag earns +4% and a losing one −2% in IDO return, at unit size *(illustrative)*. The meta-model keeps 60% of the winners and lifts precision to 55%. (a) Compute the expected IDO return per trade, and per year summed over trades at unit size, with and without the meta-model. (b) Compute the bet size for $p = 0.75$ and for $p = 0.55$. In Ines's terms, explain why a 55% read earns a small position rather than a slightly-better-than-half one. (c) The meta-model's training set contains every flag Theo has ever raised, including flags on issuers that later did a drop-down. Which splitter must you use, and what goes wrong with the obvious one?
   *Check:* (a) Without it: $0.35 \times 4 - 0.65 \times 2 = +0.10\%$ per trade, or $+4\%$ a year. With it: 8.4 winners at 55% precision means about 15.3 trades, and $0.55 \times 4 - 0.45 \times 2 = +1.30\%$ per trade, or about $+20\%$ a year from fewer than half the trades. (b) For $p = 0.75$, $z = 0.25/\sqrt{0.1875} \approx 0.577$ and $2\Phi(z) - 1 \approx 0.44$. For $p = 0.55$, $z = 0.05/\sqrt{0.2475} \approx 0.10$, giving about 0.08. The sizing rule converts the edge into a test statistic and bets the confidence that the edge exists. A 55% read is barely distinguishable from a coin flip, so it gets a chip, not a stack: bet your confidence, not your opinion. (c) Use purged, parent-grouped folds. Flags on one parent cluster in time around the same corporate event, so a shuffled split trains on the answer to the test flag.

4. **Deflate the honest number.** Section 7.8 deflated Kaz's in-sample winner. Now deflate the number on his new report: a purged out-of-sample Sharpe ratio of 0.30 per month over $T = 240$ months, with skew $-0.5$ and kurtosis 5, selected from $N = 3{,}000$ trials with $V \approx 1/T$. (a) Show that the DSR is about 0.84. (b) Clustering the trial-return correlations finds about 400 effectively distinct trials. Holding $V$ fixed, recompute $SR^\ast$ and the DSR. (c) Compute the MinTRL at 95% confidence against the clustered $SR^\ast$, and compare it with the history TRACE has. (d) Explain why feeding the *in-sample* Sharpe ratio of 2.9 into the DSR is a category error.
   *Check:* (a) $SR^\ast \approx 0.23$, the denominator is $\sqrt{1 + 0.15 + 0.09} \approx 1.11$, and $\Phi(0.07 \times 15.46 / 1.11) = \Phi(0.98) \approx 0.84$. (b) $\Phi^{-1}(1 - 1/400) \approx 2.81$ and $\Phi^{-1}(1 - 1/(400e)) \approx 3.12$, so $SR^\ast \approx 0.065 \times (0.423 \times 2.81 + 0.577 \times 3.12) \approx 0.065 \times 2.99 \approx 0.19$, and the DSR is $\Phi(0.11 \times 15.46 / 1.11) = \Phi(1.5) \approx 0.93$. It is better, and still short of 95%. (c) $T^\ast = 1 + 1.24 \times (1.645/0.11)^2 \approx 280$ months, roughly 23 years. That is about the entire life of TRACE (dissemination began in July 2002), and more than three years longer than Kaz's sample. (d) The DSR corrects for selection *across* trials. An in-sample Sharpe ratio also contains overfitting *within* the trial (the trees memorized the 47 hats), so each trial's return series must already be out of sample before it is deflated. Deflating an in-sample number is like haircutting a pro forma EBITDA that already includes the synergies.

5. **The composite is not a clean gap.** In §7.9 the gap return used a month-begin price whose noise $\delta'_{t^+}$ was uncorrelated with the month-end noise $\delta_t$. Suppose instead that the month-begin price is an AI composite anchored partly on the last print, so that $\operatorname{Corr}(\delta'_{t^+}, \delta_t) = \rho > 0$, with standard deviations $\sigma_{\delta'}$ and $\sigma_\delta$. (a) Show that $\operatorname{Cov}(\tilde r_t, \tilde r^{\text{gap}}_{t+1}) = \operatorname{Cov}(r_t, r_{t^+ \to t+1}) - \rho\,\sigma_\delta \sigma_{\delta'}$. (b) The SMU Cox study found that the composite tracked efficient prices well in March 2020 but converged slowly during fire sales. What does that imply about $\rho$ in exactly the months when a reversal strategy is most active, and what would you use as the entry price instead?
   *Check:* (a) The only noise shared by the two returns is $+\delta_t$ in $\tilde r_t$ against $-\delta'_{t^+}$ in the gap return, so the bias is $-\operatorname{Cov}(\delta_t, \delta'_{t^+}) = -\rho\,\sigma_\delta\sigma_{\delta'}$. At $\rho = 0$ it vanishes. At $\rho = 1$ with equal variances it is the full Roll bias of §7.9 again. (b) Slow convergence means the composite inherits the stale print, so $\rho$ rises precisely when dispersion and measured reversal premia are largest. Use the first executable institutional-size trade (or a dealer level you could actually have hit) as the entry price, and report the premium under both definitions.

6. **ROBO and the future.** Theo's first draft of the leakage rule read: "Make sure the model doesn't use future data." ROBO complied by deleting the label column, which was the only future data in the table. Write the precise rule in at most 120 words. Name the timestamp field, the join rule, the purge condition, the embargo, and one test that fails the build if anyone breaks the rule.
   *Check:* A good answer names `available_at` and requires an as-of join (`available_at <= t0`) for every feature. It states the purge as "drop training label $j$ if $[t_{0,j}, t_{1,j}]$ intersects $[T_0, T_1 + \text{embargo}]$," with the embargo at least $\max(h, \text{longest lookback})$. It ships the pure-noise AUC test from block 5 as the guard. Bonus credit for forbidding forward-fill across a data-release date, which is one common way the kind of error behind the 2021 corrigendum gets into a pipeline.

### Deep-Dive Resource Graph

**Podcasts**

- *Flirting with Models* (Corey Hoffstein), Season 7, Episode 32: Ben Wellington, "Complex Feature Engineering at Two Sigma." Feature construction as a discipline, which is the step before §7.3–7.4.
- *Flirting with Models*, Season 7, Episode 33: Stacie Mintz, "Turning Qualitative Fundamentals into Quantitative Factors." The closest podcast treatment of the primary-model idea in §7.5: analyst judgment turned into a signal a model can size.
- *Bloomberg Odd Lots*, "How to Succeed at Multi-Strategy Hedge Funds," with Giuseppe Paleologo (20 May 2024). Why: the platform model behind the View From Another Seat box in §7.8 (capital added to PMs who perform and taken from those who do not; stop-losses as crude tail insurance). Reading that hiring and defunding is itself a multiple-testing search, with the stop-loss as a real-time out-of-sample test, is this book's, not the guest's (paraphrased, not quoted).
- *Flirting with Models*, Season 5, Episode 7: Ralph Smith (BlueCove), "Scientific Investing in Fixed Income" (11 July 2022): https://www.flirtingwithmodels.com/episodes/kAEkSoYuRwd . Why: a practitioner on how breadth, liquidity, and the assumption about a bond's availability move a credit backtest, the seat behind the §7.10 box.

**Practitioner Writing**

- Robeco (Messow, Houweling, and 't Hoen), "The next frontier in value investing in credits: integrating machine learning" (23 June 2023): https://robeco.com/en-us/insights/2023/06/the-next-frontier-in-value-investing-in-credits-integrating-machine-learning
- Robeco, "How machine learning enhances value investing in credits" (April 2024): https://robeco.com/en-ch/insights/2024/04/how-machine-learning-enhances-value-investing-in-credits
- AQR, working-paper page for Dick-Nielsen, Feldhütter, Pedersen, and Stolborg, "Corporate Bond Factors: Replication Failures and a New Framework": https://www.aqr.com/Insights/Research/Working-Paper/Corporate-Bond-Factors-Replication-Failures-and-a-New-Framework ; Quantpedia's summary: https://quantpedia.com/corporate-bond-factors-replication-failures-and-a-new-framework/
- *Systematically Biased* (Substack), "Pockets of Replicability (Post #6)" (2 June 2026), a narrative of the Bai–Bali–Wen misalignment: https://systematicallybiased.substack.com/p/pockets-of-replicability-post-6
- Warwick Business School, news item on the Fama-DFA Prize won by Mueller and Robotti for the paper they wrote with Dickerson (9 September 2024): https://www.wbs.ac.uk/news/research-bond-market-wins-fama-dfa-prize/
- SMU Cox, *Cox Today*, on Venkataraman, Jacobsen, and Xu's study of AI-driven bond pricing (7 March 2026): https://www.smu.edu/cox/coxtoday-magazine/2026-03-07-ai-driven-technique-bond-prices ; FI Desk on MarketAxess CP+: https://www.fi-desk.com/marketaxess-bringing-transparency-to-the-muni-marketplace-with-ai-powered-pricing/
- On the shelf: Ben Dor, Dynkin, Hyman, and Phelps, *Quantitative Credit Portfolio Management* (pp. 39, 50, 204, 338); Dynkin and coauthors, *Systematic Investing in Credit* (pp. 611, 651); Bohn and Stein, *Active Credit Portfolio Management in Practice* (pp. 465–467); Paleologo, *Advanced Portfolio Management* (pp. 49, 159); BlackRock, *Systematic High Yield Credit* (p. 6); Blackstone, *Systematic Credit* (p. 2); Man Group's 2022 and 2023 quant-credit papers (Man 2022 pp. 3, 41).

**Academic Papers**

*The overfitting canon.*

- López de Prado (2018), *Advances in Financial Machine Learning* (Wiley): chapters 3–5 (labeling, sample weights, fractional differentiation) and chapter 7 (purged cross-validation).
- Hosking (1981), "Fractional differencing," *Biometrika* 68(1): 165–176, DOI 10.1093/biomet/68.1.165.
- Bailey and López de Prado (2014), "The Deflated Sharpe Ratio," *Journal of Portfolio Management* 40(5): 94–107: https://papers.ssrn.com/abstract=2460551
- Bailey, Borwein, López de Prado, and Zhu (2017), "The Probability of Backtest Overfitting," *Journal of Computational Finance* 20(4), DOI 10.21314/jcf.2016.322: https://papers.ssrn.com/abstract=2326253
- Bailey and López de Prado (2021), "The False Strategy Theorem," *American Mathematical Monthly* 128(9): https://escholarship.org/content/qt95t7k79q/qt95t7k79q.pdf
- Harvey, Liu, and Zhu (2016), "... and the Cross-Section of Expected Returns," *Review of Financial Studies* 29(1): 5–68, DOI 10.1093/rfs/hhv059: https://www.nber.org/papers/w20592
- Chordia, Goyal, and Saretto (2020), "Anomalies and False Rejections," *Review of Financial Studies* 33(5): 2134–2179, DOI 10.1093/rfs/hhaa018.
- Jensen, Kelly, and Pedersen (2023), "Is There a Replication Crisis in Finance?" *Journal of Finance* 78(5): 2465–2518, DOI 10.1111/jofi.13249: https://www.nber.org/papers/w28432 (the optimistic counterweight, for equities).
- Title only: Harvey and Liu (2015), "Backtesting," *Journal of Portfolio Management* 42(1); López de Prado (2019), "A Data Science Solution to the Multiple-Testing Crisis in Financial Research," *Journal of Financial Data Science*; Joubert (2022), "Meta-Labeling: Theory and Framework," *Journal of Financial Data Science*; Roll (1984), "A Simple Implicit Measure of the Effective Bid-Ask Spread in an Efficient Market," *Journal of Finance*.

*The bond-factor audit.*

- Bai, Bali, and Wen (2019), "Common risk factors in the cross-section of corporate bond returns," *Journal of Financial Economics* 131(3): 619–642: https://ideas.repec.org/a/eee/jfinec/v131y2019i3p619-642.html ; retraction notice, *Journal of Financial Economics* 150(3), DOI 10.1016/j.jfineco.2023.103721.
- Dickerson, Mueller, and Robotti (2023), "Priced risk in corporate bonds," *Journal of Financial Economics* 150(2), 103707; arXiv posting: https://arxiv.org/abs/2604.05699
- Dick-Nielsen, Feldhütter, Pedersen, and Stolborg (2023, revised 2025), "Corporate Bond Factors: Replication Failures and a New Framework," SSRN 4586652.
- Dickerson, Robotti, and Rossetti (2026), "The Corporate Bond Factor Replication Crisis," arXiv:2604.07880: https://arxiv.org/abs/2604.07880
- Title only: Dick-Nielsen (2009), "Liquidity Biases in TRACE"; Dick-Nielsen (2014), "How to Clean Enhanced TRACE Data."

*Machine learning for bonds.*

- Bianchi, Büchner, and Tamoni (2021), "Bond Risk Premiums with Machine Learning," *Review of Financial Studies* 34(2): 1046–1089, DOI 10.1093/rfs/hhaa062, and the corrigendum with Hoogteijling, *Review of Financial Studies* 34: 1090–1103, DOI 10.1093/rfs/hhaa098.
- Gu, Kelly, and Xiu (2020), "Empirical Asset Pricing via Machine Learning," *Review of Financial Studies* 33(5).
- Bali, Goyal, Huang, Jiang, and Wen (2020), "Predicting Corporate Bond Returns: Merton Meets Machine Learning," Swiss Finance Institute Working Paper 20-110, SSRN 3686164.
- Kelly, Palhares, and Pruitt (2023), "Modeling Corporate Bond Returns," *Journal of Finance* 78(4): 1967–2008, DOI 10.1111/jofi.13233.
- Feng, He, Wang, and Wu (2025), "Predicting individual corporate bond returns," *Journal of Banking & Finance* 171, 107372.
- Bell, Kakhbod, Lettau, and Nazemi (2026), "Glass Box Machine Learning and Corporate Bond Returns," *Journal of Financial Economics* 181, DOI 10.1016/j.jfineco.2026.104294: https://www.nber.org/papers/w33320
- Jostova, Nikolova, Philipov, and Stahel (2013), "Momentum in Corporate Bond Returns," *Review of Financial Studies* 26(7).
- Barter, Gao, Christodoulaki, Chen, and Cartlidge (2025), the BondBERT paper, arXiv:2511.01869: https://arxiv.org/abs/2511.01869v2
- Title only: Kelly, Malamud, and Zhou (2024), "The Virtue of Complexity in Return Prediction," *Journal of Finance*, read with Nagel (2025), "Seemingly Virtuous Complexity," as the critique; van Binsbergen, Nozawa, and Schwert, "Duration-Based Valuation of Corporate Bonds," *Review of Financial Studies*.

**Data & Code**

- Open Bond Asset Pricing (Dickerson and coauthors): daily and monthly TRACE panels, the 108-signal zoo, and corrected Bai–Bali–Wen factors: https://openbondassetpricing.com/ . The authors' companion Python package is reported to be distributed on PyPI as PyBondLab (search by name).
- Dickerson–Mueller–Robotti replication package, Mendeley Data, DOI 10.17632/n66rp59tr7.2: https://data.mendeley.com/datasets/n66rp59tr7
- FINRA, TRACE historic data file layout, including the `As Of Indicator` reversal flag that fooled Kaz in §7.9: https://www.finra.org/filing-reporting/trace/historic-data-file-layout-post-2612-files
- FRED, ICE BofA option-adjusted spreads for US high yield, US corporates, and CCC and lower: https://fred.stlouisfed.org/series/BAMLH0A0HYM2 , https://fred.stlouisfed.org/series/BAMLC0A0CM , https://fred.stlouisfed.org/series/BAMLH0A3HYC
- SIFMA, US corporate bond statistics (volume, issuance, amount outstanding): https://www.sifma.org/resources/research/statistics/us-corporate-bonds-statistics/
- Open Source Asset Pricing (Chen and Zimmermann): the equity-side model for a public, reproducible signal zoo (title only).
- This book: Appendix B for point-in-time TRACE and pricing-composite feeds, and the reference implementation in §7.12.

<!-- STATUS: COMPLETE -->
