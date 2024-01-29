from AdventUtils import *
import AdventUtils
AdventUtils.current_year = 2023

def move(location, up=0, down=0, left=0, right=0):
    y = right - left
    x = down - up
    return tuple(map(sum, zip(location, (x,y))))

def get_coordinates(grid, loc):
    return [t for t in [move(loc, up=1), move(loc, down=1), move(loc,left=1), move(loc,right=1)] if t in grid]

def pipe(input):
    grid = {}
    start = (-1, -1)
    for i, line in enumerate(input.splitlines()):
        for j, c in enumerate(line):
            grid[(i,j)] = c
            if c == 'S':
                start = (i,j)

    path = [start]
    location = start

    coordinates = get_coordinates(grid, location)
    location = move(location, up=1)
    path.append(location)

    while path[-1] != start:
        next = get_adjacents(grid, path)
        path.append(next)

    s = set(path)
    for i, line in enumerate(input.splitlines()):
        l = []
        for j, c in enumerate(line):
            if (i,j) in s:
                l.append('X')
            else:
                l.append(c)
        print(''.join(l))

    return len(path)//2
        

def get_adjacents(grid, path):
    location = path[-1]
    current = grid[location]
    next = ()
    if current == '|': 
        next = (move(location, up=1), move(location, down=1))
    elif current == 'L':
        next = (move(location, up=1), move(location, right=1))
    elif current == '-':
        next = (move(location, left=1), move(location, right=1))
    elif current == 'F':
        next = (move(location, down=1), move(location, right=1))
    elif current == '7':
        next = (move(location, down=1), move(location, left=1))
    elif current == 'J':
        next = (move(location, left=1), move(location, up=1))

    return next[1] if next[1] != path[-2] else next[0]


filename = '../inputs/2023/input10.txt'
input10 = pathlib.Path(filename).read_text()

print(answer(10.1, 6942, lambda: pipe(input10)))
