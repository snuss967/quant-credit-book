export const meta = {
  name: 'ed2-rv-thread',
  description: 'User directive 13: Sonnet research on pod-shop credit relative value, then a Fable RV architect designs the thread through every chapter (state/rv_thread.md, Pair Book ledger, optional new chapter), then an Opus writer for the new chapter if endorsed',
  phases: [
    { title: 'Research', detail: 'Sonnet: two RV dossiers', model: 'sonnet' },
    { title: 'Architect', detail: 'Fable: the RV thread through every chapter', model: 'fable' },
    { title: 'Write', detail: 'Opus: the Pair Book chapter, if endorsed' },
  ],
}
const ROOT = '/home/user/quant-credit-book'
const MARK = '<!-- STATUS: COMPLETE -->'
const DURABILITY = `DURABILITY: if your output file exists, read it first; if it ends with ${MARK}, stop; if partial, continue it without rewriting. Otherwise create it within your first few tool calls and append as you go. Your FINAL action is appending a line containing exactly ${MARK}.`
const USER = `The user (a restructuring banker moving to a systematic credit desk) asked: "I want to make sure we are deeply exploring the relative value side of quantitative credit as well. Particularly the pod shop long a credit short a credit so that we can isolate the idio as the alpha. That weaves through every chapter. So be intentional about how you work it in."`

const ITEMS = [
  { slug: 'rv_pod_platforms_and_risk', title: 'How multi-manager pods run credit relative value: platform structure, risk regimes, economics, crowding', scope: `Public sources only (annual letters, filings, interviews, podcasts, reputable press, academic and industry papers). Cover: multi-manager platform structure (Millennium, Citadel, Balyasny, ExodusPoint, Point72, DE Shaw and others as publicly described); pass-through fees and why platforms pay PMs for idiosyncratic return; pod risk regimes (factor-neutrality mandates, gross and net limits, drawdown stops such as the widely reported 5%/7.5% style rules, "center book" or central risk overlays), how credit RV pods are described publicly (single-name pairs, capital-structure trades, basis, curve), crowding and the reported multi-manager unwinds (e.g., 2023–2025 episodes), and talent and capacity constraints. Record dated facts with sources; mark anything unconfirmed as CHECK. Include 10+ specific podcast episodes or posts about pods or credit RV (title, date, URL), each verified.` },
  { slug: 'rv_credit_pairs_literature_and_mechanics', title: 'Credit relative value: the literature and the mechanics of long-one-credit, short-another', scope: `Annotated bibliography plus mechanics. Papers (verify authors, year, title, venue): Duarte, Longstaff and Yu (2007) on the risk and return of fixed-income arbitrage; Yu (2006) on the profitability of capital-structure arbitrage; Ben Dor, Dynkin et al. (2007) on DTS; Asquith, Au, Covert and Pathak (2013) on borrowing corporate bonds; studies of the CDS-bond basis as a trade; idiosyncratic and residual returns in corporate bonds; pairs and statistical-arbitrage evidence in credit; empirical versus model hedge ratios; crowding in credit. Mechanics, with sources: how a cash corporate bond is actually shorted (repo, borrow fees, recalls, specials), when CDS, CDX, or HY and IG ETFs are the real short leg and the basis each introduces, hedge-ratio choices (spread duration, DTS, empirical beta, factor-model residual) and when they disagree, jump-to-default asymmetry in a pair, carry and funding, and how a pair's P&L is attributed. Name the 5 must-reads.` },
]
const research = it => `You are a RESEARCHER for the book in ${ROOT} ("Systematic & Quantitative Credit: From PJT RSSG to the Automated Desk"). Work from ${ROOT}. Today is ${args.today}.
${USER}
Item: **${it.title}**
Scope: ${it.scope}
Use web search and web fetch (load them via ToolSearch); prefer primary pages. Run ls state/research first and build on existing dossiers (trend_systematic_credit_industry, perspectives_dealers_and_systematic_shops, life_quant_shop_daily_life, papers_factor_replication_crisis_and_bond_data) rather than duplicating them; cite them where they already hold a fact.
Write state/research/${it.slug}.md (4,000–7,000 words): findings, an evidence table (| date | fact | source |), the mechanics in plain language with worked numbers, and "Book placement" (which chapter each item serves). End with Sources (URLs verified this session). Never invent quotes, titles, or URLs.
${DURABILITY}
Return a 100-word summary.`

phase('Research')
const dossiers = await parallel(ITEMS.map(it => () => agent(research(it), { label: `rv:${it.slug}`, phase: 'Research', model: 'sonnet' })))

