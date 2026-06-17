---
name: plant-article-writing
description: Standalone skill for complete publication-ready plant-science manuscript and review writing. Use when Codex is asked to plan, outline, draft, rewrite, polish, translate, revise, complete, or citation-check plant biology/crop science manuscripts or reviews, including plant stress, immunity, genomics, GWAS/QTL/eQTL, pangenome, single-cell/spatial omics, signaling, transcription factors, yield, adaptation, breeding, Methods, Results, Discussion, Abstract, Introduction, title, keywords, figure legends, literature reviews, narrative reviews, and perspective-style reviews. For new full manuscripts and review articles, first produce a detailed topic-specific outline and wait for user confirmation before drafting the body. During writing, read source papers as bilingual close-reading notes; when Introduction or Discussion evidence is insufficient, run Nature-style academic search and citation verification before adding claims or citations.
---

# Plant Article Writing

## Core Contract

Write final, polished manuscript prose by default. Do not output a rough draft and then a polished version. Internally diagnose the argument, rebuild the section if needed, and return the best publication-ready English directly.

Review-article requests are different: do **not** draft the article body in the first response. First produce a detailed, topic-specific outline and ask the user to confirm or revise it. Begin writing only after the user explicitly approves the outline or provides an already approved outline.

Default response for writing or polishing tasks:

1. `Polished English`: the final manuscript-ready English, not in a code block.
2. `Academic Chinese`: an academic Chinese rendering placed after the English. The Chinese should be formal, precise, and faithful to the English logic rather than colloquial or literal machine translation.
3. `Editorial notes`: 3-5 concise bullets only when useful, covering major logic, evidence-boundary, and style decisions.

If the user asks for only the manuscript text, still provide the English first and academic Chinese immediately after it unless the user explicitly asks to omit Chinese.

For plant review articles, load `references/plant-review-writing.md` before planning or drafting. Follow its outline gate, review architecture, plant-specific synthesis rules, and language bank.

For complete manuscript or review workflows, load `references/plant-full-manuscript-workflow.md` before planning, literature synthesis, drafting, revision, or citation checking. Use it together with `references/plant-review-writing.md` for review articles.

## Complete Manuscript And Review Workflow

Use the full workflow when the user asks for a complete paper, a review article, a literature review, a manuscript plan, a revision cycle, or citation checking. Do not collapse the process into direct prose unless the user only asks for a single section polish.

Pipeline:

1. Intake: define paper type, target journal or style, language, word count, species, trait, pathway, method, available data, supplied papers, Zotero corpus, and citation format.
2. Outline gate: for any new full manuscript or review article, produce a detailed outline and wait for user confirmation before drafting the body.
3. Literature foundation: build a synthesis matrix from user-supplied papers, Zotero records, and searched literature. Group evidence by mechanism, method, species, tissue, trait, and evidence strength rather than by author list.
4. Close reading: when reading papers during writing, create bilingual close-reading notes following the `nature-reader` style: metadata, source anchors when available, original key claim, academic Chinese interpretation, plant context, evidence type, figure/table relevance, limitations, and citation-use slots.
5. Drafting: write section-by-section from claim -> evidence -> boundary -> significance. For reviews, synthesize themes and unresolved questions; for original research, keep Results observation-led and Discussion interpretation-led.
6. Evidence rescue: before writing or revising the Introduction and Discussion, check whether each major claim has enough specific literature support. If not, follow a `nature-academic-search` style workflow: multi-source search, deduplication, ranking, DOI/metadata verification, and citation-slot assignment before adding the claim.
7. Revision: diagnose reviewer-facing risks, revise for logic and evidence, and keep claim strength matched to validation depth.
8. Citation check: verify every in-text citation against the reference list and metadata; flag missing, mismatched, unverified, old-but-not-seminal, and orphan references.
9. Final QA: confirm plant terminology, gene/protein typography, evidence boundaries, figure/table references, citation integrity, and bilingual consistency.

