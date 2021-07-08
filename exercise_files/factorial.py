"""
TDD: Factorial
n! = n*(n-1)*(n-2).....*1

8! = 8*(8-1)*(8-2)......*1 = 40320
(1) pytest
(2) unittest
(3) nosetest
(4) request factory
(5) mock.Mock()
"""


def fact(*args):
    try:
        val = args[0]
        fact_result = 1
        if val >= 0:
            for num in range(1,val+1):
                fact_result = fact_result * num
            return fact_result
        else:
            return "Please provide positive number!"

    except TypeError as err:
        return err


