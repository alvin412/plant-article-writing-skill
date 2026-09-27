# Research Integrity, Review, and Four-File Delivery

## Scope of this reference

The complete review cycle, journal finalization, and four-file layout apply to full-manuscript/full-package mode. For a partial edit, verify changed claims and affected consistency only; for a citation audit, check the specified claims; for journal-only work, deliver the requested manuscript and compliance findings. Preserve all scientific integrity standards, but do not block a scoped deliverable because unrelated full-package inputs are absent. A missing or failed check prevents claiming that check passed; report its scope and continue unaffected work.

## Blocking Integrity Checks

Audit independently:

1. Bibliographic identity and publication status.
2. Exact claim-citation alignment and plant-context match.
3. Values, directions, sample sizes, replicates, tests, corrections, effect sizes, uncertainty, and figure or table consistency.
4. Materials, growth conditions, treatments, sampling, controls, assays, software, versions, thresholds, and reproducibility.
5. Agreement among Abstract, Results, Discussion, Conclusion, figures, tables, supplement, and Chinese version.
6. Terminology, gene and protein typography, originality, and absence of fabricated content.

Use `PASS`, `WARN`, and `BLOCK`. Fabricated or unverifiable content, missing reproducibility-critical methods, materially unsupported claims, causal inflation, internal inconsistency, unresolved critical reviewer issues, unverified target-journal requirements at the finalization stage, or failed Word QA block a verified/final verdict for the affected content; complete and deliver unaffected requested work with the remaining limitation stated.

## Claim-Citation Audit

Assign stable claim IDs. For every material external claim, record the manuscript sentence and location, exact source, source anchor, short passage, Chinese translation, matched entities and conditions, support grade, scope boundary, and decision. Use `reading-literature` in targeted verification mode; reuse matching verified evidence records. Metadata-only records cannot serve as substantive evidence.

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

Never claim a change unless it exists. Respectfully disagree with an incorrect request when evidence supports disagreement. Re-review every issue in scope and inspect revisions for new risks. In full mode perform a final manuscript-wide integrity pass, reusing still-valid records and rechecking changed claims and dependencies; partial tasks require only the affected checks.

## Integrated Journal Finalization

Freeze the exact revised manuscript before journal finalization. Use current official instructions for the exact journal and article type. Apply the resulting requirements to the complete English portion of `01_plant_article_bilingual.docx`; retain the complete academic-Chinese research article after it. Do not create a separate English manuscript deliverable.

Record requirement sources, compliance decisions, material changes, unresolved items, and submission readiness in `04_journal_compliance_audit_bilingual.docx`. A missing journal, uncertain article type, unavailable authoritative instructions, unresolved blocking requirement, or incomplete visual QA prevents a submission-ready decision.

## Project Layout

```text
project/
  deliverables/
    01_plant_article_bilingual.docx
    02_claim_citation_audit_bilingual.docx
    03_peer_review_and_response_bilingual.docx
    04_journal_compliance_audit_bilingual.docx
  intermediate_files/
    configuration/
    outlines/
    data_summaries/
    searches/
    literature_notes/
    evidence_maps/
    drafts/
    review_working/
    journal_requirements/
    reference_exports/
    terminology/
    word_inputs/
    validation/
    rendered_pages/
```

For the default full-manuscript package, the four named Word files are final deliverables and other artifacts belong under `intermediate_files/`. Scoped modes deliver only their requested outputs.

## Word QA

Load `documents:documents` for Word work. Preserve required journal styles and check content completeness, hierarchy, cross-references, tables, and figures. Render and inspect all pages for a new package or broad layout change; for later localized changes, inspect changed/reflowed pages against the verified baseline and broaden if impact is uncertain. Correct observed defects and verify the affected pages again. If rendering is unavailable, disclose that visual QA remains incomplete.
