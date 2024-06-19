import pkgutil
import importlib
from app.commands import CommandHandler


class App:
    def __init__(self):
        self.command_handler = CommandHandler()

    def start(self):
        self.command_handler.register_command("greet", GreetCommand())
        self.command_handler.register_command("goodbye", GoodbyeCommand())
        self.command_handler.register_command("exit", ExitCommand())
        self.command_handler.register_command("menu", MenuCommand())
        self.command_handler.register_command("discord", DiscordCommand())

        print("Type 'exit' to exit.")
        while True:
            self.command_handler.execute_command(input(">>> ").strip())
