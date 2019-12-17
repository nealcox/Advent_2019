import sys
from collections import defaultdict
from itertools import permutations
from intcode_machine import IntcodeMachine

movements = {"N": (0, -1), "E": (1, 0), "S": (0, 1), "W": (-1, 0)}


def main():
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = "17-input.txt"
    machine = IntcodeMachine()
    machine.load_memory(filename)

    finished = False
    while not finished:
        result = machine.run_program()
        if isinstance(result, int):
            finished = True
        elif result == "Awaiting Input":
            input(f"(pc = {machine.pc})?")
        else:
            raise ValueError(f"Unknown return value {result}")
    space = "".join(chr(s) for s in machine.outputs).strip().split(chr(10))
    for line in space:
        print(line)
    for r, line in enumerate(space):
        for c, char in enumerate(line):
            if char in "^>v<":
                x = c
                y = r
                "^>v<".index(char)
                facing = "NESW"["^>v<".index(char)]
                print(f"Robot {char} at {(c,r)}, facing {facing}.")
    search(x, y, facing, space)


def search(x, y, facing, space):
    width = len(space[0])
    height = len(space)
    print("Tracing path...")
    dx, dy = movements[facing]
    #    print(f"At, {x,y}, facing {facing}, dx,dy = {dx,dy}")
    finished = False
    distance = 0
    while not finished:
        next_x = x + dx
        next_y = y + dy
        #        print(f"At, {x,y}, facing {facing}, dx,dy = {dx,dy}")
        #        if (0<=next_x<width) and (0<=next_y<height):
        #            print(f"Forward {next_x,next_y} is {space[next_y][next_x]}")
        #        else:
        #            print(f"Can't move forward")
        if (
            (0 <= next_x < width)
            and (0 <= next_y < height)
            and (space[next_y][next_x] == "#")
        ):
            #            print(f"Moving forward")
            distance += 1
            x, y = next_x, next_y
        elif (
            not (0 < next_x < width)
            or not (0 < next_y < height)
            or space[next_y][next_x] == "."
        ):
            print(distance, end=",")
            distance = 1
            # Look left
            dx, dy, f = turn_left(facing)
            next_x = x + dx
            next_y = y + dy
            #            if (0<=next_x<width) and (0<=next_y<height):
            #                print(f"Left, {next_x,next_y} is {space[next_y][next_x]}")
            #            else:
            #                print(f"Left, {next_x,next_y} is outside space")
            if (
                (0 <= next_x < width)
                and (0 <= next_y < height)
                and space[next_y][next_x] == "#"
            ):
                print("L", end=",")
                facing = f
                x, y = next_x, next_y
            else:
                # Look right
                dx, dy, f = turn_right(facing)
                next_x = x + dx
                next_y = y + dy
                #                if (0<=next_x<width) and (0<=next_y<height):
                #                    print(f"Left, {next_x,next_y} is {space[next_y][next_x]}")
                #                else:
                #                    print(f"Left, {next_x,next_y} is outside space")
                if (
                    (0 <= next_x < width)
                    and (0 <= next_y < height)
                    and space[next_y][next_x] == "#"
                ):
                    print("R", end=",")
                    facing = f
                    x, y = next_x, next_y
                else:
                    finished = True


def turn_left(facing):
    f = "NWSEN"["NWSEN".index(facing) + 1]
    dx, dy = movements[f]
    return dx, dy, f


def turn_right(facing):
    f = "NESWN"["NESWN".index(facing) + 1]
    dx, dy = movements[f]
    return dx, dy, f


if __name__ == "__main__":
    main()
