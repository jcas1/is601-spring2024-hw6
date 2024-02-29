# pylint: disable=line-too-long
# pylint: disable=broad-except
'''App Class that displays the commands available to the user'''
import sys
from app.commands import CommandHandler
from app.commands.operations import AddCommand, SubtractCommand, MutiplyCommand, DivisionCommand

class App:
    '''Initializes App Class'''
    def __init__(self): # Constructor
        self.command_handler = CommandHandler()

    def start(self):
        '''Starts the app, allowing the user to select an operation with two operands'''
        self.command_handler.register_command("addition", AddCommand)
        self.command_handler.register_command("subtraction", SubtractCommand)
        self.command_handler.register_command("multiplication", MutiplyCommand)
        self.command_handler.register_command("division", DivisionCommand)

        print("Please select an operation with two operands (x, y): \n")
        print("addition")
        print("subtraction")
        print("multiplication")
        print("division \n")
        print("Type 'exit' to exit.")

        while True:
            user_input = input(">>> ").strip()

            if user_input.lower() == 'exit':
                sys.exit("Exiting")
            try:
                command_name, x, y = user_input.split()
                x = float(x)
                y = float(y)
            except ValueError:
                print("Invalid input format. Please enter [operation x y] \n x & y must be numbers.")
                continue

            result = self.command_handler.execute_command(command_name, x, y)
            print("Result:", result)
