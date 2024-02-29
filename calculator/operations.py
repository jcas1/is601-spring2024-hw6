'''Operations'''

def addition(a,b):
    '''Returns the sum of the two values'''
    return a + b

def subtraction(a,b):
    '''Returns the difference of the two values'''
    return a - b

def multiplication(a,b):
    '''Returns the product of the two values'''
    return a * b

def division(a,b):
    '''Returns the quotient of the two values'''
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero!!!")
    return a / b
