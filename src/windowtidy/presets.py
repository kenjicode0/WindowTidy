from .geometry import Grid, Rect


def thirds(bounds: Rect, index: int) -> Rect:
    g = Grid(3, 1)
    return g.cell(bounds, index, 0)


def halves(bounds: Rect, left: bool) -> Rect:
    g = Grid(2, 1)
    return g.cell(bounds, 0 if left else 1, 0)

