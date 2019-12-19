import sys
from collections import defaultdict
from itertools import permutations
from intcode_machine import IntcodeMachine

size = 50


def main():
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = "19-input.txt"
    machine = IntcodeMachine()
    machine.load_memory(filename)

    space = {}

    for x in range(size):
        for y in range(size):
            machine = IntcodeMachine()
            machine.load_memory(filename)
            res = machine.run_program([x, y])
            result = machine.outputs[-1]
            space[(x, y)] = result

    for x in range(size):
        for y in range(size):
            print(space[(x, y)], end="")
        print()
    print(f"Points affected {sum(space.values())} of {len(space.keys())}.")



    
    top_right_x,top_right_y = 25,20
    finished = False
    while not finished:
        top_right_x, top_right_y = next_top_right(top_right_x,top_right_y,space,machine)
        if (
                top_right_x > 100 and # Must be far enough across for there to be room for such a big box
                get_tractor(top_right_x-99,top_right_y,machine) and # Beam must be wide enough for the top left of the box to be inside it
                get_tractor(top_right_x-99,top_right_y+99,machine) # Beam must be tall enough at top left for bottom left to be inside it
            ):
            finished = True
    print(f"Top left of box is {(top_right_x,top_right_y)}, answer is {top_right_x*10000+top_right_y}")
            
def next_top_right(x,y,space,machine):
    y += 1
    dx = 0
    if (x,y) not in space:
        space[(x,y)]  =  get_tractor(x,y,machine)
    while space[(x+dx,y)] == 1:
        dx += 1
        if (x+dx,y) not in space:
            space[(x+dx,y)]  =  get_tractor(x+dx,y,machine)
    return x+dx-1,y

def get_tractor(x,y,machine):
    machine.reset()
    res = machine.run_program([x, y])
    return machine.outputs[-1]

if __name__ == "__main__":
    main()
