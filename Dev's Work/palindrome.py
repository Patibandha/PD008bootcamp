import logging

def palindrome_check(str):
    alphanumeric_string = ""
    for character in str:
        if character.isalnum():
            alphanumeric_string += character
    print(alphanumeric_string)
    return alphanumeric_string == alphanumeric_string[::-1]

def main():
    str = input("Enter a string:" )
    result = palindrome_check(str)
    if result:
        print("String is a palindrome!")
    else:
        msg = ("String is not a palindrome")
        logging.warning(msg)

if __name__ == '__main__':
    main()
