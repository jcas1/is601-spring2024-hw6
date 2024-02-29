'''Operation Commands used for App'''
# pylint: disable=missing-class-docstring
from app.commands import Command
from calculator.operations import addition, subtraction, multiplication, division

class AddCommand(Command):
    def execute(self, x, y):
        return addition(x, y)

class SubtractCommand(Command):
    def execute(self, x, y):
        return subtraction(x, y)

class MutiplyCommand(Command):
    def execute(self, x, y):
        return multiplication(x, y)

class DivisionCommand(Command):
    def execute(self, x, y):
        return division(x, y)
