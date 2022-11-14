import unittest

from guardian.file import File

class TestFile(unittest.TestCase):
    def test_with_no_params(self):
        self.assertRaises(
            ValueError,
            lambda: File(),
        )

    def test_with_partial_separated_path_1(self):
        self.assertRaises(
            ValueError,
            lambda: File(dirpath='../example'),
        )

    def test_with_partial_separated_path_2(self):
        self.assertRaises(
            ValueError,
            lambda: File(filename='test1.txt'),
        )

    def test_with_full_and_separated_path_1(self):
        self.assertRaises(
            ValueError,
            lambda: File(fullpath='../example/test1.txt', dirpath='../example'),
        )

    def test_with_full_and_separated_path_2(self):
        self.assertRaises(
            ValueError,
            lambda: File(fullpath='../example/test1.txt', filename='test1.txt'),
        )

    def test_with_full_and_separated_path_3(self):
        self.assertRaises(
            ValueError,
            lambda: File(fullpath='../example/test1.txt', dirpath='../example', filename='test1.txt'),
        )

    def test_with_full_path(self):
        self.assertIsInstance(
            File(fullpath='../example/test1.txt'),
            File,
        )

    def test_with_separated_path(self):
        self.assertIsInstance(
            File(dirpath='../example', filename='test1.txt'),
            File,
        )
