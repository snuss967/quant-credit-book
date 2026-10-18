export const meta = {
  name: 'ed2-chapter-pipeline',
  description: 'Configurable per-chapter Edition 2 pipeline: U1 code explanations, U4 figures + figure check, U3b resource graphs, U2 Fable brief + Opus revision + Sonnet verify (stages chosen by args.stages)',
  phases: [
    { title: 'Explain code', detail: 'Sonnet: replace EXPLAIN stubs with prose (U1)', model: 'sonnet' },
    { title: 'Figures', detail: 'Sonnet: 3-5 house-style figures per chapter (U4)', model: 'sonnet' },
    { title: 'Figure check', detail: 'Sonnet: view every figure, check math, caption, legibility', model: 'sonnet' },
    { title: 'Resources', detail: 'Sonnet: specific episodes and posts in the Resource Graphs (U3b)', model: 'sonnet' },
    { title: 'Brief', detail: 'Fable: revision brief per chapter', model: 'fable' },
    { title: 'Revise', detail: 'Opus: narrative revision per the brief (U2)' },
    { title: 'Verify', detail: 'Sonnet: nothing removed, new facts checked, hygiene', model: 'sonnet' },
    { title: 'Lessons', detail: 'Opus: apply u2_lessons to chapters revised before the lessons existed' },
    { title: 'RV thread', detail: 'Opus: weave the chapter\'s relative-value beat into revised chapters' },
  ],
}
const ROOT = '/home/user/quant-credit-book'
const MARK = '<!-- STATUS: COMPLETE -->'
const VOICE = `VOICE (Edition 2 user directives; these outrank older guidance and the reviews): read "## 8. Edition 2 Voice Amendments" in state/style_bible.md and state/user_directives_ed2.md, and follow them. Teach the way an engaging novel teaches: lead with scenes and real credit events, build intuition before formulas, and be less prescriptive (fewer bare statements and imperatives; more "here is what happened, and here is the idea that would have helped"; more judgment about when a tool applies and when it breaks). Put a "> **Math, Gently.**" box at the first use of each mathematical concept, building blocks included. Add "> **View From Another Seat.**" boxes where another kind of investor or dealer would see the situation differently (name real firms only for publicly stated views, with a citation). Include a labeled fictional quant-shop-life vignette, and the boring parts are welcome. The user's own verdict on Edition 1 is "a lot of prescriptiveness and not narrative": turn rules, imperatives, "should/must/always/never" sentences, and bullet lists into scenes, worked stories, and reasoning the reader watches unfold; let a character discover the rule the hard way instead of stating it. Keep modal and imperative density low (python3 tools/prescriptiveness.py measures it). RELATIVE-VALUE THREAD (user directive 13): the pod-shop trade, long one credit and short another, hedged so that what remains is the idiosyncratic view, runs through every chapter. If state/rv_thread.md exists, read this chapter's entry: it assigns the chapter its RV beat (a scene, or a "> **The Pair.**" box) and its place in the running Pair Book (state/rv_pair_book.md). Make the isolation logic explicit: what the hedge removes, what idio remains, what leaks, and what it costs to carry and to short. Remove no topics.
CODE: chapters carry no code. Where a listing belongs, first build up to it: explain in prose what problem it solves at this point in the story, what it computes, why it is built that way, its inputs and outputs, when to use it and when not, and the edge case that bites. Then put a line containing exactly <!-- EXPLAINED --> and the fenced python listing immediately after. The orchestrator moves listings to Appendix F mechanically and leaves a link.`

