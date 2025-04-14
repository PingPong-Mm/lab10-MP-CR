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

#partner 2 part


def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b

def log(a, b):
    if a <= 0 or a == 1 or b <= 0:
        raise ValueError("Invalid input for logarithm")
    return math.log(b, a)

def exp(a, b):
    return a ** b