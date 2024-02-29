'''Testing Commands'''
from app.commands.operations import AddCommand, SubtractCommand, MutiplyCommand, DivisionCommand

def test_add_command():
    '''Testing Add Command'''
    command = AddCommand()
    assert command.execute(3,3) == 6

def test_subtract_command():
    '''Testing Subtract Command'''
    command = SubtractCommand()
    assert command.execute(3,3) == 0

def test_mutiply_command():
    '''Testing Mutiply Command'''
    command = MutiplyCommand()
    assert command.execute(3,3) == 9

def test_division_command():
    '''Testing Division Command'''
    command = DivisionCommand()
    assert command.execute(3,3) == 1
