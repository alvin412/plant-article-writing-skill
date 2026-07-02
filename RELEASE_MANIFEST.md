# Release Manifest

## Version

`v0.3`

## Skill Directories

```text
plant-article-writing/
reading-literature/
plant-review-article/
plant-research-article/
article-finalize/
```

Each directory contains `SKILL.md` and `agents/openai.yaml`. The four functional skills contain only the references and scripts required for their workflows.

## v0.3 Highlights

- Added verified `JIF >= 10.0` high-impact literature synthesis to `reading-literature`.
- Added bilingual terminology ledgers and paraphrased professional expression guidance.
- Added separate reported research-logic maps and explicitly inferred research ideas.
- Added a controlled, provenance-backed skill domain update gate requiring author approval.
- Prevented JIF from being treated as paper-level evidence quality or a replacement for directly relevant lower-JIF literature.

## v0.2 Highlights

- Replaced mixed project modes with one router and four independent skills.
- Added full-paper literature reading with explicit Zotero-note confirmation and post-write verification.
- Split plant review and original research writing into distinct workflows.
- Added the required original-research section contract.
- Automated polishing, claim-level citation audit, peer review, revision, point-by-point response, re-review, and three-file delivery after outline approval.
- Standardized `deliverables/` and `intermediate_files/` project layout.
- Added target-journal finalization with English-only manuscript output and bilingual compliance reporting.

## Validation

Run `quick_validate.py` against each of the five skill directories. Run both copies of `build_article_package.py` against their generated template and confirm that all three DOCX files reopen with valid titles and heading hierarchy. Page-image inspection remains a separate mandatory release gate during real manuscript work.
