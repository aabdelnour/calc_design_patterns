<<<<<<< HEAD
=======
import sys
>>>>>>> origin/plugins
from app.commands import Command


class ExitCommand(Command):
    def execute(self):
<<<<<<< HEAD
        print("Type 'exit' to exit.")
        
=======
        sys.exit("Exiting...")
>>>>>>> origin/plugins
