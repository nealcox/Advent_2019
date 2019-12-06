import unittest

from intcode_machine import IntcodeMachine

class RunProgramTest(unittest.TestCase):
    def test_equals_8_position(self):
        # Using position mode, consider whether the input is equal to 8; output 1 (if it is) or 0 (if it is not).
        self.assertEqual(IntcodeMachine([3,9,8,9,10,9,4,9,99,-1,8]).run_program([1]),0)
        self.assertEqual(IntcodeMachine([3,9,8,9,10,9,4,9,99,-1,8]).run_program([7]),0)
        self.assertEqual(IntcodeMachine([3,9,8,9,10,9,4,9,99,-1,8]).run_program([8]),1)
        self.assertEqual(IntcodeMachine([3,9,8,9,10,9,4,9,99,-1,8]).run_program([9]),0)

    def test_less_than_8_position(self):
        # Using position mode, consider whether the input is less than 8; output 1 (if it is) or 0 (if it is not).
        self.assertEqual(IntcodeMachine([3,9,7,9,10,9,4,9,99,-1,8]).run_program([1]),1)
        self.assertEqual(IntcodeMachine([3,9,7,9,10,9,4,9,99,-1,8]).run_program([7]),1)
        self.assertEqual(IntcodeMachine([3,9,7,9,10,9,4,9,99,-1,8]).run_program([8]),0)
        self.assertEqual(IntcodeMachine([3,9,7,9,10,9,4,9,99,-1,8]).run_program([9]),0)
    def test_equals_8_immediate(self):
        # Using immediate mode, consider whether the input is equal to 8; output 1 (if it is) or 0 (if it is not).
        self.assertEqual(IntcodeMachine([3,3,1108,-1,8,3,4,3,99]).run_program([1]),0)
        self.assertEqual(IntcodeMachine([3,3,1108,-1,8,3,4,3,99]).run_program([7]),0)
        self.assertEqual(IntcodeMachine([3,3,1108,-1,8,3,4,3,99]).run_program([8]),1)
        self.assertEqual(IntcodeMachine([3,3,1108,-1,8,3,4,3,99]).run_program([9]),0)
    def test_less_than_8_immediate(self):
        # Using immediate mode, consider whether the input is less than 8; output 1 (if it is) or 0 (if it is not).
        self.assertEqual(IntcodeMachine([3,3,1107,-1,8,3,4,3,99]).run_program([1]),1)
        self.assertEqual(IntcodeMachine([3,3,1107,-1,8,3,4,3,99]).run_program([7]),1)
        self.assertEqual(IntcodeMachine([3,3,1107,-1,8,3,4,3,99]).run_program([8]),0)
        self.assertEqual(IntcodeMachine([3,3,1107,-1,8,3,4,3,99]).run_program([9]),0)
    def test_is_input_zero_position(self):
        # jump tests that take an input, then output 0 if the input was zero or 1 if the input was non-zero Position mode
        program = [3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9]
        self.assertEqual(IntcodeMachine(program[:]).run_program([1]),1)
        self.assertEqual(IntcodeMachine(program[:]).run_program([-1]),1)
        self.assertEqual(IntcodeMachine(program[:]).run_program([0]),0)
        
    def test_is_input_zero_immediate(self):
        # jump tests that take an input, then output 0 if the input was zero or 1 if the input was non-zero Immediate mode
        program = [3,3,1105,-1,9,1101,0,0,12,4,12,99,1]
        self.assertEqual(IntcodeMachine(program[:]).run_program([1234]),1)
        self.assertEqual(IntcodeMachine(program[:]).run_program([1]),1)
        self.assertEqual(IntcodeMachine(program[:]).run_program([0]),0)
        self.assertEqual(IntcodeMachine(program[:]).run_program([12345]),1)
        self.assertEqual(IntcodeMachine(program[:]).run_program([-1234]),1)
        self.assertEqual(IntcodeMachine(program[:]).run_program([-1]),1)

    def test_compare_to_8(self):
        program = [3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,
                    1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,
                    999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99]
        self.assertEqual(IntcodeMachine(program[:]).run_program([7]),999)
        self.assertEqual(IntcodeMachine(program[:]).run_program([8]),1000)
        self.assertEqual(IntcodeMachine(program[:]).run_program([9]),1001)

    def test_jump_if_true(self):
        # jumps
        program = [1105,1,3,1105,0,0,104,1,99]
        self.assertEqual(IntcodeMachine(program[:]).run_program([9999]),1)

if __name__ == "__main__":
    unittest.main()
 
