export const meta = {
  name: 'ed2-u1-code-explanations',
  description: 'Edition 2 U1: Sonnet replaces every EXPLAIN code stub in a lane of chapters with a plain-language explanation linked to Appendix F',
  phases: [{ title: 'Explain code', detail: 'Sonnet, one agent per file', model: 'sonnet' }],
}
const ROOT = '/home/user/quant-credit-book'
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
return await pipeline(args.stems, stem => agent(u1(stem), { label: `u1:${stem}`, phase: 'Explain code', model: 'sonnet' }).then(r => ({ stem, r })))