phase('Architect')
const ARCH_SCHEMA = { type: 'object', properties: { summary: { type: 'string' }, new_chapter: { type: 'object', properties: { endorse: { type: 'boolean' }, stem: { type: 'string' }, title: { type: 'string' } }, required: ['endorse'] } }, required: ['summary', 'new_chapter'] }
const arch = await agent(`You are the FABLE RV ARCHITECT for Edition 2 of the book in ${ROOT} ("Systematic & Quantitative Credit: From PJT RSSG to the Automated Desk"; reader: a PJT RSSG restructuring banker moving to a systematic credit desk). Work from ${ROOT}.
${USER}
FIRST: if state/rv_thread.md ends with ${MARK}, stop and return the structured result from it.
Read: state/rv_thread_plan.md (the orchestrator's draft: current coverage, design, draft per-chapter beats); state/research/rv_pod_platforms_and_risk.md and state/research/rv_credit_pairs_literature_and_mechanics.md; state/user_directives_ed2.md (item 12: the user wants narrative, not prescription); state/reviews/ed2/u2_lessons.md; state/cast_bible.md; the TOC in SYSTEM_PROMPT.md section 3 including "Edition 2 additions"; state/digests/book_outline.md (every heading). Grep book_src/ for "pair", "relative value", "idiosyncratic", "hedge ratio", "DTS", and "residual" to see what each chapter already has. No web research. At most about 35 tool calls.
Design the thread intentionally. It is a spine, not a sticker on every chapter: each chapter's beat must use that chapter's own tool and teach one RV truth the reader could not get elsewhere, in an order that builds (introduce, formalize, stress, operate, scale).
Write:
1. state/rv_thread.md (3,000–5,000 words):
   (a) the spine in one paragraph;
   (b) the RV truths the book must teach, and which chapter owns each;
   (c) canonical homes (mechanics, risk regime, P&L explain, basis, pod economics), plus your decision on a dedicated chapter;
   (d) the Pair Book: the fictional pod (platform, PM, analyst, risk manager; check the cast bible, add new names only if needed, and label it a composite), its mandate and limits, and 10–16 named pairs on real public issuers and instruments, each with thesis, legs, hedge method, and the chapter where it is opened, stressed, or closed;
   (e) a PER-CHAPTER TABLE for every file in the TOC (all chapters, primers, new chapters, and appendices A, B, D, E), giving: stem · beat type (scene or "> **The Pair.**" box) · the pair · the chapter tool it uses · the isolation lesson (what is hedged, what idio remains, what leaks) · real dated event, if any, with its dossier source · cross-reference to the canonical home · RV figure idea;
   (f) rules for writers: labeling, no invented quotes, real short legs, costs, and narrative over prescription.
2. state/rv_pair_book.md: the ledger header and one row per planned pair (pair, legs, hedge method, opened in, status "planned").
3. If you endorse a dedicated chapter: append its entry to the END of "Edition 2 additions" in SYSTEM_PROMPT.md (same format, growth-rule file name, e.g., 08_ch08d_the_pair_book_long_one_credit_short_another) and write its Fable brief (1,500–2,500 words, scene-built, with the Pair Book pod as its setting) at state/advisor_briefs/<stem>.md. Touch nothing else in SYSTEM_PROMPT.md.
DURABILITY: write rv_thread.md first, in passes; end every file you create with ${MARK}.
Return the structured result: summary, plus new_chapter = {endorse, stem, title}.`, { label: 'fable:rv-architect', phase: 'Architect', model: 'fable', effort: 'high', schema: ARCH_SCHEMA })

if (!arch || !arch.new_chapter || !arch.new_chapter.endorse || !arch.new_chapter.stem) return { dossiers, arch }
phase('Write')
const VOICE = `VOICE: read "## 8. Edition 2 Voice Amendments" in state/style_bible.md, state/user_directives_ed2.md (items 12 and 13), and state/reviews/ed2/u2_lessons.md, and follow them. Teach like a novel: scenes on real dated credit events, intuition before formulas, judgment inside the scene, fictional composites labeled, no invented quotes from real people. Math, Gently boxes at first load-bearing use (at most one per 1,200 words). CODE: explain each listing in prose first, then a line containing exactly <!-- EXPLAINED --> and the fenced python listing; the orchestrator moves listings to Appendix F.`
const c = arch.new_chapter
const written = await agent(`You are a WRITER for Edition 2 of the book in ${ROOT} ("Systematic & Quantitative Credit: From PJT RSSG to the Automated Desk"). Work from ${ROOT}.
${USER}
Your file: book_src/${c.stem}.md, new chapter: "${c.title}". Brief: state/advisor_briefs/${c.stem}.md. Thread: state/rv_thread.md. Ledger: state/rv_pair_book.md.
FIRST: if the file ends with ${MARK}, stop. If it is partial, resume by appending. If the brief lacks ${MARK}, stop and return "no brief".
Read: state/style_bible.md (all of it), the brief, the thread, the ledger, state/cast_bible.md, and the two rv_* dossiers (grep and sed). Grep book_src/ for cross-references. Web: at most 5 calls, only for facts the brief marks CHECK.
${VOICE}
Write 9,000–12,000 words, built as scenes inside the pod. Include a Desk Debrief with a Finder table, exercises WITH brief solutions, and a \`### Deep-Dive Resource Graph\` of specific, verified items. Update the ledger rows this chapter opens or closes.
Pandoc math: $...$ inline and $$...$$ display on their own lines. Escape currency as \\$. Never put a line of --- directly before text. Write in 3–5 large passes. Do not run builds or code.
${DURABILITY}
Return a 60-word summary.`, { label: `write:${c.stem}`, phase: 'Write' })
return { dossiers, arch, written }
