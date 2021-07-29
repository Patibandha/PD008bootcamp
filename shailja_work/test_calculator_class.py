import builtins

import pytest
import logging
import mock

from PD008bootcamp.shailja_work.calculator_class import Calculator, main
from testfixtures import LogCapture

LOGGER = logging.getLogger(__name__)


def test_add():
    obj_cal = Calculator()
    res = obj_cal.add(1, 2)
    assert res == 3


def test_subtract():
    obj_cal = Calculator()
    res = obj_cal.subtract(10, 5)
    assert res == 5


def test_multiply():
    obj_cal = Calculator()
    res = obj_cal.multiply(4, 2)
    assert res == 8


def test_divide():
    obj_cal = Calculator()
    res = obj_cal.divide(20, 10)
    assert res == 2


def test_special_positive():
    with mock.patch.object(builtins, 'input', lambda _: '&', '1', '+'):
        with LogCapture() as actual_log:
            main()
            expected_log = (
                ('root', 'WARNING', 'please enter numeric value'),
            )
            assert actual_log.actual()[0] == expected_log[0]


def test_list_positive():
    with mock.patch.object(builtins, 'input', lambda _: '[1,2,3]', '1', '+'):
        with LogCapture() as actual_log:
            main()
            expected_log = (
                ('root', 'WARNING', 'please enter numeric value'),
            )
            assert actual_log.actual()[0] == expected_log[0]
    LOGGER.warning("please enter numeric value")
    assert True


def test_string_negative():
    with mock.patch.object(builtins, 'input', lambda _: 'strong', '1', '+'):
        with LogCapture() as actual_log:
            main()
            expected_log = (
                ('root', 'WARNING', 'please enter numeric value'),
            )
            if expected_log == actual_log:
                assert actual_log.actual()[0] == expected_log[0]
                assert True
