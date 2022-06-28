import sqlite3

class DbConfig:
    """
    Class representing the File Integrity Guard database and its
    default configuration.
    """

    def __init__(self):
        if not hasattr(self, 'name'):
            self.name = 'db.sqlite3'

        conn = sqlite3.connect(self.name)

    def __repr__(self):
        return '<%s: %s>' % (self.__class__.__name__, self.name)