# Figure quality gates

## Scientific
- Figure-level central question is explicit, and every panel adds a distinct evidentiary/interpretive role.
- All numeric values map to actual input data. Axes transformations, filtering, exclusions and units are documented.
- n denotes the correct experimental unit; avoid drawing unwarranted inference from technical replicates.
- No invented significance annotations or selective cropping; if image processing or grouping occurred, declare it.
- Hypothesized molecular edges are labeled/dashed; causal arrows need appropriate evidence.

## Visual
- Palette prioritizes the nine user-provided colors; additions have documented reasons and are consistent.
- Arial 8 pt on **English** labels and ticks. Lowercase a/b/c/d in Arial 12 pt whenever >1 panel.
- Check panel geometry, common baseline alignment, legend collisions, no clipped letters/axes, line weights, grayscale/shape differentiation.
- Verify final-size legibility by inspecting the generated PNG and vector/PDF preview. Programmatic checks alone are not visual inspection.
- Preserve true vector in SVG/PDF geometric elements; verify PDF and SVG open correctly. Raster image panels remain raster.
- If the tool cannot render or inspect, state that QA is incomplete and do not say "publication ready".

## Delivery
- Deliver three corresponding paths `*.svg`, `*.pdf`, `*.png`, a caption and source description.
- Verify dimensions, files' existence/nonempty content, PNG dpi metadata when possible, figure version, font availability and export errors.
- Flag missing journal requirements separately from scientific validity; not every figure needs a specific journal at the drafting stage.
- Re-run export and visual review after changes; protect exact data/labels against accidental modification.