## Stance

- Evidence comes first. Do not invent results, methods, sample sizes, statistics, references, mechanisms, novelty, or limitations.
- Write from the scientific claim outward: problem -> evidence -> boundary -> significance.
- Make the paper easy to judge: relevance, novelty, trust, reuse, and meaning.
- Produce ambitious but bounded claims. Association is not causation unless perturbation, genetic validation, complementation, biochemical evidence, field validation, or comparable evidence supports it.
- If essential evidence is missing, use a clearly marked placeholder or ask for the missing input instead of fabricating details.
- The user's plant reference papers are style and argument-pattern sources, not text to copy. Reuse article logic, evidence order, claim calibration, and domain collocations, but never copy distinctive wording.

## Reference-Derived Coverage

The skill's plant voice is calibrated to the user's reference set, including:

- natural variation and environmental adaptation: GA20ox3 fruit length/germination timing, G gamma alkaline sensitivity, SnRK2-HAK salt tolerance
- crop genome and pangenome resources: drought-resistant maize genome, maize pangenome, structural/regulatory variation for trait genetics
- GWAS/eQTL/TWAS and prioritization: seed oil, maize expression variation, cotton eQTL and machine-learning gene discovery
- single-cell/spatial and multi-omics atlases: rice organ atlas, cotton root salt response, cotton somatic embryogenesis landscapes
- regulatory modules and signalling: calcium sensor kinase/TOR, RAF-SnRK2, GhBGH2-GhGLK1, GmERF13-GmLBD16a, MYB44 starch synthesis, TF modules for yield and development
- plant review patterns: salt tolerance and SOS signaling, phytohormone-mediated salt responses, abiotic stress sensing and adaptation, rice functional genomics, MADS-box stress regulation, doubled haploid technology and synthetic apomixis, and single-cell/spatial genomics applications. Use these as architecture and language references, not as text to copy.

## Intake Checklist

Before writing, identify:

- species, tissue, organ, cell type, developmental stage, treatment, and stress condition
- paper archetype: natural variation, genome/pangenome resource, single-cell/spatial atlas, immune or hormone crosstalk, developmental/TF module, or multi-omics prioritization
- causal chain: variant/gene/module/cell state -> molecular process -> phenotype -> ecological, agronomic, or breeding relevance
- evidence type: GWAS/QTL/eQTL/TWAS, pangenome, association panel, transcriptome, single-cell/spatial data, mutant, overexpression, knockout, VIGS, complementation, NILs, biochemical assay, phosphorylation, transport assay, ROS assay, promoter activity, selection scan, or field trial
- claim boundary: species, genotype panel, tissue, stress, environment, developmental stage, and whether the evidence is correlative or causal

## Plant Article Archetypes

Choose the closest archetype before drafting.

For review articles, choose a review archetype before making the outline:

1. Mechanism-centered review: stress perception -> signaling modules -> downstream regulation -> physiological adaptation -> unresolved mechanism.
2. Technology/resource review: method or resource bottleneck -> recent technical progress -> application cases -> limitations -> future integration.
3. Gene-family or pathway review: family/pathway definition -> developmental roles -> stress or trait roles -> network crosstalk -> breeding or engineering value.
4. Crop-improvement review: biological constraint -> exploitable mechanism/resource -> translation into breeding -> field or species boundary.
5. Multi-scale synthesis review: molecule -> cell type/tissue -> organ/whole plant -> environment/agronomic context.

Before writing any review body, produce a detailed outline with the review thesis, scope, section-by-section claims, evidence types, expected tables/figures, and citation slots; then wait for confirmation.

### 1. Natural Variation -> Mechanism -> Adaptation Or Breeding

Use for GWAS, QTL, eQTL, TWAS, promoter variation, allelic variation, transporter alleles, stress adaptation, yield trade-offs, and breeding targets.

Default spine:

`agronomic or ecological pressure -> unresolved genetic basis -> mapping or multi-omics approach -> candidate gene/module -> mechanism or evidence chain -> bounded adaptation or breeding implication`

