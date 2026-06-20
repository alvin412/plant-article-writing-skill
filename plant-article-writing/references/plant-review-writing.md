# Plant Review Article Writing

Use this reference when the user asks for a plant-science narrative review, perspective, scoping review, systematic review, meta-analysis, or Chinese requests such as `植物综述`, `发表级综述`, `植物类综述文章`, `文献综述`, or `综述初稿`.

This reference distills review-article logic from the local plant review corpus and the review-writing rules in `nature-writing` and `nature-polishing`. The papers are architecture and language references only. Do not copy their wording.

## Non-Negotiable Outline Gate

For every review-writing request:

1. Do not draft the article body in the first response.
2. First produce a detailed outline tailored to the user's topic.
3. Ask the user to confirm, revise, narrow, or expand the outline.
4. Start drafting only after explicit confirmation, or when the user provides an already approved outline.

The outline must include:

- working title options
- one-sentence review thesis
- scope and exclusions, including species, stress, trait, method, pathway, or time window when relevant
- intended review type: mechanism-centered, technology/resource, gene-family/pathway, crop-improvement, or multi-scale synthesis
- section-by-section argument map
- key claims for each section
- evidence types or citation slots for each claim
- proposed figures, tables, and boxes
- unresolved questions and future-perspective points
- selected review method: narrative, perspective, scoping, systematic, or meta-analysis
- proposed databases, search period, screening logic, and evidence appraisal when the review is systematic or scoping

For scoping, systematic, or meta-analytic work, also load `systematic-review-and-search.md`. Do not label a review systematic unless the search strings, dates, screening decisions, inclusion/exclusion criteria, and evidence appraisal are reproducible.

## Review Argument Chain

A publication-level plant review is not a paper-by-paper survey. Use this chain:

`field pressure -> plant-specific biological problem -> precise scope -> organizing principle -> synthesized evidence groups -> disagreements and unresolved gaps -> author's reasoned stance -> future directions and crop or mechanistic value`

Good organizing principles:

- mechanism: perception -> signaling -> transcriptional or post-translational control -> physiological output
- scale: molecule -> cell type -> tissue -> organ -> whole plant -> field environment
- technology: bottleneck -> method advance -> application cases -> limitations -> integration
- pathway or gene family: definition -> conserved roles -> stress/developmental roles -> crosstalk -> engineering potential
- breeding: trait constraint -> mechanistic or genomic resource -> validation boundary -> translational route

Avoid `Author A reported X; Author B reported Y`. Instead group studies by what they collectively show, where they disagree, and what remains unresolved.

For plant stress, gene-family, pathway, regulator, hormone, ncRNA, epigenetic, or signalling reviews, also load `plant-stress-review-storyline.md`. Use its progression from `Why -> What -> Where -> How -> Network -> Integration -> Application -> Future` to turn a catalogue of studies into a field-level explanatory model.

## Plant Review Archetypes

### 1. Stress Mechanism Review

Use for salt, drought, heat, cold, nutrient, heavy metal, oxidative, or combined stress.

Default outline:

1. Why the stress limits plant productivity and adaptation.
2. Primary stress dimensions: ionic, osmotic, oxidative, temperature, nutrient, or cellular-damage layers.
3. Early perception and second messengers: Ca2+, ROS, phospholipids, pH, membrane or cell-wall cues when supported.
4. Core signaling modules: CBL-CIPK/SOS, SnRK2/ABA, MAPK cascades, hormone pathways, kinase modules, or TF networks.
5. Tissue, organ, developmental-stage, and species specificity.
6. Physiological outputs: ion homeostasis, water management, growth adjustment, root architecture, photosynthesis, reproductive success, or yield.
7. Outstanding questions and experimental routes.

Plant language:

- `plants re-establish ionic, osmotic, and redox homeostasis`
- `stress signals are decoded through calcium-dependent and hormone-mediated networks`
- `adaptation depends on the coordination of growth restraint, cellular protection, and developmental plasticity`
- `the remaining challenge is to connect early signaling events with tissue-specific growth outcomes`

### 2. Hormone Crosstalk Review

Use for ABA, auxin, cytokinin, ethylene, gibberellin, brassinosteroid, jasmonate, salicylic acid, strigolactone, or peptide hormone reviews.