const u1 = stem => `You are a CODE EXPLAINER (Edition 2, task U1) for the book in ${ROOT} ("Systematic & Quantitative Credit: From PJT RSSG to the Automated Desk"; reader: a restructuring banker moving to a systematic credit desk). Work from ${ROOT}. File: book_src/${stem}.md.
Every code listing has moved to book_src/95_appF_code_companion.md. In the chapter, each one left a two-line stub:
<!-- EXPLAIN: Listing N.k -->
> **Code Companion: Listing N.k.** (description). The full python listing is in [Appendix F, Listing N.k](#code-...).
Run grep -n "EXPLAIN: Listing" book_src/${stem}.md. If there are none, stop and return "none".
Read the voice once at the start: sections 1, 2 and 8 of state/style_bible.md (grep -n "^## " then sed the ranges).
Then, for each stub in order:
1. Read the listing in Appendix F: grep -n the stub's anchor (the #code-... id) in book_src/95_appF_code_companion.md, then sed -n from there to the next "### Listing".
2. Read the chapter around the stub (about 12 lines before and 4 after; lines are whole paragraphs) to see where the story stands.
3. Replace BOTH stub lines with one Edit (old_string = the two stub lines exactly). The new text is prose in the book's voice. First write a bridge paragraph that builds up to the code: the problem the reader faces at this point in the section, and why a desk would automate it. Then write 150–400 words on what the listing computes step by step, why it is built that way, its inputs and outputs, when to use it and when not to, and the one edge case that bites. End with the line: *The full listing is [Listing N.k in Appendix F](#code-...).* (keep the original anchor). No code blocks; inline \`names\` are fine. Describe only what the code really does.
If the text just above the stub already explains the listing fully, write only a 1–2 sentence bridge plus the link line.
Change nothing else in the file. Each stub is one Edit, so progress is saved as you go; on a resume, the grep shows what is left.
Finish by confirming grep -c "EXPLAIN: Listing" returns 0. Return a 40-word summary.`

const brief = stem => `You are a FABLE REVISION ADVISOR (Edition 2, task U2) for the book in ${ROOT} ("Systematic & Quantitative Credit: From PJT RSSG to the Automated Desk"; reader: a PJT RSSG restructuring banker moving to a systematic credit desk). Work from ${ROOT}.
Chapter: book_src/${stem}.md. Output: state/revisions/ed2/${stem}.brief.md.
FIRST: if the output exists and ends with ${MARK}, stop and return "exists".
Read: state/user_directives_ed2.md (item 12 is the user's headline verdict); state/reviews/ed2/u2_lessons.md if it exists (lessons from quality reads of revised chapters); "## 8. Edition 2 Voice Amendments" and the cast section of state/style_bible.md (grep -n "^## " then sed); the chapter's headings (grep -n "^#"); its cold open, its case studies, and two or three of its densest sections (sed ranges, about 12k words at most in total); grep the chapter's stem and number in state/reviews/ed2/*.md and state/reviews/ed1/engagement.md for what reviewers asked of it; ls state/research/ and grep the dossiers for real events that fit this chapter. No web research. At most about 20 tool calls.
The user's verdict on Edition 1: it reads like a manual. It is too prescriptive, with facts stated rather than earned, math without context, code dropped in, and stories that are too short. Your brief tells one Opus writer how to make this chapter teach the way an engaging novel teaches, WITHOUT removing any topic, derivation, case, box, exercise, or resource.
If the chapter already has figures (grep -n '!\\[Figure' on it), list them in section 3 and propose only additional ones.
Write 1,500–2,500 words:
1. The spine: the one question the reader should feel by the end of the cold open, and how the chapter answers it.
2. A numbered EDIT CHECKLIST of 12–25 items in file order. Each item gives: [anchor heading] · action (EXPAND-SCENE, NEW-SCENE, MATH-GENTLY, ANOTHER-SEAT, SHOP-LIFE, WHEN-TO-APPLY, LIST-TO-NARRATIVE, FULL-DERIVATION-MOVE, BRIDGE) · what exactly to write (the beats, the numbers, the twist, the joke) · facts to use with their source (dossier path or chapter section), with CHECK on anything unverified.
   Every chapter needs:
   - at least two long scenes (2,000–4,000 words each) built on REAL credit events with dated, sourced facts. The fictional cast may argue, be wrong, and change their minds; real people never get invented words. Each scene ends at a "what would you do here, and why?" decision point that the chapter's tools then answer;
   - a Math, Gently box at the FIRST use of every mathematical concept in the chapter. List them all, with the analogy and the tiny worked number to use, and include the building blocks (distributions and how they differ, random walks, Itô's ½σ², risk-neutral pricing) where they first appear;
   - 2–3 View From Another Seat boxes (opportunistic credit fund, direct lender, multi-strategy RV pod, dealer desk, CLO manager, insurer, systematic fund), naming real firms only for publicly stated views;
   - one labeled fictional quant-shop-life vignette: the shop type, the mundane task, and how it connects to the chapter (boring parts welcome);
   - a "When to reach for it, and when it breaks" judgment passage for each major tool;
   - the list-heavy passages to rewrite as narrative (by heading);
   - the dense derivations to move into "The Full Derivation" subsections after the intuition.
   - its RELATIVE-VALUE beat (user directive 13): if state/rv_thread.md exists, take this chapter's assigned beat from it; otherwise design one. It is a scene or a "> **The Pair.**" box in which the pod trade (long one credit, short another, hedged so the residual is the idiosyncratic view) is built or stress-tested with THIS chapter's tool. Name the pair, the hedge construction, what the hedge removes, what idio remains, what leaks, and what it costs to carry and to short.
3. Three or more FIGURE ideas: file name chNN_slug.png, type (payoff diagram, waterfall, timeline, flow graph, distribution, data series), the data or formula to plot, and the caption. These go to a later figures pass, not to the writer.
4. Must not change: the derivations, cases, and boxes the writer must keep intact.
DURABILITY: write the file in two passes. Your FINAL action is appending a line containing exactly ${MARK}. Return a 60-word summary.`

