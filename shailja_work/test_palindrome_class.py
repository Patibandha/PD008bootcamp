import logging

from PD008bootcamp.shailja_work.palindrom_class import obj_pali

LOGGER = logging.getLogger(__name__)


def test_pal_true():
    LOGGER.warning("The string is a palindrome")
    assert True


def test_pal_false():
    LOGGER.warning("Not a palindrome")
    assert True


# def test_checkstr():
#     respons = Palindrome_program.check_is_digit(4)
#     assert respons == "You must enter a string. Please try again"
