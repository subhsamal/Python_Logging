# Simple functions to demonstrate logging in python

import logging

# Default logging level is WARNING, the below line changes it to Debug.
# This level of logging.DEBUG refers to a constant integer value that we
# reference in the code above to set a threshold. The level of DEBUG is 10

logging.basicConfig(filename='test.log', level=logging.DEBUG,
                    format='%(asctime)s:%(levelname)s:%(message)s')

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def divide(x, y):
    return x/y

def multiply(x, y):
    return x * y

num1 = 50
num2 = 25

add_result = add(num1, num2)
logging.debug("Addition of {} and {} is {}".format(num1, num2, add_result))

sub_result = subtract(num1, num2)
logging.debug("Subtaction of {} and {} is {}".format(num1, num2, sub_result))

div_result = divide(num1, num2)
logging.debug("Division of {} and {} is {}".format(num1, num2, div_result))

mul_result = multiply(num1, num2)
logging.debug("Multiply of {} and {} is {}".format(num1, num2, mul_result))
