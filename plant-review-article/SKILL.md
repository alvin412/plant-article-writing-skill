---
name: plant-review-article
description: "Create publication-ready plant-science narrative reviews, perspectives, scoping reviews, systematic reviews, and meta-analyses. Use for complete or partial plant and crop review articles involving stress, signalling, hormones, gene families, development, immunity, genomics, omics, adaptation, yield, or breeding. For a new full review, require detailed outline approval, then continue through literature reading, bilingual drafting, polishing, claim-level citation verification, independent peer review, revision, point-by-point response, re-review, and three final Word deliverables while storing all intermediate artifacts in one folder."
---

# Plant Review Article

## Required References

- Read `references/review-workflow.md` for every full review.
- Also read `references/stress-review-storyline.md` for stress, gene-family, pathway, regulator, hormone, ncRNA, epigenetic, or signalling reviews.
- Also read `references/systematic-review-search.md` for scoping, systematic, or meta-analytic reviews.
- Read `references/quality-and-deliverables.md` before citation audit, peer review, revision, or Word generation.

Use `reading-literature` for every substantive cited source. Follow its Zotero confirmation gate whenever close-reading notes may be saved to Zotero.

## Core Contract

Do not invent results, mechanisms, statistics, references, novelty, limitations, or source passages. Match every claim to its evidence and plant context.

For a new full review:

1. Create a detailed topic-specific outline and evidence plan.
2. Stop and wait for explicit outline approval.
3. After approval, continue automatically through the remaining workflow unless essential source material, user data, external-write authorization, or a material scientific decision is missing.

## Workflow

Use:

`INTAKE -> OUTLINE_APPROVAL -> CORPUS -> CLOSE_READING -> EVIDENCE_MAP -> DRAFT -> POLISH -> CITATION_AUDIT -> PEER_REVIEW -> REVISION_RESPONSE -> RE_REVIEW -> FINAL_AUDIT -> WORD_QA -> DELIVERED`

The completed review must synthesize evidence by mechanism, scale, method, evidence strength, disagreement, or translation boundary rather than list papers chronologically.

After drafting, perform these steps without requiring separate user prompts:

1. Structural and language polishing of both manuscript languages.
2. Claim-level verification that every material external assertion is truly supported.
3. Independent editorial, plant-domain, methods, relevant omics or breeding, and devil's-advocate review.
4. Manuscript revision and a preserved point-by-point response for every review issue.
5. Re-review of every claimed change and a fresh final integrity audit.
6. Word generation, reopening, page rendering, visual inspection, correction, and re-rendering.

## Required Final Files

Create exactly three final Word files under `deliverables/`:

1. `01_plant_article_bilingual.docx` — complete English review followed by the complete academic-Chinese review.
2. `02_claim_citation_audit_bilingual.docx` — claim-citation matrix, source anchors, support grades, boundaries, unresolved risks, and bilingual explanations.
3. `03_peer_review_and_response_bilingual.docx` — editorial synthesis, independent review reports, point-by-point responses, exact changes and locations, and re-review verification.

Place every other project artifact under `intermediate_files/`, including search records, screening files, literature matrices, close-reading notes, outlines, draft versions, evidence maps, reviewer working files, JSON inputs, validation reports, and rendered page images.

Use the available `docx` skill for Word creation and render-inspect-revise QA. `scripts/build_article_package.py` may build the three files from verified structured JSON; it must never fill missing scientific content.
