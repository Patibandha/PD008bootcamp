import unittest

from PD008bootcamp.shailja_work import Factorial_program


def test_fact():
    # Factorial_program.input = lambda: '4'
    respons = Factorial_program.factorial(4)
    assert respons == 24

def test_negative_fact():
    # Factorial_program.input = lambda: '-1'
    respons = Factorial_program.factorial(-1)
    assert respons == "Please Enter Positive number"

def test_one_fact():
    # Factorial_program.input = lambda: '1'
    respons = Factorial_program.factorial(1)
    assert respons == 1

def test_zero_fact():
    # Factorial_program.input = lambda: '0'
    respons = Factorial_program.factorial(0)
    assert respons == 1