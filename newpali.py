# check if it is palindrome or not.
import logging


def main():
    s = input("Enter a string")
    empty_string = ""
    for char in s:
        if char.isalnum():
            empty_string += char
    logging.warning("statement checking: " + empty_string)
    statement_condition(empty_string)


def statement_condition(empty_string):
    #logging.basicConfig(filename='newpali.py', level=logging.msg)
    if empty_string == empty_string[::-1]:
        msg = "It's a Palindrome"
    else:
        msg = "Not a Palindrome"
    logging.warning(msg)


if __name__ == '__main__':
    main()
