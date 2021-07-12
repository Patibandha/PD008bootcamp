import pytest

from PD008bootcamp.shailja_work import calculator


def test_add():
    res = calculator.add(1, 2)
    assert res == 3


def test_subtract():
    res = calculator.subtract(10, 5)
    assert res == 5


def test_multiply():
    res = calculator.multiply(4, 2)
    assert res == 8


def test_divide():
    res = calculator.divide(20, 10)
    assert res == 2

