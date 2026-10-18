# Shelf digest: foundations_shelf_pages (primer source pages for Ch 4-B, 6-B, 7-B, 12-B, App E)

Researcher run date: 2026-10-18. Queue slug: `foundations_shelf_pages`. Feeds: `04_ch04b_bond_math_for_the_desk`, `06_ch06b_options_and_measures_for_credit`, `07_ch07b_statistics_for_credit_panels`, `12_ch12b_the_restructuring_process_as_a_state_machine`, `94_appE_laws_of_the_desk`.

Citation convention: `book_id p.N` where N is the PDF page index used by `tools/pdf_search.py` (1-based), as the [SOURCE EXTRACTION] boxes require.

## 0. Method and shelf inventory

(to be filled)

## 1. Moyer: classes, voting, cramdown, plan process (Ch 12-B)

Source: `Moyer_Distressed_Debt_Analysis` (Stephen G. Moyer, *Distressed Debt Analysis: Strategies for Speculative Investors*, J. Ross Publishing, 2005; 453 PDF pages, no embedded TOC). PDF page = printed page + 17 (p.357 PDF = printed 340). Every citation in this dossier uses the PDF page. The worked example throughout is "Boxco": an operating company with a secured bank claim A and trade claim B, under a holding company with unguaranteed senior notes C, plus equity (Figures 3-6, 12-1 to 12-3).

### 1.1 The process as Moyer tells it (p.94-108, p.327-362)

**Phases and timing (p.94, p.97).** A chapter 11 has "four main objectives": stabilise operations and liquidity; develop a going-forward business plan; determine the "legitimate" liabilities and their priority; and "create and allocate a new capital structure" (p.97). The filing types are a ladder of preparation: *free-fall* (no consensus, "a warning sign that the reorganization process may be unusually lengthy (e.g., 1-3 years) and expensive", p.94); *prenegotiated* (plan agreed at filing, vote after); *prepackaged* (vote solicited before filing under BRC section 1126(b), confirmation "in less than 45 days", p.94, p.335-336). Moyer's reality check on prepacks: "Full prepacks are not common"; they were "less than 7% of cases" in 1998-2002 (p.336, Table 12-1), because a prepack needs very few voting classes, so the consenting bond class must tolerate pari passu trade creditors being left whole (p.336).

**Automatic stay, DIP, priming, roll-up (p.97-99).** The stay "freezes all creditors in their prepetition position" (p.97). Postpetition borrowings are administrative claims; the code lets the court grant the DIP lender "a super-priority interest in previously encumbered assets", "sometimes called priming", conditional on adequate protection; prepetition lenders offer to become DIP lenders to avoid being primed and "effectively convert their prepetition claim into a postpetition claim in a process commonly referred to as a rollup" (p.98). His priming arithmetic is a ready test case: a lender owed $65 with $150 of receivables as collateral can be adequately protected after a $75 DIP is given super-priority over $75 of the collateral (p.98). Critical-vendor motions, KERPs and the CRO appear at p.99.

**Exclusivity (p.94, p.346-347).** "Under BRC section 1121(b), the debtor has the exclusive right to propose a plan of reorganization for 120 days following the filing of the petition and then an additional 60 days to solicit acceptances" and courts extend it "virtually indefinitely" (p.94, p.346). Moyer's view is that this is the management-versus-creditor axis: exclusivity "tends to work against creditor interests" (p.346). **Dated:** BAPCPA (effective 17 Oct 2005) capped extensions at 18 months (file) and 20 months (solicit); see section 9.

**Assets and liabilities (p.101, p.304).** Voidable preferences: payments on antecedent debt in the 90 days before filing, one year for insiders (p.101, p.304). Fraudulent conveyance: no fair value received, "frequently ... considered in leveraged buyout situations that fail" (p.101). Substantive consolidation "effectively eliminates the notion of structural priority" (p.304) and so converts a structurally-senior operating-company trade claim and a holdco bond into pari passu claims (Figure 12-3, p.360); Moyer flags it as a tradeable hedge: buy the lower-priced claim, short the higher-priced one (p.305).

### 1.2 Classes, impairment and voting (p.106-107, p.334, p.356-358)

