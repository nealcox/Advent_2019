import sys
from itertools import permutations
from intcode_machine import IntcodeMachine


def main():

    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = "07-input.txt"
    machine = IntcodeMachine()
    machine.load_memory(filename)

    inputs = [0]
    max_prev = 0
    for p in permutations(range(5),5):
        prev = run_amplifiers(filename,p)
        if prev > max_prev:
            print(f"New Maximum {prev} for settings {p}")
            max_prev = prev

    print(max_prev)


def run_amplifiers(filename,p):
    machines = []
    for i in range(5):
        machines.append(IntcodeMachine())
        machines[i].load_memory(filename)

    prev = 0
    for i in range(5):
        phase = p[i]
        print(f"Permutation {p}, machine {i}, phase {phase}")
        machine = IntcodeMachine()
        machine.load_memory(filename)
        prev = machine.run_program([phase,prev])
    print(f"{p} > {prev}")
    return prev

if __name__ == "__main__":
    main()
