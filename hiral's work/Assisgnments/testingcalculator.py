import pytest
from calculator import addition,subtraction,division,multiplication
# class MyTestCase(unittest.TestCase):
def test_something():
    assert True == True

# testing addition method here
def test_addition():
    addition_result = addition(12,12)
    assert addition_result == 24
#
# # testing subtraction method here
def test_subtraction():
     subtraction_result = subtraction(12,12)
     assert subtraction_result == 0
#
# # testing division method here
def test_division():
     division_result = division(20,10)
     assert division_result == 2
#
# # testing multiplication method here
def test_multiplication():
     multiplication_result = multiplication(5,2)
     assert multiplication_result == 10



