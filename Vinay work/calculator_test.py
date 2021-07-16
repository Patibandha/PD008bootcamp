import unittest
import calculator_solution
from Vinaywork.calculator_solution import choice

class MyTestCase(unittest.TestCase):
    def test_add(x, y):
        return x + y

    # subratct formula
    def test_subtract(x, y):
        return x - y

    # multiply formula
    def test_multiply(x, y):
        return x * y

    # divison
    def test_divide(x, y):
        return x // y
    def test_something(self):
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
