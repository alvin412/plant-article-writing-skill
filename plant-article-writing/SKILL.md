---
name: plant-article-writing
description: Complete publication-ready plant-science manuscript and review workflow with mandatory outline approval, literature search, bilingual full-paper close reading, claim-level citation verification, plant-domain drafting, systematic-review support, multi-perspective peer review, revision and re-review, figure/data/submission checks, and three visually verified Word deliverables. Use for full or partial plant biology and crop-science papers, reviews, perspectives, revisions, rebuttals, citation audits, and journal-ready bilingual manuscripts involving plant stress, immunity, development, genomics, GWAS/QTL/eQTL, pangenomes, single-cell or spatial omics, signalling, transcription factors, yield, adaptation, breeding, and related fields. For every new full manuscript or review, first produce a detailed topic-specific outline and wait for explicit approval before drafting.
---

# Plant Article Writing

## Core Contract

Produce publication-ready plant-science writing without inventing results, methods, statistics, references, mechanisms, novelty, or limitations.

For every new full manuscript, review, perspective, or systematic review:

1. Create a detailed topic-specific outline.
2. Wait for explicit user approval.
3. Build the literature and evidence foundation.
4. Draft section by section.
5. Run blocking integrity, review, revision, citation, and format gates.
6. Deliver three visually verified Word files only after all blocking gates pass.

For a single-section polish or short rewrite, return polished English followed by academic Chinese unless the user requests one language. Do not generate the three-file package unless completing a full manuscript or review project.

## Required References

Load only the files needed for the current phase:

- Full project, planning, drafting, revision, or finalization: `references/plant-full-manuscript-workflow.md`
- Plant review or perspective: `references/plant-review-writing.md`
- Plant stress, gene-family, pathway, regulator, hormone, ncRNA, epigenetic, or signalling review storyline design: also load `references/plant-stress-review-storyline.md`
- Narrative, scoping, or systematic review search and screening: `references/systematic-review-and-search.md`
- Integrity gates, multi-reviewer assessment, revision, or re-review: `references/quality-gates-and-peer-review.md`
- Literature reading, claim-citation mapping, citation verification, or source excerpts: `references/citation-and-close-reading-audit.md`
- Figures, tables, data/code availability, declarations, or submission package: `references/submission-figures-and-data.md`
- Word generation, document hierarchy, file naming, and render QA: `references/word-deliverables.md`

When creating or editing `.docx`, also load the available `documents` skill and follow its render-inspect-revise gate.

## Project Modes

Choose the narrowest mode that covers the request:

- `full-research`: complete original research manuscript.
- `full-review`: narrative or perspective review.
- `systematic-review`: reproducible search, screening, evidence appraisal, and synthesis.
- `outline`: detailed outline and evidence plan only.
- `section`: draft or rebuild one manuscript section.
- `polish`: structural and language revision of supplied text.
- `citation-audit`: claim-level support and metadata audit.
- `peer-review`: plant-domain mock review without rewriting the manuscript.
- `revision-response`: revised manuscript plus point-by-point response.
- `finalize`: final integrity, submission sections, formatting, and three Word deliverables.

## Blocking Workflow

Use this state sequence for complete projects:

`INTAKE -> OUTLINE_APPROVAL -> CORPUS -> EVIDENCE_MAP -> DRAFT -> INTEGRITY_1 -> PEER_REVIEW -> REVISION -> RE_REVIEW -> INTEGRITY_2 -> WORD_QA -> DELIVERED`

Do not skip the following gates:

1. **Outline approval**: no body drafting before explicit approval.
2. **Corpus readiness**: major Introduction, review, and Discussion claims require mapped sources.
3. **Integrity 1**: no peer review while references, data, or major claims remain fabricated, unresolved, or internally inconsistent.
4. **Peer review**: critical scientific or methodological issues block finalization.
5. **Re-review**: every reviewer concern must be verified against the revised manuscript.
6. **Integrity 2**: repeat citation, claim, data, terminology, and completeness checks from scratch.
7. **Word QA**: reopen all files, audit heading hierarchy and formatting, render every page, inspect every page, fix, and re-render.

Classify gate results as:

- `PASS`: all blocking requirements satisfied.
- `WARN`: usable, but a documented limitation remains.
- `BLOCK`: do not advance or deliver.

## Scientific Writing Rules

Write from:

`claim -> evidence -> plant context -> boundary -> significance`

Maintain plant-specific precision:

