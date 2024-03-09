from AdventUtils import *
import AdventUtils

AdventUtils.current_year = 2023


def hotsprings(input):
    for line in input:
        print(line)
    ...


input = parse(12, show=0)
answer(12.1, 1, lambda: hotsprings(input))
