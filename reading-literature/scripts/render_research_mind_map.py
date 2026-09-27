from __future__ import annotations

import argparse
import json
import math
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from PIL import Image, ImageDraw, ImageFont


PALETTE = [
    "#2F80ED",
    "#27AE60",
    "#F2994A",
    "#EB5757",
    "#9B51E0",
    "#00A7A7",
    "#6B7280",
]

STATUS_LABELS = {
    "D": "[D]",
    "A": "[A]",
    "I": "[I]",
    "C": "[C]",
    "N": "[N]",
    "direct": "[D]",
    "author": "[A]",
    "inference": "[I]",
    "conflict": "[C]",
    "not-supported": "[N]",
}

LEGEND = (
    "[D] directly demonstrated / 直接证据   "
    "[A] author model / 作者模型   "
    "[I] inference / 推断   "
    "[C] conflict / 冲突   "
    "[N] not supported / 不支持"
)


@dataclass
class Node:
    text: str
    status: str = ""
    anchor: str = ""
    color: str = "#2F80ED"
    depth: int = 0
    children: list["Node"] = field(default_factory=list)
    lines: list[str] = field(default_factory=list)
    text_width: int = 0
    text_height: int = 0
    subtree_height: int = 0
    x: int = 0
    y: int = 0

    def label(self) -> str:
        prefix = STATUS_LABELS.get(self.status, "")
        body = f"{prefix} {self.text}".strip()
        if self.anchor:
            body = f"{body} ({self.anchor})"
        return body


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Render an evidence-anchored left-to-right research mind map."
    )
    parser.add_argument("input", type=Path, help="UTF-8 JSON mind-map file")
    parser.add_argument("--output", required=True, type=Path, help="PNG output path")
    parser.add_argument("--markdown", type=Path, help="Optional Markdown outline path")
    parser.add_argument("--scale", type=int, default=2, choices=(1, 2, 3))
    return parser.parse_args()


def load_font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    windows = Path("C:/Windows/Fonts")
    bold_candidates = [
        windows / "msyhbd.ttc",
        windows / "simhei.ttf",
        windows / "arialbd.ttf",
    ]
    regular_candidates = [
        windows / "msyh.ttc",
        windows / "simsun.ttc",
        windows / "arial.ttf",
    ]
    candidates = bold_candidates if bold else regular_candidates
    candidates += [Path("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf")]
    for candidate in candidates:
        if candidate.exists():
            return ImageFont.truetype(str(candidate), size=size)
    return ImageFont.load_default()


