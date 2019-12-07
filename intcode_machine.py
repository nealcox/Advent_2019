import sys


class IntcodeMachine:
    def __init__(self, memory=None):
        self.memory = memory
        self.memory_ = memory
        self.pc = 0
        self.inputs = []
        self.outputs = []
        self.state = "Not running"
        self.diagnostic_code = None

    def load_memory(self, filename):
        memory = []
        with open(filename) as f:
            for value in f.read().strip().split(","):
                memory.append(int(value))
        self.memory = memory
        self.memory_ = memory[:]

    def reload(self):
        self.memory = self.memory_[:]

    def get_arg(self, instruction, n):
        position_mode = 0
        immediate_mode = 1

        mode = instruction // (10 ** (n + 1)) % 10
        if mode == position_mode:
            arg = self.memory[self.memory[self.pc + n]]
        elif mode == immediate_mode:
            arg = self.memory[self.pc + n]
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

        add = 1
        mult = 2
        read = 3
        out = 4
        jump_if_true = 5
        jump_if_false = 6
        less_than = 7
        equals = 8
        halt = 99
        finished = False

        while not finished:
            instruction = self.memory[self.pc]
            opcode = instruction % 100

            if opcode == add:
                arg1 = self.get_arg(instruction, 1)
                arg2 = self.get_arg(instruction, 2)
                self.memory[self.memory[self.pc + 3]] = arg1 + arg2
                self.pc += 4
            elif opcode == mult:
                arg1 = self.get_arg(instruction, 1)
                arg2 = self.get_arg(instruction, 2)
                self.memory[self.memory[self.pc + 3]] = arg1 * arg2
                self.pc += 4
            elif opcode == read:
                if len(self.inputs) > 0:
                    self.memory[self.memory[self.pc + 1]] = self.inputs[0]
                    del self.inputs[0]
                    self.pc += 2
                else:
                    self.state =  "Awaiting Input"
                    return "Awaiting Input"
            elif opcode == out:
                arg1 = self.get_arg(instruction, 1)
                self.diagnostic_code = arg1
                self.outputs.append(arg1)
                print(arg1)
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
                arg1 = self.get_arg(instruction, 1)
                arg2 = self.get_arg(instruction, 2)
                if arg1 < arg2:
                    self.memory[self.memory[self.pc + 3]] = 1
                else:
                    self.memory[self.memory[self.pc + 3]] = 0
                self.pc += 4
            elif opcode == equals:
                arg1 = self.get_arg(instruction, 1)
                arg2 = self.get_arg(instruction, 2)
                if arg1 == arg2:
                    self.memory[self.memory[self.pc + 3]] = 1
                else:
                    self.memory[self.memory[self.pc + 3]] = 0
                self.pc += 4
            elif opcode == halt:
                finished = True
                self.state = "Halted"
            else:
                raise ValueError(
                    f"Unrecognised opcode {self.memory[self.pc]} at position {self.pc}.\n Program:\n{self.memory}"
                )
            # print(f"instruction counter: {self.pc}")

        #return diagnostic_code
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
