# Chapter 12-B: The Restructuring Process as a State Machine: Documents, Liens, Intercreditor Agreements, Out-of-Court and Chapter 11

> **Prerequisites.** Merton's "equity is a call, debt is a short put" (§6.2) and the recovery conventions of App A §A.6. Nothing else. This chapter is itself the prerequisite for Part IV (Chapters 13–16), for §5.5 and §5.6, and for the docket and claims sections of Chapter 25. If you are about to open Chapter 13, read 12-B first.

## Cold Open: The Waterfall Has a Clock

*Monday 23 November 2026, 8:05 a.m. Day 31 on the clock Chapter 4-C started; Theo's tenth week.* Halvorsen Packaging did not pay the \$18mm coupon on its 6% senior notes due 2031 on Friday. (Halvorsen is fictional, and every number in this chapter is illustrative.) The press release said the company had "elected to utilize the 30-day grace period," which is how a company tells you it has stopped paying without telling you it has stopped paying.

Theo Marsh has drawn the capital structure on the whiteboard as a waterfall: the ABL on top, the first-lien term loan and the 7.25% secured notes side by side, the two unsecured bonds, trade, and a small, sad box labeled "sponsor." Next to it Kaz Lind has drawn the same company as circles and arrows.

"Yours is a picture," Kaz says. "Mine is a state machine. Performing, grace period, forbearance, exchange, petition, emergence. Every arrow has a guard."

"What's a guard?"

"A condition that has to be true before the arrow can fire. A vote, say."

"That isn't a guard," Theo says. "That's the definition of Required Lenders. And your arrows don't say who gets to draw them."

Mags Dunleavy doesn't look up. "You're both wrong. It's a calendar. Thirty days of grace, a hundred and twenty days of exclusivity, and fourteen months of lawyers. Price is what you pay. Recovery is what you get, eventually, after the lawyers. The 'eventually' is the trade."

On Friday afternoon someone asked ROBO to "model the Halvorsen bankruptcy." It returned one number, 40, with a note: *Recovery assumed per market convention. Bankruptcy modeled.*

The desk's own risk system did only a little better. Its status field for a bond takes two values, `PERFORMING` and `DEFAULTED`, and at 7:40 this morning it showed the 6s as performing, because a coupon inside its grace period has not, as a matter of contract, been missed. The CDS screen agreed: a failure to pay counts as a credit event only once the grace period has run out (§24.6). Mags read the field aloud at the 7:45 meeting, the way other people read horoscopes. "Performing. At nine."

Ines Okafor turns her chair a quarter turn. "What's the pot, what are the odds, and who at this table knows more than you?"

"The term loan is 63, the secured notes are 61, the 6s are 9 and the 2045s are 7," Theo says. "The odds depend on which document wins each argument. And the people who know more than me are the ones who have already hired counsel."

He reads the four prices again, slower, the way he used to read a cap table to a client who had not opened the deck. The term loan and the secured notes share the same collateral under the same intercreditor agreement, and they are two points apart. "Same lien, same paper, two points," he says. "The market thinks the loan holders will be in the room and the noteholders will be in the hallway."

"Say you own the secured notes at 61," Ines says. She does not pick the bond idly. Owen Achterberg, whom Theo has known since business school, bought \$10mm of them at 79 on day 3 and shorted the 6s against them (§4C.3). "Which of the next twelve months' events can move your 61, and who holds the pen for each one?"

She takes three index cards from her drawer, the kind she uses for hand histories, and deals one to each of them, face down, as if it mattered which way up they landed. "By Friday, list the five events between now and a plan that can move the 61, who signs each, and which way it moves you."

"Friday is the day after Thanksgiving," Kaz says.

"The bond market closes at two. You have until two."

Offstage, a Rule 2019 statement is being drafted. The Ad Hoc Group, represented by counsel, speaks in unison: *"We have organized. We hold 58% of the first lien. We have signed nothing."* (Cooperation agreements signed in this book so far: still 0. Chapter 13 has the pens.)

Kaz's card is back on Ines's desk before lunch. It has one word on it, *default*, and Kaz defends it to anyone who passes: every other event anyone could write is conditional on that one, and a conditional is a parameter. "Five events is one event and four parameters."

Mags takes until Wednesday and two phone calls she does not explain. Her card says *the DIP*, underlined twice, and nothing else. "Whoever lends the money after the petition writes the plan," she says when Theo asks. "The rest is typing."

Theo fills all five lines on Thursday, on a train to his sister's, with a turkey sandwich on the tray table. The board signs the petition. The lender group signs the DIP, then the judge signs the order. The classes sign ballots. The judge signs the confirmation order. And, circled, *the intercreditor*, with a note in the margin: *pen already used, in 2021; decides whether the notes sit in the term loan's class or behind it.* He is proud of the circle. It is the PJT answer, the document nobody else on the desk has opened.

At 2:05 on Friday Ines collects the three cards, slides them into an envelope and writes *open at the effective date* on the flap. She does this with hands she expects to have misread; a poker player who grades her calls only after she sees the river learns nothing from the river.

Nobody wrote "the challenge period." Hold that thought. §12B.9 opens the envelope and puts a price on what all three cards missed. Before you turn the page, write your own card: five events, who signs each, and which way each one moves a holder at 61.

**The question this chapter answers: which document decides each move, which clock is running, and what is each claim worth in each state?**

By the end you will be able to price each signature on those cards and the wait between them; the Finder table at the head of §12B.11 lists every tool and where it lives.

**How to read this chapter.** Former bankers can skim §12B.1–12B.5 for the formal objects (the min–max threshold, the silo algorithm, the clock table) and slow down for §12B.6–12B.7, where intuition becomes a price. Quants should read it in order.

## 12B.1 Four Documents, One Capital Structure: Who Governs Which Right

At PJT you never asked "what's the recovery?" without first asking "under which document?" Of everything you are bringing to the desk, that habit travels best. A leveraged capital structure is not a stack of claims. It is a stack of claims plus a set of contracts that say who may rearrange the stack, and by what vote. A model that knows the stack but not the contracts will price a Serta-style uptier at zero probability right up to the morning it happens.

Theo had a ritual at PJT for the first night of a new mandate. Before the model, before the first call with the client's CFO, he opened four windows from the data room and tiled them across two monitors in the same positions every time, so that his eyes knew where to go at 1 a.m. Top left, the credit agreement. Top right, the indenture. Bottom left, the security agreement and its cousins. Bottom right, the intercreditor agreement. A fifth document never appeared on the screen, because nobody signs it and everybody is bound by it: Title 11 of the United States Code.

The credit agreement governs the loans, and its signature pages tell you who is in the room: the borrower, the guarantors (usually through a guarantee built into the agreement itself), the administrative agent and the lenders. Theo scrolled past the payment terms, the covenants (maintenance tests for the revolver, incurrence tests only for a cov-lite term loan), the events of default, the pro rata sharing clause, the assignment and buyback rules where the Dutch auctions and the "open market purchases" live, and the limits on affiliated lenders, and he stopped at the amendment section. That section defines "Required Lenders" and lists the "sacred rights" that need each affected lender's consent, which makes it the most valuable page in the document. A public borrower files the whole agreement on EDGAR as an exhibit, which is where Chapter 25's parser finds it (§25.1).

The indenture governs the bonds. Its parties are the issuer and a trustee, with the holders bound by reference. Its incurrence covenants, its change-of-control put (§15.2), its call schedule and make-whole, and its acceleration mechanics (typically the trustee or 25% of holders) were familiar ground. What Theo checked first were its own amendment thresholds: a majority in principal amount for most changes, each affected holder for money terms, and often a supermajority, commonly 66⅔%, to release the collateral on secured notes. Behind those sits a statute. For an indenture qualified under the Trust Indenture Act, §316(b) says that a holder's right to receive principal and interest cannot be impaired without that holder's consent. The Second Circuit's *Marblegate* decision (2017) read §316(b) to protect the *legal* right to payment, not the practical ability to collect it, which is why exit consents and asset transfers survive it. Most 144A high-yield indentures are not TIA-qualified, but they copy the protection by contract.

The bottom-left window was really a folder: the security agreement, the pledge agreement, the mortgages and the deposit-account control agreements. These documents create the liens and perfect them, with a UCC-1 financing statement for most personal property, a recorded mortgage for real estate and control for deposit accounts. They also say what the collateral is *not*: the "excluded assets," such as leased real estate, licenses that prohibit a pledge, and the traditional cap at 65% of a foreign subsidiary's voting stock. Theo learned to respect that folder from a story every restructuring lawyer tells. An unperfected lien is an unsecured claim with good intentions, because in Chapter 11 the debtor-in-possession can avoid it under the §544 strong-arm power, and the cost of one clerical filing has been measured. In 2015 the Second Circuit held that a mistakenly filed UCC-3 termination statement had nonetheless released the lien securing a roughly \$1.5bn General Motors term loan, because the secured party had authorized the filing (*In re Motors Liquidation Co.*, 2d Cir. 2015; amount approx.).

The bottom-right window is the one LMT lawyers open first (§12B.2). The intercreditor agreement (ICA), or for a unitranche the agreement among lenders (AAL), is a contract among the creditor classes themselves, through their agents and trustees; the borrower usually signs only an acknowledgment. It governs lien priority between classes that share collateral, who controls enforcement, the standstills, consent to a DIP loan, waivers of adequate protection and the turnover of proceeds received out of order. It is the only one of the four in which the borrower is not the main counterparty, and that is exactly why it matters on the day the borrower proposes to rearrange everyone else.

The fifth document overrides much of the other four the moment a petition is filed. Under the Bankruptcy Code, ipso facto clauses (terminate-on-bankruptcy) become unenforceable (§365(e), §541(c)), the automatic stay freezes enforcement (§362), and the priority of claims is reset by statute (§507). Contract priorities survive only where the Code lets them: §510(a) enforces subordination agreements to the extent they would be enforceable outside bankruptcy. Of the five windows, it is the one that can close the other four.

Two structural facts sit next to the documents. **Structural subordination** means a creditor of a holding company comes after the creditors of the operating subsidiaries that own the assets, unless those subsidiaries guarantee its debt. **Unrestricted subsidiaries** sit outside the covenant net entirely. A drop-down (§13.6) is the move of value from the first category into the second.

The map the desk keeps on one page:

