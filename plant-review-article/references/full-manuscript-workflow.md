# Full manuscript workflow

Use only for a complete manuscript or full package. Read `review-workflow.md` for scientific structure, `quality-and-deliverables.md` for review and audits, and `journal-finalization-checklist.md` for submission preparation. These are workflow requirements, not extra deliverables for a scoped edit.

## Core Contract

Do not invent results, mechanisms, statistics, references, novelty, limitations, or source passages. Match every claim to its evidence and plant context.

For a new full review:

1. Create a detailed topic-specific outline and evidence plan.
2. For a new full manuscript, obtain outline approval unless the outline is already approved or the user has authorized direct continuation. Do not repeat this gate.
3. After approval, continue automatically through the remaining workflow unless essential source material, user data, external-write authorization, or a material scientific decision is missing.

## Workflow

Use:

`INTAKE -> OUTLINE_APPROVAL -> CORPUS -> CLOSE_READING -> EVIDENCE_MAP -> DRAFT -> POLISH -> CITATION_AUDIT -> PEER_REVIEW -> REVISION_RESPONSE -> RE_REVIEW -> FINAL_AUDIT -> JOURNAL_FINALIZATION -> WORD_QA -> DELIVERED`

The completed review must synthesize evidence by mechanism, scale, method, evidence strength, disagreement, or translation boundary rather than list papers chronologically.

After drafting, perform these steps without requiring separate user prompts:

1. Structural and language polishing of both manuscript languages.
2. Claim-level verification that every material external assertion is truly supported.
3. Independent editorial, plant-domain, methods, relevant omics or breeding, and devil's-advocate review.
4. Manuscript revision and a preserved point-by-point response for every review issue.
5. Re-review of every claimed change and a final integrity pass that reuses valid evidence records and rechecks changed claims and dependencies.
6. Freeze the revised manuscript version; obtain the exact target journal, article type, current official instructions, template, and reference style; and build a source-backed requirement matrix.
7. Apply the journal requirements, reference style, nomenclature and typography rules, English-language finalization, figure and table rules, declarations, anonymization, and file conventions to the complete English review inside `01_plant_article_bilingual.docx`. Keep the complete academic-Chinese review after it; do not create a separate English manuscript deliverable.
8. Create a bilingual journal-compliance audit that records every material change, requirement status, unresolved item, visual-QA state, and submission-readiness decision.
9. Generate the selected final Word files and visually inspect every page of a newly created full manuscript package. Correct observed defects and inspect changed or reflowed pages; repeat a full visual pass only when changes affect the entire layout or the affected range is uncertain.

## Required Final Files

For full-manuscript mode, create the following four final Word files under `deliverables/` unless the user requests a different delivery scope:

1. `01_plant_article_bilingual.docx` — complete target-journal-finalized English review followed by the complete academic-Chinese review. The English portion must be the frozen, compliance-audited manuscript; the Chinese portion is retained for author use and is not a separate journal submission file.
2. `02_claim_citation_audit_bilingual.docx` — claim-citation matrix, source anchors, support grades, boundaries, unresolved risks, and bilingual explanations.
3. `03_peer_review_and_response_bilingual.docx` — editorial synthesis, independent review reports, point-by-point responses, exact changes and locations, and re-review verification.
4. `04_journal_compliance_audit_bilingual.docx` — official requirement matrix, reference and nomenclature audit, English and structural changes, figure/table/declaration checks, unresolved `WARN` or `BLOCK` items, visual-QA status, and bilingual submission-readiness decision.

Do not create `01_journal_formatted_manuscript_en.docx`; its content is the English portion of `01_plant_article_bilingual.docx`.

Place every other project artifact under `intermediate_files/`, including search records, screening files, literature matrices, close-reading notes, outlines, draft versions, evidence maps, reviewer working files, journal instructions, templates, extracted requirements, reference exports, terminology ledgers, JSON inputs, validation reports, and rendered page images.

Use the available `documents:documents` skill for Word creation and render-inspect-revise QA. `../scripts/build_article_package.py` may build the four files from verified structured JSON; it must never fill missing scientific content or claim that its generic styles satisfy a journal template without subsequent journal-specific editing and visual QA.
