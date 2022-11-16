import os

from guardian.conf import settings
from guardian.file import File

class Scanner:
    """
    The directory scanner that iterates over all files in a
    defined directory.
    """

    _files: list[File] = None

    def __init__(self):
        pass

    def get_files(self) -> list[File]:
        """
        Iterates over the GUARDED_DIRS and GUARDED_FILES provided in settings
        and retains each file as an object to be guarded.
        """

        if self._files is None:
            self._files = []

            for path in settings.guarded_dirs:
                self._walk_dirs(dir=path)

            for path in settings.guarded_files:
                self._guard_file(fullpath=path)

            self._files = sorted(self._files, key=lambda x: str(x))

        return self._files

    def _walk_dirs(self, dir: str):
        """
        Walks the provided directory, searching for files.

        Parameters
        ----------
        dir: `str`
            The directory to walk in search of files
        """

        for dirpath, _, filenames in os.walk(dir):
            for filename in filenames:
                if filename[0] == '.':
                    continue

                self._guard_file(dirpath=dirpath, filename=filename)

    def _guard_file(self, fullpath: str = None, dirpath: str = None, filename: str = None):
        """
        Creates a file object for the file, at the provided path, to be guarded.

        This function requires one of two parameter combinations.

        Option A:
            - `fullpath` is not None
            - `dirpath` is ignored
            - `filename` is ignored

        Option B:
            - `fullpath` is None
            - `dirpath` is not None
            - `filename` is not None

        Parameters
        ----------
        fullpath: `str` (optional)
            The full path to the file
        dirpath: `str` (optional)
            The path to the file
        filename: `str` (optional)
            The name of the file
        """

        if fullpath is not None:
            file = File(fullpath=fullpath)
        else:
            file = File(dirpath=dirpath, filename=filename)
        
        self._files.append(file)
