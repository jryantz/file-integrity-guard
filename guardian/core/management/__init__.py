import os
import pkgutil
import sys

from guardian.app import GuardianConfig

def find_commands(management_dir):
    """
    Navigates through the commands directory in the management module.
    """

    command_dir = os.path.join(management_dir, "commands")
    return [
        name
        for _, name, is_pkg in pkgutil.iter_modules([command_dir])
        if not is_pkg and not name.startswith("_")
    ]

def get_commands():
    """
    Return the command names to their callback modules.
    """

    commands = {name: "guardian.core" for name in find_commands(__path__[0])}
    return commands

class ManagementUtility:
    """
    Primary utility to control the execution flow of the application.
    """

    def __init__(self, argv=None):
        self.argv = argv or sys.argv[:]
        self.prog_name = os.path.basename(self.argv[0])
        if self.prog_name == "__main__.py":
            self.prog_name = "python -m guardian"

    def execute(self):
        print(self.argv)

def execute(argv=None):
    """
    Start the application from the command line.
    """

    utility = ManagementUtility(argv)
    utility.execute()