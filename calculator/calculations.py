''''Class Used to store all the previous calculation history'''

from calculator.calculation import Calculation

class Calculations:
    '''Class to store all the calculation history'''
    history: list[Calculation] = []

    @classmethod
    def add_calc(cls, calculation: Calculation):
        '''Adds the previously used calculations to the history list'''
        cls.history.append(calculation)

    @classmethod
    def get_history(cls) -> list[Calculation]:
        '''Returns the calculation history'''
        return cls.history
