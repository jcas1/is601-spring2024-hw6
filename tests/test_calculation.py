'''Calculation Test'''
from calculator import Calculator

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
