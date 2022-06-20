from guardian.settings import BASE_DIR

class AppConfig:
    """
    Class representing the File Integrity Guard application and its
    default configuration.
    """

    def __init__(self):
        if not hasattr(self, 'name'):
            self.name = 'guardian'

        if not hasattr(self, 'verbose_name'):
            self.verbose_name = self.name.title()

        print(BASE_DIR)

    def __repr__(self):
        return '<%s: %s>' % (self.__class__.__name__, self.name)
