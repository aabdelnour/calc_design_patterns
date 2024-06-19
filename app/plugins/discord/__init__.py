from app.commands import Command


class DiscordCommand(Command):
    def execute(self):
        print("Hello, Discord!")
        