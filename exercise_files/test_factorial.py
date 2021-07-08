import unittest
import pytest
from exercise_files.factorial import fact


# positive
def test_fact():
    respons = fact(8)
    assert respons == 40320


# negative
def test_negative_fact():
    respons = fact(-1)
    assert respons == "Please provide positive number!"


# exception handling test cases
def test_negative_fact_with_diff_datatype():
    respons = fact("this is my wrong input")
    # import pdb
    # pdb.set_trace()
    assert respons.args == ("'>=' not supported between instances of 'str' and 'int'",)

