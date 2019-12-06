import sys


class IntcodeMachine:
    def __init__(self, memory=None):
        self.memory = memory
        self.memory_ = memory

    def load_memory(self, filename):
        memory = []
        with open(filename) as f:
            for value in f.read().strip().split(","):
                memory.append(int(value))
        self.memory = memory
        self.memory_ = memory[:]

    def reload(self):
        self.memory = self.memory_[:]

    def get_arg(self, instruction, pc, n):
        position_mode = 0
        immediate_mode = 1

        mode = instruction // (10 ** (n + 1)) % 10
        if mode == position_mode:
            arg = self.memory[self.memory[pc + n]]
        elif mode == immediate_mode:
            arg = self.memory[pc + n]
        else:
            raise ValueError(f"Invalid mode for arg 1 in {instruction}")
        return arg

    def run_program(self, inputs=None):
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

        pointer = 0
        finished = False

        while not finished:
            instruction = self.memory[pointer]
            opcode = instruction % 100
            mode1 = instruction // 100 % 10
            mode2 = instruction // 1000 % 10
            mode3 = instruction // 10000 % 10

            if opcode == add:
                arg1 = self.get_arg(instruction, pointer, 1)
                arg2 = self.get_arg(instruction, pointer, 2)
                self.memory[self.memory[pointer + 3]] = arg1 + arg2
                pointer += 4
            elif opcode == mult:
                arg1 = self.get_arg(instruction, pointer, 1)
                arg2 = self.get_arg(instruction, pointer, 2)
                self.memory[self.memory[pointer + 3]] = arg1 * arg2
                pointer += 4
            elif opcode == read:
                self.memory[self.memory[pointer + 1]] = inputs[0]
                inputs = inputs[1:]
                pointer += 2
            elif opcode == out:
                arg1 = self.get_arg(instruction, pointer, 1)
                diagnotsic_code = arg1
                print(arg1)
                pointer += 2
            elif opcode == jump_if_true:
                arg1 = self.get_arg(instruction, pointer, 1)
                arg2 = self.get_arg(instruction, pointer, 2)
                if arg1 != 0:
                    pointer = arg2
                else:
                    pointer += 3
            elif opcode == jump_if_false:
                arg1 = self.get_arg(instruction, pointer, 1)
                arg2 = self.get_arg(instruction, pointer, 2)
                if arg1 == 0:
                    pointer = arg2
                else:
                    pointer += 3
            elif opcode == less_than:
                arg1 = self.get_arg(instruction, pointer, 1)
                arg2 = self.get_arg(instruction, pointer, 2)
                if arg1 < arg2:
                    self.memory[self.memory[pointer + 3]] = 1
                else:
                    self.memory[self.memory[pointer + 3]] = 0
                pointer += 4
            elif opcode == equals:
                arg1 = self.get_arg(instruction, pointer, 1)
                arg2 = self.get_arg(instruction, pointer, 2)
                if arg1 == arg2:
                    self.memory[self.memory[pointer + 3]] = 1
                else:
                    self.memory[self.memory[pointer + 3]] = 0
                pointer += 4
            elif opcode == halt:
                finished = True
            else:
                raise ValueError(
                    f"Unrecognised opcode {self.memory[pointer]} at position {pointer}.\n Program:\n{self.memory}"
                )
            # print(f"instruction pointer: {pointer}")

        return diagnotsic_code


def main():

    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = "05-input.txt"
    machine = IntcodeMachine()
    machine.load_memory(filename)

    inputs = [5]

    print(machine.run_program(inputs))


if __name__ == "__main__":
    main()
