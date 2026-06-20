# plant-article-writing

Version: **v0.1**

`plant-article-writing` is a Codex skill for publication-ready plant-science manuscripts and reviews. It supports plant biology, crop science, stress biology, immunity, development, genomics, GWAS/QTL/eQTL/TWAS, pangenomes, single-cell and spatial omics, signalling, transcription factors, adaptation, yield, and breeding.

The skill uses a gated workflow:

`outline approval -> literature corpus -> evidence map -> drafting -> integrity review -> peer review -> revision -> re-review -> Word QA`

For plant-stress and gene-family reviews, v0.1 adds the narrative chain:

`Why -> What -> Where -> How -> Network -> Integration -> Application -> Future`

This converts a paper catalogue into an evidence-bounded regulatory model covering abiotic and biotic stress, mechanism, hormone networks, crosstalk, growth–stress trade-offs, breeding value, and testable future directions.

## 中文说明

`plant-article-writing` 是面向植物科学论文与综述写作的 Codex skill，适用于植物生物学、作物科学、逆境生物学、免疫、发育、基因组学、GWAS/QTL/eQTL/TWAS、泛基因组、单细胞与空间组学、信号转导、转录因子、适应性、产量和育种等方向。

该 skill 使用带质量门控的完整流程：

`大纲确认 -> 文献库构建 -> 证据映射 -> 正文撰写 -> 完整性检查 -> 模拟审稿 -> 修改 -> 再审 -> Word 质量检查`

v0.1 为植物逆境、基因家族和通路类综述新增以下叙事主线：

`Why -> What -> Where -> How -> Network -> Integration -> Application -> Future`

该框架强调从研究背景和对象定义出发，依次整合非生物与生物胁迫、作用机制、激素与信号网络、Crosstalk、发育—逆境权衡、统一调控模型、育种应用及可检验的未来方向。

## Core capabilities

- Mandatory outline approval before drafting a new full manuscript or review.
- Reproducible literature search and screening.
- Full-paper bilingual close reading.
- Claim-level citation and source-passage verification.
- Plant-specific evidence and causality boundaries.
- Narrative, perspective, scoping, and systematic review support.
- Independent plant-domain peer review, revision, and re-review.
- Figure, data, declaration, and submission-package checks.
- Three hierarchical Word deliverables with structural and visual QA.
- Mechanism-led plant-stress review storyline and unified-model design.

## Repository structure

```text
.
|-- README.md
|-- FUNCTIONS.md
|-- RELEASE_MANIFEST.md
|-- .gitignore
`-- plant-article-writing/
    |-- SKILL.md
    |-- agents/
    |   `-- openai.yaml
    |-- references/
    |   |-- citation-and-close-reading-audit.md
    |   |-- plant-full-manuscript-workflow.md
    |   |-- plant-review-writing.md
    |   |-- plant-stress-review-storyline.md
    |   |-- quality-gates-and-peer-review.md
    |   |-- submission-figures-and-data.md
    |   |-- systematic-review-and-search.md
    |   `-- word-deliverables.md
    `-- scripts/
        `-- build_word_package.py
```

## Installation

Copy the `plant-article-writing` folder into the Codex skills directory:

```powershell
Copy-Item -Recurse -Force .\plant-article-writing $env:USERPROFILE\.codex\skills\
```

安装时，将 `plant-article-writing` 文件夹复制到 Codex skills 目录：

```powershell
Copy-Item -Recurse -Force .\plant-article-writing $env:USERPROFILE\.codex\skills\
```

Invoke it as:

```text
$plant-article-writing
```

See [FUNCTIONS.md](FUNCTIONS.md) for the complete function list and [RELEASE_MANIFEST.md](RELEASE_MANIFEST.md) for release contents and validation status.

## Notes

The repository excludes private manuscripts, local literature libraries, generated drafts, and local caches.

No open-source licence has been selected. Add an appropriate licence before granting reuse or redistribution rights.

For requests requiring finer domain adaptation, contact: alvin412@163.com.
