import sys
from copy import copy, deepcopy
from collections import defaultdict,deque
from itertools import permutations
from intcode_machine import IntcodeMachine


def main():

    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = "15-input.txt"
    machine = IntcodeMachine()
    machine.load_memory(filename)
    directions = {1:(0,-1),  2:(0,1), 4:(1,0),3:(-1,0)}


    dist = 0
    seen = set((0,0))
    machines = [(machine,0,0)]

    finished = False
    while not finished:
        next_machines = set()
        dist += 1
        for machine,x,y in machines:
            for d in range(1,5):
                dx,dy = directions[d]
                if (x+dx,y+dy) not in seen:
                    seen.add((x+dx,y+dy))
                    tmp_machine = deepcopy(machine)
                    tmp_machine.run_program([d])
                    res = tmp_machine.outputs[-1]
                    if res == 0: # Hit a wall
                        pass
                    elif res == 1: # Can move in this direction
                        next_machines.add((tmp_machine,x+dx,y+dy))
                    else:
                        assert res == 2
                        print(f"Oxygen found at distance {dist}")
                        finished = True
        machines = next_machines
    



if __name__ == "__main__":
    main()
