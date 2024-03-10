# pylint: disable=line-too-long
# pylint: disable=broad-except
'''App Class that displays the commands available to the user'''
#import os
import sys
import pkgutil
import importlib
from app.commands import CommandHandler, Command
#from dotenv import load_dotenv
#import logging
#import logging.config

class App:
    '''Initializes App Class'''
    def __init__(self): # Constructor
        self.command_handler = CommandHandler()
        self.plugins_path = 'app.plugins'

    def load_plugins(self):
        '''Loads plugings from plugins folder'''
        for _, plugin_name, is_pkg in pkgutil.iter_modules([self.plugins_path.replace('.', '/')]):
            if is_pkg:
                # Dynamically import the module based on its path
                module = importlib.import_module(f'{self.plugins_path}.{plugin_name}')
                for attribute_name in dir(module):
                    attribute = getattr(module, attribute_name)
                    if isinstance(attribute, type) and issubclass(attribute, Command) and attribute is not Command:
                    # Instantiate and register command
                        self.command_handler.register_command(plugin_name, attribute())

    def start(self):
        '''Starts the app, allowing the user to select an operation with two operands'''
        self.load_plugins()

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
