import os
import pkgutil
import sys

import guardian
from guardian.app import GuardianConfig

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
        """
        
        """

        try:
            subcommand = self.argv[1]
        except IndexError:
            subcommand = "help"

        if subcommand == "help":
            sys.stdout.write("Guardian Help" + "\n")
        elif subcommand == "version":
            sys.stdout.write(guardian.get_version() + "\n")
        else:
            pass

def execute(argv=None):
    """
    Start the application from the command line.
    """

    utility = ManagementUtility(argv)
    utility.execute()