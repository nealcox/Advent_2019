import sys
from collections import defaultdict
from itertools import permutations
from intcode_machine import IntcodeMachine


def main():
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = "17-input.txt"
    machine = IntcodeMachine()
    machine.load_memory(filename)
    machine.memory[0] = 2

    with open("directions.txt") as f:
        directions = f.read()
    for c in directions:
        machine.inputs.append(ord(c))

    finished = False
    while not finished:
        result = machine.run_program()
        if isinstance(result, int):
            finished = True
        elif result == "Awaiting Input":
            input(f"(pc = {machine.pc})?")
        else:
            raise ValueError(f"Unknown return value {result}")
    print(result)


if __name__ == "__main__":
    main()
