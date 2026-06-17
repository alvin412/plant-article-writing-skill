# plant-article-writing

## English

`plant-article-writing` is a Codex skill for publication-ready plant-science manuscript and review writing. It is designed for plant biology, crop science, plant stress biology, genomics, pangenomics, GWAS/QTL/eQTL/TWAS, single-cell and spatial omics, signaling, transcription factors, yield, adaptation, and breeding papers.

The skill supports complete manuscript workflows, plant review-article workflows, section-level drafting and polishing, source-paper close reading, evidence rescue for weak Introduction/Discussion sections, revision, and citation checking.

## 中文说明

`plant-article-writing` 是一个面向植物科学论文写作的 Codex skill，用于撰写、润色、修改和检查达到发表水平的植物类学术论文与综述文章。适用方向包括植物生物学、作物科学、植物逆境生物学、基因组学、泛基因组、GWAS/QTL/eQTL/TWAS、单细胞与空间组学、信号转导、转录因子、产量、适应性和分子育种等。

该 skill 支持完整论文写作流程、植物综述写作流程、单个章节起草与润色、文献中英对照精读、引言和讨论证据不足时的补充检索、稿件修改以及引用检查。

## Repository Structure

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
    `-- references/
        |-- plant-full-manuscript-workflow.md
        `-- plant-review-writing.md
```

## Installation

Copy the `plant-article-writing/` folder into your Codex skills directory:

```powershell
Copy-Item -Recurse -Force .\plant-article-writing $env:USERPROFILE\.codex\skills\
```

After installation, the skill should be available as:

```text
plant-article-writing
```

## 安装方法

将 `plant-article-writing/` 文件夹复制到 Codex 的 skills 目录：

```powershell
Copy-Item -Recurse -Force .\plant-article-writing $env:USERPROFILE\.codex\skills\
```

安装后，skill 名称为：

```text
plant-article-writing
```

## Core Use Cases

- Write complete publication-ready plant-science manuscripts.
- Write plant-science review articles and literature reviews.
- Draft and polish Abstract, Introduction, Results, Discussion, Methods, Conclusion, title, keywords, and figure legends.
- Build detailed outlines before full manuscript or review drafting.
- Create bilingual close-reading notes for source papers.
- Search and verify literature when Introduction or Discussion evidence is insufficient.
- Revise manuscripts while preserving plant-science claim boundaries.
- Check citations, citation support, and reference consistency.

## 核心用途

- 撰写完整的发表级植物科学论文。
- 撰写植物科学综述、文献综述、叙述性综述和 perspective-style review。
- 起草和润色 Abstract、Introduction、Results、Discussion、Methods、Conclusion、title、keywords 和 figure legends。
- 在正式撰写完整论文或综述前，先生成详细大纲并等待确认。
- 为写作中阅读的文献生成中英对照精读笔记。
- 当 Introduction 或 Discussion 的文献证据不足时，进行补充检索和引用核验。
- 修改稿件，同时保持植物科学中的证据边界和因果强度。
- 检查正文引用、引用支撑关系和参考文献一致性。

See [FUNCTIONS.md](FUNCTIONS.md) for the full function list.

完整功能列表见 [FUNCTIONS.md](FUNCTIONS.md)。

## Workflow Summary

For a new full manuscript or review article, the skill first produces a detailed topic-specific outline and waits for user confirmation. After confirmation, it proceeds through literature synthesis, source-paper close reading, section-by-section drafting, evidence rescue, revision, citation checking, and final QA.

For single-section writing or polishing tasks, it can directly produce polished English and academic Chinese unless the section logic is too incomplete to support safe drafting.

## 流程概述

对于新的完整论文或综述文章，该 skill 会先生成针对主题的详细大纲，并等待用户确认。确认后，再进入文献综合、中英对照精读、分章节撰写、证据补强、稿件修改、引用检查和最终质量检查。

对于单个章节的撰写或润色任务，如果证据和逻辑足够，可以直接输出发表级英文和对应的学术中文；如果证据不足，会先指出缺口，而不是编造内容。

## Notes

This repository includes only the skill files required for Codex use. It does not include the user's local reference PDFs, Zotero library, or private manuscript materials.

No license has been selected yet. Add a license before making the repository public if you want others to reuse or modify the skill.

## 注意事项

该仓库只包含 Codex 使用该 skill 所需的文件，不包含用户本地参考文献 PDF、Zotero 数据库或私人稿件材料。

非常感谢大家的使用，需要更适配精细方向的可以联系我，邮箱：alvin412@163.com