| Right | Governing document | Who can change it, typically |
| :--- | :--- | :--- |
| Amount and date of payment | Credit agreement / indenture (+ TIA §316(b)) | Each affected lender or holder |
| Covenants and baskets | Credit agreement / indenture | Required Lenders (>50%) / majority of holders |
| Whether a lien exists, on what | Security documents (+ UCC perfection) | Lien release: all lenders (CA) or 66⅔% (secured notes), *typical* |
| Lien priority between secured classes | Intercreditor agreement | The classes party to the ICA, by each one's own threshold |
| Who directs enforcement | ICA (+ agent provisions) | Usually fixed; the "controlling" class directs |
| Pro rata sharing; buybacks | Credit agreement (sharing, assignment sections) | Sacred right, unless a buyback exception reaches it |
| Subordination of loans or liens | Credit agreement amendment section | Majority, unless a Serta blocker makes it sacred |
| Guarantees and their release | Guarantee / credit agreement | Release of "all or substantially all": all lenders, *typical* |
| Change-of-control put | Indenture | Majority before the event; each holder after |
| Everything after the petition | Bankruptcy Code | Nobody; the court applies it |

The table answers "who can change this one right?" A sponsor never asks that. It asks "what is the cheapest set of rights I can change to get the deal I want?", and the answer is a small piece of mathematics.

> **Math, Gently.** *Min–max: the shed with three doors.* Your bicycle is in a shed with three doors. Each door is chained shut with two padlocks, and a door opens only when every padlock on it is open, so a door is exactly as hard as its toughest padlock. A thief needs only one door, so the thief picks the door whose toughest padlock is the weakest: a minimum, over the doors, of a maximum, over the padlocks on each door. Now make the padlocks votes. Door A, a one-step uptier, touches a sacred right (unanimity, 1) and a covenant (a majority, ½), so its toughest lock is 1. Door B, a collateral release plus a basket amendment, touches rights at ⅔ and ½, so its toughest is ⅔. Door C, a drop-down through an unrestricted subsidiary and then an exchange, touches two rights at ½ each, so its toughest is ½. Counsel picks door C, and the deal's effective threshold is ½: a 51% coalition can do what door A said needed everyone. The formal version follows.

**The derivation: a deal's effective threshold is a min–max.** Let a transaction $\mathcal{T}$ be implementable in several ways $\mathcal{I} \in \mathbb{I}(\mathcal{T})$ (one step or three, through this subsidiary or that one). Each implementation modifies a set of rights $\mathcal{R}(\mathcal{I})$, and each right $\varrho$ is protected by an amendment threshold $\theta(\varrho) \in (0, 1]$, the fraction of the relevant class whose consent changes it. The implementation is feasible for a coalition holding share $s$ of the class when $s \ge \max_{\varrho \in \mathcal{R}(\mathcal{I})} \theta(\varrho)$. The coalition gets to pick the implementation, so the threshold that actually binds is

$$
\theta^{\text{eff}}(\mathcal{T}) = \min_{\mathcal{I} \in \mathbb{I}(\mathcal{T})}\ \max_{\varrho \in \mathcal{R}(\mathcal{I})} \theta(\varrho).
$$

In the shed's language, the inner max is the door and the outer min is the thief's choice of door, and the thief has a law degree. That one line is the formal content of liability-management drafting. It is also the formal content of the litigation that follows. When a court collapses a multi-step transaction into one integrated step, as some courts have and others have refused to (Ch 13-B keeps the docket diaries), it shrinks $\mathbb{I}(\mathcal{T})$ to a single implementation whose $\mathcal{R}$ is the union of every step's rights. That raises $\theta^{\text{eff}}$, sometimes all the way to 1. Chapter 13's five clause families (§13.2) are the features from which the desk estimates each $\theta(\varrho)$; this equation is how they combine.

Theo points Kaz at one page of Halvorsen's security agreement, the definitions, and Kaz finds a "springing lien" before anyone can warn them.

"I know," Kaz says. "Not seasonal. It springs into existence when something happens."

"Usually a downgrade or a leverage test," Theo says.

"So it's a knock-in barrier option on seniority." Kaz writes this down, and for once nobody corrects them, because it is exactly right. It also explains why springing liens frighten lawyers. A lien that springs within 90 days before a petition, to secure debt that already existed, is a textbook preference under §547. The barrier tends to get hit just as the option becomes worthless.

Used in: §3.6 (who at the table knows about the LMT), §13.2 (the clause families that estimate $\theta(\varrho)$), §13.6 (drop-downs and unrestricted subsidiaries), §15.2 (the CoC put lives in the indenture), §21.1 (the loan as an instrument), §24.8 (successor and orphan CDS run through the indenture), §25.1–25.3 (the document as a constraint set and a definition graph), Ch 13-B (integrated versus step-by-step rulings).

## 12B.2 Liens, Silos and the Two Kinds of Subordination

"Senior" is the most overworked word in the capital structure. There is senior secured, senior unsecured, even senior subordinated, and every one of them is senior to something.

*A war story; Mags, the grocery chain and its numbers are fictional.* In her second year on a distressed desk, Mags bought a block of a regional grocery chain's senior subordinated notes at 40. She had read the word "senior" on the run sheet and priced the notes against the junior subordinated notes beneath them, which they did indeed outrank. The chain filed eight months later, and she spent the next year learning that "senior" had four different meanings, each of which took a slice of her recovery. The bank had a lien on the stores and the inventory, and lien priority decides who is paid first from the proceeds of a specific pool of collateral; her notes had no lien. The indenture subordinated them in right of payment to "Senior Indebtedness," which included the bank and the senior notes, and payment priority (contractual subordination) decides who is paid first from *any* source of value, so every cent her class collected from the unsecured pool was handed up the line. Her notes had been issued by the holding company, while the stores sat in an operating subsidiary that guaranteed only the bank debt, and structural priority asks whose obligor owns the assets. Finally, the lawyers and the landlords were paid ahead of everyone under §507, which is statutory priority: the order the Code imposes in bankruptcy on administrative, priority and general claims. She had expected 50 and collected 11. "Senior to what," she says now, whenever a new hire uses the word, "and at which buffet?" Confusing the four orderings is still the most common modeling error the desk sees from new hires on both sides of the RSSG–quant divide.

The buffet is hers, and it is the shortest correct version of the distinction. Lien subordination is a contract about collateral. Payment subordination is a contract about distributions. Neither changes what the debtor owes, and both change who keeps what the debtor pays. Lien subordination means you go second at one buffet; payment subordination means you go second at every buffet, including the ones you have not heard about yet.

> **Math, Gently.** *The §506 split: a bucket under a tap.* Picture a lender's claim as a bucket of fixed size, 100, set under a tap that can pour out only what the collateral is worth, 80. The bucket fills to 80, and that is the secured claim. The 20 of empty space does not vanish. It becomes a separate claim, the deficiency, which climbs out of the bucket and walks over to the pool where the unsecured creditors stand. Say the pool holds 60 of unencumbered value, and three claims stand in it: our walker's 20 and two others of 100 each. Each is paid $60/220 = 27.27$ cents on the dollar, so the deficiency collects $0.2727 \times 20 = 5.45$. The lender's total is 80 from the bucket plus 5.45 from the pool: 85.45 on a claim of 100. In symbols, the secured part is the smaller of the claim and the collateral, and the deficiency is whatever is left over; the statute's version is next.

**The secured claim, split in two.** Under §506(a), an allowed claim $C_j$ held by a creditor whose collateral is worth $V^{\text{coll}}_j$ splits into a secured part and an unsecured deficiency:

$$
C^{\text{sec}}_j = \min\big(C_j,\ V^{\text{coll}}_j\big), \qquad C^{\text{def}}_j = \big(C_j - V^{\text{coll}}_j\big)^+ .
$$

The deficiency joins the general unsecured pool. An *over*secured creditor accrues post-petition interest and reasonable fees up to its collateral cushion (§506(b)). An *under*secured creditor accrues nothing: the Supreme Court held in *Timbers of Inwood Forest* (1988) that it is not compensated for the delay. Hold onto that asymmetry. It means time is free to an oversecured lender and pure loss to an undersecured one, and §12B.7 turns it into a price.

**The silo algorithm.** Write the estate as collateral silos $\ell = 1, \dots, L$ with values $V_\ell$ and an unencumbered silo with value $V^{\text{unenc}}$. Each silo carries an ordered list of liens, and recoveries come from four steps taken in order. Inside each silo the liens are paid in lien order, each up to whatever of its claim is still outstanding; crossing liens (an ABL first on receivables and second on fixed assets, and the term loan the other way round) are just two silos with opposite orders. Whatever a secured class is still owed after its silos is its deficiency $C^{\text{def}}_j$. The unencumbered value, net of administrative and priority claims, is then shared pro rata across every general unsecured claim, deficiencies included, at the pool ratio

$$
\rho^{\text{U}} = \min\!\left(1,\ \frac{\big(V^{\text{unenc}} - C^{\text{adm}}\big)^+}{\sum_{j \in \text{GUC}} C^{\text{GUC}}_j}\right),
$$

where $C^{\text{GUC}}_j$ is class $j$'s unsecured claim (its deficiency for a secured class, its whole claim for an unsecured one). Last comes turnover: each class that is contractually subordinated in right of payment hands its pool distribution to its named senior beneficiaries until they are paid in full. That last step is where Mags's 40 became 11.

**Worked example: same claims, different subordination.** Collateral worth 80 secures a first lien of 100 and a second lien of 100. There is 60 of unencumbered value (no administrative claims, for now) and 100 of other unsecured claims. With lien subordination only, this is the bucket of the box: the first lien takes all 80 of collateral, its deficiency of 20 collects 5.45 from a pool paying 27.27%, and it recovers 85.45. The second lien gets nothing from the collateral, files a deficiency of 100, and recovers 27.27, exactly like the other unsecured creditors.

Now make the second lien payment-subordinated to the first as well. The pool still pays the second lien 27.27, but that distribution is turned over to the first lien until the first lien is whole. The first lien is still short $(1 - \rho^{\text{U}})\,C^{\text{def}}_1 = 0.7273 \times 20 = 14.55$. Recoveries: first lien 100, second lien $27.27 - 14.55 = 12.73$, other unsecured 27.27, unchanged. Same claims, same collateral, same pool: 14.55 points moved between two classes because of one sentence in a contract about distributions.

#### The Full Derivation: turnover

In general, with one beneficiary class $b$ and one subordinated class $u$:

$$
\text{Turnover} = \min\Big\{\rho^{\text{U}} C^{\text{GUC}}_u,\ \big(1 - \rho^{\text{U}}\big)\, C^{\text{def}}_b\Big\}, \qquad
R^{\text{pay}}_u = R^{\text{lien}}_u - \frac{\text{Turnover}}{C_u}.
$$

Read the minimum slowly and the rest of the doctrine falls out of it. The subordinated class loses exactly what its beneficiary was still short, capped at its own distribution. The other unsecured creditors are untouched: the benefit of subordination goes only to the classes named as beneficiaries, so trade creditors gain nothing unless the indenture's definition of "Senior Indebtedness" includes trade debt. The definition is therefore the payoff function, which is Law 8 in its purest form: whether a word sits inside or outside a defined term decides a class's recovery to the dollar. Two refinements live in the drafting. Under New York law, a senior class collects post-petition interest out of a junior's distribution only if the subordination agreement says so explicitly (the "rule of explicitness"). An "X-clause" can let a junior keep plan securities that are themselves subordinated, instead of turning them over.

