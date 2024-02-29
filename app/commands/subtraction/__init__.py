'''Operation Commands used for App'''
# pylint: disable=missing-class-docstring
from app.commands import Command
from calculator.operations import subtraction

class SubtractCommand(Command):
    def execute(self, x, y):
        return subtraction(x, y)
