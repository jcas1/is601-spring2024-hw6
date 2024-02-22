# pylint: disable=line-too-long
'''Operations'''
from calculator.operations import addition, subtraction, multiplication, division
from calculator.calculation import Calculation

class Calculator:
    '''Calculator Class'''
    @staticmethod
    def add(a,b):
        '''Returns the sum of the two values'''
        calc = Calculation(a, b, addition) #Passes two numbers into the addition function
        return calc.get_result()

    @staticmethod
    def sub(a,b):
        '''Returns the difference of the two values'''
        calc = Calculation(a, b, subtraction) #Passes two numbers into the subtraction function
        return calc.get_result()

    @staticmethod
    def multiply(a,b):
        '''Returns the product of the two values'''
        calc = Calculation(a, b, multiplication) #Passes two numbers into the multiplication function
        return calc.get_result()

    @staticmethod
    def divide(a,b):
        '''Returns the quotient of the two values'''
        calc = Calculation(a, b, division) #Passes two numbers into the division function
        return calc.get_result()
