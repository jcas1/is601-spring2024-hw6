#pylint: disable=unnecessary-pass
'''CommandHandler'''
class Command:
    '''A base class for commands that provides an execute methods using x and y as parameters'''
    def execute(self, x, y):
        '''
        Executes a command with its given parameters
            x & y should be numbers
        '''
        pass

class CommandHandler:
    '''Handler class used to manage and execute registerd commands'''

    def __init__(self):
        '''Initializes itself with a blank dictionary'''
        self.operations = {}

    def register_command(self, name: str, command):
        '''Used to register a command with a given name'''
        self.operations[name] = command

    def execute_command(self, command, x, y):
        '''Used to execute a command using x and y'''
        try:
            return self.operations[command].execute(self, x, y)
        except KeyError:
            print("Command does not exist")
            return None
        except ZeroDivisionError as e:
            return e  # Return the ZeroDivisionError instance)
