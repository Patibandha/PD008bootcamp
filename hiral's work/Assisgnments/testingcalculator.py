import unittest
import calculator

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)

# testing addition method here
def test_addition():
    addition_result = calculator.addition(12,12)
    assert addition_result == 24

# testing subtraction method here
def test_subtraction():
    subtraction_result = calculator.subtraction(12,12)
    assert subtraction_result == 0

# testing division method here
def test_division():
    division_result = calculator.division(20,10)
    assert division_result == 2

# testing multiplication method here
def test_multiplication():
    multiplication_result = calculator.multiplication(5,2)
    assert multiplication_result == 10


if __name__ == '__main__':
    unittest.main()
