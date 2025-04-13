import math

#add
def add(a, b):
    value = a + b
    return value

#subtract
def subtract(a, b):
    value = a - b
    return value

#multiply
def multiply(a, b):
    value = a * b
    return value

#division
def divide(a, b):
    value = b / a
    if a == 0:
        raise ZeroDivisionError
    else:
        return value

#log
def logarithm(a, b):
    value = math.log(a, b)
    return value

#exponent
def exponent(a, b):
    value = a ** b
    return value