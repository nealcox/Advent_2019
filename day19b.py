import sys
from collections import defaultdict
from itertools import permutations
from intcode_machine import IntcodeMachine

size_all = 50


def main():
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = "19-input.txt"
    machine = IntcodeMachine()
    machine.load_memory(filename)

    space = defaultdict(int)

    for x in range(size_all):
        for y in range(size_all):
            space[(x, y)] = get_tractor(x,y,machine)
    for y in range(size_all):
        print(f"{y:00d}: ",end="")
        for x in range(size_all):
            print(space[(x, y)],end="")
        print()
    
    y = size_all // 2
    min_x = 0
    while space[(min_x,y)] == 0:
        min_x += 1
    print(y,min_x -1,space[(min_x-1,y)])
    print(y,min_x,space[(min_x,y)])
    max_x = min_x
    while space[(max_x,y)] == 1:
        max_x += 1
    max_x -= 1
    print(y,max_x,space[(max_x,y)])
    print(y,max_x+1,space[(max_x+1,y)])

    finished = False
    while not finished:
        y += 1
        for x in range(min_x - 5, max_x + 5):
            space[(x,y)] = get_tractor(x,y,machine)
        x = min_x -5
        while space[(x,y)] == 0:
            x += 1
            min_x = x
        x = max_x +5
        while space[(x,y)] == 0:
            x -= 1
            max_x = x
        if space[(min_x+99,y-99)] == 1:
            print(f"Top left is {(min_x,y-99)}, answer {min_x*10000 + y-99}")
            finished = True

def get_tractor(x,y,machine):
    machine.reset()
    res = machine.run_program([x, y])
    return machine.outputs[-1]


if __name__ == "__main__":
    main()
