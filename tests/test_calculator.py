'''My Calculator Test'''
from calculator import addition, subtraction, multiplication, division

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
