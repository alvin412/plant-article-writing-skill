# Evidence-Anchored Research Mind Map

## 1. Evidence Pass Before Drawing

Build the map only after reading all substantive available sections and inspecting relevant figures, tables, legends, and supplements. Create one ledger row per proposed factual leaf:

```text
Claim ID:
Concise bilingual claim:
Species, genotype, tissue or assay host:
Treatment and comparison:
Perturbation and direction:
Method and decisive control:
Exact section, page, figure, table, or supplement anchor:
Body-text result:
Legend or label result:
Plotted-value direction:
Evidence status:
Support grade:
Conflict or scope boundary:
```

When body text, captions, labels, tables, or plotted values disagree, preserve the disagreement. Mark the leaf `[C]`, explain the conflict, and avoid using it as decisive evidence until resolved.

## 2. Required Structure

Use a left-to-right map with one central paper node and seven bilingual primary branches:

1. **Research basis / 研究基础** — object, plant context, gap, question, and proposed axis; distinguish experimental species from heterologous hosts.
2. **Experimental architecture / 实验技术体系** — materials, conditions, genetic perturbations, assays, statistics, controls, and replicates.
3. **Causal results / 核心结果** — one branch per causal step, following experimental order, with source anchors on every factual leaf.
4. **Mechanistic model / 分子调控模型** — distinguish directly tested edges from working-model edges and separate molecular, biochemical, physiological, and phenotypic levels.
5. **Innovation and conclusion / 创新与结论** — separate demonstrated contribution from author novelty or translational claims.
6. **Limitations and conflicts / 局限与冲突** — missing controls, unavailable evidence, internal inconsistencies, statistical ambiguity, alternatives, and generalisation limits.
7. **Research outlook / 研究展望** — author-stated work or clearly labelled reader inferences, each with a decisive experiment.

## 3. Evidence Labels and Wording Gates

Prefix every factual or interpretive leaf with one label in both languages:

- `[D]` directly demonstrated;
- `[A]` author interpretation or working model;
- `[I]` reader inference or proposed experiment;
- `[C]` internal conflict or unresolved inconsistency;
- `[N]` not supported by the available paper.

Add a short anchor such as `(Fig. 2F-G; pp. 6-7)`. Reserve `directly binds`, `required`, `necessary`, `sufficient`, `synergistic`, `additive`, `unique`, `conserved`, `first`, and similar strong terms for designs that actually establish them. Cross-check species, assay host, perturbation direction, mutant identity, residue number, separate versus combined perturbations, statistical methods, and every plotted direction.

## 4. Supplied-Map Audit

Transcribe supplied nodes before normalising them, match every factual node to the ledger, and classify it as `accurate`, `accurate with boundary`, `needs correction`, `not supported`, or `blocked by paper conflict`. Preserve the correction record and generate a corrected map rather than delivering an unverified supplied map.

Use one overall verdict: `verified`, `verified-with-minor-edits`, `corrected`, or `blocked`.

## 5. Rendering Contract

Create canonical UTF-8 JSON containing `title`, `subtitle`, `root`, and `branches`; nodes may contain `text`, `status`, `anchor`, and `children`. Use `scripts/render_research_mind_map.py` to produce:

- the final high-resolution white-background PNG under `deliverables/`;
- an evidence-equivalent Markdown outline under `intermediate_files/evidence_maps/`.

Keep the canonical JSON under `intermediate_files/evidence_maps/`. The JSON and Markdown outline are supporting artifacts, not additional final deliverables.

Run:

```text
python scripts/render_research_mind_map.py map.json --output 01_<paper-slug>_research_mind_map.png --markdown map.md
```

Inspect the final PNG at full resolution for clipped text, overlap, broken glyphs, unsupported superscripts, and unresolved placeholders.

## 6. Completion Checks

- Full-text access and unavailable supplements are explicit.
- Every factual result leaf has a source anchor.
- Map and close-reading note use the same entities, mutant identities, conditions, and causal directions.
- Direct findings, author model, inference, conflict, and unsupported claims remain distinct.
- Supplied-map corrections are preserved in the close-reading note.
- PNG, JSON, and Markdown outline contain the same claims, while only the PNG is a final deliverable.
