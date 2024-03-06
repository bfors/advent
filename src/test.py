from AdventUtils import *
from collections import Counter
import AdventUtils

AdventUtils.current_year = 2023
import polars as pl
from itertools import combinations

input = parse(12, parser=list, show=0)
df: pl.DataFrame = pl.DataFrame(input)

for i, c in enumerate(df.get_columns()):
    if len(c.value_counts().rows()) == 1:
        s = pl.Series(str(i), len(c) * ".")
        df.insert_column(i, s)

gx = set()
for row in df.iter_rows():
    print(row)
    if len(set(row)) == 1:
        print(list(len(row) * "."))


# with pl.Config(fmt_str_lengths=2000, tbl_rows=200, tbl_cols=100):
#     print(df)
