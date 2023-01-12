import json
import os
from pathlib import Path

from guardian.app import AppConfig
from guardian.cache import Cache
from guardian.core.management.base import BaseCommand
from guardian.file import File
from guardian.scanner import Scanner

UNICODE_CHECK = u'\u2713'
UNICODE_CROSS = u'\u2717'
UNICODE_QUEST = u'\u003f'

class Command(BaseCommand):
    help = '''
    Outputs the status of one, many, or all tracked files.
    Paths containing spaces must be escaped or quoted.
    '''

    _legend: dict[str, str] = {
        UNICODE_CHECK: 'Good',
        UNICODE_CROSS: 'Damage detected',
        UNICODE_QUEST: 'Invalid path',
    }

    def add_arguments(self, parser):
        parser.add_argument(
            'path',
            action='store',
            nargs='*',
            help='file or directory paths to status',
            metavar='PATH'
        )
        parser.add_argument(
            '-o',
            '--output',
            action='store',
            default='pretty',
            type=str,
            choices=['json', 'pretty'],
            help='set the output format: pretty (default), json',
            metavar='FORMAT',
        )

    def _status_files(self, files: list[File], errors: list[Path]) -> dict[Path, str]:
        """
        Combine all files and errors into a single list so that the sorting is consistent.

        Parameters
        ----------
        files: `list[File]`
            A list of File objects representing existing files that are 
            going to be statused.
        errors: `list[Path]`
            A list of Path objects representing files or directories that
            do not exist.

        Returns
        -------
        `dict[Path, str]`
            A dictionary of paths and the status.
        """

        data: dict[Path, str] = {}
        for file in files:
            data[file.path] = UNICODE_CHECK
        for error in errors:
            data[error] = UNICODE_QUEST
        return data

    def _output_pretty_legend(self) -> list[str]:
        """
        Creates the line-by-line output to render the status legend.

        Returns
        -------
        `list[str]`
            A list of strings representing each line of output for
            the status legend.
        """

        output: list[str] = []

        # Calculate the column max length for proper padding.
        c1 = max([len(x) for x in self._legend.keys()])
        c2 = max([len(x) for x in self._legend.values()])

        # Build the legend.
        for symbol, value in self._legend.items():
            output.append(f'{symbol.ljust(c1)} {value}')
        output.append('')

        return output

    def _output_pretty_data(self, data: dict[Path, str]) -> list[str]:
        """
        Creates the line-by-line output for each file to be statused.

        Parameters
        ----------
        data: `dict[Path, str]`
            A dictionary of each file and the status of that file.

        Returns
        -------
        `list[str]`
            A list of strings representing each line of output for
            the file status.
        """

        output: list[str] = []

        # Build the data.
        paths = sorted(data.keys())
        for count, path in enumerate(paths, start=1):
            symbol = data[path]
            output.append(f'{count} [{symbol}] {path}')

        return output

    def _output_pretty(self, files: list[File], errors: list[Path]):
        """
        Compiles and then prints the data to status the requested files.

        Parameters
        ----------
        files: `list[File]`
            A list of File objects representing existing files that are 
            going to be statused.
        errors: `list[Path]`
            A list of Path objects representing files or directories that
            do not exist.
        """

        output: list[str] = []
        data: dict[Path, str] = self._status_files(files, errors)

        output.extend(self._output_pretty_legend())
        output.extend(self._output_pretty_data(data))
        print('\n'.join(output))

    def _output_json(self, files: list[File], errors: list[Path]):
        """
        Compiles and then prints the data, as json, to status the requested files.

        Parameters
        ----------
        files: `list[File]`
            A list of File objects representing existing files that are 
            going to be statused.
        errors: `list[Path]`
            A list of Path objects representing files or directories that
            do not exist.
        """

        output: list[dict[str, str]] = []
        data: dict[Path, str] = self._status_files(files, errors)

        paths = sorted(data.keys())
        for count, path in enumerate(paths, start=1):
            symbol = data[path]
            output.append({
                'path': str(path),
                'symbol': symbol,
                'status': self._legend[symbol],
            })

        print(json.dumps(output))

    def handle(self, *args, **options):
        # Initialize the app.
        AppConfig()

        if len(options['path']) == 0:
            # Iterate through all files in the settings.
            scanner = Scanner()
        else:
            # Iterate through the listed files.
            scanner = Scanner(options['path'])

        # Output the results.
        files = scanner.get_files()
        errors = scanner.get_errors()
        if options['output'] == 'json':
            # Output as json if the user are requested json.
            self._output_json(files, errors)
        else:
            # Output pretty by default.
            self._output_pretty(files, errors)
