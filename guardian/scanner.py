from pathlib import Path

from guardian.conf import settings
from guardian.file import File

class Scanner:
    """
    The directory scanner that iterates over all files in a
    defined directory.

    Attributes
    ----------
    _paths: `list[Path]`
        A list of all paths scanned for files or logged as files.
    _files: `list[File]`
        A list of scanned files.
    _errors: `list[Path]`
        A list of paths that are not valid or do not exist.
    """

    _paths: list[Path] = []
    _files: list[File] = []
    _errors: list[Path] = []

    def __init__(self, paths: list[Path | str] = None):
        """
        The Scanner object will iterate over a list of files and directories
        and log every file, non-recursively.

        Parameters
        ----------
        paths: `list[Path | str]` (optional)
            A list of path objects representing files or directories 
            on the file system.

            If no value is provided, the `guarded_dirs`, `guarded_files`,
            and `guarded_paths` values from the settings will be used.
        """

        # Register the paths if passed or default to the paths
        # provided in settings.
        if paths is None:
            for path in settings.guarded_dirs:
                self._paths.append(Path(path))
            for path in settings.guarded_files:
                self._paths.append(Path(path))
        else:
            self._paths = [Path(path) for path in paths]

        # Iterate through each path, check if the path is a directory
        # or file, log invalid, then save all files and walk all directories.
        for path in self._paths:
            abspath = path.absolute()
            if abspath.exists():
                if abspath.is_file():
                    self._guard_file(fullpath=abspath)
                    continue
                elif abspath.is_dir():
                    self._walk_dirs(dir=abspath)
                    continue
            self._errors.append(abspath)

        # Sort the files and errors to ensure that the list of files
        # is consistent if/when outputted to the user.
        self._files = sorted(self._files, key=lambda x: str(x))
        self._errors = sorted(self._errors, key=lambda x: str(x))

    def get_files(self) -> list[File]:
        """
        Returns a list of scanned files.
        """

        return self._files

    def get_errors(self) -> list[Path]:
        """
        Returns a list of paths that were not valid.
        """

        return self._errors

    def _walk_dirs(self, dir: Path):
        """
        Walks the provided directory, searching for files.

        Files with a leading period (`.`) are ignored.

        Parameters
        ----------
        dir: `Path`
            The directory to walk in search of files
        """

        for path in dir.iterdir():
            if path.is_file() and path.name[0] != '.':
                self._guard_file(fullpath=path)

    def _guard_file(self, fullpath: Path | str = None, dirpath: str = None, filename: str = None):
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
        fullpath: `Path` | `str` (optional)
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
