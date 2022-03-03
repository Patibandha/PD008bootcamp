"""
Question: Define a class with a generator which can iterate the numbers, which are divisible by 7,
between a given range 0 and n.

Hints: Consider use yield
"""


num = int(input())
div = [i for i in range(0, num) if (i % 7 == 0)]
print(div)

def divCheck(num):
    for i in range(num):
        if i % 7 == 0:
            value = True
        else:
            value = False


divCheck(num)