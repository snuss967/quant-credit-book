# Chapter 6-B: Options for Credit People: Replication, Black–Scholes, Greeks, Jump-to-Default and the Two Measures

> **Prerequisites.** Itô's lemma and the volatility tax (§6.1); the Merton payoff and the closed forms it produces (§6.2, where they are stated and then used); default as a surprise with an intensity (§6.6). Spread duration and CS01 come from Chapter 4-B. Nothing else. Chapter 6 already owns the gentle explanations of distributions, random walks, Itô's $\tfrac12\sigma^2$, "risk-neutral" in plain words, Girsanov for a Brownian motion, hazard rates and the Poisson clock, and Chapter 4-B owns "an implied number is a question asked backwards"; this chapter glosses each in a sentence and points back. Read it after Chapter 6 and before Chapter 7. Every later chapter that prices an option, quotes a hazard or says "$\mathbb{Q}$" points back here.

## Cold Open: Vega on a Book With No Options

*Live, Monday 12 October 2026, the Monday after Chapter 1's lender call. The desk, Theo's book and every number on its risk report are fictional and illustrative.*

*Monday, 7:12 a.m.* Theo's first risk report has eleven columns, and he understands eight of them. Market value, he knows. DV01 and CS01 he learned in his first week, from Chapter 4-B and from Kaz, in that order of patience. DTS, carry, roll-down, the index beta and the sector bucket he could have explained to a client at his old job, if any client had asked. The ninth says **VEGA (per vol pt): −\$41k**. The tenth says **JTD: −\$6.3mm**. The eleventh says **MEASURE: Q**, in a font that suggests it has been shouted before.

"Who sold options in my book?" he asks. His book is forty-one high-yield bonds and a short CDX hedge. He has never sold an option. He has barely bought lunch.

"You did," Ines says, without looking up. "Every bond you bought. A high-yield bond is a short put that pays a coupon. You wrote forty-one of them. Vega is the risk system telling you that it noticed."

Kaz is already at the whiteboard, writing $V_0N(d_1)-Fe^{-rT}N(d_2)$ with the speed of someone who has written it four thousand times and been asked what it means twice. "It's just Black–Scholes on the firm," they say. "Assume the assets are lognormal and tradeable."

"Then show me where forty-one thousand dollars comes from," Theo says. "One line. Not the theory."

Kaz sorts the report by the ninth column and points at the top row. Twenty million face of a double-B industrial, the bond the desk's structural model maps onto the §6.2.4 firm: assets of 100 against debt of 80, asset volatility 25%, one year, a 216 bp spread. "Bond vega on that firm is minus 0.199 points per asset-vol point, per 100 face. You own two hundred thousand hundreds of face." They write it underneath the formula: $-0.199\times200{,}000=-\$39{,}800$. "That's ninety-seven percent of your number, from one bond."

"And the other forty?"

"Short vol, every one of them, the way a short put is. But you bought index protection last Tuesday, and bought protection is a long put on the same assets, so it's long vol. Forty bonds and one hedge net to about minus twelve hundred dollars." Kaz shrugs. "Nobody sized it to do that. You sized the CDX to your spread risk, and it quietly cancelled your vol risk on the side."

Theo looks at the column again. "So my vega is one bond."

"Your vega is one bond and a coincidence," Kaz says. "Coincidences don't roll."

Theo's hand goes to his pocket, where the USB stick with his 13-week cash flow model lives, for emotional support. The model has a row for every receipt and every disbursement a client's treasurer could name, a revolver availability line, a minimum-liquidity covenant shaded red, and not one cell anywhere that asks how *uncertain* any of it is. At his old job the uncertainty was the client's problem, solved by a range of three cases on page four. Here it is a number in the ninth column with a minus sign, and it has a dollar unit, and somebody will ask him about it at the 8:00 risk meeting. He writes on his pad, under the date: *vega = one bond + one accident*.

"You cannot short a factory," Mags says. "In 1994 we measured vega by calling the guy who sold us the bonds and asking whether he sounded nervous. One parameter, and he answered the phone."

ROBO, asked on Friday to "remove the vega from Theo's book," had produced a one-line execution plan: sell all forty-one bonds. Vega: zero. Carry: zero. Theo: horrified. ROBO, as always, did exactly what was asked.

Nobody had read the plan's second line. Ines scrolls to it now and reads it aloud, in the flat voice she uses for hand histories. "*Residual JTD: \$0. Residual carry: \$0. Residual Theo: not modelled.*"

"That's the most honest risk report on the floor," Mags says. "It knows what it doesn't measure."

"It measured the jump, though," Theo says, pointing at the tenth column on his own report. "Minus six point three million. What is that a derivative of?"

"Nothing," Ines says. "That's why it's the only line I read first. Hold the thought until a week from Wednesday." She means a replay; she does not say which, and Theo has learned not to ask.

"But what does the credit agreement say?" Theo asks, because that is what he asks.

"It says you are short a put to the shareholders," Ines says. "And everything else on your book is an option of some kind, written by a lawyer who did not use the word. Price them." (She does, instrument by instrument, in §6-B.7.)

Theo looks at the eleventh column. "And which probabilities do I use? Mine, or the market's?"

Nobody answers immediately, which on this desk is how you know a question is good. Kaz caps the marker. Mags goes back to her screen. Ines writes something on a sticky note, folds it in half and puts it in her drawer, which Theo will learn is where she keeps answers she wants him to find on his own.

**If every instrument on a credit desk is an option, where is the one page that shows how to price one, what each risk-report line means, what happens when the underlying can jump to zero, and whose probabilities go into the expectation?**

This chapter builds that page, from the hockey stick to the hazard multiplier, through two replays (Wolfspeed's 2025 restructuring and SVB's March 2023) and one Monday afternoon on Halvorsen. By the end you will be able to price any credit payoff by replication, read every line of the risk report including the one that is not a derivative, add a jump to default, change measure for an intensity, and say which measure every number you hand anyone is in.

## 6-B.1 Payoffs First: The Hockey Stick Is the Atom

### 6-B.1.1 Desk framing: every document is a payoff function

RSSG trained Theo to read a waterfall: who gets paid, in what order, from what pot. An options desk reads the same thing as a function $g(\cdot)$ from a terminal value to a cash flow. Once you can write $g$, pricing is a separate and much more boring problem, and most credit-desk errors happen at the first step: the wrong $g$, written from the summary of the indenture instead of the definitions (Law 8, App E). How literal that is became visible in June 2025, when a restructuring support agreement rewrote a listed stock's $g$ overnight while the ticker kept trading as if nothing had happened; §6-B.1.5 replays the evening.

Three atoms build every payoff in this book. Let $S_T$ be the value of some underlying at date $T$: a share price, a firm's asset value $V_T$, a post-close bond price, a pool's adjusted par.

$$
\underbrace{(S_T-K)^+}_{\text{call}},\qquad \underbrace{(K-S_T)^+}_{\text{put}},\qquad \underbrace{\mathbf 1_{\{S_T>K\}}}_{\text{digital}},\qquad x^+\equiv\max(x,0).
$$

**Notation for this chapter.** The style bible gives $P$ to the bond price and $S_t$ to a generic underlying. Option values are therefore written $C$ (call), $\text{Put}$ (put) and $\text{Dig}$ (digital), with arguments when they matter: $\text{Put}_{\text{BS}}(S_0,K,T,\sigma,r)$. Survival probabilities always carry their measure as a superscript, $S^{\mathbb{Q}}(T)$ or $S^{\mathbb{P}}(T)$, so they cannot be confused with $S_t$. The letter $q$ stays reserved for inventory; we assume no dividends, and where a dividend matters we say so in words. Merton's debt claim is $B_t$, as in §6.2.

### 6-B.1.2 Put–call parity: the only theorem that needs no model

> **Math, Gently.** *Two lunchboxes.* Pack one lunchbox with a call struck at $K$ and enough cash to grow into $K$ by expiry, which today is $Ke^{-rT}$. Pack the other with a put struck at the same $K$ and one share. Open both at $T$. If the share finished above $K$, the first box holds a call worth $S_T-K$ plus $K$ of cash, which is $S_T$; the second holds a worthless put and a share worth $S_T$. If the share finished below $K$, the first box holds a dead call and $K$; the second holds a put worth $K-S_T$ and a share worth $S_T$, which is $K$. Every state, same contents. Whoever charges more for one box than the other gets arbitraged by lunchtime. *A number you can check in the margin:* $S_0=100$, $K=100$, $r=4\%$, $T=1$. The cash today is $100e^{-0.04}=96.08$, so call minus put must be $100-96.08=3.92$. If the call is 13.75, the put must be 9.83, whatever anyone thinks the stock will do. No volatility, no distribution and no drift went into that; no model was used, which is why this is the first test in every engine (§6-B.9).

The identity $(S_T-K)^+-(K-S_T)^+=S_T-K$ holds in every state of the world, so a call minus a put is a share minus $K$ in cash at $T$. With a constant riskless rate $r$ and no dividends,

$$
C(K)-\text{Put}(K)=S_0-Ke^{-rT}.
$$

When a call and a put in a desk's data disagree with it, the desk has learned something about its code or its data, never about the market. (Listed single-stock options are American and pay attention to dividends and borrow. Parity then becomes a pair of inequalities, and the size of the violation is how §23.4 backs out the borrow fee.)

### 6-B.1.3 Digitals, and the density hidden in the strike axis

> **Math, Gently.** *$\mathbb{Q}$ is the second derivative of the price list.* Buy one call struck at 90, sell two at 100, buy one at 110. Draw the payoff at expiry and you get a tent: zero below 90, rising a dollar for every dollar the stock climbs to a peak of 10 at exactly 100, falling back to zero at 110, and zero above. This butterfly is a bet that the stock lands *near 100* and nowhere else. Now read three prices off a screen, say calls at 14, 8 and 4 *(illustrative)*. The butterfly costs $14-2\times8+4=2$. Divide by its peak payout of 10 and you have the price of a claim that pays about a dollar if the stock finishes in a ten-dollar bin around 100: 0.20. Undo the discounting and that is, near enough, the market's probability of the bin, 20%, read off three prices and no beliefs. Slide the tent along the strike axis and you map the whole distribution, one bin at a time; shrink its wings and you get a density. Nobody's forecast, utility function or mood went into it. **$\mathbb{Q}$ is not a belief. It is the second derivative of the price list.** The formula is next.

Differentiate the call payoff in its strike: $\partial_K(S_T-K)^+=-\mathbf 1_{\{S_T>K\}}$. Take expectations under any pricing rule that is linear and discounts at $r$:

$$
\text{Dig}(K)=e^{-rT}\,\mathbb{Q}(S_T>K)=-\frac{\partial C}{\partial K},\qquad \frac{\partial^2C}{\partial K^2}=e^{-rT}f^{\mathbb{Q}}(K),
$$

where $f^{\mathbb{Q}}$ is the density of $S_T$ under the pricing measure. The second identity is Breeden and Litzenberger (1978), and it is the butterfly in the box with its wings shrunk to nothing and its price divided by the width squared: the cleanest definition of $\mathbb{Q}$ a desk will ever get. Calls at every strike give the whole risk-neutral density, with no assumption about anybody's utility function.

Two consequences. A digital is the limit of a tight call spread, $\big[C(K-\epsilon)-C(K+\epsilon)\big]/(2\epsilon)$, so its gamma is unbounded at the strike near expiry, which is why portability (§15.3) and every other pass-or-fail clause is hard to hedge. And a probability extracted from prices is a $\mathbb{Q}$ probability, always (§6-B.6).

### 6-B.1.4 The capital structure as a ladder of call spreads

Here is the restructuring banker's waterfall, written as an options book. Let a firm have assets $V_T$ at $T$ and debt tranches $j=1,\dots,J$ ordered from senior to junior, with face values $F_j$. Define attachment points $a_1=0$ and $a_{j+1}=a_j+F_j$, so total debt is $a_{J+1}$. Under absolute priority, tranche $j$ receives

$$
\min\!\big((V_T-a_j)^+,\,F_j\big)=(V_T-a_j)^+-(V_T-a_{j+1})^+,
$$

a call spread on the assets struck at its attachment and detachment points. Equity receives $(V_T-a_{J+1})^+$, a plain call struck at total debt. Sum the payoffs: the sum telescopes to $(V_T-0)^+=V_T$. The capital structure distributes the firm and nothing else, which is the conservation law Chapter 13's waterfall engine enforces (§13.7).

```text
Figure 6-B.1  The capital structure as a ladder of call spreads (payoff at T against asset value V_T)

payoff
  |                                                         equity: call struck at a4
  |                                                       /
  |                                                     /
  |                                  junior: call spread [a3,a4]
  |                         ________________________/ 
  |                        /                       
  |      senior unsecured: call spread [a2,a3]     
  |              _________/                         
  |             /                                    
  |   1L: call spread [0,a2]                         
  |___/________|_________|_____________|______________ V_T
  0           a2        a3            a4
                        ^ plan value lands here: the [a3,a4] tranche is the fulcrum
```

Price each call with any model you like and the tranche values follow: $\text{value}_j=C(a_j)-C(a_{j+1})$, with $C(0)=V_0$. In Merton's lognormal model this is the §6.2.3 formula applied tranche by tranche. Chapter 23 calls the same picture "one distribution, many strikes" (§23.1).

RSSG teaches what falls out of the ladder by experience: where the fulcrum sits, why seniority is moneyness, which tranches are long volatility and which are short it. Those three readings are easier to watch on a real stack, on the evening a document moved its strikes, than to memorize as a list, so §6-B.1.5 deals them one at a time on Wolfspeed. Kaz, who once asked whether the fulcrum was "the tranche that does the most leverage," will turn out there to have been accidentally half right.

