import sys
from collections import defaultdict
from itertools import permutations
from intcode_machine import IntcodeMachine

size = 50


def main():
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = "21-input.txt"
    machine = IntcodeMachine()
    machine.load_memory(filename)
    
    program = """NOT J T
OR J T
NOT T J
OR I J
OR F J
AND E J 
OR H J
AND A T
AND B T
AND C T
NOT T T
AND T J
AND D J
RUN
"""

    for c in program:
        machine.inputs.append(ord(c))
    result = machine.run_program()
    if result > 255:
        print(f" Result of running program: {result}")
    else:
        for i in machine.outputs:
            print(chr(i), end="")


if __name__ == "__main__":
    main()
