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

    @classmethod
    def clear_history(cls):
        '''Removes all elements from the list for testing'''
        cls.history.clear()

    @classmethod
    def get_latest(cls) -> Calculation:
        '''Returns the lastest calculation history'''
        if cls.history:
            return cls.history[-1]
        return None