Used in: §6.2.1 (Merton's two-tranche case), §8.3, §13.3, §13.7, §15.3, §16.3, §21.4, §23.1.

### 6-B.1.5 Long Scene: Wolfspeed, 23 Jun 2025, one distribution and four strikes

*A replay. The desk's cards and all dialogue are fictional, and nobody on the desk held Wolfspeed paper in 2025. Every Wolfspeed fact is from the company's 8-Ks, its FY2025 and FY2026 10-Ks and its disclosure statement; the stock prints are from the press reports and market-data vendors named where they appear; calculations are marked (calc).*

Tuesday 20 October 2026, 4:45 p.m. Ines puts a folder on the table the way she puts down a coffee, like a chip. The tab says *Cut: close, Mon 23 Jun 2025*. The rules are the usual ones: you know what was public at the cut and nothing after it, you write your card before she opens the next folder, and a card executes at the first print after it was written, not at the last one before.

"One exception tonight," she says. "Two numbers from the future, because tonight is about the shape of a payoff and not its level, and I don't want to watch Kaz value a chip company for an hour." She writes them on the whiteboard and boxes them: *43.56mm new shares. Plan equity value \$959.4mm, so \$22.02 a share* (calc, from the FY2026 10-K). Everything else in the folder is dated on or before the cut.

**The stack.** Theo reads it aloud, from the balance sheet as the next 10-K would print it six days later, which Ines allows because no face amount on it changed in those six days. Senior Secured Notes due 2030, \$1,521.2mm, paying 9.875% plus 2% in kind. Three convertible issues, all unsecured: 1.75% due 2026, \$575mm, convertible at about \$47.32 a share; 0.25% due 2028, \$750mm, at about \$127.22; 1.875% due 2029, \$1,750mm, at about \$118.88. Renesas's deposits, \$2,062mm, unsecured and ranking with the converts. Total debt \$6,658.2mm; cash and short-term investments \$955.4mm, down \$1.22bn in a year.

The path is in the next three pages. On 28 March 2025 an out-of-court exchange failed and the stock fell about half, to \$2.59, a market capitalisation of about \$400mm. On 2 June the company did not pay the interest due on the 2029 converts and entered the 30-day grace period. On 22 June it signed a restructuring support agreement with holders of more than 97% of the secured notes, and the press release, dated that Sunday, said what everyone got: the converts and Renesas would exchange about \$5.2bn of claims for \$500mm of new notes and 95% of the new common equity, and existing shareholders would receive "their pro rata share of 3% or 5% of new common equity," subject to dilution and "potential reduction from certain events." By Monday afternoon the stock was about a third lower, near 60 cents (press reports that day put it at 60 cents, down 33 to 34 per cent).

Theo goes to the whiteboard and draws the ladder of §6-B.1.4 with real attachment points, in \$mm: the secured notes on the rung $[0,\,1{,}521]$; the converts and Renesas, pari passu, sharing one wide rung $[1{,}521,\,6{,}658]$; the old equity, a call struck at 6,658.

**The first thing that falls out.** "The converts are convertible into stock at forty-seven, a hundred and nineteen and a hundred and twenty-seven dollars," Theo says. "In March the stock was two fifty-nine. Those strikes were eighteen, forty-six and forty-nine times spot (calc). Their own call on the stock is worthless. They're not convertibles any more. They're recovery claims with a CUSIP." He circles the wide rung. "And this is where the value lands. Whatever the company is worth, it's more than the secured notes and much less than six and a half billion. So the unsecured rung is the at-the-money call spread. It's the fulcrum."

"The tranche that does the most leverage," Kaz says, pleased.

"The tranche whose price moves most when the valuation fight moves," Ines says. "Which is a kind of leverage, so you get half a point." The rungs above and below the money barely move: the secured notes are paid almost whatever the company is worth, and the old equity, a call struck at \$6.66bn on a firm worth perhaps a third of that, is too far out of the money to have a delta. (The 10-K's fair values as of 29 June would put the three convert issues at 26% of principal, and the disclosure statement filed that week would estimate their recovery at 25% to 30%. Ines shows neither yet.)

**The second thing.** Kaz has been pricing the old stock all afternoon as a Merton call on the firm, struck at total debt, and has a number to four decimal places. Mags takes the RSA out of the folder and puts it on top of Kaz's printout.

"The document wrote the payoff," she says. "That stock isn't a call on anything. It's a coupon for two point one eight million new shares and a lottery ticket on a government committee."

This is the ladder's second lesson, and it is the one a restructuring banker knows in his bones and a model does not: *seniority is moneyness, and a restructuring support agreement moves the strikes.* The RSA does not wait for the firm's value to fall below the equity's strike. It abolishes the strike. The plan fixes one pie of new stock and cuts it by document. The exit 8-K would later print the slices to the share: 24,533,760 new shares to the converts and 1,306,896 to the old equity on the effective date, with 871,287 more to the old equity and 16,852,372 to Renesas once the Committee on Foreign Investment in the United States cleared Renesas's stake. On 43.56mm shares, 1,306,896 is the RSA's 3% and the two slices together are its 5% (calc). An uptier does the same thing by inserting a rung at the bottom of the ladder and pushing everyone's attachment points up by its face (§13.3); a drop-down does it by removing assets from $V_T$ for some rungs and not others (§13.6). Here the document went further and replaced the old equity's call with a fixed number of shares in a company that did not exist yet.

Theo does the arithmetic on the board. Old shares outstanding, 156.48mm. With the committee's clearance, the old equity gets 2,178,190 new shares; at about \$22 that is \$48mm, or 31 cents an old share. Without it, 1,306,896 shares, \$29mm, 18 cents. The difference, the committee's slice, is a digital: if the committee clears Renesas by the deadline, each old share gets 0.005568 more new shares, about 12 cents at plan value; if it does not, nothing (calc).

**The third thing.** "At sixty cents," Theo says, "the market is paying ninety-four million dollars for a payoff the document values at forty-eight. Twice."

"Tag the rungs for vega," Ines says. "Plus or minus."

He does it slowly, because it is the reading that took him longest at his old job, where nobody called it vega. A call spread is convex near its lower strike and concave near its upper one, so every rung is long volatility below its midpoint and short above it. The secured rung, whose lower strike is zero, is all concavity: short volatility everywhere, which is why secured lenders hate surprises in both directions. The equity is all convexity: long volatility everywhere. The middle rungs flip sign as the firm deteriorates, and Wolfspeed's unsecured rung, with the value landing not far above its lower strike, had flipped: it was long volatility, like equity, which is the structural reason a CCC bond starts to trade like stock (§8.3). Ninety-five per cent of the new company's shares were about to go to that rung. The converts were becoming the stock in the most literal way a document can arrange.

"And the old stock?" Ines asks.

Theo looks at the plus sign he has just written next to it, and crosses it out. "Before Sunday it was the all-convexity rung. Since Sunday it's 0.008352 of a share that doesn't exist yet, plus 0.005568 if a committee says yes. Its vega is whatever the new stock's vega turns out to be, times a very small number, plus a digital." He writes $g$ in the chapter's atoms:

$$
g(\text{old share})=0.008352\,S^{\text{new}}_{T_1}+0.005568\,S^{\text{new}}_{T_2}\,\mathbf 1_{\{\text{clearance by the deadline}\}},
$$

with $T_1$ the effective date and $T_2$ the day the committee rules.

#### The card: a payoff function that a document wrote

Ines slides three index cards across the table. *Write three things: the old stock's payoff function after the RSA, in this chapter's atoms; what you do about it, and in what size; and what kills it.*

Kaz writes fast. *Short the stock against the converts, sized by the Merton delta. The model says the equity is overpriced by an order of magnitude.*

Mags writes one line. *Price is what you pay; there is nothing to borrow. No trade.*

Theo writes the longest card, as usual. *(1) A forward on 0.008352 new shares plus a digital on the committee worth 0.005568 more. (2) Short the stock, small: a size where a recall that forces me to buy back at double the price costs less than a day's P&L. (3) Kills it: a plan that fails to confirm, because then the old stock is a call again.*

What would you write? The reader's card is graded with the others, against what happened.

**The grade.** Ines opens the next folders one at a time. The company filed a prepackaged Chapter 11 in Houston on 30 June. The court confirmed the plan on 8 September, day 70. On 29 September the plan went effective, the old shares were cancelled, and each became 0.008352 of a new share. The new stock opened at \$18.00, traded as low as \$8.05 and closed at \$22.10, against the plan's \$22.02 (market-data vendor prints; Chapter 16 notes that vendors differ slightly on that day's opening and closing prints). On 29 January 2026 the committee cleared Renesas, and the old equity's 871,287 contingent shares were released, 0.005568 more per old share. (The new stock had closed 2025 at \$17.41, vendor close; the folder holds no January print.)

Theo's payoff function was right to the share. Valued at the first day's close and at that year-end price, the old share delivered about $0.008352\times22.10+0.005568\times17.41\approx\$0.28$ (calc), against 60 cents on the day of the card. The short made about half its proceeds before the cost of borrowing, and the FY2025 10-K's price range for the year to 29 June shows a closing low of \$0.41, so the market came part of the way to the document within a week. Full marks on line one, most of the marks on line two. Line three is where Ines stops.

"The plan confirmed," she says. "So your kill didn't happen. What nearly killed you is a line you didn't write."

She turns the last page in the folder. A short in a share the plan cancels does not end on the effective date; under a standard lending agreement the borrower owes the lender whatever the share would have received (Chapter 16 runs the same mechanics on Hertz). So Theo's short at 60 cents was, on 29 September, a short of 0.008352 of a brand-new stock with no trading history, whose first day's range ran from \$8.05 to \$22.10. Buying the slice back cost anywhere from about 7 cents an old share to about 18.5 cents, depending on the minute (calc). The committee slice arrived in January as a second short, in a stock that had closed the year at \$17.41. And had the short simply been left on, the way shorts on a wound-down company sometimes are, the arithmetic by 26 May 2026, when the new stock closed at \$73.50, would have been $0.013920\times73.50\approx\$1.02$ owed for every old share sold at 60 cents (calc, vendor close).

"The payoff function was right on 23 June," Ines says, "and the position was still a hand you could lose. A correct $g$ tells you nothing about the path of the thing $g$ is a function of, and after Sunday that thing wasn't the firm. It was a stock nobody had seen. Your card said what you'd owe. It didn't say in what, or when you'd stop owing it."

Kaz's card gets the same grade for direction and a lower one for reasoning. The Merton call was struck at \$6.66bn and the document had replaced the strike with a share count; its delta described an instrument that no longer existed, and the short it sized was right by accident. "The model priced an option somebody had already exercised," Ines says. "That's not a model error. That's a reading error." Kaz writes *read the RSA first* on a sticky note and puts it, for reasons nobody asks about, on Mags's monitor.

Mags's card cannot be graded, and Ines says so. The folder has no borrow tape for June 2025, and the desk does not invent fees for stocks in the week of their restructuring. "But you're the only card that wrote down a cost," Ines tells her. "Everyone else priced the payoff and forgot the rent." Mags accepts this as her due.

**The coda.** Ines leaves the last page face up. On 26 March 2026 the reorganized company sold a 1.5-lien convertible, convertible at about \$20.14 a share, and inserted it between the first and second liens, so the post-emergence stack carries four strikes on one new stock: the second-lien converts at about \$12.23, Renesas's second-lien converts at about \$18.35, the new 1.5-lien convert at about \$20.14 and Renesas's warrant at \$23.95, all around a plan value of \$22.02 (exit and March 2026 8-Ks; calc). Two months later the stock was \$73.50, 3.3 times plan value. Four strikes, one distribution: the picture Chapter 23 calls "one distribution, many strikes" (§23.1), drawn by a plan and its aftermath instead of by an options exchange.

<!-- FIGURE: ch06b_wolfspeed_strikes.png (payoff diagram over new-stock value: conversion/exercise prices 12.23, 18.35, 20.14, 23.95 around the 22.02 plan value; 29 Sep 2025 open 18.00, low 8.05, close 22.10 and 26 May 2026 73.50 marked; source WOLF §3.2–3.3) -->

Theo asks the question Ines was waiting for. "Where's the put chain? Why are we pricing this ladder from documents?"

"Because there wasn't one we could use," she says. The desk's archive has no Wolfspeed CDS series and no option-chain data it trusts for that summer; the research behind this replay found neither, an evidence gap that vendor data would close. When nothing that pays at default trades, the ladder is priced from the documents or not at all, and that is most of high yield. The dated docket is Chapter 13-B's Wolfspeed Docket Diary, the morning the new stock first traded opens Chapter 16, and Chapter 23 reads the converts as the fulcrum from the convertible desk's side. The lesson for this chapter is the first one in it: every document is a payoff function, and on the evening of 23 June 2025 a document rewrote one while the ticker kept trading as if it had not.

## 6-B.2 Replication: One Hedge Ratio, No Opinion About the Drift

### 6-B.2.1 Desk framing: the price of an option is the cost of the factory that makes it

Ines: "You don't price a hand by guessing the river. You price it by what it costs to make the same hand from the cards on the table." A dealer who sells a call needs no view on the stock, only a recipe that turns shares and cash into the call's payoff in every state; the recipe's cost *is* the price. Theo's thirteen-week model plays no part. Replication does not care what you think, only what you can trade.

### 6-B.2.2 One period, two states, and the probability that is a ratio of prices

> **Math, Gently.** *The factory, in two parts.* **Part one: a probability that is a ratio of prices.** A stock is at 100. Tomorrow it will be 120 or 90, nothing else, and money earns nothing overnight ($u=1.2$, $d=0.9$, $r=0$). You are asked to sell a call struck at 100, which pays 20 in the up state and 0 in the down state. Instead of guessing, build the call from parts. Buy $\Delta$ shares and borrow $b$, so that $120\Delta-b=20$ and $90\Delta-b=0$. Subtract: $30\Delta=20$, so $\Delta=2/3$ of a share and $b=60$. The kit costs $\tfrac23\times100-60=6.67$, and it pays exactly what the call pays in both states. So the call costs 6.67. Now notice that $6.67=\tfrac13\times20+\tfrac23\times0$: the price is an average of the payoffs with weight $\tilde q=(1-0.9)/(1.2-0.9)=1/3$ on the up state. Tell me the up-move is 90% likely and I still charge 6.67, because I am not betting, I am manufacturing; the 1/3 came out of three prices, not out of anybody's forecast. **Part two: the factory in continuous time.** Rebalance the same recipe every instant instead of once, and the cost of the kit obeys the Black–Scholes equation of §6-B.2.3. The factory still has an operating margin, though. It was built assuming a certain amount of wiggle, the implied volatility $\sigma_i$; if the world wiggles more or less, the hedger who owns the option collects or pays a rent of $\tfrac12\Gamma S^2(\sigma_r^2-\sigma_i^2)$ per year, the equation of §6-B.2.4. A tiny number: dollar gamma $\Gamma S^2=2{,}000$ *(illustrative)*, realized volatility 40% against 30% implied. The rent is $\tfrac12\times2{,}000\times(0.16-0.09)=1{,}000\times0.07=70$ a year, about 28 cents a trading day, collected one rebalance at a time. The general recipe is next.

Let the underlying be worth $S$ today and either $uS$ or $dS$ after one period of length $\Delta t$, with $d<e^{r\Delta t}<u$ (otherwise one of the assets dominates the other and there is an arbitrage). A claim pays $C_u$ or $C_d$. Buy $\Delta$ units of the underlying and invest $b$ in the riskless asset, and choose them so the portfolio pays the claim in both states:

$$
\Delta\,uS+b\,e^{r\Delta t}=C_u,\qquad \Delta\,dS+b\,e^{r\Delta t}=C_d.
$$

Subtracting, $\Delta=(C_u-C_d)/\big((u-d)S\big)$. Substituting back and writing the cost $C_0=\Delta S+b$,

$$
C_0=e^{-r\Delta t}\Big[\tilde q\,C_u+(1-\tilde q)\,C_d\Big],\qquad \tilde q=\frac{e^{r\Delta t}-d}{u-d}\in(0,1).
$$

The physical probability $p$ of the up state never enters. The weight $\tilde q$ lies between 0 and 1 and the weights sum to 1, so pricing *as if* it were a probability and discounting at $r$ gives the right answer, which is all a risk-neutral probability is (the box's 1/3; Chapter 6's box says the same thing in plain words). Cox, Ross and Rubinstein (1979) turned this one-period argument into the binomial tree.

**The credit version, and the fix §3.1 needs.** Replace the share with a one-period zero-coupon bond that pays 100 if the issuer survives and $R$ (in points) if it defaults. If it trades at $P_0$,

$$
P_0=e^{-r\Delta t}\Big[(1-\pi^{\mathbb{Q}})\,100+\pi^{\mathbb{Q}}R\Big]\quad\Longrightarrow\quad \pi^{\mathbb{Q}}=\frac{100-P_0e^{r\Delta t}}{100-R}.
$$

At $P_0=90$, $r=4\%$, $\Delta t=1$ and $R=40$, $P_0e^{r\Delta t}=93.67$ and $\pi^{\mathbb{Q}}=6.33/60\approx10.5\%$ *(illustrative)*. This is the default probability *implied by the price*, not the one Theo believes after reading the 10-Q. The two-point bond of §3.1 reads correctly this way: priced under $\mathbb{Q}$, then forecast under $\mathbb{P}$, with the gap between $\pi^{\mathbb{Q}}$ and Theo's $\pi^{\mathbb{P}}$ being the premium of §6-B.6 rather than an inconsistency.

### 6-B.2.3 Continuous time: delta hedging and the Black–Scholes PDE

Section 6.2.2 ran the delta-hedging argument for Merton's equity $E(t,V)$. Here is the general version, with one addition that matters more to a trader than the PDE itself.

Let the underlying follow $dS_t=\mu S_t\,dt+\sigma S_t\,dW_t$ under $\mathbb{P}$, and let $f(t,S)$ be a claim paying $g(S_T)$. Hold the claim and short $\Delta$ units of the underlying, $\Pi=f-\Delta S$. Itô's lemma (§6.1) gives

$$
d\Pi=\Big(f_t+\mu Sf_S+\tfrac12\sigma^2S^2f_{SS}-\Delta\mu S\Big)dt+(f_S-\Delta)\,\sigma S\,dW_t .
$$

Set $\Delta=f_S$. The noise disappears, so $\Pi$ is riskless and must earn $r$: $d\Pi=r(f-Sf_S)\,dt$. The $\mu$ terms cancel, leaving the Black–Scholes PDE

$$
f_t+rSf_S+\tfrac12\sigma^2S^2f_{SS}-rf=0,\qquad f(T,S)=g(S).
$$

The Feynman–Kac theorem turns the PDE into an expectation. The solution is

$$
f(t,S)=e^{-r(T-t)}\,\mathbb{E}^{\mathbb{Q}}\big[g(S_T)\mid S_t=S\big],\qquad dS_t=rS_t\,dt+\sigma S_t\,dW^{\mathbb{Q}}_t,
$$

which is the continuous-time version of the binomial weights: price as if the underlying grew at $r$, then discount at $r$. The drift that Theo would spend a week estimating appears nowhere.

### 6-B.2.4 The gamma rent: what a hedged option actually earns

The PDE assumes the hedger knows $\sigma$. Nobody does. Suppose a dealer sells a claim priced at implied volatility $\sigma_i$, hedges with the delta computed at $\sigma_i$, and the underlying then realizes volatility $\sigma_r$, so that $(dS)^2=\sigma_r^2S^2\,dt$. The dealer is long the hedge and short the claim; take the mirror image, a trader long the claim and short $\Delta=f_S$, with $f$ evaluated at $\sigma_i$. Itô gives

$$
d\Pi=f_t\,dt+\tfrac12f_{SS}\,\sigma_r^2S^2\,dt .
$$

The PDE at $\sigma_i$ says $f_t=rf-rSf_S-\tfrac12\sigma_i^2S^2f_{SS}$. Substituting, and writing $\Gamma=f_{SS}$,

$$
d\Pi-r\Pi\,dt=\tfrac12\,\Gamma S^2\big(\sigma_r^2-\sigma_i^2\big)\,dt .
$$

This is the most useful equation in options trading, and it is why traders talk about volatility instead of prices. A delta-hedged long option earns, every instant, half its dollar gamma times the gap between realized and implied *variance*. Long gamma means you are paid when the underlying moves more than the price assumed; short gamma means you collect a rent when it moves less. In practice the rent is collected in discrete hedges, so the realized P&L is path-dependent, and the dollar gamma $\tfrac12\Gamma S^2$ is largest exactly when the underlying sits near the strike close to expiry. Figure 6-B.2 shows where the rent is earned and how its sign follows realized minus implied volatility.

![Figure 6-B.2: The gamma rent is earned where and when the underlying sits near the strike: if realized volatility is 40% against 30% implied, a one-week option earns about nine cents a day and a one-year option about one cent (left), and a delta-hedged option's P&L crosses zero where realized volatility equals implied (right). Illustrative: Black–Scholes at 30% implied volatility and 4% rates, strike 100; the right panel hedges a three-month at-the-money call daily along 20,000 simulated lognormal paths.](assets/figures/ch06b_gamma_rent.png)

Now translate. A Merton bondholder is short a put on the firm (§6.2.1), so a hedged bondholder is short gamma on the assets: paid a rent when assets are calmer than the spread implied, billed $\tfrac12\Gamma V^2(\sigma_r^2-\sigma_i^2)$ when they are not, with $\Gamma$ largest near the default point. That is the precise sense in which "high yield is a short put that pays a coupon" (§11.1): the coupon is the rent and the bad weeks are the gamma bill.

> **[SOURCE EXTRACTION]** *Veronesi_Fixed_Income_Securities p.611:* "If the model is correct, then at maturity [$T_O$] the replicating portfolio will deliver exactly the payoff of the option we sold today."
>
> **Annotation.** Veronesi's setting is an option on a zero-coupon Treasury, hedged dynamically with bonds; the replication logic is identical to ours, and the load-bearing words are the first five. "If the model is correct" covers three assumptions that fail in credit, in increasing order of severity. Volatility is not known: the gamma-rent equation above says exactly what that costs. Rebalancing is not continuous: a high-yield bond trades a few times a day at a half-point bid–ask, so the hedger rebalances on bands and carries the residual. And the underlying can jump, which no amount of delta replicates (§6-B.5). The 2026 desk keeps the replication argument as the *definition* of a fair price and treats every failure of its assumptions as a separately reported risk line (§6-B.3).

### 6-B.2.5 The Black–Scholes formula, and the two probabilities of one event

> **Math, Gently.** *Two probabilities of one event.* Ask two accountants how likely it is that a one-year call struck at 100 finishes in the money, and tell one to keep the books in dollars and the other in shares. The dollar accountant weights every path the same way the risk-neutral measure does. The share accountant has a quirk: a path on which the stock ends at 150 is, to her, a path on which a share is worth half again as much, so she counts high-stock paths more heavily than low-stock ones. Both are doing correct arithmetic about the same event and they disagree, because they are counting in different currencies. *A tiny number:* $S_0=K=100$, $\sigma=30\%$, $r=4\%$, $T=1$. Then $d_2=(0+0.04-0.045)/0.30=-0.017$ and $d_1=d_2+0.30=0.283$, so the dollar accountant says $N(d_2)=0.493$ and the share accountant says $N(d_1)=0.611$. Carried to five places, $N(d_1)=0.61154$ and $N(d_2)=0.49335$, the call is worth $100\times0.61154-96.079\times0.49335\approx13.75$, the same 13.75 that sat in the parity lunchbox of §6-B.1.2. Sixty-one per cent and forty-nine per cent are both the probability of finishing in the money, under two numeraires, and neither is a forecast. What a forecast would need is next.

Stated once, with $N(\cdot)$ the standard normal distribution function:

$$
C=S_0N(d_1)-Ke^{-rT}N(d_2),\qquad \text{Put}=Ke^{-rT}N(-d_2)-S_0N(-d_1),\qquad d_2=\frac{\ln(S_0/K)+(r-\tfrac12\sigma^2)T}{\sigma\sqrt T},\quad d_1=d_2+\sigma\sqrt T .
$$

In the box's language, $N(d_2)$ counts the event of exercise at expiry in cash and $N(d_1)$ counts it in shares. Neither is the probability that the option will actually finish in the money: that would need $\mu$ in place of $r$, and it is $N(DD)$ in Merton's language (§6.2.3). Two correct probabilities of one event, neither of which anybody believes. Welcome to derivatives.

For Merton, $N(-d_2)=\mathbb{Q}(V_T<F)$ is the risk-neutral default probability that Chapter 6 stated; the physical $N(-DD)$ swaps $r$ back to $\mu$, and the gap is §6-B.6.

#### The Full Derivation: the change of numeraire

Under $\mathbb{Q}$, $\ln S_T=\ln S_0+(r-\tfrac12\sigma^2)T+\sigma\sqrt T\,Z$ with $Z\sim\mathcal N(0,1)$. Split the call payoff:

$$
e^{rT}C=\mathbb{E}^{\mathbb{Q}}\big[S_T\mathbf 1_{\{S_T>K\}}\big]-K\,\mathbb{Q}(S_T>K).
$$

The second term is direct: $S_T>K$ iff $Z>-d_2$, with

$$
d_2=\frac{\ln(S_0/K)+(r-\tfrac12\sigma^2)T}{\sigma\sqrt T},\qquad \mathbb{Q}(S_T>K)=N(d_2).
$$

For the first term, change numeraire. Define a new measure $\mathbb{Q}^S$ by the density $d\mathbb{Q}^S/d\mathbb{Q}=S_T/(S_0e^{rT})=\exp(\sigma\sqrt T Z-\tfrac12\sigma^2T)$. That density is positive and has expectation 1, so $\mathbb{Q}^S$ is a probability measure. Under it, $Z$ is normal with mean $\sigma\sqrt T$ (complete the square in the exponent), so $\ln S_T$ has mean $\ln S_0+(r+\tfrac12\sigma^2)T$ and

$$
\mathbb{E}^{\mathbb{Q}}\big[S_T\mathbf 1_{\{S_T>K\}}\big]=S_0e^{rT}\,\mathbb{Q}^S(S_T>K)=S_0e^{rT}N(d_1),\qquad d_1=d_2+\sigma\sqrt T .
$$

Putting the pieces together, and using parity for the put:

$$
C=S_0N(d_1)-Ke^{-rT}N(d_2),\qquad \text{Put}=Ke^{-rT}N(-d_2)-S_0N(-d_1).
$$

Used in: §3.1 (the two-point bond, read correctly), §6.2.2–6.2.3, §6.4 (the KMV inversion), §11.1, §16.3–16.4 (rights, backstops and warrants priced with these formulas), §23.1–23.2.

## 6-B.3 The Greeks as Lines on a Risk Report

### 6-B.3.1 Desk framing: a Greek is a question somebody asks at 7 a.m.

A Greek is a partial derivative with a job title. *Delta:* if the underlying moves a dollar, what do I make? *Gamma:* how wrong is my delta after it moves? *Vega:* if everyone decides the world is more volatile, what do I lose, even if nothing moves? *Theta:* what does waiting cost? *Rho:* what if rates move? And one that is not a derivative at all, *JTD:* what if the issuer is not there tomorrow? A credit desk asks all six. It just calls them CS01, convexity, "spread vol," carry, DV01 and "the jump," and then wonders why the options desk upstairs can hedge and it can't.

> **Math, Gently.** *A Greek is a bump.* Forget calculus for a moment. A risk system computes a Greek the way a mechanic finds a rattle: nudge one thing, listen, divide by the size of the nudge. Take the call of §6-B.2.5, worth 13.75 with the stock at 100. Reprice it with the stock at 101 and it is worth 14.37; with the stock at 99, 13.15. The change per dollar is $(14.37-13.15)/2=0.61$, which is the $N(d_1)$ the share accountant gave us. That is delta. Bump only upward and you get 0.62, a little more, because delta itself grew on the way up; that leftover is gamma, the next row of the table. Now leave the stock alone and bump the volatility from 30% to 31%. The call goes from 13.75 to 14.14, so it gains 0.38 *per vol point*. The closed-form vega in the next table is 38.3, because it is the change per 1.00 of volatility, a move from 30% to 130%, which nobody has ever seen happen in one go. Divide it by 100 to get the 0.38 a trader quotes. Remember that 100; it will cost somebody money before this chapter is over. The closed forms are next.

### 6-B.3.2 The five derivatives, in closed form

Differentiate the §6-B.2.5 formulas. Write $\phi(x)=e^{-x^2/2}/\sqrt{2\pi}$ for the standard normal density, and use the identity $S_0\phi(d_1)=Ke^{-rT}\phi(d_2)$, which follows from expanding $d_1^2-d_2^2=2\ln(S_0e^{rT}/K)$ and saves a page of algebra:

| Greek | Call | Put | Units |
| :-- | :-- | :-- | :-- |
| Delta $\Delta=\partial f/\partial S$ | $N(d_1)$ | $-N(-d_1)$ | per \$1 of underlying |
| Gamma $\Gamma=\partial^2f/\partial S^2$ | $\dfrac{\phi(d_1)}{S_0\sigma\sqrt T}$ | same | per \$1, per \$1 |
| Vega $\nu=\partial f/\partial\sigma$ | $S_0\phi(d_1)\sqrt T$ | same | per 1.00 of vol; divide by 100 for a vol point |
| Theta $\Theta=\partial f/\partial t$ | $-\dfrac{S_0\phi(d_1)\sigma}{2\sqrt T}-rKe^{-rT}N(d_2)$ | $-\dfrac{S_0\phi(d_1)\sigma}{2\sqrt T}+rKe^{-rT}N(-d_2)$ | per year of calendar time |
| Rho $\rho^{\text{opt}}=\partial f/\partial r$ | $KTe^{-rT}N(d_2)$ | $-KTe^{-rT}N(-d_2)$ | per 1.00 of rate |

(The superscript on $\rho^{\text{opt}}$ keeps it apart from the correlation $\rho$ of §6.3.2.) Gamma and vega are the same for calls and puts because parity makes their difference linear in $S$, and linear things have no curvature and no opinion about volatility.

### 6-B.3.3 The theta–gamma identity: the rent and the bill

Substitute the Greeks into the PDE of §6-B.2.3 and it becomes an accounting identity:

$$
\Theta+rS\Delta+\tfrac12\sigma^2S^2\Gamma=rf .
$$

For a delta-hedged position the middle term is offset by the financing of the hedge, and what remains is $\Theta-r(f-S\Delta)=-\tfrac12\sigma^2S^2\Gamma$. Read it as the desk reads it: **theta is the rent you pay for gamma**, charged at the implied variance. Combine it with the gamma-rent equation of §6-B.2.4 and the whole economics of a hedged option fits in one line. You pay $\tfrac12\Gamma S^2\sigma_i^2$ per unit time in decay and collect $\tfrac12\Gamma S^2\sigma_r^2$ from the moves. A short-gamma book reverses the signs. It collects the decay and pays for the moves, and its P&L distribution has the shape every high-yield manager knows: many small good days and a few large bad ones (§11.1). There is no free gamma. There is only gamma whose rent somebody mispriced.

### 6-B.3.4 Merton debt, Greek by Greek

In Merton, $B=Fe^{-rT}-\text{Put}(V,F)$. Every Greek of the bond is the negative of the put's Greek, plus the riskless bond's rho:

$$
\frac{\partial B}{\partial V}=N(-d_1),\qquad \frac{\partial^2B}{\partial V^2}=-\frac{\phi(d_1)}{V_0\sigma_V\sqrt T},\qquad \frac{\partial B}{\partial\sigma_V}=-V_0\phi(d_1)\sqrt T,\qquad \frac{\partial s}{\partial\sigma_V}=\frac{V_0\phi(d_1)\sqrt T}{B_0T}.
$$

The bondholder is long a little of the firm, short gamma on its assets, and short volatility. The last formula converts the bond's vega into spread units by differentiating $s=-T^{-1}\ln(B_0/Fe^{-rT})$.

*Worked example (illustrative).* Take the §6.2.4 firm ($V_0=100$, $F=80$, $r=4\%$, $\sigma_V=25\%$, $T=1$; a 216 bp, double-B-ish credit) and a CCC cousin with the same assets but $F=95$ and $\sigma_V=40\%$.

| Line | §6.2.4 firm ($F=80$, $\sigma_V=25\%$) | CCC cousin ($F=95$, $\sigma_V=40\%$) |
| :-- | --: | --: |
| $d_1$, $d_2$ | 1.178, 0.928 | 0.428, 0.028 |
| Equity $E_0$ / debt $B_0$ | 24.78 / 75.22 | 19.91 / 80.09 |
| Put on firm (= $Fe^{-rT}-B_0$) | 1.64 | 11.19 |
| Spread $s$ | 216 bp | 1,307 bp |
| $\mathbb{Q}(\tau\le T)=N(-d_2)$ | 17.7% | 48.9% |
| Bond delta $\partial B/\partial V$ | 0.119 | 0.334 |
| Bond gamma $\partial^2B/\partial V^2$ | −0.0080 | −0.0091 |
| Bond vega, per asset-vol point | −0.199 | −0.364 |
| Spread vega, per asset-vol point | +26.5 bp | +45.4 bp |
| Bond per \$1 of equity, $N(-d_1)/N(d_1)$ | 0.136 | 0.502 |
| Elasticity hedge ratio $h$ (23.10) | 0.045 | 0.125 |

Three readings. The CCC bond is a third of the firm by delta, and it moves fifty cents per dollar of equity, against fourteen for the double-B. Its vega is nearly twice as large per vol point, on a bond whose spread is six times wider, so vega *per basis point of spread* falls as the credit worsens while vega in dollars rises. And the Merton recovery problem of §6.2.4 is still there: 1,307 bp on a 48.9% default probability is a loss given default of about 25% (the bond is $1-e^{-sT}=12.3\%$ below its riskless value), a recovery near 75 cents that Mags has not seen on an unsecured bond since the Clinton administration. The Greeks are right in shape and wrong in level for the same reason the spreads are: the diffusion has no jump in it. §6-B.5 adds one. Figure 6-B.3 draws the bond delta and gamma rows of the table as curves in asset value.

![Figure 6-B.3: Bond delta falls from 1 toward 0 as assets rise, and bond gamma is negative everywhere and deepest when assets are near or below the face value, so the bondholder is short gamma exactly where default is close; at an asset value of 100 the CCC cousin's delta is 0.33 against 0.12 for the 216 bp firm. Illustrative: Merton debt with one year to maturity and r = 4%, computed with merton() of Listing 6-B.1 for the §6.2.4 firm and its CCC cousin.](assets/figures/ch06b_merton_bond_greeks.png)

### 6-B.3.5 The risk report, line by line

| Risk-report line | Option definition | Credit reading | What hedges it | Built / applied |
| :-- | :-- | :-- | :-- | :-- |
| Delta | $\partial f/\partial S$ | CS01 in spread space; shares per bond in stock space | CDX; the stock | Ch 4-B; §23.5 |
| Gamma | $\partial^2f/\partial S^2$ | Spread convexity; the bondholder's short gamma on assets | Options on CDX; listed puts | §23.5; Ch 10-B |
| Vega | $\partial f/\partial\sigma$ | Short $\sigma_V$; the cold open's −\$41k per vol point | Index swaptions; the equity surface | §23.2 |
| Theta | $\partial f/\partial t$ | Carry plus roll-down: the rent | Nothing; it is why you are there | Ch 4-B; §9 carry |
| Rho | $\partial f/\partial r$ | DV01, and the hedge ratio that is not modified duration | Treasury futures | Ch 4-B; §8.2 |
| JTD | $f(\text{post})-f(\text{pre})$ | $R-P$ per bond; $(1-R)-\text{MTM}$ per unit of bought CDS | Put spreads; CDS | §6-B.5; §23.5; §28.4 |

*Same Monday, live (fictional; the book and its numbers are the cold open's).* At 7:40, twenty minutes before his first risk meeting, Theo prints the table and lays it beside his own report, column against row. Market value and carry are theta's family. DV01 is rho. CS01 is delta in spread space, and the index beta is delta to the CDX hedge. DTS is a delta scaled for the fact that wide spreads move more. The ninth column, now that Kaz has shown him the one bond that makes it, is vega. He draws a line from each of his columns to a row of the table, and every line lands on a derivative: a slope, or the slope of a slope.

Except one. The tenth column, JTD, lands on the last row, and the last row is not a derivative of anything. It is a finite difference across the default event: what the book is worth the instant after the issuer is gone minus what it is worth now, $(R-P)\times$ face for each bond, summed. His −\$6.3mm is that sum over forty-one bonds *(illustrative)*. It does not shrink when you look more closely, the way a slope does when you zoom in on a curve. It is the same size at any magnification.

"It's the only line that doesn't care how small the move is," he says.

"It's the line an equity-options desk forgets and a credit desk lives on," Ines says, walking past with her coffee. "Charge the jump once, there, and not again in the spread, the skew and the size." That is Law 6 (App E), and §28.4 is where the size side of it gets its arithmetic. Ines does not say which replay she is saving it for. The scene after §6-B.5.3 is the week it was the only line that mattered.

> **View From Another Seat.** *The systematic fund that reads the report as a regression.* A quantitative multi-asset manager would look at Theo's eleven columns and see a factor model with too many names in it. In May 2019 Bloomberg reported on a paper by AQR's Roni Israelov showing that four exposures, government bonds, equities, equity volatility and bond volatility, explain up to 76% of corporate-debt returns, so that a Merton-style replication built from futures and listed options could stand in for the bonds "for those who desire enhanced liquidity and cash efficiency" (Bloomberg, 15 May 2019, as republished by WealthManagement.com; the same report notes Israelov would not say whether AQR would use the strategy in its funds). From that seat, Theo's vega column is a loading on an equity-volatility factor the fund can buy in the listed market, and his delta and rho columns are futures positions. The JTD line is the residual: the part of the bond no index and no option replicates, and the part a factor replicator chooses not to hold. Theo's desk exists to hold exactly that residual and to be paid for it, which is the whole relative-value thread of this book in one sentence: hedge what can be bought cheaply, and keep what cannot.

Used in: §8.3 (bond-to-equity sensitivity), §11.1, §19 (basket risk lines), §21.4 (pool-level Greeks), §23.5 (the Natenberg map, in spread space), §28.1 and §28.4 (risk budgets and Kelly with a jump).

## 6-B.4 Implied Volatility and Skew: A Price Quoted in the Wrong Units, on Purpose

### 6-B.4.1 Desk framing

Options trade in volatility for the same reason bonds trade in spread: the unit strips out the boring parts of the price (moneyness, time, rates) and leaves the part people disagree about. A \$2.10 put is not information. A 74% implied volatility on a 20-delta put, when the at-the-money vol is 48%, is.

### 6-B.4.2 Definition, existence, and a solver that does not embarrass you

An implied volatility is a question asked backwards, in the phrase of Chapter 4-B's box: not "what is the price at this volatility?" but "what volatility makes the formula print this price?" Formally, $\sigma_{\text{imp}}(K,T)$ is the number that makes Black–Scholes match the market price: $C_{\text{BS}}(S_0,K,T,\sigma_{\text{imp}},r)=C^{\text{mkt}}$. It exists and is unique whenever the price lies strictly inside the no-arbitrage bounds,

$$
\big(S_0-Ke^{-rT}\big)^+<C^{\text{mkt}}<S_0,\qquad \big(Ke^{-rT}-S_0\big)^+<\text{Put}^{\text{mkt}}<Ke^{-rT},
$$

because vega is strictly positive, so $C_{\text{BS}}$ is strictly increasing in $\sigma$. It tends to intrinsic value as $\sigma\downarrow0$ and to $S_0$ as $\sigma\uparrow\infty$. Outside the bounds there is no implied vol, and the right output is not a number but a reason: a stale quote, an American premium being fed to a European formula, a borrow fee being treated as volatility, or a crossed market.

The solver every desk eventually writes is Newton's method, $\sigma_{n+1}=\sigma_n-\big(C_{\text{BS}}(\sigma_n)-C^{\text{mkt}}\big)/\nu(\sigma_n)$, started near the Brenner and Subrahmanyam (1988) at-the-money approximation $\sigma_0\approx\sqrt{2\pi/T}\,C^{\text{mkt}}/S_0$. Newton diverges in the wings, where vega is tiny, so the §6-B.9 solver keeps a bisection bracket, rejects any step that leaves it, and declares convergence in *price* units, not vol units. A vol that is correct to $10^{-8}$ on a price nobody can trade is not precision. It is decoration.

### 6-B.4.3 Skew: two credit reasons the left wing is steep

> **Math, Gently.** *Skew is the ground-floor premium.* Flood insurance costs more per dollar of cover on the ground floor than on the tenth, and nobody thinks that is irrational: the ground floor floods in the storms that matter, and the people selling the cover know it. An implied volatility surface charges the same way. Quote every put on one stock in volatility units and the low strikes, the ground floor, carry a higher number than the at-the-money ones. *A number to check:* a \$100 stock, one year, $r=4\%$. At the money the market says 48%. Find the strike whose put has a delta of $-0.20$ at the 74% the market quotes there: it is about \$73.40. Priced at 74%, that put costs about \$12.41. Priced on a flat 48% surface, it would cost about \$5.41. The ground-floor premium is not a few per cent; the market charges about 2.3 times the flat-surface price *(illustrative; Black–Scholes, `bs_price` of Listing 6-B.1)*. The two credit reasons it does so are next.

If Black–Scholes were the truth, $\sigma_{\text{imp}}$ would be flat in $K$. It never is. By §6-B.1.3 a non-flat implied vol curve is the market telling you that its $\mathbb{Q}$-density is not lognormal. For a leveraged firm there are two reasons the low strikes are expensive, and both are credit.

*Leverage.* In Merton, equity is a call on assets, and a call's elasticity $\Omega=VN(d_1)/E$ is at least 1 (a convex payoff through the origin always has $E\le VE_V$) and rises as the call moves out of the money. So $\sigma_E=\Omega\,\sigma_V$ rises as $V$ falls. Low equity strikes correspond to states with low assets and high leverage, where the stock is more volatile. That is the compound-option skew of §23.1, and CreditGrades (§23.2) is built on it.

*Jump-to-default.* The stock can go to zero in a single print. A diffusion cannot produce that at any volatility, so the implied vol of a deep out-of-the-money put has to rise without bound to price it. §6-B.5.5 proves how fast.

The fingerprints differ in prices, not vols: if the stock cannot reach zero, $\text{Put}(K)/K\to0$ as $K\to0$; under jump-to-default it flattens to a positive floor (the `floor_ratio` test of §23.4).

> **Desk Myth vs. Desk Reality.** *Myth:* "Implied vol is the market's forecast of realized volatility." *Reality:* it is the break-even volatility of the gamma-rent equation, priced under $\mathbb{Q}$. It contains a variance risk premium (sellers of insurance want paying) and, in a high-yield name, a default premium. The gamma-rent equation tells you what a forecast is worth: you profit from a long hedged option when $\sigma_r>\sigma_i$, *weighted by where the dollar gamma happened to be*. Volatility that happens far from the strike earns nothing; Ines calls it "being right in a room nobody was in."

Used in: Ch 10-B (index option skew, payer versus receiver), §16.4 (warrant vol on an unlisted reorganized equity), §23.1–23.4 (the surface engine), §23.6 (cap-structure signals).

## 6-B.5 Jump-to-Default: Merton 1976 With One Jump, and Carr–Wu for Free

### 6-B.5.1 Desk framing: the Tuesday that is not in the diffusion

§6.2.4 showed what a pure diffusion costs a credit model: zero short-dated spreads and recoveries near 90 cents, because a firm that can only drift toward its default point is never surprised by it. The repair is to let the underlying jump, and the simplest jump that matters to credit is the one to zero. The model comes first; the week it mattered, replayed, follows §6-B.5.3.

### 6-B.5.2 The model

> **Math, Gently.** *Two parts: the survivors pay for the funeral, and the put has a floor.* Chapter 6's box gave default a Poisson clock that rings at rate $\lambda$; here the bell takes the stock straight to zero. **Part one.** Suppose the clock rings at $\lambda=5\%$ a year and money earns $r=4\%$. Any traded asset, priced risk-neutrally, must grow at 4% on average across all its paths, the dead ones included. The dead paths are worth zero. So the live paths have to grow faster to make up for them: at about $r+\lambda=9\%$, because 5% of the value disappears into the funeral each year and the survivors pay for it in their drift. Turn it around and price a dollar that is paid in a year only if the firm is still alive: discount for time, $e^{-0.04}$, and for survival, $e^{-0.05}$, and it costs $0.961\times0.951=0.914$. **Part two.** Now buy a put struck at \$1 on that stock. If the firm dies, the stock is zero and the put pays its full \$1, whatever volatility did on the way. So before any diffusion is counted, the put is worth at least a dollar paid in a year *if* the firm dies: $e^{-0.04}\times(1-e^{-0.05})=0.961\times0.049=0.047$, almost five cents. That is the floor in Figure 6-B.4, and no volatility, however low, can take a put below it. Both parts are one formula, next.

Let $N_t$ be a Poisson process with constant $\mathbb{Q}$-intensity $\lambda$ and let $\tau$ be its first jump: default. The stock is worth zero from $\tau$ on. Before default, under $\mathbb{Q}$,

$$
\frac{dS_t}{S_{t^-}}=(r+\lambda)\,dt+\sigma\,dW^{\mathbb{Q}}_t-dN_t .
$$

The $-dN_t$ term takes the stock to zero at the jump. The extra $+\lambda\,dt$ is the compensator: $\mathbb{E}^{\mathbb{Q}}[dN_t]=\lambda\,dt$, so $\mathbb{E}^{\mathbb{Q}}[dS_t/S_{t^-}]=r\,dt$ and the discounted stock is a $\mathbb{Q}$-martingale, as it must be for any traded asset (the box's 9% drift for the survivors). Solving,

$$
S_t=\tilde S_t\,\mathbf 1_{\{\tau>t\}},\qquad \tilde S_t=S_0\exp\!\Big\{\big(r+\lambda-\tfrac12\sigma^2\big)t+\sigma W^{\mathbb{Q}}_t\Big\},\qquad \mathbb{Q}(\tau>t)=S^{\mathbb{Q}}(t)=e^{-\lambda t}.
$$

This is Merton (1976) with one jump size, minus 100%: equity is a call on assets until a surprise (fraud, a lost lawsuit, an LMT that leaves equity nothing) makes it worthless whatever the diffusion was doing.

### 6-B.5.3 Calls and puts: one formula and one decomposition

A call pays only if the firm survives, and the survival indicator is independent of $W$:

$$
C^{\text{JTD}}=e^{-rT}e^{-\lambda T}\,\mathbb{E}\big[(\tilde S_T-K)^+\big]=C_{\text{BS}}\big(S_0,K,T,\sigma,\;r+\lambda\big),
$$

because $\tilde S$ grows at $r+\lambda$ and the combined discount is $e^{-(r+\lambda)T}$, which is exactly the Black–Scholes call at the rate $r+\lambda$. A put pays $K$ in every default state and $(K-\tilde S_T)^+$ in every survival state:

$$
\text{Put}^{\text{JTD}}(K)=\underbrace{K\,e^{-rT}\big(1-e^{-\lambda T}\big)}_{K\,\times\,U^{\text{Eur}}(T)}+\underbrace{\text{Put}_{\text{BS}}\big(S_0,K,T,\sigma,\;r+\lambda\big)}_{\text{diffusive put at the hazard-shifted rate}} . \tag{6B.1}
$$

**A put on a defaultable stock is $K$ unit recovery claims plus a diffusive put priced at a hazard-shifted rate.** Expand the second term and (6B.1) is the §23.4 formula (23.8) term for term; check parity and it holds, since $C^{\text{JTD}}-\text{Put}^{\text{JTD}}=S_0-Ke^{-rT}$.

Later chapters lean on two things that fall out of it. Holding the share price fixed, the jump makes a call *more* valuable, not less: rho is positive, so moving the rate from $r$ to $r+\lambda$ raises the call, because the strike is paid only in survival states and the surviving stock must outperform to pay for the dead. That is why Kaz's $e^{-\lambda T}$ haircut on the Hertz warrants charged the funeral twice (§16.4). And the jump gives a put a floor: as $K\to0$ the second term vanishes faster than $K$, so $\text{Put}^{\text{JTD}}(K)/K\to U^{\text{Eur}}(T)$, the box's five cents per dollar of strike. The floor ratio is the hazard.

#### Long Scene: SVB Financial, 8–17 Mar 2023, the line that is not a derivative

*A replay. The desk's position, its hedge, its marks, the model runs and all dialogue are fictional; nobody on the desk sat in any SVB creditor group, and Mags's own small purchase of the holdco paper that month is Chapter 6's story, not retold here. SVB facts are from the company's 10-K and 8-Ks, the Federal Reserve's review of 28 April 2023, the FDIC's release, a vendor's pre-market options report and the press reports named where they appear. Theo was at his old firm in March 2023 and was not staffed on SVB Financial (Chapter 3).*

"In textbooks companies die by diffusion," Mags says. "They drift down, they touch a barrier, they stop. In my experience they die on a Tuesday at 7 a.m. in a press release with the word 'regrettably' in it."

"This one died on a Friday," Ines says, "and it didn't send a press release. The regulator did."

Wednesday 21 October 2026, 4:15 p.m. Ines has dealt the SVB folder before, the way every desk does. Chapter 3's new-hire drill read the holding company's balance sheet, Chapter 6 watched the structural model fail to see the run, and Chapter 8's replay hedged a generic book's rates through the week. Tonight she deals it to the hedger. The tab says *Cut: close, Wed 8 Mar 2023*, and the position card clipped to the front is new.

**The position (illustrative).** Long \$25mm face of SVB Financial Group's 1.800% senior notes due 2031, the holding company's paper, marked at 76: a low coupon with eight years to run, trading below par because of rates, not credit. Against it, short SIVB common stock. The desk had wanted to size the short by the Merton bond-per-equity ratio of §6-B.3.4, $N(-d_1)/N(d_1)$, and the model had returned about $10^{-8}$: on the holdco's inputs, market equity of \$15.9bn at Wednesday's \$267.83 covered the \$3.3bn of senior notes 4.8 times, and the model's one-year default probability was of the order of one in ten million (calc, from the 10-K and that close). A hedge of zero shares is not a hedge a risk committee signs, so the desk used its house floor, five cents of stock per dollar of bond market value: about \$950,000 short, some 3,550 shares.

"Why five cents?" Theo asks.

"Because the committee needed a number with a digit in it," Ines says. "Somebody in 2019 picked five. Nobody has asked since. Every desk has a number like that, and the day you find out where it came from is usually a bad day." Kaz, who has spent part of the afternoon trying to find out where the desk's 40% recovery default came from, says nothing, which on Kaz is a confession.

Theo reads the Thursday 7 a.m. risk report off the card, line by line, the way §6-B.3.5 taught him. Delta: near zero. Gamma: near zero. Vega: near zero, on an implied volatility that had sat between 39 and 50 until that week. Theta: the carry, small and positive. Rho: the one real number on the page apart from the last, because a 1.8% coupon with eight years to run is a rates trade. And the last line, the one that is not a derivative: $(R-P)\times$ face at the desk's 40 recovery is $(0.40-0.76)\times\$25\text{mm}=-\$9.0\text{mm}$, less about \$0.95mm the stock short would make if the shares went to zero: about −\$8mm.

"Nobody read that line," Ines says. "On a desk like this one, nobody would have, because every other line said the bond was a Treasury with a funny name."

After the close on Wednesday the company had filed an 8-K announcing a securities sale and a capital raise (Chapter 3's drill reads it line by line). Ines turns the page.

**Thursday, 9 March.** The stock closes at \$106.04, down 60.4% on the day, and more than \$40bn of deposits leave the bank (the run is Chapter 6's scene; this one watches the hedge). The short-stock leg has made about \$570,000. The bond has barely printed: the folder holds no trade in the 2031s that day that the desk could find, and Ines refuses to invent one. On the report, the delta line has woken up, and the JTD line has not moved, because it never did depend on the stock.

Theo stares at that for a while. Six lines, and five of them are slopes that change when the world tilts. The sixth is a cliff, and it has been the same height since Wednesday morning: about eight million dollars, sitting at the bottom of the page in the same font as the carry. "It was the biggest number on the report on Wednesday," he says, "and the only one that didn't change on Thursday."

"That's what makes it easy to stop reading," Ines says.

#### The card: Thursday, 9 March, at the close

*Write three things: which of the six lines on the report is your risk now, what you buy to cover it, and what it costs.*

Kaz writes first. *Delta. Rerun Merton at \$106 with Thursday's equity vol; the bond-per-equity ratio rises about a hundredfold (fictional run). Short the extra shares at the open.*

Mags writes in capitals. *JTD. BUY PUTS. ANY STRIKE UNDER 50. ANY VOL.*

Theo holds his pen for a long time. He has been reading the indenture summary on the back of the position card, and one phrase has stopped him: the notes are "recourse only to the Company and ... not guaranteed by the Company's subsidiaries." The Company is the holding company. The bank is a subsidiary. *JTD,* he writes, *but whose default? The bank can fail without the holdco filing, and the holdco can be a creditor of its own dead bank. Buy a put spread whose width covers the JTD line, not outright puts. Cost: whatever tomorrow charges. I don't know what that is.*

What would you write? The house rule is the same as on Tuesday: a card executes at the first print after it was written.

**Friday, 10 March, before the open.** A vendor's pre-market options report puts SIVB's 30-day implied volatility at 167, against a 52-week range of 39 to 280, with calls to puts at 1.1 to 1 (Market Rebellion, 10 Mar 2023). The shares trade premarket, down as much as 69% on press reports, until Nasdaq halts them at 8:35 a.m. for news dissemination. That morning the California Department of Financial Protection and Innovation closes the bank and appoints the FDIC as receiver. The holding company's offerings are terminated. SIVB never reopens on Nasdaq. Listed options do not trade premarket, so Mags's puts and Theo's spread never meet a market; Kaz's extra shares could only have been sold into the thin premarket tape, at a price already about two-thirds below Thursday's close, after most of the fall. No card executes at a price worth having. TRACE data cited by Bloomberg put the senior holdco notes at roughly 37 to 42 cents at Friday's close. At 40, the desk's bond leg is down 36 points on \$25mm: −\$9.0mm, the JTD line to the dollar.

Ines makes Kaz run one more number, as the desk's fictional run. If the stock's ordinary diffusive volatility was still about 45%, the middle of the band it had lived in, what jump intensity makes a one-month at-the-money put trade at 167? Kaz bisects on $\lambda$ with (6B.1) and an implied-vol solver. The answer is about 2.5 a year: a 19% chance of a wipe-out within the month. At that intensity a one-month at-the-money put on the \$106.04 stock is worth about \$19.99, and \$19.71 of it, 99%, is the unit recovery claim of (6B.1); without the jump the same put at 45% would have been worth \$5.31. A put struck at half the forward must, by (6B.3), carry an implied volatility of at least 203%, and in the model it carries 343%. "Thursday's surface wasn't a volatility surface," Kaz says slowly. "It was a default claim in volatility's clothing. The 167 was a hazard rate quoted in the wrong units."

**The grade.** Ines grades the cards against the tape and against §6-B.5.6, which none of them had read yet.

Kaz's card hedged nothing, because the stock stopped trading before it could be sold at a price that mattered, and because even an open one would have been the wrong instrument: the stock is one instrument against two risks, the diffusion and the jump, and the delta that minimizes the first leaves almost all of the second on the table. Mags's card named the right line and the right kind of instrument, and could not be filled: by the time the volatility had moved to where (6B.3) said it had to be, there was no market to pay it in, and the house rule does not let anyone buy Thursday's close on Friday.

"The stock hedge works when the stock trades through the bad news," Ines says. "It breaks the moment the bad news arrives as a halt, and that's the moment it was for." She taps the JTD line. "The only thing on this table that would have paid is an instrument that jumps by its width at default and barely diffuses, which is a put spread, bought on Wednesday, when the line said minus eight million and the surface said nobody cared."

The desk's fictional run prices it. On Wednesday's close, at the 45% volatility and a small intensity the desk might have pencilled in, 1%, a one-month put spread struck at \$100 and \$50 cost about four cents a share and paid \$50 at a wipe-out. Covering \$9mm of JTD takes 180,000 shares of spread, 1,800 contracts; in a listed market where a deep out-of-the-money option is offered at the exchange's minimum, call it ten to twenty thousand dollars *(illustrative)*. How a put on a halted, later-delisted stock is exercised is an afternoon with the options clearing house that Ines does not deal tonight. The point is the price. On Wednesday the jump was on the report and off the surface, and that gap is the only time the hedge is cheap.

**Which default?** Theo's card gets the evening's best grade, and not for anything he bought. Ines opens the last folder. The stock's wipe-out came on 10 March, by receivership: the holding company's main asset passed to the FDIC, and the equity's value went with it. The notes' default came a week later, on 17 March, when SVB Financial Group filed for Chapter 11 in the Southern District of New York (case 23-10367), which accelerated all seven series of senior notes. The equity event and the credit event were a week apart and in different forums, a receivership and a bankruptcy court. A put-implied hazard measures the first; a bond spread prices the second; and a desk that compares them without saying which event each one is about is comparing a funeral with a will reading. Six weeks later the 3.5% notes due 2025 traded at 69 and the 1.8% notes due 2031 at 57 (MarketAxess data reported by Debtwire, 26 Apr 2023): one class of claims, twelve points apart, which §3.1.3 reads as a reinstatement bet on one class rather than two recoveries.

Theo writes the evening's sentence on a sticky note and puts it under the one from Monday, *vega = one bond + one accident*: *JTD is the only line priced before the event. Buy it while it's off the surface.* Then he adds, smaller, *and ask which default.*

Mags has the last word, as she usually does with funerals. "Your put chain saw the funeral," she says. "Your bond went to a different one."

<!-- FIGURE: ch06b_svb_week.png (timeline 8–17 Mar 2023: SIVB close 267.83, 106.04, halt; 30-day implied vol 39–50 to 167, range top 280; holdco notes at the illustrative desk mark, 37–42 TRACE via Bloomberg on 10 Mar, 69/57 on 25 Apr; receivership 10 Mar and Chapter 11 17 Mar as vertical lines labelled "equity event" and "credit event"; source SVB §2.1, §2.3) -->

### 6-B.5.4 Corollary 1: the Carr–Wu corridor, with an error term

Take two strikes $A<B$ and divide the put spread by its width. From (6B.1),

$$
\frac{\text{Put}^{\text{JTD}}(B)-\text{Put}^{\text{JTD}}(A)}{B-A}=U^{\text{Eur}}(T)+\varepsilon(A,B),\qquad 0\le\varepsilon(A,B)\le e^{-(r+\lambda)T}\,N\!\big(-\tilde d_2(B)\big), \tag{6B.2}
$$

with $\tilde d_2(B)=\big[\ln(S_0/B)+(r+\lambda-\tfrac12\sigma^2)T\big]/(\sigma\sqrt T)$; the proof is in the Full Derivation at the end of §6-B.5.5.

That is the European Carr–Wu result as a corollary: the put spread is a pure default claim plus a *corridor leak*, the chance that a live stock diffuses down into the strikes, which vanishes when the strikes sit far below spot relative to $\sigma\sqrt T$. Carr and Wu's exact American statement (§23.3) replaces the leak with an assumption: if the pre-default stock never trades below $B$, then $\varepsilon=0$ identically, early exercise happens at $\tau$, and the claim being priced becomes the American one, $U^{\text{Am}}(T)=\frac{\lambda}{r+\lambda}\big(1-e^{-(r+\lambda)T}\big)$. The model sizes the leak when the assumption is only approximately true, which is the number a desk needs.

*Worked example (illustrative).* A \$6 stock, $\sigma=80\%$, $r=4\%$, $\lambda=14.5\%$, $T=1$, and a \$1 put ($A=0$, $B=1$). Then $U^{\text{Eur}}=0.9608\times(1-e^{-0.145})=0.1297$. The bound in (6B.2) is $e^{-0.185}N(-2.071)\approx0.016$; the actual leak is $\text{Put}_{\text{BS}}(6,1,1,0.8,0.185)\approx0.0037$. The \$1 put is 97% default claim and 3% diffusion. §6-B.8 uses exactly this chain.

### 6-B.5.5 Corollary 2: the wing must blow up, and how fast

> **Math, Gently.** *The ridge.* Plot implied *variance*, $\sigma_{\text{imp}}^2T$, against log-moneyness, $\ln(F_0/K)$, which measures how far below the forward a strike sits in proportional terms. For low strikes the curve climbs. How steeply can it climb? Lee's moment formula says no faster than a straight hill of slope 2: any steeper and some option would be priced above what it could possibly pay. Think of the slope-2 line as a ridge. Ordinary stochastic-volatility models live on the hillside below it. A stock that can die in one print walks exactly on the ridge, because its low-strike puts never stop being worth something: they keep the floor of the box in §6-B.5.2. *A number for the margin:* with a 5% intensity over one year, survival is $e^{-0.05}=0.951$, and $c=N^{-1}(0.951)=1.657$. Take a put struck at a fifth of the forward, so $L=\ln5=1.609$. The bound below says $x=\sigma_{\text{imp}}\sqrt T\ge-1.657+\sqrt{1.657^2+2\times1.609}=-1.657+\sqrt{2.746+3.219}=0.785$: no implied volatility below 78.5% can price that put, whatever the stock's ordinary volatility is. The proposition is next, and both proofs follow it.

**Proposition.** In the jump-to-default model, the Black–Scholes implied volatility of a put struck at $K$ below the forward $F_0=S_0e^{rT}$ satisfies

$$
\sigma_{\text{imp}}(K)\sqrt T\;\ge\;-c+\sqrt{c^2+2\ln(F_0/K)},\qquad c=N^{-1}\big(S^{\mathbb{Q}}(T)\big)=N^{-1}\big(e^{-\lambda T}\big). \tag{6B.3}
$$

The default probability alone puts a floor under the wing. With $\lambda=5\%$ and $T=1$ the box's arithmetic gives $c=N^{-1}(0.951)=1.657$ and, at $K/F_0=0.2$, a bound of 78.5%, which the §23.4 table (about 100% at that moneyness) respects. As $K\to0$ the bound grows like $\sqrt{2\ln(F_0/K)/T}$: implied variance rises linearly in log-moneyness with slope 2. That is the steepest left wing Lee's (2004) moment formula allows. A stock that can reach zero sits exactly on the boundary. A stochastic-volatility model can make the wing steep, and an exotic one can even match the slope, but no model without mass at zero produces a positive floor in $\text{Put}(K)/K$. The floor ratio, not the slope, is how you tell the two apart in data. Figure 6-B.4 draws both, the floor ratio on the left and the wing with its bound on the right.

![Figure 6-B.4: With a jump to default the put price per dollar of strike flattens at the unit recovery claim (4.7 cents here) instead of falling toward zero (left), and the implied volatility of low-strike puts must stay above the bound (6B.3), which is 78.5% at a strike one-fifth of the forward (right). Illustrative: Merton (1976) jump to zero with spot 100, diffusive volatility 40%, r = 4%, λ = 5% and T = 1, priced with (6B.1) and inverted with implied_vol() of Listing 6-B.1.](assets/figures/ch06b_jtd_put_floor_and_wing.png)

#### The Full Derivation: the corridor leak and the wing bound

*The corridor leak, (6B.2).* *Proof.* The error is $\varepsilon=e^{-(r+\lambda)T}\,\mathbb{E}\big[(B-\tilde S_T)^+-(A-\tilde S_T)^+\big]/(B-A)$. The bracket divided by $B-A$ lies in $[0,1]$ and is zero whenever $\tilde S_T\ge B$, so $\varepsilon$ is non-negative and at most the discounted probability that the surviving path ends below $B$. $\square$

*The wing bound, (6B.3).* *Proof.* For any Black–Scholes put, $\text{Put}_{\text{BS}}(K;\sigma)/K\le e^{-rT}N(-d_2(\sigma))$, since the subtracted term $S_0N(-d_1)$ is positive. By (6B.1) the jump put is at least $KU^{\text{Eur}}=Ke^{-rT}(1-e^{-\lambda T})$. At the implied vol the two prices are equal, so $N(-d_2)\ge1-e^{-\lambda T}$, that is, $d_2\le c$. Write $x=\sigma_{\text{imp}}\sqrt T$ and $L=\ln(F_0/K)>0$, so $d_2=(L-\tfrac12x^2)/x$. Then $d_2\le c$ is $x^2+2cx-2L\ge0$, whose positive root gives (6B.3). $\square$

### 6-B.5.6 Hedging a jump with an instrument that diffuses

> **Math, Gently.** *The compromise delta.* You own something that loses a little when the stock dips and a lot when the company dies, and you are allowed exactly one hedge: shares. How many? If only dips happened, you would short just enough shares to cancel the small sensitivity. If only death happened, you would short enough to cancel the big loss. Both happen, so the variance-minimizing answer is a weighted average of the two hedge ratios, weighted by how much variance each risk contributes: the diffusion's $\sigma^2$ against the jump's intensity $\lambda^{\mathbb{P}}$. *A number for the margin:* stock volatility 80%, so $\sigma^2=0.64$; a physical default intensity of 10% a year; a claim whose diffusion delta is $f_S=-0.05$ and whose jump delta is $j=-5$ (it moves a hundred times more per dollar of stock in a default than in a dip). The compromise is $\Delta^*=\big(0.64\times(-0.05)+0.10\times(-5)\big)/(0.64+0.10)=-0.532/0.74=-0.72$ shares per unit. That over-hedges the everyday diffusion fourteen times ($0.72/0.05$) and under-hedges the default about seven times ($5/0.72$). Every ordinary day the hedge is wrong in one direction, and on the one day that matters it is wrong in the other. The formula is next; the SVB replay above is the week that arithmetic was tested.

A claim $f(t,S)$ on a defaultable stock has two risks: the diffusion, with sensitivity $f_S$, and the jump, which changes its value by $f(t,0)-f(t,S)$ while the stock changes by $-S$. Hedge with $\Delta$ shares. Under $\mathbb{P}$, with physical intensity $\lambda^{\mathbb{P}}$ (the hedge is about what will happen, so it uses the physical intensity), the instantaneous variance of the hedged position is

$$
\frac{\operatorname{Var}^{\mathbb{P}}}{dt}=\sigma^2S^2\big(f_S-\Delta\big)^2+\lambda^{\mathbb{P}}S^2\big(j-\Delta\big)^2,\qquad j\equiv\frac{f(t,S)-f(t,0)}{S}.
$$

Here $j$ is the *jump delta*: the hedge ratio that would exactly offset the default. Minimizing over $\Delta$ is a weighted average:

$$
\Delta^{*}=\frac{\sigma^2\,f_S+\lambda^{\mathbb{P}}\,j}{\sigma^2+\lambda^{\mathbb{P}}},\qquad \min\frac{\operatorname{Var}^{\mathbb{P}}}{dt}=\frac{\sigma^2\lambda^{\mathbb{P}}}{\sigma^2+\lambda^{\mathbb{P}}}\,S^2\big(f_S-j\big)^2 .
$$

The residual is zero only if $f_S=j$, which means the claim is linear between 0 and $S$, a share or cash. For anything with curvature, one hedge instrument cannot neutralize two risks. One instrument, two risks: one equation short. For bought CDS hedged with stock, $j$ is roughly minus the protection payout divided by the share price, a large negative number, and $f_S$ is the small negative CreditGrades delta, so $\Delta^*$ is a compromise that hedges neither risk properly. That is the §23.5 observation that the stock "leaves almost all of the jump on the table," now with the formula behind it. The repair is a second instrument that also jumps: a put spread, which by (6B.2) jumps by its width at default and barely diffuses. Two instruments, two risks, solved.

Notice which intensity went where: the *price* uses $\lambda^{\mathbb{Q}}$, the variance-minimizing *hedge* uses $\lambda^{\mathbb{P}}$, and one engine needs both, labelled (§6-B.6).

> **Ways This Blows Up.** *The slow bleed.* A name that drifts to zero over years (GM 2005–09, §23.3) diffuses through every corridor, so the leak is the whole price and your "default claim" is a vol position. *Borrow.* Hard-to-borrow puts are rich because shorting is expensive, not because default is likely; strip borrow from parity first (§23.4). *Which default?* The put floor measures the intensity of *equity wipe-out*. A distressed exchange can default the bonds and leave the equity alive, and an uptier can crush the excluded bonds while the stock rallies (§14.1, §23.6). The put chain cannot see the distressed-exchange intensity $\lambda_D$ of §14.2. Comparing a put-implied hazard with a bond-implied hazard compares two different events unless you say which one. *American versus European.* Listed puts are American: use $U^{\text{Am}}$, and tag every chain with its convention.

Used in: §5.3 (jumps in continuous time), §8.3, §10.9 (trend when the underlying jumps), §16.4 (warrants), §18.6 (the HJB with jump-to-default, which inherits the $\mathbb{P}$-hedge/$\mathbb{Q}$-price split), §23.3–23.5, §28.4 (Kelly with a jump).


#### Shop life: the column that was a hundred times too small

*A fictional composite. The firm, the people and the numbers are invented; the rhythms are drawn from public accounts of trading-firm life, and the Jane Street details are from its* Signals and Threads *podcast, used here only as analogy.*

The firm is a mid-sized systematic credit manager on two floors of an office building with good coffee and slow elevators. Rafael is a second-year quant there, and his Thursday is a reconciliation nobody wanted. On Wednesday afternoon the hedge desk had sent a one-line message to the quant channel: *why is this month's swaption ticket so small?* The high-yield book rebalances its volatility hedge monthly, buying payer swaptions on the CDX high-yield index against the bonds' short vega, and this month the system had asked for \$4mm of notional. The same book had needed something closer to \$50mm the year before *(illustrative)*.

Rafael's morning is the boring part, and it is most of the job. The 8:30 standup, where he says "looking into the swaption sizing" and nobody asks a follow-up. A support ticket to the risk-data vendor, which promises a reply in two business days. Two CSV files of Greeks, one from the firm's own risk engine and one from the vendor's feed, opened side by side and differenced line by line, with lunch eaten over the keyboard. At 2:10 he finds it. The firm's engine reports bond vega per vol point, the way the cold open's report does. The vendor's feed, which supplies the swaptions' Greeks, reports vega per 1.00 of volatility, the way the closed form in §6-B.3.2 does. The netting script added the two columns as if they were the same unit. For three weeks the book's vega had shown about −\$180,000 per point on the bonds against about +\$180,000 on the swaptions, a net of nearly zero, and nearly zero looked right. The swaptions' real vega was about \$1,800 a point. The book had been short about \$178,000 of vega per point the whole time, and the monthly rebalance, seeing a hedged book, had asked for almost nothing.

The harder part was finding out *when*. The vendor had switched the feed's unit in a release three weeks earlier, with a sentence in the release notes, and then, helpfully, restated its whole history in the new unit. Today's vendor archive therefore showed per-1.00 numbers for every date, including the dates when the firm's script had been reading per-point numbers correctly. To know which hedges had been sized on which unit, Rafael needed last Tuesday's file as it had arrived, not as the vendor later corrected it. Jane Street's engineers describe the same trap on their firm's podcast: vendors "tell you, whoops, made a mistake," which is why the firm saves "all the data ... along with the time we received it," so that nobody needs a time machine to replay a decision (*Signals and Threads*, episode with Eric Mannes, 2 Sep 2026, which also recalls a commodities risk system that was "a large Microsoft Excel spreadsheet"). Rafael's firm had an as-received archive for prices and not for Greeks. It has one now.

The cost was one re-hedge at a worse volatility. While the book sat unhedged, implied volatility on the index swaptions rose by about three points, so buying \$178,000 of vega a point cost about \$530,000 more than it would have three weeks earlier *(illustrative)*. Nobody was fired. The schema now carries a unit field on every Greek, and the netting step refuses to add two columns whose units differ, which is the same idea as the measure tag of §6-B.6.6 applied to a different label. The sentence the shop says now, usually to new hires and occasionally to vendors, is four words long: *vega has a unit.* §6-B.9's Ways This Blows Up box keeps the one-line version.

## 6-B.6 The Two Measures: Girsanov for Intensities and the Premium Ratio

### 6-B.6.1 Desk framing: the eleventh column

Section 6.3 gave Ines's napkin: $\mathbb{P}$ is what happens, $\mathbb{Q}$ is what the table charges you to find out. It then changed measure for a diffusion, where only the drift moves. Credit's main risk is a jump with an intensity, and the measure change for a jump changes *how often the bad thing happens*, which is precisely the number a CDS quote and an agency default study disagree about. This section derives it, names the multiplier, and makes it something a desk can rank and trade.

### 6-B.6.2 Girsanov for a Brownian motion, with the density written down

Chapter 6's box loaded the dice: Girsanov's theorem for a Brownian motion reweights the paths so that the firm's assets drift at $r$ instead of $\mu$, and leaves the volatility alone (§6.3.2 states the result). The object that does the work is a density, $Z_T=d\mathbb{Q}/d\mathbb{P}$, built from the market price of asset risk $\eta=(\mu-r)/\sigma_V$. (Chapter 6 wrote this ratio out longhand; $\theta$ is taken by the CIR long-run level of §6.7.) Under the new measure $W^{\mathbb{Q}}_t=W_t+\eta t$ is a Brownian motion and $dV_t=rV_t\,dt+\sigma_VV_t\,dW^{\mathbb{Q}}_t$: the bad paths count for more, the good ones for less, by exactly enough that the asset is priced as if it earned $r$. The density itself, the check that it is one, and the reason the volatility survives the change are in the Full Derivation at the end of §6-B.6.3.

### 6-B.6.3 Girsanov for an intensity: the hazard multiplier

> **Math, Gently.** *Two parts: speeding up the clock, then splitting the bill.* **Part one.** Chapter 6's Girsanov box loaded the dice. It made the bad paths count more without changing how hard the dice are thrown. A default is not a die rolled on every tick; it is a bell that rings now and then, on the Poisson clock of Chapter 6's other box. Changing measure for a bell does something the dice trick cannot do: it changes how *often* the bell rings. If the market's clock runs 2.34 times as fast as yours, every year of survival in your world counts as 2.34 years of survival in the market's, and survival compounds. So risk-neutral survival is physical survival raised to the power 2.34: Theo's 94% one-year survival is $0.94^{2.34}=0.865$ in the market's eyes, which are the two curves of Figure 6-B.5 (§6-B.8 is where the 2.34 comes from). **Part two.** A spread is a bill with three lines on it. Suppose you think a name defaults at 3% a year and loses 50 when it does: expected loss, 150 bp a year. The market charges as though it defaulted at 6% and lost 70, a spread of $6\%\times0.70=420$ bp. Split the bill. Your expected loss is 150. The extra frequency, priced at your loss, is $(6\%-3\%)\times0.50=150$: the hazard premium. The extra loss, priced at the market's frequency, is $6\%\times(0.70-0.50)=120$: the recovery premium. And $150+150+120=420$, to the basis point. The exact statements are next: (6B.4) here, (6B.5) in §6-B.6.4.

Change the measure on a Poisson default clock with physical intensity $\lambda^{\mathbb{P}}$ by a constant multiplier $\xi>0$ (here $\xi$ is the hazard multiplier; Chapters 5, 12 and 14 use $\xi$ locally for unrelated quantities), and the clock stays Poisson with its rate multiplied:

$$
\lambda^{\mathbb{Q}}=\xi\,\lambda^{\mathbb{P}},\qquad S^{\mathbb{Q}}(T)=e^{-\xi\lambda^{\mathbb{P}}T}=\big(S^{\mathbb{P}}(T)\big)^{\xi}. \tag{6B.4}
$$

**Risk-neutral survival is physical survival raised to the power $\xi$.** With time-varying, even stochastic, multipliers the same construction gives $\lambda^{\mathbb{Q}}_t=\xi_t\lambda^{\mathbb{P}}_t$ (Brémaud's theorem for point processes is the general statement). The diffusion Girsanov could only tilt the drift. The jump Girsanov changes the *rate*, and any $\xi>0$ gives an equivalent measure. No-arbitrage alone does not pin $\xi$: a stock and a riskless bond cannot span a jump, so many $\mathbb{Q}$'s fit the same share price. Only something that pays at default (a CDS, a bond, a low-strike put) pins $\lambda^{\mathbb{Q}}$, only a $\mathbb{P}$ model (a default study, Theo's waterfall) supplies $\lambda^{\mathbb{P}}$, and the multiplier is their ratio.

#### The Full Derivation: the two densities

*The Brownian density.* Fix a horizon $T$ and the constant $\eta$ above. Define

$$
Z_T=\frac{d\mathbb{Q}}{d\mathbb{P}}\bigg|_{\mathcal F_T}=\exp\!\Big(-\eta W_T-\tfrac12\eta^2T\Big).
$$

$Z_T$ is positive with $\mathbb{E}^{\mathbb{P}}[Z_T]=1$, so it defines an equivalent measure: the same events are possible, with different weights. Under $\mathbb{Q}$ the moment generating function of $W_T$ is $\mathbb{E}^{\mathbb{P}}[Z_Te^{uW_T}]=\exp(\tfrac12u^2T-u\eta T)$, which says $W_T\sim\mathcal N(-\eta T,T)$. So $W^{\mathbb{Q}}_t=W_t+\eta t$ is a $\mathbb{Q}$-Brownian motion, and $dV_t=\mu V_t\,dt+\sigma_VV_t\,dW_t=rV_t\,dt+\sigma_VV_t\,dW^{\mathbb{Q}}_t$. The density reweights paths: it makes the bad paths (low $W_T$) heavier and the good paths lighter, by exactly enough that the asset is priced as if it earned $r$. The volatility does not change, because equivalent measures agree on which paths are possible, and quadratic variation is a property of the path.

*The Poisson density.* Now let $N_t$ count defaults, with constant $\mathbb{P}$-intensity $\lambda^{\mathbb{P}}$. For any constant $\xi>0$ define

$$
Z_T=\xi^{N_T}\,e^{-(\xi-1)\lambda^{\mathbb{P}}T}.
$$

The Poisson generating function $\mathbb{E}^{\mathbb{P}}[z^{N_T}]=e^{\lambda^{\mathbb{P}}T(z-1)}$ gives $\mathbb{E}^{\mathbb{P}}[Z_T]=1$, so $Z_T$ is a density. Under the new measure,

$$
\mathbb{Q}(N_T=n)=\mathbb{E}^{\mathbb{P}}\big[Z_T\mathbf 1_{\{N_T=n\}}\big]=\xi^ne^{-(\xi-1)\lambda^{\mathbb{P}}T}\,e^{-\lambda^{\mathbb{P}}T}\frac{(\lambda^{\mathbb{P}}T)^n}{n!}=e^{-\xi\lambda^{\mathbb{P}}T}\frac{(\xi\lambda^{\mathbb{P}}T)^n}{n!},
$$

which is Poisson with intensity $\xi\lambda^{\mathbb{P}}$: that is (6B.4).

### 6-B.6.4 Two premia and a recovery premium

The spread pays for three things, and the identity that separates them is exact:

$$
s=\lambda^{\mathbb{Q}}L^{\mathbb{Q}}=\underbrace{\lambda^{\mathbb{P}}L^{\mathbb{P}}}_{\text{expected loss}}+\underbrace{(\lambda^{\mathbb{Q}}-\lambda^{\mathbb{P}})\,L^{\mathbb{P}}}_{\text{hazard (event) premium}}+\underbrace{\lambda^{\mathbb{Q}}\big(L^{\mathbb{Q}}-L^{\mathbb{P}}\big)}_{\text{recovery premium}} . \tag{6B.5}
$$

(Expand the right side and the cross terms cancel.) The credit triangle (§6.8) sits on the left; the desk's job is the right. Two further distinctions matter in practice.

*The event premium versus the premium on the intensity's motion.* If $\lambda_t$ is stochastic (CIR, §6.7), Girsanov applies twice: to the Brownian motion driving $\lambda_t$, which changes its $\mathbb{Q}$-dynamics and puts a premium for spread *risk* into the curve's slope, and to the default jump itself, which is $\xi$. Jarrow, Lando and Yu (2005) show that if defaults are conditionally diversifiable (independent given the common factors), then $\xi=1$ and every premium lives in the intensity's dynamics. The empirical answer is that $\xi$ is above one and moves around. Driessen (2005) estimates a ratio of risk-neutral to physical default intensity of about 2.3 for ten-year BBB bonds (as summarized in Federal Reserve Bank of New York Staff Report 577).

*Liquidity and tax.* A bond spread also pays for illiquidity and state taxes, both material in Driessen's decomposition; strip them before trusting (6B.5) (§24.3).

> **[SOURCE EXTRACTION]** *Bohn_Stein_Active_Credit_Portfolio_Management p.516:* "CDS prices provide an estimate of risk-neutral expected loss; however, a model is needed to break apart the default probability, the LGD"
>
> **Annotation.** This is the identification problem in one clause: a spread identifies the product $\lambda^{\mathbb{Q}}L^{\mathbb{Q}}$, never the factors, so every "CDS-implied default probability" on a screen has a recovery assumption hidden inside it, usually the 40% convention that Law 7 (App E) calls a quoting convention rather than a forecast. Bohn and Stein's answer is a model. The 2026 desk has a second answer that their 2009 book could not count on: a liquid listed put chain. By (6B.1) the low-strike put floor measures $\lambda^{\mathbb{Q}}$ of equity wipe-out *without* any recovery input, so put floor plus bond spread together identify the market's recovery, subject to the "which default?" caveat of §6-B.5. §6-B.8 does it on Halvorsen.

### 6-B.6.5 The premium ratio as a traded quantity

Define the **premium ratio** of issuer $i$ as spread over physical expected loss:

$$
\text{PR}_i=\frac{s_i}{\lambda^{\mathbb{P}}_iL^{\mathbb{P}}_i}=\xi_i\,\frac{L^{\mathbb{Q}}_i}{L^{\mathbb{P}}_i}.
$$

It is a traded quantity in the most literal sense: selling protection is going long it. Take a single name with $L^{\mathbb{Q}}=L^{\mathbb{P}}=L$, sell protection at $s=\xi\lambda^{\mathbb{P}}L$ for a year and approximate the default count as Poisson. The expected P&L under $\mathbb{P}$, per unit notional, is $s-\lambda^{\mathbb{P}}L=(\xi-1)\lambda^{\mathbb{P}}L$, and the standard deviation of the default loss is $L\sqrt{\lambda^{\mathbb{P}}}$. The single-name Sharpe ratio of harvesting the premium is therefore

$$
\text{SR}=\frac{(\xi-1)\lambda^{\mathbb{P}}L}{L\sqrt{\lambda^{\mathbb{P}}}}=(\xi-1)\sqrt{\lambda^{\mathbb{P}}} . \tag{6B.6}
$$

Recovery drops out, and two numbers are left. A high-yield name with $\lambda^{\mathbb{P}}=2\%$ and $\xi=2$ gives $\text{SR}\approx0.14$. An investment-grade name with $\lambda^{\mathbb{P}}=0.2\%$ and $\xi=4$ gives $3\times0.045\approx0.13$. The larger multiplier in investment grade is not a free lunch: a small $\lambda$ eats a large $\xi$ under the square root. The Sharpe of a *book* scales with the square root of effective breadth, and default correlation is what caps that breadth (Law 2; §28.2). That is also why the premium exists in the first place: if defaults diversified away, Jarrow–Lando–Yu says nobody would be paid for the jump itself.

Ranked cross-sectionally, $\text{PR}_i$ is a signal: a DTS-neutral book selling protection on high-PR names and buying it on low-PR names is long the premium and short the error in the desk's $\mathbb{P}$ model, and its returns are not alpha until the premium it was *supposed* to earn is stripped out (Law 1). The same structure links the Priming Risk Score, a $\mathbb{P}$ object (§13.8), to the SMR break probability, a $\mathbb{Q}$ gauge (§15.4): their gap is a premium ratio for an event that is not default.

> **View From Another Seat.** *The equity-derivatives market maker who sold the wing.* Picture the day of a listed-options market maker, which its own recruiting copy describes plainly: a quarter of an hour on the news before the open, a morning standup on how the market is expected to behave, the afternoon on tools and research, and at four o'clock close to an hour going through the day's trades, including "what we didn't do" (Optiver's intern and trader profiles; recruiting copy, used here for the rhythm only). In that seat a high-yield issuer's low-strike puts are not a credit view. They are inventory that customers keep buying, and the desk's risk system treats them as volatility. Run the premium-ratio arithmetic of this section from that chair and the puts turn out to be credit protection the desk never meant to write: by (6B.1) most of a deep put's value is a default claim, and the desk is short $\lambda^{\mathbb{Q}}$ on every one it sells. It hedges the diffusion with stock, which §6-B.5.6 says leaves the jump on the table, and it hedges the jump where it can, in CDS if a single-name market exists, which for most high-yield issuers it no longer does. The cleanest real example of the stock leg written into a credit document is Hertz's June 2026 financing: \$300mm, upsized to \$350mm, of 6.75% exchangeable first-lien secured PIK notes due 2030, paired with about \$100mm of shares made available to borrow, which is how buyers of exchangeable paper usually get the short they need to hedge (Chapter 16's Docket Diary, §16.6, from press reports in Bloomberg Law and IFR; figures approximate). Read in this chapter's language, that borrow facility is a delta hedge written into a credit document, and its fee is the hedger's cost of carry. The seat's view of Theo's desk is simple: the credit desk is long the recovery it understands, and the options desk is short the default it priced as volatility.

### 6-B.6.6 The rule: say which measure you are in

*Monday 12 October, 3:20 p.m., the afternoon of §6-B.8 (fictional).* Theo is halfway through the Halvorsen decomposition and wants one more input. He types to ROBO: "convert the vendor PD to risk-neutral for the Halvorsen decomposition." ROBO calls `MeasuredPD.to_q` on the vendor's 17.4% and the call raises. The error message is two lines long. The first says the input is tagged `Q`: the vendor's "PD" was backed out of Halvorsen's bond spread at a 40% recovery, so it is already a risk-neutral number. The second says that applying a $\mathbb{P}\to\mathbb{Q}$ multiplier to it would charge the premium twice, which is the commonest error in this whole subject.

Theo reads it three times. At his old firm a probability was a probability. Here it has a passport.

"Every probability on this desk carries a measure tag," Kaz says, without turning round. "`P`, `Q`, or `Q_nominal`. Every expectation in the code has its superscript, and an unlabelled $\mathbb{E}$ is a bug report waiting for an owner. Conversions go through an explicit, sourced multiplier, the $\xi$ of (6B.4) or the structural shift of §6.3.2, never by reusing a number that happens to be lying around."

"And `Q_nominal`?"

"A confession, labelled as one," Ines says. "When nothing that trades spans the risk, a backstop on unlisted equity (§16.3), a warrant before listing (§16.4), a change-of-control put on a deal that may not close (§15.2), the 'risk-neutral' price is a $\mathbb{P}$ model with the drift set to $r$. You report it as a range over $\xi$ or the drift, not as a number." She looks at Theo's screen. "And you use the right measure for the job. Prices and anything implied from them, spreads, put floors, implied vols, are $\mathbb{Q}$. Default forecasts, loss budgets, the hedge ratio that minimizes realized variance in §6-B.5.6 and the size of the position (§28.4) are $\mathbb{P}$. A CDS hazard is not an agency default rate, and an agency default rate is not a hazard until somebody has taken the distressed exchanges out of it (§14.1)."

Theo deletes the request and types a different one: the desk's own structural PD, tagged `P`, 6.0%. ROBO accepts it without comment. That is Law 4 (App E), learned the way most of this desk's laws were learned, by a machine refusing to do what it was told; the Finder table of §6-B.10 keeps its one-line form.

> **[SOURCE EXTRACTION]** *Bohn_Stein_Active_Credit_Portfolio_Management p.181:* "If our objective is valuation of other securities, then we can in fact use the PDs directly estimated from this approach, as risk-neutral PDs are what we require. However, if our objective is to build a portfolio risk model, we need physical PDs, so some transformation will be necessary based upon an estimate and functional form for the market price of risk."
>
> **Annotation.** That is Ines's "right measure for the job," prices in $\mathbb{Q}$ and risk models in $\mathbb{P}$, written in 2009 about PDs backed out of debt prices. The modern desk adds two things. First, the "transformation" is a premium ratio that moves by a factor of ten over a cycle (the Trend Watch at the end of this section), so a fixed functional form is a regime bet. Second, Bohn and Stein note on the same page that risk-neutral PDs may be acceptable for *ranking* obligors, because the transformation rarely reorders them, except among firms with similar risk-neutral PDs and very different systematic risk. That exception is where a premium-ratio book makes its money: two names at one spread, one cyclical and one not, share $\lambda^{\mathbb{Q}}$ but not $\lambda^{\mathbb{P}}$, and only $\text{PR}$ tells them apart.

Used in: §1.3.1 (the bid equation's measure), §3.1, §6.3 (extended here), §11.3–11.4 (PD models are $\mathbb{P}$), §13.8 (PRS), §14.1 and §14.9 (two default rates), §15.4 (the SMR gauge), §16.3 (`Q_nominal`), §24.3 (stripping liquidity before decomposing), §28.4.

Across town, on another firm's floor, the same two-measure mistake had once been made with a position on, and the Pair Book records it.

> **The Pair.** *Pair Book entry PB-07, opened. Owen Achterberg's capital-structure pod at Vantress Capital Management (fictional composites). A replay, cut at the close of Wednesday 17 June 2020; every Hertz date, price and plan term is from the filings and press reports cited in Chapters 6 and 16; sizes, the model's outputs and the borrow fee are illustrative.* **Thesis**, written as a sentence with a date in it: *Hertz's stock is worth less than \$2 and its unsecured notes more than 27; by the confirmation hearing one of those two prices is wrong.* It is Theo's whiteboard card from §6.10.2, "equity worthless, fleet falls," in a pod's handwriting, and it is the pod's $\mathbb{P}$. **Legs.** Long \$10mm face of Hertz's 6% senior unsecured notes due 2028 at 27, \$2.7mm of market value. Short 540,000 shares of old Hertz common at the \$2.00 close of 17 June, \$1.08mm, borrowed through the platform's prime broker. **The hedge.** A $\mathbb{Q}$ delta. Owen reads the plan as the ladder of §6-B.1.4: the notes are a call spread on the value left for the unsecured class, the stock the call struck above them. Price both rungs on one lognormal value and size the short so a small move in that value moves both legs by the same dollars: 40 cents of stock per dollar of notes, Merton's bond-per-equity ratio $N(-d_1)/N(d_1)$ in the plan's units, not resized.
>
> **What the hedge removes.** Direction in $V$: whether the fleet, and with it the estate, is worth more or less next month. Down the path the bond market was pricing that June, the fleet goes to auction, the notes recover in the teens and the stock is cancelled; the two legs roughly offset. **What idio remains.** The disagreement between two prices about one plan value. The pod's fictional run, calibrated to the notes, values a share at about \$0.50 against the screen's \$2.00, so the idio is the stock's premium to the notes' implied value, about \$0.81mm on 540,000 shares if the two prices ever agree. Chapter 12-C will call the thing underneath it, the plan's value, a negotiated random variable, and that is where this pair is stressed.
>
> **What leaks.** The pod is short a call it priced in $\mathbb{Q}$ at a $\mathbb{P}$ it believed. The 0.40 is a slope, and slopes move: if the value climbs toward the point where the notes are paid in full, the notes' delta falls toward zero and the stock's rises toward one, and the pair becomes a short call on the equity with a bond stapled to it, short vega in exactly the sense of §6-B.3.4. The pod had already watched the leak in miniature before it opened. From the filing on 22 May to early June the stock went from about \$0.59 to about \$5.50, while the company itself sold about \$29mm of new shares under a prospectus warning that they "could ultimately be worthless" (Chapter 6, §6.10.2). A short opened at the filing would have been losing more than eight times its own proceeds at the peak (calc). Owen waited for the share sale to be shelved, on 17 June, which is why the replay is cut there. **What it costs.** The notes pay no coupon in the case: post-petition interest on an unsecured claim is unmatured interest, disallowed by §502(b)(2) except where a solvent debtor must pay it, the exception Hertz's noteholders later litigated (Chapter 16, §16.5–16.6). The borrow has no public tape for a bankrupt stock in a retail rally; Wen Zhao assumes 25% a year, which she calls "a guess with a decimal point," and every lender keeps a recall right that a rally makes more likely to be used.
>
> **One line per leg, by measure.** The bond is priced in $\mathbb{Q}$, as a recovery, and sized in $\mathbb{P}$, on Owen's view of the fleet. The stock is shorted at a $\mathbb{Q}$ delta on a $\mathbb{P}$ view, with no listed way to buy back the call it has sold. PB-07 is marked *open*. Chapter 16 closes it, on the day the unsecured are paid in full and old equity receives \$1.53 a share in cash, a share of 3% of the new company and warrants or rights, and writes the sentence this box is building toward: the short leg was the fulcrum's option.

<!-- FIGURE: ch06b_pb07_hertz_pair.png (payoff diagram across plan equity value: long unsecured notes plus short common at the 0.40 Merton delta; the short leg's loss growing without bound as the plan pays equity; the 1.53 cash, 3% and warrants outcome marked; illustrative hedge ratio) -->

The premium that PB-07 sold without noticing is not a constant either, and the last word of this section belongs to the record of how much it moves.

> **Trend Watch.** *The premium moves, and the instruments that read it moved too (2002–2026).* **The ratio is not a constant.** Berndt, Douglas, Duffie and Ferguson (NBER Working Paper 24213, 2018), using Markit CDS against Moody's Analytics EDFs, find premia peaking in 2002, 2008–09 and the second half of 2011; normalized by expected loss, median premia move by more than a factor of ten, and the premium per unit of expected loss rises in distress, more so for investment grade. **The single-name market thinned.** By one 2025 count of cleared volumes, single-name CDS was on the order of 6% of index notional *(approx.; see §23.3)*, so for most high-yield issuers $\lambda^{\mathbb{Q}}$ must now be read from bonds (with a recovery assumption) or from listed puts (with a corridor assumption). **What it means for the desk:** a $\xi$ fitted in 2021 is not a parameter in 2026. It is a state variable, countercyclical, and largest exactly where expected loss looks smallest. Store it as a time series per issuer, not as a constant in a config file.

## 6-B.7 The Desk's Option Book: Eight Instruments You Already Own

*Monday 12 October, 1:05 p.m. (fictional).* Ines pays off the cold open's "Price them" the way she pays off most things, by turning it into a hand. She pulls Theo's forty-one bonds onto one screen, sorts them by rating, and walks down the list with a pen, writing one word next to each line: the row of the table below that it belongs to. Most of the book is the second row, plain high-yield paper, short a put on its issuer. Three names are wide enough to be the first row. Eleven indentures carry a 101 change-of-control put, and two of those have a portability carve-out the sponsor can steer. None of the bonds is a loan, but four of the issuers have term loans that sit in CLOs, so the last two rows are the neighbours whose forced selling moves Theo's prices. And one name, if its lender call goes the way Halvorsen's did, will one day hand him a right, a backstop or a warrant. "Eight instruments," she says. "You own six of them directly and the other two own you." This section is the single home for those readings; each later chapter applies one entry and points back here.

| Instrument | Payoff, in this chapter's atoms | Measure | Home |
| :-- | :-- | :-- | :-- |
| CCC bond | Call spread on assets near its lower strike | $\mathbb{Q}$ price, $\mathbb{P}$ size | §8.3 |
| HY bond | Riskless bond minus a put on assets | $\mathbb{Q}$ | Ch 11 |
| 101 CoC put | Digital(deal) × digital(trigger) × put on post-close price | `Q_nominal` | §15.2 |
| Portability | Short digital on leverage the issuer controls | `Q_nominal` | §15.3 |
| Right / backstop | Call / short put on pre-money value | `Q_nominal` | §16.3 |
| Plan warrant | Diluted long-dated call on a call | $\mathbb{Q}$ once listed | §16.4 |
| Leveraged loan | Floater minus a borrower call at par | $\mathbb{Q}$ | §21.1, §21.5 |
| CLO OC test | Short puts, barrier digitals, short order statistics | $\mathbb{Q}$ prices, $\mathbb{P}$ defaults | §21.4 |

**The CCC bond is an equity option that wears a tie to work (§8.3).** At 1,307 bp the §6-B.3.4 Merton bond is a third of the firm by delta, moves fifty cents per dollar of equity and carries nearly twice the double-B's vega; the coupon, the CUSIP and the trustee are the tie. Its interest-rate duration collapses for the same reason (§8.3's recovery route): the payoff is dominated by the default leg, which does not discount at the Treasury curve. In a multi-tranche structure, a junior bond whose call spread sits near its *lower* strike is even long volatility, like equity, which is the §6-B.1.4 picture.

**High yield is a short put that pays a coupon (Ch 11).** From $e^{-sT}=B_0/(Fe^{-rT})=1-\text{Put}/(Fe^{-rT})$, the spread is the put premium paid in installments: $s\approx\text{Put}/(Fe^{-rT}T)$. For the §6.2.4 firm that is $1.64/76.86\approx2.13\%$ against the exact 2.16%. The P&L shape is the gamma rent of §6-B.3.3: collect the decay, pay for the moves. The Bernoulli default leg has skewness $-(1-2p)/\sqrt{p(1-p)}$, which is why Chapter 11 calls BB defense tail avoidance and CCC defense pricing (§11.10).

**The 101 change-of-control put (§15.2)** pays $\mathbf 1_{\{\text{deal}\}}\mathbf 1_{\{\text{trig}\}}(K-P^{\text{post}})^+$ with $K=101$ plus accrued. A put gated by two digitals, the rating-event one positively correlated with the put's moneyness (§15.2's ratio $M>1$), so multiplying the probabilities underprices it; nothing listed spans a deal closing, hence `Q_nominal`.

**Portability as a digital (§15.3).** A carve-out that cancels the put when pro-forma leverage is below a test $\bar\ell$ makes the holder short $V_{\text{CoC}}\times\mathbf 1_{\{\ell\le\bar\ell\}}$: a digital. §6-B.1.3 says a digital's gamma is unbounded at the strike. §15.3 adds the twist that matters: the counterparty *chooses* $\ell$ after reading $\bar\ell$, so the probability of passing is a decision variable, not a distribution. Kaz's diagnosis is correct, for once: "It's a digital where the other side sets the spot." Ines: "That's not a digital. That's a gift."

**Rights and backstops (§16.3).** The right attached to a plan share is $\frac{m}{n_0+m}(x-K)^+$, a diluted call on pre-money value. The backstop is $-\frac{mn_0}{n_0+m}(K-x)^+$, a short put whose fair fee is its Black–Scholes value, under `Q_nominal` because nothing trades on a company that has not emerged (§16.3 says so).

**Plan warrants (§16.4).** A warrant is $1/(1+\omega)$ calls on the diluted equity value, solved as a fixed point; by §6-B.5.3 a jump to zero raises it at a fixed share price. Thirty-year warrants are mostly vega and survival; the Hertz warrants live in §16.6.

**The leveraged loan is short a call (§21.1).** When the borrower can refinance at will, the lender holds $\min(P^{\text{nc}},100)=P^{\text{nc}}-(P^{\text{nc}}-100)^+$, where $P^{\text{nc}}$ is the value of the same loan without the call. In the 101 soft-call window the strike is 101 for repricings. The call caps the price near par and makes the loan negatively convex in spread: tightening is given away, widening is kept. That is §21.5's repricing wave, the borrower exercising. When the borrower is sick the call is far out of the money and the loan is what Merton says every debt claim is, a short put on the firm: Larkspur Foam's 2029 first-lien term loan at 84 (Chapter 13's cold open) is short a put struck where the drop-down basket lets the sponsor move the assets. **A loan is short a call when it is healthy and short a put when it is sick. The one thing it is never long is optionality.**

**The OC test as an option book (§21.4).** The adjusted collateral principal amount (21.5) is a sum of option payoffs on loan prices. The pool is short a put on each defaulted loan struck at the agency recovery, short barrier digitals on discount obligations, and short the lowest order statistics of its own CCC bucket. The cushion $\kappa_k$ of each test is a function of those prices. The diversion of interest when $\kappa_k<0$ is a digital on the cushion, which is where the gamma lives: one CCC downgrade near the trigger moves the equity tranche's cash flow discontinuously. That is the mechanism behind the forced sellers of §11.6 and §16.2.

Used in: §8.3, Ch 11 (especially §11.1 and §11.6), Ch 13 (Larkspur, from the cold open to §13.6), §15.2–15.3, §16.2–16.4, §16.6, §21.1, §21.4–21.5.

## 6-B.8 Worked Case: Halvorsen on Monday, One Bond, One Put, Three Measures

*Live, Monday 12 October 2026. Halvorsen is fictional; its capital structure is in the issuer bible of the front matter. All numbers are illustrative.*

Go back to the Monday of the cold open. The replays came later in the week; this is the afternoon the question was asked. At 2:10 p.m. the Halvorsen 7.25% senior unsecured notes due 2029, which opened this morning at 78, are still at 78. The stock is \$6.00, down 60% since Friday's 8-K. The one-year listed \$1 put is \$0.136 mid, and the at-the-money implied vol is 80%. `bondmath.py` (Chapter 4-B) gives the notes a Z-spread of 1,150 bp. Theo's own numbers are $\mathbb{P}$ numbers: the desk's structural model gives a one-year default probability of 6.0%, and his RSSG waterfall, run on the documents and not the summary, recovers 40 cents for the notes.

Ines writes the three numbers on the whiteboard in a row, \$0.136, 1,150 bp and 6.0% / 40, and draws a line between the first two and the third. "This morning you asked whose probabilities go into the expectation," she says to Theo. "Two of these are the market's. One is yours. Before anybody computes anything, cards."

#### The card: two prices and a view

*Write three things: what the \$0.136 put is a price of, what the 1,150 bp is a price of, and which of the two numbers you would bet against.*

Kaz writes without looking up. *Both are volatility. The put is 80% vol on a \$6 stock; the spread is asset vol through Merton. Bet against the put: at 80% a \$1 strike is six standard deviations away.*

Mags writes one word, then, because Ines raises an eyebrow, a sentence. *Recovery. The put doesn't care what the bonds get when it dies, and the spread does.*

Theo writes slowly. *The put is the price of Halvorsen dying. The spread is the price of dying times what the notes lose when it does. I'd bet against the recovery, because that is the only one I have read.*

What would you write? The cards go face down under Ines's coffee cup, and the five steps below grade them.

Kaz checks the first card before anyone asks, because Kaz cannot help it. A Black–Scholes put at 80% on a \$6 stock, struck at \$1, one year, 4% rates: seven-tenths of a cent. The screen says 13.6 cents. "Either the market is insane," Kaz says, "or nineteen-twentieths of that put isn't volatility." Ines says nothing, which is the grade.

**Step 1: the put gives the hazard, without a recovery ($\mathbb{Q}$).** By (6B.1) and (6B.2), the \$1 put is a default claim plus a corridor leak. At 80% vol the leak is about \$0.004 (§6-B.5.4), so the American unit recovery claim is about 0.132, and solving $U^{\text{Am}}(\lambda)=0.132$ gives $\lambda^{\mathbb{Q}}\approx14.5\%$. No recovery assumption was needed: in a wipe-out the stock goes to roughly zero whatever the bonds recover.

**Step 2: the bond gives the product, so the pair gives the recovery ($\mathbb{Q}$).** The credit triangle on the flat-curve approximation gives $L^{\mathbb{Q}}=s/\lambda^{\mathbb{Q}}=0.115/0.145=0.793$, so the market's recovery is about 21 cents. Every "CDS-implied PD at 40% recovery" screen hides that number.

It is 3:20. This is the point at which Theo asked ROBO to convert a vendor PD for the next step and the request bounced (§6-B.6.6); he uses the desk's own structural number instead, tagged `P`.

**Step 3: Theo's numbers ($\mathbb{P}$).** $\lambda^{\mathbb{P}}=-\ln(1-0.06)=6.19\%$ and $L^{\mathbb{P}}=0.60$. The hazard multiplier is $\xi=14.5/6.19=2.34$, close to the Driessen benchmark: the market's fear of default *frequency* is ordinary. The premium ratio is $\text{PR}=0.115/(0.0619\times0.60)=3.10$.

"Two point three four," Kaz says. "That's a textbook number."

"That's the point," Ines says. "The market isn't panicking about whether Halvorsen dies. It's charging the ordinary premium for the frequency. Look at what's left over."

**Step 4: decompose the spread with (6B.5).**

| Component | Formula | bp |
| :-- | :-- | --: |
| Expected loss | $\lambda^{\mathbb{P}}L^{\mathbb{P}}$ | 371 |
| Hazard premium | $(\lambda^{\mathbb{Q}}-\lambda^{\mathbb{P}})L^{\mathbb{P}}$ | 499 |
| Recovery premium | $\lambda^{\mathbb{Q}}(L^{\mathbb{Q}}-L^{\mathbb{P}})$ | 280 |
| Spread | $\lambda^{\mathbb{Q}}L^{\mathbb{Q}}$ | 1,150 |

The disagreement is not about whether Halvorsen defaults. It is about what the notes are worth when it does: 280 bp of the spread is the market paying Theo to hold a recovery view. Mags reads the table twice. "Twenty-one cents for a senior unsecured with a drop-down basket in the credit agreement? I've seen worse. I've seen twelve. But I've also read this one, and the basket's been used." Theo has read it too. Recovery is the one question on this desk where an ex-RSSG banker has a genuine edge, and this chapter has been about extracting it cleanly enough to bet on. Figure 6-B.5 shows the two survival curves behind steps 1 to 3 and the decomposition as bars.

![Figure 6-B.5: For Halvorsen, the put-implied risk-neutral hazard of 14.5% is 2.34 times Theo's physical 6.19%, so one-year survival is 86.5% in the market's eyes against 94.0% in his (left), and the 1,150 bp spread splits into 371 bp of expected loss, 499 bp of hazard premium and 280 bp of recovery premium (right). Illustrative: the fictional Halvorsen notes, with the numbers of §6-B.8 computed by spread_decomposition() of Listing 6-B.1.](assets/figures/ch06b_halvorsen_two_measures.png)

The table is a description; step 5 is a position. Theo wants to own the one line he believes is wrong, the recovery premium, and nothing else. That means owning the notes, which carry all three lines, and selling off the two he has no view on: the expected loss, which he agrees with, and the hazard premium, which he has just been told is ordinary.

**Step 5: isolate the recovery view.** Buy the notes and buy enough \$1 puts that the default payoff is zero *at the market's recovery*. Per 100 face the notes lose $78-21=57$ points at default, so buy 57 points of put payout: \$570,000 of \$1 strikes, 5,700 contracts per \$1mm face, costing about \$77,500. In the recovery-of-market-value approximation of §6.6.3, with constant intensities and payment at default, the expected excess return per year in points is, for the notes, $\lambda^{\mathbb{Q}}(78-R^{\mathbb{Q}})-\lambda^{\mathbb{P}}(78-R^{\mathbb{P}})$, and for the puts $-(\lambda^{\mathbb{Q}}-\lambda^{\mathbb{P}})\times57$. Add them and the hazard premium cancels exactly:

$$
\mathbb{E}^{\mathbb{P}}[\text{excess return}]\approx\lambda^{\mathbb{P}}\big(R^{\mathbb{P}}-R^{\mathbb{Q}}\big)=0.0619\times19\approx1.2\text{ points per year}.
$$

All of it arrives in the default state: plus 19 points if Theo's 40 is right, nothing at 21, and a loss below 21. If Theo's recovery were certain, the Sharpe ratio would be $\lambda^{\mathbb{P}}\Delta R/(\Delta R\sqrt{\lambda^{\mathbb{P}}})=\sqrt{\lambda^{\mathbb{P}}}\approx0.25$, the same shape as (6B.6). Uncertainty about recovery only lowers it. This is a recovery bet with the default probability hedged out. It is the RSSG trade, finally isolated, and it is small, honest and slow. Figure 6-B.6 shows the payoff at default and the cancellation of the hazard premium.

![Figure 6-B.6: Buying 57 points of put payout against the notes makes the payoff at default zero at the market's 21-cent recovery and +19 points at Theo's 40 (left), and the hazard premium cancels between the notes (+5.9 points a year) and the puts (−4.7), leaving the 1.2 points a year that is the recovery view alone (right). Illustrative: the fictional Halvorsen notes bought at 78, with risk-neutral and physical hazards of 14.5% and 6.19% as in §6-B.8; the left panel is before carry and the put premium.](assets/figures/ch06b_halvorsen_recovery_bet.png)

Ines makes him say it as a pair, because that is how the pods across town will see it when his orders reach them. "Long the notes, long the puts. What does the second leg remove?"

"The default event at the market's recovery," Theo says, "and with it the hazard premium, because I'm paying the same $\lambda^{\mathbb{Q}}$ on the puts that I'm collecting on the notes. What's left is $R^{\mathbb{P}}-R^{\mathbb{Q}}$, nineteen points, paid only if it dies."

"What leaks?"

"Anything that isn't a clean wipe-out with my recovery on the other side. We'll get to that."

"What does it cost?"

He reads it off Figure 6-B.6. Per 100 face, the notes earn about 5.9 points a year of excess return over the riskless rate in this approximation, and the puts give back about 4.7 of it, so the view nets 1.2. In cash, the puts cost about \$77,500 up front per \$1mm of notes, almost eight points, against a coupon of 7.25 on a bond financed at 78. "It's a position that pays for its own insurance and keeps about a point and a bit," he says. "If I'm right."

Kaz runs the chain through `credit_options.py` while they talk, to make sure the hand arithmetic and the module agree. At 3:40 they do not, quite, by a quarter of a cent; §6-B.9 has the reason, and it is not a bug.

Theo checks the boring part last, which Ines says is the part that should come first. The \$1 puts have open interest in the tens of thousands of contracts and a market a penny wide either side of 13.6 cents *(illustrative)*; 5,700 contracts is a size the screen can absorb without the desk's own buying becoming the price. The notes are another matter, and he has known since Friday at 2:58 what a no-bid in that name feels like.

Ines lets him put it on in a size she calls tuition: \$1mm face of the notes against 5,700 contracts of the \$1 puts *(illustrative)*. Then she asks the question she asks of every position on the day it opens: what kills it? The answers come from three chairs.

"*Which default?*" Ines says first. "A distressed exchange that leaves the equity alive pays the puts nothing while the notes take the haircut. That's the worst state you can be in, and it's the $\lambda_D$ the put chain can't see (§14.1–14.2). Halvorsen's 8-K said 'liability management transaction.' It did not say 'filing.'"

"*The corridor,*" Mags says. "Your leak is 3% here, and all of it lives in a slow bleed. If this thing drifts to a dollar over two years instead of dying on a Tuesday, your 'default claim' was a vol position the whole time and nobody told the puts."

Theo gives the third himself, because it is his number. "*The recovery is a mixture.* My 40 is a pre-LMT waterfall. It has to be conditioned on who's inside the coalition and who isn't (§14.4), and it should come out of Chapter 12-B's state machine, not out of my old model." He touches the USB stick in his pocket, which for once he does not find comforting.

Ines turns the cards over. Kaz's card bet against the wrong number for the wrong reason: the put was 97% default claim and 3% volatility, so betting against it at 80% vol was betting that Halvorsen could not die. Mags's card named the right number. Theo's named the right number and the right reason, which was not that he was clever but that he had read the documents, and recovery is the one question on this desk where reading the documents is an edge. The reader's card is graded against the same three: if it said "recovery," it is in good company; if it said "volatility," it was in Kaz's.

> **Poker Table.** Ines replays the hand twenty days later: notes 80, puts \$0.12, position flat within a quarter point *(illustrative)*. Theo is disappointed. "That's what a hedged recovery bet does before the river," Ines says. "Nothing. You bought the right to be paid for being right about one number on one day. If it makes money before that day, find the risk you forgot to hedge."

Used in: Ch 1 cold open (Halvorsen), §13.8 (PRS as the $\mathbb{P}$ input), §14.1–14.4 (which default, which recovery), §23.3–23.6 (the put-surface engine and cap-structure trades), §24.3 (stripping basis effects before using the bond's spread), Ch 12-B.

## 6-B.9 Specification for AI Implementation: `credit_options.py`

**The Spec You Hand the Robot.** *What ROBO built from the vague version* ("price Halvorsen's puts"): a Black–Scholes pricer at the 80% at-the-money vol that valued the \$1 put at \$0.007 and reported "default probability: 0.0%." Every line was correct, and the answer was wrong by a factor of 20, because nobody told ROBO that the stock can jump to zero. The precise spec follows.

*Module.* `credit_options.py`, imported by Chapters 8, 11, 15, 16, 21, 23 and 28. Pure Python plus `numpy`; no `scipy`, so that normal tails are computed with `math.erfc` and stay accurate below $10^{-10}$.

*Units and conventions.* Prices per unit of underlying (or points per 100 face); rates, vols and intensities as annual decimals; $T$ in years, with day count converted by the caller. No dividends; borrow is stripped before the call. Every probability object carries `measure ∈ {"P","Q","Q_nominal"}`.

*Edge cases and guards.* $T\to0$ and $\sigma\sqrt T\to0$ return discounted intrinsic, not NaN. Implied vol outside no-arbitrage bounds returns NaN with a reason string. Newton steps that leave the bisection bracket are replaced by bisection. Convergence is tested in price units. `MeasuredPD.to_q` refuses anything that is not a $\mathbb{P}$ probability and refuses an unsourced multiplier, which makes double-counting the premium a runtime error instead of a career event. `hazard_from_put` raises if the quoted put is cheaper than its own diffusive part (bad vol, borrow or stale quote).

Everything in this chapter so far was done once, by hand, for one stock. Halvorsen's put gave a hazard, the hazard gave a decomposition, and the decomposition cost a page and three measures to explain. A desk does not get to do anything once. It reprices a few hundred names before the open, from put chains that go stale about when the coffee does, and it hands the answers to seven other chapters that will trust the units without checking them. By hand there are a dozen places where a $\lambda$ can come from the wrong measure or a vega can be off by a factor of 100. Automation does not remove those mistakes; it repeats them at scale, unless the module is built to refuse them. This one is.

The module has three layers. The first is arithmetic you stop thinking about: `norm_cdf` through `erfc`, `norm_pdf`, a bisection `norm_ppf`, then `bs_price` and `bs_greeks`. The `rate` argument may be $r$ or $r+\lambda$, which is how one function prices both a plain stock and the diffusive part of a defaultable one. `bs_price` refuses a non-positive spot or strike and sends default states to `jtd_price`; `bs_greeks` raises at expiry rather than invent a gamma. `implied_vol` brackets the answer between 0.01% and 1,000% vol, starts from the Brenner–Subrahmanyam guess, accepts a Newton step only if it stays inside the bracket, and otherwise bisects. It returns `(sigma, status)`, never a bare number.

The second layer is credit. `merton` prices debt as a riskless bond minus a put on assets and returns equity, spread, a $\mathbb{Q}$-tagged default probability $N(-d_2)$, the bond's Greeks and the bond-per-equity hedge ratio $N(-d_1)/N(d_1)$. `urc_eur` and `urc_am` are the unit recovery claims; `jtd_price` is (6B.1). `corridor_leak` and its bound measure the diffusion a low-strike put still carries, (6B.2). `hazard_from_put` bisects on $\lambda\in[0,5]$ until the put per unit strike matches the quote. `wing_floor_vol` is (6B.3), `jump_hedge_ratio` takes $\lambda^{\mathbb{P}}$, and `spread_decomposition` splits a spread into expected loss, hazard premium and recovery premium and asserts that they sum back to it. `MeasuredPD.to_q` converts only a $\mathbb{P}$ probability, only with a sourced multiplier.

The third layer is the proof. `_self_test` checks parity, the §6.2.4 firm, the $\lambda=0$ reduction, implied-vol round trips above the wing floor, the \$1 put, the Halvorsen chain and a seeded Monte Carlo within four standard errors. It runs on import: comforting in a notebook, wasteful in a nightly job.

At 3:40 on the Halvorsen afternoon the round trip did not close. Kaz had fed the \$0.136 put into `hazard_from_put`, got $\lambda\approx14.5\%$, and repriced it with `jtd_price` as a check, the way you add a column back up after subtracting. The answer came back \$0.1333, a quarter-cent short of the quote. Nothing was broken. `hazard_from_put` defaults to `american=True` and uses the corridor claim, while `jtd_price` always uses the European one, so the two functions were answering slightly different questions about the same put. Passed `american=False`, the round trip closes exactly, at $\lambda\approx14.8\%$. The desk's habit since that afternoon is one convention per workflow, written down next to the number it produced.

The module is at home pricing single-name, dividend-free European options and reading a hazard off a liquid low-strike put. It is blind where a distressed exchange is the likely default, because the put never sees that default; Ines's first answer to "what kills it" on Halvorsen is the module's limit, said by a person instead of a docstring.

*The full listing is [Listing 6-B.1 in Appendix F](#code-6b-1).*

> **Ways This Blows Up.** `1 - norm_cdf(9)` is exactly 0.0 in double precision and `norm_cdf(-9)` is not, so every tail is computed on its small side. `bs_greeks` returns vega per 1.00 of vol and the risk report shows it per point: the factor of 100 is the commonest unit bug in vol code, and Rafael's Thursday (before §6-B.6) is what it costs.

Used in: §8.3 and §8.8 (bond-to-equity sensitivities), §11.3 (structural PDs, tagged $\mathbb{P}$), §15.2–15.3 (`Q_nominal` digitals), §16.3–16.4 (backstops and warrants), §21.4 (pool Greeks), §23.2–23.5 (the surface engine imports `jtd_price`, `hazard_from_put` and `implied_vol`), §28.4.

## 6-B.10 Desk Debrief

**Finder.** Where each idea of the chapter lives: the equation, the gentle version, the scene where somebody had to use it, and the function in Listing 6-B.1.

| Concept | Equation | Intuition (Math, Gently) | Judgment (scene) | Code (Listing 6-B.1) |
| :-- | :-- | :-- | :-- | :-- |
| Payoff atoms and the ladder | §6-B.1.1; $C(a_j)-C(a_{j+1})$ (§6-B.1.4) | Two lunchboxes (§6-B.1.2); the butterfly (§6-B.1.3) | Wolfspeed, 23 Jun 2025 (§6-B.1.5) | `bs_price` |
| Replication | Black–Scholes PDE; gamma rent (§6-B.2.3–2.4) | The factory, two parts (§6-B.2.2) | Veronesi annotation (§6-B.2.4) | `bs_greeks` |
| Two probabilities of one event | $N(d_1)$, $N(d_2)$ (§6-B.2.5) | Two accountants (§6-B.2.5) | §6-B.2.5 and its Full Derivation | `bs_price` |
| Greeks and JTD | §6-B.3.2 table; §6-B.3.5 table | A Greek is a bump (§6-B.3.1) | Theo's eleven columns (§6-B.3.5); SVB (§6-B.5.3) | `bs_greeks` |
| Implied vol and skew | no-arbitrage bounds (§6-B.4.2) | The ground-floor premium (§6-B.4.3) | Desk Myth (§6-B.4.3); SVB's 167 | `implied_vol` |
| Jump-to-default put | (6B.1)–(6B.3) | Funeral and floor (§6-B.5.2); the ridge (§6-B.5.5) | SVB (§6-B.5.3); Halvorsen Step 1 (§6-B.8) | `jtd_price`, `hazard_from_put`, `wing_floor_vol` |
| Jump hedge | $\Delta^*$ (§6-B.5.6) | The compromise delta (§6-B.5.6) | SVB's grade (§6-B.5.3) | `jump_hedge_ratio` |
| Hazard multiplier and premia | (6B.4)–(6B.6) | Clock and bill (§6-B.6.3) | Halvorsen Steps 3–4 (§6-B.8); PB-07 (§6-B.6) | `spread_decomposition` |
| Measure tags | Law 4 (§6-B.6.6) | — | ROBO's refused `to_q` (§6-B.6.6) | `MeasuredPD` |

The rule the `to_q` scene taught, in one line for the table's sake: every probability and expectation carries its measure (`P`, `Q` or `Q_nominal`); prices and implied quantities are $\mathbb{Q}$, forecasts, hedges and sizes are $\mathbb{P}$, and conversion goes only through a sourced multiplier.

- **Write the payoff before you price it.** Every clause is a call, a put or a digital; the capital structure is a ladder of call spreads, and the fulcrum is the one at the money. (Law 8)
- **$N(d_2)$ is a price, not a forecast.** Replication deletes the drift, and $\mathbb{Q}$ is the second derivative of the price list. (Law 4)
- **Theta is the rent you pay for gamma.** A hedged option earns $\tfrac12\Gamma S^2(\sigma_r^2-\sigma_i^2)$; high yield collects the rent and pays the bill in the bad weeks. (Law 6)
- **A put on a defaultable stock is $K$ unit recovery claims plus a diffusive put at $r+\lambda$.** Carr–Wu is that sentence with the leak set to zero, and the wing's implied vol must clear (6B.3). (Law 6)
- **Risk-neutral survival is physical survival to the power $\xi$.** Store $\xi$ per issuer as a time series; it moves tenfold over a cycle. (Law 4)
- **Price in $\mathbb{Q}$, hedge and size in $\mathbb{P}$, and tag both.** An untagged PD is a bug, and `Q_nominal` is a confession. (Law 4)
- **The put chain prices the hazard without a recovery, so bond plus puts identifies the recovery.** That is where the RSSG edge lives (§6-B.8). (Laws 4, 7)

**The Spec You Hand the Robot.** "Implement `credit_options.py` per §6-B.9: Black–Scholes prices and Greeks with `erfc` tails; a bracketed Newton implied-vol solver returning `(sigma, status)`, NaN with a reason outside no-arbitrage bounds; Merton debt Greeks; the jump-to-default call and put (6B.1), European and American unit recovery claims, corridor leak and bound (6B.2), hazard from a put, wing floor (6B.3); a min-variance jump hedge that takes $\lambda^{\mathbb{P}}$; the spread decomposition (6B.5); and a `MeasuredPD` that refuses $\mathbb{Q}\to\mathbb{Q}$. Annual decimals, years. Tests: parity, the §6.2.4 firm, $\lambda=0$ reduction, Monte Carlo within four standard errors at seed 6."

### Exercises

1. *(Payoffs.)* Write Larkspur Foam's first-lien loan, second-lien notes and equity as call spreads on $V_T$. Insert a super-priority uptier tranche at $a=0$ and show which tranche's delta rises most. Which tranche did the Ad Hoc Group just become?
2. *(Measures.)* A screen shows a "CDS-implied PD" of 9% at 40% recovery beside a 4% agency default rate for the bucket. Compute the naive $\xi$, give three reasons it is not a premium ratio (recovery convention, $\lambda_D$, liquidity), and explain to ROBO in one sentence why `to_q` raised. **Check:** naive $\xi=9/4=2.25$ on the probabilities, about 2.31 on the hazards ($-\ln0.91/-\ln0.96$).
3. *(Corridors.)* With (6B.2), find the largest strike on a \$6 stock at 80% vol whose corridor leak is under 1% of $U^{\text{Eur}}$ at $\lambda=14.5\%$. Repeat at 40% vol. Why do low-vol names make better corridor instruments, and why is that exactly when nobody wants their puts? **Check:** by the (6B.2) bound, about \$0.49 at 80% vol and about \$2.04 at 40%; the actual leak, $\text{Put}_{\text{BS}}(6,B,1,\sigma,0.185)/B$, allows about \$0.75 and \$2.72.
4. *(Kaz hedges.)* Kaz proposes offsetting the cold open's −\$41k of vega with equity calls on all forty-one issuers, "because calls are long vega." Using §6-B.1.4 and §6-B.5.3, say what this hedges, what it does not, and what happens on the day an uptier crushes the bonds while the stocks rally.

### Deep-Dive Resource Graph

- **Podcasts:** *Flirting with Models* (Corey Hoffstein), Season 2 Episode 2, "Benn Eifert - Volatility Investing" (30 May 2019; the feed's libsyn page no longer resolves, so no link). *Odd Lots*, "This Is How Derivatives Trading Swallowed the Entire Market" (Benn Eifert, QVR Advisors, 17 Feb 2025), https://omny.fm/shows/odd-lots/this-is-how-derivatives-trading-swallowed-the-enti (how options selling, derivative-embedded ETFs and social-media "volfluencers" reshaped the options market: the market-structure backdrop to the implied-vol quotes of §6-B.4).
- **More Episodes and Lectures (Edition 2):**
  - **"Black Scholes Turns 50"** (*Alpha Exchange*, host Dean Curnutt, 2023-06-26). A trader's reflection on the model at 50: no model is perfect, and option participants adjust for real-world frictions it ignores; the audio companion to what the replication argument assumes in §6-B.2. https://alphaexchange.simplecast.com/episodes/black-scholes-model-and-its-50th-anniversary-lsup4hmm
  - **"Black-Scholes Formula & Risk neutral valuation"** (MIT OpenCourseWare 18.S096, Lecture 19 notes, Fall 2013). Free notes deriving the formula and the risk-neutral argument that §6-B.2.3 to §6-B.2.5 redo in this chapter's notation. https://ocw.mit.edu/courses/18-s096-topics-in-mathematics-with-applications-in-finance-fall-2013/resources/mit18_s096f13_lecnote19/
  - **"Derivatives in a Dynamic Environment"** (Myron S. Scholes, Nobel Prize Lecture, 1997-12-09). The other half of the 1997 prize, delivered the same day as Merton's lecture (Ch 6): read the two together for the replication story of §6-B.2. The PDF is a scanned image, so preview it before assigning. https://www.nobelprize.org/prizes/economic-sciences/1997/scholes/lecture/
  - **"Kris Abdelmessih, Co-Founder, Moontower AI"** (*Alpha Exchange*, host Dean Curnutt, 2024-09-11). A former option market-maker on getting into option trades, providing liquidity to the Street and risk-managing positions: the best audio for §6-B.3, where a Greek is a question somebody asks at 7 a.m. https://alphaexchange.simplecast.com/episodes/kris-abdelmessih-co-founder-moontower-ai-Qw1vbWre
  - **"Damiano Brigo - 22/01/18"** (*Risk.net Quantcast*, Imperial College London, 2018-01-25). A credit-model author on the lost causes, present role and future of quantitative finance: perspective for the measure-change material of §6-B.6 (the feed date is 25 January; the recording is dated 22 January). https://soundcloud.com/user-393208363/risknet-podcast-damiano-brigo-220118
  - **"Paul Wilmott Has Some Feelings About Quantitative Models"** (*Masters in Business*, Barry Ritholtz with Paul Wilmott, 2017-10-13). A derivatives practitioner calling models the "engine room of both the global economy and its most recent meltdown": the skeptic's companion to the "Ways This Blows Up" boxes and the Desk Debrief of §6-B.10. https://omny.fm/shows/masters-in-business/paul-wilmott-has-some-feelings-about-quantitative
- **Practitioner Writing:** OptionMetrics research note on Carr and Wu, https://optionmetrics.com/research/p-carr-and-l-wu-a-simple-robust-link-between-american-puts-and-credit-insurance ; Federal Reserve Bank of New York Staff Report 577 (which summarizes the risk-neutral versus physical intensity evidence), https://www.newyorkfed.org/medialibrary/media/research/staff_reports/sr577.html ; Natenberg, *Option Volatility and Pricing* (book).
- **Academic Papers:** Black and Scholes (1973), *The Pricing of Options and Corporate Liabilities*, JPE; Merton (1976), *Option Pricing When Underlying Stock Returns Are Discontinuous*, JFE; Cox, Ross and Rubinstein (1979), *Option Pricing: A Simplified Approach*, JFE; Breeden and Litzenberger (1978), *Prices of State-Contingent Claims Implicit in Option Prices*, Journal of Business; Brenner and Subrahmanyam (1988), *A Simple Formula to Compute the Implied Standard Deviation*, FAJ; Lee (2004), *The Moment Formula for Implied Volatility at Extreme Strikes*, Mathematical Finance; Jarrow, Lando and Yu (2005), *Default Risk and Diversification: Theory and Empirical Implications*, Mathematical Finance; Driessen (2005), *Is Default Event Risk Priced in Corporate Bonds?*, RFS 18(1), https://ideas.repec.org/a/oup/rfinst/v18y2005i1p165-195.html ; Carr and Wu (2011), *A Simple Robust Link Between American Puts and Credit Protection*, RFS 24(2), https://ideas.repec.org/a/oup/rfinst/v24y2011i2p473-505.html ; Berndt, Douglas, Duffie and Ferguson (2018), *Corporate Credit Risk Premia*, NBER Working Paper 24213, https://www.nber.org/papers/w24213.pdf
- **Data & Code:** `credit_options.py` (§6-B.9); OPRA, the consolidated feed for listed US options, https://www.opraplan.com ; SEC EDGAR for capital structures, https://www.sec.gov/edgar

Used in: every chapter that prices an option or quotes a hazard; the Desk Debrief bullets feed App E (Laws 4, 6, 7, 8) and the front-matter *Tape to Your Monitor*.

<!-- STATUS: COMPLETE -->
