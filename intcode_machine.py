import sys
from collections import defaultdict
from copy import deepcopy


class IntcodeMachine:
    def __init__(self, memory_l=None):
        if memory_l:
            self.memory = self.memory_from_list(memory_l)
            self.memory_ = self.memory_from_list(memory_l)
        else:
            self.memory = defaultdict(int)
            self.memory_ = defaultdict(int)
        self.pc = 0
        self.inputs = []
        self.outputs = []
        self.state = "Not running"
        self.diagnostic_code = None
        self.relative_base = 0

    def memory_from_list(self, memory_l):
        as_dict = defaultdict(int)
        for i, v in enumerate(memory_l):
            as_dict[i] = v
        return as_dict

    def load_memory(self, filename):
        memory_l = []
        with open(filename) as f:
            for value in f.read().strip().split(","):
                memory_l.append(int(value))
        self.memory = self.memory_from_list(memory_l)
        self.memory_ = self.memory_from_list(memory_l)

    def reset(self):
        self.memory = deepcopy(self.memory_)
        self.pc = 0
        self.inputs = []
        self.outputs = []
        self.state = "Not running"
        self.diagnostic_code = None
        self.relative_base = 0

    def get_arg(self, instruction, n):
        position_mode = 0
        immediate_mode = 1
        relative_mode = 2

        mode = instruction // (10 ** (n + 1)) % 10
        if mode == position_mode:
            arg = self.memory[self.memory[self.pc + n]]
        elif mode == immediate_mode:
            arg = self.memory[self.pc + n]
        elif mode == relative_mode:
            arg = self.memory[self.memory[self.pc + n] + self.relative_base]
        else:
            raise ValueError(f"Invalid mode for arg 1 in {instruction}")
        return arg

    def run_program(self, inputs=None):

        if inputs:
            self.inputs = inputs
        old_result = result = "not started"
        while self.memory[self.pc] != 99:
            result = self.run()
            if isinstance(result, int):
                self.state = "Halted"
                if self.outputs:
                    self.diagnostic_code = self.outputs[-1]
                return self.diagnostic_code
            elif result == "Awaiting Input":
                return "Awaiting Input"

    def run(self):
        diagnostic_code = None
        position_mode = 0
        immediate_mode = 1
        relative_mode = 2

        add = 1
        mult = 2
        read = 3
        out = 4
        jump_if_true = 5
        jump_if_false = 6
        less_than = 7
        equals = 8
        adj_rel_b = 9
        halt = 99
        finished = False

        while not finished:
            instruction = self.memory[self.pc]
            opcode = instruction % 100

            if opcode == add:
                mode = instruction // (10 ** 4) % 10
                if mode == relative_mode:
                    rel_adj = self.relative_base
                else:
                    rel_adj = 0
                arg1 = self.get_arg(instruction, 1)
                arg2 = self.get_arg(instruction, 2)
                self.memory[self.memory[self.pc + 3] + rel_adj] = arg1 + arg2
                self.pc += 4
            elif opcode == mult:
                mode = instruction // (10 ** 4) % 10
                if mode == relative_mode:
                    rel_adj = self.relative_base
                else:
                    rel_adj = 0
                arg1 = self.get_arg(instruction, 1)
                arg2 = self.get_arg(instruction, 2)
                self.memory[self.memory[self.pc + 3] + rel_adj] = arg1 * arg2
                self.pc += 4
            elif opcode == read:
                mode = instruction // (10 ** 2) % 10
                if mode == relative_mode:
                    rel_adj = self.relative_base
                else:
                    rel_adj = 0
                if len(self.inputs) > 0:
                    self.memory[self.memory[self.pc + 1] + rel_adj] = self.inputs[0]
                    del self.inputs[0]
                    self.pc += 2
                else:
                    self.state = "Awaiting Input"
                    return "Awaiting Input"
            elif opcode == out:
                arg1 = self.get_arg(instruction, 1)
                self.diagnostic_code = arg1
                self.outputs.append(arg1)
                #print(arg1)
                self.pc += 2
            elif opcode == jump_if_true:
                arg1 = self.get_arg(instruction, 1)
                arg2 = self.get_arg(instruction, 2)
                if arg1 != 0:
                    self.pc = arg2
                else:
                    self.pc += 3
            elif opcode == jump_if_false:
                arg1 = self.get_arg(instruction, 1)
                arg2 = self.get_arg(instruction, 2)
                if arg1 == 0:
                    self.pc = arg2
                else:
                    self.pc += 3
            elif opcode == less_than:
                mode = instruction // (10 ** 4) % 10
                if mode == relative_mode:
                    rel_adj = self.relative_base
                else:
                    rel_adj = 0
                arg1 = self.get_arg(instruction, 1)
                arg2 = self.get_arg(instruction, 2)
                if arg1 < arg2:
                    self.memory[self.memory[self.pc + 3] + rel_adj] = 1
                else:
                    self.memory[self.memory[self.pc + 3] + rel_adj] = 0
                self.pc += 4
            elif opcode == equals:
                mode = instruction // (10 ** 4) % 10
                if mode == relative_mode:
                    rel_adj = self.relative_base
                else:
                    rel_adj = 0
                arg1 = self.get_arg(instruction, 1)
                arg2 = self.get_arg(instruction, 2)
                if arg1 == arg2:
                    self.memory[self.memory[self.pc + 3] + rel_adj] = 1
                else:
                    self.memory[self.memory[self.pc + 3] + rel_adj] = 0
                self.pc += 4
            elif opcode == adj_rel_b:
                arg1 = self.get_arg(instruction, 1)
                self.relative_base += arg1
                self.pc += 2
            elif opcode == halt:
                finished = True
                self.state = "Halted"
            else:
                raise ValueError(
                    f"Unrecognised opcode {self.memory[self.pc]} at position {self.pc}.\n Program:\n{self.memory}"
                )
            # print(f"instruction counter: {self.pc}")

        # return diagnostic_code
        return self.diagnostic_code


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
