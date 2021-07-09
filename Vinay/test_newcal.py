from newcal import add, subtract, multiply, divide


def test_add():
    res = add(20, 40)
    assert res == 60


def test_subtract():
    res = subtract(20, 10)
    assert res == 10


def test_multiply():
    res = multiply(5, 10)
    assert res == 50


def test_divide():
    res = divide(10, 2)
    assert res == 5
