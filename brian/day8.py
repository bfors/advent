from AdventUtils import *
import AdventUtils
from math import lcm
AdventUtils.current_year = 2023

def get_dict(nodes):
    d = {}
    node: str
    for node in nodes:
        element = node.split(" ")[0]
        L = node[node.find("(") + 1 : node.find(",")]
        R = node[node.find(", ") + 2 : node.find(")")]
        d[element] = {"L": L, "R": R}
    return d

def haunted(input):
    instructions = input[0]
    nodes = input[2:]
    d = get_dict(nodes)

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

def haunted2(input):
    instructions = input[0]
    nodes = input[2:]
    d = get_dict(nodes)

    starters = [key for key in d.keys() if key[2] == 'A']
    steparr = []
    for starter in starters:
        steps = 0
        current = starter
        while True:
            if current[2] == "Z":
                steparr.append(steps)
                print(f'{starter}: {steps}')
                break
            circular_index = steps % len(instructions)
            current = d[current][instructions[circular_index]]
            steps += 1
    return lcm(*steparr)


print(answer(8.2, 16563603485021, lambda: haunted2(in8)))



