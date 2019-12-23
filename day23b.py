import sys
from collections import defaultdict
from itertools import permutations
from intcode_machine import IntcodeMachine

size = 50


def main():
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = "23-input.txt"
    machine = IntcodeMachine()
    machine.load_memory(filename)

    machines = []

    for x in range(size):
        machine = IntcodeMachine()
        machine.load_memory(filename)
        machine.inputs.append(x)
        machines.append(machine)

    output_idxs = [0] * 50
    nat_x = nat_y = None
    last_idle = False
    seen = set()
    finished = False
    while not finished:
        for i in range(size):
            machines[i].run_program()
        for i in range(size):
            idx = output_idxs[i]
            while idx < len(machines[i].outputs):
                address,x,y = machines[i].outputs[idx:idx+3]
                idx += 3
                if address == 255:
                    nat_x,nat_y = x,y
                else:
                    machines[address].inputs.append(x)
                    machines[address].inputs.append(y)
                    output_idxs[i] = idx
        idle = True
        for i in range(size):
            if len(machines[i].inputs) == 0:
                machines[i].inputs.append(-1)
            else:
                idle = False
                last_idle = False
        if idle:
            if last_idle:
                machines[0].inputs[-1] = nat_x
                machines[0].inputs.append(nat_y)
                if nat_y in seen:
                    print(f"Already seen: {nat_y}")
                    finished = True
                else:
                    print(nat_y)
                    seen.add(nat_y)
            else:
                last_idle = True


if __name__ == "__main__":
    main()
