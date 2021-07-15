
from classcalc import calculation


def test_add():
    res = calculation.add(3, 2)
    assert res == 5


def test_subtract():
    res = calculation.subtract(3, 2)
    assert res == 1


def test_multiply():
    res = calculation.multiply(3, 3)
    assert res == 9


def test_divide():
    res = calculation.divide(4, 2)
    assert res == 2
