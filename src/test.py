from AdventUtils import *
import AdventUtils

AdventUtils.current_year = 2023
import polars as pl
from itertools import combinations

input = parse(12, parser=list, show=0)
df: pl.DataFrame = pl.DataFrame(input)

with pl.Config(fmt_str_lengths=2000, tbl_rows=200, tbl_cols=100):
    print(df)

for i, c in enumerate(df.get_columns()):
    series = pl.Series("", len(c) * ".")
    with pl.Config(fmt_str_lengths=2000, tbl_rows=200, tbl_cols=100):
        print(c)
        print(series)
    if c.equals(series):
        print("we are equal")
        s = pl.Series(len(c) * ".")
        df.insert_column(i, s)
    print()
