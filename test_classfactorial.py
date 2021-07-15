from factorial_classes import factorial


def test_number_zero():
    res = factorial.factorial_number(0)
    assert res == 1


def test_number_one():
    res = factorial.factorial_number(1)
    assert res == 1


def test_negative_number():
    res = factorial.factorial_number(-1)
    assert res == "Please enter a positive number only"


def test_regular_number():
    res = factorial.factorial_number(4)
    assert res == 24





