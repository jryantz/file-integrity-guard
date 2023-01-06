"""
Settings for the File Integrity Guard package.
"""

from pathlib import Path

# Use to build paths relative to this project.
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent

# The secret key is used as a seed in the file hash.
SECRET_KEY = ''

# Use debug mode to enable in-depth logging.
DEBUG = True

# Runtime Config

GUARDIAN_CACHE_FILENAME = '.guardian'

GUARDED_DIRS = [
    'example',
    'example/folder',
]

GUARDED_FILES = [
    'example/test1.txt',
]

GUARDED_PATHS = [
    
]

# Reporting Config

ADMINS = [

]

DEFAULT_FROM_EMAIL = ''
