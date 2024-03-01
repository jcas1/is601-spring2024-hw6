'''Operation Commands used for App'''
# pylint: disable=missing-class-docstring
from app.commands import Command
from calculator.operations import multiplication

class MutiplyCommand(Command):
    def execute(self, x, y):
        return multiplication(x, y)
