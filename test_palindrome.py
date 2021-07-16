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