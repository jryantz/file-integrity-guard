import unittest

from file_integrity_guard import __version__

class TestPackage(unittest.TestCase):
    def test_version(self):
        self.assertEqual(__version__, '0.1.0')

if __name__ == '__main__':
    unittest.main()
