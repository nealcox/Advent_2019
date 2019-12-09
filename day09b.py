import sys
from itertools import permutations
from intcode_machine import IntcodeMachine


def main():

    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = "09-input.txt"
    machine = IntcodeMachine()
    machine.load_memory(filename)

    machine.run_program([2])


if __name__ == "__main__":
    main()
