
# function to replace the space and test for palindrome string
def palindrome_string_check(user_str):
    user_str = user_str.replace(" ", "")
    print(user_str)
    return user_str == user_str[::-1]


# getting user string input
s = input("Please enter your string: ")
tested_s = palindrome_string_check(s)

# testing if tested string is palindrome or not
if tested_s:
    print("String is a palindrome. ")
else:
    print("String is not a palindrome. ")