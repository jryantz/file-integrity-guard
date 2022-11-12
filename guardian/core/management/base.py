

import guardian

class BaseCommand:
    """
    
    """

    # Metadata about this command.
    help = ""

    def get_version(self):
        return guardian.get_version()
