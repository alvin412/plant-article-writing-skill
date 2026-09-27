# Full manuscript workflow

Use only for a complete manuscript or full package. Read `research-workflow.md` for scientific structure, `quality-and-deliverables.md` for review and audits, and `journal-finalization-checklist.md` for submission preparation. These are workflow requirements, not extra deliverables for a scoped edit.

## Core Contract

Never invent experimental materials, methods, sample sizes, controls, replicates, values, statistics, figures, accession numbers, results, mechanisms, novelty, or limitations. Mark missing author inputs explicitly and block claims that cannot be supported.

For a new full research article:

1. Inventory the supplied data, analyses, figures, tables, methods, and literature.
2. Create a detailed article outline and evidence or result plan.
3. For a new full manuscript, obtain outline approval unless the outline is already approved or the user has authorized direct continuation. Do not repeat this gate.
4. After approval, continue automatically through the remaining workflow unless essential data, source material, external-write authorization, or a material scientific decision is missing.

## Required Manuscript Structure

Produce, at minimum:

1. Title
2. Abstract
3. Keywords
4. Introduction
5. Materials and Methods
6. Results and Analysis
7. Discussion
8. Conclusion

Add references, figure and table legends, data and code availability, author contributions, funding, conflicts, ethics, acknowledgements, supplementary information, and other submission statements when applicable.

## Workflow

Use:

`INTAKE -> OUTLINE_APPROVAL -> DATA_AND_CORPUS -> EVIDENCE_MAP -> DRAFT -> POLISH -> INTEGRITY_AUDIT -> PEER_REVIEW -> REVISION_RESPONSE -> RE_REVIEW -> FINAL_AUDIT -> JOURNAL_FINALIZATION -> WORD_QA -> DELIVERED`

Draft Results and Analysis from verified user evidence before interpreting it. Keep Results observation-led and Discussion interpretation-led.

For Results writing, follow `results-writing-frame.md`.

After drafting, automatically perform:

1. Structural and language polishing of the English and Chinese manuscripts.
2. Cross-checking of values, figures, tables, methods, statistics, terminology, and language alignment.
3. Claim-level verification that every material external assertion is truly supported by its citation.
4. Independent editorial, plant-domain, methods and statistics, relevant genetics or omics or breeding, and devil's-advocate review.
5. Manuscript revision, point-by-point response, and exact change tracking.
6. Re-review of every claimed change and a final integrity pass that reuses valid evidence records and rechecks changed claims and dependencies.
7. Freeze the revised manuscript version; obtain the exact target journal, article type, current official instructions, template, and reference style; and build a source-backed requirement matrix.
8. Apply the journal requirements, reference style, nomenclature and typography rules, English-language finalization, figure and table rules, declarations, anonymization, and file conventions to the complete English research article inside `01_plant_article_bilingual.docx`. Keep the complete academic-Chinese article after it; do not create a separate English manuscript deliverable.
9. Create a bilingual journal-compliance audit that records every material change, requirement status, unresolved item, visual-QA state, and submission-readiness decision.
10. Generate the selected final Word files and visually inspect every page of a newly created full manuscript package. Correct observed defects and inspect changed or reflowed pages; repeat a full visual pass only when changes affect the entire layout or the affected range is uncertain.

## Required Final Files

For full-manuscript mode, create the following four final Word files under `deliverables/` unless the user requests a different delivery scope:

1. `01_plant_article_bilingual.docx` — complete target-journal-finalized English research article followed by the complete academic-Chinese article. The English portion must be the frozen, compliance-audited manuscript; the Chinese portion is retained for author use and is not a separate journal submission file.
2. `02_claim_citation_audit_bilingual.docx` — data-consistency summary, claim-citation matrix, source anchors, support grades, boundaries, and unresolved risks.
3. `03_peer_review_and_response_bilingual.docx` — editorial synthesis, independent review reports, point-by-point responses, exact changes and locations, and re-review verification.
4. `04_journal_compliance_audit_bilingual.docx` — official requirement matrix, reference and nomenclature audit, English and structural changes, figure/table/declaration checks, unresolved `WARN` or `BLOCK` items, visual-QA status, and bilingual submission-readiness decision.

Do not create `01_journal_formatted_manuscript_en.docx`; its content is the English portion of `01_plant_article_bilingual.docx`.

Place every other artifact under `intermediate_files/`, including configurations, approved outlines, datasets or derived summaries, search records, literature notes, evidence maps, draft versions, reviewer working files, journal instructions, templates, extracted requirements, reference exports, terminology ledgers, structured Word inputs, validation reports, and rendered page images.

Use the available `documents:documents` skill for Word creation and render-inspect-revise QA. `../scripts/build_article_package.py` may build the four files from verified structured JSON; it must never fill missing scientific content or claim that its generic styles satisfy a journal template without subsequent journal-specific editing and visual QA.
