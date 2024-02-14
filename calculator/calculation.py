# pylint: disable=too-few-public-methods

'''General Calculation Class'''
class Calculation:
    '''Represents the instance of the two values and operation being called'''
    def __init__(self, a,b,operation):
        #Initialized a Calcuation Object
        self.a = a
        #The first operand
        self.b = b
        #The second operand
        self.operation = operation
        #Stores the operation function

    def get_result(self):
        '''Computes and returns the result of the stores operation and operands'''
        return self.operation(self.a, self.b)
