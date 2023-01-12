from guardian.app import AppConfig
from guardian.cache import Cache
from guardian.conf import settings
from guardian.core.management.base import BaseCommand
from guardian.scanner import Scanner

class Command(BaseCommand):
    help = 'Starts the file integrity guard.'

    def add_arguments(self, parser):
        parser.add_argument(
            'path',
            action='store',
            nargs='*',
            help='file or directory paths to status',
            metavar='PATH'
        )
        parser.add_argument(
            '-q',
            '--quiet',
            action='store_true',
            help='suppresses all but the most important output',
        )
        parser.add_argument(
            '-v',
            '--verbose',
            action='store_true',
            help='verbose output',
        )

    def handle(self, *args, **options):
        # Initialize the app.
        AppConfig()

        if options['quiet']:
            settings.debug = False
        if options['verbose']:
            settings.debug = True

        if len(options['path']) == 0:
            # Iterate through all files in the settings.
            scanner = Scanner()
        else:
            # Iterate through the listed files.
            scanner = Scanner(options['path'])

        # Check and update the cache as needed.
        files = scanner.get_files()
        errors = scanner.get_errors()
        for file in files:
            cache = Cache(file)
            cache.check()
