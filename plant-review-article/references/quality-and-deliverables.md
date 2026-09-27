# Quality Gates and Four-File Delivery

## Scope of this reference

The complete review cycle, journal finalization, and four-file layout apply to full-manuscript/full-package mode. For a partial edit, verify changed claims and affected consistency only; for a citation audit, check the specified claims; for journal-only work, deliver the requested manuscript and compliance findings. Preserve all scientific integrity standards, but do not block a scoped deliverable because unrelated full-package inputs are absent. A missing or failed check prevents claiming that check passed; report its scope and continue unaffected work.

## Gate Model

- `PASS`: no blocking defect.
- `WARN`: a non-blocking limitation is explicitly disclosed.
- `BLOCK`: do not present the affected claim or artifact as verified/final until corrected, removed, or resolved; continue independent authorized work.

Always block fabricated or unverifiable content, a materially wrong claim-citation relationship, unsupported causal language, internal inconsistency, unresolved critical review issues, unverified target-journal requirements at the finalization stage, or a final Word file that fails structural or visual QA.

## Claim and Citation Audit

Assign stable claim IDs. For every citation occurrence record the manuscript sentence and location, source, exact anchor, short supporting passage, Chinese translation, matched entities and conditions, support grade, mismatch or scope drift, evidence type, and audit decision.

Use `reading-literature` targeted verification for nontrivial source claims, reusing records whose source version and scope still match. `metadata-only` and `not-supported` cannot remain as final evidence.

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

Do not automatically accept an incorrect request; disagree respectfully with evidence. Verify every claimed change against the revised manuscript. Then inspect for new risks introduced by revision. For full mode, run a final manuscript-wide integrity pass, reusing still-valid verified records; recheck changed claims and affected relationships. For partial mode, restrict re-review to the changed text and its dependencies.

## Integrated Journal Finalization

Freeze the exact revised manuscript before journal finalization. Use current official instructions for the exact journal and article type. Apply the resulting requirements to the complete English portion of `01_plant_article_bilingual.docx`; retain the complete academic-Chinese review after it. Do not create a separate English manuscript deliverable.

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
