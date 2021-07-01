p_string = input ("Enter a string: ")
al_num = ""

for character in p_string:
    if character.isalnum():
        al_num += character
print (al_num)
if(al_num == al_num[::-1]):
      print("The string is a palindrome")
else:
      print("Not a palindrome")