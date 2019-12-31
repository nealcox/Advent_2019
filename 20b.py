import sys
from collections import defaultdict, namedtuple
from copy import copy
from string import ascii_uppercase


Position = namedtuple('Position',['x','y'])
Position3 = namedtuple('Position3',['x','y','z'])

def main():
    if len(sys.argv) == 1:
        filename = "20-input.txt"
    else:
        filename = sys.argv[1]

    letters = ascii_uppercase

    blank_maze = defaultdict(str)
    portals = defaultdict(list)

    maze_text = get_input(filename)

    for y, line in enumerate(maze_text.split("\n")):
        for x, c in enumerate(line.strip("\n")):
            blank_maze[Position(x, y)] = c
    width = x
    height = y
    min_z = max_z = z = 0
    inners = set()
    outers = set()

    to_check = set(blank_maze.keys())
    for pos in to_check:
        c = blank_maze[pos]

        if c and c in letters:
            x,y = pos
            if (
                blank_maze[Position(x + 1, y)] and blank_maze[Position(x + 1, y)] in letters
            ):  # We are at the first letter in a horizontally named portal
                name = blank_maze[Position(x, y)] + blank_maze[Position(x + 1, y)]
                if blank_maze[Position(x - 1, y)] == ".":
                    new_pos = Position(x, y)
                elif blank_maze[Position(x + 2, y)] == ".":
                    new_pos = Position(x + 1, y)
                portals[name].append(new_pos)
                if new_pos.x == 1 or new_pos.x == (width - 1):
                    outers.add(new_pos)
                else:
                    inners.add(new_pos)
            elif (
                blank_maze[Position(x, y + 1)] and blank_maze[Position(x, y + 1)] in letters
            ):  # We are at the first letter in a vertically named portal
                name = blank_maze[Position(x, y)] + blank_maze[Position(x, y + 1)]
                if blank_maze[Position(x, y - 1)] == ".":
                    new_pos = Position(x, y)
                elif blank_maze[Position(x, y + 2)] == ".":
                    new_pos = Position(x, y + 1)
                portals[name].append(new_pos)
                if new_pos.y == 1 or new_pos.y == (height - 2):
                    outers.add(new_pos)
                else:
                    inners.add(new_pos)

    teleport = {}
    for name in portals:
        if len(portals[name]) == 2:
            teleport[portals[name][0]] = portals[name][1]
            teleport[portals[name][1]] = portals[name][0]
    start = Position3(*portals["AA"][0],0)
    end = Position3(*portals["ZZ"][0],0)

    steps = -1  # Start on AA adjacent to maze, first step takes us to beginning
    seen = set()
    seen.add(start)
    positions = set()
    positions.add(start)
    finished = False
    maze = copy(blank_maze)
    while  not finished:
        steps += 1
        next_positions = set()
        for pos in positions:
            for step_to in can_step_to(pos, maze,teleport,end,inners):
                if step_to not in seen:
                    seen.add(step_to)
                    next_positions.add(step_to)
                    if end in next_positions:
                        finished = True
        positions = next_positions
        print(f"After {steps} steps, positions to check:\n{positions}")
        #print_maze(maze,positions,steps,width,height)
    print(f"Took {steps -1} steps.") # Do not actually need to step out of maze, just reach exit


def can_step_to(pos, maze,teleport,end,inners):
    movements = ((1, 0), (-1, 0), (0, 1), (0, -1))
    valid_positions = []
    x,y,z = pos
    for m in movements:
        dx, dy = m
        dz = 0
        to_x, to_y = x + dx, y + dy
        to_z = z
        if (to_x, to_y) in teleport:
            if (to_x,to_y) in inners:
                dz = 1
            else:
                dz = -1
            to_z = z + dz
            if to_z >= 0:
                go_to = can_step_to(Position3(*teleport[(to_x, to_y)],to_z), maze,teleport,end,inners)
                if go_to:
                    (to_x, to_y,to_z) = can_step_to(Position3(*teleport[(to_x, to_y)],to_z), maze,teleport,end,inners)[0]
        if maze[(to_x, to_y)] == "." or (to_x,to_y,to_z) == end:
            valid_positions.append((to_x, to_y,to_z))
    valid_positions = [ (x,y,z) for (x,y,z) in valid_positions if z >= 0 ]
    return valid_positions

def print_maze(maze,positions,steps,width,height):
    print(f"After {steps} steps:")
    for y in range(height):
        for x in range(width):
            if (x,y) in positions:
                print("X", end = "")
            else:
                print(maze[(x,y)],end="")
        print()
    print()
    print()

    

def get_input(filename):
    with open(filename) as f:
        inputs = f.read()
    return inputs


if __name__ == "__main__":
    main()
