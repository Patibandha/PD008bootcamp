import math
import unittest
from testfact import check_factorial


def test_positive():
    res = check_factorial(2)
    assert res == 2


def test_zero():
    res = check_factorial(0)
    assert res == 1


def test_one():
    res = check_factorial(1)
    assert res == 1


def test_negative():
    res = check_factorial(-1)
    assert res == "Please enter a positive number only"
