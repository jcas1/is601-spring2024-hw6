'''Calculation Test'''
import pytest
from calculator import Calculator
from calculator.calculation import Calculation
from calculator.operations import division

def test_add():
    '''Test that addition function works'''
    assert Calculator.add(9,3) == 12

def test_sub():
    '''Test that subtraction function works'''
    assert Calculator.sub(9,3) == 6

def test_multiply():
    '''Test that multiplication function works'''
    assert Calculator.multiply(9,3) == 27

def test_divide():
    '''Test that division function works'''
    assert Calculator.divide(9,3) == 3

def test_calc_operations(a, b, operation, expected):
    '''
    A Test to perform calculations for all the sernarios

    Ensures that the calculation class performs the intended arithmetic function properly
    with the expected outcome
    
    Parameters:
        a: The first operand
        b: The second operand
        operation: The operation to be performed
        expected: The expected results
    '''
    calc = Calculation(a, b, operation)
    if isinstance(expected, type) and issubclass(expected, Exception):
        # If expected is an exception class, use pytest.raises to check if it is raised
        with pytest.raises(expected):
            calc.perform()
    else:
        # Otherwise, assert that the result matches the expected value
        assert calc.perform() == expected, f"Failed {operation} operation with {a} and {b}"

def test_divide_by_zero():
    '''
    A Test to form a divide by zero meant to raise the Divide by Zero Error
    '''
    calc = Calculation(10, 0, division)
    with pytest.raises(ZeroDivisionError, match="Cannot divide by zero"):
        calc.perform()
