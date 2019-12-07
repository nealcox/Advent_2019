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
    for p in permutations(range(5,10),5):
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

    for i in range(5):
        machines[(i+1)%5].inputs = machines[i].outputs
        phase = p[i]
        machines[(i-1)%5].outputs.append(phase)
    machines[4].outputs.append(0)



    finished = False
    while not finished:
        for i in range(5):
            machines[i].inputs = machines[(i - 1)%5].outputs
            print(f"{i} inputs {machines[i].inputs} {(i-1)%5} outputs {machines[(i-1)%5].outputs}")
            state = machines[i].run_program()
            print(f"{p} machine {i} > {state}")
            print(f"{i} memory: {machines[i].memory}")
        if state == "Halted":
            finished = True
    return machines[4].diagnostic_code

if __name__ == "__main__":
    main()
