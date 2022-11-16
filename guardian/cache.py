import os

from guardian.conf import settings
from guardian.file import File

class Cache:
    """
    The creator and manager of the cache file that stores
    the hash data.
    """

    def __init__(self, file: File):
        self._target_file = file
        self._cache_file = os.path.join(file.get_dirpath(), settings.cache_filename)

        print(self._cache_file)

    def create(self):
        """
        Creates the cache file in the folder.
        """

        pass

    def read(self):
        """
        Reads the existing file into memory for manipulation.
        """

        pass

    def update(self):
        """
        Updates the existing file from the data in memory.
        """

        pass
