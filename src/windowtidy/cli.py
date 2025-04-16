import argparse
from .geometry import Grid, Rect
from .config import Config


def main(argv=None) -> int:
    p = argparse.ArgumentParser(prog="windowtidy", description="Quick window layout math")
    p.add_argument("cols", type=int, nargs="?")
    p.add_argument("rows", type=int, nargs="?")
    p.add_argument("col", type=int)
    p.add_argument("row", type=int)
    p.add_argument("w", type=int, help="screen width")
    p.add_argument("h", type=int, help="screen height")
    p.add_argument("x", type=int, nargs="?", default=0)
    p.add_argument("y", type=int, nargs="?", default=0)
    args = p.parse_args(argv)

    cfg = Config.load()
    cols = args.cols if args.cols is not None else cfg.grid_cols
    rows = args.rows if args.rows is not None else cfg.grid_rows
    grid = Grid(cols, rows)
    rect = grid.cell(Rect(args.x, args.y, args.w, args.h), args.col, args.row)
    print(f"{rect.x},{rect.y},{rect.w},{rect.h}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
