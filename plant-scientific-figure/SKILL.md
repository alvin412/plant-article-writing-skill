---
name: plant-scientific-figure
description: "Design, draw, revise and validate plant-science data figures, mechanistic diagrams, pathways, workflows and multipanel publication figures. Understand the scientific purpose first; ask targeted questions if ambiguity changes the figure; export SVG, PDF and PNG."
---

# Plant Scientific Figure | 植物科研绘图

## First understand; then draw
Do **not** start from a chart template or decorative styling. Read `references/figure-contract.md` and establish (a) the single central scientific message, (b) source observations and evidence status, (c) intended readers and figure type, (d) each panel's unique evidence/logic role, (e) target dimensions and journal constraints if supplied.

If the purpose, crucial labels, data meaning, or mechanism direction cannot be inferred reliably, ask **1–3 focused questions** before drawing. Do not block if the user already provided an unambiguous brief. If the uncertainty is immaterial, state the assumption and proceed. For a conceptual diagram, separate validated interactions (solid lines) and hypotheses (dashed lines) with a clear legend; never turn a proposed mechanism into an observed fact.

## Figure types
- Data-backed: dots/scatter, time or dose curves, distributions/boxplots, grouped comparisons, heatmaps, omics summaries and multi-panel Results figures. Choose truthful encodings based on sample sizes, experimental units, distributions and data type.
- Schematic: gene regulation, protein interaction, signaling, plant physiological processes, workflows, experimental design, genetic models and graphical abstracts. Use only substantiated or explicitly hypothesis-marked arrows.
- Mixed: arrange quantitative panels plus an explanatory mechanism. Preserve original data/image provenance; a raster photograph inserted in a PDF/SVG container does not become vector.

## Fixed visual contract
Read `references/color-typography-and-export.md`.
- Ordered priority palette **exactly**:
  `#FA7F6F #FFBE7A #8ECFC9 #A6A6D2 #F4A7B9 #FC757B #FFE59B #3C9BC9 #82B0D2`.
  Prefer these first; if more distinct series or special semantic colors are truly necessary, algorithmically append documented colors compatible with the palette. No unsanctioned default rainbow/jet.
- English figure text: **Arial 8 pt at final export size**. Multi-panel identifiers: lowercase **a, b, c, d ...**, **Arial 12 pt**, at a consistent top-left anchor. Do not silently change these sizes for journal templates; disclose conflicts and obtain a decision.
- If Chinese figure text is explicitly required, render CJK glyphs with an available Chinese font, while keeping Western/digit runs Arial 8 pt; warn if correct font rendering cannot be verified.
- Preserve accessible distinctions by shape, line style or direct labels, not color alone. Confirm grayscale/color-vision legibility.

## Deliverables
Unless the user explicitly asks for a subset, export **all three** `figure.svg` (editable vector geometry/text where possible), `figure.pdf` (vector-first printable version) and `figure.png` (300 dpi or target-journal requirement). Also provide the figure caption/legend, the script or vector source, input-data provenance and a visual-QA status report. Never claim "full vector" for embedded bitmap imagery.

## Workflow
`PURPOSE -> DATA/MECHANISM AUDIT -> FIGURE PLAN -> (CLARIFICATION if needed) -> PLOT/DRAW -> VISUAL QA -> EXPORT SVG+PDF+PNG -> VERIFY -> DELIVER`.
- Load `references/quality-gates.md` before final delivery.
- Use `scripts/render_figure.py` for supported reproducible plots/schematics from a structured JSON spec. For unsupported figures use suitable vector graphics tooling without fabricating data, and keep the same contract.
- No fake datapoints, p-values, biological interactions, images, controls, labels or citations. Retain missing-value exclusions and transformation rules. Respect user-provided unpublished source-data permissions.
- For an unspecified journal use these exact defaults. For a named journal verify its current requirements, but preserve user-mandated colors/fonts unless the user approves an explicit override.

## Integration
- `reading-literature` validates source-backed biological mechanisms.
- `plant-experimental-design` may contribute conceptual experiments when available.
- `plant-research-article` provides verified Results and Figure-to-Claim mapping.
- `plant-review-article` provides evidence-bounded synthesis models.
- `plant-peer-review` may audit figures but does not redraw them unless asked.