- Name the species, genotype, tissue, cell type, developmental stage, treatment, stress, environment, and trait when they affect interpretation.
- Distinguish association, prioritization, necessity, sufficiency, biochemical interaction, physiological function, field validation, and breeding value.
- Use `candidate gene` or `strong candidate` until causal evidence supports stronger language.
- Keep Results observation-led and Discussion interpretation-led.
- Group review evidence by mechanism, scale, method, evidence strength, disagreement, or translation boundary rather than by author chronology.
- For plant stress reviews, build an explicit progression from field pressure and object definition through stress functions, mechanism, network integration, a unified model, application, and testable future directions. Treat this as an argument chain, not a mandatory table of contents.
- Preserve stable terminology for genes, proteins, alleles, haplotypes, accessions, cell types, treatments, traits, abbreviations, units, and statistical notation.

Use British spelling for Nature-leaning prose unless the target journal requires US spelling. Avoid unsupported `first`, `novel`, `breakthrough`, `master regulator`, `comprehensive`, and universal claims.

## Evidence and Search Rules

Before drafting Introduction, review-body sections, or Discussion:

1. Build a literature matrix and claim-evidence map.
2. Search when support is missing, outdated, indirect, or mismatched to the plant context.
3. Search multiple reliable sources, deduplicate by DOI then title/author, and verify metadata.
4. Read each nontrivial cited paper closely enough to assess the exact claim.
5. Grade support as `strong`, `partial`, `background`, `contradictory`, `metadata-only`, or `not-supported`.
6. Never cite a metadata-only record as evidence.

Maintain verified reference-manager records and export `.bib`, `.ris`, `.enw`, or Zotero-compatible metadata when requested. Apply the target journal's reference style only after metadata and claim support are verified.

For each cited paper, create full-paper close-reading notes covering all substantive sections. Preserve source anchors and figure/table context. Include exact source excerpts only for the specific manuscript claims they support, with academic Chinese translation and location anchors. Do not reproduce full copyrighted articles; use complete analytical notes plus short lawful excerpts unless the source is user-provided, licensed, or open access.

## Review and Revision Rules

Use independent reviewer perspectives:

1. Plant journal editor: fit, novelty, significance, readership.
2. Plant-domain reviewer: biological accuracy, literature, mechanism, crop context.
3. Methods/statistics reviewer: design, replication, analysis, reproducibility.
4. Genetics/omics/breeding reviewer when relevant: population design, omics inference, validation, translation.
5. Devil's advocate: alternative explanations, overclaiming, cherry-picking, and decisive rejection risks.

Each issue must include severity, manuscript location, evidence, requested action, and verification criterion. During revision, preserve every comment ID and record:

`reviewer comment -> author response -> manuscript change -> location -> verification -> status`

Do not automatically agree with incorrect reviewer requests. Use a respectful, evidence-based disagreement when necessary.

## Final Three-File Deliverable

After a complete project passes all gates, create exactly these Word files:

1. `01_plant_manuscript_bilingual.docx`
   - Full English manuscript.
   - Full academic Chinese manuscript.
   - Title, hierarchical headings, figures/tables/legends when available, references, and required submission statements.

2. `02_peer_review_and_response.docx`
   - Editorial synthesis.
   - Independent reviewer reports.
   - Point-by-point responses.
   - Exact manuscript changes and locations.
   - Re-review verification and final disposition of every comment.

3. `03_literature_audit_and_close_reading.docx`
   - Search and screening record.
   - Literature matrix and claim-citation audit.
   - Full-paper bilingual close-reading notes for every cited source.
   - For every manuscript citation, the supporting original excerpt, academic Chinese translation, source anchor, support grade, and boundary.
   - Metadata, DOI/PMID/URL, correction/retraction notes, and unresolved risks.

Use `scripts/build_word_package.py` with the structured project JSON described in `references/word-deliverables.md`, or create equivalent documents with the `documents` skill. The three files must have visible titles and real Word Heading 1/2/3 hierarchy.

Optional LaTeX, PDF, BibTeX, RIS, or journal-submission sidecars may be created when requested, but they do not replace the three required Word files.

## Final Release Gate

Before delivery, confirm:

- No unresolved `BLOCK` issue.
- All in-text citations and references match.
- Every material external claim has verified support.
- Source excerpts support the cited manuscript sentence without scope drift.
- English and Chinese versions preserve the same claim strength and content.
- Reviewer comments, responses, changes, and re-review results are complete.
- Figures, tables, captions, and callouts are consistent.
- Data/code/materials availability and submission declarations are present when applicable.
- Word titles, heading levels, numbering, tables, page breaks, fonts, spacing, headers/footers, and references are consistent.
- All three `.docx` files reopen successfully.
- Every page has been rendered and visually inspected; no clipping, overlap, broken table, missing glyph, orphan heading, or incoherent page break remains.

If rendering is impossible because the required renderer is unavailable, perform structural validation, mark visual QA as not completed, and do not claim that the files passed the full release gate.
