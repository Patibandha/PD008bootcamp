def pal_string(p):
    return p == p[::-1]

p = input ("Enter a string: ")
result = pal_string(p)

if result:
    print("yes")
else:
    print("no")
