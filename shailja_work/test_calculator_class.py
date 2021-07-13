import pytest

from PD008bootcamp.shailja_work.calculator_class import obj_cal


def test_add():
    res = obj_cal.add(1, 2)
    assert res == 3


def test_subtract():
    res = obj_cal.subtract(10, 5)
    assert res == 5


def test_multiply():
    res = obj_cal.multiply(4, 2)
    assert res == 8


def test_divide():
    res = obj_cal.divide(20, 10)
    assert res == 2
