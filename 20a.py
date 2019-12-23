import sys
from collections import defaultdict, namedtuple
from copy import copy
from string import ascii_uppercase


Position = namedtuple('Position',['x','y'])

def main():
    if len(sys.argv) == 1:
        filename = "20-input.txt"
    else:
        filename = sys.argv[1]

    letters = ascii_uppercase

    maze = defaultdict(str)
    portals = defaultdict(list)

    maze_text = get_input(filename)

    for y, line in enumerate(maze_text.split("\n")):
        for x, c in enumerate(line.strip("\n")):
            maze[Position(x, y)] = c
    width = x
    height = y

    to_check = set(maze.keys())
    for pos in to_check:
        c = maze[pos]

        if c and c in letters:
            x,y = pos
            if (
                maze[Position(x + 1, y)] and maze[Position(x + 1, y)] in letters
            ):  # We are at the first letter in a horizontally named portal
                name = maze[Position(x, y)] + maze[Position(x + 1, y)]
                if maze[Position(x - 1, y)] == ".":
                    new_pos = (x, y)
                elif maze[Position(x + 2, y)] == ".":
                    new_pos = (x + 1, y)
                portals[name].append(new_pos)
            elif (
                maze[Position(x, y + 1)] and maze[Position(x, y + 1)] in letters
            ):  # We are at the first letter in a vertically named portal
                name = maze[Position(x, y)] + maze[Position(x, y + 1)]
                if maze[Position(x, y - 1)] == ".":
                    new_pos = (x, y)
                elif maze[Position(x, y + 2)] == ".":
                    new_pos = (x, y + 1)
                portals[name].append(new_pos)

    teleport = {}
    for name in portals:
        if len(portals[name]) == 2:
            teleport[portals[name][0]] = portals[name][1]
            teleport[portals[name][1]] = portals[name][0]
    start = portals["AA"][0]
    end = portals["ZZ"][0]

    steps = -1  # Start on AA adjacent to maze, first step takes us to beginning
    seen = set()
    seen.add(start)
    positions = set()
    positions.add(start)
    finished = False
    while  not finished:
        steps += 1
        next_positions = set()
        for pos in positions:
            for step_to in can_step_to(pos, maze,teleport,end):
                if step_to not in seen:
                    seen.add(step_to)
                    next_positions.add(step_to)
                    if end in next_positions:
                        finished = True
        positions = next_positions
        #print_maze(maze,positions,steps,width,height)
    print(f"Took {steps -1} steps.") # Do not actually need to step out of maze, just reach exit


def can_step_to(pos, maze,teleport,end):
    movements = ((1, 0), (-1, 0), (0, 1), (0, -1))
    valid_positions = []
    x,y = pos
    for m in movements:
        dx, dy = m
        to_x, to_y = x + dx, y + dy
        if (to_x, to_y) in teleport:
            (to_x, to_y) = can_step_to(teleport[(to_x, to_y)], maze,teleport,end)[0]
        if maze[(to_x, to_y)] == "." or (to_x,to_y) == end:
            valid_positions.append((to_x, to_y))
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
