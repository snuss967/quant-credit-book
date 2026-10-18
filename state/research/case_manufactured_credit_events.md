# Case Autopsy: Manufactured and Disputed Credit Events

Codere 2013, Hovnanian 2018, Sears 2019 auction, Windstream 2019, Altice France Holding 2025 (300/5 no-auction), NTCE 2019 amendments.

Researcher dossier for the book "Systematic & Quantitative Credit". Feeds: 24_ch24_bond_cds_basis_and_deliverables.md, 93_appD_market_plumbing_and_contract_mechanics.md, 25_ch25_nlp_pacer_and_covenant_scraping.md. Drafted 2026-10-18. Facts are tagged [S#] and resolve in the Sources section; anything not verified this session is marked UNVERIFIED.

## 0. Gap inventory: what Ch 24 already covers

Inventory of book_src/24_ch24 §24.8 (read 2026-10-18; chapter is 15.7k words) and App D §D.5-D.7:

- Covered, in prose: the three kinds of engineering (manufactured default, manufactured non-default via RadioShack 2014, orphaning via McClatchy/Chatham 2018, $418.5mm); successor arithmetic (25/75 thresholds); Hovnanian as a full Docket Diary (GSO ~$333mm CDS, 28 Dec 2017 exchange, 5% 2040s, Sunrise Trails, Solus suit, 30 May 2018 settlement); Windstream (2015 Successor split, Aurelius judgment 15 Feb 2019, ~$310.5mm, Chapter 11 on 25 Feb, DC "no FTP" 26 Feb, auction 18 Mar 2019 at 29.5); Sears in one paragraph (the $82.5mm note auction, External Review "Yes" 19 Dec 2018, SRAC auction 17 Jan 2019); CFTC staff statement 24 Apr 2018; joint SEC-CFTC-FCA statement 24 Jun 2019; NTCE Supplement 15 Jul 2019 (Credit Deterioration Requirement and Outstanding Principal Balance); a Trend Watch on 2023-2026 DC governance and docket including Altice France Holding (FTP 25 Jun 2025, 11-0, "300/5 criteria not satisfied").
- App D: Table D.8 (Windstream auction parameters), Table D.9 (deliverable characteristics, North American standard), Table D.10 (successor rules).
- NOT covered at all: **Codere 2013** (zero mentions anywhere in book_src); the Hovnanian DC record and the court's actual ruling language; the Sears *notes auction* mechanics and the SRAC auction final price; the Sears deliverable dispute beyond one line; the Altice France 300/5 criteria text, what actually happened to the Altice France Holding swaps (no auction, what settles, how), and the liquidity consequence for single-name hedges; the NTCE supplement's operative wording and the three-way test; the SNAC deliverable-obligation characteristics against the 2014 Definitions (stated in App D in simplified form only); the question of whether anything was *ever* enforced against a manufactured event (no case as of Dec 2019).
- Possible internal inconsistencies to check against primary sources: App D labels the Windstream auction "DC decision of 6 Mar 2019" (that is the auction-terms vote, consistent); Ch 24 says the Hovnanian 20 Apr 2018 DC refusal is "discretionary authority" while the DC page shows a 13-15 Mar 2018 "Question Rejected" (possibly two requests); Ch 24 says GSO "tendered up to $170mm of its $236mm of 8% 2019s" (verify against Hovnanian 8-K / K&L Gates).


## 1. Dated timeline

(pending)

## 2. Instruments and tranches

(pending)

## 3. Price, spread and recovery paths

(pending)

## 4. Dollar amounts

(pending)

## 5. Legal and structural mechanics

(pending)

## 6. Players

(pending)

## 7. Outcome and later rulings

(pending)

## 8. What a systematic desk could have observed beforehand, and how it would have flagged and traded it

(pending)

## 9. Which model assumptions broke

(pending)

## 10. What the RSSG banker saw that the quant missed

(pending)

## Sources

(pending)

## Book placement

(pending)

## LEDGER (working notes, append-only, to be folded into sections above and then deleted)

### Hovnanian primary facts (read this session)
- [S1] DC page https://www.cdsdeterminationscommittees.org/?p=53208 : Issue 2018031301, "General Interest Question", category Other, 2014 and 2003 Definitions; Pending DC Consent 3/13/2018 10:50 AM EDT; Closed 3/15/2018 6:10 PM EDT; Outcome "Question Rejected"; no votes shown. Documents: Statement of Information, GSO motion to dismiss (2 Mar 2018), SDNY opinion (29 Jan 2018), Pickel supp. declaration (16 Jan 2018), Goodhill judgment, Bloomberg 9 Mar 2018 "GSO's Goodman Backs Closing CDS Loophole That His Firm Mastered".
- [S2] Solus Alternative Asset Management LP v. GSO Capital Partners L.P. et al., No. 18 CV 232-LTS-BCM (S.D.N.Y.), Doc 69, filed 29 Jan 2018, Judge Laura Taylor Swain, "Memorandum Opinion and Order Denying Motion for Preliminary Injunction". Claims: Exchange Act 10(b), 14(e), Rule 10b-5, tortious interference. Action commenced and OSC granted 11 Jan 2018; evidentiary hearing 25 Jan 2018; exchange offer to expire 11:59 pm 29 Jan 2018. Denied for want of irreparable harm only (merits not reached). Court findings: Hovnanian "has covenanted ... to default on an upcoming payment on the bonds that will be held by the affiliate notwithstanding the fact that Hovnanian has sufficient resources to make the payment. Payments to other holders of that bond issue will not be withheld." GSO "stands to profit significantly on its CDS position"; "This anticipated profit was factored into the below-market pricing of the long term bonds and certain other financing". Solus began Nov 2016 selling CDS protection, $260.5mm by 28 Dec 2017, plus $31.779mm Hovnanian bonds and 112,497 shares. Origin: Feb 2017, Ryan Mollett (GSO senior MD) "inspired by a December 2016 intentional default and CDS Credit Event involving iHeart Communications" (the court's wording). Mollett reviewed Hovnanian debt instruments "to determine whether a default sufficient to constitute a 'failure to pay' event, but not of such magnitude as to trigger a cross-default on all of Hovnanian's outstanding debt, could be engineered." 1 Aug 2017 Mollett arranged Sorsby (Hovnanian CFO) meeting with GSO outside counsel; 20 Oct 2017 NDA; 13 Nov 2017 White & Case letter for an ad hoc group; 15 Nov 2017 Bloomberg article. Solus's own competing financing proposal "included below market financing" and an unusual clause that Hovnanian would be in default under Solus's instruments if any failure to pay constituted a FTP Credit Event on CDS. Hovnanian itself is not a party to any CDS. Deal: exchange up to $185mm of 8% notes for new 13% notes due 2026 and new 5% notes due 2040 (court's wording; Ch24 says 13.5% - check 8-K); Sunrise (K. Hovnanian at Sunrise Trail III LLC) buys $26mm of 8% notes; Hovnanian agrees not to make the 1 May 2018 interest payment of $1.04mm to Sunrise, which "will just exceed the threshold" of the $1mm Payment Requirement; "far short" of cross-default magnitude. Purpose of pairing 13% (above par) with 5% 2040 (below par): "create a package that is, on average, attractive to investors, and also create a bond trading well below par so as to maximize monetary recovery for GSO under an CDS failure to pay Credit Event, by operation of the 'cheapest-to-deliver' rule." Hovnanian in CDX HY (100 names, equal weight). 7% notes: if outstanding on 15 Oct 2018 another $75mm senior debt accelerates; secured-notes covenant prevented using cash to redeem 7%/8% notes. Court: ISDA "is not ... so powerless to act" so no irreparable harm; damages adequate; Pickel (ex-ISDA GC/CEO) vs Selvaggio disagreed on proliferation. Pickel: CDS market works on the assumption that entities "will endeavor to avoid default whenever possible".
- [S3] DC Statement of Information (submitted 13 Mar 2018, unsigned submitter): GIQ asks whether s.11.1(b)(iii) of the 2014 Definitions (9.1(b)(iii) of 2003) permits a Protection Buyer to induce a Failure to Pay by giving consideration to the Reference Entity for withholding a payment. Cites Good Hill Master Fund L.P. v. Deutsche Bank AG, 146 A.D.3d 632 (1st Dep't 2017), which held the clause allowed a CDS party to act "without regard to the existence of the swap or any adverse effect it might have on [the counterparty]'s position". Cites Swain opinion at *4 (2018 WL 620490). "Parties to CDS Transactions involving at least two Reference Entities have used the Definitions as the scaffolding for an 'engineered default'".

### Sears Roebuck Acceptance Corp (SRAC) primary facts
- [S4] DC page https://www.cdsdeterminationscommittees.org/cds/sears-roebuck-acceptance-corp/ : Issue 2018101502, Credit Event, GIQ, 2014 and 2003 Definitions; Common Event Determination Date 15 Oct 2018; Auction Date 17 Jan 2019; Auction Settlement Date 23 Jan 2019; closed 10 Apr 2019. 15 Oct 2018 4:45pm pending DC consent; 16 Oct accepted; 17 Oct DC "resolved that a Bankruptcy Credit Event had occurred"; 18 Oct agreed to hold auction on 14 Nov 2018; 2 Nov Initial List; 7 Nov Supplemental List; 9 Nov DC extended auction "until a date to be determined, but no earlier than November 26, 2018"; 13 Nov challenges filed (MTN and CP obligations for insufficient documentation); 30 Nov external reviewers selected (Andy Brindle, Charles Whitehead, Jeffrey Golden by random draw); 19 Dec oral argument and unanimous "Yes"; 21 Dec decision published; 8 Jan 2019 Final List; 9 Jan draft auction terms (blacklines against Nine West and Astaldi ASTs); 15 Jan list of bidders and final terms. Advocates: Linklaters for "No"; "Yes" brief by Advocate and an amicus brief by "certain unnamed ISDA members".
- [S5] External Review Panel decision, 21 Dec 2018 (Brindle, Golden, Whitehead), https://www.cdsdeterminationscommittees.org/documents/2018/12/external-review-panel-decision-december-21-2018.pdf : Reviewable Question (published 30 Nov 2018): do the SRAC "2LL: PIK Term Loan" and "2L: Line of Credit Loans ($525.0m)", as defined in the Fifth Amendment to the Second Lien Credit Agreement dated 5 July 2018 (agent JPP, LLC), satisfy the Consent Required Loan characteristic (2014 Definitions s.3.14(b)(ii))? (Alternate Tranche Line of Credit loans excluded.) Unanimous "Yes". Reasoning: assignment under s.9.07 required Agent consent (and Borrower consent unless EoD) and an "Eligible Assignee" (>$300mm capital and surplus, approved by Agent; existing lender/affiliate/Approved Fund; or any Permitted Holder); restrictions "narrowing (but not eliminating altogether) the universe of possible assignees" do not defeat "capable of being assigned ... with ... consent"; Definitions "deliberately general"; the drafters knew how to say "without any contractual, statutory or regulatory restriction" (the Transferable definition) and did not; New York law, plain meaning; purpose of the characteristics "to cast a wide net to ensure greater liquidity through greater deliverability in order to avoid situations where no deliverables were available"; "There has been no suggestion here of bad faith or commercially unreasonable restrictions; this is not a situation such as might arise through a 'manufactured' set of facts." Panel acknowledged a "Yes" "may result in the prevention of some CDS contract holders from participating in the auction as a contingent buyer" and "this could result in the 'cheapest to deliver' changing"; noted contested loans "remain pari passu to all other senior unsecured obligations of Sears", so "natural limit to any price discrepancy"; suggested non-eligible protection sellers could unwind before the auction. Expressly reserved whether other restrictions might be "so commercially unreasonable as to effectively block"; "do not mean necessarily to set any precedent".
- [S6] Reviewable Question statement 30 Nov 2018 https://www.cdsdeterminationscommittees.org/documents/2018/11/sears-dc-statement-regarding-reviewable-question-november-30-2018.pdf (quoted in S5).
