from dataclasses import dataclass


@dataclass(frozen=True)
class Rect:
    x: int
    y: int
    w: int
    h: int

    def inset(self, dx: int, dy: int) -> "Rect":
        return Rect(self.x + dx, self.y + dy, max(0, self.w - 2 * dx), max(0, self.h - 2 * dy))


class Grid:
    def __init__(self, cols: int, rows: int):
        if cols <= 0 or rows <= 0:
            raise ValueError("cols and rows must be positive")
        self.cols = cols
        self.rows = rows

    def cell(self, bounds: Rect, col: int, row: int) -> Rect:
        if not (0 <= col < self.cols and 0 <= row < self.rows):
            raise IndexError("cell out of range")
        cw = bounds.w // self.cols
        ch = bounds.h // self.rows
        x = bounds.x + col * cw
        y = bounds.y + row * ch
        # last column/row takes the remainder to avoid gaps
        w = cw if col < self.cols - 1 else bounds.w - (self.cols - 1) * cw
        h = ch if row < self.rows - 1 else bounds.h - (self.rows - 1) * ch
        return Rect(x, y, w, h)

