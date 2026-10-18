# Ch12 App Z numbers fix log

## Note 1: "The Queue" (§12.7), Kaz's grading: "nearer seven at the technology fund"
- Note: with requests of about 40% of shares against a 5% gate, Q/g = 8, so the 90-day tau is off by about eight, not seven; HPS figure (9/5 = 1.8, "a factor of two") checks.
- Recomputation (/tmp/ed/ch12_queue.py): constant fill p = g/Q, dollar-weighted mean exit = sum n p (1-p)^(n-1) = 1/p = Q/g quarters. HPS (Q = 9%): 1.80 quarters = 164 days, 1.82x a 90-day tau, "a factor of two" holds. OTIC (Q = 40%): 8.00 quarters = 730 days, 8.1x a 90-day tau; a line that stops growing also drains in Q/g = 8 quarters. Seven would need Q = 35% (7.0 quarters, 7.1x). The chapter's own 40% for the technology fund is supported by state/research/media_episodes_posts_parts_III_IV.md (Octus EP 28: repurchase requests on 40% of shares against a 5% limit) and open_items_ch12_ed2.md item 8.
- Ruling: fixed (note right).
- Edit, book_src/12_ch12_multi_asset_credit_allocation.md, "Long Scene: The Queue", Beat 4 grading: "and by something nearer seven at the technology fund" -> "and by something nearer eight at the technology fund".
- App Z: solution text did not quote the old value; NOTE paragraph deleted from state/appZ/12_ch12_multi_asset_credit_allocation.md. (The copy in state/appZ/_editor_notes.md, an aggregate, was left untouched.)

<!-- STATUS: COMPLETE -->
