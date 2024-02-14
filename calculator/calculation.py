'''General Calculation Class'''
class Calculation:
    '''Represents the instance of the two values and operation being call'''
    def __init__(self, a,b,operation):
        self.a = a
        self.b = b
        self.operation = operation #Stores the operation function

    def get_result(self):
        '''Calls the stored operation with two values'''
        return self.operation(self.a, self.b)