Default outline:

1. Stress or developmental cue and the need to balance growth with survival.
2. Hormone biosynthesis, transport, metabolism, and signaling.
3. Crosstalk modules: synergistic, antagonistic, sequential, or tissue-specific interactions.
4. Molecular links to kinases, TFs, ion transporters, ROS, or cell-wall remodeling.
5. Species and organ specificity.
6. Crop-improvement opportunities and risks of growth penalties.

Use precise relation words: `integrates`, `antagonizes`, `potentiates`, `attenuates`, `reprograms`, `fine-tunes`.

### 3. Gene-Family Or Pathway Review

Use for MADS-box, bHLH, MYB, NAC, WRKY, NLR, SnRK, CIPK, HAK, aquaporins, transporters, or other families/pathways.

Default outline:

1. Establish the environmental or agronomic problem and the synthesis gap.
2. Define the family/pathway, origin, classification, conserved features, and normal biological functions.
3. Map involvement across relevant abiotic and biotic stresses without forcing unsupported categories.
4. Explain upstream control, direct targets, protein interactions, feedback, epigenetic regulation, and post-translational control.
5. Integrate hormone signalling, shared stress nodes, development-stress trade-offs, and combined-stress crosstalk.
6. Propose a unified, evidence-bounded regulatory model.
7. Identify conserved versus lineage- or crop-specific functions.
8. Evaluate engineering and breeding routes, limitations, and decisive future experiments.

Avoid calling a gene a `master regulator` unless the literature supports broad upstream control with genetic and molecular evidence.

### 4. Functional Genomics, Omics, And Resource Review

Use for functional genomics, GWAS/QTL/eQTL/TWAS, pangenomics, pantranscriptomics, single-cell/spatial genomics, atlases, databases, or high-throughput phenotyping.

Default outline:

1. Biological or breeding bottleneck that old approaches could not resolve.
2. What the resource or technology makes visible.
3. Major application classes: gene discovery, regulatory variation, cell-type states, spatial programs, structural variation, or breeding targets.
4. Reliability issues: sampling, annotation, batch effects, resolution, genotype diversity, environmental context, validation.
5. Integration with genetics, perturbation, field phenotyping, and breeding.
6. Future standards for data reuse and mechanistic validation.

Plant language:

- `resolve cell-type-specific programmes`
- `link regulatory variation to trait architecture`
- `place candidate genes within tissue and developmental context`
- `move from atlas construction to hypothesis-driven perturbation`

### 5. Breeding Technology Review

Use for doubled haploid technology, synthetic apomixis, genome editing, de novo domestication, molecular breeding, or hybrid fixation.

Default outline:

1. Breeding problem and why the technology matters.
2. Component processes and recent advances.
3. Crop-specific implementation status.
4. Biological and technical bottlenecks.
5. Integration with genomics, editing, speed breeding, or prediction.
6. Practical boundaries: penetrance, genotype dependence, fertility, field performance, regulatory constraints.

End with realistic translational routes rather than promotional claims.

## Section-Level Rules

### Title

Make the title specific and searchable:

- `Mechanisms and breeding potential of [process] in [plant group/crop]`
- `[Pathway/gene family] at the interface of [stress/development] and [trait]`
- `From [technology/resource] to [crop application]: advances and bottlenecks in [field]`

Avoid vague titles such as `Research progress on plant stress`.

### Abstract

Write the abstract as:

`field problem -> recent progress -> unresolved synthesis gap -> review scope and organizing principle -> integrated insight -> future direction`

Do not write a methods-style abstract. A review abstract should tell readers what map of the field they will gain.

### Introduction

Use a review-specific hourglass:

1. Establish the biological or agronomic importance.
2. Define the plant-specific system, pathway, technology, or trait.
3. Explain why recent evidence now needs synthesis.
4. State what previous reviews or fragmented studies have not integrated.
5. Define the scope and organizing principle of this review.

### Main Sections

Each section must start with a synthesis claim, not a citation list.

Paragraph pattern:

`topic synthesis claim -> grouped evidence -> contrast or unresolved tension -> mechanistic or translational interpretation -> boundary`

