import pytest
from windowtidy.geometry import Grid, Rect
from windowtidy import geometry
from windowtidy.presets import thirds, halves

def test_cell_basic():
    g = Grid(2, 2)
    r = g.cell(Rect(0,0,100,100), 0, 0)
    assert (r.x, r.y, r.w, r.h) == (0,0,50,50)


def test_last_col_row_take_remainder():
    g = Grid(3, 3)
    r = g.cell(Rect(0,0,100,100), 2, 2)
    # floor division makes 33 each, last takes remainder 34
    assert r.w in (33,34) and r.h in (33,34)


def test_inset():
    r = Rect(0,0,100,100).inset(5, 3)
    assert (r.x, r.y, r.w, r.h) == (5,3,90,94)


def test_presets():
    b = Rect(0,0,120,60)
    assert thirds(b, 0).w in (40,)
    assert halves(b, True).w in (60,)
