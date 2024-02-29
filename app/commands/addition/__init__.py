'''Operation Commands used for App'''
# pylint: disable=missing-class-docstring
from app.commands import Command
from calculator.operations import addition

class AddCommand(Command):
    def execute(self, x, y):
        return addition(x, y)
