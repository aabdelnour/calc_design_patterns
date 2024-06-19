from app.commands import Command


class ExitCommand(Command):
    def execute(self):
        print("Type 'exit' to exit.")
        