const revise = stem => `You are a REVISION WRITER (Edition 2, task U2) for the book in ${ROOT} ("Systematic & Quantitative Credit: From PJT RSSG to the Automated Desk"). Work from ${ROOT}.
Chapter: book_src/${stem}.md. Brief: state/revisions/ed2/${stem}.brief.md. Progress log: state/revisions/ed2/${stem}.log.md.
FIRST: if the brief is missing or lacks ${MARK}, stop and return "no brief". If the log ends with ${MARK}, stop and return "done". If the log exists, resume at its first unticked item. Otherwise create the log by copying the brief's EDIT CHECKLIST as "- [ ] N. ..." lines.
Read: state/style_bible.md (all of it; it is the voice), state/user_directives_ed2.md, and the brief.
If state/reviews/ed2/u2_lessons.md exists, read it first: it holds lessons from the quality reads of earlier revised chapters, and it outranks the brief where they differ. Then read the chapter section by section as you edit it (sed ranges; lines are whole paragraphs). For dossiers the brief names, grep and sed only what you need. Web: at most 6 calls, only for facts the brief marks CHECK; if you cannot verify a fact, write around it rather than state it.
${VOICE}
Work the checklist in order. Each item is one or more Edit calls on the chapter. After finishing an item, tick it in the log ("- [x]") with a 10-word note. This is your durability: never hold more than one item's prose only in context.
Rules: remove no topic, derivation, case, exercise, source extraction, Trend Watch box, or resource. You may move a derivation into a "#### The Full Derivation" subsection after the intuition, and you may rewrite list-heavy prose as narrative, but every fact and formula survives. Keep section numbering, anchors, cross-references, "Used in" lines, and every existing Appendix F link. Keep the chapter's last line as ${MARK}. Pandoc math: $...$ inline and $$...$$ display on their own lines. Escape currency as \\$. Never put a line of --- directly before text. Add no code blocks (see CODE). Do not run builds or code.
Expect to add 5,000–9,000 words. When every item is ticked, your FINAL action is appending a line containing exactly ${MARK} to the log. Return a 60-word summary.`


