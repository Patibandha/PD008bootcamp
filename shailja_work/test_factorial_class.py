import unittest

from PD008bootcamp.shailja_work.factorial_class import obj_fac


def test_fact():
    respons = obj_fac.factorial(4)
    assert respons == 24

def test_negative_fact():
    respons = obj_fac.factorial(-1)
    assert respons == "Please Enter Positive number"

def test_one_fact():
    respons = obj_fac.factorial(1)
    assert respons == 1

def test_zero_fact():
    respons = obj_fac.factorial(0)
    assert respons == 1