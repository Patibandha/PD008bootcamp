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
