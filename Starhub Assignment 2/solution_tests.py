from solution import *
import unittest

class test_program(unittest.TestCase):
    
    def test_program_output(self):
        self.assertEqual(program(127), '{"Count of Star": 26, "Count of Hub": 19, "Count of StarHub": 3}')
    
    def test_input_value(self):
        self.assertRaises(ValueError, program, True)

if __name__ == '__main__':
    unittest.main(argv = [''], verbosity = 2, exit = False)