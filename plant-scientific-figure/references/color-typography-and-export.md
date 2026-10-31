# Mandatory publication figure style / 强制科研图件样式

## Palette
Priority order (retain exact hex casing for documentation):
1. `#FA7F6F`
2. `#FFBE7A`
3. `#8ECFC9`
4. `#A6A6D2`
5. `#F4A7B9`
6. `#FC757B`
7. `#FFE59B`
8. `#3C9BC9`
9. `#82B0D2`

Use these sequentially for distinct categories when suitable. For >9 categories or insufficient contrast, synthesize additional hues with documented deterministic rules and inspect perceptual distinctness; never silently recolor the requested nine swatches. On dark backgrounds/continuous scales, request permission for a contrast-appropriate modification; semantic warning colors may require separate explanation. Pair colors with line types/markers and verify grayscale accessibility.

## Typography
- Every English figure label, legend entry, tick label, annotation, axis label and graph node: Arial, **8 pt**, measured at intended final physical size.
- For multiple panels, identifiers are italic-free lowercase letters `a`, `b`, `c`, `d` and so on, Arial **12 pt**; align identical top-left anchors; do not write `(A)` or uppercase `A`.
- Do not include a large decorative headline inside the plot; the figure caption should ordinarily be separate.
- Chinese required in a figure: choose available CJK font for Han characters; keep ASCII and digits Arial, and warn if CJK font is missing. Word body typography rules (SimSun/Times New Roman) are **not** the same as figure typography.
- At final size, do not shrink fonts after rendering to fit a page. Resolve congestion by redesigning, simplifying labels or dividing panels.

## File formats and output
- Required triplet: true-source `.svg`, vector-first `.pdf`, rasterized `.png`.
- SVG should retain text elements (`svg.fonttype = none` for Matplotlib) and editable geometric shapes; record when fonts are not embedded.
- PDF should use TrueType embedding when supported (`pdf.fonttype = 42`); verify actual font selection.
- PNG should export at >=300 dpi by default, with preserved dimensions and no resampling after labels are placed.
- For source microscopy/photo panels, bitmap regions remain bitmap **even in SVG/PDF**. Never claim full-vector conversion.
- Export reproducible input spec, scripts and data-source ledger (if permission allows) with units/normalization/exclusions.
- If Arial is not installed, do not quietly substitute Liberation Sans or DejaVu Sans and claim compliance. Report a FONT_BLOCK and instruct the user to install/select Arial with appropriate rights.

## Rendering reference
```bash
python scripts/render_figure.py input_spec.json --output-base deliverables/figure1
```
Produces `figure1.svg`, `figure1.pdf`, `figure1.png` plus `figure1_qa.json` on successful export. Script supports common line/scatter/bar/box panels and simple mechanism diagrams; advanced publication artwork should follow the same contract in a suitable rendering environment.