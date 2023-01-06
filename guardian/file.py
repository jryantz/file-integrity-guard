from hashlib import sha512
from pathlib import Path
from typing import Union

class File:
    """
    The object that represents each file.
    """

    def __init__(self, fullpath: Path | str = None, dirpath: str = None, filename: str = None):
        """
        Creates a file object for the file, at the provided path, to be guarded.

        This function requires one of two parameter combinations.

        Full Path:
            - `fullpath` is not None
            - `dirpath` is None
            - `filename` is None

        Separated Path:
            - `fullpath` is None
            - `dirpath` is not None
            - `filename` is not None

        Parameters
        ----------
        fullpath: `Path` | `str` (optional)
            The full path to the file
        dirpath: `str` (optional)
            The path to the file
        filename: `str` (optional)
            The name of the file
        """

        # Throw error if all params are None
        if (
            fullpath is None and
            dirpath is None and
            filename is None
        ): raise ValueError('Parameter values must be provided: fullpath -OR- dirpath and filename')

        # Throw error if fullpath is None -AND- dirpath or filename is None
        if (
            fullpath is None and (
                dirpath is None or
                filename is None
            )
        ): raise ValueError('dirpath and filename must both be provided')

        # Throw error if fullpath is not None -AND- dirpath and/or filename is not None:
        if (
            fullpath is not None and (
                dirpath is not None or
                filename is not None
            )
        ): raise ValueError('Parameter values must be provided: fullpath -OR- dirpath and filename')

        if fullpath is None:
            filepath = Path(dirpath, filename)
        else:
            filepath = Path(fullpath)
        abspath = filepath.absolute()
        
        self._dirpath = abspath.parent
        self._filename = abspath.name

    def __repr__(self):
        return '<%s: %s>' % (self.__class__.__name__, self.get_location())

    def get_dirpath(self) -> str:
        """
        Returns the absolute path to the file

        Returns
        -------
        `str`
            The absolute path to the file
        """

        return self._dirpath

    def get_filename(self) -> str:
        """
        Returns the name of the file

        Returns
        -------
        `str`
            The name of the file
        """

        return self._filename

    def get_location(self) -> Path:
        """
        Returns the absolute file location.

        Returns
        -------
        `str`
            The absolute file path
        """

        dirpath = self.get_dirpath()
        filename = self.get_filename()
        return Path(dirpath, filename)

    def get_hash(self) -> str:
        """
        Returns the file hash.

        Returns
        -------
        `str`
            The hash of the file contents
        """

        hash = sha512()
        filepath = self.get_location()
        with open(filepath, 'rb') as file:
            for chunk in iter(lambda: file.read(128 * hash.block_size), b''):
                hash.update(chunk)
        return hash.hexdigest()
