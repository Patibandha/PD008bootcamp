import unittest
import pytest

from palindrome import palindrome_check

def not_palindrome():
    result = palindrome_check("I am awesome")
    if !result:
        print("Not a palindrome")

def palindrome():
    result = palindrome_check("a man, a plan, a canal: panama")
    if result:
        print("Palindrome")
import logging
import builtins
import mock
from newpali import statement_condition, main
from testfixtures import LogCapture
LOGGER = logging.getLogger(__name__)


def test_correct_statement():
    LOGGER.warning('It is s a Palindrome')
    assert True


def test_false_statement():
    LOGGER.warning('Not a Palindrome')
    assert True

def test_positive():
    with mock.patch.object(builtins, 'input', lambda _: 'strong'):
        with LogCapture() as actual_log:
            main()
            expected_log = (
                ('root', 'WARNING', 'Enter valid string'),
            )
        assert actual_log.actual() == expected_log
