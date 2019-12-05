import sys


def main():

    if len(sys.argv) > 1:
        input_file = sys.argv[1]
    else:
        input_file = "05-input.txt"
    memory = load_memory(input_file)

    inputs = [5]

    print(run_program(memory, inputs))


def run_program(memory, inputs):
    diagnotsic_code = None
    position_mode = 0
    immediate_mode = 1

    add = 1
    mult = 2
    read = 3
    out = 4
    jump_if_true = 5
    jump_if_false = 6
    less_than = 7
    equals = 8
    halt = 99

    # modal args only
    args_per_opcode = {
        add: 2,
        mult: 2,
        read: 0,
        out: 1,
        halt: 0,
        jump_if_true: 2,
        jump_if_false: 2,
        less_than: 2,
        equals: 2,
    }

    pointer = 0
    finished = False

    while not finished:
        instruction = memory[pointer]
        opcode = instruction % 100
        mode1 = instruction // 100 % 10
        mode2 = instruction // 1000 % 10
        mode3 = instruction // 10000 % 10

        if args_per_opcode[opcode] > 0:
            if mode1 == position_mode:
                arg1 = memory[memory[pointer + 1]]
            elif mode1 == immediate_mode:
                arg1 = memory[pointer + 1]
            else:
                raise ValueError(f"Invalid mode for arg 1 in {instruction}")
            if args_per_opcode[opcode] > 1:
                if mode2 == position_mode:
                    arg2 = memory[memory[pointer + 2]]
                elif mode2 == immediate_mode:
                    arg2 = memory[pointer + 2]
                else:
                    raise ValueError(f"Invalid mode for arg 2 in {instruction}")
                if args_per_opcode[opcode] > 2:
                    if mode3 == position_mode:
                        arg3 = memory[memory[pointer + 3]]
                    elif mode3 == immediate_mode:
                        arg3 = memory[pointer + 3]
                    else:
                        raise ValueError(f"Invalid mode for arg 3 in {instruction}")

        if opcode == add:
            memory[memory[pointer + 3]] = arg1 + arg2
            pointer += 4
        elif opcode == mult:
            memory[memory[pointer + 3]] = arg1 * arg2
            pointer += 4
        elif opcode == read:
            memory[memory[pointer + 1]] = inputs[0]
            inputs = inputs[1:]
            pointer += 2
        elif opcode == out:
            diagnotsic_code = arg1
            print(arg1)
            pointer += 2
        elif opcode == jump_if_true:
            if arg1 != 0:
                pointer = arg2
        #     else:
        #         pointer += 3
        elif opcode == jump_if_false:
            if arg1 == 0:
                pointer = arg2
        #     else:
        #         pointer += 3
        elif opcode == less_than:
            if arg1 < arg2:
                memory[memory[pointer + 3]] = 1
            else:
                memory[memory[pointer + 3]] = 0
            pointer += 4
        elif opcode == equals:
            if arg1 == arg2:
                memory[memory[pointer + 3]] = 1
            else:
                memory[memory[pointer + 3]] = 0
            pointer += 4
        elif opcode == halt:
            finished = True
        else:
            raise ValueError(
                f"Unrecognised opcode {memory[pointer]} at position {pointer}.\n Program:\n{memory}"
            )
        print(f"instruction pointer: {pointer}")

    return diagnotsic_code


def load_memory(filename):
    memory = []
    with open(filename) as f:
        for value in f.read().strip().split(","):
            memory.append(int(value))
    return memory


if __name__ == "__main__":
    main()