def validate_text(value: Any, field_name: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{field_name} must be a non-empty string")
    return value.strip()


def build_node(
    raw: Any,
    *,
    depth: int,
    inherited_color: str,
    counter: list[int],
) -> Node:
    if isinstance(raw, str):
        raw = {"text": raw}
    if not isinstance(raw, dict):
        raise ValueError("each node must be a string or object")

    counter[0] += 1
    if counter[0] > 250:
        raise ValueError("mind map exceeds the 250-node safety limit")
    if depth > 6:
        raise ValueError("mind map depth exceeds the supported limit of 6")

    text = validate_text(raw.get("text"), "node.text")
    status = str(raw.get("status", "")).strip()
    if status and status not in STATUS_LABELS:
        raise ValueError(f"unsupported evidence status: {status}")
    anchor = str(raw.get("anchor", "")).strip()
    color = str(raw.get("color", inherited_color)).strip() or inherited_color
    if not color.startswith("#") or len(color) not in (4, 7):
        raise ValueError(f"invalid branch color: {color}")

    node = Node(text=text, status=status, anchor=anchor, color=color, depth=depth)
    raw_children = raw.get("children", [])
    if raw_children is None:
        raw_children = []
    if not isinstance(raw_children, list):
        raise ValueError("node.children must be a list")
    node.children = [
        build_node(
            child,
            depth=depth + 1,
            inherited_color=color,
            counter=counter,
        )
        for child in raw_children
    ]
    return node


def load_map(path: Path) -> tuple[dict[str, str], Node]:
    raw = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(raw, dict):
        raise ValueError("top-level JSON must be an object")
    title = validate_text(raw.get("title"), "title")
    subtitle = str(raw.get("subtitle", "")).strip()
    root_text = validate_text(raw.get("root"), "root")
    branches = raw.get("branches")
    if not isinstance(branches, list) or not branches:
        raise ValueError("branches must be a non-empty list")

    counter = [1]
    root = Node(text=root_text, color="#2F80ED", depth=0)
    root.children = []
    for index, branch in enumerate(branches):
        if isinstance(branch, str):
            branch = {"text": branch}
        if not isinstance(branch, dict):
            raise ValueError("each primary branch must be a string or object")
        branch = dict(branch)
        branch.setdefault("color", PALETTE[index % len(PALETTE)])
        root.children.append(
            build_node(
                branch,
                depth=1,
                inherited_color=branch["color"],
                counter=counter,
            )
        )
    return {"title": title, "subtitle": subtitle}, root


def wrap_text(
    draw: ImageDraw.ImageDraw,
    text: str,
    font: ImageFont.ImageFont,
    max_width: int,
) -> list[str]:
    lines: list[str] = []
    for paragraph in text.splitlines() or [text]:
        paragraph = paragraph.strip()
        if not paragraph:
            lines.append("")
            continue
        current = ""
        last_space = -1
        for char in paragraph:
            candidate = current + char
            width = draw.textbbox((0, 0), candidate, font=font)[2]
            if width <= max_width or not current:
                current = candidate
                if char.isspace():
                    last_space = len(current) - 1
                continue

            if last_space >= max(1, len(current) // 2):
                lines.append(current[:last_space].rstrip())
                current = current[last_space + 1 :] + char
            else:
                lines.append(current.rstrip())
                current = char.lstrip()
            last_space = current.rfind(" ")
        if current:
            lines.append(current.rstrip())
    return lines or [""]


def iter_nodes(root: Node) -> list[Node]:
    nodes = [root]
    for child in root.children:
        nodes.extend(iter_nodes(child))
    return nodes


def font_for(node: Node, scale: int) -> ImageFont.ImageFont:
    if node.depth == 0:
        return load_font(20 * scale, bold=True)
    if node.depth == 1:
        return load_font(19 * scale, bold=True)
    return load_font(15 * scale, bold=False)


def max_text_width_for_depth(depth: int, scale: int) -> int:
    widths = [220, 320, 760, 720, 700, 680, 660]
    return widths[min(depth, len(widths) - 1)] * scale


def prepare_layout(root: Node, scale: int) -> tuple[dict[int, int], int]:
    scratch = Image.new("RGB", (8, 8), "white")
    draw = ImageDraw.Draw(scratch)
    line_gap = 3 * scale
    vertical_gap = 6 * scale

    max_depth = 0
    depth_widths: dict[int, int] = {}
    for node in iter_nodes(root):
        max_depth = max(max_depth, node.depth)
        font = font_for(node, scale)
        node.lines = wrap_text(
            draw, node.label(), font, max_text_width_for_depth(node.depth, scale)
        )
        widths = []
        heights = []
        for line in node.lines:
            box = draw.textbbox((0, 0), line or " ", font=font)
            widths.append(box[2] - box[0])
            heights.append(box[3] - box[1])
        node.text_width = max(widths, default=1)
        node.text_height = sum(heights) + line_gap * max(0, len(node.lines) - 1)
        depth_widths[node.depth] = max(depth_widths.get(node.depth, 0), node.text_width)

    def measure_subtree(node: Node) -> int:
        own = max(node.text_height + 8 * scale, 28 * scale)
        if not node.children:
            node.subtree_height = own
            return own
        children_height = sum(measure_subtree(child) for child in node.children)
        children_height += vertical_gap * (len(node.children) - 1)
        node.subtree_height = max(own, children_height)
        return node.subtree_height

    measure_subtree(root)

    x_positions: dict[int, int] = {0: 60 * scale}
    horizontal_gap = 100 * scale
    for depth in range(1, max_depth + 1):
        x_positions[depth] = (
            x_positions[depth - 1]
            + depth_widths.get(depth - 1, 1)
            + horizontal_gap
        )

    def assign(node: Node, top: int) -> None:
        node.x = x_positions[node.depth]
        if not node.children:
            node.y = top + node.subtree_height // 2
            return
        children_total = sum(child.subtree_height for child in node.children)
        children_total += vertical_gap * (len(node.children) - 1)
        child_top = top + max(0, (node.subtree_height - children_total) // 2)
        for child in node.children:
            assign(child, child_top)
            child_top += child.subtree_height + vertical_gap
        node.y = (node.children[0].y + node.children[-1].y) // 2

    assign(root, 0)
    return x_positions, max_depth


def curve_points(
    start: tuple[int, int], end: tuple[int, int], samples: int = 30
) -> list[tuple[int, int]]:
    sx, sy = start
    ex, ey = end
    dx = ex - sx
    c1 = (sx + int(dx * 0.45), sy)
    c2 = (ex - int(dx * 0.45), ey)
    points = []
    for i in range(samples + 1):
        t = i / samples
        u = 1 - t
        x = (
            u**3 * sx
            + 3 * u**2 * t * c1[0]
            + 3 * u * t**2 * c2[0]
            + t**3 * ex
        )
        y = (
            u**3 * sy
            + 3 * u**2 * t * c1[1]
            + 3 * u * t**2 * c2[1]
            + t**3 * ey
        )
        points.append((round(x), round(y)))
    return points


def draw_multiline(
    draw: ImageDraw.ImageDraw,
    node: Node,
    font: ImageFont.ImageFont,
    scale: int,
    top_offset: int,
) -> None:
    line_gap = 3 * scale
    line_heights = [
        draw.textbbox((0, 0), line or " ", font=font)[3]
        - draw.textbbox((0, 0), line or " ", font=font)[1]
        for line in node.lines
    ]
    total = sum(line_heights) + line_gap * max(0, len(node.lines) - 1)
    y = node.y + top_offset - total // 2
    if node.depth == 1:
        fill = node.color
    elif node.status in ("C", "conflict", "N", "not-supported"):
        fill = "#9B1C1C"
    else:
        fill = "#111827"
    for line, height in zip(node.lines, line_heights):
        draw.text((node.x, y), line, font=font, fill=fill)
        y += height + line_gap


def render(meta: dict[str, str], root: Node, output: Path, scale: int) -> None:
    _, max_depth = prepare_layout(root, scale)
    nodes = iter_nodes(root)
    depth_widths: dict[int, int] = {}
    for node in nodes:
        depth_widths[node.depth] = max(depth_widths.get(node.depth, 0), node.text_width)

    margin = 70 * scale
    header = 112 * scale
    footer = 35 * scale
    width = max(
        1200 * scale,
        max(node.x + depth_widths.get(node.depth, 0) for node in nodes) + margin,
    )
    height = max(650 * scale, root.subtree_height + header + footer)
    if width > 14000 or height > 16000:
        raise ValueError(f"rendered map would be too large: {width}x{height}")

    image = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(image)
    title_font = load_font(28 * scale, bold=True)
    subtitle_font = load_font(16 * scale, bold=False)
    legend_font = load_font(14 * scale, bold=False)

    draw.text((margin, 24 * scale), meta["title"], font=title_font, fill="#111827")
    if meta.get("subtitle"):
        draw.text(
            (margin, 60 * scale),
            meta["subtitle"],
            font=subtitle_font,
            fill="#4B5563",
        )
    draw.text((margin, 84 * scale), LEGEND, font=legend_font, fill="#6B7280")
    draw.line(
        (margin, 104 * scale, width - margin, 104 * scale),
        fill="#E5E7EB",
        width=max(1, scale),
    )

    top_offset = header
    for parent in nodes:
        for child in parent.children:
            start = (
                parent.x + parent.text_width + 12 * scale,
                parent.y + top_offset,
            )
            end = (child.x - 15 * scale, child.y + top_offset)
            draw.line(
                curve_points(start, end),
                fill=child.color,
                width=max(2, 3 * scale),
                joint="curve",
            )
            radius = 4 * scale
            draw.ellipse(
                (end[0] - radius, end[1] - radius, end[0] + radius, end[1] + radius),
                fill=child.color,
            )

    for node in nodes:
        draw_multiline(draw, node, font_for(node, scale), scale, top_offset)

    root_radius = 8 * scale
    root_point = (root.x - 18 * scale, root.y + top_offset)
    draw.ellipse(
        (
            root_point[0] - root_radius,
            root_point[1] - root_radius,
            root_point[0] + root_radius,
            root_point[1] + root_radius,
        ),
        outline="#2F80ED",
        fill="white",
        width=max(2, 3 * scale),
    )

    if scale > 1:
        image = image.resize(
            (math.ceil(width / scale), math.ceil(height / scale)),
            Image.Resampling.LANCZOS,
        )
    output.parent.mkdir(parents=True, exist_ok=True)
    image.save(output, format="PNG", optimize=True)


def write_markdown(meta: dict[str, str], root: Node, path: Path) -> None:
    lines = [f"# {meta['title']}", ""]
    if meta.get("subtitle"):
        lines.extend([meta["subtitle"], ""])
    lines.extend([f"> {LEGEND}", "", f"- {root.label()}"])

    def append_node(node: Node, level: int) -> None:
        lines.append(f"{'  ' * level}- {node.label()}")
        for child in node.children:
            append_node(child, level + 1)

    for child in root.children:
        append_node(child, 1)
    lines.append("")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    args = parse_args()
    try:
        meta, root = load_map(args.input)
        render(meta, root, args.output, args.scale)
        if args.markdown:
            write_markdown(meta, root, args.markdown)
    except Exception as exc:
        print(f"error: {exc}", file=sys.stderr)
        raise SystemExit(1) from exc


if __name__ == "__main__":
    main()
