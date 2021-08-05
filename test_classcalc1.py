import builtins
import pytest
import logging
import mock
from classcalc import Calculator, main_method
from testfixtures import LogCapture
LOGGER = logging.getLogger(__name__)


def test_add():
    calculation = Calculator()
    res = calculation.add(3, 2)
    assert res == 5


def test_subtract():
    calculation = Calculator()
    res = calculation.subtract(3, 2)
    assert res == 1


def test_multiply():
    calculation = Calculator()
    res = calculation.multiply(3, 3)
    assert res == 9


def test_divide():
    calculation = Calculator()
    res = calculation.divide(4, 2)
    assert res == 2


def test_positive():
    with mock.patch.object(builtins, 'input', lambda _: 'strong', '1', '+'):
        with LogCapture() as actual_log:
            main_method()
            expected_log = (
                ('root', 'WARNING', 'Enter valid input'),
            )
            assert actual_log.actual()[0] == expected_log[0]
            LOGGER.warning("Enter valid input")
    assert True
