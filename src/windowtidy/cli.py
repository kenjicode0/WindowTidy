import argparse
from .geometry import Grid, Rect


def main(argv=None) -> int:
    p = argparse.ArgumentParser(prog="windowtidy", description="Quick window layout math")
    p.add_argument("cols", type=int)
    p.add_argument("rows", type=int)
    p.add_argument("col", type=int)
    p.add_argument("row", type=int)
    p.add_argument("w", type=int, help="screen width")
    p.add_argument("h", type=int, help="screen height")
    p.add_argument("x", type=int, nargs="?", default=0)
    p.add_argument("y", type=int, nargs="?", default=0)
    args = p.parse_args(argv)

    grid = Grid(args.cols, args.rows)
    rect = grid.cell(Rect(args.x, args.y, args.w, args.h), args.col, args.row)
    print(f"{rect.x},{rect.y},{rect.w},{rect.h}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

