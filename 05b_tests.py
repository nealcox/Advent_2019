import unittest

from day05b import run_program

class RunProgramTest(unittest.TestCase):
    def test_equals_8_position(self):
        # Using position mode, consider whether the input is equal to 8; output 1 (if it is) or 0 (if it is not).
        self.assertEqual(run_program([3,9,8,9,10,9,4,9,99,-1,8],1),0)
        self.assertEqual(run_program([3,9,8,9,10,9,4,9,99,-1,8],7),0)
        self.assertEqual(run_program([3,9,8,9,10,9,4,9,99,-1,8],8),1)
        self.assertEqual(run_program([3,9,8,9,10,9,4,9,99,-1,8],9),0)
    def test_less_than_8_position(self):
        # Using position mode, consider whether the input is less than 8; output 1 (if it is) or 0 (if it is not).
        self.assertEqual(run_program([3,9,7,9,10,9,4,9,99,-1,8],1),1)
        self.assertEqual(run_program([3,9,7,9,10,9,4,9,99,-1,8],7),1)
        self.assertEqual(run_program([3,9,7,9,10,9,4,9,99,-1,8],8),0)
        self.assertEqual(run_program([3,9,7,9,10,9,4,9,99,-1,8],9),0)
    def test_equals_8_immediate(self):
        # Using immediate mode, consider whether the input is equal to 8; output 1 (if it is) or 0 (if it is not).
        self.assertEqual(run_program([3,3,1108,-1,8,3,4,3,99],1),0)
        self.assertEqual(run_program([3,3,1108,-1,8,3,4,3,99],7),0)
        self.assertEqual(run_program([3,3,1108,-1,8,3,4,3,99],8),1)
        self.assertEqual(run_program([3,3,1108,-1,8,3,4,3,99],9),0)
    def test_less_than_8_immediate(self):
        # Using immediate mode, consider whether the input is less than 8; output 1 (if it is) or 0 (if it is not).
        self.assertEqual(run_program([3,3,1107,-1,8,3,4,3,99],1),1)
        self.assertEqual(run_program([3,3,1107,-1,8,3,4,3,99],7),1)
        self.assertEqual(run_program([3,3,1107,-1,8,3,4,3,99],8),0)
        self.assertEqual(run_program([3,3,1107,-1,8,3,4,3,99],9),0)
    def test_is_input_zero_position(self):
        # jump tests that take an input, then output 0 if the input was zero or 1 if the input was non-zero Position mode
        program = [3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9]
        self.assertEqual(run_program(program[:],[1]),0)
        self.assertEqual(run_program(program[:],[0]),1)
        self.assertEqual(run_program(program[:],[-1]),0)
        
    def test_is_input_zero_immediate(self):
        # jump tests that take an input, then output 0 if the input was zero or 1 if the input was non-zero Immediate mode
        program = [3,3,1105,-1,9,1101,0,0,12,4,12,99,1]
        self.assertEqual(run_program(program[:],[1]),0)
        self.assertEqual(run_program(program[:],[0]),1)
        self.assertEqual(run_program(program[:],[-1]),0)

    def test_compare_to_8(self):
        program = [3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,
1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,
999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99]
        self.assertEqual(run_program(program[:],[7]),999)
        self.assertEqual(run_program(program[:],[8]),1000)
        self.assertEqual(run_program(program[:],[9]),1001)
