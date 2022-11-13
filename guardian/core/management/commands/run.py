

from guardian.core.management.base import BaseCommand

class Command(BaseCommand):
    help = "Starts the file integrity guard."

    def handle(self, *args, **options):
        print("handle(...)", args, options)
