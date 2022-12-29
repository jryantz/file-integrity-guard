import os
import unittest

from guardian.cache import Cache
from guardian.file import File

class TestCacheClass(unittest.TestCase):
    def test_with_no_params(self):
        self.assertRaises(
            TypeError,
            lambda: Cache(),
        )

    def test_with_file(self):
        file = File(fullpath='example/test1.txt')
        self.assertIsInstance(
            Cache(file),
            Cache,
        )

class TestCacheFunctions(unittest.TestCase):
    def setUp(self) -> None:
        self.file: File = File(fullpath='example/test1.txt')
        cache_filename: str = '.guardtest'

        self.cache: Cache = Cache(self.file, cache_filename)

        # Check if the test cache already exists, delete if needed.
        if self.cache._cache_file.is_file():
            self.cache._cache_file.unlink()

    def tearDown(self) -> None:
        # Clean up the test cache.
        if self.cache._cache_file.is_file():
            self.cache._cache_file.unlink()

    def test_create_cache(self):
        # Create the cache.
        self.cache._create_cache()

        # Check that the cache was created.
        self.assertTrue(
            self.cache._cache_file.is_file()
        )

    def test_read_cache(self):
        # Create the cache.
        self.cache._create_cache()

        # Read the cache.
        self.assertEqual(self.cache._read_cache(), {})

    def test_update_cache(self):
        # Create the cache.
        self.cache._create_cache()

        # Update the cache.
        timestamp: str = self.cache._get_timestamp()
        hash: str = self.file.get_hash()
        self.cache._update_cache({timestamp: hash})

        # Read the cache.
        data: dict[str, str] = self.cache._read_cache()

        # Check that the hash matches.
        self.assertEqual(self.cache._get_latest_checksum(data), hash)
    
    def test_check(self):
        # Run the check.
        self.cache.check()

        # Read the cache and check that the hash matches.
        data: dict[str, str] = self.cache._read_cache()
        hash: str = self.file.get_hash()
        self.assertEqual(self.cache._get_latest_checksum(data), hash)
