"""House style for every figure in the book, so 100+ figures drawn by different agents read as one system.

Usage, from a per-chapter script tools/figures/chNN.py:

    import sys, os; sys.path.insert(0, os.path.dirname(__file__))
    from style import *            # applies the rcParams on import
    fig, ax = new_figure()         # "wide" 7x3.6 in; "square" 5x5; "tall" 6x6.5
    ax.plot(x, y, color=SERIES[0]); label_end(ax, x[-1], y[-1], "Spread", SERIES[0])
    finish(fig, "ch05_default_densities")   # -> assets/figures/ch05_default_densities.png

Rules (the dataviz method; the palette was validated with its validator, light mode):
- No in-image title. The Markdown caption is the title: ![Figure 5.2: ...](assets/figures/ch05_x.png)
  Put units in axis labels ("Spread (bp)", "Years to maturity"). Put the source in the caption
  ("Source: FRED BAMLH0A0HYM2" or "Illustrative: simulated from the model in §5.3").
- Categorical colors go in FIXED ORDER: SERIES[0], SERIES[1], ... never cycled, never by rank.
  A series keeps its color across every figure in a chapter. More than 8 series: fold into "Other"
  or use small multiples. Scatter or bubble charts: at most 3 colored groups.
- Slots 3-5 (aqua, yellow, magenta) are below 3:1 contrast on white, so any figure that uses them
  must direct-label the marks (label_end) as well as carry a legend.
- One y-axis. Never twinx(). Two measures of different scale -> two panels (new_figure(ncols=2)).
- Sequential magnitude = one hue (SEQ_BLUE, light to dark). Polarity = DIVERGING (blue, gray, red).
- STATUS colors (good/warning/serious/critical) are reserved for state and never stand in for a
  series; pair them with a text label.
- Text is ink (INK, INK_2, MUTED), never a series color; a colored mark beside the text carries identity.
- Thin marks: lines LW (1.6 pt); markers >= 5 pt; bars with a white gap; grid recessive (y only).
- Annotate sparingly: event lines (mark_event) and a few direct labels, never a number on every point.
- Real data only if it is sourced (dossier or public dataset) and cited in the caption; otherwise
  generate it from a stated model and say "Illustrative" in the caption. Never invent "real" numbers.
- Save with finish(): PNG at 150 dpi, white background, under 500 KB. Always open the PNG and look
  at it before embedding (label collisions, clipped text, overflow).
"""
import os

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.colors import LinearSegmentedColormap  # noqa: E402

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
OUT_DIR = os.path.join(ROOT, "assets", "figures")

SURFACE = "#ffffff"
INK = "#0b0b0b"        # primary text
INK_2 = "#52514e"      # secondary text, axis labels
MUTED = "#8a8984"      # tick labels, notes
GRID = "#e6e5e1"
NEUTRAL = "#b9b8b2"    # de-emphasised series, reference lines

# Categorical, fixed order (validated: worst adjacent CVD dE 9.1, normal-vision dE 19.6).
SERIES = ["#2a78d6", "#eb6834", "#1baf7a", "#eda100", "#e87ba4", "#008300", "#6250d6", "#e34948"]
BLUE, ORANGE, AQUA, YELLOW, MAGENTA, GREEN, VIOLET, RED = SERIES

SEQ_BLUE_STEPS = ["#cde2fb", "#b7d3f6", "#9ec5f4", "#86b6ef", "#6da7ec", "#5598e7", "#3987e5",
                  "#2a78d6", "#256abf", "#1c5cab", "#184f95", "#104281", "#0d366b"]
SEQ_BLUE = LinearSegmentedColormap.from_list("book_seq_blue", SEQ_BLUE_STEPS)
DIVERGING = LinearSegmentedColormap.from_list("book_diverging", ["#104281", "#3987e5", "#f0efec", "#e66767", "#a8201f"])

STATUS = {"good": "#0ca30c", "warning": "#fab219", "serious": "#ec835a", "critical": "#d03b3b"}

LW = 1.6

