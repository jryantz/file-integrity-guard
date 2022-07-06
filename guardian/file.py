

class File():
    """
    The object that represents each file.
    """

    def __init__(self, location: str):
        """
        Initializes the File object with the absolute file
        location.

        Parameters
        ----------
        location: `str`
            The absolute file path
        """

        self._location = location

    def get_location(self) -> str:
        """
        Returns the absolute file location.

        Returns
        -------
        `str`
            The absolute file path
        """

        return self._location