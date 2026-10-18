# Red-pen log (Edition 2): 25_ch25_nlp_pacer_and_covenant_scraping.md

## B10 (RSSG red-pen 10): fixed

All changes in `book_src/25_ch25_nlp_pacer_and_covenant_scraping.md`, §25.8 "Claims Registers and the Transfer Feed"; one insertion of about 380 words (two paragraphs and one display equation) between the Rule 3001(e) paragraph and the Moyer/plumbing paragraph. No existing sentence altered or removed; the Rule 3001(e) text, the Moyer quote and the portal-status paragraph are untouched.

- **What the feed is for.** The transferee's identity is the signal: the restructuring-advisory read that a handful of claims funds buy trade, vendor and lease-rejection claims in the general unsecured (GUC) class until they hold a committee seat, a blocking position, or both. Hedged in-text as "a practitioner's pattern, not a frequency this chapter has measured."
- **Correction to the red-pen's wording.** The red-pen called the GUC class the one that "elects the committee." Under 11 U.S.C. §1102(a)(1) the U.S. trustee appoints it, and §1102(b)(1) draws it from the "seven largest claims" (prepetition committee that was "fairly chosen and is representative" can stand in). The text says appointed, not elected. Verified against Cornell LII, 11 U.S.C. §1102.
- **Connection to §25.7.** Defines $\theta^{\text{xfer}}_{j,c}$ (net transferee share of filed face) and $H^{\text{xfer}}_c$ (sum of squared net-buyer shares); states both as floors (the second on `holder_hhi` of §25.7.1 once affiliates are merged, per the Moyer entity-resolution annotation; the first because publicly traded notes escape Rule 3001(e)). Ties $\theta^{\text{xfer}}_{j,c}$ to the §25.7.1 blocking bar $\theta > \varphi/3$ on amount, noting the §1126(c) headcount test is separate. Caveat that $F_c$ is filed face and moves with objections and estimation, so the share is carried as an interval. Closing hedge: whether rising transferee concentration predicts plan outcomes is a hypothesis to test, not a cited result.

Verification: 1 web fetch (Cornell LII, 11 U.S.C. §1102(a)(1), (b)(1)). No new unverified numbers; the only number added is the statutory "seven largest claims." Currency escapes: none needed. `tools/check_book.py --file` passes (20,261 words). No topic removed; the chapter's closing status line preserved.
<!-- STATUS: COMPLETE -->
