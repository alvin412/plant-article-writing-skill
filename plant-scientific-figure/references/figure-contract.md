# Figure reasoning contract / 科学目的优先

Before drawing, record:
1. **Figure-level claim/question:** What exactly should the reader learn? Separate question from hoped-for conclusion.
2. **Audience and role:** main Results figure, review mechanism, experimental workflow, graphical abstract, supplemental evidence or exploratory figure.
3. **Source evidence:** files/dataset, version, units, identity of true independent replicates, image provenance, study material and conditions; flag unverified input.
4. **Panel map:** panel letter, individual question, evidence type, input source, intended encoding, axes/labels, needed controls, relation to overall claim.
5. **Interpretation boundary:** observational, functional, direct binding, causal or hypothetical; never upgrade claim strength by arrows/colors alone.
6. **Delivery:** final physical size (inch/mm), reading order, output paths, accessibility, palette/font instructions, journal instructions if verified.

## Clarification policy
Ask up to 3 questions only when a wrong assumption would change the scientific meaning or chart type. Examples:
- "这张图希望重点证明组间差异，还是描述处理后的时间响应？"
- "连接 A 与 B 的箭头是已经验证的直接调控，还是尚待验证的假设？"
- "这些点代表独立植株、独立盆、技术重复还是单个细胞？"

If supplied data already determines a defensible representation, proceed. When no data were supplied for a numeric plot, request data or deliver a clearly labeled empty design mockup **without fabricated observations**.

## Encoding rules
- Discrete groups with small n: show individual points when possible; a bar mean alone can hide the data.
- Time, ordered doses: connected lines when there is an ordered independent variable; unrelated category groups should not be joined.
- Heatmaps: record scale, normalization, missingness and source matrix; label transformations.
- Statistical marks only from verified test results, with test, n, uncertainty and multiple-comparison treatment in the legend.
- Graphical abstracts and mechanisms: specify which arrow styles represent known or predicted relationships.
- Use layouts, not extra graphics, to focus attention. One main story per figure.

Inspired by independent scientific-design principles discussed at:
- https://github.com/Haojae/scipilot-figure-skill
- https://github.com/Yuan1z0825/nature-skills/tree/main/skills/nature-figure
This reference is newly authored for this plant-science suite.