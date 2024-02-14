from calculator.calculation import Calculation

class calc_history:
    history: list[Calculation] = []

    @classmethod
    def add_calc(cls, calculation:Calculation)
        '''Adds the previously used calculation to the history list'''
        cls.history.append(calculation)
    
    @classmethod
    def get_history(cls) -> List[Calculation]:
        '''Returns the calculation history'''
        return cls.history
