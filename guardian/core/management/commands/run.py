

from guardian.app import AppConfig
from guardian.cache import Cache
from guardian.core.management.base import BaseCommand
from guardian.scanner import Scanner

class Command(BaseCommand):
    help = "Starts the file integrity guard."

    def handle(self, *args, **options):
        # Initialize the app.
        AppConfig()

        # Create a list of the files to be scanned.
        scanner = Scanner()
        files = scanner.get_files()
        for file in files:
            cache = Cache(file)
            cache.check()