> **[SOURCE EXTRACTION]** *Moyer_Distressed_Debt_Analysis p.403:* "Intercreditor agreements are another mechanism besides indenture provisions to control or specify payment priorities in complex capital structures."
>
> **Annotation.** In Moyer's 2004 text this is a footnote, and in 2004 it deserved to be one: the ICA was mainly a first-lien/second-lien document that told the second lien to stay quiet. By 2026 it is the main event. Three changes moved it from the footnotes to the trading screen. Pari passu intercreditors now sit between term loans and secured notes that share collateral, so the threshold in one document can be overridden by whichever class the ICA makes "controlling." DIP-consent and adequate-protection waivers set in advance what the junior class can stop in Chapter 11 (§12B.5). And unitranche AALs create first-out and last-out classes that the borrower is not even a party to (Chapter 17). The desk encodes the ICA as guards on transitions, not as a static ranking.

Theo reads the provisions aloud from a standard first-lien/second-lien form, one row at a time, and gets as far as DIP consent: the second lien is deemed to consent to a DIP that the first lien provides or approves, up to a cap.

"So the junior pre-agreed to lose a vote it doesn't have yet," Kaz says.

"Years before anyone knew there would be a vote," Theo says. "For a fee of zero."

The rows that matter, read as state-machine objects:

| ICA provision | What it says (typical first lien/second lien form) | Role in the state machine |
| :--- | :--- | :--- |
| Lien priority and waterfall | Proceeds of shared collateral go to the first lien until it is paid in full, then to the second | Sets the order within each silo |
| Enforcement standstill | Second lien may not enforce for a period after notice (often 90–180 days) | A clock on the junior's enforcement transition |
| DIP consent | Second lien is deemed to consent to a DIP the first lien provides or approves, up to a cap | Removes the junior's veto from the DIP transition |
| Adequate protection | Second lien waives objections, keeps only replacement junior liens | Removes a litigation edge |
| No contest | Second lien may not challenge the first lien's liens | Removes a litigation edge |
| Release | Second-lien liens fall away when the first lien releases in an enforcement or §363 sale | Lets the sale transition clear the silo |
| Purchase option | Second lien may buy out the first lien at par plus accrued after a trigger | An American call on the senior class, struck at par |
| Plan and voting covenants | Some ICAs limit how the junior votes; enforceability is contested | A guard with an uncertain value, the court as a random variable (Law 16) |

Used in: §5.5 (recovery conditioned on seniority and collateral), §13.7 (the multi-obligor engine extends this silo algorithm to guarantees and intercompany claims), §14.4 (recovery as a mixture over coalition membership), §16.5 (the unsecured pool and its denominator), §21.8 (CLOs inside the LMT), Chapter 17 (unitranche AALs), App D (the funding and settlement legs).

## 12B.3 Thresholds: Who Can Change the Contract, and Who Can Stop Them

Ines has a rule for this part of the job: "Every threshold is a pot size. The question isn't whether you're right. It's whether you hold enough chips to make the dealer deal with you." A threshold is a price list for coalitions, and the desk needs the list both out of court, where the documents set it, and in court, where the Code does.

**Out of court.** Take an action with threshold $\theta$ measured against a voting denominator. A coalition holding share $s$ can take the action when $s \ge \theta$ (or $s > \theta$ when the document says "more than"). A holdout with share $h$ blocks when the rest of the class falls short, which means $1 - h < \theta$, or $h > 1 - \theta$. So the blocking stake is "50% or more" against a "more than 50%" Required Lenders vote, "more than a third" against a 66⅔% lien release, and a single dollar against a sacred right, *if* the holder counts as affected.

The denominator is a choice variable, and most threshold fights are fought over it rather than over the numerator. Credit agreements exclude defaulting lenders and, usually, loans held by the borrower or its affiliates. Indentures exclude notes held by the issuer. Ines explains what is left the way she explains a home game with a crooked host: "You can shrink the room, pack the room, or change who counts as being in it." Shrinking the room means retiring the loans of the lenders you could not win over, through a buyback exception to pro rata sharing (§13.2, Family 3). Packing it means issuing additional notes of the same series to the coalition before the vote. If the coalition holds share $s$ of face $F$ and receives new face $N$, its share becomes $s' = (sF + N)/(F + N)$. Setting $s' \ge \theta$ and solving,

$$
N \ \ge\ \frac{(\theta - s)\,F}{1 - \theta}.
$$

At $s = 0.59$ and $\theta = \tfrac23$, that is $N \ge 0.23F$: a coalition 7.7 points short of a supermajority needs new notes worth 23% of the series to close the gap, because every new dollar raises the denominator too. "Packing a room is expensive," Ines says, "because the new chairs count." This is the arithmetic of the 2022 Wesco/Incora vote, whose docket diary lives in Ch 13-B. Changing who counts is the cheapest move of the three. If sacred rights protect only lenders "directly and adversely" affected, a transaction designed to affect everyone indirectly turns $\theta = 1$ into $\theta = \tfrac12$ (§13.2 on the *Mitel* reading).

**In court.** Under §1126(c), a class of claims accepts a plan when holders of at least two-thirds in amount *and* more than one-half in number of the allowed claims that actually vote accept it. A class of equity interests needs two-thirds in amount (§1126(d)). Unimpaired classes are deemed to accept (§1126(f)), and classes receiving nothing are deemed to reject (§1126(g)).

> **[SOURCE EXTRACTION]** *Moyer_Distressed_Debt_Analysis p.107:* "For a class to accept the plan, more than 50% in number of claims representing at least 66 2/3% in amount must vote in favor. These thresholds are based on those participating in the voting process, not the full class size."
>
> **Annotation.** The second sentence is the one desks forget, and it turns turnout into a position (derived below). Moyer's warnings about gerrymandering by classification still apply. Since 2004 three things have sharpened them. Rule 2019 statements now give a near-real-time panel of who holds what in each group (§25.7), so the desk can estimate $s$ before the vote. Cooperation agreements turn a scattered class into one blocking stack (§13.5, §14.5). And post-LMT capital structures split one economic class into several legal classes, which multiplies the number of votes a plan has to win.

Moyer's second sentence is a whole model hiding in a footnote's clothes.

> **Math, Gently.** *Turnout: the half-empty town hall.* A town meeting passes a motion unless more than a third of the people *present* vote against it. Your faction is 20 of the town's 100 voters, and it will always show up. If all 100 come, a third of the hall is 33.3 and your 20 is a nuisance. If only half of the other 80 bother to come, the hall holds $20 + 40 = 60$ people, a third of the hall is exactly 20, and your faction is on the edge of a veto. One more absentee and you block. Nothing about your faction changed; the empty chairs did the work. An empty hall makes a small faction large, and that is the whole idea behind the inequality that comes next.

**Turnout is a position.** A holder with share $h$ of a class's allowed amount votes no. The rest of the class, $1 - h$, turns out at rate $t$ and votes yes. The amount test fails when the no votes exceed a third of the amount voting:

$$
h \ >\ \tfrac13\big[h + t(1 - h)\big]
\iff 2h + th \ >\ t
\iff h \ >\ \frac{t}{2 + t}.
$$

At full turnout the blocking stake is the familiar third. At 70% turnout it is 25.9%; at 50% it is the town hall's 20%. In bankruptcy, as in municipal elections, a determined minority's power falls as everyone else's interest in showing up rises. That is why a plan proponent spends real money on solicitation agents and a blocking group says very little in public.

**Numerosity** is the second gate. Each holder generally counts once per class, so 400 trade creditors owed \$30mm can defeat the number test in a class where twelve funds own \$300mm of bonds. Plans answer with a cash-paid *convenience class* for small claims (§1122(b)). The court may *designate*, meaning disqualify, votes not cast in good faith (§1126(e)), as *DBSD* (2d Cir. 2011) did to a strategic buyer that had bought claims to block the plan and take the company. And because cramdown needs one impaired accepting class, not counting insiders (§1129(a)(10)), proponents are tempted to impair a friendly class slightly. Courts split on whether that "artificial impairment" counts, which makes it a guard with a random value.

> **Poker Table.** "A blocking stake is a raise you can make without showing your cards," Ines says. "The rest of the table has to call, fold, or buy you out, and in this game buying you out is called a consent fee." Her hand history: a 34% position in a class whose expected turnout is 60% blocks with eleven points to spare, since the threshold is $0.6/2.6 = 23\%$. So the last ten points of it are worth less to the holder than to anyone who wants to buy a seat at the table *(illustrative)*.

Ines's hand assumes every holder in the class wants the same thing from the plan. One kind of holder rarely does.

