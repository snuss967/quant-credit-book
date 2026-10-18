# Resource graph upgrade log: 93_appD_market_plumbing_and_contract_mechanics (Edition 2, U3b)

Dossier: state/research/media_episodes_posts_parts_V_VIII.md, section 93_appD_market_plumbing_and_contract_mechanics (plus the Ch 22 section for the Treasury-clearing items, and the "Verified spares" note).

## Deep-Dive Resource Graph (end of D.11), upgraded in one Edit-equivalent replacement of the Podcasts and Practitioner Writing blocks

Replaced (channel-level or unlinked -> specific):
- Credit Derivatives Determinations Committees, homepage only -> "About Determinations Committees" with the DC Rules and CD Physical Settlement Matrix pages (dossier row), keeping the homepage and creditfixings auction link inside the same item.
- Matt Levine, Money Stuff, "columns ... 2018 (no link verified)" -> "Blackstone May Do Its Cleverest CDS Trade Again" (Bloomberg Opinion, 17 Nov 2017), the column already used in the Ch 24 graph.

Added (6 items):
- Podcast: Odd Lots, "Zoltan Pozsar and Perry Mehrling On The Historic Crisis Of Financial Market Plumbing" (30 Mar 2020), D.3.
- Podcast: The SIFMA Podcast, "Preparing for US Treasury Clearing: Industry Readiness and the Done-Away Framework" (31 Jul 2026), D.2 (Ch 22 section of the dossier).
- Blog: NY Fed Liberty Street Economics three-post repo series (28-30 Sep 2026), D.3.
- FEDS Note: "The $12 Trillion US Repo Market" (11 Jul 2025), D.3.
- FEDS Note: "Proportionate margining for repo transactions" (14 Feb 2025), D.2-D.3.
- Blog: ISDA derivatiViews (Scott O'Malia), "How Efficiency Enhances Resilience in the Financial System" (13 Oct 2026), D.2 (Ch 22 section of the dossier).

Reformatted to **Title** (show, date) + one line why, content kept: ISDA Episode 60 (now with its dossier why-line), Odd Lots/Younger, Cloud 9fin Ardagh, Cloud 9fin loan data.

Kept unchanged: EC "A shorter settlement cycle", BNP T+1, NY Fed tri-party repo statistics, all Academic Papers, all Data & Code (SEC release, ISDA, DTCC, FINRA, LSTA, App B pointer).

## Verification notes
- Dossier items used as-is (verified 2026-10-18 per the dossier): all six additions, the DC pages, ISDA Episode 60, Younger, Ardagh, fax-to-future.
- Levine column: Bloomberg returns HTTP 403 to fetch. One web search returned the headline "Blackstone May Do Its Cleverest CDS Trade Again" on both the Bloomberg View URL and a BloombergQuint copy, and the column's Hovnanian/Codere content; the 17 Nov 2017 date is read from the URL path. Re-check the exact byline date before print.
- Web calls used: 2 (1 search, 1 blocked fetch). Nothing invented.
- Dossier note: D.1 (settlement) has no podcast or blog beyond the Ch 21 loan-data episode, already listed. Spare not placed: Odd Lots, Anil Kashyap on the Fed as "market maker of last resort" (28 Aug 2024).
- Edit method: the replacement was applied by a short Python script over the contiguous Podcasts-to-Practitioner block (one replacement), not the Edit tool.

<!-- STATUS: COMPLETE -->
