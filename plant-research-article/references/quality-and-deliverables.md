# Research Integrity, Review, and Three-File Delivery

## Blocking Integrity Checks

Audit independently:

1. Bibliographic identity and publication status.
2. Exact claim-citation alignment and plant-context match.
3. Values, directions, sample sizes, replicates, tests, corrections, effect sizes, uncertainty, and figure or table consistency.
4. Materials, growth conditions, treatments, sampling, controls, assays, software, versions, thresholds, and reproducibility.
5. Agreement among Abstract, Results, Discussion, Conclusion, figures, tables, supplement, and Chinese version.
6. Terminology, gene and protein typography, originality, and absence of fabricated content.

Use `PASS`, `WARN`, and `BLOCK`. Fabricated or unverifiable content, missing reproducibility-critical methods, materially unsupported claims, causal inflation, internal inconsistency, unresolved critical reviewer issues, or failed Word QA always block delivery.

## Claim-Citation Audit

Assign stable claim IDs. For every material external claim, record the manuscript sentence and location, exact source, source anchor, short passage, Chinese translation, matched entities and conditions, support grade, scope boundary, and decision. Use `reading-literature`; metadata-only records cannot serve as substantive evidence.

## Independent Review

Use separate reports:

1. Editor: fit, significance, readership, coherence, and desk-reject risk.
2. Plant-domain reviewer: biological accuracy, mechanism, crop context, and literature.
3. Methods and statistics reviewer: design, controls, replication, analysis, assumptions, and reproducibility.
4. Genetics, omics, or breeding reviewer when relevant.
5. Devil's advocate: strongest alternative explanation, cherry-picking, overclaiming, missing decisive control, contradictory evidence, and rejection risk.

Every issue requires an ID, severity, location, problem, rationale, required action, and verification criterion.

## Revision Traceability

Record:

`comment -> decision -> author response -> manuscript change -> location -> evidence added -> re-review verification -> status`

Never claim a change unless it exists. Respectfully disagree with an incorrect request when evidence supports disagreement. Re-review every issue, inspect revisions for new risks, and repeat the integrity audit from scratch.

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
    data_summaries/
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

Load the `docx` skill. Use real Word Title and Heading 1/2/3 styles. Reopen every file, validate section completeness, hierarchy, cross-references, tables and figures, render every page, visually inspect every page, correct all defects, and re-render. If rendering is unavailable, report that visual QA did not pass.
