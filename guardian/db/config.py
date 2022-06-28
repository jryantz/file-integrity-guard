import sqlite3

class DbConfig:
    """
    Class representing the File Integrity Guard database and its
    default configuration.
    """

    def __init__(self):
        if not hasattr(self, 'name'):
            self.name = 'guardian'

        if not hasattr(self, 'verbose_name'):
            self.verbose_name = self.name.title()

        conn = sqlite3.connect('db.sqlite3')

    def __repr__(self):
        return '<%s: %s>' % (self.__class__.__name__, self.name)