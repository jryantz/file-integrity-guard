import unittest
from pathlib import Path

from guardian.file import File
from guardian.scanner import Scanner

class TestScanner(unittest.TestCase):
    def test_with_example_file(self):
        example_files = [
            'example/test1.txt',
        ]

        paths: list[str] = [x for x in example_files]
        scanner = Scanner(paths)

        files: list[File] = [File(x) for x in example_files]

        scanned_files: list[str] = [str(x) for x in scanner.get_files()]
        test_files: list[str] = [str(x) for x in files]
        self.assertEqual(scanned_files, test_files)

    def test_with_example_files(self):
        example_files = [
            'example/test1.txt',
            'example/test2.txt',
            'example/folder/test3.txt',
        ]

        paths: list[str] = [x for x in example_files]
        scanner = Scanner(paths)

        files: list[File] = [File(x) for x in example_files]
        files = sorted(files, key=lambda x: str(x))

        scanned_files: list[str] = [str(x) for x in scanner.get_files()]
        test_files: list[str] = [str(x) for x in files]
        self.assertEqual(scanned_files, test_files)

    def test_with_error(self):
        example_files = [
            'example/test1.txt',
            'example/test3.txt',
        ]

        paths: list[str] = [x for x in example_files]
        scanner = Scanner(paths)

        files: list[File] = [File('example/test3.txt')]
        files = sorted(files, key=lambda x: str(x))

        error_files: list[str] = [str(x) for x in scanner.get_errors()]
        test_files: list[str] = [str(x) for x in files]
        self.assertEqual(error_files, test_files)
