# pylint: disable=line-too-long
# pylint: disable=redefined-outer-name, unused-argument
'''Test to add calculations to the calculator and then return all calculations'''

import pytest

#Importing the Calculator & Calculations Packages nessary
from calculator.calculation import Calculation
from calculator.calculations import Calculations

#Importing Operations
from calculator.operations import addition, subtraction, multiplication, division

@pytest.fixture
def sample_calc():
    '''Clears History & Sets up sample list'''
    Calculations.clear_history()
    Calculations.add_calc(Calculation(2,2,addition))
    Calculations.add_calc(Calculation(2,2,subtraction))
    Calculations.add_calc(Calculation(2,2,multiplication))
    Calculations.add_calc(Calculation(4,2,division))

def test_get_history(sample_calc):
    '''Checks to see if list is the correct size'''
    assert len(Calculations.get_history()) == 4, "History does not contain expected results (4)"

def test_clear_history(sample_calc):
    '''Checks to see if list is the correct size'''
    Calculations.clear_history()
    assert len(Calculations.get_history()) == 0, "History does not contain expected results (0)"

def test_get_latest(sample_calc):
    '''Test to see lastest function'''
    lastest_result = Calculations.get_latest()
    assert lastest_result.a == 4 and lastest_result.b == 2, "Latest Result does not match expected values (4,2)"

def test_get_latest_no_list(sample_calc):
    '''Test to see lastest function with no history'''
    Calculations.clear_history()
    print(f"History after clear: {Calculations.get_history()}")
    lastest_result = Calculations.get_latest()
    assert lastest_result is None, "Latest Result does not match expected values (None)"
