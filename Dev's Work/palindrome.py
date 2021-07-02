def palindrome_check(str):
    str = str.replace(" ", "")
    print(str)
    return str == str[::-1]

str = input("Enter a string:" )
result = palindrome_check(str)

if result:
    print("String is a palindrome!")
else:
    print("String is not a palindrome")
