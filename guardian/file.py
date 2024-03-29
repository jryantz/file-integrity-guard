from hashlib import sha512
from pathlib import Path
from typing import Union

class File:
    """
    The object that represents each file.

    Attributes
    ----------
    _path: `Path`
        The path object representing the file.
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
        self._path = filepath.absolute()

    def __repr__(self):
        return '<%s: %s>' % (self.__class__.__name__, self.path)

    def __str__(self):
        return '%s' % (self.path)

    @property
    def name(self) -> str:
        """
        The name of the file, including the file extension.
        """

        return self._path.name

    @property
    def parent(self) -> Path:
        """
        The absolute path to the file.
        """

        return self._path.parent

    @property
    def path(self) -> Path:
        """
        The absolute file location.
        """

        return self._path

    @property
    def hash(self) -> str:
        """
        The hash of the file contents.
        """

        hash = sha512()
        with open(self.path, 'rb') as file:
            for chunk in iter(lambda: file.read(128 * hash.block_size), b''):
                hash.update(chunk)
        return hash.hexdigest()
