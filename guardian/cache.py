import json
import time
from datetime import datetime, timezone
from pathlib import Path

from guardian.conf import settings
from guardian.file import File
from guardian.utils.log import CoreLogger

class Cache:
    """
    The creator and manager of the cache file that stores
    the hash data.
    """

    def __init__(self, file: File, cache_filename: str = None):
        if cache_filename is None:
            cache_filename = settings.cache_filename

        self._target_file: File = file
        self._cache_file: Path = Path(file.get_dirpath(), cache_filename).absolute()

    def _create_cache(self):
        """
        Creates the cache file and seed with empty JSON.
        """

        with open(self._cache_file, 'w') as file:
            json.dump({}, file)

    def _read_cache(self) -> dict[str, str]:
        """
        Reads the target file data from the cache file into memory
        for manipulation.
        """

        filename: str = str(self._target_file.get_filename())
        data: dict[str, dict[str, str]] = {}

        with open(self._cache_file, 'r') as file:
            data = json.load(file)
            
        return data.get(filename, {})

    def _update_cache(self, content: dict[str, str]):
        """
        Updates the target file data in the cache.
        """

        filename: str = str(self._target_file.get_filename())
        data: dict[str, dict[str, str]] = {}

        with open(self._cache_file, 'r') as file:
            data = json.load(file)

        data[filename] = content

        with open(self._cache_file, 'w') as file:
            json.dump(data, file)

    def _get_timestamp(self) -> str:
        """
        Returns the UTC timestamp as milliseconds since 1970.
        """

        dt = datetime.now(timezone.utc)
        ts = dt.timestamp()
        return str(round(ts * 1000))

    def _get_latest_checksum(self, data: dict[str, str]) -> str:
        """
        Returns the latest checksum in the cache.
        """

        timestamps: list[str] = sorted(data.keys())
        if len(timestamps) > 0:
            timestamp: str = max(timestamps)
            return data[timestamp]
        return ''

    def check(self):
        """
        Checks the cache take the actions necessary to make sure the
        hash is checked and logged.
        """

        # Create the cache file if it doesn't exist.
        cache_file: Path = Path(self._cache_file)
        if not cache_file.is_file():
            self._create_cache()

        # Read the cache and store temporarily.
        timestamp: str = self._get_timestamp()
        cache_data: dict[str, str] = self._read_cache()

        # Get the latest cached checksum and the current checksum.
        cache_checksum: str = self._get_latest_checksum(cache_data)
        current_checksum: str = self._target_file.get_hash()

        # Check if the checksum has changed.
        if current_checksum == cache_checksum:
            # If the checksum hasn't changed, log to debug.
            CoreLogger().logger.info('match %s' % self._target_file)
        if current_checksum != cache_checksum:
            # If the checksums don't match, add then alert.
            cache_data[timestamp] = current_checksum
            self._update_cache(cache_data)

            CoreLogger().logger.warning('change %s' % self._target_file)
