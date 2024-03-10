# pylint: disable=line-too-long
# pylint: disable=broad-except
'''App Class that displays the commands available to the user'''
import os
import sys
import pkgutil
import importlib
import logging
import logging.config
from dotenv import load_dotenv
from app.commands import CommandHandler, Command

class App:
    '''Initializes App Class'''
    def __init__(self): # Constructor
        os.makedirs('logs', exist_ok=True) #personal notes: makes the directory for logs
        self.configure_logging()
        load_dotenv()
        self.settings = self.load_environment_variables()
        self.settings.setdefault('ENVIRONMENT', 'PRODUCTION')
        self.command_handler = CommandHandler()
        self.plugins_path = 'app.plugins'

    def configure_logging(self):
        '''Configuring the Logging system'''
        logging_conf_path = 'logging.conf'
        if os.path.exists(logging_conf_path):
            logging.config.fileConfig(logging_conf_path, disable_existing_loggers=False)
        else:
            logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
        logging.info("Logging configured.")

    def load_environment_variables(self):
        '''Loads the environment variables into a dictionary'''
        settings = dict(os.environ.items())
        logging.info("Environment variables loaded.")
        return settings

    def get_environment_variable(self, env_var: str = 'ENVIRONMENT'):
        '''Retrieves environment variables '''
        return self.settings.get(env_var, None)

    def load_plugins(self):
        '''Loads plugings from plugins folder'''
        try:
            discovered_plugins = pkgutil.iter_modules([self.plugins_path.replace('.', '/')])
        except FileNotFoundError:
            logging.error("Plugins directory '%s' not found.", self.plugins_path)
            return

        for _, plugin_name, is_pkg in discovered_plugins:
            if is_pkg:
                try:
                    # Dynamically import the module based on its path
                    module = importlib.import_module(f'{self.plugins_path}.{plugin_name}')
                except ImportError as e:
                    logging.error("Failed to import plugin '%s': %s", plugin_name, e)
                    continue
                for attribute_name in dir(module):
                    attribute = getattr(module, attribute_name)
                    if isinstance(attribute, type) and issubclass(attribute, Command) and attribute is not Command:
                        try:
                            self.command_handler.register_command(plugin_name, attribute())
                            logging.info("Successfully loaded plugin '%s'", plugin_name)
                        except Exception as e:
                            logging.error("Failed to register plugin '%s': %s", plugin_name, e)

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
                logging.info("User requested to exit")
                sys.exit("Exiting")
            try:
                command_name, x, y = user_input.split()
                x = float(x)
                y = float(y)
            except ValueError:
                logging.warning("invalid input format from user %s", user_input)
                print("Invalid input format. Please enter [operation x y] \n x & y must be numbers.")
                continue

            try:
                if command_name == 'division' and y == 0:
                    logging.warning("Attempt to divide by zero with operands %f, %f", x, y)
                    print("Cannot divide by zero!!!")
                else:
                    result = self.command_handler.execute_command(command_name, x, y)
                    print("Result:", result)
                    logging.info("Executed command '%s' with operands %f, %f Result: %f", command_name, x, y, result)
            except Exception as e:
                logging.error("Error executing command '%s' with operands %f, %f: %s", command_name, x, y, str(e))
                print("An error occurred during the operation. Please try again.")
