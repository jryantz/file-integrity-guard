import unittest

from guardian import __version__

class TestPackage(unittest.TestCase):
    def test_version(self):
        self.assertEqual(__version__, "0.1.0-alpha.1")
