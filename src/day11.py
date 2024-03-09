from AdventUtils import *
import AdventUtils
from itertools import combinations

AdventUtils.current_year = 2023
input = parse(11, parser=list, show=0)


def cosmic(input, exp=1):
    galaxies = []

    # Keep index of expanded space
    y_expansion = []
    x_expansion = []

    # scan rows
    y = 0
    for line in input:
        y_expansion.append(y)
        if line == len(line) * ["."]:
            y += exp
        else:
            y += 1

    # scan columns
    x = 0
    for i in range(len(input[0])):
        x_expansion.append(x)
        col = [p[i] for p in input]
        if col == len(col) * ["."]:
            x += exp
        else:
            x += 1

    for y, line in enumerate(input):
        for x, c in enumerate(line):
            if c == "#":
                galaxies.append((x_expansion[x], y_expansion[y]))

    prod = combinations(galaxies, r=2)
    s = 0
    for p in prod:
        galaxy1, galaxy2 = p
        g1x, g1y = galaxy1
        g2x, g2y = galaxy2
        dist = abs(g1x - g2x) + abs(g1y - g2y)
        s += dist
    return s


print(answer(11.1, 9724940, lambda: cosmic(input, 2)))
print(answer(11.2, 9724940, lambda: cosmic(input, 1000000)))