plt.rcParams.update({
    "figure.facecolor": SURFACE, "axes.facecolor": SURFACE, "savefig.facecolor": SURFACE,
    "font.family": "DejaVu Sans", "font.size": 9.5,
    "axes.labelsize": 9.5, "axes.labelcolor": INK_2, "axes.titlesize": 10, "axes.titlecolor": INK,
    "axes.titleweight": "semibold", "axes.titlelocation": "left",
    "axes.edgecolor": NEUTRAL, "axes.linewidth": 0.8,
    "axes.spines.top": False, "axes.spines.right": False,
    "axes.grid": True, "axes.grid.axis": "y", "grid.color": GRID, "grid.linewidth": 0.7,
    "axes.prop_cycle": matplotlib.cycler(color=SERIES),
    "xtick.color": MUTED, "ytick.color": MUTED, "xtick.labelcolor": INK_2, "ytick.labelcolor": INK_2,
    "xtick.labelsize": 8.5, "ytick.labelsize": 8.5,
    "lines.linewidth": LW, "lines.markersize": 5, "patch.linewidth": 0,
    "legend.frameon": False, "legend.fontsize": 8.5, "legend.labelcolor": INK_2,
    "text.color": INK, "mathtext.fontset": "dejavusans",
})

SIZES = {"wide": (7.0, 3.6), "square": (5.0, 5.0), "tall": (6.0, 6.5), "panel2": (7.0, 3.2)}


def new_figure(size="wide", nrows=1, ncols=1, **kw):
    """A figure in the house size, with constrained layout. Returns (fig, ax or array of axes)."""
    w, h = SIZES.get(size, size) if isinstance(size, str) else size
    if ncols == 2 and size == "wide":
        w, h = SIZES["panel2"]
    fig, ax = plt.subplots(nrows, ncols, figsize=(w, h), layout="constrained", **kw)
    return fig, ax


def label_end(ax, x, y, text, color, dx=4, dy=0, **kw):
    """Direct label at the end of a line: a small colored dot carries identity, the text stays ink."""
    ax.plot([x], [y], "o", color=color, markersize=4, zorder=5, clip_on=False)
    ax.annotate(text, (x, y), xytext=(dx, dy), textcoords="offset points", va="center",
                fontsize=8.5, color=INK_2, **kw)


def mark_event(ax, x, text, y_frac=0.96, color=NEUTRAL):
    """A dated event: thin dashed vertical line with a short label near the top."""
    ax.axvline(x, color=color, linewidth=0.9, linestyle=(0, (3, 3)), zorder=1)
    ax.annotate(text, (x, y_frac), xycoords=("data", "axes fraction"), xytext=(3, 0),
                textcoords="offset points", fontsize=8, color=INK_2, va="top")


def note(ax, text, loc="lower left"):
    """A short muted note inside the axes (e.g., parameter values)."""
    x, ha = (0.01, "left") if "left" in loc else (0.99, "right")
    y, va = (0.02, "bottom") if "lower" in loc else (0.98, "top")
    ax.text(x, y, text, transform=ax.transAxes, ha=ha, va=va, fontsize=8, color=MUTED)


def finish(fig, name, dpi=150, max_kb=500):
    """Save assets/figures/<name>.png and enforce the size budget. Returns the path relative to the repo."""
    os.makedirs(OUT_DIR, exist_ok=True)
    path = os.path.join(OUT_DIR, f"{name}.png")
    fig.savefig(path, dpi=dpi)
    plt.close(fig)
    kb = os.path.getsize(path) / 1024
    if kb > max_kb:
        raise SystemExit(f"{name}.png is {kb:.0f} KB (> {max_kb} KB): simplify it or lower the dpi")
    rel = os.path.relpath(path, ROOT)
    print(f"wrote {rel} ({kb:.0f} KB)")
    return rel


__all__ = ["plt", "SURFACE", "INK", "INK_2", "MUTED", "GRID", "NEUTRAL", "SERIES", "BLUE", "ORANGE", "AQUA",
           "YELLOW", "MAGENTA", "GREEN", "VIOLET", "RED", "SEQ_BLUE", "SEQ_BLUE_STEPS", "DIVERGING", "STATUS",
           "LW", "new_figure", "label_end", "mark_event", "note", "finish"]