> **View From Another Seat.** *A CLO manager (a generic seat; Rachel's, from Chapter 4-C).* To the solicitation agent, a CLO is one more ballot in the first-lien class. To the CLO manager, the ballot is the easy part. The vehicle's indenture, through its eligibility criteria, its reinvestment rules and its coverage tests, decides whether it can hold what the plan pays at all. Takeback paper may need a rating before it counts at par in the overcollateralization test, and new equity is something most vehicles may receive in a workout but would never choose to buy, often carried at little or nothing in the tests and sold when the market allows (Chapter 21). So the manager reads a plan's distribution menu the way a diner with an allergy reads a menu: by what it cannot eat. A cash-paid convenience class, the plan's courtesy to small holders, looks very different from a seat that would happily take less cash to avoid receiving shares it cannot carry. That is why CLO-heavy classes push for first-out takeback paper and cash elections, and why a proponent who needs their votes builds the menu around them.

Used in: §13.2 (Family 2, the per-action $\theta$), §13.4 (threshold games and the sponsor's auction), §13.5 and §14.5 (cooperation agreements as blocking stacks), §16.3 (backstop commitments as the price of votes), §25.7 (the Rule 2019 holder panel that estimates $s$), Ch 13-B (the Wesco/Incora denominator and the remedy rulings).

## 12B.4 The Out-of-Court Menu as Transitions

Kaz's whiteboard was right about the shape and wrong about the content. The restructuring process *is* a state machine. But its guards are document clauses and statutes, and its clocks are what Mags meant by "a calendar." The formal object is a **timed automaton**:

$$
\mathcal{A} = \big(\mathcal{X},\ x_0,\ \mathcal{E},\ \mathbf{c},\ \text{Guard},\ \text{Reset},\ \text{Inv}\big).
$$

Here $\mathcal{X}$ is a finite set of legal-economic states and $x_0$ is the starting state. $\mathcal{E} \subseteq \mathcal{X} \times \mathcal{X}$ is the set of transitions, each labeled by an event: a vote, a filing, a ruling, a payment, a missed payment. $\mathbf{c} = (c_1, \dots, c_m)$ is a vector of clocks measured in days, each increasing at rate one: the grace-period clock, the forbearance clock, the exclusivity clock, the challenge-period clock, the standstill clock. $\text{Guard}(e)$ is a Boolean predicate over the document state (thresholds, blockers, basket capacity) and the clocks, and transition $e$ can fire only when it is true. $\text{Reset}(e)$ lists the clocks that go back to zero when $e$ fires. $\text{Inv}(x)$ is an invariant on the clocks that must hold while the machine sits in $x$. In the grace-period state, for instance, $c^{\text{grace}} \le 30$. When an invariant is about to fail, a transition is forced, and that forced transition is how a default "happens" without anyone deciding it should.

The machine has two layers, and the desk keeps them apart. The automaton says which paths are **legal**. A probability law over the legal paths, which edge fires and when, is what the desk **prices**. The legal layer is close to deterministic and comes from documents and statutes; Chapter 25 parses it. The probability layer is estimated: Chapter 13's Priming Risk Score handles the LMT edges, §25.7.2 the docket edges, and §12B.7 turns the result into a price. Mixing the layers is how ROBO's first draft let a plan be confirmed the instant it was filed. No guard said it couldn't.

The out-of-court states are Performing, Stressed, Grace, Forbearance, Post-LMT, RSA-signed and Petition (the entry into the Chapter 11 sub-machine of §12B.5). The edges:

| Transition | Event | Guard (typical terms) | Clock | Priced in |
| :--- | :--- | :--- | :--- | :--- |
| Performing → Stressed | Liquidity runway falls below about 12 months | None; an economic state | The 13-week model's runway | §13.8 (PRS) |
| Stressed → Grace | Missed interest payment | None | Grace clock starts: often 30 days for bond interest, a few business days for loan interest, none for principal | §14.1 |
| Grace → Event of default | Grace period expires | Invariant fails at $c^{\text{grace}} = 30$ | Forced | Cross-default and cross-acceleration fan out to the other documents |
| Grace or EoD → Forbearance | Forbearance agreement | Required Lenders (loans) or majority (bonds) | Forbearance clock, usually weeks | — |
| Stressed → Post-LMT (A&E) | Amend and extend | Each extending lender opts in (maturity is sacred); non-pro-rata extension must be permitted | — | §21.5 |
| Stressed → Post-LMT (exchange) | Exchange offer with exit consents | Minimum-participation condition (often 90%+); majority to strip covenants | Offer open at least 20 business days (SEC Rule 14e-1) | §13.4 (holdout game), §14.1 |
| Stressed → Post-LMT (uptier) | Non-pro-rata uptier | $s \ge \theta^{\text{eff}}$; no Serta blocker; a buyback exception that reaches the deal | — | §13.3 |
| Stressed → Post-LMT (drop-down) | Transfer to an unrestricted subsidiary plus new structurally senior debt | Basket capacity at least the asset value; no J.Crew or Chewy blocker | — | §13.6 |
| Stressed → Post-LMT (double-dip, pari-plus) | New claims against the same credit group | Debt and lien capacity; guarantee basket | — | §13.7 |
| Any distressed state → RSA-signed | Restructuring support agreement | Signatories at or above ⅔ in amount and above ½ in number of each class the plan will impair | RSA milestones (petition by a date, confirmation by another) | §12B.3 |
| RSA-signed → Petition (prepack) | Votes solicited before the petition (§1126(b)) | Classes accepted | Combined hearing, typically weeks | §12B.5 |
| Any distressed state → Petition (free-fall) | Filing | Board resolution | Stay begins | §12B.5 |
| Post-LMT → Stressed | Re-default | None | The re-default clock | §14.3 |

Two edges carry most of the desk's risk. **Post-LMT → Stressed** is why the Post-LMT state is parole, not immunity (Law 7); Chapter 14 builds its front-loaded re-default clock. **Stressed → Post-LMT** gets three answers to "did it default?" S&P records a selective default, Moody's counts a default event (§14.1), and a standard North American CDS, which has no Restructuring credit event, usually records nothing at all (App D, §24.8). Say which one your labels use (Law 11). Figure 12-B.1 draws the whole menu with its guards and clocks.

![Figure 12-B.1: The out-of-court menu is a state machine whose arrows carry guards and clocks, and the Post-LMT state feeds back into Stressed, so an exchange or uptier is parole rather than immunity. Source: the transition table of §12B.4 (typical credit-agreement and indenture terms, SEC Rule 14e-1 and 11 U.S.C. §1126(b)); no particular borrower.](assets/figures/ch12b_out_of_court_machine.png)

Exit consents are where the menu began: the tendering holders vote to strip the old bond's covenants, so a holdout chooses between a new bond and an old one with no covenants left (§13.4 solves the game). "Back in my day," Mags says, "an exchange offer came with a prospectus and a threat. Now it comes with a co-op and a threat. The prospectus is the part that got shorter."

> **Trend Watch.** *The transition matrix moved out of court, 2018–2026.* S&P counted distressed exchanges at about 32% of rated US corporate default events over 2010–2023, then at about half for three straight years to mid-2024 (S&P study of 15 Aug 2024, as cited by FTI Consulting, 9 Oct 2026; secondary). Moody's put distressed restructurings at about 65% of 2025 corporate defaults ("Lend, Extend, and Then?", 18 May 2026). Liability-management exercises peaked at 38 in 2024 and fell to 24 in 2025, yet were still about two-thirds of default activity by issuer count (Wachtell Lipton, "Liability Management 2026," 3 Feb 2026). The Post-LMT → Stressed edge got heavier too: about 46% of 2023 distressed exchanges had re-defaulted, most within a year (Moody's, reported by Bloomberg Law, 23 Apr 2025). Among 89 coercive non-pro-rata LMEs, the debtors that later filed spent two to three times as long in bankruptcy as prepackaged cases (Roe and Rotaru, HLS Bankruptcy Roundtable, 24 Feb 2026). Large Chapter 11 filings, meanwhile, held at about 150 a year above \$50mm with no trend since early 2024 (FTI, 9 Oct 2026). **What it means for the desk:** the modal path to recovery now runs through two or three out-of-court edges before it reaches a courtroom, if it ever does. A model whose state space starts at the petition sees only the second visit.

Used in: §5.6 (the default as a negotiation), §13.1 (the LMT zoo), §13.3, §13.6 and §13.7 (one section per edge), §13.8 (the PRS as the intensity of the LMT edges), §14.1 (two default rates), §14.3 (the re-default edge), §24.8 (manufactured and missing credit events), App D (ISDA credit events), Ch 13-B (the litigation edges that follow an LMT).

## 12B.5 Chapter 11 as a Timed State Machine

"The first-day hearing is where you find out who's in charge," Mags says. "The confirmation hearing is where you find out what it cost." Almost all the value that changes hands in a Chapter 11 case changes hands at the two ends: in the first thirty days, through the DIP and the first-day orders, and in the last sixty, through the plan value and the votes. The middle is where the clocks run.

The sub-machine has these states: Petition (the stay begins), First days (interim orders), Second days (final DIP order, committee in place), Case administration (claims, exclusivity, challenges), then one of two exits, the §363 sale path or the plan path (plan and disclosure statement filed, solicitation, confirmation hearing, confirmed, effective date). It also has two failure edges: conversion to Chapter 7 (§1112(b)) and dismissal.

### The petition and the stay

A voluntary petition is an order for relief (§301), and every statutory clock in the case starts on that date. The automatic stay (§362(a)) freezes collection, enforcement and setoff against the debtor at once. The exceptions are the safe harbors for securities contracts, repos and swaps (§§555, 559, 560, 561), which let derivative counterparties terminate and net even though everyone else is frozen. That is why the plumbing in App D keeps working on day zero while the term loan agent cannot so much as send a demand letter. The petition is also a Bankruptcy credit event for CDS, which starts the auction clock of §24.6 in parallel with the case.

### First days and Rule 6003

For the first 21 days, Bankruptcy Rule 6003 bars the court from approving payment of prepetition claims, assumption of contracts, or sales outside the ordinary course, "except to the extent that relief is necessary to avoid immediate and irreparable harm." First-day relief is therefore *interim*, and the final orders come at the "second-day" hearing. The package covers cash management, wages (priority claims up to the §507(a)(4) cap), taxes, insurance, interim DIP or cash collateral, and **critical vendors**. A critical-vendor order lets the debtor pay the prepetition claims of suppliers who keep shipping on terms. For the vendor that is a jump from a general unsecured recovery to par, at the debtor's option, and it is the first trade-claim event a desk should model (§16.5). The other early clocks are in the table below. The U.S. Trustee also appoints an official unsecured creditors' committee (§1102).

### DIP financing and the roll-up

Section 364 is a ladder of inducements for post-petition lenders: administrative priority (§364(b)), then superpriority over all administrative expenses and liens on unencumbered assets or junior liens on encumbered ones (§364(c)), and finally a **priming lien** ahead of existing liens (§364(d)). A priming lien is available only if credit cannot be obtained otherwise and the primed lender is *adequately protected* (§361) against any decline in the value of its collateral. Protection comes as cash payments, replacement liens or, if it later proves inadequate, a §507(b) superpriority claim.

> **[SOURCE EXTRACTION]** *Moyer_Distressed_Debt_Analysis p.98:* "to avoid the risk of being primed, many prepetition secured lenders will offer to become DIP lenders. One benefit of becoming a DIP lender is that the prepetition lenders are sometimes able to effectively convert their prepetition claim into a postpetition claim in a process commonly referred to as a rollup."
>
> **Annotation.** In 2004 "sometimes" was accurate, and the roll-up was a defensive side benefit. In the LMT era it is often the point. The ad hoc group that led an out-of-court uptier provides the DIP, rolls up its prepetition paper at one, two or more dollars per dollar of new money, and so repeats the uptier in court with a judge's signature on it. Local rules in the busiest districts make debtors flag roll-ups for the court. The desk prices the transfer, derived next.

**The roll-up as a recovery transfer.** A secured class has face $F$ and will receive value $W < F$ (its secured value plus its pool share), so every holder recovers $R = W/F$. A subgroup lends new money $M$ in the DIP and rolls up $\kappa M$ of its own prepetition claims, where $\kappa$ is the roll-up ratio. The rolled claims become DIP claims, which must be paid in full in cash at emergence. They come off the top, so the remaining prepetition holders recover

$$
R' = \frac{W - \kappa M}{F - \kappa M}, \qquad
R - R' = \frac{W}{F} - \frac{W - \kappa M}{F - \kappa M}
= \frac{\kappa M\,(F - W)}{F\,(F - \kappa M)} .
$$

The transfer is zero when $W \ge F$: rolling up an oversecured claim costs nobody anything, because those holders were going to be paid in full regardless. It grows with the class's impairment $F - W$. A roll-up is free exactly when it does not matter. (We assume $W$ is unchanged, that is, the new money is spent inside the estate rather than added to the value the class shares.) The DIP lender also writes the case's calendar: DIP agreements carry **milestones**, such as a bidding-procedures order by day 30 or confirmation by day 120, and missing one is a DIP default. Those are clocks with the lender's name on them, and the state machine treats them exactly like statutory clocks. So does the committee's **challenge period** (often 60–75 days from its appointment, set by the DIP order). After it, the debtor's stipulations that the prepetition liens are valid bind everyone, and the committee's best weapon expires.

### Two exits: the §363 sale and the plan

**The sale path.** Section 363(b) lets the debtor sell assets outside the ordinary course with court approval, free and clear of liens and claims (§363(f)), with the liens attaching to the proceeds. A secured lender may *credit bid* its claim (§363(k)), though a court can limit a credit bid "for cause." The usual process is a stalking-horse purchase agreement with a break-up fee and expense reimbursement, then bidding procedures, an auction and a sale hearing. Kaz asks whether the stalking horse is the horse doing the stalking or the horse being stalked. "Both," Mags says. "It sets the floor, and everyone else hunts it." Kaz considers this. "So the break-up fee is a premium paid to the bidder for writing a public floor." It is, and it is priced like one: the debtor pays a few percent to buy a put on its own sale price from the one bidder willing to go first. A sale that leaves a pile of cash and no plan cannot be distributed out of priority order without consent; the Supreme Court said so in *Jevic* (2017).

**The plan path.** The debtor has the exclusive right to file a plan for 120 days after the order for relief (§1121(b)). If its plan has not been accepted by every impaired class within 180 days, any party in interest may file one (§1121(c)(3)). The court may extend these periods, but never beyond 18 and 20 months (§1121(d)(2)), and it may shorten them for cause. A creditor group's motion to terminate exclusivity is therefore one of the most informative entries on a docket (§25.7.2). The plan travels with a **disclosure statement**, which needs court approval as containing "adequate information" (§1125) before anyone may solicit votes after the petition. Notice of the disclosure-statement and confirmation hearings runs 28 days (Rule 2002(b)). Votes are tallied by the rules of §12B.3.

**Confirmation** (§1129(a)) requires, among other things:

- **(a)(7) best interests:** every holder in an impaired class who did not accept receives at least what a Chapter 7 liquidation would pay. Per holder, that is a floor: a put struck at liquidation value.
- **(a)(8):** every class accepts or is unimpaired. Failing that, the plan must satisfy the cramdown rules of §1129(b) (§12B.6).
- **(a)(9):** administrative and priority claims, 503(b)(9) claims among them, are paid in full in cash on the effective date unless the holder agrees otherwise.
- **(a)(10):** at least one impaired class, not counting insiders, accepts.
- **(a)(11) feasibility:** confirmation is not likely to be followed by liquidation or another reorganization.

After confirmation comes the **effective date**, the state that requires exit financing, regulatory approvals and other conditions precedent. On that date the discharge takes effect (§1141), distributions begin, and the claims-reconciliation machinery of §12B.8 keeps running, often for years, through a plan administrator or a litigation trust. Figure 12-B.2 lays the case's clocks on one day axis.

![Figure 12-B.2: Four clocks run out within six weeks of the petition, but exclusivity and the avoidance period stretch from months to years, so the case's calendar is set by a few long clocks. Source: 11 U.S.C. §§362, 365(d)(4), 502(b)(9), 503(b)(9), 546(a), 547(b)(4), 1121; Fed. R. Bankr. P. 1007(c), 2003(a), 4001(c), 6003 (the clock table of §12B.5); the challenge period is a typical DIP-order term, drawn from the petition although it runs from committee appointment.](assets/figures/ch12b_chapter11_clocks.png)

### The clock table

| Clock | Starts | Length | Source | What it moves |
| :--- | :--- | :--- | :--- | :--- |
| Automatic stay | Petition | Until relief or case end | §362 | Freezes enforcement; derivatives safe-harbored |
| Interim-relief window | Petition | 21 days | Rule 6003 | First-day relief stays interim |
| Final DIP hearing | Service of motion | At least 14 days | Rule 4001(c)(2) | Interim to final DIP; roll-ups often wait for it |
| Schedules | Petition | 14 days, usually extended | Rule 1007(c) | First look at the claims denominator |
| §341 meeting | Order for relief | 21–40 days | Rule 2003(a) | — |
| Challenge period | Committee appointment (typical) | Often 60–75 days | DIP order | Lien-challenge option expires |
| Exclusivity to file | Order for relief | 120 days, at most 18 months | §1121(b), (d)(2) | Who may propose the plan |
| Exclusivity to solicit | Order for relief | 180 days, at most 20 months | §1121(c)(3), (d)(2) | Who may propose the plan |
| Nonresidential real-property leases | Order for relief | 120 + 90 days | §365(d)(4) | Rejection damages (capped by §502(b)(6)) enter the pool |
| Governmental bar date | Order for relief | 180 days | §502(b)(9) | Tax claims in the denominator |
| General bar date | Court order | Case-specific | Rule 3003(c)(3) | Claims denominator |
| Hearing notice | Notice | 28 days | Rule 2002(b) | Disclosure statement and confirmation |
| Preference lookback | Backward from petition | 90 days (one year for insiders) | §547(b)(4) | Avoidance recoveries for the pool |
| Avoidance limitations | Order for relief | 2 years | §546(a) | Litigation-trust value |
| 503(b)(9) lookback | Backward from petition | 20 days | §503(b)(9) | Splits trade claims into administrative and general |

Used in: §14.6 (rulings as regime switches on these edges), §16.1 and §16.3 (the plan as a security factory; backstops and rights offerings), §21.8 (CLOs inside the LMT and the case), §24.6 (the auction clock that runs beside the case), §25.6 and §25.7.2 (the docket as an event stream and as a Markov chain over these states), Ch 13-B (exclusivity fights, the Serta remand and other docket diaries).

## 12B.6 Plan Value, Absolute Priority, Cramdown and the Fulcrum

Every Part IV chapter needs four definitions, and this section gives each of them exactly once: the waterfall, the fulcrum, the plan value, and the cramdown.

### The waterfall as call spreads

Order the classes by priority $j = 1, \dots, J$ with allowed claims $C_j$ and cumulative claims $K_j = \sum_{i \le j} C_i$, $K_0 = 0$. Let $V$ be the value distributed. Throughout Part IV, $V$ is the *distributable* value the waterfall acts on: the restructuring $\text{EV}$ plus excess cash, less whatever the estate has burned, as in §13.3. Under strict absolute priority, class $j$ recovers

$$
R_j(V) = \frac{\min\!\big(C_j,\ (V - K_{j-1})^+\big)}{C_j}, \qquad
C_j\,R_j(V) = (V - K_{j-1})^+ - (V - K_j)^+ .
$$

The second form is the one to remember. **Every class is a call spread on $V$**, long a call struck at the claims ahead of it and short a call struck at the claims including it, and old equity is the last call, $(V - K_J)^+$. Merton's "debt is a short put" (§6.2) is the special case $J = 1$, and the option language of Ch 6-B ("a CCC bond is an equity option that wears a tie to work") is this identity applied to whichever class sits where $V$ is likely to land.

### The fulcrum, defined once

The **fulcrum class** is the most senior class not paid in full:

$$
j^\star(V) = \min\{\, j : K_j > V \,\}.
$$

It recovers $R_{j^\star} = (V - K_{j^\star - 1})/C_{j^\star} \in [0, 1)$, every class above it is paid in full, and every class below it gets nothing. On the boundary $V = K_j$, class $j$ is exactly whole and the fulcrum is $j + 1$, with recovery zero. That edge case matters in code because it decides who receives the new equity. In a reorganization the fulcrum class usually receives most of the reorganized equity, which is why its holders are the ones who end up on the board.

"A fulcrum is where the lever pivots," Kaz says, "so it should have the most leverage." He is, for once, exactly right. Differentiate the call spread:

$$
\frac{\partial R_j}{\partial V} = \frac{1}{C_j}\,\mathbf{1}\{K_{j-1} < V < K_j\}.
$$

Only the fulcrum class has any delta to enterprise value. Every other class has none: those above are paid in full and those below are out of the money. With $V$ uncertain under the desk's forecast measure $\mathbb{P}$, write $\pi_j = \mathbb{P}(K_{j-1} \le V < K_j)$ for the probability that class $j$ is the fulcrum. Shifting $V$ by $h$ then gives

$$
\left.\frac{\partial}{\partial h}\,\mathbb{E}^{\mathbb{P}}\!\big[R_j(V + h)\big]\right|_{h=0} = \frac{\pi_j}{C_j}
$$

for continuously distributed $V$. A class's expected sensitivity to value is its fulcrum probability divided by its face. That gives the desk a first-order hedge ratio for any restructuring claim without a single model of the court. Figure 12-B.3 draws the stack and the hedge ratios for a four-class example.

![Figure 12-B.3: Each class is a call spread on distributable value (left), so only the class currently filling, the fulcrum, has delta, and its expected sensitivity is its fulcrum probability over its face, largest here for Classes 2 and 3 (right). Illustrative: strict absolute priority, claims of 100, 300, 400 and 200 (in millions), V lognormal with median 450 and σ = 0.40, expected delta = π/C per class from §12B.6.](assets/figures/ch12b_waterfall_call_spreads.png)

### Plan value is a price

Three different numbers are all called "value" in a restructuring, and Law 11 says label them:

- $V$: the economic value, unknown, which the reorganized company's securities will eventually reflect.
- $V^{\text{plan}}$: the value in the disclosure statement, usually the midpoint of the debtor's financial advisor's range. It is a negotiated number, not an estimate (§16.1).
- $V^{\text{mkt}}$: the value implied by post-emergence trading, which Chapter 16 trades against.

The plan uses $V^{\text{plan}}$ to decide how many new shares each class receives. The market then values those shares at $V$. Take two classes, all-equity consideration, and $C_1 < V^{\text{plan}} < C_1 + C_2$. Class 1 is paid "in full at plan value" with a share fraction $\omega_1 = C_1/V^{\text{plan}}$ of the new equity, and class 2 receives $\omega_2 = 1 - C_1/V^{\text{plan}}$. Their realized recoveries are

$$
R_1 = \frac{\omega_1 V}{C_1} = \frac{V}{V^{\text{plan}}}, \qquad
R_2 = \frac{\omega_2 V}{C_2} = \frac{(V^{\text{plan}} - C_1)\,V}{C_2\,V^{\text{plan}}},
$$

so

$$
\frac{\partial R_1}{\partial V^{\text{plan}}} = -\frac{V}{(V^{\text{plan}})^2} < 0, \qquad
\frac{\partial R_2}{\partial V^{\text{plan}}} = +\frac{C_1\,V}{C_2\,(V^{\text{plan}})^2} > 0 .
$$

**A high plan value is the senior class selling equity to the junior class at $V^{\text{plan}}$ when the shares are worth $V$.** If $V^{\text{plan}} > V$, the senior is "paid in full" in shares worth $V/V^{\text{plan}} < 1$ of its claim. If $V^{\text{plan}} \le C_1$, the senior takes all the equity, and if $V$ then turns out above $C_1$, it has recovered more than its claim, which a plan may not provide on purpose. So seniors argue for low valuations, juniors for high ones, and the valuation fight is a fight over the strike of an option that the plan writes from one class to another. That is why the plan value moves \$300mm in an afternoon (§16.1). Figure 12-B.4 plots both classes' recoveries against the plan value for a two-class example.

![Figure 12-B.4: A higher plan value moves recovery from the senior class to the junior class: the senior receives exactly its claim only when the plan value equals the true value, every dollar above it pays the senior in shares worth less than its claim, and below it the senior would be overpaid, which a plan may not provide on purpose. Illustrative: the §12B.6 two-class all-equity model with claims of 800 and 600 (in millions) and shares truly worth V = 1,000.](assets/figures/ch12b_plan_value_transfer.png)

### Absolute priority and its exceptions

When an impaired unsecured class rejects the plan, §1129(b)(2)(B) allows confirmation only if the class is paid in full (in present value) or no junior class receives or retains anything on account of its claims. That is the **absolute priority rule** in its statutory form.

> **[SOURCE EXTRACTION]** *Moyer_Distressed_Debt_Analysis p.108:* "Cram-down is the process by which a plan or reorganization is imposed on an impaired class that has voted to reject the plan." And on the same page: "a key practical effect of the cram-down provision is to force the debtor to garner the support of all impaired classes if it attempts to provide any type of recovery to an out-of-the-money junior class without paying all more senior classes in full."
>
> **Annotation.** ("Plan or reorganization" is the original's wording.) The second sentence is the whole economics of plan negotiation in one line. The absolute priority rule is a veto that a dissenting class holds over any value flowing *past* it, and the veto is worth something only if value is flowing past it. Three 2026 refinements: the "gifting" route around the veto (a senior class handing part of its recovery to a junior over an intermediate class's objection) was closed in the Second Circuit by *DBSD* (2011); old equity cannot keep its stake for "new value" without a market test (*203 North LaSalle*, 1999); and "deathtrap" provisions, under which a junior class receives warrants only if it votes yes, are legal precisely because an accepting class waives the rule for itself. The warrants of §16.4 are often deathtrap consideration.

### Cramdown of a secured class: the rate is a strike

A dissenting *secured* class can be crammed down in one of three ways (§1129(b)(2)(A)): (i) it keeps its liens and receives deferred cash payments totaling at least its allowed claim, with a present value at the effective date at least equal to the value of its collateral; (ii) the collateral is sold free and clear, subject to the credit bid, with the liens attaching to the proceeds; or (iii) it receives the "indubitable equivalent" of its claim. Route (i) is the one with a number in it: the **cramdown interest rate**.

Price a takeback note of face $S$ (the allowed secured claim), annual coupon $c$ set by the court, maturity $n$ years, when the market yield on comparable paper is $y$. With the annuity factor $a_n(y) = \big(1 - (1+y)^{-n}\big)/y$, the price is $P = S\,[\,c\,a_n(y) + (1+y)^{-n}\,]$. Par pricing gives the identity $1 = y\,a_n(y) + (1+y)^{-n}$, and subtracting it yields

$$
\frac{P}{S} = 1 - (y - c)\,a_n(y).
$$

The shortfall from par is the coupon gap times the annuity. Take a 7-year note at a court rate of 8.5% when comparable exit paper yields 11%. Then $a_7(11\%) = 4.712$, and $P/S = 1 - 0.025 \times 4.712 = 0.882$. The secured class receives paper worth 88.2 per 100 of allowed claim, and the 11.8 points do not disappear: they go to whoever owns the residual, usually the fulcrum class just below or the plan sponsor. The cramdown rate is a strike the court sets on an option the debtor holds, the option to pay a secured creditor in paper rather than cash. The Supreme Court's *Till* plurality (2004, a Chapter 13 case) endorsed a formula rate of prime plus a risk adjustment, typically 1–3%. In *Momentive* (*In re MPM Silicones*, 874 F.3d 787, 2d Cir. 2017) the Second Circuit held that in Chapter 11 the market rate applies where an efficient market exists, falling back to the formula only where none does. On remand the bankruptcy court found that no efficient market in the textbook sense had been shown, and set the rate from the debtors' arm's-length backup exit financing, a "process-efficient" market rate (Jones Day, Nov 2017, on the appeal; practitioner summaries of the remand). That two-step test is what a lender's lawyer is arguing about when the desk sees "cramdown risk" on a secured class: whether $c$ will be set near $y$ or near prime plus two.

Used in: §5.5 (seniority in the Beta recovery model), §6.2 and Ch 6-B (equity as a call; the fulcrum as the equity option), §13.3 and §13.7 (uptier and double-dip waterfalls, which are this waterfall applied twice), §14.4 (recovery as a mixture), §16.1 (plan value as a negotiated number), §16.3 and §16.4 (backstops, rights and deathtrap warrants), §16.6 (Hertz: the solvent-debtor end of the waterfall), Chapter 3 (the fulcrum in the RFQ), Chapter 28 (sizing a fulcrum position).

## 12B.7 Time Is a Claim Too: Pricing the Clock

Mags's "eventually" is a matrix. Treat the case's states as a continuous-time Markov chain with generator $\mathbf{G}$, whose off-diagonal entries $g_{xy} \ge 0$ are transition intensities per year and whose diagonal is $g_{xx} = -\nu_x$, with $\nu_x = \sum_{y \ne x} g_{xy}$. (Chapter 25 writes the same intensities as $q_{ab}$. Here they sit in $\mathbf{G}$, so that $\mathbb{Q}$ stays the measure and $q$ stays inventory.) Split the states into transient ones $\mathcal{T}$ (petition, contested, solicitation) and absorbing outcomes $\mathcal{A}$ (effective date, sale, conversion), and write $\mathbf{G}_{\mathcal{T}\mathcal{T}}$ for the transient block and $\mathbf{G}_{\mathcal{T}\mathcal{A}}$ for the exit rates. Let $T$ be the time of absorption and define the discounted outcome probabilities

$$
U_{xa}(r) = \mathbb{E}^{\mathbb{P}}_x\!\left[e^{-rT}\,\mathbf{1}\{X_T = a\}\right].
$$

**First-step analysis.** From state $x$ the chain waits an exponential time $H$ with rate $\nu_x$, so $\mathbb{E}[e^{-rH}] = \nu_x/(\nu_x + r)$, and then jumps to $y$ with probability $g_{xy}/\nu_x$. Conditioning on the first jump,

$$
U_{xa} = \frac{\nu_x}{\nu_x + r} \sum_{y \ne x} \frac{g_{xy}}{\nu_x}\, U_{ya}
\quad\Longrightarrow\quad
(r + \nu_x)\,U_{xa} - \sum_{y \in \mathcal{T},\, y \ne x} g_{xy}\,U_{ya} = g_{xa},
$$

where $U_{aa} = 1$ was used for the absorbing target. In matrix form,

$$
\mathbf{U}(r) = \big(r\mathbf{I} - \mathbf{G}_{\mathcal{T}\mathcal{T}}\big)^{-1}\mathbf{G}_{\mathcal{T}\mathcal{A}} .
$$

At $r = 0$ this gives the absorption probabilities $\mathbf{B} = (-\mathbf{G}_{\mathcal{T}\mathcal{T}})^{-1}\mathbf{G}_{\mathcal{T}\mathcal{A}}$, and the same inverse applied to a vector of ones gives the expected time to resolution, $\mathbf{m} = (-\mathbf{G}_{\mathcal{T}\mathcal{T}})^{-1}\mathbf{1}$. If recovery in outcome $a$ is $R_a$ (from §12B.6, at that outcome's value), a claim's discounted expected recovery from state $x$ is $\Pi_x = \sum_a U_{xa} R_a$.

**The fee burn.** Professional fees and other administrative expenses accrue at a rate $\phi$ (dollars per year) and are paid in cash before any prepetition class (§1129(a)(9)), so the value left at resolution is $V_T = V_0 - \phi T$. While class $j$ stays the fulcrum its recovery is linear in value, $R_j = (V_0 - \phi T - K_{j-1})/C_j$, and

$$
\mathbb{E}_x\!\left[e^{-rT} R_j\,\mathbf{1}\{X_T = a\}\right]
= \frac{(V_0 - K_{j-1})\,U_{xa} - \phi\,W_{xa}}{C_j},
\qquad
\mathbf{W} = -\frac{\partial \mathbf{U}}{\partial r} = \big(r\mathbf{I} - \mathbf{G}_{\mathcal{T}\mathcal{T}}\big)^{-2}\mathbf{G}_{\mathcal{T}\mathcal{A}},
$$

using $\partial_r (r\mathbf{I} - \mathbf{G})^{-1} = -(r\mathbf{I} - \mathbf{G})^{-2}$, so that $W_{xa} = \mathbb{E}_x[T e^{-rT}\mathbf{1}\{X_T = a\}]$. In words: the fulcrum class is short the fee rate times a resolvent squared. Senior to everyone, by statute, and paid by the hour.

Three consequences. First, the **fulcrum migrates up the stack** as the case runs: class $j$ falls out of the money at $T_j = (V_0 - K_{j-1})/\phi$, so a class that was the fulcrum on the petition date can be wiped out by confirmation. Second, the *Timbers* asymmetry of §12B.2 makes the undersecured senior the party that pays for delay twice, through lost time value and through the burn, while an oversecured lender accrues §506(b) interest. That is why undersecured lenders push for prepacks and write tight DIP milestones. Third, $\mathbf{G}$ is estimated from dockets ($\hat g_{ab} = N_{ab}/T_a$, §25.7.2), which makes it a $\mathbb{P}$ object. $\Pi$ is therefore a physical-measure forecast, and comparing it with a market price means adding a risk premium or tilting $\mathbf{G}$ and $R$ to $\mathbb{Q}$, then saying which you did (Law 4).

Used in: §14.3 (the re-default clock, the same algebra on a different chain), §16.8 (the post-reorg book's holding-period distribution), §25.7.2 (where $\mathbf{G}$ is estimated), Ch 7-B (survival and competing risks as methods), Chapter 28 (sizing against the clock).

## 12B.8 Claims Mechanics: From Proof of Claim to Distribution

The order in which a plan pays, compressed to one ladder. Legal priority inside a collateral silo follows the liens (§12B.2). The ladder is the order in which plan consideration actually flows.

| Rank | Claim | Source | Typical plan treatment |
| :--- | :--- | :--- | :--- |
| 1 | DIP claims: superpriority claim and priming liens | §364(c)(1), (d) | Cash at exit, or rolled into exit debt |
| 2 | Secured claims up to collateral value; adequate-protection claims | §506(a), §507(b) | Cash, takeback paper, equity |
| 3 | Administrative claims: post-petition trade, professional fees, 503(b)(9) goods | §503(b), §507(a)(2), §330 | Cash on the effective date (§1129(a)(9)) |
| 4 | Priority unsecured: capped wages and benefits, certain taxes | §507(a)(4)–(8) | Cash; priority taxes may be paid over five years |
| 5 | General unsecured: deficiencies, bonds, trade, rejection damages, litigation | §502 | Pro rata pool, with contractual subordination applied inside it (§510(a)) |
| 6 | Claims arising from buying or selling the debtor's securities | §510(b) | Rank with the security they concern |
| 7 | Preferred, then common equity | — | Usually cancelled |

**The claim's own state machine.** A claim begins as an entry on the debtor's schedules (§521). In Chapter 11 a scheduled claim not marked disputed, contingent or unliquidated is deemed filed (§1111(a)). Anyone else must file a proof of claim by the bar date (Rule 3003(c)), and the indenture trustee files one for the whole bond issue. A filed claim is deemed allowed unless someone objects (§502(a)). Objections, settlements and estimation (§502(c), the "M-estimator with a robe" of §16.5) move it to allowed, reduced or disallowed. Disputed claims sit in a reserve until resolved, and distributions go to holders as of the distribution record date. Every one of those arrows is a docket entry, which makes Chapter 25's claims register the log file of this machine.

**Transfers: Rule 3001(e).** When a claim is transferred after a proof of claim has been filed, the transferee must file evidence of the transfer, "except for a claim based on a publicly traded note, bond, or debenture" (Rule 3001(e)(2)). The transferor has 21 days after the clerk's notice is mailed to object; if it does not, the transferee is substituted. (Before a proof is filed, (e)(1) lets only the transferee or an indenture trustee file.) So **bonds** settle through DTC in a day (App D) and leave no trace on the docket, while **trade claims** settle in weeks under an assignment-of-claim agreement and leave the face amount, never the price, on the docket (§25.8). Most assignments carry **recourse**: if the claim is disallowed or reduced, the seller refunds that share of the price, usually with interest. A claim bought with recourse is a claim plus a put on allowance written by the seller, and buying from a vendor that is itself in trouble buys a put from someone who may not be there to honor it.

**503(b)(9), critical vendors and the GUC class.** A vendor's prepetition claim can end up in any of three places: administrative priority, for goods received in the 20 days before the petition (§503(b)(9)); paid in cash under a critical-vendor order; or the general unsecured class. The general class may itself be split, with a cash convenience class for small claims and a litigation trust for avoidance and estate claims. Section 16.5 prices each piece: the near-par 503(b)(9) claim, the random denominator of the GUC pool, and the pair trade between them. This section only fixes where each piece sits on the ladder.

Used in: §16.5 (claims pricing and the 503(b)(9) pair), §16.6 and §16.7 (Hertz and Spirit, the claims ends of their cases), §25.8 (the claims register and the transfer feed), Chapter 25's covenant-and-docket engine.

## 12B.9 The Halvorsen Files, Part II: From Grace Period to Effective Date

The cold open, run through the machine. The capital structure (in \$mm, illustrative; the Halvorsen Files use it from here through Chapter 16):

| Class | Face | Collateral and ranking |
| :--- | :--- | :--- |
| ABL revolver | 150 | First lien on receivables and inventory; second on everything else |
| First-lien term loan B | 900 | First lien on fixed assets, IP and stock pledges; second on ABL collateral |
| 7.25% senior secured notes due 2029 | 500 | Pari passu with the TLB under a pari passu intercreditor |
| 6% senior notes due 2031 | 600 | Unsecured |
| 3% senior notes due 2045 | 250 | Unsecured, pari passu with the 6s |
| Trade payables | 150 | Unsecured, of which 40 are 503(b)(9) goods |
| Lease rejection (after the §502(b)(6) cap) | 60 | Unsecured |

**Out of court.** The sponsor first floated an uptier. The 2021 credit agreement makes subordination of loans or liens a sacred right, so $\theta^{\text{eff}} = 1$ for every implementation counsel could find, and the uptier edge stayed closed. Next came an exchange offer for the unsecured notes, with a 90% minimum-participation condition. Only 62% tendered, so that edge failed as well. On day 28 of the grace period, with the invariant about to force an event of default, the first-lien ad hoc group (58% of the first lien) signed an RSA, and Halvorsen filed.

**The DIP.** The group lends \$150mm of new money with a 1:1 roll-up of \$150mm of its own term loans. At the plan value below, the first-lien class would receive $W = 910$ on $F = 1{,}400$ without the roll-up, a recovery of 65.0%. With it, the formula of §12B.5 gives

$$
R - R' = \frac{150 \times (1{,}400 - 910)}{1{,}400 \times 1{,}250} = 4.2 \text{ points},
$$

so first-lien holders outside the group recover 60.8%, while the group's blended recovery rises to $(150 + 662 \times 0.608)/812 = 68.0\%$. The roll-up also cut the group's own voting share from 58% to $662/1{,}250 = 53\%$. At 70% turnout among the remaining holders, the class needs \$54mm of outside yes votes (13% of those voting) to reach two-thirds, which the group's counsel considers a formality and the Ad Hoc Group considers an insult. (Cooperation agreements signed in this book so far: still 1.)

**The waterfall at $V^{\text{plan}} = 1{,}300$**, split into ABL collateral of 250, unencumbered value of 90 and term collateral of 960:

1. ABL collateral pays the ABL's 150 in full; the residual 100 passes to the first lien under its second lien.
2. The DIP's 300 primes the term collateral, leaving 660.
3. The first lien's secured claim is $660 + 100 = 760$ against 1,250, a deficiency of 490.
4. Unencumbered value of 90 pays 75 of administrative and priority claims (the 40 of 503(b)(9) goods, 25 of accrued fees, 10 of priority taxes and wages), leaving 15.
5. The first lien waives its deficiency share as part of the plan, so the unsecured class splits 15 across 1,020: a 1.5% recovery.

The plan delivers an exit ABL (150), an exit term loan that takes out the DIP (300), \$350mm of takeback first-lien notes and 100% of the new equity (worth $1{,}300 - 150 - 300 - 350 - 15 - 75 = 410$) to the first lien: $350 + 410 = 760$, or **60.8%**. The unsecured class receives its \$15mm cash pool, plus deathtrap warrants for 7.5% of the equity if, and only if, it votes yes. A Chapter 7 liquidation would pay the unsecured class nothing, so the best-interests test is met. Old equity receives nothing, so cramming down a rejecting unsecured class satisfies the absolute priority rule. Figure 12-B.5 follows the 1,300 from the collateral silos to the claims.

![Figure 12-B.5: Of the 1,300 of plan value the first lien receives 760, made of 100 from the ABL collateral and the 660 of term-loan collateral left after the DIP primes it, while the unsecured pool gets only 15. Illustrative: the Halvorsen waterfall of §12B.9 (fictional company, in millions).](assets/figures/ch12b_halvorsen_waterfall.png)

| $V^{\text{plan}}$ | First-lien secured value | Pool after administrative claims | First-lien recovery | Unsecured recovery | Fulcrum |
| ---: | ---: | ---: | ---: | ---: | :--- |
| 1,100 | 575 (after a 2 carve-out) | 0 | 46.0% | 0.0% | First lien |
| 1,300 | 760 | 15 | 60.8% | 1.5% | First lien |
| 1,600 | 1,034 | 41 | 82.7% | 4.0% | First lien |

*(Illustrative. Value is split by holding ABL collateral at 250 and the unencumbered share at 8.57% of the remainder.)* At 1,100 the unencumbered value no longer covers administrative claims. The case is at the edge of administrative insolvency, and the first lien funds the gap through a carve-out, because no plan means no company. The first lien stays the fulcrum until $V^{\text{plan}} \approx 1{,}836$, 41% above the debtor's midpoint. Its delta is $0.914/1{,}250$ per \$1mm of value, or 7.3 points per \$100mm. The unsecured class has a delta of 0.84 points per \$100mm, so it barely moves with value.

**Where the unsecured class's value actually lives: the challenge clock.** The committee finds three plant mortgages, worth \$120mm, that were never recorded. If its challenge succeeds, that value becomes unencumbered and the first lien loses the deficiency waiver: the unsecured recovery goes to $135/1{,}630 = 8.3\%$ and the first lien falls to 55.2%. The challenge period expires on day 75. The parties settle on day 71: the pool rises to \$35mm (3.4%), the challenge is dropped, and the first lien gives up 1.6 points. Settlement value is the option value of a lawsuit with an expiry date.

**The price of the clock.** Take a chain from the petition state with intensities per year: petition to solicitation at 3.0, petition to contested at 1.0, contested to solicitation at 2.0, contested to sale at 0.5, solicitation to effective at 6.0. At $r = 5\%$, §12B.7 gives $U_{P,\text{eff}} = 0.927$, $U_{P,\text{sale}} = 0.048$, $\mathbb{E}[T] = 0.51$ years and $W_{P,\text{eff}} = 0.457$. With a fee burn of \$60mm a year on the 1,250 fulcrum class, the first lien's value at the petition is about $0.927 \times 60.8 + 0.048 \times 50 - (60/1{,}250) \times 0.457 \times 100 \approx 56.6$, taking 50 as its recovery in the sale state. The 63 in the cold open priced the out-of-court edges, and the petition removed them. (Strictly, the first \$15mm of extra fees comes out of the unsecured pool, because administrative claims are paid from unencumbered value first. Only after that does the burn reach the first lien, through the carve-out. Charging it all to the fulcrum is off by at most 1.2 points.)

Used in: §13.3 (Larkspur, the out-of-court sibling of this case), the cold opens of Chapters 18 and 24 (earlier Halvorsen chapters, before the grace period), §24.6 (the CDS auction the petition triggers), §16.1–16.4 (Halvorsen's new equity, warrants and forced sellers), §25.7 (the docket this case would leave).

## 12B.10 Specification for AI Implementation: `restructuring_state_machine.py`

### Case Study: Serta to Incora, One Guard Read Four Times

On 22 June 2020 the uptier edge out of Serta's Stressed state fired. Its guard was one question, "is this an open market purchase?", and the bare majority holding the pens answered yes. A Texas bankruptcy court agreed in 2023. On 31 December 2024 the Fifth Circuit said no, because an open market purchase happens "on the secondary market for syndicated loans," and in July 2026 the remand court priced the wrong answer at \$261.13mm plus 9% interest (§13.3.1, §25.7.3). The machine never changed. One Boolean was read four times and flipped once, four and a half years after the edge fired. Wesco/Incora did the same to the min–max of §12B.1: read together, the steps faced a two-thirds bar the group lacked (bankruptcy court, January 2025); read one at a time, each cleared its own (district court, December 2025). Lawyers choose the outer min, and a panel audits the choice later.

> **Math, Gently.** A guard nobody can read yet is a coin nobody can see. Call $p$ the chance that a court finally says "true." An edge worth +30 points to the participants if it stands and −30 if it is unwound with damages is worth $60p - 30$ today: 18 points at $p = 0.8$, minus 12 at $p = 0.3$. That is a Bernoulli variable with a timestamp, and an appeal can flip it again. The full version is Law 16 and §14.6.

**What that asks of the code.** ROBO's answer to "model the Halvorsen bankruptcy" was the cold open's 40: no state, no clock, no document. The module keeps four layers apart. The *legal layer* is the automaton of §12B.4, with guards that return probabilities: a sacred right is 0, a clean majority vote is 1, and Serta's clause in 2024 sat in between. `legal_edges` lists every edge with a positive guard and never picks one, and the log keeps each guard's value at firing, so a later ruling revalues the edge rather than rewriting history. The *contract layer* is pure functions of §12B.1–12B.6, the *clock layer* turns a petition date into §12B.5's deadlines, and the *probability layer* returns §12B.7's $\mathbf{U}$, $\mathbf{W}$ and $\mathbf{m}$ by linear solves. Claims are in \$mm, intensities per year, recoveries fractions of claim.

Use it for the structure of a case, not to value the enterprise: $V$ is an input, and every recovery is conditional on it (§5.5 and §16.1 own its distribution). The edge case that bites is $V = K_j$, where class $j$ is whole and class $j+1$ is the fulcrum at zero, so a `<=` where a `<` belongs hands the new equity to the wrong class. Turnover runs in the order agreements are listed, and a chain with no exit makes $\mathbf{G}_{\mathcal{T}\mathcal{T}}$ singular, a case that cannot end. The self-test reproduces Moyer's Dead Co. (bank 50.00, trade 18.75, sub 6.25; Moyer_Distressed_Debt_Analysis p.160–161) and this chapter's numbers.

*The full python listing is [Listing 12-B.1 in Appendix F](#code-12b-1).*

Used in: §13.3 and §13.7 (the uptier and multi-obligor engines extend `silo_waterfall`), §13.8 (the PRS supplies the LMT edges' guard probabilities), §14.3 and §14.6 (the re-default chain; rulings as guard jumps), §16.1 and §16.5 (plan value and claims), §25.7.2 (where $\mathbf{G}$ is estimated), §28.4 (sizing against the clock).

## 12B.11 Desk Debrief

- **Ask "under which document?" before "what's the recovery?"** The binding threshold is a min over implementations of a max over rights, and a court can shrink the menu. (Laws 8, 16)
- **Lien subordination is one buffet; payment subordination is all of them.** Turnover pays only the named beneficiaries, so a defined term is a payoff. (Law 8)
- **Turnout is a position.** At 70% turnout a quarter of a class blocks, and threshold fights are fought over the denominator. (Law 8)
- **Every class is a call spread, and only the fulcrum has delta.** Plan values, roll-ups and cramdown rates are strikes that move value between classes. (Laws 7, 8)
- **Time is a senior claim.** Fees burn ahead of every prepetition class and push the fulcrum up the stack; one resolvent prices the clock, in $\mathbb{P}$ until you say otherwise. (Law 4)
- **A guard is a probability with a forum and a date.** Serta's took four and a half years to read. (Law 16)

**The Spec You Hand the Robot.** "Implement `restructuring_state_machine.py` per §12B.10: a timed automaton whose guards are probabilities and whose log keeps them; the min–max threshold; the turnout-adjusted blocking stake; the silo waterfall with ordered turnover; call spreads and a fulcrum that puts $V = K_j$ in class $j+1$; roll-up and cramdown prices; statutory deadlines; and $\mathbf{U}$, $\mathbf{W}$, $\mathbf{m}$ by linear solves on a validated $\mathbb{P}$ generator. \$mm and years. Tests: Dead Co., §12B.2, §12B.9."

### Exercises

1. *(Kaz's buffet.)* In Dead Co. (assets 75; bank 50, trade 50, sub 100, all unsecured) the sub is subordinated to the bank. Who gets what, and what changes if "Senior Debt" includes trade? *Solution:* 37.5% each, then 31.25 of turnover: bank 100%, trade 37.5%, sub 6.25%. With trade inside the definition, the sub's 37.5 splits by shortfall: bank and trade 75%, sub nothing.
2. *(The denominator.)* A coalition holds 59% of a \$600mm series and needs two-thirds. What new face closes the gap, and what share blocks a plan vote at 60% turnout? *Solution:* $N \ge 46/(1/3) = 138$, so \$138mm; any share above $0.6/2.6 = 23.1\%$.
3. *(The burn.)* In §12B.9, what fee rate takes the first lien's petition-date value from 56.6 to 50? *Solution:* before fees it is $0.927 \times 60.8 + 0.048 \times 50 = 58.8$, so fees must cost 8.8 points: $(\phi/1{,}250) \times 45.7 = 8.8$ gives $\phi \approx$ \$240mm a year, four times the assumed burn. Closing the out-of-court edges (63 to 58.8) cost the first lien more than the clock does.
4. *(ROBO confirms on filing day.)* Name three guards that should have stopped it. *Solution:* no post-petition solicitation without an approved disclosure statement (§1125(b)); 28 days' notice of the confirmation hearing (Rule 2002(b)); and §1129(a)(8) or (a)(10), which need votes. A prepack is fast only because its votes came before the petition (§1126(b)).

### Deep-Dive Resource Graph

- **Podcasts:** Bloomberg *Odd Lots*, "Inside the Blood Sport of Creditor-on-Creditor Violence," with Sujeet Indap (25 Nov 2024), transcript at https://podscripts.co/podcasts/odd-lots/inside-the-blood-sport-of-creditor-on-creditor-violence ; *Money Stuff: The Podcast*, "Hurt People Hurt People: SBUX, LMEs, BofA" (16 Aug 2024; no link verified). **"EP 21 | How Bankruptcy Really Works: Inside the System with Josh Sussberg"** (*The Octus Download*, 10 Dec 2025). A Kirkland & Ellis restructuring partner on how the 2005 Code amendments compressed timelines and pushed negotiation earlier and largely out of court; read it before the state diagram in §12B.5. https://share.transistor.fm/s/81750469 ; **"EP 22 | Judge Michael B. Kaplan, Vegas Squeeze & the First Brands Conspiracy"** (*The Octus Download*, 23 Dec 2025). A sitting judge on how feasibility is judged and why courts hesitate to reject aggressive DIP financing: the bench's view of the §12B.5 transitions and of venue choice. https://share.transistor.fm/s/aaf0387e ; **"Unjustice for all"** (*Cloud 9fin*, 21 Aug 2024). The Supreme Court's 5-4 *Purdue Pharma* ruling of 27 June 2024 against non-consensual third-party releases, i.e. what a plan can and cannot do to non-debtors (§12B.6, §12B.8). https://share.transistor.fm/s/70cc3e30
- **Practitioner Writing:** Octus, "RX 101: Creditor-on-Creditor Violence," https://octus.com/resources/articles/rx-101-creditor-on-creditor-violence ; **"Restructuring Trend: The Ultrafast Prepack for Private Credit Deals"** (Proskauer, David M. Hillman, 4 Nov 2019). Defines prepack, pre-negotiated case and free-fall, and shows the case clock collapsing to 24 and 19 hours (FullBeauty, Sungard): the premise of §12B.7, "time is a claim too." https://www.proskauer.com/pub/restructuring-trend-the-ultrafast-prepack-for-private-credit-deals ; **"Creditor's Rights Toolkit: What Is the Life Cycle of a Chapter 11 Bankruptcy Case ... (Part I)"** (Troutman Pepper Locke, 2025). A three-page, five-stage plain-language view of a Chapter 11 case, a cross-check on the state list in §12B.5. https://www.troutman.com/wp-content/uploads/2025/12/tpl_creditorsrightstoolkit_chapter11lifecycle_parti.pdf ; **"Lien Subordination and Intercreditor Agreements"** (Gibson Dunn, Robert L. Cunningham and Yair Y. Galil, May 2009). Old, but still the cleanest statement of lien versus payment subordination for §12B.2. https://www.gibsondunn.com/wp-content/uploads/documents/publications/Cunningham-Galil-LienSubordinationIntercreditorAgreements.pdf ; Cleary Gottlieb, "Recent Developments in DIP Financing," *GRR Americas Restructuring Review 2024*, https://www.clearygottlieb.com/-/media/files/grr-americas-restructuring-review-2024--recent-developments-in-dip-financing.pdf ; Mayer Brown on *Serta* and the remand (July 2026), https://www.mayerbrown.com/en/insights/publications/2026/07/serta-simmons-bedding-the-fifth-circuits-uptier-decision-and-the-landmark-damages-ruling-on-remand ; Moyer, *Distressed Debt Analysis* (2005).
- **Academic Papers:** Weiss (1990), *Bankruptcy Resolution: Direct Costs and Violation of Priority of Claims*, JFE; Eberhart, Moore and Roenfeldt (1990), *Security Pricing and Deviations from the Absolute Priority Rule in Bankruptcy Proceedings*, JF; Roe and Rotaru (2026), *Liability Management's Limited Runway*, HLS Bankruptcy Roundtable, https://bankruptcyroundtable.law.harvard.edu/2026/02/24/liability-managements-limited-runway-corporate-restructuring-today/ ; the Fifth Circuit's *Serta* opinion, https://www.ca5.uscourts.gov/opinions/pub/23/23-20181-CV0.pdf
- **Data & Code:** `restructuring_state_machine.py` (§12B.10); Title 11, https://www.law.cornell.edu/uscode/text/11 ; Federal Rules of Bankruptcy Procedure, https://www.law.cornell.edu/rules/frbp ; CourtListener API, https://www.courtlistener.com/help/api/

Used in: every Part IV chapter and §25.6–25.8; the Desk Debrief bullets feed App E (Laws 4, 7, 8, 16).

<!-- STATUS: COMPLETE -->
