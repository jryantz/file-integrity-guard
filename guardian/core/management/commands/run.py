

from guardian.app import GuardianConfig
from guardian.core.management.base import BaseCommand
from guardian.scanner import Scanner

class Command(BaseCommand):
    help = "Starts the file integrity guard."

    def handle(self, *args, **options):
        # Initialize the app.
        GuardianConfig()

        # Create a list of the files to be scanned.
        scanner = Scanner()
        files = scanner.get_files()

        for file in files:
            print(file)
