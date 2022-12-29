from guardian.utils.log import CoreLogger

class AppConfig:
    """
    Class representing the File Integrity Guard application and its
    default configuration.
    """

    def __new__(self):
        if not hasattr(self, 'instance'):
            self.instance = super(AppConfig, self).__new__(self)
        return self.instance

    def __init__(self):
        if not hasattr(self, 'name'):
            self.name = 'guardian'

        if not hasattr(self, 'verbose_name'):
            self.verbose_name = self.name.title()

    def __repr__(self):
        return '<%s: %s>' % (self.__class__.__name__, self.name)