- **Classification.** The plan "can propose the segregation of claims and interests into various classes" (p.356). All claims in a class get identical treatment, so "the main purpose of creating separate classes of claims with similar priority is to give them different treatment" (p.360). Secured claims "are required to be segregated into classes in accordance with the underlying collateral" (p.358). Gerrymandering is possible and "bankruptcy courts are mindful of this risk" (p.107).
- **Impairment.** "Effectively, a claim must be either paid off in full or reinstated under identical terms to be unimpaired. Any other treatment (even improvements) likely will be judged as an impairment" (p.356-357). Unimpaired classes are deemed to accept and are not solicited; classes receiving nothing are deemed to reject (p.106). So the voting set is the classes that "are receiving some type of recovery but are impaired" (p.106).
- **Voting test.** A class accepts if more than 50% in number and at least 66 2/3% in amount of *those voting* approve (p.107; p.357 states it as "66.7% of those voting in amount and more than 50.0% in number"). "These thresholds are based on those participating in the voting process, not the full class size" (p.107). Accepting class binds dissenters and non-voters (p.334).
- **Blocking position.** The two-prong test "was designed to prevent one large holder from imposing its will on a class where the majority (in number) objects" (p.358). The consequence: 33.4% of a class's claims blocks (more precisely, one-third plus of the *voting* amount), and a plan proponent's counter is to merge classes to dilute the blocker below one-third. Moyer's Block Partners example (45% of claim C, bonds merged with trade claims, p.358) is a ready worked example; the limit he notes is that secured claims cannot be merged across collateral.
- **Tipping.** The consensus-building mechanism: "horse trading" such as warrants struck at an equity-friendly value of 60 given to the equity (p.357). "This process, which in particular gives value to claims that would appear to be out-of-the-money, is called tipping" (p.357). Arithmetic: a $250 senior class giving up 2 points hands a $50 preferred class a 10-point improvement (p.361). Investor lessons (p.361): count votes accurately because tip-laden plans need *all* impaired classes; senior holders should "budget in potential 'tip giving'"; out-of-the-money juniors are "a bet on how big a tip can be extracted".

### 1.3 Confirmation and cramdown (p.107-108, p.359-362)

- **Section 1129 as a "bill of rights".** Confirmation is "limited democracy" (p.359): the court checks procedural items (fees, post-confirmation officers disclosed, regulatory approvals, US Trustee fees, retiree benefits; p.107) plus four substantive tests: *best interests* (each dissenting creditor gets at least chapter 7 liquidation value; "generally not much protection for unsecured creditors" because the liquidation analysis is a "fire-sale", p.107-108), *good faith* (undefined, hard to use, p.108), *feasibility* (no subsequent liquidation or reorganisation; "the most contentious part of the confirmation hearing because any single creditor can raise a challenge", p.108) and *consent or cram-down*.
- **Cram-down gate (p.359).** Three requirements: (1) at least one impaired accepting class excluding insiders; (2) no unfair discrimination; (3) fair and equitable. Unfair discrimination is the pari passu fairness test between *different* classes of the same priority (p.360: trade claims B offered 70% in cash while notes C get equity, B demanding 75%). Fair and equitable for unsecured classes is "strict enforcement of the absolute priority rule" (p.360): no junior recovery unless the objecting class is paid in full. The practical effect (p.108): any value, "regardless of how minimal", to equity means the debtor must obtain consent of, or fully pay, all impaired creditors.
- **Secured cramdown (p.362).** Absent a section 1111(b) election, the lien attaches to sale proceeds, or the creditor retains its lien to the extent of the allowed claim and gets deferred payments with present value equal to the lesser of collateral value or allowed claim. With the 1111(b) election the creditor waives its deficiency claim in exchange for a lien for the full face amount and payments whose gross equals face but whose present value equals the lesser of collateral and claim. Moyer's essence: "the secured claim must, at a minimum, receive a new secured piece of paper with a present value equal to the secured portion of the allowed claim", and a plan that partially equitises a secured claim "likely will need to be acceptable to the secured class" (p.362). Administrative claims must be paid in cash or consent at confirmation; hence rights offerings to fund exit (p.362).
- **Valuation contest (p.356).** If the committee thinks the disclosure-statement valuation is wrong, "the bankruptcy court ... will hear the conflicting testimony of the debtor's and committee's ... financial advisors", and "often ... the parties will come to a compromise" (p.356). The incentives are symmetrical and are why plan value is a random variable: seniors want a low valuation (they keep a "windfall" if the sale price exceeds it, p.106), juniors a high one.