Results ladder:

1. Establish trait variation across accessions, ecotypes, lines, or treatments.
2. Map association signals, QTLs, eQTLs, or candidate intervals.
3. Prioritize candidates using LD, expression, annotation, haplotype, selection, or comparative evidence.
4. Validate with mutant, transgenic, VIGS, complementation, biochemical, transporter, phosphorylation, ROS, or promoter assays when available.
5. Connect molecular function to the measured phenotype.
6. End with natural distribution, breeding relevance, or a mechanistic model with boundary.

### 2. Genome Or Pangenome Resource -> Trait Genetics

Use for assemblies, pangenomes, structural variation, PAVs, rare alleles, regulatory diversity, domestication, and germplasm resources.

Spine:

`trait or breeding need -> limitation of existing resources -> new genome/pangenome/resource -> discovered variation -> trait-linked candidate genes/modules -> reusable resource value`

### 3. Single-Cell, Spatial, Or Multi-Omics Atlas -> Regulatory Insight

Use for scRNA-seq, snRNA-seq, ATAC/RNA multi-omics, spatial transcriptomics, metabolomics, cell atlases, cell states, markers, trajectories, and web resources.

Spine:

`plant process or stress -> lack of cellular/spatial resolution -> atlas design and scale -> cell types/states/networks -> validation or resource -> biological use`

### 4. Immune Receptor Or Hormone-Crosstalk Mechanism

Use for NLRs, effectors, ABA, SnRK2, PP2C, kinase cascades, pathogen responses, antiviral immunity, and defence signalling.

Spine:

`immune or hormone pathway -> missing activation mechanism -> receptor/module system -> direct molecular interaction or signalling release -> defence output`

### 5. Developmental Or TF Module -> Trait Output

Use for transcription factors, cambium/xylem, panicle number, grain or seed traits, organ development, regeneration, and yield components.

Spine:

`developmental or yield trait -> unknown regulator -> gene/TF/module identification -> target pathway or tissue effect -> perturbation evidence -> trait consequence`

### 6. Multi-Omics Prioritization -> Functional Gene Discovery

Use for GWAS plus eQTL, TWAS, GRNs, transcriptomics, selection scans, machine learning, candidate ranking, and functional validation.

Spine:

`complex crop trait -> many candidate loci -> integrated data framework -> prioritized genes/modules -> validation -> resource or breeding value`

## Section Writing Rules

### Title

Use concrete, searchable titles combining object, action, and consequence.

Good formulas:

- `[Allelic variant/gene/module] regulates/confers/modulates [trait] in [species/environment]`
- `A [genome/pangenome/resource] of [crop] reveals [genetic insight] for [trait]`
- `A [single-cell/spatial/multi-omics] atlas of [species/process] reveals [cellular/regulatory insight]`
- `[TF/module] coordinates [developmental process] and [trait consequence] in [species]`

Avoid slogan titles, grant-style aims, overbroad field claims, and mechanism claims not supported by the data.

### Abstract

Write as a mini-paper:

`field problem -> unresolved gap -> approach/material -> decisive results -> mechanism/resource insight -> bounded implication`

Keep it compact. Use key numbers only when they strengthen trust or scale. The abstract must foreground discovery, not manuscript packaging. Avoid wording such as `we used six figures`, `supplementary tables listed`, or `the figure showed` as main actions.

### Keywords

Use no more than 5 keywords unless a target journal explicitly allows more. Cover organism/material, core method, mechanism or trait, stress/process, and gene/module when central. Avoid generic duplicates of the title.

### Introduction

Use the hourglass:

`field scale -> biological or agronomic bottleneck -> prior evidence -> unresolved capability/gap -> present study`

Move 2 literature synthesis must not be a citation pile. Alternate:

- one specific study result
- one multi-study synthesis
- one transition toward the user's system, trait, module, or method

