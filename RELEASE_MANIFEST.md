# Release Manifest

## Version

`v0.1`

Initial public workflow release of `plant-article-writing`, including the expanded publication pipeline and the mechanism-led plant-stress review storyline.

## Included skill files

```text
plant-article-writing/SKILL.md
plant-article-writing/agents/openai.yaml
plant-article-writing/references/citation-and-close-reading-audit.md
plant-article-writing/references/plant-full-manuscript-workflow.md
plant-article-writing/references/plant-review-writing.md
plant-article-writing/references/plant-stress-review-storyline.md
plant-article-writing/references/quality-gates-and-peer-review.md
plant-article-writing/references/submission-figures-and-data.md
plant-article-writing/references/systematic-review-and-search.md
plant-article-writing/references/word-deliverables.md
plant-article-writing/scripts/build_word_package.py
```

## Repository documentation

```text
README.md
FUNCTIONS.md
RELEASE_MANIFEST.md
.gitignore
```

## v0.1 highlights

- Mandatory outline approval and gated full-project workflow.
- Reproducible search, bilingual close reading, and claim-level citation verification.
- Independent plant-domain peer review, revision, and re-review.
- Three structured Word deliverables and format QA.
- Plant-stress review narrative:
  `Why -> What -> Where -> How -> Network -> Integration -> Application -> Future`.
- Integrated abiotic/biotic stress, hormone networks, crosstalk, development–stress trade-offs, unified regulatory models, and breeding translation.

## Excluded materials

- local reference PDFs
- Zotero databases
- private manuscripts
- generated drafts
- local validation caches
- Python virtual environments
- OS/editor metadata

## Validation

Run:

```powershell
python "$env:USERPROFILE\.codex\skills\.system\skill-creator\scripts\quick_validate.py" ".\plant-article-writing"
```

Expected result:

```text
Skill is valid!
```

The Word package builder has been executed against its generated template. All three DOCX files reopened successfully and passed title and heading-hierarchy checks. Page-image QA still requires an available Word-compatible renderer.
