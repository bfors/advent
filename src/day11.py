from AdventUtils import *
import AdventUtils
import polars as pl
from itertools import combinations

AdventUtils.current_year = 2023
input11 = parse(12, parser=str.split, show=0)


def cosmic(input):
    y = 0
    gx = list()
    print(input[1])

    df = pl.DataFrame(input)
    with pl.Config(fmt_str_lengths=2000, tbl_rows=200, tbl_cols=100):
        print(df)

    prod = combinations(gx, r=2)

    s = 0
    for p in prod:
        print(p)
        g1, g2 = p
        g1x, g1y = g1
        g2x, g2y = g2
        dist = abs(g1x - g2x) + abs(g1y - g2y)
        print(dist)
        s += dist
    return s


print(answer(11.1, 0, lambda: cosmic(input11)))