const PRE = args.pre_commit
const verify = stem => `You are a REVISION VERIFIER (Edition 2) for the book in ${ROOT}. Work from ${ROOT}.
Chapter: book_src/${stem}.md, just revised by a writer following state/revisions/ed2/${stem}.brief.md. The pre-revision text is in git: git show ${PRE}:book_src/${stem}.md > /tmp/pre_${stem}.md. Output: state/revisions/ed2/${stem}.verify.md.
FIRST: if the revision log state/revisions/ed2/${stem}.log.md lacks ${MARK}, stop and return "revision not finished". If the output exists and ends with ${MARK}, stop.
Run three checks, fixing problems directly in the chapter with small Edits, and write the report as you go:
1. Nothing removed. With a short python3 script, compare the pre and post texts: headings (lines starting with #), the number of display-math blocks ($$), [SOURCE EXTRACTION] blocks, Trend Watch boxes, exercises, Appendix F links (#code-), and Resource Graph items. For anything missing, find it in the pre text and restore it in the right place. Moving a derivation into a "The Full Derivation" subsection is fine; deleting it is not.
2. Facts. Using python3 difflib by section, list every NEW factual claim the revision added about real events, firms, people, dates, amounts, prices, or rulings. Verify each against the dossier the brief names or with web search and fetch (load them via ToolSearch; at most 15 web calls, primary sources first). Fix wrong facts, and hedge or remove what cannot be verified. Make sure no real person has invented dialogue or quotes, and that fictional composites are labeled as such.
3. Hygiene. No code blocks in the chapter except \`\`\`text diagrams; math delimiters balanced; currency escaped as \\$; no line of --- directly before text; the last line is ${MARK}.
The report lists what you checked, what you fixed, and what remains doubtful. Your FINAL action is appending a line containing exactly ${MARK} to the report. Return a 60-word summary.`


function tagOf(stem) {
  const m = stem.match(/^\d+_ch(\d+)([a-z]?)_/)
  if (!m) return { tag: stem.slice(0, 6), label: stem.slice(0, 6) }
  const n = String(parseInt(m[1], 10))
  return { tag: `ch${m[1]}${m[2]}`, label: m[2] ? `${n}-${m[2].toUpperCase()}` : n }
}
const figures = stem => { const { tag, label } = tagOf(stem); return `You are a FIGURE MAKER (Edition 2, task U4) for the book in ${ROOT} ("Systematic & Quantitative Credit: From PJT RSSG to the Automated Desk"; reader: a restructuring banker moving to a systematic credit desk). Work from ${ROOT}.
Chapter: book_src/${stem}.md (chapter label ${label}; figure file prefix ${tag}). Log: state/revisions/ed2/${stem}.figures.md.
FIRST: if the log ends with ${MARK}, stop and return "done". If the log exists, resume: the figures it lists as embedded are done.
1. Read tools/figures/style.py. Its docstring is the house style: follow it exactly, and import it as the docstring shows.
2. Choose 3–5 figures. Use section 3 of state/revisions/ed2/${stem}.brief.md if it exists; otherwise read the chapter's headings and key sections and pick the figures that would most help a reader build intuition: payoff diagrams, capital-structure waterfalls, timelines of the chapter's real credit events, flow graphs, state machines, distributions, data series. Skip any idea the chapter already has a figure for (grep -n '!\\[Figure').
3. Data: real data only from sourced dossiers (state/research/trend_figure_data_series.md and the others; cite them in the caption) or from public datasets you fetch yourself (e.g., FRED CSV at https://fred.stlouisfed.org/graph/fredgraph.csv?id=SERIES, cited by series ID). Otherwise generate the data from a stated model and caption it "Illustrative". Never invent numbers and present them as real.
4. Write tools/figures/${tag}.py, which generates every figure for this chapter as assets/figures/${tag}_<slug>.png (draw flow graphs and state machines with matplotlib patches and arrows; graphviz is not installed). Run it. Then LOOK at every PNG with the Read tool and fix label collisions, clipped text, wrong shapes, and anything unreadable. Re-run until each one is clean.
5. Embed each figure at the paragraph it illustrates: one Edit per figure, inserted after that paragraph (never inside a list, a box, or display math), with a blank line before and after:
![Figure ${label}.k: One-sentence caption that says what to notice. Source: ... (or Illustrative: ...)](assets/figures/${tag}_<slug>.png)
Number the figures ${label}.1, ${label}.2, ... in order of appearance, counting any existing ones. You may add one short sentence of prose that points to the figure ("Figure ${label}.2 shows ..."). Change nothing else in the chapter.
6. Log each figure in the log as you finish it: name, section, what it shows, data source.
Your FINAL action is appending a line containing exactly ${MARK} to the log. Return a 40-word summary.` }

