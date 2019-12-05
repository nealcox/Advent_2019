import sys

add = 1
multiply = 2
halt = 99


def main():

    if len(sys.argv) > 1:
        memory = get_memory(sys.argv[1])
    else:
        memory = get_memory("02-input.txt")

    pointer = 0
    finished = False

    memory[1] = 12
    memory[2] = 2

    while finished == False:
        opcode = memory[pointer]
        if opcode == add:
            memory[memory[pointer + 3]] = (
                memory[memory[pointer + 2]] + memory[memory[pointer + 1]]
            )
            pointer += 4
        elif opcode == multiply:
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

    for i in range(len(memory)):
        print(memory[i], end=",")
    print()


def get_memory(filename):
    memory = []
    with open(filename) as f:
        for value in f.read().strip().split(","):
            memory.append(int(value))
    return memory


if __name__ == "__main__":
    main()