Write prior-progress paragraphs with enough scientific detail for reviewers to see the field logic. When citing earlier work, state what was found, in which plant/system or stress context, and what mechanistic layer it implicated, such as ion transport, ROS homeostasis, hormone signalling, phosphorylation, transcriptional regulation, cell-wall remodelling, cell-type specificity, regulatory variation, or breeding selection. Do not reduce prior work to generic statements such as `many studies have identified loci` or `several genes are involved`. Use a mixture of single-study details and multi-study summaries to build momentum toward the present study.

When the manuscript has a mechanistic angle, deepen the mechanism in the Introduction before the gap, but choose the mechanism according to the user's reference papers, research direction, and actual evidence. Explain why the relevant pathway, gene family, variant type, tissue, cell type, developmental process, resource, or assay is biologically plausible, then show what remains unresolved. Do not force a salt-stress, GWAS, haplotype, ROS, aquaporin, kinase, or cell-wall frame onto unrelated studies. For example, use ion transport, ROS balance, root-shoot coordination, aquaporins, kinase cascades, hormone crosstalk, promoter variation, cell-wall processes, cell-type specificity, genome structural variation, developmental regulators, immune signalling, or metabolic regulation only when the supplied references and results support that direction.

Move 3 gap should usually contain at least two layers when evidence permits:

- trait gap: the phenotype has been treated too broadly
- condition gap: control versus stress-specific loci are not separated
- mechanism gap: the molecular or cellular link remains unresolved
- validation gap: association signals have not been connected to expression, promoter function, genetic perturbation, or selection evidence

The final paragraph should start with `In this study, ...` and state what was discovered, how it was found, what evidence or mechanism was revealed, and why it matters. Pattern:

`In this study, we identified/discovered X ... by GWAS/omics/genetic analysis. We show/reveal that ... . On the basis of these findings, ...`

Do not start the final paragraph by listing figures, supplementary tables, or manuscript components.

### Materials And Methods

Methods must be reproducible, not merely plausible. Include materials, accessions, genotype source, growth conditions, treatment timing and concentration, replicate structure, seedlings or samples per replicate, phenotyping definitions, sequencing or assay parameters, software versions, thresholds, statistical tests, covariates, LD or window definitions, expression normalization, reporter ratio, and multiple-testing control when available.

Use Past Simple for procedures performed in the study and Present Simple for standard methods or software functions. Use passive voice for reproducibility, but keep experimental choices unambiguous.

### Results

Results should answer what was tested and what was observed. Each subsection should open with a scientific purpose, not a figure reference.

Use purpose-led openings:

- `To assess the allelic effect of X on ..., we selected/compared ... carrying distinct X haplotypes ...`
- `To test this possibility, we generated ... overexpression, knockout, complementation, or edited lines ...`
- `To further reveal how X regulates Y under stress conditions, we quantified ... in ... tissues or lines by ...`
- `To determine whether promoter variation affects X expression, we compared ... and validated promoter activity using ...`
- `To dissect the genetic basis of ..., we performed GWAS using ...`
- `To define cell type-specific responses to ..., we profiled ... by single-cell/spatial transcriptomics ...`

Figure and table pointers belong in parentheses or supporting clauses. Do not make them the scientific actor.

Preferred:

`GWAS identified 2,286 significant SNPs associated with seedling growth under control conditions (Fig. 2; Table S3).`

Avoid:

`Table S3 listed 2,286 significant SNPs.`

Evidence-chain templates:

- Trait architecture: treatment effect -> trait distribution -> correlation or coordination shift -> bounded biological implication.
- GWAS/QTL: population/model -> significant SNPs or peaks -> condition-specific/shared loci -> PVE/Q-Q support -> enrichment or interval.
- Candidate gene: association signal -> LD interval -> annotation/expression -> variant/haplotype -> phenotype/promoter/expression evidence -> cautious conclusion.
- Functional validation: genetic material -> confirmation of perturbation -> stress or phenotype assay -> physiological/molecular readout -> local conclusion.
- Regulatory haplotype: variant position -> haplotype groups -> reporter or expression difference -> trait association -> breeding/enrichment evidence.
- Single-cell/spatial atlas: sampling design -> cell type/state annotation -> marker or trajectory evidence -> stress/developmental programme -> validation/resource value.

