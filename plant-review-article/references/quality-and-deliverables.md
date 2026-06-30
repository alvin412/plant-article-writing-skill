# Quality Gates and Three-File Delivery

## Gate Model

- `PASS`: no blocking defect.
- `WARN`: a non-blocking limitation is explicitly disclosed.
- `BLOCK`: stop until corrected, removed, or resolved by the user.

Always block fabricated or unverifiable content, a materially wrong claim-citation relationship, unsupported causal language, internal inconsistency, unresolved critical review issues, or a final Word file that fails structural or visual QA.

## Claim and Citation Audit

Assign stable claim IDs. For every citation occurrence record the manuscript sentence and location, source, exact anchor, short supporting passage, Chinese translation, matched entities and conditions, support grade, mismatch or scope drift, evidence type, and audit decision.

Use `reading-literature` to verify nontrivial sources. `metadata-only` and `not-supported` cannot remain as final evidence.

## Independent Review

Use separate perspectives:

1. Editor: fit, significance, readership, coherence, and desk-reject risk.
2. Plant-domain reviewer: biology, mechanism, crop context, competing models, and literature.
3. Methods or evidence-synthesis reviewer: search, screening, appraisal, reproducibility, and inferential validity.
4. Genetics, omics, or breeding reviewer when relevant.
5. Devil's advocate: alternative explanations, cherry-picking, overclaiming, missing decisive evidence, and rejection risk.

Each issue must include ID, severity, location, problem, evidence or rationale, required action, and verification criterion.

## Revision and Re-Review

Preserve every issue and record:

`comment -> decision -> author response -> exact manuscript change -> location -> evidence added -> verification -> status`

Do not automatically accept an incorrect request; disagree respectfully with evidence. Verify every claimed change against the revised manuscript. Then inspect for new risks introduced by revision and repeat the full claim, citation, terminology, language-alignment, and completeness audit from scratch.

## Project Layout

```text
project/
  deliverables/
    01_plant_article_bilingual.docx
    02_claim_citation_audit_bilingual.docx
    03_peer_review_and_response_bilingual.docx
  intermediate_files/
    configuration/
    outlines/
    searches/
    literature_notes/
    evidence_maps/
    drafts/
    review_working/
    word_inputs/
    validation/
    rendered_pages/
```

Only the three named Word files are final deliverables. Put all other artifacts under `intermediate_files/`.

## Word QA

Load the `docx` skill. Use real Word Title and Heading 1/2/3 styles. Reopen every file, validate hierarchy and cross-references, render every page, inspect every page, fix clipping, overlap, broken tables, missing glyphs, orphan headings, or incoherent breaks, and re-render. Do not claim visual QA when rendering was unavailable.
