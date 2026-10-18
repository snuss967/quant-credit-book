export const meta = {
  name: 'ed2-chapter-pipeline',
  description: 'Configurable per-chapter Edition 2 pipeline: U1 code explanations, U4 figures + figure check, U2 Fable brief + Opus revision + Sonnet verify (stages chosen by args.stages)',
  phases: [
    { title: 'Explain code', detail: 'Sonnet: replace EXPLAIN stubs with prose (U1)', model: 'sonnet' },
    { title: 'Figures', detail: 'Sonnet: 3-5 house-style figures per chapter (U4)', model: 'sonnet' },
    { title: 'Figure check', detail: 'Sonnet: view every figure, check math, caption, legibility', model: 'sonnet' },
    { title: 'Brief', detail: 'Fable: revision brief per chapter', model: 'fable' },
    { title: 'Revise', detail: 'Opus: narrative revision per the brief (U2)' },
    { title: 'Verify', detail: 'Sonnet: nothing removed, new facts checked, hygiene', model: 'sonnet' },
  ],
}
const ROOT = '/home/user/quant-credit-book'
const MARK = '<!-- STATUS: COMPLETE -->'
const VOICE = `VOICE (Edition 2 user directives; these outrank older guidance and the reviews): read "## 8. Edition 2 Voice Amendments" in state/style_bible.md and state/user_directives_ed2.md, and follow them. Teach the way an engaging novel teaches: lead with scenes and real credit events, build intuition before formulas, and be less prescriptive (fewer bare statements and imperatives; more "here is what happened, and here is the idea that would have helped"; more judgment about when a tool applies and when it breaks). Put a "> **Math, Gently.**" box at the first use of each mathematical concept, building blocks included. Add "> **View From Another Seat.**" boxes where another kind of investor or dealer would see the situation differently (name real firms only for publicly stated views, with a citation). Include a labeled fictional quant-shop-life vignette, and the boring parts are welcome. The user's own verdict on Edition 1 is "a lot of prescriptiveness and not narrative": turn rules, imperatives, "should/must/always/never" sentences, and bullet lists into scenes, worked stories, and reasoning the reader watches unfold; let a character discover the rule the hard way instead of stating it. Keep modal and imperative density low (python3 tools/prescriptiveness.py measures it). Remove no topics.
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

const STAGES = {
  u1: { make: u1, phase: 'Explain code', model: 'sonnet' },
  figures: { make: figures, phase: 'Figures', model: 'sonnet' },
  figcheck: { make: figcheck, phase: 'Figure check', model: 'sonnet' },
  brief: { make: brief, phase: 'Brief', model: 'fable', effort: 'high' },
  revise: { make: revise, phase: 'Revise' },
  verify: { make: verify, phase: 'Verify', model: 'sonnet' },
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
