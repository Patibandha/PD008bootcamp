import unittest
from palindromstring import palindrome_string_check

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)

# checking palindrome_string_check function here
def testing_palindromestring(self):
    assert palindrome_string_check('noon') is True
    assert palindrome_string_check('lol') is True
    assert palindrome_string_check('') is True

if __name__ == '__main__':
    unittest.main()
