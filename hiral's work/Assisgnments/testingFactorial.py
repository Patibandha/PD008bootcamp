import unittest
from factorial import factorial

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)

# testing the factorial function here
# positive value test
def factorial_testing(self):
    positive_result = factorial(5.0)
    self.assertEqual(positive_result,120.0)

# negative value test
def test_negative_fact():
    negative_result = factorial(-1)
    assert negative_result == "We need positive number please"

if __name__ == '__main__':
    unittest.main()
