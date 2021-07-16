import pytest
from factorial import factorial

def test_something():
    assert True == True

# testing the factorial function here
# positive value test
def factorial_testing():
    positive_result = factorial(5.0)
    assert positive_result == 120.0

# negative value test
def test_negative_fact():
    negative_result = factorial(-1)
    assert negative_result == "We need positive number please"

#if __name__ == '__main__':
 #   unittest.main()