### 1.4 Priority, subordination and the recovery waterfall (p.68, p.158-161)

- **Four priority techniques (p.158-159):** grants of collateral, term structure (maturity), contractual provisions, and corporate structure. A security agreement is a separate document referencing the main lending agreement, and "perfection" failures give unsecured lenders leverage (p.159).
- **Contractual subordination is purely contractual.** "Legal subordination can only occur through an express provision in the bond being subordinated", and the book's "Super-Duper Senior Notes" example shows a note cannot assert seniority over others (p.159-160). Scope matters: "Senior Debt" is a defined term and normally narrower than "all other obligations", with subordination usually limited to debt rather than trade claims (p.160).
- **Partial subordination and subrogation (Dead Co., Figure 7-2 and Table 7-1, p.160-161).** Assets $75; bank debt $50, trade claims $50, sub notes $100. Pro rata recovery is 37.5% (75/200), i.e. bank 18.75, trade 18.75, sub 37.50. Because the sub notes are subordinated only to the bank, the sub's $31.25 is turned over to the bank. Adjusted recoveries: bank 50.00 (100%), trade 18.75 (37.5%), sub 6.25 (6.3%). Sub subordinated to both bank and trade would have given both a 75% recovery (75/100). Table 7-1 is the minimum regression test for any waterfall engine; it is the "subordination as a transfer, not a rank" idea that App E law 12-style reasoning needs.
- **The pricing paradox (p.68).** Boxco senior debt at 50, sub at 20, equity positive: "the price of one security appears to imply that the price of another security is wrong". Implied asset value $290 from market prices (p.68). Useful for the cramdown chapter as the market-implied waterfall that no cut-off ever satisfies.

### 1.5 Out of court as a prisoner's dilemma (p.85-87)

The holdout arithmetic is a complete tiny model. Boxco's $700 face of bonds exchanges into 14 cents of new debt and 10 shares per dollar; full participation implies 41% (287/700); participants' securities are worth 36.5 per 100 whereas a holdout of 50 bonds is "materially better off" at 100; if too many hold out, chapter 11 costs cut value from 287 to 215 and recovery from 41.0% to 30.4% (p.85). Solutions: repeated-game "moral" coercion among a small community of regulars (the "bluff" must be credible, p.86); and "coercive structural devices", the most common being to "strip the covenant protections of nontendering bonds" (exit consents) and to couple the exchange with a prepack solicitation (p.86). Moyer p.334 draws the contrast the book needs: "a class minority can effectively defeat the wishes of the majority to effect an out-of-court restructuring. In bankruptcy, minority rights are significantly reduced." That sentence is the economic reason the whole LMT era exists (Ch 13): the out-of-court unanimity right (sacred rights) is the friction that uptiers and drop-downs route around.

### 1.6 Claims and trade-claim purchase (p.310-312)

Trade claims "are general unsecured claims and thus are equal in status with unsecured debt" and trade at a discount to the bonds (p.310); the risk is that the purchased claim will not be "an allowed claim" (p.311) and that the transfer is not valid (Rule 3001(e), p.312). There is no 503(b)(9) discussion in the PDF (the 20-day goods administrative priority came with BAPCPA, after the book); Ch 12-B must source it elsewhere.

## 2. Bohn-Stein and Schmid: lien subordination, hazard-rate change of measure (Ch 6-B, 12-B)

(to be filled)

## 3. Veronesi (Tuckman-style): price-yield, duration, convexity, OAS (Ch 4-B)

(to be filled)

## 4. Greeks and option measures (Ch 6-B)

(to be filled)

## 5. Fundamental law of active management (Ch 2, 4, 28, App E)

(to be filled)

## 6. Brownian-bridge first-passage correction (Ch 6-B)

(to be filled)

## 7. Bolder: threshold models, copulas, tail dependence (Ch 7-B)

(to be filled)

## 8. Dynkin: empirical duration regimes (Ch 4-B, Ch 8)

(to be filled)

## 9. Where the shelf is dated or superseded (2018-2026, web-confirmed)

(to be filled)

## 10. Quotation bank (verbatim, book_id p.N)

(to be filled)

## 11. Chapter map

(to be filled)

## Sources

(to be filled)

## Book placement

(to be filled)