const figcheck = stem => { const { tag } = tagOf(stem); return `You are a FIGURE CHECKER (Edition 2) for the book in ${ROOT}. Work from ${ROOT}.
Chapter: book_src/${stem}.md. Figures log: state/revisions/ed2/${stem}.figures.md. Script: tools/figures/${tag}.py. Output: state/revisions/ed2/${stem}.figcheck.md.
FIRST: if the figures log lacks ${MARK}, stop and return "figures not finished". If the output ends with ${MARK}, stop.
Read the docstring of tools/figures/style.py (the house style). Then, for every ${tag}_*.png embedded in the chapter:
1. Correctness. Read the part of the script that draws it, and confirm that the math and shapes are right: payoff kinks at the strikes, waterfall tranches that sum to the total, the right tails on distributions, monotonicity where the theory demands it, and dates of real events placed correctly.
2. Honesty. The caption matches what the image shows and gives a source, or says "Illustrative". Real-data claims trace to a cited source.
3. Legibility and style. View the PNG with the Read tool: no collisions, clipping, or tiny text. One y-axis, colors in fixed order, direct labels wherever slots 3–5 are used, text in ink.
4. Embedding. The syntax is right, the file exists, figures are numbered in order, and the image sits next to the paragraph it illustrates.
Fix problems directly (edit the script, re-run it, re-view, and fix the caption or placement with small Edits). Write the report as you go: a verdict per figure and the fixes made. Your FINAL action is appending a line containing exactly ${MARK} to the report. Return a 40-word summary.` }

function mediaDossier(stem) {
  const m = stem.match(/^(\d+)_/)
  const n = m ? parseInt(m[1], 10) : 0
  if (n >= 90) return 'state/research/media_episodes_posts_parts_V_VIII.md'
  if (n <= 7) return 'state/research/media_episodes_posts_parts_I_II.md'
  if (n <= 17) return 'state/research/media_episodes_posts_parts_III_IV.md'
  return 'state/research/media_episodes_posts_parts_V_VIII.md'
}
const resgraph = stem => `You are a RESOURCE EDITOR (Edition 2, task U3b) for the book in ${ROOT}. Work from ${ROOT}. Chapter: book_src/${stem}.md. Log: state/revisions/ed2/${stem}.resgraph.md.
FIRST: if the log ends with ${MARK}, stop and return "done".
The user wants specific podcast EPISODES and blog POSTS throughout the book, not channels or homepages. The verified items are in ${mediaDossier(stem)}: grep -n "${stem}" to find this chapter's section (if there is none, use the items whose "why / section" fits this chapter's topics).
For every "### Deep-Dive Resource Graph" (and any similar resource list) in the chapter:
1. Replace each channel-level or homepage-only reference (a show, a blog, or a newsletter named without a specific episode or post) with the specific episode or post from the dossier that serves that section, keeping one line on why it is worth the reader's time.
2. Add 3–6 specific items from the dossier that fit the section. Format each as: **Title** (show or author, date). One line on why. URL.
3. Keep every existing specific item (papers, books, datasets, verified URLs). Remove nothing else.
Use only items from the dossier (they were verified when it was written) or items you verify yourself by fetching the page (at most 6 web calls; load WebFetch via ToolSearch). Never invent titles, dates, or URLs.
Each Resource Graph is one Edit. Log each graph you upgraded (section, items added or replaced) as you go. Your FINAL action is appending a line containing exactly ${MARK} to the log. Return a 40-word summary.`

