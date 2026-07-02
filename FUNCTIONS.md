# Function List / 功能列表

## Router / 路由

`plant-article-writing` identifies whether a request concerns literature reading, a plant review, an original research paper, or journal finalization, then routes it to the correct independent skill.

`plant-article-writing` 判断请求属于文献精读、植物综述、原创研究论文还是期刊终审，并交由对应独立 skill 处理。

## Literature Reading / 文献精读

- Reads all substantive available sections rather than only the abstract.
- Produces English and academic-Chinese analytical notes with source anchors and figure or table context.
- Grades exact claim support and blocks metadata-only evidence.
- Verifies the latest available Clarivate JIF and builds a separate synthesis from directly relevant, full-text-read papers with `JIF >= 10.0`.
- Extracts bilingual domain terminology, paraphrased professional expression guidance, reported research logic, and clearly labelled inferred research ideas.
- Presents a provenance-backed candidate domain reference update and writes it only after author approval.
- Asks for confirmation before writing notes to the exact Zotero item.
- Uses direct Zotero note writing when available, otherwise verified Zotero Desktop interface control.

## Plant Review Article / 植物综述

- Supports narrative, perspective, scoping, systematic, and meta-analytic reviews.
- Requires detailed outline approval before drafting a new full review.
- Continues automatically through drafting, polishing, citation audit, peer review, revision, response, re-review, and Word QA.
- Uses mechanism-led synthesis and evidence-bounded plant context.

## Plant Research Article / 植物研究论文

- Writes Title, Abstract, Keywords, Introduction, Materials and Methods, Results and Analysis, Discussion, and Conclusion.
- Uses only author-supplied data, methods, results, analyses, figures, and tables.
- Checks methods, statistics, values, figures, tables, terminology, and English-Chinese alignment.
- Automatically completes polishing, citation audit, peer review, revision, response, re-review, and Word QA after outline approval.

## Article Finalize / 论文终审

- Applies a named journal's current official requirements and template.
- Checks references, section order, gene and allele italics, protein roman type, nomenclature, language, figures, tables, declarations, and submission conventions.
- Produces an English-only final manuscript and a bilingual compliance report.
- Does not regenerate reviewer responses.

## File Organization / 文件组织

The two writing skills output only three final Word files. Every intermediate artifact is placed under one `intermediate_files/` directory. Final files are placed under `deliverables/`.
