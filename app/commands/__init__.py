from abc import ABC, abstractmethod

<<<<<<< HEAD
from distutils.cmd import Command

class command(ABC):
=======
class Command(ABC):
>>>>>>> origin/plugins
    @abstractmethod
    def execute(self):
        pass

class CommandHandler:
    def __init__(self):
        self.commands = {}

<<<<<<< HEAD
    def register_command(self, comman_name: str, command: Command):
        self.commands[command_name] = command
    
    def execute_command(self, command_name: str):
=======
    def register_command(self, command_name: str, command: Command):
        self.commands[command_name] = command

    def execute_command(self, command_name: str):
        """ Look before you leap (LBYL) - Use when its less likely to work
>>>>>>> origin/plugins
        if command_name in self.commands:
            self.commands[command_name].execute()
        else:
            print(f"No such command: {command_name}")
<<<<<<< HEAD
=======
        """
        """Easier to ask for forgiveness than permission (EAFP) - Use when its going to most likely work"""
        try:
            self.commands[command_name].execute()
        except KeyError:
            print(f"No such command: {command_name}")
>>>>>>> origin/plugins

