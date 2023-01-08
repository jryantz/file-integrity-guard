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

UNICODE_BOXH = u'\u2500'
UNICODE_BOXV = u'\u2502'
UNICODE_BOXDR = u'\u250c'
UNICODE_BOXDL = u'\u2510'
UNICODE_BOXUR = u'\u2514'
UNICODE_BOXUL = u'\u2518'
UNICODE_BOXVR = u'\u251c'
UNICODE_BOXVL = u'\u2524'
UNICODE_BOXHD = u'\u252c'
UNICODE_BOXHU = u'\u2534'
UNICODE_BOXVH = u'\u253c'

class Command(BaseCommand):
    help = '''
    Outputs the status of one, many, or all tracked files.
    Paths containing spaces should be excaped or quoted.
    '''

    _legend: dict[str, str] = {
        UNICODE_CHECK: 'Good',
        UNICODE_CROSS: 'Damage detected',
        UNICODE_QUEST: 'Invalid path',
    }

    def add_arguments(self, parser):
        parser.add_argument(
            'path',
            nargs='*',
            help='file or directory paths to status',
        )

    def _output_legend(self) -> list[str]:
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

    def _output_data(self, data: dict[Path, str]) -> list[str]:
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
        keys = sorted(data.keys())
        for count, key in enumerate(keys, start=1):
            value = data[key]
            output.append(f'{count} [{value}] {key}')

        return output

    def _output(self, files: list[File], errors: list[Path]):
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
        
        # Combine all files and errors into a single list so that the 
        # sorting is consistent.
        data: dict[Path, str] = {}
        for file in files:
            data[file.path] = UNICODE_CHECK
        for error in errors:
            data[error] = UNICODE_QUEST

        output.extend(self._output_legend())
        output.extend(self._output_data(data))
        print('\n'.join(output))

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
        self._output(scanner.get_files(), scanner.get_errors())