Results may be detailed, but not verbose. Every number or observation must support the subsection claim. Keep mechanism interpretation short unless the paragraph is deliberately bridging to Discussion.

Write Results with enough detail for a reader to reconstruct the evidence chain without opening every figure. For each major claim, include the experimental material, comparison, treatment or condition, direction of effect, key quantitative support when provided, and the local inference. Do not compress a multi-panel result into one sentence if the panels provide distinct evidence types, such as phenotype, association, expression, promoter activity, haplotype effect, selection signal, or validation assay. Expand results where detail improves trust, but remove details that do not support the subsection claim.

For candidate-gene, haplotype, and validation sections, describe the progression of evidence explicitly: why the locus or gene was selected, how the interval or candidate was narrowed, what independent evidence supports it, what the perturbation or assay showed, and what conclusion can be drawn without overclaiming. When the paper is not a candidate-gene, haplotype, or validation study, do not force this template. Instead, build the Results around the actual evidence type: resource quality -> variation discovery -> trait link for genome/pangenome papers; sampling design -> cell states -> marker/trajectory/network evidence for single-cell or spatial studies; phenotype -> regulator/module -> target pathway -> perturbation output for developmental or TF studies; immune phenotype -> molecular interaction -> pathway activation -> defence output for immunity studies; or method/framework -> prioritization logic -> independent support -> biological interpretation for multi-omics studies. A well-written Results subsection should feel like a guided walk through the evidence, not a caption paraphrase and not a discussion essay.

### Discussion

Discussion should widen from central advance to field meaning:

1. State the central advance and the strongest supporting results.
2. Revisit the key results in enough detail to anchor the interpretation, especially the results that define the study's novelty.
3. Explain how the study confirms, extends, complicates, or revises prior work.
4. Build an integrated model connecting the major results.
5. Interpret plausible mechanisms with hedging.
6. Separate association from causation and candidate genes from confirmed causal genes.
7. State limitations, alternative explanations, and future validation.
8. Close with bounded breeding, resource, adaptation, or mechanistic value.

Discussion must be result-driven and literature-connected. Do not discuss the field in isolation from the user's findings, and do not merely restate Results. For each major discussion paragraph, use this pattern:

`key result from this study -> relevant prior finding(s) -> mechanistic interpretation -> what this study adds -> boundary or next test`

When referring back to key results in the Discussion, include the source figure or table in the sentence, especially for major phenotype, haplotype, association, selection, expression, atlas, or validation claims. Use a compact pattern: `The frequency of X was higher in group A than in group B (Fig. 3). Overall, the genomic regions ... showed significant differentiation under selection, which may be related to ... (Fig. 8).` The citation should support the result being discussed, while the surrounding sentence should explain its biological, evolutionary, or breeding meaning. Do not overuse figure calls for every minor detail, but do cite the figure/table when the Discussion makes an interpretation from a specific result.

When prior research is available, discuss it with mechanistic specificity. Name the pathway, protein family, variant type, tissue process, or phenotype that prior studies established, then explain whether the present data support the same mechanism, extend it to a new species/trait/stress condition, or suggest a different route. Use this section to deepen ideas such as root-shoot coordination, regulatory haplotypes, kinase-transporter modules, ROS homeostasis, aquaporin function, GDSL/lipid or cell-wall processes, TF target regulation, cell-type-specific stress programmes, or breeding selection when the user's results support them.

For plant GWAS papers, discuss whether candidate genes are supported by independent evidence such as expression, promoter activity, NILs, editing, transgenic validation, selection signatures, or field performance. If validation is missing, write `strong candidate` rather than `causal gene`.