Examples of useful section moves:

- `Several lines of evidence now place X upstream of Y, but the tissue context of this regulation remains unclear.`
- `These studies converge on a role for X in maintaining ion homeostasis, although they differ in the proposed upstream sensor.`
- `The strongest support comes from genetic perturbation and transporter assays, whereas expression-only studies should be interpreted as candidate evidence.`

### Figures, Tables, And Boxes

A strong plant review usually needs:

- one conceptual model figure for the pathway or mechanism
- one table grouping genes, pathways, technologies, or species by evidence level
- one timeline or workflow figure for technology/resource reviews
- one future-directions box listing open questions and decisive experiments

For integrative stress reviews, the conceptual model must show the causal reading path from stress inputs through shared and stress-specific signalling nodes to the focal regulator, targets, physiological outputs, growth or yield trade-offs, and breeding interventions. Visually distinguish demonstrated links from hypotheses.

### Future Perspectives

The closing section should give a usable map of the field. Include:

- unresolved mechanisms
- contradictory or species-specific evidence
- missing tissue, cell-type, developmental-stage, or field-context data
- validation needs: mutants, complementation, biochemical assays, spatial validation, field trials, or cross-species tests
- translational opportunities with boundaries

Avoid ending with a generic summary.

## Language And Style

Use plant-science verbs that express synthesis:

- `synthesize`, `integrate`, `reconcile`, `place in context`, `highlight`, `map`, `define`, `distinguish`, `link`, `connect`, `prioritize`, `resolve`
- `perceive`, `decode`, `transduce`, `coordinate`, `fine-tune`, `reprogram`, `buffer`, `restore`, `maintain`, `balance`
- `confer`, `constrain`, `enhance`, `attenuate`, `promote`, `restrict`, `compromise`, `stabilize`

Use logical transitions instead of generic additive transitions:

- contrast: `in contrast`, `whereas`, `by comparison`, `a remaining tension is`
- accumulation: `building on this`, `consistent with this model`, `together, these findings`
- limitation: `however`, `nevertheless`, `this interpretation remains limited by`
- consequence: `therefore`, `as a result`, `this points to`, `this raises the possibility that`

For Chinese notes, translate intent rather than syntax. First extract claims, evidence, conditions, comparison, implication, and limitation; then rebuild English paragraphs in review order.

## Evidence Boundaries

Keep claim strength matched to evidence:

- Expression correlation -> `is associated with`, `is consistent with`, `marks`, `suggests`.
- Mutant or transgenic phenotype -> `supports a role for`, `contributes to`, `is required for` only when the design supports necessity.
- Biochemical interaction -> `interacts with`, `phosphorylates`, `binds`, but do not infer whole-plant adaptation without genetic or physiological evidence.
- Cross-species patterns -> `appears conserved across`, `may represent a lineage-specific route`, depending on the evidence.
- Breeding implication -> `could be exploited`, `provides a candidate route`, not `will improve yield` unless field evidence supports it.

High-risk phrases to avoid:

- `many studies have shown` without specifying the evidence class
- `this review comprehensively summarizes everything`
- `the mechanism has been fully clarified`
- `master regulator` without strong network evidence
- `important theoretical and practical significance`
- unsupported `first`, `novel`, `breakthrough`, or `perfect solution`

## Final QA For Review Drafts

Before returning a review outline or draft, check:

- The scope is narrow enough for a publishable review.
- The organizing principle is explicit.
- Sections synthesize arguments rather than list papers.
- Plant-specific biology is present: species, tissue, cell type, developmental stage, environment, or crop context where relevant.
- Evidence strength and causality are bounded.
- Contradictions and gaps are named directly.
- Figures/tables/boxes help readers navigate the field.
- The final synthesis produces a unified regulatory model rather than merely repeating the preceding sections.
- The ending offers open questions and feasible next experiments, not a generic summary.
- The claim-citation matrix has no unsupported or metadata-only final citations.
- Search and screening methods match the declared review type.
- Independent plant-domain review, revision, and re-review have been completed for a finalized full review.
- The final English and Chinese manuscripts, review-response record, and literature audit have been generated as the three required Word files and passed format QA.
