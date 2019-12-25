import sys
from collections import defaultdict
from itertools import permutations, combinations
from intcode_machine import IntcodeMachine


def main():
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = "25-input.txt"
    machine = IntcodeMachine()
    machine.load_memory(filename)
    command_file = "commands.txt"
    commands = []
    with open(command_file) as f:
        commands= list(f.read().strip().split('\n'))
    print (commands)

    finished = False
    out_idx = 0
    things = []
    carrying = stuff()
    while not finished:
        result = machine.run_program()
        while out_idx < len(machine.outputs):
            print(chr(machine.outputs[out_idx]),end="")
            out_idx += 1
        if isinstance(result, int):
            finished = True
        elif result == "Awaiting Input":
            if commands:
                command = commands[0]
                commands = commands[1:]
            else:
                command = input("What?")
                if command == "":
                    for thing in things:
                        commands.append("drop " + thing)
                    #carrying = next(stuff)
                    things = next(carrying)
                    print(f"Carrying: {things}")
                    for thing in things:
                        commands.append("take " + thing)
                    commands.append("west")
            for c in command:
                machine.inputs.append(ord(c))
            machine.inputs.append(ord('\n'))
        else:
            raise ValueError(f"Unknown return value {result}")

def stuff():
    things = [
            "fuel cell",
"easter egg",
"ornament",
"dark matter",
"hologram",
"klein bottle",
"hypercube",
"cake",
]
    for n in range(1,len(things)):
        for combo in combinations(things,n):
            print(list(combo))
            yield list(combo)

if __name__ == "__main__":
    main()
