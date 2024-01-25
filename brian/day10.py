from AdventUtils import *
import AdventUtils
AdventUtils.current_year = 2023

def move(location, up=0, down=0, left=0, right=0):
    y = right - left
    x = down - up
    return tuple(map(sum, zip(location, (x,y))))

def get_coordinates(grid, loc):
    return [t for t in [move(loc, up=1), move(loc, down=1), move(loc,left=1), move(loc,right=1)] if t in grid]

def get_next(grid, coordinates):



def pipe(input):

    # Load entire grid into a map
    # Find start
    # Pick valid direction
    # while n is not S
        # record path
        # goto next valid direction

    grid = defaultdict(dict)
    start = (-1, -1)
    for i, line in enumerate(input.splitlines()):
        l = []
        for j, c in enumerate(line):
            grid[(i,j)] = c
            if c == 'S':
                start = (i,j)

    path = [start]
    location = start
    val = ''

    valid_left = {'L', '-', 'F'}
    valid_right = {'-', 'J', '7'}
    valid_up = {'|', '7', 'F'}
    valid_down = {'|', 'J', 'L'}

    print(f'start: {start}')
    coordinates = get_coordinates(grid, location)
    print(get_next(grid, coordinates))



filename = '../inputs/2023/input10.txt'
input10 = pathlib.Path(filename).read_text()

answer(10.1, 0, lambda: pipe(input10)) 