const lessons = stem => `You are a LESSONS EDITOR (Edition 2) for the book in ${ROOT} ("Systematic & Quantitative Credit: From PJT RSSG to the Automated Desk"). Work from ${ROOT}.
Chapter: book_src/${stem}.md. It was revised for narrative BEFORE state/reviews/ed2/u2_lessons.md existed, so it may stack new scenes on old paragraphs, overuse boxes, carry templated judgment paragraphs, or leak research notes. Log: state/revisions/ed2/${stem}.lessons.log.md.
FIRST: if state/revisions/ed2/${stem}.verify.md lacks ${MARK}, stop and return "verify not finished". If the log ends with ${MARK}, stop and return "done". If the log exists, resume at its first unticked item.
Read: state/user_directives_ed2.md (item 12: "a lot of prescriptiveness and not narrative"); state/reviews/ed2/u2_lessons.md (the rules); sections (b)–(d) of state/reviews/ed2/u2_quality_read.md and the Ch 1 table in state/reviews/ed2/u2_fixes_ch01_05_06.md (worked examples of this exact job); state/cast_bible.md; and "## 8. Edition 2 Voice Amendments" in state/style_bible.md.
AUDIT first, and write it into the log as "- [ ] ..." items before any edit:
(a) python3 tools/prescriptiveness.py --pre ${PRE} book_src/${stem}.md, recorded as "before"; growth against the 1.6–1.9× target;
(b) duplication: every place a new scene retells what an older paragraph still states (both locations, which telling survives);
(c) templates: grep for the banned phrasings in lesson 4 and for detached "When to reach for it" paragraphs that a scene already shows;
(d) boxes: Math, Gently count and adjacency against the lesson-6 budget (merge or demote extras to one-sentence glosses with pointers; first load-bearing use only), and runs of more than two boxed elements;
(e) research-note leaks ("CHECK", "search summary", "secondary") and fiction-label gaps;
(f) the Finder table at the top of the Desk Debrief (lesson 11), and promotion of long scenes to #### headings;
(g) cast-bible contradictions;
(h) the chapter's RELATIVE-VALUE beat: if state/rv_thread.md exists and this chapter lacks its assigned beat, add an item to write it (scene or "> **The Pair.**" box) and update state/rv_pair_book.md.
Then FIX the items in order. Each item is one or more Edits; re-grep before editing, and tick each item with a 10-word note.
Rules: remove no topic, numbered equation, Source Extraction with its page number, fact-checked Trend Watch wording, exercise, figure, Appendix F link, or verified URL. Duplicate paragraphs MAY be retired by merging them into the surviving telling. Keep the last line as ${MARK}. Pandoc math: $...$ inline and $$...$$ display on their own lines. Escape currency as \\$. Add no code blocks. Do not run builds.
Finish by running the metric again and recording "after". Your FINAL action is appending a line containing exactly ${MARK} to the log. Return a 60-word summary with the before and after metrics and the word count.`

