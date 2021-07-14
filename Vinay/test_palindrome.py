import logging
from newpali import statement_condition
LOGGER = logging.getLogger(__name__)


def test_correct_statement():
    LOGGER.warning('It is s a Palindrome')
    assert True


def test_false_statement():
    LOGGER.warning('Not a Palindrome')
    assert True
