import unittest
import pytest

from factorial import factorial

def test_positive_fact():
    result = factorial(8)
    assert result == 40320

def test_negative_fact():
    result = factorial(-2)
    assert result == 0