const rv = stem => `You are an RV WEAVER (Edition 2, user directive 13) for the book in ${ROOT} ("Systematic & Quantitative Credit: From PJT RSSG to the Automated Desk"). Work from ${ROOT}.
The user: "deeply explore the relative value side of quantitative credit, particularly the pod shop long a credit short a credit so that we can isolate the idio as the alpha. That weaves through every chapter. Be intentional about how you work it in."
Chapter: book_src/${stem}.md. Log: state/revisions/ed2/${stem}.rv.md.
FIRST: if state/rv_thread.md is missing or lacks ${MARK}, stop and return "no thread". If the log ends with ${MARK}, stop and return "done". If another agent is mid-revision on this chapter (state/revisions/ed2/${stem}.log.md exists without ${MARK}), stop and return "busy".
Read: state/rv_thread.md (the spine, canonical homes, and THIS chapter's entry); state/rv_pair_book.md (the running ledger of the fictional pod's pairs); state/cast_bible.md; state/reviews/ed2/u2_lessons.md; "## 8. Edition 2 Voice Amendments" in state/style_bible.md; and state/research/rv_*.md dossiers that the thread names (grep and sed only what you need).
Then grep the chapter for what it already says about pairs, hedges, idiosyncratic return, and relative value, and read the sections where the beat belongs. If the chapter ALREADY contains its assigned beat (grep the PB-id the thread assigns, or "The Pair."), do not write a second one: check the existing beat against the thread entry and strengthen it in place (isolation logic, real short leg, costs, ledger update), then log "strengthened".
Write the chapter's RV beat exactly as the thread specifies it: a scene (800–2,000 words, built on a real dated event where the thread names one, with fictional positions labeled) or a "> **The Pair.**" box (250–600 words). It must build or stress-test the pair with THIS chapter's tool, and make the isolation explicit: the two legs, the hedge construction (spread duration, DTS, empirical beta, or factor-model residual), what the hedge removes, what idio remains, what leaks, and the carry, funding, and borrow cost (cash bonds are hard to short, so name the real short leg). Retire any older paragraph that the beat now tells better (one telling per fact); never remove a topic, equation, Source Extraction, Trend Watch, exercise, figure, Appendix F link, or URL. Add one cross-reference to the canonical home. Then append the pair's entry or update to state/rv_pair_book.md (pair, legs, hedge ratio and method, chapter, status, idio share, what leaked).
Rules: real firms and people only through their sourced public record; no invented quotes; fictional pod numbers marked illustrative. Pandoc math: $...$ inline and $$...$$ display on their own lines. Escape currency as \\$. Add no code blocks. Keep the chapter's last line as ${MARK}.
Log what you wrote and where. Your FINAL action is appending a line containing exactly ${MARK} to the log. Return a 60-word summary.`

const STAGES = {
  u1: { make: u1, phase: 'Explain code', model: 'sonnet' },
  figures: { make: figures, phase: 'Figures', model: 'sonnet' },
  figcheck: { make: figcheck, phase: 'Figure check', model: 'sonnet' },
  resgraph: { make: resgraph, phase: 'Resources', model: 'sonnet' },
  brief: { make: brief, phase: 'Brief', model: 'fable', effort: 'high' },
  revise: { make: revise, phase: 'Revise' },
  verify: { make: verify, phase: 'Verify', model: 'sonnet' },
  lessons: { make: lessons, phase: 'Lessons' },
  rv: { make: rv, phase: 'RV thread' },
}
const order = (args.stages || ['u1', 'figures', 'figcheck', 'brief', 'revise', 'verify']).filter(s => STAGES[s])
log(`stages: ${order.join(' -> ')} for ${args.stems.length} chapters`)
const stageFns = order.map(s => (prev, item) => {
  // stage 1 may be called as (item, index); later stages as (prevResult, item, index)
  const stem = typeof item === 'string' ? item : prev
  const st = STAGES[s]
  const opts = { label: `${s}:${stem}`, phase: st.phase }
  if (st.model) opts.model = st.model
  if (st.effort) opts.effort = st.effort
  return agent(st.make(stem), opts).then(r => ({ ...(prev && typeof prev === 'object' ? prev : {}), [s]: r }))
})
return await pipeline(args.stems, ...stageFns)
