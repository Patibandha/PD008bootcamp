"""
TDD: Factorial
n! = n*(n-1)*(n-2).....*1

8! = 8*(8-1)*(8-2)......*1 = 40320
(1) pytest
(2) unittest
(3) nosetest
(4) request factory
(5) mock.Mock()

logging is the module
there main logging
(1) logging.info --- this is informative log for your code or development
(2) logging.warning --- this is warning log (message) generated from your code
(3) logging.error --- this is error log (message) generated from your code, it break the code

"""
import logging

def fact(*args):
    try:
        logging.info(msg='I am inside try block of fact method')
        val = args[0]
        fact_result = 1
        if val >= 0:
            for num in range(1,val+1):
                fact_result = fact_result * num
            return fact_result
        else:
            return "Please provide positive number!"

    except TypeError as err:
        logging.error(msg="the code break")
        return err