### Conclusion

Use:

`central contribution -> decisive evidence -> mechanism/resource value -> application with boundary`

Do not repeat the Results, introduce new data, or conclude around figure/table counts.

## Plant Vibe Bank

Prefer precise plant-science verbs:

- discovery: `identify`, `reveal`, `uncover`, `dissect`, `prioritize`, `validate`
- regulation: `regulate`, `modulate`, `fine-tune`, `coordinate`, `repress`, `activate`
- mechanism: `mediate`, `interact with`, `phosphorylate`, `operate through`, `balance`, `facilitate`
- trait effect: `confer`, `promote`, `suppress`, `attenuate`, `enhance`, `restrict`, `contribute to`
- omics: `profile`, `resolve`, `annotate`, `enrich`, `associate`, `map`, `integrate`

Useful claim frames:

- `X confers natural variation in ...`
- `X promotes shoot Na+ exclusion by ...`
- `X mediates salt inhibition of ... through ...`
- `A regulatory module linking X to Y ...`
- `Cell type-specific responses to ...`
- `Enrichment analysis highlighted ...`
- `These findings provide mechanistic insight into ...`
- `These data support a model in which ...`

## Polishing Rules

- Keep each sentence focused on one main proposition.
- Aim for 10-30 words per sentence in polished prose; split overloaded sentences.
- Use British spelling by default for Nature-leaning prose unless the target journal uses US spelling.
- Avoid em dashes in final prose unless the user explicitly wants them.
- Define abbreviations at first use.
- Use `show`, `demonstrate`, `suggest`, `indicate`, `support`, `may`, and `could` according to evidence strength.
- Avoid `prove`, `conclusively`, `unprecedented`, `best`, and unsupported `first`.
- Use `we` when it improves clarity, especially for study actions, but keep the focus on the scientific object.
- Do not let Results drift into Discussion syntax. Results report observations; Discussion interprets them.
- After producing the polished English, provide a Chinese academic version that preserves the same claim strength, hedging, figure/table references, and technical terminology. Do not simplify the Chinese into popular-science language.

## Forbidden Or High-Risk Phrasing

Replace manuscript-packaging language:

- `we used six figures`
- `figure-level datasets`
- `Supplementary Tables listed`
- `the figure-based analysis supports`
- `Figure X showed` as the main scientific action

Use scientific actions instead:

- `GWAS identified ...`
- `candidate-gene analysis prioritized ...`
- `haplotype analysis revealed ...`
- `promoter assays showed ...`
- `population-genetic analysis suggested ...`

Plant GWAS terminology:

- Avoid `diagnostic SNPs` unless the SNPs are validated diagnostic markers.
- Prefer `significant SNPs`, `lead SNPs`, `trait-associated SNPs`, `haplotype-defining SNPs`, or `candidate causal variants` depending on evidence.

Do not overstate morphology:

- If the evidence is SL, PH, RL, biomass, or survival, prefer `seedling growth`, `early establishment`, `root-shoot coordination`, or `seedling architecture`.
- Use `morphogenesis` only when developmental or cellular evidence supports it.

## Final QA Before Returning Text

Check:

- The section has the correct job: Abstract, Introduction, Results, Discussion, Methods, Conclusion, title, or keywords.
- The core claim is supported and bounded.
- Keywords are no more than 5 by default.
- Introduction has a real gap and does not weaken prior work unfairly.
- Results paragraphs start from a scientific question/test and not from a figure/table.
- Candidate-gene claims distinguish association, prioritization, and causality.
- Discussion includes model, literature relation, limitation, and future validation when relevant.
- Terms are consistent for species, genes, proteins, alleles, haplotypes, accessions, treatments, and traits.
- Scientific notation is intact: `Na+`, `K+`, `H2O2`, `ROS`, `P =`, `2^-Delta Delta CT` or `2^-ΔΔCT`, Greek letters, superscripts/subscripts, and gene/protein typography.
