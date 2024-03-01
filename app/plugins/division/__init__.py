'''Operation Commands used for App'''
# pylint: disable=missing-class-docstring
from app.commands import Command
from calculator.operations import addition, subtraction, multiplication, division

class DivisionCommand(Command):
    def execute(self, x, y):
        return division(x, y)
