export const meta = {
  name: 'ed2-appz-complete',
  description: 'Finish App Z: worked, numerically checked solutions for the primers, new chapters and appendices (then a per-chapter number-fix pass), the 4-D sixty-problem bank, and the eight Part gates (table in each Part opener plus worked answers)',
  phases: [
    { title: 'Solve', detail: 'Sonnet: one agent per chapter, numbers checked in python', model: 'sonnet' },
    { title: 'Fix', detail: 'Sonnet: resolve each editor NOTE in the chapter', model: 'sonnet' },
    { title: 'Gates', detail: 'Sonnet: one agent per Part', model: 'sonnet' },
  ],
}
const ROOT = '/home/user/quant-credit-book'
const MARK = '<!-- STATUS: COMPLETE -->'
const BOOK = `the book in ${ROOT} ("Systematic & Quantitative Credit: From PJT RSSG to the Automated Desk"; reader: a restructuring banker moving to a systematic credit desk)`
const FORMAT = tag => `For EACH exercise or problem, write:
- **Z.${tag}.k: the exercise's short title** (with its [Read]/[Derive]/[Build] tag if it has one), k counting from 1 in the chapter's own order;
- **Answer:** the numbers or the result, stated first;
- **How:** the method in 3–10 lines of prose and LaTeX (the steps that matter; no code blocks, but name the Appendix F listing if a [Build] exercise extends one);
- **The trap:** the most common wrong answer and why it is wrong;
- **If you got this wrong, read:** the § that builds the idea (check that the § exists with grep -n "^#").
State the measure (physical or risk-neutral) and the units whenever either could be in doubt. Check every numerical answer by computing it yourself in python3 (throwaway scripts under /tmp only, never in the repo). Where the chapter's own text, inline solution, check value, listing output or figure caption disagrees with your computation, write a separate paragraph starting "NOTE (for the editor):" giving both numbers; do not edit the chapter.
Voice: warm and direct, like a good TA; brief. Pandoc math: $...$ inline and $$...$$ display on their own lines. Escape currency as \\$.`
const solve = c => `You are a SOLUTIONS AUTHOR for Appendix Z of ${BOOK}. Work from ${ROOT}.
Source: book_src/${c.stem}.md (label ${c.tag}). Output: state/appZ/${c.stem}.md.
FIRST: if the output ends with ${MARK}, stop and return "done". If it exists, resume after the last finished solution. Otherwise create it (mkdir -p state/appZ) with the heading line "## Z.${c.tag} ${c.kind} ${c.tag}: <the title from the file's first # heading>" and one short paragraph saying how many exercises there are and anything unusual about them.
Find the exercises: grep -n -i "exercise" and read that section, plus any exercises embedded elsewhere. This file already prints brief solutions next to its exercises; App Z gives the worked version. Do not copy the brief solution: verify it, then write the full one, and if the brief one is wrong, say so in a NOTE.
${FORMAT(c.tag)}
Append each solution as you finish it (durability). Your FINAL action is appending a line containing exactly ${MARK}. Return a 30-word summary with the exercise count and the NOTE count.`
const solve4d = part => `You are a SOLUTIONS AUTHOR for Appendix Z of ${BOOK}. Work from ${ROOT}.
Source: book_src/04_ch04d_getting_the_seat.md (label 4-D). Its §4D.12 "Sixty Tagged Problems" says "Solutions are in Appendix Z", and this is that promise. Output: state/appZ/04_ch04d_getting_the_seat.md.
${part === 1
    ? `You do problems 1–30. FIRST: if the output contains the line <!-- Z4D PART 1 COMPLETE -->, stop and return "done". If it exists, resume after the last finished problem. Otherwise create it with the heading line "## Z.4-D Chapter 4-D: <the title from the file's first # heading>", one short paragraph on how to use the bank (do the problem cold, time yourself against the stated minutes, then read), and the line "**The problem bank (§4D.12)**".`
    : `You do problems 31–60, then the end-of-chapter Exercises (the "### Exercises" section near the Desk Debrief). FIRST: if the output ends with ${MARK}, stop and return "done". The file must already contain <!-- Z4D PART 1 COMPLETE -->; if it does not, stop and return "part 1 missing". Resume after the last finished item. Before the chapter exercises, add the line "**The chapter exercises**" and number them Z.4-D.E1, E2, ….`}
Read §4D.12 (grep -n "4D.12" then sed the range) and, for each problem, the home section it names.
${FORMAT('4-D')} Number the bank problems Z.4-D.P1 … P60 to match the chapter's numbering. Problems tagged [Build] get a short description of the function, its tests and the expected output, not a code listing. Keep each solution tight: the bank is sixty items, so 80–200 words each.
Append each solution as you finish it. Your FINAL action is appending a line containing exactly ${part === 1 ? '<!-- Z4D PART 1 COMPLETE -->' : MARK}. Return a 30-word summary.`
const fix = stem => `You are a NUMBERS EDITOR for ${BOOK}. Work from ${ROOT}.
Chapter: book_src/${stem}.md. Its worked solutions: state/appZ/${stem}.md. Log: state/revisions/ed2/${stem}.appz_fix.md.
FIRST: if the log ends with ${MARK}, stop and return "done". If it exists, skip the notes it already rules on. If grep -c "NOTE (for the editor)" state/appZ/${stem}.md is 0, write the log with one line "No editor notes." and ${MARK}, and return "none".
The App Z author left paragraphs starting "NOTE (for the editor):" wherever the chapter's text, inline solution, check value, listing output or figure caption disagrees with a careful computation. For each, in order:
1. Read the note, the exercise, and the section it cites (grep -n, then sed -n the range). If it concerns an Appendix F listing, read it in book_src/95_appF_code_companion.md.
2. Recompute the disputed number yourself in python3 (throwaway scripts under /tmp only) and decide which is right. Most notes are right, but not all: rule on the evidence.
3. If the chapter is wrong or misleading, make the SMALLEST edit that makes it right (a number, a clause, a caption, an inline solution, a check value), in the chapter's voice. If a figure script (tools/figures/*.py) draws the wrong number, fix it and re-run it. If the fix needs a sourced fact you cannot verify from files in the repo, soften the claim to what the sources in state/research/ support instead of inventing a number.
4. Make the solution agree with the fixed chapter (edit its text if it quoted the old value), then DELETE the NOTE paragraph from state/appZ/${stem}.md. If you rule the note wrong, delete it too and keep the solution correct.
5. Append to the log: the note in one line, your recomputation, the ruling (fixed / note wrong / softened), and the exact old → new text.
Never rewrite prose beyond the fix, never change a story beat, never remove a topic. Your FINAL action is appending a line containing exactly ${MARK} to the log. Return a 30-word summary: notes handled, fixed, ruled wrong.`
const gate = g => `You are the GATE AUTHOR for ${g.roman} of ${BOOK}. Work from ${ROOT}.
Part opener: book_src/${g.opener}.md. Chapters in this Part: ${g.stems.join(', ')}. Answers file: state/appZ/gates/${g.opener}.md.
FIRST: if the answers file ends with ${MARK}, stop and return "done". If it exists, resume.
Background: book_src/00_02_how_to_use_this_book.md §0.5 "The Gates" (grep -n "0.5 The Gates", then read about 60 lines) promises that each Part opener closes with ten things the reader can do on leaving the Part, each naming the section that builds it and the check, and that Appendix Z holds the worked answers. It prints the Part II gate in full as the model, and a one-line summary of the other seven. A gate is a markout, not a quiz: the reader writes the number down before looking.
1. Design this Part's gate: ten items, in the Part's teaching order, each a concrete skill with a checkable result (a number with a tolerance, a sign, a named failure). ${g.roman === 'Part II' ? 'For Part II, use the ten items printed in §0.5 exactly as they are.' : `Start from the items in §0.5's one-line summary for this Part and keep all of them; add items from the Part's chapters (read each chapter's headings and Desk Debrief: grep -n "^#" and the Debrief section) so that every chapter in the Part, the new ones included, owns at least one item.`} Every "Built in" § must exist (grep -n "^#" in the chapter). Prefer skills an exercise in the chapter already tests, and name the exercise where one does.
2. Before the final ${MARK} line of book_src/${g.opener}.md, insert (one Edit): a heading "## The Gate: Before You Leave ${g.roman}, You Can…", one or two sentences in the book's voice saying how to use it, the table | # | Before you leave ${g.roman}, you can… | Built in | The check |, and the line "Worked answers: Appendix Z, Gate ${g.short}." If the opener already has a gate, stop and return "exists".
3. Write the answers file: the heading "### Gate ${g.short}: Before You Leave ${g.roman}", then for each item "**G${g.short}.k: <the skill, short>**" with **Answer:** (the number first), **How:** (3–8 lines, LaTeX where it helps), **The trap:**, and **If you got this wrong, read:** §. Recompute every number in python3 (throwaway scripts under /tmp). If a chapter's own number disagrees with yours, add a paragraph starting "NOTE (for the editor):" with both numbers; do not edit the chapter.
${g.roman === 'Part II' ? '' : `4. If your ten items change what the §0.5 one-line summary for this Part says, update ONLY that one row of the §0.5 summary table in 00_02 (one Edit, matching it exactly) so it stays true; other agents are editing other rows.`}
Pandoc math: $...$ inline and $$...$$ display on their own lines. Escape currency as \\$. Your FINAL action is appending a line containing exactly ${MARK} to the answers file. Return a 30-word summary.`

const chapters = args.chapters || []
const runChapters = pipeline(chapters,
  c => agent(solve(c), { label: `solve:${c.tag}`, phase: 'Solve', model: 'sonnet' }),
  (r, c) => agent(fix(c.stem), { label: `fix:${c.tag}`, phase: 'Fix', model: 'sonnet' }).then(f => ({ stem: c.stem, solve: r, fix: f })))
const run4d = args.do4d === false ? Promise.resolve(null) : (async () => {
  const a = await agent(solve4d(1), { label: 'solve:4-D P1-30', phase: 'Solve', model: 'sonnet' })
  const b = await agent(solve4d(2), { label: 'solve:4-D P31-60', phase: 'Solve', model: 'sonnet' })
  const f = await agent(fix('04_ch04d_getting_the_seat'), { label: 'fix:4-D', phase: 'Fix', model: 'sonnet' })
  return { stem: '04_ch04d_getting_the_seat', a, b, f }
})()
const runGates = pipeline(args.gates || [], g => agent(gate(g), { label: `gate:${g.short}`, phase: 'Gates', model: 'sonnet' }).then(r => ({ part: g.opener, r })))
const [ch, d4, gates] = await Promise.all([runChapters, run4d, runGates])
return { chapters: ch, d4, gates }
