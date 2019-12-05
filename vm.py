import sys


def main():

    if len(sys.argv) > 1:
        input_file = sys.argv[1]
    else:
        input_file = "XX-input.txt"
    memory = load_memory(input_file)

    memory = run_program(memory)

    for i in range(len(memory)):
        print(memory[i], end=",")
    print()


def run_program(memory):
    add = 1
    mult = 2
    halt = 99

    pointer = 0
    finished = False

    while not finished:
        opcode = memory[pointer]
        if opcode == add:
            memory[memory[pointer + 3]] = (
                memory[memory[pointer + 2]] + memory[memory[pointer + 1]]
            )
            pointer += 4
        elif opcode == mult:
            memory[memory[pointer + 3]] = (
                memory[memory[pointer + 2]] * memory[memory[pointer + 1]]
            )
            pointer += 4
        elif opcode == halt:
            finished = True
        else:
            raise ValueError(
                f"Unrecognised opcode {memory[pointer]} at position {pointer}.\n Program:\n{memory}"
            )

    return memory


def load_memory(filename):
    memory = []
    with open(filename) as f:
        for value in f.read().strip().split(","):
            memory.append(int(value))
    return memory


if __name__ == "__main__":
    main()
