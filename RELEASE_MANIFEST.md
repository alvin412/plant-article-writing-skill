# Release Manifest

## Included Skill Files

The GitHub release package contains the complete `plant-article-writing` skill:

```text
plant-article-writing/SKILL.md
plant-article-writing/agents/openai.yaml
plant-article-writing/references/plant-full-manuscript-workflow.md
plant-article-writing/references/plant-review-writing.md
```

## Repository Documentation

```text
README.md
FUNCTIONS.md
RELEASE_MANIFEST.md
.gitignore
```

## Excluded Materials

The package intentionally excludes:

- local reference PDFs
- Zotero database files
- private manuscripts
- generated drafts
- local validation caches
- Python virtual environments
- OS/editor metadata

## Validation

Validate the skill folder with:

```powershell
python "$env:USERPROFILE\.codex\skills\.system\skill-creator\scripts\quick_validate.py" ".\plant-article-writing"
```

Expected result:

```text
Skill is valid!
```

## Current Validation Status

The source and installed copies were validated locally after PyYAML installation:

```text
Skill is valid!
```
