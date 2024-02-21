'''Operations Test'''
import pytest

from calculator.calculation import Calculation
from calculator.operations import addition, subtraction, multiplication, division

def test_addition():
    '''Test that addition function works'''
    assert addition(9,3) == 12

def test_subtraction():
    '''Test that subtraction function works'''
    assert subtraction(9,3) == 6

def test_multiplication():
    '''Test that multiplication function works'''
    assert multiplication(9,3) == 27

def test_division():
    '''Test that division function works'''
    assert division(9,3) == 3

def test_division_by_zero():
    '''Test divide by zero exception works'''
    with pytest.raises(ZeroDivisionError):
        division(9,0)

def test_operations(a, b, operation, expected):
    '''Testing Various operations for num_records'''
    calculation = Calculation.create_calc(a, b, operation)
    if isinstance(expected, type) and issubclass(expected, Exception):
        # If expected is an exception class, use pytest.raises to check if it is raised
        with pytest.raises(expected):
            calculation.perform()
    else:
        # Otherwise, assert that the result matches the expected value
        assert calculation.perform() == expected, f"Failed {operation} operation with {a} and {b}"
