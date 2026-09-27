# Full-Paper Close Reading and Zotero

This reference applies to full-paper note production. Use `claim-verification.md` for targeted checks. Honour the selected outputs and languages from `SKILL.md`; optional maps, domain updates, JIF checks, and Zotero writes do not become mandatory through this reference.

## 1. Source Record

Record:

```text
Citation key:
Title and authors:
Journal and year:
JIF value, edition year, verification source, and status (only if requested or required by an opted-in domain route):
DOI / PMID / PMCID / URL:
Zotero item key:
Article type and publication status:
Access state: full-text / partial-reading / abstract-only / metadata-only
Correction, retraction, or expression-of-concern status:
Plant context:
Intended manuscript claim or project:
Research-mind-map source: supplied / generated
Research-mind-map audit status: verified / corrected / blocked
```

## 2. Research-Mind-Map Record

If a map is among the selected outputs, complete `research-mind-map.md` before drafting the close-reading note; otherwise omit the map record. Record the map title, version date, access completeness, evidence legend, canonical JSON path, intermediate outline path, final PNG path, supplied-map verdict and corrections, claim-evidence anchors, conflicts, and visual-QA state.

Do not treat a visually plausible map as verified. Cross-check species and assay host, perturbation direction, mutant identity, residue number, directness of binding, pathway direction, separate versus combined perturbations, statistics, and every strong causal or novelty term.

## 3. Complete Bilingual Note

By default create one note containing a complete English analytical version followed by a complete academic-Chinese version; use only the requested language when the user specifies one. Do not interleave sentence-by-sentence translations unless needed in an evidence table.

For each substantive section capture:

```text
Section and exact source anchors:
Analytical synthesis:
Key evidence and quantitative direction:
Methods, controls, replicates, and statistics:
Relevant figures, tables, and supplements:
Species, genotype, tissue, stage, treatment, and environment:
Evidence strength and causal boundary:
Limitations, conflicts, and alternative explanations:
Potential manuscript uses:
Field terminology candidates:
Reported research logic:
Clearly labelled inferred ideas:
```

Follow the evidence chain from design and controls to quantitative result. Distinguish demonstrated findings from interpretation, extrapolation, and speculation. If full text is incomplete, label the note `partial-reading` and list unavailable sections. Abstract-only or metadata-only records cannot establish a nontrivial manuscript claim.

Use this note structure in both languages:

```text
Purpose and manuscript use
Bibliographic identity and publication status
Reading completeness and access limits
Analytical summary
Research question, gap, and experimental architecture
Methods, controls, and statistics
Key results with source anchors
Figures, tables, and supplements
Mechanistic interpretation and evidence boundaries
Claim-support decisions
Limitations, internal conflicts, and alternatives
Terminology and expression guidance
Reported research logic and transferable design principles
Inferred research ideas and decisive experiments
Domain-file route and update summary (only when requested)
Unresolved checks
```

## 4. Claim-Citation Audit

Use one record per citation occurrence:

```text
Claim ID:
Manuscript sentence and location:
Cited source:
Claim type:
Exact source anchor:
Short original excerpt:
Academic Chinese translation:
Matched entities and conditions:
Support grade:
Scope mismatch or boundary:
Audit decision: PASS / WARN / BLOCK
```

Grade support as `strong`, `partial`, `background`, `contradictory`, `metadata-only`, or `not-supported`. `metadata-only` and `not-supported` cannot remain as final substantive evidence. If no exact support can be located, block or narrow the claim.

## 5. Local File and Single Zotero Child Note

Always save the canonical local note under `deliverables/` with a Windows-safe filename:

```text
02_Codex_full-paper_close_reading_<YYYY-MM-DD>_<project-or-claim-ID>_bilingual.md
```

When authorized, create one non-destructive Zotero child note attached to the exact bibliographic item:

```text
Codex full-paper close reading | YYYY-MM-DD | project or claim ID
```

Use the same complete content and selected language scope as the local file. Preserve existing notes. Append only when the user identifies the destination note and authorizes appending; otherwise create one new dated child note. Do not create a separate research-mind-map Zotero note.

Use this synchronization order:

1. The most direct reliable Zotero note-write capability available in the active Zotero skill.
2. Zotero Desktop interface control if a direct write capability is unavailable or fails.
3. Local-only delivery marked `NOT_SYNCED_TO_ZOTERO`.

After writing, reopen or list the child note and verify its parent item, title, and substantive content in every selected language. Never claim success from an attempted click, paste, or request alone.
