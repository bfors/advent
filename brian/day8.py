from AdventUtils import *
import AdventUtils

AdventUtils.current_year = 2023

def haunted(input):
    instructions = input[0]
    nodes = input[2:]

    d = {}
    node: str
    for node in nodes:
        element = node.split(" ")[0]
        L = node[node.find("(") + 1 : node.find(",")]
        R = node[node.find(", ") + 2 : node.find(")")]
        d[element] = {"L": L, "R": R}

    current = "AAA"
    steps = 0
    while True:
        if current == "ZZZ":
            return steps
        circular_index = steps % len(instructions)
        current = d[current][instructions[circular_index]]
        steps += 1

in8 = parse(8, show=0)
print(answer(8.1, 16897, lambda: haunted(in8)))


