import unittest
#import pytest

from factorial import factorial

def test_positive_fact():
    result = factorial(8)
    assert result == 40320

def test_negative_fact():
    result = factorial(-2)
    assert result == 0

def test_zero_fact():
    result = factorial(0)
    assert result == 1
   
def test_one_fact():
    result = factorial(1)
    assert result == 1
