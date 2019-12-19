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


if __name__ == "__main__":
    main()
