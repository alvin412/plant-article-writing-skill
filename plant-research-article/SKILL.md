---
name: plant-research-article
description: "Create publication-ready original plant-science and crop-science research manuscripts from user-supplied methods, data, results, analyses, figures, and tables. Use for full or partial experimental, genetics, genomics, omics, physiology, development, immunity, stress, adaptation, yield, or breeding papers. For a new full paper, require detailed outline approval, then continue through bilingual drafting of title, abstract, keywords, introduction, materials and methods, results and analysis, discussion, and conclusion; polishing; claim-citation verification; independent peer review; revision and point-by-point response; and three final Word deliverables while storing all intermediate artifacts in one folder."
---

# Plant Research Article

Read `references/research-workflow.md` for every full manuscript and `references/quality-and-deliverables.md` before integrity review, peer review, revision, or Word generation.

Use `reading-literature` for every substantive cited source. Follow its Zotero confirmation gate whenever close-reading notes may be saved to Zotero.

## Core Contract

Never invent experimental materials, methods, sample sizes, controls, replicates, values, statistics, figures, accession numbers, results, mechanisms, novelty, or limitations. Mark missing author inputs explicitly and block claims that cannot be supported.

For a new full research article:

1. Inventory the supplied data, analyses, figures, tables, methods, and literature.
2. Create a detailed article outline and evidence or result plan.
3. Stop and wait for explicit outline approval.
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

`INTAKE -> OUTLINE_APPROVAL -> DATA_AND_CORPUS -> EVIDENCE_MAP -> DRAFT -> POLISH -> INTEGRITY_AUDIT -> PEER_REVIEW -> REVISION_RESPONSE -> RE_REVIEW -> FINAL_AUDIT -> WORD_QA -> DELIVERED`

Draft Results and Analysis from verified user evidence before interpreting it. Keep Results observation-led and Discussion interpretation-led.

After drafting, automatically perform:

1. Structural and language polishing of the English and Chinese manuscripts.
2. Cross-checking of values, figures, tables, methods, statistics, terminology, and language alignment.
3. Claim-level verification that every material external assertion is truly supported by its citation.
4. Independent editorial, plant-domain, methods and statistics, relevant genetics or omics or breeding, and devil's-advocate review.
5. Manuscript revision, point-by-point response, and exact change tracking.
6. Re-review of every claimed change and a fresh final integrity audit.
7. Word generation, reopening, rendering, page inspection, correction, and re-rendering.

## Required Final Files

Create exactly three final Word files under `deliverables/`:

1. `01_plant_article_bilingual.docx` — complete English research article followed by the complete academic-Chinese article.
2. `02_claim_citation_audit_bilingual.docx` — data-consistency summary, claim-citation matrix, source anchors, support grades, boundaries, and unresolved risks.
3. `03_peer_review_and_response_bilingual.docx` — editorial synthesis, independent review reports, point-by-point responses, exact changes and locations, and re-review verification.

Place every other artifact under `intermediate_files/`, including configurations, approved outlines, datasets or derived summaries, search records, literature notes, evidence maps, draft versions, reviewer working files, structured Word inputs, validation reports, and rendered page images.

Use the available `docx` skill for Word creation and render-inspect-revise QA. `scripts/build_article_package.py` may build the three files from verified structured JSON; it must never fill missing scientific content.
