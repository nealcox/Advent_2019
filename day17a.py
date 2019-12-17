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
    a_ps = 0
    for r, line in enumerate(space):
        for c, char in enumerate(line):
            if char in "^>v<":
                i = "^>v<".index(char)
                facing = "NESW"[i]
                print(f"Robot {char} at {(c,r)}, facing {facing}.")
            elif char == "#":
                if (
                    space[r - 1][c] == "#"
                    and space[r + 1][c] == "#"
                    and space[r][c - 1] == "#"
                    and space[r][c + 1] == "#"
                ):
                    print(f"Intersection @ {(c,r)}")
                    a_ps += r * c
                    print(f"Sum of alignment parameters is {a_ps}")


if __name__ == "__main__":
    main()
